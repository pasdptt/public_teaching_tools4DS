# Authoring guide (staff)

How to produce a module so that it meets the [definition of done](blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module). The PCA pilot ([`../modules/w05-w06-pca/`](../modules/w05-w06-pca/)) is the worked example of every step.

## 1. Folder layout of a module

Copy [`../modules/_template/`](../modules/_template/) to `modules/wNN-<topic>/` and keep this structure:

```
modules/wNN-<topic>/
├── README.md              status table, objectives, lesson plan, datasets, legacy material, assessment links
├── lecture/outline.md     equations, assumptions, worked examples (numbers produced by code), misconception checks
├── lab/labNN_<name>.ipynb STUDENT notebook — generated, never edited by hand
├── exercises/             problem-set.md, misconception-checks.md (questions only)
├── references.md          every DOI checked against Crossref
└── EXECUTION-REPORT.md    environments, test results, cross-environment comparison, mutation tests
```

**Private material** goes in the instructor repository (currently the git-ignored `instructor/` folder): lab sources, solutions, answer keys and examination items. The public repository never contains solutions.

## 2. Writing a lab: one source, two notebooks

Write each lab once, as a Python source file in `instructor/<module>/src/labNN.py`, using [`../tools/nbbuild.py`](../tools/nbbuild.py):

```python
lab = Lab("Lab NN — Title", "modules/wNN-topic/lab/labNN_name.ipynb", extra_imports="import numpy as np")
lab.md("## Part 1 ...")                      # explanation
lab.code("given code students run")          # must work WITHOUT any task being solved
lab.task("T1", '''
student scaffold
### BEGIN SOLUTION
solution code (removed in the student copy, indentation preserved)
### END SOLUTION
''')
lab.check("T1", "assert ...; print('OK')")   # self-check for that task
lab.answer("Q1", "prompt", "model answer + marking notes")
lab.build(student_path, solution_path)
```

Building writes the public student notebook (Colab badge, setup cell, no outputs) and the private solution notebook. Both come from the same source, so the questions and solutions cannot drift apart.

## 3. Rules for lab content

1. **Given cells must run without solutions.** CI executes the student notebook with task and check cells removed.
2. **Seed everything:** use `SEED` and `rng` from the setup cell. Pass `random_state=SEED` to every estimator that accepts it, including `PCA` on wide data (scikit-learn switches to a randomised solver).
3. **Load data only through the registry** (`tsds.data.load`). Add new datasets to [`../src/tsds/registry.yaml`](../src/tsds/registry.yaml) with source, DOI, creators, licence, how and when it was verified, a citation, and a SHA-256 checksum if downloaded.
4. **Every fitted step goes inside the validation boundary**, and **every comparison has a baseline and an uncertainty estimate**.
5. **Every lab ends with failure analysis and an interpretation question**, and has an AI-use log cell.
6. **Self-checks must catch typical mistakes.** Write a mutation test (see `instructor/w05-w06-pca/mutation_test.py`) that injects them; every one must make its check fail.
7. **Numbers quoted in lectures and keys come from code** run in both CI environments (see `instructor/w05-w06-pca/facts.py`).
8. **Write original text.** Cite sources; do not copy tutorial or blog prose (audit P2).

## 4. Dependencies

A module that needs a new package must add it to **both** `environment/requirements-local.in` and `environment/requirements-colab-proxy.in`. Then recompile each environment from the repository root:

```bash
uv pip compile environment/requirements-local.in -p 3.12 -o environment/requirements-local.txt
```

```bash
uv pip compile environment/requirements-colab-proxy.in -p 3.12 -o environment/requirements-colab-proxy.txt
```

Packages that are not preinstalled in Colab must also be installable by the lab's setup cell. Prefer libraries already in Colab and the scikit-learn stack. Avoid TensorFlow, PyTorch and Spark in required work.

## 5. Testing

Rebuild a lab from its source:

```bash
python instructor/<module>/src/labNN.py
```

Run the notebook tests (the solution tests run only when `instructor/` is present):

```bash
python -m pytest -q tests
```

Run the structure checks alone:

```bash
python -m pytest -q tests/test_structure.py
```

CI ([`../.github/workflows/notebooks.yml`](../.github/workflows/notebooks.yml)) runs the public tests in both pinned environments on every push and weekly.

## 6. Finishing a module

1. Fill in `EXECUTION-REPORT.md` (copy the pilot's sections).
2. Change the status in the module README and in [`../course/schedule.md`](../course/schedule.md) from *Planned* to *Built*.
3. Have the lab trialled for timing (3 h), and record the result.
