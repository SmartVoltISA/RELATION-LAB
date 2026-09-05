# RELATION-MASTER-BATTERY-003 — Final Property Sweep

Date: 2026-09-05
Status: COMPLETE CURRENT SWEEP

## Purpose

This document records the final broad sweep of properties that can be tested in the present laboratory model. The aim is not to prove an ontology, but to identify which mathematical/operational properties of relation survive controls, representation changes, temporal changes, stochasticity, coarse-graining, and hidden perturbation.

No decorative separator lines are used in the report; tables are the primary record.

## A. Directness, mediation, common cause, feedback

A controlled nonlinear one-step intervention was applied with identical state and deterministic update.

| System | Target response after source intervention | Reverse response | Result |
|---|---:|---:|---|
| Direct 0→1 | 0.1785659 | 0 | direct relation |
| Indirect 0→2→1 | 0 | 0 | no one-step direct relation |
| Common cause 3→0,3→1 | 0 | 0 | dependence is not direct causation |
| Feedback 0↔1 | 0.1785659 | 0.1460602 | both directions are relations |

Conclusion: a relation is not equivalent to passive statistical dependence. Directness is defined relative to a temporal/causal resolution.

## B. Passive observation versus hidden exogenous variation

Synthetic confounding system:

`x0 = 0.8 z + 0.6 u + noise`

`x2 = 0.9 u + noise`

`x1 = 0.4 x0 + 0.7 x2 + noise`

True direct effect: 0.4.

| Estimator | Estimated effect |
|---|---:|
| Naive regression | 0.750073 |
| Instrumental variable using z | 0.406618 |

Conclusion: passive association can be biased; exogenous variation can recover the direct relation without directly intervening on the source in this model.

## C. Time-varying relation

Two-element process with coupling c(t) = 0 for 0–1499, +0.5 for 1500–2999, -0.3 for 3000–4499, 0 for 4500–5999. Window = 300 samples.

| Metric | Result |
|---|---:|
| Correlation estimated c versus true c | 0.992635 |
| RMSE | 0.036792 |
| Positive interval sign | recovered |
| Negative interval sign | recovered |
| Zero intervals | centered near zero |

Conclusion: relation can be a time-dependent object rather than a constant scalar.

## D. Delay

A relation with true delay 3 was embedded with K=0.35. Correlation of x(t-lag) with y(t+1) was evaluated for lags 0–8.

| Lag | Correlation |
|---:|---:|
| 0 | -0.00860 |
| 1 | -0.01434 |
| 2 | -0.00176 |
| 3 | **0.73225** |
| 4 | 0.45081 |
| 5 | 0.26828 |
| 6 | 0.16211 |
| 7 | 0.08582 |
| 8 | 0.05810 |

Conclusion: direction and existence of a relation can be inseparable from its temporal delay. A one-step definition can miss a real delayed relation.

## E. Nonlinear amplitude dependence

For `y_next = tanh(0.4y + 0.6 tanh(x))`, the normalized response changes with intervention amplitude.

| delta | response / delta |
|---:|---:|
| 0.05 | 0.553805 |
| 0.10 | 0.544315 |
| 0.25 | 0.511635 |
| 0.50 | 0.450152 |
| 1.00 | 0.336021 |
| 2.00 | 0.198898 |

Conclusion: there is no universal scalar strength independent of state and perturbation amplitude in nonlinear systems.

## F. State-gated relation

The source-target relation was deliberately active only when an independent context variable z was positive:

`y(t+1) = 0.5 y(t) + 0.45 x(t) I[z(t)>0] + noise`.

Regression recovered coefficients:

| Term | Estimated coefficient |
|---|---:|
| x main effect | -0.00322 |
| z main effect | 0.00075 |
| x × I[z>0] | **0.45019** |

Conclusion: a relation may be conditional on system context. The correct object is therefore a conditional response operator, not one unconditional number.

## G. Stochastic relation with zero mean signed effect

A random-sign coupling was constructed so the signed mean coupling was approximately zero while its effect changed target variance.

| Quantity | Result |
|---|---:|
| Mean signed coupling | approximately 0 |
| Target variance, low |x| | 0.8425237 |
| Target variance, high |x| | 2.7964492 |
| High/low variance ratio | **3.3191** |

Conclusion: a relation can exist in conditional variance or higher-order statistics even when its conditional mean is zero. Mean response alone is insufficient.

## H. Missing observations

For a specified direct relation, random missingness up to 80% increased uncertainty but did not destroy identification in the tested simple model.

| Missing fraction | Estimated response/δ | Standard error |
|---:|---:|---:|
| 0% | 0.200577 | 0.000999 |
| 10% | 0.200587 | 0.001051 |
| 30% | 0.201877 | 0.001202 |
| 50% | 0.200935 | 0.001428 |
| 80% | 0.202515 | 0.002266 |

Conclusion: random missingness is mainly a precision problem here. Informative/structured missingness remains an unresolved limitation.

## I. Detection power and finite resolution

For a paired direct-response experiment with delta=0.5, Gaussian noise sigma=0.05, a simple 3-sigma detection rule was simulated over 5000 Monte Carlo repetitions.

| K | n=10 | n=30 | n=100 | n=300 | n=1000 |
|---:|---:|---:|---:|---:|---:|
| 0.005 | 0.0036 | 0.0036 | 0.0042 | 0.0072 | 0.0276 |
| 0.010 | 0.0028 | 0.0048 | 0.0114 | 0.0354 | 0.2180 |
| 0.020 | 0.0070 | 0.0116 | 0.0588 | 0.3022 | 0.9292 |
| 0.040 | 0.0184 | 0.0764 | 0.4346 | 0.9688 | 1.0000 |
| 0.080 | 0.1078 | 0.5448 | 0.9962 | 1.0000 | 1.0000 |

Conclusion: “relation exists” and “relation is experimentally detectable” are different statements. Detectability depends on signal, noise, sample size and resolution.

## J. Continuum/decomposition test

A 120-element periodic discretization was treated as a continuous-like field. One weak directed contribution was placed between fine locations 17 and 83. The same dynamics was represented at multiple spatial resolutions.

| Block size | Fine elements represented per block | Hidden contribution score |
|---:|---:|---:|
| 1 | 120 | 2.000000e-03 |
| 2 | 60 | 5.000000e-04 |
| 3 | 40 | 2.222222e-04 |
| 4 | 30 | 1.250000e-04 |
| 5 | 24 | 8.000000e-05 |
| 10 | 12 | 2.000000e-05 |
| 20 | 6 | 5.000000e-06 |
| 60 | 2 | 5.555556e-07 |
| 120 | 1 | 1.388889e-07; source/target merged |

Conclusion: measured pairwise strength depends on resolution. The underlying dynamical response can remain while source-target identifiability is lost through coarse-graining.

## K. Coordinate-change test

For a linear operator A and invertible coordinate transformation y=Mx, the transformed operator was A_y=M A M^-1. The same physical input/output experiment was compared.

| Quantity | Discrepancy |
|---|---:|
| Eigenvalue set | 1.19e-09 |
| Response tau=1 | 1.82e-14 |
| Response tau=2 | 3.59e-14 |
| Response tau=4 | 5.56e-14 |
| Response tau=8 | 5.90e-14 |

Conclusion: individual matrix entries are representation-dependent, while the physical response operator is representation-covariant when input and output are transformed consistently.

## L. Geometry independence

Earlier continuous-ring tests and random directed-network tests both recovered relations when the estimator was not given coordinates or adjacency labels. The random directed case had no spatial geometry at all.

Conclusion: geometry is not required for the operational definition of relation.

## M. Representation preserving element identity

Earlier tests with X→sinh(X), X→X^3+X, and element permutations preserved relation support. Arbitrary coordinate mixing did not preserve sparse pairwise support.

Conclusion: relation is robust under reparameterization that preserves the identity of the elements being related, but pairwise sparsity is not invariant under arbitrary changes of decomposition.

## N. Spatiotemporal fingerprint and weak relations

The previously locked signal sweep in a continuous medium gave the following detection boundary.

| K | One-step AUC | One-step AP | Fingerprint AUC | Fingerprint AP | Top-1 |
|---:|---:|---:|---:|---:|---|
| 0.035 | 0.9974 | 0.0427 | 1.0000 | 1.0000 | yes |
| 0.025 | 0.9921 | 0.0261 | 1.0000 | 1.0000 | yes |
| 0.020 | 0.9847 | 0.0168 | 0.9998 | 0.9951 | yes |
| 0.015 | 0.9632 | 0.0094 | 0.9971 | 0.9124 | yes |
| 0.010 | 0.9215 | 0.0052 | 0.9816 | 0.5718 | yes |
| 0.005 | 0.7349 | 0.0019 | 0.8427 | 0.1184 | no |

Conclusion: temporal structure substantially improves identification, but sensitivity remains finite.

## O. Independent confirmation

Previous discovery experiments froze the predicted relation and then used fresh interventions.

| Experiment | Confirmation correlation |
|---|---:|
| Random directed network | 0.999599 |
| Homogeneous natural network | 0.999975 |
| Discovery experiments | approximately 0.9996–0.99998 |

Conclusion: independent reproduction of the response fingerprint is stronger evidence than one fitted parameter.

## P. Weak ordinary relation correction

A weak relation drawn from the same population as all other relations was fully testable when its pair was specified, but blind top-ranked discovery failed: the relation ranked approximately 114–123 of 1560 across six seeds.

Conclusion: relation verification and relation discovery are distinct tasks.

## Q. Current operational property map

| Property | Current status |
|---|---|
| Conditional dependence | real but insufficient for direct relation |
| Direct causal response | supported under intervention |
| Direction | supported |
| Sign | supported |
| Delay | measurable and important |
| Time variation | supported |
| State dependence | supported |
| Nonlinearity | supported; destroys universal scalar strength |
| Stochastic/higher-order relation | supported |
| Reproducibility | supported |
| Geometry independence | supported |
| Element-preserving representation robustness | supported |
| Arbitrary coordinate invariance of pairwise edges | refuted |
| Universal scalar K | refuted |
| Infinite sensitivity | refuted |
| Passive-only direct causality | insufficient in general |
| Independent confirmation | strongly supported as a validation criterion |

## R. Strongest surviving mathematical formulation

The relation should be represented as a response object rather than a scalar:

`R(i -> j | S, delta, tau, resolution, context)`

For a continuous field:

`R(r -> r', tau | S, delta, resolution, context)`

For stochastic systems, R may be a change in a conditional distribution, not merely a change in its mean.

For local deterministic dynamics `dX/dt = F(X)`, the Jacobian element `dF_j/dX_i` is one local projection of R. It is not the relation in general.

## S. Strongest current operational definition

**A relation is a reproducible conditional response structure linking distinguishable states: a controlled or exogenous change associated with one state produces a statistically distinguishable, directionally attributable change in the response distribution of another state relative to an appropriate null, with the response remaining reproducible under an independent confirmation.**

## T. What we still cannot claim

The experiments do not establish that:

- relation is an ontologically fundamental object of nature;
- the chosen state variables are fundamental;
- electrons are fundamental nodes;
- physical space is necessarily emergent from relation;
- every relation is intervention-defined;
- passive observations can always recover direct causality;
- a universal scalar measure of relation strength exists;
- the present definition transfers unchanged to quantum field theory or spacetime geometry.

## U. Final research conclusion

The broadest evidence currently favors the following hierarchy:

`element` → `state` → `response structure` → `relation representation`.

The experimentally stable content is the response structure. Graph edges, Jacobian entries and scalar coefficients are representations or projections of that structure under a chosen decomposition, scale and observable.

The remaining fundamental question is therefore no longer simply “what number is the connection?” It is:

**What invariant content of a system's dynamics remains when the decomposition into elements, coordinates, resolution and observation protocol are all changed consistently?**

That is the next frontier beyond the present battery.
