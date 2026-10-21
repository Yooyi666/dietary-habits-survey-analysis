# Methodology

## Dataset and questions

The source is an observational dietary survey with 107 responses and 19 recorded variables. Two descriptive questions guide the portfolio:

1. How does weekly breakfast frequency vary across reported employment categories?
2. How does weekly lunch frequency vary across self-reported gender categories?

No respondent-level records are bundled with the public package.

## Variables

| Field | Meaning | Measurement |
|---|---|---|
| `Breakfast` | Number of days breakfast is consumed per week | Discrete numeric count, 0–7 |
| `Employment` | Reported employment or enrolment category | Nominal categorical variable |
| `Lunch` | Number of days lunch is consumed per week | Discrete numeric count, 0–7 |
| `Gender` | Self-reported gender category | Nominal categorical variable |

## Method

Both charts are stacked count bar plots. Frequency axes show the number of respondents, with colour indicating the categorical grouping. The breakfast public display uses neutral, semantically equivalent category descriptions without changing the underlying group membership or tally.

A basic validation pipeline checks that meal frequency is a non-missing whole number between 0 and 7, and that grouping fields contain no blanks. For the known dataset, the frequency totals also match the fixed verification baselines.

## Summary

| Days per week | Breakfast respondents | Lunch respondents |
|---:|---:|---:|
| 0 | 2 | 1 |
| 1 | 1 | 0 |
| 2 | 5 | 1 |
| 3 | 8 | 1 |
| 4 | 10 | 6 |
| 5 | 12 | 15 |
| 6 | 7 | 17 |
| 7 | 62 | 66 |
| **Total** | **107** | **107** |

## Limitations

The sample may not represent a broader population. Counts are not normalised to group sizes, and there is no causal identification. Self-reported behaviour can be affected by recall and measurement error. Category imbalance, particularly a one-response gender category, limits meaningful comparisons and raises disclosure considerations.
