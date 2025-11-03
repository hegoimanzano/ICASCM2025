# Results and Conclusions

### Interpretation of the Results

![system](/images/traj.png)

First, we visualy check the structure. This is the last snapshot of the simulation, with the box replicated for a better view. The C-S-H layers are preserved, the pore space has closed, and overall we can observe that the structure is physically sound

---

![equil](/images/equil.png)

Then we analyse several parameters to check convergency. The total energy decreases very fast after the initial relaxation of the atomic positions. It seems that the system has converged, but we recommend to zoom in to guarantee convergence. Same interpretation could be done with the pressure. Regarding lattice parameters, the **x** dimension presents a strong fluctuaction in the very beggining, but the system recovers the initial value after 20ps. The changes in the **z** dimension is much more pronounced as the pore decreases its size to equilibrate the water density inside the pore. 


---
The density profile of Cl ions and water in your system should look like this:

![MSD](/images/dprof.png)

The results for Cl computed from LAMMPS and TRAVIS are equal, with th only difference of the bin resolution, 0.5 in LAMMPS and $\aprox$ 0.13 in TRAVIS depending on your settings. The water dprof shows 2 peaks of well structured water close to the surfaces (more clear in the bottom) followed by "bulk"  water in the center of the pore. Cl ions are located preferentlially at the surfaces. In the botton surface, the structure is more clear, with Cl ion(s) in a fixed site just after the 2nd water layer. 

--- 

The MSD of Cl ions in the pore looks like this:

![MSD](/images/MSD.png)


In this case, the results from TRAVIS and LAMMPS **do not match perfectly**, just because the used algorithms are different. LAMMPS computes the MSD on-the-fly during the simulation with the displacement always measured with respect to the initial configuration:

$$
\mathrm{MSD}_{\text{LAMMPS}}(t) = \langle |\mathbf{r}_i(t) - \mathbf{r}_i(0)|^2 \rangle_i
$$

Only one time origin (t₀ = 0) is used, so no temporal averaging is performed. TRAVIS calculates the MSD in post-processing from the full trajectory, averaging over many time origins:

$$
\mathrm{MSD}_{\text{TRAVIS}}(\Delta t) = \langle |\mathbf{r}_i(t+\Delta t) - \mathbf{r}i(t)|^2 \rangle{i,t}
$$

The program uses all possible starting points times up to a defined correlation depth. This multi-time averaging provides smoother and **more statistically reliable results**. However, it requires saving and processing the full trajectory. Therefore, LAMMPS provides a quick estimate of diffusion and displacement behavior, while TRAVIS offers a more accurate and statistically averaged MSD, better suited for extracting reliable diffusion coefficients.


---

### Overall Conclusions of the Course

In this tutorial, we have shown the full workflow of atomistic simulation applied to cementitious materials: (i) building a structural model of C–S–H with a slit pore, (ii) preparing and running a molecular dynamics simulation with LAMMPS, and (iii) analysing the output to extract physically meaningful properties such as diffusion constants and density distributions.

It is important to stress, however, that the examples presented here are highly simplified. The simulation times are much shorter than those required to obtain converged transport properties, and the models do not yet account for the full structural complexity of real C–S–H. In a research-grade study, one would need to run trajectories that are hundreds of times longer, carefully test the force field, and validate the results against experimental data.

Despite these limitations, the course provides a paradigmatic case study that illustrates the power and limitations of molecular dynamics for cement science. Students leave the course with a clear view of how atomistic simulations are set up, run, and analysed, and what steps are necessary to transition from a didactic example to a robust scientific study.

---

### Future courses

The material from this course will remain permanently available. If you use it, you can cite it as (Zenodo)[^1]: My reference.. New material will be created for future ICASCM courses, tentatively 2027. In addition, the UPV/EHU will offer a 25-hours course on atomistic simulation of cementitious materials in October 2026. The course will be hybrid online and in person, with theory and hands on exercises. The sites are limited, you can send your expressions of interest by mail to [eduardo.duque@ehu.eus](eduardo.duque@ehu.eus).


[^1]: This tutorial was prepared by **Hegoi Manzano** and **Eduardo Duque-Redondo**. We thank Yerai Folio for the express development of the pyCSH version 2.0, and our beta-testers (Jon Otegi, Yerai Folio, Aden Rana, Batoul Assi, and Jontxu Gaitero). The work was supported by the “Departamento de Educación, Política Lingüística y Cultura del Gobierno Vasco” (Grant No.  IT1458-22), the Transnational Common Laboratory “Aquitaine-Euskadi Network in Green Concrete and Cement-based Materials” (LTC-Green Concrete), the European Union’s Horizon Europe research and innovation programme under the Marie Skłodowska-Curie grant agreement No 101119715 (CONTRABASS).


