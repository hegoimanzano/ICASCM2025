# Building the C-S-H model with PyCSH

In this step we construct a C-S-H model, carve a cylindrical pore, and fill it with water and NaCl.

## Python script

```{code-block} python
# code/build_model.py
import sys

try:
    import pycsh
except ImportError:
    sys.exit("PyCSH is not installed. Please install it or provide a mock interface.")

# --- Parameters (feel free to modify for exercises) ---
CA_SI = 1.7          # target Ca/Si ratio
DENSITY = 2.6        # g/cm^3 (effective)
BOX_SIZE_NM = (5, 5, 5)  # nm
PORE_RADIUS_NM = 1.0
N_WATER = 500
N_NA = 50
N_CL = 50

# --- Build C-S-H and pore ---
csh = pycsh.CSHModel(ca_si=CA_SI, density=DENSITY)
csh.build_box(box_size=BOX_SIZE_NM)          # box size in nm
csh.create_pore(radius=PORE_RADIUS_NM, axis='z')

# --- Hydrate and add ions ---
csh.add_water(n_molecules=N_WATER)
csh.add_ions({'Na+': N_NA, 'Cl-': N_CL})

# --- Export to LAMMPS data file ---
csh.write_lammps_data("csh_pore.data")
print("Wrote LAMMPS data to csh_pore.data")
```

## Exercises
- Double the pore radius and observe the initial density change.
- Increase NaCl concentration and discuss screening effects.
- Export multiple realizations (different random seeds) for statistics.
