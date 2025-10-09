# Build a basic C–S–H model with pyCSH

The first step for a high quality simulation of C-S-H (and any other material) is to build an atomic scale model as realistic as possible, this is, that comprises all the necessary features to represent the real conditions to reproduce the experimental physical properties. In our case, we will build a slit-pore C-S-H model" to study NaCl diffusion in C-S-H nanopores.

The general procedure for building a slit pore in a calcium–silicate–hydrate (C–S–H) model follows the same logic as in layered silicate clays.
- **Build the bulk structure**  A detailed description of the different model construction methods can be found in this [article](https://doi.org/10.1016/j.cemconres.2022.106784). Here we will use the [pyCSH code](https://doi.org/10.1016/j.cemconres.2024.107593), a Python code for the automated generation of realistic bulk calcium silicate hydrate (C-S-H) structures.
- **Introduce the pore** (slit geometry) Choose a crystallographic direction perpendicular to the layers of interest. Define a “gap” by translating one part of the structure away from the other, thereby creating an empty region. Adjust the simulation box dimensions accordingly to maintain periodic boundary conditions. The pore width can be tuned by setting the separation distance between the two C–S–H surfaces.
- **Saturate with water** Insert water molecules into the pore region using a packing algorithm (e.g., Packmol, mBuild, or custom scripts). Maintain realistic densities by filling until the desired target pore solution density is reached.
---
### Download the pyCSH code
- Download the zip file from the course link I will provide in class (or clone the repo).
- Unzip and enter the folder (e.g. csh_basic/).

> Optional (recommended): create a python virtual environment. A Python environment is basically a self-contained workspace where you keep your Python interpreter plus the exact set of libraries you need for a project. Think of it as a sandbox: it isolates your project’s Python version and packages from everything else installed on your computer. You avoid breaking your system Python. Installing libraries globally (pip install … without an environment) can mess up system tools. When you’re done with a project, you can just delete the environment folder and it’s gone—no leftover libraries.

```
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt    # only if provided
```
---
### Edit the input.py
Open **input.py** in your text editor. In windows the default is **Notepad**, int Mac **Textedit** and they are enough, but if you are going to work on simulations, we recommend something more sophisticated as **vim** or **visual studio**. You will only change a few parameters (I will dictate the exact options later). The file looks like:

---
### Run

In a terminal inside the folder:

```
python3 run.py
```

That’s it. The script will:
- Read input.py.
- Build a basic C–S–H model (or C–S–H slit-pore if selected).
- Save structure files and produce some plots.

You should see terminal messages ending with something like:

```
[OK] wrote: csh_basic.data
[OK] wrote: csh_basic.xyz
[OK] wrote: csh_basic.cif
[OK] plots saved in: plots/
```
---
### What the outputs are and how to read them

Structure files
- csh_basic.data — LAMMPS data file (topology + box).
- Used later if we run MD.
- OVITO can open LAMMPS data directly (File → Load… → choose LAMMPS data).
 - csh_basic.xyz — simple XYZ with all atoms.
- OVITO can open it directly.
- Good for quick previews.
- csh_basic.cif — CIF crystallographic file.
- VESTA: File → Open… → choose csh_basic.cif.
- Preferred for VESTA (periodic cell handled nicely).

Plots (inside plots/)
- density_profile_z.png — number-density profiles along the pore axis z (H_2O O, Na^+, Cl^-).
- rdf_example.png — example radial distribution function (pair(s) will be specified).
- composition_summary.png — basic composition/stoichiometry bars (if provided).
- (If a short MD is bundled) msd_water.png — MSD of water oxygens with a rough D estimate.

---
### Visualize the model

VESTA (for CIF)
- Open VESTA → File → Open… → select csh_basic.cif.
- Properties → Data to verify the box; Properties → Atoms to color by element.
- Use Boundary settings to show periodic images if desired.

OVITO (for LAMMPS data or XYZ)
- Open OVITO → File → Load… → choose csh_basic.data (format: LAMMPS data) or csh_basic.xyz.
- In the Pipeline add modifiers if you want (e.g., Slice, Color coding, Coordination analysis).
- Use the Viewport to make quick screenshots for your report.

---
## What students must hand in (suggested)
- A screenshot from VESTA (CIF) or OVITO (DATA/XYZ) showing the C–S–H or pore.
- The plots in plots/ with 2–3 lines interpreting each figure (what you observe and why it makes sense).
- The input.py used (so we can reproduce your settings).
