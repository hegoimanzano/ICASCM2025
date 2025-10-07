# Writing the LAMMPS input

The LAMMPS **input file** contains, together with the **data file** that we built, the necessary information to run (an analyse) your molecular dynamics simulation. We present the **input file** in several pieces to explain the different aspects of the simulation. At the end of this page you will find the complete input file to facilitate coy-paste.

### Basic structure of a LAMMPS input file
_If you are a experienced user, you can skip this section_

The options in LAMMPS are vast. The [LAMMPS Manual](https://docs.lammps.org/) might be overwhelmig for begginers, but it contains all the necessary information to build an **input file**. A LAMMPS **input file** is basically a script that tells the MD engine exactly how to build, run, and analyze a molecular simulation. It is written in a line-by-line command language, not in Python or C++, but in its own syntax. You can think of it as having four layers:

**1. Header / Global Settings** These commands define the units, atom style, boundary conditions, and load your starting structure.

**2. Force Field Definition** Here you specify interatomic potentials and their parameters.
- pair_style + pair_coeff = how nonbonded atoms interact. 
- bond_style, angle_style, dihedral_style = for bonded terms.
- kspace_style = long-range electrostatics.
- special FF like COMB, ReaxFF, or MLP have their own syntax

**3. Simulation Control** This is the heart of the input. It defines time integration, thermostats/barostats, neighbor lists, and trajectory dumps. There are different commands grouped in large families:
- fix = continuous operations applied at every step of the simulation (e.g., integrators like fix nvt, thermostats, SHAKE constraints, MSD calculators, walls, restraints).
- dump = how to write trajectory snapshots and how often
- thermo and thermo_style → control which thermodynamics quantities and other paramaters appears in log output file and how oftern

LAMMPS has compute and variable as analysis tools, and fix ave/time to average over time. (computes, variables, averages)
- compute = generates per-atom or global quantities (MSD, stress, RDF, density profiles).
- variable = algebra with computed quantities.
- fix ave/time / fix ave/chunk = averages, profiles, histograms.

**4. Execution** Finally, you tell LAMMPS to run → length of the simulation (number of timesteps).

Note that LAMMPS interprets commands strictly in the order they appear in the input file. This means that the simulation environment is built step by step, and a command cannot use information that has not yet been defined. You must be carefull with the order of the commands.

--
### LAMMPS input file for C-S-H simulations

**1. Header / Global Settings** We are going to simulate a C-S-H box with periodic boundary conditions in x y z. There are different units systems that must be consistent with your force field and all the input parameters. Note that the all the results will also be printed in these units. The _atom_style_ defines what information is stored for each atom. The choice depends on the physics of your system and the force field you plan to use. In our case with CSHFF, we require full, which indicates information about _atom_id, type, coordinates, charge, molecule-ID, bonds, angles, dihedrals_. 
The _neighbor_-related options refer to how LAMMPS builds the pairwise neighbor lists to compute forces between atoms. They affect the efficiency and sometimes may induce errors, but it is safe to use the standard values. More info on [neighbors](https://docs.lammps.org/Developer_par_neigh.html)

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

**3. Simulation Control** Now we start the simulation. In any MD simulations there are at least two stpes. First, an **equilibration period**, in which our system adapts to the desidered thermodynamic conditions. The equilibration time is system-specific, and depends on your initial simulation protocol, how you build your simulation box, the force field, the final thermodynamic conditions, etc. For example, AND GIVE EXAMPLEs

```
# ---------- FAST EQUILIBRATION ----------
velocity        all create 300.0 4928459 rot yes mom yes
fix             nvt all nvt temp 300.0 300.0 100.0
thermo          1000
thermo_style    custom step temp pe etotal press density
run             10000
unfix           nvt
```
_NOTE it is also common, altough we did not do it, to perform an energy minimization step before the equilibration to relax the initial simulation box and avoid "explosions" due to overlapping of atoms_


```
# ---------- PRODUCTION ----------
reset_timestep  0
fix             nvt all nvt temp 300.0 300.0 100.0
thermo          1000
run             50000
```

```
# --------- MSD & DIFUSIÓN ----------
# compute msd produce: [1]=MSDx, [2]=MSDy, [3]=MSDz, [4]=MSDtot  (en Å^2)
compute         msd_all mobile msd

# tiempo en ps (dt en fs -> ps = fs * 1e-3)
variable        t_ps    equal step*dt*1.0e-3

# Evitar división por cero al inicio (usa max(t, tiny))
variable        t_safe  equal max(v_t_ps,1.0e-9)

# Difusiones (m^2/s): D_x = MSDx / (2 t) * (Å^2/ps -> m^2/s = 1e-8)
variable        Dx      equal c_msd_all[1]/(2.0*v_t_safe) * 1.0e-8
variable        Dy      equal c_msd_all[2]/(2.0*v_t_safe) * 1.0e-8
variable        Dz      equal c_msd_all[3]/(2.0*v_t_safe) * 1.0e-8
# D_total (3D): MSDtot / (6 t)
variable        Dtot    equal c_msd_all[4]/(6.0*v_t_safe) * 1.0e-8

# Registrar serie temporal (MSD + D)
# Nevery Nrepeat Nfreq = 100 10 1000 -> cada 1000 pasos (1 ps) si dt=1 fs
fix             msdout all ave/time 100 10 1000 \
                c_msd_all[1] c_msd_all[2] c_msd_all[3] c_msd_all[4] \
                v_Dx v_Dy v_Dz v_Dtot \
                file msd_D.dat mode vector
# Columnas: time_step MSDx MSDy MSDz MSDtot Dx Dy Dz Dtot  (t en *pasos*; convertir a ps con dt)

# Mostrar en thermo también (resumen)
thermo_style    custom step temp c_msd_all[1] c_msd_all[2] c_msd_all[3] c_msd_all[4] v_Dtot

# --------- PERFIL DE DENSIDAD EN z ----------
# Bin size en nm (ajusta). LAMMPS usa Å en 'real'; delta_A = dz_nm*10
variable        dz_nm   equal 0.5
variable        dz_A    equal v_dz_nm*10.0

# Chunks a lo largo de z (desde el límite inferior de la caja)
compute         zbin all chunk/atom bin/1d z lower ${dz_A} units box

# Densidad numérica (#/Å^3). Guardamos y damos factor de conversión a nm^-3.
# 1 Å^-3 = 1e3 nm^-3  -> multiplica por 1000 fuera o usa la versión escalada abajo
fix             profA all ave/chunk 100 10 1000 c_zbin density/number file density_z_A3.dat ave running

# (Opcional) También #/nm^3 directamente: usamos 'count' y dividimos por volumen del bin
# Volumen del bin = Lx * Ly * dz (Å^3); multiplicador 1000/Å^3 -> nm^-3
# No hay multiplicador directo en ave/chunk, así que generamos 'count' y post-procesa:
fix             profC all ave/chunk 100 10 1000 c_zbin count file density_z_counts.dat ave running
# Para convertir a nm^-3: rho_nm3 = counts / (frames * Lx * Ly * dz_A) * 1000
# (fácil de hacer con una línea en Python o gnuplot al analizar)

# ---------- PRODUCIR TRAYECTORIA LIGERA ----------
dump            trj all custom 1000 traj.lammpstrj id type q x y z
dump_modify     trj sort id

# ---------- CORRER PRODUCCIÓN ----------


# ---------- LIMPIEZA ----------
unfix           msdout
unfix           profA
unfix           profC
undump          trj
```



You can find more information on how to perform MD simulations in LAMMPS in the [LAMMPS tutorials](https://lammpstutorials.github.io/index.html) webpage

```{code-block} none
# ---------- SETTINGS / SYSTEM ----------
units           real
atom_style      full
boundary        p p p

read_data       csh_basic.data     # <-- AJUSTA si tu fichero se llama distinto

neighbor        2.0 bin
neigh_modify    delay 10 every 1

# ---- Fuerzas (EJEMPLO: AJUSTAR a tu FF) ----
pair_style      lj/cut/coul/long 10.0 10.0
kspace_style    pppm 1.0e-4
# pair_coeff    * * 0.0 3.0     # <-- PON tus parámetros reales

# Grupos (móviles = todos; ajusta si quieres seleccionar un subconjunto)
group           mobile type <> 1 100000   # (ejemplo) aquí "mobile" = all por defecto
group           mobile clear
group           mobile union all

timestep        1.0                 # 1 fs en 'real'

# ---------- EQUILIBRACIÓN RÁPIDA ----------
velocity        all create 300.0 4928459 rot yes mom yes
fix             nvt all nvt temp 300.0 300.0 100.0
thermo          1000
thermo_style    custom step temp pe etotal press density
run             10000

unfix           nvt

# ---------- PRODUCCIÓN ----------
reset_timestep  0
fix             nvt all nvt temp 300.0 300.0 100.0
thermo          1000

# --------- MSD & DIFUSIÓN ----------
# compute msd produce: [1]=MSDx, [2]=MSDy, [3]=MSDz, [4]=MSDtot  (en Å^2)
compute         msd_all mobile msd

# tiempo en ps (dt en fs -> ps = fs * 1e-3)
variable        t_ps    equal step*dt*1.0e-3

# Evitar división por cero al inicio (usa max(t, tiny))
variable        t_safe  equal max(v_t_ps,1.0e-9)

# Difusiones (m^2/s): D_x = MSDx / (2 t) * (Å^2/ps -> m^2/s = 1e-8)
variable        Dx      equal c_msd_all[1]/(2.0*v_t_safe) * 1.0e-8
variable        Dy      equal c_msd_all[2]/(2.0*v_t_safe) * 1.0e-8
variable        Dz      equal c_msd_all[3]/(2.0*v_t_safe) * 1.0e-8
# D_total (3D): MSDtot / (6 t)
variable        Dtot    equal c_msd_all[4]/(6.0*v_t_safe) * 1.0e-8

# Registrar serie temporal (MSD + D)
# Nevery Nrepeat Nfreq = 100 10 1000 -> cada 1000 pasos (1 ps) si dt=1 fs
fix             msdout all ave/time 100 10 1000 \
                c_msd_all[1] c_msd_all[2] c_msd_all[3] c_msd_all[4] \
                v_Dx v_Dy v_Dz v_Dtot \
                file msd_D.dat mode vector
# Columnas: time_step MSDx MSDy MSDz MSDtot Dx Dy Dz Dtot  (t en *pasos*; convertir a ps con dt)

# Mostrar en thermo también (resumen)
thermo_style    custom step temp c_msd_all[1] c_msd_all[2] c_msd_all[3] c_msd_all[4] v_Dtot

# --------- PERFIL DE DENSIDAD EN z ----------
# Bin size en nm (ajusta). LAMMPS usa Å en 'real'; delta_A = dz_nm*10
variable        dz_nm   equal 0.5
variable        dz_A    equal v_dz_nm*10.0

# Chunks a lo largo de z (desde el límite inferior de la caja)
compute         zbin all chunk/atom bin/1d z lower ${dz_A} units box

# Densidad numérica (#/Å^3). Guardamos y damos factor de conversión a nm^-3.
# 1 Å^-3 = 1e3 nm^-3  -> multiplica por 1000 fuera o usa la versión escalada abajo
fix             profA all ave/chunk 100 10 1000 c_zbin density/number file density_z_A3.dat ave running

# (Opcional) También #/nm^3 directamente: usamos 'count' y dividimos por volumen del bin
# Volumen del bin = Lx * Ly * dz (Å^3); multiplicador 1000/Å^3 -> nm^-3
# No hay multiplicador directo en ave/chunk, así que generamos 'count' y post-procesa:
fix             profC all ave/chunk 100 10 1000 c_zbin count file density_z_counts.dat ave running
# Para convertir a nm^-3: rho_nm3 = counts / (frames * Lx * Ly * dz_A) * 1000
# (fácil de hacer con una línea en Python o gnuplot al analizar)

# ---------- PRODUCIR TRAYECTORIA LIGERA ----------
dump            trj all custom 1000 traj.lammpstrj id type q x y z
dump_modify     trj sort id

# ---------- CORRER PRODUCCIÓN ----------
run             50000

# ---------- LIMPIEZA ----------
unfix           msdout
unfix           profA
unfix           profC
undump          trj
unfix           nvt
```
