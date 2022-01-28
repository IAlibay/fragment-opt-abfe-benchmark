# Example Rocklin correction scripts

Included are example inputs to calculate an analytical net charge
correction using the method described by Rocklin et al. (10.1063/1.4826261)
as implemented in rocklinc (https://github.com/xiki-tempula/rocklinc).

The relevant scripts for the complex and ligand-in-solvent analytical corrections
are found under `complex` and `ligand` respectively, with example inputs from
the first replica of ligand-1 from the MCL-1 dataset.

Trajectories from the fully interacting non-restrained protein-ligand complex
and ligand-in-solvent ABFE windows were used. These trajectories were first
PBC fixed, centered and least-squares fit to the first frames' alpha carbon
to avoid out-of-box issues in the APBS calculations. The trajectories were
also subsampled, with the analytical correction being calculated over 11 frames
in each trajectory.

