# Additive-manufacturing-of-tungsten-using-directed-energ_2021_Surface-and-Coa

<!-- source: D:\总文献\Additive-manufacturing-of-tungsten-using-directed-energ_2021_Surface-and-Coa.pdf -->
<!-- file_sha256: 2831c167a7b610a818325d2dcf8c4053a4ffe1e8286268c04baaeb08037db723 -->

## Page 1

Surface & Coatings Technology 409 (2021) 126884
Available online 21 January 2021
0257-8972/© 2021 Elsevier B.V. All rights reserved.
Additive manufacturing of tungsten using directed energy deposition for 
potential nuclear fusion application 
Jichang Xie
a , 1
, Haifei Lu
b , 1
, Jinzhong Lu
b , *
, Xinling Song
a
, Shikai Wu
c
, Jianbo Lei
a , ** 
a
Laser Technology Institute, Tiangong University, Tianjin 300387, China 
b
School of Mechanical Engineering, Jiangsu University, Zhenjiang 212013, China 
c
Beijing Engineering Research Center of Laser Technology, Beijing University of Technology, Beijing 100124, China 
ARTICLE INFO 
Keywords: 
Tungsten 
Nuclear fusion 
Directed energy deposition 
Microstructure 
Thermal conductivity 
ABSTRACT 
Building better nuclear fusion equipment with reduced cost is important for a sustainable society. In this study, 
pure tungsten is deposited on different steel substrates by directed energy deposition (DED). Specifically, the 
deposited layers with graded tungsten content by low and high laser scanning speed are fabricated. In addition, 
the processing parameters were optimized by analyzing the microstructure, phases and defects. Results show that 
the 9-layer sample (3000 W @ 3000 mm/min) exhibits a better thermal performance, which the thermal con -
ductivity is about 73.75 W/(m ⋅ K) at room temperature and 147.45 W/(m ⋅ K) at 900 
◦
C, respectively. Finally, the 
surface of the manufactured thick deposited layer by high-low combined laser scanning speed can reach a high 
tungsten content of up to 99.78 wt%. It is believed that the additive manufacturing of pure tungsten by DED can 
combine the advantages of tungsten and steel substrates, and simplify the manufacturing process of thermo- 
nuclear fusion devices. 
1. Introduction 
As a crucial module of thermonuclear facility (such as ITER [ 1 ]), 
divertor could remove helium ash from plasma reaction [ 2 ] and the 
contaminants caused by the interaction between plasma and Plasma- 
Facing Materials (PFMs) [ 3 ] in the harsh environment, such as high 
energy (14 MeV) neutrons irradiation and high-heat-flux. In order to 
keep long-term stable operation of divertor, tungsten, as one of the PFMs 
[ 4 ], is usually used as an armour to covered on divertor due to its high 
melting point (3414 
◦
C), high thermal conductivity (174 W/(m ⋅ K)), 
excellent resistance to sputtering and erosion, and mechanical proper -
ties at elevated temperature [ 5 – 8 ]. However, in the current nuclear 
fusion system, the tungsten tiles could not cover conformally and require 
machining to match the geometry. Such processing can result in high 
manufacturing cost and material waste. Furthermore, in the cooling 
phase of the tungsten tile, large tensile residual stresses are induced by 
plastic deformation acting as the driving force of the opening of the 
cracks [ 9 ]. Therefore, direct depositing of tungsten on divertor can not 
only reduce the manufacturing cost but also simplify the component 
structure. More than that, the sharp interface is replaced by a gradient 
interface could relieve the high stress concentrations and avoid delam -
ination under complex loading conditions [ 10 ], thus improving the 
service life of the equipment as the coefficient of thermal expansion 
(CTE) changes gradually, and alleviating the mismatch between tung -
sten and other supporting materials (or substrate). 
However, it is challenging to realize the additive manufacturing 
(AM) of pure tungsten on steel for the following reasons. Firstly, tung -
sten has a much higher melting point than steel substrates [ 11 ] 
(~2000 
◦
C). It means that the high energy input needed to melt tungsten 
will simultaneously melt the substrate and even evaporate it. Mean -
while, it is required to overcome the mismatch between the thermal 
expansion coefficients between tungsten and substrate. Secondly, 
tungsten has a high viscosity, poor flowability, and rapid solidification 
rate due to its high thermal conductivity. These characteristics can easily 
cause balling phenomena and cavities during laser processing [ 12 ]. 
Thirdly, tungsten tends to be oxidized during processing, resulting in 
impurity, dewetting and porosity. Furthermore, tungsten has a vital 
issue of natural brittleness, which can cause serious cracks [ 13 ]. 
As a versatile technology, laser additive manufacturing (LAM) pro -
vides an effective approach for complex structure cladding and 3D 
* Correspondence to: J. Lu, Xuefu Road 301, Jingkou District, Zhenjiang 212013, PR China . 
** Correspondence to: J. Lei, BinShuiXi Road 399, XiQing District, Tianjin 300387, PR China. 
E-mail addresses: blueesky2005@163.com (J. Lu), ljbtj@163.com (J. Lei). 
1 
Both authors contributed equally to this work. 
Contents lists available at ScienceDirect 
Surface & Coatings Technology 
journal homepage: www.else vier.com/loc ate/surfcoat 
https://doi.org/10.1016/j.surfcoat.2021.126884 
Received 18 November 2020; Received in revised form 4 January 2021; Accepted 8 January 2021

## Page 2

Surface & Coatings Technology 409 (2021) 126884
2
structure fabrication. Due to the refractory properties yet wide appli -
cations of tungsten, intensive attention and efforts have been paid to 
LAM of tungsten. Zhong et al. [ 14 ] tried laser direct manufacturing to 
fabricate tungsten and tungsten alloy, but pure tungsten was only 
partially melted and could not build up. Zhang et al. [ 15 ] used selective 
laser melting (SLM) to fabricate nanocrystalline tungsten; however, only 
partial melting of tungsten was achieved. A complex collimator was 
successfully fabricated using SLM [ 16 ]; however, the influence of laser 
processing on the microstructure was missing. Balling phenomena were 
systematically studied in SLM of tungsten [ 12 ]; however, the 3D printed 
tungsten samples were rough. In a followed study, the authors signifi -
cantly improved the manufacturing quality of the printed sample by 
changing the powder morphology from polyhedral to spherical [ 17 ]. 
Further optimization can be conducted to get denser tungsten without 
significant balling or macrocracks [ 18 ]. Enneti et al. [ 19 ] also tried the 
SLM method to fabricate pure tungsten samples. However, no clear 
metallurgical bonding was formed between layers, and there were many 
un-melted or partially melted particles. It indicates that the energy 
density was not enough to melt tungsten. A higher energy density input 
can improve the melting, but can also generate cracks [ 13 , 20 ]. Recently, 
high-density tungsten with good mechanical and thermal conductivity 
was fabricated using SLM [ 21 ]. 
Compared with SLM [ 22 ], directed energy deposition (DED) using a 
laser beam offers higher flexibility, which can fabricate full density and 
functionally graded materials directly on similar or dissimilar substrates 
conformally [ 10 , 23 ]. DED is preferable in rapid manufacturing, clad -
ding, repair [ 24 , 25 ], and the modification of metallic components, 
especially on large parts that are beyond the capability of powder-bed- 
based SLM. 
However, by now, limited reports were available about DED of pure 
tungsten [ 14 ]. Several studies have been performed using DED for 
tungsten alloys manufacturing [ 26 – 28 ]. Nevertheless, the complete 
melting of tungsten powders is still very challenging; meanwhile, 
porosity and cracks can cause serious problems and need to be opti -
mized. Recently, Jeong et al. [ 29 ] conducted DED of pure tungsten to 
fabricate 3D structure; however, the surface finish was not smooth, and 
there was no detailed understanding of microstructure. Thus, it will be 
of great importance to systematically study the relationship between 
laser processing parameters and the microstructures of pure tungsten 
using DED. On the other hand, lots of efforts although have been devoted 
to exploring the application of tungsten (or tungsten alloys) through AM, 
direct depositing pure tungsten on steel substrates has not been studied. 
In this study, the processing parameters in relation to microstructure, 
microhardness, thermal preformance, defectsgeneration, and micro -
structural evolution mechanism were systematically investigated to 
optimize the manufacturability of pure tungsten. Finally, a promising 
tungsten content of 99.78 wt% was fabricated by DED using laser beam 
with a coaxial powder feeding system. It is believed that the results 
obtained from this study could provide a fundamental understanding for 
LAM of pure tungsten. 
2. Materials and methods 
2.1. Materials 
The substrates were reduced activation ferritic/martensitic (RAFM) 
steel [ 30 ] (CLF-1 steel) (300 × 70 × 10 mm) and 45# carbon steel (150 
× 150 × 20 mm). The chemical compositions (in wt%) of CLF-1 are 
0.088% C, 8.54% Cr, 1.34% W, 0.62% Mn, 0.29% V, 0.14% Ta, 0.021% 
N, 0.0058% Ni, 0.0011% S and balance Fe; and the chemical composi -
tions (in wt%) of 45 # carbon steel are 0.43% C, 0.66% Mn, 0.014% S, 
0.002% P, 0.23% Si and balance Fe. The pure tungsten powders used in 
this study were polygonal particles (as shown in Fig. 1 a) with a size 
between 20 and 150 μ m (indicated in Fig. 1 b). 
2.2. Methods 
An LDM-8060 DED system (Raycham, China) was used for LAM of 
pure tungsten. The system is shown in Fig. 2 , which includes laser 
(Laserline LDF 10000 – 100, Germany), three-axis numerical control 
working table, and a powder feeder. The experiment was carried out in 
an argon vacuumed chamber atmosphere (oxygen content < 50 ppm). 
The distance between the coaxial laser head and the substrate was 15 
mm. Based on our preliminary results, the carrier gas flow rate and 
powder feeding rate were set at 10 L/min, and 29.3 g/min, respectively. 
The laser processing parameters for single- and multiple-track samples 
are listed in Tables 1 and 2 , respectively. In addition, the hatch space of 
multiple-track samples was 1.5 mm (the diameter of the laser spot was 3 
mm). 
The tungsten powder and deposited samples were characterized by 
optical microscope (Leica DVM6A), scanning electron microscope (SEM) 
(ZEISS Sigma 300 equipped with X-ray energy-dispersive spectrometer 
(EDS)) and transmission electron microscope (TEM) (JEOL JEM-2100). 
X-ray diffraction (XRD, D/MAX-2500) was used to analyze the phases of 
the deposited samples (Cu source, 40 kV, 140 mA). 
An HV-1000 Vickers digital microhardness tester was used to mea -
sure the in-depth microhardness of all deposited samples, with a load of 
1.96 N and a dwell time of 10 s. The space between each test point was 
100 μ m. 
The thermal conductivity ( λ ) of the deposited sample was calculated 
from the thermal diffusivity ( α ), specific heat ( C
p
), and density ( ρ ) using 
the following formula [ 31 ]: 
Fig. 1. (a) SEM image of the pure tungsten powder, and (b) the size distribution of the tungsten powder. 
J. Xie et al.

## Page 3

Surface & Coatings Technology 409 (2021) 126884
3
λ = α ⋅ C
p
⋅ ρ (1) 
The thermal diffusivity of sandpaper-polished (#400) sample with 
12.7 mm in diameter was determined by a laser flash apparatus (Netzsch 
LFA 427, Germany) using the Cape and Lehman method. For Sample 4 
(4.4 mm in thickness), the thickness of the sample in the laser flash 
measurement is 2 mm, which selected from the upper part of the 
deposited layer. For others, a piece of sample was cut down and worn 
until the interface between the deposited layer and substrate disappear, 
and then test the remained deposited layer. The specific heat was 
measured by a thermal analyzer (Netzsch DSC 200 F3, Germany) with a 
sample dimension of 2 × 2 × 2 mm
3 
(if the thickness thinner than 2 mm, 
the samples were prepared as the sample of laser flash measurement). 
The thermal diffusivity data were corrected using Azumi and Takaha -
shi ’ s method [ 32 ] to decrease the finite pulse effect. The density was 
measured using the Archimedes ’ principle. The testing temperatures 
were in the range of room temperature (RT) to 900 
◦
C. 
3. Results and discussion 
3.1. Macro-morphology of single- and multiple-track samples 
Fig. 3 shows the macro-morphology of the single- and multiple-track 
samples prepared by DED with different processing parameters (power, 
scanning speed, and layer number). As shown in Fig. 3 a, the continuous 
and uniform single-track deposited layers exhibit silver-white metallic 
luster. With the increase of laser power or the decrease of scanning 
speed, the width of single-track sample increases. 
For the multiple-track samples ( Figs. 3 c-e), a smooth surface finish 
was successfully deposited without any obvious balling, cracks, or pores. 
Nevertheless, a little roughness surface formed in the thick deposited 
layer (~4.4 mm), as shown in Fig. 3 f, due to un-optimized processing 
parameters. It should be noted that with the increase of thickness, the 
tungsten content gradually increases to very close to pure tungsten in the 
underlying deposited layer. This change (content of tungsten) makes the 
melting of the underlying layer difficult and causes the molten pool to 
become smaller. Therefore, 1.5 mm hatch space is not enough to meet 
overlap between adjacent single-track samples and causing the rough -
ness surface of thick deposited layer. 
3.2. Microstructure and microhardness of the single-track samples 
3.2.1. Microstructure 
To understand the influence of laser processing parameters on the 
morphologies and microstructures of DEDed pure tungsten, the cross- 
sections (Y-Z plane in Fig. 3 d, the same as below) of single-track sam -
ples were characterized by SEM. It is indicated in Figs. 4 and 5 that at a 
fixed speed of 400 mm/min, with the increase of laser power, the width 
of the sample gradually increases from 3.8 to 6.0 mm; meanwhile, the 
depth of the molten pool, the depth of the heat-affected zone (HAZ), and 
the height of the sample increase. 
On the other hand, with the increase of scanning speed, the width, 
height, depth of the molten pool and the HAZ of the sample decrease. 
Overall, relatively smooth and uniform deposited layers were realized at 
the millimeter scale with limited pores and cracks. It should be noted 
that there is a big difference between the melting point of pure tungsten 
and the CLF-1 steel substrate. Thus, a sufficient energy density to melt 
tungsten but without vaporizing of CLF-1 steel is needed. In this section, 
it is found that increasing the energy density (increase of laser power or 
Fig. 2. (a) Schematic diagram, and (b) photo of directed energy deposition system. 
Table 1 
Processing parameters for the single-track samples (
○ 
represents the selected 
parameters). 
Scanning speed (mm/min) Laser power(W) 
2000 2500 3000 3500 4000 
200 ○ 
300 ○ 
400 ○ ○ ○ ○ ○ 
500 ○ 
600 ○ 
Table 2 
Processing parameters for the multiple-track samples. 
Sample NO. of layers Power 
(W) 
Scanning speed 
(mm/min) 
1 1 3000 300 
2 2 3000 300 
3 9 3000 3000 
4 1 – 3 3000 3000 
4 4000 540 
5 – 11 3500 540 
J. Xie et al.

## Page 4

Surface & Coatings Technology 409 (2021) 126884
4
decrease of scanning speed) results in a wider and thicker deposited 
layer. 
In order to reveal the microstructure of lowest energy input cases in 
Fig. 4 , the cross-sectional SEM images with higher magnification are 
presented in Fig. 6 . Some scattered pure tungsten particles are observed 
in Fig. 6 a, which are relatively large and partially melted particles. 
Fig. 6 b shows a magnified image of an un-melted (bottom one) and 
nearly completely melted or re-solidified tungsten particle (top one). It 
is inferred that the un-melted particles are partially melted particles 
based on the interfacial area around these particles. Higher magnifica -
tion images shown in Fig. 6 c indicate that the melted tungsten has fused 
together with its surrounding materials, which is further confirmed by 
EDS analysis of Points 1 and 2 (listed in Table 3 ). However, due to the 
high thermal conductivity and viscosity, the melted tungsten has limited 
diffusion time before solidification. The melted particle is not able to 
spread out, which is isolated from the matrix. Also, few tiny un-melted 
tungsten domains are observed (as indicated in Fig. 6 c), embedded in 
acicular microstructures. In addition to these, the majority of the sample 
shows smooth areas, such as Areas 1 – 4 (labeled in Fig. 6 a), where 
tungsten is uniformly distributed in the deposited layer. Such results 
indicate that most of the tungsten particles have been completely melted 
during DED. Furthermore, a slightly higher energy input case with a 
laser power of 3000 W and a scanning speed of 600 mm/min is also 
presented in Figs. 6 d-f to check the melting and diffusion of tungsten 
particles, showing less un-melted pure tungsten particles. Acorrding to 
the EDS results of Areas 5 – 8 (labeled in Fig. 6 d), tungsten is also uni -
formly distributed in the deposited layer, which is less than that in Areas 
1 – 4. Higher magnification images shown in Figs. 6 e & f indicate that a 
better melting and fusion is achieved with less color contrast with the 
surrounding matrix. Thus, it is believed that power higher than 2000 W 
(scanning speed at 400 mm/min) or speed lower than 600 mm/min 
(laser power at 3000 W) will be enough to melt the tungsten particles. 
3.2.2. Microhardness 
In this section, the influence of the laser processing parameter on the 
tungsten content and the microhardness of the deposited layer is stud -
ied. Fig. 7 a shows that at a laser power of 3000 W, with the increase of 
scanning speed, the content of tungsten first increases and then de -
creases. Similarly, at a scanning speed of 400 mm/min, with the increase 
of laser power, the content of tungsten first increases (until 3500 W), 
then decreases. 
Here, the dynamic viscosity ( μ ) of the melten pool can be calculated 
as [ 33 ]: 
μ =
16 γ
15
̅̅̅̅̅̅̅ ̅
m
k
B
T
√
(2) 
where γ is the surface tension of the melten pool, m is the atomic mass, k
B 
is the Boltzmann constant, and T is the temperature of the molten pool. 
Accompanied by the increases of laser power to 3500 W, the tempera -
ture of the molten pool also increases, which leads to the decrease of the 
dynamic viscosity ( μ ) of the composite melt. A lower dynamic viscosity 
increases the convection of molten pool, and allows more tungsten 
particles to enter the molten pool and form high tungsten content. On 
the other hand, to some extent, with the increasing laser energy input, 
the molten pool becomes wider, causing more tungsten powders to enter 
the molten pool; however, if the size of molten pool is lager than that of 
powder flow (as shown in Fig. 2 a), the percentage of tungsten will 
decline. Therefore, as the laser power further increases to 4000 W, the 
percentage of tungsten in the deposited layer reduces. This phenomenon 
should be attributed to the higher dilution rate during DED. As shown in 
Fig. 5 a, with the increase of laser power, the size of the molten pool (and 
HAZ) increases; however, with a constant and limited power feeding 
rate, the same amount of tungsten will be diluted more. Thus, at a given 
powder feeding rate, after reaching a threshold laser power, the tung -
sten content will decrease with a further increase of laser power. 
Similarly, the scanning speed also affects the depth of the molten 
pool and HAZ (shown in Fig. 5 b), which will also affect the tungsten 
content. Excessive dilution can happen with very low scanning speed 
(such as 200 mm/min) due to the large and deep molten pool. Thus, the 
maximum tungsten content is achieved at a scanning speed of 300 mm/ 
min rather than the lowest scanning speed. However, with a further 
increase in scanning speed, the tungsten content decreases rapidly. It is 
because the higher scanning speed reduces the number of tungsten 
Fig. 3. Photograph of the single- and multiple-track samples with different processing parameters. Single-track with (a) different laser power (2000 to 4000 W @ 
400 mm/min) and (b) different scanning speed (200 to 600 mm/min @ 3000 W) on CLF-1 steel; (c) Single-layer (Sample 1) and (d) double-layer (Sample 2) (3000 W 
@ 300 mm/min) on CLF-1 steel; (e) 9 layers (3000 W @ 3000 mm/min) on CLF-1 steel; (f) 11 layers on 45# carbon steel. 
J. Xie et al.

## Page 5

Surface & Coatings Technology 409 (2021) 126884
5
particles received in per unit area. 
The corresponding microhardness presented in Fig. 7 b shows that 
with a scanning speed of 400 mm/min, the microhardness correlates 
positively with the tungsten content. With a laser power of 3000 W and 
speed ≤ 400 mm/min, the change of microhardness is similar to the 
tungsten content. However, with high speed (500 and 600 mm/min), a 
lower content of tungsten shows higher microhardness. This might 
result from the refined grain caused by fast scanning speed. Conse -
quently, the fine grains strengthen the deposited layer, resulting in 
higher microhardness [ 34 ]. 
Fig. 4. The cross-sectional SEM images (Y-Z plane in Fig. 3 d, the same as below) of single-track samples with different laser powers at a scanning speed of 400 mm/ 
min and different scanning speeds at a laser power of 3000 W. (The definitions of width, height, and depth are indicated in (a), the same below.) 
J. Xie et al.

## Page 6

Surface & Coatings Technology 409 (2021) 126884
6
Based on the above analysis, it can be concluded that in the single- 
tracksamples, a higher tungsten content is beneficial to the improve -
ment of the microhardness. Also, the microhardness of the deposited 
layer is related to the size of the crystal grain. A relatively high cooling 
rate can refine the grains and increases the microhardness. Thus, the 
laser power of 3000 W and a scanning speed of 300 mm/min were 
selected for multiple-track samples(Samples 1 and 2). 
3.3. Microstructure, phases and microhardness of multiple-track samples 
prepared by low laser scanning speed 
3.3.1. Microstructure and phases 
In this section, the microstructure of multiple-track samples is 
investigated. First, the morphologies of single- and double-layer 
deposited layers are compared, as shown in Fig. 8 . In the low magnifi -
cation image, there is no obvious difference between single-track and 
single-layer deposited layers ( Fig. 8 a). However, in the double-layer 
deposited layer, many un-melted or partially melted tungsten particles 
appear after the deposition of the second layer, as indicated in Fig. 8 b. It 
is noticed that the measured thickness of the single-layer deposited layer 
is about 1.7 mm (including the melted substrate), while the double-layer 
deposited layer is only ~0.6 mm thicker than the single-layer one. Such 
a difference is caused by the easy melting of CLF-1 steel substrate and 
accompanied dilution of the tungsten during the deposition of the first 
layer. However, during the deposition of the second layer, since the prior 
layer is a mixture of tungsten, CLF-1 steel and some intermetallic com -
pounds, the melting and dilution are limited. Thus, the measured 
Fig. 5. The influence of (a) laser power and (b) scanning speed on the morphology of single-track samples. 
Fig. 6. The cross-sectional SEM images of single-track samples. (a-c) The lowest power (2000 W) at 400 mm/min and (d-f) fastest speed (600 mm/min) at 3000 W; 
(a)(d) overviews, and (b)(c)(e)(f) the magnified images of nearly completely melted or re-solidified tungsten particle. 
Table 3 
EDS analysis of the labeled areas in Fig. 6 (laser power of 2000 W, scanning 
speed of 400 mm/min) (wt%). 
Cr Fe W Cr Fe W 
Area 1 7.51 72.09 20.39 Area 5 8.19 79.54 12.27 
Area 2 7.09 68.96 23.95 Area 6 7.75 77.83 14.42 
Area 3 7.23 70.75 22.02 Area 7 8.04 78.38 13.57 
Area 4 7.41 70.89 21.70 Area 8 8.31 78.44 13.25 
Point 1 6.10 57.07 36.83 Point 2 5.28 39.97 54.76 
J. Xie et al.

## Page 7

Surface & Coatings Technology 409 (2021) 126884
7
thickness of the double-layer deposited layer is less than twice of the 
thickness of the single-layer one. With the increase of thickness (as well 
as the tungsten percentage), the diffusion of tungsten keeps reducing, 
while the heat accumulates, leading to the sufficient melting of tungsten. 
Therefore, in the second layer of double-layer deposited layer, dendritic 
crystals due to recrystallization dominate with scattered tungsten-rich 
Fig. 7. The influence of laser power and scanning speed on the (a) tungsten content and (b) microhardness of single-track samples. 
Fig. 8. The cross-sectional SEM images of multiple-track samples. (a) Sample 1 (single-layer), (b) Sample 2 (double-layer), (c)(e)(g) top, middle and bottom areas of 
Sample 1, and (d)(f)(h) top, middle and bottom areas of Sample 2. 
J. Xie et al.

## Page 8

Surface & Coatings Technology 409 (2021) 126884
8
particles. On the microscopic scale, the double-layer deposited layer 
shows denser tungsten particles, distributed throughout the cross- 
section. 
Side by side comparison of single- and double-layer deposited layers 
at different locations (top, middle, and bottom) is presented in Figs. 8 c- 
h. Both cases show some un-melted and partially melted tungsten par -
ticles. Noteworthy, in the top area, a thin layer of tungsten particles is 
presented in Fig. 8 d-i, which is different from the single-layer deposited 
layer. As indicated by EDS analysis in Areas 1 of Fig. 8 a and Areas 5 of 
Fig. 8 b, by depositing the second layer, the tungsten content near the top 
area increases from 46.79 wt% to 83.9 wt%. It is believed that the high 
viscosity and poor flowability of tungsten [ 12 ] lead to the concentration 
of tungsten particles. Meanwhile, a significant amount of dendritic 
crystals form in the top and middle areas of the double-layer deposited 
layer; likewise, more small grains develop near the bottom area, as 
shown in Figs. 8 d, f & h. Figs. 8 c-h shows that the deposition of the second 
layer not only increases the percentage of tungsten but also enhances the 
dendritic crystals formation and growth (in the middle and top area). 
Compared with the double-layer deposited layer, the single-layer one 
has less dendritic crystals and unmelted tungsten powder, and its second 
phase exists in the form of lamellar submicron particles. 
It is shown Areas 1 – 4 in Fig. 8 a that the distribution of tungsten is 
relatively uniform in single-layer deposited layer with a percentage of 
about 45 wt%. However, a clear gradient distribution is observed in the 
double-layer deposited layer, with tungsten percentage increasing from 
the bottom (57.65 wt%) to top (83.9 wt%) (Areas 5 – 9 in Fig. 8 b), which 
indicates with the increasing number of deposited layer, the tungsten 
content increases. 
In order to evaluate the diffusion of tungsten and the interface be -
tween tungsten and matrix, the EDS line scan and TEM characterization 
were conducted. Figs. 9 a & b present the interface of randomly selected 
areas at the edge of tungsten particles in single- and double-layer 
deposited layers, respectively. From the outside to inside ( Fig. 9 a), 
tungsten first gradually increases and then jumps at the boundary 
(indicated by the dashed line); meanwhile, Fe and Cr gradually decrease 
until indetectable at the boundary. This change indicates that these 
tungsten particles are partially melted and have diffused into the sur -
rounding matrix. Two phases of gray present at the edge of the tungsten 
particle ( Fig. 9 b), and higher contents of Fe and Cr are detected in the 
peripheral gray phase. It is hypothesized that the Fe and Cr reacted with 
the partially melted tungsten particles during DED, gradually diffused 
into the un-melted tungsten particles and forming a new phase. The 
corresponding TEM image of the tungsten particle and surrounding 
matrix is shown in Fig. 9 c, where a clear difference can be observed in 
and outside of the tungsten particle. The element distribution can be 
roughly inferred based on the contrast, where the white (Point 1) and 
gray (Point 2) areas are dominated by Fe and W, respectively. Based on 
the SAED patterns in Fig. 9 c, the calculated lattice constants are 0.287 
and 0.316 nm, respectively, which are identical to the previously re -
ported lattice constant of Fe and W. Further, the EDS analysis of Points 1 
and 2 shown in Figs. 9 d & e, give a quantitative amount of each element. 
Thus, the phases in Points 1 and 2 are Fe and W, respectively, confirming 
the above speculation. A high-resolution TEM image ( Fig. 9 f) at the edge 
of the tungsten particle shows the transition from crystalline to amor -
phous Fe dominated matrix, where the d-space is 0.889 nm, indicating a 
potential phase of Fe
7
W
6
. 
Further, the sub-micro precipitates are examined to determine its 
composition. Fig. 10 a shows lamellar tungsten-rich phase embedding in 
the CLF-1 steel matrix, which corresponds to the dark particles in the 
TEM image shown in Fig. 10 b. The bright-field image shows a clear 
contrast between precipitates and matrix. The SAED pattern in Fig. 10 b 
reveals the existence of Fe
7
W
6 
and some other content, which is also 
confirmed by EDS analysis (Table in Fig. 10 d). Further, a higher 
magnification bright-field TEM image ( Fig. 10 c) reveals the existence of 
different phases or grain orientations in the precipitate consisted of 
Fe
7
W
6
-Fe-Cr. Therefore, in the DED process, tungsten particles first melt 
with the substrate and then solidify into little tungsten particles or 
intermetallic precipitates. 
XRD patterns of the multiple-track samples shown in Fig. 11 indicate 
that the main phases in the single- and double-layer deposited layers are 
Fe, W, Fe
7
W
6 
and Fe
–
Cr (i.e. Cr
0.26
Fe
1.74
). It is found that the peak 
intensity at 40.27
◦
, 58.26
◦
and 73.20
◦
significantly increases from 
single-layer sample to double-layer sample, indicating a higher content 
of tungsten. In contrast, the diffraction peaks of Fe
–
Cr (e.g. 44.49
◦
) and 
Fe
7
W
6 
(e.g. 37.93
◦
) in the double-layer sample are slightly lower than 
those of the single-layer one. Also, some of the peaks disappeared (be -
tween 95 and 99
◦
), indicating the decrease of contents in the double- 
layer sample, which is consistent with the EDS results in Fig. 8 . It can 
be inferred that with the increasing thickness of deposited layer, the 
tungsten content will increase, while other elements decrease. It is 
believed that with the decrease of dilution rate, the deposition of pure 
tungsten can be obtained eventually. 
Fig. 9. EDS line scanning of the edge of un-melted tungsten particles in (a) single-layer and (b) double-layer deposited layers, and (c-f) TEM images of the edge of the 
un-melted tungsten particle and EDS analysis of Points 1 and 2. 
J. Xie et al.

## Page 9

Surface & Coatings Technology 409 (2021) 126884
9
3.3.2. Microhardness 
In this section, the microhardness of single- and double-layer sam -
ples is characterized. As displayed in Fig. 12 , the microhardness of both 
single- and double-layer samples share similar trends in the HAZ with 
relatively smooth transition; however, a large fluctuation is observed in 
the deposited area. The deposited layer shows higher microhardness 
than the substrate. Especially the double-layer sample shows ~2.6 times 
higher microhardness than the substrate with a maximum value of 708 
HV
0.2
. A sharp jump of microhardness is observed for single-layer 
sample, which can result from the unmelted tungsten particle. Simi -
larly, some dip can be seen in the double-layer sample due to the 
existence of the matrix. Further away from the interface, the double- 
layer sample exhibits a significantly higher microhardness than that of 
the single-layer one. Such change is consistent with the microstructure 
observed in Fig. 8 . 
3.4. Analysis of defects 
3.4.1. Cracks in the single-track sample 
Representative cracks observed in the deposited layer are analyzed 
in this section. Fig. 13 a shows the crack starts from the interface area 
between substrate and deposited layer, and gradually extends towards 
Fig. 10. (a)(b) SEM and TEM images of lamellar precipitated phase, (c) TEM image of another precipitate, and (d) EDS analysis of Areas 1 and 2 in (b) and (c). 
Fig. 11. XRD pattern of single-layer (Sample 1) and double-layer (Sample 2) samples. 
J. Xie et al.

## Page 10

Surface & Coatings Technology 409 (2021) 126884
10
the surface of the deposited layer. A higher magnification image in 
Fig. 13 b reveals that the crack happens at the grain boundaries. Such 
crack is a typical solidification crack caused by the anisotropic 
contraction [ 23 ]. During the rapid solidification of DED, some incom -
pletely melted tungsten particles initiate crystallization as nuclei. Then 
these crystals compete with each as they grow. Before the complete 
solidification, the liquefied film resulted from low-melting-point CLF-1 
steel substrate (such as Fe and Cr) replenishes the grain boundaries [ 35 ]. 
When the contraction stress caused by different grains is higher than the 
interfacial tension, cracks tend to initiate [ 36 ]. Due to the relatively 
Fig. 12. Microhardness of single- and double-layer samples. 
Fig. 13. Representative cracks in the single-track sample. (a) The laser power of 3500 W, scanning speed of 400 mm/min, (b) the magnified image of Rectangle B in 
(a); (c) the laser power of 3000 W, scanning speed of 500 mm/min, and (d) the laser power of 3000 W, scanning speed of 300 mm/min. 
J. Xie et al.

## Page 11

Surface & Coatings Technology 409 (2021) 126884
11
weaker strength of the grain boundary [ 37 ], cracks usually propagate 
along such weak boundaries, forming transgranular cracks. 
It should be noted that the brittleness of W and Fe
7
W
6 
intermetallic 
compounds can also contribute to the crack formation [ 28 ]. It is hard to 
determine where the crack initiates exactly in this case, but it can be 
inferred that the bottom can be a favorable spot to initiate the crack. 
During DED, the bottom part (interface) tends to have a much higher 
temperature gradient and cooling rate [ 13 , 23 ], which can result in high 
residual stress, acting as the driving force for the crack formation. 
In addition to the above case, we also notice that cracks can take 
place near un-melted tungsten particles and the location where mate -
rials show distinct thermal properties, as indicated in Figs. 13 c & d. These 
two cracks are also resulted from the different thermal contractions 
[ 23 ], particularly the composition segregation in Fig. 13 d. At the 
macroscale, these factors are manifested as CTE mismatch between 
different phases in deposited layer. 
3.4.2. Crack and pore in the multiple-track sample 
To gain more understanding of the crack formation in the multiple- 
track sample, the observed cracks in the single-layer sample (Sample 
1) are analyzed in this section. Fig. 14 a shows the traces of multiple- 
track deposited layer, where big crack tends to form at the overlap 
zone as indicated by the yellow ellipses. Figs. 14 b-d shows that both 
cracks have wide openings at the top and narrow down from top to 
bottom. The cracking mechanism is very complex due to the repeated 
rapid heating and cooling. Here, the left crack is magnified to unveil 
more details. Based on the irregular and zigzag morphology shown in 
Figs. 14 b & d, it is speculated this crack is related to liquation cracking 
and cyclic thermal stresses [ 38 ]. However, it is difficult to figure out the 
initiation of the crack. It is inferred that the big solidification crack 
might result from the liquation cracking. Here, the overlap area covers 
two parts, one is the previous track, and the other one is the CLF-1 steel 
substrate. Due to the distinct CTE, the different shrinkage rates cause 
solidification cracking [ 39 ]. Interestingly, three tungsten particles with 
different phenomena exist at the top, middle, and bottom. Fig. 14 e 
shows the crack penetrating the top tungsten particle. Then, the crack 
passes around the edge of the middle tungsten particle (yellow dashed 
circle in Fig. 14 c) during its propagation. Finally, the crack stops at the 
bottom particle ( Fig. 14 d). Fig. 14 a suggests the crack potentially starts 
from the top and propagates to the bottom. Here, the crack might be the 
combinational result of high thermal stress in the overlap zone and the 
brittleness fracture of tungsten and its compounds. Further study is 
needed to reveal the exact mechanism of crack initiation and propaga -
tion in the area with complex thermal history. 
In addition, pore (or void) is also a typical defect in LAM. In this 
study, due to the rapid solidification and high viscosity of the molten 
tungsten, the vaporized elements (Fe and Cr) cannot escape by floating 
up and will be entrapped inside the deposition. Some pores can retain 
their spherical shape while some initiate cracking during solidification, 
as shown in Fig. 15 . During the processing, the gas pore resulted from 
Fig. 14. SEM image of the cracks in the single-layer sample (Sample 1). (a) Overview, and (b-e) the magnified images of cracks. (Laser power of 3000 W and scanning 
speed of 300 mm/min). 
J. Xie et al.

## Page 12

Surface & Coatings Technology 409 (2021) 126884
12
vaporization can be relatively easily controlled by reducing the energy 
input. In the coming section, since decreasing the laser power could lead 
to incompletely melting of tungsten particles during DED, increasing 
laser scanning speed is adopted as an alternative way to avoid the over- 
melting of the substrate and the forming of compounds. 
3.5. Thick deposited layer prepared by high laser scanning speed 
In this section, the feasibility of DED of thick deposited layer is 
studied using high laser scanning speed to reduce the aforementioned 
crack, pore and compounds. Fig. 16 a shows the cross-section of Sample 
3, which is about 1.15 mm thick without any pores or macro-cracks. 
Different from low scanning speed, the rapid scanning delivers less en -
ergy and powder in a given area. Thus, the molten pool is shallower, the 
cooling rate is higher, and the thickness of each layer is thinner. 
Consequently, its surface and the interface (between the deposited layer 
and substrate) are flatter than Samples 1 and 2. With a slightly higher 
magnification ( Fig. 16 b), a clear outline of particles can be observed 
throughout the deposited layer, with its density increase from the bot -
tom to top. Corresponding EDS analysis reveals the tungsten content 
increases from about 72 wt% to 96 wt%, indicating high purity of the 
tungsten part can be manufactured as the number of layers increases. 
However, due to the fast scanning speed and insufficient melting, 
there are many unmelted tungsten particles scattered in the CLF-1 steel 
matrix ( Fig. 16 f). Limited diffusion of tungsten can be observed in the 
matrix, as indicated in Fig. 16 i. With the decrease of dilution rate, the 
middle area becomes denser ( Fig. 16 e), with more tungsten particles in 
contact with each other. A higher magnification image, Fig. 16 h, shows 
that the melted tungsten particles recrystallize into many small tungsten 
particles. In the middle area, due to the accumulation of heat, more 
tungsten particles are melted. With the further accumulation of heat, 
tungsten dominates the whole area, showing shattered tungsten 
particles and recrystallized dendrites ( Figs. 16 d & g). These shattered 
particles and microcracks are formed due to the high cooling rate and 
the brittleness of tungsten. On the other hand, it indicates that the 
shattered particles do not have enough energy to melt completely and 
diffuse out of the original tungsten particle domain. Since the deposition 
mechanism of tungsten deposited layer prepared by DED is complicated, 
the further explanation is necessary. 
3.6. Microstructural evolution mechanism for DED of pure tungsten 
The schematics of microstructural evolution processes with low and 
high laser scanning speed are discussed in this section, as shown in 
Fig. 17 . During the first deposited layer, tungsten as solid powder enters 
into the molten pool of steel substrate and still keeps solid at the very 
beginning due to its high melting point. 
In the case of low laser scanning speed (300 mm/min), the temper -
ature of the molten pool will continue to rise due to heat accumulation, 
which can peel off the surface of tungsten powder and melt it. After that, 
the melting tungsten mixes with matrix elements (Fe and Cr) to form the 
lamellar submicron intermetallic compounds (Fe
7
W
6
) embedded in the 
matrix ( Fig. 10 a). In addition, some ten-micron tungsten particles also 
react with the matrix, the smaller of them turn into intermetallic com -
pounds completely ( Figs. 8 d-ii & h-ii), but the cores of the larger ones are 
still pure tungsten ( Figs. 9 b & c). Meanwhile, since the temperature of 
molten pool is very high, the cracks and pores will appear during the 
cooling process. 
On the other hand, in the case of high laser scanning speed (3000 
mm/min), the temperature of the molten pool is lower than the low laser 
scanning speed, reducing the amount of exfoliated tungsten; meanwhile, 
the shallower molten pool provides less liquid matrix so that minimizing 
the lamellar submicron intermetallic compounds. Therefore, most of the 
tungsten powders still keep their initial chemical component and 
Fig. 15. SEM image and corresponding EDS mapping of a big pore in the double-layer sample. 
J. Xie et al.

## Page 13

Surface & Coatings Technology 409 (2021) 126884
13
without any pores or macro-cracks appearing in the deposited layer 
during the cooling process. Interestingly, since the larger cooling rate in 
the surface of the molten pool [ 40 ], the tungsten powders are shattered 
and solidified immediately ( Fig. 16 g). 
3.7. Thermal properties 
Since the thermal conductivity is significant in thermo-nuclear 
fusion device, in this section, the thermal performance of the selected 
Fig. 16. SEM images and EDS results of Sample 3. (a) The image of cross-section, (b) the magnified image of Rectangle B in (a), (c) EDS result of different areas in (b), 
and the higher magnification images of top (d & g), middle (e & h) and bottom areas (f & i). 
Fig. 17. The diagram illustration of tungsten deposited on steel susbtarte by DED with low and high laser scanning speed. 
J. Xie et al.

## Page 14

Surface & Coatings Technology 409 (2021) 126884
14
samples are assessed. As shown in Table 4 , the surface of the Sample 2 
(double-layer) has a few pores, but the Sample 3 (9-layer) is compact 
and without any pores or cracks, with the number of layers increases, the 
overall density increases, but still far away from pure tungsten [ 20 ]. It is 
noticed that with the increase of temperature, the specific heat of both 
samples increases. However, the thermal diffusivity of 9-layer sample is 
much higher than that of double-layer one at all different test temper -
atures. According to Eq. (1) in Section 2.2 , the double-layer sample 
shows a thermal conductivity of 18.24 (at RT), 27.70 (at 500 
◦
C) and 
39.41 (at 900 
◦
C) W/(m ⋅ K), respectively. However, for Sample 3, a 
thermal conductivity of 73.75 W/(m ⋅ K) is obtained at RT; at a higher 
temperature, the thermal conductivity can increase up to 106.00 W/ 
(m ⋅ K) at 500 
◦
C and 147.45 W/(m ⋅ K) at 900 
◦
C, which is much higher 
than the capability of double-layer sample. 
Here, although the thermal conductivity of the DEDed samples are 
smaller than that of pure tungsten (174 W/(m ⋅ K)) [ 7 ], compared with 
double-layer sample, the performance of 9-layer sample has been greatly 
improved, which is attributed to the higher tungsten content, fewer 
defects (pores) and intermetallic compounds (Fe
7
W
6
). Therefore, it is 
foreseeable that with the further optimization of the DED process, 
deposited layer with higher thermal conductivity will be prepared and 
practically used in nuclear fusion equipment. 
3.8. Thick deposited layer prepared by high-low combined laser scanning 
speed 
Based on the above results, a scheme of high-low combined laser 
scanning speed is adopted to prepare a thicker deposited layer to meet 
the need of practical application. As shown in Fig. 18 , the DEDed sample 
(Sample 4) with 11 layers was prepared. According to aforementioned 
experiment results, the 1 – 3 layers were deposited with 3000 W and 
3000 mm/min as a transition layer. Then, we increased the laser power 
to 4000 W and decreased the scanning speed to 540 mm/min. After that, 
the laser power was found a bit high to fabricate the remaining depos -
ited layers and then it was slightly reduced to 3500 W to continue the 
DED. 
Fig. 18 a shows the overall cross-sectional microstructure of Sample 4 
(~4.4 mm). Although there are many pores and micro-cracks, no wide 
cracks are found throughout the deposited layer. It can be noticed that 
cracks are concentrated in the upper part of the sample and propagate 
among pores. According to Fig. 18 b, tungsten content in cracked areas 
are more than 90 wt%, therefore, it can be concluded that the causes of 
these cracks not only structural defects caused by pores and cyclic 
thermal stresses, but also the natural brittleness of the material caused 
by the high tungsten content. Similar to Samples 2 (double-layer) and 3 
(9-layer), the tungsten shows a gradient distribution from bottom 
(72.94 wt%) to top (99.78 wt%). Nevertheless, the difference is that in 
the upper part of Sample 4, the all tungsten particles were completely 
melted and solidified as a whole. High magnification images ( Figs. 18 c- 
g) present the microstructural evolution of tungsten from partially 
melting to completely melting. From the very bottom ( Figs. 18 g-i), a 
distinct difference can be observed between the 45# carbon steel matrix 
and the partially melted tungsten particle. Identical to the observations 
in the multiple-track sample ( Section 3.3 ), precipitates formed and 
intermetallic compounds developed at the edge of tungsten particles 
( Fig. 18 g-ii). However, there is no matrix observed in this area (as shown 
in Fig. 18 g-iii) because of the higher substrate composition (45# carbon 
steel matrix) at the bottom area. Since the gradient distribution of 
tungsten and its intermetallic compounds are more resistant to corrosion 
than 45# carbon steel substrate during the process of preparing metal -
lographic samples; therefore, the Fe matrix at the bottom was over- 
etched and forming uneven microstructure. Above the bottom 
( Figs. 18 f-i-iii), the over-etched area (Fe matrix area) decreases, and 
many small tungsten-rich particles form between big tungsten particles 
together with intermetallic compounds. With the decrease of scanning 
speed, increase of laser power and heat accumulation, the un-melted 
tungsten particles are connected with intermetallic compounds and 
small tungsten-rich particles ( Figs. 18 e-i-iii). Then, tungsten particles 
are merged, and big area of tungsten is formed with little intermetallic 
compounds, as indicated in Figs. 18 d-i-iii. Finally, due to the decrease of 
Fe matrix, the pure tungsten deposition layer is formed ( Figs. 18 c-i-iii). 
Here, the influence of processing parameters is discussed. To avoid 
excessive melting of the substrate, the first three layers use a lower 
energy input (3000 W and 3000 mm/min), which is the same as Sample 
3. After that, a higher energy input (3500 – 4000 W and 540 mm/min) is 
adopted. Unfortunately, the energy input of the forth layer is too high for 
the first three layers, causing them to be melted completely and melting 
a bit of the substrate at the same time. Therefore, the wavy deposition- 
substrate interface of Sample 4 is not as flat as Sample 3. Meanwhile, this 
high energy input also results in the high substrate content in the first 
four layers, and directly causes a large number of pores in subsequent 
DED processes. Therefore, based on this processing parameter, the en -
ergy input is slightly reduced. Finally, the remaining 7 layers are 
completely melted, and successfully deposited to form very smooth 
tungsten deposited layer, as shown in Figs. 18 c-e. The high content of 
tungsten near the top area proves the feasibility for DED of pure 
tungsten. 
Based on aforementioned results, instead of radically increasing the 
energy input, if we gradually increase the energy input and decrease the 
hatch space after the third layer, under deposited layer will contain less 
substrate content, and a fewer or even flawless deposited layer with 
smooth surface will hopefully be prepared. Furthermore, other methods 
could also mitigate the formation of cracks, just like substrate heating 
(reduce thermal gradient and therefore reduce tensile residual stress) 
[ 41 ] and laser shock peening (transform tensile residual stress caused by 
LAM into compressive residual stress) [ 42 , 43 ]. 
4. Conclusions 
In this paper, pure tungsten deposited layer was fabricated on the 
reduced activation ferritic/martensitic (CLF-1) and 45# carbon steel 
substrates by DED. The following are the main conclusions: 
(1) During the DED of pure tungsten, dilution decreased with the 
increase of thickness while tungsten content increased, and the 
deposited layers with graded tungsten content were prepared. 
The acquired thickest deposited layer in this study was 4.4 mm 
with the highest tungsten content (99.78 wt%) in the top area. 
Intermetallic compounds, such as Fe
7
W
6 
and Fe
–
Cr, formed 
during DED, and their contents could be reduced to some extent 
through the adjustment of the manufacturing process. 
(2) Cracks mainly resulted from thermal stress, composition segre -
gation, pore and the brittleness of tungsten and its intermetallic 
compounds. Over-heating could cause cracks, as well as pores 
due to the evaporation of low melting point elements. Thus, the 
lower energy input at the very beginning should be adopted to 
Table 4 
Results of thermal performance. 
Sample
Test 
temperature 
(˚C)
Density
(ρ)
(g/cm3)
Specific 
heat (Cp)
(J/(g·K))
Thermal 
diffusivity 
(α)
(cm2/s)
Thermal 
conductivit
y (λ)
(W/(m·K))
RT 0.151 8.822 18.24
500 13.695 0.218 9.278 27.70
900 0.289 9.958 39.41
RT 0.216 22.938 73.75
500 14.886 0.321 22.184 106.00
900 0.443 22.360 147.45
J. Xie et al.

## Page 15

Surface & Coatings Technology 409 (2021) 126884
15
prepare a transitional layer before the pure tungsten deposited 
layer builds up. 
(3) The thermal conductivities were increased from 18.24 (at RT), 
27.70 (at 500 
◦
C) and 39.41 (at 900 
◦
C) W/(m ⋅ K) in double-layer 
sample to 73.75 (at RT), 106.00 (at 500 
◦
C) and 147.45 (at 
900 
◦
C) W/(m ⋅ K) in 9-layer sample with process optimization. 
Author statement 
Jichang Xie: Conceptualization, Investigation, Writing – Original 
Draft. 
Haifei Lu: Microstructural observations, Methodology. Co-first 
author. 
Jinzhong Lu: Conceptualization, Supervision, Writing – Reviewing 
& Editing. 
Xinling Song: Methodology supervision. 
Shikai Wu: Technology supervision. 
Jianbo Lei: Conceptualization, Supervision, Writing – Reviewing & 
Editing. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Fig. 18. SEM images and EDS results of Sample 4. (a) The image of cross-section, (b) EDS result of different areas, and (c-g) the high magnification images of selected 
areas from top to bottom. 
J. Xie et al.

## Page 16

Surface & Coatings Technology 409 (2021) 126884
16
Acknowledgments 
This work was financially supported by the National Key R & D Pro -
gram of China (Grant No. 2017YFB1103604), the industrial trans -
formation and upgrading funds of Ministry of Industry and Information 
Technology (RZJC-XM19-004), the Tianjin Municipal Special Program 
of Talents Development for Excellent Youth Scholars (TJTZJH-QNBJRC- 
2-15), the National Natural Science Foundation of China (Grant No. 
61475117), and the open project of Beijing Engineering Researching 
Center of Laser Technology (BG0046-2018-11). 
References 
[1] P. Lorenzetto, J. Andrade, S. Banetta, T. Cicero, G. Dellopoulos, A. Durocher, 
F. Escourbiac, M. Felip, L. Ferrand, P. Gavila, S. Gicquel, L. Guerrini, S. Heikkinen, 
P. Marshall, M. Merola, R. Mitteau, R. Raffray, B. Riccardi, EU contribution to the 
procurement of blanket first wall and divertor components for ITER, Fusion Eng. 
Des. 136 (2018) 975 – 982, https://doi.org/10.1016/j.fusengdes.2018.04.050 . 
[2] R.A. Pitts, X. Bonnin, F. Escourbiac, H. Frerichs, J.P. Gunn, T. Hirai, A. 
S. Kukushkin, E. Kaveeva, M.A. Miller, D. Moulton, V. Rozhansky, I. Senichenkov, 
E. Sytova, O. Schmitz, P.C. Stangeby, G. De Temmerman, I. Veselova, S. Wiesen, 
Physics basis for the first ITER tungsten divertor, Nucl. Mater. Energy 20 (2019) 
100696, https://doi.org/10.1016/j.nme.2019.100696 . 
[3] S. Wurster, N. Baluc, M. Battabyal, T. Crosby, J. Du, C. García-Rosales, 
A. Hasegawa, A. Hoffmann, A. Kimura, H. Kurishita, R.J. Kurtz, H. Li, S. Noh, 
J. Reiser, J. Riesch, M. Rieth, W. Setyawan, M. Walter, J.-H. You, R. Pippan, Recent 
progress in R & D on tungsten alloys for divertor structural and plasma facing 
materials, J. Nucl. Mater. 442 (2013) 181 – 189, https://doi.org/10.1016/j. 
jnucmat.2013.02.074 . 
[4] H.C. Kim, E. Bang, N. Kwak, Y. Oh, H.N. Han, H. Choi, K. Kim, Thermal and 
microstructural properties of spark plasma sintered tungsten for the application to 
plasma facing materials, Fusion Eng. Des. 146 (2019) 2649 – 2653, https://doi.org/ 
10.1016/j.fusengdes.2019.04.071 . 
[5] A. Herrmann, H. Greuner, N. Jaksic, M. Balden, A. Kallenbach, K. Krieger, P. de 
Marn ´e, V. Rohde, A. Scarabosio, G. Schall, Solid tungsten Divertor-III for ASDEX 
upgrade and contributions to ITER, Nucl. Fusion 55 (2015), 063015, https://doi. 
org/10.1088/0029-5515/55/6/063015 . 
[6] A. Moitra, S. Kim, S.G. Kim, S.J. Park, R.M. German, M.F. Horstemeyer, 
Investigation on sintering mechanism of nanoscale tungsten powder based on 
atomistic simulation, Acta Mater. 58 (2010) 3939 – 3951, https://doi.org/10.1016/ 
j.actamat.2010.03.033 . 
[7] X. Zhang, Q. Yan, S. Lang, Y. Wang, C. Ge, Preparation of pure tungsten via various 
rolling methods and their influence on macro-texture and mechanical properties, 
Mater. Des. 126 (2017) 1 – 11, https://doi.org/10.1016/j.matdes.2017.04.021 . 
[8] M.R. Gilbert, J.C. Sublet, Neutron-induced transmutation effects in W and W-alloys 
in a fusion environment, Nucl. Fusion 51 (2011), 043005, https://doi.org/ 
10.1088/0029-5515/51/4/043005 . 
[9] I. Zammuto, M. Li, A. Herrmann, N. Jaksic, V. Rohde, M. Balden, S. Vorbrugg, 
G. Matern, H. Greuner, R. Neua, A. Kallenbach, Cracks avoidance with a modified 
solid tungsten divertor in ASDEX upgrade, Fusion Eng. Des. 136 (2018) 
1052 – 1057, https://doi.org/10.1016/j.fusengdes.2018.04.066 . 
[10] L. Yan, Y. Chen, F. Liou, Additive manufacturing of functionally graded metallic 
materials using laser metal deposition, Addit. Manuf. 31 (2020) 100901, https:// 
doi.org/10.1016/j.addma.2019.100901 . 
[11] C. Li, Y.P. Wang, S.Y. Ma, X.S. Yang, J.F. Li, Y.Z. Zhou, X. Liu, J.G. Tang, X. 
Y. Wang, G.M. Le, Densification, microstructural evolutions of 90W-7Ni-3Fe 
tungsten heavy alloys during laser melting deposition process, Int. J. Refract. Met. 
Hard Mater. 91 (2020) 105254, https://doi.org/10.1016/j.ijrmhm.2020.105254 . 
[12] X. Zhou, X.H. Liu, D.D. Zhang, Z.J. Shen, W. Liu, Balling phenomena in selective 
laser melted tungsten, J. Mater. Process. Technol. 222 (2015) 33 – 42, https://doi. 
org/10.1016/j.jmatprotec.2015.02.032 . 
[13] M. Guo, D.D. Gu, L.X. Xi, L. Du, H.M. Zhang, J.Y. Zhang, Formation of scanning 
tracks during Selective Laser Melting (SLM) of pure tungsten powder: morphology, 
geometric features and forming mechanisms, Int. J. Refract. Met. Hard Mater. 79 
(2019) 37 – 46, https://doi.org/10.1016/j.ijrmhm.2018.11.003 . 
[14] M. Zhong, W. Liu, G. Ning, L. Yang, Y. Chen, Laser direct manufacturing of 
tungsten nickel collimation component, J. Mater. Process. Technol. 147 (2) (2004) 
167 – 173, https://doi.org/10.1016/j.jmatprotec.2003.12.009 . 
[15] D. Zhang, Q. Cai, J. Liu, Formation of nanocrystalline tungsten by selective laser 
melting of tungsten powder, Mater. Manuf. Process. 27 (2012) 1267 – 1270, https:// 
doi.org/10.1080/10426914.2012.663119 . 
[16] A.T. Sidambe, D.S. Judson, S.J. Colosimo, P. Fox, Laser powder bed fusion of a pure 
tungsten ultra-fine single pinhole collimator for use in gamma ray detector 
characterisation, Int. J. Refract. Met. Hard Mater. 84 (2019) 104998, https://doi. 
org/10.1016/j.ijrmhm.2019.104998 . 
[17] D. Wang, C. Yu, X. Zhou, J. Ma, W. Liu, Z. Shen, Dense pure tungsten fabricated by 
selective laser melting, Appl. Sci. 7 (2017) 430, https://doi.org/10.3390/ 
app7040430 . 
[18] C. Tan, K. Zhou, W. Ma, B. Attard, P. Zhang, T. Kuang, Selective laser melting of 
high-performance pure tungsten: parameter design, densification behavior and 
mechanical property, Sci. Tech. Adv. Mater. 19 (2018) 370 – 380, https://doi.org/ 
10.1080/14686996.2018.1455154 . 
[19] R.K. Enneti, R. Morgan, S.V. Atre, Effect of process parameters on the selective 
laser melting (SLM) of tungsten, Int. J. Refract. Met. Hard Mater. 71 (2018) 
315 – 319, https://doi.org/10.1016/j.ijrmhm.2017.11.035 . 
[20] A. Ivekovi ´c, N. Omidvari, B. Vrancken, K. Lietaert, L. Thijs, K. Vanmeensel, 
J. Vleugels, J.P. Kruth, Selective laser melting of tungsten and tungsten alloys, Int. 
J. Refract. Met. Hard Mater. 72 (2018) 27 – 32, https://doi.org/10.1016/j. 
ijrmhm.2017.12.005 . 
[21] S.F. Wen, C. Wang, Y. Zhou, L.C. Duan, Q.S. Wei, S.F. Yang, Y.S. Shi, High-density 
tungsten fabricated by selective laser melting: densification, microstructure, 
mechanical and thermal performance, Opt. Laser Technol. 72 (2018) 27 – 32, 
https://doi.org/10.1016/j.ijrmhm.2017.12.005 . 
[22] M. Xie, S.F. Zhou, S.Z. Zhao, J.B. Jin, D.C. Chen, L.C. Zhang, In-situ Fe
2
P 
reinfocrced bulk Cu-Fe immiscible alloy with nanotwinned Cu produced by 
selective laser melting, J. Alloys Compd. 838 (2020) 155592, https://doi.org/ 
10.1016/j.jallcom.2020.155592 . 
[23] T. DebRoy, H.L. Wei, J.S. Zuback, T. Mukherjee, J.W. Elmer, J.O. Milewski, A. 
M. Beese, A. Wilson-Heid, A. De, W. Zhang, Additive manufacturing of metallic 
components-process, structure and properties, Prog. Mater. Sci. 92 (2018) 
112 – 224, https://doi.org/10.1016/j.pmatsci.2017.10.001 . 
[24] Y.R. Choi, S.D. Sun, Q.C. Liu, M. Brandt, M. Qian, Influence of deposition strategy 
on the microstructure and fatigue properties of laser metal deposited Ti-6Al-4V 
powder on Ti-6Al-4V substrate, Int. J. Fatigue 130 (2020) 105236, https://doi.org/ 
10.1016/j.ijfatigue.2019.105236 . 
[25] G.F. Sun, X.T. Shen, Z.D. Wang, M.J. Zhan, S. Yao, R. Zhou, Z.H. Ni, Laser metal 
deposition as repair technology for 316L stainless steel: influence of feeding 
powder compositions on microstructure and mechanical properties, Opt. Laser 
Technol. 109 (2019) 71 – 83, https://doi.org/10.1016/j.optlastec.2018.07.051 . 
[26] Y.P. Wang, S.Y. Ma, X.S. Yang, Y.Z. Zhou, X. Liu, J.F. Li, J.J. Zhang, C. Li, X. 
Y. Wang, G.M. Le, Y. Zhang, Microstructure and strengthening mechanisms of 
90W-7Ni-3Fe alloys prepared using laser melting deposition, J. Alloys Compd. 838 
(2020) 155545, https://doi.org/10.1016/j.jallcom.2020.155545 . 
[27] G. Wang, X. Sun, M. Huang, Y. Qin, Y. Yao, S. Yang, Influence of processing 
parameters on the microstructure and tensile property of 85 W-15Ni produced by 
laser direct deposition, Int. J. Refract. Met. Hard Mater. 82 (2019) 227 – 233, 
https://doi.org/10.1016/j.ijrmhm.2019.04.016 . 
[28] C. Li, S.Y. Ma, X. Liu, J.F. Li, G.M. Le, Microstructures and properties of 80W-20Fe 
alloys prepared using laser melting deposition process, Int. J. Refract. Met. Hard 
Mater. 77 (2018) 113 – 119, https://doi.org/10.1016/j.ijrmhm.2018.08.005 . 
[29] W. Jeong, Y.S. Kwon, D. Kim, Three-dimensional printing of tungsten structures by 
directed energy deposition, Mater. Manuf. Process. 34 (2019) 986 – 992, https:// 
doi.org/10.1080/10426914.2019.1594253 . 
[30] S.K. Wu, J.C. Zhang, J.X. Yang, J.X. Lu, H.B. Liao, X.Y. Wang, Investigation on 
microstructure and properties of narrow-gap laser welding on reduced activation 
ferritic/martensitic steel CLF-1 with a thickness of 35 mm, J. Nucl. Mater. 503 
(2018) 66 – 74, https://doi.org/10.1016/j.jnucmat.2018.02.038 . 
[31] W.J. Parker, R.J. Jenkins, C.P. Butler, G.L. Abbott, Flash method of determining 
thermal diffusivity, heat capacity, and thermal conductivity, J. Appl. Phys. 32 
(1961) 1679, https://doi.org/10.1063/1.1728417 . 
[32] T. Azumi, Y. Takahashi, Novel finite pulse-width correction in flash thermal 
diffusivity measurement, Rev. Sci. Instrum. 52 (1981) 1411 – 1413, https://doi.org/ 
10.1063/1.1136793 . 
[33] D.D. Gu, W. Meiners, K. Wissenbach, R. Poprawe, Laser additive manufacturing of 
metallic components: materials, processes and mechanisms, Int. Mater. Rev. 57 
(2013) 133 – 164, https://doi.org/10.1179/1743280411Y.0000000014 . 
[34] J.H. Martin, B.D. Yahata, J.M. Hundley, J.A. Mayer, T.A. Schaedler, T.M. Pollock, 
3D printing of high-strength aluminium alloys, Nature 549 (2017) 365 – 369, 
https://doi.org/10.1038/nature23894 . 
[35] J.J. Xu, X. Lin, P.F. Guo, H.B. Dong, X.L. Wen, Q.G. Li, L. Xue, W.D. Huang, The 
initiation and propagation mechanism of the overlapping zone cracking during 
laser solid forming of IN-738LC superalloy, J. Alloys Compd. 749 (2018) 859 – 870, 
https://doi.org/10.1016/j.jallcom.2018.03.366 . 
[36] J.D. Wang, L.Q. Li, W. Tao, Crack initiation and propagation behavior of WC 
particles reinforced Fe-based metal matrix composite produced by laser melting 
deposition, Opt. Laser Technol. 82 (2016) 170 – 182, https://doi.org/10.1016/j. 
optlastec.2016.03.008 . 
[37] P. Gumbsch, J. Riedle, A. Hartmaier, H.F. Fischmeister, Controlling factors for the 
brittle-to-ductile transition in tungsten single crystals, Science 282 (1998) 
1293 – 1295, https://doi.org/10.1126/science.282.5392.1293 . 
[38] E. Chauvet, P. Kontis, E.A. J ¨agle, B. Gault, D. Raabe, Tassin Catherine, J.J. Blandin, 
R. Dendievel, B. Vayre, et al., Acta Mater. 142 (2017) 82 – 94, https://doi.org/ 
10.1016/j.actamat.2017.09.047 . 
[39] L. Aucott, D. Huang, H.B. Dong, S.W. Wen, J. Marsden, A. Rack, A.C.F. Cocks, 
A threestage mechanistic model for solidification cracking during welding of steel, 
Metall. Mater. Trans. A 49 (5) (2018) 1674 – 1682, https://doi.org/10.1007/ 
s11661-018-4529-z . 
[40] Z.T. Gan, G. Yu, X.L. He, S.X. Li, Numerical simulation of thermal behavior and 
multicomponent mass transfer in direct laser deposition of Co-base alloy on steel, 
Int. J. Refract. Met. Hard Mater. 104 (2017) 28 – 38, https://doi.org/10.1016/j. 
ijheatmasstransfer.2016.08.049 . 
[41] A. Sadhu, A. Choudhary, S. Sarkar, A.M. Nair, P. Nayak, S.D. Pawar, G. Muvvala, S. 
K. Pal, A.K. Nath, A study on the influence of substrate pre-heating on mitigation of 
cracks in direct metal laser deposition of NiCrSiBC-60%WC ceramic coating on 
J. Xie et al.

## Page 17

Surface & Coatings Technology 409 (2021) 126884
17
Inconel 718, Surf. Coat. Technol. 389 (2020) 125646, https://doi.org/10.1016/j. 
surfcoat.2020.125646. 
[42] J.Z. Lu, H.F. Lu, X. Xu, J.H. Yao, J. Cai, K.Y. Luo, High-performance integrated 
additive manufacturing with laser shock peening-induced microstructural 
evolution and improvement in mechanical properties of Ti6Al4V alloy 
components, Int. J. Mach. Tools & Manuf. 148 (2020) 103475, https://doi.org/ 
10.1016/j.ijmachtools.2019.103475. 
[43] C.Y. Wang, K.Y. Luo, X.Y. Bu, Y.Y. Su, J. Cai, Q.L. Zhang, J.Z. Lu, Laser shock 
peening-induced surface gradient stress distribution and extension mechanism in 
corrosion fatigue life of AISI 420 stainless steel, Corros. Sci. 177 (2020) 109027, 
https://doi.org/10.1016/j.corsci.2020.109027. 
J. Xie et al.
