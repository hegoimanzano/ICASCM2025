# Analysis (MSD & density)

We will analyse the performed MD simulation. The objective is to understand the diffusion and the equilibrium state of Cl ions in the C-S-H slit-(nano)pore. Furthermore, it is always desiderable to check the basic thermodynamics properties and do a visual inspection of the trayectory. There are unphysical behaviours that can be observed on one or another. For example, the silicate chains can break, forming an amorphous material that does not represent C-S-H anymore, and yet, the thermodynamic properties can give reasonable energies, densities, etc. 

> ✏️ **Novel users** will have to follow the instructions to plot . The simulation must equilibrate the system for 0.5 ps in NPT and perform a production run in NVT for 1 ps, with clayFF force field, dumping the trayectory every 200 steps and printing the properties every 100 steps.

> ✒️ **Advanced users** will have to follow the [Basic LAMMPS input file for C-S-H simulations](#basic-lammps-input-file-for-c-s-h-simulations) section, and add the information on the [Advanced LAMMPS input file for C-S-H simulations](#advanced-lammps-input-file-for-c-s-h-simulations) section to improve the LAMMPS input file. The simulation must equilibrate the system for 0.5 ps in NPT and perform a production run in NVT for 1 ps, with clayFF force field, dumping the trayectory every 200 steps and printing the properties every 100 steps. The simulation must print the MSD and the density profiles of Cl, Na and water in 2 files called MSD.txt and DP.txt.


---
### Thermodynamic properties and trayectory

LAMMPS writes thermodynamic data (energy, pressure, density, etc.) into the `log.lammps` file (or into a user-defined text file if requested).  We can use this information to check whether the system has reached equilibrium. After the simulation, open the `log.lammps`, and plot **energy vs. time**, **density vs. time**, etc. Stable values indicate equilibration, and the average will give you the value of the property. If energy or density continues to drift, the system is not equilibrated. To do these plots you can use your preferred software (_excel_, _gnuplot_, _mathematica_, _kaleidagraph_,...). We recommend **_Matplotlib_**, the python plotting package. An example Python script to plot the total energy:

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

```{caution}
Thermodynamic properties (energy, enthalpy...), structure (RDFs, Density profiles...) and dynamic properties (viscosity, diffusion coefficients) must not be computed unless the system is at equilibrium.
```

---

## 2. Visualizing the Trajectory

Numbers alone are not enough. Even if energy looks stable, the system structure might become unphysical. For example, uncorrect typing of the force field in the input file or a wrong asigment of the atoms might lead the system towards a unrealistic structure, breaking the silicate chains and losing the layered structure. But eventually the thermodynamic properties may converge. Visualization allows us to *see* the atomic arrangement and detect problems and trends.

Open the trajectory with one of the following tools:
- **OVITO** → for dynamic inspection, slicing, and analysis.  
- **VMD** → for detailed visualization of molecular motion.  

Check whether:
- The pore remains open.  
- Water molecules remain liquid and did not break.  
- The silicate chains and the layer structure are mantained

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
