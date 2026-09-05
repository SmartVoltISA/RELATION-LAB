# RELATION-INVAR-006 — Blind Continuous-Field Fingerprint Test

**Status:** EXECUTED / VERIFIED — NEGATIVE FOR THE CURRENT SCORE
**Date:** 2026-09-05

## Question
Can an unknown weak nonlocal relation be found blindly from a continuous field when the estimator does not know source or target locations, using one-step intervention response alone?

## Setup
N=80 continuous spatial elements on a periodic ring. Local nonlinear background dynamics plus one hidden nonlocal directed relation:

| source | target | K |
|---:|---:|---:|
| 23 | 67 | +0.045 |

The estimator was not told these locations. It scanned all 6320 ordered pairs and ranked them by mean absolute one-step response to a source perturbation of delta=0.5 over 40 held-out intervention times.

## Result

| metric | result |
|---|---:|
| ROC-AUC | 0.974680 |
| Average Precision | 0.006211 |
| True hidden pair score | 0.020826 |
| Top-ranked pair | 46 -> 47 |
| Top-ranked false-pair score | 0.039983 |
| Number of positives | 1 / 6320 |
| Prevalence baseline AP | 0.000158 |

## Decision
**FAIL for blind identification with this one-step score.**

The AUC is high because the hidden pair is generally ranked above most null pairs, but the AP is poor and the true pair is not the top-ranked pair. A strong local background response can exceed the weak nonlocal relation.

This is a genuine negative result, not a failure to obtain a convenient number.

## Interpretation

The experiment separates three concepts:

1. The hidden relation exists in the generating dynamics.
2. Its effect is statistically detectable against most null pairs.
3. Its location is not reliably identifiable from a single scalar one-step response ranking.

Therefore the hypothesis that **one-step response magnitude alone is a complete relation detector in an unknown continuous field is rejected for this regime**.

## Consequence

The next method must use the full response fingerprint:

- spatial profile,
- temporal profile,
- sign,
- propagation speed,
- repeatability across interventions,
- and comparison with a locally generated null response.

A relation should be treated as an equivalence class of response trajectories, not as a single amplitude.

## Important correction

Previous exploratory discussion suggested that the next step might simply recover weak relations by integrating the temporal trace. That is now treated as a **hypothesis**, not a result. This experiment shows why it must be tested against local-background controls rather than assumed to work.

## What remains open

Whether a full spatiotemporal response fingerprint can distinguish a weak nonlocal relation from strong local dynamics without predefined elements remains unresolved.
