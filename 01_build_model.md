# Build a basic C–S–H model with pyCSH

The first step for a high quality simulation of C-S-H (and any other material) is to build an atomic scale model as realistic as possible. In other words, a model that comprises all the necessary features to represent the real conditions to reproduce the experimental physical properties. In our case, we will build a "slit-pore C-S-H model" to study NaCl diffusion in C-S-H nanopores.

The general procedure for building a slit pore in a calcium–silicate–hydrate (C–S–H) is:

- **Build the bulk structure**  A detailed description of the different model construction methods can be found in this [review article](https://doi.org/10.1016/j.cemconres.2022.106784). Here we will use the [pyCSH code](https://doi.org/10.1016/j.cemconres.2024.107593), a Python code for the automated generation of realistic bulk calcium silicate hydrate (C-S-H) structures.

- **Introduce the pore** (slit geometry) Choose a crystallographic direction perpendicular to the layers of interest. Define a “gap” by translating one part of the structure away from the other, thereby creating an empty region. The pore width can be tuned by setting the separation distance between the two C–S–H surfaces.

- **Saturate with water** Insert water molecules into the pore region using a packing algorithm. Reach realistic densities by filling until the desired target pore solution density is reached or by MD relaxation.

> ✏️ **Novel users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code. The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1.3, a C-S-H surface of least 2.25nm^2, and a pore space of aprox 2nm filled with water and 10NaCl ion pairs. The files must be written in lammps_xxxx format. _Estimated time XXX min_.

> ✒️ **Advanced users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code **_and packmol_**. The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1.3, a C-S-H surface of least 2.25nm^2, and a pore space of aprox 2nm filled with water and 10NaCl ion pairs. The files must be written in lammps_xxxx format. _Estimated time XXX min_.

---

### Construction of C-S-H model using pyCSH.

PyCSH descripción y lo que puede hacer( inclyyo abrir poro y meter moleculas 

```{Note}
Advanced users do not saturate the pore after with packmol
```

**1. Donwload pyCSH** Download the zip file from the github repository. Unzip and enter the folder (e.g. csh_basic/).

**2. Edit the input.py**  Open **input.py** in your text editor. You will have to change a few parameters to build your model.

```{tip}
In windows the default is _Notepad_, in Mac _Textedit_ and in Linux _Nano_. They are enough, specially _Nano_, but if you are going to work on simulations, we recommend to use something more sophisticated as _vim_ or _visual studio_ despite teh steper learning curve.
```

The parameters that control the generated CSH models are defined in `parameters.py`, and are the following:

 - `seed`: **Optional**. Default : 1123
   Seed for the random number generator.
   
- `shape`: **Required**
  Shape of the supercell of defective tobermorite 14 A. Tuple of the shape (Nx, Ny, Nz).
  
- `Ca_Si_ratio`: **Required**
Target Ca/Si ratio of the CSH model.

- `W_Si_ratio`: **Required**
Target water/Si ratio of the CSH model.

- `prefix`: **Optional**. Default: 'input'
  Name of the output files.
 
- `N_samples`: **Required**
Number of structures to be generated.

- `make_independent`: **Optional**. Default: False
  Whether to ensure that none of the structures are different spatial arrangement of the same unit cells or not.

- `offset_gaussian`: **Optional**. Default: False
  If True, some preliminary calculations will be done in order to impose more strictly that the amount of Ca-OH and Si-OH are closer to the experimental values.

- `width_Ca_Si`: **Optional**. Default: 0.1
Width of the gaussian used for sampling the Ca/Si ratio of each of the unit cells that compose the total supercell.  Smaller values (e.g. 0.01) will  lead to ratios closer to the target, but might cause the code to fail.

- `width_SiOH`: **Optional**. Default: 0.08
Width of the gaussian used for sampling the Si-OH/Si ratio.

- `width_CaOH`: **Optional**. Default: 0.04
Width of the gaussian used for sampling the Ca-OH/Ca ratio.

- `create`: **Required**.
True if you want to generate new structures, False, if other modes are required. See `check` and `read_structure`.

- `check`: **Optional**. Default: False
If True, a prelimilary check for a wide range of Ca/Si ratios will be performed, in order to show the accuracy of the generated models for the selected parameters with respect to the Ca/Si ratio, water/Si ratio etc.

- `read_structure`: **Optional**. Default: False
If True, handmade brick code will be read from the end of the parameters file.

- `surface_from_bulk`: **Optional**. Default: False.
If True, the handmade structure will be transformed to a surface  in the **z** dimension by adding upper (">Lo", ">Ro") and lower ("<Lo", "<Ro") chains.

- `surface_separation`: **Optional**. Default: False
Approximate distance between the layers of CSH surfaces.
	 
- `write_lammps`: **Optional**. Default: True
Write a `.data` LAMMPS data file for each of the structures. 

- `write_lammps_erica`: **Optional**. Default: True
Write a `.data` LAMMPS data file for each of the structures, with core-shell, bonds and angle information to use with EricaFF.

- `write_vasp`: **Optional**. Default: True
Write a `.vasp` VASP data file for each of the structures. 


**3. Run pyCSH** In a terminal inside the folder (or VScode) run simply 

```
python3 run.py
```

That’s it! The script will read you input.py, build the required C–S–H models, save structure files, and produce some plots.

**4. What the outputs are and how to read them**

- prefix.data/vasp/xyz/... — Datafiles containing the atomic postions LAMMPS data file OVITO can open LAMMPS data directly.
- name.xyz — simple XYZ with all atoms. OVITO can open it directly. Good for quick previews.
- name.cif — CIF crystallographic file. VESTA can open it directly. Preferred for VESTA (periodic cell handled nicely).

Plots:
- MCL.pdf, Ca/Si

> ✏️ **Next step Novel users** Select one of the models and move to the topology section. By looking at the results elegir el mas representativo y comtinuar. 

> ✒️ **Advanced users** Select one of the models by looking at the results elegir el mas representativo. Still packmol setps


### Packmol (advanced users)

### Packing molecular systems with Packmol

Packmol is a program designed to create initial configurations for molecular dynamics simulations by packing molecules into defined regions of space according to user-specified geometric constraints. It takes as input one or more molecular structures (in PDB or XYZ format) and places them inside a simulation box or around predefined surfaces, ensuring that the molecules do not overlap and that a minimum distance between atoms is respected.

pyCSH allows also to insert water molecules and certain ions within the slit pore. However, Packmol offers much greater flexibility: it allows you to pack any kind of molecule, such as solvents, organic additives, surfactants, or any other chemical compound species, into complex geometries, interfaces, or pores. This makes it extremely useful when constructing more heterogeneous systems. 

**1. Installing Packmol**

Before using Packmol to build our systems, we need to install it on our computers. Packmol is available on Linux, macOS and Windows, and can be downloaded it from its [official website](https://m3g.github.io/packmol/download.shtml).

**2. Creating a Packmol input file**

To build a system with Packmol, we first need to create a plain text file with the `.inp` extension (for example, `Packing.inp`). This file must contain all the instructions that indicate Packmol which molecules to include, how many copies of each, and where to place them in space. An example of a typical Packmol input file is shown below:
```
tolerance 2.0
filetype pdb
output Packed_System.pdb

structure CSH.pdb
number 1
center
fixed 10.0 10.0 10.0 0.0 0.0 0.0
end structure

structure NaCl.pdb
number 20
inside box 0.5 0.5 0.5 19.5 19.5 19.5
end structure

structure Water.pdb
number 300
inside box 0.5 0.5 0.5 19.5 19.5 19.5
end structure
```
In this input file:
- **`tolerance 2.0`** defines the minimum allowed distance (in Å) between atoms belonging to different molecules to avoid overlaps.  
- **`filetype pdb`** indicates that all structure files are provided in PDB format.  
- **`output Packed_System.pdb`** is the name of the resulting packed system that will be created.  
- The **`structure ... end structure`** blocks define the molecules to be included and how they are positioned:
  - The keyword **`number 1`** indicates that only one copy will be inserted.
  - The keyword **`structure`** loads the atomic coordinates from the corresponding `.pdb` file.
  - **`center`** tells Packmol to center the coordinates of that structure with respect to the defined box, while **`fixed 10.0 10.0 10.0 0. 0. 0.`** indicates that the (center of the) structure should be place exactly at that position (10.0 10.0 10.0) and prevents it from moving during packing. The last three zeros correspond to allowed translation tolerances (here all set to zero, meaning the structure remains completely fixed).
  - The command **`inside box 0.5 0.5 0.5 19.5 19.5 19.5`** defines a three-dimensional region — in this case, a rectangular box — inside which Packmol will randomly place the predefined number of molecules. The six numerical values correspond to the lower and upper limits of the box along the three Cartesian coordinates (x_min, y_min, z_min and x_max, y_max, z_max).
> [!WARNING]
> **Periodic boundary conditions and box margins**
>
>  When using periodic boundary conditions (PBC), atoms located exactly at the edges of the simulation box are periodically replicated on the opposite side. If Packmol places molecules too close to the box boundaries, this replication can cause overlaps between periodic images, leading to unrealistic atomic contacts or large forces during energy minimization.
>
> To prevent this, it is recommended to leave a small safety margin* between the packing region and the box limits — typically 0.5 Å on each side. This ensures that no atom lies exactly on the boundary, avoiding artificial overlaps when the system is replicated under PBC and improving the stability of the subsequent molecular dynamics simulation.

**3. Running Packmol**

Once the input file (for example `Packing.inp`) is ready and all the molecular structure files (`.pdb` files) are in the same directory, Packmol can be runned directly from the terminal. To do so, navigate to the folder containing your input file and execute:
```
./packmol < Packing.inp
```
When using this command, Packmol reads all the packing instructions, load the molecular coordinates from the `.pbd` files, and place each molecule inside the specified regions while ensuring that no overlaps occur according to the defined tolerance.
During execution, Packmol prints progress information in the terminal (such as iteration steps and molecule placement).
When it finishes, a new file — in this example `System.pdb` — will be created in the same directory. This file contains the complete packed configuration of your system. This file can be opened in VMD or another molecular visualization program to inspect the result before generating the corresponding LAMMPS data file.

> [!TIP]
> **Packing the pore region directly in LAMMPS**
>
> The approach shown here uses Packmol to fill the pore of a C–S–H model with water and ions by explicitly packing them around the solid block. However, LAMMPS offers an alternative since it allows to merge multiple systems by reading several `.data` files in sequence. This can be useful for constructing hybrid systems such as a C–S–H matrix with an empty pore and a separate box containing pre-packed water and ions to fill the empty C-S-H pore. In this way, by keeping a single structural framework (for example, the same C–S–H slab) and replacing only the pore box `.data` file, a set of simulations with different compositions — varying water content, ion concentration, or even alternative pore chemistries — can be easily created without rebuilding the solid phase each time. The process is straightforward and implies loading one of the structures using `read_data CSH.data` and adding the new atoms from the other data file without replacing the existing ones with `read_data Pore_box.data add append shift 0 0 0`. **`shift`** can be used to move the entire *pore_box* block into the desired region (for example, inside the pore).
> It is essential that both data files use the same `atom_style`, units, and consistent atom-type numbering. If the second data file defines overlapping atom types (same atom-type number), they should be renumbered to avoid conflicts.


