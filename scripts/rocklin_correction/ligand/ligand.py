import numpy as np
import rocklinc
import MDAnalysis as mda
import MDAnalysis.transformations as trans

u = mda.Universe('prod.tpr', 'frames.xtc')
pqr = mda.Universe('prod.pqr')
u.add_TopologyAttr('radii')
u.atoms.radii = pqr.atoms.radii

lig_netq = np.round(u.select_atoms('resname LIG').charges.sum())
protein_netq = 0
temp = 298.15
lig_selection = "resname LIG"
charges = u.atoms.charges
apbs_exe = '/home/bioc1523/software/apbs-3.0/APBS-3.0.0.Linux/bin/apbs'

results = []

for i, ts in enumerate(u.trajectory):
    correction = rocklinc.RocklinCorrection(u.dimensions[:3], lig_netq, protein_netq, temp)
    correction.make_APBS_input(universe=u.select_atoms('not resname NA CL'),
                               ligand_selection=lig_selection,
                               solvent_selection="resname SOL",
                               in_prot_only=f"prot_only_step{i}.pqr",
                               in_lig_in_prot=f"lig_in_prod_step{i}.pqr",
                               in_lig_only=f"lig_only_step{i}.pqr",
                               apbs_in=f"apbs_step{i}.in")
    u.atoms.charges = charges
    correction.run_APBS(apbs_exe=apbs_exe, apbs_in=f"apbs_step{i}.in")
    correction.read_APBS()
    results.append(correction.compute())
    correction.write(f"correction_step{i}.txt")

data = np.zeros(len(results))

for i, res in enumerate(results):
    data[i] = res / 1000

with open('results.txt', 'w') as filed:
    filed.write(f"{data.mean()} {data.std()}")
