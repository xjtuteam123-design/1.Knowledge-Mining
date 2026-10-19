# Site preference and effect on shear deformation of co-alloying elements addition to   -Ni3Al phase in Ni-based single crystal superalloys

<!-- source: D:\总文献\Site preference and effect on shear deformation of co-alloying elements addition to   -Ni3Al phase in Ni-based single crystal superalloys.pdf -->
<!-- file_sha256: 2e24f5b16f8a2212d02a944efc9273e5e625f3b1b467d81aa642b9b001031587 -->

## Page 1

Integrated Ferroelectrics
An International Journal
ISSN: 1058-4587 (Print) 1607-8489 (Online) Journal homepage: www.tandfonline.com/journals/ginf20
Site preference and eﬀect on shear deformation
of co-alloying elements addition to γ′-Ni3Al phase
in Ni-based single crystal superalloys
Changyun Li, Zhengcong Song, Guofa Mi, Jun Jiang, Jiahao Li & Qingyan Xu
To cite this article: Changyun Li, Zhengcong Song, Guofa Mi, Jun Jiang, Jiahao Li & Qingyan Xu
(2023) Site preference and eﬀect on shear deformation of co-alloying elements addition to γ
′-Ni3Al phase in Ni-based single crystal superalloys, Integrated Ferroelectrics, 233:1, 174-186,
DOI: 10.1080/10584587.2023.2191509
To link to this article: https://doi.org/10.1080/10584587.2023.2191509
Published online: 10 May 2023.
Submit your article to this journal 
Article views: 78
View related articles 
View Crossmark data
Citing articles: 2 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=ginf20

## Page 2

Site preference and effect on shear deformation of co-
alloying elements addition to c0-Ni3Al phase in Ni-based
single crystal superalloys
Changyun Li a,b , Zhengcong Song a, Guofa Mi a, Jun Jiang c, Jiahao Li d, and
Qingyan Xu d
aSchool of Material Science and Engineering, Henan Polytechnic University, Jiaozuo, China; bFaculty of
Engineering, China University of Petroleum-Beijing at Karamay, Karamay, China; cBeijing Computing
Center, Beijing, China; dKey Laboratory for Advanced Materials Processing Technology (MOE), School of
Materials Science and Engineering, Tsinghua University, Beijing, China
ABSTRACT
Alloy composition design at the atomic scale is one of the key strat-
egies for Ni-based single crystal superalloys (Ni-SCSs). In this article,
the site preference of co-alloying elements Re-M (M: Cr, Mo, W or
Re) in Ni
3Al system and the strengthening effects of co-alloying ele-
ments on the shear deformation resistance of Ni 3Al system are inves-
tigated using the first-principles method. It is found that the atom
pairs of co-alloying elements prefer Al –Al site and the site preference
of alloying elements is not affected by paired atoms. And co-alloying
atom pairs occupying Ni –Ni site have a strong mutual interaction,
which can be responsible for the formation of Re clusters and segre-
gation of alloying elements. The ideal shear strength (ISS) of the
quaternary Ni3Al system enhanced greatly by co-alloying elements is
at least higher 11.9% than that of any Ni 3Al system doped with sin-
gle alloying elements, which indicates there are common effect
among the co-alloying elements. The result of electronic structures
shows that the strong interaction between the alloy atoms and their
common the first nearest neighbors (FNN) Ni atoms is the common
strengthening mechanism. The present article provides valuable
guidelines for improving the mechanical strength of Ni-SCSs via alloy
composition design.
ARTICLE HISTORY
Received 18 June 2022
Accepted 9 March 2023
KEYWORDS
Ni3Al; Co-alloying elements;
Site preference; Ideal shear
strength; The first-principles
calculation
1. Introduction
Ni-SCSs that are mainly composed of the c0 phase (L1 2, order face-centered cubic (fcc),
Ni3Al based) precipitate coherently dispersed on the matrix c phase (fcc, Ni) are widely
used in aerospace due to their superior high-temperature mechanical properties [ 1–10].
The high-temperature strength of Ni-SCSs is mainly derived from the high volume frac-
tion of c0 phase [ 1, 11]. To improve the aero-engine efficiency and fit the service tem-
perature, the new generation of Ni-SCSs has a higher c0 precipitation volume fraction
(70 vol%) [ 12–14]. Hence, the study of the mechanical properties of the c0 phase should
partially reflect the overall performance of the Ni-SCSs [ 2]. Many alloying elements are
CONTACT Qingyan Xu scjxqy@tsinghua.edu.cn
/C2232023 Taylor & Francis Group, LLC
INTEGRATED FERROELECTRICS
2023, VOL. 233, 174 –186
https://doi.org/10.1080/10584587.2023.2191509

## Page 3

added to Ni-SCSs to enhance the mechanical property and long-term microstructure
stability, including Co, Cr, Mo, W, Al, Ti, Ta, Re, and Ru [ 1, 10, 15, 16]. Re has been
shown to play an important role in improving the mechanical properties of superal-
loys [ 17, 18]. But as the content of Re increases, topologically close-packed (TCP)
phases and Re –Re clusters are easily generated [ 2, 14, 19]. Thus it is quite necessary
to study their site occupancy behavior in Ni-SCSs and the effect of alloying elements
on the properties of Ni-SCSs. Many related works utilize the first-principles to study
t h es i t ep r e f e r e n c eo fs i n g l ea l l o y i n ge l e m e n t si nt h et e r n a r yN i3Al system. Most of
the single alloy elements prefer occupying the Al site, and some elements prefer the
Ni site or have no obvious tendency, which is basically the same as the experimental
results [ 5, 11, 20, 21].With the improvement of the experimental method, more accur-
a t eo b s e r v a t i o n sa r em a d eo nt h ed i s t r i b u t i o no fa l l o y i n ge l e m e n t s .F o re x a m p l e ,M o
and Re are found to be present in the c0 phase, which used to be supposed to exist
mainly in the c phase [ 22–24]. These experimental results have further promoted
many works on the site preference of single alloying elements in Ni 3Al. However, the
research on the doping of co-alloying elements is insufficient. And the understanding
of the site preference of co-alloying elements, dopant concentration and resulting
shear deformation resistance as a result of doping co-alloying elements is far from
complete. Fortunately, the first-principles method has been successfully applied to cal-
culate the theoretical strength of materials, and it is reliable in predicting the proper-
ties of alloy systems [ 25, 26]. There are many theoretical studies on ternary alloy
s y s t e m s ,f o re x a m p l e ,R ei m p r o v e st h ei d e a ls t r e n g t ho fc
0 phase greatly and Co has
n ou s ei ni m p r o v i n gt h eI S So ft h eN i3Al system at 0 K [ 2, 27, 28]. Unfortunately, the
research on quaternary alloy systems are only limited to Ni 3AlCr-M (M: Co, Ta) and
Ni3AlMo-M (M: Cr, Ta, and Re) [ 21, 29, 30]. Few studies have investigated Re-M
atoms pairs or the effect of quaternary alloying elements on the shear deformation
resistance of c
0-Ni3Al phase.
In the light of this background, the site preference of Re-M (M: Cr, Mo, W or Re)
co-alloying elements doped in the quaternary Ni 3Al alloy system is calculated with the
first-principles method in this work. Meanwhile, the site preference of co-alloying ele-
ments in different sizes of Ni 3Al systems and the interaction between co-alloying ele-
ments are also studied. The effect of co-alloying elements on the shear deformation
resistance of Ni 3Al system is evaluated by calculating the shear strain of the Ni 3Al Re-
M quaternary alloy system. And the strengthening mechanism of co-alloying elements
doped in Ni
3Al system is further analyzed by electronic structure information.
2. Computational Methods
In the present study, all the calculations are performed using the Vienna ab initio simu-
lation package (VASP) based on density-functional theory (DFT) [ 31]. The generalized
gradient approximation (GGA) [ 32] parameterized by Perdew-Burke-Ernzerhof (PBE)
[33, 34] is utilized to obtain the exchange-correlation functional. Projector augmented
wave (PAW) [ 35, 36] is used in the simulation with a plane-wave cutoff energy of
450 eV. The 7 /C2 7 /C2 7 k points meshes are sampled according to the Monkhorst-Pack
scheme for the shear model. And the shear deformation of close-packed {111} plane of
INTEGRATED FERROELECTRICS 175

## Page 4

Ni3Al system in both 110/C138
/C2
and ½112/C138 directionsis studied, and the lattice vector of
deformation R is acquired from [ 28, 37]:
R ¼ R0D (1)
where the matrix R0 represents the un-deformed lattice vectors, and the deformation
matrix D is described as:
D½112/C138 ¼
100
010
c 01
2
4
3
5D½110/C138 ¼
100
010
0 c 1
2
4
3
5 (2)
Where c is the shear strain. The shear strength is calculated according to the stand-
ard approach describing in ref [ 26, 28]. The stress-strain is determined by incrementally
deforming the model in the strain direction. Meanwhile, under fixed strain, all atomic
positions in the model are fully relaxed at each step until the maximum residual force
is less than 0.009 eV/Ð. The energy of electronic self-consistent is set to 10
/C0 5 eV. The
results of configuration from the previous step are used as the start of the next step in
the shear process.
To determine the site preference of co-alloying elements in the Ni
3Al system, a qua-
ternary Ni 3Al system with Re-M (M: Cr, Mo, W, or Re) pairs occupying four nearest-
neighbors of the Ni 3Al system respectively is used as the calculation model, where the
four sites (Al –Al, Al –Ni, Ni –Al, and Ni –Ni) occupied by Re-M are recorded as
ReAlMAl,R e AlMNi,R e NiMAl, and Re NiMNi respectively. As is shown in Figure 1 , the four
quaternary alloying models are Ni 3x(Alx/C0 2ReM), (Ni 3x/C0 1M) (Al x/C0 1Re), (Ni 3x/C0 1Re)
(Alx/C0 1M), and (Ni 3x/C0 2ReM)Alx. In this research, a 2 /C2 2 /C2 2 supercell (32 atoms) is used
to study the sites occupation of co-alloying elements, and another larger size model
with 3 /C2 3 /C2 3 supercell (108 atoms) is utilized to evaluate the effect of model size on
site preference. Both spin-polarized and non-spin-polarized have been considered [ 29].
Our calculated lattice parameter of Ni
3Al is 3.569 Ð, which is highly consistent with
the experimental data (3.570 Ð) and previously calculated results (3.566 and 3.567 Ð)
[21, 38, 39].
Figure 1. L12-Ni3Al model with the alloying atom pairs Re-M (M: Cr, Mo, W, or Re).
176 C. LI ET AL.

## Page 5

3. Results and Discussion
3.1. Site preference of alloying elements in Ni 3Al system
First, the study of site preference of single alloying atom M (Cr, Mo, W, Re, and Ru)
doped in Ni 3Al is performed in this section, which is solely governed by the enthalpy
and energy factor. The energy factor ENi!Al
X represents the energy obtained in transfer-
ring the alloying atom M from the initial site (Ni) to the nearest-neighbors site (Al).
The formation enthalpy H
d of a Ni 3Al-M alloying system and the energy factor can be
determined as: [ 5, 11]:
Hd ¼ ENimAlnM
total /C0 mENi
per/C0 nEAl
per /C0 EM
per
/C16/C17
=32 (3)
Ni3x/C0 1AlxM þ Ni3xAlx! Ni3xAlx/C0 1M þ Ni3x/C0 1Alxþ1 (4)
ENi!Al
M ¼ ENi3xAlx/C0 1M
total þ ENi3x/C0 1Alxþ1
total /C0 ENi3x/C0 1AlxM
total /C0 ENi3xAlx
total (5)
where d (M Al,M Ni,N i Al, and Al Ni) characterizes the types of antisite defects. ENimAlnM
total ,
ENi3xAlx/C0 1M
total , ENi3x/C0 1Alxþ1
total , ENi3x/C0 1Alx M
total , and ENi3xAlx
total describe the total energy of the ternary
alloy Ni 3xAlx-M system. E Ni,E Al, and E M are the total energies (per atom) of the
pure alloying elements of fcc Ni, fcc Al and M atom in its ground state, respectively.
The site preference of single element is estimated as [ 5, 40]: ENi!Al
M < 0 M prefers Al
site; ENi!Al
M > HAlNi þHNiAl M prefers Ni site; 0 < ENi!Al
M < HAlNi þHNiAl M prefers Al or
Ni sites randomly.
Thus, our formation enthalpy of HAlNi þHNiAl is 1.03 eV, which is in accordance with
the previous calculation values 1.03 eV and 1.12 eV [ 5, 41]. The calculation results show
that all the energy factors of the alloying atom are negative except Ru, which are given
in Table 1 . Hence, it can be obtained that Cr, Mo, W, and Re prefer to occupy Al site
in Ni 3Al system, while Ru occupies Al or Ni sites at random, which are consistent with
those previous research results [ 5, 11, 16]. Moreover, the difference value between
energy factors calculated with spin-polarized and non-spin-polarized method respect-
ively is less than 0.018 meV/atom, which means that the effects of spin-polarized can be
ignored [ 29].
In order to further explore the site preference of co-alloying elements in quaternary
Ni
3Al system, the energy factor that co-alloying atom pairs transfer between two of
those four types of Al –Al, Al –Ni, Ni –Al, and Ni –Ni sites is calculated according to the
following equation, for example, transfer from the initial Al –Al site to the Al –Ni site:
EAl/C0 Al!Al/C0 Ni
Re/C0 M ¼ ENi3x/C0 1 Alx/C0 1 ReM
total þ ENi3x/C0 1Alxþ1
total /C0 ENi3x/C0 1 Alx M
total /C0 ENi3x Alx
total (6)
It is worth pointing out that the transform between different positions is not a revers-
ible process [ 14]. But a negative value means that the final configuration is more stable
than the initial structure [ 29]. In other words, the co-alloying atom pair tends to occupy
the final site. The energy factor results of co-alloying atom pairs are described in Figure 2.
It can be seen from Figure 2a that the energy factor values converted to the other three
Table 1. Energy factor of single alloying atom M.
M Cr Mo W Re Ru
ENi!Al
M /C0 0.675 /C0 1.166 /C0 1.341 /C0 1.126 0.094
Site preference Al Al Al Al Composition-dependent
INTEGRATED FERROELECTRICS 177

## Page 6

sites (Al–Ni, Ni –Al, and Ni –Ni) with the Al –Al site as the initial position are all positive.
As shown in Figure 2b –d, the energy factors of co-alloying atom pairs being transferred
from Al –Ni, Ni –Al, and Ni –Ni sites to Al –Al site are negative values. These results indi-
c a t et h a tt h eA l - A ls i t ei sm o r es t a b l ea n dm o r el i k e l yt ob eo c c u p i e db yc o - a l l o y i n ge l e -
ments. Similarly, Re-M (M: Cr, Mo, W, or Re) co-alloying elements prefer Ni –Al site to
Al–Ni site in the quaternary Ni 3Al system, excepting for Re –Cr. This phenomenon can be
explained by comparing the energy factor of single elements. Because Mo and W are
p r o n et oo c c u p y i n gt h eA ls i t ec o m p a r i n gw i t hR e ,w h i l et h et e n d e n c yo fC rt ot h eA ls i t e
is weaker in the energy factor result of the site preference of single co-alloying elements.
Thus, the alloying element with a stronger site preference prioritizes occupying the site
when co-alloying elements are to occupy two different sites. According to the occupying
results, it can be concluded that the site preference of co-alloying elements is not changed
by the paired atomic combination, but the co-alloying elements with weaker site preference
is affected by the stronger one when occupying two different sites, for example, Re in Re –
Wa n dC ri nR e –Cr when occupying Ni –Al site.
The impacts of the Ni
3Al system size on the site preference of co-alloying elements
are investigated by calculating the energy factor of co-alloying elements transferring in
the same site of the Ni
3Al system with different sizes, taking Re –W and Re –Cr as exam-
ples. Results listed in Table 2 show that values of the energy factor are affected by the
size of Ni 3Al system, but the site preference of co-alloying elements is not changed.
Therefore, the site preference of co-alloying elements has little correlation with the size
Figure 2. Calculation of energy factor for four initial sites: (a) Al –Al site; (b) Al –Ni site; (c) Ni –Al site;
(d) Ni –Ni site.
178 C. LI ET AL.

## Page 7

of Ni 3Al system, and the 2 /C2 2 /C2 2 supercell model can meet the needs of the site pref-
erence study.
It is obvious that the four sites (Al –Al, Al –Ni, Ni –Al, and Ni –Ni sites) calculated as
above are all based on the nearest neighbors. However, too much Re can result in form-
ing Re clusters and TCP phases. Thus, it is necessary to make researches on the impacts
of distance between the atom pairs of co-alloying elements on their site preference.
That is to calculate the correlation energy of different distances to show whether co-
alloying elements are mutually exclusive or attracting, and divide Al-Al sites into the
first nearest neighbors (FNN, d¼a
0), the second nearest neighbors (SNN, d¼
ﬃﬃ ﬃ
2
p
a0) and
the third nearest neighbors (TNN, d¼
ﬃﬃ ﬃ
3
p
a0), in which a 0 is the lattice constant. The
correlation energy of three kinds of Al-Al sites in Ni 3Al system are calculated according
to the formula [ 42]:
DEAl/C0 Al
Re/C0 M ¼ HNi3xAlx/C0 2ReM /C0 HNi3xAlx/C0 1 Re /C0 HNi3xAlx/C0 1M (7)
where a position value of correlation energy indicates that co-alloying elements are
mutually exclusive, while a negative one means attracting. The extent of repulsion or
attraction increases with the absolute value of correlation energy. The results in Table 3
shows that co-alloying elements prefer TNN Al –Al site, and stay away from each other
in Ni 3Al system. But the correlation energy is negative when the atom pair occupy the
FNN Ni –Ni site in Ni 3Al system, which means an attractive interaction [ 14, 42]. The
result provides evidences for the formation of Re clusters and segregation of alloying
elements, and may even be responsible for the formation of the TCP phase.
3.2. Shear deformation resistance
The mechanical properties of Ni
3Al system can be obvious affected by the doping of
alloying elements. The site preference results of alloying elements show the changes that
alloying elements are doped in the Ni 3Al system, and provide accurate and reliable tern-
ary and quaternary Ni 3Al systems for relevant studies on the impacts of alloying ele-
ments on shear deformation of Ni 3Al system.
According to the site preference results, alloying elements occupying the Al site and
FNN Al –Al site in Ni 3Al are selected for shear deformation calculation. It is difficult to
measure experimentally the shear strength of a material [ 25]. Hence, a theoretical
Table 3. Correlation energy of Ni 3Al system doped co-alloying elements with different distance.
FNN (Al-Al) SNN (Al-Al) TNN (Al-Al) FNN (Ni-Ni)
DEAl/C0 Al
Re/C0 Cr 0.0371 0.0586 0.0062 /C0 0.3014
DEAl/C0 Al
Re/C0 Mo 0.0651 0.0836 0.0089 /C0 0.1087
DEAl/C0 Al
Re/C0 W 0.0863 0.0724 0.0091 /C0 0.0178
DEAl/C0 Al
Re/C0 Re 0.1014 0.0667 0.0067 /C0 0.2249
Table 2. Calculation results of energy factor with different sized configurations.
Size EAl/C0 Al!Al/C0 Ni
Re/C0 w EAl/C0 Al!Ni/C0 Al
Re/C0 w EAl/C0 Al!Ni/C0 Ni
Re/C0 w EAl/C0 Al!Al/C0 Ni
Re/C0 Cr EAl/C0 Al!Ni/C0 Al
Re/C0 Cr EAl/C0 Al!Ni/C0 Ni
Re/C0 Cr
2 /C2 2 /C2 2 2.75 2.46 5.41 1.97 2.22 4.72
3 /C2 3 /C2 3 2.86 2.58 5.29 2.10 2.35 4.43
INTEGRATED FERROELECTRICS 179

## Page 8

investigation into the effect of alloying elements on the shear behaviors of Ni 3Al system
is necessary. The shear stress is calculated by the following expression as describing in
ref [ 26].
s ¼ 1
V cðÞ
@E
@c (8)
where E is the total energy and V is the volume when the strain is c. The shear deform-
ation resistance of Ni 3Al system doped with and without alloying elements is calculated
to compare the effect of alloying elements on shear deformation, and the results of
energy-strain and stress-strain curves are shown in Figure 3 .
As is shown in the Figure 3b, d, f, h , all of the energy-strain curves are continuous
and rising, which indicates that the shear deformation is continuous and the calcula-
tions are reliable [ 2, 28]. There is an inflection point in the energy –strain curve of each
single alloying elements and co-alloying elements doping Ni 3Al system. In the stress –
strain curve, the strain at the inflection point corresponds to the highest point of stress,
of which stress of the highest point represents the ISS of the system. For example, the
stress of pure Ni 3Al system in the ½112/C138ð 111Þ shear direction reaches the maximum of
3.67 GPa at the strain of 0.2. By making comparisons between Figure 3a , c, it is found
that the ISS of the Ni 3Al-M system gets improved with varying degrees as the single
alloying element doping into Ni 3Al system, which is consistent with results in the previ-
ous studies [ 2, 28]. Re has the most significant improvement on shear deformation
resistance in both shear directions. Hence, in the doping co-allying elements, Re is
selected to study the common strengthening effects between Re and other elements —
Re-M (M: Cr, Mo, W, or Re). In the strain-stress curves of the Ni 3Al system doped
with co-allying elements, it can be found that within the range of the initial shear
deformation, for example, 0.036-0.04 strain, the shear stress is higher than that of any
system doped with single alloying elements in both shear directions, of which the rela-
tionship of size should be Re-M > Re > M. The Table 4 shows that the ISS of all the
Ni
3Al system doped with single alloying elements is more than 46.1% higher than that
of the pure Ni 3Al system in the two shear directions. The ISS of all the Ni 3Al system
doped with co-alloying elements Re-M is at least higher 11.9% than the Ni 3Al system
doped with single Rein the two shear directions. All of the co-alloying elements Re-M
have similar reinforcement effects in the two shear directions. Besides, the ISS of the
Re-M system is higher than that of any system doped with single elements, for example,
Re-W > Re and Re-W > W, which indicates that co-alloying elements have the effect of
common strengthening. The Ni
3Al system doping with Re-W are the most beneficial
for ISS, increasing by 20.7% in ½112/C138ð 111Þ direction.
To explore the reason why co-alloying elements have the strengthening effects on
shear resistance, the density of states (DOS) and the differential charge density are cal-
culated to better illustrating the physical mechanism by taking Re –Re and Re –W atom
pairs as examples.
The DOS is investigated and the results are shown in Figure 4.A si ss h o w ni nFigure 4b,
comparing with the pure Ni
3Al system, the peak value of Ni-3d or bitin the Ni 3Al sys-
tem doped with Re –W co-alloying atom pairs falls on the left side and rises on the
other side at Fermi level. The whole peaks move to high energy level, which indicates
180 C. LI ET AL.

## Page 9

Figure 3. Stress–strain and energy –strain curves of Ni 3Al system doped with single alloying atom in
½/C22110/C138ð 111Þ and ½11/C222/C138ð 111Þ directions (a –d); doped with co-alloying atom pair in ½/C22110/C138ð 111Þ and
11/C222½/C138 111ðÞ direction (e–h).
INTEGRATED FERROELECTRICS 181

## Page 10

that the interaction between Ni and other atoms is enhanced. Besides, the d orbitals of
the W and Re have obvious peaks on both sides of the Fermi level, of which the peaks
are well separated into bonding and anti-bonding regions by the deep valley near the
Fermi level. It indicates that the co-alloying atoms can be stable in the Ni 3Al system
after replacing the Al –Al site and have strong bonding tendencies and obvious interac-
tions with surrounding atoms [ 43, 44]. Moreover, there are strong d-d orbital hybridiza-
tion among W, Re and the FNN atom Ni. This enhanced strong interaction can be
considered as the main mechanism for the common strengthening of co-alloying ele-
ments. The same results can also be obtained in the Ni
3Al systems doped with Re –Re.
In order to gain a deeper insight into the origin of the common strengthen mecha-
nisms of the co-alloying elements in the Ni 3Al system, the differential charge density is
calculated in this step. The isosurface around the atom means the accumulation of
charge and the isosurface between atoms means the loss of charge. As shown in Figure 5,
Table 4. The ISS and critical shear strain of pure Ni 3Al system, ternary Ni 3Al–M alloy system and
quaternary Ni 3Al–Re–M alloy system in the shear direction of ½/C22110/C138ð 111Þ and ½11/C222/C138ð 111Þ:
System
½/C22110/C138ð 111Þ½ 11/C222/C138ð 111Þ
ISS (GPa) Critical shear strain ISS (GPa) Critical shear strain
Ni3Al 4.40 0.19 3.67 0.20
Ni3Al [ 38] 4.45 0.12 3.9 0.34
Ni3Al [ 14] 4.83 4.23
Ni3Al–Cr 6.43 0.19 5.48 0.21
Ni3Al–Mo 6.47 0.19 5.53 0.21
Ni3Al–W 6.62 0.19 5.66 0.21
Ni3Al–Re 6.81 0.18 5.64 0.19
Ni3Al–Re–Cr 7.65 0.17 6.53 0.18
Ni3Al–Re–Mo 7.75 0.17 6.65 0.18
Ni3Al–Re–W 7.93 0.17 6.81 0.18
Ni3Al–Re–Re 7.62 0.16 6.43 0.17
Figure 4. DOS of pure Ni 3Al and Re-M (W or Re) doping in Ni 3Al system: (a) pure Ni 3Al; (b) Ni 3Al-Re-
W; (c) Ni 3Al-Re–Re.
182 C. LI ET AL.

## Page 11

the charge accumulation is apparent between the alloy atoms and the surrounding host
atoms, which mainly exist along the {110} and {111} directions. In the Re-W doping
Ni
3Al system shown in Figure 5a , there is charge accumulation between the common
FNN Ni atoms and Re and W, and this indicates that there are strong covalent bonds
between them, which improves the shear deformation resistance of the Ni 3Al system. The
same is true in the Re-Re doping Ni 3Al system shown in Figure 5b , which explains the
reason why that the co-alloying elements have similar strengthening. These results are
highly consistent with the DOS results, that is, the strong interaction between the alloy
atoms with the common FNN Ni atoms of Re is the common strengthening mechanism.
4. Conclusions
In the article, the common effects of the Ni 3Al system doped with co-alloying elements
on their site preference and shear deformation resistance are investigated by means of
the first-principles method. The conclusions are drawn as follows:
1. Single alloying elements prefer the Al site, and the paired co-alloying elements
are more inclined to the Al-Al site, and the paired co-alloying elements do not
change the site preference of the elements. But when occupying the Ni-Al site,
elements with stronger site preference have the priority to the site and the
weaker ones are affected to some extent, for example, Re in Re-W and Cr in Re-
Cr. Moreover, co-alloying elements in the Ni
3Al system tend to stay away from
each other. But there is a strong mutual attraction when occupying the FNN Ni-
Ni sites, which can be responsible for the formation of Re clusters and segrega-
tion of alloying elements, and may even be responsible for the formation of the
TCP phase. The size of the Ni
3Al system does not affect the site preference of
alloying element. The results all above can be valuable guidelines for Ni-SCSs
composition design.
2. It is found that the shear deformation resistance of the Ni
3Al system after being
doped with single alloying elements has been significantly improved by at least
46.1% in both 110/C138ð 111Þ
/C2
and ½112/C138ð 111Þ directions. The shear deformation
resistance of the Ni 3Al system doped with co-alloying elements have been further
improved by at least 11.9% compared with single Re, and there are similar
enhanced effects in the co-alloying elements. The ISS of Ni 3Al system has the
Figure 5. Differential charge density of Re-M (W or Re) doping in Ni 3Al system: (a) Ni 3Al-Re-W;
(b) Ni 3Al-Re-Re.
INTEGRATED FERROELECTRICS 183

## Page 12

greatest enhancement by Re-W doping, increasing by 20.7% in ½112/C138ð 111Þ
direction.Moreover, the ISS of the Re-M system is higher than that of any sys-
tems doped with single element, for example, Re-W > Re, Re-W > W, which
indicates that common strengthening exist among the co-alloying elements. It is
found that the common strengthening mechanism of the co-alloying elements in
the Ni
3Al system is the strong interaction between the co-alloying elements and
their common FNN Ni according to the electronic structure analysis.
Acknowledgments
Thanks for the financial support from the National Science and Technology Major Project (2017-
VI-0003-0073, 2017-VII-0008-0101), and the National Key Research and Development Program
of China (2017YFB0701503) and the Fundamental Research Funds for the University of Henan
Province and the Natural Science Foundation of Henan Province (182300410266). We are grate-
ful to Prof Yunjiang Wang of Institute of Mechanics, Chinese Academy of Sciences, Mr. Sida Ma
and Mr. Cong Yang of Tsinghua University and Mr. Chen Liu of Institute of metal research,
Chinese Academy of Sciences for their inspiring discussions and help.
ORCID
Changyun Li http://orcid.org/0000-0003-4286-3579
References
1. H. Long et al. , Microstructural and compositional design of Ni-based single crystalline
superalloys: A review, J. Alloys Compd. 743, 203 (2018). DOI: 10.1016/j.jallcom.2018.01.224.
2. Y.-J. Wang, and C.-Y. Wang, Influence of the alloying element Re on the ideal tensile and
shear strength of c0-Ni3A., Scr. Mater. 61, 197 (2009). DOI: 10.1016/j.scriptamat.2009.03.042.
3. P. Peng et al. , First-principles study of the properties of Ni/Ni 3Al interface doped with B
or P., Mater. Sci. Eng. A 416, 169 (2006). DOI: 10.1016/j.msea.2005.10.019.
4. M. Chen, and C.-Y. Wang, First-principles investigation of the site preference and alloying
effect of Mo, Ta and platinum group metals in γ0-Co3(Al, W)., Scr. Mater. 60, 659 (2009).
DOI: 10.1016/j.scriptamat.2008.12.040.
5. C. Jiang, and B. Gleeson, Site preference of transition metal elements in Ni 3Al., Scr. Mater.
55, 433 (2006). DOI: 10.1016/j.scriptamat.2006.05.016.
6. Y. Rao et al. , Segregation of alloying elements to planar faults in γ0-Ni3Al., Acta Mater.
148, 173 (2018). DOI: 10.1016/j.actamat.2018.01.055.
7. K. Kumar, R. Sankarasubramanian, and U. V. Waghmare, Tuning planar fault energies of
Ni3Al with substitutional alloying: First-principles description for guiding rational alloy
design., Scr. Mater. 142, 74 (2018). DOI: 10.1016/j.scriptamat.2017.08.021.
8. A. Breidi, J. Allen, and A. Mottura, First-principles modeling of superlattice intrinsic stack-
ing fault energies in Ni 3Al based alloy., Acta Mater. 145, 97 (2018). DOI: 10.1016/j.actamat.
2017.11.042.
9. X. Zhang, and C.-Y. Wang, First-principles study of vacancy formation and migration in
clean and Re-doped γ0-Ni3Al, Acta Mater. 57, 224 (2009). DOI: 10.1016/j.actamat.2008.08.
052.
10. R. C. Reed, T. Tao, and N. Warnken, Alloys-By-Design: Application to nickel-based single
crystal superalloys., Acta Mater. 57, 5898 (2009). DOI: 10.1016/j.actamat.2009.08.018.
11. C. Jiang, D. J. Sordelet, and B. Gleeson, Site preference of ternary alloying elements in
Ni3Al: A first-principles study., Acta Mater. 54, 1147 (2006). DOI: 10.1016/j.actamat.2005.
10.039.
184 C. LI ET AL.

## Page 13

1 2 . W .Z h a o ,Z .S u n ,a n dS .G o n g ,V a c a n c ym e d i a t e da l l o y i n gs t r e n g t h e n i n ge f f e c t so nγ/γ0 interface
of Ni-based single crystal superalloys: A first-principles study.,Acta Mater. 135, 25 (2017). DOI:
10.1016/j.actamat.2017.05.074.
13. D. Blavette, P. Caron, and T. Khan, An atom probe investigation of the role of rhenium
additions in improving creep resistance of Ni-base superalloys., Scr. Metall. 20, 1395
(1986). DOI: 10.1016/0036-9748(86)90103-1.
14. Y. Chen et al. , Impact of correlative defects induced by double Re-addition on the ideal
shear strength of γ0-Ni3Al phases., Comput. Mater. Sci. 152, 408 (2018). DOI: 10.1016/j.
commatsci.2018.06.014.
15. A. Sato et al. , The effects of ruthenium on the phase stability of fourth generation Ni-base
single crystal superalloys., Scr. Mater. 54, 1679 (2006).
16. Q. Wu, and S. Li, Alloying element additions to Ni 3Al: Site preferences and effects on elas-
tic properties from first-principles calculations., Comput. Mater. Sci. 53, 436 (2012).
17. C. P. Liu et al. , Effect of rhenium and ruthenium on the deformation and fracture mechan-
ism in nickel-based model single crystal superalloys during the in-situ tensile at room tem-
perature. Mater. Sci. Eng. A 682, 90 (2017).
18. A. Kumar et al. , An ab initio investigation of the effect of alloying elements on the elastic
properties and magnetic behavior of Ni
3Al, Comput. Mater. Sci. 101, 39 (2015).
19. C. M. F. Rae, and R. C. Reed, The precipitation of topologically close-packed phases in rhe-
nium-containing superalloys. Acta Mater. 49, 4113 (2001).
20. Yu S. Mitrokhin et al. , Site preference of ternary alloying elements in Ni 3Al-X (X ¼ Co,
Nb): a first-principles calculations in combination with XPS study, Site preference of tern-
ary alloying elements in Ni
3Al-X (X ¼ Co, Nb): a first-principles calculations in combin-
ation with XPS study, Mater. Res. Express 4, 025016 (2017).
21. C. Booth-Morrison et al. , Chromium and tantalum site substitution patterns in Ni 3Al(L12)
γ0-precipitates, Appl. Phys. Lett. 93 (2008).
22. Y. Tu, Z. Mao, and D. N. Seidman, Phase-partitioning and site-substitution patterns of
molybdenum in a model Ni-Al-Mo superalloy: An atom-probe tomographic and first-prin-
ciples study, Appl. Phys. Lett. 101, 121910 (2012).
23. Y. Zhou et al. , The partitioning and site preference of rhenium or ruthenium in model
nickelbased superalloys: An atom-probe tomographic and first-principles study, Appl. Phys.
Lett. 93, 171905 (2008).
24. P. A. J. Bagot et al. , An Atom Probe Tomography study of site preference and partitioning
in a nickel-based superalloy, Acta Mater. 125, 156 (2017).
25. Y. Wang, Z. K. Liu, and L. Q. Chen, Thermodynamic properties of Al, Ni, NiAl, and Ni 3Al
from first-principles calculations. Acta Mater. 52, 2665 (2004).
26. D. Roundy et al. , Ideal Shear Strengths of fcc Aluminum and Copper, Phys. Rev. Lett. 82,
2713 (1999).
27. M.-L. Huang, and C.-Y. Wang, Effects of boron and carbon on the ideal strength of Ni
solution and Ni 3Al intermetallics: A first-principles study of tensile deformation., Comput.
Mater. Sci. 140, 140 (2017).
28. X. Wu, and C. Wang, Effect of the alloying element on the temperature-dependent ideal
shear strength of γ0-Ni3Al. RSC Adv. 6, 20551 (2016).
29. W. Zhao, Z. Sun, and S. Gong, Synergistic effect of co-alloying elements on site preferences
and elastic properties of Ni 3Al: A first-principles study. Intermetallics 65, 75 (2015).
30. M. Chaudhari et al. , Site preference and interaction energies of Co and Cr in gamma prime
Ni3Al: a first-principles study, Modell. Simul. Mater. Sci. Eng. 21 (2013).
31. G. Kresse, Efficient iterative schemes for ab initio total-energy calculations using a plane-
wave basis set. Phys. Rev. B (Condensed Matter) 54, 11169 (1996).
32. J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made sim-
ple, Phys. Rev. Lett. 77 (18), 3865 (1996). DOI: 10.1103/PhysRevLett.77.3865.
33. M. Ernzerhof, and G. E. Scuseria, Assessment of the Perdew –Burke–Ernzerhof exchange-
correlation functional. J. Chem. Phys. 110, 5029 (1999).
INTEGRATED FERROELECTRICS 185

## Page 14

34. B. Hammer, L. B. Hansen, and J. K. Nørskov, Improved adsorption energetics within dens-
ity-functional theory using revised Perdew-Burke-Ernzerhof functionals. Phys. Rev. B 59,
7413 (1999).
35. P. E. Bl €ochl, Projector augmented-wave method. Phys. Rev. B 50, 17953 (1994).
36. G. Kresse, and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-
wave method. Phys. Rev. B 59, 1758 (1999).
37. S. L. Shang et al. , Effects of alloying element and temperature on the stacking fault energies
of dilute Ni-base superalloys. J. Phys. Condens. Matter 24, 155402[Database] (2012).
38. Z. Wen et al. , Z. Wen et al., Theoretical Calculations of the Ideal Strength of Ni, NiAl and
Ni3Al in Tension and Shear, Sci. Adv. Mater. 10, 1420 (2018). Sci. Adv. Mater. 10, 1420
(2018).
39. R. C. Reed, Line 564-R39: R. C. Reed, The Superalloys: Fundamentals and Applications,
Cambridge University Press, 2006. 372. Cambridge University Press, 2006. 372.
40. M. Wen, and C.-Y. Wang, Transition-metal alloying of γ0–Ni3Al: Effects on the ideal uniaxial
compressive strength from first-principles calculations, Phys. Rev. B 97, 024101 (2018).
41. M. Chaudhari et al. , Site occupancy of chromium in the γ0-Ni3Al phase of nickel-based
superalloys: a combined 3D atom probe and first-principles study. Philos. Mag. Lett. 92,
495 (2012).
42. Y.-J. Li et al. , Strengthening of γ-TiAl-Nb by short-range ordering of point defects.
Intermetallics 19, 793 (2011).
43. J. Xu, T. Oguchi, and A. J. Freeman, Solid-solution strengthening: Substitution of V in
Ni3Al and structural stability of Ni 3(Al,V), Phys. Rev. B Condens. Matter 36 (8), 4186
(1987). DOI: 10.1103/physrevb.36.4186.
44. Z. Song et al. , First principles calculation on the newly superhard materials of W-B-C tern-
ary system. First principles calculation on the newly superhard materials of W-B-C ternary
system, Solid State Commun. 301, 113705 (2019).
186 C. LI ET AL.
