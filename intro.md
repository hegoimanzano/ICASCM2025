# Welcome to the hands-on course ICASCM 2025

### Course Overview  

This course is designed as a hands-on tutorial that introduces the use of molecular dynamics simulations in the study of cementitious materials. It provides a practical first overview of how atomistic modeling can be applied to this field.  

As a case of study, we will focus on a paradigmatic examples that has been widely studied in the cement research community: **the calculation of ion diffusivity in C-S-H gel nanopores** (see [Duque-Redondo *et al.*, 2022](https://doi.org/10.1016/j.cemconres.2022.106784) for a review). We will: 

- Construct a realistic slit-pore C–S–H model saturated with water and NaCl
- Prepare a LAMMPS input file to run Molecular Dynamics simulations
- Analyse the results, and calculate
  - the diffusion constants of the ions inside the pore. 
  - the density profiles of the ions inside the pore.  

The aim is to illustrate two complementary approaches:  

1. **A simple tool-based route**, intended for novel users taking their first steps in molecular simulations.  
2. **A programing-based route** for more experienced users, illustrating how to automatize the simulations and analyses. It may initially seem more demanding, but quickly becomes straightforward and will increase your productivity.  

Each section contains a very detailed explanation of what to do, together with the instructions of the corresponding exercise, and the _estimated time_ to complete it. In case that you do not complete the exercise, you will have the solution in the course folder to be able to continue with the class.

---

### Software Requirements  

To follow the tutorial, participants will need to prepare a **few tools in advance**:  

- **Visualization programs**: We will use *Ovito* or *VESTA*. These are free visualization tools, available for Windows, Linux, and macOS.
  - [OVITO](https://www.ovito.org) is excellent for analyzing atomistic trajectories and creating high-quality animations, focused on material science.
  - [VESTA](https://jp-minerals.org/vesta/en/) is widely used for crystallographic structures and static visualizations.

- **Python execution environment**: We will use pyCSH and small Python scripts to postprocess simulation data. A minimal understanding of how to navigate file paths and execute Python scripts will be necessary. For editing and running scripts, we like Visual Studio Code ([VS Code](https://code.visualstudio.com)) but you can run it from your terminal or any other choice. 

- **Model set up**: We will use several codes to set up our model and simulation. VMD, pyCSH, packmol (advaced)
  - pyCSH is a code to automatically create hundres of unique and realistic C-S-H models 
  - [VMD](https://www.ks.uiuc.edu/Research/vmd/) is a visualuzation and analysis code designed for biomolecules, but we will use it here for topology recognition.
  - [Packmol](https://m3g.github.io/packmol/) is a code to efficiently pack molecules in multiple shapes

- **Simulation code** We will use [LAMMPS](https://docs.lammps.org) (Large-scale Atomic/Molecular Massively Parallel Simulator). LAMMPS is a open source classical molecular dynamics simulation code focusing on materials modeling, originally developed at Sandia National Laboratories. Usually LAMMPS will be installed and runed on HPC, but here we will use [Atomify](https://andeplane.github.io/atomify/), a lightweight graphical front-end for LAMMPS. Atomify allows you to build, run, and visualize molecular dynamics simulations in real time through an interactive interface.

```{note}
No access to a supercomputer is required, since the tutorial is based on a **basic but representative example** designed to be executable on a personal computer.  
```

- **Postprocessing and Analysis**: Postprocessing will be done with python and [TRAVIS](travis-analyzer.de) (Trajectory Analyzer and Visualizer). TRAVIS is a free program that can process MD trajectories to compute properties such as Mean Square Displacement (MSD) and diffusion coefficients, Density and radial distribution profiles, Vibrational spectra, velocity autocorrelation functions, and more. TRAVIS is available for Windows, Linux, and macOS.


```{tip}
There are many more [codes and tools](https://www.lammps.org/prepost.html#lunar) that can be helpful to perform MD simulations. We always strongly advocated the use of open-source and freely available software, as it ensures transparency, reproducibility, and accessibility for the entire scientific community
```
