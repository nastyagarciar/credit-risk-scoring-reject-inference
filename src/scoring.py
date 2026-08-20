"""Reusable functions for the credit-risk scoring portfolio project."""

from __future__ import annotations

import numpy as np
import pandas as pd


APPLICATION_FEATURES = [
    "Age",
    "Income",
    "Ownrent",
    "Selfempl",
    "Depndt",
    "Inc_per",
    "Cur_add",
    "Major",
    "Active",
]


def build_application_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Create application-time features and clean impossible ages."""
    out = pd.DataFrame(index=df.index)

    age = pd.to_numeric(df["Age"], errors="coerce")
    age = age.mask((age < 18) | (age > 80))

    income = pd.to_numeric(df["Income"], errors="coerce")
    inc_per = pd.to_numeric(df["Inc_per"], errors="coerce")
    cur_add = pd.to_numeric(df["Cur_add"], errors="coerce")
    active = pd.to_numeric(df["Active"], errors="coerce")

    out["Age"] = age
    out["log1p_Income"] = np.log1p(income.clip(lower=0))
    out["Ownrent"] = pd.to_numeric(df["Ownrent"], errors="coerce")
    out["Selfempl"] = pd.to_numeric(df["Selfempl"], errors="coerce")
    out["Depndt"] = pd.to_numeric(df["Depndt"], errors="coerce")
    out["log1p_Inc_per"] = np.log1p(inc_per.clip(lower=0))
    out["log1p_Cur_add"] = np.log1p(cur_add.clip(lower=0))
    out["Major"] = pd.to_numeric(df["Major"], errors="coerce")
    out["sqrt_Active"] = np.sqrt(active.clip(lower=0))

    return out


def probability_to_score(
    probability,
    pdo: float = 40,
    base_score: float = 600,
    base_odds: float = 50,
):
    """Convert probability of default to a traditional points-based score."""
    probability = np.clip(np.asarray(probability, dtype=float), 1e-6, 1 - 1e-6)
    factor = pdo / np.log(2)
    offset = base_score - factor * np.log(base_odds)
    odds = (1 - probability) / probability
    return offset + factor * np.log(odds)
