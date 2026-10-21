# Reproducibility and verification

## Checks completed

- Inspected the supplied 107-row, 19-column dataset in a private environment.
- Cross-checked breakfast counts for days 0–7: `2, 1, 5, 8, 10, 12, 7, 62`.
- Cross-checked lunch counts for days 0–7: `1, 0, 1, 1, 6, 15, 17, 66`.
- Confirmed that the two analysis fields in each report have no missing records.
- Verified both analytical approaches with earlier local R Markdown HTML renders.
- Refactored the publication sources with neutral file names and presentation labels.
- Confirmed that the static public reports and figures use aggregate-only data.
- Passed the distributed Python package-level checks.

## Runtime boundaries

The two `.Rmd` files are designed to run from the repository root, where an authorised private file named `survey_data.csv` must be placed. The data file is neither distributed nor fetched automatically.

The published `breakfast_report.html` and `lunch_report.html` are **purpose-built static previews**, not knitted outputs. The `.Rmd` scripts regenerate their own local HTML documents when dependencies and the private CSV are available. The renamed/refactored source files have not been independently executed with R in the packaging environment; run the R commands in the README for runtime confirmation.

GitHub Actions executes static checks only. A passing run does not establish source-data sharing permissions, validate future input datasets or execute R Markdown.
