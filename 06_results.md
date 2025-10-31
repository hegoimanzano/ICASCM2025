# Results and Conclusions

### Interpretation of the Results




---
The MSD of Cl ions in the pore looks like this:

![MSD](/images/dprof.png)

--- 

The MSD of Cl ions in the pore looks like this:

![MSD](/images/MSD.png)


In this case, the results from TRAVIS and LAMMPS do not match perfectly because the used algorithms are different. LAMMPS computes the MSD on-the-fly during the simulation with the displacement is always measured with respect to the initial configuration:

$$
\mathrm{MSD}_{\text{LAMMPS}}(t) = \langle |\mathbf{r}_i(t) - \mathbf{r}_i(0)|^2 \rangle_i
$$

Only one time origin (t₀ = 0) is used, so no temporal averaging is performed. TRAVIS calculates the MSD in post-processing from the full trajectory, averaging over many time origins:

$$
\mathrm{MSD}_{\text{TRAVIS}}(\Delta t) = \langle |\mathbf{r}_i(t+\Delta t) - \mathbf{r}i(t)|^2 \rangle{i,t}
$$

The program uses all possible starting points t, up to a defined correlation depth. This multi-time averaging provides smoother and more statistically reliable results. However, it requires saving and processing the full trajectory. Therefore, LAMMPS provides a quick estimate of diffusion and displacement behavior, while TRAVIS offers a more accurate and statistically averaged MSD, better suited for extracting reliable diffusion coefficients.


---

### Overall Conclusions of the Course

In this tutorial, we have shown the full workflow of atomistic simulation applied to cementitious materials: (i) building a structural model of C–S–H with a slit pore, (ii) preparing and running a molecular dynamics simulation with LAMMPS, and (iii) analysing the output to extract physically meaningful properties such as diffusion constants and density distributions.

It is important to stress, however, that the examples presented here are highly simplified. The simulation times are much shorter than those required to obtain converged transport properties, and the models do not yet account for the full structural complexity of real C–S–H. In a research-grade study, one would need to run trajectories that are hundreds of times longer, carefully test the force field, and validate the results against experimental data.

Despite these limitations, the course provides a paradigmatic case study that illustrates the power and limitations of molecular dynamics for cement science. Students leave the course with a clear view of how atomistic simulations are set up, run, and analysed, and what steps are necessary to transition from a didactic example to a robust scientific study.

---

### Future courses

The material from this course will remain permanently available. If you use it, you can cite it as (Zenodo). New material will be created for future ICASCM courses, tentatively 2027. In addition, the UPV/EHU will offer a 25-hours course on atomistic simulation of cementitious materials in October 2027. The course will be hybrid online and in person, with theory and hands on exercises. The sites are limited, you can send your expressions of interest by mail to [eduardo.duque@ehu.eus](eduardo.duque@ehu.eus).
