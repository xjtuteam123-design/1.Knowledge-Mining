# Additive-manufacturing-of-tantalum-scaffolds_2023_International-Journal-of-R

<!-- source: D:\总文献\Additive-manufacturing-of-tantalum-scaffolds_2023_International-Journal-of-R.pdf -->
<!-- file_sha256: f3c06f773208a38671eba859ccb7dac1560da9f7670f56763938f98ba0720bbd -->

## Page 1

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
Available online 25 January 2023
0263-4368/© 2023 Published by Elsevier Ltd.
Additive manufacturing of tantalum scaffolds: Processing, microstructure 
and process-induced defects 
Abdul Azeez Abdu Aliyu
a
, Kitti Poungsiri
b
, Junji Shinjo
c
, Chinnapat Panwisawas
d
, 
Roger C. Reed
e
, Chedtha Puncreobutr
a
, Krittima Tumkanon
a
, Surasak Kuimalee
f
, 
Boonrat Lohwongwatana
a , b , * 
a
M3D Laboratory, Advanced Materials Analysis Research Unit, Department of Metallurgical Engineering, Faculty of Engineering, Chulalongkorn University, Phayathai 
Road, Wangmai, Pathumwan District, Bangkok 10330, Thailand 
b
Biomechanics Research Center, Meticuly Co. Ltd., Pathumwan, Wang-mai District, Bangkok, Thailand 
c
Next Generation Tatara Co-Creation Centre (NEXTA), Shimane University, 1060, Nishikawatsu, Matsue 690-8504, Japan 
d
School of Engineering and Materials Science, Queen Mary University of London, London E1 4NS, UK 
e
Department of Materials, University of Oxford, Parks Road, Oxford OX1 3PH, UK 
f
Industrial Chemistry and Textile Technology Program, Faculty of Science, Maejo University, 50290 Chiang Mai, Thailand 
ARTICLE INFO 
Keywords: 
Tantalum 
Additive manufacturing 
Defects 
Microstructure 
Implant 
Laser powder-bed fusion 
ABSTRACT 
Extreme melting point, high density, and ease of oxidation of tantalum (Ta) make its processing rather difficult 
using conventional methods. Additive manufacturing (AM) serves as an alternative Ta processing technique with 
unique design flexibility, customization, and minimizing material wastage. However, most additively manu -
factured parts contain undesired microstructural features or deviations (process-induced defects). This study 
aimed to assess the processability of the solid and structurally porous scaffolds of Ta through laser powder-bed 
fusion (LPBF) AM. It will further characterize and evaluate microstructure of LPBF processed Ta, with emphasis 
on assessing the mechanism of the process-induced defects. The x-ray diffraction (XRD) and microstructural 
investigation confirmed the presence of BCC Ta phase containing columnar, equiaxed and fine grains with 
roughness between 3.88 nm to 10.40 nm. The presence of oxygen resulted in the formation of some oxide phases 
such as Ta
2
O
5 
and Ta
2
O
3
. Numerous process-induced defects, including solidification-induced micropores, pores- 
induced and solidification-induced microcracks were identified. The dislodge unmelted or partially fused Ta 
powder resulted in other form of defects including micro-concaves and microgrooves. The mechanism of pore 
formation during the LPBF of Ta was assessed through computational simulation and its findings rationalised the 
experimental results. 
1. Introduction 
Owing to their high strength, high ductility, resistance to corrosion 
and biocompatibility behaviour, refractory metals becomes widely used 
as biomaterials for the fabrication of medical devices, orthopaedic or 
load-bearing implants [ 1 ]. Tantalum (Ta) was first discovered by Anders 
Gustaf Ekeberg of Sweden in 1802 and its clinical application as 
biomaterial can be traced back to 1940s [ 2 , 3 ]. Robertson and Peacher 
[ 4 ] utilize Ta medical devices in the form of plate, foil, wire and ribbon 
to accurately perform the nerve suture, repair cranial defects, inhibits 
postoperative adhesions and secure hemostasis without adverse effect to 
the surrounding tissues. Various in-vivo and in-vitro studies confirmed 
the excellent osteointegration, exceptional biocompatibility, high 
strength and good corrosion resistance of Ta implant [ 5 – 7 ]. Another 
study by Matsuno, et al. [ 8 ] further confirmed the non-toxicity and 
biocompatibility of the Ta. Compared to the most commonly used sur -
gical grade biomaterial like Ti-6Al-4 V, the adhesion, proliferation and 
differentiation of human osteoblast cells was remarkably observed on 
the Ta surface [ 9 ]. Meijer, et al. [ 10 ] investigated the strain distribution 
and stability of the tibial plateau reconstruction using Ta trabecular 
cones. The implant was found to have high stability with good strain 
distribution. Despite the outstanding biological performance and 
* Corresponding author at: M3D Laboratory, Advanced Materials Analysis Research Unit, Department of Metallurgical Engineering, Faculty of Engineering, 
Chulalongkorn University, Phayathai Road, Wangmai, Pathumwan District, Bangkok 10330, Thailand. 
E-mail address: boonrat@gmail.com (B. Lohwongwatana). 
Contents lists available at ScienceDirect 
International Journal of Refractory 
Metals and Hard Materials 
journal homep age: www. elsevier.com/ locate/IJ RMHM 
https://doi.org/10.1016/j.ijrmhm.2023.106132 
Received 1 November 2022; Received in revised form 19 January 2023; Accepted 23 January 2023

## Page 2

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
2
numerous advantages of Ta over the currently used metallic bio -
materials, its application as biomaterial is limited, especially for making 
large implants owing to its high density and high cost [ 11 ]. In early 
2000s, the surge in research related to Ta porous implants was noticed 
after the introduction of porous Ta acetabular cup implants by Trabec -
ular Metal ™ (Zimmer, Warsaw, IN, USA). However, processing of both 
solid and porous Ta is challenging through conventional techniques such 
as lost wax casting, furnace sintering and electron beam melting, owing 
to its extreme melting point (2996 
◦
C), high density (16.68 g/cm
3
) and 
high affinity to oxygen [ 12 , 13 ]. 
In recent years, there is rising attempts to fabricate both solid and 
porous Ta implants through additive manufacturing (AM), specifically 
laser powder-bed fusion (LPBF) [ 14 – 19 ]. LPBF utilized computer-aided 
design (CAD) to build a part through layer-by-layer powder deposition 
following the prescribed laser scan path [ 20 , 21 ]. The advantages of 
LPBF include its freedom to design porosities and macro/microstruc -
tures of the implants, which allow control of mechanical properties, 
fabrication of complex structures to match that of human bone and to 
enable patient-specific implants [ 17 , 22 , 23 ]. Chandhanayingyong, et al. 
[ 24 ] utilize LPBF to fabricate a highly complex and patient-specific 
proximal phalangeal prosthesis, whereby a giant cell tumor in the toe 
was successfully treated. In another study by Zhao, et al. [ 25 ], a porous 
scaffold of Ta was developed through gel casting-based 3D printing 
coupled with an electrolytic reduction. The fabricated scaffolds were 
found to have high strength (4.1 ± 0.4 MPa) close to that of cancellous 
bone (4 – 12 MPa) and facilitate the cells proliferation. 
Although, researches on processing solid and porous Ta through 
LPBF approach could be found [ 26 – 29 ], there are still key issues which 
require an in-depth understanding and systematic investigation. An 
extremely high cooling rate coupled with non-equilibrium solidification 
during the LPBF of metals resulted in various process-induced defects 
[ 30 , 31 ]. Gong, et al. [ 32 ] revealed the formation of other defects, 
including micro-concaves and microgrooves during LPBF of Ti-6Al-4 V 
implant. These defects seriously degrade the mechanical and biomedical 
behaviours of metallic implants. However, to the best of the authors' 
knowledge, little has been focused on assessing the causes, distribution, 
occurrences and formation mechanisms of the process-induced defects 
that normally formed on the additively manufactured solid and porous 
Ta parts. Hence, these motivated the idea for this research. 
In this study, solid and porous scaffolds of Ta were designed using 
ANSYS 2020r1 software and processed through LPBF technique. The 
fabricated specimens were characterized through various characteriza -
tion methods which are field emission scanning electron microscopy 
(FESEM), optical microscopy (OM), energy dispersive x-ray spectros -
copy (EDX), x-ray photoelectron spectroscopy (XPS) and x-ray diffrac -
tion (XRD). Microstructural investigation presents various deviations 
and undesired features resulting in LPBF process-induced defects. BCC 
Ta enriched with columnar, equiaxed and fine grains and some oxide 
phases like Ta
2
O
3 
and Ta
2
O
5 
was identified. A numerical simulation 
demonstrating the pores generation and formation mechanism during 
the LPBF of solid and porous scaffolds of Ta is also presented. 
2. Method 
2.1. Design of solid and porous scaffolds of Ta 
ANSYS 2020r1 software was employed to design and model the solid 
and the porous scaffolds of Ta specimens. The compute-aided design 
(CAD) models are then saved in STereoLithography (STL) file, and the 
redesigned models were imported in the form of STL format files. 
Different sizes of the cubic solid Ta specimens namely D-Ta1, D-Ta2 and 
D-T3 with dimensions 5 mm, 10 mm and 15 mm, respectively were 
designed. The purpose of the solid specimens is to allow comparison 
with the porous specimens. Octet truss and diamond truss with di -
mensions 10 × 10 × 12 mm with 25% and 50% infill density were used 
for the porous scaffolds. Various designs of the porous scaffold of Ta 
specimens were levelled S-Ta1, S-Ta2, S-Ta3 and S-Ta4 as indicated in 
Fig. 1 . 
2.2. LPBF of solid and porous scaffolds 
Both solid and porous scaffolds of Ta were 3D printed based on the 
CAD models using LPBF equipment (FARSOON Technologies Inc. and 
MiCap Machinery co. ltd., Changsha, Hunan, China). A medical grade 
pure Ta powder, which is also supplied by FARSOON Technology, China 
with physical properties shown in Table 1 is used to fabricate the solid 
and the porous scaffold specimens. The 3D printed specimens were dried 
for 90 mins at an ambient temperature after printing. Trapped and un -
bounded powder was removed by a compressed air and ultrasonic 
washing. Bulk porous part is built by selectively melting the powder 
through the laser beam and the subsequent layer is formed by spreading 
the powder on the previous layer consecutively. The process continues 
until the designed bulk Ta part is formed. The manufacturing process of 
the specimens was throughout conducted in a vacuum shield with an 
Argon atmosphere to avoid oxidation. The infill and the borderline 
parameter conditions used for processing Ta specimens through LPBF 
process are presented in Table 2 . 
The laser energy used in this study can be estimated via Eq. (1) . 
Laser energy ( E ) =
P ( W )
v ( mm / s ) × t ( mm ) × h ( mm )
(1) 
where P is the laser power, v is the scanning speed, t is the layer 
thickness and h is the hatch spacing [ 33 ]. Using the infill and borderline 
parameter settings ( Table 2 ), the laser energy was computed to be 83.3 
Fig. 1. Computer-aided design of the unit cells and the porous scaffolds with 
respective pores density. 
A.A.A. Aliyu et al.

## Page 3

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
3
J/mm
3 
and 6.7 J/mm
3 
for the infill and borderline parameters, 
respectively. 
2.3. Dimensional accuracy and relative density 
To determine the dimensional accuracy of the LPBF processed solid 
and porous scaffolds of Ta, each side of the specimens was measured 
using vernier calliper. The measurement was repeated five times and the 
average value was calculated. To estimate the errors between the 
measured and design values, standard deviation was computed. Density 
and relative density were determined using the displacement method 
according to ASTM D792 standard [ 34 ]. The mass of the fabricated solid 
Ta specimens was weighed in air. It was then immersed in deionised 
water (DI) and the apparent mass of the specimen is determined. Then 
the density and the relative density (specific gravity) of the specimens 
were calculated using Eqs. (2) and (3) , respectively. 
Density =
w
a
w
a
 w
w
(2) 
Relative density =
ρ
substance
ρ
reference
(3) 
where: 
w
a
= apperent mass of specimen in air 
w
w
= apparent mass of totally immersed spacimen in water 
ρ
substance
= density of the substance been measured ,
ρ
reference
= density of the reference 
2.4. Metallographic specimen preparation for microstructural 
investigation 
Solid and porous 3D printed Ta specimens were prepared through 
four stages to enable microstructural observations as prescribed by the 
standard metallographic procedures. Firstly, the specimens were cut 
perpendicular to the direction of scan. In the second stage, the specimens 
were mounted to enable proper handling and safe grinding. The next 
stage involved grinding using premium grade abrasive paper (93 U- 
4854) and polishing by 1 μ m water-based diamond suspension through a 
conventional grinding/polishing technique. Last stage involved etching 
of the specimens using 50% lactic acid, 30% sulfuric acid and 20% hy -
drochloric acid etchants solution for 2 min at room temperature. 
2.5. Characterization 
Field emission Scanning electron microscopy (FESEM, FEI Quanta 
FEG 250, Thermo Fisher Scientific, Hillsboro, OR, USA) at 15 kV and 
optical microscope (OM, Hubitz - HRM 300, Korea) were used to visu -
alise and analyse the microstructure and the microstructural defects in 
the LPBF-processed solid and porous Ta specimens. Further analysis to 
assess the pore shape, size and the area density through Image J (KEY -
ENCE VR3000, Japan) analysis was performed. The surface topology 
and roughness were evaluated using atomic force microscope (AFM, 
Veeco, Dimension 3100, Plainview, NY, USA). The chemical composi -
tions and phases of the LPBF processed solid and porous scaffold of Ta 
were analysed through energy dispersive x-ray spectroscopy (FEI 
Quanta FEG 250, Thermo Fisher Scientific, Hillsboro, OR, USA), x-ray 
photoelectron spectroscopy (XPS, Bara Scientific Co., Ltd., series Axis 
Ultra) and x-ray diffraction (XRD, Bruker D8 Discover). The XRD mea -
surement was carried out at step size 0.01
◦
and scanning range of 2 θ =
10
◦
to 90
◦
using CuK α radiation at 15 kV, 30 mA. 
2.6. Thermal-fluid flow during LPBF AM 
A computational fluid dynamics (CFD) calculation is used to inves -
tigate the thermal-fluid flow dynamics of the melt pool to understand 
porosity development and surface structure to rationalise the micro -
structure observation from experiment. Our in-house CFD code called 
TATM-MEX has been adopted to model the interaction between the laser 
heat source and the powder materials [ 35 ]. The governing equations for 
fluid flow dynamics are presented in Eqs. (4.1), (4.2) and (4.3) : 
∂ρ
∂ t
+ ( u ⋅ ∇) ρ = ρ ∇ ⋅ u (4.1) 
∂ u
∂ t
+ ( u ⋅ ∇) u = 
∇ p
ρ
+ Q
u
+ g + F
u , surf
(4.2) 
∂ T
∂ t
+ ( u ⋅ ∇) T = 
p ∇ ⋅ u
ρ c
p
+ Q
T
+
1
ρ c
p
q
L
(4.3) 
Here, Q
u 
is the viscous term and g is the gravitational acceleration. 
All the interfacial phenomena present within the LPBF process, 
including surface tension, Marangoni's flow (thermo-capillary force) and 
recoil pressure have been incorporated in the simulation as F
u , surf 
as 
adopted by [ 35 ]. The liquid/gas interface is captured by the level-set 
method, combined with the volume-of-fluid method to assure volume 
conservation. The laser heat source q
L 
is calculated by tracking light 
propagation using the ray-tracing method, and the heat loss due to 
vaporization, conduction, convection and radiation have also been 
considered in Q
T
. Details of Modelling description can be found else -
where [ 35 ]. The physical properties of tantalum used in the simulation 
Table 1 
Physical properties of Pure Tantalum powder (source: manufacturer's Data). 
Physical properties Value Unit 
Density ≥ 16.360 g/cm
3 
Yield Strength Rp0.2 ≥ 140 MPa 
Tensile strength Rm ≥ 210 MPa 
Compressive strength ≥ 15 MPa 
Bending strength ≥ 700 MPa 
Elongation A ≥ 27 % 
Hardness ≥ 100 HV10 
Table 2 
Different operating parameter between infill and borderline. 
Operation parameter Infill parameter Borderline parameter 
Layer thickness 0.03 mm 0.03 mm 
Laser power 250 W 100 W 
Scanning speed 100 mm/s 500 mm/s 
Laser wavelength 1060 nm 1060 nm 
Laser spot size 85 μ m 128 μ m 
Table 3 
Thermo-physical properties of Ta [ 35 ]. 
Thermo-physical properties Value Unit 
Atomic weight 180.95 g/mol 
Solid density 16,654 kg/m
3 
Liquid density 15,000 kg/m
3 
Melting temperature 3258 K 
Boiling temperature 5783 K 
Δ h
melt 
36.6 kJ/mol 
Δ h
boil 
733 kJ/mol 
Surface tension, σ
0 
2150 mN/m 
Surface tension gradient, 
d σ
dT 
 0.21 mN/m/ 
K 
Viscosity, μ μ ( T ) = 0.0035 exp (213.3 ×
10
3
/ RT ) 
mPa ⋅ s 
Heat capacity at melting temperature, 
c
p 
41.8 J/mol/ 
K 
Thermal conductivity at melting 
temperature, λ 
47 W/m/K 
A.A.A. Aliyu et al.

## Page 4

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
4
are summarised in Table 3 . 
2.7. Vickers hardness 
The microhardness of the LPBF processed solid and porous scaffolds 
of Ta was determined according to standard test method provided by 
ASTM E98 – 82. The test was carried out using Vickers hardness testing 
machine (ZWICK, mode: 3214) and indented via diamond indenter. The 
load of 0.5 kg was applied at a slowdown speed and dwell time of 15 s. 
For each specimen, the hardness measurement was carried out five times 
at different locations and average value was recorded. 
3. Results 
3.1. LPBF processing of solid and porous tantalum 
Unlike conventional processes, Wauthl ´e, et al. [ 36 ] showed that, 
fully dense Ta components can be processed through LPBF technique 
with satisfactory mechanical properties as required by ISO 13782 of the 
pure Ta for surgical applications. Different sizes of the solid and porous 
Ta scaffolds were fabricated through LPBF technique ( Fig. 2 ). The 
dimensional accuracy was measured in x, y and z-directions as presented 
in Fig. 2 a-c and the results shown in Table 4 . The percentage dimen -
sional deviation (error) observed in the D-Ta1, D-Ta2 and D-Ta3 Ta 
specimens are 1.13%, 1.10% and 0.55%, respectively. The relative 
density of each solid Ta specimen measured through Archimedes 
method is presented in Table 5 . The solid Ta specimens D-Ta1, D-Ta2 
and D-Ta3 were found to have a very high relative density of 99.56%, 
98.99% and 99.43%, respectively. The specimen D-Ta2 has the lowest 
relative density. Therefore, it is selected for the subsequent pore 
analysis. 
Porous scaffolds of Ta were designed and fabricated through LPBF 
technique ( Fig. 2 d-g). The designed pore and strut of Ta scaffolds were 
printed using the imported CAD model in the form of STL files. The 25% 
and 50% infill density were designed for both diamond and octet truss 
scaffolds. The actual strut thickness of the scaffolds was compared with 
the average thickness of the measured values. 
The optical microscope images were used to measure and determine 
the strut thickness of the LPBF processed porous scaffolds of Ta ( Fig. 3 ). 
Three strut thickness values at different locations along the strut length 
was measured and average values were computed. To determine the 
mismatch between the designed and the 3D printed scaffolds of Ta, the 
standard deviation was calculated as indicated by the error bar ( Fig. 4 ). 
The highest discrepancy of 34.66 μ m is observed in the S-Ta3 specimen. 
The strut thickness was designed as 465.0 μ m while the measured 
thickness was found to be 511.26 μ m. The smallest discrepancy of 7.89 
μ m was found in the S-Ta2 specimen. 
3.2. Chemical composition and phase analysis 
The EDX, XPS and XRD characterization tools were utilized to assess 
chemical compositions of the LPBF-processed Ta specimens. Very long 
peak and numerous short peaks of Ta were observed in the EDX spec -
trum shown in Fig. 5 a. Despite the presence of a very short oxygen peak 
( Fig. 5 b), Ta dominates the LPBF processed solid specimens. Being an 
oxygen getter, it is quite tedious to separate oxygen from Ta powder. 
Therefore, 0.5% and 0.6% of oxygen was detected by the EDX analysis in 
the fabricated Ta specimens at different locations, Fig. 5 a and Fig. 5 b, 
respectively. Oxygen is believed to infiltrate the Ta powder during 
passivation for LPBF processing or more likely from the metallurgical 
preparation. It is beneficial to the implants by reacting with the alloying 
elements to form biocompatible metallic oxides. Another benefit of ox -
ygen in metallic alloy is its hardening capability, which enhance the 
hardness of the processed part. The elemental mapping for Ta and O, 
which shows the distribution of both elements in the built Ta parts is 
presented in Fig. 5 c and Fig. 5 d, respectively. 
Fig. 6 shows the XPS spectra of the LPBF processed Ta. The chemical 
states and the oxide species are shown in Fig. 6 a. The presence of oxygen 
in the LPBF processed specimen is further confirmed by the observed 
O1s XPS spectra ( Fig. 6 b). The O1s spectrum contained two regions of 
Ta
2
O
3 
and Ta
2
O
5 
oxide compounds with a binding energy of 531.5 eV 
and 532.8 eV, respectively. The Ta4f spectrum shown in Fig. 6 c also 
contains two regions of Ta4f2/5 and Ta4f7/2 at a binding energy of 27.5 
eV and 29.5 eV, respectively. These two species of Ta4f are believed to 
be responsible for the formation of metallic oxides. 
The XRD patterns of the LPBF-processed solid and porous Ta pro -
cessed at low and high energy conditions is presented in Fig. 7 . It 
revealed similar diffraction patterns in most of the specimens and 
parameter settings, which contained highly BCC Ta phase. The long 
sharp Ta peaks observed at 2 θ = 38
◦
, 57
◦
, 70
◦
and 83
◦
confirmed the 
crystalline nature of the LPBF processed solid and porous scaffolds of Ta 
( Fig. 7 a). Despite Ar protection during sintering, other secondary peaks 
of Ta
2
O
5 
precursor were detected at 2 θ = 45
◦
, 65
◦
and 78
◦
. This is 
believed to occur due to reaction of Ta with O, which previously 
detected by the EDX and XPS analysis. However, no secondary peaks of 
Ta
2
O
5 
or metallic oxide were observed in the D-Ta2 specimen. This 
further confirmed that, the oxygen is not present in the feedstock, rather 
infiltrated the LPBF processed Ta during the postprocessing. The 
diffraction peaks of BCC Ta phase in the porous Ta scaffolds (S-Ta1-4) 
are longer and broader than those of solid Ta (D-Ta1-3) as seen in 
Fig. 7 b. This might relate to the formation of highly refined micro -
structures and hence, enhanced residual stresses [ 23 ]. 
3.3. Topography and microstructural evaluation 
SEM micrograph revealing the microstructure of the LPBF-processed 
Ta scaffold (S-Ta1) at borderline parameter settings is displayed in 
Fig. 8 . The micro-concaves observed in Fig. 8 a are believed to be 
resulted from dislodged Ta particles during the conventional grinding/ 
polishing processes. Large columnar grains, which believed to be grown 
along the building direction were observed ( Fig. 8 b). Thermal gradient 
along the solid/liquid interface in the pool boundaries, which normally 
occurred during LPBF process resulted in columnar grains growth along 
the building direction [ 37 ]. Equiaxial grains and fine nano structures 
were also observed ( Fig. 8 c and e). These nano-structural features 
enhance not only the ductility or mechanical properties of the LPBF 
processed part, but also its biological properties such as cell adhesion 
and proliferation. 
The presence of nano-structural features on the LPBF-processed Ta 
surface was further analysed through AFM ( Fig. 9 ). The 3D surface 
Fig. 2. LPBF processed solid and porous Ta specimens with direction of mea -
surements and dimensions (a) D-Ta1 (b) D-Ta2 (c) D-Ta3 (d) S-Ta1 (e) S-Ta2 (f) 
S-Ta3) (g) S-Ta4. 
A.A.A. Aliyu et al.

## Page 5

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
5
topography analysed over an area 20 μ m × 20 μ m revealed various 
uniform sharp peaks, indicating the nanostructured surface of the LPBF- 
processed Ta. The peak intensity of D-Ta1 is longer and hence, has a high 
average surface roughness of 10.40 nm ( Fig. 9 a). To better understand 
the level of the roughness intensity, the pattern is presented ( Fig. 9 b). 
The relatively low roughness of 5.09 nm and 3.88 nm was recorded for 
D-Ta2 ( Fig. 9 c) and D-Ta3 ( Fig. 9 d), respectively. Thus, the roughness 
decreases with an increase in the specimen size. This could occur due to 
two reasons: Firstly, an increase in unmelted or partially fused Ta 
powder with decrease in LPBF-processed Ta specimen size. Dislodging 
the partially fused Ta powder increase the surface roughness resulted in 
deeper concavity and microgrooves, hence, higher roughness. Secondly, 
increase in residual stress accumulation with a decrease in the specimen 
size, which increase the grain coarsening, hence, increase the surface 
roughness. 
To further understand the microstructure of the LBBF-processed 
scaffold of Ta, the FESEM measurement of specimen S-Ta4 was pre -
sented in Fig. 10 . It revealed numerous partially fused and unmelted Ta 
powder on the strut edges ( Fig. 10 a). The spherical shape Ta particles on 
the LPBF processed part confirmed the presence of unmelted Ta powder, 
which bonded together to form microgrooves ( Fig. 10 b). This confirmed 
the inability of the LPBF process to completely melt the Ta powder, 
which might relate to an extremely high melting temperature property 
of the Ta powder [ 38 ]. Further investigation at high magnification 
revealed some partially fused Ta particles on the scaffold surface as 
depicted in Fig. 10 c. The unmelted and partially fused Ta particle was 
removed through conventional grinding/polishing processes. However, 
it resulted in the formation of some micro features such micro-concaves 
and microgrooves, as well as exposing the pores-induced microcracks 
( Fig. 10 d). 
3.4. Process-induced defects evaluation 
During the LPBF process, numerous undesired microstructural fea -
tures or deviation, herein; referred to as process-induced defects are 
normally formed. These defects are detrimental to the quality and per -
formance of the fabricated parts. In this study about five process- 
induced defects were identified. These include (i) pores-induced 
microcracks, which induced by interconnected micropores (ii) 
solidification-induced microcracks, which is formed due to shrinkage of 
the Ta molten pool during solidification (iii) solidification-induced mi -
cropores, which resulted from gasses vaporization during solidification 
of the molten pool (iv) micro-concaves and (v) microgrooves, which are 
formed due to dislodged unmelted or partially fused Ta powder. In this 
study, SEM images of the solid and porous scaffolds of Ta were employed 
to evaluate the process-induced defects that formed during LPBF 
process. 
3.4.1. Solidification-induced micropores in solid Ta 
Generally, process-induced micropores are formed on the LPBF- 
processed metallic parts due to low laser energy, which resulted in an 
incomplete melting and the vaporization of the trapped gasses in the 
melt pool. However, when the energy is too high, melt instability 
occurred and the pores are formed due to solidification, herein referred 
solidification-induced micropores [ 39 ]. Solid LPBF-processed Ta (D- 
Ta2) was selected for the porosity analysis. The specimen was fabricated 
via the laser power of 250 W and scanning speed of 100 mm/s parameter 
Table 4 
Dimensional accuracy of D-Ta1, D-Ta2 and D-Ta3 Ta specimens. 
Directions D-Ta1 D-Ta2 D-Ta3 
Design (mm) Measured/Std. dev. (mm) Design (mm) Measured/Std. dev. (mm) Design (mm) Measured/Std. dev. (mm) 
X 5.0 5.1 ± 0 10.0 10.18 ± 0.02 15.0 15.12 ± 0.08 
Y 5.0 5.1 ± 0 10.0 10.15 ± 0.04 15.0 15.13 ± 0.05 
Z 5.0 5.0 ± 0 10.0 10.0 ± 0 15.0 15.0 ± 0 
Table 5 
Average measured density and relative density of the solid Ta specimens. 
Density AVG (g/cm
3
) Relative density (%) 
D-Ta1 16.58 ± 0.11 99.56 
D-Ta2 16.56 ± 0.02 98.99 
D-Ta3 16.66 ± 0.01 99.43 
Fig. 3. Optical micrographs comparing the mismatch between the LPBF- 
processed porous scaffolds of Ta, indicating the measured struts thickness (a) 
S-Ta1 (b) S-Ta2 (c) S-Ta3 and (d) S-Ta4 specimens. 
Fig. 4. Design versus average measured strut thickness of the S-Ta1, S-Ta2, S- 
Ta3, S-Ta4 specimens processed through LPBF indicating the error bar of the 
measured strut thickness. 
A.A.A. Aliyu et al.

## Page 6

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
6
conditions (high laser energy, E = 83.3 J/mm
3
). Particle analyser 
command in ImageJ was used to examine the area porosity. Thresh -
olding was used to select the features of the image and the number of the 
red pixels was measured ( Fig. 11 a). The outline of the pores detected 
during the analysis is presented in Fig. 11 b. The measured percentage 
area porosity was found to be 1.19%. 
The surface morphology of LPBF processed solid Ta specimens using 
100 W and 500 mm/s power and scanning speed, respectively was 
presented in Fig. 12 . Despite low energy setting used, no clear process- 
induced defects observed in D-Ta1 specimen ( Fig. 12 a). This is expected, 
owing to its high density of 99.56%. A cluster of solidification-induced 
micropores (encircled in red) and highly rough surface was observed 
in D-Ta2 specimen ( Fig. 12 b), which further observed through high 
magnification ( Fig. 12 c). This may relate to its low density (98.99%). 
The high roughness observed is due to lower laser energy (E = 6.7 J/ 
mm
3
) used, which is not sufficient to melt the Ta powder completely, 
owing to its extremely high melting temperature. Thus, the dislodged 
unmelted and partially fused Ta resulted in the deeper and narrow 
craters, hence the formation of rougher surface. Dramatic decrease in 
the micropores and smoother surface was noticed on the D-Ta3 spec -
imen ( Fig. 12 d). The decrease in solidification-induced micropores and 
improved roughness might also relate to the size of specimen. A similar 
finding was reported by Livescu, et al. [ 28 ], whereby less micropores 
was observed in a small size Ta specimen with less layer thickness. 
3.4.2. Process-induced defects in octet truss scaffolds 
Fig. 13 shows FESEM images of 50% Octet truss porous scaffold of Ta 
(S-Ta2) processed through the power (250 W) and scanning speed (100 
mm/s) parameter settings. It is obvious that various process-induced 
defects are present on the LPBF-processed surface ( Fig. 13 a). The high 
energy density used in processing this specimen resulted to some 
shallow microgrooves and few pores-induced microcracks ( Fig. 13 b). 
These defects are normally formed on the LPBF-processed surface due to 
dislodge unmelted or partially fused Ta powder. The defects are not 
pronounced due to significant melting of Ta powder. However, it is 
accompanied by Ta melts instability (balling) and accumulation of 
thermal stresses (tensile) in the adjacent solidified layers. The contin -
uous partial relieving of these stresses and the balling phenomenon 
induced the formation of interconnected micropores, which resulted to 
pores-induced microcracks [ 40 ]. To fully understand the deepness and 
the geometry of the microgrooves formed during LPBF process, the 
cross-section of S-Ta2 was observed ( Fig. 13 c). A semi-circular micro -
groove, which partially penetrated the strut connection was noticed 
( Fig. 13 d). 
3.4.3. Process-induced defects in diamond truss scaffolds 
The FESEM micrographs of S-Ta3 processed through parameter set -
tings of 100 W laser power and 500 mm/s scanning speed is displayed in 
Fig. 14 . It is evident that various morphological features revealed the 
process-induced defects ( Fig. 14 a). The pores-induced microcracks 
resulted from interconnected solidification-induced micropores and 
dislodge partially fused Ta powder are pronounced ( Fig. 14 b). This 
might relate to low energy density used in fabricating this specimen. The 
partially fused Ta powder are more concentrated around the strut 
connection and edges ( Fig. 14 c) and hence, the pores-induced micro -
cracks are more pronounced in this region ( Fig. 14 d). 3D printed 
nanostructured and micro scale porous scaffold surface was found to 
facilitate tissue growth and adhesion after implantation [ 41 ]. However, 
the undesired or undesigned features like process-induced defects de -
grades the properties of the LPBF-fabricated solid and porous scaffolds of 
Ta, thereby reducing its quality or service life. 
Fig. 5. SEM-EDX spectrum of the porous Ta specimen (S-Ta1) (a) numerous long peaks and short peaks of tantalum and oxygen, containing about 99.5% and 0.5%, 
respectively (b) 99.6% Ta and 0.4% (c) elemental mapping showing the distribution of tantalum and (c) oxygen. 
A.A.A. Aliyu et al.

## Page 7

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
7
3.5. Thermal-fluid flow simulation 
Numerical simulation results for the two conditions are shown in 
Fig. 15 a-b. For the lower laser energy case in Fig. 15 a, the conduction 
mode is observed since the laser power is not large and the scanning 
speed is relatively high. The powder bed surface is melted, but lack of 
fusion is observed in some places. Under the 250 W laser power and 100 
mm/s scanning speed parameter conditions, a keyhole is formed due to 
its higher laser energy as shown in Fig. 15 b. Although, the scanning 
speed is slower in this case, the keyhole tip oscillates faster than the 
scanning speed scale in accordance with the unsteady melt pool motion, 
as shown in Fig. 15 c. The liquid/gas interface is drawn at one instant and 
cross-sectional shapes at three-time instants are superposed by the solid 
lines with the time interval of 3.5 μ s. The change in the keyhole surface 
shape induces the change in the laser ray absorption/reflection and thus 
induces the change in local heat distribution, which are all inter -
connected. The melt pool motion is affected by this heat change in a 
complicated way as well. The fast keyhole flapping motion occasionally 
leads to the micropores formation, as shown in Fig. 15 d. The observed 
porosity (the ratio of the pore volume to the melt pool volume) is 1.08% 
at this instant. This porosity may vary temporarily, but the order of 
porosity is estimated around this value, which agrees with the present 
experimental observation. Therefore, the unsteady keyhole motion 
could be one reason for micropores formation. The interface between 
gas and liquid/solid is directly solved and the pores are identified as gas 
islands formed in the liquid metal. The pores here are generated due to 
the entrapment of the metal vapour at the keyhole tip, induced by the tip 
flapping motion. Although the porosity is not high or critical, suppres -
sion of this motion may require detailed thermal control, and further 
investigation is needed. 
3.6. Vickers microhardness 
The microhardness of LPBF processed solid and porous scaffolds of 
Ta is presented in Fig. 16 . The porous scaffolds processed through high 
energy with 250 W power and 100 mm/s scanning speed parameter 
settings has highest hardness value of 140 Hv while the lowest hardness 
of 131 Hv is observed in the solid Ta specimen processed through low 
energy with 100 W power and 500 mm/s scanning speed settings. This 
large variation in the hardness value might relate to low energy of 6.7 J/ 
mm
3 
in the borderline setting. Microhardness of LPBF processed Ta was 
found to increase with increasing energy density. However, it decreases 
when too high energy density (362.32 J/mm
3
) is used [ 22 ]. In a similar 
study, a higher hardness value of 228 Hv was reported, when processing 
trabecular Ta through LPBF technique [ 26 ]. LPBF processed Ta has a 
much higher hardness compared to those processed through conven -
tional methods like casting, powder metallurgy and annealing with 
hardness of 110 Hv, 120 Hv and 90 Hv, respectively [ 42 , 43 ]. 
Fig. 6. XPS spectra of LPBF processed Ta indicating the chemical compositions and oxide species (a) chemical states of Ta (b) O1s spectrum (c) Ta4f spectrum. 
A.A.A. Aliyu et al.

## Page 8

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
8
4. Discussions 
This study processed, characterized and assessed the microstructural 
features during LPBF of various solid and porous scaffolds of Ta, with 
emphasis on the types, distribution and formation mechanisms of 
microstructural deviations (process-induced defects). Process-induced 
defects degrade the mechanical and biomedical properties of the im -
plants. Therefore, it needs to be highly minimized or eliminated. 
Fig. 7. XRD spectrum of LPBF processed solid and porous Ta specimens (a) various peaks of Ta and Ta
2
O
5 
phases (b) Ta peaks within 2 θ = 35
◦
and 45
◦
presenting the 
broadness of the peaks. 
Fig. 8. FESEM micrographs of LPBF processed S-Ta1 specimen revealing (a) microstructure with various micro-concaves due to dislodged partially fuse Ta powder 
(b) columnar and equiaxial grains, solidification-induced microcracks and the partially fused Ta powder (c) equiaxial grains (d) fine grains. 
A.A.A. Aliyu et al.

## Page 9

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
9
4.1. Accuracy and density of LPBF processed Ta 
The average standard deviation in the measured and designed di -
mensions along x, y and z directions of the cubic solid Ta specimens (D- 
Ta1, D-Ta2 and D-Ta3) were averagely calculated as ± 0.0, ± 0.02 and ±
0.04, respectively ( Table 4 ). This very low deviation confirmed the 
capability of the LPBF technique in fabricating highly dense pure Ta 
parts. Similarly, the standard deviation of the strut thickness for the 
porous scaffolds were calculated, with values 20.17, 7.89, 34.66 and 
14.10 for the S-Ta1, S-Ta2, S-Ta3 and S-Ta4, respectively ( Fig. 3 ). This 
high discrepancy in the strut thickness of the designed and fabricated 
porous scaffolds of Ta might be related to the presence of unmelted and 
partially fused Ta powder, which led to a highly rough surface of the 3D 
printed porous Ta specimen. A similar finding was reported during the 
3D printing of Ti-alloy porous scaffolds [ 44 ]. The high relative density of 
the cubic solid Ta specimens, D-Ta1 and D-Ta3 of 99.56% and 99.43%, 
respectively, confirmed the suitability of the LPBF technique to fabricate 
highly dense Ta parts. The low density (98.99%) observed in the D-Ta2 
specimen is believed to occur due to high micropores or partially fused 
Ta powder, owing to the low energy density used in processing this 
specimen. Other factors that might contribute to the decrease in density 
of the LPBF processed Ta is the increase in hatch distance and layer 
thickness, which resulted to a higher material overlap and hence, 
increasing the solidification-induced micropores [ 28 ]. 
Fig. 9. AFM images showing the surface topology and roughness of LPBF-processed solid Ta (a) D-Ta1 (b) D-Ta1 roughness profile (c) D-Ta2 (d) D-Ta3. 
Fig. 10. FESEM images of LPBF processed S-Ta4 specimen (a) various unmelted and partially fused Ta powder (b) higher magnification revealing the shape of the 
unmelted Ta powder and microgroove formation (c) partially fused Ta powder on the strut surface (d) pores-induced microcracks and micro-concaves due to dis -
lodged unmelted Ta powder. 
A.A.A. Aliyu et al.

## Page 10

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
10
4.2. Oxide formation and its effect on LFBF processed Ta 
To reduce oxidation during the LPBF of Ta, high-purity (5 N purity 
with an oxygen level below 1.5 ppm) argon atmosphere was employed. 
However, the presence of secondary oxide, which is believed to be Ta
2
O
5 
and Ta
2
O
3 
were detected in the LPBF processed solid and porous scaf -
folds of Ta. The presence of oxygen was earlier detected by the EDX and 
XPS analysis, which chemically react with Ta to produce a secondary 
oxide. We have to state that, balling which resulted from oxidation 
during LPBF was not observed. Low level control of the oxygen content 
of non-spherical tantalum powder used for spheroidization is believed to 
enhance the purity and control the impurity content of the spherical Ta 
powder [ 45 ]. Nanoscale oxides are apatite formers. They are beneficial 
to the implants by enhancing not only the bone-implant bonding, but 
Fig. 11. ImageJ pores analysis of the LPBF processed D-Ta2 specimen fabricated using high energy settings (a) normal to building direction (b) outline of the pores 
detected at surface area analysis. 
Fig. 12. FESEM micrographs of LPBF processed solid Ta specimens presenting various solidification-induced micropores (a) D-Ta1 (b) D-Ta2, cluster of 
solidification-induced micropores encircled in red (c) D-Ta 3 observed at high magnification to clearly view the solidification-induced micropores (c) D-Ta 3 
revealing the solidification-induced defects and partially fused Ta powder. (For interpretation of the references to colour in this figure legend, the reader is referred to 
the web version of this article.) 
A.A.A. Aliyu et al.

## Page 11

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
11
also its biocompatibility and resistance to corrosion [ 46 , 47 ]. 
4.3. Phases formation during LPBF of ta 
The XRD patterns of LPBF processed Ta revealed various sharp and 
long peaks, which corresponds to BCC Ta. Obviously, the BBC Ta 
diffraction angles increased with increasing energy density. Other fac -
tors that might contribute to the shift of diffraction angles to higher 
values is high residual stress, which resulted in microscopic volume 
expansion and hence, affect the lattice structure of the Ta specimens 
[ 48 ]. Despite high residual stresses developed during LPBF, it does not 
always affect the diffraction angle [ 49 ]. Thus, our findings show no 
significant shift in the angle of diffraction in both infill and borderline 
parameter conditions. Our results are in agreement with the findings 
reported by Zhou, et al. [ 22 ]. At infill parameter conditions, whereby the 
scanning speed is low and the input energy is relatively high, the tem -
perature rises, which resulted in thermal accumulation in the Ta molten 
pool. Heat release by conduction through the LPBF processed Ta de -
creases the residual stress. Thus, widen the diffraction angle of the BCC 
Ta and form a refined microstructure. 
4.4. Microstructure and defects formation during LPBF of ta 
It is apparent that, columnar and equiaxed grains are formed in the 
LPBF processed Ta microstructures, as observed in Fig. 8 . In most situ -
ation, the orientation of the columnar grains occurred parallel to the 
building direction due to thermal gradient in the pool boundaries at the 
liquid/solid interface [ 50 ]. However, sometimes the local variations in 
heat transfer resulted in an inclination between the building and growth 
directions, which causes the columnar grains to grow in a different di -
rection. Formation of equiaxed and fine grains is beneficial to LPBF 
processed Ta by enhancing its ductility (elastic limit) and biomedical 
properties [ 51 ]. Previous report revealed that, columnar grains can be 
completely eliminated through heat treatment [ 23 ]. 
The FESEM microstructural analysis of both solid and porous scaf -
folds of Ta processed through borderline and infill process parameter 
conditions revealed numerous process-induced defects. The micro -
structural defects observed include pores-induced microcracks, 
solidification-induced micropores, solidification-induced microcracks, 
micro-concaves and microgrooves. Unlike structural or designed pores, 
solidification-induced micropores are unintentional or undesigned mi -
cropores, which commonly occur in the LPBF processed part, due to 
vaporization of gasses. During the heating, melting and deposition of the 
top layer, the previous solidified layer will also be slowly heated. As the 
top layer cools rapidly, the shrinkage of such layer is hindered by the 
previous layer, which resulted in a thermal mismatch and hence, re -
sidual stresses are generated. Subsequent relieving of the already 
accumulated residual stresses causes solidification-induced microcracks 
[ 33 ]. The 100 W laser power and 500 mm/s scanning speed parameters 
combination in the borderline parameter settings implies very low laser 
energy (6.7 J/mm
3
), which is insufficient to completely melt the Ta 
powder during the LPBF process. Postprocessing through conventional 
grinding/polishing dislodge the unmelted or partially fuse Ta powder, 
Fig. 13. FESEM images of LPBF processed S-Ta2 specimen (a) surface 
morphology (b) pores-induced microcracks at struts connection (c) cross- 
sectional view of solidification-induced micropores and (d) microgrooves 
Fig. 14. FESEM images of LPBF processed S-Ta3 specimen presenting various process-induced defects (a) pores-induced microcracks (b) pores-induced microcracks 
and micro-concaves (c) partially fused Ta powder and (d) high magnification SEM image revealing the pores-induced microcracks. 
A.A.A. Aliyu et al.

## Page 12

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
12
which resulted to microgrooves and micro-concaves [ 52 ]. In the infill 
parameter settings, the laser power (250 W) and the scanning speed 
(100 mm/s) combination resulted to a high energy density. At this 
condition, Ta powder are highly melted. However, too high energy 
resulted in the instability of the melt pool, which causes a phenomenon 
called balling and the formation of interconnected porosities (pores- 
induced microcracks) ( Fig. 10 ) [ 40 ]. Process-induced defects have to be 
minimized or completely avoided to reduce their detrimental effect on 
the biomedical and mechanical properties of the LPBF built parts, 
thereby enhancing the performance of the fabricated parts [ 53 ]. Proper 
process parameter settings and optimization is proposed as the best 
approach to minimize the process-induced defects during LPBF [ 54 ]. 
4.5. Solidification-induced pores distribution and microhardness 
The percentage area distribution of the porosities formed in the 
fabricated cubic solid D-Ta2 specimen was determined through particle 
analyser commend. The measured pore distribution of 1.19% agrees 
with the simulated results, which has a volumetric pores distribution of 
1.08%. In a similar study, Ghods, et al. [ 55 ] investigated the role of re- 
used Ti-6Al-4 V powder on the porosities and spatial distribution during 
the additive manufacturing of Ti-6Al-4 V material. The average volu -
metric pore distribution of the 3D printed specimens was found to be 0.1 
± 0.02%. The numerical simulation analysing the Ta molten pool 
behaviour and the pore formation mechanism contributes to the better 
understanding of the process parameters and hence, directed for opti -
misation in the future. 
The microhardness results achieved show that, the specimens pro -
cessed via low energy settings has lower hardness. This is caused by 
grain coarsening due to low density coupled with a very high speed (500 
mm/s) [ 22 ]. On the other hand, the high hardness of the LPBF processed 
Ta is caused by grain refining, which strengthened the specimen's sur -
face [ 56 ]. Additionally, the rapid laser solidification resulted in a high 
accumulation of residual stresses during LPBF, which in-turn enhance 
surface hardness [ 57 ]. It has to be noted that, the high hardness-value of 
3D printed Ta trabecular (228 Hv) reported by Yang, et al. [ 26 ] was 
achieved after postprocessing (annealing), which is believed to greatly 
raised its hardness. The as-built Ta has hardness-value of 190 Hv. 
However, this value is still higher than the hardness reported in this 
study. The relatively low hardness achieved in this study, might relate to 
presence of oxygen, which resulted in the formation of thin oxide films 
on the LPFB processed Ta surface. It is obvious that, oxide films like 
Ta
2
O
5 
and Ta
2
O
3 
reduces the hardness of metallic alloys [ 19 ]. 
Fig. 15. Simulation results (a) Low 
energy with laser power = 100 W and 
scanning speed = 500 mm/s param -
eter conditions and (b) high energy 
with laser power = 250 W and scan -
ning speed = 100 mm/s parameter 
conditions (c) cross-section of “ low 
energy ” case where surface melting 
occurs in the conduction mode (d) 
cross-section of “ high energy ” case 
where the keyhole mode appears. The 
keyhole tip exhibits flapping motion 
and micropores are formed accord -
ingly. The liquid/gas interface is 
drawn at one instant and cross- 
sectional shapes at three-time in -
stants are superposed by the solid 
lines with the time interval of 3.5 μ s. 
Fig. 16. Vickers hardness of LPBF processed solid and porous scaffolds of Ta at 
low energy and high energyconditions with corresponding error bars. 
A.A.A. Aliyu et al.

## Page 13

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
13
5. Conclusion 
Additive manufacturing of pure tantalum has been presented to 
understand the microstructure of the solid and porous scaffolds and to 
evaluate the process-induced defects for biomedical applications. The 
following specific conclusion can be drawn: 
(1) The processability, microstructure, defect formation and gener -
ation mechanism, types and geometrical distribution of micro -
structural defects and the dimensional accuracies of the solid and 
porous scaffolds of Ta were successfully studied. 
(2) The microstructure revealed the formation of nanostructures 
with roughness between 3.88 nm to 10.40 nm and a BBC Ta phase 
consisting of columnar, equiaxed and fine grains. Most of the 
specimens contained a short secondary oxide peak. 
(3) Numerous undesired micro features such as solidification- 
induced micropores, pores-induced and solidification-induced 
microcracks, as well micro-concave and microgrooves, resulted 
from dislodged partially fuse Ta powder were assessed. 
(4) The process-induced defects are denser and more prevalent on 
the solid and porous Ta specimens processed through borderline 
parameter settings. However, solidification-induced micropores 
are predominant on the specimens processed through infill 
parameter conditions. 
(5) Porous scaffolds of Ta processed through infill parameter settings 
were found to have maximum microhardness while the lower 
hardness value is observed in the solid Ta processed via border -
line parameter settings. 
(6) The numerical simulation conducted to study the formation and 
defect generation mechanism as well as the volumetric distribu -
tion of the porosities developed during the LPBF of Ta agrees with 
the experimental results. This demonstrates that, the model can 
predict and rationalise the process-induced porosity and gain 
insight into process improvement. 
CRediT authorship contribution statement 
Abdul Azeez Abdu Aliyu: Conceptualization, Formal analysis, 
Writing – original draft, Investigation. Kitti Poungsiri: Data curation, 
Investigation. Junji Shinjo: Software. Chinnapat Panwisawas: 
Writing – review & editing. Roger C. Reed: Visualization. Chedtha 
Puncreobutr: Methodology, Supervision. Krittima Tumkanon: Project 
administration. Surasak Kuimalee: Resources. Boonrat Lohwongwa -
tana: Funding acquisition, Validation, Supervision. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Data availability 
Data will be made available on request. 
Acknowledgments 
The research was funded and supported by the 90th Anniversary of 
Chulalongkorn University Fund (Ratchadaphiseksomphot Endowment 
Fund), Chulalongkorn University, Bangkok, Thailand. PP was supported 
by the Ratchadaphiseksomphot Endowment Fund of Chulalongkorn 
University (RES560530156-HR) and the Research Chair Grant 2012, the 
National Science and Technology Development Agency (NSTDA). We 
also acknowledge the support by the Second Century Fund (C2F), 
Chulalongkorn University, Bangkok, Thailand and Chulalongkorn Aca -
demic Advancement into its 2nd Century Project, Phase 2, 
Chulalongkorn University, Bangkok, Thailand. Chinnapat Panwisawas 
would like to acknowledge the funding from Innovation Fellowship by 
Engineering and Physical Science Research Council (EPSRC), UK 
Research and Innovation (UKRI) (grant number: EP/S000828/2). 
References 
[1] T. Hanawa, Research and development of metals for medical devices based on 
clinical needs, Sci. Technol. Adv. Mater. 13 (6) (2012), 064102. 
[2] R.C. Robertson, Repair of cranial defects with tantalum, J. Neurosurg. 1 (4) (1944) 
227–236. 
[3] J. Black, Biologic performance of tantalum, Clin. Mater. 16 (3) (1994) 167–173. 
[4] R.C. Robertson, W.G. Peacher, The use of tantalum foil in the subdural space, 
J. Neurosurg. 2 (4) (1945) 281–284. 
[5] B.H. Sagherian, R.J. Claridge, The use of tantalum metal in foot and ankle surgery, 
Orthop. Clin. 50 (1) (2019) 119–129. 
[6] Y. Liu, C. Bao, D. Wismeijer, G. Wu, The physicochemical/biological properties of 
porous tantalum and the potential surface modification techniques to improve its 
clinical application in dental implantology, Mater. Sci. Eng. C 49 (2015) 323–329. 
[7] M. Weinmann, C. Schnitter, M. Stenzel, J. Markhoff, C. Schulze, R. Bader, 
Development of bio-compatible refractory Ti/Nb (/Ta) alloys for application in 
patient-specific orthopaedic implants, Int. J. Refract. Met. Hard Mater. 75 (2018) 
126–136. 
[8] H. Matsuno, A. Yokoyama, F. Watari, M. Uo, T. Kawasaki, Biocompatibility and 
osteogenesis of refractory metal implants, titanium, hafnium, niobium, tantalum 
and rhenium, Biomaterials 22 (11) (2001) 1253–1262. 
[9] D.M. Findlay, K. Welldon, G.J. Atkins, D.W. Howie, A.C. Zannettino, D. Bobyn, The 
proliferation and phenotypic expression of human osteoblasts on tantalum metal, 
Biomaterials 25 (12) (2004) 2215–2227. 
[10] M.F. Meijer, et al., Tibial component with and without stem extension in a 
trabecular metal cone construct, Knee Surg. Sports Traumatol. Arthrosc. 25 (11) 
(2017) 3644–3652. 
[11] V.K. Balla, S. Bose, N.M. Davies, A. Bandyopadhyay, Tantalum—a bioactive metal 
for implants, Jom 62 (7) (2010) 61–64. 
[12] C. Dong, X. Bi, J. Yu, R. Liu, Q. Zhang, Microstructural evolution and sintering 
kinetics during spark plasma sintering of pure tantalum powder, J. Alloys Compd. 
781 (2019) 84–92. 
[13] E. Hosseini, M. Kazeminezhad, Dislocation structure and strength evolution of 
heavily deformed tantalum, Int. J. Refract. Met. Hard Mater. 27 (3) (2009) 
605–610. 
[14] C. Sungail, A. Abid, Spherical tantalum feed powder for metal additive 
manufacturing, Metal Powder Rep. 73 (6) (2018) 316–318. 
[15] R. Wauthle, et al., Additively manufactured porous tantalum implants, Acta 
Biomater. 14 (2015) 217–225. 
[16] L. Thijs, M.L.M. Sistiaga, R. Wauthle, Q. Xie, J.-P. Kruth, J. Van Humbeeck, Strong 
morphological and crystallographic texture and resulting yield strength anisotropy 
in selective laser melted tantalum, Acta Mater. 61 (12) (2013) 4657–4668. 
[17] Q. Qin, et al., 3D printing of tantalum parts based on low molecular mass organic 
gel system, Int. J. Refract. Met. Hard Mater. 84 (2019) 105014. 
[18] A. Bandyopadhyay, I. Mitra, A. Shivaram, N. Dasgupta, S. Bose, Direct comparison 
of additively manufactured porous titanium and tantalum implants towards in vivo 
osseointegration, Addit. Manuf. 28 (2019) 259–266. 
[19] C. Sungail, A.D. Abid, Additive manufacturing of tantalum–a study of chemical and 
physical properties of printed tantalum, Metal Powder Rep. 75 (1) (2020) 28–33. 
[20] N. Sri-utenchai, N. Pengrung, K. SrikonKorn, C. Puncreobutr, B. Lohwongwatana, 
P. Sa-ngasoongsong, Using 3D Printing Technology for Corrective Biplanar 
Chevron Osteotomy with Customized Osteotomy Guide and Patient-Matched 
Monoblock Crosslink Plate in Treatment of Cubitus Varus Deformity: A Case Report 
and Technical Note, 2020. 
[21] T. Thomrungpiyathan, S. Luenam, B. Lohwongwatana, W. Sirichativapee, 
K. Nabudda, C. Puncreobutr, A custom-made distal humerus plate fabricated by 
selective laser melting, Comput. Methods Biomech. Biomed. Eng. 24 (6) (2021) 
585–596. 
[22] L. Zhou, T. Yuan, R. Li, J. Tang, G. Wang, K. Guo, Selective laser melting of pure 
tantalum: densification, microstructure and mechanical behaviors, Mater. Sci. Eng. 
A 707 (2017) 443–451. 
[23] L. Zhou, et al., Microstructure tailoring to enhance strength and ductility in pure 
tantalum processed by selective laser melting, Mater. Sci. Eng. A 785 (2020) 
139352. 
[24] C. Chandhanayingyong, K. Srikong, C. Puncreobutr, B. Lohwongwatana, 
R. Phimolsarnti, B. Chuckpaiwong, Three-dimensional printed, proximal 
phalangeal prosthesis with metatarsophalangeal joint arthroplasty for the 
treatment of a giant cell tumor of the fifth toe: the first case report, Int. J. Surg. 
Case Rep. 73 (2020) 84–89. 
[25] G. Zhao, et al., Porous tantalum scaffold fabricated by gel casting based on 3D 
printing and electrolysis, Mater. Lett. 239 (2019) 5–8. 
[26] J. Yang, et al., Additive manufacturing of trabecular tantalum scaffolds by laser 
powder bed fusion: mechanical property evaluation and porous structure 
characterization, Mater. Charact. 170 (2020) 110694. 
[27] J. Yang, et al., Static compressive behavior and material failure mechanism of 
trabecular tantalum scaffolds fabricated by laser powder bed fusion-based additive 
manufacturing, Int. J. Bioprinting 8 (1) (2022). 
[28] V. Livescu, C.M. Knapp, G.T. Gray III, R.M. Martinez, B.M. Morrow, B.G. Ndefru, 
Additively manufactured tantalum microstructures, Materialia 1 (2018) 15–24. 
A.A.A. Aliyu et al.

## Page 14

International Journal of Refractory Metals and Hard Materials 112 (2023) 106132
14
[29] H. Qian, T. Lei, P. Lei, Y. Hu, Additively manufactured tantalum implants for 
repairing bone defects: a systematic review, Tissue Eng. B Rev. 27 (2) (2021) 
166 – 180 . 
[30] H. Taheri, M.R.B.M. Shoaib, L.W. Koester, T.A. Bigelow, P.C. Collins, L.J. Bond, 
Powder-based additive manufacturing-a review of types of defects, generation 
mechanisms, detection, property evaluation and metrology, Int. J. Addit. Subtract. 
Mater. Manuf. 1 (2) (2017) 172 – 209 . 
[31] T. Yamamoto, M. Hara, Y. Hatano, Effects of fabrication conditions on the 
microstructure, pore characteristics and gas retention of pure tungsten prepared by 
laser powder bed fusion, Int. J. Refract. Met. Hard Mater. 95 (2021) 105410 . 
[32] H. Gong, K. Rafi, H. Gu, G.J. Ram, T. Starr, B. Stucker, Influence of defects on 
mechanical properties of Ti – 6Al – 4 V components produced by selective laser 
melting and electron beam melting, Mater. Des. 86 (2015) 545 – 554 . 
[33] A. Sola, A. Nouri, Microstructural porosity in additive manufacturing: the 
formation and detection of pores in metal parts fabricated by powder bed fusion, 
J. Adv. Manuf. Process 1 (3) (2019) e10021 . 
[34] N.J. Harrison, I. Todd, K. Mumtaz, Reduction of micro-cracking in nickel 
superalloys processed by selective laser melting: a fundamental alloy design 
approach, Acta Mater. 94 (2015) 59 – 68 . 
[35] J. Shinjo, C. Panwisawas, Digital materials design by thermal-fluid science for 
multi-metal additive manufacturing, Acta Mater. 210 (2021) 116825 . 
[36] R. Wauthl ´e, J.-P. Kruth, M. Montero Sistiaga, L. Thijs, J. Van Humbeeck, New 
opportunities for using tantalum for implants with additive manufacturing, Eur. 
Cells Mater. 26 (2013) . 
[37] E. Seki, et al., Effect of heat treatment on the microstructure and fatigue strength of 
CoCrMo alloys fabricated by selective laser melting, Mater. Lett. 245 (2019) 53 – 56 . 
[38] A. Dewaele, M. Mezouar, N. Guignot, P. Loubeyre, High melting points of tantalum 
in a laser-heated diamond anvil cell, Phys. Rev. Lett. 104 (25) (2010) 255701 . 
[39] E. Yasa, J.-P. Kruth, J. Deckers, Manufacturing by combining selective laser 
melting and selective laser erosion/laser re-melting, CIRP Ann. 60 (1) (2011) 
263 – 266 . 
[40] X. Nong, X. Zhou, Y. Ren, Fabrication and characterization of Fe-based metallic 
glasses by selective laser melting, Opt. Laser Technol. 109 (2019) 20 – 26 . 
[41] Z. Wang, et al., Analysis of factors influencing bone ingrowth into three- 
dimensional printed porous metal scaffolds: a review, J. Alloys Compd. 717 (2017) 
271 – 285 . 
[42] V.K. Balla, S. Banerjee, S. Bose, A. Bandyopadhyay, Direct laser processing of a 
tantalum coating on titanium for bone replacement structures, Acta Biomater. 6 (6) 
(2010) 2329 – 2334 . 
[43] G. Marinelli, F. Martina, S. Ganguly, S. Williams, Microstructure, hardness and 
mechanical properties of two different unalloyed tantalum wires deposited via wire 
+ arc additive manufacture, Int. J. Refract. Met. Hard Mater. 83 (2019) 104974 . 
[44] Y. Zheng, Q. Han, J. Wang, D. Li, Z. Song, J. Yu, Promotion of osseointegration 
between implant and bone interface by titanium alloy porous scaffolds prepared by 
3d printing, ACS Biomater. Sci. Eng. 6 (9) (2020) 5181 – 5190 . 
[45] Z. Jin, C. He, J. Fu, Q. Han, Y. He, Balancing the customization and 
standardization: exploration and layout surrounding the regulation of the growing 
field of 3D-printed medical devices in China, Bio-design Manuf. (2022) 1 – 27 . 
[46] M.R.S.N. Hazwani, L.X. Lim, Z. Lockman, H. Zuhailawati, Fabrication of titanium- 
based alloys with bioactive surface oxide layer as biomedical implants: opportunity 
and challenges, Trans. Nonferrous Metals Soc. China 32 (1) (2022) 1 – 44 . 
[47] P. Grewe, et al., Stents: material, surface texture and design, in theory and practice, 
Minim. Invasive Ther. Allied Technol. 11 (4) (2002) 157 – 163 . 
[48] J. Moyer, G. Ansell, The volume expansion accompanying the martensite 
transformation in iron-carbon alloys, Metall. Trans. A. 6 (9) (1975) 1785 – 1791 . 
[49] D. Gu, Y.-C. Hagedorn, W. Meiners, K. Wissenbach, R. Poprawe, Nanocrystalline 
TiC reinforced Ti matrix bulk-form nanocomposites by selective laser melting 
(SLM): densification, growth mechanism and wear behavior, Compos. Sci. Technol. 
71 (13) (2011) 1612 – 1620 . 
[50] B.E. Carroll, T.A. Palmer, A.M. Beese, Anisotropic tensile behavior of Ti – 6Al – 4V 
components fabricated with directed energy deposition additive manufacturing, 
Acta Mater. 87 (2015) 309 – 320 . 
[51] Z. Zhao, J. Chen, H. Tan, G. Zhang, X. Lin, W. Huang, Achieving superior ductility 
for laser solid formed extra low interstitial Ti-6Al-4V titanium alloy through 
equiaxial alpha microstructure, Scr. Mater. 146 (2018) 187 – 191 . 
[52] D.D. Gu, W. Meiners, K. Wissenbach, R. Poprawe, Laser additive manufacturing of 
metallic components: materials, processes and mechanisms, Int. Mater. Rev. 57 (3) 
(2012) 133 – 164 . 
[53] B. Zhang, Y. Li, Q. Bai, Defect formation mechanisms in selective laser melting: a 
review, Chin. J. Mech. Eng. 30 (3) (2017) 515 – 527 . 
[54] T. Gustmann, et al., Influence of processing parameters on the fabrication of a Cu- 
Al-Ni-Mn shape-memory alloy by selective laser melting, Addit. Manuf. 11 (2016) 
23 – 31 . 
[55] S. Ghods, et al., Electron Beam Additive Manufacturing of Ti6Al4V: Evolution of 
Powder Morphology and Part Microstructure with Powder Reuse, Mater 9 (2020) 
100631 . 
[56] Q. Li, et al., A comprehensive study of tantalum powder preparation for additive 
manufacturing, Appl. Surf. Sci. 593 (2022) 153357 . 
[57] E. Santos, K. Osakada, M. Shiomi, Y. Kitamura, F. Abe, Microstructure and 
mechanical properties of pure titanium models fabricated by selective laser 
melting, Proc. Inst. Mech. Eng. C J. Mech. Eng. Sci. 218 (7) (2004) 711 – 719 . 
A.A.A. Aliyu et al.
