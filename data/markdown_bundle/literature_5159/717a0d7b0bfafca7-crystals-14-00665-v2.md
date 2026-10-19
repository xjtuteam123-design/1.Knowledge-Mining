# crystals-14-00665-v2

<!-- source: D:\总文献\crystals-14-00665-v2.pdf -->
<!-- file_sha256: 1350a4e9eb16dbe62e2411e1a634b37531e915ad43d30bd9f3ba0298c373f418 -->

## Page 1

Citation: Zarinejad, M.; Tong, Y.;
Salehi, M.; Mu, C.; Wang, N.; Xu, Y.;
Rimaz, S.; Tian, L.; Kuah, K.X.; Chen,
X. Advancements and Perspectives in
Additive Manufacturing of Tungsten
Alloys and Composites: Challenges
and Solutions. Crystals 2024, 14, 665.
https://doi.org/10.3390/
cryst14070665
Academic Editor: Umberto Prisco
Received: 4 June 2024
Revised: 15 July 2024
Accepted: 17 July 2024
Published: 20 July 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
crystals
Review
Advancements and Perspectives in Additive Manufacturing of
T ungsten Alloys and Composites: Challenges and Solutions
Mehrdad Zarinejad 1,2, *
 , Yunxiang Tong3,*, Mojtaba Salehi 4,*
 , Chengfa Mu 1, Nian Wang 2, Yonglong Xu 2,
Sajjad Rimaz 5, Lintao Tian 1, Kai Xiang Kuah 6 and Xiaotong Chen 1
1 Research and Development Institute, Wenzhou Hongfeng Electrical Alloy Co., Ltd., No. 5600, Oujin Avenue,
Oujiangkou Industry Cluster, Wenzhou 325700, China; muchengfa@wzhf.com (C.M.);
tianlintao@wzhf.com (L.T.); chenxiaotong@wzhf.com (X.C.)
2 Wenzhou Hongfeng Alloy Co., Ltd., No. 1633, Binhai First Avenue, Wenzhou Economic and Technology
Development Zone, Wenzhou 325603, China; wangnian@wzhf.com (N.W.); xuyonglong@wzhf.com (Y.X.)
3 Institute of Materials Processing and Intelligent Manufacturing, College of Materials Science
and Chemical Engineering, Harbin Engineering University, Harbin 150001, China
4 Additive Manufacturing Division, Singapore Institute of Manufacturing Technology (SIMTech),
Agency for Science, Technology and Research (A*STAR), 5 Cleantech Loop, Singapore 636732, Singapore
5 Department of Chemical and Bimolecular Engineering, National University of Singapore,
4 Engineering Drive 4, Singapore 117585, Singapore
6 Department of Materials Science and Engineering, National University of Singapore, 9 Engineering Drive 1,
Singapore 117575, Singapore; kxkuah@u.nus.edu
* Correspondence: mehrdad@wzhf.com (M.Z.); tongyx@hrbeu.edu.cn (Y.T.);
mojtaba_salehi@simtech.a-star.edu.sg (M.S.)
Abstract: This review explores additive manufacturing (AM) for refractory tungsten (W) and its
alloys, highlighting the primary challenges and determining factors in the AM of pure W, W alloys
and composites. The challenges mainly arise from W’s high melting point, low laser absorptivity,
high thermal conductivity, high melt viscosity, high oxygen affinity, high ductile-to-brittle transition
temperature, and inherent embrittlement, which lead to defects and anomalies in AM-produced
parts. This review focuses on both processes and alloying strategies to address the issues related
to densification, micro-cracking, and the resultant properties in W-based components. Cracking in
additively manufactured W remains a persistent issue due to thermal stress, embrittlement, and
oxide formation. Powder characteristics, process parameters, and thermal management strategies are
crucial for W densification. Throughout the review, existing knowledge and insights are organized
into comprehensive tables, serving as valuable resources for researchers delving deeper into this
topic. Future research in W-AM should focus on understanding the interaction between AM process
parameters and microstructural and material design. Advances in atomic-level understanding,
thermodynamic modeling, and data analytics have the potential to significantly enhance the precision,
sustainability, and applicability of W-AM.
Keywords: refractory alloys; tungsten alloys and composites; additive manufacturing; laser and
electron beam melting; challenges and mitigation strategies
1. Introduction
Refractory alloys, including tungsten (W) and its alloys, are integral to aerospace and
energy-generation industries [1]. W is well known for its high melting point (approximately
3422 ◦C), good mechanical properties, and low thermal expansion coefficient of less than
4 µm/m·K [2]. Additionally, its impressive thermal conductivity, surpassing 150 W/m·K [2],
exceptional resistance to heat and wear [ 3], notable chemical stability, and remarkable
hardness [3] make W suitable for high-temperature and radiation-resilient applications.
Examples of its applications include collimators, heat sinks [ 4], integrated circuits [5,6],
switch contacts [7], rocket nozzles [5,8], turbine blades [5], and nuclear reactor parts [5,9].
Crystals 2024, 14, 665. https://doi.org/10.3390/cryst14070665 https://www.mdpi.com/journal/crystals

## Page 2

Crystals 2024, 14, 665 2 of 40
Harnessing the full potential of refractory alloys, particularly those of W-based materi-
als, has been challenging owing to their high melting points and complex metallurgical
behavior [10].
Conventional production methods for W-based alloys primarily rely on powder met-
allurgy techniques, which require high-temperature sintering. Achieving full densification
is particularly challenging. Additionally, the hardness and brittleness of W alloys compli-
cate formative and subtractive manufacturing processes, such as forming and machining
methods. Furthermore, W oxidizes at relatively low temperatures (beginning around
400–500 ◦C), which increases the complexity and cost of manufacturing. Historically, the
manufacturability of W-based alloys has been hindered by high costs, scalability issues,
and challenges in producing intricate structures [ 11]. Additive manufacturing (AM) of
refractory alloys offers unparalleled design freedom. Unlike traditional subtractive tech-
niques that can waste up to 70% of material [12–14], AM’s layer-by-layer approach ensures
material efficiency, especially with costly refractory alloys [15,16].
AM could address some of the traditional challenges associated with the production
of W-based alloys and provide significant advantages in terms of design flexibility, material
efficiency, and the capability to create complex geometries. For instance, AM facilitates
the production of intricate and custom molds for high-temperature tooling. As another
example, AM allows for the creation of sophisticated channels and intricate geometries,
enhancing the cooling efficiency of plasma-facing components in nuclear fusion reactors.
Although W-AM can mitigate many of the issues associated with traditional techniques,
the inherent properties of W alloys present significant challenges for AM processes. The
high melting points and elevated ductile-to-brittle transition temperatures (DBTTs) pose
concerns for all refractory alloys but are amplified for W because of its high viscosity
(8 × 10−3 Pa·s) [17], surface tension (2.361 N/m) [17], and rapid solidification rate [18]. In
the solid state, W’s body-centered cubic structure adds complexity to thermal processes,
particularly given its DBTT [ 19,20] and the notable influence of impurities on its DBTT.
Issues such as interstitial contamination, balling [ 21], cracking [22], and the limited un-
derstanding of process-structure-property relationships [ 18,21,23] represent substantial
hurdles to overcome.
Over the past decade, extensive research has been undertaken on the AM of unal-
loyed and alloyed W, as well as W-matrix composites [24,25]. Most studies on unalloyed
W have utilized Powder Bed Fusion (PBF) processes, namely, Selective Laser Melting
(SLM) [8,17–19,21,24,26–61], and Electron Beam Melting (EBM) [33,34,47,59–69] of W. Other
notable methods employed include Direct Energy Deposition (DED) processes, namely
laser-based DED [2,34,47,59–61,70–77] and electric arc-based DED [78,79], and binder jet-
ting (BJ) which shows promise for W-based materials [80–84]. Other novel methods such
as ultrashort-time liquid phase sintering (LPS) [85], and bound metal deposition (BMD)
have also been introduced [86].
In most AM processes, W materials initially melt, and then solidify, leading to nu-
cleation and subsequent grain growth. This thermal history contrasts with traditional
processing techniques like sintering, which primarily deal with powder densification
followed by sintering and grain growth. Post-solidification grain growth in AM shares
similarities with sintering and is guided by kinetic laws [60,87]. However, in AM of nano-W,
surface diffusion prevails [60,88], unlike traditional sintering’s grain boundary diffusion.
Recognizing these differences and understanding the influence of process parameters
and alloy chemistry on molten pool behavior, solidification, and further solid-state mi-
crostructural evolution and strengthening effects are essential for advancing the field of
W-AM [24,60,74,89–91].
Building on the foundation of previous review articles on W-AM [58,60,61], our review
delves deeper into understanding process parameters’ design and recent advancements in
materials design strategies aimed at mitigating W-AM challenges. We begin by providing
an overview of the current status of AM techniques for W alloys, focusing on the PBF, DED,
and BJ processes. We will then look at the challenges that are often associated with their AM

## Page 3

Crystals 2024, 14, 665 3 of 40
processes, such as densification, microcracking, and limited material properties, followed
by mitigation strategies that researchers have developed from both design and material
perspectives to address these issues. Finally, our review concludes with an exploration
of promising future directions for W-AM, aimed at paving the way for broader adoption
and commercialization.
2. Techniques for Additive Manufacturing of W-Based Materials
W and W-based metal systems demand substantial energy input during AM. With
technological advancements, AM systems have been equipped with high-energy sources
like lasers and electrons to provide the energy required. Table 1 provides a brief comparison
of process parameters and relative densities achieved via different AM techniques for W-
based materials (pure, alloys, and composites). Figure 1 depicts the schematic setups of
these methods [92–96]. The choice of an AM method for W materials depends on several
factors including the material type, post-processing needs, geometric accuracy, cost, surface
finish, and property requirements [33,61].
Crystals 2024, 14, 665 3 of 44 
 
 
providing an overview of the current status of AM techniques for W alloys, focusing on 
the PBF, DED, and BJ processes. We will then look at the challenges that are often associ-
ated with their AM processes, such as densification, microcracking, and limited material 
properties, followed by mitigation strategies that researchers have developed from both 
design and material perspectiv es to address these issues. Finally, our review concludes 
with an exploration of promising future directions for W-AM, aimed at paving the way 
for broader adoption and commercialization. 
2. Techniques for Additive Manufacturing of W-Based Materials 
W and W-based metal systems demand substantial energy input during AM. With 
technological advancements, AM systems have been equipped with high-energy sources 
like lasers and electrons to provide the energy required. Table 1 provides a brief compar-
ison of process parameters and relative dens ities achieved via different AM techniques 
for W-based materials (pure, alloys, and comp osites). Figure 1 depicts the schematic set-
ups of these methods [92–96]. The choice of an AM method for W materials depends on 
several factors including the material type, post-processing needs, geometric accuracy, 
cost, surface finish, and property requirements [33,61]. 
 
Figure 1. Schematic setups of AM techniques used in W materials fabrication: (a) SLM [92], (b) EBM 
[94], (c) laser-based DED [93], and (d) BJ [96]. 
SLM (Figure 1a) has been exte nsively studied for fabricating W and its alloys [97]. 
Crack forming, especially at grain boundaries, is a major issue in SLM-produced W parts. 
This happens because of factors such as rapid cooling creating thermal stresses exceeding 
DBTT, and oxygen trapped at the boundaries during the coalescence of the particles 
Figure 1. Schematic setups of AM techniques used in W materials fabrication: ( a) SLM [ 92],
(b) EBM [94], (c) laser-based DED [93], and (d) BJ [96].
SLM (Figure 1a) has been extensively studied for fabricating W and its alloys [97]. Crack
forming, especially at grain boundaries, is a major issue in SLM-produced W parts. This hap-
pens because of factors such as rapid cooling creating thermal stresses exceeding DBTT, and
oxygen trapped at the boundaries during the coalescence of the particles[19,29,63]. Neverthe-
less, SLM-fabricated W materials can achieve relative densities of 95% to 99.2%[30,47,54,98].
Advancements like femtosecond fiber lasers can potentially improve this technique [18].

## Page 4

Crystals 2024, 14, 665 4 of 40
Using the double melt strategy also improves W densification [46]. SLM has the potential
for integration with other techniques (such as infiltration) to achieve higher density in W
parts [19,60].
EBM (Figure 1b) is another prominent AM technique for W [94]. This method employs
an electron beam as its primary heat source, which is manipulated through an electromag-
netic lens, as detailed in Galati [62]. EBM requires a high vacuum level post He/N2 purge
due to electron travel [32,63]. In comparison to SLM, EBM offers a higher power level of
powder [61,99], with typical values between 1000 and 3000 W [ 32,60,63]. This increased
power is responsible for a relative density close to 99.5% in W materials [ 32]. With ap-
propriate preheating, EBM can address cracking issues in AM for W materials [32,61,62],
with many promising results from EBM-fabricated W being reported [32,60,61]. EBM has
also been adapted for W surface treatment to enhance quality, due to its controlled beam
size and thermal influence [69]. Despite the advantages of EBM, challenges in its use that
include complexities associated with electron focusing and the need for maintaining a high
vacuum remain [32].
Laser-based DED (Figure 1c) has the distinction of directly adding energy during
processing [71–77,93]. In laser-based DED, the relationship between molten pool size
and powder flow is crucial [ 4]. Although increased laser energy can widen the molten
pool, when the molten pool exceeds the flow of the powder, it can result in a reduction
in the percentage of W entering [2]. The high-energy laser beam rapidly heats and cools
powders, which reduces the microstructural coarsening duration [ 71,76]. Laser-based
DED, with its larger melt pools (about several mm) and reduced cooling rates [61,71,76,99],
promotes W particle rearrangement and reduces porosity [72–75], while SLM-processed
W materials show fusion deficiencies and non-uniform W particle distribution (despite
powder preheating) that lead to brittleness. There remains a growing interest in laser-based
DED for W alloys because it can produce materials with higher relative density compared
to SLM. This improved performance is largely credited to the technique’s larger laser spot
size [6,31]. Challenges arise in laser-based DED such as managing surface roughness [70]
and the formation of intermetallic compounds due to high energy inputs [31].
In BJ (Figure 1d), a flowable powder is laid onto a build platen, followed by the
selective deposition of binder material in the shape of the intended part [96]. After each
layer, the platen descends, a new powder layer is spread, and the procedure is repeated.
These layers are adhered together to create the targeted component. Once the printing
is finished, the build box undergoes a curing process in an oven to solidify the binder
material [80–84]. The green body is subsequently separated from the surplus powder for
further processing. Then, the part undergoes sintering, similar to a standard compacted W
component. Tungsten Heavy Alloys (WHAs) with a relative density of 99.7% have been
obtained via this method [ 80]. While the BJ method offers the significant advantage of
stacking parts for mass production, achieving fully dense W parts is extremely challenging
due to the necessity of high-temperature sintering.
In subsequent sections, we will discuss the AM of W-based materials, which includes
pure W, W alloys, and W composites. In this review, we consider all combinations of
W with other elements as alloys and refer to combinations of W with ceramic materials
as composites. We begin by examining the factors and processing strategies involved
in the AM of unalloyed W. We next highlight methods to address the challenges related
to processing and properties. Following this, we discuss additively manufactured W
alloys and composites, presenting alloying strategies and the role of dispersed ceramic
phases (in the W composites) on AM processing, and the resulting properties of W alloys
and composites.

## Page 5

Crystals 2024, 14, 665 5 of 40
Table 1. A brief comparison of AM processes for W-based materials.
AM Process Energy (W) Beam Size ( µm) Scan Speed
(mm/s)
Temperature
Gradient
(◦C/mm)
Cooling Rate
(◦C/s)
Relative
Density (%)
SLM
102–103 (normally
below 1000
[60,61,99])
30–200 [61,99] 10–1000 [99] 106–107 [61,99] 10 5–107 [61,99] 99.2 [98]
EBM
102–103 [61,99]
(normally more
than 1000 W,
up to 3000 W
[32,60,63], but can
be as high
as 6000)
100–1000 [61,99] 10–1000 [99] - 103–104 [61,71,99] ~100 [100]
Laser-based DED
102–104 [71,99]
(normally
between 600 and
4000 [61])
100–1000
[61,71,76,99]
10–1000
[61,76,99] 104–106 [61,71,99]
102–105 [99],
mostly on the
order of
104 ◦C/s [19]
More than 99 for
W [2]: even
higher for W
alloys [31]
BJ (Binder Jetting)
[80–84] Not applicable Not applicable Not applicable Not applicable Not applicable 99.7 for WHA [80]
3. Additively Manufactured Unalloyed W: Challenges, Determining Factors, and
Mitigating Strategies
3.1. Problems and Resolutions in Brief
The remarkable properties of unalloyed W, including its exceptional melting point
and high thermal conductivity, make it highly desirable in different applications. How-
ever, problems associated with the AM of W still need to be overcome. This section will
briefly introduce key challenges and look at their potential solutions (Table 2). The me-
chanical properties of additive-manufactured unalloyed W, particularly its elongation,
tensile strength, and fracture toughness, often fall short of expectations. Researchers have
found ways to improve these properties through targeted alloying, the inclusion of ceramic
reinforcements, and optimizing the parameters used during the AM process itself [49].
W is inherently brittle due to its high Peierls stress that stems from its BCC crystal
structure and weak grain boundary cohesion. The ductility of W can be improved through
appropriate alloying, which improves the stacking fault energy of the microstructure to
enhance the slip mechanism [ 60]. The inherent brittleness of W is further exacerbated
by its high DBTT, thermal stresses, and oxygen-induced grain boundary issues, all of
which led to cracking during the AM process. While strategies like alloying, incorporating
carbide/oxide reinforcements, and process adjustments have shown some promise in
improving the ductility of additively manufactured W, further studies are needed to
completely eradicate these cracking problems [21,38,49].
Another problem stems from the confluence of W’s high melting point, low laser
absorptivity (<70% in SLM), and high viscosity, making it difficult for powders of W and al-
loying elements to properly melt and fuse during the printing process. Furthermore, the AM
process can be plagued by phenomena like balling, where molten material forms spheres in-
stead of adhering properly. The selection of W powders with improved laser absorption and
optimization of processing parameters can mitigate these issues [30,38,40,41,43,51,53,101].
Optimizing process control parameters, particularly laser power and scan variables, has
been shown to be instrumental in achieving better densification of W parts [30,38,41,102].
W’s propensity for oxygen poses another challenge, as it leads to the formation and
incorporation of W oxide and subsequent hot cracking during AM. There are limited
options for mitigating the oxidation of W during AM, including the use of high-quality
starting materials, establishing better processing atmospheres, and using specific alloying
combinations [49].

## Page 6

Crystals 2024, 14, 665 6 of 40
Table 2. An overview of the primary challenges, governing factors, and potential or attempted
mitigation strategies in the AM of W.
Challenges Possible Strategy/Developments to Tackle the Challenge Reference
The inherent brittleness and low ductility of W stem
from (1) the high Peierls stress of its BCC crystal
structure and (2) weak grain boundary cohesion.
Requires appropriate alloying to increase stacking fault
energy for easier slip, and microstructural optimization. [60]
High melting point, significant laser absorptivity
(<70% for SLM), pronounced viscosity, densification,
porosities, balling, and deformation.
Use of smaller, spherically shaped W powders to enhance
laser absorptivity; adjusting processing parameters to
influence outcomes like defects, densification, and
grain structures.
Optimizing parameters like power and volumetric energy
density have been found pivotal for improved
W densification.
[30,38,40,41,43,53,71,102]
Oxygen affinity and W oxide segregation lead to
hot cracking.
Better quality starting material (powder, wire) production,
optimized processing atmosphere, alloying. [49]
Cracks due to W embrittlement and high DBTT;
thermal stress-induced, difficult-to-control
crystallization; and oxygen-induced cracking along
the grain boundaries.
Adjusting laser speeds and reducing grain sizes; techniques
to adjust laser speeds and reduce grain sizes showed some
positive results but did not completely resolve the issue.
Scanning strategy optimization: speed, rotation, remelting.
[8,19,21,38,45,49]
Mechanical property issues (tensile strength and
limited fracture toughness) especially in
SLM-fabricated W.
Alloying, introduction of reinforcements,
process adjustments. [49]
3.2. High Melting Point, Related Challenges, and Controlling Strategies
W’s intrinsic high melting point can result in pronounced thermal gradients during
AM. Rapid heating and cooling cycles lead to thermal distortion, significant residual
stresses, and crack initiation. This compromises the mechanical integrity of the printed
components. Furthermore, W exhibits high thermal conductivity. In AM, this causes rapid
heat dissipation, complicating the sustenance of the molten state, leading to partial melting
and inconsistent fusion. These characteristics can influence the resultant component’s
microstructure and mechanical properties [29,41,42,53,67]. In the case of alloyed W, the
evaporation of low melting point elements can also be a challenge. Working at elevated
temperatures also demands more of AM machinery, leading to heightened maintenance
needs and increased costs [61,103]. Concurrently, the susceptibility of W and its alloys to
oxidation increases at high temperatures, often leading to surface oxide formations that
undermine material performance [49].
3.2.1. Melting
Melting behavior is integral to W-AM, often serving as a key factor that defines its
AM processing window. The direct melting of W presents significant challenges due to
the practical constraints associated with high laser power sources and the large beam
sizes required. The very high melting point of W necessitates powerful laser systems
capable of delivering sufficient energy for melting. These systems often require power
sources that are not commonly available in standard AM machines. Additionally, the
large beam sizes needed to ensure adequate energy distribution across the W powder bed
can lead to significant thermal gradients, causing residual stresses and potential cracking.
The combination of high laser power and large beam sizes also limits the precision and
resolution of the final parts. Such strict criteria lead to many partial melting situations,
making it difficult to fabricate high-quality parts [52]. The particle size and morphology
of W powder, layer thickness, heat source power, volumetric energy density controlled by
scanning variables and strategies, melting behavior, and interfacial characteristics are all
important in the melting of W during AM processing.

## Page 7

Crystals 2024, 14, 665 7 of 40
Particle Size and Morphology
Several powder characteristics are decisive for W-AM, especially for PFB pro-
cesses [104,105] . The primary factors include powder particle morphology, particle size,
and purity. Particle size and morphology significantly influence the flowability of the
powder and the resulting powder bed density, which in turn influences the density and
mechanical properties of the final component. Smaller particle sizes generally lead to
better packing density and surface finish but may increase the risk of oxidation and require
higher laser energy due to an increased surface area. The shape of the powder particles
(spherical vs. irregular) directly impacts the flowability such that spherical particles tend
to flow more easily and pack more densely than irregularly shaped particles, resulting in
a consistent layer formation during the built cycle. The purity of the powder is critical in
avoiding contamination that can lead to defects in the final product. Impurities can cause
the formation of brittle phases, reduce ductility, and introduce cracks or other anomalies in
AM-fabricated parts.
W’s inherent properties necessitate the modification of its powders. These adjustments
are needed to improve morphology, ensure uniform size, maximize laser absorption [26],
and enhance surface conditions. Techniques such as the utilization of radio frequency
plasma have been employed for these modifications [26,27]. The modifications are critical
for powder flowability and to achieve a desired density [ 27]. Zhang et al. studied the
influence of particle size on laser absorptivity [53], finding absorptivity to be higher when
the powder bed was on a substrate because of incident laser ray entrapment. As an example,
a 5 µm powder natively had 0.53 absorptivity but this increased to 0.603 on a stainless
steel substrate. Finer particles increase absorptivity, which is the ability of a material to
absorb energy from the laser or electron beam, due to their higher surface area-to-volume
ratio. Fine powders can also enhance printability by improving detail resolution, packing
density, and surface finish. Notably, printability is a comprehensive measure of how
effectively a material can be used in a given AM process. It is influenced by a variety of
factors, including powder material properties, machine capabilities, process parameters,
and design considerations.
Given the cost and limited availability of fine powder sizes, Wang et al. [26] explored
an alternative approach to enhance W powder absorptivity. They managed to transform
irregularly shaped powder particles into near-perfect spheres (close to 100% sphericity)
using radio frequency (RF) induction plasma. These spherical particles were significantly
smaller (average size of 31.5 µm) compared to the raw powder (average size of 56.8 µm).
This transformation resulted in a significant increase in absorptivity, exceedingly not
only in the raw powder (as shown in Figure 2) but also exceeding the values predicted
by Zhang et al. [ 53]. Very fine particles with an average size of 17.3 µm were used to
successfully obtain continuous tracks without cracks [29]. However, it is important to note
that studies have not established a direct correlation between particle size and achieving
crack-free tracks of pure W.
Power, Volumetric Energy Density, Layer Thickness
Volumetric energy density (VED) is a crucial parameter in AM design, as it plays a
decisive role in defining processing parameters. This can be mathematically represented in
Equation (1), where the VED is expressed as follows [106,107]:
VED = P/(v × s × t) (1)
where P is the laser power, v is the laser scanning speed, s is the hatch spacing, and t is the
layer thickness. The energy input required for AM varies depending on the specific AM
processes, machine parameters, material characteristics, and part geometries. Due to the
interplay of these factors, a single, universal value for energy input in the AM of a material
cannot be established. These variations are reflected in the reported literature, where a
wide range of energy input values is observed for W-based materials (e.g., 400 J/mm 3,

## Page 8

Crystals 2024, 14, 665 8 of 40
8.595 J/mm3, 1000 J/mm3). These variations highlight the importance of considering the
specific experimental conditions under which such values were determined. Table 3 offers
an overview of the VED’s effect on W-AM.
Crystals 2024, 14, 665 8 of 44 
 
 
 
Figure 2. Comparison of absorption properties between non-spherical (raw) and spherical W pow-
ders [26]. Reproduced with permission from Elsevier. 
Power, Volumetric Energy Density, Layer Thickness 
Volumetric energy density ( VED) is a crucial parameter in AM design, as it plays a 
decisive role in defining processing parameters. This can be mathematically represented 
in Equation (1), where the VED is expressed as follows [106,107]: 
VED = P/(v × s × t) (1)
where P is the laser power, v is the laser scanning speed, s is the hatch spacing, and t is 
the layer thickness. The energy input required for AM varies depending on the specific 
AM processes, machine parameters, material characteristics, and part geometries. Due to 
the interplay of these factors, a single, univ ersal value for energy input in the AM of a 
material cannot be established. These variatio ns are reflected in the reported literature, 
where a wide range of energy input values is observed for W-based materials (e.g., 400 
J/mm3, 8.595 J/mm3, 1000 J/mm3). These variations highlight the importance of considering 
the specific experimental conditions under which such values were determined. Table 3 
offers an overview of the VED’s effect on W-AM. 
Sidambe and Fox [108] as well as Sidambe et al. [36] investigated the impact of VED 
on the relative density of W parts. Both stud ies found relative density to increase with 
higher VED, although the latter reported even higher relative density values at the same 
VED (Figure 3a). Guo et al. [41] and Hu et al. [42] examined the impact of VED on relative 
density and hardness using spherical particles. They found that increasing VED led to 
increased relative density and decreased pore size to achieve a maximum relative density 
of approximately 98.3%. Microhardness also increased with higher VED, reaching values 
of 474 Hv [41] and 430 Hv [42]. Other studies on SLM, however, reveal the complexity of 
the influence of VED and laser power. Yamamoto et al. investigated how laser power, 
scanning speed, and hatch spacing affect the density of W cylinders [50]. The parts printed 
from pure polyhedral W powder at a preheating temperature of 35 °C showed that higher 
laser power and wider hatch spacing led to denser parts, matching the results of those 
from Rebesan et al. [37]. Plotting the VED against relative densit y showed the highest 
relative density reached was 98.58% at a VED of 411 J/mm
3 (P = 370 W, v = 500 mm/s, h = 
90 μm, t = 20 μm; Figure 3b). This VED trend differed from those of Guo et al. [41] and 
Enneti et al. [51], who reported increasing relative density within the VED range. This 
difference highlights the uncertain role of VED in relative density estimation. Hatch spac-
ing and scanning strategy affect part integrity, porosity type, and thermal history for each 
layer. Thus, interpreting these trends requires a full understanding of each study’s param-
eters and specific porosity characteristics [50,58]. Wen et al. [30] studied the fabrication of 
W cubes with varying laser power, scanning speed, and hatch spacing. They found the 
Figure 2. Comparison of absorption properties between non-spherical (raw) and spherical W pow-
ders [26]. Reproduced with permission from Elsevier.
Sidambe and Fox [108] as well as Sidambe et al. [36] investigated the impact of VED
on the relative density of W parts. Both studies found relative density to increase with
higher VED, although the latter reported even higher relative density values at the same
VED (Figure 3a). Guo et al. [41] and Hu et al. [42] examined the impact of VED on relative
density and hardness using spherical particles. They found that increasing VED led to
increased relative density and decreased pore size to achieve a maximum relative density
of approximately 98.3%. Microhardness also increased with higher VED, reaching values
of 474 Hv [41] and 430 Hv [ 42]. Other studies on SLM, however, reveal the complexity
of the influence of VED and laser power. Yamamoto et al. investigated how laser power,
scanning speed, and hatch spacing affect the density of W cylinders [50]. The parts printed
from pure polyhedral W powder at a preheating temperature of 35 ◦C showed that higher
laser power and wider hatch spacing led to denser parts, matching the results of those
from Rebesan et al. [ 37]. Plotting the VED against relative density showed the highest
relative density reached was 98.58% at a VED of 411 J/mm 3 (P = 370 W, v = 500 mm/s,
h = 90 µm, t = 20 µm; Figure 3b). This VED trend differed from those of Guo et al. [ 41]
and Enneti et al. [51], who reported increasing relative density within the VED range. This
difference highlights the uncertain role of VED in relative density estimation. Hatch spacing
and scanning strategy affect part integrity, porosity type, and thermal history for each layer.
Thus, interpreting these trends requires a full understanding of each study’s parameters
and specific porosity characteristics [50,58]. Wen et al. [ 30] studied the fabrication of W
cubes with varying laser power, scanning speed, and hatch spacing. They found the
use of low laser power to result in dense, high-relative-density cubes due to the laser’s
impact on melt pool temperature. Increasing the line (laser) energy density (LED) led
to warped morphologies, which were eliminated with a further increase in LED due to
stronger interlayer bonding. Cracks were observed but reduced with higher scanning
speed, reaching a maximum relative density of 98.71% at 200 mm/s scanning speed.
For W materials, a higher VED and subsequent higher processing temperature may
reduce the resultant residual stresses due to enhanced annealing effects [ 60,109]. This
reduction in residual stresses might be why using EBM generally leads to a reduced
cracking probability in W materials when compared to using SLM [63]. Extremely high
VEDs (e.g., >300 J/mm3) are not necessarily beneficial (Figure 3c) [19,50,110]. Density in
AM-produced W parts is influenced by several factors. One issue is unstable laser melting.
The intense laser beam can create deep holes, called keyholes, that do not fully solidify,

## Page 9

Crystals 2024, 14, 665 9 of 40
leaving air pockets (porosity) throughout a part [19]. Another problem arises from using
too much laser power. Excessive melting disrupts the molten metal pool, trapping air
bubbles and reducing density [ 32]. Powder characteristics can also be problematic. If
particles do not flow smoothly into the melt pool but instead stick to the edges, they create
voids and hinder densification [32]. Finally, W’s high melting point presents another hurdle.
Some elements that evaporate easily (volatile elements) may vaporize during the printing
process, leaving behind tiny holes that contribute to lower density [60,61].
Crystals 2024, 14, 665 9 of 44 
 
 
use of low laser power to result in dense, high-relative-density cubes due to the laser’s 
impact on melt pool temperature. Increasing the line (laser) energy density (LED) led to 
warped morphologies, which were eliminated with a further increase in LED due to 
stronger interlayer bonding. Cracks were observed but reduced with higher scanning 
speed, reaching a maximum relative density of 98.71% at 200 mm/s scanning speed. 
For W materials, a higher VED and subseq uent higher processing temperature may 
reduce the resultant residual stresses due to enhanced annealing effects [60,109]. This re-
duction in residual stresses might be why using EBM generally leads to a reduced crack-
ing probability in W materials when compared to using SLM [63]. Extremely high VEDs 
(e.g., >300 J/mm
3) are not necessarily beneficial (Fig ure 3c) [19,50,110]. Density in AM-
produced W parts is influenced by several factors. One issue is unstable laser melting. The 
intense laser beam can create deep holes, called keyholes, that do not fully solidify, leaving 
air pockets (porosity) throughout a part [19]. Another problem arises from using too much 
laser power. Excessive melting disrupts the molten metal pool, trapping air bubbles and 
reducing density [32]. Powder characteristics can also be problematic. If particles do not 
flow smoothly into the melt pool but instead stick to the edges, they create voids and 
hinder densification [32]. Finally, W’s high melting point presents another hurdle. Some 
elements that evaporate easily (volatile elements) may vaporize during the printing pro-
cess, leaving behind tiny holes that contribute to lower density [60,61]. 
 
Figure 3. (a) The relative density of SLM-fabricated W cubes [36,108], (b) influence of VED on the density 
of pure W parts made with SLM [50], (c) influence of substrate preheating temperatures on the relative 
density of W samples [19], (d) relationship between VED and density in W-nickel alloy (W-15Ni) parts 
fabricated using DED [74], and (e) influence of LED and electron beam power on the relative density of 
W parts made with EBM [58]. Data and figures were reproduced with permission from Elsevier. 
The work of Wang et al. on the laser-based DED processing of W found the relative 
density of fabricated parts increases with VED (Figure 3d) [74]. In their study on EBM 
processing of unalloyed W, Dorow-Gerspach et al. investigated the impact of LED varia-
tions by altering the power and speed of the electron beam to assess its effect on cubic 
samples [65]. These experiments were carried out at a substrate preheating temperature 
of 1000 °C. They achieved a high relative density of 99.5% but observed cracking in all 
Figure 3. (a) The relative density of SLM-fabricated W cubes [36,108], (b) influence of VED on the
density of pure W parts made with SLM [50], (c) influence of substrate preheating temperatures on
the relative density of W samples [19], (d) relationship between VED and density in W-nickel alloy
(W-15Ni) parts fabricated using DED [74], and (e) influence of LED and electron beam power on the
relative density of W parts made with EBM [58]. Data and figures were reproduced with permission
from Elsevier.
The work of Wang et al. on the laser-based DED processing of W found the relative
density of fabricated parts increases with VED (Figure 3d) [ 74]. In their study on EBM
processing of unalloyed W, Dorow-Gerspach et al. investigated the impact of LED vari-
ations by altering the power and speed of the electron beam to assess its effect on cubic
samples [65]. These experiments were carried out at a substrate preheating temperature
of 1000 ◦C. They achieved a high relative density of 99.5% but observed cracking in all
fabricated cubes. While increasing electron beam energy led to a decrease in relative density,
it also resulted in a decrease in crack density (Figure 3e), highlighting the trade-off between
densification and structural integrity in this AM process [65].
High energy inputs in AM processes that include SLM affect the molten pool due to
the Marangoni effect. The severity of this effect is directly proportional to the laser energy
input [38,111,112]. This effect can drag gas into the molten pool, leading to pore formation
upon solidification. Excessive laser energy density, especially at lower scan speeds, can
also result in molten pool instabilities, yielding a rough track [29]. As SEM images showing
the typical surface morphologies of scanning tracks at different laser powers in the AM
processing of W (Figure 4a–e [29]) indicate, an optimal laser power can result in a regular
flow front and no cracking (Figure 4b).

## Page 10

Crystals 2024, 14, 665 10 of 40
Crystals 2024, 14, 665 10 of 44 
 
 
fabricated cubes. While increasing electron beam energy led to a decrease in relative den-
sity, it also resulted in a decrease in crack density (Figure 3e), highlighting the trade-off 
between densification and structural integrity in this AM process [65]. 
High energy inputs in AM processes that include SLM affect the molten pool due to 
the Marangoni effect. The severity of this effect is directly proportional to the laser energy 
input [38,111,112]. This effect can drag gas into the molten pool, leading to pore formation 
upon solidification. Excessive laser energy dens ity, especially at lower scan speeds, can 
also result in molten pool instabilities, yielding a rough track [29]. As SEM images show-
ing the typical surface morphologies of scanning tracks at different laser powers in the 
AM processing of W (Figure 4a–e [29]) indicate, an optimal laser power can result in a 
regular flow front and no cracking (Figure 4b). 
Properly controlling the melting behavior during AM can yield several significant 
advantages. High energy input facilitates th e mixing of elements with lower melting 
points, enhancing interfacial bonding through Marangoni convection [29,97]. Stable mol-
ten pools promote the formation of complete columnar crystals in additively manufac-
tured W parts [32]. Additionally, techniques such as EBM can introduce remelting during 
AM, annealing the built portion of the W parts, and reducing their susceptibility to crack-
ing [63]. Another parameter affecting melting in AM processing is the layer thickness, as 
indicated in Equation (1). The comprehensive review by Marcos et al. indicates that re-
ducing the layer thickness in PBF processes requires less energy to melt the powder, re-
sulting in continuous conduction mode tracks at lower energy input levels [58]. 
 
Figure 4. SEM images showing surface morphologies of scanning tracks at a laser power of ( a) 250 
W, (b) 300 W, (c) 350 W, (d) 400 W, and (e) 450 W; the scanning speed is 200 mm/s [29]. 
Scan Speed 
Scanning speed is a dominant factor, accounting for a ~75% variation in W densifica-
tion within the SLM process [51,60]. Ren et al. [17] examined how the morphology of W 
single tracks can be influenced by laser po wer and scanning speed. These single tracks 
were printed onto a stainless steel substrate preheated to 200 °C. Establishing a processing 
map based on the surface characteristics of th e single tracks (Figure 5a) allows different 
regions to be delineated, where one can observe regular tracks, irregular tracks, or in-
stances of balling. The scanning speed plays a critical role in determining the quality of 
the fabricated tracks. At lower scanning speeds, the laser imparts sufficient energy to the 
Figure 4. SEM images showing surface morphologies of scanning tracks at a laser power of (a) 250 W,
(b) 300 W, (c) 350 W, (d) 400 W, and (e) 450 W; the scanning speed is 200 mm/s [29].
Properly controlling the melting behavior during AM can yield several significant
advantages. High energy input facilitates the mixing of elements with lower melting
points, enhancing interfacial bonding through Marangoni convection [29,97]. Stable molten
pools promote the formation of complete columnar crystals in additively manufactured
W parts [32]. Additionally, techniques such as EBM can introduce remelting during AM,
annealing the built portion of the W parts, and reducing their susceptibility to cracking [63].
Another parameter affecting melting in AM processing is the layer thickness, as indicated in
Equation (1). The comprehensive review by Marcos et al. indicates that reducing the layer
thickness in PBF processes requires less energy to melt the powder, resulting in continuous
conduction mode tracks at lower energy input levels [58].
Scan Speed
Scanning speed is a dominant factor, accounting for a ~75% variation in W densi-
fication within the SLM process [ 51,60]. Ren et al. [ 17] examined how the morphology
of W single tracks can be influenced by laser power and scanning speed. These single
tracks were printed onto a stainless steel substrate preheated to 200 ◦C. Establishing a
processing map based on the surface characteristics of the single tracks (Figure 5a) allows
different regions to be delineated, where one can observe regular tracks, irregular tracks,
or instances of balling. The scanning speed plays a critical role in determining the quality
of the fabricated tracks. At lower scanning speeds, the laser imparts sufficient energy to
the powder, facilitating the formation of regular and continuous tracks. Conversely, as the
scanning speed increases, the reduced time available for melting and consolidation leads
to the formation of irregular tracks and balling, where molten material forms spherical
particles instead of continuous lines.
Rebesan et al. [ 37] explored how adjusting the laser scanning speed and spacing
between hatch spacing affects the density of SLM-fabricated W parts under Ar atmosphere
at a power of 170 W and spherical particles (Figure 5b). This approach resulted in achieving
high relative densities of 96.4% to 99.6%. Enneti et al. took a different approach, with
the laser power kept at 90 watts, a VED of 1000 J/mm 3, and the base plate preheated to
80 ◦C [51,102]. With these settings, densities ranging from 60% to 75% were achieved.
Li et al. [113] examined the impact of process parameters (laser power, scanning speed,

## Page 11

Crystals 2024, 14, 665 11 of 40
hatch spacing) on the density of as-SLM bulk W parts, achieving a maximum relative
density of 98.31%, and creating process maps (Figure 6). Here, there was a direct correlation
between laser power and density (Figure 6a), with hatch spacing and scanning speed
having minor effects (Figure 6b,c). High densities (>98%) were consistently attained
with 250–300 W power, 0.08–0.1 mm hatch spacing, and 0.03 mm layer thickness, offering
valuable insights into process optimization. Xiong et al. [45] used image analysis to measure
density and established process parameters for achieving high-density W coupons. They
achieved densities of 97.3% to 98.1% with laser powers between 250 and 300 W and
scanning speeds of 400 to 500 mm/s. Dong et al. [114] conducted a study to investigate how
various factors influence the quality of AM-produced W parts. They utilized a preheating
temperature of 100 ◦C and employed irregularly shaped (polyhedral) particles for the
powder material. Furthermore, they observed that higher laser power and slower scanning
speeds produced denser parts. However, when the scanning speed was excessively high, it
caused the material to ball up and led to the formation of surface pores. Specific studies on
the effect of nitrogen on W-AM are limited. Dong et al. [114] found that W parts printed
under a nitrogen atmosphere achieved higher density, hardness, and overall strength
compared to those printed under an argon atmosphere.
Crystals 2024, 14, 665 11 of 44 
 
 
powder, facilitating the formation of regula r and continuous tracks. Conversely, as the 
scanning speed increases, the reduced time available for melting and consolidation leads 
to the formation of irregular tracks and ball ing, where molten material forms spherical 
particles instead of continuous lines. 
 
Figure 5. (a) Processing map for SLM of unalloyed W [17], and ( b) the influence of hatch spacing 
and scanning speed on the relative density. The laser was maintained at a power of 170 W and the 
substrate was preheated to 80 °C [37]. Reproduced with permission from Elsevier. 
Rebesan et al. [37] explored how adjusting the laser scanning speed and spacing be-
tween hatch spacing affects the density of SLM-fabricated W parts under Ar atmosphere 
at a power of 170 W and spherical particles (Figure 5b). This approach resulted in achiev-
ing high relative densities of 96.4% to 99.6%. Enneti et al. took a different approach, with 
the laser power kept at 90 watts, a VED of 1000 J/mm
3, and the base plate preheated to 80 
°C [51,102]. With these settings, densities ranging from 60% to 75% were achieved. Li et 
al. [113] examined the impact of process para meters (laser power, scanning speed, hatch 
spacing) on the density of as-SLM bulk W parts, achieving a maximum relative density of 
98.31%, and creating process maps (Figure 6). Here, there was a direct correlation between 
laser power and density (Figure 6a), with hatch spacing and scanning speed having minor 
effects (Figure 6b,c). High densities (>98%) were consistently attained with 250–300 W 
power, 0.08–0.1 mm hatch spacing, and 0.03 mm layer thickness, offering valuable insights 
into process optimization. Xion g et al. [45] used image anal ysis to measure density and 
established process parameters for achievin g high-density W coupons. They achieved 
densities of 97.3% to 98.1% with laser powers between 250 and 300 W and scanning speeds 
of 400 to 500 mm/s. Dong et al. [114] conducted a study to investigate how various factors 
influence the quality of AM-produced W parts. They utilized a preheating temperature of 
100 °C and employed irregularly shaped (polyhedral) particles for the powder material. 
Furthermore, they observed that higher laser power and slower scanning speeds pro-
duced denser parts. However, when the scanning speed was excessively high, it caused 
the material to ball up and led to the format ion of surface pores. Specific studies on the 
effect of nitrogen on W-AM are limited. Dong et al. [114] found that W parts printed under 
a nitrogen atmosphere achieved higher density, hardness, and overall strength compared 
to those printed under an argon atmosphere. 
Figure 5. (a) Processing map for SLM of unalloyed W [17], and (b) the influence of hatch spacing
and scanning speed on the relative density. The laser was maintained at a power of 170 W and the
substrate was preheated to 80 ◦C [37]. Reproduced with permission from Elsevier.
Recent findings by Sharma et al. [98] have demonstrated a maximum relative density of
99.2% for pure W, which is the highest value reported in the SLM of pure W. They employed
a multi-scale thermo-kinetic and thermo-mechanical computational model to fine-tune the
laser parameters and understand the thermal behavior during the melting and solidification
phases. Their work demonstrates the potential for further density improvement through
controlling laser power, scan speed, and hatch spacing.
Other Scanning Variables and Strategies
The scanning pattern plays a critical role in determining the thermal history of pro-
cessed W materials, offering flexibility suitable for a variety of applications. This flexibility
represents a unique advantage of AM over traditional manufacturing techniques. Table 3
offers an overview of scanning variables and strategies employed in W-AM. The localized
differences in material properties can be ascribed to the focused energy input from electron
or laser beams or other energy sources that determine the thermal history experiences at a
point [60]. In the EBM process, for example, one can witness multiple instances of melting
and re-melting at a single scanning point [ 63]. EBM utilizes flexible bidirectional scan
patterns to optimize densification and surface finish, leading to a high print quality [32].

## Page 12

Crystals 2024, 14, 665 12 of 40
Crystals 2024, 14, 665 12 of 44 
 
 
 
Figure 6. Processing map for SLM of W. (a) laser power vs. hatch spacing, (b) laser power vs. scan-
ning speed, and (c) scanning speed vs. hatch spacing, [113]. 
Recent findings by Sharma et al. [98] have demonstrated a maximum relative density 
of 99.2% for pure W, which is the highest value reported in the SLM of pure W. They 
employed a multi -scale thermo-kinetic and thermo -mechanical computational model to 
fine-tune the laser parameters and understand the thermal behavior during the melting 
and solidification phases. Their work demonstrates the potential for further density im-
provement through controlling laser power, scan speed, and hatch spacing. 
Other Scanning Variables and Strategies 
The scanning pattern plays a critical role in determining the thermal history of pro-
cessed W materials, offering flexibility suitable for a variety of applications. This flexibility 
represents a unique advantage of AM over traditional manufacturing techniques. Table 3 
offers an overview of scanning variables and strategies employed in W-AM. The localized 
differences in material properties can be ascribed to the focused energy input from elec-
tron or laser beams or other energy sources that determine the thermal history experiences 
at a point [60]. In the EBM process, for example, one can witness multiple instances of 
melting and re-melting at a single scanning point [63]. EBM utilizes flexible bidirectional 
scan patterns to optimize densification and surface finish, leading to a high print quality 
[32]. 
In PBF for W materials, different scanning patterns have been explored. A 67 ° rota-
tion between layers randomizes grain orientation, reducing the ladder-shaped grain struc-
tures which are potential crack-formation sites [21]. While many studies adopt a 67° rota-
Figure 6. Processing map for SLM of W. ( a) laser power vs. hatch spacing, ( b) laser power vs.
scanning speed, and (c) scanning speed vs. hatch spacing, [113].
In PBF for W materials, different scanning patterns have been explored. A 67◦ rotation
between layers randomizes grain orientation, reducing the ladder-shaped grain structures
which are potential crack-formation sites [21]. While many studies adopt a 67◦ rotation to
minimize scan alignment, others use rotational angles of 45◦ or 90◦ [8,19,27]. Remelting,
which is scanning a track multiple times before recoating, combined with rotation, curtails
the formation of columnar grains and reduces longitudinal cracks, resulting in smaller
grain sizes and reduced surface roughness [21,45,61]. Wang et al. [21] investigated crack
development in SLM of unalloyed W. They studied three scanning strategies: parallel, 67◦
rotation, and remelting with 67◦ rotation. Matching scan tracks between layers resulted
in consistent crack growth along the build direction. Rotation between layers reduced
crack propagation, while remelting did not effectively reduce cracks but instead promoted
thermal fatigue crack growth [21].
A growing body of research explores the relationship between scan pattern design and
the properties of additively manufactured W materials. These studies have quantified the
effects of specific pattern parameters. Hatch spacing, interestingly, is responsible for a mere
~7% fluctuation in the final W densification [60]. Point distance is another crucial factor in
the AM relative density for W materials. Wang et al. [43] and Huang et al. [115] studied the
influences of point distance and hatch spacing on the relative density of W achieved when
pulsed (Figure 7a), and continuous lasers were used (Figure 7b,c), respectively. By adjusting
these parameters, different melting strategies can be deployed, presenting an opportunity
to oversee and regulate re-melting sequences to ensure that they sidestep randomness [46].

## Page 13

Crystals 2024, 14, 665 13 of 40
Crystals 2024, 14, 665 13 of 44 
 
 
tion to minimize scan alignment, others use rotational angles of 45° or 90° [8,19,27]. Re-
melting, which is scanning a track multiple times before recoating, combined with rota-
tion, curtails the formation of columnar grains and reduces longitudinal cracks, resulting 
in smaller grain sizes and reduced surface roug hness [21,45,61]. Wang et al. [21] investi-
gated crack development in SLM of unalloyed W. They studied three scanning strategies: 
parallel, 67° rotation, and remelting with 67° rotation. Matching scan tracks between lay-
ers resulted in consistent crack growth along the build direction. Rotation between layers 
reduced crack propagation, while remelting did not effectively reduce cracks but instead 
promoted thermal fatigue crack growth [21]. 
A growing body of research explores the relationship between scan pattern design 
and the properties of additively manufactured W materials. These studies have quantified 
the effects of specific pattern parameters. Hatch spacing, interestingly, is responsible for a 
mere ~7% fluctuation in the final W densification [60]. Point distance is another crucial 
factor in the AM relative density for W materials. Wang et al. [43] and Huang et al. [115] 
studied the influences of point distance and hatch spacing on the relative density of W 
achieved when pulsed (Figure 7a), and continuous lasers were used (Figure 7b,c), respec-
tively. By adjusting these parameters, differ ent melting strategies can be deployed, pre-
senting an opportunity to oversee and regulate re-melting sequences to ensure that they 
sidestep randomness [46]. 
 
Figure 7. Influence on the relative density of manufactured W cubes due to the interaction between 
hatch spacing and point distance with input parameters of ( a) a pulsed laser power of 400 W and 
exposure time of 100 μs [43], and (b,c) a laser power of 40 W, layer thickness of 50 μm, and exposure 
time of 300 μs [115]. Reproduced with permission from Elsevier. 
In examining the role of scan track design, we find it plays an important role in pat-
tern design, especially in upholding the quality of SLM-fabricated parts [60]. Parameters 
such as the single scan track width and hatch spacing can be adjusted. Within SLM, the 
overlap rate is devised in line with these two parameters, serving as an analytical tool to 
gauge conditions across multiple scan tracks. Previous studies have underscored a non-
linear relationship between scan track characteristics, which is dictated by overlap design 
choices, and the eventual densification of W ma terial. This points to the existence of an 
optimal overlap rate that balances these parameters [17]. 
Table 3. An overview of scanning variables and strategies employed in the AM of W. 
Parameters Details Reference 
VED 
- VED: 
- Increased power in AM aﬀects the molten pool via the Marangoni 
eﬀect, with the severity proportional to laser energy. 
- Can introduce gas, causing pore formation and pool instabilities, 
resulting in rough tracks. 
- Enhances the densiﬁcation of manufactured parts. 
- Reduces residual stresses via annealing. 
- Relates to pattern design. 
[19,29,32,38,50,60,61,63,74,97,
109–112] 
Figure 7. Influence on the relative density of manufactured W cubes due to the interaction between
hatch spacing and point distance with input parameters of (a) a pulsed laser power of 400 W and
exposure time of 100 µs [43], and (b,c) a laser power of 40 W, layer thickness of 50 µm, and exposure
time of 300 µs [115]. Reproduced with permission from Elsevier.
In examining the role of scan track design, we find it plays an important role in pattern
design, especially in upholding the quality of SLM-fabricated parts [60]. Parameters such
as the single scan track width and hatch spacing can be adjusted. Within SLM, the overlap
rate is devised in line with these two parameters, serving as an analytical tool to gauge
conditions across multiple scan tracks. Previous studies have underscored a non-linear
relationship between scan track characteristics, which is dictated by overlap design choices,
and the eventual densification of W material. This points to the existence of an optimal
overlap rate that balances these parameters [17].
Table 3. An overview of scanning variables and strategies employed in the AM of W.
Parameters Details Reference
VED
- VED:
- Increased power in AM affects the molten pool via the
Marangoni effect, with the severity proportional to
laser energy.
- Can introduce gas, causing pore formation and pool
instabilities, resulting in rough tracks.
- Enhances the densification of manufactured parts.
- Reduces residual stresses via annealing.
- Relates to pattern design.
- Extremely high energy densities (>300 J/mm3) have
drawbacks: more porosity, excessive fusion risks,
disrupted melt pools with stuck powder particles, and
the vaporization of volatile elements. These challenges
impact printed part quality.
- Controlled melting has benefits, allows the mixing of
low melting point elements, and improves interfacial
bonding. It promotes the growth of full columnar
crystals in W-AM.
[19,29,32,38,50,60,61,63,74,97,109–112]
Scanning Variables
- Direction and Angle:
- EBM process allows multiple instances of melting and
re-melting at a single scanning point.
- 90 ◦ alternating bidirectional scanning in SLM.
- 67 ◦ alternating bidirectional scan.
- Speed: scanning speed affects ~75% of W densification
variation in SLM.
- Hatch Spacing: affects ~7% of W densification variation.
- Overlap Rate: The relationship between scan track
characteristics and final W material densification is
non-linear. An optimal overlap rate exists.
- Scan Track Width
[17,19,27,32,46,51,60,63]

## Page 14

Crystals 2024, 14, 665 14 of 40
Wetting Behavior and Interfacial Characteristics
For producing high-quality components via AM, interfacial design and W wetting be-
havior at multiple scales are vital due to their well-documented influence on reducing crack
initiation and propagation, and on mechanical properties (Table 4). Microscopic wetting be-
havior involves the internal heterogeneous boundaries within the AM-produced W parts. W
is not easily wettable by most metals at low temperatures (below 2000◦C). The temperature-
dependent wettability of W has been a focal point for many researchers [60,116]. Mura-
matsu et al. [97,117] underscored the significance of the heterogeneous interface, especially
when considering the broad temperature range covered in AM processes [97,116,118]. To
enhance the AM quality of W-based materials, researchers have introduced small quantities
of transition metals like Ni and Fe. These elements reduce the activation energy required
during the sintering of W, accelerate W diffusion, and provide improved wettability to
facilitate an AM process [60,97].
Table 4. An overview of W wetting behavior and interfacial phenomena at micro as well as macro
scale in AM processes.
Category Description Examples and Developments References
Microscopic Wetting Behavior Concerns internal heterogeneous
boundaries in W-AM.
- Temperature-dependent wettability of W
- Introduction of Ni and Fe to improve
wettability and AM quality
[60,97,116–118]
Macroscopic W
Material/Substrate Interfacial
Wetting and Reaction
Relates to interfaces between the
substrate and W material,
affecting parts quality.
- Use of stainless steel interlayers
containing nickel
- Substituting substrates with Ti-based alloys,
e.g., Ti–6Al–4V
- Sandwich-structural printing sequences
- Risks of diffusion-induced secondary phases
and unwanted reactions
[32,73,97,119]
On the other hand, macroscopic W material/substrate interfacial wetting and reaction
involve the interfaces between the substrate and the W material to influence the final
quality of an AM part. Stainless steel interlayers, containing nickel, have been employed
to improve the adhesion between W and other alloying elements because of an enhanced
solid-state diffusion and grain boundary diffusion [97]. For better outcomes, substrates can
be substituted with Ti-based alloys such as Ti–6Al–4V due to the enhanced thermodynamic
compatibility between W and Ti [32]. Novel approaches, like sandwich-structural printing
sequences, have been developed for W materials, leading to better quality AM parts [119].
However, using such interlayers can lead to diffusion-induced secondary phases. Addition-
ally, interactions with other elements might bring about unwanted reactions, such as the
peritectic reaction seen between Fe and W during non-equilibrium solidification [73,97].
3.3. Oxygen, DBTT, and Micro-Cracking
Oxygen, along with other interstitial contaminants like nitrogen and hydrogen, presents
serious challenges in the AM of refractory alloys (including W materials). Such contami-
nants, particularly oxygen, critically affect properties like the DBTT value in W materials,
with molten W being especially sensitive to oxygen [17,120–122]. This heightened sensitiv-
ity leads to embrittlement, increasing DBTT, and decreased strength. Table 5 summarizes
the current understanding of oxygen contamination for W in AM processing. Common
sources of oxygen contamination include oxidized powder surfaces, residual oxygen in the
chamber [49], and oxygen present in the substrate due to high thermal energy inputs which
suggests that substrates may function as oxygen reservoirs [19]. The powders utilized in
AM, owing to their vast surface-to-volume ratio, are notably prone to absorbing oxygen
from their surroundings. Moreover, when W is exposed to oxygen at room temperature,
it promptly forms an oxide layer within an hour [123]. Nagy and Humphry-Baker [122]
conducted a study on the oxidation of W and developed a W oxidation mechanism map
to reveal the kinetics of W oxidation at the 600–1600 ◦C temperature range (Figure 8).

## Page 15

Crystals 2024, 14, 665 15 of 40
This can be useful in W-AM. Under AM’s elevated temperatures, oxygen can not only
diffuse swiftly into the alloy but also react with W, resulting in intergranular cracking upon
cooling [48,63,124].
Table 5. Current understanding of interstitial contamination in W during AM processing.
Factor/Parameter Details/Effects References
Contaminants Oxygen, nitrogen, hydrogen [17,120–122]
Adverse Effects
- Embrittlement
- Shifts in DBTT
- Strength reduction
- Cause cracking especially at HAGBs
[17,21,120–122]
Sources of Oxygen in W Materials
- Oxidized powder surface
- Residual oxygen in the chamber
- Substrates due to high thermal energy inputs
[19,49]
Oxygen Sensitivity in W Materials
- Molten W is sensitive to oxygen
- Oxide layer formation (1 nm thick within an hour)
- Potential for intergranular cracking upon cooling
[48,63,123,124]
Oxygen Control Techniques in AM Processes
- Higher beam power
- Enhanced VED
- Radio frequency induction plasma treatment
[26,63]
Material Design for Reduced Oxygen Sensitivity Introduction of alloying elements such as Ta to W [48]
Important Studies and Findings Oxidation mechanism map for AM applications exists [122]
Crystals 2024, 14, 665 16 of 44 
 
 
 
Figure 8. W oxidation map in the temperature range of 600–1600 °C and up to 2 years. Contours 
indicate the thickness of the metal oxidized. Th e parabolic, linear, and sublimation regions are 
shaded in green, red, and blue respectively [122]. Reproduced with permission from Elsevier. 
Reducing oxygen levels during the AM process is paramount, as this will improve 
part quality by reducing the occurrence of crac ks [49]. W oxides can remain stable at up 
to 2000 °C, potentially initiating cracks during rapid solidification [120]. To confront these 
challenges, researchers can turn to several strategies in many metallic systems. Gas atom-
ization under inert conditions delivers powders with appreciably lower oxygen and ni-
trogen contents. The use of inert gas environments, such as argon or helium, during AM 
offers a practical way to minimize contamination by isolating the alloy from potential con-
taminants. Additionally, enhancing powder handling and storage protocols—like the vac-
uum packaging of powders an d handling under inert atmo spheres—is another avenue 
being explored to eliminate contamination. Implementing techniques like using higher 
beam power and enhancing volumetric energy density can diminish the oxygen content 
and curb cracking [63]. The role of oxygen is not just restricted to the fabrication process 
but extends to preheating, underscoring the necessity for an oxygen-regulated environ-
ment [32]. Innovatively, as pointed out earlier, methods such as radio frequency induction 
plasma treatment have been deployed to ma nage oxygen levels effectively [26]. Further-
more, material design advancements, like introducing Ta to W, offer a promising avenue 
to counteract oxygen sensitivity [48]. To facilitate deeper insights, detailed studies to un-
derstand W oxidation have been undertaken, resulting in the creation of an oxidation 
mechanism map tailored for AM [122]. 
Crack nucleation and propagation in the AM of W correlate with its high DBTT of 
approximately 200–600 °C. Support for this comes from an observed delay between solid-
ification and crack appearance using in situ high-speed cameras reported by Vrancken et 
al. [24,35]. Cracks often propagate along high-angle grain boundaries (HAGBs) [21], 
where the formation of cracks in the intergranular regions of SLM-fabricated W has been 
mostly observed. Such behavior is linked to W’s grain boundary sensitivity to impurities, 
notably oxygen, found in amounts between 30 and 370 ppm in W powder [24,38]. While 
some researchers attribute cracks to W oxide aggregation during solidification 
Figure 8. W oxidation map in the temperature range of 600–1600 ◦C and up to 2 years. Contours
indicate the thickness of the metal oxidized. The parabolic, linear, and sublimation regions are shaded
in green, red, and blue respectively [122]. Reproduced with permission from Elsevier.
Reducing oxygen levels during the AM process is paramount, as this will improve
part quality by reducing the occurrence of cracks [ 49]. W oxides can remain stable at

## Page 16

Crystals 2024, 14, 665 16 of 40
up to 2000 ◦C, potentially initiating cracks during rapid solidification [120]. To confront
these challenges, researchers can turn to several strategies in many metallic systems. Gas
atomization under inert conditions delivers powders with appreciably lower oxygen and
nitrogen contents. The use of inert gas environments, such as argon or helium, during
AM offers a practical way to minimize contamination by isolating the alloy from potential
contaminants. Additionally, enhancing powder handling and storage protocols—like
the vacuum packaging of powders and handling under inert atmospheres—is another
avenue being explored to eliminate contamination. Implementing techniques like using
higher beam power and enhancing volumetric energy density can diminish the oxygen
content and curb cracking [63]. The role of oxygen is not just restricted to the fabrication
process but extends to preheating, underscoring the necessity for an oxygen-regulated
environment [32]. Innovatively, as pointed out earlier, methods such as radio frequency
induction plasma treatment have been deployed to manage oxygen levels effectively [26].
Furthermore, material design advancements, like introducing Ta to W, offer a promising
avenue to counteract oxygen sensitivity [48]. To facilitate deeper insights, detailed studies
to understand W oxidation have been undertaken, resulting in the creation of an oxidation
mechanism map tailored for AM [122].
Crack nucleation and propagation in the AM of W correlate with its high DBTT of approx-
imately 200–600◦C. Support for this comes from an observed delay between solidification and
crack appearance using in situ high-speed cameras reported by Vrancken et al.[24,35]. Cracks
often propagate along high-angle grain boundaries (HAGBs) [21], where the formation of
cracks in the intergranular regions of SLM-fabricated W has been mostly observed. Such
behavior is linked to W’s grain boundary sensitivity to impurities, notably oxygen, found
in amounts between 30 and 370 ppm in W powder [24,38]. While some researchers attribute
cracks to W oxide aggregation during solidification [21,37,41,42], persistent cracks at low
oxygen levels indicate other possible influencing factors as well [24]. The role of impurities,
including oxygen and hydrogen, in SLM on W brittleness has not been fully explored.
High-speed in situ SLM videos show cracking across W’s DBTT, likely due to the increased
stress [24]. Such stresses from SLM may only be offset by cracking at impurity-contaminated
grain boundaries [ 42,125]. A study by Rebesan et al. on SLM-fabricated W specimens
revealed a high cracking tendency [37]. Two types of cracks were identified: longitudinal
(along the melt-pool center) and transverse (perpendicular to laser-induced surface ripples).
Longitudinal cracks are linear and 30–100 µm long, while transverse cracks are shorter
with an “S”-shape along grain boundaries (Figure 9). The extensive cracking results from
thermal stresses during rapid solidification or recrystallization (Figure 10a), particularly be-
low the DBTT. Micro-cracks that resemble intergranular hot cracking form due to nanopore
aggregation at grain boundaries induced by boiling W oxides (WOx) in the melting pool
(Figure 10b) [37].
Crystals 2024, 14, 665 17 of 44 
 
 
[21,37,41,42], persistent cracks at low oxygen levels indicate other possible influencing 
factors as well [24]. The role of impurities, including oxygen and hydrogen, in SLM on W 
brittleness has not been fully explored. High -speed in situ SLM videos show cracking 
across W’s DBTT, likely due to the increased stress [24]. Such stresses from SLM may only 
be offset by cracking at im purity-contaminated grain boun daries [42,125]. A study by 
Rebesan et al. on SLM-fabricated W specimen s revealed a high crac king tendency [37]. 
Two types of cracks were identified: longitudinal (along the melt-pool center) and trans-
verse (perpendicular to laser-induced surface ripples). Longitudinal cracks are linear and 
30–100 μm long, while transverse cracks are shorter with an “S”-shape along grain bound-
aries (Figure 9). The extensive cracking results from thermal stresses during rapid solidi-
fication or recrystallization (Figure 10a), particularly below the DBTT. Micro-cracks that 
resemble intergranular hot cracking form due to nanopore aggregation at grain bounda-
ries induced by boiling W oxides (WO
x) in the melting pool (Figure 10b) [37]. 
 
Figure 9. SEM image of surface morphology and crack type in SLM-fabricated W [37]. 
 
Figure 10. SEM images of SLM-fabricated W sample, ( a) electrolytically etched displaying a crack 
network; (b) a higher magnification of grain boundaries displaying micro-cracks and pores [37]. 
Cracking in EBM-produced W is comparable to in an SLM one, with their mecha-
nisms still under debate. Solid-state cracks may arise from inelastic deformation near low-
angle grain boundaries (LAGBs) (Figure 11a) , which is supported by EBSD data (Figure 
11b) [63]. In laser-based DED, residual stress-induced cracking due to high thermal gra-
dients and porosity are common challenges [61]. Oxygen contamination and its contribu-
tion to microcracking is another challenge. 
Figure 9. SEM image of surface morphology and crack type in SLM-fabricated W [37].

## Page 17

Crystals 2024, 14, 665 17 of 40
Crystals 2024, 14, 665 17 of 44 
 
 
[21,37,41,42], persistent cracks at low oxygen levels indicate other possible influencing 
factors as well [24]. The role of impurities, including oxygen and hydrogen, in SLM on W 
brittleness has not been fully explored. High -speed in situ SLM videos show cracking 
across W’s DBTT, likely due to the increased stress [24]. Such stresses from SLM may only 
be offset by cracking at im purity-contaminated grain boun daries [42,125]. A study by 
Rebesan et al. on SLM-fabricated W specimen s revealed a high crac king tendency [37]. 
Two types of cracks were identified: longitudinal (along the melt-pool center) and trans-
verse (perpendicular to laser-induced surface ripples). Longitudinal cracks are linear and 
30–100 μm long, while transverse cracks are shorter with an “S”-shape along grain bound-
aries (Figure 9). The extensive cracking results from thermal stresses during rapid solidi-
fication or recrystallization (Figure 10a), particularly below the DBTT. Micro-cracks that 
resemble intergranular hot cracking form due to nanopore aggregation at grain bounda-
ries induced by boiling W oxides (WO
x) in the melting pool (Figure 10b) [37]. 
 
Figure 9. SEM image of surface morphology and crack type in SLM-fabricated W [37]. 
 
Figure 10. SEM images of SLM-fabricated W sample, ( a) electrolytically etched displaying a crack 
network; (b) a higher magnification of grain boundaries displaying micro-cracks and pores [37]. 
Cracking in EBM-produced W is comparable to in an SLM one, with their mecha-
nisms still under debate. Solid-state cracks may arise from inelastic deformation near low-
angle grain boundaries (LAGBs) (Figure 11a) , which is supported by EBSD data (Figure 
11b) [63]. In laser-based DED, residual stress-induced cracking due to high thermal gra-
dients and porosity are common challenges [61]. Oxygen contamination and its contribu-
tion to microcracking is another challenge. 
Figure 10. SEM images of SLM-fabricated W sample, (a) electrolytically etched displaying a crack
network; (b) a higher magnification of grain boundaries displaying micro-cracks and pores [37].
Cracking in EBM-produced W is comparable to in an SLM one, with their mechanisms
still under debate. Solid-state cracks may arise from inelastic deformation near low-angle
grain boundaries (LAGBs) (Figure 11a), which is supported by EBSD data (Figure 11b) [63].
In laser-based DED, residual stress-induced cracking due to high thermal gradients and
porosity are common challenges [61]. Oxygen contamination and its contribution to micro-
cracking is another challenge.
Crystals 2024, 14, 665 19 of 44 
 
 
 
Figure 11. A vertical crack at grain boundaries of EBM-fabricated W samples: (a) EBSD in which the 
crack appears as random unindexed pixels, and (b) an optical image [63]. 
Substrate Preheating 
Utilizing a heated substrate plate in PBF processes can potentially mitigate the prob-
lems posed by thermal gradients [19,38]. Preheating is an essential preparatory technique 
implemented before the actual PBF processes to optimize the material’s structure and im-
prove the resultant properties. This method confers several advantages (Table 6). Firstly, 
preheating aids in the mitigation of built-up thermal residual stresses within the material 
to enhance its stability [109]. Moreover, by controlling the melt pool’s cooling rate and the 
thermal gradient during solidification, preheating ensures improved material formation 
and properties. This is particularly critical for W which has a high DBTT; preheating can 
potentially delay or even avert this transition [44]. Additionally, preheating can emulate 
the annealing process, refining W’s microstructure to produce parts with increased den-
sity and fewer microcracks [109]. In some cases, preheating the substrate to temperatures 
close to 1000 °C has proven effective in achieving those outcomes [19]. 
 
Figure 11. A vertical crack at grain boundaries of EBM-fabricated W samples: (a) EBSD in which the
crack appears as random unindexed pixels, and (b) an optical image [63].

## Page 18

Crystals 2024, 14, 665 18 of 40
Overall, micro-cracking in W-based alloys arises due to several mechanisms, which are
as follows. Thermal stress: The high melting point and low thermal expansion coefficient
of W lead to substantial thermal gradients during the rapid heating and cooling cycles in
AM processes. These thermal gradients induce thermal stresses that exceed the material’s
fracture toughness, resulting in micro-cracks. Solidification cracking: During the rapid
solidification in AM, the difference in cooling rates can cause uneven shrinkage and create
tensile stresses in the material. If the material solidifies with significant residual stresses,
it can lead to solidification cracking. The presence of impurities and alloying elements
can intensify this issue by creating brittle phases or weakening grain boundaries. Phase
transformations: Certain tungsten-based alloys undergo phase transformations during the
cooling process. These transformations can involve volume changes that induce additional
stresses within the microstructure, contributing to micro-cracking. The incompatibility
between different phases in terms of their mechanical properties can further complicate
this problem. Porosity and defects: Incomplete melting and impurities can introduce
porosity and other defects within the material. These defects act as stress concentrators
and can initiate micro-cracks under the applied thermal and mechanical loads during the
AM process and subsequent cooling. Grain boundary embrittlement: Alloying elements or
impurities that segregate to grain boundaries can weaken these boundaries and make them
more susceptible to cracking under thermal and mechanical stresses. This embrittlement
can significantly contribute to the formation and propagation of micro-cracks. In addition
to powder and process parameter-related solutions, post-processing techniques like hot
isostatic pressing (HIP) can be explored as viable techniques for closing microcracks in W-
based alloys to enhance the overall mechanical properties of AM-fabricated W components.
Substrate Preheating
Utilizing a heated substrate plate in PBF processes can potentially mitigate the prob-
lems posed by thermal gradients [19,38]. Preheating is an essential preparatory technique
implemented before the actual PBF processes to optimize the material’s structure and
improve the resultant properties. This method confers several advantages (Table 6). Firstly,
preheating aids in the mitigation of built-up thermal residual stresses within the material
to enhance its stability [109]. Moreover, by controlling the melt pool’s cooling rate and the
thermal gradient during solidification, preheating ensures improved material formation
and properties. This is particularly critical for W which has a high DBTT; preheating can
potentially delay or even avert this transition [44]. Additionally, preheating can emulate
the annealing process, refining W’s microstructure to produce parts with increased density
and fewer microcracks [109]. In some cases, preheating the substrate to temperatures close
to 1000 ◦C has proven effective in achieving those outcomes [19].
Elevating substrate temperature beyond W’s DBTT decreases cracking likelihood,
thereby improving the relative density of parts manufactured using AM with W. SLM
processing at increased temperatures from 200 ◦C to 1000 ◦C reduced cracking. Such
findings have been visually represented in the works of Muller et al. (Figure 12) [19], where
they compare the microstructure of SLM-fabricated W with a substrate temperature of
200 ◦C that includes grain boundary cracks (Figure 12a) to that of a SLM-fabricated W
using a substrate temperature of 1000 ◦C without cracks (Figure 12b). In another study,
using ~850 ◦C substrate heating led to minor cracking [32]. Other observations indicate
that temperatures below 400 ◦C are inadequate for preventing microcrack formation [8].
Vrancken et al. also showed that the exact temperature above which cracks in SLM-
fabricated W are eliminated ranged from 500 ◦C to 600 ◦C. The crack-mitigating effect of
preheating persists when scaling up from a single scan track to a hatched area. Without
preheating, a large crack network is formed (Figure 13a), whereas only small, isolated
cracks are found using 500 ◦C preheating (Figure 13b) [44].

## Page 19

Crystals 2024, 14, 665 19 of 40
Table 6. An overview of the effects and benefits of preheating in the AM of W materials.
Preheating Effects Information/Description Reference
Purpose Used before the process to enhance obtained properties
Benefits
- Mitigation of Stress Reduces built-up thermal stresses [102]
- Melt Pool Dynamics Controls cooling rate and thermal gradient during solidification
- Delay/Avoidance of DBTT Delays or prevents DBTT [44]
- Annealing Effect Simulates the annealing process, refining W microstructure [109]
- Enhanced Density and Reduced
Microcracks
Increases part density and reduces microcrack formation, especially
with preheating up to 1000 ◦C in SLM, and more in EBM [19,63]
Optimal Preheating Range
- Observation Low preheating temperatures below 400 ◦C are insufficient for
microcrack mitigation of W materials [8,32]
- General Findings Higher preheating temperatures minimize high DBTT effects and
enhance the density of W parts [19]
Drawbacks of Excessive Preheating
- Recrystallization Extremely high temperatures trigger recrystallization in material [63]
- Grain Vulnerabilities Larger recrystallized grains are prone to intergranular cracking,
acting as pathways for cracks near grain boundaries [60,121]
Crystals 2024, 14, 665 20 of 44 
 
 
Table 6. An overview of the effects and benefits of preheating in the AM of W materials. 
Preheating Effects Information/Description Reference 
Purpose Used before the process to enhance obtained properties 
Benefits 
- Mitigation of Stress Reduces built-up thermal stresses [102] 
- Melt Pool Dynamics Controls cooling rate and thermal gradient during solidification 
- Delay/Avoidance of DBTT Delays or prevents DBTT [44] 
- Annealing Eﬀect Simulates the annealing process, refining W microstructure [109] 
- Enhanced Density and Reduced 
Microcracks 
Increases part density and reduces microcrack formation, especially 
with preheating up to 1000 °C in SLM, and more in EBM [19,63] 
Optimal Preheating Range 
- Observation Low preheating temperatures below 400 °C are insufficient for 
microcrack mitigation of W materials [8,32] 
- General Findings Higher preheating temperatures minimize high DBTT effects and 
enhance the density of W parts [19] 
Drawbacks of Excessive Preheating 
- Recrystallization Extremely high temperatures trigger recrystallization in material [63] 
- Grain Vulnerabilities Larger recrystallized grains are prone to intergranular cracking, 
acting as pathways for cracks near grain boundaries [60,121] 
Elevating substrate temperature beyond W’s DBTT decreases cracking likelihood, 
thereby improving the relative density of parts manufactured using AM with W. SLM 
processing at increased temperatures from 200 °C to 1000 °C reduced cracking. Such find-
ings have been visually represented in the wo rks of Muller et al. (Figure 12) [19], where 
they compare the microstructure of SLM-fabricated W with a substrate temperature of 200 
°C that includes grain boundary cracks (Figur e 12a) to that of a SLM-fabricated W using 
a substrate temperature of 1000 °C without cracks (Figure 12b). In another study, using 
~850 °C substrate heating led to minor cracking [32]. Other observations indicate that tem-
peratures below 400 °C are inadequate for preventing microcrack formation [8]. Vrancken 
et al. also showed that the exact temperature above which cracks in SLM-fabricated W are 
eliminated ranged from 500 °C to 600 °C. The crack-mitigating effect of preheating persists 
when scaling up from a single scan track to a hatched area. Without preheating, a large 
crack network is formed (Figure 13a), whereas only small, isolated cracks are found using 
500 °C preheating (Figure 13b) [44]. 
 
Figure 12. Effect of temperature on SLM-fabricated pure W cubes: (a) optical image of a cross-section at 
200 °C, (b) optical image of a cross-section at 1000 °C [19]. Reproduced with permission from Elsevier. 
Figure 12. Effect of temperature on SLM-fabricated pure W cubes: ( a) optical image of a cross-
section at 200 ◦C, (b) optical image of a cross-section at 1000 ◦C [19]. Reproduced with permission
from Elsevier.
Crystals 2024, 14, 665 21 of 44 
 
 
 
Figure 13. Crack formations in SLM-fabricated W samples: ( a) crack pattern of a 1 by 2 mm area 
scanned using hatch spacing h = 25 μm, and (b) absence of cracks in a 1 by 2 mm area scanned using 
500 °C preheating [44]. Reproduced with permission from Elsevier. 
In EBM processing of W, preheating each layer up to 1800 °C may be required to 
fabricate high density parts [100]. Ellis et al. observed a lower crack density at 1500 °C 
(corresponding to a preheating input energy of 735 J/mm2) than at 1100 °C (corresponding 
to a preheating energy input of 325 J/mm 2), as shown in Figure 14a,b [63]. This led them 
to postulate that the higher preheat energy suppresses cracking by raising the ambient 
temperature of the build [63]. While preheating is beneficial, overdoing it can have detri-
mental effects. Excessive preheating temper atures can induce undesirable recrystalliza-
tion processes within W materials [63]. The fo rmation of larger recrystallized grains, a 
consequence of intense preheating, makes the material susceptible to intergranular crack-
ing [60,121]. These grains can then become crack-initiation points, especially in regions 
close to or on the grain boundaries [60,121] . As a result, extremely high preheating tem-
peratures can be counterintuitive and diminish the quality of the product [63]. 
Residual stresses in W-AM arise from W’s high melting point and low thermal ex-
pansion coefficient. These stresses are genera ted by the complex thermal cycles experi-
enced during AM processes, including thermal gradients, solidification stresses, phase 
transformations, and mechanical constraints. W parts undergo rapid heating and cooling, 
leading to steep thermal gradients that cause differential expansion and contraction. This 
results in tensile and compressive stresses wi thin different regions of the part. Further-
more, as the molten W solidifies, the materi al shrinks. Non-uniform solidification and 
cooling rates across the part introduce residual stresses due to uneven shrinkage. Addi-
tionally, W-based materials may experience phase transformations during cooling, in-
volving volume changes that generate further stresses. The build platform and surround-
ing material can also constrain the part, leading to residual stresses as the material con-
tracts upon cooling. Mitigation strategies involve controlled cooling post-deposition to 
minimize thermal stresses through preheating, optimizing scan strategies, and designing 
effective support structures. 
Figure 13. Crack formations in SLM-fabricated W samples: ( a) crack pattern of a 1 by 2 mm area
scanned using hatch spacing h = 25 µm, and (b) absence of cracks in a 1 by 2 mm area scanned using
500 ◦C preheating [44]. Reproduced with permission from Elsevier.
In EBM processing of W, preheating each layer up to 1800 ◦C may be required to
fabricate high density parts [100]. Ellis et al. observed a lower crack density at 1500 ◦C

## Page 20

Crystals 2024, 14, 665 20 of 40
(corresponding to a preheating input energy of 735 J/mm2) than at 1100 ◦C (corresponding
to a preheating energy input of 325 J/mm2), as shown in Figure 14a,b [63]. This led them to
postulate that the higher preheat energy suppresses cracking by raising the ambient tem-
perature of the build [63]. While preheating is beneficial, overdoing it can have detrimental
effects. Excessive preheating temperatures can induce undesirable recrystallization pro-
cesses within W materials [63]. The formation of larger recrystallized grains, a consequence
of intense preheating, makes the material susceptible to intergranular cracking [ 60,121].
These grains can then become crack-initiation points, especially in regions close to or on
the grain boundaries [60,121]. As a result, extremely high preheating temperatures can be
counterintuitive and diminish the quality of the product [63].
Crystals 2024, 14, 665 22 of 44 
 
 
 
Figure 14. Cracking in EBM-fabricated W blocks built with nominally identical melt parameters: (a) 
and (b) XY sections, approximate elevations 9 mm, (c,d) XZ sections, approximately at the midline. 
The build shown in (a,c) did not crack; the build in (b,d) exhibited cracking [63]. 
Thermal management is crucial in W-AM and can be addressed through various 
strategies during the design, AM processing, and post-AM processes. Enhanced support 
structures specifically designed for W-AM can effectively dissipate heat and stabilize the 
part. Preheating the build platform, optimizing scan strategies, and adjusting process pa-
rameters to control cooling rates help maintain a more uniform temperature distribution, 
thereby reducing thermal gradients during th e build cycle. Post-processing heat treat-
ments, such as annealing or HIP, are employed to relieve residual stresses and improve 
the microstructural integrity of AM-produce d W components, significantly reducing in-
ternal stresses and enhancing mechanical properties. 
Ledford et al. [100] employed a comprehens ive experimental design to establish an 
optimal processing window for achieving high-density, crack-free pure W using the EBM 
method. They successfully attained full density in select fabricated samples by preheating 
the substrate to 1800 °C and optimizing the other parameters such as scan speed and layer 
thickness. The as-fabricated W samples exhibited subgrains approximately 10–20 μm in 
size, with low-angle grain boundaries characterized by high dislocation densities ranging 
from approximately 1015 to 1016 per square meter in certain instances. High-temperature 
tensile testing revealed significant tensile an isotropy attributed to inherent crystallo-
graphic variations. Yield strength ranged from 85 to 202 MPa, while tensile strength 
ranged from 121 to 274 MPa, closely resembling annealed tungsten properties. 
Similarly, Antusch et al. [126] utilized EBM to manufacture pure W components for 
nuclear fusion reactors, achieving 99.8% density and a crack-free microstructure charac-
terized by elongated columnar grains. The absence of microcracks was attributed to re-
duced thermal stress facilitated by optimized pre-heating strategies during EBM and the 
absence of oxide precipitates due to manufa cturing in a vacuum environment. This re-
sulted in a stable melt pool during the fabrication process. Tensile testing conducted be-
tween 600 °C and 1000 °C demonstrated ductile behavior with a total elongation of 80% 
Figure 14. Cracking in EBM-fabricated W blocks built with nominally identical melt parameters:
(a,b) XY sections, approximate elevations 9 mm, (c,d) XZ sections, approximately at the midline. The
build shown in (a,c) did not crack; the build in (b,d) exhibited cracking [63].
Residual stresses in W-AM arise from W’s high melting point and low thermal expan-
sion coefficient. These stresses are generated by the complex thermal cycles experienced
during AM processes, including thermal gradients, solidification stresses, phase transfor-
mations, and mechanical constraints. W parts undergo rapid heating and cooling, leading
to steep thermal gradients that cause differential expansion and contraction. This results
in tensile and compressive stresses within different regions of the part. Furthermore, as
the molten W solidifies, the material shrinks. Non-uniform solidification and cooling rates
across the part introduce residual stresses due to uneven shrinkage. Additionally, W-based
materials may experience phase transformations during cooling, involving volume changes
that generate further stresses. The build platform and surrounding material can also
constrain the part, leading to residual stresses as the material contracts upon cooling. Miti-
gation strategies involve controlled cooling post-deposition to minimize thermal stresses
through preheating, optimizing scan strategies, and designing effective support structures.
Thermal management is crucial in W-AM and can be addressed through various
strategies during the design, AM processing, and post-AM processes. Enhanced support

## Page 21

Crystals 2024, 14, 665 21 of 40
structures specifically designed for W-AM can effectively dissipate heat and stabilize the
part. Preheating the build platform, optimizing scan strategies, and adjusting process
parameters to control cooling rates help maintain a more uniform temperature distribution,
thereby reducing thermal gradients during the build cycle. Post-processing heat treatments,
such as annealing or HIP , are employed to relieve residual stresses and improve the
microstructural integrity of AM-produced W components, significantly reducing internal
stresses and enhancing mechanical properties.
Ledford et al. [100] employed a comprehensive experimental design to establish an
optimal processing window for achieving high-density, crack-free pure W using the EBM
method. They successfully attained full density in select fabricated samples by preheating
the substrate to 1800 ◦C and optimizing the other parameters such as scan speed and layer
thickness. The as-fabricated W samples exhibited subgrains approximately 10–20 µm in
size, with low-angle grain boundaries characterized by high dislocation densities ranging
from approximately 1015 to 1016 per square meter in certain instances. High-temperature
tensile testing revealed significant tensile anisotropy attributed to inherent crystallographic
variations. Yield strength ranged from 85 to 202 MPa, while tensile strength ranged from
121 to 274 MPa, closely resembling annealed tungsten properties.
Similarly , Antusch et al. [126] utilized EBM to manufacture pure W components for
nuclear fusion reactors, achieving 99.8% density and a crack-free microstructure characterized
by elongated columnar grains. The absence of microcracks was attributed to reduced thermal
stress facilitated by optimized pre-heating strategies during EBM and the absence of oxide
precipitates due to manufacturing in a vacuum environment. This resulted in a stable melt
pool during the fabrication process. Tensile testing conducted between 600◦C and 1000 ◦C
demonstrated ductile behavior with a total elongation of 80% along the building direction and
DBTT ranging from 700◦C to 900 ◦C. Thermal conductivity measurements were comparable
with values in the literature for conventionally produced W counterparts. These studies
highlight the potential of EBM as a promising method for processing W (Figure 15).
Crystals 2024, 14, 665 23 of 44 
 
 
along the building direction and DBTT ranging from 700 °C to 900 °C. Thermal conduc-
tivity measurements were comparable with values in the literature for conventionally pro-
duced W counterparts. These studies highlight the potential of EBM as a promising 
method for processing W (Figure 15). 
 
Figure 15. Pure W components fabricated using EBM: ( a) complex geometrical parts [126], ( b) a 
diverter tile and mesh demonstration piece, along with a mockup illustrating the potential diverter 
geometry featuring tungsten plasma-facing tiles [100], and (c) the integration of W-EBM with copper 
infiltration tailored for fusion applications [126]. 
4. Additively Manufactured W Alloys and Composites 
Amongst the strategies to mitigate the challenges discussed in the preceding sections, 
alloying is a particularly useful approach. Alloying has been shown to impart multifac-
eted effects on the properties and behavior of W in AM contexts. Several W alloys have 
been studied in the realm of AM. Since W is often insoluble or immiscible with other ele-
ments, its alloyed materials with some elements , have been referred to as composites in 
some studies. In this review, we consider al l combinations of W wi th other elements as 
alloys and refer to combinations of W with ceramic materials (such as carbides and oxides) 
as composites (Table 7). The AM-fabricated alloy groups that have been studied include 
W-Re [127–129], W-Ni [74,130], W-Ni-Fe [71, 72,75,77,80,83,85,103,131–133], W-Ni-Fe-Co 
[134], W-Ni-Fe-Cu [80], W-Ni-Cu [4,135], W-Cu [4,6,136–138], W-Cu-Sn [139], W-Ta 
[8,140–143], W-Ta-Re [144,145], W-Nb [110], W-Fe [73,146], W-Mo [147], and W-Cr [86]. 
W-based matrix composites with different ceramic phases such as TiC [148,149], ZrC [120], 
TaC [150], La
2O3 [44], CeO2 [44], a mix of La2O3–ZrO2–Y2O3 [44], and Y2O3 [42,61] have also 
been fabricated via AM methods. 
 
Figure 15. Pure W components fabricated using EBM: ( a) complex geometrical parts [ 126], (b) a
diverter tile and mesh demonstration piece, along with a mockup illustrating the potential diverter
geometry featuring tungsten plasma-facing tiles [100], and (c) the integration of W-EBM with copper
infiltration tailored for fusion applications [126].

## Page 22

Crystals 2024, 14, 665 22 of 40
4. Additively Manufactured W Alloys and Composites
Amongst the strategies to mitigate the challenges discussed in the preceding sections,
alloying is a particularly useful approach. Alloying has been shown to impart multifaceted
effects on the properties and behavior of W in AM contexts. Several W alloys have been
studied in the realm of AM. Since W is often insoluble or immiscible with other elements,
its alloyed materials with some elements, have been referred to as composites in some
studies. In this review, we consider all combinations of W with other elements as alloys
and refer to combinations of W with ceramic materials (such as carbides and oxides) as
composites (Table 7). The AM-fabricated alloy groups that have been studied include W-
Re [127–129], W-Ni [74,130], W-Ni-Fe [71,72,75,77,80,83,85,103,131–133], W-Ni-Fe-Co [134],
W-Ni-Fe-Cu [80], W-Ni-Cu [4,135], W-Cu [4,6,136–138], W-Cu-Sn [139], W-Ta [8,140–143],
W-Ta-Re [144,145], W-Nb [110], W-Fe [73,146], W-Mo [147], and W-Cr [86]. W-based matrix
composites with different ceramic phases such as TiC [ 148,149], ZrC [ 120], TaC [ 150],
La2O3 [44], CeO2 [44], a mix of La2O3–ZrO2–Y2O3 [44], and Y2O3 [42,61] have also been
fabricated via AM methods.
Table 7. Additively manufactured W-based alloys and W-matrix composites.
Materials References
W Alloys
W-1–25%Re [128,151]
W-0.1–40%Ni [74,130]
W-7%Ni-3%Fe [71,72,75,77,80,83,85,103,131,132]
W-4.6%Ni-2.4%Fe [133]
W-6%Ni-2%Fe-2%Co [134]
W-12%Ni-4%Fe-4%Co [134]
W-18%Ni-6%Fe-6%Co [134]
W-8.7%(Ni-Fe-Cu) [80]
W-5%Ni-15%Cu [3]
W-5%Ni-25%Cu [135]
W-10%Ni-10%Cu [135]
W-10–40%Cu [4,6,136–138]
W-20%(Cu10Sn) [139]
W-1–12%Ta [8,140–143]
W-14.8%Ta-17.2%Re [144,145]
W-5%Nb [110]
W-14–79%Fe [73,146]
W-50%Mo [147]
W-12.85%Cr [86]
W Matrix Composites
W-0.5–2.5%TiC [148,149]
W-0.5%ZrC [120]
W-5%TaC [150]
W-5%La2O3 [44]
W-2%CeO2 [44]
W-1.75%La2O3-0.12%ZrO2-0.12%Y2O3 [44]
Y2O3 [42,61]
A comprehensive review of the impact of alloying elements and ceramic particles
on mitigating the challenges associated with the AM of W-based materials, as well as
their microstructure and mechanical properties (Table 8), reveals several key purposes for
these additions. Alloying elements and ceramic particles are introduced for the following
purposes: to lower the melting point of W to enhance densification, for the modification of
laser absorption, reduction in thermal conductivity of W, and reduction in melt viscosity
to enhance densification, to form binding phases to enhance densification, improve grain
boundary strengthening, modify grain structure, enhance grain boundary cohesion and
improve pore distribution to enhance mechanical properties and to mitigate microcracking,
to strengthen through secondary dispersed or precipitated phases to restrict grain boundary

## Page 23

Crystals 2024, 14, 665 23 of 40
movement and enhance mechanical properties to mitigate microcracking and enhance low-
temperature ductility, increasing stacking fault energy, boosting dislocation mobility to
improve ductility and lower DBTT, and for other purposes such as self-passivating behavior
and the reduction in fuzz formation in the nuclear application.
Table 8. An overview of the impact of alloying elements and dispersion particles on mitigating the
challenges of the AM of W-based materials and on their microstructure and mechanical properties.
Effects on
W-AM
Alloying
Element(s) Specifics/Notes Ref
Enhanced
Densification
Ni, Fe, Co, Mo,
Re, Ta, etc.
Due to the lower melting points of alloying phases densification is promoted.
The melting of Ni, Fe, and Co enhances the dissolution of W particles. [19,41,74,86,130,134–138]
Cu
Occurs due to the role of alloying elements in forming binding phases. Good wetting
allows the molten Cu to spread and adhere strongly to the W particles. Surface smoothing
also contributes to a denser final structure.
[4,6]
Ni, Cu, Ta,
Fe, Mo
Modifications in laser absorption, melt viscosity, and fluidity. Ni works better than Cu.
Ta increases recrystallization temperature and decreases thermal conductivity of WNi and
Fe for improves wettability of W.
[4,6,8,74,130,135–138,140–143]
Microcrack
Mitigation
Re, Ta, Nb, Mo,
Cr, Ti, Ir
Re lowers the DBTT of W alloys, significantly reducing their tendency to crack during
AM processes.
Ta forms a special cellular structure that keeps tiny air pockets (nanopores) separated from
each other. This reduces the overall tendency of the material to crack. Ta also oxidizes more
easily than W during the building process. As a result, fewer nanopores form in the final W
alloy, and the risk of microcracks is reduced.
Nb improves the intergranular bonding of the alloy via solid solution strengthening.
Cr forms the Cr-rich Cr-W phase and causes grain refinement.
Ti (in conventional manufacturing of W) gives rise to a heterogeneous chemical distribution
to prevent the nanostructured microstructure from coarsening.
Ir (proved in conventional manufacturing of W) strengthens grain boundary cohesion,
optimizes dislocation mobility, and reduces cracking.
Adding some of these elements prevents the formation of tiny cracks (microcracks) in the
building process. In general, W solidifies first, causing stress within the material. Alloying
elements helps lessen this stress by essentially acting as a buffer.
They also result in grain refinement of W, improved grain boundary strengthening,
modified grain structure, and better pore distribution.
[4,44,48,86,110,127–129,141–
144,152,153]
Re
W, when alloyed with Re, showed a reduced DBTT and increased low-temperature ductility.
This improvement is attributed to Re’s high solubility in W and its capability as a solution
hardener. The other benefits include the enhancement of grain boundary cohesion, boosting
dislocation mobility and lowering DBTT, and reducing embrittlement.
[127–129]
TiC, ZrC, TaC,
Y2O3, La2O3, etc.
Y2O3 leads to more LAGBs and reduces cracking.
W–Y2O3 has a better low-temperature ductility and suppresses cracking.
La2O3 not only bolsters radiation resistance but also provides an indirect solution to these
interstitial contamination challenges.
ZrC nanoparticles decrease crack density due to finer grains and increased grain-boundary
length. They also capture oxygen to form ZrOy, reducing embrittlement.
TaC supports the formation of W2C phases within the material, further increasing the
overall strength and crack resistance. It also reacts with any oxygen present, forming TaOx,
effectively removing oxygen from the system.
TiC enhances hardness.
[42,47,120,141,150]
Mechanical
Properties
Adjustments
Fe
Strengthening by the formation of secondary or precipitated phases during AM processes.
The non-equilibrium solidification between Fe and W allows for the potential formation of
intermetallic phases like Fe7W6 and Fe2W, improving the hardness.
[73,144,146]
Ni Tensile strength and fracture toughness enhancement. [74,130]
Ti, Ir, Hf
Increase in recrystallization temperatures.
Potent carbide formers mitigate the adverse effects of carbon impurities on the
alloy’s mechanics.
Elevate the recrystallization temperatures and improve W’s low-temperature ductility and
high-temperature strength.
Ir can improve mechanical properties by increasing grain boundary cohesion.
[152–156]
Ta, Nb, and other
group V and IV
transition metals
Improvement of intrinsic ductility of W alloys.
Ta can increase hardness.
Solid solution strengthening by Nb.
[110,141–144]
Others
Ta Fuzz formation reduction, especially during He plasma irradiation. [140]
Cr and Y Self-passivation behavior for high-temperature applications. [157]
In the subsequent sections, we will closely examine some of these alloying strategies.
4.1. Alloying for Enhanced Densification
Alloying with metals that have lower melting points is a strategy to decrease the
overall melting point of W. But it is important for this to be carried out in moderation to

## Page 24

Crystals 2024, 14, 665 24 of 40
ensure that the intrinsic high-temperature properties of the W alloys are retained [19,41].
W alloys behave differently when melted compared to pure W. The alloying elements can
form phases with lower melting points than pure W, aiding in the binding and dissolution
of W particles [4]. These elements can also affect melt viscosity and fluidity during AM,
especially in SLM. Alloying elements can lead to unique solidification behaviors, leading
to improved grain structures, and reduced stresses, among other benefits. Overall, W
alloys generally exhibit superior AM part quality compared to the use of pure W [60,61]. A
major consequence observed is the enhanced densification of the W matrix. Most alloying
elements, including Ni, Fe, Co, Cu, and Re contribute to this phenomenon. The basis for
this enhanced densification is the lower melting points of these alloying elements compared
to W and the possibility of melting at lower energy inputs and faster scan rates. In the
context of the SLM technique, the melting of Ni, Fe, and Co has been noted to expedite the
dissolution of W particles [134,135], leading to a more consolidated alloy [6,130,134,135].
Cu, as an alloying element, has been studied to reveal its distinct role in W densification
during AM [4,6,136–138]. The significance of Cu lies in its ability to form binding phases
with W. The molten state of Cu ensures the effective wetting of W particles, while W
particles concurrently undergo surface smoothing. Both these effects foster the increased
densification of the W-Cu composite [4].
The alloying elements Ni, Cu, and Ta introduce significant changes in the AM process
by altering parameters such as laser absorption, melt viscosity, and fluidity [4,6,8,74,130,135–
138,140–143]. Among these alloying elements, Ni demonstrates superior efficacy over Cu
in such modifications, primarily due to its lower thermal conductivity [42]. The use of Ta
comes with its benefits, including the elevation of the recrystallization temperature and
a decrement in thermal conductivity [ 4,130]. Re plays a multifaceted role in the AM of
W alloys, one of which is its contribution to densification. The addition of Re allows for
parts with higher relative density to be achieved (relative to pure W) (Figure 16a) [ 127].
The addition of alloying elements such as Cu, Ni, Fe, Mo, and Cr can facilitate higher
densification in AM W materials (Figure 16b). Obtaining a relative density of more than
95% in SLM-fabricated unalloyed W is usually difficult, but precise scanning parameter
adjustments, preheating, and the use of optimized starting materials have resulted in
achieving relative densities over 98%. The EBM technique for unalloyed W fabrication has
been shown to achieve relative densities up to 99.5%.
Crystals 2024, 14, 665 27 of 44 
 
 
than 95% in SLM-fabricated unalloyed W is usually difficult, but precise scanning param-
eter adjustments, preheating, and the use of optimized starting materials have resulted in 
achieving relative densities over 98%. The EBM technique for unalloyed W fabrication has 
been shown to achieve relative densities up to 99.5%. 
 
Figure 16. (a) Achieved relative (% of theoretical) desnity for SLM-manufactured W-5%Re, W-
25%Re alloys, and unalloyed W vers us energy density [127], and ( b) obtained relative density of 
alloyed and unalloyed W fabricated via different AM techniques. 
4.2. Alloying and Ceramic Dispersions for Microcrack Mitigation 
4.2.1. Alloying Elements 
Alloying is a very useful strategy for reducing interstitial contamination. The intro-
duction of specific alloying elements in W during AM has been shown to substantially 
impact the microcrack mitigation process, which is achieved through mechanisms such as 
grain structure modification, improved pore distribution, grain boundary strengthening, 
stress reduction, a decrease in DBTT, and reduced nanopore formation. The addition of 
Ta induces a cellular structure that spreads the nanopore distribution, culminating in an 
80% reduction in cracking [48,143] (Figure 17). Furthermore, the role of Ta in reducing 
oxygen sensitivity during solidification, courtesy of its in situ oxidation, is essential in 
alleviating microcracks in the W alloy [48,141–143]. 
Nb is beneficial as an alloying element due to solid solution strengthening, which 
strengthens intergranular bonding to provide an effective countermeasure against mi-
crocracking [110]. Alloying W with Re offers promising outcomes. Apart from its contri-
bution to enhancing densification, the resultant alloys show enhanced grain boundary co-
hesion and an increased mobility of screw dislocations, significantly altering their me-
chanical behaviors. The addition of Re significantly reduces the ease at which W alloy 
cracks during the manufacturing process due to the significant lowering of the DBTT 
[127–129]. Eckley et al. [127] used EBSD maps and optical microscopy images to show 
significant cracking in pure W parts fabricated by SLM (Figure 18). Cracking increased 
with density and followed scan tracks, branch ing at 45-degree angles, and longitudinal 
cracking traced columnar grain boundaries in the build direction (Figure 18a,b). The in-
troduction of 5 wt.% Re failed to effectively mitigate the observed cracking (Figure 18c,d). 
However, an increase in Re content to 25 wt.% resulted in a significant reduction in both 
surface and longitudinal cracking, and the ch aracteristic horizontal and 45-degree angle 
cracking behaviors were notably minimized (F igure 18e,f). This improvement can be at-
tributed to the lowered DBTT of W due to Re alloying, decreasing brittleness during cool-
ing. Despite these enhancements, some cracking persisted. This study shows Re alloying 
to be effective in enhancing the crack resistance of W-AM. Notably, conventional fabrica-
tion has demonstrated the profound influence of Re, with W alloys containing 26 wt.% Re 
exhibiting a DBTT as low as −101 °C [60,155,156]. 
Figure 16. (a) Achieved relative (% of theoretical) desnity for SLM-manufactured W-5%Re, W-25%Re
alloys, and unalloyed W versus energy density [127], and (b) obtained relative density of alloyed and
unalloyed W fabricated via different AM techniques.
4.2. Alloying and Ceramic Dispersions for Microcrack Mitigation
4.2.1. Alloying Elements
Alloying is a very useful strategy for reducing interstitial contamination. The intro-
duction of specific alloying elements in W during AM has been shown to substantially

## Page 25

Crystals 2024, 14, 665 25 of 40
impact the microcrack mitigation process, which is achieved through mechanisms such as
grain structure modification, improved pore distribution, grain boundary strengthening,
stress reduction, a decrease in DBTT, and reduced nanopore formation. The addition of Ta
induces a cellular structure that spreads the nanopore distribution, culminating in an 80%
reduction in cracking [48,143] (Figure 17). Furthermore, the role of Ta in reducing oxygen
sensitivity during solidification, courtesy of its in situ oxidation, is essential in alleviating
microcracks in the W alloy [48,141–143].
Crystals 2024, 14, 665 28 of 44 
 
 
 
Figure 17. Schematic illustration of how adding Ta affects the formation of nanopores during SLM 
of W and W-Ta alloys [48]. 
 
Figure 17. Schematic illustration of how adding Ta affects the formation of nanopores during SLM of
W and W-Ta alloys [48].
Nb is beneficial as an alloying element due to solid solution strengthening, which
strengthens intergranular bonding to provide an effective countermeasure against microc-
racking [110]. Alloying W with Re offers promising outcomes. Apart from its contribution
to enhancing densification, the resultant alloys show enhanced grain boundary cohesion
and an increased mobility of screw dislocations, significantly altering their mechanical
behaviors. The addition of Re significantly reduces the ease at which W alloy cracks during
the manufacturing process due to the significant lowering of the DBTT [127–129]. Eckley
et al. [127] used EBSD maps and optical microscopy images to show significant cracking in
pure W parts fabricated by SLM (Figure 18). Cracking increased with density and followed
scan tracks, branching at 45-degree angles, and longitudinal cracking traced columnar
grain boundaries in the build direction (Figure 18a,b). The introduction of 5 wt.% Re failed
to effectively mitigate the observed cracking (Figure 18c,d). However, an increase in Re
content to 25 wt.% resulted in a significant reduction in both surface and longitudinal
cracking, and the characteristic horizontal and 45-degree angle cracking behaviors were
notably minimized (Figure 18e,f). This improvement can be attributed to the lowered DBTT
of W due to Re alloying, decreasing brittleness during cooling. Despite these enhancements,
some cracking persisted. This study shows Re alloying to be effective in enhancing the
crack resistance of W-AM. Notably, conventional fabrication has demonstrated the pro-
found influence of Re, with W alloys containing 26 wt.% Re exhibiting a DBTT as low as
−101 ◦C [60,155,156].

## Page 26

Crystals 2024, 14, 665 26 of 40
Crystals 2024, 14, 665 28 of 44 
 
 
 
Figure 17. Schematic illustration of how adding Ta affects the formation of nanopores during SLM 
of W and W-Ta alloys [48]. 
 
Crystals 2024, 14, 665 29 of 44 
 
 
 
Figure 18. EBSD maps and optical microscopy images of W cubes made using SLM with different 
Re contents: (a,b) pure W cubes, (c,d) W with 5 wt.% Re cubes, and ( e,f) W with 25 wt.% Re cubes. 
The laser power, hatch spacing, and scan sp eed were all kept constant at 200 W, 50 μm, and 400 
mm/s, respectively. The build direction is also indicated in the image [127]. 
The inherent characteristics of alloying el ements relieve stress by compensating for 
the shrinkage experienced as W solidifies (a direct consequence of its elevated melting 
point). This phenomenon plays a direct role in minimizing microcracking [110]. Further 
contributions from Cr result in grain refinement, indirectly aiding in crack mitigation. Cr 
induces a Cr-rich Cr-W phase to optimize grain refinement [86]. In conventional fabrica-
tion techniques of W-based alloys, adding Ti as an alloying element creates a heterogene-
ous chemical distribution, stalling the coarsening of nanostructured microstructures [152], 
whereas adding Ir strengthens grain boundary cohesion, optimizes dislocation mobility, 
and subsequently deters crack formation [153]. These alloying additions (Ti and Ir) may 
be beneficial in materials design for AM as well. 
4.2.2. Ceramic Dispersions (W Composites) 
Incorporating ceramic particles in W has been shown to enhance composite re-
sistance to cracking. W’s challenges with oxide retention and the power balling effect are 
clear indicators of oxidation difficulties, but solutions are on hand. The integration of 
La
2O3 not only bolsters radiation resistance but also provides an indirect solution to the 
problem of interstitial contamination. Innova tions like nanopore segregation have been 
introduced, inducing and identifying crack initiation. Achieving a high theoretical density 
range of 96–98.5%, combined with the optimal conditions characterized by elevated laser 
energy density and low oxygen levels, represent meaningful advancements in countering 
these challenges. 
W-Y2O3 composites offer a refined grain size and commendable low-temperature 
ductility [42]. Based on EBSD grain size, and grain misorientation distribution studies of 
W-Y2O3 composites, the use of nano-sized Y 2O3 particles leads to grain refinement and a 
greater occurrence of LAGBs. The concomitant reduction in HAGBs (which are more sus-
ceptible to cracking) markedly reduces cracking in the resulting W composites (Figure 19) 
[42]. Introducing micron-sized Y2O3 dispersions into W does not lead to grain refinement, 
although this increases the fraction of LAGBs (Figure 19c,d). However, when nano-sized 
Y
2O3 dispersions are used in the composite, the fraction of LAGBs and grain size are both 
reduced (Figure 19e,f). 
Figure 18. EBSD maps and optical microscopy images of W cubes made using SLM with different Re
contents: (a,b) pure W cubes, (c,d) W with 5 wt.% Re cubes, and (e,f) W with 25 wt.% Re cubes. The
laser power, hatch spacing, and scan speed were all kept constant at 200 W, 50µm, and 400 mm/s,
respectively. The build direction is also indicated in the image [127].
The inherent characteristics of alloying elements relieve stress by compensating for
the shrinkage experienced as W solidifies (a direct consequence of its elevated melting
point). This phenomenon plays a direct role in minimizing microcracking [110]. Further
contributions from Cr result in grain refinement, indirectly aiding in crack mitigation. Cr
induces a Cr-rich Cr-W phase to optimize grain refinement [86]. In conventional fabrication
techniques of W-based alloys, adding Ti as an alloying element creates a heterogeneous
chemical distribution, stalling the coarsening of nanostructured microstructures [ 152],
whereas adding Ir strengthens grain boundary cohesion, optimizes dislocation mobility,
and subsequently deters crack formation [153]. These alloying additions (Ti and Ir) may be
beneficial in materials design for AM as well.

## Page 27

Crystals 2024, 14, 665 27 of 40
4.2.2. Ceramic Dispersions (W Composites)
Incorporating ceramic particles in W has been shown to enhance composite resis-
tance to cracking. W’s challenges with oxide retention and the power balling effect are
clear indicators of oxidation difficulties, but solutions are on hand. The integration of
La2O3 not only bolsters radiation resistance but also provides an indirect solution to the
problem of interstitial contamination. Innovations like nanopore segregation have been
introduced, inducing and identifying crack initiation. Achieving a high theoretical density
range of 96–98.5%, combined with the optimal conditions characterized by elevated laser
energy density and low oxygen levels, represent meaningful advancements in countering
these challenges.
W-Y2O3 composites offer a refined grain size and commendable low-temperature
ductility [42]. Based on EBSD grain size, and grain misorientation distribution studies
of W-Y2O3 composites, the use of nano-sized Y 2O3 particles leads to grain refinement
and a greater occurrence of LAGBs. The concomitant reduction in HAGBs (which are
more susceptible to cracking) markedly reduces cracking in the resulting W composites
(Figure 19) [42]. Introducing micron-sized Y2O3 dispersions into W does not lead to grain
refinement, although this increases the fraction of LAGBs (Figure 19c,d). However, when
nano-sized Y2O3 dispersions are used in the composite, the fraction of LAGBs and grain
size are both reduced (Figure 19e,f).
Crystals 2024, 14, 665 30 of 44 
 
 
 
Figure 19. EBSD grain size distribution for SLM-fabricated samples: (a,b) pure W, (c,d) W-Y2O3 (mi-
cron-sized), and (e,f) W-Y2O3 (nano-sized) [42]. 
Li et al.’s study identified zirconium carbide (ZrC) as a crucial ceramic particle [120]. 
They showed that W-ZrC samples showed a remarkable reduction in crack density com-
pared to pure W, showing fewer and more dispersed cracks in W-ZrC (Figure 20a,b). The 
images also reveal that , while pure W had long and densely distributed cracks, W -ZrC 
had shorter and sparser cracks (Figure 20c,d). This improved crack resistance is attributed 
to secondary-phase nanoparticles in W -ZrC, which refined the grain structure and cap-
tured oxygen impurities to hinder crack propagation. Achieving a fully uniform grain 
structure would require further efforts to ensure an even ZrC distribution. Li et al.’s study 
highlighted ZrC’s role in reducing crack density, promoting finer grains, and extending 
Figure 19. Cont.

## Page 28

Crystals 2024, 14, 665 28 of 40
Crystals 2024, 14, 665 30 of 44 
 
 
 
Figure 19. EBSD grain size distribution for SLM-fabricated samples: (a,b) pure W, (c,d) W-Y2O3 (mi-
cron-sized), and (e,f) W-Y2O3 (nano-sized) [42]. 
Li et al.’s study identified zirconium carbide (ZrC) as a crucial ceramic particle [120]. 
They showed that W-ZrC samples showed a remarkable reduction in crack density com-
pared to pure W, showing fewer and more dispersed cracks in W-ZrC (Figure 20a,b). The 
images also reveal that , while pure W had long and densely distributed cracks, W -ZrC 
had shorter and sparser cracks (Figure 20c,d). This improved crack resistance is attributed 
to secondary-phase nanoparticles in W -ZrC, which refined the grain structure and cap-
tured oxygen impurities to hinder crack propagation. Achieving a fully uniform grain 
structure would require further efforts to ensure an even ZrC distribution. Li et al.’s study 
highlighted ZrC’s role in reducing crack density, promoting finer grains, and extending 
Figure 19. EBSD grain size distribution for SLM-fabricated samples: ( a,b) pure W, (c,d) W-Y2O3
(micron-sized), and (e,f) W-Y2O3 (nano-sized) [42].
Li et al.’s study identified zirconium carbide (ZrC) as a crucial ceramic particle [120].
They showed that W-ZrC samples showed a remarkable reduction in crack density com-
pared to pure W, showing fewer and more dispersed cracks in W-ZrC (Figure 20a,b). The
images also reveal that, while pure W had long and densely distributed cracks, W-ZrC
had shorter and sparser cracks (Figure 20c,d). This improved crack resistance is attributed
to secondary-phase nanoparticles in W-ZrC, which refined the grain structure and cap-
tured oxygen impurities to hinder crack propagation. Achieving a fully uniform grain
structure would require further efforts to ensure an even ZrC distribution. Li et al.’s study
highlighted ZrC’s role in reducing crack density, promoting finer grains, and extending
grain boundaries. Their bright field TEM, HRTEM (high-resolution transmission electron
microscopy), and high-angle annular dark field images (Figure 21a–c) along with EDS
chemical maps (Figure 21d–h) at various magnifications, and the SAEDP (selected-area elec-
tron diffraction pattern) of selected nanoparticles (Figure 21f) provide compelling evidence
of ZrC’s capacity to capture and bind oxygen to form ZrOy particles. This mechanism is a
highly effective means of mitigating embrittlement [60,120].
Tantalum carbide (TaC) particles in W also play an important role in crack mitiga-
tion. This is achieved via the dual action of initiating in situ W 2C phase formations and
promoting oxygen consumption through TaOx formation, which collectively suppresses
cracks [141,150]. Titanium carbide (TiC), while predominantly increasing hardness, may
indirectly improve crack resistance due to the improved mechanical properties of the com-
posite [42,47,141,150]. Hafnium carbide (HfC) dispersion in conventionally fabricated W
alloys has provided excellent thermal stability and tensile properties of composites [154,155].
This can be a useful feature to have for materials design in the AM of W as well.
4.3. Alloying and Ceramic Dispersions for Mechanical Properties Adjustments
Besides mitigating the problems discussed above, alloying confers additional benefits.
Fe integration in W alloys during AM strengthens the resulting material due to the for-
mation of secondary or precipitated phases. This is due to the possible peritectic reaction
between Fe and W during non-equilibrium solidification, leading to the emergence of
intermetallic phases such as Fe7W6 and Fe2W. This formation significantly increases the
hardness of the W–Fe alloy [60,73,146]. Ni addition enhances the alloy’s tensile strength
and fracture toughness [74,130]. Nb provides solid solution strengthening and similarly
improves the mechanical properties of the alloy [110]. The inclusion of Ta and other group
V and IV transition metals improves the intrinsic ductility of W alloys. In particular, Ta not
only enhances ductility but also increases the hardness of resultant alloys [141–144].

## Page 29

Crystals 2024, 14, 665 29 of 40
Crystals 2024, 14, 665 31 of 44 
 
 
chemical maps (Figure 21d–h) at various ma gnifications, and the SAEDP (selected-area 
electron diffraction pattern) of selected nanoparticles (Figure 21f) provide compelling ev-
idence of ZrC’s capacity to capture and bind oxygen to form ZrOy particles. This mecha-
nism is a highly effective means of mitigating embrittlement [60,120]. 
 
Figure 20. SEM images of SLM-fabricated pu re W and W-ZrC nanocomposites: ( a,c) the top and 
side surface of pure W cubes, and (b,d) the top and side surface of W-ZrC cubes. The build direction 
(BD) is also indicated in the image [120]. 
Tantalum carbide (TaC) particles in W also play an important role in crack mitigation. 
This is achieved via the dual action of initiating in situ W 2C phase formations and pro-
moting oxygen consumption through TaO x formation, which collectively suppresses 
cracks [141,150]. Titanium carbide (TiC), while predominantly increasing hardness, may 
indirectly improve crack resistance due to the improved mechanical properties of the com-
posite [42,47,141,150]. Hafnium carbide (HfC) dispersion in conventionally fabricated W 
alloys has provided excellent thermal stability and tensile properties of composites 
[154,155]. This can be a useful feature to have for materials design in the AM of W as well. 
Figure 20. SEM images of SLM-fabricated pure W and W-ZrC nanocomposites: (a,c) the top and side
surface of pure W cubes, and (b,d) the top and side surface of W-ZrC cubes. The build direction (BD)
is also indicated in the image [120].
The incorporation of Ti, Ir, and Hf in conventionally fabricated W alloys achieves mul-
tiple objectives as they influence the mechanical properties in different ways. They increase
recrystallization temperatures and, as potent carbide formers, mitigate the adverse effects
of carbon impurities on the alloy’s mechanics, elevate the recrystallization temperatures,
and improve W’s low-temperature ductility and high-temperature strength [152–156].
Since unalloyed W exhibits limited plasticity, studies have predominantly focused on
reporting compression test results. Conversely, a wealth of tensile test results is available
for W alloys processed using AM (Figure 22). Alloying elements play a pivotal role in
enhancing the tensile properties of W, notably its elongation, which is otherwise limited
or non-existent in unalloyed W. The strength and elongation of W alloys vary depending
on compositions (Figure 22a,b). Wang et al. [ 74] reported a W–15% Ni alloy with a UTS
of 560 MPa and 3.75% elongation, while W–7% Ni–3% Fe showed a UTS of 1037 MPa
and 3.5% elongation [ 71], and W–4.6%Ni–2.4% Fe fabricated via powder extrusion 3D
printing and sintering showed a UTS of 1040 MPa and remarkably high (20.7%) elongation

## Page 30

Crystals 2024, 14, 665 30 of 40
(Figure 22a,b) [133]. Ultrashort-time laser liquid phase sintering processing for W heavy
alloy resulted in a UTS of 1374 MPa, and 8.5% elongation (Figure 22a,b) [85].
Crystals 2024, 14, 665 32 of 44 
 
 
 
Figure 21. Analysis of the nanoparticle’s dispersion in the SLM-fabricated W-ZrC nanocomposites: 
(a) distribution of nanoparticles, (b) the high-resolution transmission electron microscope of the se-
lected nanoparticle, (c) the high-angle annular dark field image, (d–h) its EDS elemental maps, and 
(f) the selected-area electron diffraction pattern of the selected nanoparticle [120]. 
4.3. Alloying and Ceramic Dispersions for Mechanical Properties Adjustments 
Besides mitigating the problems discussed above, alloying confers additional bene-
fits. Fe integration in W alloys during AM strengthens the resulting material due to the 
formation of secondary or precipitated phases. This is due to the possible peritectic reac-
tion between Fe and W during non-equilibrium solidification, leading to the emergence 
of intermetallic phases such as Fe7W6 and Fe2W. This formation significantly increases the 
hardness of the W–Fe alloy [60,73,146]. Ni a ddition enhances the alloy’s tensile strength 
and fracture toughness [74,130]. Nb provides solid solution strengthening and similarly 
improves the mechanical properties of the alloy [110]. The inclusion of Ta and other group 
V and IV transition metals improves the intrinsic ductility of W alloys. In particular, Ta 
not only enhances ductility but also increases the hardness of resultant alloys [141–144]. 
The incorporation of Ti, Ir, and Hf in conv entionally fabricated W alloys achieves 
multiple objectives as they influence the me chanical properties in different ways. They 
increase recrystallization temperatures and, as potent carbide formers, mitigate the ad-
verse effects of carbon impurities on the a lloy’s mechanics, elevate the recrystallization 
Figure 21. Analysis of the nanoparticle’s dispersion in the SLM-fabricated W-ZrC nanocomposites:
(a) distribution of nanoparticles, ( b) the high-resolution transmission electron microscope of the
selected nanoparticle, (c) the high-angle annular dark field image, (d–h) its EDS elemental maps, and
(f) the selected-area electron diffraction pattern of the selected nanoparticle [120].
Figure 22c depicts the microhardness of AM-fabricated W-based materials. Li et al. [145]
examined the variation in Vickers microhardness due to VED in the context of W-3%Ta
alloy. Operating at a substrate preheating temperature of 150 ◦C and a 67◦ layer angle, they
reported a range of microhardness values from 493.8 to 535.6 Hv. This range correlated
with VED values spanning 192 to 1000 J/mm3, with an average microhardness of 505.7 Hv.
An upward trend in relative density was concurrently observed as VED values increased.
Conversely, Bose et al. [86] reported the highest microhardness achievement of 966 Hv
for a W-Cr component produced through binder jetting and sintering at 1500 ◦C for 1 h,
demonstrating a striking contrast to the above trends. Zhang et al. [130] and Yan et al. [136]
showed a contrasting narrative, showcasing a decline in hardness with an incremental
influx of Ni in W-Ni and W-Ni-Cu systems. In a related study, Zhang et al. [130] highlighted
a gradient of hardness reduction with the distance from the base of SLM-fabricated samples,
plummeting from 810 to 300 Hv for W-10%Ni and from 490 to 250 Hv for W-40Ni.

## Page 31

Crystals 2024, 14, 665 31 of 40
Crystals 2024, 14, 665 33 of 44 
 
 
temperatures, and improve W’s low-temperature ductility and high-temperature strength 
[152–156]. 
Since unalloyed W exhibits limited plasticity, studies have predominantly focused 
on reporting compression test results. Conversely, a wealth of tensile test results is avail-
able for W alloys processed using AM (Figure 22). Alloying elements play a pivotal role 
in enhancing the tensile properties of W, notably its elongation, which is otherwise limited 
or non-existent in unalloyed W. The strength and elongation of W alloys vary depending 
on compositions (Figure 22a,b). Wang et al. [74] reported a W–15% Ni alloy with a UTS of 
560 MPa and 3.75% elongation, while W–7% Ni–3% Fe showed a UTS of 1037 MPa and 
3.5% elongation [71], and W–4.6%Ni–2.4% Fe fabricated via powder extrusion 3D printing 
and sintering showed a UTS of 1040 MPa and remarkably high (20.7%) elongation (Figure 
22a,b) [133]. Ultrashort-time laser liquid phase sintering processing for W heavy alloy re-
sulted in a UTS of 1374 MPa, and 8.5% elongation (Figure 22a,b) [85]. 
 
Figure 22. Mechanical properties of AM-fabricated W alloys: (a) ultimate tensile strength, (b) elon-
gation, and (c) microhardness. 
Figure 22c depicts the microhardness of AM-fabricated W-based materials. Li et al. 
[145] examined the variation in Vickers micr ohardness due to VED in the context of W-
3%Ta alloy. Operating at a substrate prehea ting temperature of 150 °C and a 67° layer 
angle, they reported a range of microhardne ss values from 493.8 to 535.6 Hv. This range 
correlated with VED values spanning 192 to 1000 J/mm3, with an average microhardness 
of 505.7 Hv. An upward trend in relative density was concurrently observed as VED val-
ues increased. Conversely, Bose et al. [86] reported the highest microhardness achieve-
ment of 966 Hv for a W-Cr component produc ed through binder jetting and sintering at 
1500 °C for 1 h, demonstrating a striking contrast to the above trends. Zhang et al. [130] 
and Yan et al. [136] showed a contrasting narrative, showcasing a decline in hardness with 
an incremental influx of Ni in W-Ni and W- Ni-Cu systems. In a related study, Zhang et 
al. [130] highlighted a gradient of hardness reduction with the distance from the base of 
SLM-fabricated samples, plummeting from 810 to 300 Hv for W-10%Ni and from 490 to 
250 Hv for W-40Ni. 
Ivekovic et al. [132] noted a decline in hardness post-heat treatment of SLM-fabri-
cated W-7Ni-3Fe samples, which diverged from the augmentation in hardness expected. 
Figure 22. Mechanical properties of AM-fabricated W alloys: (a) ultimate tensile strength, (b) elonga-
tion, and (c) microhardness.
Ivekovic et al. [132] noted a decline in hardness post-heat treatment of SLM-fabricated
W-7Ni-3Fe samples, which diverged from the augmentation in hardness expected. Con-
versely, Wang et al. [135] demonstrated that an escalation in the microhardness of W-Ni-Cu
alloys, ranging from 360 to 395 Hv, was linked to increasing VED. This phenomenon is
attributed to the formation of finer grain sizes owing to elevated melt pool temperatures.
Moreover, Hu et al. [42] brought nano-structural considerations into the equation, under-
scoring the influence of grain size. They documented an upswing in hardness with the
decreasing grain size of Y2O3 particles, transitioning from micro- to nano-scale dimensions.
These findings underscore the fact that enhanced and/or adjusted mechanical proper-
ties are achievable through alloying in the AM of W-based materials.
4.4. Alloying for Other Specific Purposes
The addition of Ta to W alloys is pivotal for reducing fuzz formation. Ta has demon-
strated its capability to reduce fuzz during He plasma irradiation, making these alloys
suitable for nuclear applications [140]. Furthermore, W alloys formulated with the Cr-Y
combination exhibit self-passivation behavior in conventional fabrication. This intrin-
sic property makes W alloys integrated with Cr-Y especially useful in high-temperature
applications [60,157].
Overall, the addition of alloying elements activates several mechanisms to enhance
various properties (Table 8), which are as follows. Alloying elements such as Ta, Re,
and Ni can act as grain refiners in W-based alloys. These elements reduce the grain size
by inhibiting grain growth during solidification, resulting in a finer and more uniform
microstructure [158]. Fine-grained microstructures typically exhibit higher strength and
improved toughness due to the grain boundary strengthening mechanism. Alloying
elements like Mo and Ti lead to solid solution strengthening [159]. These elements distort
the W lattice and impede dislocation motion, thereby enhancing the yield strength and
overall mechanical properties of the alloy. This mechanism is particularly beneficial in
improving the high-temperature strength of W alloys. Certain alloying elements can
form stable second phases or precipitates within the W matrix [160]. For example, carbide-
forming elements such as carbon C can produce W carbides (WC) that enhance the hardness

## Page 32

Crystals 2024, 14, 665 32 of 40
and wear resistance of the alloy. These second phases also contribute to the overall strength
by hindering dislocation movement. Alloying with elements such as Cr and Si can improve
the oxidation resistance of W alloys [161]. These elements form protective oxide layers on
the surface, which act as barriers to further oxidation, thereby enhancing the performance of
W components in high-temperature environments [162]. Other elements like Re improve the
ductility of W alloys by reducing the DBTT [128]. This brings about a more ductile fracture
behavior and better toughness at lower temperatures, which is crucial for applications
where mechanical shock or impact resistance is required.
5. Conclusions
Overall, the proposed solutions, which include optimizing process parameters, re-
fining powder characteristics, implementing post-processing treatments, and employing
alloying elements, are essential to address the fundamental issues of densification and
mechanical properties in W-based materials. Here, we provide a detailed discussion of
how each approach contributes to improving densification and mechanical properties,
supported by the relevant literature.
1. Powder Characteristics
Particle Size and morphology: Utilizing W powder with a well-controlled particle size
distribution and spherical morphology enhances flowability, packing density, and uniform
layer formation during the built cycle. These characteristics are crucial for achieving high
relative density and consistent microstructures, as evidenced by improved mechanical
properties in various studies.
Powder purity: High-purity W powder minimizes contaminants that can cause defects
and degrade mechanical properties. Ensuring powder purity is fundamental for producing
high-quality components with superior mechanical integrity.
2. Process Parameter Optimization
Laser power and scan speed: By carefully adjusting the laser power and scan speed,
we can ensure adequate energy input for the complete melting of tungsten powder while
avoiding defects such as keyhole porosity and excessive vaporization. Optimal control
of these parameters results in improved densification and reduced residual stresses. A
maximum density of 99.2% in SLM and 100% in EBM was demonstrated by adjusting
process parameters.
Volumetric energy density (VED): Our study emphasizes the critical role of VED in
balancing energy input to promote full melting and minimize defects. Extremely high VED
can introduce porosity and fusion issues, while insufficient VED can result in incomplete
melting. Optimizing VED is essential for achieving high relative density and enhancing
mechanical properties.
3. Thermal Management Strategies
Controlled atmosphere: Using an inert gas atmosphere of argon or nitrogen during
the AM process prevents oxidation and contamination, preserving the material’s purity
and mechanical properties. While the majority of studies used argon, processing in a
nitrogen atmosphere could enhance the microstructure and mechanical performance of
tungsten parts.
Substate preheat: Utilizing a heated substrate plate in PBF processes is necessary to
control cooling rates and mitigate thermal gradients such as built-up thermal residual
stresses within the material, and improves material formation and properties. In most
cases, the substrate is preheated in the range of 500 ◦C to 1000 ◦C in SLM and up to 1800 ◦C
in EBM to eliminate crack formation.
Optimized scan strategies: Utilizing optimized scanning strategies such as alternating
scan directions, island scanning, and contour scanning can distribute heat more evenly
across the build area, reducing localized thermal stresses. These strategies help in achieving
uniform thermal profiles and minimizing warping and distortion.

## Page 33

Crystals 2024, 14, 665 33 of 40
4. Alloying Strategies
The introduction of alloying elements: Adding alloying elements such as Re, Ta, and
Hf can significantly enhance the mechanical properties and processability of W. Re, for
instance, is known to improve ductility and reduce the DBTT, refine the grain structure,
and improve the toughness of W alloys.
The introduction of ceramic particles: carbide formers (e.g., TiC, ZrC) can be in-
troduced, which act as grain refiners and strengthen the W matrix through dispersion
strengthening to improve the hardness and wear resistance of W components.
5. Post-Processing Treatments
Heat treatment: Post-process heat treatments are vital for relieving residual stresses,
promoting grain growth, and enhancing mechanical properties. Techniques such as anneal-
ing reduce micro-cracks and improve ductility.
Hot isostatic pressing (HIP): HIP applies high pressure and temperature to further
densify the components, close remaining pores, and refine the microstructure. This results
in significantly improved mechanical strength and integrity.
6. Future Directions
Although W-AM holds great promise for producing high-performance parts, its
widespread adoption has been hindered by problems associated with W’s inherent material
properties and printability challenges. Research efforts into the AM of W should be priori-
tized through the fine-tuning of process parameters, as well as microstructural and material
design. We believe in the possibilities of bringing W-AM into a new era of precision, sustain-
ability, and widespread applicability through advancements in atomic-level understanding,
and thermodynamic modeling, as well as through harnessing the power of data analytics.
1. Atomic-Level Understanding: The Key to Tailored Properties
Further studies are needed to understand W at the atomic level, focusing on the local
atomic structure and short-range order chemistry. Improving our understanding of the
inherent atomic arrangement in W from the microscopic perspective will enable us to
unlock new possibilities for tailored material properties and optimized performance.
2. Thermodynamic Modeling: A Roadmap for Alloy Design
Integrating the thermodynamic calculation of phase diagram modeling into alloy
design will play a key role in predicting phase equilibria and allow researchers to
design W alloys with better control over composition and phase transitions. This
thermodynamic approach ensures a systematic exploration of the uncharted alloy
space, allowing materials with tailored properties to be developed. This provides
insights into process optimization through thermal gradients, melt pool dynamics,
and solidification rates, which are essential for minimizing porosity and achieving
uniform microstructures.
3. Composite Design: Improved Innovative Composite
Researchers can seek to synergize W with other advanced ceramics, to create composites
that exhibit superior mechanical, thermal, and chemical properties. This approach opens
avenues for tailoring W composites for specific applications across diverse industries.
4. Harnessing the Power of Data Analytics: Machine Learning and in situ Monitoring
Researchers can leverage machine learning and statistical techniques to identify pat-
terns and correlations which can help in the optimization of processing parameters.
Multiphysics and multi-scale computational modeling are essential for establishing
process–structure–property relationships in metal AM [163]. This paves the way for
the development of a digital twin for W-AM. Further studies can also develop and
implement advanced in situ process monitoring techniques during AM. The data gen-
erated during the real-time monitoring of temperature, microstructure evolution, and
defect formation will provide valuable insights, enabling adaptive control strategies
to enhance the quality and repeatability of W components.

## Page 34

Crystals 2024, 14, 665 34 of 40
5. Sustainable Manufacturing: the Hidden Cost of the Oxidation of W
The high oxygen affinity of W and its influence extends beyond AM-fabricated parts.
The high temperatures and heating profiles employed during AM processes can lead
to the inadvertent oxidation of adjacent powder beds. This oxidation significantly
affects the reusability of W powder, potentially increasing waste and negating the
environmental and cost benefits of AM. Future research efforts should prioritize
mitigating this hidden cost by a comprehensive understanding of W oxidation to
minimize the impact of oxidation and maximize powder reusability.
Author Contributions: Conceptualization, M.Z., Y.T. and C.M.; methodology, M.Z., M.S. and N.W.;
validation, Y.X., M.Z. and L.T.; formal analysis, M.Z., C.M. and M.S.; resources, M.Z., N.W. and
Y.X.; data curation, S.R., X.C. and L.T.; writing—original draft preparation, M.Z., M.S., Y.T., S.R.
and C.M.; writing—review and editing, M.Z., M.S., X.C., N.W., Y.X., S.R. and K.X.K.; visualization,
M.Z., M.S. and K.X.K.; supervision, M.Z., Y.T. and M.S.; project administration, M.Z., C.M. and Y.T.;
funding acquisition, C.M. and M.Z. All authors have read and agreed to the published version of
the manuscript.
Funding: This research was funded by Zhejiang Province grant number: 2023C01SA393195, and
Wenzhou City grant number: ZG2023036.
Data Availability Statement: No further data are available. All the data pertaining to this work are
already included in the article.
Acknowledgments: The authors from Wenzhou Hongfong Electrical Alloy Co Ltd and its subsidiary
acknowledge these generous financial supports.
Conflicts of Interest: Authors Mehrdad Zarinejad, Chengfa Mu, Lintao Tian, and Xiaotong Chen
were employed by the company Wenzhou Hongfeng Electrical Alloy Co., Ltd. Authors Nian Wang,
and Yonglong Xu were employed by the company Wenzhou Hongfeng Alloy Co., Ltd. The remaining
authors declare that the research was conducted in the absence of any commercial or financial
relationships that could be construed as a potential conflict of interest.
Abbreviations
List of abbreviations used in the manuscript along with their full forms.
Abbreviation Term
AM Additive manufacturing
BMD Bound metal deposition
DED Direct energy deposition
DBTT Ductile-to-brittle transition temperatures
EBM Electron beam melting
HAGBs High-angle grain boundaries
LED Line (laser) energy density
LPS Liquid phase sintering
LAGBs Low-angle grain boundaries
PBF Powder bed fusion
W Tungsten
VED Volumetric energy density
References
1. Rieth, M.; Dudarev, S.L.; de Vicente, S.M.G.; Aktaa, J.; Ahlgren, T.; Antusch, S.; Armstrong, D.E.J.; Balden, M.; Baluc, N.; Barthe,
M.-F.; et al. Recent progress in research on tungsten materials for nuclear fusion applications in Europe. J. Nucl. Mater. 2013, 432,
482–500. [CrossRef]
2. Xie, J.; Lu, H.; Lu, J.; Song, X.; Wu, S.; Lei, J. Additive manufacturing of tungsten using directed energy deposition for potential
nuclear fusion application. Surf. Coat. Technol. 2021, 409, 126884. [CrossRef]
3. Katoh, Y.; Snead, L.L.; Garrison, L.M.; Hu, X.; Koyanagi, T.; Parish, C.M.; Edmondson, P .D.; Fukuda, M.; Hwang, T.; Tanaka, T.;
et al. Response of unalloyed tungsten to mixed spectrum neutrons. J. Nucl. Mater. 2019, 520, 193–207. [CrossRef]
4. Wang, G.; Qin, Y.; Yang, S. Influence of Ni additions on the microstructure and tensile property of W-Cu composites produced by
direct energy deposition. J. Alloys Compd. 2022, 899, 163272. [CrossRef]

## Page 35

Crystals 2024, 14, 665 35 of 40
5. Engwall, A.M.; Shin, S.J.; Bae, J.; Wang, Y.M. Enhanced properties of tungsten films by high-power impulse magnetron sputtering.
Surf. Coat. Technol. 2019, 363, 191–197. [CrossRef]
6. Su, S.; Lu, Y. Densified W Cu composite fabricated via laser additive manufacturing. Int. J. Refract. Met. Hard Mater. 2020,
87, 105122. [CrossRef]
7. Oponowicz, A.; Marciszko-Wi ˛ ackowska, M.; Baczma ´ nski, A.; Klaus, M.; Genzel, C.; Wro ´ nski, S.; Kollbek, K.; Wróbel, M. Gradient
of Residual Stress and Lattice Parameter in Mechanically Polished Tungsten Measured Using Classical X-rays and Synchrotron
Radiation. Metall. Mater. Trans. A 2020, 51, 5945–5957. [CrossRef]
8. Ivekovi´ c, A.; Omidvari, N.; Vrancken, B.; Lietaert, K.; Thijs, L.; Vanmeensel, K.; Vleugels, J.; Kruth, J.-P . Selective laser melting of
tungsten and tungsten alloys. Int. J. Refract. Met. Hard Mater. 2018, 72, 27–32. [CrossRef]
9. Jia, Y.; Chang, S.; Du, X.; Guo, S. Corrosion Performance of Commercial Alloys and Refractory Metals in Conditions for
Electrorefining of Spent Nuclear Fuels. Crystals 2023, 13, 817. [CrossRef]
10. Wei, Q.; Ramesh, K.T.; Schuster, B.E.; Kecskes, L.J.; Dowding, R.J. Nanoengineering opens a new era for tungsten as well.JOM
2006, 58, 40–44. [CrossRef]
11. Zinkle, S.J.; Ott, L.J.; Ingersoll, D.T.; Ellis, R.J.; Grossbeck, M.L. Overview of materials technologies for space nuclear power and
propulsion. AIP Conf. Proc. 2002, 608, 1063–1073. [CrossRef]
12. Mani, M.; Madan, J.; Lee, J.H.; Lyons, K.W.; Gupta, S.K. Sustainability characterisation for manufacturing processes. Int. J. Prod.
Res. 2014, 52, 5895–5912. [CrossRef]
13. Valivullah, L.; Mani, M.; Lyons, K.W.; Gupta, S.K. Manufacturing Process Information Models for Sustainable Manufacturing. In
Volume 1: Materials; Micro and Nano Technologies; Properties, Applications and Systems; Sustainable Manufacturing; American Society
of Mechanical Engineers: New York, NY, USA, 2014. [CrossRef]
14. Mani, M.; Lyons, K.W.; Gupta, S.K. Sustainability Characterization for Additive Manufacturing. J. Res. Natl. Inst. Stand. Technol.
2014, 119, 419. [CrossRef] [PubMed]
15. Moghimian, P .; Poirié, T.; Habibnejad-Korayem, M.; Zavala, J.A.; Kroeger, J.; Marion, F.; Larouche, F. Metal powders in additive
manufacturing: A review on reusability and recyclability of common titanium, nickel and aluminum alloys. Addit. Manuf. 2021,
43, 102017. [CrossRef]
16. Mireles, O.; Rodriguez, O.; Gao, Y.; Philips, N. Additive Manufacture of Refractory Alloy C103 for Propulsion Applications. In
AIAA Propulsion and Energy 2020 Forum; American Institute of Aeronautics and Astronautics: Reston, VA, USA, 2020. [CrossRef]
17. Ren, X.; Liu, H.; Lu, F.; Huang, L.; Yi, X. Effects of processing parameters on the densification, microstructure and mechanical
properties of pure tungsten fabricated by optimized selective laser melting: From single and multiple scan tracks to bulk parts.
Int. J. Refract. Met. Hard Mater. 2021, 96, 105490. [CrossRef]
18. Bai, S.; Liu, J.; Yang, P .; Huang, H.; Yang, L.-M. Femtosecond Fiber Laser Additive Manufacturing of Tungsten. In Proceedings of
the SPIE 9738-24, San Francisco, CA, USA, 13–18 February 2016; Gu, B., Helvajian, H., Piqué, A., Eds.; SPIE: San Francisco, CA,
USA, 2016. [CrossRef]
19. Müller, A.V .; Schlick, G.; Neu, R.; Anstätt, C.; Klimkait, T.; Lee, J.; Pascher, B.; Schmitt, M.; Seidel, C. Additive manufacturing
of pure tungsten by means of selective laser beam melting with substrate preheating temperatures up to 1000 ◦C. Nucl. Mater.
Energy 2019, 19, 184–188. [CrossRef]
20. Feng, F.; Lian, Y.; Wang, J.; Song, J.; Yan, B.; Liu, X. Mechanical Properties and Thermal Shock Performance of High-Energy-Rate-
Forged W-1%TaC Alloy.Crystals 2022, 12, 1047. [CrossRef]
21. Wang, D.-Z.; Li, K.-L.; Yu, C.-F.; Ma, J.; Liu, W.; Shen, Z.-J. Cracking Behavior in Additively Manufactured Pure Tungsten.Acta
Metall. Sin. (Engl. Lett.) 2019, 32, 127–135. [CrossRef]
22. Lassner, E.; Schubert, W.-D. Tungsten; Springer US: Boston, MA, USA, 1999. [CrossRef]
23. Mitteau, R.; Missiaen, J.M.; Brustolin, P .; Ozer, O.; Durocher, A.; Ruset, C.; Lungu, C.P .; Courtois, X.; Dominicy, C.; Maier, H.; et al.
Recent developments toward the use of tungsten as armour material in plasma facing components. Fusion. Eng. Des. 2007, 82,
1700–1705. [CrossRef]
24. Vrancken, B.; Ganeriwala, R.K.; Matthews, M.J. Analysis of laser-induced microcracking in tungsten under additive manufacturing
conditions: Experiment and simulation. Acta Mater. 2020, 194, 464–472. [CrossRef]
25. Elsayed, A.H.; Sayed, M.A.; Dawood, O.M.; Daoush, W.M. Effect of Transition Metals Oxides on the Physical and Mechanical
Properties of Sintered Tungsten Heavy Alloys. Crystals 2020, 10, 825. [CrossRef]
26. Wang, L.; Wu, J.; Zhang, D. Properties evolution of additive manufacture used tungsten powders prepared by radio frequency
induction plasma. Int. J. Refract. Met. Hard Mater. 2017, 67, 90–97. [CrossRef]
27. Zi, X.; Chen, C.; Wang, X.; Wang, P .; Zhang, X.; Zhou, K. Spheroidisation of tungsten powder by radio frequency plasma for
selective laser melting. Mater. Sci. Technol. 2018, 34, 735–742. [CrossRef]
28. Gu, D.D.; Meiners, W.; Wissenbach, K.; Poprawe, R. Laser additive manufacturing of metallic components: Materials, processes
and mechanisms. Int. Mater. Rev. 2012, 57, 133–164. [CrossRef]
29. Guo, M.; Gu, D.; Xi, L.; Du, L.; Zhang, H.; Zhang, J. Formation of scanning tracks during Selective Laser Melting (SLM) of pure
tungsten powder: Morphology, geometric features and forming mechanisms. Int. J. Refract Metals Hard Mater. 2019, 79, 37–46.
[CrossRef]
30. Wen, S.; Wang, C.; Zhou, Y.; Duan, L.; Wei, Q.; Yang, S.; Shi, Y. High-density tungsten fabricated by selective laser melting:
Densification, microstructure, mechanical and thermal performance. Opt. Laser Technol. 2019, 116, 128–138. [CrossRef]

## Page 36

Crystals 2024, 14, 665 36 of 40
31. Gokcekaya, O.; Ishimoto, T.; Todo, T.; Wang, P .; Nakano, T. Influence of powder characteristics on densification via crystallographic
texture formation: Pure tungsten prepared by laser powder bed fusion. Addit. Manuf. Lett. 2021, 1, 100016. [CrossRef]
32. Yang, G.; Yang, P .; Yang, K.; Liu, N.; Jia, L.; Wang, J.; Tang, H. Effect of processing parameters on the density, microstructure
and strength of pure tungsten fabricated by selective electron beam melting. Int. J. Refract. Metals Hard Mater. 2019, 84, 105040.
[CrossRef]
33. Gokuldoss, P .K.; Kolla, S.; Eckert, J.; Processes, A.M. Electron Beam Melting and Binder Jetting—Selection Guidelines.Materials
2017, 10, 672. [CrossRef] [PubMed]
34. Klahn, C.; Leutenecker, B.; Meboldt, M. Design Strategies for the Process of Additive Manufacturing. Procedia CIRP 2015, 36,
230–235. [CrossRef]
35. Vrancken, B.; King, W.E.; Matthews, M.J. In-situ characterization of tungsten microcracking in Selective Laser Melting.Procedia
CIRP 2018, 74, 107–110. [CrossRef]
36. Sidambe, A.T.; Tian, Y.; Prangnell, P .B.; Fox, P . Effect of processing parameters on the densification, microstructure and crys-
tallographic texture during the laser powder bed fusion of pure tungsten. Int. J. Refract. Metals Hard Mater. 2019, 78, 254–263.
[CrossRef]
37. Rebesan, P .; Bonesso, M.; Gennari, C.; Dima, R.; Pepato, A.; Vedani, M. Tungsten Fabricated by Laser Powder Bed Fusion.BHM
Berg-Und Hüttenmännische Monatshefte 2021, 166, 263–269. [CrossRef]
38. Tan, C.; Zhou, K.; Ma, W.; Attard, B.; Zhang, P .; Kuang, T. Selective laser melting of high-performance pure tungsten: Parameter
design, densification behavior and mechanical properties. Sci. Technol. Adv. Mater. 2018, 19, 370–380. [CrossRef] [PubMed]
39. Chen, J.; Li, K.; Wang, Y.; Xing, L.; Yu, C.; Liu, H.; Ma, J.; Liu, W.; Shen, Z. The effect of hot isostatic pressing on thermal
conductivity of additively manufactured pure tungsten. Int. J. Refract. Met. Hard Mater. 2020, 87, 105135. [CrossRef]
40. Field, A.C.; Carter, L.N.; Adkins, N.J.E.; Attallah, M.M.; Gorley, M.J.; Strangwood, M. The Effect of Powder Characteristics on
Build Quality of High-Purity Tungsten Produced via Laser Powder Bed Fusion (LPBF).Metall. Mater. Trans. A 2020, 51, 1367–1378.
[CrossRef]
41. Guo, M.; Gu, D.; Xi, L.; Zhang, H.; Zhang, J.; Yang, J.; Wang, R. Selective laser melting additive manufacturing of pure tungsten:
Role of volumetric energy density on densification, microstructure and mechanical properties. Int. J. Refract. Metals Hard Mater.
2019, 84, 105025. [CrossRef]
42. Hu, Z.; Zhao, Y.; Guan, K.; Wang, Z.; Ma, Z. Pure tungsten and oxide dispersion strengthened tungsten manufactured by selective
laser melting: Microstructure and cracking mechanism. Addit. Manuf. 2020, 36, 101579. [CrossRef]
43. Wang, D.; Yu, C.; Zhou, X.; Ma, J.; Liu, W.; Shen, Z. Dense Pure Tungsten Fabricated by Selective Laser Melting.Appl. Sci. 2017,
7, 430. [CrossRef]
44. Vrancken, B.; Ganeriwala, R.K.; Martin, A.A.; Matthews, M.J. Microcrack mitigation during laser scanning of tungsten via
preheating and alloying strategies. Addit. Manuf. 2021, 46, 102158. [CrossRef]
45. Xiong, Z.; Zhang, P .; Tan, C.; Dong, D.; Ma, W.; Yu, K. Selective Laser Melting and Remelting of Pure Tungsten.Adv. Eng. Mater.
2020, 22. [CrossRef]
46. Zhou, X.; Liu, X.; Zhang, D.; Shen, Z.; Liu, W. Balling phenomena in selective laser melted tungsten. J. Mater. Process Technol. 2015,
222, 33–42. [CrossRef]
47. Wu, Y. Manufacturing of tungsten and tungsten composites for fusion application via different routes.Tungsten 2019, 1, 80–90.
[CrossRef]
48. Wang, D.; Wang, Z.; Li, K.; Ma, J.; Liu, W.; Shen, Z. Cracking in laser additively manufactured W: Initiation mechanism and a
suppression approach by alloying. Mater. Des. 2019, 162, 384–393. [CrossRef]
49. Braun, J.; Kaserer, L.; Stajkovic, J.; Leitz, K.-H.; Tabernig, B.; Singer, P .; Leibenguth, P .; Gspan, C.; Kestler, H.; Leichtfried, G.
Molybdenum and tungsten manufactured by selective laser melting: Analysis of defect structure and solidification mechanisms.
Int. J. Refract. Met. Hard Mater. 2019, 84, 104999. [CrossRef]
50. Yamamoto, T.; Hara, M.; Hatano, Y. Effects of fabrication conditions on the microstructure, pore characteristics and gas retention
of pure tungsten prepared by laser powder bed fusion. Int. J. Refract. Metals Hard Mater. 2021, 95, 105410. [CrossRef]
51. Enneti, R.K.; Morgan, R.; Atre, S.V . Effect of process parameters on the Selective Laser Melting (SLM) of tungsten.Int. J. Refract.
Met. Hard Mater. 2018, 71, 315–319. [CrossRef]
52. Zhang, D.; Cai, Q.; Liu, J. Formation of Nanocrystalline Tungsten by Selective Laser Melting of Tungsten Powder.Mater. Manuf.
Process. 2012, 27, 1267–1270. [CrossRef]
53. Zhang, J.; Gu, D.; Yang, Y.; Zhang, H.; Chen, H.; Dai, D.; Lin, K. Influence of Particle Size on Laser Absorption and Scanning Track
Formation Mechanisms of Pure Tungsten Powder During Selective Laser Melting. Engineering 2019, 5, 736–745. [CrossRef]
54. Deprez, K.; Vandenberghe, S.; Van Audenhaege, K.; Van Vaerenbergh, J.; Van Holen, R. Rapid additive manufacturing of MR
compatible multipinhole collimators with selective laser melting of tungsten powder. Med. Phys. 2013, 40, 012501. [CrossRef]
55. Sidambe, A.T.; Judson, D.S.; Colosimo, S.J.; Fox, P . Laser powder bed fusion of a pure tungsten ultra-fine single pinhole collimator
for use in gamma ray detector characterisation. Int. J. Refract. Met. Hard Mater. 2019, 84, 104998. [CrossRef]
56. Gear, J.I.; Taprogge, J.; White, O.; Flux, G.D. Characterisation of the attenuation properties of 3D-printed tungsten for use in
gamma camera collimation. EJNMMI Phys. 2019, 6, 1. [CrossRef] [PubMed]
57. Zhou, K.; Chen, W.; Yang, Y.; Li, R.; Dong, L.; Fu, Y.-Q. Microstructure and mechanical behavior of porous tungsten skeletons
synthesized by selected laser melting. Int. J. Refract. Met. Hard Mater. 2022, 103, 105769. [CrossRef]

## Page 37

Crystals 2024, 14, 665 37 of 40
58. Morcos, P .; Elwany, A.; Karaman, I.; Arr óyave, R. Review: Additive manufacturing of pure tungsten and tungsten-based alloys.
J. Mater. Sci. 2022, 57, 9769–9806. [CrossRef]
59. Omole, S.; Lunt, A.; Kirk, S.; Shokrani, A. Advanced Processing and Machining of Tungsten and Its Alloys. J. Manuf. Mater.
Process. 2022, 6, 15. [CrossRef]
60. Pan, S.-H.; Yao, G.-C.; Cui, Y.-N.; Meng, F.-S.; Luo, C.; Zheng, T.-Q.; Singh, G. Additive manufacturing of tungsten, tungsten-based
alloys, and tungsten matrix composites. Tungsten 2023, 5, 1–31. [CrossRef]
61. Talignani, A.; Seede, R.; Whitt, A.; Zheng, S.; Ye, J.; Karaman, I.; Kirka, M.M.; Katoh, Y.; Wang, Y.M. A review on additive
manufacturing of refractory tungsten and tungsten alloys. Addit. Manuf. 2022, 58, 103009. [CrossRef]
62. Galati, M. Electron beam melting process. In Additive Manufacturing; Elsevier: Amsterdam, The Netherlands, 2021; pp. 277–301.
[CrossRef]
63. Ellis, E.A.I.; Sprayberry, M.A.; Ledford, C.; Hankwitz, J.P .; Kirka, M.M.; Rock, C.D.; Horn, T.J.; Katoh, Y.; Dehoff, R.R. Processing
of tungsten through electron beam melting. J. Nucl. Mater. 2021, 555, 153041. [CrossRef]
64. Zhang, H.; Carriere, P .R.; Amoako, E.D.; Rock, C.D.; Thielk, S.U.; Fletcher, C.G.; Horn, T.J. Microstructure and Elevated Temperature
Flexure Testing of Tungsten Produced by Electron Beam Additive Manufacturing.JOM 2023, 75, 4094–4107. [CrossRef]
65. Dorow-Gerspach, D.; Kirchner, A.; Loewenhoff, T.; Pintsuk, G.; Weißgärber, T.; Wirtz, M. Additive manufacturing of high density
pure tungsten by electron beam melting. Nucl. Mater. Energy 2021, 28, 101046. [CrossRef]
66. Wang, J.; Yao, D.; Li, M.; An, X.; Li, S.; Hou, W.; Zhang, X.; Yang, G.; Wang, J.; Wang, L. Hierarchical effects of multi-layer
powder spreading in the electron beam powder bed fusion additive manufacturing of pure tungsten material. Addit. Manuf. 2022,
55, 102835. [CrossRef]
67. Zhao, X.; An, N.; Yang, G.; Wang, J.; Tang, H.; Li, M.; Zhou, J. Enhancing standard finite element codes with POD for reduced
order thermal analysis: Application to electron beam melting of pure tungsten. Mater. Today Commun. 2021, 29, 102796. [CrossRef]
68. Fernandez-Zelaia, P .; Kirka, M.; Campbell, Q.; Rojas, J.O.; Rossy, A.M.; Ledford, C. Electron Beam Powder Bed Fusion Additive
Manufacturing of Refractory Metals. In Proceedings of the Powdermet/Tungsten 2021; Orlando, FL, USA, 20–23 June 2021. Available
online: https://www.osti.gov/biblio/1832704 (accessed on 15 July 2024).
69. Liao, W.-B.; Liu, Z.-Y.; He, M.-J.; Feng, C.; Wang, F.; Huang, J. Effect of Electron Beam Remelting Treatments on the Microstructure
and Properties of Atmospheric Plasma Sprayed Tungsten Coatings. J. Therm. Spray. Technol. 2021, 30, 2128–2137. [CrossRef]
70. Jeong, W.; Kwon, Y.-S.; Kim, D. Three-dimensional printing of tungsten structures by directed energy deposition.Mater. Manuf.
Process. 2019, 34, 986–992. [CrossRef]
71. Wang, Y.P .; Ma, S.Y.; Yang, X.S.; Zhou, Y.Z.; Liu, X.; Li, J.F.; Zhang, J.J.; Li, C.; Wang, X.Y.; Le, G.M.; et al. Microstructure and
strengthening mechanisms of 90W–7Ni–3Fe alloys prepared using laser melting deposition. J. Alloys Compd. 2020, 838, 155545.
[CrossRef]
72. Wang, G.-Y.; Gu, S.-N.; Yang, S. Microstructure and properties of tungsten heavy alloys fabricated by laser direct deposition.
Mater. Sci. Technol. 2017, 33, 415–420. [CrossRef]
73. Li, C.; Ma, S.; Liu, X.; Li, J.; Le, G. Microstructures and properties of 80W-20Fe alloys prepared using laser melting deposition
process. Int. J. Refract. Met. Hard Mater. 2018, 77, 113–119. [CrossRef]
74. Wang, G.; Sun, X.; Huang, M.; Qin, Y.; Yao, Y.; Yang, S. Influence of processing parameters on the microstructure and tensile
property of 85 W-15Ni produced by laser direct deposition. Int. J. Refract. Met. Hard Mater. 2019, 82, 227–233. [CrossRef]
75. Zhou, S.; Wang, L.; Liang, Y.-J.; Zhu, Y.; Jian, R.; Wang, B.; Wang, L.; Xue, Y.; Wang, F.; Cai, H.; et al. A strategy to achieve
high-strength WNiFe composite-like alloys with low W content by laser melting deposition. Mater. Des. 2020, 190, 108554.
[CrossRef]
76. DebRoy, T.; Wei, H.L.; Zuback, J.S.; Mukherjee, T.; Elmer, J.W.; Milewski, J.O.; Beese, A.M.; Wilson-Heid, A.; De, A.; Zhang, W.
Additive manufacturing of metallic components—Process, structure and properties.Prog. Mater. Sci. 2018, 92, 112–224. [CrossRef]
77. Li, C.; Wang, Y.; Ma, S.; Yang, X.; Li, J.; Zhou, Y.; Liu, X.; Tang, J.; Wang, X.; Le, G. Densification, microstructural evolutions of
90W-7Ni-3Fe tungsten heavy alloys during laser melting deposition process. Int. J. Refract. Met. Hard Mater. 2020, 91, 105254.
[CrossRef]
78. Marinelli, G.; Martina, F.; Lewtas, H.; Hancock, D.; Mehraban, S.; Lavery, N.; Ganguly, S.; Williams, S. Microstructure and thermal
properties of unalloyed tungsten deposited by Wire + Arc Additive Manufacture. J. Nucl. Mater. 2019, 522, 45–53. [CrossRef]
79. Pixner, F.; Buzolin, R.; Warchomicka, F.; Pilz, A.; Enzinger, N. Wire-based electron beam additive manufacturing of tungsten.Int.
J. Refract. Met. Hard Mater. 2022, 108, 105917. [CrossRef]
80. Stawovy, M.T.; Myers, K.; Ohm, S. Binder jet printing of tungsten heavy alloy.Int. J. Refract. Met. Hard Mater. 2019, 83, 104981.
[CrossRef]
81. Doddapaneni, V .V .K.; Lee, K.; Aysal, H.E.; Paul, B.K.; Pasebani, S.; Sierros, K.A.; Okwudire, C.E.; Chang, C. A Review on Progress,
Challenges, and Prospects of Material Jetting of Copper and Tungsten. Nanomaterials 2023, 13, 2303. [CrossRef]
82. Ottensmeyer, M.; Sabet, H.; Furenlid, L.; May, M.; Kupinski, M. Collimator fabrication techniques: A comparative study.J. Nucl.
Med. 2023, 64, P1600. Available online: http://jnm.snmjournals.org/content/64/supplement_1/P1600.abstract (accessed on
15 July 2024).
83. Bose, A.; Reidy, J.P .; Tuncer, N.; Jorgensen, L. Processing of tungsten heavy alloy by extrusion-based additive manufacturing.Int.
J. Refract. Met. Hard Mater. 2023, 110, 106021. [CrossRef]

## Page 38

Crystals 2024, 14, 665 38 of 40
84. Huang, N.; Cook, O.J.; Argüelles, A.P .; Beese, A.M. Review of Process–Structure–Property Relationships in Metals Fabricated
Using Binder Jet Additive Manufacturing. Metallogr. Microstruct. Anal. 2023, 12, 883–905. [CrossRef]
85. Zhou, S.; Liang, Y.-J.; Zhu, Y.; Wang, B.; Wang, L.; Xue, Y. Ultrashort-time liquid phase sintering of high-performance fine-grain
tungsten heavy alloys by laser additive manufacturing. J. Mater. Sci. Technol. 2021, 90, 30–36. [CrossRef]
86. Bose, A.; Schuh, C.A.; Tobia, J.C.; Tuncer, N.; Mykulowycz, N.M.; Preston, A.; Barbati, A.C.; Kernan, B.; Gibson, M.A.; Krause, D.;
et al. Traditional and additive manufacturing of a new Tungsten heavy alloy alternative. Int. J. Refract. Met. Hard Mater. 2018, 73,
22–28. [CrossRef]
87. Du, Z.-Y.; Lv, Y.-Q.; Han, Y.; Fan, J.-L.; Ye, L. Sintering densification behavior and kinetic mechanism of nano-tungsten powder
prepared by sol-spray drying. Tungsten 2020, 2, 371–380. [CrossRef]
88. Han, Y.; Fan, J.; Liu, T.; Cheng, H.; Tian, J. The effect of trace nickel additive and ball milling treatment on the near-full densification
behavior of ultrafine tungsten powder. Int. J. Refract. Met. Hard Mater. 2012, 34, 18–26. [CrossRef]
89. Thompson, S.M.; Bian, L.; Shamsaei, N.; Yadollahi, A. An overview of Direct Laser Deposition for additive manufacturing; Part I:
Transport phenomena, modeling and diagnostics. Addit. Manuf. 2015, 8, 36–62. [CrossRef]
90. Karafi, T.; Tahiri, A.; Chabba, H.; Idiri, M.; Boubeker, B. Effect of Grain-Size in Nanocrystalline Tungsten on Hardness and
Dislocation Density: A Molecular Dynamics Study. Crystals 2023, 13, 469. [CrossRef]
91. Kozyrev, N.V .; Gordeev, V .V . Thermodynamic Properties and Equation of State for Tungsten.Crystals 2023, 13, 1470. [CrossRef]
92. Griffiths, V .; Scanlan, J.P .; Eres, M.H.; Martinez-Sykora, A.; Chinchapatnam, P . Cost-driven build orientation and bin packing of
parts in Selective Laser Melting (SLM). Eur. J. Oper. Res. 2019, 273, 334–352. [CrossRef]
93. Ren, K.; Di, Y.; Wang, G.; Wang, L.; Wang, H.; Rong, Y. Forward calculation model for utilization of energy and mass in
laser-directed energy deposition. Addit. Manuf. 2023, 68, 103512. [CrossRef]
94. Mohammadhosseini, A.; Masood, S.H.; Fraser, D.; Jahedi, M. Dynamic compressive behaviour of Ti-6Al-4V alloy processed by
electron beam melting under high strain rate loading. Adv. Manuf. 2015, 3, 232–243. [CrossRef]
95. Yang, S.F.; Li, C.W.; Chen, A.Y.; Gan, B.; Gu, J.F. Microstructure and corrosion resistance of stainless steel manufactured by laser
melting deposition. J. Manuf. Process 2021, 65, 418–427. [CrossRef]
96. Ziaee, M.; Crane, N.B. Binder jetting: A review of process, materials, and methods. Addit. Manuf. 2019, 28, 781–801. [CrossRef]
97. Wei, C.; Liu, L.; Gu, Y .; Huang, Y .; Chen, Q.; Li, Z.; Li, L. Multi-material additive-manufacturing of tungsten-copper alloy bimetallic
structure with a stainless-steel interlayer and associated bonding mechanisms.Addit. Manuf.2022, 50, 102574. [CrossRef]
98. Sharma, S.; Krishna, K.V .M.; Joshi, S.S.; Radhakrishnan, M.; Palaniappan, S.; Dussa, S.; Banerjee, R.; Dahotre, N.B. Laser based
additive manufacturing of tungsten: Multi-scale thermo-kinetic and thermo-mechanical computational model and experiments.
Acta Mater. 2023, 259, 119244. [CrossRef]
99. Mukherjee, T.; DebRoy, T. A digital twin for rapid qualification of 3D printed metallic components.Appl. Mater. Today 2019, 14,
59–65. [CrossRef]
100. Ledford, C.; Fernandez-Zelaia, P .; Graening, T.; Campbell, Q.; Rojas, J.O.; Rossy, A.M.; Kato, Y.; Kirka, M.M. Microstructure and
high temperature properties of tungsten processed via electron beam melting additive manufacturing. Int. J. Refract. Met. Hard
Mater. 2023, 113, 106148. [CrossRef]
101. Matthews, M.; Trapp, J.; Guss, G.; Rubenchik, A. Direct measurements of laser absorptivity during metal melt pool formation
associated with powder bed fusion additive manufacturing processes. J. Laser Appl. 2018, 30, 032302. [CrossRef]
102. Enneti, R.; Morgan, R.; Wolfe, T.; Harooni, A.; Volk, S. Direct Metal Laser Sintering (DMLS) of Tungsten Powders. In Proceedings
of the Additive Manufacturing with Powder Metallurgy, Las Vegas, NV , USA, 13–15 June 2017.
103. Li, J.; Wei, Z.; Zhou, B.; Wu, Y.; Chen, S.-G.; Sun, Z. Densification, Microstructure and Properties of 90W-7Ni-3Fe Fabricated by
Selective Laser Melting. Metals 2019, 9, 884. [CrossRef]
104. Hu, Z.; Liu, Y.; Chen, S.; Liu, S.; Yu, L.; Liu, Y.; Ma, Z. Achieving high-performance pure tungsten by additive manufacturing:
Processing, microstructural evolution and mechanical properties. Int. J. Refract. Met. Hard Mater. 2023, 113, 106211. [CrossRef]
105. Müller, A.V .; Dorow-Gerspach, D.; Balden, M.; Binder, M.; Buschmann, B.; Curzadd, B.; Loewenhoff, T.; Neu, R.; Schlick, G.;
You, J.H. Progress in additive manufacturing of pure tungsten for plasma-facing component applications.J. Nucl. Mater. 2022,
566, 153760. [CrossRef]
106. Xia, Y.; Dong, Z.; Guo, X.; Tian, Q.; Liu, Y. Towards a circular metal additive manufacturing through recycling of materials: A
mini review. J. Cent. South. Univ. 2020, 27, 1134–1145. [CrossRef]
107. Gradl, P .; Mireles, O.R.; Andrews, N. Introduction to Additive Manufacturing for Propulsion and Energy Systems. In Proceedings
of the AIAA Propulsion and Energy Forum 2021, Denver, CO, USA, 9–11 August 2021.
108. Sidambe, A.; Fox, P . Analysis of melt pool during the laser powder bed fusion of tungsten. In Proceedings of the RAPDASA 2019
Conference and Exhibition, Gqeberha, South Africa, 28–31 October 2019.
109. Sochalski-Kolbus, L.M.; Payzant, E.A.; Cornwell, P .A.; Watkins, T.R.; Babu, S.S.; Dehoff, R.R.; Lorenz, M.; Ovchinnikova, O.; Duty,
C. Comparison of Residual Stresses in Inconel 718 Simple Parts Made by Electron Beam Melting and Direct Laser Metal Sintering.
Metall. Mater. Trans. A 2015, 46, 1419–1432. [CrossRef]
110. Xue, J.; Feng, Z.; Tang, J.; Tang, C.; Zhao, Z. Selective laser melting additive manufacturing of tungsten with niobium alloying:
Microstructure and suppression mechanism of microcracks. J. Alloys Compd. 2021, 874, 159879. [CrossRef]
111. Ng, G.K.L.; Jarfors, A.E.W.; Bi, G.; Zheng, H.Y. Porosity formation and gas bubble retention in laser metal deposition.Appl. Phys.
A 2009, 97, 641–649. [CrossRef]

## Page 39

Crystals 2024, 14, 665 39 of 40
112. Zhong, M.; Liu, W.; Ning, G.; Yang, L.; Chen, Y. Laser direct manufacturing of tungsten nickel collimation component.J. Mater.
Process Technol. 2004, 147, 167–173. [CrossRef]
113. Li, J.; Wu, Y.; Zhou, B.; Wei, Z. Laser Powder Bed Fusion of Pure Tungsten: Effects of Process Parameters on Morphology.Densif.
Microstruct. Mater. 2020, 14, 165. [CrossRef]
114. Dong, J.; Liu, S.; Chen, H.; Li, D.; Zhang, T.; Chen, C.; Zhou, K. Effect of atmosphere on the microstructure and properties of
additively manufactured tungsten. Mater. Sci. Technol. 2020, 36, 1988–1996. [CrossRef]
115. Huang, J.; Li, M.; Wang, J.; Pei, Z.; Mclntyre, P .; Ma, C. Selective laser melting of tungsten: Effects of hatch distance and point
distance on pore formation. J. Manuf. Process 2021, 61, 296–302. [CrossRef]
116. Adamson, A.W. Potential distortion model for contact angle and spreading. II. Temperature dependent effects. J. Colloid. Interface
Sci. 1973, 44, 273–281. [CrossRef]
117. Muramatsu, Y.; Halada, K.; Dan, T.; Isoda, Y. Solid-Liquid Interfacial Tension of the W-Cu System. J. Jpn. Inst. Met. 1990, 54,
679–684. [CrossRef]
118. Pan, S.; Guan, Z.; Yao, G.; Yuan, J.; Li, X. Mo-enhanced chemical stability of TiC nanoparticles in molten Al. J. Alloys Compd. 2021,
856, 158169. [CrossRef]
119. Wei, C.; Gu, H.; Gu, Y.; Liu, L.; Huang, Y.; Cheng, D.; Li, Z.; Li, L. Abnormal interfacial bonding mechanisms of multi-material
additive-manufactured tungsten–stainless steel sandwich structure. Int. J. Extrem. Manuf. 2022, 4, 025002. [CrossRef]
120. Li, K.; Wang, D.; Xing, L.; Wang, Y.; Yu, C.; Chen, J.; Zhang, T.; Ma, J.; Liu, W.; Shen, Z. Crack suppression in additively
manufactured tungsten by introducing secondary-phase nanoparticles into the matrix. Int. J. Refract. Met. Hard Mater. 2019, 79,
158–163. [CrossRef]
121. Kurishita, H.; Matsuo, S.; Arakawa, H.; Sakamoto, T.; Kobayashi, S.; Nakai, K.; Okano, H.; Watanabe, H.; Yoshida, N.; Torikai, Y.;
et al. Current status of nanostructured tungsten-based materials development. Phys. Scr. T 2014, 159, 014032. [CrossRef]
122. Nagy, D.; Humphry-Baker, S.A. An oxidation mechanism map for tungsten. Scr. Mater. 2022, 209, 114373. [CrossRef]
123. Warren, A.; Nylund, A.; Olefjord, I. Oxidation of tungsten and tungsten carbide in dry and humid atmospheres.Int. J. Refract.
Met. Hard Mater. 1996, 14, 345–353. [CrossRef]
124. Savitskii, E.M.; Burkhanov, G.S.Physical Metallurgy of Refractory Metals and Alloys; Springer US: Boston, MA, USA, 1995. [CrossRef]
125. Naghshineh, B.; Ribeiro, A.; Jacinto, C.; Carvalho, H. Social impacts of additive manufacturing: A stakeholder-driven framework.
Technol. Forecast. Soc. Chang. 2021, 164, 120368. [CrossRef]
126. Antusch, S.; Klein, A.; Baumgärtner, S.; Bonnekoh, C.; Böswirth, B.; Dorow-Gerspach, D.; Dietrich, S.; Ehrhardt, M.; Ghidersa,
B.-E.; Greuner, H.; et al. Additive manufacturing of novel complex tungsten components via electron beam melting: Basic
properties and evaluation of the high heat flux behavior. Nucl. Mater. Energy 2024, 39, 101683. [CrossRef]
127. Eckley, C.C.; Kemnitz, R.A.; Fassio, C.P .; Hartsfield, C.R.; Leonhardt, T.A. Selective Laser Melting of Tungsten-Rhenium Alloys.
JOM 2021, 73, 3439–3450. [CrossRef]
128. Yamamoto, T.; Hara, M.; Hatano, Y. Cracking behavior and microstructural. mechanical and thermal characteristics of tungsten–
rhenium binary alloys fabricated by laser powder bed fusion. Int. J. Refract. Metals Hard Mater. 2021, 100, 105651. [CrossRef]
129. Klopp, W.; Witzke, W.; Raffo, P . Mechanical Properties of Dilute Tungsten-Rhenium Alloys. 1966. Available online:
https://www.semanticscholar.org/paper/Mechanical-properties-of-dilute-tungsten-rhenium-Klopp-Witzke/f3a5af30bb932
de1537aaa486f215920185ab265 (accessed on 15 July 2024).
130. Zhang, D.Q.; Liu, Z.H.; Cai, Q.Z.; Liu, J.H.; Chua, C.K. Influence of Ni content on microstructure of W–Ni alloy produced by
selective laser melting. Int. J. Refract. Met. Hard Mater. 2014, 45, 15–22. [CrossRef]
131. Zhang, D.; Cai, Q.; Liu, J.; Li, R. Research on Process and Microstructure Formation of W-Ni-Fe Alloy Fabricated by Selective
Laser Melting. J. Mater. Eng. Perform. 2011, 20, 1049–1054. [CrossRef]
132. Ivekovi´ c, A.; Montero-Sistiaga, M.L.; Vanmeensel, K.; Kruth, J.-P .; Vleugels, J. Effect of processing parameters on microstructure
and properties of tungsten heavy alloys fabricated by SLM. Int. J. Refract. Met. Hard Mater. 2019, 82, 23–30. [CrossRef]
133. Hu, Z.; Liu, Y.; Wu, J.; Dong, J.; Ma, Z.; Liu, Y. The simultaneous improvement of strength and ductility of the 93W-4.6Ni-2.4Fe
prepared by additive manufacturing via optimizing sintering post-treatment. Addit. Manuf. 2021, 46, 102216. [CrossRef]
134. Chen, H.; Zi, X.; Han, Y.; Dong, J.; Liu, S.; Chen, C. Microstructure and mechanical properties of additive manufactured
W-Ni-Fe-Co composite produced by selective laser melting. Int. J. Refract. Met. Hard Mater. 2020, 86, 105111. [CrossRef]
135. Wang, M.; Li, R.; Yuan, T.; Chen, C.; Zhang, M.; Weng, Q.; Yuan, J. Selective laser melting of W-Ni-Cu composite powder:
Densification, microstructure evolution and nano-crystalline formation. Int. J. Refract. Met. Hard Mater. 2018, 70, 9–18. [CrossRef]
136. Yan, A.; Wang, Z.; Yang, T.; Wang, Y.; Ma, Z. Microstructure, thermal physical property and surface morphology of W-Cu
composite fabricated via selective laser melting. Mater. Des. 2016, 109, 79–87. [CrossRef]
137. Li, R.; Shi, Y.; Liu, J.; Xie, Z.; Wang, Z. Selective laser melting W–10 wt.% Cu composite powders. Int. J. Adv. Manuf. Technol. 2010,
48, 597–605. [CrossRef]
138. Wang, G.; Qin, Y.; Yang, S. Characterization of laser-powder interaction and particle transport phenomena during laser direct
deposition of W–Cu composite. Addit. Manuf. 2021, 37, 101722. [CrossRef]
139. Zhou, Z.; Tan, Z.; He, D.; Zhou, Z.; Cui, L.; Wang, Y.; Shao, W.; Wang, G. Fabrication of three-dimensional connected W-Cu10Sn
composites by selective laser melting. Mater. Lett. 2020, 264, 127377. [CrossRef]
140. Li, K.; Li, Y.; Chen, W.; Zhao, C.; Yuan, Y.; Cheng, L.; Morgan, T.W.; Liu, W.; Shen, Z. Effect of Ta addition on the fuzz formation of
additively manufactured W-based materials. Nucl. Fusion. 2020, 60, 064004. [CrossRef]

## Page 40

Crystals 2024, 14, 665 40 of 40
141. Li, K.; Ma, G.; Xing, L.; Wang, Y.; Yu, C.; Chen, J.; Ma, J.; Wu, G.; Liu, W.; Shen, Z.; et al. Crack suppression via in-situ oxidation in
additively manufactured W-Ta alloy.Mater. Lett. 2020, 263, 127212. [CrossRef]
142. Guo, Z.; Wang, L.; Wang, X.-Z. Additive manufacturing of W-12Ta(wt%) alloy: Processing and resulting mechanical properties.
J. Alloys Compd. 2021, 868, 159193. [CrossRef]
143. Li, J.; Wei, Z.; Zhou, B.; Wu, Y.; Chen, S.-G.; Sun, Z. Preparation, microstructure, and microhardness of selective laser-melted
W–3Ta sample. J. Mater. Res. 2020, 35, 2016–2024. [CrossRef]
144. Xiao, B.; Jia, W.; Tang, H.; Wang, J.; Zhou, L. Microstructure and mechanical properties of a newly developed WTaRe refractory
alloy by selective electron beam melting. Addit. Manuf. 2022, 54, 102738. [CrossRef]
145. Xiao, B.; Jia, W.; Wang, J.; Zhou, L. High-temperature mechanical behaviors of a WTaRe refractory alloy manufactured by selective
electron beam melting. Int. J. Refract. Met. Hard Mater. 2023, 116, 106371. [CrossRef]
146. Chen, H.; Ye, L.; Han, Y.; Chen, C.; Fan, J. Additive manufacturing of W–Fe composites using laser metal deposition: Microstruc-
ture, phase transformation, and mechanical properties. Mater. Sci. Eng. A 2021, 811, 141036. [CrossRef]
147. Tan, Z.; Zhou, Z.; Wu, X.; Wang, Y.; Shao, W.; Guo, X.; Zhou, Z.; Yang, Y.; Wang, G.; He, D. In situ synthesis of spherical W Mo
alloy powder for additive manufacturing by spray granulation combined with thermal plasma spheroidization. Int. J. Refract.
Met. Hard Mater. 2021, 95, 105460. [CrossRef]
148. Lang, S.; Sun, N.; Cao, J.; Yu, W.; Yang, Z.; Hou, S. Fabrication of Ultra-Fine-Grained W-TiC Alloys by a Simple Ball-Milling and
Hydrogen Reduction Method. Materials 2021, 14, 5865. [CrossRef] [PubMed]
149. Gu, D.; Dai, D.; Chen, W.; Chen, H. Selective Laser Melting Additive Manufacturing of Hard-to-Process Tungsten-Based Alloy
Parts with Novel Crystalline Growth Morphology and Enhanced Performance. J. Manuf. Sci. Eng. 2016, 138, 081003. [CrossRef]
150. Chen, J.; Zhao, C.; Li, K.; Li, M.; Sun, S.; Zhang, S.; Ma, J.; Liu, W. Effect of TaC addition on microstructure and microhardness of
additively manufactured tungsten. J. Alloys Compd. 2022, 897, 162978. [CrossRef]
151. Cole, N.C.; Gilliland, R.G.; Slaughter, G.M. Weldability of tungsten and its alloys. In Proceedings of the American Welding Society
49th Annual Meeting, Chicago, IL, USA, 1–5 April 1968.
152. Bose, A.; German, R.M. Microstructural refinement of W-Ni-Fe heavy alloys by alloying additions. Metall. Trans. A 1988, 19,
3100–3103. [CrossRef]
153. Luo, A.; Jacobson, D.L.; Shin, K.S. Solution softening mechanism of iridium and rhenium in tungsten at room temperature. Int. J.
Refract. Met. Hard Mater. 1991, 10, 107–114. [CrossRef]
154. Wang, Y.K.; Xie, Z.M.; Wang, M.M.; Deng, H.W.; Yang, J.F.; Jiang, Y.; Zhang, T.; Wang, X.P .; Fang, Q.F.; Liu, C.S. The superior
thermal stability and tensile properties of hot rolled W-HfC alloys. Int. J. Refract. Met. Hard Mater. 2019, 81, 42–48. [CrossRef]
155. Leonhardt, T. Properties of tungsten-rhenium and tungsten-rhenium with hafnium carbide. JOM 2009, 61, 68–71. [CrossRef]
156. Ren, C.; Fang, Z.Z.; Koopman, M.; Butler, B.; Paramore, J.; Middlemas, S. Methods for improving ductility of tungsten—A review.
Int. J. Refract. Met. Hard Mater. 2018, 75, 170–183. [CrossRef]
157. Calvo, A.; Schlueter, K.; Tejado, E.; Pintsuk, G.; Ordás, N.; Iturriza, I.; Neu, R.; Pastor, J.Y.; García-Rosales, C. Self-passivating
tungsten alloys of the system W-Cr-Y for high temperature applications.Int. J. Refract. Met. Hard Mater. 2018, 73, 29–37. [CrossRef]
158. Zhang, Y.; Huang, Y.; Liu, W.; Ma, Y.; Wang, Y.; Liang, C. Effect of tantalum addition method on microstructure and mechanical
properties of the 90(W 20Ta)–Ni–Fe alloy.Int. J. Refract. Met. Hard Mater. 2022, 105, 105848. [CrossRef]
159. Chen, B.; Li, Z.-B.; Liu, J.-R.; Zhang, G.-H. Effect of molybdenum addition on microstructure and mechanical properties of 90%
tungsten heavy alloys. Int. J. Refract. Met. Hard Mater. 2022, 106, 105868. [CrossRef]
160. Xie, Z.M.; Liu, R.; Miao, S.; Yang, X.D.; Zhang, T.; Wang, X.P .; Fang, Q.F.; Liu, C.S.; Luo, G.N.; Lian, Y.Y.; et al. Extraordinary
high ductility/strength of the interface designed bulk W-ZrC alloy plate at relatively low temperature. Sci. Rep. 2015, 5, 16014.
[CrossRef] [PubMed]
161. Suman, V .; Chaira, D. Improvement of Oxidation Resistance in Tungsten Heavy Alloys through Si, Y2O3, Ni, and Co Addition.J.
Mater. Eng. Perform. 2023, 33, 5279–5290. [CrossRef]
162. Yin, C.; Terentyev, D.; Zhang, T.; Nogami, S.; Antusch, S.; Chang, C.-C.; Petrov, R.H.; Pardoen, T. Ductile to brittle transition
temperature of advanced tungsten alloys for nuclear fusion applications deduced by miniaturized three-point bending tests. Int.
J. Refract. Met. Hard Mater. 2021, 95, 105464. [CrossRef]
163. Sharma, S.; Joshi, S.S.; Pantawane, M.V .; Radhakrishnan, M.; Mazumder, S.; Dahotre, N.B. Multiphysics multi-scale computational
framework for linking process–structure–property relationships in metal additive manufacturing: A critical review. Int. Mater.
Rev. 2023, 68, 943–1009. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
