# GROMACS MD conventional MD simulation input files

Contained here the GROMACS mdp files for the pre-ABFE conventional MD
simulations dones as part of the fragment optimisation ABFE benchmark.

Each sub-directory refers to the following:

  - `emin`: energy minimisation
  - `nvt_heat`: (restrained) NVT equilibration (1 ns)
  - `npt_equil1`: (restrained) NPT equilibration (1 ns)
  - `npt_equil2`: NPT equillibration (5 ns)
  - `npt_prod1`: NPT production (20 ns)

## Simulation order

The simulation order is:
    `emin` -> `nvt_heat` -> `npt_equil1` -> `npt_equil2` -> `npt_prod1`
