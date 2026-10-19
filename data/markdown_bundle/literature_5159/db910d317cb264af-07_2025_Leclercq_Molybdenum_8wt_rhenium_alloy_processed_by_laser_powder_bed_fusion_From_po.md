# 07_2025_Leclercq_Molybdenum_8wt_rhenium_alloy_processed_by_laser_powder_bed_fusion_From_powder_production_to_mechanic

<!-- source: D:\总文献\07_2025_Leclercq_Molybdenum_8wt_rhenium_alloy_processed_by_laser_powder_bed_fusion_From_powder_production_to_mechanic.pdf -->
<!-- file_sha256: 90048a159a96deb1bc8bc89bec2304b2b282c0d2b898209bc473f7d077f52e7b -->

## Page 1

Molybdenum 8wt% rhenium alloy processed by laser powder bed fusion: 
From powder production to mechanical testing at elevated temperatures
Aurore Leclercq
a
, Anna Czech
b
, Thibault Mouret
a
, Marcin Lis
b
, Adriana Wrona
b
, 
Vladimir Brailovski
a , *
a
Mechanical Engineering Department, 
´
Ecole de Technologie Sup ´erieure, 1100 Notre-Dame Street West, Montreal, Quebec H3C 1K3, Canada
b
Centre of Powder and Composite Materials, Ł ukasiewicz Research Network - Institute of Non-Ferrous Metals, 5 Sowi ´nskiego Street, 44-100 Gliwice, Poland
ARTICLE INFO
Keywords:
Laser powder bed fusion
Molybdenum-rhenium alloys
Powder production
Mechanical testing
Elevated temperature tests
Crack-free specimens
ABSTRACT
Molybdenum is highly valued in industry because of its unique properties, especially at high temperatures. 
Additive manufacturing technologies, particularly laser powder bed fusion (LPBF), are becoming increasingly 
popular for producing complex shapes at a lower cost as compared to the conventional forming processes. 
However, printing molybdenum with LPBF presents challenges, especially caused by its hot cracking suscepti -
bility. Several approaches have been explored to address this issue, including alloying molybdenum with other 
elements, which has proven effective in enhancing the printability and minimizing the occurrence of cracking, 
particularly with the addition of rhenium. In this study, a combination of mechanical blending of molybdenum 
powder and a rhenium precursor, followed by the reduction of the precursor and plasma spheroidization, was 
used to produce spherical 30 – 55 μ m molybdenum ‑ rhenium (8 wt%) powders with rheological properties suitable 
for LPBF. Compared to pure molybdenum, the use of the alloyed powder led to an increase in the crack-free 
printed density, from 97 to 98.5 %, and in the compressive strength, from 240 to 340 MPa, at 600 
◦
C and 
from 150 to 190 MPa at 1000 
◦
C, at the expense of a ~ 5 % reduction in the compression strain. To demonstrate 
the potential of printing complex geometries using the developed powders, complex geometry artifacts con -
taining 0.25 mm-thin letters, wide dense sections and auto-supported 50 %-density 0.7 mm-thin strut diamond 
lattice structures were successfully printed.
1. Introduction
Molybdenum (Mo) belongs to the refractory metal group, coming in 
fourth in line after Tungsten, Rhenium and Tantalum in terms of melting 
temperature ( T = 2896 K / 2623 
◦
C). Like other refractory metals, 
molybdenum is distinguished by its excellent electrical [ 1 ] and thermal 
[ 2 ] conductivity, a low coefficient of thermal expansion [ 3 ], as well as a 
high mechanical [ 4 ], wear [ 5 ] and corrosion [ 6 ] resistance. This 
element is regularly introduced in small concentrations into the com -
positions of advanced alloys (e.g. , various INCONEL ® , Hastelloy B or 
titanium alloys, such as Ti6246 for example) to improve their corrosion 
resistance. For elevated temperature applications, with UTS = 210 MPa 
[ 4 ] and E = 280 GPa [ 7 ] at 800 
◦
C, molybdenum manifests the highest 
strength- and stiffness-to-density ratios among all the refractory metals. 
Due to this unique combination of properties, molybdenum is a prom -
ising candidate for various applications in different fields, including the 
medical, petrochemical, aerospace and defense industries [ 8 , 9 ].
The creation of semi-finished molybdenum products (e.g. , sheets, 
rods and bars) is currently driven by conventional forming processes, 
mainly including powder metallurgy and plastic deformation processes, 
such as forging, rolling, etc. To manufacture complex geometries, sub -
tractive and joining processes are required, but these have their own 
limitations when applied to refractory metals, such as high machining 
costs and a strong oxygen affinity in the heat affected zone. In response, 
the recent and rapid development of additive manufacturing (AM) 
technologies offers a promising technical solution enabling the pro -
duction of complex shapes at reduced processing cost. Over the years, 
numerous AM technologies have been tested to print refractory metals 
[ 10 , 11 ], each with its own pros and cons. The layer-by-layer laser 
powder bed fusion (LPBF) is the most mature AM technology. The 
process uses a laser heat source to sequentially melt one layer of powder 
at a time according to a pre-defined pattern generated from a sliced 3D 
* Corresponding author.
E-mail addresses: aurore.leclercq.1@ens.etsmtl.ca (A. Leclercq), Anna.Czech@imn.lukasiewicz.gov.pl (A. Czech), thibault.mouret@etsmtl.ca (T. Mouret), Marcin. 
Lis@imn.lukasiewicz.gov.pl (M. Lis), Adriana.Wrona@imn.lukasiewicz.gov.pl (A. Wrona), vladimir.brailovski@etsmtl.ca (V. Brailovski). 
Contents lists available at ScienceDirect
International Journal of Refractory 
Metals and Hard Materials
journal homep age: www. elsevier.com/ locate/IJ RMHM
https://doi.org/10.1016/j.ijrmhm.2025.107266
Received 17 April 2025; Received in revised form 26 May 2025; Accepted 27 May 2025 
International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
Available online 29 May 2025 
0263-4368/© 2025 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by- 
nc-nd/4.0/ ).

## Page 2

CAD model of the desired part. In contrast to its main competitor, 
electron beam powder bed fusion (EB-PBF), LPBF is distinguished by its 
higher resolution, greater printing flexibility, and lower processing costs 
[ 12 , 13 ].
Notwithstanding all the advancements in industrial LPBF applica -
tion, the printability of molybdenum remains a significant challenge. 
The high energy input required to reach the melting temperature and the 
rapid solidification rate of the process result in substantial temperature 
gradients and residual stresses. Additionally, the high ductile to brittle 
transition temperature (DBTT) of molybdenum contributes to its sus -
ceptibility to cracking during printing. The DBTT of molybdenum is 
reported to be highly dependent on the segregation of impurities at the 
grain boundaries (GB) and on the material microstructure [ 14 – 17 ]. Most 
researchers agree to consider molybdenum as a crack-prone material, 
and many of them tried to overcome this problem using different stra -
tegies including optimization of printing parameters [ 10 ], preheating of 
the baseplate [ 18 – 20 ], and preheating of the powder bed using a mul -
tiple exposure approach. To date, the two first strategies have demon -
strated low-to-zero efficiency, while the third approach has appeared to 
be more technologically promising but less economically efficient in this 
regard [ 21 ].
In the literature, alloying molybdenum with different elements rep -
resents a common solution for improving its printability, increasing its 
density, and simultaneously, mitigating hot cracking [ 22 – 26 ]. Various 
alloy compositions have been tested, and depending on the nature of the 
alloying elements involved, several types of microstructural modifica -
tions improving the cracking resistance of molybdenum have been re -
ported. These modifications target the main factors responsible for 
cracking, including the propensity to form irregular microstructures or 
to segregate interstitial elements at grain boundaries (GB). In fact, 
alloying has been successfully used to transform coarse columnar mi -
crostructures into equiaxed grain structures or submicron cell structures 
[ 23 , 27 , 28 ]. Alloying has been also successfully used to promote GB 
cohesion and to limit their oxidation [ 24 , 25 ], as well as to decrease the 
DBTT [ 29 , 30 ]. Thus, depending on the physical, mechanical and 
microstructural features expected, the selection of alloying elements is 
fundamental. Moreover, both the pre-alloyed powders and in-process 
alloyed powders can also be considered in this regard.
As an example, dispersion within the powder bed of oxygen-sensitive 
elements, such as carbon (C, 0.45 wt%, [ 23 ]) under its elemental form, 
or through the use of silicon carbide (SiC, 0.1 wt%, [ 24 ]), appeared to be 
a promising solution to increase the printed density of molybdenum and 
to reduce its brittleness. In the atmospheric conditions of the LPBF 
process (O
2 
low partial pressure), these species enable the reduction of 
the overall oxygen content, through the outgassing of a volatile carbon 
monoxide CO. Thus, segregation at the grain boundaries and the for -
mation of detrimental molybdenum oxide MoO
3 
is limited. Further -
more, elemental carbon powders modify the solidification behavior and 
lead to a refined cellular microstructure, with molybdenum surrounded 
by molybdenum carbide Mo
2
C, while nanosized SiC particles apparently 
block dislocations and inhibit the propagation of cracks. Effectively, by 
combining the dispersion of elemental carbon powders with the base -
plate preheating to up to 800 
◦
C, the authors of the referenced studies 
were able to reduce cracking.
Alloying refractory metals with others transition metals was also 
found to be effective in inhibiting the cracks formation associated with 
the LBPF process by Gan et al. [ 25 ] who successfully used chromium (Cr) 
and titanium (Ti) additions into molybdenum. For their part, Guo et al. 
[ 28 ] dispersed nickel (Ni) and iron (Fe) nanoparticles within tungsten 
powders. In both cases, the authors reported cracks suppression. From 
their observations, using nanosized particles with a large surface area 
promote the formation of an equiaxed fine grain microstructure with 
sufficient ductility to prevent cracking. Conversely, with coarser parti -
cles ( μ m range), they attributed the resistance to cracking to the for -
mation of solid solutions strengthening the parts and capturing 
oxidation traces (MoO
3
) in the melt pool. Recently, some authors have 
also steered their attention to high-entropy refractory alloys (RHEA) 
[ 31 , 32 ].
One of the most common and commercially available Mo alloys is 
Titanium-Zirconium-Molybdenum (TZM). It contains small concentra -
tions ( < 1 wt%) of titanium, zirconium and carbon enhancing its me -
chanical strength through the precipitation of Mo and Ti carbides. This 
mechanism is analogous to the process observed with the addition of 
elemental carbon powders. In fact, oxidation, carboreduction and out -
gassing inhibit segregation of impurities at the grain boundaries through 
the formation of gaseous carbon monoxide and titanium oxides (TiO bp 
= 3227 
◦
C, TiO
2 
bp = 2970 
◦
C) [ 33 ]. The same authors also reported 
oxygen bounding with zirconium (ZrO
2
) and with (Mo,Ti)
x
C
y 
pre -
cipitates, which lead to LPBF parts with purified grain boundaries. They 
also demonstrated that a TZM-modified alloy with an increased carbon 
content (up to 2.3 at.%) enables to create refined and isotropic cellular 
microstructures with improved elevated-temperature mechanical prop -
erties (YS = 450 MPa, UTS = 600 MPa at 800 
◦
C) over what could be 
obtained using conventional processes [ 34 ]. In all cases, the authors of 
the above works reported the LPBF production of high density and 
crack-free TZM samples. The main drawback of the TZM alloy is its high 
price per weight ratio, which is at least three times higher than that of 
pure molybdenum. This is the reason why the most common alloying 
solution for refractory metals continues to be their combination in dual 
alloys with reduced DBTT, enhanced ductility, and suppressed cracking 
[ 35 – 37 ].
In the above context, rhenium (Re) represents one of the most 
promising alloying elements for dual refractory alloys, notwithstanding 
a related increase in powder cost. For example, alloys such as Mo47.5Re 
or W25Re30Mo (wt%) have shown remarkable enhancements in their 
mechanical properties at room [ 35 ] and high [ 38 ] temperatures, 
respectively. Oehlerking et al. [ 26 ] reported the successful LPBF print -
ing of complex demo parts with Mo47.5Re powders and an almost 60 % 
improvement in their room-temperature mechanical properties. How -
ever, the authors were not able to prevent cracking due to an excessive 
residual oxygen content. Eckley et al. [ 39 ] investigated the impact of 
adding 5, 10 and 25 wt% of rhenium on the room-temperature flexural 
strength of Mo
–
Re alloys. They reported a softening effect occurring for 
the low Re content, no changes for the intermediate Re content, and a 
slight hardening for the high Re content. These results are in agreement 
with the extensive study conducted by J. Stephens and W. R. Witzke 
[ 40 ], who identified a Re threshold separating the softening and the 
hardening behavior of Mo
–
Re compounds at Re ≈ 16 at.% and/or at 
0.16T
m 
Mo (⁓420 
◦
C).
Although the production catalogues of powder manufacturers have 
grown significantly over the years, the process of obtaining 
molybdenum-based powders with specific alloying compositions, such 
as those described previously, remains challenging and costly. The 
powder production step is crucial as the quality of LPBF parts is signif -
icantly influenced by the uniformity and density of the powder bed, 
which in turn depends on the morphology and size distributions of 
powder particles [ 41 , 42 ]. Traditional mechanical methods (e.g. , 
grinding, mechanical synthesis, etc.) or physicochemical methods (e.g. , 
reduction of compounds, condensation from the gas phase, synthesis 
from solutions, etc.) used to produce alloyed powders are unsuitable for 
this process. Powders produced with such methods are generally char -
acterized by an irregular particle shape and a low bulk density, likely to 
negatively affect the density and mechanical properties of printed parts.
Spherical powders can be produced using different physical atomi -
zation methods. Wide applications of some of these methods, such as the 
plasma rotating electrode process (PREP) [ 43 – 45 ] or ultrasonic 
vibrations-assisted atomization [ 46 , 47 ], are limited because of the 
accompanying low production rates. The use of other physical methods, 
such as water atomization, is much more cost-effective, but results in 
somewhat coarse and irregular-shape particles. Moreover, the high ox -
ygen intake inherent to this process makes it incompatible with reactive 
metals such as titanium or aluminum [ 48 ] and unsuitable for refractory 
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
2

## Page 3

metals which are also highly sensitive to oxygen content. The gas at -
omization method, while being largely used for the production of metal 
powders for 3D printing [ 49 , 50 ], has limited applicability for refractory 
metals because of their extremely high melting temperatures.
To overcome the above difficulties related to the production of re -
fractory powders with a high degree of purity and sphericity, industry 
principally uses plasma-based techniques, such as plasma atomization 
and plasma spheroidization [ 58 , 59 ]. In the former case, the feedstock is 
generally a wire, while in the latter, it consists of crushed powder par -
ticles. The use of a wire feedstock requires several resource-intensive 
steps, involving rolling and drawing, which result in extremely expen -
sive products and carries a significant environmental footprint. For its 
part, the use of plasma spheroidization is less restrictive, since the 
technique produces spherical powders from their irregular precursors, 
the latter obtained by various mechanical (crashing, milling), and 
therefore, less expensive and less polluting methods. In both cases, 
however, an ingot of a given alloy composition must be cast, making the 
production of powders of different target formulations economically 
challenging. To overcome this, alloyed powders suitable for 3D printing 
can be produced via chemical modifications of their elementary pre -
cursors [ 51 , 52 ] and then subjected to plasma spheroidization.
This study delineates the methodology employed to produce LPBF- 
ready molybdenum alloy powders containing a low amount of 
rhenium, Mo8wt%Re, abbreviated as Mo8Re. The alloyed powder is 
subsequently characterized in terms of its physical and rheological 
properties and used in a comprehensive printability study involving the 
physical and microstructural analyses of specimens produced using 
different combinations of printing parameters. Two optimized sets of 
printing parameters found during this study are then used to produce 
specimens for mechanical testing in a wide temperature range. Finally, 
the results obtained with Mo8Re powders are compared to those ac -
quired with ≥ 99.9 %Mo powders, to reveal the effect of a relatively 
limited rhenium addition on the LPBF printability and mechanical 
properties of molybdenum.
2. Materials and methods
2.1. Powder production
Two powder lots were concurrently used in the context of this study: 
the first is a commercial (Tekna Co. Ltd., Sherbrooke, Canada) plasma- 
atomized molybdenum powder (99.9 % Mo) with the following pow -
der size distribution: D10 = 12.6, D50 = 20.6 and D90 = 32.0 ( μ m). This 
powder was considered as a reference feedstock for the LPBF process. 
The second is an alloyed Mo8Re powder developed for this study.
The production of Mo8Re powders was divided in three successive 
steps and was entirely realized at the Institute of Non-Ferrous Metal 
( Ł ukasiewicz Research Network, Poland). First, the preparation of a 
feedstock started with the mechanical blending of the molybdenum 
powder and the rhenium precursor, followed by the latter being reduced 
to obtain a Mo
–
Re mixture. To this end, commercial high purity Mo 
powder (99.99 %, KAMB Import Export) with a particle size range of 
17 – 78 μ m was selected. Regarding the rhenium, it was introduced as 
ammonium perrhenate (APR) NH
4
ReO
4 
(99.9 %, Innovator Ltd). The 
mixture was made according to the stoichiometric Mo8Re proportions 
(88.87 %wt Mo + 11.52 %wt NH
4
ReO
4
). The reduction process that 
enables to obtain metallic rhenium was conducted at 800 
◦
C in 100 % 
hydrogen atmosphere for two hours. This specific temperature is asso -
ciated with the APR reduction temperature. During the thermal treat -
ment, direct NH
4
ReO
4 
reduction (1) and/or indirect reduction from the 
oxides (mainly Re
2
O
7
, ReO
3 
and ReO
2
) occur, depending on the tem -
perature of the reaction [ 53 ]. 
2 NH
4
ReO
4 ( s )
+ 7 H
2 ( g )
= 2 Re
( s )
+ 8 H
2
O
( g )
+ 2 NH
3 ( g )
(1) 
Then, the Mo
–
Re mixture was introduced in a customized plasma 
spheroidization system. To generate Ar
–
H
2 
plasma, a 7 MB plasma 
torch was used (Sulzer Metco [ 54 ]). The addition of hydrogen enables to 
increase the enthalpy and temperature of plasma flame, which is 
beneficial in the production of spherical high-melting powders. The 
powder was injected perpendicularly into the plasma flame area, melted 
inside and sprayed in the form of spherical droplets. After leaving the 
plasma zone, liquid particles were rapidly cooled down in an inert at -
mosphere to minimize their oxidation. The plasma spheroidization pa -
rameters used are summarized in Table 1 . This spheroidization step is an 
essential stage of the whole powder production technology chain. It 
enables to improve the flowability of powder by changing the particle 
morphology from irregular to spheroidal, also enhancing the overall 
chemical composition homogeneity and bulk density.
The literature demonstrated that the presence of oxygen in powders 
and printed parts made of molybdenum is one of the main factors 
leading to embrittlement and cracking during the LPBF process. 
Consequently, to minimize the oxygen content, a supplementary deox -
idization process of the spheroidal powder was conducted at 1050 
◦
C for 
one hour in a 100 % hydrogen atmosphere. A final sieving step through a 
90 μ m sieve was realized before the powder was used for LPBF printing.
2.2. Powder characterization
2.2.1. Chemical and phase analyses
The element distribution within the powder was assessed using an 
electron probe microanalyzer (EPMA) (JEOL JXA-8230, JEOL Ltd., 
Japan) and its EDS detector. The oxygen content in the powder was 
obtained with an IR spectroscope (LECO ON836, LECO Corp., USA). The 
crystalline structure of the powder was determined by X-ray diffraction 
(XRD) (Seifert XRD7, Cu source, GE Inspection Technologies, USA). 
These observations and analyses were conducted at different stages of 
the process to evaluate the efficiency of the production steps.
2.2.2. Physical and rheological analyses
The particle size distribution (PSD) was measured using an Analy -
sette 22 Nanotec powder size analyzer (Fritsch, Germany), while its 
pycnometric density was obtained using an Accupyc 1340 helium pyc -
nometer (Micromeritics, USA). The efficiency of the spheroidization step 
was evaluated by measuring the specific surface area, using the BET 
method (Gemini 2360, Micromeritics, USA). The powder flowability 
was measured using a Hall flowmeter according to the ISO 4490-2018 
standard (50 g). Additional rheological measurements were carried 
out using an FT4 powder rheometer (Freeman Technology, UK). This 
equipment possesses different testing modes for which detailed infor -
mation and listed outputs can be found in the manufacturer ’ s docu -
mentation and publications [ 55 , 56 ]. The rheological behavior of the 
produced Mo8Re powder was compared to that of a pure molybdenum 
powder used in the reference work [ 57 ]. Five testing modes were 
applied, namely dynamic flow, aeration, permeability, compressibility 
and shear. Table 2 summarizes the metrics obtained from these tests.
Finally, the Additive Manufacturing Suitability ( AMS ) figure of merit 
(2) was used to express the overall suitability of two powder lots for 
LPBF. The figure was first defined in a work dedicated to the comparison 
of Ti-6Al-4 V powders [ 58 ] and aims to compare different powder lots of 
the same material based of selected rheological characteristics repre -
sentative of the LPBF process. The smaller the AMS value, the more 
suitable the selected powder for the LPBF process: 
Table 1 
Plasma spheroidization process parameters.
Current 
(A)
Plasma gas 
flow 
rate ‑ argon 
(l/min)
Plasma gas flow 
rate ‑ hydrogen 
(l/min)
Carrier gas 
flow 
rate ‑ argon 
(l/min)
Powder feeder 
plate revolutions 
(rpm)
500 50 10 4 2
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
3

## Page 4

AMS =
1
ρ
powder
+ CI + PD + SE + AE
10
+ BFE + CC
7
(2) 
where ρ
powder 
is the relative powder bed density obtained from (3). 
ρ
powder
=
BD
ρ
s
(3) 
where ρ
s 
is the material density obtained by the pycnometer measure -
ments of each powder lot.
2.3. LPBF process and plan of experiment
In the literature, various printing parameter sets have been tested in 
a bid to improve the printability of pure molybdenum, leading to very 
divergent results due to the impact of multiple phenomena occurring 
during printing (lack of fusion, cracking, etc.). However, a critical 
analysis of the results obtained in a previous study using a 200 W-power 
LPBF printer [ 57 ] enabled to highlight general trends and formulate 
some potential solutions to solve the above problems. These solutions 
include the reduction of the scanning speed and the optimization of the 
hatching space for a given laser spot size. That was carried out using a 
series of printing parameter sets defined in the volumetric energy den -
sity ( VED , (4)) - build rate ( BR , (5)) coordinates: 
VED
[
J
/
mm
3
]
=
P
vht
(4) 
BR
[
cm
3
/
h
]
= vht (5) 
where P (W) is the laser power; v (mm/s), the scanning speed; h ( μ m), 
the hatching space and t ( μ m), the layer thickness.
For pure molybdenum, two different VED-BR sets provided superior 
results in terms of the printed density and the mechanical properties at 
room and elevated temperatures: 750 J/mm
3
– 0.86 cm
3
/h and 400 J/ 
mm
3
– 1.62 cm
3
/h. Consequently, the same two VED-BR sets, herein 
called Set I and Set II (analogous to the VED-BR combinations C and in E 
in the reference study [ 57 ]), were considered in the present study for 
Mo8Re printing. To optimize the printing parameters using these VED- 
BR combinations, the hatching space value was incrementally increased 
(h = 40, 60, 80, 100 and 120 μ m) to cover the 1.1 to 4 h / t ratio range. 
The printed samples were tagged with their respective VED-BR set and 
hatching space denominations. For example, specimen I-80 stands for 
the one obtained with VED = 750 J/mm
3
, BR = 0.86 cm
3
/h, i.e., laser 
power P = 179 W, scanning speed v = 100 mm/s and hatching space h =
80 μ m. Note that the layer thickness t was constant and equal to 30 μ m in 
all the cases. Table 3 summarizes the printing conditions of the experi -
mental plan.
The Mo8Re powders were printed under argon atmosphere on a 
Trumpf Truprint1000 system with a 200 W dual laser source. The 
printing parameters described in the plan of experiments above were 
used to produce ten cylindrical specimens (h = 20 mm, Φ = 10 mm), 
with 5 mm-thickness dense supports ( Fig. 1 a). All the specimens were 
printed on a stainless-steel baseplate without preheating. After removal 
from the baseplate, the specimens were cut and the samples obtained 
were used for structural analyses and compression testing at room 
temperature, RT ( Fig. 1 a). Based on the printed density values measured 
and on the results of the RT testing, one parameter set was selected as 
being the best, and it was then used to print specimens for compression 
testing at elevated temperatures (600, 800 and 1000 
◦
C).
In addition to the cylindrical specimens used to optimize the printing 
parameters, lattice-containing artifacts in the shape of a pineapple were 
produced ( Fig. 1 b). Apart from the aesthetic aspect, this complex ge -
ometry part contains some design features which are challenging to 
print with the LPBF process, such as thin walls, fine letters, wide dense 
sections and self-supported structures.
2.4. Density measurements
The densities of the printed samples reported in the study were 
evaluated using the image analysis method. Their z-y cross sections were 
mounted in carbon-doped resin and mirror-polished and subjected to 
microscopic observations using a LEXT OLS4100 (Lext Olympus Corp., 
Japan) laser confocal microscope. The raw images were binarized in the 
MATLAB environment (R2022b, MathWorks, USA), considering a local 
grey level threshold adjusted to the mean intensity of vicinity pixels. The 
overall level of porosity was quantified using the white-to-black pixels 
ratio. The image analysis was carried out on three different observation 
areas, representing a major part of the samples ’ cross-sections (⁓40 
mm
2
). The same images were also used to calculate the pore density 
(pore/mm
2
), size (equivalent diameter DE in μ m, (6)) and shape 
(circularity C without unit, (7)). To focus on the most impactful pores 
(from a mechanical property viewpoint), while considering limitations 
related to the measurement resolution (1 px = 2.5 μ m), all the pores 
smaller than DE = 20 μ m were removed from the analysis. Of note, the 
contribution of these pores to the overall porosity was negligible, since 
Table 2 
List of metrics extracted from the rheometer FT4 analysis and their subsequent 
influence on the powder flowability.
Testing 
mode
Metrics Interpretation
Dynamic flow
Basic Flow Energy 
( BFE , mJ)
Represents the resistance to flow in 
confined environment
Specific Energy 
( SE , mJ/g)
Indicates how powder will flow in an 
unconfined environment and provides 
an indication about the shear forces 
acting between particles
Bulk Density 
( BD , g/cm
3
)
Represents the bulk density of the 
conditioned powder
Flow Rate Index 
( FRI , w. u.)
Represents the sensitivity of the 
powder to flow rate change
Aeration
Aeration Energy at 10 
mm/s air speed 
( AE
10
, mJ) Traduces the sensitivity to aeration
Aeration Ratio 
( AR , w. u.)
Compressibility
Compressibility Index 
( CI , %)
Measures the ability of the powder to 
become compacted when subjected to 
normal stresses (Packing ability)
Permeability
Pressure Drop 
( PD , mbar)
Measures the ease with which the 
powder will release air over a range of 
stress conditions
Shear
Cohesion coefficient 
( CC , kPa)
Represents the powder internal 
resistance to flow
Flow Function 
( FF , w. u.)
Measures the shear stress required to 
initiate flow in a consolidated powder
Table 3 
Variations of the two parameters sets (I and II) printed with a layer thickness of 
30 μ m.
Set Name Hatching 
Space 
( μ m)
Power 
(W)
Speed 
(mm/s)
Volumetric 
Energy 
Density (J/ 
mm
3
)
Build 
Rate 
(cm
3
/h)
I I-40 40 179 199 750 0.86
I-60 60 133
I-80 80 100
I-100 100 80
I-120 120 66
II II-40 40 180 375 400 1.62
II-60 60 250
II-80 80 188
II- 
100
100 150
II- 
120
120 125
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
4

## Page 5

they represented only ~5 % in terms of the cumulative pore surface 
area. 
Equivalent Diameter ( DE ) =
̅̅̅̅̅̅̅̅̅̅̅̅ ̅
4 Area
π
√
(6) 
Circularity ( C ) =
4 π Area
Perimeter
2
(7) 
The image-based density measurements were repeated on different 
cross-sections of the same sample and on different samples printed using 
identical parameters. These inter- and intra-part measurements 
demonstrated that the pore distributions in all the printed samples were 
relatively uniform, with only slight observable variations.
It should be noted that while the 2D image-based measurement 
technique used in this study provides only local information about 
process-induced porosity, it nevertheless represents a reasonable choice 
since no other porosity detection technique was found suitable for 
printed molybdenum. For example, the high density of molybdenum ( ρ 
= 10.22 g/cm
3
) limits the use of X-ray micro-computed tomography 
with this material. Also, printed density values measured using the 
Archimedes technique are frequently compromised by the presence of 
unmelted particles trapped inside the pores [ 59 , 60 ].
2.5. Crystallographic and microstructural analyses
The crystallographic structure of printed samples and traces of their 
potential oxidation were assessed using X-ray diffraction analysis 
(X ’ Pert3, Co source, Malvern Panalytical Ltd. – UK). A deeper investi -
gation of the oxidation of printed parts was realized using an IR spec -
troscope (LECO ON836, LECO Corp., USA). A WDS analysis using an 
Electron Probe Microanalyzer (EPMA) (JEOL JXA-8230, JEOL Ltd., 
Japan) was used to evaluate the Mo/Re composition ratio inside the 
printed parts.
The microstructural analyses were carried out on the z-y cross- 
sections of printed samples using a field emission scanning electron 
microscope (Hitachi SU-8230, Hitachi Ltd., Japan) equipped with an 
electron backscattered diffraction detector (EBSD) (e
 
Flash
HR
, Bruker, 
USA). Prior to the inspection, the polished mounted surfaces were ion 
milled with a Hitachi EM 4000 plus system (5 kV, 25 rpm, 15 min). The 
post-treatment of EBSD maps was carried out using the MATLAB MTEX 
library. From these maps, the grain size, orientation and distribution 
were extracted according to the E2627 – 13 ASTM standard [ 61 ]. In the 
present work, these metrics are described by analogy to the pore 
description, as the grain density (grain/mm
2
), size DE
g 
( μ m) and circu -
larity C
g 
(without unit). Additional data, such as the band contrast (BC) 
diagrams and the MacKenzie distributions are also plotted to reveal the 
presence of substructures and defects. Two subgroups of structural ele -
ments are defined depending on the misorientation angle measured, the 
low angle grain boundaries (LAGB) structural elements, considering the 
angle range between 2 and 10
◦
, and the high angle grain boundaries 
(HAGB) structural elements with angles greater than 10
◦
. These 
substructural elements are quantified using their density values ( μ m
 1
) 
calculated as a ratio of the LAGB and HAGB lengths to the total indexed 
area.
2.6. Mechanical properties
Room-temperature compression testing of the specimens in their as- 
built state was realized in conformity with E9 – 09 ASTM standard [ 62 ] 
using an Alliance RF/200 testing machine (MTS, Eden Prairie, MN, USA) 
and 0.01 mm/s compression rate. The force applied during testing was 
measured by a 200 kN MTS load cell and the displacement monitored 
using an LVDT. From the strain-stress diagrams plotted, the following 
metrics were extracted: the maximum stress reached during the test 
(Ultimate Compression Strength, UCS, MPa), the yield stress (Yield 
Strength, YS, MPa), calculated at 0.2 % on the strain axis, and the strain 
under maximum load ( δ , %). For each testing temperature, three sam -
ples were tested. The compression failure mode was monitored and 
recorded using a camera located in front of the sample.
High temperature compression testing (600, 800 and 1000 
◦
C) was 
realized on an MTS 810 testing machine (MTS, Eden Prairie, MN, USA), 
under argon-controlled atmosphere (flow rate of 27.5 ft
3
/h). The force 
applied was measured by a 100 kN MTS load cell and the displacement 
monitored by an LVDT. The compression rate was set to 0.075 mm/min 
according to the E209 – 18 ASTM standard [ 63 ]. An infrared furnace, 
regulated by a K-type thermocouple, was used to control the tempera -
ture during the test. Prior to testing, the sample was heated up (stress- 
free) to the test temperature with a 10 
◦
C/min rate, while monitoring 
temperature in the core of the sample. This allowed to define a dwell 
time of 3 min to ensure that the temperature at the sample core corre -
sponded to a preset value. For each testing temperature, three samples 
were tested. The mechanical properties obtained at room and elevated 
temperatures were then compared to their best equivalents reported in 
the previous study on LPBF of pure molybdenum powders [ 57 ].
3. Results
3.1. Elaboration and characterization of the Mo8Re powder
3.1.1. Morphological and chemical analyses
Fig. 2 shows SEM images of the alloyed powder at different stages of 
its preparation. After mechanical blending and APR reduction ( Fig. 2 a), 
the feedstock retains an irregular morphology (S
BET 
= 0.4 m
2
/g) of the 
raw molybdenum powder used. Adding rhenium slightly increases the 
powder density ( ρ = 10.5 g/cm
3
). The local EDS analysis ( Table 4 ) 
realized on the particle surface highlighted an excessive amount of 
rhenium as compared to the targeted composition, meaning that 
rhenium agglomerated on the Mo particle surfaces during the reduction 
process. This observation demonstrated that the temperature (800 
◦
C) 
used was sufficient to reduce the rhenium precursor but too low to ho -
mogenize the chemical composition of the powder.
Following the plasma spheroidization process ( Fig. 2 b), the alloyed 
Fig. 1. a) Schematic representation of a printed specimen with samples for structural analyses and mechanical testing; b) Pineapple artifact with design features.
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
5

## Page 6

powder exhibits the typical spheroidal morphology expected for the 
LPBF process, resulting in a markedly reduced specific surface (S
BET 
=
0.08 m
2
/g). Observations revealed the presence of a limited number of 
satellite particles having irregular morphologies. However, the powder 
itself displayed a predominantly circular morphology, much like that of 
the reference 99.9 % Mo molybdenum powder ( Fig. 2 c). According to 
the granulometry measurements ( Fig. 2 d), the alloyed Mo8Re powder 
has a slightly larger particle size distribution as compared to its pure 
molybdenum counterpart.
The EDS analyses realized on the Mo
–
Re spheroidized powder 
( Table 4 ) demonstrate the effectiveness of this step in enhancing the 
homogeneity of the chemical composition. The reported rhenium con -
tent is significantly lower and closer to the targeted proportion (~8 % 
wt), than in the Mo
–
Re blend, proving that rhenium which was initially 
concentrated on the surface is now distributed throughout the volume of 
the molybdenum particles. This observation is supported by the XRD 
diffractograms ( Fig. 3 ) and the crystalline patterns identified at each 
step. After blending, two crystalline structures (Mo, bcc, ICDD 00 – 042- 
1120); Re, hcp, ICDD 00 – 005-0702) are detected, while after the 
spheroidizing step, only the cubic structure of molybdenum is indexed. 
According to the Mo
–
Re phase diagram [ 64 ], such a reduced amount of 
rhenium can be accommodated inside the molybdenum crystalline lat -
tice and form a solid solution. Note that introducing a larger element 
(such as rhenium) inside the molybdenum cubic structure reduces the 
interplanar distance and induces a slight shift towards larger angles, as 
observed in Fig. 3 . A simple comparison of this displacement was made 
with the only Mo
0.92
Re
0.08 
crystallographic reference available (ICDD 
04 – 001-9280), and suggests a slightly reduced rhenium content 
compared to the expected composition (8 %wt). No further qualitative 
estimation through the Rietveld refinement was performed. Moreover, 
irregular satellite particles retained an excessive amount of rhenium on 
their surface. The standard deviation obtained for the EDS measure -
ments made on these particles is significant, highlighting the lack of 
homogeneity of these satellites. According to these observations, the 
satellite particles were probably not entirely melted by the flame, 
meaning that the plasma spheroidization process parameters described 
in Table 1 can still be optimized.
Regarding the final oxygen reduction step, the infrared spectroscopy 
measurements reaching below 100 ppm ( Table 4 ), indicate a significant 
decrease in the residual oxygen content. This is beneficial for preventing 
the oxygen segregation issues at the GB, which are frequently reported 
for refractories.
Fig. 2. Scanning electron microscope images: a) Mo8Re powder after mechanical blending, b) Mo8Re after plasma spheroidization, c) Pure Mo used as reference, d) 
Particle size distributions of both spheroidized powders (Mo8Re and pure Mo).
Table 4 
Chemical composition (Mo and Re: EDS, O: IR), morphology and physical properties of the pure and alloyed molybdenum powders.
Powder Chemical composition (%wt) Morphology Physical properties
Mo Re O (ppm) S
BET 
(m
2
/g) d
10 
( μ m) d
50 
( μ m) d
90 
( μ m) He pycno (g/cm
3
)
Mo 99.9 * / < 500 * / 19.5 29.7 42.1 10.2
Mo-Re Blend 67.1 ± 1.3 32.9 ± 1.3 198 0.4 / 10.5
Mo-Re Spheroidized (round) 92.4 ± 2.5 7.6 ± 2.5
84 0.08 28.7 39.4 55.5 10.5
Mo-Re Spheroidized (satellite) 71.6 ± 16.0 28.4 ± 16.0
*
Commercial data.
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
6

## Page 7

3.1.2. Flowability and suitability for the LPBF process
The of powder flowability measurements using a Hall flowmeter 
funnel demonstrate the benefits of the spheroidization process as it di -
vides the required flow time (50 g) by two, between the blended and the 
spheroidized powders ( Table 5 ). The Hall measurement results of both 
spheroidized powders, pure Mo and alloyed Mo8Re, are in the same 
order of magnitude.
The rheological testing made with a FT4 rheometer demonstrates 
that overall, the two powders are non-cohesive ( Table 5 ). The aeration 
tests and the resulting elevated aeration ratio ( AR > 20) show that air 
easily breaks the weak cohesive forces between the particles. This 
behavior is corroborated by the cohesive coefficient ( CC ) obtained with 
the shear tests, which is close to or less than 1. Note that the comparison 
of these metrics for the two powders highlights that the alloyed Mo8Re 
powder ( AR = 45, CC = 1.3) is more cohesive than its Mo competitor 
( AR = 102, CC = 0.33). The flow function ( FF ) values measured during 
the shear tests, reinforce this conclusion, since this value is greater for 
pure Mo powder ( FF = 12.5, i.e., the free-flowing powder category) than 
for the alloyed Mo8Re powder ( FF = 5.4, i.e., the limited-to-easy powder 
flowing category).
The flow rate index ( FRI ) measured through the dynamic flow tests is 
close to unity for both powders (Mo 1.1 and Mo8Re 1.2), meaning that 
they are insensitive to flow rate variations. A low level of the aeration 
energy AE and the constant pressure drop lead to a similar conclusion 
about an excellent sphericity of particles of both powders. Slightly larger 
particles of the alloyed powder ( Fig. 2 c) result in a lower pressure drop 
( PD ) during permeability testing as compared to their pure Mo equiva -
lents. Next, Fig. 4 a presents the results of the stability test obtained from 
the dynamic flow testing mode. Both powders exhibit unstable, but 
opposite behavior: a decrease in the total energy value observed with the 
pure Mo powder can be characteristic of deagglomeration, while an 
increase in this value in the Mo8Re powder can rather be linked to 
agglomeration, segregation moisture uptake or de-aeration.
Finally, the rheological properties measurements retained to calcu -
late the AMS of the two powders are summarized in Table 5 and Fig. 4 b 
shows a radar graph representing all metrics used to calculate the AMS 
value. Since the AMS values of two powders show less than a 6 % dif -
ference, they should not manifest any significant differences in terms of 
their spreading capacities and powder bed densities.
3.2. Density and porosity analyses
Fig. 5 presents the printed density as a function of the h / t ratio. All 
the process parameters tested led to a density higher than 95 % with a 
maximum at 98 %. No significant differences were observed between the 
two tested VED-BR sets and a slight increase in density was noticed 
around h / t = 3.3. Based on these results, two parameter sets were 
retained, the first one leading to the best measured density of the alloyed 
powder (II-100) and the second set (II-80) having the same density as the 
highest-density pure molybdenum samples obtained in the previous 
study, i.e., ~97 %. The latter comparison is intended to isolate the 
impact of 8 % rhenium addition on the material microstructure from 
that on the printed density. The binarized images of these two samples 
are shown in Fig. 5 b,c with the related information about pore pop -
ulations. Note no clear tendency was observed with any of the pore- 
related metrics with respect to the process parameters. The pores pop -
ulation was evaluated in the [15;45] p/mm
2 
range, with a median 
circularity C50
p 
= [0.60;0.75] and a median pore size DE50
p 
= [35;50] 
μ m.
3.3. Crystalline phases and microstructure
XRD analyses (no shown in this paper) were performed on samples 
just after their printing and only the bcc phase of pure molybdenum was 
revealed, with no traces of oxidation that may have occurred during the 
fabrication process. Further analyses were conducted on the polished 
surface using WDS to gauge the rhenium behavior in the molybdenum 
matrix and more precisely detect any oxidation signs. As presented in 
Figure 6abc, the samples are homogeneous, and rhenium did not 
segregate and was well diffused in the molybdenum matrix. The WDS 
analyses show an average rhenium content close to the nominal value 
regardless of the printing parameters used (II-80 Re wt% = 7.8 ± 0.3, II- 
100 Re wt% = 8.3 ± 0.4). Regarding the residual oxygen content after 
printing, the IR spectroscopy measurements made on the denser sample 
(II-100) highlight a significant increase in the oxygen content inside 
printed parts (875 ± 210 ppm) as compared to the initial proportion 
inside the spheroidized powder ( Table 4 ). The EBSD analyses were then 
carried out and the BC maps plotted, with the latter revealing no sig -
nificant differences between the two samples. They were both relatively 
Fig. 3. XRD diffractograms of the alloyed powder at different steps of the 
process and of pure molybdenum used for the reference study [ 57 ].
Table 5 
Powder rheological characteristics (Hall flow and FT4 rheometer).
Powders Hall flow FT4 Rheometer
Flowability (s/50 g) BD 
(g/cm
3
)
CI (%) 
at 15 kPa
PD 
(mBar) 
at 15 kPa
SE 
(mJ/g)
AE
10 
(mJ)
BFE 
(mJ)
CC 
(kPa)
AMS
Mo8Re 
(This study)
38.7 (Blend) 
13 (Atom.)
5.16 ( ± 0.99 %) 3.48 ( ± 12.30 %) 2.51 ( ± 14.10 %) 3.35 ( ± 4.24 %) 24.50 ( ± 12.10 %) 1110 ( ± 3.81 %) 1.30 164
Mo 
[ 57 ]
< 15 * 6.04 ( ± 0.47 %) 7.65 ( ± 6.57 %) 8.31 ( ± 8.51 %) 2.53 ( ± 2.65 %) 10.60 ( ± 6.21 %) 1084 ( ± 1.23 %) 0.33 159
*
Commercial data.
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
7

## Page 8

light-colored, which correspond to good quality patterns and indicate 
that no defects nor internal stresses were detected. Note that in Fig. 6 d, 
one of these maps is presented with a superposed bcc molybdenum 
phase map (uniformity of color proves a single-phase state of the ma -
terial). These observations were confirmed by their corresponding sta -
tistical distributions ( Fig. 6 e) which revealed only one peak at BC = 160, 
suggesting the presence of only one phase associated with molybdenum 
(Cubic, Im-3 m, 229), which is consistent with the extracted phase map 
( Fig. 6 d), XRD and WDS analyses.
Also from the EBSD analyses, the MacKenzie plots of the misorien -
tation angles ( Fig. 7 a) were analyzed and associated with those of a 
conventional polycrystalline cubic material having a random texture 
[ 65 ], which was confirmed by the IPF maps ( Fig. 7 b) and the pole figures 
( Fig. 7 c). These diagrams also revealed a significant population of 
structural elements with small misorientation angles (LAGB, < 10
◦
), 
thus reflecting the presence of substructures accommodated by arrays of 
dislocations. Finally, no significant differences were found in the LAGB 
and HAGB densities of both Mo8Re samples ( Table 6 ). However, the 
grain density of the Mo8Re 97 %-density samples was found higher and 
coinciding with smaller grains and a greater porosity as compared to 
their Mo8Re 98 %-density equivalents. However, compared to the pure 
molybdenum samples, the LAGB and HAGB densities of the Mo8Re 
Fig. 4. a) Stability test plots and b) Additive Manufacturing Suitability ( AMS ) radar chart for pure Mo and alloyed Mo8Re powders.
Fig. 5. a) Measured printed densities as functions of the h /t ratio for the two VED-BR sets; Examples of the binarized surfaces of the samples b) II-80 and c) II-100.
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
8

## Page 9

samples were 1.5 to 2 times higher, and this increase in boundary 
densities was accompanied by a 15 to 20 % decrease in the grain size.
3.4. Mechanical testing at room and elevated temperatures
Fig. 8 a presents the ultimate compressive strength as a function of 
the testing temperature for the 97 % and 98 % density Mo8Re samples 
and their reference 97 %-density pure molybdenum counterparts. At 
room temperature, both Mo8Re samples show lower strength values 
than their molybdenum counterparts, and the higher the printed den -
sity, the higher the mechanical strength. However, at elevated temper -
atures, the strength values of two alloyed samples were higher than 
those of the molybdenum samples. It should be noted that the degree of 
oxidation of the alloyed and unalloyed samples during testing at 
elevated temperatures was equivalent, as witnessed by their mass loss 
(~4 % at 800 
◦
C and ~ 6 % at 1000 
◦
C). Of note, contrary to the 98 
%-density Mo8Re samples, 97 %-density Mo8Re samples presented the 
same non-monotonic temperature evolution of strength as their pure 
molybdenum counterparts (aging-related increase in strength at around 
800 
◦
C [ 66 , 67 ]). This difference in the temperature-related behavior is 
illustrated by the stress-strain diagrams shown in Fig. 8 b,c and 
comparing the highest-density (98 %) Mo8Re samples with their 
highest-density (97 %) pure Mo counterparts.
Regarding the strain under maximum load, no significant differences 
were observed for the alloyed samples when varying the testing tem -
perature, nor between the 98 %-density and the 97 %-density Mo8Re 
samples. Indeed, as listed in Table 7 , the strain under maximum load of 
the alloyed samples varied from 4 to 7 %, following no particular trend, 
and representing half that of pure molybdenum. All the mechanical 
properties (YS, UCS and δ ) extracted from these compressive tests, are 
summarized in Table 7 .
3.5. Artifacts
The complex pineapple-shaped structure was successfully printed in 
two different formats, measuring 4 and 2 cm in height, respectively. The 
smallest version is not a simple downsizing of the larger one, but rather, 
a geometric adaptation. Indeed, the leaves in the shorter one are of a 
shorter stature, with a restricted area allocated to fine letters. However, 
the lattice strut size of both formats remains almost identical (respec -
tively 680 and 650 μ m). No discontinuity was observed at the transition 
zone between the dense lower part and the lattice structure ( Fig. 9 a). 
With regards to the self-supported leave structures (angle = 45
◦
), they 
were correctly printed throughout their height. On the smaller structure, 
the text was downsized to fit the available area, and distinguishable fine 
letters were printed with a minimal thickness going down to 250 μ m 
( Fig. 9 b).
4. Discussions
4.1. Printability of the alloyed Mo8Re powder
Among the various prints realized with pure Mo and alloyed Mo8Re 
powders, a slight difference in terms of spreading behavior was 
observed. Both powders were found suitable for the LPBF process, 
exhibiting good flowability and spreading properties that enabled to 
obtain a highly dense powder bed. However, the alloyed Mo8Re powder 
appeared to be more sensitive to its environment and prone to 
agglomeration. Indeed, during printing preparation, it was observed 
that large agglomerates were formed inside the Mo8Re powder 
container. They were easily breakable during the powder loading by 
slight agitation inside the supply chamber and did not impact the quality 
of the powder spread over the baseplate ( Fig. 10 a). The agglomerates 
Fig. 6. WDS mapping of the II-100 (98 %) sample: a) polished surface, b) molybdenum and c) rhenium distributions; d) Superposition of the Band Contrast (BC) and 
bcc molybdenum phase maps of the II-100 (98 %) sample; e) BC cumulative histograms of the two retained samples (II-80 (97 %) and II-100 (98 %)).
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
9

## Page 10

were also clearly visible during the unloading of the printer ( Fig. 10 b). 
Moreover, blue color traces were observed inside the unsealed con -
tainers not used for extended periods of time, evidencing the powder ’ s 
sensitivity to humidity. This color is correlated with the water dissolu -
tion of traces of molybdenum oxide (MoO
3
) ( Fig. 10 c). This sensitivity to 
humidity and propensity to agglomeration were not observed for pure 
Mo powders. Overall, the aforementioned printing behavior of the 
Mo8Re and Mo powders was in agreement with the conclusions of the 
rheological measurements ( CC , AE ) described in Section 3.1.2 .
4.2. Impact of the 8 wt% rhenium addition on the printed density and 
chemistry
It was observed in this work that adding 8 wt% of rhenium increased 
the overall density of printed parts ( Fig. 5 ) as compared to those of pure 
molybdenum [ 57 ]. Indeed, for the same combinations of process pa -
rameters, the printed density range of the Mo8Re parts (96 – 98 %) is 
higher and narrower than that of the pure Mo parts (89 – 97 %). Since it is 
a known fact that the rhenium addition [ 68 ], even in small proportions 
[ 69 ], enables to decrease the DBTT, and therefore increase the ductility 
of refractory metals, it may be hypothesized that this phenomenon was 
one of the main contributing factors to the enhanced densification 
during printing.
As far as the Re content is concerned, the literature highlighted the 
metastability of brittle phases in Mo
–
Re alloys ( σ [ 70 ] or χ ), especially 
for high rhenium contents and processes involving high cooling rates 
[ 71 ]. Consequently, the production of high rhenium-containing powders 
and the use of these powders for 3D printing could be challenging as 
both processes, plasma atomization and LPBF, involve high cooling 
rates. In our study, a relatively small rhenium addition was homoge -
neously accommodated inside the bcc crystallographic structure of 
molybdenum, in agreement with the Mo
–
Re phase diagram [ 64 ]. This 
excellent solid solubility of Re in Mo led to a final chemical composition 
close to the nominal value ( ≈ 8 wt%) regardless of the printing pa -
rameters (see Section 3.3 ).
It is reasonable to assert that even higher printed densities can be 
obtained provided both the Re content and the LPBF conditions are 
optimized. However, the amount of data on the additive manufacturing 
of Mo
–
Re alloys actually available is insufficient to allow to propose an 
optimal rhenium content for these compounds. This is especially true 
because of the multitude of factors impacting the densification behavior 
and the cracking susceptibility of refractory alloys during their laser 
powder bed fusion.
Fig. 7. a) MacKenzie plots of Mo8Re (97 %) and Mo8Re (98 %) samples; b) orientation map (IPF Y) and c) pole figures of a Mo8Re (98 %) sample.
Table 6 
Boundary densities, grain density, size and circularity of the two Mo8Re samples 
retained and the pure molybdenum from the reference work.
Sample LAGB 
( μ m
 1
)
HAGB 
( μ m
 1
)
Grain density 
(g/mm
2
)
DE90
g 
( μ m)
C90
g
Mo8Re (98 %) 0.12 0.062 654 85 0.7
Mo8Re (97 %) 0.10 0.067 804 80 0.65
Mo (97 %) 0.06 0.044 278 100 0.7
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
10

## Page 11

4.3. Microstructure
In conventional powder metallurgy, it was observed that a rhenium 
addition contributes to a refinement of the microstructure and increases 
the recrystallization temperature of refractory alloys. In fact, a NASA 
technical report [ 69 ] showed that for the same manufacturing and post- 
treatment conditions, Mo
–
14Re (wt%) parts exhibited a finer micro -
structure than their pure molybdenum equivalents. Similar observations 
related to rhenium alloying have also been reported for LPBF Mo
–
Re 
alloys with respect to the grain refinement [ 39 ] and texture evolution 
[ 26 ]. However, these effects have thus far only been reported for sam -
ples printed using rhenium contents greater than 25 wt%.
When comparing the microstructure of the Mo8Re (actual work) and 
Mo [ 57 ] samples printed using the same sets of printing parameters (II- 
80 or II-100 in Table 3 , P = 180 W, v = 188 or 150 mm/s, h = 80 or 100 
μ m, t = 30 μ m), it can be concluded that even a relatively small addition 
of rhenium, such as that in this study (8 wt%), also results in micro -
structure refinement: (II-80: 105 μ m (Mo) to 80 μ m (Mo8Re) and II-100: 
125 μ m (Mo) to 85 μ m (Mo8Re). For the other microstructural features, 
neither the columnar aspect nor the texture, seem to be affected by 
adding rhenium, regardless of the printing parameters used.
4.4. Mechanical properties
Alloying of Mo with Re has been proven efficient in strongly 
increasing the mechanical properties at room temperature, as 
Fig. 8. a) Evolution of the Ultimate Compression Strength as a function of the testing temperature; b) Typical stress-strain curves at all tested temperatures for b) 
Mo8Re (98 %) and c) Mo (97 %) samples.
Table 7 
Mechanical properties in compression at room and elevated temperatures.
Sample Temperature (
◦
C) YS (MPa) UCS (MPa) δ (%)
Mo8Re (98 %)
20 303 ± 30 460 ± 31 7 ± 1.3
600 206 ± 8 339 ± 1 4 ± 0.5
800 186 ± 10 302 ± 20 4 ± 0.3
1000 119 ± 28 193 ± 31 6 ± 0.6
Mo8Re (97 %)
20 256 ± 2 416 ± 22 7 ± 0.8
600 205 ± 28 317 ± 19 4 ± 1.2
800 206 ± 8 335 ± 6 4 ± 0.6
1000 119 ± 4 182 ± 11 6 ± 0.1
Mo (97 %)
20 340 ± 20 500 ± 15 11 ± 1
600 150 ± 20 240 ± 30 8 ± 1
800 160 ± 5 260 ± 8 14 ± 1
1000 90 ± 10 150 ± 18 9 ± 4
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
11

## Page 12

demonstrated by compression testing of Mo-47.5wt%Re LPBF samples 
in [ 26 ]. An enhancement of the mechanical strength of alloyed LPBF 
parts as compared to their pure molybdenum equivalents has also been 
highlighted by flexural testing of MoRe samples with rhenium contents 
of 10 and 25 wt% [ 39 ]. In the latter study, parts with a lower rhenium 
concentration (5 wt%) were also tested, but showed lower mechanical 
properties at room temperature than their pure Mo counterparts. These 
findings align with the observations of the present study and can be 
attributed to the rhenium softening effect in MoRe alloys with lower Re 
contents described in [ 40 ]. Note that this softening effect in Mo-low Re 
content alloy specimens processed by powder sintering and hot radial 
forging was observed in their as-worked conditions only [ 72 ]. Heat 
treatments, such as stress relief and recrystallization annealing, led to 
microstructural changes (dislocation density reduction, grain 
coarsening, etc.), which suppressed the softening effect. A dedicated 
study on the impact of heat treatments of LPBF-processed molybde -
num ‑ rhenium specimens with low rhenium content on their mechanical 
properties is yet to be conducted.
To the best of the authors ’ knowledge, the effect of rhenium addition 
on the mechanical properties of additively manufactured molybdenum 
parts at elevated temperatures is yet to be addressed. However, the 
literature attests that the addition of rhenium, even in small proportions, 
improves the mechanical properties of conventionally-manufactured 
molybdenum parts. For example, [ 69 ], a progressive increase in 
rhenium content (from 7 to 14 at.%) enabled to increase the ultimate 
strength of hot isostatic pressed (HIP-ed) tensile specimens in the 980 to 
1650 
◦
C temperature range (almost a twofold increase for 14at% Re 
addition). A more recent study on powder metallurgy processed Mo42.5 
Fig. 9. a) Side view and b) inclined view of the pineapple artifacts printed using Mo8Re powder.
Fig. 10. a) Powder bed of Mo8Re during printing. b) Agglomerates of Mo8Re powders observed during the printer unloading. c) Unsealed containers for storing 
samplings of pure Mo and alloyed Mo8Re powders. A dark blue color observed on the surface of Mo8Re is correlated with that of molybdenum oxides dissolution in 
water. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
12

## Page 13

wt% Re parts [ 73 ] also showed a significant increase in the mechanical 
properties at temperatures of up to 1200 
◦
C. These observations are in 
line with those of this study, indicating an increase in the elevated 
temperature properties of MoRe alloys as compared to their Mo 
equivalents.
5. Conclusions
In this study, the spheroidization process was used to change the 
shape of particles from agglomerated granules to a powder with good 
particles sphericity and rheological properties suitable for the LPBF 
process. It also reduced the specific surface area (BET) of the powders by 
80 %, but according to pycnometric measurements, had no effect on the 
powder density. The chemical composition within individual particles 
was homogenized to an average of 8 % wt% of rhenium and was pre -
served and homogenously distributed in the molybdenum matrix after 
printing. The selected optimal set of printing parameters ( P = 180 W, v 
= 188 mm/s, h = 100 μ m and t = 30 μ m) led to the printing of crack-free 
specimens with a density of 98 %. Adding rhenium caused a decrease in 
both the compression strength and strain under maximum load at room 
temperature as compared to samples printed with pure Mo powders. 
However, it led to significantly higher mechanical properties in the 
600 – 1000 
◦
C temperature range (ultimate strength of 340 and 190 MPa 
at 600 and 1000 
◦
C, respectively). Finally, fine letter- and lattice- 
containing complex structures were successfully printed to demon -
strate the printability of these powders.
CRediT authorship contribution statement
Aurore Leclercq: Writing – original draft, Visualization, Software, 
Methodology, Investigation, Formal analysis, Data curation, Conceptu -
alization. Anna Czech: Writing – original draft, Visualization, Investi -
gation, Data curation. Thibault Mouret: Writing – original draft, 
Visualization, Software, Methodology, Investigation, Formal analysis, 
Data curation. Marcin Lis: Writing – original draft, Investigation, Data 
curation. Adriana Wrona: Supervision, Resources, Methodology. Vla -
dimir Brailovski: Writing – review & editing, Visualization, Validation, 
Supervision, Resources, Project administration, Methodology, Funding 
acquisition, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
The authors acknowledge the financial support provided by PRIMA 
Qu ´ebec (P ˆole de recherche et d ’ innovation en mat ´eriaux avanc ´es) in the 
framework of the M-ERA.NET program, NSERC (Natural Sciences and 
Engineering Research Council of Canada) and PyroGenesis Canada Inc.
Data availability
Data are contained within the article.
References
[1] R.A. Holmwood, R. Glang, Resistivity and temperature coefficient of pure 
molybdenum, J. Chem. Eng. Data 10 (2) (1965) 162 – 163, https://doi.org/ 
10.1021/je60025a028 .
[2] P. Rebesan, et al., Pure molybdenum manufactured by laser powder bed fusion: 
thermal and mechanical characterization at room and high temperature, Addit. 
Manuf. 47 (2021) 102277, https://doi.org/10.1016/j.addma.2021.102277 .
[3] P. Hidnert, W.B. Gero, Thermal expansion of molybdenum, Sci. Pap. Bur. Stand. 19 
(1924) 429, https://doi.org/10.6028/nbsscipaper.171 .
[4] H. Baker, Properties of metals, in: J.R. Davis (Ed.), Metals Handbook Desk Edition, 
2nd ed, ASM International, 1998, pp. 114 – 121, https://doi.org/10.31399/asm.hb. 
mhde2.a0003086 .
[5] Y.-J. Hwang, Y. Kim, S.-H. Park, S.-C. Park, K.-A. Lee, Wear and corrosion 
properties of pure Mo coating layer manufactured by atmospheric plasma spray 
process, Arch. Metall. Mater. (2024) 81 – 85, https://doi.org/10.24425/ 
amm.2024.147790 .
[6] H. Zhao, L. Xie, C. Xin, N. Li, B. Zhao, L. Li, Effect of molybdenum content on 
corrosion resistance and corrosion behavior of Ti-Mo titanium alloy in 
hydrochloric acid, Mater. Today Commun. 34 (2023) 105032, https://doi.org/ 
10.1016/j.mtcomm.2022.105032 .
[7] Plansee, Des M ´etaux Solides Pour des Produits Solides | Plansee [Online]. 
Available, https://www.plansee.com/www.plansee.com/fr.html , 2023.
[8] J. Wadsworth, T.G. Nieh, J.J. Stephens, Recent advances in aerospace refractory 
metal alloys, Int. Mater. Rev. 33 (1) (1988) 131 – 150, https://doi.org/10.1179/ 
imr.1988.33.1.131 .
[9] J.A. Shields Jr., Applications of Molybdenum Metal and Its Alloys, International 
Molybdenum Association, 2013 .
[10] D. Wang, C. Yu, J. Ma, W. Liu, Z. Shen, Densification and crack suppression in 
selective laser melting of pure molybdenum, Mater. Des. 129 (2017) 44 – 52, 
https://doi.org/10.1016/j.matdes.2017.04.094 .
[11] A. Talignani, et al., A review on additive manufacturing of refractory tungsten and 
tungsten alloys, Addit. Manuf. 58 (2022) 103009, https://doi.org/10.1016/j. 
addma.2022.103009 .
[12] A. Garcia-Colomo, D. Wood, F. Martina, S.W. Williams, A comparison framework 
to support the selection of the best additive manufacturing process for specific 
aerospace applications, Int. J. Rapid Manuf. 9 (2 – 3) (2020) 194 – 211, https://doi. 
org/10.1504/IJRAPIDM.2020.107736 .
[13] P. Gradl, et al., Robust metal additive manufacturing process selection and 
development for aerospace components, J. Mater. Eng. Perform. 31 (8) (2022) 
6013 – 6044, https://doi.org/10.1007/s11665-022-06850-0 .
[14] E. Pink, R.W. Armstrong, Total Material Variables Influencing DBTT for 
Molybdenum, Technical Report to Office Of Naval Research NR031 – 739 Vol. I, 
1970. Accessed: Jul. 22, 2024[Online]. Available, https://apps.dtic.mil/sti/pdfs 
/AD0713191.pdf .
[15] Y. Hiraoka, Significant effect of carbon content in the low-temperature fracture 
behavior of molybdenum, Mater. Trans. JIM 31 (10) (1990) 861 – 864, https://doi. 
org/10.2320/matertrans1989.31.861 .
[16] Y. Hiraoka, H. Kurishita, M. Narui, H. Kayano, Fracture and ductile-to-brittle 
transition characteristics of molybdenum by impact and static bend tests, Mater. 
Trans. JIM 36 (4) (1995) 504 – 510, https://doi.org/10.2320/ 
matertrans1989.36.504 .
[17] H. Xing, et al., Effects of oxygen on microstructure and evolution mechanism of 
body-centred-cubic molybdenum, Int. J. Refract. Met. Hard Mater. 103 (2022) 
105747, https://doi.org/10.1016/j.ijrmhm.2021.105747 .
[18] A. Ivekovi ´c, et al., Selective laser melting of tungsten and tungsten alloys, Int. J. 
Refract. Met. Hard Mater. 72 (2018) 27 – 32, https://doi.org/10.1016/j. 
ijrmhm.2017.12.005 .
[19] J. Braun, et al., Molybdenum and tungsten manufactured by selective laser 
melting: analysis of defect structure and solidification mechanisms, Int. J. Refract. 
Met. Hard Mater. 84 (2019) 104999, https://doi.org/10.1016/j. 
ijrmhm.2019.104999 .
[20] A.V. Müller, et al., Additive manufacturing of pure tungsten by means of selective 
laser beam melting with substrate preheating temperatures up to 1000 
◦
C, Nucl. 
Mater. Energy 19 (2019) 184 – 188, https://doi.org/10.1016/j.nme.2019.02.034 .
[21] N. Alinejadian, P. Wang, L. Kollo, K.G. Prashanth, Selective laser melting of 
commercially pure molybdenum by laser rescanning, 3D Print Addit. Manuf. 10 (4) 
(2023) 785 – 791, https://doi.org/10.1089/3dp.2021.0265 .
[22] B. Guan, et al., Strategies to reduce pores and cracks of molybdenum fabricated by 
selective laser melting, Int. J. Refract. Met. Hard Mater. 112 (2023) 106123, 
https://doi.org/10.1016/j.ijrmhm.2023.106123 .
[23] L. Kaserer, et al., Fully dense and crack free molybdenum manufactured by 
selective laser melting through alloying with carbon, Int. J. Refract. Met. Hard 
Mater. 84 (2019) 105000, https://doi.org/10.1016/j.ijrmhm.2019.105000 .
[24] N.E. Ellsworth, et al., Influence of Nano-sized SiC on the laser powder bed fusion of 
molybdenum, Crystals 12 (2022), https://doi.org/10.3390/cryst12091276 .
[25] J. Gan, et al., Research about the microcrack mechanisms in molybdenum and 
corresponding suppression strategies during laser additive manufacturing process, 
Materialia 36 (2024) 102173, https://doi.org/10.1016/j.mtla.2024.102173 .
[26] F. Oehlerking, M.T. Stawovy, S. Ohm, A. Imandoust, Microstructural 
characterization and mechanical properties of additively manufactured 
molybdenum and molybdenum alloys, Int. J. Refract. Met. Hard Mater. 109 (2022) 
105971, https://doi.org/10.1016/j.ijrmhm.2022.105971 .
[27] D. Wang, Z. Wang, K. Li, J. Ma, W. Liu, Z. Shen, Cracking in laser additively 
manufactured W: initiation mechanism and a suppression approach by alloying, 
Mater. Des. 162 (2019) 384 – 393, https://doi.org/10.1016/j.matdes.2018.12.010 .
[28] M. Guo, K. Liu, J. Sun, D. Gu, Laser powder bed fusion of a novel nano-modified 
tungsten alloy with refined microstructure and enhanced strength, Mater. Sci. Eng. 
A 843 (2022) 143096, https://doi.org/10.1016/j.msea.2022.143096 .
[29] T. Takida, H. Kurishita, M. Mabuchi, T. Igarashi, Y. Doi, T. Nagae, Mechanical 
properties of fine-grained, sintered molybdenum alloys with dispersed particles 
developed by mechanical alloying, Mater. Trans. 45 (1) (2004) 143 – 148, https:// 
doi.org/10.2320/matertrans.45.143 .
[30] P. Hu, et al., Preparation and ductile-to-brittle transition temperature of the La- 
TZM alloy plates, Int. J. Refract. Met. Hard Mater. 52 (2015) 131 – 136, https://doi. 
org/10.1016/j.ijrmhm.2015.05.006 .
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
13

## Page 14

[31] J. Xu, et al., Enhanced strength and ductility of laser powder bed fused NbMoTaW 
refractory high-entropy alloy via carbon microalloying, Addit. Manuf. Lett. 3 
(2022) 100079, https://doi.org/10.1016/j.addlet.2022.100079 .
[32] T. Ron, et al., Synthesis of refractory high-entropy alloy WTaMoNbV by powder 
bed fusion process using mixed elemental alloying powder, Materials 15 (2022), 
https://doi.org/10.3390/ma15124043 .
[33] L. Kaserer, et al., Microstructure and mechanical properties of molybdenum- 
titanium-zirconium-carbon alloy TZM processed via laser powder-bed fusion, Int. 
J. Refract. Met. Hard Mater. 93 (2020) 105369, https://doi.org/10.1016/j. 
ijrmhm.2020.105369 .
[34] L. Kaserer, et al., Molybdenum alloy Mo-Ti-Zr-C adapted for laser powder bed 
fusion with refined isotropic microstructure and excellent high temperature 
strength, Int. J. Refract. Met. Hard Mater. 113 (2023) 106174, https://doi.org/ 
10.1016/j.ijrmhm.2023.106174 .
[35] T. Leonhardt, J.-C. Carl ´en, M. Buck, C.R. Brinkman, W. Ren, C.O. Stevens, 
Investigation of mechanical properties and microstructure of various molybdenum- 
rhenium alloys, AIP Conf. Proc. 458 (1) (1999) 685 – 690, https://doi.org/10.1063/ 
1.57638 .
[36] T. Yamamoto, M. Hara, Y. Hatano, Cracking behavior and microstructural, 
mechanical and thermal characteristics of tungsten – rhenium binary alloys 
fabricated by laser powder bed fusion, Int. J. Refract. Met. Hard Mater. 100 (2021) 
105651, https://doi.org/10.1016/j.ijrmhm.2021.105651 .
[37] J. Li, Y. Wu, L. Xue, Z. Wei, Laser powder bed fusion in-situ alloying of refractory 
WTa alloy and its microstructure and mechanical properties, Addit. Manuf. 67 
(2023) 103493, https://doi.org/10.1016/j.addma.2023.103493 .
[38] R.H. Cooper Jr., E.E. Hoffman, Refractory Alloy Technology for Space Nuclear 
Power Applications, Oak Ridge National Laboratory and U.S Department of Energy 
oak Ridge Operations, Oak Ridge, Tennessee, USA, 1984. CONF-8308130; ON: 
DE84001745 .
[39] C.C. Eckley, et al., Evaluating molybdenum-rhenium alloys through additive 
manufacturing, JOM 75 (6) (2023) 1928 – 1940, https://doi.org/10.1007/s11837- 
023-05813-7 .
[40] J.R. Stephens, W.R. Witzke, Alloy softening in group via metals alloyed with 
rhenium, J. Common Met. 23 (4) (1971) 325 – 342, https://doi.org/10.1016/0022- 
5088(71)90043-9 .
[41] N.R. Philips, M. Carl, N.J. Cunningham, New opportunities in refractory alloys, 
Metall. Mater. Trans. A 51 (7) (2020) 3299 – 3310, https://doi.org/10.1007/ 
s11661-020-05803-3 .
[42] A.C. Field, L.N. Carter, N.J.E. Adkins, M.M. Attallah, M.J. Gorley, M. Strangwood, 
The effect of powder characteristics on build quality of high-purity tungsten 
produced via laser powder bed fusion (LPBF), Metall. Mater. Trans. A 51 (3) (2020) 
1367 – 1378, https://doi.org/10.1007/s11661-019-05601-6 .
[43] X. Liu, K. Wang, P. Hu, Q. Chen, A.A. Volinsky, Spheroidization of molybdenum 
powder by radio frequency thermal plasma, Int. J. Miner. Metall. Mater. 22 (11) 
(2015) 1212 – 1218, https://doi.org/10.1007/s12613-015-1187-7 .
[44] Z. Hao, et al., Spheroidization of a granulated molybdenum powder by radio 
frequency inductively coupled plasma, Int. J. Refract. Met. Hard Mater. 82 (2019) 
15 – 22, https://doi.org/10.1016/j.ijrmhm.2019.03.023 .
[45] S. Qiu, B.K. Chen, C.S. Xiang, Preparation and properties of spherical Mo powders 
by plasma rotating electrode process for additive manufacturing, Mater. Sci. Forum 
993 (2020) 391 – 397, https://doi.org/10.4028/www.scientific.net/MSF.993.391 .
[46] F. Hinrichs, et al., Flexible powder production for additive manufacturing of 
refractory metal-based alloys, Metals 11 (2021), https://doi.org/10.3390/ 
met11111723 .
[47] B. Ba ł asz, M. Bielecki, W. Gulbi ´nski, Ł . S ł oboda, Comparison of ultrasonic and 
other atomization methods in metal powder production, J. Achiev. Mater. Manuf. 
Eng. 116 (1) (2023) 11 – 24, https://doi.org/10.5604/01.3001.0016.3393 .
[48] T. Fedina, J. Sundqvist, J. Powell, A.F.H. Kaplan, A comparative study of water and 
gas atomized low alloy steel powders for additive manufacturing, Addit. Manuf. 36 
(2020) 101675, https://doi.org/10.1016/j.addma.2020.101675 .
[49] K. Kassym, A. Perveen, Atomization processes of metal powders for 3D printing, 
Mater. Today Proc. 26 (2020) 1727 – 1733, https://doi.org/10.1016/j. 
matpr.2020.02.364 .
[50] S.Z. Soong, W.L. Lai, A.N. Kay Lup, Atomization of metal and alloy powders: 
processes, parameters, and properties, AICHE J. 69 (11) (2023) e18217, https:// 
doi.org/10.1002/aic.18217 .
[51] T. Majewski, Research of Spheroidization processes of W-re powders, Solid State 
Phenom. 199 (2013) 490 – 495, https://doi.org/10.4028/www.scientific.net/ 
SSP.199.490 .
[52] A. Wrona, et al., Ni – Cr powders modified with rhenium as a novel coating 
material — physical properties, microstructure, and behavior in plasma plume, 
Materials 15 (2022), https://doi.org/10.3390/ma15113844 .
[53] J. Tang, et al., Reaction mechanism and process control of hydrogen reduction of 
ammonium Perrhenate, Metals 10 (2020), https://doi.org/10.3390/met10050640 .
[54] F.R. Caliari, F.S. Miranda, D.A.P. Reis, G.P. Filho, L.I. Charakhovski, 
A. Essiptchouk, Plasma torch for supersonic plasma spray at atmospheric pressure, 
J. Mater. Process. Technol. 237 (2016) 351 – 360, https://doi.org/10.1016/j. 
jmatprotec.2016.06.027 .
[55] R. Freeman, Measuring the flow properties of consolidated, conditioned and 
aerated powders — a comparative study using a powder rheometer and a 
rotational shear cell, Powder Technol. 174 (1) (2007) 25 – 33, https://doi.org/ 
10.1016/j.powtec.2006.10.016 .
[56] R. Freeman, X. Fu, Characterisation of powder bulk, dynamic flow and shear 
properties in relation to die filling, Powder Metall. 51 (3) (2008) 196 – 201, https:// 
doi.org/10.1179/174329008X324115 .
[57] A. Leclercq, T. Mouret, V. Brailovski, Laser powder bed fusion of molybdenum: 
density, structure and mechanical properties at room and elevated temperatures, 
Mater. Sci. Eng. A (2025) 148004, https://doi.org/10.1016/j.msea.2025.148004 .
[58] S.E. Brika, M. Letenneur, C.A. Dion, V. Brailovski, Influence of particle morphology 
and size distribution on the powder flowability and laser powder bed fusion 
manufacturability of Ti-6Al-4V alloy, Addit. Manuf. 31 (2020) 100929, https://doi. 
org/10.1016/j.addma.2019.100929 .
[59] C. Tan, K. Zhou, W. Ma, B. Attard, P. Zhang, T. Kuang, Selective laser melting of 
high-performance pure tungsten: parameter design, densification behavior and 
mechanical properties, Sci. Technol. Adv. Mater. 19 (1) (2018) 370 – 380, https:// 
doi.org/10.1080/14686996.2018.1455154 .
[60] A. Leclercq, V. Brailovski, Improving laser powder bed fusion printability of 
tungsten powders using simulation-driven process optimization algorithms, 
Materials 17 (2024), https://doi.org/10.3390/ma17081865 .
[61] E04 Committee, Practice for Determining Average Grain Size Using Electron 
Backscatter Diffraction (EBSD) in Fully Recrystallized Polycrystalline Materials, 
E2627, 2025, https://doi.org/10.1520/E2627-13R19 .
[62] Test Methods of Compression Testing of Metallic Materials at Room Temperature, 
E9 – 09, 2025, https://doi.org/10.1520/E0009-09 .
[63] E28 Committee, Practice for Compression Tests of Metallic Materials at Elevated 
Temperatures With Conventional or Rapid Heating Rates and Strain Rates, 2025, 
https://doi.org/10.1520/E0209-18 .
[64] H. Okamoto, Mo-Re (Molybdenum-Rhenium), J. Phase Equilib. Diffus. 31 (6) 
(2010) 580 – 581, https://doi.org/10.1007/s11669-010-9787-4 .
[65] J.K. Mason, C.A. Schuh, The generalized Mackenzie distribution: disorientation 
angle distributions for arbitrary textures, Acta Mater. 57 (14) (2009) 4186 – 4197, 
https://doi.org/10.1016/j.actamat.2009.05.016 .
[66] R.P. Carreker, R.W. Guard, Tensile deformation of molybdenum as a function of 
temperature and strain rate, JOM 8 (2) (1956) 178 – 184, https://doi.org/10.1007/ 
BF03377669 .
[67] A.H. Cottrell, B.A. Bilby, Dislocation theory of yielding and strain ageing of Iron, 
Proc. Phys. Soc. Sect. A 62 (1) (1949) 49 – 62, https://doi.org/10.1088/0370-1298/ 
62/1/308 .
[68] W.D. Klopp, Review of Ductilizing of Group via Elements by Rhenium and Other 
Solutes, National Aeronautics and Space Administration, Cleveland, OH (USA), 
1968. Lewis Research Center, Technical Note NASA-TN-D-4955. Accessed: Nov. 22, 
2024. [Online]. Available, https://www.osti.gov/biblio/5785668 .
[69] W.D. Klopp, W.R. Witzke, Mechanical Properties of Electron-Beam-Melted 
Molybdenum and Dilute Molybdenum-Rhenium Alloys, NASA Lewis Research 
Center, Cleveland, OH, USA, Technical Memorandum NASA-TM-X-2576, 1972. 
Accessed: Nov. 22, 2024. [Online]. Available, https://ntrs.nasa.gov/citations/19 
720017873 .
[70] J.-C. Carlen, B.D. Bryskin, Concerning sigma-phase in molybdenum-rhenium 
alloys, J. Mater. Eng. Perform. 3 (2) (1994) 282 – 291, https://doi.org/10.1007/ 
BF02645854 .
[71] R.L. Mannheim, J.L. Garin, Structural identification of phases in Mo – re alloys 
within the range from 5 to 95% re, J. Mater. Process. Technol. 143 – 144 (2003) 
533 – 538, https://doi.org/10.1016/S0924-0136(03)00342-X .
[72] G. Leichtfried, J.H. Schneibel, M. Heilmaier, Ductility and impact resistance of 
powder-metallurgical molybdenum-rhenium alloys, Metall. Mater. Trans. A 37 
(10) (2006) 2955 – 2961, https://doi.org/10.1007/s11661-006-0177-9 .
[73] H. Huang, et al., Hot compression behaviors and microstructural evolution of Mo- 
42 wt%re alloy, Mater. Lett. 318 (2022) 132252, https://doi.org/10.1016/j. 
matlet.2022.132252 .
A. Leclercq et al. International Journal of Refractory Metals and Hard Materials 132 (2025) 107266 
14
