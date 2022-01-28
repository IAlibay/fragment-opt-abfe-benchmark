import MDAnalysis as mda
import sys

u = mda.Universe(sys.argv[1], sys.argv[2])

u.atoms.write('traj.ncdf', frames='all')
