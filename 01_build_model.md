# Building the C-S-H model with PyCSH

```{code-block} python
# (Pseudo-API example; adapt to your version)
# import pycsh
# csh = pycsh.CSHModel(ca_si=1.7, density=2.6)
# csh.build_box(box_size=(5,5,5))
# csh.create_pore(radius=1.0, axis='z')
# csh.add_water(n_molecules=500)
# csh.add_ions({'Na+':50, 'Cl-':50})
# csh.write_lammps_data("csh_pore.data")
```
