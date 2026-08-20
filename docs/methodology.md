# Methodology

## 1. Population separation

The dataset is split into accepted, rejected and new applicants before modeling.

Observed default labels exist only for accepted applicants.

## 2. Data-quality rules

The portfolio workflow treats ages below 18 or above 80 as invalid and converts them to missing values for imputation inside the model pipeline.

Two variables are deliberately excluded from the professional application-time model:

- `Avgexp`
- `Exp_Inc`

Both are structural zero for every rejected and every new applicant in the supplied data, while they contain post-acceptance spending information for most accepted applicants. Using them directly in an admission model would therefore create a serious availability / leakage concern.

## 3. Model development

Only accepted applicants have known outcomes.

- 75% development sample
- 25% untouched holdout sample
- stratification by default
- logistic regression with class balancing
- regularization parameter selected by 5-fold ROC-AUC cross-validation on development data only
- threshold selected from out-of-fold development predictions using Youden's J

Selected `C`: **0.1**

Probability threshold: **0.4692**

## 4. Reject inference

A first model trained on accepted development data estimates risk for rejected applicants.

Rejected applicants are pseudo-labeled using the development threshold:

- PD below threshold → inferred non-default
- PD at/above threshold → inferred default

The model is then refitted using accepted development observations plus pseudo-labeled rejected applicants.

Because true rejected outcomes are unknown, the augmented model is evaluated only on the untouched accepted holdout sample.

## 5. Score transformation

PD is converted to points using:

- Base score = 600
- Base odds = 50:1
- PDO = 40

The operational score threshold corresponding to the development PD threshold is **381.37** points.

## 6. Academic benchmark

The user's graded quiz provides official Information Value results for Question 8 and a subset of corrected approve/decline decisions for Question 9.

Those values are preserved as a benchmark, but they are **not used to tune the professional model**.

The professional model agrees with **12 of 14 (85.7%)** of the graded decision examples while using a separately defined leakage-aware feature set.
