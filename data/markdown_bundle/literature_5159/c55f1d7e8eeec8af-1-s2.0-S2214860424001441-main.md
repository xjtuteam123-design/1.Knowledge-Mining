# 1-s2.0-S2214860424001441-main

<!-- source: D:\总文献\1-s2.0-S2214860424001441-main.pdf -->
<!-- file_sha256: 6b4ff6e5de59fd5e00d9345a9b0649dca1c2aa8897359579802c51b28c22cdbf -->

## Page 1

Additive Manufacturing 84 (2024) 104098
Available online 22 March 2024
2214-8604/© 2024 Elsevier B.V. All rights reserved.
A new approach to design advanced superalloys for additive manufacturing 
Wei Song
a , b
, Junying Yang
a , b
, Jingjing Liang
a , *
, Nannan Lu
a
, Yizhou Zhou
a
, Xiaofeng Sun
a
, 
Jinguo Li
a , * 
a
Shi-changxu Innovation Center for Advanced Materials, Superalloys Division, Institute of Metal Research, Chinese Academy of Sciences, 72 Wenhua Road, Shenyang 
110016, China 
b
School of Materials Science and Engineering, University of Science and Technology of China, Shenyang 110016, China 
ARTICLE INFO 
Keywords: 
New alloy design approach 
Additive manufacturing 
Nickel-based superalloys 
Cracking resistance mechanisms 
Mechanical properties 
ABSTRACT 
A novel approach centered on a high Ta/Al ratio and a significant dependence on the boundary composition 
addressed the challenges in the manufacturability and material performance of additive-manufactured nickel 
(Ni)-based superalloys. This approach integrated alloy composition, defect management, and mechanical 
behavior considerations. This study investigated the impact of this approach on microstructural characterization, 
solidification behavior, elemental microsegregation, and precipitation, demonstrating its efficacy in crack 
resistance and performance enhancement. Ultimately, this approach facilitated the successful design of a crack- 
free Ni-based superalloy, ZGH451 – 1, featuring a high γ ′ -phase content. Extensive comparisons of mechanical 
properties, including tensile and creep tests, against reported AM-ed superalloys and partially heat-treated first- 
generation Ni-based single-crystal superalloys validated the superior mechanical properties and processability of 
the newly designed alloy. The rationality and feasibility of this approach for achieving collaborative optimization 
of properties and formability were demonstrated, paving the way for the design of new high-performance su -
peralloys suitable for additive manufacturing. 
1. Introduction 
Nickel-based superalloys, renowned for their exceptional high- 
temperature performance and operational reliability [1 – 3] , have 
extensive applications in the fabrication of turbine blades and vanes for 
advanced aircraft engines. Traditionally, these superalloys have been 
produced through casting, powder metallurgy, or wrought stock 
methods, which are limited in their ability to manufacture intricate 
components. These conventional processes, with their intricate steps 
and material wastage, impede further advancement of superalloys. Ad -
ditive manufacturing (AM) is a burgeoning technology wherein 
three-dimensional parts are designed digitally and then fabricated 
layer-by-layer under computer control, offering near-net-shape pro -
duction [4 – 6] . This innovative approach holds promise for addressing 
current challenges by offering superior precision, enhanced material 
utilization, and unprecedented design flexibility [7,8] . 
However, the local high-energy input and repeated heating inherent 
[9] in the layer-by-layer printing process of metal-based materials lead 
to a complex thermal history and the formation of defects, such as cracks 
and pores [10 – 13] . This issue is particularly notable in the AM of 
nickel-based superalloys, thus impeding their widespread application. 
The key contributing factors include: (i) the wide freezing range of al -
loys, where the addition of solid solution-strengthened refractory ele -
ments (W, Mo, Cr, and Co) and precipitation-strengthened elements (Al, 
Ti, Ta, and Nb) extends the freezing range [14 – 18] ; (ii) elemental 
segregation and the formation of liquation sources, wherein local 
enrichment of elements such as Al, Ti, Ta, C and Hf during solidification 
induces solute segregation, lowering the local liquidus temperature and 
resulting in the formation of low-melting-point phases between solid 
dendrites, which can lead to crack formation during printing [19 – 23] ; 
and (iii) internal residual stresses, comprising thermal stress and phase 
transformation stress, both of which contribute to unstable microstruc -
tures. High level of residual thermal stress can rupture high-angle grain 
boundaries or liquid films [24 – 26] , forming cracks, whereas phase 
transformation stress arises from the precipitation and growth of the γ’ 
phase during cyclic intrinsic heating. The rapid and extensive precipi -
tation of the γ’ phase can induce a significant stress concentration, 
leading to cracking between the γ and γ’ phases. 
Thus, weldable alloys typically possess a lower degree of alloying 
and lack a high-temperature strengthening γ ′ phase. Such AM-ed 
* Corresponding authors. 
E-mail addresses: jjliang@imr.ac.cn (J. Liang), jgli@imr.ac.cn (J. Li). 
Contents lists available at ScienceDirect 
Additive Manufacturing 
journal homepag e: www.else vier.com/loc ate/addma 
https://doi.org/10.1016/j.addma.2024.104098 
Received 26 October 2023; Received in revised form 16 February 2024; Accepted 21 March 2024

## Page 2

Additive Manufacturing 84 (2024) 104098
2
superalloys are commonly employed in medium-to low-temperature 
applications, exemplified by materials such as IN718 and IN625 [27,28] . 
Conversely, classical high-performance engineering superalloys such as 
second-generation single-crystal superalloys CMSX-4 and CM247LC [29, 
30] exhibit a notable propensity for cracking during AM, which is 
attributed to their high volume fraction of the strengthening phase γ ′ 
( > 60%) and the presence of numerous refractory elements. Wang et al. 
[31] attributed the crack-free fabrication of Ni-based single-crystal Ren ´e 
N5 via DED to a high fraction of low-angle grain boundaries (LAGBs). Ci 
et al. [32] observed gradual eutectic increase during deposition in DD32 
single crystal Ni-base superalloy repaired by laser metal forming, lead -
ing to cracking and reduced tensile properties in the heat-affected zone 
(HAZ). Xu et al. [33] suppressed the hot cracking formation of DD98M 
fabricated by DED via using a continuous scanning strategy, while 
several liquation and solidification cracks still occurred in alloy due to 
the stable liquid film on high-angle grain boundaries (HAGBs). Despite 
extensive research on cracking mechanisms, complete control over crack 
formation remains elusive [34 – 36] . Process optimization alone cannot 
entirely eliminate micro-defects with intricate structures [37] , high -
lighting the urgent need for new alloy designs tailored for AM. 
Various composition design methods have recently emerged for the 
alloys used in AM. Tang et al. [38] introduced an alloys-by-design (ABD) 
method grounded in computational modeling, resulting in the devel -
opment of two alloys featuring a medium volume fraction of the γ ′ phase 
(20% – 30%). T. M. Pollock et al. [39] devised a defect-resistant Co – Ni 
superalloy, SB-CoNi-10, based on the Co-Al-W alloy system through a 
series of calculations, achieving a high volume fraction of the γ ′ phase 
(~70%). These successful design and optimization endeavors under -
score the capability of elemental regulation to generate novel superalloy 
grades. However, prior methods for designing new alloys for AM-ed 
Ni-based superalloys predominantly focused on attaining crack-free al -
loys with a medium-low volume fraction of the γ’ phase or susceptibility 
to γ’ structure deterioration, failing to sufficiently meet the 
high-temperature mechanical requirements for turbine blade prepara -
tion. To address this gap and develop an alloy suitable for turbine blade 
preparation, a balance between a high γ’ volume fraction and a low 
cracking susceptibility is imperative. This dual consideration ensured 
excellent mechanical properties and formability. 
This study introduced a novel approach to alloy design by controlling 
the composition of γ’ -forming elements, including Al, Ti, and Ta, with a 
particular focus on the Ta/Al ratio, utilizing d-electron alloy theory and 
Thermal-Calc (with the TCNI10 database). Adjusting the γ’ -forming 
element content and the Ta/Al ratio resulted in a narrow freezing range, 
minimal solute segregation, and slow precipitation of the γ’ phase. This 
adjustment effectively mitigated the stress concentration during late 
solidification or phase transformation, consequently reducing suscepti -
bility to liquid/solid-mediated cracking. 
2. Principles and methods for alloy design 
The primary principle guiding the design of advanced AM-enabled 
superalloys is to achieve a high volume fraction of γ’ phase while 
minimizing crack susceptibility. To attain a substantial γ’ phase content, 
elements such as Al, Ti, and Ta were selected. Al served as a key 
γ’ -forming element based on its molecular formula (Ni
3
Al, L1
2
) [40] . Ta, 
which possesses a larger atomic radius, aided in regulating the size and 
morphology of the γ’ -precipitates, and reinforcing them [41] . The in -
clusion of Ti was aimed at ensuring resistance to hot corrosion and 
maintaining a sufficient γ’ content. Notably, Nb was omitted because of 
its high tendency to form Laves phases [42] , which are detrimental to 
the performance. Consequently, the γ’ phase composition in our target 
alloy was denoted as Ni
3
(Al, Ti, Ta). 
The novel procedure involved navigating the composition design 
space comprising Al, Ti, and Ta elements to narrow down the selection 
range based on predetermined screening conditions for the γ’ volume 
fraction and cracking factors [43 – 45] . Subsequently, the potential 
compositions of the new alloys were further identified. The design of Al, 
Ti and Ta is based on the alloy 
7 – 9 W-7 – 9Cr-7 – 9Co-1 – 3Mo-0.01 C-0.015B-Bal.Ni (wt%). This study 
employed computationally intensive thermodynamic modeling along -
side conventional alloy design methods to rationalize the composition 
determination. More than 10
3 
alloys, including traditional variants, 
were evaluated during the design phase. Further elaboration of this 
process is shown in Fig. 1 . 
Maximizing the γ’ phase content in the new alloy is essential for 
achieving superior mechanical properties [46] at elevated temperatures. 
Strengthened γ’ phase with a cubic shape and appropriate size is crucial. 
Employing solution strengthening and precipitation strengthening 
mechanisms within the γ’ phase effectively impeded dislocation motion 
and facilitated the formation of stable interface structures, such as 
dislocation networks. These enhancements significantly bolstered the 
alloy ’ s ability to withstand damage and prevent failure. 
This study considered three methods to decrease cracking sensitivity. 
First, a narrow freezing range was used to mitigate solidification-related 
cracks. The freezing range of the alloy was determined through Scheil 
analysis of non-equilibrium solidification utilizing the TCNI10 database 
(assuming no back-diffusion). Second, the low strain-age cracking (SAC) 
merit index was evaluated with reference to Prager – Shira weldability 
diagrams [47] , which assess cracking during thermal cycling and 
post-processing in the solid state. Finally, minimizing element segrega -
tion during the final liquid solidification enhanced the resistance to 
liquid-film-related cracking. Notably, the elements content in solid was 
not utilized because of inaccuracies in reflecting the segregation 
behavior amidst diverse phases (such as γ matrix, γ’ phase, and carbide). 
Additionally, microstructural structural stability was evaluated using 
the d-electron alloy theory [48] to prevent the formation of topological 
close-packed (TCP) phases. The final alloy compositions were deter -
mined through a comprehensive analysis of all calculated factors. 
Fig. 2 illustrates the selection of the alloy compositions within the 
design space and the corresponding calculated results. Initially, the 
composition range of Al, Ti, and Ta was determined based on the design 
objective of achieving a 40% – 60% volume fraction of the γ’ phase. 
Analysis of Figs. 2 (a) and 2 (b) revealed a strong positive correlation 
between the γ’ phase content and Al, with Ta and Ti serving to supple -
ment this effect. Notably, Al exhibited greater efficiency in forming γ’ 
phase compared to Ta ( Fig. 2 (a)), suggesting that a higher Ta content is 
required to achieve a substantial γ’ phase fraction when Al and Ti levels 
decrease. Leveraging this contrary influence trend of Ta and Al on the γ’ 
fraction, namely, a high Ta/Al ratio, proved efficient in controlling the γ’ 
phase level. The controlled γ’ content not only regulated solid-state 
cracking by reducing the phase transformation stress but also 
enhanced the properties. A high content of Ta and γ’ phases is expected 
to enhance the mechanical properties [49,50] , as supported by the sta -
tistical results provided in the Supplementary Material. Hence, a high 
Ta/Al ratio was a crucial prerequisite for a new compositional design 
approach. Additionally, the use of Ti was gradually being reduced or 
eliminated in higher-generation casting alloys [40,51] owing to its 
adverse impact on structural stability. However, given its beneficial ef -
fects on hot corrosion resistance and ensuring adequate γ’ content in 
alloys, a low level of Ti was incorporated. 
Fig. 2 (c) illustrates the relationship between the Scheil freezing 
range and γ’ phase content. It is evident that the alloys closer to the top 
exhibited higher crack sensitivities. A freezing range of 300 K, posi -
tioned between non-printable alloy IN939 [52] (320 K) and readily 
printable alloy IN718 [53] (255 K), was chosen as the boundary value 
for low/high crack sensitivity. Many printable alloys have freezing 
ranges close to or below this boundary value (e.g., alloys of Inconel and 
ABD). Therefore, while maximizing the γ’ phase fraction, the design 
objective was to align the freezing range as closely as possible to the 
boundary value (300 K). 
In Fig. 2 (d), the variation in the element content during the final 
solidification with increasing Ta levels is depicted. With higher Ta 
W. Song et al.

## Page 3

Additive Manufacturing 84 (2024) 104098
3
content, elements such as Ti, C, B, and Mo notably decreased, while 
others such as W, Co, Cr, and Al exhibited slight increases. Specifically, a 
high Ta/Al ratio, characterized by high Ta levels and low Al content, can 
reduce element aggregation during the final solidification. This reduc -
tion is advantageous in mitigating the occurrence of low-melting-point 
phases and effectively regulating solidification/remelting-related 
cracking. 
Regarding high-strain-age cracking, Figs. 2 (e) and 2 (f) depict the 
trade-off among weldability originating from the welding community 
[47] , SAC merit index and expected volume fraction of the γ’ phase. 
With an increase in the γ’ phase content, the risk of cracking also 
increased. An alloy composition near the boundary (~6 wt% Al in Fig. 2 
(e)) was preferable to preserve a higher fraction of the γ’ phase. Simi -
larly, a maximum SAC merit index of 4.7 was chosen ( Fig. 2 (f)), posi -
tioned between the reported weldable alloy ABD-900AM [38] (3.9) and 
the non-weldable alloy IN792 [54] (5.1). Additionally, comprehensive 
considerations included ensuring that Ti + Al < 6 wt%, a value of 
metal-d levels M
d 
< 0.99, and an electron vacancy number N
V. 
< 2.44 
[48] . 
Overall, the primary design concept for synergistically enhancing the 
mechanical properties and formability is characterized by a high Ta/Al 
ratio and significant dependence on the boundary composition (such as 
regions near freezing range of low/high crack sensitivity in Fig. 2 (c) or 
near SAC merit index of weldable/non-weldable in Fig. 2 (f)). This 
approach effectively controls and strengthens the γ’ phase by adjusting 
the Ta/Al ratio, suppressing the formation of low-melting-point phases 
between dendrites, narrowing the freezing range of the alloy, and ulti -
mately reducing its crack sensitivity, while improving its mechanical 
properties. Building on this analysis, a crack-free alloy, ZGH451 – 1, with 
a high γ’ content was successfully developed and fabricated using 
directed energy deposition (DED). Moreover, to validate the rationality 
and feasibility of this approach, two other alloys, ZGH451 – 2 and 
ZGH451 – 3, with varying Ta/Al ratios were also analyzed under 
identical conditions. 
3. Experimental procedures 
3.1. Alloys for directed energy deposition (DED) 
ZGH451 – 1, ZGH451 – 2, and ZGH451 – 3 have different Ta/Al ratio 
(0.8 – 1.3) and similar contents of γ ′ -forming elements (Al + Ti + Ta). The 
spherical powder was fabricated by argon gas atomization, of which the 
D50 is about 95 – 110 μ m. The composition of each alloy powder shown 
in Table 1 was determined by inductively coupled plasma-optical 
emission spectroscopy (ICP-OES) and ICP-combustion analysis. 
Table 2 shows the thermodynamic and d-electron theory calculation 
results of three alloys. Moreover, the substrates with the same compo -
sition of each alloy prepared by vacuum melting furnace were 
employed. 
3.2. Process parameters of DED 
To ensure the unique impact of alloy composition on defect forma -
tion and mechanical properties, all alloys were produced by a similar 
build strategy and laser parameters. A CO
2 
laser deposition machine 
assembled by Institute of Metal Research, Chinese Academy of Sciences, 
with a maximum laser power of 2.5 KW was employed for printing. This 
machine had four coaxial nozzles with argon shielding gas channels to 
transport powders and avoid oxidation. According to dozens of pro -
cessing parameters optimization were investigated including laser 
power from 1500 W to 2000 W with 100 W interval, scanning speed 
from 900 to 1300 mm/min with 100 mm/min interval, powder feeding 
rate from 9 to 11 g/min with 0.5 g/min interval. The processing pa -
rameters used in this work are confirmed as: laser power 1700 W, 
powder feeding rate 10.5 g/min, scanning speed 1100 mm/min, laser 
beam diameter 2.0 mm, beam-on time 0.16 s and the beam-off time 
Fig. 1. Diagrammatic sketch of the main process of new way. 
W. Song et al.

## Page 4

Additive Manufacturing 84 (2024) 104098
4
Fig. 2. Alloy design space and relevant results calculated for superalloy obtained by new way, including several heritage alloys for verification. (a & b) display the 
tendency of γ’ fraction with content of Al, Ta and Ti at 900 º C, respectively, calculated by Thermal-Calc (with TCNI10 database). (c) shows the relationship between 
Scheil freezing rang and γ’ fraction. (d) illustrates the segregating behavior of elements in final liquid with change of Ta content at 1350 º C. (e & f) presents the design 
space limited by weldability diagram and strain-age cracking merit index in relation to γ’ fraction. 
Table 1 
Alloy composition for current study in wt% (Ni-base), measured using ICP-OES, ICP-combustion (carbon) and Spark OES (boron). 
Alloy Co + Cr + W + Mo Al Ti Ta C B Ta/Al Ni 
ZGH451 – 1 26 4.30 1.22 5.50 0.01 0.01 1.3 Bal 
ZGH451 – 2 26 4.50 1.40 4.50 0.01 0.01 1.0 Bal 
ZGH451 – 3 26 5.00 1.23 4.10 0.01 0.01 0.8 Bal 
W. Song et al.

## Page 5

Additive Manufacturing 84 (2024) 104098
5
0.4 – 0.6 s. The schematic illustration of the scan strategy is shown in 
Fig. 3 (a). The laser moves in a straight line in each cladding layer and is 
scanned perpendicular to the motion direction of the previous layer, 
with the powder-feeding head raised by one layer. Before sample 
printing, the laser will scan on the substrate surface several times 
without powder-feeding to preheat the substrate to diminish the tem -
perature gradient. 
3.3. Microstructure observation 
The microstructures were examined by a Zeiss optical microscope 
(OM) and Thermo Scientific Apreo 2 field emission gun scanning elec -
tron microscope (FEG-SEM) on longitudinal (X-Z) sections of the DED 
specimens, which are parallel to the build direction (Z). Since defect 
distribution was the main research content, the backscattered electron 
(BSE) images of the X-Z plane surface were obtained at 20 kV to accu -
rately distinguish the cracks, holes, precipitates, and grain boundaries. 
Samples were chemically etched in a solution of CuCl
2 
(50 g) + HCl 
(100 ml) + C
2
H
5
OH (100 ml) for 15 s or electrolytically etched using 
30% phosphoric acid at 8 V direct current for 5 s, which etches away the 
γ ′ and γ matrix, respectively and highlights the unetched areas. 
Furthermore, samples after vibration polishing were investigated by 
electron backscattered diffraction (EBSD) system to characterize crystal 
orientation (included inverse pole figure (IPF) and pole figure maps), 
texture and geometrically necessary dislocation (GND) distribution in 
the as-printed microstructures. The electron probe microanalysis 
(EPMA) was applied to measure the dendrite ’ s and interdendritic ’ s local 
chemical composition to characterize the element segregation degree. 
3.4. Quantification of cracks and precipitates 
The characterization of cracks and precipitates were observed and 
quantified by digitized optical, SEM and BSE micrographs. The images 
were obtained from the longitudinal (X-Z) plane, which was parallel to 
the building direction (Z) and sectioned at the central area of samples 
(20 cm away from the top and bottom ( Fig. 3 (b)). Samples were polished 
with sandpaper (150#~2000#) and a silica water-solubility polishing 
paste (W2.5) based on the standard metallographic procedures. The 
degree of cracking in each material was captured randomly in bulk; 
here, the border and bulk were not distinguished in detail due to iden -
tical distributions of cracks. The distribution features of precipitates, 
such as carbides and γ ′ phase, were collected in the same regions. For 
each analysis, more than ten pictures from several random locations 
were captured and summed (~8 mm
2 
and 0.002 mm
2 
for cracks and 
phases in area, respectively) for quantitative statistics. The ImageJ Pro 
software was then used for measuring the size (length or width) and Per 
Area (Obj./Total: the ratio of area of objective to total) of cracks and 
precipitates. The cracking density was approximately replaced with 
Obj./Total, regarded as area percent or volume fraction. 
3.5. Mechanical properties testing 
The tensile testing was carried out on an AG-250KNE machine at 
room temperature, 760 º C and 1000 º C for estimating the mechanical 
properties of the as-fabricated alloys. The tested specimens were 
sectioned parallel to the building direction from the cube samples 
printed with identical process parameters. The size of the tested 
specimens was the cylindrical shape bars with a gauge length and 
diameter of 20 mm and 3 mm, thread segment diameter of 6 mm and 
total length of 47 mm, namely standard M6 φ 3 tensile bars. The surface 
of the specimens was polished clean and smooth. More than 3 samples 
were tested under each test conditions, and all tests were conducted 
under atmospheric environment. The uniaxial loading was applied along 
with the build direction at a strain rate of 1.67 × 10
 3 
s
 1
. Moreover, to 
reduce the risk of cracking induced by the phase transformation during 
heating to the middle-high temperature, a rapid heating rate of 120 K/s 
was employed. The stress rupture of the alloys was conducted at 760 º C/ 
780 MPa and 980 º C/260 MPa on an F-25 creep testing machine. The 
samples for stress rupture had the same size as the ones for tensile test. 
3.6. Differential scanning calorimetry (DSC) 
Differential scanning calorimetry was used to approximately acquire 
the critical phase transformation temperatures during the process of 
melting and solidification, which was contributed to rationalizing our 
findings about the revolution of microstructures and defects. The as- 
fabricated samples were cut using electrical discharge machining 
(EDM) into small cylinders with 3 mm in diameter and 1.5 mm in 
height. The tests were carried out in a flowing argon atmosphere (20 ml/ 
min) at a heating rate of 5 º C/min to 1420 º C, held for 15 mins and then 
cooled at the same rate. The cooling and heating curves of each alloy 
were obtained. 
4. Results 
4.1. Observation of microstructure: as-printed, powders and defects 
Fig. 3 presents an overview of the microstructures of the three alloys, 
including both the as-printed specimens and the powders. All samples 
were collected from the middle section of the bars, approximately 20 cm 
from the top and bottom, to mitigate any influence of unstable structures 
induced by the DED process during the experimental analysis. The 
observation direction was parallel to the building direction, namely, the 
X-Z plane ( Figs. 3 (a) and 3 (b)). Additionally, Figs. 3 (c) – 3 (e) demon -
strated that the initial morphology of the powders is consistent, exhib -
iting a near-spherical shape with minimal satellites and irregular 
particles. Laser diffractometry confirmed that the powder distributions 
fell within the same size range ( Figs. 3 (o) – 3 (q)), with average values of 
D10, D50, and D90 of approximately 60 μ m, 105 μ m, and 168 μ m, 
respectively ( Fig. 3 (r)). This suggests that any disturbances from the 
powder characteristics, such as size, surface topography, and defects, 
were excluded. 
OM images ( Figs. 3 (f) – 3 (h)) revealed that the microstructure of the 
alloys consisted of typical columnar grains growing along the build di -
rection. Within these grains, numerous dendrites exhibited epitaxial 
growth perpendicular to the fusion line, with fewer dendrites tilting 
parallel to the scanning speed direction. Notably, cracks were promi -
nently visible in ZGH451 – 2 and ZGH451 – 3, with widths ranging from to 
100 – 200 μ m and lengths exceeding 1 mm. In contrast, ZGH451 – 1 
exhibited no cracks under identical conditions. Fig. 3 (s) illustrates that 
the crack densities in the two control alloys were 0.8% and 1.1%, 
respectively, as estimated by the area percentage. 
Further analysis of the SEM images ( Figs. 3 (i) – 3 (k)) revealed clear 
distinctions between the dendrite core (DC), interdendritic region (IR), 
and primary dendrite arms. Some pore defects, attributed to gas 
entrapment or inadequate powder fusion, were evident in the IR. The 
former pores typically arise from the escape of shielding gas or metallic 
vapor and appear as small, regular spheres. Irregular pores resulting 
from inadequate powder fusion contain unmelted powder particles. 
Since both types of pores are rare and minor, their impact was dis -
regarded and not elaborated upon in this study. Figs. 3 (l) – 3 (n) depict the 
enlarged SEM morphology of DC and IR following electrolytic etching, 
revealing low cubicity with a certain degree of sphericity and fine γ ′ 
Table 2 
Some calculated results of three alloys based on the d-electrons alloy theory, 
Thermal-Calc and alloy design experiences of welding. 
Alloy M
d 
N
V. 
calculated γ’ volume fraction (%) Ti + Al (wt%) 
ZGH451 – 1 0.95 1.92 48 5.52 
ZGH451 – 2 0.97 1.95 51 5.90 
ZGH451 – 3 0.98 2.01 56 6.23 
W. Song et al.

## Page 6

Additive Manufacturing 84 (2024) 104098
6
phase precipitation in both regions owing to intrinsic heating cycling. 
Moreover, uniformly distributed MC-type carbides were observed in 
both DC and IR. Finally, several critical microstructure parameters were 
quantitatively examined, including the primary dendrite arm spacing 
(PDAS), γ ′ phase size in DC/IR, and defect formation (as detailed in 
Table 3 ). 
4.2. Characteristic of cracks 
Detailed observations of OM and SEM (SE or BSE) images ( Figs. 4 – 6 ) 
were conducted to characterize the crack types and confirm the cracking 
modes. Crack classification was based on fractography, location, and 
surrounding precipitates, considering previous reports on cracking 
Fig. 3. Overall inspection and analysis of as-built microstructures and corresponding powder of alloy ZGH451-1, ZGH451-2 and ZGH451-3, structures observed 
parallel to building direction (X-Z plane). (a, b) shows the diagrammatic sketch of DED process and the XZ-planes sectioned location from each cube. (c-e) are the 
SEM images of powders. (f-h) displays the OM images of typical columnar grains structures of the X-Z plane and (i-k) are the SEM images of dendrites in these. (l-n) 
are the magnified dendrites by SEM, which illustrates the DC, IR, tiny γ ′ phase and MC carbides. (o-r) demonstrates the consistent relationships between size and 
morphology of three alloy powders. (s) shows the cracking degree of alloys estimated by area percentage. 
W. Song et al.

## Page 7

Additive Manufacturing 84 (2024) 104098
7
behavior in other AM-ed superalloys [55,56] and the welding literature 
[47] . Cracks were divided into two categories: (i) heating-related cracks, 
such as solidification cracks (resulting from direct hot tearing) and 
liquation cracking (associated with intrinsic heating) and (ii) solid-state 
cracks (resulting from phase transformation). Crack features were pri -
marily illustrated based on the alloys ZGH451 – 2 and ZGH451 – 3. 
Fig. 4 depicts the solidification cracks in alloys ZGH451 – 2 and 
ZGH451 – 3 on the X-Z plane. These cracks form owing to insufficient 
liquid remaining to sustain solid-phase growth, particularly dendritic 
growth, during the final stages of solidification. Consequently, the so -
lidification shrinkage strain perpendicular to the cracking direction in 
the solid/liquid coexisting zone fractured the remaining liquid phase. 
Notably, a distinguishing characteristic of these cracks was the larger 
gap between the two cleavage surfaces and the presence of solidification 
dendrite arms, typically observed in the IR ( Figs. 4 (c) and 4 (f)). Addi -
tionally, nanometer-sized carbides ( Figs. 4 (b) and 4 (e)) can obstruct the 
liquid-filled channel, hindering liquid filling and resulting in cracks with 
shrinkage cavities, which represents another typical feature. Solidifica -
tion cracks can be effectively differentiated based on their location and 
structures. 
Table 3 
Several important characteristic parameters of three alloys such as, PDAS, size of 
γ ′ phase in DC/IR and defect formation. 
Alloy γ ′ size of DC/IR 
(nm) 
PDAS 
( μ m) 
Cracking Porosity Lack of 
fusion 
ZGH451 – 1 44.7/50.9 
± 0.23 
17.8 
± 0.15 
N Y Y 
ZGH451 – 2 52/60 ± 0.31 20.5 
± 0.21 
Y Y Y 
ZGH451 – 3 40.5/49.1 
± 0.27 
24.2 
± 0.18 
Y Y Y 
Fig. 4. Solidification crack observed in alloy ZGH451-2 (a-c) and ZGH451-3 (d-f) of as-built microstructure on X-Z plane. Cracks are shown typical features of: 
primary dendrite arms, shrinkage cavity and located in IR. 
Fig. 5. Liquation crack observed in alloy ZGH451-2 (a-c) and ZGH451-3 (d-f) of as-built microstructure on X-Z plane. 
W. Song et al.

## Page 8

Additive Manufacturing 84 (2024) 104098
8
Liquation cracks were observed in alloys ZGH451 – 2 and ZGH451 – 3 
( Fig. 5 ), resulting from the remelting of low-melting-point phases within 
the solid part during the intrinsic heat treatment. These cracks typically 
occurred in areas of elemental segregation away from the melt pool, 
such as grain boundaries and the IR ( Figs. 5 (a) and 5 (d)), where has 
lower precipitation temperature. Moreover, the liquated regions 
exhibited a low-melting-point phase of the ( γ + γ ′ ) eutectic with fine 
spherical MC-type carbides ( Figs. 5 (b) and 5 (e)). Magnified SEM images 
obtained by electrolytic etching in the IR ( Fig. 5 (c)) and chemical 
etching on grain boundaries ( Fig. 5 (f)) revealed an alternating lamellar 
morphology of phases, further confirming the presence of the ( γ + γ ′ ) 
eutectic [57] . Localized liquification of these eutectics during the 
layer-wise deposition process led to the formation of a liquid film, which 
tore under tensile stress. By observing the morphology of cracks care -
fully, several connected shrinkage cavities (see the red square in Fig. 5 
(b) and (d)) larger than interdendritic solidification shrinkage cavities 
were examined. They were formed by the secondary solidification of a 
liquid film that remained intact under minor stress. In addition, the 
dissolution of MC-type carbides was observed on the grain boundary 
( Fig. 5 (f)), which is contributed to forming intergranular liquid film 
either [58,59] . Hence, liquation cracks were characterized by a smooth 
crack interface and larger shrinkage cavities induced by the solidifica -
tion of the residual remelted liquid film. These cracks typically 
measured tens of micrometers in length with width dimensions on the 
sub-micron scale. 
Solid-state cracks were exclusively observed in alloy ZGH451 – 3, 
showing distinct morphologies from the solidification and liquation 
cracks. This type of cracking typically occurred in solid parts near the 
bottom of the as-printed samples and was induced by stress concentra -
tion from solid-state phase transformations during prolonged inherent 
heat treatment, such as precipitation and growth of the γ ′ phase. 
Consequently, it is alternatively termed ductility dip cracking (DDC) 
[60] or strain-age cracking (SAC). The metallographic, SME, and BSE 
images ( Figs. 6 (a) – 6 (c)) depict cracking frequently occurring along the 
grain boundaries, often characterized by specific sharp kinks. Notably, 
the crack surface lacked dendrite arms and liquid films, presenting a 
neat and straight appearance. The locally enlarged image ( Fig. 6 (c)) 
obtained by BSE confirmed this structural characteristic, clearly delin -
eating the transition from solidification cracking (marked in red 
squares) to solid-state cracking (marked in yellow squares). A sharp kink 
(approximately 90
◦
) connected the two crack types, with solid-state 
cracks cutting through the DC and disappearance of dendrite arms. 
These cracks exceeded 1 mm in length, surpassing the depth of the melt 
pool (approximately 400 μ m), and penetrated multiple pools ( Fig. 6 (b)). 
4.3. Texture development 
Figs. 7 (a) – 7 (c) depict the formation of consecutive dendrites 
perpendicular to the fusion lines driven by epitaxial growth from the 
remelted previous layers. This inheritance of the as-fabricated micro -
structures established the approximate growth direction of the columnar 
grains, generating a strong texture. Results from EBSD scans (covering 
an area of 4 mm
2
) located in the middle of all three alloy bulks revealed 
inverse pole figure (IPF) maps of the X-Z plane ( Figs. 7 (d) – 7 (f)), 
showing a preferred orientation of {1 0 0} along the building direction. 
Coarse columnar grains were observed in alloys ZGH451 – 1 and 
ZGH451 – 2, while they were relatively smaller in ZGH451 – 3. The 
average grain sizes for each alloy were 237.5 μ m, 266.2 μ m, and 220.7 
μ m, considerably larger than those of selective laser melting samples 
[61,62] . Figs. 7 (g) – 7 (i) present pole figure maps of the three alloys, 
providing the texture strength for the three plane families {1 0 0}, {1 1 
0}, and {1 1 1} compared to the X-Z plane. Notably, the {1 0 0} texture 
component was the strongest, which is consistent with the IPF results. 
Figs. 7 (j) – 7 (l) displays the distribution of the GND density, whereas 
Figs. 7 (m) – 7 (o) presents histogram maps. Prominent GND accumulation 
was observed solely at the grain boundaries in all alloys, particularly at 
the high-angle grain boundaries (HAGB). A single modal distribution 
indicative of uniaxial deformation [63] was evident in the histogram 
maps, reflecting a similar GND density distribution across all grains. 
Statistical analysis revealed a small GND density value, lower than 
0.4 × 10
14 
m
-2
. This distribution pattern may be attributed to a low 
cooling rate (in comparison to selective laser melting (SLM)), flat molten 
pool, and preferential fiber texture formed by large grains. The low 
cooling rate limits the mechanical driving forces, whereas the flat 
molten pool alleviates residual stress. Additionally, large grains reduce 
the number of grain boundaries, thus minimizing the GND regions and 
facilitating significant thermal expansion along the [0 0 1]. Based on 
these EBSD results, all three alloys exhibited stable columnar grain 
structures with a [0 0 1] orientation and relatively low GND density, 
mitigating the influence of the DED process on subsequent experimental 
results. 
4.4. Evolution of phases during deposition 
Fig. 8 presents the heating and cooling curves of the three alloys 
obtained using DSC. These curves revealed distinct phase transition 
temperatures (listed in Table 4 ) during non-equilibrium solidification, 
confirming the phase constituents in the as-printed state. Notably, a 
significant change in heat flow occurred at the γ ′ dissolution temperature 
at the beginning of all curves. As the heating temperature increased, the 
solidus temperature ( T
S
) and liquidus temperature ( T
L
) emerged 
sequentially on the heating curves, as determined by extrapolation 
method [64,65] . Notably, the high Ta/Al ratio in ZGH451 – 1 enhanced 
both T
S 
and T
L
. Furthermore, the dissolution of carbide/boride at 1334 
◦
C and a clear eutectic reaction at 1276 
◦
C were observed only in the 
heating and cooling curves of alloy ZHG451 – 3, respectively, further 
confirming the absence of the ( γ + γ ′ ) eutectic phase in alloy ZGH451 – 1. 
During cooling, owing to nucleation undercooling, the γ ′ dissolution 
temperature and T
L 
in all the three alloys were lower than those during 
heating. 
4.5. Tensile behavior 
The mechanical properties of the three alloys were evaluated by 
Fig. 6. Solid-state crack observed in alloy ZGH451-3 (a-c) of as-built microstructure on X-Z plane. 
W. Song et al.

## Page 9

Additive Manufacturing 84 (2024) 104098
9
Fig. 7. SEM, EBSD-IPF (X-axis), pole figure maps and GND density of three alloys (as-built) on the X-Z plane. (a-c) shows the SEM images of columnar grains. (d-f) 
displays the IPF along building direction. (g-i) gives the bulk texture strength of {1 0 0}, {1 1 0} and {1 1 1} poles. (j-l) demonstrates the distribution of GND density 
in the bulk part of alloys and (m-o) are histograms exhibiting their concrete number values. 
W. Song et al.

## Page 10

Additive Manufacturing 84 (2024) 104098
10
tensile testing at room temperature, 760 
◦
C, and 1000 
◦
C in the as- 
fabricated state, as illustrated in Fig. 9 . The data included stress-strain 
curves, ultimate tensile strength, ductility, and area reduction. The 
tests were conducted within a limited heating and testing time of 30 s to 
preserve the initial structure post-AM process, akin to in situ measure -
ments. Alloy ZGH451 – 1 demonstrated excellent tensile strength and 
ductility across all temperatures, comparable to or surpassing many 
reported additive manufacturing superalloys [38,39,66 – 68] . Notably, at 
760 
◦
C, a temperature typically associated with a ductility dip in su -
peralloys, ZGH451 – 1 exhibited robust strength (ultimate tensile 
strength of 1160 MPa) and significant ductility ( > 40%). This observa -
tion could be attributed to the fact that the test temperature was slightly 
lower than the initial ductility dip temperature (~800 
◦
C). Furthermore, 
owing to the alloy ’ s low stacking fault energy, a novel deformation 
mechanism involving nanotwins may contribute to enhanced plasticity 
and strength. 
5. Discussions 
The proposed design method, which focused on a high Ta/Al ratio 
Fig. 8. The heating and cooling curves of three alloys measured from differential scanning calorimetry (DSC). Remarkable phase transition temperatures are labeled 
on each curve and specific values are shown in Table 4 . 
Table 4 
Phase transition temperatures of three alloys measured by DSC. 
Alloy Heating ( ◦ C) Cooling ( ◦ C) 
γ ′ T
S 
(Solidus) 
MC carbide T
L 
(Liquidus) γ ′ T
S 
(Solidus) 
MC carbide T
L 
(Liquidus) 
ZGH451 – 1 1197 1352 N/A 1396 1120 N/A N/A 1383 
ZGH451 – 2 1193 1343 N/A 1390 1151 N/A N/A 1380 
ZGH451 – 3 1200 1345 1334 1390 1163 N/A N/A 1380 
Fig. 9. The as-fabricated tensile properties of three alloys at room temperature and between 760 and 1000 º C. (a-c) shows the tensile curves after RT, 760 º C and 
1000 º C tests. (d-e) illustrates the comparison of ultimate tensile strength, ductility and reduction of area values of three alloys. 
W. Song et al.

## Page 11

Additive Manufacturing 84 (2024) 104098
11
and a dependence on the boundary composition, significantly influ -
enced the formability and mechanical properties through detailed 
studies of microstructures and defects. This demonstrates the strong 
correlation between the alloy chemistry, defect formation, and perfor -
mance. Notably, by collaboratively optimizing defect resistance factors 
alongside conventional alloy design theory, it is possible to find an 
approach that balances contradictions when designing new grades of 
AM-ed superalloys with a high γ ′ content. However, further discussion is 
required to thoroughly examine the rationality and internal mechanisms 
of this new approach. 
5.1. Capability to resist solidification cracking 
The suppression of solidification cracking in alloy ZGH451 is pri -
marily attributed to its narrow Scheil freezing range, as observed 
through microstructural analysis. However, the Scheil freezing range 
provides a broad overview of the solidification process, which lacks 
specificity in later stages when most solids are formed [69] . To address 
this limitation, the solidification cracking index (SCI) proposed by Kou 
[70] , which considers both solid formation (contributing to cracking) 
and liquid feeding (reducing cracking), was adopted to further elucidate 
the reduced susceptibility to cracking in advanced alloys designed using 
this new methodology. SCI
Kou 
primarily defines the ratio of the tem -
perature change to the change in the square root of the solid fraction, 
expressed as: 
SCI
Kou
=
⃒
⃒
⃒
⃒
⃒
dT
df
1 / 2
s
⃒
⃒
⃒
⃒
⃒
(1) 
where f
s 
is the mole fraction of solid, T is temperature. Based on Kou 
and Tang ’ s findings [38] , we proposed a likely solid fraction range of 0.8 
< f
s 
< 0.99, wherein significant differences in SCI
Kou 
values were 
observed across various alloys. Therefore, for our analysis of the 
cracking tendency in the three newly designed alloys, we focused on the 
expanded range of 0.5 < f
s 
< 1.0 in the final stage. Additionally, we 
compared two conventional alloys, IN718 (printable) and Ren ´e 108 
(cracked), with the recently reported crack-free superalloy for additive 
manufacturing, ABD-900AM. Furthermore, another 
composition-dependent solidification cracking criterion proposed by 
Clyne and Davies (SCI
CD
) [71] and the equilibrium freezing range were 
utilized for various alloys, allowing for a comprehensive analysis of the 
effect of solidification on cracking susceptibility. The SCI
CD 
approach 
represents the ratio of the time interval (0.9 ≤ f
s 
≤ 0.99) during which 
the alloy is prone to cracking to the time interval (0.4 ≤ f
s 
≤ 0.9) during 
which it can alleviate accumulated stress. When the cooling rate remains 
constant, this ratio is solely dependent on the temperature and can be 
simplified as: 
SCI
CD
=
T
f
s = 0 . 99
 T
f
s = 0 . 9
T
f
s = 0 . 9
 T
f
s = 0 . 4
(2) 
The accuracy of the SCI
CD 
method is compromised by its arbitrary 
time-range selection; however, it provides a useful supplementary 
Fig. 10. Results of solidification cracking susceptibility of various alloys based on the solidification cracking index of equilibrium freezing range, Clyne & Davies 
(SCI
CD
) and Kou (SCI
Kou
), calculated by Thermo-Calc with TCNI10 database. (a) shows the overview of SCI
Kou 
curves in the solid fraction of 0.5 – 1.0 and (b) is the 
magnified curves in the solid fraction of 0.8 – 1.0. (c) illustrates the SCI
Kou 
values at the last stage solidification with solid fraction of 0.8 – 0.996. (d) displays the 
distribution of SCI
CD 
and equilibrium freezing range values of various alloys. 
W. Song et al.

## Page 12

Additive Manufacturing 84 (2024) 104098
12
analysis. 
Figs. 10 (a) and 10 (b) display the SCI
Kou 
values within the ranges of 
0.5 < f
s 
< 1.0 and 0.8 < f
s 
< 1.0, respectively. It is evident that the 
cracking index increased significantly in the later stages of solidification 
as f
s 
approached 1. Examination of Fig. 10 (b) revealed a consistent trend 
in the SCI
Kou 
values across all alloys within the range of 0.8 – 0.9, yet 
significant fluctuations occurred between 0.9 and 1. The critical 
threshold is f
s 
= 0.9, as evidenced by substantial SCI
Kou 
variations 
observed for the printable alloy IN718 and ABD-900AM within the range 
0.9 < f
s 
< 1.0. Moreover, the nonprintable alloy Ren ´e108 consistently 
exhibited maximum SCI
Kou 
values beyond f
s 
> 0.9 across all alloys, 
further highlighting the critical influence of the solid fraction on the 
cracking behavior. 
The enlarged graph ( Fig. 10 (c)) provides a comparative analysis of 
the SCI
Kou 
variations, shedding light on the solidification cracking ten -
dencies of the newly designed alloys. Within the range of 0.9 < f
s 
< 0.98, 
the average SCI
Kou 
values for the alloys were consistent. However, 
beyond f
s 
> 0.98, ZGH451 – 3 demonstrated a rapid increase in SCI
Kou
, in 
contrast to the behavior of the other two alloys, aligning with their 
respective cracking susceptibilities. Specifically, ZGH451 – 3 ’ s higher 
volume fraction of the liquid phase in the final solidification stages 
elevated the risk of tearing. Conversely, the preferred alloy, ZGH451 – 1, 
maintained a consistently low SCI
Kou 
value throughout Scheil solidifi -
cation. Therefore, the SCI
Kou 
analysis of these alloys corroborates the 
experimental observations, indicating that alloys that surpass certain 
boundary compositions exhibit higher SCI
Kou 
values and are more prone 
to cracking. Additionally, Fig. 10 (d) presents the SCI
CD 
calculations and 
equilibrium freezing range for various reported alloys alongside our 
newly designed ones. Notably, alloys that were challenging to process 
occupied the upper right corner with elevated SCI
CD 
values and wider 
freezing ranges, whereas those suitable for AM occupied the lower left 
quadrant. Alloy ZGH451 – 1 closely aligned with printable alloys, such as 
IN718, IN625, and ABD-850AM, distinguishing itself from the other two 
designed alloys, which increasingly resembled alloys with high solidi -
fication cracking susceptibility, such as IN792 and IN738. 
Moreover, in addition to assessing each alloy ’ s cracking propensity 
through SCI values, which reflect solidification behavior, the influence 
of carbides was also considered. Given that the alloys were designed 
according to the same criteria, their elemental compositions remained 
consistent. Alloy ZGH451 – 1 was selected for carbide feature analysis. 
Fig. 11 illustrates the shape and composition of the carbides in 
ZGH451 – 1 under TEM. Clearly, the carbide (highlighted in yellow 
circles) was rich in Ti and C and was surrounded by Al/Ti-rich oxides 
(highlighted in red circles). Based on the carbide diffraction patterns, it 
was identified as MC type. The attached growth of two-phase structures 
increased the risk of cracking with increasing size [72] . Fig. 12 shows 
the carbide sizes across the three alloys, revealing them to be small and 
within the nanometer range. However, the average spacing of primary 
dendrites in the newly designed alloys was 26.8 μ m, 30.5 μ m, and 36.1 
μ m, approximately one order of magnitude larger than carbides. Thus, 
the obstructive effect of carbides on liquid feeding during dendrite 
growth is less efficient; hence, they are not the primary factor contrib -
uting to solidification cracking. 
In summary, the SCI analysis and carbide distribution further vali -
dated the rationale behind the proposed newly designed approach. This 
approach ensures a high volume fraction of the γ ′ phase, while identi -
fying alloys with low cracking tendencies. However, this verification is 
not exhaustive. For instance, the microstructure significantly influenced 
cracking indices. Larger grain sizes and strong textures reduced weak -
ened areas, such as grain boundaries (GB
S
), yet they also induced sharp 
stress concentrations on the remaining GBs, promoting crack formation 
[73,74] . Nonetheless, alloy ZGH451 – 1 exhibited low crack susceptibil -
ity, confirming the efficacy of the newly designed approach in the 
development of advanced alloys. Further investigation is warranted to 
explore the potential effects and enhance the methodology. 
5.2. Influence of γ ’ -forming elements on liquation cracks 
Liquation cracks arise from the interplay between pre-existing liquid 
films and thermal stress, commonly observed in the heat-affected zone 
(HAZ), where repeated heating between layers remelts local phases, 
inducing shrinkage strain. Hence, reducing elemental segregation, 
particularly of the γ’ -forming elements in IR, is imperative for the 
elimination of liquation cracking. These elements expedite the forma -
tion of low-melting-point MC-type carbides [42] , Laves phases [57] , and 
( γ + γ’ ) eutectics [59] , which have a considerable potential for 
liquefaction. 
The DSC curves accurately measure the phase transition tempera -
tures, enabling the distinction of solid-solid phase transitions that 
elevate liquation susceptibility. Prior to the melting onset, the 
ZGH451 – 2 and ZGH451 – 3 curves progressively flattened, indicating 
enhanced element diffusion favoring noticeable segregation in the final 
stages of solidification [75] , consistent with their developed dendritic 
structure. Moreover, the ZGH451 – 3 curve depicted the phase transitions 
Fig. 11. Morphology, diffraction pattern and distribution of elements obtained by TEM of carbides in alloy ZGH451-1. (a) shows the morphology of carbides and 
oxides. (b-l) exhibits the distribution of all elements. 
W. Song et al.

## Page 13

Additive Manufacturing 84 (2024) 104098
13
of carbide and ( γ + γ’ ) eutectic, both of which are potential liquation 
sources. Conversely, ZGH451 – 1 exhibited a steep curve at a melting 
onset of 1352 
◦
C, suggesting rapid freezing with minimal segregation. 
Notably, no significant low-melting phase transition corresponded to the 
microstructure observations, implying effective resistance to liquation 
cracking during reheating. This suggests that the proposed high Ta/Al 
ratio may influence micro-segregation and mitigate liquation crack 
formation. 
The decrease in liquation susceptibility is primarily attributed to 
process features and the segregation behavior of elements. (i) The rapid 
cooling rate of DED, approximately 10
3
– 10
5 
K/s [76] , limits element 
diffusion due to insufficient time and driving force. Although subsequent 
heat treatment may partially mitigate this, the PDAS ( Table 3 ) was 
considerably smaller than that in the as-cast state [77] . (ii) The presence 
of the ( γ + γ’ ) eutectic in the columnar grain boundaries and interden -
dritic regions in the as-built microstructures, with cracks predominantly 
occurring in the former, is noteworthy. This is attributed to the high 
coherency of dendrites within the grains, allowing for thermal stress 
co-allocation in a specific direction, unlike grain boundaries that lack 
coherency. Grain misorientations exacerbate element enrichment, 
Fig. 12. Size and area percentage (equivalent to volume fraction) of carbides in three alloys. 
Fig. 13. Segregation behavior of each alloying element reflected via partitioning ratio, namely K ′ and K. 
W. Song et al.

## Page 14

Additive Manufacturing 84 (2024) 104098
14
thereby increasing the likelihood of eutectic pool formation. Addition -
ally, the grain boundary contraction provides a driving force for eutectic 
film tearing. However, the DED process yields coarse columnar grains 
with fewer boundaries, mitigating these detrimental factors and 
reducing the likelihood of liquation cracking. (iii) Fig. 13 illustrates the 
distribution coefficient of major elements obtained by EPMA, where K
i 
represents the ratio of dendrite core concentration to interdendritic re -
gion concentration for the i th element, with the opposite applying to K
′
i
: 
K
i
= K
i
C
i
CD
C
i
IR
(3) 
K
’
i
C
i
IR
C
i
CD
(4) 
it is notable that K
i 
approaches 1, indicating a uniform distribution of 
W, Co, Cr, Mo, and Ni. Conversely, K
′
i 
increased with decreasing Ta/Al 
ratio, signifying increased segregation of Al, Ti, and Ta, which promoted 
crack formation. Therefore, substituting Al and Ti with a higher Ta 
content to form the γ’ phase reduced the content of strongly segregated 
elements. Moreover, the low diffusion coefficient and high melting point 
of Ta [41] alleviated segregation and suppressed the formation of 
low-melting phases. The influence of Ta on segregation can be assessed 
through its impact on effective diffusivity ( D
eff
) proposed by Reed [78] , 
which estimates the diffusion capacity of elements within an alloy: 
D
eff
= D
eff
0
exp
(
 
Q
eff
RT
)
(5) 
where D
eff
0
and Q
eff 
are the pre-exponential coefficient and activation 
energy respectively, T is the temperature of measurement, R represents 
the ideal gas constant. The pre-exponential coefficient of alloys in -
fluences by each content of elements, which is defined as: 
D
eff
0
=
∑
m
x
m
D
m , Ni
0
(6) 
where x
m 
is the atomic concentration of element m in γ matrix, D
m , Ni
0
is 
the pre-exponential factor of solute m in nickel (listed in Table 6 ). The 
effective activation energy is defined as the sum of Q
eff 
of pure nickel and 
the weighted average of contributions from the different solutes: 
Q
eff
= Q
Ni
+
∑
m
x
m
Q
m , Ni
(7) 
where Q
Ni 
is activation energy for self-diffusion of nickel, Q
m , Ni
is the 
activation energy for interdiffusion of solute m in nickel. To quantify the 
value of D
eff
, pseudo-binary phase diagrams ( Fig. 14 ) were constructed, 
varying the content of Al and Ta to ascertain the experimental temper -
ature. Based on these diagrams, a temperature of 1060 
◦
C was selected 
within the solid zone containing γ and γ’ phases. The atomic concen -
tration of each element in the γ phase was calculated using Thermal-Calc 
(with the TCNI10 database) at a specified temperature (listed in 
Table 5 ). Therefore, the values of D
eff
0
, Q
eff
, and D
eff 
for the three alloys 
were determined and are listed in Table 6 . It is evident that a high Ta/Al 
ratio not only introduced a low diffusion coefficient element (Ta) but 
also reduced the effective diffusivity, thereby weakening the diffusion 
ability of elements and suppressing segregation, thereby reducing the 
occurrence of liquation cracks. (iiii) Moreover, the low levels of C and B 
(approximately 0.01 wt%) resulted in the formation of few, small-sized 
carbides (100 – 150 nm) that were uniformly distributed. According to 
Dye ’ s research [59] , carbides of larger size (~2 μ m) exhibit an increased 
liquation propensity. Hence, both in terms of content and size, liquation 
cracking associated with carbides is mitigated, suggesting that carbides 
might not be the primary source of liquation, and the ( γ + γ’ ) eutectic 
could be more detrimental. 
Overall, the proposed high Ta/Al ratio effectively addressed printing 
challenges arising from the segregation of γ’ forming elements (Al and 
Ti) based on welding experience, reducing the crack sensitivity. Addi -
tionally, it ensured a higher volume fraction of γ’ precipitates, the 
impact of which on performance was extensively discussed in Section 
5.3 . 
5.3. Prevention of solid-state cracks 
Solid-state cracking is closely linked to phase precipitation, which 
induces stress in surrounding areas. This phenomenon primarily stems 
from the abundant precipitation of the γ’ phases in advanced superal -
loys, as they are the primary strengthening phases for high-performance 
superalloys at elevated temperatures. The relatively low cooling rate of 
DED and repeated thermal cycles further enhance the propensity for 
strain aging [79] . Hence, there is a contradiction between the need for 
the γ’ phase in printability and performance. This study addressed this 
contradiction by proposing an effective approach based on a high Ta/Al 
ratio and a significant dependence on boundary composition. The 
coordinating mechanism of this approach was discussed in terms of its 
influence on the precipitation behavior of γ’ phase and the deformation 
resistance of alloys. 
When the intrinsic heat treatment temperature is below the γ’ solvus, 
Fig. 14. Establishment of the pseudo-binary phase diagrams with the variable of Al (a) and Ta (b). 
W. Song et al.

## Page 15

Additive Manufacturing 84 (2024) 104098
15
the precipitation of the γ ′ phase results in varying degrees of phase 
transition stress, enhancing the propensity for cracking. The stress level 
can be qualitatively estimated by the cooling rate C
γ ′ 
at the γ ′ solvus, 
which is closely related to the size of γ ′ as follows [80] : 
d
0
= qC
 p
γ’
(8) 
where d
0 
is the initial γ ′ diameter (nm) precipitating just below the γ ′ 
solvus, q and p is the constant values determined from the reported 
U720LI superalloys as 442.5 and 0.4605, respectively [81] . Because of 
the lack of preheating and short duration of the DED process, it is 
assumed that the size of γ ′ (located at DC and IR) after printing remains 
identical to the initial precipitation size. By applying the γ ′ values listed 
in Eq. 3 to Eq . [8] , the C
γ ′ 
values for the three alloys in DC/IR were 
calculated as 149.2/110.1 K ⋅ s
 1
, 106.9/77.8 K ⋅ s
 1
, and 178.9/121.4 
K ⋅ s
 1
, respectively. It is evident that a high Ta/Al ratio can reduce the 
cooling rate, indicating lower phase-transition stresses induced by γ’ 
precipitation and fewer cracks. Furthermore, the high Ta/Al ratio can 
decrease the segregation of γ ′ forming elements ( Fig. 13 ) and improve 
the chemical driving force for γ ′ precipitation (as predicted by 
Thermo-Calc, detailed in the Appendix), thereby creating conditions 
lacking composition and energy for phase transition. 
In addition to the precipitation behavior, the deformation resistance, 
influenced by compositional changes and the volume fraction of γ’ 
precipitates, is crucial in assessing the cracking tendency. The inter -
dendritic region (IR) is particularly prone to γ ′ precipitation, leading to 
heightened stress concentration. Therefore, quantitatively analyzing the 
deformation resistance between dendrites can effectively gauge the 
ability of an alloy to resist solid-state cracking. In this context, the re -
sidual thermal stress levels of the three alloys were considered to be 
approximately similar and thus neglected, given their similar process 
characteristics. Utilizing the additive law in γ ′ -strengthened nickel-based 
superalloys [82] , the IR strength can be defined as follows: 
σ
S
= σ
SS . IR
+ σ
γ’ . IR
+ σ
GB
+ σ
Dis . IR
+ σ
p
(9) 
where σ
SS . IR 
is the solid solution strengthening in IR, σ
γ ′ . IR
is the γ ′ 
precipitation strengthening. σ
GB 
is grain boundary strengthening, which 
is inversely proportional to the square root of grain size [83] . In the 
as-DED-processed microstructure of the aforementioned three alloys, 
they all exhibited large grain sizes and fewer grain boundaries, 
rendering σ
GB 
insignificantly contributing to strength. σ
Dis . IR 
represents 
dislocation strengthening, proportionate to the square root of disloca -
tion density according to Taylor ’ s dislocation strengthening equation 
[84,85] . However, the dislocation density remained nearly constant 
after an identical printing procedure, as reported in extensive previous 
studies [86,87] . σ
p 
denotes the Peierls stress induced by the pure nickel 
lattice resistance, remaining constant. Hence, after modifying the con -
stant term, Eq. (9) could be rewritten as: 
σ
S
= σ
SS . IR
+ σ
γ’ . IR
+ Constant (10) 
Then, the IR strength is primarily influenced by precipitation and 
solution strengthening. The impact of the γ ′ morphologies on precipi -
tation strengthening is assumed to be minimal given their subtle dif -
ferences in shape and size ( Fig. 3 ). For a single γ or γ ′ phase solid 
solution, strength is heavily dependent on chemical composition, 
meaning that σ
SS . IR 
and σ
γ ′ . IR 
is determined by the alloying elements. The 
contributions to strengthening from each element i can be summed using 
a simple chemical composition-based formula, which is consistent with 
the reference: 
σ
S
=
∑
n
i = 1
̅̅̅̅̅ ̅
x
i
IR
√
× k
i
+
∑
n
i = 1
̅̅̅̅̅̅ ̅
x
i
γ’
√
× k
i
+ Constant (11) 
where x
i
IR 
and x
i
γ ′
are the atomic fraction of the i th alloying 
element of the IR and γ ′ phase, respectively. k
i 
represents the respective 
solid-solution strengthening coefficient of each element, with values 
derived from Roth et al. [88] for dilute alloys and multi-regression 
fitting results from Joseph et al. [67] for AM superalloys at 800 
◦
C 
(both listed in Table 7 ). Notably, σ
S 
increased with a higher Ta/Al ratio, 
as the strengthening coefficient of Ta surpassed that of other elements. 
This underscores the efficacy of the proposed high Ta/Al ratio in 
enhancing the crack resistance. Moreover, significant dependence on 
boundary composition rigorously regulates the γ ′ content, resulting in a 
comparatively high volume fraction of the γ ′ phase in alloy ZGH451 – 1 
(approximately 48%), which is lower than that of the other two alloys. 
This design approach reduces stress levels, diminishes cracking risks, 
and ensures high-temperature performance. The tensile curves in Fig. 9 
demonstrate the superior performance of ZGH451 – 1 at 1000 
◦
C. Addi -
tionally, cracking alloys with high volume fractions of the γ’ phase 
demonstrate respectable properties at high temperatures (~1000 
◦
C) 
( Fig. 9 (c)), implying uneven crack distribution in low-crack-content al -
loys, potentially lacking apparent cracks in the mechanical property test 
samples. Furthermore, the sufficiency of time and energy (e.g., tem -
perature dependence) for crack initiation and propagation significantly 
determines their harmful effects as precipitation strengthening remains 
dominant. 
In summary, alloy ZGH451 – 1 consistently exhibited the lowest 
cooling rate of the γ ′ phase and the highest deformation resistance, 
coupled with excellent tensile strength and ductility across a range of 
temperatures. These experimental findings conclusively demonstrate 
that the proposed approach can effectively design a new grade of crack- 
free superalloy with a high volume fraction of the γ ′ phase and excep -
tional high-temperature performance, thereby achieving collaborative 
optimization of properties and formability. 
6. Further insights into alloy composition design 
To comprehensively demonstrate the effectiveness of the new design 
method in improving the alloy performance, the microstructure and 
Table 5 
The atomic concentration of each element in γ phase calculated by Thermal-Calc (with TCNI10 database) of three alloys at 1060 º C. 
Alloy Co Cr W Mo Al Ti Ta Ni 
ZGH451 – 1 0.09 0.11 0.03 0.017 0.07 0.009 0.007 0.63 
ZGH451 – 2 0.10 0.13 0.03 0.017 0.07 0.01 0.006 0.62 
ZGH451 – 3 0.1 0.12 0.03 0.015 0.08 0.007 0.005 0.618 
Table 6 
Pre-exponential factors and activation energies for solutal diffusion in pure 
nickel and calculated effective pre-exponential factors, effective activation en -
ergies and effective diffusivity for three new designed alloys. 
Element D
0
[ m
2
s
 1
] Q
m , Ni
[ kJ mol
 1
]
Ni 1.9 × 10
 4 
284 
Cr 3 × 10
 6 
170.7 
Co 7.5 × 10
 5 
285.1 
W 8.0 × 10
 6 
264 
Al 7.52 × 10
 4 
284 
Ta 2.19 × 10
 5 
251 
Mo 1.15 × 10
 4 
281.3 
Ti 8.6 × 10
 5 
257 
Alloy 
D
eff
0
[ m
2
s
 1
] Q
eff
[ kJ mol
 1
] D
eff
[ m
2
s
 1
]
ZGH451 – 1 1.83 × 10
 4 
380.9 2.11 × 10
 19 
ZGH451 – 2 1.83 × 10
 4 
371.3 5.18 × 10
 19 
ZGH451 – 3 1.89 × 10
 4 
370.9 5.60 × 10
 19 
W. Song et al.

## Page 16

Additive Manufacturing 84 (2024) 104098
16
tensile properties of ZGH451 – 1 produced by SLM are examined in 
Fig. 15 . The fabrication utilized a GE Concept Laser M2 machine 
equipped with a modulated 370 W ytterbium fiber laser for processing 
the powder feedstock. The modulated laser conducted point-to-point 
scans using the following process parameters: laser power of 240 W, 
layer thickness of 50 μ m, hatch spacing of 100 μ m, scanning speed of 
700 mm/s, and an exposure time of 50 μ s at each point. A meander scan 
strategy involving a raster scan with 67
◦
rotation for each layer was 
employed. Cubes measuring 20 × 20 × 60 mm
3 
were manufactured for 
each alloy during processing trials. The heat treatment (HT) strategy 
comprised the following steps: 650 
◦
C/4 h, AC (stress relief annealing) +
1200 
◦
C/180 MPa/2 h, AC (hot isostatic pressing-HIP) + 1240 
◦
C/3 h, 
AC (solution) + 1120 
◦
C/4 h, AC; 870 
◦
C/24 h, AC (aging). The load 
direction was aligned along the building direction, specifically along the 
Z-axis. 
The OM ( Figs. 15 (a) – 15 (c)) and SEM ( Fig. 15 (d)) images of the as- 
built SLM ZGH451 – 1 clearly demonstrated its remarkable crack resis -
tance and wide process window (ranging from VED = 62.86 J/cm
3 
to 
137.51 J/cm
3
). Following heat treatment (HT), the volume fraction of 
the γ ′ phase can reach 63% ( Fig. 15 (e)), which is closely aligned with 
most 1 – 3th-generation cast superalloys, including single-crystal alloys 
(e.g., CMSX-2 ~60%, CMSX-4 ~65%, TMS-75 ~60%, and CM247LC 
~65%). Moreover, the tensile properties from room temperature to 
1100 
◦
C for both as-built and heat-treated SLM ZGH451 – 1 are depicted 
in Figs. 15 (f) and 15 (g), consistently demonstrating high UTS and 
ductility, which are close to or surpass those of DED ZGH451 – 1 ( Fig. 9 ) 
and maintain exceptional high-temperature performance. Notably, the 
ductility exceeded 10% throughout, even after the heat treatment. 
Finally, a commercial turbine blade ( Fig. 15 (h)), approximately 15 cm 
long and 4 cm wide, is perfectly printed by SLM without cracks. Above 
better process suitability, fully crack-resistance, adequate γ ′ content and 
excellent performance further demonstrate the applicability of the new 
design approach. 
Fig. 16 presents the tensile properties (ultimate tensile strength 
(UTS) and ductility) of the as-built ZGH451 – 1 (fabricated by DED and 
SLM) in comparison to other reported superalloys in various states. 
Table 7 
Solid solution strengthening coefficient of alloying elements in Nickel fabricated by casting [88] and AM [67] used in this study. 
Solid solution strengthening coefficients (MPa at. Fraction
1/2
) C B Co Cr W Al Mo Ta Ti 
k
i 
[88] 1061 N/A 39 337 977 225 1015 1191 775 
k
AM
i
[67] 
5355 N/A 43 285 1813 1787 795 3736 1438 
Fig. 15. Overall inspection and analysis of as-built and heat-treated microstructures of alloy ZGH451-1 fabricated by SLM, structures observed perpendicular to 
building direction (X-Y plane). (a-c) displays the OM images of crack-free structures of the X-Y plane under various volume energy density (VED) and (d, e) are the 
SEM images of as-built and heat-treated microstructures, respectively. (f) shows tensile curves for as-built and heat-treated SLM ZGH451-1 from RT to 1100 º C and (g) 
is the corresponding ultimate tensile strength and ductility values. (h) Crack-free turbine blade with complex structure fabricated by SLM, using alloy ZGH451-1. 
W. Song et al.

## Page 17

Additive Manufacturing 84 (2024) 104098
17
Through further optimization of the laser process parameters, alloy 
ZGH451 – 1 not only achieved crack-free microstructures but also 
demonstrated superior tensile properties across different temperatures. 
Notably, ZGH451 – 1 exhibited higher UTS and ductility compared to 
most AM-ed superalloys and partially outperformed directionally so -
lidified (DZ) and single-crystal (SX) alloys up to medium temperatures. 
Specifically, at 800 
◦
C, ZGH451 – 1 showed a UTS of 1080 MPa and 
ductility of 11%, indicating a strong performance despite a slight 
decrease in ductility. Furthermore, at high temperatures, ZGH451 – 1 
demonstrated favorable tensile properties, comparable to those of alloys 
with a high volume fraction of the γ ′ phase ( > 60%), including AM-ed 
and SX superalloys. 
Additionally, the creep performance of ZGH451 – 1 (fabricated by 
DED) in both the as-built and heat-treated (650 
◦
C/4 h, AC (stress-relief 
annealing) + 1200 
◦
C/180 MPa/2 h, AC (HIP)) states was evaluated. 
Creep tests were conducted at temperatures of 760 
◦
C and 980 
◦
C with 
applied stresses of 780 MPa and 260 MPa, respectively. The corre -
sponding creep times were 92 h/27 h for the as-built state and 65 h/ 
15 h for the heat-treated state. To illustrate the exceptional creep 
resistance of ZGH451 – 1, a Larson-Miller parameter (LMP) plot ( Fig. 17 ) 
was generated to compare its overall creep resistance with those of al -
loys IN718, ABD-900AM, and CM247LC under various conditions, 
defined as: 
LMP = T × (20 + log 
10 
(t 
r
) / 1000) (12) 
where T is absolute temperature in Kelvin and t
r 
is time to rupture in 
hours. ZGH451 – 1 demonstrated superior resistance to creep compared 
to the other three alloys, particularly under conditions of intermediate 
temperature/high stress or high temperature/low stress, despite the 
reasonable heat treatment and stable microstructure of the latter alloys. 
Notably, the highly processable alloy IN718 exhibited the poorest creep 
performance, particularly at high temperatures, which is attributed to 
Fig. 16. Comparison of tensile properties after RT (a), 760 º C (b) and 1000 º C (c) tests of reported directionally solidified (DZ, heat-treated) [89 – 91] , single crystal 
(SX, heat-treated) [92 – 98] and additive manufacturing superalloys [27 – 29,38,39,52,99,100] with as-built state alloy ZGH451-1. 
Fig. 17. Comparison of creep properties based upon Larson-Miller parameter of 
reported heat-treated alloy IN718, ABD-900AM, CM247LC [38,39,52] and 
as-built state alloy ZGH451-1. 
W. Song et al.

## Page 18

Additive Manufacturing 84 (2024) 104098
18
the instability of its γ ′ ′ intermetallic phase and lower oxidation resis -
tance. The substantial difference in the γ ′ content between the newly 
designed processable ABD-900AM (~30%) and ZGH451 – 1 (~48%) 
contributed to the latter ’ s superior properties. Although the heritage 
alloy CM247LC benefited from its high γ ′ content (~65%) for enhanced 
creep resistance, the presence of numerous cracks compromised the 
structural integrity, resulting in lower creep times compared to the 
crack-free alloy ZGH451 – 1 with a relatively high γ ′ content, particularly 
under high-temperature and low-stress conditions. 
To sum up, the new design method presented here indeed controls 
cracks, preserves a high-volume fraction of γ ′ phase, and avoids the 
decrease in high-temperature performance, proving its rationality and 
feasibility and opening an avenue for designing new high-performance 
superalloys suitable for additive manufacturing. It is also worth noting 
that the design concept of a high Ta/Al ratio has a significant effect and 
certain universality in regulating the content of strengthening phases 
and suppressing crack formation. Additionally, a part of the design 
methods for conventional superalloys, such as the control of the TCP 
phase is well-matched to the new AM process, this finding is worthy of 
further investigation. 
7. Summary and conclusions 
The following conclusions can be acquired from this work: 
1. A new design approach for additively manufactured Ni-based 
superalloys based on a high Ta/Al ratio and strong boundary 
composition-dependent, considering the alloy composition, defect con -
trol, and mechanical behavior, is proposed to overcome the difficulties 
between manufacturability and materials performance. A newly- 
designed crack-free superalloy with a high-volume fraction of γ ′ phase 
named as ZGH451 – 1 was successfully isolated from alloy design space 
using computationally-intensive thermodynamic modeling, which ex -
hibits outstanding mechanical properties at various conditions. 
2. In the two alloys, ZGH451 – 2 and ZGH451 – 3 design deviated from 
the new way, decreasing the Ta/Al ratio. Various types of cracks have 
emerged, including solidification, liquidation, and solid-state cracking, 
while some differences exist in crack distribution for each alloy. Both 
alloys have obvious solidification cracking and low numbers of liquation 
cracks, yet the solid-state cracking is observed only in ZGH451 – 3 with 
the lowest Ta/Al ratio. For the preferred alloy, no cracks of any form 
were observed in all positions of the sample. 
3. Multiple favorable factors for regulating cracks of newly-designed 
alloy have been fully validated. To begin with, a narrower Scheil 
freezing range and lower SCI value induced by composition design 
effectively optimize solidification behavior, decreasing the susceptibil -
ity to solidification cracking. Next, the high Ta/Al ratio lowers the 
effective diffusivity of the alloy and suppresses the segregation in IR, 
resulting in the absence of low melting point ( γ + γ ′ ) eutectic pools, which 
eliminates the liquation cracks. Finally, the lowest cooling rate of γ ′ 
phase and sufficient deformation resistance caused by a high Ta/Al ratio 
improves the capability of resistance to solid-state cracking. At the same 
time, the strong boundary composition-dependent maximizes the above 
effects and strictly limits the γ ′ content, ensuring lower crack 
susceptibility. 
4. Extensive performance (including tensile and creep tests) com -
parisons have shown that the newly-designed alloy has excellent prop -
erties and higher workability. The more pronounced inherent heat 
treatment of DED allows the as-built structure to be in an under-heat- 
treated state with a certain volume fraction of γ ′ phases, resulting in 
the alloy ZGH451 – 1 showing better mechanical properties than most of 
the reported AM-ed superalloys and partially heat-treated first/second- 
generation Ni-based single-crystal superalloys. 
5. The present new alloy design method can indeed develop new 
grades of superalloys with high volume fraction of γ ′ phases and few 
cracks, which can make up for the lack of high-temperature performance 
of alloys for additive manufacturing or solve the problem of their poor 
printability at present, achieving synergistic optimization of both. In 
addition, the excellent microstructure stability of ZGH451 – 1 indicates 
that the conventional alloy design method can be partially applied to 
design AM-ed alloys, such as the d-electrons alloy theory. 
CRediT authorship contribution statement 
Junying Yang: Supervision, Formal analysis, Data curation. Wei 
Song: Writing – review & editing, Writing – original draft, Validation, 
Methodology, Investigation, Formal analysis, Data curation. Jinguo Li: 
Supervision, Resources, Project administration. Xiaofeng Sun: Super -
vision, Project administration. Yizhou Zhou: Supervision, Resources, 
Project administration. Nannan Lu: Supervision, Project administra -
tion, Funding acquisition. Jingjing Liang: Supervision, Project admin -
istration, Funding acquisition. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Data availability 
The data that has been used is confidential. 
Acknowledgements 
The financial support provided by Defense Industrial Technology 
Development Program (No. JCKY2020130C024), National Key R & D 
Program of China (Grant No. 2021YFB3702503), Science Center for Gas 
Turbine Project (Project No. P2022-C-IV-002-001), National Science and 
Technology Major Project (Y2019-VII-0011-0151). The authors are 
grateful for those supports. 
References 
[1] A. Epishin, T. Link, Mechanisms of high-temperature creep of nickel-based 
superalloys under low applied stresses, Philos. Mag. 84 (19) (2004) 1979 – 2000 . 
[2] A.C. Yeh, A. Sato, T. Kobayashi, H. Harada, On the creep and phase stability of 
advanced Ni-base single crystal superalloys, Mater. Sci. Eng. A. 490 (1) (2008) 
445 – 451 . 
[3] T.M. Pollock, Alloy design for aircraft engines, Nat. Mater. 15 (8) (2016) 
809 – 815 . 
[4] D.D. Gu, W. Meiners, K. Wissenbach, R. Poprawe, Laser additive manufacturing 
of metallic components: materials, processes and mechanisms, Int. Mater. Rev. 57 
(3) (2012) 133 – 164 . 
[5] B.B. Milner, P. Gradl, G. Snedden, M. Brooks, J. Pitot, E. Lopez, M. Leary, F. Berto, 
A. Plessis, Metal additive manufacturing in aerospace: a review, Mater. Des. 
(2021) 110008 . 
[6] C. Panwisawas, Y.T. Tang, R.C. Reed, Metal 3D printing as a disruptive 
technology for superalloys, Nat. Commun. 11 (1) (2020) 1 – 4 . 
[7] C. K ¨orner, Additive manufacturing of metallic components by selective electron 
beam melting-a review, Int. Mater. Rev. 61 (5) (2016) 361 – 377 . 
[8] T. DebRoy, T. Mukherjee, J.O. Milewski, J.W. Elmer, B. Ribic, J.J. Blecher, 
W. Zhang, Scientific, technological and economic issues in metal printing and 
their solutions, Nat. Mater. 18 (2019) 1026 – 1032 . 
[9] E. Chauvet, P. Kontis, E.A. J ¨agle, B. Gault, D. Raabe, C. Tassin, J.J. Blandin, 
R. Dendievel, B. Vayre, S. Abed, Hot cracking mechanism affecting a nonweldable 
Ni-based superalloy produced by selective electron Beam Melting, Acta Mater. 
142 (2018) 82 – 94 . 
[10] B. Wahlmann, M. Markl, C. K ¨orner, A thermo-mechanical model for hot cracking 
susceptibility in electron beam powder bed fusion of Ni-base superalloys, Mater. 
Des. 237 (2024) 112528 . 
[11] Y. Wang, W. Guo, H. Zheng, Y.K. Xie, X.F. Zhang, H.X. Li, M. Xu, H.Q. Zhang, 
Microstructure, crack formation and improvement on nickel-based superalloy 
fabricated by powder bed fusion, J. Alloy. Comp. 962 (2023) 171151 . 
[12] N.N. Lu, Z.L. Lei, K. Hu, X.F. Yu, P. Li, J. Bi, S.B. Wu, Y.B. Chen, Hot cracking 
behavior and mechanism of a third-generation Ni-based single-crystal superalloy 
during directed energy deposition, Addit. Manuf. 34 (2020) 101228 . 
[13] E. Chauvet, P. Kontis, E.A. J ¨agle, B. Gault, D. Raabe, C. Tassin, J.J. Blandin, 
R. Dendievel, B.J. Vayre, S. Abed, G. Martin, Hot cracking mechanism affecting a 
non-weldable Ni-based superalloy produced by selective electron Beam Melting, 
Acta Mater. 142 (2018) 82 – 94 . 
W. Song et al.

## Page 19

Additive Manufacturing 84 (2024) 104098
19
[14] C. Guo, G. Li, S. Li, X.G. Hu, H.X. Lu, X.G. Li, Z. Xu, Y.H. Chen, Q.Q. Li, J. Lu, 
Q. Zhu, Additive manufacturing of Ni-based superalloys: residual stress, 
mechanisms of crack formation and strategies for crack inhibition, Nano Mater. 
Sci. 5 (2023) 53 – 77 . 
[15] K.H. Ryou, H.J. Im, J.W. Park, P.P. Choi, Microstructural evolution and hot 
cracking prevention in direct-laser-deposited Ni-based superalloy through Hf 
addition, Mater. Des. 234 (2023) 112298 . 
[16] K. Lindgren, F. Schulz, H. Gruber, A. Markstr ¨om, E. Hryha, On the role of Zr and B 
addition on solidification cracking of IN738LC produced by laser powder bed 
fusion, Mater 26 (2022) 101609 . 
[17] N. Wang, S. Mokadem, M. Rappaz, W. Kurz, Solidification cracking of superalloy 
single- and bi-crystals, Acta Mater. 52 (11) (2004) 3173 – 3182 . 
[18] J. Liu, S. Kou, Susceptibility of ternary aluminum alloys to cracking during 
solidification, Acta Mater. 125 (2017) 513 – 523 . 
[19] A. Mostafaei, R. Ghiaasiaan, T. Ho, S. Strayer, K.C. Chang, N. Shamsaei, S. Shao, 
S. Paul d, A.C. Yeh, S. Tin, A.C. To, Additive manufacturing of nickel-based 
superalloys: a state-of-the-art review on process-structure-defect-property 
relationship, Prog. Mater. Sci. 236 (2023) 101108 . 
[20] O.A. Ojo, M.C. Chaturvedi, Liquation microfissuring in the weld heat-affected 
zone of an overaged precipitation-hardened nickel-base superalloy, Metall. Mater. 
Trans. A 38 (2007) 356 – 369 . 
[21] M. Montazeri, F.M. Ghaini, The liquation cracking behavior of IN738LC 
superalloy during low power Nd:YAG pulsed laser welding, Mater. Charact. 67 
(2012) 65 – 73 . 
[22] S.G. Jeong, S.Y. Ahn, E.S. Kim, S.H. Kang, S.H. Yoo, J.Y. Ryu, J.H. Chun, G. 
M. Karthik, H.S. Kim, Liquation cracking in laser powder bed fusion-fabricated 
Inconel718 of as-built, stress-relieved, and hot isostatic pressed conditions, Mater. 
Sci. Eng. A. 888 (2023) 145797 . 
[23] W.Z. Zhou, Y.S. Tian, Q.B. Tan, S. Qiao, H. Luo, G.L. Zhu, D. Shu, B.D. Sun, Effect 
of carbon content on the microstructure, tensile properties and cracking 
susceptibility of IN738 superalloy processed by laser powder bed fusion, Addit. 
Manuf. 58 (2022) 103016 . 
[24] S. Park, Y. Tanaka, S. Okazaki, Y. Funakoshi, H. Kawashima, H. Matsunaga, Role 
of grain boundaries and precipitates in small, fatigue crack-growth resistance of 
additively-manufactured, Ni-based superalloy 718 under torsional cyclic loading, 
Mater. Lett. 350 (2023) 134844 . 
[25] I. Todd, No more tears for metal 3D printing, Nat 549 (7672) (2017) 342 – 343 . 
[26] B. Liu, Y.T. Ding, J.Y. Xu, X.M. Wang, Y.B. Gao, Y. Hu, D.L. Chen, Achievement of 
grain boundary engineering by transforming residual stress in selective laser- 
melted Inconel 718 superalloy, Mater. Sci. Eng. A. 866 (2023) 144683 . 
[27] K. Moussaoui, W. Rubio, M. Mousseigne, T. Sultan, F. Rezai, Effects of selective 
laser melting additive manufacturing parameters of Inconel 718 on porosity, 
microstructure and mechanical properties, Mater. Sci. Eng. A. 735 (2018) 
182 – 190 . 
[28] K.S. Kim, T.H. Kang, M.E. Kassner, K.T. Son, K.A. Lee, High-temperature tensile 
and high cycle fatigue properties of Inconel 625 alloy manufactured by laser 
powder bed fusion, Addit. Manuf. 35 (2020) 101377 . 
[29] M. Ramsperger, R.F. Singer, C. K ¨orner, Microstructure of the nickel-base 
superalloy CMSX-4 fabricated by selective electron beam melting, Metall. Mater. 
Trans. A 47 (2016) 1469 – 1480 . 
[30] L.N. Carter, C. Martin, P.J. Withers, M.M. Attallah, The influence of the laser scan 
strategy on grain structure and cracking behaviour in SLM powder-bed fabricated 
nickel superalloy, J. Alloy. Comp. 615 (2014) 338 – 347 . 
[31] R. Wang, J. Wang, T.W. Cao, R.X. Zhao, X.F. Lu, W. Guan, H. Tao, S.S. Shuai, X. 
S. Zhe, W.D. Xuan, C. Panwisawas, C.Y. Chen, Z.M. Ren, Microstructure 
characteristics of a Ren ´e N5 Ni-based single-crystal superalloy prepared by laser- 
directed energy deposition, Addit. Manuf. 61 (2023) 103363 . 
[32] S.C. Ci, J.J. Liang, J.G. Li, H.W. Wang, Y.Z. Zhou, X.F. Sun, Y.T. Ding, 
Microstructure and stress-rupture property of DD32 nickel-based single crystal 
superalloy fabricated by additive manufacturing, J. Alloy. Comp. 854 (2021) 
157180 . 
[33] J.W. Wang, H.M. Wang, H.W. Gao, H.W. Deng, M.L. Zhang, X. Cheng, S.Q. Zhang, 
D. Liu, Origin of hot cracking formation and suppression method in laser additive 
manufactured nickel-based superalloys, Mater. Lett. 352 (2023) 135200 . 
[34] M. Zhong, H. Sun, W. Liu, X. Zhu, J. He, Boundary liquation and interface 
cracking characterization in laser deposition of Inconel 738 on directionally 
solidified Ni-based superalloy, Scr. Mater. 53 (2005) 159 – 164 . 
[35] S. Griffiths, H. Tabasi, T. Ivas, X. Maeder, A. De Luca, K. Zweiacker, R. Wrobel, 
J. Jhabvala, R. Log ´e, C. Leinenbach, Combining alloy and process modification 
for micro-crack mitigation in an additively manufactured Ni-base superalloy, 
Addit. Manuf. (2020) 101443 . 
[36] Y. Li, K. Chen, N. Tamura, Mechanism of heat affected zone cracking in Ni-based 
superalloy DZ125L fabricated by laser 3D printing technique, Mater. Des. 150 
(2018) 171 – 181 . 
[37] H.E. Sabzi, S. Maeng, X.Z. Liang, M. Simonelli, N.T. Aboulkhair, P.E.J. Rivera- 
Díaz-del-Castillo, Controlling crack formation and porosity in laser powder bed 
fusion: alloy design and process optimization, Addit. Manuf. 34 (2020) 101360 . 
[38] Y.T. Tang, C. Panwisawas, J.N. Ghoussoub, Y. Gong, J.W. Clark, A.A. N ´emeth, D. 
G. McCartney, R.C. Reed, Alloys-by-design: application to new superalloys for 
additive manufacturing, Acta Mater. 202 (2021) 417 – 436 . 
[39] S.P. Murray, K.M. Pusch, A.T. Polonsky, C.J. Torbet, G.G. Seward, N. Zhou, S. 
A. Forsik, P. Nandwana, M.M. Kirka, R.R. Dehoff, et al., A defect-resistant Co-Ni 
superalloy for 3D printing, Nat. Commun. 11 (1) (2020) 1 – 11 . 
[40] R.C. Reed, 2006, The Superalloys fundamentals and applications. 
[41] W. Song, X.G. Wang, J.G. Li, J. Meng, Y.H. Yang, J.L. Liu, J.G. Liu, Y.Z. Zhou, X. 
F. Sun, Influence of Ta/Al ratio on the microstructure and creep property of a Ru- 
containing Ni-based single-crystal superalloy, J. Mater. Sci. Technol. 89 (2021) 
16 – 23 . 
[42] Y. Chen, Y.B. Guo, M.J. Xu, C.F. Ma, Q.L. Zhang, L. Wang, J.H. Yao, Z.G. Li, Study 
on the element segregation and Laves phase formation in the laser metal 
deposited IN718 superalloy by flat top laser and gaussian distribution laser, 
Mater. Sci. Eng. A. 754 (2019) 339 – 347 . 
[43] D. Grange, J. Bartout, B. Macquaire, C. Colin, Processing a non-weldable nickel- 
base superalloy by selective laser melting: role of the shape and size of the melt 
pools on solidification cracking, Mater 12 (2020) 100686 . 
[44] Z.P. Zhou, L. Huang, Y.J. Shang, Y.P. Li, L. Jiang, Q. Lei, Causes analysis on cracks 
in nickel-based single crystal superalloy fabricated by laser powder deposition 
additive manufacturing, Mater. Des. 160 (2018) 1238 – 1249 . 
[45] Y. Chen, K. Zhang, J. Huang, S.R.E. Hosseini, Z. Li, Characterization of heat 
affected zone liquation cracking in laser additive manufacturing of Inconel 718, 
Mater. Des. 90 (2016) 586 – 594 . 
[46] J.S. Van Sluytman, T.M. Pollock, Optimal precipitate shapes in nickel-base γ - γ ′ 
alloys, Acta Mater. 60 (2012) 1771 – 1783 . 
[47] T. DebRoy, H.L. Wei, J.S. Zuback, T. Mukherjee, J.W. Elmer, J.O. Milewski, A. 
M. Beese, A. Wilson-Heid, A. De, W. Zhang, Additive manufacturing of metallic 
components - Process, structure and properties, Prog. Mater. Sci. 92 (2018) 
112 – 224 . 
[48] R.C. Reed, T. Tao, N. Warnken, Alloys-by-design: application to nickel-based 
single crystal superalloys, Acta Mater. 57 (19) (2009) 5898 – 5913 . 
[49] S.M. Cardonne, P. Kumar, C.A. Michaluk, H.D. Schwartz, Tantalum and its alloys, 
Int. J. Refract. Met. Hard Mater. 13 (1995) 187 – 194 . 
[50] L. Zheng, G.Q. Zhang, T.L. Lee, M.J. Gorley, Y. Wang, C.B. Xiao, Z. Li, Mater. Des. 
61 (2014) 61 – 69 . 
[51] M. Abbasi, D.I. Kim, J.H. Shim, W.S. Jung, Effects of alloyed aluminum and 
titanium on the oxidation behavior of Inconel 740 superalloy, J. Alloy. Compd. 
658 (2016) 210 – 221 . 
[52] P. Kanagarajah, F. Brenne, T. Niendorf, H.J. Maier, Inconel 939 processed by 
selective laser melting: Effect of microstructure and temperature on the 
mechanical properties under static and cyclic loading, Mater. Sci. Eng. A. 588 
(2013) 188 – 195 . 
[53] H. Qi, M. Azer, A. Ritter, Studies of standard heat treatment effects on 
microstructure and mechanical properties of laser net shape manufactured 
Inconel 718, Metall. Mater. Trans. A. 40 (2009) 2410 – 2422 . 
[54] J.D. DeFouw, D.C. Dunand, Processing and compressive creep of cast replicated 
IN792 Ni-base superalloy foams, Mater. Sci. Eng. A. 588 (2012) 129 – 133 . 
[55] W. Zhou, G. Zhu, R. Wang, C. Yang, Y. Tian, L. Zhang, A. Dong, D. Wang, D. Shu, 
B. Sun, Inhibition of cracking by grain boundary modification in a non-weldable 
nickel-based superalloy processed by laser powder bed fusion, Mater. Sci. Eng. A 
791 (2020) 139745 . 
[56] A.A.N. N ´emeth, D.J. Crudden, D.M. Collins, V. Kuksenko, C.H. Liebscher, D.E. 
J. Armstrong, A.J. Wilkinson, R.C. Reed, On the influence of Nb/Ti ratio on 
environmentally-assisted crack growth in high-strength nickel-based superalloys, 
Metall. Mater. Trans. A 49 (9) (2018) 3923 – 3937 . 
[57] M. Cloots, P.J. Uggowitzer, K. Wegener, Investigations on the microstructure and 
crack formation of IN738LC samples processed by selective laser melting using 
Gaussian and doughnut profiles, Mater. Des. 89 (2016) 770 – 784 . 
[58] X. Wang, L.N. Carter, B. Pang, M.M. Attallah, M.H. Loretto, Microstructure and 
yield strength of SLM-fabricated CM247LC Ni-superalloy, Acta Mater. 128 (2017) 
87 – 95 . 
[59] D. Dye, O. Hunziker, R. Reed, Numerical analysis of the weldability of 
superalloys, Acta Mater. 49 (4) (2001) 683 – 697 . 
[60] Y.F. Li, J.Q. Wang, E.H. Han, W.B. Wu, H. H ¨anninen, Multi-scale study of 
ductility-dip cracking in nickel-based alloy dissimilar metal weld, J. Mater. Sci. 
Technol. 35 (2019) 545 – 559 . 
[61] M. Zhong, H. Sun, W. Liu, X. Zhu, J. He, Boundary liquation and interface 
cracking characterization in laser deposition of Inconel 738 on directionally 
solidified Ni-based superalloy, Scr. Mater. 53 (2) (2005) 159 – 164 . 
[62] J.P. Choi, G.H. Shin, S.G. Yang, D.Y. Yang, J.S. Lee, M. Brochu, J.H. Yu, 
Densification and microstructural investigation of inconel 718 parts fabricated by 
selective laser melting, Powder Technol. 310 (2017) 60 – 66 . 
[63] S. Li, Q.S. Wei, Y.S. Shi, Z.C. Zhu, D.Q. Zhang, Microstructure characteristics of 
Inconel 625 superalloy manufactured by selective laser melting, J. Mater. Sci. 
Technol. 35 (2015) 946 – 952 . 
[64] J. Jiang, T.B. Britton, A.J. Wilkinson, Accumulation of geometrically necessary 
dislocations near grain boundaries in deformed copper, Philos. Mag. Lett. 92 (11) 
(2012) 580 – 588 . 
[65] W. Boettinger, U. Kattner, K. Moon, J. Perepezko, DTA and Heat Flux DSC 
Measurements of Alloy Melting and Freezing, National Institute of Standards and 
Technology Special Publication, pp. 151-221. 
[66] Y. Murata, R. Ninomiya, N. Yukawa, A nickel-hafnium intermetallic compound 
and its transformation in a hafnium-doped nickel-base superalloy, Scr. Mater. 22 
(1988) 21 – 26 . 
[67] J.N. Ghoussoub, P. Klup ´s, W.J.B. Dick-Cleland, K.E. Rankin, S. Utada, P.A. 
J. Bagot, D.G. McCartney, Y.B. Tang, R.C. Reed, A new class of alumina-forming 
superalloy for 3D printing, Addit. Manuf. 52 (2022) 102608 . 
[68] K.N. Amato, S.M. Gaytan, L.E. Murr, E. Martinez, P.W. Shindo, J. Hernandez, 
S. Collins, F. Medina, Microstructures and mechanical behavior of Inconel 718 
fabricated by selective laser melting, Acta Mater. 60 (2012) 2229 – 2239 . 
[69] J.U. Park, S.Y. Jun, B.H. Lee, J.H. Jang, B.S. Lee, H.J. Lee, J.H. Lee, H.U. Hong, 
Alloy design of Ni-based superalloy with high γ ′ volume fraction suitable for 
additive manufacturing and its deformation behavior, Addit. Manuf. 52 (2022) 
102680 . 
W. Song et al.

## Page 20

Additive Manufacturing 84 (2024) 104098
20
[70] S. Kou, A criterion for cracking during solidification, Acta Mater. 88 (2015) 
366 – 374 . 
[71] T. Clyne, G. Davies, Br. Foundrym. 74 (1981) 65 – 73 . 
[72] A. Hariharan, L. Lu, J. Risse, A. Kostka, B. Gault, E.A. J ¨agle, D. Raabe, 
Misorientation-dependent solute enrichment at interfaces and its contribution to 
defect formation mechanisms during laser additive manufacturing of superalloys, 
Phys. Rev. Mater. 3 (2019) 123602 . 
[73] P. Kontis, E. Chauvet, Z. Peng, J.Y. He, A.K.D. Silva, D. Raabe, C. Tassin, J. 
J. Blandin, S. Abed, R. Dendievel, B. Gault, G. Martin, Atomic-scale grain 
boundary engineering to overcome hot-cracking in additively-manufactured 
superalloys, Acta Mater. 177 (2019) 209 – 221 . 
[74] J.J. Xu, X. Lin, P.F. Guo, Y.L. Hu, X.L. Wen, L. Xue, J.R. Liu, W.D. Huang, The 
effect of preheating on microstructure and mechanical properties of laser solid 
forming IN-738LC alloy, Mater. Sci. Eng. A 691 (2017) 71 – 80 . 
[75] Q.Q. Han, Y.C. Gu, J. Huang, L.W. Wang, K.W.Q. Low, Q.X. Feng, Y.Y. Yin, R, 
Setchi Selective laser melting of Hastelloy X nanocomposite: effects of TiC 
reinforcement on crack elimination and strength improvement, Compos. Part B- 
Eng. 202 (2020) 108442 . 
[76] V. Divya, R. Mu ˜noz-Moreno, O. Mess ´e, J. Barnard, S. Baker, T. Illston, H. Stone, 
Microstructure of selective laser melted CM247LC nickel-based superalloy and its 
evolution through heat treatment, Mater. Charact. 114 (2016) 62 – 74 . 
[77] W. Song, X.G. Wang, J.G. Li, L.H. Ye, G.C. Hou, Y.H. Yang, J.L. Liu, J.D. Liu, W. 
L. Pei, Y.Z. Zhou, X.F. Sun, Effect of ruthenium on microstructure and high- 
temperature creep properties of fourth generation Ni-based single-crystal 
superalloys, Mater. Sci. Eng. A 772 (2020) 138646 . 
[78] Z. Zhu, H. Basoalto, N. Warnken, R.C. Reed, A model for the creep deformation 
behaviour of nickel-based single crystal superalloys, Acta Mater. 60 (2012) 
4888 – 4900 . 
[79] Y.L. Hu, X. Lin, Y.L. Li, S.Y. Zhang, X.H. Gao, F.G. Liu, X. Li, W.D. Huang, Plastic 
deformation behavior and dynamic recrystallization of Inconel 625 superalloy 
fabricated by directed energy deposition, Mater. Des. 186 (2020) 108359 . 
[80] X.F. Dang, Y. Li, K. Chen, U. Ramamurty, S.H. Luo, X.Q. Liang, W.F. He, Avoiding 
cracks in additively manufactured non-weldable directionally solidified Ni-based 
superalloys, Addit. Manuf. 59 (2022) 103095 . 
[81] D. Furrer, γ ′ formation in superalloy U720LI, Scr. Mater. 40 (1999) 1215 – 1220 . 
[82] E.I. Galindo-Nava, L.D. Connor, C.M.F. Rae, On the prediction of the yield stress 
of unimodal and multimodal γ ′ Nickel-base superalloys, Acta Mater. 98 (2015) 
377 – 390 . 
[83] R.D.D. Bert Verlinden, J. Driver, I. SamajdarChapter 4 Work hardening Elsevier , 
Thermo-Mechanical Processing of Metallic Materials , 2007, 55 – 81. 
[84] Y.K. Kim, J. Choe, K.A. Lee, Selective laser melted equiatomic CoCrFeMnNi high- 
entropy alloy: microstructure, anisotropic mechanical response, and multiple 
strengthening mechanism, J. Alloy. Compd. 805 (2019) 680 – 691 . 
[85] K.M. Bertsch, G. Meric de Bellefon, B. Kuehl, D.J. Thoma, Origin of dislocation 
structures in an additively manufactured austenitic stainless steel 316L, Acta 
Mater. 199 (2020) 19 – 33 . 
[86] A.W. Thompson, Substructure strengthening mechanisms, Metall. Trans. A 8 
(1977) 833 – 842 . 
[87] U.F. Kocks, H. Mecking, Physics and phenomenology of strain hardening: the FCC 
case, Prog. Mater. Sci. 48 (2003) 171 – 273 . 
[88] H.A. Roth, C.L. Davis, R.C. Thomson, Modeling solid solution strengthening in 
nickel alloys, Metall. Mater. Trans. A 28 (1997) 1329 – 1335 . 
[89] C.X. Shi, China Superalloys Handbook, pp. 393-398. 
[90] Y. Lu, S. Ma, B.S. Majumdar, 2008, 11th International Symposium on 
Superalloys553 – 562. 
[91] Z.K. Chu, J.J. Yu, X.F. Sun, H.R. Guan, Z.Q. Hu, Tensile property and deformation 
behavior of a directionally solidified Ni-base superalloy, Mater. Sci. Eng. A 527 
(2010) 2010 – 3014 . 
[92] R.V. Miner, R.C. Voigt, J. Gayda, T.P. Gabb, Orientation and temperature 
dependence of some mechanical properties of the single crystal nickel-based 
superalloy Rene-N4.1. tensile behavior, Metall. Trans. A 17 (1986) 491 – 496 . 
[93] X.Y. Li, P. Li, Y.Z. Zhou, T. Jin, Z.F. Zhang, Effect of orientation misorientation on 
the tensile properties of SRR99 superalloy bicrystals, Acta Metall. Sin. ( Chin. ) 49 
(2013) 351 – 357 . 
[94] L.P. Kubin, B. Lisiecki, P. Caron, Octahedron slip instabilities in γ / γ ′ superalloy 
single crystals CMSX-2 and AM3, Philos. Mag. A 71 (1995) 991 – 1009 . 
[95] C.X. Shi, China Superalloys Handbook, pp. 581-587. 
[96] X.H. Xiong, D.M. Quan, P.D. Dai, Z.P. Wang, Q.X. Zhang, Z.F. Yue, 2015, Tensile 
behavior of nickel-base single-crystal superalloy DD6 636608 – 612. 
[97] C.X. Shi, China Superalloys Handbook, pp. 574-580. 
[98] D. Tomus, Y. Tian, P.A. Rometsch, M. Heilmaier, X.H. Wu, Influence of post heat 
treatments on anisotropy of mechanical behaviour and microstructure of 
Hastelloy-X parts produced by selective laser melting, Mater. Sci. Eng. A 667 
(2016) 42 – 53 . 
[99] L. Rickenbache, T. Etter, S. Hovel, K. Wegener, High temperature material 
properties of IN738LC processed by selective laser melting (SLM) technology, 
Rapid. Prototyp. J. 19 (2013) 282 – 290 . 
[100] T. Bauer, K. Dawson, A.B. Spierings, K. Wegener, Microstructure and mechanical 
characterisation of SLM processed Haynes ® 230 ® , ETH Library, 2015, 
pp. 813 – 822 . 
W. Song et al.
