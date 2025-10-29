# Running the simulation

We have created an input file and a data file, all the necessary files are ready! We will use Atomify, [Atomify](https://andeplane.github.io/atomify/), a web editor running LAMMPS with real time visualization, access to real time plotting of physical quantities and much more. 
After a simulation is finished, all files are available in a jupyter notebook that also runs in the browser. With Atomify, we can run LAMMPS examples in the browser. It runs with about 50% of the speed of natively compiled LAMMPS (single threaded), so this is good for testing and teaching purposes, not for real production.

> **All users** will have to run their simulations. You can play with the Atomify options to see the real time evolution of your simulation and try to understand and evaluate if the evolution of the physical quantities is the expected one.

The **left menu** controls the folders, files, and the navigation thorugh them. To run the simulation, just click in `New simulation`, give a **name** to your project, and drag and drop the input anda data files.

**During the simulation** you can explore the options on the right menu, which shows all the simulation parameters and output properties. You can change atom and bond sizes, and cliking on the physical observables and defined variables you will see plots of their evolution in real time. Hidding the menu you will see aditional options to control for example the brightness.

**When the simulation finishes**, the lammps.log file with the simulation output pops out. There you have information about the properties defined by the `thermo` command in the input, as well as the simulation time and performance. By clicking on the `analyze notebook` option you will be able to plot automatically these thermodynamic properties in python. The lammps.log output file and the trajectory file are located in a folder with the **name** you used. You have to donwload them for a posteriory analysis. 

```{Tip}
You can add Atomify commands, starting with #/, to your input file. These commands are NOT part of the lammps input, only work in this environment. They allow you to set atomic species and camera details.

# Move camera to a nice position
#/camera position 7.0 8.0 23.0
#/camera target 7.0 8.0 23.0

# Set atom size and color
#/atom 1 calcium
#/atom 2 calcium
...
...
```

