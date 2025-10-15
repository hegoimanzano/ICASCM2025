# Writing the LAMMPS input

The LAMMPS **input file** contains, together with the **data file** that we built, the necessary information to run (an analyse) your molecular dynamics simulation. We will have two different execises depending on the experience.


> ✏️ **Novel users** will have to follow the [Basic LAMMPS input file for C-S-H simulations](#basic-lammps-input-file-for-c-s-h-simulations) section to understand and create in a text file the LAMMPS input file. The simulation must equilibrate the system for 0.5 ps in NPT and perform a production run in NVT for 1 ps, with clayFF force field, dumping the trayectory every 200 steps and printing the properties every 100 steps.

> ✒️ **Advanced users** will have to follow the [Basic LAMMPS input file for C-S-H simulations](#basic-lammps-input-file-for-c-s-h-simulations) section, and add the information on the [Advanced LAMMPS input file for C-S-H simulations](#advanced-lammps-input-file-for-c-s-h-simulations) section to improve the LAMMPS input file. The simulation must equilibrate the system for 0.5 ps in NPT and perform a production run in NVT for 1 ps, with clayFF force field, dumping the trayectory every 200 steps and printing the properties every 100 steps. The simulation must print the MSD and the density profiles of Cl, Na and water in 2 files called MSD.txt and DP.txt.


### The structure of a LAMMPS input file
```{note}
This is a basic explanation of LAMMPS input file structure. If you are a experienced user, you can skip this section
```

The options in LAMMPS are vast. The [LAMMPS Manual](https://docs.lammps.org/) might be overwhelmig for begginers, but it contains all the necessary information to build an **input file**. A LAMMPS **input file** is basically a script that tells the MD engine exactly how to build, run, and analyze a molecular simulation. It is written in a line-by-line command language, not in Python or C++, but in its own syntax. You can think of it as having four layers:

**1. Header / Global Settings** These commands define the units, atom style, boundary conditions, and load your starting structure.

**2. Force Field Definition** Here you specify interatomic potentials and their parameters.
- pair_style + pair_coeff = how nonbonded atoms interact. 
- bond_style, angle_style, dihedral_style = for bonded terms.
- kspace_style = long-range electrostatics.
- special FF like COMB, ReaxFF, or MLP have their own syntax

**3. Simulation Control and execution** This is the heart of the input. It defines time integration, thermostats/barostats, neighbor lists, and trajectory dumps. There are different commands grouped in large families:
- fix = continuous operations applied at every step of the simulation (e.g., integrators like fix nvt, thermostats, SHAKE constraints, MSD calculators, walls, restraints).
- dump = how to write trajectory snapshots and how often
- thermo and thermo_style → control which thermodynamics quantities and other paramaters appears in log output file and how oftern

**4. Analysis** LAMMPS has compute and variable as analysis tools, and fix ave/time to average over time. (computes, variables, averages). The analysis commands are intermixed with layer 3, and they are not strictly necessary, as analysis can be done in a postprocessing stage
- compute = generates per-atom or global quantities (MSD, stress, RDF, density profiles).
- variable = algebra with computed quantities.
- fix ave/time / fix ave/chunk = averages, profiles, histograms.

Finally, you tell LAMMPS to run → length of the simulation (number of timesteps).

Note that LAMMPS interprets commands strictly **in the order** they appear in the input file. This means that the simulation environment is built step by step, and a command cannot use information that has not yet been defined. You must be carefull with the order of the commands.

---

### Basic LAMMPS input file for C-S-H simulations

**1. Header / Global Settings** We are going to simulate a C-S-H box with periodic boundary conditions in x y z. There are different units systems that must be consistent with your force field and all the input parameters. Note that the all the results will also be printed in these units. The `atom_style` defines what information is stored for each atom. The choice depends on the physics of your system and the force field you plan to use. In our case with CSHFF, we require full, which indicates information about _atom_id, type, coordinates, charge, molecule-ID, bonds, angles, dihedrals_. 
The `neighbor`-related options refer to how LAMMPS builds the pairwise neighbor lists to compute forces between atoms. They affect the efficiency and sometimes may induce errors, but it is safe to use the standard values. More info on [neighbors](https://docs.lammps.org/Developer_par_neigh.html)

```
# ---------- SETTINGS / SYSTEM ----------
units           real
atom_style      full
boundary        p p p

read_data       csh_basic.data     # write the name of your data file

neighbor        2.0 bin
neigh_modify    delay 10 every 1
```

**2. Force Field Definition** Here you specify interatomic potentials and their parameters.
- pair_style + pair_coeff → how nonbonded atoms interact. 
- bond_style, angle_style, dihedral_style → for bonded terms.
- kspace_style → long-range electrostatics.

```
# ---- Fuerzas (EJEMPLO: AJUSTAR a tu FF) ----
pair_style      lj/cut/coul/long 10.0 10.0
kspace_style    pppm 1.0e-4
# pair_coeff    * * 0.0 3.0     # <-- PON tus parámetros reales
```

**3. Simulation Control and execution** Now we start the simulation. In any MD simulations there are at least two stpes. First, an **equilibration period**, in which our system adapts to the desidered thermodynamic conditions. First we assign random `velocity` to the particles according to a Boltzmann distribution at 300 K. Then, we perform the simulation in the canonical ensemble `fix nvt`, at an initial and final temperature of 300 K, applying a thermostat every 100 steps to maintain the target temperature. We record selected `thermo` properties in the output every 1000 steps. Finally, we need to `unfix` the fix that was defined for this phase to prepare the system for the next stage.

```
# ---------- FAST EQUILIBRATION ----------
velocity        all create 300.0 4928459 rot yes mom yes
fix             nvt all nvt temp 300.0 300.0 100.0
thermo          1000
thermo_style    custom step temp pe etotal press density
run             10000
unfix           nvt
```

```{tip}
It is also common, altough we did not do it, to perform an energy minimization step before the equilibration to relax the initial simulation box and avoid "explosions" due to overlapping of atoms
```

**How long should an equilibration phase last?** The simple answer is that it should last as long as necessary, and the exact duration is system-specific, and depends on your initial simulation protocol, how you build your simulation box, the force field, the final thermodynamic conditions, etc. It is essential to  to confirm that equilibrium has truly been reached by monitoring the energy, density of the system, the mobility of the atoms, or structural properties. 

```{caution}
The energy can be misleading: if the initial configuration is very far from equeilibrium, the first energy values will often be very high, and the subsequent rapid decrease may create the false impression of convergence.
```

Second, we enter the **production phase**. In this stage, thermodynamic quantities are collected, and snapshots of the trajectory are stored in order to compute the properties of interest. The production run must be sufficiently long to ensure that the observables under study have converged. The required length strongly depends on the property we wish to calculate. For instance, if the goal is to obtain an infrared spectrum, relatively short trajectories are sufficient, since molecular vibrations take place on the timescale of a few picoseconds. If instead we are interested in the coordination of water molecules around a cation, the simulation must extend to the nanosecond or even tens of nanoseconds, because that is the timescale for water molecules to exchange between the first and second solvation shells. In this course, due to time limitations, we will restrict ourselves to production runs of about 10 picoseconds, which is sufficient for demonstration purposes. However, keep in mind that for a **reliable calculation of the mean square displacement, appropriate simulations would need to reach 100–200 nanoseconds or more**.

```
# ---------- PRODUCTION ----------
reset_timestep  0
fix             nvt all nvt temp 300.0 300.0 100.0 
thermo          1000
run             50000
```

With this basic input file + the data file, you can perform your MD simulation.

---

### Advanced LAMMPS input file for C-S-H simulations
In the "advanced" mode, we show how to use LAMMPS not only to perform the MD simulation, but also to analyse it **_on the fly_**. The input will not work by just copy-pasting, and some editing will be necessary.
Doing the analysis on the fly saves time optimising the simulation pipelines and makes allows automatization of the procedure. 

First, we will include an automatic analysis of **Cl diffusion**. The `compute msd` produces a with the components MSDx, MSDy, MSDz, MSDtot. Note that we have a `type_Cl` group of atoms. This group must be defined after reading the data file, and before the `compute msd`. The values from the compute can be printed in the ouput calling them in a custom `thermo_style`

```
# --------- MSD & DIFFUSION COEFFICIENTS ----------
# compute msd produce: [1]=MSDx, [2]=MSDy, [3]=MSDz, [4]=MSDtot  (en Å^2)
group           Cl_atoms type Cl
compute         msdCl Cl_atoms msd
thermo_style    custom step temp c_msdCl_all[1] c_msdCl_all[2] c_msdCl_all[3] c_msdCl_all[4]
```

From the slope of the msd vs time, the diffusión coefficient can be computed from the Einstein formula. You could do it in postprocessing.

$$
D = \frac{1}{2d} \frac{\mathrm{d}}{\mathrm{d}t} \big\langle \lvert \mathbf{r}(t)-\mathbf{r}(0)\rvert^2 \big\rangle\Big|_{t\to\infty}
= \frac{1}{2d} \frac{\mathrm{d}}{\mathrm{d}t} \big\langle \mathrm{MSD_d} \big\rangle\
$$ 

The second property will be the **density profile** of the XXX in the slit pore. The density profile represents the density of secies in perpendicular to the C-S-H surfaces, and helps us to understand adsorption and the formation of electrical double layers. The `compute` command divides the simulation box along the z-axis into bins of width _dz_A_ (define before), starting from the lower boundary of the box. Each Cl atom (group defined before) is then assigned to a bin according to its z-coordinate. With this command we compute the density profile at each simulation step, but any physical observable must be obtained from the time average of the property over time. We do it with the next `fix` command, which generates the average number density profile along the z direction using the bins defined in `c_zbin`. Every 10 steps is samples c_bin, it takes 20 samples, and it writes the profile into density_z_A3.dat every 10x20 = 200 steps. The _ave running_ instruction, implies that then we do cumulative averages over the entire simulation, rather than  take the short blocks generated every 200 steps.

```
# --------- PERFIL DE DENSIDAD EN z ----------
# Bin size en nm (ajusta). LAMMPS usa Å en 'real'; delta_A = dz_nm*10
variable        dz_A    equal 0.5

# Chunks a lo largo de z (desde el límite inferior de la caja)
compute         zbin Cl_atoms chunk/atom bin/1d z lower ${dz_A} units box

# Densidad numérica (#/Å^3). Guardamos y damos factor de conversión a nm^-3.

fix             profA all ave/chunk 10 20 200 c_zbin density/number file density_z_A3.dat ave running
```


