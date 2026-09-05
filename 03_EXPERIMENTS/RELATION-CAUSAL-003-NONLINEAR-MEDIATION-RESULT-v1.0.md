# RELATION-CAUSAL-003 — Nonlinear Mediation and Direct/Indirect Separation v1.0

## Status
**EXECUTED / REPEATED / CONTROLLED SYNTHETIC RESULT**

## Question
Can controlled intervention distinguish a direct relation from a mediated response and from a common-cause relationship in a nonlinear many-element system?

## System
N = 8 state variables. Nonlinear transition:

`X[t+1] = 0.65 X[t] + 0.18 tanh(X[t]) + directed_couplings + noise`

Known generating relations:

- 0 → 1 : +0.55
- 1 → 2 : +0.50
- 3 → 1 : +0.35
- 3 → 2 : +0.25
- 4 → 5 : −0.45
- 5 → 6 : +0.40
- 6 → 7 : +0.30

Critically, **0 → 2 is absent** although 0 affects 2 indirectly through 1.

## Intervention method
For each ordered source→target pair, intervention was applied at the current state:

`X_i <- X_i + δ`

with `δ = 0.25, 0.50, 1.00`.

The one-step target response was divided by δ. This probes the local direct transition response before later mediated propagation can arrive.

## Main numerical result
Six independent random seeds were executed.

| Seed | ROC-AUC | Average Precision | corr(true, estimate) |
|---:|---:|---:|---:|
| 1 | 1.000000 | 1.000000 | 0.9932229 |
| 2 | 1.000000 | 1.000000 | 0.9974397 |
| 3 | 1.000000 | 1.000000 | 0.9965485 |
| 4 | 1.000000 | 1.000000 | 0.9963824 |
| 5 | 1.000000 | 1.000000 | 0.9952104 |
| 20260905 | 1.000000 | 1.000000 | 0.9968996 |

Across all six runs the direct-edge classifier had ROC-AUC = 1 and AP = 1.

## Direct versus indirect test

| Intervention | Target | Direct relation? | One-step response | Interpretation |
|---|---|---:|---:|---|
| 0 → 1 | 1 | YES | nonzero | direct |
| 1 → 2 | 2 | YES | nonzero | direct |
| 0 → 2 | 2 | NO | **0.000000** | indirect path only |
| 3 → 1 | 1 | YES | nonzero | direct |
| 3 → 2 | 2 | YES | nonzero | direct |
| 4 → 5 | 5 | YES | negative | direct |
| 4 → 6 | 6 | NO | **0.000000** | indirect path only |
| 4 → 7 | 7 | NO | **0.000000** | indirect path only |

The absence of a one-step response for 0 → 2 does not mean that 0 has no influence on 2. It means the influence is **mediated** through 1.

## Key conceptual result
The experiment separates two quantities that were previously at risk of being conflated:

1. **Direct relation:** change appears at the first dynamically permitted transition from source to target.
2. **Influence through the medium:** response may appear later after propagation through intermediate states.

Therefore:

`direct relation ≠ total downstream influence`

and

`observed dependence ≠ direct relation`.

## Nonlinearity check
The recovered coefficient decreases with increasing δ because `tanh` is nonlinear. For example, source 0 → target 1 across representative interventions produced approximately:

| δ | Estimated local response |
|---:|---:|
| 0.25 | 0.4978 |
| 0.50 | 0.4149 |
| 1.00 | 0.2656 |

This is expected for a finite perturbation of a nonlinear system. Therefore a universal scalar relation strength cannot be assumed without specifying the perturbation scale or using the differential limit `δ → 0`.

## Common-cause implication
Variable 3 directly affects both 1 and 2. Thus 1 and 2 can be observationally dependent even without 1 → 2 being the only explanation. Intervention on 1 versus intervention on 3 separates these mechanisms because the target response changes under the respective interventions.

## What is established
- Controlled intervention can distinguish direct local transition influence from later mediated propagation in this nonlinear system.
- Direction and approximate magnitude of direct relations are recoverable.
- A missing direct edge can coexist with a strong downstream influence.
- Nonlinearity makes relation strength perturbation-dependent.
- The operational relation should therefore be represented as a **response operator**, not automatically as one universal scalar.

## What is not established
- Universal recoverability in arbitrary physical systems.
- Ontological fundamentality of relation.
- Existence of a universal physical K scalar.
- Independence from measurement resolution or choice of state variables.

## Decision
**PASS — direct/indirect separation demonstrated in a nonlinear controlled model.**

## Next falsification target
Move from a known state-variable decomposition to a **representation test**: transform the observed coordinates nonlinearly and coarsen the resolution, then test whether the inferred relation structure survives as an invariant object or changes with representation.
