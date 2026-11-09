"""Notebook checks run in CI for every environment in environment/.

Public checks (always run):
  * student notebooks are valid, have no stored outputs, start with the Colab badge and setup cell;
  * every task cell raises NotImplementedError until solved;
  * the student notebook executes top to bottom in a fresh kernel once task and check cells are removed
    (i.e. all given code works without hidden state and without solutions).

Instructor checks (run only when the private instructor/ folder is present):
  * every solution notebook executes top to bottom without errors, including all self-checks;
  * student and solution notebooks contain the same task, check and answer ids in the same order.
"""
import copy
import os
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
STUDENT = sorted(ROOT.glob("modules/*/lab/*.ipynb"))
INSTRUCTOR = ROOT / "instructor"
KERNEL = os.environ.get("TSDS_KERNEL", "python3")
TIMEOUT = int(os.environ.get("TSDS_CELL_TIMEOUT", "600"))


def _tags(cell):
    return set(cell.get("metadata", {}).get("tags", []))


def _ids(nb):
    return [(sorted(_tags(c) & {"task", "check", "answer"}), c["metadata"]["tsds"]["id"])
            for c in nb.cells if "tsds" in c.get("metadata", {})]


def _execute(nb, tmp_path):
    client = NotebookClient(nb, timeout=TIMEOUT, kernel_name=KERNEL, resources={"metadata": {"path": str(tmp_path)}})
    client.execute()
    return nb


def _solution_for(student_path: Path) -> Path:
    rel = student_path.relative_to(ROOT / "modules")
    return INSTRUCTOR / "solutions" / rel.parent.parent / rel.name.replace(".ipynb", "_solution.ipynb")


@pytest.mark.parametrize("path", STUDENT, ids=lambda p: p.name)
def test_student_structure(path):
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    assert "colab.research.google.com/github/" in nb.cells[0].source, "first cell must hold the Open-in-Colab badge"
    assert "setup" in _tags(nb.cells[1]), "second cell must be the setup cell"
    for c in nb.cells:
        if c.cell_type == "code":
            assert not c.outputs and c.execution_count is None, "student notebooks are committed without outputs"
            assert "### BEGIN SOLUTION" not in c.source and "### END SOLUTION" not in c.source
        if "task" in _tags(c):
            assert "raise NotImplementedError()" in c.source


@pytest.mark.parametrize("path", STUDENT, ids=lambda p: p.name)
def test_student_given_code_executes(path, tmp_path):
    nb = nbformat.read(path, as_version=4)
    nb.cells = [c for c in nb.cells if not (_tags(c) & {"task", "check"})]
    _execute(nb, tmp_path)


@pytest.mark.skipif(not INSTRUCTOR.exists(), reason="instructor material is private")
@pytest.mark.parametrize("path", STUDENT, ids=lambda p: p.name)
def test_solution_matches_and_executes(path, tmp_path):
    sol_path = _solution_for(path)
    assert sol_path.exists(), f"missing solution {sol_path}"
    student, solution = nbformat.read(path, as_version=4), nbformat.read(sol_path, as_version=4)
    assert _ids(student) == _ids(solution), "student and solution notebooks must have the same task/check/answer ids"
    executed = _execute(copy.deepcopy(solution), tmp_path)
    counts = [c.execution_count for c in executed.cells if c.cell_type == "code"]
    assert counts == list(range(1, len(counts) + 1)), "solution must run strictly top to bottom"
    out_dir = INSTRUCTOR / "executed"
    out_dir.mkdir(exist_ok=True)
    nbformat.write(executed, out_dir / sol_path.name)
