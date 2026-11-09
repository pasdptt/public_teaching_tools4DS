"""Execute a notebook cell-by-cell with errors captured. usage: runnb.py <in.ipynb> <out.ipynb> <cwd> <mode>"""
import sys, re, time, json, os, nbformat
from nbclient import NotebookClient
src, out, cwd, mode = sys.argv[1:5]
nb = nbformat.read(src, as_version=4)
skipped = []
for i, c in enumerate(nb.cells):
    if c.cell_type != "code": continue
    lines = c.source.split("\n"); new = []
    for l in lines:
        if re.match(r"^\s*(!|%pip|%%bash)", l):
            skipped.append((i, l.strip()[:120])); new.append(re.match(r"^\s*", l).group(0) + "pass  # [audit] shell command not executed: " + l.strip()[:80].replace("\\", "/"))
        else: new.append(l)
    c.source = "\n".join(new)
for c in nb.cells:
    if c.cell_type == "code": c.outputs = []; c.execution_count = None
t0 = time.time()
client = NotebookClient(nb, timeout=1500, kernel_name=os.environ.get("AUDIT_KERNEL","audit312"), allow_errors=True, resources={"metadata": {"path": cwd}})
status = "completed"
try: client.execute()
except Exception as e: status = f"aborted: {type(e).__name__}: {str(e)[:200]}"
elapsed = time.time() - t0
nbformat.write(nb, out)
cells = []
for i, c in enumerate(nb.cells):
    if c.cell_type != "code": continue
    errs = [o for o in c.get("outputs", []) if o.get("output_type") == "error"]
    warns = [o for o in c.get("outputs", []) if o.get("output_type") == "stream" and o.get("name") == "stderr"]
    cells.append({"cell": i, "error": (errs[0]["ename"] + ": " + errs[0]["evalue"][:220]) if errs else None,
                  "stderr": ("".join(w["text"] for w in warns)[:300]) if warns else None})
rep = {"notebook": os.path.basename(src), "mode": mode, "status": status, "seconds": round(elapsed, 1),
       "code_cells": len(cells), "error_cells": sum(1 for c in cells if c["error"]), "skipped_shell_lines": skipped, "cells": cells}
json.dump(rep, open(out + ".report.json", "w"), ensure_ascii=False, indent=1)
print(f"{rep['notebook']} [{mode}] {status} {rep['seconds']}s errors={rep['error_cells']}/{rep['code_cells']} shell_skipped={len(skipped)}")
