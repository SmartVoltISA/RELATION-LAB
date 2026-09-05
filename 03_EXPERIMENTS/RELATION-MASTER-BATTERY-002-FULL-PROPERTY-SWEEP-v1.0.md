# RELATION-MASTER-BATTERY-002 — Full Property Sweep

Date: 2026-09-05
Status: COMPLETE CURRENT BATTERY

## Scope

This battery tests the current operational concept of relation across directness, direction, feedback, mediation, common cause, time variation, nonlinearity, stochastic response, missing observations, representation, geometry dependence, passive latent perturbations, and independent confirmation.

This is not a claim that every possible physical relation has been tested. It is the broadest current falsification battery in RELATION-LAB.

## 1. Directness and direction

| System | Direct i→j one-step | Reverse j→i one-step | Interpretation |
|---|---:|---:|---|
| Direct 0→1 | 0.400 | 0.000 | direct directed relation |
| Indirect 0→2→1 | 0.000 | 0.000 | no direct one-step 0→1 |
| Common cause 3→0,3→1 | 0.000 | 0.000 | dependence can exist without direct edge |
| Feedback 0↔1 | 0.400 | 0.300 | both directions are genuine |
| Signed bidirectional | 0.400 | -0.250 | direction and sign are distinct |

Conclusion: passive dependence is insufficient; intervention response distinguishes directness and direction at the tested temporal resolution.

## 2. Direct versus mediated temporal structure

For a direct 0→1 system with coefficient 0.4 and intervention δ=0.5, the one-step target response is 0.2 and later direct response is zero in the locked linear model.

For an indirect 0→2→1 system with coefficients 0.4 and 0.5, the one-step 0→1 response is 0, while the two-step response is 0.1.

Conclusion: directness is temporal-scale dependent. A multi-step response can reveal mediation that a one-step test intentionally excludes.

## 3. Time-varying relation

Two-variable process with c(t) = 0 for 0–1499, +0.5 for 1500–2999, -0.3 for 3000–4499, and 0 for 4500–5999.

Window = 300 samples.

| Metric | Result |
|---|---:|
| Correlation estimated c vs true c | 0.983650 |
| RMSE | 0.053487 |
| Positive segment recovered | yes |
| Negative segment recovered | yes |
| Zero segments near zero | yes |

Conclusion: relation can be a state/time-dependent response structure rather than a fixed scalar.

## 4. Nonlinear intervention amplitude

For a nonlinear response y_next = tanh(0.4y + 0.6 tanh(x)), the normalized response changes with intervention amplitude.

| δ | response / δ |
|---:|---:|
| 0.05 | 0.553805 |
| 0.10 | 0.544315 |
| 0.25 | 0.511635 |
| 0.50 | 0.450152 |
| 1.00 | 0.336021 |
| 2.00 | 0.198898 |

Conclusion: a universal scalar relation strength is not valid in a nonlinear system. The local response depends on state and intervention amplitude.

## 5. State-dependent relation

A two-element nonlinear system used K=0.15 for negative source states and K=0.45 for nonnegative source states.

Estimated coefficients from passive data:

| Source-state regime | Estimated K |
|---|---:|
| x < 0 | 0.1427698 |
| x >= 0 | 0.4180368 |

Conclusion: relation strength can be conditional on system state. The relation is better represented as a conditional response operator than as one constant number.

## 6. Stochastic relation

A zero-mean random-sign coupling K(t) ∈ {-0.5,+0.5} was constructed so that the mean signed response cancels.

| Quantity | Result |
|---|---:|
| Low-|x| target variance | 0.0052323 |
| High-|x| target variance | 0.0409244 |
| Variance ratio high/low | **7.8215** |
| Mean signed coupling | approximately 0 |

Conclusion: a relation need not appear in the conditional mean. Relations may reside in variance, higher moments, or other response statistics. A mean-only definition is therefore insufficient.

## 7. Missing observations

Specified direct relation K=0.4, δ=0.5, 5000 paired observations, Gaussian noise σ=0.05. Randomly removed observations were tested.

| Missing fraction | Estimated K | Standard error |
|---:|---:|---:|
| 0% | 0.200577 response / δ equivalent | 0.000999 |
| 10% | 0.200587 response / δ equivalent | 0.001051 |
| 30% | 0.201877 response / δ equivalent | 0.001202 |
| 50% | 0.200935 response / δ equivalent | 0.001428 |
| 80% | 0.202515 response / δ equivalent | 0.002266 |

Conclusion: random missingness increases uncertainty but does not destroy identification in this simple specified-pair experiment. Structured or informative missingness remains unresolved.

## 8. Passive latent perturbation / instrumental-variable test

The source was not directly intervened on. A hidden exogenous shock z affected source x0. Target x1 was causally affected by x0 and also shared a confounder x2.

True direct effect x0→x1 = 0.4.

| Method / system | Estimated effect |
|---|---:|
| Naive regression, causal + confounder system | 0.693213 |
| IV using hidden exogenous shock z | **0.414972** |
| Naive regression, confounding-only null | 0.118787 |
| IV, confounding-only null | **-0.002844** |

Conclusion: passive data alone can be biased by confounding. An exogenous instrument can recover the causal relation without direct source intervention in the tested model.

## 9. Geometry independence

Previously tested continuous rings and random directed networks. The estimator succeeded without being given coordinates or adjacency labels in both classes.

Conclusion: geometry is not required for operational relation detection. Geometry can be one source of structure, but is not definitionally required.

## 10. Representation robustness

Previously tested element-preserving transformations X→sinh(X) and X→X^3+X plus element permutation.

| Representation | Relation support preserved? | Numerical magnitude preserved? |
|---|---|---|
| Original X | yes | baseline |
| sinh(X) | yes | no |
| X^3+X | yes | no |
| Element permutation | yes, after relabeling | not applicable |
| Random invertible coordinate mixing | no sparse support guarantee | no |

Conclusion: relation support is robust under transformations that preserve element identity. Arbitrary coordinate mixing changes the element decomposition and therefore changes the sparse relation representation.

## 11. Spatiotemporal fingerprint

Previously tested weak nonlocal relation in a continuous medium.

| K | One-step AUC | One-step AP | Fingerprint AUC | Fingerprint AP | Top-1 fingerprint |
|---:|---:|---:|---:|---:|---|
| 0.035 | 0.9974 | 0.0427 | 1.0000 | 1.0000 | yes |
| 0.025 | 0.9921 | 0.0261 | 1.0000 | 1.0000 | yes |
| 0.020 | 0.9847 | 0.0168 | 0.9998 | 0.9951 | yes |
| 0.015 | 0.9632 | 0.0094 | 0.9971 | 0.9124 | yes |
| 0.010 | 0.9215 | 0.0052 | 0.9816 | 0.5718 | yes |
| 0.005 | 0.7349 | 0.0019 | 0.8427 | 0.1184 | no |

Conclusion: temporal structure materially improves relation identification, but sensitivity has a finite detection boundary.

## 12. Independent confirmation

Across previous controlled discovery experiments, candidate relation predictions were frozen before a fresh intervention series.

| Test | Confirmation correlation |
|---|---:|
| Random directed network | 0.999599 |
| Natural homogeneous network | 0.999975 |
| Previous discovery test | approximately 0.9996–0.99998 |

Conclusion: reproducibility of the response fingerprint is stronger evidence than a single fitted coefficient.

## 13. Weak ordinary relation: correction

A deliberately weak ordinary relation was selected from the same population as all other relations.

The full population of real relations was separable from null pairs (AUC/AP = 1.0), but the chosen weak relation ranked only 114–123/1560 across six seeds. Conditional testing of that specified pair recovered the coefficient with mean absolute error ≈0.00111 and correct sign 6/6.

Conclusion: relation testing and relation discovery are different problems. A weak relation may be real and testable without being the easiest relation to discover blindly.

## 14. What appears necessary for the current operational definition

At the resolution of the experiments, the following are required:

1. identifiable element/state variables;
2. a perturbation, intervention, or naturally occurring exogenous variation that changes the source state;
3. an observable response channel;
4. a controlled null or comparison state;
5. reproducibility beyond the null;
6. source-target identity at the claimed resolution;
7. enough signal relative to noise/background for the requested claim.

## 15. What is not necessary

The experiments do not require:

- a graph drawn in advance;
- spatial coordinates;
- Euclidean distance;
- a universal scalar K;
- a special anomalous edge;
- a particular coordinate representation;
- a nonzero conditional mean response in every stochastic system.

## 16. Current definition

The strongest operational definition surviving the battery is:

**A relation is a reproducible conditional response structure linking identifiable states, such that a controlled or exogenous change associated with one state produces a statistically distinguishable, directionally attributable response pattern in another state, relative to an appropriate null, and the pattern can be independently reproduced.**

For deterministic local systems this can reduce to a Jacobian element. For nonlinear systems it becomes state- and amplitude-dependent. For time-varying systems it becomes R(i,j,t,δ,τ). For stochastic systems it may live in conditional variance or higher-order response statistics.

## 17. What remains unresolved

The battery does not establish:

- that every physical relation is intervention-defined;
- that passive observations can always establish direct causality;
- that the identified state variables are ontologically fundamental;
- that relation exists independently of the chosen decomposition of a system into elements;
- that a universal scalar or universal metric of relation strength exists;
- that the same operational definition applies unchanged to quantum fields, spacetime geometry, or the whole universe.

## Bottom line

The evidence now strongly favors **relation as response structure** rather than relation as graph edge, correlation, or universal scalar coefficient.

The next decisive frontier is to test the definition under a genuinely autonomous continuous field where the decomposition into elements is itself arbitrary, while relation candidates are inferred from natural fluctuations and independently checked with hidden exogenous perturbations.
