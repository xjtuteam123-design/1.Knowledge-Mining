# Lesieur-2026-Effects-of-niobium-on-the-mechanica

<!-- source: D:\总文献\Lesieur-2026-Effects-of-niobium-on-the-mechanica.pdf -->
<!-- file_sha256: c8962796546c07f5f4845ce4cfe1694e3c29e26203b9e5ba2bff02300051603a -->

## Page 1

RESEARCH
Progress in Additive Manufacturing (2026) 11:7183–7193
https://doi.org/10.1007/s40964-026-01722-8
 
 Cayla Eckley
cayla.eckley.1@us.af.mil
Alexander LeSieur
alexander.lesieur.2@us.af.mil
Ryan Kemnitz
ryan.kemnitz.1@us.af.mil
1 Air Force Institute of Technology, Dayton, USA
Abstract
Although additive manufacturing presents a novel and customizable approach to fabricating tungsten (W) alloys, the 
layer-by-layer production technique presents a unique set of processing challenges which are further exacerbated by the 
metal’s refractory properties. In this study, additions of niobium (Nb) were found to improve the mechanical properties and 
oxidation resistance of additively manufactured W. Microstructural investigation revealed the effect of Nb on the crack -
ing, grain size, and texture in the as-built material. Mechanical compression testing showed significant improvement in 
ductility with increasing Nb content. The low concentrations of Nb used did not induce large changes in the yield strength 
of the material. The work shows that Nb may be a useful alloying element for improving additive manufacturing of W.
Keywords Tungsten · Niobium · Oxidation · Laser powder bed fusion · Additive manufacturing
Received: 19 August 2025 / Accepted: 22 April 2026 / Published online: 12 May 2026
This is a U.S. Government work and not under copyright protection in the US; foreign copyright protection may apply 2026
Effects of niobium on the mechanical and oxidation properties of 
additively manufactured tungsten
Alexander LeSieur1 · Cayla Eckley1 · Ryan Kemnitz1
additions, the DBTT can vary significantly. Furthermore, 
when in polycrystalline form, W is highly susceptible to 
grain boundary attack by segregating interstitial impuri -
ties, promoting intergranular decohesion, which worsens 
deformation performance [ 4, 5]. In addition to the afore -
mentioned embrittlement mechanisms, W also has the high-
est cohesive energy of all elements, resulting from covalent 
bonds which form between its atoms’ valence 5d electron 
orbitals [6]. Collectively, these material properties make W 
very challenging to manufacture through traditional meth -
ods and additive manufacturing (AM) has been identified as 
a promising technology for producing geometrically com -
plex W parts that would be time-consuming or impossible 
to manufacture otherwise. As a result, publications on addi-
tively manufactured W have steadily increased over the past 
two decades, with the majority of studies using laser powder 
bed fusion (LPBF) to print W [7].
A limited number of studies have also investigated print-
ing W using directed energy deposition (DED) and electron 
beam powder bed fusion (EB-PBF) [8–12]. Parts manufac-
tured by DED exhibit a very rough surface finish compared 
to LPBF, necessitating some form of post processing to 
achieve the desired geometry [13]. The added time of post-
processing limits the productivity of using DED to produce 
geometrically complex components, especially when print-
ing W which is difficult to machine. In the case of EB-PBF, 
while the vacuum chamber is beneficial in minimizing the 
1 Introduction
As a member of the refractory metals group, tungsten 
(W) is known for its exceptional physical and mechani -
cal properties. Exhibiting a melting point of 3422 °C and 
tensile strength at 1650 °C of 172 MPa, both of which are 
the highest of all pure metals, W is a leading candidate for 
extreme temperature structural material applications in 
aerospace and space propulsion as well as for use in nuclear 
fusion reactors [ 1–3]. Unfortunately, its exceptional attri -
butes also create distinct manufacturing challenges which 
restrict its practical usage in commercial and industrial set -
tings. Owing to its body-centered cubic (BCC) crystalline 
structure, W’s lack of a well-defined slip system results in 
temperature-dependent plastic flow properties which give 
rise to its high Peierls stress and ductile-to-brittle transition 
temperature (DBTT) of 200–300 °C [ 1]. Depending upon 
the processing route, impurities in the sample, and alloying

## Page 2

1 3
7184
Progress in Additive Manufacturing (2026) 11:7183–7193
oxygen presence in the build chamber, the complex nature 
of the machine does not lend itself well to scaling up to 
larger build chambers needed to build large components for 
the aerospace and power generation sectors. Additionally, 
the high temperature preheating inherent to the EB-PBF 
process can cause sintering of the powder in the powder bed 
which limits the recyclability of powders, which is espe -
cially relevant with refractory metals due to their high costs. 
The preheating step is typically accomplished by rastering 
the defocused electron beam over the powder bed, which 
may add a nontrivial amount of time to the overall build 
process if the preheat temperature is high. Both of these 
additional factors are drawbacks to productivity and cost-
effectiveness of the EB-PBF process. Therefore, based upon 
the broader use of LPBF in the W literature and disadvan -
tages to utilizing DED and EB-PBF for producing refractory 
components, LPBF was chosen as the additive manufactur-
ing method for the present study.
However, there are many factors unique to the LPBF 
process that must be explored in order to improve the print-
ability of pure W and the final part quality. The distinct char-
acteristics of W discussed previously result in an increased 
susceptibility to residual stress and crack development, 
as well as a high surface tension and poor wettability, all 
of which impede LPBF processing [ 14–16]. Nonetheless, 
many advancements in the LPBF process have enabled the 
production of additively manufactured W materials which 
exhibit relative densities of over 99%. LPBF machines 
with increased laser energy input have overcome the high 
melting temperature and surface tension of W, resulting in 
more consistent welding, while improved purity in powder 
feedstocks and lower oxygen presence in the build cham -
ber during printing have both helped to reduce the delete -
rious effects of oxygen on grain boundary cohesion [ 15, 
16]. Build plate preheating has also been utilized to heat 
the material above the DBTT and decrease residual stress 
driven cracking [17, 18].
Despite these improvements, additively manufacturing 
W that maintains strength at high temperature and sufficient 
ductility at room temperature to resist cracking during pro -
cessing remains a challenge. Efforts to produce crack free, 
and highly dense pure W parts through LPBF have not yet 
been met with success. There have been suggestions of 
achieving crack-free W in the literature but similar find -
ings have not been widely reported by different researchers 
using similar methods [19, 20]. Alloying has been one of the 
primary routes to improve W’s room temperature ductility, 
particularly through alloying with rhenium [ 21–24]. When 
retention of its favorable high temperature and strength 
properties is of chief importance, W is often alloyed with 
one or more other refractory metals, including niobium 
(Nb), molybdenum (Mo), rhenium (Re), and tantalum (Ta). 
Nb exhibits the lowest density of the refractory metals of 
8.57 g/cm3, which would provide the greatest reduction in 
density when alloyed with W. Nb also induces a favorable 
solid solution strengthening (SSS) effect when alloyed into 
W, resulting from atomic size differences which distort its 
lattice structure and restrict dislocation motion [ 25]. Nb 
also reacts more readily with oxygen than W, allowing it to 
serve as an oxygen getter, thereby reducing the segregation 
of oxygen to grain boundaries and improving microcracking 
and grain boundary cohesion in pure W [26]. Since the two 
elements exhibit unlimited solid solubility with each other, 
W-Nb alloy compositions are adjustable based on design 
requirements and desired material properties.
To date, there is very limited experimental research on 
W-Nb alloys, with only one publication examining the 
binary system from an AM perspective by Xue et al. [ 26]. 
The work of Xue et al. centered on a single formulation, 
W-5Nb, in lieu of a range of compositions. Building upon 
this foundational work, the present study aims to evaluate an 
array of LPBF-produced W-Nb alloy compositions through 
microstructural and mechanical investigations. Literature 
suggests the W DBTT may be as high as 200–300 °C or 
higher depending upon the oxygen content of the alloy [ 1]. 
Mechanical tests were performed from room temperature 
up to 400 °C to assess the effect of the additions of Nb on 
the DBTT of the alloys produced in this study. Short-term 
oxidation behavior was investigated to probe any potential 
oxidation resistance benefits imparted by Nb to the alloy. 
For comparative purposes, pure W samples were also exam-
ined in order to isolate contributions from the dilute Nb 
additions.
2 Materials and methodology
2.1 Test specimen design and construction
W-Nb alloys were manufactured with Nb concentrations 
ranging from 3 to 11 wt% to capture the effects of increas -
ing Nb content on LPBF-produced W. Alloy compositions 
were mixed from pure powder feedstocks using a Resodyn 
LabRAM II acoustic mixer to ensure a uniform particle dis-
tribution. Mixing of the powders was qualitatively evalu -
ated using back-scatter electron microscopy and energy 
dispersive spectroscopy (EDS), and representative images 
are displayed in Fig. 1. Table 1 lists various specifications 
for the pure W and Nb powders used to produce all samples 
examined in this study.
An initial processing parameter optimization procedure 
was performed to identify the printing configuration which 
resulted in the fewest printing defects. Comparisons were 
qualitative, using a Tescan MIRA-3 field emission Scanning

## Page 3

1 3
7185
Progress in Additive Manufacturing (2026) 11:7183–7193
Electron Microscope (SEM) to examine the as-printed spec-
imens’ top surfaces, minimizing the appearance of crack -
ing, balling, and porosity. The final fabrication settings that 
were chosen as a result of this process are listed in Table 2. 
Cylindrical test specimens were produced with dimensions 
of 6.5 mm in diameter and 10 mm in height. All specimens 
were manufactured using a GE Additive Concept Laser M2 
printer equipped with a 50 μm diameter, 200 W continuous 
wave fiber laser. Specimens were consolidated on copper 
substrates under a nitrogen shielding gas. Nitrogen was cho-
sen as a shielding gas in the current work based on a study 
by Dong et al. which demonstrated that additively manu -
factured W exhibits higher density and mechanical strength 
when printed in nitrogen compared to W printed in argon 
[20]. Additionally, Dong et al. observed that the ductility 
of the nitrogen shield gas printed specimens was similar or 
better than the specimens printed in argon, which suggests 
that while the nitrogen content was slightly higher in the 
nitrogen-produced samples, the nitrides formed did not lead 
to embrittlement of W. Precise characterization of nitride 
formation was deemed to be beyond the scope of the pres -
ent work and will be addressed in a future study.
After AM processing, as-printed samples were separated 
from the build plates by wire electrical discharge machining 
(EDM) using a 0.5 mm offset. Next, the specimens were 
readied for subsequent analysis using a Buehler EcoMet 300 
grinding and polishing system. All compression test samples 
were ground using 320-grit SiC paper to achieve a uniform 
diameter and flat circular faces. Metallographic specimens 
were mounted in a thermoset polymer mold and prepared 
for examination through standard grinding and polishing 
procedures. Samples were first ground with SiC papers, up 
to 800 grit, before being polished sequentially with 9 μm, 
3 μm, and 1 μm polycrystalline diamond polishes.
2.2 Materials characterization
As-built test specimens were evaluated using an array of both 
non-destructive and destructive materials characterization 
techniques. For metallographic analysis, each formulation was 
imaged using the SEM, which was performed in conjunction 
with Electron Backscatter Diffraction (EBSD). Prior to EBSD 
analysis, samples were prepared by vibratory polishing over-
night in a Saphir Vibro polisher with a colloidal silica solution 
to accentuate grain characteristics and improve data precision.
Compression tests were performed under atmospheric con-
ditions at temperatures from 25 to 400 °C, using an MTS 810 
system. The tests were conducted in displacement control with 
a displacement rate corresponding to a strain rate of 10− 3 s− 1. 
Hardened steel compression platens were employed during 
room temperature trials, while elevated temperature testing 
was accomplished using an MTS 653 furnace in conjunction 
with machined W rods held by cylindrical MTS 647 hydraulic 
wedge grips. The furnace temperature settings were calibrated 
by attaching a thermocouple to a W sample held in the test con-
figuration. The furnace ramp rate was set to 40 °C per minute.
Cyclic oxidation testing was performed at 1000 °C for 
4 h in a Cress electric furnace. Samples were loaded into the 
furnace at the test temperature and removed in hourly inter-
vals for weight measurements and qualitative imaging. X-ray 
Table 1 Selected characteristics of the powdered metals used during 
specimen production
Tungsten Niobium
Supplier Tekna (Quebec, 
Canada)
Heeger Materials (Denver, 
USA)
Shape Spherical Spherical
D10 (µm) 1.45 1.10
D50 (µm) 6.91 5.72
D90 (µm) 13.74 28.00
Purity (wt%) 99.9 99.9
Impurities 
(wt%)
Cr-< 0.001, Fe-< 
0.001, Ni-< 0.1, O-< 
0.025
Fe-< 0.005, Ni-< 0.002, 
Si-< 0.002, Mo-< 0.002, 
W-< 0.005, Al-< 0.002, Ti-< 
0.001, Ta-< 0.05, C-0.0015, 
H-0.0011, N-0.0077, O-0.02
Table 2 AM processing parameters used to fabricate the materials 
examined in this study
Processing parameter Value
Laser power (W) 400
Scan speed (mm/s) 400
Hatch spacing (µm) 50
Powder height (µm) 30
Interlayer rotation (°) 67
Fig. 1 Back-scattered electron 
microscope image and EDS map of 
a W-7Nb powder sample show-
ing the dispersion of W and Nb 
powders

## Page 4

1 3
7186
Progress in Additive Manufacturing (2026) 11:7183–7193
Diffraction (XRD) was performed on each specimen before 
and after testing with a Rigaku Smartlab Studio II instrument 
equipped with a 9 kW rotating anode X-ray source.
3 Results and discussion
3.1 Metallography analysis
As-printed specimens were mounted laying on their sides to 
show microstructural features along the build direction (BD). 
Representative SEM images of the specimens are shown in Fig. 
2. Qualitative analysis and comparison of cracking between 
pure W and W-Nb alloys containing up to 7 wt% Nb, revealed 
an apparent reduction in microstructural cracking. Xue et al. 
[26] documented similar results while studying LPBF-pro -
duced W-5Nb, which they attributed to a decrease in nanopores 
arising from evaporating oxides, as well as improved grain 
boundary cohesion provided by SSS. The reduced cracking 
observed in alloys containing 3–7 wt% Nb in the current work 
lends support to Xue et al.’s conclusions, although the quali-
tative nature of the crack analysis performed in both studies 
limits the ability to make direct comparisons of cracking den-
sity. In contrast to these compositions, specimens containing 
9 and 11 wt% Nb exhibited severely cracked microstructures. 
Furthermore, these Nb-rich compositions also exhibited small 
areas of poor mixing of the W and Nb powders, represented 
by the EDS maps shown in Fig. 3. It is suspected the 9 and 11 
wt% Nb content alloys underwent cracking in response to large 
residual stress accumulations, as discussed in further detail in 
Sect. 3.2.
Alloys containing at least 5 wt% Nb displayed localized 
areas of apparent sub-grain structures, such as the region 
highlighted in Fig. 4, with the cell wall boundaries serving 
as preferential nanopore formation sites. Similar features 
were also observed by Wang et al. in their study on LPBF-
produced W alloyed with 6 wt% Ta [ 27]. They theorized 
these subgrain features entrapped pores resulting from tung-
sten oxide (WO x) gasification in the laser melt pool, pre -
venting their aggregation along grain boundaries where they 
could serve as crack nucleation sites.
Figure 5 contains inverse pole figure (IPF) maps for pure 
W, W-3Nb, and W-7Nb, which were selected as character -
istic formulations for illustrating the impact of Nb additions 
on the crystallographic structure of LPBF W. Corroborating 
the SEM imagery analysis, the IPF map data reveals a dis -
tinct columnar-to-equiaxed grain structure transition result-
ing from the increasing Nb concentration. This indicates 
Fig. 2 Microstructural comparison of the studied formulations. Build direction (BD) indicated

## Page 5

1 3
7187
Progress in Additive Manufacturing (2026) 11:7183–7193
the Nb additions effectively suppressed the development of 
columnar grains typical of LPBF W which cause anisotro -
pic, directionally-dependent properties [ 28]. Additionally, 
EBSD-derived grain structure data is provided in Table 3. 
As evidenced by the relatively minor MUD readings, nei -
ther pure W nor any of the W-Nb formulations displayed 
a strong preferential crystallographic texture, with Nb-rich 
alloys exhibiting the lowest values. Nonetheless, the added 
Nb solutes eliminated the modest {111} texture exhibited 
by pure W, which was also observed in LPBF W studies 
conducted by Wright [29] and Kemnitz et al. [ 30]. Consis-
tent with qualitative SEM imaging results, the EBSD data 
also captured the grain refinement induced by the addition 
of Nb; all W-Nb specimens exhibited average grain diam -
eters lower than pure W. The decrease in grain diameter cor-
responds with increasing Nb content up to 7 wt% beyond 
which greater additions of Nb did not produce further 
decrease in grain diameter.
3.2 Mechanical testing
Yield and ultimate compression strength (UCS) measure -
ments obtained through compression testing performed at 
Table 3 Various EBSD-derived parameters for the examined W-Nb 
formulations, including multiples of uniform distribution (MUD), a 
variable used to quantify a material’s degree of crystallographic tex -
ture
Average grain characteristics
wt% Nb Diameter (µm) Misorientation angle MUD
0 16.52 7.08 3.771
3 13.19 17.84 3.255
5 12.48 20.67 4.742
7 10.66 21.79 2.251
9 11.08 20.97 1.324
11 10.84 20.93 1.719
In practice, values under 7 indicate a lack of preferential texture
Fig. 5 Inverse pole figure maps of pure W, W-3Nb, and W-7Nb along with a reference standard showing the color scheme for BCC crystallographic 
directions
 
Fig. 4 Subgrain cell walls observed within the grain of a W-5Nb 
specimen
 
Fig. 3 Scanning electron microscope images of W-9Nb with corresponding EDS maps of Nb and W

## Page 6

1 3
7188
Progress in Additive Manufacturing (2026) 11:7183–7193
both room and elevated temperatures are provided in Fig. 6. 
Overall, all W-Nb specimens exhibited superior yield and 
ultimate strengths and ductility in comparison to pure W. 
The room temperature yield strength and UCS of pure W 
was 738.7 and 855.3 MPa, respectively. Among all tested 
formulations, W-9Nb registered the highest yield and ulti -
mate strengths of 909.1 and 1755.9 MPa, respectively. 
These strength improvements likely resulted from a combi-
nation of SSS, more equiaxed grains, grain size reduction, 
and reduced oxygen concentration at the grain boundaries 
because of Nb’s oxygen gettering effect.
The yield strength increases weakly as Nb content 
increases but appears to remain constant in the range of 
7–11 wt% Nb. Similar behavior is evident in the grain size 
measurements reported in Table 3, where the grain size 
decreases until W-7Nb, but then remains consistent through 
W-11Nb. Grain size can affect the yield strength through 
a Hall-Petch relationship, which may explain why the two 
relationships follow a similar trend; however, an increase in 
yield strength due to SSS is expected to occur in this com -
position range. The discrepancy may be a result of difficulty 
achieving a homogeneous mixture at the higher concentra -
tions of Nb.
W-11Nb exhibited reduced room temperature mechani -
cal performance, including a reduction in UCS compared 
to W-9Nb. Comparing these results with the specimen sur -
face images provided in Fig. 3, this deviation from the linear 
relationship observed between Nb content and compressive 
strength was attributed to the relatively defective morphol -
ogy of W-11Nb, as a result of the greater accumulation of 
residual stress as Nb content increased. The noted decline in 
mechanical strength from W-9Nb to W-11Nb did not occur 
in the 200 and 400 °C tests, which may point to higher duc-
tility and ability to bear load in the presence of cracks in this 
temperature range.
Strain measurements recorded at the UCS of each alloy 
are listed in Table 4. All samples failed by the formation of 
cracks in their sides and rapid load drop shortly after reach-
ing the UCS. Although an increase in strain occurs with the 
addition of Nb, the relatively low strain values suggest all 
specimens experienced brittle failure, independent of test -
ing temperature. These findings were verified through SEM 
analysis of specimens after compression testing, which 
overwhelmingly exhibited brittle intergranular fracture sur-
faces. Representative SEM images of the side fracture sur -
faces are displayed in Fig. 7. The various pieces of evidence 
suggest that the DBTT of these alloys is likely above the 
Table 4 Strain at UCS recorded for each alloy/test temperature configuration, as well as the percent increase in comparison to pure W baseline 
measurements
wt% Nb Testing temperature (°C)
25 200 400
Strain (%) % Inc. Strain (%) % Inc. Strain (%) % Inc.
0 4.22 – 4.66 – 5.66 –
3 10.50 149 13.90 198 12.87 127
5 12.44 195 15.69 237 24.87 339
7 16.59 293 16.97 264 16.69 195
9 17.43 313 16.95 264 20.52 263
11 13.08 210 14.25 206 17.50 209
Fig. 6 Yield strength and ultimate compressive strength (UCS) values for each of the tested alloys, categorized by ambient testing temperature

## Page 7

1 3
7189
Progress in Additive Manufacturing (2026) 11:7183–7193
tested maximum temperature, indicating that Nb did not sig-
nificantly affect the DBTT. Müller et al. found that cracking 
occurred even when pre-heating AM W to 1000 °C, sug -
gesting that the DBTT of AM W may be much higher than 
the lower range of 200–300 °C, which is characteristic of 
traditionally manufactured W [1, 18].
Undoubtedly, one of the greatest challenges presented in 
manufacturing LPBF W is identifying methods to alleviate 
its predisposition to microcracking. Over a series of experi-
mental and computational investigations, Vrancken et al. 
[17, 31, 32] determined W intrinsically releases large resid-
ual stresses generated during LPBF through cracking, espe-
cially when the magnitude of the residual stresses exceeds 
the material’s yield strength. Furthermore, it was also con -
cluded the strain relaxation phenomenon is only resolvable 
through macroscopic production strategies. Specifically, the 
authors focused on employing build plate heating tempera -
tures at or above the metal’s DBTT as a means to promote 
dislocation motion and dissipate residual stresses. This 
strategy was not possible in the present work due to a lack 
of this feature on the LPBF machine used.
Alloying W with Nb is an effective technique for reduc -
ing the susceptibility of W to oxygen-induced grain bound-
ary embrittlement, resulting in intergranular strengthening. 
Specifically, Nb behaves as an oxygen getter, promoting 
impurity dissolution into the bulk material in lieu of inter -
granular segregation [33, 34]. Ultimately, this contributed to 
the reduced microcracking exhibited by W-Nb alloys con -
taining up to 7 wt% Nb in the current work, as well as by 
W-5Nb in the study performed by Xue et al. [26].
However, it is suspected the benefits of oxygen scaveng-
ing diminish above a certain solute concentration, as there 
are fewer freely available oxygen atoms to dissolve into 
the W-Nb matrix. Meanwhile, the effects of SSS become 
increasingly prominent as the proportion of Nb to W atoms 
in the material’s lattice structure rises. Applying the theory 
proposed by Vrancken et al., residual stress accumulations 
in W-9Nb and W-11Nb reached a critical threshold beyond 
which the specimens could no longer accommodate any 
further strain. Consequently, this led to the violent crack -
ing observed in Fig. 3. In response to these findings, future 
works could examine the efficacy of various residual stress 
reduction measures, such as build plate heating, as a means 
to reduce the accumulation of residual stress in W-Nb alloys.
3.3 High-temperature oxidation testing
Surface appearance and mass gain measurements from oxi-
dation trials conducted on each of the studied alloys are 
presented in Fig. 8. While all oxidized specimens exhibit 
yellow oxide scale indicative of WO3 formation [35], a com-
parison of the oxidized test sample surfaces reveals a dis -
tinct inverse correlation between Nb content and mass gain. 
The apparent decrease in scale formation with increasing 
Fig. 8 a Yellow WO3 scale exhib-
ited by each tested alloy formu-
lation following exposure to a 
1000 °C atmosphere for the speci-
fied time period. b Corresponding 
weight gain measurements for each 
of the imaged cylinders
 
Fig. 7 Representative scanning electron microscope images taken on 
the sides of the specimens displaying brittle fracture surfaces of pure 
W, W-3Nb, W-7Nb, and W-11Nb

## Page 8

1 3
7190
Progress in Additive Manufacturing (2026) 11:7183–7193
amounts of Nb, observed qualitatively in Fig. 8a, is corrobo-
rated by the mass gain data, shown in Fig. 8b. The addition 
of 3 wt% Nb resulted in a 45% decrease in mass gain after 4 
h of oxidation, compared to pure W. The addition of greater 
amounts of Nb led to a further reduction in mass gain, with 
a 64% decrease in mass gain achieved with 11 wt% Nb. Col-
lectively, these results indicate Nb additions provide W with 
a nontrivial improvement in oxidation resistance at short 
testing intervals.
By comparison, Telu et al. [36] found the addition of 30 
wt% Cr to pure W reduced mass gain at 1000 °C to nearly 
half of that observed in W after cyclic testing in lab air for 4 
h. In a similar 1000 °C oxidation study conducted cyclically 
in lab air on W-15Nb, Das et al. [ 37] also noted an inverse 
relationship between Nb alloying content and oxidative 
mass gain. Das et al. attributed the beneficial effect seen in 
their study to the formation of complex W-Nb-O oxides that 
were more protective than WO3. However, the mechanically 
alloyed and sintered samples produced by Das et al. exhib -
ited a heterogeneous, two-phase microstructure, making it 
challenging to directly compare the oxidation behavior to 
that of the material manufactured in the current work which, 
by comparison, exhibited greater homogeneity. Interdiffu -
sion of an alloy’s constituent elements plays a crucial role in 
oxidation behavior, and in turn is influenced by the homoge-
neity of the base material [38, 39].
Nonetheless, SEM analysis of the oxide scale adds 
credence to the idea of multiple different oxides forming. 
Representative surface oxides with a variety of morphologi-
cal variations are presented in Fig. 9. In pure W, the major-
ity of the scale was made up of spherical oxides of the type 
shown in Fig. 9a. The addition of any amount of Nb to the 
alloys seemed to produce a scale with greater morphologi -
cal diversity. Fine needle-like and larger rod-shaped oxide 
structures were observed, along with delicate, thread-like 
oxides that spanned cracks and fissures in the scale.
EDS was conducted on several of the oxides to deter -
mine which elements were present. The scales on the W-Nb 
alloys appeared to be predominately WO 3; however, sam -
ples with higher Nb content had an increasing presence of 
morphologically unique oxides that possessed a mixture of 
W, Nb, and O. Nb-rich oxides, highlighted by the red arrow 
in Fig. 9c, were identified alongside fine, needle-like W-rich 
oxides, and WO 3, which is indicated by the black arrow. 
The observation of a morphologically complex oxide scale 
seems to support the idea that the improvement of oxidation 
behavior is linked to the formation of a variety of oxides on 
the surface of the material.
In order to more carefully probe which oxides were form-
ing, XRD was used to interrogate the oxide scales of all W-Nb 
alloys. XRD data was collected across a 2θ range of 20° to 
80° using a scan speed of 4°/min. Figures 10 and 11 contain, 
respectively, pre- and post-oxidation XRD patterns of pure 
W, W-3Nb, and W-7Nb, which were chosen as representative 
plots for depicting trends observed across all alloys studied. 
The XRD diffractograms of pre-oxidized samples reveal a 
bulk material that is well alloyed. A slight leftward shift of 
the peaks was noted as a result of increasing Nb content. Peak 
shift corresponds to a change in the lattice parameter of the 
material, in this case indicating that the lattice parameter is 
increasing and therefore constructive interference is occur -
ring at a smaller angle. Nb has a larger atomic radius than 
W (145 pm vs. 135 pm) and as greater concentrations of Nb 
atoms are incorporated into the W lattice, they induce a slight 
expansion of the lattice, reflected in the XRD data [40]. Peak 
shift can also result from other microstructural alterations 
such as microstrain or grain size changes.
XRD diffractograms from the oxidized samples identify 
the primary constituent of the scale to be WO3, as expected 
from the observed yellow color and from the previous SEM 
analysis. An additional peak not identified in pure W was 
present at a 2θ value of 23° in compositions with Nb. Other 
peaks at 27° and 31° were identified in compositions with 
additions of Nb greater than 3 wt%, as shown in Fig. 11. The 
locations of these peaks align well with patterns taken from 
Nb pentoxide, Nb2O5, identified in previous studies [41, 42]. 
Nb2O5 has a more negative enthalpy of formation at 1000 °C 
compared to WO3, so it is likely that Nb pentoxide is form-
ing, although it may be overwhelmed in the scale by WO 3 
[43]. Another possibility is that complex W-Nb-O oxides are 
Fig. 9 Scanning electron microscope images of oxide scales from a 
pure W, b W-3Nb, c W-7Nb, and d W-11Nb after 4 h of exposure at 
1000 °C

## Page 9

1 3
7191
Progress in Additive Manufacturing (2026) 11:7183–7193
forming in addition to WO3 but are not detected by XRD due 
to the small volume of these oxides relative to WO3.
It was hypothesized that Nb additions to the alloys may 
have altered the Pilling-Bedworth (PB) ratio of the formed 
oxide, thus producing a more protective scale. PB ratios 
illustrate the volumetric difference between oxide scale and 
metal substrate, with ratios close to unity being the most 
protective. Unit cell dimensions for both the base metal 
alloys and oxides were calculated from the XRD spectra. 
These dimensions were used to calculate the volume of the 
alloys and the oxides, which allowed for the calculation of 
the PB ratio. Unit cell dimensions obtained from XRD dif -
fractograms, along with calculated density and PB ratios for 
pure W and all binary alloys are shown in Table 5. The vol-
ume of oxides was essentially the same across all composi-
tions with less than 0.25% difference compared to the oxide 
on the pure W sample. The volume change of the metal lat-
tice reached the maximum increase of 1.39% in the W-11Nb 
alloy. Therefore, it is unsurprising that the PB ratio did not 
vary significantly across all compositions, reaching its mini-
mum of 3.29 with the W-11Nb alloy, virtually unchanged 
from the baseline value of 3.33 for WO3 on pure W.
Oxidized samples were mounted in phenolic resin in 
order to make qualitative observations about adherence 
and density of the scale. Representative SEM images are 
presented in Fig. 12. In all samples, the scales were mark -
edly cracked and porous; however, a distinct difference was 
noted in the scale adherence in the binary alloys compared 
to the pure metal. The scale formed on pure W shows poor 
adherence to the underlying metal and large cracks and 
pores were observed along the entire scale-metal interface. 
The addition of Nb appears to improve the scale adhesion 
and although there is evidence of oxidation proceeding 
into the bulk material via fine cracks, the scale itself dem -
onstrated good adherence to the metal substrate across all 
W-Nb alloys. The formation of Nb 2O5 and mixed W-Nb-O 
oxides are believed to be promoting better chemical bond -
ing along the interface. A more in-depth exploration of this 
phenomenon will be pursued in a future study.
Table 5 Unit cell dimension, density, and PB ratio of pure W and all 
W-Nb alloys, as calculated from collected XRD data
wt% Nb Unit cell dimension 
(pm)
Calculated density 
(g/cm3)
PB 
ratio
0 316.89 ± 0.153 19.19 3.33
3 317.10 ± 0.043 18.60 3.33
5 317.32 ± 0.021 18.22 3.32
7 317.90 ± 0.082 17.78 3.31
9 318.00 ± 0.060 17.45 3.31
11 318.35 ± 0.115 17.08 3.29
Fig. 11 XRD patterns of pure W, W-3Nb, and W-7Nb with peaks 
labeled
 
Fig. 10 XRD patterns for pure W, W-3Nb, and W-7Nb, as recorded prior to oxidation testing, with peak shift highlighted

## Page 10

1 3
7192
Progress in Additive Manufacturing (2026) 11:7183–7193
4 Conclusions
The present work investigated the effects of 3–11 wt% Nb 
additions on the mechanical and oxidation performance 
of LPBF-produced W. Nb solute concentrations of up to 
7 wt% significantly improved the micro-cracking and oxi -
dation resistance properties of LPBF-produced W, as well 
as its compressive strength and ductility at both room and 
elevated temperatures. While a continued improvement in 
mechanical performance was realized at solute concen -
trations above this range, it was also accompanied by an 
increase in microstructural defects, which was attributed 
to an increased residual stress state resulting from the SSS 
effect of Nb. Future work to explore heat treating the sam -
ples to relieve these residual stresses, and testing samples at 
temperatures above 400 °C to observe the effect that oxida-
tion has on the mechanical strength of these alloys would be 
valuable. The addition of ternary elements to improve the 
ductility of the W-Nb binary alloys is also of interest.
In addition to its enhancement of the mechanical proper-
ties of W, Nb also provided a non-trivial improvement in 
oxidation resistance which was more prevalent with increas-
ing Nb content. The addition of Nb produces an oxide scale 
that is more closely adherent to the base metal, possibly 
due to the formation of Nb2O5 in the scale. A more in-depth 
exploration of the mechanism behind the oxidation benefit 
of Nb alloying will be pursued in a subsequent paper.
Author contributions A.L. and C.E. wrote the main manuscript text 
and prepared the figures. All authors reviewed the manuscript.
Funding Open Access funding provided by Air Force Research Labo-
ratory (AFRL) Technical Libraries Consortia. This research was sup -
ported by the Materials and Manufacturing and Aerospace Systems 
directorates of the Air Force Research Laboratories.
Data availability The datasets generated and/or analyzed during the 
current study are available from the corresponding author upon reason-
able request.
Declarations
Competing interests The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons 
Attribution 4.0 International License, which permits use, sharing, 
adaptation, distribution and reproduction in any medium or format, 
as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate 
if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not 
included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright 
holder. To view a copy of this licence, visit h t t p : / / c r e a t i v e c o m m o n s . o 
r g / l i c e n s e s / b y / 4 . 0 / . 
References
1. Lassner E, Schubert W-D (2000) Tungsten: properties, chemistry, 
technology of the element, alloys, and chemical compounds. Klu-
wer Academic/Plenum, Vienna, Austria
2. Ptable, Periodic Table (2021) https:/ /ptable .com/#P roper ties
3. Tungsten Material Properties—MatWeb Material Property Data 
(2022) https://www.matweb.com/
4. Stephens JR (1964) Effects of interstitial impurities on the low-
temperature tensile properties of tungsten. Technical report. 
NASA Lewis Research Center, Cleveland, OH
5. Smiti E, Jouffrey P, Kobylanski A (1984) The influence of carbon 
and oxygen in the grain boundary on the brittle-ductile transition 
temperature of tungsten Bi-crystals. Scr Metall 18(7):673–676. 
https:/ /doi.or g/10.10 16/00 36-9748(84)90318-1
6. Pettifor D (1995) Bonding and structure of molecules and solids. 
Clarendon, New York. h t t p s : / / d o i . o r g / 1 0 . 1 0 9 3 / o s o / 9 7 8 0 1 9 8 5 1 7 8 
7 0 . 0 0 1 . 0 0 0 1 
7. Morcos P, Elwany A, Karaman I et al (2022) Review: addi -
tive manufacturing of pure tungsten and tungsten-based 
alloys. J Mater Sci 57:9769–9806. https:/ /doi.or g/10.10 07/s1 
0853-022-07183-y
8. Ellis EAI, Sprayberry MA, Ledford C, Hankwitz JP, Kirka MM, 
Rock CD, Timothy J, Horn Y , Katoh R, Dehoff (2021) Process-
ing of tungsten through electron beam melting. J Nucl Mater 
555:153041. https:/ /doi.or g/10.10 16/j. jnucmat.2021.153041
Fig. 12 SEM images of oxide scales in cross-section on a W, b W-3Nb, c W-7Nb, and d W-11Nb

## Page 11

1 3
7193
Progress in Additive Manufacturing (2026) 11:7183–7193
9. Yang G, Yang P, Yang K, Liu N, Jia L, Wang J, Tang H (2019) 
Effect of processing parameters on the density, microstructure 
and strength of pure tungsten fabricated by selective electron 
beam melting. Int J Refract Met Hard Mater 84:105040. h t t p s : / / d 
o i . o r g / 1 0 . 1 0 1 6 / j . i j r m h m . 2 0 1 9 . 1 0 5 0 4 0 
10. Ren X, Peng H, Li J, Liu H, Huang L, Xin Y (2022) Selective 
electron beam melting (SEBM) of pure tungsten: metallurgical 
defects, microstructure, texture and mechanical properties. Mater 
15(3):1172. https:/ /doi.or g/10.33 90/ma 15031172
11. Xie J, Lu H, Lu J, Song X, Wu S, Jianbo, Lei (2021) Addi -
tive manufacturing of tungsten using directed energy deposi -
tion for potential nuclear fusion application. Surf Coat Technol 
409:126884. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . s u r f c o a t . 2 0 2 1 . 1 2 6 8 8 4 
12. Jeong W, Kwon Y-S, Kim D (2019) Three-dimensional print -
ing of tungsten structures by directed energy deposition. Mater 
Manuf Process 34:9: 986–992. h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 0 4 2 6 9 1 4 
. 2 0 1 9 . 1 5 9 4 2 5 3 
13. Jardon Zoé, Ertveldt J, Raphaël, Lecluyse Michaël, Hinderdael 
L, Pyl (2022) Directed energy deposition roughness mitigation 
through laser remelting. Procedia CIRP 111:180–184. h t t p s : / / d o i . 
o r g / 1 0 . 1 0 1 6 / j . p r o c i r . 2 0 2 2 . 0 8 . 0 4 2 
14. Rebesan P, Bonesso M, Gennari C, Dima R, Pepato A, Vedani 
M (2021) Tungsten fabricated by laser powder bed fusion, BHM 
Berg- und Hüuttenmäannische. Monatshefte 166(5):263–269. 
https:/ /doi.or g/10.10 07/s0 0501-021-01109-y
15. Iveković A, Omidvari N, Vrancken B, Lietaert K, Thijs L, Van -
meensel K, Vleugels J, Kruth JP (2018) Selective laser melting 
of tungsten and tungsten alloys. Int J Refract Met Hard Mater 
72:27–32. https:/ /doi.or g/10.10 16/j. ijrmhm.2017.12.005
16. Zhou X, Liu X, Zhang D, Shen Z, Liu W (2015) Balling phenom-
ena in selective laser melted tungsten. J Mater Process 222:33–
42. https:/ /doi.or g/10.10 16/j. jmatprotec.2015.02.032
17. Vrancken B, Ganeriwala RK, Martin AA, Matthews MJ (2021) 
Microcrack mitigation during laser scanning of tungsten via pre -
heating and alloying strategies. Addit Manuf 46:102158. h t t p s : / / d 
o i . o r g / 1 0 . 1 0 1 6 / j . a d d m a . 2 0 2 1 . 1 0 2 1 5 8 
18. Müller A V , Schlick G, Neu R, Anstätt C, Klimkait T, Lee J et 
al (2019) Additive manufacturing of pure tungsten by means of 
selective laser beam melting with substrate preheating tempera -
tures up to 1000 °C. Nucl Mater Energy 19:184–188. h t t p s : / / d o i . 
o r g / 1 0 . 1 0 1 6 / j . n m e . 2 0 1 9 . 0 2 . 0 3 4 
19. Ramakrishnan T, Kumar A, Kumar TS, Kwon S, Muniz-Lerma 
JA, Gauvin R, Brochu M (2024) Crack‐free tungsten fabricated 
via laser powder bed fusion additive manufacturing. Adv Funct 
Mater 34(12):2309304. https:/ /doi.or g/10.10 02/ad fm.202309304
20. Dong J, Liu S, Chen H, Li D, Zhang T, Chen C, Zhou K (2020) 
Effect of atmosphere on the microstructure and properties of addi-
tively manufactured tungsten. Mater Sci Technol 36(18):1988–
1996. https:/ /doi.or g/10.10 80/02 670836.2020.1852680
21. Luo A, Jacobson DL, Shin KS (1991) Solution softening mecha-
nism of iridium and rhenium in tungsten at room temperature. Int 
J Refract Met Hard Mater 10(2):107–114. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 
/ 0 2 6 3 - 4 3 6 8 ( 9 1 ) 9 0 0 2 8 - M 
22. Tran-Huu-Loi, Morniroli J, Gantois M, Lahaye M (1985) Brittle 
fracture of polycrystalline tungsten. J Mater Sci 20:199–206. 
https:/ /doi.or g/10.10 07/BF 00555913
23. Ren C, Fang ZZ, Koopman M, Butler B, Paramore J, Middlemas 
S (2018) Methods for improving ductility of tungsten—a review. 
Int J Refract Met Hard Mater 75:170–183. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 
6 / j . i j r m h m . 2 0 1 8 . 0 4 . 0 1 2 
24. Klopp WD (1968) Review of ductilizing of group VIA elements 
by Rhenium and other solutes. Technical Report NASA TN 
D-4955, Lewis Research Center, Cleveland, OH
25. Wilson JL, McKinsey CR T (1961) Tungsten-Columbium-Tanta-
lum alloys; their high-temperature properties. J Met 13:494–496. 
https:/ /doi.or g/10.10 07/BF 03378090
26. Xue J, Feng Z, Tang J, Tang C, Zhao Z (2021) Selective laser 
melting additive manufacturing of tungsten with niobium alloy -
ing: microstructure and suppression mechanism of microcracks. J 
Alloys Compd 874:159879. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . j a l l c o m . 2 0 2 
1 . 1 5 9 8 7 9 
27. Wang D, Wang Z, Li K, Ma J, Liu W, Shen Z (2019) Cracking 
in laser additively manufactured W: initiation mechanism and a 
suppression approach by alloying. Mater Des 162:384–393. h t t p s 
: / / d o i . o r g / 1 0 . 1 0 1 6 / j . m a t d e s . 2 0 1 8 . 1 2 . 0 1 0 
28. Tan C, Zhou K, Ma W, Attard B, Zhang P, Kuang T (2018) Selec-
tive laser melting of high-performance pure tungsten: parameter 
design, densification behavior and mechanical properties. Sci 
Technol Adv Mater 19:370–380. h t t p s : / / d o i . o r g / 1 0 . 1 0 8 0 / 1 4 6 8 6 9 
9 6 . 2 0 1 8 . 1 4 5 5 1 5 4 
29. Wright J (2020) Additive manufacturing of tungsten. PhD thesis, 
University of Sheffield
30. Kemnitz RA, Eckley CC, Sexton BM, Lesieur AR (2023) 
Strengthening of additively manufactured tungsten by use of 
hydrogen in argon shielding gas. Int J Refract Met Hard Mater 
110:105970. https:/ /doi.or g/10.10 16/j. ijrmhm.2022.105970
31. Vrancken B, Wauthle R, Kruth JP, Van Humbeeck J (2013) Study 
of the influence of material properties on residual stress in selec -
tive laser melting. In: 24th International SFF symposium—an 
additive manufacturing conference, SFF 2013, pp 393–407
32. Vrancken B, Ganeriwala RK, Matthews MJ (2020) Analysis of 
laser-induced microcracking in tungsten under additive manu -
facturing conditions: experiment and simulation. Acta Mater 
194:464–472. https:/ /doi.or g/10.10 16/j. actamat.2020.04.060
33. Hughes JR (1994) Mechanical working of refractory alloys pro -
duced by melting processes. Mater Res Soc Symp Proc 322:363–
375. https:/ /doi.or g/10.15 57/PR OC-322-363
34. Buckman R Jr (1988) Alloying of refractory metals. ASM Inter -
national, Alloying, pp 419–445
35. Cifuentes SC, Monge M, Pérez P (2012) On the oxidation mecha-
nism of pure tungsten in the temperature range 600–800 C. Cor -
ros Sci 57:114–121. https:/ /doi.or g/10.10 16/j. corsci.2011.12.027
36. Telu S, Patra A, Sankaranarayana M, Mitra R, Pabi S (2013) 
Microstructure and cyclic oxidation behavior of W–Cr alloys pre-
pared by sintering of mechanically alloyed nanocrystalline pow -
ders. Int J Refract Met Hard Mater 36:191–203. h t t p s : / / d o i . o r g / 1 
0 . 1 0 1 6 / j . i j r m h m . 2 0 1 2 . 0 8 . 0 1 5 
37. Das J, Rao GA, Pabi SK, Sankaranarayana M, Nandy TK (2014) 
Oxidation studies on W-Nb alloy. Int J Refract Met Hard Mater 
47:25–37. https:/ /doi.or g/10.10 16/j. ijrmhm.2014.06.016
38. Wagner C (1952) Theoretical analysis of the diffusion processes 
determining the oxidation rate of alloys. J Electrochem Soc 
99:10: 369. https:/ /doi.or g/10.11 49/1. 2779605
39. Gesmundo F, Gleeson B (1995) Oxidation of multicomponent 
two-phase alloys. Oxid Met 44:211–237. h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 
B F 0 1 0 4 6 7 2 8 
40. Slater JC (1964) Atomic radii in crystals. Chem Phys 
41(10):3199–3204. https:/ /doi.or g/10.10 63/1. 1725697
41. Liu J, Xue D, Li K (2011) Single-crystalline nanoporous nb2o5 
nanotubes. Nanoscale Res Lett 6:1–8. h t t p s : / / d o i . o r g / 1 0 . 1 1 8 6 / 1 5 
5 6 - 2 7 6 X - 6 - 1 3 8 
42. Zhou Y , Qiu Z, Lü M, Zhang A, Ma Q (2008) Preparation 
and spectroscopic properties of Nb2O5 nanorods. J Lumin 
128(8):1369–1372. https:/ /doi.or g/10.10 16/j. jlumin.2008.01.001
43. Telu S, Mitra R, Pabi SK (2013) High temperature oxidation 
behavior of W–Cr–Nb alloys in the temperature range of 800–
1200 °C. Int J Refract Met Hard Mater 38:47–59. h t t p s : / / d o i . o r g / 
1 0 . 1 0 1 6 / j . i j r m h m . 2 0 1 2 . 1 2 . 0 0 8 
Publisher’s note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
