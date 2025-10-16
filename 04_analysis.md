# Analysis (MSD & density)

We will analyse the performed MD simulation. The objective is to understand the diffusion and the equilibrium state of Cl ions in the C-S-H slit-(nano)pore. Furthermore, it is always desiderable to check the basic thermodynamics properties and do a visual inspection of the trayectory. There are unphysical behaviours that can be observed on one or another. For example, the silicate chains can break, forming an amorphous material that does not represent C-S-H anymore, and yet, the thermodynamic properties can give reasonable energies, densities, etc. 

> ✏️ **Novel users** will have to follow the instructions to analyse the data. **First** you have to produce plots to justify if the simulation has converged or not. **Second** you will have to save an image with a simulation snapshot from VMD or OVITO. **Third** you will have to use TRAVIS to plot the MSD and report the obtained diffusion coefficient. **Finally** you will have to use TRAVIS to plot and save an image with the density profile.

> ✒️ **Advanced users** will have to do the same as novel users. In adittion, you will have to plot the MSD and density profile obtained directly from LAMMPS.


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

### Visualizing the Trajectory

Numbers alone are not enough. Even if energy looks stable, the system structure might become unphysical. For example, uncorrect typing of the force field in the input file or a wrong asigment of the atoms might lead the system towards a unrealistic structure, breaking the silicate chains and losing the layered structure. But eventually the thermodynamic properties may converge. Visualization allows us to *see* the atomic arrangement and detect problems and trends.

Open the trajectory with one of the following tools:
- **OVITO** → for dynamic inspection, slicing, and analysis.  
- **VMD** → for detailed visualization of molecular motion.  

Check whether:
- The pore remains open.  
- Water molecules remain liquid and did not break.  
- The silicate chains and the layer structure are mantained

---

### Analysis with TRAVIS

[TRAVIS](https://www.travis-analyzer.de) (Trajectory Analyzer and Visualizer) is a free postprocessing program for MD data. It can calculate Mean Square Displacement (MSD), density profiles, radial distribution functions, vibrational spectra, and many more. TRAVIS is a very powerful tool, but it does not have a very comprehesive documentation. For novel users it is very practical because it is **verbose**, i.e. it will ask you questions step by step to perform your analysis. 

Download binaries from the TRAVIS website for your OS (no special dependencies are required), and place the executable in your working directory (same directory where the LAMMPS trajectory is). You can run TRAVIS by typing in you terminal:

```
travis -p lammps.trj
```

This launches an interactive menu, and now you need to answer the questions as they appear on screen. Be patient and read carefully, you cannot go back and making a mistake implies starting again. There are several important things to consider

- **Mean Square Displacement**:  
  Select atom types (e.g., Na⁺, Cl⁻, H₂O oxygen). TRAVIS will compute MSD(t) and diffusion coefficients.  

- **Density Profiles**:  
  Define the axis (typically z for slit pores). TRAVIS will output the density distribution of ions/water across the pore.  

Results can be exported as text files or ready-to-plot graphics.

---
### Analysis with python (advanced)


