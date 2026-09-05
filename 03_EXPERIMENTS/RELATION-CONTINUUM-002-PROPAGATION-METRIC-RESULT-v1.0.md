# RELATION-CONTINUUM-002 — Propagation Response as a Decomposition-Independent Metric

**Date:** 2026-09-05  
**Status:** PASS  
**Scope:** synthetic continuous wave field

## Question

If the system is treated as a continuous field and we change only the set of observed elements, does the structure of propagation survive?

The specific test is whether arrival times of a localized perturbation recover the same source-to-observer distance structure for a regular sensor decomposition and an irregular sensor decomposition.

## Model

A periodic one-dimensional wave field was simulated on a fine spectral grid of 512 points. The fine grid is the numerical carrier of one continuous-like field; the experiment does not use a hidden interaction matrix between the observed sensors.

Wave dynamics:

`u_tt = c^2 u_xx - gamma u_t`

with:

* domain length = 1;
* wave speed `c = 0.22`;
* damping `gamma = 0.03`;
* Gaussian local perturbation width `sigma = 0.015`;
* simulation duration = 2.6;
* time step = 0.0008;
* recorded every 5 integration steps.

Two incompatible observation decompositions were used:

1. 64 uniformly spaced sensors;
2. 64 randomly positioned sensors on the same physical domain.

The underlying field is identical. Only the observation/decomposition changes.

## Observable used

For each localized perturbation, the first arrival time at every sensor was detected from the normalized absolute response.

No adjacency list, graph, generating coupling matrix, or sensor-to-sensor edge list was supplied to the estimator.

The true physical circular distance was used only after the measurement for validation.

## Test A — Recovering distance from propagation time

Twenty source positions were used for each sensor decomposition. Arrival time was compared with the physical circular distance from source to sensor.

| Observation decomposition | Pearson r | Spearman rho | Arrival-time slope | Fitted RMSE | Effective speed |
|---|---:|---:|---:|---:|---:|
| Regular 64-sensor | 0.9990773 | 0.9997938 | 4.4596023 | 0.0276979 | 0.2242352 |
| Irregular 64-sensor | 0.9985553 | 0.9995322 | 4.4266009 | 0.0348446 | 0.2259070 |

The expected slope is approximately `1/c = 4.54545`. The recovered effective speeds are within about 2.7% of the generating wave speed.

## Test B — Cross-decomposition prediction

Eight source positions were held fixed in physical coordinates. The same perturbation was observed through both sensor decompositions.

The irregular-sensor arrival curve was interpolated onto the regular sensor coordinates and compared with the directly observed regular-sensor arrival curve.

| Source position | Correlation | MAE | RMSE | Max error |
|---:|---:|---:|---:|---:|
| 0.0500 | 0.999529 | 0.006853 | 0.022347 | 0.128379 |
| 0.1625 | 0.999972 | 0.002065 | 0.005107 | 0.033984 |
| 0.2750 | 0.999893 | 0.003876 | 0.010368 | 0.055208 |
| 0.3875 | 0.999979 | 0.002072 | 0.004313 | 0.022839 |
| 0.5000 | 0.999789 | 0.005823 | 0.015243 | 0.072025 |
| 0.6125 | 0.999975 | 0.001967 | 0.004828 | 0.031361 |
| 0.7250 | 0.999949 | 0.002403 | 0.006943 | 0.049252 |
| 0.8375 | 0.999988 | 0.001722 | 0.003304 | 0.015738 |
| **Mean** | **0.999884** | **0.003347** | **0.009056** | — |

## Control — destroy the decomposition-to-position correspondence

The irregular sensor labels were randomly permuted before comparing their arrival times with the physical positions.

| Control | Pearson r | Spearman rho | Fitted RMSE |
|---|---:|---:|---:|
| Correct physical correspondence | 0.9985553 | 0.9995322 | 0.0348446 |
| Random sensor-position permutation | 0.0311303 | 0.0303444 | 0.6481597 |

The propagation structure is therefore not a generic statistical artifact of the time series. It depends on the reproducible correspondence between response and physical location.

## Main result

A localized perturbation generated a propagation pattern from which the spatial distance structure could be recovered with essentially the same result under regular and irregular observation decompositions.

The robust object was not a particular sensor-to-sensor coefficient. It was the **arrival-time structure of the response**.

In this model, the relation can therefore be represented as a propagation response:

`R(source, observer, tau)`

rather than as a fixed edge between two preselected elements.

## Important consequence

This gives a concrete interpretation of the earlier observation that one system can look like a local network while another can look like a field.

A field-like system does not need a discrete object to travel from element A to element B. A perturbation changes the field, and the change has a reproducible spatiotemporal propagation pattern.

The discrete relation graph is then one possible sampling of that response structure.

## What this establishes

1. A continuous-like dynamical field can carry a recoverable relation structure without a privileged sensor decomposition.
2. Propagation time can act as an observable relational coordinate.
3. Regular and irregular discretizations recover the same propagation geometry to high accuracy.
4. Destroying the correspondence between response and physical location destroys the recovered metric.
5. A relation in a field-like system can be represented by a Green-function-like response structure rather than by a pairwise edge.

## What this does NOT establish

* It does not prove that physical space is emergent from relations.
* It does not prove that all physical fields admit a scalar travel-time metric.
* The simulated medium is homogeneous and one-dimensional.
* The result is not yet a test of anisotropic, dispersive, or genuinely multidimensional media.

## Next falsification

The next test is to remove the homogeneous-speed assumption and use an inhomogeneous or anisotropic medium. If the same procedure recovers a **dynamical metric** rather than ordinary coordinate distance, this will tell us whether the recovered geometry belongs to the propagation relation itself.

The stronger question is then:

**Does the response structure define its own notion of distance, independent of the coordinates used to describe the field?**
