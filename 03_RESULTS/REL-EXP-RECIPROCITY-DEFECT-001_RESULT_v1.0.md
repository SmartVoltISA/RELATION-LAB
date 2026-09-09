# REL-EXP-RECIPROCITY-DEFECT-001 — Result v1.0

Date: 2026-09-09

## Outcome
**SUPPORT**

The tested reciprocity defect

`rho(R) = ||R-R^T||_F / ||R+R^T||_F`

was zero for all paired symmetric controls to numerical precision and positive for all tested generic directed systems across four deterministic response operators.

## Evidence
- 80 directed realizations tested.
- 80 paired symmetric controls tested.
- 4 operators: direct, square, matrix exponential, resolvent.
- Maximum symmetric-control defect < 1e-16.
- Directed defect positive in every tested realization/operator pair.

## Interpretation
The result independently reproduces the Ω-Math operator-robustness finding inside RELATION-LAB. It supports a narrow structural statement: reciprocity can be tested as a property of a declared response matrix without dependence on node labels or response units.

It does not establish that all physical systems expose their intrinsic relation structure through such a response matrix.

## Promotion status
**Not foundational yet.**

Required next evidence: perturbation/noise robustness and explicit implementation as a typed Ω-Math derived invariant, followed by an audit for hidden physical assumptions.
