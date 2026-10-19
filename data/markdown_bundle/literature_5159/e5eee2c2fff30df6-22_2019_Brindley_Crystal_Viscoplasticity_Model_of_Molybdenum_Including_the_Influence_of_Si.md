# 22_2019_Brindley_Crystal_Viscoplasticity_Model_of_Molybdenum_Including_the_Influence_of_Silicon_in_Solid_Solution

<!-- source: D:\总文献\22_2019_Brindley_Crystal_Viscoplasticity_Model_of_Molybdenum_Including_the_Influence_of_Silicon_in_Solid_Solution.pdf -->
<!-- file_sha256: 4d03b298b89285cb4cd709c8586c07ff95aad6158c5fcaf2047e62c9c1f46347 -->

## Page 1

LA-UR-18-21658 (Accepted Manuscript)
Crystal Viscoplasticity Model of Molybdenum Including the Influence of
Silicon in Solid Solution
Brindley, Kyle Andrew
Neu, Richard W
Provided by the author(s) and the Los Alamos National Laboratory (2019-07-12).
To be published in: Materials Performance and Characterization
DOI to publisher's version: 10.1520/MPC20190040
Permalink to record: http://permalink.lanl.gov/object/view?what=info:lanl-repo/lareport/LA-UR-18-21658
Disclaimer:
Los Alamos National Laboratory, an affirmative action/equal opportunity employer, is operated by Triad National Security, LLC for the National
Nuclear Security Administration of U.S. Department of Energy under contract 89233218CNA000001. By approving this article, the publisher
recognizes that the U.S. Government retains nonexclusive, royalty-free license to publish or reproduce the published form of this contribution, or
to allow others to do so, for U.S. Government purposes. Los Alamos National Laboratory requests that the publisher identify this article as work
performed under the auspices of the U.S. Department of Energy. Los Alamos National Laboratory strongly supports academic freedom and a
researcher's right to publish; as an institution, however, the Laboratory does not endorse the viewpoint of a publication or guarantee its technical
correctness.

## Page 2

Crystal Viscoplasticity Model of Mo Including the Inﬂuence of
Si in Solid Solution
K. A. Brindley 1, R. W. Neu 1,2,∗
1The George W. Woodruﬀ School of Mechanical Engineering, 801 Ferst Drive, Georgia
Institute of Technology; Atlanta, GA, 30332, USA
2School of Materials Science and Engineering, 771 Ferst Drive, Georgia Institute of
Technology; Atlanta, GA, 30332, USA
∗Corresponding Author: rick.neu@me.gatech.edu
Keywords: molybdenum, constitutive model, Mo-Si-B, materials design,
structure-properties relations
Abstract
Mo-based alloys oﬀer higher temperature capability than Ni-base superalloys. The chal-
lenge of designing these alloys is tailoring the chemistry and microstructure to achieve
high temperature strength, creep and fatigue resistance, oxidation resistance while main-
taining lower temperature ductility and damage tolerance. Structure-properties modeling
tools can be used to identify optimum microstructures. However, one missing element
in this tool set is a constitutive model for the more ductile α-Mo phase over the entire
temperature range from room temperature to 1400 ◦C. A crystal viscoplasticity model is
developed for α-Mo including the inﬂuence of varying amounts of Si in solid solution.
The temperature, strain rate, and Si dependence of the deformation behavior needed to
determine the model parameters is obtained from new compression experiments.
Introduction
Refractory metals and their alloys oﬀer higher temperature alternatives to Ni-base su-
peralloys [1–5]. For example, Mo-Si-B alloys oﬀer oxidation and creep resistance at tem-
peratures up to 1300 ◦C [3,6,7]. The microstructure generally consists of an α-Mo phase
and two intermetallic phases, e.g. Mo5SiB2 (T2) and Mo3Si (A15). The borosilicides pro-
mote the formation of a passivation layer on the exposed surfaces resulting in improved
1 of 25

## Page 3

oxidation resistance. However, the intermetallics present a signiﬁcant design challenge
due to their low ductility and low fracture toughness at room temperature [3]. A bal-
ance of high temperature and low temperature mechanical properties may be achieved
in Mo-Si-B alloys by designing a microstructure containing the more ductile α-Mo phase
with the intermetallic phases [3,6,7].
In alloys based on borosilicides of Mo, the α-Mo phase may have Si in solid solution,
where the Si content can be controlled by processing to some extent. This body-centered
cubic (BCC) phase is key to providing the ductility and fracture toughness in Mo-Si-B
alloys; however, it oxidizes readily above 600 ◦C and has poor creep resistance at high
temperatures [3, 8]. The strength of the α-Mo phase is highly dependent on Si content,
where small additions of Si can dramatically increase the yield strength [8]. However,
adding Si also decreases the fracture toughness and ductility. It has been shown that the
addition of 0.5 wt.% Si will reduce the room temperature ductility of α-Mo from 25% to
3% [9,10].
Before multiphase Mo-Si-B alloys can be adopted the microstructure must be opti-
mized to provide a balance of mechanical properties over a wide temperature range. In-
tegrated Computational Material Engineering (ICME) tools can reduce the time, money,
and eﬀort required to optimize material microstructures; however, ﬁrst constitutive mod-
els of the constituent phases must be developed that capture the eﬀects of chemistry,
microstructural features, and environment on mechanical behavior. Several plasticity
models have been used to predict microstructure-sensitive properties for Mo-Si-B al-
loys [11, 12]; however, they do not include the anisotropic nature of the constituent
phases. A macroscopic model of polycrystalline Mo that accounts for both elastic and
plastic anisotropy over a wide range of strain rates has been developed, but this model
does not account for the eﬀects of Si composition or allow for microstructure-sensitive
property prediction [13, 14]. One approach to modeling microstructure-sensitive prop-
erties in polycrystals is the visco-plastic self-consistent (VPSC) method [15] which has
been used to model BCC polycrystalline metals [16] and thin Mo sheets at relatively low
2 of 25

## Page 4

temperatures [17]. Another approach to modeling microstructure-sensitive properties is
crystal plasticity. Two crystal-plasticity constitutive models for BCC metals have been
calibrated for Mo [18,19]; however, they do not include the eﬀects of Si composition and
are not calibrated to the high temperatures commonly seen by the Ni-base superalloy
components that Mo-Si-B alloys are intended to replace. The work presented in this
paper develops and calibrates a crystal plasticity constitutive model for the α-Mo phase
as a function of Si composition, temperature, and strain rate suitable for microstructure-
sensitive mechanical property prediction.
Constitutive Model
The ultimate goal of this work is to produce a constitutive model suitable for multi-
property materials design of three-phase Mo-Si-B alloys. This work focuses on a missing
element to ICME design tools for such alloys, a constitutive model for the α-Mo phase
that is temperature, strain rate, and Si content dependent. The constitutive model for
the α-Mo phase developed in this work consists of both fully anisotropic elasticity and
crystal viscoplasticity. For the crystal viscoplasticity model, the slip rule is based on the
shear strain rate relation
˙γα = ˙γ0
⟨|τα−χα|− κα
Dα
⟩ 1
m
sgn (τα−χα) (1)
whereα is a slip system index, ˙γα is the inelastic shear strain rate on theαth slip system,
˙γ0 is the reference inelastic shearing rate, τα is the resolved shear stress on the αth
slip system, and χα, κα, and Dα are the current values of back stress, threshold stress,
and drag stress on the αth slip system, respectively. The ⟨⟩ brackets are MacCauly
brackets andsgn () returns positive or negative unity, depending on the sign of the term
in parentheses. The variable m in the exponent is the strain rate sensitivity exponent.
Both ˙γ0 and m are material parameters that are typically treated as constants, but can
vary with microstructure and temperature in general. For the α-Mo phase, it is assumed
3 of 25

## Page 5

that the 12{100}⟨111⟩ and 12{112}⟨111⟩ BCC slip systems are active. Since no single
crystal information is available for the α-Mo phase to individually calibrate each slip
system, all 24 slip systems are treated equally.
Back stress, threshold stress, and drag stress may all evolve over the course of loading.
Depending on the material under consideration, many diﬀerent types of equations have
been used for the evolution of back stress, threshold stress, and drag stress. For back
stress and drag stress, the most common evolution equations follow the direct hardening,
dynamic recovery form of the Armstrong-Frederick equations [20].
For theα-Mo phase, the drag stress is treated as a non-evolving constant dependent
on temperature and Si content and back stress evolves as
˙χα =B ˙γα−Cχα⏐⏐ ˙γα
⏐⏐ (2)
where B and C are functions of temperature and Si content. The reference inelastic
shearing rate ˙γ0 is also a function of temperature and Si content and the strain rate
sensitivity exponent m is a function of Si content. The threshold stress κα can also be
an evolving function of temperature, Si content, and grain size; however, this parameter
is not used since the drag stress parameter was suﬃcient to capture the yield response
as a function of temperature and Si content.
The strain rate sensitivity exponent accounts for diﬀerences in yield strength as a
function of strain rate, and back stress evolution is used to calibrate the plastic hardening
behavior. Because the available stress-strain response of α-Mo is limited to monotonic
uniaxial compression and tension tests, no calibration can be made for the cyclic response.
However, a cyclic model is required for the ultimate goal of multi-property optimizations
that include fatigue resistance. Therefore, it is assumed that the material is cyclically
stable and the stabilized hysteresis curve can be obtained from the monotonic calibration.
This assumption requires a purely kinematic hardening model and amounts to assuming
that there is no cyclic hardening or softening of the material when modeling fatigue.
4 of 25

## Page 6

Until cyclic experiments are available, this assumption provides the means to perform
coarse multi-property optimizations that include fatigue resistance and provide early
microstructure optimization guidance across a wide range of microstructures. Once cyclic
experiments become available, this assumption should be re-visited and the model re-
calibrated to obtain more accurate fatigue resistance predictions.
The constitutive equation is implemented as a User Material subroutine (UMAT) for
the general purpose ﬁnite element code ABAQUS [21]. The speciﬁc Fortran code used in
this work is based on previous work for γ-TiAl alloys [22] and has been modiﬁed for α-
Mo by adding the appropriate slip systems, evolution equations, the evolution equation
derivatives, and temperature dependence for the elastic properties.
Elastic Properties
The fully anisotropic elasticity tensors for α-Mo are obtained from literature data [23].
The elasticity tensor components for Mo are shown in Figure 1. The elasticity tensor is
known from room temperature to 700 ◦C [23]. To use the constitutive model at higher
temperatures, this data is ﬁt with a linear regression and extrapolated to 1400 ◦C. The
regression coeﬃcients can be found in Table 1. Although the constitutive model focuses
on the eﬀects of Mo with Si in solid solution, it has been shown that the addition of Si
has very little eﬀect of the elastic modulus [8]. Consequently, the assumption that the
elastic properties of α-Mo are invariant with respect to Si content is reasonable.
Figure 1: α-Mo anisotropic elasticity tensor components as a function of temperature.
Data points from reference [23]. Lines represent the linear regression and extrapolation.
5 of 25

## Page 7

Table 1: Elasticity tensor component regressions for α-Mo as a function of
temperature [ ◦C]: y =Mx +b
C11 C12 C44
M -0.0578 0.0058 -0.0102
b 463.0 157.5 109.1
α-Mo Characterization
To calibrate the crystal viscoplasticity model for theα-Mo phase as a function of temper-
ature and Si content, as-cast arc melted buttons with varying Si content were prepared
from high purity elemental powders by Pratt & Whitney to provide single phase α-Mo
material without precipitates. No additional heat treatment was performed on this ma-
terial, so the microstructure is unreﬁned and contains regions of textured, elongated
grains.
Compression tests, using specimens cut from the arc-meltedα-Mo buttons, were con-
ducted by Pittsburgh Materials Technology. Tests were conducted at room temperature,
600◦C, 1100 ◦C, and 1400 ◦C and two strain rates approximately two orders of magni-
tude apart: 1 .66× 10−4 s−1 and 2.77× 10−2 s−1 for each Si content ranging from pure
Mo to Mo with 0.29, 0.40, 0.58, and 1.16 wt.% Si. Since Mo readily oxidizes above
600◦C [3], all tests above room temperature were conducted in a vacuum. There was
insuﬃcient material for duplicate test specimens, so a single test was conducted for each
test condition.
The test specimens were cut as rectangular prisms with dimensions that varied be-
tween specimens but was nominally 5.1 mm in width and depth and 7.6 mm tall. The
full measurements for each specimen were recorded before and after testing. Specimens
were compressed between two platens and the axial force and cross-head displacement
were measured throughout the test. It was not possible to directly measure the strain
in the gage section due to the diﬃculty of performing strain measurements at high tem-
6 of 25

## Page 8

peratures in a vacuum. The high strength of the Mo-1.16Si (wt.%) samples broke a
test ﬁxture and required a special high strength ﬁxture, especially at room temperature.
Consequently, the compression tests were not conducted to specimen failure, but were
stopped after yield was obtained and at least 3% strain. A representative engineering
stress-strain curve from the Mo-0.40Si material is shown in Figure 2.
Figure 2: Engineering stress-strain curves for Mo-0.40Si experiments.
OIM was performed to characterize the arc melted α-Mo material. Figure 3 shows
an EBSD map of a sample of α-Mo with 0.40 wt.% Si (Mo-0.40Si), including an overlay
of the approximate specimen size. The arc melted α-Mo specimen microstructures vary
with Si content. Due to the heterogeneous, anisotropic microstructure and the variety
of microstructures in material with diﬀering Si content, extra care was taken to properly
characterize and model the arc melted α-Mo material to obtain a suitable calibration of
the constitutive model from the measured macroscopic compression deformation.
Figure 3: EBSD map of arc melted α-Mo material: Mo-0.40Si (wt%). The columnar
region mean grain size is approximately 890 µm and the bottom region mean grain size
is approximately 320 µm.
The grain sizes of roughly 300 to 900 µm in the arc-melted samples were much larger
than the grain sizes of typical three-phase Mo-Si-B microstructures that this modeling
eﬀort ultimately targets. Typical three-phase Mo-Si-B alloys have grain sizes closer to
10 µm for the α-Mo phase and 8 µm for the intermetallic phases [24, 25]. This large
diﬀerence in grain size requires additional modeling eﬀort to address the calibration of
the constitutive equations for the α-Mo phase. Studies of the Hall-Petch eﬀect in α-
Mo have shown inconsistent results with some studies showing no Hall-Petch behavior
at grain sizes as small as 50 µm [8, 26, 27]. In the ﬁnal calibration of the constitutive
law for the α-Mo phase, the yield strength calibration was obtained from the work of
Sturm et al. with material of more reﬁned microstructures that is comparable to Mo-
Si-B alloys [8], while the response of the α-Mo obtained form the new experiments was
7 of 25

## Page 9

used to determine the plastic hardening behavior and strain rate sensitivity. Within
the modeling work itself, there are several opportunities for continuing work. The most
useful such work would be to combine this crystal-plasticity model with a cohesive zone
model of grain boundary strength. This would enable studies of the structure-property
relationships in the formation of brittle microcracks, a critical mechanical property for
any material optimization of Mo-Si-B alloys.
Microstructure Generator
The microstructure generator used to generate a digital representation of the arc-melted
α-Mo specimens is based on an ellipsoidal packing algorithm developed by Przybyla [28]
and related to the work of Groeber et al [29], which Przybyla showed to give greater
control over grain shape distributions in comparison to conventional Voronoi tessellation
based algorithms [28]. This is especially important for the arc-melted α-Mo specimen
material, which exhibits two unique regions of microstructure. This microstructure gen-
erator is capable of capturing the volume fractions for multiple phases and the crystal
structure, mean and standard deviation of grain size, grain shape distribution, grain
shape orientation distributions, and orientation distribution for each phase.
Grain size statistics are deﬁned as a mean and standard deviation for a uniform
distribution, which the microstructure generator then converts to a log normal distribu-
tion. Grain shape is captured by approximating grains with ellipsoids deﬁned by major
and minor aspect ratios which vary according to a beta distribution. Orientation dis-
tributions are captured through the free and open source, third party, Matlab toolbox
MTEX [30].
The microstructure generator is also capable of capturing the misorientation distribu-
tion for single phase, single region microstructures; however, the two region microstruc-
ture generator required for creating synthetic microstructures of the α-Mo compression
specimens complicates these calculations and cannot currently account for misorientation
8 of 25

## Page 10

distribution.
Tests were conducted on ﬁve materials with diﬀerent Si contents. Each required a
unique synthetic microstructure to be generated for the matching simulations. Three
of these materials, Mo-0.00Si, Mo-0.29Si, and Mo-0.40Si where Si is in weight percent,
require a two region microstructure. The two higher Si content materials, Mo-0.58Si and
Mo-1.16Si, require a single region microstructure.
The synthetic microstructures maintain a ﬁxed number of 27 elements per edge and
are loaded along the vertical (Y) axis to a mechanical strain of 0.5%. The number of
elements per edge is chosen to balance the ability to match the microstructural features,
mesh reﬁnement, and simulation run time. Periodic boundary conditions are applied
to all six faces of the synthetic volume elements, consistent with the periodic packing
of ellipsoids in the microstructure generator. A representative two region synthetic mi-
crostructure created for the arc-melted α-Mo Mo-0.40Si (wt.%) material is shown in
Figure 4.
Figure 4: Two region synthetic Mo-0.29Si and Mo-0.40Si microstructure with an edge
length of 5 mm and 610 total grains. Colors are assigned to unique grains.
The synthetic microstructure representing the arc-melted α-Mo material generated
for Mo-0.58Si and Mo-1.16Si is shown in Figure 5. This single region microstructure
does not require any special treatment to subdivide into separate regions.
Figure 5: Single region synthetic Mo-0.58Si and Mo-1.16Si microstructure with an
edge length of 2.7 mm and 200 total grains. Colors are assigned to unique grains.
Ideally, both the volume of the arc-melted α-Mo microstructures tested and the
volume of the synthetic microstructures simulated would be large enough to qualify as
representative volume elements (RVE) for the mechanical properties of volume averaged
elastic modulus and yield strength [31]. However, due to the small number of grains
and the large heterogeneity of the arc-melted α-Mo material used in this work, there is
no guarantee that the response of the physical specimens is insensitive to the speciﬁc
9 of 25

## Page 11

specimen tested. Therefore, instead of creating RVE simulations, the synthetic volume
element size corresponds directly to the specimen dimensions and should be considered
a statistical volume element (SVE) [31,32].
While this may not guarantee a converged stress-strain response of the arc-melted α-
Mo synthetic volume elements, it allows the constitutive model to be calibrated for plastic
hardening within the accuracy allowed by the experimental specimens and is suﬃcient
for a ﬁrst order study over a broad range of microstructures. The variability in yield
strength from the arc-meltedα-Mo material of this work due to the coarse microstructure
does not allow an acceptable calibration of the model parameters associated with yield
strength. Instead, separate volume elements are created matching Sturm et al. α-Mo
material [8] speciﬁcally for calibrating the yield strength of α-Mo as a function of Si
content and temperature.
Four distinct volume elements are created to match the distinct characteristics of the
four Sturm et al. α-Mo materials with diﬀering Si contents: 0.0, 0.1, 0.5, and 1.0 weight
percent Si [8]. These volume elements are created with equiaxed, randomly textured
grains. In this data set, only the mean grain size varies with Si content and is 97, 54, 35,
and 82µm, respectively [8]. There is no information on the actual grain size distribution
of the Sturm et al. material, so a log normal distribution is created from the mean grain
diameter and an assumed standard deviation approximately ten times smaller than the
mean diameter.
Figure 6 shows a representative synthetic microstructure for the Sturm et al. Mo-
0.00Si material. These volume elements have a slightly ﬁner mesh at 33 elements per
edge. Each volume element has a random texture and equiaxed grains.
Figure 6: Single region synthetic Sturm et al. Mo-0.00Si microstructure with an edge
length of 0.9 mm and 290 total grains. Colors are assigned to unique grains.
10 of 25

## Page 12

Viscoplastic Property Calibration
Due to the heterogeneous microstructure of the arc-melted calibration material, contain-
ing regions of textured and elongated grains, additional modeling work was required to
obtain the stress-strain response from the experimental load-displacement data. First
the elastic modulus was estimated for the calibration material at each Si content from
matching synthetic volume elements and the anisotropic, temperature dependent elas-
ticity tensors presented in Figure 1 [23]. The estimated elastic modulus was then sub-
tracted from the elastic portion of the load-displacement data to determine the machine
compliance. Finally, the estimated machine compliance was subtracted from the total
load-displacement data to obtain the engineering stress-strain curve. A representative
engineering stress-strain curve from the Mo-0.40Si material is shown in Figure 2. The
full set of stress-strain curves for the new arc-melted α-Mo experiments presented in this
work are found elsewhere [33]
The yield strength plot for the faster strain rate is compared to results by Sturm
et al. [8] in Figure 7. This plot shows that the arc-melted material captures the ex-
pected general trends of increasing strength with strain rate and decreasing strength
with temperature. However, some of the α-Mo deformation experiments conducted for
this work show increasing strength with temperature, as in the Mo-0.29Si data at 600 ◦C
and 1100◦C in Figure 7a. It is hypothesized that this is a result of the highly heteroge-
neous and sparsely populated microstructure of the experimental specimens.
Although the volume elements captured the characteristics of the two region mi-
crostructures with the intention of addressing these problems in the calibration, the
sparse number of total grains in the test specimens would require direct, three dimen-
sional characterization and modeling of the microstructure in individual test specimens to
capture the eﬀects of microstructure on yield strength. Consequently, the yield strength
used for model calibration was based on the Sturm et al. material with ﬁner, equiaxed
grains and random texture. Separate volume elements matching the Sturm et al. ma-
11 of 25

## Page 13

terial were created to perform this calibration. The resulting yield strength calibration
is presented in Figure 7c. Figure 7d compares the simulation calibration against exper-
imental data from a smaller Mo-Si solid solution study by Yu et al. for an extruded
and annealed material with similar grain sizes [34]. While the processing route of this
material diﬀers from the current study and the study of Sturm et al., Yu et al. noted
the similarities in strength behavior and mechanisms to the study of Sturm et al. It is
included here to partially validate the calibration of the constitutive model.
(a) Experimental results from calibration
material with a strain rate of 2 .77× 10−2 s−1
(b) Experimental results from Sturm et al.
at a strain rate of 2 .20× 10−3 s−1 [8] 1
(c) Simulation results of yield strength
calibration to Sturm et al. material
(d) Experimental results from Yu et al. at a
strain rate of 1 .0× 10−4 s−1 [34]
Figure 7: Calibration material yield strength as a function of temperature at the fast
strain rate in comparison to Sturm et al. data [8]
Despite the large diﬀerences in grain size between the two materials, this approach is
justiﬁed by the reported lack of a Hall-Petch eﬀect for grain sizes as small as 50 µm over
a range of Si contents [8,27]. One possible explanation is that the yield behavior in Mo
is not dependent on dislocation pile up on the length scale of grain size, but governed
by interactions of individual dislocations before pile-ups traversing an entire grain can
form [8].
Figure 7 also shows the eﬀects of solid solution softening of the α-Mo phase at room
temperature, where the yield strength of the Mo-0.10Si α-Mo is lower than that of the
Mo-0.00Si α-Mo. Although solid solution softening is observed experimentally at room
temperature in both the experiments of Sturm et al. [8] and those of this work, it is
not seen at high temperature in either set of experiments. The transition from solid
solution softening to solid solution strengthening with increasing temperature is related
to a transition temperature where the double kink mechanism no longer dominates plas-
tic deformation and the mobilities of edge and screw dislocations become similar [8].
1Reprinted from Materials Science and Engineering A, vol. 463, D. Sturm et al., ”The Inﬂuence of
Silicon on the Strength and Fracture Toughness of Molybdenum”, pp. 107-114, 2007, with permission
from Elsevier.
12 of 25

## Page 14

Consequently, solid solution softening is only observed near room temperature and lower
temperatures. These sub-structure eﬀects are homogenized and properly captured in the
constitutive model through the Si content and temperature-sensitive calibration of the
constitutive model parameters.
The primary motivation for conducting the compression tests presented in this work
is to supplement existing experimental data for α-Mo, which lacks variation in strain
rates and plastic hardening for higher temperatures. Therefore, despite the diﬃculties
associated with the arc-melted α-Mo specimens of this study, the strain rate sensitivity
and plastic hardening must be calibrated from the new compression experiments. The
methods employed to account for eﬀects of the arc-melted α-Mo microstructures will be
described in the calibration procedure.
To calibrate strain rate sensitivity, the inelastic strain rate and stress is plotted from
the yield point. At each temperature and Si content, a power law is ﬁt to the data and
the exponent of this ﬁt is the strain rate sensitivity exponent. Figures 8 and 9 present the
strain rate sensitivity exponent calibration plots for a 0.2% oﬀset yield strength of the
Mo-0.00Si and Mo-0.40Si material, respectively. Because of the variability in the yield
strength data, some of the yield strengths from the fast strain rate tests are actually lower
than low strain rate tests. Consequently the exponent of the power law is negative, which
is an unrealistic result contradictory to the mechanisms driving strain rate sensitivity.
Figure 8: Strain rate sensitivity calibration plot of inelastic strain rate vs. 0.2% oﬀset
yield stress as a function of temperature for Mo-0.00Si
Figure 9: Strain rate sensitivity calibration plot of inelastic strain rate vs. 0.2% oﬀset
yield stress as a function of temperature for Mo-0.40Si
To address the eﬀects of Si content on strain rate sensitivity, the strain rate sensitivity
exponent calibration is separated into two parts: one for the pure Mo material (Mo-
0.00Si) and another for the Mo with Si in solid solution. This division is a natural
result of the experimental data and corresponds to the changing dislocation mobilities of
13 of 25

## Page 15

Mo with any addition of Si in solid solution [8]. As a result of the changing dislocation
mobilities, Mo shows diﬀerent strain rate sensitivity as a function of Si content. Pure Mo
demonstrates room temperature strain rate sensitivity which decreases with increasing
temperature. However, Mo with Si in solid solution is relatively insensitive to strain rate
at room temperature and becomes sensitive to strain rate at higher temperatures.
Due to the inconsistency in experimental yield strength as a function of strain rate
from the arc-melted α-Mo experiments, a reliable calibration of strain rate sensitivity
could not be made from any single oﬀset yield strength calculation. Instead, a power
law is ﬁt to 0.02%, 0.2%, and 2% oﬀset yield strength calculations and the calibration
is chosen from a mix of the average results with respect to the expected trends. The
ﬁnal calibration of the strain rate sensitivity exponent as a function of Si content and
temperature is presented in Table 4.
After calibrating the strain rate sensitivity exponent, the yield strength is calibrated
through the initial drag stress,D0. With the limited information available, yield strength
is assumed to be a function of the initial drag stress alone and each slip system is treated
identically. Consequently, a maximum of three simulations are required to complete
the calibration of initial drag stress. Two diﬀerent estimates for D0 are made and the
resulting yield stress predictions can be used to solve for the ﬁnal calibration value
through linear interpolation between the corresponding predictions of yield strength.
In this work, the ﬁrst and second estimate are made from parametric studies on the
inﬂuence of model parameters. The calibrated initial drag stress value can be calculated
from linear interpolation as a function of the ﬁrst and second simulation predictions of
yield strength as
Df
0 =
(
D2
0−D1
0
) (σY−σ1
Y )
(σ2
Y−σ1
Y ) +D1
0 (3)
whereDf
0 is the ﬁnal initial drag stress calibration, σY is the experimentally determined
yield strength,D1
0 andD2
0 are the ﬁrst and second estimates of initial yield strength, and
σ1
Y andσ2
Y are the simulation predictions of yield strength corresponding to the ﬁrst and
14 of 25

## Page 16

second estimates of initial yield strength, respectively. Better calibrations could be made
as a function of slip system or slip system type or family if single crystal stress-strain
data is available. This would also require a more sophisticated calibration technique.
After calibrating the initial drag stress, the evolution parameters for back stress are
calibrated. To make a complete calibration with drag stress evolution, back stress evo-
lution, and threshold stress evolution, a full set of fatigue experiments are required and
must include the cyclic hardening or softening of the resultant cyclic stress-strain behav-
ior in addition to the stabilized cyclic response. With limited information available it is
assumed that the material is cyclically stable and that isotropic hardening is negligible so
cyclic behavior can be determined from the monotonic stress-strain behavior. Therefore,
back stress evolution is assumed to be the only set of parameters aﬀecting the plastic
hardening. Linear interpolation does not work directly as is the case for initial drag
stress. Instead, the ﬁnal calibration was ﬁrst bounded by prior back stress parameter
sensitivity studies and a small number of trial simulations were guided by interpolation
between these bounds. A quantitative ﬁt would require additional iteration or a more so-
phisticated approach using a ﬁtting function or surrogate models; however, the approach
used here is deemed suﬃcient given the variations expected as a result of the arc-melted
α-Mo specimens’ inhomogeneous microstructure.
Ideally, the plastic hardening could be calibrated quantitatively from a series of points
along the stress-strain curve at one strain rate, for instance at the 0.2% and 2% oﬀset
strengths, and the calibration would be validated by matching the curves of the second
strain rate. The separate direct hardening and dynamic recovery terms can be calibrated
iteratively by requiring a calibration both to early hardening behavior and the later
linear hardening behavior. The direct hardening term determines the initial slope of
early plastic hardening, while the dynamic recovery term determines how quickly the
plastic hardening saturates, ultimately limiting additional plasticity to perfectly plastic
behavior. However, due to the separate calibration of the yield strength and the large
variation in apparent strain rate sensitivity, the calibration is conducted by ﬁxing the
15 of 25

## Page 17

dynamic recovery coeﬃcient,C, at 10.0 for all Si contents and temperatures and varying
the direct hardening parameter, B, until a reasonable ﬁt of hardening slope could be
made for the slow strain rates at strains up to 3%.
A representative ﬁnal calibration plot of the Mo-0.40Si material for plastic hardening
is presented in Figure 10. Calibration was limited to 3% strain for several reasons. The
higher Si content arc-melted specimens were limited to roughly 3% ductility at lower
temperatures. The ultimate goal for this constitutive model development is focused
on three-phase Mo-Si-B alloys, which typically display room temperature ductility near
3% [3] and even high temperature modeling eﬀorts of fracture behavior do not usually
need to exceed 3% strain [12]. The multi-property material design goal for three-phase
Mo-Si-B alloys also includes fatigue resistance, but such simulations do not typically
cycle at higher strains. Because the calibration is only performed up to 3% strain, the
engineering stress-strain plot is suﬃciently accurate for this calibration.
Figure 10: Plastic hardening calibration plot for Mo-0.40Si. Lines represent
simulations. Markers represent select experimental data points.
The microstructure of the arc-melted α-Mo specimens could aﬀect the plastic hard-
ening calibration in a similar manner to the yield strength calibration; however, a more
suitable data set is not available for this calibration. Instead, after the ﬁnal calibration,
the resulting plastic hardening is simulated with the Sturm et al. volume elements and
compared to the experimental results from Sturm et al. as shown in Figure 11. Given
the extreme diﬀerences in microstructure and the number of assumptions involved in
calibrating the ﬂow rule, the resulting similarity in the plastic hardening calibration and
the plastic hardening seen in the Sturm et al. experimental results is reasonable.
Figure 11: Plastic hardening calibration comparison to Sturm et al. data at room
temperature and a strain rate of 2 .20× 10−3 s−1 using simulation volume elements
matching the Sturm et al. material [8]. Sturm data plotted with markers and
simulation results plotted without markers.
The complete set of material parameters are presented in Tables 2-4. Linear interpo-
16 of 25

## Page 18

lation is used to bridge the mix of calibration simulations. Linear interpolation is ﬁrst
carried out by temperature, and then by Si content. The values in bold are calibrated to
the experimental data at that Si content and temperature, while the rest are values that
are interpolated from nearby calibration points. Missing entries are locations where the
calibration was not conducted and the interpolation was not required for any simulation.
Table 2: Initial drag stress, D0, for α-Mo
Initial drag stress, D0 [MPa]
Temperature [◦C] Si content [wt.%]
0.00 0.10 0.25 0.29 0.40 0.50 0.58 0.75 1.00 1.16
22 157.6 135.0 260.5 411.0
25 156.2 134.3 181.3 259.7 334.6 409.4
260 43.0 76.4 198.5 283.4
538 28.6 65.1 163.5 247.9
600 27.6 63.7 156.5
816 23.9 58.9 132.1
1093 20.5 51.4 109.2
1100
1400 17.8 50.7 70.3 102.9 159.3 215.7
17 of 25

## Page 19

Table 3: Back stress direct hardening, B, for α-Mo
Back stress direct hardening, B [MPa], with ﬁxed back stress dynamic recovery, C = 10.0 [-]
Temperature [◦C] Si content [wt.%]
0.00 0.10 0.29 0.40 0.50 0.58 1.00 1.16
22 5014.3 5000.0 4436.9 3986.5
25 5000.0 5000.0 5000.0 5000.0 3986.5 3986.5
260 3879.7 5000.0 4436.9 3986.5
538 2554.5 5000.0 4436.9 3986.5
600 2258.9 5000.0 5000.0 5000.0 4436.9 3986.5 3986.5 3986.5
816 2258.9 3815.8 3496.0 3240.2
1093 2258.9 2297.3 2289.4 2283.1
1100 2258.9 2258.9 2258.9 2258.9 2258.9 2258.9 2258.9 2258.9
1400 2258.9 2258.9 2258.9 2258.9 2258.9 2258.9
18 of 25

## Page 20

Table 4: Strain rate sensitivity exponent, m, for α-Mo
Strain rate sensitivity exponent, m [-], with a ﬁxed reference shearing rate, ˙γ = 0.001 s −1
Temperature [◦C] Si content [wt.%]
0.00 0.10 0.29 0.40 0.50 0.58 1.00 1.16
22 5.9 20.0 20.0 20.0
25 6.0 20.0 20.0 20.0 20.0 20.0
260 11.7 20.0 20.0 20.0
538 18.5 20.0 20.0 20.0
600 20.0 20.0 20.0 20.0 20.0 20.0 20.0 20.0
816 20.0 15.7 15.7 15.7
1093 20.0 10.1 10.1 10.1
1100 20.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0
1400 20.0 6.0 6.0 6.0 6.0 6.0
19 of 25

## Page 21

Discussion
The goal of temperature, strain rate, and Si content dependent constitutive model for α-
Mo is to begin computational materials design of Mo-Si-B alloys. The constitutive model
developed and calibrated in this eﬀort provides the missing ICME tool to begin optimiz-
ing the Mo-Si-B alloys across multiple material properties for high strength structural
applications. The target class of alloys generally contain intermetallic phases which are
much stronger than α-Mo, making a ﬁrst order modeling eﬀort possible by treating the
intermetallic phases with temperature dependent, anisotropic elasticity. Use of the α-
Mo constitutive model developed here for multi-property materials design of three-phase
Mo-Si-B alloys is described separately [33,35].
While the model developed here provides a missing tool for computational materials
optimization studies, additional experimental work is required to extend this model to
higher ﬁdelity simulations. Physically based evolution equations, such as developed in
related work [18, 19], would provide better understanding of the underlying material
behavior. Unfortunately, there is a severe lack of useful experimental studies of Mo
and Mo-Si-B alloys suitable for calibration and validation. The model calibration could
be improved with calibration material of well characterized, uniform microstructures
and a test schedule including compression, tension, and cyclic loading at a variety of
temperatures and strain rates.
Conclusions
New experiments of polycrystalline α-Mo were conducted to determine the temperature
and strain rate sensitivity as a function of Si content. These experiments provide evidence
of solid solution softening in α-Mo in agreement with limited previous experiments and
conﬁrm the sharp contrast in behavior between pure Mo and Mo with Si in solid solution.
A crystal viscoplasticity model is developed and calibrated for α-Mo with varying
Si composition over a wide range of high temperatures and a range of strain rates with
20 of 25

## Page 22

the goal of modeling the α-Mo phase in Mo alloys based on borosilicides. The crystal
viscoplasticity model is the ﬁrst such model for α-Mo to include the eﬀects of Si content
and captures the solid solution softening seen at very low Si contents. The model also
captures the sharp change in behavior between pure Mo and Mo with even small amounts
of Si in solid solution. While addressing the non-uniform, anisotropic microstructure
of the calibration specimens, it is shown that a synthetic microstructure generator can
allow the use of non-ideal experimental calibration specimens in the calibration of crystal
viscoplasticity models.
Acknowledgments
This work was supported by United Technologies Corporation, Pratt & Whitney Divi-
sion. Special thanks to the points of contact during the course of this work, Dr. Gopal
Das, Rick Montero, and Dr. Shiela Woodard, and to Greg Levan from Pratt & Whitney
Materials & Processes Engineering for providing technical support characterizing the
α-Mo calibration material.
References
[1] B. P. Bewlay, M. R. Jackson, J. C. Zhao, and P. R. Subramanian, “A review of
very-high-temperature Nb-silicide-based composites,” Metallurgical and Materials
Transactions A, vol. 34A, pp. 2043–2052, October 2003.
[2] D. M. Dimiduk and J. H. Perepezko, “Mo-Si-B alloys: Developing a revolutionary
turbine-engine material,” Materials Research Society Bulletin , vol. 28, pp. 639–645,
September 2003.
[3] J. A. Lemberg and R. O. Ritchie, “Mo-Si-B alloys for ultrahigh-temperature struc-
tural applications,” Advanced Materials, vol. 24, pp. 3445–3480, 2012.
21 of 25

## Page 23

[4] R. Mitra, “Mechanical behaviour and oxidation resistance of structural silicides,”
International Materials Reviews , vol. 51, no. 1, pp. 13–64, 2006.
[5] S. Aryal, M. C. Gao, L. Ouyang, P. Rulis, and W. Y. Ching, “ Ab initio studies
of Mo-based alloys: Mechanical, elastic, and vibrational properties,” Intermetallics,
vol. 38, pp. 116–125, 2013.
[6] J. H. Schneibel, M. J. Kramer, O. ¨Unal, and R. N. Wright, “Processing and me-
chanical properties of a molybdenum silicide with the composition Mo-12Si-8.5B
(at. %),” Intermetallics, vol. 9, pp. 25–31, 2001.
[7] T. A. Parthasarathy, M. G. Mendiratta, and D. M. Dimiduk, “Oxidation mech-
anisms in Mo-reinforced Mo 5SiB2 (T2) - Mo 3Si alloys,” Acta Materialia , vol. 50,
pp. 1857–1868, 2002.
[8] D. Sturm, M. Heilmaier, J. H. Schneibel, P. J´ ehanno, B. Skrotzki, and H. Saage,
“The inﬂuence of silicon on the strength and fracture toughness of molybdenum,”
Materials Science and Engineering A , vol. 463, pp. 107–114, 2007.
[9] W. L. Bruckart, M. H. LaChance, C. M. Craighead, and R. I. Jaﬀee, “Properties of
some hydrogen-sintered binary molybdenum alloys,” Transactions of the American
Society of Metals , vol. 45, no. 286, 1953.
[10] L. Northcott, Molybdenum. New York: Academic Press Inc., 1956.
[11] K. S. Kumar, “Fatigue response of Mo-Si-B alloys,” tech. rep., Brown University,
2005.
[12] A. Patra, M. W. Priddy, and D. L. McDowell, “Modeling the eﬀects of microstruc-
ture on the tensile properties and micro-fracture behavior of Mo-Si-B alloys at ele-
vated temperatures,” Intermetallics, vol. 64, pp. 6–17, 2015.
22 of 25

## Page 24

[13] G. J. Kleiser, B. Revil-Baudard, O. Cazacu, and C. L. Pasiliao, “Plastic deformation
of polycrystalline molybdenum: Experimental data and macroscopic model account-
ing for its anisotropy and tension-compression asymmetry,” International Journal
of Solids and Structures , vol. 75-76, pp. 287–298, December 2015.
[14] G. J. Kleiser, B. Revil-Baudard, and C. L. Pasiliao, “High strain-rate plastic de-
formation of molybdenum: Experimental investigation, constitutive modeling and
validation using impact tests,” International Journal of Impact Engineering , vol. 96,
pp. 116–128, October 2016.
[15] R. A. Lebensohn and C. N. Tom´ e, “A self-consistent anisotropic approach for the
simulation of plastic deformation and texture development of polycrystals: Applica-
tion to zirconium alloys,”Acta Metallurgica et Materialia, pp. 2611–2624, September
1993.
[16] M. Knezevic, I. J. Beyerlein, M. L. Lovato, C. N. Tom´ e, A. W. Richards, and R. J.
McCabe, “A strain-rate and temperature dependent constitutive model for BCC
metals incorporating non-schmid eﬀects: Application to tantalum-tungsten alloys,”
International Journal of Plasticity , pp. 93–104, November 2014.
[17] T. Walde, “Plastic anisotropy of thin molybdenum sheets,” International Journal
of Refractory Metals and Hard Materials , vol. 26, pp. 396–403, September 2008.
[18] H. Lim, C. C. Battaile, J. D. Carroll, B. L. Boyce, and C. R. Weinberger, “A phys-
ically based model of temperature and strain rate dependent yield in BCC metals:
Implementation into crystal plasticity,” Journal of the Mechanics and Physics of
Solids, vol. 74, pp. 80–96, 2015.
[19] T. Yalcinkaya, W. A. M. Brekelmans, and M. G. D. Geers, “BCC single crystal
plascticity modeling and its experimental identiﬁcation,” Modelling and Simulation
in Materials Science and Engineering , vol. 16, pp. 1–16, October 2008.
23 of 25

## Page 25

[20] P. J. Armstrong and C. O. Frederick, “A mathematical representation of the multi-
axial bauschinger eﬀect,” Tech. Rep. GEGB Report, RD/B/N731, Berkeley Nuclear
Laboratories, 1966.
[21] Dassault Systemes, “Abaqus v. 6.11-1. 2011.” Providence, RI, USA.
[22] K. A. Brindley and R. W. Neu, “Progress in structure-property modeling tools for
γ-TiAl,” in Symposium on High Performance Aerospace Alloys Design Using ICME
Approach, (Orlando, FL, USA), pp. 1173–1183, The Minerals, Metals, and Materials
Society, Wiley, March 2015.
[23] J. M. Dickinson and P. E. Armstrong, “Temperature dependence of the elastic con-
stants of molybdenum,” Journal of Applied Physics , vol. 38, pp. 602–606, February
1967.
[24] M. R. Middlemas, Fabrication, Strength and Oxidation of Molybdenum-Silicon-
Boron Alloys from Reaction Synthesis . PhD Dissertation, Georgia Institute of Tech-
nology, Atlanta, Georgia, May 2009.
[25] P. Jain and K. S. Kumar, “Tensile creep of Mo-Si-B alloys,”Acta Materialia, vol. 58,
pp. 2124–2142, 2010.
[26] A. S. Wronski and A. A. Johnson, “The deformation and fracture properties of
polycrystalline molybdenum,” Philosophical Magazine, vol. 7, no. 74, pp. 213–227,
1962.
[27] R. N. Orava Transactions of the Metallurgical Society of AIME , vol. 230, p. 1614,
1964.
[28] C. P. Przybyla, Microstructure-sensitive Extreme Value Probabilities of Fatigue in
Advance Engineering Alloys . PhD Dissertation, Georgia Institute of Technology,
Atlanta, Georgia, August 2010.
24 of 25

## Page 26

[29] M. Groeber, S. Ghosh, M. D. Uchic, and D. M. Dimiduk, “A framework for auto-
mated analysis and simulation of 3d polycrystalline microstructures. part 2: Syn-
thetic structure generation,” Acta Materialia, vol. 56, pp. 1274–1287, 2008.
[30] F. Bachmann, R. Hielscher, and H. Schaeben, “Texture analysis with MTEX - free
and open source software toolbox,” Solid State Phenomena , vol. 160, pp. 63–68,
February 2010.
[31] R. Hill, “Elastic properties of reinforced solids: Some theoretical principles,” Journal
of the Mechanics and Physics of Solids , vol. 11, no. 5, pp. 357–372, 1963.
[32] D. L. McDowell and F. P. E. Dunne, “Microstructure-sensitive computational model-
ing of fatigue crack formation,”International Journal of Plasticity , vol. 32, pp. 1521–
1542, 2010.
[33] K. A. Brindley, Microstructure-sensitive Structure-property Modeling Tools for
Triplex Mo-Si-B Alloys . PhD Dissertation, Georgia Institute of Technology, At-
lanta, Georgia, May 2017.
[34] X. J. Yu and K. S. Kumar, “The tensile response of Mo, Mo-Re and Mo-Si solid
solutions,” International Journal of Refractory Metals and Hard Materials , vol. 41,
pp. 329–338, 2013.
[35] K. A. Brindley, M. W. Priddy, and R. W. Neu, “Integrative materials design of
three-phase Mo-Si-B alloys,” Integrating Materials and Manufacturing Innovation ,
vol. 8, pp. 1–16, March 2019.
25 of 25
