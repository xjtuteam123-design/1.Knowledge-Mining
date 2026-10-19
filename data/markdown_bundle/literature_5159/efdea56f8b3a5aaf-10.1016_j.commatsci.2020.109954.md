# 10.1016_j.commatsci.2020.109954

<!-- source: D:\总文献\10.1016_j.commatsci.2020.109954.pdf -->
<!-- file_sha256: 35371a8310603e39d2fd375757e3ef9bea752dcd0d2e99a007c4bd8765393741 -->

## Page 1

Contents lists available at ScienceDirect
Computational Materials Science
journal homepage: www.elsevier.com/locate/commatsci
Molecular dynamics study of fatigue mechanical properties and
microstructural evolution of Ni-based single crystal superalloys under cyclic
loading
Bin Chen a, Wen-Ping Wu a,b,⁎
, Ming-Xiang Chen a,b, Ya-Fang Guo c
a Department of Engineering Mechanics, School of Civil Engineering, Wuhan University, Wuhan 430072, China
b State Key Laboratory of Water Resources & Hydropower Engineering Science, Wuhan University, Wuhan 430072, China
c Institute of Engineering Mechanics, Beijing Jiaotong University, Beijing 100044, China
ARTICLE INFO
Keywords:
Ni-based single crystal superalloys
Molecular dynamics simulation
Cyclic deformation
Fatigue behavior
Microstructural evolution
ABSTRACT
The fatigue performance and deformation mechanism of Ni-based single crystal superalloys under cyclic ten-
sion–compression loading are studied by molecular dynamics simulations. The eﬀ ects of temperature and strain
rate on the cyclic deformation of superalloys are discussed. The results show that there are three di ﬀerent cyclic
deformation mechanisms at di ﬀerent temperature ranges. In the low temperature range, dislocations and
stacking faults shearing γ' phase is the main deformation mechanism. In the high temperature range, Orowan
bypassing and climbing mechanism dominates the deformation. While in the medium temperature range, the
deformation mechanism gradually transforms from the dislocation and stacking faults shearing the γ' phase to
the Orowan bypassing and climbing. The simulation results also reveal that the superalloys exhibit a cyclic
saturation stage after the initial cyclic hardening. The cyclic saturation stage is a dynamic equilibrium of dis-
location proliferation and annihilation, indicating that the superalloys have excellent fatigue mechanical
properties. Moreover, the dislocation density and the proportion of stacking faults increase with increasing strain
rate, resulting in faster cyclic stability and higher stress amplitude for the superalloys. These results provide
important information for understanding the fatigue mechanisms of superalloys from an atomistic perspective.
1. Introduction
Ni-based single crystal superalloys have been widely used as pri-
mary materials in turbines blades for aircraft and power-generation
turbines, rocket engines, owing to their excellent high temperature
creep, fatigue and corrosion resistance [1–4]. During the engine in
service, the blade is repeatedly subjected to the scouring of high tem-
perature and pressure gas, and the cyclic stress caused by start-up, shut-
down and acceleration of turbine blades, resulting in low-cycle fatigue
failure [5,6]. In the past few decades, many researchers have been at-
tracted to study the high temperature fatigue behavior of the super-
alloys.
Study on the fatigue damage mechanism plays an essential role in
both understanding fatigue failure behavior and improving the life
prediction accuracy of superalloys [7,8]. Related experimental studies
[9–16] have shown that the main characteristics of low-cycle fatigue
deformation of Ni-based single crystal superalloys at low temperature
are that the high density of tangled dislocations cut through γ' phase to
form plenty of planar slip bands by planar slip. Some stacking faults
(SFs) were observed in the γ phase, which hindered the cross slip of
dislocations. Thus, the planar slip is deemed as the primary deformation
mechanism at low temperature. In the medium temperature range, the
dominant deformation mechanism is dislocation climb and cross-slip,
the formation of irregular dislocation network at the γ/γ' interface, as
well as a minority of SFs cutting γ' phase. At high temperature, the
deformation mechanism is mainly the Orowan bypassing mechanism,
combined with the glide-climb process. Although these studies on the
fatigue behaviors of Ni-based superalloys have been applied at di ﬀerent
temperatures, the e ﬀects of temperature on the interface microstructure
and cyclic mechanical properties of Ni-based superalloys are still not
very clear.
The evolution of the interface microstructure has a great e ﬀect on
the fatigue properties of the superalloys. Low-cycle fatigue for a Ni-
based single-crystal superalloy studied by Zhang et al. [17] indicated
that the irregular dislocation networks and the SFs of the γ phase led to
cyclic hardening. Ott and Mughrabi [18] found that the microstructure
https://doi.org/10.1016/j.commatsci.2020.109954
Received 17 May 2020; Received in revised form 19 July 2020; Accepted 20 July 2020
⁎ Corresponding author at: Department of Engineering Mechanics, School of Civil Engineering, Wuhan University, Wuhan 430072, China.
E-mail address: wpwu@whu.edu.cn (W.-P. Wu).
Computational Materials Science 185 (2020) 109954
0927-0256/ © 2020 Elsevier B.V. All rights reserved.
T

## Page 2

of γ/γ' interface had an important in ﬂuence on the crack growth and
fatigue life. Lin et al. [19] revealed that the dislocation networks at the
γ/γ′ interface play a key role in the strain hardening of the low-cycle
fatigue behavior of superalloys, while the shearing of γ' precipitate by
super-dislocations make a major contribution to the strain softening of
superalloys. Fan et al. [20] found that the γ′ rafting microstructure
signiﬁcantly reduced the Low-cycle fatigue life of Ni-based superalloy
compared to the virgin microstructure. These studies indicated that
during the fatigue damage process of Ni-based single crystal super-
alloys, the morphologies and evolutions of microstructures (including
dislocations, slip bands, SFs, dislocation network) directly a ﬀected the
initiation and propagation of fatigue crack and the fatigue lifetime of
superalloys, ultimately led to the fracture failure of the superalloys.
Under various conditions, the evolution characteristics of the interface
microstructure result in an extremely complicated fatigue process of the
superalloys [21]. It is indispensable for comprehensively considering
the γ/γ' interface microstructures and their evolutions under di ﬀerent
conditions, and exploring the microscopic mechanisms of fatigue da-
mage of superalloys. However, due to the extreme di ﬃculties of in-situ
experimental observation, current micro-scale experiments mainly ob-
served the microstructures before and after cyclic loading, the forma-
tion and evolution processes of microstructure in superalloys during the
cyclic deformation has not yet been fully understood.
Molecular dynamics (MD) simulation has the advantage of cap-
turing real-time dynamic deformation and plays an important part in
studying the microscopic deformation mechanism at the atomistic
scale. Many researchers have studied the mechanical properties and
deformation mechanisms of superalloys through MD simulations at
nanoscale. For example, Yashiro et al. [22] used MD to simulate the
dislocation pinning at γ′ precipitates, bowing-out in the γ channel, pile-
up and nucleation of super-dislocation in the γ′ precipitate. Ma et al.
[23] found that the shearing process caused by the dislocations motion
was the dominant deformation mechanism in γ/γ' phase interface at
room temperature under tensile loading. Zhu et al. [24] and Xiong et al.
[25] studied the interaction between matrix dislocation and interfacial
misﬁt dislocation networks in Ni-based single crystal superalloys, in-
dicated that the interfacial dislocation networks can prevent the matrix
dislocations cutting into the γ' precipitate. Yu et al. [26] investigated
the microstructure evolution of γ/γ′ interface under thermal –mecha-
nical
coupling. Xie et al. [27] studied three di ﬀerent deformation me-
chanisms of dislocations under shear loads, and revealed that the sta-
bility of the phase interface strongly related to the interaction of
mutually perpendicular mis ﬁt dislocations. However, these studies
focus on the exploration of the deformation mechanisms under uniaxial
tensile or shear loading, very few studies analyzed the fatigue behavior
and deformation mechanism of superalloys under cyclic loading.
Moreover, most of MD simulations were carried out by using double-
layer structure model, which did not consider the cubic structure of γ'
precipitate embedded in the γ matrix with a high-volume fraction
(~70%), resulting in an inaccurate calculation of the atomic stress ﬁeld
and hardly obtain three-dimensional (3D) dislocation structure.
In this paper, MD simulations are performed to investigate the fa-
tigue mechanical properties and microstructure evolution of γ/γ′ in-
terface in Ni-based single crystal superalloys under cyclic loading. The
MD model uses a 3D cubic unit with the volume fraction of γ' pre-
cipitate phase ( ≈70%), which is similar to the structure of the actual
materials. The cyclic deformation mechanisms of superalloys are ex-
plored at the atomistic scale, and the e ﬀects of temperature and strain
rate on the cyclic deformation mechanisms are systematically dis-
cussed. The present work will be helpful to understand the fatigue
deformation behavior of superalloys from an atomistic perspective.
2. Modeling and simulation
The Ni-based single crystal superalloys consist of the γ matrix phase
(composed of the single crystal Ni) and the γ' precipitate phase
(composed of the intermetallic compound Ni
3Al) with di ﬀerent lattice
parameters, resulting in the formation of lattice mismatch on the phase
interface. The lattice mismatch of the (0 0 1) plane in [0 0 1] direction
can be de ﬁned as [28]
=× −
+
′
′
δ aa
aa2
γγ
γγ (1)
Here =a 3.52γ Å and =′a 3.62γ Å [29]. The lattice mismatch
=δ 2.8% , which indicates that the mismatch stress ﬁeld caused by the
lattice mismatch will be generated at the (0 0 1) interface between γ and
γ' phases, and the mismatch stress will achieve equilibrium by creating
a dislocation network at the phase interface [28,30]. Given the concept
of coincidence site lattice (CSL) on the mis ﬁt phase interface, we can
obtain the relation between aγ and ′aγ .
=+
=≈
′
−′
na n a
n
(1 ) ,
35
γγ
a
aa
γ
γ γ (2)
Based on the idea of constructing the (0 0 1) orientation γ/γ' inter-
face model in our previous work [29–31], it can be understood easily
that a γ' structural unit of 35 × 35 × 35 (de ﬁning the side length of the
cuboidal γ' phase) has almost the same volume and shape as a γ
structural unit of 36 × 36 × 36. Then by replacing the γ structural unit
with the γ' structural unit, which has fewer atoms, but approximately
the same size, in the center of a 40 × 40 × 40 γ block with the same
lattice directions, we can obtain the initial unit cell of the (0 0 1) or-
ientation γ/γ' interface model, as shown in Fig. 1(a) and (b). The size of
the simulation box is 140.8 Å ×140.8 Å ×140.8 Å, the γ' volume
fraction of the model is (36/40) 3 = 72.9%, which is similar to the
structure of the actual materials. Fig. 1(c) displays that the mis ﬁt dis-
location network of (0 0 1) orientation occurs at the γ/γ' phase interface
at very low temperature after MD relaxation, which is consistent with
the previous experimental observation [12,13] and simulations results
[29,32].
In the present work, the open-source LAMMPS code [33] is used to
carry out MD simulations of the fatigue behavior of superalloys under
cyclic loading. The Ni-Al alloy potential (Mishin-Ni-Al-2009.eam) is
used [34], and the periodic boundary conditions are employed along all
three directions to eliminate the boundary e ﬀect. The loading is per-
formed under cyclic tension –compression conditions by controlling the
strain, and a triangular waveform with a strain ratio of R = −1i s
adopted (R is the ratio of the minimum strain to the maximum strain for
each cycle), the loading diagram is shown in Fig. 2. To separately study
the e ﬀects of temperature and strain rate on the fatigue mechanical
properties and deformation mechanisms under cyclic loading, six dif-
ferent temperatures (300 K, 500 K, 800 K, 1000 K, 1200 K, 1500 K) and
three di ﬀerent strain rates
××× −−−sss(51 0 , 11 0 , 21 0 )81 91 91 are set.
The detailed cyclic loading conditions for each sample are shown in
Table 1. The dislocation analysis (DXA) proposed by Stukowski et al.
[35] and the common neighborhood analysis (CNA) proposed by Faken
et al. [36] in OVITO software [37] are used to analyze the evolution of
microstructure, which can provide the details of dislocation structure
evolution.
3. Results and discussion
3.1. The evolutions of microstructure at di ﬀerent loading stages
The cyclic stress –strain curve at 300 K is shown in Fig. 3(a), when
the superalloys are subjected to cyclic loading, the maximum stress
rises with the increase of the number of cycles, i.e. the stress cyclic
hardening occurs ﬁrst, which is mainly due to the accumulation of the
initial defects, such as dislocation, stacking fault (SF) [38]. As loading
progresses, the cyclic stress –strain curves are basically consistent in the
last few cycles. As the number of cycles increases, the maximum stress
tends to stabilize and reaches a cyclic saturation state, which is
B. Chen, et al. Computational Materials Science 185 (2020) 109954
2

## Page 3

consistent with the cyclic deformation characteristics of metals [39].
In order to explore the evolution of dislocation structure in a certain
cycle process after reaching a cyclic saturation state, the cycle process is
divided into four stages (AB, BC, CD, DE) as shown in Fig. 3(b). During
the cyclic loading process, the initial mis ﬁt interface dislocation net-
work in Fig. 1(c) will evolve into the chaotic dislocation structure, due
to the dislocations reaction, interaction, proliferation and annihilation.
Meanwhile, to observe the evolution of defects more clearly, only the
microstructure on the
(11¯1) plane (the primary slip plane) is selected for
analysis as shown in Fig. 4(a). Fig. 4(b) shows the morphology of the
microstructure on the (11¯1) plane after relaxation at 300 K, and the
following dislocation reaction is obtained:
→++ SF1/2[101¯] 1/6[211 ¯]1 / 6 [ 1 1¯2¯] (3)
Among them, 1/2[101¯] is a perfect dislocation, 1/6[211¯] and 1/6[11¯2¯]
are Shockley partial dislocations, and the SF lies in between two
Shockley dislocations. According to the dislocation reaction (3), the
perfect dislocations in the matrix can be decomposed into two Shockley
dislocations and a SF when the alloy is subjected to temperature e ﬀects.
Other dislocation reactions of the similar mechanism are also observed
in other parts of the
(11¯1) plane as:
→++ SF1/2[1¯01] 1/6[1 ¯12] 1/6[2 ¯1¯1] (4)
As shown in Fig. 4(b), dislocation reactions mainly occur in four
regions, named as a, b, c, and d, each region consists of two partial
dislocations and a part of SFs in the middle of the two dislocations. We
will focus on these regions in the subsequent cyclic loading.
Fig. 5 demonstrates the microstructural evolution on the
(11¯1) plane
during cyclic loading. From the evolution of dislocations in Fig. 5(a), it
can be found that during the process from point A to point B, the dis-
locations and SFs in the c and d regions occur initially in the γ matrix,
Fig. 1. The model diagram for simulation. (a) the geometric model; (b) the atomic structure model; (c) the mis ﬁt dislocation network at the (0 0 1) orientation γ/γ'
phase interface.
Fig. 2. The loading diagram of symmetrical cyclic tension and compression, the
strain is ﬁrst loaded from 0 to εΔ /2, then reverse loading to − εΔ/ 2 and forward
loading to εΔ /2. The cyclic loading is repeated in this way.
Table 1
The cyclic loading parameters for each specimen.
Specimen Temperature (K) Strain rate (s −1) Strain range Cycles
1 300 ×1 109 0.06 30
2 500 ×1 109 0.06 30
3 800 ×1 109 0.06 30
4 1000 ×1 109 0.06 30
5 1200 ×1 109 0.06 30
6 1500 ×1 109 0.06 30
7 300 ×5 108 0.1 20
8 300 ×1 109 0.1 20
9 300 ×21 0 9 0.1 20
10 1200 ×5 108 0.1 20
11 1200 ×1 109 0.1 20
12 1200 ×21 0 9 0.1 20
B. Chen, et al. Computational Materials Science 185 (2020) 109954
3

## Page 4

and then gradually cut into the γ' phase together with the increase of
the strain. The sliding direction is shown by the black arrow in the
Fig. 5. Meanwhile, the dislocations and SFs in regions a and b slip in the
opposite direction and remain in the matrix. During the process from
point B to point C, the dislocations and SFs in regions c and d slide
along the direction of γ matrix, and return to the initial position due to a
reduction in the ﬁnal strain. At this time, the dislocations and SFs in
regions a and b will also return to their original positions. A similar
process can be found in Fig. 5(b) in the CD and DE stages, the dis-
locations slide into and out of the interface during the loading and
unloading processes. However, the sliding directions of dislocations and
SFs in the CD and DE stages are opposite to those in the AB and BC
stages.
From the above analysis, it can be concluded that at 300 K, after the
cycle saturation stage is reached, the deformation of the microstructure
is mainly the reciprocating slip of the dislocations and SFs, resulting in
continuous shearing of the γ' phase, which is supported by research
related to the cyclic deformation in face-centered cubic (FCC) metals
[38].
3.2. E ﬀect of temperature
The microstructure evolution and mechanical properties of the su-
peralloys under cyclic loading are simulated at di ﬀerent ambient tem-
peratures (300 K, 500 K, 800 K, 1000 K, 1200 K, and 1500 K) with the
same strain rate
× −s(11 0 )91 . As shown in Figs. 6 and 7, the results in-
dicate that cyclic hardening ﬁrst occurs under cyclic loading, which is
mainly due to the accumulation of initial dislocations and SFs. Subse-
quently, the stress amplitude will gradually become a stable value and
reach a cyclic saturation state. Compared with the traditional fatigue
experimental data, the simulation results indicate that the sample can
reach the saturation state in fewer cycles, and most of the saturation
state can be reached within 30 cycles due to the di ﬀerence of time scale
in MD simulation. Moreover, it can be seen from Fig. 7(a) that as the
temperature increases, the number of cycles required to reach the cyclic
saturation state gradually decreases. By comparing with the cyclic
curves at di ﬀerent temperatures, it is found that it takes about 25 cycles
to achieve the cycle saturation under the low-temperature conditions of
300 and 500 K. However, at the high-temperature conditions of 1200
and 1500 K, it only takes about 5 cycles to reach the saturation state.
Because in the high-temperature range, the resistance to cross slip de-
creases, leading to an increase in hardening rate in the rapid hardening
stage [38]. Besides, more slip systems are activated due to the e ﬀect of
thermal activation in the γ matrix [40], which results in rapid cyclic
hardening and then reaches the saturation stage [41].
As shown in Fig. 7(b), the saturation stress amplitude ﬁrst increases
and then decreases with increasing the temperature. This is because the
deformation mechanisms of superalloys at di ﬀerent temperatures are
diﬀerent. From Fig. 8(a) and (b), it can be observed that the sample
surface exists obvious SFs. It can be inferred that in the low temperature
range of 300 K and 500 K, the main deformation mechanism is the
dislocations and SFs continuously shearing the γ' phase during the
cyclic loading process. However, with increasing temperature in Fig. 8,
the SFs on the surface gradually disappear, which indicates that the
Fig. 3. (a) The cyclic stress –strain curve at the temperature of 300 K and the strain rate of × −s1 109 1; (b) the ﬁve representative points of the stress –strain curve on
one cycle after cycle saturation.
Fig. 4. (a) The (11¯1) plane as the selected the primary slip plane; (b) the morphology of the microstructure on the (11¯1) plane after relaxation at 300 K. (Blue line:
perfect dislocation; other color lines: partial dislocation; red dots part: SFs; the meaning of the color applies to all microstructure patterns in this paper).
B. Chen, et al. Computational Materials Science 185 (2020) 109954
4

## Page 5

deformation mechanism of the alloy has also changed.
In order to further explore the deformation mechanisms of the su-
peralloys at di ﬀerent temperatures, Fig. 9 shows the microstructure
evolution process at the high temperature of 1200 K. It can be seen from
Fig. 9 (a) that when the dislocation slips to the γ/γ' phase interface,
these dislocation are hindered and bowed in matrix channel due to the
hardness of γ' increases with the rise in temperature [42], With the
increase of strain, these bow dislocations eventually form dislocation
loops in the matrix channel, which is a typical Orowan bowing me-
chanism or (Orowan bypassing mechanism). As the cyclic loading and
Fig. 5. The evolutions of microstructure on the (11¯1) plane at di ﬀerent loading stages.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
5

## Page 6

unloading proceeds, the hexagonal dislocation loop at the bottom of the
model will gradually climb into the γ' phase as the strain increases, as
shown in Fig. 9(b). In addition, due to the thermal activation at high
temperature, there is also a small amount of dislocation cross slip
during cyclic loading (see Fig. 10), but Orowan-bypassing and climbing
are the dominant mechanisms. From the above results, it can be con-
cluded that the mechanisms of Orowan bypassing and climbing mainly
dominate the deformation of the superalloys at 1200 K, which is con-
sistent with the ﬁndings of other cyclic deformation studies
[12,13,40,43].
Fig. 11 reveals that not only the dislocations and SFs shearing γ'
phase but also hexagonal dislocation loops are observed at 800 K and
1000 K. Combined with the result in Fig. 8, the SFs gradually disappears
with the increase of temperature, it can be deduced that the deforma-
tion mechanism in the medium temperature range (800 K and 1000 K)
gradually transforms from the dislocations and SFs shearing γ' phase to
the Orowan-bypassing and climbing.
Based on the above analysis, in the low-temperature range, the
Fig. 6. The cyclic stress –strain curves at di ﬀerent temperatures. (a) 300 K, (b) 500 K, (c) 800 K, (d) 1000 K, (e) 1200 K, and (f) 1500 K.
Fig. 7. (a) Variation of stress amplitude with the number of cycles at di ﬀerent temperatures; (b) variation of saturation stress amplitude with temperature.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
6

## Page 7

deformation mechanism of the superalloys is mainly the dislocations
and SFs continuously shearing of the γ' phase. At high temperature, the
deformation mechanism of the superalloys is dominated by Orowan-
bypassing and climbing mechanism. And the deformation mechanism
of the superalloys at intermediate temperature gradually transforms
from the dislocation and stacking faults shearing the γ' phase to the
Orowan-bypassing and climbing, which are in agreement with experi-
mentally studied by Li et al. [13] and Lian et al. [40].
In the range of 300 K –800 K, the dominant deformation mechanism
is dislocations and SFs shearing the γ' phase. According to the study of
Daymond et al. [42], the hardness of γ' increases with rising tempera-
ture, the resistance of shearing γ' phase increases with rising tempera-
ture, so the saturation stress amplitude increases during the cyclic
loading process. In the range of 1000 K –1500 K, a small amount of
cross slip occurs during cyclic deformation, as shown in Fig. 10. How-
ever, the deformation mechanism is mainly dominated by Orowan-
bypassing and climbing, which reduces the resistance of dislocation
movement and eventually leads to a reduction in the saturation stress
amplitude.
Fig. 12 shows the variation of dislocation density with loading time
at di ﬀerent temperatures. Due to the e ﬀect of thermal activation, more
slip bands will be activated at higher temperatures [40], resulting in an
initial dislocation density at higher temperatures of 1000 K and 1200 K
higher than that at 300 K. And then through dislocation reaction and
dislocation interaction during cyclic loading, the dislocation density
tends to dynamic stable with small ﬂuctuations. The higher the tem-
perature results in the smaller of the dislocation density when it reaches
dynamic stability. This is because the climbing mechanism at high
temperatures can e ﬀectively release dislocation pile-ups [44], and the
climbing mechanism can only be generated by edge dislocations, but
the slip mechanism at low temperatures can be generated by edge
dislocations or screw dislocations. Whatever the deformation me-
chanism, the dislocation density remains basically constant after cyclic
saturation. Combined with the above analysis, it can be concluded that
although the deformation mechanisms are various at di ﬀerent tem-
peratures, the proliferation and annihilation of dislocations achieve a
dynamic equilibrium in the loading and unloading processes after the
superalloys enter into the cyclic saturation stage, and the dislocation
density remains basically stable. The relevant mechanisms have been
veriﬁed experimentally by Feltner et al. [38] and Essmann et al. [45].
3.3. E ﬀect of strain rate
Strain-rate sensitivity of ﬂow stress, strain hardening and strain-
hardening rate has been observed in many studies of superalloys
[46–48], but the strain rate e ﬀect on mechanism of cyclic deformation
is still not clear, an e ﬀort is made in this section to investigate the e ﬀect
of strain rates on fatigue mechanisms of superalloys. Figs.
 13 and 14
show the cyclic stress-strain curves and variation of stress amplitude at
three diﬀerent strain rates. The same situation as mentioned above, the
initial cyclic hardening of the superalloys appears ﬁrstly and then the
stress reaches saturation state during the cyclic loading process. In
addition, it can be found from Fig. 14 that the hardening rate increases
and the rate of reaching the saturation stage become faster as the strain
rate increases, this phenomenon is even more pronounced at the higher
temperature of 1200 K, this phenomenon can be explained from the
following discussion. The nature of work hardening is the reduction of
dislocation mobility caused by these three factors, (1) the interaction
between dislocations and dislocations, (2) ﬁxed dislocations (the
Lomer-Cottrell dislocations and dislocation jog) formed by the inter-
penetration of dislocation from di ﬀerent slip systems, (3) the hindering
eﬀect of SFs on dislocation movement [48,49]. Fig. 15(a) shows that the
dislocation density increases with the increase of the strain rate. A
higher dislocation density in the same volume means that the interac-
tion between dislocations is more intense, which results in the move-
ment of dislocations is restrained. Fig. 15(b) shows that as the strain
rate increases, the proportion of SFs structure in the entire model in-
creases, so the hindering e ﬀect of SFs on dislocation motion is also
increased. Moreover, when the strain rate increases, due to the faster
deformation speed, not only the primary slip system starts, but also the
secondary slip system will start one after another. The dislocations on
the more slip systems will interpenetrate to form more ﬁxed disloca-
tions, which further hinders the movement of dislocations. To sum up,
the higher the strain rate is, the faster the hardening rate is, the faster
the cyclic saturation stage reaches.
Furthermore, according to the foregoing discussion, it is known that
the stress amplitude is related to the deformation mechanism [13,40],
but it can be observed from Fig. 14 that at the same temperature and
the same deformation mechanism, the strain rate increases and the
corresponding stress amplitude also increases. This can be explained by
the fact that regardless of the deformation mechanism, the deformation
is mainly accomplished by the movement of dislocations. From Fig. 15,
both dislocation density and proportion of SF increase at high strain
Fig. 8. The microstructure of model surface based
on CNA analysis at the same strain (3%) and dif-
ferent temperatures, the red stripe pointed by the
blue arrow is the SFs. (a) 300 K, (b) 500 K, (c) 800 K;
(d) 1000 K, (e) 1200 K, and (f) 1500 K. (For inter-
pretation of the references to colour in this ﬁgure
legend, the reader is referred to the web version of
this article.)
B. Chen, et al. Computational Materials Science 185 (2020) 109954
7

## Page 8

Fig. 9. The microstructure evolution process at 1200 K. (a) dislocation-bypassing process, and (b) dislocation climbing process.
Fig. 10. The dislocation cross slip mechanism. (a) the microstructure of dislocation cross slip in the simulation process. (b) the schematic diagram of dislocation cross
slip.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
8

## Page 9

rate, the higher dislocation density and proportion of SFs will more
strongly impede the movement of dislocations, resulting in an increase
in deformation resistance [50]. In addition, the fact of dislocation
motion is time-dependent [51], as the strain rate increases, the accel-
eration of dislocation motion is larger, and the obstacles encountered in
unit time are stronger, so the resistance of dislocation motion is greater.
Therefore, the movement of dislocations is more di ﬃcult and the stress
also increases at a higher strain rate.
3.4. Validation of MD simulations
Obviously, in the present model, the channel width and precipitate
size are 14.08 Å and 126.7 Å, respectively, which are much smaller
than the real channel width and precipitate size. However, due to the
cubic-structure model is adopted, and the γ' precipitate volume fraction
of the model is 72.9% in the present model, which ensures that the ratio
of the channel width to the size of the precipitate is consistent with that
of the actual materials. The size of the model only changes the size of
the dislocation structure in the same proportion, but does not change
the morphology of the dislocation structure [29,30]. Therefore, the
present MD model can describe basically consistent physical phe-
nomena, such as the morphology of dislocation structure and the
characteristics of dislocation movement in the channel, when the ratio
of matrix channel width to precipitate size is ﬁxed.
In addition, due to the time scale of MD simulation is very small,
results in the strain rate is very high (10
7–1010 s−1), which is multiple
orders of magnitude faster than the existing experimental tests.
Researchers have mainly qualitatively compared the MD simulations
with the corresponding experimental results. For example, Ma et al.
[23] studied the crack propagation at the Ni/Ni
3Al interface by using
the strain-controlled loading and unloading simulations with the strain
rate of 10
9 s−1. Xiong et al. [52] studied the e ﬀect of hydrogen (H) on
the interface damage of Ni-based single crystal superalloys by MD si-
mulation with a shear strain rate of 10
9 s−1. Liu et al. [53] studied the
inﬂuence of Re on the propagation of a Ni/Ni 3Al interface crack under
the strain rate of 10 9 s−1. Li et al. [54] used MD simulation to in-
vestigate the tension process of Ni-based superalloy at various strain
rates (1 × 10 10 s−1,3×1 0 9 s−1,3×1 0 8 s−1 and 3 × 10 7 s−1).
Houllé et al. [55] carried MD simulation to study the uniaxial com-
pression deformation behavior of γ'N i 3Al nanocubes at a strain rate of
108 s−1. Liu et al. [56] investigated the mechanical properties in nickel-
based superalloys by MD simulation with strain rates at 0.5 × 10 9 s−1,
1.0 × 109 s−1 and 2.0 × 10 9 s−1 in the models without and with voids.
All of the above studies are qualitatively studying the deformation
mechanisms and mechanical behavior of materials from the atomic
scale, and obtained results are similar to the experimental observations.
Based on the above discussion, by comparing the MD simulations
obtained in this work and corresponding macroscopic and microscopic
experimental observations, it can be seen that the MD simulations are
Fig. 11. The microstructure morphology at the strain (3%). (a) 800 K and (b) 1000 K.
Fig. 12. The variation of dislocation density with loading time at di ﬀerent
temperatures.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
9

## Page 10

reasonable and further re ﬂect the fatigue behaviors and its deformation
mechanisms of Ni-based single crystal superalloys under cyclic loading
in atomic scale.
4. Conclusions
The fatigue deformation mechanisms and mechanical properties of
Ni-based superalloys at di ﬀerent temperatures and strain rates under
cyclic loadings are studied by MD simulations, the following conclu-
sions can be drawn from the present study.
(1) When the superalloys are subjected to cyclic loading, cyclic hard-
ening ﬁrst occurs, and then the stress amplitude reaches saturation
stage as the number of cycles increased. Meanwhile, the cyclic
Fig. 13. The cyclic stress–strain curves at di ﬀerent strain rates, (a1) at 300 K, × −s5 108 1; (a2) at 300 K, × −s1 109 1; (a3) at 300 K, × −s21 0 9 1; (b1) at 1200 K, × −s5 108 1;
(b2) at 1200 K, × −s1 109 1; (b3) at 1200 K, × −s21 0 9 1.
Fig. 14. Variation of stress amplitude with the number of cycles at di ﬀerent strain rates. (a) at 300 K, (b) at 1200 K.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
10

## Page 11

deformation mechanism of superalloys is the dynamic equilibrium
of proliferation and annihilation process of the dislocation. The
dislocation density tends to remain stable in the cyclic saturation
stage, which indicates that the superalloys have excellent fatigue
mechanical properties.
(2) Three cyclic deformation mechanisms are found: In the low tem-
perature range, dislocations and stacking faults shearing γ' phase is
the main deformation mechanism. In the high temperature range,
Orowan-bypassing and climbing mechanism dominates the de-
formation. While in the medium temperature range, the deforma-
tion mechanism gradually transforms from the dislocation and
stacking faults shearing the γ' phase to the Orowan-bypassing and
climbing, which are supported by previous experiments.
(3) The superalloys show faster cyclic stability and higher stress am-
plitude with increasing strain rate, which is caused by the dis-
location density and the proportion of stacking faults increases with
the increase of the strain rate.
CRediT authorship contribution statement
Bin Chen: Conceptualization, Software, Validation, Writing - ori-
ginal draft. Wen-Ping Wu: Conceptualization, Data curation, Formal
analysis, Validation, Writing - review & editing, Project administration.
Ming-Xiang Chen: Data curation, Visualization. Ya-Fang Guo: Formal
analysis, Validation, Writing - review & editing.
Declaration of Competing Interest
The authors declare that they have no known competing ﬁnancial
interests or personal relationships that could have appeared to inﬂ u-
ence the work reported in this paper.
Acknowledgements
We gratefully acknowledge National Natural Science Foundation of
China (Grant Nos. 11772236, 11472195, and 11711530643) for their
ﬁnancial support. The work was carried out at Supercomputer Center in
Wuhan University.
References
[1] T.M. Pollock, S. Tin, Nickel-based superalloys for advanced turbine engines:
Chemistry, microstructure, and properties, J. Propul. Power 22 (8) (2006) 361 –374.
[2] W. Xia, X. Zhao, L. Yue, Z. Zhang, A review of composition evolution in Ni-based
single crystal superalloys, J. Mater. Sci. Technol. 44 (2020) 76 –95.
[3] H. Long, S. Mao, Y. Liu, Z. Zhang, X. Han, Microstructural and compositional design
of Ni-based single crystalline superalloys – A review, J. Alloy. Compd. 743 (2018)
203–220.
[4] Z.X. Wen, J.W. Liang, C.Y. Liu, H.Q. Pei, S.F. Wen, Z.F. Yue, Prediction method for
creep life of thin-wall specimen with ﬁlm cooling holes in Ni-based single-crystal
superalloy, Int. J. Mech. Sci. 141 (2018) 276 –289.
[5] J. Hou, B.J. Wicks, R.A. Antoniou, An investigation of fatigue failures of turbine
blades in a gas turbine engine by mechanical analysis, Eng. Fail. Anal. 9 (2002)
201–211.
[6] M. Naeem, R. Singh, D. Probert, Implications of engine deterioration for a high-
pressure turbine blade ’s low-cycle fatigue (LCF) life-consumption, Int. J. Fatigue 21
(8) (1999) 831 –847.
[7] S.P. Zhu, H.Z. Huang, R. Smith, V. Ontiveros, L.P. He, M. Modarres, Bayesian fra-
mework for probabilistic low cycle fatigue life prediction and uncertainty modeling
of aircraft turbine disk alloys, Probabilist. Eng. Mech. 34 (2013) 114 –122.
[8] Y. Fan, W. Huang, X. Yang, D. Shi, S. Han, The role of coarsening on LCF behaviour
using small coupons of a DS Ni-based superalloy, Int. J. Fatigue 125 (2019)
418–431.
[9] Z.Y. Yu, X.M. Wang, H. Liang, Z.X. Li, L. Li, Z.F. Yue, Thickness debit e ﬀect in Ni-
based single crystal superalloys at di ﬀerent stress levels, Int. J. Mech. Sci. 170
(2020) 105357 .
[10] T.P. Gabb, J. Gayda, R.V. Miner, Orientation and temperature dependence of some
mechanical properties of the single-crystal Nickel-base superalloy René N4: Part Ⅱ.
Low cycle fatigue behavior, Metall. Mater. Trans. A 17A (1986) 497 –505.
[11] I.S. Kim, B.G. Choi, J.E. Jung, J. Do, C.Y. Jo, E ﬀect of microstructural characteristics
on the low cycle fatigue behaviors of cast Ni-base superalloys, Mater. Charact. 106
(2015) 375 –381.
[12] X.G. Wang, J.L. Liu, T. Jin, X.F. Sun, Y.Z. Zhou, Z.Q. Hu, J.H. Do, B.G. Choi,
I.S. Kim, C.Y. Jo, Deformation mechanisms of a nickel-based single-crystal super-
alloy during low-cycle fatigue at di ﬀerent temperatures, Scripta Mater. 99 (2015)
57–60.
[13] P. Li, Q.Q. Li, T. Jin, Y.Z. Zhou, J.G. Li, X.F. Sun, Z.F. Zhang, Comparison of low-
cycle fatigue behaviors between two nickel-based single-crystal superalloys, Int. J.
Fatigue 63 (2014) 137 –144.
[14] H.
Zhou, Y. Ro, H. Harada, Y. Aoki, M. Arai, Deformation microstructures after low-
cycle fatigue in a fourth-generation Ni-base SC superalloy TMS-138, Mater. Sci. Eng.
A 381 (1 –2) (2004) 20 –27.
[15] V. Brien, B. Décamps, Low cycle fatigue of a nickel based superalloy at high tem-
perature: deformation microstructures, Mater. Sci. Eng. A 316 (2001) 18 –31.
[16] S. Kraft, I. Altenberger, H. Mughrabi, Directional γ/γ' coarsening in a mono-
crystalline nickel-based superalloy during low-cycle thermomechanical fatigue,
Scripta Metall. et Mater. 32 (3) (1995) 411 –416.
[17] L. Zhang, L.G. Zhao, A. Roy, V.V. Silberschmidt, G. McColvin, Low-cycle fatigue of
single crystal nickel-based superalloy – Mechanical testing and TEM characterisa-
tion, Mater. Sci. Eng. A 744 (2019) 538 –547.
[18] M. Ott, H. Mughrabi, Dependence of the high-temperature low-cycle fatigue be-
haviour of the monocrystalline nickel-base superalloys CMSX-4 and CMSX-6 on the
γ/γ'-morphology, Mater. Sci. Eng. A 272 (1999) 24 –30.
[19] B. Lin, M.S. Huang, L.G. Zhao, A. Roy, V. Silberschmidt, N. Barnard, M. Whittaker,
G. McColvin, 3D DDD modelling of dislocation –precipitate interaction in a nickel-
based single crystal superalloy under cyclic deformation, Philos. Mag. 98 (17)
(2018) 1550 –1575.
[20] Y.S. Fan, X.G. Yang, D.Q. Shi, S.W. Han, S.L. Li, A quantitative role of rafting on low
cycle fatigue behaviour of a directionally solidi ﬁed Ni-based superalloy through a
cross-correlated image processing method, Int. J. Fatigue 131 (2020) 105305 .
[21] A. Pineau, S.D. Antolovich, High temperature fatigue of nickel-base superalloys – A
review with special emphasis on deformation modes and oxidation, Eng. Fail. Anal.
16 (8) (2009) 2668 –2697.
[22] K. Yashiro, M. Naito, Y. Tomita, Molecular dynamics simulation of dislocation
nucleation and motion at γ/γ' interface in Ni-based superalloy, Int. J. Mech. Sci. 44
(2002) 1845 –1860.
[23] L. Ma, S. Xiao, H. Deng, W. Hu, Tensile mechanical properties of Ni-based super-
alloy of nanophases using molecular dynamics simulation, Phys. Status Solidi B 253
(4) (2016) 726 –732.
[24] Y.X. Zhu, Z.H. Li, M.S. Huang, Atomistic modeling of the interaction between
matrix dislocation and interfacial mis ﬁt dislocation networks in Ni-based single
crystal superalloy, Comput. Mater. Sci. 70 (2013) 178 –186.
[25] J. Xiong, Y.X. Zhu, Z.H. Li, M.S. Huang, Quantitative study on interactions between
interfacial mis ﬁt
 dislocation networks and matrix dislocations in Ni-based single
crystal superalloys, Acta Mech. Solida Sin. 30 (4) (2017) 345 –353.
[26] J.G. Yu, Q.X. Zhang, Z.F. Yue, R. Liu, M.K. Tang, X.W. Li, Microstructure evolution
and mechanical behavior of the Ni/Ni 3Al interface under thermal-mechanical
Fig. 15. Variations of dislocation density and the proportion of SF structure at di ﬀerent strain rates. (a) dislocation density, (b) the proportion of SF structure.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
11

## Page 12

coupling, Mater. Express 5 (4) (2015) 343 –350.
[27] H.X. Xie, C.Y. Wang, T. Yu, Motion of mis ﬁt dislocation in an Ni/Ni3Al interface: A
molecular dynamics simulations study, Model. Simul. Mater. Sci. Eng. 17 (5) (2009)
055007.
[28] T. Zhu, C.Y. Wang, Mis ﬁt dislocation networks in the γ/γ' phase interface of a Ni-
based single-crystal superalloy: Molecular dynamics simulations, Phys. Rev. B 72
(1) (2005) 014111 .
[29] T. Zhu, C.Y. Wang, Molecular dynamics study of mosaic structure in the Ni-based
single-crystal superalloy, Chin. Phys. B 15 (9) (2006) 2087 –2091.
[30] Y.L. Li, W.P. Wu, Z.G. Ruan, Molecular dynamics simulation of the evolution of
interfacial dislocation network and stress distribution of a Ni-based single-crystal
superalloy, Acta Metall. Sin-Engl. 29 (7) (2016) 689 –696.
[31] N.L. Li, W.P. Wu, K. Nie, Molecular dynamics study on the evolution of interfacial
dislocation network and mechanical properties of Ni-based single crystal super-
alloys, Phys. Lett. A 0382 (20) (2018) 1361 –1367.
[32] T. Zhu, C.Y. Wang, Y. Gan, E ﬀect of Re in γ phase, γ' phase and γ/γ' interface of Ni-
based single-crystal superalloys, Acta Mater. 58 (2010) 2045 –2055.
[33] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J.
Comput. Phys. 117 (1995) 1 –19.
[34] G.P. Purja Pun, Y. Mishin, Development of an interatomic potential for the Ni-Al
system, Philos. Mag. 89 (34 –36) (2009) 3245 –3267.
[35] A. Stukowski, V.V. Bulatov, A. Arsenlis, Automated identi ﬁcation and indexing of
dislocations in crystal interfaces, Model. Simul. Mater. Sci. Eng. 20 (8) (2012)
085007.
[36] D. Faken, H. Jónsson, Systematic analysis of local atomic structure combined with
3D computer graphics, Comput. Mater. Sci. 2 (1994) 279 –286.
[37] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO-
the open visualization tool, Model. Simul. Mater. Sci. Eng. 18 (1) (2010) 015012 .
[38] C.E. Feltner, A debris mechanism of cyclic strain hardening for F.C.C. metals, Philos.
Mag. 12 (120) (1965) 1229 –1248.
[39] Z.S. Basinski, S.J. Basinski, Fundamental aspects of low amplitude cyclic de-
formation in face-centred cubic crystals, Prog. Mater. Sci. 36 (1992) 89 –148.
[40] Z.W.
Lian, J.J. Yu, X.F. Sun, H.R. Guan, Z.Q. Hu, Temperature dependence of tensile
behavior of Ni-based superalloy M951, Mater. Sci. Eng. A 489 (1) (2008) 227 –233.
[41] T.P. Gabb, G. Welsch, R.V. Miner, J. Gayda, The low cycle fatigue deformation
response of a single-crystal superalloy at 650 °C, Mater. Sci. Eng. A 108 (1989)
189–202.
[42] M.R. Daymond, M. Preuss, B. Clausen, Evidence of variation in slip mode in a
polycrystalline nickel-base superalloy with change in temperature from neutron
diﬀraction strain measurements, Acta Mater. 55 (9) (2007) 3089 –3102.
[43] J. Zhang, L. Wang, D. Wang, G. Xie, Y. Lu, J. Shen, L. Lou, Recent progress in
research and development of Nickel-based single crystal superalloys, Acta Metall.
Sin. 55 (9) (2019) 1077 –1094 (in Chinese) .
[44] M.S. Huang, Z.H. Li, J. Tong, The in ﬂuence of dislocation climb on the mechanical
behavior of polycrystals and grain size e ﬀect at elevated temperature, Int. J.
Plasticity 61 (2014) 112 –127.
[45] U. Essmann, H. Mughrabi, Annihilation of dislocations during tensile and cyclic
deformation and limits of dislocation densities, Philos. Mag. A 40 (6) (1979)
731–756.
[46] Y. Tirupataiah, G. Sundararajan, The strain-rate sensitivitity of ﬂow stress and
strain-hardening rate in metallic materials, Mater. Sci. Eng. A 189 (1 –2) (1994)
117–127.
[47] X. Zhang, T. Jin, N.R. Zhao, Z.H. Wang, X.F. Sun, H.R. Guan, Z.Q. Hu, E ﬀect of
strain rate on the tensile behavior of a single crystal nickel-base superalloy, Mater.
Sci. Eng. A 492 (1 –2) (2008) 364 –369.
[48] K. Gopinath, A.K. Gogia, S.V. Kamat, R. Balamuralikrishnan, U. Ramamurty, Tensile
properties of Ni-Based superalloy 720Li: Temperature and strain rate e ﬀects, Metall.
Mater. Trans. A 39 (10) (2008) 2340 –2350.
[49] X.G. Wang, J.L. Liu, J.D. Liu, Y.Z. Zhou, J.G. Li, X.F. Sun, J.H. Do, B.G. Choi,
I.S. Kim, C.Y. Jo, Dependence of stacking faults in gamma matrix on low-cycle fa-
tigue behavior of a Ni-based single-crystal superalloy at elevated temperature,
Scripta Mater. 152 (2018) 94 –97.
[50] X.G. Wang, J.L. Liu, T. Jin, X.F. Sun, Tensile behaviors and deformation mechan-
isms of a nickel-base single crystal superalloy at di ﬀerent temperatures, Mater. Sci.
Eng. A 598 (2014) 154 –161.
[51] L. Wang, Y. Liu, X. Song, J. Jin, J. Du, B. Zhang, Study on the strain rate sensitivity
of a Ni-based superalloy, Min. Metals Mater. Soc. (2013) 469 –474.
[52] J. Xiong, Y. Zhu, Z. Li, M. Huang, Hydrogen-enhanced interfacial damage in Ni-
based single crystal superalloy, Scripta Mater 143 (2018) 30 –34.
[53] Z.G.
Liu, C.Y. Wang, T. Yu, In ﬂuence of Re on the propagation of a Ni/Ni 3Al in-
terface crack by molecular dynamics simulation, Model. Simul. Mater. Sci. Eng. 21
(2013) 045009 .
[54] H. Li, W. Du, Y. Liu, Molecular dynamics study of tension process of Ni-Based su-
peralloy, Acta Metall. Sin-Engl. 33 (2020) 741 –750.
[55] F. Houllé, F. Walsh, A. Prakash, E. Bitzek, Atomistic simulations of compression
tests on γ-Precipitate Containing Ni
3Al Nanocubes, Metall. Mater. Trans. A 49
(2018) 4158 –4166.
[56] H. Liu, X.M. Wang, H. Liang, Z.N. Zhao, L. Li, Z.F. Yue, C.H. Deng, The e ﬀect of void
defect on the evolution mechanisms of dislocations and mechanical properties in
nickel-based superalloys by molecular dynamics simulation of real γ/ γ’ structures,
Int. J. Solides Struct. 191 –192 (2020) 464 –472.
B. Chen, et al. Computational Materials Science 185 (2020) 109954
12
