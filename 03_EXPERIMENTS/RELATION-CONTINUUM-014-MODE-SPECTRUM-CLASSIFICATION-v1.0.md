# RELATION-CONTINUUM-014

## Internal mode spectrum classification and finite-box control

### Question
Does the nodeless localized state contain several genuine internal modes, or is only the first radial mode robust while higher spectral features belong to the numerical continuum or outer boundary?

### Model
The same 2D focusing saturable nonlinear Schrodinger equation was used:

`i psi_t = -(1/2) Laplacian(psi) - g |psi|^2/(1+s|psi|^2) psi`

with `g=4`, `s=1`, `mu=0.5`.

The nodeless stationary radial solution was recomputed independently for each radial domain. The linearized Bogoliubov operator was discretized in radial angular sectors `m=0,1,2,3`.

### Radial-resolution control

For the first radial mode in the `m=0` sector, the positive angular frequency converges as follows:

| Radial intervals | Angular frequency | Cycles/time |
|---:|---:|---:|
| 600 | 0.499018 | 0.079421 |
| 1200 | 0.498972 | 0.079414 |
| 1800 | 0.498964 | 0.079413 |

The variation over this resolution range is below `1e-5` cycles/time.

### Angular-sector spectrum at R=26

The lowest oscillatory frequency in each angular sector was:

| Angular sector m | Angular frequency | Cycles/time |
|---:|---:|---:|
| 0 | 0.498964 | 0.079413 |
| 1 | 0.511303 | 0.081376 |
| 2 | 0.519494 | 0.082680 |
| 3 | 0.530108 | 0.084369 |

These values alone are not sufficient to call all four modes physical because angular sectors with nonzero `m` must pass the finite-box test.

### Finite-box control

The lowest oscillatory frequency was recomputed at three radial domain sizes:

| R | m=0 | m=1 | m=2 | m=3 |
|---:|---:|---:|---:|---:|
| 18 | 0.079713 | 0.083479 | 0.086037 | 0.089574 |
| 22 | 0.079509 | 0.082127 | 0.083908 | 0.086270 |
| 26 | 0.079414 | 0.081376 | 0.082680 | 0.084369 |

Interpretation is based on convergence as `R` increases. The `m=0` mode changes only slightly and approaches a stable localized value. The lowest `m=1`, `m=2`, and `m=3` frequencies drift substantially with the outer domain and therefore are not accepted as converged internal eigenfrequencies in this experiment.

### Higher radial features

In the `m=0` sector at `R=26`, the first several oscillatory frequencies in cycles/time were approximately:

`0.079414, 0.082370, 0.087937, 0.096187, 0.107062, 0.120507, 0.136470, 0.154910`.

The second value shifts to approximately `0.086214` at `R=18` and `0.083712` at `R=22`, so it is also sensitive to the outer domain. It is therefore not accepted as a genuine discrete internal mode.

### Stability indicators

Near-zero modes occur in `m=0` and `m=1` sectors. Their small real eigenvalues decrease as radial resolution is increased, consistent with numerical representations of symmetry-related zero modes rather than a finite-frequency instability. For `m=0`, the magnitude decreased from approximately `0.0243` at 600 intervals to `0.0081` at 1800. For `m=1`, it decreased from approximately `0.0152` to `0.0051` over the same resolution range.

The nonzero `m=2` and `m=3` modes showed no comparable real growth in the tested eigensolver window.

### Result

The combined controls sharpen the previous conclusion:

1. One radial internal mode near `0.0794 cycles/time` is robust against radial resolution and outer-domain changes.
2. The previously observed direct-excitation frequency near `0.0786 cycles/time` is consistent with this converged radial eigenmode.
3. Several additional spectral features exist mathematically in the discretized operator, but the lowest nonradial and higher radial features move with the outer domain and are therefore not yet established as localized discrete modes.
4. The experiment rejects the temptation to interpret every spectral line as an internal level.

### Decision

STATUS: PASS for one converged internal radial mode; INCONCLUSIVE for a multi-mode discrete spectrum.

The strongest currently supported statement is:

`continuous nonlinear field -> nodeless localized state -> converged internal radial eigenmode`

A complete atom-like spectrum has not been demonstrated.

### Next experiment

Compute the full 2D linearized eigenproblem with localization and box-size criteria applied to every eigenmode. Then independently excite the accepted nonradial candidates in time domain. A mode should be accepted only if its eigenfrequency, spatial localization, and measured temporal frequency remain stable under grid and box changes.
