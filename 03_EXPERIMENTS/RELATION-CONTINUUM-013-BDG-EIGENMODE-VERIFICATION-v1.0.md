# RELATION-CONTINUUM-013

## Linearized eigenmode verification of the nodeless localized state

### Question
Does the reproducible radial frequency found in RELATION-CONTINUUM-012 correspond to a converged eigenfrequency of the linearized dynamics around the nodeless stationary state?

### Base stationary state

The same 2D focusing saturable nonlinear Schrodinger model was used:

`i psi_t = -(1/2) Laplacian(psi) - g |psi|^2/(1+s|psi|^2) psi`

with `g=4`, `s=1`, `mu=0.5`.

A nodeless radial stationary solution was recomputed independently with a large radial domain. Its central amplitude was `0.8549002483` and its norm was approximately `2.4129535`.

### Linearization

For `psi = exp(i mu t) (phi + eta)`, the perturbation was linearized as

`i d eta/dt = A eta + B eta*`

with

`A = -(1/2) Laplacian + mu - g [F(rho) + rho F'(rho)]`

`B = -g rho F'(rho)`

where `rho=phi^2` and `F(rho)=rho/(1+rho)`.

The radial Bogoliubov matrix was discretized with a finite-volume radial Laplacian and solved as a sparse eigenvalue problem.

### Eigenfrequency convergence

The smallest near-zero pair is a phase/gauge mode and decreases toward zero as radial resolution is increased. The first nonzero positive eigenfrequency converges near `0.499` to `0.501` angular frequency units.

| Radial resolution | Near-zero mode | First nonzero angular frequency | Frequency in cycles/time |
|---:|---:|---:|---:|
| 600 | 0.014912 | 0.500792 | 0.079690 |
| 1200 | 0.007440 | 0.500829 | 0.079696 |
| 1800 | 0.004968 | 0.500836 | 0.079697 |
| 2400 | 0.003715 | 0.500839 | 0.079698 |

The near-zero mode behaves as expected for the phase symmetry: its magnitude decreases with resolution. The nonzero mode is essentially unchanged.

### Box-size convergence

The stationary solution was solved on several radial domains. The first nonzero mode remained close to the same value:

| Radial domain R | First nonzero angular frequency | Cycles/time |
|---:|---:|---:|
| 12 | 0.507515 | 0.080774 |
| 15 | 0.502888 | 0.080037 |
| 18 | 0.500818 | 0.079707 |
| 22 | 0.499530 | 0.079502 |
| 26 | 0.498924 | 0.079406 |

The residual drift with increasing box size is small and moves toward a stable localized value. The mode is therefore not dominated by the outer numerical boundary.

### Direct excitation of the computed eigenmode

The computed radial eigenvector from the R=26 calculation was mapped back onto 2D grids. A small perturbation was applied to the stationary state and evolved with a split-step Fourier method.

| Grid | Box | T | Measured dominant frequency |
|---:|---:|---:|---:|
| 64 x 64 | 40 | 120 | 0.080000 |
| 96 x 96 | 40 | 120 | 0.080000 |
| 128 x 128 | 40 | 160 | 0.078571 |
| 128 x 128 | 50 | 160 | 0.078571 |

The measured frequency is consistent with the converged eigenfrequency `0.0794 to 0.0797 cycles/time`, with the remaining difference attributable to finite time spectral binning and nonlinear/finite-amplitude effects.

For the 128 x 128, L=40 run, the RMS radius stayed in the narrow interval `1.1854826 to 1.1858618`. For L=50 it stayed in `1.1854835 to 1.1858688`.

### Revision of the previous interpretation

RELATION-CONTINUUM-012 reported a broader finite-amplitude radial perturbation frequency near `0.0833 cycles/time`. The present eigenmode calculation gives a converged linear frequency near `0.0797 cycles/time`, while direct excitation of the computed eigenvector gives approximately `0.0786 cycles/time` on the longest tested 2D runs.

Therefore the earlier `0.0833` value should NOT be treated as the exact eigenfrequency. It is better interpreted as a finite-amplitude response band of the same localized object.

### Result

The experiment establishes a much stronger correspondence:

1. A nodeless localized stationary state exists.
2. The linearized operator around that state has a nonzero radial eigenfrequency near `0.0797 cycles/time`.
3. The eigenfrequency converges with radial resolution.
4. It remains approximately stable when the radial computational domain is changed.
5. Direct real-time excitation of the computed eigenmode produces the same frequency band.
6. The localized object remains strongly confined during the eigenmode excitation.

### Decision

STATUS: PASS for one radial internal eigenmode in the specified mathematical model.

This is stronger than simply observing a spectral peak. The frequency is obtained independently from the linearized operator and then reproduced by a time-domain perturbation.

Not established:

1. A complete discrete spectrum.
2. Stability of all higher modes.
3. Universality outside the chosen nonlinear equation.
4. Any physical identification with an electron or atom.

### Next experiment

Compute and classify several radial and nonradial eigenmodes around the same nodeless state. Repeat the eigenvalue and real-time verification for dipole, quadrupole, and higher modes, and check whether the number and frequencies of localized modes remain unchanged under systematic changes of grid and box size.
