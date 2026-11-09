# Getting started (students)

All labs run in **Google Colab** in your browser. You do not need to install anything, mount Google Drive or create a Kaggle account.

## Opening a lab

1. Go to the module folder for the week (see the [schedule](schedule.md)) and click **Open in Colab** on the lab.
2. In Colab choose **File → Save a copy in Drive**, so that your work is saved under your account.
3. Run the **setup cell** (the first code cell). On the first run in a new Colab session it installs the small course helper package `tsds`, which takes a few seconds. It then prints a table of package versions.
   * If a line says `outside tested range`, the lab will probably still work. If something fails, include that table when you ask for help.

## While you work

* Complete the cells marked **Task** by replacing `raise NotImplementedError()` with your code.
* Run the **Self-check** cell under each task; it prints `OK` when your answer is consistent.
  * Self-checks catch typical mistakes, but they do not mark your interpretation.
  * The written answers marked **Q** carry half of each lab's marks.
* Do not change the given code cells unless a task tells you to.
* Use the course seed (`SEED`, `rng`) wherever a function takes `random_state`, so your results can be reproduced.

## Before you submit

1. Choose **Runtime → Restart session and run all** (called *Restart and run all* in some Colab versions).
2. Check that **every cell ran top to bottom without errors**. Notebooks that only work when cells are run out of order receive the lowest reproducibility mark.
3. Fill in the **AI-use log** at the end (write "None" if you used no AI tool); see the [AI policy](ai-policy.md).
4. Download the notebook (**File → Download → .ipynb**) and submit it through the course's submission channel *(to be announced by the lecturer)*.

## Working offline (optional fallback)

If Colab is unavailable, the same notebooks run on a laptop with Python 3.12. Run each command from the repository root.

Create an environment with the pinned package versions:

```bash
uv venv -p 3.12 .venv
```

```bash
uv pip install -p .venv/bin/python -r environment/requirements-local.txt -e src
```

Start Jupyter from that environment:

```bash
.venv/bin/python -m jupyter lab
```

`jupyter lab` is not included in the pinned list; install `jupyterlab` into the environment first if you want it.
