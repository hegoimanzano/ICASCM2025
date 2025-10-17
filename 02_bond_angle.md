# Topology

Explicación GENERAL de a qué se refiere topology - enlaces, angulos, atom, types, Force field. LAMMPS necesita esta info.

Lo vamos a hacer a partir de la estructura construida por pyCSH usando VMD (Visual Molecular Dynamics) is a molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3D graphics and built-in scripting. VMD is particularly useful for preparing input files for molecular dynamics simulations with software such as LAMMPS.

```{Note}
Hay otras opciones, más o menos complejas y flexibles. Incluso slef programing pythion + ASE
```

> ✏️ **Novel users** will have to  _Estimated time XXX min_.

> ✒️ **Advanced users** will have to  _Estimated time XXX min_.

### ClayFF atom types 



### Novel users: typing step by step 
**1. Loading the PDB file in VMD**
2.1. Open VMD:
Start the program.
2.2. Load the PDB file:
Go to File/New Molecule.
In the Molecule File Browser, click Browse, select your System.pdb file, and click Load.

**2. Using TopoTools to create a LAMMPS data file**
TopoTools is a VMD plugin that provides a set of commands for building and manipulating molecular structures and preparing them for molecular dynamics simulations.

Open the Tk Console:
Go to `Extensions/Tk Console`.

Load TopoTools and PBCtools:
In the Tk Console, load the packages with the following commands:

```
package require topotools
package require pbctools
```

package require topotools loads the TopoTools package, which is used for manipulating molecular topologies and preparing data files for LAMMPS.
package require pbctools loads the PBCtools package, which provides tools for handling periodic boundary conditions.

3.5. Define simulation box:
Set the periodic boundary conditions (PBC) for the simulation box:
pbc set {20.8 20.8 20.8 90.0 90.0 90.0}
pbc set {20.8 20.8 20.8 90.0 90.0 90.0} sets the periodic boundary conditions for the simulation box. The first three values are the box dimensions in the x, y, and z directions in Å, and the last three values are the angles between the box edges.

3.3. Generate bonds, angles, dihedrals, and impropers:

Use topo commands to guess the molecular topology mol bondsrecalc top recalculates the bonds for the top molecule to ensure that the bond information is correct. topo guessangles generates angle interactions in the molecular topology based on the bond structure.
topo guessdihedrals generates dihedral interactions (torsional angles) in the molecular topology.
topo guessimpropers generates improper dihedral interactions, which are often used to maintain planarity in certain molecular structures.

```
mol bondsrecalc top
topo guessangles
topo guessdihedrals
topo guessimpropers
```

3.4. Reanalyze the structure:
Recalculate the bonds and reanalyze the molecular structure to ensure everything is correctly set up:
```
mol reanalyze top
```

mol reanalyze top reanalyzes the top molecule, updating its molecular topology information.

3.6. Create the LAMMPS data file: Write the data to a LAMMPS-compatible file:
```
topo writelammpsdata atoms.data full
```
 writes the LAMMPS data (atoms.data) file in the full format, which includes detailed information about atom types, coordinates, bonding, angles, etc.

Esto te da el archivo listo para LAMMPS 

### Advanced users: script based construction

Te permite automatizar todo incluyendo hacer multiples cosntructions blabla bla. 
You need to write all the steps in a text file and execute from terminal parte dificil es saber navegar en tu arbold e archviso. 

```{Warning}
Hay otras opciones, más o menos complejas y flexibles. Incluso slef programing pythion + ASE
```
