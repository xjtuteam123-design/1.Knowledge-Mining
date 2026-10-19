# 1-s2.0-S2214860424005104-main

<!-- source: D:\总文献\1-s2.0-S2214860424005104-main.pdf -->
<!-- file_sha256: 6237e615c8e51e14e092d92a1b88b9f9251e85af725d906a0b579a23e1d6749e -->

## Page 1

Review
Laser-based additive manufacturing of refractory metals and their alloys: 
A review
Cecilie Vase Funch
a , *
, Gw ´ena ¨elle Proust
a , b
a
School of Civil Engineering, The University of Sydney, Sydney, NSW 2006, Australia
b
Sydney Manufacturing Hub, The University of Sydney, Sydney, NSW 2006, Australia
ARTICLE INFO
Keywords:
Refractory metals
Additive manufacturing
Laser powder-bed fusion
Laser directed energy deposition
Tungsten
Molybdenum
Tantalum
Niobium
Rhenium
High entropy alloys
ABSTRACT
The system of refractory metals and their alloys appear to be promising candidate materials for additive 
manufacturing. These materials are challenged by a combination of high raw material costs, complex geometries 
and applications as well as machining difficulties, which additive manufacturing can help alleviate. Pure 
tungsten produced by laser-based additive manufacturing suffers from cracking due to its brittle nature. The 
cracking could be improved but not eliminated through optimisation of the build process parameters and scan 
strategies. Alloying to improve ductility and reduce oxygen contamination at grain boundaries proved more 
successful. Pure molybdenum faces similar challenges with cracking due to brittleness, which could be limited by 
process optimisation, but more effectively optimised by alloying and grain refinement. Tantalum has almost 
solely been produced as the pure material and significant research has focussed on manufacturing porous lattice 
structures for implant applications. Research on niobium and niobium-based alloys has been more limited, but 
their higher inherent ductility makes cracking less likely. Only a single study produced pure rhenium by additive 
manufacturing. This contribution will review and provide an overview of the state of the research field regarding 
laser-based additive manufacturing with a specific focus on the resulting microstructures, densification levels, 
cracking behaviour and mechanical performance of these materials. Furthermore, this review will provide 
suggestions for the direction of research for each refractory metal alloy system within the field of additive 
manufacturing.
1. Introduction
Technological advancements have steadily raised the required 
operating temperatures in many different fields of applications such as 
nuclear energy, space reactors, advanced aerospace developments and 
hypersonic flights. Nickel-based superalloys have often been the mate -
rial of choice for these applications, but they are usually limited to 
maximum application temperatures of around 1077 
◦
C, which is 
increasingly proving to be insufficient [1] . The group of metals with a 
melting temperature above 2000 
◦
C is usually classified as refractory 
and includes niobium (Nb), molybdenum (Mo), tantalum (Ta), tungsten 
(W) and rhenium (Re) [1 – 3] . These metals possess a range of desirable 
properties, which dictate their areas of application. Most of these metals 
have a body-centred cubic (BCC) crystal structure, except rhenium 
which has a hexagonal close-packed (HCP) crystal structure. They are 
generally characterised by a high or very high density and good wear 
resistance [2] . Depending on the exact definition, sometimes other 
elements with melting temperatures below 2000 
◦
C are also classified as 
refractory (chromium (Cr), vanadium (V), hafnium (Hf), titanium (Ti), 
zirconium (Zr), ruthenium (Ru), osmium (Os), rhodium (Rh), and 
iridium (Ir)) [2] , but only the aforementioned five elements will be 
covered by this review.
The most important physical properties of these five refractory ele -
ments are summarised in Table 1 . W has the highest melting tempera -
ture of any metal at 3422 
◦
C and a high density of 19.3 g/cm
3
. The 
ductile to brittle transition temperature (DBTT) of W is significantly 
above room temperature (RT) at > 300 
◦
C, which makes the material 
brittle and usually hard to process. W has extensively been used as wire 
filaments in light bulbs and electron microscopes, X-ray targets, plasma- 
facing materials in nuclear reactors and as highly abrasion-resistant 
cutting tools as tungsten carbide [1,4] . The melting temperature of Mo 
is lower than W at 2623 
◦
C with a moderately high density at 
10.2 g/cm
3
. Similarly, Mo is often brittle at RT due to a DBTT in the 
range of 0 – 50 
◦
C depending on microstructure, purity, and heat 
* Corresponding author.
E-mail address: cecilie.funch@sydney.edu.au (C.V. Funch). 
Contents lists available at ScienceDirect
Additive Manufacturing
journal homepag e: www.else vier.com/loc ate/addma
https://doi.org/10.1016/j.addma.2024.104464
Received 26 April 2024; Received in revised form 19 September 2024; Accepted 28 September 2024 
Additive Manufacturing 94 (2024) 104464 
Available online 30 September 2024 
2214-8604/© 2024 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

## Page 2

treatment history. The main use of Mo is as an alloying element in steels 
and nickel-based superalloys but also as Mo-based alloys for radiation 
shields and heat sinks [5] . Ta has a melting temperature of 3020 
◦
C, 
good ductility, and a high density of 16.7 g/cm
3
. Ta is considered the 
most corrosion-resistant of the refractory metals due to its stable oxide 
layer, which makes it a highly desirable material to produce implants for 
the medical field [6,7] . Furthermore, its excellent resistant to most acids 
allows for implementation in heat exchangers, valves, and pipes in 
chemical plants [8] . Nb has the lowest melting temperature of the re -
fractory metals at 2477 
◦
C and the lowest density at 8.75 g/cm
3
. It ex -
hibits good ductility and corrosion resistance due to the formation of a 
stable oxide layer at room temperature. The majority of Nb is today used 
for alloying of steels and nickel-based superalloys with even low 
amounts of Nb giving a significant strength contribution [1] . Other uses 
include superconductors [9] and applications in chemical and medical 
industries due to their stability against many acids and sterilisation 
methods [8] . Re has an extremely high melting temperature of 3182 
◦
C 
and the highest density of the refractories at 21 g/cm
3
. It is characterized 
by a combination of high tensile and creep strength and good ductility 
but is almost exclusively used as an alloying element in superalloys or 
alloys based on other refractory metals [10] .
Machinability or fabricability of refractory metals can be a challenge. 
W and its alloys are usually produced by powder metallurgy due to the 
high melting temperature of W and its propensity to form highly volatile 
oxides. Powders are often produced by a hydride/dehydride and 
decrepitation process from purified ore, which will result in irregularly 
shaped powder particles. These powders are compacted and sintered 
usually using a form of resistance heating or using hot isostatic pressing 
(HIP) [2,16] . The sintered products are then shaped into the desired 
geometries by either hot- or cold-working. Even at high temperatures, W 
is usually formed as cold working below its recrystallization tempera -
ture. As an alternative, W alloys can be formed as near-net-shape com -
ponents using e.g., powder injection moulding (PIM) [2,17] . Similar 
issues occur in the processing of Mo, where Mo powder is used to create 
solid products by sintering, arc melting or electron beam melting [2,18, 
19] . Mo is generally weldable, but the welds of pure Mo are usually not 
considered for loadbearing applications due to the heat-affected zone 
(HAZ) having an increased DBTT resulting in brittle failure of the weld 
[2] . The RT brittleness of both W and Mo makes machining these ma -
terials challenging to achieve without the risk of cracking [2] . Nb alloys 
are most efficiently prepared by electron beam or arc melting. While a 
wide range of Nb alloys was developed initially with a particular focus 
on improving the high temperature strength and oxidation resistance, it 
eventually became clear that these improvements in e.g. high temper -
ature mechanical properties came with an unacceptable decline in 
machinability [2,20] . This resulted in only a handful of Nb-based alloys 
being commercially available today with Nb-1Zr and C103 alloyed with 
Hf, Ti and Zr dominating the market [21,22] . Both Ta and Re are most 
commonly prepared by powder metallurgy with the addition of arc or 
electron beam melting for purification due to their high melting tem -
peratures and reactive nature [2] . These challenges regarding 
manufacturing and machining of the different refractory metals and 
their alloys make them prime candidates for application with new and 
emerging manufacturing technologies.
Additive manufacturing (AM) of metals can be an extremely useful 
tool for manufacturing components with complicated geometries and 
highly customized design features in low-batch production runs. 
Furthermore, AM can be an important tool for improving the so-called 
buy-to-fly ratio of expensive materials and reducing material waste as 
compared to subtractive machining [23 – 25] . A wide range of metal AM 
methods has been developed using different sources of energy (laser, 
electron beam, arc) and different types of feedstock (wire, sheet, pow -
der) in a variety of machine configurations [26] . The laser-based pro -
cesses are currently the most widespread technology in metal AM due to 
their high resolution, flexible processing, and a long list of compatible 
material systems [27] . The laser-based AM processes usually use 
micron-scale spherical powder as their feedstock. The powder feedstock 
can either be supplied as a full layer spread over the build plate or 
supplied directly to the area of interest using a nozzle. The former 
method is generally known as laser-based powder-bed fusion (PBF-LB), 
while the latter is commonly called laser-based directed energy depo -
sition (DED-LB) [24] . With both processes, the material is selectively 
solidified at desired locations by a high-energy laser beam during the 
production of each layer, which usually will have a thickness of 
20 – 100 µ m [26] . The build plate is then lowered, and the next layer is 
subsequently deposited on the previously solidified material [25] . While 
many of the characteristics of the two processes are similar, the main 
difference lies in the spot size of the laser beam, the thickness of each 
powder layer, its energy input, and the resulting melt pool dimensions. 
This creates different thermal gradients depending on the characteristics 
of the specific AM process and the applied process parameters resulting 
in different cooling rates and thermal gradients in the material. PBF-LB 
is characterized by a smaller beam size and smaller layer heights, which 
in turn result in higher cooling rates compared to DED-LB, which means 
that PBF-LB generally produces a finer microstructure and a higher level 
of residual stress [28] . Furthermore, PBF-LB is more suitable to produce 
fine and complex geometrical features such as overhangs, while DED-LB 
is more suited for the manufacturing of larger scale components due to 
increased production speed [29] . DED-LB uses a smaller feedstock 
amount and can be fitted with several material hoppers, which facili -
tates the production of multi-material components [29] .
Defects are considered unavoidable byproducts of all AM processes. 
For PBF-LB and DED-LB the most common defects include porosity, 
cracking, and elemental contamination. Different types of porosity can 
appear in components produced by these processes. At insufficient en -
ergy input porosity can occur due to lack of fusion (LOF) between 
adjacent scan tracks or subsequent layers. At excessive energy inputs 
porosity can occur due to unstable melt pool conditions and keyholing 
[28,30] . When the rate of solidification exceeds the time necessary to 
ensure proper spreading of the droplet of molten metal, balling and 
interrupted scan tracks can occur [31] . Fine, spherical pores can be 
formed during AM due to the entrapment of either gas from the atmo -
sphere or powder or as evaporated alloying elements [30] . The steep 
thermal gradient and complex cyclic thermal history of the PBF-LB and 
DED-LB processes can result in the build-up of residual stresses in the 
material [28,32] . There can be several sources of this residual stress. 
Phase transformation can occur in some materials during cooling, which 
can induce stresses because of a volume mismatch of the different 
phases. Furthermore, the localized melting and rapid solidification will 
cause different levels of thermal expansion in different regions of the 
material, where the expansion of the just solidified regions will be 
constrained by cooler regions of the component. This can result in 
Table 1 
Properties of refractory elements [1 – 3,11 – 15] .
Crystal structure DBTT [
◦
C] Melting temperature [
◦
C] Density [g/cm
3
] Thermal conductivity at 20 
◦
C [W/m • K] Young ’ s modulus [GPa]
W BCC > 300 3422 19.3 175 400
Mo BCC 0 – 50 2623 10.2 142 324
Ta BCC < 250 3020 16.7 57.6 185
Nb BCC < 120 2477 8.75 54 103
Re HCP - 3182 21 71 469
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
2

## Page 3

significant residual thermal stresses in materials produced by PBF-LB 
and DED-LB, which is not in itself an issue for materials produced by 
these AM methods, however, if the level of residual stress exceeds the 
strength of the material, cracking, delamination, or warping may occur 
[28,32] . These cracks and porosities may either cause the build to fail or 
deteriorate the properties of the material. Some alloys may also be prone 
to solidification cracking or liquation cracking (both forms of hot 
cracking) as known from welding theory. Solidification cracking occurs 
when a thin film of the last remaining liquid is experiencing tensile 
stresses exceeding the crack resistance of the material. Liquation 
cracking occurs in the partially melted zone adjacent to the fusion line 
by partial melting of the solid. These phenomena can also be observed 
during some AM processes [30] . PBF-LB is conducted in an inert build 
chamber atmosphere consisting most likely of argon or nitrogen, while 
the carrier gas for the deposited powder in DED-LB will also act as a 
shielding gas for the laser-material interaction. During the solidification 
and cooling process, there will be a potential for impurity pickup leading 
to an increased content of N, O, C or H in the final component [33,34] .
The printability of metal alloys by PBF-LB and DED-LB can be diffi -
cult to assess and is generally based on extensive experimental trial and 
error [35] . Materials that are easily weldable can often also be good 
candidates for AM, but the cyclic thermal history of PBF-LB and DED-LB 
complicates this evaluation [36] . Some of the important factors for the 
print quality of PBF-LB and DED-LB include their ductility and 
thermo-physical properties of the materials leading to residual stress, 
distortion and potential cracking. Furthermore, alloying elements can be 
volatile and susceptible to vaporization during high temperature 
melting processes such as those involved in laser-based metal AM. This 
susceptibility can be assessed based on the vapor pressure of the ele -
ments and especially Al, Mn, Mg and Zn are considered at high risk of 
vaporization [26,28] . Materials that experience martensitic trans -
formations are often difficult to process using PBF-LB and DED-LB due to 
the massive stresses associated with the sudden volume changes [28] . 
Highly brittle materials also pose challenges for PBF-LB and DED-LB due 
to the thermal gradients involved in the process may lead to cracking 
during cooling [37,38] . Furthermore, alloys with a large solidification 
range (temperature difference from the formation of the first solid and 
the solidification of the last liquid) are more prone to hot cracking and 
will be challenging to implement in metal AM [39] . Furthermore, most 
refractory metals and their alloys are sensitive to non-metal impurities 
such as oxygen, nitrogen, carbon and/or hydrogen, which makes the 
control of feedstock and atmosphere purity important for additive 
manufacturing of these materials. These elements and other impurities 
are known to segregate to grain boundaries and cause embrittlement of 
the materials [18,40,41] . Especially, Ta and Nb have a high solubility of 
oxygen at elevated temperatures, which may pose challenges in PBF-LB 
and DED-LB [12] . On the contrary, molybdenum has a very low solu -
bility and is known to form an oxide film along grain boundaries, which 
makes the material extremely brittle [18] .
Refractory alloys are promising candidates for AM due to their raw 
material cost and aforementioned machining challenges. Research into 
these alloys within the field of metal AM has been increasing in the last 
decade but is still considered a niche topic as illustrated by the timeline 
in Fig. 1
1
.
W was the first of the refractory metals to be investigated back in 
2004 when Zhong et al. fabricated pure W and different W-Ni alloys 
using DED-LB for the use in a collimation component [42] . This initial 
research was followed by a five-year gap until 2009 when Gu and Shen 
used PBF-LB to produce W-Cu composites for thermal and electrical 
applications [43] . In 2010, PBF-LB was used to manufacture both W-Cu 
[44] and W-Ni-Fe [45] composites. It was not until 2012 and 2013 that 
any of the other refractory metal systems were produced by AM. In 
2012, Adams published a PhD thesis investigating Re produced by 
DED-LB [46] . This is to date the only available study of pure Re or 
Re-based alloys in AM. In 2013, Martinez et al. investigated the 
manufacturing of pure Nb by electron beam powder-bed fusion (PBF-EB) 
for its superconducting properties [47] , while Thijs et al. researched the 
crystallographic texture of pure Ta produced by PBF-LB [48] . Since 2019 
the number of publications investigating AM of refractory systems sta -
bilized to about 30 per year. Interestingly, the fraction of publications 
concerning W and W-based alloys was initially significantly higher than 
any of the other alloys but has clearly decreased since 2021. Instead, Ta, 
Mo, and refractory high entropy alloys (HEAs) contribute larger frac -
tions of the current research. In total, 192 publications and research 
studies have been published to date concerning any alloy or pure ma -
terial based on one of the five classical refractory metals with PBF-LB 
(67 %) and DED-LB (15 %) covering the majority of these studies 
( > 150 publications), see Fig. 2 . PBF-EB using powder as a feedstock also 
contributes significantly to the research into AM of refractory metals 
(10 %). More niche technologies such as wire arc additive 
manufacturing (also known as arc directed energy deposition, DED-Arc), 
wire electron beam directed energy deposition (DED-EB-W), material 
extrusion (MEX), and cold spray additive manufacturing (CSAM) have 
only minor contributions to the current state-of-the-art (a total of about 
9 %). The most investigated parameters for L-PBF have been laser 
power, scan speed and hatch spacing with lesser contributions of layer 
height, scanning strategy and composition among others, see Supple -
mentary Table 1 – 5 . For DED-LB the most investigated parameters 
include laser power, scan speed, layer height and composition as seen in 
Supplementary Table 1 – 5 .
The overall balance between the pure refractory metals and their 
alloys is almost even with 52 % of studies concerning pure materials, 
while 48 % of studies investigating the use of one or more alloying el -
ements, see Table 2 . The alloy systems for W and Mo approximately 
follow this same split between the pure metals and their alloys, while the 
Ta system is heavily dominated by the pure metal and the Nb system 
favours Nb-based alloys.
This review will be the first comprehensive review covering all re -
fractory metals as defined above along with their alloys. By covering all 
alloying systems in the same review, better comparisons between the 
differences and similarities of the microstructures and properties of each 
refractory system when produced by laser-based additive manufacturing 
as opposed to previous reviews focusing on a single refractory system 
such as W [37,38] or Ta (with a special focus on Ta implants) [49] or 
pure metals [50] . Furthermore, by including all alloys a more compre -
hensive understanding of the behaviour of these materials when pro -
duced by AM can be gained. As seen in Table 2 , refractory alloys 
represent 7 – 100 % of the studies depending on the system and therefore 
need to be included for a complete review. The review shows as well that 
pure metals are much more difficult to manufacture through AM than 
their alloys.
2. Tungsten and its alloys
W and W-based alloys are by far the most investigated refractory 
metal systems, constituting 39 % of research into AM of refractory 
metals. Almost 90 % of studies considered either PBF-LB (76 %) or DED- 
LB (9 %), while 8 % of studies considered electron beam-based processes 
(PBF-EB or DED-EB-W), see Fig. 3 . Three studies were published on 
material extrusion additive manufacturing (MEX). Two of these studies 
used a filament feedstock to produce a W-Cr alloy [51] and a W-Ni-Fe 
alloy [52] respectively, while the third study used a slurry feedstock to 
produce pure W [53] . Two other studies concerned DED-Arc of pure W 
[54] and a W-Cu-TiC alloy [55] . Of these studies, 53 % investigated pure 
W, while 47 % considered one or more alloying elements, see Table 2 .
1
As of March 2024
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
3

## Page 4

2.1. Microstructure
2.1.1. Pure tungsten
The microstructure of pure W produced by PBF-LB and DED-LB 
generally consists of a single BCC phase [56] . The grains are elongated 
approximately along the build direction or the direction of the largest 
heat flux [57 – 60] . The additive nature of the PBF-LB process often re -
sults in crystallographic texture by epitaxial growth of subsequently 
deposited layers. Sidambe et al. observed a < 111 > texture along the 
build direction, which intensified with increasing energy density [61] . 
Fig. 1. Timeline of the research into additive manufacturing of refractory metals and their alloys.
Fig. 2. Distribution of different additive manufacturing technologies within the field of refractory metals and alloys. Electron beam powder bed fusion (PBF-EB). 
Laser directed energy deposition (DED-LB). Laser powder bed fusion (PBF-LB). Wire arc additive manufacturing (DED-Arc). Wire electron directed energy deposition 
(DED-EB-W). Cold spray (CSAM). Material extrusion (MEX).
Table 2 
Overview of material classes investigated for each alloying system.
Alloy system Material class
Overall refractory 52 % Pure, 48 % Alloyed
Tungsten 53 % Pure, 47 % Alloyed
Molybdenum 55 % Pure, 45 % Alloyed
Tantalum 93 % Pure, 7 % Alloyed
Niobium 24 % Pure, 76 % Alloyed
Refractory high entropy 100 % Alloyed
Fig. 3. Statistic distribution of AM technologies within the research on W and 
W-based alloys produced by additive manufacturing.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
4

## Page 5

However, Gu et al. found a < 100 > texture when employing a zigzag 
scan strategy, which transitioned to a strong < 111 > texture, when uti -
lising a remelting strategy [62] . This is in contrast to Wang et al., who 
attributed a random crystallographic texture to the applied scan rotation 
between layers of 67 
◦
[63] .
2.1.1.1. Effect of process parameters and characteristics. The micro -
structure development during AM is sensitive to the applied process 
parameters due to changes in the applied heat input into the material. 
The exact nature of this relationship between microstructure and pro -
cessing is still being investigated and will depend on the nature of the 
alloying system. Sidambe et al. observed that decreasing the energy 
density led to grain coarsening and suggested that the maximum grain 
diameter was related to the melt pool overlap [61] . On the contrary, 
Zhang et al. noted grain refinement and formation of nanocrystalline W 
with increasing scan speed (decreasing energy density) [64] . Wen et al. 
also observed refinement of the elongated W grains with increased scan 
speed, which at very high scan speeds caused a columnar-to-equiaxed 
transition and some equiaxed grains were formed due to the high 
cooling and crystallisation rates [59] . Li et al. observed grain refinement 
with increasing scan speed as well as a change in melt pool shape, which 
in turn changed the orientation of the elongated W grains as the direc -
tion of heat flux changed [65] . Huang et al. noted a smaller grain size at 
the bottom of the sample compared to the top and attributed this to the 
part being built directly onto the build plate, which led to a higher 
cooling rate in this area [66] . Sidambe et al. also noted that scanning of 
different-sized areas may lead to different levels of heat flux due to 
changes to the length of the laser path, which in turn will lead to 
different local variations in the cooling rate of the process [61] .
Xiong et al. observed the formation of a fine-grained zone when 
employing a laser remelting strategy by partial transformation of the 
columnar grains and a higher cooling rate during remelting [58] . On the 
other hand, Gu et al. observed grain coarsening due to additional heat 
input during laser remelting [62] . Wang et al. observed changes in grain 
shape when employing different scan strategies [67] . When no scan 
rotation was utilised, slender grains stacked together and formed par -
allel grain rows, whereas a 67 
◦
rotation interrupted this grain stacking, 
which created a more intertwined grain structure. Remelting completely 
removed these slender grains, but did not cause grain refinement as the 
cooling rate during this remelting was similar to the initial solidification 
[67] .
2.1.1.2. Effect of atmosphere. Oxygen contamination and oxide forma -
tion have been an important topic for additively manufactured W due to 
their effect on cracking, DBTT and mechanical properties. Kemnitz et al. 
found that adding hydrogen to the protective argon atmosphere resulted 
in grain refinement by the formation of very fine oxides at the grain 
boundaries, which hindered grain boundary movement [68] . The 
hydrogen addition resulted in increased oxygen content in the as-built 
material by suppression of tungsten oxides sublimation and reduction 
of higher order oxides [68] . Braun et al. observed that the oxygen 
segregated to high-angle grain boundaries (HAGBs) formed nanoscale 
tungsten oxides at the boundaries leading to an increased DBTT [69] . 
They however mainly attributed this oxygen impurity to the purity of 
the W feedstock and an initial oxygen content of 227 ppm [69] .
2.1.2. Tungsten-based alloys
2.1.2.1. Alloying with refractory elements. W for PBF-LB has been 
alloyed with other refractory elements to control the microstructure, 
improve processability and target specific properties. From conventional 
manufacturing, this alloying strategy is known to improve strength and/ 
or ductility through solid solution strengthening or softening along with 
grain refinement [40,70 – 72] . For AM of W-based alloys, alloying with 
mainly Ta, Re and Nb has been investigated. Eckley et al. observed that 
the addition of 25 wt% Re to pure W transitioned the microstructure 
from columnar to equiaxed grains and provided significant grain 
refinement [73] , see Fig. 4 a-c. Chen et al. observed grain refinement and 
carbide formation from the addition of 5 wt% Re along with dilute C 
alloying [74] . Li et al. observed grain refinement and the formation of a 
cell structure with clusters of nanoscale Ta oxides and a high dislocation 
density in an alloy with 3 wt% Ta [75] . Similar cell structures were 
observed by Wang et al. in a 6 wt% Ta alloy by segregation of Ta and O 
to the cell boundaries [76] and by Li et al. in a 3 wt% Ta alloy [77,78] , 
see Fig. 4 d. LeSieur et al. noted cellular structures in specimens con -
taining at least 5 wt% Ta [79] . Li et al. observed nanoscale Ta oxides and 
dislocation tangles in a 6 wt% Ta alloy [80] . It is not clear whether the 
oxides in any of these W-Ta alloys were formed by the pickup of at -
mospheric impurities or impurities in the powder feedstock [75] . Wang 
et al. saw an increase in oxygen content of the W-6Ta alloy as the applied 
polyhedral Ta powder had a much higher oxygen content than the 
99.9 % purity W powders [76] . Ivekovi ´c et al. observed grain refinement 
and an increased < 111 > crystallographic texture when adding 5 – 10 wt 
% Ta to pure W [81] . On the contrary, LeSieur et al. observed a gradual 
reduction in texture from the initial weak < 111 > texture of pure W to a 
random texture with the addition of 11 wt% Ta [79] . Xue et al. observed 
elongated grains with an almost random crystallographic texture during 
PBF-LB of W-5 wt% Nb with a distribution of nanoscale Nb
x
O
y 
pre -
cipitates as seen in Fig. 4 e [82] . At the melting temperature of W, the 
solubility of oxygen increases significantly, resulting in a pickup of these 
impurities and oxide formation [82] .
2.1.2.2. Particle additions. Several studies have focused on controlling 
the microstructure of W produced by AM by mixing different powder 
particles into pure W. These changes in microstructure as a result of the 
powder alloying will depend on how the particles are distributed in the 
microstructure and their degree of melting. Li et al. investigated adding 
ZrC particles to pure W during PBF-LB and found that this resulted in 
grain refinement and a microstructure consisting of both thin columnar 
grains and fine equiaxed grains due to grain boundary pinning [83] . This 
inhomogeneous microstructure is speculated to be related to the uneven 
distribution of the ZrC nanoparticles [83] . During PBF-LB, the ZrC 
particles were transformed into nanoscale ZrO
2 
precipitates, which were 
homogeneously distributed in the W grains [83] . Gu et al. added TiC 
particles to pure W, which resulted in a solid solution of W with Ti and C, 
where the Ti and C content increased with increasing energy density 
[84] . The microstructure was found to evolve from cellular to cellular 
dendritic to equiaxed with gradually increasing energy input [84] . Guo 
et al. added nanoscale Fe and Ni, which created a significantly refined 
microstructure of equiaxed grains with a strengthened < 100 > crystal -
lographic texture [85] . No grain refinement was observed by Hu et al. 
when investigating microscale and nanoscale Y
2
O
3 
particles to pure W, 
however nanoscale Y
2
O
3 
particles changed the shape of the W grains 
[86] . Microscale Y
2
O
3 
was found to agglomerate in the upper half of the 
melt pool, while nanoscale Y
2
O
3 
was evenly distributed in the micro -
structure [86] .
2.1.2.3. Tungsten heavy alloys. W-heavy alloys (WHAs) generally 
consist of unmelted or partially melted W particles in a matrix. These 
alloys act as a composite providing properties of the hard/brittle W 
particles in combination with a softer/more ductile matrix material [87, 
88] . These microstructure characteristics have made WHAs a prominent 
topic of research in the AM field to aid the processability of W. The 
W-Ni-Fe system is a popular WHA and its microstructure when produced 
by PBF-LB consists of pure W in a W-Fe-Ni matrix [89,90] . At low energy 
densities, only the melting of the Ni-Fe matrix phase occurs, which is 
comparable to liquid phase sintering [45,91] . At intermediate energy 
density, partial melting of the W particles occurs, while full melting 
occurs at high energy densities [91] . Full melting is associated with 
excessive binder evaporation and cracking due to continuity between 
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
5

## Page 6

unmelted W particles [91,92] . Wang et al. noted that solid-state sin -
tering of W did not occur due to the rapid cooling rate and short sin -
tering time of the PBF-LB process [93] . For optimal properties, the 
microstructures should consist of partially melted W particles in a 
dendritic matrix of reprecipitated W and Ni-Fe [91] . Schwanekamp et al. 
observed almost pure W in the centre of the scan track due to the high 
temperature of the liquid in this location [92] , while Chen et al. noted 
the melting of W at the top of the melt pool [94] . Gravity-induced 
segregation resulted in more W particles at the bottom of the melt 
pool [94] . Chen et al. showed that the microstructure changed with the 
amount of binder in the alloy. When the alloys had a low binder content, 
the W particles had direct contact with each other as illustrated in Fig. 5
[94] . The addition of Co to the alloy improved the solubility of W in the 
matrix [94] . Zhang et al. observed the formation of the Ni
4
W interme -
tallic and that the content of Ni
4
W increased with increasing Ni content 
[95] . In addition to Ni
4
W, Miranda et al. also observed the formation of 
the NiW and NiW
2 
intermetallics [96] . Other WHAs contain Cu as the 
matrix element, but similar microstructures consisting of W in a Cu 
matrix are formed during PBF-LB [44] . While W and Cu have good 
wettability, they are mutually insoluble, so negligible W reprecipitation 
occurs in this system [43] . Adding Ni to the W-Cu system was shown by 
Yan et al. to improve sintering and promote some solubility of W in the 
matrix [97] . This solubility was confirmed by Zhang et al., where cel -
lular/dendritic structures adjacent to unmelted W particles [98] . Wang 
et al. noted that the dendrite arms were rich in W, while the 
inter-dendritic region showed Ni and Cu segregation up to the ends of 
the dendrites [99] .
2.1.3. Laser directed energy deposition of W and W-based alloys
DED-LB of W and W-based alloys has been studied to a much smaller 
degree than PBF-LB, which is likely related to the extremely high 
melting temperature of W. During DED-LB of pure W on a steel substrate, 
formation of nanoscale Fe
7
W
6 
intermetallics was found by Xie et al. and 
their number density decreased with increasing deposition rate as less W 
dilution occurred [100] . Lee et al. developed an offset DED-LB tech -
nique, which allowed pure W to be deposited on a steel substrate 
without excessive overheating [101] . Jeong et al. noted that the carrier 
gas velocity and feed rate were especially important for ensuring a 
smooth surface finish [102] . Li et al. noted that no intermetallics were 
formed during DED-LB of a W-Ni-Fe alloy, but that the W particles are 
heterogeneously distributed in the matrix due to settlement of the par -
ticles in the liquid [103] . Polygonal W grains were found to be unmelted 
W powder particles, while dendritic W was found to be partially melted 
and reprecipitated W, which was located adjacent to the polygonal W 
grains [103] . A similar microstructure was observed by Wang et al. in 
the W-Ni system, where the partial melting of W increased with 
increasing energy density, which in turn increased the connectivity of W 
particles [104] . Zhong et al. showed that with decreasing W content in a 
W-Ni alloy, the microstructure is dominated by dendritic W rather than 
unmelted W [42] . DED-LB of a W-Cu alloy was found by Su et al. to 
consist of W particles homogeneously distributed in a Cu matrix [105] .
2.2. Densification
2.2.1. Effect of process parameters and characteristics on densification
Densification for W and W-based alloys has been a common topic of 
investigation as with most metals produced by AM as most practical 
applications require a reasonable level of densification. Several studies 
have focused on investigating the connection between PBF-LB process -
ing parameters and the achievable relative density of the material. The 
main parameters that have been investigated include laser power, scan 
speed, layer height, hatch spacing and point distance. Generally, the 
density is found to increase with increasing energy input [64,90,106, 
107] , but as the energy density is further increased the relative density 
will stabilise [44,60,108] or eventually decrease again [57,59,66,77,82, 
84,109 – 112] , see Fig. 6 a. However, there have also been observed sig -
nificant influences of the individual process parameters regardless of the 
volumetric energy density input. Several studies have concluded that the 
laser scan speed was the dominant process parameter in achieving good 
densification of these alloys when produced by PBF-LB and that a high 
laser speed generally resulted in poor density [57,113] . As the scan 
speed initially increased, fewer pores were formed due to an increased 
Fig. 4. Microstructures of W-based alloys alloyed with other refractory elements. a) Pure W, b) W-5 wt% Re, c) W-25 wt% Re [73] . Reproduced with permission from 
Springer. d) W-3 wt% Ta [78] . e) W-5 wt% Nb [82] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
6

## Page 7

effect of gas dragging probability, while further increased scan speed 
resulted in increased porosity due to additional LOF porosity and 
shrinkage cavities [59] , see Fig. 6 b. If the scan speed was too low, 
however, Ren et al. observed that extremely wide scan tracks would be 
formed, which led to a large denudation zone, where powder particles 
adjacent to the melt pool were pulled into the molten material, which in 
turn left insufficient powder for the next scan tracks [107] . Balling is a 
significant challenge for AM of W due to its high melting temperature 
and high thermal conductivity, which deteriorates the wetting behav -
iour of the W melt [114] . The solidification time is shorter than the 
spreading time, which leads to the solidification of W melt droplets as 
globular islands with significant retained porosity between these drop -
lets [108,112,114,115] . The balling phenomenon in PBF-LB of W and 
W-based alloys was found to be particularly sensitive to the applied scan 
speed. At excessively high scan speeds, the melt pool temperature was 
too low, which resulted in a high viscosity of the melt and insufficient 
wetting [57,90,106,107,110] . Lower scan speeds resulted in a longer 
liquid lifetime before solidification [64,112] . However, excessively low 
scan speeds could also be observed to cause balling by overheating of the 
melt pool and associated melt pool instability [84,109] . These issues 
with balling due to insufficient wetting were also observed to occur 
when the laser power was insufficient [43,63,116] , while excessive laser 
power also caused the same melt pool instabilities and balling [63] . 
Rebesan et al. attributed the formation of nanopores at the grain 
boundaries to the boiling and evaporation of W oxides [106] . Huang 
et al. noted that the overlap between adjacent scan tracks needed to be at 
least 50 % to prevent LOF porosity between adjacent tracks [66] . Ren 
et al. noted that an excessive hatch spacing resulted in an insufficient 
track overlap and LOF porosities between the tracks, while an insuffi -
cient hatch spacing also caused porosity due to uneven height of the melt 
tracks and uneven powder distribution [107] . Enneti et al. concluded 
that the laser power was more influential than energy density, scan 
speed and hatch spacing on the achievable density [116] . Li et al. also 
concluded that laser power was the most influential process parameter 
in determining the density of the component as compared to scan speed 
and hatch spacing [65] . Likely, the optimal density for W and W-based 
alloys can only be achieved through a simultaneous optimisation of the 
entire PBF-LB process [78,82,90,110,111] .
Gu et al. employed a laser remelting strategy to eliminate LOF 
porosity in pure W by increasing the heat input in the material [62] . 
Xiong et al. observed a competing relationship between improved 
densification and increased gas entrapment during remelting, which 
Fig. 5. The relation between the W content in a WHA and their resulting microstructure. a-b) W90 exhibiting a large degree of W-W connectivity, c-d) W80 
exhibiting larger W dispersion and some dendritic regions, and e-f) W70 exhibiting a combined microstructure of large W grains and fine dendritic regions [94] . 
Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
7

## Page 8

means that remelting parameters must be carefully chosen [58] . On the 
other hand, Wang et al. concluded that remelting provided no further 
density improvement as the maximal density was already achieved after 
the first scan when processing the W-Ni-Fe WHA [93] .
Sidambe et al. found that the number of defects increased with 
increasing build height and attributed this to variations in heat flux 
between the powder bed and the build plate, which led to variations in 
the local thermal gradients [61] . Müller et al. found that porosity 
generally decreased with increasing build plate preheating temperature 
[117] . On the contrary, Schwanekamp et al. found that a preheating of 
800 
◦
C increased the level of porosity in a W-Fe-Ni WHA produced by 
PBF-LB and attributed this to an already high energy input, which 
became excessive with the application of preheating [92] .
As all PBF-LB processes are conducted in a protective atmosphere, its 
composition may be important for densification. Dong et al. showed an 
improvement in relative density by using a nitrogen atmosphere as 
opposed to argon and speculated that the potential formation of nitrides 
would reduce the surface tension of the liquid leading to increased 
spreadability [115] . Ivekovi ´c et al. attributed a lower density achieved 
in a specific PBF-LB machine to a higher level of oxygen contamination 
in that specific machine [81] .
During the DED-LB process of pure W, Jeong et al. found a narrow 
window of an optimal combination of scan speed and laser power to 
avoid over- or under building [102] . Xie et al. observed porosity due to 
the trapping of elements evaporated from the substrate into the melt 
during DED-LB of pure W when producing components directly on the 
build plate [100] .
2.2.2. Effect of powder quality on densification
The powder quality, composition and morphology are important for 
ensuring sufficient powder packing and accordingly sufficient density of 
the final component produced by PBF-LB. Wang et al. showed that the 
uniformity of the powder bed and the laser absorptivity were improved 
by employing spherical powder rather than polyhedral, which in turn 
improved the achievable relative density [63] . The absorption coeffi -
cient of the powder bed was improved by 15 % by plasma spheroidising 
the polyhedral powder [118] . Field et al. showed that plasma spher -
oidizing of polyhedral powder eliminated the occurrence of LOF 
porosity dominating the initial irregular powder by improving the 
contact area and powder flowability and limiting the reflectivity and 
powder bed variations [119] . Similar observations were made by Ver -
donik et al., where higher levels of porosity occurred when utilising 
W-Ni-Fe powders with an irregular shape [89] . Enneti et al. showed that 
a smaller powder particle size resulted in a higher density due to better 
packing density and particle-to-particle contact [116] . Schwanekamp 
et al. compared pre-alloyed and mixed powder for a W-Ni-Fe WHA and 
found that using pre-alloyed powder improved the density by ensuring a 
decreased loss of binder by evaporation during the PBF-LB process [92] . 
In the mixed powder, the Fe and Ni particles were very small and prone 
to quickly overheating [92] .
2.2.3. Effect of alloying on densification
Alloying has been investigated as a way of improving the densifi -
cation of pure W produced by AM. Eckley et al. found that the relative 
density generally increased with increasing Re content in a W-Re alloy 
[73] . Chen et al. investigated WHAs and found that the relative density 
generally improved with decreasing W content due to the lower melting 
temperature of the matrix elements (Ni, Fe and Co) [94] . This rela -
tionship was confirmed by Zhang et al. in the W-Ni system [95] and Yan 
et al. in the W-Cu system [97] , where a significant proportion of binder 
was necessary to ensure proper densification. The addition of Ni to a 
W-Cu alloy was found to have a positive effect on the densification of the 
Cu matrix and to promote the solubility of W in the matrix [97] .
2.3. Cracking
2.3.1. Effect of process parameters and characteristics on cracking
The inherently brittle nature of W and its extremely high melting 
temperature makes processing of its alloys with laser-based AM chal -
lenging due to their crack propensity. The cracks observed in pure W 
produced by PBF-LB are likely to be thermal shrinkage cracks occurring 
due to the steep thermal gradients involved in the PBF-LB process when 
cooling below the DBTT of W. Cracks were found to run primarily along 
high-angle grain boundaries in a fine network structure, which is related 
to the weakening of grain boundaries with impurity contamination, 
particularly oxygen [57,69] . The cracks were oriented both longitudi -
nally along the centre of the scan tracks as well as transversely along the 
surface ripples, which created shorter almost “ S ” or “ V ” -shaped cracks 
Fig. 6. Correlation between part quality and process parameters for PBF-LB of pure W. a) Density initially increases with increasing energy density due to reduction 
in LOF porosity, but eventually decreases again due to balling at high energy densities. b) Excessively high power can lead to warping, while lower laser power in 
combination with high scan speeds results in dense components [59] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
8

## Page 9

[59,106] . The process parameters were found to affect the size of the 
microcracks. Abbas et al. noted that the crack size decreased with 
increasing laser power [109] . On the contrary, other studies suggested 
that the crack length, width and density can be reduced at lower energy 
inputs by tailoring the inhomogeneous temperature field and resultant 
residual stress [59,77,110,120] . Guo et al. showed that both increasing 
laser power and reducing scan speed increased the cracking of pure W 
produced by PBF-LB [110] . Similar considerations were made by 
Sidambe et al. where a wide scan track was employed to reduce the 
thermal gradients and limit cracking [61] .
Wen et al. observed warping due to excessive residual stresses, which 
was alleviated at the same energy density by employing a lower laser 
power [59] . The lower laser power resulted in a longer heating time, 
more even temperature distribution and shallower temperature gradi -
ents, which in turn reduced the residual stress created by the PBF-LB 
process [59] .
The powder characteristics can have an impact on the build quality 
and cracking, but their connection has only been investigated to a very 
limited degree. Zhang et al. found that when using a much smaller 
powder size to produce single tracks, cracking could be suppressed due 
to improved laser absorptivity [121] .
2.3.1.1. Effect of scan strategy. It is well established that the scan 
strategy or movement pattern of the laser can influence the level of re -
sidual stress induced in PBF-LB materials [28] . Wang et al. showed that 
rotating the laser between layers led to a reduced crack length of the 
longitudinal cracks by disturbing the epitaxial growth of the highly 
elongated W grains [67] . Microcracks between adjacent layers had 
different orientations due to laser rotation [59] . Gu et al. found that the 
discontinuous energy transfer of an island scan strategy led to consid -
erably more severe cracking than the continuous energy transfer of a 
zigzag pattern [62] . Furthermore, employing a remelting strategy 
further reduced cracking by reducing residual stress and eliminating 
porosity as illustrated by Fig. 7 [62] . Xiong et al. also utilised a laser 
remelting strategy but attributed the crack reduction to a more 
fine-grained structure formed during remelting, which reduced oxygen 
contamination at the grain boundaries and reduced their cracking pro -
pensity [58] . On the other hand, Wang et al. still observed elongated 
grains after remelting and that the cracks still penetrated the deposition 
layers [67] . Guo et al. developed a specialised in-situ annealing scan 
strategy to reduce the residual stresses developed during PBF-LB of a 
W-Ta alloy, which led to a significantly improved cracking behaviour 
[122] .
2.3.1.2. Effect of preheating. Other studies attempted to utilise elevated 
preheating temperatures to reduce thermal gradients during processing 
thereby limiting cracking. Müller et al. employed a preheating of 
600 – 1000 
◦
C, which reduced the crack length and connectivity, but even 
the highest preheating temperature was unsuccessful in fully elimi -
nating this phenomenon [117] . Braun et al. showed that preheating the 
build plate to 1000 
◦
C eliminated the continuous crack network and 
longitudinal cracks, but transverse cracking persisted [69] . Ivekovi ´c 
et al. similarly concluded that 400 
◦
C preheating was insufficient to 
provide meaningful crack reduction [81] .
2.3.2. Effect of alloying on cracking
2.3.2.1. Alloying with refractory elements. Most studies conclude that 
even with optimal processing parameters, microcrack formation 
appeared inevitable when processing pure W by PBF-LB and DED-LB 
[57,65,100,107,111,112] . To combat the challenge of cracking in pure 
W, various alloying elements have been introduced. Several studies 
investigated alloying with more ductile refractory elements such as Ta, 
Nb and Re. Ta has been by far the most investigated refractory alloying 
element for AM of W and is generally found to reduce crack propensity 
during PBF-LB. Li et al. attributed the observed 30 % reduction in crack 
density in the investigated W-Ta alloy to grain boundary purification by 
the formation of nanoscale Ta
x
O
y 
precipitates [75,78,80] . Ivekovi ´c et al. 
attributed the crack reduction observed in W-Ta alloys (5 and 10 wt% 
Ta) to grain refinement and increased grain boundary length [81] . Wang 
et al. mainly attributed cracking to the formation of nanopores at GBs by 
boiling W-oxides, where the addition of 6 wt% Ta trapped the nanopores 
in the grain interior, which led to an increased grain boundary strength 
[76] . Xue et al. found that alloying with 5 wt% Nb was effective in 
mostly suppressing cracking by preventing segregation of nanopores to 
the GBs and GB purification by overall grain refinement and formation 
of Nb
x
O
y 
precipitates [82] . While LeSieur et al. agreed that Nb additions 
contributed to reduced cracking and oxygen purification, they also 
observed that excessively high Nb contents (9 – 11 wt%) led to severe 
cracking due to extreme residual stress accumulation [79] . Eckley et al. 
found that alloying with 25 wt% Re led to a significant crack reduction 
due to a reduction of the DBTT of tungsten and GB purification by grain 
refinement [73] . Chen et al. observed further crack reduction by dilute 
carbon alloying of a W-5Re alloy by a reduction of stress accumulation 
during the LPBF processing [74] .
2.3.2.2. Particle additions. Other approaches for alloying to reduce 
crack density include the addition of small amounts of second-phase 
particles (usually oxides or carbides). Li et al. showed a marked 
improvement in cracking when adding ZrC particles to pure W by acting 
as heterogeneous nucleation sites during solidification and causing grain 
refinement, which also led to less oxygen impurities at the GBs and more 
uniform distribution of residual strain in the material [83] , see Fig. 8 . 
Furthermore, the ZrC particles were seen to transform to ZrO
2 
during the 
PBF-LB process, which in turn reduced the content of oxygen in solid 
solution [83] . Hu et al. showed that oxide dispersion strengthening 
(ODS) of W with nanoscale Y
2
O
3 
particles significantly reduced the 
crack density and length due to the formation of a large proportion of 
low-angle grain boundaries (LAGBs), which obstructed the path for 
crack propagation [86] . Guo et al. utilized 1 wt% each of nanoscale Fe 
and Ni powders to act as nucleation sites during solidification, which 
promoted grain refinement and formation of equiaxed grains, which in 
Fig. 7. The effect of different scan strategies on cracking in pure W produced by PBF-LB. a) Chess-board scan strategy, b) zigzag scan strategy and c) remelting 
strategy [62] . Reproduced under Creative Commons CC BY 4.0 licence.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
9

## Page 10

turn significantly reduced crack formation by distributing the plastic 
deformation homogeneously [85] .
2.3.2.3. Tungsten heavy alloys. Generally, the group of WHAs prepared 
by PBF-LB are less susceptible to cracking due to the microstructure 
consisting of W particles in a ductile matrix of Ni, Fe, Co and/or Cu [45, 
92,95] . Chen et al. showed that only the composite consisting of 70 wt% 
W was produced without cracks as a sufficient amount of ductile matrix 
elements was necessary to accommodate the residual stresses of the 
process [94] . This is consistent with Verdonik et al. observing significant 
microcracking in a WHA containing 93 wt% W [89] . Generally, an 
excessive energy density caused some cracking of the matrix due to 
shrinkage during the liquid-solid transition [44,123] . Ivekovi ´c et al. 
showed that high energy densities and the almost complete melting of W 
powders resulted in a more brittle material and increased cracking [91] .
2.4. Mechanical properties
2.4.1. Effect of process parameters and characteristics on mechanical 
properties
The mechanical properties of pure W are dependent on the applied 
process parameters. The hardness of additively manufactured W is 
usually reported to be higher than W prepared by conventional methods 
due to a combination of grain refinement and residual stresses [57,77, 
106,112] . The hardness variation with energy input and process pa -
rameters will often reflect the achievable relative density for that spe -
cific parameter set [59] . This means that hardness will initially increase 
with increasing energy input [63,109] to eventually stabilise or decrease 
when the heat input becomes excessive [57,58] . Wen et al. observed an 
increasing hardness with increasing scan speed even though the density 
decreased and related this to grain refinement at higher laser speeds 
[59] . Guo et al. reported that variations from the optimal process 
parameters lead to a decrease in hardness and attributed this to different 
levels of densification and microstructure coarsening at excessive heat 
inputs [57] . This relationship was also observed by Dong et al. when 
comparing different build chamber atmospheres, where high-density 
specimens provided a higher microhardness [115] . Gu et al. showed 
that utilising a remelting strategy resulted in a lower microhardness due 
to grain coarsening [62] . Huang et al. observed a higher hardness at the 
bottom of the sample due to finer grains in this section of the specimen 
[66] . The hardness of pure W produced by DED-LB was found by Jeong 
et al. to be lower than with PBF-LB, which they attributed to lower re -
sidual stress produced by the DED-LB process [102] .
Similarly to the microhardness, W produced by AM has a higher 
strength than conventionally manufactured W [59,107] . The compres -
sive strength was found by Wen et al. to increase with increasing scan 
speed due to reduced grain size and cracking tendency [59] . Tan et al. 
correlated optimal compressive strength to optimal densification pa -
rameters, while the inevitable microcracks proved to not be detrimental 
to the properties of the component, as they were tested in compression 
[112] . Kemnitz et al. showed that the horizontal orientation exhibited a 
significantly lower strength than the vertical orientation and attributed 
this to the highly elongated grain shape produced by the PBF-LB process 
[68] . Guo et al. noted that brittle fracture occurred during compressive 
loading, which was initiated at voids and unmelted particles [57] . The 
applied process parameters directly controlled the compressive strength 
by changing the level of residual porosity [57] , as seen in Fig. 9 a.
Gu et al. showed that the compressive strength depended on the scan 
strategy employed, where the zigzag strategy exhibited the highest 
strength and ductility even though the remelting strategy showed a 
lower porosity level and crack density [62] . They attributed this to 
significant grain coarsening of the remelting strategy [62] .
Kemnitz et al. showed that the increased oxide formation and 
resultant grain refinement, when utilising an argon-hydrogen 
Fig. 8. The crack suppression of ZrC addition during PBF-LB of pure W by grain refinement and grain boundary purification. a-c) Pure W and d-e) W-ZrC. The kernel 
average misorientation (KAM) in pure W (c) is concentrated along grain boundaries, while in the W-ZrC alloy (f) the KAM is more evenly distributed in the 
microstructure [83] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
10

## Page 11

atmosphere caused a marked increase in strength with little effect on the 
ductility, with both specimens exhibiting brittle failure [68] , see Fig. 9 a.
2.4.2. Effect of alloying on mechanical properties
The mechanical properties of W alloys will depend on their specific 
composition. Eckley et al. showed that the addition of 25 wt% Re to pure 
W increased the hardness significantly due to solid solution strength -
ening and grain refinement, while 5 wt% Re resulted in a lowered 
hardness in line with the so-called Re softening effect [73] . Guo et al. 
showed that alloying W with 12 wt% Ta resulted in improved ductility, 
but a reduced hardness of the material [122] . This is opposed by findings 
by Wang et al. who showed that a W alloy with 6 wt% Ta had a higher 
hardness and plasticity compared to pure W [76] . Gu et al. produced an 
alloy with Ti and C in solid solution and observed that the achievable 
hardness was strongly dependent on the level of densification and en -
ergy input [84] . Guo et al. observed a considerable improvement in 
compressive strength and ductility during PBF-LB of W with nanoscale 
Fe and Ni due to grain refinement and crack suppression [85] . Xue et al. 
observed an improved strength of an alloy with 5 wt% Nb and mainly 
attributed this to solid solution strengthening [82] . LeSieur et al. 
generally observed increasing strength and ductility with increasing Nb 
content in the alloy and attributed this to a combination of solid solution 
strengthening, grain refinement and less cracking [79] . The addition of 
nanoscale Y
2
O
3 
to W was found by Hu et al. to significantly improve the 
hardness due to oxide dispersion strengthening [86] .
The mechanical properties of WHAs are sensitive to W-W grain 
boundaries due to their inherent brittleness. Ivekovi ´c et al. attributed 
the brittle failure of a W-Ni-Fe WHA to its nonuniform microstructure 
and continuity between adjacent unmelted W particles [91] . Verdonik 
et al. attributed the elevated hardness of PBF-LB W-Ni-Fe to a high W 
content in the matrix and grain refinement [89] . Chen et al. found that 
the strength of a W-Ni-Fe-Co alloy improved with energy input and 
densification, but that the ductility was largely unchanged [94] . Zhang 
et al. observed a decreasing hardness with increasing build height and 
attributed this to layer thickness variations [95] . The hardness was also 
found to decrease with increasing binder content as this phase is much 
softer than W [95] . This behaviour was also observed by Yan et al. in the 
W-Cu-Ni system [97] . Wang et al. showed that the tensile strength of a 
W-Ni alloy produced by DED-LB generally increased with increasing 
energy density due to improved densification, but that excessive energy 
input and connectivity of individual W particles in the matrix resulted in 
brittle fracture [104] .
2.5. Suggested areas of research
Pure W generally seems to experience unavoidable cracking when 
processed by laser-based AM. This is reflected in the overall decline in 
publications considering W and W-based alloys for AM, see Fig. 1 . 
Therefore, it is suggested that the research in this field should focus on 
developing alloys that are designed to imbue the W with more ductility 
or ensure purification of the grain boundaries by limiting oxygen 
contamination. Additions of Zr, ZrC, Ti, Nb or Y show promise for effi -
cient oxygen trapping [79,82,83,86] , but the properties of these alloys 
still require further investigation. Reducing the DBTT of W by alloying 
with e.g. Re has also proved to be a promising solution to limit cracking, 
however at this stage mostly simple binary alloys have been investigated 
and the field could benefit from investigating the processing of more 
complex W-based alloys with AM. Due to this sensitivity to interstitials, 
it is suggested that the feedstock and atmosphere purity should be 
investigated with a particular focus on understanding the gas-metal in -
teractions during the PBF-LB and DED-LB processes. The vast majority of 
studies on PBF-LB and all studies on DED-LB use an Ar build atmosphere 
and changes to the atmosphere could provide microstructural, densifi -
cation and crack suppression benefits, which still needs to be system -
atically investigated for W and W-based alloys. Furthermore, laser-based 
AM processing may not be the ideal method for manufacturing, espe -
cially, pure W but also certain W-based alloys due to the steep thermal 
gradients created by these processes. However, WHAs appear to be 
promising candidates for alloys that can be processed by PBF-LB and 
DED-LB as the ductile matrix (consisting of e.g. Fe, Ni, Cu and/or Co) 
may be able to accommodate some of the excessive residual stresses that 
otherwise would cause cracking in solid solution tungsten alloys. For 
other W-based alloys and where pure W is required, it is suggested that 
the research focus should shift to other methods where the cooling is less 
extreme like PBF-EB, which has been shown to be effective in reducing 
or eliminating cracking in W and W-based alloys due to a combination of 
the high pre-heating, a lower oxygen contamination due to the vacuum 
atmosphere of the PBF-EB process and the slower heat transfer in vac -
uum compared to an Ar or N atmosphere [124 – 128] . Other processes 
based on powder metallurgy and sintering like binder jetting (BJT) or 
MEX [51 – 53] have also shown to be promising for the production of 
WHAs and pure W.
Fig. 9. Mechanical properties of pure W produced by PBF-LB. a) Compressive stress-strain curves for different energy densities [57] . b) Bending strength for different 
scan speeds, specimen build orientations and build chamber atmospheres [68] .
Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
11

## Page 12

3. Molybdenum and its alloys
The research into Mo-based alloys comprises about 14 % of the total 
research on refractory metals in AM. More than 60 % of these studies 
utilised PBF-LB as the manufacturing method, while around 7 % used 
DED-LB. 20 % of the studies used DED-Arc and about 10 % used an 
electron beam-based process (PBF-EB and DED-EB-W), see Fig. 10 . 
Herein around 55 % of these studies investigated pure Mo, while the rest 
contained at least one alloying element as seen in Table 2 .
3.1. Microstructure
3.1.1. Pure molybdenum
The microstructure of pure Mo produced by PBF-LB and DED-LB 
generally consists of a single BCC phase with columnar grains elon -
gated along the build direction or with an angle hereto [69] . These 
columnar grains span several layers and facilitate bonding between 
them [129,130] .
3.1.1.1. Effect of process parameters and characteristics. The complex 
thermal history of the laser-based AM processes is extremely influential 
in determining the resulting microstructure. Wang et al. showed that the 
grain shape depends on the applied scan strategy [131] . Using a scan 
strategy without rotation between layers, the grains in the XY build 
plane grew directionally along the temperature gradient from the border 
of the melt track to the centre leading to “ S ” -shaped grains on the top 
surface [131] . Using 90 
◦
rotation produced “ C ” -shaped grains in the XY 
plane, while 67 
◦
rotation resulted in equiaxed grains [131] . Yan et al., 
however, observed “ S ” -shaped grains with a 67 
◦
rotation [129] . Higashi 
et al. found that the crystallographic texture depended on the applied 
parameters for the PBF-LB process, where a high energy density gener -
ally created a < 110 > fibre texture, while a lower energy density created 
a < 100 > fibre texture [132] . An almost random texture was created at 
excessively low energy densities (high speed or low power) due to 
porosity levels inhibiting epitaxial growth [132] . This relationship be -
tween processing parameters and crystallographic texture is illustrated 
in Fig. 11 .
Braun et al. found that storing the Mo powder with 800 ppm oxygen 
in the atmosphere resulted in the formation of fine MoO
2 
precipitates at 
the grain boundaries during the PBF-LB process in coordination with 
oxygen enrichment in the last liquid to solidify [69] . Eckley et al. found 
that adding 3 % hydrogen to the argon atmosphere when processing 
pure Mo by PBF-LB led to larger oxygen content in the material and the 
formation of Mo-oxides, which in turn limited grain growth and created 
a refined microstructure [133] .
3.1.2. Molybdenum-based alloys
The microstructure of alloyed Mo will depend on the specific 
alloying system regardless of the manufacturing method. Alloying Mo 
with high amounts of Re in solid solution led to significant grain 
refinement while maintaining the columnar grains observed in PBF-LB 
of pure Mo [133,134] . Oehlerking et al. also noted that high amounts 
of Re led to texture randomization and increased oxygen content in the 
as-built material and related this to increased atmosphere reactions of 
the Re-containing alloy [134] . Fine sub-grains were found inside the 
larger elongated grains with a similar orientation to that of their parent 
grains [134] . The Mo-alloy TZM alloyed with 0.5 wt% Ti and 0.08 wt% 
Zr has great potential for applications where high-temperature resil -
ience is required [135,136] . When this alloy was produced by PBF-LB it 
consisted of elongated grains where the aspect ratio depended on the 
processing parameters [137] . Kaserer et al. found a weak < 111 > fibre 
texture during PBF-LB of the TZM alloy and that about 60 % of the grain 
boundaries were HAGBs [137] . The PBF-LB process resulted in a 
reduction in the Ti, O and C contents compared to the raw powder 
(99.9 % purity) due to the outgassing of C and Ti-oxides [137] . Oxygen 
segregation to the grain boundaries was largely prevented by the for -
mation of nanoscale ZrO
2 
and a ternary (Mo, Ti) carbide with a signif -
icant oxygen solubility [137,138] . Spherical Mo
2
C precipitates were 
found in the grain interior keeping the grain boundaries free of pre -
cipitates [137] . Increasing the carbon content in the TZM alloy to 2.3 at 
% resulted in a fine cellular network of a (Mo, Ti) carbide with dissolved 
oxygen, which contributed to significant grain refinement compared to 
standard TZM and purification of the grain boundaries [138] . This study 
found a < 100 > texture for pure and low C TZM, while the high C alloy 
resulted in randomisation of the crystallographic texture [138] . Alloying 
pure Mo with only C resulted in a fine microstructure of columnar cells 
as seen in Fig. 12 [139,140] , analogous to the cell structures seen in 
many other metals produced by AM [26] . The cell walls were formed by 
a continuous network of Mo
2
C ( Fig. 12 c-d), which was observed by 
Kaserer et al. to be finer in the bottom of the melt pools as a consequence 
of local differences in cooling rate [140] . Braun et al. also noted that the 
observed orthorhombic Mo
2
C showed solubility for oxygen leading to 
grain boundary purification [139] .
3.1.2.1. Alloying with Si. Ellsworth et al. noted that alloying pure Mo 
with nanoscale SiC powder resulted in a coarser microstructure due to 
an increased melt pool temperature and slower cooling rates [141] . 
Nanoscale silicon oxides were formed by reaction with residual oxygen 
in the atmosphere [141] . Mo alloyed with Si and B produced by PBF-LB 
consisted of Mo solid solution dendrites in a silicide matrix [142] . These 
silicides comprise about 22 % for the Mo
5
SiB
2 
phase and 48 % for the 
Mo
3
Si phase [142] . A similar microstructure was achieved by Schmelzer 
et al. by using DED-LB to produce the same Mo-Si-B alloy, albeit creating 
a coarser microstructure than the one produced by PBF-LB [143] , which 
is likely connected to differences in cooling rates between the processes 
[29] .
3.2. Densification
3.2.1. Effect of process parameters and characteristics on densification
The densification of Mo and Mo-alloys has been a common challenge 
for a large part of the research on PBF-LB and DED-LB of these materials. 
As with most metals produced by these AM processes, the density is 
sensitive to the applied process parameters and energy density of the 
laser.
At lower energy densities, the density generally increases with 
increasing energy density as the melt pool temperature increases and 
fusion between adjacent layers and scan tracks improves [131] . Even -
tually, as the energy density further increases the density will plateau 
[144] or start to decrease again [132] . Higashi et al. noted that with 
exceedingly large layer thicknesses during PBF-LB of pure Mo, the 
densification behaviour could not be correlated with energy density as 
excessive porosity always occurred in these specimens [132] . They also 
Fig. 10. Statistic distribution of AM technologies within the research on Mo 
and Mo-based alloys produced by additive manufacturing.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
12

## Page 13

observed increased porosity at excessive scan speeds regardless of the 
laser power due to insufficient time for spreading the melt [132] . 
Similarly to W, Mo faces challenges with balling due to its high surface 
tension and viscosity causing slow wetting and insufficient spreading of 
the melt. This effect was found to be improved at lower scan speeds 
[130,141] or higher laser power [130] . Faidel et al. only achieved 
Fig. 11. Effect of different scan speeds on the microstructure and crystallographic texture of pure W produced by PBF-LB. With increasing scan speed, the texture 
transitions from < 110 > fibre texture to a < 100 > fibre texture and eventually to an almost random texture at 2000 mm/s [132] . Reproduced with permission 
from Elsevier.
Fig. 12. Microstructure of Pure Mo and a Mo-0.45 wt% C alloy produced by PBF-LB. a) Pure Mo and b) 0.45 wt% C resulting in grain refinement [140] . c) and d) 
Cellular microstructure of the Mo-C alloy, showing the presence of a Mo-carbide (Mo
2
C) at the cell walls [139] .
Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
13

## Page 14

82.5 % relative density for PBF-LB of pure Mo, but noted that an 
insufficient overlap between adjacent scan tracks led to increased 
porosity, while an excessive overlap resulted in excessive heat accu -
mulation and deformation of the layer [145] .
3.2.2. Effect of powder quality on densification
The powder shape is critical to achieving a high relative density with 
polyhedral powder only reaching a density of about 84 % of the theo -
retical density of pure molybdenum compared to spherical powder 
reaching 96 – 99 % [129,130] . Wang et al. also observed a distinct 
improvement in laser absorptivity and achievable density by applying 
plasma spheroidisation to granulated polyhedral powders [131] . Van -
hoose also attributed the poor density achievable for PBF-LB of TZM to 
poor powder quality [146] .
3.2.3. Effect of alloying on densification
Another strategy to improve the densification of AM Mo-alloys is by 
addition of alloying elements to change the solidification behaviour of 
the system. Kaserer et al. found that adding 0.45 wt% C to pure Mo 
improved the relative density from 97.7 % to 99.7 % by increasing the 
temperature interval of solidification and therefore the solidification 
time [140] . They also noted that this composition is close to the Mo-C 
eutectic, which may improve the wetting behaviour and viscosity of 
the melt. Guan et al. showed that the addition of 0.9 wt% La
2
O
3 
reduced 
the amount of residual porosity of pure Mo from 0.76 % to 0.63 % and 
they attributed this to the La addition reducing the melting temperature 
of the alloy [147] . Similar observations were made by Ellsworth et al. by 
adding 0.1 wt% SiC to pure Mo [141] and by Oehlerking et al. for a 
Mo-Re alloy with 47.5 wt% Re [134] .
3.3. Cracking
3.3.1. Effect of process parameters and characteristics on cracking
Due to the DBTT of Mo being above room temperature, pure Mo is 
prone to cracking when produced by PBF-LB and DED-LB. The cracks 
usually occur parallel to the scan direction (longitudinal cracks) and/or 
at an angle of approximately 45 
◦
to the scan vector or between the 
adjacent scan tracks (transverse cracks) [69,129,131] . Attempts have 
been made to reduce or eliminate the cracking by optimising the build 
parameters, however, they have not been able to fully suppress the 
cracking phenomenon [132,145] . Wang et al. showed that employing a 
rotation of 67 
◦
between layers aided in balancing the residual stress and 
thereby reduced the crack length and inter-connection of the cracks 
[131] , see Fig. 13 .
Yan et al. and Wang et al. both showed that utilising a support 
structure and thereby increasing heat accumulation in the part and 
reducing the thermal gradient could be an effective means of sup -
pressing cracking during PBF-LB of pure Mo [129,131] . Rebesan et al. 
noted that while a support structure could be beneficial in suppressing 
longitudinal cracks, transverse cracks remained in the material [130] . 
Yan et al. also noted that increasing the pre-heating temperature of the 
chamber to 1000 
◦
C could be beneficial for crack suppression [129] , 
while Kaserer et al. noted that a pre-heating of 800 
◦
C was insufficient to 
entirely suppress cracking or change the fracture mode of the material 
[140] . Fichtner et al. noted that not even 1200 
◦
C pre-heating was suf -
ficient to produce crack-free samples in the Mo-Si-B systems [142] . 
Johnson et al. found for DED-LB that utilizing a stainless steel build plate 
with minimal pre-heating of 120 – 150 
◦
C caused less cracking by 
reducing the thermal shock and limiting the temperature gradient 
[148] . They also speculated that employing power modulation to con -
trol the thermal cycles, may be beneficial for reducing cracking in W 
produced by DED-LB [148] .
Braun et al. noted that the cracking could be significantly reduced, 
and the crack length lowered, so they no longer formed a continuous 3D 
crack network, by reducing the oxygen content in the material and build 
atmosphere [69] . The oxygen content in the powder was observed to 
increase significantly during storage (from 535 µ g/g to 1216 µ g/g ) [69] . 
Ramakrishnan et al. showed that crack-free Mo could be produced by 
utilizing a nitrogen build atmosphere rather than argon and incorpo -
rating N into the Mo lattice [144] . The presence of N in the micro -
structure raised the energy barrier for O diffusion, effectively trapping O 
interstitially and preventing the GB embrittlement caused by excessive 
oxygen content and oxide formation [144] . The crack length was found 
to gradually decrease with increasing N
2 
partial pressure in the Ar-N
2 
mixed atmosphere [149] .
3.3.2. Effect of alloying on cracking
Alloying of pure Mo with C has proved to be a promising method for 
producing crack-free Mo by PBF-LB [139,140] . Kaserer et al. showed 
that the increased grain boundary length of the cellular microstructure 
produced by PBF-LB of a Mo alloy containing 0.45 wt% C reduced ox -
ygen segregation at the boundaries and improved grain boundary 
embrittlement [140] . This is reflected in a change of fracture mode from 
intergranular in pure Mo to transgranular in the Mo-C alloy [140] . 
Similar observations were made by Kaserer et al. on modifying the TZM 
alloy with C, which led to fully crack-free samples by oxygen dissolution 
in (Mo, Ti)-carbides formed at the cell boundaries and binding oxygen in 
ZrO
2 
[138] . Fichtner et al. found that the storage and drying of the 
powder before manufacturing was crucial for reducing the oxygen 
content in the powder and producing crack-free components when 
working with a Mo-Si-B alloy [142] . Ellsworth et al. showed that while 
the addition of nanoscale SiC particles aided in trapping oxygen from the 
atmosphere, 0.1 wt% SiC was insufficient to prevent the formation of 
Mo-oxides and associated crack formation [141] . Oehlerking et al. noted 
that alloying with 47.5 wt% Re reduced the crack length of the alloy, but 
cracking persisted and the crack width was unchanged, which was 
attributed to a higher oxygen content in the Re-containing alloy [134] . 
Guan et al. found that the addition of La
2
O
3 
significantly reduced the 
crack density and crack width and attributed this to a reduction in the 
melting temperature of the alloy [147] .
3.4. Mechanical properties
3.4.1. Mechanical properties of pure Mo
The mechanical properties of additively manufactured Mo and Mo- 
based alloys have been only superficially investigated. The hardness of 
pure Mo manufactured by PBF-LB was found by Yan et al. to depend on 
the applied process parameters, where increasing laser power was 
observed to lead to increased grain refinement and accordingly 
increased hardness [129] . Furthermore, the properties will also be 
sensitive to the amount of residual stress and porosity created by the 
process parameters [129] . The achieved hardness of 202 – 260 HV is 
higher than conventional manufacturing by powder metallurgy 
(160 – 180 HV), which was largely attributed to a refined grain size due 
to the high cooling rate in the PBF-LB process [129,130] . The tensile 
strength, stiffness and ductility of PBF-LB were found to be significantly 
lower than conventionally manufactured pure Mo, which was attributed 
to cracks and unmelted particles present on the fracture surface [130] . 
These cracks were formed during the PBF-LB process due to an excessive 
oxygen content in the material as compared to the conventionally pro -
duced material [130] . Furthermore, the strength of the horizontal di -
rection was found to be distinctly lower than the vertical direction, 
which was attributed to the orientation of the elongated Mo grains 
[130] . The brittle fracture mode of additively manufactured Mo was also 
observed by Yan et al., who noted a 280 MPa bending strength and a 
mostly intergranular fracture surface [129] . Bustin noted that while 
PBF-LB Mo is exhibiting brittle fracture at room temperature, significant 
ductility can be reached at elevated temperatures [150] . The use of a 
protective atmosphere of nitrogen as compared to argon was found to 
enhance both the bending strength and ductility of the PBF-LB Mo 
[150] .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
14

## Page 15

3.4.2. Mechanical properties of Mo-based alloys
Slightly more data is available for the mechanical properties of PBF- 
LB of Mo alloys. Kaserer et al. found that adding 0.45 wt% C to pure Mo 
increased the bending strength and hardness of the material from about 
250 MPa and 208 HV for pure Mo to 1180 MPa and 343 HV for the alloy, 
which was related to better densification, crack suppression and the 
formation of a closed network of Mo
2
C [140] . The strength and hardness 
were observed to vary based on processing parameters with a lower 
energy density resulting in higher residual stress and higher hardness, 
while a lower pre-heating temperature resulted in an incomplete re -
covery and an elevated hardness but lower strength due to internal 
cracks [140] . Kaserer et al. found that the bending strength of PBF-LB of 
the TZM alloy was ~50 % lower than conventional manufacturing, 
which was related to residual porosity, internal stresses and a high 
dislocation density [137] . The bending strength was largely dependent 
on the level of residual porosity with some more porous specimens 
showing less than half of the strength of more dense specimens [137] . 
Kaserer et al. noted that the addition of 2.3 at% C to the TZM alloy 
increased the bending strength from 666 MPa to 998 MPa likely due to 
grain refinement and grain boundary purification [138] . The TMZ-C 
alloy maintained a brittle fracture mode with virtually no elongation 
at break at RT and 4 – 7 % elongation at elevated temperatures [138] .
Ellsworth et al. showed that the addition of 0.1 wt% nano-sized SiC 
powder to pure Mo increased the hardness from around 207 HV to 
around 318 HV, which was mostly attributed to the formation of nano- 
scale silicon oxides in the material [141] . The bending strength of this 
alloy also increased from 134 MPa for pure Mo to 242 MPa for Mo-SiC, 
which is likely related to better densification and less segregation of 
oxygen to the grain boundaries [141] , see Fig. 14 . The silicides formed 
in the Mo-Si-B alloy investigated by Fichtner provide a very high 
bending strength in the range of 900 – 1100 MPa, which drops to 
491 MPa at 1100 
◦
C and the alloy exhibited ductile behaviour above 
1050 
◦
C [142] . Oehlerking et al. found that alloying Mo with 47.5 wt% 
Re significantly increased not only the compressive strength but also the 
ductility of the PBF-LB alloy due to a combination of solid solution 
strengthening, texture randomization and increased densification [134] . 
Similarly, Eckley et al. found that 25 wt% Re was necessary to provide a 
meaningful strengthening effect, while 5 wt% Re resulted in the Re 
softening effect and a correspondingly lower bending strength [133] . 
Significant differences in strength between the horizontal and vertical 
build orientations were noted with the horizontal direction reaching 
only 238 MPa, while the vertical orientation achieved 614 MPa. This 
was related to the columnar nature of the as-built microstructure [133] . 
Utilizing an Ar-H atmosphere rather than pure Ar enhanced the bending 
strength of the alloys, which was attributed to the grain refinement and 
increased oxygen content with H in the atmosphere [133] .
3.5. Suggested areas of research
Similarly to W, the processing of dense and crack-free pure Mo with 
PBF-LB and DED-LB has been very challenging, and the research is 
gradually moving away from the pure material to more promising al -
ternatives. The alloy design process should focus on ensuring sufficient 
ductility through additions of high ductility alloying elements or on 
ensuring grain boundary purity by trapping oxygen contaminants in 
secondary phases. Especially carbon addition to pure Mo and Mo-based 
alloys has appeared to be a promising avenue for successfully producing 
dense, crack-free Mo components with excellent mechanical properties. 
Alloying with e.g. Re or Nb to reduce the DBTT of the Mo-alloy may 
prove to be an important research topic to allow Mo-alloys to be pro -
duced by laser-based AM. The cracking and brittleness of Mo are 
strongly linked to impurity concentration and segregation, but the pu -
rity of the feedstock has only superficially been considered at this stage. 
Utilizing higher purity feedstock may be beneficial in achieving higher 
Fig. 13. The effect of different scan strategies on the cracking behaviour of pure Mo produced by PBF-LB. a) 0 
◦
rotation, b) 90 
◦
rotation and c) 67 
◦
rotation between 
layers. Cracking is reduced by balancing the residual stress in the component and limiting stress buildup during the PBF-LB process [131] . Reproduced with 
permission from Elsevier.
Fig. 14. Comparison of the bending strength of pure Mo and a Mo-0.1 wt% SiC 
alloy as a function of the applied scan speed. The SiC significantly improved the 
strength of the material due to nano-scale Si oxides [141] . Reproduced under 
Creative Commons CC BY 4.0 licence.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
15

## Page 16

part quality of Mo and its alloys. Also, the composition of the build at -
mosphere during PBF-LB has shown to influence both microstructure 
and cracking behaviour of Mo-based alloys, however this knowledge still 
needs to be expanded and transferred to the L-DED process. The DBTT of 
Mo is highly sensitive to the oxygen content in the material [11] and will 
need to be carefully controlled to manage the cracking phenomenon in 
laser-based additive manufacturing of these alloys. If pure Mo is 
required, other manufacturing techniques such as PBF-EB with 
pre-heating above the DBTT have been shown to successfully be able to 
process pure Mo [128,151] . The heat transfer in vacuum is also slower 
than in argon and the vacuum environment provides less contamination 
with interstitials, which contributes to the success of the PBF-EB and 
DED-EB-W process for AM of pure Mo [148] . Binder jetting may also 
prove capable of producing pure Mo components, but this has not yet 
been investigated.
4. Tantalum and its alloys
The research into AM of Ta and its alloys comprises about 22 % of the 
studies on refractory metal systems. Of these studies, 68 % consider the 
PBF-LB process and 11 % investigated DED-LB, while 13 % concern PBF- 
EB and two studies investigate pure Ta produced by DED-Arc [152,153]
and cold spray (CSAM) [154,155] , respectively ( Fig. 15 ). This research 
has almost solely focused on pure Ta (93 %), while only 3 studies (7 %) 
consider Ta alloys as seen in Table 2 .
4.1. Microstructure
4.1.1. Microstructure of pure tantalum
AM of pure Ta results in the formation of a single-phase material with 
a BCC crystal structure. The directional nature of the PBF-LB process 
generally results in grain elongation along the build direction and 
crystallographic texture [48,156,157] . Pure Ta produced by PBF-LB 
generally exhibited a strong < 111 > texture aligned with the build di -
rection [156,158 – 161] , whereas the conventionally manufactured 
sample exhibited a weak < 100 > texture [156] .
4.1.1.1. Effect of process parameters and characteristics. The heat input 
and heat flux direction will change with changing process parameters 
and processing strategy. Oh et al. found the < 111 > orientation prefer -
ably aligned with the build direction, while the < 110 > orientation was 
aligned with the laser scan direction in the XY plane, which was related 
to epitaxial growth across subsequent layers [157] . Lian et al. found that 
the texture depended on the applied process parameters as the shape of 
the melt pool and direction and magnitude of local thermal gradients 
change with changing energy input [162] . Du et al. noted that a high 
energy input changed the texture from a < 111 > fibre texture at low 
energy to a random crystallographic orientation at high energy [159] . 
This also changed the grain shape from highly elongated to almost 
equiaxed [159] . The texture was also found by Thijs et al. to depend on 
the scan strategy of the process, where 0 
◦
rotation resulted in a much 
weaker < 111 > texture than 60 
◦
and 90 
◦
rotations, due to a stronger 
effect of pronounced grain selection during growth when the scan vector 
was rotated [48] , see Fig. 16 . At the outer ~300 – 350 µ m of the sample, a 
random grain orientation was produced [48] . In the XY build plane, the 
grains were found to be constrained by the edges of the scan tracks, 
creating a characteristic “ S ” -shape, which formed a checkerboard 
pattern when 90 
◦
rotation was applied [48] .
Some studies noted a fine structure of dislocation cells formed inside 
the primary BCC grains even when processing commercially pure Ta 
[163] .
Guan et al. found that processing pure Ta by DED-LB created 
comparatively coarse grains in comparison to PBF-LB and attributed due 
to a slower cooling rate of the DED-LB process [164] . Similarly to 
PBF-LB, the grains were elongated and oriented with a small deviation to 
the build direction due to the direction of a large heat flux being at an 
angle to the build direction [164] .
4.1.1.2. Effect of atmosphere. The build chamber atmosphere is impor -
tant to protect the material from excessive interstitial contamination 
during the AM process. Aliyu et al. observed the formation of Ta
2
O
5 
and 
Ta
2
O
3 
on the specimen surfaces by oxygen pickup from the argon used 
during PBF-LB of pure Ta and emphasized the importance of good at -
mosphere control [165] . Lian et al. compared the oxygen content of the 
powder and as-built pure Ta and noted an increase of both O and N due 
to atmosphere reactions [162] . Sungail et al. found that reducing the 
residual oxygen in the as-built Ta resulted in grain coarsening, as the 
oxide formation at higher oxygen concentrations was expected to hinder 
grain boundary migration [166] . Tan et al. found that an increase in 
oxygen content resulted in a change of crystallographic texture from a 
< 100 > to a < 111 > texture due to changes in the viscosity of the melt 
pool and the ability of the droplet to spread out evenly [158] , see Fig. 17 . 
The increased oxygen content also caused grain refinement, which was 
attributed to grain boundary pinning and a higher density of sub-grain 
boundaries [158] . This differing oxygen content was related to 
different atmospheres of the atomising process during the feedstock 
production [158] .
4.1.2. Microstructure of tantalum-based alloys
Sing et al. investigated a 50 % Ti/50 % Ta alloy and found that 
significant amounts of unmelted Ta particles were retained when high 
scan speeds were utilized leading to a lower Ta content than expected 
[167] . Increasing the energy to ensure full melting of the Ta could lead 
to undesirable vaporisation of Ti [167] . Ta is a β -stabiliser in Ti and 
effectively aids in retaining metastable β at room temperature during 
PBF-LB processes, when present in sufficient quantities [167] . Xie et al. 
investigated using DED-LB to deposit a Ta-Zr coating on a Ti-6Al-4V 
substrate, which produced a microstructure consisting of α -Ta grains 
and TiZr and Al
3
Zr
4 
precipitates at the grain boundaries [168] .
4.2. Densification
4.2.1. Effect of process parameters and characteristics on densification
As for most metals processed by laser-based AM, studies on Ta alloys 
processed by PBF-LB and DED-LB have been concerned with achieving a 
high relative density by optimising process parameters. Generally, the 
density was found to improve with increasing density [159,160,169]
until eventually reaching a density plateau [170] or decreasing again as 
the energy density was further increased [162,171,172] , see Fig. 18 . 
Valentino et al. found that a relatively long exposure time and slow laser 
speed were necessary to fully penetrate the powder layer and ensure 
good density and adhesion between layers [169] . Livescu et al. noted 
Fig. 15. Statistic distribution of AM technologies within the research on Ta and 
Ta-based alloys produced by additive manufacturing.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
16

## Page 17

that density improved with increasing energy density but eventually 
stabilised. Laser power and scan speed were found to have a much bigger 
impact on part quality than hatch spacing, stripe overlap and layer 
thickness [170] . Similarly, Qi et al. noted that excessive scan speeds 
increased the porosity regardless of the laser power due to increased 
surface tension of the melt, which in turn deteriorated the spreading of 
the melt [160] . Zhou et al. found that the solidification behaviour was 
particularly sensitive to the applied scan speed, where high scan speeds 
led to an increased temperature gradient and surface tension, which in 
turn caused increased porosity [172] . Excessively slow scan speeds 
caused overheating of the melt pool and porosity associated with the 
balling effect [172] . Song et al. also demonstrated keyhole porosity 
forming at low scan speeds [171] .
Chen et al. investigated producing porous pure Ta by utilising non- 
optimal processing parameters for DED-LB and found pore size and 
connectivity to increase with increasing laser speed [173] . Guan et al. 
Fig. 16. Evolution of texture intensity as a function of different scan strategies and rotations between layers during PBF-LB of pure Ta. Left: 0 
◦
rotation. Middle: 60 
◦
rotation. Right: 90 
◦
rotation [48] . Reproduced with permission from Elsevier.
Fig. 17. Comparison of different oxygen contents in pure Ta and their effect on crystallographic texture as represented by EBSD maps and pole figures. a-c) Low 
oxygen (150 ppm). d-f) High oxygen (470 ppm) [158] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
17

## Page 18

noted porosity due to entrapment of the shielding gas in the DED-LB 
process [164] . Xie et al. found porosity relating to the evaporation of 
elements with low melting temperatures (Al and Ti), which did not have 
sufficient time to escape and instead became entrapped in the solidified 
material [168] . Wermuth et al. showed high defect levels when pro -
cessing a Ta-W alloy by DED-LB and showed high defect levels due to the 
difference in melting temperature between the two powders [174] .
4.2.2. Effect of powder quality on densification
The quality of the feedstock can have a strong impact on the quality 
of the printed component, which in the case of PBF-LB and DED-LB is 
often related to the sphericity of the powder. Zhou et al. showed that the 
powder shape may influence the level of densification achievable, with 
spherical powder reaching 98.3 % density, while non-spherical powder 
only reaching 97.9 % density [163] . Qi et al. and Sungail et al. noted 
that spheroidisation of angular Ta powder improved packing density 
and flow characteristics of the powder bed, which in turn improved part 
density [160,166] . Tan et al. showed that the relative density generally 
decreased with an increase in the oxygen content in the powder during 
successive powder reuse cycles as the increased oxygen level reduced 
wetting and spreading of the molten metal, which led to balling and 
increased porosity [158] .
4.3. Cracking
Due to the high ductility of pure Ta, cracking when produced by AM 
has usually not been a significant issue [158,163,175,176] . However, 
Valentino et al. found that more microcracking occurred close to the 
build plate due to more reheating and remelting cycles [169] . On the 
contrary, Jones et al. observed cracking due to hot tearing at the top of 
the PBF-LB component [156] . Zhou et al. and Aliyu et al. found that low 
scanning speeds (and resultant high energy density) created thermal 
microcracks due to thermal shrinkage and simultaneously balling 
created cracks between layers [165,172] . On the other hand, Song et al. 
observed cracking at excessively high scanning speeds (and low energy 
density), which was correlated with insufficient fusion [171] .
4.4. Mechanical properties
4.4.1. Effect of process parameters and characteristics on mechanical 
properties
The hardness of pure Ta produced by additive manufacturing was in 
most studies found to be in the range of 150 – 250 HV, which is higher 
than pure Ta by various conventional manufacturing methods (90 – 120 
HV) [160,162,165,171,177] . This improved hardness of the PBF-LB 
process is likely related to a combination of grain refinement and re -
sidual stresses. The hardness of as-built pure Ta is comparable to the 
hardness of conventionally manufactured pure Ta subjected to severe 
plastic deformation and is likely related to the high levels of residual 
stress produced by the AM processes being comparable to this plastic 
deformation [160] . Zhou et al. found a much higher maximum hardness 
of 425 HV at an optimised process parameter combination. They related 
this high hardness to primarily a fine-grained microstructure and high 
levels of residual stress [172] , however, it is not clear why the hardness 
measured in this study is much higher than the remaining research. 
Chen et al. noted that the microhardness of pure Ta produced by DED-LB 
varied within the melt pool and attributed this to different local cooling 
rates and residual stress accumulations [173] .
Zhou et al. found that the UTS of PBF-LB-produced pure Ta was 
higher than that of conventionally manufactured Ta and comparable to 
that of cold-worked Ta [172] . They related this to high levels of residual 
stress and grain refinement [172] . While a high UTS of 739 MPa was 
achieved, the material only reached 2 % elongation at fracture [172] . 
Most studies found that a maximum elongation at fracture and tensile 
strength can be achieved simultaneously at the optimal processing pa -
rameters for ensuring low porosity levels as cracks tend to initiate at 
preexisting porosities [162,171] . Qi et al. showed that the elongation at 
fracture was especially sensitive to the residual porosity in the material, 
while the tensile strength was almost stable across the investigated 
parameter space [160] . Song et al. reached a maximum UTS of 706 MPa 
and an elongation at fracture of 33 % as seen in Fig. 19 a [171] , while 
Lian et al. found a maximum of 640 MPa and 16 % elongation [162] .
The performance of pure Ta produced by PBF-LB has been investi -
gated in shock loading at high strain rates to understand its resistance to 
spallation, which was found to be highly dependent on build orienta -
tion. The Ta produced by AM showed a higher Hugoniot Elastic Limit 
than wrought Ta, but a lower spall strength [156,178,179] , which was 
explained by the impurities in the AM components contributing to a 
higher yield strength and elastic limit and reducing the resistance to 
damage and spallation under shock loading [156] . The damage evolu -
tion of the PBF-LB specimens was primarily initiated by pre-existing 
defects from the manufacturing process [156,178,179]
4.4.2. Effect of impurity on mechanical properties
The mechanical properties of pure Ta are highly sensitive to the level 
of impurities in the material, but especially to the level of oxygen 
contamination. Sungail et al. noted that significant purification of the 
oxygen levels in the powder feedstock correlated with lower oxygen 
Fig. 18. Effect of differing scan speeds and laser powers on the achievable level of densification for pure Ta produced by PBF-LB. a) Variation of laser power under 
constant scan speed and b) variation of scan speed under constant laser power [172] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
18

## Page 19

content in the as-built pure Ta and resulted in a reduction in the hard -
ness from 237 HV to 149 HV. Guan et al. also attributed the high 
hardness achieved by DED-LB of pure Ta to high interstitial contents 
with contributions from residual stress [164] . They also showed that 
reducing the oxygen content from 700 ppm to 300 ppm in the as-built 
material reduced the hardness from 309 HV to 194 HV [164] . This 
reduction of oxygen in the powder was related to the particle size with 
the fine particles having a larger free surface area and larger interstitial 
concentrations [164] .
Sungail et al. found that reducing the residual oxygen in the as-built 
parts from 1422 ppm to 149 ppm improved the elongation at fracture 
from 4 % to 35 % [166] . Guan et al. similarly found that specimens with 
high interstitial contents failed in a brittle manner, while those with 
lower interstitial contents could achieve 14 – 16 % elongation at fracture 
and a UTS above 400 MPa [164] . Tan et al. showed that an increased 
oxygen content in the powders led to an increased oxygen content in the 
material. The oxygen segregated at the grain boundaries, which in turn 
led to a significant increase in UTS at the cost of a severe reduction in 
tensile elongation [158] , see Fig. 19 b.
4.5. Production of lattice structures
As Ta has been considered a promising material for biomedical ap -
plications a significant portion of studies have focused on lattice struc -
tures for implant production. These lattice structures are designed with 
specific porosity levels, pore sizes and strut dimensions to simulate the 
Fig. 19. Mechanical properties of PBF-LB Ta. a) The relationship between tensile properties and energy input during PBF-LB of pure Ta [171] . b) The relationship 
between mechanical properties and oxygen impurities in pure Ta [158] .
Reproduced with permission from Elsevier.
Fig. 20. Geometric morphology of trabecular Ta scaffolds with different amounts of porosity (noted on the left of the images) and under different levels of strain 
(noted on top of the images) [175] . Reproduced under Creative Commons CC BY 4.0 licence.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
19

## Page 20

properties of human bone and promote osteointegration as seen in 
Fig. 20 [175,180,181] . Yang et al. found that lattice structures produced 
by PBF-LB had a pore diameter and strut diameter significantly bigger 
than those produced by chemical vapour deposition (CVD) [177] . The 
strut diameter was especially sensitive to the applied process parameters 
[177] and the struts were generally larger than the initial design leading 
to lower pore size and porosity level [175,177,180,182] . Li et al. also 
noted that the strut size in the build direction was larger than in the 
horizontal direction, while more powder adhesion occurred on struts 
with an angle to the build plate [182] .
The mechanical properties of these lattice structures will be 
distinctly different to the properties of the solid Ta produced by AM. The 
mechanical properties are usually desired to be comparable to those of 
the human host bone to limit stress-shielding effects. Several studies 
found the compressive properties of Ta structures to be within the range 
of properties of human cancellous bone, which means a yield strength in 
the range of 6.6 – 36.2 MPa and a Young ’ s modulus in the range of 
0.88 – 3.4 GPa, respectively [161,175,177,180,183 – 185] . Some studies 
showed strengths and stiffnesses more in line with human trabecular 
bone ( σ
y 
= 0.2 – 120 MPa and E = 0.01 – 3 GPa depending on anatomic 
location) [182,186] . The mechanical properties and failure mechanisms 
are dependent on the geometry of the lattice structures and strut angles 
in relation to the loading direction [180,182] . Failure was found to 
occur predominantly on struts with more imperfections [184] and at 
junctions [175,183] . Ta produced by AM showed a better normalised 
fatigue strength compared to PBF-LB-produced Ti implants [183] .
These porous and lattice structures have been investigated for 
implant applications and were generally found to show good biocom -
patibility and bone in-growth during in-situ experiments [187,188] . 
Wauthle et al. found substantial bone in-growth and almost full defect 
bridging after 12 weeks [183] . Jiao et al. showed that the level of 
porosity affected the cell adhesion, proliferation and differentiation as 
well as the osteointegration with 70 % porous implants showing the 
most promising results and the highest level of bone in-growth [189] . 
Porous additively manufactured Ta implants showed higher osteoid 
formation 12 weeks after surgery compared to Ti implants produced by 
AM [190] . Chen et al. showed that PBF-LB-produced Ta had improved 
wettability compared to forged Ta, which led to better cell adhesion and 
proliferation [161] , while Huang et al. attributed this effect to their high 
surface area to volume ratio [186] . Torsion testing of the explants 
showed a strong implant-bone interface connection, with failure 
occurring both at the interface and in the host bone [183] .
4.6. Suggested areas of research
Contrary to the other refractory alloy systems in the context of AM, 
Ta has almost solely been investigated as a pure material. Therefore, the 
research field could logically be supported and expanded by the appli -
cation of Ta-based alloys to achieve other properties and capabilities. 
Additions of Ti, Ni, W, Mo, Nb, Re and/or Hf have all shown to improve 
the mechanical properties at elevated temperatures for Ta-based alloys 
in conventional manufacturing. The mechanical properties of pure Ta 
are highly sensitive to its oxygen content, so the effect of atmosphere 
composition and purity still needs to be understood. For other refractory 
systems (W and Mo) replacing the Ar fully or partially atmosphere with 
N or H has been shown to be impactful for reducing oxygen pickup, 
causing grain refinement, improving densification and crack suppres -
sion, however this effect should also be investigated for the Ta-system. 
PBF-EB has been shown to be a promising method of reducing oxygen 
pick-up from the atmosphere as this process is conducted under vacuum 
[191,192] . This also indicates that the effect of feedstock purity may 
need to be an area of research to achieve reliable and predictable me -
chanical properties as even small differences in interstitial content in the 
powder and final component could cause inconsistent properties. 
Furthermore, pure Ta has shown extensive promise for biomedical ap -
plications with porous and lattice-based designs having comparable 
mechanical properties to human bone. This area of research still needs to 
be further developed with a particular focus on osteointegration, 
longevity and fatigue testing.
5. Niobium and its alloys
The published research into AM of pure Nb and its alloys has 
generally been rather limited comprising about 10 % of the total 
research on refractory metals in AM. 57 % of the studies concern pro -
cessing by PBF-LB, while the remaining studies are distributed between 
DED-LB (24 %) and PBF-EB (19 %), see Fig. 21 . About a quarter of the 
studies investigate AM of pure Nb, while the majority of studies involve 
one or more alloying elements, see Table 2 .
5.1. Microstructure
5.1.1. Microstructure of pure niobium
The microstructure of pure Nb will generally consist of a single-phase 
BCC structure regardless of the production method, due to the nature of 
Nb. As is characteristic of most metals produced by PBF-LB, the grains 
are elongated along the build direction and their shape reflects the 
movement of the laser during the PBF-LB process. Griemsmann et al. 
found that highly elongated grains with a preferred orientation were 
formed along the edges of the melt pool boundaries, while the centre of 
the melt pools also exhibited grain elongation, the strength of the texture 
being weaker [193] . Liu et al. noted that PBF-LB of pure Nb creates a 
moderate < 111 > texture along the build direction with crystallographic 
misorientations being concentrated along the melt pool boundaries 
[194] .
5.1.2. Microstructure of niobium-based alloys
The microstructure of alloyed Nb produced by AM will naturally 
depend on the specific alloy used. As C103 is the most widely used Nb 
alloy in conventional manufacturing, two studies also focussed on this 
alloy which is alloyed with Hf and Ti. C103 is largely single-phase BCC 
similar to pure Nb with grains elongated along the build direction [195, 
196] , see Fig. 22 f. However, the texture was found to align the < 100 >
direction with the build direction [195] rather than the < 111 > found in 
pure Nb [194] , which may be related to differences in scan strategies 
and manufacturing parameters [197] . Mireles et al. also noted the 
presence of fine HfO
2 
precipitates due to a combination of a high oxygen 
in the powder feedstock along with pickup from the build atmosphere 
[196] . Awasthi et al. found a high dislocation density and a cellular 
structure in PBF-LB produced C103 [195] , similar to the cell structures 
observed in many other alloys produced by AM [28] , see Fig. 22 a-e. 
Dense C103 was also produced by Ferguson et al. using the DED-LB 
process [198] . The conventional Nb521 alloy (alloyed with W, Mo and 
Fig. 21. Statistic distribution of AM technologies within the research on Nb and 
Nb-based alloys produced by additive manufacturing.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
20

## Page 21

Zr) has also been prepared by PBF-LB and the microstructure was found 
to consist of large columnar grains with fine equiaxed grains at the edges 
of the melt pools [199] . A weak < 111 > crystallographic texture was 
reported along the build direction. Zirconia (ZrO
2
) precipitates formed 
primarily at the bottom of the melt pool [199] . On the contrary, Chen 
et al. observed the formation of fine, homogeneously distributed ZrO
2 
precipitates during PBF-LB of the Nb521 alloy [200] . The oxygen con -
tent of the jet milled Nb521 powders in both studies was high 
(0.13 – 0.18 wt%) and was seen to increase after the PBF-LB process due 
to reactions with atmospheric impurities [199,200] .
5.1.2.1. Nb-silicide alloys. Other alloys applied in metal AM literature 
rely more heavily on the formation of secondary phases in the alloy, 
more specifically on the formation of Nb silicides. While different 
alloying elements such as Ti, Hf, Mo, Cr, Al, Zr and V are present in these 
alloys along with Si, the microstructure after PBF-LB and DED-LB 
generally consists of an Nb solid solution phase and different silicides. 
These silicides were found with DED-LB to primarily be the non- 
equilibrium γ -Nb
5
Si
3 
[201,202] , while Guo et al. found that by using 
PBF-LB both the α -Nb
5
Si
3
, β -Nb
5
Si
3 
and Nb
3
Si silicides formed in a 
highly complex and refined microstructure [203] . Generally, the mi -
crostructures of these alloys produced by PBF-LB experienced significant 
grain refinement compared to DED-LB, which is likely related to the 
higher cooling rates created by the PBF-LB process. Feitosa found that 
alloying with Al, V, Mo and Hf aided in suppressing the formation of 
Nb
3
Si and that the high cooling rates involved in the DED-LB process 
were the primary driving force for creating these non-equilibrium 
structures [201] . Li et al. found that by increasing the content of Zr in 
the alloy, the silicide changed from the hypoeutectic Nb
3
Si micro -
structure to a hypereutectic microstructure of γ -Nb
5
Si
3 
[204] . Alloying 
with Hf creates HfO
2 
precipitates through the reaction with oxygen 
impurities in the powder or the atmosphere [201,203] . At high Cr 
contents, Feitosa noted that increasing the scan speed generally creates a 
grain refinement [201] .
5.2. Densification
Due to the limited number of studies on Nb and Nb-alloys, the 
densification of these materials has not been thoroughly investigated. 
The studies that have investigated the densification of these materials 
have been focused on optimising the process parameters to achieve the 
highest possible density. Liu et al. noted that an insufficient energy 
density resulted in insufficient fusion and excessive porosity [194] , see 
Fig. 23 a. This was observed to be particularly sensitive to excessively 
high scan speeds, which resulted in a low temperature of the melt pool 
and a correspondingly narrow melt pool. This prevented sufficient 
spreading of the melt. This phenomenon also occurred at an insufficient 
laser power of excessive hatch spacing [194] . However, they also noted 
that excessive energy density led to a decline in densification as a 
consequence of molten pool instabilities and the formation of keyhole 
porosity [194] . Griemsmann et al. created a process map for PBF-LB of 
pure Nb and found that a range of process parameters was capable of 
producing parts with a relative density of more than 99.9 % [193] , see 
Fig. 23 b. This resulted in the build-up rate being improved from 
0.33 mm
3
/s to 1.63 mm
3
/s, which makes the PBF-LB process much 
more efficient [193] . Candela et al. noted that the scan strategy affects 
the achievable densification, where a smaller stripe width resulted in 
lower density [205] . Guo et al. used single tracks to evaluate the 
printability of an Nb-silicide alloy and noted that the balling phenom -
enon could generally be reduced by increasing the laser power [206] .
5.3. Cracking
Due to the generally ductile nature of Nb and its alloys and the DBTT 
of pure Nb of < -120 
◦
C, most studies do not experience issues with 
cracking. Mullin et al. observed shallow solidification cracks in C103 
under certain process parameter combinations, particularly at high scan 
speeds [207] . However, the Nb-silicides formed in the Si-containing 
alloys were brittle and resulted in cracking when produced by PBF-LB 
even with optimised process parameters [203] . The DBTT of these 
high-Si alloys can be as high as 1000 
◦
C [208,209] , which in combina -
tion with the rapid solidification and cooling of the PBF-LB process can 
result in cracking.
5.4. Mechanical properties
A wide range of hardness has been reported for pure Nb. Griems -
mann et al. reported a hardness of approximately 150 HV regardless of 
the applied parameters [193] . In contrast, Liu et al. recorded a much 
higher hardness of about 250 – 375 HV [194] . They noted that the 
highest hardness was found at intermediate energy inputs and specu -
lated that higher scan speeds and lower laser powers resulted in weaker 
Fig. 22. Microstructure of C103 produced by PBF-LB. A-e) Cellular dislocation structures observed via TEM. f) Elongated primary Nb grains observed via EBSD 
[195] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
21

## Page 22

residual stresses and more porosity, while excessively high laser powers 
or low scan speeds also decreased the hardness due to grain coarsening 
[194] . The differences between the two studies might be related to 
differences in purity and residual stress in the material. Hardness above 
300 HV was only recorded for specimens with an excessive oxygen 
content in the material. By alloying with Ti, Scheider-Maunoury et al. 
raised the hardness from 150 HV for pure Nb to 245 HV for a 1:1 Nb:Ti 
ratio [210]
2
. The C103 alloy was found to have a hardness of 190 HV in 
the as-built condition [196] . Nb-silicides are usually very hard, which 
explains the much higher hardness of 810 HV noted by Guo et al. when 
investigating the PBF-LB of an Nb-Si-Ti-Cr-Al-Hf alloy [203] .
Similarly, the strength of these alloys is also found to be dependent 
on alloy type and manufacturing conditions. Griemsmann et al. found 
that pure Nb produced by PBF-LB had a much higher strength and lower 
ductility compared to conventional wrought material. They related this 
effect to grain size and shape, while the higher oxygen content of the 
PBF-PB material was held responsible for the increased strength [193] . 
Liu et al. noted that the strength and elongation of pure Nb initially 
increased with increasing energy input and attributed this to improved 
densification of the component. Further increasing the energy input 
caused a dramatic decrease in strength and ductility due to balling and 
increased porosity [194] . They also noted that an increased oxygen 
content significantly increased the strength of pure Nb, but at a severe 
cost of ductility by reducing the elongation at fracture from 26 % to less 
than 2 %, see Fig. 24 . Awasthi et al. found an increased strength and 
reduced ductility of C103 produced by PBF-LB compared to wrought 
C103, which was attributed to the high dislocation density and cell 
structure formed during PBF-LB [195] . Similar observations were made 
by Mireles et al., however they attributed this strength/ductility 
trade-off to grain refinement in the PBF-LB process [196] . Chen et al. 
observed excellent mechanical properties of an Nb521 alloy produced 
by PBF-LB and attributed this to a combined transformation induced 
plasticity (TRIP) and twinning induced plasticity (TWIP) effect of the 
fine ZrO
2 
precipitates formed during the PBF-LB process [200] . Li et al. 
found that the addition of 5 at% of Zr to a Nb-Si-Ti alloy manufactured 
by DED-LB improved the fracture toughness from 11 Mpa.m
1/2 
to 15 
Mpa.m
1/2
, which was stable up to 15 at% Zr [204] .
5.5. Suggested areas of research
Due to the highly limited amount of research on pure Nb and Nb- 
based alloys produced by laser-based AM, the field needs to be 
expanded. More research needs to be conducted into the connections 
between process parameters, densification, microstructure, and 
properties for both pure Nb and Nb-alloys. As all studies employ an Ar 
shielding gas, replacing this with N, H or a combination hereof may 
provide benefits in terms of reducing interstitial pickup, cracking or 
achievable density. The feedstock purity of Nb and Nb-based alloys will 
also have to become a topic of research moving forward as these ma -
terials are sensitive to impurity concentration and prone to grain 
boundary embrittlement. Furthermore, the number of commercially 
available Nb-alloys is very small which is reflected in the limited number 
of Nb-alloy powders available for AM. Therefore, alloys that previously 
fell out of favour due to machining difficulties could be reinvestigated 
using AM, such as the so-called third phase Nb-alloys AS30, B77, 
C132M, D41 and similar [11] . Lastly, Nb-silicides seem to be a prom -
ising class of alloys but due to their inherent brittleness, they might be 
more suited to other manufacturing methods such as PBF-EB or BJT.
6. Refractory high entropy alloys
Different definitions of high entropy alloys (HEAs) can be made, but 
this review considers HEAs as alloys containing four or more alloying 
elements of equimolar or near equimolar composition. For refractory 
HEAs specifically, at least two elements will be from the refractory 
category (W, Mo, Ta, Nb, Re). Research on AM of refractory HEAs 
comprised about 14 % of refractory metals employed in AM. About 53 % 
of studies investigated the PBF-LB process, while 32 % considered DED- 
LB. The remaining studies were split between PBF-EB (3 studies, 11 %) 
and DED-Arc (1 study, 4 %), see Fig. 25 . Almost all studies employ a 
powder mixing strategy (91 %) as opposed to pre-alloyed powders. No 
studies investigated all five refractory elements (W, Mo, Ta, Nb, Re) in a 
HEA, however the majority of studies (39 %) involve four of the five 
elements (all except Re) or three elements (46 %). Only 15 % of the 
refractory HEAs produced by AM employ just two refractory elements.
6.1. Microstructure
The microstructure of each refractory HEA will depend on the exact 
alloying elements but most of them present a single-phase BCC solid 
solution [211 – 214] . The primary grains are elongated along or at an 
angle to the build direction.
For a NbMoTaW alloy, Zhang et al. observed microscale fluctuations 
of Nb and Mo in the microstructure along with a loss of Mo and Nb from 
the nominal composition [215] . A cellular structure was observed inside 
the elongated primary grains [215] . In a NbMoTaWV alloy, Huber et al. 
observed strong segregation of V and weak segregations of Mo and Nb to 
the cell walls, while W and Ta segregated to the cell interiors [212] . The 
refinement of the cell structure was found to be dependent on the energy 
input into the material [212,214] . The Ta and W were unevenly 
distributed in the microstructure, likely due to differing melting tem -
peratures and uneven powder mixing [213] . A high dislocation density 
Fig. 23. Relations between processing parameters and achievable relative density for pure Nb produced by PBF-LB. a) At a fixed scan speed the density improves 
with increasing laser power to a maximum of around 350 W [194] . Reproduced with permission from Elsevier. b) Process map for pure Nb with varying scan speeds 
and laser powers [193] . Reproduced under Creative Commons CC BY 4.0 licence.
2
Note that these measurements were done using nano-indentation so direct 
comparison to microhardness-indentation may not be applicable.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
22

## Page 23

was observed along with the cell structure [213,214] . A similar cell 
structure was observed by Liu et al. in a TiZrNbTaMo alloy with Ti 
primarily segregating to the cell walls, while Ta and Nb were segregated 
to the cell interiors [216] . Xu et al. observed grain refinement during 
PBF-LB when adding C to the NbMoTaW HEA along with niobium car -
bides at grain boundaries hindering grain growth [217] . Zhang et al. 
investigated Ti and Ni additions to a NbMoTa HEA and observed grain 
refinement by the addition of Ni, or Ti and Ni simultaneously as Ni 
expanded the solidification temperature range as seen in Fig. 26 [218] . 
In the NbMoTaTi alloy, α -Ti with Nb, Mo and Ta in solid solution was 
formed at the GBs, while the NbMoTaNi alloy possessed two GB phases: 
BCC Nb
2
Mo
0.5
Ta
3
Ni
4 
and face-centred cubic (FCC) Ta
4
Nb
3
Ni
3 
[218] . 
The NbMoTaTiNi alloy contained multiple GB phases: monoclinic Ni
3
Ta 
(Nb,Mo,Ti), FCC (TiNi)
3
Mo(Nb,Ta)
2 
and BCC β -Ti(Nb,Mo,Ta) [218] . 
Zhang et al. also investigated a NbMoTaTiNi HEA and found a dendritic 
BCC as-built microstructure with a phase rich in Ti and Ni with a B2 
crystal structure at the GBs [219] . Furthermore, FCC Ti
2
Ni was found to 
be distributed in the bulk, while the trigonal X
B 
phase was distributed 
around the matrix and contained about 40 at% Ni [219] . Chen et al. also 
observed a dual-phase microstructure in an NbMoTi medium entropy 
alloy (MEA) with small amounts of FCC phase in a BCC matrix [220] .
Mooraj et al. compared the microstructure of a TiZrNbTa alloy pro -
duced by PBF-LB to the same alloy produced by arc melting and found 
significant grain refinement and increased dislocation density due to the 
high cooling rate of the PBF-LB process [221] . Wang et al. investigated a 
NbTaTi alloy with different Mo additions and found them all to consist 
of a single dendritic BCC phase, where the dendrites were enriched in 
the low melting temperature element Ti [222] . No crystallographic 
texture was observed [222] . A similar lack of texture and segregation of 
Ti to the dendrite arm were observed by Liu et al. for a WMoTaTi alloy, 
where the HCP α -Ti phase formed [223] . Ye et al. investigated a CoCr -
MoNbTi alloy reinforced with carbon nanotubes and observed a den -
dritic microstructure consisting of a BCC phase rich in Mo and Nb, an 
HCP phase rich in Co and Cr and small TiC particles [224] . The addition 
of carbon nanotubes also caused significant grain refinement [224] .
6.1.1. Laser directed energy deposition processing
Less studies have been done on refractory HEAs produced by DED-LB 
as this process is less widespread. Dobbelstein et al. investigated a 
TiZrNbTa HEA produced by DED-LB with differing Zr and Nb contents 
and found that the Nb-rich composition produced a single BCC phase, 
while the Zr-rich composition produced a secondary Ta-rich BCC phase 
at the GBs [225] . A dendritic microstructure was observed with 
Fig. 24. The mechanical properties of pure Nb with different levels of oxygen contamination as a function of the applied PBF-LB process parameters. A) Fixed scan 
speed. b) Fixed laser power. c-d) Different oxygen levels [194] . Reproduced with permission from Elsevier.
Fig. 25. Statistic distribution of AM technologies within the research on re -
fractory HEAs produced by additive manufacturing.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
23

## Page 24

enrichment of the dendrite arms with Nb and Ta, the inter-dendritic 
regions were enriched in Ti and Zr [226] . Dobbelstein et al. observed 
that the higher melting temperature elements of a TiZrNbHfTa alloy 
needed to be added in quantities larger than equi-atomic as these par -
ticles would bounce off the component and not be incorporated in the 
melt pool [227] . In this alloy, the dendrites were enriched in Ta, while 
the inter-dendritic regions were enriched in Ti, Zr and Hf [226] . Melia 
et al. investigated the NbMoTaW alloy with DED-LB and found that the 
columnar grains at the bottom of the specimen gradually transitioned to 
fine equiaxed grains with increasing build height [228] . For specimens 
graded from the HEA to pure W or Nb, the grains were observed to 
transition back into coarse columnar grains as the pure composition was 
approached [228] . A fine cellular structure with segregation of Nb and 
Mo to the cell walls was also observed for the DED-LB process 
[228 – 230] . Similar segregations were observed for the NbTaWV alloy 
[230] and the NbMoTaTiHf alloy [231] . The microstructure was seen to 
depend on the location within the component due to differing heat flow 
directions as the scan vector changes [231] . While many similar 
microstructural features are observed when processing these refractory 
HEAs by either PBF-LB or DED-LB, the DED-LB process usually created a 
coarser cell structure with a higher degree of elemental segregation, 
which is likely related to the slower cooling of this process.
6.2. Densification
The densification of materials produced by AM is of utmost impor -
tance, so several studies have investigated the different parameters that 
may affect the achievable density of refractory HEAs produced by DED- 
LB and PBF-LB. Liu et al. observed that the density of PBF-LB WMoTaTi 
improved with increasing energy density by a combined use of high laser 
power, low scan speed and low hatch spacing, which was attributed to 
the need for a high melt pool temperature due to the high melting 
temperatures of the refractory elements in this alloy [223] . Similarly, Gu 
et al. observed balling in an NbMoTaWV alloy produced by PBF-LB and 
increased porosity at excessive laser speeds due to increased surface 
tension of the melt and a lower liquid lifetime [214] . Ye et al. noted that 
the density of a CoCrMoNbTi alloy produced by DED-LB increased with 
increasing laser power due to an increased temperature of the melt pool, 
while excessive laser power decreased the achievable density by over -
heating of the melt pool and evaporation of low melting temperature 
elements [224] . Wang et al. noted that severe balling occurred and 
associated LOF porosity increased with increasing Mo content during 
PBF-LB of NbTaTiMo due to more unmelted particles and a discontinuity 
of the molten pool [222] , see Fig. 27 .
Fig. 26. Microstructure refinement as an effect of Ti and Ni additions to a NbMoTa refractory HEA observed via EBSD. A) NbMoTa, b) NbMoTaTi, c) NbMoTaNi, d) 
NbMoTaTiNi. e) Grain sizes for different refractory HEAs [218] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
24

## Page 25

6.3. Cracking
6.3.1. Effect of process parameters and characteristics on cracking
As with most refractory alloys produced by AM, there is a risk of 
HEAs cracking during the process due to the development of large re -
sidual stresses. Moorehead et al. observed cracking between the build 
plate and specimen due to large thermal stresses in NbMoTaW produced 
by DED-LB [229] . Zhang et al. utilised simulation of the temperature 
distribution and thermal stress formation to optimise the PBF-LB process 
parameters for an NbMoTaW alloy to eliminate cracking and warping 
during build [211] . Gu et al. generally observed crack reduction and 
shortening when the energy input was increased by reducing the scan 
speed [214] . Liu et al. also observed a crack reduction with increasing 
energy input by increasing the laser power [223] . On the contrary, 
Huber et al. found increased cracking with increased energy density and 
somewhat related this to differences in thermal gradients and stress 
states as different laser power, scan speed and hatch spacing were 
employed between the two parameter sets [212] . Li et al. had similar 
observations on NbMoTa produced by DED-LB, where low energy input 
(by increasing laser power or increasing scan speed) resulted in less 
cracking but more unmelted particles [232] . Ye et al. noted that 
excessively high energy inputs resulted in cracking due to damage to the 
carbon nanotube structure in a CoCrMoNbTi-C alloy produced by 
DED-LB, which in turn acted as crack nucleation sites [224] .
6.3.2. Effect of alloying on cracking
Due to the complex chemical nature of HEAs, several studies have 
focused on varying the chemical composition of the alloy to suppress the 
cracking phenomenon during PBF-LB and DED-LB. Zhang et al. 
increased the crack resistance of the NbMoTa refractory HEA by alloying 
with Ni and Ti, where the simultaneous addition of both elements 
effectively suppressed cracking by improving the crack-filling ability of 
the molten metal due to an increased melting range [218] . Furthermore, 
these alloying elements increased the formability of the alloy [218,219] . 
Xu et al. showed that cracking in an NbMoTaW alloy could be sup -
pressed by C addition as O segregation at the GBs and associated 
embrittlement were reduced [217] . Wang et al. observed that cracking 
increased with increasing Mo content in a NbTaTiMo HEA due to 
reduced ductility and suppression of the more ductile HCP phase [222] . 
Melia et al. produced a graded NbMoTaW alloy by DED-LB and observed 
less cracking in the Nb-rich part of the specimen due to a higher intrinsic 
ductility [228] . Mullin et al. investigated a MoNbTaTiHf alloy produced 
by PBF-LB and showed that cracking reduced with increasing Ta content 
as the ductility of the material increased [207] .
6.4. Mechanical properties
6.4.1. Effect of process parameters and characteristics on mechanical 
properties
The mechanical properties of each HEA will heavily depend on its 
composition due to the wide compositional space for these alloys along 
with the process parameters applied during the manufacturing process. 
Liu et al. generally noted that the cell structure formed in a TiZrNbTaMo 
alloy produced by PBF-LB provided a synergy of good yield strength and 
ductility due to the cell walls initially impeding dislocation motion and 
later absorbing and storing dislocations [216] . Zhang et al. noted that 
the NbMoTaW alloy produced by PBF-LB had a significantly higher 
hardness than the cast zalloy due to grain refinement [215] . Huber et al. 
noted that the hardness increased with the refinement of the cell 
structure by changing process parameters [212] . The compressive 
strength of an NbMoTaWV alloy produced by PBF-LB was higher than in 
conventional manufacturing due to the refined cell structure [213] . 
Similar observations were made by Gu et al. as they noted that the 
compressive strength decreased with increasing scan speed due to an 
increased crack density and size [214] , see Fig. 28 . The TiZrNbTa alloy 
produced by PBF-LB also showed improved strength over arc melting, 
which was attributed to a combination of grain refinement and 
increased dislocation density [221] . Generally, the hardness was found 
to be higher for the same alloy produced by PBF-LB compared to DED-LB 
due to grain refinement and higher residual stress observed in compo -
nents manufactured by PBF-LB [211,215,228] .
6.4.2. Effect of alloying on mechanical properties
As HEAs contain multiple principal alloying elements, the ratios 
between these elements may determine the achievable mechanical 
properties. Therefore, several studies have investigated how tailoring 
the chemical composition of additional alloying elements influenced the 
mechanical performance of these alloys. Melia et al. noted that the 
hardness generally increased with increasing entropy of the system as 
solid solution strengthening is the primary strengthening mechanism for 
the NbMoTaW HEA produced by DED-LB [228] . Dobbelstein noted that 
the Nb-rich end of a graded TiZrNbTa alloy was much softer than the 
Zr-rich due to precipitation strengthening at this location [225] . The 
hardness was observed by Xu et al. to increase with C addition due to 
grain refinement and carbide precipitation [217] . Zhang et al. observed 
a significant hardness increase upon the addition of Ni and Ti simulta -
neously to an NbMoTa alloy due to grain refinement. The strength at 
Fig. 27. Achievable relative density of a NbTaTi HEA as a function of Mo 
content [222] . Reproduced with permission from Elsevier.
Fig. 28. Compressive stress-strain curves for NbMoTaWV produced by PBF-LB 
at different scan speeds and associated energy densities [214] . Reproduced with 
permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
25

## Page 26

room temperature was improved by the Ti and Ni combined addition 
due to efficient crack suppression [218] . However, the lower melting 
temperature of the added alloying elements (compared to the refractory 
elements in the alloy) resulted in a rapidly decreasing strength at 
elevated temperatures [218] . Wang et al. observed an increasing 
strength and hardness with increasing Mo content in a NbTaTi alloy due 
to solid solution strengthening, with excessively high Mo addition 
leading to insufficient compressive ductility and deformation due to 
lower density and Mo inhibiting the transformation of metastable BCC to 
HCP upon deformation [222] . Similarly, Zhang et al. showed a gradual 
decrease in room temperature plasticity and an increase in yield strength 
with increasing Mo content in a NbTaTiNi alloy due to grain refinement 
and solid solution strengthening [233] . Liu et al. attributed the observed 
high hardness of a WMoTaTi alloy produced by PBF-LB to grain 
refinement and formation of a secondary α -Ti phase [223] . Ye et al. also 
attributed the high hardness and strength of a CoCrMoNbTi with carbon 
nanotubes to grain refinement and precipitation of TiC particles [224] .
6.5. Suggested areas of research
Due to the complex nature of HEAs and their multiple principal el -
ements, there are an almost infinite amount of possible alloying com -
binations. Due to the complexity of these high entropy alloying systems, 
thermodynamic modelling as a screening tool for compositional com -
binations may become an important topic of research. These modelling 
tools can potentially reduce the variables during alloys development and 
help select the most promising candidate compositions. Most of the 
current studies on AM of refractory HEAs have been focused on mixed 
elemental powders, which can create challenges in terms of chemical 
heterogeneity, so it is suggested to compare properties of components 
from mixed powders to components produced from pre-alloyed pow -
ders. All studies across PBF-LB and DED-LB have used Ar as the shielding 
gas, so it becomes important to understand how the purity of this gas 
influences the oxygen uptake during the build. As many of the refractory 
HEAs suffer from cracking, the effect of different shielding gases may 
become a topic of interest. Furthermore, PBF-EB has shown some success 
in suppressing the cracking of refractory HEAs [234 – 236] , but the 
research into this technology is still limited.
7. Post-processing
Thermal post-processing of additively manufactured metals, here -
under also refractory metals, has generally fallen into three main cate -
gories: low temperature stress relief, high temperature annealing and 
hot isostatic pressing (HIP).
The stress relief treatment can be important or imperative for addi -
tively manufactured metals to avoid cracking or warping when 
removing components from the build plate [80,195,200] . Ideally, the 
stress relief treatment should not significantly alter the microstructure 
beyond reducing the residual stress and dislocation density of the ma -
terial. Ren et al. employed a stress relief treatment of pure W produced 
by PBF-LB at 1100 
◦
C, which provided no observable microstructural 
changes [107] . Stress relief was applied by Oehlerking et al. at 1000 
◦
C 
to safely remove pure Mo components from the build plate after PBF-LB 
[134] , while Kaserer et al. stress relieved the parts simultaneously with 
the PBF-LB build process by heating the build plate to 1200 
◦
C for 1 h to 
reduce cracking [138] . Several studies employed stress relief heat 
treatments to pure Ta to reduce residual stresses [175,177,180,184,186, 
187] .
High temperature annealing of refractory alloys produced by AM has 
not been consistently studied across the different systems. Generally, 
these alloys experienced grain growth and associated reduction in their 
strength and hardness at these high annealing temperatures. Yamamoto 
et al. showed that the microstructure of pure W produced by PBF-LB 
remained unchanged during heat treatment at 1300 
◦
C, while 1900 
◦
C 
led to grain growth and a 10 % hardness reduction [111] . Similarly, Lian 
et al. showed that annealing of pure Ta increased the elongation at 
fracture, reduced the tensile strength and transitioned to ductile fracture 
mode due to grain growth, while the elongated grain shape remained 
[162] . On the contrary, Sungail et al. showed that high temperature 
annealing (1700 – 2000 
◦
C) of pure Ta produced by PBF-LB resulted in 
grain growth and increased ductility without reduction in the yield 
strength and attributed this to redistribution of grain boundary oxygen 
to grain interiors [166] . Schwanekamp et al. observed no microstruc -
tural changes during heat treatment of a WHA at 1100 
◦
C, while a 
treatment at 1500 
◦
C caused grain growth [92] . Fichtner et al. found that 
significant grain growth and microstructure coarsening occurred during 
annealing of a Mo-Si-B alloy at 1600 
◦
C, even though the overall phase 
composition of the alloy remained the same [142] .
Depending on the alloy and heat treatment temperature and char -
acteristics, more distinct changes to the microstructure may also occur. 
Ivekovi ´c et al. showed that spherodised W grains formed during 
annealing of a WHA at 1500 
◦
C, which led to an improved uniaxial 
tensile elongation (from < 1 % elongation to > 10 %), while maintaining 
a high strength, see Fig. 29 [91] . Zhou et al. designed a triple heat 
treatment for pure Ta produced by PBF-LB, which resulted in an equi -
axed grain structure. Some dislocation cell structures remained, which 
resulted in a significant increase in ductility while maintaining a high 
strength [163] . Lian et al. noted a change in crystallographic texture 
during high temperature annealing of pure Ta at 1200 – 1600 
◦
C [162] . 
During high temperature (900 – 1500 
◦
C) vacuum annealing of the C103 
alloy produced by PBF-LB, Fietek et al. observed grain growth and 
coarsening of Hf-oxides at the grain boundaries [237] .
High temperature annealing of Nb-silicide alloys was observed by 
Guo et al. [203] and Feitosa [201] to stabilise equilibrium Nb-Si phases, 
cause microstructure coarsening and homogenise chemical and micro -
structural variations. Zhang et al. observed that the fine dendritic 
microstructure in a NbMoTaTiNi alloy produced by PBF-LB was gradu -
ally removed with increasing annealing temperature, where annealing 
at 1300 
◦
C resulted in a dendrite-free microstructure with the X
B 
and 
Ti
2
Ni phases precipitating during cooling, see Fig. 30 [219] . The 
strength and hardness of the alloy were seen to decrease with increasing 
annealing temperature due to grain growth [219] . Ozalp et al. observed 
the formation of oxides and porosities at GBs during heat treatment of a 
NbMoTaTiHf alloy produced by DED-LB [231] . Extremely high tem -
perature annealing in hydrogen at 2400 
◦
C of a W-Re alloy was shown to 
heal internal microcracks from the PBF-LB process and reduce the ox -
ygen content of the material due to the reducing nature of the hydrogen 
atmosphere, which in turn improved its strength and ductility, as the 
reduction of oxygen content and defect concentration was more im -
pactful than grain size [73] .
HIP has been a popular post-processing method for improving the 
density of additively manufactured materials by closing residual 
porosity and healing internal microcracks [238] . Chen et al. noted that 
the HIP treatment of pure W resulted in significant grain growth and 
reduction of dislocation density while bridging microcracks [239] . 
Eckley et al. showed that the HIP treatment of a W-Re alloy caused grain 
growth, an increased density, partial crack bridging and reduced oxygen 
content [73] . Similar observations of grain growth and particle coars -
ening were made for HIP-treated Nb-based C103 alloy by Mireles et al. 
[196] . The high temperature of the HIP process was observed to cause 
recrystallisation and a reduction of texture strength for both the C103 
[237] and Nb521 [199] Nb-based alloys. Analogous to the high tem -
perature annealing, the HIP treatment of Nb-silicide alloys resulted in a 
transformation of the non-equilibrium microstructure produced by AM 
into a microstructure resembling that obtained at equilibrium [201] . 
Guan et al. noted that the addition of La
2
O
3 
to pure Mo during the 
PBF-LB process improved the efficacy of subsequent HIP treatment in 
terms of densification of the material [147] .
Motschmann et al. employed a solid state gettering technique by 
deposition of pure Ti on pure Nb produced by PBF-LB to improve its 
purity and improve its superconductive properties [240,241] .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
26

## Page 27

8. Conclusions
AM of refractory metals and their alloys has been a consistently 
increasing field of research accelerating rapidly from 2015 to 2019 with 
a fairly consistent research output since then. Laser-based AM has been 
by far the most dominant energy source due to its availability and 
flexibility. While many different alloy systems and processing parameter 
combinations have been investigated the following conclusions can be 
drawn: 
• Cracking has been the biggest challenge for refractory metals with a 
high DBTT and inherent brittleness (W and Mo). While many studies 
have focused on improving the crack propensity of these pure ma -
terials through optimisation of the process characteristics (energy 
density, scan strategy, substrate pre-heating), they have been only 
partially successful. The crack density and length could be reduced, 
however crack-free W and Mo could not be achieved by using PBF-LB 
or DED-LB. Powder characteristics such as particle size and impurity 
level had some effect on the crack susceptibility.
• Alloying the brittle W and Mo appeared to be a more successful 
strategy for producing crack-free components by PBF-LB and DED- 
LB. Especially additions of Nb, Ta and ZrC to W were promising, 
while C additions to Mo helped the formation of a cellular micro -
structure and effectively suppressed cracking.
• WHA appeared to be a promising compromise between the high 
strength and hardness of W and the ductility and crack resistance of 
the Fe/Ni/Cu-containing matrix phase. It was found to be important 
to ensure a sufficient fraction of the matrix phase to prevent the 
connection of the W particles and sufficient energy to ensure partial 
melting of the W particles without excessive evaporation of the 
matrix elements.
• While several studies investigated the connection between process -
ing parameters and densification, there is no clear consensus on the 
effects of individual parameters, energy densities or scan strategies. 
It is however clear that the processing needs to be optimised to 
reduce porosity for each refractory metal and their alloys.
• Ta has almost solely been investigated as a pure material with a 
specific focus on porous lattice structures for implant applications. 
Ta produced by PBF-LB, or DED-LB generally exhibit good density 
and a fine-grained microstructure.
• The studies on Nb have either been focused on pure Nb, conven -
tionally available solid solution alloys or Nb-silicide alloys. The solid 
solution alloys generally showed a good combination of strength and 
ductility, while the silicide-based alloys showed an extremely high 
strength but also an associated brittleness and crack susceptibility.
Fig. 29. Microstructure and performance of a WHA after being subjected to a 1500 
◦
C heat treatment. a) Microstructure showing spherodised W grains, b) elemental 
distribution after heat treatment and c) tensile stress-strain curves for the as–built and heat treated conditions [91] . Reproduced with permission from Elsevier.
Fig. 30. Microstructure evolution and stabilisation of equilibrium phases in a NbMoTaTiNi HEA alloy produced by PBF-LB. a) 600 
◦
C, b) 800 
◦
C, c) 1000 
◦
C, d) 1100 
◦
C, e) 1200 
◦
C and f) 1300 
◦
C [219] . Reproduced with permission from Elsevier.
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
27

## Page 28

• Many different elemental combinations of refractory HEAs have been 
studied containing between two and four refractory elements. The 
elements used for these refractory HEAs consisted of W, Mo, Ta, Nb, 
Ti, Ni, Zr, Hf, V, Al, Cr, Co, Sn and C. DED-LB constituted a larger 
fraction of studies compared to the other refractory alloy systems due 
to the ease of elemental powder mixing using this method.
• The strength of refractory metals and alloys produced by AM was 
generally found to be higher than that of their conventionally man -
ufactured counterparts due to a combination of microstructure 
refinement, residual stress and precipitation. The mechanical prop -
erties were found to be sensitive to achieved levels of density and 
oxygen impurity levels. Purification of grain boundaries was found to 
be important for the mechanical properties and in particular for the 
ductility of the material. Grain refinement and oxygen trapping by 
the addition of Ta, Nb, Re, ZrC, C, Hf or Ti were both effective grain 
boundary purification methods.
• Feedstock purity and atmospheric reactions and oxygen, nitrogen 
and/or hydrogen pickup during the additive manufacturing process 
is a topic that still requires investigation due to the sensitive inter -
play between oxygen content and the ductile-to-brittle transition of 
these refractory alloys. Furthermore, the formation of strengthening 
oxides may provide a promising route for developing alloys that can 
handle the impurity contamination that may occur during powder 
production or storage along with the additive manufacturing 
process.
CRediT authorship contribution statement
Cecilie Vase Funch: Writing – original draft, Visualization, Meth -
odology, Investigation, Formal analysis, Conceptualization. Gw ´ena ¨elle 
Proust: Writing – review & editing, Supervision, Funding acquisition, 
Conceptualization.
Declaration of Competing Interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Data Availability
No data was used for the research described in the article.
Acknowledgement
The authors thank the Digital Science Initiative (DSI) within the 
Faculty of Engineering at the University of Sydney for the financial 
support by the DSI Pilot Project Funding Scheme (grant number 
M1DSIAMM) that facilitated their research project on the additive 
manufacturing of refractory alloys. The authors also thank the technical 
staff at the Sydney Manufacturing Hub, a core research facility at the 
University of Sydney, for the fruitful discussions surrounding AM of 
refractory alloys.
Appendix A. Supporting information
Supplementary data associated with this article can be found in the 
online version at doi:10.1016/j.addma.2024.104464 .
References
[1] V.V. Satya Prasad, R.G. Baligidad, A.A. Gokhale, Niobium and other high 
temperature refractory metals for aerospace applications, Aerosp. Mater. Mater. 
Technol. (2017) 267 – 288 .
[2] L.L. Snead, et al., Refractory alloys: vanadium, niobium, molybdenum, Tungsten, 
Struct. Alloy. Nucl. Energy Appl. (2019) 585 – 640 .
[3] H. Warlimont, W. Martienssen (Eds.), Springer Handbook of Materials Data, 
2018 .
[4] Y. Yu, et al., Ultra-high purity tungsten and its applications, Int. J. Refract. Met. 
Hard Mater. 53 (2015) 98 – 103 .
[5] H. Walser, J.A.J. Shields, Traditional and emerging applications of molybdenum 
metal and its alloys, IMOA (2017) .
[6] F. Mayta-Tovalino, et al., Uses and applications of tantalum in oral implantology: 
a literature review, J. Int. Oral. Health 13 (4) (2021) .
[7] V.K. Balla, et al., Tantalum - a bioactive material for implants, Jom 62 (7) (2010) 
61 – 64 .
[8] E.E. Nikishina, D.V. Drobot, E.N. Lebedeva, Niobium and tantalum: State of the 
world market, fields of application, and raw sources. Part I, Russ. J. Non-Ferr. 
Met. 54 (6) (2014) 446 – 452 .
[9] P. Kumar, High purity niobium for superconducting applications, J. Less- 
Common Met. 139 (1988) 149 – 158 .
[10] A.D. Dobrza ´nska-Danikiewicz, W. Wolany, A rhenium review – from discovery to 
novel applications, Arch. Mater. Sci. Eng. 82 (2) (2016) 70 – 78 .
[11] Syre, R., Handbook on the properties of niobium, molybdenum, tantalum, 
tungsten and some of their alloys. 1965, North Atlantic Treaty Organization.
[12] J.B. Lambert, Refractory Metals and Alloys. ASM Handbook, Volume 2: Properties 
and Selection: Nonferrous Alloys and Special-Purpose Materials, ASM Handbook, 
1990, pp. 557 – 585 .
[13] I.V. Savchenko, S.V. Stankus, Thermal conductivity and thermal diffusivity of 
tantalum in the temperature range from 293 to 1800 K, Thermophys. Aeromech. 
15 (2008) 679 – 682 .
[14] Koechlin, F. and B. Bonin. Parametisation iof the niobium thermal conductivity in 
the superconductive state. in Proceedings of the 1995 Workshop on RF 
Superconductivity. 1995. Gif-sur-Yvette, France.
[15] L. Hu, B.D. Wirth, D. Maroudas, Thermal conductivity of tungsten: effects of 
plasma-related structural defects from molecular-dynamics simulations, Appl. 
Phys. Lett. 111 (8) (2017) .
[16] V. Piotter, et al., Development of a powder metallurgy process for tungsten 
components, Fusion Eng. Des. 83 (10-12) (2008) 1517 – 1520 .
[17] S. Antusch, et al., Two component tungsten powder injection molding – An 
effective mass production process, J. Nucl. Mater. 447 (1-3) (2014) 314 – 317 .
[18] Q. Zhu, et al., Research Status and Progress of Welding Technologies for 
Molybdenum and Molybdenum Alloys, Metals 10 (2) (2020) .
[19] J.L. Ham, An Introduction to Arc-Cast Molybdenum and Its Alloys, Trans. ASME 
(1951) 723 – 731 .
[20] N.R. Philips, M. Carl, N.J. Cunningham, New opportunities in refractory alloys, 
Metall. Mater. Trans. A 51 (7) (2020) 3299 – 3310 .
[21] Aerospace materials and material technologies, ed. N. Eswara Prasad and R.J.H. 
Wanhill. Vol. Volume 1: Aerospace Materials. 2017: Springer. .
[22] J. Hebda, Niobium Alloy. High. Temp. Appl. (2001) .
[23] V.V. Popov, et al., Powder bed fusion additive manufacturing using critical raw 
materials: a review, Materials 14 (4) (2021) .
[24] H. Sahasrabudhe, S. Bose, A. Bandyopadhyay, Laser-based additive 
manufacturing processes, Adv. Laser Mater. Process. (2018) 507 – 539 .
[25] Milewski, J.O., Additive manufacturing of metals. Springer. Vol. 258. 2017: 
Springer series in materials science.
[26] D. Herzog, et al., Additive manufacturing of metals, Acta Mater. 117 (2016) 
371 – 392 .
[27] M. Schmidt, et al., Laser based additive manufacturing in industry and academia, 
CIRP Ann. 66 (2) (2017) 561 – 583 .
[28] T. DebRoy, et al., Additive manufacturing of metallic components – Process, 
structure and properties, Prog. Mater. Sci. 92 (2018) 112 – 224 .
[29] T.F. Babuska, et al., Comparison of powder bed fusion and directed energy 
deposition for tailoring mechanical properties of traditionally brittle alloys, 
Manuf. Lett. 28 (2021) 30 – 34 .
[30] M.C. Brennan, J.S. Keist, T.A. Palmer, Defects in metal additive manufacturing 
processes, J. Mater. Eng. Perform. 30 (7) (2021) 4808 – 4818 .
[31] A. Sola, A. Nouri, Microstructural porosity in additive manufacturing: The 
formation and detection of pores in metal parts fabricated by powder bed fusion, 
J. Adv. Manuf. Process. 1 (3) (2019) .
[32] Z.-C. Fang, et al., Review on residual stress in selective laser melting additive 
manufacturing of alloy parts, Opt. Laser Technol. (2020) 129 .
[33] C. Pauzon, et al., Effect of argon and nitrogen atmospheres on the properties of 
stainless steel 316 L parts produced by laser-powder bed fusion. Mater. Des. 
(2019) 179 .
[34] H. Amano, T. Ishimoto, T. Nakano, Review — importance of atmospheric gas 
selection in metal additive manufacturing: effects on spatter, microstructure, and 
mechanical properties, Mater. Trans. 64 (1) (2023) 2 – 9 .
[35] T. Mukherjee, et al., Printability of alloys for additive manufacturing, Sci. Rep. 6 
(2016) 19717 .
[36] L. Johnson, et al., Assessing printability maps in additive manufacturing of metal 
alloys, Acta Mater. 176 (2019) 199 – 210 .
[37] A. Talignani, et al., A review on additive manufacturing of refractory tungsten 
and tungsten alloys, Addit. Manuf. 58 (2022) .
[38] P. Morcos, et al., Review: additive manufacturing of pure tungsten and tungsten- 
based alloys, J. Mater. Sci. 57 (21) (2022) 9769 – 9806 .
[39] A. Wall, M.J. Benoit, A review of existing solidification crack tests and analysis of 
their transferability to additive manufacturing, J. Mater. Process. Technol. 320 
(2023) .
[40] C. Ren, et al., Methods for improving ductility of tungsten - a review, Int. J. 
Refract. Met. Hard Mater. 75 (2018) 170 – 183 .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
28

## Page 29

[41] M.H. Scott, P.M. Knowlson, The welding and brazing of the refractory metals 
niobium, tantalum, molybdenum and tungsten — a review, J. Less-Common Met. 
5 (1963) 205 – 244 .
[42] M. Zhong, et al., Laser direct manufacturing of tungsten nickel collimation 
component, J. Mater. Process. Technol. 147 (2) (2004) 167 – 173 .
[43] D. Gu, Y. Shen, Effects of processing parameters on consolidation and 
microstructure of W – Cu components by DMLS, J. Alloy. Compd. 473 (1-2) (2009) 
107 – 115 .
[44] R. Li, et al., Selective laser melting W – 10 wt% Cu composite powders, Int. J. Adv. 
Manuf. Technol. 48 (5-8) (2010) 597 – 605 .
[45] D. Zhang, et al., Research on process and microstructure formation of W-Ni-Fe 
alloy fabricated by selective laser melting, J. Mater. Eng. Perform. 20 (6) (2010) 
1049 – 1054 .
[46] R. Adams, Microstructural and Mechanical Property Characterization of Laser 
Additive Manufactured (LAM) Rhenium, Arizona State University, 2012, p. 92 .
[47] E. Martinez, et al., Microstructures of niobium components fabricated by electron 
beam melting, Metallogr., Microstruct., Anal. 2 (3) (2013) 183 – 189 .
[48] L. Thijs, et al., Strong morphological and crystallographic texture and resulting 
yield strength anisotropy in selective laser melted tantalum, Acta Mater. 61 (12) 
(2013) 4657 – 4668 .
[49] H. Qian, et al., Additively manufactured tantalum implants for repairing bone 
defects: a systematic review, Tissue Eng. Part B Rev. 27 (2) (2021) 166 – 180 .
[50] B. Liu, et al., A review on manufacturing pure refractory metals by selective laser 
melting, J. Mater. Eng. Perform. (2024) .
[51] A. Bose, et al., Traditional and additive manufacturing of a new Tungsten heavy 
alloy alternative, Int. J. Refract. Met. Hard Mater. 73 (2018) 22 – 28 .
[52] A. Bose, et al., Processing of tungsten heavy alloy by extrusion-based additive 
manufacturing, Int. J. Refract. Met. Hard Mater. 110 (2023) .
[53] Z. Hu, et al., Achieving high-performance pure tungsten by additive 
manufacturing: processing, microstructural evolution and mechanical properties, 
Int. J. Refract. Met. Hard Mater. 113 (2023) .
[54] G. Marinelli, et al., Development of Wire + Arc additive manufacture for the 
production of large-scale unalloyed tungsten components, Int. J. Refract. Met. 
Hard Mater. 82 (2019) 329 – 335 .
[55] Y. Shao, et al., Properties of TiC-reinforced Cu-W alloys prepared by wire arc 
additive manufacturing, Int. J. Refract. Met. Hard Mater. 115 (2023) .
[56] K. Deprez, et al., Rapid additive manufacturing of MR compatible multipinhole 
collimators with selective laser melting of tungsten powder, Med Phys. 40 (1) 
(2013) 012501 .
[57] M. Guo, et al., Selective laser melting additive manufacturing of pure tungsten: 
Role of volumetric energy density on densification, microstructure and 
mechanical properties, Int. J. Refract. Met. Hard Mater. 84 (2019) .
[58] Z. Xiong, et al., Selective Laser Melting and Remelting of Pure Tungsten, Adv. 
Eng. Mater. 22 (3) (2020) .
[59] S. Wen, et al., High-density tungsten fabricated by selective laser melting: 
densification, microstructure, mechanical and thermal performance, Opt. Laser 
Technol. 116 (2019) 128 – 138 .
[60] A.T. Sidambe, P. Fox, Interaction of pure tungsten powder with processing 
conditions in Selective Laser Melting, Adv. Powder Metall. abd Part. Mater. 2017 
(2017) 701 – 711 .
[61] A.T. Sidambe, et al., Effect of processing parameters on the densification, 
microstructure and crystallographic texture during the laser powder bed fusion of 
pure tungsten, Int. J. Refract. Met. Hard Mater. 78 (2019) 254 – 263 .
[62] D. Gu, et al., Effects of laser scanning strategies on selective laser melting of pure 
tungsten, Int. J. Extrem. Manuf. 2 (2) (2020) .
[63] D. Wang, et al., Dense pure tungsten fabricated by selective laser melting, Appl. 
Sci. 7 (4) (2017) .
[64] D. Zhang, Q. Cai, J. Liu, Formation of nanocrystalline tungsten by selective laser 
melting of tungsten powder, Mater. Manuf. Process. 27 (12) (2012) 1267 – 1270 .
[65] J. Li, et al., Laser powder bed fusion of pure tungsten: effects of process 
parameters on morphology, densification, microstructure, Materials 14 (2021) 
165 .
[66] J. Huang, et al., Selective laser melting of tungsten: Effects of hatch distance and 
point distance on pore formation, J. Manuf. Process. 61 (2021) 296 – 302 .
[67] D.-Z. Wang, et al., Cracking behavior in additively manufactured pure tungsten, 
Acta Metall. Sin. (Engl. Lett. ) 32 (1) (2019) 127 – 135 .
[68] R.A. Kemnitz, et al., Strengthening of additively manufactured tungsten by use of 
hydrogen in argon shielding gas, Int. J. Refract. Met. Hard Mater. 110 (2023) .
[69] J. Braun, et al., Molybdenum and tungsten manufactured by selective laser 
melting: Analysis of defect structure and solidification mechanisms, Int. J. 
Refract. Met. Hard Mater. 84 (2019) .
[70] X. Duan, et al., Effect of Ta on the microstructure and mechanical properties of W 
Ta alloys prepared by arc melting, Mater. Charact. 188 (2022) .
[71] Y.-H. Li, et al., Transition from ductilizing to hardening in tungsten: the 
dependence on rhenium distribution, Acta Mater. 181 (2019) 110 – 123 .
[72] L.-M. Luo, et al., Influence of Nb content on the microstructure and deuterium 
retention of W – Nb alloys, Fusion Eng. Des. 129 (2018) 120 – 129 .
[73] C.C. Eckley, et al., Selective laser melting of tungsten-rhenium alloys, Jom 73 (11) 
(2021) 3439 – 3450 .
[74] J. Chen, et al., A novel performance optimization study in additively 
manufactured tungsten-5 wt%Rhenium alloys reinforced with dilute carbon, Scr. 
Mater. 240 (2024) .
[75] K. Li, et al., Crack suppression via in-situ oxidation in additively manufactured W- 
Ta alloy, Mater. Lett. 263 (2020) .
[76] D. Wang, et al., Cracking in laser additively manufactured W: Initiation 
mechanism and a suppression approach by alloying, Mater. Des. 162 (2019) 
384 – 393 .
[77] J. Li, et al., Preparation, microstructure, and microhardness of selective laser- 
melted W – 3Ta sample, J. Mater. Res. 35 (15) (2020) 2016 – 2024 .
[78] J. Li, et al., Laser powder bed fusion in-situ alloying of refractory WTa alloy and 
its microstructure and mechanical properties, Addit. Manuf. 67 (2023) .
[79] A.R. LeSieur, C.C. Eckley, R.A. Kemnitz, Effects of niobium on the mechanical and 
oxidation properties of additively manufactured tungsten, Air Force Inst. 
Technol.: J. Alloy. Compd. (2023) .
[80] K. Li, et al., Effect of Ta addition on the fuzz formation of additively 
manufactured W-based materials, Nucl. Fusion 60 (6) (2020) .
[81] A. Ivekovi ´c, et al., Selective laser melting of tungsten and tungsten alloys, Int. J. 
Refract. Met. Hard Mater. 72 (2018) 27 – 32 .
[82] J. Xue, et al., Selective laser melting additive manufacturing of tungsten with 
niobium alloying: microstructure and suppression mechanism of microcracks, 
J. Alloy. Compd. 874 (2021) .
[83] K. Li, et al., Crack suppression in additively manufactured tungsten by 
introducing secondary-phase nanoparticles into the matrix, Int. J. Refract. Met. 
Hard Mater. 79 (2019) 158 – 163 .
[84] D. Gu, et al., Selective laser melting additive manufacturing of hard-to-process 
tungsten-based alloy parts with novel crystalline growth morphology and 
enhanced performance, J. Manuf. Sci. Eng. 138 (8) (2016) .
[85] M. Guo, et al., Laser powder bed fusion of a novel nano-modified tungsten alloy 
with refined microstructure and enhanced strength, Mater. Sci. Eng.: A 843 
(2022) .
[86] Z. Hu, et al., Pure tungsten and oxide dispersion strengthened tungsten 
manufactured by selective laser melting: microstructure and cracking mechanism, 
Addit. Manuf. 36 (2020) .
[87] Y. S ¸ ahin, Recent progress in processing of tungsten heavy alloys, J. Powder 
Technol. 2014 (2014) 1 – 22 .
[88] A. Panchal, T.K. Nandy, Effect of composition, heat treatment and deformation on 
mechanical properties of tungsten heavy alloys, Mater. Sci. Eng.: A 733 (2018) 
374 – 384 .
[89] T.W. Verdonik, et al., Investigation of powder bed laser fusion additive 
manufacturing of 93W, 5.6Ni, 1.4Fe tungsten heavy alloys, Int. J. Refract. Met. 
Hard Mater. 111 (2023) .
[90] R.D. Li, et al., Effects of processing parameters on rapid manufacturing 
90W – 7Ni – 3Fe parts via selective laser melting, Powder Metall. 53 (4) (2013) 
310 – 317 .
[91] A. Ivekovi ´c, et al., Effect of processing parameters on microstructure and 
properties of tungsten heavy alloys fabricated by SLM, Int. J. Refract. Met. Hard 
Mater. 82 (2019) 23 – 30 .
[92] T. Schwanekamp, et al., Investigations on laser powder bed fusion of tungsten 
heavy alloys, Int. J. Refract. Met. Hard Mater. 109 (2022) .
[93] X. Wang, et al., Densification of W – Ni – Fe powders using laser sintering, Int. J. 
Refract. Met. Hard Mater. 56 (2016) 145 – 150 .
[94] H. Chen, et al., Microstructure and mechanical properties of additive 
manufactured W-Ni-Fe-Co composite produced by selective laser melting, Int. J. 
Refract. Met. Hard Mater. 86 (2020) .
[95] D.Q. Zhang, et al., Influence of Ni content on microstructure of W – Ni alloy 
produced by selective laser melting, Int. J. Refract. Met. Hard Mater. 45 (2014) 
15 – 22 .
[96] F. Miranda, et al., Ni based tungsten heavy alloy processed by L-PBF additive 
manufacturing and conventional LPS routes, Mater. Today.: Proc. (2023) .
[97] A. Yan, et al., Microstructure, thermal physical property and surface morphology 
of W-Cu composite fabricated via selective laser melting, Mater. Des. 109 (2016) 
79 – 87 .
[98] D. Zhang, et al., Microstructural evolvement and formation of selective laser 
melting W – Ni – Cu composite powder, Int. J. Adv. Manuf. Technol. 67 (9-12) 
(2013) 2233 – 2242 .
[99] M. Wang, et al., Selective laser melting of W-Ni-Cu composite powder: 
Densification, microstructure evolution and nano-crystalline formation, Int. J. 
Refract. Met. Hard Mater. 70 (2018) 9 – 18 .
[100] J. Xie, et al., Additive manufacturing of tungsten using directed energy deposition 
for potential nuclear fusion application, Surf. Coat. Technol. 409 (2021) .
[101] J. Lee, Y.C. Shin, Crack-free tungsten coating on ODS plate via a modified laser- 
based additive technique: offset laser cladding, Surf. Coat. Technol. 476 (2024) .
[102] W. Jeong, Y.-S. Kwon, D. Kim, Three-dimensional printing of tungsten structures 
by directed energy deposition, Mater. Manuf. Process. 34 (9) (2019) 986 – 992 .
[103] C. Li, et al., Densification, microstructural evolutions of 90W-7Ni-3Fe tungsten 
heavy alloys during laser melting deposition process, Int. J. Refract. Met. Hard 
Mater. 91 (2020) .
[104] G. Wang, et al., Influence of processing parameters on the microstructure and 
tensile property of 85 W-15Ni produced by laser direct deposition, Int. J. Refract. 
Met. Hard Mater. 82 (2019) 227 – 233 .
[105] S. Su, Y. Lu, Densified W Cu composite fabricated via laser additive 
manufacturing, Int. J. Refract. Met. Hard Mater. 87 (2020) .
[106] P. Rebesan, et al., Tungsten Fabricated by Laser Powder Bed Fusion, BHM Berg. H. 
üttenm ¨annische Mon. 166 (5) (2021) 263 – 269 .
[107] X. Ren, et al., Effects of processing parameters on the densification, 
microstructure and mechanical properties of pure tungsten fabricated by 
optimized selective laser melting: From single and multiple scan tracks to bulk 
parts, Int. J. Refract. Met. Hard Mater. 96 (2021) .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
29

## Page 30

[108] R.K. Enneti, R. Morgan, S.V. Atre, Effect of process parameters on the Selective 
Laser Melting (SLM) of tungsten, Int. J. Refract. Met. Hard Mater. 71 (2018) 
315 – 319 .
[109] Abbas, M.A., Y. Anru, and Z.Y. Wang, Micro-Structural characteristics of 
Additively Manufactured Pure Tungsten, in International Conference on 
Sustainable Future and Environmental Science. 2021, IOP Conference Series. p. 
012014. .
[110] M. Guo, et al., Formation of scanning tracks during Selective Laser Melting (SLM) 
of pure tungsten powder: Morphology, geometric features and forming 
mechanisms, Int. J. Refract. Met. Hard Mater. 79 (2019) 37 – 46 .
[111] T. Yamamoto, M. Hara, Y. Hatano, Effects of fabrication conditions on the 
microstructure, pore characteristics and gas retention of pure tungsten prepared 
by laser powder bed fusion, Int. J. Refract. Met. Hard Mater. 95 (2021) .
[112] C. Tan, et al., Selective laser melting of high-performance pure tungsten: 
parameter design, densification behavior and mechanical properties, Sci. Technol. 
Adv. Mater. 19 (1) (2018) 370 – 380 .
[113] Sidambe, A.T. and P. Fox, Analysis of the melt pool during laser powder bed 
fusion of tungsten in RAPDASA 2019 Conference Proceedings. 2019. p. 129-139.
[114] X. Zhou, et al., Balling phenomena in selective laser melted tungsten, J. Mater. 
Process. Technol. 222 (2015) 33 – 42 .
[115] J. Dong, et al., Effect of atmosphere on the microstructure and properties of 
additively manufactured tungsten, Mater. Sci. Technol. 36 (18) (2020) 
1988 – 1996 .
[116] R.K. Enneti, et al., Direct Metal Laser Sintering (DMLS) of Tungsten Powders, Int. 
J. Powder Metall. 53 (4) (2017) 23 – 31 .
[117] Av Müller, et al., Additive manufacturing of pure tungsten by means of selective 
laser beam melting with substrate preheating temperatures up to 1000 ∘ C, Nucl. 
Mater. Energy 19 (2019) 184 – 188 .
[118] L.-Z. Wang, J.-J. Wu, D.-J. Zhang, Properties evolution of additive manufacture 
used tungsten powders prepared by radio frequency induction plasma, Int. J. 
Refract. Met. Hard Mater. 67 (2017) 90 – 97 .
[119] A.C. Field, et al., The effect of powder characteristics on build quality of high- 
purity tungsten produced via laser powder bed fusion (LPBF), Metall. Mater. 
Trans. A 51 (3) (2020) 1367 – 1378 .
[120] B. Vrancken, R.K. Ganeriwala, M.J. Matthews, Analysis of laser-induced 
microcracking in tungsten under additive manufacturing conditions: Experiment 
and simulation, Acta Mater. 194 (2020) 464 – 472 .
[121] J. Zhang, et al., Influence of particle size on laser absorption and scanning track 
formation mechanisms of pure tungsten powder during selective laser melting, 
Engineering 5 (4) (2019) 736 – 745 .
[122] Z. Guo, L. Wang, X.-Z. Wang, Additive manufacturing of W-12Ta(wt%) alloy: 
Processing and resulting mechanical properties, J. Alloy. Compd. 868 (2021) .
[123] H. Ye, et al., Densification and microstructure formation mechanisms of 80 W- 
14Ni-6Fe fabricated by laser powder bed fusion, J. Alloy. Compd. 909 (2022) .
[124] X. Ren, et al., Selective Electron Beam Melting (SEBM) of pure tungsten: 
metallurgical defects, microstructure, texture and mechanical properties, 
Materials 15 (3) (2022) .
[125] E.A.I. Ellis, et al., Processing of tungsten through electron beam melting, J. Nucl. 
Mater. 555 (2021) .
[126] D. Dorow-Gerspach, et al., Additive manufacturing of high density pure tungsten 
by electron beam melting, Nucl. Mater. Energy 28 (2021) .
[127] G. Yang, et al., Effect of processing parameters on the density, microstructure and 
strength of pure tungsten fabricated by selective electron beam melting, Int. J. 
Refract. Met. Hard Mater. 84 (2019) .
[128] Ledford, C., et al., Electron Beam Powder Bed Fusion Additive Manufacturing of 
Refractory Metals, in Powdermet/Tungsten 2021. 2021: Orlando, Florida, United 
States of America.
[129] A. Yan, et al., The microstructure and cracking behaviors of pure molybdenum 
fabricated by selective laser melting, Mater. (Basel) 15 (18) (2022) .
[130] P. Rebesan, et al., Pure molybdenum manufactured by Laser Powder Bed Fusion: 
Thermal and mechanical characterization at room and high temperature, Addit. 
Manuf. 47 (2021) .
[131] D. Wang, et al., Densification and crack suppression in selective laser melting of 
pure molybdenum, Mater. Des. 129 (2017) 44 – 52 .
[132] M. Higashi, T. Ozaki, Selective laser melting of pure molybdenum: evolution of 
defect and crystallographic texture with process parameters, Mater. Des. (2020) 
191 .
[133] C.C. Eckley, et al., Evaluating Molybdenum-Rhenium Alloys Through Additive 
Manufacturing, Jom 75 (6) (2023) 1928 – 1940 .
[134] F. Oehlerking, et al., Microstructural characterization and mechanical properties 
of additively manufactured molybdenum and molybdenum alloys, Int. J. Refract. 
Met. Hard Mater. 109 (2022) .
[135] D.R. Ervin, et al., Structure and properties of high energy, high rate consolidated 
molybdenum alloy TZM, Mater. Sci. Eng.: A 102 (1988) 25 – 30 .
[136] T. Liu, et al., Oxygen content effect on mechanical properties and microstructure 
of TZM alloy, Mater. Charact. 203 (2023) .
[137] L. Kaserer, et al., Microstructure and mechanical properties of molybdenum- 
titanium-zirconium-carbon alloy TZM processed via laser powder-bed fusion, Int. 
J. Refract. Met. Hard Mater. 93 (2020) .
[138] L. Kaserer, et al., Molybdenum alloy Mo-Ti-Zr-C adapted for laser powder bed 
fusion with refined isotropic microstructure and excellent high temperature 
strength, Int. J. Refract. Met. Hard Mater. 113 (2023) .
[139] J. Braun, et al., On the role of carbon in molybdenum manufactured by Laser 
Powder Bed Fusion, Int. J. Refract. Met. Hard Mater. 92 (2020) .
[140] L. Kaserer, et al., Fully dense and crack free molybdenum manufactured by 
Selective Laser Melting through alloying with carbon, Int. J. Refract. Met. Hard 
Mater. 84 (2019) .
[141] N.E. Ellsworth, et al., Influence of Nano-Sized SiC on the Laser Powder Bed Fusion 
of Molybdenum, Crystals 12 (9) (2022) .
[142] D. Fichtner, et al., Additive manufacturing of a near-eutectic Mo – Si – B alloy: 
Processing and resulting properties, Intermetallics 128 (2021) .
[143] J. Schmelzer, et al., Printability of gas atomized Mo-Si-B powders by laser metal 
deposition, Int. J. Refract. Met. Hard Mater. 78 (2019) 123 – 126 .
[144] T. Ramakrishnan, et al., Laser powder bed fusion additive manufacturing of 
molybdenum using a nitrogen build atmosphere, Int. J. Refract. Met. Hard Mater. 
119 (2024) .
[145] D. Faidel, et al., Investigation of the selective laser melting process with 
molybdenum powder, Addit. Manuf. 8 (2015) 88 – 94 .
[146] Vanhoose, J.H.., Investigating using titanium zirconium molybdenum for 
additively manufacturing aerospace components, in Department of Mechanical 
Engineering. 2019, University of Texas at el Paso.
[147] B. Guan, et al., Strategies to reduce pores and cracks of molybdenum fabricated by 
selective laser melting, Int. J. Refract. Met. Hard Mater. 112 (2023) .
[148] J.L. Johnson, T. Palmer, Directed energy deposition of molybdenum, Int. J. 
Refract. Met. Hard Mater. 84 (2019) .
[149] T. Ramakrishnan, S. Kwon, M. Brochu, Laser powder bed fusion of molybdenum 
under various Ar-N2 mixture build atmospheres, Int. J. Refract. Met. Hard Mater. 
119 (2024) .
[150] Bustin, M.L., Additive Manufacturing of Molybdenum for High Temperature 
Structural Applications, in Department of Aeronautics and Astronautics. 2022, Air 
Force Institute of Technology.
[151] P. Fernandez-Zelaia, et al., Crystallographic texture evolution in electron beam 
melting additive manufacturing of pure Molybdenum, Mater. Des. (2021) 207 .
[152] G. Marinelli, et al., Microstructure, hardness and mechanical properties of two 
different unalloyed tantalum wires deposited via wire + arc additive 
manufacture, Int. J. Refract. Met. Hard Mater. 83 (2019) .
[153] G. Marinelli, et al., Grain refinement in an unalloyed tantalum structure by 
combining Wire + Arc additive manufacturing and vertical cold rolling, Addit. 
Manuf. 32 (2020) .
[154] Y.-K. Kim, H.-J. Kim, K.-A. Lee, Solid-state cold spray additive manufacturing of 
pure tantalum with extraordinary high-temperature mechanical properties, 
J. Mater. Res. Technol. 23 (2023) 5698 – 5709 .
[155] D.M. Jafarlou, et al., Solid-state additive manufacturing of tantalum using high- 
pressure cold gas-dynamic spray, Addit. Manuf. 47 (2021) .
[156] D.R. Jones, et al., Spall fracture in additive manufactured tantalum, J. Appl. Phys. 
124 (22) (2018) .
[157] Oh, J., et al., Crystallographic Texture Formation of Pure Tantalum by Selective 
Laser Melting Method. 2019.
[158] C. Tan, et al., Effect of oxygen content of tantalum powders on the characteristics 
of parts processed by laser powder bed fusion, Int. J. Refract. Met. Hard Mater. 
110 (2023) .
[159] J. Du, et al., Improving the microstructure and mechanical properties of laser 
powder bed fusion-fabricated tantalum by high laser energy density, Mater. Lett. 
333 (2023) .
[160] S. Qi, et al., Microstructure and mechanical properties of selective laser melted 
pure tantalum using radio frequency plasma spheroidized powder, Rare Met. 
Mater. Eng. 49 (12) (2020) 4023 – 4030 .
[161] W. Chen, et al., Fatigue behaviour and biocompatibility of additively 
manufactured bioactive tantalum graded lattice structures for load-bearing 
orthopaedic applications, Mater. Sci. Eng. C. Mater. Biol. Appl. 130 (2021) 
112461 .
[162] F. Lian, et al., Selective Laser Melting Additive Manufactured Tantalum: Effect of 
Microstructure and Impurities on the Strengthening-Toughing Mechanism, Mater. 
(Basel) 16 (8) (2023) .
[163] L. Zhou, et al., Microstructure tailoring to enhance strength and ductility in pure 
tantalum processed by selective laser melting, Mater. Sci. Eng.: A 785 (2020) .
[164] B. Guan, et al., Microstructure and strengthening mechanisms of tantalum 
prepared using laser melting deposition, Int. J. Refract. Met. Hard Mater. 103 
(2022) .
[165] A.A.A. Aliyu, et al., Additive manufacturing of tantalum scaffolds: processing, 
microstructure and process-induced defects, Int. J. Refract. Met. Hard Mater. 112 
(2023) .
[166] C. Sungail, A.D. Abid, Additive manufacturing of tantalum – A study of chemical 
and physical properties of printed tantalum, Met. Powder Rep. 75 (1) (2020) 
28 – 33 .
[167] S.L. Sing, F.E. Wiria, W.Y. Yeong, Selective laser melting of titanium alloy with 
50 wt% tantalum: effect of laser process parameters on part quality, Int. J. 
Refract. Met. Hard Mater. 77 (2018) 120 – 127 .
[168] J. Xie, et al., Additive manufacturing of tantalum-zirconium alloy coating for 
corrosion and wear application by laser directed energy deposition on Ti6Al4V, 
Surf. Coat. Technol. 411 (2021) .
[169] G.M. Valentino, et al., Influence of laser processing parameters on the density- 
ductility tradeoff in additively manufactured pure tantalum, Addit. Manuf. Lett. 4 
(2023) .
[170] V. Livescu, et al., Additively manufactured tantalum microstructures, Materialia 1 
(2018) 15 – 24 .
[171] C. Song, et al., Pure tantalum manufactured by laser powder bed fusion: Influence 
of scanning speed on the evolution of microstructure and mechanical properties, 
Int. J. Refract. Met. Hard Mater. 107 (2022) 105882 .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
30

## Page 31

[172] L. Zhou, et al., Selective laser melting of pure tantalum: Densification, 
microstructure and mechanical behaviors, Mater. Sci. Eng.: A 707 (2017) 
443–451 .
[173] C. Chen, et al., Effect of laser processing parameters on mechanical properties of 
porous tantalum fabricated by laser multi-layer micro-cladding, Rapid Prototyp. 
J. 23 (4) (2017) 758–770 .
[174] Wermuth, L., et al., Selective Laser Melting of Noble and Refractory Alloys for 
Next Generation Spacecraft Thrusters, in METALLIC MATERIALS AND 
PROCESSES: INDUSTRIAL CHALLENGES - MMP 2015. 2015. p. 1-10. .
[175] J. Yang, et al., Static compressive behavior and material failure mechanism of 
trabecular tantalum scaffolds fabricated by laser powder bed fusion-based 
additive manufacturing, Int J. Bioprint 8 (1) (2021) 438 .
[176] A. Girotto, et al., Additively manufactured tantalum cathode for FEBIAD type ion 
sources: production, geometric measurements, and high temperature test, in 14th 
International Particle Accelerator Conference, J. Phys.: Conf. Ser. (2024) 082047 .
[177] J. Yang, et al., Additive manufacturing of trabecular tantalum scaffolds by laser 
powder bed fusion: mechanical property evaluation and porous structure 
characterization, Mater. Charact. 170 (2020) .
[178] 2018, Gray, G.T., et al., Structure/property characterization of spallation in 
wrought and additively manufactured tantalum. 2018..
[179] Gray, G.T., et al., Structure / Property (Constitutive and Dynamic Strength / 
Damage) Behavior of Additively Manufactured Tantalum, in EPJ Web of 
Conferences - DYMAT 2018. 2018.
[180] H. Gao, et al., Static compressive behavior and failure mechanism of tantalum 
scaffolds with optimized periodic lattice fabricated by laser-based additive 
manufacturing, 3D Print. Addit. Manuf. (2022) .
[181] Y. Zhang, et al., Customized design and biomechanical property analysis of 3D- 
printed tantalum intervertebral cages, Biomed. Mater. Eng. 35 (2) (2024) 99–124 .
[182] H. Li, et al., Effects of unit cell topology on the mechanical properties of porous 
tantalum structures via Laser Powder Bed Fusion, Adv. Eng. Mater. 25 (9) (2023) .
[183] R. Wauthle, et al., Additively manufactured porous tantalum implants, Acta 
Biomater. 14 (2015) 217–225 .
[184] H. Gao, et al., Porous structure and compressive failure mechanism of additively 
manufactured cubic-lattice tantalum scaffolds, Mater. Today Adv. 12 (2021) .
[185] H. Wang, et al., Comparison of 3D-printed porous tantalum and titanium scaffolds 
on osteointegration and osteogenesis, Mater. Sci. Eng. C. Mater. Biol. Appl. 104 
(2019) 109908 .
[186] G. Huang, S.T. Pan, J.X. Qiu, The osteogenic effects of porous Tantalum and 
Titanium alloy scaffolds with different unit cell structure, Colloids Surf. B 
Biointerfaces 210 (2022) 112229 .
[187] P. Lei, et al., Porous tantalum structure integrated on Ti6Al4V base by Laser 
Powder Bed Fusion for enhanced bony-ingrowth implaNts: In Vitro and in vivo 
validation, Bioact. Mater. 7 (2022) 3–13 .
[188] A. Bandyopadhyay, et al., Direct comparison of additively manufactured porous 
titanium and tantalum implants towards in vivo osseointegration, Addit. Manuf. 
28 (2019) 259–266 .
[189] J. Jiao, et al., Influence of porosity on osteogenesis, bone growth and 
osteointegration in trabecular tantalum scaffolds fabricated by additive 
manufacturing, Front. Bioeng. Biotechnol. 11 (2023) 1117954 .
[190] H. Fan, et al., Highly porous 3D printed tantalum scaffolds have better 
biomechanical and microstructural properties than titanium scaffolds, Biomed. 
Res Int 2021 (2021) 2899043 .
[191] H.P. Tang, et al., Tantalum bone implants printed by selective electron beam 
manufacturing (SEBM) and their clinical applications, Jom 72 (3) (2020) 
1016–1021 .
[192] Y. Guo, et al., Microstructural evolution and mechanical behavior of additively 
manufactured tantalum produced by electron beam powder bed fusion, Int. J. 
Refract. Met. Hard Mater. 110 (2023) .
[193] T. Griemsmann, et al., Laser-based powder bed fusion of niobium with different 
build-up rates, Int. J. Adv. Manuf. Technol. 114 (1-2) (2021) 305–317 .
[194] M. Liu, et al., Additive manufacturing of pure niobium by laser powder bed 
fusion: Microstructure, mechanical behavior and oxygen assisted embrittlement, 
Mater. Sci. Eng.: A (2023) 866 .
[195] P.D. Awasthi, et al., Mechanical properties and microstructural characteristics of 
additively manufactured C103 niobium alloy, Mater. Sci. Eng.: A 831 (2022) .
[196] Mireles, O., et al., Additive Manufacture of Refractory Alloy C103 for Propulsion 
Applications, in AAIA Propulsion and Energy 2020 Forum. 2020: Virtual Event.
[197] K. Hagihara, T. Nakano, Control of anisotropic crystallographic texture in powder 
bed fusion additive manufacturing of metals and ceramics—a review, Jom 74 (4) 
(2021) 1760–1773 .
[198] J.I. Ferguson, et al., The role of additively manufactured niobium alloy C103 
substrate’s surface finish and corner geometry on the silicide diffusion coating’s 
performance, Surf. Coat. Technol. 479 (2024) .
[199] J. Chen, et al., Laser powder bed fusion of a Nb-based refractory alloy: 
microstructure and tensile properties, Mater. Sci. Eng.: A (2022) 843 .
[200] J. Chen, et al., Strong and ductile niobium-based refractory alloy via deformable 
zirconia nanoparticles, Int. J. Refract. Met. Hard Mater. 118 (2024) .
[201] Feitosa, L.M., Solidification Behaviour and Microstructure Evolution of Refractory 
Metals-Based Alloys Under Rapid Solidification, in Department of Engineering. 
2018, The University of Leicester.
[202] A. Allen, et al., Solidification of niobium-silicide-based alloys during laser 
additive manufacturing process, IOP Conf. Ser.: Mater. Sci. Eng. (2019) 012006 .
[203] Y. Guo, et al., Rapid fabrication of Nb-Si based alloy by selective laser melting: 
microstructure, hardness and initial oxidation behavior, Mater. Des. 109 (2016) 
37–46 .
[204] Y. Li, et al., Zirconium modified Nb-22Ti-16Si alloys fabricated by laser additive 
manufacturing: microstructure and fracture toughness, J. Alloy. Compd. 783 
(2019) 66–76 .
[205] S. Candela, et al., Pure niobium manufactured by Laser-Based Powder Bed Fusion: 
influence of process parameters and supports on as-built surface quality, Int. J. 
Adv. Manuf. Technol. (2024) .
[206] Y. Guo, et al., Single track and single layer formation in selective laser melting of 
niobium solid solution alloy, Chin. J. Aeronaut. 31 (4) (2018) 860–866 .
[207] K.M. Mullin, et al., Rapid screening of single phase refractory alloys under laser 
melting conditions, Mater. Des. (2024) 238 .
[208] B.P. Bewlay, et al., Ultrahigh-temperature Nb-silicide-based composites, MRS 
Bull. 28 (2003) 646–653 .
[209] M.G. Mendiratta, D.M. Dimiduk, Strength and toughness of a Nb/Nb5Si3 
composite, Metall. Trans. A 24 (1993) 501–504 .
[210] C. Schneider-Maunoury, et al., On the use of instrumented indentation to 
characterize the mechanical properties of functionally graded binary alloys 
manufactured by additive manufacturing, Mater. Today Commun. 25 (2020) .
[211] H. Zhang, et al., The thermal-mechanical behavior of WTaMoNb high-entropy 
alloy via selective laser melting (SLM): experiment and simulation, Int. J. Adv. 
Manuf. Technol. 96 (1-4) (2018) 461–474 .
[212] F. Huber, D. Bartels, M. Schmidt, In-situ alloy formation of a WMoTaNbV 
refractory metal high entropy alloy by laser powder bed fusion (PBF-LB/M), 
Materials 14 (11) (2021) .
[213] T. Ron, et al., Synthesis of refractory high-entropy alloy WTaMoNbV by powder 
bed fusion process using mixed elemental alloying powder, Materials 15 (12) 
(2022) .
[214] P. Gu, et al., Manufacturing and analysis of VNbMoTaW refractory high-entropy 
alloy fabricated by selective laser melting, Int. J. Refract. Met. Hard Mater. 105 
(2022) .
[215] H. Zhang, et al., Manufacturing and analysis of high-performance refractory high- 
entropy alloy via selective laser melting (SLM), Materials 12 (5) (2019) .
[216] C. Liu, et al., Deformation mechanisms of additively manufactured TiNbTaZrMo 
refractory high-entropy alloy: the role of cellular structure, Int. J. Plast. 173 
(2024) .
[217] J. Xu, et al., Enhanced strength and ductility of laser powder bed fused NbMoTaW 
refractory high-entropy alloy via carbon microalloying, Addit. Manuf. Lett. 3 
(2022) .
[218] H. Zhang, et al., High-strength NbMoTaX refractory high-entropy alloy with low 
stacking fault energy eutectic phase via laser additive manufacturing, Mater. Des. 
(2021) 201 .
[219] H. Zhang, et al., Study on annealing treatment of NbMoTaTiNi high-entropy alloy 
with ultra-high strength disordered-ordered transition structure for additive 
manufacturing, J. Alloy. Compd. 941 (2023) .
[220] Y. Chen, B. Li, Double-phase refractory medium entropy alloy NbMoTi via selective 
laser melting (SLM) additive manufacturing, in MAEIE-2022, J. Phys.: Conf. Ser. 
(2023) 012074 .
[221] S. Mooraj, et al., Additive manufacturing of defect-free TiZrNbTa refractory high- 
entropy alloy with enhanced elastic isotropy via in-situ alloying of elemental 
powders, Commun. Mater. 5 (2024) 1–12 .
[222] F. Wang, et al., Effect of Mo on the morphology, microstructure and mechanical 
properties of NbTa0.5TiMo refractory high entropy alloy fabricated by laser 
powder bed fusion using elemental mixed powders, Int. J. Refract. Met. Hard 
Mater. 111 (2023) .
[223] C. Liu, et al., Additive manufacturing of WMoTaTi refractory high-entropy alloy 
by employing fluidised powders, Powder Metall. 65 (5) (2022) 413–425 .
[224] X. Ye, et al., Carbon Nanotubes (CNTs) Reinforced CoCrMoNbTi0.4 Refractory 
High Entropy Alloy Fabricated via Laser Additive Manufacturing: Processing 
Optimization, Microstructure Transformation and Mechanical Properties, Crystals 
12 (11) (2022) .
[225] H. Dobbelstein, et al., Laser metal deposition of compositionally graded TiZrNbTa 
refractory high-entropy alloys using elemental powder blends, Addit. Manuf. 25 
(2019) 252–262 .
[226] H. Dobbelstein, et al., Laser metal deposition of refractory high-entropy alloys for 
high-throughput synthesis and structure-property characterization, Int. J. Extrem. 
Manuf. 3 (1) (2020) .
[227] H. Dobbelstein, et al., Laser metal deposition of a refractory TiZrNbHfTa high- 
entropy alloy, Addit. Manuf. 24 (2018) 386–390 .
[228] M.A. Melia, et al., High-throughput additive manufacturing and characterization 
of refractory high entropy alloys, Appl. Mater. Today 19 (2020) .
[229] M. Moorehead, et al., High-throughput synthesis of Mo-Nb-Ta-W high-entropy 
alloys via additive manufacturing, Mater. Des. (2020) 187 .
[230] E. Lang, et al., Compositional effects of additively manufactured refractory high- 
entropy alloys under high-energy helium irradiation, Nanomater. (Basel) 12 (12) 
(2022) .
[231] A. Ozalp, et al., Development and directed energy deposition of high strength 
Hf5Mo15Nb35Ta25Ti20 refractory high entropy alloys, Mater. Charact. 209 
(2024) .
[232] Q. Li, et al., Comparative study of the microstructures and mechanical properties 
of laser metal deposited and vacuum arc melted refractory NbMoTa medium- 
entropy alloy, Int. J. Refract. Met. Hard Mater. 88 (2020) .
[233] H. Zhang, et al., Development of high strength high plasticity refractory high 
entropy alloy based on Mo element optimization and advanced forming process, 
Int. J. Refract. Met. Hard Mater. 112 (2023) .
[234] B. Xiao, et al., Cracking suppression in selective electron beam melted 
WMoTaNbC refractory high-entropy alloy, J. Alloy. Compd. 948 (2023) .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
31

## Page 32

[235] V.V. Popov, et al., Selective electron beam melting of Al0.5CrMoNbTa0.5 high 
entropy alloys using elemental powder blend, Heliyon 5 (2) (2019) e01188 .
[236] B. Xiao, et al., Selective electron beam melting of WMoTaNbVFeCoCrNi refractory 
high-entropy alloy, Mater. Charact. 193 (2022) .
[237] C. Fietek, E. Brizes, J. Milner, Evaluation of high-vacuum annealing and hot 
isostatic pressing on the microstructure and properties of an additively 
manufactured niobium alloy, Jom 76 (3) (2024) 1223–1234 .
[238] A. du Plessis, E. Macdonald, Hot isostatic pressing in metal additive 
manufacturing: X-ray tomography reveals details of pore closure, Addit. Manuf. 
34 (2020) .
[239] J. Chen, et al., The effect of hot isostatic pressing on thermal conductivity of 
additively manufactured pure tungsten, Int. J. Refract. Met. Hard Mater. 87 
(2020) .
[240] F. Motschmann, R. Gerard, F. Gilles, Purification of selective laser melting 
additive manufactured niobium for superconducting RF-applications transactions 
on applied superconductivity, IEEE Trans. Appl. Supercond. 29 (5) (2019) 1–5 .
[241] H. Dobbelstein, et al., Direct metal deposition of refractory high entropy alloy 
MoNbTaW, Phys. Procedia 83 (2016) 624–633 .
C.V. Funch and G. Proust Additive Manufacturing 94 (2024) 104464 
32
