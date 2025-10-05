# Writing the LAMMPS input

```{code-block} none
units           real
atom_style      full
boundary        p p p

read_data       csh_pore.data

pair_style      lj/cut/coul/long 10.0 10.0
kspace_style    pppm 1.0e-4

neighbor        2.0 bin
neigh_modify    delay 10 every 1

timestep        1.0
fix             nvt_all all nvt temp 300.0 300.0 100.0

thermo          1000
thermo_style    custom step temp pe ke etotal press density

dump            trj all custom 100 traj.lammpstrj id type q x y z
dump_modify     trj sort id

run             50000
```
