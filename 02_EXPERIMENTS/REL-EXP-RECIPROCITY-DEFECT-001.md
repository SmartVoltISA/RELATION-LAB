# REL-EXP-RECIPROCITY-DEFECT-001 — Reciprocity defect across response operators

Date: 2026-09-09
Hypothesis link: H2 — Relation may be directional

## Question
Can a declared response matrix be assigned a label-independent scalar reciprocity defect that is zero for reciprocal structure and remains discriminative for directed structure across multiple deterministic response operators?

## Candidate

`rho(R) = ||R - R^T||_F / ||R + R^T||_F`

Domain restriction: denominator must be nonzero.

## Protocol
For N in {8,12,20,32}, generate 20 directed weighted matrices. For each directed matrix A construct a paired symmetric control S=(A+A^T)/2. Normalize inputs by Frobenius norm. Apply exactly the same operator to both members of every pair.

Operators:
- direct A
- A^2
- exp(A)
- (I - 0.2A)^(-1)

Total: 80 directed systems and 80 paired symmetric controls.

## Preregistered acceptance logic
1. Symmetric controls must have rho numerically zero.
2. Directed systems must have positive rho unless structurally reciprocal.
3. The scalar must be unchanged by node relabelling and positive rescaling of the declared response matrix.
4. The test must not claim physical causality, geometry, time, or energy.

## Result
All 80 symmetric controls were reciprocal to numerical precision for every operator. Maximum control rho was <1e-16.

All 80 directed systems had positive rho for every tested operator.

Means across directed systems:
- direct: 0.841527
- A^2: 0.678417
- exp(A): 0.162125
- resolvent: 0.033247

Ranges:
- direct: 0.491532–1.000000
- A^2: 0.160389–1.000000
- exp(A): 0.108686–0.250275
- resolvent: 0.022086–0.050565

## Classification
**SUPPORT** for the narrow mathematical hypothesis.

This is an operational invariant of the declared response matrix, not a proof of a universal physical directional law.

## Limitations
- rho is not a complete classifier of directed structures.
- A physical observation process may alter the response object before rho is evaluated.
- Coarse-graining is not assumed invariant.
- The result is independent confirmation in RELATION-LAB, but additional model classes and perturbation/noise tests remain required before foundational promotion.
