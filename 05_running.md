# Running the simulation

We have created an input file and a data file, all the necessary files are ready! We will use Atomify, [Atomify](https://andeplane.github.io/atomify/), a web editor running LAMMPS with real time visualization, access to real time plotting of physical quantities and much more. 
After a simulation is finished, all files are available in a jupyter notebook that also runs in the browser. With Atomify, we can run LAMMPS examples in the browser. It runs with about 50% of the speed of natively compiled LAMMPS (single threaded), so this is good for testing and teaching purposes, not for real production.

> **All users** will have to run their simulations. You can play with the Atomify options to see the real time evolution of your simulation and try to understand and evaluate if the evolution of the physical quantities is the expected one.

To run the simulation on Atomify, just go to the left menu, click in `New simulation`, give a **name** to your simulation and drag and drop the input anda data files. 
You can explore the options on the right menu, and cliking on the physical properties you will see plots of their evolution in real time. Hidding the menu you will see aditional options to control for example the brightness.

When the simulation finishes, the lammps.log file with the simulation output pops out. There you have information about the performance + oansfajdnsfa. By clicking on the `analyze notebook` option you will be able to plot automatically the thermodynamic parameters from the log file in python. This lammps.log output file plus the trajectory file are located in a folder with the **name** you used. You can donwload them for posteior analysis.


