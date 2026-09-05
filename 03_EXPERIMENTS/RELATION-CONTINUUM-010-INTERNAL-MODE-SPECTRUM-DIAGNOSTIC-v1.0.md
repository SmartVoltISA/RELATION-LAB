# RELATION-CONTINUUM-010

## Internal-mode spectrum diagnostic

### Question
Does the self-confined nonlinear field from RELATION-CONTINUUM-009 already demonstrate a discrete set of internal modes, or does the observed motion remain dominated by a common breathing process?

### Model
2D focusing saturable nonlinear Schrödinger field:

`i psi_t = -(1/2) Laplacian(psi) - g |psi|^2/(1+s|psi|^2) psi`

Parameters:

| Parameter | Value |
|---|---:|
| Grid N | 64 x 64 |
| Box L | 40 |
| dt | 0.02 |
| T | 80 |
| g | 4 |
| s | 1 |
| Initial amplitude A | 1.8 |
| Initial Gaussian width | 2 |
| Perturbation amplitude | 0.02 |
| Sampling | every 2 integration steps |

The numerical box is periodic and much larger than the localized initial structure. No external trap or reflecting wall is used.

### Perturbations

Four cases were examined:

1. no perturbation
2. radial perturbation
3. quadrupole perturbation
4. ring perturbation

For each run, the central amplitude and RMS radius were recorded. The spectrum was computed after t > 10 after subtracting a quadratic trend.

### Results

The localized object remained bounded during the run. RMS-radius ranges were:

| Perturbation | RMS radius min | RMS radius max |
|---|---:|---:|
| none | 0.778 | 2.300 |
| radial | 0.784 | 2.380 |
| quadrupole | 0.778 | 2.281 |
| ring | 0.779 | 2.285 |

The dominant spectral peak of the central amplitude was approximately 0.300 cycles per unit time in all four cases. Representative normalized peak powers:

| Perturbation | Peak 1 frequency | Relative power | Peak 2 | Relative power |
|---|---:|---:|---:|---:|
| none | 0.300 | 1.000 | 0.600 | 0.013 |
| radial | 0.300 | 1.000 | 0.286 | 0.030 |
| quadrupole | 0.300 | 1.000 | 0.600 | 0.012 |
| ring | 0.300 | 1.000 | 0.600 | 0.012 |

A longer diagnostic run with T=100 and mode-specific observables showed the same dominant breathing band around 0.294 to 0.306 cycles per unit time. The quadrupole and cross moments also contained low-frequency components, but these did not form a clean, perturbation-selective discrete spectrum.

### Interpretation

This is NOT a positive demonstration of discrete internal modes.

What is established in this diagnostic is narrower:

1. The self-confined localized field has a strong reproducible breathing timescale.
2. Different small perturbation shapes do not replace that dominant timescale with obviously different isolated frequencies.
3. The current object therefore behaves more like a coherent nonlinear dynamical structure with a common breathing process than like an already demonstrated multi-level atom with discrete internal spectrum.

### Important control issue

The experiment above is not yet a true linearized normal-mode calculation around an exactly stationary nonlinear solution. The initial localized state itself breathes. Therefore spectral peaks can mix the base breathing motion with perturbation modes.

### Next required experiment

To test discrete internal modes properly, first obtain a numerically stationary localized solution of the same nonlinear equation to a strict residual tolerance. Then linearize the dynamics around that solution, excite radial, dipole, quadrupole, and higher-order perturbations independently, and measure whether the response contains reproducible isolated eigenfrequencies. Repeat across grid sizes and box sizes to distinguish genuine internal modes from finite-box resonances.

### Decision

STATUS: INCONCLUSIVE, diagnostic only.

The self-confined object remains interesting because a stable localized process exists without an external wall in the chosen nonlinear model, but the existence of an atom-like discrete internal spectrum has not been demonstrated.
