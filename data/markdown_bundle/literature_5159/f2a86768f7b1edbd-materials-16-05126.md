# materials-16-05126

<!-- source: D:\总文献\materials-16-05126.pdf -->
<!-- file_sha256: b17e285b8d00918c71070ecf248fa06d5e351906cca1035be0bf33455859d469 -->

## Page 1

Citation: Wang, J.; Ma, Q.; Cheng, H.;
Yu, H.; Zhang, S.; Shang, H.; Zhang,
G.; Wang, W. Investigation of the
Micromechanical Behavior of a
Ti68Nb7Ta3Zr4Mo18 (at.%)
High-Entropy Alloy. Materials 2023,
16, 5126. https://doi.org/10.3390/
ma16145126
Academic Editor: Alexander J.
G. Lunt
Received: 21 June 2023
Revised: 11 July 2023
Accepted: 17 July 2023
Published: 20 July 2023
Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
materials
Article
Investigation of the Micromechanical Behavior of a
Ti68Nb7Ta3Zr4Mo18 (at.%) High-Entropy Alloy
Jin Wang 1,2, *, Qianli Ma 1, Hepeng Cheng 1, Hechun Yu 1, Suxiang Zhang 1, Huichao Shang 1, Guoqing Zhang 1
and Wenbo Wang 1
1 School of Mechatronics Engineering, Zhongyuan University of Technology, Zhengzhou 450007, China;
2021104101@zut.edu.cn (Q.M.); 2021104099@zut.edu.cn (H.C.); yuhechun1106@126.com (H.Y.);
3968@zut.edu.cn (S.Z.); sh_hc@126.com (H.S.); zgq@zut.edu.cn (G.Z.); wwb@zut.edu.cn (W.W.)
2 School of Mechanical and Transportation Engineering, Hunan University, Changsha 410082, China
* Correspondence: 6722@zut.edu.cn
Abstract: Intense research efforts are focused on the development of advanced high-entropy alloys
intended for premium aerospace components and other applications, where high strength and good
formability are crucial. The mechanical properties of these alloys are closely related to the phase
transformation, dislocation evolution, and grain size, and these factors are affected by the deformation
temperature. The response of the retained austenite to strain-induced martensitic transformation
at various temperatures was studied in an advanced Ti68Nb7Ta3Zr4Mo18 (at.%) high-entropy alloy
via molecular dynamics simulation. It was found that the Ti68Nb7Ta3Zr4Mo18 alloy changes from a
single crystal to a polycrystal during the tensile process, and the transition of the Ti68Nb7Ta3Zr4Mo18
(at.%) high-entropy alloy from the BCC phase to the FCC phase occurs. At high temperatures and
low strain rates, grain boundary slip is the main deformation mechanism, and at low temperatures
and high strain rates, dislocation slip replaces grain boundary slip as the dominant deformation
mechanism, which improves the strength of the alloy. Moreover, when the grain size is too small, the
strength of the alloy decreases, which does not satisfy the ﬁne grain strengthening theory and shows
an inverse Hall–Petch relationship. This study offers a new compositional window for the additive
manufactured lightweight high-strength material categories for various applications including the
aerospace industry.
Keywords: high-entropy alloy; molecular dynamics; dislocation evolution; strain rate; grain size
1. Introduction
High-entropy alloys (HEAs) were ﬁrst proposed and named in 2004 [1]. It is generally
believed that high-entropy alloys have four major effects: a high-entropy effect in thermo-
dynamics, a hysteresis diffusion effect in dynamics, a lattice distortion effect in structure,
and a “cocktail” effect in performance. Multiple principal elements have led to higher
mixing entropy, which can inhibit segregation and even the combination of elements, thus
promoting the formation of solid solutions of single FCC, BCC, and HCP phases [ 2–4].
Due to the diffusion-activated energy and interatomic binding force of different principal
element atoms, these factors hinder the diffusion of atoms, making high-entropy alloys
stable in a wide temperature range. In addition, the difference in atomic size will inevitably
lead to more or less lattice distortion of the alloy, thus affecting its mechanical properties.
Finally, the characteristics of different principal elements will interact with each other and
inﬂuence each other to develop a synergistic performance effect. Compared to traditional
metals, HEAs have excellent mechanical, chemical, and thermal properties, which are
intended for premium aerospace components and other applications [5–10].
The excellent properties of HEAs have aroused the research interest of many scholars,
from theory to experiments and molecular dynamics simulation. Taking into account
Materials 2023, 16, 5126. https://doi.org/10.3390/ma16145126 https://www.mdpi.com/journal/materials

## Page 2

Materials 2023, 16, 5126 2 of 12
the effect of strain rate, Li et al. conducted tensile simulations on an AlCrFeCuNi alloy
and a CoNiFeAlCu alloy to study the mechanical properties of the alloys and the main
mechanism of plastic deformation. The results showed that the AlCrFeCuNi alloy had not
only high strength but also good plasticity. With the increase in strain, the AlCrFeCuNi alloy
produced dislocation and stratiﬁcation. Dislocation slip twins were the main deformation
mechanism of the AlCrFeCuNi high-entropy alloy. Due to severe lattice distortion and
high local strain, the CoNiFeAlCu alloy induced a phase transition from FCC to BCC. This
phase transition mechanism can make the CoNiFeAlCu alloy obtain high ductility and
high strength at the same time. In addition, this phase transition is mainly affected by the
strain rate [11,12]. Geantă prepared an AlCrxFeCoNi (x = 0.2~2.0 at.%) high-entropy alloy
with different Cr content and studied its microstructure and mechanical properties. The
results showed that the content of Cr had an inﬂuence on the microstructure, grain size, and
microhardness of the high-entropy alloy. With the change in Cr content, the microhardness
changed from 389.6 to 562.6 HV 0.1 [13]. Temperature also affects the properties of high-
entropy alloys. Nutor et al. designed a face-centered cubic/B2 dual-phase HEA based
on CoNiV by adjusting the composition and reported that the HEA maintained excellent
strength–ductility synergism in a wide temperature range due to a variety of deformation
mechanisms [14]. The stress and super-elasticity of high-entropy alloys with shape memory
functions, such as NiTiHfPd, FeMnAlNi, etc., can also be affected by special temperature
values [15,16]. In recent years, the properties of BCC phase high-entropy alloys with
principal elements concentrated in refractory elements such as Ti, Zr, Ta, and Nb have been
reported. These elements have the characteristics of thermal stability and high-temperature
strength, and the density of the elements is low. Cr and Mo can improve the hardness and
strength of the alloy, Ti can improve the plasticity and oxidation resistance of the alloy, and
Zr can give consideration to both plasticity and strength; in addition, Zr can lead to the
transformation of the phase structure of the alloy to diversiﬁcation [17,18]. For example,
the TaNbTaZrMo HEA has excellent yield strength and good biocompatibility, and the PBS
medium showed excellent corrosion resistance comparable to Ti6Al4V , with a hardness and
elastic modulus of 4.9GPa and 153GPa, respectively. The fracture mode and morphology of
the alloy at room temperature show typical brittleness and ﬁnite plasticity [19]. In addition,
the Mo element has a solid solution hardening effect, and its microhardness linearly scales
with the Mo concentration, with an increase of ∼53% from 3.2 GPa to 4.9 GPa in the range
of 0∼20 at.% Mo and an increment of 84 MPa per unit at.% Mo. This indicates that the
Mo atoms generate a signiﬁcant solid-solution hardening (SSH) effect on the quaternary
TiZrNbTa alloy. The hardness and elastic modulus of the TiZrNbTaMox high-entropy alloy
increase linearly with the concentration of the Mo element (0 ≤ x ≤ 20), while the ductility
of the alloy decreases. When the concentration of the Mo element is 20%, the alloy has
good corrosion resistance [20,21]. However, the inﬂuence of temperature and strain rate on
the properties of the TiNbTaZrMo high-entropy alloy is still limited.
Thus, this research focuses on an HEA with Ti, Nb, Ta, Zr, and Mo, among which
Ti, Nb, Ta, and Zr all have the function of improving the plasticity and ductility of the
HEA. In addition, Ti and Zr are isomorphic in the solid state at room temperature, and Nb
and Ta are also isomorphic; they have inﬁnite compatibility and can be well fused. Mo
can improve the hardness of HEAs. In order to maintain the hardness of the HEA while
improving the plasticity, a Ti68Nb7Ta3Zr4Mo18 (at.%) HEA was chosen and simulated to
obtain the effects of temperature, strain rate, and grain size on the mechanical properties of
the Ti68Nb7Ta3Zr4Mo18 HEA. Moreover, the transformation process and deformation mech-
anism of the Ti68Nb7Ta3Zr4Mo18 (at.%) high-entropy alloy were also explored. This study
will provide theoretical guidance for improving the service performance and structural
regulation of HEAs.
2. Potential Functions and Simulation Methods
Molecular dynamics simulations use potential functions to describe the interactions
between atoms, and the accuracy of the potential functions determines the correctness of

## Page 3

Materials 2023, 16, 5126 3 of 12
the results. At present, among the potential functions of metal elements, the embedded
atom method (EAM) has been studied earlier and used more maturely. In this paper, the
ﬁtting potential function program developed by Zhou et al. was used to ﬁt the required
EAM potential function, and LAMMPS open-source code was used for all simulations [22].
Considering whether the ﬁtting potential function is suitable for the alloy system, the
potential function is veriﬁed by LAMMPS simulation of the average lattice constant, the
melting point of the alloy, and X-ray diffraction (XRD) compared with the experiment. As
shown in Figure 1a, the corresponding energy is the lowest when the lattice constant is
3.27 Å. In Figure 1b, the temperature corresponding to the sudden change in potential
energy is the melting point, namely, 2500 K. Figure 1c shows the XRD experiment, simula-
tion, and comparison of the diffraction pattern of the IDCC ﬁle numbered PDF-65-9438.
The diffraction angles of each diffraction peak and the peak surface index are consistent.
According to the systematic extinction law of X-ray diffraction, the BCC structure material
will generate diffraction when the peak surface indices h, k, and l are added to an even
number. The peak surface index of each diffraction peak of the high-entropy alloy is even,
so the main structure of the high-entropy alloy is BCC. In addition, the ﬁrst diffraction peak
matches PDF-65-9438 well, and its phase is a TiNb compound. The above three groups of
data show little difference from the measured values of Wang et al. [19].
Materials 2023, 16, x FOR PEER REVIEW 4 of 12 
 
 
 
Figure 1. (a) Cohesion energy–la ttice constant curve; ( b) potential energy temperature curve; and 
(c) X-ray diﬀraction pattern. 
 
Figure 2. The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model: (a) atomic type and (b) CNA. 
3. Result 
3.1. Mechanical Properties 
The stress–strain curves of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA stretched at di ﬀerent 
temperatures and strain rates are shown in Fi gure 3. The elastic modulus E of the alloy 
with high entropy can be obtained by ﬁtting the slope of the 0–0.05 strain segment in the 
stress–strain curve. It can be seen from Figure 3 that the strain segments of curves from 0 
to 0.05 basically coincide at the same temperature, so increasing the strain rate has no 
Figure 1. (a) Cohesion energy–lattice constant curve; (b) potential energy temperature curve; and
(c) X-ray diffraction pattern.
LAMMPS was used to construct the BCC structural model as shown in Figure 2. The
size of the model was 30a× 30a × 30a, and ﬁve kinds of atoms (Ti, Nb, Ta, Zr, and Mo) were
randomly assigned in proportion to the model, which contained a total of 54,000 atoms. To
avoid the scale effect, the X, Y, and Z directions of the model were set as periodic boundary
conditions (P P P). Conjugate gradient methods (CG) were used to minimize the energy

## Page 4

Materials 2023, 16, 5126 4 of 12
of the model, and the model relaxed 50fs under isothermal and isobaric NPT. Finally, the
model was stretched by 0.35 strains along the Y direction at different temperatures (77, 300,
700, and 1000 K) and strain rates (1 × 109 s−1, 5 × 109 s−1, 1 × 1010 s−1, 3 × 1010 s−1, and
5 × 1010 s−1). The whole process is completed in an isothermal isovolumic ensemble NVT.
Ovito (3.8.5) software can visualize the simulation results. Common neighbor analysis
(CNA) can distinguish the atomic structure, and the dislocation extraction algorithm (DXA)
can track the dislocation motion [23].
Materials 2023, 16, x FOR PEER REVIEW 4 of 12 
 
 
 
Figure 1. (a) Cohesion energy–la ttice constant curve; ( b) potential energy temperature curve; and 
(c) X-ray diﬀraction pattern. 
 
Figure 2. The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model: (a) atomic type and (b) CNA. 
3. Result 
3.1. Mechanical Properties 
The stress–strain curves of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA stretched at di ﬀerent 
temperatures and strain rates are shown in Fi gure 3. The elastic modulus E of the alloy 
with high entropy can be obtained by ﬁtting the slope of the 0–0.05 strain segment in the 
stress–strain curve. It can be seen from Figure 3 that the strain segments of curves from 0 
to 0.05 basically coincide at the same temperature, so increasing the strain rate has no 
Figure 2. The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model: (a) atomic type and (b) CNA.
3. Result
3.1. Mechanical Properties
The stress–strain curves of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA stretched at different
temperatures and strain rates are shown in Figure 3. The elastic modulus E of the alloy
with high entropy can be obtained by ﬁtting the slope of the 0–0.05 strain segment in the
stress–strain curve. It can be seen from Figure 3 that the strain segments of curves from
0 to 0.05 basically coincide at the same temperature, so increasing the strain rate has no
obvious effect on the elastic modulus of the HEA. The effect of the strain rate on the ultimate
strength of the HEA is obvious, and the ultimate strength increases with the increase in
the strain rate. The stress–strain curve has the same trend as the strain rate at different
temperatures. When the strain rate was 1 × 109 s−1 and the strain was 0.1, the curves all
showed a downward change. With the increase in the strain, the curves continued to rise.
After reaching the ultimate strength, the curves dropped rapidly. When the strain rate is
increased, the curve does not decrease at 0.1 strain, but the rising rate of the curve after
0.1 strain ﬁrst decreases and then increases. When the strain rate increases to 5 × 1010 s−1,
the curve keeps rising steadily. In addition, the higher the strain rate, the slower the curve
declines after reaching the ultimate strength. Figure 4 shows the changes in the elastic
modulus and ultimate strength with the strain rate at different temperatures. It can be seen
that temperature has a great inﬂuence on the properties of the Ti68Nb7Ta3Zr4Mo18 (at.%)
HEA. With the increase in temperature, the elastic modulus and ultimate strength of the
high-entropy alloy decrease obviously due to the softening effect of the high temperature.
As shown in Figure 4a, with the increase in the strain rate, each curve had an upward trend,
but the rise was slow, and the change in the elastic modulus was not obvious with the
increase in the strain rate. As shown in Figure 4b, with the increase in the strain rate, the
change in each curve was obvious, and the ultimate strength increased signiﬁcantly. The
ultimate strength decreases when the strain rate increases from 5 × 109 s−1 to 1 × 1010 s−1
at 77 K and 300 K, but it is still larger than that at 1 × 109 s−1. On the whole, there is a

## Page 5

Materials 2023, 16, 5126 5 of 12
positive correlation between the ultimate strength and the strain rate. The elastic modulus
E of the high-entropy alloy is 116.7 GPa at 300 K and the 1 × 1010 s−1 strain rate and the
elastic modulus of the TiNbTaZrMo HEA is 153 GPa in the experiment. This is mainly
caused by the different content of the Ti element. In this paper, the atomic concentration of
Ti in the high-entropy alloy is about 68% [24].
Materials 2023, 16, x FOR PEER REVIEW 5 of 12 
 
 
obvious eﬀect on the elastic modulus of the HEA. The e ﬀect of the strain rate on the ulti-
mate strength of the HEA is obvious, and the ultimate strength increases with the increase 
in the strain rate. The stress–strain curve has the same trend as the strain rate at di ﬀerent 
temperatures. When the strain rate was 1 × 10 9 s−1 and the strain was 0.1, the curves all 
showed a downward change. With the increase in the strain, the curves continued to rise. 
After reaching the ultimate strength, the curves dropped rapidly. When the strain rate is 
increased, the curve does not decrease at 0.1 strain, but the rising rate of the curve after 
0.1 strain ﬁrst decreases and then increases. When the strain rate increases to 5 × 10 10 s−1, 
the curve keeps rising steadily. In addition, the higher the strain rate, the slower the curve 
declines after reaching the ultimate strength . Figure 4 shows the changes in the elastic 
modulus and ultimate strength with the strain rate at di ﬀerent temperatures. It can be 
seen that temperature has a great in ﬂuence on the properties of the Ti 68Nb7Ta3Zr4Mo18 
(at.%) HEA. With the increase in temperature, the elastic modulus and ultimate strength 
of the high-entropy alloy decrease obviously due to the softening e ﬀect of the high tem-
perature. As shown in Figure 4a, with the increase in the strain rate, each curve had an 
upward trend, but the rise was slow, and the change in the elastic modulus was not obvi-
ous with the increase in the strain rate. As shown in Figure 4b, with the increase in the 
strain rate, the change in each curve was obvious, and the ultimate strength increased 
signiﬁcantly. The ultimate strength decreases wh en the strain rate increases from 5 × 10
9 
s−1 to 1 × 1010 s−1 at 77 K and 300 K, but it is still larger than that at 1 × 109 s−1. On the whole, 
there is a positive correlation between the ultimate strength and the strain rate. The elastic 
modulus E of the high-entropy alloy is 116.7 GPa at 300 K and the 1 × 10 10 s−1 strain rate 
and the elastic modulus of the TiNbTaZrMo HEA is 153 GPa in the experiment. This is 
mainly caused by the diﬀerent content of the Ti element. In this paper, the atomic concen-
tration of Ti in the high-entropy alloy is about 68% [24]. 
 
Figure 3. Stress–strain curves of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA at di ﬀerent temperatures (77, 
300, 700, and 1000 K) and strain rates (1 × 109 s−1, 5 × 109 s−1, 1 × 1010 s−1, 3 × 1010 s−1, and 5 × 1010 s−1). (a) 
Stress-strain curves of 77 K at diﬀerent strain rates; (b) Stress-strain curves of 300K at diﬀerent strain 
rates; (c) Stress–strain curves of 700 K at di ﬀerent strain rates; (d) Stress–strain curves of 1000 K at 
diﬀerent strain rates. 
Figure 3. Stress–strain curves of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA at different temperatures
(77, 300, 700, and 1000 K) and strain rates (1 × 109 s−1, 5 × 109 s−1, 1 × 1010 s−1, 3 × 1010 s−1, and
5 × 1010 s−1). ( a) Stress-strain curves of 77 K at different strain rates; ( b) Stress-strain curves of
300 K at different strain rates; (c) Stress–strain curves of 700 K at different strain rates; (d) Stress–strain
curves of 1000 K at different strain rates.
Materials 2023, 16, x FOR PEER REVIEW 6 of 12 
 
 
 
Figure 4. (a) Curves of elastic modulus with the strain rate at diﬀerent temperatures and (b) curves 
of ultimate strength with the strain rate at diﬀerent temperatures. 
3.2. Deformation Behavior 
The diﬀerent atomic structures in Ti68Nb7Ta3Zr4Mo18 (at.%) HEA crystals can be clas-
siﬁed and colored by common neighbor analysis visualization. Figure 5 is a snapshot of 
the structural changes of the high-entropy alloy during the tensile process at the 1 × 10 10 
s−1 strain rate at a temperature of 300 K. Green, blue, and red represent the FCC, BCC, and 
HCP structures, respectively, and white represents atoms that do not satisfy any of the 
basic structures. It is well known that a single layer composed of HCP atoms means a twin 
boundary (TB), and a double layer of HCP mean s stacking faults (SFs). The structure of 
high-entropy alloy changes with the increase in the tensile load. As shown in Figure 5b–
e, the initial BCC structure of the high-entropy alloy is transformed into an FCC structure, 
accompanied by a crisscross HCP structure and disordered white atoms. With the increase 
in strain, the HCP structures gradually increase and fuse with BCC phase boundaries, as 
shown in the black dotted line in Figure 5d. When stretched to 0.2 strain, almost all of the 
BCC phase was transformed into the FCC phase, and twins appeared in the black line art 
of Figure 5e. When the tensile load continues to be applied, the high-entropy alloy gener-
ates a cavity at the grain boundary and fractu res, as shown in Figure 5f. Therefore, the 
grain of the high-entropy alloy also changes during the tensile process. In Figure 5a, it can 
be seen more directly that the FCC structure increases rapidly at the expense of the BCC 
structure. At 0.2 strain, the FCC structure reaches its maximum cont ent, accounting for 
about 51%. As the tension continues, the hollow formed by the high-entropy alloy gradu-
ally increases. Figure 6 is a snapshot of the failure of the high-entropy alloy, and there is 
a certain adhesion on the (001) crystal plane. It can be seen that this type of fracture is 
more like the dimple produced when the plastic fracture occurs, so this high-entropy alloy 
has a certain degree of toughness. 
Figure 4. (a) Curves of elastic modulus with the strain rate at different temperatures and (b) curves
of ultimate strength with the strain rate at different temperatures.

## Page 6

Materials 2023, 16, 5126 6 of 12
3.2. Deformation Behavior
The different atomic structures in Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA crystals can be
classiﬁed and colored by common neighbor analysis visualization. Figure 5 is a snap-
shot of the structural changes of the high-entropy alloy during the tensile process at the
1 × 1010 s−1 strain rate at a temperature of 300 K. Green, blue, and red represent the FCC,
BCC, and HCP structures, respectively, and white represents atoms that do not satisfy any
of the basic structures. It is well known that a single layer composed of HCP atoms means
a twin boundary (TB), and a double layer of HCP means stacking faults (SFs). The structure
of high-entropy alloy changes with the increase in the tensile load. As shown in Figure 5b–e,
the initial BCC structure of the high-entropy alloy is transformed into an FCC structure,
accompanied by a crisscross HCP structure and disordered white atoms. With the increase
in strain, the HCP structures gradually increase and fuse with BCC phase boundaries, as
shown in the black dotted line in Figure 5d. When stretched to 0.2 strain, almost all of the
BCC phase was transformed into the FCC phase, and twins appeared in the black line art of
Figure 5e. When the tensile load continues to be applied, the high-entropy alloy generates
a cavity at the grain boundary and fractures, as shown in Figure 5f. Therefore, the grain of
the high-entropy alloy also changes during the tensile process. In Figure 5a, it can be seen
more directly that the FCC structure increases rapidly at the expense of the BCC structure.
At 0.2 strain, the FCC structure reaches its maximum content, accounting for about 51%.
As the tension continues, the hollow formed by the high-entropy alloy gradually increases.
Figure 6 is a snapshot of the failure of the high-entropy alloy, and there is a certain adhesion
on the (001) crystal plane. It can be seen that this type of fracture is more like the dimple
produced when the plastic fracture occurs, so this high-entropy alloy has a certain degree
of toughness.
Materials 2023, 16, x FOR PEER REVIEW 7 of 12 
 
 
 
Figure 5. Structural snapshot of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA at di ﬀerent strains during the 
tensile process ((a): The proportion of individual structures in the tensile process; (b): ε = 0.05; (c): ε 
= 0.10; (d): ε = 0.15; (e): ε = 0.20; (f): ε = 0.25). 
 
Figure 6. Snapshot of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA after stretching ((a) (100) and (b) (001) crys-
tal face). 
In order to reveal the in ﬂuence of temperature and strain rate on the deformation 
mechanism of the high-entropy alloy, the structural changes and dislocation evolution of 
the high-entropy alloy under diﬀerent tensile conditions were studied. After stretching to 
ultimate strength, the structure and dislocation of the high-entropy alloy at 77 K and 1000 
K temperatures are shown in Figure 7a–d,e–h, respectively. It can be seen that the defor-
mation of the high-entropy alloy is mainly divided into grain boundary slip and disloca-
tion slip. When the temperature rises, the atoms inside the alloy move violently, and some 
atoms at the grain boundaries break away from their original positions and become dis-
ordered, resulting in grain boundary damage, as shown in the black dotted line in Figure 
7c,d. In addition, there are some di ﬀerences in dislocation density
 at diﬀerent tempera-
tures and strain rates. At 77 K, the dislocation densities of 1 × 109 s−1 and 1 × 1010 s−1 are 4.6 
× 1017 m−2 and 5 × 1017 m−2, respectively. At 1000 K temperature, the dislocation densities of 
1 × 10 9 s−1 and 1 × 10 10 s−1 are 2.5 × 10 16 m−2 and 1 × 10 17 m−2, respectively. The green line 
represents 1/6[1 1 2] Shockley, yellow represents 1/3[1 0 0] Hirth, and red represents the 
other. It is clear that the main type of dislocation in the alloy is Shockley dislocation, which 
is a continuous long dislocation at low temp eratures and a discrete short dislocation at 
high temperatures. Dislocations occur mainly within the grain, and most remain parallel 
Figure 5. Structural snapshot of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA at different strains during the
tensile process (( a): The proportion of individual structures in the tensile process; ( b): ε = 0.05;
(c): ε = 0.10; (d): ε = 0.15; (e): ε = 0.20; (f): ε = 0.25).

## Page 7

Materials 2023, 16, 5126 7 of 12
Materials 2023, 16, x FOR PEER REVIEW 7 of 12 
 
 
 
Figure 5. Structural snapshot of the Ti 68Nb7Ta3Zr4Mo18 (at.%) HEA at di ﬀerent strains during the 
tensile process ((a): The proportion of individual structures in the tensile process; (b): ε = 0.05; (c): ε 
= 0.10; (d): ε = 0.15; (e): ε = 0.20; (f): ε = 0.25). 
 
Figure 6. Snapshot of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA after stretching ((a) (100) and (b) (001) crys-
tal face). 
In order to reveal the in ﬂuence of temperature and strain rate on the deformation 
mechanism of the high-entropy alloy, the structural changes and dislocation evolution of 
the high-entropy alloy under diﬀerent tensile conditions were studied. After stretching to 
ultimate strength, the structure and dislocation of the high-entropy alloy at 77 K and 1000 
K temperatures are shown in Figure 7a–d,e–h, respectively. It can be seen that the defor-
mation of the high-entropy alloy is mainly divided into grain boundary slip and disloca-
tion slip. When the temperature rises, the atoms inside the alloy move violently, and some 
atoms at the grain boundaries break away from their original positions and become dis-
ordered, resulting in grain boundary damage, as shown in the black dotted line in Figure 
7c,d. In addition, there are some di ﬀerences in dislocation density
 at diﬀerent tempera-
tures and strain rates. At 77 K, the dislocation densities of 1 × 109 s−1 and 1 × 1010 s−1 are 4.6 
× 1017 m−2 and 5 × 1017 m−2, respectively. At 1000 K temperature, the dislocation densities of 
1 × 10 9 s−1 and 1 × 10 10 s−1 are 2.5 × 10 16 m−2 and 1 × 10 17 m−2, respectively. The green line 
represents 1/6[1 1 2] Shockley, yellow represents 1/3[1 0 0] Hirth, and red represents the 
other. It is clear that the main type of dislocation in the alloy is Shockley dislocation, which 
is a continuous long dislocation at low temp eratures and a discrete short dislocation at 
high temperatures. Dislocations occur mainly within the grain, and most remain parallel 
Figure 6. Snapshot of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA after stretching (( a) (100) and ( b) (001)
crystal face).
In order to reveal the inﬂuence of temperature and strain rate on the deformation
mechanism of the high-entropy alloy, the structural changes and dislocation evolution of
the high-entropy alloy under different tensile conditions were studied. After stretching
to ultimate strength, the structure and dislocation of the high-entropy alloy at 77 K and
1000 K temperatures are shown in Figure 7a–d,e–h, respectively. It can be seen that the
deformation of the high-entropy alloy is mainly divided into grain boundary slip and
dislocation slip. When the temperature rises, the atoms inside the alloy move violently,
and some atoms at the grain boundaries break away from their original positions and
become disordered, resulting in grain boundary damage, as shown in the black dotted line
in Figure 7c,d. In addition, there are some differences in dislocation density at different
temperatures and strain rates. At 77 K, the dislocation densities of 1 × 109 s−1 and
1 × 1010 s−1 are 4.6 × 1017 m−2 and 5 × 1017 m−2, respectively. At 1000 K temperature, the
dislocation densities of 1 × 109 s−1 and 1 × 1010 s−1 are 2.5 × 1016 m−2 and 1 × 1017 m−2,
respectively. The green line represents 1/6[1 1 2] Shockley, yellow represents 1/3[1 0 0]
Hirth, and red represents the other. It is clear that the main type of dislocation in the alloy
is Shockley dislocation, which is a continuous long dislocation at low temperatures and a
discrete short dislocation at high temperatures. Dislocations occur mainly within the grain,
and most remain parallel to each other. The grain boundary has a certain hindrance effect
on the dislocation slip, so at the grain boundary, the dislocations accumulate and wrap
to form dislocation nodes, as shown in the black coils in Figure 7e,f. With the increase in
the strain rate, the length of the dislocation line increases, more dislocation entanglement
occurs at the grain boundary, and the dislocation density increases. At high temperatures,
the phenomenon of dislocation entanglement is not obvious, but the length and density of
the dislocation line increase signiﬁcantly, as shown in Figure 7g,h.
3.3. The Effect of Grain Size on the Mechanical Properties
When the strain rate of 300 K is 1× 1010 s−1, the monocrystalline is transformed into
polycrystalline in addition to molecular structure transformation. In order to study the effect
of grain size on the mechanical properties, the V oronoi structure method was used to modify
the model [25,26], as shown in Figure 8a–d. All the models were 10× 10 × 10 nm3 in size
and contained different quantities of randomly oriented particles, which were controlled
by this method. Figure 8e shows the stress–strain curve of the HEA after the tensile process.
It can be seen that in the strain 0–0.05 stage, the rate of curve rise is different, so the elastic
modulus is affected by the grain size. When the number of grains increases, the grain size
decreases, and the elastic modulus also decreases. When the strain reaches about 0.15,
the alloy with high entropy reaches the ultimate strength. The ultimate strength of the
alloy with the number of grains at 4 is the highest, the ultimate strength of the alloy with
the number of grains at 2 is only second, and the ultimate strength of the alloy with the

## Page 8

Materials 2023, 16, 5126 8 of 12
number of grains at 6 and 8 is the lowest and basically the same. Generally, ﬁne grain
strengthening can be expressed by the Hall–Petch relationship, that is, the strength of the
material is inversely proportional to the grain size. It is obvious that the appeal result does
not fully satisfy this relationship. When the grain size is reduced to a certain extent, the
inverse Hall–Petch phenomenon appears [27].
Materials 2023, 16, x FOR PEER REVIEW 8 of 12 
 
 
to each other. The grain boundary has a certain hindrance eﬀect on the dislocation slip, so 
at the grain boundary, the dislocations accumulate and wrap to form dislocation nodes, 
as shown in the black coils in Figure 7e,f. With the increase in the strain rate, the length of 
the dislocation line increases, more dislocation entanglement occurs at the grain bound-
ary, and the dislocation density increases. At high temperatures, the phenomenon of dis-
location entanglement is not obvious, but the length and density of the dislocation line 
increase signiﬁcantly, as shown in Figure 7g,h. 
 
Figure 7. Structural distribution and dislocation distribution under different tensile conditions (a,e) 77 
K and 1 × 109 s−1, (b,f) 77 K and 1 × 1010 s−1, (c,g) 1000 K and 1 × 109 s−1, and (d,h) 1000 K and 1 × 1010 s−1. 
3.3. The Eﬀect of Grain Size on the Mechanical Properties 
When the strain rate of 300 K is 1 × 10 10 s−1, the monocrystalline is transformed into 
polycrystalline in addition to molecular stru cture transformation. In order to study the 
eﬀect of grain size on the mechanical properties, the Voronoi structure method was used 
to modify the model [25,26], as shown in Figure 8a–d. All the models were 10 × 10 × 10 
nm3 in size and contained diﬀerent quantities of randomly oriented particles, which were 
controlled by this method. Figure 8e shows the stress–strain curve of the HEA after the 
tensile process. It can be seen that in the strain 0–0.05 stage, the rate of curve rise is diﬀer-
ent, so the elastic modulus is a ﬀected by the grain size. When the number of grains in-
creases, the grain size decreases, and the elastic modulus also decreases. When the strain 
reaches about 0.15, the alloy with high entropy reaches the ultimate strength. The ultimate 
strength of the alloy with the number of grains at 4 is the highest, the ultimate strength of 
the alloy with the number of grains at 2 is only second, and the ultimate strength of the 
alloy with the number of grains at 6 and 8 is the lowest and basically the same. Generally, 
ﬁne grain strengthening can be expressed by the Hall–Petch relationship, that is, the 
strength of the material is inversely proportion al to the grain size. It is obvious that the 
appeal result does not fully satisfy this relationship. When the grain size is reduced to a 
certain extent, the inverse Hall–Petch phenomenon appears [27]. 
Figure 7. Structural distribution and dislocation distribution under different tensile conditions
(a,e) 77 K and 1 × 109 s−1, (b,f) 77 K and 1 × 1010 s−1, (c,g) 1000 K and 1 × 109 s−1, and (d,h) 1000 K
and 1 × 1010 s−1.
Materials 2023, 16, x FOR PEER REVIEW 9 of 12 
 
 
 
Figure 8. HEA model with a diﬀerent number of grains. Grain number: (a) 2, (b) 4, (c) 6, and (d) 8. 
(e) Stress–strain curves. 
In order to further investigate the cause of the inverse Hall–Petch phenomenon, a 
snapshot of the grain and dislocation with the tensile strain of the high-entropy alloy at 
0.15 was taken, as shown in Figure 9. After stretching, the number of grains increases fur-
ther, and the grain size becomes smaller. For dislocation, in high-entropy alloys with rel-
atively large grain sizes, dislocation lines are denser and longer, and entanglement to form 
dislocation knots is more likely, as shown in Figure 9e. However, in the high-entropy alloy 
with a relatively small grain size, the length of the dislocation line is shorter and there is 
not much winding, forming a discrete state di stribution, as shown in Figure 9e–h. In ad-
dition, a small number of 1/6[1 1 0] stair-rod dislocations occur in polycrystalline stretch-
ing compared to single-crystal stretching. 
 
Figure 9. HEA structure and dislocation with diﬀerent grains at 0.15 tensile strain: (a–d) HEA struc-
ture and (e–h) HEA dislocation. 
4. Discussion 
The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model underwent BCC–FCC phase transition in 
uniaxial Y-axis stretching along the NVT system, which is somewhat di ﬀerent from the 
single crystal Fe model studied by Ma et al. [28], which underwent BCC–FCC phase tran-
sition under uniaxial compression along the X-axis. During the stretching process, the 
transition from BCC to FCC is divided into two stages. First, under tensile load, the BCC 
close-packed surface atoms change from “ ABABAB” stacking mode to “ ABCABCABC” 
stacking mode, as shown in Figure 10c,d, and the la ttice angle changes from 90° to 70.5°. 
Then, the atoms in the BCC close-packed surface rearrange, and the lattice Angle becomes 
60°, as shown in Figure 10e,f. Therefore, the BCC structure is transformed into an FCC 
Figure 8. HEA model with a different number of grains. Grain number: (a) 2, (b) 4, (c) 6, and (d) 8.
(e) Stress–strain curves.
In order to further investigate the cause of the inverse Hall–Petch phenomenon, a
snapshot of the grain and dislocation with the tensile strain of the high-entropy alloy at
0.15 was taken, as shown in Figure 9. After stretching, the number of grains increases
further, and the grain size becomes smaller. For dislocation, in high-entropy alloys with
relatively large grain sizes, dislocation lines are denser and longer, and entanglement to
form dislocation knots is more likely, as shown in Figure 9e. However, in the high-entropy
alloy with a relatively small grain size, the length of the dislocation line is shorter and
there is not much winding, forming a discrete state distribution, as shown in Figure 9e–h.
In addition, a small number of 1/6[1 1 0] stair-rod dislocations occur in polycrystalline
stretching compared to single-crystal stretching.

## Page 9

Materials 2023, 16, 5126 9 of 12
Materials 2023, 16, x FOR PEER REVIEW 9 of 12 
 
 
 
Figure 8. HEA model with a diﬀerent number of grains. Grain number: (a) 2, (b) 4, (c) 6, and (d) 8. 
(e) Stress–strain curves. 
In order to further investigate the cause of the inverse Hall–Petch phenomenon, a 
snapshot of the grain and dislocation with the tensile strain of the high-entropy alloy at 
0.15 was taken, as shown in Figure 9. After stretching, the number of grains increases fur-
ther, and the grain size becomes smaller. For dislocation, in high-entropy alloys with rel-
atively large grain sizes, dislocation lines are denser and longer, and entanglement to form 
dislocation knots is more likely, as shown in Figure 9e. However, in the high-entropy alloy 
with a relatively small grain size, the length of the dislocation line is shorter and there is 
not much winding, forming a discrete state di stribution, as shown in Figure 9e–h. In ad-
dition, a small number of 1/6[1 1 0] stair-rod dislocations occur in polycrystalline stretch-
ing compared to single-crystal stretching. 
 
Figure 9. HEA structure and dislocation with diﬀerent grains at 0.15 tensile strain: (a–d) HEA struc-
ture and (e–h) HEA dislocation. 
4. Discussion 
The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model underwent BCC–FCC phase transition in 
uniaxial Y-axis stretching along the NVT system, which is somewhat di ﬀerent from the 
single crystal Fe model studied by Ma et al. [28], which underwent BCC–FCC phase tran-
sition under uniaxial compression along the X-axis. During the stretching process, the 
transition from BCC to FCC is divided into two stages. First, under tensile load, the BCC 
close-packed surface atoms change from “ ABABAB” stacking mode to “ ABCABCABC” 
stacking mode, as shown in Figure 10c,d, and the la ttice angle changes from 90° to 70.5°. 
Then, the atoms in the BCC close-packed surface rearrange, and the lattice Angle becomes 
60°, as shown in Figure 10e,f. Therefore, the BCC structure is transformed into an FCC 
Figure 9. HEA structure and dislocation with different grains at 0.15 tensile strain: ( a–d) HEA
structure and (e–h) HEA dislocation.
4. Discussion
The Ti68Nb7Ta3Zr4Mo18 (at.%) HEA model underwent BCC–FCC phase transition
in uniaxial Y-axis stretching along the NVT system, which is somewhat different from
the single crystal Fe model studied by Ma et al. [28], which underwent BCC–FCC phase
transition under uniaxial compression along the X-axis. During the stretching process, the
transition from BCC to FCC is divided into two stages. First, under tensile load, the BCC
close-packed surface atoms change from “ABABAB” stacking mode to “ABCABCABC”
stacking mode, as shown in Figure 10c,d, and the lattice angle changes from 90◦ to 70.5◦.
Then, the atoms in the BCC close-packed surface rearrange, and the lattice Angle becomes
60◦, as shown in Figure 10e,f. Therefore, the BCC structure is transformed into an FCC
structure, as shown in Figure 10g. Figure 10a shows the microscopic magniﬁcation of the
BCC and FCC phases at 0.15 strain. The whole phase transition process is similar to the
transition from BCC to FCC studied by Ding et al. and satisﬁes the KS relationship [ 29,30].
Materials 2023, 16, x FOR PEER REVIEW 10 of 12 
 
 
structure, as shown in Figure 10g. Figure 10a shows the microscopic magniﬁcation of the 
BCC and FCC phases at 0.15 strain. The whole phase transition process is similar to the 
transition from BCC to FCC studied by Ding et al. and satisﬁes the KS relationship [29,30]. 
 
Figure 10. Schematic diagram of phase tran sition from BCC to FCC. ( a) Snapshot of the transition 
from BCC to FCC (b) Structure of BCC; (c–f) The transition from BCC to FCC; (g) Structure of FCC. 
As can be seen from the results in Summary I conﬁrm 3.2 of this paper, obvious grain 
boundary slip occurs in the high-entropy alloy at high temperatures. Due to the high tem-
perature, the thermal motion of atoms is intensi ﬁed, and a large number of disordered 
atoms are formed from the original position of atoms, and these disordered atoms are 
mostly concentrated near the crystallization, as shown in Figure 7c,d. At low tempera-
tures, this phenomenon is not obvious, and no large number of disordered atoms are pro-
duced, as shown in Figure 7a,b. However, at low temperatures, a large number of dislo-
cations are generated, which slip within the grain and gather and intertwine at the grain 
boundaries to form dislocation knots, as shown in Figure 7e,f. The strain rate has a great 
inﬂuence on dislocation. By comparing Figure 7e,f (or Figure 7g,h), it can be found that 
more dislocations and entanglement occur at hi gher strain rates. Therefore, at high tem-
peratures, grain boundary slip is more serious and plays a leading role in deformation. At 
low temperatures and high strain rates, dislocation slip is more serious and dominates the 
deformation mechanism. This is consistent with the conclusion of Li et al. [31], who stud-
ied the inﬂuence of temperature and strain rate on the deformation mechanism of high-
entropy alloys. 
It is generally believed that dislocation occurs in the deformation process of materials, 
and dislocations intertwine with each other to form dislocation knots, resulting in increased 
dislocation density and relatively difficult dislocation movement. Because the free travel of 
dislocation movement decreases, the interaction between dislocation hinders the slip move-
ment of dislocation, and the stronger the material resistance to deformation, the higher the 
strength of the material. However, when the grain size is less than a certain degree, it is 
difficult for the dislocation to move within the grain, and the phenomenon of intertwining 
will not appear. In addition, grain boundaries are more likely to break down during defor-
mation due to the small grain size. The above two reasons will lead to the reduction of ma-
terial strength and reverse the Hall–Petch phenomenon at the realization point. 
5. Conclusions 
The micromechanical properties of a Ti
68Nb7Ta3Zr4Mo18 (at.%) HEA were studied by 
the molecular dynamics method, and the eﬀects of temperature, strain rate, and grain size 
on the mechanical properties were considered. The following conclusions were obtained. 
1. High temperatures can soften the alloy and reduce the elastic modulus and ultimate 
strength of the alloy. The strain rate has little eﬀect on the elastic modulus of the high-
entropy alloy but a great e ﬀect on the ultimate strength of the high-entropy alloy, 
that is, the higher the strain rate, the greater the ultimate strength. 
Figure 10. Schematic diagram of phase transition from BCC to FCC. (a) Snapshot of the transition
from BCC to FCC (b) Structure of BCC; (c–f) The transition from BCC to FCC; (g) Structure of FCC.
As can be seen from the results in Summary I conﬁrm 3.2 of this paper, obvious
grain boundary slip occurs in the high-entropy alloy at high temperatures. Due to the
high temperature, the thermal motion of atoms is intensiﬁed, and a large number of
disordered atoms are formed from the original position of atoms, and these disordered
atoms are mostly concentrated near the crystallization, as shown in Figure 7c,d. At low
temperatures, this phenomenon is not obvious, and no large number of disordered atoms
are produced, as shown in Figure 7a,b. However, at low temperatures, a large number of
dislocations are generated, which slip within the grain and gather and intertwine at the

## Page 10

Materials 2023, 16, 5126 10 of 12
grain boundaries to form dislocation knots, as shown in Figure 7e,f. The strain rate has a
great inﬂuence on dislocation. By comparing Figure 7e,f (or Figure 7g,h), it can be found
that more dislocations and entanglement occur at higher strain rates. Therefore, at high
temperatures, grain boundary slip is more serious and plays a leading role in deformation.
At low temperatures and high strain rates, dislocation slip is more serious and dominates
the deformation mechanism. This is consistent with the conclusion of Li et al. [ 31], who
studied the inﬂuence of temperature and strain rate on the deformation mechanism of
high-entropy alloys.
It is generally believed that dislocation occurs in the deformation process of mate-
rials, and dislocations intertwine with each other to form dislocation knots, resulting in
increased dislocation density and relatively difﬁcult dislocation movement. Because the
free travel of dislocation movement decreases, the interaction between dislocation hinders
the slip movement of dislocation, and the stronger the material resistance to deforma-
tion, the higher the strength of the material. However, when the grain size is less than
a certain degree, it is difﬁcult for the dislocation to move within the grain, and the phe-
nomenon of intertwining will not appear. In addition, grain boundaries are more likely to
break down during deformation due to the small grain size. The above two reasons will
lead to the reduction of material strength and reverse the Hall–Petch phenomenon at the
realization point.
5. Conclusions
The micromechanical properties of a Ti68Nb7Ta3Zr4Mo18 (at.%) HEA were studied by
the molecular dynamics method, and the effects of temperature, strain rate, and grain size
on the mechanical properties were considered. The following conclusions were obtained.
1. High temperatures can soften the alloy and reduce the elastic modulus and ultimate
strength of the alloy. The strain rate has little effect on the elastic modulus of the
high-entropy alloy but a great effect on the ultimate strength of the high-entropy alloy,
that is, the higher the strain rate, the greater the ultimate strength.
2. The transition from an FCC structure to a BCC structure occurs during the tensile
process of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA. The main deformation mechanism at
high temperatures is grain boundary slip, while the main deformation mechanism at
low temperatures and high strain rates is dislocation slip.
3. The grain size of the Ti68Nb7Ta3Zr4Mo18 (at.%) HEA is too small due to the internal
dislocation of grain growth and slippage, and with the instability of grain boundaries,
the strength of the alloy will reverse the Hall–Petch law phenomenon.
Author Contributions: Conceptualization, J.W. and H.Y.; methodology, J.W.; software, Q.M., G.Z.
and H.C.; validation, S.Z. and H.S.; formal analysis, Q.M.; investigation, J.W.; resources, H.Y. and
H.S.; data curation, J.W. and W.W.; writing—original draft preparation, Q.M.; writing—review and
editing, J.W.; supervision, H.Y. and H.S.; project administration, J.W.; funding acquisition, H.Y. All
authors have read and agreed to the published version of the manuscript.
Funding: The research was supported by the National Natural Science Foundation of China (51875586);
the Training Program for Young Backbone Teachers in Colleges and Universities of Henan Province,
No.2018GGJS105; and the China National Textile Industry Council (2019067).
Informed Consent Statement: Not applicable.
Data Availability Statement: All data used to support the ﬁndings of this study are included within
the article.
Conﬂicts of Interest: The authors declare that they have no known competing ﬁnancial interest or
personal relationship that could have appeared to have inﬂuenced the work reported in this paper.

## Page 11

Materials 2023, 16, 5126 11 of 12
References
1. Yeh, J.W.; Chen, S.K.; Lin, S.J.; Gan, J.Y.; Chin, T.S.; Shun, T.T.; Tsau, C.H.; Chang, S.Y. Nanostructured high-entropy alloys with
multiple principal elements: Novel alloy design concepts and outcomes. Adv. Eng. Mater. 2004, 6, 299–303. [CrossRef]
2. Song, M.; Zhou, R.; Gu, J.; Wang, Z.; Ni, S.; Liu, Y. Nitrogen induced heterogeneous structures overcome strength-ductility
trade-off in an additively manufactured high-entropy alloy. Appl. Mater. T oday2020, 18, 100498. [CrossRef]
3. Shahmir, H.; Asghari-Rad, P .; Mehranpour, M.S.; Forghani, F.; Kim, H.S.; Nili-Ahmadabadi, M. Evidence of FCC to HCP and
BCC-martensitic transformations in a CoCrFeNiMn high-entropy alloy by severe plastic deformation. Mater. Sci. Eng. A 2021,
807, 140875. [CrossRef]
4. Kim, I.H.; Oh, H.S.; Lee, K.S.; Park, E.S. Optimization of conﬂicting properties via engineering compositional complexity in
refractory high entropy alloys. Scr. Mater. 2021, 199, 113839. [CrossRef]
5. Greer, A.L. Confusion by design. Nature 1993, 366, 303–304. [CrossRef]
6. Gubicza, J.; Heczel, A.; Kawasaki, M.; Han, J.-K.; Zhao, Y.; Xue, Y.; Huang, S.; Lábár, J.L. Evolution of microstructure and hardness
in Hf25Nb25Ti25Zr25 high-entropy alloy during high-pressure torsion. J. Alloys Compd. 2019, 788, 318–328. [CrossRef]
7. Nene, S.S.; Frank, M.; Liu, K.; Sinha, S.; Mishra, R.; McWilliams, B.; Cho, K. Corrosion-resistant high entropy alloy with high
strength and ductility. Scr. Mater. 2019, 166, 168–172. [CrossRef]
8. Kasar, A.K.; Scalaro, K.; Menezes, P .L. Tribological properties of high-entropy alloys under dry conditions for a wide temperature
range—A review. Materials 2021, 14, 5814. [CrossRef]
9. Moschetti, M.; Burr, P .A.; Obbard, E.; Kruzic, J.J.; Hosemann, P .; Gludovatz, B. Design considerations for high entropy alloys in
advanced nuclear applications. J. Nucl. Mater. 2022, 567, 153814. [CrossRef]
10. Afolabi, A.E.; Popoola, A.P .I.; Popoola, O.M. High Entropy Alloys: Advance Material for Landing Gear Aerospace Applications.
In Handbook of Nanomaterials and Nanocomposites for Energy and Environmental Applications ; Springer: Berlin/Heidelberg, Germany,
2020; pp. 1–27.
11. Li, J.; Fang, Q.H.; Liu, B.; Liu, Y.; Liu, Y. Mechanical behaviors of AlCrFeCuNi high-entropy alloys under uniaxial tension via
molecular dynamics simulation. RSC Adv. 2016, 6, 76409–76419. [CrossRef]
12. Li, J.; Fang, Q.; Liu, B.; Liu, Y. Transformation induced softening and plasticity in high entropy alloys. Acta Mater. 2018,
147, 35–41. [CrossRef]
13. Geantă, V .; Voiculescu, I.; Istrate, B.; Vrânceanu, D.M.; Ciocoiu, R.; Cotru t,, C.M. The inﬂuence of chromium content on the
structural and mechanical properties of AlCrxFeCoNi high entropy alloys. Int. J. Eng. Res. Afr. 2018, 37, 23–28. [CrossRef]
14. Nutor, R.K.; Cao, Q.; Wei, R.; Su, Q.; Du, G.; Wang, X.; Li, F.; Zhang, D.; Jiang, J.-Z. A dual-phase alloy with ultrahigh
strength-ductility synergy over a wide temperature range. Sci. Adv. 2021, 7, eabi4404. [CrossRef] [PubMed]
15. Omori, T.; Ando, K.; Okano, M.; Xu, X.; Tanaka, Y.; Ohnuma, I.; Kainuma, R.; Ishida, K. Superelastic effect in polycrystalline
ferrous alloys. Science 2011, 333, 68–71. [CrossRef]
16. Toker, G.P .; Saedi, S.; Acar, E.; Ozbulut, O.E.; Karaca, H.E. Loading frequency and temperature-dependent damping capacity of
NiTiHfPd shape memory alloy. Mech. Mater. 2020, 150, 103565. [CrossRef]
17. Chen, G.; Luo, T.; Shen, S.; Tao, T.; Tang, X.; Xue, W. Research progress in Refractory High-entropy Alloys.Mater. Rev. 2021, 35,
17064–17080. (In Chinese)
18. Tian, Y.; Zhou, W.; Tan, Q.; Wu, M.; Qiao, S.; Zhu, G.; Dong, A.; Shu, D.; Sun, B. A review of refractory high-entropy alloys.T rans.
Nonferrous Met. Soc. China 2022, 32, 3487–3515. [CrossRef]
19. Wang, S.P .; Xu, J. TiZrNbTaMo high-entropy alloy designed for orthopedic implants: As-cast microstructure and mechanical
properties. Mater. Sci. Eng. C 2017, 73, 80–89. [CrossRef]
20. Wang, S.P .; Xu, J. (TiZrNbTa)-Mo high-entropy alloys: Dependence of microstructure and mechanical properties on Mo concentra-
tion and modeling of solid solution strengthening. Intermetallics 2018, 95, 59–72. [CrossRef]
21. Nguyen, V .T.; Qian, M.; Shi, Z.; Song, T.; Huang, L.; Zou, J. A novel quaternary equiatomic Ti-Zr-Nb-Ta medium entropy alloy
(MEA). Intermetallics 2018, 101, 39–43. [CrossRef]
22. Zhou, X.W.; Johnson, R.A.; Wadley, H.N.G. Misﬁt-energy-increasing dislocations in vapor-deposited CoFe/NiFe multilayers.
Phys. Rev. B 2004, 69, 144113. [CrossRef]
23. Stukowski, A. Visualization and analysis of atomistic simulation data with OVITO–the Open Visualization Tool.Model. Simul.
Mater. Sci. Eng. 2009, 18, 015012. [CrossRef]
24. Li, Q.; Zhang, H.; Hu, Z.; Yang, Y. Effect of Ti Doping on Structure and Mechanical Properties of High Entropy Alloy FeCrVMoTix
(x = 0–1). Chin. J. At. Mol. Phys. 2022, 39, 142–146. [CrossRef]
25. Hirel, P . Atomsk: A tool for manipulating and converting atomic data ﬁles.Comput. Phys. Commun. 2015, 197, 212–219. [CrossRef]
26. Singh, S.K.; Parashar, A. Effect of lattice distortion and grain size on the crack tip behaviour in Co-Cr-Cu-Fe-Ni under mode-I and
mode-II loading. Eng. Fract. Mech. 2022, 274, 108809. [CrossRef]
27. Tong, Y.; Tian, N.; Chen, H.; Zhang, X.; Hu, Y.; Ji, X.; Zhang, M.; Zhao, C. Atomic scale deformation behavior of CoCrCuFeNi
High Entropy Alloy. T rans. Nonferrous Met. Soc. China 2023, 33, 1156–1163. [CrossRef]
28. Ma, T.; Xie, H.X. Formation mechanism of face-centered cubic phase of single crystal iron in the process of impact along the
crystal direction. Acta Phys. Sin. 2020, 69, 111–121. [CrossRef]
29. Ding, B.; Song, H.Y.; An, M.R.; Xiao, M.X.; Li, Y.L. Atomistic simulations of deformation mechanism of fcc/bcc dual-phase
high-entropy alloy multilayers. J. Appl. Phys. 2021, 130, 244301. [CrossRef]

## Page 12

Materials 2023, 16, 5126 12 of 12
30. Wang, S.J.; Wang, H.; Du, K.; Zhang, W.; Sui, M.L.; Mao, S.X. Deformation-induced structural transition in body-centred cubic
molybdenum. Nat. Commun. 2014, 5, 3433. [CrossRef]
31. Li, L.; Chen, H.; Fang, Q.; Li, J.; Liu, F.; Liu, Y.; Liaw, P .K. Effects of temperature and strain rate on plastic deformation mechanisms
of nanocrystalline high-entropy alloys. Intermetallics 2020, 120, 106741. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
