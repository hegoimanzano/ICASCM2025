# Build a basic C–S–H model with pyCSH

The first step for a high quality simulation of C-S-H (and any other material) is to build an atomic scale model as realistic as possible. In other words, a model that comprises all the necessary features to represent the real conditions to reproduce the experimental physical properties. In our case, we will build a "slit-pore C-S-H model" to study NaCl diffusion in C-S-H nanopores.

The general procedure for building a slit pore in a calcium–silicate–hydrate (C–S–H) is:

- **Build the bulk structure**  A detailed description of the different model construction methods can be found in this [review article](https://doi.org/10.1016/j.cemconres.2022.106784). Here we will use the [pyCSH code](https://doi.org/10.1016/j.cemconres.2024.107593), a Python code for the automated generation of realistic bulk calcium silicate hydrate (C-S-H) structures.

- **Introduce the pore** (slit geometry) Choose a crystallographic direction perpendicular to the layers of interest. Define a “gap” by translating one part of the structure away from the other, thereby creating an empty region. The pore width can be tuned by setting the separation distance between the two C–S–H surfaces.

- **Saturate with water** Insert water molecules into the pore region using a packing algorithm. Reach realistic densities by filling until the desired target pore solution density is reached or by MD relaxation.

> ✏️ **Novel users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code. The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1.3, a C-S-H surface of least 2.25nm^2, and a pore space of aprox 2nm filled with water and 10NaCl ion pairs.

> ✒️ **Advanced users** will have to follow the the instructions to build 10 unique C-S-H models using the pyCSH code **_and packmol_**. The final models should be orthogonal, have a C/S ratio 1.4, a w/S ratio of 1.3, a C-S-H surface of least 2.25nm^2, and a pore space of aprox 2nm filled with water and 10NaCl ion pairs.

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

That’s it. The script will read you input.py, build the required C–S–H models, save structure files, and produce some plots.


**4. What the outputs are and how to read them**

Structure files:
- name.data — LAMMPS data file OVITO can open LAMMPS data directly.
- name.xyz — simple XYZ with all atoms. OVITO can open it directly. Good for quick previews.
- name.cif — CIF crystallographic file. VESTA can open it directly. Preferred for VESTA (periodic cell handled nicely).

Plots:
- MCL.pdf, Ca/Si

**Next step Novel users** Select one of the models and move to the topology section. By looking at the results elegir el mas representativo y comtinuar. 

**Advanced users** Select one of the models by looking at the results elegir el mas representativo. Still packmol setps


### Packmol (advanced users)

Packmol description y por que es util por meter cosas mas complicadas pyCSH solo agua e iones

EDU 

```{Warning}
boundary conditions dejar 0.5Å
```

```{tip}
Another option is to prepare 2 systems and use LAMMPS box blabla to merge different files
```
