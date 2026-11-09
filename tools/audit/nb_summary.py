import json, sys, re
nb = json.load(open(sys.argv[1])); mdmax=int(sys.argv[2]) if len(sys.argv)>2 else 200
for i,c in enumerate(nb["cells"]):
    src="".join(c.get("source",[]))
    if c["cell_type"]=="markdown":
        s=re.sub(r"\s+"," ",src)[:mdmax]; print(f"[{i}] MD: {s}")
    else:
        print(f"[{i}] CODE[{c.get('execution_count')}]:\n{src}")
        for o in c.get("outputs",[]):
            ot=o.get("output_type")
            if ot=="error": print(f"   !! {o['ename']}: {o['evalue'][:200]}")
            elif ot=="stream": print("   >>", "".join(o['text'])[:160].replace("\n"," | "))
            else:
                d=o.get("data",{})
                t="".join(d.get("text/plain",[]))[:160].replace("\n"," | ")
                print(f"   >> {'IMG ' if 'image/png' in d else ''}{t}")
