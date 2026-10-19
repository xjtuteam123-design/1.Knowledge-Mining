# 40_2022_Wang_Influence_of_Carbon_and_Oxygen_on_the_Core_Structure_and_Peierls_Stress_of_Screw_Dislocation_in_Moly

<!-- source: D:\总文献\40_2022_Wang_Influence_of_Carbon_and_Oxygen_on_the_Core_Structure_and_Peierls_Stress_of_Screw_Dislocation_in_Moly.pdf -->
<!-- file_sha256: 7cfa8f5f0c140e2395aa9e6e71a4875f22a8a587a9dd133d67e9105896670da1 -->

## Page 1

/gid00030/gid00035/gid00032/gid00030/gid00038/gid00001/gid00033/gid00042/gid00045/gid00001
/gid00048/gid00043/gid00031/gid00028/gid00047/gid00032/gid00046
Citation: Wang, Z.-Q.; Li, Y.-H.;
Lu, G.-H.; Zhou, H.-B. Inﬂuence of
Carbon and Oxygen on the Core
Structure and Peierls Stress of Screw
Dislocation in Molybdenum. Metals
2022, 12, 507. https://doi.org/
10.3390/met12030507
Academic Editor: Eric Hug
Received: 10 February 2022
Accepted: 14 March 2022
Published: 16 March 2022
Publisher’s Note:MDPI stays neutral
with regard to jurisdictional claims in
published maps and institutional afﬁl-
iations.
Copyright: © 2022 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
metals
Article
Inﬂuence of Carbon and Oxygen on the Core Structure and
Peierls Stress of Screw Dislocation in Molybdenum
Zi-Qi Wang 1,2
 , Yu-Hao Li 1,2, *, Guang-Hong Lu 1,2 and Hong-Bo Zhou 1,2, *
1 Department of Physics, Beihang University, Beijing 100191, China; wzq92wzq@buaa.edu.cn (Z.-Q.W.);
lgh@buaa.edu.cn (G.-H.L.)
2 Beijing Key Laboratory of Advanced Nuclear Materials and Physics, Beihang University, Beijing 100191, China
* Correspondence: yuhaoli@buaa.edu.cn (Y.-H.L.); hbzhou@buaa.edu.cn (H.-B.Z.)
Abstract: The plasticity and hardness of metals are largely dependent on how dislocation interacts
with solute atoms. Here, taking bcc molybdenum (Mo) as the example, the interaction of interstitial
solutes carbon (C) and oxygen (O) with screw dislocation, and their inﬂuences on the dislocation
motion, have been determined using ﬁrst-principles calculations and thermodynamic models. Due
to the incompact atomic structure and variation of electronic states in the dislocation core, C and
O will segregate from the bulk system to the dislocation region. Notably, the presence of C/O
at the dislocation induces the reconstruction of the core structure, from an easy-core to hard-core
conﬁguration. This originates from the fact that the hard-core structure provides a larger available
volume at the interstitial site than the easy-core structure and, thus, facilitates the dissolution of C
and O. More importantly, the addition of C/O in the dislocation signiﬁcantly increases the Peierls
stresses and double-kink formation enthalpies of screw dislocation in Mo, from 1.91 GPa and 1.18 eV
for C/O-free dislocation to 5.63/4.69 GPa and 1.77/1.58 eV for C/O-saturated dislocation. Therefore,
these interstitial solutes have a pinning effect on the dislocation motion, and this effect becomes
stronger with higher segregating levels. This work reveals the profound effect of interstitial solutes on
the properties of the dislocation core and provides a fundamental factor to account for the interstitial
solutes-related phenomena in bcc metals.
Keywords: carbon and oxygen; screw dislocation; core structure; bcc molybdenum
1. Introduction
The body-centered cubic (bcc) refractory metals are of prominent importance for
many potential applications in nuclear energy, aerospace and metallurgy, owing to their
high melting temperature, corrosion resistance and excellent strength [ 1–3]. However,
these metals typically display brittleness and poor formability at room temperature, which
severely limits their practical application. Ordinarily, the low plasticity of bcc metals at
low-to-intermediate temperatures should be rationalized by the substantially low mobility
of 1/2<111> screw dislocation [4–6]. Thus, in order to improve the ductility of refractory
metals, great efforts have been made to explore the inﬂuence of alloying elements on the
glide of 1/2<111> screw dislocation [7–10]. For example, it has long been recognized that
the addition of rhenium effectively reduces the brittleness of bcc metals, known as the “Re
ductilizing effect”, which can be attributed to the promoting effect of Re on the mobility
of screw dislocation [11,12]. Therefore, a full investigation of the behaviors of dislocation
and its interactions with solutes has become the key issue in understanding the plastic
deformation and mechanical properties of bcc refractory metals.
Besides the substitutional alloying elements, the interstitial impurities (intentionally
introduced and/or naturally incorporated during processing) also strongly inﬂuence the
mechanical properties of bcc metals, even at extremely low concentrations. For example,
using the transmission electron microscopy (TEM) in-situ straining experiment, a distinct
Metals 2022, 12, 507. https://doi.org/10.3390/met12030507 https://www.mdpi.com/journal/metals

## Page 2

Metals 2022, 12, 507 2 of 14
increase in the hardness of iron was observed with the addition of 110 appm carbon (C)
below 170 K or above 280 K [ 13]. Additionally, the presence of ~400 appm oxygen can
signiﬁcantly increase the yield and tensile strength of niobium (Nb), leading to the pro-
nounced hardening effect [14,15]. Similar results have been observed in bcc tungsten [16],
molybdenum [17], tantalum [18] and vanadium [19]. Therefore, these interstitial solutes
(e.g., C and O) are well-known to effectively induce the solution hardening of bcc metals
and, thus, rapidly degrade the malleability and fracture toughness of materials. Physically,
the inﬂuence of interstitial solutes on the plastic deformation of bcc metals should originate
from the interaction between the screw dislocation and solute atoms, which can only be
investigated by the atomic resolution methods that consider the local chemistry.
Beneﬁting from the rapid devolvement of computing capability and advanced algo-
rithms, enormous research efforts have been performed on solute–dislocation interactions in
bcc refractory metals by employing the density functional theory (DFT) method. It is found
that screw dislocation has a complex and non-planar core structure (i.e., high-symmetry
easy-core structure) in pure bcc metals [20,21], which offers a high lattice friction stress than
the easy-type dislocations. Since the incompact atomic arrangement is conducive to the
dissolution of interstitial impurities, there are expected to be strong attractive interactions
between C/O and screw dislocation [ 22–24]. Although the hindering of the dislocation
motion is traditionally attributed to the strong attraction of solutes with the dislocation and
the formation of “Cottrell atmospheres” [25–27], the dislocation–O interactions in Nb is
found to be repulsive [14]. Interestingly, besides the attractive or repulsive interactions,
recent studies have found that the segregation of interstitial solutes (e.g., hydrogen, helium,
carbon, oxygen) may induce the reconstruction of the dislocation core structure in bcc
metals [23,24,28]. Additionally, such a solute-induced transition of the core structure is
strongly dependent on the type of bcc metals and nominal concentration of interstitial
solutes. These results suggest that the interaction between the solute and screw dislocation
in bcc metals is complex and needs further in-depth investigation.
In the present work, the interaction of interstitial solutes (C and O) with 1/2<111>
screw dislocation and their effects on the dislocation motion in bcc Mo are investigated by
using the DFT calculations combined with thermodynamic models. This is an attractive
and active system because of the practical interest and technological importance of Mo as
accident tolerant fuel (ATF) cladding materials, in which C and O are known as the most
common foreign interstitial atoms in Mo-based alloys. According to our calculations, the
C/O atoms will segregate from the bulk system into the screw dislocation core, which can
be rationalized by the available volume and electronic interaction. Speciﬁcally, the presence
of C/O in the dislocation gives rise to the transition of the core structure from the original
easy-core structure in pure Mo to the hard-core structure of the C/O-decorated screw
dislocation. This is because the hard-core structure provides a larger available volume
at the interstitial site, in comparison with the easy-core dislocation, and facilitates the
C/O dissolution. Thus, the segregated C/O atoms occupy the trigonal prism center in the
hard-core conﬁguration and tend to form clusters along the dislocation line. Moreover,
the presence of C/O in the dislocation and the reconstruction of the core structure can
signiﬁcantly increase the Peierls stresses and double-kink formation enthalpies of screw
dislocation, and accordingly, suppress the dislocation motion in Mo. These results provide
a fundamental and essential factor to account for the profound effect of C/O on the
performance of bcc metals, especially for the solute-induced embrittlement/hardening.
2. Methodology
The ﬁrst-principles calculations were performed in the Vienna ab initio Simulation
Package (v5.4.1, VASP Software GmbH, Vienna, Austria) code [ 29] using the projector
augmented-wave pseudopotential scheme. The exchange-correlation parts were approxi-
mated within the generalized gradient approximation parameterized by Perdew, Burke
and Ernzerhof. A cutoff of 350 eV was applied, and the convergence criteria of force and
energy was set to be 0.01 eV/Å and 10−6 eV for ionic and electronic relaxation, respectively.

## Page 3

Metals 2022, 12, 507 3 of 14
Here, we used a 250-atom supercell for bulk calculations and a 4 × 4× 4 k-points grid
within the Monkhorst–Pack approach [30]. In all calculations, the periodic boundary con-
ditions were imposed for the relaxation of the supercell shape and size as well as atomic
positions. According to our calculations, the lattice parameter of perfect Mo is 3.149 Å, in
good accordance with the experimental value of 3.15 Å [31].
Here, a quadrupolar periodic array of dislocation dipoles was used to explore the
core property of screw dislocation and C/O–dislocation interactions in Mo. The screw
dislocation with 1/2 <111> Burgers vector has a three-fold screw rotation symmetry along
the core, as demonstrated in [32,33], and three core atoms per period are displaced along
the <111> direction to change the chirality of the triangular lattice. Here, in order to mimic
the core properties of screw dislocation, a pair of dislocation dipoles with opposite Burgers
vectors (i.e., +
→
b and−
→
b ) was introduced in the supercell with periodic bondary conditions
(see Figure 1), resulting in a square-like periodic arrangement of quadrupoles. Actually,
this method has been proven to rapidly converge the dislocation core energy [34,35] and
has been widely employed in recent DFT calculations of bcc metals [24,33,36]. Accordingly,
a symmetrical and non-degenerate core structure was obtained, which is in agreement with
previous studies [37,38]. The unit cell vector of dislocation in pure Mo is
→
C1 = 5a0
[
112
]
,
→
C2 = 2.5a0
[
112
]
+ 4.5a0
[
110
]
+ 0.5 a0
2 [111],
→
C3 = a0
2 [111], containing 135 Mo atoms (only
1
→
b along the dislocation line). To simulate the behaviors of C/O in the dislocation and
reduce the periodic solute–solute interaction, the simulation box in the dislocation line
was two times as large as the Burger vector, resulting from a 270-atom (2
→
b ) supercell. The
1× 2× 16 and 1× 2× 8 k-points k-point sampling for the supercells along the dislocation
line of 1b and 2b were used, respectively. It is important to note that the C/O atoms are
introduced around both dislocations to ensure equivalent energy and symmetric structure.
Moreover, in order to determine the properties of SD with hard-core structure in pure
Mo, a constrained minimization was employed to stabilize this conﬁguration (since it is
unstable in pure bcc metals). Similar with previous studies [ 39,40], only the positions
along the dislocation line of three central columns constituting the hard-core conﬁguration
were ﬁxed. It should be noted this hard-core structure may transform into the easy-core
conﬁguration, if the constrain is released. The obtained formation energy of a hard-core
screw dislocation is 0.15 eV/b higher than the easy-core structure, which is in agreement
with previous studies [41].
Metals 2022, 12, x FOR PEER REVIEW 3 of 14 
 
 
energy was set to be 0.01 eV/Å and 10−6 eV for ionic and electronic relaxation, respectively. 
Here, we used a 250-atom supercell for bulk calculations and a 4 × 4 × 4 k-points grid 
within the Monkhorst–Pack approach [30]. In all calculations, the periodic boundary con-
ditions were imposed for the relaxation of th e supercell shape and size as well as atomic 
positions. According to our calculations, the lattice parameter of perfect Mo is 3.149 Å, in 
good accordance with the experimental value of 3.15 Å [31]. 
Here, a quadrupolar periodic array of disl ocation dipoles was used to explore the 
core property of screw dislocation and C/O–dislocation interactions in Mo. The screw dis-
location with 1/2 <111> Burgers vector has a three-fold screw rotation symmetry along the 
core, as demonstrated in [32,33], and three core atoms per period are displaced along the 
<111> direction to change the chirality of the triangular lattice. Here, in order to mimic the 
core properties of screw dislocation, a pair of dislocation dipoles with opposite Burgers 
vectors (i.e., +𝒃ሬ
ሬ⃗ and −𝒃ሬሬ⃗) was introduced in the supercell with periodic bondary condi-
tions (see Figure 1), resulting in a square-lik e periodic arrangement of quadrupoles. Ac-
tually, this method has been proven to rapidly converge the dislocation core energy 
[34,35] and has been widely employed in recent DFT calculations of bcc metals [24,33,36]. 
Accordingly, a symmetrical and non-degenerate core structure was obtained, which is in 
agreement with previous studies [37,38]. The unit cell vector of dislocation in pure Mo is 
𝐶ଵሬሬሬሬ⃗ =5 𝑎଴[112ത], 𝐶ଶሬሬሬሬ⃗ =2 . 5 𝑎଴[112ത] +4 . 5 𝑎଴[1ത10] +0 . 5
௔బ
ଶ [111], 𝐶ଷሬሬሬሬ⃗ =
௔బ
ଶ [111], containing 135 
Mo atoms (only 1𝑏ሬ⃗ along the dislocation line). To simulate the behaviors of C/O in the 
dislocation and reduce the periodic solute–solute interaction, the simulation box in the 
dislocation line was two times as large as th e Burger vector, resulting from a 270-atom 
(2𝒃ሬሬ⃗) supercell. The 1 × 2 × 16 and 1 × 2 × 8 k-points k-point sampling for the supercells 
along the dislocation line of 1b and 2b were used, respectively. It is important to note that 
the C/O atoms are introduced around both di slocations to ensure equivalent energy and 
symmetric structure. Moreover, in order to determine the properties of SD with hard-core 
structure in pure Mo, a constrained minimization was employed to stabilize this configu-
ration (since it is unstable in pure bcc metals). Similar with previous studies [39,40], only 
the positions along the dislocation line of three central columns constituting the hard-core 
configuration were fixed. It should be noted this hard-core structure may transform into 
the easy-core configuration, if the constrain is released. The obtained formation energy of 
a hard-core screw dislocation is 0.15 eV/b higher than the easy-core structure, which is in 
agreement with previous studies [41]. 
 
Figure 1. Dislocation dipole within a (111) plane deno ted by a differential displacement map. The 
dislocation center is represented by the red triang le, while the small circles indicate the atomic po-
sitions. Three different colors of small circles ar e used to show that these atoms belong to three 
different (111) planes before introducing the dislocations. 
Figure 1. Dislocation dipole within a (111) plane denoted by a differential displacement map. The
dislocation center is represented by the red triangle, while the small circles indicate the atomic
positions. Three different colors of small circles are used to show that these atoms belong to three
different (111) planes before introducing the dislocations.

## Page 4

Metals 2022, 12, 507 4 of 14
For the Peierls stress calculations, we gradually increase the external strain until the
screw dislocation in Mo starts to move. The additional shear strain is applied by changing
the
→
C2 along the
→
C3 direction, that is
→
C′
2 =
→
C2 + k
→
C3. The main component of stress induced
by this strain σyz produces a force on the supercell, driving the dislocation motion along[
112
]
. The detailed information of our calculations is provided in [33].
3. Results and Discussions
3.1. Interaction of Screw Dislocation with Single C/O Atom
Since the atomic radii are much lower than that of the matrix, the C and O atoms
prefer to occupy the interstitial sites in bcc Mo. According to our calculations, the favorable
interstitial site of C/O is the octahedral/tetrahedral interstitial site (OIS/TIS) in Mo. The
obtained solution energy of interstitial C/O is 0.45/−0.59 eV , which is consistent with previ-
ous DFT results [23,42]. As for the screw dislocation in pure Mo, it adopts a high-symmetry
and nondegenerate conﬁguration, i.e., easy-core structure, as in most bcc metals [28,41,43].
This conﬁguration is centered on a triangle of ﬁrst-neighbor <111> atomic columns and the
helicity is reversed compared to the bulk system (see Figure 1). Here, in order to explore
the interaction of C/O with screw dislocation, a single C/O atom is placed at different
interstitial sites (including both OI- and TI-like sites) in the vicinity of the dislocation core,
as shown in Figure 2a. Accordingly, the interaction energy of C/O-dislocation can be
calculated by:
Eeasy
int = 1
2 (ESD+2X− ESD ) + (Ebulk− Ebulk +X) (1)
where ESD+2X (or ESD) is the energy of a supercell containing a dislocation dipole with (or
without) a single X (X denotes C/O) atom at each core. The presence of a factor of 1/2 is
because two screw dislocations are introduced in the simulation box, as seen in Figure 1.
Ebulk +X (or Ebulk ) is the energy of a perfect crystal with (or without) an X atom.
Metals 2022, 12, x FOR PEER REVIEW 4 of 14 
 
 
For the Peierls stress calculations, we gradually increase the external strain until the 
screw dislocation in Mo starts to move. The additional shear strain is applied by changing 
the 𝐶ଶሬሬሬሬ⃗ along the 𝐶ଷሬሬሬሬ⃗ direction, that is 𝐶ଶ
ᇱሬሬሬሬ⃗ =𝐶 ଶሬሬሬሬ⃗ +𝑘 𝐶ଷሬሬሬሬ⃗. The main component of stress in-
duced by this strain 𝜎௬௭ produces a force on the supercell, driving the dislocation motion 
along [112ത]. The detailed information of our calculations is provided in [33]. 
3. Results and Discussions 
3.1. Interaction of Screw Dislocation with Single C/O Atom 
Since the atomic radii are much lower than that of the matrix, the C and O atoms 
prefer to occupy the interstitial sites in bcc Mo. According to our calculations, the favora-
ble interstitial site of C/O is the octahedral/tetrahedral interstitial site (OIS/TIS) in Mo. The 
obtained solution energy of interstitial C/O is 0.45/−0.59 eV, which is consistent with pre-
vious DFT results [23,42]. As for the screw di slocation in pure Mo, it adopts a high-sym-
metry and nondegenerate configuration, i.e., ea sy-core structure, as in most bcc metals 
[28,41,43]. This configuration is centered on a triangle of first-neighbor <111> atomic col-
umns and the helicity is reversed compared to the bulk system (see Figure 1). Here, in 
order to explore the interaction of C/O with screw dislocation, a single C/O atom is placed 
at different interstitial sites (including both OI- and TI-like sites) in the vicinity of the dis-
location core, as shown in Figure 2a. Accordingly, the interaction energy of C/O-disloca-
tion can be calculated by: 
𝐸
௜௡௧
௘௔௦௬ = 1
2 (𝐸ௌ஽ାଶ௑ −𝐸 ௌ஽)+( 𝐸௕௨௟௞ −𝐸 ௕௨௟௞ା௑) (1)
where 𝐸ௌ஽ାଶ௑ (or 𝐸ௌ஽) is the energy of a supercell containing a dislocation dipole with (or 
without) a single X (X denotes C/O) atom at ea ch core. The presence of a factor of 1/2 is 
because two screw dislocations are introduced i n t h e s i m u l a t i o n b o x , a s s e e n i n F i g u r e 
1. 𝐸௕௨௟௞ା௑ (or 𝐸௕௨௟௞) is the energy of a perfect crystal with (or without) an X atom. 
 
Figure 2. (a) Projection along the (111) plane for pure Mo dislocation. The position of dislocation is 
marked with the red triangle and the position of the reconstructed hard core is marked with H. A 
total of 7 octahedral-like (O1–O7) and tetrahedral-like (T1–T7) interstitial sites around the dislocation 
core in pure Mo (without the relaxation of the solute–dislocation interactions) are represented in 
different colors. (b) The interaction energy of the C/O atom wi th dislocation as a function of initial 
solute–dislocation distance. 
Figure 2b displays the interaction energy of C/O with the screw dislocation in Mo. 
Note that the TI-like sites are unstable for C, and it will spontaneously move towards the 
neighboring OI-like sites after structure optimi zation. Similar results were also obtained 
for C in bulk Mo [44]. Therefore, the interaction energies of screw dislocation with C at TI-
like sites are not presented. As expected in Fi gure 2b, the interaction energy is negative 
Figure 2. (a) Projection along the (111) plane for pure Mo dislocation. The position of dislocation is
marked with the red triangle and the position of the reconstructed hard core is marked with H. A total
of 7 octahedral-like ( O1–O7) and tetrahedral-like ( T1–T7) interstitial sites around the dislocation
core in pure Mo (without the relaxation of the solute–dislocation interactions) are represented in
different colors. (b) The interaction energy of the C/O atom with dislocation as a function of initial
solute–dislocation distance.
Figure 2b displays the interaction energy of C/O with the screw dislocation in Mo.
Note that the TI-like sites are unstable for C, and it will spontaneously move towards the
neighboring OI-like sites after structure optimization. Similar results were also obtained for
C in bulk Mo [44]. Therefore, the interaction energies of screw dislocation with C at TI-like
sites are not presented. As expected in Figure 2b, the interaction energy is negative for all

## Page 5

Metals 2022, 12, 507 5 of 14
cases, indicating the attractive interactions of C/O-dislocation, which provide the driving
force for the segregation of C/O into the dislocation. Moreover, the lowest interaction
between C and the screw dislocation is−1.33 eV with the C-dislocation distance of 0.74 Å,
while that of the O-dislocation is−1.76 eV at the distance of 1.86 Å. These results suggest
that the segregation tendency of O in the screw dislocation is stronger than that of C.
Beyond these distances, the interaction energy increases with increasing C/O–dislocation
separation and approaches zero asymptotically. Thus, we can divide the C/O–dislocation
interaction into two regions. In the ﬁrst one, the C/O-dislocation distance ranges from
0.37 Å to 5 Å, and the interaction energy is lower than −1.08/−1.43 eV , respectively,
representing a strong interaction region. In the second one, the C/O–dislocation distance is
larger than 5 Å, and the interaction is much weaker. Such signiﬁcant variation of interaction
energy should be attributed to the reconstruction of the dislocation core structure. When
the distance between C/O and the dislocation line is lower than 5 Å (corresponding to
the strong interaction region), the spontaneous transition of the dislocation core (from the
easy-core structure to the hard-core conﬁguration) is clearly observed and the C/O atom is
located at the center of the trigonal prism in the hard-core conﬁguration. As for the case of
the weak interaction region, the dislocation remains as the original easy-core conﬁguration
and the C/O atom is “attracted” to the screw dislocation at the interstitial sites. These
results suggest that, similar with previous studies for H/He/C/N/O in tungsten and
C/N/O/B in iron [23,24,28], the segregation of C/O at the dislocation core triggers the
reconstruction of the core structure in bcc Mo, which enhances the interaction between
C/O and dislocation.
To explore the physical origin of the strong attraction of C/O–dislocation and the
C/O-induced core transition, the solution energy of C/O in bulk Mo and screw disloca-
tion core are decomposed into two contributions. The ﬁrst contribution is the mechanical
contribution, which is the deformation energy from pure Mo crystal (bulk or with screw
dislocations) to a solute-induced distorted one, corresponding to the energy release of struc-
ture relaxation after C/O removal, namely Esol
MC = E[(N Mo+X)−X]
⏐⏐⏐NSW =1− EN Mo , where
E[(N Mo+X)−X]
⏐⏐⏐
NSW =1
denotes the total energy of the distorted supercell. The second one
is the chemical contribution and reﬂects the variation of chemical bonds between solutes
and matrix atoms, which can be obtained by subtracting the mechanical contribution from
the solution energy, i.e., Esol
CC = Esol− Esol
MC.Obviously, the mechanical contribution has a
negative impact on the dissolution of C/O in Mo (corresponding to the positive values in
Table 1). This is due to the fact that the available volume of interstitial sites in Mo (both
the bulk system and dislocation region) is very small, and the dissolution of C/O induces
the volume expansion, resulting in the positive distortion energy. As for the chemical
contribution, it has a positive impact on the C/O dissolution (corresponding to the negative
values in Table 1), which is attributed to the strong electronic interaction of C/O with
matrix atoms. More importantly, the difference in mechanical contribution between bulk
and dislocation can reach up to 1.03 eV for C and comprises 78% of the solution energy
difference. This indicates that the mechanical contribution is mainly responsible for the
attraction of C-dislocation. The case of O shows the different results, in which the differ-
ence of electronic contribution (~1.10 eV) is larger than that of the mechanical part and
dominates the segregation of O into the screw dislocation. Besides, it is important to note
that the two contributions (i.e., mechanical and electronic part) of C/O dissolution in the
bulk system is much higher than that at the dislocation core, and together, these trigger the
strong attractive interaction of C/O–dislocation.

## Page 6

Metals 2022, 12, 507 6 of 14
Table 1. The solution energy (Esol in eV), mechanical contribution (Esol
MC in eV), chemical contribution
(Esol
CC in eV) and corresponding 1NN C/O-Mo distance as well as Voronoi volumes (in Å3) of interstitial
C/O before ionic relaxations in Mo. For reference, the italicized values show the results after
ionic relaxations.
Conﬁguration Esol Esol
MC Esol
CC Distance Voronoi Volume
C Bulk 0.46 1.66 −1.19 1.57/ 1.97 7.79/9.29
SD −0.86 0.63 −1.49 1.60/ 2.15 8.73/9.95
O Bulk −0.59 1.33 −1.92 1.76/ 1.98 7.97/10.38
SD −2.36 0.66 −3.02 1.78/ 2.16 8.73/10.15
Generally, the mechanical contribution reﬂects the solute-induced lattice distortion,
which originates from the difference between the available volume of interstitial sites in Mo
crystal and the ideal volume of interstitial C/O dissolution. Here, in order to quantitatively
estimate the available volume in bulk Mo and dislocation core, the Voronoi volume of
possible interstitial sites before ionic relaxation are examined, as illustrated in Table 1. As
expected, the Voronoi volume of interstitial sites in the dislocation region (both easy-core
and hard-core conﬁguration) is much larger than that in bulk Mo (~7.79 Å 3 for OIS and
~7.97 Å3 for TIS), leading to the low deformation energy induced by C/O dissolution in the
dislocation core. This is also conﬁrmed by the atomic conﬁguration. As seen in Figure 3,
the ﬁrst-nearest neighboring (1NN) distance of C-Mo and O-Mo in bulk is 1.57 Å and
1.76 Å, but in the dislocation core can reach up to 1.60 Å and 1.78 Å, respectively. It is
important to note that the Voronoi volume and 1NN C/O-Mo distance in the hard-core
structure are larger than that in the easy-core conﬁguration, as shown in Figure 3 and
Table 1, indicating that the C/O atom prefers to occupy the interstitial sites in the former
environment. Ordinarily, the easy-core structure is the most stable conﬁguration of screw
dislocation in bcc Mo [43]. However, in comparison with the easy-core conﬁguration, the
hard-core structure provides a larger available volume at the interstitial site, facilitating the
C/O dissolution and transitioning its core structure from an easy to a hard conﬁguration.
As for the electronic part, it is largely dependent on the chemical interaction of C/O
with matrix atoms. Here, to understand the electronic origin of C/O–dislocation interaction,
we examine the projected density of states (PDOSs) of Mo in the bulk and the dislocation
core (in both easy- and hard-core structures) as illustrated in Figure 4. The d-projected
DOSs of Mo have a bimodal distribution with a precipitous drop near the Fermi level, with
far more occupied states deep in the d-band and fewer occupied states at the Fermi level,
which underlies the higher stability of bcc metals. In contrast, the dislocation (both easy-
and hard-core) exhibits higher DOS near the Fermi level, suggesting lower stability than
the bulk. Similar observations were made in bcc W/Ta [ 45–47]. In general, the upshift
of the d-band center of Mo atoms weakens Mo–Mo bonds and enhances C/O-Mo bonds,
giving rise to the attractive interaction of C/O–dislocation in Mo (corresponding to the
reduction in electronic contribution from−1.19/−1.92 eV in bulk Mo to−1.49/−3.02 eV
in the dislocation core, see Table 1). There is, however, a negligible difference in PDOSs
between the easy- and hard-core conﬁguration, which suggests that the C/O-induced
easy-to-hard transition cannot be rationalized by the variation in the electronic structure of
Mo atoms.

## Page 7

Metals 2022, 12, 507 7 of 14
Metals 2022, 12, x FOR PEER REVIEW 6 of 14 
 
 
OIS and ~7.97 Å3 for TIS), leading to the low deformation energy induced by C/O disso-
lution in the dislocation core. This is also confirmed by the atomic configuration. As seen 
in Figure 3, the first-nearest neighboring (1NN) distance of C-Mo and O-Mo in bulk is 1.57 
Å and 1.76 Å, but in the dislocation core can reach up to 1.60 Å and 1.78 Å, respectively. It 
is important to note that the Voronoi volume and 1NN C/O-Mo distance in the hard-core 
structure are larger than that in the easy-core configuration, as shown in Figure 3 and Table 
1, indicating that the C/O atom prefers to occu py the interstitial sites in the former envi-
ronment. Ordinarily, the easy-core structure is the most stable configuration of screw dis-
location in bcc Mo [43]. However, in comparison with the easy-core configuration, the 
hard-core structure provides a larger available volume at the interstitial site, facilitating 
the C/O dissolution and transitioning its core structure from an easy to a hard configura-
tion. 
Table 1. The solution energy (𝐸௦௢௟ in eV), mechanical contribution ( 𝐸ெ஼
௦௢௟ in eV), chemical contribu-
tion (𝐸஼஼
௦௢௟ in eV) and corresponding 1NN C/O-Mo distance as well as Voronoi volumes (in Å 3) of 
interstitial C/O before ionic relaxations in Mo. For reference, the italicized values show the results 
after ionic relaxations. 
Configuration 𝑬𝒔𝒐𝒍 𝑬𝑴𝑪
𝒔𝒐𝒍 𝑬𝑪𝑪
𝒔𝒐𝒍 Distance Voronoi Volume 
C Bulk 0.46 1.66 −1.19 1.57/ 1.97 7.79/ 9.29 
SD −0.86 0.63 −1.49 1.60/ 2.15 8.73/ 9.95 
O Bulk −0.59 1.33 −1.92 1.76/ 1.98 7.97/ 10.38 
SD −2.36 0.66 −3.02 1.78/ 2.16 8.73/10.15 
 
Figure 3. The atomic conﬁguration of ( a) easy-core dislocation, ( b) tetrahedral interstitial site,
(c) octahedral interstitial site and (d,e) reconstructed hard-core dislocation with a C–C/O–O distance
of 2b and 1b in Mo.
Metals 2022, 12, x FOR PEER REVIEW 7 of 14 
 
 
Figure 3. The atomic configuration of ( a) easy-core dislocation, ( b) tetrahedral interstitial site, ( c) 
octahedral interstitial site and (d,e) reconstructed hard-core dislocation with a C–C/O–O distance of 
2b and 1b in Mo. 
As for the electronic part, it is largely dependent on the chemical interaction of C/O 
with matrix atoms. Here, to understand the electronic origin of C/O–dislocation interac-
tion, we examine the projected density of states (PDOSs) of Mo in the bulk and the dislo-
cation core (in both easy- and hard-core st ructures) as illustrated in Figure 4. The d-pro-
jected DOSs of Mo have a bi modal distribution with a precipitous drop near the Fermi 
level, with far more occupied states deep in the d-band and fewer occupied states at the 
Fermi level, which underlies the higher stability of bcc metals. In contrast, the dislocation 
(both easy- and hard-core) exhibits higher DOS near the Fermi level, suggesting lower 
stability than the bulk. Similar observations were made in bcc W/Ta [45–47]. In general, 
the upshift of the d-band center of Mo atoms weakens Mo–Mo bonds and enhances C/O-
Mo bonds, giving rise to the attractive interaction of C/O–dislocation in Mo (correspond-
ing to the reduction in electronic contribution from −1.19/−1 . 9 2 e V i n b u l k M o t o 
−1.49/−3.02 eV in the dislocation core, see Table 1). There is, however, a negligible differ-
ence in PDOSs between the easy- and hard-c ore configuration, which suggests that the 
C/O-induced easy-to-hard transi tion cannot be rationalized by the variation in the elec-
tronic structure of Mo atoms. 
 
Figure 4. Local d-DOS of Mo in the bulk and in the dislocation core with easy-core and hard-core 
configuration. 
3.2. Segregation of C/O Atoms in the Screw Dislocation 
As mentioned above, C/O tends to segregate into the screw dislocation core in Mo 
with a negative segregation energy, and more importantly, leads to the reconstruction of 
the dislocation core structure. Next, we consider the interaction of C–C and O–O in the 
screw dislocation in Mo. Similarly, based on the most stable configuration of an isolated 
C/O at the screw dislocation, the second C or O atom is placed at potential interstitial sites 
in the vicinity of the dislocation core. According to our calculations, once the second C or 
O atom is inserted, it tends to stay next to the pre-segregated C/O in the dislocation line 
(i.e., most stable configuration), as seen in Figure 3d,e. This can be simply understood by 
the minimization of total lattice distortion (that is the easy-to-hard transition) at the 
Figure 4. Local d-DOS of Mo in the bulk and in the dislocation core with easy-core and hard-
core conﬁguration.

## Page 8

Metals 2022, 12, 507 8 of 14
3.2. Segregation of C/O Atoms in the Screw Dislocation
As mentioned above, C/O tends to segregate into the screw dislocation core in Mo
with a negative segregation energy, and more importantly, leads to the reconstruction of
the dislocation core structure. Next, we consider the interaction of C–C and O–O in the
screw dislocation in Mo. Similarly, based on the most stable conﬁguration of an isolated
C/O at the screw dislocation, the second C or O atom is placed at potential interstitial sites
in the vicinity of the dislocation core. According to our calculations, once the second C
or O atom is inserted, it tends to stay next to the pre-segregated C/O in the dislocation
line (i.e., most stable conﬁguration), as seen in Figure 3d,e. This can be simply understood
by the minimization of total lattice distortion (that is the easy-to-hard transition) at the
dislocation core. Although the second C/O atom is placed at the different interstitial sites
initially, most conﬁgurations will reorganize and relax towards this most stable structure
spontaneously. Since the supercell containing a core length of two periods is employed
here, two C–C/O–O bonds are formed with the addition of a second C/O atom due to the
periodic boundary condition. Hence, the ﬁrst neighboring interaction (along the distance
line) between C/O atoms in the dislocation core can be expressed as:
EX−X
int = 1
4 (ESD+4X + ESD )− 1
2 ESD+2X (2)
where ESD+4X is the energy of a 270-Mo atom supercell containing dislocation dipoles with
4 solute atoms in the vicinity of the cores. Accordingly, the binding energy of C–C and O–O
in the screw dislocation is calculated to be−0.09 eV and 0.07 eV , respectively. These values
are lower than the binding energy of C–C/O–O in bulk, implying the weak interaction
between C/O atoms in the dislocation core. Furthermore, the interaction of the second
C/O with the screw dislocation (~−1.82/−1.93 eV of segregation energy) is much stronger
than that with the ﬁrst C/O atom and, thus, the pre-existing C/O has a slight effect on the
segregation of subsequent C/O atoms in the dislocation region. Namely, the segregated
C/O atoms occupy the center of the trigonal prism at the dislocation and tend to form
clusters along the dislocation line.
To estimate the segregating level of C/O in the dislocation, a mean-ﬁeld approach is
applied to estimate the concentration of C/O at the screw dislocation core in Mo. Within
this model, the contributions of enthalpy and conﬁgurational entropy are considered, while
other types of entropy (such as vibrational and electronic entropy) are neglected. Similar to
previous calculations [48], the equilibrium concentration of C/O in the screw dislocation
and bulk system are expressed by:
ceq
1− ceq
= cbulk
1− cbulk
exp (−Eseg
(
ceq
)
/kT) (3)
where Eseg
(
ceq
)
is the segregation energy of C/O at the dislocation core, obtained by:
Eseg
(
ceq
)
= Ehard
int + 2ceq EX−X
int (4)
where Ehard
int is the interaction energy of an interstitial C/O with the hard-core dislocation.
EX−X
int (X denotes C or O) is the interaction energy between X atoms at 1NN distance in the
screw dislocation. Additionally, the concentrations of C/O at the dislocation core and bulk
system are also linked to their nominal concentration (i.e., the number of C/O atoms per
Mo) and, thus, we obtain Nicbulk + Ndceq = NMo c0. Ni and Nd is the number of interstitial
sites (OISs for C and TIS for O) in the bulk and the dislocation for a volume V , respectively.
Since there are three (or six) OISs (or TISs) per Mo atom in the bulk system, the number
of TISs for C (or OISs for O) in the bulk Mo can be calculated by 6V/a03 (or 12V/a03, a0
~lattice parameter). In the dislocation region, the corresponding number of interstitial
sites is expressed as ρV/b, in which ρ and b are the dislocation density and Burgers vector,
respectively. As for NMo, it represents the number of Mo atoms in the bulk system with a

## Page 9

Metals 2022, 12, 507 9 of 14
volume V, that is NMo = 2V/a03. It is important to note that the above equations are solved
self-consistently to determine the segregating concentration of C/O at the dislocation core
in Mo.
The equilibrium concentrations of interstitial C/O at dislocation as a function of
temperature are illustrated in Figure 5. Here, three different nominal concentration of C/O
(10 appm, 100 appm, and 1000 appm) and two different dislocation densities (1012 m−2 and
1015 m−2) are taken into account. As expected, the equilibrium concentration of interstitial
C/O is strongly related to the temperatures, nominal concentration and dislocation density.
As seen in Figure 5, the segregating level of interstitial C/O in the dislocation region
decreases with the increasing of dislocation density, and increases with the increase in
nominal concentration in bulk Mo. The equilibrium concentration of interstitial C/O
in the dislocation region is close to ~100% at 1200 K for all cases, except the extremely
low solute concentration (~10 appm) and high dislocation density (~10 15 m−2). Beyond
1200 K, the equilibrium concentration of C/O decreases with the increase in temperatures
(since the high temperature facilitates the de-trapping of solute atoms) but still reaches
up to 22%/57% at 2700 K with the nominal concentration of 1000 appm and dislocation
density of 1012 m−2. Therefore, the screw dislocation would be easily and fully saturated
by C/O in Mo, which triggers the transition of the dislocation core structure. Moreover, the
segregating concentration of O in the dislocation is slightly higher than that of C because
the former one has a lower segregation energy (see Figure 2).
Metals 2022, 12, x FOR PEER REVIEW 9 of 14 
 
 
concentration (~10 appm) and high dislocation density (~10 15 m −2). Beyond 1200 K, the 
equilibrium concentration of C/O decreases with the increase in temperatures (since the 
high temperature facilitates the de-trapping of solute atoms) but still reaches up to 
22%/57% at 2700 K with the nominal concentration of 1000 appm and dislocation density 
of 1012 m−2. Therefore, the screw dislocation would be easily and fully saturated by C/O in 
Mo, which triggers the transition of the dislocation core structure. Moreover, the segre-
gating concentration of O in the dislocation is slightly higher than that of C because the 
former one has a lower segregation energy (see Figure 2). 
 
Figure 5. Temperature dependence of the (a) C and (b) O concentration segregated in the dislocation 
core for three typical nominal concentrations of solutes and for two dislocation densities, 10 12 m−2 
(solid lines) and 1015 m−2 (dashed lines). 
3.3. The Effect of C/O Segregation on the Dislocation Motion 
Generally speaking, the reconstruction of the dislocation core will profoundly affect 
its movement [28,49]. We thus examine the influences of C and O on the critical stress for 
the glide of a screw dislocation in Mo. As shown in Figure 6, the shear stress exhibits a 
linear increase when the applied strain is less than 0.135. After that, the shear stress shows 
a sharp reduction, because of the glide of th e screw dislocation. The maximum stress at 
this point is regarded as the Peierls stress. Accordingly, the Peierls stress of pure Mo is 
1.91 GPa, as seen in Figure 6, in good acco rdance with previous studies (~2.1 GPa in [20] 
and ~1.8 GPa in [43]). More importantly, the presence of C/O segregation has a significant 
influence on the Peierls stress and dislocation motion. As illustrated in Figure 6, when a 
single C and O is introduced in the dislocation, the corresponding Peierls stress reaches 
up to 4.12 and 3.37 GPa, respectively. These values are much higher than that in C/O-free 
dislocation, suggesting that the interstitial C/O serve as strong obstacles for dislocation 
motion. Also, the Peierls stress increases wi th the increasing of C/O numbers, from 
4.12/3.37 GPa for one C/O atom (within two periods) to 5.63/4.69 GPa for a C–C/O–O pair. 
Therefore, owing to the strong attractive interaction of C/O with dislocation, the segrega-
tion of C/O significantly increases the Peierl s stress of screw dislocation and suppresses 
the dislocation motion in Mo, and the pinning effect becomes stronger with higher segre-
gating levels. 
Figure 5. Temperature dependence of the (a) C and (b) O concentration segregated in the dislocation
core for three typical nominal concentrations of solutes and for two dislocation densities, 1012 m−2
(solid lines) and 1015 m−2 (dashed lines).
3.3. The Effect of C/O Segregation on the Dislocation Motion
Generally speaking, the reconstruction of the dislocation core will profoundly affect its
movement [28,49]. We thus examine the inﬂuences of C and O on the critical stress for the
glide of a screw dislocation in Mo. As shown in Figure 6, the shear stress exhibits a linear
increase when the applied strain is less than 0.135. After that, the shear stress shows a sharp
reduction, because of the glide of the screw dislocation. The maximum stress at this point
is regarded as the Peierls stress. Accordingly, the Peierls stress of pure Mo is 1.91 GPa, as
seen in Figure 6, in good accordance with previous studies (~2.1 GPa in [20] and ~1.8 GPa
in [43]). More importantly, the presence of C/O segregation has a signiﬁcant inﬂuence on
the Peierls stress and dislocation motion. As illustrated in Figure 6, when a single C and
O is introduced in the dislocation, the corresponding Peierls stress reaches up to 4.12 and
3.37 GPa, respectively. These values are much higher than that in C/O-free dislocation,
suggesting that the interstitial C/O serve as strong obstacles for dislocation motion. Also,
the Peierls stress increases with the increasing of C/O numbers, from 4.12/3.37 GPa for
one C/O atom (within two periods) to 5.63/4.69 GPa for a C–C/O–O pair. Therefore,
owing to the strong attractive interaction of C/O with dislocation, the segregation of C/O

## Page 10

Metals 2022, 12, 507 10 of 14
signiﬁcantly increases the Peierls stress of screw dislocation and suppresses the dislocation
motion in Mo, and the pinning effect becomes stronger with higher segregating levels.
Metals 2022, 12, x FOR PEER REVIEW 10 of 14 
 
 
 
Figure 6. Shear stress variation as a function of strain for pure and decorated screw dislocation in 
Mo. 1b and 2b represent the distance between the solute (C or O) atoms along <111> direction. 
Microscopically, the motion of screw dislocations in bcc metals at a finite temperature 
is controlled by the kink-pair mechanism, which depends strongly on the kink-pair for-
mation enthalpy (𝐻௞௣). Here, we employed a line tension model to approximate the kink-
pair formation enthalpy in Mo without and with interstitial C/O based on known lattice 
parameters, elastic constants, calculated solu te-dislocation trapping energies and corre-
sponding Peierls stresses. Similar to previous studies [50,51], the double-kink formation 
enthalpies in stress-free conditions are obtained by: 
𝐻௞௣ =𝑍 𝑑଴ට2𝛾ௗ𝑑଴𝑏𝜎௣ (5)
where Z is a constant ~ 4/πଷଶ⁄ (since the Peierls potential of screw dislocation in Mo is 
assumed to be a sinusoidal shape [51]). 𝑑଴ = ඥ2/3𝑎଴ is the period of Peierls potential and 
𝛾ௗ is the line tension of an isolated scre w dislocation, which can be calculated as 𝛾ௗ =
௄௕మ
(ସగ) ୪୬ቀ ೃ
ೝ೎ቁ
+𝐸 ௖௢௥௘. As proposed in a previous study [51], the term ln(
ோ
௥೎
) is generally as-
sumed to be 4 and the prefactor ( 𝐾) is obtained by [𝐶ସସ(𝐶ଵଵ −𝐶 ଵଶ)/2]
భ
మ. The elastic con-
stants of pure Mo are obtained by our DFT ca lculations using a two-atom supercell with 
a 30 × 30 × 30 k-points grid, which were fo und to be 487 GPa, 171 GPa and 107 GPa for 
𝐶ଵଵ, 𝐶ଵଶ and 𝐶ସସ, respectively. These values were consistent with the results reported pre-
viously [44,52]. As for the core energy ( 𝐸௖௢௥௘), it is extracted from the first-principles cal-
culations. It is important to note that the line tension model used in Equation (5) has been 
shown to successfully reproduce the kink-pair formation enthalpies in pure bcc metals 
and/or describe the influence of high concen tered alloying elements in a mean-field ap-
proach [51,53,54]. Therefore, in order to employ this model to estimate the effects of C/O 
with low concentration, two prerequisites should be satisfied. The first one is that the con-
centration of C/O in the dislocation region is high enough so that a mean-field approxi-
mation is justified; this is clarified in detail in Section 3.2. The second one is that the mo-
bility of interstitial C/O should be much higher than that of screw dislocation, thus, the 
solute atom can catch up with the moving screw dislocation in Mo. This is the case in the 
Mo-C/O system because the migration energy barrier of C/O in the bulk Mo (~1.20 eV for 
C and ~0.05 eV for O in our calculations, ~1.22 eV for C in [44]) is lower or comparable 
Figure 6. Shear stress variation as a function of strain for pure and decorated screw dislocation in
Mo. 1b and 2b represent the distance between the solute (C or O) atoms along <111> direction.
Microscopically, the motion of screw dislocations in bcc metals at a ﬁnite temperature
is controlled by the kink-pair mechanism, which depends strongly on the kink-pair forma-
tion enthalpy (Hkp). Here, we employed a line tension model to approximate the kink-pair
formation enthalpy in Mo without and with interstitial C/O based on known lattice param-
eters, elastic constants, calculated solute-dislocation trapping energies and corresponding
Peierls stresses. Similar to previous studies [50,51], the double-kink formation enthalpies
in stress-free conditions are obtained by:
Hkp = Zd0
√
2γdd0bσp (5)
where Z is a constant ~ 4/π3/2 (since the Peierls potential of screw dislocation in Mo is
assumed to be a sinusoidal shape [ 51]). d0 =√
2/3a0 is the period of Peierls potential
and γd is the line tension of an isolated screw dislocation, which can be calculated as
γd = Kb2
(4π) ln( R
rc ) + Ecore. As proposed in a previous study [51], the term ln
(
R
rc
)
is generally
assumed to be 4 and the prefactor ( K) is obtained by [C44(C11− C12)/2]
1
2 . The elastic
constants of pure Mo are obtained by our DFT calculations using a two-atom supercell
with a 30× 30× 30 k-points grid, which were found to be 487 GPa, 171 GPa and 107 GPa
for C11, C12 and C44, respectively. These values were consistent with the results reported
previously [44,52]. As for the core energy ( Ecore), it is extracted from the ﬁrst-principles
calculations. It is important to note that the line tension model used in Equation (5) has
been shown to successfully reproduce the kink-pair formation enthalpies in pure bcc
metals and/or describe the inﬂuence of high concentered alloying elements in a mean-ﬁeld
approach [51,53,54]. Therefore, in order to employ this model to estimate the effects of
C/O with low concentration, two prerequisites should be satisﬁed. The ﬁrst one is that
the concentration of C/O in the dislocation region is high enough so that a mean-ﬁeld
approximation is justiﬁed; this is clariﬁed in detail in Section 3.2. The second one is that the
mobility of interstitial C/O should be much higher than that of screw dislocation, thus, the

## Page 11

Metals 2022, 12, 507 11 of 14
solute atom can catch up with the moving screw dislocation in Mo. This is the case in the
Mo-C/O system because the migration energy barrier of C/O in the bulk Mo (~1.20 eV
for C and ~0.05 eV for O in our calculations, ~1.22 eV for C in [44]) is lower or comparable
with the kink-pair formation enthalpy of screw dislocation (~1.27 eV in [54] and ~1.05 eV
in [55]). Accordingly, we employed this model to describe the inﬂuences of C and O on
the movement of screw dislocation in Mo. Thus, based on the obtained segregation energy,
Peierls stress and known elastic parameters, we can examine the kink-pair formation
enthalpy of C/O-free and C/O-decorated dislocation in Mo.
Table 2 displays the inﬂuence of interstitial C/O on the properties of screw dislocation
core in Mo. Apparently, the presence of C/O atoms in the dislocation generally reduces
the core energy and the line tension of screw dislocation. This is because of the attraction
of C/O–dislocation, which lowers the formation energy of the screw dislocation in Mo.
Namely, the lower the segregation energy, the lower the core energy (or line tension) of
screw dislocation. Speciﬁcally, we found the double-kink formation enthalpy in pure Mo to
be 1.18 eV . This is consistent with previous theoretic studies (~1.15 eV in [41] and ~1.05 eV
in [55]) and experimental values (~1.19 eV in [ 54]). Furthermore, the presence of C/O
atoms signiﬁcantly affects the double-kink formation enthalpies. As displayed in Table 2,
the double-kink formation enthalpy increases with the increase in C/O numbers, from
1.65/1.47 eV for a single C/O to 1.77/1.58 eV for a C–C/O–O pair. Notably, the obtained
kink-pair formation enthalpies in the C/O-decorated system are much higher than that
in the pure system, demonstrating the strong pinning effects of interstitial C/O atoms on
the motion of screw dislocations in Mo. The above calculations are consistent with the
experimental observations [16,17] in which the addition of dilute C and O rapidly increases
the hardness of bcc metals.
Table 2. Inﬂuence of interstitial C/O on the screw dislocation (SD) core property in Mo. The core
energy (in eV/b), line tension of an isolated dislocation (in eV/Å), Peierls stress (in GPa) and kink-pair
formation enthalpy (in eV) are given.
Conﬁguration Ecore γd σP Hkp
Pure SD 1.18 2.47 1.91 1.18
SD + 1C 0.46 2.20 4.12 1.65
SD + 2C −0.45 1.87 5.63 1.77
SD + 1O 0.30 2.15 3.37 1.47
SD + 2O −0.66 1.79 4.69 1.58
4. Conclusions
In summary, the behaviors of C and O at the screw dislocation core in Mo are sys-
tematically investigated by employing the comprehensive ﬁrst-principles calculations and
statistical models. The C and O atoms are favorable to segregate from the bulk to the dislo-
cation core in Mo. This is because, compared to the bulk system, the dislocation core has an
incompact atomic arrangement and activated electronic states. Both of them are conducive
to the dissolution of interstitial solutes, leading to the strong attraction of C/O–dislocation.
Moreover, the presence of C and O in the dislocation will induce the reconstruction of the
dislocation core structure spontaneously, from an original easy-core structure in pure Mo
to a hard-core conﬁguration for C/O-decorated dislocation. Such easy-to-hard transition is
rationalized by the atomic structure variation since the available volume of interstitial sites
in the hard-core dislocation is much larger than that in the easy-core structure and, thus,
facilitates the C/O dissolution.
Further, we examine the segregating level of interstitial C/O in the dislocation region.
Because of the attraction of C/O with the hard-core dislocation, the segregated C/O
atoms occupy the center of the trigonal prism at the dislocation core and tend to form
clusters along the dislocation line. More importantly, unless the solute concentrations
are very low (~10 appm for C/O) and the densities of screw dislocation are extremely
high (~1015 m−2), the concentration of C/O at the dislocation line reaches up to ~100% at

## Page 12

Metals 2022, 12, 507 12 of 14
1200 K. This suggests that the screw dislocation would be easily and fully saturated by
C/O in Mo, which triggers the transition of the dislocation core structure. Additionally,
the segregation of interstitial C/O atoms in the screw dislocation signiﬁcantly increases
the Peierls stresses and double-kink formation enthalpies, from 1.91 GPa and 1.18 eV for
C/O-free dislocation to 5.63/4.69 GPa and 1.77/1.58 eV for C/O-saturated dislocation,
suggesting the strong pinning effects of interstitial C/O on the dislocation motion in Mo.
Our calculations provide a good reference for understanding the inﬂuences of impurities
on the mechanical properties of Mo.
Author Contributions: Conceptualization, Y.-H.L. and H.-B.Z.; Investigation, Z.-Q.W.; Methodology,
Z.-Q.W. and Y.-H.L.; Project administration, G.-H.L.; Supervision, H.-B.Z.; Writing—original draft,
Z.-Q.W.; Writing—review and editing, Y.-H.L., G.-H.L. and H.-B.Z. All authors have read and agreed
to the published version of the manuscript.
Funding: This research is ﬁnancially supported by the National Natural Science Foundation of
China with Grant Nos. 11905135 and 12075022, and the Major Program of National Natural Science
Foundation of China with Grant Nos. 12192281.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data sharing is not applicable.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1. Terrani, K.A. Accident tolerant fuel cladding development: Promise, status, and challenges. J. Nucl. Mater. 2018, 501, 13–30.
[CrossRef]
2. Terrani, K.A.; Zinkle, S.J.; Snead, L.L. Advanced oxidation-resistant iron-based alloys for LWR fuel cladding. J. Nucl. Mater. 2014,
448, 420–435. [CrossRef]
3. Bachurina, D.; Vorkel, V .; Suchkov, A.; Gurova, J.; Ivannikov, A.; Penyaz, M.; Fedotov, I.; Sevryukov, O.; Kalin, B. Overview of the
mechanical properties of tungsten/steel brazed joints for the demo fusion reactor. Metals 2021, 11, 209. [CrossRef]
4. Christian, J.W. Some surprising features of the plastic deformation of body-centered cubic metals and alloys. Metall. T rans. A
1983, 14, 1237–1256. [CrossRef]
5. Pande, C.S.; Goswami, R. Dislocation emission and crack dislocation interactions. Metals 2020, 10, 473. [CrossRef]
6. Carneiro, Í.; Simões, S. Recent Advances in EBSD Characterization of Metals. Metals 2020, 10, 1097. [CrossRef]
7. Meyers, M.A.; Mishra, A.; Benson, D.J. Mechanical properties of nanocrystalline materials. Prog. Mater. Sci. 2006, 51, 427–556.
[CrossRef]
8. Weygand, D.; Mrovec, M.; Hochrainer, T.; Gumbsch, P . Multiscale Simulation of Plasticity in bcc Metals.Annu. Rev. Mater. Res.
2015, 45, 369–390. [CrossRef]
9. Seeger, A. Peierls barriers, kinks, and ﬂow stress: Recent progress. Z. Für Met. 2002, 93, 760–777. [CrossRef]
10. Gröger, R.; Bailey, A.G.; Vitek, V . Multiscale modeling of plastic deformation of molybdenum and tungsten: I. Atomistic studies
of the core structure and glide of 1/2⟨1 1 1⟩screw dislocations at 0 K. Acta Mater. 2008, 56, 5401–5411. [CrossRef]
11. Luo, A.; Jacobson, D.L.; Shin, K.S. Solution softening mechanism of iridium and rhenium in tungsten at room temperature. Int. J.
Refract. Met. Hard Mater. 1991, 10, 107–114. [CrossRef]
12. Miao, S.; Xie, Z.; Lin, Y.; Fang, Q.; Tan, J.; Zhao, Y. Mechanical Properties, Thermal Stability and Microstructures of W-Re-ZrC
Alloys Fabricated by Spark Plasma Sintering. Metals 2020, 10, 277. [CrossRef]
13. Caillard, D. An in situ study of hardening and softening of iron by carbon interstitials. Acta Mater. 2011, 59, 4974–4989. [CrossRef]
14. Yang, P .J.; Li, Q.J.; Tsuru, T.; Ogata, S.; Zhang, J.W.; Sheng, H.W.; Shan, Z.W.; Sha, G.; Han, W.Z.; Li, J.; et al. Mechanism
of hardening and damage initiation in oxygen embrittlement of body-centred-cubic niobium. Acta Mater. 2019, 168, 331–342.
[CrossRef]
15. Yang, P .J.; Li, Q.J.; Han, W.Z.; Li, J.; Ma, E. Designing solid solution hardening to retain uniform ductility while quadrupling yield
strength. Acta Mater. 2019, 179, 107–118. [CrossRef]
16. Stephens, J.R. Effects of Interstitial Impurities on the Low-T emperature T ensile Properties of T ungsten; Technical Report NASA TN
D-2287; National Aeronautics and Space Administration, Lewis Research Center: Cleveland, OH, USA, 1964.
17. Xing, H.; Hu, P .; Han, J.; Li, S.; Ge, S.; Hua, X.; Hu, B.; Yang, F.; Wang, K.; Feng, P . Effects of oxygen on microstructure and
evolution mechanism of body-centred-cubic molybdenum. Int. J. Refract. Met. Hard Mater. 2022, 103, 105747. [CrossRef]
18. Ulitchny, M.G.; Gibala, R. The effects of interstitial solute additions on the mechanical properties of niobium and tantalum single
crystals. J. Less Common Met. 1973, 33, 105–116. [CrossRef]

## Page 13

Metals 2022, 12, 507 13 of 14
19. Jo, M.G.; Madakashira, P .P .; Suh, J.Y.; Han, H.N. Effect of oxygen and nitrogen on microstructure and mechanical properties of
vanadium. Mater. Sci. Eng. A 2016, 675, 92–98. [CrossRef]
20. Woodward, C.; Rao, S.I. Ab-initio simulation of isolated screw dislocations in bcc Mo and Ta.Philos. Mag. A 2001, 81, 1305–1316.
[CrossRef]
21. Li, J.; Wang, C.-Z.; Chang, J.-P .; Cai, W.; Bulatov, V .V .; Ho, K.-M.; Yip, S. Core energy and Peierls stress of a screw dislocation in
bcc molybdenum: A periodic-cell tight-binding study. Phys. Rev. B 2004, 70, 104113. [CrossRef]
22. Lüthi, B.; Ventelon, L.; Rodney, D.; Willaime, F. Attractive interaction between interstitial solutes and screw dislocations in bcc
iron from ﬁrst principles. Comput. Mater. Sci. 2018, 148, 21–26. [CrossRef]
23. Lüthi, B.; Ventelon, L.; Elsässer, C.; Rodney, D.; Willaime, F. First principles investigation of carbon-screw dislocation interactions
in body-centered cubic metals. Model. Simul. Mater. Sci. Eng. 2017, 25, 084001. [CrossRef]
24. Hachet, G.; Ventelon, L.; Willaime, F.; Clouet, E. Screw dislocation-carbon interaction in BCC tungsten: An ab initio study.Acta
Mater. 2020, 200, 481–489. [CrossRef]
25. Medvedeva, N.I.; Gornostyrev, Y.N.; Freeman, A.J. Solid solution softening and hardening in the group-V and group-VI bcc
transition metals alloys: First principles calculations and atomistic modeling. Phys. Rev. B 2007, 76, 212104. [CrossRef]
26. Yu, Q.; Qi, L.; Tsuru, T.; Traylor, R.; Rugg, D.; Morris, J.W.; Asta, M.; Chrzan, D.C.; Minor, A.M. Origin of dramatic oxygen solute
strengthening effect in titanium. Science 2015, 347, 635–639. [CrossRef] [PubMed]
27. Zhao, Y.; Marian, J. Direct prediction of the solute softening-to-hardening transition in W-Re alloys using stochastic simulations
of screw dislocation motion. Model. Simul. Mater. Sci. Eng. 2018, 26, 045002. [CrossRef]
28. Ventelon, L.; Lüthi, B.; Clouet, E.; Proville, L.; Legrand, B.; Rodney, D.; Willaime, F. Dislocation core reconstruction induced by
carbon segregation in bcc iron. Phys. Rev. B 2015, 91, 220102. [CrossRef]
29. Kresse, G.; Hafner, J. Ab initio molecular dynamics for liquid metals. Phys. Rev. B 1993, 47, 558–561. [CrossRef]
30. Pack, J.D.; Monkhorst, H.J. “Special points for Brillouin-zone integrations”—A reply. Phys. Rev. B 1977, 16, 1748–1749. [CrossRef]
31. Kittel, C. Introduction to Solid State Physics , 8th ed.; Wiley Sons: New York, NY, USA, 2004.
32. Trinkle, D.R.; Woodward, C. The Chemistry of Deformation: How Solutes Soften Pure Metals. Science 2005, 310, 1665–1667.
[CrossRef]
33. Li, Y.-H.; Zhou, H.-B.; Gao, F.; Lu, G.; Lu, G.-H.; Liu, F. Hydrogen induced dislocation core reconstruction in bcc tungsten.Acta
Mater. 2022, 226, 117622. [CrossRef]
34. Ventelon, L.; Willaime, F. Core structure and Peierls potential of screw dislocations inα-Fe from ﬁrst principles: Cluster versus
dipole approaches. J. Comput. Mater. Des. 2007, 14, 85–94. [CrossRef]
35. Clouet, E.; Ventelon, L.; Willaime, F. Dislocation Core Energies and Core Fields from First Principles. Phys. Rev. Lett. 2009,
102, 055502. [CrossRef] [PubMed]
36. Rodney, D.; Ventelon, L.; Clouet, E.; Pizzagalli, L.; Willaime, F. Ab initio modeling of dislocation core properties in metals and
semiconductors. Acta Mater. 2017, 124, 633–659. [CrossRef]
37. Ismail-Beigi, S.; Arias, T.A. Ab Initio Study of Screw Dislocations in Mo and Ta: A New Picture of Plasticity in bcc Transition
Metals. Phys. Rev. Lett. 2000, 84, 1499–1502. [CrossRef]
38. Woodward, C.; Rao, S.I. Flexible Ab Initio Boundary Conditions: Simulating Isolated Dislocations in bcc Mo and Ta. Phys. Rev.
Lett. 2002, 88, 216402. [CrossRef]
39. Ventelon, L.; Willaime, F.; Clouet, E.; Rodney, D. Ab initio investigation of the Peierls potential of screw dislocations in bcc Fe and
W. Acta Mater. 2013, 61, 3973–3985. [CrossRef]
40. Itakura, M.; Kaburaki, H.; Yamaguchi, M. First-principles study on the mobility of screw dislocations in bcc iron. Acta Mater. 2012,
60, 3698–3710. [CrossRef]
41. Dezerald, L.; Ventelon, L.; Clouet, E.; Denoual, C.; Rodney, D.; Willaime, F. Ab initio modeling of the two-dimensional energy
landscape of screw dislocations in bcc transition metals. Phys. Rev. B 2014, 89, 024104. [CrossRef]
42. Scheiber, D.; Pippan, R.; Puschnig, P .; Romaner, L. Ab initio search for cohesion-enhancing impurity elements at grain boundaries
in molybdenum and tungsten. Model. Simul. Mater. Sci. Eng. 2016, 24, 085009. [CrossRef]
43. Shimizu, F.; Ogata, S.; Kimizuka, H.; Kano, T.; Li, J.; Kaburaki, H. First-principles Calculation on Screw Dislocation Core Properties
in BCC Molybdenum. J. Earth Simulator 2007, 7, 17–21.
44. Yang, K.J.; Liu, Y.L.; Liu, Z.L.; Liu, C.; Shao, P .; Zhang, X.; Han, Q.F. Basic physical behavior of impurity carbon in molybdenum
for nuclear material: A systematical ﬁrst-principles simulation. Nucl. Mater. Energy 2021, 28, 101053. [CrossRef]
45. Hu, Y.-J.; Zhao, G.; Zhang, B.; Yang, C.; Zhang, M.; Liu, Z.-K.; Qian, X.; Qi, L. Local electronic descriptors for solute-defect
interactions in bcc refractory metals. Nat. Commun. 2019, 10, 4484. [CrossRef] [PubMed]
46. Ren, Q.-Y.; Li, Y.-H.; Zhou, H.-B.; Li, Z.-Z.; Cheng, L.; Lu, G.-H. Characterization of the energetics and conﬁgurations of hydrogen
in vacancy clusters in tungsten. Nucl. Fusion 2019, 59, 106032. [CrossRef]
47. Li, Y.H.; Zhou, H.B.; Liang, L.; Gao, N.; Deng, H.; Gao, F.; Lu, G.; Lu, G.H. Transition from ductilizing to hardening in tungsten:
The dependence on rhenium distribution. Acta Mater. 2019, 181, 110–123. [CrossRef]
48. Tréglia, G.; Legrand, B.; Ducastelle, F.; Sa úl, A.; Gallis, C.; Meunier, I.; Mottet, C.; Senhaji, A. Alloy surfaces: Segregation,
reconstruction and phase transitions. Comput. Mater. Sci. 1999, 15, 196–235. [CrossRef]
49. Tsuru, T.; Suzudo, T. First-principles calculations of interaction between solutes and dislocations in tungsten. Nucl. Mater. Energy
2018, 16, 221–225. [CrossRef]

## Page 14

Metals 2022, 12, 507 14 of 14
50. Seeger, A.; Veyssiere, P .; Kubin, L.P .; Castaing, J. Dislocations 1984; CNRS: Paris, France, 1984.
51. Brunner, D. Comparison of Flow-Stress Measurements on High-Purity Tungsten Single Crystals with the Kink-Pair Theory.Mater.
T rans. JIM2000, 41, 152–160. [CrossRef]
52. Dudarev, S.L.; Ma, P .-W. Elastic ﬁelds, dipole tensors, and interaction between self-interstitial atom defects in bcc transition metals.
Phys. Rev. Mater. 2018, 2, 033602. [CrossRef]
53. Li, H.; Draxl, C.; Wurster, S.; Pippan, R.; Romaner, L. Impact of d-band ﬁlling on the dislocation properties of bcc transition
metals: The case of tantalum-tungsten alloys investigated by density-functional theory. Phys. Rev. B 2017, 95, 094114. [CrossRef]
54. Hollang, L.; Hommel, M.; Seeger, A. The Flow Stress of Ultra-High-Purity Molybdenum Single Crystals. Phys. Status Solidi 1997,
160, 329–354. [CrossRef]
55. Dezerald, L.; Proville, L.; Ventelon, L.; Willaime, F.; Rodney, D. First-principles prediction of kink-pair activation enthalpy on
screw dislocations in bcc transition metals: V , Nb, Ta, Mo, W, and Fe.Phys. Rev. B 2015, 91, 094105. [CrossRef]
