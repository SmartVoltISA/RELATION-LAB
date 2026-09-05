# RELATION-CONTINUUM-012

## Nodeless stationary mode: stability and perturbation spectrum

### Question
Does the same saturable nonlinear field admit a nodeless localized stationary state that remains dynamically localized, and does a small controlled perturbation reveal a reproducible internal frequency?

### Model
2D focusing saturable nonlinear Schrodinger equation:

`i psi_t = -(1/2) Laplacian(psi) - g |psi|^2/(1+s|psi|^2) psi`

Parameters:

| Parameter | Value |
|---|---:|
| g | 4 |
| s | 1 |
| chemical potential mu | 0.5 |
| radial shooting domain | r in [0, 18] |
| stationary central amplitude | 0.8549002491 |
| stationary norm | 2.4120551 |
| stationary RMS radius | 1.18685 |
| radial nodes | 0 |

The stationary profile was obtained independently from the time-dependent breathing Gaussian by solving the radial stationary equation with regularity at the origin and decay at the outer radius.

### Real-time stability test

The stationary radial profile was interpolated onto periodic Fourier grids. No trap, reflecting wall, or external potential was added.

The state was propagated with a split-step Fourier integrator, dt=0.02, T=80.

| Grid | RMS at t=0 | RMS at t=80 | RMS min | RMS max | Norm drift |
|---|---:|---:|---:|---:|---:|
| 64 x 64 | 1.187063 | 1.187141 | 1.187063 | 1.187170 | +2.30e-12 |
| 96 x 96 | 1.187079 | 1.186500 | 1.186197 | 1.187079 | -1.22e-11 |
| 128 x 128 | 1.187104 | 1.186512 | 1.186203 | 1.187104 | +3.48e-12 |

The 96 x 96 and 128 x 128 runs agree closely. The localized state therefore remains strongly confined over this test interval, unlike the unstable excited state found in RELATION-CONTINUUM-011.

### Controlled radial perturbation

A small radial perturbation was applied to the stationary profile:

`psi(r,0) = phi(r) [1 + epsilon exp(-(r/2.5)^2)]`

with epsilon=0.01 for the main comparison and epsilon=0.005 for the longer spectral run.

For the radial observable RMS radius, after removing a quadratic trend, the dominant spectral peak was:

| Grid / box | T | epsilon | dominant frequency, cycles per time |
|---|---:|---:|---:|
| 96 x 96, L=40 | 120 | 0.01 | 0.083319 |
| 128 x 128, L=40 | 120 | 0.01 | 0.083319 |
| 128 x 128, L=50 | 120 | 0.01 | 0.083319 |
| 96 x 96, L=40 | 240 | 0.005 | 0.083326 |

The frequency resolution of the 120-time-unit runs is about 0.00833 cycles per time. The longer run improves the bin spacing to about 0.00417. The peak remains at approximately 0.0833 cycles per time.

The perturbed RMS radius remained bounded. For the T=240 run with epsilon=0.005, RMS radius ranged from 1.17313 to 1.18581 and norm drift was -3.70e-11.

### Quadrupole diagnostic

A quadrupolar perturbation was also tested. A broad low-frequency component and higher-frequency power near 0.26 to 0.30 cycles per time were observed, but the peak position changed with box size and therefore is not accepted as a converged internal eigenfrequency.

This is an important negative control: not every spectral feature is treated as a physical mode.

### Result

This experiment establishes a stronger result than RELATION-CONTINUUM-011:

1. A nodeless localized stationary solution exists for the same nonlinear field model.
2. It remains localized over the tested real-time interval on multiple spatial resolutions.
3. A controlled radial perturbation excites a reproducible dominant oscillation near 0.0833 cycles per unit time.
4. The radial frequency is stable across grid resolution and the tested box sizes.
5. The quadrupole spectrum is not yet accepted as a discrete mode because it is more sensitive to numerical box conditions.

### Interpretation

The radial result is evidence for an internal dynamical timescale of the localized nonlinear object. It is not yet a proof of a complete discrete spectrum.

The important conceptual change is that the frequency is now measured around a separately constructed nodeless stationary state, rather than around a breathing initial Gaussian. This makes the interpretation as an internal response much cleaner.

The result still belongs to the chosen nonlinear mathematical model. It does not establish electron or atom physics.

### Decision

STATUS: PARTIAL PASS.

Accepted:

`stable localized stationary state + reproducible radial response frequency`

Not yet accepted:

`complete discrete internal spectrum`

### Next required test

Compute the linearized Bogoliubov-type eigenproblem around the nodeless stationary state. Compare eigenvalues across grid sizes and box sizes, then excite individual computed eigenvectors and verify their temporal frequencies. In particular, test whether the approximately 0.0833 cycles/time radial response corresponds to a converged eigenmode rather than a nonlinear finite-amplitude oscillation.
