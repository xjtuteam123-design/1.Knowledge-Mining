# 1-s2.0-S092583882501758X-main

<!-- source: D:\总文献\1-s2.0-S092583882501758X-main.pdf -->
<!-- file_sha256: b07f1fa5516fcc1e040b6fa78db4b0d9295142996832ff7a4fdccb676a3415bb -->

## Page 1

Effects of Nb doping and crystal symmetry on the structural stability and 
mechanical properties at U-Nb twin boundaries
Xin Wen
a
, Congyi Li
b
, Tong Liu
a , *
a
School of Nuclear Science and Engineering, School of Mechanical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China
b
Global Institute of Future Technology, Shanghai Jiao Tong University, Shanghai 200240, China
ARTICLE INFO
Keywords:
First-principles
U-Nb alloy
Twin boundary energy
Strengthening/embrittlement
Ideal tensile strength
ABSTRACT
Uranium is commonly alloyed with transition metals such as Nb, Zr, and Mo to improve mechanical properties 
and corrosion resistance. Among them, U-Nb alloys possess a well-rounded combination of mechanical prop -
erties. The unique properties of U-Nb alloys are closely related to their metastable monoclinic phase structure 
and twin boundary (TB) mediated deformation mechanism. Recent low-temperature U-Nb aging experiments 
have revealed that significant changes in strength and ductility are induced by the perturbation of solute atoms 
and TB microstructure at extremely fine scales ( < 3 nm). These phenomena pose challenges for conventional 
experimental characterization methods, limiting a fundamental understanding of the correlation between 
atomic-scale microstructural evolution and the degradation of mechanical behavior in U-Nb alloys. This study 
employed first-principles density functional theory (DFT) calculations to systematically investigate the effects of 
Nb doping and crystal symmetry on structural stability and mechanical properties of U-Nb {130} TBs, including 
surface energy, twin boundary energy, segregation energy, strengthening/embrittling energy, maximum tensile 
strength, and elongation. The results show that the monoclinic α ’’ -U {130} twin structures exhibit enhanced 
structural stability along with a higher propensity of twin formation compared with the orthorhombic α -U {130} 
twin structures. Furthermore, the α ’’ -U {130} twin structures demonstrate a stronger tendency for atomic 
segregation that promotes TB strengthening, resulting in superior tensile strength and ductility. This study 
provides atomic-scale theoretical evidence to elucidate the intrinsic mechanism underlying twinning-modulated 
mechanical behavior in U-Nb alloys.
1. Introduction
Uranium (U) metal is widely used in the field of nuclear energy due 
to its unique physical and chemical properties [1,2] . Uranium has three 
different allotropes at specific temperatures and pressures: α , β , and γ 
phases. At high temperatures (774.8 – 1132.3 ℃ ), uranium is in the γ 
phase with a crystal structure of body-centered-cubic (bcc). During the 
cooling process, γ -U first transforms into the β phase (667.7 – 774.8 ℃ ) 
with a body-centered tetragonal crystal structure (bct), and then into the 
α phase (face-centered orthorhombic, < 667.7 ℃ ) [3,4] . The α -U phase is 
stable at room temperature, but it has several shortcomings such as low 
hardness, low yield strength, low ductility, and poor corrosion resis -
tance, which limit its safety margins in applications of reactor fuel or 
structural materials [5] . In order to improve the mechanical properties 
and corrosion resistance of α -U, U is usually alloyed with transition 
metals, such as Mo [4] , Ti [3] , Zr [6] , and Nb [7] . Among them, U-Nb 
alloys exhibit the most intriguing thermodynamic and mechanical 
behavior. The addition of Nb significantly alters the phase diagram of U, 
introducing metastable phases (orthorhombic α ’ : 0 – 4.2 wt% Nb; 
monoclinic α ’’ : 4.2 – 6.9 wt% Nb; tetragonal γ
◦
: 6.9 – 8.9 wt% Nb) with 
mechanical properties that differ drastically from the common equilib -
rium phases ( α and γ ) [8] . In particular, U-Nb alloys in the α ’’ phase 
exhibit dual-yielding deformation (DYD) behavior [9] and 
shape-memory effect (SME) [10] similar to Ti-Ni SMAs [11,12] , which is 
ascribed to the twinning-detwinning process controlled by the twin 
structure [13] . Consequently, gaining a comprehensive understanding 
of the structural characteristics and mechanical properties of U-Nb twins 
is of great significance to investigate the intrinsic mechanism of 
twin-controlled deformation behavior.
As revealed by multiple experimental studies, the unique mechanical 
behavior of α ’’ U-Nb alloys is predominantly controlled by their low- 
symmetry monolithic crystal structure and the interplay between Nb 
* Corresponding author.
E-mail address: tongliu@sjtu.edu.cn (T. Liu). 
Contents lists available at ScienceDirect
Journal of Alloys and Compounds
journal homepage: www.else vier.com/loc ate/jalcom
https://doi.org/10.1016/j.jallcom.2025.180200
Received 30 December 2024; Received in revised form 14 March 2025; Accepted 1 April 2025 
Journal of Alloys and Compounds 1025 (2025) 180200 
Available online 2 April 2025 
0925-8388/© 2025 Published by Elsevier B.V.

## Page 2

atoms and the TB. [7 – 9,14] . D.W. Brown et al. [7] reported that the 
recoverable deformation of α ’’ U-Nb alloy was caused by one or more 
equivalent martensitic variants of the parent phase through migration, 
growth, and reorientation of twin boundaries. R. D. Field et al. [15]
observed that the motion of { 172} twin dominated in the early stages of 
deformation. In the later stages of deformation within the U-Nb SME 
regime, there was a cooperative movement of { 130} and crossing { 172} 
twin boundaries, which may be the reason for the elimination of fine 
twins from the as-transformed structure. As mentioned above, the 
unique mechanical properties of U-Nb alloys are highly dependent on 
the concentration of Nb. For example, under long-term aging at inter -
mediate temperature, the ductile metastable α ’’ phase would decompose 
into a Nb-depleted α phase and a Nb-rich γ
2 
phase, resulting in 
tremendous loss of ductility [16] . Additionally, the spatial distribution 
of Nb atoms may also severely affect the mechanical properties of U-Nb 
alloys. Research conducted by the Los Alamos National Laboratory 
(LANL) [17,18] demonstrated that the long-term aging of U-Nb alloys at 
200 ℃ resulted in increased strength and hardness, accompanied by a 
significant loss of ductility (decreasing from a range of 30 % - 35 % to an 
extreme value of zero). Post-aging examinations revealed noticeable 
roughening of TBs, but could not distinguish a sign of phase decompo -
sition under high-resolution transmission electron microscopy (TEM). 
On the other hand, the statistical analysis of Nb mapping by atom probe 
tomography (APT) showed a subtle trend of less randomness in spatial 
distribution. The collective evidence from mechanical tests and micro -
structural characterizations during the 200 ˚ C U-Nb aging process sug -
gests that, although changes in Nb distribution and microstructure occur 
at an extremely fine scale (less than 3 nm) and with small amplitude 
[16] , these subtle changes may result in significant degradation of me -
chanical properties. Thus, elucidating the influence of Nb on the me -
chanical properties of TB in different crystal structures at nm- or even 
atomic-scale is of critical importance to reveal the degradation mecha -
nism of low-temperature aged U-Nb alloys [14,19] .
First-principles method is a powerful tool to investigate the me -
chanical properties of materials at extremely fine scales. Per S ¨oderlind 
et al. [20] calculated the lattice dynamics and mechanical properties of 
U and U-12.5 at% Nb alloys by using the all-electron full-potential linear 
muffin-tin orbitals (FPLMTO) method, it was found that compared to 
pure U metal, U-Nb alloy exhibited a general trend of elastic softening. 
Additionally, with the addition of Nb, the bulk modulus of the alloys 
remained nearly unchanged, while the shear modulus was noticeably 
smaller, indicating that the U-Nb alloy possessed greater ductility. The 
first-principles calculation results by Xin Wang et al. [10] indicated that 
the local atomic structure of Nb had a significant impact on the twin 
boundary energy, which was attributed to charge-depleted zones at Nb 
atoms and charge-rich zones around Nb atoms.
While current atomic simulation studies have reported valuable re -
sults on the structural [5,21] and mechanical properties of U-Nb alloys 
[20,22] , there is still a huge gap between the characteristics of Nb atoms 
and TBs and the mechanical behavior of U-Nb alloys. Particularly, the 
theoretical understanding of the influence of Nb microstructural 
perturbation on the mechanical behavior of U-Nb alloys is not yet fully 
established, despite evidence from LANL ’ s low-temperature aging 
studies [17,18] . In this work, the structural characteristics of TBs and the 
segregation behavior of Nb atoms at TBs [23 – 25] were systematically 
investigated through atomic-scale calculations, in order to establish a 
connection between the atomic structural characteristics and mechani -
cal behavior of U-Nb alloys. Twin boundary energy, segregation energy, 
strengthening/embrittling energy, uniaxial tensile stress-strain 
response, maximum tensile strength, and elongation of U-Nb alloys 
were calculated by using the first-principles method. The results of this 
study provide a theoretical foundation for comprehending the intrinsic 
mechanism of the mechanical behavior modulated by U-Nb TBs.
2. Computational methods and models
2.1. Theoretical method
The electronic structure, energy calculations, and first-principles 
uniaxial tensile tests of the U-Nb twin systems were calculated by the 
Vienna Ab initio Simulation Package (VASP) code [26] , a first-principles 
software based on density functional theory (DFT). The electron-ion 
interactions were treated with the projector augmented wave (PAW) 
[27] pseudopotential method. The exchange-correlation functional was 
described by the Perdew – Burke – Ernzerhof (PBE) version of the gener -
alized gradient approximation (GGA) [28] . Plane-wave cutoff energy 
was selected as 500 eV, and the Monkhorst-Pack [29] k-point sampling 
of 5 × 2 × 1 and 4 × 3 × 1 was used for α -U and α ’’ -U twin structure, 
respectively. Ground state energy minimization was performed until the 
electron self-consistency calculation reached to 1 × 10
 6 
eV and 
Hellmann-Feynman force on each atom was less than 0.02 eV /
˚
A. In the 
energy calculations, the geometric relaxation was performed using the 
conjugate gradient algorithm, and the Methfessel-Paxton method was 
used for the distribution function calculation in Brillouin zone integra -
tion. To calculate the density of states (DOS), the tetrahedral method 
with Bl ¨ochl correction [30] was selected to determine the electron 
orbital fraction occupation. The calculation results were post-processed 
by VESTA software [31] and VASPKIT [32] code. In addition, when 
spin-polarization was added to the U-Nb system, it was found that the 
magnetic moments of each atom were zero, so spin-polarization in the 
U-Nb system was not considered in this study. Finally, 5 f electrons in U 
can impose strong on-site Coulomb interaction [33] , and thus need to be 
properly treated in the calculation of electronic structure [34,35] . In this 
research, the effect of adding the Hubbard parameter U
eff 
value 
(1.24 eV) [36] on the crystal parameters of α -U and α ’’ -U bulk struc -
tures, as well as twin boundary energy and segregation energy of α ’’ -U 
twin structures were tested. It was found that the addition of the U
eff 
value increased the crystal parameters of α -U and α ’’ -U bulk structures 
compared to those without the U value [37,38] . Furthermore, the 
correction effect of a U
eff 
value had little influence on the segregation 
energy of α ’’ U-Nb, but the twin boundary energy of the α ’’ -U twin 
structure with a U
eff 
value increased by an order of magnitude. There -
fore, for this work on structural characteristics and mechanical prop -
erties of U-Nb twins, the DFT + U method was not used. These test results 
are consistent with the viewpoint of P. S ¨oderlind et al. [39,40] that 
DFT + U is closely related to oxides but not necessary for metals. Con -
ventional DFT methods can provide satisfactory descriptions of uranium 
ground state, equilibrium and structural properties, elastic constants, 
phonon spectra, various defects, and electronic structure.
The doping of Nb elements into the α ’’ -U crystal structure may be 
through substitutional doping or interstitial doping, which includes 
tetrahedral and octahedral interstitial doping [41] . The magnitude of 
defect formation energy directly indicates the difficulty of impurity 
doping. Therefore, the doping mode of Nb is determined by calculating 
the defect formation energy. The formation energy of one Nb atom 
substitutional defect E
S 
is defined as [42] : 
E
S
= E
( n 1 ) U + Nb
 
( n 1 )
n
E
nU
 E
Nb
(1) 
where E
(n-1)U + Nb 
is the total energy of ( n -1)U atoms and one Nb atom 
occupying the n lattice sites, E
nU 
is the total energy of a perfect α ’’ -U 
crystal structure, and E
Nb 
is the energy of one Nb atom. The formation 
energy of Nb atom interstitial defect E
I 
is defined as: 
E
I
= E
nU + Nb
 E
nU
 E
Nb
(2) 
where E
nU + Nb 
is the total energy of n U atoms occupying the n lattice sites 
and Nb atom in an interstitial site of the simulation structures.
Surface energy is the energy consumed to disrupt the chemical bonds 
between molecules when constructing the surface of a substance, which 
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
2

## Page 3

is the foundation for recognizing and understanding various surface 
phenomena [43] . The calculation formula for surface energy is as fol -
lows [44] : 
σ = σ
unrel
+ E
rel
= 1 / 2 A
 
E
surf
 n × E
bulk
)
+ 1 / A
 
E
slab rel
 E
surf
)
(3) 
where A is the area of the surface slab. E
rel 
is the relaxation energy, 
defined as the energy difference before and after the relaxation of the 
surface slab. E
bulk 
is the energy of a single atom in the bulk phase 
structure. n is the ratio of the number of atoms in the surface slab to the 
bulk structure.
Twin boundary energy (TBE) is an important indicator for measuring 
the stability and twinnability of twin structures [10,45] . The theoretical 
calculation formula for twin boundary energy in U twin structures is as 
follows [46] : 
ς
U U
=
E
U U
twin
 E
U U
bulk
2 A
(4) 
where E
U U
twin 
and E
U U
bulk
are the total energies of the twin and corre -
sponding bulk structures, respectively. A is the cross-sectional area of 
the twin structure. When the doped atom Nb is introduced into the U 
TBs, the twin boundary energy can be calculated as follows [47] : 
ς
U Nb
=
E
U Nb
twin
 E
U Nb
bulk
A
 ς
U U
(5) 
where E
U Nb
twin 
and E
U Nb
bulk
represent the total energies of the Nb-doped U TB 
and bulk structure, respectively.
Segregation energy (SE) is a characterization of the ability of doped 
Nb atoms to segregate to twin boundaries. The SE can be calculated as 
follows [48,49] : 
E
U Nb
SE
= ( E
U Nb
twin
 E
U U
twin
) ( E
U Nb
bulk
 E
U U
bulk
) (6) 
Among them, the number of atoms in the bulk structures corre -
sponding to E
U Nb
bulk 
and E
U U
bulk 
must be the same as the atomic number of 
the corresponding twin structures. A positive SE indicates the mutual 
attraction between doped atoms and matrix atoms, while a negative 
value means the opposite [50] . When E
U Nb
SE 
is less than zero, the doped 
Nb atoms tend to segregate towards the TBs of alloys, and vice versa. At 
the same time, E
U Nb
SE 
is also the segregation energy of doped atoms in the 
de-twinning structures.
Based on the Rice-Wang model, the strengthening and embrittling 
energy is used to measure the strengthening and embrittlement effect of 
doped atoms at TBs. The energy is defined as [23] : 
E
U Nb
R W
= ( E
U Nb
twin
 E
U U
twin
) ( E
U Nb
fs
 E
U U
fs
) (7) 
where E
U Nb
fs 
and E
U U
fs 
are the total energies of the free surfaces with and 
without doped Nb atoms. A negative value of E
U Nb
R W 
indicates TB cohe -
sion, and a positive value reflects embrittlement of the TB.
The strengthening and embrittling energy can be decomposed into 
three energy contributions, namely mechanical E
mech
, chemical E
chem
, 
and host removal energy E
rem
, which are attributed to the structural 
distortion due to the atomic volume misfit, the changes in charge dis -
tribution caused by the doped atoms, and the removal of the host atoms 
from the TB plane [51] . The TB energy, denoted as λ , is used to describe 
the three components of strengthening and embrittling energy, which is 
the energy required to divide a TB into two grains. It can be calculated as 
follows: 
λ = E
TB
 2 E
FS
(8) 
where E
TB 
and E
FS 
are the total energies of the TB and separated free 
surfaces, respectively. The formulas for these three components of E
U Nb
R W 
are expressed as follows: 
E
mech
= λ
vac
U Nb
 λ
vac
U
(9) 
where λ
vac
U Nb 
is the TB energy required to remove the doped Nb atoms 
from the TB plane in the Frozen
U-Nb + vac 
structure, and λ
vac
U 
represents the 
TB energy of the removal of a U atom from TBs of the Frozen
U + vac 
structure. 
E
chem
= λ
U Nb
 λ
vac
U Nb
(10) 
where λ
U Nb 
is the TB energy of Nb atoms doped at TB plane in the 
Relaxed
U-Nb 
structure. 
E
rem
= λ
vac
U
 λ
U
(11) 
where λ
U 
is the TB energy of the relaxed U twin structure.
Ideal strength is the stress required for a material to deform or 
fracture due to the elastic instability of its crystal lattice, which is the 
maximum stress that the material can withstand in an ideal state [52] . 
Ab initio calculations of ideal strength can reveal the charge transfer and 
bond breaking process of α -U and α ’’ -U, thereby elucidating the effects 
of Nb doping and crystal symmetry on the mechanical properties of 
U-Nb alloys. In this study, a two-dimensional tensile deformation model 
was constructed to analyze the stress-strain relationship and calculate 
ideal strength. Although this simplified model is insufficient to repro -
duce experimental data from tensile tests, it includes crystal structural 
symmetry, twin boundary orientation and solute doping, all of which are 
critical for understanding the Nb doping and crystal symmetry effects. 
The uniaxial tensile deformation of the α -U and α ’’ -U twin structures 
was calculated using the affine deformation of ADAIS [53] code, that is, 
all atomic layers of the twin structure were uniformly displaced along 
the tensile direction. Affine deformation is achieved by transforming the 
initial lattice vector matrix R
ini 
to a deformed lattice vector matrix R
def
: 
R
def
= R
ini
⋅ ( I + ε ) (12) 
where for two-dimensional materials, I represents a 2 × 2 identity ma -
trix, ε is the strain matrix, defined as: 
ε
2 D
=
[
ε
1
0
0 ε
2
]
(13) 
where ε
1 
= ε
xx 
and ε
2 
= ε
yy
. For the uniaxial tensile deformation of two- 
dimensional materials, ε
1 
= 0 and ε
2 
∕= 0.
2.2. Construction of atomic structures
For the orthorhombic α -phase U with space group of No.63 Cmcm, 
lattice constants are [54] : a = 2 . 836 Å, b = 5 . 867 Å, c = 4 . 936 Å. For the 
monoclinic α ’’ -phase U, according to the literature [10,14] , its space 
group type is determined as P12
1
1, and the initial lattice parameters are: 
a = 3 . 148 Å, b = 4 . 971 Å, c = 2 . 915 Å, and β = 114 . 4
∘
. Based on the α -U 
and α ’’ -U unit-cell structures, {130} twins of α -U and α ’’ -U with 46 U 
atoms and 44 U atoms were both constructed by building surface slabs, 
merging grains, and deleting atoms that were too close. Their crystal 
dimensions were 4.936 × 10.335 × 24.779 Å
3 
and 
5.830 × 9.934 × 21.970 Å
3 
with supercells of 1 × 2 × 1 and 2 × 1 × 1, 
respectively, as shown in Fig. 1 .
After establishing the twin structures, it was necessary to cyclically 
adjust the twin grains to obtain the twin structure with the minimum 
twin boundary energy. The specific method for cyclically adjusting twin 
structures was as follows: the grains on the left side of the twin boundary 
remained stationary, while the grains on the right side moved 0.2 Å in 
sequence along the twinning plane in the X direction, or Z direction, or 
both XZ directions. After the grain movement, the overlapping atoms 
need to be deleted. The criterion for identifying overlapping atoms was 
set at 0.3 lattice lengths. Finally, the left and right grains were not 
completely symmetrical. α -U and α ’’ -U twin structures after cyclic 
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
3

## Page 4

adjustment are shown in Fig. 1 (c) and (d), where site 1 to site 12 
represent the segregation sites of Nb atom on TBs. The testing and 
determination of twin structures is discussed in Section 3.1 .
3. Results
3.1. Twin boundary energy
The energetics of Nb atoms at different doping sites were first 
computed to determine the most suitable doping configuration for the 
surface structure. The atomic radius of Nb (1.34 Å) is close to that of U 
atom (1.38 Å). Therefore, there are three possible doping methods for 
incorporating Nb atoms into U supercell structures: Nb substitution, Nb 
interstitial at a tetrahedral site (T), and Nb interstitial at an octahedral 
site (O). Three types of defect formation energies are calculated for the 
monoclinic-U bulk structure with 8 atoms. Substitutional doping in -
volves randomly replacing one U atom in the bulk structure with one Nb 
atom. Both tetrahedral and octahedral interstitial sites are located at the 
center of the tetrahedron and octahedron. The calculation results indi -
cate that at 0 K and zero pressure, the energy of a Nb atom is 
 10.083 eV, the formation energy of Nb substitutional defect is 
0.908 eV, that of Nb tetrahedral interstitial defect is 2.275 eV, and that 
of Nb octahedral interstitial defect is 2.377 eV. The magnitude of defect 
formation energy indicates the difficulty and stability of impurity 
doping. The smaller the defect formation energy, the easier it is for the 
defect to form. Therefore, the doping method of Nb atoms in the 
monoclinic α ’’ U structure is chosen as substitutional doping, which is 
consistent with the results in the literature [41,42] .
Based on the stable doping configuration, surface energies for 
different surface structures are calculated and presented in Table 1 . For 
all these calculations, atomic configurations are surface slabs with 6 at. 
layers and 24 atoms. The shrinkage rates of α -U (130), α -U ( 130), α ’’ -U 
(130), and α ’’ -U ( 130) surface slabs are calculated by the change of 
atomic distance between the first and second layers as 11.069 %, 
11.024 %, 7.861 %, and 1.857 %, respectively. This indicates that dur -
ing the optimization process of these surface slabs, all surface atoms 
contract towards the bulk phase, thereby reducing the total energy of the 
system and increasing the stability of surface slabs. It can be seen from 
Table 1 that the surface energies of α -U (130) and α -U ( 130) are 1.6102 
and 1.6112 J • m
 2
, respectively, while the surface energies of α ’’ -U 
(130) and ( 130) slabs are 1.5696 J • m
 2
. The surface energy of α ’’ -U is 
lower than that of α -U, illustrating that the monoclinic α ’’ -U (130) 
surface is more stable than the orthorhombic α -U (130) surface. The 
surface energies of the seven low-index α -U surfaces calculated in the 
literature range from 1.756 to 2.151 J • m
 2 
[55] , which is in the same 
order of magnitude as the surface energy calculated in this study.
To obtain the optimal atomic configuration of twin boundary, the 
atomic positions were adjusted along the X-, Z-, and XZ-direction with 
respect to the TBs to search for the minimum twin boundary energy. The 
calculated TBEs of pure α -U and α ’’ -U at different translation directions 
and distances are illustrated in Fig. 2 . Considering thermodynamic 
favorability, among the 22 cyclically adjusted twin structures of the 
orthorhombic α -U phase, the range of TBEs is 0.544 – 2.202 J • m
 2
, and 
the twin structure with a simultaneous translation of 1.2 Å towards the 
XZ direction has the smallest TBE of 0.596 J • m
 2
. In the monoclinic 
α ’’ -U phase, a total of 43 cyclically adjusted twin structures are calcu -
lated for the TBEs, as shown in Fig. 2 (b), the range of TBEs is 
 0.509 – 0.760 J • m
 2
. Among the positive TBEs, the twin structure 
translated 0.4 Å along the X direction exhibits the smallest TBE, which is 
approximately 0.043 J • m
 2
.
Based on the pure α -U and α ’’ -U {130} twins after cyclic adjustment, 
the TBEs of doped Nb atoms in α -U and α ’’ -U twin structures are dis -
played in Fig. 3 . Doping Nb atom significantly increases the TBE by 
about an order of magnitude, and the TBE at each doping site is 
Fig. 1. Structural models of α -U and α ’’ -U {130} twins. (a) α -U {130} twinning plane and (b) α ’’ -U {130} twinning plane are constructed based on their respective 
unit-cells. The supercells of α -U {130} twin and α ’’ -U {130} twin are presented in (c) and (d), respectively, where site 1-site 12 indicate the segregation sites of Nb 
atom on TBs. The preferred sites of doped Nb atoms in U TBs are discussed in Section 3.2 .
Table 1 
Calculation results of surface energy for α -U and α ’’ -U surface slabs.
Surface 
slabs
Slab energy 
pre- 
relaxation 
(eV)
Slab energy 
post- 
relaxation 
(eV)
Relaxation 
energy (eV)
Surface 
area (Å
2
)
Surface 
energy 
(J • m
 2
)
α -U 
(130)
 252.2055 254.8940 2.6885 48.2210 1.6102
α -U 
( 130)
 252.2055 254.8938 2.6883 48.1944 1.6112
α ’’ -U 
(130)
 247.7358 252.1974 4.4616 54.2218 1.5696
α ’’ -U 
( 130)
 247.7357 252.1974 4.4617 54.2213 1.5696
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
4

## Page 5

different. For the doped α -U twin structure, the minimum TBE is at site 4, 
which is 3.561 J • m
 2
. For the doped α ’’ -U twin structure, the minimum 
TBE occurs at site 8, with a minimum value of 0.299 J • m
 2
. This in -
dicates that the most stable doping twin structure is replacing the U 
atom with the Nb atom at site 4 and site 8 of the α -U and α ’’ -U TBs, 
respectively. In addition, it can be seen from Fig. 2 and Fig. 3 that both 
pure α -U (0.596 J • m
 2
) and doped α -U (3.561 J • m
 2
) twin structures 
require higher TBEs compared to pure α ’’ -U (0.043 J • m
 2
) and doped 
α ’’ -U (0.299 J • m
 2
) twin structures, indicating that α ’’ -U-based {130} 
twins have higher structural stability than α -U-based {130} twin 
structures.
3.2. Segregation energy and strengthening/embrittling energy
The figures depicted in Fig. 4 illustrate the segregation energies of 
doped atom Nb at different sites of α -U and α ’’ -U {130} twin structures. 
The negative SE indicates that the doped Nb atom prefers to stay at the 
U-TBs, while the positive SE demonstrates that the Nb atom tends to stay 
inside grains [24] . As shown in Fig. 4 (a), for the α -U {130} twin struc -
ture, segregation energy E
U Nb
SE 
is positive for all segregation positions at 
the α -U TB, indicating that the Nb atoms are unstable in the TBs and 
prefer to stay inside the grain. For the doped α ’’ -U {130} twin structure, 
it can be seen from Fig. 4 (b) that E
U Nb
SE 
exhibits positive or negative 
values at different segregation sites, meaning that Nb atoms at α ’’ -U 
{130} TBs have both stable and unstable sites. Among these sites, the 
segregation of Nb atoms to site 8 has the lowest SE (-0.983 J • m
 2
) and a 
relatively stable doping TB structure. Consequently, the position of 
doped atoms and the atomic structure of substitution sites play a vital 
role in SE calculations.
According to the Rice-Wang model, the results of strengthening and 
embrittling energy of doped Nb atoms at favorable segregation positions 
in α -U and α ’’ -U TBs are presented in Table 2 . It can be seen that the 
segregation of Nb atoms at TBs has different effects on the α and α ’’ -U 
TBs. The E
U Nb
R W 
value of α -U is positive, meaning that the segregation of 
Nb atoms will lead to α -U TB embrittlement, while the strengthening and 
embrittling energy E
U Nb
R W 
of α ’’ -U is negative, indicating that the 
segregation of the doped Nb atoms to the α ’’ -U TBs has a strengthening 
effect on the TB cohesion.
As described in Section 2.1 , the strengthening and embrittling energy 
decomposes into three components, E
mech
, E
chem
, and E
rem
. Corre -
spondingly, the solute atomic segregation leads to different strength -
ening and embrittlement effects at TBs primarily due to the following 
mechanisms [24,56,57] : (i) the mechanical component caused by size 
effect is mainly due to the difference in atomic size between solute atoms 
and matrix atoms, which leads to atomic volume expansion (contrac -
tion) near TB and weakens (strengthens) the TB strength; (ii) the 
chemical component is essentially the electronic effect, that is, when an 
impurity atom substitutes a matrix atom, the original metallic bonds are 
replaced by stronger or weaker host-solute bonds; (iii) the removal of 
matrix atom is also actually due to the size effect – the atomic volume 
misfit caused by the removal of the matrix atom at the substitution 
position on the TB plane. The schematic diagram of the calculation 
process for three components in α ’’ -U is shown in Fig. 5 , and the 
Fig. 2. Calculated TBEs of the (a) α -U and (b) α ’’ -U {130} twins as a function of 
translation distance in different directions. A positive value of TBE is thermo -
dynamically favorable, while a negative value indicates that the twin structure 
is unstable. The gray pentagram represents the minimum value.
Fig. 3. Calculated TFEs of the (a) α -U-Nb and (b) α ’’ -U-Nb {130} twins at different segregation positions. The rectangle on each image represents the minimum value 
among all TBEs.
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
5

## Page 6

calculation process of α -U is the same as described above.
Fig. 6 illustrates the strengthening and embrittling energies and their 
three components of Nb segregation at α -U and α ’’ -U TBs. For the doped 
α -U twin structure, the values of mechanical and removal components 
are positive, weakening the TB cohesion. The chemical component is 
negative (-1.199 eV), indicating that the electronic effect enhances the 
TB cohesion. However, the strengthening effect of the chemical 
component is smaller than the total embrittlement effect caused by 
mechanical and removal components, resulting in a positive total 
strengthening and embrittling energy of α -U-Nb. This indicates that Nb 
segregation at the TB will lead to α -U TB embrittlement. For the doped 
α ’’ -U twin structure, the total strengthening and embrittling energy and 
Fig. 4. Calculated SEs of different segregation sites of Nb in the (a) α -U and (b) α ’’ -U {130} twins. The numbers in the figures represent the minimum segregation 
energy of the two twin structures.
Table 2 
Calculation results of strengthening and embrittling energy for dopant atom Nb 
at α -U and α ’’ -U TBs.
TB 
structures
E
U Nb
twin 
(eV) E
U U
twin 
(eV) E
U Nb
fs 
(eV) E
U U
fs 
(eV) E
U Nb
R W 
(eV)
α -U (130) 519.408 521.461 253.532 254.730 0.855
α ’’ -U 
(130)
 486.766 487.856 229.891 231.187 0.206
Fig. 5. Schematic diagram of three components calculation of strengthening/embrittling energy ( α ’’ -U as an example). The blue and yellow dashed circles in the 
Frozen
U + vac 
and Frozen
U-Nb + vac 
structures represent U vacancy and Nb vacancy, respectively.
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
6

## Page 7

the energies of three components are all negative, indicating that all 
three components contribute to enhancing the strength of α ’’ -U TB. 
Among them, the removal component contributes the most to the 
strengthening effect (-0.129 eV), followed by the chemical component 
(-0.077 eV), and the mechanical component contributes the least to TB 
strengthening (-0.007 eV). In general, the energy of the chemical 
component, i.e., the electronic effect, is negative in both α -U and α ’’ -U, 
leading to an enhancement of TB strength. However, mechanical and 
removal components, i.e., the size effect, exhibit different strengthening 
and embrittlement effects on α -U and α ’’ -U TB, indicating that crystal 
structures with different symmetries not only possess varying twin sta -
bilities but also affect the strength and cohesion of TB, thereby influ -
encing the mechanical properties of the alloy.
As mentioned above, U-Nb TBs have varying structural stability and 
segregation energies at different Nb doping sites, and the doped Nb 
atoms that segregate in α -U and α ’’ -U TBs exhibit distinct strengthening 
or embrittlement effects. In order to further characterize the correlation 
between electronic interactions and strengthening/embrittlement ef -
fects caused by Nb segregation, the electron localization function (ELF) 
was used to analyze the distribution of electron localization and electron 
bonding in U-Nb alloys [58,59] . The ELF distribution diagrams are 
shown in Fig. 7 . In α -U, the ELF value between the highly localized 
spherical U atoms is about 0.5 (green), indicating that adjacent atoms 
are bonded by metallic bonds. However, α ’’ -U exhibits more 
electron-delocalized regions (with low ELF) between adjacent U atoms, 
suggesting that the degree of bonding is lower than that in pure α -U. In 
the doped α -U structure, the effect of Nb atom on the ELF is localized, 
with only slight changes in the ELF near the doped atom. Adjacent U 
atoms are still bonded by metallic bonds, but the delocalization of 
electrons around Nb atom indicates that the U-Nb bond exhibits a 
certain degree of ionic character. In the doped α ’’ -U, the doping element 
Nb has a significant impact on the ELF. The electrons around the Nb 
atom still exhibit delocalization, but the ELF value between atoms in -
creases to about 0.4, indicating that doping Nb at a favorable segrega -
tion site in the α ’’ -U twin structure will increase the bonding ability to a 
certain extent.
3.3. First-principles calculational tensile tests
First-principles calculational tensile tests (FPCTT) was performed to 
investigate the effects of Nb doping and crystal symmetry on the ideal 
strength and stress-strain response of α -U and α ’’ -U TBs. Before con -
ducting uniaxial first-principles tensile tests on the twin structures, the 
uniaxial tensile stress-strain response of the α -U three-dimensional bulk 
phase was calculated to verify the accuracy of the computational 
method. The results indicate that the stress-strain curve is continuous in 
the [001] direction of the α -U bulk structure, with no abrupt changes in 
stress observed along this tensile direction. The calculated ideal tensile 
strength is 22.04 GPa, which is in good agreement with previously re -
ported values in the literature [5,60] . This indicates that the ADAIS code 
is suitable for tensile calculations within the U-system.
Fig. 8 displays the calculated energy-strain and stress-strain re -
lationships of the α -U, α -U-Nb, α ’’ -U, and α ’’ -U-Nb two-dimensional 
twin structures under uniaxial tensile loading. For pure α -U, as the 
strain continues to increase, the stress reaches its first maximum value of 
0.59 N/m at a strain of 1 % and then decreases to a first minimum stress 
of 0.25 N/m at 3 % strain. Subsequently, the stress increases to a second 
maximum of 0.88 N/m at a strain of 6 %, and then suddenly drops to 
0.23 N/m at 7 % strain. In the case of doped α -U, the maximum stress 
occurs at 8 % strain, which is later than the maximum stress observed in 
pure α -U. After a 10 % strain, the stress-strain curves for both α -U and 
α -U-Nb exhibit continuous fluctuations. For pure α ’’ -U, the change in 
crystal symmetry leads to a small residual compressive stress ( σ < 0) 
when the initial strain is applied, which is compensated by the tensile 
stress as tensile strain increases. The continuous increase in strain leads 
to increased stress until the first maximum of 21.18 N/m is reached at a 
strain point of 7 %. Beyond 8 % strain, the stress suddenly drops to the 
first stress minimum of 11.26 N/m. Although the stress has decreased, 
the total energy of the system continues to increase steadily, indicating 
that the material has not yet fractured and the system is evolving to a 
more unstable structure [61] . Afterward, the stress increases again to a 
second maximum value of 22.29 N/m at a strain of 18 %, before sud -
denly dropping to 0.07 N/m of compressive stress at a strain of 21 %. 
Fig. 6. Calculated strengthening and embrittling energies and the three com -
ponents of α U-Nb and α ’’ U-Nb twins. A negative value of E
U Nb
R W 
indicates TB 
cohesion, and a positive value reflects embrittlement of the TB.
Fig. 7. Calculated electron localization function distributions of α -U, α -U-Nb, α ’’ -U, and α ’’ -U-Nb, respectively. Range of ELF value is 0 ≤ ELF ≤ 1, where ELF = 1 
indicates complete localization of electrons, and ELF = 0 corresponds to delocalization of electrons. The maximum and minimum values of ELF are represented in red 
and blue, respectively, and their values are marked on the left side of each ELF diagram.
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
7

## Page 8

As shown in Fig. 8 (a), the maximum stress value and fracture point of 
α ’’ -U-Nb are delayed compared to pure α ’’ -U. The first maximum stress 
of 18.88 N/m occurs at a strain of 10 %, and the fracture point is reached 
at a strain of 22 % for α ’’ -U-Nb. So, the ideal tensile strengths of α -U, 
α -U-Nb, α ’’ -U, and α ’’ -U-Nb twin structures are 0.88 N/m, 0.86 N/m, 
22.29 N/m, and 18.88 N/m, respectively, with fracture points at strains 
of 6 %, 8 %, 21 %, and 22 %, respectively. It is worth noting that since 
the calculation is for uniaxial tensile of two-dimensional materials, the 
stress unit used here is force-per-length (N/m).
According to the report on the electronic structure evolution of α -U 
by J.W. Yang [60] , this study also investigated the electronic structure 
evolution of monoclinic α ’’ -U under different tensile strains through 
DOS calculations. Fig. 9 displays the electronic structure evolution of the 
total and partial DOS of pure and doped α ’’ -U under different tensile 
strains. If there are DOS peaks on both sides of the Fermi level (E
F 
= 0), 
and the DOS value between the two peaks is not zero, then the width 
between the two peaks is considered as a ‘‘pseudo-gap ’’ . The longer the 
‘‘pseudo-gap ’’ width, the higher the degree of bonding between atoms 
[60,61] . In Fig. 9 (a), the width of the ‘‘pseudo-gap ’’ is approximately 
0.42 eV without strain ( ε = 0). At larger strains ( ε = 0.08 and ε = 0.15), 
the ‘‘pseudo-gap ’’ becomes less pronounced, and its DOS value is also 
larger than that of the unstrained structure. At the fracture point ( ε =
0.21), the DOS near the Fermi level becomes more localized, and the 
‘‘pseudo-gap ’’ completely disappears, indicating that atomic bonding 
weakens with increasing tensile strain. This trend is also observed in 
doping α ’’ -U (see Fig. 9 (b)). As illustrated in Fig. 9 (c), the incorporation 
of Nb atoms results in a smoother peak spacing on both sides of the 
Fermi level, a reduction in DOS localization, and a more conspicuous 
‘‘pseudo-gap ’’ than that of pure α ’’ -U under larger strain ( ε = 0.15). This 
indicates that the slight orbital hybridization between the Nb-4d 
electrons and U-6d or 5 f states near the Fermi level enhances the 
interatomic bonding. In the partial DOS of U atom, the f-state DOS near 
the Fermi level is almost consistent with the total DOS curve, even under 
large strain (as shown in Fig. 9 (d)). This observation indicates that the 
evolution of the ‘‘pseudo-gap ’’ of U atoms under uniaxial tensile strain is 
mainly caused by the U-5f electrons, and the 5f-electrons charge evo -
lution plays a crucial role in the mechanical properties of uranium.
4. Discussions
Due to the low crystal symmetry of U and U-Nb alloys, their me -
chanical response exhibits significant anisotropy, and plastic deforma -
tion necessitates the simultaneous activation of multiple slip and 
twinning modes, resulting in complex deformation behavior [62,63] . 
Among these mechanisms, twinning is a crucial crystallographic feature 
that predominantly influences the plastic deformation of α -U. The lattice 
orientation of twinning has a significant impact on the evolution of 
crystal structure and strain-induced hardening [64] . Based on the DFT 
calculation results mentioned above, a detailed comparison and dis -
cussion were conducted regarding the effects of Nb doping and crystal 
symmetry on twinning properties, solute segregation, strength -
ening/embrittlement effect, and the uniaxial stress-strain response, in 
order to establish the correlation between twin microstructural char -
acteristics and the mechanical properties of U-Nb alloys.
Twin boundary is a particular type of symmetric tilt grain boundary 
(STGB) with a minimal atomic mismatch on the grain boundary plane, 
typically resulting in a very low grain boundary energy [65] . From 
Fig. 2 , it can be found that within the range of positive TBEs that satisfy 
thermodynamic stability, the relatively most stable twin structures of 
orthorhombic α -U and monoclinic α ’’ -U are translated by 1.2 Å in the XZ 
Fig. 8. FPCTT of the pure and doped α -U and α ’’ -U twin structures. (a) and (b) The stress-strain response and energy-strain curves of pure and doped α -U and α ’’ -U 
TB, respectively.
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
8

## Page 9

direction and 0.4 Å in the X direction, and their TBEs are 0.596 J • m
 2 
and 0.043 J • m
 2
, respectively. The calculated average TBE value, as 
reported by X. Wang, is 0.074 J • m
 2 
[10] , which is close to the calcu -
lated TBE value of α ’’ -U {130} twin in this study, but the calculated TBE 
value of α -U {130} twin is one order of magnitude larger than that of 
α ’’ -U. Similarly, the TBE of the doped α -U alloy (3.561 J • m
 2
) is much 
larger than that of the α ’’ U-Nb alloy (0.299 J • m
 2
). The formation 
propensity of TBs is highly related to stacking fault energy (SFE), and the 
lower the SFE, the higher the possibility of TB formation [66,67] . 
Because double TBE can be approximated as the SFE [68] , it is specu -
lated that the α ’’ -U {130} twin has a lower SFE, a higher density of TBs, 
and a higher possibility of hindering dislocation movement compared to 
the α -U {130} twin. This speculation is consistent with experimental 
results observed in face-centered cubic (FCC) [69] , HCP [70] , and 
high-entropy alloys (HEAs) [71] , which suggest that reducing the SFE 
can induce twinning, impede dislocation movement, and consequently 
improve the strength and ductility of these alloys.
Controlling segregation-induced grain boundary strengthening can 
effectively improve metal ductility, alleviate intergranular fracture, and 
reduce the GB migration rate. GB strengthening is closely related to GB 
structure to a large extent, such as grain boundary formation energy, 
atomic radius size, etc [24] . Calculation results in Section 3.2 show that 
U-Nb alloys have different segregation energies at distinct Nb doping 
positions on the TB, and the segregation energies also exhibit different 
changing trends in α -U and α ’’ -U. Numerous studies have reported that 
the solute atomic radius is closely related to the TBE, SE, and GB 
strengthening effect [23,24,50,72] . Since the atomic radius of Nb is 
close to that of U, it seems that the atomic radius effect is negligible in 
the case of U-Nb alloys. However, the nominal atomic radius does not 
consider the effect of local lattice distortion, which may alter the atomic 
radius in the vicinity of GB. Thus, the Voronoi volume of Nb at the TB is 
evaluated to investigate the effect of local lattice distortion on atomic 
size [73] . The results demonstrate that at the most favorable segregation 
site 8 of α ’’ -U, the atomic volume of Nb contracts from 21.1911 
˚
A
3 
to 
20.7642 
˚
A
3 
due to local lattice distortion. Recent studies showed that 
atomic size expansion/contraction due to local lattice distortion may 
reflect the solute segregation trend at GBs. For example, G. Bozzolo et al. 
[74] found that atomic size contraction may lead to enhanced Zr 
segregation at low Zr concentrations ( < 20 at%). This was because lower 
values of bulk lattice parameters may increase the 
Bozzolo-Ferrante-Smith (BFS) strain of Zr atoms, and the higher strain 
will drive the segregation of solute atoms to GB. This viewpoint can 
explain our calculated result of negative segregation energy and a 
contraction of Voronoi volume at the most favorable segregation site 8 
of α ’’ -U. It is worth noting that segregation behavior is highly dependent 
on crystal orientation, temperature (this DFT works at 0 K, Ref. [74] at 
Fig. 9. Evolution of the total DOS near the Fermi level with increasing tensile strain of (a) pure and (b) doped α ’’ -U. (c) The total DOS of pure and doped α ’’ -U at 
15 % tensile strain. The circular dashed line represents the position of the ‘‘pseudo-gap ’’ . (d) The partial DOS of pure α ’’ -U.
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
9

## Page 10

1000 – 1400 K), and doping concentration. These factors have not been 
considered in this DFT work and will be further studied in the future.
Grain boundary solute segregation contributes to grain refinement of 
strengthening phase and strengthens alloys by inhibiting the GB 
migration rate [75] . It can be seen from Section 3.2 that the Nb atom 
plays a role in embrittling TB in the α -U twin structure, while the 
segregation of Nb atom has a strengthening effect on α ’’ -U TB. This is 
consistent with the ELF diagram in Fig. 7 , which shows that Nb atom in 
α -U weakens the bonding ability of U-Nb bonds, leading to TB embrit -
tlement effect. In contrast, doping Nb atom in α ’’ -U will increase the 
bonding ability to a certain extent, thereby increasing the TB strength. 
Therefore, it can be considered that a doped site that is unfavorable for 
segregation cannot enhance the TB strength, while a doped site that is 
favorable for segregation can further enhance the TB cohesion. This 
observation is in great agreement with the Ref. [76] , which suggests that 
the segregation of Nb (or impurities) to existing TBs in U-14 at% Nb may 
serve as a potentially effective strengthening mechanism [18] . J.J. Kim 
et al. proposed that the instability of GB structure was alleviated when 
segregated atoms tended to move towards the free volume of GB caused 
by segregation [77] . This mechanism may be used to explain the phe -
nomenon that structural deformation caused by size-effect enhances the 
TB cohesion of α ’’ -U twin structure in this work. After structural relax -
ation, the distance between the solute atom and the TB atom decreases 
from 3.426 
˚
A to 2.949 
˚
A, indicating that the doped atom Nb tends to 
move towards the TB, thereby reducing the total energy of structure and 
increasing the stability of twin structure.
From the stress-strain curves in Fig. 9 (a), it can be seen that the 
elongation ratios and ideal tensile strengths for α -U, α -U-Nb, α ’’ -U, and 
α ’’ -U-Nb alloys are 6 %, 8 %, 21 %, and 22 %, as well as 0.88 N/m, 
0.86 N/m, 22.29 N/m, and 18.88 N/m, respectively. Given that the 
elongation ratio directly reflects ductility [23] , it can be concluded that 
Nb doping improves the ductility of U-TBs without significantly sacri -
ficing tensile strength. Moreover, the monoclinic α ’’ -U twin structure 
exhibits superior ductility and tensile strength compared to the ortho -
rhombic α -U. This calculation result is consistent with the literature 
report that the elongation of α -U is less than 10 % at room temperature 
[78] , and U-alloy compounds exhibit high ductility [20,79] . It is 
generally accepted that strength and ductility are two opposing material 
properties, and increasing the ultimate tensile strength of a material 
tends to reduce its ductility [80] . This work demonstrates that mono -
clinic α ’’ -U has higher tensile strength and ductility than orthorhombic 
α -U. Additionally, doping Nb in the same crystal structure can improve 
the ductility of alloys without significantly sacrificing tensile strength. It 
is worth noting that the tensile test conducted here is based on a 
defect-free supercell model [81] , while the tensile behavior of actual 
engineering materials is inevitably influenced by various defects, such as 
dislocations and cracks [82] . Therefore, the stress-strain response ob -
tained through FPCTT was used for a qualitative comparison of me -
chanical properties of α -U and α ’’ -U under the influence of TB and Nb.
Currently, due to the difficulty in experimentally characterizing U- 
Nb alloys, research on the correlation between the chemical redistri -
bution of Nb elements and their mechanical properties is quite limited. 
In Ti-Nb shape memory alloys, researchers have found that under stress 
induction, the austenite region (Nb-rich region) with a B2 ordered 
structure transforms into α ’’ martensite, while the Nb-depleted region, 
characterized by a BCC disordered structure, transforms into δ 
martensite. The stress-induced martensitic transformation in two re -
gions occurs at different critical stresses [83] . Moreover, the reports 
confirm that parameters such as Young ’ s modulus, transformation 
strain, shear value, and shuffle value of Ti-Nb alloys are 
concentration-dependent [84,85] . Therefore, in U-Nb alloys, the atomic 
arrangement after Nb redistribution and the concentration of Nb may 
also affect the stress-strain response [12] and alter the DYD behavior of 
the alloys. In future research, the effect of Nb atomic redistribution at 
different temperatures on the stress-strain response will be considered, 
and the DYD behavior of the alloys will be modulated by adjusting the 
arrangement of Nb atoms.
5. Conclusions
In summary, the effects of Nb doping and crystal symmetry on 
structural stability and mechanical properties of U-Nb twin structures 
were systematically investigated by DFT computations in this paper. The 
atomic scale calculation results indicate that the α ’’ -U {130} twin 
structures exhibit greater structural stability, a higher possibility of twin 
formation, stronger atomic segregation tendency, and enhanced tensile 
strength and ductility compared to the α -U {130} twin structures. 
Furthermore, the strengthening and embrittlement effect induced by 
solute atom segregation is highly dependent on the twin crystal structure 
and segregation sites. The contraction of Voronoi volume at the most 
favorable segregation site in α ’’ -U leads to an increase in BFS strain, 
further promoting the segregation of solute atoms toward the TB. The 
segregated atom Nb enhances the strength of α ’’ U-TB by alleviating the 
structural instability of the twin structure and increasing the U-Nb 
bonding ability, which is mediated by the weak orbital hybridization 
between Nb-4d and U-6d or 5 f electrons. Based on the above calculation 
conclusions, we believe that the segregation-induced TB strengthening 
mechanism may explain the improvement in the mechanical properties 
of α ’’ U-Nb alloys. These findings provide valuable insights into the 
microscopic characteristics and mechanical properties of low-symmetry 
U-Nb alloys at the atomic level, compensating for the limitations of 
experimental characterization techniques. To obtain a comprehensive 
understanding of the mechanical properties and deformation mecha -
nisms of U-Nb alloys, further studies will focus on the effects of Nb 
concentration and distribution on ideal tensile strength, shear strength, 
generalized stacking fault energy, and TB migration rate at different 
temperatures, in order to explore the more complex mechanical 
behavior of three-dimensional U-Nb twin structures.
CRediT authorship contribution statement
Wen Xin: Writing – original draft, Visualization, Software, Meth -
odology, Investigation, Data curation. Li Congyi: Writing – review & 
editing, Validation, Supervision, Methodology. Liu Tong: Writing – re -
view & editing, Supervision, Resources, Methodology, Funding 
acquisition.
Declaration of Competing Interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
The authors are grateful for the support provided by the Nuclear 
Technology Research and Development Project of China Atomic Energy 
Authority (HNKF202314(48)) and the LingChuang Research Project of 
China National Nuclear Corporation (CNNC-LCKY-202242).
References
[1] W.J. Carmack, D.L. Porter, Y.I. Chang, S.L. Hayes, M.K. Meyer, D.E. Burkes, C. 
B. Lee, T. Mizuno, F. Delage, J. Somers, Metallic fuels for advanced reactors, 
J. Nucl. Mater. 392 (2009) 139 – 150 .
[2] Z.Y. Ren, J. Wu, R. Ma, G.C. Hu, C. Luo, Thermodynamic properties of α -uranium, 
J. Nucl. Mater. 480 (2016) 80 – 87 .
[3] J.B. Qi, G.X. Wu, J.Y. Zhang, Mechanical properties of U-0.95 mass fraction of Ti 
alloy quenching and aging treatment: a first principles study, Adv. Manuf. 3 (2015) 
244 – 251 .
[4] B.Q. Liu, X.X. Duan, G.A. Sun, J.W. Yang, T. Gao, Structural instabilities and 
mechanical properties of U2Mo from first principles calculations, Phys. Chem. 
Chem. Phys. 17 (2015) 4089 .
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
10

## Page 11

[5] N.Y. Bao, Q.C. Tong, F.Y. Guo, S. Zhang, D.D. Kang, A. Akinpelu, J. Lv, Y.S. Yao, J. 
Y. Dai, Structures and properties of uranium – niobium intermetallic compounds 
under high pressure: a first principles study, J. Appl. Phys. 133 (2023) 095901 .
[6] J.J. Ma, X.F. Han, X.X. Cai, R.Z. Qiu, O. Eriksson, P. Zhang, B.T. Wang, High- 
temperature mechanical and dynamical properties of γ -(U,Zr) alloys, Materials 16 
(2023) 2623 .
[7] D.W. Brown, M.A.M. Bourke, P.S. Dunn, R.D. Field, M.G. Stout, D.J. Thoma, 
Uniaxial tensile deformation of uranium 6 wt Pct niobium: a neutron diffraction 
study of deformation twinning, Metall. Mater. Trans. A 32 (2001) 2219 – 2228 .
[8] D.W. Brown, M.A.M. Bourke, R.D. Field, W.L. Hults, D.F. Teter, D.J. Thoma, S. 
C. Vogel, Neutron diffraction study of the deformation mechanisms of the 
uranium – 7 wt% niobium shape memory alloy, Mater. Sci. Eng. A 421 (2006) 
15 – 21 .
[9] C.S. Zhang, H. Wang, J. Li, B.B. Pang, Y.H. Xia, Y.G. Liu, G.A. Sun, X.J. Zhang, 
T. Fa, X.L. Wang, The aging-effect-modulated mechanical behavior in U-Nb shape 
memory alloys through the modified twinning-detwinning process of the α ’’ phase, 
Mater. Des. 162 (2019) 94 – 105 .
[10] X. Wang, W.Y. Wang, C. Lu, Y.W. Zhao, R.Z. Qiu, T. Shi, P. Zhou, H. Huang, T. Fa, 
Interface structure of (130) twin in the U-14.0 at% Nb alloy: an experimental and 
theoretical study, Scri. Mater. 209 (2022) 114417 .
[11] A.P. Stebner, S.C. Vogel, R.D. Noebe, T.A. Sisneros, B. Clausen, D.W. Brown, 
A. Garg, L.C. Brinson, Micromechanical quantification of elastic, twinning, and slip 
strain partitioning exhibited by polycrystalline, monoclinic nickel – titanium during 
large uniaxial deformations measured via in-situ neutron diffraction, J. Mech. 
Phys. Solids 61 (2013) 2302 – 2330 .
[12] C.S. Zhang, L. Xie, Z.J. Fan, H. Wang, X.P. Chen, J. Li, G.A. Sun, Straightforward 
understanding of the structures of metastable α ’’ and possible ordered phases in 
uraniumeniobium alloys from crystallographic simulation, J. Alloy. Compd. 648 
(2015) 389 – 396 .
[13] C.N. Tupper, D.W. Brown, R.D. Field, T.A. Sisneros, B. Clausen, Large strain 
deformation in uranium 6 wt Pct niobium, Metall. Mater. Trans. A 43 (2012) 
520 – 530 .
[14] Y.Z. Zhang, X.L. Wang, Q.Y. Xu, Y.F. Li, X-ray diffraction study of low temperature 
aging in U – 5.8 wt%Nb, J. Nucl. Mater. 456 (2015) 41 – 45 .
[15] R.D. Field, D.J. Thoma, P.S. Dunn, D.W. Brown, C.M. Cady, Martensitic structures 
and deformation twinning in the U – Nb shape-memory alloys, Philos. Mag. A 81 
(2001) 1691 – 1724 .
[16] R.E. Hackenberg, D.W. Brown, A.J. Clarke, L.B. Dauelsberg, R.D. Field, W.L. Hults, 
A.M. Kelly, M.F. Lopez, D.F. Teter, D.J. Thoma, T.J. Tucker, C.J. Vigil, H.M. Volz, 
U-Nb aging final report, Report LA-14327, Los Alamos National Laboratory, Los 
Alamos, NM, 2007.
[17] D.W. Brown, M.A.M. Bourke, A.J. Clarke, R.D. Field, R.E. Hackenberg, W.L. Hults, 
D.J. Thoma, The effect of low-temperature aging on the microstructure and 
deformation of uranium- 6 wt% niobium: an in-situ neutron diffraction study, 
J. Nucl. Mater. 481 (2016) 164 – 175 .
[18] A.J. Clarke, R.D. Field, R.E. Hackenberg, D.J. Thoma, D.W. Brown, D.F. Teter, M. 
K. Miller, K.F. Russell, D.V. Edmonds, G. Beverini, Low temperature age hardening 
in U – 13 at% Nb: an assessment of chemical redistribution mechanisms, J. Nucl. 
Mater. 393 (2009) 282 – 291 .
[19] H.M. Volz, R.E. Hackenberg, A.M. Kelly, W.L. Hults, A.C. Lawson, R.D. Field, D. 
F. Teter, D.J. Thoma, X-ray diffraction analyses of aged U – Nb alloys, J. Alloy. 
Compd. 444 – 445 (2007) 217 – 225 .
[20] P. S ¨oderlind, L.H. Yang, A. Landa, A. Wu, Mechanical and thermal properties for 
uranium and U – 6Nb alloy from first-principles theory, Appl. Sci. 11 (2021) 5643 .
[21] X.L. Pan, H. Wang, L.L. Zhang, Y.F. Wang, X.R. Chen, H.Y. Geng, Y. Chen, 
Prediction of novel final phases in aged uranium-niobium alloys, J. Nucl. Mater. 
579 (2023) 154394 .
[22] Z.Y. Shen, Y. Kong, Y. Du, S.Y. Zhang, Effect of alloying on stability of grain 
boundary in γ phase of the U – Mo and U – Nb systems, Calphad 72 (2021) 102241 .
[23] J. Hui, X.Y. Zhang, T. Liu, W.G. Liu, B. Wang, First-principles calculation of twin 
boundary energy and strength/embrittlement in hexagonal close-packed titanium, 
Mater. Des. 213 (2022) 110331 .
[24] X.B. Wu, Y.W. You, X.S. Kong, J.L. Chen, G.N. Luo, G.H. Lu, C.S. Liu, Z.G. Wang, 
First-principles determination of grain boundary strengthening in tungsten: 
dependence on grain boundary structure and metallic radius of solute, Acta Mater. 
120 (2016) 315 – 326 .
[25] A. Kumar, J. Wang, C.N. Tome, First-principles study of energy and atomic 
solubility of twinning-associated boundaries in hexagonal metals, Acta Mater. 85 
(2015) 144 – 154 .
[26] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy 
calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169 – 11186 .
[27] P.E. Blo ¨ chl, Projector augmented-wave method, Phys. Rev. B Condens. Matter 
Mater. Phys. 50 (1994) 17953 – 17979 .
[28] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made 
simple, Phys. Rev. Lett. 77 (1996) 3865 – 3868 .
[29] H.J. Monkhorst, J.D. Pack, Special points for Brillonin-zone integrations, Phys. 
Rev. B 13 (1976) 5188 – 5192 .
[30] P.E. Bl ¨ochl, O. Jepsen, O.K. Andersen, Improved tetrahedron method far Brillouin- 
zone integrations, Phys. Rev. B 49 (1994) 16223 .
[31] K. Momma, F. Izumi, VESTA3 for three-dimensional visualization of crystal, 
volumetric and morphology data, J. Appl. Cryst. 44 (2011) 1272 – 1276 .
[32] V. Wang, N. Xu, J.C. Liu, T. G, W.T. Geng, VASPKIT: A user-friendly interface 
facilitating high-throughput computing and analysis using VASP code, Comput. 
Phys. Commun. 267 (2021) 108033 .
[33] P.P. Dholabhai, On the behavior of 5f electrons, Univ. Tex. Arlingt. ProQuest Diss. 
Theses (2005) 1428130 .
[34] S. Fujimori, M. Kobata, Y. Takeda, T. Okane, Y. Saitoh, A. Fujimori, H. Yamagami, 
Y. Haga, E. Yamamoto, Y. Onuki, Manifestation of electron correlation effect in 5f 
states of uranium compounds revealed by 4d-5f resonant photoelectron 
spectroscopy, Phys. Rev. B 99 (2019) 035109 .
[35] A.N. Chantis, R.C. Albers, M.D. Jones, Mark van Schilfgaarde, T. Kotani, Many- 
body electronic structure of metallic α -uranium, Phys. Rev. B 78 (2008) 081101 .
[36] W. Xie, W. Xiong, C.A. Marianetti, D. Morgan, Correlation and relativistic effects in 
U metal and U-Zr alloy: validation of ab initio approaches, Phys. Rev. B 88 (2013) 
235128 .
[37] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, First principles calculations of the 
structure and elastic constants of α , β and γ uranium, J. Nucl. Mater. 433 (2013) 
143 – 151 .
[38] C.D. Taylor, Evaluation of first-principles techniques for obtaining materials 
parameters of α -uranium and the (001) α -uranium surface, Phys. Rev. B 77 (2008) 
094119 .
[39] P. S ¨oderlind, B. Sadigh, V. Lordi, A. Landa, P.E.A. Turchi, Electron correlation and 
relativity of the 5f electrons in the U – Zr alloy system, J. Nucl. Mater. 444 (2014) 
356 – 358 .
[40] P. S ¨oderlind, A. Landa, P.E.A. Turchi, Comment on “ Correlation and relativistic 
effects in U metal and U-Zr alloy: validation of ab initio approaches ” , Phys. Rev. B 
90 (2014) 157101 .
[41] S.K. Xiang, H.C. Huang, L.M. Hsiung, Quantum mechanical calculations of uranium 
phases and niobium defects in γ -uranium, J. Nucl. Mater. 375 (2008) 113 – 119 .
[42] J.T. Wang, W.L. Yu, T. Wang, Y.L. Wang, Y.L. Gao, First-principles study on the 
thermodynamic defect and crystal structure of U-12.5 at% Nb alloy, Int. J. Heat. 
Tech. 33 (2015) 175 – 180 .
[43] R. Tran, Z.H. Xu, B. Radhakrishnan, D. Winston, W.H. Sun, K.A. Persson, S.P. Ong, 
Surface energies of elemental crystals, Sci. Data 3 (2016) 160080 .
[44] Q. Li, M.R. Pi ˜neiro, N.A. Barrios, M.G. Rat ´es, I.N. Remediakis, N. L ´opez, Shape 
control in concave metal nanoparticles by etching, Nanoscale 9 (2017) 
13089 – 13094 .
[45] C. Wang, H.Y. Wang, T.L. Huang, X.N. Xue, F. Qiu, Q.C. Jiang, Generalized- 
stacking-fault energy and twin-boundary energy of hexagonal close-packed Au: a 
first-principles calculation, Sci. Rep. 5 (2015) 10213 .
[46] Y. Wang, L.Q. Chen, Z.K. Liu, S.N. Mathaudhu, First-principles calculations of twin- 
boundary and stacking-fault energies in magnesium, Scr. Mater. 62 (2010) 
646 – 649 .
[47] J. Hui, W.G. Liu, B. Wang, Theoretical study of the effects of alloying elements on 
Cu nanotwins, Sci. China-Phys. Mech. Astron 63 (2020) 104612 .
[48] Z.R. Pei, R. Li, J.F. Nie, J.R. Morris, First-principles study of the solute segregation 
in twin boundaries in Mg and possible descriptors for mechanical properties, 
Mater. Des. 165 (2019) 107574 .
[49] R. Tran, Z.H. Xu, N.X. Zhou, B. Radhakrishnan, J. Luo, S.P. Ong, Computational 
study of metallic dopant segregation and embrittlement at molybdenum grain 
boundaries, Acta Mater. 117 (2016) 91 – 99 .
[50] J. Hui, X.Y. Zhang, G. Yang, T. Liu, W.G. Liu, First-principles study of de-twinning 
in a FCC alloy, J. Solid State Chem. 293 (2021) 121765 .
[51] M. V ˇsiansk ´a, M. 
ˇ
Sob, The effect of segregated sp-impurities on grain-boundary and 
surface structure, magnetism and embrittlement in nickel, Prog. Mater. Sci. 56 
(2011) 817 – 840 .
[52] D.M. Clatterbuck, D.C. Chrzan, J.W. Morris Jr, The ideal strength of iron in tension 
and shear, Acta Mater. 51 (2003) 2271 – 2283 .
[53] S.H. Zhang, Z.H. Fu, R.F. Zhang, ADAIS: Automatic derivation of anisotropic ideal 
strength via high-throughput first-principles computations, Comput. Phys. 
Commun. 238 (2019) 244 – 253 .
[54] C.S. Barrett, M.H. Mueller, R.L. Hitterman, Crystal structure variations in alpha 
uranium at low temperatures, Phys. Rev. 129 (1963) 625 .
[55] S.Q.S. Huang, X.H. Ju, First-principles study of properties of alpha uranium crystal 
and seven alpha uranium surfaces, J. Chem. (2017) 8618340 .
[56] A.Y. Lozovoi, A.T. Paxton, M.W. Finnis, Structural and chemical embrittlement of 
grain boundaries by impurities: a general theory and first-principles calculations 
for copper, Phys. Rev. B 74 (2006) 155416 .
[57] S.J. Zhang, O.Y. Kontsevoi, A.J. Freeman, G.B. Olson, Sodium-induced 
embrittlement of an aluminum grain boundary, Phys. Rev. B 82 (2010) 224107 .
[58] P. Vajeeston, P. Ravindran, R. Vidya, A. Kjekshus, H. Fjellvåg, Site preference of 
hydrogen in metal, alloy, and intermetallic frameworks, Europhys. Lett. 72 (2005) 
569 – 575 .
[59] J.H. Dai, X. Wu, Y. Song, R. Yang, Electronic structure mechanism of martensitic 
phase transformation in binary titanium alloys, J. Appl. Phys. 112 (2012) 123718 .
[60] J.W. Yang, T. Gao, B.Q. Liu, G.A. Sun, B. Chen, Ab initio calculations of the ideal 
tensile and shear strengths of uranium metal, J. Nucl. Mater. 458 (2015) 122 – 128 .
[61] Y. Zhang, G.H. Lu, S.H. Deng, T.M. Wang, H.B. Xu, M. Kohyama, R. Yamamoto, 
Weakening of an aluminum grain boundary induced by sulfur segregation: a first- 
principles computational tensile test, Phys. Rev. B 75 (2007) 174101 .
[62] R.J. McCabe, L. Capolungo, P.E. Marshall, C.M. Cady, C.N. Tome, Deformation of 
wrought uranium: experiments and modeling, Acta Mater. 58 (2010) 5447 – 5459 .
[63] D.W. Wheeler, S.T. Morris, Micro-mechanical characterisation of uranium, J. Nucl. 
Mater. 385 (2009) 122 – 125 .
[64] M. Knezevic, L. Capolungo, C.N. Tome, R.A. Lebensohn, D.J. Alexander, B. Mihaila, 
R.J. McCabe, Anisotropic stress – strain response and microstructure evolution of 
textured a-uranium, Acta Mater. 60 (2012) 702 – 715 .
[65] K. Mahbuba, B. Beeler, A. Jokisaari, Evaluation of the anisotropic grain boundaries 
and surfaces of α -U via molecular dynamics, J. Nucl. Mater. 554 (2021) 153072 .
[66] I.J. Beyerlein, X.H. Zhang, A. Misra, Growth twins and deformation twins in 
metals, Annu. Rev. Mater. Res. 44 (2014) 329 – 363 .
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
11

## Page 12

[67] L. Velasco, A.M. Hodge, Growth twins in high stacking fault energy metals: 
microstructure, texture and twinning, Mater. Sci. Eng. A 687 (2017) 93 – 98 .
[68] R. Yu, L.L. He, H.Q. Ye, Effects of Si and Al on twin boundary energy of TiC, Acta 
Mater. 51 (2003) 2477 – 2484 .
[69] Z.J. Zhang, P. Zhang, L.L. Li, Z.F. Zhang, Fatigue cracking at twin boundaries: 
effects of crystallographic orientation and stacking fault energy, Acta Mater. 60 
(2012) 3113 – 3127 .
[70] R.Z. Su, D. Neffati, Y.F. Zhang, J.H. Cho, J. Li, H.Y. Wang, Y. Kulkarni, X.H. Zhang, 
The influence of stacking faults on mechanical behavior of advanced materials, 
Mater. Sci. Eng. A 803 (2021) 140696 .
[71] A.J. Zaddach, R.O. Scattergood, C.C. Koch, Tensile properties of low-stacking fault 
energy high-entropy alloys, Mater. Sci. Eng. A 636 (2015) 373 – 378 .
[72] T. Tsuru, H. Somekawa, D.C. Chrzan, Interfacial segregation and fracture in Mg- 
based binary alloys: experimental and first-principles perspective, Acta Mater. 151 
(2018) 78 – 86 .
[73] A. Goede, R. preissner, C. Fr ¨ommel, Voronoi Cell: New Method for allocation of 
space among atoms: elimination of avoidable errors in calculation of atomic 
volume and density, J. Comput. Chem. 18 (1997) 1113 – 1123 .
[74] G. Bozzolo, H.O. Mosca, A.M. Yacout, G.L. Hofman, Y.S. Kim, Surface properties, 
thermal expansion, and segregation in the U – Zr solid solution, Comput. Mater. Sci. 
50 (2010) 447 – 453 .
[75] S. Liu, J. Zhu, X.D. Lin, X.B. Wang, G.C. Wang, Coupling effect of stretch-bending 
deformation and electric pulse treatment on phase transformation behavior and 
superelasticity of a Ti-50.8 at% Ni alloy, Mater. Sci. Eng. A 799 (2021) 140164 .
[76] R.J. Jackson, Elastic, plastic, and strength properties of U–Nb and U–Nb–Zr alloys. 
Conference on Physical Metallurgy of Uranium Alloys, Brook Hill Publishing Co, 
Chestnut Hill, MA, 1976, pp. 611 – 656 .
[77] Jae Joon Kim, Hyun Woo Seong, Ho. Jin Ryu, First principles calculations of 
cohesive energy of fission-product-segregated grain boundary of UO
2
, J. Nucl. 
Mater. 566 (2022) 153780 .
[78] R.W. Li, K.Z. Liu, W.H. Luo, B. Su, D.L. Zou, Anisotropy in the elasticity of α -U from 
first-principles calculations and nanoindentation, J. Nucl. Mater. 558 (2022) 
153351 .
[79] K.H. Eckelmeyer, G.B. Dudder, L.R. Chapman, G.M. Ludtka, M.K. O ’ Brien, 
Deformation strengthening of uranium and dilute uranium alloys, J. Nucl. Mater. 
589 (2024) 154825 .
[80] D. Chen, X.J. Zhang, H.X. Wu, D.M. Lang, D.W. Xiao, Z.H. Wang, B. Su, D.Q. Meng, 
The influence of impurities on the ductility and toughness of a low-temperature- 
aged U-Nb alloy, Mater. Sci. Eng. A 739 (2019) 1 – 16 .
[81] R.F. Zhang, S.H. Sheng, S. Veprek, First principles studies of ideal strength and 
bonding nature of AlN polymorphs in comparison to TiN, Appl. Phys. Lett. 91 
(2007) 031906 .
[82] Y. Umeno, Y. Kinoshita, T. Kitamura, Ab initio DFT simulation of ideal shear 
deformation of SiC polytypes, Model. Simul. Mater. Sci. Eng. 15 (2007) 27 – 37 .
[83] J.P. Liu, Y.D. Wang, Y.L. Hao, Y.Z. Wang, Z.H. Nie, D. Wang, Y. Ren, Z.P. Lu, J. 
G. Wang, H.L. Wang, X.D. Hui, N. Lu, Moon J. Kim, R. Yang, New intrinsic 
mechanism on gum-like superelasticity of multifunctional alloys, Sci. Rep. 3 (2013) 
2156 .
[84] Y.L. Hao, H.L. Wang, T. Li, J.M. Cairney, A.V. Ceguerra, Y.D. Wang, Y. Wang, 
D. Wang, E.G. Obbard, S.J. Li, R. Yang, Superelasticity and tunable thermal 
expansion across a wide temperature range, J. Mater. Sci. Technol. 32 (2016) 
705 – 709 .
[85] Y.T. Su, C.X. Liang, X. Sun, H.L. Zhang, Q.L. Liang, Y.F. Zheng, Y.L. Hao, R. Yang, 
D. Wang, D. Banerjee, Y.Z. Wang, Composition-dependent shuffle-shear coupling 
and shuffle-regulated strain glass transition in compositionally modulated Ti-Nb 
alloys, Acta Mater. 246 (2023) 118697 .
X. Wen et al. Journal of Alloys and Compounds 1025 (2025) 180200 
12
