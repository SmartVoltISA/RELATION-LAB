# RELATION-MASTER-BATTERY-001

## Purpose

Consolidated falsification battery for the operational concept of relation.

The goal is to separate dependence, directness, direction, reproducibility, temporal structure, representation robustness, geometry dependence, and independent confirmation.

## Property matrix

| Property | Test | Result | Status |
|---|---|---|---|
| Dependence | Passive correlation / regression | Can appear under common cause and indirect paths | INSUFFICIENT |
| Direct effect | Controlled one-step intervention | Direct case responds immediately; indirect case has zero one-step direct response | SUPPORTED |
| Direction | Source intervention vs reverse intervention | Direct 0→1 response 0.2882; reverse 1→0 = 0 in nonlinear controlled test | SUPPORTED |
| Reproducibility | Independent seeds / fresh interventions | Repeated across prior controlled experiments | SUPPORTED |
| Sign | Signed response | Positive and negative relations recovered in prior multi-seed tests | SUPPORTED |
| Temporal fingerprint | Multi-step response | Temporal profile improves discrimination and identifies mediated vs direct response | SUPPORTED |
| Representation invariance | Element-preserving transforms | Support preserved under sinh and x^3+x; random element permutation preserved | SUPPORTED |
| Coordinate mixing invariance | Random invertible mixing | Sparse relation support becomes dense and original edge labels are no longer directly recoverable | REFUTED |
| Geometry dependence | Ring vs random directed network | Relation recovery succeeded with no spatial geometry | NOT REQUIRED |
| Special anomaly requirement | Homogeneous natural network | Ordinary strongest relation recovered without injected hidden anomaly | NOT REQUIRED |
| Weakness independence | Weak ordinary relation | Population-level recovery succeeds; blind top-rank discovery of a weak relation can fail | LIMITED |
| Independent confirmation | Freeze prediction then new intervention | Prior runs achieved fingerprint correlation ≈0.9996–0.99998 | SUPPORTED |
| Passive-only causality | Observation without direct source intervention | Confounding and indirect dependence remain; direct causal identification is not guaranteed | INSUFFICIENT |

## Current controlled ablation run

Four systems were tested with the same nonlinear intervention protocol.

| System | Mean normalized 0→1 response | SD | Mean 1→0 response | Interpretation |
|---|---:|---:|---:|---|
| Direct 0→1 | 0.288206 | 0.047348 | 0.000000 | Immediate direct relation |
| Indirect 0→2→1 | 0.000000 | 0.000000 | 0.000000 | No one-step direct relation 0→1 |
| Common cause 3→0, 3→1 | 0.000000 | 0.000000 | 0.000000 | Dependence can exist without direct causal response |
| None | 0.000000 | 0.000000 | 0.000000 | Null |

This run used 1000 paired interventions per ordered test. Perturbed and control trajectories shared the same noise realization, isolating the intervention effect.

## Passive observation control

A separate long passive simulation shows why correlation is not enough.

| System | Passive coefficient 0→1 | Passive coefficient 1→0 |
|---|---:|---:|
| Direct 0→1 | 0.15269 | 0.00156 |
| Indirect 0→2→1 | 0.04207 | 0.00425 |
| Common cause 3→0,3→1 | 0.04361 | 0.04106 |
| None | 0.00093 | 0.00200 |

The common-cause case produces apparent directional coefficients despite no direct 0→1 relation. Therefore passive predictive dependence is not sufficient for direct causal identification.

## Previously locked experiments incorporated into the battery

### Continuous weak local recovery

A continuous analog-like 40-element system with local and second-neighbor coupling gave passive local-Jacobian recovery ROC-AUC = 0.754821, while a time-shuffled control gave ROC-AUC = 0.541772. This establishes signal but also demonstrates the difficulty of passive recovery in correlated many-element media.

### Time-varying two-element relation

The locked two-variable time-varying coupling experiment recovered the coupling trajectory with aggregate correlation 0.991959, RMSE 0.059889, and active-state ROC-AUC/AP = 1.0/1.0. The shuffled control gave correlation -0.027637 and RMSE 0.475303.

### Nonlinear causal recovery

The locked nonlinear 8-variable intervention experiment recovered all direct ordered relations across six seeds with AUC = 1.0 and AP = 1.0. Correlation between true and estimated coefficients was approximately 0.993–0.997 across seeds.

### Representation invariance

Element-preserving nonlinear transformations preserved relation support and recovery. A random coordinate mixing transformation did not preserve sparse source-target support. Therefore the relation is robust to reparameterization that preserves element identity, but it is not invariant to arbitrary coordinate mixing that changes the decomposition into elements.

### Continuous medium without geometry supplied to estimator

A blind continuous-medium intervention test recovered sparse nonlocal direct relations with mean ROC-AUC ≈0.9468 and mean AP ≈0.5402 across seeds, compared with shuffled-source mean AUC ≈0.4433. This is positive but not perfect under severe class imbalance.

### Full spatiotemporal fingerprint

In a 40-element continuous ring with one weak nonlocal relation, a multi-step signed temporal fingerprint achieved AUC = 1.0 and AP = 1.0. The subsequent signal sweep showed top-1 recovery down to K = 0.010, with degradation at K = 0.005. This is a model-specific detection boundary, not a universal constant.

### Random directed network without geometry

A 40-element random directed network with 120 background relations and no geometry recovered a distinguished relation with AUC/AP = 1.0 and independently confirmed its 8-step response with correlation 0.999599 and RMSE 0.001781. A null with the relation removed did not systematically recover it.

### Natural network without a special hidden edge

All relations were generated from the same distribution. No anomaly relation was injected. The strongest ordinary relation was recovered across six seeds with AUC/AP = 1.0, direction correct in 6/6, and mean prediction/confirmation correlation = 0.999975.

### Weak ordinary relation discovery correction

The previous report claimed blind top-ranked discovery of a weak ordinary relation. Rechecking showed that claim was too strong. The full relation population remained separable (AUC/AP = 1.0), but the selected weak relation ranked only 114–123/1560. Conditional testing of the specified pair remained accurate. This correction is important: testing a proposed relation and discovering an unknown relation are different tasks.

## Necessary versus sufficient properties

The current evidence suggests the following operational hierarchy.

### Necessary for the present causal definition

1. A defined intervention or perturbation channel.
2. An observable state variable or response measure.
3. A measurable difference between intervention and control.
4. Repeatability beyond the controlled null.
5. Source-target identity, at least at the resolution at which the relation is claimed.

### Sufficient within the tested model class

For a proposed directed relation i→j, the following criterion has worked:

`controlled intervention on i`

`→ reproducible response in j`

`→ stable sign/direction`

`→ predicted temporal response`

`→ independent confirmation`

This is sufficient as an operational criterion inside the tested dynamical model classes. It is not a theorem about all physical systems.

## Critical distinction

A nonzero parameter is not automatically an experimentally established relation.

A correlation is not automatically a direct relation.

A predictive coefficient is not automatically causal.

A graph edge is not the relation itself; it is a representation of a relation that has already been defined or inferred.

## Working definition after the battery

For the current research program, a directed relation between i and j is provisionally:

**a reproducible, statistically distinguishable response structure in j produced by a controlled perturbation of i, with identifiable direction and a response fingerprint that survives an independent confirmation experiment.**

The scalar coefficient is only one projection of that response structure.

## Main unresolved question

The strongest remaining conceptual dependency is intervention.

The current definition says what relation means operationally when we are allowed to perturb a source. It does not yet tell us whether the same relation can be established from the autonomous dynamics of a system without direct source intervention.

Therefore the next decisive experiment is a passive/latent-perturbation test with hidden exogenous shocks, instrumental variables, and adversarial confounding controls. The target is not to prove that passive data always suffice, but to determine exactly which information about a relation is irreducibly supplied by intervention.

## Final status

The battery supports a robust operational concept of relation as **reproducible response structure**, not as a graph line or universal scalar.

The ontology question remains open.
