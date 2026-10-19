# Fatigue Fract Eng Mat Struct - 2024 - Kumar - Dislocation density‐based constitutive model for cyclic deformation and

<!-- source: D:\总文献\Fatigue Fract Eng Mat Struct - 2024 - Kumar - Dislocation density‐based constitutive model for cyclic deformation and.pdf -->
<!-- file_sha256: ed9cdb6db2ed27ebf10057cb0d0ffe5f89191c44afa6968a65e62a9b2d57db69 -->

## Page 1

ORIGINAL ARTICLE
Dislocation density-based constitutive model for cyclic
deformation and softening of Ni-based superalloys
Shivam Kumar 1,2 | Anirban Patra 3 | J. K. Sahu 1,2
1Academy of Scientific and Innovative
Research (AcSIR), Ghaziabad, India
2MTE Division, CSIR-National
Metallurgical Laboratory, Jamshedpur,
India
3Department of Metallurgical Engineering
and Materials Science, Indian Institute of
Technology Bombay, Mumbai, India
Correspondence
Shivam Kumar, Academy of Scientific and
Innovative Research (AcSIR), Ghaziabad-
201002, India.
Email:
4shivamkumar@gmail.com
Abstract
A physically-based constitutive modeling framework is proposed for the cyclic
deformation and softening of Ni-based superalloys. The constitutive model
accounts for underlying mechanisms of grain size strengthening, dislocation
strengthening, solid solution strengthening, and precipitate strengthening,
commonly observed in these alloys. A constitutive model is proposed for the
shearing of precipitates on their interaction with glide dislocations during
cyclic deformation. This is the primary contributor to the experimentally
observed cyclic softening behavior in Ni-based superalloys. Model predictions
of the cyclic stress –strain response and the cyclic softening (quantified in terms
of the peak stress) are compared with the experimental counterparts for a
range of strain amplitudes under fully-reversed cyclic loading of Inconel
718 (IN 718). Further, model predictions of precipitate size are also compared
with the experimentally measured transmission electron micrographs of pre-
cipitate sizes at the end of deformation. Concurrence in the cyclic stress –strain
response, peak stress, and precipitate size provides validation for our constitu-
tive modeling framework.
KEYWORDS
cyclic deformation, cyclic softening, dislocation density, Inconel, low cycle fatigue,
precipitate shearing
Highlight
• Development of a physically-based constitutive modeling framework for
cyclic deformation.
• Microstructure-based strengthening mechanisms are considered in the
model.
• Model incorporated the physical mechanisms of cyclic softening due to pre-
cipitate shearing.
Received: 5 February 2024 Revised: 3 May 2024 Accepted: 1 June 2024
DOI: 10.1111/ffe.14367
3264 © 2024 John Wiley & Sons Ltd. Fatigue Fract Eng Mater Struct. 2024;47:3264–3284.wileyonlinelibrary.com/journal/ffe

## Page 2

1 | INTRODUCTION
Inconel alloys are a class of polycrystalline nickel-based
superalloys that are widely used for manufacturing
turbine discs in aero engines due to their superior high-
temperature mechanical properties.
1–5 The microstruc-
ture of these alloys is generally comprised of γ0 and γ00
precipitates in the γ matrix, and precipitate strengthening
is one of the main mechanisms contributing to the high-
temperature strength. 1,6 Aero-engine discs are generally
subjected to cyclic mechanical loads at elevated tempera-
tures. It is thus essential to study the cyclic deformation
behavior of Inconel alloys and correlate with the underly-
ing microstructure-sensitive dislocation-mediated mecha-
nisms. Given the high costs associated with experimental
studies, design analyses often rely on predictive simula-
tions for the life prediction of structural components.
However, the accuracy of these simulations is strongly
dependent on the validity of the constitutive models over
the range of loading conditions generally encountered
during operation. In this respect, physically-based consti-
tutive models that can account for such mechanisms can
be used for the prediction of mechanical properties.
There are several phenomenological models available in
the literature
7–12 to describe the cyclic deformation of Ni-
based superalloys. However, these approaches do not
generally account for the underlying physical mecha-
nisms of dislocation-mediated phenomena that may
occur during cyclic deformation, such as precipitate
strengthening, solid solution strengthening, dislocation
strengthening, and precipitate shearing.
1
A commonly observed phenomenon during the cyclic
deformation of Inconel alloys is cyclic softening, which
generally refers to the progressive reduction in stress
amplitude with the number of cycles. This is often corre-
lated with the shearing of the γ
0 and γ00 precipitates by
glide dislocations in Ni-based superalloys, 4,5,13,14 which
contributes to a reduction in the flow stress. Note that
cyclic softening is also observed in other alloys, such as
stainless steels, although the underlying physical mech-
anisms are different.
15,16 While constitutive models have
phenomenologically accounted for such softening by
considering damage, 17–20 the underlying physical mech-
anisms have only been accounted recently in crystal
plasticity models.
21–24 In this respect, it should be men-
tioned that there are several crystal plasticity models
for the cyclic deformation of Ni-based superalloys. 25–29
However, given the high computational costs generally
associated with crystal plasticity models, computation-
ally efficient J2 plasticity models may be preferred for
life prediction at the component level. The development
of a physically-based J
2 plasticity model for the elevated
temperature cyclic deformation of Ni-based superalloys,
with consideration for the underlying mechanisms of
cyclic softening, comprises the main objective of the
present work.
The present work proposes a physically-based J
2
plasticity constitutive modeling framework for predict-
ing the elevated temperature cyclic deformation behav-
ior of Ni-based superalloys. Dislocation density-based
constitutive equations are proposed for representing the
strengthening and substructure evolution during cyclic
deformation of Ni-based superalloys, with emphasis on
the microstructure-specific strength contributions. In
this regard, constitutive equations for grain size
strengthening, solid solution strengthening, precipitate
strengthening, and dislocation strengthening are consid-
ered in our model. Further, a novel constitutive model
is proposed for the interaction of glide dislocations with
precipitates that contribute to the observed cyclic soft-
ening in these superalloys. The elasto-plastic constitu-
tive modeling framework has been implemented as a
User Material subroutine in the commercial finite ele-
ment software ABAQUS ™. The framework is validated
by comparing model predictions with the experimental
data of a polycrystalline Ni-based superalloy, Inconel
718 (IN 718).
30
2 | MATERIAL
This work studies the cyclic deformation behavior of a
polycrystalline Ni-based superalloy, IN 718. Details
regarding the material chemistry are given in Banerjee
et al.
30 The IN 718 alloy was initially forged and then
subjected to a solutionizing heat treatment, followed by
aging. This is schematically shown in Figure 1A. The
material was solution treated at 960
/C14
C for 1 h and then
air cooled to room temperature. Subsequently, it was
aged at 760
/C14
C for 8 h and then furnace cooled to 620
/C14
C,
where it was held for 8 h, before being finally air cooled
to room temperature. The aging heat treatment aids in
the formation of γ
0 and γ00 precipitates. Given that the
sizes of γ0and γ00 precipitates are very small, it is difficult
to determine their volume fractions by electron micros-
copy. Given the difficulties in estimating the exact vol-
ume fraction of the different phases, the predicted
fraction of the different phases formed during the heat
treatment process estimated using ThermoCalc is shown
in Figure
1B. Neglecting the carbide phases, these phase
fractions were subsequently utilized in the developed
model to accurately represent the microstructural evolu-
tion of the material.
Further, the as-received material was characterized
using scanning electron microscopy (SEM) and transmis-
sion electron microscopy (TEM) to evaluate the grain size
KUMAR ET AL . 3265
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

of the γ phase and the sizes of γ0 and γ00 precipitates.
These microstructural parameters serve as input to our
constitutive model described in Section 3. Analysis of the
SEM microstructure shown in Figure 2A reveals that
the mean grain radius of the γ phase is ≈ 4 μm. TEM
microstructures of the as-received material are shown in
Figure
2B,C, which indicate the approximate size of
γ0 and γ00 precipitates as 12 and 10 nm, respectively. The
high-resolution TEM (HRTEM) image of a representative
γ00 precipitate is also shown in Figure 2C. The precipitate
sizes were measured by calculating the area of each parti-
cle from TEM images using ImageJ software and then
converting to the corresponding size under the assump-
tion of a circular cross-section.
The study utilized a material identical to that
employed by Banerjee et al.,
30 with an additional material
(IN 718) sharing the same composition but featuring a
distinct grain size of 24 μm. The aim was to predict the
yield strength and low-cycle fatigue (LCF) mechanical
response from Banerjee et al.
30 using our model, specifi-
cally considering strain amplitudes of 1.0%, 0.8%, and
0.6%. Further, additional LCF experiments were also per-
formed at 0.9% and 0.7% strain amplitude on identical
material of grain size of 4 μm in the present study for
comparison with predicted model trends.
3 | CONSTITUTIVE MODEL
The enhanced mechanical properties of IN 718 are gener-
ally owed to the underlying microstructure and the corre-
sponding strengthening mechanisms. Here, we propose a
physically-based constitutive model that can predict the
effect of the microstructure on the cyclic deformation of
IN 718.
The small strain plasticity framework is based on the
additive decomposition of the strain tensor, ε, into the
elastic, ε
e, and plastic, εp, parts, that is,
ε ¼ εe þ εp ð1Þ
The stress, σ, is related to the elastic strain using the
constitutive relationship for linear elasticity, that is,
σ ¼ C : εe ¼ C : ε /C0 εpðÞ ð 2Þ
where C is the isotropic elastic stiffness tensor. Plastic
deformation is modeled using a rate-dependent constitu-
tive model based on a Von Mises yield criterion, which is
of the form
31:
F ¼ 3
2 S /C0 χðÞ : S /C0 χðÞ /C0 σ2
f ≥ 0 ð3Þ
for plastic deformation to occur. Here, S is the deviatoric
stress tensor, χ is the backstress tensor, and σf is the flow
stress that evolves as a function of the equivalent plastic
strain rate, _ε
p
, and the internal state variables with
plastic deformation. In this yield function, the yield stress
is estimated from the second invariant, J2, of the deviato-
ric stress tensor, S, minus the backstress tensor, χ , and
hence is commonly referred as a J2 plasticity model. Fur-
ther, the rate of evolution of the plastic strain rate tensor
is given as
_εp ¼
ﬃﬃﬃ
3
2
r
_ε
p
Np ð4Þ
where Np is the direction of plastic flow and is given as
the unit normal to the yield surface, that is,
FIGURE 1 (A) Schematic of the heat treatment process. (B) Volume fractions of the various phases of IN 718 as predicted by
Thermocalc. [Colour figure can be viewed at wileyonlinelibrary.com]
3266 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

Np ¼
ﬃﬃﬃ
3
2
r
S /C0 χ
σ ð5Þ
where σ ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
3
2 S /C0 χðÞ : S /C0 χðÞ
q
is the effective stress. Fur-
ther, _ε
p
is the effective plastic strain rate given by
_ε
p
¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2
3 _εp : _εp
r
ð6Þ
Note that variables in bold notation represent tensor
quantities in the above equations.
While these constitutive equations for J2 plasticity
have existed previously, we have considered physically-
based deformation mechanisms, along with dislocation
density-based strengthening. These dislocation density-
based models have been adapted to material-specific
strengthening mechanisms for Ni-based superalloys in
the present work from prior studies,
32–34 where they were
used for studying deformation in various multi-phase
alloys. The following discusses equations that account for
contributions due to each of these distinct strengthening
mechanisms to the σ
f term.
FIGURE 2 (A) SEM image showing
the γ grains in the as-received material.
TEM images showing (B) γ0 precipitates
and (C) γ00 precipitates in the as-received
material and corresponding size
distribution of the (D) γ0precipitates and
(E) γ00 precipitates. [Colour figure can be
viewed at wileyonlinelibrary.com]
KUMAR ET AL . 3267
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

Follansbee and Kocks 35 considered the flow stress as
a function of the mechanical threshold stress, which has
two components, namely, the thermal, σ
t, and athermal,
σa, resistance to dislocation glide. The athermal resis-
tance is representative of the rate-independent interac-
tions of glide dislocations with long-range barriers, while
the thermal resistance is representative of rate-dependent
interactions with short-range barriers. The corresponding
flow strength due to these individual contributions to the
mechanical threshold stress is given as
35,36
σf ¼ σa þ σt 1 /C0 kT
ΔFg
ln _ε0
_ε
p
/C18/C19/C20/C21 1
q
() 1
p
ð7Þ
Here, ΔFg is the activation energy, k is the Boltzmann
constant, T is the absolute temperature, _ε0 is the refer-
ence strain rate, and p and q are parameters governing
the shape of the activation energy curve.
Kozar et al. 1 have discussed the contribution of the
individual strengthening mechanisms in Ni-based super-
alloys. These are expected to contribute to the athermal
resistance, σ
a, that is,
σa ¼ Δσgb þ Δσss þ Δσppt þ Δσdislocation ð8Þ
where the terms Δσgb, Δσss, Δσppt , and Δσdislocation repre-
sent the strength contributions due to grain boundary
strengthening, solid solution strengthening, strengthen-
ing due to γ
0 and γ00 precipitates, and dislocation strength-
ening, respectively. These individual contributions are
discussed in the following.
i. Grain boundary strengthening
High-angle grain boundaries in the γ matrix may act
as barriers to dislocation glide. Accordingly, this has been
modeled using a Hall –Petch type term, which gives the
increase in strength as an inverse of the square root of
the grain size, that is,
Δσ
gb ¼ f kHPﬃﬃﬃ
d
p ð9Þ
where f is the volume fraction of the γ matrix, kHP is the
Hall–Petch coefficient, and d is the mean grain size. 1
ii. Solid solution strengthening
Several alloying elements are added to Ni-based
superalloys to enhance their mechanical properties due
to solid solution strengthening. Gypen and Deruyttere
37
proposed a model for solid solution strengthening of the
nickel matrix-based alloy that assumes superposition of
the strengthening due to individual solute species with
different potencies. Given that the solute spacing is pro-
portional to the square root of the concentration, the
strength contribution can be written as
Δσ
ss ¼
X
i
ks,i
ﬃﬃﬃﬃci
p ð10Þ
where ks,i is the strengthening coefficient of the solute
species, ci.
iii. Precipitate strengthening
The IN 718 microstructure is comprised of γ0and γ00
precipitates, with an L1 2 (ordered FCC) and metastable
D022 crystal structure, respectively. 38,39 These ordered
precipitates are the main contributors to the strength of
IN 718. Ordered precipitates in the path of glide disloca-
tions may get sheared by the dislocations. The anti-phase
boundary (APB) energy and the size of the ordered pre-
cipitates may also influence the dislocation-precipitate
interactions and the formation of dislocation pairs.
27,40,41
For smaller sized precipitates (less than approxi-
mately 20 nm), shearing by weakly coupled dislocation
pairs may be active. Kozar et al. 1 have proposed a model
for weak pair coupling that is a function of the precipitate
size, d
s, and the APB energy, γAPB, such that
τweak ¼ γAPB
2b
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
γAPB ds
2TL
s
ds
Ls
/C0 π
4
ds
Ls
/C18/C19 2 !
ð11Þ
where b is the Burgers vector magnitude, TL is the dislo-
cation line tension, and Ls is the precipitate spacing.
Based on a model proposed by Ardell, 42 the precipitate
spacing is given as
Ls ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
8
3πf p
s
ds /C0 ds ð12Þ
where f p is the volume fraction and ds is the mean planar
size. Given that mean sizes both the γ0and γ00 precipitates
are less than 10 nm for the material under consideration
(cf. Figure 2), it is assumed that weak pair coupling is
dominant for these precipitates, that is, Δσppt ¼
τweakðÞ γ0 þ τweakðÞ γ00 . The corresponding size, volume frac-
tion, and APB energy of the precipitates are used in the
above constitutive equations accordingly.
The resistance to dislocation glide due to weak pair
coupling may increase with the increase in precipitate size,
3268 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

until the strengthening mechanism changes to strong pair
coupling, which offers a lower resistance to dislocation
glide, as compared with weak pair coupling. For higher
precipitate sizes, Orowan looping may also be dominant.
iv. Dislocation strengthening
We consider the evolution of mobile and immobile
dislocation densities as a function of plastic strain in our
model. The strength contribution due to the dislocation
density is given by a Taylor hardening model,
43
Δσdislocation ¼ Gb ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃqρ ρtot
p ð13Þ
where G is the shear modulus, qρ is dislocation barrier
strength, and ρtot is the total dislocation density, given as
the linear sum of the mobile, ρM , and immobile, ρI , dislo-
cation densities.
Constitutive models for the evolution of the mobile
and immobile dislocation densities have been adopted
from previous studies, 29,33,44–46 where they have been
implemented in crystal plasticity and J2 plasticity
models to study the deformation of metallic alloys,
including Ni-based superalloys. Their evolution rates
are of the form:
_ρ
M ¼ _ρmul /C0 _ρmutual /C0 _ρtrap ¼ kM
b
ﬃﬃﬃﬃﬃﬃρM
p _ε
p
/C0 2Rc
b ρM _ε
p
/C0 kI
bλ
_ε
p
ð14Þ
_ρI ¼ _ρtrap /C0 _ρdyn ¼ kI
bλ
_ε
p
/C0 kD ρI _ε
p
ð15Þ
These constitutive equations account for the multipli-
cation of mobile dislocations at existing segments, _ρmul;
mutual annihilation of dislocation dipoles, _ρmutual; trap-
ping of mobile dislocations, _ρtrap, thus rendering them
immobile; and dynamic recovery of immobile disloca-
tions, _ρdyn. λ is the effective dislocation mean free path
and kM , Rc, kI , and kD are associated material constants
that can be estimated by fitting.
3.1 | Backstress evolution
Shenoy et al. 25 proposed a dislocation density-based kine-
matic hardening model for Ni-based superalloys, in the
form of an Armstrong –Frederick model. This model
accounts for linear hardening due to dislocation density
and recovery along the direction of the backstress tensor.
We have adapted the model from its slip system-level
form to a total dislocation density form, such that
_χ ¼ k
χ1
kχ2
1 þ kχ3
ﬃﬃﬃﬃﬃﬃﬃρtot
p Gb ﬃﬃﬃﬃﬃﬃﬃρtot
p Np /C0 χ
/C18/C19
_ε
p
ð16Þ
where kχ1, kχ2, and kχ3 are associated material
parameters.
3.2 | Cyclic softening
Cyclic softening, a progressive reduction in stress ampli-
tude with number of cycles, has been generally observed
in IN 718 during low-cycle fatigue deformation.
4,47–49 In
these alloys, cyclic hardening was found to take place
during the initial cycles, followed by progressive cyclic
softening till failure.
48,50 Physically, the cyclic softening
has generally been attributed to successive shearing of
coherent and ordered γ00 precipitates by dislocations dur-
ing cyclic deformation. This successive shearing leads to
a progressive reduction in size up to a point where they
offer no resistance to the dislocation movement. 51,52
Crystal plasticity-based constitutive models for cyclic
softening in Ni-based superalloys have been proposed by
Agaram et al. 22 and Le /C19on-C/C19azares et al. 23 These studies
considered shearing of precipitates during cyclic defor-
mation. Further, Patra et al.
53 proposed a constitutive
model for annihilation of irradiation-induced defects on
their interaction with mobile dislocations that contrib-
utes to dislocation channeling and flow softening in irra-
diated materials during tensile deformation. This
constitutive model gives the rate of reduction in the
defect size as a function of the mobile dislocation density
and the areal loop density. The same constitutive model
has been adapted in the present work to account for pre-
cipitate shearing during cyclic deformation of Ni-based
superalloys. The rate of evolution of precipitate size is
phenomenologically modeled as a function of the areal
density of the precipitates and the interacting mobile dis-
location density. Further, since this phenomenon is only
observed during cyclic loading, the evolution rate is mod-
eled as a function of the effective cyclic strain rate, _
ε
p
cyc,
rather than the effective plastic strain rate. Accordingly,
we have adapted a modified form of the defect annihila-
tion model 53 to represent the rate of evolution of precipi-
tate size, dγ00 ,a s
_dγ00 ¼ /C0 kCS
εaNγ00
Nγ00 dγ00
/C0/C1 cCS
ρMðÞ 1/C0 cCS _ε
p
cyc;dγ00 >0 :5nm
0; dγ00 ≤ 0:5nm
8
<
: ð17Þ
KUMAR ET AL . 3269
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

where kCS and cCS are material parameters, εa is the
applied strain amplitude, Nγ00 is the number density of
precipitates, and _ε
p
cyc ¼ _ε
p
Δ cyclicðÞ is the cyclic effective
plastic strain rate, and Δ cyclicðÞ ¼ 1 for cyclic deforma-
tion and Δ cyclicðÞ ¼ 0 elsewise. The variable, _ε
p
cyc, is used
to modulate between cyclic and monotonic loading using
the Δ cyclicðÞ input parameter. As a first-order approxima-
tion, the minimum precipitate size is limited to 0 :5 nm,
and precipitate shearing is not allowed once the precipi-
tate size is below this value. This is justified based on the
fact that precipitate sizes below twice the Burgers vector
magnitude would be aphysical. In future work, the lower
limit of the precipitate size may be experimentally esti-
mated using higher resolution TEM. The strength contri-
bution due to precipitates is reduced due to the decrease
in the size of the sheared precipitates, and this may con-
tribute to the lowering in peak stress observed during
cyclic loading.
These constitutive equations have been implemented
in the J
2 plasticity framework with a fully implicit time
step integration based on the algorithm proposed by Pra-
sannavenkatesan.
54 Note that while several of these
micromechanical models (apart from the cyclic softening
model) have been individually proposed in the literature,
they have generally not been used together to predict the
cyclic deformation behavior of Ni-based superalloys in a
J
2 plasticity framework (which can be used for multi-
axial plasticity). Further, as will be demonstrated later,
the newly proposed cyclic softening model can predict
both the cyclic softening behavior (quantified in terms of
the peak stress evolution with number of cycles) and the
precipitate size evolution and can be validated with rele-
vant experimental microstructure measurements.
The constitutive model was implemented as a User
Material (UMAT) subroutine in the commercial finite
element software, ABAQUS. While all predictions pre-
sented in this work are using single-element simulations,
the UMAT can be used for component-level finite ele-
ment simulations in the future.
Note that the mechanisms considered in this work
are assumed to be the primary contributors to the
strength of the alloy under consideration, that is, IN 718.
While similar strengthening mechanisms are expected to
be operative in other Ni-based superalloys as well, some
additional mechanisms may also be present depending
on the microstructure and the processing route. For
example, powder metallurgy-processed Ni-based superal-
loys may have large, micron-sized primary γ
0 precipitates,
which may contribute to the strength and also deform
plastically.46 Further, Orowan looping may also contrib-
ute for precipitate sizes higher than 500 nm, when weak-
and strong-pair coupling may not be dominant.
1 Appro-
priate modifications may be made in future work to con-
sider other superalloys.
4 | MODEL PARAMETERS
The deformation of Ni-based superalloys involves com-
plex physical mechanisms, and their representation in
constitutive equations makes it challenging to calibrate
the various model parameters. To the extent possible, we
have used available data from the literature for the
parameters, while calibrating the rest to fit the experi-
mental stress–strain response.
Temperature-dependent isotropic elastic constants for
IN 718 are taken from Perea et al.
55 and are of the form:
E ¼ 249:80 þ 0:23729 T þ 4:0609 /C2 10/C0 4 T2 /C0 2:7533
/C16
/C2 10/C0 7 T3
/C17
GPa
ν ¼ 0:25916 /C0 9:63371 /C2 10/C0 5 T þ 6:24818 /C2 10/C0 7 T2
/C0 5:8018 /C2 10/C0 10 T3
The solid solution strengthening constants for various
alloying elements have been experimentally calculated by
Mishima et al. 56 for binary Ni-X system, with X being an
alloying element. Roth et al. 57 have studied ternary and
higher order systems. The coefficient, ks,i, pertaining to
the solid solution strengthening for different solute atoms
in the γ matrix is taken from these studies and is shown
in Table 1. Further, the measured elemental concentra-
tions (converted from weight fraction to mole fraction) in
IN 718 have been used from Banerjee et al. 30
Model parameters related to precipitate strengthen-
ing are given in Table 2. The APB energies, shear mod-
uli, and Burgers vector magnitudes are taken directly
from literature. 47 The volume fractions of the precipi-
tates are obtained using Thermocalc simulations of the
heat treatment regime mentioned earlier. Given that
TABLE 1 Solid solution
strengthening coefficients for different
elements in Ni solution
57 along with the
measured solute concentrations from
Banerjee et al. 30
Cr Co Mo Fe Si Mn Cu C
ks,i (MPa/pct1/2) 337 39.4 1015 153 275 448 86.7 1061
ci (mole fraction) 5.203 2.34 0.277 11.46 0.11 0.07 0.3 0.006
3270 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

the volume fraction of the carbides (as predicted by
Thermocalc) is less than 0.02, we have neglected their
contribution to the strength, as a first-order assumption.
Further, the precipitate sizes (prior to cyclic deforma-
tion) are obtained from the TEM measurements in
Figure
2. The precipitate sizes obtained from our lim-
ited measurements are in accordance with values
reported in the literature. 27,50,58,59
Given that there are several model parameters associ-
ated with the strengthening and substructure evolution
mechanisms, we have tried to estimate them via trial and
error, while at the same time ensuring that the assumed
value of these model parameters does not violate the
known physics of plastic deformation. A parametric study
of the effect of some of the model parameters governing
the initial strength and subsequent hardening is shown
in Appendix
A (Figures A1 and A2). Further, we also
note that while the estimated values of these parameters
lie in the range of literature studies for other structural
alloys,
33,44,46 their uniqueness is not guaranteed, that is,
alternate model parameters that can predict a similar
stress–strain response may also exist. Plastic flow param-
eters, such as the reference strain rate, _ε0; activation
energy for dislocation glide, ΔFg; shape parameters for
the enthalpy curve, p and q; and the thermal resistance
to dislocation glide, St, are calibrated by fitting the
temperature-dependent yield stress to corresponding
experimental values. The range of initial dislocation den-
sities has generally been reported in the order of
10
/C0 11 /C0 10/C0 12m/C0 2:60 Accordingly, we have assumed an
initial value of 1 /C2 10/C0 12 m/C0 2 for both mobile and immo-
bile dislocation densities. The dislocation evolutions
parameters ( k
M ,Rc, kI , and kD) are calibrated by fitting
the model to experimental response of strain hardening
during cyclic deformation. These values are in the same
range as earlier studies.
45,53,61,62 Specifically, the value of
the dislocation immobilization parameter, kI , has gener-
ally been assumed to be about 80% –90% of the dislocation
multiplication parameter, kM :44 Physically, these govern
the rate of generation of mobile dislocation density and
their conversion to immobile dislocation densities. The
dynamic recovery parameter, kD, generally governs
the hardening rate at higher values of plastic strain, that
is, the higher the value of this parameter, the higher the
saturation in the stress –strain response. A parametric
study of these dislocation evolution parameters has been
performed over a range of possible values and the results
are presented in terms of their effect on the uniaxial
stress–strain response in Appendix
A (Table A1). Simi-
larly, the kinematic hardening parameters, kχ1, kχ2, and
kχ3, were obtained by fitting the model response to the
experimental cyclic stress –strain data. Finally, model
parameters for cyclic softening, kCS and cCS, were
obtained by fitting the model predictions to the experi-
mental peak stress data. These parameters are given in
Table
3.
TABLE 3 Model parameters for dislocation strengthening,
evolution, backstress evolution, and cyclic softening obtained by fit
to the experimental data.
Parameter Value Meaning
_ε0 1 /C2 106s/C0 1 Reference strain rate
ΔFg 1 /C2 10/C0 19J Activation energy for
dislocation glide
p,q 0.3, 1.5 Shape factors for
activation energy curve
σt 100 MPa Thermal slip resistance
qρ 0.1 Dislocation Barrier
strength
ρm,ρi 1 /C2 1012,1 /C2 1012m/C0 2 Initial dislocation
densities
b 2:54 /C2 10/C0 10m Burgers vector
magnitude
kM 0.1 Dislocation
multiplication parameter
Rc 1:488 /C2 10/C0 9m Critical capture radius
kI 0.088 Dislocation
immobilization
parameter
k
D 100 Dynamic recovery
parameter
kχ1,kχ2,kχ3 1000, 120, 6 /C2 10/C0 6 Back stress evolution
parameters
kCS, cCS 0.1, 1 Cyclic softening
parameters
TABLE 2 Model parameters for precipitate strengthening due to the γ0 and γ00 precipitates.
APB energy ( γAPB) mJ
m2
Shear modulus
(μ) GPa
Burgers vector
magnitude (b) nm
Volume
fraction
Precipitate
size (nm)
γ0 207 78.2 0.254912 0.05 11
γ00 378.1 72.6 0.256255 0.14 10
KUMAR ET AL . 3271
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

5 | RESULTS AND DISCUSSION
5.1 | Yield stress prediction
The model was first used to predict the yield stress of IN
718 at room temperature (RT) and at 600 /C14 C. Further, two
different grain sizes were used for predicting the yield
stress at 600 /C14 C. The comparison of the predicted
yield stress with the corresponding experimental values 30
is shown in Figure 3. The predicted yield stress values at
RT and 600 /C14 C, with a grain size of 4 μm, are 1117 and
1052 MPa, respectively, and show reasonable comparison
with the experimental data, as seen in Figure
3. We have
also predicted the yield stress at 600 /C14 C for a different
grain size of 24 μm and compared with the corresponding
experimental data in Figure 3. The model predicts rela-
tively lower yield stress (by ≈10%) than the experimental
values for the 24- μm grain size at 600 /C14 C. While there
could be some uncertainties in the experimental mea-
surements, the lower values of predicted yield stresses
could also be due to the fact that we have not considered
any other microstructural changes for the 24- μm grain
size simulation. The yield stress comprises contributions
from grain size strengthening, solid solution strengthen-
ing, and precipitate strengthening. In our model, we have
only considered change in the grain size strengthening
for the 24- μm grain size simulation. Generally, a larger
grain size in the experimental microstructure would also
be associated with higher annealing times, which may
have led to a change in the microstructure chemistry and
the precipitate sizes. Due to a lack of relevant experimen-
tal measurements, we have not considered these micro-
structural variations in our simulations, and this may
have contributed to the lower predicted yield stress
values for the 24- μm grain size simulation at 600
/C14 C.
5.2 | Prediction of cyclic stress –strain
response
The constitutive model was then used to predict the
cyclic stress –strain response of IN 718 for a symmetrical,
fully reversed ( R-ratio of /C0 1) strain-controlled loading,
with strain amplitudes of 1.0%, 0.9%, 0.8%, 0.7%, and
0.6%, at a nominal strain rate of 10
/C0 3 s/C0 1 and tempera-
ture of 600
/C14
C. The material had a grain size of 4 μmi n
these cyclic loading tests. While strain amplitudes of 1.0%
and 0.6% were used to fitting the model to the experimen-
tal cyclic stress –strain response, the remaining tests were
used for model validation. Model predictions in terms of
the hysteresis loop for the 1st cycle, 20th cycle, and the
half-life cycle are plotted for the different strain ampli-
tudes and compared with the corresponding experimen-
tal data in Figure
4. The model predictions compare
reasonably well with the experimental data for all five
strain amplitudes. There is some difference in the predic-
tion of the peak stress at the end of the loading cycle,
especially for the strain amplitude of 0.9% at the 20th
FIGURE 3 Comparison of
simulated yield stress with the
experimental yield stress of IN 718 at RT
and 600
/C14
C for grain size of 4 μm and at
600
/C14
C for grain size of 4 and 24 μm. The
experimental data were obtained from
Banerjee et al. 30
3272 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

cycle. Nonetheless, model predictions are comparable
with the experimental counterparts for the overall trends.
The hysteresis loops get narrower with the decrease in
the strain amplitude. Note that the model is also able to
predict the elastic –plastic transition reasonably well at
different stages of cyclic loading.
5.3 | Prediction of cyclic softening
It was found in prior studies 30 that the IN 718 alloy
shows cyclic softening behavior during low cycle fatigue
loading. The cyclic hardening/softening behavior is gen-
erally quantified in terms of the peak stress at the end of
FIGURE 4 Predicted hysteresis loop and comparison with the corresponding experimental data for the 1st, 20th, and half-life cycles for
fully reversed cyclic loading ( R = /C0 1) under five different strain amplitudes of 1.0%, 0.9%,0.8%,0.7%, and 0.6% at 600
/C14
C.
KUMAR ET AL . 3273
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

the loading cycle. Depending on the strain amplitude, the
material may initially demonstrate a few cycles of cyclic
hardening, followed by cyclic softening (of the peak
stress). Figure 5 shows a comparison of the model-
predicted evolution of peak stress as a function of the
number of cycles, as compared with the corresponding
experimental data, for the different strain amplitudes.
Note that the number of cycles is plotted on the logarith-
mic scale.
It can be seen that the model predictions compare
qualitatively with the experimental data for all strain
amplitudes. There is progressive degradation in the peak
stress (representative of the material's strength) with the
increasing number of cycles for all strain amplitudes.
Further, the peak stress is higher for the higher strain
amplitude at any given cycle. Cyclic softening due to the
shearing of γ
00 precipitates is the primary mechanism
responsible for the observed cyclic softening. While there
is an increase in the isotropic hardening (dislocation den-
sity) and backstress with an increase in the number of
cycles (this contributes to the initial saturation in peak
stress for the first few cycles at 1.0% and 0.9% strain
amplitude), shearing of the precipitates leads to reduced
strength contribution of the material, which lowers the
peak stress. At a higher number of cycles, the model gen-
erally predicts a saturation in peak stress values as
observed from the flat curves toward the end of the
respective simulations. This is primarily due to the fact
that the mean precipitate size is not allowed to go below
0:5 nm in our simulations (cf. Equation
17). Once this
threshold precipitate size is reached, the drop in strength
contribution due to the precipitates saturates.
5.4 | Evolution of precipitate with cyclic
deformation
IN 718 exhibits cyclic hardening for the initial 2 –3 cycles,
followed by progressive softening during cyclic loading
till failure. As mentioned earlier, the primary contribu-
tion to this softening is due to the shearing of γ
00 precipi-
tates.30,51,63 When a dislocation interacts with a γ00
precipitate, it can either shear the precipitate or loop
around the precipitate depending upon the size of the
precipitate. Given that the size of γ00 precipitates is very
small in IN 718, they get sheared by the dislocations.
Under fully reversed cyclic loading condition, the
γ
00 precipitate present in the slip band gets sheared by the
leading dislocation. 38 After this initial shearing, trailing
dislocations in the same slip plane again shear the precip-
itate and regain the order structure which was destroyed
by the leading dislocation. This process is repeated in
each cycle, and the size of γ
00 precipitate reduces such that
it offers no resistance to dislocation movement. Given
that IN 718 is a precipitate-hardened superalloy, the size
of the precipitate influences the strength of the material
by its contribution to the precipitation-hardening compo-
nent ( Δσ
ppt in Section 3). Figure 6 shows model
FIGURE 5 Predicted evolution of
peak stress as a function of number of
cycles, as compared with the
corresponding experimental data, for
different strain amplitudes at 600
/C14
C.
[Colour figure can be viewed at
wileyonlinelibrary.com]
3274 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 12

predictions of the γ00precipitate size as a function of the
number of cycles for different strain amplitudes. Note
that the precipitate sizes are updated using the constitu-
tive model for precipitate shearing proposed in
Equation (
17). Initially, the rate of reduction in the pre-
cipitate size is relatively slow, while it increases during
the subsequent cycles for all strain amplitudes. This also
correlates with the observed decrease in peak stress
(cf. Figure
5), which gets accelerated at a higher number
of loading cycles.
Thin foils for TEM were prepared from fatigue-tested
specimens close to the fracture end, and electro polished
using 90% acetic + 10% perchloric acid employing 40-mA
current for TEM observation. Figure 7 shows representa-
tive TEM images from the failed microstructures for the
different strain amplitudes. The TEM dark field images
FIGURE 7 TEM micrographs showing the γ00 precipitates in LCF-tested specimens for strain amplitudes of (A) 1.0%, (B) 0.8%, and
(C) 0.6%, at 600
/C14
C, along with the corresponding size distribution. [Colour figure can be viewed at wileyonlinelibrary.com]
FIGURE 6 Model predictions of the
precipitate size with number of cycles
for different strain amplitudes at 600
/C14
C:
KUMAR ET AL . 3275
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 13

were captured using a super lattice spot of the diffraction
pattern, which is less intense; thus, it required higher
exposure time. This leads to drifting of the specimen
(i.e., 0.2 nm/min), which is unavoidable and leads to
blurring of the images. Further, to overcome this, we
have carried out atomic resolution HRTEM imaging,
showing the sheared zone within a γ
00 precipitate in
Figure 8. Clear evidence of shearing of the γ00 precipitates
can be observed in certain cases (see highlighted region
in Figures 7 and 8), which indicates that the precipitates
are sheared into two halves by the glide dislocations. The
HRTEM image in Figure
8 is in contrast with
the HRTEM images of the unsheared γ00 precipitates
shown in Figures 2C and B1 and shows clear evidence of
change in the lattice arrangements inside the sheared
zone of the γ
00 precipitate. Further, the size distribution of
the precipitates in these TEM images is also plotted. The
measured mean precipitate size is in the range of 1 –2n m
for all three strain amplitudes. As can be seen from
Figure
6, the simulations predict the precipitate size to be
approximately 0.5 nm.
Thus, the precipitate size predicted from simulations
is in the same range as those measured from the TEM
micrographs. It should be noted that very few experimen-
tal studies showing clear evidence of the shearing of γ00
precipitates are available in the literature. 30,63 This is pri-
marily due to the very small size of the precipitates,
which makes them difficult to characterize. Figure 8
shows, the sheared zone inside the γ00 precipitate. Our
TEM micrographs provide such evidence, which is then
used to guide and validate our constitutive models.
A parametric study of the effect of changing kCS,
which governs the rate of precipitate shearing in
Equation ( 14), was performed for the simulation with a
FIGURE 8 TEM image of SA 0.6% showing sheared γ00 precipitates, along with the HRTEM image showing the sheared zone within the
precipitate. [Colour figure can be viewed at wileyonlinelibrary.com]
FIGURE 9 (A) Reduction of
peak stress and (B) evolution of
precipitate with number of cycles for
different values of k
CS. [Colour figure
can be viewed at wileyonlinelibrary.
com]
3276 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 14

strain amplitude of 1.0%. This is plotted in terms of the
reduction of peak stress, Δσsoftening, and the precipitate
size for different values of kCS in Figure 9. kCS was found
to have a significant influence on the rate of cyclic soften-
ing and the size of the precipitates. It was found from the
parametric study that k
CS = 0.1 predicts cyclic softening,
interpreted in terms of Δσsoftening, qualitatively similar to
the corresponding experimental softening rate for IN
718, which has been plotted using open circles. In order
to predict cyclic softening for other alloys, this parameter
needs to be calibrated to the relevant experimental data.
6 | CONCLUSIONS
A dislocation density-based J2 plasticity model has been
developed to predict the cyclic deformation behavior of
IN 718 in this work. The physically-based constitutive
modeling framework considers microstructure-sensitive
strengthening mechanisms, including grain size, disloca-
tion, solid solution, and precipitate strengthening, which
are commonly observed in Ni-based superalloys. Further,
we have developed a constitutive model to account for
the shearing of γ
00 precipitates during cyclic deformation,
which has been identified as the primary contributor to
cyclic softening in Ni-based superalloys. This is in con-
trast with previous modeling studies that have accounted
for this softening behavior either empirically or in more
computationally expensive crystal plasticity frameworks.
Development and implementation of physically-based
constitutive equations for the above-mentioned strength-
ening mechanisms and microstructure evolution due to
precipitate shearing, which contribute to cyclic softening
of Ni-based superalloys, in a computationally efficient J
2
plasticity framework (as compared with a crystal plastic-
ity framework) is the novel contribution of this work.
The following conclusions were drawn based on the
model predictions:
• The constitutive model can qualitatively predict the
yield stress at room temperature and at 600
/C14
C for
microstructures with different initial grain sizes.
• The model can predict the cyclic stress –strain response
over a range of strain amplitudes, from 0.6% to 1.0%,
for fully reversed cyclic loading at 600
/C14
C with reason-
able accuracy.
• Model predictions of peak stress as a function of the
number of cycles are in agreement with
the experiments.
• The reduction in peak stress with the number of cycles
can be correlated with the decrease in precipitate size
and is the primary contributor to the predicted cyclic
softening.
• Model predictions of the sheared precipitate sizes are
in qualitative agreement with the experimental TEM
measurements.
NOMENCLATURE
T absolute temperature
ΔF
g activation energy
γAPB anti-phase boundary (APB) energy
σa athermal stress resistance
χ backstress tensor
kχ backstress parameter
k Boltzmann constant
b Burger vector
_ε
p
cyc cyclic effective plastic strain rate
S deviatoric stress tensor
dγ00 size of γ00 precipitate
Δσdislocation dislocation strengthening
qρ dislocation barrier strength
kM , Rc, dislocation interaction kI and kD material
parameter
TL dislocation line tension
Np direction of the flow
_ρdyn dynamic recovery rate of immobile
dislocations
σ effective stress
ci element mole fraction
_ε
p
equivalent plastic strain rate
σf flow stress
Δσgb grain boundary strengthening
J2 second invariant of the deviatoric stress
minus the backstress tensor
kHP Hall–Petch coefficient
kCS,cCS material parameters governing precipitate
shearing
λ mean free path
d mean grain size
ds mean planar size
ρM mobile dislocation density
_ρmul multiplication rate of mobile dislocation
_ρmutual mutual annihilation rate of dislocation
Nγ00 number density of γ00 precipitates
ρI immobile dislocation density
_εp plastic strain rate tensor
Δσppt precipitate strengthening
_ε0 reference strain rate
p and q shape parameters
G shear modulus
Δσss solid solution strengthening
ks,i solid solution strengthening coefficient
KUMAR ET AL . 3277
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 15

Ls spacing between precipitate
σt thermal stress resistance
_ρtrap trapping rate of mobile dislocations
f volume fraction of the γ matrix
f p volume fraction of precipitate
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are avail-
able from the corresponding author upon reasonable
request.
ORCID
Shivam Kumar
https://orcid.org/0000-0002-2425-9557
Anirban Patra https://orcid.org/0000-0002-9928-0959
J. K. Sahu https://orcid.org/0000-0002-9486-3055
REFERENCES
1. Kozar RW, Suzuki A, Milligan WW, Schirra JJ, Savage MF,
Pollock TM. Strengthening mechanisms in polycrystalline mul-
timodal nickel-base superalloys. Metall Mater Trans a Phys
Metall Mater Sci . 2009;40(7):1588-1603. doi:
10.1007/s11661-
009-9858-5
2. Lancaster RJ, Whittaker MT, Williams SJ. A review of thermo-
mechanical fatigue behaviour in polycrystalline nickel superal-
loys for turbine disc applications. Mater High Temp . 2013;30(1):
2-12. doi:
10.3184/096034013X13630238172260
3. Kawagoishi N, Chen Q, Yan N, Goto M, Wang Q, Ohzono Y.
Fracture mechanism in fatigue of nickel-based superalloy
Inconel 718 at elevated temperatures. J Solid Mech Mater Eng .
2007;1(6):734-743. doi:10.1299/jmmp.1.734
4. Fournier D, Pineau A. Low cycle fatigue behavior of Inconel
718 at 298 K and 823 K. Metall Trans a . 1977;8(7):1095-1105.
doi:10.1007/BF02667395
5. Pineau A, Antolovich SD. High temperature fatigue of nickel-
base superalloys —a review with special emphasis on deforma-
tion modes and oxidation. Eng Fail Anal . 2009;16(8):2668-2697.
doi:10.1016/j.engfailanal.2009.01.010
6. Pollock TM, Tin S. Nickel-based superalloys for advanced tur-
bine engines: chemistry, microstructure, and properties.
J Propuls Power . 2006;22(2):361-374. doi:
10.2514/1.18239
7. Chaboche JL. Constitutive equations for cyclic plasticity and
cyclic viscoplasticity. Int J Plast. 1989;5(3):247-302. doi:10.1016/
0749-6419(89)90015-6
8. Chaboche J-L, Kanouté P, Azzouz F. Cyclic inelastic constitu-
tive equations and their impact on the fatigue life predictions.
Int J Plast. 2012;35:44-66. doi:
10.1016/j.ijplas.2012.01.010
9. Dong C, Yang X, Shi D, Yu H. Modeling of anisotropic tensile
and cyclic viscoplastic behavior of a nickel-base directionally
solidified superalloy. Mater des . 2014;55:966-978. doi: 10.1016/j.
matdes.2013.10.085
10. Zhan ZL, Tong J. A study of cyclic plasticity and viscoplasticity
in a new nickel-based superalloy using unified constitutive
equations. Part I: evaluation and determination of material
parameters. Mech Mater . 2007;39(1):64-72. doi:
10.1016/j.
mechmat.2006.01.005
11. Zhan ZL, Tong J. A study of cyclic plasticity and viscoplasticity
in a new nickel-based superalloy using unified constitutive
equations. Part II: simulation of cyclic stress relaxation. Mech
Mater. 2007;39(1):73-80. doi: 10.1016/j.mechmat.2006.01.006
12. Becker M, Hackenberg HP. A constitutive model for rate
dependent and rate independent inelasticity. Application to
IN718. Int J Plast. 2011;27(4):596-619. doi:
10.1016/j.ijplas.2010.
08.005
13. Stoltz RE, Pineau AG. Dislocation-precipitate interaction and
cyclic stress-strain behavior of a γ' strengthened superalloy.
Mater Sci Eng . 1978;34(3):275-284. doi: 10.1016/0025-5416(78)
90060-5
14. Wang K, Jing H, Xu L, Han Y, Zhao L, Song K. Cyclic response
and dislocation evolution of a nickel-based superalloy under
low cycle fatigue deformation. Mater Sci Eng a . 2021;814:
141225. doi:10.1016/j.msea.2021.141225
15. Paul SK, Sivaprasad S, Dhar S, Tarafder S. Cyclic plastic defor-
mation and cyclic hardening/softening behavior in 304LN
stainless steel. Theor Appl Fract Mech . 2010;54(1):63-70. doi:
10.
1016/j.tafmec.2010.06.016
16. Xie XF, Jiang W, Chen J, Zhang X, Tu ST. Cyclic
hardening/softening behavior of 316L stainless steel at elevated
temperature including strain-rate and strain-range dependence:
experimental and damage-coupled constitutive modeling. Int J
Plast. 2019;114:196-214. doi:
10.1016/j.ijplas.2018.11.001
17. Fang D, Berkovits A. Mean stress models for low-cycle fatigue
of a nickel-base superalloy. Int J Fatigue. 1994;16(6):429-437.
doi:10.1016/0142-1123(94)90458-8
18. Tong J. Modelling of cyclic plasticity and viscoplasticity of
a nickel-based alloy using Chaboche constitutive equations.
Int J Fatigue. 2004;26(8):829-837. doi:
10.1016/j.ijfatigue.2004.
01.002
19. Cornet C, Zhao LG, Tong J. A study of cyclic behaviour of a
nickel-based superalloy at elevated temperature using
a viscoplastic-damage model. Int J Fatigue . 2011;33(2):241-249.
doi:10.1016/j.ijfatigue.2010.08.016
20. Brommesson R, Ekh M, Persson C. Experimental observations
and modelling of cyclic and relaxation behaviour of the Ni-
based superalloy Haynes 282. Int J Fatigue. 2016;87:180-191.
doi:
10.1016/j.ijfatigue.2016.01.027
21. Cruzado A, LLorca J, Segurado J. Modeling cyclic deformation
of Inconel 718 superalloy by means of crystal plasticity and
computational homogenization. Int J Solids Struct . 2017;
122-123:148-161. doi:
10.1016/j.ijsolstr.2017.06.014
22. Agaram S, Kanjarla AK, Bhuvaraghan B, Srinivasan SM. Dislo-
cation density based crystal plasticity model incorporating the
effect of precipitates in IN718 under monotonic and cyclic
deformation. Int J Plast . 2021;141:102990. doi: 10.1016/j.ijplas.
2021.102990
23. Le /C19on-C/C19azares FD, Monni F, Jackson T, Galindo-Nava EI,
Rae CMF. Stress response and microstructural evolution of
nickel-based superalloys during low cycle fatigue: physics-
based modelling of cyclic hardening and softening. Int J Plast.
2020;128:102682. doi:
10.1016/j.ijplas.2020.102682
24. le Graverend J-B. Crystal-plasticity modeling of monotonic and
cyclic softening in Inconel 718 superalloy. Int J Mech Sci . 2023;
239:107871. doi:10.1016/j.ijmecsci.2022.107871
25. Shenoy M, Tjiptowidjojo Y, McDowell D. Microstructure-
sensitive modeling of polycrystalline IN 100. Int J Plast. 2008;
24(10):1694-1730. doi:10.1016/j.ijplas.2008.01.001
26. Lin B, Zhao LG, Tong J, Christ HJ. Crystal plasticity modeling
of cyclic deformation for a polycrystalline nickel-based
3278 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 16

superalloy at high temperature. Mater Sci Eng a . 2010;527(15):
3581-3587. doi:10.1016/j.msea.2010.02.045
27. Ghorbanpour S, Zecevic M, Kumar A, et al. A crystal plasticity
model incorporating the effects of precipitates in superalloys:
application to tensile, compressive, and cyclic deformation of
Inconel 718. Int J Plast. 2017;99:162-185. doi:
10.1016/j.ijplas.
2017.09.006
28. Zhang WT, Jiang R, Zhao Y, et al. Effects of temperature and
microstructure on low cycle fatigue behaviour of a PM Ni-
based superalloy: EBSD assessment and crystal plasticity simu-
lation. Int J Fatigue. 2022;159:106818. doi:
10.1016/j.ijfatigue.
2022.106818
29. Chaudhary S, Guruprasad PJ, Patra A. Crystal plasticity consti-
tutive modeling of tensile, creep and cyclic deformation in sin-
gle crystal Ni-based superalloys. Mech Mater . 2022;174:104474.
doi:
10.1016/j.mechmat.2022.104474
30. Banerjee A, Sahu JK, Paulose N, Fernando CD, Ghosh RN.
Micromechanism of cyclic plastic deformation of alloy IN
718 at 600
/C14 C. Fatigue Fract Eng Mater Struct . 2016;39(7):877-
885. doi:10.1111/ffe.12406
31. Khan AS, Huang S. Continuum Theory of Plasticity . John
Wiley & Sons; 1995.
32. Ellis BD, Haider H, Priddy MW, Patra A. Integrated computa-
tional design of three-phase Mo –Si–B alloy turbine blade for
high-temperature aerospace applications. Integr Mater Manuf
Innov. 2021;10(2):245-264. doi: 10.1007/s40192-021-00207-6
33. Khandelwal S, Basu S, Patra A. A machine learning-based surro-
gate modeling framework for predicting the history-dependent
deformation of dual phase microstructures. Mater Today Com-
mun. 2021;29:102914. doi:
10.1016/j.mtcomm.2021.102914
34. Basu S, Patra A, Jaya BN, Ganguly S, Dutta M, Samajdar I.
Study of microstructure-property correlations in dual phase
steels for achieving enhanced strength and reduced strain parti-
tioning. Materialia. 2022;25:101522. doi: 10.1016/j.mtla.2022.
101522
35. Follansbee PS, Kocks UF. A constitutive description of the
deformation of copper based on the use of the mechanical
threshold stress as an internal state variable. Acta Metall. 1988;
36(1):81-93. doi:
10.1016/0001-6160(88)90030-2
36. Kocks UF, Argon AS, Ashby MF. Thermodynamics and Kinet-
ics of Slip. Volume 19 of Progress in materials science . Pergamon
Press; 1975. ISBN: 0080179649, 9780080179643.
37. Gypen LA, Deruyttere A. Multi-component solid solution
hardening—part 1 proposed model. J Mater Sci . 1977;12(5):
1028-1033. doi:10.1007/BF00540987
38. Sundararaman M, Mukhopadhyay P, Banerjee S. Deformation
behaviour of γ00 strengthened Inconel 718. Acta Metall . 1988;
36(4):847-864. doi:10.1016/0001-6160(88)90139-3
39. Chaturvedi MC, Han YF. Strengthening mechanisms in
Inconel 718 superalloy. Met Sci . 1983;17(3):1-5. doi: 10.1179/
030634583790421032
40. Li W, Ma J, Kou H, et al. Modeling the effect of temperature on
the yield strength of precipitation strengthening Ni-base super-
alloys. Int J Plast. 2019;116(January):143-158. doi:
10.1016/j.
ijplas.2019.01.002
41. Keshavarz S, Ghosh S, Reid ACE, Langer SA. A non-Schmid
crystal plasticity finite element approach to multi-scale model-
ing of nickel-based superalloys. Acta Mater . 2016;114:106-115.
doi:10.1016/j.actamat.2016.05.016
42. Ardell AJ. Precipitation hardening. Metall Trans a . 1985;16(2):
75-83. doi:10.1063/1.1714842
43. Voyiadjis GZ, Yaghoobi M. Nonlocal continuum plasticity. In:
Size Effects in Plasticity . Elsevier; 2019:81-190. doi: 10.1016/
B978-0-12-812236-5.00002-5
44. Patra A, Chaudhary S, Pai N, et al. ρ-CP: open source disloca-
tion density based crystal plasticity framework for simulating
temperature- and strain rate-dependent deformation. Comput
Mater Sci . 2023;224:112182. doi: 10.1016/j.commatsci.2023.
112182
45. Ranjan D, Narayanan S, Kadau K, Patra A. Crystal plasticity
modeling of non-Schmid yield behavior: from Ni3Al single
crystals to Ni-based superalloys. Model Simul Mater Sci Eng .
2021;29(5):55005. doi:10.1088/1361-651X/abd621
46. Chaudhary S, Pai N, Rao GA, et al. Competitive role of primary
γ' precipitates and annealing twins on the heterogeneous defor-
mation of a polycrystalline ni-based superalloy: crystal plastic-
ity modeling and experiments. J Alloys Compd . 2023;967:
171783. doi:
10.1016/j.jallcom.2023.171783
47. Deng W, Xu J, Hu Y, Huang Z, Jiang L. Isothermal and ther-
momechanical fatigue behavior of Inconel 718 superalloy.
Mater Sci Eng a . 2019;742:813-819. doi:
10.1016/j.msea.2018.
11.052
48. Prasad K, Sarkar R, Ghosal P, Kumar V, Sundararaman M.
High temperature low cycle fatigue deformation behaviour of
forged IN 718 superalloy turbine disc. Mater Sci Eng a . 2013;
568:239-245. doi:10.1016/j.msea.2012.12.069
49. Xiao L, Chen DL, Chaturvedi MC. Low-cycle fatigue behavior
of INCONEL 718 superalloy with different concentrations of
boron at room temperature. Metall Mater Trans a Phys Metall
Mater Sci . 2005;36(10):2671-2684. doi:
10.1007/s11661-005-
0264-3
50. Xiao L, Chen DL, Chaturvedi MC. Cyclic deformation mecha-
nisms of precipitation-hardened Inconel 718 superalloy. Mater
Sci Eng a . 2008;483-484(1-2 C):369-372. doi: 10.1016/j.msea.
2006.10.181
51. Xiao L, Chen DL, Chaturvedi MC. Shearing of γ00 precipitates
and formation of planar slip bands in Inconel 718 during cyclic
deformation. Scr Mater . 2005;52(7):603-607. doi: 10.1016/j.
scriptamat.2004.11.023
52. Kalluri S, Rao KBS, Halford GR, McGaw MA. Deformation
mechanisms and fatigue behavior of prestrained Inconel
718 superalloy. In: Superalloys 718, 625, 706 and Various
Derivatives (1997) . TMS; 2012:595-606. doi:
10.7449/1997/
superalloys_1997_595_606
53. Patra A, McDowell DL. Continuum modeling of localized
deformation in irradiated bcc materials. J Nucl Mater . 2013;
432(1–3):414-427. doi:10.1016/j.jnucmat.2012.08.021
54. Prasannavenkatesan R. Microstructure-Sensitive Fatigue Model-
ing of Heat Treated and Shot Peened Martensitic Gear Steels .
PhD Thesis. Georg Inst Technol; 2009.
55. Aba-Perea PE, Pirling T, Withers PJ, Kelleher J, Kabra S,
Preuss M. Determination of the high temperature elastic prop-
erties and diffraction elastic constants of Ni-base superalloys.
Mater des. 2016;89:856-863. doi:
10.1016/j.matdes.2015.09.152
56. Mishima Y, Ochiai S, Hamao N, Yodogawa M, Suzuki T. Solid
solution hardening of nickel —role of transition metal and
B-subgroup solutes. Trans Japan Inst Met . 1986;27(9):656-664.
doi:10.2320/matertrans1960.27.656
KUMAR ET AL . 3279
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 17

57. Roth HA, Davis CL, Thomson RC. Modeling solid solution
strengthening in nickel alloys. Metall Mater Trans a Phys
Metall Mater Sci . 1997;28(6):1329-1335. doi: 10.1007/s11661-
997-0268-2
58. Liu L, Tanaka K, Hirose A, Kobayashi KF. Effects of precipita-
tion phases on the hydrogen embrittlement sensitivity of
Inconel 718. Sci Technol Adv Mater . 2002;3(4):335-344. doi: 10.
1016/S1468-6996(02)00039-6
59. Wang C, Li R. Effect of double aging treatment on structure in
Inconel 718 alloy. J Mater Sci . 2004;39(7):2593-2595. doi: 10.
1023/B:JMSC.0000020036.96777.9c
60. Pollock TM, Argon AS. Directional coarsening in nickel-base
single crystals with high volume fractions of coherent precipi-
tates. Acta Metall Mater . 1994;42(6):1859-1874. doi: 10.1016/
0956-7151(94)90011-6
61. Patra A. Modeling the Mechanical Behavior and Deformed
Microstructure of Irradiated BCC Materials Using Continuum
Crystal Plasticity. PhD Thesis. Georg Inst Technol; 2013.
62. Patra A, Zhu T, McDowell DL. Constitutive equations for
modeling non-Schmid effects in single crystal bcc-Fe at low
and ambient temperatures. Int J Plast. 2014;59:1-14. doi:
10.
1016/j.ijplas.2014.03.016
63. Kalluri S, Rao KBS, Halford GR, McGaw MA. Deformation and
damage mechanisms in Inconel 718 superalloy. In: Superalloys
718, 625, 706 and Various Derivatives (1994) . TMS; 1994:593-
606. doi:10.7449/1994/Superalloys_1994_593_606
64. Park SJ, Kim KS, Kim HS. Ratcheting behaviour and mean
stress considerations in uniaxial low-cycle fatigue of Inconel
718 at 649
/C14 C. Published online 2007:1076-1083. 10.1111/j.
1460-2695.2007.01177.x, 30, 11.
How to cite this article: Kumar S, Patra A,
Sahu JK. Dislocation density-based constitutive
model for cyclic deformation and softening of Ni-
based superalloys. Fatigue Fract Eng Mater Struct .
2024;47(9):3264‐3284. doi:10.1111/ffe.14367
3280 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 18

A P P E N D I X A : PARAMETRIC STUDY OF THE EFFECT OF VARIOUS MODEL PARAMETERS ON THE
CYCLIC STRESS–STRAIN RESPONSE
The parameters affecting the initial yield stress, _ε0, p, q, and ΔFg, were first varied parametrically in simulations
1 through 11, while parameters affecting the dislocation evolution and corresponding strengthening, kM ,kI ,kD were var-
ied parametrically in simulations 12 through 18 to study their effect on the predicted cyclic stress –strain response in the
1st and 20th cycles, and compared with the corresponding experimental data for a strain amplitude of 1% at 600
/C14
C.
“Sim 1 ” represents the best-fit model obtained by trial and error, which has been used for predicting the results pre-
sented in the main text.
TABLE A1 Values of the model
parameters varied parametrically to
study their effect on the predicted cyclic
stress–strain response.
_ε
0 pq ΔFg kM kI kD
Sim 1 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 0.1 0.088 100
Sim 2 1 /C2 101s/C0 1 0.3 1.5 1 /C2 10/C0 19J 0.1 0.088 100
Sim 3 1 /C2 109s/C0 1 0.3 1.5 1 /C2 10/C0 19J 0.1 0.088 100
Sim 4 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 18J 0.1 0.088 100
Sim 5 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 17J 0.1 0.088 100
Sim 6 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 16J 0.1 0.088 100
Sim 7 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 20J 0.1 0.088 100
Sim 8 1 /C2 106s/C0 1 0.1 1.5 1 /C2 10/C0 19J 0.1 0.088 100
Sim 9 1 /C2 106s/C0 1 0.1 1 1 /C2 10/C0 19J 0.1 0.088 100
Sim 10 1 /C2 106s/C0 1 111 /C2 10/C0 19J 0.1 0.088 100
Sim 11 1 /C2 106s/C0 1 121 /C2 10/C0 19J 0.1 0.088 100
Sim 12 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 1.0 0.088 100
Sim 13 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 2.0 0.088 100
Sim 14 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 2 0.5 100
Sim 15 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 2 1 100
Sim 16 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 2 2 100
Sim 17 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 0.1 0.088 1,000
Sim 18 1 /C2 106s/C0 1 0.3 1.5 1 /C2 10/C0 19J 0.1 0.088 3,000
KUMAR ET AL . 3281
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 19

FIGURE A1 Predicted cyclic stress –strain response using different values of _ε0, p, q, and ΔFg for the 1st and 20th cycles for a strain
amplitude of 1.0% at 600
/C14
C. Sim 1 represents the best model using which predictions have been presented in the main text. [Colour figure
can be viewed at wileyonlinelibrary.com]
3282 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 20

FIGURE A2 Predicted cyclic stress –strain response using
different values of kM , kI , and kD for the 1st and 20th cycles for a
strain amplitude of 1.0% at 600
/C14
C. Sim 1 represents the best model
using which predictions have been presented in the main text.
[Colour figure can be viewed at
wileyonlinelibrary.com]
KUMAR ET AL . 3283
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 21

A P P E N D I X B : TEM CHARACTERIZATION OF AS-RECEIVED MATERIAL
A P P E N D I X C : MODEL PREDICTIONS OF RATCHETING STRAIN
While the constitutive model has been used to predict the cyclic softening behavior of IN 718 and compared with rele-
vant experiments in the present work, it can also be used to predict the ratcheting behavior during cyclic deformation.
Figure
C1 shows the evolution of uniaxial ratcheting strain with number for different stress amplitudes at a constant
value of mean stress, while Figure C2 shows the evolution of uniaxial ratcheting strain with number of cycles for differ-
ent values of mean stress at a constant stress amplitude. The ratcheting strain increases with increasing stress amplitude
at a constant value of mean stress. On the other hand, the ratcheting strain increases monotonically for positive values
of mean stress and is higher for a higher mean stress and decreases monotonically for a negative mean stress with
increasing number of cycles at a constant stress amplitude. We do not have experimental measurements for our mate-
rial to compare these ratcheting strain predictions with. However, our model predictions are in qualitative agreement
with experimental measurements reported for IN 718 in the literature.
64 This behavior will be investigated in more
details in future work.
FIGURE C1 Evolution of ratcheting strain with number of
cycles for different stress amplitudes and mean stress of 50 MPa.
[Colour figure can be viewed at
wileyonlinelibrary.com]
FIGURE C2 Evolution of ratcheting strain with number of
cycles for different mean stress values and stress amplitude of
850 MPa. [Colour figure can be viewed at
wileyonlinelibrary.com]
FIGURE B1 HRTEM image of (A) γ00
precipitate in the as-received material and
(B) magnified image of the γ00 precipitate
showing an “unsheared” lattice inside the
precipitate. [Colour figure can be viewed at
wileyonlinelibrary.com]
3284 KUMAR ET AL .
 14602695, 2024, 9, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.14367 by Xian Jiaotong University, Wiley Online Library on [02/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
