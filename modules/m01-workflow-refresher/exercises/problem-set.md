# Problem set — module m01 (independent work, about 3 hours)

This week's independent work is: **redo Lab 1 on your own and submit it in Teams** (about 2 hours), the **core** items below (P1–P5, P8–P10 and P13; about 2 hours) and the reading (about 1 hour). Items marked *(optional)* are extra practice.

Not graded. Worked answers are discussed at the start of the week 2 lab. Items marked **[hand]** are the kind that appear on the paper midterm (one A4 sheet of notes, no computer); do them on paper first, then check them in Colab.

## A. Statistics refresher (core: about 1 hour)

**P1 [hand] — Three means.** For the positive values $x = (2, 4, 8)$: (a) compute the arithmetic, geometric and harmonic means. (b) Verify $\text{HM} \le \text{GM} \le \text{AM}$. (c) Give a real situation in which each mean is the right summary.

**P2 [hand] — Growth.** A shop's sales grew by 20% in year 1, fell by 10% in year 2 and grew by 5% in year 3. (a) What constant yearly growth rate gives the same three-year total? (b) Why is the arithmetic mean of the three rates (5%) misleading?

**P3 [hand] — Average speed.** A bus travels 10 km at 20 km/h and then 10 km at 60 km/h. Find the average speed for the 20 km. Which mean is it, and why is it not 40 km/h?

**P4 [hand] — Sample variance and a sentinel.** A sensor recorded the hourly values $12, 15, -200, 14, 19, -200, 16$, where −200 means "missing". (a) Compute the mean and the sample standard deviation ($n-1$ divisor) **treating −200 as data**. (b) Recompute them after recoding −200 as missing. (c) In one sentence, what would you report, and what else must you report with it?

**P5 [hand] — `ddof`.** For $x = (1, 2, 3, 4)$ compute the standard deviation with divisor $n$ and with divisor $n-1$. Which one does `np.std(x)` return, and which does `pd.Series(x).std()` return?

**P6 — Floating point** *(optional)*. In Colab, run `0.1 * 3 == 0.3`, `print(0.1 * 3)` and `np.isclose(0.1 * 3, 0.3)`. Explain the three results in one sentence each. Then try `sum([0.1] * 10) == 1.0`: why is "it worked this time" not a reason to use `==` on floats?

**P7 — Hidden state** *(optional)*. Write three notebook cells (as strings, using `run_cells` from Lab 1) that give a **different** answer when the second cell is run twice, then rewrite them so that rerunning any cell is safe. State the rule you applied.

## B. SQL with DuckDB (core: about 45 minutes)

Use the cleaned `aq` table from Lab 1 (registered as `aq_tbl`). For each query, also compute the result in pandas and `assert` that the two agree.

**P8 — Monthly coverage.** For each calendar month, return the number of hours, the number of valid CO readings and the share of valid readings, ordered by month. Which month has the lowest coverage?

**P9 — Hour-of-day profile.** Return the mean CO for each hour of the day (0–23). At which hours is CO highest, and what might explain it?

**P10 — `COUNT(*)` vs `COUNT(col)`.** Write one query that returns, for the whole table, `COUNT(*)`, `COUNT(co)` and `COUNT(nmhc)`. Explain the three numbers.

**P11 — Window functions** *(optional)*. For each day, rank the hours by CO (highest first) with `RANK() OVER (PARTITION BY CAST(ts AS DATE) ORDER BY co DESC)`, and return the hour with rank 1 for each day. How are missing CO values ranked, and should they be?

**P12 — Daily change** *(optional)*. Using the daily table from Lab 1 task T5, compute each day's change in mean CO from the previous day with `LAG(co_mean) OVER (ORDER BY day)`. What happens on days after a day with no valid reading?

## C. Reading (about 1 hour)

**P13.** Read Rule et al. (2019), *Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks* ([references](../references.md)). Choose the three rules that would have prevented the problems you met in Lab 1, and say in one sentence each how.

**P14** *(optional)*. Read the course [AI-use policy](../../../course/ai-policy.md). Write one row of an AI-use log for a realistic use of an AI tool in Lab 1, including how you would verify the output.
