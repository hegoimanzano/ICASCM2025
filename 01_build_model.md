# Quickstart: Build a basic C–S–H model in 5 minutes

This section is intentionally minimal. Students will:
	1.	Download a ready-made code package.
	2.	Edit one file: input.py.
	3.	Run a single Python command.
	4.	See outputs (plots + structure files).
	5.	Visualize the structure in VESTA or OVITO.


## 1) Download the pyCSH code
- Download the zip from the course link I will provide in class (or clone the repo).
- Unzip and enter the folder (e.g. csh_basic/).

> Optional (recommended): create a python virtual environment. A Python environment is basically a self-contained workspace where you keep your Python interpreter plus the exact set of libraries you need for a project. Think of it as a sandbox: it isolates your project’s Python version and packages from everything else installed on your computer. You avoid breaking your system Python. Installing libraries globally (pip install … without an environment) can mess up system tools. When you’re done with a project, you can just delete the environment folder and it’s gone—no leftover libraries.

```
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt    # only if provided
```

## 2) Edit only input.py

Open **input.py** in your text editor. In windows the default is **Notepad**, and it is enough. But if you are going to work on simulations, we recommend something more sophisticated as **vim** or **visual studio**. You will only change a few parameters (I will dictate the exact options later). The file looks like:


## 3) Run

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

## 4) What the outputs are (and how to read them)

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


## 5) Visualize the model

VESTA (for CIF)
- Open VESTA → File → Open… → select csh_basic.cif.
- Properties → Data to verify the box; Properties → Atoms to color by element.
- Use Boundary settings to show periodic images if desired.

OVITO (for LAMMPS data or XYZ)
- Open OVITO → File → Load… → choose csh_basic.data (format: LAMMPS data) or csh_basic.xyz.
- In the Pipeline add modifiers if you want (e.g., Slice, Color coding, Coordination analysis).
- Use the Viewport to make quick screenshots for your report.


## 6) What students must hand in (suggested)
- A screenshot from VESTA (CIF) or OVITO (DATA/XYZ) showing the C–S–H or pore.
- The plots in plots/ with 2–3 lines interpreting each figure (what you observe and why it makes sense).
- The input.py used (so we can reproduce your settings).

## 7) Troubleshooting (two most common)
- “Module not found”: if the code needs a small library (e.g., numpy, matplotlib), install it:

```
python -m pip install numpy matplotlib
```

- VESTA cannot open XYZ: use csh_basic.cif in VESTA (preferred). OVITO can open both XYZ and LAMMPS data.


## 8) (Optional) Minimal automation for students

A tiny helper so they only type one command:

```
python3 -m venv .venv && source .venv/bin/activate && \
python -m pip install --upgrade pip && \
python -m pip install -r requirements.txt && \
python3 run.py
```

Notes for instructors (you)
- You will provide the zip/repo URL.
- You will provide the allowed/required keys inside input.py (we left placeholders).
- The code will always emit csh_basic.data, csh_basic.xyz, and csh_basic.cif plus the plots/ folder so VESTA/OVITO usage is frictionless.

If you want, I can generate a starter zip with run.py, a template input.py, and a minimal plots/ logic so you can share it right away; later you send me the exact list of commands/parameters and I’ll plug them into input.py’s validation.
