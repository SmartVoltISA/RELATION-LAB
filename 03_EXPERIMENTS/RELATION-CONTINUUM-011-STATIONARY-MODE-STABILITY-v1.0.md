# RELATION-CONTINUUM-011

## Stationary localized mode and stability diagnostic

### Question
Can the self-confined nonlinear field be converted from a breathing initial condition into a stationary localized state, and does that state remain dynamically stable when evolved without an external trap?

### Model
2D focusing saturable nonlinear Schrödinger equation:

`i psi_t = -(1/2) Laplacian(psi) - g |psi|^2/(1+s|psi|^2) psi`

Parameters:

| Parameter | Value |
|---|---:|
| g | 4 |
| s | 1 |
| radial chemical potential mu | 0.5 |
| radial domain | r in [0, 15] |
| stationary center amplitude | 1.2597035429 |
| stationary norm | 16.158556803 |
| stationary RMS radius | 3.4409664829 |
| radial node count | 1 |
| node radius | 1.6566210394 |

The stationary radial profile was obtained by solving the radial boundary-value problem

`0.5(phi'' + phi'/r) + g phi^3/(1+phi^2) - mu phi = 0`

with `phi'(0)=0` and `phi(15)=0`.

The resulting state is not the nodeless ground state. It is a radial excited stationary solution with one sign change.

### Discretization check

The radial solution was interpolated onto periodic 2D Fourier grids. The continuum stationary residual on the 128 x 128 grid was:

| Quantity | Value |
|---|---:|
| residual RMS | 0.0002772989 |
| residual maximum | 0.0042326858 |
| interpolated norm | 16.15694882 |

### Real-time stability test

The stationary profile was evolved with a split-step Fourier integrator. No trap, reflecting wall, or external potential was added.

Short-time convergence of RMS radius:

| Grid | t=0 | t=10 | t=19 |
|---|---:|---:|---:|
| 64 x 64 | 3.440964 | 3.4557 approx. | not used for final long test |
| 96 x 96 | 3.440961 | 3.441726 | 3.442077 |
| 128 x 128 | 3.440906 | 3.441831 | 3.447564 |

The 96 and 128 grids agree closely through the first ~10 time units, showing that the initial stationary profile is not merely a coarse-grid artifact.

At longer time the 128-grid run begins to grow in width, while the 64-grid run shows much stronger growth. This indicates a genuine stability question rather than a clean stable mode.

A previous 64 x 64, T=40 diagnostic gave RMS width range approximately 3.44 to 10.01 for the unperturbed stationary profile. This long run should be treated as a stability/instability indication, not as a converged quantitative growth rate.

### Result

A stationary localized solution can be constructed for the same nonlinear field model, including a solution with norm approximately equal to the norm used in the earlier self-confined experiment.

However, the particular solution found here has one radial node and is not demonstrated to be dynamically stable. Grid-converged evolution is initially stationary to high accuracy, then develops slow growth of the RMS radius at longer times.

Therefore the experiment does NOT yet establish a stable atom-like internal mode.

### What changed relative to RELATION-CONTINUUM-010

The previous diagnostic started from a breathing Gaussian and therefore mixed the object's base breathing motion with perturbation spectra.

This experiment removes that ambiguity partially by constructing an explicit stationary nonlinear state first.

The remaining problem is stability. Before extracting internal frequencies, the next calculation must determine whether a stable nodeless stationary branch exists and whether its linearized spectrum contains isolated eigenfrequencies.

### Decision

STATUS: PARTIAL PASS / STABILITY UNRESOLVED.

Established:

1. The nonlinear equation admits localized stationary radial solutions.
2. A stationary solution can be constructed independently of the earlier breathing trajectory.
3. The solution is initially stable under direct real-time propagation at multiple grid resolutions.

Not established:

1. Long-time nonlinear stability.
2. Existence of a stable nodeless stationary branch at the relevant norm.
3. A discrete internal spectrum independent of finite-box effects.
4. Any physical identification with an electron or atom.

### Next experiment

Continue from the stationary-solution family, not from a breathing Gaussian. Map the nodeless and excited branches as a function of chemical potential and norm. For each converged stationary state, compute the linearized Bogoliubov-type eigenproblem and compare eigenfrequencies across grid sizes and box sizes. Then excite individual eigenvectors and verify that the observed temporal response matches the predicted mode frequency.
