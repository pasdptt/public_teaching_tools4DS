"""Repository-structure checks: modules are complete and documented, and every documentation link resolves."""
import re
import unicodedata
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MODULES = sorted(p for p in (ROOT / "modules").iterdir() if p.is_dir() and not p.name.startswith("_"))
DOCS = sorted([ROOT / "README.md", *ROOT.glob("course/*.md"), *ROOT.glob("modules/**/*.md"), *ROOT.glob("docs/**/*.md"),
               *ROOT.glob("datasets/*.md"), *ROOT.glob("tools/**/*.md")])
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")


def _slug(heading: str) -> str:
    """GitHub-style heading anchor."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)       # links -> link text
    text = text.replace("`", "").replace("*", "").strip().lower()
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat.startswith("L") or cat.startswith("N") or cat.startswith("M"):
            out.append(ch)
    return "".join(out).replace(" ", "-")


def _anchors(md: Path) -> set:
    anchors, in_code = set(), False
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and re.match(r"#{1,6} ", line):
            anchors.add(_slug(line.lstrip("#").strip()))
    return anchors


@pytest.mark.parametrize("module", MODULES, ids=lambda p: p.name)
def test_module_readme(module):
    readme = module / "README.md"
    assert readme.exists(), "every module needs a README.md"
    text = readme.read_text(encoding="utf-8")
    assert re.search(r"^\| Status \|", text, re.M), "README must start with the status table"
    for section in ("Objectives", "Datasets", "Assessment"):
        assert re.search(rf"^## .*{section}", text, re.M | re.I), f"missing a '## ...{section}...' section"


@pytest.mark.parametrize("module", MODULES, ids=lambda p: p.name)
def test_module_in_schedule(module):
    schedule = (ROOT / "course/schedule.md").read_text(encoding="utf-8")
    assert f"../modules/{module.name}/" in schedule, "every module must be linked from course/schedule.md"
    built = re.search(rf"\[{re.escape(module.name)}\].*\|\s*\*\*(Pilot built|Built)\*\*", schedule)
    if built:
        assert list((module / "lab").glob("*.ipynb")), "a built module must contain its lab notebooks"


@pytest.mark.parametrize("md", DOCS, ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_resolve(md):
    text = md.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)                 # ignore code blocks
    problems = []
    for target in LINK.findall(text):
        if re.match(r"^[a-z]+:", target):                                 # http(s), mailto, etc.
            continue
        path, _, anchor = target.partition("#")
        dest = (md.parent / path).resolve() if path else md
        if not dest.exists():
            problems.append(f"missing file: {target}")
        elif anchor and dest.suffix == ".md" and anchor not in _anchors(dest):
            problems.append(f"missing anchor: {target}")
    assert not problems, "; ".join(problems)
