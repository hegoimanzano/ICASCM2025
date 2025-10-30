# Running the simulation

So far, we have created both the input and data file – all the necessary files are ready! We will use [Atomify](https://andeplane.github.io/atomify/), a web editor running LAMMPS that provides real-time visualization, access to real-time plotting of physical quantities and much more. 

After the simulation finishes, all output files are available in a Jupyter notebook that runs directly in the browser. With Atomify, we can run LAMMPS examples entirely online. It runs at roughly 50% of the speed of a natively compiled LAMMPS (single-threaded), so it is suitable for testing and teaching purposes, but not for production runs.

> **All users** will have to run their simulations. You can explore Atomify's options to see the real-time evolution of your simulation and try to understand and evaluate whether the behavior of the physical quantities is as expected.

The **left menu** controls the folders, files, and navigation through them. To run the simulation, just click on `New simulation`, give a **name** to your project, and drag and drop the input and data files. You are now ready to run your job.

```{Note}
**Your browser must remain in the foreground and your system awake.** Atomify runs LAMMPS through WebAssembly inside the browser, so the simulation only progresses while the tab is active and in the foreground. When the tab loses focus, most browsers throttle or pause background WebAssembly execution to save CPU resources. Your system must be awake, so you need to configure it accordingly. To do so, you can use apps like Caffeine (Windows) or Amphetamine (macOS), or native commands (check online for the option that suits you best). Simulations were tested using Google Chrome. 
```

**During the simulation**, you can explore the options in the right-hand menu, which displays all simulation parameters and output properties. You can change atom and bond sizes, and by clicking on the physical observables or defined variables, you will see plots of their evolution in real time. Hiding the menu reveals additional display controls, such as brightness.

**When the simulation finishes**, the `lammps.log file with the simulation output is generated. It contains the properties defined by the `thermo` command in the input file, as well as the simulation time and performance. By clicking on the `Analyze notebook` option, you can automatically plot these thermodynamic properties in Python. The `lammps.log` file and the trajectory file are located in a folder with the name you defined earlier. You have to download them for later post-processing analysis. 

The simulation will run for about 20–30 minutes depending on your computer's capabilities. You can check the performance – in our case: `Performance: 18.886 ns/day, 1.271 hours/ns, 218.582 timesteps/s`. If you experience memory issues or your browser freezes (which is quite common), you can reduce the simulation time by a factor of 10 to observe the process, and use the 200 ps results from [GitHub](https://github.com/hegoimanzano/ICASCM2025/tree/main/results) to continue the analysis.

```{Tip}
You can add Atomify commands, starting with #/, to your input file. These commands are **NOT** part of the LAMMPS input, they only work in this environment. They allow you to set atomic species and camera details.

For example, to move the camera to a better position, use:
   
   #/camera position 7.0 8.0 23.0
   #/camera target 7.0 8.0 23.0
   
 Atom sizes and colors can be set by assigning their element names:
   
   #/atom 1 calcium
   #/atom 2 calcium
   ...
```

