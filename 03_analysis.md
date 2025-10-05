# Analyzing the simulation results

We will compute energy time series, Mean Square Displacement (MSD), RDF, and axial density profiles.

## MSD with MDAnalysis

```{code-block} python
# code/analysis_msd.py
import MDAnalysis as mda
from MDAnalysis.analysis import msd
import matplotlib.pyplot as plt

u = mda.Universe("csh_pore.data", "traj.lammpstrj")

# Example: select water oxygens (adjust to your topology)
sel = "resname H2O and name O"
waterO = u.select_atoms(sel)

msd_calc = msd.EinsteinMSD(waterO, select="name O", msd_type="xyz", fft=True)
msd_calc.run()

plt.figure()
plt.plot(msd_calc.times, msd_calc.results.msd)
plt.xlabel("time (ps)")
plt.ylabel("MSD (Å$^2$)")
plt.title("Water MSD (O atoms)")
plt.savefig("msd_water.png", dpi=200, bbox_inches="tight")
print("Saved msd_water.png")
```

## Density profiles (axial, along z)

```{code-block} python
# code/analysis_density.py
import numpy as np
import MDAnalysis as mda
import matplotlib.pyplot as plt

u = mda.Universe("csh_pore.data", "traj.lammpstrj")

# Binning along z axis
nbins = 100
zmin, zmax = 0.0, u.dimensions[2]
bins = np.linspace(zmin, zmax, nbins+1)
centers = 0.5*(bins[1:] + bins[:-1])

def density_profile(selection):
    atoms = u.select_atoms(selection)
    hist = np.zeros(nbins, dtype=float)
    frames = 0
    for ts in u.trajectory:
        z = atoms.positions[:, 2]
        h, _ = np.histogram(z, bins=bins)
        hist += h
        frames += 1
    # Convert counts to number density (per Å), normalize by cross-section area
    Lx, Ly, Lz = u.dimensions[:3]
    area = (Lx * Ly) if (Lx > 0 and Ly > 0) else 1.0
    rho = hist / (frames * area * (bins[1]-bins[0]))
    return centers, rho

for label, sel in [("H2O O", "resname H2O and name O"),
                   ("Na+", "name Na"),
                   ("Cl-", "name Cl")]:
    zc, rho = density_profile(sel)
    plt.plot(zc, rho, label=label)

plt.xlabel("z (Å)")
plt.ylabel("number density (1/Å^3)")
plt.legend()
plt.title("Axial density profiles")
plt.savefig("density_profiles.png", dpi=200, bbox_inches="tight")
print("Saved density_profiles.png")
```

## Exercises
- Compare MSD of water with and without NaCl.
- Compute RDF g(r) for water O–O and Na–Cl (hint: `MDAnalysis.analysis.rdf`).
- Quantify diffusion coefficient from long-time MSD slope:

  $$ D = \frac{1}{2d} \frac{d}{dt} \langle \Delta r^2(t) \rangle,\quad d=3.$$
