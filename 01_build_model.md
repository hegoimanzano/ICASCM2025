# Build a basic C–S–H model with pyCSH

The first step for a high quality simulation of C-S-H (and any other material) is to build an atomic scale model as realistic as possible. In other words, a model that comprises all the necessary features to represent the real conditions to reproduce the experimental physical properties. In our case, we will build a "slit-pore C-S-H model" to study NaCl diffusion in C-S-H nanopores.

The general procedure for building a slit pore in a calcium–silicate–hydrate (C–S–H) is:

- **Build the bulk structure**  A detailed description of the different model construction methods can be found in this [review article](https://doi.org/10.1016/j.cemconres.2022.106784). Here we will use the [pyCSH code](https://doi.org/10.1016/j.cemconres.2024.107593), a Python code for the automated generation of realistic bulk calcium silicate hydrate (C-S-H) structures.

- **Introduce the pore** (slit geometry) Define a “gap” by translating one part of the structure away from the other in perpendicular to the C-S-H layers (z axis). The pore width can be tuned by setting the separation distance between the two C–S–H surfaces.

- **Saturate with water** Insert water molecules and ions into the pore region using pyCSH or a packing algorithm. Reach realistic densities by filling until the desired target pore solution density is reached or by MD relaxation.

> ✏️ **Novice users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code. The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1, a C-S-H surface about 1.5 nm$^2$, 2 C-S-H layers, and a pore space of aprox 2 nm filled with water and 10 NaCl ion pairs. The files must be written in lammps.data format. _Estimated time XXX min_.

> ✒️ **Advanced users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code **_and packmol_** (do not saturate the pore space automatically!). The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1, a C-S-H surface about 1.5 nm$^2$, 2 C-S-H layers, and a pore space of aprox 2 nm filled with water and 10 NaCl ion pairs. The files must be written in lammps.data format. _Estimated time XXX min_.

---

### Construction of C-S-H model using pyCSH.

PyCSH is a Open Access code developed orginally by UPV/EHU and EPFL teams for the automated generation of realistic bulk calcium silicate hydrate (C-S-H) structures. Specifying the desidered chemistry and system size, the code generates automatically hundreds of structures. 

```{Warning}
You will use today a beta version of pyCSH v2.0. We have tested the specific example that you will use in this tutorial, but we do not advise to use it for scientific production until the code is oficially released.
```

**1. Download pyCSH** Download the zip file from the [github repository](https://github.com/hegoimanzano/pyCSH/tree/v1.1). Click in `Code` and `Download .zip`. Unzip and enter the folder with your terminal or with VScode.

**2. Edit the `parameters.py`**  Open `parameters.py` file in your text editor. You will have to change a few parameters to build your model according to the instructions above.

```{tip}
In windows the default is _Notepad_, in Mac _Textedit_ and in Linux _Nano_. They are enough, specially _Nano_, but if you are going to work on simulations, we recommend to use something more sophisticated as _vim_ or _visual studio_ despite teh steper learning curve.
```

The parameters that control the generated CSH models are defined in `parameters.py`, and are the following:

 - `seed`: **Optional**. Default : 1123. 
   Seed for the random number generator.
   
- `size`: **Required**.
Size of the C-S-H model supercell in terms of bricks. Tuple of the shape (Nx, Ny, Nz). 

- `Ca_Si_ratio`: **Required**.
Target Ca/Si ratio of the CSH model.

- `W_Si_ratio`: **Required**.
Target water/Si ratio of the CSH model.

- `prefix`: **Optional**. Default: "input".
  Name of the output files. The name must be between 
 
- `N_samples`: **Required**.
Number of structures to be generated.

- `make_independent`: **Optional**. Default: False.
 True implies that none of the structures are equal, or have a different spatial arrangement of the same unit cells.

- `offset_gaussian`: **Optional**. Default: False.
  If True, some preliminary calculations will be done in order to impose more strictly that the amount of Ca-OH and Si-OH are closer to the experimental values.

- `width_Ca_Si`: **Optional**. Default: 0.1.
Width of the gaussian used for sampling the Ca/Si ratio of each of the unit cells that compose the total supercell. Smaller values (e.g. 0.01) will  lead to ratios closer to the target, but the code might not be able to find a solution.

- `width_SiOH`: **Optional**. Default: 0.08.
Width of the gaussian used for sampling the Si-OH/Si ratio. Same as before.

- `width_CaOH`: **Optional**. Default: 0.04.
Width of the gaussian used for sampling the Ca-OH/Ca ratio. Same as before.

- `create`: **Required**.
True if you want to generate new structures, False, if other modes are required. See `check` and `read_structure`.

- `check`: **Optional**. Default: False.
If True, a prelimilary check for a wide range of Ca/Si ratios will be performed, in order to show the accuracy of the generated models for the selected parameters with respect to the Ca/Si ratio, water/Si ratio etc.

- `read_structure`: **Optional**. Default: False.
If True, handmade brick code will be read from the end of the parameters file.

- `diferentiate`: **Optional**. Default: True.
Atoms are distinguished depending on their topological environment.

- `orthogonal`: **Optional**. Default: False.
Wheter your simulation box keeps the original shape or is converted to orthogonal
 
- `write_lammps`: **Optional**. Default: False.
Write a `prefix.data` LAMMPS data file for each of the structures with 

- `write_lammps_erica`: **Optional**. Default: False.
Write a `.data` LAMMPS data file for each of the structures, with core-shell, bonds and angle information to use with EricaFF.

- `write_vasp`: **Optional**. Default: False.
Write a `.vasp` VASP data file for each of the structures.

- `Dpore`:  **Optional**. Default: 0.0.
The expansion of the desired pore in Å. A value of 0.0 indicates no pore opening. The pore is always created at the center of the supercell

- `shift` = **Optional**. Default: False.
Shif the layers to ensure that the center of the supercell matches with an interlaminar space. Basically, you need to shift your system if the number of blocz in z dimension is even. 



**3. Run pyCSH** In a terminal inside the folder (or VScode) run simply 

```
python3 main_brick.py
```

That’s it! in few seconds you will have your structures. The script will read you parameters.py, build the required C–S–H models, save structure files, and produce some plots.  

**4. What the outputs are and how to read them**

pyCSH creates automatic plots with the characteristics of the **bulk** C-S-H. Note that the Ca/Si or w/si ratio of the simulation box with the pore opened does not make sense. The generated plots are:

- **distributions.pdf**: The generated models have a slighlty variable chemistry around the desidered value. The distributions are shown in this file.
- **X-OH.pdf**: the ratio of Ca-OH/Ca and Si-OH/Si of the generated models as a function of the Ca/Si ratio, and  compared with the experimental data
- **MCL.pdf**: the mean chain lenghts of the generated models as a function of the Ca/Si ratio, and compared with the experimental data
- **water.pdf**: the water content of the generated models, normalised by the silicate content, and compared with the experimental data

pyCSH also generates a **output** folder where you will find several files (# denotes structure number):

- **prefix_#.log**: Files contain the information about the specific model (composition, size, etc), the "fingerprint" of the model (all the blocks used in the construction and their position in the supercell) and the charge distribution (not all the blocks are neutral, but the final structure is always neutral)
- **prefix_#.data/vasp/siesta...**: Files containing the atomic structure in the required format.

Check the plots and files. Open the `.data` and visualise them with OVITO. Select one of the generated models to continue. Rename your particle types according to the table below (right menu), change colors and sizes to improve visualization (usually smaller), and create bonds (`Add modification` menu).  Export it from OVITO in `.xyz` format

| Type | Mass | pyCSH Label | radius  |   |
|----|-------------|--------|---|---|
| 1  | 40.08  | Ca_1  |   |   |
| 2  | 40.08  | Ca_2  |   |   |
| 3  | 28.10  | Si_1  |   |   |
| 4  | 28.10  | Si_2  |   |   |
| 5  | 15.79  | O_Ca  |   |   |
| 6  | 15.79  | O_Si  |   |   |
| 7  | 15.79  | O     |   |   |
| 8  | 15.79  | Ow    |   |   |
| 9  | 15.79  | Oh    |   |   |
| 10 | 1.00   | Hw    |   |   |
| 11 | 1.00   | H     |   |   |

```{Tip}
You can save `.OVITO` session states with all the parameters and modifications and load them for new atomic structures
```

> ✏️ **Next step for Novice users** Move your model to the next page "topology".  

> ✒️ **Next step for Advanced users** Move to the next section "Packing molecular systems with Packmol"


### Packing molecular systems with Packmol  (advanced users)

Packmol is a program designed to create initial configurations for molecular dynamics simulations by packing molecules into defined regions of space according to user-specified geometric constraints. It takes as input one or more molecular structures and places them inside a simulation box or around predefined surfaces, ensuring that the molecules do not overlap and that a minimum distance between atoms is respected.

pyCSH allows to insert water molecules and certain ions within the slit pore in very simple cases. Packmol offers much greater flexibility: it allows you to pack any kind of molecule, such as solvents, organic additives, surfactants, or any other chemical compound species, into complex geometries, interfaces, or pores. This makes it extremely useful when constructing more heterogeneous systems. 

**1. Installing Packmol**

Packmol is available on Linux, macOS and Windows, and can be downloaded it from its [official website](https://m3g.github.io/packmol/download.shtml).

**2. Creating a Packmol input file**

To build a system with Packmol, we first need to create a plain text file with the `.inp` extension (for example, `Packing.inp`). This file must contain all the instructions that indicate Packmol which molecules to include, how many copies of each, and where to place them in space. An example of a typical Packmol input file is shown below:

```
tolerance 2.0
filetype xyz
output Packed_System.xyz

structure name.xyz
number 1
center
fixed 10.0 10.0 10.0 0.0 0.0 0.0 # input your simulation box parameters
end structure

structure Water.xyz
number 300
inside box 0.5 0.5 0.5 19.5 19.5 19.5
end structure

...
...
```

In this input file:
- **`tolerance`** defines the minimum allowed distance (in Å) between atoms belonging to different molecules to avoid overlaps.  
- **`filetype`** indicates the format of the output file, .pdb or .xyz
- **`output`** is the name of the resulting packed system that will be created.  
- The **`structure ... end structure`** blocks define the molecules to be included and how they are positioned:
  - **`number`** indicates the number of molecules/systems to be inserted.
  - **`structure`** loads the atomic coordinates from the corresponding molecule/system defined in a separated file.
  - **`inside box 0.5 0.5 0.5 19.5 19.5 19.5`** defines a three-dimensional region inside which Packmol will randomly place the predefined number of molecules. The six numerical values correspond to the lower and upper limits of the box along the three Cartesian coordinates (x_min, y_min, z_min and x_max, y_max, z_max).
  - **`center`** tells Packmol to center the coordinates of that structure with respect to the defined box
  - **`fixed`** indicates that the (center of the) structure should be place exactly at that position (10.0 10.0 10.0) and prevents it from moving during packing. The last three zeros correspond to allowed translation tolerances (here all set to zero, meaning the structure remains completely fixed).
 
 Note that you need to prepare your Na.xyz, Cl.xyz and H20.xyz files independently with a xyz file format:
 
```
<number of atoms>
comment line or blank 
<element> <X> <Y> <Z>
...
...
```
 
 There are many other options available to define how molecules are packed and in the region of the space. You can check them in the packmol manual

 
```{Warning}
When using periodic boundary conditions (PBC), atoms located exactly at the edges of the simulation box are periodically replicated on the opposite side. If Packmol places molecules too close to the box boundaries, this replication can cause overlaps between periodic images, leading to unrealistic atomic contacts or large forces during energy minimization. To prevent this, it is recommended to leave a small safety margin* between the packing region and the box limits — typically 0.5 Å on each side. This ensures that no atom lies exactly on the boundary, avoiding artificial overlaps when the system is replicated under PBC and improving the stability of the subsequent molecular dynamics simulation.
```

**3. Running Packmol**

Once the input file (for example `Packing.inp`) is ready and all the molecular structure files (`.pdb` files) are in the same directory, Packmol can be runned directly from the terminal. To do so, navigate to the folder containing your input file and execute:

```
./packmol < Packing.inp
```

When using this command, Packmol reads all the packing instructions, load the molecular coordinates from the `.xyz` files, and place N copies of each molecule inside the specified regions while ensuring that no overlaps occur according to the defined tolerance. During execution, Packmol prints progress information in the terminal (such as iteration steps and molecule placement). When it finishes, a new file (in this example `Packed_System.xyz`) will be created in the same directory. This file can be opened in VMD or another molecular visualization program to inspect the result before generating the corresponding LAMMPS data file.

```{Tip}
**Packing the pore region directly in LAMMPS**. The approach shown here uses Packmol to fill the pore of a C–S–H model with water and ions by explicitly packing them in the pore space. However, LAMMPS offers an interesting alternative for automatization. Tt allows to merge multiple systems by reading several `.data` files in sequence. This can be useful for constructing hybrid systems such as a C–S–H matrix with an empty pore, and a separate box containing pre-packed water and ions to fill the empty C-S-H pore. In this way, by keeping a single structural framework (for example, the same C–S–H slab) and replacing only the pore box `.data` file, a set of simulations with different compositions — varying water content, ion concentration, or even alternative pore chemistries — can be easily created without rebuilding the solid phase each time. The process is straightforward and implies loading one of the structures using `read_data CSH.data` and adding the new atoms from the other data file without replacing the existing ones with `read_data Pore_box.data add append shift 0 0 0`. **`shift`** can be used to move the entire *pore_box* block into the desired region (for example, inside the pore). It is essential that both data files use the same `atom_style`, units, and consistent atom-type numbering. If the second data file defines overlapping atom types (same atom-type number), they should be renumbered to avoid conflicts.
```

