# Welcome to the hands-on course ICASCM 2025

### Course Overview  

This course is designed as a hands-on tutorial that introduces the use of molecular dynamics simulations in the study of cementitious materials. It provides a practical first overview of how atomistic modeling can be applied to this field.  

As a case of study, we will focus on a paradigmatic examples that has been widely studied in the cement research community: **the calculation of ion diffusivity in C-S-H gel nanopores** (see [Duque-Redondo *et al.*, 2022](https://doi.org/10.1016/j.cemconres.2022.106784) for a review). We will: 

- Construct a realistic slit-pore C–S–H model saturated with water and sodium chloride (NaCl).
- Prepare a LAMMPS input file to run Molecular Dynamics simulations
- Analyse the results, and calculate
  - the diffusion constants of the ions inside the pore. 
  - the density profiles of the ions inside the pore.  

The aim is to illustrate two complementary approaches:  

1. **A simple tool-based route**, intended for novel users taking their first steps in molecular simulations.  
2. **A programing-based route** for more experienced users, illustrating how to automatize the simulations and analyses, which may initially seem more demanding, but quickly becomes straightforward once the basic steps are understood.  

Each section contains a very detailed explanation of what to do, together with the instructions of the corresponding exercise, and the estimated time to complete it. In case that you do not complete the exercise, you will have the solution in the course folder to be able to continue with the class.

---

### Software Requirements  

To follow the tutorial, participants will need to prepare a few tools in advance:  

- **Visualization programs**: We will use *Ovito* or *VESTA*, and *VMD*. These are free visualization tools, available for Windows, Linux, and macOS.
  - OVITO is excellent for analyzing atomistic trajectories and creating high-quality animations, focused on material science.
  - VESTA is widely used for crystallographic structures and static visualizations.
  - VMD is designed for trajectory analysis of biomolecules, but we will use it for bond recognition. 

- **Python execution environment**: We will write and execute small Python scripts to postprocess simulation data. A minimal understanding of how to navigate file paths and execute Python scripts will be necessary.
  - On macOS and Linux, Python is usually pre-installed. You can run scripts directly from the terminal, or create a virtual environment with 
  - On Windows, Python is not installed by default. We recommend downloading it from python.org or installing through the Microsoft Store. For editing and running scripts, Visual Studio Code (VS Code) is highly recommended. It is a free code editor by Microsoft, integrates seamlessly with Python, and supports virtual environments as well.

- **Model set up**: VMD, pyCSH, packmol (advaced) 

- **Simulation code** We will use [LAMMPS](https://docs.lammps.org) (Large-scale Atomic/Molecular Massively Parallel Simulator). LAMMPS is a open source classical molecular dynamics simulation code focusing on materials modeling, originally developed at Sandia National Laboratories. Usually LAMMPS will be installed and runed on HPC, but here we will use [Atomify](https://andeplane.github.io/atomify/), a lightweight graphical front-end for LAMMPS. Atomify allows you to build, run, and visualize molecular dynamics simulations in real time through an interactive interface. 

- **Postprocessing and Analysis**: Postprocessing will be done with python and [TRAVIS](travis-analyzer.de) (Trajectory Analyzer and Visualizer). TRAVIS is a free program that can process MD trajectories to compute properties such as Mean Square Displacement (MSD) and diffusion coefficients, Density and radial distribution profiles, Vibrational spectra, velocity autocorrelation functions, and more. TRAVIS is available for Windows, Linux, and macOS.

```{note}
No access to a supercomputer is required, since the tutorial is based on a **basic but representative example** designed to be executable on a personal computer.  
```
