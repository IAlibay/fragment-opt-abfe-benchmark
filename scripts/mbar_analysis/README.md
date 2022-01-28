# Scripts for MBAR analysis of free energies

Here are the two scripts used to calculate free energies from the `.xvg`
files generated through the ABFE simulations. These use the alchemlyb
and, by consequence, the pymbar libraries.

These scripts expect a specific file layout which is demonstrated in the
provided `xvg` dataset in the paper SI. With `complex-analysis.py` referring
to the complex decoupling xvg files separated into three steps
(coul, vdw and restraints), and `ligand-analysis.py` the ligand decoupling
from solvent xvgs separated into two (coul, and vdw). See the associated SI
datasets for more details (dois: 10.5281/zenodo.5904110,
10.5281/zenodo.5906019, 10.5281/zenodo.5906110, 10.5281/zenodo.5906262,
10.5281/zenodo.5906805).
