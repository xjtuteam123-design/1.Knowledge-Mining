# 1-s2.0-S0167663622002381-main

<!-- source: D:\总文献\1-s2.0-S0167663622002381-main.pdf -->
<!-- file_sha256: e9d50dd7da0187d5cd89d0ad0c7fb4030fda5533ba003f6fa991e87ea1c04918 -->

## Page 1

Mechanics of Materials 174 (2022) 104474
Available online 20 September 2022
0167-6636/© 2022 Elsevier Ltd. All rights reserved.
Contents lists available at ScienceDirect
Mechanics of Materials
journal homepage: www.elsevier.com/locate/mecmat
Research paper
Crystal plasticity constitutive modeling of tensile, creep and cyclic
deformation in single crystal Ni-based superalloys
Suketa Chaudhary a, P.J. Guruprasadb, Anirban Patraa,∗
a Department of Metallurgical Engineering and Materials Science, Indian Institute of Technology Bombay, Mumbai, 400076, Maharashtra, India
b Department of Aerospace Engineering, Indian Institute of Technology Bombay, Mumbai, 400076, Maharashtra, India
A R T I C L E I N F O
Keywords:
Ni-based superalloys
Crystal plasticity
Creep
Cyclic
Constitutive model
A B S T R A C T
A microstructure-sensitive crystal plasticity constitutive framework is proposed for simulating the tensile,
cyclic, and creep response of single crystal Ni-based superalloys. In this framework, a non-Schmid model is
used to account for the orientation- and temperature-dependent yield anisotropy. A model for the evolution
of the slip system-level backstress is developed to simulate the cyclic response. The model accounts for the
effect of microstructural features like precipitate volume fraction and size, and matrix channel width, on
the associated hardening mechanisms. A physical model for creep deformation has also been developed that
accounts for dislocation climb normal to the slip plane and the microstructure evolution due to rafting and
isotropic coarsening of the precipitates. Application of the model is demonstrated by predicting the orientation-
and temperature-dependent thermo-mechanical deformation of two single crystal superalloys, CMSX-4 and
PWA-1484. The model is calibrated to the experimental tensile, cyclic and creep response for these alloys.
Finally, the model is qualitatively validated by predicting the creep-fatigue interactions for different loading
orientations and a range of thermo-mechanical conditions for CMSX-4 and PWA-1484.
1. Introduction
Nickel-based superalloys are widely used in applications that re-
quire superior elevated temperature properties like high strength, high
toughness, relatively high creep resistance and thermal fatigue resis-
tance (Geddes et al., 2010). Turbine blades and turbine discs of modern
gas turbines, burner cans and vanes are some engineering applications
where Ni-based superalloys are used (Antolovich, 1996). The mechani-
cal properties of Ni-based superalloys are governed by their underlying
microstructure. Generally, these alloys comprise of a two-phase mi-
crostructure: a Ni-rich solid solution, with Face-Centered Cubic (FCC)
crystal structure, called the 𝛾 phase, and coherent𝐿12-type, long-range
ordered intermetallic Ni3Al precipitates, called the𝛾 ′ phase (Murakumo
et al. , 2004 ). Several factors influence the deformation behavior of
these alloys: (i) Orowan looping of matrix dislocations around pre-
cipitates (Fedelich et al. , 2009); (ii) interface coherency stress ( Tinga
et al., 2008); (iii) activation of cube slip in the 𝛾 ′ phase (Tinga et al. ,
2009b; Wang et al. , 2016); and (iv) shearing of precipitates by super
dislocations, which leads to the formation of Anti-Phase Boundaries
(APBs) (Allan, 1995; Keshavarz and Ghosh , 2015). These factors con-
tribute to anisotropic, orientation- and temperature-dependent defor-
mation in Ni-based superalloys ( Ranjan et al. , 2021 ). Contrary to
conventional metals and alloys, these superalloys show an anomalous
∗ Corresponding author.
E-mail address: anirbanpatra@iitb.ac.in (A. Patra).
yield behavior, with little or no decrease in yield strength with tem-
perature up to a certain value, after which yield strength decreases.
This makes them suitable for use in elevated temperature applica-
tions ( Westbrook, 1957 ; Flinn , 1960 ; Shenoy et al. , 2008 ). Further,
rafting, directional coarsening of cuboidal 𝛾 ′ phase into lamellar struc-
tures, usually occurs at temperatures above 900◦C, which significantly
affects the creep deformation of superalloy single crystals ( Fan et al. ,
2015).
Creep deformation of single crystal superalloys is anisotropic and
depends on the stress, temperature and loading orientation (Sims et al.,
1987; Stouffer and Dame , 1996 ; Xia et al. , 2020 ). Single crystal su-
peralloys show tertiary creep behavior, along with a small amount of
steady-state creep at temperatures greater than 850 ◦C (Ghosh et al. ,
1990; Reed, 2008; Titus et al. , 2012). Deformation near [001] crystal
orientations primarily occurs due to the glide/climb of dislocation
on the octahedral slip systems ⟨111⟩{1̄10} (Pollock and Argon , 1994).
Glide/climb of dislocations on the ⟨001⟩{1̄10} cube slip systems have
been observed near the [111] crystal orientation at high tempera-
tures (Sun and Hazzledine , 1996; Matan et al. , 1999a). Although the
role of cube slip on deformation is not yet fully understood, but ex-
perimental observations by Clement et al. (1991), Österle et al. (2000),
Tinga et al. (2009b), Wang et al. (2016) are indicative of the activation
https://doi.org/10.1016/j.mechmat.2022.104474
Received 26 April 2022; Received in revised form 8 September 2022; Accepted 14 September 2022

## Page 2

Mechanics of Materials 174 (2022) 104474
2
S. Chaudhary et al.
of cube slip near the [111] orientations. Rafting of 𝛾 ′ precipitates
was first observed in Ni-based superalloys by Webster and Sullivan
(1967). It strongly depends on the elastic constants of 𝛾/𝛾 ′ phases,
the sign of applied stress and lattice misfits (Chang and Allen, 1991;
Ignat et al., 1993; Pollock and Argon, 1994; Nabarro, 1996; Svoboda
and Lukas, 1996; Laberge et al., 1997; Ohashi et al., 1997; Henderson
et al., 1998; Mughrabi and Tetzlaff, 2000; Epishin et al., 2000; Titus
et al., 2012; Mughrabi, 2014). Experimental studies have revealed that
rafting occurs parallel (or perpendicular) to the loading axis under
compression (or tension) for alloys with negative lattice misfit (Lukáš
et al., 1996). It was also reported that rafting does not occur during
creep loading along the [111] orientation (Liu et al., 2008; Yu et al.,
2013).
Several continuum crystal plasticity models have been developed to
predict the temperature and orientation-dependent deformation behav-
ior of Ni-based superalloys (Ghosh et al., 1990; Qin and Bassani, 1992;
Allan, 1995; Brehm and Glatzel, 1999; MacLachlan and Knowles, 2000;
Ma et al., 2008; Shenoy et al., 2008; Tinga et al., 2009a; Staroselsky
and Cassenti, 2011; Vattré and Fedelich, 2011; Le Graverend et al.,
2014; Keshavarz and Ghosh, 2015; Keshavarz et al., 2016; Ghorbanpour
et al., 2017; Rodas and Neu, 2018; Yu et al., 2020; Agaram et al.,
2021; Gupta and Bronkhorst, 2021; Ranjan et al., 2021). A power law
model, with consideration for the shearing of the ⟨112⟩ super-partials,
was proposed by MacLachlan and Knowles (2000). This model was
able to predict the creep response for the [001] and [111] loading
orientations. Ma et al. (2008) proposed a dislocation density-based
crystal plasticity model, with consideration for climb in the precipitates
and a creep flow rule. Model predictions were in good agreement for
all the creep stages for the [001] orientations. Le Graverend et al.
(2014) developed a microstructure sensitive model to investigate non-
isothermal creep, fatigue, and creep-fatigue response. However, this
model is only valid for creep of single crystal alloys with negative
lattice misfit under tension. Keshavarz and Ghosh (2015) proposed a
dislocation density based non-Schmid crystal plasticity model to predict
anomalous thermo-mechanical behavior for Ni3Al single crystals. Gupta
and Bronkhorst (2021) proposed a crystal plasticity model with sep-
arate flow rules for the 𝛾 and 𝛾 ′ phases that includes the effects of
strengthening mechanisms like Orowan hardening, 𝛾 ′ contribution to
initial slip resistance, and Anti-Phase Boundary (APB) shearing of 𝛾 ′
phase.
A number of studies have proposed crystal viscoplasticity models
to capture the creep-fatigue interactions. Rodas and Neu (2018) have
extended the model proposed by Ma et al. (2008) to predict 3-D
creep-fatigue interactions by adding backstress formulations, strain rate
sensitivity exponent and dislocation evolution. Effect of orientation
on the mechanical response of single crystal alloys has been modeled
and compared with experiments by Sabnis et al. (2013), Su et al.
(2020). Crystal plasticity constitutive models have also been proposed
for polycrystalline Ni-based superalloys (Shenoy, 2006; Shenoy et al.,
2008; Zhang et al., 2015; Ghorbanpour et al., 2017; Phan et al., 2017;
León-Cázares et al., 2020; Sun et al., 2020; Agaram et al., 2021;
Fernandez-Zelaia et al., 2022). Further, macroplasticity models have
also been proposed to predict the thermo-mechanical deformation of
Ni-based superalloys (Chaboche et al., 2013; Lindström et al., 2022).
In addition to the mechanical properties, the microstructure of
Ni-based superalloys evolves during creep deformation at elevated tem-
peratures, as well. The morphology of the 𝛾 ′ precipitate changes from
cuboidal geometry to elongated rafts during directional coarsening and
the 𝛾 channels widen along the direction of loading. Different models
have been proposed to model the evolution of channel width due
to rafting (Epishin et al., 2009; Fedelich et al., 2009; Tinga et al.,
2009a; Le Graverend et al., 2014; Fan et al., 2015; Desmorat et al.,
2017; Wu et al., 2019; Guo et al., 2021). Epishin et al. (2009) have
modeled the channel width evolution during rafting using a mod-
ified Arrhenius equation that accounts for temperature- and stress-
dependence. Tinga et al. (2009a) extended this model to a multiaxial
stress state within crystal plasticity formulation to simulate tensile
and cyclic tests. Fedelich et al. (2009) proposed a dimensionless pa-
rameter to capture the isotropic and direction coarsening of channel
width. Fan et al. (2015) further extended this model to predict the
rafting characteristics under various loading conditions like double
shear creep and rafting without external stress. Although their model is
orientation-dependent, the applicability of the model to capture chan-
nel width and creep response along different orientations (e.g. [111]
loading) was not demonstrated. Desmorat et al. (2017) proposed a
model considering the effect of isotropic and directional coarsening
on viscoplastic behavior at higher temperatures, which includes a
tensorial description of channel width evolution. It should also be
noted that several recent studies have focused on phase field modeling
of microstructure evolution during creep deformation (Gaubert et al.,
2015; Wu et al., 2017; Ali et al., 2020; Zhang et al., 2020; Le Bouar
et al., 2022). These spatially resolved simulations provide detailed
information regarding the microstructural evolution, however they are
computationally expensive.
As can be seen, significant research has been directed at consti-
tutive modeling of deformation in these alloys. However, there are
only a few frameworks proposed for unified modeling of the effects
of temperature- and strain rate-dependence, and directional harden-
ing in order to predict creep, cyclic and creep-fatigue interactions
in superalloy single crystals over a range of deformation histories
(cf. Staroselsky and Cassenti (2011), Vattré and Fedelich (2011), Rodas
and Neu (2018)). Further, microstructure evolution during creep has
also not been addressed explicitly in some of these works. The present
work aims to address these gaps in the literature by developing a
physically-based constitutive framework for unified modeling of the
above mentioned phenomena.
We propose a microstructure-sensitive crystal plasticity constitutive
model to simulate thermo-mechanical deformation in single crystal
Ni-based superalloys. Description of the proposed crystal plasticity
framework and constitutive equations for microstructure evolution dur-
ing creep are first given in Section 2. Details of the constitutive model
parameters fit to the available experimental data for tensile, cyclic
and creep response for two different superalloys, CMSX-4 and PWA-
1484, are then given in Section 3. Finally, the model is validated by
comparison of the predicted response with the available experimental
data for the creep-fatigue loading for these alloys.
2. Crystal plasticity framework
The constitutive modeling framework is based on the prior work
of Ranjan et al. (2021), where a crystal plasticity model was proposed
to model the homogenized response of the microstructure comprising of
the𝛾 matrix and𝛾 ′ precipitate. Ranjan et al. (2021) modeled the effect
of non-Schmid stresses on the orientation- and temperature-dependent
yield stress for single crystal Ni-based superalloys. In the present work,
we extend this framework by proposing constitutive models for back-
stress evolution, climb enhanced glide and microstructure evolution
during elevated temperature deformation in order to predict the creep,
cyclic and creep-fatigue interactions.
2.1. Finite deformation kinematics
This framework is based on the multiplicative decomposition of the
deformation gradient,𝑭 , into the elastic deformation gradient,𝑭𝒆, and
the inelastic deformation gradient, 𝑭𝒊 (Asaro and Rice, 1977):
𝑭 =𝑭𝒆⋅𝑭𝒊 (1)
Here,𝑭𝒆 accounts for the lattice distortion and the rigid body rotation
that carries the intermediate isoclinic configuration to the current,
deformed configuration and 𝑭𝒊 accounts for the effects of inelastic

## Page 3

Mechanics of Materials 174 (2022) 104474
3
S. Chaudhary et al.
deformation on a undeformed lattice, mapping the reference configura-
tion to an intermediate configuration in which the lattice has the same
orientation.
The second Piola–Kirchhoff stress in the intermediate configuration
is given by 𝑺 = 𝑪𝒆𝒇𝒇 ∶ 𝑬𝒆, where, 𝑪𝒆𝒇𝒇 is the fourth rank elasticity
tensor and𝑬𝒆 is the elastic Green strain tensor. The effective elasticity
tensor for the homogenized material is given by Ranjan et al. (2021):
𝑪𝑖𝑗𝑘𝑙
𝒆𝒇𝒇 =
((1 −𝑓𝛾′
)𝑪𝑖𝑗𝑘𝑙−1
𝒎 +𝑓𝛾′𝑪𝑖𝑗𝑘𝑙−1
𝒑
)−1
(2)
where, 𝑪𝑖𝑗𝑘𝑙
𝒎 and 𝑪𝑖𝑗𝑘𝑙
𝒑 represent the anisotropic fourth order elasticity
tensors of the matrix phase, 𝛾, and the precipitate phase, 𝛾 ′, respec-
tively. The second Piola–Kirchhoff stress is related to the Cauchy stress,
𝝈, in current configuration by 𝑺 =𝑑𝑒𝑡 (𝑭𝑒)𝑭𝑒−1⋅𝝈⋅𝑭𝑒−𝑇 .
The inelastic deformation gradient is given by ̇𝑭𝑖 =𝑳𝒊⋅𝑭𝒊, where
𝑳𝒊 is the inelastic velocity gradient. 𝑳𝒊 is modeled as the tensor sum
of crystallographic shearing rates and climb rates across all possible
deformation systems and is given by:
𝑳𝒊 = (1 −𝑓𝛾′
) 𝑁𝑚∑
𝛼=1
̇𝛾𝛼
𝑔𝒔𝛼
0𝑚⊗𝒎𝛼
0𝑚 +𝑓𝛾′
𝑁𝑝∑
𝛽=1
̇𝛾𝛽
𝑔𝒔𝛽
0𝑝⊗𝒎𝛽
0𝑝
+(1 −𝑓𝛾′
) 𝑁𝑚∑
𝛼=1
̇𝛾𝛼
𝑐𝒔𝛼
0𝑚⊗𝒔𝛼
0𝑚 +𝑓𝛾′
𝑁𝑝∑
𝛽=1
̇𝛾𝛽
𝑐𝒔𝛽
0𝑝⊗𝒔𝛽
0𝑝
(3)
Here, ̇𝛾𝛼
𝑔 and ̇𝛾𝛼
𝑐 are the crystallographic strain rates due to glide and
climb on deformation system𝛼, respectively, and𝑁𝑚 and𝑁𝑝 denote the
total number of deformation systems for matrix and precipitate phase,
respectively. Further, the slip system direction and plane normal in the
reference configuration are given by 𝒔𝛼
0 and𝒎𝛼
0, respectively. The sub-
scripts,𝑚 and𝑝, denote the corresponding quantities for the matrix and
the precipitate phase, respectively. The dominant deformation mech-
anism (dislocation glide or climb) generally depends on the loading
conditions and the deformation temperature. Constitutive equations for
dislocation glide and climb contributing to the total velocity gradient
have been discussed later. Further, the relative contribution of these
mechanisms has also been predicted for different loading conditions
later in the manuscript.
The model considers deformation on the octahedral {111}⟨1̄10⟩
deformation systems for the matrix phase. Further, in order to ac-
count for non-Schmid effects, the model explicitly accounts for forward
and backward slip on the octahedral {111}⟨1̄10⟩ slip systems in the
precipitate phase. In addition, the cube {100}⟨011⟩ slip systems are
also considered for the precipitate phase, which are expected to get
activated at elevated temperatures (cf. Allan (1995), Keshavarz and
Ghosh (2015), Ranjan et al. (2021)). The list of deformation systems
considered in the present work is given in Appendix B.
Further, dislocation climb perpendicular to the slip plane is modeled
based on the climb kinematics proposed by Geers et al. (2014), where
the climb projection tensor was introduced to model the additional
strain rate due to dislocation climb in a small deformation plasticity
framework for coupled glide and climb. Here, we have extended the
same to a finite deformation framework. Note that other forms of
constitutive equations for modeling combined glide and climb have also
been proposed by Lebensohn et al. (2010), Patra and McDowell (2012),
Phan et al. (2017), Wen et al. (2017, 2020).
In the following sections, we refer to the deformation systems 𝛼 in
the phase 𝑗 using the following notation: 𝛼 ∈ oct,cube and 𝑗 ∈ m,p.
Here ‘oct’ represents the octahedral slip systems, while ‘cube’ represents
the cube slip systems. Further, ‘m’ represents the matrix phase, while
‘p’ represents the precipitate phase.
2.2. Kinetics of deformation
2.2.1. Dislocation glide
Thermally-activated dislocation glide can been modeled using an
Arrhenius type activation energy-based model for crystalline materi-
als (Kocks et al., 1975). A similar flow rule is used in this framework
for modeling the crystallographic shearing rate due to glide (Ranjan
et al., 2021), with additional consideration for the slip system-level
backstress:
̇𝛾𝛼
𝑔 =
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎩
̇𝛾𝛼
0𝑗𝑒𝑥𝑝
⎡
⎢
⎢⎣
−
𝛥𝐹𝛼
𝑔𝑗
𝑘𝑇
(
1 −
(|||𝜏𝛼
𝑗 −𝜒𝛼
𝑗
|||−𝑠𝛼
𝑎𝑗
𝑠𝛼
𝑡𝑗
)𝑝𝛼
𝑗
)𝑞𝛼
𝑗 ⎤
⎥
⎥⎦
𝑠𝑔𝑛
(
𝜏𝛼
𝑗 −𝜒𝛼
𝑗
)
;|||𝜏𝛼
𝑗 −𝜒𝛼
𝑗
|||>𝑠 𝛼
𝑎𝑗,𝛼 ∈ oct,𝑗 ∈ m
̇𝛾𝛼
0𝑗𝑒𝑥𝑝
⎡
⎢
⎢
⎢⎣
−
𝛥𝐹𝛼
𝑔𝑗
𝑘𝑇
⎛
⎜
⎜⎝
1 −
((
𝜏𝛼
𝑗 −𝜒𝛼
𝑗
)
−𝑠𝛼
𝑎𝑗
𝑠𝛼
𝑡𝑗
)𝑝𝛼
𝑗⎞
⎟
⎟⎠
𝑞𝛼
𝑗 ⎤
⎥
⎥
⎥⎦
;
(
𝜏𝛼
𝑗 −𝜒𝛼
𝑗
)
>𝑠 𝛼
𝑎𝑗,𝛼 ∈ oct,𝑗 ∈ p
̇𝛾𝛼
0𝑗𝑒𝑥𝑝
⎡
⎢
⎢⎣
−
𝛥𝐹𝛼
𝑔𝑗
𝑘𝑇
(
1 −
(|||𝜏𝛼
𝑗 −𝜒𝛼
𝑗
|||−𝑠𝛼
𝑎𝑗
𝑠𝛼
𝑡𝑗
)𝑝𝛼
𝑗
)𝑞𝛼
𝑗 ⎤
⎥
⎥⎦
𝑠𝑔𝑛
(
𝜏𝛼
𝑗 −𝜒𝛼
𝑗
)
;|||𝜏𝛼
𝑗 −𝜒𝛼
𝑗
|||>𝑠 𝛼
𝑎𝑗,𝛼 ∈ cube,𝑗 ∈ p
0; otherwise
(4)
where, 𝛼 ∈ oct,𝑗 ∈ m denotes octahedral slip in the matrix phase,
𝛼 ∈ oct,𝑗 ∈ p denotes octahedral slip in the precipitate phase, and
𝛼 ∈ cube,𝑗 ∈ p denotes cube slip in the precipitate phase. Further,̇𝛾𝛼
0𝑗 is
the pre-exponential factor,𝛥𝐹𝛼
𝑔𝑗 is the activation energy for dislocation
glide in the absence of external stress,𝑘 is the Boltzmann constant,𝑇 is
the absolute temperature, 𝜏𝛼
𝑗 is the driving stress for dislocation glide,
𝜒𝛼
𝑗 is the slip system-level backstress,𝑠𝛼
𝑎𝑗 is the athermal slip resistance,
𝑠𝛼
𝑡𝑗 is the thermal slip resistance to dislocation glide, and 𝑝𝛼
𝑗 and𝑞𝛼
𝑗 are
parameters used to model the shape of the activation enthalpy function.
Based on the non-Schmid model proposed by Ranjan et al. (2021),
the driving stress for dislocation glide, 𝜏𝛼
𝑗 , is a function of the resolved
shear stress (Schmid and non-Schmid stresses depending on the type of
slip system), i.e.,
𝜏𝛼
𝑗 =
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪⎩
𝒔𝛼⋅𝝈⋅𝒎𝛼;𝛼 ∈ oct,𝑗 ∈ m
𝒔𝛼⋅𝝈⋅𝒎𝛼 +
(
𝑎1𝒔𝛼
𝑝𝑒⋅𝝈⋅𝒎𝛼
𝑝𝑒 +𝑎2𝒔𝛼
𝑠𝑒⋅𝝈⋅𝒎𝛼
𝑠𝑒
+𝑎3𝒔𝛼
𝑐𝑏⋅𝝈⋅𝒎𝛼
𝑐𝑏
)𝑒𝑥𝑝
(
−
𝜖𝑖
𝑝
𝜖𝑖𝑜
)
;𝛼 ∈ oct,𝑗 ∈ p
𝒔𝛼⋅𝝈⋅𝒎𝛼;𝛼 ∈ cube,𝑗 ∈ p
(5)
where, (𝒔𝛼,𝒎𝛼) are unit vectors along the slip and slip plane normal on
the primary slip plane, 𝛼,
(
𝒔𝛼
𝑝𝑒,𝒎𝛼
𝑝𝑒
)
, (𝒔𝛼
𝑠𝑒,𝒎𝛼
𝑠𝑒
) and (𝒔𝛼
𝑐𝑏,𝒎𝛼
𝑐𝑏
) are the
unit vectors along slip and slip plane normal associated with the pri-
mary edge, secondary edge and cube planes,𝜖𝑖
𝑝 is the effective inelastic
strain in the precipitate phase and 𝜖𝑖
𝑜 is a material constant.The choice
of the primary and secondary edge slip planes are motivated by crystal-
lographic considerations of the formation of Anti Phase Boundary (APB)
and the cross-slip planes onto which the super-dislocation core may
spread (Paidar et al., 1984). The reader is referred to a comprehensive
discussion of the underlying mechanisms by Ranjan et al. (2021).
Beyond yield, dislocation glide is expected to be driven only by resolved
shear stress on the primary slip plane. This is modeled using the
exponential decay of non-Schmid stresses subsequent to yield (Ranjan
et al., 2021). Further, also note that the non-Schmid stress components
are present only for the octahedral slip systems in the precipitate phase.
This is motivated by prior experimental and modeling studies, which
point to the absence of the same for cube slip in the precipitate phase
and octahedral slip in the matrix phase (Allan, 1995; Keshavarz and
Ghosh, 2015; Ranjan et al., 2021). Tension–compression asymmetry
observed during yield is generally an effect of non-Schmid slip (Qin
and Bassani, 1992; Patra et al., 2014). The experimental data for 𝛾 ′
(Ni3Al) (Heredia and Pope, 1991) and CMSX-4 (Allan, 1995) indicate
that while there is clear evidence of tension–compression asymmetry
for loading orientations in which the octahedral slip systems may be

## Page 4

Mechanics of Materials 174 (2022) 104474
4
S. Chaudhary et al.
Fig. 1. (a) Schematic of climb-enhanced glide, and (b) 3-D Unit Cell Model (UCM) for 𝛾/𝛾 ′ phases.
active ([001], for example), such effects are not present at higher
temperatures for the [1̄11] and [011] loading orientations, where cube
slip may get activated. Hence, we have not considered non-Schmid
behavior of the cube slip systems.
2.2.2. Dislocation climb
In the absence of sufficient driving force due to external stresses,
dislocations may not be able to overcome the barriers to glide and such
barriers may be overcome by climb. This deformation mechanism may
be expected to be dominant at elevated temperatures and low stresses.
The consideration for climb is motivated by experimental microstruc-
ture observations ( Pollock and Argon , 1994 ; Li et al. , 2022 ), which
indicate the same during high temperature deformation of single crystal
Ni-based superalloys. For example, dislocation glide in the𝛾 phase may
get impeded at the 𝛾∕𝛾 ′ interface, when stresses are not sufficient to
penetrate or cut through the 𝛾 ′ precipitates. In order to accommodate
the imposed deformation, these dislocations may climb along the 𝛾∕𝛾 ′
interface by a thermally-activated process (see schematic in Fig. 1 (a)).
Dislocation climb may also occur in the matrix and precipitate phases,
when encountered with other obstacles such as dislocation networks,
etc.
The crystallographic strain rate due to dislocation climb is modeled
using a phenomenological power law model. Such models are generally
of the form: ̇𝛾𝑐 = 𝜌𝑏𝑣 and 𝑣 ∝ 𝜎𝑛, where the symbols have their usual
meaning (Mesarovic, 2017). Accordingly, we model the corresponding
crystallographic strain rate as:
̇𝛾𝛼
𝑐 = ̇𝛾𝛼
0𝑐𝑗𝑒𝑥𝑝
(
−
𝛥𝐹𝛼
𝑐𝑗
𝑘𝑇
)
𝜌𝛼
𝑀𝑗
(|||𝜎𝛼
𝑗
|||
)𝑛𝛼
𝑗
𝑠𝑔𝑛
(
𝜎𝛼
𝑗
)
;𝛼 ∈ oct,cube,𝑗 ∈ m,p
(6)
where, ̇𝛾𝛼
0𝑐𝑗 is a material constant, 𝐹𝛼
𝑐𝑗 is the activation energy for
diffusion-mediated processes contributing to dislocation climb. 𝜌𝛼
𝑀𝑗 is
the density of mobile dislocations, 𝜎𝛼
𝑗 is the resolved normal stress
(perpendicular to the slip plane), and 𝑛𝛼
𝑗 is the climb exponent. Since
climb is generally a diffusion mediated process, we have assumed that
there is no stress threshold for thermally-activated dislocation climb.
The driving stress for dislocation climb, 𝜎𝛼
𝑗 , is given by:
𝜎𝛼
𝑗 =𝒔𝛼⋅𝝈⋅𝒔𝛼;𝛼 ∈ oct,cube,𝑗 ∈ m,p (7)
This stress is the resolved normal stress perpendicular to the slip
plane (Geers et al., 2014) and is motivated by crystallographic consid-
erations for the Peach–Koehler force for dislocation climb ( Peach and
Koehler, 1950).
2.3. Slip resistance and substructure evolution
The resistance to dislocation glide due to the long-range stress fields
is modeled using the athermal slip resistance,𝑠𝛼
𝑎, and has dominant con-
tributions from existing dislocations (Taylor hardening) and Orowan
hardening due to bowing of dislocations around the precipitates (only
in the matrix phase). Their contribution depends on the type of slip
system and phase (Ranjan et al., 2021), and is given as:
𝑠𝛼
𝑎𝑗 =
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
𝜏𝛼
𝑡ℎ +𝑘𝑜𝑟𝑜
𝐺𝑗𝑏𝑗
̄𝑤 +𝑘𝜌𝑗𝐺𝑗𝑏𝑗
√√√√
(𝑁𝑚∑
𝜉=1
𝐴𝛼𝜉𝜌𝜉
𝑗
)
;𝛼 ∈ oct,𝑗 ∈ m
𝜏𝛼
𝑡ℎ +𝑘𝜌𝑗𝐺𝑗𝑏𝑗
√√√√
(𝑁𝑚∑
𝜉=1
𝐴𝛼𝜉𝜌𝜉
𝑗
)
;𝛼 ∈ oct,cube,𝑗 ∈ p
(8)
Here, 𝜏𝛼
𝑡ℎ is the threshold resistance, 𝐺𝑗 is the shear modulus, 𝑏𝑗 is
the Burgers vector magnitude, 𝑘𝜌𝑗 is the dislocation barrier strength,
𝐴𝛼𝜉 is the matrix of slip system dislocation interaction coefficients and
𝜌𝜉 is the dislocation density in the slip system 𝜉. 𝑘𝑜𝑟𝑜 is a material
constant associated with Orowan hardening and ̄𝑤 is the effective
width of matrix channel, with consideration for rafting during creep
deformation. The constitutive equation for modeling the evolution of
̄𝑤 due to rafting is discussed later.
Dislocations overcome the short-range stress due to lattice thermal
vibrations, which is given by the thermal slip resistance, 𝑠𝛼
𝑡𝑗,
𝑠𝛼
𝑡𝑗 =𝜏𝛼
0𝑗 ;𝛼 ∈ oct,cube,𝑗 ∈ m,p (9)
Here, 𝜏𝛼
0𝑗 is a material constant. Note that this term may have con-
tributions from the intrinsic slip resistance and the solute solution
strengthening in these superalloys. As a first order approximation, this
term is assumed to be invariant with deformation.
Constitutive equations governing the evolution of mobile and immo-
bile dislocations have been adapted from Patra and McDowell ( 2012),
Ranjan et al. (2021) and are given in Eqs. ( 10) and (11) respectively.
̇ 𝜌𝛼
𝑀𝑗 =
𝑘𝛼
𝑚𝑗
𝑏𝑗𝜆𝛼
𝑗
|||̇𝛾𝛼
𝑔𝑗
||| − 2𝑅𝑐
𝑏𝑗
𝜌𝛼
𝑀𝑗 |̇𝛾𝛼|
−
𝑘𝛼
𝑡𝑗
𝑏𝑗𝜆𝛼
𝑗
|||̇𝛾𝛼
𝑔𝑗
||| − 1
𝑏𝑗𝑙𝛼
𝑔𝑗
|||̇𝛾𝛼
𝑐𝑗
||| ;𝛼 ∈ oct,cube,𝑗 ∈ m,p (10)
̇ 𝜌𝛼
𝐼𝑗 =
𝑘𝛼
𝑡𝑗
𝑏𝑗𝜆𝛼
𝑗
|||̇𝛾𝛼
𝑔𝑗
||| −𝑘𝛼
𝑑𝑗𝜌𝛼
𝐼𝑗
|||̇𝛾𝛼
𝑔𝑗
||| + 1
𝑏𝑗𝑙𝛼
𝑔𝑗
|||̇𝛾𝛼
𝑐𝑗
||| ;𝛼 ∈ oct,cube,𝑗 ∈ m,p (11)
The first term in the mobile dislocation evolution rate (Eq. ( 10))
accounts for the multiplication of mobile dislocations at pre-existing
dislocation segments (Essmann and Mughrabi 1979), where𝑘𝛼
𝑚𝑗 denotes
the dislocation multiplication constant. The annihilation of dislocation
dipoles within a capture radius, 𝑅𝑐, is modeled using the second term.

## Page 5

Mechanics of Materials 174 (2022) 104474
5
S. Chaudhary et al.
Trapping of mobile dislocation segments at other dislocations is mod-
eled using the third term, where𝑘𝛼
𝑡 is the dislocation trapping constant.
The effective free path of dislocation trapping 𝜆𝛼
𝑗 is given by Eq. (12).
The migration rate of mobile dislocations (due to climb) is modeled
using the last term, where 𝑙𝛼
𝑔𝑗 ≈ 𝜆𝛼 is the average distance swept by
glide dislocations on the slip plane (Patra and McDowell, 2012). The
effective mean free path of dislocations, 𝜆𝛼, is generally given as the
harmonic mean of the individual obstacle mean free paths (Krausz and
Krausz, 1996; Austin and McDowell, 2011) and is given by:
1
𝜆𝛼 =
⎧
⎪
⎨
⎪⎩
√𝜌𝑗 + 1
̄𝑤 ;𝛼 ∈ oct,𝑗 ∈ m
√𝜌𝑗 ;𝛼 ∈ oct,cube,𝑗 ∈ p
(12)
While the mean free path for the precipitates is primarily a function
of the dislocation density, the channel width may also play a role in
limiting the dislocation mean free path for the matrix phase. The trap-
ping of mobile dislocations increases the immobile dislocation density
as given in the first term of Eq. (11). The annihilation of dislocations by
dynamic recovery is represented by the second term in Eq. (11), where
𝑘𝛼
𝑑𝑗 is the dynamic recovery constant. Migration of mobile dislocation
density increases the immobile dislocation density as given in third
term in Eq. (11).
2.4. Backstress
The model for backstress evolution is adapted from (Shenoy et al.,
2008), and is given as a function of the dislocation density, i.e.,
𝜒𝛼
𝑗 =
(
𝑘𝛼
𝜒1𝐺𝑗𝑏𝑗
√
𝜌𝛼
𝑗𝑠𝑔𝑛
(
𝜏𝛼
𝑗 −𝜒𝛼
𝑗
)
−𝑘𝛼
𝜒2𝜒𝛼
𝑗
)|||̇𝛾𝛼
𝑗
||| ;𝛼 ∈ oct,cube,𝑗 ∈ m,p
(13)
Here, 𝑘𝛼
𝜒1 and 𝑘𝛼
𝜒2 are material constants. The first term in this model
represents the directional hardening due to the accumulation of dislo-
cations. The second term is a recovery term similar to an Armstrong–
Frederick model. Here both octahedral and cube slip systems are in-
cluded, although backstress is primarily expected to play a role in
affecting slip for the octahedral slip systems (Shenoy et al., 2008).
2.5. Microstructure evolution during creep deformation
The microstructure evolution during high temperature creep de-
formation is assumed to be governed by two primary mechanisms:
isotropic coarsening (homothetic growth of single 𝛾 ′ precipitates)
(Epishin et al., 2009; Fedelich et al., 2009; Le Graverend et al., 2014)
and directional coarsening (rafting) (Henderson et al., 1998; Matan
et al., 1999b). Isotropic coarsening does not change the internal stress
state in the structure, it is just a change of scale (Fedelich et al., 2009).
On the other hand, directional coarsening (rafting) relaxes the internal
stresses significantly (Fedelich et al., 2009). Based on prior modeling
works (Fedelich et al., 2009; Tinga et al., 2009a; Fan et al., 2015;
Guo et al., 2021), two geometric parameters, matrix channel width,𝑤𝑖,
and precipitate size, 𝑑𝑖, are required to describe the current state of 𝛾 ′
morphology along the𝑖th direction. These two parameters are schemat-
ically described in terms of the geometric model as shown in Fig. 1(b).
The relationship between these parameters is as follows (Fedelich et al.,
2009; Guo et al., 2021):
𝜁 =𝑤1 +𝑑1 =𝑤2 +𝑑2 =𝑤3 +𝑑3 (14)
where, 𝜁 is the microstructure periodicity and directions 1, 2 and 3
correspond to the [001], [010] and [001] directions of the reference
crystal.
The matrix channel width is assumed to evolve according to two
mechanisms: isotropic coarsening and rafting (Fan et al., 2015). As
a first order approximation, dissolution of the 𝛾 ′ phase (evolution of
volume fraction of 𝛾 ′ phase) is not considered as the volume fraction
of the precipitates has been found to be invariant up to ≈ 980 ◦C (Serin
et al., 2004). Accordingly, the volume fraction of the 𝛾 ′ phase, 𝑓𝛾′, is
assumed to be constant during isothermal creep deformation.
2.5.1. Isotropic coarsening
The driving force for isotropic coarsening is due to the reduction
of overall interfacial energy (Baldan, 2002). It is generally assumed
that this phenomenon is independent of the stress state and only a
function of time and temperature (Tinga et al., 2009a; Fedelich et al.,
2012). Isotropic coarsening occurs due to Ostwald ripening during the
rafting process. During isotropic coarsening, the smaller precipitates
disappear along with an increase in the size of the larger precipitates,
due to which the microstructure coarsens at a global scale and increases
the microstructure periodicity (Tinga et al., 2009a). Following prior
works (Tinga et al., 2009a; Le Graverend et al., 2014; Fan et al.,
2015), we model isotropic coarsening using the Lifschitz–Slyosov–
Walter (LSW) theory (Glicksman and Fradkov, 1995). According to
LSW theory, the microstructure periodicity,𝜁 (𝑡), increases with time,𝑡,
according to the following:
𝜁 (𝑡)3 −𝜁 3
0 =𝐾𝑡 (15)
where, 𝜁0 = 𝑤0 +𝑑0 is the initial microstructure periodicity, and 𝐾 is
a temperature-dependent material constant. 𝑤0 is the initial channel
width and 𝑑0 is the initial precipitate size. The rate of evolution of the
microstructure periodicity is given by:
̇𝜁 = 𝐾
3
(𝜁 3
0 +𝐾𝑡) −2
3 (16)
Moreover, it is assumed that the precipitate size and channel width
increase proportionally from their initial value as:
̇𝑤𝑖𝑠𝑜
̇𝜁
= 𝑤0
𝜁0
(17)
where, ̇𝑤𝑖𝑠𝑜 is the rate of evolution of channel width due to isotropic
coarsening and 𝑤0 is the initial channel width.
2.5.2. Directional coarsening (Rafting)
Rafting is the morphological change of the 𝛾 ′ precipitate from
cuboidal geometry to elongated rafts at elevated temperatures. During
rafting, the 𝛾 channels widen in the direction of applied stress for
alloys with negative lattice misfit subjected to tension (Lukáš et al.,
1996) and give way to dislocation accumulation and motion due to the
Orowan mechanism. It must be noted that rafting may occur parallel or
perpendicular to the loading axis depending on the lattice misfit and the
direction of applied stress. For negative misfit𝛿 and positive stresses𝜎,
(𝜎 ×𝛿 <0), rafts would form perpendicular to the loading axis (N-type
rafts), whereas for (𝜎 ×𝛿 >0) rafts would form parallel to the loading
axis, i.e., 𝛾 channels widen perpendicular to the direction of applied
stress (P-type rafts) (Mughrabi, 2014). However, our proposed model
is valid only for alloys with negative lattice misfit subjected to tension.
We propose to model the rafting kinetics using a modified form
of the Johnson–Mehl–Avrami–Kolmogorov (JMAK) equation (Porter
and Easterling, 2009). The JMAK equation has been extensively used
to model the kinetics of isothermal phase transformations in various
metallurgical applications (Ohring, 1998; Jiang et al., 2014; Yang et al.,
2020). The original JMAK model has been modified here to account
for temperature- and stress-dependence to model the microstructure
evolution during rafting.
If rafting is considered as an evolution of𝛾 ′ precipitate morphology
from the cuboidal structure to the rafted structure at a constant tem-
perature, then the rate of increase of channel width in the direction of
applied stress (rafting direction) is given by:
( ̇𝑤3
)
𝑟𝑎𝑓𝑡 =𝐴0
(𝑤𝑓 −𝑤3
)𝑒𝑥𝑝
(
−𝛥𝐹𝑟 − ̄ 𝜎𝛥𝑉
𝑘𝑇
)
(18)
where, 𝐴0 is the Avrami constant, 𝛥𝐹𝑟 is the associated activation
energy, ̄ 𝜎is the von Mises effective stress, and 𝛥𝑉 is the activation
volume. Note that while this constitutive model is similar in form to
those proposed by Fedelich et al. (2009), Tinga et al. (2009a), Fan
et al. (2015), our form of constitutive model allows a more direct
physical interpretation in terms of the activation energy for rafting and

## Page 6

Mechanics of Materials 174 (2022) 104474
6
S. Chaudhary et al.
its reduction due to the current stress state. Infinite 𝛾 ′ plates like rafts
will form perpendicular to the direction of loading for a fully rafted
microstructure (Fedelich et al., 2009). As a result, the channel width
evolves from 𝑤0 (initial channel width) to 𝑤𝑓 (channel width for a
fully rafted microstructure) (Fedelich et al., 2009). The instantaneous
volume fraction of the precipitate is given as (Serin et al., 2004),
𝑓𝛾′ =
(
1 − 𝑤3
𝜁
)(
1 − 𝑤2
𝜁
)(
1 − 𝑤1
𝜁
)
(19)
where, 𝑤1 and 𝑤2 are the channels width along directions transverse
to the loading direction. For loading in the [001] direction 𝑤1 = 𝑤2.
For a fully rafted microstructure, 𝑤1 =𝑤2 = 0,𝑤 3 =𝑤𝑓 . Thus,
𝑓𝛾′ = 1 −
𝑤𝑓
𝜁0
(20)
𝑤𝑓 = (1 −𝑓𝛾′
)𝜁0 (21)
Here, 𝑤𝑓 remains constant as 𝑓𝛾′ and 𝜁0 is constant. However due to
precipitate dissolution, volume fraction of 𝛾 ′ precipitates may decrease
with increase in temperature after a critical temperature. Accordingly,
the initial microstructure periodicity parameter, 𝜁0, may vary for other
alloys. The total increase of channel width in the direction of rafting at
any given time is the summation of an increase in channel width due to
isotropic coarsening (Eq. (17)) and the increase of channel width due
to rafting (Eq. (18)) (Fan et al., 2015), i.e.,
̇𝑤3 = ( ̇𝑤3
)
𝑟𝑎𝑓𝑡 + ( ̇𝑤)𝑖𝑠𝑜 (22)
From (Eq. (19)),
𝑤1 =𝑤2 =𝜁
⎛
⎜
⎜⎝
1 −
√√√√ 𝑓𝛾′
1 − 𝑤3
𝜁
⎞
⎟
⎟⎠
(23)
Note that the above description of channel width evolution holds
only for a crystal loaded along the [0 0 1] direction. However, the
orientation dependence of rafting needs to be considered for creep
loading along different orientations. In order to accomplish this, we
adopt the tensorial description of channel width proposed by Desmorat
et al. (2017), i.e.,
𝒘′ =𝑸𝑇 ⋅𝒘⋅𝑸 (24)
Here, 𝒘′ is the second rank tensor of channel width in the rotated
configuration, 𝑸 is the rotation tensor and 𝒘 is a second order tensor
of channel width with diagonal elements as 𝑤1, 𝑤2 and 𝑤3, and the
non-diagonal elements are zero. Depending on the applied rotation,
the rotated channel width tensor,𝒘′, may of course have non-diagonal
components.. We adopt the same formulation in our work, with 𝑸
directly obtained from the rotation tensor corresponding to the Euler
angles in the Bunge notation. Note that this is the same rotation tensor
that we use for the rotation of the elastic stiffness tensor as well.
Finally, the effective channel width, ̄𝑤, is calculated as the𝐿2 norm
of the channel width tensor (Desmorat et al., 2017), i.e.,
̄𝑤 = ‖𝒘′‖ (25)
As mentioned earlier, the effect of rafting on creep deformation is
incorporated in the crystal plasticity model by Orowan strengthening
in the matrix phase (Eq. (8)).
These equations comprise the full set of equations for modeling the
thermo-mechanical deformation of Ni-based superalloys. A fully im-
plicit Newton–Raphson scheme is implemented for the time integration
of the constitutive model. The constitutive model has been imple-
mented as a material model and interfaced with the open-source fi-
nite element library, MOOSE (Multiphysics Object-Oriented Simulation
Environment) (Permann et al., 2020).
Table 1
Temperature-dependent elastic constants for the 𝛾 and
𝛾 ′ phases (Keshavarz et al., 2016).
Parameter Value
𝛾 𝐶 11 = (298.0 − 0.096𝑇 ) GPa
𝐶12 = (191.0 − 0.057𝑇 ) GPa
𝐶44 = (139.0 − 0.035𝑇 ) GPa
𝛾 ′ 𝐶11 = (325.0 − 0.096𝑇 ) GPa
𝐶12 = (209.0 − 0.057𝑇 ) GPa
𝐶44 = (144.0 − 0.035𝑇 ) GPa
2.6. Model parameters
Complex physical mechanisms are involved in the deformation
of Ni-based superalloys and their representation in the constitutive
equations makes the calibration of the numerous model parameters
non-trivial.
In the present work, we have demonstrated application of the
model to predict thermo-mechanical deformation in two different single
crystal superalloys, CMSX-4 and PWA-1484. These materials are similar
in composition, with small difference in the alloy element content
between them (Rodas and Neu, 2018). First, we calibrated the model
parameters for CMSX-4 by fitting them to the available experimental
data for tension tests and cyclic tests for different temperatures, ori-
entations, and strain rate conditions. Subsequently, we estimated the
parameters pertaining to creep deformation for different temperatures,
orientations, and stress conditions. A similar procedure was followed
for estimating the model parameters for PWA-1484.
The temperature-dependent elastic constants for 𝛾 and𝛾 ′ phase are
given in Table 1.
Some of the parameters related to slip resistance and substructure
evolution (𝑘𝑜𝑟𝑜, 𝑘𝛼
𝜌𝑗, 𝐴𝛼𝛼, 𝐴𝛼𝜁 , 𝜌0
𝑀, 𝜌0
𝐼, 𝑘𝛼
𝑚𝑗, 𝑅𝑐, 𝑘𝛼
𝑡𝑗, 𝑘𝛼
𝑑𝑗 ) were adopted
directly from (Ranjan et al., 2021). Here, 𝑘𝑜𝑟𝑜 (material constant asso-
ciated with Orowan hardening) varies between 0.238 and 2.15 (Tinga
et al., 2008; Ranjan et al., 2021). Accordingly, 𝑘𝑜𝑟𝑜 = 0.25 is assumed
in our model. The initial dislocation densities (𝜌0
𝑀, 𝜌0
𝐼) are assumed to
be very low ( 1 × 10 10𝑚−2) for an undeformed 𝛾 ′ phase (Ranjan et al.,
2021). Further, the range of initial dislocation density for 𝛾 phase has
been experimentally reported of order 1011 − 10 12𝑚−2 (Jacome et al.,
2013; Pollock and Argon, 1992). Accordingly, somewhat higher initial
dislocation density (1 × 1011𝑚−2) has been assumed for 𝛾 phase (Ranjan
et al., 2021). The dislocation hardening parameters (𝑘𝛼
𝜌𝑗,𝐴𝛼𝛼,𝐴𝛼𝜁 ) are
chosen to have physically representative values (Ranjan et al., 2021).
The material constants (𝑘𝛼
𝑚𝑗, 𝑅𝑐, 𝑘𝛼
𝑡𝑗, 𝑘𝛼
𝑑𝑗 ) are calibrated by fitting the
model to experimental hardening response. Values of these constants
are in the same range as earlier studies (Patra and McDowell, 2012;
Patra et al., 2014; Ranjan et al., 2021). The magnitude of the Burgers
vector was taken from Keshavarz and Ghosh (2015). The temperature-
dependent material parameter, 𝜏𝛼
0𝑗, in Eq. (9) was obtained by fitting
to the tension test data. Here, we initially started with the values given
by Ranjan et al. (2021) and then adjusted according to the fit to the
experimental tensile test data. While the material considered in this
prior study was the same, difference in processing history might have
contributed to a different initial threshold slip resistance. A single set
of the flow parameters were chosen for deformation at all the different
temperatures and strain rates. Model parameters related to kinematic
hardening, 𝑘𝛼
𝜒1 and 𝑘𝛼
𝜒2, were obtained by fitting the model to the
available cyclic test data. A parametric study for 𝑘𝛼
𝜒1 and 𝑘𝛼
𝜒2 was
performed by maintaining the ratio 𝑘𝛼
𝜒1∕𝑘𝛼
𝜒2 = 1 .055. This is in the
range of literature values (0.47 to 2) for similar kinematic hardening
models (Shenoy et al., 2008; Agaram et al., 2021). Essentially, a ratio
close to unity for these two kinematic hardening parameters implies
lower kinematic hardening and vice-versa.
Based on the best fit, the activation energy for dislocation climb,
𝐹𝛼
𝑐𝑗, was set to 8.46 × 10 −19𝐽 for octahedral slip and 1.28 × 10 −18𝐽 for

## Page 7

Mechanics of Materials 174 (2022) 104474
7
S. Chaudhary et al.
Table 2
Temperature-invariant flow rule related model parameters for the 𝛾 and 𝛾 ′ phases.
Parameters Material 𝛼 ∈ oct, 𝛼 ∈ cube, 𝛼 ∈ oct,
𝑗 ∈ p (𝛾 ′) 𝑗 ∈ p (𝛾 ′) 𝑗 ∈ m (𝛾)
Glide flow rule: CMSX-4 1.5 × 10−2, 1 × 10−3, 1 × 10−5,
̇𝛾0𝑗
(s−1), 1.4𝐺𝑏3, 0.3, 1.45 0.5𝐺𝑏3, 0.5, 1 0.25𝐺𝑏3, 0.9, 1
𝛥𝐹𝛼
𝑔𝑗 , 𝑝𝛼
𝑗 , 𝑞𝛼
𝑗 PWA-1484 1.5 × 10−2, 1 × 10−3, 1 × 10−5,
1.4𝐺𝑏3, 0.3, 1.45 0.5𝐺𝑏3, 0.5, 1 0.25𝐺𝑏3, 0.9, 1
Climb flow rule: CMSX-4 8.46 × 10−19, 1.28 × 10−18, 8.46 × 10−19,
𝛥𝐹𝛼
𝑐𝑗 (J), 3.84 × 10−15, 10 5.72 × 10−2, 10 4.5, 5
̇𝛾𝛼
0𝑐𝑗 (MPa × s∕mm)−1, PWA-1484 6.42 × 10−19, 1.38 × 10−18, 6.42 × 10−19,
𝑛𝛼
𝑗 3.84 × 10−15, 10 93.9, 10 2.4 × 10−5, 5
Table 3
Temperature-invariant hardening and backstress related model parameters for the 𝛾 and 𝛾 ′ phases. The same parameters are
used for both CMSX-4 and PWA-1484.
Parameters 𝛼 ∈ oct, 𝛼 ∈ cube, 𝛼 ∈ oct,
𝑗 ∈ p (𝛾 ′) 𝑗 ∈ p (𝛾 ′) 𝑗 ∈ m (𝛾)
Orowan hardening: – – 0.25
𝑘𝑜𝑟𝑜
Dislocation hardening: 0.31, 1, 1 × 10−4 0.31, 1, 1 × 10−4 0.31, 1, 1 × 10−4
𝑘𝛼
𝜌𝑗, 𝐴𝛼𝛼, 𝐴𝛼𝜁
Initial dislocation 1 × 1010, 1 × 1010 1 × 1010, 1 × 1010 1 × 1011, 1 × 1011
densities: 𝜌0
𝑀
(m−2)
𝜌0
𝐼
(m−2)
Dislocation evolution: 0.07, 6b, 0.065, 0.07, 6b, 0.065, 7.096 × 10−3, 6b, 1.35 × 10−2,
𝑘𝛼
𝑚𝑗, 𝑅𝑐, 𝑘𝛼
𝑡𝑗, 𝑘𝛼
𝑑𝑗 600 1 × 106 3000
Threshold slip 71.5 31.5 1.5
resistance: 𝜏𝛼
𝑡ℎ
Burgers vector 0.249 0.249 0.249
magnitude: 𝑏 (nm)
Backstress: 9500, 9000 9500, 9000 9500, 9000
𝑘𝛼
𝜒1, 𝑘𝛼
𝜒2
cube slip. 𝑛𝛼
𝑚 = 5 was used for the creep exponent of the matrix phase
and 𝑛𝛼
𝑝 = 10 was used for the creep exponent of the precipitate phase.
This is in the range of creep exponents calculated from experimental
data for similar superalloys (Sharma et al., 2008; Huang et al., 2016).
̇𝛾0𝑐 was obtained based on best fit to the experimental data. Note that
all model parameters related to creep were assumed to be temperature-
invariant. All the temperature-invariant model parameters for inelastic
deformation are listed in Tables 2, 3, and the temperature-dependent
model parameters are listed in Table 4.
Further, the initial microstructure parameters,𝑓𝛾′,𝑑𝛾′ and𝑤0, were
adopted from Tinga et al. (2009b). Directional coarsening parameters
(𝛥𝐹𝑟 and𝛥𝑉 ) were set to 6.64 × 10−20𝐽 and 6.64 × 10−28𝑚3, respectively.
This is in the range given by Tinga et al. (2009a). The isotropic
coarsening parameter 𝐾 and directional coarsening parameter, 𝐴0,
were determined by performing a parametric study and comparing
with the experimental channel width data (not presented here). The
initial microstructure, isotropic coarsening and directional coarsening
parameters are listed in Table 5.
After obtaining a reasonable fit with the experimental data for
CMSX-4 for various loading conditions, we performed calibration of the
model to the available experimental data for PWA-1484. Most of the
model parameters for PWA-1484 were assumed to be same as CMSX-
4. This is reasonable, given that the chemical composition of both the
alloys are comparable (Rodas and Neu, 2018). Note that the hardening
and the dislocation evolution parameters are assumed to be the same
for both alloys as given in a Table 3. However, the parameters, 𝜏𝛼
0𝑗 and
̇𝛾0𝑗 had to be modified based on fit to the experimental tension test data
for PWA-1484. Further, 𝐹𝛼
𝑐𝑗 and ̇𝛾0𝑐 were also calibrated by fitting it to
the experimental creep test data for PWA-1484.
3. Results and discussion
We have used the constitutive model to predict the tensile, cyclic,
and creep deformation behavior of CMSX-4 and PWA-1484 for various
loading conditions. All simulations were performed with single element
calculations. Symmetric boundary conditions were applied on the three
adjacent faces of the cell, implying that the displacement normal to
these three faces was fixed to be zero, and the corner node common
to these three faces was fixed to prevent rigid body rotation. In the
laboratory coordinate system, the crystal was loaded along the 𝑧-
direction for all the cases (cf. Figure 5(a) in Ranjan et al. (2021) for
schematic). While displacement-controlled loading was applied for the
tensile and cyclic tests at the prescribed strain rates, stress-controlled
loading was applied for the creep tests at the prescribed stress values.
For displacement-controlled loading, a constant nominal strain rate
was maintained throughout the simulation. For creep tests performed
under stress-controlled loading, the stress was initially ramped up to
the desired stress level at a constant stress rate within the initial 10 s
of the simulation and then held constant for the remaining duration of
the simulation. A hexahedral finite element, with linear interpolation,
was used for all simulations. Although all the simulations have been
performed using a single element, the same can easily be performed
for larger number of finite elements and complex geometries. We have
verified the same by performing two additional simulations of tension
and creep using 27 elements and comparing the predicted response
with the single element predictions. These results are shown in the
Fig. C.13. As can be seen, there is no significant difference between
the predictions for the two cases.
We have gathered relevant experimental data for CMSX-4 and PWA-
1484 from different sources in the literature. These are in the tem-
perature range of 1123–1273 K, which is generally also the operating

## Page 8

Mechanics of Materials 174 (2022) 104474
8
S. Chaudhary et al.
Table 4
Temperature-dependent model parameters for the 𝛾 and 𝛾 ′ phases.
Parameter T(K) 𝛼 ∈ oct
𝑗 ∈ p(𝛾 ′) 𝛼 ∈ cube
𝑗 ∈ p(𝛾 ′) 𝛼 ∈ oct
𝑗 ∈ m (𝛾)
CMSX-4 PWA-1484 CMSX-4 PWA-1484 CMSX-4 PWA-1484
𝜏𝛼
0𝑗 (MPa) 1123–1143 674.25 674.25 411.6 411.6 265.71 275.7076
𝜏𝛼
0𝑗 (MPa) 1223–1273 554.18 554.18 286.10 186.10 228.45 153.4454
Table 5
Microstructural parameters for CMSX-4 and PWA-1484. Note that in
the absence of relevant experimental data for PWA-1484, the same
microstructural parameters have been assumed, as for CMSX-4.
Parameters Value
Volume fraction: 0.28, 0.72
𝑓𝛾, 𝑓𝛾 ′
Precipitate size: 1, 0.5 × 10−3
𝑑𝛾 (mm), 𝑑𝛾 ′ (mm)
Initial channel width: 0.06 × 10−3
𝑤0 (mm)
Directional coarsening: 1 × 10−9, 6.64 × 10−20,
𝐴0, 𝛥𝐹𝑟 (J), 𝛥𝑉 (m3) 6.64 × 10−28
Isotropic coarsening: 3 × 10−16
𝐾(mm3∕s)
Table 6
List of the experimental data used for model prediction and validation.
Alloy Test Experimental data T(K)
CMSX-4 Tension tests Vattré and Fedelich (2011) 1123, 1223
CMSX-4 Cyclic tests Vattré and Fedelich (2011) 1123, 1223
CMSX-4 Creep tests Vattré and Fedelich (2011) 1123
CMSX-4 Creep tests MacLachlan et al. (2001) 1223
CMSX-4 Creep tests Miura et al. (2003) 1273
CMSX-4 Relaxation tests Vattré and Fedelich (2011) 1123, 1223
PWA-1484 Tension tests Staroselsky and Cassenti (2010) 1255
PWA-1484 Cyclic tests Staroselsky and Cassenti (2011) 1143
PWA-1484 Creep tests Staroselsky and Cassenti (2011) 1143, 1255
PWA-1484 Creep tests Staroselsky and Cassenti (2010) 1200
PWA-1484 Relaxation tests Staroselsky and Cassenti (2011) 1255
temperature of these alloys in aerospace applications (Allan, 1995; Ali
et al., 2020). The different sets of experimental conditions are listed in
Table 6 along with the test temperatures. The experimental data sets
for tension tests, cyclic tests and creep tests were used for calibration,
while the relaxation data sets were used for model validation. While
it is possible that the different sources may have used materials with
different processing histories for their experiments, this is unavoidable
since there is no single data set, which contains all the different
conditions used for calibration and prediction in our work.
3.1. Tensile loading
The constitutive model was fit to the experimental tension test data
at different temperatures and strain rates. Fig. 2 compares the true
stress–strain curves for CMSX-4 at different strain rates and 1123 K for
(a) [001] and (b) [̄111] loading orientation and 1223 K for (c) [001]
and (d) [̄111] loading orientation, respectively. Fig. 3 compares the
true stress–strain curves for PWA-1484 at 1255 K for (a) [001] and
(b) [̄111] loading orientation. A reasonable fit was obtained for loading
at the different strain rates, temperatures and crystal orientations for
both the materials. The model is able to capture both the temperature
and strain rate sensitivity effects for CMSX-4. This is primarily due
to the Kocks-type thermally activated flow rule (cf. Eq. (4)), which
can account for such effects via the activation enthalpy, shape pa-
rameters and the pre-exponential factor. In addition, the temperature
dependent slip resistance (cf. Eq. (9) and Table 4) is also used to
capture the experimental observed temperature dependence of the yield
stress. Limited experimental data is available for PWA-1484 and hence
such predictions are not possible. Deviations from exact single crystal
orientations in the experiments (cf. Vattré and Fedelich (2011)) could
also be a source of discrepancy between the model predictions and
experimental data. Further, our model does not predict the initial
softening subsequent to yield as experimentally observed for CMSX-4.
This is especially evident for both the [001] and [1̄11] loading at higher
strain rates. Microstructure degradation effects could be contributing to
this phenomenon. As discussed in Section 3.7, discrepancies between
the experiments and simulations can be addressed by adding the effect
of coherency stresses (lattice misfit), precipitate dissolution and the
effect of APB energy on precipitate shearing. (Ranjan et al., 2021)
have shown that such effects can be captured by accounting for the
decay of non-Schmid stresses subsequent to the initiation of plastic
deformation (cf. Eq. (5)). However, we have neglected such effects as a
first order approximation in the present work, where the main focus is
on predicting the cyclic and creep response. The ability of the model to
predict the orientation dependent yield stress of CMSX-4 over a wide
range of temperatures (from room temperature to 1123 K) has also been
demonstrated in Ranjan et al. (2021).
Difference in the flow stress for the two different orientations under
identical loading conditions may be attributed to the elastic anisotropy
and the activation of different slip systems. Plastic deformation in
the [001] orientation is governed by the octahedral ⟨111⟩{110} slip
systems, while for the [̄111] orientation, it is dominated by the cube
⟨100⟩{110} slip systems. The tensile response of CMSX-4 for the [001]
loading orientation exhibits three stages of deformation. The elastic
regime (stage 1) is followed by dislocation glide in 𝛾 channel (stage 2)
and finally𝛾 ′ precipitate shearing (stage 3), which is nearly a horizontal
stress-plateau (Vattré et al., 2010; Gupta and Bronkhorst, 2021). For
loading along the [̄111] orientation, the elastic regime (stage 1) is
followed by a low hardening phase (stage 3), where stress drops from
the upper yield point and stage 2 is missing for loading along the [111]
orientation (Vattré et al., 2010). In our simulations, the stress drop is
missing for both orientations, although it has been shown earlier that
such effects can be captured by the constitutive model (Ranjan et al.,
2021). Note that the constitutive model is still capturing the effects of
precipitate evolution on the Orowan stress, although its effect on the
macroscopic stress is not significant. This is described in Appendix A.
Finally, it is observed that there is a significant drop in the flow stress
(150–200 MPa) from 1123 K to 1223 K for a given orientation and
strain rate. This could be correlated with the non-Schmid deformation
mechanisms, which are operative up to about 1123 K and contribute
to the strength plateau (cf. Allan (1995), Keshavarz and Ghosh (2015),
Ranjan et al. (2021)). Presumably, the strength of the alloy drops
significantly, as the contribution of non-Schmid stresses (due to APB
formation) is reduced beyond this temperature.
3.2. Cyclic loading
The constitutive model was fit to the experimental data for cyclic
tests for CMSX-4 and PWA-1484 with different strain amplitudes and at
different temperatures. Fig. 4 shows a comparison of model predictions
of the cyclic stress–strain curves with the corresponding experimental
data for CMSX-4 loaded along different orientations ([001], [011],
[̄111]) at different strain rates and temperatures. Fig. 5 compares the
simulated cyclic stress–strain curves with the experimental data for
PWA-1484 loaded along different orientations ([001], [̄111], [̄123]) at

## Page 9

Mechanics of Materials 174 (2022) 104474
9
S. Chaudhary et al.
Fig. 2. Simulated true stress–strain curves for different strain rates at 1123 K for (a) [001] and (b) [̄111] loading orientations, and at 1223 K for (c) [001] and (d) [̄111] loading
orientations as compared with the experimental data for CMSX-4 ( Vattré and Fedelich , 2011). The simulated data is plotted with solid lines, while the experimental data is plotted
with symbols.
Fig. 3. Simulated true stress–strain curves at 1255 K for (a) [001] and (b) [̄111] orientations as compared with the experimental data for PWA-1484 ( Staroselsky and Cassenti ,
2010). The simulated data is plotted with solid lines, while the experimental data is plotted with symbols.
1143 K. All the simulated stress–strain curves are plotted for twenty cy-
cles for CMSX-4. For PWA-1484, the number of cycles for the different
tests are shown in the corresponding figures.
Model predictions for CMSX-4 agree qualitatively with the exper-
imental data. There is some discrepancy in the predicted flow stress
for the [̄111] cyclic loading cases at 1123 K (see Fig. 4 (c) and (d)),
which may be due to the model’s inability to accurately capture the
strain rate sensitivity of the material for the [̄111] orientation. Given
that the model is able to predict the tensile response for this orientation
with reasonable accuracy, this discrepancy could be indicative of the
temperature- and strain rate-dependence of the backstress evolution,
which has not been considered in the present work. Cube slip is ex-
pected to dominate for these loading conditions. For the other loading
conditions, the model predicts a wider hysteresis loop as compared
to the experiments, although the peak stresses are predicted with
reasonable accuracy. In all the cases, the simulated stress–strain curves
were found to converge after two or three cycles towards a stabilized
hysteresis loop. A similar observation was noted in the experimental
study of Vattré and Fedelich (2011) as well.
The model predicts the cyclic response for PWA-1484 with higher
accuracy (see Fig. 5) as compared to CMSX-4. While details of the ex-
perimental conditions for PWA-1484 are not entirely known, deviation
from ideal orientations of the test specimens for CMSX-4 (cf. Vattré and
Fedelich (2011)) could have contributed to some of this discrepancy in
the predicted mechanical response. Further, repeatability of the exper-
imental tests over multiple specimens has not been discussed in the
experimental references in Table 5 as well. This could be an additional
source of discrepancy.. The amount of plastic deformation (width of the
loop) is remarkably similar between the experiments and simulations.
The hysteresis loop is wider for the [̄111] orientation, as compared
to similar loading conditions along the [001] orientation. This could
be due to higher elastic stiffness along the [̄111] orientation, which
leads to a more pronounced yielding ( Staroselsky and Cassenti, 2010).
The hysteresis loop for loading along [̄123] orientation is significantly
wide due to the relatively lower yield stress, as compared to the [001]
orientation. The low cycle fatigue life of specimens along the [̄123]
orientation is expected to be shorter than the specimens oriented along
the [001] direction. Note that while the [001] and [̄111] orientations
were used for model calibration, the [̄123] loading orientation was
used for validation of the cyclic response for PWA-1484 in Fig. 5 (c).
Given that the model is able to predict the cyclic response for this
loading orientation, it points to the ability of the model to predict the
orientation-dependent activation of different deformation modes.
3.3. Creep loading
The constitutive model was fit to the experimental creep data for
CMSX-4 and PWA-1484. Fig. 6 compares model predictions of the creep

## Page 10

Mechanics of Materials 174 (2022) 104474
10
S. Chaudhary et al.
Fig. 4. Simulated true stress–strain curves for different strain rates at 1123 K for (a) [001], (b) [011] and (c), (d) [̄111] orientations, and at 1223 K for (e) [001] and (f), (g)
[̄111] orientations as compared with the experimental data for CMSX-4 ( Vattré and Fedelich , 2011). The simulated data is plotted with solid lines, while the experimental data is
plotted with symbols.
strain with the experimental data for CMSX-4 loaded along different
orientations ([001] and [̄111]) over a range of stresses and tempera-
tures. Fig. 7 compares the same for PWA-1484 loaded along different
orientations for different temperatures and stresses.
It is observed that the model predictions are in general qualitative
agreement with the experiments. As discussed earlier, steady state
secondary creep is generally absent/minimal in both the experiments
and simulations (cf. 1). Further, the tertiary creep behavior, which may
lead to eventual failure via rupture, is captured by our model. There is
some discrepancy in predicted creep strains for the lower stresses (180
MPa and 250 MPa) at 1223 K for CMSX-4 (see Figs 6 (c) and 6(d)). It
should also be pointed out that variability in the creep response may
be expected from experiments even for identical loading conditions.
Hence, our focus has been on predicting the overall creep trends with
temperature and applied stress. As can be seen, the tertiary creep strains
are generally comparable with experiments for higher stress values.
However, we note that other mechanisms, such as damage, may also be
prevalent during the later stages of creep. Presumably, our model is not
able to capture the tertiary creep rates accurately (as compared to the
experiments) due to the neglect of such mechanisms in the constitutive
model. As can be seen, the model under-predicts the tertiary creep rates
for CMSX-4 for [0 0 1] loading and over-predicts the tertiary creep rates
for [̄1 1 1] loading (for some cases at 1223 K) at higher temperatures.
Similar trends are also observed for [0 0 1] loading for PWA-1484.
While the reasons for this are not entirely clear, this could possibly be
attributed to the above mentioned neglect of damage in our constitutive
model.
It is natural to expect that mechanisms governing the evolution
of creep strains over the range of stresses, temperatures and loading
orientations may change from one test case to another. These are
discussed in the context of the various deformation mode activities in
Section 3.5.

## Page 11

Mechanics of Materials 174 (2022) 104474
11
S. Chaudhary et al.
Fig. 5. Simulated true stress–strain curves at 1143 K for (a) [001], (b) [̄111] and (c) [123] orientations as compared with the experimental data for PWA-1484 ( Staroselsky and
Cassenti, 2011). The simulated data is plotted with solid lines, while the experimental data is plotted with symbols.
Fig. 6. Simulated creep strain versus time for different stresses at 1123 K for (a) [001] and (b) [̄111] orientations, and at 1223 K for (c) [001] and (d) [̄111] orientations, and
at 1273 K for (e) [001] orientation as compared with the experimental data for CMSX-4 ( Vattré and Fedelich , 2011 ). The simulated data is plotted with solid lines, while the
experimental data is plotted with symbols.

## Page 12

Mechanics of Materials 174 (2022) 104474
12
S. Chaudhary et al.
Fig. 7. Simulated creep strain versus time for different stresses at (a) 1143 K, (b) 1200 K, and (d) for [001] orientation, and (c) 1200 K and (e) 1255 K for [̄111] orientation as
compared with the experimental data for PWA-1484 ( Staroselsky and Cassenti , 2011). The simulated data is plotted with solid lines, while the experimental data is plotted with
symbols.
3.4. Channel width evolution
The channel width evolution of CMSX-4 is studied using the consti-
tutive model described in Section 2.5 along with values of the model
parameters in Table 5. Fig. 8 compares the simulated channel width
along the direction of loading with the available experimental data at
1223 K ( Fedelich et al. , 2009) for different applied stresses and two
different loading orientations. It can be seen from Fig. 8 (a) that the
channel width increases both with applied stress and loading time for
loading along the [001] direction, as also indicated by the limited ex-
perimental data. This has contributions from both isotropic coarsening
and rafting. However, the channel width does not evolve with stress for
creep loading along the [̄111] orientation. This is due to the inherent
geometric orientation of the channel for the [̄111] single crystal, which
does not allow rafting (Liu et al., 2008). In our framework, this effect is
captured due to the rotation of the channel width tensor as a function
of the loading orientation (cf. Eq. ( 24)). For the [̄111] orientation,
the primary contribution to the evolution of channel width is due to
isotropic coarsening.
The channel width evolution has several effects on the material’s re-
sponse: (a) the Orowan stress decreases as the channel width increases
(Eq. (8)), which increases the matrix slip rate ( Fedelich et al. , 2009),
and (b) coherency between the precipitate and matrix phase reduces
during rafting, which makes precipitate shearing easier ( Tinga et al. ,
2009a). While coherency stresses have not been explicitly accounted
for in our model, the effect on Orowan stress has been modeled
using appropriate constitutive equations in the present work. When
deformation is dominated by precipitate shearing and/or matrix slip
(tensile tests, creep tests at higher stresses), rafting causes increase in
the crystallographic slip rate. On the other hand, rafting increases the
load bearing capacity of the material when dislocation climb dominates
deformation (creep at lower stresses) ( Tinga et al., 2009a).
Before moving further, it should be noted that experimental data
for channel width is not available for PWA-1484. Hence, relevant model
parameters calibrated to CMSX-4 are used for PWA-1484 predictions as
well, with the inherent assumption of similar channel width evolution.
There are some differences in the underlying deformation mecha-
nisms for creep under [0 0 1] and [ ̄1 1 1] loading. Based on model
predictions for CMSX-4, the contribution of dislocation glide to defor-
mation is higher as compared to dislocation climb at higher stresses for
the [̄1 1 1] orientation (Fig. 9), which may have led to higher tertiary
creep rates for [ ̄1 1 1] loading as compared to [0 0 1] loading. For
the [0 0 1] orientation, the Orowan stress decreases with increase in
rafting (cf. Fig. A.12). This may have led to stress relaxation within the
𝛾 channels and an accompanying decrease in the glide rate. This may
have caused a decrease in the tertiary creep rate during the later stages
of creep deformation for the [0 0 1] orientation as compared to the [ ̄1
1 1] orientation.
3.5. Relative slip activity
Fig. 9 shows the contribution of different deformation modes as a
function of von Mises effective strain for loading in tension, cyclic and
creep conditions for the [001] and the [̄111] orientations at 1123 K.
Note that the cyclic tests were conducted for a strain amplitude of 0.01.

## Page 13

Mechanics of Materials 174 (2022) 104474
13
S. Chaudhary et al.
Fig. 8. Evolution of channel width during creep loading at 1223 K for (a) [001] and (b) [̄111] orientations. The simulated data is plotted with solid lines, while the experimental
data (Fedelich et al. , 2009) is plotted with symbols.
As can been seen, octahedral slip in the matrix phase is dominant
for loading along the [001] orientation, while the contribution from
cube slip in the precipitate phase is higher for loading along the [̄111]
orientation. Also, deformation occurs primarily by dislocation glide
for tensile and cyclic loading, whereas for creep loading, deformation
occurs primarily by dislocation climb. Note that some climb activity
is observed even during tensile and cyclic loading during the initial
transients, until the threshold to initiate deformation by slip is reached.
Further, glide activity is also observed during the initial phases of
creep deformation, until the creep stresses have been relaxed by dis-
location climb. While there is some experimental transmission electron
microscopy evidence showing the presence of both octahedral and cube
dislocations in the precipitate phase at elevated temperatures ( Wang
et al. , 2014 ; Ding et al. , 2021 ), there is no clear indication in the
literature about whether these dislocations were formed due to glide or
climb. Moreover, the relative fraction of different types of dislocations
is also difficult to estimate using such techniques. Based on the fit to
the experimental macroscopic response, our model predictions indicate
that octahedral glide in the precipitate phase, although present to a
small extent for tensile and cyclic loading, is rather limited.
Rafting also plays an important role during creep deformation.
Dislocation slip occurs in the𝛾 matrix at the onset of creep deformation,
which increase the dislocation density. The material hardens as a result
and the creep strain rate decreases as further dislocation multiplication
and motion are hindered by existing dislocations in the narrow 𝛾
channels. This corresponds to the steady state, secondary creep. These
𝛾 channels widen due to isotropic coarsening and rafting at elevated
temperatures. Consequently, the glide of dislocations in the 𝛾 channels
becomes relatively easier. This also causes an increase in the creep
strain rate and corresponds to the initiation of tertiary creep. Thus, the
microstructure degradation caused by isotropic coarsening and rafting
is one of the primary contributors to the acceleration of creep rate
during the later stages of deformation ( Fan et al., 2015).
3.6. Creep-fatigue interactions
In the previous sections, the constitutive model has been calibrated
to predict the tensile, cyclic and creep response of CMSX-4 and PWA-
1484 for a wide range of loading conditions. Here, we use the model to
predict the creep-fatigue interactions for both alloys as validation test
cases.
Fig. 10 compares model predictions of tensile or cyclic relaxation in
terms of the stress–strain as compared with the corresponding experi-
mental data for CMSX-4 for different orientations ([001] and[̄111]) and
different strain rates at 1123 K and 1223 K (Vattré and Fedelich, 2011).
Strain-controlled relaxation tests were performed with strain holds
of different time intervals during cyclic/tensile loading. The loading
histories are given in the form of strain versus time plots in Figs. 10
and 11. The model is able to qualitatively predict the experimentally
observed relaxation behavior for CMSX-4. There is some variation in
the predicted flow stress, as compared with the experimental data at
1123 K for [̄111] orientation. As mentioned earlier, this might be due
to the model’s inability to capture the the temperature- and strain
rate- sensitivity of the backstress evolution for the [̄111] orientation at
very low strain rates. Similar to the cyclic loading data in Fig. 4 , the
effects appear to be more severe for [̄111] loading as compared to the
[001] loading. Future work could consider the said temperature- and
strain rate sensitivity to improve the model’s predictive capabilities.
Further, as can be seen in the experimental data in Fig. 10 (c), there
is some cyclic softening observed; the constitutive model for which has
not been proposed here. As was seen earlier, the peak stresses during
cyclic loading are not predicted accurately by the model, although
qualitative concurrence is still present. Mechanisms responsible for
cyclic softening include precipitate shearing, precipitate dissolution,
precipitate disordering, and loss of coherency between the precipitates
and the matrix ( Antolovich et al. , 1981 ; Sundararaman et al. , 1989 ;
Humphreys and Hatherly , 2012 ; Phillips et al. , 2013 ; Zhang et al. ,
2019; León-Cázares et al., 2020). Recent works on constitutive model-
ing of Ni-based superalloys have considered such effects (León-Cázares
et al., 2020; Agaram et al., 2021) and similar models could be included
in future work.
Fig. 11 compares the simulated cyclic relaxation stress–strain curve
with the corresponding experimental data for PWA-1484 for [001]
orientation at 1255 K for strain amplitudes 0.005 and 0.008 ( Starosel-
sky and Cassenti , 2010). A strain hold of 5 min was applied both in
tension and compression at the maximum strain for each cycle. Further,
note that the number of cycles are different in both cases. Model
predictions agree qualitatively with the experimental results for PWA-
1484. However, the peak stresses are not predicted accurately here as
well. This could be due to the fact that the strain amplitudes are very
small in both these cases and the initiation of plastic deformation is not
predicted accurately. It can be seen that the model predicts the width of
the hysteresis loop better at higher strain amplitude, which is expected
to have higher plastic strain.
3.7. Discussion
While the constitutive model presented in this work is comprehen-
sive enough to capture the temperature- and strain rate-sensitivity, di-
rectional hardening and microstructure evolution during creep loading,
there are certain underlying assumptions involved in these equations:
1. It has been assumed that the channel width due to rafting
increases along the loading direction, which is only valid for neg-
ative lattice misfit alloys subjected to tension. With appropriate
modifications, positive misfit can also be accounted for in the
present framework (cf. Desmorat et al. (2017), Wu et al. (2019)).
2. The volume fraction of 𝛾 ′ precipitates has been assumed to be
constant in the present work. However, precipitate dissolution is
expected to occur beyond a critical temperature (Desmorat et al.,
2017). Based on fit to appropriate experimental data, the change
in volume fraction with temperature can be empirically or phe-
nomenologically modeled ( Fan et al. , 2015 ; Desmorat et al. ,

## Page 14

Mechanics of Materials 174 (2022) 104474
14
S. Chaudhary et al.
Fig. 9. Relative activity of different deformation modes as a function of applied strain for tension, cyclic and creep loading along [001] and [̄111] orientations at 1123 K.
2017). Insights from phase field and kinetics models could also
be used to inform such constitutive equations ( Masoumi et al. ,
2016). This can also be accounted for with minor modifications.
3. Lattice misfit and associated coherency stresses have not been
explicitly considered in our model. Coherency stresses affect the
fatigue, creep and directional coarsening ( Tinga et al. , 2009a).
Further, these may also influence the type of rafting observed in
single crystal superalloys (Guo et al., 2021). In our model, these
stresses are implicitly assumed to be present in the threshold
stress term, 𝑠𝛼
𝑎𝑗, and their description can be refined further in
future work.
4. Finally, the effect of APB energy on precipitate shearing ( Ghor-
banpour et al. , 2017 ; Li et al. , 2019 ; Gupta and Bronkhorst ,
2021) and its temperature dependence has not been explicitly
considered in our work. This may be expected to vary between
alloys with different compositions. While this term is inherently
assumed to be present in the temperature-dependent threshold
resistance, 𝜏𝛼
0𝑗 (cf. Ranjan et al. (2021)), its description can also
be refined in future work.
The overall framework is modular in nature to be able to incor-
porate such individual mechanisms in future work. Moreover, despite
these assumptions, the model is able to predict qualitative trends of
mechanical response across a wide range of loading histories for the
two alloys, CMSX-4 and PWA-1484.
4. Conclusions
We have proposed a crystal plasticity constitutive framework for
modeling the thermo-mechanical deformation of single crystal Ni-based
superalloys. In this dislocation density-based framework, slip is mod-
eled using an Arrhenius type activation energy-based equation. A model

## Page 15

Mechanics of Materials 174 (2022) 104474
15
S. Chaudhary et al.
Fig. 10. Strain versus time for strain controlled relaxation test for (a) [001] orientation at 1123 K, and (d) [̄111] orientation at 1123 K, and (g-j) [001] orientation at 1223 K.
The corresponding simulated creep-fatigue behavior as a function of (b) strain and (c) time for [001] orientation at 1123 K, and (e) strain and (f) time for [̄111] orientation at
1123 K, and (h-k) strain and (i-l) time for [001] orientation at 1223 K as compared with the experimental data for CMSX-4 ( Vattré and Fedelich , 2011 ). The simulated data is
plotted with solid lines, while the experimental data is plotted with symbols.
Fig. 11. (a), (c) Strain versus time for strain controlled relaxation test for [001] orientation at 1255 K and two different strain amplitudes. The corresponding simulated creep-fatigue
behavior as compared with the experimental data for PWA-1484 ( Staroselsky and Cassenti , 2010) are shown in (b) and (d). The simulated data is plotted with solid lines, while
the experimental data is plotted with symbols.

## Page 16

Mechanics of Materials 174 (2022) 104474
16
S. Chaudhary et al.
Fig. A.12. Evolution of Orowan stress with time for (a) tensile loading at 10−4 s−1 strain rate and (b) creep loading at 250 MPa stress for CMSX-4.
Table B.7
Octahedral and cube slip systems in 𝛾 ′ phase (Qin and Bassani 1992 ).
𝛼 Type ( 𝑚𝛼)[𝑠𝛼]
(
𝑚𝛼
𝑝𝑒
) [
𝑠𝛼
𝑝𝑒
] (𝑚𝛼
𝑠𝑒
) [𝑠𝛼
𝑠𝑒
] ( 𝑚𝛼
𝑐𝑏
) [𝑠𝛼
𝑐𝑏
]
1 Octahedral (111)[01 ̄1] (111)[ ̄211] (1 ̄1̄1)[̄2̄1̄1] (100)[01 ̄1]
2 Octahedral (111)[ ̄101] (111)[1 ̄21] ( ̄11̄1)[̄1̄2̄1] (010)[ ̄101]
3 Octahedral (111)[1 ̄10] (111)[11 ̄2] ( ̄1̄11)[̄1̄1̄2] (001)[1 ̄10]
4 Octahedral (1 ̄1̄1)[0̄11] (1 ̄1̄1)[̄2̄1̄1] (111)[ ̄211] (100)[0 ̄11]
5 Octahedral (1 ̄1̄1)[̄10̄1] (1 ̄1̄1)[12̄1] ( ̄11̄1)[̄112] (0 ̄10)[̄10̄1]
6 Octahedral (1 ̄1̄1)[110] (1 ̄1̄1)[1̄12] ( ̄11̄1)[̄112] (00 ̄1)[110]
7 Octahedral ( ̄11̄1)[011] ( ̄11̄1)[21̄1] ( ̄1̄11)[2̄11] ( ̄100)[011]
8 Octahedral ( ̄11̄1)[10̄1] ( ̄11̄1)[̄1̄2̄1] (111)[1 ̄21] (010)[10 ̄1]
9 Octahedral ( ̄11̄1)[̄1̄10] ( ̄11̄1)[̄112] (1 ̄1̄1)[1̄12] (00 ̄1)[̄1̄10]
10 Octahedral ( ̄1̄11)[0̄1̄1] ( ̄1̄11)[2̄11] ( ̄11̄1)[21̄1] ( ̄100)[0̄1̄1]
11 Octahedral ( ̄1̄11)[101] ( ̄1̄11)[̄121] (1 ̄1̄1)[1̄12] (0 ̄10)[101]
12 Octahedral ( ̄1̄11)[̄110] ( ̄1̄11)[̄1̄1̄2] (111)[11 ̄2] (001)[ ̄110]
13 Octahedral (111)[0 ̄11] (111)[ ̄211] (1 ̄1̄1)[̄2̄1̄1] (100)[0 ̄11]
14 Octahedral (111)[10 ̄1] (111)[1 ̄21] ( ̄11̄1)[̄1̄2̄1] (010)[10 ̄1]
15 Octahedral (111)[ ̄110] (111)[11 ̄2] ( ̄1̄11)[̄1̄1̄2] (001)[ ̄110]
16 Octahedral (1 ̄1̄1)[01̄1] (1 ̄1̄1)[̄2̄1̄1] (111)[ ̄211] (100)[01 ̄1]
17 Octahedral (1 ̄1̄1)[101] (1 ̄1̄1)[12̄1] ( ̄11̄1)[̄112] (0 ̄10)[101]
18 Octahedral (1 ̄1̄1)[̄1̄10] (1 ̄1̄1)[1̄12] ( ̄11̄1)[̄112] (00 ̄1)[̄1̄10]
19 Octahedral ( ̄11̄1)[0̄1̄1] ( ̄11̄1)[21̄1] ( ̄1̄11)[2̄11] ( ̄100)[0̄1̄1]
20 Octahedral ( ̄11̄1)[̄101] ( ̄11̄1)[̄1̄2̄1] (111)[1 ̄21] (010)[ ̄101]
21 Octahedral ( ̄11̄1)[110] ( ̄11̄1)[̄112] (1 ̄1̄1)[1̄12] (00 ̄1)[110]
22 Octahedral ( ̄1̄11)[011] ( ̄1̄11)[2̄11] ( ̄11̄1)[21̄1] ( ̄100)[011]
23 Octahedral ( ̄1̄11)[̄10̄1] ( ̄1̄11)[̄121] (1 ̄1̄1)[1̄12] (0 ̄10)[̄10̄1]
24 Octahedral ( ̄1̄11)[1̄10] ( ̄1̄11)[̄1̄1̄2] (111)[11 ̄2] (001)[1 ̄10]
25 Cube (100)[ 011] – – –
26 Cube (100)[01 ̄1] – – –
27 Cube (010)[ 101] – – –
28 Cube (010)[10 ̄1] – – –
29 Cube (001)[ 110] – – –
30 Cube (001)[1 ̄10] – – –
for the evolution of the slip system-level back stress is used predict the
cyclic response. Climb of dislocations is modeled with consideration
for the climb kinematics perpendicular to the slip plane and a Peach–
Koehler-type crystallographic normal stress that causes climb. Further,
dislocation climb is modeled using a power law type equation with tem-
perature dependence. Material-specific hardening mechanisms such as
Orowan looping around precipitates, grain/precipitate size hardening,
dislocation density based hardening are considered in this framework.
The substructure evolution is considered in terms of the mobile and
immobile dislocation densities. Further, constitutive equations for raft-
ing and isotropic coarsening of the 𝛾 ′ precipitates are developed to
account for the microstructure evolution commonly observed in these
materials during creep deformation. The constitutive model has been
implemented and coupled with the open source finite element library,
MOOSE, using a fully implicit time integration scheme.
Application of the constitutive model has been demonstrated to pre-
dict the mechanical response of two different single crystal superalloys,
CMSX-4 and PWA-1484, and compared with available experimental
data. Specifically, the orientation-, temperature- and rate-dependent
response has been predicted under tensile loading. The cyclic and
creep response has also been predicted for a range of strain ampli-
tudes, orientations and stresses, respectively. Insights obtained from the
Table B.8
Octahedral slip systems in 𝛾 phase.
𝛼 Type ( 𝑚𝛼)[𝑠𝛼]
1 Octahedral (111)[01 ̄1]
2 Octahedral (111)[ ̄101]
3 Octahedral (111)[1 ̄10]
4 Octahedral (1 ̄1̄1)[0̄11]
5 Octahedral (1 ̄1̄1)[̄10̄1]
6 Octahedral (1 ̄1̄1)[110]
7 Octahedral ( ̄11̄1)[011]
8 Octahedral ( ̄11̄1)[10̄1]
9 Octahedral ( ̄11̄1)[̄1̄10]
10 Octahedral ( ̄1̄11)[0̄1̄1]
11 Octahedral ( ̄1̄11)[101]
12 Octahedral ( ̄1̄11)[̄110]
model have been used to understand the competitive role of various
deformation mechanisms during different loading conditions. Finally,
the model has been used to predict the creep-fatigue interactions in
both alloys and compared with available experimental data.
This physically-based, microstructure sensitive constitutive model
accounts for a wide range of deformation mechanisms that may be
occurring under different loading conditions during the operation cy-
cle of these alloys in aerospace components. The model’s ability to
predict the mechanical response due to such competing effects at
relatively low computational costs (as compared to more computa-
tionally intensive tools, such as coupled phase field-crystal plasticity
models) is one of the main advantages of this framework. Further,
while mechanisms such as dislocation density-based backstress evo-
lution, dislocation climb kinematics, orientation-dependent channel
width evolution, and temperature- and stress-dependent evolution of
rafting kinetics, have been individually proposed in the literature, their
integration into a unified crystal plasticity constitutive framework for
single crystal superalloys enhances the model’s predictive capabilities
significantly over a wide range of possible deformation histories. This
is the primary contribution of the proposed framework.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Data availability
Data will be made available on request.
Acknowledgments
The authors gratefully acknowledge funding received from the Aero-
nautics Research and Development Board (AR & DB) for this project via
GTMAP project no. 1850. Suketa Chaudhary is also grateful for funding
received from the Prime Minister’s Research Fellowship to support her
doctoral studies.

## Page 17

Mechanics of Materials 174 (2022) 104474
17
S. Chaudhary et al.
Fig. C.13. Simulated response with different number of elements for (a) tensile loading at 10−4 s−1 strain rate and (b) creep loading at 450 MPa stress for CMSX-4. No noticeable
difference is observed on increasing the number of elements.
Appendix A. Evolution of Orowan stress during tensile and creep
loading
Fig. A.12 shows the evolution of Orowan stress with respect to time
for tensile and creep loading, respectively. The Orowan stress decreases
with increase in time for both cases, although the drop in stress for
tensile loading is abrupt at the beginning of inelastic deformation, when
dislocation glide has not yet set in. This is primarily due to the increase
in channel width due to rafting, which can lead to stress softening
for low strain rate tensile loading ( Desmorat et al. , 2017). Our model
predicts that the Orowan stress is almost constant (after the initial
drop) even at lowest strain rate (at 10−4 s−1) as these tests are not
long enough to allow for microstructure degradation. This may also
explain the stress plateau observed during stage 3 tensile loading (cf.
Section 3.1). Initially, deformation occurs due to dislocation climb until
critical resolved stress for glide does not reaches threshold value after
which dislocation glide dominates the deformation. Sudden drop in the
Orowan stress is observed when slip gets activated.
Appendix B. Slip systems considered for the crystal plasticity
model
The slip systems for octahedral and cube slip are adopted from Qin
and Bassani (1992) and listed here. (see Tables B.7 and B.8 ).
Appendix C. Simulated response with different number of ele-
ments
See Fig. C.13.
Table D.9
Euler angles (in Bunge notation) for loading orientations used in the
present work.
Orientation no. Crystal orientation Euler angles
1 [ 001] [0, 0, 0]
2 [ 011] [0, −45, 0]
3 [ ̄111] [45, −54.736, 0]
4 [ ̄123] [255.4, 36.7, 333.43]
Appendix D. Loading orientations used in the present work
See Table D.9.
Fig. E.14. Influence of initial channel width value on the macroscopic response during (a) tensile loading at a strain rate of 10−4 𝑠−1 at 1223 K, and (b) creep loading at 520
MPa at 1123 K stress for [001] orientation for CMSX-4.

## Page 18

Mechanics of Materials 174 (2022) 104474
18
S. Chaudhary et al.
Appendix E. Effect of channel width on the macroscopic response
We have varied the channel width parametrically to study its effect
on the macroscopic response. For this study, three simulations with
varying channel width (keeping the volume fraction of precipitate
constant at 0.72) were performed for both tensile and creep loading of a
[0 0 1] CMSX-4 crystal at 1223 K. These results are shown in Fig. E.14.
The effect of change in channel width on the macroscopic behavior is
significant for tensile loading, with an increase in flow stress as the
channel width decreases. This is primarily an effect of the increase
in the Orowan stress (cf. Eq. (8)) with decrease in channel width.
However, no significant effect was observed on the creep response with
varying channel width.
References
Agaram, S., Kanjarla, A.K., Bhuvaraghan, B., Srinivasan, S.M., 2021. Dislocation density
based crystal plasticity model incorporating the effect of precipitates in IN718
under monotonic and cyclic deformation. Int. J. Plast. 141, 102990.
Ali, M.A., Amin, W., Shchyglo, O., Steinbach, I., 2020. 45-Degree rafting in Ni-based
superalloys: A combined phase-field and strain gradient crystal plasticity study. Int.
J. Plast. 128, 102659.
Allan, C.D., 1995. Plasticity of Nickel Base Single Crystal Superalloys (Ph.D. thesis).
Massachusetts Institute of Technology.
Antolovich, B.F., 1996. Fatigue and fracture of nickel-base superalloys. pp. 854–
868, ASM International, Member/Customer Service Center, Materials Park, OH
44073-0002, USA, 1996.
Antolovich, S.D., Rosa, E., Pineau, A., 1981. Low cycle fatigue of René 77 at elevated
temperatures. Mater. Sci. Eng. 47 (1), 47–57.
Asaro, R.J., Rice, J., 1977. Strain localization in ductile single crystals. J. Mech. Phys.
Solids 25 (5), 309–338.
Austin, R.A., McDowell, D.L., 2011. A dislocation-based constitutive model for vis-
coplastic deformation of FCC metals at very high strain rates. Int. J. Plast. 27 (1),
1–24.
Baldan, A., 2002. Review progress in Ostwald ripening theories and their applications
to nickel-base superalloys Part I: Ostwald ripening theories. J. Mater. Sci. 37 (11),
2171–2202.
Brehm, H., Glatzel, U., 1999. Material model describing the orientation dependent creep
behavior of single crystals based on dislocation densities of slip systems. Int. J.
Plast. 15 (3), 285–298.
Chaboche, J.-L., Gaubert, A., Kanoute, P., Longuet, A., Azzouz, F., Mazière, M., 2013.
Viscoplastic constitutive equations of combustion chamber materials including
cyclic hardening and dynamic strain aging. Int. J. Plast. 46, 1–22.
Chang, J.C., Allen, S.M., 1991. Elstic energy changes accompanying gamma-prime
rafting in nickel-base superalloys. J. Mater. Res. 6 (9), 1843–1855.
Clement, N., Couret, A., Caillard, D., 1991. An in situ study of cube glide in the 𝛾
′
-phase
of a superalloy: I. The controlling mechanism. Phil. Mag. A 64 (3), 669–695.
Desmorat, R., Mattiello, A., Cormier, J., 2017. A tensorial thermodynamic framework
to account for the 𝛾’rafting in nickel-based single crystal superalloys. Int. J. Plast.
95, 43–81.
Ding, Q., Bei, H., Yao, X., Zhao, X., Wei, X., Wang, J., Zhang, Z., 2021. Temperature
effects on deformation substructures and mechanisms of a Ni-based single crystal
superalloy. Appl. Mater. Today 23, 101061.
Epishin, A., Link, T., Klingelhöffer, H., Fedelich, B., Brückner, U., Portella, P.D., 2009.
New technique for characterization of microstructural degradation under creep:
Application to the nickel-base superalloy CMSX-4. Mater. Sci. Eng. A 510, 262–265.
Epishin, A., Link, T., Portella, P.D., Brückner, U., 2000. Evolution of the 𝛾/𝛾’ microstruc-
ture during high-temperature creep of a nickel-base superalloy. Acta Mater. 48 (16),
4169–4177.
Essmann, U., Mughrabi, H., 1979. Annihilation of dislocations during tensile and cyclic
deformation and limits of dislocation densities. Phil. Mag. A 40 (6), 731–756.
Fan, Y.-N., Shi, H.-J., Qiu, W.-H., 2015. Constitutive modeling of creep behavior in
single crystal superalloys: Effects of rafting at high temperatures. Mater. Sci. Eng.
A 644, 225–233.
Fedelich, B., Epishin, A., Link, T., Klingelhöffer, H., Künecke, G., Portella, P.D.,
2012. Rafting during high temperature deformation in a single crystal superalloy:
Experiments and modeling. Superalloys 2012 6, 491.
Fedelich, B., Künecke, G., Epishin, A., Link, T., Portella, P., 2009. Constitutive modelling
of creep degradation due to rafting in single-crystalline Ni-base superalloys. Mater.
Sci. Eng. A 510, 273–277.
Fernandez-Zelaia, P., Lee, Y., Dryepondt, S., Kirka, M.M., 2022. Creep anisotropy
modeling and uncertainty quantification of an additively manufactured Ni-based
superalloy. Int. J. Plast. 103177.
Flinn, P.A., 1960. Theory of deformation in superlattices. Trans. Am. Inst. Min. Metall.
Eng. 218 (1), 145–154.
Gaubert, A., Jouiad, M., Cormier, J., Le Bouar, Y., Ghighi, J., 2015. Three-dimensional
imaging and phase-field simulations of the microstructure evolution during creep
tests of< 011>-oriented Ni-based superalloys. Acta Mater. 84, 237–255.
Geddes, B., Leon, H., Huang, X., 2010. Superalloys: Alloying and Performance. Asm
International.
Geers, M., Cottura, M., Appolaire, B., Busso, E.P., Forest, S., Villani, A., 2014. Coupled
glide-climb diffusion-enhanced crystal plasticity. J. Mech. Phys. Solids 70, 136–153.
Ghorbanpour, S., Zecevic, M., Kumar, A., Jahedi, M., Bicknell, J., Jorgensen, L.,
Beyerlein, I.J., Knezevic, M., 2017. A crystal plasticity model incorporating the
effects of precipitates in superalloys: Application to tensile, compressive, and cyclic
deformation of inconel 718. Int. J. Plast. 99, 162–185.
Ghosh, R., Curtis, R., McLean, M., 1990. Creep deformation of single crystal
superalloys—modelling the crystallographic anisotropy. Acta Metall. Mater. 38 (10),
1977–1992.
Glicksman, M., Fradkov, V., 1995. Kinetics of Diffusional Droplet Growth in a
Liquid/liquid Two-Phase System. Final Technical Report Rensselaer Polytechnic
Inst.
Guo, Z., Huang, D., Yan, X., 2021. Physics-based modeling of 𝛾/𝛾
′
microstructure
evolution and creep constitutive relation for single crystal superalloy. Int. J. Plast.
137, 102916.
Gupta, S., Bronkhorst, C.A., 2021. Crystal plasticity model for single crystal Ni-based
superalloys: Capturing orientation and temperature dependence of flow stress. Int.
J. Plast. 137, 102896.
Henderson, P., Berglin, L., Jansson, C., 1998. On rafting in a single crystal nickel-base
superalloy after high and low temperature creep. Scr. Mater. 40 (2).
Heredia, F., Pope, D., 1991. Effect of boron additions on the ductility and fracture
behavior of Ni3Al single crystals. Acta Metall. Mater. 39 (8), 2017–2026.
Huang, J., Shi, D.-Q., Yang, X.-G., 2016. A physically based methodology for predicting
anisotropic creep properties of Ni-based superalloys. Rare Metals 35 (8), 606–614.
Humphreys, F.J., Hatherly, M., 2012. Recrystallization and Related Annealing
Phenomena. Elsevier.
Ignat, M., Buffiere, J.-Y., Chaix, J., 1993. Microstructures induced by a stress gradient
in a nickel-based superalloy. Acta Metall. Mater. 41 (3), 855–862.
Jacome, L.A., Nörtershäuser, P., Heyer, J.-K., Lahni, A., Frenzel, J., Dlouhy, A.,
Somsen, C., Eggeler, G., 2013. High-temperature and low-stress creep anisotropy
of single-crystal superalloys. Acta Mater. 61 (8), 2926–2943.
Jiang, X., Wang, D., Xie, G., Li, H., Lou, L., Zhang, J., 2014. The effect of long-
term thermal exposure on the microstructure and stress rupture property of
a directionally solidified Ni-based superalloy. Metall. Mater. Trans. A 45 (13),
6016–6026.
Keshavarz, S., Ghosh, S., 2015. A crystal plasticity finite element model for flow stress
anomalies in Ni3Al single crystals. Phil. Mag. 95 (24), 2639–2660.
Keshavarz, S., Ghosh, S., Reid, A.C., Langer, S.A., 2016. A non-schmid crystal plasticity
finite element approach to multi-scale modeling of nickel-based superalloys. Acta
Mater. 114, 106–115.
Kocks, U.F., AS, A., MF, A., 1975. Thermodynamics and kinetics of slip. Prog. Mater.
Sci. 19, 1.
Krausz, A., Krausz, K., 1996. Unified Constitutive Laws of Plastic Deformation. Elsevier
Science, URL: https://books.google.co.in/books?id=OA9PxDRYpUoC.
Laberge, C., Fratzl, P., Lebowitz, J., 1997. Microscopic model for directional coarsening
of precipitates in alloys under external load. Acta Mater. 45 (10), 3949–3962.
Le Bouar, Y., Finel, A., Appolaire, B., Cottura, M., 2022. Phase field models for modeling
microstructure evolution in single-crystal Ni-base superalloys. In: Nickel Base Single
Crystals Across Length Scales. Elsevier, pp. 379–399.
Le Graverend, J.-B., Cormier, J., Gallerneau, F., Villechaise, P., Kruch, S., Mendez, J.,
2014. A microstructure-sensitive constitutive modeling of the inelastic behavior of
single crystal nickel-based superalloys at very high temperature. Int. J. Plast. 59,
55–83.
Lebensohn, R.A., Hartley, C.S., Tomé, C.N., Castelnau, O., 2010. Modeling the me-
chanical response of polycrystals deforming by climb and glide. Phil. Mag. 90 (5),
567–583.
León-Cázares, F., Monni, F., Jackson, T., Galindo-Nava, E., Rae, C., 2020. Stress
response and microstructural evolution of nickel-based superalloys during low cycle
fatigue: Physics-based modelling of cyclic hardening and softening. Int. J. Plast.
128, 102682.
Li, W., Ma, J., Kou, H., Shao, J., Zhang, X., Deng, Y., Tao, Y., Fang, D., 2019. Modeling
the effect of temperature on the yield strength of precipitation strengthening
Ni-base superalloys. Int. J. Plast. 116, 143–158.
Li, Y., Wang, L., He, Y., Zheng, W., Lou, L., Zhang, J., 2022. Role of interfacial
dislocation networks during secondary creep at elevated temperatures in a single
crystal Ni-based superalloy. Scr. Mater. 217, 114769.
Lindström, T., Nilsson, D., Simonsson, K., Eriksson, R., Lundgren, J.-E., Leidermark, D.,
2022. Constitutive model for thermomechanical fatigue conditions of an additively
manufactured combustor alloy. Mech. Mater. 168, 104273.
Liu, J., Jin, T., Sun, X., Zhang, J., Guan, H., Hu, Z., 2008. Anisotropy of stress rupture
properties of a Ni base single crystal superalloy at two temperatures. Mater. Sci.
Eng. A 479 (1–2), 277–284.
Lukáš, P., Čadek, J., Šustek, V., Kunz, L., 1996. Creep of CMSX-4 single crystals of
different orientations in tension and compression. Mater. Sci. Eng. A 208 (2),
149–157.

## Page 19

Mechanics of Materials 174 (2022) 104474
19
S. Chaudhary et al.
Ma, A., Dye, D., Reed, R., 2008. A model for the creep deformation behaviour of
single-crystal superalloy CMSX-4. Acta Mater. 56 (8), 1657–1670.
MacLachlan, D., Knowles, D., 2000. Creep-behavior modeling of the single-crystal
superalloy CMSX-4. Metall. Mater. Trans. A 31 (5), 1401–1411.
MacLachlan, D.W., Wright, L.W., Gunturi, S., Knowles, D.M., 2001. Constitutive
modelling of anisotropic creep deformation in single crystal blade alloys SRR99
and CMSX-4. Int. J. Plast. 17 (4), 441–467.
Masoumi, F., Jahazi, M., Shahriari, D., Cormier, J., 2016. Coarsening and dissolution of
𝛾
′
precipitates during solution treatment of AD730 Ni-based superalloy: Mechanisms
and kinetics models. J. Alloys Compd. 658, 981–995.
Matan, N., Cox, D., Carter, P., Rist, M., Rae, C., Reed, R., 1999a. Creep of CMSX-4
superalloy single crystals: Effects of misorientation and temperature. Acta Mater.
47 (5), 1549–1563.
Matan, N., Cox, D., Rae, C., Reed, R., 1999b. On the kinetics of rafting in CMSX-4
superalloy single crystals. Acta Mater. 47 (7), 2031–2045.
Mesarovic, S.D., 2017. Dislocation creep: Climb and glide in the lattice continuum.
Crystals 7 (8), http://dx.doi.org/10.3390/cryst7080243, URL: https://www.mdpi.
com/2073-4352/7/8/243.
Miura, N., Kondo, Y., Matsuo, T., 2003. Relation between creep rate during accelerating
creep stage and 𝛾 channel thickness in single crystal nickel-based superalloy,
CMSX-4. Tetsu-To-Hagané 89 (12), 1240–1247.
Mughrabi, H., 2014. The importance of sign and magnitude of 𝛾/𝛾
′
lattice misfit in
superalloys—with special reference to the new 𝛾
′
-hardened cobalt-base superalloys.
Acta Mater. 81, 21–29.
Mughrabi, H., Tetzlaff, U., 2000. Microstructure and high-temperature strength of
monocrystalline nickel-base superalloys. Adv. Energy Mater. 2 (6), 319–326.
Murakumo, T., Kobayashi, T., Koizumi, Y., Harada, H., 2004. Creep behaviour of Ni-
base single-crystal superalloys with various 𝛾
′
volume fraction. Acta Mater. 52 (12),
3737–3744.
Nabarro, F.R., 1996. Rafting in superalloys. Metall. Mater. Trans. A 27 (3), 513–530.
Ohashi, T., Hidaka, K., Imano, S., 1997. Elastic stress in single crystal Ni-base
superalloys and the driving force for their microstructural evolution under high
temperature creep conditions. Acta Mater. 45 (5), 1801–1810.
Ohring, M., 1998. Reliability and Failure of Electronic Materials and Devices. Elsevier.
Österle, W., Bettge, D., Fedelich, B., Klingelhöffer, H., 2000. Modelling the orientation
and direction dependence of the critical resolved shear stress of nickel-base
superalloy single crystals. Acta Mater. 48 (3), 689–700.
Paidar, V., Pope, D., Vitek, V., 1984. A theory of the anomalous yield behavior in L12
ordered alloys. Acta Metall. 32 (3), 435–448.
Patra, A., McDowell, D.L., 2012. Crystal plasticity-based constitutive modelling of
irradiated BCC structures. Phil. Mag. 92 (7), 861–887.
Patra, A., Zhu, T., McDowell, D.L., 2014. Constitutive equations for modeling non-
Schmid effects in single crystal BCC-Fe at low and ambient temperatures. Int. J.
Plast. 59, 1–14.
Peach, M., Koehler, J., 1950. The forces exerted on dislocations and the stress fields
produced by them. Phys. Rev. 80 (3), 436.
Permann, C.J., Gaston, D.R., Andrš, D., Carlsen, R.W., Kong, F., Lindsay, A.D.,
Miller, J.M., Peterson, J.W., Slaughter, A.E., Stogner, R.H., Martineau, R.C.,
2020. MOOSE: Enabling massively parallel multiphysics simulation. SoftwareX
11, 100430. http://dx.doi.org/10.1016/j.softx.2020.100430, URL: https://www.
sciencedirect.com/science/article/pii/S2352711019302973.
Phan, V.-T., Zhang, X., Li, Y., Oskay, C., 2017. Microscale modeling of creep defor-
mation and rupture in nickel-based superalloy in 617 at high temperature. Mech.
Mater. 114, 215–227.
Phillips, P., Unocic, R.R., Mills, M.J., 2013. Low cycle fatigue of a polycrystalline
Ni-based superalloy: Deformation substructure analysis. Int. J. Fatigue 57, 50–57.
Pollock, T., Argon, A., 1992. Creep resistance of CMSX-3 nickel base superalloy single
crystals. Acta Metall. Mater. 40 (1), 1–30.
Pollock, T., Argon, A., 1994. Directional coarsening in nickel-base single crystals
with high volume fractions of coherent precipitates. Acta Metall. Mater. 42 (6),
1859–1874.
Porter, D.A., Easterling, K.E., 2009. Phase Transformations in Metals and Alloys
(Revised Reprint). CRC Press.
Qin, Q., Bassani, J.L., 1992. Non-schmid yield behavior in single crystals. J. Mech.
Phys. Solids 40 (4), 813–833.
Ranjan, D., Narayanan, S., Kadau, K., Patra, A., 2021. Crystal plasticity modeling of
non-schmid yield behavior: From Ni3Al single crystals to Ni-based superalloys.
Modelling Simulation Mater. Sci. Eng. 29 (5), 055005.
Reed, R.C., 2008. The Superalloys: Fundamentals and Applications. Cambridge
University Press.
Rodas, E.A.E., Neu, R.W., 2018. Crystal viscoplasticity model for the creep-fatigue
interactions in single-crystal Ni-base superalloy CMSX-8. Int. J. Plast. 100, 14–33.
Sabnis, P.A., Forest, S., Arakere, N.K., Yastrebov, V.A., 2013. Crystal plasticity analysis
of cylindrical indentation on a Ni-base single crystal superalloy. Int. J. Plast. 51,
200–217.
Serin, K., Göbenli, G., Eggeler, G., 2004. On the influence of stress state, stress level
and temperature on 𝛾-channel widening in the single crystal superalloy CMSX-4.
Mater. Sci. Eng. A 387, 133–137.
Sharma, S., Ko, G., Li, F., Kang, K., 2008. Oxidation and creep failure of alloy 617
foils at high temperature. J. Nucl. Mater. 378 (2), 144–152.
Shenoy, M.M., 2006. Constitutive Modeling and Life Prediction in Nickel-Base
Superalloys. Georgia Institute of Technology.
Shenoy, M., Tjiptowidjojo, Y., McDowell, D., 2008. Microstructure-sensitive modeling
of polycrystalline in 100. Int. J. Plast. 24 (10), 1694–1730.
Sims, C.T., Stoloff, N.S., Hagel, W.C., 1987. Superalloys II, Vol. 8. Wiley New York.
Staroselsky, A., Cassenti, B.N., 2010. Combined rate-independent plasticity and creep
model for single crystal. Mech. Mater. 42 (10), 945–959.
Staroselsky, A., Cassenti, B.N., 2011. Creep, plasticity, and fatigue of single crystal
superalloy. Int. J. Solids Struct. 48 (13), 2060–2075.
Stouffer, D.C., Dame, L.T., 1996. Inelastic Deformation of Metals: Models, Mechanical
Properties, and Metallurgy. John Wiley & Sons.
Su, Y., Han, Q.-N., Qiu, W., He, Z., Shang, Y.-B., Shi, H.-J., Niu, L.-S., 2020. High
temperature in-situ SEM observation and crystal plasticity simulation on fretting
fatigue of Ni-based single crystal superalloys. Int. J. Plast. 127, 102645.
Sun, Y., Hazzledine, P., 1996. Geometry of dislocation glide in Ll2 𝛾
′
-phase: TEM
observations. In: Dislocations in Solids, Vol. 10. Elsevier, pp. 27–68.
Sun, S., Li, L., Yue, Z., Yang, W., Zhao, Z., Cao, R., Li, S., 2020. Experimental and
numerical investigation on fretting fatigue behavior of nickel-based single crystal
superalloy at high temperature. Mech. Mater. 150, 103595.
Sundararaman, M., Chen, W., Wahi, R., 1989. Interpretation of fatigue softening at
room temperature in a superalloy. Scr. Metall. 23 (10), 1795–1800.
Svoboda, J., Lukas, P., 1996. Modelling of kinetics of directional coarsening in
Ni-superalloys. Acta Mater. 44 (6), 2557–2565.
Tinga, T., Brekelmans, W., Geers, M., 2008. Incorporating strain gradient effects in
a multiscale constitutive framework for nickel-base superalloys. Phil. Mag. 88
(30–32), 3793–3825.
Tinga, T., Brekelmans, W., Geers, M., 2009a. Directional coarsening in nickel-base
superalloys and its effect on the mechanical properties. Comput. Mater. Sci. 47
(2), 471–481.
Tinga, T., Brekelmans, W., Geers, M.G., 2009b. Cube slip and non-schmid effects in
single crystal Ni-base superalloys. Modelling Simulation Mater. Sci. Eng. 18 (1),
015005.
Titus, M.S., Suzuki, A., Pollock, T.M., 2012. Creep and directional coarsening in single
crystals of new 𝛾–𝛾
′
cobalt-base alloys. Scr. Mater. 66 (8), 574–577.
Vattré, A., Devincre, B., Roos, A., Feyel, F., 2010. Predicting size effects in nickel-
base single crystal superalloys with the discrete-continuous model. Eur. J. Comput.
Mech./Revue Européenne De Mécanique Numérique 19 (1–3), 65–76.
Vattré, A., Fedelich, B., 2011. On the relationship between anisotropic yield strength
and internal stresses in single crystal superalloys. Mech. Mater. 43 (12), 930–951.
Wang, J., Guo, W.-G., Su, Y., Zhou, P., Yuan, K., 2016. Anomalous behaviors of a
single-crystal nickel-base superalloy over a wide range of temperatures and strain
rates. Mech. Mater. 94, 79–90.
Wang, X., Liu, J., Jin, T., Sun, X., 2014. Tensile behaviors and deformation mechanisms
of a nickel-base single crystal superalloy at different temperatures. Mater. Sci. Eng.
A 598, 154–161.
Webster, G., Sullivan, C., 1967. Some effects of temperature cycling on the creep
behavior of a nickel-base alloy. Inst. Metals J. 95 (5), 138–142.
Wen, W., Capolungo, L., Patra, A., Tomé, C., 2017. A physics-based crystallographic
modeling framework for describing the thermal creep behavior of Fe-Cr alloys.
Metall. Mater. Trans. A 48 (5), 2603–2617.
Wen, W., Kohnert, A., Kumar, M.A., Capolungo, L., Tomé, C.N., 2020. Mechanism-
based modeling of thermal and irradiation creep behavior: An application to
ferritic/martensitic HT9 steel. Int. J. Plast. 126, 102633.
Westbrook, J., 1957. Temperature dependence of the hardness of secondary phases
common in turbine bucket alloys. JOM 9 (7), 898–904.
Wu, W.-P., Li, S.-Y., Li, Y.-L., 2019. An anisotropic elastic–plastic model for predicting
the rafting behavior in Ni-based single crystal superalloys. Mech. Mater. 132, 9–17.
Wu, R., Zaiser, M., Sandfeld, S., 2017. A continuum approach to combined 𝛾/𝛾
′
evolution and dislocation plasticity in nickel-based superalloys. Int. J. Plast. 95,
142–162.
Xia, W., Zhao, X., Yue, L., Zhang, Z., 2020. Microstructural evolution and creep
mechanisms in Ni-based single crystal superalloys: A review. J. Alloys Compd. 819,
152954.
Yang, X., Cui, X., Yuan, H., 2020. Correlations between microstructure evolution and
mechanical behavior of a nickel-based single crystal superalloy with long-term
aging effects. Mater. Charact. 169, 110652.
Yu, H., Su, Y., Tian, N., Tian, S., Li, Y., Yu, X., Yu, L., 2013. Microstructure evolution
and creep behavior of a [111] oriented single crystal nickel-based superalloy during
tensile creep. Mater. Sci. Eng. A 565, 292–300.
Yu, Z., Wang, X., Yue, Z., 2020. The effect of stress state on rafting mechanism and
cyclic creep behavior of Ni-base superalloy. Mech. Mater. 149, 103563.
Zhang, K.-S., Ju, J.W., Li, Z., Bai, Y.-L., Brocks, W., 2015. Micromechanics based fatigue
life prediction of a polycrystalline metal applying crystal plasticity. Mech. Mater.
85, 16–37.
Zhang, Y., Yang, C., Xu, Q., 2020. Numerical simulation of microstructure evolution in
Ni-based superalloys during P-type rafting using multiphase-field model and crystal
plasticity. Comput. Mater. Sci. 172, 109331.
Zhang, L., Zhao, L., Roy, A., Silberschmidt, V., Mccolvin, G., 2019. Low-cycle fatigue of
single crystal nickel-based superalloy–mechanical testing and TEM characterisation.
Mater. Sci. Eng. A 744, 538–547.
