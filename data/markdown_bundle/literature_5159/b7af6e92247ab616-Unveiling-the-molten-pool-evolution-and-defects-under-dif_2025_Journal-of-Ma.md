# Unveiling-the-molten-pool-evolution-and-defects-under-dif_2025_Journal-of-Ma

<!-- source: D:\总文献\Unveiling-the-molten-pool-evolution-and-defects-under-dif_2025_Journal-of-Ma.pdf -->
<!-- file_sha256: b351850ac6f5f2892f520031b839b8dc0a9d4865d6dd0d60e22c12addefe9bfe -->

## Page 1

Unveiling the molten pool evolution and defects under different processing 
parameters in pure tantalum fabricated via laser powder bed fusion
Zhenyu Yang
a , b
, Jiangqi Zhu
b , *
, Yajun Liu
c
, Chao Pan
d
, Dan Wu
a
, Zhaoyang Deng
b
, Di Wang
e
, 
Rongpei Shi
f
, Gang Wang
a , *
, Zhaoguo Qiu
a
, Min Liu
b
, Xingchen Yan
b , *
a
School of Materials Science and Engineering, South China University of Technology, Guangzhou 510641, China
b
Institute of New Materials, Guangdong Academy of Sciences, Guangdong-Hong Kong Joint Laboratory of Modern Surface Engineering Technology, Guangdong 
Provincial Key Laboratory of Modern Surface Engineering Technology, Guangzhou, Guangdong 510651, PR China
c
Beijing Research Institute of Traumatology and Orthopaedics, Beijing Jishuitan Hospital, Capital Medical University, Beijing 100035, China
d
Beijing Chunlizhengda Medical Instruments Co., Ltd, Beijing 101112, China
e
School of Mechanical & Automotive Engineering, South China University of Technology, Guangzhou 510641, China
f
School of Materials Science and Engineering, Harbin Institute of Technology, Shenzhen 518055, China
ARTICLE INFO
Keywords:
Defects
LPBF
Molten pool
Processing parameters
Tantalum
ABSTRACT
Tantalum (Ta) is an important biomedical material for the preparation of implants due to its excellent me -
chanical and biological properties. However, the presence of defects has a significant impact on the implantation 
effect. The stability and flow state of the molten pool, which is controlled by processing parameters, are of great 
significance for the formation of defect-free components fabricated by laser powder bed fusion (LPBF). To date, 
the relationship among processing parameters, molten pool evolution, and defects has not been established yet. 
In this paper, single-track and bulk samples of pure Ta were fabricated using LPBF technology, and a powder- 
resolved computational fluid dynamics (CFD) model of pure Ta was established to study heat transfer and 
fluid flow characteristics in the molten pool. The effects of processing parameter variations on the types and 
quantities of defects were systematically analyzed, and the formation mechanisms of defects were revealed by 
combining simulation results of molten pool evolution under different parameters. The results show that 
increasing the laser energy density would promote higher temperature and faster velocity fields within the 
molten pool. Under the elevated temperature field, the spreading speed was faster than the solidification speed of 
the molten Ta, and the melt of powders was more sufficient, resulting in fewer keyholes after solidification. 
Under the rapid velocity field, the Marangoni convection was intense, which would lead to difficulty for bubbles 
to escape and an increase in gas pores. The coordination of temperature and velocity fields in the molten pool 
determined the types and quantities of defects in LPBF samples. Unmelted Ta powders acted as barriers to 
prevent the epitaxial growth of grains, depending on the melting state. This article presents a profound analysis 
of processing parameters, defects, molten pools, and microstructure changes, and is expected to provide scientific 
and theoretical support for the exploration of LPBF processing parameters and the causes of changes in the 
microstructure and properties of LPBF samples.
1. Introduction
Due to the gradual aging of the world ’ s population, people are sus -
ceptible to various orthopedic injuries, including fractures, bone defects, 
and other bone-related diseases [ 1 , 2 ]. For patients with large bone de -
fects, orthopedic implant surgery is a crucial method to restore mobility 
[ 3 ]. Common materials used for bone implants that can persist in the 
human body with minimal degradation include titanium (Ti) and Ti 
alloys, cobalt ‑ chromium (CoCr) alloys, stainless steel, tantalum (Ta), etc 
[ 4 ] Currently, Ta is becoming an ideal candidate among non-degradable 
medical metallic materials due to its unique advantages. Metallic im -
plants are subjected to a complex corrosive environment and long-term 
cycle stress within the body. Therefore, the effect of the implantation is 
highly related to the combination of multiple properties [ 5 ]. The Ta
2
O
5 
oxide film formed on the surface of Ta improves its corrosion and wear 
resistance [ 6 ]. Ta implants are nontoxic to human cells and beneficial 
* Corresponding authors.
E-mail addresses: zhujiangqi@gdinm.com (J. Zhu), msgwang@scut.edu.cn (G. Wang), yanxingchen@gdinm.com (X. Yan). 
Contents lists available at ScienceDirect
Journal of Manufacturing Processes
journal homep age: www. elsevier.com/ locate/m anpro
https://doi.org/10.1016/j.jmapro.2025.04.041
Received 2 July 2024; Received in revised form 14 March 2025; Accepted 9 April 2025 
Journal of Manufacturing Processes 144 (2025) 311–325 
Available online 19 April 2025 
1526-6125/© 2025 The Society of Manufacturing Engineers. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, 
and similar technologies.

## Page 2

for cell attachment [ 7 ]. Additionally, compared to other biomaterials, 
Ta has an excellent ability to promote cell proliferation and adhesion 
[ 8 ], as well as its capacity to stimulate bone osteogenesis [ 9 ], facilitating 
a more rapid integration between the bone and the implant. This reduces 
the duration of the patient ’ s recovery and is beneficial for the long-term 
stability of the implant. Based on the aforementioned advantages of Ta 
in biomedical applications, it has become a research hotspot in the field 
of biomedical materials in recent years [ 10 ].
Customization and lightweight are underlined characteristics and 
demands of medical metallic implants as patients have varying lesion 
sites [ 11 ]. A porous design is essential for implants, but it also poses 
significant challenges to traditional processing techniques. As a kind of 
additive manufacturing technique, laser powder bed fusion (LPBF) is 
suitable for processing porous and complex structured products since 
the components are shaped by layer-by-layer stacking. Products fabri -
cated via LPBF only require a small amount of post-processing before 
being put into use [ 12 ], which reduces the processing cycle and in -
creases the materials utilization rate. The emergence of LPBF greatly 
abates the difficulty of preparation and delivery costs, which has 
brought new vitality to the research of Ta [ 13 ]. LPBF customized porous 
implants are currently trending in orthopedic practice, necessitating the 
fabrication of Ta implants [ 14 ].
Despite the fact that Ta processed by LPBF is a popular choice for the 
fabrication of implants, no Ta products have virtually achieved large- 
scale commercialization in the medical field, with only a few products 
such as intervertebral fusion cages, bone stems, and acetabular cups 
being applied clinically [ 15 – 17 ]. Furthermore, the development of high- 
stress load-bearing bone implants such as joints is still ongoing. One of 
the reasons is possibly related to the mechanical properties of Ta, where 
stringent requirements for strength and toughness are demanded. De -
fects and solidification microstructure within the molten pools intro -
duced during the LPBF process are important factors affecting 
mechanical performance [ 18 ].
To promote the application of pure Ta, many scholars have con -
ducted systematic research on the optimization of LPBF processing pa -
rameters and the regulation of mechanical properties. The selection of 
processing parameters directly determines the microstructure and me -
chanical properties; hence, the exploration of processing parameters is 
the main focus to control mechanical properties [ 19 ]. Laser power ( P ) 
and scanning speed ( v ) determine the output energy and the time for the 
powder to absorb the energy, respectively. Matching combinations of P 
and v can obtain relatively dense, high-performance pure Ta samples. 
Zhou et al. [ 20 ] fabricated Ta via LPBF by adopting scanning speed at a 
range of 60 – 200 mm/s and showed that the relative density and 
ductility were not ideal due to the formation of cracking and pores. Song 
et al. [ 21 ] further optimized the process, using a fixed laser power of 
300 W and a scanning speed of 400 – 1000 mm/s, establishing a link 
between scanning speed variation and molten pool width. At low 
scanning speed, the laser residence time is longer, which is more 
conducive to presenting a wide molten pool. Their results showed that 
under high P and high v , the density and mechanical properties of Ta 
samples were improved. The reason for such a large performance gap 
under different combinations of P and v may be attributed to the changes 
in the type, size, and number of defects as well as the evolution of molten 
pools [ 22 ].
During the LPBF process, the direction and speed of the melt flow and 
the internal temperature field are important factors that affect the for -
mation of the sample. Changes in processing parameters can alter the 
heat distribution, thereby affecting the stability of the molten pool. 
Unstable molten pools can promote the formation of defects. The com -
plex heat transfer and fluid flow phenomena within the molten pool 
during processing can be revealed through CFD simulations, enabling 
more precise adjustment of process parameters and optimization of 
sample quality. Research related to the effects of size alteration in 
molten pools on microstructure and mechanical properties has been 
performed on stainless steel [ 23 , 24 ], Ni-based alloys [ 25 ], Al alloys 
[ 26 , 27 ], Ti alloys [ 28 ], and so on. Columnar grains typically grow along 
the direction of rapid heat dissipation, and the heat dissipation at the 
boundary of the molten pool is significantly faster than that within the 
interior, so the columnar grains will grow perpendicular to the bound -
ary. The significant difference in orientation of grains on molten pool 
boundaries would easily lead to the formation of cracks and fracture 
under loads perpendicular to the molten pool boundaries [ 29 ]. Due to 
the formation of pores, cracks, and other defects near the boundaries, 
the microhardness and stress bearing ability at the boundaries are 
poorer compared to that in the interior.
However, there is currently less research on the evolution in the 
molten pool during LPBF of Ta and its influence on defects. In this 
article, both the changes in the number of defects and the alterations in 
the width and depth of the molten pool under varying parameters are 
investigated in detail. Simultaneously, a combination of experimental 
characterization and CFD simulation is used to explore the evolution of 
the molten pool and its effects on the subsequent solidification micro -
structure. The relationship between the impact of the molten pool and 
defects on the performance of the samples is fully discussed.
2. Experimental and modeling procedures
2.1. Calculation of the process window for LPBF Ta
Ta has a high melting point [ 30 ]. To ensure that the interior of LPBF 
Ta samples has good metallurgical bonding while avoiding excessive 
laser energy density that may lead to sample burnout [ 31 , 32 ], it is 
necessary to systematically calculate and analyze the rationality of 
processing parameter settings. The minimum energy output required to 
fully melt the powder per unit volume Q
n
, can be expressed as [ 33 ]: 
Qn = ρ [ L + Cp ( Tm T 0 ) ] (1) 
where ρ is the density of pure Ta at ambient temperatures, L is the latent 
heat of fusion, C
p 
is the specific heat of Ta, T
m
, and T
0 
referring to the 
melting temperature and the preheating temperature of Ta, respectively. 
Relative property values are displayed in Table 1 and Table 2 .
In the LPBF process, the laser is the heat source and the laser heat 
Table 1 
LPBF processing parameters.
Processing parameters Values
Preheating temperature ( T
0
) 373 K
Laser spot radius ( r
b
) 50 μ m
Hatch distance ( d ) 80 μ m
Layer thickness ( T ) 20 μ m
Laser power ( P ) 180, 200, 220, 240, 260, 300 W
Scanning speed ( v ) 500, 580, 660, 740, 800 mm/s
Table 2 
Parameters used in the heat transfer and fluid flow simulation of LPBF pure Ta 
[ 40 – 43 ].
Physical quantity Value
Solid phase temperature 3288 K
Liquid phase temperature 3288 K
Evaporation temperature 5643 K
Viscosity 0.001 Pa ⋅ s
Latent heat of fusion 3.6 × 10
4 
J ⋅ kg
 1
Latent heat of evaporation 4.1 × 10
6 
J ⋅ kg
 1
Laser absorption 0.41
Laser radius 50 μ m
Radiation coefficient 0.3
Stenfan-Blotzmann constant 5.67 × 10
 8 
W ⋅ m
 2
⋅ K
 4
Surface tension 2.131 kg ⋅ s
 2
Density 16.654 g ⋅ cm
 3
Specific Heat of fusion 231 J ⋅ kg
 1
⋅ K
 1
Thermal diffusion coefficient 6.2 × 10
 6 
m
2
⋅ s
 1
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
312

## Page 3

transfer process needs to be considered. The laser energy flux, q
in
(r) , can 
be expressed by the following formula [ 34 ]: 
qin ( r ) =
2 η P
π r
2
b
exp
(
 
2 r
2
r
2
b
)
(2) 
where η is the laser absorptivity coefficient of the Ta powder, P is the 
laser power, r
b 
is the laser spot radius, and r is the distance from the laser 
center spot. Since the laser energy distribution approximately follows a 
Gaussian distribution, with higher temperature in the central area and 
lower on both sides [ 35 ], it is necessary to use integration to calculate 
the total laser input energy Q
in
: 
Qin =
∫
rb
0
2 π rqin ( r ) dr = η P
(
1 
1
e
2
)
(3) 
The laser can be approximated as a circle, and the average energy 
flux per unit area of the circle q
a 
is: 
qa =
η P
π r
2
b
(
1 
1
e
2
)
(4) 
Heat transfer occurs in three basic modes: thermal conduction, 
convective heat transfer, and radiative heat transfer. Among them, the 
Fig. 1. (a) Schematic representation of the interaction between the laser and the powders during LPBF process; (b) Equivalent model of the molten pool; (c) Molten 
pool morphology in the preliminary experiment.
Fig. 2. (a) SEM micrograph and (b) size distribution of pure Ta powders; (c) The dimensional diagram of fabricated samples; (d)Schematic diagram of LPBF pro -
cessing and (e) scanning strategy of the LPBF process.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
313

## Page 4

laser transmits heat to the powder primarily through conduction, while 
a small portion of the energy is lost through radiation and convection 
[ 34 ], as illustrated in Fig. 1 a. Therefore, the effective laser energy flux, 
q
e
, is the portion of energy that the powders can absorb, which is 
assumed to be: 
qe = 80% qa (5) 
Setting that the existence time of a molten pool is t , it can be 
determined by a laser beam with a certain scanning speed to traverse its 
diameter, which is given by t =
2 rb
v
. The energy released by a single laser 
beam is the product of the effective laser flux and the laser beam area, 
that is, π r
2
b
qe . Therefore, during the existence of the molten pool, the unit 
volume energy absorbed by the molten pool, Q
v
, is: 
QV =
π r
2
b
qet
Ve
(6) 
The molten pool can be approximated as the spherical cap portion of 
a sphere ( Fig. 1 b). The immersion depth of the molten pool is H . The 
equivalent radius of the sphere is calculated as 
r
2
+ H
2
2 H
. Therefore, the 
volume of the spherical cap V
e 
can be expressed as [ 36 ]: 
Ve ≅
1
6
π
 
3 r
2
H + H
3
)
(7) 
By substituting all the equations, we can derive the energy absorbed 
by the powder per unit volume, Q
v
, as: 
Q
V
=
48
5
η
(
1 
1
e
2
)
rb
π
 
3 r
2
H + H
3
) .
P
v
(8) 
Through pre-experiments ( Fig. 1 c), r is taken as 77 μ m and H as 60 
μ m. To ensure the complete melting of the powder, it is necessary to 
make Q
v 
greater than or equal to Q
n
. Therefore, the value 
P
v
, called as the 
linear energy density, should not be less than 248 J/m. Based on this 
premise, wide processing parameters were investigated with a laser 
power range of 180 – 300 W, a scanning speed of 500 – 800 mm/s, and a 
linear energy density of 225 – 600 J/m.
2.2. Powder preparation and design of LPBF processing parameters
The plasma-spheroidized pure Ta powders were used in this study 
(Xingchen Technology Company, China). The D
v
(10) , D
v
(50) , and 
D
v
(90) of the powder were 20.7 μ m, 32.5 μ m, and 49.4 μ m, respectively 
( Fig. 2 a, b).
The samples were manufactured on a Ti substrate using a commer -
cial EOS M290 system (EOS GmbH, Germany) equipped with a 400 W 
Yb-fiber laser (1064 nm) ( Fig. 2 c). The equipped laser is circular with a 
diameter of 100 μ m, and its energy output follows a Gaussian distribu -
tion. The hatching distance and layer thickness were set to fixed values 
of 80 and 20 μ m, respectively ( Table 1 ). Laser powers ranging from 180 
to 300 W and scanning speeds of 500 – 800 mm/s were used to prepare 
bulk samples by varying the angle between layers by 67
◦
( Fig. 2 d). The 
30 fabricated samples are labeled as 1*-30* ( Fig. 2 c). The dimensions of 
the bulk samples were 10 mm × 10 mm × 10 mm. Single-track samples 
were fabricated using laser powers of 180 W, 240 W, and 300 W with 
scanning speeds of 500 mm/s, 660 mm/s, and 800 mm/s. High-purity Ar 
was chosen as the protecting atmosphere. The substrate was preheated 
to 373 K and the printing started when the oxygen content was reduced 
to 1000 ppm.
2.3. Measurements of relative density
All surfaces of the bulk specimen were polished sequentially with 
80#, 320#, and 1000# sandpaper to remove surface oxidation. The 
polished samples were then tested for relative density using the Archi -
medes method based on the following formula [ 37 ]: 
ρ
ρ s
=
ma ( ρ w ρ a )
( ma mw ) ρ s
+
ρ a
ρ s
(9) 
where ρ is the density of as-printed samples, ρ
s 
is the density of as-cast 
samples, m
a 
and m
w 
refer to the mass of samples in the air and water, 
respectively, and ρ
a 
and ρ
w 
are the density of air and water, respectively. 
Each sample was measured five times, and the average value was taken 
as the relative density.
2.4. Microstructure characterization
Before microstructure characterization, the as-printed samples were 
first embedded in epoxy resin and then ground using an automatic 
grinding and polishing machine (Tegramin-25, Denmark). Diamond 
polishing paste and SiO
2 
suspension were used successively to polish the 
samples until the surface became mirror-like for optical microscopy 
(OM, Leica Dmi5000 m, Germany) imaging. The macro morphology and 
the cross-sectional microstructure were characterized using scanning 
electron microscopy (SEM, FEI Nova NanoSEM 450, USA). The electron 
backscattered diffraction (EBSD) was performed to characterize grain 
size and crystallographic texture of the longitudinal facet after vibratory 
polishing for 2 h. To observe the morphology of the molten pool, the 
samples were etched for 30 s using a mixed solution of nitric acid, sul -
furic acid, and hydrofluoric acid in a volume ratio of 2:2:5.
2.5. Numerical simulation
Creating a powder bed model at the micrometer precision level based 
on the discrete element method, the sizes of powder particles in the 
powder bed followed a normal distribution ranging from 20 to 50 μ m. 
The heat transfer process and evolution of the molten pool under various 
parameters were simulated using Flow3D AM software. The size of the 
computational domain was 1 mm × 0.4 mm × 0.2 mm, including the 
baseplate (100 μ m), powder layer (60 μ m), and gas region (40 μ m). The 
mesh size was set to 7 μ m, and 9 sets of processing parameters including 
laser powers of 180 W, 240 W, and 300 W, and scanning speeds of 500 
mm/s, 660 mm/s, and 800 mm/s were simulated. The parameters used 
in heat transfer and fluid flow simulation of LPBF pure Ta are presented 
in Table 2 .
The heat transfer and fluid flow during LPBF process are described by 
the CFD model. The specific details of the formulas and governing 
equations used in the simulation refer to the previous work of the 
research group [ 38 ]. After establishing the geometric model using DEM, 
parameters such as powder material, quantity, shape, particle size, and 
distribution are set. Each discrete particle is subjected to forces from 
other particles, including gravity, elastic forces, frictional forces, and 
more. Under the influence of gravity, the powder particles are randomly 
stacked within a rectangular cavity until they reach a stable state. To 
facilitate the computation, certain physical mechanisms during the LPBF 
process are appropriately simplified: (1) It is assumed that the fluid in 
the molten pool exhibits laminar flow and is an incompressible New -
tonian fluid; (2) All thermal properties are considered as functions of 
temperature; (3) The flow at the interface between the solid and liquid 
phases is defined as a mushy zone [ 39 ].
3. Results
3.1. Morphologies of single-track samples
Based on the morphology characteristics, the fusion states of single- 
track samples were categorized into discontinuous ( Fig. 3 a-f) and 
continuous ( Fig. 3 g-i). When low laser power (180 W) was employed, 
the continuity of molten tracks was hampered by balling and unmelted 
particles. There was a noticeable necking phenomenon, with the widest 
part being greater than 100 μ m and the narrowest part being less than 
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
314

## Page 5

30 μ m ( Fig. 3 a-c). With the increase of laser power and energy density, 
the widths around the necking area were enlarged. Under moderate 
laser power (240 W), the continuity of the molten track was improved, 
and the width at the necking area increased with the increase in energy 
density ( Fig. 3 d-f). When the scanning speed exceeded 500 mm/s, the 
molten tracks appeared nonlinear ( Fig. 3 f). Further increasing the laser 
power to 300 W resulted in a continuous and smooth molten track, with 
thorough melting of Ta powder, outward spreading of the melt, and 
Fig. 3. OM images of single-track samples under various processing parameters on XY top view: (a) 180 W 500 mm/s; (b) 180 W 660 mm/s; (c) 180 W 800 mm/s; (d) 
240 W 500 mm/s; (e) 240 W 660 mm/s; (f) 240 W 800 mm/s; (g) 300 W 500 mm/s; (h) 300 W 660 mm/s; (i) 300 W 800 mm/s.
Fig. 4. SEM results of the LPBF Ta single track samples with various processing parameters on YZ cross-section: (a) 180 W 500 mm/s; (b) 180 W 660 mm/s; (c) 180 
W 800 mm/s; (d) 240 W 500 mm/s; (e) 240 W 660 mm/s; (f) 240 W 800 mm/s; (g) 300 W 500 mm/s; (h) 300 W 660 mm/s; (i) 300 W 800 mm/s.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
315

## Page 6

widening of the molten track ( Fig. 3 g-i).
Fig. 4 presents the SEM results of the LPBF samples under different 
cross-sections with various parameters. Relatively fractions of Ta pow -
ders were present in the solidified molten pool. Comparing Fig. 4 c, f, 
and i, it was evident that large and regular powders existed in single- 
track samples under low P . With increasing P , these powder particles 
were gradually melted, transforming into irregularly shaped unmelted 
particles ( Fig. 4 d-e). Low scanning speed allowed the molten droplets 
more time to extend deeper and wider, which led to the formation of 
molten pool with larger volume. Laser power had a more pronounced 
effect on the fraction of unmelted Ta. The single-track samples owned 
fewer unmelted particles under 300 W ( Fig. 4 g-h). The scanning speed 
and laser power are critical factors impacting the width of molten pool. 
Simply boosting the laser power or reducing the scanning speed would 
lead to a notable expansion in the molten pool width. Nevertheless, the 
length of molten pool fluctuated randomly and did not show a clear 
pattern in response to changes in parameters.
SEM images of the single-track samples revealed the presence of both 
regular and irregular unmelted particles ( P = 240 W, v = 660 mm/s), 
which generally existed along the edges ( Fig. 5 a-c). The elemental 
analysis of the unmelted particles indicated that they were Ta particles. 
In other areas of the molten pool, Ti and Ta were evenly distributed, 
with Ti being the majority ( Fig. 5 d-f). Line scans were performed on 
unmelted particles in two different areas within the molten pool ( Fig. 5
g, h). The variation in Ta and Ti content at different sites was similar, 
with Ta content predominating at the location of the unmelted particles, 
followed by a stepped decrease in Ta content as the distance from the 
unmelted particles increased. It is noteworthy that the ratio of Ta to Ti at 
the upper edge of the molten pool in the matrix and the unmelted par -
ticles corresponded to the ratio of these two elements at the same 
location at the lower edge of the molten pool.
3.2. Relative density
The OM images of the pure Ta processing window and the corre -
sponding relative densities are shown in Fig. 6 . Except for the samples 
processed at the low laser power of 180 W, samples were relatively 
dense under other parameters, with a density above 99 %. The results of 
Fig. 5. Microstructures of LPBF Ta specimen at a laser power of 240 W and a scanning speed of 660 mm/s: (a) SEM image; (b, c) EDS line from (a); (d-f) EDS map of 
(a); (g) Line scanning result of (b); (h) Line scanning results of (c).
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
316

## Page 7

relative density also matched the theoretical calculation of energy input. 
The laser power of 180 W was the critical value for melting Ta powders 
based on the relative density. The unmelted particles of the previous 
layer could be remelted by the penetration of the molten pool of the next 
layer during the processing of the bulk sample when the laser power 
exceeded 180 W.
Specifically, as the laser power increased, the density first increased 
to a stable region and then decreased slightly. The increase in scanning 
speed had no outstanding effect on the density of Ta, and the density 
showed a fluctuating trend. Based on the varying relative density, the 
processing window was classified as insufficient melting, sufficient 
melting, and excessive melting ( Fig. 6 ). Samples in insufficient melting 
zone exhibited significantly lower relative density ( ≤ 99 %). The relative 
density of samples in sufficient melting zone sustained a relative density 
above 99 %, while samples in the excessive melting area fluctuated 
around 99 % and exhibited regular gas pores ( Fig. 7 ). Select represen -
tative processing parameters from three areas for comparative study.
3.3. Microstructure observation
The OM images of the etched samples are shown in Fig. 8 . When the 
laser power of 180 W was employed, the molten pool was almost 
invisible, with long columnar grains extending upward from the bottom. 
When the laser power was further increased to 240 W, a few layers of 
molten pool are visible at the bottom. Due to the adoption of 67
◦
scanning strategy, the molten pool did not exist solely along the building 
direction, instead facing several directions. At a laser power of 300 W, 
due to the increased energy input, the molten pool absorbed sufficient 
Fig. 6. Cross-sectional microstructure and relative density of LPBF Ta samples under different processing parameters.
Fig. 7. Relationship between the relative density of LPBF Ta samples and the applied linear energy density.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
317

## Page 8

Fig. 8. Microstructure of LPBF pure Ta on cross sectional face after etching.
Fig. 9. EBSD orientation maps of LPBF pure Ta sample under various processing parameters on building direction: (a) 1*; (b) 3*; (c) 5*; (d) Grain size distributions 
when the laser power reaches 180 W; (e) 16*; (f) 18*; (g) 20*; (h) Grain size distributions when the laser power reaches 240 W; (i) 26*; (j) 28*; (k) 30*; (l) Grain size 
distributions when the laser power reaches 300 W.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
318

## Page 9

heat to expand wider and deeper, thus increasing the size of the molten 
pool. In comparison, when the scanning speed gradually increased from 
500 mm/s to 800 mm/s at the same laser power, the size of the molten 
pool tended to decrease.
Fig. 9 presents the EBSD grain orientation results, which were pre -
dominantly composed of coarse columnar grains, with a small number of 
fine grains presented in the bottom area near the substrate. The orien -
tation distributions of the grains showed no obvious anisotropy in the 
samples. Combining the grain size distribution, it was evident that the 
average grain size increased with the increase in laser power or the 
decrease in scanning speed. Under the laser power of 180 W and scan -
ning speeds greater than 500 mm/s, there were few grains larger than 
200 μ m in size and the majority of small grains ( Fig. 9 a-d). As the energy 
density increased, smaller grains gradually grew larger, and the pro -
portion of grains larger than 200 μ m significantly increased ( Fig. 9 h, l). 
Furthermore, long columnar grains tended to be distributed in the 
central area, while smaller grains were primarily distributed at the edges 
( Fig. 9 e-g and i-k). The variation and distribution of grain size were 
closely related to the heat input and the cooling rate within the molten 
pool.
Further magnifying the observation of the small grain area in Fig. 9 c, 
an unmelted Ta particle was found under this parameter ( Fig. 10 a). The 
EBSD image showed that the unmelted particles appear at the junction 
of multiple grain boundaries. ( Fig. 10 b). The grain size near the 
unmelted particles was relatively small (~62.8 μ m) compared with 
those under other processing parameters ( Fig. 9 ), and the growth of 
columnar grains was obstructed near the unmelted particle.
4. Discussion
4.1. Defects evolution and relative density change
The laser beam used in LPBF can instantaneously release high tem -
perature, leading to the melting of powders. The melting of the powder 
and the connection of molten droplets form a molten pool, which 
competes with the solidification process [ 44 ]. The time taking for the 
melt to spread completely was defined as t
Spreading
, and the time for the 
melt to solidify was defined as t
Solidification
. If t
Solidification 
> t
Spreading
, then 
the melt would spread completely before gradually solidifying, resulting 
in good interconnection between the molten tracks. However, the 
opposite scenario, where t
Solidification 
< t
Spreading
, could lead to discon -
tinuous molten tracks, resulting in defects such as pores and balling. The 
solidification time t
Solidification 
is defined as [ 45 ]: 
t
Solidification
= 2
(
r
2
3 a
)
ln
[
( Ta T 0 )
Tm T 0
]
(10) 
The spreading time t
Spreading 
is defined as [ 44 ]: 
t
Spreading
=
(
ρ r
3
σ
)
0 . 5
(11) 
where r denotes the radius of droplets, typically around 100 μ m [ 44 ], σ is 
the surface tension of Ta, a is the thermal diffusion coefficient, ρ is the 
density, T
a
, T
m
, and T
0 
denote respectively the ambient temperature, the 
melting point of Ta, and the preheating temperature ( Table 2 ). Through 
calculation, the droplet spreading time for Ta was 88.4 μ s. When the 
solidification time was 88.4 μ s, the temperature of the molten pool was 
3538 K ( Fig. 11 ). This indicated that during the LPBF process when the 
molten pool temperature was below 3538 K, solidification within the 
molten pool occurred faster than the spread of the melt. Conversely, 
when the temperature was above 3538 K, the melt flowed well, 
contributing to good interlayer bonding.
The simulation results of molten pool flow and temperature were 
used to further verify the computational results, as shown in Fig. 12 . 
When low laser power was employed, insufficient energy input was 
provided, which led to a low molten pool temperature below 3500 K, 
and the melt spread time was insufficient. This led to the solidification of 
areas between the molten tracks that had not been filled with the 
droplets, resulting in significant defects after solidification ( Fig. 12 a-c).
In addition to the discontinuity defects caused by the internal tem -
perature field variation of the molten pool, the presence and variation of 
unmelted particles and pores were also important factors affecting 
density. With a high melting point of 2997 
◦
C, Ta may not absorb enough 
energy at a laser power of 180 W, resulting in the presence of unmelted 
particles. Additionally, at lower temperatures, the viscosity of Ta melt 
was high, and poor spreading occurred. Coupled with the high surface 
tension, the spreading droplets tended to contract and spheroidize. 
Therefore, the presence of pores caused by unmelted particles and 
disconnected molten pools were the main factors causing the decrease in 
density at low laser power. The improvement in laser power caused the 
metal powder to absorb more heat per unit of time, which expanded the 
molten pool outward and deeper. This improved the fluidity and 
spreading properties of the melt. Therefore, samples in the intermediate 
parameter window were highly dense and had fewer defects ( Fig. 12 d- 
f). Nevertheless, when the laser power was further increased, the rela -
tive density exhibited a slight decreasing trend. This phenomenon was 
attributed to the appearance of amounts of regular and small pores. 
When the linear energy density was relatively high, the convective 
motion and vaporization of molten metal became more prominent 
( Fig. 12 g-i). Consequently, more and more gases were trapped in the 
molten pool, leading to a decrease in relative density.
4.2. Evolution of molten pool
4.2.1. Effect of scanning speed on the molten pool
Fig. 13 illustrates the velocity field of the molten pool of LPBF Ta 
obtained from simulations under the scanning speeds of 500, 660, and 
800 mm/s. At low scanning speeds, the laser dwelled on a particular spot 
for a longer duration, resulting in more powders being melted under the 
laser irradiation. In the velocity vector diagram at 800 μ s, a substantial 
amount of melt could be observed trending downward to the left, hence, 
Fig. 10. Microstructure of pure Ta sample 5*: (a) Backscattered electron image; (b) EBSD image.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
319

## Page 10

under the parameters in Fig. 4 , the molten pool had a deeper immersion 
depth. In the front end of the laser-irradiated area in Fig. 13 a at time 
400 μ s and Fig. 13 b at time 160 μ s, island-like molten regions could be 
seen. The internal temperature field within the laser was exhibited in 
Gaussian distribution. With high laser power laser input, even the areas 
exposed to the periphery of the laser were partially melted. To reduce 
surface tension, the material tended to form spheroidal shapes. Due to 
the Plateau-Rayleigh instability, the melt exhibited unstable oscillations 
under the combined effects of surface tension and gravity, leading to the 
formation of spherical island-like structures. However, as the laser swept 
over the island region, the temperature of the molten material increased, 
enhancing its fluidity. The island droplets flowed backward and con -
nected with other molten materials. Therefore, at scanning speeds of 
500 mm/s and 660 mm/s, the molten pool exhibited greater width and 
depth. When 800 mm/s scanning speed was applied, the thermal 
gradient would increase, which exacerbated the Marangoni flow [ 46 ]. 
As depicted in Fig. 13 c at time 120 μ s, the flow of melt within the molten 
pool did not simply circulate in a clockwise or counterclockwise direc -
tion but rather dispersed along various directions. This non-directional 
flow led to the entrapment of gas within the molten pool [ 47 ]. With 
the shorter solidification time provided by high scanning speeds, bub -
bles might remain trapped, ultimately forming pores upon solidification 
( Fig. 13 c at time 360 μ s and time 480 μ s).
4.2.2. Effect of laser power on the molten pool
When the scanning speed was set as 660 mm/s, the internal tem -
perature field within the molten pool fluctuated with the increase of 
laser power. Under the laser power of 180 W, the temperature of melts 
was below 3875 K, hence a considerable number of inter-molten pool 
pores appeared at 160 and 320 μ s ( Fig. 14 a). The surface tension of the 
molten Ta was high at low temperatures. To reduce the surface tension, 
the molten pool fragmented into multiple small droplets and became 
Fig. 11. A plot of the functional relationship between the solidification time and temperature of molten Ta.
Fig. 12. Single-track morphology of LPBF pure Ta samples in the cross-section view obtained from simulations under various processing parameters: (a) 1*; (b) 3*; 
(c) 5*; (d) 16*; (e) 18*; (f) 20*; (g) 26*; (h) 28*; (i) 30*.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
320

## Page 11

spheroidized. Consequently, spheroidization defects also occurred in the 
samples. Additionally, under this parameter, there was almost no 
downward velocity vector in the molten pool. In contrast, there was a 
greater amount of backward flow, hence the length of the molten pool 
was relatively small while the width was larger, as shown in Fig. 4 b.
When the laser power increased to 240 W, the molten pool flowed 
more intensely, which was characterized by a denser array of velocity 
vectors ( Fig. 14 b). The temperature within the molten pool was around 
3875 K. At the edges of the molten pool, the temperature did not reach 
the melting point of Ta, resulting in a certain amount of Ta powders 
moving into the edge of the molten pool under the influence of gravity. 
Driven by the downward velocity vector of the molten pool, the powders 
were transferred to the deeper areas of the molten pool. However, due to 
low temperatures at the edge, it ultimately remained as unmelted par -
ticles. The quantity of unmelted particles was greatly affected by 
parameter variations, as shown in Fig. 4 . When the laser power was 180 
W, the molten pool was shallower with larger intact particles remaining. 
As the laser power increased, the molten pool deepened, and both reg -
ular and irregular powders were present. The irregular powders were Ta 
powders that had been partially melted by the molten pool. Since there 
was not enough energy to completely transform the powder into a liquid 
state, the powder remained in an irregular form ( Fig. 4 e). When the 
laser power was 300 W, the number of unmelted particles was signifi -
cantly reduced, and the single-track fused well with the substrate. At a 
medium laser power of 240 W, reducing the powder particle size was an 
effective way to decrease the number of unmelted particles.
4.3. Impact of melting state on defects
Fig. 15 shows the evolution of the inner temperature and molten 
pool. At t = 800 μ s, a depression zone could be observed between two 
protruding molten pools ( Fig. 15 a). Within this area, the temperature 
field exceeded 4000 K, which reached the boiling point of Ti. The Ti 
metal vaporized, and the recoil pressure pushed the molten pool 
downward. The resulting vapor recoil pressure was sufficient to over -
come the surface tension of the liquid metal and the force of gravity, 
thereby displacing some of the liquid metal and causing the concave of 
the laser-irradiated area of the molten pool, forming a small hole ( Fig. 15
b). However, under these parameters, the surface tension of the molten 
pool was relatively low, with a greater tendency to spread out. Addi -
tionally, there were velocity vectors in both the left and right regions of 
the keyhole that fell towards the center. Therefore, as time extended, the 
keyhole area disappeared, connecting the two separate molten pools 
( Fig. 15 c).
At t = 960 μ s, the molten pool could be divided into four zones ac -
cording to the velocity vector: clockwise flow, anticlockwise flow, hor -
izontal flow, and downward flow zone ( Fig. 15 d). At the range of 
clockwise flow and anticlockwise flow, although the direction of the 
Fig. 13. Velocity vector plots of the single-track cross-sectional molten pool of LPBF Ta obtained from simulations under 300 W and various scanning speeds: (a) 500 
mm/s; (b) 660 mm/s; (c) 800 mm/s.
Fig. 14. Velocity vector plots of the single-track cross-sectional molten pool of 
LPBF Ta obtained from simulations under 660 mm/s and various laser power: 
(a) 180 W; (b) 240 W; (c) 300 W.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
321

## Page 12

velocity vector flow was different, the result was the same: the molten 
metal moved downward from the central upper surface and then flowed 
towards the edge. At the edge, there were two types of velocity vector 
flows, one flowed parallel, and the other flowed downward. Conse -
quently, affected by the molten pool flow, some particles that had not 
yet melted left the area of 4000 K and moved towards the edge areas, 
either to the left or downward ( Fig. 4 a). Within the 2000 K area, it was 
still above the melting point of Ti, hence the molten Ti continued to force 
the unmelted Ta particles to flow. Near the edge areas, the temperature 
of the molten pool decreased and Ti gradually solidified, therefore, the 
unmelted particles were mainly concentrated and distributed in the edge 
areas where the temperature was lower ( Fig. 15 e-f).
4.4. Combined effects of G and R in the molten pool on the microstructure
Fig. 16 and Fig. 17 display the temperature distribution of various 
locations obtained from simulations under various parameters. For 
constant scanning track, slow scanning speed caused more processing 
time, which intensified the heating of temperature. Consequently, the 
peak temperature was higher with a slower scanning speed ( Fig. 16 a). 
By contrast, higher laser power contributed to higher peak temperature 
owing to more sufficient heat input ( Fig. 17 a). The temperature 
continuously rose and reached its peak at X = 0.4 mm, and then dropped 
sharply as the laser moved away ( Fig. 16 b and Fig. 17 b). Such drastic 
temperature changes could lead to high cooling rates and temperature 
gradients, affecting the microstructure formed afterward.
In the vicinity of the temperature peak on the temperature distri -
bution curve and the cooling curve, performing linear fitting resulted in 
slopes that represented the temperature gradient ( G ) and the change in 
cooling rate ( R ), respectively. The G and R values are displayed in 
Table 3 . For fixed v ( v = 660 mm/s), G and R increased with more energy 
input. However, for fixed P ( P = 180 W), longer scanning time induced 
more heat absorption by the molten pool, which improved the value of 
G . Once the laser moved away from a certain point, the temperature 
began to decrease and cooled down. Therefore, it could be understood 
that a faster scanning speed led to a more rapid temperature drop, and 
thus a higher cooling rate.
G and R were two key factors impacting the microstructure, and 
more pronounced G would induce more directional solidification. Heat 
was consumed more rapidly in the direction of the temperature gradient, 
causing the material to solidify in a preferential direction. Furthermore, 
the lack of constitutional supercooling and heterogeneous nucleation 
sites in pure Ta made it prone to the thermodynamic tendency of 
forming columnar grains. In the case of a slow cooling rate, the columnar 
grains coarsen through competitive growth, further promoting the for -
mation of columnar grains. As a result, the dynamic tendency of forming 
columnar grains was high, leading to the observation of only columnar 
grains under visual fields, as shown in Fig. 8 , with no sign of equiaxed 
grains.
The presence of unmelted particles could act as an obstacle to the 
growth of long columnar grains ( Fig. 18 a). At low laser power, the 
molten pool was discontinuous, and the balling and unmelted particles 
together became barriers to the epitaxial growth of columnar grains 
( Fig. 18 b and Fig. 10 b). Therefore, under these processing parameters, 
the average grain size formed was relatively small in comparison. 
However, the remaining unmelted particles and consequent defects had 
Fig. 15. Representative simulation result showing the flow characteristics in a single-track LPBF of pure Ta ( P = 240 W, v = 660 mm/s): (a) t = 800 μ s; (b) Keyhole 
generation; (c) Keyhole disappear; (d) t = 960 μ s; (e) The flow of unmelted particles; (f) The solidification of molten pool.
Fig. 16. Temperature distribution within the molten pool of LPBF Ta obtained from simulations: (a) The temperature changes along X -axis ( Y = 0.2 mm, Z = 0.1 mm, 
t = 0.6 ms); and (b) the temperature changes with time ( X = 0.4 mm, Y = 0.2 mm, Z = 0.1 mm) under various scanning speeds when P = 300 W.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
322

## Page 13

a detrimental effect on the interface bonding. Even at low laser power 
where there were a certain number of unmelted particles hindering the 
columnar grains, the depth and width of the molten pool for each layer 
processed were relatively large. Thus, under the influence of the adja -
cent molten pools and the next layer ’ s molten pool, the unmelted par -
ticles would be remelted and the grains continued to grow in a specific 
direction ( Fig. 18 d). This phenomenon was very evident at P = 300 W 
and v = 500, 660 mm/s ( Fig. 9 g-h). The long and coarse columnar grains 
would deteriorate densification and mechanical properties, resulting in 
anisotropy. When the laser power of 240 W was employed, the unmelted 
particles were melted but the columnar grains that were hindered by 
them did not grow epitaxially along a fixed orientation, resulting in the 
length of the columnar grains failing to reach the size under high laser 
power. Meanwhile, the defects were minimal and the bonding between 
layers was fine, which belonged to the optimal parameter range ( Fig. 18
c). When processing refractory metals like Ta, which required a signif -
icant amount of heat input, the formation of equiaxed grains was diffi -
cult, and long columnar grains often penetrated through multiple 
molten pools. As a result, it was almost impossible to distinguish indi -
vidual molten pools in the etched bulk samples and only a few layers of 
molten pools could be observed at the bottom at high laser power 
( Fig. 8 ).
5. Conclusions
In this paper, LPBF pure Ta of single-track and bulk samples were 
successfully fabricated. By integrating the simulation results of the 
molten pool evolution, the flow of melt in the single-track molten pool 
and the impact of unmelted particles on the microstructure and densi -
fication of multiple-track samples were analyzed. The major conclusions 
are as follows: 
Fig. 17. Temperature distribution within the molten pool of LPBF Ta obtained from simulations: (a) The temperature changes along X -axis ( Y = 0.2 mm, Z = 0.1 mm, 
t = 0.6 ms); and (b) the temperature changes with time ( X = 0.4 mm, Y = 0.2 mm, Z = 0.1 mm) under various laser power when v = 660 mm/s.
Table 3 
The range of G and R within the molten pool of LPBF Ta.
P (W) v (mm/s) G (K/m) R (K/s)
180 660 7.54 × 10
6
– 1.25 × 10
7
3.28 × 10
6
– 4.98 × 10
6
240 660 8.80 × 10
6
– 2.15 × 10
7
4.87 × 10
6
– 8.71 × 10
6
300 660 1.34 × 10
7
– 1.88 × 10
7
6.28 × 10
6
– 1.09 × 10
7
300 500 1.55 × 10
7
– 2.24 × 10
7
7.29 × 10
6
– 9.60 × 10
6
300 800 1.29 × 10
7
– 1.87 × 10
7
1.01 × 10
7
– 1.17 × 10
7
Fig. 18. The schematic diagram of the effect of unmelted particles on grain growth under different parameters in LPBF Ta: (a) Coexistence of unmelted particles and 
columnar grains in a single-track sample; (b) Unmelted particles remain unmelted under low energy; (c) Unmelted particles were melted under moderate energy; (d) 
Unmelted particles were melted and grain coarsening under high energy.
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
323

## Page 14

(1) Due to the high melting point of Ta, variations in parameters 
cause the change of defects in samples. Samples fabricated by low 
power exhibited a number of unmelted particles and balling 
owing to the impacts of low energy input and short solidification 
time. As energy input increased, the fluidity of the melt improved 
and defects were reduced. When the energy input exceeded a 
certain range (393.9 J/m), the convection within the molten pool 
intensified, leading to an increase in the gas pores.
(2) Owing to the high temperature induced by high-energy laser, Ti 
and Ta melted and mixed evenly at the influence of Marangoni 
flow. The unmelted Ta particles were brought into the bottom 
and edge of the molten pool by Ti melt flow and solidified there.
(3) The grain growth of LPBF Ta is influenced by defects and tem -
perature fields. High temperature gradient and cooling rate 
within the molten pool contributed to the formation and coars -
ening of columnar grains. Adverse unmelted particles under high 
laser power could be remelted and played a certain role in hin -
dering the growth of columnar grains.
CRediT authorship contribution statement
Zhenyu Yang: Writing – original draft, Investigation, Conceptuali -
zation. Jiangqi Zhu: Writing – review & editing, Methodology, Inves -
tigation, Conceptualization. Yajun Liu: Resources. Chao Pan: 
Resources. Dan Wu: Formal analysis. Zhaoyang Deng: Data curation. 
Di Wang: Methodology. Rongpei Shi: Software. Gang Wang: Writing – 
review & editing, Supervision, Funding acquisition. Zhaoguo Qiu: 
Project administration. Min Liu: Project administration, Funding 
acquisition. Xingchen Yan: Supervision, Project administration, Meth -
odology, Funding acquisition.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgements
This research was supported by the National Key R & D Program 
(2022YFC2406000), Guangdong Academy of Science Projects 
(2022GDASZH-2022010107), Guangdong Provincial Key R & D Program 
(2023B0909020004), GDAS ’ project of Science and Technology Devel -
opment (2022GDASZH-2022010203-003), Guangdong province Sci -
ence and Technology (2023B1212120008, 2023B1212060045).
References
[1] Mastnak T, Maver U, Fin ˇsgar M. Addressing the needs of the rapidly aging society 
through the development of multifunctional bioactive coatings for orthopedic 
applications. Int J Mol Sci 2022;23(5):2786. https://doi.org/10.3390/ 
ijms23052786 .
[2] Ru Q, Li Y, Xie W, Ding Y, Chen L, Xu G, et al. Fighting age-related orthopedic 
diseases: focusing on ferroptosis. Bone Res 2023;11(1):12. https://doi.org/ 
10.1038/s41413-023-00247-y .
[3] Kim T, See CW, Li X, Zhu D. Orthopedic implants and devices for bone fractures 
and defects: past, present and perspective. Eng Regen 2020;1:6 – 18. https://doi. 
org/10.1016/j.engreg.2020.05.003 .
[4] Chen Q, Thouas GA. Metallic implant biomaterials. Mater Sci Eng R 2015;87:1 – 57. 
https://doi.org/10.1016/j.mser.2014.10.001 .
[5] Wauthle R, van der Stok J, Amin Yavari S, Van Humbeeck J, Kruth JP, Zadpoor AA, 
et al. Additively manufactured porous tantalum implants. Acta Biomater 2015;14: 
217 – 25. https://www.ncbi.nlm.nih.gov/pubmed/25500631 .
[6] Hou J, Wang Y, Yuan Z, Cai H, Chen W. Study on improving corrosion resistance of 
tantalum coating by anodic oxidation. Int J Electrochem Sci 2021;16. https://doi. 
org/10.20964/2021.07.13 .
[7] Koshevaya E, Nazarovskaia D, Simakov M, Belousov A, Morozov V, Gandalipov E, 
et al. Surfactant-free tantalum oxide nanoparticles: synthesis, colloidal properties, 
and application as a contrast agent for computed tomography. J Mater Chem B 
2020;8(36):8337 – 45. https://doi.org/10.1039/D0TB01204A .
[8] Findlay DM, Welldon K, Atkins GJ, Howie DW, Zannettino AC, Bobyn D. The 
proliferation and phenotypic expression of human osteoblasts on tantalum metal. 
Biomater 2004;25(12):2215 – 27. https://doi.org/10.1016/j. 
biomaterials.2003.09.005 .
[9] Wang X, Ning B, Pei X. Tantalum and its derivatives in orthopedic and dental 
implants: osteogenesis and antibacterial properties. Colloids Surf B: Biointerfaces 
2021;208:112055. https://doi.org/10.1016/j.colsurfb.2021.112055 .
[10] Huo W, Zhao L, Yu S, Yu Z, Zhang P, Zhang Y. Significantly enhanced osteoblast 
response to nano-grained pure tantalum. Sci Rep 2017;7(1):40868. https://doi. 
org/10.1038/srep40868 .
[11] Bandyopadhyay A, Mitra I, Goodman SB, Kumar M, Bose S. Improving 
biocompatibility for next generation of metallic implants. Prog Mater Sci 2023; 
133:101053. https://www.sciencedirect.com/science/article/pii/S0079642522 
001347 .
[12] Didier P, Le Coz G, Robin G, Lohmuller P, Piotrowski B, Moufki A, et al. 
Consideration of SLM additive manufacturing supports on the stability of flexible 
structures in finish milling. J Manuf Process 2021;62:213 – 20. https://doi.org/ 
10.1016/j.jmapro.2020.12.027 .
[13] Li K, Zhai Y, Zhu J, Hu X, Su C, Kong Y, et al. Effect of building orientation on the in 
vitro corrosion of biomedical Zn-Cu alloys prepared by selective laser melting. 
Corros Sci 2024;231:111957. https://doi.org/10.1016/j.corsci.2024.111957 .
[14] Ma Z, Li J, Cao F, Yang J, Liu R, Zhao D. Porous silicon carbide coated with 
tantalum as potential material for bone implants. Regen Biomater 2020;7(5): 
453 – 9. https://doi.org/10.1093/rb/rbaa021 .
[15] Tang H, Yang K, Jia L, He W, Yang L, Zhang Xz. Tantalum bone implants printed by 
Selective Electron Beam Manufacturing (SEBM) and their clinical applications. 
JOM 2020;72(3):1016 – 21. https://doi.org/10.1007/s11837-020-04016-8 .
[16] Zhao D, Ma Z, Wang T, Liu B. Biocompatible porous tantalum metal plates in the 
treatment of tibial fracture. Orthop Surg 2019;11(2):325 – 9. https://doi.org/ 
10.1111/os.12432 .
[17] Li Z, Chen G, Xiang Y, Muheremu A, Wu X, He P, et al. Treatment of massive iliac 
chondrosarcoma with personalized three-dimensional printed tantalum implant: a 
case report and literature review. J Int Med Res 2020;48(10). https://www.ncbi. 
nlm.nih.gov/pubmed/33050744 .
[18] Leung CLA, Marussi S, Atwood RC, Towrie M, Withers PJ, Lee PD. In situ X-ray 
imaging of defect and molten pool dynamics in laser additive manufacturing. Nat 
Commun 2018;9(1):1355. https://doi.org/10.1038/s41467-018-03734-7 .
[19] Mishurova T, Artzt K, Haubrich J, Requena G, Bruno G. New aspects about the 
search for the most relevant parameters optimizing SLM materials. Addit Manuf 
2019;25:325 – 34. https://doi.org/10.1016/j.addma.2018.11.023 .
[20] Zhou L, Yuan T, Li R, Tang J, Wang G, Guo K. Selective laser melting of pure 
tantalum: densification, microstructure and mechanical behaviors. Mater Sci Eng A 
2017;707:443 – 51. https://doi.org/10.1016/j.jmatprotec.2003.11.051 .
[21] Song C, Deng Z, Zou Z, Liu L, Xu K, Yang Y. Pure tantalum manufactured by laser 
powder bed fusion: influence of scanning speed on the evolution of microstructure 
and mechanical properties. Int J Refract Met Hard Mater 2022;107. https://doi. 
org/10.1016/j.ijrmhm.2022.105882 .
[22] Aliyu AAA, Poungsiri K, Shinjo J, Panwisawas C, Reed RC, Puncreobutr C, et al. 
Additive manufacturing of tantalum scaffolds: processing, microstructure and 
process-induced defects. Int J Refract Met Hard Mater 2023;112. https://doi.org/ 
10.1016/j.ijrmhm.2023.106132 .
[23] Jeyaprakash N, Saravana Kumar M, Yang C-H, Cheng Y, Radhika N, 
Sivasankaran S. Effect of microstructural evolution during melt pool formation on 
nano-mechanical properties in LPBF based SS316L parts. J Alloys Compd 2024; 
972. https://doi.org/10.1016/j.jallcom.2023.172745 .
[24] Chen H, Li W, Huang Y, Xie Z, Zhu X, Liu B, et al. Molten pool effect on mechanical 
properties in a selective laser melting 316 L stainless steel at high-velocity 
deformation. Mater Charact 2022;194. https://doi.org/10.1016/j. 
matchar.2022.112409 .
[25] Gu D, Shi Q, Lin K, Xi L. Microstructure and performance evolution and underlying 
thermal mechanisms of Ni-based parts fabricated by selective laser melting. Addit 
Manuf 2018;22:265 – 78. https://doi.org/10.1016/j.addma.2018.05.019 .
[26] Guo Y, Liao H, Chang C, Yan X, Deng Z, Dong D, et al. Effects of solute atoms re- 
dissolution on precipitation behavior and mechanical properties of selective laser 
melted Al – Mg-Sc-Zr alloys. Mater Sci Eng A 2022;854:143870. https://doi.org/ 
10.1016/j.msea.2022.143870 .
[27] Dai D, Gu D. Influence of thermodynamics within molten pool on migration and 
distribution state of reinforcement during selective laser melting of AlN/AlSi10Mg 
composites. Int J Mach Tool Manu 2016;100:14 – 24. https://doi.org/10.1016/j. 
ijmachtools.2015.10.004 .
[28] Li Y, Zalo ˇznik M, Zollinger J, Dembinski L, Mathieu A. Effects of the powder, laser 
parameters and surface conditions on the molten pool formation in the selective 
laser melting of IN718. J Mater Process Technol 2021;289. https://doi.org/ 
10.1016/j.jmatprotec.2020.116930 .
[29] Wen S, Li S, Wei Q, Yan C, Zhang S, Shi Y. Effect of molten pool boundaries on the 
mechanical properties of selective laser melting parts. J Mater Process Technol 
2014;214(11):2660 – 7. https://doi.org/10.1016/j.jmatprotec.2014.06.002 .
[30] Yang Z, Zhu J, Lu B, Liu Y, Shi W, Liu M, et al. Powder bed fusion pure tantalum 
and tantalum alloys: from original materials, process, performance to applications. 
Opt Laser Technol 2024;177:111057. https://www.sciencedirect.com/science/ 
article/pii/S0030399224005152 .
[31] Qin F, Shen Z, Shi Q, Zhou G, Yao D, Zhao Y, et al. Effect of processing parameters 
on microstructure and mechanical properties of Ta prepared by selective laser 
melting. Rare Metal Mater Eng 2023;09(52):3026 – 36. https://doi.org/10.12442/j. 
issn.1002-185X.20230031 .
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
324

## Page 15

[32] Chen C, Li Y, Zhang M, Wang X, Zhang C, Jing H. Effect of laser processing 
parameters on mechanical properties of porous tantalum fabricated by laser multi- 
layer micro-cladding. Rapid Prototyp J 2017;23(4):758 – 70. https://doi.org/ 
10.1108/RPJ-05-2014-0068 .
[33] Yadroitsev I, Krakhmalev P, Yadroitsava I, Johansson S, Smurov I. Energy input 
effect on morphology and microstructure of selective laser melting single track 
from metallic powder. J Mater Process Technol 2013;213(4):606 – 13. https://doi. 
org/10.1016/j.jmatprotec.2012.11.014 .
[34] Han L, Liou FW, Musti S. Thermal behavior and geometry model of melt pool in 
laser material process. J Heat Transf 2005;127(9):1005 – 14. https://doi.org/ 
10.1115/1.2005275 .
[35] Ding L, Liu J, Tan S, Zhang Y, Fan C, Gomes S, et al. A novel layer-based 
optimization method for stabilizing the early printing stage of LPBF process. 
Virtual Phys Prototyp 2024;19(1):e2325578. https://doi.org/10.1080/ 
17452759.2024.2325578 .
[36] Yan X, Chang C, Dong D, Gao S, Ma W, Liu M, et al. Microstructure and mechanical 
properties of pure copper manufactured by selective laser melting. Mater Sci Eng A 
2020;789:139615. https://doi.org/10.1016/j.jmst.2020.09.031 .
[37] Bruce D, Paradise P, Saxena A, Temes S, Clark R, Noe C, et al. A critical assessment 
of the Archimedes density method for thin-wall specimens in laser powder bed 
fusion: measurement capability, process sensitivity and property correlation. 
J Manuf Process 2022;79:185 – 92. https://doi.org/10.1016/j.jmapro.2022.04.059 .
[38] Cheng Y, Wang G, Qiu Z, Zheng Z, Zeng D, Tang X, et al. Multi-physics simulation 
of non-equilibrium solidification in Ti-Nb alloy during selective laser melting. Acta 
Mater 2024;272:119923. https://doi.org/10.1016/j.actamat.2024.119923 .
[39] Yan W, Ge W, Qian Y, Lin S, Zhou B, Liu WK, et al. Multi-physics modeling of 
single/multiple-track defect mechanisms in electron beam selective melting. Acta 
Mater 2017;134:324 – 33. https://doi.org/10.1016/j.actamat.2017.05.061 .
[40] Leitner M, Schr ¨oer W, Pottlacher G. Density of liquid tantalum and estimation of 
critical point data. Int J Thermophys 2018;39(11). https://doi.org/10.1007/ 
s10765-018-2439-3 .
[41] Ayyad A, Atawneh M. Surface tensions of undercooled liquids aluminum, tantalum, 
tungsten and niobium. Phys Chem Liq 2022;60(5):778 – 85. https://doi.org/ 
10.1080/00319104.2022.2053974 .
[42] Rai R, Elmer JW, Palmer TA, DebRoy T. Heat transfer and fluid flow during 
keyhole mode laser welding of tantalum, Ti – 6Al – 4V, 304L stainless steel and 
vanadium. J Phys D Appl Phys 2007;40(18):5753 – 66. https://doi.org/10.1088/ 
0022-3727/40/18/037 .
[43] Ntonti E, Sotiriadou S, Assael MJ, Huber ML, Wilthan B, Watanabe M. Reference 
correlations for the density and thermal conductivity, and review of the viscosity 
measurements, of liquid titanium, zirconium, hafnium, vanadium, niobium, 
tantalum, chromium, molybdenum, and tungsten. Int J Thermophys 2024;45(2). 
https://doi.org/10.1007/s10765-023-03305-z .
[44] Zhou X, Liu X, Zhang D, Shen Z, Liu W. Balling phenomena in selective laser melted 
tungsten. J Mater Process Technol 2015;222:33 – 42. https://doi.org/10.1016/j. 
jmatprotec.2015.02.032 .
[45] Gao F, Sonin AA. Precise deposition of molten microdrops: the physics of digital 
microfabrication. Proc R Soc Lond A Math Phys Sci 1994;444(1922):533 – 54. 
https://doi.org/10.1098/rspa.1994.0037 .
[46] Chia HY, Wang L, Yan W. Influence of oxygen content on melt pool dynamics in 
metal additive manufacturing: high-fidelity modeling with experimental 
validation. Acta Mater 2023;249. https://doi.org/10.1016/j. 
actamat.2023.118824 .
[47] Guo C, Xu Z, Zhou Y, Shi S, Li G, Lu H, et al. Single-track investigation of IN738LC 
superalloy fabricated by laser powder bed fusion: track morphology, bead 
characteristics and part quality. J Mater Process Technol 2021;290. https://doi. 
org/10.1016/j.jmatprotec.2020.117000 .
Z. Yang et al. Journal of Manufacturing Processes 144 (2025) 311–325 
325
