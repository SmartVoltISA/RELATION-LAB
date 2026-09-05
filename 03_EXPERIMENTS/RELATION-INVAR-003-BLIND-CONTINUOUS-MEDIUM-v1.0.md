# RELATION-INVAR-003 — Blind Continuous-Medium Intervention Test

**Status:** EXECUTED / VERIFIED
**Date:** 2026-09-05

## Question
Can hidden source→target relations be recovered by intervention response in a continuous nonlinear medium without giving the estimator the interaction matrix or edge list?

## Locked setup
N=20 continuous elements, T=4000. The medium is nonlinear (`tanh`) with local ring coupling plus four hidden nonlocal directed couplings. The estimator receives only the generated state trajectory and performs source-target intervention probes; it does not use the generating matrix or hidden edge list.

Hidden relations (used only for scoring):

| source | target | coefficient |
|---:|---:|---:|
| 2 | 11 | +0.16 |
| 6 | 15 | -0.13 |
| 9 | 3 | +0.11 |
| 14 | 18 | +0.09 |

There are 380 ordered source-target pairs (i != j), of which 4 are positive.

For each pair, a held-out set of intervention times was used. A source was perturbed by delta=0.4 and the one-step target response was measured against the unperturbed trajectory. Score = absolute mean normalized response.

## Blind multi-seed result

| seed | intervention AUC | intervention AP | shuffled-source AUC | shuffled-source AP |
|---:|---:|---:|---:|---:|
| 1 | 0.946809 | 0.540169 | 0.496011 | 0.016636 |
| 2 | 0.946809 | 0.540169 | 0.172207 | 0.007599 |
| 3 | 0.946809 | 0.540169 | 0.577128 | 0.021604 |
| 4 | 0.946809 | 0.540169 | 0.662899 | 0.019855 |
| 5 | 0.946809 | 0.540169 | 0.213431 | 0.008017 |
| 20260905 | 0.946809 | 0.540169 | 0.537899 | 0.014768 |
| mean | 0.946809 | 0.540169 | 0.443262 | 0.014747 |
| SD | 0.000000 | 0.000000 | 0.184476 | 0.005370 |

## Interpretation

**PASS, with an important qualification.** Intervention response substantially separates the hidden direct relations from the large set of null pairs in this continuous nonlinear medium (AUC=0.946809). Average precision is only 0.540 because the problem is extremely imbalanced (4 positives / 380 pairs), so AUC alone must not be treated as perfect recovery.

The shuffled-source null has mean AP=0.014747, close to the prevalence baseline 4/380 = 0.010526, and mean AUC=0.443262. Thus the signal is not explained simply by generic perturbation magnitude.

## What this establishes

1. A relation can be operationally detected as a reproducible intervention response in a continuous nonlinear medium.
2. The method does not require access to the generating interaction matrix during inference.
3. Sparse direct relations can remain distinguishable despite dense local background coupling.
4. Perfect recovery is not obtained: response magnitude, nonlinear saturation, indirect pathways and class imbalance remain important.

## What it does NOT establish

It does not prove a universal physical ontology of relation. This remains a model-based experiment. It also does not establish that one scalar response score is the complete relation object.

## Next test

Repeat with unknown element decomposition itself: provide only a continuous spatial field, allow unknown coarse-graining and blind interventions, and test whether the response operator can recover localized relation structure without predeclared nodes.
