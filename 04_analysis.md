# Analysis (MSD & density)

We will analyze the performed MD simulation. The objective is to understand the diffusion and the equilibrium state of Cl ions in the C-S-H slit-(nano)pore. Furthermore, it is always desirable to check the basic thermodynamic properties and perform a visual inspection of the trajectory. There are unphysical behaviors that can be observed on one or another. For example, the silicate chains can break, forming an amorphous material that no longer represents C-S-H, and yet, the thermodynamic properties can still give reasonable energies, densities, etc. 

> ✏️ **Novice users** will have to follow the instructions to analyze the data. **First** you have to produce plots to justify if the simulation has converged or not. **Second** you will have to save an image with a simulation snapshot from OVITO. **Third** you will have to use TRAVIS to plot the MSD and report the obtained diffusion coefficient. **Finally** you will have to use TRAVIS to plot and save an image with the density profile.

> ✒️ **Advanced users** will have to do the same as novice users. In addition, you will have to plot the MSD and density profiles obtained directly from LAMMPS.

```{caution}
Thermodynamic properties (energy, enthalpy...), structural features (RDFs, density profiles...), dynamic properties (viscosity, diffusion coefficients...), and basically **any property** must not be computed unless the system is at equilibrium. The current example may not be converged due to time limitation of the course.
```

---
### Thermodynamic properties and trajectory

LAMMPS writes thermodynamic data (energy, pressure, density, etc.) into the `log.lammps` file (or into a user-defined text file if requested).  We can use this information to check whether the system has reached equilibrium. After the simulation, open the `log.lammps` and plot **energy vs. time**, **density vs. time**, etc. Stable values indicate equilibration, and the average will give you the observable value of the property. If energy or density continues to drift, the system is not equilibrated. To do these plots you can copy-paste in spreadsheet-based software (_Excel_, _LibreOffice_, _Kaleidagraph_,...) or do a bit of scripting in advanced tools (_MATLAB_, _Mathematica_, _R_,...). Again, we recommend Python-based plotting using a combination of tools like [Matplotlib](https://matplotlib.org) and [lammps-logfile](https://pypi.org/project/lammps-logfile/), but use your preferred tool.

If you decide to use Python, you can simply run:

```python
import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("path/to/logfile")

x = log.get("Time")
y = log.get("Temp")

plt.plot(x, y)
plt.show()
```

and you get a quick plot, highly customizable through the myriad of Matplotlib options. If you want all plots at once, you can use:

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
This is just a tutorial, you do not need to go further. For real work, invest time in your plots. Do not use the defaults, and do not copy other people's plot styles. Your plots are like the visual presentation of your work; think about how to make them both informative and readable.
```

---

### Visualizing the Trajectory

Numbers alone are not enough. Even if the energy appears stable, the system's structure might still become unphysical. For example, incorrect typing of the force field in the input file or a wrong assignment of the atoms might lead the system towards an unrealistic configuration, breaking the silicate chains and losing the layered structure, yet the thermodynamic properties may still appear to converge. Visualization allows us to **_see_** the atomic arrangement and detect problems and trends.

Open the trajectory with **OVITO**. Drag and drop your trajectory file, or load your file from the menu bar. Visualize your simulation, play with the available visualization options, export a snapshot of the trajectory, and check whether:

- The pore remains open.  
- Water molecules have not broken.  
- The silicate chains and the layer structure are maintained.

---

### Analysis with TRAVIS

[TRAVIS](https://www.travis-analyzer.de) (Trajectory Analyzer and Visualizer) is a free post-processing program for MD data. It can calculate the mean square displacement (MSD), density profiles, radial distribution functions, vibrational spectra, and many more. TRAVIS is a very powerful tool, but it does not have a very comprehensive documentation. For novice users, it is practical because it is **verbose**, i.e., it will ask you questions step-by-step to perform your analysis. 

Download the binaries from the TRAVIS website for your OS (no special dependencies are required), and place the executable in your working directory (the same directory as the LAMMPS trajectory). You can run TRAVIS by typing in your terminal:

```
travis -p traj.lammpstrj
```

This launches an interactive menu; answer the questions as they appear on-screen. Be patient and read carefully — **you cannot go back**, and making a mistake means starting again. There are several important things to consider:

- TRAVIS expects a specific LAMMPS trajectory format, e.g. `custom id element xu yu zu`. Ensure your dump uses these arguments, as we did in this tutorial, so you will not face any problem.
- Do not use advanced mode; use the **default** answers when possible, unless you understand exactly what you are doing (experience!). TRAVIS will handle it for you.
- TRAVIS performs molecular recognition to define the species in your system. Do not include Ca or Na in bond recognition, or TRAVIS will treat Ca-water and Na-water will as single molecules rather than separated species.

After the molecule recognition, TRAVIS will give you a list of the available properties to be computed. In this exercise we are interested in the mean square displacement / diffusion coefficients (`msd`) and the fixed-plane density profile (`dprof`). 

- **Mean Square Displacement**:
Type `msd` and follow the instructions on the screen. You need to set the time between trajectory frames. That is, your `timestep` * `dump` frequency. You can select several atoms/molecules as separated "observations". If you did everything correctly, TRAVIS generates several files: 
  - `msd_*.csv` where * is the name of your atom/molecule. These files can be plotted in spreadsheet-based software or do a bit of scripting in advanced tools like Python.
  - `travis.log` with all the information that you answered on the screen and the results of the analysis. In this file you can find the diffusion coefficient computed from the linear regression of the MSD. You can also perform the linear regression yourself from the `msd_*.csv` plot.

- **Density Profiles**:  
 Type `dprof` and follow the instructions on the screen. The default domain is slightly smaller than the simulation box. Adjust the minimum and maximum distances of the density profile to the **z** dimension. If you did everything correctly, TRAVIS generates several files:
  - `dprof_*.csv` where * is the name of your atom/molecule. These files can be plotted in spreadsheet-based software or do a bit of scripting in advanced tools like Python.
  - `dprof_*.agr` Same information but in a format ready to use in Grace (an obsolete software package).
  - `travis.log` with all the information provided on-screen and the results of the analysis.


```{Tip}
TRAVIS also generates an `input.txt` file that can be read when calling TRAVIS with `travis -p traj.lammpstrj -i input.txt`. This is useful for automation purposes, as it allows scripting.
```

---
### Analysis with Python (advanced)

Analyzing the MSD and density profiles from LAMMPS with Python should be easier than running TRAVIS, but you need sufficient expertise to understand your needs and prepare a LAMMPS input file capable of performing the analysis _on the fly_. If you did it correctly, you should have the data files with the mean square displacement and the density profiles. Open the files and plot them with Python. 

For comparison, perform the same analysis with TRAVIS and check whether both methods yield the same result. The results should be equivalent, with only minor differences arising from the smoothing algorithms used by TRAVIS. If you have time, explore other options available in TRAVIS, such as RDFs, autocorrelation functions (ACFs), etc. Some of these properties cannot be computed directly with LAMMPS and may be difficult to code. 

