# Analysis (MSD & density)

We will analyse the performed MD simulation. The objective is to understand the diffusion and the equilibrium state of Cl ions in the C-S-H slit-(nano)pore. Furthermore, it is always desiderable to check the basic thermodynamics properties and do a visual inspection of the trayectory. There are unphysical behaviours that can be observed on one or another. For example, the silicate chains can break, forming an amorphous material that does not represent C-S-H anymore, and yet, the thermodynamic properties can give reasonable energies, densities, etc. 

> ✏️ **Novel users** will have to follow the instructions to analyse the data. **First** you have to produce plots to justify if the simulation has converged or not. **Second** you will have to save an image with a simulation snapshot from OVITO. **Third** you will have to use TRAVIS to plot the MSD and report the obtained diffusion coefficient. **Finally** you will have to use TRAVIS to plot and save an image with the density profile.

> ✒️ **Advanced users** will have to do the same as novel users. In adittion, you will have to plot the MSD and density profile obtained directly from LAMMPS.

```{caution}
Thermodynamic properties (energy, enthalpy...), structure (RDFs, Density profiles...), dynamic properties (viscosity, diffusion coefficients), and basically **any property** must not be computed unless the system is at equilibrium. The current example may no be converged due to time limitation of the course.
```

---
### Thermodynamic properties and trayectory

LAMMPS writes thermodynamic data (energy, pressure, density, etc.) into the `log.lammps` file (or into a user-defined text file if requested).  We can use this information to check whether the system has reached equilibrium. After the simulation, open the `log.lammps`, and plot **energy vs. time**, **density vs. time**, etc. Stable values indicate equilibration, and the average will give you the observable value of the property. If energy or density continues to drift, the system is not equilibrated. To do these plots you can copy-paste in spreeadsheet based software (_excel_, -libreoffice_, _kaleidagraph_,...) or do a bit of scripting in advanced tools (_matlab_, _mathematica_, _R_,...). Again, we recommend python-based plotting using a combination of tools like [matplotlib](https://matplotlib.org) and [lammps-logfile](https://pypi.org/project/lammps-logfile/), but use your preferred tool.

If you decided to use python, you can simply run:

```python
import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("path/to/logfile")

x = log.get("Time")
y = log.get("Temp")

plt.plot(x, y)
plt.show()
```

and you have a fast plot, higly cusomizable by the miriad of matplotlib options. If you want all the plots at once, you can use:

```python
import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("path/to/logfile")
step = log.get("Step")

for keyword in log.keywords:
    plt.figure()
    plt.plot(step, log.get(keyword), label=keyword)
    plt.xlabel('Timestep')
    plt.title(keyword)
    plt.show()
```

```{Tip}
This is just a tutorial, you don't need to go further. For real work, invest time in your plots. Do not use the defaults, do not copy others plot style. Your plots are like a presentation letter of the work, think about how to get the most information from them and how to make them readable. 
```

---

### Visualizing the Trajectory

Numbers alone are not enough. Even if energy looks stable, the system structure might become unphysical. For example, uncorrect typing of the force field in the input file or a wrong asigment of the atoms might lead the system towards a unrealistic structure, breaking the silicate chains and losing the layered structure. But eventually the thermodynamic properties may converge. Visualization allows us to **_see_** the atomic arrangement and detect problems and trends.

Open the trajectory with **OVITO**. Drag and drop your trayectory file, or load your file from the menu bar. Visualise your simulation, play with the available visualization options, export a snaphsot of the trayectory, and check whether:

- The pore remains open.  
- Water molecules did not break.  
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

Actually, the analysis with python is easier than running TRAVIS, but you need the right expertise to understand what you need and prepare a LAMMPS input file to perform the analysis _on the fly_. If you did it correctly, you should have an MSD.txt and DP.txt datafiles with the mean square displacement and the density profile. Opend the files and make a plot with python. 

For comparison, do the same analysis with TRAVIS and check if both methods are giving you the same answer. The results should be equal, with minor differences due to the TRAVIS algorithms used to smooth data. Explore if you have time other options that TRAVIS gives you, like RDFs, autocorrelation plots, etc. Some of the properties cannot be computed with LAMMPS, and can be difficult to code. 

