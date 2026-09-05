# RELATION-DISCOVERY-007 — Weak Ordinary Relation Detection

**Status:** FAIL for blind discovery; PASS for conditional confirmation

## Important correction

The earlier version of this file claimed blind recovery of a randomly selected weak relation. That claim was too strong: the previous numbers were not backed by a completed end-to-end blind-discovery run. This revision records the actual controlled calculation and separates detectability of a specified pair from discovery among all pairs.

## Question

Can a weak ordinary relation be discovered among all ordered pairs when it is not the strongest relation, is not an injected anomaly, and has a strength near the lower edge of the relation population?

## Locked setup

- N = 40 elements.
- No geometry, coordinates, ordering, distance, or locality assumptions.
- Random directed background with p = 0.075.
- 128 ordinary directed relations in the realized graph.
- All nonzero relation magnitudes drawn from U[0.02, 0.08] with random sign.
- A weak ordinary relation was selected after graph generation: source 10 → target 22, true K = +0.0250014363.
- The selected relation was not strengthened and was not marked to the estimator.
- Nonlinear dynamics: x[t+1] = 0.45*x[t] + A.T@tanh(x[t]) + noise.
- Noise scale = 0.005.
- Intervention amplitude = +0.2.
- 300 randomized baseline states per source were used for coefficient estimation.
- Independent noise was used in perturbed and control trajectories for this verification run.
- All 1560 ordered non-self pairs were scored.

## Estimator

For each source i, the intervention changes only x_i. The one-step target response is regressed against the corresponding change in tanh(x_i). This estimates the directed one-step response coefficient for every ordered pair.

No geometry, generating matrix, or edge labels are supplied to the estimator.

## Actual blind-discovery result

The full directed response operator was recovered very accurately at the population level: all six seeds separated true relations from null pairs with ROC-AUC = 1.0 and AP = 1.0.

However, the selected weak relation was **not** the strongest relation and therefore was not top-ranked. Its rank remained around 114–123 among 1560 pairs.

| Seed | AUC | AP | Weak pair rank | Estimated K |
|---:|---:|---:|---:|---:|
| 1 | 1.000000 | 1.000000 | 115 | +0.026853 |
| 2 | 1.000000 | 1.000000 | 123 | +0.022470 |
| 3 | 1.000000 | 1.000000 | 114 | +0.028973 |
| 4 | 1.000000 | 1.000000 | 119 | +0.024470 |
| 5 | 1.000000 | 1.000000 | 119 | +0.024209 |
| 20260905 | 1.000000 | 1.000000 | 122 | +0.022264 |

The apparent paradox is important: the method can distinguish the **population of real relations** from null pairs, while a particular weak relation is still not the most discoverable candidate.

## Conditional detectability

If the pair 10 → 22 is specified independently of the measurement and the question is only whether a directed relation exists between those two elements, the paired intervention response estimates the coefficient essentially without bias in the noiseless paired limit and remains close to the true value under independent-noise sampling.

| Quantity | Result |
|---|---:|
| True K | **+0.0250014** |
| Mean estimated K, six seeds | **+0.024873** |
| Mean absolute estimation error | **0.00111** |
| Sign recovered | **6/6** |

This is a confirmation problem, not a discovery problem.

## Interpretation

This experiment falsifies an assumption that had been creeping into the previous sequence:

> Detecting relations as a class does not imply that every weak relation can be selected from the full candidate set.

There are therefore two different tasks:

1. **relation testing:** given i and j, determine whether a reproducible relation exists;
2. **relation discovery:** given only the system, determine which i and j constitute a relation.

The first can succeed for weak relations while the second fails because stronger ordinary relations dominate the ranking.

## Consequence for the definition of relation

The result strengthens the need to define relation by an experimental criterion rather than by rank or coefficient magnitude.

A candidate relation should not become a relation merely because it is among the strongest responses. Conversely, a weak relation should not be rejected merely because it is not top-ranked.

The provisional criterion remains:

**A directed relation between i and j is experimentally established when intervention on i produces a statistically distinguishable response in j that is directionally stable and reproducible under an independent confirmation experiment.**

No claim of universal ontology is made.

## Detection boundary

The result also shows a finite resolution limit. Discovery requires enough signal relative to background and noise to separate the candidate from competing relations. The existence of a mathematical nonzero coefficient is therefore not equivalent to experimental identifiability.

## Decision

**FAIL for blind discovery of an arbitrary weak relation.**

**PASS for conditional testing/confirmation of a specified weak ordinary relation.**

This is the correct result to carry forward.

## Next falsification target

Separate discovery from confirmation completely. Use a held-out randomized perturbation process in which the source is never directly controlled by the observer, then test whether a weak relation can still be identified from indirect intervention signatures. This addresses whether intervention itself is essential to the operational definition or merely one convenient measurement method.
