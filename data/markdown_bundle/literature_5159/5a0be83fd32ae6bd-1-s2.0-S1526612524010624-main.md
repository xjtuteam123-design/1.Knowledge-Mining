# 1-s2.0-S1526612524010624-main

<!-- source: D:\总文献\1-s2.0-S1526612524010624-main.pdf -->
<!-- file_sha256: 3e41a65d325549a4ffaab2b78096c48b3afa3802a7ef95981a882b9a407d1a60 -->

## Page 1

Review article
Current status and potential strategies for crack-free tungsten by laser
powder bed fusion: A review
Lina Ji
a , *
, Shenyu Wei
a
, Zeli Wang
b
, Yuanbin Zhang
c
, A.V. Radhamani
d
,
Ramakrishna Seeram
e
a
Chongqing Institute of Green and Intelligent Technology, Chinese Academy of Sciences, Chongqing 400714, China
b
School of Materials Science and Engineering, Dalian University of Technology, Dalian 116024, China
c
School of Materials Science and Engineering, Shandong Jianzhu University, Jinan 250101, China
d
Department of Physics and Nanotechnology, SRM Institute of Science and Technology, Chennai, 603202, India
e
College of Design and Engineering, Department of Mechanical Engineering, National University of Singapore, Singapore, 117575, Singapore
ARTICLE INFO
Keywords:
Tungsten (W)
Tungsten-based materials
Laser powder bed fusion
micro cracking
Density
Crack-free W
ABSTRACT
Tungsten (W) has wide application in many high-end fields, however, post-processing and forming of complex
parts are difficult for traditional manufacturing due to its inherent properties. Therefore attention has been paid
to laser powder bed fusion (LPBF) of W. But there are micro cracking and pores in as-built parts, which decrease
density, quality and limit their wide application. The current status of LPBF of W is reviewed with emphasis on
the overall influence factors of powder property and process parameters (laser parameters, forming parameters
and other parameters) on their density/quality at first, then formation mechanism of defects, numerical simu-
lation, complex parts and their application are followed. Next, traditional methods to reduce defects by alloying
and composites are summarized. The reason for cracking in LPBF of W is mainly due to solid-state cracking and
hot cracking as well. For the indelible micro cracking in as-built parts, potential strategies of structure design,
composition optimization, hybrid additive manufacturing methods, grain boundary engineering, defect engi-
neering, metastability engineering and post treatment are put forward.
1. Introduction
Tungsten (W) and W-based materials (W alloys and W-based com-
posites) have many advantages such as high melting point, high
strength, high thermal conductivity and chemical stability. Therefore
they have wide application in aerospace, weaponry, nuclear energy,
automotive, defense, optics and biomedical apparatus [ 1 – 3 ]. However,
post-processing and forming of complex parts are difficult for traditional
manufacturing due to their inherent hardness, brittleness, high ductile-
to-brittle transition temperature (DBTT) and low recrystallization tem-
perature [ 4 ].
Additive manufacturing (AM) technique has advantages in forming
parts with less waste of materials and near net-shape in layer by layer
stacking, especially for those that are difficult for traditional processing,
complex shapes, or customized products, and has wide application in
many fields [ 5 – 9 ]. However, due to the large temperature gradient
during rapid courses of melting and cooling, there are thermal and re-
sidual stress in as-built parts, which usually cause the warping and
deformation of parts [ 10 ]. When residual stress is over materials ’ ulti-
mate tensile strength, cracking is easy to appear, which leads to low
density and quality. Besides, large temperature gradient causes coarse
columnar grains growth and the consequent anisotropic mechanical
properties.
Compared to other metal-based AM techniques such as electron
beam powder bed fusion and direct energy deposition, laser powder bed
fusion (LPBF) has higher accuracy, which has become the popular
technique for AM of W. Therefore this review is mainly focused on LPBF
of W, different from former reviews that are concentrated on AM of W,
W alloys or W-based composites [ 11 – 13 ]. LPBF of W is more difficult
than other metallic materials because its melting point (3420
◦
C) is the
highest among metals and needs more energy to melt. While high
thermal conductivity of 173 W/m ⋅ K results in loss of energy quickly, and
melt of W has high viscosity of ~8 mPa ⋅ s and high surface tension of
2361 mN/m, therefore the balling phenomenon appears easily [ 11 ]. The
hardness and brittleness, high DBTT and volatilization of WO
3
often lead
to micro cracking [ 14 ]. The sketch of LPBF process and the defects of
* Corresponding author.
E-mail address: lnji@cigit.ac.cn (L. Ji).
Contents lists available at ScienceDirect
Journal of Manufacturing Processes
journal homep age: www. elsevier.com/ locate/m anpro
https://doi.org/10.1016/j.jmapro.2024.10.020
Received 19 December 2023; Received in revised form 25 September 2024; Accepted 7 October 2024
Journal of Manufacturing Processes 131 (2024) 2535–2554 
Available online 5 November 2024 
1526-6125/© 2024 The Society of Manufacturing Engineers. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, 
and similar technologies.

## Page 2

pores and micro cracking in as-built W are shown in Fig. 1 . The reason
for defects in W-based materials is similar if they contain most of W and
less other elements or reinforced phases. But if content of the added
phases is high, the melting temperature is lower, then defects especially
micro cracking may not exist and is not an issue any more, such as W
heavy alloys. Therefore, only those with high content of W ( > 90 wt%)
will be discussed in this review considering its use for plasma-facing
materials, which is indeed useful as reference for manufacturing of
defect-free parts for critical composition requirement [ 15 ].
To print defect-free W with high density and good quality as those
prepared by traditional methods has become the hot and difficult
research topic for the whole AM community [ 16 ]. Due to the dependent
relationship of defects and density of as-built W, this review will base
and focus on the comprehensive influence factors for density, then
classify and summarize them from powder property and process pa-
rameters (including laser parameters, forming parameters and other
parameters like post treatment). Besides, the detailed powder and pro-
cess parameters are listed for reference. Next, defect formation mecha-
nism, numerical simulation, complex parts and their application for
LPBF of W are illustrated. The normal methods to reduce defects and
increase density of LPBF of W such as alloying and composites are fol-
lowed. For the difficulty to eliminate micro cracking, potential strategies
of structure design, powder composition optimization, new hybrid AM
methods, grain boundary engineering, defect engineering, metastability
engineering and post treatment are put forward. This is the novelty and
main difference from former reviews of AM of W. At last is conclusion to
complete the review and the schematic diagram for the whole review is
shown in Fig. 2 .
2. Influence factors for density of LPBF of W
Based on the interaction mechanism of laser and powder, powder
property, laser mode and process parameters can all influence the
quality of LPBF of W [ 17 ]. Powder property is the principal factor that
determines the final quality of as-built parts [ 15 , 18 – 20 ]. For the same
powder, under various process parameters, the forming morphology,
precision and quality of as-built parts are different, therefore process
parameters are necessary to be optimized. Other factors such as scanning
strategy, substrate preheat temperature, atmosphere in the chamber,
support structure, with or without post treatment can be chosen to
reduce defects.
2.1. Powder property
Powder property includes powder size and size distribution, powder
morphology/flowability, composition and structure of powder. The
energy (E) needed to raise the temperature of powder materials is as
formula (1) [ 21 ]:
E =
4
3
π r
3
p
ρα C
p
Δ T (1)
where r
p
is powder radius, ρ is material density, α is energy absorptivity
coefficient of powder, Cp is material specific heat and Δ T is temperature
rise of powder. It indicates that the particle size of powder can affect E
directly. Smaller size of W powder has more absorptivity of laser energy,
more distribution of absorbed irradiance, which needs less energy for
melting and can form continuous, homogeneous and smooth molten
tracks as shown in Fig. 3 [ 22 ]. Due to its high melting point, powder size
and its distribution of W (usually 5 – 25 μ m) for LPBF is much smaller and
narrower than that normally used (15 – 45 μ m) for other metal powders
in order to decrease input laser energy for powder melting. Powder with
wider particle size distribution especially with bimodal distribution has
larger stacking density, less porosity and less gas among the powder than
that with similar average powder size, which is beneficial to decrease
porosity inside as-built W.
Powder morphology influences its stacking density and flowability.
Spherical powder is easy to spread homogeneously on the substrate and
is beneficial for density improvement. Enneti et al. [ 23 ] used W powder
with irregular morphology and obtained W parts with density of only 75
% even under high volumetric energy density (E
V
) of 1000 J/mm
3
,
which may be because that laser power of 90 W is too low even if
scanning speed of 200 mm/s, hatch space (HS) of 15 μ m and layer
thickness (t) of 30 μ m are suitable. The density was increased to 96.4 %
after optimization of process parameters to 300 W, 300 mm/s, HS = 70
μ m and t = 30 μ m with more spherical powder [ 24 ]. Usually powder
plasma spheroidization technique with high temperature ( > 10,000
◦
C)
and high pressure plasma is used to prepare spherical powder for
printing, which helps to volatilize impurities, and obtain continuous
molten tracks with smooth surface. The morphology comparison of
molten tracks is shown in Fig. 4 with irregular and spherical W powder
[ 25 ]. Besides, plasma spheroidized powder has more energy absorptiv-
ity, stacking density, better flowability and wide size distribution
[ 25 , 26 ]. With spherical powder, the density can be improved to 96.0 %
[ 25 ], 96.9 % [ 27 ], 96.95 % [ 28 ], 97.3 % [ 29 ], 98.7 % [ 30 ] and 99.1 %
Fig. 1. Sketch of LPBF process and defects of pores and micro cracking in as-built W.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2536

## Page 3

[ 31 ] under optimized Ev of 356 (400 W, exposure time of 200 μ s, point
distance of 75 μ m, HS = 100 μ m, t = 30 μ m) [ 25 ], 293 (475 W, 600 mm/
s, HS = 90 μ m, t = 30 μ m) [ 27 ], 313 (300 W, 400 mm/s, HS = 80 μ m, t =
30 μ m) [ 28 ], 222 (300 W, 750 mm/s, HS = 60 μ m, t = 30 μ m [ 29 ] J/
mm
3
), and (360 W, 600 – 1200 mm/s, HS = 40 – 100 μ m and t = 20 μ m)
[ 31 ], respectively.
Elements are easy to evaporate due to the high input laser energy and
high melting temperature. Element segregation also exists thoughcool-
ing rate is rapid during LPBF, therefore powder composition is an
important factor [ 32 ]. Electron probe micro analyzer and atom probe
tomography are usually used for characterization of element segregation
near cracking in order to adjust powder composition [ 33 ]. According to
the characteristic of metal AM, special powder with customized
composition is very important to obtain crack-free as-built parts. This
has already been proved in LPBF of crack-free Al alloys and Ni-based
alloys by optimization of composition based on thermodynamic calcu-
lation and machine learning [ 34 , 35 ]. For crack-free LPBF of W, the
compositions for traditional preparation methods could be good refer-
ences [ 36 , 37 ].
2.2. Process parameters
Process parameters include laser parameters, forming parameters
and other parameters such as scanning strategy, substrate geometry and
preheat temperature, atmosphere in the chamber, with/without post-
treatment and support structure. The numerous process parameters
are important for quality improvement. Usually laser parameters are
fixed during printing and forming parameters need to be adjusted for
optimization. Other parameters are usually adjusted to decrease tem-
perature gradient and residual stress, which are often fixed during
printing once they are chosen.
2.2.1. Laser parameters
The diameter and shape of laser beam are important parameters,
which are usually fixed during printing. Smaller beam diameter has
higher power density, therefore lower laser power is needed for the same
input energy, and the efficiency with small beam diameter can be
improved by increasing scanning speed. For the shape of laser beam, the
transverse elliptical beam along the scanning direction has lower tem-
perature gradient and larger cooling rate compared to the circular beam
and longitudinal beam, which is in favor of forming equiaxial grains
Fig. 2. Schematic diagram of the review.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2537

## Page 4

[ 38 ]. Vrancken et al. [ 39 ] found that micro cracking for single molten
track of W is strain rate dependent, and the relationship of crack tem-
perature and strain rate (for beam diameter of 100 μ m) to linear energy
density E
L
(E
L
is ratio of laser power to scanning speed) is shown in
Fig. 5 . It indicates that crack temperature comes from the high strain
rate, which resulted from the edge dislocation glide for low E
L
, and
cracks are not easy to appear for small beam diameter.
Usually continuous wave laser is used for LPBF, which has contin-
uous and pulse function modes. Under continuous mode, the forming
efficiency is improved and higher density can be obtained, but the size
accuracy is bad; while the temporal and spatial adjustment for pulse
mode will influence the temperature field, improve cooling rate, refine
grain size and improve mechanical properties, which is suitable for
forming of complex parts like thin-walled and lattice structures with
high precision and low density [ 40 – 43 ]. While Mantel et al. [ 44 ] found
that continuous mode is better to obtain size consistency for lattice
structure. Pulse laser has much higher energy density to melt powder
and has drawn attention in LPBF [ 45 ]. W parts with density of 99 % have
been obtained by LPBF with femtosecond laser, whose grains for surface
and cross section become finer and the mechanical properties are better
compared to those obtained with picosecond pulse width laser and
continuous wave laser as shown in Fig. 6 [ 46 – 48 ].
2.2.2. Forming parameters
Forming parameters include laser power ( P ), scanning speed ( v ),
hatch space ( HS ), exposure time ( ET ), point distance ( PD ) and layer
thickness ( t ). For the usual adjusted parameters like laser power,
scanning speed and hatch space, laser power has the most apparent ef-
fect on density. The curved grains along scanning direction turn to
relatively straight columnar grains with the increase of scanning speed,
and hatch space has no apparent effect on grain size while a little effect
on their morphology [ 49 ]. Exposure time is the time when laser is on and
reacts with powder for laser pulse mode. Point distance is the distance
for laser jumping from one spot to the other spot when laser is on to react
with powder, which is also for pulse mode. The ratio of point distance to
exposure time is considered as scanning speed because laser turn on and
off time can be ignored compared to exposure time. According to
different laser modes, E
L
and Ev can be depicted as formulas (2) and (3) :
E
L
= P / v = P ⋅ ET / PD (2)
E
V
= P / v ⋅ HS ⋅ t = P ⋅ ET / PD ⋅ HS ⋅ t (3)
The powder cannot be completely melted with too low laser energy
and the density is low with increased apparent porosity. However, there
is splash for powder and melt with too high laser energy, which gener-
ates defects like closed porosity and micro cracking, and low density as
well [ 50 ]. Zhang et al. [ 51 ] obtained W with density of 82 % under E
V
of
3200 J/mm
3
(200 W, 25 mm/s, HS = 50 μ m, t = 50 μ m). Guo et al.
[ 52 , 53 ] obtained parts with density of 98.4 % under optimal E
V
of 1000
J/mm
3
(300 W, 300 mm/s, HS = 50 μ m and t = 20 μ m), whose micro-
structure and compressive stress-strain curve compared with those
under different energy densities are shown in Fig. 7 . However, Ren et al.
[ 54 ] obtained W parts with similar density of 98.51 % under much lower
E
V
of 322 J/mm
3
(300 W, 300 mm/s, HS = 103.6 μ m, t = 30 μ m). Tan
et al. [ 55 ] put forward that formula (4) is workable to completely melt
Fig. 3. Morphology of the surface of scanning track for W powder on a stainless steel substrate for different particle sizes: (a) D50 = 5.7 μ m; (b) D50 = 22.47 μ m; (c)
D50 = 37.26 μ m and (d) D50 = 47.63 μ m. Partial magnified details are shown in the insets. D50 refers to the particle size, which means a cumulative particle size
distribution percentage of 50 % [ 22 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2538

## Page 5

the powder,
π r
2
× 0 . 8 × 2 α P ( 1 e
 2
) × Δ t
V
m
× π r
2
b
≥ ρ C
p
( T
m
 T
0
) + ρ L
f
(4)
where r is radius of molten area, α is laser absorptivity, P is laser power,
Δ t is exposure time, V
m
is molten volume of powder, r
b
is radius of laser
beam, T
m
is melting point of powder, T
0
is original temperature of
powder, ρ is powder density, C
p
is specific heat, L
f
is molten latent heat.
They obtained W parts with density of 98.5 % under E
L
of 0.667 J/mm
(200 W, 300 mm/s). Wen et al. [ 56 ] increased density of W parts to
98.71 % with E
V
of 333.3 J/mm
3
(200 W, 200 mm/s, HS = 100 μ m, t =
30 μ m), whose compressive curve indicates that W parts with best
compressive mechanical properties are not those with the highest den-
sity [ 40 , 57 , 58 ]. Rebesan et al. [ 59 ] achieved W parts with density of
99.6 % by adjusting the process parameters based on single scan track.
It is known that E
V
differs much for different researchers, which may
be due to different printers and process parameters. Though laser energy
density could be referred for design of process parameters, there is
limitation because it cannot depict the complex dynamic behavior of
molten pool [ 60 ].
2.2.3. Other parameters
Other parameters include scanning strategy and scanning angle,
substrate geometry and preheat temperature, printing atmosphere,
with/without post treatment, support structure and geometrical shape.
The scanning strategy includes scanning length and scanning times
(laser remelting), usually the zigzag scanning strategy with rotation of
67
◦
between layers is adopted to decrease residual stress [ 61 , 62 ].
However, this should be designed and optimized according to crystal-
lographic concepts to get better results [ 31 ]. The laser remelting for
once or several times can melt W powder completely, which can
decrease porosity and surface roughness, and increase density [ 59 ].
At present, micro cracking could not be eliminated even when sub-
strate is heated to 1000
◦
C [ 63 ]. Ivekovic et al. [ 64 ] obtained higher
density W and W alloys with lower oxygen content, which can be ach-
ieved by adding reducing gas/materials [ 65 ]. Dong et al. [ 66 ] found that
the surface roughness is lower, while density (97.05 %), maximal
compressive strength (1074 MPa) and bend strength (153 MPa) under
N
2
are higher than those obtained under Ar atmosphere (95.46 %, 1015
MPa and 124 MPa, respectively) with the same Ev of 803.6 J/mm
3
(450
W, 400 mm/s, HS = 70 μ m, t = 20 μ m).
Suitable post heat-treatment temperature should be chosen for W
parts since grains are easy to grow up at high temperatures, which lead
to low mechanical quality [ 67 , 68 ]. Chen et al. [ 69 ] found that hot
isostatic pressing (HIP) had a little effect on density of LPBF of W parts,
but thermal conductivity increased about 16 % and the comparison of
microstructure and cracking before and after HIP are shown in Fig. 8 .
While Shi et al. [ 70 ] found that the density increased from 95.91 % (as-
built) to 98.97 % after HIP.
Zhou et al. [ 71 ] found that the grain structure and crack behaviors
were different for LPBF of W with different geometrical shapes and
support structures due to the various absorbed laser energy and cooling
rate. Seyam et al. [ 72 ] reviewed that different substrates influenced the
nucleation energy barrier and spread of W melt on the substrate.
Fig. 4. Scanning electron microscopy (SEM) images showing the morphologies of (a) polyhedral and (b) spherical tungsten powders; and SEM images showing the
top surface of tungsten parts fabricated using (c) polyhedral and (d) spherical powders [ 25 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2539

## Page 6

3. Forming mechanism of defects
3.1. Forming mechanism of pores
Lack of fusion can cause irregular unmelted pores, while too large
laser energy can lead to keyhole. The high melting point, thermal con-
ductivity, viscosity, surface tension and oxytropism of W contribute to
easy formation of pores, too. Zhou et al. [ 73 , 74 ] found that when melt
spreads, the angle between underlayer or substrate to the tangent line of
melt surface, θ
a
, decreased. While when melt solidifies, the angle be-
tween underlayer or substrate to the tangent line of solid surface, θ
s
,
increased ( Fig. 9 (a)). θ * is denoted when θ
a
= θ
s
, the dependent Stefan
number S for a certain material is as formula (5) [ 75 ]:
θ
*
= f ( S ) , S = C
p
 
T
f
 T
t
)/
L
f
(5)
C
p
is specific heat, L
f
is latent heat for melting, T
f
and T
t
are tem-
peratures for melting front and for underlayer or substrate, respectively.
It is known that θ * is not only related to material, but also to the dif-
ference of temperatures, therefore preheating of substrate can improve
density. When θ
a
≈ θ
s
, the solidification time τ is as formula (6) :
τ = 2
 
a
2
/
3 α
)
ln ( T
0
 T
at
)
/ 
T
f
 T
at
)
(6)
α is the coefficient of thermal diffusivity, T
at
is atmosphere temper-
ature, T
0
is the overheat temperature of molten drop and latent heat is
ignored. The relationship of τ and T
0
is shown in Fig. 9 (c). The spread
time for W melt drop is about 86.3 μ s, and the solidification time is about
46 μ s at 6000 K and about 7.6 μ s near melting point, which causes easy
balling phenomenon and pores further ( Fig. 9 (b)). Oxidation results in
balling and pores due to Marangoni flow from high temperature and low
surface tension to the direction of low temperature and high surface
tension. Usually the surrounding area of holes has higher oxygen
content.
3.2. Forming mechanism of cracking
Forming mechanism of cracking during LPBF is similar to that for
traditional casting and welding, which is mainly hot cracking. Hot
cracking, also known as hot tearing, includes solidification cracking and
liquation cracking due to thermal contraction and solidification
shrinkage. Solidification cracking usually occurs at final stage of solid-
ification, which is normally within molten pool or mushy zone with
feature of cells/dendrites [ 76 ]. Liquation cracking occurs at heat
affected zone and along grain boundaries, which is usually due to low
melting-point phases [ 77 ]. There is also solid-state cracking, which oc-
curs at a relatively lower temperature and includes strain-age cracking
and ductility-dip cracking. Strain-age cracking is especially for
precipitation-hardening Ni-based super-alloys and occurs at heat-
affected zone and grain boundaries typically with carbides acting as
cracking initiation points during post heat treatment or reheating during
AM. Ductility-dip cracking happens when materials suffer from a sharp
reduction in ductility in a temperature range between solidus and
approximately half the solidus temperature and produces intergranular
cracking, which increased around high angle grain boundaries [ 78 ]. The
obvious virtue of solid-state cracking is lack of cells/dendrites and liquid
film. Different types of cracking are shown in Fig. 10 [ 79 ].
Pure W solidifies at the freezing point, therefore the melt may not fill
in dendrite gaps during rapid cooling of LPBF. Then pores are easy to
appear and cause stress concentration and cracking further. This is
different from W alloys and other alloys, which have some range of
solidification temperature for liquid to backfill though they both belong
to solidification cracking. For W-based composites with second phases
addition, the most important effect is heterogeneous nucleus to refine
grains, which shorten the gap among grains for liquid to fill easily.
Therefore both W alloys and W-based composites can reduce cracking,
however cracking cannot be eliminated. This may be because that there
is still solid-state cracking especially ductility-dip cracking during LPBF
of W.
Low level impurities also have an effect in cracking. Wang et al.
[ 80 , 81 ] found that volatilization of WO
3
during solidification formed
nano pores, which aggregated and separated near the grain boundary to
Fig. 5. (a) Temperature at the micro-cracking location as a function of P/v,
extracted from the thermal Diablo model. (b) Strain rate for all 100 μ m beam P-
v combinations upon reaching 650 K (the maximum crack temperature),
extracted from the thermo-mechanical Diablo model. The temperature markers
are the median values, the error bars correspond to the IQR (interquartile range
error bar), which is asymmetric. The red markers correspond to parameter sets
for which longitudinal cracking was observed [ 39 ]. (For interpretation of the
references to colour in this figure legend, the reader is referred to the web
version of this article.)
Fig. 6. Comparison of SEM images for cross section of tungsten samples made by femtosecond, 20 ps, 200 ps and continuous wave laser from left to right,
respectively (extracted from Ref. [ 47 ]).
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2540

## Page 7

Fig. 7. OM images showing the microstructure of SLM-processed pure W parts at different energy densities: (a) E = 667 J/mm
3
, (b) E = 833 J/mm
3
, (c) E = 1000 J/
mm
3
, (d) Compressive stress-strain curves for SLM-processed pure W samples under different energy densities [ 53 ].
Fig. 8. The microstructure and crack distribution in as-built and post-HIPed samples from the top view: (a) IPF mapping and (b, c) corresponding SEM image of the
as-built sample, (d) IPF mapping and (e, f) corresponding SEM image of the post-HIPed sample. Molten tracks are marked by white curves while crack tips and
passivated cracks are indicated by red circles. The red lines in (a, d) represent subgrain boundaries (misorientation < 15
◦
) whereas black lines represent grain
boundaries (misorientation > 15
◦
) [ 69 ]. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2541

## Page 8

cause cracking. Cracking grows along grain boundary with longitudinal
cracks (mainly at center of molten track) and transverse cracks inter-
connect with each other to form crack networks [ 82 ]. Remelting cannot
eliminate cracking though scanning strategy and microstructure opti-
mization can affect the distribution mode of cracking.
High DBTT is one important reason for cracking in LPBF of W,
decreasing DBTT is beneficial to resolve this problem, so as to increase
the ductility. At present, due to the defects of cracking and pores in LPBF
of W, little study is on DBTT of LPBF of W and to decrease it. Ductility
improvement can refer to other crack-sensitive materials. Mitigation and
elimination defects of pores and cracking to improve quality of LPBF of
W will be illustrated in Parts 6 and 7. Anyway more efforts are needed to
study on cracking of LPBF of W whatever on micro-scale experiment
characterization or simulation in order to eliminate cracking.
4. Numerical simulation
Only trial-and-error experiment is insufficient to obtain high quality
as-built W. Numerical simulation could help to understand the dynamic
course and evolution mechanism of the whole process. The normal
method is a multi-physics, multi-scale finite element analysis to predict
the thermos-kinetic and thermos-mechanical effects. High throughput
calculation based on machine learning could give optimized results
within several iterations to reduce experimental cost.
Estrada-Diaz et al. [ 83 ] studied the model for high density of LPBF of
metal parts and put forward new formula (7) :
ρ = f ( P , h , v , C
P
, k ) (7)
It indicates that density is not only related to process parameters like
laser power, scanning speed, hatch space( h ), but also to materials ’
properties like thermal conductivity ( k ) and specific heat ( C
p
). This can
give more accurate results compared to those just considering process
parameters. The above 5 parameters are independent variables for
density. The theoretical density for a certain laser power and its corre-
sponding scanning speed according to related dimensionless quantity π
0
and independent π
1
is listed in formulas (8) – (9)
Fig. 9. (a) An illustrative drawing demonstrated the competitive relationship of the spreading and arresting of the melt line. (b) The SEM micrograph revealed the
morphology of one arrested droplet. (c) The calculated solidification time ( τ ) plotted versus the temperature (T
0
) for five metals when T
t
is set as 288 K [ 68 ].
Fig. 10. Schematic illustration of different types of cracking during LPBF (a) with enlarged images for solidification cracking (b), liquation cracking (c) and ductility-
dip cracking (d), respectively. Arrow means laser scanning direction. BTR: brittle temperature range, HAZ: heat-affected zone, DTR: ductility-tip temperature
range [ 79 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2542

## Page 9

v =
(
P
1 α
C
ρ
th
h
2
(
kh
C
P
)
α
)
1
3 2 α
(8)
π
0
=
ρν
3
h
2
P
, π
1
=
κ υ
2
h
PC
p
, π
0
= C π
α
1
(9)
The fitted curve coincidence for π
0
and π
1
is good according to
experimental results of LPBF of W [ 23 ].
Todo et al. [ 31 ] simulated the thermal diffusivity and found that the
strategy of double direction scanning and rotating 90
◦
between layers
can obtain the 〈 011 〉 texture along scanning direction, which resembles
single crystal W and obtain the maximal density of 99.07 %. The model
for heat source is listed in formula (10) :
Q =
4 α P
π r
2
b
H
exp
(
 
2r
2
r
2
b
)
[
1 
z
H
]
( 0 < z < H ) (10)
where Q is unit volumetric energy, r
b
is laser radius, r is the distance
from the laser spot center to the powder bed, α is laser absorptivity, H is
depth of permeation, z is depth. But due to its high melting point and
thermal conductivity, the direction for thermal flow when laser scans,
the shape and temperature distribution of molten pool for W are
different from those of titanium alloy as shown in Fig. 11 . The texture is
mainly determined by materials ’ thermal physical properties and shape
of molten pool.
Due to the ubiquitous problem of micro cracking in as-built W, the
simulation for related dynamics, shape and temperature distribution of
molten pool, residual stress and deformation, optimization of process
parameters, heat and mass transportation, and microstructure is bene-
ficial to deeply understand the printing course and mechanism of LPBF
of W [ 84 ]. The melt is opaque for direct observation and it is difficult to
monitor melting temperature due to the high melting point of W,
therefore the in-situ quality monitoring based on high-speed camera, X-
CT, plasma spectrum, acoustic signal as well as machine learning are
important and can give guidance to experiment and simulation [ 85 , 86 ].
5. Complex parts and their application
Including its excellent high-temperature properties, W has high
sputtering threshold and low retention of tritium to be used as plasma-
facing materials in present and future nuclear fusion devices [ 55 ].
Therefore less other elements or phases are better considering the
detrimental effect with neutron and other particles ’ irradiation. Besides,
metallic composites with W as a reinforcement becomes increasingly
interesting as plasma-facing components application for advanced
plasma-facing and structural heat sink materials [ 87 ]. Except use as
nuclear materials [ 87 , 88 ], complex W parts also have vital application
in sub-wavelength image in water due to its significant acoustic
impedance mismatch with water [ 89 ]. Another important application is
medical shielding and image for detrimental rays [ 90 – 93 ]. Therefore
printing of thin-walled and other complex structures is demanding
( Fig. 12 ), besides the issues of residual stress and micro-cracking in bulk
W are less problematic for thin-walled structures [ 87 ]. Muller et al. [ 87 ]
printed W thin-walled honeycomb structure with liquid Cu infiltrated to
combine high-temperature strength and high thermal conductivity
properties, which is beyond existing Cu-based alloys for high-heat-
loaded plasma facing components ( Fig. 12 (b), (c)). Gear et al. [ 92 ]
printed W disk collimator with density of 80 % and thickness increase of
20 %, and found that though its attenuation decreased 33 % compared to
100 % W, while increased about 15 % compared to Pb collimator.
Sidambe et al. [ 93 ] printed 4 cm length W parts with 500 μ m microhole
for γ -ray collimation, whose beam diameter for the emergent ray is
similar without leakage of ray. In order to protect the plasma facing
component, the lattice structure with fitted thermal conductivity and
structure as the sacrificed limiter component is customized in design of
EU-DEMO, which reduces influence of temperature gradient, stress and
crack sensitivity due to different materials [ 44 ]. This is especially suit-
able to form by AM methods. Besides, it is easier to improve ductility of
such lattice structure by design and by composition adjustment.
There are problems of low accuracy of size and surface, and easy
deformation during printing of complex parts like thin-wall structure.
When thickness of thin-wall is similar to the width of molten pool, there
is powder sticking phenomenon for both sides of molten pool [ 94 – 96 ].
Xie et al. [ 97 ] gave the model for printing thin-wall W parts by choosing
suitable laser power and scanning speed as formulas (11) and (12) ,
respectively:
T = a + bP (11)
T = c + d × e
( v / f )
(12)
where T is thickness of the thin-wall ( μ m), a and b are intercept and
slope of the T-P line, while c is the minimum wall thickness in theory, f is
constant scanning rate, and d is constant for fitting of the correlation
between wall thickness and scanning speed ( v ). Laser remelting can
decrease the thickness of thin-wall and improve density of molten track
[ 97 ].
6. Normal methods to improve quality of LPBF of W
Due to its important application, it is better to eliminate defects of
pores and micro cracking in LPBF of pure W. Many efforts have been
tested to improve the quality of as-built W parts including W-based
materials of alloys and composites by adding other elements/phases to
refine grains, adjust the interface energy, grain boundary, local range
order besides the corresponding optimization of powder composition
and process parameters [ 98 ].
6.1. W alloys
W alloys decrease the melting temperature and can be solution
strengthened by forming solid solution, refining grain size and inhibiting
cracking to extend [ 99 – 103 ]. If the added metal elements are easier to
combine with oxygen, the amount of nano pores around grain bound-
aries can be decreased and the intergranular bonding strength can be
increased [ 104 ]. The intragranular distribution of Nb
–
O nano pores
and nano phases after 5 wt% of Nb added to W compared to pure W is
shown in Fig. 13 . Li et al. [ 105 ] compared the irradiation effect of rolled
W, LPBF of W and LPBF of W
–
6Ta alloy, and found that though cracks
could not be completely eliminated for W
–
6Ta, fuss structure resulted
from irradiation is inhibited due to solution strengthening, Ta nano
oxides and higher density of defects. Guo et al. [ 106 ] ball milled W with
1wt%Ni and 1wt%Fe nano particles and obtained nearly complete dense
parts by LPBF, whose compressive strength (2638 MPa) and strain (46
%) are the maximum until now. Liu et al. [ 107 ] obtained 99.1 % parts
with 6wt%Ti (average size of 15.85 μ m) added, however there are still
micro cracking inside.
6.2. W-based composites
The added ceramic phases can also decrease grain size and improve
density by heterogeneous nucleation of W-based composites [ 108 – 110 ].
Li et al. [ 111 , 112 ] found that grain size decreased from 10.1 μ m (pure
W) to 5.6 μ m and the density of cracking decreased 88.7 % by adding
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2543

## Page 10

0.5 wt% ZrC due to formed ZrO
2
and decreased oxygen content at grain
boundaries. Hu et al. [ 113 ] compared the micro structure and cracking
of pure W, W composites with addition of micro and nano Y
2
O
3
and
obtained parts with density of 98.3 %, for which decrease of cracking
was mainly due to plenty of low angle gain boundary without W grains
refined obviously. However, Wei et al. [ 114 , 115 ] decreased the porosity
and grain size (about 51 %) obviously by adding 2 wt% nano La
2
O
3
powder with mechanical properties improved as shown in Fig. 14 .
Vrancken et al. [ 116 ] used the synergy of substrate preheat and 2 wt%
adding of rare earth oxides (REO) (La
2
O
3
, CeO
2
, 1.75 wt% La
2
O
3
+
0.12wt%ZrO
2
+ 0.12wt%Y
2
O
3
), and found that cracking was eliminated
by preheat to 773 K and molten track was stable and smooth with REO
added as shown in Fig. 15 . However, it only used W substrate without
powder and is not LPBF of W actually.
Fig. 11. Schematic illustrations of melt pool formed through laser scanning for (a, c, e, g) tungsten and (b, d, f, h) titanium alloy with temperature distribution on xy-
plane (a, b) and heat flow directions on yz-plane (c, d) and zx-plane (e, f) for tungsten and titanium alloy, respectively. Two-dimensional 〈 100 〉 growth occurs in the
xy - (g) and yz -planes (h), respectively, and the crystal orientation is adjusted such that a misorientation becomes smaller at the center of the melt pool in these planes.
Blue lines indicate 〈 100 〉 direction, and blue squares schematically indicate cubic crystal lattice [ 31 ]. (For interpretation of the references to colour in this figure
legend, the reader is referred to the web version of this article.)
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2544

## Page 11

From above analysis, it shows that though reducing materials such as
metals, allotropes of carbon or carbides have been added into W to
decrease the effect of oxygen impurity, cracking could not be eliminated
for W alloys and W-based composites by LPBF. Besides, oxygen content
increased for W-based composites with addition of rare earth oxides
[ 114 ]. Though cracking still existed, their mechanical properties
increased, which indicates that precipitation of oxygen impurities at
grain boundaries is not the whole reason for cracking generation. The
reason may be because that there is still solid-state cracking especially
ductility-dip cracking. Summary of different powder and process pa-
rameters optimized for LPBF of W and W-based materials with parts ’
density is listed in Table 1 . The relationship of compressive strength and
strain of current LPBF of W and W-based materials is shown in Fig. 16 .
7. Potential strategies for crack-free W
The above summary shows that with optimization of the related
composition and process parameters, density of W and W-based mate-
rials both is over 99 %. However, there is still cracking in as-built parts.
According to the forming mechanism of cracking, methods help to
eliminate hot cracking and solid-state cracking work. The potential
strategies are as follows:
7.1. Structure design
As an intelligent manufacturing technique, AM can form complex
structures once designed, which embodies designers ’ high degree of
freedom. With pre-simulation of distribution of temperature and stress
fields in printed materials and structure, optimization of structure can be
designed to reduce residual stress and chance of failure [ 117 , 118 ]. Be-
sides, peculiar designed motif/structure different from conventional
structure/mode can improve mechanical and physical properties
[ 119 , 120 ]. Also architected materials learned from crystal-inspired
microstructure, physical metallurgical concepts, bioinspired nano-
composites and artificial intelligence design enable the desired proper-
ties [ 31 , 121 – 123 ].
7.2. Composition optimization
One issue for defects in LPBF of W is the high temperature gradient.
Fig. 12. Pure tungsten parts by LPBF: (a) thin-wall [ 55 ], (b) honey-comb and Cu infiltrated (c) [ 87 ], (d) collimator [ 88 ], (e) disk [ 92 ], (f) collimator with microhole
[ 93 ], (g) thin-wall [ 94 ], (h) grids [ 97 ] and (i) gear [ 47 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2545

## Page 12

W alloys and W-based composites both can reduce solidification
cracking, however, there is still ductility-dip cracking in LPBF of W and
W-based materials. The mechanism for ductility-dip cracking is still in
debate and the metallurgical factors that to reduce solidification
cracking may increase susceptibility to ductility-dip cracking [ 78 ].
Therefore the mechanisms of cracking elimination and composition
optimization need further study especially those on atomic level. Fluxes
can reduce melting temperature, viscosity and thermal stress, which
benefit to obtain high quality as-built W [ 124 ]. At the same time, con-
solidant may be good option to heal existed cracking by capillary force
during LPBF. Thermodynamics-guided and machine learning enable
alloy design more successfully with desired microstructures, size and
properties [ 125 , 126 ]. New methods for powder preparation such as
liquid-phase mixing and core-shell-structured powder (low melting
point materials outside W core helps to reduce absorbed laser energy)
may reduce impurities from the normal mechanical mixing.
7.3. Hybrid AM methods
Cracking is easy to appear when residual tensile stress is over ma-
terials ’ ultimate tensile strength. Hybrid AM methods with other energy
sources such as magnetic [ 127 ], acoustic [ 128 ], thermal [ 87 , 129 ], me-
chanical [ 130 ], electric [ 131 ], plasma(optical) fields [ 132 ] and multi-
filed coupling assisted AM [ 133 ]could refine grains and reduce micro
cracking [ 134 ]. The in-situ micro-casting and in-situ laser shock peening
(3D LSP or hybrid AM) can heal micro cracking during printing
[ 135 , 136 ]. The single layer effect of W with 3D-LSP is shown in Fig. 17 .
3D LSP is beneficial to eliminate cracking real-time and improve mate-
rials ’ fatigue, corrosion and friction properties by introducing
compressive residual stress, nano twins and nano grains [ 137 ].
7.4. Grain boundary engineering
Grain boundary engineering can design and adjust grain boundary,
which includes the composition, amount and types of grain boundary.
Fig. 13. Schematic diagram of nanopore formation: (a) pure W; (b) W-5Nb [ 104 ].
Fig. 14. Mechanical properties of LPBF W and W-La
2
O
3
: (a) Compressive stress-strain curves, (b) Vickers hardness [ 114 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2546

## Page 13

Solute atoms can segregate and deplete on grain boundary with change
of temperature, stress and irradiation, which affect mechanical proper-
ties greatly. Besides, the amount (addition or depletion) and types (small
angle, large angle and special grain boundaries) of grain boundary can
also be changed with these effects. At the same time, voids and impu-
rities also can react with grain boundary and change mechanical prop-
erties much [ 138 ]. A certain elements can promote effect of grain
boundary engineering for some materials and can accomplish with
composition optimization [ 98 ].
7.5. Defect engineering
Low ductility is another issue for W and increase ductility of W is
highly desired for its application and the whole refractory metal com-
munity. Defects include point (void, interstitial and substituted atoms),
line (edge and screw dislocations, dislocation loops) and planar faults
(grain boundary, phase boundary, twin grain boundary and stacking
fault energy), which all have important role in mechanical properties by
motion and interaction [ 139 – 142 ]. Materials with twins (nanotwins)
usually have both high strength and large ductility. Structure/chemical
order proved to work by tuning stacking fault energy to improve creep
resistance, phase stability and mechanical properties [ 143 ]. Nano pores
can improve materials ’ ductility by addition of volatile materials. Mul-
tiscale, hierarchical architecture can enhance the strength, ductility, and
radiation-damage tolerance [ 144 ]. Besides, anomalous slip in body-
centered cubic metals takes place at low temperature [ 145 ].
7.6. Metastability engineering
Structure/chemical order proved to work by tuning stacking fault
energy for high entropy alloys and simple alloys with such order can also
improve creep resistance, phase stability and mechanical properties
[ 146 , 147 ].Materials with dual phases usually have good mechanical
properties than those with single phase or with hierarchical micro-
structures. Therefore combination of different phases such as hard and
soft phases (brick-and-mortar structure) can help to improve ductility.
Phase transformation induced plasticity and twin induced plasticity are
also potential to obtain crack-free as-built parts [ 148 , 149 ]. Phase
transformation can happen with change of composition, temperature
and stress such as fs laser processing and composition optimization.
7.7. Post treatment
For the indelible cracking by above potential strategies, post treat-
ment is a good choice. Usually HIP is used for post heat-treatment of as-
built W parts since long time annealing can increase grain size. Post
treatment includes surface treatment, which can improve fracture
property by improving surface quality [ 150 ]. Post treatment for bulk is
different from hybrid AM, which is in-situ methods for AM. Heating and
aging at a certain temperature, introducing stress into samples such as
electro-assisted micro-forging [ 151 ] and high-energy particles irradia-
tion may bring phase transformation, eliminate grain boundary, reduce
accumulation of elements/phases or voids and heal or self-heal cracking
at last [ 152 , 153 ].
There are other AM methods with high energy beam to form W parts
like electron beam powder bed fusion, laser direct energy deposition and
wire arc AM [ 9 ]. Still there are other new AM methods to form W at
room temperature, like extrusion printing, binder printing and electro-
chemical method, which do not introduce thermal stress [ 154 – 156 ].
Besides, high entropy alloys have good strength and ductility after
composition/structure optimization, among which W high entropy al-
loys have potential application for fusion reactor materials [ 157 ].
However, they are beyond this topic and will not be illustrated here. The
current issues for LPBF of W and different strategies based on every
influence factor to improve quality are shown in Fig. 18 .
8. Conclusions
There is micro cracking in LPBF of W due to high temperature
gradient and rapid cooling rate during printing and its inherent
Fig. 15. Scan track morphology for W-REO using P = 250 W, v = 400 mm/s. (a) Without preheating, cracks run perpendicular to the scan track. (b) Using 773 K
preheating, the melt pool is wider and cracks are eliminated. (c) Cracks run perpendicular across all scan vectors, in a zigzag pattern obeying the local grain boundary
orientations. (d) Some cracks are still present, though shorter and with a smaller opening [ 116 ].
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2547

## Page 14

Table 1
Powder parameter, process parameters and density for LPBF of W and W-based materials.
Powder shape/
Average size
or D50
Machine/
Laser power
Laser beam
size/type/
/wavelength
Scanning
speed/
Point
distance
exposure
time
Hatch
space
( μ m)
Layer
thickness/
Atmosphere/
Oxygen
content
Scanning
strategy
Substrate
material
/temperature
Optical Ev
(E
L
)/
Composition
Density Author
Ref.
Spherical
14.8 μ m
SLM 125
200 W
100 μ m
200 mm/
s
100
30 μ m
Ar
Zig-zag
67
◦
rotation
316 L
stainless steel
200
◦
C
333 J/mm
3
98.7 % C. Wang [ 16 ]
Irregular
30 μ m
Concept
laser (Mlab
curing R)
90 W
CW fiber
200 mm/
s
15 30 μ m
​
Steel 1000 J/mm
3
75 %
R. K. Enneti
[ 23 ]
Polyhedron
32 μ m
EOSINT
M280
300 W
100 μ m
1070 nm
300 mm/
s
70
30 μ m
Ar
< 1000 ppm
​ ​
476.2 J/
mm
3
96.4 %
R.K. Enneti
[ 24 ]
Spherical
28 μ m
Renishaw
AM 400
400 W
75 μ m
75 μ m
200 μ s
100
30 μ m
Ar
< 100 ppm
Zig-zag
67
◦
rotation
Steel
355.6 J/
mm
3
96 % –
96.5 %
D. Wang
[ 25 , 80 , 81 ]
Spherical
35.6 μ m
Farsoon
FS271M
475 W
​
600 mm/
s
90
30 μ m
N
2
< 40 ppm
Zig-zag
67
◦
rotation
​
293 J/mm
3
96.9 % X. Zi [ 27 ]
Spherical
22.7 μ m
300 W
​
400 mm/
s
80
30 μ m
Ar
Zig-zag
67
◦
rotation
316 L
stainless steel
180
◦
C
313 J/mm
3
95.65 % W. Du [ 28 ]
Spherical
27.4 μ m
EOS M290
360 W
​
800 mm/
s
40
20 μ m
Ar
< 500 ppm
Bidirectional
90
◦
rotation
200
◦
C
562.5 J/
mm
3
99.1 % T. Todo [ 31 ]
Spherical
Renishaw
AM125
200 W
43 μ m
1070 nm
20 μ m
200 μ s
115
50 μ m
Ar
< 1800 ppm
Meander
67
◦
rotation
Pure Ti 348 J/mm
3
98 %
A.T. Sidambe
[ 40 , 93 ]
​ ​ 750 fs
1030 nm
​ ​ ​ ​
Tungsten
​
99 % S. Bai [ 48 ]
Spherical
15.87 μ m
SLM 280HL
300 W
​
400 mm/
s
80
30 μ m
Ar
< 300 ppm
Zig-zag
67
◦
rotation
316 L
stainless steel
150
◦
C
312.5 J/
mm
3
98.31 % J. Li [ 49 ]
Spherical
15 – 45 μ m
Renishaw
AM 400
400 W
70 μ m
pulse mode
1070 nm
300 μ s 100
50 μ m
Ar
< 200 ppm
67
◦
rotation Stainless steel 40 J/mm
2
92.5 % J. Huang [ 50 ]
polygonal
75 μ m
HRPM-IV
SLM
200 W
CW/modulated
fiber laser
1095 nm
25 mm/s 50
50 μ m
Ar
​ ​
3200 J/mm
3
82 % D. Zhang [ 51 ]
Spherical
~ 17.3 μ m
Self-
developed
70 μ m
​
50
80 μ m
Ar
​ 304 L
stainless steel
200
◦
C
< 1.5 J/mm
​
M. Guo [ 52 ]
Spherical
14.41 μ m
Self-
developed
300 W
70 μ m
Fiber laser
300 mm/
s
50
20 μ m
Ar
< 100 ppm
Chessboard
67
◦
rotation
Stainless steel
200
◦
C
1000 J/mm
3
98.4 %
M. Guo [ 53 ]
D. Gu [ 62 ]
Spherical
5 – 25 μ m
SLM solution
125HL
300 W
70 μ m
300 mm/
s
~ 104
30 μ m
Ar
Stripe scan
67
◦
rotation
316 L
stainless steel
200
◦
C
322 J/mm
3
98.51 % X. Ren [ 54 ]
17 ± 5 μ m
EOS M290
200 W
100 μ m
300 mm/
s
​ 20 μ m
Ar
< 1000 ppm
Zig-zag
67
◦
rotation
50
◦
C 0.667 J/mm 98.50 % C. Tan [ 55 ]
Spherical
14.8 μ m
SLM 125
200 W
Nd:YAG laser
200 mm/
s
100
30 μ m
Ar
< 200 ppm
Zig-zag
67
◦
rotation
200
◦
C 333 J/mm
3
98.71 % S. Wen [ 56 ]
Spherical
15.8 μ m
EOS M290
300 W 100 μ m
400 mm/
s
20 μ m
Ar
< 1000 ppm
67
◦
rotation 180
◦
C
​
98.1 %
Z. Xiong [ 58 ]
150 W Remelting 98.4 %
Spherical
TEKMAT
W25
EOS M100
170 W
40 μ m
1064 nm
600 mm/
s
40
20 μ m
Ar
1000 ppm
Bidirectional
67
◦
rotation
80
◦
C
354.2 J/
mm
3
99.6 %
P. Rebesan
[ 59 ]
Spherical
5 – 25 μ m
Customized
Nd:YAG
fiber laser
​
100
30 μ m
Ar
< 20 ppm
67
◦
rotation 1000
◦
C
​
97.5 % J. Braun [ 63 ]
Spherical
self-
developed
90 μ m
1064 nm
Ar
150 – 200 ppm
Bidirectional
400
◦
C 475 J/mm
3
94.4 %
A. Ivekovi ´c
[ 64 ]ProX
DMP320
​
< 50 ppm
​
> 200 J/mm
3
97.1 %
Non-spherical
11.5 μ m
Farsoon
271 M
450 W
130 μ m
1070 nm
400 mm/
s
70
30 μ m
N
2
Ar
< 1000 ppm
​
Stainless steel
100
◦
C
535.7 J/
mm
3
97.05 %
95.46 %
J. Dong [ 66 ]
( continued on next page )
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2548

## Page 15

Table 1 ( continued )
Powder shape/
Average size
or D50
Machine/
Laser power
Laser beam
size/type/
/wavelength
Scanning
speed/
Point
distance
exposure
time
Hatch
space
( μ m)
Layer
thickness/
Atmosphere/
Oxygen
content
Scanning
strategy
Substrate
material
/temperature
Optical Ev
(E
L
)/
Composition
Density Author
Ref.
Polyhedron
42 μ m
FS271M
300 W
68 – 90 μ m
1070 nm
200 mm/
s
240
30 μ m
Ar
​
100
◦
C 208 J/mm
3
95.7 % M. Zhang [ 67 ]
Polyhedron
26.5 μ m
EOSINT
M280
370 W
100 μ m
1070 nm
500 mm/
s
90
`
20 μ m
Ar
< 1000 ppm
Zig-zag
67
◦
rotation
Carbon steel
35
◦
C
411 J/mm
3
98.58 %
T. Yamamoto
[ 68 ]
Spherical
32 μ m
SLM 125HL
400 W
80 μ m
fiber laser
300 mm/
s
100
30 μ m
Ar
< 500 ppm
zig-zag
67
◦
rotation
Tungsten
444.4 J/
mm
3
~ 97 % J. Chen [ 69 ]
Spherical
22.7 μ m
EOS M290
350 W
​
400 mm/
s
80
30 μ m
Ar
HIP
Parallel
scanning
67
◦
rotation
Stainless steel
180
◦
C
364.58 J/
mm
3
HIP at 1600
◦
C
95.91 %
98.97 %
Q. Shi [ 70 ]
Non-spherical
19.4 μ m
Renishaw
AM 250
200 W
75 μ m
fiber laser
1071 nm
167 mm/
s
50 μ m
300 μ s
90
Ar
< 600 ppm
Meander
67
◦
rotation
​
Remelting 82.9 % X. Zhou [ 73 ]
Spherical
15 – 45 μ m
AconityONE
400 W
100 μ m
fiber laser
1075 nm
510 mm/
s
80
40 μ m
Ar
90
◦
alternating
bidirection
Tungsten
1000
◦
C
245 J/mm
3
98 %
A. v. Müller
[ 87 ]
35 μ m
​ ​ ​ ​ ​ ​ ​ ​
89.92 %
J. Deprez
[ 90 , 91 ]
​
EOS M280
370 W
80 μ m
​ ​ 30 μ m
Ar
< 100 ppm
​ ​ ​
80 % J.I. Gear [ 92 ]
Spherical
16.76 μ m
EOS M290 100 μ m
​
50
20 μ m
Ar
< 1000 ppm
Zigzag
90
◦
rotation
50
◦
C 0.4 J/mm 95.13 % F. Wu [ 94 , 96 ]
Spherical
15 – 30 μ m
YLM-120
300 W
​
300 mm/
s
60
30 μ m
Ar
< 1000 ppm
​ ​ 1000 J/m
555.6 J/
mm
3
84.5 % X. Shi [ 95 ]
Not fully
spherical
17.8 μ m
EOS M280
250 W
100 μ m
1060 – 1100 nm
200 mm/
s
​ 30 μ m
Ar
< 1 %
​
80
◦
C 1.25 J/mm
​
Y.-J. Xie [ 97 ]
Spherical
33 μ m
Aconity MIDI
900 W
80 μ m
1070 nm
500 mm/
s
60
50 μ m
Ar
< 10 ppm
Stripe
scanning
90
◦
rotation
Tungsten
600
◦
C
600 J/mm
3
99.2 %
S. Sharma
[ 158 ]
Spherical
31 μ m
Renishaw
AM400
400 W
70 μ m
​
50
30 μ m
Ar
N
2
< 300 ppm
Bidirectional
67
◦
rotation
Tungsten
​
98 %
99 %
T.
Ramakrishnan
[ 159 ]
W-based materials
Spherical W
Ta
Self-
developed
90 μ m
1064 nm
Ar
150 – 200 ppm
Bidirectional 400
◦
C
475 J/mm
3
W-5wt%Ta
W-10wt%Ta
94.1 %
97.5 % A. Ivekovi ´c
[ 64 ]
ProX
DMP320
​
< 50 ppm
​ ​ > 200 J/mm
3
W-5wt%Ta
W-10wt%Ta
98.7 %
98.4 %
Polyhedron
19 μ m W
14 μ m (Re)
EOSINT
M280
370 W
100 μ m
1070 nm
500 mm/
s
90
`
20 μ m
Ar
< 1000 ppm
67
◦
rotation Carbon steel
411 J/mm
3
W
W-1%Re
W-3%Re
W-10%Re
98.5 %
98.1 %
98.5 %
98.8 %
T. Yamamoto
[ 99 ]
Spherical
11.75 μ m W
20 μ m (Re)
Concept
laser (Mlab
curing 200R)
200 W
50 μ m
1080 nm
200 mm/
s
50
15 μ m
Ar
< 1000 ppm
Meander
90
◦
rotation
​
1333 J/mm
3
W
W-5%Re
95 %
97.4 %
C.C. Eckley
[ 100 ]
Polyhedral W
spongy Ta
Renishaw
AM400
400 W
​
75 μ m
70 μ s
100
Ar
< 100 ppm
Meander
67
◦
rotation
​
W-6Ta%
​
K. Li [ 102 ]
Spherical W
15 – 45 μ m
0.3 – 2 μ m
(Ta)
SLM 280 HL
​ ​ ​
30 μ m
Ar
< 0.04 wt%
67
◦
rotation
Stainless steel
150
◦
C
714.29 J/
mm
3
W-3Ta%
95.79 % J. Li [ 103 ]
Spherical W
5 – 25 μ m
1 – 10 μ m
(Nb)
EOS
M280
​ ​ ​
30 μ m
Ar
< 100 ppm
Zig-zag
90
◦
rotation
200
◦
C
397 J/mm
3
W-5Nb
98 % J. Xue [ 104 ]
Polyhedral
32 μ m W
spongy
18 μ m (Ta)
SLM 280
400 W
​
500 mm/
s
100 Ar
Meander
67
◦
rotation
​
W-6Ta
​
K. Li [ 105 ]
( continued on next page )
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2549

## Page 16

Table 1 ( continued )
Powder shape/
Average size
or D50
Machine/
Laser power
Laser beam
size/type/
/wavelength
Scanning
speed/
Point
distance
exposure
time
Hatch
space
( μ m)
Layer
thickness/
Atmosphere/
Oxygen
content
Scanning
strategy
Substrate
material
/temperature
Optical Ev
(E
L
)/
Composition
Density Author
Ref.
Spherical W
5 – 25 μ m
nano Ni, Fe
Self-
developed
400 W
70 μ m
500 mm/
s
50 30 μ m
Zigzag
67
◦
rotation
​ 533.3 J/
mm
3
W-1%Ni-1%
Fe
​
M. Guo [ 106 ]
Spherical W
14.52 μ m
15.85 μ m
(Ti)
Self-
developed
350 W
70 μ m
275 mm/
s
50
30 μ m
Ar
Chessboard
67
◦
rotation
​
848 J/mm
3
W-6Ti
99.1 % K Liu [ 107 ]
7 μ m W
50 nm (TiC)
Self-
developed
160 W
70 μ m
100 mm/
s
50
25 μ m
Ar
< 10 ppm
​ ​ 1280 J/
mm
3
W-
2.5 %TiC
97.8 % D. Gu [ 108 ]
Spherical W
5 – 25 μ m
spongy
5 μ m (TaC)
SLM 280
2.0
400 W
80 – 115 μ m
1070 nm
300 mm/
s
130
20 μ m
Ar
< 500 ppm
Meander
67
◦
rotation
Stainless steel
512.8 J/
mm
3
W-5%
TaC
​
J. Chen
[ 109 , 110 ]
Polyhedral
32 μ m W
ZrC (50 nm)
Renishaw
AM 400
​ ​ ​
Ar
< 100 ppm
Zigzag
67
◦
rotation
Tungsten W-0.5 %ZrC
​
K. Li [ 111 ]
Spherical W
14.8 μ m
ZrC (50 nm)
SLM 125
200 W
​
200 mm/
s
100
30 μ m
Ar
< 200 ppm
Zigzag
67
◦
rotation
Steel
200
◦
C
333.3 J/
mm
3
W-
0.5 %ZrC
​
Y. Zhou [ 112 ]
Spherical W
15 – 45 μ m
Spherical
15 – 53 μ m
(Y
2
O
3
)
50 nm
(Y
2
O
3
)
Renishaw
AM 400
70 μ m
​ ​
Ar
< 0.1 vol%
Zigzag
67
◦
rotation
180
◦
C
W
W-1%Y
2
O
3
98.3 % Z. Hu [ 113 ]
Spherical
5 – 25 μ m
Irregular
50 nm
(La
2
O
3
)
Self-
developed
300 W
​
200 mm/
s
150
25 μ m
Ar
Zigzag
67
◦
rotation
Steel
400 J/
mm
3
W-2%
La
2
O
3
​
S. Wei [ 114 ]
Fig. 16. The compressive strength and strain for LPBF of W and W-based materials.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2550

## Page 17

properties like brittleness, hardness, high DBTT and oxyphilic. The
volatilization of WO
3
generated nano pores, which aggregated and
separated near grain boundaries and caused micro cracking, too. There
are still reports that density of LPBF of W has been improved over 99 %
and even reached 99.2 %, which solved the low density issue that
perplexed the whole AM field [ 158 , 159 ]. But the micro cracking still
could not be eliminated and the following is conclusion that could be
referred and deeply researched in the future:
1) The optimized E
V
for the densest LPBF of W differed a lot and it may
be because of different printers and process parameters. However Ev
cannot depict the complex dynamics of molten pool, therefore there
is limitation to be used for design of process parameters. Numerical
simulation, machine learning and quality monitor should work
synergistically for high quality W parts.
2) Though micro cracking for W-based materials can be decreased, they
could not be eliminated and the maximal density for LPBF of W-
based materials is less than that of pure W. It may be because that
though the added phases can reduce solidification cracking, there is
still ductility-dip cracking during LPBF of W.
3) Powder property has decisive effect on the final quality of printed
parts. New methods to obtain more homogeneous composites are to
be developed such as liquid phase method. The customized powder
with special composition, size distribution, and special structure is
beneficial to improve quality of as-built W parts. W high entropy
alloys may have superior quality and properties in future.
4) It is difficult to completely eliminate cracking inside as-built W parts,
and those with the best compressive mechanical properties are not
usually the ones with the highest density. Therefore it is crucial to
choose suitable process parameters for printing according to prac-
tical application and make sure if there should not have defects like
micro cracking or pores. Therefore, determining the amount, size,
shape and effect of defects with nondestructive testing such as X-CT
or neutron radiation is significant for application as well.
In all, in order to reduce defects and improve quality of LPBF of W,
structure design, composition optimization, new hybrid AM methods,
improve ductility by various methods and post treatment are important.
At the same time, it is significant to make sure application scenarios in
order to choose suitable process parameters. Besides, new printing
methods without high energy beams may be tried for high quality as-
Fig. 17. Single layer W before (a) and after (b) 3D LSP.
Fig. 18. Strategies to improve the quality of LPBF of W.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2551

## Page 18

built W parts especially with complex structures.
CRediT authorship contribution statement
Lina Ji: Writing – review & editing, Writing – original draft, Inves-
tigation, Funding acquisition, Data curation, Conceptualization. Shenyu
Wei: Software, Methodology, Formal analysis, Data curation, Concep-
tualization. Zeli Wang: Software, Methodology, Formal analysis, Data
curation, Conceptualization. Yuanbin Zhang: Validation, Supervision.
A.V. Radhamani: Writing – review & editing, Formal analysis. Ram-
akrishna Seeram: Writing – review & editing, Formal analysis.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
Acknowledgement
This work was financially supported by Young Scholar A of West
China, Chinese Academy of Sciences and Chongqing Commission of
Science and Technology (No. cstc2020jscx-msxmX0205).
References
[1] Luo K, Yang Y, Liang X, Ma J, Wang J. Preparation of tungsten matrices of
dispenser cathodes by selective laser melting. In: 2020 IEEE 21ST international
conference on vacuum electronics (IVEC). New York: IEEE; 2020. p. 87–8.
[2] Sugiyama K, Mayer M, Rohde V, Balden M, Durbeck Th, Herrmann A, et al.
Deuterium inventory in the full-tungsten divertor of ASDEX upgrade. Nucl.
Fusion 2010;50:035001.
[3] You JH, Bachmann C, Belardi VG, Binder M, Bowden D, Calabro G, et al. Limiters
for DEMO wall protection: initial design concepts & technology options. Fusion
Eng Des 2022;174:112988.
[4] Ren C, Fang ZZ, Koopman M, Butler B, Paramore J, Middlemas S. Methods for
improving ductility of tungsten - a review. Int J Refract Met Hard Mater 2018;75:
170–83.
[5] Yap CY, Chua CK, Dong ZL, Liu ZH, Zhang DQ, Loh LE. Review of selective laser
melting: materials and applications. Appl Phys Rev 2015;2:041101.
[6] Bose S, Ke D, Sahasrabudhe H, Bandyopadhyay A. Additive manufacturing of
biomaterials. Prog. Mater. Sci. 2018;93:45–111.
[7] Riaz RD, Usman M, Ali A, Majid U, Faizan M, Malik UJ. Inclusive characterization
of 3D printed concrete (3DPC) in additive manufacturing: a detailed review.
Construct Build Mater 2023;394:132229.
[8] Hu S, Huan X, Liu Y, Cao S, Wang Z, Kim JT. Recent advances in meniscus-on-
demand three-dimensional micro- and nano-printing for electronics and
photonics. Int J Extreme Manuf 2023;5:032009.
[9] Byron B-M, Gradl P, Snedden G, Brooks M, Pitot J, Lopez E, et al. Metal additive
manufacturing in aerospace: a review. Mater Des 2021;209:110008.
[10] Sefene EM. State-of-the-art of selective laser melting process: a comprehensive
review. J Manuf Syst 2022;63:250–74.
[11] Morcos P, Elwany A, Karaman I, Arroyave R. Review: additive manufacturing of
pure tungsten and tungsten-based alloys. J Mat Sci 2022;57(21):9769–806.
[12] Talignani A, Seede R, Whitt A, Zheng S, Ye J, Karaman I, et al. A review on
additive manufacturing of refractory tungsten and tungsten alloys. Addit Manuf
2022;58:103009.
[13] Pan S-H, Yao G-C, Cui Y-N, Meng F-S, Luo C, Zheng T-Q, et al. Additive
manufacturing of tungsten, tungsten-based alloys, and tungsten matrix
composites. Tungsten 2023;5:1–31.
[14] Xiong Z, Zou J, Deng Z, Chen J, Liu W, Fan Y, et al. Integrating thin wall into
block: a new scanning strategy for laser powder bed fusion of dense tungsten.
J Mater. Sci. Technol. 2022;120:167–71.
[15] Li K, Chen J, Zhao C, Shen Z, Liu W. A review of tungsten fabricated via laser
powder bed fusion. Tungsten 2021;3:218–33.
[16] Wang C, Chen D, Zhou Y, Xie Z, Fang Q, Wen S, et al. Microstructures, thermal
and mechanical properties of pure tungsten-a comparison between selective laser
melting and hot rolling. Chin J Mech Eng 2022;35:48.
[17] Bouabbou A, Vaudreuil S. Understanding laser-metal interaction in selective laser
melting additive manufacturing through numerical modeling and simulation: a
review. Virtual Phys Prototyping 2022;17(3):543–62.
[18] Müller AV, Dorow-Gerspach D, Balden M, Binder M, Buschmann B, Curzadd B,
et al. Progress in additive manufacturing of pure tungsten for plasma-facing
component applications. J Nucl Mater 2022;566:153760.
[19] Wright J. Additive manufacturing of tungsten. University of Sheffield; 2020 [Ph.
D. thesis.].
[20] Buschmann B. Influence of powder characteristics and component wall thickness
on material quality when producing pure tungsten by means of laser powder bed
fusion. Technische Universitat Munchen; 2019 [Master’s thesis].
[21] Qi H, Mazumder J, Ki H. Numerical simulation of heat transfer and fluid flow in
coaxial laser cladding process for direct metal deposition. J Appl Phys 2006;100:
024903.
[22] Zhang J, Gu D, Yang Y, Zhang H, Chen H, Dai D, et al. Influence of particle size on
laser absorption and scanning track formation mechanisms of pure tungsten
powder during selective laser melting. Engineering 2019;5:736–45.
[23] Enneti RK, Morgana R, Atre SV. Effect of process parameters on the selective laser
melting (SLM) of tungsten. Int J Refract Met Hard Mater 2018;71:315–9.
[24] Enneti RK, Morgan R, Wolfe T, Harooni A, Volk S. Direct metal laser sintering/
selective laser melting of tungsten powders. Int J Powder Metall 2017;53:23–31.
[25] Wang D, Yu C, Zhou X, Ma J, Liu W, Shen Z. Dense pure tungsten fabricated by
selective laser melting. Appl. Sci. 2017;7:430.
[26] Ji L, Wang C, Wu W, Tan C, Wang G, Duan X. Spheroidization by plasma
processing and characterization of stainless steel powder for 3D printing. Metall
Mater Trans A 2017;48A:4831–41.
[27] Zi X, Chen C, Wang X, Wang P, Zhang X, Zhou K. Spheroidisation of tungsten
powder by radio frequency plasma for selective laser melting. Mater Sci Technol
2018;34(6):735–42.
[28] Du W, Shi Q, Wu A, Liu X, Zhou F. Selective laser melting of tungsten powder
prepared by RF-plasma spheroidization. Rare Met Mater Eng 2021;50(12):
4457–64.
[29] Field AC, Carter LN, Adkins NJE, Attallah MM, Gorley MJ, Strangwood M. The
effect of powder characteristics on build quality of high-purity tungsten produced
via laser powder bed fusion (LPBF). Metall. Mater. Trans. A 2020;51A:1367–78.
[30] Gokcekaya O, Ishimoto T, Todo T, Wang P, Nakano T. Influence of powder
characteristics on densification via crystallographic texture formation: pure
tungsten prepared by laser powder bed fusion. Addi Manuf Lett 2021;1:100016.
[31] Todo T, Ishimoto T, Gokcekaya O, Oh J, Nakano T. Single crystalline-like
crystallographic texture formation of pure tungsten through laser powder bed
fusion. Scripta Mater 2022;206:114252.
[32] Zhang D, Qiu D, Gibson MA, Zheng Y, Fraser HL, StJohn DH, et al. Additive
manufacturing of ultrafine-grained high-strength titanium alloys. Nature 2019;
576:91–5.
[33] Zhou W, Tian Y, Tan Q, Qiao S, Luo H, Zhu G, et al. Effect of carbon content on
the microstructure, tensile properties and cracking susceptibility of IN738
superalloy processed by laser powder bed fusion. Addit Manuf 2022;58:103016.
[34] Sanchez S, Smith P, Xu Z, Gaspard G, Hyde CJ, Wits WW, et al. Powder bed fusion
of nickel-based superalloys: a review. Int J Mach Tool Manuf 2021;165:103729.
[35] Kusoglu IM, Gokce B, Barcikowski S. Research trends in laser powder bed fusion
of Al alloys within the last decade. Addit Manuf 2022;36:103016.
[36] Wu Y. Manufacturing of tungsten and tungsten composites for fusion application
via different routes. Tungsten 2019;1:80–90.
[37] Ma XL, Zhang XX, Wang T, Gao Y, Yuan Y, Cheng L, et al. Decreased surface
blistering and deuterium retention in potassium-doped tungsten exposed to
deuterium plasma following ion irradiation. Nucl Fusion 2023;63:026013.
[38] Shi R, Khairallah SA, Roehling TT, Heo TW, McKeown JT, Matthews MJ.
Microstructural control in metal laser powder bed fusion additive manufacturing
using laser beam shaping strategy. Acta Mater 2020;184:284–305.
[39] Vrancken B, Ganeriwala RK, Matthews MJ. Analysis of laser-induced
microcracking in tungsten under additive manufacturing conditions: experiment
and simulation. Acta Mater 2020;194:464–72.
[40] Sidambe AT, Tian Y, Prangnell PB, Fox P. Effect of processing parameters on the
densification, microstructure and crystallographic texture during the laser
powder bed fusion of pure tungsten. Int J Refract Met Hard Mater 2019;78:
254–63.
[41] Demir AG, Colombo P, Previtali B. From pulsed to continuous wave emission in
SLM with contemporary fiber laser sources: effect of temporal and spatial pulse
overlap in part quality. Int J Adv Manuf Tech 2017;91:2701–14.
[42] Caprio L, Demir AG, Previtali B. Influence of pulsed and continuous wave
emission on melting efficiency in selective laser melting. J Mater Process Tech
2019;266:429–41.
[43] Guo C, Zhou Y, Li X, Hu X, Xu Z, Dong E, et al. A comparing study of defect
generation in IN738LC superalloy fabricated by laser powder bed fusion:
continuous-wave mode versus pulsed-wave mode. J Mater. Sci. Technol. 2021;90:
45–57.
[44] Mantel N, Bowden D, Herashchenko SS, Fursdon M, Hancock ADL, Garkusha IE,
et al. Development and testing of an additively manufactured lattice for DEMO
limiters. Nucl. Fusion 2022;62:036017.
[45] Saunders J, Elbestawi M, Fang Q. Ultrafast laser additive manufacturing: a
review. J Manuf Mater Process 2023;7:89.
[46] Nie B, Yang L, Huang H, Bai S, Wan P, Liu J. Femtosecond laser additive
manufacturing of iron and tungsten parts. Appl. Phys. A 2015;119:1075–80.
[47] Nie B, Huang H, Bai S, Liu J. Femtosecond laser melting and resolidifying of high-
temperature powder materials. Appl Phys A 2015;118:37–41.
[48] Bai S, Liu J, Yang P, Zhai M, Huang H, Yang L-M. Femtosecond fiber laser additive
manufacturing of tungsten. Proc of SPIE 2016;9738 [97380U-1].
[49] Li J, Wu Y, Zhou B, Wei Z. Laser powder bed fusion of pure tungsten: effects of
process parameters on morphology. Densification, Microstructure, Materials
2021;14:165.
[50] Huang J, Li M, Wang J, Pei Z, Mclntyre P, Ma C. Selective laser melting of
tungsten: effects of hatch distance and point distance on pore formation. J Manuf
Process 2021;61:296–302.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2552

## Page 19

[51] Zhang D, Cai Q, Liu J. Formation of nanocrystalline tungsten by selective laser
melting of tungsten powder. Mater Manuf Process 2012;27(12):1267 – 70 .
[52] Guo M, Gu D, Xi L, Du L, Zhang H, Zhang J. Formation of scanning tracks during
selective laser melting (SLM) of pure tungsten powder: morphology, geometric
features and forming mechanisms. Inter. J Refract. Metal. Hard Mater. 2019;79:
37 – 46 .
[53] Guo M, Gu D, Xi L, Zhang H, Zhang J, Yang J, et al. Selective laser melting
additive manufacturing of pure tungsten: role of volumetric energy density on
densification, microstructure and mechanical properties. Inter. J Refract. Metal.
Hard Mater. 2019;84:105025 .
[54] Ren X, Liu H, Lu F, Huang L, Yi X. Effects of processing parameters on the
densification, microstructure and mechanical properties of pure tungsten
fabricated by optimized selective laser melting: from single and multiple scan
tracks to bulk parts. Inter J Refract Metal Hard Mater 2021;96:105490 .
[55] Tan C, Zhou K, Ma W, Attard B, Zhang P, Kuang T. Selective laser melting of high-
performance pure tungsten: parameter design, densification behavior and
mechanical properties. Sci Technol Adv Mat 2018;19(1):370 – 80 .
[56] Wen S, Wang C, Zhou Y, Duan L, Wei Q, Yang S, et al. High-density tungsten
fabricated by selective laser melting: densification, microstructure, mechanical
and thermal performance. Opt. Laser Technol. 2019;116:128 – 38 .
[57] Ji L, Wang S, Wang C, Zhang Y. Effect of hatch space on morphology and tensile
property of laser powder bed fusion of Ti6Al4V. Opt Laser Technol 2022;150:
107929 .
[58] Xiong Z, Zhang P, Tan C, Dong D, Ma W, Yu K. Selective laser melting and
remelting of pure tungsten. Adv Eng Mater 2020;22:1901352 .
[59] Rebesan P, Bonesso M, Gennari C, Dima R, Pepato A, Vedani M. Tungsten
fabricated by laser powder bed fusion. Berg Huettenmaenn Monatsh 2021;166(5):
263 – 9 .
[60] Bertoli US, Wolfer AJ, Matthews MJ, Delplanque J-PR, Schoenung JM. On the
limitations of volumetric energy density as a design parameter for selective laser
melting. Mater Design 2017;113:331 – 40 .
[61] Parry L, Ashcroft IA, Wildman RD. Understanding the effect of laser scan strategy
on residual stress in selective laser melting through thermo-mechanical
simulation. Addit Manuf 2016;12:1 – 15 .
[62] Gu D, Guo M, Zhang H, Sun Y, Wang R, Zhang L. Effects of laser scanning
strategies on selective laser melting of pure tungsten. Int J Extrem Manuf 2020;2:
025001 .
[63] Braun J, Kaserer L, Stajkovic J, Leitz K-H, Tabernig B, Singer P, et al.
Molybdenum and tungsten manufactured by selective laser melting: analysis of
defect structure and solidification mechanisms. Int J Refract Met Hard Mater
2019;84:104999 .
[64] Ivekovi ´c A, Omidvari N, Vrancken B, Lietaert K, Thijs L, Vanmeensel K, et al.
Selective laser melting of tungsten and tungsten alloys. Int J Refract Met Hard
Mater 2018;72:27 – 32 .
[65] Kemnitz RA, Eckley CC, Sexton BM, LeSieur AR. Strengthening of additively
manufactured tungsten by use of hydrogen in argon shielding gas. Inter J Refract
Metal Hard Mater 2023;110:105970 .
[66] Dong J, Liu S, Chen H, Li D, Zhang T, Chen C, et al. Effect of atmosphere on the
microstructure and properties of additively manufactured tungsten. Mater Sci
Tech 2020;36(18):1988 – 96 .
[67] Zhang M, Jiang G, Wang P, Jiang J, Wu H. Property study on selective laser
melting of pure tungsten. Rare Metal Mater Eng 2019;48(5):1645 – 50 .
[68] Yamamoto T, Hara M, Hatano Y. Effects of fabrication conditions on the
microstructure, pore characteristics and gas retention of pure tungsten prepared
by laser powder bed fusion. Int J Refract Met Hard Mater 2021;95:105410 .
[69] Chen J, Li K, Wang Y, Xing L, Yu C, Liu H, et al. The effect of hot isostatic pressing
on thermal conductivity of additively manufactured pure tungsten. Int J Refract
Met Hard Mater 2020;87:105135 .
[70] Shi Q, Du W, Qin F, Tan C, Khanlari K, Xie H, et al. Pure tungsten fabricated by
laser powder bed fusion with subsequent hot isostatic pressing: microstructural
evolution, mechanical properties, and thermal conductivity. JMEPEG 2023;32:
10910 – 23 .
[71] Zhou Z, He D, Tan Z, Wang Y, Shao W, Guo X, et al. Grin structure and cracks
behaviors of tungsten with different geometrical shapes and support structure
prepared by laser powder bed fusion. J Manuf. Process. 2022;82:253 – 64 .
[72] Seyam MS, Koshy P, Elbestawi MA. Laser powder bed fusion of unalloyed
tungsten: a review of process, structure and properties relationships. Metals 2022;
12(2):274 .
[73] Zhou X, Liu X, Zhang D, Shen Z, Liu W. Balling phenomena in selective laser
melted tungsten. J Mater Process Tech 2015;222:33 – 42 .
[74] Zhou X, Liu W. Melting and solidifying behavior in single layer selective laser of
pure tungsten powder. Chin J Lasers 2016;43(5):0503006 .
[75] Schiafino S, Sonin AA. Motion and arrest of a molten contact line on a cold
surface: an experimental study. Phys Fluids 1997;9:2217 – 26 .
[76] Tang YT, Panwisawas C, Ghoussoub JN, Gong Y, Clark JWG, Nemeth AAN, et al.
Alloys-by-design: application to new superalloys for additive manufacturing. Acta
Mater 2021;202:417 – 36 .
[77] Fu J, Li H, Song X, Fu MW. Multi-scale defects in powder-based additively
manufactured metals and alloys. J Mater Sci Technol 2022;122:165 – 99 .
[78] Lippold JC. Welding metallurgy and weldability. John Wiley & Sons, Inc.; 2014 .
[79] Hu X, Guo C, Huang Y, Xu Z, Shi Z, Zhou F, et al. Liquid-induced healing of cracks
in nickel-based superalloy fabricated by laser powder bed fusion. Acta Mater
2024;267:119731 .
[80] Wang D-Z, Li K-L, Yu C-F, Ma J, Liu W, Shen Z-J. Cracking behavior in additively
manufactured pure tungsten. Acta Metall. Sin.-Engl. 2019;32:127 – 35 .
[81] Wang D, Wang Z, Li K, Ma J, Liu W, Shen Z. Cracking in laser additively
manufactured W: initiation mechanism and a suppression approach by alloying.
Mater. Design 2019;162:384 – 93 .
[82] Abbas MA, Yan A, Wang Z. Micro-structural characteristics of additively
manufactured pure tungsten. IOP Conf. Series: Earth and Environmental Science
2021;635:012014 .
[83] Estrada-Díaz JA, Elías-Zú ˜niga A, Martínez-Romero O, Olvera-Trejo D. Enhanced
mathematical model for producing highly dense metallic components through
selective laser melting. Materials 2021;14:1571 .
[84] Markl M, Korner C. Multiscale modeling of powder bed – based additive
manufacturing. Annu Rev Mat Res 2016;46:93 – 123 .
[85] Lee J, Park HJ, Chai S, Kim GR, Yong H, Bae SJ, et al. Review on quality control
methods in metal additive manufacturing. Appl Sci 2021;11:1966 .
[86] Raza A, Deen KM, Jaafreh R, Hamad K, Haider A, Haider W. Incorporation of
machine learning in additive manufacturing: a review. Int J Adv Manuf Technol
2022;122(3 – 4):1143 – 66 .
[87] Müller AV, Schlick G, Neu R, Anstatt C, Klimkait T, Lee J, et al. Additive
manufacturing of pure tungsten by means of selective laser beam melting with
substrate preheating temperatures up to 1000
◦
C. Nucl Mater Energy 2019;19:
184 – 8 .
[88] Zhou K, Chen W, Yang Y, Li R, Dong L, Fu Y-Q. Microstructure and mechanical
behavior of porous tungsten skeletons synthesized by selected laser melting. Int J
Refract Met Hard Mater 2022;103:105769 .
[89] Astolfi L, Hutchins DA, Thomas PJ, Watson RL, Nie L, Freear S, et al. Holey-
structured tungsten metamaterials for broadband ultrasonic sub-wavelength
imaging in water. J Acoust Soc Am 2021;150(1):74 – 80 .
[90] Deprez K, Vandenberghe S, Van Audenhaege K, Vaerenbergh JV, Van Holen R.
Rapid additive manufacturing of MR compatible multipinhole collimators with
selective laser melting of tungsten powder. Med Phys 2013;40(1):012501 .
[91] Deprez K, Van Holen R, Van Audenhaege K, Vandenberghe S. Additive
manufacturing of high density tungsten collimators. J Nucl Med 2012;53(1):
2394 .
[92] Gear JI, Taprogge J, White O, Flux GD. Characterisation of the attenuation
properties of 3D-printed tungsten for use in gamma camera collimation. EJNMMI
Phys 2019;6:1 .
[93] Sidambe AT, Judson DS, Colosimo SJ, Fox P. Laser powder bed fusion of a pure
tungsten ultra-fine single pinhole collimator for use in gamma ray detector
characterization. Inter J Refract Metal Hard Mater 2019;84:104998 .
[94] Wu F, Sun Z, Li B, Chen H, Guo S, Zhu Y. Research on pure tungsten thin wall part
fabricated by laser single track scanning via SLM. Rare Metal Mater. Eng. 2020;49
(10):3490 – 7 .
[95] Shi X, Liu X, Ren S, Lu P, Xie Z, Wu M. Selective laser melting fabricated tungsten
with thin-walled structure: role of linear energy density on temperature evolution
and manufacturing quality. Inter J Mater Form 2022;15:2 .
[96] Wu F, Sun Z, Li B, Chen H, Guo S, Zhu Y. Influence of laser energy input on
fabricating pure tungsten thin wall grids by selective laser melting. Mater Res
Express 2019;6:126526 .
[97] Xie Y-J, Yang H-C, Wang X-B, Zhao L, Kuang C-J, Han W. Control of wall
thickness and surface morphology of tungsten thin wall parts by adjusting
selective laser melting parameters. J Iron Steel Res Int 2019;26:182 – 90 .
[98] Wu X, Li X, Zhang Y, Xu Y, Liu W, Xie Z, et al. Recent advances on interface design
and preparation of advanced tungsten materials for plasma facing materials.
J Fusion Eng 2020;39:342 – 54 .
[99] Yamamoto T, Hara M, Hatano Y. Cracking behavior and microstructural,
mechanical and thermal characteristics of tungsten-rhenium binary alloys
fabricated by laser powder bed fusion. Inter. J Refract. Metal. Hard Mater. 2021;
100:105651 .
[100] Eckley CC, Kemnitz RA, Fassio CP, Hartsfield CR, Leonhardt TA. Selective laser
melting of tungsten-rhenium alloys. JOM 2021;73(11):3439 – 50 .
[101] Zhang Y, Yu Y, Yang L, Li Y, Lin F, Tan W. Dispersion of reinforcing micro-
particles in the powder bed fusion additive manufacturing of metal matrix
composites. Acta Mater 2022;235:118086 .
[102] Li K, Ma G, Xing L, Wang Y, Yu C, Chen J, et al. Crack suppression via in-situ
oxidation in additively manufactured W-Ta alloy. Mater Lett 2020;263:127212 .
[103] Li J, Wei Z, Zhou B, Wu Y, Chen S-G, Sun Z. Preparation, microstructure, and
microhardness of selective laser-melted W-3Ta sample. J Mater Res 2020;35(15):
2016 – 24 .
[104] Xue J, Feng Z, Tang J, Tang C, Zhao Z. Selective laser melting additive
manufacturing of tungsten with niobium alloying: microstructure and suppression
mechanism of microcracks. J Alloy Compd 2021;874:159879 .
[105] Li K, Li Y, Chen W, Zhao C, Yuan Y, Cheng L, et al. Effect of Ta addition on the
fuzz formation of additively manufactured W-based materials. Nucl. Fusion 2020;
60:064004 .
[106] Guo M, Liu K, Sun J, Gu D. Laser powder bed fusion of a novel nano-modified
tungsten alloy with refined microstructure and enhanced strength. Mater Sci Eng
A 2022;843:143096 .
[107] Liu K, Gu D, Guo M, Sun J. Effects of processing parameters on densification
behavior, microstructure evolution and mechanical properties of W-Ti alloy
fabricated by laser powder bed fusion. Mater Sci Eng A 2022;829:142177 .
[108] Gu D, Dai D, Chen W, Chen H. Selective laser melting additive manufacturing of
hard-to-process tungsten-based alloy parts with novel crystalline growth
morphology and enhanced performance. J Manuf Sci E-TASME 2016;138:081003 .
[109] Chen J, Zhao C, Li K, Li M, Sun S, Zhang S, et al. Effect of TaC addition on
microstructure and microhardness of additively manufactured tungsten. J Alloy
Compd 2022;897:162978 .
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2553

## Page 20

[110] Chen J, Zhao C, Li K, Shen Z, Liu W. Formability and controlling of cracks in laser
powder bed fusion of tungsten-5wt% tantalum carbide alloys. Chin J Lasers 2021;
48:1502006.
[111] Li K, Wang D, Xing L, Wang Y, Yu C, Chen J, et al. Crack suppression in additively
manufactured tungsten by introducing secondary-phase nanoparticles into the
matrix. Int J Refract Met Hard Mater 2019;79:158–63.
[112] Zhou Y, Che Y-S, Wang C, Liu R, Wen S-F. Selective laser melting high-
performance ZrC-reinforced tungsten composites with tailored microstructure
and suppressed cracking susceptibility. Tungsten 2021;3:72–88.
[113] Hu Z, Zhao Y, Guan K, Wang Z, Ma Z. Pure tungsten and oxide dispersion
strengthened tungsten manufactured by selective laser melting: microstructure
and cracking mechanism. Addit Manuf 2020;36:101579.
[114] Wei S-Y, Ji L-N, Wu W-J, Ma H-L. Selective laser melting of lanthanum oxide-
reinforced tungsten composites: microstructure and mechanical properties.
Tungsten 2022;4:67–78.
[115] L. Ji, S. Wei, W. Wu, H. Ma, Nano-lanthanum oxide reinforced tungsten-based
composite material and preparation method thereof, US Patent. 17/810,171,
2023.
[116] Vrancken B, Ganeriwala RK, Martin AA, Matthews MJ. Microcrack mitigation
during laser scanning of tungsten via preheating and alloying strategies. Addit
Manuf 2021;46:102158.
[117] Sarkar D, Kapil A, Sharma A. Advances in computational modeling for laser
powder bed fusion additive manufacturing: a comprehensive review of finite
element techniques and strategies. Addiv Manuf 2024;85:104157.
[118] Qin E, Li W, Zhou H, Liu C, Wu S, Shi G. Simulation and experimental
investigation on additive manufacturing of highly dense pure tungsten by laser
powder bed fusion. Materials 2024;17:3966.
[119] Wang W, Chen SJ, Chen W, Duan W, Lai JZ, Sagoe-Crentsil K. Damage-tolerant
material design motif derived from asymmetrical rotation. Nat Commun 2022;13:
1289.
[120] Sarvestani HY, Esmail I, Katz Z, Jain S, Sa JH, Backman D, et al. Interlocking
design, programmable laser manufacturing and testing for architectured
ceramics. Sci Rep 2022;12:17330.
[121] Pham M-S, Liu C, Todd I, Lertthanasarn J. Damage-tolerant architected materials
inspired by crystal microstructure. Nature 2019;565:305.
[122] Nepal D, Kang S, Adstedt KM, Kanhaiya K, Bockstaller MR, Brinson LC, et al.
Hierarchically structured bioinspired nanocomposites. Nat Mater 2023;22:18–35.
[123] Kim K, Kim G-H, Kim HG, Kim HJ, Kim N. Customizing the mechanical properties
of additively manufactured metallic meta grain structure with sheet-based gyroid
architecture. Sci Rep 2022;12:19897.
[124] Raabe D, Ponge D, Uggowitzer PJ, Roscher M, Paolantonio M, Liu C, et al. Making
sustainable aluminum by recycling scrap: the science of “dirty” alloys. Prog Mater
Sci 2022;128:100947.
[125] Sun Z, Ma Y, Ponge D, Zaefferer S, Jagle EA, Gault B, et al. Thermodynamics-
guided alloy and process design for additive manufacturing. Nat Commun 2022;
13:4361.
[126] Zhao C, Chung C-C, Jiang S, Noack M, Chen J-H, Manandhar K, et al. Machine-
learning for designing nanoarchitectured materials by dealloying. Commu. Mater.
2022;3:86.
[127] Seidel A, Degener L, Schneider J, Brueckner F, Beyer E, Leyens C. Novel approach
for suppressing of hot cracking via magneto-fluid dynamic modification of the
laser-induced Marangoni convection. Superalloys 2020 2020:972–81.
[128] Ning F, Hu Y, Cong W. Microstructure and mechanical property of TiB reinforced
Ti matrix composites fabricated by ultrasonic vibration-assisted laser engineered
net shaping. Rapid Prototyp J 2019;25(3):581–91.
[129] Roehling JD, Smith WL, Roehling TT, Vrancken B, Guss GM, McKeown JT, et al.
Reducing residual stress by selective large-area diode surface heating during laser
powder bed fusion additive manufacturing. Addit Manuf 2019;28:228–35.
[130] Lv J, Luo K, Lu H, Wang Z, Liu J, Lu J. Achieving high strength and ductility in
selective laser melting Ti-6Al-4V alloy by laser shock peening. 2021.
[131] Huang Y, Cao Y, Qin H. Electric field assisted direct writing and 3D printing of
low-melting alloy. Adv Eng Mater 2022;24(9).
[132] Yoon H, Liu P, Park Y, Choi G, Choi PP, Sohn H. Pulsed laser-assisted additive
manufacturing of Ti-6Al-4V for in-situ grain refinement. Sci Rep 2022;12(1):
22247.
[133] Ma G, Liu X, Song C, Niu F, Wu D. TiCp reinforced Ti6Al4V of follow-up
synchronous electromagnetic induction-laser hybrid directed energy deposition:
microstructure evolution and mechanical properties. Addit Manuf 2022;59.
[134] Tan C, Li R, Su J, Du D, Du Y, Attard B, et al. Review on field assisted metal
additive manufacturing. Inter J Mach Tool Manuf 2023;189:104032.
[135] Chen Q, Wang G, Liang L, Zhang H. Microstructure and mechanical properties of
arc-laser microcasting hybrid additive manufacturing of ZL114A alloy. Hot
Working Process 2023;52:125–9.
[136] Kalentics N, Sohrabi N, Tabasi HG, Griffiths S, Jhabvala J, Leinenbach C, et al.
Healing cracks in selective laser melting by 3D laser shock peening. Addit Manuf
2019;30:100881.
[137] Deng W, Wang C, Lu H, Meng X, Wang Z, Lv J, et al. Progressive developments,
challenges and future trends in laser shock peening of metallic materials and
alloys: a comprehensive review. Int J Mach Tool Manuf 2023;191:104061.
[138] Li C, Chen F, Ge G, Lin J, Sun Z, Fan M, et al. Impact of sub-grain structure on
radiation resistance in additively manufactured 316L stainless steels: an atomic
insight into the mechanism. Appl Sur Sci 2022;606:154926.
[139] Cui Y, Li K, Wang C, Liu W. Dislocation evolution during additive manufacturing
of tungsten. Model Simul Mater Sci Eng 2022;30:024001.
[140] Kraych A, Clouet E, Dezerald L, Ventelon L, Willaime F, Rodney D. Non-glide
effects and dislocation core fields in BCC metals. NPJ Compu. Mater. 2019:109.
[141] Li Z, Zhang Y, Zhang Z, Cui Y, Guo Q, Liu P, et al. A nanodispersion-in-nanograins
strategy for ultra-strong, ductile and stable metal nanocomposites. Nat Commu
2022;13:5581.
[142] Niu P, Li R, Gan K, Fan Z, Yuan T, Han C. Manipulating stacking fault energy to
achieve crack inhibition and superior strength-ductility synergy in an additively
manufactured high-entropy alloy. Adv Mater 2024;36:2310160.
[143] Bao S, Guo XW, Wang ZL, Zhao Q, Liu YL, Meng FS, et al. Short range ordering
improves elastic properties of Mo additive W-Re solid solution: a first principles
investigation. Scrip Mater 2023;224:115132.
[144] Zhao S, Zhang R, Yu Q, Ell J, Ritchie RO, Minor AM. Cryoforged nanotwinned
titanium with ultrahigh strength and ductility. Science 2021;373:1363–8.
[145] Caillard D, Bienvenu B, Clouet E. Anomalous slip in body-centred cubic metals.
Nature 2022;609:936–41.
[146] Lei Z, Liu X, Wu Y, Wang H, Jiang S, Wang S, et al. Enhanced strength and
ductility in a high-entropy alloy via ordered oxygen complexesvol. 563; 2018.
p. 546.
[147] Neeraj T, Mills MJ. Short-range order (SRO) and its effect on the primary creep
behavior of a Ti-6wt%Al alloy. Mater Sci Eng A 2001;319-321:415–9.
[148] Huang H, Wu Y, He J, Wang H, Liu X, An K, et al. Phase-transformation ductility
of brittle high-entropy alloys via metastability engineering. Adv Mater 2017;29:
1701678.
[149] De Cooman BC, Estrin Y, Kim SK. Twinning-induced plasticity (TWIP) steels. Acta
Mater 2018;142:283–362.
[150] Omole Samuel, Lunt Alexander, Kirk Simon, Shokrani Alborz. Advanced
processing and machining of tungsten and its alloys. J Manuf Mater Process 2022;
6:15.
[151] Meng LX, Yang HJ, Wang SG, Ji HB, Shao XH, Zhang ZJ, et al. Defect-healing of a
s laser-powder bed fusion Ti6Al4V alloy via electro-assisted micro-forging. Mater
Chract 2023;205:113298.
[152] Barr CM, Duong T, Bufford DC, Milne Z, Molkeri A, Heckman NM, et al.
Autonomous healing of fatigue cracks via cold welding. Nature 2023;620:552.
[153] Sokoluk M, Yuan J, Pan S, Li X. Nanoparticles enabled mechanism for hot
cracking elimination in aluminum alloys. Metall Mater Trans 2021;52A:3083–96.
[154] Kenel C, Casati NPM, Dunand DC. 3D ink-extrusion additive manufacturing of
CoCrFeNi high- entropy alloy micro-lattices. Nat. Commu. 2019;10:904.
[155] Stawovy MT, Myers K, Ohm S. Binder jet printing of tungsten heavy alloy. Int J
Refract Met Hard Mater 2019;83:104981.
[156] Jung W, Pikhitsa PV, Jung Y-H, Shin J, Han M, Choi M. 3D nanoprinting with
charged aerosol particles-an overview. Acc Mater Res 2021;2:1117–28.
[157] Huber F, Bartels D, Schmidt M. In-situ alloy formation of a WMoTaNbV refractory
metal high entropy alloy by laser powder bed fusion (PBF-LB/M). Materials 2021;
14:3095.
[158] Sharma S, Krishna KVM, Joshi SS, Radhakrishnan M, Palaniappan S, Dussa S,
et al. Laser based additive manufacturing of tungsten: multi-scale thermos-kinetic
and thermo-mechanical computational model and experiments. Acta Mater 2023;
259:119244.
[159] Ramakrishnan T, Kumar A, Kumar TS, Kwon S, Muniz-Lerma JA, Cauvin R, et al.
Crack-free tungsten fabricated via laser powder bed fusion additive
manufacturing. Adv Funct Mater 2024;34:2309304.
L. Ji et al. Journal of Manufacturing Processes 131 (2024) 2535–2554 
2554
