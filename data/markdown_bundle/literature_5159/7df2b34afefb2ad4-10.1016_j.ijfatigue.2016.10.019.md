# 10.1016_j.ijfatigue.2016.10.019

<!-- source: D:\总文献\10.1016_j.ijfatigue.2016.10.019.pdf -->
<!-- file_sha256: 5e8a32ee6241cc561503293e04ea338e1ac6ee3f92a84413ec323119d10b03d9 -->

## Page 1

Accepted Manuscript
Service-like TMF tests for the validation and assessment of a creep-fatigue life
procedure developed for GT blades and vanes
E. Vacchieri, S.R. Holdsworth, E. Poggio, P. Villari
PII: S0142-1123(16)30344-9
DOI: http://dx.doi.org/10.1016/j.ijfatigue.2016.10.019
Reference: JIJF 4103
To appear in: International Journal of Fatigue
Accepted Date: 19 October 2016
Please cite this article as: Vacchieri, E., Holdsworth, S. R., Poggio, E., Villari, P., Service-like TMF tests for the
validation and assessment of a creep-fatigue life procedure developed for GT blades and vanes, International Journal
of Fatigue (2016), doi: http://dx.doi.org/10.1016/j.ijfatigue.2016.10.019
This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers
we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and
review of the resulting proof before it is published in its final form. Please note that during the production process
errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Page 2

Service-like TMF tests for the validation and assessment
of a creep-fatigue life procedure developed for GT
blades and vanes
E. Vacchieri1,∗, S.R. Holdsworth 2, E. Poggio 1, P. Villari1
1 Ansaldo Sviluppo Energia s.r.l. Via N. Lorenzi 8, 16152 Genoa, Italy
2 EMPA, Swiss Federal Laboratories for Materials Science and Technology,
¨Uberlandstrasse 129, 8600 D¨ ubendorf, Switzerland
∗ corresponding author: erica.vacchieri@ansaldoenergia.com
Abstract
The evolution of the energy production market is responsible for more de-
manding conditions in terms of thermo-mechanical fatigue (TMF) for GT
critical components. In fact, daily cycling is generally conducted by plant
owners to feed the market when the request is higher or when renewable
energy sources are absent or weak.
TMF benchmark tests have been exploited to assess and validate a creep-
fatigue liﬁng procedure developed for two Ni based superalloys applied on
the most critical GT blade and vane of an F-class power plant. The TMF
cycles have been deﬁned on the basis of start-up/shut-down transient FE
simulations for three case studies. For one of the studied components, the
eﬀect of the metallic coating on life reduction has been evaluated. The TMF
benchmark tests results have been compared to ﬁeld feedback from real com-
ponents in order to further validate the whole creep-fatigue life procedure.
Keywords: Ni based superalloys, TMF benchmark cycle, Creep-fatigue
interaction, Damage summation diagram, Liﬁng procedure
Nomenclature
TMF Thermo-mechancal fatigue
GT Gas turbine
OEM Original equipment manufacturer
SX Single crystal
Preprint submitted to International Journal of Fatigue September 29, 2016

## Page 3

ϑ deviation angle with the nominal⟨001⟩ solidiﬁcation direction of a SX alloy
VPS Vacuum plasma spray
BKIN Bilinear kinematic hardening
˙ε strain rate
Rε strain ratio
IP In-phase
OP Out-of-phase
s1, s3 principal stress components
DBTT Ductile brittle temperature transition
TV2 Second stage vane
TV3 Third stage vane
SED Strain energy density
Nf Number of cycle to crack initiation
T Temperature
εcr creep strain
σV M Von Mises stress
1. Introduction
The increased ﬂexibility of the power generation market due to the eco-
nomic climate and discontinuous use of conventional resources for renewable
energies is responsible for a new service environment. The eﬀect of the new
operating regime on the most critical components of GT plants is key knowl-
edge for GT original equipment manufactures (OEMs). In fact, blades and
vanes can suﬀer strongly from the frequent start-up and shut-down transients
because fatigue damage can interact with creep and environmental damage,
reducing the expected life for these components, their maintenance intervals
and repairability. In this environment, thermo-mechanical fatigue (TMF)
is the main source of failure of GT hollow components as they are charac-
terised by strong thermal gradients and complex geometry. Therefore the life
assessment procedure for these components has to involve the consideration
of TMF.
TMF resistance is a key feature for alloys employed as structural ma-
terials for GT blades and vanes due to their mode of operation. Material
behaviour is generally studied through ”classical” tests like creep and fatigue
that simulate in a distinct way the service condition for this kind of com-
ponent. This strategy is consistent with the real blade and vane material
2

## Page 4

behaviour if the operating regime is mainly base load. However, since the
service environment has had to change completely in recent years, material
characterisation testing campaigns have also had to evolve and improve to
simulate the eﬀect of short base load periods spaced out by frequent shut-
down and start-up transients. For this reason, cyclic-hold time and TMF
tests are conducted to generate results that are able to assess and validate
the life assessment procedures that have been selected for this class of GT
components.
The materials that are employed in GT critical components are Ni based
superalloys that guarantee an excellent mechanical resistance at high tem-
peratures due to their microstructure which is composed of a high volume
fraction (45-60%) of an intermetallic phase, Ni 3Al, called γ′, that precip-
itates coherently in a solid solution strengthened austenitic matrix [1, 2].
Moreover, single crystal (SX) alloys are used for the most critical blades for
their outstanding creep and satisfactory fatigue properties along the compo-
nent axis, that corresponds to the centrifugal force. Their extremely stable
microstructure is responsible for their high yield strength that is maintained
at high temperature. These alloys are also characterised by relatively low
ductility at high temperature and so their fatigue endurances exhibit a very
low transition life Nt , generally less than 100 [3]. As a consequence, elastic
conditions dominate in the region of interest of practical application to real
components and are fundamental in determining creep-fatigue behaviour.
These materials exhibit fatigue dominated failures with a greater vulnerabil-
ity to compressive hold times than tensile dwells. This response is due to
the evolution and maintenance of high levels of mean stress during cycling
acting together with environmental eﬀects [3]. Nevertheless, it is important
to emphasise that critical GT components are relatively light as they are hol-
low and they are characterised by complex cooling systems and geometries.
These conditions lead to stress states that are mainly thermally driven, also
considering rotating components.
In the present paper, the developed creep-fatigue life assessment proce-
dure has been benchmarked through TMF tests based on three case studies
from an F-class GT plant. The service like cycle has been deﬁned on the ba-
sis of an FE simulation output of a start-up/shut-down transient. The test
results have been exploited to examine the life assessment procedure and
to validate the developed strategy, evaluating the location and features of
physical damage observed in operated components. Moreover, for one of the
three case studies, the eﬀect of metallic coating on TMF life reduction has
3

## Page 5

been evaluated comparing two coatings with diﬀerent chemical compositions.
2. Materials and methods
The creep-fatigue life assessment procedure was developed considering
three case studies, two vanes made in Ren´ e 80 and one blade produced in
IN792SX. The compositions of the two alloys are shown in Table 1.
Table 1: Chemical composition (wt%) of the two Ni based superalloys.
Alloy Ni Cr Co Al Ti Mo W T a Zr B C
Ren´ e 80 bal. 14.0 9.50 3.00 5.00 4.00 4.00 - 0.03 0.015 0.17
IN792SX bal. 12.2 9.00 3.60 4.10 1.80 3.80 5.00 - - 0.07
For the SX blade, the eﬀect of two metallic coatings was studied. They
were both NiCoCrAlYRe that diﬀered mainly in their Re and Co contents.
In Table 2 their compositions are compared.
Table 2: Chemical composition (wt%) of the two NiCoCrAlYRe coatings.
Coating Ni Cr Co Al Re Y
NiCoCrAlY2Re bal. 21.0 12.0 11.0 2.00 0.40
NiCoCrAlY1Re bal. 17.0 25.0 10.0 1.50 0.40
Mechanical samples were machined from investment cast bars, solidiﬁed
along the ⟨001⟩ crystallographic direction for the SX alloy with the same
acceptance limit for θ as for real components. Some of the SX specimens
after machining were coated by vacuum plasma spray (VPS) with the two
studied coatings. All the specimens (coated and uncoated) were tested in the
fully heat-treated condition. The starting microstructure for these two alloys
was slightly diﬀerent as the γ′ phase volume fraction was about 50% with a
bimodal distribution of γ′ particles, primary precipitates of about 0.40 µm
and secondary particles of about 20 nm for the equiaxed alloy, and 60% with
a monomodal distribution of γ′ precipitates of about 0.40-0.50 µm for the
SX alloy.
The FE simulations of the selected components were conducted, using
Ansys 15.0, adopting an elasto-plastic bilinear kinematic hardening cyclic
stress-strain (BKIN) model and a creep (Norton) model for the base ma-
terial. For the SX blade, the simulation was conducted applying also the
4

## Page 6

metallic coating as shell elements, and for this layer the elastic properties
and a time hardening creep model derived for one of the studied coatings
was used for both. The anisotropy of the SX material was considered for
both elastic properties and the plasticity model. The calculations were per-
formed simulating a standard start-up/shut-down transient and are repeated
four times to enable stabilisation of the simulation. The identiﬁed vane and
blade critical locations were used for the TMF benchmark cycle deﬁnition by
post-processing the simulation output.
The TMF tests were performed in strain control mode, following exist-
ing standards [4], using an induction heating system, with the detailed fea-
tures of the cycles described in §3.2. A comprehensive post-test inspection
was conducted in order to identify the diﬀerent cracking mechanisms and to
understand the physical reasons of the mechanical test results. Moreover,
ex-service components were examined to compare the ﬁeld critical locations
with those identiﬁed by FE calculation and thereby to compare the ex-service
damage with that created in the service-like TMF tests.
3. Results and Discussion
The main focus of this paper is devoted to TMF bechmark tests but a
short summary of the developed life assessment procedure is reported to un-
derstand the role of these tests for its validation. Moreover, the ﬁeld feedback
for the studied parts is here summarised mainly to show the eﬀectiveness of
the TMF test: in simulating the physical damage condition of operated com-
ponents, and also for life assessment procedure validation.
3.1. Creep-fatigue life procedure
The developed strategy starts from an integrated procedure described
in [5, 6, 7] and depicted in Figure 1.
The procedure is composed of four steps. The ﬁrst step corresponds to
the deﬁnition of the constitutive models that describe the studied material
and to deﬁnition of the external forces imposed on the structure. The sec-
ond step involves ﬁnite element analysis and identiﬁcation of the critical
locations in the parts from the simulation output (and the deﬁnition of the
creep-fatigue tests, conducted in the next step). The third stage of the
procedure comprises the creep-fatigue interaction testing campaign respon-
sible for deﬁnition of the damage summation diagram for the studied alloy
applied for the selected component. Finally, in the fourth step service-like
5

## Page 7

Figure 1: Flow diagram of the analysis route adopted in the present paper and by a
number of defect-free creep-fatigue assessment procedure [5, 6, 7].
6

## Page 8

TMF tests are conducted in order to validate the developed life assessment
strategy. In some cases, the TMF benchmark test results can be exploited
also for the assessment of the whole procedure.
In the present paper the main focus is the development of service-like
TMF tests in terms of cycle deﬁnition from FE simulation, and the test results
that have been exploited to evaluate the whole life assessment procedure and
to validate the followed strategy by the comparison of ﬁeld and laboratory
damage features.
3.2. TMF cycle deﬁnition
The FE simulation of a start-up/shut-down transient, conducted itera-
tively to allow code stabilisation, identiﬁes at least a critical location for
each case study in terms of cumulated creep and plastic strain.
The selected nodes from the three case studies have been post-processed
in order to obtain their stress-strain conditions. This information has been
exploited for two purposes. The ﬁrst is to deﬁne the condition for the
cyclic/hold tests in terms of temperature, strain and hold time position.
The second is to deﬁne the benchmark TMF cycles that will be described
below. This ﬁrst has been shown in more detail in [7].
Considering the selected case studies, the two vanes are mainly subjected
to thermal loading. This is also the case for the blade which also experiences
weak primary loads. This is because the blade is hollow and light but with-
stands strong thermal gradients due to its complex geometry and cooling
system.
For all the studied parts, the critical locations are surface nodes that
are characterised by high or intermediate maximum temperatures and com-
pressive or tensile loads during the steady running period, depending on the
component. Moreover, they are generally strain driven even if some mixed
mode has been observed in particular for locations characterised by geo-
metrical discontinuities or complex temperature distribution. In Figure 2
the critical location for the second stage vane is depicted in terms of stress,
strain and temperature distributions at the end of the steady running period
of the self-equilibrated cycle for the simulated transient.
The transients have been studied for all the components in terms of
”signed” von Mises stress and mechanical strain and the stabilised cycle
has been used to deﬁne the service-like TMF test conditions.
For the two vanes the cycle temperature ranges from 400 to 800 ◦C while
the cycle shape is diﬀerent. For the second stage vane, TV2, the cycle is
7

## Page 9

Figure 2: Critical location at the ﬁllet radius between the trailing edge and the internal
platform for second stage vane: normalised s1, s3, σV M (Von Mises stress), T (tempera-
ture) and εcr (cumulated creep strain) at the end of the self-equilibrated base load cycle.
IP with a tensile strain during the maximum temperature hold time, while
the third stage vane, TV3, has an OP cycle with a compressive strain acting
during the hold time. The ˙ε and theRε are diﬀerent with respect to explored
LCF and cyclic-hold time test conditions [8, 7], with ˙ ε≪ 10−2s−1 for both
the components. Rε=0 for the second stage vane and−∞ for the third stage
vane. In Figure 3 the two TMF cycles are compared.
For the blade, two TMF cycles have been deﬁned based on two diﬀer-
ent critical locations, identiﬁed by FE simulation. The ﬁrst one is on the
platform edge while the second one at the ﬁllet radius of the airfoil with the
platform, both on the pressure side. The platform edge is a hot region of
the blade where high creep strain is cumulated in compression at the end
of the FE simulation. The cycle is OP with Rε=−∞ and the temperature
ranges from 400 to 950 ◦C. In contrast, the criticality for the ﬁllet radius is
due to the strong s3 tensor component at the beginning of the steady run-
ning phase that quickly relaxes, and to the not negligible s1 component at
the end of the transient. For this location, the coating shell elements have
been considered in the FE simulation. In Figure 4-a the critical location is
highlighted in the s3 map during the base load and the trend of the stress
8

## Page 10

Figure 3: Service-like TMF cycles for Ren´ e 80 benchmark tests for the TV2 and TV3
vanes.
tensor as signed Von Mises stress is shown for the node in the coating and
in the base material in Figure 4-b. This condition is very detrimental for
coatings as the tensile peak at the end of the transient below their ductile
brittle temperature transition (DBTT) can cause quick crack initiation and
for this reason this TMF cycle has been applied on coated samples to bench-
mark the coating role in crack initiation and the eﬀect on endurance of its
chemical composition modiﬁcation. Also in this case the TMF cycle is OP
and Rε=−∞, but the temperature range is from 200 to 815 ◦C, to evaluate
the eﬀect of low minimum temperature for coating behaviour.
Figure 4: (a) s3 tensor component map during the base load and (b) trend of the signed
Von Mises stress for the coating (BC) and the facing base material (BM) nodes.
9

## Page 11

3.3. TMF benchmark test results
The two sets of service-like TMF cycle results for Ren´ e 80 are summarised
in Figure 5. The greater endurance reduction is observed for the IP-cycle
(TV2, with tensile hold time at maximum temperature) compared with the
OP-condition (TV3, with compressive hold time at maximum temperature).
This observation is the opposite of what has been observed for cyclic/hold
tests, described in [8].
Figure 5: Comparison of third (TV3) and second (TV2) stage vane TMF test results on
Ren´ e 80 samples with respect to LCF endurance at 800◦C.
However, as already highlighted previously, in these tests theRε values are
far from -1 and for the IP-cycle the starting mean stress is high and positive,
as shown in Figure 6. In spite of this observation, it is important to highlight
that the OP cycle seems to become more detrimental with decreasing strain
range and it can be expected that after a certain number of cycles this cycle
starts to be more dangerous than the IP one.
No great amount of TMF test results is shown in the open literature for
this alloy. Furthermore, the results are cycle shape dependent, so it is very
diﬃcult to compare the obtained results with already published data. Similar
trends have been summarised in [3]. Recently, Ren´ e 80 has been tested in
10

## Page 12

Figure 6: Normalised peak stresses for the IP (TV2) and OP (TV3) service-cycle TMF
tests (red lines maximum stress, light-blue lines minimum stress and green lines mean
stress.
standard OP and IP-TMF tests without dwell time and with Rε =−1 [9].
The collected results do not show a great diﬀerence between OP and IP cycles,
for temperature ranging from 100◦C to 950◦C, while the diﬀerence becomes
signiﬁcant when Tmax is 750◦C. In these conditions OP-TMF tests exhibit
shorter lives than IP-TMF tests. This observation is not in accordance with
the TMF results here presented while they are consistent with the cyclic/hold
test results [8, 7], as they have been conducted with the same Rε. Another
great diﬀerence between these tests and the results shown here is the presence
of a long dwell time for the TMF tests described in the present paper. The
hold time at the maximum temperature of the cycle strongly aﬀects the
hysteresis loop position within TMF sample life due to stress relaxation that
causes physical damage and deformation eﬀect (i.e. γ′ rafting) in the sample
gauge length. In fact, the two service-like TMF cycles are more complicated
because time-dependent eﬀects have not been neglected and the cycle shapes
are far from the standard ones used by Buchholz et al [9].
For the blade critical locations, the results for the two TMF cycles on
uncoated samples are summarised in Figure 7-a. Both the TMF cycles show
a life reduction with respect to the LCF curve and the TMF endurance
decreases with smaller strain range, in agreement with the cyclic/hold test
behaviour for this alloy [7]. This is due to the main elastic contribution that
causes a continuous shift of the mean stress towards positive values.
For the ﬁllet radius region, the TMF test results of uncoated samples
11

## Page 13

Figure 7: TMF test results for IN792SX (a) uncoated samples with platform region cycle
(black circle) and ﬁllet radius cycle (grey triangle) and (b) coated sample with ﬁllet radius
cycle (black diamond NiCoCrAlY1Re and black square NiCoCrAlY2Re).
12

## Page 14

have been compared to the coated ones and the endurance reduction is two
order of magnitude bigger for NiCoCrAlY2Re coating than the other coating
that behaves as the base material, Figure 7-b. NiCoCrAlY2Re seems to ex-
hibit “instantaneous” crack initiation in particular for the highest mechanical
strain.
The sample surface after test conﬁrms this observation as there are several
circumferential cracks with quite constant distance, that always cross the
whole coating thickness also away from the main crack, as shown in Figure 8-
a, b. It is not the case for the NiCoCrAlY1Re that shows a sample surface
characterised by small cracks with irregular path, that generally are more
similar to surface roughness and whose penetration does not reach more
than half of the coating thickness away from the main crack, as shown in
Figure 8-c, d.
The two coatings depict completely diﬀerent crack initiation and propa-
gation mechanisms and this behaviour is related to their diﬀerent chemical
composition that brings to diﬀerent thermo-physical and mechanical proper-
ties. The minimum temperature for this TMF cycle is low (200 ◦C) and for
both the coatings it is below the DBTT. These two coatings are also diﬀer-
ent because their thermal expansion coeﬃcient, α(T ), with NiCoCrAlY1Re
having anα(T ) closer to the SX alloy in contrast to that of NiCoCrAlY2Re.
However, this aspect cannot explain completely the diﬀerent endurances de-
picted by the two coatings. In fact, the chemical composition of the two
coatings is responsible for a diﬀerent microstructure considering the TMF
temperature range as shown in Figure 9 where the microstructure and the
phase distribution as a function of temperature are represented. The coating
that shows the shortest endurance curve is characterised at the cycle maxi-
mum temperature by aγ′ phase matrix, as observed from the microstructure
and from the thermodynamic calculation. This phase is highly fragile which
explains the cracks through the whole coating thickness.
3.4. Creep-fatigue life methodology validation
The TMF test results have been used to calculate damage fractions by
considering the mid-life cycle. The fatigue damage fraction has been calcu-
lated considering the strain range and the maximum temperature of the cycle
to identify the reference endurance in the Manson-Coﬃn equation. For creep
damage fraction, the strain energy density (SED) method [10] has been used
[8, 7]. The choice of the creep damage calculation method has been based on
the goodness in life prediction as reported in [7]. The life evaluation based
13

## Page 15

Figure 8: TMF coated sample after test: (a) sample surface that shows circumferential
cracks and (b) metallographic section for NiCoCrAlY2Re coating; (c) sample surface that
depicts roughness-like cracks and (d) their aspect in section for NiCoCrAlY1Re coating.
14

## Page 16

Figure 9: Thermodynamic calculations performed with Thermocalc software and TCNi6
database and coating microstructure after the TMF test: (a) NiCoCrAlY2Re and (b)
NiCoCrAlY1Re.
15

## Page 17

on linear damage summation shows non-conservative estimation for some of
the tested conditions for both the studied alloys and considered case stud-
ies, as shown in Figure 10-a, b. So, a summation locus that comprises an
interaction factor has been deﬁned and following this strategy all the exper-
imental points are well predicted and non-conservativeness is prevented, as
depicted in Figure 10-c, d, except for one point of Ren´ e 80 alloy that is still
non-conservative considering the selected interaction locus.
This allows the veriﬁcation of the creep-fatigue locus reliability, deﬁned
in the step 3 of the procedure (§3.1).
Figure 10: Life prediction using SED method for creep and linear interaction for (a)
IN792SX and (b) Ren´ e 80 and improved prediction through the use of an interaction
factor (c) IN792SX and (d) Ren´ e 80, with a±2 scatter band.
3.5. Field feedback veriﬁcation
The deﬁned life prediction methodology has been applied to the FE sim-
ulation output for the three case studies. Endurance evaluations have been
16

## Page 18

based on the last simulated cycles calculating the damage fractions and sum-
ming them up following the deﬁned interaction rule. They form the basis
of creep-fatigue Nf (life) map. The life maps have been compared to the
ﬁeld feedback and a good correspondence has been achieved both in terms of
location of critical areas and of quantitative evaluation of number of cycle to
crack initiation. In Figure 11 the life maps for TB1 and TV2 has been com-
pared to the ﬁeld feedback and it is possible to appreciate the eﬀectiveness
of the developed methodology.
The ﬁeld feedback permits further veriﬁcation of the developed strategy
as the damage features that have been created through the TMF benchmark
cycles are in agreement with the real damage observed at the selected crit-
ical locations. In Figure 12 some examples of cracks in operated parts are
compared with the TMF sample damage.
4. Conclusions
TMF benchmark tests are fundamental for the assessment and validation
of a new life assessment procedure. The great eﬀectiveness of the TMF
cycles deﬁned from FE transient simulations of the selective case studies has
been demonstrated by comparison with the physical damage observed in real
components and the one produced in the tested samples. This observation,
valid for all the considered parts, enforces the use of these benchmark tests
during the design of new components as it allows the evaluation of critical
location behaviour and the validation of the developed design. Finally, the
service-like TMF tests can be exploited for the coating eﬀect quantiﬁcation.
By focusing on a critical location, the life reduction when a coating is applied
can be evaluated. In the next future the developed life assessment procedure
will be applied to other case studies and to other transients that characterise
the service experience of GT blade and vane, like unexpected stops (i.e. trip
or load rejection) or quick ramps from minimum load to peak load. Future
improvements will comprise iterative FE simulations trying to reduce their
calculation time and damage fraction evaluation extending the calculation to
the whole life of the test and not only to mid-life cycle and considering the
mean stress eﬀect.
Acknowledgement
The authors wish to express their thanks to Daniele Antoniol from Ansaldo
Sviluppo Energia srl Mechanical testing Lab for his support in TMF tests ex-
17

## Page 19

Figure 11: Comparison of the Nf maps and ﬁeld feedback from components after service
that withstand diﬀerent operating regimes, from intermediate to daily cycling: (a) TV2,
(b) TB1.
18

## Page 20

Figure 12: Comparison of the cracks observed at the critical locations in real operated
components and in the TMF samples during post-test inspection: Ren´ e 80 - (a) TV2 ﬁllet
radius with the internal platform at trailing edge and (b) TMF sample; IN792SX - (c)
TB1 ﬁllet radius on the pressure side and (d) TMF sample.
19

## Page 21

ecution. The support of Tullio Ranucci and Dr. Maurizio Maldini from CNR
IENI Milano for the TMF tests conducted in their Lab was very important
and greatly appreciated.
References
[1] Reed, R., 2006. The superalloys, fundamentals and applications. Cam-
bridge University Press, Cambridge, UK.
[2] Mughrabi, H., 2009. ”Microstructural aspects of high temperature de-
formation of monocrystalline nickel base superalloys: some open prob-
lems”. Matererial Science and Technology, 25(2), pp. 191–204.
[3] Plumbridge, W. J., and Ellison, E. G., 1987. ”Low cycle fatigue be-
haviour of superalloy blade materials at elevated temperature”. Matere-
rial Science and Technology, 3, pp. 706–715.
[4] ISO 12111, 2011, Metallic naterials - Fatigue testing - Strain controlled
thermomechanical fatigue testing method, International standards or-
ganisation.
[5] Holdsworth, S. ”Creep-fatigue testing and assessment guideline material
property data requirements for component assessment”. EPRI Technical
Report 1019778, December 2010.
[6] Holdsworth, S., 2011. ”Component assessment data requirements from
creep-fatigue tests”. Journal ASTM International, 8(3), p. JAI103583.
[7] E. Vacchieri, S.R. Holdsworth, E. Poggio, P. Villari, A. Costa, ”Creep-
fatigue assessment strategy for gas turbine blades and vanes: safe
life procedure development, assessment and experimental validation”,
ASME Turbo Expo 2016, Seul, South Korea, June 2016, GT2016-58039.
[8] E. Vacchieri, S. R. Holdsworth, A. Costa, E. Poggio, A. Riva and P. Vil-
lari, ”Creep–fatigue interaction in two gas turbine Ni based superalloys
subjected to service-like conditions”, Materials at High Temperatures,
31(4), 2014, pp. 348–356.
[9] Buchholz, B. ”Development of a generalised LCF-TMF liﬁng model for
a nickel-base superalloy”. ASME Turbo Expo 2012, Copenhagen, Den-
mark, June 2012, GT2012–68786.
20

## Page 22

[10] Payten, W., 2010. ”A strain energy density method for the prediction of
creep-fatigue damage in high temperature components”, Material Sci-
ence Engineering A, 527, pp. 1920–1925.
21

## Page 23

 A creep-fatigue interaction lifing strategy has been defined for two Ni based superalloys with 
different solidification microstructures. 
 The validation and assessment of the lifing strategy has been performed through service-like TMF 
tests defined on the basis of FE simulation of the GT components. 
 The lifing procedure has been successfully applied to three parts and verified through field 
feedback. 
Highlights
