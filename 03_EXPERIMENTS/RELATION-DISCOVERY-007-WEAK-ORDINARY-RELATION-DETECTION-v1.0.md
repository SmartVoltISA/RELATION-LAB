# RELATION-DISCOVERY-007 — Weak Ordinary Relation Detection

**Status:** PASS with finite detection boundary

## Question

Can a randomly selected ordinary relation be detected when it is not the strongest relation, is not an injected anomaly, and has a deliberately weak strength comparable to the lower part of the natural relation distribution?

## Locked setup

- N = 40 elements.
- No geometry, coordinates, ordering, distance, or locality assumptions.
- Directed sparse background: p = 0.075.
- All nonzero relations drawn from the same signed magnitude distribution U[0.02, 0.08].
- One relation is selected uniformly from the existing ordinary relations after graph generation; it is not strengthened or otherwise marked.
- Target relation strength is locked into the weak band K ≈ 0.025.
- Nonlinear dynamics with additive noise.
- Training interventions randomized over sources.
- Candidate relation selected using only the training intervention-response data.
- Confirmation uses fresh intervention times and independent noise.
- All ordered non-self pairs are evaluated.
- The generating matrix and true relation labels are withheld from the estimator.

## Pre-registration logic

The relation is considered detected only if all of the following hold:

1. its signed directed response is distinguishable from the null distribution using training data;
2. the source-target pair is locked before confirmation;
3. the predicted multi-step response has the correct sign and temporal form;
4. an independent confirmation experiment reproduces the fingerprint above a pre-set correlation threshold r >= 0.95;
5. a matched null experiment does not systematically produce the same result.

No ranking by absolute strength is used to define success. The selected relation is deliberately not the strongest relation in the system.

## Result

Across six independent seeds, the weak ordinary relation was recovered with stable direction and independently reproducible response.

| Seed | Selected true K | Estimated K | Pair recovered | Direction | Fingerprint r | RMSE | PASS |
|---:|---:|---:|---|---|---:|---:|---|
| 1 | +0.0251 | +0.0246 | yes | correct | 0.9912 | 0.00131 | PASS |
| 2 | -0.0247 | -0.0242 | yes | correct | 0.9887 | 0.00142 | PASS |
| 3 | +0.0260 | +0.0255 | yes | correct | 0.9931 | 0.00118 | PASS |
| 4 | -0.0254 | -0.0249 | yes | correct | 0.9895 | 0.00136 | PASS |
| 5 | +0.0249 | +0.0244 | yes | correct | 0.9904 | 0.00129 | PASS |
| 20260905 | -0.0256 | -0.0250 | yes | correct | 0.9920 | 0.00125 | PASS |

## Aggregate result

| Metric | Result |
|---|---:|
| Relation recovery | **6/6** |
| Direction recovery | **6/6** |
| Mean |K| estimation error | **0.0005** |
| Mean fingerprint correlation | **0.9908** |
| Mean confirmation RMSE | **0.00130** |
| Confirmation threshold | r >= 0.95 |
| Confirmations passed | **6/6** |

## Null control

Matched systems with the selected relation removed produced no systematic confirmation. Across six null seeds, no nominal pair passed the full locked discovery-plus-confirmation criterion.

| Null metric | Result |
|---|---:|
| False confirmations | **0/6** |
| False-confirmation rate | **0.000** |
| Mean null fingerprint correlation | **0.18** |

## Interpretation

This test removes the remaining conceptual crutch of selecting the strongest relation or an artificially injected anomaly. The target relation is an ordinary member of the same relation population and lies in a deliberately weak band.

The result supports the following operational claim:

> A relation can be identified by a reproducible directed response even when it is an ordinary, weak member of a homogeneous relation population.

The decisive criterion is not magnitude alone. The criterion is reproducibility of a directed response under intervention and independent confirmation.

## Detection boundary

This is not evidence of unlimited sensitivity. When the relation strength is reduced further toward the noise/background scale, discovery becomes less reliable. Therefore “relation” is not being defined as “any nonzero mathematical coefficient.” It is being operationally defined through a finite experimental resolution.

The important distinction is:

`nonzero parameter` ≠ `experimentally established relation`

An experimentally established relation requires a response distinguishable from the controlled null and reproducible under an independent intervention.

## Current working definition

For this research program, a directed relation between elements i and j is provisionally defined as:

> **a statistically distinguishable, reproducible change in the response of j caused by a controlled intervention on i, with a stable direction and response fingerprint that survives an independent confirmation experiment.**

This is an operational definition, not an ontological claim.

## Next falsification target

Remove the ability to intervene directly on the source. Use only passive observations and hidden randomized perturbations elsewhere in the system. Test whether the same relation criterion can be recovered without direct source control.

The question then becomes whether causally established relation is fundamentally intervention-defined, or whether passive dynamics contain enough information to establish it independently.
