# Results

## Holdout performance

The final reject-inference model is evaluated on accepted applicants that were never used for fitting or pseudo-labeling.

| Metric | Result |
|---|---:|
| ROC-AUC | 0.8141 |
| Average Precision | 0.3189 |
| Balanced Accuracy | 0.7383 |
| Default Recall | 0.8846 |
| Default Precision | 0.2018 |
| Default F1 | 0.3286 |

Confusion matrix:

- True non-default: 132
- False default flag: 91
- Missed defaults: 3
- Detected defaults: 23

## New applicants

The model scores all 34 new applicants.

- Approved: 15
- Declined: 19

See `new_applicant_scores.csv`.

## Academic benchmark

The model matches 12 of 14 corrected decisions shown in the graded quiz screenshot.

This comparison is diagnostic only; the answer key was not used for threshold tuning.
