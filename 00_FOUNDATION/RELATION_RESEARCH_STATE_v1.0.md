# RELATION-LAB — Research State v1.1

Date: 2026-09-05
Status: ACTIVE RESEARCH

## Current state

1. A relation can be treated operationally as a reproducible dependence of one state transition on another, provided controls distinguish it from indirect dependence, common cause and noise.
2. Directional influence can be recovered in controlled synthetic dynamical systems; intervention is stronger evidence than correlation alone.
3. A single instantaneous relation/change vector is not generally sufficient to determine the future.
4. Relation classes can emerge from invariants and symmetry, but observed relation values must not be equated with fundamental relation types.
5. Memory can alter transition resistance in a controlled model.
6. Minimal cellular media can generate localized propagating structures, but the electron hunt did not identify an electron.
7. Known electron numerical constants and derived quantities were independently reproduced; this is numerical verification, not evidence for a new ontology.
8. Relation-first clustering of a supplied particle dataset found nonrandom structure, but did not establish new physics.
9. **RELATION-CAUSAL-001 executed successfully in the specified N=40 analogue-like model.** Controlled intervention on source 10 produced a target-11 response whose increment above the known K=0 structural baseline matched `0.035*K` exactly at lag 1 for K=+0.18, +0.05 and −0.16. Source permutation strongly suppressed the response.
10. The experiment also exposed a key caveat: raw intervention response is not identical to hidden relation strength because background structural coupling and indirect propagation contribute.

## What remains unproven

- relation is ontologically more fundamental than particles, fields, space or time;
- all physical interaction is reducible to one universal relation variable;
- relation has a universal scalar strength;
- relation is necessarily symmetric or necessarily dual;
- memory is universally a property of relation rather than state;
- energy is universally identical to relation change;
- a physical electron can emerge from a relation-only medium;
- a continuous physical relation kernel K(r,r',t) can be recovered without presupposing node decomposition;
- direct relation strength can be recovered when background coupling and indirect pathways are unknown.

## Mathematical bridge

For a state vector X(t):

`X(t+1) = F(X(t), t) + noise`

Local direct influence candidate:

`K_ji(t) = ∂F_j/∂X_i`

For a continuous field:

`K(r,r',t) = δF(r,t)/δX(r',t)`

Operational intervention response:

`R_j(τ | do(X_i += δ)) = E[X_j(t+τ | intervention) - X_j(t+τ | control)]`

The task is to estimate direct relation from response structure while separating baseline coupling, indirect paths, noise and representation effects.

## Completed experiment: RELATION-CAUSAL-001

Hidden coupling 10→11 was switched as `K = 0, +0.18, +0.05, 0, −0.16`.

Lag-1 response at target 11:

| K | Observed response | Increment above K=0 | Expected 0.035*K |
|---:|---:|---:|---:|
| 0.00 | +0.003500 | +0.000000 | +0.000000 |
| +0.18 | +0.009800 | +0.006300 | +0.006300 |
| +0.05 | +0.005250 | +0.001750 | +0.001750 |
| −0.16 | −0.002100 | −0.005600 | −0.005600 |

At K=+0.18 and lag 10, source 10 produced +0.084006 target response; alternative sources produced 0 except a tiny +0.000063 background response for source 15.

Full result is recorded in:
`03_EXPERIMENTS/RELATION-CAUSAL-001-LOCAL-PERTURBATION-RESULT-v1.0.md`

## Revised next decisive experiment

Remove prior knowledge of the K=0 baseline. Randomize source/target pairs and infer direct relation strength from intervention responses while separating direct and indirect pathways.

Required controls:

- ±δ intervention scaling (δ=0.5, 1.0, 2.0);
- source permutation;
- target permutation;
- independent random seeds;
- time-shuffled observational control;
- nonlocal/random coupling control;
- multiple intervention lags;
- held-out source/target pairs;
- comparison with passive Jacobian/correlation estimators.

Required table:

`source | target | true K | lag | observed response | normalized response | sign | seed SD | permutation percentile | direct/indirect classification`

## Decision rule

A successful next result must generalize to held-out source/target pairs and distinguish direct edges from indirect paths without using the hidden K=0 baseline as an input.

If it fails, preserve the failure and revise the operational definition or estimator rather than weakening the controls.
