# Energy-Assisted additive manufacturing for weldable and non-weldable Ni-based superalloys  a review

<!-- source: D:\总文献\Energy-Assisted additive manufacturing for weldable and non-weldable Ni-based superalloys  a review.pdf -->
<!-- file_sha256: e583cf26f7446e96b80b4e86ff6d30d2da19d623bdefb991dffe8df9de2bd503 -->

## Page 1

Virtual and Physical Prototyping
ISSN: 1745-2759 (Print) 1745-2767 (Online) Journal homepage: www.tandfonline.com/journals/nvpp20
Energy-Assisted additive manufacturing for
weldable and non-weldable Ni-based superalloys:
a review
Junmyoung Jang, Taehwan Ko, Jaeheon Lee, Dukyong Kim, Hwani Hwang,
Taesoon Jeong, Heuisu Kim & Seung Hwan Lee
To cite this article: Junmyoung Jang, Taehwan Ko, Jaeheon Lee, Dukyong Kim, Hwani
Hwang, Taesoon Jeong, Heuisu Kim & Seung Hwan Lee (2025) Energy-Assisted additive
manufacturing for weldable and non-weldable Ni-based superalloys: a review, Virtual and
Physical Prototyping, 20:1, e2512163, DOI: 10.1080/17452759.2025.2512163
To link to this article: https://doi.org/10.1080/17452759.2025.2512163
© 2025 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 01 Jul 2025.
Submit your article to this journal 
Article views: 1199
View related articles 
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=nvpp20

## Page 2

REVIEW ARTICLE
Energy-Assisted additive manufacturing for weldable and non-weldable 
Ni-based superalloys: a review
Junmyoung Jang, Taehwan Ko, Jaeheon Lee, Dukyong Kim, Hwani Hwang, Taesoon Jeong, Heuisu Kim and 
Seung Hwan Lee
Department of Mechanical Engineering, Hanyang University, Seoul, 04763, Republic of Korea
ABSTRACT 
Additive manufacturing (AM) of Ni-based superalloys has garnered significant attention for 
fabricating complex, high-performance components in aerospace, gas turbines, and other 
demanding applications, owing to its ability to achieve intricate geometries with excellent high- 
temperature strength and corrosion resistance. However, the process and material 
characteristics of AM for Ni-based superalloys introduce challenges that hinder industrial 
adoption. Recent studies have demonstrated that supplying additional energy beyond the heat 
required to melt the feedstock can address these challenges. This review systematically 
examines the effects of mechanical and thermal energy on AM deposits of Ni-based superalloys. 
Given the distinct material characteristics of weldable and non-weldable Ni-based superalloys, 
mechanical and thermal energy influence these classes of superalloys differently during AM. 
Therefore, various methods for applying mechanical and thermal energy, either individually or 
simultaneously, are comprehensively analyzed, along with their effects on weldable and non- 
weldable Ni-based superalloys. The effects of the energy applied through each method on 
weldable and non-weldable alloys are systematically summarised in terms of the internal 
defects, microstructures, and mechanical properties.
ARTICLE HISTORY
Received 13 March 2025 
Accepted 22 May 2025 
KEYWORDS 
Additive manufacturing; Ni- 
based superalloys; energy- 
assisted AM; microstructure; 
mechanical property
1. Introduction
Ni-based superalloys are widely utilised in turbines for 
power generation and aerospace engines because of 
their excellent thermal stability, mechanical proper -
ties, and corrosion resistance at high temperatures 
[ 1–4 ]. In recent years, turbine inlet temperatures 
have been progressively increased to enhance the 
energy conversion efficiency of turbines fabricated 
from Ni-based superalloys. To address the problems 
that have arisen with these higher temperatures, 
several strategies have been proposed. These include 
employing materials with superior thermal stability at 
elevated temperatures for turbine blades or incorpor -
ating complex internal structures, such as conformal 
cooling channels, to maximise cooling efficiency [ 5– 
8 ]. Consequently, several Ni-based superalloys have 
garnered significant attention, including IN738, 
CMSX-4®, and MAR-M247, which exhibit exceptional 
thermal stability at high temperatures. Meanwhile, 
additive manufacturing (AM) achieves high design 
freedom and manufacturing flexibility by repetitively 
melting and solidifying materials layer by layer. This 
process has emerged as a promising method for the 
efficient fabrication of complex internal geometries 
for turbine blades [ 9–12 ].
AM of Ni-based superalloys has high potential, but 
owing to the characteristics of the AM process, 
process-related issues such as low surface quality, 
internal defects, anisotropy, and heterogeneity exist 
[ 13–15 ]. These issues, in turn, degrade the mechanical 
properties of the deposits. Recent studies have proposed 
solutions to address these issues by optimising the 
entire process parameters [ 16 ], such as the beam focus 
[ 17 ], heat input [ 18–20 ], powder condition [ 21–23 ], and 
heat treatment [ 24 , 25 ]. However, as discussed in 
several review papers, conventional AM processes have 
limitations on printability for materials with low weld -
ability [ 26 , 27 ]. In the case of Ni-based superalloys, 
materials with an Al+Ti content greater than 6 wt.% 
are classified as non-weldable alloys [ 28 , 29 ]. These 
non-weldable alloys are prone to significant crack for -
mation, which severely limits their printability [ 30 ].
© 2025 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group 
This is an Open Access article distributed under the terms of the Creative Commons Attribution License ( http://creativecommons.org/licenses/by/4.0/ ), which permits unrestricted use, 
distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this article has been published allow the posting of the Accepted 
Manuscript in a repository by the author(s) or with their consent. 
CONTACT Seung Hwan Lee 
 seunghlee@hanyang.ac.kr
 Department of Mechanical Engineering, Hanyang University, 222 Wangsimni-ro, Seongdong- 
gu, Seoul, 04763, Republic of Korea
VIRTUAL AND PHYSICAL PROTOTYPING 
2025, VOL. 20, NO. 1, e2512163 (69 pages) 
https://doi.org/10.1080/17452759.2025.2512163

## Page 3

Despite the low printability, non-weldable Ni-based 
superalloys exhibit superior performance compared to 
weldable alloys, such as enhanced thermal stability and 
strength at higher temperatures [ 31 , 32 ]. Therefore, 
energy-assisted additive manufacturing (EAAM) has been 
developed to utilise non-weldable alloys to be employed 
in AM. EAAM refers to methods that apply additional 
energy beyond the heat input of conventional AM pro -
cesses [ 33–36 ]. Among these additional energy, mechani -
cally generated energy—rolling, peening, and burnishing 
—can induce plastic deformation at the surface of depos -
its. Such plastic deformation is known to help close internal 
cracks that are formed in the AM of non-weldable alloys 
[ 37 , 38 ]. Alongside mechanical energy, thermal energy 
can be supplied to AM through induction heating or hot 
plates, which helps reduce thermal residual stress in the 
deposits and thereby suppress crack formation [ 32 ].
Beyond its crack reduction effects in non-weldable Ni- 
based superalloys, EAAM has also been reported to 
enhance the mechanical properties of weldable alloys 
by controlling the microstructure of the deposit. For 
instance, in weldable alloys, the mechanical energy- 
assisted AM using rolling and peening can improve the 
creep resistance [ 39 , 40 ], hardness [ 40 , 41 ], and yield 
strength (YS) [ 42 ] by inducing microstructural changes 
such as work hardening and grain refinement. In addition 
to mechanical energy, thermal energy applied to weld -
able alloys through induction heating or hot plates can 
enhance ductility [ 43 ] and hardness [ 44 ] by modifying 
the grain size and morphology of the deposit. These 
findings indicate that the effects of the additional 
energy input in EAAM are highly correlated with the met -
allurgical characteristics of the deposit. Therefore, a com -
prehensive understanding of these effects is essential to 
fully realise the potential of EAAM in AM applications.
The effects of EAAM on weldable and non-weldable 
alloys have been discussed in several review papers, pri -
marily focusing on the enhancement of the mechanical 
properties [ 45–48 ]. However, considering that the 
complex strengthening mechanisms govern the mech -
anical properties of Ni-based superalloys, mechanical 
property evaluations should be accompanied by metal -
lurgical investigations to understand the effects of 
EAAM comprehensively. For this end, an in-depth 
review is required to analyze the influence of additional 
energy on AM of weldable and non-weldable Ni-based 
superalloys from metallurgical aspects, from fundamen -
tal principles to applications, to maximise the potential 
of EAAM. Such an analysis can provide a pathway 
toward selecting a proper material-EAAM combination, 
guided by the metallurgical principles that explain 
how additional energy enhances the printability and 
performance of the deposit.
This review provides an overview of the current state 
of the art in the application of additional energy to the 
AM of the weldable and non-weldable Ni-based superal -
loys. In addition to this overview, the effects of 
additional energy on the internal defects, microstruc -
ture, and mechanical properties of deposits are reviewed 
in detail. In Section 2 , the characteristics of various AM 
processes and Ni-based superalloys are summarised. In 
Section 3 , mechanical energy-assisted AM methods, 
including peening-assisted AM (PAAM), vibration- 
assisted AM (VAAM), and rolling-assisted AM (RAAM), 
are reviewed. In Section 4 , thermal energy-assisted AM 
methods, such as hot-plate-assisted AM (HPAAM), induc -
tion-coil-assisted AM (ICAAM), and process-heat-source- 
assisted AM (PHSAAM), are outlined. In Section 5 , 
methods that simultaneously apply mechanical and 
thermal energy during deposition, namely, hot isostatic 
pressing-assisted AM (HIP-assisted AM) and hot rolling- 
assisted AM (HRAAM), are analyzed. In Sections 3 – 5 , 
the systems and principles of each EAAM method are 
presented, followed by summary of the effects of 
EAAM methods on both weldable and non-weldable 
alloys. Section 6 comparatively analyzes the preceding 
discussions to propose future research directions for 
the energy-assisted AM of Ni-based superalloys.
2. Characteristics of Ni-based superalloys in AM
2.1. Characteristics of AM process
AM is a manufacturing process in which the final geome -
try is built through the repetitive melting and solidifica -
tion of material in a layer-by-layer manner. Thus, Ni- 
based superalloy deposits undergo complex thermal 
history and rapid solidification, which govern the result -
ing microstructural and mechanical characteristics of the 
deposit [ 49 , 50 ]. Understanding this thermal–solidifica -
tion process is crucial before assessing the effect of 
any additional energy input on deposits. EAAM has 
been applied across various AM processes, including 
laser metal deposition (LMD), wire arc additive manufac -
turing (WAAM), laser powder bed fusion (L-PBF), and 
electron-beam powder bed fusion (EB-PBF), each of 
which employs different heat sources, feedstock forms, 
and material delivery techniques, resulting in different 
solidification characteristics [ 49–51 ]. As each process 
exhibits different solidification characteristics, under -
standing their influence on the deposit is essential 
prior to the design of EAAM methods.
The different solidification characteristics of each AM 
process govern the grain size and morphology of the 
deposit [ 52 , 53 ]. In AM, repeated heat input causes the pre -
vious layer to be partially remelte and resolidified when the 
2 
 J. JANG ET AL.

## Page 4

next layer is being deposited. During this process, grains 
tend to grow in the build direction, which is opposite to 
the direction of heat transfer [ 54 , 55 ]. The morphology and 
the size of the grains within the deposits are primarily deter -
mined by various solidification parameters such as thermal 
gradient (G), solidification rate (R), and cooling rate (G × R) 
[ 56 ]. Regarding the grain morphology, the AM of Ni-based 
superalloys typically forms columnar grains owing to the 
steep thermal gradient. In particular, on the top surface of 
the deposit, heat is primarily transferred to the surroundings 
through convection, which has a lower heat transfer coeffi -
cient than conduction. As a result, the reduced heat transfer 
leads to a lower thermal gradient, promoting the formation 
of equiaxed grains at the top surface. Regarding the grain 
size, the significantly higher cooling rate in AM processes 
(10
2
–10⁶ K·s−1) compared to casting (10⁰–10
1 
K·s−1) lead 
to formation of finer grains in AM deposits than in cast pro -
ducts. Even within AM, the cooling rates of different pro -
cesses, such as LMD, WAAM, L-PBF, and EB-PBF, can vary 
by orders of magnitude depending on factors such as the 
energy source and type of feedstock. For instance, cooling 
rates are generally 10
2
–10
3 
K s−1 in WAAM, 10
3
–10⁴ K s 
−1 in LMD, 10⁴–10⁵ K s−1 in EB-PBF, and 10⁵–10⁶ K s−1 in 
L-PBF. As lower cooling rates result in coarser grains, 
slower-cooling processes such as WAAM, which uses an 
arc as the heat source with a high heat input, tend to 
produce the coarsest grains. Conversely, L-PBF, a faster- 
cooling process using a laser heat source with a relatively 
low heat input, typically forms the finest grains.
Besides microstructural evolution, the distribution of 
thermal residual stress is also governed by the different 
solidification characteristics of each AM process. 
Thermal residual stress typically develops as a result of 
intense interactions between thermal, mechanical, and 
metallurgical factors during AM [ 57–59 ]. Specifically, 
when heat input is applied, the material is rapidly 
heated to its melting point, forming a melt pool. As the 
heat source moves, the melt pool undergoes a high 
cooling rate, resulting in rapid solidification. During this 
process, the material tends to expand and shrink, but 
the surrounding solid material constrains the thermal 
deformation, thereby leading to the development of 
residual stress. Among the various factors influencing 
thermal residual stresses, the cooling rate plays a critical 
role; an increase in cooling rate generally leads to 
higher thermal residual stress. In comparison with other 
AM processes, L-PBF is typically exhibits the highest 
cooling rate, which results in the largest residual stress. 
In contrast, the EB-PBF process exhibits a low cooling 
rate due to the frequent use of preheating, which 
reduces the thermal gradient, resulting in a significantly 
reduced level of residual stress. In contrast to most AM 
processes, WAAM tends to generate higher thermal 
residual stress than LMD, despite the lower cooling rate 
due to excessive heat input from the arc heat source. 
This is attributed to the repeated high heat input over a 
wide area by the arc heat source, which leads to a signifi -
cantly wider heat-affected zone [ 51 ].
As the influence on the deposit varies depending on 
the AM process, the types and amounts of defects in 
the deposits also differ. These defects can be classified 
into lack of fusion (LOF), porosity, and cracks [ 60–62 ]. 
LOF occur when the deposited material fails to fully 
bond with adjacent layers, typically under low heat 
input conditions where the feedstock is not sufficiently 
melted. This defects are commonly observed in every 
AM processes. However, in EB-PBF, as the preheating 
is commonly utilised, the heat input is generally 
sufficient, resulting in the lowest amounts of LOF. Simi -
larly, LOF can be prevented in L-PBF, LMD, and WAAM 
by selecting appropriate process parameters to ensure 
sufficient heat input. Next, porosity refers to voids 
formed when gas vapor is trapped in the melt pool 
during the solidification process, or when keyhole col -
lapse occurs. This is particularly problematic in L-PBF, 
where the melt pool is small and the energy density 
is high. Under such conditions, keyhole-mode melting 
can lead to keyhole collapse, which increases the risk 
of porosity. Moreover, the high cooling rate in L-PBF 
limits the escape of trapped gas, further contributing 
to porosity formation. In contrast, LMD and WAAM, 
which exhibit larger melt pools with lower cooling 
rates, provide sufficient time for gas to escape, 
thereby reducing porosity. Furthermore, as mentioned 
earlier, EB-PBF provides sufficient heat input, which 
allows gas to escape easily from the melt pool, resulting 
in reduced porosity. Lastly, the crack formation is pri -
marily influenced by residual stress. Since the solidifica -
tion characteristics of each AM process affect residual 
stress, they consequently influence the crack formation 
of each process. For this reason, EB-PBF exhibits the 
lowest tendency for crack formation owing to its 
lower residual stress, whereas L-PBF, LMD, and WAAM, 
with higher thermal residual stresses, exhibit a higher 
tendency for crack formation. This indicates that crack 
formation is influenced by the solidification character -
istics of each AM process. In addition to these charac -
teristics, the material’s intrinsic properties also play a 
significant role in crack formation. Therefore, the 
characteristics of Ni-based superalloys are discussed in 
the following section.
2.2. Characteristics of Ni-based superalloys
In the AM of Ni-based superalloys, the material charac -
teristics also significantly influence various aspects of 
VIRTUAL AND PHYSICAL PROTOTYPING 
 3

## Page 5

the deposit, as well as the characteristics of process. 
Numerous alloying elements in Ni-based superalloys 
affect mechanical properties of the deposit through 
the solid-solution and precipitation strengthening 
mechanisms, which are essential for ensuring high- 
temperature performance [ 31 , 63–65 ]. For instance, Mo, 
Ta, and W act as solid-solution strengtheners by indu -
cing lattice distortions within the γ-matrix. In contrast, 
elements such as Ti, Al, and Nb promote precipitation 
strengthening by forming the strengthening phases, 
such as γ
′
and γ
′′
phases. Consequently, the primary 
strengthening mechanism, which influences the micro -
structural and mechanical characteristics of the AM 
deposit, is determined by the composition of an alloy.
Solid solution strengthened Ni-based superalloys, 
such as IN625 and Hastelloy X, are strengthened by 
solid-solution strengthening as their primary strength -
ening mechanism [ 66 , 67 ]. In these alloys, elements 
such as Mo, Ta, and W are dissolved in the Ni-based γ 
matrix, inducing lattice distortions that interrupt dislo -
cation movement, thereby enhancing mechanical prop -
erties such as strength and creep resistance. The extent 
of solid-solution strengthening depends on the type and 
concentration of the alloying element. Elements with a 
larger atomic size compared to Ni, such as W and Mo, 
induce more significant lattice distortions, resulting in 
a stronger strengthening effect than smaller-size 
elements such as Cr or Co. Consequently, elements 
with high solid-solution-strengthening coefficients lead 
to greater mechanical reinforcement. However, the 
solid-strengthening mechanism requires sufficient time 
at the strengthening temperature for atoms to solute 
within the matrix. In AM, the rapid solidification limits 
this solution, thereby reducing the extent of solid-sol -
ution strengthening during fabrication. Therefore, for 
solid-solution-strengthened alloys, appropriate post- 
heat treatments are essential after AM processing to 
promote the solid-solution strengthening mechanisms.
In contrast, precipitation-strengthened Ni-based 
superalloys, such as IN718 and IN738, primarily derive 
their mechanical properties from precipitation strength -
ening. Due to their high contents of phase-forming 
elements such as Al, Ti, and Nb, these alloys undergo 
phase precipitation during the AM process as a result 
of the complex thermal history and rapid solidification 
[ 68 ]. Specifically, among the alloying elements in Ni- 
based superalloys, elements with low solubility in the 
alloy matrix, such as Al, Ti, and Nb, do not fully dissolve 
in the grains during solidification and are rejected into 
the grain boundaries or interdendritic regions. These 
rejected elements segregate at the solid–liquid interface, 
leading to the precipitation of phases containing these 
elements during solidification [ 69 , 70 ]. Additionally, the 
complex thermal history of AM parts can maintain the 
temperature of the deposit within the precipitation 
temperature range of certain phases, and this heat 
accumulation can further promote phase precipitation. 
In Ni-based superalloys, phases that precipitate 
because of segregation or the complex thermal history 
include γ’ (Ni₃(Al,Ti)), γ’’ (Ni₃Nb), δ (Ni₃Nb), Laves ((Ni,Fe, 
Cr)₂(Nb,Mo,Ti)), and carbide phases. Strengthening 
phases such as γ’ and γ’’ are well known to enhance 
the strength of deposits by hindering dislocation move -
ment. Conversely, Laves, δ, and carbide phases are 
known to have complex effects on mechanical proper -
ties. The Laves phase, being hard and brittle, adversely 
affects multiple mechanical properties, including 
strength, ductility, fatigue resistance, and creep 
rupture resistance [ 71 ]. Meanwhile, the δ phase can 
improve the high-temperature creep rupture strength, 
but it is also known to degrade the overall strength 
and service life of components [ 72 ]. Lastly, carbides 
can enhance creep resistance by relaxing the stress at 
grain boundaries and preventing grain boundary 
sliding at high temperatures. However, excessive 
carbide precipitation can increase brittleness, thereby 
increasing crack susceptibility. Furthermore, the Laves, 
δ, and carbide phases are undesirable in Ni-based super -
alloys as they consume elements such as Al, Ti, and Nb, 
which are critical for the formation of strengthening 
phases, thereby reducing the amount of strengthening 
phases that can precipitate [ 73 , 74 ].
Among the phases that precipitate in Ni-based super -
alloys, the γ’ phase significantly affects the weldability of 
AM-fabricated Ni-based superalloys [ 75 ]. The alloying 
elements used to classify the weldability of Ni-based 
superalloys are Al and Ti, which are the components of 
the γ’ phase. As mentioned above, alloys with Al+Ti con -
tents exceeding 6 wt% are categorised as non-weldable 
[ 28 , 29 ]. During AM processes using non-weldable Ni- 
based superalloys as feedstock, as shown in Figure 1 , 
numerous solidification cracks in the fusion zone and 
liquation cracks in the heat-affected zone (HAZ) are 
easily formed [ 30 , 76 ]. Specifically, in the case of solidifi -
cation cracks, Al and Ti, which are γ’-phase-forming 
elements, exhibit low solubility in the γ matrix during 
solidification and are rejected to the grain boundaries 
as depicted in Figure 1 (a) [ 77 , 78 ]. These elements, 
which have relatively low melting points, form liquid 
films as shown in Figure 1 (b) at the grain boundaries 
during solidification [ 79 , 80 ]. The higher the Al+Ti 
content, the greater the volume of these films formed 
during solidification. These liquid films are easily torn 
under the high tensile residual stresses caused by the 
rapid cooling and localised thermal deformation in the 
deposit, leading to solidification cracks as illustrated in 
4 
 J. JANG ET AL.

## Page 6

Figure 1 (c). As for liquation cracks, low-melting-point 
phases, which are solidified from the liquid films at the 
grain boundaries of the HAZ in the previous layer, are 
reheated owing to the complex thermal history charac -
teristics of AM processes. This reheating causes partial 
remelting at the grain boundaries, re-forming the 
liquid films as illustrated in Figure 1 (b) [ 76 ]. These 
liquid films are also prone to tearing under the high 
tensile residual stresses induced by the rapid solidifica -
tion in AM, resulting in liquation cracks [ 81 ]. As a 
result, unlike weldable alloys, AM deposits of non-weld -
able alloys are more susceptible to cracking because of 
the higher Al+Ti content, which causes a significant 
amount of liquid films to form at the grain boundaries 
[ 82 , 83 ].
As such, although an Al+Ti content exceeding 6 wt.% 
degrades weldability in Ni-based superalloys, it also pro -
vides benefits in terms of thermal stability [ 82–84 ]. By 
contrast, in the case of weldable alloys, the low Al+Ti 
content ensures excellent weldability; however, these 
elements precipitate a relatively smaller volume fraction 
of the γ’ phase than those in non-weldable alloys. 
Instead, weldable alloys are primarily strengthened by 
the γ’’ phase (Ni₃Nb), which precipitates with Nb as its 
key constituent instead of Al and Ti. Comparing the γ’’ 
and γ’ phases, the γ’’ phase begins to transform into 
the detrimental δ phase above approximately 650°C. In 
contrast, the γ’ phase remains stable up to a dissolution 
temperature of 915°C, offering superior thermal stability 
in higher temperature ranges [ 72 ]. Consequently, weld -
able alloys, in which the γ’’ phase is primarily responsible 
for strengthening, are mainly employed in environments 
below 650°C [ 74 ], whereas non-weldable alloys, which 
rely on the γ’ phase as the primary strengthening 
phase, are predominantly used in high-temperature 
environments ranging from 650°C to 910°C [ 84 ].
Consequently, although there is a growing demand 
to achieve both high performance and excellent print -
ability in the AM of Ni-based superalloys, conventional 
AM remains limited in achieving these objectives simul -
taneously. To address this issue, this review introduces a 
promising strategy: EAAM, which can enhance the per -
formance (e.g. creep resistance, YS, and hardness) of 
weldable alloys, while improving the printability of 
non-weldable alloys. Accordingly, EAAM presents a 
viable pathway for overcoming the material-based con -
straints associated with the AM of Ni-based superalloys. 
Representative examples of weldable and non-weldable 
Ni-based superalloys deposited through EAAM are sum -
marised in Table 1 , including their alloy composition, 
primary strengthening mechanism, high-temperature 
performance, and typical applications.
3. Mechanical-energy-assisted AM of Ni-based 
superalloys
Some traditional manufacturing methods, such as 
rolling, forging, and extrusion, apply mechanical 
energy to materials, inducing plastic deformation to 
achieve the desired shapes while simultaneously 
improving the microstructure and mechanical properties 
of the material. Mechanical-energy-assisted AM, which 
integrates the advantages of such plastic deformation 
processes into AM technology, applies external mechan -
ical forces to solid or semi-solid deposits to induce 
plastic deformation. This approach not only alters the 
thermal residual stress but also promotes microstruc -
tural evolution within the deposited material. This 
Figure 1. Schematic illustration of the cracking mechanism in non-weldable Ni-based superalloys during the AM process: (a) rejection 
of low-solubility elements (Al and Ti) to grain boundary region during solidification; (b) formation of liquid film along grain bound -
aries; and (c) crack initiation due to tensile residual stress acting on the liquid film.
VIRTUAL AND PHYSICAL PROTOTYPING 
 5

## Page 7

section reviews research utilizing mechanical-energy- 
assisted AM to enhance the build quality of Ni-based 
superalloys. These AM studies are classified depending 
on the instruments employed, such as peening, 
vibration, and rolling. Then, the influence of each instru -
ment on the build quality of both weldable and non- 
weldable Ni-based superalloys is discussed based on 
the specific characteristics of the instrument.
3.1. Peening-assisted AM of Ni-based superalloys
3.1.1. Process methodology
Peening is a surface treatment process that induces 
plastic deformation to a depth of several tens to hun -
dreds of micrometers through repeated mechanical 
impacts. In the peening process, various media, such 
as metal shots, pins, ultrasonic waves, or laser plasma, 
repeatedly apply mechanical energy to the material. 
This process generates surface stresses exceeding the 
YS of the material on the surface, thereby inducing 
plastic deformation [ 100 ]. Recently, to improve the 
quality of the AM deposits, PAAM has been developed. 
During PAAM, peening induces plastic deformation on 
the surface of the deposited layers, thereby alleviating 
residual stresses generated by rapid cooling in the 
layer-by-layer deposition process. This leads to a 
reduction in crack susceptibility and distortion in the 
fabricated components [ 101 ]. Furthermore, the plastic 
deformation induced during the process promotes 
changes in the lattice structure, such as the generation 
of dislocations and twins [ 102 ]. These structural 
changes cause work hardening, which increases the 
resistance to deformation or stimulates recrystallization, 
further improving the material properties [ 103 , 104 ].
PAAM, which exhibits these effects, is primarily 
applied in L-PBF and LMD. These processes use metal 
powder as a feeding material and are characterised by 
relatively thin deposit layers; thus, they are commonly 
employed to manufacture components that require 
high surface quality and precision [ 105 ]. In this type of 
AM process, various peening methods, such as shot 
peening (SP), ultrasonic shot peening (USP), ultrasonic 
impact peening (UIP), hammer peening (HP), and laser 
shock peening (LSP), can be applied as post-treatment 
after deposition process to improve the surface quality 
of AM parts. As shown in Figure 2 (a, b), both USP and 
SP post-processes are performed by placing the AM 
part inside a chamber and spraying steel shots onto its 
surface [ 102 , 106 ]. On the other hand, when UIP, HP, or 
LSP is employed, peening instruments—such as ultra -
sonic horns, hammers, and pulsed lasers, which 
operate similarly to machine tools—deliver mechanical 
energy while scanning across the surface of the 
Table 1. Summary of the composition, primary strengthening mechanism, high-temperature performance, and applications of representative Ni-based superalloys [ 85–99 ].
Alloy
Composition, in wt.% Primary 
strengthening 
mechanism
Operating 
temperature ApplicationsNi Cr Al Ti Nb Mo Fe W Co Zr Ta Hf Re C B
IN625 Bal. 20–23 < 0.4 < 0.4 3.15–4.15 8–10 < 5 < 1 0.1 < Solid-solution 593–816°C Exhaust systems, shroud rings, etc.
IN718 50–55 17–21 0.2–0.8 0.65–1.15 4.75–5.50 2.8–3.3 Bal. < 0.08 Precipitation 649–704°C Turbine blades, discs, nuclear 
reactor components, etc.
Hastelloy X Bal. 20.5–23 < 0.5 < 0.15 < 0.5 8–10 17– 
20
0.2–1 0.5–2.5 < 0.01 Solid-solution 650–870°C Heat treatment furnace, 
turbocharger components, jet 
engine, etc.
Haynes 
230
Bal. 22 0.3 0.1 0.5 2 3 14 5 0.1 0.015 Solid-solution 800–1150°C Flame Holders, thermocouple 
sheaths, etc.
René 104 Bal. 11–13 4.5 4.5 0.5–3 3 < 0.1 2 11–13 0.2 3 0.04 <0.03 Precipitation 704–982°C Turbine disk, blades, compressor, 
etc.
CM247 
LC
Bal. 8.0–8.5 5.5–5.7 0.6–0.8 <0.05 0.4–0.6 <0.1 9.3–9.7 9.1–9.4 0.02 3.1–3.3 1.3–1.6 <0.05 0.07–0.09 0.005– 
0.03
Precipitation 900–1050°C Turbine blades, vanes, etc.
IN738LC Bal. 16 3.4 3.4 1.75 0.1 2.6 8.5 1.75 0.11 Precipitation 950–1050°C Drilling equipment, jet engine 
components, etc.
IN939 Bal. 22–23 1.8–2 3.5–4 0.8–1.5 1–2 < 0.5 1.8–2.2 18–20 < 0.04 1.2–1.8 0.1–0.15 <0.006 Precipitation 700–1100°C Vanes, blades, heat-shields, etc.
CMSX-4 Bal. 6.5 5.6 1 0.6 < 0.1 6.4 9.6 6.5 0.1 3 0.1 < 0.015 Precipitation 950–1200°C Turbine blades, 
jet engines, turbocharger, etc.
6 
 J. JANG ET AL.

## Page 8

deposited material, as shown in Figure 2 (c–e) 
[ 41 , 54 , 107 ]. Moreover, advanced methods have recently 
been introduced that utilise such peening instruments 
to induce plastic deformation within each deposition 
layer during the layer-by-layer stacking process, as 
shown in Figure 2 (f–h) [ 37 , 108 , 109 ]. In such interlayer 
peening processes, deposition by the heat source alter -
nates with the surface treatment by the peening instru -
ment, thus inducing layer-wise plastic deformation 
within the deposit.
3.1.2. Process effects for weldable Ni-based 
superalloys
In the PAAM process, mechanical energy induced by 
various peening methods effectively improves the depo -
sition quality and mechanical properties of weldable 
alloys. Table 2 summarises the reported effects of 
peening processes applied to weldable Ni-based alloys 
with various AM processes. In the PAAM process for 
weldable Ni-based superalloys, one of the prominent 
external effects is the enhancement of the surface 
quality of AM components. The repeated impacts 
applied during peening post-processing induce perma -
nent compressive deformation, thereby eliminating 
surface defects and reducing the surface roughness of 
weldable Ni-based superalloy deposits. In addition, the 
peening pressure influences the depth of plastic defor -
mation induced by the process [ 107 , 110 , 111 ]. Specifi -
cally, in studies applying SP post-treatment after the L- 
PBF process of IN718, higher peening pressure resulted 
in greater reduction of surface defects such as partially 
melted powder particles and spatter [ 102 ]. Moreover, 
during the L-PBF process of IN718, the sample treated 
with UIP exhibits the fewest surface defects compared 
to the as-deposited sample, as shown in Figure 3 (a), 
due to the higher energy accumulated through UIP rela -
tive to other peening methods [ 107 ]. By a similar prin -
ciple, extending the peening duration promotes 
uniform plastic deformation across the surface of the 
deposits, thus reducing the surface roughness 
[ 106 , 111 , 112 ]. Figure 3 (b) shows the measured surface 
roughness of L-PBF-fabricated IN718 deposits with and 
without SP post-treatment [ 102 ]. Surface roughness 
was measured on four surfaces: the top and bottom 
Figure 2. Schematic diagram of variouis type of PAAM process: (a) SP post-treatment, (b) USP post-treatment, (c) UIP post-treatment, 
(d) HP post-treatment, (e) LSP post-treatment, (f) interlayer UIP treatment, (g) interlayer HP treatment, and (h) interlayer LSP 
treatment.
VIRTUAL AND PHYSICAL PROTOTYPING 
 7

## Page 9

surfaces, which are perpendicular to the build direction, 
and two side surfaces, which are parallel to the build 
direction. The results show that the average surface 
roughness on all four surfaces was lower in the SP 
post-treated sample compared to the as-built (AB) 
sample. This roughness-reducing effect became more 
pronounced as the scanning hatch spacing decreased 
during the SP post-treatment. Finally, the plastic defor -
mation induced by peening can close micropores near 
the surface, thereby densifying the deposited material 
[ 106 , 111 , 112 ]. According to Chen et al. [ 106 ], in the L- 
PBF process of GH3230 alloy, the application of USP sig -
nificantly reduced the number of micropores compared 
to the as-built sample, as shown in Figure 3 (c). 
Table 2. Summary of the PAAM on weldable Ni-based superalloys.
Type of 
weldability Alloy
AM 
process
Assistant 
process Peening process parameter Effects of PAAM process Ref.
Weldable IN625 
IN718
L-PBF SP post- 
treatment
• Peening intensity: 8 Almen 
• Coverage: 200%
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving fatigue life
[ 102 ]
Weldable IN718 L-PBF SP post- 
treatment
• Peening pressure: 0.4, 0.5, 0.6 
MPa 
• Peening intensity: 6–10 Almen 
• Coverage: 100%
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving hardness
[ 111 ]
Weldable IN718 L-PBF SP post- 
treatment
• Peening intensity: 12 Almen 
• Coverage: 150%
• Tensile residual stress relaxation 
• Improving fatigue life, hardness
[ 113 ]
Weldable IN718 L-PBF SP post- 
treatment
• Peening pressure: 0.55–0.68 
MPa 
• Peening intensity: 6 Almen 
• Peening velocity: 70 m/s 
• Coverage: 200%
• Surface quality improvement 
• Improving corrosion resistance
[ 110 ]
Weldable GH3230 L-PBF USP post- 
treatment
• Frequency: 30, 45 kHz 
• Amplitude: 45 μm
• Tensile residual stress relaxation 
• Improving hardness
[ 114 ]
Weldable GH3230 L-PBF USP post- 
treatment
• Frequency: 20 kHz 
• Amplitude: 45 μm 
• Treatment time: 240, 300, 360, 
840 s
• Tensile residual stress relaxation 
• Improving hardness, YS, Ultimate tensile strength 
(UTS), elongation (EL)
[ 106 ]
Weldable Haynes 
230
L-PBF UIP post- 
treatment
• Amplitude: 27 μm 
• Frequency: 20 kHz 
• Overlap rate: 50%
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving YS, UTS, EL, wear resistance
[ 112 ]
Weldable IN718 LMD UIP post- 
treatment
• Frequency: 1 kHz 
• Treatment time: 120 s
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving hardness
[ 107 ]
Weldable IN718 L-PBF Interlayer UIP • Frequency: 20 kHz 
• Treatment interval: 8 layers
• Improving fatigue life, YS, UTS 
• Inhibiting crack propagation
[ 39 ]
Weldable IN718 LMD UIP post- 
treatment
• Frequency: 20 kHz 
• Amplitude: 30 μm 
• Feed rate: 30 μm 
• Static load: 50 N
• Tensile residual stress relaxation 
• Improving hardness, YS, UTS, wear resistance
[ 40 ]
Weldable IN718 LMD Interlayer UIP • Frequency: 28 kHz 
• Power: 1 kW 
• Travel speed: 3 mm/s
• Tensile residual stress relaxation 
• Improving hardness
[ 108 ]
Weldable IN718 LMD Interlayer UIP • Frequency: 28 kHz 
• Power: 1 kW 
• Amplitude: 0.1 mm
• Tensile residual stress relaxation 
• Improving YS, UTS
[ 115 ]
Weldable IN718 L-PBF LSP post- 
treatment
• Laser power: 140, 170, 200 mW 
• Number of shots: 3, 5, 7
• Tensile residual stress relaxation 
• Improving hardness, wear resistance
[ 41 ]
Weldable IN718 L-PBF LSP post- 
treatment
• Pulse laser energy: 250, 300, 
350 mJ 
• Overlapping rate: 80, 70, 60%
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving hardness
[ 116 ]
Weldable IN718 L-PBF LSP post- 
treatment
• Repetition rate: 10 Hz 
• Pulse duration: 10 ns 
• Pulse laser energy: 1.9 J
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving fatigue life, hardness
[ 117 ]
Weldable IN625 
+TiC
L-PBF LSP post- 
treatment
• Pulse width: 10 ns 
• Repetition rate: 5 Hz 
• Pulse laser energy: 7 J 
• Overlapping rate: 50%
• Tensile residual stress relaxation 
• Improving hardness, YS, UTS
[ 118 ]
Weldable IN718 LMD LSP post- 
treatment
• Spot diameter: 3 mm 
• Pulse duration: 10 ns 
• Overlapping rate: 50% 
• Power density: 8.49, 9.90, 11.31 
GW/cm2
• Surface quality improvement 
• Tensile residual stress relaxation 
• Improving fatigue life, hardness 
• Inhibiting crack propagation
[ 119 ]
Weldable IN718 LMD Interlayer HP • Hammer-to-surface distance 
: 10 mm 
• Moving speed: 2 mm/s
• Improving hardness, YS, UTS, EL [ 109 ]
8 
 J. JANG ET AL.

## Page 10

Consequently, these external effects induced by peening 
have a positive effect on improving mechanical proper -
ties by alleviating stress concentrations at the surface or 
within the material.
For weldable Ni-based superalloys, the PAAM process 
not only improves the surface quality but also can miti -
gate tensile residual stresses formed within the deposited 
material. As shown in Figure 4 (a), typical AM processes 
involve the formation of metallic bonds between the pre -
viously solidified layer and the newly deposited layer, 
enabling layer-by-layer deposition. During the cooling 
and solidification of semi-solid deposits, thermal contrac -
tion and solidification shrinkage act as the driving forces 
for the shrinkage of the deposit. However, due to the met -
allurgical bonding between the two layers, the shrinkage 
of the deposit is constrained, leading to the generation of 
tensile residual stresses [ 108 ]. In comparison, when 
peening post-treatment is applied to such a deposited 
material, the surface undergoes plastic deformation, 
resulting in the formation of a permanently compressed 
deformation layer. Beneath this layer of compressed 
deformation, where plastic deformation is absent, 
elastic springback forces are induced. However, because 
the surface remains plastically deformed and does not 
recover, compressive residual stresses are introduced at 
the surface. The magnitude of these compressive residual 
stresses, as well as the depth at which they form, is 
strongly influenced by peening process parameters 
such as peening time and power. As these parameters 
increase, the depth of plastic deformation increases, 
thereby enhancing the magnitude of compressive 
residual stresses [ 112 , 114 , 116 ].
Figure 3. Comparative analysis of the surface integrity between conventional AM deposits and PAAM deposits: (a) SEM images of 
IN718 deposits fabricated by L-PBF with and without UIP [ 107 ], (b) measured roughness of IN718 deposits fabricated by L-PBF 
with and without SP [ 102 ], and (c) porosity simulation results of GH3230 deposits fabricated by L-PBF with and without USP [ 106 ].
Figure 4. Differences in residual stress between conventional AM process and PAAM process [ 108 ]: (a) schematic of residual stress 
generation during inter-layer UIP-assisted LMD process and (b) residual stress profile of IN718 LMD deposits along the depth direction 
with and without inter-layer UIP process.
VIRTUAL AND PHYSICAL PROTOTYPING 
 9

## Page 11

Moreover, In addition to applying post-peening to 
the deposit, applying interlayer peening during layer- 
by-layer deposition can effectively reduce tensile 
residual stresses throughout the entire deposit. In struc -
tures deposited with interlayer peening, compressive 
residual stresses form at the interfaces owing to the 
plastic deformation induced between the layers. This 
compressive stress counteracts the tensile residual stres -
ses generated during repetitive heating and cooling 
cycles, thereby reducing the overall residual stress 
[ 39 , 108 ]. Figure 4 (b) shows the depth-wise residual 
stress profiles of IN625 deposits manufactured by LMD 
process with and without interlayer UIP [ 108 ]. Unlike 
the as-built sample, which exhibited tensile residual 
stress across the depth regardless of heat treatment 
(HT), the interlayer UIP sample showed compressive 
residual stress throughout the entire depth. These 
results indicate that utilizing the PAAM can effectively 
mitigate the residual stress–related issues commonly 
observed in AM, such as distortion and mechanical prop -
erty degradation.
In addition to its residual stress relaxation effects, the 
PAAM process offers the advantage of promoting micro -
structural evolution. The peening-induced plastic defor -
mation has a notable effect on increasing the density 
of dislocations and twins within the grains near the 
surface of the deposit. For example, Figure 5 (a) and (b) 
present SEM images showing the microstructures of 
Haynes 230, fabricated by the L-PBF process with and 
without the application of UIP, respectively [ 112 ]. When 
comparing these SEM images, a higher density of dislo -
cations is observed in the UIP-processed sample than in 
the as-built sample. Such an increase in the density of 
intra-granular lattice defects near the surface is further 
Figure 5. Comparative analysis of the microstructures between conventional AM process and PAAM process: SEM images of the (a) as- 
built (AB) and (b) AB+UIP specimens [ 112 ]; EBSD results of the (c) AB and (d) AB+UIP specimens [ 115 ].
10 
 J. JANG ET AL.

## Page 12

promoted by increasing the peening process par -
ameters, such as duration or power, thereby increasing 
the depth of plastic deformation [ 112 , 115 ]. The increased 
density of lattice defects within the grains enhances the 
interactions among the defects, causing them to entan -
gle. This entanglement obstructs the initiation of slip 
and movement of dislocations, thereby inducing work 
hardening [ 39 , 40 ]. Furthermore, a lattice with a higher 
density of defects stores more energy, rendering the 
grains thermodynamically unstable. This instability acts 
as a driving force for recrystallization. In particular, apply -
ing interlayer peening during layer-by-layer deposition 
—where plastic deformation from peening alternates 
with heat input from the heat source—creates con -
ditions favorable for static recrystallization, such as high 
lattice energy and sufficient recrystallization tempera -
ture [ 108 , 109 , 115 ]. For example, Wang et al. [ 115 ] inves -
tigated the effect of interlayer UIP during the LMD 
process of IN718. Compared to the as-deposited 
sample, the deposit treated with interlayer UIP exhibited 
static recrystallization beneath the interlayer fusion line, 
resulting in the formation of fine equiaxed grains with 
isotropic properties. As shown in the electron backscatter 
diffraction (EBSD) maps in Figure 5 (c, d), this microstruc -
tural change contrasts with the coarse columnar grain 
structure with anisotropic properties that dominates 
the as-built samples. Below the recrystallization fine 
region, equiaxed grains were not formed due to the 
limited heat input in the build direction during the 
LMD process; however, the formation of sub-grains was 
observed, resulting from concentrated slip and dislo -
cations induced by plastic deformation. This indicates 
that even when recrystallization does not occur due to 
interlayer UIP, the work hardening effect induced by 
plastic deformation remains effective.
The effect of PAAM, such as surface quality improve -
ment, tensile residual stress relaxation, and microstruc -
ture evolution, synergistically enhances the various 
mechanical properties of weldable Ni-based superalloy 
deposits. One of the most notable improvements in 
the mechanical properties caused by PAAM is the 
fatigue life [ 39 , 102 , 113 , 117 , 119 ]. As shown in the 
Figure 6 (a), SP post-treatment after the L-PBF process 
for IN625 and IN718 significantly increases the number 
of cycles to failure compared to the AB samples under 
the same high maximum stress [ 102 ]. This improvement 
Figure 6. Comparative analysis of the mechanical properties between conventional AM deposits and PAAM deposits: (a) fatigue life 
for IN625 and IN718 deposits fabricated by L-PBF with and without SP [ 102 ], (b) Friction coefficient and wear volume for Haynes 230 
deposits fabricated by L-PBF with and without UIT [ 112 ], (c) surface microhardness of GH3230 deposits fabricated by L-PBF with and 
without USP [ 114 ], and (d) tensile properties for IN718 deposits fabricated by DED with and without HP [ 109 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 11

## Page 13

in fatigue life resulting from PAAM is attributed to the 
various effects of peening previously discussed. The 
reduction of surface defects and internal pores by 
PAAM mitigates stress concentrations that can initiate 
fatigue cracks, thereby enhancing fatigue life. In 
addition, the compressive residual stresses induced by 
PAAM help suppress the propagation of fatigue cracks.
Additionally, peening-induced work hardening on 
the surface of a deposit improves its resistance to defor -
mation, thereby enhancing surface properties such as 
hardness and wear resistance [ 40 , 41 , 108 , 112 , 114 ]. For 
instance, Liu et al. [ 112 ] investigated the effects of post 
L-PBF ultrasonic impact treatment (UIT) on Haynes 230. 
Compared with an as-deposited sample, the UIT- 
treated sample showed a decrease in both friction coeffi -
cient and wear volume, and the effect became greater as 
the number of UIT cycles increased from 1 to 3, as shown 
in Figure 6 (b). As another example, in a study on the L- 
PBF process of the GH3230 alloy, the USP-treated 
deposit exhibited higher surface microhardness than 
the as-built deposit, as shown in Figure 6 (c) [ 114 ].
In addition to surface property improvements, inter -
layer PAAM also contributes to the enhancement of 
the tensile properties of the deposit [ 39 , 109 , 118 ]. 
According to Zhou et al. [ 109 ], who applied interlayer 
HP to the hybrid-DED (HDED) process of IN718, the 
HDED samples exhibited superior UTS, YS, and EL in 
both the horizontal and vertical directions compared 
to the as-built samples, as shown in Figure 6 (d). As pre -
viously explained, these improvements are attributed to 
the layer-by-layer work hardening induced by peening- 
induced plastic deformation, along with grain refine -
ment promoted by static recrystallization.
As discussed above, when the PAAM process is used 
independently, it can enhance the mechanical proper -
ties by inducing microstructural evolution, such as 
work hardening and recrystallization. Moreover, it also 
plays a critical role in supporting the formation of 
strengthening phases when applied before or after the 
essential post-heat treatment of Ni-based superalloy 
deposits. As mentioned in Section 2 , during the AM 
process for weldable Ni-based superalloys, the material 
undergoes melting and solidification owing to the heat 
source. In precipitation-hardening superalloys such as 
IN718, this often leads to the formation of detrimental 
phases such as the Laves phase rather than the 
primary strengthening phase, γ
′′
. The early formation 
of the Laves phase depletes Nb, a critical element for 
γ
′′
precipitation, thereby hindering the precipitation of 
such strengthening phases. To address this issue and 
improve the mechanical properties of weldable Ni- 
based superalloy deposits, the detrimental phases 
must be fully dissolved through homogenisation and 
solution treatment during post-heat treatment. Accord -
ing to Zhou et al. [ 109 ], interlayer HP conducted 
before the post-heat treatment in IN718 deposits frag -
mented the Laves phase, which forms in the interdendri -
tic regions. These fragments are evenly distributed 
throughout the microstructure, as illustrated in Figure 
7 (a). Furthermore, the repeated heat input during 
layer-by-layer deposition promotes the re-dissolution 
of the fragmented Laves phase, gradually reducing its 
presence and facilitating the precipitation of γ
′′
. The 
fragmented Laves phase also enhances the dissolution 
process during the subsequent solution and double- 
aging treatments, thus increasing the fraction of 
strengthening phases and distributing them more uni -
formly within the microstructure.
In addition, the fragmentation effect induced by 
peening remains significant not only during the AM 
process but also after deposition. When peening post- 
treatment is performed after the AM process and heat 
Figure 7. (a) Schematic diagram of precipitation evolution in LMD deposit of IN718 utilizing inter-layer HP [ 109 ] and (b) schematic of 
precipitation evolution in L-PBF deposits of GH3230 utilizing USP after a heat treatment [ 114 ].
12 
 J. JANG ET AL.

## Page 14

treatment, the plastic deformation induced by peening 
generates compressive residual stress at the surface 
and causes work hardening. At the same time, peening 
post-treatment has the effect of fragmenting precipi -
tates formed at the grain boundaries during heat treat -
ment. For instance, utilizing USP at the selective laser 
melting (SLM) process of the GH3230 alloy, M23C6 pre -
cipitates formed during the solution treatment (ST) are 
fragmented by USP induced plastic deformation [ 114 ]. 
When fragmented M23C6, which has a higher strength 
than the γ matrix, is uniformly distributed along the 
grain boundaries, it obstructs dislocation motion, 
increases the dislocation density, and suppresses grain 
boundary sliding, thereby enhancing deformation resist -
ance. Consequently, peening applied both before and 
after post-heat treatment reduces detrimental phases 
such as Laves while promoting the finer, more uniform 
precipitation of phases such as MC carbides and γ
′′
. 
These findings demonstrate that peening is instrumental 
in maximising the mechanical property improvements 
achieved through heat treatment.
3.1.3. Process effects for non-weldable Ni-based 
superalloys
The effects of the peening-induced plastic deformation 
during the PAAM process for Ni-based superalloys are 
fundamentally similar, regardless of the material. 
However, the extent and nature of these effects vary 
depending on the weldability of the material. Peening- 
induced plastic deformation eliminates surface defects 
and internal porosity in the deposits, thereby reducing 
surface roughness and increasing densification. Simul -
taneously, it generates compressive residual stresses, 
which mitigates the tensile residual stresses typically 
formed during deposition. Furthermore, plastic defor -
mation triggers work hardening. When these effects 
act synergistically, the mechanical properties, such as 
hardness, strength, and fatigue life are enhanced, even 
in the PAAM process of non-weldable Ni-based superal -
loys, as shown in Table 3 . However, unlike the PAAM 
process for weldable Ni-based superalloys—where the 
primary benefit lies in improving mechanical properties 
by increasing deformation resistance—the PAAM 
process for non-weldable superalloys, which are highly 
susceptible to cracking, not only enhances deformation 
resistance but also reduces crack formation during 
processing.
This crack reduction effect in non-weldable superal -
loys exhibits different mechanisms depending on the 
timing of the peening application during the PAAM 
process. In the PAAM process for non-weldable Ni- 
based superalloys, post-process peening induces com -
pressive residual stresses on the surface, following the 
same principles discussed in Section 3 . 1 . 2 . These com -
pressive stresses counteract the tensile residual stresses, 
which serve as the driving force for the solidification and 
liquation cracking commonly observed during the AM 
process for non-weldable Ni-based superalloys [ 121 ]. 
Simultaneously, peening-induced compressive residual 
stresses close cracks, thereby preventing the propa -
gation of existing cracks [ 37 ]. The effectiveness of 
crack suppression is influenced by the magnitude and 
depth of these compressive stresses. Larger stresses 
and deeper stress penetration are more advantageous 
for mitigating cracks. According to Chen et al. [ 121 ], 
who investigated peening-assisted L-PBF of the non- 
weldable K447A superalloy, combined methods—such 
as ultrasonic after laser shock peening (ULSP) and laser 
after ultrasonic shock peening (LUSP)—produced 
higher compressive residual stresses than individual 
techniques such as USP or LSP. As shown in Figure 
8 (a), during the deposition of non-weldable K447A, 
applying the LUSP post-treatment results in significantly 
greater compressive residual stresses and more effec -
tively reduces cracking compared to other single or 
combined peening techniques.
Table 3. Summary of the PAAM on non-weldable Ni-based superalloys.
Type of 
weldability Alloy
AM 
process Assistant process Peening process parameter Effects of PAAM process Ref.
Non-weldable K447A LMD SP pre-treatment • Peening pressure: 0.7 MPa 
• Duration: 10, 30, 50, 70 min
• Reducing crack formation [ 120 ]
Non-weldable IN100 LMD Interlayer UIP • Frequency: 28 kHz 
• Amplitude: 20 μm 
• Peening force: 25, 50, 75 N
• Reducing crack formation [ 38 ]
Non-weldable CM247LC L-PBF Interlayer LSP • Repetition rate: 5 Hz 
• Pulse duration: 6.3 ns • Pulse laser energy: 
0.4 J 
• Overlapping rate: 40%, 80%, 80%×2
• Reducing crack formation [ 37 ]
Non-weldable K447A L-PBF LUSP post- 
treatment
[USP parameter] 
• Frequency: 20 kHz 
• Amplitude: 45 μm 
[LSP parameter] 
• Wavelength: 1064 nm 
• Pulse width: 10 ns 
• Overlapping rate: 50%
• Reducing crack formation 
• Improving hardness, YS, UTS, 
EL
[ 121 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 13

## Page 15

Unlike post-process peening, the pre-peening of the 
base material in the PAAM of non-weldable Ni-based 
superalloys exhibits distinct behaviour: the simultaneous 
generation of surface compressive residual stress and 
grain refinement [ 120 ]. Figure. 8(b) is a schematic 
diagram describing the microstructure evolution and 
crack behaviour according to SP pre-treatment in the 
LMD process of K447A. SP pre-treatment increases the 
formation of dislocations and twins in the base material, 
thereby increasing the lattice energy. When the heat 
input is subsequently applied by the heat source, 
static recrystallization occurs in the HAZ, thus forming 
fine equiaxed grains, which in turn increases the 
number density of the grain boundaries. Furthermore, 
when the heat input partially remelts γ’, the primary 
strengthening phase of non-weldable Ni-based super -
alloys, a fine liquid film network forms along these 
densely packed grain boundaries. According to strain- 
based criteria, solidification and liquation cracking 
occur when the thermal strain caused by thermal 
contraction and solidification shrinkage exceeds the 
critical strain that the liquid film can withstand [ 120 ]. 
This fine liquid film network induced by recrystalliza -
tion helps disperse the thermal strain, effectively 
reducing the crack susceptibility in the HAZ of non- 
weldable Ni-based superalloys.
In addition, as shown in Figure 8 (c), the PAAM process 
for non-weldable Ni-based superalloys, where interlayer 
peening is performed during deposition, not only 
reduces crack susceptibility and promotes crack 
closure but also exhibits a crack healing effect [ 37 , 38 ]. 
The cracks closed by compressive residual stresses are 
remelted during the layer-by-layer deposition as heat 
is applied by the heat source. During this remelting, 
the cracks fully bond and heal, which effectively elimin -
ates these defects. For instance, Wang et al. [ 38 ] investi -
gated the crack reduction effect of interlayer UIP 
parameters in the LMD process of IN100 to derive the 
optimal conditions for crack mitigation. By applying 
peening forces from 0 N to 75 N across four deposit 
samples, they found that the 75 N condition nearly elimi -
nated crack formation. This was linked to the formation 
of strong compressive residual stresses, which occurred 
when the plastic deformation layer extended beyond 
Figure 8. Comparing the crack suppression mechanism according to the timing of peening application during AM process: (a) 
changes in residual stress and cracking induced LUSP post-treatment [ 121 ], (b) schematic of microstructure evolution and crack miti -
gation induced SP pre-processing [ 120 ], and (c) schematic of crack healing mechanism induced inter-layer LSP [ 37 ].
14 
 J. JANG ET AL.

## Page 16

the laser-induced HAZ. The resulting stress field, in con -
junction with crack remelting, enabled effective crack 
closure and healing.
Furthermore, similar to the mechanism in weldable 
superalloys discussed in Section 3 . 1 . 2 , the PAAM 
process for non-weldable Ni-based superalloys influ -
ences the strengthening phases precipitated during 
post-heat treatment. In the PAAM process for weldable 
superalloys, peening has been shown to fracture detri -
mental phases into smaller fragments, thereby mitigat -
ing their inhibitory effects on the precipitation of the 
primary strengthening phase γ’. While PAAM induces 
fragmentation of detrimental phases in both weldable 
and non-weldable Ni-based superalloys, it further con -
tributes to the modification of strengthening phase size 
and distribution in non-weldable alloys. Figure 9 pre -
sents a schematic diagram explaining the effect of 
PAAM on precipitation behaviour in these non-weld -
able Ni-based superalloys. During the conventional L- 
PBF process for the K447A alloy, which is representative 
of non-weldable Ni-based superalloys, γ’ precipitates 
with a consistent size are uniformly distributed in the 
γ matrix after post-heat treatment; however, carbides 
with irregular sizes and distributions also form, as 
shown in Figure 9 (a). However, in the PAAM process, 
peening induces plastic deformation, leading to the 
fragmentation of γ’ precipitates and carbides near the 
surface of the deposits after post-heat treatment 
[ 121 ]. As illustrated in Figure 9 (b), the surface of the 
K447A deposits processed with LUSP exhibited signifi -
cant plastic deformation, which increased the dislo -
cation density and refined the γ’ precipitates and 
carbides, breaking them into smaller fragments. This 
fragmentation effect on precipitates decreases with 
the increasing depth from the surface of the deposit. 
Consequently, in the PAAM process for non-weldable 
Ni-based superalloys, the size distribution of precipi -
tates exhibits a gradient along the depth direction of 
the deposit.
As the feasibility of PAAM has been established for 
simple geometries, recent research has focused on 
extending its application to complex-shaped structures 
used in real industrial applications. For instance, Lesyk 
et al. [ 107 , 122 ] applied various peening post-treat -
ments—such as SP, USP, and UIP—to the L-PBF 
process of IN718 for turbine blade fabrication, and 
demonstrated that PAAM is a technological solution 
for enhancing the performance of complex aerospace 
components through improved material properties. In 
particular, their study focused on the improvement of 
surface properties such as hardness and roughness 
through the application of PAAM. Such enhancements 
are particularly beneficial in aerospace applications, 
where low fluid drag and high surface resistance to 
heat and pressure are required. From this perspective, 
PAAM technology for Ni-based superalloys is expected 
to apply not only to turbine blades but also to 
complex-shaped gas turbine parts, such as turbine com -
bustors and combustor transition ducts.
3.2. Vibration-assisted AM of Ni-based 
superalloys
3.2.1. Process methodology
Vibration is another method for transmitting mechanical 
energy to materials that has been primarily utilised in 
Figure 9. Schematic diagram of precipitate evolution in heat-treated L-PBF deposits of non-weldable alloy (a) before and (b) after 
LUSP application [ 121 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 15

## Page 17

welding and casting to control melt pool flow and hom -
ogenise the composition [ 123–126 ]. Recently, vibration 
has been extensively researched to control both the 
melt pool flow and microstructural evolution during 
the AM process. Figure 10 shows a schematic of VAAM 
system, which consists of vibrating components and 
AM equipment. In the vibrating components, the 
vibrations generated by the transducer are amplified 
through the sonotrode and transmitted to the substrate. 
In the AM equipment, a layer-by-layer stacking process is 
performed by supplying powder or wire feedstock 
materials on the vibrating substrate. By using the 
VAAM system, the melt pool flow and microstructural 
evolution can be controlled during the AM process, 
therby enhancing the quality of deposits with improved 
mechanical properties. While VAAM provides these sub -
stantial advantages, there are certain limitations to its 
application depending on the type of AM process. In 
specific, there are limitations to apply the virbration to 
PBF process because of the vibration-induced scattering 
of unmelted powder on the deposition bed. Therefore, it 
is mostly applied to LMD or WAAM processes, where 
materials are directly supplied to the melt pool formed 
by the heat source [ 45 ].
As mentioned above, the VAAM process enables the 
fabrication of deposits with improved mechanical prop -
erties by transmitting mechanical energy as vibration 
during AM process. In the VAAM process, the vibration 
is generated by the piezoelectric effect, where piezoelec -
tric elements in the transducer expand and contract 
repeatedly due to change in the electric field. When 
this vibration energy is transmitted to the substrate, con -
vection in the melt pool is enhanced, thus activating the 
melt pool flow [ 42 , 127 ]. The extent of convection 
enhancement varies depending on the frequency and 
amplitude of vibration applied to the substrate. At 
low frequencies below 20 kHz, less energy is trans -
mitted, but the relatively high amplitude can still 
induce strong melt pool convection. This intesified 
melt pool convection helps mitigate tempreature gra -
dients and promotes uniform elemental distribution 
within the melt pool [ 128 , 129 ]. In contrast, at higher 
frequencies above 20 kHz, the amplitude is lower, 
resulting in comparatively weaker convection. Never -
theless, the vibration at higher freqeuncy enables 
greater energy transmission to the melt pool com -
pared to the lower frequency vibration. The amount 
of energy transmitted influences the extent of acoustic 
cavitation, which involves the repeated formation and 
collapse of cavitation bubbles [ 127 ]. These collapsing 
bubbles generate shock waves within the melt pool, 
and a higher frequency vibration, due to its greater 
energy transmission, can produce more shock waves 
compared to lower frequency vibration. Through 
these effects of low and high frequency vibrations on 
melt pool behaviour, the VAAM process contributes 
to the improvement of the mechanical properties of 
the deposit.
3.2.2. Process effects for weldable Ni-based 
superalloys
For weldable Ni-based superalloys, VAAM has been 
shown to improve the density, refined grain structure, 
and control of detrimental phases, thereby leading to 
improved mechanical properties compared to conven -
tional AM deposits. Table 4 summarises these effects 
of VAAM, providing an overview of the materials, type 
of AM process, process parameters, and the correspond -
ing outcomes, as discussed in Section 3 . 2 . 2 . In terms of 
the densification, the density of the VAAM deposit is 
enhanced by reducing porosity [ 128 , 130–132 ]. According 
to Dash et al. [ 133 ], who investigated porosity in IN625 
fabricated by LMD, numerous small and large pores 
were observed under non-vibration condition, as shown 
in Figure 11 (a). In contrast, under vibration condition, 
only a few small pores are observed as shown in Figure 
11 (b). The underlying mechanism for the porosity 
reduction, as mentioned in Section 3 . 2 . 1 , is closely 
related to the melt pool dynamics. When the vibration 
energy is transmitted to the melt pool, it promotes the 
convection and induces stirring within the melt pool. 
This intensified flow within the melt pool facilitates the 
upward movement of process-induced pores and gas 
pores formed from the vaporisation of alloying elements 
during deposition [ 130 , 131 , 134 ]. If these pores are 
expelled from the melt pool before complete solidifica -
tion, the internal porosity is reduced, resulting in a 
denser structure. Particularly when ultrasonic vibration 
is applied, the acoustic cavitation induces the repeated 
nucleation, expansion, and collapse of cavitation 
bubbles, thus preventing the formation of gas-induced 
Figure 10. Schematic of VAAM system consisting of equipment 
for both AM and vibration.
16 
 J. JANG ET AL.

## Page 18

pores. Notably, the extent of this porosity reduction varies 
with process parameters such as vibration frequency. As 
shown in Figure 11 (c), which presents the fraction of por -
osity in IN625 deposits fabricated by the LMD process, the 
sample without vibration exhibited the highest porosity. 
When vibration was applied, porosity was significantly 
reduced. Moreover, a clear trend is observed in which 
lower frequencies—from 33 kHz to 30.5 kHz and finally 
to 28 kHz—lead to progressively lower porosity, with 
the 28 kHz condition showing the most effective 
reduction. These results emphasise the importance of 
optimising vibration parameters to enhance the densifi -
cation performance of VAAM.
In addition to densification, the VAAM process of 
weldable Ni-based superalloys facilitates the columnar- 
to-equiaxed transition (CET), which results in grain 
refinement [ 42 , 135 ]. Figure 12 (a, b) exhibit this grain 
refinement of vibration in IN625 of WAAM [ 42 ]. The prin -
ciple of grain refinement effect can be attributed to two 
key mechanisms. First, the enhanced melt pool flow 
induced by the stirring action from vibration moderates 
the temperature gradient, which expands the region of 
constitutional supercooling, where residual liquid 
remains below the solidus temperature [ 42 , 127 , 139 ]. 
This lowered temperature gradient reduces the nuclea -
tion energy barrier at the solid–liquid interface, 
thereby increasing the nucleation rate [ 136 ]. Second, 
Table 4. Summary of the VAAM on weldable Ni-based superalloys.
Type of weldability Alloy AM process Vibration process parameter Effects of VAAM process Ref.
Weldable IN625 WAAM • Frequnecy: 20 kHz 
• Amplitude: 50 µm
• Grain refinement 
• Controlling formation of precipitates 
• Improving YS, UTS
[ 42 ]
Weldable IN718 LMD • Frequency: 0, 25, 33, 41 kHz 
• Amplitude: 5 µm
• Densification 
• Grain refinement 
• Improving hardness
[ 130 ]
Weldable IN718 LMD • Frequency: 0, 25, 33, 41 kHz 
• Amplitude: 5 µm
• Densification 
• Grain refinement 
• Controlling formation of precipitates 
• Improving hardness, wear resistance, elastic modulus
[ 131 ]
Weldable IN718 LMD • Frequency: 19.8 kHz • Grain refinement 
• Improving YS, UTS, hardness
[ 132 ]
Weldable IN718 LMD • Frequency: 41 kHz 
• Amplitude: 5 µm
• Densification 
• Grain refinement 
• Controlling formation of precipitates 
• Improving YS, UTS, hardness, wear resistance
[ 133 ]
Weldable IN625 LMD • Frequency: 28–33 kHz 
• Amplitude: 6–13 µm
• Densification 
• Grain refinement 
• Improving hardness, wear resistance
[ 134 ]
Weldable IN625 WAAM • Frequency: 20 kHz • Grain refinement 
• Improving YS, UTS
[ 135 ]
Weldable IN718 LMD • Frequency: 24 kHz 
• Amplitude: 25 µm
• Improving hardness, wear resistance [ 136 ]
Weldable IN718 LMD • Frequency: 20 kHz 
• Power: 0, 2000, 3000, 4000 W
• Grain refinement 
• Controlling formation of precipitates 
• Improving hardness
[ 137 ]
Weldable IN625 WAAM • Frequency: 28 kHz 
• Power: 100 W
• Grain refinement 
• Controlling formation of precipitates 
• Improving YS, UTS
[ 138 ]
Figure 11. Comparative analysis of porosity between conven -
tional AM and VAAM processes [ 133 ]: (a, b) optical microscophy 
images in cross-section of deposits with and without VAAM 
process and (c) quantified porosity (%) under different vibration 
conditions.
VIRTUAL AND PHYSICAL PROTOTYPING 
 17

## Page 19

the acoustic cavitation generates strong shock waves in 
the melt pool that fragment long dendrites at the solid– 
liquid interface, as shown in Figure 12 (c) [ 140 ]. The stir -
ring action causes these fragmented small dendrites to 
re-enter into the residual liquid and disperses them 
throughout the melt pool, where they act as nuclei to 
promote heterogeneous nucleation [ 42 , 129 ]. These 
two mechanisms simultaneously increase the nucleation 
rate and enhance heterogeneous nucleation, which con -
verts large columnar grain structure into refined 
equiaxed grain structure in the VAAM process. Notably, 
as grain refinement effect is proportional to the 
applied vibration energy, increasing the frequency in 
VAAM can further promote the CET [ 131 ]. Consequently, 
the VAAM of weldable Ni-based superalloys can fabri -
cate deposits with finer grains than conventional AM 
by inducing the CET.
Beyond the densification and grain refinement, VAAM 
can also control the formation of precipitates in weld -
able Ni-based superalloys by reducing elemental segre -
gation during solidification. Figure 13 (a, b) shows 
scanning electron microscopy (SEM) images for the 
cross-section of IN718 deposits fabricated by LMD, com -
paring the formation of Laves phase with and without 
the application of vibration [ 137 ]. As shown in Figure 
13 (a), where vibration was applied, long striped shape 
Laves phase is observed. In conventional AM, alloying 
elements with low solubility in the γ matrix, such as 
Nb and Mo, segregate between columnar dendrites 
during solidification, forming long-striped Laves phase 
in interdendritic regions. In contrast, as shown in 
Figure 13 (b), fine granular Laves phase is observed 
when the vibration is applied. The formation of long 
striped Laves phase can be suppressed by stirring 
Figure 12. EBSD images of IN625 deposits according to vibration condition [ 42 ]: (a) without vibration and (b) with vibration; (c) sche -
matic of dendrite fracture mechanism within melt pool [ 140 ].
18 
 J. JANG ET AL.

## Page 20

action and acoustic cavitation induced by vibration, 
which promote the growth of the fine equiaxed grains. 
As these grains grow and merge during solidification, 
numerous small and isolated interdendritic regions 
form. This morphological change disperses Nb-rich pre -
cipiates, facilitating the formation of fine granular Laves 
phase [ 141 ]. In addition to the morphological changes in 
the Laves phase, the concentration of Nb and Mo within 
the Laves phase is reduced in VAAM deposits. Figure 
13 (c, d) shows the chemical composition of the Laves 
phase with and without vibration measure by SEM and 
electron diffraction scanning (EDS) analysis. When the 
vibration is applied, the concentrations of Nb and Mo 
within the Laves phase are lower compared to when 
the vibration is not applied. Generally, in conventional 
AM, constitutional supercooling occurs during solidifica -
tion due to the rapid cooling rate, leading to inhomo -
geneous compositions where solute atoms concentrate 
in liquid regions [ 142 ]. In contrast, the VAAM process 
enhances the internal flow of the melt pool, thereby 
moderating concentration gradients of solute elements. 
This helps suppress the segregation of elements such as 
Nb and Mo at the solid–liquid interface. Consequently, 
the VAAM process for weldable Ni-based superalloys 
contributes to suppressing the formation of detrimental 
phases and alleviating compositional inhomogeneity.
As discussed above, the application of vibration 
energy during the VAAM process leads to changes in 
the grain structure and the formation of precipitates, 
both of which enhance the mechanical properties of 
weldable Ni-based superalloy deposits. Figure 14 (a) 
shows the microhardness of IN718 deposits fabricated 
by LMD process under different frequency conditions 
[ 131 ]. The microhardness is improved when the 
vibration is applied during LMD process. In particular, 
In particular, according to Ning et al. [ 130 ], vibration fre -
quency plays an important role in microhardness of 
IN718 deposits fabricated by LMD. When the frequency 
is 25 and 41kHz, the microhardness reaches 254 and 
280 HV, respectively. The reason why microhardness is 
measured to be higher as frequency increases is that 
higher vibration frequencies promote greater grain 
refinement, thereby increasing the grain boundary 
density per unit volume in the deposit. This increased 
grain boundary density enhances microhardness by 
increasing resistance to plastic deformation, as grain 
boundaries hinder slip formation and dislocation move -
ment within grains. Moreover, as indicated by the Hall– 
Petch equation, the grain refinement improves not only 
the microhardness but also YS and UTS [ 42 , 135 , 137 , 138 ]. 
In addition to hardness, the tensile properties of the 
deposits are also significantly enhanced in VAAM. 
Figure 13. SEM-EDS analysis results for IN718 deposits [ 137 ]: SEM image showing (a) long-striped Laves phase without vibration and 
(b) fine granular Laves phase with vibration; EDS line analysis showing (c) segregation of Nb and Mo without vibration and (d) reduced 
segregation with vibration.
VIRTUAL AND PHYSICAL PROTOTYPING 
 19

## Page 21

Figure 14 (b) shows the tensile stress–strain curves for 
IN625 deposits fabricated by WAAM, comparing the 
tensile properties with and without vibration, depend -
ing on the build direction. The specimens fabricated 
by conventional WAAM exhibit lower UTS compared to 
those fabricated by VAAM, regardless of the horizontal 
or vertical direction to the build direction. Moreover, 
the differences in the tensile stress–strain curves for 
VAAM-processed specimens between the horizontal 
and vertical directions are reduced, which is attributed 
to the mitigation of anisotropy through the formation 
of equiaxed grains. Moreover, it is reported that, in 
IN718 of LMD, refined grains contribute to reducing 
the wear rate of the deposit due to their enhanced resist -
ance to friction and wear [ 131 ]. Regarding the influence 
of precipitates on the mechanical properties of weldable 
Ni-based superalloy deposits, it has been reported that, 
for IN718 of LMD, the suppression of Laves phase for -
mation in the interdendritic region helps disperse the 
localised concentration of Nb and promotes the 
uniform distribution of strengthening phases [ 137 ]. 
Similar to the effect of increased grain boundary 
density, these strengthening phases inhibit slip for -
mation and dislocation movement within the micro -
structure, thereby enhancing mechanical properties.
3.2.3. Process effects for non-weldable Ni-based 
superalloys
As discussed in Section 3 . 2 . 2 , the vibration-induced stir -
ring action and cavitation both contribute to the micro -
structural evolution by eliminating pores formed in the 
melt pool. This process densifies the deposit, induces 
the CET, and moderates Nb and Mo segregation. These 
effects, resulting from vibration in the VAAM process, 
occur regardless of the weldability of specific material. 
However, in addition to the improvements in mechan -
ical properties such as hardness, strength, and wear 
resistance in the VAAM of weldable Ni-based superal -
loys, the VAAM of non-weldable Ni-based superalloys 
demonstrates a significant effect in reducing crack 
formation.
The reduction of cracks observed in the VAAM of non- 
weldable Ni-based superalloys is attributed to the 
vibration-induced microstructural evolution, which inhi -
bits crack initiation. According to Tian et al. [ 143 ], who 
deposited IN738 samples using both the conventional 
LMD process and VAAM, the solidification cracking was 
only observed in conventional LMD deposited sample. 
This is because, when the vibration is not applied, long 
continuous liquid channels composed of low-melting- 
point eutectics are formed between the long straight 
columnar dendrites, and these liquid channels act as 
crack initiation points. As illustrated in Figure 15 (a), 
liquid channels rupture due to thermal contraction and 
solidification shrinkage during solidification and 
cooling, where the resulting shrinkage cavities are not 
sufficiently compensated by residual liquid, leading to 
solidification cracks. In contrast, in VAAM process, the 
acoustic cavitation induces shock waves, which break 
the long straight columnar dendrites. As shown in 
Figure 15 (b), this mechanism allows residual liquid to 
fully penetrate the space between the broken dendrites, 
thereby suppressing the formation of shrinkage cavities 
and reducing solidification cracking in the VAAM of non- 
weldable Ni-based superalloys.
In addition, the microstructural evolution caused by 
vibration not only suppresses crack initiation but also 
inhibits crack propagation. Figure 16 (a, b) shows EBSD 
Figure 14. (a) Microhardness value of specimens with different vibration frequency conditions [ 131 ]; (b) tensile stress–strain curves 
measured at different build orientations (0° and 90°) for conventional AM and VAAM specimens [ 42 ].
20 
 J. JANG ET AL.

## Page 22

images for IN738 deposits fabricated by LMD, comparing 
the crack propagation behaviour with and without the 
application of vibration [ 143 ]. As shown in Figure 16 (a), 
when the vibration is not applied, a crack propagation 
is observed along the grain boundary of long coarse 
columnar grains. The coarse columnar structure is rela -
tively vulnerable to crack propagation compared to 
the fine grains. This is because the thermal contraction 
and solidification shrinkage generate thermal stress, 
which is concentrated on a small number of grain 
boundaries [ 144 ]. In contrast, under the condition 
where vibration is applied, the crack propagation is rela -
tively limited. The fine equiaxed grain structure induced 
by vibration helps reduce cracks by dispersing thermal 
stress, which is the driving force for crack propagation, 
due to its high density of grain boundaries [ 145 ]. Fur -
thermore, the fine equiaxed structure has tortuous 
grain boundaries, unlike the straight boundaries found 
in columnar structures. Since the cracks tend to propa -
gate along paths requiring minimal energy, the cracks 
easily propagate along straight grain boundaries, as 
illustrated in Figure 16 (c). In contrast, the tortuous 
boundaries require more energy for crack propagation, 
effectively hindering the crack growth ( Figure 16 (d)). 
This crack prevention mechanism becomes even more 
effective with finer grain sizes. Therefore, VAAM 
Figure 15. Schematics showing the mechanism of crack formation [ 143 ]: (a) solidification cracking induced by shrinkage cavities 
between columnar dendrites without vibration and (b) the suppression of crack formation with vibration by fragmenting dendrites.
Figure 16. EBSD images and schematic of grain structure according to vibration condition [ 143 ]: (a, c) without vibration and (b, d) 
with vibration (BD: build direction, GB: grain boundary).
VIRTUAL AND PHYSICAL PROTOTYPING 
 21

## Page 23

effectively reduces both crack initiation and propa -
gation, enabling high-quality deposits with minimal 
cracks in the deposition of non-weldable Ni-based 
superalloys.
3.3. Rolling-assisted AM of Ni-based superalloys
3.3.1. Process methodology
Unlike peening, which induces plastic deformation 
through repetitive impact forces, rolling applies high 
loads through a roller to induce plastic deformation. 
Compared with peening, which typically induces 
surface plastic deformation to a depth of tens to hun -
dreds of micrometers, rolling offers the advantage of 
inducing plastic deformation to depths of several milli -
meters by continuously applying high loads through 
direct contact between the roller and the material 
[ 146 ]. RAAM, which leverages the advantages of 
rolling, has gained attention as a complementary 
approach to PAAM for mitigating tensile residual stres -
ses and improving the heterogeneous and anisotropic 
microstructures commonly observed in Ni-based super -
alloy deposits.
As shown in Figure 17 , the RAAM system typically 
consists of two major components: a heat source and 
a cylindrical hydraulic pressure roller. The RAAM 
process generally induces plastic deformation through -
out the deposit using a layer-wise rolling method. This 
method is primarily utilised in open-bed-type AM pro -
cesses such as LMD and WAAM, whereas its use is 
restricted in enclosed-bed-type processes like L-PBF 
and EB-PBF. Layer-wise RAAM differs in its implemen -
tation between LMD and WAAM owing to variations in 
their heat sources and material feeding methods. For 
the LMD process, which uses a laser heat source and 
metal powder, the deposition layers are relatively thin. 
To induce appropriate plastic deformation, a load of 1– 
10 kN is applied to the roller in this process [ 146 ]. Fur -
thermore, because the rapid solidification of the melt 
pool in LMD prevents distortion, in situ rolling is com -
monly employed, where the roller follows directly 
behind the heat source during layer-by-layer deposition, 
as shown in Figure 17 (a). In contrast, WAAM, which uti -
lises an arc heat source and a metal wire, produces 
thicker deposition layers than LMD. As a result, a 
higher load, often tens of kilonewtons, is applied to 
the roller to achieve the required plastic deformation 
in the WAAM process [ 147 ]. In addition, owing to the 
slower solidification rate of the molten material in 
WAAM, interlayer rolling is performed after cooling 
each layer to maintain the shape of the deposit, as 
shown in Figure 17 (b).
In contrast with the cylindrical-roller-based RAAM 
process, ball-type-roller RAAM is performed on com -
pleted deposits. This post-processing technique primar -
ily aims to enhance the surface properties through 
plastic deformation and is generally carried out with a 
load of less than 1 kN [ 148 ]. As shown in Figure 17 (c), 
the RAAM process uses a ball-type roller as a machine 
tool to treat the surface of the finished deposit. Unlike 
layer-wise RAAM, which is restricted to open-bed AM 
systems, the ball-type roller method has an advantage 
that can be applied to AM processes with both open- 
bed and close bed systems.
3.3.2. Process effects for weldable Ni-based 
superalloys
In the RAAM process for Ni-based superalloys, the effects 
of plastic deformation induced by rolling are consistent 
between weldable and non-weldable materials. Table 5
summarises the reported effects of RAAM applied to 
various materials and AM processes. Compared with 
Figure 17. Schematics of various RAAM systems: (a) in-situ rolling assisted AM, (b) interlayer rolling assisted AM, and (c) rolling post- 
treatment assisted AM.
22 
 J. JANG ET AL.

## Page 24

conventional AM, the most prominent external effects 
observed in the RAAM of Ni-based superalloys are the 
densification of the deposited material and the improve -
ment in the surface roughness. In conventional AM 
deposits, internal defects such as gas pores and LOF 
are frequently observed. Additionally, in high-depo -
sition-rate processes, a staircase-like pattern often 
forms between layers during layer-by-layer stacking, 
resulting in poor surface roughness. In contrast, the 
RAAM process achieves densification by closing internal 
defects, such as pores and LOF, through intense plastic 
deformation [ 148 , 149 ]. These effects are influenced by 
the rolling process parameters, and the roller pressure 
has a significant effect on densification, particularly. 
For example, when post-rolling treatment using ball 
type rollers was applied after the EB-PBF process of 
Table 5. Summary of the RAAM on Ni-based superalloys.
Type of 
weldability Alloy
AM 
process Assistant process Rolling process parameter Effects of RAAM process Ref.
Weldable IN718 EB-PBF Post rolling 
+grinding
• Rolling speed: 1000 mm/min 
• Rolling pressure: 10–40 MPa 
• Number of pass: 2
• Improving roughness, hardness, compressive 
residual stress 
• Mitigating internal defects
[ 149 ]
Weldable IN625 L-PBF Post rolling • Loading force: 2 kgf 
• Friction coefficient: 0.31
• Tensile residual stress 
relaxation
[ 148 ]
Weldable IN718 L-PBF Post rolling 
+ sand blast + 
HT
• Loading force: 250, 750 N 
• Rolling speed: 350, 1050 RPM
• Improving roughness, wear resistance, hardness [ 150 ]
Weldable IN718 L-PBF Post rolling 
+cooling 
condition
• Loading force: 300, 600, 900 N 
• Cooling condition: RT, −45, 
200°C
• Improving roughness, microhardness [ 151 ]
Weldable IN718 L-PBF Post rolling 
+ electric current
• Rolling speed: 100, 200, 300 
RPM 
• Feed rate: 0.08, 0.16, 0.24 mm/ 
rev 
• Current density: 0, 5, 10 A/mm
2 
• Static force: 100, 200, 300 N 
• Pass number: 1, 2, 3
• Improving roughness, hardness, fatigue life 
• Tensile residual stress 
relaxation
[ 152 ]
Weldable IN718 L-PBF Post rolling 
+ electric current
• Rolling speed: 100, 200, 300 
RPM 
• Feed rate: 0.08, 0.16, 0.24 mm/ 
rev 
• Current density: 0, 5, 10 A/mm
2 
• Static force: 100, 200, 300 N 
• Pass number: 1, 2, 3
• Improving roughness, hardness, fatigue life 
• Tensile residual stress 
relaxation
[ 153 ]
Weldable IN718 L-PBF Post rolling 
+ electric current
• Rolling speed: 2000 mm/min 
• Static force: 100 N 
• Current density: 0, 5, 10 A/mm
2 
• Pass number: 1, 2, 3
• Improving roughness, hardness, fatigue life 
• Tensile residual stress 
relaxation
[ 155 ]
Weldable IN718 LMD In-situ rolling • Loading force: 3 kN • Improving hardness, 
YS, UTS, EL 
(at high temperature)
[ 156 ]
Weldable IN718 LMD In-situ rolling 
+ HT
• Loading force: 3 kN • Improving hardness, 
YS, UTS, EL 
(at high temperature)
[ 157 ]
Weldable IN718 LMD In-situ rolling • Roller radius: 8 mm 
• Friction coefficient: 0–0.3
• Tensile residual stress 
relaxation
[ 158 ]
Weldable IN718 LMD In-situ rolling • Roller radius: 8 mm 
• Friction coefficient: 0.3
• Tensile residual stress 
relaxation 
• Improving hardness, 
YS, UTS
[ 159 ]
Weldable IN718 WAAM In-situ rolling • Rolling compression: 0.125–0.5 
mm 
• Friction coefficient: 0.1–0.5
• Tensile residual stress 
relaxation 
• Improving EL
[ 160 ]
Weldable IN718 WAAM Interlayer Rolling 
+ HT
• Loading force: 50, 75 kN 
• Roller radius: 50 mm 
• Roller travel speed: 2 m/min
• Improving hardness, 
YS, UTS, EL
[ 147 ]
Weldable IN718 WAAM Interlayer rolling 
+ HT
• Loading force: 0, 50, 75 kN 
• Roller radius: 50 mm 
• Roller travel speed: 5 mm/s
• Tensile residual stress 
relaxation 
• Improving hardness, YS, UTS 
(at high temperature)
[ 146 ]
Weldable IN718 WAAM Interlayer rolling 
+ HT
• Loading force: 0, 50, 75 kN 
• Roller radius: 50 mm
• Improving hardness, YS, UTS [ 161 ]
Weldable IN718 WAAM Interlayer rolling 
+ HT
• Loading force: 50 kN • Tensile residual stress 
relaxation
[ 162 ]
Weldable IN718 WAAM In-situ rolling 
+ HT
• Deformation rate: 0, 15, 30% • Improving tensile strength, EL, impact energy [ 163 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 23

## Page 25

IN718, internal defects such as pores, cracks, and LOF 
were noticeably reduced in the rolled samples at high 
rolling pressures (30 and 40 MPa) compared to the as- 
built samples, as shown in Figure 18 (a) [ 149 ]. Addition -
ally, in the RAAM process of Ni-based superalloys, 
surface defects, such as spatter and slag, and staircase- 
effect-induced surface patterns are both eliminated 
through plastic deformation. This contributes to the 
improvement of the surface roughness of the deposit, 
as shown in Figure 18 (b). Previous studies have demon -
strated that in RAAM using a ball-type roller, the surface 
roughness of L-PBFed IN718 deposits decreases as the 
roller load and number of rolling passes increase [ 150– 
152 ]. However, excessive rolling loads and an excessive 
number of process repetitions may degrade the 
surface quality, necessitating proper process control. 
Recently, research has focused on addressing this issue 
by integrating additional techniques, such as applying 
an electric current during the rolling process or combin -
ing it with grinding and sandblasting. These approaches 
aim to improve surface roughness under lower roller 
loads and optimise the RAAM process by reducing 
mechanical input requirements while maintaining or 
enhancing surface integrity [ 149 , 153–155 ].
In addition to the externable improvements in den -
sification and surface roughness, the RAAM process for 
Ni-based superalloys can also enhance the tensile 
residual stresses formed during the heating and 
cooling cycles of the deposition process. According to 
finite element analysis (FEA) based simulation studies, 
the compressive residual stress induced during RAAM 
is attributed to the compressive plastic deformation of 
the material and the restoring force due to the elastic 
springback occurring under the deformation region. In 
this regard, compressive residual stress formed during 
the RAAM is similar to the compressive residual stress 
formed during the PAAM process [ 148 ]. However, 
unlike PAAM, which effect limited to a surface, RAAM 
induces deep compressive plastic deformation along 
multiple layers due to a load of several tens of kilonew -
tons. As a result, the compressive residual stresses 
induced by RAAM are significantly deeper than those 
induced by PAAM. Specifically, the layer-wise RAAM 
process can induce plastic deformation to depths of 
tens of millimeters, allowing for the simultaneous gener -
ation of compressive residual stresses across multiple 
layers and effectively counteracting the tensile residual 
stresses formed throughout the entire deposit. These 
compressive residual stresses induced during layer- 
wise RAAM are influenced by the rolling process par -
ameters. In particular, during interlayer-rolling-assisted 
WAAM, which is a layer-wise RAAM process, increasing 
the roller load has been shown to correspond to 
deeper plastic deformation [ 146 , 147 , 161 , 162 ]. Likewise, 
during in situ rolling-assisted LMD, another layer-wise 
RAAM process, deeper plastic deformation is observed 
with higher roller loads. Moreover, as the distance 
between the heat source and roller increases, a 
Figure 18. Differences in surface characteristics and residual stress between conventional AM and RAAM processes: (a) optical micro -
graph (OM) images of the EB-PBFed IN718 depoists according to rolling pressure [ 149 ], (b) measured roughness analysis of L-PBFed 
IN718 deposits [ 155 ], and (c) simulation results of residual stress for WAAM-fabricated IN718 deposits according to friction coefficients 
[ 158 ].
24 
 J. JANG ET AL.

## Page 26

combination of high-temperature plastic deformation 
and the cooling effect induced by the roller reduces 
the tensile residual stress within the deposited material 
[ 158–160 ]. In addition, the frictional condition of the 
roller is another factor influencing the residual stress. 
According to Raj et al. [ 158 ], who analyzed the stress dis -
tribution resulting from in-situ rolling during the LMD 
process of IN718, the deposit subjected to in-situ 
rolling exhibited overall lower residual stresses com -
pared to the as-deposited sample. As shown in Figure 
18 (c), a higher friction coefficient of the roller promoted 
the formation of greater compressive stresses within the 
deposit.
In addition, the plastic deformation applied to each 
layer during the RAAM process for Ni-based superalloys 
can induce a microstructural evolution within the 
deposit. The intense load exerted by the roller generates 
plastic deformation, leading to numerous dislocations 
and twins in the microstructure of the deposit 
[ 154 , 159 , 161 ]. As discussed in Section 3 . 1 . 2 , these 
regions with a high density of dislocations and twins 
exhibit interactions that cause entanglement, resulting 
in work hardening and increasing the deformation resist -
ance. Furthermore, the increased lattice deformation 
within the microstructure accumulates lattice energy, 
creating a thermodynamically unstable state that serves 
as a driving force for recrystallization. In particular, in 
the layer-wise RAAM process, plastic deformation and 
heat input repeatedly occur during layer-by-layer depo -
sition. Because the depth of plastic deformation 
exceeds the thickness of a single deposition layer, 
recrystallization occurs throughout the entire deposit 
[ 146 , 147 , 157 ]. For instance, during the WAAM process 
of IN718, the as-built deposit exhibits a columnar grain 
structure, whereas the inter-pass rolled deposit displays 
the formation of recrystallized equiaxed grains at its 
center, as shown in Figure 19 (a). Such recrystallization is 
further promoted as the degree of plastic deformation 
increases. As illustrated in Figure 19 (b), in the WAAM 
process of IN718, higher inter-pass rolling pressures lead 
to the formation of finer recrystallized grains compared 
to the as-built sample. Additionally, as greater plastic 
deformation promotes recrystallization, the grain size 
becomes finer with higher roller loads, as shown in 
Figure 19 (b). This indicates that increased roller loads 
during RAAM not only enhance recrystallization but also 
lead to significant grain refinement.
The recrystallization phenomenon observed in layer- 
wise RAAM differs from that in the layer-wise PAAM 
process discussed in Section 3 . 1 . 2 . In layer-wise PAAM, 
incomplete recrystallization of the deposited material 
partially retains the work hardening effects. Simul -
taneously, the microstructure exhibits anisotropic 
characteristics, with alternating layers of coarse colum -
nar grains and fine equiaxed grains. In contrast, in the 
layer-wise RAAM process, the deposits fully recrystallize, 
completely consuming the lattice deformation respon -
sible for work hardening, as shown in Figure 19 (c). As 
a result, the coarse columnar grains that grow epitaxially 
during layer-by-layer deposition are entirely trans -
formed into fine isotropic equiaxed grains, effectively 
eliminating the material anisotropy commonly observed 
Figure 19. Microstructural differences in WAAM-fabricated IN718 deposits with and without inter-pass rolling: (a) OM images with 
and without inter-pass rolling [ 147 ], (b) magnified OM images according to the rolling load [ 146 ], and (c) kernel average misorienta -
tion maps according to the rolling load based on EBSD analysis [ 161 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 25

## Page 27

in conventional AM [ 147 , 161 ]. Interestingly, the mechan -
ism underlying this recrystallization phenomenon, which 
resolves material anisotropy, varies depending on the 
two approaches of layer-wise RAAM. During interlayer 
rolling-based RAAM ( Figure 17 (b)), static recrystallization 
occurs as the deposit sequentially experiences plastic 
deformation and heat input from the heat source. 
Because static recrystallization relies solely on the 
stored deformation energy, it is characterised by a rela -
tively low driving force for recrystallization. On the other 
hand, during the in-situ rolling-based RAAM ( Figure 
17 (a)), dynamic recrystallization occurs as the deposit 
simultaneously experiences heat input and plastic defor -
mation. Dynamic recrystallization, which has a relatively 
high driving force due to the continuous supply of heat 
and plastic strain energy, is more advantageous in pro -
ducing a uniform and fine-grain structure than static 
recrystallization.
Based on the aforementioned effects, the RAAM 
process for Ni-based superalloys offers significant 
benefits for various mechanical properties compared 
with conventional AM processes, particularly the hard -
ness. As shown in Figure 20 (a), IN718 deposits fabricated 
by the inter-pass rolled WAAM process exhibit higher 
surface hardness compared to the as-built WAAM 
deposit. Notably, even without post-heat treatment, 
the upper region showed excellent hardness compar -
able to that of the AD+SQA sample. Moreover, when 
SQA was performed on the IR deposit, an even higher 
hardness was achieved throughout the entire deposit. 
This improvement due to inter-pass rolling is attributed 
to the combined effects of densification, work harden -
ing, and grain refinement, which enhance resistance to 
deformation at grain boundaries and within grains, par -
ticularly near the surface [ 162 , 164 ].
Meanwhile, RAAM can improve not only the hardness 
near the surface but also tensile strength along the entire 
deposits based on deep plastic deformation 
[ 149 , 152 , 153 , 155 ]. Figure 20 (b) shows the stress–strain 
curves of WAAM deposits of IN718 under different 
rolling pressures. Compared to the as-deposit, the inter- 
layer rolled deposits exhibited superior YS and UTS, and 
both YS and UTS increased with higher rolling pressures. 
Furthermore, the beneficial effect of inter-layer rolling 
was found to be more pronounced after post-solution 
treatment. This effect is attributed to recrystallization 
occurring between layers, forming fine equiaxed grains 
throughout the deposit during layer-wise RAAM. Such 
Figure 20. Differences in the mechanical properties between between conventional AM and RAAM processes: (a) Depth-wise micro -
hardness of WAAM-fabricated IN718 deposits under different IR and SQA conditions [ 162 ], (b) tensile properties of WAAM-fabricated 
IN718 deposits under different rolling load at ambient temperature [ 146 ], (c) tensile properties of WAAM-fabricated IN718 deposits 
according to X-direction(scanned direction) and Z-direction(built direction) [ 163 ] and (d) tensile properties of WAAM-fabricated IN718 
deposits under different rolling load at elevated temperature [ 146 ].
26 
 J. JANG ET AL.

## Page 28

recrystallization promotes the formation of a fine 
equiaxed grain structure, thereby increasing the density 
of grain boundaries per unit volume. The increased 
grain boundary density hinders dislocation movement 
and enhances resistance to deformation, which ultimately 
leads to an improvement in tensile strength. Moreover, 
the fine, uniform equiaxed grains induced by layer-wise 
RAAM help alleviate anisotropy throughout the deposit 
[ 163 ]. Figure 20 (c) presents a comparison of the tensile 
properties in the X and Z directions of IN718 deposits fab -
ricated by the WAAM-based RAAM process, with varying 
rolling deformation rates. As the deformation rate 
induced by rolling increases, the anisotropy in tensile 
strength decreases compared to the as-deposited 
sample. Also, for the RAAM samples subjected to post- 
T6 heat treatment, the anisotropy in not only tensile 
strength but also YS and EL is further mitigated.
The improvements in tensile properties due to RAAM 
are effective not only at ambient temperature but also 
at elevated temperatures [ 146 ]. In general, the tensile per -
formance of Ni-based superalloy deposits degrades at 
elevated temperatures as a result of mechanisms includ -
ing creep, grain boundary weakening, and dynamic 
strain aging. However, as previously discussed, applying 
RAAM of Ni-based superalloy can effectively offset such 
high-temperature degradation by promoting work hard -
ening and grain refinement through plastic deformation. 
For instance, when comparing stress–strain curve in 
Figure 20 (b) and (d), enhancement of the tensile proper -
ties remains effective with increasing rolling pressure, 
despite the presence of dynamic strain aging owing to 
elevated temperature. In fact, the tensile strength of the 
RAAM sample processed with a rolling pressure of 75 
kN under elevated temperature closely approached that 
of the as-deposited sample tested at ambient tempera -
ture. This indicates that RAAM is a highly effective tech -
nique for securing the tensile performance of Ni-based 
superalloys under an elevated temperature environment.
Figure 21. Optical micrographs (OM) and SEM images showing the precipitate evolution in WAAM-fabricated IN718 deposits with and 
without rolling process [ 163 ]: as-built deposits (a) before and (b) after heat treatment; 30% deformed RAAM deposit (c) before and (d) 
after heat treatment.
VIRTUAL AND PHYSICAL PROTOTYPING 
 27

## Page 29

As discussed above, RAAM enhances the mechanical 
properties of deposits by inducing compressive residual 
stresses and microstructural evolution, even when used 
independently. However, similar to the PAAM process 
discussed in Section 3 . 1 . 2 , RAAM also influences the pre -
cipitation of strengthening phases during post-heat 
treatments following the AM process for Ni-based super -
alloys. Comparing Figure 21 (a) and Figure 21 (c), the 
intense load and friction induced by the roller during 
RAAM not only fracture the epitaxially grown dendrites 
in the dendritic regions but also fragment the precipitates 
that segregate in the interdendritic regions during the 
solidification of molten metal [ 120 , 121 , 146 , 157 , 163 ]. In 
particular, the Laves and δ phases, which are detrimental 
precipitates formed by segregation in the interdendritic 
regions, are representative phases that tend to fragment 
during the RAAM process owing to their brittle character -
istics. The fragmentation and dispersion of such detri -
mental phases within the microstructure not only 
alleviate the concentration of Nb—the key element in 
the strengthening phase—but also promote its solubility 
during subsequent heat treatments.
As shown in Figure 21 (b, d), after the heat treatment 
following RAAM, the microstructure shows significantly 
fewer Laves and δ phases owing to the fragmentation 
effect described earlier. According to previous studies, 
in the RAAM process for Ni-based superalloys, increasing 
the load during layer-wise rolling further fragments the 
Laves and δ phases. Consequently, when a solution 
treatment is performed at temperatures above 970°C 
after the RAAM process, the dissolution of the Laves 
and δ phases is accelerated, thus increasing the solubi -
lity of Nb in the γ matrix [ 163 ]. Furthermore, performing 
an aging treatment below 720°C after the solution treat -
ment promotes the precipitation of the strengthening 
phase γ’’, leading to finer, more uniformly distributed 
γ’’ phases within the γ matrix. This demonstrates that 
when applying a post-heat treatment, RAAM is more 
advantageous than conventional AM in improving the 
mechanical properties of the deposit.
Based on the findings from previous studies, RAAM is 
being considered for repair applications in maintenance, 
repair, and overhaul (MRO) contexts, unlike PAAM, which 
has mainly focused on improving surface properties of 
completed parts [ 165 ]. This is primarily because rolling is 
most compatible with open-bed AM processes such as 
LMD and WAAM, which are frequently studied for repair 
purposes. One of the representative examples of RAAM 
applied to real industrial products is the exhaust valve of 
a marine diesel engine. Zhao et al. [ 166 ] proposed a 
method in which IN718 is locally deposited onto SNCrW 
steel exhaust valves—exposed to long-term high temp -
eratures and repeated mechanical impacts—using 
WAAM, followed by localised plastic deformation via 
rolling. The rolled region exhibited lower residual stress 
compared to the base metal and demonstrated increased 
hardness due to fine recrystallized grains and work harden -
ing. These results suggest that RAAM offers a clear advan -
tage in applications requiring localised mechanical 
property enhancement or component repair. Based on 
these advantages, RAAM is expected to be applied to 
other complex-shaped Ni-based superalloy components, 
such as turbine discs in aero engines, and mill rolls or 
cutting tools in shield tunnelling machines.
4. Thermal-energy-assisted AM of Ni-based 
superalloys
In the AM process of Ni-based superalloys, the localised 
heat input from a laser or electron beam increases the 
thermal gradient (G) and solidification speed (R) at the 
solid–liquid interface of the melt pool [ 45 ]. Elevated G 
and R values can alter the solidification behaviour of 
the deposit, thus modifying the grain morphology of 
the Ni-based superalloy or changing the size and 
shape of precipitates, such as the Laves and carbide 
phases. These changes can ultimately increase the sus -
ceptibility to cracking of the deposit or even degrade 
the deposit’s mechanical properties. Additionally, in 
environments where high G and R values are present, 
the melt pool may solidify unevenly, and the surround -
ings of the melt pool may rapidly expand and contract, 
thus heightening the thermal residual stresses within 
the deposit. Crucially, a high thermal residual stress 
within the deposit can cause severe distortion, which 
can degrade the geometrical accuracy of the final 
product; therefore, the effect of thermal residual stress 
during the AM process of Ni-based superalloys must 
be considered. To address these issues, many research -
ers have focused on providing additional thermal 
energy during the AM of Ni-based superalloys to 
reduce and precisely control the G and R values during 
solidification. Thermal energy can be supplied by utiliz -
ing various instruments during the AM process, such 
as hot plates, induction coils, and laser or electron 
beams, as shown in Figure 22 (a–c). For each instrument, 
the method of delivering the thermal energy varies 
depending on whether the AM process must preserve 
the powder bed in a chamber and maintain a vacuum 
environment, which are conditions required for the EB- 
PBF process.
The thermal energy generated by various instruments 
can be applied to the AM process to mitigate issues of 
low deposition quality. Accordingly, Section 4 of this 
review summarises and discusses the current research 
progress and the diversity of thermal-energy-assisted 
28 
 J. JANG ET AL.

## Page 30

AM processes. Specifically, it analyzes how various 
instruments capable of providing thermal energy affect 
the grain morphology and microstructure of weldable 
and non-weldable Ni-based superalloys. Each instru -
ment is discussed in relation to the factors contributing 
to the deposition quality of AM Ni-based superalloy 
deposits, such as the mechanical properties or crack 
susceptibility.
4.1. Hot-plate-assisted AM of Ni-based 
superalloys
4.1.1. Process methodology
Hot plates are widely employed in thermal-energy- 
assisted AM processes, which effectively affect the 
temperature gradient (G) and solidification rate (R) 
values [ 167 ]. These effects change the grain mor -
phology of the deposit as well as the size and shape 
of precipitates, which in turn can enhance the mech -
anical properties of weldable alloys and prevent distor -
tion issues in the deposit by reducing the thermal 
residual stress. As shown in Figure 23 (a), various 
types of hot plates are used to generate thermal 
energy, including electric hot plates with resistive 
heating elements ( Figure 23 (a-1)) and electromagnetic 
hot plates using pancake-shaped induction coils 
( Figure 23 (a-2)) [ 168 , 170 ]. These hot plates can be 
broadly applied in various AM processes, namely 
LMD, WAAM, L-PBF and EB-PBF. In the LMD and 
WAAM processes, which are classified as directed 
energy deposition (DED) methods, a hot plate is 
placed beneath the substrate to preheat it by supply -
ing the thermal energy, onto which the Ni-based 
superalloy is deposited in powder or wire form [ 170 ]. 
The hot plate beneath the substrate can be controlled 
by utilizing an additional temperature control module, 
and the temperature is measured in real time using 
either a non-contact-type pyrometer or a contact- 
type thermocouple attached to the substrate 
[ 43 , 168 ]. Meanwhile, in the L-PBF and EB-PBF pro -
cesses, which are classified as a PBF method, hot 
plates are either separately installed inside the build 
chamber ( Figure 23 (b)) or integrated into the 
machine as internal heating systems ( Figure 23 (c)), 
through which thermal energy is supplied to the 
powder. In addition, an infrared thermometer installed 
inside the chamber can measure the temperature of 
the powder bed in real time, as depicted in Figure 
23 (d). Thermal energy generated from hot plates— 
installed in various configurations across different AM 
systems—affects the G and R values during the AM 
process. These effects in G and R values directly 
Figure 22. Three-dimensional schematics of the instruments utilised during the thermal-energy-assisted AM of Ni-based superalloys: 
(a) a hot plate-assisted AM process, consisting of a hot plate with (a-1) the substrate or (a-2) the PBF chamber; (b) an induction coil- 
assisted AM process, consisting of a induction coil (b-1) with the substrate or (b-2) the PBF chamber; and (c) process-heat-source- 
assisted AM process, consisting of a process-heat-sourece (c-1) with the substrate or (c-2) the PBF chamber (image not to scale).
VIRTUAL AND PHYSICAL PROTOTYPING 
 29

## Page 31

influence the microstructural evolution, ultimately 
impacting the overall deposition quality in both weld -
able and non-weldable Ni-based superalloys.
4.1.2. Process effects for weldable Ni-based 
superalloys
In the Hot-Plate-Assisted Additive Manufacturing 
(HPAAM) process for weldable alloys, the hot plate 
is utilised in order to enhance the deposition 
quality of the weldable alloy. Table 6 summarises 
the process parameters and effects of HPAAM 
applied to weldable alloys. Specifically, the hot plate 
can effectively prevent the thermal residual stress 
from high thermal gradients during AM and 
improve the mechanical properties of the weldable 
Ni-based superalloys. These effects are associated 
with the G and R values induced by the thermal 
energy generated from the hot plate. The G and R 
Figure 23. Overview of the specific systems of the hot-plate-assisted AM of Ni-based superalloys: photographs and schematics depict -
ing (a-1) the hot-plate-assisted AM process using an electrical heater or (a-2) a pancake coil [ 168 , 169 ], (b) photographs of the hot- 
plate-assisted AM process with an external temperature control module [ 171 ], (c) schematic of a commercial L-PBF system with an 
integrated heating plate [ 172 ], and (d) photograph of the multiple preheating platforms for the EB-PBF process with an infrared ther -
mometer [ 173 ].
Table 6. Summary of the HPAAM on weldable Ni-based superalloys.
Type of weldability Alloy AM process Hot plate process parameter Effects of HPAAM process Ref.
Weldable IN625 LMD
• 
Temperature: 0, 400°C . Reduced residual stress
. Grain coarsening
[ 43 ]
Weldable IN718 LC
• 
Temperature: 0, 200, 400°C
• 
Grain coarsening [ 168 ]
Weldable IN718 L-PBF
• 
Temperature: 200, 600°C . Grain coarsening
. Enlarged melt pool
[ 174 ]
Weldable IN718 L-PBF
• 
Temperature: 50, 100, 150°C . Improving tensile strength, hardness
. Reduced residual stress
. Grain coarsening
[ 175 ]
Weldable IN718 L-PBF
• 
Temperature: 100, 200, 300, 400, 500 °C . Enlarged melt pool
. Grain coarsening
[ 171 ]
Weldable IN718 L-PBF
• 
Temperature: 20, 100, 300, 500°C . Reduced residual stress
. Reduced build direction distortion
. Grain coarsening
[ 176 ]
Weldable IN718 EB-PBF
• 
Temperature: 950, 1000°C . Improving hardness
. Grain coarsening
[ 44 ]
Weldable IN718 LMD
• 
Temperature: 100, 150, 200°C . Reduced residual stress
. Grain coarsening
[ 177 ]
30 
 J. JANG ET AL.

## Page 32

values are governed by the thermal energy distri -
bution during processing, and they vary depending 
on the applied preheating temperature. For 
example, in IN718 deposit fabricated by laser clad -
ding (LC) process, Figure 24 (a-1) and (a-2) show the 
G and R, respectively, as a function of the preheating 
temperature. As the preheating temperature increases 
from 20°C to 400°C, both G and R values decrease 
consistently across the different heights in deposits 
(A, B, and C) [ 168 ]. The decreased G and R values ulti -
mately affect the grain morphology and precipitation 
behaviour, which then influence the mechanical 
properties of the weldable alloy while also effectively 
reducing the thermal residual stress.
Numerous studies have thoroughly investigated the 
influence of hot-plate-generated thermal energy on 
grain morphology, confirming that reduced solidifica -
tion time caused by hot plate preheating leads to 
changes in grain size. The thermal energy from the hot 
plate delays the solidification process, thereby extend -
ing the time available for grain growth during the 
liquid-to-solid phase transition. This prolonged solidifi -
cation time allows grains to grow larger, ultimately pro -
moting the formation of coarser grains, which can be 
Figure 24. (a-1) Temperature gradient, (a-2) solidification rate, and (a-3) PDAS values with three preheating conditions of single-layer 
cladding [ 168 ]; (b) PDAS (left) and SDAS (right) of the deposit at various preheating temperatures [ 174 ]; (c-1) EBSD maps of the 
samples processed at hot plate temperatures of 50, 100, and 150°C, and (c-2) LAGB fraction as a function of misorientation angle 
for samples processed at 50, 100, and 150°C [ 175 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 31

## Page 33

evaluated using indicators such as columnar dendrite 
width [ 43 ], primary dendrite arm spacing (PDAS) and 
secondary dendrite arm spacing (SDAS), and interden -
drite spacing [ 175 ]. Figure 24 (a-3) presents the PDAS 
width at various heights of the IN718 deposit fabricated 
by the LC process under different preheating tempera -
tures, while Figure 24 (b) shows both PDAS and SDAS 
at different heights with increasing preheating tempera -
tures. Both figures demonstrate that higher preheating 
temperature leads to an increase in PDAS and SDAS 
width, indicating the formation of coarser grains 
[ 168 , 174 ]. The hot plate influences not only the grain 
size but also the grain misorientation angle, and this 
effect varies with the preheating temperature. Figure 
24 (c-1) presents an EBSD map of the IN718 deposit fab -
ricated by the L-PBF process, showing that increasing 
the preheating temperature from 50°C to 150 °C leads 
to more randomised grain orientations in samples. Fur -
thermore, Figure 24 (c-2) demonstrates that the 
number fraction of low-angle grain boundaries 
(LAGBs), particularly within the 2–4° range, gradually 
decreases with increasing hot plate temperature. This 
increase in grain orientation randomness is attributed 
to the thermal energy from the hot plate, which disrupts 
the uniform heat flow toward the substrate and induces 
variations in grain growth direction [ 175 ]. The reduction 
in LAGB fraction implies the occurrence of recrystalliza -
tion, which lowers the dislocation density and reduces 
the stored strain energy, thereby mitigating thermal 
residual stresses [ 178 , 179 ].
Furthermore, the HPAAM process influences not only 
the grain morphology of the deposit but also the for -
mation and distribution of various precipitated phases 
that typically form during the AM process. For 
example, according to Jin et al. [ 168 ], the Laves phase 
precipitates in IN718 deposited by LC irregularly along 
the interdendritic regions, and its volume fraction 
increases as the hot plate temperature rises from 200° 
C to 400°C. This is attributed to the reduced cooling 
rate caused by the hot plate during the solidification 
process, which promotes the segregation of Nb atoms 
into the interdendritic areas. In addition to the Laves 
phase, the hot-plate-induced reduction in the cooling 
rate also impacts the precipitation of the carbide 
phase. Furthermore, the HPAAM process significantly 
influences the formation of strengthening phases in 
weldable alloys. In particular, the EB-PBF process utiliz -
ing HPAAM typically operates at elevated temperatures 
ranging from 950 to 1500°C, which facilitates the precipi -
tation of strengthening phases such as δ, γ
′
and γ
′′
[ 25 , 44 , 180 ]. For example, as shown in Figure 25 (a), 
which represents the phase fractions of various precipi -
tation such as δ, γ
′
and γ
′′
at different preheating temp -
eratures (1000°C for Build-H and 950°C for Build-L), the 
dominant precipitation phase in the IN718 deposit 
changes depending on the applied preheating 
Figure 25. (a) Phase fractions of γ
′
, γ
′′
, δ phases, and MC carbides of samples processed at different preheating temperatures [ 44 ], (b) 
tensile properties of samples processed under different heat treatment, including as-deposited (AD) and substrate preheating (SP) 
[ 43 ], and (c) average hardness of samples fabricated with different preheating temperatures: build-H (1000°C) and build-L (950°C) [ 44 ].
32 
 J. JANG ET AL.

## Page 34

temperature. When the preheating temperature exceeds 
the δ-solvus temperature (up to 1000°C) in the deposit, 
the δ phase dissolves, retaining Nb and Ni in the 
matrix and promoting precipitation of γ
′′
[ 44 ]. Conver -
sely, preheating below the δ-solvus (up to 950°C) pro -
motes intragranular δ phase formation, which 
consumes Nb and consequently suppresses the precipi -
tation of γ
′′
.
As discussed above, the thermal energy introduced 
by the hot plate significantly affects both the grain mor -
phology and the formation of various precipitated 
phases within the deposit. These microstructural 
changes, in turn, have a substantial impact on the mech -
anical properties of weldable alloys. Grain coarsening 
induced by thermal energy reduces the movement of 
dislocations within the lattice, thereby decreasing the 
microhardness and UTS. Conversely, the reduction in 
the number of grain boundaries due to grain coarsening 
enhances ductility, thus increasing EL [ 43 ]. For example, 
Figure 25 (b) presents the variations in UTS, YS and EL of 
the IN625 deposit fabricated by the LMD process under 
different thermal treatments, including substrate pre -
heating. Among all conditions, the SP-treated sample 
exhibits the lowest UTS and YS values, but shows the 
highest EL, indicating a trade-off between strength 
and ductility induced by substrate preheating. In 
addition to these mechanical properties, using a hot 
plate enables the precipitation of γ
′′
. The precipitation 
of γ
′′
plays a key role in enhancing the hardness of the 
deposit, and this effect is strongly dependent on the pre -
heating temperature. Figure 25 (c) illustrates the average 
hardness values of IN718 fabricated by the EB-PBF 
process under different preheating conditions. It is 
evident that the specimen processed at 1000°C exhibits 
higher hardness compared to that processed at 950°C, 
indicating that increased thermal energy promotes γ
′′
precipitation by enhancing the diffusion of Ni and Nb 
[ 44 ]. In addition to affecting the mechanical properties, 
the hot plate also effectively prevents distortion by redu -
cing the thermal residual stress. The thermal energy 
supplied by the hot plate can help alleviate residual 
stress by lowering both G and R values within the melt 
pool [ 176 , 177 ].
4.1.3. Process effects for non-weldable Ni-based 
superalloys
Unlike weldable alloys, non-weldable alloys are signifi -
cantly more prone to thermal cracking during additive 
manufacturing due to their high Al and Ti content, 
which has inherently limited their practical application 
in AM. Table 7 summarises the effects of HPAAM on 
non-weldable alloys under various preheating tempera -
tures. The HPAAM process offers a promising solution to 
this challenge by effectively reducing crack formation in 
these difficult-to-process materials. The crack suscepti -
bility primarily arises from factors such as unfavorable 
grain morphology and various precipitates within the 
deposit. These factors are strongly influenced by the 
thermal gradient and solidification rate, which can be 
modified through thermal energy from the hot plate. 
By controlling these thermal-solidification conditions, 
hot plate preheating facilitates microstructural evolution 
and mitigates thermal residual stress, thereby effectively 
mitigating crack susceptibility.
Specifically, regarding the grain morphology, the hot 
plate can affect on grain morphology by reducing the G 
and R values. In fact, for representative non-weldable 
Ni-based superalloys, such as IN738LC, the thermal 
energy influences misorientation angle, which is related 
to crack susceptibility, and this effect is strongly depen -
dent on the preheating temperature. As shown in 
Figure 26 (a), which presents EBSD maps of the XY and 
XZ cross-sections of IN738LC fabricated via the L-PBF 
process, an increase in preheating temperature leads to 
a notable change in the grain boundary character distri -
bution. Specifically, the fraction of LAGBs (2–10°) 
increases at elevated temperatures, while the fraction of 
high-angle grain boundaries (HAGBs, >15°) decreases 
[ 182 ]. This shift does not necessarily imply enhanced 
recrystallization but rather indicates that recovery is 
Table 7. Summary of the HPAAM on non-weldable Ni-based superalloys.
Type of weldability Alloy AM process Hot plate process parameter Effects of HPAAM process Ref.
Non-weldable IN939 L-PBF
• 
Temperature: 0, 200, 400°C . Improving UTS, hardness, 0.2% proof stress
. Grain coarsening
. Enlarged melt pool
[ 181 ]
Non-weldable IN738LC L-PBF
• 
Temperature: 200, 700°C . Improving UTS (Build & Horizontal dir.)
. Crack suppression
. Grain coarsening
[ 182 ]
Non-weldable IN738LC EB-PBF
• 
Temperature: 1000°C . Grain coarsening
. Crack suppression
[ 173 ]
Non-weldable René 104 LSF
• 
Temperature: 0, 450, 600, 750°C . Improving microhardness
. Reduced crack intensity
[ 183 ]
Non-weldable Mar-M-247 
CM 247LC
LMD
• 
Temperature: 900°C . Improving tensile strength
. Crack suppression
. Grain coarsening
[ 170 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 33

## Page 35

facilitated at higher temperatures. The thermal energy 
provided by preheating promotes dislocation rearrange -
ment and partial annihilation, which reduces internal mis -
orientations and leads to the stabilisation of the subgrain 
structure. In addition to influencing grain misorientation 
angle, thermal energy also significantly affects precipi -
tation behaviour. In particular, during L-PBF of IN738LC, 
high-temperature preheating enhances atomic 
diffusion, which not only promotes elemental segre -
gation of strong carbide-forming elements such as Ti 
and Nb at grain boundaries but also provides sufficient 
thermal energy and time for in-situ precipitation. This 
enables the formation of MC-type carbides through 
solute enrichment and reduced cooling rates, alongside 
the nucleation of a high density of fine γ
′
precipitate [ 182 ].
Figure 26 (b) demonstrates that at a preheating temp -
erature of 200°C, carbides and γ
′
precipitates are scarcely 
observed. In contrast, at 700°C, both phases are clearly 
visible and appear as nanoparticles, as indicated in the 
figure. Additionally, in the IN939 deposit fabricated by 
L-PBF, the hot plate effectively decreases the cooling 
rate of the melt pool, promoting the segregation of 
carbide-forming elements such as Nb, Ti, and Ta into 
the interdendritic region. This segregation promotes 
the growth and increased formation of carbide precipi -
tates [ 181 ]. However, according to Yang et al. [ 173 ], 
such precipitation behaviour can vary significantly 
depending on the preheating strategy during EB-PBF 
of IN738LC. When a multiple preheating process is 
employed—where the build surface is reheated at 
Figure 26. Overview of the effects of the hot-plate-assisted AM process on non-weldable Ni-based superalloys: (a) EBSD maps of grain 
boundaries at temperatures of 200 and 700°C [ 182 ], (b) SEM image of samples preheated at 200°C and 700°C showing the nanoscale 
particles precipitated in the sub-grain boundaries [ 182 ], and (c) crack intensity distributions for various crack sizes at different pre -
heating temperatures [ 183 ].
34 
 J. JANG ET AL.

## Page 36

each stage before and after powder spreading—the 
overall temperature fluctuation is minimised. As a 
result, excessive segregation of carbide-forming 
elements at grain boundaries is suppressed, since 
reduced temperature fluctuation helps prevent local 
overcooling that would otherwise promote solute 
enrichment, leading to a significant reduction in the 
amount and area fraction of MC-type carbides. Thus, 
since the effect of preheating on precipitation behaviour 
can vary significantly depending on the strategy, 
method, and temperature applied, optimising the 
process strategy is essential to achieve desirable micro -
structures and mechanical properties.
As previously discussed, thermal energy from the hot 
plate plays a critical role in modifying both grain mor -
phology and precipitation behaviour, thereby influen -
cing the overall microstructural evolution in non- 
weldable alloys. These microstructural changes, in turn, 
have a direct impact on the formation of thermal 
cracks, which are frequently observed during the addi -
tive manufacturing of non-weldable alloys. Specifically, 
elevated thermal input reduces the fraction of HAGBs, 
leading to lower grain boundary misorientation during 
solidification—a condition favorable for suppressing 
the initiation and propagation of hot cracks [ 182 ]. In 
addition, thermal energy mitigates crack susceptibility 
not only by changing grain structure, but also by reliev -
ing thermal stress, which is one of the primary driving 
forces behind crack formation. Specifically, the hot- 
plate-generated thermal energy effectively forms a 
homogeneous thermal field and decreases the slope of 
the thermal gradient within the deposit. In L-PBF of 
IN738, these homogeneous thermal field and decreased 
thermal gradiment stabilise the solidification front and 
promote multidirectional columnar growth. This in 
turn mitigates thermal stress and consequently 
reduces crack formation [ 63 , 183 ]. Additionally, a similar 
trend is observed in the laser solid forming (LSF) of 
René 104, where crack formation also decreases with 
increasing preheating temperature through the same 
thermal mechanisms. Figure 26 (c) presents a graph 
showing the variation in crack intensity across different 
crack length ranges (<100 μm, 100–200 μm, 200–300 
μm, and >300 μm) as a function of preheating tempera -
ture. The results indicate a consistent decrease in crack 
intensity from 450°C to 750°C, including the 6 h hold 
condition [ 183 ]. Beyond the issue of crack susceptibility, 
the hot plate also influences the mechanical properties 
of non-weldable alloys. In terms of hardness, the 
applied thermal energy promotes grain densification 
and microstructural coarsening, both of which contrib -
ute to a decrease in microhardness [ 183 ]. However, 
regarding the tensile properties, the hot plate promotes 
multiple growth directions for columnar dendrites, thus 
facilitating an isotropic microstructure that allows for 
uniform stress distribution and effectively increases the 
ductility of the deposit [ 182 , 183 ]. In addition to 
affecting the tensile properties, the thermal energy gen -
erated by the hot plate also contributes to grain refine -
ment, thereby increasing grain boundary area. This 
microstructural refinement contributes significantly to 
high-temperature performance by reducing creep 
strain localisation along grain boundaries, which is a 
primary deformation mechanism at elevated tempera -
tures. For example, EB-PBF-fabricated IN738LC with hot 
plate preheating exhibited enhanced creep resistance, 
demonstrating improved structural stability under such 
conditions [ 173 ].
4.2. Induction-coil-assisted AM of Ni-based 
superalloys
4.2.1. Process methodology
An induction coil generates thermal energy through 
electromagnetic induction and transfers this energy to 
the target object. Figure 27 shows the process by 
which the induction coil generates and transfers 
thermal energy, where a medium- or high-frequency 
generator is used to produce a corresponding alternat -
ing current in the induction coil [ 184 , 185 ]. This generates 
an electromagnetic field around the induction coil, 
which in turn forms eddy currents within the substrate. 
These eddy currents flow through the substrate, which 
is typically made of Ni-based superalloys or stainless 
steel [ 43 , 168 , 176 , 181 ], and induce a Joule heating 
effect based on the electrical resistance of the substrate. 
Through this series of processes, the induction coil effec -
tively generates and applies thermal energy to the sub -
strate. Because it delivers rapid, localised heating 
without direct contact, it offers a clear advantage in 
AM, particularly for complex geometries where 
uniform preheating is difficult [ 184 ].
Induction coils are widely used to apply thermal 
energy in the AM of Ni-based superalloys to address 
layer quality issues. Although induction-coil-assisted 
AM (ICAAM) is similar to the HPAAM process described 
in Section 4 . 1 , their effects differ because of some sys -
tematic differences. For example, the hot plate heats a 
large area beneath the substrate or build platform 
from a fixed position, whereas the induction coil is 
either fixed around the substrate [ 34 , 186 ] or moves 
along with the laser module [ 187 , 188 ]. Additionally, 
unlike the hot plate, the induction coil can quickly gen -
erate and control localised thermal energy using a fre -
quency generator [ 189 , 190 ]. Another difference 
between induction coils and hot plates is the variety of 
VIRTUAL AND PHYSICAL PROTOTYPING 
 35

## Page 37

shapes that the induction coil can have. Notably, the 
induction coil can be custom-shaped to match the geo -
metry of the target part, offering a significant advantage 
in the additive manufacturing of complex structures. 
This flexibility allows for effective and localised preheat -
ing even on curved or irregular surfaces, which is critical 
for maintaining thermal consistency and minimising 
defects during fabrication. As shown in Figure 28 (a), 
the induction coil can also be integrated into a DED 
system in a way that conforms to the shape of the 
build platform, further enhancing its applicability to 
real industrial scenarios involving complex geometries. 
In PBF processes, the induction coil can also be built 
around the build plate, as shown in Figure 28 (b), 
offering the advantage of providing uniform thermal 
energy even to deposits with relatively high build 
heights, in contrast with hot plates, which are always 
located beneath the build platform [ 172 ]. Moreover, 
unlike the hot plate, the induction coil does not directly 
contact the substrate, minimising the risk of mechani -
cally deforming or contaminating the substrate 
[ 190 , 191 ]. To maximise the advantages of the induc -
tion-coil-assisted AM process, the temperature of the 
substrate or deposit heated by an induction coil must 
be precisely controlled, which is managed using pyro -
metric sensors or thermocouples [ 34 , 184 ]. As mentioned 
above, the induction coil has the advantage of being sys -
temically independent and free to conform to the 
complex shapes of the substrate or deposit. Conse -
quently, Section 4 . 2 comprehensively analyzes how 
ICAAM specifically affects the grain morphology, micro -
structure, and other factors contributing to deposition 
quality for both weldable and non-weldable Ni-based 
alloys.
4.2.2. Process effects for weldable Ni-based 
superalloys
In the ICAAM process, thermal energy effectively 
improves the mechanical properties of weldable alloys 
and prevents distortion. Table 8 summarises the process 
parameters and effects of ICAAM applied to weldable 
alloys. To understand these effects, the influence of 
Figure 27. Schematic of the basic mechanism by which the induction coil generates thermal energy via eddy currents and Joule 
heating toward a cylindrical substrate (image not to scale).
Figure 28. Schematics of induction-coil-assisted AM: (a) LMD systems with induction heating system [ 34 , 192 ] and (b) the L-PBF 
system with an inductive heating system [ 172 ].
36 
 J. JANG ET AL.

## Page 38

induction-coil-generated thermal energy on the grain 
morphology and precipitation of weldable alloys must 
first be examined, while also considering the impact of 
the eddy currents and Joule heating of the induction 
coil. Specifically, the induction-coil-induced thermal 
energy coarsens grains in the deposit. The grain coarsen -
ing mechanism is strongly related to the electromagnetic 
field formed by the induction coil, which generates eddy 
currents within the deposit and induces Joule heating, as 
depicted in Figure 27 . The thermal effect of the eddy cur -
rents promotes atomic diffusion, and the increased temp -
erature caused by Joule heating reduces the activation 
energy required for recrystallization and grain growth. 
Thus, induction heating triggers the creation of eddy cur -
rents and the effects of Joule heating within the deposit, 
both of which contribute to increasing the grain size 
[ 34 , 185 ]. Moreover, the thermal energy from the induc -
tion coil not only changes the grain size but also signifi -
cantly impacts the grain shape. In particular, the 
induction coil is advantageous for increasing grain size 
and creating directionally solidified columnar grain struc -
tures. For example, in the LMD process using IN718, 
induction heating reduces the cooling rate and stabilises 
the thermal gradient through continuous thermal energy 
input. This thermal energy from the induction coil pro -
motes strong directional solidification, resulting in 
coarse columnar grains with a pronounced [ 001 ] 
texture. Figure 29 (a) demonstrates that oriented and 
coarser columnar grains are more pronounced in the 
induction-heated specimen as revealed by the EBSD 
results—including inverse pole figure (IPF) maps, multiple 
of uniform density (MUD), and grain size distributions— 
compared to the as-deposited and furnace-treated con -
ditions [ 34 ]. Furthermore, maintaining the stable down -
ward heat flow during solidification inhibited the 
nucleation of equiaxed grains ahead of the solidification 
front. This led to effective suppression of the CET.
The induction coil also impacts the precipitation of 
weldable alloys. The thermal energy generated by the 
induction coil delays the formation of the Laves phase 
by mitigating the segregation of Nb. To achieve this, 
the process temperature of the induction coil must be 
maintained above the dissolution temperature of the 
Laves phase, which is 1010°C. Therefore, in the LMD 
process using IN718, maintaining the temperature of 
the deposit at 1100°C with an induction coil provides 
an advantage in reducing the Nb segregation ratio and 
the volume fraction of the Laves phase up to a deposit 
height of 10 mm, as shown in Figure 29 (b), which illus -
trates these values as a function of deposit height. This 
suggests that the induction coil can be used not only 
to apply thermal energy during the process but also to 
perform an in situ heat treatment [ 34 ]. In addition to 
affecting the precipitation of the Laves phase in the 
Inconel series of Ni-based superalloys, induction-coil- 
generated thermal energy can also influence the 
amount of precipitation in non-Inconel series Ni-based 
superalloys [ 192 ]. This effect can be observed in 
materials such as Ni60 (which is added with Cr and B 
to enhance its wear resistance and is used as a coating 
material), where increasing the induction coil tempera -
ture effectively reduces the precipitation of the chro -
mium carbides and chromium borides that increase 
crack susceptibility. This is because the increase in 
thermal energy enhances the diffusion of Fe from the 
substrate to the Ni60 coating. This additional Fe reacts 
with Cr and B to form various compounds, the formation 
of which can effectively suppress the precipitation of 
chromium carbides and chromium borides.
Ultimately, the effects of ICAAM on weldable alloys 
contribute to enhancing the mechanical properties of 
the deposits. Thermal energy generated by the induc -
tion coil suppresses the CET by maintaining a stable 
thermal gradient during solidification. This promotes 
the formation of directionally solidified columnar 
grains with reduced grain boundary area. These grains 
minimize the number of high-angle boundaries, 
thereby suppressing grain boundary sliding—one of 
the primary mechanisms of creep deformation at elev -
ated temperatures. As a result, the deposit exhibits 
improved creep performance under high-temperature 
loading conditions in IN718 [ 34 ]. In addition to enhan -
cing the creep resistance, the induction coil also 
enhances the adhesion strength between the deposit 
Table 8. Summary of the ICAAM on weldable Ni-based superalloys.
Type of weldability Alloy AM process Induction coil process parameter Effects of ICAAM process Ref.
Weldable IN718 LMD
• 
Temperature: 1100°C . Grain coarsening
. Improving creep properties
[ 34 ]
Weldable Ni60 EHLA
• 
Temperature: 200, 300, 400°C . Grain coarsening
. Crack suppression
. Reduced residual stress
. Improving wear resistance
[ 192 ]
Weldable IN625 LC
• 
Temperature: 550°C . Crack suppression
. Grain coarsening
. Increased deposition rate
[ 185 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 37

## Page 39

and the substrate. In fact, during the cold spraying 
process with IN625, atomic diffusion actively occurs at 
the penetration depth level of the eddy currents, result -
ing in strong metallurgical bonding at the interface 
between the deposit and the substrate, thereby 
strengthening their adhesion [ 185 ]. Regarding the Ni60 
coating discussed above, induction-coil-generated 
thermal energy effectively suppresses the formation of 
chromium carbides and chromium borides, preventing 
crack initiation and promoting a uniform microstructure. 
In addition, enhanced Fe diffusion improves melt fluidity 
and facilitates the even distribution of hard phases. 
These effects result in a dense, crack-free coating with 
improved wear resistance [ 192 ].
4.2.3. Process effects for non-weldable Ni-based 
superalloys
In ICAAM, the thermal energy generated by the induc -
tion coil can be utilised to mitigate the high crack sus -
ceptibility of non-weldable alloys, which is primarily 
caused by their high Al and Ti content, and to 
improve their mechanical properties. Table 9 presents 
a summary of the process parameters and correspond -
ing microstructural and mechanical outcomes of ICAAM 
Figure 29. (a) EBSD results for the as-deposited, furnace-treated, and induction-coil-heated specimens at deposit height of 4–6 mm, 
including inverse pole figure (IPF) maps along the build direction, pole figures with MUD values, and grain size distributions [ 34 ]; (b) 
segregation ratio of Nb and the volume fraction of Laves phase along the height of deposits [ 34 ].
38 
 J. JANG ET AL.

## Page 40

applied to non-weldable alloys. These effects are highly 
correlated with the relationship between the additional 
thermal energy and the grain morphology of non-weld -
able alloys [ 193 ]. Specifically, induction-coil-generated 
thermal energy coarsens the grains of non-weldable 
alloys. Indeed, in the LSF process for IN738LC, the 
slower cooling rate induced by the thermal energy 
increased the dendrite spacing, which was similar to 
the effects observed with hot plates [ 194 ]. Beyond 
grain coarsening, the induction coil effectively pro -
motes the formation of a high volume fraction of 
equiaxed grains in the LSF process for IN738LC, owing 
to the low G and R values facilitating the CET 
[ 194 , 195 ]. Furthermore, the thermal energy generated 
by the induction coil can also maintain a stable heat 
flow toward the substrate, promoting directional grain 
growth. In the LMD process of René N5, this consistent 
heat flow facilitates the formation of a single-crystal 
structure and a noticeable increase in LAGBs (θ < 
15°), as shown in Figure 30 (a), which compares the 
EBSD image and grain misorientation fractions of 
samples with and without induction coil [ 186 ]. From a 
microstructural perspective, the thermal energy from 
the induction coil impacts the size and amount of pre -
cipitates in non-weldable alloys. Due to their high Ti 
and Al contents, non-weldable alloys exhibit more pro -
nounced precipitation behaviour under induction 
heating compared to weldable alloys, which typically 
contain lower amounts of these elements. This results 
in noticeable changes in the morphology and distri -
bution of precipitates, with these changes being 
further influenced by the applied preheating tempera -
ture. Jianjun et al. [ 194 ] investigated the effect of 
thermal energy provided by an induction coil on the 
morphology and distribution of precipitates, focusing 
on how varying preheating temperatures influence 
microstructural evolution in IN738LC deposit fabricated 
by laser solid forming. Figure 30 (b) presents SEM 
images showing changes in the morphology and 
distribution of MC-type carbides, while Figure 30 (c) 
illustrates the evolution of γ/γ
′
eutectic regions under 
different preheating conditions. Without induction 
heating, the microstructure exhibited both rod-like 
and blocky MC carbides along with fine, sparse γ/γ
′
eutectic regions due to limited solute segregation and 
restricted growth space. At a preheating temperature 
of 800°C, rod-like carbides disappeared, giving way to 
slightly coarser blocky morphologies, and the eutectic 
regions became noticeably larger. At 900°C, further 
coarsening of blocky carbides and γ-γ
′
eutectic zones 
was observed, corresponding with increased dendrite 
spacing and enhanced segregation of Ti and Al. At 
1050 °C, blocky carbides became dominant, though 
their growth remained limited by rapid cooling, while 
γ-γ
′
eutectic regions showed the most significant coar -
sening, driven by pronounced solute segregation and 
expanded interdendritic regions. Furthermore, the 
evolution of γ
′
phases varies depending on the 
specific alloy and AM process. In the LSF process of 
IN738LC, moderate-temperature preheating enhances 
the diffusion of Ti and Al. This promotes not only γ
′
coarsening, but also an increase in the volume fraction 
of the γ
′
phase [ 194 , 195 ]. In contrast, in the LC process 
of CM247LC, preheating at approximately 1100°C, 
above the γ
′
solvus, provides sufficient thermal 
energy to partially dissolve coarse γ
′
precipitates. 
Upon subsequent rapid cooling, finer secondary γ
′
phases reprecipitate, resulting in a refined precipitation 
structure [ 196 ]. These findings demonstrate that the 
effect of preheating on microstructural evolution 
varies significantly depending on the preheating temp -
erature, alloy composition, and AM process. Therefore, 
careful optimisation of these parameters offers a prom -
ising strategy for tailoring the microstructure to achieve 
desired properties in additively manufactured 
components.
As described above, the induction-coil-induced 
changes in the grain morphology and microstructure 
Table 9. Summary of the ICAAM on non-weldable Ni-based superalloys.
Type of weldability Alloy AM process Induction coil process parameter Effects of ICAAM process Ref.
Non-weldable IN738LC LSF
• 
Temperature: 800, 900, 1050°C . Grain coarsening
. Crack suppression
. Improving YS, UTS, EL
[ 194 ]
Non-weldable IN738LC LSF
• 
Temperature: 1050°C . Grain coarsening
. Crack suppression
. Improving YS, UTS, EL
[ 195 ]
Non-weldable René N5 LMD
• 
Temperature: 900°C
• 
Grain coarsening [ 186 ]
Non-weldable CM247LC LC
• 
Temperature: 400–1100°C . Grain coarsening
. Crack suppression
[ 196 ]
Non-weldable K417G LMD
• 
Temperature: 400–1100°C . Grain coarsening
. Crack suppression
. Improving YS, UTS, EL
[ 197 ]
Non-weldable DZ4125 LSF
• 
Temperature: 500°C
• 
Crack suppression [ 193 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 39

## Page 41

of non-weldable alloys effectively address the issue of 
high crack susceptibility. In detail, induction coil 
heating at 1100°C reduces the cooling rate, which 
results in the formation of secondary and smaller γ’ pre -
cipitates that effectively prevent hot cracking in LC of 
CM247LC [ 196 ]. In addition to this precipitate-mediated 
effect on crack susceptibility, the induction coil can also 
decrease crack susceptibility by reducing the thermal 
residual stress. The high temperature generated by the 
induction coil alleviates the thermal residual stress and 
phase transition stress within the deposit, thus reducing 
crack susceptibility and shortening the measured cracks 
[ 197 ]. Additionally, by decreasing the G and R values, the 
thermal energy effectively reduces the thermal residual 
stress acting on the liquid film at grain boundaries, 
which is a driving force for crack formation 
[ 193 , 194 , 197–199 ]. Beyond crack susceptibility, the 
thermal energy from the induction coil also impacts 
the mechanical properties of non-weldable alloys. 
Regarding microhardness, when a high-temperature 
induction coil at 1050°C is used in LSF of IN738LC, the 
increased particle size of the γ’ phase decreases its 
coherence with the γ matrix, which decreases the 
resistance of the deposit to dislocation motion and con -
sequently decreasing its microhardness [ 194 ]. From the 
perspective of the tensile properties, induction-coil-gen -
erated thermal energy promotes the CET and precipi -
tates coarse, nearly cubic γ’ phases that can inhibit 
dislocation motion. Therefore, the induction coil has 
the advantage of increasing both the UTS and EL [ 195 ].
4.3. Process-heat-source-assisted AM of Ni-based 
superalloys
4.3.1. Process methodology
Beam sources in AM processes not only enable material 
deposition but also function as auxiliary thermal energy 
sources during the manufacturing process. Such beam- 
based, process-heat-source-assisted AM can be broadly 
categorised as laser-assisted or electron-beam-assisted 
approaches, depending on the type of beam used. 
Specifically, in laser-assisted AM, the laser can be used 
to assist the AM process in two main ways: by preheating 
the substrate or by remelting the deposited material. For 
laser preheating, the laser is scanned along the intended 
deposition path of each layer prior to the main AM 
Figure 30. (a) EBSD maps and crystal misorientation fractions of samples fabricated with and without induction heating [ 186 ], (b) SEM 
image showing carbide morphology in deposits without induction coil and with a induction coil at 800°C, 900°C, and 1050°C, and (c) 
SEM image showing γ’ morphology in deposits without induction coil and with hot plate at 800°C, 900°C, and 1050°C [ 194 ].
40 
 J. JANG ET AL.

## Page 42

process, as depicted in Figure 31 (a), which outlines the 
sequential steps of laser preheating prior to and 
during the AM process, including substrate preheating 
(a-1), layer deposition (a-2), and subsequent preheat -
ing (a-3) [ 200 ]. In addition to preheating, the laser 
can be used post-deposition to remelt the surface 
layer, delivering localised thermal energy to the pre -
viously deposited material, as shown in Figure 31 (c). 
In both laser preheating and remelting processes, the 
laser typically operates in a defocused mode with low 
power, enabling stable thermal energy delivery over 
a broad area while preventing premature melting of 
the substrate or powder. Meanwhile, electron-beam- 
assisted AM uses the electron beam to preheat the 
powder in the chamber, as shown in Figure 31 (b). 
This preheating is carried out using a scattered-focus 
beam, in which the electron beam is intentionally defo -
cused to deliver thermal energy uniformly over a wide 
area [ 201 ]. The beam is rapidly scanned across the 
build platform and is applied repeatedly to maintain 
the high-temperature environment within the 
chamber [ 172 ]. Process-heat-source-assisted AM pro -
cesses have various advantages compared to other 
heating methods. By utilizing the inherent heat 
source of the AM process, it eliminates the need for 
additional equipment such as a hot plate, induction 
coil, or temperature control module, thereby overcom -
ing the space constraints. For example, in DED systems 
integrated with a computerised numerical control 
(CNC) machine, where space limitations make it 
difficult to install additional heating equipment, utiliz -
ing the beam source itself enables effective preheating 
as shown in Figure 31 (d) [ 202 ]. Moreover, compared to 
conventional heating methods that require scaling 
with part size, laser and electron beams provide 
localised, non-contact thermal energy precisely along 
the deposition path. This capability substantially 
alleviates geometric limitations and facilitates the 
flexible fabrication of complex or large-scale structures. 
Therefore, process-heat-source-assisted AM holds 
strong potential for real industrial applications, particu -
larly in the manufacturing of intricate and functionally 
demanding components.
4.3.2. Process effects for weldable Ni-based 
superalloys
In PHSAAM process for weldable alloys, thermal 
energy can enhance the mechanical properties or 
Figure 31. Schematics of various types of the process-heat-source-assisted AM: (a) laser synchronous preheating system during the 
laser deposition process including (a-1) substrate preheating, (a-2) normal laser deposition, and (a-3) subsequent preheating [ 200 ]; (b) 
electron beam powder bed fusion system with integrated preheating functionality [ 172 ]; (c) laser-based remelting system for post- 
deposition surface refinement [ 203 ]; (d) the hybrid LMD system wherein a CNC machine is integrated [ 202 ]
VIRTUAL AND PHYSICAL PROTOTYPING 
 41

## Page 43

strengthen the metallurgical bonds at the interface 
between the substrate and the deposit or between 
separate layers of the deposit. Table 10 provides a 
detailed summary of PHSAAM applied to weldable 
alloys. To understand these effects, it is essential to 
know how laser- or electron-beam-generated 
thermal energy affects the grain morphology and 
how these changes ultimately affect the mechanical 
properties. Specifically, laser-generated thermal 
energy for preheating can delay the solidification 
process of the melt pool, ultimately affecting the 
grain size and shape. For instance, in the L-PBF 
process of IN718, preheating up to 1200°C using a 
Gaussian laser beam effectively promotes uniform 
and coarse grain growth [ 204 ]. These effects are 
specifically related to the changes in G and R values 
induced by the thermal energy of the laser beam, as 
preheating helps maintain uniform G values across 
the melt pool. Such uniformity can reduce thermal 
residual stress, which in turn induces randomness in 
the grain morphology, contributing to maintaining a 
uniform grain structure within the deposit. Moreover, 
a low R value provides an environment where atoms 
in the melt pool have sufficient time to join the exist -
ing lattice structure, thus promoting larger grain 
growth [ 204 ]. Similarly, laser-generated thermal 
energy for remelting can also affect grain morphology 
[ 205 ]. Since grain morphology is governed by the 
thermal gradient and cooling rate, variations in scan -
ning speed during the laser remelting process lead to 
differences in thermal conditions, which in turn 
influence grain structure. For example, in the L-PBF 
of IN718, the scanning speed directly impacts the 
orientation of grains in the deposited layer. 
Figure 32 (a) shows the grain boundary misorientation 
distributions in samples processed at scanning 
speeds of 1200 mm/s (left) and 2000 mm/s (right) 
during the laser remelting process. At 1200 mm/s, 
where the energy input is relatively higher, the 
grain structure is more directionally aligned, with 
63.3% of the grain boundaries exhibiting misorienta -
tion angles greater than 15°, and 36.7% between 
2° and 15°. In contrast, at a higher scanning speed 
of 2000 mm/s—corresponding to a lower energy 
input—the fraction of high-angle grain boundaries 
decreases to 71%, while the fraction of low-angle 
boundaries increases to 29%, indicating a more ran -
domised grain structure [ 203 ].
The additional thermal energy generated by the main 
process heat source not only changes the grain mor -
phology but also transforms the microstructure. Specifi -
cally, in the EB-PBF process of IN718, using a defocused 
electron beam for preheating the chamber promotes the 
precipitation of γ
′
and γ
′′
phases. Preheating the chamber 
to 1025°C, near the dissolution temperature of γ
′
and γ
′′
phases, reduces the cooling rate and mitigates the 
thermal gradient during the AM process. This thermal 
stabilisation enhances atomic diffusion and extends the 
residence time within the optimal temperature range 
(700–900°C) for γ
′
and γ
′′
precipitation. This ultimately 
increases the volume fractions of these strengthening 
phases in the deposit [ 211 ]. Meanwhile, the laser-beam- 
assisted AM process has the advantage of enhancing inter -
facial diffusion between the substrate and deposit, forming 
Table 10. Summary of the PHSAAM on weldable Ni-based superalloys.
Type of 
weldability Alloy
AM 
process Purpose
Process-heat-source 
process parameter Effects of PHSAAM process Ref.
Weldable IN625 L-PBF Remelting . Laser power: 95, 110, 120 W
. Laser scanning speed: 900 mm/s
. Porosity suppression
. Improving YS, UTS, EL
. Grain coarsening
[ 206 ]
Weldable IN625 LMD Remelting . Laser power: 1600 W
. Laser scanning speed: 1000 mm/ 
min
. Porosity suppression
. Improving hardness
[ 207 ]
Weldable IN625 LMD Preheating . Laser power: 4000 W
. Laser scanning speed: 5 mm/s
• 
Improving hardness, wear resistance [ 208 ]
Weldable IN625 LMD Preheating . Laser power: 650 W
. Laser scanning speed: 8 mm/s
. Crack suppression
. Improving hardness
[ 209 ]
Weldable IN625 LMD Preheating . Laser power: 650 W
. Laser scanning speed: 8 mm/s
. Crack suppression
. Improving hardness
. Improving structure uniformity
[ 210 ]
Weldable IN625 LMD Preheating . Laser power: 650 W
. Laser scanning speed: 8 mm/s
. Crack suppression
. Improving hardness
[ 200 ]
Weldable IN718 L-PBF Remelting . Laser power: 300 W
. Laser scanning speed: 1000–2000 
mm/s
. Porosity suppression
. Improving hardness, wear resistance, corrosion 
resistance
. Grain coarsening
[ 203 ]
Weldable IN718 EB-PBF Preheating
• 
Current: 14–48 mA . Porosity suppression
. Improving TS, EL
[ 211 ]
42 
 J. JANG ET AL.

## Page 44

stronger metallurgical bonding, as evidenced by the SEM- 
EDS elemental map [ 208 ]. The laser-beam-generated 
thermal energy results in excellent metallurgical bonding 
because laser preheating reduces the reflectivity of the sub -
strate to the infrared laser, enabling the substrate to more 
effectively absorb the laser beam during the subsequent 
LMD process. The effects of laser- or electron-beam- 
assisted AM strongly depend on the interaction principles 
between the laser or electron beam and the materials, 
such as the high reflectivity of metal-based substrates or 
the laser penetration depth.
The changes in the grain morphology and precipi -
tation caused by the thermal energy from main 
process-heat-source-assisted AM impact the mechanical 
properties of the deposits. Specifically, coarser grains 
induced by the laser contribute to reducing the micro -
hardness, as grain coarsening can hinder dislocation 
movement within the lattice [ 204 ]. Regarding the 
tensile properties, using the main electron beam as an 
additional heat source to assist the AM process increases 
both the ductility and tensile strength by forming γ’ and 
γ” phases [ 211 ]. In addition to enhancing mechanical 
properties, process-heat-source-assisted AM can also 
improve the structural integrity of the deposit, primarily 
by reducing porosity and crack formation. Specifically, 
laser-assisted remelting process effectively reduces the 
porosity in the deposit by localised remelting and reso -
lidification during AM process. This additional thermal 
cycle allows trapped gases and residual pores to 
escape from the molten pool, resulting in a denser and 
more homogeneous microstructure [ 206 ]. For exmaple, 
as shown in Figure 32 (b), which shows the distribution 
of local porosity rate in IN625 deposit with conventional 
LMD and combining remelting process, the region 
where the laser remelting process was applied exhibited 
pronounced reducion of porosity [ 207 ]. Furthermore, 
process-heat-source-assisted AM effectively reduces 
crack susceptibility in functionally graded materials 
(FGMs) produced by LMD processes. As shown in 
Figure 32 (c), which shows a side view of the deposit to 
compare the morphology with and without preheating, 
when LMD process is assisted by its own laser heat 
Figure 32. (a) Grain boundary distribution of samples with remelting speed 1200 and 2000 mm/s [ 203 ], (b) local porosity color map of 
deposit according to laser remelting process [ 207 ], (c) direct LMD graded samples for (c-1) type STS316L/IN625 [ 200 ], (c-2) type IN625/ 
Ti6Al4V [ 210 ], (c-3) type STS316L/IN625/Ti6Al4V [ 209 ] without and with synchronous preheating.
VIRTUAL AND PHYSICAL PROTOTYPING 
 43

## Page 45

source, laser synchronous preheating has shown advan -
tages in producing crack-free IN625-based FGMs, includ -
ing STS316L/IN625(c-1), IN625/Ti6Al4V(c-2), and 
STS316L/IN625/Ti6Al4V(c-3) structures [ 200 , 209 , 210 ]. 
The advantage of laser synchronous preheating in creat -
ing crack-free deposits is due to the reduction of high 
thermal residual stress near the substrate when applying 
thermal energy generated by the laser, facilitating crack 
suppression. Additionally, the thermal energy from laser 
synchronous preheating results in a uniform tempera -
ture distribution and can control the cooling rate, effec -
tively producing a finer, more uniform grain structure.
4.3.3. Process effects for non-weldable Ni-based 
superalloys
In process-heat-source-assisted AM, the additional 
thermal energy from the beam source effectively miti -
gates the crack susceptibility of non-weldable alloys. 
Table 11 presents an overview of process parameters 
and effects of PHSAAM on non-weldable alloys. By 
adjusting the thermal environment through beam- 
modulated strategies, G and R can be controlled to 
stabilise the solidification front and suppress crack 
initiation. This contributes to improved defect tolerance 
and structural reliability, which are critical for processing 
non-weldable alloys. Specifically, the application of 
additional thermal energy can mitigate crack formation 
by modifying melt pool dynamics during solidification. 
Sufficient thermal input allows the molten material to 
fill cavities and microcracks within the mushy zone. In 
the L-PBF of IN713LC and CM247LC, maintaining the 
deposit temperature above the γ
′
solvus (up to 1200° 
C) through laser-assisted preheating reduces the 
thermal gradient and cooling rate. This promotes 
liquid feeding into interdendritic regions and 
significantly decreases hot cracking susceptibility [ 212 ]. 
Similarly, in the LMD process of ZGH451, thermal 
energy generated by the process heat source extends 
the mushy zone residence time and preserves the 
liquid fraction. This facilitates gradual backfilling of inter -
dendritic cavities and relieves localised stress concen -
trations that would otherwise trigger crack initiation 
[ 213 ]. Furthermore, the laser remelting process enables 
localised backfilling of residual cracks and pores by par -
tially remelting the deposit. For instance, in the L-PBF of 
CM247LC, this approach effectively heals pre-existing 
defects, substantially reducing crack density and enhan -
cing the structural integrity of the deposit [ 214 ].
In addition to mitigating crack formation, process- 
heat-source-assisted AM can reduce crack susceptibility 
by actively modifying precipitation and segregation 
behaviours during solidification. Thermal energy gener -
ated by the process heat source can suppress the segre -
gation of low-melting-point elements and inhibit the 
formation of brittle eutectic structures along grain 
boundaries. In the L-PBF of IN713LC and CM247LC, 
laser-assisted preheating reduces the cooling rate and 
moderates thermal gradients during solidification. 
These conditions suppress the segregation of solute 
elements such as Ti, Nb, and Hf at grain boundaries, 
minimising the formation of brittle eutectic phases. 
This is particularly important for non-weldable Ni- 
based superalloys, which typically contain high 
amounts of Ti and Al—unlike weldable alloys, which 
generally have lower concentrations of these elements. 
Such alloying elements are known to promote the for -
mation of low-melting-point eutectic constituents, 
increasing the risk of liquation cracking during solidifica -
tion. Similarly, in the DMD of IN738LC, moderated 
thermal conditions stabilise the solidification front and 
Table 11. Summary of the PHSAAM on non-weldable Ni-based superalloys.
Type of 
weldability Alloy
AM 
process Purpose Process-heat-source process parameter Effects of PHSAAM process Ref.
Non-weldable Mar-M247 SLM Remelting . Laser power: 60–90 W
. Laser scanning speed: 600–800 
mm/s
. Crack suppression
. Improving UTS, EL
[ 215 ]
Non-weldable CM247LC, 
IN713LC
L-PBF Preheating . Laser power: 280 W
. Laser scanning speed: 1350 mm/s
• 
Crack suppression [ 212 ]
Non-weldable CM247LC L-PBF Remelting . Laser power: 175–225 W
. Laser scanning speed: 800–1200 
mm/s
. Crack suppression
. Improving UTS, YS, EL
[ 214 ]
Non-weldable IN738 EB-PBF Preheating
• 
Current: 14–45 mA . Crack suppression
. Improving hardness, elastic 
modulus
[ 216 ]
Non-weldable IN738 EB-PBF Preheating
• 
Current: 12–20 mA . Crack suppression
. Grain coarsening
[ 217 ]
Non-weldable IN738LC DMD Preheating . Laser power: 1000 W
. Laser scanning speed: 3000 mm/s
• 
Crack suppression [ 201 ]
Non-weldable ZGH451 LMD Preheating . Laser power: 1700 W
. Laser scanning speed: 1100 mm/s
. Crack suppression
. Grain coarsening
. Improving creep resistance
[ 213 ]
44 
 J. JANG ET AL.

## Page 46

suppress the excessive formation of γ–γ
′
eutectic struc -
tures near grain boundaries. This thermal control 
reduces localised thermal stress concentrations and sub -
stantially decreased hot cracking susceptibility [ 201 ]. 
Laser remelting can also contribute to crack resistance 
by redistributing phases that act as crack initiation 
sites. For instance, in the SLM of Mar-M247, high 
carbon content led to excessive MC carbide formation, 
which aligned continuously along cell and grain bound -
aries [ 215 ]. These carbides pinned dislocations, causing 
dislocation wall formation and promoting localised 
stress concentrations. However, with progressive laser 
remelting, these precipitated carbides were redistribu -
ted more uniformly into both dendrite arms and inter -
dendritic regions. This microstructural homogenisation 
alleviated local stress accumulation and significantly 
reduced the crack susceptibility of the as-built deposit.
Beyond crack mitigation, process-heat-source- 
assisted AM processes affect the grain morphology of 
non-weldable alloys, further improving their mechanical 
performance. For example, in EB-PBF of IN738, the high- 
temperature environment maintained by electron beam 
preheating suppresses steep thermal gradients and pro -
motes random grain growth. As a result, equiaxed grains 
formed uniformly throughout the deposit [ 216 ]. With 
more sophisticated control of thermal gradients and 
solidification rates, directional grain structures can also 
be achieved. In addition, in the EB-PBF processing of 
IN738, multiple preheating steps facilitated the for -
mation of single-crystal structures [ 217 ]. The absence 
of grain boundaries in the single-crystal structure effec -
tively suppresses creep-related deformation mechan -
isms such as intergranular diffusion, thereby leading to 
significant improvements in high-temperature mechan -
ical properties.
5. Mechanical- and thermal-energy-assisted 
AM of Ni-based superalloys
As discussed in Sections 3 and 4 , mechanical- and thermal- 
energy-based methods to the AM of Ni-based superalloys 
can both be applied to reduce defects in weldable and 
non-weldable alloys, thereby enhancing the mechanical 
properties of the deposited material. Building upon 
these efforts, researchers have simultaneously utilised 
mechanical and thermal energy. Thus, Section 5 presents 
methods for enhancing the quality of Ni-based superalloy 
deposits by combining mechanical and thermal energy. 
These mechanical- and thermal-energy-assisted AM pro -
cesses include hot isostatic pressing (HIP), which applies 
mechanical energy through high-pressure gas and 
thermal energy through a chamber heater, and hot 
rolling, which involves applying thermal energy through 
preheating followed by mechanical deformation using 
rollers. This section provides an overview of the general 
effects of each method, describes their systems, and exam -
ines their impact on the AM of both weldable and non- 
weldable Ni-based superalloys.
5.1. HIP-assisted AM of Ni-based superalloys
5.1.1. Process methodology
HIP is a representative post-treatment method based on 
mechanical and thermal energy that can be applied to 
AM processes. HIP is primarily used as a post-processing 
technique following AM, utilizing thermal energy from 
high-temperature environments and mechanical 
energy from high-pressure isostatic conditions to 
enhance the quality of the deposited material [ 218 ]. As 
illustrated in Figure 33 , the HIP system consists of com -
ponents such as a pressure chamber, heater, gas inlet, 
and cooling jacket. Specifically, the material to be pro -
cessed is placed inside a pressure chamber designed 
to withstand high temperatures and pressures. The 
chamber is filled with high-pressure gas through the 
gas pressure inlet, creating a uniform pressure environ -
ment inside. At this stage, argon gas, which exhibits 
superior high-temperature stability and minimal chemi -
cal reactivity, is primarily used. The heater raises the 
internal temperature of the chamber, thus initiating 
the HIP process, whereas the cooling jacket facilitates 
the cooling process once the procedure is completed. 
The HIP process, which establishes a high-temperature, 
high-pressure environment through these sequential 
processes, affects the deposited material in several 
ways, as described below. The high-temperature 
environment of HIP supplies thermal energy, which 
enhances atomic diffusion within the deposit. In detail, 
thermal energy allows atoms in the deposit to migrate 
Figure 33. Schematic diagram of a hot isostatic pressing system, 
which applies heat and gas pressure simultaneously to the 
workpiece.
VIRTUAL AND PHYSICAL PROTOTYPING 
 45

## Page 47

more rapidly within the crystal lattice and along the 
grain boundaries, thereby facilitating atomic diffusion. 
This increased atomic movement promotes the diffu -
sional flow of vacancies, which in turn aids in healing 
voids, such as porosity, within the deposit [ 218 , 219 ]. In 
addition, atomic diffusion can induce recrystallization, 
where new nuclei are formed and grow [ 220 ], and it 
can facilitate the homogenisation effect [ 221 ], which 
alleviates the segregation of alloying elements that 
occurs during the AM process. Along with the effects 
of thermal-energy-driven atomic diffusion, the isostatic 
high-pressure environment of HIP supplies mechanical 
energy to the deposit, thereby promoting plastic defor -
mation. Specifically, in the presence of internal defects, 
such as porosity and LOF, the high-pressure environ -
ment induces a stress concentration, which stimulates 
the initiation and movement of dislocations near the 
defect sites. The movement of these dislocations indi -
cates the occurrence of plastic deformation, which can 
gradually reduce or eliminate internal defects 
[ 222 , 223 ]. Combining the effects of atomic diffusion 
and plastic deformation, the HIP process can be effec -
tively applied to the AM of Ni-based superalloys. Accord -
ingly, Sections 5.1.2 and 5.1.3 review studies that have 
analyzed the impact of HIP on weldable and non-weld -
able alloys.
5.1.2. Process effects for weldable Ni-based 
superalloys
As briefly introduced above, the HIP process facilitates 
atomic diffusion and plastic deformation within the 
deposit, which effectively reduces the internal defects 
that occur during the AM process of weldable Ni- 
based superalloys.
Table 12 summarises the effects of the HIP process on 
various weldable Ni-based superalloys, with respect to 
different material and AM processes. Among the internal 
defects that occur during AM, porosity forms because of 
the rapid cooling, which traps gas within the melt pool 
and hinders its escape, resulting in void formation. 
When HIP is applied to a deposit containing such poros -
ity, it induces atomic diffusion and plastic deformation, 
which can significantly reduce the pore size or even 
remove pores, as illustrated in Figure 34 (a) [ 219 ]. In 
addition, the HIP process significantly mitigates the 
LOF, a defect that occurs when the powder or wire feed -
stock fails to fully melt, resulting in incomplete bonding 
between particles. This effect is particularly pronounced 
in EB-PBF processes, where the layer thickness is greater 
and interlayer bonding is weaker than those in L-PBF 
processes [ 224 ]. As shown in Figure 34 (b), which 
shows the IN718 material processed by each of these 
processes, LOF defects are evident in both EB-PBF and 
L-PBF. However, bar graph in Figure 34 (b) shows that 
the volume fraction of LOF is significantly reduced in 
the EB-PBF process, demonstrating its superior effective -
ness in mitigating LOF compared to the L-PBF process. 
The extent to which HIP can reduce internal defects, 
such as porosity and LOF, is highly dependent on its 
process parameters, such as temperature and pressure. 
According to Tillmann et al. [ 225 ], when the HIP 
process temperature for IN718 deposits fabricated by 
L-PBF is below 900°C, the reduction of porosity within 
the deposit is primarily driven by the high-pressure 
environment rather than the high temperature. In this 
case, the extent of atomic diffusion is limited, resulting 
in less effective porosity elimination. Conversely, as 
shown in Figure 34 (c), when the HIP process tempera -
ture is above 900°C, the fraction of porosity decreases 
significantly across all pressure conditions. This is 
because the Ni-based superalloy in the solid state 
becomes more flexible, facilitating plastic deformation 
and enhancing atomic diffusion, thereby maximising 
the porosity reduction effect within the deposit. 
However, if the HIP process temperature exceeds 
1300°C, recrystallization occurs within the deposit, 
which can weaken the extent of plastic deformation. 
HIP can effectively reduce internal defects regardless of 
the initial defect density of the as-built deposit. For 
instance, in the L-PBF process, LOF increasingly occurs 
as the volumetric energy density decreases; however, 
the HIP process has been reported to reduce the internal 
defect density to 0.01% across all volumetric energy 
density conditions [ 226 ]. Nonetheless, according to 
Poulin et al. [ 227 ], HIP could not eliminate large clusters 
of pores near the deposit surface. As illustrated in Figure 
34 (d), most pores are eliminated after the HIP process, 
but some remain, particularly those extending to the 
surface. This limitation was due to high-pressure argon 
gas infiltrating the surface-adjacent pores during the 
HIP process, which hindered the effectiveness of HIP in 
these regions.
In addition to reducing internal defects, such as por -
osity and LOF, the high-temperature environment of 
the HIP process facilitates the microstructural evolution 
of the deposit. During the AM of weldable alloys, a 
high thermal gradient typically results in the formation 
of a columnar grain structure, which exhibits a strong 
texture and anisotropy. When the HIP process is 
applied to such deposits, atomic diffusion induced by 
the high-temperature environment promotes recrystalli -
zation, thus inducing the CET and improving isotropy 
[ 220 , 221 , 243 ]. For instance, Figure 35 (a-1, a-2) shows 
EBSD inverse pole figure maps obtained from an IN718 
deposit fabricated by the L-PBF process. Figure 35 (a-1) 
presents the microstructure before the HIP process, 
46 
 J. JANG ET AL.

## Page 48

Table 12. Summary of the HIP-assisted AM on weldable Ni-based superalloys.
Type of 
weldability Alloy
AM 
process Additional process HIP process parameter Effects of HIP-assisted AM process Ref.
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1160°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Mitigating mechanical anisotropy
[ 219 ]
Weldable IN718 L-PBF • Aging process • Temperature: 1120°C 
• Holding time: 1.5 / 4 / 16 
h 
• Pressure: Not disclosed
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Mitigating mechanical anisotropy, residual 
stress
[ 221 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1185°C 
• Holding time: 3 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving EL, ductility
[ 223 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1150°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure
[ 225 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1160°C 
• Holding time: 3 h 
• Pressure: 102 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Mitigating mechanical anisotropy
[ 226 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1163°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving ductility 
• Mitigating mechanical anisotropy
[ 228 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1150°C 
• Holding time: 4 h 
• Pressure: 150 MPa
• Homogenisation within microstructure 
• Improving ductility
[ 229 ]
Weldable IN718 L-PBF • Stress relief 
• Homogenisation 
• Solution treatment 
• Aging process
• Temperature: 1163°C 
• Holding time: 3 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Improving EL
[ 230 ]
Weldable IN718 L-PBF • Solution treatment 
• Aging process
• Temperature: 1163°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving EL
[ 231 ]
Weldable IN718 L-PBF • Stress relief 
• Solution treatment 
• Aging process
• Temperature: 1163°C 
• Holding time: 3 h 
• Pressure: 105 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving ductility, work hardening rate
[ 232 ]
Weldable IN718 L-PBF • Stress relief 
• Solution treatment
• Temperature: 1163°C 
• Holding time: 4 h 
• Pressure: 101.7 MPa
• Reduction of internal defect 
• Recrystallization of microstructure
[ 233 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1185°C 
• Holding time: 3 h 
• Pressure: 170 MPa
• Reduction of internal defect 
• Homogenisation within microstructure
[ 218 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1185°C 
• Holding time: 3 h 
• Pressure: 170 MPa
• Reduction of internal defect 
• Homogenisation within microstructure
[ 222 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1185°C 
• Holding time: 3 h 
• Pressure: 170 MPa
• Reduction of internal defect 
• Homogenisation within microstructure
[ 234 ]
Weldable IN718 EB-PBF Not disclosed • Temperature: 1200°C 
• Holding time: 2 / 4 h 
• Pressure: 100 MPa
• Homogenisation within microstructure 
• Mitigating mechanical anisotropy
[ 235 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Improving ductility, fatigue resistance 
• Mitigating mechanical anisotropy
[ 236 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1185°C 
• Holding time: 4 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving oxidation resistance
[ 237 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving ductility
[ 238 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 120 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving EL, fatigue resistance
[ 239 ]
Weldable IN718 EB-PBF • Aging process • Temperature: 1120°C 
• Holding time: 1 h 
• Pressure: 200 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving fatigue resistance
[ 240 ]
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Homogenisation within microstructure
[ 241 ]
(Continued ) 
VIRTUAL AND PHYSICAL PROTOTYPING 
 47

## Page 49

where columnar grains typical of the as-built state are 
observed. In contrast, Figure 35 (a-2) shows the micro -
structure after the HIP process, where atomic diffusion 
induced by the high-temperature environment pro -
motes recrystallization, resulting in the formation of an 
equiaxed grain structure. Furthermore, recrystallization 
facilitates the formation of annealing twins, where the 
atoms within the deposit arrange themselves symmetri -
cally. These annealing twins contribute to stabilising the 
microstructure because they possess lower free energy 
than conventional grain boundaries [ 220 ]. Beyond the 
microstructural recrystallization, HIP also influences the 
distribution of secondary phases commonly observed 
in weldable alloys. The high-temperature environment 
of the HIP process dissolves detrimental phases, such 
as the Laves phase, enabling the re-distribution of Nb 
previously segregated in brittle intermetallics, which in 
turn promotes the formation of strengthening phase 
such as γ
′′
[ 223 ]. Furthermore, the high-temperature 
environment of the HIP process also promotes the 
uniform distribution and stabilisation of carbides, such 
as MC-type carbides, within the microstructure. In par -
ticular, the uniformly distributed carbides within the 
grains and along the grain boundaries provide Zener 
pinning, effectively suppressing abnormal grain growth 
[ 234 ].
These microstructural evolution effects induced by 
the HIP process vary significantly depending on its pro -
cessing parameters. According to Jiang et al. [ 221 ], the 
HIP holding time plays a critical role in the microstruc -
ture of IN718 deposits fabricated by L-PBF. Specifically, 
When the holding time was limited to 1.5 h at 1120°C, 
recrystallization scarcely occurred, resulting in a predo -
minantly columnar grain structure, while the brittle 
Laves phase was effectively dissolved into the matrix. 
At 4 h, partial recrystallization occurred, leading to the 
formation of equiaxed grains and the initial appearance 
of annealing twins, and MC-type carbides began to form 
along grain boundaries. With a prolonged holding time 
of 16 h, full recrystallization occurred, producing a 
uniform equiaxed grain structure with well-developed 
annealing twins and coarsened MC carbides. Further -
more, the effects of HIP are not solely governed by 
process parameters, but are also significantly influenced 
by the initial microstructural condition of the deposit. To 
better understand the relationship between the initial 
microstructural condition of deposit and the effects of 
HIP process, Nandwana et al. [ 235 ] applied HIP to 
IN718 deposits fabricated by EB-PBF at different 
process temperatures. They reported that grain growth 
occurred in deposits processed at lower temperatures, 
whereas no such growth was observed in those pro -
duced at higher temperatures. This phenomenon is 
associated with the precipitation behaviour of the δ 
phase and carbides, which varies depending on the 
EB-PBF process temperature. As shown in Figure 35 (b- 
1), in samples deposited at lower temperatures, the δ 
phase and carbides are evenly precipitated within both 
the intragranular regions and grain boundaries. In con -
trast, in high-temperature-deposited samples, the δ 
phase and carbides are predominantly concentrated 
along the grain boundaries, as depicted in Figure 35 (b- 
2). When the HIP process was applied to these deposits, 
the δ phase dissolved in both cases; however, the 
Table 12. Continued.
Type of 
weldability Alloy
AM 
process Additional process HIP process parameter Effects of HIP-assisted AM process Ref.
Weldable IN718 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving EL
[ 242 ]
Weldable IN718 L-PBF EB- 
PBF
• Solution treatment 
• Aging process
• Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 120 MPa
• Reduction of internal defect 
• Improving ductility, fatigue resistance
[ 224 ]
Weldable IN625 L-PBF • Stress relief • Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Reducing fatigue crack growth rate 
• Improving ductility
[ 227 ]
Weldable IN625 L-PBF • Stress relief • Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Improving ductility, fatigue resistance 
• Mitigating mechanical anisotropy
[ 243 ]
Weldable IN625 L-PBF • Stress relief 
• Recrystallization 
annealing 
• Solution treatment
• Temperature: 1120 – 
1240°C 
• Holding time: 3–4 h 
• Pressure: 100–165 MPa
• Recrystallization of microstructure 
• Improving ductility 
• Mitigating mechanical anisotropy
[ 244 ]
Weldable IN625 EB-PBF Not disclosed • Temperature: 1120°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving ductility
[ 220 ]
48 
 J. JANG ET AL.

## Page 50

carbides, which inhibit grain growth, remained 
unaffected. Consequently, after HIP process, grain 
growth occurred in the low-temperature deposit, 
where the grain boundaries had a relatively lower 
carbide content, as illustrated in Figure 35 (b-3). Similarly, 
another study demonstrated that the initial microstruc -
ture of the as-built deposit influenced the effectiveness 
of HIP. Specifically, in as-built IN718 deposits with a 
columnar grain structure, the strong texture of the 
columnar grains resulted in a higher distribution of car -
bides along the grain boundaries, effectively suppres -
sing the grain growth after the HIP process. However, 
in deposits with a fully equiaxed grain structure, the 
weaker texture led to a lower carbide distribution 
Figure 34. Overview of the effects of HIP on internal defects in a weldable Ni-based superalloy: (a) optical microscopy images in cross 
section of HIP and non-HIP deposits [ 219 ]; (b) optical microscopy images of EB-PBF and L-PBF deposit and bar graph which shows 
defect volume fraction in each process [ 224 ]; (c) porosity-temperature graph measured after HIP processing at different pressures 
(50, 100 and 150 MPa) [ 225 ]; and (d) Computed Tomography-reconstructed image showing defect distribution according to HIP 
process [ 227 ].
Figure 35. Overview of the HIP effect on the microstructure of a weldable Ni-based superalloy: (a-1, a-2) EBSD images of HIPed and 
non-HIPed deposit [ 221 ], (b-1, b-2) SEM images of IN718 deposit processed at low and high temperatures, showing the formation and 
distribution of secondary phases within intragranular regions and along grain boundaries and (b-3) EBSD images of as-built and HIPed 
samples deposited at low (left) and high (right) temperatures [ 235 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 49

## Page 51

along the grain boundaries, which reduced the Zener 
pinning effect after HIP, ultimately resulting in abnormal 
grain growth [ 236 ]. Through these studies by Jiang et al. 
and Nandwana et al., it is evident that both the HIP pro -
cessing parameters and the initial microstructural con -
dition of the deposit play a critical role in determining 
microstructural evolution. Therefore, by precisely con -
trolling these factors the microstructure and perform -
ance of deposit can be effectively optimised.
In summary, the HIP process, based on atomic 
diffusion and plastic deformation, effectively reduces 
residual internal defects within the deposit while pro -
moting microstructural evolution. These combined 
effects enhance the mechanical properties of the weld -
able alloy deposits. By mitigating the internal defects 
that could act as stress concentration factors, the HIP 
process reduces the fatigue crack growth rate [ 227 ] 
and improves the EL of the deposit, compared to the 
gray dotted line and the orange dotted line in Figure 
36 (a-2) [ 223 ]. Furthermore, the dissolution of brittle det -
rimental phases and the transition of the microstructure 
into an equiaxed grain structure enhance the ductility of 
the deposit [ 220 , 243 ]. This transition also helps mitigate 
the mechanical anisotropy associated with the build 
direction in AM [ 226 , 235 , 243 ]. Figure 36 (b-1) illustrates 
the fatigue crack propagation rate without the HIP 
process, where significant mechanical anisotropy is 
observed due to the differences in properties along 
the build direction in L-PBF process. In contrast, 
Figure 36 (b-2) shows the effect of the HIP process, 
which leads to isotropic mechanical properties that are 
independent of the build direction. In addition, HIP pro -
motes the homogeneous distribution of Cr within the 
microstructure, which facilitates the formation of a 
Cr₂O₃-based oxide layer, thereby improving the oxi -
dation resistance of the IN718 deposit [ 237 ]. Overall, 
the HIP process positively affects the mechanical proper -
ties of the deposit, including increased ductility and 
reduced fatigue crack propagation rate and anisotropy.
While HIP is generally effective in enhancing these 
mechanical properties, some studies have reported 
that HIP may lead to a reduction in rigidity-based mech -
anical properties, such as strength and hardness, when 
solely applied without subsequent post-processing 
[ 223 , 228–230 ]. For example, as shown in Figure 36 (a- 
1), the HIP-processed IN718 deposit produced by the 
L-PBF process, which is represented as the gray dotted 
line, exhibits the lowest hardness compared to the 
other conditions. Even more notably, Kreitcberg et al. 
[ 244 ] reported that the yield and tensile strengths of 
HIP-treated IN625 deposits fabricated by L-PBF were sig -
nificantly lower at high temperatures compared to the 
as-built condition. This reduction in rigidity-based mech -
anical properties occurs because the HIP process oper -
ates at high temperatures, potentially leading to grain 
coarsening, which in turn decreases the number of 
grain boundaries that act as barriers to dislocation 
motion. However, enhancing these properties is 
Figure 36. (a-1, a-2) Hardness profile and stress-strain curve of IN718 deposit, showing the effect of HIP and heat treatment on mech -
anical properties [ 223 ]; (b-1, b-2) fatigue crack propagation diagrams for non-HIPed and HIPed specimens built with orientations 0°, 
45°, and 90° [ 243 ]; (c) heat treatment regimes with and without the HIP process [ 219 ]; and (d) geometry, topology, and relative density 
of the additively manufactured lattice structures [ 233 ].
50 
 J. JANG ET AL.

## Page 52

essential for excellent mechanical properties of Ni-based 
superalloy, particularly at high temperatures, and it can 
be achieved through additional heat treatments such 
as solution treatment and aging processes. During sol -
ution treatment, the δ phase dissolves, allowing 
elements such as Nb, which is essential for the precipi -
tation of strengthening phases like the γ
′ ′
phase, to be 
uniformly distributed within the microstructure. Sub -
sequently, a two-step aging process facilitates the 
uniform precipitation of the strengthening phases γ
′
and γ
′ ′
, which are critical for Ni-based superalloys 
strengthened through precipitation hardening mechan -
isms. These strengthening precipitates primarily form at 
the grain boundaries, where they enhance precipitation 
hardening, effectively restricting dislocation movement 
and crack propagation. As a result, the strength and 
hardness of the deposit are significantly improved 
[ 219 , 231 , 238 ]. When heat treatments are applied in con -
junction with HIP, the precipitation hardening effect is 
further enhanced. A typical process combining HIP and 
heat treatment is illustrated in Figure 36 (c). According 
to Schröder et al. [ 232 ], IN718 deposits that underwent 
heat treatment in conjunction with the HIP process 
exhibited homogeneously precipitated γ
′ ′
phase, 
whereas deposits subjected only to heat treatment 
resulted in inhomogeneous γ
′ ′
precipitates, thereby 
reducing the effectiveness of precipitation hardening. 
This difference is attributed to the homogenisation 
effect of the HIP process, which ensures the uniform dis -
tribution of Nb, a key element required for γ
′ ′
phase pre -
cipitation, within the grain structure, thereby enabling 
the formation of a more uniform γ
′ ′
phase. Additionally, 
HIP-induced reduction in internal defects further 
enhances the precipitation hardening effect. Internal 
defects, which can contribute to the segregation of 
elements such as Al and Ti, are effectively reduced by 
HIP processing, leading to a more uniform distribution 
of the γ
′ ′
phase [ 239 ]. Leveraging these advantages of 
HIP can significantly improve the process efficiency of 
the heat treatment. The reduction of internal defects 
and the homogenisation effect facilitated by HIP create 
favorable conditions for the uniform precipitation of 
the γ
′ ′
phase. As a result, the solution treatment can 
be omitted [ 240 ], and the traditional two-step aging 
process, which typically requires 16 h, can be substan -
tially shortened to 5 h [ 241 , 242 ]. In addition to enhan -
cing process efficiency, recent studies have also 
highlighted the feasibility of the HIP process with 
other heat treatments for the practical application of 
complex structures in real industrial environments. 
Hazeli et al. [ 233 ] investigated the influence of HIP on 
various lattice topologies that are widely used in indus -
trial components such as heat exchangers and aircraft 
exhaust systems. As illustrated in Figure 36 (d), they fab -
ricated lattice structures of IN718 using the L-PBF 
process with four representative topologies—Octet 
Truss (OT), Rhombic Dodecahedron (RD), Diamond (D), 
and Dode-Medium (DM)—and subsequently applied 
HIP and additional heat treatments. After post-proces -
sing, including HIP, the Diamond topology showed a 
reduction in mechanical strength after HIP treatment, 
whereas the OT, RD, and DM topologies exhibited 
improved or maintained strength compared to the as- 
built condition. This degradation was attributed to the 
unique geometric feature of the Diamond structure, 
which has a high density of strut intersections (nodes). 
During HIP, intense recrystallization at these nodes led 
to localised softening and stress concentration, ulti -
mately diminishing structural integrity. These results 
highlight the need for geometry-specific HIP strategies 
to ensure reliable performance in industrial applications.
5.1.3. Process effects for non-weldable Ni-based 
superalloy
As discussed in Section 5 . 1 . 2 , the HIP process facilitates 
atomic diffusion and plastic deformation within the 
deposit, effectively reducing internal defects such as 
porosity and LOF. Non-weldable Ni-based superalloys 
can benefit from these same effects of HIP. Table 13
summarises the effect of the HIP process on non-weld -
able Ni-based superalloys across different materials 
and AM process types. Moreover, as shown in Figure 
37 (a), HIP is effective not only in reducing defects like 
porosity but also in mitigating cracks, such as thermal 
cracks, which often occur in non-weldable alloys 
because of their high Al and Ti contents and the rapid 
cooling characteristic of AM processes. By alleviating 
these thermal cracks, HIP enables the stable fabrication 
and application of non-weldable alloys, which would 
otherwise suffer from severe cracking issues during addi -
tive manufacturing. Specifically, the high-temperature 
environment of HIP enhances atomic diffusion, allowing 
atoms on the surfaces of thermal cracks to diffuse and 
interact with one another, ultimately leading to 
diffusion bonding within the cracks [ 245 ]. Additionally, 
the high-pressure environment of HIP promotes plastic 
deformation, which is particularly significant in thermal 
cracks owing to the high levels of stress concentration 
in their vicinity. The increased localised plastic defor -
mation facilitates the bonding of crack surfaces, effec -
tively narrowing the crack opening, which heals 
thermal cracks [ 246 , 247 ]. As shown in Figure 37 (b), 
which illustrates the crack density in CM247LC deposits 
processed by L-PBF with different process parameter 
sets, it can be observed that the crack density is signifi -
cantly reduced in all cases where the HIP process was 
VIRTUAL AND PHYSICAL PROTOTYPING 
 51

## Page 53

applied. In addition, secondary cracks, which can 
develop when high tensile residual stress acts on 
internal defects, can also be healed by HIP-induced 
diffusion bonding and plastic deformation [ 247 ]. This 
demonstrates that the HIP process is highly effective in 
reducing thermal cracks in non-weldable alloys, with 
its effectiveness varying depending on the type of 
thermal crack. According to Koo et al. [ 248 ], HIP is 
more effective in mitigating liquation cracks than soli -
dification cracks in CM247LC deposits fabricated by L- 
PBF. This is because solidification cracks typically form 
in the grain core, where the solute concentration is 
low and the crack path is irregular, which hinder 
atomic diffusion and plastic deformation, respectively. 
In contrast, liquation cracks are located along the grain 
boundaries, where the solute concentration is higher 
and the crack path is more linear, enabling the HIP 
process to more effectively promote atomic diffusion 
and plastic deformation. Furthermore, the efficacy of 
HIP is influenced not only by the type of thermal crack 
but also by its width. Research has shown that thermal 
cracks with widths of 6 μm or less can be effectively 
eliminated by the HIP process in IN738LC deposit fabri -
cated by L-PBF, whereas those wider than 6 μm tend 
to persist even after HIP treatment, as illustrated in 
Figure 37 (c) [ 249 ]. This is because the diffusion 
bonding effect between the crack surfaces becomes 
insufficient for larger cracks. It has been suggested 
that increasing the processing time during the HIP 
cycle can address this issue. Nevertheless, HIP is ineffec -
tive in healing surface-connected thermal cracks 
because these cracks extend to the external surface of 
the deposit. Because they are open to the external 
environment, the compressive forces generated by the 
pressure inside the HIP chamber are limited in their 
ability to fully close and heal such cracks [ 245 , 250 ].
In addition to healing thermal cracks in non-weldable 
alloys, the HIP process also facilitates microstructural 
evolution within the deposit. During HIP, recrystalliza -
tion causes the CET, eliminating the strong-textured 
columnar grain structure typically observed in as-depos -
ited conditions. The CET stabilises the microstructure 
Table 13. Summary of the HIP-assisted AM on non-weldable Ni-based superalloys.
Type of weldability Alloy
AM 
process Additional process HIP process parameter Effects of HIP-assisted AM process Ref.
Non-weldable IN738LC L-PBF Not disclosed • Temperature: 1180°C 
• Holding time: 3 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving micro-hardness
[ 249 ]
Non-weldable IN738LC L-PBF • Solution treatment 
• Aging process
Not disclosed • Reduction of internal defect 
• Homogenisation within microstructure 
• Improving creep resistance, ductility
[ 250 ]
Non-weldable IN738LC L-PBF • Solution treatment 
• Aging process
• Temperature: 1175°C 
• Holding time: 4 h 
• Pressure: 100 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving EL, tensile strength
[ 251 ]
Non-weldable IN738LC EB-PBF • Solution treatment 
• Aging process
• Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 120 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Improving EL
[ 252 ]
Non-weldable IN738 L-PBF • Solution treatment 
• Aging process
• Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Improving ductility, strength
[ 253 ]
Non-weldable IN738 L-PBF • Solution treatment • Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 140 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Mitigating dislocation density, residual stress
[ 254 ]
Non-weldable CM247LC L-PBF Not disclosed • Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving EL, UTS, ductility
[ 247 ]
Non-weldable CM247LC L-PBF • Aging process • Temperature: 1200°C 
• Holding time: 4 h 
• Pressure: 98 MPa
• Reduction of internal defect [ 248 ]
Non-weldable CMSX-4 L-PBF • Aging process • Temperature: 1300°C 
• Holding time: 15 min 
• Pressure: 100 Mpa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving fatigue resistance
[ 255 ]
Non-weldable CMSX-4 EB-PBF Not disclosed • Temperature: 1280–1315°C 
• Holding time: 15–180 min 
• Pressure: 100–150 MPa
• Reduction of internal defect 
• Recrystallization of microstructure 
• Homogenisation within microstructure 
• Improving fatigue resistance
[ 256 ]
Non-weldable DZ1215 EB-PBF • Solution treatment 
• Aging process
• Temperature: 1230°C 
• Holding time: 4 h 
• Pressure: 150 MPa
• Reduction of internal defect 
• Homogenisation within microstructure
[ 246 ]
Non-weldable René 104 LMD Not disclosed • Temperature: 1107°C 
• Holding time: 2 h 
• Pressure: 103 MPa
• Reduction of internal defect 
• Homogenisation within microstructure 
• Improving creep resistance
[ 245 ]
52 
 J. JANG ET AL.

## Page 54

and reduces the dislocation density. Figure 38 (a) illus -
trates the dislocation density of IN738 deposits fabri -
cated by L-PBF process, where the samples underwent 
different treatments: as-built, heat treatment, and HIP 
processing. It is evident that the HIP process significantly 
reduces the dislocation density compared to both the 
as-built and heat-treated samples. This reduction in dis -
location density facilitates the formation of uniform 
carbide precipitation at the grain boundaries, which con -
sequently reduces the crack susceptibility of non-weld -
able alloys [ 252 , 253 ]. Moreover, the high-temperature 
environment of HIP not only promotes recrystallization 
but also induces a homogenisation effect within the 
microstructure. Figure 38 (b) illustrates the EDS elemen -
tal maps of CMSX-4 deposits fabricated by EB-PBF, 
used to evaluate elemental segregation before and 
after HIP process. Due to the high thermal gradient 
during additive manufacturing, elements such as Ti 
tend to accumulate in the interdendritic regions, as 
shown in Figure 38 (b-1, b-3), leading to significant seg -
regation and increasing the risk of liquation cracks. 
However, as illustrated in Figure 38 (b-2, b-4), HIP proces -
sing facilitates homogenisation effect, which effectively 
alleviates elemental segregation, promotes a more 
uniform distribution of elements, and consequently 
reduces the susceptibility to liquation cracking 
[ 251 , 256 ].
Furthermore, the homogenisation effect induced by 
the HIP process also affects the secondary phases in 
non-weldable alloys. As mentioned in Section 2 , non- 
weldable alloys, owing to their high Al and Ti contents, 
form strengthening γ
′
phases during the AM of these 
alloys. However, the characteristically rapid cooling of 
AM processes results in irregular γ
′
precipitates. 
When HIP is applied, the homogenisation effect 
ensures that these γ
′
precipitates are uniform in size 
and shape, thereby enhancing the precipitation hard -
ening effect [ 250 ]. In addition, carbides such as MC car -
bides, which are often formed with heterogeneous 
distributions during AM, become more uniformly dis -
tributed along the grain boundaries through the HIP 
process, as shown in Figure 38 (c). This uniform distri -
bution helps hinder both crack propagation and dislo -
cation movement, contributing to improved 
mechanical properties [ 252 , 254 ]. The efficacy of HIP 
in facilitating microstructural recrystallization and 
homogenisation is highly dependent on process par -
ameters such as temperature and pressure. According 
to Ruttert et al. [ 256 ], conducting HIP at 1280°C and 
150 MPa for 3 h alleviates segregation in the 
Figure 37. Overview of the effects of HIP on thermal cracks in non-weldable Ni-based superalloy: (a) optical microscopy images 
showing a thermal crack and pores in the as-built and HIPed CM247LC deposit [ 247 ], (b) crack density of the as-built and HIP- 
treated samples with different process parameter set [ 248 ], and (c) optical microscopy images showing thermal cracks before 
(left) and after (right) HIP treatment [ 249 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 53

## Page 55

interdendritic region and dissolves detrimental phases 
in CMSX-4 superalloy fabricated by EB-PBF; however, 
the γ
′
phase tends to overgrow, which may negatively 
impact the mechanical properties. On the other hand, 
when HIP is performed at 1300°C and 100 MPa for a 
shorter duration of 4 min, segregation is effectively 
mitigated, detrimental phases are dissolved, and 
thermal cracks are efficiently healed, while the γ
′
phase is refined and uniformly distributed. However, 
if the HIP process is conducted at a temperature 
exceeding the solvus temperature of the γ
′
phase, 
such as 1315°C, the γ
′
phase completely dissolves, 
which limits the precipitation hardening effect.
The impact of the HIP process on the AM of non-weld -
able Ni-based superalloys can be summarised as follows: 
HIP effectively heals thermal cracks within the deposit 
Figure 39. (a) Engineering stress–strain curves of as-built, HIP, and cast + HT alloys [ 247 ]; (b) microhardness values of as-built and HIP 
specimens with different process parameter [ 249 ]; (c) SEM images of L-PBF deposits (c-1) processed with a solution heat treatment 
and age-hardening only and (c-2) HIPed, solution heat treated, and age-hardened [ 250 ]; and (d) regimes of shortened heat treatments 
[ 255 ].
Figure 38. Overview of the effects of HIP on the microstructure of non-weldable Ni-based superalloy: (a) dislocation densities in the L- 
PBF-built IN738 alloy after HIP and heat treatment [ 253 ], (b) EDS elemental mappings of the as-built (b-1, b-3) and HIPed (b-2, b-4) EB- 
PBF deposit [ 256 ], and (c) schematics of microstructural evolution during the HIP process [ 252 ].
54 
 J. JANG ET AL.

## Page 56

and promotes microstructural evolution, which ulti -
mately reduces crack susceptibility and enhances the 
precipitation hardening effect. These mechanisms can 
significantly improve the mechanical properties of 
non-weldable alloys. In Figure 39 (a), which is the 
stress–strain curve of CM247LC deposits fabricated by 
L-PBF in the as-built, HIP-treated, and cast + heat- 
treated conditions, the HIP-treated sample, which is rep -
resented by red curve, exhibits the highest EL, indicating 
a significant improvement in ductility resulting from the 
HIP process. Moreover, HIP can mitigate elemental seg -
regation and dissolve brittle detrimental phases, enhan -
cing fatigue resistance [ 255 , 256 ]. Additionally, the 
uniform distribution of carbides within the grain bound -
aries helps suppress grain boundary sliding, thereby 
enhancing the creep resistance of the deposit 
[ 245 , 250 ]. Beyond the improvement in general mechan -
ical properties, the refined and evenly distributed γ
′
phase after HIP processing significantly enhances rigid -
ity-based mechanical properties in non-weldable Ni- 
based superalloys, in contrast to the typical degradation 
observed in weldable alloys [ 247 , 249 , 252 , 254 ]. For 
example, Figure 39 (b) shows the micro-hardness of 
IN738LC deposits fabricated by the L-PBF process, with 
each sample divided based on different processing par -
ameters. It is evident that for all samples, the deposits 
processed with HIP exhibit higher micro-hardness com -
pared to the as-built samples, demonstrating the effec -
tiveness of the HIP process in enhancing the rigidity- 
based mechanical properties. In other words, the pre -
cipitation hardening effect of HIP on the γ
′
phase plays 
a crucial role in improving the rigidity-based mechanical 
properties. This effect can be further maximised when 
HIP is combined with heat treatments, such as solution 
treatment and aging processes. According to Rickenba -
cher et al. [ 250 ] and Xu et al. [ 253 ], only heat-treating 
IN738 deposits resulted in a unimodal distribution of 
fine γ
′
precipitates, as illustrated in Figure 39 (c-1). In con -
trast, when HIP was combined with heat treatment, both 
fine and coarse γ
′
precipitates coexisted, forming a 
bimodal distribution ( Figure 39 (c-2)). These fine γ
′
pre -
cipitates improve the tensile strength and wear resist -
ance, while coarse γ
′
precipitates enhance creep 
resistance and ductility. Thus, the bimodal combination 
of fine and coarse γ
′
precipitates further enhances the 
precipitation hardening effect, improving the durability 
and mechanical stability of the deposit. The process 
efficiency of the heat treatment can also be significantly 
improved by shortening the process time, as illustrated 
in Figure 39 (d), by leveraging the strong precipitation 
hardening effect achieved by the HIP process. According 
to Lopez-Galilea et al. [ 255 ], HIP facilitates the reduction 
of elemental segregation and promotes microstructural 
homogenisation, which can reduce the time required 
for solution treatment or even eliminate the need for 
this step entirely. Moreover, the homogenised micro -
structure facilitates the precipitation of sufficient γ
′
phases, allowing for a significantly reduced aging 
process time while still effectively achieving the 
desired precipitation hardening effect.
5.2. Hot-rolling-assisted AM of Ni-based 
superalloys
5.2.1. Process methodology
Hot rolling is a plastic deformation technique in which 
the material is preheated to a high temperature before 
undergoing the rolling process introduced in Section 
3 . 3 , inducing plastic deformation throughout the 
material. HRAAM, which utilises the characteristics of 
hot rolling, simultaneously applies both thermal and 
mechanical energy. As a result, compared with RAAM, 
HRAAM offers advantages in mitigating the microstruc -
tural inhomogeneity and anisotropy that typically 
develop during deposition [ 257 ]. As shown in 
Figure 40 , the HRAAM system is similar to the RAAM 
system but includes an additional flame heating 
process using a torch to preheat the material prior to 
being plastically deformed by the roller [ 257 , 258 ]. Fur -
thermore, HRAAM primarily employs interlayer rolling, 
as it is designed to improve the heterogeneous and ani -
sotropic microstructure throughout the material. Due to 
this, a key characteristic of this process is that the depos -
ited material is rolled only after being preheated to the 
target temperature [ 257 , 258 ]. The lattice energy within 
the material, facilitating lattice slip and grain boundary 
movement, both of which reduce the resistance of the 
material to deformation. Owing to these effects, 
HRAAM enables more uniform and consistent plastic 
deformation than RAAM conducted at room tempera -
ture, and it offers the advantage of achieving a deeper 
plastic deformation zone.
5.2.2. Process effects for weldable Ni-based 
superalloy
The study on the effects of the HRAAM process induced 
by both thermal and mechanical energy on Ni-based 
superalloys is summarised in Table 14 . As explained 
above, HRAAM requires a complex system consisting 
of three key components, so there are limitations in 
controlling and optimising the process, and further 
research is needed. However, based on the two pre -
vious studies, the effects of HRAAM induced by both 
thermal and mechanical energy are slightly different 
from those of RAAM induced only by mechanical 
energy. As shown in Figure 41 (a), hot-rolling deposits 
VIRTUAL AND PHYSICAL PROTOTYPING 
 55

## Page 57

cause greater deformation than cold-rolling them 
[ 257 ]. Consequently, the effects observed in the 
RAAM process discussed in Section 3 . 3 , including den -
sification, formation of compressive residual stress, 
work hardening, and grain refinement through recrys -
tallization, are amplified in HRAAM. For instance, as 
depicted in Figure 41 (b), the hot-rolled deposit exhi -
bits noticeably finer equiaxed grains extending more 
deeply than those in the cold-rolled deposit. Further -
more, even when the same roller load is applied, the 
fragmentation of precipitates, as described in Section 
3 . 3 for the RAAM process, is significantly enhanced 
by HRAAM, as shown in Figure 41 (c) [ 257 ]. This 
implies that adding thermal energy enables deeper 
microstructural changes along the depth of the 
deposit, even when the same level of mechanical 
energy is applied.
The microstructural evolution induced by the HRAAM 
process also affects the mechanical properties of the 
deposit. Similar to RAAM, HRAAM improves the hard -
ness, strength, and EL. However, the most notable 
result of HRAAM is that these mechanical properties 
are uniformly enhanced, regardless of the test direction 
of the material [ 257 , 258 ]. In general, the degree of 
anisotropy of a material is quantified using the aniso -
tropy coefficient (α), which is defined by the following 
equation:
a =
(V
1
 V
2
)
V
2
× 100 [%] 
When the mechanical properties are measured through 
tensile testing in two directions, V1 and V2 represent this 
property in the directions with higher and lower values, 
respectively [ 257 ]. A smaller anisotropy coefficient indi -
cates isotropic tensile properties, whereas a larger coeffi -
cient reflects greater differences in the mechanical 
properties between the two directions. Owing to the 
layer-by-layer stacking inherent to AM, the microstruc -
ture of the deposits typically consists of an epitaxially 
grown columnar grain structure. Consequently, the 
strength is generally higher in the horizontal direction, 
whereas the EL tends to be higher in the vertical 
(build) direction. Figure 42 (a) compares the effects of 
cold- and hot-rolling on the anisotropy of IN718 
WAMM deposit before heat treatment. In conventional 
WAAM without rolling, the anisotropy coefficients for 
the UTS and YS exceed 8.5%, whereas that for EL 
reaches 16%, indicating high anisotropy. In contrast, 
Figure 40. Schematic of HRAAM system.
Table 14. Summary of the HRAAM on Ni-based superalloys.
Type of weldability Alloy
AM 
process Assistant process Rolling process parameter Effects of RAAM process Ref.
Weldable IN718 WAAM Inter-pass hot rolling +HT • The rolling force: 50 kN 
• Roller travel speed: 5 mm/s 
• Inter-pass cooling time: 3 min 
• Pre-heating temperature: 450°C 
• Homogenisation, solution, aging
• Improving hardness, YS, UTS, EL 
• Mitigating anisotropy of tensile properties
[ 257 ]
Weldable IN718 WAAM Inter-pass hot rolling 
+HT
• The rolling force: 50 kN 
• Roller travel speed: 5 mm/s 
• Inter-pass cooling time: 3 min 
• Pre-heating temperature: 450°C 
• Solution, aging
• Improving hardness, YS, UTS, EL 
• Mitigating anisotropy of tensile properties
[ 258 ]
56 
 J. JANG ET AL.

## Page 58

the anisotropy coefficients in HRAAM of Ni-based super -
alloys are reduced below 7.8% for UTS and YS and to 
7.3% for EL. These values are all lower than those 
observed after the RAAM process under the same 
roller load, demonstrating that HRAAM more effectively 
reduces anisotropy.
The anisotropy alleviation effect observed in the 
HRAAM of Ni-based superalloys becomes even more dis -
tinct after post-heat treatments. Zhang et al. [ 257 , 258 ] 
investigated the anisotropy of IN718 deposits fabricated 
using WAAM-based HRAAM after post-heat treatment; 
comparing the anisotropy coefficients for UTS, YS, and 
EL before heat treatment revealed that anisotropy in 
UTS, YS, and EL decreases in the order of conventional 
AM, RAAM, and HRAAM. Further, after performing sol -
ution and double aging treatment (SA), the anisotropy 
coefficients for the UTS and YS were lower than the 
pre-heat-treatment values, but EL did not significantly 
improve, as shown in Figure 42 (b). On the other hand, 
when a homogenisation treatment followed by SA 
(HSA) was performed, the anisotropy coefficients for 
the UTS and YS substantially decreased, along with 
drastic alleviation in elongation anisotropy, as shown 
in Figure 42 (c). Notably, WAAM-based HRAAM of IN718 
consistently exhibited the lowest material anisotropy 
among the three AM process conditions, regardless of 
whether post-heat treatments were performed. Among 
the conditions investigated, HRAAM combined with 
HSA achieved anisotropy coefficients of less than 3% 
for all mechanical properties, demonstrating isotropy 
comparable to that of wrought alloys. These research 
findings demonstrate that HRAAM plays a significant 
role in mitigating anisotropy, both when implemented 
alone and when combined with post-heat treatment.
6. Prospects
Energy-assisted AM technology has demonstrated sig -
nificant potential in addressing the process- and 
material-related issues of AM for Ni-based superalloys. 
However, further development is required for its appli -
cation in actual production processes. Applying 
additional energy in AM significantly increases the 
number of process variables, making optimisation essen -
tial to ensuring the repeatability and scalability of these 
processes. Consequently, further experimental studies 
are required to quantitatively analyze the relationships 
between EAAM variables, microstructures, and 
Figure 41. Comparative analysis of microstructure between the RAAM and HRAAM deposits: (a) OM images of cold rolled and hot 
rolled IN718 deposits fabricated by WAAM [ 258 ], (b) magnified OM images of grain structure in cold rolled and hot rolled IN718 depos -
its fabricated by WAAM [ 258 ], and (c) phase formation of the IN718 deposit fabricated by WAAM under three different rolling con -
ditions (as-built, cold rolled, hot rolled) [ 257 ].
VIRTUAL AND PHYSICAL PROTOTYPING 
 57

## Page 59

mechanical properties, and to identify optimal process 
conditions. To the best of the authors’ knowledge, 
process optimisation has not yet been conducted for 
certain material–EAAM methods combinations such as 
Haynes 230, GH3230, K447A with PAAM, IN625 with 
HPAAM, DZ4125, René N5 with ICAAM, indicating a 
clear research gap.
In particular, for non-weldable Ni-based superalloys, 
existing research has primarily focused on healing the 
cracks that form during solidification. However, given 
that AM-fabricated Ni-based superalloy parts are predo -
minantly used in high-temperature environments, the 
presence of low-melting-point phases surrounding 
healed cracks continues to increase their crack suscepti -
bility. Therefore, future research should focus on control -
ling the microstructure of the deposit to prevent liquid 
films from contributing to crack formation. To achieve 
this, new approaches are required, such as suppressing 
liquid film formation at grain boundaries, controlling 
the grain morphology to enhance backfilling, and 
designing new alloy compositions to reduce the 
amount of liquid film. In particular, as energy-assisted 
AM has expanded the range of Ni-based superalloys 
applicable to AM, leveraging data-driven approaches, 
such as deep-learning-based inverse alloy design to 
develop materials and optimise their microstructures 
while considering the AM process characteristics, are 
expected to suppress crack formation and maximise per -
formance in high-temperature environments.
Although this review focuses on the application of 
EAAM to Ni-based superalloys, it’s fundamental prin -
ciples are broadly applicable to a wide range of 
materials. This is because the mechanical and thermal 
energy applied during AM process can significantly 
influence microstructural evolution and crack formation. 
For instance, HIP has been shown to eliminate internal 
porosity and improve ductility in stainless steels 
[ 259 , 260 ], aluminum alloy [ 261 ], and Ti-6Al-4V [ 262 ]. 
Similary, rolling promotes grain refinement and 
improves mechanical isotropy in stainless steel [ 263 ] 
and Ti-6Al-4V [ 264 ]. Preheating strategies can moderate 
thermal gradients and suppress crack formation in 
martensitic stainless steels [ 265 ] and Ti-6Al-4V [ 266 ]. 
Furthermore, surface treatments such as peening and 
ultrasonic vibration, which induce compressive stresses 
and refine surface grains, have been successfully 
applied to materials such as Ti-6Al-4V [ 266 , 267 ], 
AlSi10Mg [ 268 ], and Fe-Cr-Ni-B-Si alloy [ 269 ]. Thus, the 
underlying mechanisms associated with mechanical 
and thermal energy input suggest a promising 
pathway for extending these strategies to a broader 
spectrum of materials.
7. Conclusion
This paper comprehensively reviews the effects of EAAM 
on both weldable and non-weldable Ni-based superal -
loys, where a trade-off relationship exists between print -
ability and performance. The principles and systems for 
applying mechanical and thermal energy, either indivi -
dually or simultaneously, in AM processes were intro -
duced, followed by an analysis of their distinct effects 
on weldable and non-weldable alloys. Energy-assisted 
AM effectively addresses challenges specific to AM pro -
cesses such as LMD, L-PBF, EB-PBF, and WAAM for weld -
able alloys. Additionally, it mitigates crack-related issues 
in non-weldable alloys, which exhibit poor weldability 
due to the formation of numerous cracks during AM. 
This analysis can provide a pathway toward selecting a 
adequate material-EAAM methods combibation, 
grounded in the principles that explain how additional 
energy enhances the printability and performance of 
the deposit as follows:
In mechanical energy-assisted AM, methods such as 
PAAM and RAAM have beneficial effects on the mechan -
ical property enhancement of weldable alloys by reliev -
ing residual stress, inducing work hardening, and 
promoting grain refinement. Additionally, these 
Figure 42. Comparison of the anisotropy coefficient between as-built, RAAM, and HRAAM deposits under three different heat treat -
ment conditions [ 257 ]: (a) before heat treatment, (b) after SA heat treatment, and (c) after HSA heat treatment.
58 
 J. JANG ET AL.

## Page 60

methods effectively mitigate the crack formation in non- 
weldable alloys by physically closing preformed cracks 
through plastic deformation. VAAM enhances densifica -
tion, induces CET, and suppresses segregation in weld -
able alloys, resulting in improved mechanical 
properties. Furthermore, in non-weldable alloys, VAAM 
prevents crack initiation and propagation by promoting 
the formation of fine equiaxed grains, which effectively 
dissipate tensile residual stress.
Thermal energy-assisted AM involves preheating 
using external heat sources, such as hot plates, induction 
coils, lasers or electron beams, to control the solidifica -
tion parameters of the deposit. For weldable alloys, 
this approach has been shown to improve mechanical 
properties and mitigate distortion by reducing residual 
stress, controlling grain morphology and size, and regu -
lating phase precipitation. In non-weldable alloys, 
thermal energy-assisted AM effectively suppresses 
crack formation during the process by alleviating 
thermal residual stress and promoting the formation of 
finer γ
′
precipitates.
Mechanical and thermal energy-assisted additive man -
ufacturing includes methods such as HIP and HRAAM, 
which employ atomic diffusion through thermal energy 
to achieve plastic deformation with less mechanical 
energy input. In weldable alloys, both HIP and HRAAM 
have been shown to effectively eliminate internal 
defects and increase the density of the deposit. Addition -
ally, as HIP operates within the post-heat-treatment 
temperature range of Ni-based superalloys, it has the 
potential to reduce total manufacturing time by integrat -
ing heat treatment into the process. In non-weldable 
alloys, mechanical and thermal energy have successfully 
removed internal cracks within the deposit. However, 
HIP has limitations in addressing surface-connected 
cracks due to its inability to apply pressure to such 
regions. Conversely, hot rolling has proven particularly 
effective in healing cracks near the surface, highlighting 
differences in the applicable range of these methods.
Acknowledgement
This work was supported by the National Research Foundation 
of Korea (NRF) grant funded by the Korea government (MSIT) 
under Grant 2023R1A2C1004272.
CRediT author statement
Junmyoung Jang: Writing – original draft, Writing – 
Review & Editing, Data curation, Investigation, 
Visualization.
Taehwan Ko: Writing – original draft, Investigation, Data 
curation, Visualization.
Jaeheon Lee: Writing – original draft, Data curation, 
Visualization.
Dukyong Kim: Writing – original draft, Data curation, 
Visualization.
Hwani Hwang: Writing – original draft, Data curation, 
Visualization.
Taesoon Jeong: Writing – original draft, Data curation, 
Visualization.
Heuisu Kim: Writing – original draft, Data curation, 
Visualization.
Seung Hwan Lee: Conceptualisation, Writing – Review & 
Editing, Supervision, Project administration, Funding 
acquisition.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
This work was supported by National Research Foundation of 
Korea [grant number: 2023R1A2C1004272].
Data availability statement
Data sharing is not applicable to this article as no new data 
were created or analyzed in this study.
References
[1] Caron P, Khan T. Evolution of Ni-based superalloys for 
single crystal gas turbine blade applications. Aerosp 
Sci Technol. 1999 ;3:513–523. doi: 10.1016/S1270- 
9638(99)00108-X
[2] Li D-W, Liu J-X, Sun Y-T, et al. Microstructure and mechan -
ical degradation of K403 Ni-based superalloy from ultra- 
long-term serviced turbine blade. J Alloys Compd. 
2023 ;957:170378. doi: 10.1016/j.jallcom.2023.170378
[3] Hashizume R, Yoshinari A, Kiyono T, et al. Development 
of Ni based single crystal superalloys for power gener -
ation gas turbine blades. Energy Materials. 2007 ;2:5– 
12. doi: 10.2355/tetsutohagane1955.90.7_518
[4] Cheng X, Xu J, Yang Z, et al. A novel nickel-based super -
alloy with excellent high temperature performance 
designed for laser additive manufacturing. Mater Sci 
Eng A. 2024 ;911:146926. doi: 10.1016/j.msea.2024.146926
[5] Szeliga D, Kubiak K, Motyka M, et al. Directional solidifi -
cation of Ni-based superalloy castings: thermal analysis. 
Vacuum. 2016 ;131:327–342. doi: 10.1016/j.vacuum.2016. 
07.009
[6] Theska F, Tse WF, Schulz B, et al. Review of microstruc -
ture–mechanical property relationships in cast and 
wrought Ni-based superalloys with boron, carbon, and 
zirconium microalloying additions. Adv Eng Mater. 
2022 ;25:2201514. doi: 10.1002/adem.202201514
[7] Han J-C. Recent studies in turbine blade cooling? The 
International Journal of Rotating Machinery. 
2004 ;10:443–457. doi: 10.1080/10236210490503978
VIRTUAL AND PHYSICAL PROTOTYPING 
 59

## Page 61

[8] Jiang C-PM, Wibisono AT, Macek W, et al. Enhancing internal 
cooling channel design in inconel 718 turbine blades via 
laser powder Bed fusion: A comprehensive review of 
surface topography enhancements. Int J Prec Eng Manuf. 
2024 ;26(2);487–511. doi: 10.1007/s12541-024-01177-3
[9] Boulila A, Boujelbene M, Fekiri C, et al. Optimization of 
manufacturing complex-shaped gas turbine blades. 
Measurement (Mahwah N J). 2019 ;135:768–781. doi: 10. 
1016/j.measurement.2018.12.040
[10] Wildgoose AJ, Thole KA, Sanders P, et al. Impact of addi -
tive manufacturing on internal cooling channels With 
varying diameters and build directions. J Turbomach. 
2021 ;143(7):071003. doi: 10.1115/1.4050336
[11] Tang P, Zhao X, Shi H, et al. A review of multi-axis addi -
tive manufacturing: potential, opportunity and chal -
lenge. Addit. Manuf. 2024 ;83:104075. doi: 10.1016/j. 
addma.2024.104075
[12] Kim D, Ko T, Lee SH. Study on the influence of proces -
sing variables under various tilting angles of laser 
nozzle and substrate on the deposition quality of the 
multi-axis laser metal deposition. J Laser Appl. 
2023 ;35:022025. doi: 10.2351/7.0000979
[13] Ajay P, Dabhade VV. Heat treatments of inconel 718 
nickel-based superalloy. A Review, Metals and 
Materials International. 2024 ;31(5):1204–1231. doi: 10. 
1007/s12540-024-01812-8
[14] Zhao C, Wang L, Wang B, et al. Effect of post-deposition 
heat treatments on the microstructure and tensile prop -
erties of wire-fed electron beam directed energy depo -
sition GH4169 Ni-based alloy. Mater Charact. 
2024 ;215:114177. doi: 10.1016/j.matchar.2024.114177
[15] Meng G, Gong Y, Zhang J, et al. Effect of heat treatment 
on microstructure, precipitation behavior and mechan -
ical properties of inconel 718 fabricated by laser direct 
energy deposition. Mater Sci Eng A. 2024 ;898:146396. 
doi: 10.1016/j.msea.2024.146396
[16] Wang Y, Guo W, Xie Y, et al. In-situ monitoring plume, 
spattering behavior and revealing their relationship 
with melt flow in laser powder bed fusion of nickel- 
based superalloy. J Mater Sci Technol. 2024 ;177:44–58. 
doi: 10.1016/j.jmst.2023.07.068
[17] Karimi P, Sadeghi E, Ålgårdh J, et al. EBM-manufactured 
single tracks of alloy 718: influence of energy input and 
focus offset on geometrical and microstructural charac -
teristics. Mater Charact. 2019 ;148:88–99. doi: 10.1016/j. 
matchar.2018.11.033
[18] Yu H, Fu J, Wang C, et al. Robust additive manufactur -
able Ni superalloys designed by the integrated optimiz -
ation of local elemental segregation and cracking 
susceptibility criteria. Acta Mater. 2024 ;266:119658. 
doi: 10.1016/j.actamat.2024.119658
[19] Chung H-T, Tsai C-C, Jen K-K, et al. Optimization of 
process parameters of selective laser melted nickel- 
based superalloy for densification by random forest 
regression algorithm and response surface method -
ology. Results in Engineering. 2024 ;22:102182. doi: 10. 
1016/j.rineng.2024.102182
[20] He X, Yang B, Kong D, et al. An integrated multiscale 
simulation guiding the processing optimisation for addi -
tively manufactured nickel-based superalloys. Virtual 
Phys Prototyp. 2024 ;19:e2313661. doi: 10.1080/ 
17452759.2024.2313661
[21] Spierings AB, Voegtlin M, Bauer T, et al. Powder flowabil -
ity characterisation methodology for powder-bed-based 
metal additive manufacturing. Progress Addit. Manuf. 
2015 ;1:9–20. doi: 10.1007/s40964-015-0001-4
[22] Gruber K, Smolina I, Kasprowicz M, et al. Evaluation of 
inconel 718 metallic powder to optimize the reuse of 
powder and to improve the performance and sustain -
ability of the laser powder Bed fusion (LPBF) process. 
Materials (Basel. 2021 ;14:1538. doi: 10.3390/ma14061538
[23] Murtaza HA, Mukhangaliyeva A, Golman B, et al. 
Quantitative characterization of metal powder mor -
phology, size distribution, and flowability for additive 
manufacturing. J Mater Eng Perform. 2023 ;33:10853– 
10867. doi: 10.1007/s11665-023-08761-0
[24] Hosseini E, Popovich VA. A review of mechanical proper -
ties of additively manufactured inconel 718. Addit. 
Manuf. 2019 ;30:100877. doi: 10.1016/j.addma.2019. 
100877
[25] Adomako N K, Haghdadi N, Primig S. Electron and laser- 
based additive manufacturing of Ni-based superalloys: A 
review of heterogeneities in microstructure and mech -
anical properties. Mater Des. 2022 ;223:111245. doi: 10. 
1016/j.matdes.2022.111245
[26] Yu Q, Wang C, Zhao Z, et al. New Ni-based superalloys 
designed for laser additive manufacturing. J Alloys 
Compd. 2021 ;861:157979. doi: 10.1016/j.jallcom.2020. 
157979
[27] Xu J, Kontis P, Peng RL, et al. Modelling of additive man -
ufacturability of nickel-based superalloys for laser 
powder bed fusion. Acta Mater. 2022 ;240:118307. 
doi: 10.1016/j.actamat.2022.118307
[28] Chauvet E, Kontis P, Jägle EA, et al. Hot cracking mech -
anism affecting a non-weldable Ni-based superalloy 
produced by selective electron beam melting. Acta 
Mater. 2018 ;142:82–94. doi: 10.1016/j.actamat.2017.09. 
047
[29] Zhang X, Chen H, Xu L, et al. Cracking mechanism and 
susceptibility of laser melting deposited inconel 738 
superalloy. Mater Des. 2019 ;183:108105. doi: 10.1016/j. 
matdes.2019.108105
[30] Guo C, Li G, Li S, et al. Additive manufacturing of Ni- 
based superalloys: residual stress, mechanisms of crack 
formation and strategies for crack inhibition. Nano 
Materials Science. 2023 ;5:53–77. doi: 10.1016/j.nanoms. 
2022.08.001
[31] Li Y, Kan W, Zhang Y, et al. Microstructure, mechanical 
properties and strengthening mechanisms of IN738LC 
alloy produced by electron beam selective melting. 
Addit. Manuf. 2021 ;47:102371. doi: 10.1016/j.addma. 
2021.102371
[32] Hsu K-T, Wang H-S, Chen H-G, et al. Effects of the Hot iso -
static pressing process on crack healing of the laser 
repair-welded CM247LC superalloy. Metals (Basel). 
2016 ;6(10);238. doi: 10.3390/met6100238
[33] Goel S, Ahlfors M, Bahbou F, et al. Effect of different 
post-treatments on the microstructure of EBM-built 
alloy 718. J Mater Eng Perform. 2018 ;28:673–680. 
doi: 10.1007/s11665-018-3712-0
[34] Jang J, Yim J, Lee SH. Enhanced creep stability in inconel 
718 deposited by induction-heating-assisted laser- 
directed energy deposition. Mater Sci Eng A. 
2023 ;880:145319. doi: 10.1016/j.msea.2023.145319
60 
 J. JANG ET AL.

## Page 62

[35] Wang Y, Guo W, Li H, et al. Nano-scale microstructural 
evolution and mechanical property enhancement mech -
anism during crack inhibition in nickel-based superalloys 
fabricated by laser powder bed fusion. Addit. Manuf. 
2025 ;100:104685. doi: 10.1016/j.addma.2025.104685
[36] Hu X, Guo C, Huang Y, et al. Liquid-induced healing of 
cracks in nickel-based superalloy fabricated by laser 
powder bed fusion. Acta Mater. 2024 ;267:119731. 
doi: 10.1016/j.actamat.2024.119731
[37] Kalentics N, Sohrabi N, Tabasi HG, et al. Healing cracks in 
selective laser melting by 3D laser shock peening. Addit. 
Manuf. 2019 ;30:100881. doi: 10.1016/j.addma.2019.100881
[38] Wang Y, Roy S, Choi H, et al. Cracking suppression in 
additive manufacturing of hard-to-weld nickel-based 
superalloy through layer-wise ultrasonic impact 
peening. J. Manuf. Process. 2022 ;80:320–327. doi: 10. 
1016/j.jmapro.2022.05.041
[39] Sebdani RM, Gale J, Bilan H, et al. In-situ ultrasonic 
impact treatment (UIT) to improve the fatigue proper -
ties of laser powder bed fusion (LPBF) manufactured 
inconel 718. Mater. Chem. Phys. 2024 :129595. doi: 10. 
1016/j.matchemphys.2024.129595
[40] Amanov A, Karimbaev R, Li C, et al. Effect of surface 
modification technology on mechanical properties and 
dry fretting wear behavior of inconel 718 alloy fabri -
cated by laser powder-based direct energy deposition. 
Surf. Coat. Technol. 2023 ;454:129175. doi: 10.1016/j. 
surfcoat.2022.129175
[41] Jinoop A, Subbu SK, Paul C, et al. Post-processing of laser 
additive manufactured inconel 718 using laser shock 
peening. Int. J. Precis. Eng. Manuf. 2019 ;20:1621–1628. 
doi: 10.1016/j.surfcoat.2019.125136
[42] Chen Y, Xu M, Zhang T, et al. Grain refinement and 
mechanical properties improvement of inconel 625 
alloy fabricated by ultrasonic-assisted wire and arc addi -
tive manufacturing. J Alloys Compd. 2022 ;910:164957. 
doi: 10.1016/j.jallcom.2022.164957
[43] Khan K M, Rao TB, Manjunath BN, et al. Studies on the 
effect of substrate preheating, interlayer dwell, and 
heat treatment on microstructure, residual stress, and 
mechanical properties of IN625 superalloy built by 
direct metal deposition. J Eng Mater Technol. 
2023 ;145:041004. doi: 10.1115/1.4062503
[44] Adomako NK, Haines M, Haghdadi N, et al. On the role of 
the preheat temperature in electron-beam powder bed 
fusion processed IN718. Addit. Manuf Lett. 
2024 ;11:100238. doi: 10.1016/j.addlet.2024.100238
[45] Tan C, Li R, Su J, et al. Review on field assisted metal addi -
tive manufacturing. Int J Mach Tools Manuf. 
2023 ;189:104032. doi: 10.1016/j.ijmachtools.2023.104032
[46] Chen C, Zhang Z, Cai Y, et al. Research and development 
status of in situ field assisted laser additive manufactur -
ing: A review. Opt Laser Technol. 2025 ;181:111700. 
doi: 10.1016/j.optlastec.2024.111700
[47] Lv J, Liang Y, Xu X, et al. Performance-control-orientated 
hybrid metal additive manufacturing technologies: state 
of the art, challenges, and future trends. International 
Journal of Extreme Manufacturing. 2024 ;6:032009. 
doi: 10.1088/2631-7990/ad3315
[48] Farias FWC, dos Santos TJG, Oliveira JP. Directed energy 
deposition + mechanical interlayer deformation additive 
manufacturing: a state-of-the-art literature review. The 
International Journal of Advanced Manufacturing 
Technology. 2024 ;131:999–1038. doi: 10.1007/s00170-024- 
13126-5
[49] Zhang S, Lin X, Wang L, et al. Strengthening mechan -
isms in selective laser-melted Inconel718 superalloy. 
Mater Sci Eng A. 2021 ;812:141145. doi: 10.1016/j.msea. 
2021.141145
[50] Shahwaz M, Nath P, Sen I. A critical review on the 
microstructure and mechanical properties correlation 
of additively manufactured nickel-based superalloys. J 
Alloys Compd. 2022 ;907:164530. doi: 10.1016/j.jallcom. 
2022.164530
[51] Laleh M, Sadeghi E, Revilla RI, et al. Heat treatment for 
metal additive manufacturing. Prog Mater Sci. 
2023 ;133:101051. doi: 10.1016/j.pmatsci.2022.101051
[52] Wei S, Wang P, Zhang L, et al. Grain morphologies in 
additively manufactured alloys: from solidification fun -
damentals to advanced microstructure control. J Mater 
Sci Technol. 2025 ;235:133–145. doi: 10.1016/j.jmst.2025. 
02.033
[53] Mukherjee T, Elmer JW, Wei HL, et al. Control of grain 
structure, phases, and defects in additive manufacturing 
of high-performance metallic components. Prog Mater 
Sci. 2023 ;138:101153. doi: 10.1016/j.pmatsci.2023.101153
[54] Meng TL, Wang T, Lin M, et al. Grinding-and robotic 
hammer peening-induced modifications in the near- 
surface regions of laser-cladded inconel 718 coatings. 
Surf. Coat. Technol. 2024 ;489:131130. doi: 10.1016/j. 
surfcoat.2024.131130
[55] Goodfellow AJ. Strengthening mechanisms in polycrys -
talline nickel-based superalloys. Mater Sci Technol. 
2018 ;34:1793–1808. doi: 10.1080/02670836.2018.1461594
[56] Lee SH. CMT-Based Wire Arc additive manufacturing 
using 316L stainless steel: effect of heat accumulation 
on the multi-layer deposits. Metals (Basel). 
2020 ;10:278. doi: 10.3390/met10020278
[57] Chen SG, Gao HJ, Zhang YD, et al. Review on residual 
stresses in metal additive manufacturing: formation 
mechanisms, parameter dependencies, prediction and 
control approaches. J Mater Res Technol. 
2022 ;17:2950–2974. doi: 10.1016/j.jmrt.2022.02.054
[58] Fang Z-C, Wu Z-L, Huang C-G, et al. Review on residual 
stress in selective laser melting additive manufacturing 
of alloy parts. Opt Laser Technol. 2020 ;129:106283. 
doi: 10.1016/j.optlastec.2020.106283
[59] Ye C, Zhang C, Zhao J, et al. Effects of post-processing on 
the surface finish, porosity, residual stresses, and fatigue 
performance of additive manufactured metals: A review. 
J Mater Eng Perform. 2021 ;30:6407–6425. doi: 10.1007/ 
s11665-021-06021-7
[60] Wang D, Han H, Sa B, et al. A review and a statistical 
analysis of porosity in metals additively manufactured 
by laser powder bed fusion. Opto-Electronic Advances. 
2022 ;5(10):210058. doi: 10.29026/oea.2022.210058
[61] Huang DJ, Li H. A machine learning guided investigation 
of quality repeatability in metal laser powder bed fusion 
additive manufacturing. Mater Des. 2021 ;203:109606. 
doi: 10.1016/j.matdes.2021.109606
[62] Dekis M, Tawfik M, Egiza M, et al. Challenges and devel -
opments in wire arc additive manufacturing of steel: A 
review. Results in Engineering. 2025 ;26:104657. doi: 10. 
1016/j.rineng.2025.104657
VIRTUAL AND PHYSICAL PROTOTYPING 
 61

## Page 63

[63] Wang W, Lin W, Yang R, et al. Mesoscopic evolution of 
molten pool during selective laser melting of superalloy 
inconel 738 at elevating preheating temperature. Mater 
Des. 2022 ;213:110355. doi: 10.1016/j.matdes.2021. 
110355
[64] Goodfellow AJ, Galindo-Nava EI, Schwalbe C, et al. The 
role of composition on the extent of individual strength -
ening mechanisms in polycrystalline Ni-based superal -
loys. Mater Des. 2019 ;173:107760. doi: 10.1016/j. 
matdes.2019.107760
[65] Kumar D, Idapalapati S, Wang W, et al. Microstructural 
characteristics and strengthening mechanisms in a poly -
crystalline Ni-based superalloy under deep cold rolling. 
Mater Sci Eng A. 2019 ;753:285–299. doi: 10.1016/j.msea. 
2019.03.005
[66] Su Y, Dai Z, Yang T, et al. Study on hot deformation 
behavior and strengthening mechanism of inconel 625 
deposited metal at high temperature. J Mater Sci. 
2021 ;56:16745–16761. doi: 10.1007/s10853-021-06357-4
[67] Ma Y, Ding Y, Gao Y, et al. Strengthening the mechanical 
properties of inconel 625 superalloy with gradient 
nanotwinned structure. J Mater Eng Perform. 
2023 ;32(24):11260–11274. doi: 10.1007/s11665-023- 
07915-4
[68] Zhang Y, Yang L, Chen T, et al. Investigation on the opti -
mized heat treatment procedure for laser fabricated 
IN718 alloy. Opt Laser Technol. 2017 ;97:172–179. 
doi: 10.1016/j.optlastec.2017.06.027
[69] Chen S, Yu H, Lu N, et al. The effect of carbon content on 
the printability and mechanical properties of Ni-based 
superalloy in laser additive manufacturing. Mater Sci 
Eng A. 2024 ;898:146398. doi: 10.1016/j.msea.2024. 
146398
[70] Winowlin Jappes JT, Ajithram A, Adamkhan M, et al. 
Welding on Ni based super alloys – A review. Mater 
Today Proc. 2022 ;60:1656–1659. doi: 10.1016/j.matpr. 
2021.12.208
[71] Zhang S, Wang L, Lin X, et al. The formation and dissol -
ution mechanisms of laves phase in inconel 718 fabri -
cated by selective laser melting compared to directed 
energy deposition and cast. Compos B Eng. 
2022 ;239:109994. doi: 10.1016/j.compositesb.2022. 
109994
[72] Xi N, Ni Z, Fang X, et al. Role of δ-phase on mechanical 
behaviors of additive manufactured inconel 718: 
detailed microstructure analysis and crystal plasticity 
modelling. Int J Plast. 2023 ;168:103708. doi: 10.1016/j. 
ijplas.2023.103708
[73] Jang J, Van D, Lee SH. Precipitation kinetics of secondary 
phases induced by heat accumulation in the deposit of 
inconel 718. Addit. Manuf. 2022 ;55:102831. doi: 10.1016/ 
j.addma.2022.102831
[74] Starikov K, Polozov I, Borisov E, et al. Selective laser 
melting of Non-weldable nickel superalloy: microstruc -
ture, cracks and texture. Metals (Basel). 2023 ;13:1886. 
doi: 10.3390/met13111886
[75] Dang X, Li Y, Chen K, et al. Avoiding cracks in additively 
manufactured non-weldable directionally solidified Ni- 
based superalloys. Addit. Manuf. 2022 ;59:103095. 
doi: 10.1016/j.addma.2022.103095
[76] Zhou Z, Huang L, Shang Y, et al. Causes analysis on 
cracks in nickel-based single crystal superalloy 
fabricated by laser powder deposition additive manu -
facturing. Mater Des. 2018 ;160:1238–1249. doi: 10.1016/ 
j.matdes.2018.10.042
[77] Yi Z, Shan J, Zhao Y, et al. Recent research progress in 
the mechanism and suppression of fusion welding- 
induced liquation cracking of nickel based superalloys, 
international journal of minerals. Metallurgy and 
Materials. 2024 ;31:1072–1088. doi: 10.1007/s12613-024- 
2869-9
[78] Xu J, Lin X, Zhao Y, et al. HAZ liquation cracking mech -
anism of IN-738LC superalloy prepared by laser solid 
forming. Metallurgical and Materials Transactions A. 
2018 ;49:5118–5136. doi: 10.1007/s11661-018-4826-6
[79] Taheri M. Analysis of solidification and liquation cracks 
in the electron beam welding of IN738 superalloy, 
metallography. Microstructure, and Analysis. 
2021 ;10:815–822. doi: 10.1007/s13632-021-00793-z
[80] Zhao Y, Ma Z, Yu L, et al. New alloy design approach to 
inhibiting hot cracking in laser additive manufactured 
nickel-based superalloys. Acta Mater. 2023 ;247:118736. 
doi: 10.1016/j.actamat.2023.118736
[81] Zhang Z, Zhao Y, Shan J, et al. Evolution behavior of 
liquid film in the heat-affected zone of laser cladding 
non-weldable nickel-based superalloy. J Alloys Compd. 
2021 ;863:158463. doi: 10.1016/j.jallcom.2020.158463
[82] Carter LN, Martin C, Withers PJ, et al. The influence of the 
laser scan strategy on grain structure and cracking 
behaviour in SLM powder-bed fabricated nickel superal -
loy. J Alloys Compd. 2014 ;615:338–347. doi: 10.1016/j. 
jallcom.2014.06.172
[83] Attallah MM, Jennings R, Wang X, et al. Additive manu -
facturing of Ni-based superalloys: The outstanding 
issues. MRS Bull. 2016 ;41:758–764. doi: 10.1557/mrs. 
2016.211
[84] Shahwaz M, Nath P, Sen I. Recent advances in additive 
manufacturing technologies for Ni-based inconel super -
alloys – A comprehensive review. J Alloys Compd. 
2025 ;1010:177654. doi: 10.1016/j.jallcom.2024.177654
[85] Barrett PR, Ahmed R, Menon M, et al. Isothermal low- 
cycle fatigue and fatigue-creep of haynes 230. Int J 
Solids Struct. 2016 ;88-89:146–164. doi: 10.1016/j.ijsolstr. 
2016.03.011
[86] Du B, Hu Z, Sheng L, et al. Tensile, creep behavior and 
microstructure evolution of an as-cast Ni-based K417G 
polycrystalline superalloy. J Mater Sci Technol. 
2018 ;34:1805–1816. doi: 10.1016/j.jmst.2018.02.007
[87] John R, Buchanan DJ, Caton MJ, et al. Stability of shot 
peen residual stresses in IN100 subjected to creep and 
fatigue loading. Procedia Eng. 2010 ;2:1887–1893. 
doi: 10.1016/j.proeng.2010.03.203
[88] Li D, Li G, Wei X, et al. Long-term aging behavior and 
mechanism of CMSX-4 nickel-based single crystal super -
alloy at 950 and 1050 ℃. J Alloys Compd. 
2024 ;1004:175763. doi: 10.1016/j.jallcom.2024.175763
[89] Mathew MD, Parameswaran P, Bhanu Sankara Rao K. 
Microstructural changes in alloy 625 during high temp -
erature creep. Mater Charact. 2008 ;59:508–513. doi: 10. 
1016/j.matchar.2007.03.007
[90] Megahed S, Krämer KM, Heinze C, et al. Influence of build 
orientation on the creep behavior of IN738LC manufac -
tured with laser powder bed fusion. Mater Sci Eng A. 
2023 ;878:145197. doi: 10.1016/j.msea.2023.145197
62 
 J. JANG ET AL.

## Page 64

[91] Sun H, Tian S, Tian N, et al. Microstructure heterogeneity 
and creep damage of DZ125 nickel-based superalloy. 
Progress in Natural Science: Materials International. 
2014 ;24:266–273. doi: 10.1016/j.pnsc.2014.05.004
[92] Sun Z, Jiang X, Zheng W, et al. Creep rupture life predic -
tion methodology based on establishment of the corre -
lations between creep properties of superalloy in virgin 
and degraded conditions. J Mater Sci. 2024 ;59:11633– 
11643. doi: 10.1007/s10853-024-09863-3
[93] Xu Q, Hou C, Ren X, et al. Study on creep behaviors of 
GH3230 superalloy With side notches or a center 
inclined hole at 900°C and 1000°C. Fatigue & Fracture 
of Engineering Materials & Structures. 2024 ;48:669– 
683. doi: 10.1111/ffe.14498
[94] Zhang Z, Zhao Y, Shan J, et al. Influence of heat treat -
ment on microstructures and mechanical properties of 
K447A cladding layers obtained by laser solid forming. 
J Alloys Compd. 2019 ;790:703–715. doi: 10.1016/j. 
jallcom.2019.03.136
[95] Zhou B, Huang S, Wang T, et al. Investigation of high- 
temperature tensile properties and fracture mechanisms 
of GH3536 alloy fabricated by selective laser melting. 
Metals (Basel). 2025 ;15(4):381. doi: 10.3390/met15040381
[96] Fu S, Dong J, Zhang M, et al. Research on Inconel 718 
type alloys with improvement of temperature capability, 
in: 7th International Symposium on Superalloy, 2010, 
pp. 281-96. doi: 10.1002/9781118495223.ch21
[97] Kvapilová M, Kuchařová K, Hrbáček K, et al. Creep pro -
cesses in MAR-M247 nickel-base superalloy. Solid State 
Phenomena. 2017 ;258:603–606. doi: 10.1515/htmp- 
2019-0006
[98] Groh JR, Mourer DP. Alternate material for elevated 
temperature turbine cooling plate applications. 
Superalloys 2004 ;2004:101–108. doi: 10.7449/2004/ 
Superalloys_2004_101_108
[99] Basak A, Das S. A study on the microstructural character -
ization of rené 142 deposited atop rené 125 processed 
through scanning laser epitaxy,: in: materials science 
forum. Trans Tech Publ. 2017 ;879:187–192. doi: 10. 
4028/www.scientific.net/MSF.879.187
[100] John M, Kalvala PR, Misra M, et al. Peening techniques 
for surface modification. Processes, Properties, and 
Applications, Materials. 2021 ;14(14):3841. doi: 10.3390/ 
ma14143841
[101] Liu Y, Shi J, Wang Y. Evolution, control, and mitigation of 
residual stresses in additively manufactured metallic 
materials: a review. Adv. Eng. Mater. 
2023 ;25(21):2300489. doi: 10.1002/adem.202300489
[102] Balbaa M, Ghasemi A, Fereiduni E, et al. Improvement of 
fatigue performance of laser powder bed fusion fabri -
cated IN625 and IN718 superalloys via shot peening. J. 
Mater. Process. Technol. 2022 ;304:117571. doi: 10.1016/ 
j.jmatprotec.2022.117571
[103] Foss B, Gray S, Hardy M, et al. Analysis of shot-peening 
and residual stress relaxation in the nickel-based super -
alloy RR1000. Acta Mater. 2013 ;61:2548–2559. doi: 10. 
1016/j.actamat.2013.01.031
[104] Deng W, Wang C, Lu H, et al. Progressive developments, 
challenges and future trends in laser shock peening of 
metallic materials and alloys: A comprehensive review. 
Int J Mach Tools Manuf. 2023 ;191:104061. doi: 10.1016/ 
j.ijmachtools.2023.104061
[105] Kladovasilakis N, Charalampous P, Kostavelis I, et al. 
Impact of metal additive manufacturing parameters 
on the powder bed fusion and direct energy depo -
sition processes: A comprehensive review. Prog. 
Addit. Manuf. 2021 ;6:349–365. doi: 10.1007/s40964- 
021-00180-8
[106] Chen L, Li Y, Yu T, et al. Effects of ultrasonic shot peening 
process on the microstructure and mechanical proper -
ties of nickel-based superalloys formed by selective 
laser melting. J Mater Process Technol. 2025 ;335: 
118667. doi: 10.1016/j.jmatprotec.2024.118667
[107] Lesyk D, Martinez S, Mordyuk B, et al. Post-processing of 
the inconel 718 alloy parts fabricated by selective laser 
melting: effects of mechanical surface treatments on 
surface topography, porosity, hardness and residual 
stress. Surf. Coat. Technol. 2020 ;381:125136. doi: 10. 
1016/j.surfcoat.2019.125136
[108] Wang Y, Shi J. Microstructure and properties of inconel 
718 fabricated by directed energy deposition with in- 
situ ultrasonic impact peening. Metall Mater Trans B. 
2019 ;50:2815–2827. doi: 10.1007/s11663-019-01672-3
[109] Zhou S, Liu Z, Yang G, et al. Heterostructure microstruc -
ture and laves phase evolution mechanisms during 
inter-layer hammering hybrid directed energy depo -
sition (DED) process. Mater Sci Eng A. 
2023 ;886:145668. doi: 10.1016/j.msea.2023.145668
[110] Mythreyi OV, Raja A, Nagesha BK, et al. Corrosion study 
of selective laser melted IN718 alloy upon post heat 
treatment and shot peening. Metals (Basel). 
2020 ;10(12):1562. doi: 10.3390/met10121562
[111] Lesyk D, Dzhemelinskyi V, Martinez S, et al. Surface shot 
peening post-processing of inconel 718 alloy parts 
printed by laser powder bed fusion additive manufac -
turing. J. Mater. Eng. Perform. 2021 ;30:6982–6995. 
doi: 10.1007/s11665-021-06103-6
[112] Liu W, Li H, Yin Q, et al. Promoting densification and 
strengthening effect of ultrasonic impact treatment on 
haynes 230 alloy manufactured by laser powder bed 
fusion. J. Mater. Sci. Technol. 2025 ;216:226–240. doi: 10. 
1016/j.jmst.2024.07.036
[113] Bianchetti C, Tsoutsouva MG, Toualbi L, et al. Surface 
treatment impact on fatigue life at 550° C of the as- 
built inconel 718 manufactured by laser-powder bed 
fusion. Mater. Charact. 2023 ;206:113386. doi: 10.1016/j. 
matchar.2023.113386
[114] Yu T, Chen L, Zhang X, et al. Effect of ultrasonic shot 
peening on microstructure and mechanical properties 
of GH3230 superalloy during selective laser melt sol -
ution heat treatment. Mater. Today Commun. 
2024 ;39:108850. doi: 10.1016/j.mtcomm.2024.108850
[115] Wang Y, Shi J. Recrystallization behavior and tensile 
properties of laser metal deposited inconel 718 upon 
in-situ ultrasonic impact peening and heat treatment. 
Mater Sci Eng A. 2020 ;786:139434. doi: 10.1016/j.msea. 
2020.139434
[116] Haribaskar R, Kumar TS, Tamiloli N. Surface integrity of 
additively manufactured inconel-718 by peening 
approaches. Mater. Manuf. Process. 2023 ;38:1009– 
1019. doi: 10.1080/10426914.2022.2146716
[117] Banderas-Hernández JA, Rubio-González C, Gómez- 
Ortega A, et al. Laser shock peening as a post-processing 
technique for inconel 718 components manufactured by 
VIRTUAL AND PHYSICAL PROTOTYPING 
 63

## Page 65

laser powder bed fusion. Int. J. Adv. Manuf. Technol. 
2024 ;132:669–687. doi: 10.1007/s00170-024-13402-4
[118] Chen L, Gu P, Ge T, et al. Effect of laser shock peening on 
microstructure and mechanical properties of TiC 
strengthened inconel 625 alloy processed by selective 
laser melting. Mater Sci Eng A. 2022 ;835:142610. 
doi: 10.1016/j.msea.2022.142610
[119] Wang Y, Huang S, Sheng J, et al. Strengthening effect of laser 
peening on fatigue performance and life extension of laser 
cladded IN718 nickel-based alloy parts. Int J Fatigue. 
2024 ;180:108081. doi: 10.1016/j.ijfatigue.2023.108081
[120] Zhang Z, Zhao Y, Shan J, et al. The role of shot peening 
on liquation cracking in laser cladding of K447A nickel 
superalloy powders over its non-weldable cast structure. 
Mater Sci Eng A. 2021 ;823:141678. doi: 10.1016/j.msea. 
2021.141678
[121] Chen L, Xie J, Li Y, et al. Effect of laser/ultrasonic shock 
peening on the microstructure and mechanical proper -
ties of nickel-based superalloys prepared by powder Bed 
fusion laser beam (PBF-LB). J. Mater. Res. Technol-JMRT. 
2024 ;33:7668–7680. doi: 10.1016/j.jmrt.2024.11.147
[122] Lesyk D, Martinez S, Pedash O, et al. Nickel superalloy 
turbine blade parts printed by laser powder bed 
fusion: thermo-mechanical post-processing for 
enhanced surface integrity and precipitation strength -
ening. J Mater Eng Perform. 2022 ;31:6283–6299. 
doi: 10.1007/s11665-022-06710-x
[123] Atamanenko T, Eskin D, Zhang L, et al. Criteria of grain 
refinement induced by ultrasonic melt treatment of 
aluminum alloys containing Zr and Ti. Metallurgical 
and Materials Transactions A. 2010 ;41:2056–2066. 
doi: 10.1007/s11661-010-0232-4
[124] Lei Z, Bi J, Li P, et al. Melt flow and grain refining in ultra -
sonic vibration assisted laser welding process of AZ31B 
magnesium alloy. Opt Laser Technol. 2018 ;108:409–417. 
doi: 10.1016/j.optlastec.2018.07.015
[125] Ramirez A, Qian M, Davis B, et al. Potency of high-inten -
sity ultrasonic treatment for grain refinement of mag -
nesium alloys. Scr Mater. 2008 ;59:19–22. doi: 10.1016/j. 
scriptamat.2008.02.017
[126] Yuan T, Kou S, Luo Z. Grain refining by ultrasonic stirring 
of the weld pool. Acta Mater. 2016 ;106:144–154. doi: 10. 
1016/j.actamat.2016.01.016
[127] Todaro C, Easton M, Qiu D, et al. Grain refinement of 
stainless steel in ultrasound-assisted additive manufac -
turing. Addit. Manuf. 2021 ;37:101632. doi: 10.1016/j. 
addma.2020.101632
[128] Ou Y, Lu Q, Li C, et al. Effect of vibration frequency on 
microstructure and properties of laser-welded inconel 
718 nickel-base superalloy. J Mater Eng Perform. 
2021 ;30:2399–2407. doi: 10.1007/s11665-020-05392-7
[129] Xu M, Chen Y, Zhang T, et al. Effect of post-heat treat -
ment on microstructure and mechanical properties of 
nickel-based superalloy fabricated by ultrasonic-assisted 
wire arc additive manufacturing. Mater Sci Eng A. 
2023 ;863:14454. doi: 10.1016/j.msea.2022.144548
[130] Ning F, Jiang D, Liu Z, et al. Ultrasonic frequency effects 
on the melt pool formation, porosity, and thermal- 
dependent property of inconel 718 fabricated by ultra -
sonic vibration-assisted directed energy deposition. J 
Manuf Sci Eng. 2021 ;143(5):051009. doi: 10.1115/1. 
4048515
[131] Wang H, Hu Y, Ning F, et al. Ultrasonic vibration-assisted 
laser engineered net shaping of inconel 718 parts: 
effects of ultrasonic frequency on microstructural and 
mechanical properties. J Mater Process Technol. 
2020 ;276:116395. doi: 10.1016/j.jmatprotec.2019.116395
[132] Yang Z, Zhu L, Wang S, et al. Effects of ultrasound on 
multilayer forming mechanism of inconel 718 in 
directed energy deposition. Addit. Manuf. 
2021 ;48:102462. doi: 10.1016/j.addma.2021.102462
[133] Dash BK, Bhatnagar S, Magham HSR, et al. Effect of ultra -
sonic vibration on microstructural evolution, clad 
defects, and surface properties in laser direct energy 
deposition of inconel 625. J Laser Appl. 
2024 ;36(2):022002. doi: 10.2351/7.0001258
[134] Ning F, Hu Y, Liu Z, et al. Ultrasonic vibration-assisted 
laser engineered net shaping of inconel 718 parts: 
microstructural and mechanical characterization. J 
Manuf Sci Eng. 2018 ;140(6):061012. doi: 10.1115/1. 
4039441
[135] Xu M, Chen Y, Zhang T, et al. Effect of grain refinement 
on strain hardening behavior of nickel-based superalloy 
fabricated by wire arc additive manufacturing. Mater 
Lett. 2022 ;324:132723. doi: 10.1016/j.matlet.2022. 
132723
[136] Lv J, Zhou J, Zhang T, et al. Microstructure and wear 
properties of IN718/WC composite coating fabricated 
by ultrasonic vibration-assisted laser cladding. 
Coatings. 2022 ;12(3):412. doi: 10.3390/ 
coatings12030412
[137] Chen J, Yao Z, Wang F, et al. Grain refinement and laves 
phase dispersion by high-intensity ultrasonic vibration 
in laser cladding of inconel 718. J Mater Res Technol. 
2024 ;30:8563–8575. doi: 10.1016/j.jmrt.2024.05.229
[138] Ma Q, Chen H, Ren N, et al. Effects of ultrasonic vibration 
on microstructure, mechanical properties, and fracture 
mode of inconel 625 parts fabricated by cold metal 
transfer arc additive manufacturing. J Mater Eng 
Perform. 2021 ;30:6808–6820. doi: 10.1007/s11665-021- 
06023-5
[139] Todaro C, Easton M, Qiu D, et al. Grain structure control 
during metal 3D printing by high-intensity ultrasound. 
Nat Commun. 2020 ;11(1):142. doi: 10.1038/s41467-019- 
13874-z
[140] Fan Q, Chen C, Fan C, et al. Ultrasonic induces grain 
refinement in gas tungsten arc cladding AlCoCrFeNi 
high-entropy alloy coatings. Mater Sci Eng A. 
2021 ;821:141607. doi: 10.1016/j.msea.2021.141607
[141] Xiao H, Li S, Han X, et al. Laves phase control of inconel 
718 alloy using quasi-continuous-wave laser additive 
manufacturing. Mater Des. 2017 ;122:330–339. doi: 10. 
1016/j.matdes.2017.03.004
[142] Kou S. Welding metallurgy, A John Wiley & Sons Inc. 
2003. doi: 10.1557/mrs2003.197
[143] Tian Z, Zheng Y, Wang H, et al. Crack inhibition of non- 
weldable inconel 738 alloy in ultrasound-assisted laser 
directed energy deposition. Mater Sci Eng A. 
2025 ;921:147607. doi: 10.1016/j.msea.2024.147607
[144] Lee J, Jang J, Lee S, et al. Mitigating solidification crack -
ing during the laser welding of extruded Al–Mg–Si alloys 
by tailoring the microstructure. Engineering Science and 
Technology, an International Journal. 2024 ;55:101759. 
doi: 10.1016/j.jestch.2024.101759
64 
 J. JANG ET AL.

## Page 66

[145] Lin S, Aliravci C, Pekguleryuz M. Hot-tear susceptibility of 
aluminum wrought alloys and the effect of grain 
refining. Metallurgical and Materials Transactions A. 
2007 ;38:1056–1068. doi: 10.1007/s11661-007-9132-7
[146] Zhang T, Li H, Gong H, et al. Effect of rolling force on 
tensile properties of additively manufactured inconel 
718 at ambient and elevated temperatures. J. Alloy. 
Compd. 2021 ;884:161050. doi: 10.1016/j.jallcom.2021. 
161050
[147] Xu X, Ganguly S, Ding J, et al. Enhancing mechanical 
properties of wire+ arc additively manufactured 
INCONEL 718 superalloy through in-process thermo -
mechanical processing. Mater. Des. 2018 ;160:1042– 
1051. doi: 10.1016/j.matdes.2018.10.038
[148] Sunny S, Mathews R, Yu H, et al. Effects of microstructure 
and inherent stress on residual stress induced during 
powder bed fusion with roller burnishing. Int. J. Mech. 
Sci. 2022 ;219:107092. doi: 10.1016/j.ijmecsci.2022.107092
[149] Raaj RK, Anirudh PV, Karunakaran C, et al. Exploring 
grinding and burnishing as surface post-treatment 
options for electron beam additive manufactured alloy 
718. Surf. Coat. Technol. 2020 ;397:126063. doi: 10.1016/ 
j.surfcoat.2020.126063
[150] Yaman N, Sunay N, Kaya M, et al. Enhancing surface 
integrity of additively manufactured inconel 718 by 
roller burnishing process. Procedia CIRP. 2022 ;108:681– 
686. doi: 10.1016/j.procir.2022.03.106
[151] Kaya M, Yaman N, Taşcioğlu E, et al. Influence of burnish -
ing process on surface integrity of inconel 718 fabri -
cated by laser powder bed fusion additive 
manufacturing. Sigma J. Eng. Nat. Sci. 2024 ;42:335– 
343. doi: 10.14744/sigma.2023.00101
[152] Alharbi N. Optimization of electric current-assisted sus -
tainable burnishing process of additively manufactured 
inconel 718: trade-off between production rate and 
fatigue life. Int. J. Adv. Manuf. Technol. 
2024 ;132(5):3067–3092. doi: 10.1007/s00170-024-13417-x
[153] Alharbi N. Interaction of electric current with burnishing 
parameters in surface integrity assessment of additively 
manufactured inconel 718. Measurement ( Mahwah N J). 
2024 ;230:114474. doi: 10.1016/j.measurement.2024. 
114474
[154] Qi B, Chai Z, Huang X, et al. Surface integrity improve -
ment of the ground surface of inconel 718 fabricated 
by forging and additive manufacturing using a robotic 
rotational burnishing method. J. Manuf. Process. 
2024 ;125:566–579. doi: 10.1016/j.jmapro.2024.07.083
[155] Alharbi N. Electrical current-assisted low-plasticity burn -
ishing of inconel 718 built by laser powder bed fusion: 
surface integrity and fatigue life analysis. Arab. J. Sci. 
Eng. 2024 ;49(8):11381–11396. doi: 10.1007/s13369-023- 
08677-w
[156] Li C, Tian Y, Chen Y, et al. Hierarchical layered and 
refined grain structure of inconel 718 superalloy pro -
duced by rolling-assisted directed energy deposition, 
addit. Manuf. Lett. 2021 ;1:100009. doi: 10.1016/j.addlet. 
2021.100009
[157] Li C, Hodgson P, Preuss M, et al. Rolling-assisted direct 
energy deposited inconel 718: microstructural evolution 
and mechanical properties after optimized heat treat -
ment. J. Mater. Sci. Technol. 2023 ;144:118–127. doi: 10. 
1016/j.jmst.2022.10.021
[158] Raj R, Chiu LN, Marla D, et al. Understanding the 
dynamics of in-situ micro-rolling in directed energy 
deposition using thermo-mechanical finite-element 
analyses. Finite Elem. Anal. Des. 2024 ;238:104194. 
doi: 10.1016/j.finel.2024.104194
[159] Raj R, Chiu LNS, Marla D, et al. Development and vali -
dation of a fully coupled thermo-mechanical model for 
in-situ micro-rolling in laser-directed energy deposition: 
single-track multi-layer case. Mater. Des. 
2024 ;245:113210. doi: 10.1016/j.matdes.2024.113210
[160] Zhao X, Wang Y, Wang G, et al. Effect of process par -
ameters on stress and strain of hybrid deposition and 
micro-rolling. Rapid Prototyping J. 2022 ;28:490–504. 
doi: 10.1108/RPJ-01-2021-0012
[161] Zhang T, Li H, Gong H, et al. Study on location-related 
thermal cycles and microstructure variation of addi -
tively manufactured inconel 718. J. Mater. Res. 
Technol-JMRT. 2022 ;18:3056–3072. doi: 10.1016/j.jmrt. 
2022.03.178
[162] Hönnige J, Seow CE, Ganguly S, et al. Study of residual 
stress and microstructural evolution in as-deposited 
and inter-pass rolled wire plus arc additively manufac -
tured inconel 718 alloy after ageing treatment. Mater 
Sci Eng A. 2021 ;801:140368. doi: 10.1016/j.msea.2020. 
140368
[163] Chen Q, Wang G, Zhang H, et al. Research on microstruc -
ture and mechanical properties of hybrid plasma arc and 
micro-rolling additive manufacturing of inconel 718 
superalloy. Rapid Prototyping J. 2022 ;28:1509–1519. 
doi: 10.1108/RPJ-09-2021-0227
[164] Zhao W, Zha G, Xi M, et al. Effects of synchronous rolling 
on microstructure, hardness, and wear resistance of 
laser multilayer cladding. J. Mater. Eng. Perform. 
2018 ;27:1746–1752. doi: 10.1007/s11665-018-3286-x
[165] Hua B, Yin J, Wang B, et al. Microstructure evolution and 
performance improvement of 42CrMo steel repaired by 
an ultrasonic rolling assisted laser directed energy depo -
sition IN718 superalloy. J. Alloy. Compd. 
2025 ;1026:180385. doi: 10.1016/j.jallcom.2025.180385
[166] Zhao J, Quan GZ, Zhang YQ, et al. A gradient strengthen -
ing method of wire-arc additive manufacturing coupling 
with surface rolling and its application. J Mater Process 
Technol. 2024 ;330:118473. doi: 10.1016/j.jmatprotec. 
2024.118473
[167] Qu G, Guo W, Shi J, et al. Improvement of gradient 
microstructure and properties of wire-arc directed 
energy deposition titanium alloy via laser shock 
peening. Mater Sci Eng A. 2024 ;918:147422. doi: 10. 
1016/j.msea.2024.147422
[168] Jin Z, Kong X, Ma L. Investigating the impact of substrate 
preheating on the thermal flow and microstructure of 
laser cladding of nickel-based superalloy. Materials 
(Basel) 2024 ;17(2):399. doi: 10.3390/ma17020399
[169] Gupta NK, Ganesan G, Siddhartha S, et al. In situ Pre- 
heating in wire Arc additive manufacturing: design, 
development, and experimental investigation on 
residual stresses and metallurgical and mechanical 
properties. J Mater Eng Perform. 2024 ;1–12. doi: 10. 
1007/s11665-024-10011-w
[170] Seidel A, Finaske T, Straubel A, et al. Additive manufac -
turing of powdery Ni-based superalloys Mar-M-247 
and CM 247 LC in hybrid laser metal deposition. 
VIRTUAL AND PHYSICAL PROTOTYPING 
 65

## Page 67

Metallurgical and Materials Transactions A. 
2018 ;49:3812–3830. doi: 10.1007/s11661-018-4777-y
[171] Chen Q, Zhao Y, Strayer S, et al. Elucidating the effect of 
preheating temperature on melt pool morphology vari -
ation in inconel 718 laser powder bed fusion via simu -
lation and experiment. Addit. Manuf. 2021 ;37:101642. 
doi: 10.1016/j.addma.2020.101642
[172] Caprio L, Demir AG, Chiari G, et al. Defect-free laser 
powder bed fusion of Ti–48Al–2Cr–2Nb with a high temp -
erature inductive preheating system. Journal of Physics: 
Photonics. 2020 ;2(2):024001. doi: 10.1088/2515-7647/ 
ab7080
[173] Li Y, Long H, Wei B, et al. Multiple preheating processes 
for suppressing liquefaction cracks in IN738LC superal -
loy fabricated by electron beam powder Bed fusion 
(EB-PBF). Materials (Basel). 2024 ;17:5667. doi: 10.3390/ 
ma17225667
[174] Chowdhury HT, Palleda TN, Kakuta N, et al. Effects of pre -
heating on thermal behavior in inconel 718 processed 
by additive manufacturing. Thermo. 2024 ;4:48–64. 
doi: 10.3390/thermo4010005
[175] Park J-H, Bang GB, Lee K-A, et al. Effect of preheating 
temperature on microstructural and mechanical proper -
ties of inconel 718 fabricated by selective laser melting. 
Met Mater Int. 2022 ;28:2836–2848. doi: 10.1007/s12540- 
022-01169-w
[176] Benchabane BY, Belkacemi Y, Belouchrani M, et al. 
Thermomechanical modelling of residual stresses and 
distortion in laser powder bed fusion: assessment of 
the effect of build plate preheating on the behaviour 
of inconel 718. Opt Laser Technol. 2025 ;181:111641. 
doi: 10.1016/j.optlastec.2024.111641
[177] Kim H, Lee KK, Ahn DG, et al. Effects of deposition strat -
egy and preheating temperature on thermo-mechanical 
characteristics of inconel 718 super-alloy deposited on 
AISI 1045 substrate using a DED process. Materials 
(Basel) 2021 ;14(7):1794. doi: 10.3390/ma14071794
[178] Liu Q, Fang L, Xiong Z, et al. The response of dislo -
cations, low angle grain boundaries and high angle 
grain boundaries at high strain rates. Mater Sci Eng A. 
2021 ;822:141704. doi: 10.1016/j.msea.2021.141704
[179] Dutta RK, Petrov RH, Delhez R, et al. The effect of tensile 
deformation by in situ ultrasonic treatment on the 
microstructure of low-carbon steel. Acta Mater. 
2013 ;61:1592–1602. doi: 10.1016/j.actamat.2012.11.036
[180] Park J-U, Jun S-Y, Lee BH, et al. Alloy design of Ni-based 
superalloy with high γ
′
volume fraction suitable for addi -
tive manufacturing and its deformation behavior. Addit. 
Manuf. 2022 ;52:102680. doi: 10.1016/j.addma.2022. 
102680
[181] Maly M, Nopova K, Klakurkova L, et al. Effect of preheating 
on the residual stress and material properties of inconel 
939 processed by laser powder Bed fusion. Materials 
(Basel) 2022 ;15(18):6360. doi: 10.3390/ma15186360
[182] Chen Y, Wang W, Ou Y, et al. Effect of high preheating on 
the microstructure and mechanical properties of high 
gamma prime Ni-based superalloy manufactured by 
laser powder bed fusion. J Alloys Compd. 
2023 ;960:170598. doi: 10.1016/j.jallcom.2023.170598
[183] Ying W, Han F, Wang J. Effects of preheating and cooling 
on the crack defects of laser solid formed rene 104 
superalloy parts, Proceedings of the Institution of 
Mechanical Engineers, Part B: Journal of Engineering 
Manufacture 2020 ;234:1087–1101. doi: 10.1177/ 
0954405420909182
[184] Nowotny S, Brueckner F, Thieme S, et al. High-perform -
ance laser cladding with combined energy sources. J 
Laser Appl. 2015 ;27(1):S17001. doi: 10.2351/1.4817455
[185] Wu K, Aprilia A, Tan SC, et al. Rapid post processing 
of cold sprayed inconel 625 by induction heating. 
Mater Sci Eng A. 2023 ;872;144955. doi: 10.1016/j.msea. 
2023.144955
[186] Wang Y, Choi J, Mazumder J. Laser-Aided direct 
writing of nickel-based single-crystal super alloy (N5). 
Metallurgical and Materials Transactions A. 
2016 ;47:5685–5690. doi: 10.1007/s11661-016-3755-5
[187] Huang Y, Zeng X. Investigation on cracking behavior of 
Ni-based coating by laser-induction hybrid cladding. 
Appl Surf Sci. 2010 ;256:5985–5992. doi: 10.1016/j. 
apsusc.2010.03.106
[188] Hascoët J-Y, Parrot J, Mognol P, et al. Induction heating 
in a wire additive manufacturing approach. Weld World. 
2017 ;62:249–257. doi: 10.1007/s40194-017-0533-y
[189] Bai X, Zhang H, Wang G. Modeling of the moving induc -
tion heating used as secondary heat source in weld- 
based additive manufacturing. The International 
Journal of Advanced Manufacturing Technology. 
2014 ;77:717–727. doi: 10.1007/s00170-014-6475-2
[190] Zhao P, Gao J, Wang Y, et al. Hybrid heat source 
model for coaxial follow-up induction heating-assisted 
laser direct energy deposition. Materials Today 
Communications. 2025 ;42:111482. doi: 10.1016/j. 
mtcomm.2024.111482
[191] Oskolkov AA, Bezukladnikov DNT. Application of induc -
tion heating in the FDM/FFF 3D manufacturing. J Phys: 
Conf Ser. 2020 ;1730(1):012005. doi: 10.1088/1742-6596/ 
1730/1/012005
[192] Li S, Chen L, Zhu L, et al. Comparative research on the 
microstructure and mechanical properties of traditional 
and induction heating aided extreme-high-speed laser 
cladding of Ni60 coatings. Appl Phys A. 
2024 ;130(3):159. doi: 10.1007/s00339-024-07299-9
[193] Hu YL, Lin X, Song K, et al. Effect of heat input on crack -
ing in laser solid formed DZ4125 superalloy. Opt Laser 
Technol. 2016 ;86:1–7. doi: 10.1016/j.optlastec.2016.06.008
[194] Xu J, Lin X, Guo P, et al. The effect of preheating on 
microstructure and mechanical properties of laser solid 
forming IN-738LC alloy. Mater Sci Eng A. 2017 ;691:71– 
80. doi: 10.1016/j.msea.2017.03.046
[195] Xu J, Lin X, Guo P, et al. The microstructure evolution 
and strengthening mechanism of a γ
′
-strengthening 
superalloy prepared by induction-assisted laser solid 
forming. J Alloys Compd. 2019 ;780:461–475. doi: 10. 
1016/j.jallcom.2018.11.386
[196] Bidron G, Doghri A, Malot T, et al. Reduction of the hot 
cracking sensitivity of CM-247LC superalloy processed 
by laser cladding using induction preheating. J Mater 
Process Technol. 2020 ;277:116461. doi: 10.1016/j. 
jmatprotec.2019.116461
[197] Liu S, Liu C, Gao X, et al. Insights into process optimiz -
ation and induction preheating for crack-free laser 
metal deposition of nickel-based superalloy K417G. J 
Mater Res Technol. 2024 ;29:2035–2050. doi: 10.1016/j. 
jmrt.2024.01.266
66 
 J. JANG ET AL.

## Page 68

[198] Xu J, Lin X, Guo P, et al. The initiation and propagation 
mechanism of the overlapping zone cracking during 
laser solid forming of IN-738LC superalloy. J Alloys 
Compd. 2018 ;749:859–870. doi: 10.1016/j.jallcom.2018. 
03.366
[199] Liu S, Liu C, Yuan C. Effect of laser energy density and 
scanning strategy on residual stress in laser melting 
deposited FGH4096 superalloy. J Mater Eng Perform. 
2024 ;33:4029–4038. doi: 10.1007/s11665-024-09152-9
[200] Meng W, Zhang W, Zhang W, et al. Fabrication of steel- 
inconel functionally graded materials by laser melting 
deposition integrating with laser synchronous preheat -
ing. Opt Laser Technol. 2020 ;131:106451. doi: 10.1016/j. 
optlastec.2020.106451
[201] Soffel F, Papis K, Bambach M, et al. Laser preheating for 
Hot crack reduction in direct metal deposition of inconel 
738LC. Metals (Basel). 2022 ;12(4):614. doi: 10.3390/ 
met12040614
[202] Dezaki M L, Serjouei A, Zolfagharian A, et al. A review on 
additive/subtractive hybrid manufacturing of directed 
energy deposition (DED) process. Advanced Powder 
Materials. 2022 ;1:100054. doi: 10.1016/j.apmate.2022. 
100054
[203] Zhang H, Wang Y, Wang Z, et al. Enhancing microstruc -
tural control, tribological and electrochemical perform -
ances of laser powder bed fusion processed nickel 
superalloys through in-situ remelting. J Alloys Compd. 
2024 ;980:173608. doi: 10.1016/j.jallcom.2024.173608
[204] Borisov EV, Popovich VA, Popovich AA, et al. Selective 
laser melting of inconel 718 under high laser power. 
Mater Today Proc. 2020 ;30:784–788. doi: 10.1016/j. 
matpr.2020.01.571
[205] Zhang D, Liu W, Li Y, et al. In situ observation of crystal 
rotation in Ni-based superalloy during additive manu -
facturing process. Nat Commun. 2023 ;14:2961. doi: 10. 
1038/s41467-023-38727-8
[206] Ledwig P, Pasiowiec H, Cichocki K, et al. Tailoring micro -
structure and mechanical properties of additively manu -
factured inconel 625 by remelting strategy in laser 
powder Bed fusion. Metallurgical and Materials 
Transactions A. 2024 ;55:2485–2508. doi: 10.1007/ 
s11661-024-07412-w
[207] Koike R, Misawa T, Aoyama T, et al. Controlling metal 
structure with remelting process in direct energy depo -
sition of inconel 625. CIRP Ann. 2018 ;67:237–240. doi: 10. 
1016/j.cirp.2018.04.061
[208] Zhao R, Li L, Nie Z, et al. Effects of pre-heating induced 
interfacial diffusion on microstructure and related 
mechanical properties of direct laser metal deposited 
inconel 625 superalloy on a Cu-Cr-Zr substrate. Mater 
Sci Eng A. 2025 ;920:147551. doi: 10.1016/j.msea.2024. 
147551
[209] Meng W, Zhang W, Zhang W, et al. Additive fabrication of 
316L/Inconel625/Ti6Al4V functionally graded materials 
by laser synchronous preheating. The International 
Journal of Advanced Manufacturing Technology. 
2019 ;104:2525–2538. doi: 10.1007/s00170-019-04061-x
[210] Meng W, Xiaohui Y, Zhang W, et al. Additive manufactur -
ing of a functionally graded material from Inconel625 to 
Ti6Al4V by laser synchronous preheating. J Mater 
Process Technol. 2020 ;275:116368. doi: 10.1016/j. 
jmatprotec.2019.116368
[211] Lee H-J, Kim H-K, Hong H-U, et al. Influence of the focus 
offset on the defects, microstructure, and mechanical 
properties of an inconel 718 superalloy fabricated by 
electron beam additive manufacturing. J Alloys Compd. 
2019 ;781:842–856. doi: 10.1016/j.jallcom.2018.12.070
[212] Abdelwahed M, Puchades JRB, Griñán LP, et al. Cracking 
mechanisms and effect of extensive preheating in 
CM247LC and IN713LC Ni-base superalloy processed 
by laser powder Bed fusion. Materials Today 
Communications. 2023 ;37:107644. doi: 10.1016/j. 
mtcomm.2023.107644
[213] Song W, Yang J, Liang J, et al. A new approach to design 
advanced superalloys for additive manufacturing. 
Additive Manufacturing. 2024 ;84:104098. doi: 10.1016/j. 
addma.2024.104098
[214] Liu L, Wang D, Deng G, et al. Crack inhibition and mech -
anical property enhancement of a CM247LC alloy fabri -
cated by laser powder bed fusion through remelting 
strategy. Mater Charact. 2024 ;214:114073. doi: 10.1016/ 
j.matchar.2024.114073
[215] Li L, Dong T, Jiang F, et al. A novel method enhanced mech -
anical properties of a selective laser melted Mar-M247 
superalloy by progressive remelting. J Mater Res Technol. 
2024 ;33:4968–4980. doi: 10.1016/j.jmrt.2024.10.182
[216] Lim B, Chen H, Chen Z, et al. Microstructure-property 
gradients in Ni-based superalloy (inconel 738) additively 
manufactured via electron beam powder bed fusion. 
Addit. Manuf. 2021 ;46:102121. doi: 10.1016/j.addma. 
2021.102121
[217] Li Y, Yu Y-F, Wang Z-B, et al. Additive manufacturing of 
nickel-based superalloy single crystals with IN-738 alloy. 
Acta Metallurgica Sinica (English Letters) 
2022 ;35(3):369–374. doi: 10.1007/s40195-021-01320-3
[218] Goel S, Ahlfors M, Bahbou F, et al. Effect of different 
post-treatments on the microstructure of EBM-built 
alloy 718. J Mater Eng Perform. 2019 ;28:673–680. 
doi: 10.1007/s11665-018-3712-0
[219] Rezaei A, Kermanpur A, Rezaeian A, et al. Contribution of 
hot isostatic pressing on densification, microstructure 
evolution, and mechanical anisotropy of additively man -
ufactured IN718 Ni-based superalloy. Mater Sci Eng A. 
2021 ;823:141721. doi: 10.1016/j.msea.2021.141721
[220] Murr LE, Martinez E, Gaytan S, et al. Microstructural 
architecture, microstructures, and mechanical proper -
ties for a nickel-base superalloy fabricated by electron 
beam melting. Metallurgical and Materials Transactions 
A. 2011 ;42:3491–3508. doi: 10.1007/s11661-011-0748-2
[221] Jiang R, Mostafaei A, Pauza J, et al. Varied heat treat -
ments and properties of laser powder bed printed 
inconel 718. Mater Sci Eng A. 2019 ;755:170–180. 
doi: 10.1016/j.msea.2019.03.103
[222] Goel S, Sittiho A, Charit I, et al. Effect of post-treatments 
under hot isostatic pressure on microstructural charac -
teristics of EBM-built alloy 718. Addit. Manuf. 
2019 ;28:727–737. doi: 10.1016/j.addma.2019.06.002
[223] Popovich V, Borisov E, Popovich A, et al. Impact of heat 
treatment on mechanical behaviour of inconel 718 pro -
cessed with tailored microstructure by selective laser 
melting. Mater Des. 2017 ;131:12–22. doi: 10.1016/j. 
matdes.2017.05.065
[224] Balachandramurthi AR, Moverare J, Dixit N, et al. 
Influence of defects and as-built surface roughness on 
VIRTUAL AND PHYSICAL PROTOTYPING 
 67

## Page 69

fatigue properties of additively manufactured alloy 718. 
Mater Sci Eng A. 2018 ;735:463–474. doi: 10.1016/j.msea. 
2018.08.072
[225] Tillmann W, Schaak C, Nellesen J, et al. Hot isostatic 
pressing of IN718 components manufactured by selec -
tive laser melting. Addit. Manuf. 2017 ;13:93–102. 
doi: 10.1016/j.addma.2016.11.006
[226] Moussaoui K, Rubio W, Mousseigne M, et al. Effects of 
selective laser melting additive manufacturing par -
ameters of inconel 718 on porosity, microstructure 
and mechanical properties. Mater Sci Eng A. 
2018 ;735:182–190. doi: 10.1016/j.msea.2018.08.037
[227] Poulin J-R, Kreitcberg A, Brailovski V. Effect of hot iso -
static pressing of laser powder bed fused inconel 625 
with purposely induced defects on the residual porosity 
and fatigue crack propagation behavior. Addit. Manuf. 
2021 ;47:102324. doi: 10.1016/j.addma.2021.102324
[228] Ghorbanpour S, Alam ME, Ferreri NC, et al. Experimental 
characterization and crystal plasticity modeling of aniso -
tropy, tension-compression asymmetry, and texture 
evolution of additively manufactured inconel 718 at 
room and elevated temperatures. Int J Plast. 
2020 ;125:63–79. doi: 10.1016/j.ijplas.2019.09.002
[229] Xu J, Ma T, Peng RL, et al. Effect of post-processes on the 
microstructure and mechanical properties of laser 
powder bed fused IN718 superalloy. Addit. Manuf. 
2021 ;48:102416. doi: 10.1016/j.addma.2021.102416
[230] Schneider J, Lund B, Fullen M. Effect of heat treatment 
variations on the mechanical properties of inconel 718 
selective laser melted specimens. Addit. Manuf. 
2018 ;21:248–254. doi: 10.1016/j.addma.2018.03.005
[231] Gribbin S, Ghorbanpour S, Ferreri NC, et al. Role of grain 
structure, grain boundaries, crystallographic texture, 
precipitates, and porosity on fatigue behavior of 
inconel 718 at room and elevated temperatures. Mater 
Charact. 2019 ;149:184–197. doi: 10.1016/j.matchar.2019. 
01.028
[232] Schröder J, Mishurova T, Fritsch T, et al. On the influence 
of heat treatment on microstructure and mechanical 
behavior of laser powder bed fused inconel 718. Mater 
Sci Eng A. 2021 ;805:140555. doi: 10.1016/j.msea.2020. 
140555
[233] Hazeli K, Babamiri BB, Indeck J, et al. Microstructure-top -
ology relationship effects on the quasi-static and 
dynamic behavior of additively manufactured lattice 
structures. Mater Des. 2019 ;176:107826. doi: 10.1016/j. 
matdes.2019.107826
[234] Goel S, Mehtani H, Yao S-W, et al. As-built and post- 
treated microstructures of an electron beam melting 
(EBM) produced nickel-based superalloy. Metallurgical 
and Materials Transactions A. 2020 ;51:6546–6559. 
doi: 10.1007/s11661-020-06037-z
[235] Nandwana P, Kirka M, Okello A, et al. Electron beam 
melting of inconel 718: effects of processing and post- 
processing. Mater Sci Technol. 2018 ;34:612–619. 
doi: 10.1080/02670836.2018.1424379
[236] Gundgire T, Goel S, Klement U, et al. Response of 
different electron beam melting produced alloy 718 
microstructures to thermal post-treatments. Mater 
Charact. 2020 ;167:110498. doi: 10.1016/j.matchar.2020. 
110498
[237] Sadeghi E, Karimi P, Momeni S, et al. Influence of thermal 
post treatments on microstructure and oxidation behav -
ior of EB-PBF manufactured alloy 718. Mater Charact. 
2019 ;150:236–251. doi: 10.1016/j.matchar.2019.02.016
[238] Kirka MM, Medina F, Dehoff R, et al. Mechanical behavior 
of post-processed inconel 718 manufactured through 
the electron beam melting process. Mater Sci Eng A. 
2017 ;680:338–346. doi: 10.1016/j.msea.2016.10.069
[239] Balachandramurthi AR, Moverare J, Mahade S, et al. 
Additive manufacturing of alloy 718 via electron beam 
melting: effect of post-treatment on the microstructure 
and the mechanical properties. Materials (Basel). 
2018 ;12:68. doi: 10.3390/ma12010068
[240] Goel S, Zaninelli E, Gundgire T, et al. Microstructure evol -
ution and mechanical response-based shortening of 
thermal post-treatment for electron beam melting 
(EBM) produced alloy 718. Mater Sci Eng A. 
2021 ;820:141515. doi: 10.1016/j.msea.2021.141515
[241] Goel S, Zaninelli E, Gårdstam J, et al. Microstructure evol -
ution-based design of thermal post-treatments for EBM- 
built alloy 718. J Mater Sci. 2021 ;56:5250–5268. doi: 10. 
1007/s10853-020-05595-2
[242] Ghorpade A, Prakash U, Joshi S. Effect of heat treatments 
on strengthening mechanisms in electron beam melted 
superalloy inconel 718. Mater Sci Eng A. 
2024 ;895:146232. doi: 10.1016/j.msea.2024.146232
[243] Poulin J-R, Brailovski V, Terriault P. Long fatigue crack 
propagation behavior of inconel 625 processed by 
laser powder bed fusion: influence of build orientation 
and post-processing conditions. Int J Fatigue. 
2018 ;116:634–647. doi: 10.1016/j.ijfatigue.2018.07.008
[244] Kreitcberg A, Brailovski V, Turenne S. Effect of heat treat -
ment and hot isostatic pressing on the microstructure 
and mechanical properties of inconel 625 alloy pro -
cessed by laser powder bed fusion. Mater Sci Eng A. 
2017 ;689:1–10. doi: 10.1016/j.msea.2017.02.038
[245] Yang J, Li F, Wang Z, et al. Cracking behavior and control 
of rene 104 superalloy produced by direct laser fabrica -
tion. J Mater Process Technol. 2015 ;225:229–239. doi: 10. 
1016/j.jmatprotec.2015.06.002
[246] Peng H, Shi Y, Gong S, et al. Microstructure, mechanical 
properties and cracking behaviour in a γ
′
-precipitation 
strengthened nickel-base superalloy fabricated by elec -
tron beam melting. Mater Des. 2018 ;159:155–169. 
doi: 10.1016/j.matdes.2018.08.054
[247] Lee J-U, Kim Y-K, Seo S-M, et al. Effects of hot isostatic 
pressing treatment on the microstructure and tensile 
properties of Ni-based superalloy CM247LC manufac -
tured by selective laser melting. Mater Sci Eng A. 
2022 ;841:143083. doi: 10.1016/j.msea.2022.143083
[248] Koo J, Kim JE, Auyeskhan U, et al. Influence of Hot iso -
static pressing on different crack modes of laser 
powder Bed fusion-processed CM247LC: alternative 
process parameters considering post-processing. Int J 
Prec Eng Manuf. 2024 ;26:513–525. doi: 10.1007/s12541- 
024-01124-2
[249] Vilanova M, Garciandia F, Sainz S, et al. The limit of hot 
isostatic pressing for healing cracks present in an addi -
tively manufactured nickel superalloy. J Mater Process 
Technol. 2022 ;300:117398. doi: 10.1016/j.jmatprotec. 
2021.117398
68 
 J. JANG ET AL.

## Page 70

[250] Rickenbacher L, Etter T, Hövel S, et al. High temperature 
material properties of IN738LC processed by selective 
laser melting (SLM) technology. Rapid Prototyp J. 
2013 ;19:282–290. doi: 10.1108/13552541311323281
[251] Wang H, Zhang X, Wang G, et al. Selective laser melting 
of the hard-to-weld IN738LC superalloy: efforts to miti -
gate defects and the resultant microstructural and 
mechanical properties. J Alloys Compd. 
2019 ;807:151662. doi: 10.1016/j.jallcom.2019.151662
[252] Li Y, Liang X, Peng G, et al. Effect of heat treatments on 
the microstructure and mechanical properties of 
IN738LC prepared by electron beam powder bed 
fusion. J Alloys Compd. 2022 ;918:165807. doi: 10.1016/j. 
jallcom.2022.165807
[253] Xu J, Ding Y, Gao Y, et al. Improving high-temperature 
mechanical properties of laser powder bed-fused 
inconel 738 alloy by hot isostatic pressing: tailoring pre -
cipitates and healing defects. Mater Sci Eng A. 
2023 ;862:144285. doi: 10.1016/j.msea.2022.144285
[254] Zhou W, Tian Y, Wei D, et al. Effects of heat treatments 
on the microstructure and tensile properties of IN738 
superalloy with high carbon content fabricated via 
laser powder bed fusion. J Alloys Compd. 
2023 ;953:170110. doi: 10.1016/j.jallcom.2023.170110
[255] Lopez-Galilea I, Ruttert B, He J, et al. Additive manufac -
turing of CMSX-4 Ni-base superalloy by selective laser 
melting: influence of processing parameters and heat 
treatment. Addit. Manuf. 2019 ;30:100874. doi: 10.1016/j. 
addma.2019.100874
[256] Ruttert B, Ramsperger M, Roncery LM, et al. Impact of 
hot isostatic pressing on microstructures of CMSX-4 
Ni-base superalloy fabricated by selective electron 
beam melting. Mater Des. 2016 ;110:720–727. doi: 10. 
1016/j.matdes.2016.08.041
[257] Zhang T, Li H, Gong H, et al. Hybrid wire-arc additive 
manufacture and effect of rolling process on microstruc -
ture and tensile properties of inconel 718. J. Mater. 
Process. Technol. 2022 ;299:117361. doi: 10.1016/j. 
jmatprotec.2021.117361
[258] Zhang T, Li H, Gong H, et al. Comparative analysis of 
cold and warm rolling on tensile properties and micro -
structure of additive manufactured inconel 718. Arch. 
Civ. Mech. Eng. 2022 ;22:1–14. doi: 10.1007/s43452-021- 
00356-7
[259] Kluczyński J, Śnieżek L, Grzelak K, et al. Hot isostatic 
pressing influence on the mechanical properties of 
selectively laser-melted 316L steel. Bulletin of the 
Polish Academy of Sciences Technical Sciences. 
2020 ;68:1413–1424. doi: 10.24425/bpasts.2020.135396
[260] Hirata T, Kimura T, Nakamoto T. Effects of hot isostatic 
pressing and internal porosity on the performance of 
selective laser melted AlSi10Mg alloys. Mater Sci Eng 
A. 2020 ;772:138713. doi: 10.1016/j.msea.2019.138713
[261] Gheysen J, Tingaud D, Villanova J, et al. Exceptional 
fatigue life and ductility of new liquid healing hot iso -
static pressing especially tailored for additive manufac -
tured aluminum alloys. Scr Mater. 2023 ;233:115512. 
doi: 10.1016/j.scriptamat.2023.115512
[262] Molaei R, Fatemi A, Phan N. Significance of hot isostatic 
pressing (HIP) on multiaxial deformation and fatigue 
behaviors of additive manufactured Ti-6Al-4V including 
build orientation and surface roughness effects. Int J 
Fatigue. 2018 ;117:352–370. doi: 10.1016/j.ijfatigue.2018. 
07.035
[263] Xu H, Zhang Q, Tian T, et al. In-situ hot rolling directed 
energy deposition-arc repair of shafts. Addit. Manuf. 
2023 ;61:103362. doi: 10.1016/j.addma.2022.103362
[264] McAndrew AR, Alvarez Rosales M, Colegrove PA, et al. 
Interpass rolling of Ti-6Al-4V wire + arc additively manufac -
tured features for microstructural refinement. Addit. 
Manuf. 2018 ;21:340–349. doi: 10.1016/j.addma.2018.03. 
006
[265] Tian WP, Zhang ZY, Jin ZQ, et al. Influence of substrate 
pre-heating on microstructural homogeneity in wire- 
arc additively manufactured super martensitic stainless 
steel. Mater Charact. 2025 ;222:114868. doi: 10.1016/j. 
matchar.2025.114868
[266] Tariq U, Wu SH, Mahmood MA, et al. Effect of Pre- 
heating on residual stresses and deformation in laser- 
based directed energy deposition repair: A comparative 
analysis. Materials (Basel) 2024 ;17:2179. doi: 10.3390/ 
ma17102179
[267] Soyama H, Takeo F. Effect of various peening methods 
on the fatigue properties of titanium alloy Ti6Al4V man -
ufactured by direct metal laser sintering and electron 
beam melting. Materials (Basel) 2020 ;13:2216. doi: 10. 
3390/ma13102216
[268] Uzan NE, Ramati S, Shneck R, et al. On the effect of shot- 
peening on fatigue resistance of AlSi10Mg specimens 
fabricated by additive manufacturing using selective 
laser melting (AM-SLM). Addit. Manuf. 2018 ;21:458– 
464. doi: 10.1016/j.addma.2018.03.030
[269] Zhang X, Huang S, Li D, et al. An approach to 
improve the microstructure and mechanical 
properties: A hybrid manufacturing of laser 
directed energy deposition and shot peening. 
Addit. Manuf. 2022 ;55:102686. doi: 10.1016/j.addma. 
2022.102686
VIRTUAL AND PHYSICAL PROTOTYPING 
 69
