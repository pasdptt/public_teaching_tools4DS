# Misconception checks — module m01 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Hidden state** (lecture §2). A notebook gives the right answer on its author's laptop. After *Restart and run all* the third cell raises `NameError`. The most likely cause is:
A. a bug in Colab · B. a cell uses a variable that is defined in a cell further down · C. a missing package · D. the random seed changed

**MC2 — What a fresh run proves** (lecture §2). A notebook passes *Restart and run all* without errors. True or false: *"Then every cell gives the same result however many times I run it."* Explain in one sentence.

**MC3 — Which mean** (lecture §4.1). A fund's yearly returns are +50% and −50%. Its "average return" is reported as 0%. What happened to an investment of 100 baht over the two years?
A. still 100 baht · B. 75 baht · C. 125 baht · D. cannot be known

**MC4 — `ddof`** (lecture §4.2). `np.std(x)` and `pd.Series(x).std()` give different answers for the same five numbers. Which statement is correct?
A. one of the libraries has a bug · B. numpy divides by $n$ and pandas by $n-1$ by default · C. pandas drops the largest value · D. they differ only in rounding

**MC5 — Sentinels** (lecture §4.3). A temperature column has mean 9.8 °C and minimum −200 °C, and `isna().sum()` is 0. Which is the best first action?
A. report 9.8 °C; no values are missing · B. drop the minimum and report again · C. check the documentation for a missing-value code and recode it before summarising · D. replace −200 by 0

**MC6 — Verifying AI code** (lecture §6). An AI assistant's code for "daily means" runs without errors and returns numbers in a plausible range. Which check best verifies it?
A. ask the assistant whether it is correct · B. check that the output has one value per calendar day in the data and compare one day with a hand calculation · C. check that the numbers are positive · D. run it twice
