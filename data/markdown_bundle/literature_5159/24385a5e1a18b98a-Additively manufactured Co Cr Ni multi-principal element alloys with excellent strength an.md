# Additively manufactured Co Cr Ni multi-principal element alloys with excellent strength and ductility at room and cryogenic temperatures

<!-- source: D:\总文献\Additively manufactured Co Cr Ni multi-principal element alloys with excellent strength and ductility at room and cryogenic temperatures.pdf -->
<!-- file_sha256: 3aa6b7425ab9dd1c7213b515c2399f82110a20d6eeac0fc9e1a9fee1bf98459f -->

## Page 1

Virtual and Physical Prototyping
ISSN: 1745-2759 (Print) 1745-2767 (Online) Journal homepage: www.tandfonline.com/journals/nvpp20
Additively manufactured Co–Cr–Ni multi-principal
element alloys with excellent strength and
ductility at room and cryogenic temperatures
Abhinav Chandraker, Ketan Sharma , Chethan Konkati , Sampad Barik ,
Shubham Sisodia, Kaushik Chatterjee & Ankur Chauhan
To cite this article: Abhinav Chandraker, Ketan Sharma , Chethan Konkati , Sampad Barik ,
Shubham Sisodia, Kaushik Chatterjee & Ankur Chauhan (2025) Additively manufactured
Co–Cr–Ni multi-principal element alloys with excellent strength and ductility at room
and cryogenic temperatures, Virtual and Physical Prototyping, 20:1, e2551867, DOI:
10.1080/17452759.2025.2551867
To link to this article: https://doi.org/10.1080/17452759.2025.2551867
© 2025 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group
Published online: 02 Sep 2025.
Submit your article to this journal 
Article views: 907
View related articles 
View Crossmark data
Citing articles: 1 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=nvpp20

## Page 2

Additively manufactured Co–Cr–Ni multi-principal element alloys with excellent 
strength and ductility at room and cryogenic temperatures
Abhinav Chandraker 
 , Ketan Sharma, Chethan Konkati, Sampad Barik, Shubham Sisodia 
 , 
Kaushik Chatterjee and Ankur Chauhan
Department of Materials Engineering, Indian Institute of Science, Bengaluru, India
ABSTRACT 
Additive manufacturing (AM) can facilitate the design of novel multi-principal element alloys 
(MPEAs), with the CoCrNi system gaining prominence for its outstanding mechanical properties. 
In this study, two non-equiatomic CoCrNi alloys with tailored stacking fault energies (SFE) – a 
high-SFE (HSFE) and a low-SFE (LSFE) variant – were fabricated using the directed energy 
deposition (DED) process. An equiatomic CoCrNi was also printed to validate the process 
parameters. Monotonic tensile tests were conducted at room (298 K) and cryogenic (77 K) 
temperatures, followed by detailed microstructural characterisation to understand the influence 
of SFE on underlying deformation mechanisms. The LSFE alloy exhibited a higher yield strength 
than the HSFE alloy at both temperatures, attributed to its higher Cr content and lower SFE, 
which increases typical strengthening contributions from solid solution, dislocation forest, and 
grain boundaries. At 298 K, HSFE alloy deformed mainly by dislocation slip-mediated 
mechanisms, while LSFE alloy additionally showed twinning, resulting in improved work 
hardening rate and strength-ductility trade-off. At 77 K, both alloys exhibited significant 
strength and work hardening rate enhancements. The LSFE alloy achieved tensile strength 
>1 GPa with ∼45% ductility, while the HSFE alloy maintained high ductility (∼74%) and tensile 
strength >800 MPa. In both alloys, multiple deformation mechanisms activated at 77 K, 
including dislocation slip-mediated mechanisms, twinning, and ε-martensite formation. These 
mechanisms contributed to enhanced strain hardening and strength, with LSFE showcasing 
more pronounced contributions due to its higher Cr content and lower SFE. Overall, two MPEAs 
fabricated via DED showcase superior strength-ductility combinations over comparable cast or 
AM alloys.
ARTICLE HISTORY
Received 24 May 2025 
Accepted 19 August 2025 
KEYWORDS 
High-entropy alloys; stacking 
fault energy; directed energy 
deposition; deformation 
twinning; transformation- 
induced plasticity
1. Introduction
The advent of multi-principal element alloys (MPEAs) 
marks a paradigm shift from conventional alloy design, 
which typically centres around a dominant base element. 
Instead, MPEAs combine several principal elements in 
near-equiatomic or non-equiatomic proportions [ 1 , 2 ], fre -
quently stabilising as single-phase solid solutions. This 
unique compositional complexity results in severe lattice 
distortion and synergistic atomic interactions, giving rise 
to remarkable mechanical properties [ 3–5 ].
Among MPEAs, those based on the face-centered 
cubic (FCC) structure owe much of their performance 
to their stacking fault energy (SFE), in addition to the 
inherent lattice distortion that enhances solid solution 
strengthening. SFE is a fundamental property governed 
by alloy composition and is independent of the 
fabrication route. Low SFE in FCC MPEAs promotes 
deformation mechanisms such as planar glide of disso -
ciated Shockley partials, twinning-induced plasticity 
(TWIP), and transformation-induced plasticity (TRIP) at 
stresses exceeding the yield point [ 6–10 ]. These mechan -
isms significantly elevate strain hardening capacity and 
suppress necking, making such alloys ideal candidates 
for structural applications under both ambient and cryo -
genic environments [ 6 , 11 ].
A pertinent example is the equiatomic CoCrNi alloy, 
with its SFE (13.5 to 22 mJ/m
2
) – lower than that of 
equiatomic CoCrFeMnNi (30–35 mJ/m
2
) [ 12–16 ]. This 
facilitates planar slip, inhibits cross-slip, and enables 
twinning and phase transformation, resulting in excep -
tional combinations of strength, ductility, and toughness 
that outperform the five-element system at cryogenic, 
ambient, and elevated temperatures [ 7 , 17 ].
© 2025 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group 
This is an Open Access article distributed under the terms of the Creative Commons Attribution License ( http://creativecommons.org/licenses/by/4.0/ ), which permits unrestricted use, 
distribution, and reproduction in any medium, provided the original work is properly cited. The terms on which this article has been published allow the posting of the Accepted 
Manuscript in a repository by the author(s) or with their consent. 
CONTACT Ankur Chauhan 
 ankurchauhan@iisc.ac.in
 Department of Materials Engineering, Indian Institute of Science, Bengaluru, Karnataka 560012, 
India
VIRTUAL AND PHYSICAL PROTOTYPING 
2025, VOL. 20, NO. 1, e2551867 (24 pages) 
https://doi.org/10.1080/17452759.2025.2551867

## Page 3

Tailoring SFE through compositional adjustments – 
particularly by deviating from equiatomic ratios within 
the CoCrNi system – offers a powerful strategy for opti -
mising mechanical performance [ 18–24 ]. Prior studies 
have demonstrated that modifying the Co, Cr, and Ni 
contents can effectively modulate SFE [ 24 , 20 ]. For 
example, first-principle [ 25 ] and thermodynamics calcu -
lations [ 26 , 27 ] have demonstrated that increasing Co 
and Cr content and reducing Ni content reduces SFE, 
with Cr having a stronger effect. A nonlinear correlation 
between Cr content and SFE in CoCrNi alloys was also 
computationally established by Ikeda et al. [ 28 ]. Similar 
conclusions were drawn experimentally by Wang et al. 
[ 24 ], who additionally reported that reducing SFE leads 
to a shift in the dominant deformation mechanism, 
from dislocation slip-mediated to twinning, and even -
tually to hexagonal close-packed (HCP)-martensitic 
phase transformation. Despite this, detailed mechanical 
investigations of non-equiatomic CoCrNi compositions 
with systematically varied SFEs remain scarce.
Meanwhile, most existing studies on MPEAs, 
especially single-phase FCC types, rely on traditional 
casting routes followed by thermomechanical proces -
sing to enhance strength via grain size refinement [ 29 ] 
and/or heterogeneous dislocation and grain structures 
[ 30–33 ]. In contrast, additive manufacturing (AM) has 
emerged as a disruptive fabrication pathway, capable 
of producing near-net-shaped components with 
minimal post-processing and tailored microstructures 
[ 9 , 34 ]. AM techniques such as laser powder bed fusion 
(LPBF) and direct energy deposition (DED) employ loca -
lised melting of metal powders using high-energy 
beams, followed by rapid solidification [ 35 , 36 ]. These 
processes expose material to extreme thermal gradients 
[ 37 , 38 ] and cooling rates (∼10³–10⁵ K/s for DED) [ 39 ], 
vastly surpassing those in conventional casting (∼0.1– 
10 K/s). Such rapid thermal cycling during AM gives 
rise to unique microstructural features – including 
refined dislocation substructures, columnar grains, and 
crystallographic texture – which can enhance strength 
[ 35 , 36 , 40 , 41 ]. However, achieving a favourable 
strength–ductility balance remains a challenge, as it is 
highly sensitive to alloy composition, processing par -
ameters, and AM-induced defects [ 9 , 11 , 42 ]. MPEAs, 
owing to their intrinsic lattice distortion and compo -
sitional tunability of SFE, are well-positioned to address 
this trade-off.
While equiatomic CoCrNi has been extensively 
explored in both cast and AM forms for its strength– 
ductility synergy, similar efforts on non-equiatomic, 
AM-produced CoCrNi alloys – especially those with 
deliberately engineered SFEs and tested under both 
room and cryogenic conditions – are limited. This 
study aims to address that gap by systematically investi -
gating the mechanical behaviour of three DED-fabri -
cated, single-phase FCC CoCrNi alloys with distinctly 
separated SFEs: (i) an equiatomic baseline composition 
(Co₃₃.₃Cr₃₃.₃Ni₃₃.₃) for process standardisation, (ii) a high- 
SFE variant (Co₃₀Cr₂₀Ni₅₀; ∼50 mJ/m
2 
[43]), and (iii) a 
low-SFE variant (Co₂₅Cr₄₅Ni₃₀; ∼10 mJ/m
2 
[24,43]). To 
our knowledge, this is the first study to directly 
compare DED-processed, single-phase non-equiatomic 
CoCrNi alloys with varying SFE range at 298 and 77 K.
Our approach (1) maintains an FCC structure while 
varying composition to modulate SFE, (2) leverages 
microstructural features inherent to AM for enhanced 
mechanical response, and (3) evaluates tensile perform -
ance at both 298 and 77 K. Pre- and post-deformation 
microstructural characterisation further elucidates the 
underlying deformation mechanisms responsible for 
the observed mechanical responses.
2. Experimental
2.1. Materials
As outlined earlier, the three Co–Cr–Ni compositions 
investigated in this study, Co
33.3
Cr
33.3
Ni
33.3
, Co
30
Cr
20
Ni
50
, 
and Co₂₅Cr₄₅Ni₃₀, were chosen based on their experimen -
tally determined distinct SFE values [ 24 , 43 ] and single- 
phase microstructure. CALPHAD–predicted isothermal 
sections at elevated temperatures [ 44 ], together with 
available experimental phase–equilibria data [ 45 , 46 ] 
and other experimental studies on their cast variants 
[ 24 ], confirm that all three alloys lie within the FCC 
single-phase field. Additionally, since additive manufac -
turing involves extremely high local temperatures 
[ 37 , 38 ], combined with rapid cooling rates [ 39 ], it 
promotes the formation of supercooled structures. 
Under such conditions, high-temperature phase dia -
grams are a reliable guide for predicting the phases at 
room temperature.
2.2. Powder mixing and printing
Elemental Co, Cr, and Ni powders, each with particle 
sizes in the 50–100 µm range, were procured and 
measured in the desired ratios, then mechanically 
mixed using ball milling to ensure homogeneity. A low 
milling speed of 100 rpm for 3 h and a low ball-to- 
powder ratio of 5:1 were employed to avoid changes 
in particle shape, breakdown, or agglomeration of the 
spherical particles. The resulting mixed powder retained 
a near-spherical morphology. For example, Figure 1 (a) 
shows the mechanically mixed Co
33.3
Cr
33.3
Ni
33.3 
powder particles, while the corresponding Energy 
2 
 A. CHANDRAKER ET AL.

## Page 4

Dispersive X-ray Spectroscopy (EDS) map in Figure 1 (b), 
obtained using an FEI APREO scanning electron micro -
scope (SEM) operating at 20 kV and a probe current of 
0.8 nA, confirms a relatively uniform distribution of the 
elemental powders, with particle sizes remaining in the 
50–100 µm range.
Thereafter, a series of trials was conducted using 
the FORM ALLOY metal 3D printer to determine the 
optimal printing parameters (see Figure 1 (c)). Initially, 
120 single tracks were deposited across a broad range 
of laser powers (300–800 W), scan speeds (6–11 mm/s), 
and powder feed rates (3.1–10 g/min). Upon visual 
inspection, tracks exhibiting smooth and continuous mor -
phology were shortlisted for further evaluation. These 
shortlisted parameters were refined by fabricating single 
layers, followed by multi-layer blocks, to assess printing 
stability. Using the Archimedes principle and SEM- 
based, porosity analysis was then performed to guide 
the final parameter selection. The optimised parameter 
set, ensuring stable, defect-minimized multi-layer depo -
sition, included a laser power of 700 W, scan speed of 
8 mm/s, powder feed rate of 7.54 g/min, hatch spacing 
Figure 1. (a) SEM micrograph and (b) corresponding EDS elemental map of the mechanically mixed Co
33.3
Cr
33.3
Ni
33.3 
powder feed -
stock, demonstrating uniform distribution of elemental powder particles (50–100 µm in size). (c) Photograph of printing trials carried 
out on a steel substrate using different parameter combinations to arrive at optimum parameters. (d) Final printed block with labelled 
build direction (BD), transverse direction (TD), and longitudinal direction (LD). (e) Schematic showing the machining layout for 
miniature dog-bone tensile specimens. (f) Photograph of a prepared miniature dog-bone tensile sample for mechanical testing.
VIRTUAL AND PHYSICAL PROTOTYPING 
 3

## Page 5

of 0.3 mm, and a scan rotation of 67°. The final bulk 
samples were printed with dimensions of 26 mm × 
14 mm × 12 mm, as shown in Figure 1 (d).
2.3. Alloys density and porosity estimation
The theoretical density ( r
theoretical
) of the alloys was calcu -
lated using Equation (1) [ 47 ].
r
theoretical
=
N · M
N
a
· V
(1) 
where N is the number of atoms per unit cell, M is the 
molecular weight of the unit cell, N
a 
is Avogadro’s 
number, and V is the unit cell volume.
The experimental density ( r
experimental
) was deter -
mined using the Archimedes principle, as expressed in 
Equation (2) [ 47 ]:
r
experimental
=
M
a
M
a
 M
w
􏼒 􏼓
r
w
(2) 
where M
a 
is the dry weight of the specimen, M
w 
is the 
weight of the specimen when submerged in water, 
and r
w 
is the density of water.
Densification percentages were determined using 
Archimedes’ principle (as calculated by Equation (3) ) 
and SEM-based backscattered electron (BSE) image 
contrast analysis at high magnification to confirm pore 
distribution and morphology.
Densification (%) =
r
theoretical
 r
experimental
r
theoretical
􏼒 􏼓
∗100 (3) 
2.4. Monotonic tensile testing
Mini-tensile samples were fabricated from the printed 
block via electrical discharge machining, with the gauge 
length oriented perpendicular to the build direction 
(BD). The gauge dimensions were 6 mm × 2 mm × 2 mm, 
as illustrated in Figure 1 (e,f). Tensile tests were conducted 
at 298 and 77 K using an Instron 5967 universal testing 
machine equipped with a 30 kN load cell. The tests were 
conducted at nominal strain rates of 10
−
³ s
−
¹, with strain 
measurements captured via digital image correlation 
(DIC) using Vic2D software (Correlated Solutions, USA). A 
high-contrast speckle pattern, created by spraying black 
paint over a white background, was applied to the speci -
men surface to facilitate accurate strain tracking.
For cryogenic testing, a custom setup was developed 
in-house. Specimens were immersed in liquid nitrogen 
for approximately 10 min before testing to ensure 
thermal equilibrium at 77 K. During testing, liquid nitro -
gen was continuously replenished at a controlled rate to 
maintain a stable temperature of 77 K.
2.5. Microstructure characterisation
For characterisation, the gauge sections of all specimens 
were wet ground longitudinally up to 4 μm grit size 
silicon carbide abrasive papers and polished with 1 and 
0.25 μm diamond suspensions for a smooth surface 
finish. This is followed by etching with Kalling’s II 
reagent to reveal the microstructure. Optical microscopy 
was then conducted using a Leica optical microscope.
Phase analyses were performed using a Bruker D8 
Advance X-ray diffractometer equipped with a copper 
source (Kα
1 
and Kα
2 
radiations with wavelengths of 
0.15406 and 0.15444 nm, respectively). X-ray diffraction 
(XRD) patterns were obtained in a 2θ-range from 30° to 
100° using a step size of Δ2θ = 0.02°, scan speed of 2° 
per min. Following this, microstrain (ε) calculations were 
carried out by employing the Williamson-Hall (WH) 
method [ 48 , 49 ]. This procedure involved extracting the 
diffraction peak positions (diffraction angles: u ). The 
values of the full widths at half-maximum ( b ) correspond -
ing to the Cu Kα
1 
radiation were determined. Thereafter, ε 
values were determined as the slopes of fitted lines in the 
( b c os u )-versus-(4 si n u ) plots. Subsequently, the dislo -
cation density was estimated using Equation (4) [ 50 ]
r =
6 p 1
2
b
2
(4) 
Where b is the Burgers vector of a full dislocation in an 
FCC structure.
XRD bulk texture measurements were conducted 
using a Rigaku diffractometer in Schulz reflection geome -
try mode with a Cu Kα source. Three pole figures (111), 
(002), and (022) were measured, covering a range from 
ψ = 0° to 80°. These figures were used to calculate the 
orientation distribution function (ODF) through quantitat -
ive texture analysis using Bunge notation for Euler angles, 
with the help of ResMat Textools software.
Wavelength-dispersive X-ray spectroscopy-based 
mapping was carried out for the three alloys to ascertain 
the achieved compositions and assess the elemental 
segregations that may have occurred during the printing 
process. A JEOL JXA 8230 electron probe microprobe 
analyzer (EPMA) with a tungsten filament source was uti -
lised for carrying out the area mapping measurements 
using an accelerating voltage of 15 kV and a step size 
of 0.04 μm. Calibration of the instrument was carried 
out using natural and pure metal standards. The Co– 
Kα, Cr–Kα, and Ni–Kα characteristic X-ray peak intensities 
were measured using pure Co, Cr, and Ni as standards, 
respectively. The data reduction was performed using 
the ZAF model correction procedure [ 51 ].
Electron backscatter diffraction (EBSD) investigations 
were carried out on a ThermoFisher Helios G4-UX SEM 
4 
 A. CHANDRAKER ET AL.

## Page 6

equipped with an EDAX detector. For EBSD analysis, the 
samples were electropolished using standard A2 electro -
lyte of the Struers lectropol setup at 28 V for 13 s, main -
taining a flow rate of 18. EBSD data were acquired at an 
accelerating voltage of 30 kV, a probe current of 13 nA, 
a working distance of 9.7 mm, and a step size of 4 μm 
for undeformed and 0.75 µm for deformed samples, tar -
geting regions approximately 2 mm away from the frac -
ture surface. The acquired EBSD data were processed 
using EDAX’s OIM software (version 8).
For transmission electron microscopy (TEM), samples 
were prepared using an FEI Scios focused-ion beam (FIB) 
SEM. Diffraction contrast imaging was conducted using 
a ThermoFisher T20 Tecnai TEM operated at 200 kV. 
Additionally, high-resolution scanning-TEM (HR-STEM) 
investigations were performed using an aberration-cor -
rected ThermoFisher Titan Themis microscope at 300 kV.
Post-fracture, the tensile specimen fracture surfaces 
were examined using FEI Quanta 200 SEM.
3. Results
3.1. Equiatomic alloy characterisation, testing, 
and validation with literature
An XRD pattern acquired along the TD of the as-printed 
Co
33.3
Cr
33.3
Ni
33.3 
block is shown in Figure 2 (a). As 
evident, the XRD pattern exhibits slightly broad diffrac -
tion peaks at relatively unique 2θ values, which are 
indexed to be from a single-phase FCC crystal structure. 
The slightly broader peaks indicate the presence of AM- 
induced defects and dislocations. The lattice parameter 
(a) was determined to be 0.356 nm, in line with that 
reported by Laplanche et al. [ 7 ]. Utilising the XRD 
pattern, the WH method [ 48 , 49 ] and Equation (4) , the 
dislocation density for as-printed Co
33.3
Cr
33.3
Ni
33.3 
was 
estimated to be 1.69 × 10
14
m
 2
.
The theoretical and experimental densities of the 
alloy calculated using Equations (1) and (2) were 8.22 
and 8.18 g/cm
3
, respectively. Densification was 
assessed using Equation (3) and through BSE image 
contrast analysis at high magnification. Both methods 
yielded values close to 99% (see Table 1 ), indicating 
that the selected printing parameters resulted in 
highly dense samples.
The EBSD-derived inverse pole figure (IPF) map three- 
dimensional (3D) reconstruction is shown in Figure 2 (b). 
In contrast to the as-recrystallized materials, this 3D 
reconstruction shows non-equiaxed grains with a wide 
grain size distribution. The average grain size estimated 
using the line intercept method is 141 ± 11 µm. A predo -
minant (110) texture is observed in the build direction 
and is attributed to the vertical temperature gradient 
and curvature of the melt pools during solidification 
[ 52 ]. The optical microscope observation of the micro -
structure further reveals characteristic melt pool bound -
aries with dislocation cellular substructures, see Figure 
2 (c,d). Cellular boundaries contain high dislocation den -
sities. Rapid thermal gradients during printing cause 
residual stress and localised plastic deformation, pro -
moting dislocation formation and rearrangement into 
cell structures [ 53 ]. Their orientation is dictated by the 
underlying crystallography and the heat flow direction 
in successive layers [ 53 ]. EPMA confirmed the overall 
composition of the equiatomic alloy to be Co
32
Cr
34
Ni
34
. 
EPMA elemental maps for the equiatomic composition, 
shown in Figure 2 (e–g), reveal minor Cr segregation 
accompanied by Co depletion at cellular boundaries, 
consistent with the literature. Notably, no significant 
segregation was observed along grain boundaries.
The engineering tensile stress–strain curves for the 
two equiatomic as-printed CoCrNi samples tested at 
298 K are shown in Figure 3 (a). The alloy exhibits a 
yield strength (YS) of 417 ± 4 MPa, the ultimate tensile 
strength (UTS) of 707 ± 10 MPa, and a total elongation 
to failure of 63 ± 6%. This excellent strength-ductility 
combination of this alloy is attributed to the activation 
of deformation twinning alongside dislocation slip, as 
evidenced by the EBSD-derived IPF and KAM maps over -
laid on the IQ map in Figure 3 (b,c). The misorientation 
profile along the white arrow in the inset of Figure 
3 (b) confirms the presence of deformation twins with 
characteristic Σ3 twin boundaries, exhibiting a typical 
60° misorientation. Furthermore, high KAM values are 
seen as green pixels in Figure 3 (c) after deformation, 
which indicates a high dislocation density.
A comparable tensile response for the same compo -
sition produced via AM has been reported previously. 
Figure 3 (d) compares the UTS and total elongation to 
failure of the DED-produced equiatomic alloy from this 
study with literature values for the same composition fab -
ricated using both DED and LPBF methods, showing 
tensile properties consistent with those reported for 
DED samples [ 8 , 9 , 54–68 ]. Additionally, despite possessing 
a larger average grain size, the additively manufactured 
equiatomic CoCrNi alloy demonstrates comparatively 
higher strength and ductility than the as-recrystallized 
cast counterpart, see Ref. [ 7 ]. This enhanced strength in 
the AM alloy is due to the additional strengthening con -
tribution from the high dislocation density introduced 
during the AM process, discussed in Section 4 . 1 .
Overall, these results verify that the printing par -
ameters are well optimised. The same approach was 
therefore used to fabricate the HSFE and LSFE 
alloys, which exhibit markedly different SFEs, with the cor -
responding findings discussed in the following sections.
VIRTUAL AND PHYSICAL PROTOTYPING 
 5

## Page 7

3.2. Microstructural characterisation of HSFE and 
LSFE alloys
XRD patterns acquired along the TD of the printed HSFE 
(Co₃₀Cr₂₀Ni₅₀) and LSFE (Co
25
Cr
45
Ni
30
) blocks are shown 
in Figure 4 . Evidently, both alloys exhibit similar XRD 
patterns, characterised by slightly broad diffraction 
peaks at distinct 2θ positions, all of which correspond 
to a single-phase FCC crystal structure. The lattice par -
ameters of HSFE and LSFE alloys were determined to 
be 0.354 and 0.357 nm, respectively. The difference in 
Figure 2. Microstructural characterisation of the as-printed equiatomic CoCrNi composition fabricated by DED: (a) X-ray diffraction 
pattern showing FCC phase peaks, (b) EBSD 3D reconstruction showing micrographs along each direction, i.e. LD, TD, and BD; (c) 
Optical micrograph highlighting the melt pool boundaries marked with dotted black lines; (d) High-magnification image revealing 
cellular substructures (1–3 µm in size) comprising dislocation arrays within the grains. (e–g) EPMA elemental maps from the interior 
of the grain reveal minor Cr segregation and Co depletion at cell boundaries. A common colour legend indicating atomic percentages 
is provided on the right.
Table 1. XRD analysis and densification measurement results of the equiatomic CoCrNi alloy. Densification was evaluated using 
Archimedes’ principle and SEM-based image analysis.
Composition
Lattice parameter 
(nm)
Theoretical density (g/ 
cm
3
)
Experimental density (g/ 
cm
3
)
Densification (Archimedes’ 
principle)
Densification (SEM 
analysis)
Equiatomic 0.356 8.22 8.18 99.6% 99.3%
6 
 A. CHANDRAKER ET AL.

## Page 8

lattice parameter indicates a compositional effect on the 
lattice parameter, with higher Cr content resulting in a 
higher lattice parameter. Notably, the lattice parameter 
for LSFE is similar to that of the equiatomic alloy 
(0.356 nm). Utilising XRD patterns, the WH method 
[ 48 , 49 ] and Equation (4) , the dislocation density of as- 
printed HSFE and LSFE was estimated to be 
1.6 × 10
14
m
 2 
and 2.3 × 10
14
m
 2
, respectively.
Additionally, both alloys exhibit comparable theoreti -
cal and experimental densities, with densification levels 
exceeding 98% by the Archimedes method and 99% by 
SEM-based analysis (see Table 2 ). The high values 
confirm that the printed samples have low porosity.
The EBSD-derived IPF map 3D reconstructions of the 
two alloys are shown in Figure 5 (a,b). Evidently, the 
microstructures are similar to that of the printed equia -
tomic alloy, with non-equiaxed grains having a wide 
grain size distribution. The average grain sizes, deter -
mined using the line-intercept method, were 136 ± 9 µm 
for the HSFE alloy and 142 ± 15 µm for the LSFE alloy. 
The characteristic melt pool structures and dislocation cel -
lular substructures are similar (see Figure 5 (c–f)). The 
underlying mechanisms responsible for these features 
are also expected to be same as discussed for the equia -
tomic alloy.
Cell size measurements for HSFE and LSFE alloys were 
conducted in grain interiors, away from boundaries (see 
Figure 6 ), analysing 450 cells from 9 images per sample 
Figure 3. (a) Representative engineering tensile stress–strain curves for two equiatomic alloy samples obtained at a nominal strain 
rate of 10
−3 
s
−1 
at 298 K; (b) EBSD-derived IQ + IPF map, along with the misorientation profile across the marked white arrow, confi -
rming the presence of deformation twins with characteristic Σ3 twin boundaries. (c) The corresponding IQ + KAM map showcases high 
KAM values (green pixels) indicative of a high dislocation density. (d) A comparison of UTS and total elongation to failure of the DED- 
produced equiatomic alloy from this study with literature values for the same composition fabricated using both DED and LPBF 
methods [ 8 , 9 , 54–68 ].
Figure 4. XRD patterns of the as-printed HSFE and LSFE alloys 
exhibiting FCC phase peaks.
VIRTUAL AND PHYSICAL PROTOTYPING 
 7

## Page 9

Table 2. XRD analysis and densification measurements of the printed HSFE and LSFE alloys. Densification was evaluated using 
Archimedes’ principle and SEM-based image analysis.
Composition
Lattice parameter 
(nm)
Theoretical density (g/ 
cm
3
)
Experimental density (g/ 
cm
3
)
Densification (Archimedes’ 
principle)
Densification (SEM 
analysis)
HSFE 0.354 8.6 8.7 98.5% 99.3%
LSFE 0.357 8.1 8.0 98.4% 99.2%
Figure 5. Microstructural characterisation of the as-printed LSFE and HSFE alloys: (a,b) EBSD 3D reconstructions showcasing micro -
graphs along each direction, i.e. LD, TD, and BD for HSFE and LSFE, respectively; (c–f) Optical micrographs acquired from the LD-TD 
planes of the (c,e) HSFE and (d,f) LSFE printed blocks highlighting the melt pool boundaries, and cellular substructures.
8 
 A. CHANDRAKER ET AL.

## Page 10

(50 cells/micrograph). HSFE exhibited a slightly smaller 
average equivalent cell radius than LSFE alloy, likely 
due to its higher SFE, which enhances cross-slip and 
results in greater dislocation entanglement, forming 
more compact dislocation cells during printing [ 69 ].
EPMA analysis revealed compositions of Co
30
Cr
20
Ni
50 
for the HSFE alloy and Co
22
Cr
46
Ni
32 
for the LSFE alloy, 
with elemental maps shown in Figure 7 . It is evident 
that Cr segregation at cell boundaries, coupled with 
depletion of Co and Ni, was more pronounced in the 
LSFE alloy than in the HSFE and equiatomic compo -
sitions (compare with Figure 2 (e–g)).
The bulk texture investigations were carried out using 
XRD. The (111) pole figures presented in Figure 8 (a) 
(HSFE) and Figure 8 (b) (LSFE) reveal that both alloys 
exhibit weak and broadly distributed textures. Although 
some intensity maxima are visible along the build direc -
tion (BD) and transverse direction (TD), the overall 
texture strength remains low, with maximum intensity 
values of approximately 2.45 for HSFE and 2.35 for LSFE. 
These values suggest that the DED process employed 
for fabricating both compositions resulted in comparable 
texture evolution. Similar observations were reported for 
(002) and (022) pole figures (not shown here).
Overall, since the HSFE and LSFE alloys exhibit similar 
average grain sizes, dislocation densities, and textures, 
the differences in their mechanical behaviour presented 
in the subsequent sections can be mainly ascribed to the 
variations in their composition and SFE.
3.3. Tensile response for HSFE and LSFE alloys at 
298 and 77 K
The engineering tensile stress–strain behaviour of the 
HSFE and LSFE alloys tested at 298 and 77 K tempera -
tures is presented in Figure 9 (a). At 298 K, the HSFE 
alloy exhibited a YS of 296 ± 6 MPa and a UTS of 562 ± 
12 MPa, with a total elongation to failure of 56 ± 2%. 
The LSFE alloy demonstrated a YS of 415 ± 13 MPa and 
UTS of 658 ± 3 MPa, along with a total elongation to 
failure of 65 ± 1%. This corresponds to a ∼40% increase 
in YS for the LSFE alloy relative to HSFE, while maintain -
ing ∼15% higher ductility, as shown in Figure 10 . 
Figure 6. Representative histogram of equivalent cell radii for 
the HSFE and LSFE alloys. The mean cell radii (µ) are higher 
for LSFE than HSFE, with a comparable standard deviation (σ).
Figure 7. EPMA elemental maps from the interior of (a–c) HSFE and (d–f) LSFE grains displaying the atomic percentages of Co, Cr, and 
Ni, represented by colour gradients for each alloy. A common colour legend indicating atomic percentages is provided on the right.
VIRTUAL AND PHYSICAL PROTOTYPING 
 9

## Page 11

Compared to the equiatomic composition, LSFE exhibits 
similar YS and total elongation to failure (see inset in 
Figure 3 (a)), though the equiatomic alloy achieves a 
slightly higher UTS.
At 77 K, both alloys show a marked improvement in YS 
and UTS compared to their 298 K performance ( Figures 
9 (a) and 10 ). Specifically, the HSFE alloy demonstrates a 
∼40% increase in YS (416 ± 5 MPa) and an UTS of 811 ± 
18 MPa at 77 K. In comparison, the LSFE alloy shows a 
more pronounced ∼60% rise in YS (663 ± 8 MPa), with a 
UTS of 1057 ± 13 MPa – approximately 60% and 30% 
higher in YS and UTS, respectively, relative to HSFE. 
However, despite its superior strength, LSFE exhibits 
reduced ductility, with total elongation to failure decreas -
ing to 45 ± 1%, whereas HSFE maintains excellent duct -
ility, reaching 74 ± 1% at cryogenic temperature. The 
Figure 8. (111) pole figures obtained via XRD along the longitudinal direction (LD) of the printed blocks of (a) HSFE and (b) LSFE 
compositions, respectively.
Figure 9. (a) The representative engineering tensile stress-strain curves of the HSFE and LSFE alloys obtained at a constant strain rate 
of 10
−3 
s
−1 
at 298 and 77 K. (b) Work hardening rate and true tensile stress-strain curves for both alloys at 298 and 77 K.
Figure 10. Comparison of the tensile properties obtained from 
the engineering stress-strain curves of HSFE and LSFE alloys at 
298 and 77 K.
10 
 A. CHANDRAKER ET AL.

## Page 12

underlying mechanisms contributing to this contrasting 
behaviour are discussed in detail in the discussion 
section. Compared to the as-recrystallized LSFE alloy 
reported in the literature, with a finer grain size [ 24 ], our 
DED-processed variant exhibits higher YS and UTS at 
both 298 and 77 K. This enhanced strength in the AM 
alloy is due to the additional strengthening contribution 
from the high dislocation density introduced during the 
AM process, see Section 4 . 1 .
The work-hardening rate (WHR) curves as a function of 
true strain for the HSFE and LSFE alloys at both 298 and 
77 K are presented in Figure 9 (b). At 298 K, both alloys 
exhibit an initially sharp decrease in the WHR, marking 
the initiation of plasticity, which is followed by a relatively 
stable, quasi-constant phase. This plateau is more pro -
nounced in the LSFE alloy, with a slight hint of increased 
WHR. Subsequently, both alloys exhibit a gradual decrease 
in WHR, with the decline being more pronounced in the 
HSFE alloy, ultimately culminating in failure.
In contrast, the WHR behaviour at 77 K reveals a sig -
nificantly higher magnitude of hardening rates for 
both alloys ( Figure 9 (b)). Following the initial relatively 
gradual drop, the alloys display a considerably extended 
plateau region where the WHR remains nearly constant. 
This sustained work-hardening response for both alloys 
is much longer than at 298 K.
Overall, the WHR is markedly enhanced at 77 K for 
both HSFE and LSFE alloys. LSFE exhibits a higher work- 
hardening capacity than HSFE under both temperatures. 
While the WHR decreases more rapidly at 298 K, the rate 
of decline is notably slower at 77 K. Furthermore, LSFE 
shows a more gradual reduction in WHR than HSFE at 
both temperatures, indicating better strain-hardening 
capability, especially under cryogenic conditions.
3.4. Comparison with the equiatomic alloy data 
reported in the literature
Figure 11 compares the UTS and total elongation to 
failure for the additively manufactured CoCrNi MPEAs 
investigated in this study, alongside the additively 
manufactured equiatomic alloy data reported in the lit -
erature [ 8 , 9 , 62–66 , 68 ], for tests conducted at 298 K and 
cryogenic temperatures (77–143 K). Literature data for 
cast CoCrNi MPEAs are excluded from this comparison, 
as their properties vary widely depending on the 
thermo-mechanical processing routes used, preventing 
a fair comparison. At 298 K, all three printed alloys 
exhibit an excellent combination of strength and duct -
ility, positioned towards the right of the property envel -
ope of the equiatomic CoCrNi alloys. At 77 K, this 
study’s equiatomic and LSFE alloys display superior 
mechanical performance, offering comparable strength 
but improved ductility relative to their equiatomic 
counterparts in the literature. Notably, the HSFE alloy 
achieves the highest ductility among all tested variants 
at 77 K while maintaining a high UTS. These results under -
score the efficacy of compositional tuning, particularly via 
adjustments that influence SFE and AM parameters in 
governing deformation behaviour and optimising mech -
anical properties in CoCrNi-based MPEAs.
3.5. Post-deformation characterisation for HSFE 
and LSFE alloys
Post-deformation microstructural characterisation was 
performed using EBSD and TEM to elucidate the under -
lying mechanisms responsible for the distinct tensile 
responses of the HSFE and LSFE alloys.
Figure 12 presents EBSD-derived IPF maps superim -
posed on IQ maps for the room-temperature fractured 
HSFE and LSFE specimens, respectively. In the HSFE 
alloy, deformation is predominantly accommodated by 
dislocation slip-mediated mechanisms, as witnessed by 
the gradual colour gradients within individual grains 
( Figure 12 (a)) and the continuous low misorientation 
profile along the white arrow in Figure 12 (b). Notably, 
no evidence of deformation twins is observed.
In contrast, the LSFE alloy exhibits signatures of both 
dislocation slip-mediated mechanisms and deformation 
twinning, as evidenced in the IPF + IQ map shown in 
Figure 12 (c). The misorientation profile along the white 
arrow in the Figure 12 (d) confirms the presence of defor -
mation twins with characteristic Σ3 twin boundaries, 
Figure 11. Ultimate tensile strength versus total elongation to 
failure plot showcasing data for equiatomic, LSFE, and HSFE 
alloys investigated in this study, alongside the data of the addi -
tively manufactured equiatomic CoCrNi alloys reported in the lit -
erature [ 8 , 9 , 62–66 , 68 ], at room temperature (298 K) and 
cryogenic temperatures (77–143 K).
VIRTUAL AND PHYSICAL PROTOTYPING 
 11

## Page 13

exhibiting a typical 60° misorientation. The activation of 
deformation twinning in LSFE is attributed to its lower 
SFE, which facilitates twin nucleation post-yielding [ 70 ].
TEM characterisation was performed on FIB-extracted 
lamellae from regions approximately 2 mm away from 
the fracture surfaces of both HSFE and LSFE specimens 
to confirm the presence of deformation twinning and 
the associated dislocation structures. The representative 
bright-field (BF) TEM micrograph obtained from the 
HSFE sample ( Figure 13 (a)) displays only dislocation 
structures (including cells) without the presence of 
deformation twins, indicating that dislocation slip- 
mediated mechanisms primarily accommodate plastic 
deformation. This observation is consistent with EBSD 
observations and is further supported by the corre -
sponding inverted-contrast selected area diffraction 
pattern (SADP) shown in the inset, which reveals only 
matrix diffraction spots and lacks any additional reflec -
tions typically associated with deformation twins. In con -
trast, the BF-TEM micrograph acquired from the LSFE 
sample ( Figure 13 (b)) displays a high density of planar 
fault-like features oriented along two distinct directions, 
highlighted by dotted lines. The corresponding SADP 
acquired near <011> zone axis ( Figure 13 (c)) exhibits 
mirror-symmetric diffraction spots, which were indexed 
to the matrix (green dashed circles) and deformation 
twins (orange). The dark-field (DF) TEM micrograph 
( Figure 13 (d)) generated using a twin-related reflection 
from the SADP further validates that the planar fault- 
like features observed in Figure 13 (b) are bright-contrast 
deformation twins embedded within the FCC matrix. In 
addition to twinning, the LSFE alloy exhibits dislocation 
cell structures ( Figure 13 (e)) and high-density dislocation 
walls (HDDWs, Figure 13 (f)). While some of the dislo -
cation cells in both alloys may be remnants of the AM 
process, the formation of HDDWs in LSFE is associated 
with increased dislocation-dislocation interactions and 
clustering, ultimately leading to the development of 
thick, wall-like configurations [ 71 ]. These substructures 
are indicative of active dislocation cross-slip processes.
Overall, these observations demonstrate that the 
LSFE alloy accommodates plastic deformation at 298 K 
through a synergistic combination of dislocation slip- 
mediated mechanisms and deformation twinning. In 
Figure 12. EBSD-derived microstructural analysis of deformed HSFE and LSFE alloys at 298 K. (a) IQ + IPF map from deformed 
HSFE alloy showcasing slip characteristics, with corresponding point-to-point misorientation profile in (b) along white 
arrow indicating slip activity characterised by a continuous low misorientation angle. (c) IQ + IPF map from the deformed 
LSFE alloy revealing both dislocation slip-mediated mechanisms and deformation twinning. The corresponding point-to-point 
misorientation profile in (d) along the white arrow confirms the presence of Σ3 twin boundaries, exhibiting a typical 60° 
misorientation.
12 
 A. CHANDRAKER ET AL.

## Page 14

contrast, the HSFE alloy deforms primarily via slip- 
mediated mechanisms.
EBSD and TEM analyses were also conducted on the 
HSFE and LSFE specimens fractured under cryogenic 
conditions to assess the influence of temperature on 
deformation mechanisms. EBSD-derived IPF maps over -
laid on IQ maps for the cryogenically tested HSFE and 
LSFE alloys are shown in Figure 14 (a,b). Compared to 
298 K, a significant increase in deformation twinning 
activity is observed in both alloys at 77 K. The misorien -
tation profiles along the white arrows in the Figure 14 (c, 
d) confirm the presence of Σ3 twin boundaries, charac -
terised by a typical 60° misorientation.
TEM analysis was performed on FIB-prepared lamel -
lae extracted from regions approximately 2 mm from 
the fracture surface to corroborate these observations. 
BF-TEM micrographs from the HSFE ( Figure 15 (a)) and 
LSFE ( Figure 15 (b)) samples reveal dislocation struc -
tures along with high densities of planar fault-like fea -
tures. The corresponding SADPs acquired near the 
<011> zone axis from the HSFE ( Figure 15 (c)) and the 
LSFE ( Figure 15 (d)) samples show prominent reflec -
tions from the FCC matrix (green dashed circles), 
along with weaker reflections corresponding to defor -
mation twins (orange) and HCP ε-martensite (blue). 
The coloured DF-TEM micrographs in Figure 15 (e,f), 
acquired using twin and HCP phase-related reflections 
from the HSFE sample, showcase some planar faults in 
Figure 15 (a) that correspond to the deformation twin 
lamellae. In contrast, some thinner features sand -
wiched between deformation twins and the surround -
ing FCC matrix correspond to ε-martensite lamellae 
( Figure 15 (f)). The HCP lamellae exhibit a well-defined 
orientation relationship with the surrounding FCC 
matrix, specifically (0001)
HCP 
|| (111)
FCC 
and [11
̅
20]
HCP 
|| [1
̅
10]
FCC
. Notably, the HCP lamellae are aligned 
along the same {111} habit planes as the coherent 
twin boundaries within the FCC structure. Complemen -
tary HR-STEM investigations further confirm the pres -
ence of deformation twins, intrinsic stacking fault 
(ISF), and HCP ε-martensite embedded in the FCC 
matrix (see Figure 15 (g,h)).
These findings highlight enhanced propensity for 
deformation twinning (TWIP) and additional ε-martensite 
formation (TRIP) in both alloys at 77 K. These mechanisms 
complement dislocation slip-mediated mechanisms, 
Figure 13. TEM-based microstructural analysis of deformed HSFE and LSFE alloys at 298 K. (a) BF-TEM micrograph showcasing the 
dislocation cell structure in the HSFE sample, with the corresponding SADP in the inset showcasing only matrix diffraction spots. 
(b) BF-TEM micrograph from the LSFE sample showcases dark-contrast planar faults in two orientations marked with white dotted 
lines. (c) The corresponding SADP with twin spots (orange dashed circle) and matrix spots (green) acquired near <110> zone axis 
from the LSFE sample. (d) DF-TEM micrograph showcasing planar faults in (d) to be bright contrast twins. (e,f) BF-TEM micrographs 
from the LSFE sample showcasing dislocation cells (dashed lines) and high dislocation density walls (HDDWs).
VIRTUAL AND PHYSICAL PROTOTYPING 
 13

## Page 15

reflecting their role in governing cryogenic deformation 
behaviour in the investigated MPEAs.
4. Discussion
4.1. Strengthening contributions to yield strength 
at 298 K
According to the classical Hall–Petch relationship 
[ 72 , 73 ], the experimental yield strength of the as-recrys -
tallized single-phase MPEAs can be estimated by 
incorporating contributions from lattice friction/solid 
solution strengthening ( s
0
) and grain boundaries (GBs) 
strengthening ( s
g
) [ 74 ]. In additively manufactured 
samples, the rapid solidification associated with steep 
thermal gradients introduces high residual stresses, 
which are accommodated by a high density of dislo -
cations into cellular boundaries that impede dislocation 
motion upon deformation. This additional dislocation 
forest strengthening ( s
d
) contribution is quantified 
using Taylor’s hardening law [ 75 , 76 ]. Therefore, the com -
bined yield strength ( s
YS
) expression is given by:.
s
YS
= s
0
+ s
g
+ s
d
= s
0
+ k × d
 1/2
+ M · a · G · b · r
1/2
(5) 
Here, k is the Hall-Petch coefficient, d is the average grain 
size determined by the line intercept method, M is the 
Taylor factor, a is the obstacle strength, G is the shear 
modulus, b is the Burgers vector, and r is the dislocation 
density. For equiatomic CoCrNi alloy, s
0
= 21 8 MP a [ 77 ], 
k = 26 5 MPa√µm [ 77 ], d = 14 1 mm, M = 3.06 [ 77 ], 
a = 0.2 [ 77 ], G = 90 GP a [ 77 ], b = 0.25 2 nm , and 
r = 1.69 × 10
14
m
 2 
were used, and the estimated s
YS 
using Equation (5) was ∼421 MPa, which agrees well 
with the average experimental value of ∼417 MPa. Fur -
thermore, using Zhu et al. [ 29 ] estimated upper bound 
values of s
0 
and k , i.e. 174 MPa and 812 MPa√µm for 
equiatomic CoCrNi alloy, the estimated s
YS 
is approxi -
mately 423 MPa, which is again in good agreement with 
the average experimental value. These results indicate 
that the experimentally observed yield strength can be 
reasonably described by Equation (5) ; however, there 
exists an uncertainty in the available material constants 
in the literature [ 29 , 77 , 78 ].
Upon comparing LSFE and HSFE alloys, the enhanced 
yield strength of the former at 298 K can primarily be 
attributed to its higher Cr content (130%), combined 
with its lower SFE. Cr enhances solid solution strengthen -
ing due to its larger atomic size (which enhances mean 
Figure 14. EBSD-derived microstructural analysis of deformed HSFE and LSFE alloys at 77 K. (a,b) IQ + IPF maps from (a) HSFE and (b) 
LSFE alloys revealing both dislocation slip-mediated mechanisms and deformation twinning. The corresponding point-to-point mis -
orientation profiles in (c,d) along the white arrows confirm the presence of the Σ3 twin boundaries, exhibiting a typical 60° misor -
ientation. (e) Magnified IQ + IPF map from a marked section in (b) showcasing extensive lens-shaped twins.
14 
 A. CHANDRAKER ET AL.

## Page 16

square atomic displacement [ 79 ]) and higher modulus 
than Ni and Co. The resulting higher geometrical lattice 
distortion and stress fields due to local changes in shear 
modulus interact with dislocation stress fields, impeding 
their motion, thus increasing lattice friction/solid solution 
strengthening. Additionally, the lower SFE promotes 
more widely spaced Shockley partial dislocations, with a 
stacking fault region enclosed between them [ 79 ]. This 
separation hinders their recombination, suppressing 
cross-slip and favouring planar dislocation glide. The 
resulting planar slip of extended dislocations is more 
difficult than that of compact dislocations, requiring 
higher stresses and thereby contributing to the increased 
lattice friction in line with the Friedel-Escaig mechanism 
[ 80 , 81 ]. Additionally, in LSFE alloy, extended dislocations 
interacting with each other can form extended dislo -
cation nodes and Lomer-Cottrell locks [ 82 ], which serve 
as effective barriers to dislocation motion, thereby 
increasing the dislocation forest strengthening for LSFE 
alloy. Furthermore, at GBs, the constriction of extended 
dislocations is necessary for transmission, a process that 
is more difficult in LSFE due to its lower SFE, further 
Figure 15. TEM-based microstructural analysis of deformed HSFE and LSFE alloys at 77 K. BF-TEM micrographs from the (a) HSFE and 
(b) LSFE alloys showcasing marked planar fault-like features. The corresponding SADPs from the (c) HSFE and (d) LSFE alloys acquired 
near <110> zone axis showcasing matrix spots (green dashed circles), twin spots (orange), and ε-martensite spots (blue). The coloured 
DF-TEM micrographs in (e) and (f), acquired using twin and HCP phase-related reflections from the HSFE sample, showcase some 
planar features corresponding to bright contrast deformation twin lamellae, while some left thin planar features sandwiched 
between deformation twins and the surrounding FCC matrix correspond to bright contrast ε-martensite lamellae with HCP structure. 
(g, h) HR-STEM micrographs from the HSFE alloy reveal deformation twins, intrinsic stacking fault (ISF), and HCP ε-martensite, charac -
terised as overlapping ISFs, embedded in the FCC matrix. The fast Fourier transform (FFT) of micrograph in (g) is shown in its inset.
VIRTUAL AND PHYSICAL PROTOTYPING 
 15

## Page 17

contributing to the grain boundary strengthening. 
Additionally, the higher Cr concentration at cell bound -
aries ( Figure 7 ) and GBs enhances their strength, contri -
buting to increased dislocation forest and grain 
boundary strengthening in the LSFE alloy.
Direct estimation of the specific s
0 
and k values for the 
additively manufactured HSFE and LSFE alloys was not 
possible due to the absence of yield strength data as a 
function of grain size. Nevertheless, the yield strength of 
the LSFE alloy at 298 K (∼415 MPa) is nearly identical to 
that of the additively manufactured equiatomic CoCrNi 
alloy (∼417 MPa). At first glance, this is unexpected 
because the LSFE matrix contains more Cr (∼35%, even 
with segregation at cell boundaries) than the equiatomic 
variant, which would typically enhance solid solution 
strengthening and lower the SFE via a higher Cr/Ni 
ratio. However, the LSFE also has ∼31% less Co, and 
since Co stabilises the HCP phase and lowers the SFE 
[ 20 ], its reduction offsets the strengthening effect of 
increased Cr. Therefore, given that both alloys share 
similar lattice parameters, SFEs, grain sizes, and dislo -
cation densities, their σ₀ and k values in the Hall–Petch 
relation are expected to be comparable, leading to their 
similar yield strengths despite compositional differences.
In contrast, at 298 K, HSFE exhibits a notably lower YS 
of ∼296 MPa than both equiatomic and LSFE alloys. This 
suggests that the lower Cr content and higher SFE in the 
HSFE alloy likely led to reduced contributions from solid 
solution strengthening, grain boundary strengthening, 
and dislocation forest strengthening compared to the 
equiatomic and LSFE alloys. Moreover, the higher SFE 
of the HSFE alloy promotes easier cross-slip of dislo -
cations onto favourable slip planes, facilitating easier 
plastic deformation and lower yield strength.
Further experimental investigations, including tensile 
testing of samples with systematically varied grain sizes, 
are required to accurately determine the material con -
stants for the non-equiatomic alloys at both 298 and 
77 K. However, these studies are beyond the scope of 
the present work.
4.2. Deformation and damage mechanisms at 
298 and 77 K
The mechanical responses of additively manufactured 
HSFE and LSFE alloys reflect a remarkable synergy 
between strength and ductility, governed mainly by 
their compositions and intrinsic SFEs. At 298 K, the defor -
mation in the HSFE alloy is primarily governed by dislo -
cation slip-mediated mechanisms, including dislocation 
slip and their interactions with dislocations confined 
within the AM-induced cell boundaries and GBs ( Figures 
12 (a), 13 (a) and schematic in Figure 16 (a)). The relatively 
high SFE of this alloy is expected to promote a more 
compact dislocation core, which will facilitate cross-slip 
that requires lower stress for dislocation movement 
across different slip planes. This enhances the alloy’s 
ability to deform uniformly by slip without necessitating 
additional mechanisms such as twinning.
In contrast, the LSFE alloy at 298 K exhibits a more 
complex deformation behaviour, incorporating additional 
deformation twinning ( Figures 12 (c), 13 (b–f) and 16 (b)), 
akin to that seen in the equiatomic composition, which 
is attributed to their low SFE. The deformation twinning 
is expected to initiate beyond the yield point [ 7 , 13 ]. The 
contribution of twinning through a dynamic Hall-Petch 
effect [ 83 ], in addition to slip, significantly enhances 
the strain hardening capability and ductility of the 
LSFE alloy, leading to a more favourable strength- 
ductility synergy relative to the HSFE alloy at 298 K 
(see Figures 9 (a) and 10 ).
At 77 K, both alloys demonstrate a marked increase 
in strength relative to their performance at 298 K 
( Figures 9 (a) and 10 ). The increment in yield strength 
at low temperature can be attributed to the combined 
effects of increased solid solution, dislocation forest, 
and grain boundary strengthening contributions. 
These mechanisms are amplified by the reduction in 
thermal energy, an increase in shear modulus, elevated 
drag forces, and an expected decrease in SFE at lower 
temperatures, all of which contribute to higher resist -
ance to dislocation motion.
A striking feature at 77 K is the substantial increase 
in WHR for both alloys ( Figure 9 (b)), primarily driven 
by an increased propensity for planar dislocation slip 
and its associated interactions, due to the reduction 
in SFE. Additionally, extensive deformation twinning 
and TRIP effect via the formation of ε-martensite with 
an HCP crystal structure further contribute to the elev -
ated WHR ( Figures 14 , 15 and 16 (c,d)). These mechan -
isms are absent in the HSFE alloy at 298 K, whereas 
the LSFE alloy exhibits less pronounced twinning and 
no evidence of HCP phase transformation at 298 K. 
For example, in the LSFE sample, the average twin 
width at 77 K reaches 72 ± 40 nm, which is approxi -
mately 166% wider than the 27 ± 10 nm measured 
at 298 K.
The increased twinning propensity at lower tempera -
tures can be attributed to the disparity in temperature sen -
sitivity between the critical resolved shear stress (CRSS) 
required for slip and the stress required for twinning. As 
temperature decreases, the reduction in thermal energy, 
increase in shear modulus, and higher drag forces collec -
tively hinder dislocation mobility, raising the CRSS for 
slip. In contrast, the stress needed for twin nucleation 
remains relatively insensitive to temperature, facilitating 
16 
 A. CHANDRAKER ET AL.

## Page 18

the earlier activation of twinning and its complementary 
role alongside slip at cryogenic conditions.
Furthermore, deformation-induced HCP phase trans -
formation was observed in both alloys at 77 K, aligning 
with the expected behaviour under high stress and 
strain at cryogenic temperatures [ 84 ], and consistent 
with prior observations reported for the as-recrystallized 
LSFE variant [ 24 ]. Density functional theory (DFT) calcu -
lations for equiatomic CoCrNi [ 13 ] indicate that the HCP 
phase is energetically more stable than the FCC phase 
at 0 K. While vibrational entropy must be considered for 
accurate phase stability predictions at finite temperatures, 
the significant energy difference suggests that the HCP 
phase remains thermodynamically favourable at low 
temperatures [ 13 ]. Furthermore, the computed average 
magnitudes of the [11
̅
20]
HCP 
and [1
̅
10]
FCC 
vectors are 
2.492 and 2.501 Å, respectively [ 13 ]. This minimal lattice 
mismatch implies a low interfacial energy for the 
(0001)
HCP 
and (111)
FCC 
boundaries, supporting their fre -
quent experimental observation. Notably, HCP lamellae 
are often found embedded between a deformation twin 
and the surrounding FCC matrix, forming nanotwin– 
HCP composite regions ( Figures 15 (e,f) and 16 (c,d)), con -
sistent with previous reports [ 13 85 ].
Prior studies have proposed that the nucleation of the 
HCP phase may be facilitated by the formation of stair-rod 
dislocations and the overlap of stacking faults [ 86 ]. The 
transformation from FCC to HCP occurs through the coor -
dinated glide of Shockley partial dislocations on alternat -
ing {111} planes of the FCC matrix. Niu et al. [ 87 ] described 
the role of deformation twins in the phase transformation 
in equiatomic CoCrNi alloys. It was suggested that the 
glide of edge-character partial dislocations along twin 
boundaries can nucleate a three-layered HCP region. 
Repeated slip of these partials further extends the HCP 
structure, forming multi-layered ε-martensite. The 
strengthening from such transformations arises from a 
dynamic Hall–Petch effect and increased resistance to dis -
location motion across twin–HCP interfaces [ 85 ]. The HCP 
lamellar structures are expected to act as strong barriers 
to dislocation motion, particularly because transmitting 
edge dislocations into the HCP region requires activation 
of dislocations possessing a component along [0001]. 
These can be either 〈c〉 or 〈c + a〉 – dislocations, both of 
which typically have high CRSS in HCP crystals, especially 
under cryogenic conditions [ 13 , 88 ]. Together, these 
mechanisms contribute to the increased strength and 
WHR in both alloys.
Among the two alloys, the LSFE alloy exhibits superior 
strength and WHR at 77 K compared to the HSFE alloy. 
This indicates that the combined influence of higher Cr 
content and lower SFE of the LSFE more strongly 
Figure 16. Schematic illustrating observed active deformation mechanisms for (a,c) HSFE and (b,d) LSFE alloys at (a,b) 298 K and (c,d) 77 K.
VIRTUAL AND PHYSICAL PROTOTYPING 
 17

## Page 19

enhances the contributions from solid solution, grain 
boundary, and dislocation forest hardening than at cryo -
genic temperatures. Additionally, the active deformation 
mechanisms at 77 K, including slip-mediated mechan -
isms, deformation twinning, and TRIP ( Figures 14 , 15
and 16 (c,d)), are more prominently activated in LSFE 
than in HSFE alloy, collectively resulting in pronounced 
strengthening and strain hardening. This observation 
aligns with previous findings in the Co-Cr-Ni system 
[ 20 , 24 ], where the volume fraction of the HCP phase is 
reported to increase with decreasing SFE. Additionally, 
a decrease in SFE can shift the dominant deformation 
mechanism, from deformation twinning to ε-martensitic 
transformation, consistent with multiple earlier studies 
[ 24 , 27 , 89 , 90 ].
Despite the enhanced strength and WHR observed in 
the LSFE alloy at 77 K, a relatively lower total elongation 
to failure was recorded compared to the HSFE counter -
part (see Figures 9 (a) and 10 ). To elucidate the 
mechanisms contributing to this contrasting ductility 
behaviour, detailed fractographic analyses were carried 
out on the fractured specimens. Secondary electron 
SEM micrographs in Figure 17 of both alloys tested at 
298 and 77 K revealed predominantly dimpled fracture 
surfaces, indicative of a ductile fracture mode even 
under cryogenic conditions.
Nonetheless, a closer examination of the LSFE sample 
fractured at 77 K revealed several dark-contrast particles, 
measuring roughly 40–90 µm in diameter and covering 
about 1.4% of the fracture surface, outlined in 
Figure 18 (a). At high magnification ( Figure 18 (b)), these 
particles appeared fractured and the EDS point scan analy -
sis confirmed them to be enriched in Cr ( Figure 18 (c)). 
Complementary XRD analysis, using a reduced step size 
(Δ2θ = 0.006°) and slow scan speed (1° per min), showed 
that in addition to the primary FCC peaks, weak reflections 
corresponding to BCC Cr (lattice parameter = 0.290 nm) 
[ 91 ]. were present (see Figure 19 ). These observations 
Figure 17. Secondary electron SEM micrographs revealing fracture surfaces of (a,c) HSFE; (b,d) LSFE samples fractured at (a,b) 298 K 
and (c,d) 77 K. The presence of dimples, indicating a predominantly ductile fracture mode, is evident across all conditions.
18 
 A. CHANDRAKER ET AL.

## Page 20

confirm that the particles are unmelted Cr powder 
retained from the initial feedstock, a feature more promi -
nent in the LSFE alloy due to its higher Cr content.
These unmelted Cr particles and their interfaces with 
the matrix likely served as preferential sites for crack 
initiation and propagation, particularly under the high 
Figure 18. Secondary electron SEM micrographs revealing fracture surface of LSFE sample fractured at 77 K. (a) Shows circled dark 
contrast particles dispersed non-uniformly across the fracture surface; (b) Magnified view of the marked area in (a) shows cracked dark 
contrast particle (highlighted by white dashed line); (c) EDS point scan profile obtained from the region marked by red star in (b) show 
Cr enrichment.
Figure 19. XRD pattern acquired from LSFE alloy at a low step size of Δ2θ = 0.006° and scan speed of 1° per min, showcasing BCC Cr 
peaks along with a shoulder peak around 44°, zoomed in the inset.
VIRTUAL AND PHYSICAL PROTOTYPING 
 19

## Page 21

stress at 77 K, thereby contributing to the premature 
failure and reduced ductility of the LSFE alloy. Although 
similar particles were also identified in the LSFE samples 
tested at 298 K, their influence on ductility appears less 
severe. This can be attributed to the ease of dislocation 
slip at 298 K, which may facilitate stress redistribution, 
accommodate strain mismatch at the particle/matrix 
interface, and delay the onset of particle-induced crack -
ing. Thus, the combined effects of reduced slip activity 
and unmelted brittle Cr particles are proposed to 
govern the reduced ductility observed in the LSFE 
alloy at 77 K. A marginally higher energy density, 
achieved by increasing the laser power and/or reducing 
the scan speed compared to the parameters used in this 
study, may facilitate complete melting of the Cr particles 
in the LSFE alloy, potentially leading to improved duct -
ility in the resulting composition.
Finally, the reduction in tensile ductility in literature 
has also been linked to the formation of deformation- 
induced ε-martensite laths in Co-based alloys and 
high-Mn steels [ 27 , 92 ], which promotes crack initiation 
at boundaries they intersect, an effect that intensifies 
with decreasing SFE. Given the low SFE of the LSFE 
alloy, a higher ε-martensite fraction is expected, poten -
tially contributing to its lower ductility relative to the 
HSFE alloy at 77 K, as reported in Co–Cr–Ni systems 
[ 20 , 24 ]. However, since both HSFE and LSFE fracture 
surfaces predominantly display transgranular dimples 
without evidence of intergranular cracking due to 
ε-martensite [ 20 ], this mechanism is unlikely to be the 
dominant factor.
5. Conclusions
In this study, three CoCrNi-based MPEAs – equiatomic 
(Co
32
Cr
34
Ni
34
), LSFE (Co
22
Cr
46
Ni
32
), and HSFE (Co
30
Cr
20 -
Ni
50
) – were fabricated via the DED process to systema -
tically examine how compositional tuning of SFE 
influences tensile properties and underlying defor -
mation mechanisms. The equiatomic alloy was first 
printed to validate the process parameters, and it exhib -
ited excellent tensile properties and expected defor -
mation behaviour, thereby confirming the adequacy of 
the printing conditions used for the two other compo -
sitions. The key findings regarding the LSFE and HSFE 
alloys are summarised as follows: 
.
The LSFE alloy exhibited higher yield strength than the 
HSFE alloy at both 298 and 77 K. This is attributed to 
its higher Cr content and lower SFE, which increases 
the typical strengthening contributions from solid sol -
ution, dislocation forest, and grain boundaries.
.
Although the precise values of lattice friction (σ₀) and 
the Hall–Petch constant (k) could not be directly 
determined for the either alloy, the LSFE alloy exhibits 
comparable room temperature yield strength, grain 
size, lattice parameter, dislocation density, and SFE 
to the equiatomic composition – indicating that its 
σ₀ and k values are likely similar. In contrast, the 
lower yield strength of the HSFE alloy suggests that 
its σ₀ and k values are comparatively reduced.
.
At 298 K, deformation in the HSFE alloy was accom -
modated through dislocation slip-mediated mechan -
isms, consistent with its higher SFE. In contrast, the 
LSFE alloy demonstrated additional activation of 
deformation twinning, leading to greater work-hard -
ening capability and a superior strength-ductility 
trade-off.
.
Under 77 K, both alloys exhibited substantial 
increases in strength and work-hardening rates. The 
HSFE alloy demonstrated exceptional ductility 
(∼74%) with a tensile strength of ∼800 MPa, while 
the LSFE alloy exhibited a higher ultimate tensile 
strength exceeding 1 GPa and a higher work-harden -
ing rate, albeit with lower ductility (∼45%).
.
In both alloys, multiple deformation mechanisms 
were activated at 77 K, including dislocation slip- 
mediated mechanisms, twinning (TWIP), and ε-mar -
tensite formation (TRIP). These mechanisms contribu -
ted to enhanced strain hardening and strength, with 
LSFE showing more pronounced contributions due 
to its higher Cr content and lower SFE.
.
Despite its superior strength, the LSFE alloy exhibited 
relatively lower ductility at 77 K than HSFE. Fracto -
graphic and microstructural analysis revealed the 
presence of some unmelted Cr particles retained 
from the AM process, which themselves or their inter -
face with the matrix served as crack initiation sites 
and reduced ductility by promoting early failure. 
These features were absent in HSFE and less detri -
mental in LSFE at 298 K, where slip is more readily 
activated and accommodates strain mismatch. 
Additionally, the formation of more pronounced ε- 
martensite laths in LSFE, which are known to 
promote crack initiation at intersected boundaries, 
may have further contributed to its reduced ductility.
In summary, CoCrNi-based MPEAs were fabricated via 
DED, showcasing superior strength-ductility combinations 
over comparable cast or AM alloys. The findings highlight 
that precise compositional tuning of SFE effectively 
enhances mechanical performance, especially for struc -
tural applications in cryogenic environments. Further 
gains may be achieved by incorporating strategic alloying 
elements and tailored secondary phases.
20 
 A. CHANDRAKER ET AL.

## Page 22

Acknowledgements
The authors thank the Advanced Centre for Microscopy and 
Microanalysis (AFMM), IISc, for access to EBSD and TEM facilities 
and appreciate the support of its technical staff. Sincere thanks 
are extended to Prof. Rajeev Ranjan and Mr Deepak Sharma, 
both at the Department of Materials Engineering, IISc, for pro -
viding access and assistance in utilising the ball milling and XRD 
facilities. The authors also acknowledge the I-STEM facility and 
its staff at IISc for access to XRD instrumentation.
Author contributions
CRediT: Abhinav Chandraker: Data curation, Formal analysis, 
Investigation, Validation, Visualization, Writing – original draft; 
Ketan Sharma: Data curation, Formal analysis, Investigation, 
Visualization, Writing – original draft; Chethan Konkati: Inves -
tigation, Writing – review & editing; Sampad Barik: Investi -
gation, Writing – review & editing; Shubham Sisodia: 
Investigation, Writing – review & editing; 
Kaushik Chatterjee: Resources, Writing – review & editing; 
Ankur Chauhan: Conceptualization, Funding acquisition, 
Methodology, Project administration, Resources, Supervision, 
Validation, Visualization, Writing – original draft, Writing – 
review & editing.
Disclosure statement
No potential conflict of interest was reported by the author(s).
Funding
AC gratefully acknowledges financial supports from the Indian 
Institute of Science (IISc) and Infosys Foundation, Bengaluru. 
The first author also acknowledges funding received under 
the PMRF scheme.
Data availability statement
The data that support the findings of this study are available 
from the corresponding author, [AC], upon reasonable 
request. The data that support the findings of this study are 
openly available in Mendeley Data at https://data.mendeley. 
com/preview/tbps84cgxx?a=035220d3-16ec-4c9a-bb4f-7a9a0 
d795e80 .
ORCID
Abhinav Chandraker 
 http://orcid.org/0000-0002-9368-0599
Shubham Sisodia 
 http://orcid.org/0000-0001-5315-5637
References
[1] Yeh JW, Chen YL, Lin SJ, et al. High-entropy alloys – a new 
era of exploitation. Mater Sci Forum. 2007 ;560:1–9. doi: 10. 
4028/www.scientific.net/MSF.560.1
[2] Yeh J-W, Chen S-K, Lin S-J, et al. Nanostructured high- 
entropy alloys with multiple principal elements: novel 
alloy design concepts and outcomes. Adv Eng Mater. 
2004 ;6(5):299–303. doi: 10.1002/adem.200300567
[3] Shim SH, Pouraliakbar H, Hong SI. High strength dual Fcc 
phase CoCuFeMnNi high-entropy alloy wires with dislo -
cation wall boundaries stabilized by phase boundaries. 
Mater Sci Eng A. 2021 ;825:141875. doi: 10.1016/j.msea. 
2021.141875
[4] Shim SH, Pouraliakbar H, Hong SI. Hierarchical 
structured As-cast CrFeNiMn
0.5
Cu
0.5 
high entropy alloy 
with excellent tensile strength/ductility properties. Scr 
Mater. 2022 ;210:114473. doi: 10.1016/j.scriptamat.2021. 
114473
[5] Pouraliakbar H, Shim SH, Kim YK, et al. Microstructure 
evolution and mechanical properties of 
(CoCrNi)90(AlTiZr)5(CuFeMo)5 multicomponent alloy: A 
pathway through multicomponent alloys toward new 
superalloys. J Alloys Compd. 2021 ;860:158412. doi: 10. 
1016/j.jallcom.2020.158412
[6] Gludovatz B, Hohenwarter A, Thurston KVS, et al. 
Exceptional damage-tolerance of a medium-entropy 
alloy CrCoNi at cryogenic temperatures. Nat Commun. 
2016 ;7(1):10602. doi: 10.1038/ncomms10602
[7] Laplanche G, Kostka A, Reinhart C, et al. Reasons for the 
superior mechanical properties of medium-entropy 
CrCoNi compared to high-entropy CrMnFeCoNi. Acta 
Mater. 2017 ;128:292–303. doi: 10.1016/j.actamat.2017.02. 
036
[8] Xue P, Zhu L, Xu P, et al. Crconi medium-entropy alloy 
thin-walled parts manufactured by laser metal depo -
sition: microstructure evolution and mechanical aniso -
tropy. Mater Sci Eng A. 2021 ;817:141306. doi: 10.1016/j. 
msea.2021.141306
[9] Weng F, Chew Y, Zhu Z, et al. Excellent combination of 
strength and ductility of CoCrNi medium entropy alloy 
fabricated by laser aided additive manufacturing. 
Addit Manuf. 2020 ;34:101202. doi: 10.1016/j.addma.2020. 
101202
[10] Lu K, Chauhan A, Litvinov D, et al. Micro-mechanical 
deformation behavior of CoCrFeMnNi high-entropy 
alloy. J Mater Sci Technol. 2022 ;100:237–245. doi: 10. 
1016/j.jmst.2021.04.079
[11] Deng HW, Wang MM, Xie ZM, et al. Enhancement of 
strength and ductility in non-equiatomic CoCrNi 
medium-entropy alloy at room temperature via trans -
formation-induced plasticity. Mater Sci Eng A. 
2021 ;804:140516. doi: 10.1016/j.msea.2020.140516
[12] Tirunilai AS, Sas J, Weiss K-P, et al. Peculiarities of defor -
mation of CoCrFeMnNi at cryogenic temperatures. J 
Mater Res. 2018 ;33(19):3287–3300. doi: 10.1557/jmr. 
2018.252
[13] Miao J, Slone CE, Smith TM, et al. The evolution of the 
deformation substructure in a Ni–Co–Cr equiatomic 
solid solution alloy. Acta Mater. 2017 ;132:35–48. doi: 10. 
1016/j.actamat.2017.04.033
[14] Otto F, Dlouhý A, Somsen C, et al. The influences of temp -
erature and microstructure on the tensile properties of a 
CoCrFeMnNi high-entropy alloy. Acta Mater. 
2013 ;61(15):5743–5755. doi: 10.1016/j.actamat.2013.06.018
[15] Laplanche G, Kostka A, Horst OM, et al. Microstructure 
evolution and critical stress for twinning in the 
CrMnFeCoNi high-entropy alloy. Acta Mater. 
2016 ;118:152–163. doi: 10.1016/j.actamat.2016.07.038
VIRTUAL AND PHYSICAL PROTOTYPING 
 21

## Page 23

[16] Gali A, George EP. Tensile properties of high- and 
medium-entropy alloys. Intermetallics. 2013 ;39:74–78. 
doi: 10.1016/j.intermet.2013.03.018
[17] Gludovatz B, Hohenwarter A, Catoor D, et al. A fracture- 
resistant high-entropy alloy for cryogenic applications. 
Science. 2014 ;345(6201):1153–1158. doi: 10.1126/science. 
1254581
[18] Coury FG, Clarke KD, Kiminami CS, et al. High throughput 
discovery and design of strong multicomponent metallic 
solid solutions. Sci Rep. 2018 ;8(1):8600. doi: 10.1038/ 
s41598-018-26830-6
[19] Coury FG, Santana D, Guo Y, et al. Design and In-situ 
characterization of a strong and ductile Co-rich multi -
component alloy with transformation induced plasticity. 
Scr Mater. 2019 ;173:70–74. doi: 10.1016/j.scriptamat. 
2019.07.045
[20] Yoshida S, Ikeuchi T, Bai Y, et al. Effect of cobalt-content 
on mechanical properties of non-equiatomic Co–Cr–Ni 
medium entropy alloys. Mater Trans. 2020 ;61(4):587– 
595. doi: 10.2320/matertrans.MT-MK2019004
[21] Yan J, Fang W, Huang J, et al. Plastic deformation 
mechanism of CoCrxNi medium entropy alloys. Mater 
Sci Eng A. 2021 ;814:141181. doi: 10.1016/j.msea.2021. 
141181
[22] Huang D, Zhuang Y, Wang C. Advanced mechanical prop -
erties obtained via accurately tailoring stacking fault 
energy in Co-Rich and Ni-depleted Co
x
Cr
33
Ni
67−x 
medium-entropy alloys. Scr Mater. 2022 ;207:114269. 
doi: 10.1016/j.scriptamat.2021.114269
[23] Yan JX, Zhang ZJ, Zhang P, et al. Design and optimization 
of the composition and mechanical properties for non- 
equiatomic CoCrNi medium-entropy alloys. J Mater Sci 
Technol. 2023 ;139:232–244. doi: 10.1016/j.jmst.2022.07. 
031
[24] Wang Z, Li L, Chen Z, et al. A new route to achieve high 
strength and high ductility compositions in Cr-Co-Ni- 
based medium-entropy alloys: A predictive model con -
necting theoretical calculations and experimental 
measurements. J Alloys Compd. 2023 ;959:170555. 
doi: 10.1016/j.jallcom.2023.170555
[25] Zhang HF, Yan HL, Yu H, et al. The effect of Co and Cr sub -
stitutions for Ni on mechanical properties and plastic 
deformation mechanism of FeMnCoCrNi high entropy 
alloys. J Mater Sci Technol. 2020 ;48:146–155. doi: 10. 
1016/j.jmst.2020.03.010
[26] Liu SF, Wu Y, Wang HT, et al. Stacking fault energy of face- 
centered-cubic high entropy alloys. Intermetallics. 
2018 ;93:269–273. doi: 10.1016/j.intermet.2017.10.004
[27] Wei D, Li X, Jiang J, et al. Novel Co-rich high performance 
twinning-induced plasticity (TWIP) and transformation- 
induced plasticity (TRIP) high-entropy alloys. Scr Mater. 
2019 ;165:39–43. doi: 10.1016/j.scriptamat.2019.02.018
[28] Ikeda Y, Körmann F, Tanaka I, et al. Impact of chemical 
fluctuations on stacking fault energies of CrCoNi and 
CrMnFeCoNi high entropy alloys from first principles. 
Entropy. 2018 ;20(9):655. doi: 10.3390/e20090655
[29] Zhu L, Li G, Dong W, et al. On the grain size dependence 
of competing deformation mechanisms in a CrCoNi 
medium entropy alloy. Acta Mater. 2025 ;289:120907. 
doi: 10.1016/j.actamat.2025.120907
[30] Schuh B, Völker B, Todt J, et al. Influence of annealing on 
microstructure and mechanical properties of a 
nanocrystalline CrCoNi medium-entropy alloy. Materials 
(Basel). 2018 ;11(5):662. doi: 10.3390/ma11050662
[31] Ma Y, Yuan F, Yang M, et al. Dynamic shear deformation 
of a CrCoNi medium-entropy alloy with heterogeneous 
grain structures. Acta Mater. 2018 ;148:407–418. doi: 10. 
1016/j.actamat.2018.02.016
[32] Yang M, Yan D, Yuan F, et al. Dynamically reinforced het -
erogeneous grain structure prolongs ductility in a 
medium-entropy alloy with gigapascal yield strength. 
Proc Natl Acad Sci USA. 2018 ;115(28):7224–7229. doi: 10. 
1073/pnas.1807817115
[33] Slone CE, Miao J, George EP, et al. Achieving ultra-high 
strength and ductility in equiatomic CrCoNi with partially 
recrystallized microstructures. Acta Mater. 2019 ;165:496– 
507. doi: 10.1016/j.actamat.2018.12.015
[34] Herzog D, Seyda V, Wycisk E, et al. Additive manufactur -
ing of metals. Acta Mater. 2016 ;117:371–392. doi: 10. 
1016/j.actamat.2016.07.019
[35] Gorsse S, Hutchinson C, Gouné M, et al. Additive 
manufacturing of metals: a brief review of the character -
istic microstructures and properties of steels, Ti–6Al–4V 
and high-entropy alloys. Sci Technol Adv Mater. 
2017 ;18(1):584–610. doi: 10.1080/14686996.2017.1361305
[36] Yadollahi A, Shamsaei N, Thompson SM, et al. Effects of 
process time interval and heat treatment on the 
mechanical and microstructural properties of direct 
laser deposited 316L stainless steel. Mater Sci Eng A. 
2015 ;644:171–183. doi: 10.1016/j.msea.2015.07.056
[37] Smoqi Z, Bevans BD, Gaikwad A, et al. Closed-Loop 
control of meltpool temperature in directed energy 
deposition. Mater Des. 2022 ;215:110508. doi: 10.1016/j. 
matdes.2022.110508
[38] Paudel BJ, Marshall GJ, Thompson SM. Thermal monitor -
ing and modeling of Ti–6Al–4V thin wall temperature dis -
tribution during blown powder laser directed energy 
deposition. J Manuf Sci Eng. 2022 ;144(4):041007. doi: 10. 
1115/1.4052285
[39] Jeong J, Webster S, Liao S, et al. Cooling rate 
measurement in directed energy deposition using 
photodiode-based Planck thermometry (PDPT). Addit 
Manuf Lett. 2022 ;3:100101. doi: 10.1016/j.addlet.2022. 
100101
[40] Pham MS, Dovgyy B, Hooper PA. Twinning induced plas -
ticity in austenitic stainless steel 316L made by additive 
manufacturing. Mater Sci Eng A. 2017 ;704:102–111. 
doi: 10.1016/j.msea.2017.07.082
[41] Ma M, Wang Z, Zeng X. A comparison on metallurgical 
behaviors of 316L stainless steel by selective laser 
melting and laser cladding deposition. Mater Sci Eng A. 
2017 ;685:265–273. doi: 10.1016/j.msea.2016.12.112
[42] Arif ZU, Khalid MY, Rehman Eu. Laser-aided additive man -
ufacturing of high entropy alloys: processes, properties, 
and emerging applications. J Manuf Process. 
2022 ;78:131–171. Preprint, Elsevier Ltd, December 2022. 
doi: 10.1016/j.jmapro.2022.04.014
[43] Köster EH, Thölén AR, Howie A. Stacking fault energies of 
Ni–Co–Cr alloys. Philos Mag. 1964 ;10(108):1093–1095. 
doi: 10.1080/14786436408225417
[44] Liu XL, Lindwall G, Gheno T, et al. Thermodynamic mod -
eling of Al–Co–Cr, Al–Co–Ni, Co–Cr–Ni ternary systems 
towards a description for Al–Co–Cr–Ni. Calphad. 
2016 ;52:125–142. doi: 10.1016/j.calphad.2015.12.007
22 
 A. CHANDRAKER ET AL.

## Page 24

[45] Omori T, Sato J, Shinagawa K, et al. Experimental determi -
nation of phase equilibria in the Co-Cr-Ni system. J Phase 
Equilib Diffus. 2014 ;35(2):178–185. doi: 10.1007/s11669- 
014-0292-z
[46] Zhanpeng J. A study of the range of stability of σ phase 
in some ternary systems. Scand J Metall. 1981 ;10(6): 
279–287.
[47] Slotwinski JA, Garboczi EJ, Hebenstreit KM. Porosity 
measurements and analysis for metal additive manufac -
turing process control. J Res Natl Inst Stand Technol. 
2014 ;119:494–528. doi: 10.6028/jres.119.019
[48] Williamson GK, Hall WH. X-Ray line broadening from filed 
aluminium and wolfram. Acta Metall. 1953 ;1(1):22–31. 
doi: 10.1016/0001-6160(53)90006-6
[49] Williamson GK, Smallman RE. III. Dislocation densities in 
some annealed and cold-worked metals from measure -
ments on the X-ray debye-scherrer spectrum. Philos 
Mag. 1956 ;1(1):34–46. doi: 10.1080/14786435608238074
[50] Garcia-Mateo C, Caballero FG, Capdevila C, et al. 
Estimation of dislocation density in bainitic microstruc -
tures using high-resolution dilatometry. Scr Mater. 
2009 ;61(9):855–858. doi: 10.1016/j.scriptamat.2009.07.013
[51] Ul-Hamid A, Tawancy HM, Mohammed A-RI, et al. 
Quantitative WDS analysis using electron probe microa -
nalyzer. Mater Charact. 2006 ;56(3):192–199. doi: 10.1016/ 
j.matchar.2005.11.007
[52] Marattukalam JJ, Karlsson D, Pacheco V, et al. The effect of 
laser scanning strategies on texture, mechanical proper -
ties, and site-specific grain orientation in selective laser 
melted 316L SS. Mater Des. 2020 ;193:108852. doi: 10. 
1016/j.matdes.2020.108852
[53] Kong D, Dong C, Wei S, et al. About metastable cellular 
structure in additively manufactured austenitic stainless 
steels. Addit Manuf. 2021 ;38:101804. doi: 10.1016/j. 
addma.2020.101804
[54] Sun H, Luo Z, Wang S, et al. Overcoming strength- 
ductility trade-off in CoCrNi medium entropy alloy by 
forming fine crescent grains in laser powder-bed fusion. 
Mater Lett. 2023 ;347:134644. doi: 10.1016/J.MATLET. 
2023.134644
[55] Wang J, Zou J, Yang H, et al. Exceptional strength-ductility 
synergy of additively manufactured CoCrNi medium- 
entropy alloy achieved by lattice defects in hetero -
geneous microstructures. J Mater Sci Technol. 
2022 ;127:61–70. doi: 10.1016/J.JMST.2022.03.024
[56] Han B, Zhang C, Feng K, et al. Additively manufactured 
high strength and ductility CrCoNi medium entropy 
alloy with hierarchical microstructure. Mater Sci Eng A. 
2021 ;820:141545. doi: 10.1016/J.MSEA.2021.141545
[57] Ge J, Chen C, Zhao R, et al. Strength-ductility synergy of 
CoCrNi medium-entropy alloy processed with laser 
powder bed fusion. Mater Des. 2022 ;219:110774. doi: 10. 
1016/J.MATDES.2022.110774
[58] Jinlong L, Zhiping Z, Wenli G. The effect of annealing on 
mechanical properties of selective laser melted CoCrNi 
medium-entropy alloy. Mater Lett. 2023 ;343:134353. 
doi: 10.1016/J.MATLET.2023.134353
[59] Jung KH, Tran MT, Shan Z, et al. Correlation of cryogenic 
deformation mechanisms to excellent strength-ductility 
of CrCoNi medium entropy alloy processed by selective 
laser melting. J Mater Res Technol. 2023 ;22:2297–2315. 
doi: 10.1016/J.JMRT.2022.12.084
[60] Niu P, Li R, Gan K, et al. Microstructure, properties, and 
metallurgical defects of an equimolar CoCrNi medium 
entropy alloy additively manufactured by selective laser 
melting. Metall Mater Trans A. 2021 ;52(2):753–766. 
doi: 10.1007/s11661-020-06121-4
[61] Zhou K, Cui D, Chai Z, et al. In-Situ tailoring microstruc -
tures to promote strength-ductility synergy in laser 
powder bed fusion of NiCoCr medium-entropy alloy. 
Addit Manuf. 2023 ;66:103443. doi: 10.1016/J.ADDMA. 
2023.103443
[62] Deshmukh PS, Yadav S, Dan Sathiaraj G, et al. Nano to 
macro-mechanical properties of laser directed energy 
deposited CoCrNi medium entropy alloy. Mater Today 
Commun. 2023 ;35:106351. doi: 10.1016/J.MTCOMM.2023. 
106351
[63] Weng F, Chew Y, Zhu Z, et al. Influence of oxides on the 
cryogenic tensile properties of the laser aided additive 
manufactured CoCrNi medium entropy alloy. Compos B 
Eng. 2021 ;216:108837. doi: 10.1016/J.COMPOSITESB.2021. 
108837
[64] Xue P, Zhu L, Xu P, et al. Microstructure evolution and 
enhanced mechanical properties of additively manufac -
tured CrCoNi medium-entropy alloy composites. J 
Alloys Compd. 2022 ;928:167169. doi: 10.1016/j.jallcom. 
2022.167169
[65] Kim YS, Chae H, Woo W, et al. Multiple deformation 
scheme in direct energy deposited CoCrNi medium 
entropy alloy at 210 K. Mater Sci Eng A. 2021 ;828:142059. 
doi: 10.1016/j.msea.2021.142059
[66] Bi X, Li R, Li T, et al. Anisotropic microstructure, properties 
and molecular dynamics simulation of CoCrNi medium 
entropy alloy fabricated by laser directed energy depo -
sition. Mater Sci Eng A. 2023 ;871:144834. doi: 10.1016/j. 
msea.2023.144834
[67] Xue P, Zhu L, Ning J, et al. Effect of laser incident energy 
on the densification and structure–property relationships 
of additively manufactured CrCoNi medium-entropy 
alloy. Virtual Phys Prototyp. 2021 ;16(4):404–416. doi: 10. 
1080/17452759.2021.1947509
[68] Tran MT, Nguyen TH, Kim DK, et al. Effect of hot isostatic 
pressing on the cryogenic mechanical properties of 
CrCoNi medium entropy alloy processed by direct 
energy deposition. Mater Sci Eng A. 2021 ;828:142110. 
doi: 10.1016/J.MSEA.2021.142110
[69] Sisodia S, Laplanche G, Rajkowski M, et al. Enhancing 
fatigue resistance of Cr-Mn-Fe-Co-Ni multi-principal 
element alloys by varying stacking fault energy and sigma 
(σ)-phase assisted grain-size reduction. Int J Fatigue. 
2025 ;191:108704. doi: 10.1016/j.ijfatigue.2024.108704
[70] Naeem M, He H, Zhang F, et al. Cooperative deformation 
in high-entropy alloys at ultralow temperatures. Sci Adv. 
2020 ;6(13):eaax4002. doi: 10.1126/sciadv.aax4002
[71] Chandan AK, Murugaiyan P, Chowdhury SG. 
Temperature-Dependent stacking fault energy, defor -
mation behavior, and tensile properties of a new high- 
entropy alloy. Mater Sci Eng A. 2023 ;883:145522. doi: 10. 
1016/j.msea.2023.145522
[72] Hall EO. The deformation and ageing of mild steel: III dis -
cussion of results. Proc Phys Soc London Sect B. 
1951 ;64(9):747–753. doi: 10.1088/0370-1301/64/9/303
[73] Petch NJ. The cleavage strength of polycrystals. J Iron 
Steel Inst. 1953 ;174:25–28.
VIRTUAL AND PHYSICAL PROTOTYPING 
 23

## Page 25

[74] Schneider M, George EP, Manescau TJ, et al. Analysis of 
strengthening due to grain boundaries and annealing 
twin boundaries in the CrCoNi medium-entropy alloy. Int 
J Plast. 2020 ;124:155–169. doi: 10.1016/j.ijplas.2019.08.009
[75] Taylor GI. The mechanism of plastic deformation of crys -
tals. Part I.—theoretical. Proc R Soc Lond A. 
1934 ;145(855):362–387. doi: 10.1098/rspa.1934.0106
[76] Nabarro FRN, Basinski ZS, Holt DB. The plasticity of pure 
single crystals. Adv Phys. 1964 ;13(50):193–323. doi: 10. 
1080/00018736400101031
[77] Yoshida S, Bhattacharjee T, Bai Y, et al. Friction stress and 
hall-petch relationship in CoCrNi equi-atomic medium 
entropy alloy processed by severe plastic deformation 
and subsequent annealing. Scr Mater. 2017 ;134:33–36. 
doi: 10.1016/j.scriptamat.2017.02.042
[78] Chandraker A, Barik S, Sai NJ, et al. Experimentally vali -
dated and empirically compared machine learning 
approach for predicting yield strength of additively man -
ufactured multi-principal element alloys from Co–Cr–Fe– 
Mn–Ni system. Metall Mater Trans A. 2025 ;56(2):571–586. 
doi: 10.1007/s11661-024-07661-9
[79] Okamoto NL, Yuge K, Tanaka K, et al. Atomic displace -
ment in the CrMnFeCoNi high-entropy alloy – a scaling 
factor to predict solid solution strengthening. AIP Adv. 
2016 ;6(12):125008. doi: 10.1063/1.4971371
[80] Escaig B. Sur Le Glissement Dévié Des Dislocations Dans La 
Structure Cubique à Faces Centrées. J Phys. 1968 ;29(2– 
3):225–239. doi: 10.1051/jphys:01968002902-3022500
[81] Escaig B. Dissociation and mechanical properties.disloca -
tion splitting and the plastic glide process in crystals. J 
Phys Colloq. 1974 ;35(C7):C7-151–C7-166. doi: 10.1051/ 
jphyscol:1974717
[82] Tang H, Niu P, Kang J, et al. Hierarchically microstructure 
endowing high strength-ductility synergy in CoCrNi 
medium entropy alloy fabricated by laser powder bed 
fusion. Mater Sci Eng A. 2025 ;940:148506. doi: 10.1016/j. 
msea.2025.148506
[83] Bouaziz O, Allain S, Scott C. Effect of grain and twin 
boundaries on the hardening mechanisms of twinning- 
induced plasticity steels. Scr Mater. 2008 ;58(6):484–487. 
doi: 10.1016/j.scriptamat.2007.10.050
[84] Zhao S, Li Z, Zhu C, et al. Amorphization in extreme defor -
mation of the CrMnFeCoNi high-entropy alloy. Sci Adv. 
2021 ;7(5):eabb3108. doi: 10.1126/sciadv.abb3108
[85] Tirunilai AS, Hanemann T, Reinhart C, et al. 
Comparison of cryogenic deformation of the concen -
trated solid solutions CoCrFeMnNi, CoCrNi and CoNi. 
Mater Sci Eng A. 2020 ;783:139290. doi: 10.1016/j.msea. 
2020.139290
[86] Fujita H, Ueda S. Stacking faults and f.c.c. (γ) → h.c.p. (ɛ) 
transformation in - type stainless steel. Acta Metall. 
1972 ;20(5):759–767. doi: 10.1016/0001-6160(72)90104-6
[87] Niu C, LaRosa CR, Miao J, et al. Magnetically-driven phase 
transformation strengthening in high entropy alloys. 
Nat Commun. 2018 ;9(1):1363. doi: 10.1038/s41467-018- 
03846-0
[88] Williams JC, Baggerly RG, Paton NE. Deformation 
behavior of HCP Ti-Al alloy single crystals. Metall Mater 
Trans A. 2002 ;33(3):837–850. doi: 10.1007/s11661-002- 
0153-y
[89] Kelly PM. The martensite transformation in steels with 
low stacking fault energy. Acta Metall. 1965 ;13(6):635– 
646. doi: 10.1016/0001-6160(65)90126-4
[90] Xu M, Mi Z, Li H, et al. Deformation mechanism transition 
in Fe–17Mn–0.4C–0.06V TWIP steel with different strain 
rates. Mater Sci Technol. 2018 ;34(2):242–251. doi: 10. 
1080/02670836.2017.1370157
[91] ‘ Https://Periodictable.Com - Chromium.’. ( n.d ). [accessed 
2025 Aug 6]. Available from: https://periodictable.com/ 
Elements/024/data.html.
[92] Koyama M, Sawaguchi T, Tsuzaki K. Premature fracture 
mechanism in an Fe-Mn-C austenitic steel. Metall Mater 
Trans A. 2012 ;43(11):4063–4074. doi: 10.1007/s11661- 
012-1220-7
24 
 A. CHANDRAKER ET AL.
