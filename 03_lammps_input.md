# Writing the LAMMPS input

The LAMMPS **input file**, together with **the data** file you already built, contains the information needed to run (and analyze) your molecular dynamics simulation. Here we propose two different exercises depending on your experience.

> ✏️ **Novice users** will have to follow the [Basic LAMMPS input file for C-S-H simulations](#basic-lammps-input-file-for-c-s-h-simulations) section to understand and create in a text file the LAMMPS input file. The simulation must equilibrate the system for 0.2 ns in NPT and perform a production run in NVT for 0.1 ns, with ClayFF force field, dumping the trajectory every 1000 steps and printing the properties every 1000 steps.

> ✒️ **Advanced users** will have to follow the [Basic LAMMPS input file for C-S-H simulations](#basic-lammps-input-file-for-c-s-h-simulations) section, and add the information on the [Advanced LAMMPS input file for C-S-H simulations](#advanced-lammps-input-file-for-c-s-h-simulations) section to improve the LAMMPS input file. The simulation must equilibrate the system for 0.2 ns in NPT and perform a production run in NVT for 0.1 ns, with ClayFF force field, dumping the trajectory every 1000 steps and printing the properties every 1000 steps. The simulation must print the MSD and the density profiles of Cl and water.

---
### The structure of a LAMMPS input file
```{note}
This is a basic explanation of LAMMPS input file structure. If you are an experienced user, you can skip this section.
```

LAMMPS offers a vast set of options. The [LAMMPS Manual](https://docs.lammps.org/) can be overwhelming for beginners, but it contains all the information needed to build an **input file**. A LAMMPS input file is basically a script that tells the MD engine exactly how to build, run, and analyze a molecular simulation. It is written in a line-by-line command language with its own syntax (not Python or C++). You can think of it as having four layers:

**1. Header / Global Settings.** These commands define the units, atom style, boundary conditions, and load your starting structure.

**2. Force Field Definition.** Here you specify interatomic potentials and their parameters.
- `pair_style` + `pair_coeff` = how nonbonded atoms interact. 
- `bond_style`, `angle_style` = for bonded terms.
- `kspace_style` = long-range electrostatics.
- special FF like COMB, ReaxFF, or machine learning potentials (MLPs) have their own syntax.

**3. Simulation Control and Execution.** This is the heart of the input. It defines time integration, thermostats/barostats, neighbor lists, and trajectory dumps. There are different commands grouped in large families:
- `fix` = continuous operations applied every step of the simulation (e.g., integrators like `fix nvt`, thermostats, `fix shake` constraints, MSD calculators, walls, restraints).
- `dump` = how to write trajectory snapshots and how often.
- `thermo` and `thermo_style` = control which thermodynamic quantities and other parameters appear in the log output and how often.

**4. Analysis.** 
LAMMPS provides `compute` and `variable` as analysis tools, and `fix ave/time` to average over time. Analysis commands are interleaved with layer 3, and they are not strictly necessary, since analysis can be done in post-processing stage.
- `compute` = generates per-atom or global quantities (MSD, stress, RDF, density profiles).
- `variable` = algebra with computed quantities.
- `fix ave/time` / `fix ave/chunk` = averages, profiles, histograms.

Finally, you tell LAMMPS to `run`, specifying the length of the simulation (number of timesteps).

```{Caution}
Note that LAMMPS interprets commands strictly **in the order** they appear in the input file. This means that the simulation environment is built step by step, and a command cannot use information that has not yet been defined. You must be carefull with the order of commands.
```

---

### Basic LAMMPS input file for C-S-H simulations

Open a text file and build your input following the next steps. You can save it with any extension (`.inp`, `.input`, `.in`, `.txt`...).

**1. Header / Global Settings.** We are going to simulate a C-S-H box with periodic boundary conditions in x y z. There are different unit systems that must be consistent with your force field and all the input parameters. Note that all results will also be printed in these units. The `atom_style` defines what information is stored for each atom. The choice depends on the physics of your system and the force field you plan to use. In our case, ClayFF requires `full` atom style, which includes information about atom_id, atom_type, coordinates, charge, molecule-ID, bonds, angles, etc. 
The `neighbor`-related options refer to how LAMMPS builds the pairwise neighbor lists to compute forces between atoms. They affect the efficiency and sometimes may induce errors, but it is safe to use the standard values. For more information, see [neighbor lists](https://docs.lammps.org/Developer_par_neigh.html).

```
# ---------- SETTINGS / SYSTEM ----------
units           real
atom_style      full
boundary        p p p

read_data       CSHmodel_final.data     # write the name of your data file

neighbor        2.0 bin
neigh_modify    delay 10 every 1
```

**2. Force Field Definition.** Here you specify interatomic potentials and their parameters.
- `pair_style` + `pair_coeff` = how nonbonded atoms interact. You have to input the parameters are given in the **Topology** section (Table 1) in the correct order.
- `bond_style`, `angle_style` = for bonded terms. You have to input the parameters are given in the **Topology** section (Table 1) in the correct order.
- `kspace_style` = how long-range electrostatics are computed. Long range interactions are difficult to compute because they decay slowly with distance. Thus, special algorithms such as Ewald summation or `pppm`(particle-particle particle-mesh) are required.

```
# ---- Non bonded interactions  ----
pair_style      lj/cut/coul/long 10.0 10.0     # lennard-jones and coulomb cut offs
kspace_style    pppm 1.0e-4                    # coulomb long range solver and accuracy
pair_coeff    1 1 0.1554164124 3.1655200879    # atom1 + the ClayFF parametes of the atoms ($\epsilon$ and $\sigma$ in table S1). Check which is your atom 1 in the data file!
pair_coeff    2 2 0.0000000000 0.0000000000    # atom2 + the ClayFF parametes of the atoms ($\epsilon$ and $\sigma$ in table S1).  Check which is your atom 2 in the data file!
...
...

# ------ Bonded interactions  -------
bond_style      harmonic
angle_style     harmonic

bond_coeff      1  450.0  1.0        # SPC model: Hw–Ow bond 
angle_coeff     1  55.0  109.47      # SPC model: Hw–Ow–Hw angle

```

Note that we define only the interactions between equal atoms (Ow-Ow, Hw-Hw). The cross terms (Ow-Hw) are computed automatically from arithmetic [mixing rules](https://en.wikipedia.org/wiki/Combining_rules)


**3. Simulation Control and Execution.** Now we start the simulation. In any MD simulation there are at least two stpes. First, an **equilibration period**, in which our system adapts to the desired thermodynamic conditions. First, we do an energy minimization (`minimize`) to relax the atomic positions. Second, we assign random `velocity` to the particles according to a Boltzmann distribution at 300 K. Then, we perform a MD equilibration in the canonical ensemble `fix nvt`, at an initial and final temperature of 300 K, applying a thermostat every 100 steps to maintain the target temperature. We record selected `thermo` properties in the output every 1000 steps. Finally, we need to `unfix` the fix that was defined for this phase to prepare the system for the next stage.

```
# ---------- FAST EQUILIBRATION ----------
min_style       cg
minimize        1.0e-3 1.0e-4 500 1000

velocity        all create 298.0 4928459 rot yes mom yes
fix             npt all npt temp 298.0 298.0 100.0 aniso 1 1 1000
thermo          1000
thermo_style    custom step time temp pe ke etotal press density lx ly lz vol

timestep        1
run             100000
unfix           npt
```

**How long should an equilibration phase last?** The simple answer is that it should last as long as necessary; the exact duration is system-specific and depends on your initial simulation protocol, how you build your simulation box, the force field, the final thermodynamic conditions, etc. It is essential to confirm that equilibrium has truly been reached by monitoring the energy, system density, atomic mobility, and structural properties. 

```{caution}
The energy can be misleading: if the initial configuration is very far from equeilibrium, the first energy values will often be very high, and the subsequent rapid decrease may create the false impression of convergence.
```

Second, we enter the **production phase**. In this stage, thermodynamic quantities are collected, and snapshots of the trajectory are stored to compute the properties of interest. The production run must be sufficiently long to ensure that the observables under study have converged. The required length strongly depends on the property we wish to calculate. For instance, if the goal is to obtain an infrared spectrum, relatively short trajectories are sufficient, since molecular vibrations take place on the timescale of a few picoseconds. If instead we are interested in diffusivity, the simulation must extend to the hundreds of nanoseconds, because that is the timescale for water molecules to diffuse ($D_{\text{H₂O}} = 2.3 \text{nm}^2/\text{ns}$). In this course, due to time limitations, we will restrict ourselves to production runs of about 10 picoseconds, which is sufficient for demonstration purposes. Keep in mind, however, that **reliable mean square displacement calculations, typically require simulations extending 100 ns or more**. Here we also add a `dump` to save the trajectory in a file called `traj.lammpstrj`.

```
# ---------- PRODUCTION ----------
fix             nvt all nvt temp 298.0 298.0 100.0
dump            trj all custom 1000 traj.lammpstrj id element xu yu zu 
dump_modify     trj element Ca Ca Cl H H Na O O O O O Si Si
thermo_style    custom step time temp etotal 
thermo          1000
run             100000
```

With this basic input file + the data file, you can perform your MD simulation (next page!).

---

### Advanced LAMMPS input file for C-S-H simulations
In the *advanced* mode, we show how to use LAMMPS not only to perform the MD simulation but also to analyze it **_on the fly_**, allowing automation of the procedure and reducing post-processing time. Note that the input file will not work by just copy-pasting, some editing will be necessary.

First, we will include an automatic analysis of **Cl diffusion** (you have to do it also for water!). The `compute msd` produces output with the components MSDx, MSDy, MSDz, and MSDtot. Note that we define a `type_Cl` group of atoms. This group must be placed after reading the data file, and before the `compute msd`. The values from this compute can be printed in the ouput by including them in a custom `thermo_style`.

```
# --------- MSD & DIFFUSION COEFFICIENTS ----------
group           Cl_atoms type 3
compute         msdCl Cl_atoms msd        # compute msd produce: [1]=MSDx, [2]=MSDy, [3]=MSDz, [4]=MSDtot  (in Å^2)
```

From the slope of the MSD vs time, the diffusion coefficient can be computed from the Einstein formula. You could do it in post-processing.

$$
D = \frac{1}{2d} \frac{\mathrm{d}}{\mathrm{d}t} \big\langle \lvert \mathbf{r}(t)-\mathbf{r}(0)\rvert^2 \big\rangle\Big|_{t\to\infty}
= \frac{1}{2d} \frac{\mathrm{d}}{\mathrm{d}t} \big\langle \mathrm{MSD_d} \big\rangle\
$$ 

The second property will be the **density profile** of the Cl ions in the slit pore (do it also for water!). The density profile represents the distribution of a given species along the direction perpendicular to the C–S–H surfaces, and helps us to understand adsorption and the formation of electrical double layers. The `compute` command divides the simulation box along the z-axis into bins of width _dz_A_ (define before), starting from the lower boundary of the box. Each Cl atom (from the group defined earlier) is then assigned to a bin according to its z-coordinate. With this command we compute the density profile at each simulation step, but any physical observable must be obtained from the time average of the property over time. We perform this averaging with the `fix` command shown below, which generates the average number density profile along the z direction using the bins defined in `zbin`. Every 1000 steps it samples `c_bin`, takes 100 samples, and writes the profile into density_z.dat every 10000 steps. The _ave running_ option means that cumulative averages are computed over the entire simulation rather than using short, independent blocks generated every 200 steps.

```
# --------- Density profile in z ----------
variable        dz_A    equal 0.5
compute         zbin Cl_atoms chunk/atom bin/1d z lower ${dz_A} units box       # Chunks along the z direction (from the lower boundary of the simulation box)
fix             profA Cl_atoms ave/chunk 1000 100 10000 zbin density/number file density_z.dat ave running     # Density (particles/Å^3). 
```

Remember: **LAMMPS reads the input file in order!** The analysis blocks must be placed in the correct position within the input file — not simply appended at the end. Furthermore, to print the MSD values, you need to modify your `thermo_style`:

```
thermo_style    custom step time temp etotal c_msdCl[1] c_msdCl[2] c_msdCl[3] c_msdCl[4]
```

