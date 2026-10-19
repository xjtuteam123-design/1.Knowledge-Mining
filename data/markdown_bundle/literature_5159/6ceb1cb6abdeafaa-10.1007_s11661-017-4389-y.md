# 10.1007_s11661-017-4389-y

<!-- source: D:\总文献\10.1007_s11661-017-4389-y.pdf -->
<!-- file_sha256: 6400c503e1d8d55cebd25bc073a5c106e18fff3f829246289bc76880590ccc96 -->

## Page 1

The Compositional Dependence of the
Microstructure and Properties of CMSX-4
Superalloys
HAO YU, WEI XU, and SYBRAND VAN DER ZWAAG
The degradation of creep resistance in Ni-based single-crystal superalloys is essentially ascribed
to their microstructural evolution. Yet there is a lack of work that manages to predict (even
qualitatively) the eﬀect of alloying element concentrations on the rate of microstructural
degradation. In this research, a computational model is presented to connect the rafting kinetics
of Ni superalloys to their chemical composition by combining thermodynamics calculation and
a modiﬁed microstructural model. To simulate the evolution of key microstructural parameters
during creep, the isotropic coarsening rate and c/c¢ misﬁt stress are deﬁned as composition-re-
lated parameters, and the eﬀect of service temperature, time, and applied stress are taken into
consideration. Two commercial superalloys, for which the kinetics of the rafting process are
selected as the reference alloys, and the corresponding microstructural parameters are simulated
and compared with experimental observations reported in the literature. The results conﬁrm
that our physical model not requiring any ﬁtting parameters manages to predict (semiquan-
titatively) the microstructural parameters for diﬀerent service conditions, as well as the eﬀects of
alloying element concentrations. The model can contribute to the computational design of new
Ni-based superalloys.
DOI: 10.1007/s11661-017-4389-y
/C211 The Author(s) 2017. This article is an open access publication
I. INTRODUCTION
THE outstanding high-temperature mechanical per-
formance of Ni-based single-crystal superalloys, in
particular, their superior creep resistance, makes them
favorite materials for turbine blades in aero engines. [1]
Their interesting properties are largely dictated by the
high volume fraction (up to 70 pct) of ordered, L1 2
structured c¢ precipitates, which are coherently embed-
ded in a solid-solution-strengthened c matrix (fcc
structure). During the high-temperature creep process
above 900 /C176 C, the creep behavior strongly depends on
the microstructural evolution. Speciﬁcally, in the early
creep stage of so-called negative misﬁtting alloys,
initially adjacent cuboidal c¢ particles coalesce and turn
into platelike structures, which are normal to the stress
direction. This microstructure of alternating platelets of
c and c¢ phases is called the rafted structure. The
lamellar structure is rather stable and essentially blocks
the dislocation bypassing mechanism, resulting in a low
creep rate during the secondary creep stage. In the later
stage of creep, the destabilization of the rafted
microstructure occurs through a topological inversion
of c/c¢ microstructure, resulting in a steep increase in the
creep rate. Hence, the creep kinetics can be linked to the
process of microstructural evolution, and it is of great
importance to identify the main microstructural evolu-
tion mechanisms and to incorporate their eﬀects as a
function of service conditions.
The characterization of microstructural evolution
during the creep process is of utmost importance in
detecting the desirable mechanical properties of Ni
single-crystalline superalloys. Hence, since the 1990s, a
large number of models have been derived to describe
and investigate the progress of c¢ morphology evolution.
Most of them focus on the dynamics of dislocation
behavior, exploring the balance between dislocation
multiplication and interaction with precipitates, as well
as dislocation annihilation and recovery. [2–6] Other
models focus on probing the driving force of the
anisotropic coarsening of precipitates. [7–10] Essentially,
the microstructural characteristics for Ni superalloys are
determined by three factors: c¢ precipitate volume
fraction, isotropic coarsening, and directional coarsen-
ing, also called rafting. There are two main parameters
in describing the rafted microstructure, i.e., the
HAO YU and SYBRAND VAN DER ZWAAG are with the Novel
Aerospace Materials Group, Faculty of Aerospace Engineering, Delft
University of Technology, 2629 HS Delft, The Netherlands. WEI XU
is with the Novel Aerospace Materials Group, Faculty of Aerospace
Engineering, Delft University of Technology, and also with the State
Key Laboratory of Rolling and Automation, Northeastern University,
Shenyang 110819, China. Contact e-mail: xuwei@ral.neu.edu.cn
Manuscript submitted July 10, 2017.
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 2

microstructural periodicity k and the c channel width x.
The k parameter characterizes the global coarsening of
the c/c¢ microstructure, since the rafted c/c¢ composite
morphology is found to be almost independent of the
initial microstructure. The widening of the c channel
width, which is perpendicular to the uniaxial applied
stress, is also an important process in presenting creep
kinetics during microstructural evolution, since the
channel width determines the dislocation motion due
to the Orowan mechanism and their accumulation. The
c channel widening is driven by the superimposition of
internal misﬁt stress and the uniaxial applied stress,
which can signiﬁcantly aﬀect the kinetics of the
anisotropic coarsening mechanism.
As mentioned previously, the creep kinetics are
linked to the process of microstructural evolution,
which is not only a function of the imposed loading
conditions but also of the chemical composition of the
superalloy. However, there are only a few studies that
attempt to show the eﬀect of alloying element concen-
trations on microstructural evolution
[11–13] because of
the large number of potential interactions between the
alloying elements and the complex dependences on
service temperature, time, and applied stress that need
to be evaluated. Theoretical analyses and computer
modeling tools might conceivably provide a qualitative
or semiquantitative method to solve this problem.
[14,15]
In the present article, the Ni single-crystal commercial
grades CMSX-4 and Rene ´ N4 are selected as the
reference alloys, since their microstructural parameters
and creep behavior during diﬀerent creep tests have
been reported in quite some detail. [1,16–19] A novel
computational design model p redicting the microstruc-
tural development during the creep process is presented
in which thermodynamic data are combined with an
energy-based microstructural evolution model. The
microstructural features a re computationally linked
to the chemical composition, and the simulated results
are validated against experimental observations.
Speciﬁcally, the conditions considered in this work
correspond to the coalescence of cubic c¢ precipitates at
elevated service temperatures (above 1173 K, 900 /C176 C),
leading to the lamellar structure under uniaxial h001i
tensile loading. Other load ing conditions (uniaxial
compression, multiaxial stress, cyclic loading, etc.)
are outside the scope of this work.
II. MODEL DESCRIPTION
In this section, a model that combines thermodynamic
calculations with two representative methods that
describe the microstructural evolution of CMSX-4 and
Rene´N4 superalloys is presented. The eﬀects of chem-
ical compositions are introduced and the corresponding
microstructural parameters can be predicted as a func-
tion of stress and temperature. For the relatively limited
composition domain explored in this work, the compo-
sition dependence of dislocation behavior is ignored.
The nominal chemical compositions of commercial
superalloy CMSX-4 and Rene´N4 are shown in Table I.
A. Fedelich’s Phenomenological Model
Recently, Fedelich et al .
[20] measured the increase in
the microstructural periodicity k and the c channel width
x of CMSX-4 commercial superalloys as a function of
service time, temperature, and applied stress. An ana-
lytical expression was proposed, which seems to capture
the ﬁndings from detailed observations on the transition
of c¢ morphology from cuboid to rafted shape. In their
work, the processes of isotropic coarsening and unidi-
rectional coarsening, i.e., rafting, are considered sepa-
rately and are assumed to be governed by diﬀerent
driving mechanisms. Based on geometrical considera-
tions, the channel width in the two diﬀerent procedures
is given by
x
cubeðtÞ¼ 1 /C0
ﬃﬃﬃﬃ ﬃ
fc03
p/C16/C17
kðtÞ½ 1/C138
xraftðtÞ¼ 1 /C0 fc0
/C0/C1
kðtÞ; ½2/C138
where fc¢ is the volume fraction of precipitates and k(t)
is the microstructural periodicity. The isotropic coars-
ening of k(t) was captured by the ﬁtted equation used
for specimens crept at 1223 K (950 /C176 C):
kðtÞ¼ k0
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
1 þ bt
p
: ½3/C138
A dimensionless parameter, termed rafting degree n,i s
deﬁned to quantify the microstructural changes. It pre-
sents the normalized channel width, which increases
from 0 to 1 when the microstructure changes from
cubes to plates:
n ¼
xðtÞ/C0 xcubeðtÞ
xraftðtÞ/C0 xcubeðtÞ : ½4/C138
The analytical expression to describe the degree of
rafting as a function of time and external stress based
on experimental results is given by
n ¼ 1 /C0 expð/C0 br
ntÞ: ½5/C138
Fundamentally, the aforementioned model is an exper-
imentally based analytical expression, which can be
applied only for CMSX-4 alloy at the temperature
1223 K (950 /C176 C), where b, b, and n are all ﬁtting
parameters not having any physical meaning. To
extend the application scope of this model over a
wider temperature range, Fedelich et al .[21] further col-
lected the microstructural evolution data of CMSX-4
over a wide temperature range and built the following
equation to describe the kinetics of evolving periodicity
and channel width:
k
001½/C138 ¼ k0
½001/C138 1 þ D0exp /C0 Qk
RT
/C18/C19
t
/C20/C21 a
½6/C138
x½001/C138 ¼ xcube þ xraft /C0 xcubeðÞ
/C2 1 /C0 exp /C0 A0exp /C0 Qn
RT
/C18/C19
1 þ r
r0
/C18/C19 p
t
/C20/C21/C26/C27
:
½7/C138
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 3

In these two equations, D0, Qk, a, A0, Qn, r0,a n d p are
also ﬁtting parameters. This modiﬁed equation excel-
lently describes the microstructural degradation of
CMSX-4 at diﬀerent stress and temperature levels with
the correlation factors r
2 > 0.97. However, all the
parameter values in the equation remain ﬁtted values,
which means for other superalloy systems with slightly
diﬀerent chemical compositions, the applicability of the
model should be reassessed and the parameter values
need to be redetermined.
B. Fan’s Model
Fan et al .
[22] follow the approach of Fedelich et al .’s
work[20] in describing the channel width and rafting
degree but attempt to bring in a more physical
approach. They describe the isotropic coarsening of
the microstructural periodicity, as follows:
kðtÞ3 /C0 k3
0 ¼ BQ
RT t: ½8/C138
In this equation, B is a material constant and Q is the
activation energy. One could argue that the Oswald
ripening mechanism describes the coarsening of spher-
ical particles, while the actual microstructure in the
superalloys considered is a lamellar structure. However,
it would be reasonable to simplify the coarsening
kinetics of lamellar structures in the same way since,
essentially, it is the overall interfacial energy that drives
the coarsening mechanism. Recent studies
[23,24] also
show that the isotropic coarsening rate, as in the LSW
coarsening mechanism, can be applied as an indicator of
creep properties in Ni superalloys. In this model, the
isotropic coarsening rate is proportional to temperature
and determined by two constants, while no formal
connection to the chemical composition is assumed.
According to Fan’s study, in the directional coarsen-
ing process, c¢ precipitates only change their shape from
cubes to rafts while the precipitate volume remains
constant, since the change of c¢ volume was included in
the isotropic coarsening. The driving force for rafting is
the strain energy w, which equals the distortion strain
energy since the volumetric strain energy is zero. The
strain energy during rafting is formulated as
w ¼ t
d ¼ð 1 /C0 cnÞ 1 þ t
3E r2
s ; ½9/C138
where td is the distortion strain energy, E is the elastic
modulus, t is the Poisson ratio, and rs is the largest
Mises stress in three types of channels. From a ther-
modynamics perspective, the driving force for rafting
is the partial derivative of the strain energy to the
degree of rafting:
F ¼/C0
@w
@n ¼ c 1 þ t
3E r2
s : ½10/C138
In the case of a uniaxial applied tensile stress in one of
the three principal h001i directions,
rs ¼ r0 þð 1 þ aÞrijj : ½11/C138
This direction was selected since it leads to the highest
von Mises stress value, which was taken to be the
superimposition of extrinsic applied stress r0 and
intrinsic lattice misﬁt stress ri, and ri was set as a con-
stant value 300 MPa for CMSX-4 superalloy. Simi-
larly, the evolution of the rafting degree n is related to
the actual morphology, the driving force, and the tem-
perature. Hence, the channel width during rafting can
be predicted with the following equation:
xðtÞ¼ x
cubeðtÞþ½ xraftðtÞ/C0 xcubeðtÞ/C138
/C2 1 /C0 exp /C0 Arn
s exp /C0 Q
RT
/C18/C19
t
/C20/C21/C26/C27
: ½12/C138
In this model, the microstructural parameter c channel
width now is presented as a function of time, temper-
ature, and stress. In contrast to Fedelich’s work, every
parameter in this equation has a clear physical meaning.
C. Composition-Dependent Microstructural Model
In this work, we also assume that the growth of
microstructural periodicity follows the LSW theory but
redeﬁne the isotropic coarsening rate to present the proper
eﬀect of temperature. The is otropic coarsening rate of
microstructural periodicity is shown in this equation:
kðtÞ3 /C0 k3
0 ¼ Kt; ½13/C138
where t is the creep time. This equation resembles
Eq. [ 8], but in contrast to the formulation of Eq. [ 8],
our deﬁnition of K allows for making a connecting to
the equilibrium chemical composition of both the
matrix and the precipitate as well as the diﬀusivities of
the alloying elements. Based on earlier work,
[25–28] the
rate constant for the isotropic coarsening rate of pre-
cipitates is given by the following equation:
K ¼ 8cV
p
m
,Xn
i¼1
9 xp
i /C0 xmp
iðÞ 2
xmp
i Di=RT ½14/C138
in which Vm
p is the molar volume of precipitate, x is the
equilibrium interface mole fraction of the c¢ forming
elements on both the matrix ( m) and precipitate ( p)
sides, T is the service temperature, and D is the
corresponding diﬀusion coeﬃcient. In the calculations,
the interfacial energy is arbitrarily set at a ﬁxed value of
Table I. Nominal Chemical Compositions of Commercial Superalloys CMSX-4 and Rene ´N4 (Weight Percent)
Al Co Cr W Mo Ta Ti Re
CMSX-4 5.6 9.0 6.5 6.0 0.6 6.5 1.0 3.0
Rene´N4 3.7 8.0 9.0 6.0 2.0 4.0 4.2 —
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 4

0.3 J/m 2 irrespective of the precipitate size and the
actual composition of precipitate and matrix. [29] This is
a slight simpliﬁcation but helps in illustrating the eﬀect
of alloy and particle composition on precipitate coars-
ening. All thermodynamic parameter values, including
x
i
p, xi
mp, Di,a n d Vm
p , required during the calculations
were calculated via Thermo-Calc using the latest TCNI8
and MobNI4 databases.
In addition to the coarsening rate, the misﬁt stress
induced by the mismatch of lattice parameter and
elasticity coeﬃcient is also treated as a composition-de-
pendent parameter. In this work, the lattice misﬁt stress
is deﬁned as r
i which is taken as the product of the
Young’s modulus and the lattice misﬁt strain, as shown
in Eq. [ 15]
r
d ¼ Edjj ½15/C138
d ¼ 2 ac0 /C0 ac
/C0/C1
ac0 þ ac
: ½16/C138
The lattice misﬁt stress is determined by the element
concentration in c/c¢ phases as well as the thermal
expansion coeﬃcients of both phases. In fact, apart
from the internal stress induced by lattice misﬁt, the
elastic misﬁt between the c/c¢ phase contributes to
internal stress as well. Dye et al .’s research
[30] revealed
that at temperatures above 1173 K (900 /C176 C), the diﬀer-
ences in the elastic moduli between c/c¢ phases in a
CMSX-4 superalloy are within 5 pct. Therefore, in our
work, the internal stress is simpliﬁed as the lattice misﬁt
stress only.
The evolution of channel width in CMSX-4 superal-
loy during rafting is presented in the following equation:
xðtÞ¼ x
cubeðtÞþ½ xraftðtÞ/C0 xcubeðtÞ/C138
/C2 1 /C0 exp /C0 Arn
s exp /C0 Q
RT
/C18/C19
t
/C20/C21/C26/C27
:
½17/C138
As mentioned previously, the lattice misﬁt between the
c/c¢ phase is, on the one hand, governed by the chemi-
cal composition of the phases at the relevant tempera-
ture via Vegard’s law and, on the other hand, by the
thermal expansion coeﬃcients of both phases. In this
article, the calculation of lattice misﬁt follows the
method from Rettig et al .[14] The misﬁt is determined
by Eqs. [ 18] through [ 21], which concern element con-
centrations of the respective phases at the required
temperature.
aRT
c ¼ 3:524 þ 0:0196xc
Co þ 0:110xc
Cr þ 0:478xc
Mo
þ 0:444xc
W þ 0:441xc
Re þ 0:3125xc
Ru þ 0:179xc
Al
þ 0:422xc
Ti þ 0:7xc
Ta
½18/C138
aRT
c0 ¼ 3:57 /C0 0:004xc0
Cr þ 0:208xc0
Mo þ 0:194xc0
W
þ 0:262xc0
Re þ 0:1335xc0
Ru þ 0:258xc0
Ti þ 0:5xc0
Ta
½19/C138
and
ac ¼ aRT
c þ 5:741 /C2 10/C0 5T /C0 1:01 /C2 10/C0 9T2 ½20/C138
ac0 ¼ aRT
c0 þ 6:162 /C2 10/C0 5T /C0 1:132 /C2 10/C0 8T2: ½21/C138
The element concentrations of c/c¢ phases can be directly
obtained from CALPHAD calculation and the simu-
lated lattice misﬁt. In the absence of better data and
reliable ab-initio calculations, the empirical Eqs. [ 18]
through [ 21] are used to calculate the lattice misﬁts.
Since the predictions of this model rely on the
accuracy of the underlying database (as all thermody-
namic calculations), we checked the validity of the
database used in predicting the characteristics of Ni
superalloys. Disagreements between experimental
results and simulated volume fractions and chemical
compositions of c/c¢ phases have been reported when use
was made of the formal TCNI databases,
[31,32] but
recent publications have validated the reliability of the
current databases TCNI8.
[33,34] Modest deviations
between the actual experimental data topologi-
cally-closed-packed (TCP) phases and the recalculated
values on the basis of the database are reported in
Reference 35. Hence, the results of the thermodynamic
calculations for TCP phases should be considered as
indicative.
III. RESULTS
Figure 1 shows the simulated channel width of
commercial alloys CMSX-4 and Rene ´ N4 obtained
from our model and the comparison with the experi-
mental data at diﬀerent temperatures and applied stress
levels. The solid lines are the simulation results obtained
from our model, while the dashed lines are the results
from Fedelich’s analytical expression (Eq. [ 7]). It turns
out in Figure 1(a) that at 1123 K (850 /C176 C), at the lowest
stress level, a misﬁt exists between our predictions and
the experimental data. However, at high stress levels,
our model perfectly reproduces the experimental results
and even outperforms Fedelich’s analytical expression.
Figure 1(b) shows that at a service temperature of
1223 K (950 /C176 C), a good agreement in the kinetics is
obtained for the high stress 240 MPa, while at lower
stresses, the kinetics of the channel widening process are
slightly overestimated. From Figure 1(c), it can be
deduced that our model predictions ﬁt quite well with
Eggeler’s experimental data obtained at 1323 K
(1050 /C176 C).
[36] The results in Figure 1(d) show that at
1373 K (1100 /C176 C), the channel characteristics are also
slightly overestimated by our simulation, but the
Fig. 1—Comparison of the calculated channel width of CMSX-4
superalloy with the experimental data from Fedelich and Eggeler at
the temperature of 1123 K (850 /C176 C) (a), 1223 K (950 /C176 C) (b), 1323 K
(1050 /C176 C) (c), and 1373 K (1100 /C176 C) (d); and the comparison of
Rene´N4 microstructural parameters at 1144 K (871 /C176 C) and 1255 K
(982 /C176 C) (e) (Color ﬁgure online).
c
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 5

METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 6

tendency of convergence is well predicted. To validate
our model for other compositions than that of CMSX-4,
the evolution of c channel width in Ni commercial
grades Rene´N4, as reported by Shastry et al .,[19] was
employed, and the comparison with simulation results is
shown in Figure 1(e). At a temperature of 1144 K
(871 /C176 C), the predictions are rather lower than the
experimental observation, while at a higher temperature
of 1255 K (982 /C176 C), the prediction suits the experimen-
tal results perfectly. It is necessary to point out that for
our model, which has no ﬁtting parameter in the
calculation at all and only uses independently derived
physical parameter values, the agreement of the predic-
tions at diverse levels of temperature, stress, and
diﬀerent compositions is remarkable. As such, it is one
of the ﬁrst models that manages to couple the
microstructural characteristics of the rafting process
with the chemical composition-based thermodynamic
calculation in Ni superalloys.
A. Effect of Alloying Element on Microstructure and
Creep Properties
For Ni superalloys, the microstructural features and
their evolution during creep are intrinsically determined
by the type and concentration of the various alloying
elements. For example, Al and Ta are the main c¢
forming elements and higher levels of these elements can
eﬀectively increase the c¢ volume fraction.
[37] Mo and Co
partition preferentially in c matrix and play as strong
solid-solution-strengthening elements to elevate the
creep properties,
[38–40] while Co addition helps to reduce
the tendency to form TCP phases. [41,42] Cr was found to
increase the c¢ volume fraction [38] but deteriorates the
microstructural stability at high level of concentra-
tion.[43] Re addition can substantially lower the c¢
coarsening kinetics and helps to bring about large
negative misﬁts, but also increases the tendency to form
Rerich TCP phases.
[44,45] Ru can eﬀectively stabilize the
microstructure by suppressing the precipitation of TCP
phases.[34,46]
We now attempt to predict the eﬀect of the concen-
tration of speciﬁc alloying elements on the microstruc-
ture and rafting kinetics, taking the base composition of
CMSX-4 superalloy as the starting point. The change in
alloy composition is obtained at the expense of varying
Ni concentration. The service temperature, total time,
and applied stress are set as 1273 K (1000 /C176 C),
200 hours, and 100 MPa, respectively, and the predicted
trends are compared with the experimental observations
reported in the literature. All alloying concentrations are
given in weight percent.
1. Cr effect
The predicted eﬀects of Cr on the microstructural
parameters and c¢ coarsening rate are shown in
Figure 2. The calculation results show that as the Cr
concentration incre ases, the value of c channel width
varies but the changes are minor. The c¢ coarsening rate
decreases slightly when the Cr levels increase from 2 to
10 pct, and the decrease becomes sharper as Cr
increases from 10 to 14 pct. The c¢ volume fraction
decreases slowly but continuously with the Cr level.
When the Cr level reaches 11 pct, the TCP phases,
including the l and r phases, are predicted to start to
precipitate.
Fig. 2—Eﬀect of Cr on the c channel width, c¢ volume fraction, and c¢ coarsening rate. The dashed region marks the formation of undesirable
phases (Color ﬁgure online).
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 7

The predicted inﬂuence of the Cr level on the volume
fraction is in good agreement with the experimental
observations by Mackay et al .[40] and Huo et al .,[13]
which showed that Cr helps to develop the c¢ volume
fraction in Ni superalloy. Huo et al .’s data also indicate
that a Cr addition contributes to narrowing the c
channel width, which also agrees well with the predic-
tions. Carroll et al .’s
[37] and Chen et al .’s[47] investiga-
tions show that an increasing Cr level helps to improve
the creep strength of Ni superalloys. This result can be
explained by the eﬀect of Cr on decreasing c¢ coarsening
rate, as shown in this ﬁgure. Besides, it also has been
reported
[12,13] that high Cr levels can deteriorate the
microstructural stability by increasing the proneness to
TCP phase formation, in accordance with the simulation
results reﬂected by the pink dots. In this ﬁgure, the
backward slash patterns deﬁne areas where undesirable
phases precipitate. From the simulations presented in
Figure 2 and assuming the thermodynamic database to
be suﬃciently validated and correct (refer to the validity
comment at the end of the model introduction section),
it can be concluded that the Cr level can be increased in
the base CMSX-4 alloy, to further retard the coarsening
rate without the occurrence of TCP phase formation.
2. Co effect
As shown in Figure 3, a rise in Co level from 0 to
16 wt pct brings a continuous increase in c channel
width and a continuous drop in c¢ volume fraction from
71 to 48 pct, while the c¢ coarsening rate decreases
simultaneously. Over the entire Co concentration range,
no signs of the existence of TCP phases are found, which
agrees well with the experimental investigations
[43]
showing that Co addition helps to suppress the forma-
tion of TCP phases.
The predicted eﬀect of Co on decreasing the c¢
volume fraction ﬁts well with MacKay’s investiga-
tion.[40,48] In contrast, Huo et al .’s[13] experimental
results show that an 8 wt pct addition of Co can
slightly reduce the c¢ volume fraction to 3 pct. This
mismatch reﬂects the complex eﬀect of Co on c¢
precipitation, which can be ascribed to the eﬀect of
Co on altering the c/c¢ partitioning behavior of other
alloying elements.
[49]
3. Ta effect
The eﬀect of Ta on the microstructural parameters
of c/c¢ phases is shown in Figure 4. The calculated
results show that if the Ta concentration increases
from 4 to 12 pct, the value of c channel width is
almost halved, while the c¢ volume fraction increases
continuously from 39 to 60 pct and the c¢ coarsening
rate has a sustained decrease. The simulated results
agree well with Jena’s experimental investigations,
showing that Ta promotes c¢ formation as a c¢
former,
[50] and Forde’s study showing that Ta addi-
tion helps to retard diﬀusion-mediated processes in
Ni-based systems. [51] When the Ta content reaches
8.1 pct, Cr-enriched r phase begins to precipitate, as
shown by pink dots and the area marked by the slash
pattern. It has been demonstrated by Karunaratne
et al .’s experimental results that the Ta addition
increases the susceptibility to TCP formation by
concentrating the c-partitioning TCP-forming ele-
ments in the c phase[52]; Speciﬁcally, Booth-Morrison
et al .’s study shows that Ta increases the partitioning
ratio for Cr by displacing Cr atoms from the c¢
phase, [53] in this way promoting TCP formation. The
reported experimental observations are well predicted
by the model presented here.
Fig. 3—Eﬀect of Co on the c channel width, c¢ volume fraction, and c¢ coarsening rate (Color ﬁgure online).
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 8

4. Mo effect
Figure 5 shows that the c channel width drops from
0.45 to 0.3 lm as the Mo concentration increases from 0
to 2.5 wt pct. After that, the channel width experiences
a slow increase and then keeps decreasing with a further
increase in Mo concentration. Besides, the ﬁgure shows
Fig. 4—Eﬀect of Ta on the c channel width, c¢ volume fraction, and c¢ coarsening rate. The dashed region marks the formation of undesirable
phases (Color ﬁgure online).
Fig. 5—Eﬀect of Mo on the c channel width, c¢ volume fraction, and c¢ coarsening rate. The dashed region marks the formation of undesirable
phases (Color ﬁgure online).
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 9

that Mo additions can slightly increase the volume
fraction of c¢ precipitates and reduce the c¢ coarsening
rate by a factor 8 when the Mo concentration rises from
0 to 5 pct. However, the undesirable l phase begins to
precipitate and grow rapidly for Mo concentrations in
excess of 1.7 pct. The simulation results for the c
channel width and c¢ volume fraction ﬁt well with Huo
et al .’s data,
[13] which showed that 1.5 pct addition of
Mo can slightly increase the precipitation volume
fraction and decrease the c channel width. Moreover,
Biss and Sponseller’s experimental results
[54] showing
that Mo addition can retard the coarsening rate of c¢
particles also agree well with the calculated results. The
role of Mo as a strong TCP former has been investigated
experimentally by many researchers, [11,12] and their
results conﬁrm the simulation results that an elevated
level of Mo promotes the formation of the detrimental l
phase. The forbidden area with the presence of l phase
is marked by a backward slash pattern. It is also worth
mentioning here that the model predictions suggest that
there still exists some space to increase the Mo concen-
tration in the base CMSX-4 alloy, as it leads to a higher
precipitation volume fraction and a lower coarsening
rate while the TCP phases should remain absent.
5. Re effect
Finally, Figure 6 shows that according to the simu-
lations based on the existing data in the TCNI8 and
MobNI4 thermodynamic databases, Re additions can
slightly decrease the c channel width, while the c¢ volume
fraction remains more or less unchanged. The blue dots
indicate that the coarsening rate of c¢ precipitates
experiences a slow decrease when the Re level increases
from 1 to 5 pct. Besides, TCP phases are predicted not
to form over the entire concentration range of Re from 1
to 5 pct. According to the experimental results by Heckl
et al .,
[44] a 2 at. pct Re addition can signiﬁcantly reduce
the c¢ volume fraction to 15 pct. Besides, the eﬀect of Re
on the coarsening rate of c¢ has also been investigated
extensively. The conclusions are quite consistent and
indicate that Re addition in Ni superalloys can eﬀec-
tively retard the c¢ coarsening rates,
[55,56] due to the fact
that Re is the slowest diﬀusing element in Ni among all
alloy elements. [57,58] The calculated results are in qual-
itative agreement with the reported eﬀect of Re, but the
high eﬃciency of Re in lowering the coarsening rate as
well as decreasing the c¢ volume fraction is quantita-
tively not captured very well. It might be that the data in
the thermodynamic databases TCNI8 and MobNI4
regarding the impact of the element Re need some
adjustment.
To sum, our model can semiquantitatively predict the
eﬀect of chemical composition of Ni-based superalloys
on c channel width at a relatively high temperature and
low stress range on the basis of hard physical data
rather than empirical ﬁtted parameter values, which
reﬂects the power of the model in simulating the
microstructural evolutions during the rafting process.
The eﬀect of alloying elements Cr, Co, Ta, Mo, and Re
in CMSX-4 superalloy on the microstructural parame-
ters, c¢ coarsening rates, and microstructural stability
are calculated by this model, and the simulated results
have qualitatively good agreement with the experimen-
tal results from the literature. Moreover, our calculation
Fig. 6—Eﬀect of Re on the c channel width, c¢ volume fraction, and c¢ coarsening rate (Color ﬁgure online).
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 10

shows that the chemical composition of CMSX-4
superalloy has not reached the optimal values from a
thermomechanical stability perspective. There still exists
some space to increase the alloying levels of Cr, Ta, and
Mo to further improve the precipitation strengthening
while maintaining the microstructural stability of the
matrix.
IV. CONCLUSIONS
1. A novel computational model for the microstruc-
tural stability of Ni-based single-crystal superalloys
as a function of temperature and applied tensile
stress was built by combining thermodynamics
calculations and an energy-based microstructural
model. The connection between chemical composi-
tions and the rate of microstructural evolution is
based on the isotropic coarsening of c¢ phase and c/
c¢ lattice misfit during creep.
2. The model was applied to predict the c channel
widening of Ni commercial grades of CMSX-4. The
microstructural characteristics of the rafting pro-
cess, especially at elevated temperature, can be well
simulated by the model.
3. The effect of alloying elements Cr, Co, Mo, and
Re on the microstructural parameters, c¢ coarsen-
ing rates, and microstructural stability in CMSX-4
superalloy were analyzed by this model. The
simulated results are well confirmed by the
reported experimental data. The calculated results
show that from a thermomechanical stability
point of view, the chemical composition of the
CMSX-4 superalloy has not reached its optimal
value. There still exists some space to increase the
alloying level of Cr, Ta, and Mo, to further
improve the precipitation strengthening while
maintaining the microstructural stability of the
matrix.
ACKNOWLEDGMENTS
This work was carried out with ﬁnancial support
from the Chinese Scholarship Council (CSC) as well as
TU Delft internal funding. The authors thank Dr.
Bernard Fedelich, Federal Institute for Materials Re-
search and Testing (BAM), for helpful discussions dur-
ing the early stages of the preparation of the
manuscript.
OPEN ACCESS
This article is distributed under the terms of the
Creative Commons Attribution 4.0 International Li-
cense ( http://creativecommons.org/licenses/by/4.0/),
which permits unrestricted use, distribution, and re-
production in any medium, provided you give appro-
priate credit to the original author(s) and the source,
provide a link to the Creative Commons license, and
indicate if changes were made.
REFERENCES
1. R.C. Reed: The Superalloys: Fundamentals and Applications ,
Cambridge University Press, Cambridge, United Kingdom, 2008.
2. Z. Zhu, H. Basoalto, N. Warnken, and R.C. Reed: Acta Mater. ,
2012, vol. 60, pp. 4888–4900.
3. S. Gao, M. Fivel, A. Ma, and A. Hartmaier: J. Mech. Phys. Solids ,
2017, vol. 102, pp. 209–23.
4. V.A. Vorontsov, R.E. Voskoboinikov, and C.M.F. Rae: Advanced
Materials Research , Trans Tech Publications, Aedermannsdorf,
2011, pp. 150–55.
5. M. Cottura, B. Appolaire, A. Finel, and Y. Le Bouar: J. Mech.
Phys. Solids , 2016, vol. 94, pp. 473–89.
6. Y.S. Choi, T.A. Parthasarathy, C. Woodward, D.M. Dimiduk,
and M.D. Uchic: Metall. Mater. Trans. A , 2012, vol. 43A,
pp. 1861–69.
7. F.R.N. Nabarro, C.M. Cress, and P. Kotschy: Acta Mater., 1996,
vol. 44, pp. 3189–98.
8. T. Ohashi, K. Hidaka, and S. Imano: Acta Mater. , 1997, vol. 45,
pp. 1801–10.
9. J.C. Chang and S.M. Allen: J. Mater. Res. , 1991, vol. 6,
pp. 1843–55.
10. W.-P. Wu, Y.-F. Guo, G.-S. Dui, and Y.-S. Wang: Comput.
Mater. Sci. , 2008, vol. 44, pp. 259–64.
11. X.G. Liu, L. Wang, L.H. Lou, and J. Zhang: J. Mater. Sci.
Technol., 2015, vol. 31, pp. 143–47.
12. B. Wang, J. Zhang, T. Huang, S. Haijun, Z. Li, L. Liu, and F.
Hengzhi: J. Mater. Res. , 2016, vol. 31, pp. 3381–89.
13. J.J. Huo, Q.Y. Shi, and Q. Feng: Mater. Sci. Eng. A , 2017,
vol. 693, pp. 136–44.
14. R. Rettig, N.C. Ritter, H.E. Helmer, S. Neumeier, and R.F.
Singer: Model. Simul. Mater. Sci. , 2015, vol. 23, p. 035004.
15. R.C. Reed, T. Tao, and N. Warnken: Acta Mater. , 2009, vol. 57,
pp. 5898–5913.
16. A. Epishin, T. Link, H. Klingelho ¨ﬀer, B. Fedelich, U. Bru ¨ckner,
and P.D. Portella: Mater. Sci. Eng. A , 2009, vol. 510, pp. 262–65.
17. A. Scholz, Y. Wang, S. Linn, C. Berger, and R. Znajda: Mater.
Sci. Eng. A , 2009, vol. 510, pp. 278–83.
18. A. Epishin, T. Link, M. Nazmy, M. Staubli, H. Klingelhoﬀer, and
G. Nolze: Superalloys, 2008, pp. 725–31.
19. C. Girish Shastry, V. Sivakumar, G. Kelekanjeri, T. Vishwanath,
and S. Chaudhuri: Mater. Sci. Eng. A , 2013, vol. 585, pp. 47–56.
20. B. Fedelich, G. Ku ¨necke, A. Epishin, T. Link, and P. Portella:
Mater. Sci. Eng. A , 2009, vols. 510–511, pp. 273–77.
21. B. Fedelich, A. Epishin, T. Link, H. Klingelho ¨ﬀer, G. Ku¨necke,
and P.D. Portella: Superalloys 2012, TMS, Warrendale, PA, 2012,
pp. 491–500.
22. Y.-N. Fan, H.-J. Shi, and W.-H. Qiu: Mater. Sci. Eng. A , 2015,
vol. 644, pp. 225–33.
23. J. Gong, D. Snyder, T. Kozmel, C. Kern, J.E. Saal, I. Berglund, J.
Sebastian, and G. Olson: JOM, 2017, vol. 69, pp. 880–85.
24. C. Ai, X. Zhao, J. Zhou, H. Zhang, L. Liu, Y. Pei, S. Li, and S.
Gong: J. Alloys Compd. , 2015, vol. 632, pp. 558–62.
25. Q. Lu, W. Xu, and S. van der Zwaag: Philos. Mag., 2013, vol. 93,
pp. 3391–3412.
26. Q. Lu, W. Xu, and S. van der Zwaag: Comput. Mater. Sci. , 2014,
vol. 84, pp. 198–205.
27. Q. Lu, W. Xu, and S. van der Zwaag: Acta Mater. , 2014, vol. 77,
pp. 310–23.
28. Q. Lu, W. Xu, and S. van der Zwaag: Acta Mater. , 2014, vol. 64,
pp. 133–43.
29. X. Yang, W. Hu, and X. Zhang: Appl. Surf. Sci. , 2013, vol. 264,
pp. 563–69.
30. D. Dye, J. Coakley, V.A. Vorontsov, H.J. Stone, and R.B. Rogge:
Scr. Mater. , 2009, vol. 61, pp. 109–12.
31. Y. Amouyal, Z. Mao, and D.N. Seidman: Acta Mater. , 2010,
vol. 58, pp. 5898–5911.
32. M. Palumbo, D. Baldissin, L. Battezzati, O. Tassa, R. Wunderlich,
H.J. Fecht, R. Brooks, and K. Mills: Materials Science Forum ,
Trans Tech Publications, Aedermannsdorf, 2006, pp. 591–96.
METALLURGICAL AND MATERIALS TRANSACTIONS A

## Page 11

33. S.C.H. Llewelyn, K.A. Christoﬁdou, V.J. Araullo-Peters, N.G.
Jones, M.C. Hardy, E.A. Marquis, and H.J. Stone: Acta Mater. ,
2017, vol. 131, pp. 296–304.
34. K. Matuszewski, A. Mu¨ller, N. Ritter, R. Rettig, K.J. Kurzydłowski,
and R.F. Singer: Adv. Eng. Mater., 2015, vol. 17, pp. 1127–33.
35. K. Matuszewski, R. Rettig, H. Matysiak, Z. Peng, I. Povstugar, P.
Choi, J. Mu¨ller, D. Raabe, E. Spiecker, K.J. Kurzyd łowski, and
R.F. Singer: Acta Mater. , 2015, vol. 95, pp. 274–83.
36. K. Serin, G. Go ¨benli, and G. Eggeler: Mater. Sci. Eng. A , 2004,
vol. 387, pp. 133–37.
37. L.J. Carroll, Q. Feng, and T.M. Pollock: Metall. Mater. Trans. A ,
2008, vol. 39A, pp. 1290–1307.
38. R.A. MacKay, T.P. Gabb, A. Garg, R.B. Rogers, and M.V.
Nathal: NASA Glenn Research Center, Cleveland, OH, unpub-
lished research, 2012.
39. J.X. Zhang, T. Murakumo, H. Harada, and Y. Koizumi: Scr.
Mater., 2003, vol. 48, pp. 287–93.
40. R.A. MacKay, T.P. Gabb, A. Garg, R.B. Rogers, and M.V.
Nathal: Mater. Charact. , 2012, vol. 70, pp. 83–100.
41. G.L. Erickson: Superalloys 1996 , TMS, Warrendale, PA, 1996,
pp. 35–44.
42. W.S. Walston, K.S. O’Hara, E.W. Ross, T.M. Pollock, and W.H.
Murphy: Superalloys 1996, TMS, Warrendale, PA, 1996, pp. 27–34.
43. C.M.F. Rae and C. Roger: Reed. Acta Mater. , 2001, vol. 49,
pp. 4113–25.
44. A. Heckl, S. Neumeier, M. Go ¨ken, and R.F. Singer: Mater. Sci.
Eng. A , 2011, vol. 528, pp. 3435–44.
45. P. Caron and T. Khan: Aerosp. Sci. Technol. , 1999, vol. 3,
pp. 513–23.
46. K. Matuszewski, R. Rettig, and R.F. Singer: MATEC Web Con-
ference, EDP Sciences, 2014, p. 09001.
47. J.Y. Chen, Q. Feng, L.M. Cao, and Z.Q. Sun: Mater. Sci. Eng. A ,
2011, vol. 528, pp. 3791–98.
48. M.V. Nathal and L.J. Ebert: Metall. Trans. A , 1985, vol. 16A,
pp. 1849–62.
49. R.L. Dreshﬁeld and K.J. Thomas: unpublished research,
2005.
50. A.K. Jena and M.C. Chaturvedi: J. Mater. Sci. , 1984, vol. 19,
pp. 3121–39.
51. P.T. Forde: Adv. Mater. Process. , 1996, vol. 149, p. 4.
52. M.S.A. Karunaratne, C.M.F. Rae, and R.C. Reed: Metall. Mater.
Trans. A , 2001, vol. 32A, pp. 2409–21.
53. C. Booth-Morrison, Z. Mao, R.D. Noebe, and D.N. Seidman:
Appl. Phys. Lett. , 2008, vol. 93, p. 033103.
54. V. Biss and D.L. Sponseller: Metall. Trans. , 1973, vol. 4,
pp. 1953–60.
55. A.F. Giamei and D.L. Anton: Metall. Trans. A , 1985, vol. 16A,
pp. 1997–2005.
56. K.E. Yoon, R.D. Noebe, and D.N. Seidman:
Acta Mater. , 2007,
vol. 55, pp. 1159–69.
57. C.L. Fu, R. Reed, A. Janotti, and M. Krcmar: Superalloys 2004 ,
TMS, Warrendale, PA, 2004, pp. 867–76.
58. A. Janotti, M. Krc ˇ mar, C.L. Fu, and R.C. Reed: Phys. Rev. Lett. ,
2004, vol. 92, p. 085901.
METALLURGICAL AND MATERIALS TRANSACTIONS A
