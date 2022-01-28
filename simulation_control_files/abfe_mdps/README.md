# Absolute binding free energy MDP files

Contained here are MDP files used for the three different steps of the
absolute binding alchemical cycle. Two variants of these MDP files are provided
under the folders `2fs` and `4fs`, intended for systems using standard mass
and hydrogen mass repartitioning respectively. The three ABFE steps consist
of `coul` the annhilation of partial charges, `vdw` the decoupling of Van der
Waals interactions, and `restraints` the addition of orientational restraints.

## Contents

The directories for each step have the following tree structure:

step
├── em
│   └── em.mdp
├── nvt
│   └── nvt.mdp
├── npt
│   └── npt.mdp
├── npt-norest
│   └── npt-norest.mdp
└── prod
    └── prod.mdp


Each sub-directory refers to the following:

  - `em`: energy minimisation
  - `nvt`: (restrained) NVT equilibration (10 ps)
  - `npt`: (restrained) NPT equilibration (100 ps)
  - `npt-norest`: NPT equilibration (500 ps)
  - `prod`: NPT production (20 ns)

## Simulation order

The order of simulation is `em` -> `nvt` -> `npt-norest` -> `prod`.
