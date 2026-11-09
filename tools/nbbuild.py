"""Build a student notebook and an instructor solution notebook from one lab source.

A lab source is a Python file (kept in the private instructor repository) that does:

    from nbbuild import Lab
    lab = Lab("Lab 4A - PCA I", "modules/m04-pca/lab/lab4a_pca_theory.ipynb")
    lab.md("## Part 1 ...")
    lab.code("given code that students run")
    lab.task("T1", '''
    partial code students see
    ### BEGIN SOLUTION
    solution code (removed from the student notebook)
    ### END SOLUTION
    ''')
    lab.check("T1", "assert ...")            # self-check that depends on task T1
    lab.answer("Q1", "prompt", "model answer and marking notes")
    lab.build(student_path, solution_path)

Tags written into cell metadata:
  setup  - first code cell (installs/checks the environment)
  task   - student must write code; contains `raise NotImplementedError()` in the student copy
  check  - self-check assertions for a task
  answer - written answer (markdown)
Every task/check/answer cell also carries metadata {"tsds": {"id": ...}} so tests can match
student and solution notebooks one-to-one.

Rule for authors: cells that are not tagged task/check must run without any task being solved.
The public CI executes the student notebook with task and check cells removed.
"""
import hashlib
import re
import textwrap

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

REPO = "pasdptt/public_teaching_tools4DS"
DEFAULT_REF = "main"

SOL_RE = re.compile(r"^([ \t]*)### BEGIN SOLUTION\n(.*?)^[ \t]*### END SOLUTION\n?", re.S | re.M)

SETUP = '''# Setup: run this cell first (Google Colab or a local Jupyter kernel).
COURSE_REF = "{ref}"  # version of the course repository to install the helper package from
try:
    import tsds
except ImportError:  # first run in a fresh Colab runtime: install the course helper package
    import subprocess, sys
    subprocess.run([sys.executable, "-m", "pip", "install", "-q",
                    f"tsds @ git+https://github.com/{repo}@{{COURSE_REF}}#subdirectory=src"], check=True)
    import tsds

tsds.env.check()          # prints versions; warns if a package is outside the tested range
SEED = tsds.seed_everything()
rng = tsds.rng()'''


def _dedent(s: str) -> str:
    return textwrap.dedent(s).strip("\n")


class Lab:
    def __init__(self, title: str, repo_path: str, ref: str = DEFAULT_REF, extra_imports: str = ""):
        self.title = title
        self.repo_path = repo_path
        self.ref = ref
        self.cells = []  # (kind, id, student_cell, solution_cell)
        badge = (f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
                 f"(https://colab.research.google.com/github/{REPO}/blob/{ref}/{repo_path})")
        self._add("header", None, "markdown", f"{badge}\n\n# {title}")
        setup = SETUP.format(ref=ref, repo=REPO)
        if extra_imports:
            setup += "\n\n" + _dedent(extra_imports)
        self._add("setup", None, "code", setup, tags=["setup"])

    def _add(self, kind, cid, ctype, student, solution=None, tags=None):
        solution = student if solution is None else solution
        mk = new_markdown_cell if ctype == "markdown" else new_code_cell
        s, t = mk(student), mk(solution)
        for c in (s, t):
            if tags:
                c.metadata["tags"] = list(tags)
            if cid:
                c.metadata["tsds"] = {"id": cid}
        self.cells.append((kind, cid, s, t))

    def md(self, text: str):
        self._add("md", None, "markdown", _dedent(text))

    def code(self, src: str):
        src = _dedent(src)
        if "### BEGIN SOLUTION" in src:
            raise ValueError("Use task() for cells that contain solutions.")
        self._add("code", None, "code", src)

    def task(self, cid: str, src: str):
        src = _dedent(src) + "\n"
        if not SOL_RE.search(src):
            raise ValueError(f"Task {cid} has no ### BEGIN/END SOLUTION block.")
        student = SOL_RE.sub(lambda m: f"{m.group(1)}# YOUR CODE HERE\n{m.group(1)}raise NotImplementedError()\n", src).rstrip("\n")
        solution = SOL_RE.sub(lambda m: m.group(2), src).rstrip("\n")
        self._add("task", cid, "code", f"# Task {cid}\n{student}", f"# Task {cid}\n{solution}", tags=["task"])

    def check(self, cid: str, src: str):
        self._add("check", cid, "code", f"# Self-check for task {cid}: run it; it should print OK.\n{_dedent(src)}",
                  tags=["check"])

    def answer(self, cid: str, prompt: str, model_answer: str):
        prompt = _dedent(prompt)
        student = f"**{cid}.** {prompt}\n\n*Your answer:* "
        solution = f"**{cid}.** {prompt}\n\n**Model answer and marking notes:**\n\n{_dedent(model_answer)}"
        self._add("answer", cid, "markdown", student, solution, tags=["answer"])

    def _notebook(self, which: int):
        nb = new_notebook()
        nb.metadata = {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
            "colab": {"provenance": []},
        }
        for i, (_, _, s, t) in enumerate(self.cells):
            cell = (s, t)[which].copy()
            cell["id"] = hashlib.sha1(f"{self.repo_path}:{i}".encode()).hexdigest()[:12]
            nb.cells.append(cell)
        nbformat.validate(nb)
        return nb

    def build(self, student_path: str, solution_path: str):
        nbformat.write(self._notebook(0), student_path)
        nbformat.write(self._notebook(1), solution_path)
        n = {k: sum(1 for c in self.cells if c[0] == k) for k in ("task", "check", "answer")}
        print(f"built {student_path} and {solution_path}: {n}")
