# RELATION-CONTINUUM-005 — Coordinate-Invariance of Dynamical Geometry

**Date:** 2026-09-05  
**Status:** PASS (synthetic numerical test)  
**Scope:** anisotropic 2D propagation; smooth nonlinear coordinate transformation

## Question

The previous tests showed that propagation can induce a distance-like and directional geometry. The next question is stronger:

**Does the recovered dynamical geometry survive a nontrivial change of coordinates, rather than merely a change of sensor decomposition?**

The test compares the same physical propagation process in a Cartesian chart and in a smoothly warped coordinate chart.

## Model

A two-dimensional anisotropic propagation law is represented by the travel-time field

`T_s(x,y) = sqrt(((x-x_s)/c_x)^2 + ((y-y_s)/c_y)^2)`

with

- `c_x = 0.22`
- `c_y = 0.12`
- 45 x 45 observation grid
- 9 independent source positions
- periodic-free interior region used for validation

The physical inverse metric is

`G_x = diag(c_x^2, c_y^2) = diag(0.0484, 0.0144)`.

A smooth nonlinear coordinate chart was then introduced:

`q_x = x + 0.10 sin(2 pi y)`

`q_y = y + 0.07 sin(2 pi x)`.

The Jacobian determinant remained positive everywhere:

`min(det J) = 0.7236511`

`max(det J) = 1.2014497`

so the transformation is locally invertible throughout the tested region.

## Test A — Recover the metric from propagation responses

For every source, the gradient of the measured arrival-time field satisfies the anisotropic eikonal relation

`grad(T)^T G grad(T) = 1`.

Using all nine source fields, the physical-chart metric was estimated from the response gradients without supplying the generating metric to the estimator.

| Metric component | True | Estimated | Absolute error |
|---|---:|---:|---:|
| G_xx | 0.0484000000 | 0.0484000001 | 1.0e-10 |
| G_xy | 0 | -1.7e-18 | 1.7e-18 |
| G_yy | 0.0144000000 | 0.0144000000 | <1e-10 |
| Eikonal RMSE | — | 1.89e-09 | — |

## Test B — Transform the same response into a curved coordinate chart

The measured gradient transforms as

`grad_q(T) = J^{-T} grad_x(T)`.

The contravariant metric transforms as

`G_q = J G_x J^T`.

The same physical response therefore satisfies

`grad_q(T)^T G_q grad_q(T) = 1`.

Using the transformed response, the numerical eikonal residual was:

| Quantity | Result |
|---|---:|
| q-chart eikonal RMSE | 1.89e-09 |
| q-chart maximum absolute residual | 1.49e-08 |
| determinant transformation error | 3.33e-16 |

The physical law is therefore preserved to numerical precision even though the coordinate representation of the metric changes from a diagonal constant matrix to a spatially varying tensor.

## Test C — Add measurement noise

Arrival-time noise with standard deviation `0.0005` was added before numerical differentiation. Local metric estimates were obtained independently from the nine source responses.

| Quantity | Result |
|---|---:|
| Physical-chart mean metric-vector error | 5.248e-04 |
| Physical-chart median metric-vector error | 3.708e-04 |
| Warped-chart mean relative metric error | 1.006% |
| Warped-chart median relative metric error | 0.656% |
| Mean physical-chart fit residual | 0.01327 |

The coordinate change does not destroy the recoverability of the underlying geometry; it changes the coordinate components in exactly the way required by tensor transformation.

## Critical control

A naive Euclidean distance measured directly in the warped chart is not equivalent to physical distance. The nonlinear chart intentionally distorts lengths and angles.

Thus the experiment distinguishes:

1. **coordinate geometry** — changes under the chart transformation;
2. **dynamical geometry** — transforms covariantly and preserves the physical response predictions.

## Main result

**PASS.**

The same propagation-response structure defines the same physical geometry in two nonlinearly related coordinate descriptions.

The numerical matrix components of the metric are not invariant. The transformation law of the response geometry is invariant.

This is the important distinction:

`invariant relation` does not mean `same numbers in every coordinate system`.

It means:

`same physical predictions after the correct transformation of representation`.

## What this establishes

1. A propagation response can define a geometric object whose coordinate components change under a nonlinear coordinate transformation.
2. The physical content of that object survives the coordinate change.
3. A scalar graph edge or fixed matrix coefficient is therefore too representation-specific to be the fundamental relational object.
4. The response/metric structure behaves like a geometric object: representation changes, predictive content remains.
5. The distinction between coordinate-dependent description and relationally meaningful response survives a nontrivial curved chart.

## What this does NOT establish

- It does not prove that physical spacetime is emergent from relations.
- It does not prove that every dynamical system possesses a metric tensor.
- The propagation law was prescribed and reciprocal.
- The experiment does not yet include nonreciprocity, topology, dispersion, or a dynamically evolving metric.

## Consequence

The research target should now be upgraded again.

We are no longer primarily searching for:

`K_ij`

or even only for:

`R(i -> j, tau)`.

The stronger candidate is:

`R[perturbation -> field response]`

with its induced transformation law under changes of observation coordinates.

A relation is increasingly looking less like an object **between** two things and more like a rule governing **possible transformations of the whole system**.

## Next falsification target

Remove reciprocity.

Use a medium where propagation from A to B differs from B to A, then test whether the response structure induces a directed/non-symmetric geometry and whether the same object survives incompatible coordinate transformations.

That is the next serious boundary: **relation as geometry without symmetry**.
