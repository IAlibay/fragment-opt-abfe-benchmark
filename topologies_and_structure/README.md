# Topology and structure input files

Included here are the input topology and structures used for each of the ligands in this work.

## Directory structure and contents

<system>
└── ligand-<id>
    ├── complex
    │   ├── abfe
    │   │   ├── coul
    │   │   ├── restraint
    │   │   └── vdw
    │   ├── amber
    │   └── gromacs
    │
    └── ligand
        ├── abfe
        │   ├── coul
        │   └── vdw
        └── gromacs


### `<system>`

These top level directories exist for each of the four systems investigated in
this benchmark (`MCL-1`, `HSP90`, `CylophilinD`, and `PWWP1`).


### `<system>/ligand-<id>`

Under each `<system>` directory are individual directories for each of the
ligands investigated. Here `<id>` refers to the ligand identification number
as described in the initial fragment optimisation study (see Text S1).

Each ligand directory has two sub-directories, `complex` and `ligand`.


### `complex`

These contain files related to simulations of the ligand in its target protein
binding site.

#### `abfe`

Under `abfe` are the inputs topologies and structure files for
each of the protein-ligand complex parts of the absolute binding free energy
cycle. With `coul`, `restraint`, and `vdw` representing the charge addition,
orientational restraint removal, and Van der Waals coupling steps respectively.
For brevity, these are provided for a single replica (the starting positions
and orientational restraint definition is different between replicates).

**Note:** in the case of the `CyclophilinD` ligands, an additional directory
`abfe_2fs` is present which includes inputs using standard mass instead of
hydrogen mass repartitioning.

#### `amber` and `gromacs`

These directories include the starting conventional MD topologies and structure
files in both AMBER and GROMACS format respectively.

**Note:** in the case of ligands 8, 12, 16, and 17, an additional directory
named `gromacs-full` exists, which include the starting topologies and
structure files for the non N-termini truncated version of the PWWP1
construct. See Text S2 for more details.


### `<ligand>`

These contain files related to simulations of the ligand in solvent.

#### `<abfe>`

Under `abfe` are the input topologies and structure files for each of the
ligand decoupling from solvent parts of the absolute binding fee energy cycle.
With `coul` and `vdw` representing the charge annihilation and Van der Waals
decoupling steps repsectively. For all replica, the same starting positions and
topologies are used.

**Note:** in the case of the `CyclophilinD` ligands, an additional directory
`abfe_2fs` is present which includes inputs using standard mass instead of
hydrogen mass repartitioning.

#### `gromacs`

These directories include the starting conventional MD topologies and structure
files in GROMACS format.


## References

The ligands for each system were first described here:

PWWP1: https://doi.org/10.1038/s41589-019-0310-x
MCL-1: https://doi.org/10.1021/jm301448p
HSP90: https://doi.org/10.1021/jm100059d
Cyclophilin D: https://doi.org/10.1016/j.bmcl.2019.126717
