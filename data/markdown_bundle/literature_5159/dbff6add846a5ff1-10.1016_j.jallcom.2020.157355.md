# 10.1016_j.jallcom.2020.157355

<!-- source: D:\总文献\10.1016_j.jallcom.2020.157355.pdf -->
<!-- file_sha256: 5e4c5ed085ee55562a5765fb85ca7e51abc95a79ce15bc20e1a9b9f3c81abe85 -->

## Page 1

Journal Pre-proof
Atomistic simulation studies of Ni-based superalloys
Ronghai Wu, Yunsong Zhao, Qian Yin, Jiapo Wang, Xing Ai, Zhixun Wen
PII: S0925-8388(20)33719-1
DOI: https://doi.org/10.1016/j.jallcom.2020.157355
Reference: JALCOM 157355
To appear in: Journal of Alloys and Compounds
Received Date: 21 July 2020
Revised Date: 24 September 2020
Accepted Date: 26 September 2020
Please cite this article as: R. Wu, Y. Zhao, Q. Yin, J. Wang, X. Ai, Z. Wen, Atomistic simulation studies
of Ni-based superalloys, Journal of Alloys and Compounds (2020), doi: https://doi.org/10.1016/
j.jallcom.2020.157355.
This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition
of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of
record. This version will undergo additional copyediting, typesetting and review before it is published
in its final form, but we are providing this version to give early visibility of the article. Please note that,
during the production process, errors may be discovered which could affect the content, and all legal
disclaimers that apply to the journal pertain.
© 2020 Published by Elsevier B.V.

## Page 2

Atomistic simulation studies of Ni-based superalloys
Ronghai Wua,∗, Yunsong Zhaob,∗, Qian Yina, Jiapo Wanga, Xing Aic, Zhixun Wena,∗
aSchool of Mechanics, Civil Engineering and Architecture, Northwestern Polytechnical University, Xian, 710129, PR China
bBeijing Institute of Aeronautical Materials, Beijing 100095, PR China
cState Key Laboratory of Powder Metallurgy, Central South University, Changsha 410083, PR China
Abstract
Ni-based superalloys are key materials for hot-end components of aeroengines. Considering the importance
and complex of aeroengine components, the understanding on fundamental mechanisms in Ni-based super-
alloys has been a long-standing demand and challenge. Thanks to the robustness in physics and the fast
improvement of computer technology in the past thirty years, atomistic simulation methods have become one
of the most popular techniques to study the fundamental mechanisms in Ni-based superalloys. Surprisingly,
there has been no review on the atomistic simulation studies of Ni-based superalloys. In the present work,
we provide an overview on the studies of Ni-based superalloys by atomistic simulation methods including
molecular dynamics (MD), Monte Carlo (MC) and phase ﬁeld crystal (PFC). Given the small scale of atom-
istic simulation methods, it is naturally found that the atomistic simulation studies of Ni-based superalloys
mainly focus on micro-defects (e.g. alloying element, dislocation and phase microstructure) and the inter-
action between them, as well as their relation with mechanical properties, which are reviewed in detail with
a separate section for each issue. Based on the results of atomistic simulation of Ni-based superalloys, the
simulation validity and gap with experiments are critically discussed, as well as some outlooks are proposed.
Keywords: Mechanical property; Defect; Superalloy; Molecular dynamics; Monte Carlo; Phase ﬁeld crystal
1. Introduction
The basics of Ni-based superalloys and atomistic
simulation methods are introduced in the present sec-
tion, such that one can have the necessary knowledge
for understanding atomistic simulation results of Ni-5
based superalloys. Ni-based superalloys are key ma-
terials for hot-end components of aeroengine serv-
ing at high temperature loading condition [1–3]. As
shown in Fig. 1(a)-(c), the phase microstructure of
Ni-based superalloys mainly consists of L1 2 cube-10
like γ′, DO 22 particle-like γ′′, and FCC channel-
like γ phases with characteristic size about 500 nm,
50 nm and 100 nm (channel width), respectively [4,
5]. The crystal orientation of the three phases is the
∗Corresponding author.
Email addresses: ronghai.wu@nwpu.edu.cn (Ronghai
Wu), yunsongzhao@163.com (Yunsong Zhao),
zxwen@nwpu.edu.cn (Zhixun Wen)
commonly same, which is why many Ni-based su-15
peralloys are regarded single crystals in spite of the
presence of multi-phases. Because of the single crys-
tal feature and small misﬁt of γ/γ′, the γ/γ′ inter-
face naturally has misﬁt edge dislocations. The γ′
phase is generally dislocation free and theγ matrix is20
with dislocations in undeformed samples. During de-
formation, dislocations certainly move and may cut
through theγ′ (see Fig. 1(d)) [6]. The main strength-
ening mechanism is that the precipitates impede the
motion of dislocations. Since the γ′ precipitates def-25
initely exists in all Ni-based superlloys whileγ′′ pre-
cipitates only exist in some the of Ni-based super-
lloys, γ′ is regarded as the primary strengthening
phase and γ′′ is the secondary. Apart from the main
element (i.e. Ni and Al), many alloying elements30
(e.g. Re, Mo and Co) may play important roles in
Ni-based superalloys. The mechanical properties of
Ni-based superalloys are determined by the evolu-
Preprint submitted to Elsevier September 26, 2020

## Page 3

tion and interaction between diﬀerent defects such as
point defect, phase microstructure, dislocation and so35
on. There are simulation methods at diﬀerent scales
Figure 1: Microstructures of Ni-based superalloys: (a) A high
magniﬁcation SEM image showing undeformed γ, γ′ and γ′′
phases [4]; (b) A low magniﬁcation SEM image showing un-
deformed γ (darker, channel-like) and γ′ (cube-like) [4]; (c)
Crystal unit cells of γ (FCC), γ′ (L12) and γ′′ (DO22), where
grey atoms are Ni, blue atoms are Al and red atoms are X (e.g.
V and Nb)[5]; (d) A TEM image showing dislocations (pointed
by the white arrow), deformedγ′ andγ′′ after high temperature
deformation [6].
for studying diﬀerent aspects of materials, which is
necessary to be clariﬁed here. The simulation meth-
ods can be brieﬂy classed as electronic scale, atom-
istic scale and continuum scale. The electronic scale40
methods are also called ﬁrst principle or Ab-initial
methods, which means the interaction between elec-
trons and nuclei is resolved based on quantum me-
chanics. The atomistic scale means that the mini-
mum resolution is a complete atom whose motion is45
controlled by Newtonian classical mechanics. The
atomistic simulation methods include the molecular
dynamics (MD), Monte Carlo (MC) and phase ﬁeld
crystal (PFC) that we are interested in. The con-
tinuum scale does not consider discrete particles at50
all, instead, the system is made of unite volumes
continuously connected to each other and controlled
by continuum mechanics. It is also worth clarify-
ing the kind of confusing terminology about "phase
ﬁeld". Phase ﬁeld crystal is the vocabulary specif-55
ically for phase ﬁeld method at atomistic scale. It
should be distinguished from the phase ﬁeld crystal
plasticity coupled method often used for creep sim-
ulation of Ni-based at mesoscale [7–10].Also noting
that Monte Carlo can be used at mesoscale [11, 12].60
Nevertheless, the present work focuses on molecu-
lar dynamics, atomistic Monte Carlo and phase ﬁeld
crystal studies of Ni-based superalloys, the electronic
scale ﬁrst principle studies of Ni-based superalloys is
not the considered either.65
The MD [13], MC [14] and PFC [15] methods
have been widely used to study the mechanisms and
mechanical properties of alloys. Atomistic simula-
tions are conducted by doing the following things:
1) setup of the total number of atoms N and geom-
etry structure of the system; 2) applying initial and
boundary conditions; 3) relaxing the system to equi-
librium (if appropriate); 4) running a simulation; 5)
calculating properties and analysing data. The main
diﬀerence of diﬀerent atomistic simulations is the
governing mechanism running a simulation. MD and
PFC are deterministic methods, meaning that once
the atomic setups and conditions of the system are
determined, all the details in the system evolve in the
same way no matter how many times the simulation
is repeated. The MD system is uniquely determined
the positions and velocities of atoms which are con-
trolled by Newton law:
mi
d2⃗r
dt2 = ∂U
∂⃗ri
= ⃗fi (1)
where i = 1,..., N is the number of ith atom, m is
the mass of ith atom,⃗r is the position of ith atom, U
is the potential energy (see Fig. 2) usually calculated
by eletronic ﬁrst principle method and ⃗f is the force
acting on ith atom. The total energy of the system is
calculated by:
E =
N∑
i=1
0.5mi|d⃗r
dt|2 + U (2)
where the ﬁrst term on the right hand side is the
kinetic energy of the system. The atomic structure
2

## Page 4

in PFC is represented by atom density ρ at numeric
grids. For a binary Ni-Al system, the physical inter-
pretation ofρ is the probability of ﬁnding a Al atom
at a given site and time. The basic idea of phase-ﬁeld
method is that the system evolves to minimize its to-
tal free energy under the governing of Cahn-Hillard
or Allen-Cahn equation. The general formulation of
total free energy in the PFC is expressed in functional
form [16]:
E =
∫
V
ρ
2ρ(∇2 + 1)2ρ + Hρ2 + ρ4
4 dV (3)
where∇ is the Nabla operator, H is a temperature re-
lated parameter. The integrand of Eq. (3) is a double-
well shape potential and the system equilibrium is
reached at coexistence of two states at minimums of
the double-well. Since atom density is conserved, the
governing equation of ρ follows Cahn-Hillard equa-
tion as:
β∂ρ
∂t =α∇2δF
δρ +η (4)
whereα andβ are parameters controlling the length
and time scales, η is the thermal noise term satisfy-
ing ﬂuctuation-dissipation theorem. The functional
derivative in the Cahn-Hillard equation ensures that
the system evolves to the direction of energy mini-70
mization. An advantage of PFC over MD is that the
time scale of PFC can be 10 3∼ 106 bigger than that
of MD. Thus, PFC is particularly suitable for diﬀu-
sion associated problems (e.g. nanophase precipita-
tion).75
Figure 2: Pair-interaction functions of the embedded atom
method potential in the eﬀective pair format [17].
In contrast to MD and PFC, MC is a stochastic
method which means the ensemble properties of the
system are similar while the details in the system can
not be the same after many repeats of the simulation.
MC samples a conﬁguration si from N atoms, where
i = 1,..., M. The system does not certainly be conﬁg-
uration si, but with a probability Pi. Assuming that
system moves from the current conﬁguration si to a
trial conﬁguration s j, then the potential energy diﬀer-
ence between the two conﬁgurations ∆U = U j− Ui
is calculated. If ∆U > 0 and Pi/P j < exp(−∆U/kT )
where 0 < Pi/P j < 1, k is the Boltzmann constant
and T is the temperature, or simply ∆U < 0, then
the system allows the move. The equilibrium state
of conﬁguration si requires Peq
i = exp(Ui/kT )
∑M
i exp(−Ui/kT ). For
a kinetic process, Pi becomes the probability that the
system conﬁguration is si at time t, now Pi satisﬁes:
dPi
dt =−
∑
j
W(si→ s j)Pi +
∑
j
W(s j→ si)P j (5)
where W(si, s j) = exp(−∆U/kT )
1+exp(−∆U/kT ) is the probability per
unit time of moving from si to s j. The equilib-
rium state of conﬁguration si yields dPi/dt = 0,
namely W(si, s j)/W(s j, si) = exp(−∆U/kT ). Ideally,
after proper ensemble and average of the system, all80
the properties in classical and statistical mechanics
framework can be calculated. Noting that here we
just brieﬂy introduce the basic equations of the three
atomistic methods, for more details, we refer to a
comprehensive textbook [18].85
In the present work, the atomistic simulation stud-
ies of Ni-based superalloys are reviewed. Speciﬁ-
cally, the following sections includes the review of
atomistic simulations of the point defect in the Sec-
tion 2, phase interface in the Section 3, phase mor-90
phology in the Section 4, dislocation and nano-crack
in the Section 5, as well as the interaction between
diﬀerent defects and mechanical properties in the
Section 6. Finally, the simulation validity, gap with
experiments and outlooks are critically discussed in95
the Section 7.
2. Point defect
There have been considerable investigations on the
characteristics of addition and impurity elements in
3

## Page 5

single crystal Ni-based superalloy, especially on their100
distributions. Mianroodi et al. studied the role of
Co in Ni-based superlloys by a Ni-Al-Co embedded
atom method (EAM) potential assisted PFC simu-
lations [19]. The simulation results show that Co
tends to segregate in both γ and γ′ by replacing Ni105
atoms (see Fig. 3(a)), as well as dislocation cores
and stacking faults inγ′, forming Cottrell and Suzuki
atmospheres which drag dislocations in the γ phase
from cutting into theγ′ phase. As the Co content in-
creases from 0 to 0.2, it is found that: 1) Nearly all110
the elastic constants of γ andγ′ phases decreases by
15%∼ 20% as the Co content increases from 0 to
0.2; 2) The induced lattice distortion is trivial in the
γ′ phase while considerably increased in theγ phase;
3) The intrinsic stacking fault energy increases while115
the anti-phase boundary energy decreases. The MD
and MC simulation results of the role of Re in Ni-
based superlloys show that: 1) Re tends to cluster
in γ phase by replacing Ni sites or in γ′ phase by
replacing Al, which enhances the bonding strength120
between Re and its neighboring atoms, suggesting
that the substitution atom Re inﬂuences dislocation
motion along the γ/γ′ interface [20]; 2) The diﬀu-
sion coeﬃcient of vacancy, Re and Ni all decreases
as the Re content increases from 0 to 0.1 at high tem-125
perature, since the rate of second creep stage of Ni-
based superalloys is controlled by dislocation climb
associated with interchange between atoms and va-
cancies at dislocation cores, it explains why Re en-
hances the creep property of Ni-based superlloys at130
high temperatures [21]. It is worth mentioning that
the formation of Re clusters in superalloys is still a
debatable issue. Because some atom probe observa-
tions and ﬁrst-principle calculations do not support
the formation of Re clusters [22, 23]. We are not135
intended to draw a conclusion on it. But let’s as-
sume that Re clusters have formed and it would be
interesting to estimate the possibility that Re clusters
act as obstacles and further lead to the formation of
cracks. There are many models linking dislocation140
pile-up and crack formation. We chose a classical
one based on the theory that a crack is formed pro-
vided the released elastic energy exceeds the newly
added surface energy, which further leads to a crack
formation criterion: τ =
√
3πsµ/(8(1−ν)L) [24],145
where τ is the shear stress in the glide plane act-
ing on the dislocation pile-up. The shear modulus
µ is estimated as 100 GPa and the Poisson’s ratio
is estimated as 0.3. The surface energy is the en-
ergy braking 1 m2 Re-Re bonds and can be estimated150
as (0.43× 10−19)/(0.25× 10−9)2 = 6.4 Jm−2 [23],
which agrees with typical surface energy value of
metals [25]. Given the width ofγ channel (50∼ 100
nm) and mutual average distance between Re clus-
ters (20 nm), the length of glide plane occupied by155
dislocations in the pile-up L has a maximum value
of 100 nm. Then, the calculation result leads to a
minimum τmin=3.3 GPa. It is unlikely to have such
a high stress acting on dislocation pile-up in super-
alloys. Saito investigated the distribution of alloying160
element and ordering ofγ/γ′ phases by MC based on
the Lennard-Jones potential [26]. The results show
that: 1) Al, Ti and Ta tend to locate inγ′ phase, while
Cr tends to locate in both γ and γ′ phases; 2) The
temporal evolution of alloying element composition165
inγ andγ′ phases are negligible; 3) The γ/γ′ order-
ing is performed by direct exchange of a randomly
selected single atom with one of its neighbouring
atoms.
Figure 3: Atomic structures with point defects: (a) A MD sim-
ulation, blue atoms are Ni and red atoms are H [19]; (b) a PFC
simulation [27].
The role of impurity elements in Ni-based super-170
alllys can be investigated by atomistic methods as
well. The MD simulation of the eﬀect of vacancies
in nickel shows that oxygen tends to diﬀuse by the
movement of the oxygen–vacancy pair, segregate to
lattice interstitial voids because of the strong oxy-175
gen–vacancy binding eﬀect [27]. Xiong et al. studied
the eﬀect of H element on interfacial damage by MD
[28]. It is found that H atoms tend to locate in the
crystalline lattice voids ofγ andγ′ phases as intersti-
4

## Page 6

tials (see Fig. 3(b)), as well as the core of misﬁt dis-180
locations at γ/γ′ interface, which drags the motion
of misﬁt dislocations under 300 K/250 MPa loading.
However, it is also suggested that H enhances reac-
tion and dissociation of misﬁt dislocations, promot-
ing the damage of misﬁt dislocation network after-185
wards.
3. Phase interface
The γ/γ′ interfaces are the main planar defects
in single crystal Ni-based superlloys. The previ-
ous studies mainly focus on the characteristics such190
as the interface dislocation network, interface en-
ergy of diﬀerent oriented the γ/γ′ interfaces and so
on. Mishin et al. studied the γ/γ′ interface prop-
erties in Ni-Al binary system using MC based on
the embedded atom method potential. The simula-195
tion results show the γ/γ′ interface energy ranges
from 12× 10−3 J/m2 to 46× 10−3 J/m2 at three dif-
ferent interface plane orientations (i.e. [001], [011]
and [111]) [17]. However, the MD simulations
of γ/γ′ interface in Ni-Al binary system suggested200
slight diﬀerent results [20, 29]. MD simulations
show that the interface energies are 271× 10−3 J/m2,
240× 10−3 J/m2 and 32× 10−3 J/m2 for (100), (110),
and (111) γ/γ′ interfaces, respectively. Beside, it is
found that square, rectangle and equilateral triangle205
misﬁt dislocation networks with side length 16.7 nm,
16.7 nm/23.6 nm and 16.7 nm are formed at (100),
(110), and (111) γ/γ′ interfaces, respectively (see
Fig. 4). Noting that here the three orientations are
not the loading orientations often set for studying210
the crystalline orientation dependence of mechanical
properties, but the normal directions of three diﬀer-
entγ/γ′ interface planes. The quantitative diﬀerence
between the two investigations might be caused by
diﬀerent method mechanisms or temperatures (not215
mentioned in the articles). It is worth mentioning
that which interface orientation appear in the real su-
perlloys is not solely determined by the interface en-
ergy, but by the total free energy including the local
interface energy as well as long range elastic energy220
due toγ/γ′ interface misﬁt. Yang studied the role of
γ/γ′ interface thickness in the Ni-Al binary system
by MD simulations [30, 31]. The simulation results
show that: 1) The volume fraction of the γ′ has no
Figure 4: Illustration of γ/γ′ interfaces with diﬀerent plane
orientations, dashed lines in the last column represent misﬁt
dislocation networks after system relaxation [29]: (a) [001]; (b)
[110]; (c) [111].
5

## Page 7

eﬀect on the γ/γ′ interface energy and the thickness225
of interface transition region; 2) Interface energy in-
creases linearly as the thickness of interface transi-
tion region increase; 3) The critical thickness of the
γ/γ′ interface transition region is 1.7 nm at 300 K.
The elastic responses near the γ/γ′ interface in the230
Ni-Al binary system was investigated by Farkas us-
ing MD simulations [31]. It is found that the γ/γ′
interface leads to decrement of the interplanar spac-
ing on theγ phase side while increment of the inter-
planar spacing on the γ′ side, which can be directly235
related to the forced coherency as given by the Pois-
son ratio of both phases. This eﬀect decays as the
forced coherency decays, away from the interface.
4. Phase morphology
Theγ/γ′ morphology evolution takes place during240
the precipitation that theγ′ phase precipitates fromγ
solution in heat treatment, as well as during defor-
mation of heat treated samples. The mechanism of
γ/γ′ morphology evolution can be element diﬀusion
and local ordering. Sun et al. obtained the diﬀu-245
sion coeﬃcients of Ni, Al and Re in the γ phase,γ′
phase and γ/γ′ interface by MC simulations[32]. It
turned out the order of magnitude of diﬀusion coeﬃ-
cients are 10−51 m2s−1∼ 10−39 m2s−1, 10−20 m2s−20∼
10−17 m2s−1 and 10−18 m2s−1∼ 10−14 m2s−1 at 300 K,250
600 K and 1400 K, respectively. The variation of dif-
fusion coeﬃcient of Al in the γ phase and Re in the
γ/γ′ interface with di ﬀerent Al content at a certain
temperature does not exceed one order of magnitude.
Bonvalet et al. developed a new MC for study the255
precipitation kinetics in Ni-Al-Cr tertiary superalloy
system [33]. The simulation results show that the
evolution of the mean γ′ composition is not mono-
tonic during the precipitation and phase composition
does not follow the tie line, due to complicated inter-260
play between capillarity and diﬀusion processes: the
growth rate of radius of the γ′ phase is proportional
to the diﬀusion coeﬃcient and strong diﬀusion tends
to enhance the increment of radius, while strong cap-
illarity brings the opposite eﬀect.265
The PFC simulation results of precipitation of γ′
and γ′′ phases in Ni-based superalloys show that
[35–37]: 1) the precipitation sequence is the γ′′
ﬁrst followed by γ′ for the Ni–18.7Cr–6.3Al ter-
Figure 5: PFC simulation results of a Ni-Al-V tertiary sys-
tem [34]: (a) The phase morphology projected on (001) plane,
where the red atoms are V , the green atoms are Al and the blue
atoms are Ni; (b) Dependence of the γ′ volume fraction on the
loading; (c) Dependence of theγ′′ volume fraction on the load-
ing.
6

## Page 8

tiary system, while the opposite sequence for the270
Ni–14.0Cr–11.0Al tertiary alloy [35]; 2) As the Al
content increases from 9.5 at.%Al to 17.8 at.%Al
at 1100 K, the precipitation mechanism of γ′ phase
changes from non-classical nucleation growth to
spinodal decomposition in the Ni-Al binary system275
[36]; 3) At 1230 K, the precipitation of γ′′ phase
takes place by sequential growth and coarsening pro-
cesses at lower A1 concentration regions while by si-
multaneous growth and coarsening processes at high
Al concentration regions in the Ni-Al-V tertiary sys-280
tem. The precipitation of the γ′ phase at the same
regions is reverse to that ofγ′′ phase [37]. MC simu-
lations of the equilibrium shape of phase morphology
suggest that the equilibrium shape ofγ andγ′ phases
depends on the degree of elastic anisotropy, γ′ size,285
γ/γ′ misﬁt and interface energy. Speciﬁcally, the rea-
son that the soft γ phase has plate-like or channel-
like equilibrium shape, while the hard γ′ phase has
sphere-like or dice-like equilibrium shape can be ex-
plained by elastic energy distribution[38]. Valles et290
al. simulated the directional coarsening (rafting) of
γ′ phase by the MC, in which the extend of rafting
is characterized by aspect ratio of the γ′ precipitate
[39]. Results show that it is the ratio of the elastic
moduli of γ and γ′ rather than the γ/γ′ lattice mis-295
ﬁt phases dramatically a ﬀects the directional evolu-
tion of morphology. Since the ratio of the elastic
moduli of two phases decreases with decreasing tem-
perature, the results explain why there is a criteria
temperature below which rafting does not take place300
even though the diﬀusion coeﬃcient is big enough to
let it take place. The simulation results of PFC incor-
porating stresses induced by external creep loading
and γ/γ′ misﬁt in tertiary alloys (see Fig. 5) can be
concluded as follows [34, 40, 41]: 1) the kinetics of305
phase coarsening is controlled by diﬀusion process;
2) the rafting ofγ′ is closely related to the stresses in-
duced by both external load and misﬁt stress; 3) the
γ′′ coarsens along its short axis.
5. Dislocations and nano-cracks310
MD simulations of dislocation network evolution
during system relaxation at diﬀerent γ/γ′ interface
planes (i.e. 001, 110 and 111) and temperatures
show that as the temperature increases, dislocation
networks change from regular to irregular or dis-315
appear regardless of the γ/γ′ interface planes, and
the density and stability decrease [42, 43]. Aihara
et al. also investigated the temperature dependence
of dislocation mechanisms. The results show that
under tensile deformation, dislocations need higher320
stress to propagate at low temperature than at high
temperature, and the motion speed is nearly half the
speed of sound at low temperature but much lower
at high temperature [44]. MD simulations of nano-
indentation ofγ′ show that the dislocation nucleation325
site and active slip system are signiﬁcantly aﬀected
by the crystallographic orientation, domain size, in-
denter radius and temperature [45]. In most cases,
the plastic deformation starts with nucleation of the
1/6⟨112⟩ Shockley partial dislocation (see Fig. 6).330
Figure 6: MD simulation of nano-indentation of γ′ phase with
diﬀerent domain size where L is the domain size and R is the
indenter size [45]: (a) and (d) Viewing from the [11 ¯2] direc-
tion at the beginning of indentation; (b) and (e) Viewing from
the [111] direction at the beginning of indentation; (c) and (f)
Viewing from the [11¯2] direction in the end of indentation.
Xie et al. investigated external stress dependence
of the motion of misﬁt dislocation at 5 K [46]. The
results show that at a low stress the γ/γ′ misﬁt dis-
locations move by nucleation and propagation of the
double kinks, while at a higher stress they move by335
formation of intrinsic stacking fault. Zhu et al. stud-
ied the interaction between matrix dislocations and
interfacial misﬁt dislocation networks in Ni-Al bi-
7

## Page 9

nary system by MD simulations [47]. The results
show that the role of interfacial dislocation networks340
is multiple. On one hand, the interfacial dislocation
networks serve as sinks to absorb/accommodate the
matrix dislocations, which promoting the formation
of the interfacial Lomer–Cottrell locks and⟨100⟩ dis-
location junctions which stabilize the interfacial dis-345
location networks. On the other hand, the interfacial
dislocation networks prohibit the matrix dislocations
to cut through theγ′precipitate and these matrix dis-
location segments pinned at γ/γ′ interfaces can act
as Frank–Read sources. PFC simulations of single350
dislocation climb and slip show that under a high
shear strain rate the potential energy curve evolves
monotonically with time, indicating that the disloca-
tion moves at a constant speed, while under a small
shear strain rate the dislocation moves in a periodic355
“jerky” way and the potential energy curve presents
wavy feature. The critical potential energy for the
onset of dislocation motion is much higher for climb-
ing than that for slipping [48]. PFC simulations of
the dislocation and premelting interface interaction360
at high temperature show that two alternant slip sys-
tems exist near premelting interface. Dislocations
exhibit dynamic multiplication and annihilation dur-
ing cyclic loading [49].
Lu el al. investigated the the eﬀect of crystalline365
orientation on nano-crack behavior in sample with
a notch by the PFC. Results show that for sample
misorientation of 5◦ and 20◦, the nano-crack directly
initiates at the notch due to the strain concentration
of the dislocation near the crack tip, exhibiting brit-370
tle cracking feature. However, for sample misori-
entation of 10◦ and 15◦, vacancies are ﬁrst formed
at the notch by dislocation slip, followed by growth
and merging of vacancies which lead to formation
of nano-cracks later[50]. Such nano-crack evolu-375
tion mechanism was also studied by Gao et al. by
PFC simulations. The results show that both ex-
ternal loading and temperature aﬀect the propaga-
tion path and kinetics of the nano-crack, which can
be explained by energy evolution during nano-crack380
propagation [51]. MD simulations show that at low
temperature cracks initiate by emission of Shock-
ley partial dislocations followed by formation of the
pseudo-twins on {111} planes in crack-tip. At the
higher temperature, the observed blunting of crack385
tip is induced by the emission of ⟨110⟩ superdis-
locations on {100} planes [52]. The onset of the
microtwinning at crack tip is accomplished by the
emission of Shockley partial dislocations which slip
on adjacent {111} planes (see Fig. 7) [53]. MD390
simulations of tension with intergranular and trans-
granular cracks show diﬀerent damage mechanisms
and mechanical properties. The intergranular crack
starts propagation at the densest spot of the dislo-
cation slip bands, but propagates into the γ′ phase.395
The transgranular crack propagates with an angle 45◦
to the γ/γ′ interface and dislocations move on the
⟨110⟩{¯111} slip systems. The yield stress of the trans-
granular crack model is smaller than that of the inter-
granular crack model [54].
Figure 7: MD simulation of a nano-crack tip [53]: a) The
atomic conﬁguration of the crack tip at 8 ps at 5 K, the red lines
cover the microtwinning region; (b) Dislocations emitted from
the crack tip at 8 ps and 5 K (projected on (111) plane), red
and blue balls represent Al and Ni atoms, respectively; (c) The
atomic conﬁguration of the crack tip at 30 ps and 5 K, the red
lines cover the microtwinning region; (d) The atomic conﬁgu-
ration of the crack tip at 20 ps and 600 K, the red lines cover the
microtwinning region.
400
6. Interaction between diﬀerent defects & me-
chanical properties
The interaction between point defect, linear defect
and planar defect may all have considerable eﬀect
on mechanical properties. Zhang et al. compared the405
solid solution strengthening that diﬀerentalloying el-
ements bring to dislocations in the γ phase by MD
8

## Page 10

simulations. The results show that the solid solution
strengthening increases in the order of Re, Ru and
Co [55]. MD simulations also show that the activa-410
tion energy of dislocation nucleation decreases with
the Re, W and Co contents. The strong bonding be-
tween Ni the three alloying elements inhibit crack
cleavage and promote dislocation nucleation, in the
order of W > Re > Co [56]. The Co drags dislo-415
cations in γ and inhibits dislocations to cut into γ′,
which then reverses the Co depletion inγ′ phase [19].
Among all thealloying elements, Re attracts the most
attention and more MD simulation results are as fol-
lows: 1) The activation energy of dislocation nu-420
cleation decreases with Re content, which can be
explained by the expansion of local structure when
dislocations passing through Re atoms; 2) The fre-
quency of dislocation nucleation is increased by the
Re addition regardless of temperature, indicating that425
the ductility of cracks in γ phase might be improved
by Re [57]; 3) The lattice trapping limits are not in-
ﬂuenced by Re content below 3%, while increases
with Re content from 3% to 6%, indicating that the
strength ofγ can be improved by proper Re addition430
[58]. Prakash et al. studied the interaction between
dislocations and the γ/γ′ interface during tension at
1250 K (see Fig. 8) [59]. The results show that: 1)
important interaction mechanism like cutting of the
γ′ by a pair of super-partial dislocations, the pinning435
of threading dislocations and the knitting out of mis-
ﬁt dislocations; 2) γ/γ′ interface, especially its local
curvature, and the local chemical composition dra-
matically aﬀect the γ/γ′ misﬁt dislocation network;
3) Diﬀerent samples (i.e. experiment-informed and440
idealized samples) and diﬀerent boundary conditions
(i.e. periodic and ﬁxed boundary conditions) have
non-trivial inﬂuence on the stress states in the γ and
γ′ phases [60]. The ordering induced hardening of
γ′ blocking dislocation is represented by critical re-445
solved shear stresses that a superdislocation dissoci-
ates into four partial dislocations. MD simulations
show that with a diameter of γ′ smaller than the av-
erage distance of dislocations in γ, the critical re-
solved shear stresses of the trailing dislocation of the450
superdislocation is about 40% of that of the leading
dislocation [61].
The MD simulations of γ′ compression at 300 K
reproduced some important features in experiments
Figure 8: MD simulation of the interaction between disloca-
tions and the γ/γ′ interface [59]: (a) The atomic structure ob-
tained by atom probe in experiments; (b) The MD atomic struc-
ture converted from the atom probe structure; (c) A MD simu-
lation domain showing the interaction between dislocations and
theγ/γ′ interface.
such as the lack of strain hardening, homogeneous455
deformation and high stress levels. Initial defor-
mation starts with energetically favored pseudo-
twinning instead of dislocation activity, which is the
reason of initial strain burst (see Fig. 9). Then fur-
ther deformation is performed by Shockley partial460
dislocations [62]. However, the plasticity initiation
mechanism is di ﬀerent in system of γ channel con-
taining theγ′ precipitate, which shows that the plas-
tic deformation of the γ is initiated by the Shockley
partial dislocations near the γ′ corners followed by465
the formation of pseudo-twins, regardless of the pre-
cipitate size, corner curvature, surface roughness and
strain rate [63]. Yashiro et al. investigated the tensile
loading along ⟨001⟩ at 1273 K by MD simulations
[64, 65]. It is found that dislocations nucleate and470
evolve as follows: 1) A dislocation loop nucleates
at corner of γ/γ′ interface, then bowing out in the γ
channel; 2) the dislocation loop dissociates into two
partial dislocations when the tip of the loop reaches
the adjacentγ′ precipitate; 3) the two partial disloca-475
tions move in opposite directions so that the stacking
fault between them is extended till they are blocked
byγ/γ′ interfaces; 4) Due to the high energy barrier
of ordering change when dislocations in γ channel
cut into γ′ precipitate, dislocations piled up at γ/γ′480
interfaces do not penetrateγ′ precipitate until the lo-
cal stress is big enough (about 3 GPa) for the nucle-
ation of superpartial dislocations.
MD simulations of tensile loading along ⟨001⟩,
and under diﬀerent strain rates (from 10 8 s−1 to485
1010 s−1) and diﬀerent temperatures (from 0 K to
1200 K) show that the deformation mechanisms and
9

## Page 11

mechanical properties depend on conditions [66–68].
At the low strain rate, the square dislocation network
is locally damaged at one node and a/2⟨110⟩ dislo-490
cations penetrate theγ′ precipitate, while at the high
strain rate, the square dislocation network is dam-
aged four nodes simultaneously and no dislocations
penetrate the γ′ precipitate, leading to high strength
and low plasticity at high strain rate. Besides, the495
initial misﬁt, elastic modulus and strength decrease,
while plasticity increases with increasing tempera-
ture. Moreover, tension–compression asymmetry is
observed regardless of deformation conditions, due
to the sign of misﬁt stress. Under cyclic loading,500
theγ/γ′ interface serves as barrier for fatigue crack
propagation [69]. Wang et al. investigated the depen-
dence of tensile properties on the crystalline orienta-
tion and nano-cavity in the Ni-Al binary system [70–
72]. The results show that dislocations tend to nucle-505
ate from the stress concentration region at the nano-
cavity edge (see Fig. 10) and the dislocation density
decreases with the order of [110], [111] and [100]
[72]. The nano-cavity sizes and volume fraction sig-
niﬁcantly aﬀect mechanical properties like Young’s510
modulus, incipient yield stress and incipient yield
strain. The critical stresses under [100], [110] and
[111] orientation loading are 6.97 GPa, 6.77 GPa and
7.31 GPa, respectively. It is worth mentioning that
the mechanical properties calculated by MD simu-515
lations are strongly inﬂuenced by the sixth nearest
neighboring shell, a linear elastic behaviour is pre-
sented without the pair interaction of the sixth near-
est neighboring shell [73].
7. Discussion and outlooks520
As has been presented above, atomistic meth-
ods have been used to study various aspects of mi-
crostructure, defect and mechanical behavior in Ni-
based superalloys, which proves that the power of
atomistic methods. Nevertheless, every simulation525
method has its limits, it is not beneﬁcial to discuss the
results critically before they are trusted. The applica-
bility of a simulation method is basically determined
by its scale. The lattice parameter of superalloys is
about 3× 10−10 m and the maximum realistic num-530
ber of atoms that MD can handle is 10 3 in one spa-
cial dimension of a 3D simulation, indicating that the
Figure 9: MD simulation results of Ni-Al binaryγ′ under [001]
compression, where orange, red and white atoms represent per-
fectγ′ structure orange, complex stacking faults and other de-
fects ,respectively: (a)-(c) atomic structures at diﬀerent strains;
(d) Stress–strain curves and evolution of normalized contact
area for 11 nm (black) and 25 nm (red) cubes.
10

## Page 12

Figure 10: MD simulation results of the interaction between
dislocations and a nano-cavity under [001] tensile loading,
where upper ﬁgure shows atomic structure of the dislocation
and nano-cavity, the middle ﬁgure shows the stress-strain curve
corresponding to mechanical properties at representative points
(a)-(e), and the lower ﬁgure shows the evolution of nano-cavity
fraction with time [70].
maximum length of MD simulation domain is below
the characteristic length of γ′ phase microstructure
500 nm (see Fig. 1(b)). The PFC is much more com-535
putationally expensive than MD, since MD solves
Newtonian equations of motion which are ordinary
diﬀerential equations while PFC solves non-linear
partial diﬀerential equations. This is the main rea-
son that most PFC simulations are in 2D [74], which540
also indicates that PFC is not suitable for simulat-
ing γ′ phase microstructure in terms of the length
scale. Only under long-term and elevated tempera-
ture loading (e.g. creep and fatigue) can γ′ phase
microstructure have essential evolution, due to the545
diﬀusion control feature of γ′ evolution. The diﬀu-
sion coeﬃcient increases with temperature and diﬀu-
sion coeﬃcient in Ni-based superalloy is in the range
of 10−14 m2s−1∼ 10−16 m2s−1 even at very high tem-
perature, meaning that atoms need 25 s ∼ 2500 s to550
travel a characteristic length of γ′ (i.e. 500 nm), and
several hours are needed to observe essential change
ofγ′ morphology. The typical time range of MD can
handle is 10−12 s ∼ 10−9 s and even the time scale
of PFC can be extended to 10−6 s, however, still too555
small compare with the characteristic time scale ofγ′
morphology evolution. Hence, atomic methods are
not suitable for studying the γ′ morphology evolu-
tion no matter in terms of length scale or in term of
time scale. If simulating the γ′ with PFC, γ′ mor-560
phology and volume fraction discrepant with exper-
iments may obtained (see Fig. 5(a)). However, the
PFC might be suitable for studying the evolution of
γ′′ morphology, since the the characteristic length of
γ′′ is 30 nm∼ 50 nm (see Fig. 1(a)) which is possible565
for big 2D PFC simulations. Understanding element
partition during the evolution of nano phases is ben-
eﬁcial for revealing the role of keyalloying elements
in alloys [75].
It is worth mentioning the gap between atomistic570
simulation and experimental results due to the ultra-
high strain rate caused by the ultra-small time scale
of atomistic simulations. To have 10 −3 strain above
which suﬃcient deformation is generated, the strain
rates need to be higher than 106 s−1 in MD and 103 s−1575
in PFC, which are much higher than real deforma-
tion rate of Ni-based superalloys [76]. Ni-based su-
peralloys usually undergo creep and fatigue defor-
mation in real service as well as experimental study,
11

## Page 13

the strain rate is 10 −4 s−1 ∼ 10−9 s−1 in creep and580
10−3 s−1 ∼ 1 s−1 in fatigue. In atomistic simula-
tions, the initial microstructures are typically dislo-
cation free, since even dislocations are prescribed
they vanish during the relaxation of the system be-
fore loading. After the onset of loading, dislocations585
mostly nucleate from dislocation free crystal, lead-
ing to ultrahigh yield stress about 5 GPa ∼ 10 GPa,
which is never observed in experiments. Because
in real Ni-based superalloys, dislocations with den-
sity about 12 m−2 constantly exist in γ phase even590
after long time heat treatment before deformation.
Plastic deformation starts by bowing out of disloca-
tions in γ phase at high temperature or cut through
γ′ at low temperature, leading to yield stress lower
than 1 GPa [77]. The ultra-high strain rate of atom-595
istic simulations also causes dislocation mechanism
bias to experimental results. In atomistic simula-
tions, dislocations typically nucleate as partial dis-
locations since the very beginning of plastic defor-
mation, regardless of the temperature. Despite that600
the dislocation reaction that a a/2[110] perfect dis-
location decomposes into two partial dislocations
a/2[110] → a/6[211] + a/6[21¯1] or a/2[0¯11] →
3/a[1¯12] + a/6[¯2¯1¯1 is energetically favorable, the
stacking fault naturally formed between two partial605
dislocations is a barrier which might not be overcame
at low stress. Hence, in experiments dislocations are
2/a⟨110⟩ perfect dislocations inγ phase during most
of the time of plastic deformation at high tempera-
ture. Only at the late stage of high temperature defor-610
mation when severe dislocation pile-up atγ/γ′ inter-
face provides enough force to the front dislocations
can the reaction take place and partial dislocations
form [78, 79]. While at a low temperature, since the
loading is usually much bigger, partial dislocations615
may form at the early stage of plastic deformation
[80].
As atomistic methods cannot simulate microstruc-
ture in micron scale, it would be interesting to
develop multiscale simulation framework to reveal620
more mechanisms in Ni-based superalloys. There
are two basic types of multiscale simulation: se-
quential and concurrent multiscale simulation meth-
ods. The former means that simulations at diﬀer-
ent scales are conducted sequentially and results of625
the smaller scale simulation are used as inputs for
the larger scale simulation. The latter means that
simulations at diﬀerent scales are conducted concur-
rently and the quantities that the larger scale simu-
lation needed from the smaller scale simulation are630
calculated on-the-ﬂy. Both types of multiscale simu-
lation associated with atomistic methods can be per-
formed to beneﬁt the investigations of Ni-based su-
peralloys in many ways. The dislocation dynamics
is an important method to quantitatively study dis-635
location mechanisms and as its name implies, dy-
namics (e.g. velocity law) is a key issue for this
method. The stress-velocity relation and drag coeﬃ-
cient are aﬀected by temperature, alloying elements
and so on, which need atomistic simulations to accu-640
rately identify [81]. Some high temperature informa-
tion of superalloys like lattice parameter,γ/γ′ misﬁt
and interface energy are di ﬀerent to obtain by ex-
periments, but must be needed for continuum scale
methods for quantitative study of phase microstruc-645
tures [82]. In this case, one can set up atomistic
simulations with γ/γ′ structures to obtain these pa-
rameters at high temperatures. The role of disloca-
tion pattern in crack formation during cyclic load-
ing of superalloys is still debatable. As crack initi-650
ation is intrinsically an atomistic process and dislo-
cation pattern is above atomistic scale, one needs a
concurrent multiscale framework coupling atomistic
methods and dislocation dynamics to resolve the is-
sue [83]. The interaction between dislocations and655
obstacles (e.g. void and γ′ phase) in sueralloys can
be investigated by concurrent atomistic–continuum
simulations, with atomic resolution around the ob-
stacles to study interactions at obstacle interfaces and
ﬁnite element coarse resolution away from the obsta-660
cles to study the long range continuum level interac-
tions [84].
Based on what have been discussed above, we pro-
pose some suggestions for future atomistic simula-
tion study of Ni-based superalloys. The ﬁrst is to in-665
corporate more alloying elements into atomistic sim-
ulations, such that the composition is closer to real
Ni-based superalloys. Despite that distribution of al-
loying elements in the tertiary and quarternary alloy
system has been widely studied, the number of ele-670
ment is still much less the real Ni-based superalloys.
Apart from that, most of the past atomistic simula-
tions on phase interface, dislocation, nano-crack, de-
12

## Page 14

fect interaction and mechanical property were based
on the binary Ni-Al system. However, experiments675
have shown that some the alloying elements dra-
matically aﬀect the defect evolution and mechanical
property during deformation, in which the mecha-
nisms are waiting for atomistic methods to reveal and
some of the questions even can only be answered by680
atomistic methods. For example, the Ta, Mo and Re
are believed to have signiﬁcant roles by experimen-
tal study [85–87], but what is the combined eﬀect
on defects and mechanical properties? Since the mi-
croscopy observations are conducted at interrupted685
samples, what is the dynamic process of the their
evolutions? How the force or energy motivates the
evolutions? Another suggestion for future study is
to focus more on cyclic loading and high tempera-
ture rather than uniaxial loading and low tempera-690
ture like most of the past atomistic simulations did,
because the cyclic loading and high temperature is
closer to real service condition of Ni-based superal-
loys. The Ni-based superalloys in aero-engines are
constantly under high frequency cyclic shakes, due695
to aerodynamic excitation force, aerocraft speed al-
ternation and so on. The mechanisms under cyclic
loading might be much complicated than that under
uniaxial loading and might not be suﬃcient to sim-
ply deduce from mechanisms under uniaxial loading.700
The last but not the least, as microscopies at atomic
scale (e.g. 3D atom probe) are increasingly popu-
lar, experimentally informed samples for atomistic
simulations should be used more often. In this way,
some mechanisms existed in experiments but waived705
by the usage of idealized samples can be recovered in
atomistic simulations. For instance, the importance
of γ/γ′ interface curvature had been ignored since
idealized MD simulation samples were alwayscubes
with 90◦ conners, until Prakash et al. recently used710
an atom probe informed sample [59].
8. Conclusion
The studies of Ni-based superalloys by MD, MC
and PFC in the past thirty years are critically re-
viewed in the present work. The following conclu-715
sion can be drawn:
1. The atomistic simulations of Ni-based super-
alloys have covered most of the microstruc-
tures and mechanical properties, including ad-
dition element, impurity element, phase in-720
terface, phase morphology, dislocation, nano-
crack, nano-cavity and the their interactions,
as well as tensile and compressive properties
at diﬀerent microstructures and loading condi-
tions.725
2. Most of the simulation results well explained
the evolution of microstructures and mechani-
cal properties by underlying physics (e.g. en-
ergy) and can bring useful information for the
design of new Ni-based superlloys. Neverthe-730
less, a few debatable results are obtained due to
improper understanding on the scales of atom-
istic methods and microstrcuture features (e.g.
PFC simulation of the γ′ evolution). There is
a gap between the simulated and experimen-735
tal mechanical properties induced by the small
scale nature of atomistic methods, which always
deserves additional attention when one tries to
understand the simulated mechanical property
of Ni-based superalloys.740
3. Three suggestions are proposed for the fu-
ture atomistic simulations of Ni-based superal-
loys, which are incorporating more addition ele-
ments, switching from uniaxial loading to cyclic
loading and using experimentally informed sim-745
ulation samples, such that the simulations are
closer to the experiments and the simulation re-
sults are more useful both in terms of under-
standing mechanisms and developing the next
generation of Ni-based superlloys.750
Acknowledgment
The research is supported by the National Natu-
ral Science Foundation of China (NO. 12002275),
National Science and Technology Major Project
(NO. 2017-IV-0003-0040), Opening Project of State755
Key Laboratory of Solidiﬁcation Processing (NO.
SKLSP201833), Opening Project of Applied Me-
chanics and Structure Safety Key Laboratory of
Sichuan Province (NO. SZDKF-1803), and the Fun-
damental Research Funds for the Central Universi-760
ties in NWPU (NO. 31020180QD088), Natural Sci-
ence Foundation of Shaanxi Province (NO. 2020JQ-
125).
13

## Page 15

[1] H. Long, S. Mao, Y . Liu, Z. Zhang, X. Han, Microstruc-
tural and compositional design of Ni-based single crys-765
talline superalloys—A review, Journal of Alloys and
Compounds 743 (2018) 203–220.
[2] R. Vilar, A. Almeida, Repair and manufacturing of single
crystal Ni-based superalloys components by laser powder
deposition-A review, Journal of Laser Applications 27770
(2015).
[3] Y . Zhao, J. Zhang, F. Song, M. Zhang, Y . Luo, H. Zhao,
D. Tang, E ﬀect of trace boron on microstructural evo-
lution and high temperature creep performance in Re-
contianing single crystal superalloys, Progress in Natural775
Science: Materials International (2020).
[4] B. Wilson, G. Fuchs, The eﬀect of secondary γ′ on the
primary creep behavior of single-crystal nickel-base su-
peralloys, Metallurgical and Materials Transactions A 41
(2010) 1235–1245.780
[5] A. J. Knowles, L. Reynolds, V . A. V orontsov, D. Dye,
A nickel based superalloy reinforced by both Ni 3Al and
Ni3V ordered-FCC precipitates, Scripta Materialia 162
(2019) 472–476.
[6] L. A. Jacome, P. Nörtershäuser, J.-K. Heyer, A. Lahni,785
J. Frenzel, A. Dlouhy, C. Somsen, G. Eggeler, High-
temperature and low-stress creep anisotropy of single-
crystal superalloys, Acta Materialia 61 (2013) 2926–
2943.
[7] C. Wang, M. A. Ali, S. Gao, J. V . Goerler, I. Steinbach,790
Combined phase-ﬁeld crystal plasticity simulation of P-
and N-type rafting in Co-based superalloys, Acta Materi-
alia 175 (2019) 21–34.
[8] A. Gaubert, Y . Le Bouar, A. Finel, Coupling phase ﬁeld
and viscoplasticity to study rafting in Ni-based superal-795
loys, Philosophical Magazine 90 (2010) 375–404.
[9] R. Wu, M. Zaiser, S. Sandfeld, A continuum approach
to combined γ/γ′ evolution and dislocation plasticity in
Nickel-based superalloys, International Journal of Plas-
ticity 95 (2017) 142–162.800
[10] R. Wu, S. Sandfeld, Insights from a minimal model of
dislocation-assisted rafting in single crystal Nickel-based
superalloys, Scripta Materialia 123 (2016) 42–45.
[11] X. Wang, Z. J. Yang, J. Yates, A. Jivkov, C. Zhang, Monte
Carlo simulations of mesoscale fracture modelling of con-805
crete with random aggregates and pores, Construction and
Building Materials 75 (2015) 35–45.
[12] X. Wang, Z. Yang, A. P. Jivkov, Monte Carlo simulations
of mesoscale fracture of concrete with random aggregates
and pores: a size eﬀect study, Construction and Building810
Materials 80 (2015) 262–272.
[13] V . Yamakov, D. Wolf, S. Phillpot, A. Mukherjee,
H. Gleiter, Deformation-mechanism map for nanocrys-
talline metals by molecular-dynamics simulation, Nature
Materials 3 (2004) 43–47.815
[14] Z. Mao, C. K. Sudbrack, K. E. Yoon, G. Martin, D. N.
Seidman, The mechanism of morphogenesis in a phase-
separating concentrated multicomponent alloy, Nature
Materials 6 (2007) 210–216.
[15] P. Stefanovic, M. Haataja, N. Provatas, Phase-ﬁeld crys-820
tals with elastic interactions, Physical Review Letters 96
(2006) 225504.
[16] K. Elder, M. Katakowski, M. Haataja, M. Grant, Model-
ing elasticity in crystal growth, Physical review letters 88
(2002) 245701.825
[17] Y . Mishin, Atomistic modeling of the γ andγ′-phases of
the Ni–Al system, Acta Materialia 52 (2004) 1451–1467.
[18] S. Yip, Handbook of materials modeling, Springer Sci-
ence & Business Media, 2007.
[19] J. R. Mianroodi, P. Shanthraj, P. Kontis, J. Cormier,830
B. Gault, B. Svendsen, D. Raabe, Atomistic phase
ﬁeld chemomechanical modeling of dislocation-solute-
precipitate interaction in Ni–Al–Co, Acta Materialia 175
(2019) 250–261.
[20] T. Zhu, C. Wang, Y . Gan, Eﬀect of Re inγ phase,γ′ phase835
andγ/γ′ interface of Ni-based single-crystal superalloys,
Acta Materialia 58 (2010) 2045–2055.
[21] K. N. Goswami, A. Mottura, A kinetic Monte Carlo study
of vacancy diﬀusion in non-dilute Ni-Re alloys, Materials
Science and Engineering: A 743 (2019) 265–273.840
[22] A. Mottura, N. Warnken, M. K. Miller, M. Finnis,
R. Reed, Atom probe tomography analysis of the dis-
tribution of rhenium in nickel alloys, Acta Materialia 58
(2010) 931–942.
[23] A. Mottura, M. Finnis, R. Reed, On the possibility of845
rhenium clustering in nickel-based superalloys, Acta Ma-
terialia 60 (2012) 2866–2872.
[24] J. R. Low Jr, The fracture of metals, Progress in materials
science 12 (1963) 3–96.
[25] W. Tyson, Surface energies of solid metals, Canadian850
Metallurgical Quarterly 14 (1975) 307–314.
[26] Y . Saito, H. Harada, The Monte Carlo simulation of or-
dering kinetics in Ni-base superalloys, Materials Science
and Engineering: A 223 (1997) 1–9.
[27] C. Zou, Y . K. Shin, A. C. van Duin, H. Fang, Z. Liu,855
Molecular dynamics simulations of the eﬀects of vacan-
cies on nickel self-diﬀusion, oxygen diﬀusion and oxida-
tion initiation in nickel, using the ReaxFF reactive force
ﬁeld, Acta Materialia 83 (2015) 102–112.
[28] Y . Tao, X. Hongxian, W. Chongyu, E ﬀect of H impurity860
on misﬁt dislocation in Ni-based single-crystal superal-
loy: molecular dynamic simulations, Chinese Physics B
21 (2012) 026104.
[29] T. Zhu, C. Wang, Misﬁt dislocation networks in the γ/γ′
phase interface of a Ni-based single-crystal superalloy:865
Molecular dynamics simulations, Physical Review B 72
(2005) 014111.
[30] X. Yang, W. Hu, X. Zhang, Atomistic simulation for
theγ′-phase volume fraction dependence of the interfacial
behavior of Ni-base superalloy, Applied Surface Science870
264 (2013) 563–569.
[31] D. Farkas, M. de Campos, R. de Souza, H. Goldenstein,
Atomistic structure of the coherent interface, Scripta Met-
allurgica et Materialia 30 (1994) 367–371.
[32] M. Sun, Z. Li, G. Zhu, W. Liu, S. Liu, C. Wang, Diﬀusion875
14

## Page 16

in Ni-based single crystal superalloys with density func-
tional theory and kinetic Monte Carlo method, Commu-
nications in Computational Physics 20 (2016) 603–618.
[33] M. Bonvalet, T. Philippe, X. Sauvage, D. Blavette, Mod-
eling of precipitation kinetics in multicomponent systems:880
Application to model superalloys, Acta Materialia 100
(2015) 169–177.
[34] K. Yang, M. Zhang, Z. Chen, X. Fan, Microscopic phase-
ﬁeld study for mechanisms of directional coarsening and
the transformation of rafting types in Ni-Al-V ternary al-885
loys, Computational Materials Science 62 (2012) 160–
168.
[35] Y . Lu, Z. Chen, Y . Wang, J. Zhang, K. Yang, Phase-ﬁeld
study the eﬀect of elastic strain energy on the incubation
period of Ni-Cr-Al alloys, Computational Materials Sci-890
ence 50 (2011) 1925–1931.
[36] Y . L. Lu, Z. Chen, Y . X. Wang, Microscopic phase-ﬁeld
simulation of the early precipitation mechanism of Ni3Al
phase in Ni-Al alloys, Materials Letters 62 (2008) 1385–
1388.895
[37] Y . Li, Z. Chen, Y . Lu, Y . Wang, Coarsening kinetics of
intermetallic precipitates in Ni75AlxV25-x alloys, Journal
of Materials Research 22 (2007) 61–67.
[38] J. K. Lee, J. H. Choy, On the shape evolution of coherent
precipitates: discrete atom method, MRS Online Proceed-900
ings Library Archive 398 (1995).
[39] J. Valles, D. Arrell, Monte Carlo simulation of anisotropic
coarsening in nickel-base superalloys, Acta metallurgica
et materialia 42 (1994) 2999–3008.
[40] K. Yang, Z. Chen, Y . Wang, X. Fan, Microscopic905
phase-ﬁeld study on directional coarsening mechanism
caused by interaction between precipitates in Ni-Al-V al-
loy, Transactions of Nonferrous Metals Society of China
23 (2013) 193–200.
[41] Y . Lu, C. Zheng, Y . Li, Y . Wang, Microscopic phase-ﬁeld910
simulation coupled with elastic strain energy for precip-
itation process of Ni-Cr-Al alloys with low Al content,
Transactions of Nonferrous Metals Society of China 17
(2007) 64–71.
[42] W. Wu, Y . Guo, Y . Wang, R. Mueller, D. Gross, Molecular915
dynamics simulation of the structural evolution of misﬁt
dislocation networks at γ/γ′ phase interfaces in Ni-based
superalloys, Philosophical Magazine 91 (2011) 357–372.
[43] B. Chen, W. Wu, M. Chen, Orientation-dependent mor-
phology and evolution of interfacial dislocation networks920
in Ni-based single-crystal superalloys: A molecular dy-
namics simulation, Acta Mechanica Solida Sinica (2020)
1–12.
[44] T. Aihara, T. Sho, Molecular dynamics simulation on de-
formation dynamics of Ni and Ni 3Al single crystals and925
Ni/Ni3Al composite crystal, Materials Transactions, JIM
40 (1999) 1281–1287.
[45] K. Xiong, H. Lu, J. Gu, Atomistic simulations of
the nanoindentation-induced incipient plasticity in Ni 3Al
crystal, Computational Materials Science 115 (2016)930
214–226.
[46] H. Xie, C. Wang, T. Yu, Motion of misﬁt dislocation in
an Ni/Ni3Al interface: a molecular dynamics simulations
study, Modelling and Simulation in Materials Science and
Engineering 17 (2009) 055007.935
[47] Y . Zhu, Z. Li, M. Huang, Atomistic modeling of the in-
teraction between matrix dislocation and interfacial misﬁt
dislocation networks in Ni-based single crystal superal-
loy, Computational Materials Science 70 (2013) 178–186.
[48] Y . Gao, S. Quan, Q. Deng, Z. Luo, C. Huang, K. Lin,940
Phase-ﬁeld-crystal simulation of edge dislocation climb-
ing and gliding under shear strain, Acta Physica Sinica 64
(2015) 106104.
[49] Y . Gao, L. Huang, Q. Deng, W. Zhou, Z. Luo, K. Lin,
Phase ﬁeld crystal simulation of dislocation conﬁguration945
evolution in dynamic recovery in two dimensions, Acta
Materialia 117 (2016) 238–251.
[50] Y . Lu, Y . Gao, Q. Deng, Z. Liu, Y . Li, Z. Huang, Z. Luo,
Eﬀect of crystal orientation on initiation and propagation
of crack: Phase ﬁeld crystal model study, The European950
Physical Journal B 92 (2019) 194.
[51] G. Yingjun, L. Zhirong, H. Lilin, M. Hong, H. Chuang-
gao, L. Kui, Phase ﬁeld crystal study of nano-crack
growth and branch in materials, Modelling and Simu-
lation in Materials Science and Engineering 24 (2016)955
055010.
[52] H. Xie, C. Wang, T. Yu, Atomistic simulation of fracture
in Ni3Al, Journal of Materials Research 23 (2008) 1597–
1603.
[53] H. Xie, L. Bo, T. Yu, Atomistic simulation of microtwin-960
ning at the crack tip in L12Ni3Al, Philosophical Magazine
92 (2012) 1542–1553.
[54] J. Yu, Q. Zhang, R. Liu, Z. Yue, M. Tang, X. Li, Molec-
ular dynamics simulation of crack propagation behaviors
at the Ni/Ni 3Al grain boundary, Rsc Advances 4 (2014)965
32749–32754.
[55] X. Zhang, H. Deng, S. Xiao, X. Li, W. Hu, Atomistic
simulations of solid solution strengthening in Ni-based
superalloy, Computational Materials Science 68 (2013)
132–137.970
[56] D. Wang, C. Wang, T. Yu, Eﬀects of Re, W and Co on
dislocation nucleation at the crack tip in the γ -phase of
Ni-based single-crystal superalloys by atomistic simula-
tion, Royal Society Open Science 6 (2019) 190441.
[57] Z. Liu, C. Wang, T. Yu, Eﬀect of Re on dislocation nucle-975
ation from crack tip in Ni by atomistic simulation, Com-
putational Materials Science 97 (2015) 127–135.
[58] S. Liu, C. Wang, T. Yu, Z. Liu, Eﬀect of Re on lattice trap-
ping inγ′-Ni3Al cracks by atomistic simulation, Compu-
tational Materials Science 97 (2015) 102–108.980
[59] A. Prakash, J. Guénolé, J. Wang, J. Müller, E. Spiecker,
M. J. Mills, I. Povstugar, P. Choi, D. Raabe, E. Bitzek,
Atom probe informed simulations of dislocation–
precipitate interactions reveal the importance of local in-
terface curvature, Acta Materialia 92 (2015) 33–45.985
[60] A. Prakash, E. Bitzek, Idealized vs. realistic microstruc-
tures: An atomistic simulation case study on γ/γ′ mi-
15

## Page 17

crostructures, Materials 10 (2017) 88.
[61] C. Kohler, P. Kizler, S. Schmauder, Atomistic simulation
of the pinning of edge dislocations in Ni by Ni 3Al pre-990
cipitates, Materials Science and Engineering: A 400-401
(2005) 481–484.
[62] J. Amodeo, C. Begau, E. Bitzek, Atomistic simulations
of compression tests on Ni 3Al nanocubes, Materials Re-
search Letters 2 (2014) 140–145.995
[63] F. Houllé, F. Walsh, A. Prakash, E. Bitzek, Atomistic sim-
ulations of compression tests on γ-precipitate containing
Ni3Al nanocubes, Metallurgical and Materials Transac-
tions A 49 (2018) 4158–4166.
[64] K. Yashiro, M. Naito, Y . Tomita, Molecular dynamics1000
simulation of dislocation nucleation and motion at γ/γ′
interface in Ni-based superalloy, International Journal of
Mechanical Sciences 44 (2002) 1845–1860.
[65] K. Yashiro, Y . Tabata, Y . Tomita, Molecular dynamics
study on the characteristics of edge and screw disloca-1005
tions in γ/γ′ microstructure of Ni-based superalloy, in:
IUTAM Symposium on Mesoscopic Dynamics of Frac-
ture Process and Materials Strength, Springer, 2004, pp.
59–68.
[66] W. Wu, Y . Guo, Y . Wang, Evolution of misﬁt dislocation1010
network and tensile properties in Ni-based superalloys: a
molecular dynamics simulation, Science China Physics,
Mechanics and Astronomy 55 (2012) 419–427.
[67] N. Li, W. Wu, K. Nie, Molecular dynamics study on
the evolution of interfacial dislocation network and me-1015
chanical properties of Ni-based single crystal superalloys,
Physics Letters A 382 (2018) 1361–1367.
[68] Y . Li, W. Wu, Z. Ruan, Molecular dynamics simulation of
the evolution of interfacial dislocation network and stress
distribution of a Ni-based single-crystal superalloy, Acta1020
Metallurgica Sinica (English Letters) 29 (2016) 689–696.
[69] L. Ma, S. Xiao, H. Deng, W. Hu, Tensile mechanical
properties of Ni-based superalloy of nanophases using
molecular dynamics simulation, Physica Status Solidi (b)
253 (2016) 726–732.1025
[70] J. Wang, J. Liang, Z. Wen, Z. Yue, Atomic simula-
tion of void location eﬀect on the void growth in Nickel-
based single crystal, Computational Materials Science
160 (2019) 245–255.
[71] J. Wang, Z. Yue, Z. Wen, D. Zhang, C. Liu, Orientation1030
eﬀects on the tensile properties of single crystal nickel
with nanovoid: Atomistic simulation, Computational Ma-
terials Science 132 (2017) 116–124.
[72] Z. Wen, J. Wang, Y . Wu, K. Zhou, Z. Yue, Atomistic
simulation analysis of the eﬀects of void interaction on1035
void growth and coalescence in a metallic system, Current
Applied Physics 18 (2018) 744–751.
[73] J. Alizadeh, M. Panjepour, M. Ahmadian, Modeling the
stretch behavior of the single-crystal Ni-Al alloy and its
molecular dynamics simulation, Physics of the Solid State1040
62 (2020) 83–91.
[74] N. Provatas, J. Dantzig, B. Athreya, P. Chan, P. Ste-
fanovic, N. Goldenfeld, K. Elder, Using the phase-ﬁeld
crystal method in the multi-scale modeling of microstruc-
ture evolution, JOM 59 (2007) 83–90.1045
[75] V . Fallah, N. Ofori-Opoku, J. Stolle, N. Provatas, S. Es-
maeili, Simulation of early-stage clustering in ternary
metal alloys using the phase-ﬁeld crystal method, Acta
Materialia 61 (2013) 3653–3666.
[76] X. Zhang, T. Jin, N. Zhao, Z. Wang, X. Sun, H. Guan,1050
Z. Hu, Eﬀect of strain rate on the tensile behavior of a
single crystal nickel-base superalloy, Materials Science
and Engineering: A 492 (2008) 364–369.
[77] W. W. Milligan, S. D. Antolovich, Yielding and deforma-
tion behavior of the single crystal superalloy PW A 1480,1055
Metallurgical Transactions A 18 (1987) 85–95.
[78] A. Epishin, T. Link, Mechanisms of high-temperature
creep of nickel-based superalloys under low applied
stresses, Philosophical Magazine 84 (2004) 1979–2000.
[79] L. A. Jácome, G. Göbenli, G. Eggeler, Transmission elec-1060
tron microscopy study of the microstructural evolution
during high-temperature and low-stress (011)[111] shear
creep deformation of the superalloy single crystal LEK
94, Journal of Materials Research 32 (2017) 4491–4502.
[80] X. Wu, A. Dlouhy, Y . Eggeler, E. Spiecker, A. Kostka,1065
C. Somsen, G. Eggeler, On the nucleation of planar faults
during low temperature and high stress creep of single
crystal Ni-base superalloys, Acta Materialia 144 (2018)
642–655.
[81] E. Bitzek, P. Gumbsch, Dynamic aspects of dislocation1070
motion: atomistic simulations, Materials Science and En-
gineering: A 400 (2005) 40–44.
[82] R. Wu, Y . Zhao, Y . Liu, X. Ai, High temperature creep
mechanisms of a single crystal superalloy: A phase-ﬁeld
simulation and microstructure characterization, Progress1075
in Natural Science: Materials International (2020).
[83] G. Anciaux, T. Junge, M. Hodapp, J. Cho, J. Molinari,
W. Curtin, The coupled atomistic/discrete-dislocation
method in 3d part I: Concept and algorithms, Journal of
the Mechanics and Physics of Solids 118 (2018) 152–171.1080
[84] L. Xiong, S. Xu, D. L. McDowell, Y . Chen, Concurrent
atomistic–continuum simulations of dislocation–void in-
teractions in fcc crystals, International Journal of Plastic-
ity 65 (2015) 33–42.
[85] J. Zhang, Eﬀect of Ti and Ta on hot cracking susceptibil-1085
ity of directionally solidiﬁed Ni-based superalloy IN792,
Scripta Materialia 48 (2003) 677–681.
[86] J. Zhang, J. Li, T. Jin, X. Sun, Z. Hu, Eﬀect of Mo concen-
tration on creep properties of a single crystal nickel-base
superalloy, Materials Science and Engineering: A 5271090
(2010) 3051–3056.
[87] X. Wu, S. K. Makineni, P. Kontis, G. Dehm, D. Raabe,
B. Gault, G. Eggeler, On the segregation of Re at dislo-
cations in theγ′ phase of Ni-based single crystal superal-
loys, Materialia 4 (2018) 109–114.1095
16

## Page 18

1. The first review on atomistic simulation studies of Ni-based superalloys. 
2. Covering studies on micro-defects and mechanical pr operties by three atomistic simulation 
methods. 
3. The current results are critically discussed and outlooks are proposed. 
Journal Pre-proof
