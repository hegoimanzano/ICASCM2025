# Writing the LAMMPS input

Minimal input to equilibrate the hydrated C-S-H + NaCl system. Adapt force field to your PyCSH export.

## Template

```{code-block} none
# code/lammps_input.in
units           real
atom_style      full
boundary        p p p

read_data       csh_pore.data

# --- Pair interactions (placeholder) ---
# Replace with the correct style/coeffs consistent with the data file exported by PyCSH
pair_style      lj/cut/coul/long 10.0 10.0
kspace_style    pppm 1.0e-4

# Example (must be replaced by real parameters):
# pair_coeff    * * 0.0 3.0
# bond_style    harmonic
# angle_style   harmonic
# dihedral_style none
# improper_style none

neighbor        2.0 bin
neigh_modify    delay 10 every 1

# Groups (adapt selections to your topology if needed)
group           solvent type 1 2 3  # placeholder
group           solid subtract all solvent

# Thermostat (equilibration)
timestep        1.0   # fs if 'real' units
fix             nvt_all all nvt temp 300.0 300.0 100.0

thermo          1000
thermo_style    custom step temp pe ke etotal press density

# Output
dump            trj all custom 100 traj.lammpstrj id type q x y z
dump_modify     trj sort id

# Short run for testing
run             50000

unfix           nvt_all

# Optional: production run, change ensemble if desired
# fix          npt_all all npt temp 300 300 100 iso 1.0 1.0 1000
# run          200000
```

## Exercises
- Switch to **NPT** once the system is equilibrated to relax volume.
- Increase the cutoff and discuss Ewald/PPPM accuracy vs. cost.
- Enable SHAKE/RATTLE if water is constrained.
