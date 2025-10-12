# Analysis (MSD & density)

We will analyse the performed MD simulation. The objective is to understand the diffusion and the equilibrium state of Cl ions in the C-S-H slit-(nano)pore.

---
### Thermodynamic properties and trayectory

It is always desiderable to check the basic thermodynamics properties and do a visual inspection of the trayectory. There are unphysical behaviours that can be observed on one or another. For example, the silicate chains can break, forming an amorphous material that does not represent C-S-H anymore, and yet, the thermodynamic properties can ARROJAR reasonable energies, densities, etc. 

Perfect — here’s a **ready-to-use Markdown page** with the three analysis steps, written cleanly for JupyterBook. You can paste it directly into your `docs/` folder as e.g. `03_analysis.md` and include it in your `_toc.yml`.  

---

```markdown
# Data Analysis of Molecular Dynamics Simulations

In this section, we will analyze the data produced by our LAMMPS simulations.  
The analysis will follow three main steps:  

1. **Thermodynamic output**  
2. **Trajectory visualization**  
3. **Postprocessing with TRAVIS**

---

## 1. Thermodynamic Output from LAMMPS

LAMMPS writes thermodynamic data (energy, pressure, density, etc.) into the log file (`log.lammps`) or a user-defined file.  
We can use this information to check whether the system has reached equilibrium.

```lammps
thermo_style custom step temp density etotal press
thermo 1000
```

After the simulation:

- Open the `log.lammps` file or redirect the thermo data to a file (e.g., `thermo_output.dat`).  
- Plot **energy vs. time** or **density vs. time**. Stable values indicate equilibration.  

Example Python script to plot the total energy:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("thermo_output.dat", delim_whitespace=True)
plt.plot(df["Step"], df["Etot"])
plt.xlabel("Timestep")
plt.ylabel("Total Energy (eV)")
plt.title("Energy vs Time")
plt.show()
```

**Why this matters:** Thermodynamic stability is our first check of equilibration. If energy or density continues to drift, the system is not equilibrated.

---

## 2. Visualizing the Trajectory

Numbers alone are not enough. Even if energy looks stable, the system structure might become unphysical.  
Visualization allows us to *see* the atomic arrangement.

```lammps
dump traj all custom 1000 traj.lammpstrj id type x y z
```

This creates a trajectory file every 1000 steps.

Open the trajectory with one of the following tools:
- **OVITO** → for dynamic inspection, slicing, and analysis.  
- **VMD** → for detailed visualization of molecular motion.  
- **VESTA** → for static structural inspection.

Check whether:
- The pore remains open.  
- Water molecules remain liquid.  
- The ions distribute realistically.  

**Why this matters:** A force field may produce stable energy but an unphysical structure. Visualization helps detect such problems.

---

## 3. Advanced Analysis with TRAVIS

[TRAVIS](https://www.travis-analyzer.de) (Trajectory Analyzer and Visualizer) is a free postprocessing program for MD data.  
It can calculate Mean Square Displacement (MSD), density profiles, radial distribution functions, vibrational spectra, and more.

### Installation
- Download binaries from the TRAVIS website for **Linux, Windows, or macOS**.  
- No special dependencies are required.  
- Place the executable in your working directory or add it to your PATH.

### Preparing the trajectory
Export your trajectory in XYZ format from LAMMPS:

```lammps
dump travis all xyz 1000 traj.xyz
```

### Running TRAVIS
```bash
travis traj.xyz
```

This launches an interactive menu. Choose the desired analysis:

- **Mean Square Displacement**:  
  Select atom types (e.g., Na⁺, Cl⁻, H₂O oxygen). TRAVIS will compute MSD(t) and diffusion coefficients.  

- **Density Profiles**:  
  Define the axis (typically z for slit pores). TRAVIS will output the density distribution of ions/water across the pore.  

Results can be exported as text files or ready-to-plot graphics.

**Why this matters:** TRAVIS provides a robust, automated way to compute structural and dynamical observables, complementing what LAMMPS can calculate on-the-fly.

---

## Summary

- **Thermo output**: first check of system equilibration.  
- **Visualization**: essential to detect structural artifacts.  
- **TRAVIS analysis**: advanced postprocessing (MSD, density profiles, RDFs, spectra).  

Together, these steps ensure that your simulation data is both physically meaningful and ready for scientific interpretation.
```

---

Would you like me to also prepare **example plots** (e.g. sample MSD, density profile) with fake/simple data, so your students see what to expect before they run their own?