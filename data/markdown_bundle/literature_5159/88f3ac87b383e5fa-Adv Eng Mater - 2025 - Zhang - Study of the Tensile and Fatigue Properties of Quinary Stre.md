# Adv Eng Mater - 2025 - Zhang - Study of the Tensile and Fatigue Properties of Quinary Strengthening Phase in Ni‐Based

<!-- source: D:\总文献\Adv Eng Mater - 2025 - Zhang - Study of the Tensile and Fatigue Properties of Quinary Strengthening Phase in Ni‐Based.pdf -->
<!-- file_sha256: af882f60711711a0ca00bd150e280b04743d2c145028120691f12109acd9ec8d -->

## Page 1

Study of the Tensile and Fatigue Properties of Quinary
Strengthening Phase in Ni-Based Superalloys
Chuan-Hui Zhang,* Ni Lu, Liwu Jiang,* and Jin Wang
1. Introduction
Ni-based superalloys are extensively utilized as the primary mate-
rial for turbine blades in aircraft and power generation turbines,
due to their exceptional high-temperature creep resistance, fatigue
strength, and corrosion resistance.[1–3] Research has demonstrated
that Ni-based superalloys enhance their strength by embedding
ﬁne and ordered γ 0 precipitates within theγ matrix. This structure
effectively impedes the movement of dislocations at high temper-
atures. Over time, a dislocation network forms at the γ/γ 0 inter-
faces, mitigating the stress changes caused by lattice
mismatches, thereby enhancing the mechanical properties of
the superalloys.[4]
With advancements in aircraft engine
performance, such as increased power
and thermal ef ﬁciency, turbine blades Ni-
based superalloys face more challenging
conditions within combustors. The high
temperatures and stresses exerted on tur-
bine blades can cause the superalloy to
experience creep deformation, reducing
its service life. [5] Consequently, creep resis-
tance is an important mechanical property
of Ni-based superalloys. Over the past few
decades, the high-temperature creep per-
formance of Ni-based superalloys has been
extensively studied. For instance, Raffaitin
investigated the creep behavior of Ni-based
superalloys under nonisothermal condi-
tions and found signi ﬁcant differences
compared to isothermal load conditions.
Under nonisothermal conditions, the creep
lifespan of the superalloys was reduced to
1/3 to 1/4 of its original duration, and
the secondary creep rate increased ten-
fold.[6] Additionally, thermomechanical
fatigue behavior is a principal load type
for Ni-based superalloys, with engine com-
ponents, such as turbine blades experienc-
ing low-cycle mechanical fatigue loads at high temperatures
around 950 °C.[7] Studies indicate that the evolution of the micro-
structure at the interfaces of Ni-based superalloys signi ﬁcantly
affects their fatigue performance. Research by Lin showed that
the dislocation networks at the γ/γ 0 interfaces play a crucial role
in strain hardening during the low-cycle fatigue behavior of high-
temperature alloys, while the shearing of γ 0 precipitates by super-
dislocations plays a signi ﬁcant role in the strain softening of
these alloys.[8] In recent years, both experimental and simulation
studies have focused intensively on the high-temperature fatigue
behavior of nickel-based superalloys. [9] Fatigue research on the
DZ411 alloy has also seen some progress. Theoretically, Wang
et al. developed a multiaxial fatigue model for predicting the life-
span of DZ411, signi ﬁcantly simplifying the fatigue life predic-
tion process. [10] Experimentally, Sun et al. found that
rejuvenation heat treatment can effectively restore low-cycle
fatigue performance. [11] However, there are few reports on
atomic-scale studies in this area. In summary, resistance to
high-temperature creep and fatigue performance are critical met-
rics for evaluating Ni-based superalloys. Although numerous
studies on creep and low-cycle fatigue exist, most experimental
research has focused on observing the similarities and differen-
ces in the microstructures of superalloys before and after load-
ing, and detailed information about the formation and evolution
C.-H. Zhang, N. Lu, L. Jiang, J. Wang
National Center for Materials Service Safety
University of Science and Technology Beijing
Beijing 102206, China
E-mail: zhangch@ustb.edu.cn; lwjiang@ustb.edu.cn
The ORCID identi ﬁcation number(s) for the author(s) of this article
can be found under https://doi.org/10.1002/adem.202402338.
DOI: 10.1002/adem.202402338
The embedded atom method potential for the Ni –Al–Co–Ti–Cr quinary alloy is
established using the lattice inversion method, con ﬁrming that this potential
accurately captures the sta tic physical properties of t he multielement alloy. The
mechanical behavior of the DZ411 allo y at high temperatures is simulated
through molecular dynami cs, focusing on its tensile strength and fatigue
properties. The high-temperature tensile simulations show that as temperature
increases, the interatom ic forces weaken and the dislocation density signi ﬁ-
cantly decreases, leading to a notable dro p of ultimate tensile strength. Fatigue
tests conducted at various temperatures for 15 cycles reveal that at room
temperature, the internal structure gradually deteriorates under repeated
loading, reducing its tensile strength . At high temperatures, due to the pre-
dominance of elastic deformation, the mechanical properties exhibit minimal
variance before and after loading. Duri ng the compression process, the alloy
exhibits characteristics of the face-cubic-centered structure and formed hex-
agonal-close-packed structure on the (111) crystal plane, which ensures that the
stress–strain curve maintains a consisten t shape throughout the compression
process. This work deepens the understa nding of the mechanical performance
changes of the DZ411 alloy under extrem e conditions, providing theoretical
guidance for the performance optimiz ation of high-temperature alloys.
RESEARCH ARTICLE
www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (1 of 10) © 2025 Wiley-VCH GmbH

## Page 2

of microstructures during creep and fatigue processes remains
very limited.[12] Therefore, a deeper exploration of the microme-
chanisms of interaction between microstructures within the
superalloys not only aids in enhancing material performance
but also provides a scienti ﬁc foundation for the development
of new superalloy materials to meet more stringent engineering
requirements.
In the study of the microstructural properties of high-
temperature alloys, the molecular dynamics (MD) method offers
unique advantages. MD can rapidly process large-scale atomic
systems and accurately re ﬂect their micromechanisms, while
also considering various complex environmental conditions such
as temperature and pressure in simulation calculations.
Numerous studies have successfully utilized MD to investigate
Ni-based superalloys. For instance, Mianroodi discovered
through simulations that Co segregates at Ni lattice positions
in Ni-based superalloys, with increasing Co content leading to
greater lattice distortions in the γ phase and a reduction in elastic
constants.[13] Research by Liu demonstrated that adding Re to
Ni/Ni3Al alloys signi ﬁcantly improves crack propagation, enhan-
ces the Re─Ni bond strength, and reduces atomic bond breakage
at the crack sites, thereby decreasing the brittleness of the super-
alloy and enhancing its ductility. [14]
DZ411 alloy is a directionally solidi ﬁed Ni-based superalloy
speciﬁcally designed for turbine blades, with γ 0 phase as its pri-
mary strengthening phase and key strengthening elements
including Co, Cr, Ti. [15] Despite its excellent performance in
applications, the microbehavior and failure mechanisms of
DZ411 alloy at high temperatures remain unclear, limiting fur-
ther development of its application potential. The mechanical
properties of DZ411 alloy are typically in ﬂuenced by a combina-
tion of various strengthening elements, but most of the potential
functions developed for Ni-based superalloys are ternary force
ﬁelds, and their construction largely relies on empirical param-
eters, which signi ﬁcantly restrict their practical application. [16,17]
In this work, a Ni– Al– Co– Cr– Ti quinary embedded atom method
(EAM) potential was developed speciﬁcally for the DZ411 alloy. It
aims to investigate the intrinsic microscopic mechanisms that
affect the tensile properties and metal fatigue characteristics
of the superalloy at high temperatures, thereby providing theo-
retical assistance for designing the next generation of alloys.
2. Experimental Section
2.1. Quinary Ni –Al–Co–Cr–Ti Potential
Lattice inversion method allows for precise derivation of inter-
atomic potential expressions from the binding energies of crys-
tals. This method was applied in an attempt to construct EAM
potential for Ni– Al– Co– Cr– Ti quinary conﬁguration. In previous
work, binary potential models were successfully developed and
applied for face-centered-cubic (FCC) and hexagonal-close-
packed (HCP) structures. [18] However, element Cr is a body-
centered-cubic (BCC) structure, the development of a new
potential model to accommodate BCC structure is necessary.
Due to the lower atomic packing factor of the BCC structure com-
pared to FCC and HCP structures, the pair potential in this struc-
ture does not exhibit the “softer” characteristics seen in the
Morse potential [19] that previously work used. Instead of energy
changing slowly with increasing distance, it quickly approaches
zero as distance increases. Therefore, the pair potential function
proposed by Zhou [20] was adopted. Although this model involves
numerous parameters, its function shape is quite ﬂexible, mak-
ing it highly suitable for constructing lattice inversion potentials
for BCC structures. The speci ﬁc form is as follows.
ϕðrÞ¼ Aexp½/C0 αðr=re /C0 1Þ/C138
1 þð r=re /C0 kÞ20 /C0 Bexp½/C0 βðr=re /C0 1Þ/C138
1 þð r=re /C0 λÞ20 (1)
where re is the equilibrium spacing between nearest neighbors,
A, B, α, and β are four adjustable parameters, and k and λ are two
additional parameters for the cutoff. The electron density func-
tion is taken in the same form as the attractive term in the pair
potential with the same values of k and λ.
Above pair potential function and Rose potential were applied
to describe the total energy of BCC structure. Then, the results in
Equation (2) were substituted to obtain the potential parameter of
Cr which can be used for calculation of physical properties.
Figure 1 displays the lattice inversion data and ﬁtting results
for Cr element using this pair potential. The red curve of the pair
potential aligns closely with the black lattice inversion data, dem-
onstrating the effectiveness of the BCC pair potential form used.
When constructing interaction potentials between different
types of atoms in an alloy, it is necessary to consider and elimi-
nate the interactions between identical atoms in the lattice. This
ensures that the pair potential derived from lattice inversion is
calculated solely from the interactions between different atoms.
The speci ﬁc calculation formula is as follows.
ϕpqðrÞ¼ 2
X
n¼1
IpqðnÞ
/C20
EtðbpqðnÞrÞ
/C0
X
x¼p;q
Fx ðρx Þ/C0
X
x¼p;q
ϕxx ðbxx ðnÞrÞ
/C21 (2)
where Et represents the total energy of the binary alloy, p and q
denote two different types of atoms. Ipq(n) is the inversion coef-
ﬁcient for the corresponding hypothetical lattice structure, and
the acquisition of bxx(n) depends on the structural relationships
of the same element x (x = p, q) within the alloy.
Figure 1. Cr inversion results and ﬁtting curve, the red curve represents
Morse potential ﬁtting.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (2 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

Based on this potential function model and our previous
research, a lattice inversion EAM potential (LI-EAM) was devel-
oped for the Ni – Al– Co– Cr– Ti quinary alloy. The complete
parameters for the metals Ni, Co, and Ti, as well as the embed-
ding energy and electron density parameters for Cr are listed in
Table 1 . Metal Cr has numerous parameters related to its pair
potential, which are additionally provided in Table 2 .
2.2. Simulation Model and Software
According to the γ/γ 0 phase structures observed in the experi-
ments,[11] the atomic model shown in Figure 2a was constructed.
The γ phase is primarily composed of pure Ni, with a lattice con-
stant of 3.52 Å and FCC crystal structure in this model. It serves
as a matrix containing other precipitated phases and forms a
solid solution with other phases. The γ 0 phase serves as the main
precipitated phase in Ni-based single-crystal alloys and occupies a
signiﬁcant proportion. Its main component is Ni 3Al with a lattice
constant of 3.62 Å, presenting an L12 crystal structure in the form
of a precipitate phase. The lattice mismatch at the interface is
2.8%, so the interface formed by 35 γ 0 lattices and 36 γ lattices
minimizes the stress differences caused by the disparity in lattice
parameters. Figure 2b shows the dislocation network formed at
the phase interface to reduce the system ’s strain energy. This
structure system is consistent with observations made in
experiments.[21,22]
Based on the alloy composition ratios, the elements Co, Cr,
and Ti are identi ﬁed as main strengthening components in
the DZ411 alloy. [15] The composition of DZ411 superalloy is
13.5– 14.3Cr, 9.0 – 10.0Co, 1.3 – 1.7Mo, 3.5 – 4.1W, 4.6 – 5.2Ti,
2.8– 3.4Al, 0.07 – 0.12C, 2.5 – 3.1Ta, and the rest is Ni (wt%). [15]
Obviously, the atomic masses of Ta and W are 3 – 4 times that
of Ti and 6 – 7 times that of Al, so the atomic counts of Ta
and W are relatively low compared to Ti and Al. This means
Ni, Al, Co, Ti, and Cr are the main elements with a high atomic
ratio in the DZ411 alloy. Selecting these primary elements to con-
struct a potential function would facilitate simulation studies. An
attempt was made to incorporate the three strengthening ele-
ments Co, Cr and Ti into the γ/γ 0 model. Co and Cr were ran-
domly assigned to occupy the Ni site, with atomic proportions of
≈10% and 16%, respectively. Ti randomly occupies the Al site,
and the atomic proportion is about 6%. At the same time, Co and
Cr do not occupy the same speci ﬁc Ni sites, so that the true con-
tent of strengthening elements will not be affected. In order to
make the model and the results more universal, ﬁve models of
the same proportion but different random occupancy were
designed for each strengthening element, and a total of 15 ran-
dom ternary alloy models were designed for the three strength-
ening elements. Then, the ultimate tensile strength (UTS) of 15
models was calculated at three typical temperatures of 300, 600,
and 900 K. The results for ﬁve random occupancy models of each
strengthening element at each temperature were statistically
averaged and are presented in Figure 3 . The evaluation of
mechanical properties is based on UTS, which re ﬂects the mate-
rial’s performance at maximum stress. It also indirectly indicates
the material’s ductility and toughness, serving as a representative
criterion in the evaluation of mechanical properties. In Figure 3a,
the UTS of model 1 is the highest among the ﬁve groups of ran-
dom models, which approaches 9.3 GPa. Therefore, it was con-
sidered to be the Ni – Al– Co model with the best mechanical
properties. In constructing the Ni – Al– Cr random alloy model,
it is crucial to note that the strengthening elements Co and
Table 1. LI-EAM parameters in elemental Ni, Co, Ti, and Cr.
ϕ(r) F(ρ) f(r)
D0 a0 r0 λ F0 ρ0 μ fe β
Al[15] 0.093 1.942 2.950 0.790 2.708 0.900 0.100 0.062 3.689
Ni 0.207 2.531 2.500 0.580 3.082 0.427 0.010 0.031 3.251
Co 0.210 2.271 2.520 0.655 2.940 0.625 0.010 0.033 2.773
Ti 0.231 1.876 3.000 0.490 3.221 1.902 0.010 0.137 3.253
Cr –– – 0.314 1.582 0.336 0.010 0.037 7.370
Table 2. The pair potential parameters in the LI-EAM of elemental Cr.
AB αβ k λ
1.806 2.147 8.766 7.372 0.008 0.322
Figure 2. The initial model of the γ/γ’ phase of DZ411 alloy and the opti-
mized dislocation network. a) crystal structure of the interface and
b) dislocation of the interface structure.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (3 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

Cr both occupy Ni atomic sites in the alloy. To prevent conﬂicts in
lattice positions of the strengthening elements during model
construction, the sites occupied by Co were ﬁrst identi ﬁed.
These sites were then excluded when selecting random sites
for Cr. Figure 3b shows the UTS of ﬁve Ni– Al– Cr random alloy
models, and model 1 also displays a tensile strength close to
11.2 GPa, signi ﬁcantly higher than the other four models.
Therefore, it was considered the best mechanical performance
Ni– Al– Cr model. The strengthening element Ti is determined
to occupy 40% in the DZ411 alloy. Using the same construction
method as before, the tensile strength of Ni – Al– Ti was calcu-
lated. As shown in Figure 3c, the UTS of model 1 exceeds
9.2 GPa, making it the best among the ﬁve random models.
In summary, the random models with the best mechanical prop-
erties from the ternary alloys were selected and combined to
construct the ﬁnal Ni – Al– Co– Cr– Ti quinary alloy model, which
is presented in Figure 4 .
The large-scale atom/molecule massively parallel simulator [23]
was used to simulate the basic physical properties and dynamic
processes of DZ411 alloy, and OVITO [24] was employed for
model construction and visualization analysis. Data processing
and potential functions were implemented using C language
programs.
3. Results and Discussion
3.1. Basic Properties
For the basic properties of the system, the experimental or ﬁrst-
principles data were tested to validate the reliability of the poten-
tial. All simulations are conducted at 0 K, with a potential cutoff
distance set at 6.875 Å. The basic properties of elemental Al can
be referenced from our previous work, [18] and the properties of
the metals Ni, Co, Ti, and Cr are displayed in Table 3 . As the
lattice inversion process takes into account the actual structure
and energy of the crystals, the calculated lattice constants and
energies are consistent with experimental data, with all errors
Figure 3. Random model UTS of each strengthening element. a) Co, b) Cr,
c) Ti. The x-axis represents randomly occupied models with different
atomic distributions.
Figure 4. The ﬁnal model of the γ/γ’ phase of DZ411 alloy and the opti-
mized dislocation network. a) crystal structure of the interface and
b) dislocation of the interface structure.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (4 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

not exceeding 1%. The formation energy of vacancies is usually
represented by the difference in average atomic energy between
perfect crystals. From the table, it can be seen that the LI-EAM
calculated results match well with experimental results. The bulk
modulus BV is calculated using the Voigt approximation
method,[25] which derives the bulk and shear moduli by solving
relationships between elastic constants in the crystal. Calculations
are within 4% error of experimental data.
Table 4 lists the elastic constants for each metal. Cubic crystal
systems for Ni and Cr are FCC and BCC, featuring three inde-
pendent matrix elements: C11, C12, and C44. Elements Co and Ti
belong to the hexagonal crystal system, which has ﬁve indepen-
dent matrix elements: C11, C12, C13, C33, and C44. Additionally, in
the hexagonal system, the elastic constant C66 can be derived
from independent matrix elements. The table shows that all cal-
culated elastic constants meet the stability requirements of the
crystals and are generally consistent with experimental data. [26]
The results from Table 3 and 4 demonstrate that the
Ni– Al– Co– Cr– Ti LI-EAM potentials for these ﬁve metals accu-
rately describe their fundamental physical properties.
3.2. High-Temperature Tensile Properties
The γ and γ 0 phases in the DZ411 alloy are subjected to stress
due to lattice mismatch, leading to the formation of a dislocation
network at the interfaces. Experimental studies shows that the
dislocation network and the microstructure of interfaces directly
impact the alloy ’s resistance to crack propagation, tensile
strength, and fatigue performance. [27,28] The evolution of dislo-
cations under high-temperature conditions was simulated using
the developed Ni – Al– Co– Cr– Ti quinary LI-EAM potential. The
microscopic mechanism by which the internal structure affects
the alloy properties was then analyzed. The simulation setup
includes three operational temperatures for the alloy (1100,
1200, and 1300 K), with an additional set at room temperature
for comparison. The velocities of the atoms within the alloy fol-
low a Gaussian distribution. All simulations are conducted with a
time step of 0.001 ps. After a relaxation period of 20 ps under an
number of molar molecules, the pressure and temperature
(NPT) ensemble, the alloy is subjected to uniaxial tension along
the z-axis with a strain rate of 0.0025 ps /C0 1.
Figure 5 a displays the tensile curves at various temperatures
for the DZ411 alloy. At room temperature, the alloy exhibits
exceptional tensile performance with an UTS of 12.8 GPa. As
the temperature increases, the weakening of interatomic forces
makes atoms more prone to relative displacement, altering the
microstructure of the system. Consequently, the UTS of the alloy
gradually decreases, and the elongation rate improves compared
to room temperature. Experimental comparisons of DZ411 indi-
cated that its tensile curve reaches UTS at ≈0.1% strain. [29]
Additionally, the UTS decreases rapidly with increasing temper-
ature, which aligns with the conclusions shown in Figure 5a.
Further observation found that the alloy displays an initial phase
of elastic deformation at 300 K, which then gradually shifts to
plastic deformation. The maximum tensile strength is observed
when the strain rate reaches 10%. This indicates that the alloy
Table 3. Lattice inversion EAM-calculated physical properties of metal
elements compared with experiments and density functional theory
(DFT) calculations.
LI-EAM Experiment or DFT
a [Å] Ec [eV] BV Ef [eV] a [Å] Ec [eV] BV Ef [eV]
Al 4.06 [18] 3.36[18] 78.93[18] 0.73[18] 4.05[40] 3.42[41] 80.78[42] 0.66[43]
Ni 3.52 4.45 187.59 1.43 3.52 [44] 4.44[44] 180.33[45] 1.40[46]
Co 2.49 4.42 182.18 1.42 2.51 [44] 4.39[44] 187.44[47] 1.35[48]
Ti 2.94 4.86 106.38 1.52 2.94 [44] 4.85[44] 109.7[45] 1.55[48]
Cr 2.88 4.11 208.92 2.54 2.88 [44] 4.10[44] 201[49] 2.27[50]
Table 4. Comparison of elastic constants calculated by LI-EAM with
experimental or DFT calculations.
C11 C12 C13 C33 C44 C66
Al 96.10[18]
101.5[42]
70.34[18]
70.4[42]
–– 38.46[18]
31.7[42]
–
Ni 251.49
247[45]
155.64
147[45]
–– 128.23
125[45]
–
Co 300.35
295[47]
147.69
159[47]
98.38
111[47]
349.98
335[47]
70.88
71[47]
76.33
68[47]
Ti 178.80
176.1[45]
85.49
86.9[45]
54.80
68.3[45]
209.61
190.5[45]
43.54
50.8[45]
46.66
44.6[45]
Cr 399.92
391.0[45]
113.42
89.6[45]
–– 100.16
103.2[45]
–
 Figure 5. Tensile curve and UTS of DZ411 alloy at different temperatures.
a) stress-strain curve of the model and b) Ultimate tensile strength of the
model.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (5 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

exhibits good plasticity at room temperature. Under high-
temperature conditions, the alloy does not exhibit a distinct elastic
stage, and the initial strength during stretching changes slowly.
Plastic deformation occurs when the strain rate reaches 4%, with
stress values gradually increasing. Subsequently, a wider plastic
deformation region is demonstrated. Under the driving of tensile
stress, the strain rate exceeds 11% before reaching its maximum
tensile strength value. Figure 5b shows the relationship between
the maximum tensile strength of the DZ411 alloy and tempera-
ture. The result reveals that the UTS gradually decreases with ris-
ing temperature, showing a trend of slow decline followed by a
rapid drop. Results are consistent with trends observed experi-
mentally in data from other Ni-based superalloys. [2,3] This means
that under the inﬂuence of high temperature, DZ411 alloy under-
goes irreversible structural changes at an early stage.
To further investigate the micromechanical mechanisms
behind the effect of temperature on the tensile properties of
the DZ411 alloy, the evolution of the structure during the tensile
process was visualized. Figure 6 presents snapshots of the atomic
structure of the alloy at various stages of deformation. At room
temperature, the alloy exhibits a relatively FCC structure without
strain. When the strain rate is within 4%, the system remains in
the elastic deformation stage. To more clearly demonstrate the
internal structural changes, the FCC structure is hidden and then
only the disordered structures are visible in the snapshots at 4%
and 10% strain rates. The result shows that the alloy model can
retain its initial structural characteristics below 4% strain rate.
When the strain rate exceeds 4%, the atomic structure at the
phase boundary becomes more susceptible to deformation under
continuous external stress. The γ phase gradually loses its FCC
characteristic and displays HCP feature on the (111) plane.
Although the HCP microstructure that emerges does not meet
the perfect axial ratio of 1.633 (OVITO recognition range is
≈1.5– 1.9), an axial ratio within this range is identi ﬁed as HCP
structure. As the internal stress increases, HCP in the γ matrix
causes the alloy to transition from elastic deformation to plastic
deformation at the phase boundary. As the strain further
increases, HCP also begins to form within the γ 0 phase.
Eventually, when the alloy reaches its UTS, the initial fracture
occurs at the phase boundary.
Figure 6b – d displays the internal structural changes of the
DZ411 alloy under high-temperature tensile conditions. Due
to a signiﬁcant proportion of disordered atomic structures during
high-temperature deformation, the impact of these disordered
atoms on the alloy ’s tensile performance cannot be overlooked,
so the snapshots show the complete alloy structure. Figure 6 indi-
cates that after high-temperature relaxation, the initial structure
of the alloy remains FCC structure. However, due to the high-
temperature environment, the average kinetic energy of the
internal atoms increases, weakening the interatomic forces. It
leads to the transformation from FCC to HCP becoming increas-
ingly dif ﬁcult as the strain increases. Consequently, internal
atoms are more likely to deviate from their equilibrium positions
and then become disordered atoms. When the strain rate reaches
10%, the proportion of disordered structures inside the alloy is as
high as 60%. Unlike at room temperature where disordered
structures are mostly distributed in the γ matrix, disordered
atoms are almost uniformly distributed throughout the alloy
at high temperatures. This is the microscopic mechanism behind
the absence of elastic deformation and the occurrence of yield
Figure 6. Changes in the internal structure of DZ411 alloy at various temperatures and strain stages. a) 300 K, b) 1100 K, c) 1200 K, d) 1300 K.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (6 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

changes in the high-temperature curves shown in Figure 5a. The
high density of disordered structures makes it dif ﬁcult to main-
tain higher strength, which also corroborates experimental ﬁnd-
ings that the γ 0 phase is a major source of strength in Ni-based
superalloys.[30] When the γ 0 phase within the alloy can no longer
maintain its structural characteristics, a signi ﬁcant reduction in
tensile strength occurs.
Figure 7 illustrates the evolution of dislocation structures
inside the DZ411 alloy during the tensile process. Given that
the dislocation evolution processes are similar under the three
high-temperature conditions, the dislocation structure evolution
at 1200 K was selected to analysis. At room temperature and with-
out stress, perfect dislocations with <110> orientation naturally
form at the two-phase interfaces within the alloy. As the applied
stress gradually increases (strain rate of 4%), the dislocation
loops within the alloy begin to break down, and an increasing
number of green Shockley dislocations appear. When the alloy
reaches its UTS (strain rate of 10%), the dislocation density
within the alloy peaks. A large variety of dislocations concentrate
at the phase interfaces, and some also appear within the bulk of
the alloy. The alloy fractures once the strain rate exceeds 10%,
and a large number of disordered structures are produced inter-
nally, making it dif ﬁcult for dislocations to continue increasing
and leading to short and discontinuous characteristics. Under
high-temperature conditions, the dislocation density remains
low throughout the deformation process of the alloy. This indi-
cates that the coupling of strain and high temperature disrupts
the internal dislocation network. Once the system reaches its
temperature or stretch limit, the alloy maintains a lower disloca-
tion density until it fractures. Therefore, the dislocation line den-
sity inside the alloy has a direct impact on its tensile strength,
which can be described by the Taylor relationship. [31]
σ ¼ αGb ﬃﬃ ﬃρp (3)
In this relationship, α depends on the material’s intrinsic prop-
erties, the parameter σ, G, b, and ρ represent the material ’s ﬂow
stress, shear modulus, magnitude of the Burgers vector, and dis-
location density, respectively. The ﬂow stress described in this
relationship is positively correlated with the square root of the
dislocation density. At 300 K, dislocations are uniformly distrib-
uted along the primary slip systems in the material. At elevated
temperatures above 1100 K, the dislocation density decreases, pri-
marily due to dislocation climb, leading to a gradual transforma-
tion of the crystal structure from FCC to HCP. Moreover, under
high-temperature and high-strain conditions, dislocation slip and
climb accelerate, resulting in the formation of numerous disor-
dered atomic structures. At room temperature, the internal dis-
location line density of the DZ411 alloy gradually increases as the
strain goes up, and the tensile strength also increases. However,
the internal dislocation density of the alloy remains at a lower
level at high temperatures, resulting in signi ﬁcantly lower tensile
strength compared to room-temperature conditions.
3.3. High-Temperature Fatigue Properties
Metal fatigue affects Ni-based high-temperature alloys through
changes in microstructural features, such as the precipitation
and morphological changes of the γ 0 phase.[32,33] Additionally,
the formation and propagation of fatigue-induced cracks directly
impact the mechanical properties of the alloy. Especially in high-
temperature environments, the in ﬂuence of temperature accel-
erates microstructural evolution, thereby signiﬁcantly shortening
the service life of the alloy. [34] Therefore, the fatigue mechanical
properties of the γ/γ 0 phase under high-temperature cyclic load-
ing were calculated. The simulation process involves setting
three groups of service temperatures for the alloy (1100, 1200,
and 1300 K), with an additional group set at room temperature
as a control. The internal atomic velocities of the alloy follow a
Gaussian distribution, and the time step for all simulation pro-
cesses is set to 0.001 ps. Initially, after relaxing the system for
20 ps under the NPT ensemble, the alloy undergoes 15 cycles
of tension– compression simulation along the z-axis with a strain
amplitude of 8% and a strain rate of 0.0025 ps /C0 1.
Figure 8 illustrates the cyclic stress– strain curves of the DZ411
alloy under room temperature and high-temperature conditions.
The results indicate a gradual decrease in tensile strength after
repeated loading, but with signi ﬁcant differences in the charac-
teristics of the curves between room temperature and high tem-
perature. Based on the results of the previous uniaxial tensile
simulations, the orderly structure begins to change after repeated
application of stress at room temperature, leading to a weakening
of its resistance to deformation, while the plastic deformation
Figure 7. Changes in dislocations of DZ411 alloy at various temperatures and strain stages. a) 300 K, b) 1200 K.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (7 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

gradually becomes the primary mode of deformation for the
alloy. According to Figure 8a, after the ﬁfth tensile loading, there
is a distinct drop in the stress – strain curve when the strain rate
exceeds 6%, which indicates that slight fracture may occur within
the alloy. Consequently, when the alloy is further compressed,
the stress – strain curve exhibits unstable oscillations. And
throughout all subsequent cyclic processes, the curve also shows
similar variations. This indicates that irreversible structural dam-
age occurs within the alloy after repeated tension – compression
loading at room temperature, leading to a signi ﬁcant decline in
mechanical performance.
Under high-temperature conditions of 1100– 1200 K, the inter-
atomic interactions are weak and the strength is ≈7.5 GPa at a
strain rate of 8%, signi ﬁcantly lower than the strength at room
temperature (12 GPa). However, the stress – strain curves still
exhibit a high degree of overlap even after multiple loading
cycles. This indicates that the plastic strain energy at room tem-
perature is higher than that at high temperatures. Therefore, the
strength only experiences a slight decrease after repeated load-
ing. Despite a decrease in strength of ≈5 GPa after more than
5 cycles at 1300 K, the monotonicity of the curve remains rela-
tively stable, demonstrating that the primary mode of deforma-
tion is elastic under high-temperature conditions. [35,36] At high
temperatures, the ﬁrst 1 – 2 cycles exhibit hysteresis loops that
enclose an almost negligible area. Under strain-controlled fatigue
loading, the variation in peak stress re ﬂects the fatigue mechani-
cal characteristics of metallic materials. [37] Both the tensile and
compressive peak stresses remain constant throughout the entire
cycle, indicating that DZ411 undergoes an elastic stage during
the cyclic loading without exhibiting localized plasticity. [38]
After ﬁve cycles, cyclic hysteresis appears. The area enclosed
by the hysteresis loop represents the work done by plastic
strain.[39] A larger hysteresis loop area indicates increased plastic
deformation in DZ411. This suggests that after cycle 5, both at
room temperature and high temperature, elastic strain
decreases, as one can expect a corresponding increase in plastic
strain for a consistent total strain. [11] At temperatures of 1200 K
and below, DZ411 shows a trend toward cyclic saturation. At
1300 K, after 15 cycles, cyclic hardening is observed, but the
degree of hardening is not severe, and the change in plastic work
remains minimal. Consequently, the DZ411 alloy exhibits higher
resistance to fatigue damage in high-temperature environments.
This aligns with the conclusions drawn by Sun et al. from their
creep testing on DZ411.[11] The isothermal cyclic hysteresis loops
at midlife showed that the reduction in elastic strain for DZ411
specimens thermally exposed at 1000 °C is less pronounced than
for specimens tested at 900 °C. The low-cycle-fatigue fracture
cycles under thermal exposure at different temperatures were
1554 /C6 29 cycles at 850 °C, 1090 /C6 219 cycles at 900 °C, and
1293 /C6 28 cycles at 1000 °C. These ﬁndings align with the con-
clusion that DZ411 exhibits greater resistance to fatigue damage
under high-temperature conditions.
In order to more intuitively analyze the effect of fatigue cyclic
loading on the microstructure evolution, the internal structural
changes of the alloy are presented during the ﬁrst and ﬁfteenth
cycles of loading. Given the similarity in structural evolution pro-
cesses under the three high-temperature conditions, typical
structures under the 1200 K condition were selected for analysis
and discussion. Figure 9a1 depicts the internal atomic structure
at room temperature when reaching maximum strain for the ﬁrst
time, and the FCC and disordered structures in the ﬁrst extreme
tensile and compressive states were hidden. The stretching
Figure 8. Cyclic stress – strain curves of DZ411 alloy at different temperatures. a) 300 K, b) 1100 K, c) 1200 K, d) 1300 K.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (8 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

results are similar to Figure 5, the alloy forms HCP structures
along the (111) plane in the γ matrix, while there is no signi ﬁcant
structural change in the γ 0 phase. This indicates that at a strain
rate of 8%, the γ 0 phase primarily undergoes elastic deformation,
whereas plastic deformation occurs in the γ phase. Figure 9a3
presents the internal atomic structure when reaching maximum
strain for the ﬁfteenth time, the result shows a more chaotic dis-
tribution of HCP structures within the alloy. These structures are
no longer predominantly oriented along speci ﬁc (111) planes,
and the alloy undergoes partial fracture at the phase interface,
accompanied by the emergence of a signi ﬁcant number of dis-
ordered structures. So, the mechanism of decreased mechanical
performance is shown in Figure 8a. Figure 9b1 illustrates the
internal atomic structure at 1200 K when reaching maximum
strain for the ﬁrst time. HCP structures are evenly distributed
within the γ matrix, and the strengthening element Ti promotes
the formation of BCC structures in the γ 0 phase, which is used to
ensure the stability of the alloy at high temperatures. [11]
Consequently, there are no signi ﬁcant differences in the internal
structure after multiple cycles of loading, although the tensile
strength of the alloy is slightly reduced, and the elastic deforma-
tion is still maintained. Figure 9a2,a4 as well as 9b2,b4 depict the
internal atomic structure after the ﬁrst and ﬁfteenth compres-
sions at two temperature conditions. Observation reveals that
atoms are conﬁned to a small space during compression, signi ﬁ-
cantly reducing the possibility of relative displacement away from
equilibrium positions. As a result, the alloy reverts to exhibit FCC
structure characteristics. Lattice contraction leads to the forma-
tion of HCP structures along the (111) planes, and the structural
changes during all compression processes follow the same pat-
tern. Therefore, the mechanical performance remains relatively
stable during the compression processes in Figure 8.
4. Conclusion
For simulating the mechanical properties of the DZ411 superal-
loy at high temperature, the Ni – Al– Co– Ti– Cr quinary LI-EAM
potential is developed. The physical properties of elements are
in good agreement with experimental data, indicating that
LI-EAM can accurately compute the static properties of metals.
Then, Co, Ti, and Cr are selected as three main strengthening
elements in the DZ411 alloy for constructing multidisordered
alloy models. At last, MD simulations of tensile properties
and fatigue damage behavior at high temperatures are
performed.
The results show that the alloy forms HCP structures in the γ
matrix during room-temperature tensile process. With the
increase of strain, the γ 0 phase also gradually undergoes the same
transformation, ultimately leading to fracture at the phase inter-
face. At high temperatures, the weakening of interatomic forces
caused atoms to gradually deviate from equilibrium positions. As
the strain increases, it leads to a transition to a disordered atomic
structure, the tensile strength of the alloy signi ﬁcantly decreases.
Dislocation density is also a factor affecting the tensile strength
of alloys. During the stretching at room temperature, the alloy
generates a large number of dislocations, which enhances its ten-
sile strength. At high temperatures, the fewer dislocations in the
alloy are insuf ﬁcient to support higher tensile strength. The
results of cyclic fatigue loading simulations show that the inter-
nal structure is damaged under multiple cycles of loading at
room temperature, leading to a decrease in tensile strength.
Under high-temperature fatigue loading, the primary deforma-
tion mode of the alloy is elastic deformation, and the differences
in mechanical properties after multiple cycles of loading are
small. The alloy exhibits the same trend during all compression
processes. Lattice contraction con ﬁnes the atoms to a small
space, and the alloy forms HCP structure on the (111) plane.
It is the microscopic mechanism that maintains the consistent
shape of the compression curves in the cyclic stress – strain
diagram.
Acknowledgements
This work was supported by National Science and Technology Major
Project of China (no. J2019-VI-0004-0117) and Science Center for Gas
Turbine Project (grant no. P2022-B-IV-009-002).
Figure 9. Changes in the internal structure of DZ411 alloy under different cyclic loading stages. a) 300 K and b) 1200 K.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (9 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

Conﬂict of Interest
The authors declare no con ﬂict of interest.
Author Contributions
Chuan-Hui Zhang : conceptualization (equal); formal analysis (equal);
funding acquisition (lead); investigation (lead); methodology (lead); proj-
ect administration (lead); supervision (lead); validation (lead); writing —
original draft (supporting); writing —review & editing (lead). Ni Lu : data
curation (supporting); formal analysis (equal); investigation (equal); meth-
odology (supporting); software (equal); visualization (equal); writing —
review & editing (equal). Liwu Jiang : funding acquisition (supporting);
writing—review & editing (supporting). Jin Wang: data curation (lead); for-
mal analysis (lead); investigation (equal); methodology (equal); software
(lead); visualization (lead); writing —original draft (lead).
Data Availability Statement
The data that support the ﬁndings of this study are available from the
corresponding author upon reasonable request.
Keywords
embedded atomic methods, fatigues, high-temperature performances,
Ni-based superalloys, stress – strains
Received: October 6, 2024
Revised: November 18, 2024
Published online: January 30, 2025
[1] X. Xiong, D. Quan, P. Dai, Z. Wang, Q. Zhang, Z. Yue, Mater. Sci.
Eng., A 2015, 636, 608.
[2] P. S. M. Jena, S. K. Pradhan, S. Tripathy, B. Mahato, C. Fernando,
N. Paulose, J. K. Sahu, Mater. Sci. Eng., A 2021, 807, 140855.
[3] F. F. Han, B. M. Zhou, H. F. Huang, B. Leng, Y. L. Lu, J. S. Dong,
Z. J. Li, X. T. Zhou, Mater. Chem. Phys. 2016, 182, 22.
[4] W.-P. Wu, Y.-F. Guo, Y.-S. Wang, R. Mueller, D. Gross, Philos. Mag.
2011, 91, 357.
[5] J. Yu, X. Sun, T. Jin, N. Zhao, H. Guan, Z. Hu, Mater. Sci. Eng., A 2010,
527, 2379.
[6] A. Raffaitin, D. Monceau, F. Crabos, E. Andrieu, Scr. Mater. 2007, 56,
277.
[7] V. Brien, B. Décamps, Mater. Sci. Eng., A 2001, 316, 18.
[8] B. Lin, M. Huang, L. Zhao, A. Roy, V. Silberschmidt, N. Barnard,
M. Whittaker, G. McColvin, Philos. Mag. 2018, 98, 1550.
[9] J.-C. He, S.-P. Zhu, J.-W. Gao, R. Liu, W. Li, Q. Liu, Y. He, Q. Wang,
Int. J. Plast. 2024, 172, 103857.
[10] T. Wang, Y. Wang, D. Wei, S. Yang, Int. J. Fatigue 2024, 187, 108475.
[11] Z. Sun, X. Jiang, X. Zhan, K. Li, W. Zheng, D. Jiang, D. Liu, J. Dong,
L. Lou, Mater. Sci. Eng., A 2023, 888, 145831.
[12] B. Chen, W.-P. Wu, M.-X. Chen, Y.-F. Guo, Comput. Mater. Sci. 2020,
185, 109954.
[13] J. R. Mianroodi, P. Shanthraj, P. Kontis, J. Cormier, B. Gault,
B. Svendsen, D. Raabe, Acta Mater. 2019, 175, 250.
[14] Z.-G. Liu, C.-Y. Wang, T. Yu, Modell. Simul. Mater. Sci. Eng. 2013, 21,
045009.
[15] P. Peng, L. Lu, Z. Liu, X. Pei, L. Gan, Y. Xu, X. Zhang, Z. Ma, M. Guo,
L. Liu, J. Alloys Compd. 2022, 920, 165886.
[16] J. P. Du, C. Y. Wang, T. Yu, Modell. Simul. Mater. Sci. Eng. 2012, 21,
015007.
[17] W.-M. Choi, Y. Kim, D. Seol, B.-J. Lee, Comput. Mater. Sci. 2017, 130,
121.
[18] J. Wang, N. Lu, C.-H. Zhang, Mater. Today Commun. 2024, 38,
107664.
[19] P. M. Morse, Phys. Rev. 1929, 34, 57.
[20] X. W. Zhou, R. A. Johnson, H. N. G. Wadley, Phys. Rev. B 2004, 69,
144113.
[21] X. G. Wang, J. L. Liu, T. Jin, X. F. Sun, Y. Z. Zhou, Z. Q. Hu, J. H. Do,
B. G. Choi, I. S. Kim, C. Y. Jo, Scr. Mater. 2015, 99, 57.
[22] P. Li, Q. Q. Li, T. Jin, Y. Z. Zhou, J. G. Li, X. F. Sun, Z. F. Zhang, Int. J.
Fatigue 2014, 63, 137.
[23] S. Gowthaman, Compos. Struct. 2023, 5, 012005.
[24] A. Stukowski, Modell. Simul. Mater. Sci. Eng. 2010, 18, 015012.
[25] R. S. Crosson, J.-W. Lin, J. Geophys. Res. 1971, 76, 570.
[26] Z. Wu, E. Zhao, H. Xiang, X. Hao, X. Liu, J. Meng, Phys. Rev. B 2007,
76, 054115.
[27] J. X. Zhang, J. C. Wang, H. Harada, Y. Koizumi, Acta Mater. 2005, 53,
4623.
[28] I. S. Kim, B. G. Choi, J. E. Jung, J. Do, C. Y. Jo, Mater. Charact. 2015,
106, 375.
[29] J. Sun, R. Yin, Y. Hu, Y. Tan, Q. Xu, China Foundry 2023, 20, 365.
[30] J. Xu, X. Zhao, Q. Yue, W. Xia, H. Duan, Y. Gu, Z. Zhang, Mater. Today
Nano 2023, 22, 100335.
[31] M. Zaiser, Adv. Phys. 2006, 55, 185.
[32] L. Cui, J. Liu, R. L. Peng, J. Yu, J. Moverare, X. Sun, Mater. Charact.
2020, 163, 110241.
[33] C. A. Stein, A. Cerrone, T. Ozturk, S. Lee, P. Kenesei, H. Tucker,
R. Pokharel, J. Lind, C. Hefferan, R. M. Suter, A. R. Ingraffea,
A. D. Rollett, Curr. Opin. Solid State Mater. Sci. 2014, 18, 244.
[34] L. Garimella, P. K. Liaw, D. L. Klarstrom, JOM 1997, 49, 67.
[35] Q. Wang, Y. Wu, J. Chen, J. Song, C. Xiao, X. Hui, Scr. Mater. 2023,
224, 115151.
[36] Z. Y. Liang, Z. H. Tan, C. H. Zhang, S. Zhang, X. P. Tao, X. G. Wang,
S. M. A. Jafri, Z. W. Shi, Y. H. Yang, J. D. Liu, J. L. Liu, J. G. Li,
Y. Z. Zhou, X. F. Sun, Mater. Charact. 2023, 205, 113329.
[37] J. Luo, K. Dahmen, P. K. Liaw, Y. Shi, Acta Mater. 2015, 87, 225.
[38] J. Shen, X. Shen, J. Zhou, W. Yue, T. Zhang, Mater. Today Commun.
2024, 39, 109138.
[39] P. Li, Q. Q. Li, T. Jin, Y. Z. Zhou, J. G. Li, X. F. Sun, Z. F. Zhang, Mater.
Sci. Eng., A 2014, 603, 84.
[40] J. Wang, S.-L. Shang, Y. Wang, Z.-G. Mei, Y.-F. Liang, Y. Du, Z.-K. Liu,
Calphad 2011, 35, 562.
[41] B. R. Zhang, Z. Jia, X. Z. Duan, Acta Phys. Pol. A 2013, 123, 668.
[42] E. Clouet, J. M. Sanchez, C. Sigli, Phys. Rev. B 2002, 65, 094105.
[43] A. Kiejna, Phys. Rev. B 2003, 68, 235405.
[44] C. Kittel, P. McEuen, Introduction to Solid State Physics , John Wiley &
Sons, Hoboken 2018.
[45] G. Simmons, J. Grad. Res. Cent. 1965, 34, 84.
[46] D. Connétable, Y. Wang, D. Tanguy, J. Alloys Compd. 2014, 614, 211.
[47] E. A. Brandes, G. B. Brook, Smithells Metals Reference Book , Elsevier,
Amsterdam 2013.
[48] F. R. de Boer, W. C. M. Mattens, R. Boom, A. R. Miedema,
A. K. Niessen, Cohesion in Metals. Transition Metal Alloys , Elsevier,
New York 1988, 1, https://www.osti.gov/etdeweb/biblio/5556327
(accessed: April 2024).
[49] T. Flynn, Cryogenic Engineering, Revised and Expanded , 2nd ed., CRC
Press, Boca Raton, FL 2004, https://doi.org/10.1201/9780203026991.
[50] T. Korhonen, M. J. Puska, R. M. Nieminen, Phys. Rev. B 1995, 51,
9526.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2025, 27, 2402338 2402338 (10 of 10) © 2025 Wiley-VCH GmbH
 15272648, 2025, 7, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202402338 by Xian Jiaotong University, Wiley Online Library on [26/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
