# RELATION-CONTINUUM-004 — Directional Geometry from Anisotropic Propagation

**Date:** 2026-09-05  
**Status:** PASS  
**Scope:** synthetic two-dimensional continuous wave field

## Question

The previous experiment showed that a field can induce a dynamical distance. The stronger question is whether the relation structure can also contain directionality.

If propagation is anisotropic, a scalar distance is insufficient. The response should distinguish different directions from the same source.

## Model

A periodic two-dimensional wave field was simulated on a 64 x 64 fine grid.

Dynamics:

`u_tt = c_x^2 u_xx + c_y^2 u_yy - gamma u_t`

An anisotropic medium was used with:

* `c_x = 0.22`
* `c_y = 0.12`
* damping = 0.01
* Gaussian source width = 0.018
* time step = 0.001
* duration = 1.8

The response was observed over the complete two-dimensional field.

## Observable

The estimator uses only the first-arrival time of the response at each spatial observation point.

No adjacency graph or interaction matrix is supplied.

## Directional test

Arrival times were measured along the x and y axes from the same source.

Using a linear fit of arrival time against coordinate displacement, the recovered effective propagation speeds were:

| Direction | Effective speed |
|---|---:|
| x | 0.24418 |
| y | 0.14820 |
| y/x ratio | 0.60693 |

The generating ratio was `0.12 / 0.22 = 0.54545`.

The absolute values are biased by finite pulse width, threshold arrival definition, and the numerical wavefront, but the directional asymmetry is recovered strongly.

## Isotropic control

The same numerical experiment was repeated with `c_x = c_y = 0.17`.

| Medium | Effective x speed | Effective y speed | y/x ratio |
|---|---:|---:|---:|
| Anisotropic | 0.24418 | 0.14820 | 0.60693 |
| Isotropic control | 0.18790 | 0.18790 | 1.00000 |

The directional difference disappears in the isotropic control.

## Full-field metric comparison

A direction-dependent travel-time metric was compared with ordinary Euclidean coordinate distance.

For the anisotropic medium:

`d_dyn = sqrt((dx/0.22)^2 + (dy/0.12)^2)`

The measured arrival map gave:

| Candidate structure | Correlation with arrival | RMSE after linear fit |
|---|---:|---:|
| Direction-dependent dynamical metric | 0.956390 | 0.074474 |
| Euclidean coordinate distance | 0.949907 | 0.079686 |

The difference in global correlation is modest because both structures preserve radial ordering, but the axis experiment reveals the essential directional information that Euclidean distance cannot represent.

## Main finding

The response structure contains more than pairwise influence and more than scalar distance.

It can encode a **direction-dependent geometry of propagation**.

In this model, relation is better represented by a response kernel or propagation operator than by a symmetric scalar relation between two elements.

A useful conceptual form is:

`R(r_source, r_observer, tau | state, direction)`

or, at the local level, a response tensor rather than a single coefficient.

## What this establishes

1. An anisotropic field produces direction-dependent propagation that is recoverable from response timing alone.
2. The directional structure survives the same observable framework used for the scalar dynamical metric.
3. An ordinary graph edge is insufficient to represent the complete relation in a field-like system.
4. The natural relational object is becoming a spatiotemporal response operator with direction and memory.

## What this does NOT establish

* It does not prove a universal physical metric.
* The simulated anisotropy is prescribed rather than emergent.
* The medium is reciprocal and linear in its principal propagation law.
* More complex effects such as dispersion, nonreciprocity, topology, and nonlinear state dependence remain open.

## Consequence for the research program

The investigation has now crossed an important boundary.

The question is no longer only whether A affects B.

The stronger object being recovered is:

**how a perturbation changes the set of possible future responses of the system across space, time, direction, and resolution.**

The next decisive falsification is therefore to test whether this response structure can remain identifiable when the coordinate system itself is changed nontrivially, including curved coordinates and incompatible sensor layouts, while the underlying field dynamics are unchanged.
