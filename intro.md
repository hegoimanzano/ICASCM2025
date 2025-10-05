# Introduction

This one-day course covers **atomistic simulation applied to cementitious materials**. We will:  
1) Build a **C-S-H** model with a cylindrical pore using **PyCSH**.  
2) Hydrate the pore and add **NaCl**.  
3) Run **LAMMPS**.  
4) Analyze energies, **MSD**, radial distribution functions (RDF), and density profiles.

> Requirements (suggested conda env): `python>=3.10`, `jupyter-book`, `mdanalysis`, `matplotlib`, `numpy`, `scipy`, `nglview` (optional).

## Learning outcomes
By the end, students will be able to construct, simulate, and analyze C-S-H models with saline solutions.

## How to build the book
```bash
pip install -r requirements.txt
jupyter-book build .
# The HTML will be under _build/html/index.html
```
