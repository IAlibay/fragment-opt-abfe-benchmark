# AMBER MC/MD simulation input files

Contained here the AMBER mdin files for the MC/MD equilibration used in the
fragment ABFE benchmark.

Each sub-directory refers to the following:

  - `min-all`: energy minimisation
  - `heat-system`: (protein & ligand restrained) NVT equilibration (500 ps)
  - `NPT-equil`: (protein & ligand restrained) NPT equilibration (5 ns)
  - `mc-phase1`: (protein & ligand restrained) NVT MC/MD equilibration (5 ns)
  - `mc-phase2`: (protein restrained) NVT MC/MD equilibration (10 ns)

Notes:
  - The `restraintmask` residue range was altered as required to match the
    protein residue range in the system investigated.
  - The `mcboxshift` parameter was adjusted per system to ensure sufficient
    coverage of the protein-ligand binding site. This was set to 12.0 for
    MCL-1, Cyclophilin D, 13.0 for PWWP1 and 15.0 for HSP90.

## Simulation order

The simulation order is:
    `min-all` -> `heat-system` -> `NPT-equil` -> `mc-phase1` -> `mc-phase2`
