import json, sys, re
def txt(c):
    out=[]
    for o in c.get("outputs",[]):
        if o.get("output_type")=="stream" and o.get("name")=="stdout": out.append("".join(o["text"]))
        elif o.get("output_type") in ("execute_result",): out.append("".join(o.get("data",{}).get("text/plain","")))
    s="".join(out); s=re.sub(r"0x[0-9a-f]+","0x",s); return s.strip()
a=json.load(open(sys.argv[1])); b=json.load(open(sys.argv[2]))
same=diff=0; ex=[]
for i,(ca,cb) in enumerate(zip(a["cells"],b["cells"])):
    if ca["cell_type"]!="code": continue
    ta,tb=txt(ca),txt(cb)
    if not ta or not tb: continue
    if ta==tb: same+=1
    else:
        diff+=1
        if len(ex)<4: ex.append(f"cell {i}: orig={ta[:70]!r} | rerun={tb[:70]!r}")
print(f"{sys.argv[1].split('/')[-1]}: comparable text outputs identical={same} different={diff}")
for e in ex: print("   ",e.replace("\n"," "))
