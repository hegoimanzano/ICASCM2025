# Welcome to the hands-on course ICASCM 2025

### Course Overview  

This course is designed as a hands-on tutorial that introduces the use of molecular dynamics simulations in the study of cementitious materials. It provides a practical first overview of how atomistic modeling can be applied to this field.  

As a case of study, we will focus on a paradigmatic examples that has been widely studied in the cement research community: **the calcuation of ion diffusivity in C-S-H gel nanopores** (see, for example, [Manzano *et al.*, 2009](your-reference-here)). We will: 

- Construct a realistic slit-pore C–S–H model saturated with water and sodium chloride (NaCl).
- Prepare a LAMMPS input file to run Molecular Dynamics simulations
- Analyse the results, and calculate
  - the diffusion constants of chloride, sodium, and water,  
  - the density profiles of the ions inside the pore.  

The aim is to illustrate two complementary approaches:  

1. **A simple tool-based route**, intended for beginners taking their first steps in molecular simulations.  
2. **A programing-based route**, which may initially seem more demanding, but quickly becomes straightforward once the basic steps are understood, and has the great advantage of enabling high levels of automation.  

---

### Software Requirements  

To follow the tutorial, participants will need to prepare a few tools in advance:  

- **Visualization programs**: We will use *Ovito*, *VESTA*, and *VMD*. These are free visualization tools, available for Windows, Linux, and macOS.  

- **Python execution environment**:  
  - On macOS and Linux, Python can be run natively or inside a virtual environment.  
  - On Windows, a separate installation is required. We recommend using *Visual Studio Code* (VS Code), a free editor by Microsoft that integrates smoothly with Python.  

- **Basic file and path handling**: A minimal understanding of how to navigate file paths and execute Python scripts will be necessary.  

> **Note**: No access to a supercomputer is required, since the tutorial is based on a **basic but representative example** designed to be executable on a personal computer.  





