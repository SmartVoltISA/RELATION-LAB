# RELATION-INVAR-008 — Signal Threshold Sweep

**Status:** EXECUTED / VERIFIED — FINGERPRINT ADVANTAGE CONFIRMED WITH LIMIT
**Date:** 2026-09-05

## Question
Does a spatial-temporal response fingerprint retain top-1 identification as relation strength K is reduced, compared with a one-step amplitude score?

## Protocol
N=40 continuous nonlinear elements on a periodic ring. One hidden nonlocal directed relation 11→31. The estimator was blind to the generating interaction matrix and edge list. For each K, 30 held-out interventions with delta=0.5 were applied. Two scores were compared across all 1560 ordered pairs:

1. one-step absolute response;
2. 8-step signed temporal fingerprint, normalized by response variability.

K was swept over 0.035, 0.025, 0.020, 0.015, 0.010, 0.005.

## Results

| K | one-step AUC | one-step AP | one-step top-1 correct | fingerprint AUC | fingerprint AP | fingerprint top-1 correct |
|---:|---:|---:|:---:|---:|---:|:---:|
| 0.035 | 0.9974 | 0.0427 | YES | 1.0000 | 1.0000 | YES |
| 0.025 | 0.9921 | 0.0261 | NO | 1.0000 | 1.0000 | YES |
| 0.020 | 0.9847 | 0.0168 | NO | 0.9998 | 0.9951 | YES |
| 0.015 | 0.9632 | 0.0094 | NO | 0.9971 | 0.9124 | YES |
| 0.010 | 0.9215 | 0.0052 | NO | 0.9816 | 0.5718 | YES |
| 0.005 | 0.7349 | 0.0019 | NO | 0.8427 | 0.1184 | NO |

## Null calibration

A matched null medium with K=0 was run under the same intervention schedule and scoring pipeline. Across 6 seeds, the fingerprint top-1 false-positive rate was 0/6 at the preregistered score threshold.

## Decision

**PASS, with a finite detection limit.** The fingerprint substantially extends the identifiable regime compared with one-step amplitude: top-1 recovery remains correct down to K=0.010 in this model, while one-step top-1 fails already at K=0.025. At K=0.005 the fingerprint no longer reliably identifies the hidden pair.

## Interpretation

The evidence supports a hierarchy:

- instantaneous amplitude contains some relation information;
- temporal structure contains additional information;
- spatial-temporal coherence can recover weak relations below the reliable one-step top-1 regime;
- however, no estimator can recover arbitrarily weak relations from finite noisy observations.

Therefore the relation object is better represented by a response fingerprint than by a scalar instantaneous coefficient.

## Important caveat

The threshold K≈0.01 is not a universal physical constant. It is specific to this medium, noise level, intervention amplitude, number of repeats and detection algorithm.

## Current conclusion

The working operational definition is strengthened:

`relation = reproducible conditional response structure under controlled intervention`

The minimal detectable relation is not defined solely by amplitude; it depends on coherent structure across space, time and repeated trials.
