# 32_2019_Brindley_Integrative_Materials_Design_of_Three_Phase_Mo_Si_B_Alloys

<!-- source: D:\总文献\32_2019_Brindley_Integrative_Materials_Design_of_Three_Phase_Mo_Si_B_Alloys.pdf -->
<!-- file_sha256: 88203aa7c1394b914fce49d8493b25723e7d50f64af01d4c38c91c47323fa024 -->

## Page 1

IntegratingMaterialsandManufacturingInnovation(2019)8:1–16
https://doi.org/10.1007/s40192-019-0124-4
TECHNICALARTICLE
IntegrativeMaterialsDesignofThree-PhaseMo-Si-BAlloys
K.A.Brindley 1 ·M.W.Priddy 2 ·R.W.Neu 1,3
Received:8November2018/Accepted:2January2019/Publishedonline:12February2019
©TheMinerals,Metals&MaterialsSociety2019
Abstract
Mo-Si-B alloys can offer higher temperature capability than Ni-base superalloys with proper balancing of the creep, ductility,
and oxidation resistance through microstructure optimization. Mo-Si-B alloys are heterogeneous, containing both brittle
and ductile phases and interfaces. Therefore, the phase fractions, their distributions, and their constitutive properties over
the range of room temperature to maximum use temperature must be considered. This work addresses the optimization
of mechanical properties for three-phase Mo-Si-B alloys. Three modeling tools are employed: microstructure generators
to re-create statistically realistic microstructures, crystal viscoplasticity constitutive equations implemented for use with
finite element solvers to capture microplasticity, and reduced-order models for evaluating important mechanical properties.
In particular, the effects of microstructure on elastic modulus, yield strength, fatigue resistance, and susceptibility to
brittle microcracking are considered. A novel reduced-order model is introduced for the evaluation of susceptibility to
microcracking at phase interfaces. It is found that the Si content of the α-Mo phase is much more significant to the alloy’s
balance of mechanical properties than the α-Mo volume fraction.
Keywords Mo-Si-B alloys · Molybdenum-silicide alloys · ICME · Structure-property relationships
Introduction
Refractory metals and their alloys offer higher temperature
alternatives to Ni-base superalloys [1–6]. In particular,
Mo-Si and Mo-Si-B intermetallics offer oxidation and
creep resistance at temperatures up to 1300
◦C[ 3, 7,
8], which is approximately the melting temperature of
Ni-base superalloys [ 1, 6]. However, these intermetallics
present a significant design challenge due to their low
ductility and low fracture toughness at room temperature
[3]. A balance of high-temperature and low-temperature
mechanical properties may be achieved in Mo-Si-B alloys
/envelopebackK. A. Brindley
kbrindley@gatech.edu
1 The George W. Woodruff School of Mechanical Engineering,
Georgia Institute of Technology, 801 Ferst Drive, Atlanta,
GA 30332, USA
2 Department of Mechanical Engineering, Mississippi State
University, 479-1 Hardy Road, Mississippi State,
MS 39762, USA
3 School of Materials Science and Engineering,
Georgia Institute of Technology, 771 Ferst Drive,
Atlanta, GA 30332, USA
by including the more ductile α-Mo phase in addition to
the intermetallic phases [3, 7, 8]. However, balancing the
oxidation resistance, creep resistance, and damage tolerance
requires careful microstructure optimization.
Of the numerous studies on the development of three-
phase Mo-Si-B alloys [7, 9–20], perhaps the most promising
of Mo alloys is a three-phase microstructure consisting of
the intermetallic Mo 3Si and Mo 5SiB2 (T2) phases in a con-
tinuous α-Mo matrix [12, 18, 19, 21, 22]. Consequently, the
material chosen for the focus of this research is a equiaxed,
randomly textured, three-phase Mo-Si-B alloy with a con-
tinuous α-Mo matrix with average grain diameters of 10 μm
and containing the intermetallic Mo 3Si and T 2 phases with
average grain diameters of 8 μm. These alloys are typically
created using powder metallurgy because it has proven
difficult to create the desired α-Mo matrix using melt-based
processing and hot working [ 7, 23, 24].
The α-Mo phase is a solid solution of Si in Mo. This
body-centered cubic (BCC) phase is key to providing the
ductility and fracture toughness for three-phase Mo-Si-B
alloys; however, it oxidizes readily above 600
◦C and has
poor creep resistance at high temperatures [3, 25]. The
strength of the α-Mo phase is highly dependent on Si
content, where as little as 1 wt.% Si can increase the yield
strength to nearly 1000 MPa from the 400 MPa of pure

## Page 2

2 IntegrMaterManufInnov(2019)8:1–16
Mo at room temperature [25]. However, adding Si also
decreases the fracture toughness and ductility. It has been
shown that the addition of 0.5 wt% Si will reduce the room
temperature ductility of α-Mo from 25 to 3% [26, 27].
The reduced fracture toughness and ductility is partially
attributed to Si segregation to grain boundaries [ 15, 25, 28].
Non-uniform distribution of dissolved Si within grains and
throughout the matrix phase may also appear due to sluggish
kinetics [15].
The intermetallic Mo
3Si phase is an A15 cubic phase.
Although only a few mechanical properties have been
quantified for this phase at high temperature, the room
temperature properties of single crystal Mo
3Si specimens
have been investigated [29]. This phase is brittle and strong
at room temperature and high temperatures. At 1325 ◦C,
Mo3Si has a yield strength of over 700 MPa and shows little
plasticity under deformation due to a small number of active
slip systems [3, 30]. The Si in this phase provides oxidation
resistance by forming a nanoporous SiO
2 scale over the
oxidizing surface [3, 8, 31].
The intermetallic Mo 5SiB2 (T2) phase has a body-
centered tetragonal structure. Similar to the Mo 3Si phase,
this phase is strong and brittle from room temperature
up to temperatures of 1500 ◦C[ 32]. High-temperature
mechanical properties have been explored to determine the
elastic constants from room temperature up to 1100 ◦C
[32]. The importance of the T 2 phase is to provide high-
temperature strength and oxidation resistance [ 3]. The
T2 phase provides oxidation resistance by forming a
borosilicate scale in the early stages of oxidation. This
scale then diffuses into the SiO
2 s c a l ef o r m e db yM o3Si,
which lowers the viscosity of the SiO 2 scale and leads to
passivation of the scale [3, 8, 31].
The intermetallic silicide phases are necessary to
improve the high-temperature oxidation resistance and
creep resistance; however, these intermetallics are brittle
even at high temperatures [17, 32]. Consequently, creating
a Mo-Si-B alloy for use in the hot section of gas turbine
engines requires an optimization of the microstructure
between the competing properties of damage tolerance,
strength, fatigue resistance, oxidation resistance, and creep
resistance. In the development of Mo-Si-B alloys, single
property optimizations targeting oxidation resistance have
been explored experimentally and through kinetics models
[23, 24, 31, 33, 34], in some cases demonstrating reasonable
oxidation resistance with as much as 50% α-Mo volume
fraction [33]. While some experimental investigations
on fracture toughness and damage tolerance have been
conducted [12, 18, 22, 35], there has not been much
work done to develop microstructure-sensitive modeling
tools for the toughness and damage tolerance of Mo-Si-
B alloys suitable as a tool for Integrated Computational
Materials Engineering (ICME). The modeling work that
has been done has used computationally expensive cohesive
zone models (CZM) to simulate microcracking at phase
interfaces and within the brittle intermetallic phases [ 36].
In this paper, ICME tools are established to enable
the investigation of the microstructure-sensitive mechanical
properties of Mo-Si-B alloys. Four mechanical properties
are evaluated: two properties controlled by homogenization,
elastic modulus, and yield strength, and two properties
controlled by localization, fatigue crack formation, and
susceptibility to microcracking, which is inversely related
to ductility. For this task, three tools are required: a
microstructure generator for creating synthetic volume
elements, a constitutive model implemented for a finite
element solver, and reduced-order models for evaluation
of mechanical properties. A novel reduced-order model
is introduced to reduce the computational cost of the
evaluation of susceptibility to microcracking at phase
interfaces in comparison to cohesive zone models. A
parametric study is carried out to demonstrate the use
of these tools and to compare the effects of α-Mo Si
content and temperature on the four mechanical properties
of interest.
MicrostructureGenerator
The microstructure generator developed for this work is
based on an ellipsoidal packing algorithm developed by
Przybyla, which includes a simulated anneal algorithm for
space filling [37]. This algorithm is related to the work of
Groeber et al. [38] in development of the tools packaged in
the software package DREAM.3D [ 39]. The microstructure
generator developed for this work is chosen for ease of
extending the algorithm to multiple regions with distinct
microstructural features in a single volume element, which
is important to capture the features of the α-Mo calibration
material [40]. The generator also captures the unique traits
for separate phases as well as the phase volume fractions
for each phase. For each phase, the microstructure generator
is capable of capturing crystal structure, mean and standard
deviation of grain size, grain shape distribution, grain shape
orientation distributions, and orientation distribution.
The crystal structure is captured by passing the phase
and its orientation to the constitutive model, which captures
the elastic anisotropy and slip systems associated with
the crystal structure of that phase. Grain size statistics
are defined as a mean and standard deviation for a
uniform distribution, which the microstructure generator
then converts to a log normal distribution. Grain shape is
captured by approximating grains with ellipsoids defined
by major and minor aspect ratios which vary according
to a beta distribution. The generated ellipsoids are packed
in order from largest to smallest for a single phase at a

## Page 3

IntegrMaterManufInnov(2019)8:1–16 3
time. Control over the final features is provided by artificial
parameters that reduce the ellipsoidal volumes and phase
volume fractions prior to the ellipsoidal packing to account
for changes created by the space filling simulated anneal
process. Both the ellipsoidal packing and space filling
algorithms respect the periodic boundary conditions of the
volume elements. Orientation distributions are captured
through the free and open source, third party, MA TLAB
toolbox MTEX [41]. After the space filling algorithm, all
of the final microstructural features are verified against the
original microstructural description [ 37, 40].
For this work, the synthetic volume elements are required
to be large enough to provide representative volume
elements (RVEs) [42] for the mechanical properties of
elastic modulus and yield strength demonstrated through
convergence studies of mesh refinement and total grain
count (volume element size) [40]. V olume elements
sufficiently large enough to be considered representative for
modeling microstructure-sensitive fatigue crack formation
and damage initiation are computationally intractable.
Instead RVEs for yield strength are treated as statistical
volume elements (SVEs), which capture the locally varying
heterogeneous response of the material [ 43], for fatigue
resistance and susceptibility to brittle microcracking.
Three-PhaseMo-Si-BMaterial
The three-phase Mo-Si-B material synthetic microstructure
instantiations are randomly textured, three-phase volume
elements with a random spatial distribution of the phases.
The characteristics of the synthetic microstructures are
chosen to match some of the more promising Mo-Si-B
alloys [15, 23, 24]. The parametric study conducted in this
work varies two key parameters: volume fraction of each
phase and Si content of the α-Mo phase. The variation
in Si content is achieved through the calibration of the
constitutive model, but the volume fraction of each phase
is captured explicitly in the volume element instantiations.
For the three-phase Mo-Si-B material in the parametric
study, the volume fraction (Vv) of α-Mo is varied from
45 to 80% and the remaining volume fraction is divided
between the intermetallics at a constant ratio of 1:2 A15
to T
2 phase to match the approximate ratios found in the
reference material [24]. The volume element definitions for
the parametric study are presented in Tables 1 and 2.I n
addition to these parameters, several parameters are held
constant for all synthetic microstructures: 33 elements per
edge (35,937 total elements) and ellipsoid aspect ratios of
0.80 with a standard deviation of 0.08 for all three phases.
Six separate instantiations are created for each set
of parameters in the parametric study. An example
instantiation with 63% volume fraction of α-Mo is
Table 1 Microstructure parameters investigated in parametric study
Parameter SVE1 SVE2 SVE3 SVE4 SVE5 SVE6
Edge length (mm) 0.090 0.090 0.090 0.090 0.090 0.090
Vv α-Mo 0.45 0.54 0.63 0.71 0.76 0.80
Vv A15 0.37 0.31 0.25 0.19 0.16 0.13
Vv T2 0.18 0.15 0.12 0.10 0.08 0.07
presented in Fig. 1. The three-phase Mo-Si-B SVEs are
0.09 mm on each edge with 33 elements per edge.
While each instantiation matches the statistical descrip-
tion of the grain size, grain shape, grain shape orientation,
and texture, individual instantiations exhibit locally vary-
ing microstructural features that may effect variability in
the mechanical properties. Specific features, such as mis-
orientation, have been shown to be important for predicting
fatigue response [43] and may be anticipated to effect
damage formation as well. The purpose of these multiple
instantiations is to investigate the sensitivity of the mechan-
ical properties to the locally varying inhomogeneity of the
microstructure.
ConstitutiveModel
A crystal viscoplastic model is used for all three phases
of the three-phase Mo-Si-B alloy, with unique parameter
sets for each phase [ 40]. The model includes the fully
anisotropic elasticity tensors, the crystal slip systems, the
flow rule, and evolution equations. The relatively hard,
brittle, intermetallic phases [3, 30, 32] are treated as purely
elastic, while the relatively ductile α-Mo phase is treated
with a full crystal viscoplasticity (CVP) flow rule over
the 12 {100}⟨111⟩ and 12 {112}⟨111⟩ BCC slip systems.
The option to build upon this work by including plasticity
in the intermetallic phases is maintained by using the
full CVP flow rule for these phases, but assigning the
calibration parameters in such a way that plasticity is
inactive. The full development and calibration of the α-Mo
phase model parameters from polycrystalline experimental
data is presented elsewhere [40].
The flow rule used in this work is an extension of the
crystal plasticity flow rule developed by Pierce et al. [ 44]
Table 2 Fixed microstructure parameters in parametric study
Parameter α-Mo A15 T 2
Mean dia. (μm) 10 8 8
std. dev. dia. (μm) 2 1 1

## Page 4

4 IntegrMaterManufInnov(2019)8:1–16
Fig.1 Three-phase Mo-Si-B
synthetic microstructure with
63% volume fraction α-Mo
and is chosen for its wide use in metal crystal plasticity
models [45–47]. The flow rule is defined as
˙γα =˙γ0
⟨|τα − χα|− κα
Dα
⟩1
m
sgn
(
τα − χα)
(1)
where α is a slip system index, ˙γα is the inelastic shear
strain rate on the αth slip system, ˙γ0 is the reference inelastic
shearing rate, τα is the resolved shear stress on the αth
slip system, and χα , κα ,a n dD α are the current values of
back stress, threshold stress, and drag stress on the αth slip
system, respectively. The ⟨⟩brackets are Macaulay brackets
and sgn () returns positive or negative unity, depending on
the sign of the term in parentheses. The variable m in the
exponent is the strain rate sensitivity exponent. Both ˙γ0
and m are material parameters that are typically treated as
constants, but can vary with microstructure and temperature.
For the α-Mo phase, it is assumed that the 12 {100}⟨111⟩
and 12 {112}⟨111⟩BCC slip systems are active.
Back stress, threshold stress, and drag stress may all
evolve over the course of loading. Depending on the
material under consideration, many different types of
equations have been used for the evolution of back stress,
threshold stress, and drag stress. For back stress and drag
stress, the most common evolution equations follow the
direct hardening, dynamic recovery form of the Armstrong-
Frederick equations [48].
For the α-Mo phase, the drag stress is treated as a non-
evolving constant dependent on temperature and Si content
and back stress evolves as
˙χ
α = B ˙γα − Cχα| ˙γα| (2)
where B and C are functions of temperature and Si content.
The reference inelastic shearing rate ˙γ0 is also a function
of temperature and Si content and the strain rate sensitivity
exponent m is a function of Si content. The threshold stress
κα can also be an evolving function of temperature, Si
content, and grain size. However, the threshold stress is not
used because temperature and solid solution hardening are
already captured in the drag stress and studies of the Hall-
Petch effect in α-Mo have shown inconsistent results with
some studies showing no Hall-Petch behavior at grain sizes
as small as 50 μm[ 25, 49, 50].
The strain rate sensitivity exponent accounts for differ-
ences in yield strength as a function of strain rate, and back
stress evolution is used to calibrate the plastic hardening
behavior. Since no single crystal information is available
for the α-Mo phase to individually calibrate each slip sys-
tem, all 24 slip systems are treated with the same parameter
set; however, the model implementation retains the option
of treating up to three separate types of slip systems with
unique calibrations and can be extended to treat each system
individually.
One limitation of this constitutive framework is the
inability to investigate the dislocation mechanisms of BCC
metals. There are two crystal plasticity frameworks that
directly address the dislocation physics of Mo, such as
twinning/anti-twinning asymmetry and non-glide stresses
[51, 52]; however, these works are limited to relatively
low temperatures and to pure Mo. While these frameworks
are not adopted for the broad parametric study presented
here, future investigations targeting specific microstructures
should include these effects by extending those frameworks
to higher temperatures and Mo-Si solid solutions.
Because stress-strain information available for the α-Mo
phase is limited to monotonic uniaxial compression and
tension tests [25, 40], no calibration can be made for the
cyclic response. Instead, it is assumed that the material

## Page 5

IntegrMaterManufInnov(2019)8:1–16 5
Table 3 Elasticity tensor
component regressions as a
function of temperature (◦C):
y = Mx + b
Component α-Mo A15 T 2
C11 M
[
GPa
◦C
]
−0.0578 −0.0578 −0.0460
b [GPa] 463.0 506.3 492.7
C12 M 0.0058 0.0058 0.0037
b 157.5 79.9 164.0
C13 M –– −0.0017
b – – 196.4
C33 M –– −0.0247
b – – 420.4
C44 M −0.0102 −0.0102 −0.0212
b 109.1 130.2 180.1
C66 M –– −0.0198
b – – 148.3
is cyclically stable and the stabilized hysteresis curve is
obtained from the monotonic calibration.
The constitutive equation is implemented as a User
Material subroutine (UMA T) for the general-purpose finite
element code ABAQUS [53]. The specific Fortran code
used in this work is based on one for γ -TiAl alloys [54]
and has been modified for α-Mo by adding the appropriate
slip systems, evolution equations, the evolution equation
derivatives, and temperature dependence for the elastic and
thermal properties.
ElasticandThermalProperties
The fully anisotropic elasticity tensors and coefficient
of thermal expansion for each phase are obtained from
literature data [29, 32, 55]. The elasticity tensor of Mo
is known from room temperature to 700
◦C[ 55]. To use
the constitutive model at higher temperatures, the elasticity
tensor components are fit with a linear regression as
a function of temperature and extrapolated to 1400
◦C.
Although the majority of the parametric study is for Mo
with Si in solid solution, it has been shown that the addition
of Si up to 1.0 wt% has very little effect on the elastic
modulus [25]. Consequently, the assumption that the elastic
and thermal properties of α-Mo are unaffected by Si content
is reasonable.
The elasticity tensor components for the T
2 phase are
also known as a function of temperature up to 1100 ◦C
[32]. The elasticity tensor is similarly fit with a linear
regression and extrapolated to 1400 ◦C for this phase. The
elasticity tensor components for the A15 phase are only
known at room temperature [29], so some assumption about
the temperature dependence must be made. In this work,
the slope of the linear regression is obtained from the BCC
Mo data for the matching cubic symmetry and used to
extrapolate the cubic A15 elasticity tensor components to
higher temperatures. Other work has used the temperature
dependence of the T
2 phase to extrapolate isotropic
elasticity constants for the A15 phase [ 56]; however, the
temperature dependence prescribed for each phase was
similar. It is worth noting that the elastic properties of
the covalently bonded A15 phase may be less sensitive to
increasing temperature than the Mo phase. The equations
defining the elasticity tensor components are given in
Table 3.
ViscoplasticProperties: α-Mo
The α-Mo phase model parameters are calibrated from
a mixture of polycrytalline α-Mo experimental data [ 25,
40] and presented in Tables 4, 5,a n d 6.T h ev a l u e s
presented here are calculated for use in the three-phase
Table 4 Initial drag stress, D0,
for α-Mo Initial drag stress, D0 (MPa)
Temperature (◦C) Si content (wt%)
0.00 0.10 0.25 0.50 0.75 1.00
25 156.2 134.3 181.3 259.7 334.6 409.4
1400 17.8 50.7 70.3 102.9 159.3 215.7

## Page 6

6 IntegrMaterManufInnov(2019)8:1–16
Table 5 Back stress direct
hardening, B,f o rα -Mo Back stress direct hardening, B (MPa) with fixed back stress dynamic recovery, C = 10.0 [–]
Temperature (◦C) Si content (wt%)
0.00 0.10 0.25 0.50 0.75 1.00
25 5000.0 5000.0 4788.8 4436.9 4211.7 3986.5
1400 2258.9 2258.9 2258.9 2258.9 2258.9 2258.9
Mo-Si-B microstructure simulations from the development
and calibration of the α-Mo constitutive law presented
elsewhere [40]. In this work, the Si content is assumed to be
uniform throughout the α-Mo matrix as well as within each
α-Mo grain. While this is consistent with the calibration
to polycrystal α-Mo data [25], future work can use the
framework developed here to further explore the effects of
Si segregation and distribution.
Linear interpolation is first carried out by temperature,
and then by Si content, except for the initial drag stress, D
0,
at 1400 ◦C where it is found that a power law made a better
fit than a linear regression as a function of temperature at
fixed Si content. For linear interpolation at a Si content
below 0.29 wt% (Mo-0.29Si), the calibration is extrapolated
from Mo-0.29Si and Mo-0.40Si instead of interpolating
between Mo-0.00Si and Mo-0.29Si. This is necessary
because the addition of small amounts of Si in solid solution
changes the dominant deformation mechanism of Mo.
The transition from solid solution softening to solid solu-
tion strengthening with increasing temperature is related to
a transition temperature where the double kink mechanism
no longer dominates plastic deformation and the mobilities
of edge and screw dislocations become similar [ 25]. Conse-
quently, solid solution softening is only observed near room
temperature and lower temperatures. These sub-structure
effects are homogenized in the Si content and temperature
sensitive calibration of the constitutive model parameters for
the α-Mo flow rule and evolution equations [40].
ParametricStudyofThree-PhaseMo-Si-B
The parametric study is designed to help determine
an optimized three-phase Mo-Si-B microstructure that
balances strength, fatigue resistance, and susceptibility to
brittle microcracking. The α-Mo phase volume fraction
varies from 0.45 to 0.8, with the intermetallic phases
maintaining a constant ratio of 2:1 A15 to T
2 phase to fill the
remaining volume. The Si content of α-Mo varies from 0.0
to 1.0 wt% Si to cover the full range of Si content possibly
present in three-phase Mo-Si-B alloys. Each microstructure
has a random texture with randomly orientated grain shapes
because most feasible processing methods result in such
a microstructure. Six sets of volume elements are created
according to the microstructure characteristics shown in
Table 1. To examine the effects of the volume element
instantiations themselves, six separate synthetic volume
element instantiations are created for each microstructure
definition.
The parametric study is carried out at room temperature
and 1400
◦C. A representative microstructure is taken from
Jain and Kumar [15] and from sample material provided by
Pratt and Whitney to ensure the synthetic microstructures
closely match promising Mo-Si-B microstructures. In the
Jain and Kumar microstructure, the α-Mo phase has an
average grain diameter of 20 μm and a volume fraction of
0.511, while the intermetallic phases have grain diameter
averages of 15 μm with 0.170 volume fraction Mo
3Si and
the remainder made up of the T 2 phase.
The simulation consists of one fully reversed cycle with
strain controlled loading to a mechanical strain amplitude of
0.5% applied along the Y-axis (vertical direction in Fig. 1).
Periodic boundary conditions are applied to all six faces of
the SVE, consistent with the periodic packing of ellipsoids
in the microstructure generator. Rigid body motion is
eliminated by fixing a corner node on the negative Y face of
the model. Loading is applied through displacement along
the global Y-axis of a corner node on the positive Y face.
Table 6 Strain rate sensitivity
exponent, m,f o rα-Mo Strain rate sensitivity exponent, m [–] with a fixed reference shearing rate, ˙γ = 0.001
[
1
s
]
Temperature (◦C) Si content (wt.%)
0.00 0.10 0.25 0.50 0.75 1.00
25 6.0 20.0 20.0 20.0 20.0 20.0
1400 20.0 6.0 6.0 6.0 6.0 6.0

## Page 7

IntegrMaterManufInnov(2019)8:1–16 7
An example macroscopic stress-strain response gener-
ated by a simulation for the 63% α-Mo SVE for the dif-
ferent Si contents at room temperature is shown in Fig. 2.
This figure shows solid solution softening of the α-Mo
phase at room temperature where the yield strength of the
Mo-0.10Si α-Mo is lower than that of the Mo-0.00Si α-
Mo. This is caused by changing deformation mechanisms
with increased temperature and Si content as previously
discussed. Although solid solution softening is observed
experimentally at room temperature, it is not seen at high
temperature [25].
ElasticModulus
The elastic modulus of the simulation is determined from
the volume averaged stress-strain response in the elastic
portion of initial loading. The elastic modulus predictions
as a function of α-Mo volume fraction at both room
temperature and 1400
◦C are presented in Fig. 3. Because
the elastic tensor properties of α-Mo are assumed to
be invariant with α-Mo Si content, the elastic modulus
predictions do not vary with α-Mo Si content. Each data
point in Fig. 3 represents the mean modulus calculated from
six instantiations of the same microstructural parameters.
The vertical bars represent two standard deviations of
the predicted elastic modulus over six instantiations. The
ellipsoidal packing algorithm does not precisely match the
target phase volume fractions. The horizontal bars reflect
two standard deviations of the final α-Mo volume fraction
over six instantiations.
Figure 3 shows that the volume averaged elastic modulus
is consistent between SVE instantiations targeting the same
Fig.2 Cyclic stress-strain response of three-phase Mo-Si-B SVE with
63% volume fraction α-Mo as a function of Si content at room
temperature
Fig.3 Predicted mean elastic modulus for six instantiations of each α-
Mo volume fraction with a Mo-0.00Si α-Mo CVP parameter set. Bars
represent two standard deviations
α-Mo volume fraction, despite the relatively large variation
in final volume fraction. Better control over the variation in
final α-Mo volume fraction requires a significant increase in
SVE volume. However, there is a clear and correct trend of
decreasing modulus with increasing α-Mo volume fraction.
Therefore, the volume element instantiations are considered
to be sufficiently accurate to the target volume fraction for
the purposes of this broad microstructure study.
YieldStrength
Yield strength is calculated as a 0.02% offset strength
from the volume averaged stress-strain response. Figure 4
presents the uniaxial yield strength predictions as a function
of α-Mo volume fraction and temperature for the Mo-
0.00Si and Mo-0.50Si α-Mo. As with the elastic modulus
predictions, the yield strength shows very little variation
as a function of instantiation at each combination of α-
Mo volume fraction and α-Mo Si content. The simulations
also capture the expected trends of decreasing strength with
increasing α-Mo volume fraction and decreasing strength
with increasing temperature.
Figure 5 presents the representative yield strength
predictions as a function of Si content and temperature at
63% α-Mo volume fraction. Except for the softening at
room temperature for small Si content, the yield strength
increases with increasing Si content at both temperatures.
Comparing Figs. 4 and 5, it is evident that the yield strength
of the three-phase material is more dependent on the Si
content of the α-Mo phase than on the α-Mo phase volume
fraction.

## Page 8

8 IntegrMaterManufInnov(2019)8:1–16
Fig.4 Predicted mean 0.02% offset yield strength for six instantiations
of each α-Mo volume fraction. Bars represent two standard deviations
FatigueResistance
Fatigue crack formation is controlled by the localized cyclic
response in the microstructure. The computational method
used to evaluate fatigue resistance compares the driving
force against critical driving force required for fatigue crack
formation. The driving force is measured through fatigue
indicator parameters (FIPs). The possible microstructure
dependence of the critical driving force for fatigue crack
formation is not addressed in this work. Consequently,
the results in this section can only be treated as direct
comparisons of fatigue resistance under the assumption that
the driving force for fatigue crack formation is strongly
dependent on microstructure, while the critical driving force
for crack formation is not dependent on microstructure.
Fig.5 Predicted mean 0.02% offset yield strength for six instantiations
of each α-Mo Si content at 63% volume fraction α-Mo. Bars represent
two standard deviations. Note the stronger dependence of yield stress
on α-Mo Si content than on α-Mo phase volume fraction
Two FIPs are used in this study, the Fatemi-Socie
(FS) parameter and the effective cumulative plastic strain
(ECPS), which have been shown to correlate well with
both low and high cycle fatigue [ 43, 57–60]. The effective
cumulative plastic strain parameter accounts for cyclically
accumulated plastic strain and the Fatemi-Socie parameter
includes the effects of normal stress at fatigue crack
formation sites. The FIPs are calculated from the stress-
strain response of a single, fully reversed fatigue cycle with
a macroscopic mechanical strain amplitude of 0.5%. The
calculation is performed at each integration point prior to
performing a local volume average over a grain volume,
which is consistent with the volume involved in fatigue
crack formation in similar brittle material systems. In this
work, the local volume averaging is performed using a
Gaussian filter where the length scale is adjusted by setting
the standard deviation of the filter to half of the mean α-Mo
equivalent grain radius.
Due to the localization problem of fatigue crack
formation, a proper treatment of fatigue requires several
hundred SVE instantiations for each combination of
microstructural parameters, α-Mo CVP parameter set, and
loading conditions [ 43, 47]. Approaching such a study
with crystal plasticity is computationally expensive, so
recent efforts have pursued reduced-order methods instead
[61]. The breadth of microstructures in this study limits
the fatigue resistance analysis to a small number of
SVEs and a single loading condition. Instead of the usual
extreme value approach, this study presents the results
of instantiation volume averaged FIPs to capture the
general trends microstructure effects for the purposes of
efficient, multi-property, microstructure optimization with

## Page 9

IntegrMaterManufInnov(2019)8:1–16 9
the understanding that a more complete fatigue study will
be required as the microstructure optimization is refined.
Figure 6 presents the mean and standard deviation of six
instantiations for the volume average FIPs as a function of
α-Mo volume fraction for Mo-0.00Si and Mo-0.50Si. Note
that for FIPs, a larger value represents greater damage per
cycle and therefore less fatigue resistance.
Figure 6a shows that both FIPs predict increasing damage
per cycle with increasing α-Mo volume fraction at room
temperature. This is explained by greater amounts of cyclic
plasticity present in the volume due to a larger volume
fraction of the plastically deformable α-Mo phase. At
1400
◦C, both FIPs initially increase with increasing α-Mo
volume fraction, but transition to decreasing with increasing
α-Mo volume fraction at higher α-Mo volume fractions.
This indicates a re-distribution in the strain fields at higher
Fig.6 Predicted mean volume averaged FIPs for six instantiations of
each α-Mo volume fraction. Bars represent two standard deviations
α-Mo volume fractions where plastic strain accumulation
is less severe, resulting in lower FIP calculations across
the SVE on average. The predicted α-Mo volume fraction
where the trend changes is 74% for ECPS and 54% for
FS. The difference in transition point for ECPS and FS is
likely related to the effects of normal stress, indicating a
transition to lower normal stresses at crack formation sites
that decreases the FS parameter before the ECPS parameter.
In Fig. 6a, the unusually large variation of the mean
volume average ECPS prediction for 63% α-Mo volume
fraction is the result of a single instantiation with a
much lower volume average ECPS. This large difference
does not show up at room temperature, and if the
instantiation is excluded from the mean and standard
deviation calculations, the resulting standard deviation more
closely resembles that of all the other predictions on this
plot.
The change in variation from room temperature to
1400
◦C is accompanied by a shift in the location where
the largest maximum valued ECPS is predicted within
the outstanding instantiation. Most instantiations predict
that the maximum valued FIPs remain in the same grain
as a function of temperature, but in this case the grain
with the maximum valued ECPS is different at room
temperature and 1400
◦C. This change in location suggests
that the microstructural feature driving fatigue damage
has changed with changing temperature. In this case, it
is speculated that the outstanding instantiation contains
a favorable misorientation distribution that tends to more
evenly distribute the accumulated plastic strain.
Figure 7 presents the same volume average FIP
predictions as a function of α-Mo Si content and
Fig. 7 Predicted mean volume average FIPs for six instantiations of
each α-Mo Si content at 63% volume fraction of α-Mo. Bars represent
two standard deviations. Note the stronger dependence of FIPs on
α-Mo Si content than on α-Mo phase volume fraction

## Page 10

10 IntegrMaterManufInnov(2019)8:1–16
temperature at 63% α-Mo volume fraction. The other α-Mo
volume fractions show the same trends as a function of Si
content. At room temperature, the solid solution softening
demonstrated by α-Mo at 0.1 wt% Si results in increased
plasticity and an increase in FIP over pure Mo. Subsequent
increases in Si content result in decreasing FIP , where the
FIP at 0.25 wt% Si is slightly less than for pure Mo. At
1400 ◦C, increasing Si content results in decreasing FIP .
While less obvious than in the yield strength plots, Figs. 6
and 7 show that the FIPs have a stronger dependence on
α-Mo Si content than on α-Mo phase volume fraction.
When comparing the FIP trends as a function of Si
content, it is important to remember that these predictions
do not necessarily reflect changes in fatigue resistance.
Particularly in the case of Mo-0.00Si, it is possible that the
critical driving force required for fatigue crack formation
is significantly larger than that for α-Mo containing
Si. For a more definitive characterization of fatigue
resistance, fatigue experiments are required to establish
how fatigue resistance changes with α-Mo Si content.
However, the results of these simulations provide insight
into the microstructure-sensitive fatigue crack driving force,
reducing the number of fatigue experiments required.
SusceptibilitytoMicrocracking
Reduced-OrderMeasure
Modeling tools for predicting the influence of microstruc-
ture variation on the susceptibility to brittle microcrack for-
mation in fully 3D simulations are computationally expen-
sive, particularly when modeling weak interfaces with cohe-
sive zone elements in finite element solvers. These tools are
less practical for use in microstructure optimization studies
with large numbers of simulations spanning large changes
in microstructure. It is desirable to develop a reduced-order
measure of susceptibility to brittle microcrack formation
that can be calibrated from more detailed microstructural
models and used in the optimization of mechanical prop-
erties as a function of microstructure. Therefore, a new
damage indicator parameter (DIP) suitable for use as a
quantitative reduced-order indicator of damage formation
is developed and validated against cohesive zone element
simulations [40].
The method is developed by running two sets of
parallel 2D simulations, one with and one without the
use of cohesive elements, to evaluate the suitability of a
reduced-order DIP for indicating relative susceptibility to
brittle microcracking between microstructures. The chosen
damage law for the development of a DIP is the same
irreversible, bilinear traction-separation damage law used
in the cohesive element simulations and shown in Fig. 8
Fig.8 Bilinear traction-separation CZM
[53, 62]. This cohesive element damage law has been used
previously to investigate structure-property relationships in
three-phase Mo-Si-B alloys [ 36], and the development of
the DIP follows upon this foundation. The cohesive element
model form is
t
i = k′δi = (1 − d) kδi (3)
where ti is the traction on the ith direction, k′ is the
effective stiffness of a cohesive element, δi is the relative
displacement or separation between faces of the cohesive
element, d is the isotropic damage variable, and k is the
original, undamaged stiffness of the cohesive element.
The relevant damage law for this bilinear traction-
separation cohesive zone model is
d =
⎧
⎪⎪
⎪⎪⎨
⎪⎪⎪⎪
⎩
0; δ
max
i ≤ δ0
i
δf
i
(
δmax
i − δ0
i
)
δmax
i
(
δf
i − δ0
i
) ; δ0
i <δ max
i ≤ δf
i
1; δmax
i >δ f
i
(4)
where d is the damage of the cohesive element ranging
from zero to one where unity represents a completely failed
element, δmax
i is the maximum effective displacement of the
loading history and is required to be positive to maintain
irreversible damage, δ0
i is the initial effective displacement
when damage starts, and δf
i is the effective displacement for
final failure of the cohesive element.
Damage formation is defined by a maximum nominal
stress criterion given in three dimensions by
max
{ ⟨tn⟩
t0n
, |ts|
t0s
, |tt|
t0
t
}
= 1( 5 )
where the angled brackets, ⟨⟩, are Macaulay brackets, tn
is the normal traction, ts and tt are the shear tractions in
the 3D case, and the superscript 0 refers to the traction
required to initiate damage. With this damage formation
criterion, the subscript i in Eq. 4 refers to the direction of

## Page 11

IntegrMaterManufInnov(2019)8:1–16 11
displacement. In the 2D plane strain case, this corresponds
to the normal direction and one shear direction. The damage
criterion relates the damage formation displacement to the
appropriate traction as
δ
0
i = t0
i
k (6)
where t0
i is the nominal stress at the initiation of decohesion
in the ith direction and k is the cohesive zone element
stiffness. Using a maximum nominal stress criterion,
damage is calculated separately for the normal and shear
directions. The final damage used in Equation 3, d,i s
assigned according to the maximum value from the separate
normal and shear damage calculations as
d = max {d
n,d s} (7)
where dn and ds are the damage calculated from the normal
and shear stresses, respectively. Calibration of the cohesive
zone model can be found in the work of Patra et al. [ 36].
Without cohesive zone elements, the DIP must be
calculated from the local stress-strain field during post-
processing. The damage calculation is carried out on the
elements on either side of a location where cohesive zone
elements would normally be placed using the properties and
local strain tensor of that element. The largest calculated
damage between two elements making up an interface is
then assigned to that interface as
d
j = max
{
dj1,d j2
}
(8)
where dj is the damage of the j th interface, dj1 is the
damage calculated for the first element making up the
interface, and dj2 is the damage calculated for the second
element making up the interface.
For this study, the locations of interest are the α-Mo/A15
and α-Mo/T2 grain boundaries and the intermetallic grains,
which were found to be the competing crack propagation
paths in two- and three-phase Mo-Si-B alloys [11, 36,
63, 64]. However, predicting the location of cracking in
the intermetallic grains without introducing an additional
constitutive law governing crack location is difficult without
cohesive elements. For preliminary development of the DIP ,
choosing and calibrating an additional constitutive law were
not feasible. Instead, intermetallic cracking is neglected
in order to simplify the exercise of developing a reduced
order quantitative DIP . This approach is justified by the
preferred intergranular cracking observed in both two- and
three-phase Mo-Si-B alloys [ 17, 63–65].
For comparing damage between microstructures, the
total damage present in the SVE is calculated from the
damage of individual interfaces. Since the damage is only
calculated at the α-Mo/intermetallic grain boundaries, an
interface average damage may be calculated over the
interfaces as
DIP
avg =
∑ NMo/Inter
j=1 dj
NMo/Inter
(9)
where DIPavg is a measure of the mean damage over all
α-Mo/intermetallic interfaces within the SVE, NMo/Inter
is the total number of interfaces of interest, and dj is the
damage at the j th interface of interest. DIPavg represents
the mean damage of the interfaces which are allowed to
initiate damage within a single SVE instantiation and has
a range of zero to one, with one representing a complete
failure of additional load bearing capacity. A simulation
with a larger DIP
avg at a fixed macroscopic strain would
be more likely to develop widespread cohesive element
failure in a cohesive simulation. Therefore, a larger DIPavg
indicates a greater susceptibility to microcrack formation.
A mean value metric is chosen for comparison over
localization metrics, such as the extreme values of local
damage d
j , for two reasons: (1) to capture the dependence
of fracture on widespread cracking, crack percolation, and
crack coalescence and (2) to reduce the computational cost
of the large number of instantiations required to properly
evaluate extreme value statistics. The full development and
validation of the DIP
avg as a quantitative reduced-order
measure of susceptibility to microcracking are developed
elsewhere [40].
The validation of the approach is made by calculating
the interface average DIP
avg for both the cohesive and
non-cohesive simulations. Figure 9 compares the results of
Fig.9 Predicted mean DIPavg of ten instantiations calculated at 1%
macroscopic strain. Bars represent two standard deviations

## Page 12

12 IntegrMaterManufInnov(2019)8:1–16
these simulations as a function of α-Mo volume fraction.
Each data point represents the mean of ten instantiations
for the same microstructure, and the error bars correspond
to two standard deviations. The calculation is performed
at 1% macroscopic strain to show the deviation in the
DIP
avg of the non-cohesive simulations from the DIPavg
of the cohesive simulations. This macroscopic strain is
approximately 10 times the yield strain and corresponds to
the point where widespread cohesive zone element failure
has not quite begun for the majority of the simulations.
From Fig. 9,t h eDIP
avg shows the expected trends
of decreasing susceptibility to brittle microcracking with
increasing α-Mo volume fraction. The DIPavg is inversely
correlated with the strain at the maximum tensile stress of
the cohesive simulations, which is an indicator of ductility.
Thus, the DIP
avg correctly indicates increasing ductility
with increasing α-Mo volume fraction.
As cohesive elements fail in the cohesive simulations,
they leave behind cracks with free surfaces, which are
traction free. The stress is redistributed around the cracks
in the cohesive simulations but not in the non-cohesive
simulations, causing differences in the stress and strain
fields. Since the local damage, d
j , is calculated from the
traction at the interface elements where cohesive elements
are failing, the traction free surfaces in the cohesive
simulations reduce the calculated local damage with respect
to the non-cohesive simulations. In Fig. 9, the failure of
a large number of cohesive elements and the resulting
free surfaces are the reason for the difference between the
DIP
avg of the cohesive and non-cohesive simulations at
52.5% volume fraction α-Mo.
Although the volume average approach with DIPavg is
shown to yield good results for ranking relative susceptibil-
ity to microcracking, it is anticipated that a more thorough
development of the DIP may extend the usefulness of this
approach. If the DIP is evaluated according to extreme value
statistics and includes the effects of spatial distribution of
microcrack formation, it may be possible to capture the
percolation threshold of crack coalescence. Such a develop-
ment would enable use of the DIP to build more detailed
structure-property linkages by identifying microstructure
characteristics driving microcrack coalescence and the limit
of load bearing capacity.
This approach was developed with the intention to reduce
computational cost with respect to cohesive zone elements.
In the 2D simulations used to develop the DIP , removing
the cohesive zone elements reduced computation time by
a factor of 2 to 4. Although a direct comparison was not
conducted in 3D, it would be expected to see even greater
computation time savings. The fully 3D three-phase Mo-
Si-B simulations often required 15 h to complete using 16
cpus. With over 200 simulations in the parametric study, this
represents a significant reduction in computational cost.
ParametricStudyResults
The prediction of susceptibility to microcracking in 3D,
three-phase Mo-Si-B simulations was evaluated using the
volume averaged DIP
avg , calculated at 0.5% macroscopic
uniaxial strain. A larger value for DIPavg indicates greater
susceptibility to damage formation and is an indicator of a
decrease in ductility and damage tolerance. Although the
dependence of critical driving force is addressed in the
calibration of interface strengths as a function of Si content
[36], it is possible that the critical crack driving force
depends on additional microstructural features. Therefore,
comparing the susceptibility to microcracking with the
DIP
avg metric requires the assumption that the critical
driving force is solely dependent on α-Mo Si content.
Figure 10 presents DIPavg as a function of α-Mo
volume fraction at room temperature and 1400 ◦Cf o rM o -
0.00Si. Figure 10 clearly shows the trends for DIPavg
as a function of increasing α-Mo volume fraction at
Mo-0.00Si and the same trends are seen at each α-
Mo Si content. DIPavg is larger at room temperature
than at 1400 ◦C, which is expected since most materials
demonstrate more ductility at high temperatures. At room
temperature, DIP
avg demonstrates a shallowly decreasing
damage with increasing α-Mo volume fraction. At 1400 ◦C,
the same trend is seen, but the decrease in damage is
more significant with increasing α-Mo volume fraction.
The same general trends hold for Mo-0.10Si through Mo-
1.00Si; however, the differences between room temperature
and 1400
◦C DIPavg decrease with increasing alpha-Mo
Si content. Additionally, with increasing Si content the
decrease in damage with increasing α-Mo volume fraction
becomes less significant.
Fig. 10 Predicted mean DIPavg of six instantiations for each α-Mo
volume fraction with a Mo-0.00Si CVP parameter set. Bars represent
two standard deviations

## Page 13

IntegrMaterManufInnov(2019)8:1–16 13
Fig.11 Predicted mean DIPavg of six instantiations for each α-Mo Si
content at 63% volume fraction of α-Mo. Bars represent two standard
deviations. Note the stronger dependence of DIPavg on α-Mo Si
content than on α-Mo phase volume fraction
Figure 11 clearly shows the trends in DIPavg as a
function of Si content at 63% α-Mo volume fraction. These
trends are consistent for each α-Mo volume fraction. There
is a steep increase in DIPavg from pure Mo with the
addition of 0.1 wt% Si, corresponding to a decrease in
relative ductility. This large jump in DIPavg is more severe
at 1400 ◦C than at room temperature. From 0.10 to 1.00 wt%
Si, DIPavg steadily increases, with smaller increases
between the higher Si content α-Mo CVP parameter sets.
In fact, at room temperature, DIPavg is nearly invariant
between 0.50 and 1.00 wt.% Si in α-Mo. Figures 10 and 11
show that the DIP has a stronger dependence on α-Mo Si
content, particularly at low Si content, than onα-Mo volume
fraction.
ModelValidation
The α-Mo model development includes stress-strain and
yield strength comparisons to the limited experimental
data available [40]. There is limited availability of stress-
strain behavior of fully characterized two- and three-
phase Mo-Si-B materials with usable strain measurements
in the range used in this study. However, a reasonable
comparison of yield strength data can be made against
two experimental studies of three-phase Mo-Si-B alloys.
Tables 7 and 8 present a comparison of the three-phase
Mo-Si-B simulations with the yield strength and available
characterization of similar three-phase Mo-Si-B materials
from literature [ 14, 16, 23]. Table 7 also includes modulus
comparisons [14, 16].
A relatively recent study on the fabrication, strength,
and oxidation of Mo-Si-B alloys includes high-temperature
tensile tests of a three-phase Mo-Si-B alloy including the
α-Mo, A15, and T
2 phases [23]. However, the tensile
tests are performed without a strain measurement and are
uncorrected for the test frame compliance, so a direct
stress-strain comparison is not useful. An exact match of
the experimental microstructures are not included in the
parametric study; however, several simulations are close
enough to show that the three-phase Mo-Si-B simulations
fall in a similar range of strength values. The experimental
material has higher yield strengths than both the Mo-0.50Si
and Mo-0.75Si α-Mo calibrations for SVEs including 45%
and 54% α-Mo volume fraction. This is expected due to the
lower experimental test temperature and 0.2% offset yield
strength reported; however, a more direct set of simulations
would be required to more accurately compare to the
experimental material. The reported Si content of the α-Mo
phase is not measured directly, so a range of simulations
with varying α-Mo Si content would still be required for
comparison purposes.
Table 7 Comparison of Middlemas material yield strength to simulated three-phase Mo-Si-B predicted yield strength [ 23]
Parameter Simulation Middlemas [23]
0.02% offset σY (MPa) 313.5 446.1 287.1 414.9 419* 577* 477*
α-Mo vol. frac. (%) 45.0 45.0 54.0 54.0 47.8 47.8 67.2
A15 vol. frac. (%) 0.37 0.37 0.31 0.31 33.4 33.4 9.2
T2 vol. frac. (%) 0.18 0.18 0.15 0.15 18.8 18.8 27.3
α-Mo Si content (wt.%) 0.50 0.75 0.50 0.75 0.61** 0.61** 0.61**
Temperature (◦C) 1400 1400 1400 1400 1300 1200 1200
Strain rate
[
1
s
]
2.2×10−3 2.2×10−3 2.2×10−3 2.2×10−3 1.0×10−4 1.0×10−4 1.0×10−4
*0.2% offset yield strength reported
**A later study reported the Si content of this material closer to 1.3 wt% Si [ 18]

## Page 14

14 IntegrMaterManufInnov(2019)8:1–16
Table 8 Comparison of J ´ehanno et al. material yield strength to simulated three-phase Mo-Si-B predicted yield strength, continued [14, 16]
Parameter Simulation J´ehanno [14, 16]
Elastic modulus (GPa) 297.6 297.6 290.8 290.8 264 264 259 259
0.02% offset σY (MPa) 90.1 185.9 75.2 165.1 300* 64* 85* 27*
Max σ (MPa) – – – – 315 102 107 45
α-Mo vol. frac. (%) 45.0 45.0 54.0 54.0 50 50 50 50
A15 vol. frac. (%) 0.37 0.37 0.31 0.31 ? ? ? ?
T2 vol. frac. (%) 0.18 0.18 0.15 0.15 ? ? ? ?
α-Mo Si content (wt.%) 0.00 0.10 0.00 0.10 0.01** 0.01** 0.01** 0.01**
Temperature (◦C) 1400 1400 1400 1400 1300 1300 1400 1400
Strain rate [ 1
s ]2 .2×10−3 2.2×10−3 2.2 × 10−3 2.2×10−3 1.0×10−3 1.0×10−4 1.0 × 10−3 1.0×10−4
*Yield strength not reported and stress-strain plot has insufficient strain resolution for accurate 0.02% offset calculation
**As estimated by Patra et al. [ 36]
A more direct comparison can be made to a study on a
similar three-phase Mo-Si-B alloy from the work of J´ehanno
et al. [14, 16]. Unfortunately, only the volume fraction of
α-Mo is characterized. The relative volume fractions of the
A15 and T2 phase and the Si content of the α-Mo phase are
not characterized. The probable closest matching material
characteristics from this work are presented in Table 8,
where an estimation of the α-Mo Si content is taken from
Patra et al. [36]. The simulations of this work bounding the
α-Mo volume fraction and Si content of the expected values
for the J ´ehanno et al. material suggest that the Si content
estimate is reasonable and that the resulting three-phase Mo-
Si-B mechanical behavior is in reasonable agreement given
the unknowns in material characterization. The differences
in modulus as a function of temperature are likely a result of
the unknown volume fractions of intermetallics, but could
also result from the unknown texture of the J ´ehanno et al.
material.
SummaryandConclusions
Research into Mo-Si-B alloys has begun to yield promising
results towards using these alloys in gas turbine engines.
The work presented here advances the understanding of the
microstructure-property relationships of Mo-Si-B alloys by
developing and exercising a novel computational approach
to microstructure-sensitive mechanical property modeling
for Mo-Si-B alloys.
This paper demonstrates that several mechanical proper-
ties can be evaluated using a combination of modeling tools,
including elastic modulus, yield strength, fatigue resistance,
and susceptibility to microcracking. Three tools are used to
explore the microstructure-sensitive mechanical properties
of three-phase Mo-Si-B alloys: a microstructure generator,
a crystal viscoplastic constitutive law, and reduced-order
models for evaluating mechanical properties.
A novel damage indicator parameter (DIP) is developed
for use as a surrogate for susceptibility to brittle microcrack
formation without the use of cohesive elements. This
reduced-order modeling approach facilitates the design of
fully 3D microstructures using a quantitative measure for
relative interface average damage indicator as one of the
targeted design objectives in the optimization of multiple
mechanical properties.
A parametric study of three-phase Mo-Si-B alloys con-
taining the α-Mo, A15, and T
2 phases is presented to cap-
ture the microstructure-sensitive modulus, yield strength,
fatigue resistance, and susceptibility to microcracking
related to relative ductility. The parametric study explored
the effects of α-Mo Si content and phase volume frac-
tion. The yield strength predictions of the parametric study
are used to validate the constitutive model of three-phase
Mo-Si-B against similar experimental materials.
Since the susceptibility to brittle microcracking, espe-
cially at room temperature, is a critically important mechan-
ical property for the high-temperature structural applica-
tions of Mo-Si-B alloys, it is found that the Si content of
the α-Mo phase is more significant to the alloy’s balance of
mechanical properties than the α-Mo volume fraction. Con-
sequently, it is recommended that future development work
focus primarily on reducing or controlling the Si content of
the α-Mo phase. A balance of mechanical properties, then,
can be found between 55 and 63% α-Mo volume fraction
with as low an α-Mo Si content as possible. In this range
of α-Mo volume fraction, oxidation resistance requires fur-
ther study and must be included in future microstructure
optimization work.
These results agree with the findings of experimental
work on three-phase Mo-Si-B alloys. The significance of

## Page 15

IntegrMaterManufInnov(2019)8:1–16 15
this work is the development of an efficient computational
framework to explore the material design space of Mo-Si-B
alloys for multi-property optimization. This framework and
the predicted microstructure-property relationships could
be refined with additional experiments for calibration and
validation of single phase properties, especially for the
intermetallic phases. However, the benefit of this ICME
framework is the reduction in the number of experiments
required to explore the Mo-Si-B material design space.
There are several novel contributions in this work.
The crystal viscoplastic constitutive model used in this
study is the first crystal plasticity model developed for
three-phase Mo-Si-B alloys and the first crystal plasticity
model to include Si composition effects and temperatures
above 300
◦Co nt h eα -Mo phase. A novel reduced-order
quantitative damage indicator parameter (DIP) is developed
and used to compare susceptibility to microcracking as a
function of microstructure. The parametric study is also the
first quantitative multi-property microstructure optimization
of Mo-Si-B alloys.
Acknowledgments Special thanks to the points of contact during the
course of this work, Dr. Gopal Das, Rick Montero, and Dr. Shiela
Woodard.
Funding Information This work was supported by United Technolo-
gies Corporation, Pratt & Whitney Division.
Publisher’s Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
References
1. Bewlay BP, Jackson MR, Zhao JC, Subramanian PR (2003) A
review of very-high-temperature Nb-silicide-based composites.
Metall Mater Trans A 34A:2043–2052
2. Dimiduk DM, Perepezko JH (2003) Mo-Si-B alloys: developing
a revolutionary turbine-engine material. Mater Res Soc Bull
28:639–645
3. Lemberg JA, Ritchie RO (2012) Mo-Si-B alloys for ultrahigh-
temperature structural applications. Adv Mater 24:3445–3480
4. Mitra R (2006) Mechanical behaviour and oxidation resistance of
structural silicides. Int Mater Rev 51(1):13–64
5. Aryal S, Gao MC, Ouyang L, Rulis P, Ching WY (2013) Ab initio
studies of Mo-based alloys: mechanical, elastic, and vibrational
properties. Intermetallics 38:116–125
6. Perepezko JH (2009) The hotter the engine, the better. Science
326:1068–1069
7. Schneibel JH, Kramer MJ, ¨Unal O, Wright RN (2001) Processing
and mechanical properties of a molybdenum silicide with the
composition Mo-12Si-8.5B (at. %). Intermetallics 9:25–31
8. Parthasarathy TA, Mendiratta MG, Dimiduk DM (2002) Oxida-
tion mechanisms in Mo-reinforced Mo
5SiB2 ( T 2 )-M o3Si alloys.
Acta Mater 50:1857–1868
9. Alur AP, Chollacoop N, Kumar KS (2004) High-temperature
compression behavior of Mo-Si-B alloys. Acta Mater 52:5571–
5587
10. Alur AP, Sakidja R, Wang P, Jain P, Perepezko JH, Kumar KS
(2011) Deformation behavior of a quaternary Mo-Nb-Si-B alloy.
In: Materials research society symposium proceedings, vol 1295.
Materials Research Society, pp 355–360
11. Choe H, Chen D, Schneibel JH, Ritchie RO (2001) Ambient to
high temperature fracture toughness and fatigue-crack propagation
behavior in a Mo-12Si-8.5B (at. %) intermetallic. Intermetallics
9:319–329
12. Choe H, Schneibel JH, Ritchie RO (2003) On the fracture and
fatigue properties of Mo-Mo
3Si-Mo5SiB2 refractory intermetallic
alloys at ambient to elevated temperatures (25 ◦C to 1300 ◦C).
Metall Mater Trans A 34A(2):225
13. Jain P, Alur AP, Kumar KS (2006) High temperature compressive
flow behavior of a Mo-Si-B solid solution alloy. Scr Mater 54:
13–17
14. J ´ehanno P, Heilmaier M, Saage H, B ¨oning M, Kestler H,
Freudenberger J, Drawin S (2007) Assessment of the high
temperature deformation behavior of molybdenum silicide alloys.
Mater Sci Eng A 463:216–223
15. Jain P, Kumar KS (2010) Tensile creep of Mo-Si-B alloys. Acta
Mater 58:2124–2142
16. J ´ehanno P, Heilmaier M, Saage H, Heyse H, B ¨oning M, Kestler
H, Schneibel JH (2006) Superplasticity of a multiphase refractory
Mo-Si-B alloy. Scr Mater 55:525–528
17. Kumar KS, Alur AP (2007) Deformation behavior of a two-phase
Mo-Si-B alloy. Intermetallics 15:687–693
18. Lemberg JA, Middlemas MR, Weing ¨artner T, Gludovatz B,
Cochran JK, Ritchie RO (2012) On the fracture toughness of fine-
grained Mo-3Si-1B (wt.%) alloys at ambient to elevated (1300
◦C)
temperatures. Intermetallics 20:141–154
19. Liu CT, Schneibel JH, Heatherly L (1999) Processing, microstruc-
ture, and properties of multiphase Mo silicide alloys. In: Materi-
als research society symposium proceedings, vol 552. Materials
Research Society
20. Nieh TG, Wang JG, Liu CT (2001) Deformation of a multiphase
Mo-9.4Si-13.8B alloy at elevated temperatures. Intermetallics
9:73–79
21. Schneibel JH, Kramer MJ, Easton DS (2002) A Mo-Si-B
intermetallic alloy with a continuous α-Mo matrix. Scr Mater
46:217–221
22. Kruzic JJ, Schneibel JH, Ritchie RO (2005) Ambient- to elevated-
temperature fracture and fatigue properties of Mo-Si-B alloys: role
of microstructure. Metall Mater Trans A 36A:2393–2402
23. Middlemas MR (2009) Fabrication, strength and oxidation of
molybdenum-silicon-boron alloys from reaction synthesis. PhD
Dissertation, Georgia Institute of Technology, Atlanta, Georgia
24. Middlemas MR, Cochran JK (2008) Dense, fine-grain Mo-Si-B
alloys from nitride-based reactions. JOM, 19–24
25. Sturm D, Heilmaier M, Schneibel JH, J ´ehanno P, Skrotzki B,
Saage H (2007) The influence of silicon on the strength and
fracture toughness of molybdenum. Mater Sci Eng A 463:107–114
26. Bruckart WL, LaChance MH, Craighead CM, Jaffee RI (1953)
Properties of some hydrogen-sintered binary molybdenum alloys.
Trans Amer Soc Metals 45:286
27. Northcott L (1956) Molybdenum. Academic Press Inc., New Y ork
28. Saage H, Kr¨ uger M, Sturm D, Heilmaier M, Schneibel JH,
George E, Heatherly L, Somsen C, Eggeler G, Y ang Y (2009)
Ductilization of Mo-Si solid solutions manufactured by powder
metallurgy. Acta Mater 57:3895–3901

## Page 16

16 IntegrMaterManufInnov(2019)8:1–16
29. Swadener JG, Rosales I, Schneibel JH (2001) Elastic and plastic
properties of Mo 3Si measured by nanoindentation. In: Materials
research society symposium proceedings, vol 646. Materials
Research Society
30. Rosales I, Schneibel JH, Heatherly L, Horton JA, Martinez L,
Campillo B (2003) High temperature deformation of A15 Mo 3Si
single crystals. Scr Mater 48:185–190
31. Rioult FA, Imhoff SD, Sakidja R, Perepezko JH (2009) Transient
oxidation of Mo-Si-B alloys: effect of the microstructure size
scale. Acta Mater 57:4600–4613
32. Ito K, Ihara K, Tanaka K, Fujikura M, Y amaguchi M (2001)
Physical and mechanical properties of single crystals of the T 2
phase in the Mo-Si-B system. Intermetallics 9:591–602
33. Marshall PE (2015) Development of oxidation resistant
molybdenum-silicon-boron composites. PhD Dissertation,
Georgia Institute of Technology, Atlanta, Georgia
34. Daloz WL (2015) Developing a high temperature, oxidation resis-
tant molybdenum-silica composite. PhD Dissertation, Georgia
Institute of Technology, Atlanta, Georgia
35. Kruzic JJ, Schneibel JH, Ritchie RO (2005) Role of microstructure
in promoting fracture and fatigue resistance in Mo-Si-B alloys. In:
Materials research society symposium proceedings, vol 842
36. Patra A, Priddy MW, McDowell DL (2015) Modeling the
effects of microstructure on the tensile properties and micro-
fracture behavior of Mo-Si-B alloys at elevated temperatures.
Intermetallics 64:6–17
37. Przybyla CP (2010) Microstructure-sensitive extreme value
probabilities of fatigue in advance engineering alloys. PhD
Dissertation, Georgia Institute of Technology, Atlanta, Georgia
38. Groeber M, Ghosh S, Uchic MD, Dimiduk DM (2008) A frame-
work for automated analysis and simulation of 3d polycrystalline
microstructures. Part 2: synthetic structure generation. Acta Mater
56:1274–1287
39. Groeber MA, Jackson MA (2014) DREAM.3D: a digital
representation environment for the analysis of microstructure in
3d. Integrat Mater Manuf Innov 3:5
40. Brindley KA (2017) Microstructure-sensitive structure-property
modeling tools for triplex Mo-Si-B alloys. PhD Dissertation,
Georgia Institute of Technology, Atlanta, Georgia
41. Bachmann F, Hielscher R, Schaeben H (2010) Texture analysis
with MTEX - free and open source software toolbox. Solid State
Phenom 160:63–68
42. Hill R (1963) Elastic properties of reinforced solids: some
theoretical principles. J Mech Phys Solids 11(5):357–372
43. McDowell DL, Dunne FPE (2010) Microstructure-sensitive
computational modeling of fatigue crack formation. Int J Plast
32:1521–1542
44. Peirce D, Asaro RJ, Needleman A (1983) Material rate
dependence and localized deformation in crystalline solids. Acta
Metall 31(12):1951–1976
45. No AMC, Ortiz M (1992) Computational modelling of single
crystals. Model Simul Mater Sci Eng 1:225–263
46. Zhang M, Zhang J, McDowell DL (2007) Microstructure-based
crystal plasticity modeling of cyclic deformation of Ti-6Al-4V. Int
J Plast 23(8):1328–1348
47. Priddy MW, Paulson NH, Kalidindi SR, McDowell DL (2017)
Strategies for rapid parametric assessment of microstructure-
sensitive fatigue for hcp polycrystals. Int J Fatigue, 231–242
48. Armstrong PJ, Frederick CO (1966) A mathematical represen-
tation of the multiaxial bauschinger effect, Tech. Rep. GEGB
Report, RD/B/N731 Berkeley Nuclear Laboratories
49. Wronski AS, Johnson AA (1962) The deformation and fracture
properties of polycrystalline molybdenum. Philos Mag 7(74):213–
227
50. Orava RN (1964) Trans Metallur Soc AIME 230:1614
51. Lim H, Battaile CC, Carroll JD, Boyce BL, Weinberger CR (2015)
A physically based model of temperature and strain rate dependent
yield in BCC metals: implementation into crystal plasticity. J
Mech Phys Solids 74:80–96
52. Y alcinkaya T, Brekelmans W AM, Geers MGD (2008) BCC single
crystal plascticity modeling and its experimental identification.
Model Simul Mater Sci Eng 16:1–16
53. Dassault Systemes: Abaqus v. 6.11-1. 2011. Providence, RI, USA
54. Brindley KA, Neu RW (2015) Progress in structure-property
modeling tools for γ -TiAl. In: Symposium on high performance
aerospace alloys design using ICME approach, (Orlando, FL,
USA), the minerals, metals, and materials society. Wiley, pp
1173–1183
55. Dickinson JM, Armstrong PE (1967) Temperature dependence of
the elastic constants of molybdenum. J Appl Phys 38:602–606
56. Biragoni PG, Heilmaier M (2007) FEM-simulation of real and
artificial microstructures of Mo-Si-B alloys for elastic properties
and comparison with analytical methods. Adv Eng Mater
9(10):882–887
57. Suresh S (1998) Fatigue of materials, 2 edn. Cambridge University
Press
58. Manonukul A, Dunne FPE (2004) High- and low-cycle fatigue
crack initiation using polycrystal plasticity. R Soc 460:1881–1903
59. Dunne FPE, Wilkinson AJ, Allen R (2007) Experimental and
computational studies of low cycle fatigue crack nucleation in a
polycrystal. Int J Plast 23:273–295
60. Socie D (1993) Critical plane approaches for multiaxial fatigue
damage assessment. In: McDowell DL, Ellis R (eds) Advances
in multiaxial fatigue, ASTM STP 1191. American Society for
Testing and Materials, pp 7–36
61. Paulson NH, Priddy MW, McDowell DL, Kalidindi SR (2018)
Data-driven reduced-order models for rank-ordering the high
cycle fatigue performance of polycrystalline microstructures.
Mater Des 154:170–183
62. Camanho PP, D ´avila CG (2002) Mixed-mode decohesion finite
elements for the simulation of delamination in composite
materials. Tech. Rep. TM-2002-211737 NASA
63. Alur AP, Kumar KS (2006) Monotonic and cyclic crack growth
response of a Mo-Si-B alloy. Acta Materiala 54:385–400
64. Kumar S, Alur AP (2007) Crack growth behavior in a two-phase
Mo-Si-B alloy, vol 980 of materials research society symposia pro-
ceedings. Materials Research Society Cambridge University Press
65. Y u JL, Li ZK, Zheng X, Zhang JJ, Liu H, Bai R, Wang H
(2012) Tensile properties of multiphase Mo-Si-B refractory alloys
at elevated temperatures. Mater Sci Eng A 532:392–395
