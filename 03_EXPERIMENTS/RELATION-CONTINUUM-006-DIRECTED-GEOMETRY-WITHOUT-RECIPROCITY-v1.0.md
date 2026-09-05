# RELATION-CONTINUUM-006 — Directed Geometry Without Reciprocity

**Date:** 2026-09-05  
**Status:** PASS (synthetic numerical test)  
**Scope:** continuous 1D periodic transport; unequal right/left propagation speeds; coordinate warp control

## Question

Can a relation define a geometric structure that is intrinsically directional, so that the effective distance from A to B differs from B to A?

The experiment removes reciprocity from the previous continuum model and asks whether directional structure can be recovered from observed propagation responses.

## Dynamical model

A periodic one dimensional medium carries two continuously transported components:

`u_R,t + c_R u_R,x = -gamma u_R`

`u_L,t - c_L u_L,x = -gamma u_L`

with

- domain length `L = 1`
- `N = 160` spatial samples
- `dt = 0.002`
- `500` time steps
- rightward speed `c_R = 0.32`
- leftward speed `c_L = 0.14`
- damping `gamma = 0.15`
- impulse split equally between right and left components

The total observed response is `u = u_R + u_L`.

The dynamics are genuinely nonreciprocal because the two propagation directions have different speeds.

## Test A — Recover directional propagation from responses

For 20 source positions, the complete temporal response was recorded at every target. The first resolved response peak was used as the arrival-time estimate.

For a separation of `d` spatial cells, the expected travel times are

`t_R = d*dx/c_R`

`t_L = d*dx/c_L`.

Representative results:

| Separation | Expected right | Measured right | Expected left | Measured left |
|---:|---:|---:|---:|---:|
| 1 cell | 0.01953 | 0.018 | 0.04464 | 0.044 |
| 5 cells | 0.09766 | 0.096 | 0.22321 | 0.222 |
| 10 cells | 0.19531 | 0.194 | 0.44643 | 0.444 |
| 20 cells | 0.39063 | 0.388 | 0.89286 | 0.886 |

Across separations 1 to 20 cells and 20 source positions:

| Quantity | Right propagation | Left propagation |
|---|---:|---:|
| Mean timing error | -0.00158 | -0.00395 |
| Timing error SD | 0.00060 | 0.00174 |

The direction of propagation is therefore recoverable directly from the temporal response.

## Test B — Reciprocity control

The same simulation was repeated with

`c_R = c_L = 0.23`.

The measured directional asymmetry was exactly zero at the tested numerical resolution:

| Metric | Reciprocal control |
|---|---:|
| Mean `(t_L - t_R)` | 0.00000 |
| SD | 0.00000 |
| Maximum absolute asymmetry | 0.00000 |

This is the required negative control: the directional signature disappears when reciprocity is restored.

## Test C — Directional asymmetry

For the nonreciprocal medium, the mean difference between the same-distance left and right travel times was

`mean(t_L - t_R) = 0.26130`

with SD `0.14354`.

For 20-cell separation:

`t_R = 0.388`

`t_L = 0.886`

so the same physical separation has a travel time ratio of approximately

`0.886 / 0.388 = 2.28`.

The relation is therefore not representable by an ordinary symmetric distance `d(A,B)=d(B,A)`.

## Test D — Coordinate warp

A smooth nonlinear coordinate chart was applied:

`q(x) = x + 0.08 sin(2*pi*x)`.

Its Jacobian is

`dq/dx = 1 + 0.16*pi*cos(2*pi*x)`

with

- minimum Jacobian `0.4973452`
- maximum Jacobian `1.5026548`

so the coordinate transformation remains locally invertible.

The measured arrival times themselves do not change under this reparameterization. What changes is the coordinate expression of local propagation speed.

Thus the invariant object is not the numerical speed written in a particular coordinate chart. The invariant object is the directed response structure: which perturbation reaches which region, in which temporal order, and with what travel time.

## Main result

**PASS.**

A nonreciprocal dynamical medium produces a recoverable directed geometric structure.

The data require a generalized distance or travel-time relation of the form

`D(A,B) != D(B,A)`.

The ordinary symmetric metric is therefore not fundamental enough to describe this class of relational dynamics.

## What this establishes

1. Directionality can be recovered from propagation responses without assuming a symmetric relation.
2. A controlled reciprocity restoration removes the directional signature.
3. The response structure contains more information than an ordinary scalar distance.
4. Coordinate changes alter the numerical representation of local speed while preserving the observed directed response.
5. A plausible next mathematical object is a **directed/Finsler-like relational geometry**, rather than necessarily a Riemannian metric.

## What this does NOT establish

- It does not prove that physical spacetime has Finsler geometry.
- It does not prove that all physical relations are nonreciprocal.
- The two propagation speeds were prescribed by the model.
- The experiment does not yet derive directionality from an unknown microscopic ontology.

## Consequence for the relation program

The working hierarchy becomes:

`coefficient -> pairwise response -> spatiotemporal response fingerprint -> induced geometry`

and the induced geometry may be symmetric or directed depending on the dynamics.

The deeper candidate is therefore not a fixed connection value but the transformation rule for possible responses.

## Next falsification target

The next test should remove the known spatial ordering as well. Give the observer only the temporal response fingerprints, without coordinates or source-target labels, and ask whether it can reconstruct both the relational neighborhoods and the direction field from the response data alone.

That test attacks the remaining assumption that the elements and their positions are already known.
