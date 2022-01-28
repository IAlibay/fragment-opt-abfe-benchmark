# Boresch-style orientational restraint scripts

Scripts to obtain a Boresch-style orientational restraint from a trajectory
using the MDRestraintsGenerator (https://github.com/IAlibay/MDRestraintsGenerator).

The `trjconv.sh` is intended to be run on the output of the `npt_prod1` step
outlined in `simulation_control_files/equilibration_mdps/npt_prod1` of this
repository. This generates a centered, PBC adjusted trajectory which can then
be parsed using `boresch.py` to obtain a GROMACS topology
[ intermolecular_interactions ] section for the Boresch-style orientational
restraint and a `.gro` file for the trajectory frame reflecting the position
taken by this restraint.
