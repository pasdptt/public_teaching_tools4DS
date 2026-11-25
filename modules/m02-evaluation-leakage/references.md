# References — module m02

Each entry was checked on 25 November 2026 against its Crossref DOI record (`api.crossref.org/works/<DOI>`): authors, year, title, venue, volume, issue and pages.

## Core reading (assigned)

| Key | Reference | DOI |
|---|---|---|
| KN23 | Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9), 100804. | [10.1016/j.patter.2023.100804](https://doi.org/10.1016/j.patter.2023.100804) |

## Cited in the lecture outline

| Key | Reference | DOI |
|---|---|---|
| Kau12 | Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: formulation, detection, and avoidance. *ACM Transactions on Knowledge Discovery from Data*, 6(4), 1–21. Crossref's title field gives only "Leakage in data mining". | [10.1145/2382577.2382579](https://doi.org/10.1145/2382577.2382579) |
| AM02 | Ambroise, C., & McLachlan, G. J. (2002). Selection bias in gene extraction on the basis of microarray gene-expression data. *Proceedings of the National Academy of Sciences*, 99(10), 6562–6566. | [10.1073/pnas.102102699](https://doi.org/10.1073/pnas.102102699) |
| VS06 | Varma, S., & Simon, R. (2006). Bias in error estimation when using cross-validation for model selection. *BMC Bioinformatics*, 7, 91. | [10.1186/1471-2105-7-91](https://doi.org/10.1186/1471-2105-7-91) |
| Rob17 | Roberts, D. R., Bahn, V., Ciuti, S., Boyce, M. S., Elith, J., Guillera-Arroita, G., Hauenstein, S., Lahoz-Monfort, J. J., Schröder, B., Thuiller, W., Warton, D. I., Wintle, B. A., Hartig, F., & Dormann, C. F. (2017). Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure. *Ecography*, 40(8), 913–929. | [10.1111/ecog.02881](https://doi.org/10.1111/ecog.02881) |
| Wil27 | Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association*, 22(158), 209–212. | [10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953) |
| BCD01 | Brown, L. D., Cai, T. T., & DasGupta, A. (2001). Interval estimation for a binomial proportion. *Statistical Science*, 16(2), 101–133. | [10.1214/ss/1009213286](https://doi.org/10.1214/ss/1009213286) |
| CBHK02 | Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research*, 16, 321–357. | [10.1613/jair.953](https://doi.org/10.1613/jair.953) |

## Data

| Dataset | Source and licence |
|---|---|
| Digits (registry `digits`) | Alpaydin & Kaynak (1998), UCI Machine Learning Repository, doi:10.24432/C50P49, CC BY 4.0; the 1,797-image subset bundled with scikit-learn |
| Grouped patients, noise, clinic | Synthetic, generated in the lab with the course seed |

## Software documentation (no DOI)

* scikit-learn: model selection (`GroupKFold`, `cross_val_score`), `Pipeline` — <https://scikit-learn.org/stable/>
* imbalanced-learn: `imblearn.pipeline`, `SMOTE` — <https://imbalanced-learn.org/stable/>
