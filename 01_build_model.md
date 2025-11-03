# Build a basic C–S–H model with pyCSH

The first step for a high-quality simulation of C–S–H (and any other material) is to build an atomic-scale model as realistic as possible. In other words, a model that comprises all the necessary features to represent the real conditions to reproduce the experimental physical properties. In our case, we will build a "slit-pore C–S–H model" to study NaCl diffusion in C–S–H nanopores.

The general procedure for building a slit pore in a calcium–silicate–hydrate (C–S–H) is:

- **Build the bulk structure**  A detailed description of the different model construction methods can be found in this [review article](https://doi.org/10.1016/j.cemconres.2022.106784). Here we will use the [pyCSH code](https://doi.org/10.1016/j.cemconres.2024.107593), a Python code for the automated generation of realistic bulk calcium silicate hydrate (C–S–H) structures.

- **Introduce the pore** (slit geometry) Define a “gap” by translating one part of the structure away from the other perpendicular to the C–S–H layers (z axis). The pore width can be tuned by setting the separation distance between the two C–S–H surfaces.

- **Saturate with water** Insert water molecules and ions into the pore region using pyCSH or a packing algorithm. Reach realistic densities by filling until the desired target pore solution density is reached or by MD relaxation.

> ✏️ **Novice users** will have to follow the instructions to build 10 unique C–S–H models using the pyCSH code. The final models should be orthogonal, have a C/S ratio 1.2, a w/S ratio of 0.75, a C–S–H surface about 1.5 nm$^2$, 2 C–S–H layers, and a pore space of approx. 2 nm filled with water and 5 NaCl ion pairs. The files must be written in lammps.data format. _Estimated time XXX min_.

> ✒️ **Advanced users** will have to follow the instructions to build 10 unique C–S–H models using the pyCSH code **_and packmol_** (do not saturate the pore space automatically!). The final models should be orthogonal, have a C/S ratio 1.2, a w/S ratio of 0.75, a C–S–H surface about 1.5 nm$^2$, 2 C–S–H layers, and a pore space of approx. 2 nm filled with water and 5 NaCl ion pairs (also with packmol). The files must be written in lammps.data format. _Estimated time XXX min_.

---

### Construction of C–S–H model using pyCSH

PyCSH is an Open Access code developed originally by UPV/EHU and EPFL teams for the automated generation of realistic bulk calcium silicate hydrate (C–S–H) structures. Specifying the desired chemistry and system size, the code generates automatically hundreds of structures. 

```{Warning}
You will use today a beta version of pyCSH v2.0 still under development. We have tested the specific examples that you will use in this tutorial, but we (strongly) do not advise to use it for scientific production until the code is officially released (tentative date January 2026).
```

**1. Download pyCSH.** Download the zip file from the [github repository](https://github.com/hegoimanzano/pyCSH/tree/v1.1). Click `Code` and then `Download .zip`. Unzip and enter the folder with your terminal or with VScode.

**2. Edit the `parameters.py`.**  Open `parameters.py` file in your text editor. You will have to change a few parameters to build your model according to the instructions above.

```{tip}
In Windows the default is _Notepad_, in Mac _TextEdit_ and in Linux _Nano_. They are enough, especially _Nano_, but if you are going to work on simulations, we recommend to use something more sophisticated such as _Vim_ or _Visual Studio_ despite the steeper learning curve.
```

The parameters that control the generated CSH models are defined in `parameters.py`, and are the following:

- `seed`: **Optional**. Default : 1123. 
   Seed for the random number generator.
   
- `size`: **Required**.
Size of the C–S–H model supercell in terms of bricks. Tuple of the shape (Nx, Ny, Nz). 

- `Ca_Si_ratio`: **Required**.
Target Ca/Si ratio of the CSH model.

- `W_Si_ratio`: **Required**.
Target water/Si ratio of the CSH model.

- `prefix`: **Optional**. Default: "input".
  Name of the output files. 
 
- `N_samples`: **Required**.
Number of structures to be generated.



- `make_independent`: **Optional**. Default: False.
 True implies that none of the structures are equal, or have a different spatial arrangement of the same unit cells.

- `offset_gaussian`: **Optional**. Default: False.
  If True, some preliminary calculations will be done in order to impose more strictly that the amount of Ca-OH and Si-OH are closer to the experimental values.

- `width_Ca_Si`: **Optional**. Default: 0.4.
Width of the gaussian used for sampling the Ca/Si ratio of each of the unit cells that compose the total supercell. Smaller values (e.g. 0.01) will  lead to ratios closer to the target, but the code might not be able to find a solution.

- `width_SiOH`: **Optional**. Default: 0.08.
Width of the gaussian used for sampling the Si-OH/Si ratio. Same as `width_Ca_Si`.

- `width_CaOH`: **Optional**. Default: 0.04.
Width of the gaussian used for sampling the Ca-OH/Ca ratio. Same as `width_Ca_Si`.



- `create`: **Required**.
True if you want to generate new structures, False, if other modes are required. See `check` and `read_structure`.

- `check`: **Optional**. Default: False.
If True, a preliminary check for a wide range of Ca/Si ratios will be performed, in order to show the accuracy of the generated models for the selected parameters with respect to the Ca/Si ratio, water/Si ratio etc.



- `orthogonal`: **Optional**. Default: True.
Whether your simulation box keeps the original trigonal shape or is converted to orthogonal (convenient for simulation purposes).

- `diferentiate`: **Optional**. Default: True.
Atoms are distinguished depending on their topological environment. If False, just the chemical symbol is included. If True, the different species are labelled.

- `Dpore`:  **Optional**. Default: 0.0.
The expansion of the desired pore in Å. A value of 0.0 indicates no pore opening. The pore is always created at the center of the supercell.

- `shift` = **Optional**. Default: False.
Shift the layers to ensure that the center of the supercell matches with the center of a pore. Basically, you need to shift your system if the number of blocks in z dimension is even, not shift if it is odd.



- `guest_ions` =  **Optional**. False.
Controls if guest ions are introduced in the model, substituting Ca. If True, the guest ions are controlled by the next line. If false, the next line is not read.

- `substitute` = np.array([["Ca1", "Zn", 5, 0.848],["Ca2", "Mn", 5, 0.848]], dtype = object).
An array that shows the substituted Ca, the substituting element, the %, and the charge assigned to the new element.

- `saturation` =  **Optional**. False.
Controls if the pore opened is saturated with water or not. If True, the amount of water is controlled by the next line. 

- `grid` = np.array([5, 5, 10, "Cl", 1, "Na", 1], dtype = object).
Water is introduced in a grid of positions. The first 3 numbers of the array determine how many water molecules are introduced in x y and z respectively. Then, the requested number of Cl and Na ions are introduced by replacing randomly water molecules in the grid.


 
- `write_lammps`: **Optional**. Default: True.
Write a `.data` LAMMPS data file for each of the structures. 

- `write_lammps_erica`: **Optional**. Default: False.
Write a `.data` LAMMPS data file for each of the structures, with core-shell, bonds and angle information to use with EricaFF. 

- `write_vasp`: **Optional**. Default: False.
Write a `.vasp` VASP data file for each of the structures.

- `write_siesta`: **Optional**. Default: False.
Write a `.siesta` SIESTA data file for each of the structures.



- `read_structure`: **Optional**. Default: False.
If True, handmade brick code will be used to create a model. The brick code should be placed at the end of the parameters file. This option is useful to reproduce models.




**3. Run pyCSH.** In a terminal inside the folder (or VScode) run simply:

```
python3 main_brick.py
```

That’s it! in a few seconds you will have your structures. The script will read your parameters.py, build the required C–S–H models, save structure files, and produce some plots.  

**4. What the outputs are and how to read them.**

pyCSH creates automatic plots with the characteristics of the **bulk** C–S–H. Note that the Ca/Si or w/Si ratio of the simulation box with the pore opened does not make sense. The generated plots are:

- **distributions.pdf**: The generated models have a slightly variable chemistry around the desired value. The distributions are shown in this file.
- **X-OH.pdf**: The ratio of Ca-OH/Ca and Si-OH/Si of the generated models as a function of the Ca/Si ratio, and  compared with the experimental data.
- **MCL.pdf**: The mean chain lengths of the generated models as a function of the Ca/Si ratio, and compared with the experimental data.
- **water.pdf**: The water content of the generated models, normalized by the silicate content, and compared with the experimental data.

pyCSH also generates an **output** folder where you will find several files (# denotes structure number):

- **prefix_#.log**: Files contain the information about the specific model (composition, size, etc), the "fingerprint" of the model (all the blocks used in the construction and their position in the supercell) and the charge distribution (not all the blocks are neutral, but the final structure is always neutral).
- **prefix_#.data/vasp/siesta...**: Files containing the atomic structure in the requested format.

Check the plots and files. Open the `.data` and visualize them with OVITO. Select one of the generated models to continue. Rename your particle types according to the pyCSH labels that appears in table below using the right panel in OVITO, change colors and sizes to improve visualization (typically smaller), and create bonds (`Add modification` menu). Export it from OVITO as `CSHmodel_filled.xyz` in xyz format. When exporting, include only the particle types and the atomic coordinates (x, y, z) so that the file can be read by VMD.


| Type | pyCSH Label | ClayFF Label | Mass (u) | Radius (Å) |
|------|-------------|--------------|----------|------------|
| 1    | Ca1         | cao          | 40.078   | 2.31       |
| 2    | Ca2         | cah          | 40.078   | 2.31       |
| 3    | Si1         | st           | 28.085   | 2.10       |
| 4    | Si2         | st           | 28.085   | 2.10       |
| 5    | Oca         | obos         | 15.999   | 1.52       |
| 6    | Osi         | ob           | 15.999   | 1.52       |
| 7    | O           | obos         | 15.999   | 1.52       |
| 8    | Ow          | o*           | 15.999   | 1.52       |
| 9    | Oh          | oh           | 15.999   | 1.52       |
| 10   | Hw          | h*           | 1.008    | 1.20       |
| 11   | H           | ho           | 1.008    | 1.20       |
| 12   | Cl          | Cl           | 35.450   | 1.75       |
| 13   | Na          | Na           | 22.990   | 2.27       |



```{Tip}
To avoid typing the same for each model you want to visualize, you can do it once and save `.OVITO` session states with all the parameters and modifications. Load the session state before a new model, and all the options will automatically load for the new atomic structures.
```

> ✏️ **Next step for Novice users** Move your model to the next page "topology".  

> ✒️ **Next step for Advanced users** Move to the next section "Packing molecular systems with Packmol".

---

### Packing molecules with Packmol (advanced users)

Packmol is a program designed to create initial configurations for molecular dynamics simulations by packing molecules into defined regions of space according to user-specified geometric constraints. It takes as input one or more molecular structures and places them inside a simulation box or around predefined surfaces, ensuring that the molecules do not overlap and that a minimum distance between atoms is respected.

pyCSH allows the insertion of water molecules and certain ions within the slit pore in very simple cases. Packmol offers much greater flexibility: it allows you to pack any kind of molecule, such as solvents, organic additives, surfactants, or any other chemical compound species, into complex geometries, interfaces, or pores. This makes it extremely useful when constructing more heterogeneous systems. 

**1. Installing Packmol.**

Packmol is available on Linux, macOS and Windows, and can be downloaded from its [official website](https://github.com/m3g/packmol/releases/tag/v21.1.1).

**2. Creating a Packmol input file.**

To build a system with Packmol, we first need to create a plain text file with the `.inp` extension (for example, `Packing.inp`). This file must contain all the instructions that indicate Packmol which molecules to include, how many copies of each, and where to place them in space. An example of a typical Packmol input file is shown below:

```
tolerance 2.0
filetype xyz
output CSHmodel_filled.xyz

structure name.xyz
number 1
center
fixed 10.0 10.0 10.0 0.0 0.0 0.0
end structure

structure Na.xyz
number 10
inside box 0.5 0.5 0.5 19.5 19.5 19.5
end structure

...
```

In this input file:
- **`tolerance`** defines the minimum allowed distance (in Å) between atoms belonging to different molecules to avoid overlaps.  
- **`filetype`** indicates the format of the output file, .pdb or .xyz.
- **`output`** is the name of the resulting packed system that will be created.  
- The **`structure ... end structure`** blocks define the molecules to be included and how they are positioned:
  - **`structure`** loads the atomic coordinates from the corresponding molecule/system file (`.xyz`).
  - **`number`** indicates how many molecules/systems will be inserted (for water you need to calculate this number to match the desired density, e.g. water = 1 g/cm³).
  Subsequent lines in the structure block define the region where the molecules will be packed, such as in a fixed position, inside/outside a box/cilinder/sphere, above/below planes, etc.
  - **`inside box`** defines a three-dimensional region inside which Packmol will randomly place the predefined number of molecules. The six numerical values correspond to the lower and upper limits of the box along the three Cartesian coordinates (x_min, y_min, z_min and x_max, y_max, z_max).
  - **`center`** tells Packmol to center the coordinates of that structure with respect to the defined box.
  - **`fixed`** indicates that the (center of the) structure should be placed exactly at the given coordinates (i.e., 10.0 10.0 10.0) and prevents it from moving during packing. The last three zeros correspond to allowed translation tolerances (here all set to zero, meaning the structure remains completely fixed). Note that to ensure that the structure is positioned right at the geometric center of the simulation cell, the specified coordinates here must be half of each box dimension. For example, if the box length is 20 Å in each direction, the center will be at (10.0, 10.0, 10.0).
 
 Note that you need to prepare your `Na.xyz`, `Cl.xyz` and `H2O.xyz` files independently in a text file with a xyz format:
 
```
<number of atoms>
comment line or blank 
<element> <X> <Y> <Z>
...
```
 
 
```{Warning}
When using periodic boundary conditions (PBC), atoms located exactly at the edges of the simulation box are periodically replicated on the opposite side. If Packmol places molecules too close to the box boundaries, this replication can cause overlaps between periodic images, leading to unrealistic atomic contacts or large forces during energy minimization. To prevent this, it is recommended to leave a small **safety margin** between the packing region and the box limits — typically 0.5 Å on each side. This ensures that no atom lies exactly on the boundary, avoiding artificial overlaps when the system is replicated under PBC and improving the stability of the subsequent molecular dynamics simulation.
```

**3. Running Packmol.**

Once the input file (for example `Packing.inp`) is ready and all the molecular structure files (`.pdb` files) are in the same directory, Packmol can be run directly from the terminal. To do so, navigate to the folder containing your input file and execute:

```
./packmol < Packing.inp
```

When using this command, Packmol reads all the packing instructions, loads the molecular coordinates from the `.xyz` files, and places N copies of each molecule inside the specified regions while ensuring that no overlaps occur according to the defined tolerance. During execution, Packmol prints progress information in the terminal (such as iteration steps and molecule placement). When it finishes, a new file (in this example `CSHmodel_filled.xyz`) will be created in the same directory. This file can be opened in VMD or another molecular visualization program to inspect the result before generating the corresponding LAMMPS data file.

```{Tip}
**Packing the pore region directly in LAMMPS**. The approach shown here uses Packmol to fill the pore of a C–S–H model with water and ions by explicitly packing them in the pore space. However, LAMMPS offers an interesting alternative for automation. It allows you to merge multiple systems by reading several `.data` files in sequence. This can be useful for constructing hybrid systems such as a C–S–H matrix with an empty pore, and a separate box containing pre-packed water and ions to fill the empty C–S–H pore. In this way, by keeping a single structural framework (for example, the same C–S–H slab) and replacing only the pore box `.data` file, a set of simulations with different compositions — varying water content, ion concentration, or even alternative pore chemistries — can be easily created without rebuilding the solid phase each time. The process is straightforward and implies loading one of the structures using `read_data CSH.data`, and adding the new atoms from the other data file without replacing the existing ones with `read_data Pore_box.data add append shift 0 0 0`. **`shift`** can be used to move the entire *pore_box* block into the desired region (for example, inside the pore). It is essential that both data files use the same `atom_style`, units, and consistent atom-type numbering. If the second data file defines overlapping atom types (same atom-type number), they should be renumbered to avoid conflicts.
```

