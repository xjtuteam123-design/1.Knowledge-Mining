# 10.1016_j.commatsci.2018.11.027

<!-- source: D:\总文献\10.1016_j.commatsci.2018.11.027.pdf -->
<!-- file_sha256: c9b5cfddea555a15d1ee1474943adf14d2b7e2ed52ea0c98293df9f83d6237b7 -->

## Page 1

Contents lists available at ScienceDirect
Computational Materials Science
journal homepage: www.elsevier.com/locate/commatsci
Thermo-mechanical properties of Ni-Mo solid solutions: A ﬁrst-principles
study
Wenyue Zhao a,b,⁎
, Wei Li c, Xiaoqing Li c, Shengkai Gong a, Levente Vitos c,d,e, Zhimei Sun a,b
a Key Laboratory of Aerospace Materials and Performance (Ministry of Education), Key Laboratory of High-Temperature Structural Materials & Coatings Technology
(Ministry of Industry and Information Technology), School of Materials Science and Engineering, Beihang University, Beijing 100191, China
b Center for Integrated Computational Materials Engineering, International Research Institute for Multidisciplinary Science, Beihang University, Beijing 100191, China
c Applied Materials Physics, Department of Materials Science and Engineering, Royal Institute of Technology, Stockholm SE-100 44, Sweden
d Department of Physics and Astronomy, Division of Materials Theory, Uppsala University, Box 516, SE-751210 Uppsala, Sweden
e Wigner Research Centre for Physics, Research Institute for Solid State Physics and Optics, P.O. Box 49, H-1525 Budapest, Hungary
ARTICLE INFO
Keywords:
Superalloys
Solid solution
Bulk modulus
Stacking fault energy
Twinning
First-principles calculations
ABSTRACT
The mechanical strength of Ni-based single-crystal superalloys under service condition is related to the thermo-
mechanical properties of the disordered γ matrix. Here we use density functional theory and quasi-harmonic
approximation to determine the temperature-dependent bulk moduli and generalized stacking fault energies
(GSFEs) of Ni-Mo solid solutions. We show that the increasing temperatures between 1000 K and 1400 K cause
evident reductions in the bulk moduli and planar fault energies of Ni-Mo alloys. Furthermore, their negative
slopes versus temperature are gradually diminished with increasing Mo concentration except that of the unstable
stacking fault energy. Adopting recent theoretical models for twinning based on GSFE, increasing temperature
enhances the twinnability of low-Mo alloys but has limited in ﬂuences in the case of high-Mo alloys. The com-
position-dependent thermal expansion, the thermal electronic excitation and the magnetic transition are shown
to be the main factors rendering the complex variations in the elastic properties and twinning behavior of Ni-Mo
solid solution with temperature.
1. Introduction
There has been continuous interest in the microscopic processes
during the mechanical deformation of Ni-based single crystal (SC) su-
peralloys, which are applied in the modern turbine engines with-
standing load and high temperature [1]. With increasing content of Al
and other alloying elements, the volume fraction of the ordered γ′
precipitates becomes high, which are connected by the narrow γ
channels [2]. As a consequence, the dislocation activity restricted to the
γ matrix plays an increasingly important role in di ﬀerent creep regimes
[1,3,4]. Preceding the dislocation cutting into the γ′ preticipate, these
dislocation motions are closely related to the creep deformation me-
chanisms of SC superalloy [5]. Moreover, slowly di ﬀusing alloying
elements can also enhance the creep resistances of superalloys via the
solid solution strengthening contribution to internal stresses [4].
Therefore, a thorough study of the thermo-mechanical properties of γ
solid solution becomes essential for guiding the rational design of Ni-
based SC superalloys.
Both the γ and γ′ phases have the face-centered cubic (fcc) structure,
and the plastic deformation of fcc crystal via dislocation motions is
considered to be governed by the competition between full slip and
twinning. According to phenomenological models, the stacking fault
energy controls the microscopic process of partial dislocation motions
during the plastic deformation of fcc crystals [6,7]. Low stacking fault
energy of the γ phase has been proved to impede the dislocation cross-
slip and improve the creep resistances of the superalloys [8,9]. This can
be achieved by introducing di ﬀerent alloying elements into the fcc Ni
matrix [10–12]. However, many studies have revealed that the de-
formation modes of fcc metals cannot be determined by stacking fault
energy alone [13–15]. Instead, generalized stacking fault energy (GSFE)
or the so called γ-surface can provide more comprehensive information
on the operation of plastic deformation mechanisms [16,17]. The γ-
surface or the GSFE represents the excess energy associated with slip-
ping half of the fcc crystal within a close-packed (1 1 1) plane along the
lowest energy path corresponding to the 〈112 〉 direction. The three
fundamental parameters describing the γ-surface are the intrinsic
stacking fault (ISF) energy, the unstable stacking fault (USF) energy and
the unstable twin fault (UTF) energy. The ISF is formed when one close-
https://doi.org/10.1016/j.commatsci.2018.11.027
Received 18 September 2018; Received in revised form 24 October 2018; Accepted 15 November 2018
⁎ Corresponding author at: School of Materials Science and Engineering, Beihang University, 37 Xueyuan Rd., Beijing 100191, China.
E-mail address: wendyzhao56@buaa.edu.cn (W. Zhao).
Computational Materials Science 158 (2019) 140–148
0927-0256/ © 2018 Elsevier B.V. All rights reserved.
T

## Page 2

packed atomic layer is missing from the ideal fcc (1 1 1) packing, which
corresponds to a two-layer hexagonal close-packed (hcp) embryo em-
bedded in the fcc lattice. The USF and UTF energies describe the lowest
energy barriers for the nucleation of leading and twinning partial dis-
locations respectively. The propensity of twinning (i.e. twinnability) of
fcc metal can be characterized by various models based on the above
parameters [16,18,19]. Studying the ISF, USF, UTF energies and the
corresponding twinning models is expected to contribute to a deeper
understanding of the plastic behavior Ni-based alloys, which is in turn
closely related to the creep deformation mechanisms speci ﬁcally at
intermediate temperature [5].
Due to the di ﬃculties associated with measuring the ISF energy at
high temperature [20] and the lack of methodologies obtaining the
unstable energies merely from experiments, ﬁrst-principles calculations
have become the primary tools to obtain GSFE and thus analyze the
plastic deformation behaviors of metals and alloys [21–23]. Many
theoretical works have focused on the GSFE of pure Ni as well as the
alloying e ﬀects on the ISF energies of Ni-based binary alloys at 0 K
[20,24–26]. Nevertheless, little attention has been paid to the GSFEs of
disordered Ni-based solid solutions at ﬁnite temperature. Moreover, the
published results on the temperature-dependent planar fault energy of
pure Ni via phonon calculations are also inconsistent [27–29]. Because
Mo is the main solid-solution strengthening element in γ phase [1], our
previous study on Ni-Mo solid solution focused on the e ﬀect of Mo at
static conditions and revealed that increasing Mo concentration
changes the shape of the GSFE curve and enhances the twinnability as a
result [30].
In the present work, the elastic parameters and the plastic behaviors
characterized by the γ-surface of Ni-Mo solid solution are studied at
temperatures between 1000 K and 1400 K. We pay close attentions to
the composition and temperature e ﬀects in order to uncover the
strengthening mechanisms of Mo in the γ phase under the service
condition of Ni-based SC superalloys. Firstly, the equilibrium volumes
and elastic parameters of Ni-Mo solid solutions are calculated as a
function of temperature and composition using the ﬁrst-principles alloy
theory in combination with the quasi-harmonic approximation. Then,
the GSFEs of Ni-Mo solid solutions are calculated taking into account
the obtained thermal expansion. The plastic deformation behavior of
Ni-Mo is evaluated by studying the twinnability varied with tempera-
ture and composition. Finally, the contributions of the magnetic tran-
sition, the thermal electronic excitation and the lattice vibration to the
GSFEs of Ni-Mo solid solutions at high temperature are discussed in
detail in order to reveal the atomistic mechanisms behind the disclosed
trends.
2. Theoretical methods
2.1. Elastic properties
The elastic properties of a single cubic crystal are described by three
independent components ( C
11, C12 and C44) in the elastic tensor, which
is deﬁned as the second-order derivative of energy with respect to strain
tensor. In practice, the tetragonal shear modulus ′ =−CC C ( )1
2 11 12 and
C44 were evaluated from the total energy changes caused by volume-
conserving distortions (Eq. (S1) in Supplementary). The bulk modulus B
was calculated by ﬁtting the free energy versus volume ( F-V) curve
according to the Birch-Murnaghan equation of state (EOS) [31].
2.2. Temperature-dependent properties
In an e ﬀort to predict the thermo-mechanical properties of fcc Ni-
Mo solid solutions, the ﬁrst-principles quasi-harmonic approximation
(QHA) was applied to describe the Helmholtz free energy F(V, T)a sa
function of volume V and temperature T [32],
=+ +VT V VT VTFE F F(, ) ( ) (, ) (, )sta ele vib (1)
in which Esta(V) is the static energy at 0 K, Fele(V, T) and Fvib(V, T) are
the contributions due to the thermal electronic excitation and the lat-
tice vibration, which were estimated using the Fermi-Dirac distribution
function [33] and the Debye model [34] respectively. The elastic con-
stants for di ﬀerent volumes were calculated in order to self-consistently
obtain the equilibrium Debye temperature, which was used to de-
termine the vibration contribution at speci ﬁc temperature. The thermal
expansion of fcc Ni-Mo within QHA was determined from the tem-
perature depended equilibrium volume
V T()0 which in turn is obtained
by minimizing the Helmholtz free energy at each temperature T, i.e.
=TV TFV T F(( ) , ) m i n ( , )
V
0 .
2.3. Generalized stacking fault energy
The most common slip system in fcc crystals is 〈〉110 { 111 } . The
smallest full dislocation with a Burgers vector of =〈 〉b 1 / 2 110 can en-
ergetically dissociate into two Shockley partial dislocations such as
→+[1¯ 10 ] [ 1 ¯ 12 ] [ 1 ¯ 12¯]1
2
1
6
1
6
. An intrinsic stacking fault (ISF) forms
when the leading partial dislocation sweeps over the {1 1 1} plane. If a
trailing partial dislocation slides on the same plane (but in a di ﬀerent
direction), then this planar fault area is removed and we arrive at full
slip. Otherwise, an extrinsic stacking fault (ESF) forms if a twinning
partial dislocation slides on the adjacent plane (twinning).
In the present work, a supercell model containing of 9 fcc-(1 1 1)
layers with the primitive lattice vectors ( a
1, a2, a3) along the [11¯ 0],
[01¯ 1¯] and [111 ] directions was constructed to mimic the process de-
scribed above. The generalized stacking fault was generated by shifting
the primitive vector a3 along the [112¯] direction with displacement b
ranging from 0 to 2b 0, in which the Burgers vector is =b a / 6[ 112¯]00
(Fig. 1). The interlayer distance was allowed to relax only along the
direction perpendicular to the fault plane (i.e. in the [111 ] direction)
until the total energy of the supercell was minimized. The lattice
parameters along a1 and a2 were ﬁxed to the ideal values in the perfect
fcc lattice of pure Ni or Ni-Mo solid solution without planar fault. The
GSFE (
γb) is calculated as follows,
=−γF F A() /b b0 (2)
where Fb is the free energy of the supercell containing a planar fault
with b, F0 is the free energy of the perfect supercell, and A is the area of
the (1 1 1) plane in the supercell. The four extreme values on the curve
of γb versus displacement correspond to the USF energy, ISF energy,
UTF energy and ESF energy. More details of the supercell models for
generalized stacking faults can be found in Refs. [23,30].
2.4. Total energy calculation
All the total energy calculations were carried out by using the exact
muﬃn-tin orbital (EMTO) method [35–37] based on density functional
theory (DFT) [38]. Perdew-Burke-Ernzerhof (PBE) exchange-correla-
tion functional is applied within the generalized gradient approxima-
tion (GGA) [39]. The EMTO method is an improved screened Korringa-
Kohn-Rostoker (KKR) method [40,41], where large overlapping mu ﬃn-
tin potential spheres are used to represent the exact Kohn-Sham po-
tential more accurately as compared with traditional mu ﬃn-tin
schemes [42]. In the framework of the EMTO, the coherent potential
approximation (CPA) [37,43] was adopted to treat the compositional
disorder of Mo in Ni-based solid solution and the full charge-density
technique [35,36] was used to calculate the total energy. The EMTO-
CPA method has been proved to predict the elastic properties of metals
and the planar fault energies for the close-packed faulted lattices well
[44–47].
The parameter α
c in the screened impurity model (SIM) was opti-
mized to be 0.87 for Ni-Mo system, which was used to correct the
electrostatic energy [48,49]. The k-mesh was carefully tested to be
27 × 27 × 27 and 12 × 24 × 3 for elastic constants and planar fault
energy calculations respectively, due to the negligible changes in total
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
141

## Page 3

energy (on the order of 10 −6 Ry) caused by two more k points on any
primitive vector. The pure Ni and the Ni-Mo solid solutions were
treated as ferromagnetic (FM) state at 0 K and nonmagnetic (NM) state
at temperatures ranging between 1000 K and 1400 K (which are far
above the Curie temperature of Ni, =T 631Kc
Ni ). At this point we should
mention that a better description of the high-temperature paramagnetic
phase would be the disordered local magnetic (DLM) model [50].
However, a static DLM produces vanishing local magnetic moments on
Ni sites and thus it is equivalent to the non-magnetic scheme. Here the
longitudinal spin ﬂuctuation e ﬀects were neglected, which would in-
duce non-zero moments on Ni atoms at elevated temperatures. Addi-
tional ﬁrst-principles calculations using the Vienna Ab initio Simulation
Package (VASP) [51] within GGA-PBE were also carried out in order to
verify some of the EMTO results. The plane-wave cuto ﬀs and k-point
grids were all tested to achieve the global precision switch “Accurate”
with proper sizes of supercell models.
3. Results
3.1. Elastic properties at 0 K
Based on the equilibrium Wigner-Seitz radii of Ni-Mo solid solutions
obtained in our previous EMTO calculations [30], the elastic para-
meters including equilibrium bulk moduli, elastic constants and shear
moduli at 0 K were calculated ﬁrst and compared with the VASP results
obtained using 16-atom supercell models. As shown in Fig. 2, the in-
creasing Mo concentration elevates the equilibrium bulk modulus ( B
0)
of fcc Ni-Mo solid solution, while it decreases the tetragonal shear
modulus (C') following a linear law. The slopes of B
0 and C' against Mo
concentration calculated by EMTO are almost the same with those using
VASP. Compared with the experimental results, the EMTO under-
estimates C' of pure Ni while overestimates B0 of pure Ni and Ni-Mo
with lower Mo content. However, the theoretical results are still con-
sidered to be reasonable, as the experimental data quoted are estimated
using the reduction in the bulk modulus of pure Ni from room
temperature to 0 K [29,52,53]. Further results in shear moduli, bulk/
shear modulus ratio ( B
0/G0) and elastic anisotropy constants
(Supplementary data Table S1) indicate that higher Mo concentration
enhances the anisotropy and ductility of the Ni-based solid solution
with larger values of B
0/G0 ratio and AG, in addition to its positive
eﬀect on the bulk modulus. Hence, based on the static elastic para-
meters we conclude that Mo addition strengthens the γ matrix of Ni-
based SC superalloys in the composition range studied.
3.2. Thermal expansion and bulk modulus at high temperature
The thermal expansions and bulk moduli of Ni-Mo solid solutions at
ﬁnite temperature were calculated using ﬁrst-principles QHA. To model
the service conditions of Ni-based SC superalloys, in the present study
we considered the temperatures ranging between 1000 K and 1400 K.
First, the magnetic properties of Ni-Mo system were analyzed since the
magnetic transition of pure Ni is around 631 K. The results indicate that
the magnetic moments of Ni and Mo components in FM state at 0 K drop
rapidly with increasing Mo concentration, while those in paramagnetic
(PM) state at 1000 K modeled via the static DLM picture all approach 0
μB( Supplementary data Table. S2). The rapid loss of magnetic order in
Ni due to Mo alloying has been observed and its Curie temperature is
also considered to decrease obviously with increasing Mo content
[54,55]. Therefore, the Ni-Mo solid solutions are treated as PM systems
at high temperature. At this point we should mention that thermal
longitudinal spin ﬂuctuations could give rise to a ﬁnite magnetic mo-
ment within the present temperature interval [56–58]. However, since
such ﬂuctuations were reported to have small impact on the elastic
properties of paramagnetic alloys, here we neglect them and treat the
system with static DLM, which actually reduces to the NM state.
The composition of the Ni-based solid solution is ﬁxed to 5at.% Mo
ﬁrst to study the temperature e ﬀects solely. The calculated thermal
expansion with a linear coe ﬃcient of about 12.6 × 10
−6·K−1 agrees
well with the experimental value (14.1 × 10 −6·K−1) [59], while its
equilibrium bulk modulus decreases by 12.5 –18.7% with increasing
Fig. 1. Supercell models for the calculations
of generalized stacking fault energy. Two
repetitions along [1 1 1] direction of the 9-
layer supercells are depicted in order to
show the stacking sequence changes after
the introduction of the planar faults. (a)
Perfect fcc supercell with the stacking se-
quence of ABCABCABCABCAB…; (b) ISF
conﬁguration with the stacking sequence of
ABCABCABC|BCABC…, formed with the
displacement b=b
0; (c) ESF con ﬁguration
with the stacking sequence of ABCABC-
ABCB'ABCAB…, formed with the displace-
ment b=2 b 0. =b a / 6[ 112¯]00 is the Burgers
vector of a Shockley partial dislocation.
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
142

## Page 4

temperature from 1000 K to 1400 K ( Fig. 3). Next the composition ef-
fects on the thermal expansion and bulk modulus of Ni-Mo solid solu-
tion at 1000 K are discussed. The Wigner-Seitz radius of the solid so-
lution has a positive slope as a function of Mo content at 1000 K,
following almost the same trend as that at 0 K ( Fig. 4 (a)). As a result,
lower thermal expansion coe ﬃcients ( =−α aaa T () / ( · )lT 0 0 ) are ob-
tained for the solid solutions with higher Mo content because of their
larger lattice constants at 0 K ( a0). These results are consistent with the
previous ones obtained by molecular dynamics simulation [59]. The
smaller thermal expansion coe ﬃcient but larger atomic size of Mo than
that of Ni are partly the reasons behind the obtained trends [59]. On the
other hand, it is noteworthy that the reduction in the bulk modulus of
solid solution at 1000 K decreases slightly with increasing Mo con-
centration ( Fig. 4(b)), which suggests the stronger strengthening e ﬀect
of higher Mo content in γ matrix at service temperature. Compared with
the experimental results [53,59], the EMTO results slightly over-
estimate the slope of lattice constant and underestimate that of bulk
modulus against Mo concentration. The increased deviation between
the theoretical and experimental data at high Mo concentration might
be due to the chemical inhomogeneities (e.g. segregations or other al-
loying elements) in the experimental samples which are ignored in the
present solid solution scheme.
3.3. Generalized stacking fault energy at high temperature
Using the equilibrium volumes at ﬁnite temperatures, the GSFEs of
Ni-Mo solid solutions were calculated and compared with those at 0 K.
Our previous study on the GSFE of Ni-Mo solid solution at 0 K has
obtained consistent results with the VASP ones, which has proved the
feasibility of the EMTO method in the planar fault energy calculation
Fig. 2. Calculated tetragonal shear moduli and bulk
moduli of Ni-Mo solid solutions by EMTO (unit cell
model, ﬁlled symbols), VASP (supercell model,
open symbols) (both at 0 K) and experimental data
(half-ﬁlled symbols). aExperimental values of pure
Ni recommended by Ref. [52]. bExtrapolated from
the experimental data at room temperature [53] to
0 K, according to the bulk modulus reduction of
pure Ni with increasing temperature [29].
Fig. 3. Calculated equilibrium Wigner-Seitz radius and bulk modulus of Ni-5at.%Mo solid solution at high temperature ( ﬁlled symbols). The experimental lattice
constants extrapolated from 0 K to 1000 K using the linear thermal expansion coe ﬃcient [59] are also plotted for comparison (half- ﬁlled symbols).
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
143

## Page 5

[30]. At this point we should emphasize an important aspect of the
ﬁnite temperature GSFE calculations. The USF or UTF energy is an
energy barrier meaning that no free energy can be deﬁ ned for these
structures. The only way to describe the full temperature dependence of
these barriers is to carry out molecular dynamics simulation based on
interaction potentials. Here we follow another route and calculate the
energy barriers from energies only accounting for thermal expansion
and electronic excitation. In order to make our approach consistent, the
USF, UTF and ISF energies were calculated using the same approx-
imation method above. Nevertheless, the lattice vibration contribution
to the ISF energy at ﬁnite temperature will be estimated and discussed
later separately. The GSFE changes caused by the magnetic transition
from FM to NM as the temperature rising from 0 K to above 1000 K are
analyzed as well.
The ISF energy of NM Ni at 1000 K was calculated to be 118 mJ/m
2.
Compared with the FM value at 0 K (150 mJ/m 2), the slope against
temperature is basically consistent with the experimental result dγ isf/
dT = −0.04 mJ/(m2·K) [60]. It is important to mention that the
thermal electronic excitation has an obvious e ﬀect on the ISF energy of
Ni, which lowers the NM value of 135 mJ/m 2 considering only the
thermal expansion we get further to 118 mJ/m 2. As for Ni-Mo solid
solutions, the ISF energies of Ni-5.at% Mo were calculated from 1000 K
to 1400 K both in FM and NM states. The results in Fig. 5 show that the
ISF energy of Ni-5.at% Mo decreases with increasing temperature.
Diﬀerent from the obvious contributions from the thermal expansion
and thermal electronic excitation, the magnetic transition from FM to
NM only contributes a little to the ISF energy drop.
At 1000 K, the ISF energies of Ni-Mo solid solutions are studied as a
function of Mo content so as to reveal the composition e ﬀect at high
temperature (Fig. 6). Similar to the case at 0 K, the ISF energy of Ni-Mo
solid solution at 1000 K decreases with increasing Mo concentration but
with a weaker descending slope. In other words, Mo addition reduces
the temperature e ﬀect for the ISF energy and Ni-15at.%Mo has almost
the same ISF energy at 1000 K with that at 0 K. The thermal expansion
and the thermal electronic excitation also give limited contributions to
the ISF energy reductions of the high-Mo solid solutions.
The unstable planar fault energies including the USF and UTF en-
ergies are obtained as the local maxima of γ-surface. Here we approx-
imate these energy barriers with energies calculated at b = 0.5b
0 and
b = 1.5b0 respectively, because the true local maxima are usually lo-
cated very close to the middle point connecting the two consecutive
minima. Similar to the case of ISF energy, the unstable planar fault
energies of Ni-Mo solid solution both decrease with increasing tem-
perature obviously (Figs. 7 and 8). However, high temperature (1000 K)
has a small e ﬀect on the variation of the USF energy with composition
(Fig. 8(a)), while the slope of the UTF energy against Mo concentration
is less negative than that at 0 K in a small extent ( Fig. 8(b)). Unlike the
case of the ISF energy, the higher Mo content has no weakening e ﬀect
on the reductions of the unstable planar fault energies due to thermal
expansion. Moreover, distinctly stronger e ﬀects of magnetic transition
than those of thermal electronic excitation are observed on the USF and
UTF energies. This phenomenon is particular true for the solid solutions
with 5at.%Mo, in which the magnetic transition has almost constant
eﬀects on the USF and UTF energies with increasing temperature
(Fig. 7). It is noteworthy that the consideration of thermal electronic
excitation elevates the unstable planar fault energies ( Fig. 8) rather
than decline them as it does on the ISF energy ( Fig. 5 ), except for the
UTF energies of Ni-5at.%Mo ( Fig. 7(b)). Here, the ESF energies of Ni-
Mo solid solutions at high temperature are not discussed individually,
due to their almost equal values to those of the ISF energies [30].
3.4. Twinnability at high temperature
Combined with recent plasticity models, the GSFEs of fcc metals
have been widely used to interpret many dislocation-related phe-
nomena [61] and predict the Peierls stress [62] as well as the plastic
Fig. 4. Calculated equilibrium Wigner-Seitz radii (a) and bulk moduli (b) of Ni-Mo solid solutions at 1000 K ( ﬁlled symbols). The experimental results at 0 K and high
temperatures are also plotted for comparison (half- ﬁlled symbols) [53,59]. The shadow regions with dashed edges are depicted in order to show the variation trends
of Wigner-Seitz radius and bulk modulus with composition more clearly.
Fig. 5. Intrinsic stacking fault energy of Ni-5at.%Mo solid solution at high
temperature ( ﬁlled circles). The calculation results without the thermal elec-
tronic excitation contribution in ferromagnetic (FM) and nonmagnetic (NM)
states are plotted for comparison (half- ﬁlled symbols). Previous theoretical
result at 0 K is also presented by a dash line [30].
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
144

## Page 6

deformation regimes of metals [16]. As for the plastic deformation
mechanism closely related to the emission of the trailing partial dis-
location following the leading one, several measures have been pro-
posed to evaluate the twinning tendencies of metals based on plastic
mechanics. In the present study, two twinnability measures are used to
evaluate the twinning tendency of Ni-Mo solid solution at high tem-
perature, which have been proved to be applicable in this system [30]
with the expressions as follows [16,18]:
=−Tγ γ γ(3 2 )/usf isf utf (3)
=−γγγ γ /( )d isf usf isf (4)
The twinnability measure T is derived within the Peierls framework
involving the ISF, USF and UTF energies, while γd is an improved
measure simply depending on the ﬁrst half of γ-surface. Twinning
mechanism is considered to be favored with T > 1 or small positive
value of γd.
Based on the GSFE results of Ni-Mo solid solutions at high tem-
perature, the temperature and composition e ﬀects on their twinnability
are studied. As shown in Fig. 9(a), the twinnability of Ni-5at.%Mo is
enhanced obviously with increasing temperature which has much
higher T value larger than 1 and small positive
γd value. In other words,
twinning is favored over dislocation slip more at high temperature.
However, the twinnability changes caused by temperature decrease
with increasing Mo concentration at 1000 K, especially when the Mo
content is higher than 10at.% ( Fig. 9(b)). Consequently, the slopes of
the twinnability measures become weaker than those at 0 K. Among the
three contributions to the GSFE changes considered here, the thermal
electronic excitation makes the largest e ﬀect on the twinnability of Ni-
Mo solid solution while the thermal expansion and the magnetic tran-
sition both have very limit e ﬀects on it. The stronger e ﬀect of thermal
electronic excitation on the ISF energy compared with those on the USF
and UTF energies of Ni-Mo solid solution is considered to be the main
reason behind. The enhanced twinnability of the Ni-based solid solution
with Mo content below 10at.% suggests the suppressed dislocation slip
during its plastic deformation and the necessity of controlling the ad-
dition of Mo in order to maintain the strength of Ni-based SC super-
alloys at high temperature.
4. Discussions
4.1. The eﬀ ect of magnetic transition on the GSFE
The GSFE results of Ni-Mo solid solutions at high temperature
suggest that the magnetic transition from FM to PM (NM) contributes to
the γ-surface changes, particularly for the unstable planar fault en-
ergies. In order to uncover the mechanisms behind, the magnetic mo-
ments of Ni components at the fault plane are analyzed and compared
with those in the perfect fcc solid solutions. Using the equilibrium vo-
lumes of Ni-Mo solid solutions at 1000 K, the magnetic moments of Ni
components are found to drop sharply with increasing Mo concentra-
tion both in the perfect fcc and faulted lattices ( Supplementary data Fig.
S1). This result is in good agreement with the dramatic drops of mag-
netic moment and Curie temperature in Ni by Mo alloying [58,59],
which also proves the reasonability of treating the Ni-Mo solid solution
as NM state at the temperatures far above T
c. Furthermore, larger
changes in the magnetic moment of Ni caused by the introduction of
planar faults are observed when varying the Mo content from 5at.% to
10at.%. Nevertheless, the magnetic e ﬀects on GSFE are rather weak in
the high-Mo solid solution, owing to their much smaller (even zero)
absolute values of magnetic moments. The higher deviations of mag-
netic moments provided by USF and UTF than that by ISF in Ni-5at.%
Mo are considered to be the main reasons of the stronger magnetic
eﬀects on its unstable planar fault energies.
Fig. 6. Intrinsic stacking fault energies of Ni-Mo solid solutions at 1000 K ( ﬁlled
symbols). The calculation results without the thermal electronic excitation
contribution in ferromagnetic (FM) and nonmagnetic (NM) states are presented
in order to study the magnetic eﬀ ects (half-ﬁlled symbols). Previous theoretical
results at 0 K are also plotted for comparison (open symbols) [30].
Fig. 7. Unstable planar fault energies of Ni-5at.%Mo solid solution at high temperature ( ﬁlled circles): (a) unstable stacking fault energy; (b) unstable twin fault
energy. The calculation results without the thermal electronic excitation contribution in ferromagnetic (FM) and nonmagnetic (NM) states are plotted for comparison
(half-ﬁlled symbols). Previous theoretical results at 0 K are also presented by dash lines [30].
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
145

## Page 7

4.2. The eﬀ ect of thermal electronic excitation on the GSFE
The particularly important role of thermal electronic excitation in
metals is due to their non-zero electronic density at Fermi level. Hence,
the total density of states (DOS) of the perfect and faulted Ni-Mo solid
solutions are compared, in order to explain the di ﬀerent contributions
of thermal electronic excitation to the ISF, USF and UTF energies
against composition. As shown in Supplementary data Table S3, the
total DOSs around Fermi level in the faulted lattices with ISF are higher
than those in the perfect fcc lattices, which suggests the more negative
electronic excitation energies ( F
ele) in the faulted lattices. As a result,
further reductions of ISF energies at high temperature are found in
these solid solutions. Nevertheless, the DOS di ﬀerence between faulted
and perfect lattices decreases with increasing Mo concentration, along
with the evident drops of the DOSs themselves. These results can ex-
plain the weak e ﬀects of electronic excitation on the ISF energies of
high-Mo solid solutions. Contrary results appear in the most cases of
USF and UTF, in which the DOSs around Fermi level are lower in the
faulted lattices instead. These are consistent with the elevated unstable
planar fault energies at high temperature due to the thermal electronic
excitation. The particular case of the UTF energy in Ni-5at.%Mo can be
ascribed to its much larger DOS with UTF than that in the perfect lat-
tice. Moreover, the discrepancies in DOSs between the perfect and
faulted lattices with USF or UTF are smaller than those with ISF, cor-
responding to the stronger e ﬀect of thermal electronic excitation on the
ISF energy.
4.3. Lattice vibration contribution to the ISF energy at high temperature
The slope of the ISF energy in pure Ni at elevated temperature
(dγ
isf/dT) obtained in this work ( −0.032 mJ/(m2·K)) is close to but still
less negative than the experimental result ( −0.04 mJ/(m2·K)), with the
considerations of thermal expansion and thermal electronic excitation.
Consequently, the lattice vibration of the perfect and faulted Ni might
also contribute to the ISF energy drop at high temperature. The lattice
vibration e ﬀect on the ISF energy of pure Ni has been studied in pre-
vious works via phonon calculations but no consistent result is obtained
[27–29]. According to the results in a more recent study, the ISF energy
of pure Ni was considered to decrease from 122 mJ/m
2 at 0 K to
112 mJ/m2 at 1000 K caused by phonon e ﬀect [27]. Due to the larger
supercell, denser k-mesh and the similar lattice constant to that in our
EMTO calculation they used, this reasonable reduction of ISF energy
can be used to correct the ISF energy at high temperature in the present
work (detailed method can be found in Supplementary). Employing the
axial nearest neighbor Ising (ANNI) model [63] and the Debye model
[34], the higher Debye temperatures ( ΘD) of fcc Ni and Ni-Mo than
those with hcp structures ( Supplementary data Table S4) verify the
further drops of their ISF energies at high temperature due to lattice
vibration ( Supplementary data Table S5). However, the reductions in
the ISF energies of Ni-Mo solid solutions at 1000 K diminish with
Fig. 8. Unstable planar fault energies of Ni-Mo solid solutions at 1000 K ( ﬁlled symbols): (a) unstable stacking fault energy; (b) unstable twin fault energy. The
calculation results without the thermal electronic excitation contribution in ferromagnetic (FM) and nonmagnetic (NM) states are plotted for comparison (half- ﬁlled
symbols). Previous theoretical results at 0 K are also presented (open symbols) [30].
Fig. 9. Temperature and composition eﬀ ects on the twinnability measures of Ni-Mo solid solutions ( ﬁlled symbols): (a) the twinnability measures of Ni-5at.%Mo
solid solution at high temperature; (b) the twinnability measures of Ni-Mo solid solutions with di ﬀerent Mo concentrations at 1000 K. The calculation results without
the thermal electronic excitation contribution in ferromagnetic (FM) and nonmagnetic (NM) states are plotted for comparison (half- ﬁlled symbols). Previous the-
oretical results at 0 K are also presented by dash lines (with open symbols) [30].
W. Zhao et al. Computational Materials Science 158 (2019) 140–148
146

## Page 8

increasing Mo concentration. Unfortunately, it is impracticable to
evaluate the lattice vibration contributions to USF and UTF energies via
phonon calculation due to their unstable lattices, thus the lattice vi-
bration e ﬀects on the twinnability of Ni-Mo at ﬁnite temperature are
still to be solved.
5. Conclusions
First-principles alloy theory as implemented in the EMTO-CPA
method and quasiharmonic approximation was employed to predict the
thermo-mechanical properties of Ni-Mo solid solution. The temperature
eﬀects as well as the composition e ﬀects of Mo on the equilibrium
lattice constants, equilibrium bulk modulus and GSFE at ﬁnite tem-
perature are discussed in detail. Besides the enhanced modulus, ani-
sotropy and ductility with Mo alloying at 0 K, the bulk moduli of the Ni-
based solid solutions decrease strongly with increasing temperature.
However, higher Mo concentration causes a lower thermal expansion
coeﬃcient and a reduced temperature e ﬀect for the bulk modulus of the
solid solution, which still results in a positive slope of bulk modulus
against Mo concentration at high temperature. On the other hand, the
ISF, USF and UTF energies of Ni-Mo solid solutions all decrease with
increasing temperature. Less negative slopes of ISF and UTF energies
against Mo concentration are observed at 1000 K, while the variation
trend of USF energy with composition is similar to that at 0 K. As a
consequence, the twinnability of the Ni-based solid solution at high
temperature is only enhanced for lower Mo content. The thermal ex-
pansion, the thermal electronic excitation and the magnetic transition
from FM to PM (NM) all contribute to the GSFE changes at elevated
temperature. The di ﬀerent e ﬀects of these composition-dependent
contributions on the changes of the stable and unstable planar fault
energies are considered to be the main mechanisms. The lattice vibra-
tion at ﬁnite temperature may also a ﬀect the twinnability of Ni-Mo
solid solution at high temperature, which still needs to be solved via the
molecular dynamics simulations of unstable planar fault con ﬁgurations.
The composition-dependent GSFEs of Ni-Mo obtained here o ﬀer a
possibility of ﬁne-tuning the elasticity and twinnability of γ matrix and
improving the creep resistances of Ni-based SC superalloys especially at
intermediate temperature.
CRediT authorship contribution statement
Wenyue Zhao: Conceptualization, Data curation, Formal analysis,
Investigation, Writing - original draft. Wei Li: Conceptualization,
Methodology. Xiaoqing Li: Conceptualization, Data curation.
Shengkai Gong: Funding acquisition, Investigation. Levente Vitos:
Methodology, Software, Writing - review & editing, Funding
acquisition. Zhimei Sun: Funding acquisition, Writing - review &
editing.
Acknowledgements
The ﬁnancial support provided by National Natural Science
Foundation of China (NSFC) under Grant No. U1435207 for carrying
out the present research work are gratefully acknowledged. The
Swedish Research Council (VR), the Swedish Foundation for Strategic
Research (SSF), the Swedish Foundation for International Cooperation
in Research and Higher Education (STINT), the Carl Tryggers
Foundations, the Swedish Governmental Agency for Innovation
Systems (VINNOVA), and the Hungarian Scienti ﬁc Research Fund (re-
search project OTKA 109570) are also acknowledged for ﬁnancial
support. W. Y. Zhao would also like to acknowledge the helpful dis-
cussions with Dr. Zhihua Dong, Royal Institute of Technology (KTH).
Appendix A. Supplementary material
Supplementary data to this article can be found online at https://
doi.org/10.1016/j.commatsci.2018.11.027.
References
[1] R.C. Reed, The Superalloys: Fundamentals and Applications, Cambridge University
Press, Cambridge, 2006 .
[2] Y.Y. Huang, Z.G. Mao, R.D. Noebe, D.N. Seidman, The e ﬀect of refractory elements
on Ni-depletions at γ (f.c.c)/γ′ (L12) interfaces in model Ni-based superalloys: atom-
probe tomographic experiments and ﬁrst-principles calculations, Acta Mater. 121
(2016) 288 –298.
[3] X. Wu, A. Dlouhy, Y.M. Eggeler, E. Spiecker, A. Kostka, C. Somsen, G. Eggeler, On
the nucleation of planar faults during low temperature and high stress creep of
single crystal Ni-base superalloys, Acta Mater. 144 (2018) 642 –655.
[4] M. Pröbstle, S. Neumeier, P. Feldner, R. Rettig, H.E. Helmer, R.F. Singer, M. Göken,
Improved creep strength of nickel-base superalloys by optimized γ/γ' partitioning
behavior of solid solution strengthening elements, Mater. Sci. Eng. A 676 (2016)
411–420.
[5] T.M. Smith, Y. Rao, Y. Wang, M. Ghazisaeidi, M.J. Mills, Di ﬀusion processes during
creep at intermediate temperatures in a Ni-based superalloys, Acta Mater. 141
(2017) 261 –272.
[6] M.A. Meyers, O. Vöhringer, V.A. Lubarda, The onset of twinning in metals: a con-
stitutive description, Acta Mater. 49 (2001) 4025 –4039.
[7] G.B. Viswanathan, R. Shi, A. Genc, V.A. Vorontsov, L. Kovarik, C.M.F. Rae,
M.J. Mills, Segregation at stacking faults within the γ' phase of two Ni-base su-
peralloys following intermediate temperature creep, Scripta Mater. 94 (2015) 5 –8.
[8] C.G. Tian, G.M. Han, C.Y. Cui, X.F. Sun, E ﬀects of stacking fault energy on the creep
behaviors of Ni-base superalloy, Mater. Des. 64 (2014) 316 –323.
[9] R.R. Unocic, N. Zhou, L. Kovarik, C. Shen, Y. Wang, M.J. Mills, Dislocation dec-
orrelation and relationship to deformation microtwins during creep of a γ' pre-
cipitate strengthened Ni-based superalloy, Acta Mater. 59 (2011) 7325 –7339.
[10] X.G. Wang, J.L. Liu, X.F. Sun, Z.Q. Hu, J.H. Do, B.G. Choi, I.S. Kim, C.Y. Jo,
Dislocation motion during high-temperature low-stress creep in Ru-free and Ru-
containing single-crystal superalloys, Mater. Des. 67 (2015) 543 –551.
[11] C.G. Tian, G.M. Han, C.Y. Cui, X.F. Sun, E ﬀects of Co content on tensile properties
and deformation behaviors of Ni-based disk superalloys at di ﬀerent temperatures,
Mater. Des. 88 (2015) 123 –131.
[12] X.G. Wang, J.L. Liu, T. Jin, X.F. Sun, The e ﬀects of ruthenium additions on tensile
deformation mechanisms of single crystal superalloys at di ﬀerent temperatures,
Mater. Des. 63 (2014) 286 –293.
[13] V. Yamakov, D. Wolf, S.R. Phillpot, A.K. Mukherjee, H. Gleiter, Dislocation pro-
cesses in the deformation of nanocrystalline aluminium by molecular-dynamics
simulation, Nat. Mater. 1 (2002) 45 –49.
[14] W.Z.
Han, G.M. Cheng, S.X. Li, S.D. Wu, Z.F. Zhang, Deformation induced micro-
twins and stacking faults in aluminum single crystal, Phys. Rev. Lett. 101 (2008)
115505.
[15] M.W. Chen, E. Ma, K.J. Hemker, H.W. Sheng, Y.M. Wang, X.M. Cheng, Deformation
twinning in nanocrystalline aluminum, Science 300 (2003) 1275 –1277.
[16] M. Jo, Y.M. Koo, B.-J. Lee, B. Johansson, L. Vitos, S.K. Kwon, Theory for plasticity of
face-centered cubic metals, PNAS 111 (2014) 6560 –6565.
[17] X.Z. Wu, R. Wang, S.F. Wang, Q.Y. Wei, Ab initio calculations of generalized-
stacking-fault energy surfaces and surface energies for FCC metals, Appl. Surf. Sci.
256 (2010) 6345 –6349.
[18] R.J. Asaro, S. Suresh, Mechanistic models for the activation volume and rate sen-
sitivity in metals with nanocrystalline grains and nano-scale twins, Acta Mater. 53
(2005) 3369 –3382.
[19] N. Bernstein, E.B. Tadmor, Tight-binding calculations of stacking energies and
twinnability in fcc metals, Phys. Rev. B 69 (2004) 094116 .
[20] S.L. Shang, C.L. Zacherl, H.Z. Fang, Y. Wang, Y. Du, Z.K. Liu, E ﬀects of alloying
element and temperature on the stacking fault energies of dilute Ni-base super-
alloys, J. Phys.: Condens. Matter 24 (2012) 505403 .
[21] K. Kumar, R. Sankarasubramanian, U.V. Waghmare, Tuning planar fault energies of
Ni
3Al with substitutional alloying: ﬁrst-principles description for guiding rational
alloy design, Scripta Mater. 142 (2018) 74 –78.
[22] D.D. Zhao, O.M. Løvvik, K. Marthinsen, Y.J. Li, Combined e ﬀect of Mg and vacancy
on the generalized planar fault energy of Al, J. Alloys Compd. 690 (2017) 841 –850.
[23] L.Y. Tian, R. Lizárraga, H. Larsson, E. Holmström, L. Vitos, A ﬁrst principles study of
the stacking fault energies for fcc Co-based binary alloys, Acta Mater. 136 (2017)
215–223.
[24] M. Chandran, S.K. Sondhi, First-principle calculation of stacking fault energies in Ni
and Ni-Co alloy, J. Appl. Phys. 109 (2011) 103525 .
[25] X.X. Yu, C.Y. Wang, The e ﬀect of alloying elements on the dislocation climbing
velocity in Ni: a ﬁrst-principles study, Acta Mater. 57 (2009) 5914 –5920.
[26] D.J. Siegel, Generalized stacking fault energies, ductilities, and twinnabilities of Ni
and selected Ni alloys, Appl. Phys. Lett. 87 (2005) 121901 .
[27] L.L. Liu, R. Wang, X.Z. Wu, L.Y. Gan, Q.Y. Wei, Temperature e ﬀects on the gen-
eralized planar fault energies and twinnabilities of Al, Ni and Cu: ﬁrst principles
calculations, Comput. Mater. Sci. 88 (2014) 124 –130.
[28] M. Bhogra, U. Ramamurty, U.V. Waghmare, Temperature-dependent stability of
stacking faults in Al, Cu and Ni: ﬁrst-principles analysis, J. Phys.: Condens. Matter
26 (2014) 385402 .
[29] S.L. Shang, W.Y. Wang, Y. Wang, Y. Du, A.D. Patel, Z.K. Liu, Temperature-depen-
dent ideal strength and stacking fault energy of fcc Ni: a ﬁrst-principles study of
shear deformation, J. Phys.: Condens. Matter 24 (2012) 155402 .
[30] W.Y. Zhao, W. Li, Z.M. Sun, S.K. Gong, L. Vitos, Tuning the plasticity of Ni-Mo solid
solution in Ni-based superalloys by ab initio calculations, Mater. Des. 124 (2017)
W. Zhao et al.
Computational Materials Science 158 (2019) 140–148
147

## Page 9

100–107.
[31] F. Birch, Finite elastic strain of cubic crystals, Phys. Rev. 71 (1947) 809 –824.
[32] Y. Wang, Z.K. Liu, L.Q. Chen, Thermodynamic properties of Al, Ni, NiAl, and Ni 3Al
from ﬁrst-principles calculations, Acta Mater. 52 (2004) 2665 –2671.
[33] N.D. Mermin, Thermal properties of the inhomogeneous electron gas, Phys. Rev.
137 (1965) A1441 –A1443.
[34] O.L. Anderson, Equations of State of Solids for Geophysics and Ceramic Science,
Oxford University Press, New York, 1995 .
[35] J. Kollár, L. Vitos, H.L. Skriver, Electronic Structure and Physical Properties of
Solids: the Uses of the LMTO Method, Springer-Verlag, Berlin, 2000 .
[36] L. Vitos, J. Kollár, H.L. Skriver, Full charge-density scheme with a kinetic-energy
correction: application to ground-state properties of the 4d metals, Phys. Rev. B 55
(1997) 13521.
[37] B.L. Gyor ﬀy, Coherent-potential approximation for a nonoverlapping-mu ﬃn-tin-
potential model of random substitutional alloys, Phys. Rev. B 5 (1972) 2382 .
[38] P. Hohenberg, W. Kohn, Density functional theory, Phys. Rev. B 136 (1964)
864–876.
[39] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made
simple, Phys. Rev. Lett. 77 (1996) 3865 .
[40] J. Korringa, On the calculation of the energy of a Bloch wave in a metal, Physica 13
(1947) 392 –400.
[41] W. Kohn, N. Rostoker, Solution of the Schrödinger equation in periodic lattices with
an application to metallic lithium, Phys. Rev. 94 (1954) 1111 .
[42] L. Vitos, Computational Quantum Mechanics for Materials Engineers, Springer-
Verlag, London, 2007 .
[43] P. Soven, Coherent-potential model of substitutional disordered alloys, Phys. Rev.
156 (1967) 809 –813.
[44] X.Q. Li, First-principles study of the third-order elastic constants and related an-
harmonic properties in refractory high-entropy alloys, Acta Mater. 142 (2018)
29–36.
[45] H.B. Luo, C.M. Li, Q.M. Hu, R. Yang, B. Johansson, L. Vitos, Theoretical in-
vestigation of the e ﬀects of composition and atomic disordering on the properties of
Ni
2Mn(Al1-xGax) alloy, Acta Mater. 59 (2011) 971 –980.
[46] S. Lu, R.H. Li, K. Kádas, H.L. Zhang, Y.Z. Tian, S.K. Kwon, K. Kokko, Q.M. Hu,
S. Hertzman, L. Vitos, Stacking fault energies of C-alloyed steels: the e ﬀect of
magnetism, Acta Mater. 122 (2017) 72 –81.
[47] S. Huang, W. Li, S. Lu, F.Y. Tian, J. Shen, E. Holmström, L. Vitos, Temperature
dependent stacking fault energy of FeCrCoNiMn high entropy alloy, Scripta Mater.
108 (2015) 44 –47.
[48] P.A. Korzhavyi, A.V. Ruban, I.A. Abrikosov, H.L. Skriver, Madelung energy for
random metallic alloys in the coherent potential approximation, Phys. Rev. B 51
(1995) 5773 .
[49] A.V. Ruban, H.L. Skriver, Screened Coulomb interactions in metallic alloys. I.
Universal screening in the atomic-sphere approximation, Phys. Rev. B 66 (2002)
024201.
[50] B.L. Györ ﬀy, A.J. Pindor, J. Staunton, G.M. Stocks, H. Winter, A ﬁrst-principles
theory of ferromagnetic phase transitions in metals, J. Phys. F 15 (1985)
1337–1386.
[51] G. Kresse, J. Furthmueller, E ﬃcient iterative schemes for ab initio total-energy
calculations using a plane-wave basis set, Phys. Rev. B 54 (1996) 11169 .
[52] G. Simmons, H. Wang, Single Crystal Elastic Constants and Calculated Aggregate
Properties, MIT Press, Cambridge, MA, 1971 .
[53] T.C. Tiearney Jr., N.J. Grant, Measurement of structural parameters important in
creep of Ni-Mo and Ni-W solid solutions, Metall. Trans. A 13A (1982) 1827 –1836.
[54] F.A. Khan, M.A. Asgar, P. Nordblad, Magnetization and magnetocrystalline aniso-
tropy of Ni-Mo single crystal alloys, J. Magn. Magn. Mater. 174 (1997) 121 –126.
[55] V.S. Babu, A.S. Pavlovic, M.S. Seehra, Rapid loss of magnetic order in Ni on alloying
with Cr, Mo, Re, and Si, J. Appl. Phys. 79 (1996) 5230 –5232.
[56] Z.H. Dong, W. Li, S. Schönecker, S. Lu, D.F. Chen, L. Vitos, Thermal spin ﬂuctuation
eﬀect on the elastic constants of paramagnetic Fe from ﬁrst principles, Phys. Rev. B
92 (2015) 224420 .
[57] Z.H. Dong, W. Li, D.F. Chen, S. Schönecker, M.J. Long, L. Vitos, Longitudinal spin
ﬂuctuation contribution to thermal lattice expansion of paramagnetic Fe, Phys. Rev.
B 95 (2017) 054426 .
[58] Z.H. Dong, S. Schönecker, D.F. Chen, W. Li, M.J. Long, L. Vitos, Elastic properties of
paramagnetic austenitic steel at ﬁnite temperature: longitudinal spin ﬂuctuations in
multicomponent alloys, Phys. Rev. B 96 (2017) 174415 .
[59] A.S. Pavlovic, V.S. Babu, M.S. Seehra, High-temperature thermal expansion of
binary alloys of Ni with Cr, Mo and Re: a comparison with molecular dynamics
simulations, J. Phys.: Condens. Matter 8 (1996) 3139 –3149.
[60] L.E.
Murr, Interfacial Phenomena in Metals and Alloys, Addison-Wesley Educational
Publisher Inc., Boston, 1975 .
[61] D.H. Warner, W.A. Curtin, S. Qu, Rate dependence of crack-tip processes predicts
twinning trends in fcc metals, Nat. Mater. 6 (2007) 876 –881.
[62] E.B. Tadmor, S. Hai, A Peierls criterion for the onset of deformation twinning at a
crack tip, J. Mech. Phys. Sol. 51 (2003) 765 –793.
[63] P.J.H. Denteneer, W. van Haeringen, Stacking-fault energies in semiconductors
from ﬁrst principles calculations, J. Phys. C 20 (1987) 883 –887.
W. Zhao et al.
Computational Materials Science 158 (2019) 140–148
148
