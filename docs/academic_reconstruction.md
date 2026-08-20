# Academic Reconstruction Notes

The original evaluation contained two scoring questions.

## Question 8 — Information Value

The graded correction showed these IV values when all accepted customers were used without a train/test split:

| Variable | IV |
|---|---:|
| Age | 0.224977 |
| Income | 0.222999 |
| Exp_Inc | 0.187134 |
| Avgexp | 0.271663 |
| Ownrent | 0.011976 |
| Selfempl | 0.011895 |
| Depndt | 0.005121 |
| Inc_per | 0.156240 |
| Cur_add | 0.192857 |
| Major | 0.030557 |
| Active | 0.004177 |

These are included in `results/academic_iv_reference.csv` as the graded benchmark.

## Question 9 — New applicants

The correction screenshot identifies the following decisions among the IDs shown in that multiple-choice question:

Approved:
`1286, 1291, 1294, 1300, 1303, 1305, 1309, 1314, 1317, 1319`

Declined:
`1287, 1301, 1306, 1307`

The portfolio model does not tune its threshold to reproduce this answer key. Instead, the key is used only as an external comparison after model development.
