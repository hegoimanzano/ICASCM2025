mol new 1.CSHmodel_filled.xyz type xyz

package require topotools
package require pbctools

pbc set {13.4704 12.419042 47.987367 90.0000 90.0000 90.0000} 
pbc box

mol bondsrecalc top
mol reanalyze top

set Ca1 [atomselect top "name Ca1"]
$Ca1 set element Ca
$Ca1 set mass 40.77999 
$Ca1 set charge 1.36
#$Ca1 set radius 1.3700000047683716
$Ca1 set radius 0.0

set Ca2 [atomselect top "name Ca2"]
$Ca2 set element Ca
$Ca2 set mass 40.078
$Ca2 set charge 1.05
#$Ca2 set radius 1.3700000047683716
$Ca2 set radius 0.0

set Si1 [atomselect top "name Si1"]
$Si1 set element Si
$Si1 set mass 28.085501
$Si1 set charge 2.1
#$Si1 set radius 2.0999999046325684
$Si1 set radius 0.0

set Si2 [atomselect top "name Si2"]
$Si2 set element Si
$Si2 set mass 28.085501
$Si2 set charge 2.1
#$Si2 set radius 2.0999999046325684
$Si2 set radius 0.0

set Oca [atomselect top "name Oca"]
$Oca set element O
$Oca set mass 15.999400
$Oca set charge -1.05
#$Oca set radius 1.5199999809265137
$Oca set radius 0.0

set Osi [atomselect top "name Osi"]
$Osi set element O
$Osi set mass 15.999400
$Osi set charge -1.1808
#$Osi set radius 1.5199999809265137
$Osi set radius 0.0

set O [atomselect top "name O"]
$O set element O
$O set mass 15.999400
$O set charge -1.1688
#$O set radius 1.5199999809265137
$O set radius 0.0

set Ow [atomselect top "name Ow"]
$Ow set element O
$Ow set mass 15.999400
#$Ow set radius 1.5199999809265137
$Ow set radius 1.0
$Ow set charge -0.82

set Oh [atomselect top "name Oh"]
$Oh set element O
$Oh set mass 15.999400
#$Oh set radius 1.5199999809265137
$Oh set radius 1.0
$Oh set charge -0.95

set Hw [atomselect top "name Hw"]
$Hw set element H
$Hw set mass 1.007940 
$Hw set radius 1.0
$Hw set charge 0.41

set H [atomselect top "name H"]
$H set element H
$H set mass 1.007940 
$H set radius 1.0
$H set charge 0.425

set Na [atomselect top "name Na"]
$Na set element Na
$Na set mass 22.990 
$Na set radius 0.0
$Na set charge 1.0

set Cl [atomselect top "name Cl"]
$Cl set element Cl
$Cl set mass 35.45000 
$Cl set radius 0.0
$Cl set charge -1.0

mol bondsrecalc top
topo retypebonds
topo guessangles
mol reanalyze top

topo writelammpsdata CSHmodel_final.data full
exit
