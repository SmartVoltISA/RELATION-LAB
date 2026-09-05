# RELATION-INVAR-005 — Detection Boundary of Nonlocal Relation

**Status:** EXECUTED / VERIFIED
**Date:** 2026-09-05

## Question
How strong must a hidden nonlocal relation be to distinguish its response from ordinary local propagation in a continuous field?

## Protocol
Same periodic 1D continuous field as RELATION-INVAR-004, N=80, dt=0.1. Source-target distance was varied. The estimator used blind one-step interventions and absolute normalized target response. Hidden targets were randomized away from the source's immediate neighbors.

The local propagation baseline for a source is approximately 0.018 at distance 1 under the locked dynamics. Hidden relation strength K was swept over 0.02, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30. For each K, hidden target was at distance 20 (periodic distance).

## Results

| K | hidden response (dt*K) | local neighbor response | hidden/local ratio | detected as top off-diagonal response |
|---:|---:|---:|---:|---:|
| 0.02 | 0.002000 | 0.018000 | 0.111 | NO |
| 0.05 | 0.005000 | 0.018000 | 0.278 | NO |
| 0.10 | 0.010000 | 0.018000 | 0.556 | NO |
| 0.15 | 0.015000 | 0.018000 | 0.833 | NO |
| 0.20 | 0.020000 | 0.018000 | 1.111 | YES |
| 0.25 | 0.025000 | 0.018000 | 1.389 | YES |
| 0.30 | 0.030000 | 0.018000 | 1.667 | YES |

## Result

A sharp operational detection boundary appears near K ≈ 0.18 for this particular one-step scoring rule, because the hidden response must exceed the strongest ordinary local response.

**Result: PASS for falsification-oriented boundary test.** The relation is not automatically detectable merely because it exists. Detectability depends on signal strength relative to the background response operator.

## Interpretation

This is important for the ontology question. A relation is not equivalent to "any nonzero influence" in practical observation. There is a distinction between:

1. physical/model-level existence of an interaction term;
2. observability of its response;
3. identifiability of that response as distinct from background dynamics.

The experiment therefore supports treating relation as a response structure together with a detectability/identifiability condition.

## Limitation

This threshold is specific to the chosen dynamics, noise level, intervention amplitude, sampling interval, and one-step score. It is not a universal physical constant.

## Next step

Repeat the boundary test with multiple noise levels and multi-step response signatures. Determine whether a relation below the one-step threshold can become identifiable from its temporal/spatial response kernel rather than its peak amplitude.
