# sciadv.adq0083

<!-- source: D:\总文献\sciadv.adq0083.pdf -->
<!-- file_sha256: d4b7d706c88dee527f11342c524d6e5064ccf17a452d504300481977e4eeeee1 -->

## Page 1

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
1 of 14
MATERIALS SCIENCE
Integrated design of aluminum- enriched high- entropy 
refractory B2 alloys with synergy of high strength 
and ductility
Jie Qi1*, Xuesong Fan2, Diego Ibarra Hoyos1, Michael Widom3,4, Peter K. Liaw2*, Joseph Poon1,5*
Refractory high- entropy alloys (RHEAs) are promising high- temperature structural materials. Their large composi-
tional space poses great design challenges for phase control and high strength- ductility synergy. The present re-
search pioneers using integrated high- throughput machine learning with Monte Carlo simulations supplemented 
by ab initio calculations to effectively navigate phase selection and mechanical property predictions, developing 
single- phase ordered B2 aluminum- enriched RHEAs (Al- RHEAs) demonstrating high strength and ductility. These 
Al- RHEAs achieve remarkable mechanical properties, including compressive yield strengths up to 1.7 gigapascals, 
fracture strains exceeding 50%, and notable high- temperature strength retention. They also demonstrate a ten-
sile yield strength of 1.0 gigapascals with a ductility of 9%, albeit with B2 ordering. Furthermore, we identify va-
lence electron count domains for alloy ductility and brittleness with the explanation from density functional 
theory and provide crucial insights into elemental influence on atomic ordering and mechanical performance. The 
work sets forth a strategic blueprint for high- throughput alloy design and reveals fundamental principles govern-
ing the mechanical properties of advanced structural alloys.
INTRODUCTION
In the ceaseless quest to defy extreme temperatures and hostile environ-
ments, high- performance alloys become indispensable in aerospace, au-
tomotive, and power generation sectors. Conventional Ni/Co- based 
superalloys, despite their thermal stability and high- temperature me-
chanical properties, have inevitably encountered inherent performance 
ceilings, such as a melting point below 1500°C. The past decade has seen 
the advent of high- entropy alloys (HEAs) (1) with revolutionized perfor-
mance. The refractory high- entropy alloys (RHEAs), comprising refrac-
tory elements, Ti, V , Cr, Zr, Nb, Mo, Hf, Ta, and W , have stood out for 
elevated- temperature applications with high strength and ductility (2, 3). 
However, their broader adoption faces challenges, such as high cost, 
densities, and poor oxidation resistance. Al- containing RHEAs (Al- 
RHEAs) resembling aluminides have emerged as a solution (4–7), with 
the Al incorporation yielding cost/density reductions, and enhanced 
oxidation and corrosion resistance (8, 9). Moreover, Al inclusion typi-
cally induces the formation of an ordered body- centered- cubic (BCC)–
derivative (B2) phase within the disordered BCC matrix (10–12), further 
strengthening the alloys. This B2- BCC morphology sometimes under-
goes the “phase inversion” (5 ), a transformation of a continuous, 
channel- like B2 phase into discontinuous B2 phases surrounded by a 
BCC matrix after extended annealing, highlighting the thermal instabil-
ity of the mixed BCC- B2 phase configuration compared to the stable 
γ′- γ phases for Ni/Co- based superalloys.
Despite the noteworthy advantages of Al- RHEAs, their design in-
evitably introduces specific challenges. Most Al- RHEAs demonstrate 
limited ductility. The strong p- d electron interaction between the Al 
and refractory elements can precipitate brittle intermetallic phases 
(IMs) (11,  13). The dislocation movement impediment from B2 
long- range ordering (LRO) and the reduced slip planes from the 
BCC to B2 phase further limit their ductility (10). Excluding the 
mostly brittle Al- RHEAs due to the formation of Laves phases or 
other brittle IMs (11,  14), those composed solely of a B2 phase or 
BCC + B2 composite phase also seldom exhibit plasticity or ductility. 
For example, Al- RHEAs from the AlNbTiV (11,  13), AlCrNbTiV 
(13), AlNbTaTiZr (14, 15), AlNbTaTiVZr (15), AlCrMoTi (10), and 
AlMoNbTiV (16) systems have been documented to display com-
pressive plasticity limited to a maximum of 6% at room temperature. 
Therefore, careful phase and B2- LRO control becomes imperative. 
Besides, the design challenge resides in effectively navigating the 
vast HEA compositional space and optimizing manifold materials’ 
properties simultaneously to achieve the Pareto front. The conven-
tional trial- and- error approaches have become obsolete, making 
integrated computational material engineering (ICME) vital in 
material exploration ( 17–20). Moreover, how various material pa-
rameters fundamentally influence alloy formation and ductility is yet 
to be fully elucidated, which remains an area of substantial re-
search focus.
The present work features three core innovations that address the 
aforementioned challenges: First, a comprehensive alloy- design strate-
gy merges the cutting- edge machine learning (ML) models with an 
enhanced ICME framework combined with Monte Carlo (MC) simu-
lations, ab initio molecular dynamics (AIMD) simulations, ab initio 
relaxation, and classical computational methodologies, enabling high- 
throughput HEA predictions, effectively pinpointing potential high- 
performance alloys, and reducing experimental efforts. Second, joint 
endeavors from experiments and MC studies successfully optimize a 
series of single B2- phase AlHfNbTi(V) HEAs, exhibiting superior 
strength and ductility, compared to typical plasticity- constrained B2 
Al- RHEAs, highlighting aluminum’s role in atomic ordering and plas-
ticity control. Third, a prominent correlation between the valence elec-
tron count (VEC) (21) and alloy ductility elucidated in light of density 
functional theory (DFT) calculations underscores VEC’s importance 
within the property- prediction paradigm.
1Department of Physics, University of virginia, charlottesville, vA 22904, USA. 
2Department of Materials Science and engineering, the University of tennessee, 
Knoxville, tn 37996, USA. 3Department of Physics, carnegie Mellon University, 
Pittsburgh, PA 15213, USA. 4Department of Materials Science and engineering, 
carnegie Mellon University, Pittsburgh, PA 15213, USA. 5Department of Materials 
Science and engineering, University of virginia, charlottesville, vA 22904, USA.
*corresponding author. email: sjp9x@ virginia. edu (J.P .); pliaw@ utk. edu (P .K.l.); 
jq4xa@ virginia. edu (J.Q.)
copyright © 2024 the 
Authors, some rights 
reserved; exclusive 
licensee American 
Association for the 
Advancement of 
Science. no claim to 
original U.S. 
Government Works. 
Distributed under a 
creative commons 
Attribution 
noncommercial 
license 4.0 (cc BY- nc). 
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 2

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
2 of 14
Moving forward, this article will provide insights into a high- 
performance HEAs development methodology via ICME and theory- 
guided efficient compositional tuning. It delves into fundamental 
phenomena regarding the elemental influence on atomic ordering 
and the role of electronic structures on HEA- mechanical properties, 
laying a foundation for future alloy development and inspiring re-
search in this field.
RESUL TS
ICME model construction and results
The ICME model (Fig. 1) integrates phases and property prediction 
modules to design Al- RHEAs with high strengths and ductility. 
Considering phase predictions, CALPHAD (CALculation of PHAse 
Diagrams) frequently identifies Al- RHEAs’ Al- X- Y type (X and Y 
are refractory elements) B2- strengthening phase (22) as the BCC 
matrix (22, 23). Therefore, we adopt ML models trained specifically 
for Al- X- Y B2 and other phases [detailed in our prior work (24, 25)], 
which integrate innovatively designed phase- diagram features (24) 
with traditional Hume- Rothery and thermodynamic features (26), 
and are enhanced by feature engineering for improved accuracy. 
Trained on a database of ~ 1000 HEAs and comprehensively vali-
dated by experiments, the ML models can predict nine phases with 
around 90% accuracy. Our targeted phases allow a solid- solution 
matrix and strengthening B2 phase in an as- cast condition, poten-
tially exhibiting ductility, as predicted by subsequent ML mechani-
cal property prediction models. Notably, while face- centered- cubic 
(FCC) and hexagonal close- packed (HCP) phases are permissible, 
they have not been predicted by ML to form in our Al- enriched 
RHEAs. Meanwhile, we aim to circumvent noncubic Laves and 
Sigma phases, which can embrittle the alloy due to the precipitate- 
matrix strain incompatibility, acting as stress concentrators and 
promoting crack initiation and propagation and leading to alloy 
early failure (11, 13, 14). In addition, despite the Heusler phase’s po-
tential as a coherent strengthening phase in alloys with FCC matri-
ces (18), its relevance is limited in Al- RHEAs due to the absence of 
an FCC matrix and will be avoided.
Predictions of mechanical properties, such as compressive yield 
strength, σYS, and fracture strain, εf , are conducted with ML models. 
Additional properties, including melting temperature, Tmelt (Eq. 9), 
density, ρ (Eq. 10), and Poisson’ s ratio, ν (table S1), are determined 
through separate calculations. The ML mechanical property prediction 
models select the optimal feature combinations by a genetic algorithm 
(GA) (27) (details in Methods) from a total of 16 initial physics- based 
features (table S1), with some computed by the effective medium calcu-
lation (EMC) method (28) to reduce the computational burden while 
maintaining fidelity to experimental or DFT- calculated values. The 
EMC’s effectiveness is exemplified in the D- parameter calculation (29) 
(detailed in Methods), whose DFT- calculated values show a direct cor-
relation with the BCC HEAs’ εf (29, 30). The EMC- computed D pa-
rameter is well aligned with the DFT- calculated values (29) with a mere 
5% absolute mean error (Fig. 2A), demonstrating a fast and reliable al-
ternate calculation for high- throughput and ICME applications.
Most current ML- based mechanical property models are tailored to 
specific HEA phases to enhance prediction accuracies by focusing on 
phase- specific properties controlling mechanisms. The ICME- designed 
Fig. 1. Schematic diagram showing the Al- RHEAs design process. the abbreviations icMe, Ml, vec, and DFt denote integrated computational material engineering, 
machine learning, valence electron count, and density functional theory, respectively.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 3

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
3 of 14
Al- RHEAs predominantly form an Al- X- Y B2 phase (22). However, 
owing to the limited mechanical properties data available for B2 Al- 
RHEAs, we alternatively develop a baseline ML model using more 
abundant disordered BCC RHEAs and Al- RHEAs. Because the B2 
phase’s LRO can introduce ordering- strengthening, enhancing strength, 
and reducing ductility (29, 31), the baseline ML model based on BCC 
HEAs might underestimate strength and overestimate the ductility of 
B2 HEAs. Our goal is to identify Al- RHEAs with inherent ductility pre-
dicted in their BCC phase, as brittle BCC Al- RHEAs are unlikely to 
manifest ductility upon the formation of B2- LRO. Furthermore, 30% of 
the ML training database consists of HEAs with 3 to 20 atomic % (at %) 
Al. This Al inclusion highlights that the strengthening effect from po-
tent Al- refractory elements bonds has been inherently considered. 
With the synchronized refinement of both ML algorithms and feature 
combinations, as elaborated in Methods, the model achieved a root 
mean square error (RMSE) of 159 MPa for σYS, alongside a notable 
alignment between the predicted and measured values, shown in Fig. 
2B. The prediction of compressive εf exhibits a moderate RMSE of 8.2% 
(Fig. 2C), comparable to the leading results in similar prediction tasks 
(32). In these ML models, the prediction of εf is challenging primarily 
due to the database noise, where factors, such as sample defects (e.g., 
pores) and processing conditions (e.g., cooling rate and solidification 
direction), can greatly affect the εf . It is important to note that certain 
compression tests were terminated at 50% in instances where samples 
did not fracture (solid red data point in Fig. 2C). Alloys demonstrating 
high plasticity under these conditions were incorporated into the ML 
training to broaden the models’ application scope. Last, with the two 
baseline ML models built with BCC alloys and the data challenge 
mentioned, we are not ambitious in obtaining precise alloy proper-
ties’ predictions on B2 Al- RHEAs. The current models for σYS and εf 
exhibiting high and moderate accuracies, respectively, adequately direct 
us toward optimal compositional regions. These regions are then sub-
ject to further first- principles and experimental analyses and optimiza-
tions for the design of high- performance Al- RHEAs.
As depicted in Fig. 1, the ICME model begins with 84 equimolar 
quaternary Al- RHEAs by combining Al with any three refractory 
elements. The top five systems forming the B2 phase without other 
undesired IM, and showing the highest scores (Eq. 1), indicating the 
best overall properties, are listed in Fig. 2D (full list in table S4). 
Al25Hf25Nb25Ti25 emerges as the leading candidate exhibiting the 
best comprehensive performance, with the highest predicted εf 
(27%) and an intermediate σYS (1206 MPa) among all evaluated qua-
ternary Al- RHEA systems assuming the absence of B2- LRO. Such 
plasticity surpasses many existing Al- RHEAs. However, the induc-
tion of B2- LRO is anticipated to reduce plasticity while enhancing 
strength. With Hf also known to enhance grain- boundary adhesion 
(33), Al25Hf25Nb25Ti25, is chosen for initial experimental examina-
tion. Subsequent composition adjustments for property optimiza-
tion will be guided by experiments and MC studies.
MC- guided experimental optimization of Al- RHEAs
Al25Hf25Nb25Ti25
The x- ray diffraction (XRD) and scanning electron microscopy 
(SEM) characterizations of the initial composition, Al25Hf25Nb25Ti25 
in the as- cast condition, show the single–B2- phase formation (Fig. 3, 
A and B). This alloy exhibits high strength, with a compressive 
Fig. 2. ML mechanical property prediction models’ performances and prediction results. (A) comparison of D- parameter values calculated using DFt and eMc. the 
eMc method demonstrates a promising agreement with DFt results, yielding an absolute mean error of 5% and validating its potential for the efficient estimation of the 
D parameter. (B) the comparison between the compressive yield strengths, σYS, as predicted by Ml and measured from experiments for Bcc heAs, with an RMSe value of 
159 MPa. (C) the comparison between the compressive fracture strain, εf , as predicted by Ml and measured from experiments for Bcc heAs, with an RMSe value of 8.2%. 
the solid red data points on the right side of the figure indicate instances where compression tests terminated at a 50% strain without fracture. (D) the top five equimolar 
quaternary Al- RheAs, predicted to form B2 phases without other iM. their predicted properties, including σYS (yield strength), εf (fracture strain), Tmelt (melting tempera-
ture), and ν (Poisson’s ratio), along with their respective scores (details in Methods), are also presented.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 4

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
4 of 14
Fig. 3. Microstructures and phases for Al- RHEAs in the present work. (A) XRD patterns for Al25hf25nb25ti25, Al20hf24nb29ti27, Al15hf25nb32ti28, and Al10hf20nb22ti33v33 
in the as- cast condition. Peaks corresponding to the disordered Bcc phase or B2 phase are labeled with their (hkl) indices in black or red color. For Al 15hf25nb32ti28, the 
insets provide higher- magnification views of the (111) and (210) superlattice diffraction peaks for the B2 phase. a.u., arbitrary units. (B to E) SeM backscattered electron 
(BSe) images for four alloys in the as- cast condition. B2- phase grains can be observed. insets are the SAeD showing B2- lRO. Additional SAeD patterns for the four alloys, 
obtained from various regions of the samples, are presented in fig. S6. (F and G) teM dark- field images for the B2 phase with an antiphase boundary (APB) in the as- cast 
Al20hf24nb29ti27. (H and J) Scanning transmission electron microscopy (SteM) high- angle annular dark- field (hAADF) image for Al 20hf24nb29ti27 along the [001] zone 
axis. the intensity profile along the red arrow, spanning nine atoms, reveals periodic variation consistent with B2 ordering. (I and K ) SteM- hAADF image for the 
Al10hf20nb22ti33v33 along the [001] zone axis, showing minimal variation in atomic intensity profiles due to the weak B2- lRO.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 5

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
5 of 14
σYS ~ 1.7 GPa, but lower εf ~ 2% (Fig. 4A). The alloy exhibits strong 
B2- LRO, as indicated by the pronounced (100) su perlattice XRD 
diffraction peak (Fig. 3A). This extensive LRO could substantially 
hinder dislocation movement, resulting in a higher strength but de-
creased plasticity, compared to the values (Fig. 2D) predicted as-
suming a disordered BCC phase forms.
Metropolis MC simulations (20,  34) (details in Methods) were 
conducted to study the LRO, the B2 order- disorder transition during 
solidification, and the atomic sublattice occupancy. Al25Hf25Nb25Ti25 
shows pronounced B2- LRO (Fig. 5A, LRO spans between 0 and 1, 
representing disordering and ordering) and atomic order parame-
ters, LROi (Fig. 5C, LRO i spans between − 1 and 1, with 0 and ±1 
representing disordering and ordering), with the order- disorder 
transformation temperature, Ttransform ~ 2000 K, slightly below the 
predicted melting temperature of Tmelt ~ 2108 K by Eq. 9. Given that 
phase transformation and evolution in as- cast HEAs continue below 
Tmelt due to high atomic kinetic energy [such a rapid phase transition 
may cease around 0.8 Tmelt (24)], substantial B2- LRO can be devel-
oped in Al25Hf25Nb25Ti25 below the Tmelt. Here, we present a semi-
quantitative estimation of the LRO experimentally established in the 
alloy, relative to the theoretically most ordered reference state at 
0 K. Specifically, the XRD patterns for the most ordered reference state 
were simulated using the MC structure at 0 K, and were subsequently 
compared with the experimentally measured XRD patterns, as de -
tailed in Methods and Eq. 8. The LRO established in Al25Hf25Nb25Ti25 
is estimated to be ~100% of the reference state. This estimation may 
suggest that a high Ttransform does exist near the Tmelt as described 
earlier, facilitating LRO development. Figure 5C shows that Al and 
(Hf, Ti) predominantly settle to different B2 sublattices, with Nb 
exhibiting little inclination. The site- occupancy tendency is also evi-
dent in Fig. 5G, with Al- Ti and Al- Hf being the primary nearest- 
neighbor pair around Al, Hf, and Ti. Self- pairs are less prevalent in 
all nearest- neighbor pairs. Such site occupancy can be attributed to 
the binary atomic interaction energies, H ij, listed in table S5, where 
Al- Hf and Al- Ti pairs exhibit the lowest H ij, indicative of more stable 
bonding. Figure 5H, which shows the MC superlattice configura-
tions at 2000, 1800, and 500 K, further il lustrates the BCC- to- B2 
transition. Al gradually segregates to the α sublattice, while Hf and Ti 
segregates to the β sublattice as temperature decreases. These MC- 
discovered site- occupancy preferences have been validated in similar 
systems like Ti2AlHf (35) and AlNbTiV (36), by using DFT, ML, MC 
simulations, and experiments (11).
Using MC- simulated supercell structures, ab initio relaxation is 
used on Al25Hf25Nb25Ti25 (Fig. 6, A to C) to elucidate their thermo-
dynamic phase stability at temperatures of 300, 1373, and 2000 K, 
corresponding to scenarios wherein LRO is either fully established, 
partially present, or absent, respectively. The calculated relaxation 
energies (ΔE) are positive, relative to the convex hull of enthalpies 
within the Al- Hf- Nb- Ti system, confirming that they are thermody-
namically (but not dynamically) unstable to phase separation. 
Moreover, the decrease in quenched (0 K) ΔE from 126 meV per 
atom following 2000 K annealing down to 76 meV per atom follow-
ing 300 K annealing demonstrates the increasing thermodynamic 
stability resulting from increasing chemical order. To assess the dy-
namic stability of the B2 structure, AIMD relaxations (Fig. 6, D to F) 
were conducted, wherein the Al 25Hf25Nb25Ti25 structures were 
quenched from temperatures of 300, 1373, and 2000 K down to 
300 K. The observed lattice distortions < |ΔR|> were of moderate 
magnitude, indicating the dynamic stability of the B2 phase after 
quenching. The extent of distortions is comparable to the Al- free 
RHEAs that span groups IV and V of the periodic table (37). The 
decreasing <|ΔR|> with decreasing annealing temperature suggests 
that LRO can reduce the lattice distortion.
The high B2- LRO substantially decreases the plasticity from the 
predicted εf value. Understanding the influence of each element on 
LRO is essential for the subsequent composition adjustment. There-
fore, each element in Al 25Hf25Nb25Ti25 was systematically reduced 
to 20 at %, generating compositions of Al20(Hf26.7Nb26.7Ti26.6), Hf20
(Al26.7Nb26.7Ti26.6), Nb20(Al26.7Hf26.7Ti26.6), and Ti20(Al26.7Hf26.7Nb26.6), 
referred to as Al20, Hf20, Nb20, and Ti20, respectively, in Fig. 5B. Ttransform 
and the B2- LRO at specific reference temperatures (1500 K as an 
example) are calculated. Decreasing the Al content lowers both 
Ttransform and the B2- LRO. Conversely, reducing Hf, Nb, or Ti raises 
Ttransform and LRO, likely due to the resultant increase in the Al con-
tent. This trend suggests that decreasing the Al content could be a 
strategy to lower B2- LRO and enhance ductility/plasticity. Addi-
tional heat treatment of Al25Hf25Nb25Ti25 also reveals a tendency of 
Laves- phase formation above 700°C (fig. S1). This phase transfor -
mation does not contradict the ICME phase prediction of a single 
B2 formation, which is predicted for the as- cast condition. The B2 
region in the as- annealed samples has an energy dispersive spec-
troscopy (EDS)–determined composition of Al20Hf24Nb29Ti27 (fig. S1). 
Given its thermal stability and reduced Al content, this B2 composi-
tion is chosen for a more detailed study.
Al20Hf24Nb29Ti27
The as- cast Al20Hf24Nb29Ti27 shows a single B2 phase from XRD and 
SEM characterizations in Fig. 3 (A and C). Transmission electron mi-
croscopy (TEM) investigations (Fig. 3, F and G) present the antiphase 
boundaries, with the selected area electron diffraction (SAED, inset 
of Fig. 3C), confirming the B2- LRO. Compression testing of Al20Hf24 
Nb29Ti27 (Fig. 4A) exhibits a σYS of 1.6 GPa, an ultimate strength of 
2.4 GPa, and a notable εf of 35%. Al20Hf24Nb29Ti27 exhibits weakened 
B2- LRO than Al 25Hf25Nb25Ti25, indicated by the less intense XRD 
superlattice diffractions and the MC studies in Fig. 5 (A and D). The 
MC- computed Ttransform of ~1600 K is close to 0.8 Tmelt where a rapid 
phase transition still exists, allowing for substantial B2- LRO develop-
ment. It is estimated that ~85% (Eq. 8) of the LRO for the reference 
state at 0 K is established. Al and (Hf,Ti) continue their sublattice 
segregation (Fig. 5D and fig. S2). Scanning transmission electron mi-
croscopy (STEM) high- angle annular dark- field (HAADF) images in 
Fig. 3 (H and J) also reveal the distinct periodic variations in the in-
tensity profile for Al20Hf24Nb29Ti27, consistent with B2 ordering. These 
periodic variations are more clearly visible in the lower- magnification 
STEM- HAADF image shown in fig. S7. Al20Hf24Nb29Ti27 exhibits a 
substantial εf improvement, about 16 times that of Al25Hf25Nb25Ti25, 
with nearly unchanged σYS. This feature improved plasticity, which 
could be attributed to the moderated B2- LRO, facilitating plastic de-
formation through the glide of either <111> or a/2 <111> disloca-
tions ( 38). The LRO decrease does not notably affect the overall 
strength. Next, a further Al reduction, as in Al 15Hf25Nb32Ti28 with 
other elemental contents increased accordingly, may decrease the 
LRO and facilitate plasticity increase.
Al15Hf25Nb32Ti28
The as- cast Al 15Hf25Nb32Ti28 exhibits a single B2 phase (Fig. 3D) 
with weak B2- LRO indicated by the magnified B2- (111) and (210) 
peak in the inset of Fig. 3A. TEM- SAED (Fig. 3H) further confirms 
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 6

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science A D v A nce S | Re S e AR ch A R ticle
6 of 14
Fig. 4. The mechanical properties of Al- RHEAs in the present work. (A) Representative compression engineering stress- strain curves for the as- cast Al25hf25nb25ti25, 
Al20hf24nb29ti27, Al15hf25nb32ti28, and Al10hf20nb22ti33v33. tests terminated with the sample fractured are labeled by crosses, while circles represent nonfractured sam-
ples. (B) Representative tensile engineering stress- strain curves for the as- cast Al10hf20nb22ti33v33. (C) comparison of the compressive yield stress and fracture strain among 
heAs in different categories; 3D represents heAs with only 3D- transition metals. RheAs denote heAs with only refractory elements. Al+ represents the inclusion of Al. the two 
alloys in the present work with high toughness are highlighted with yellow oval. (D) SeM images showing the ductile fracture surfaces of an Al10hf20nb22ti33v33 tensile test 
specimen. (E) teM image of the 4% plastic- strained Al10hf20nb22ti33v33 sample, showing discrete long curved dislocations. the vertical boundary in the image results from 
the stitching of two teM images. (F) teM image of the 10% plastic- strained Al10hf20nb22ti33v33 sample, where multiple slip systems are observed, with the corresponding 
slip bands intersecting each other. (G) high- temperature compression test showing the variation of the compressive yield strength against test temperature for the Al10h-
f20nb22ti33v33.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 7

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
7 of 14
Fig. 5. Metropolis MC simulation results for Al- RHEAs. (A) variation of lRO of the B2 phase under different temperatures in the four alloys: Al25hf25nb25ti25, Al20hf24nb29ti27, 
Al15hf25nb32ti28, and Al10hf20nb22ti33v15 represented by black, red, blue, and green lines, respectively. lRO spans between 0 and 1, representing disordering and ordering. 
the temperatures where B2- lRO disappears are labeled. (B) variation of B2- ordering transformation temperature, Ttransform, and B2- lRO at 1500 K with different composi-
tions. Al20, hf20, nb20, and ti20 represent Al20(hf26.7nb26.7ti26.6), hf20(Al26.7nb26.7ti26.6), nb20(Al26.7hf26.7ti26.6), and ti20(Al26.7hf26.7nb26.6), respectively. error bars are from the 
SDs of five rounds of Mc calculations. (C to F) variation of atomic order parameters, lRO i, under different temperatures for Al25hf25nb25ti25, Al20hf24nb29ti27, Al15hf25n-
b32ti28, and Al10hf20nb22ti33v15. lROi spans between −1 and 1, with 0 and ±1 denoting disordering and ordering, respectively. (G) variation of nearest- neighbor pair for 
different elements under various temperatures for Al25hf25nb25ti25. (H) the atomic configurations of the Mc- simulated superlattices at temperatures of 2000, 1800, and 
500 K, illustrating the transition from the disordered Bcc (A2 phase) to partially ordered, and fully ordered B2 within the Al25hf25nb25ti25 system. two small cubes at each 
temperature denote the α and β sublattices of the B2- lattice structure, showing the sublattice elemental segregation tendency.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 8

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
8 of 14
the B2- LRO. The compression test (Fig. 4A) exhibits a σYS of 1.5 GPa. 
Notably, the samples endured up to a 50% height reduction 
without fracture before the test termination, demonstrating excep-
tional plasticity.
Compared to Al 25Hf25Nb25Ti25 and Al 20Hf24Nb29Ti27, Al 15Hf25 
Nb32Ti28 experiences a marginal σYS reduction by ~ 10%, but a no-
table εf increase. Concurrently, B2- LRO is further weakened to be 
nearly XRD undetectable, suggesting that LRO exerts a more pro -
nounced effect on plasticity rather than strength. The MC studies 
in Fig. 5 (A and E) show a T transform of ~1150 K, around half of the 
predicted Tmelt of ~2208 K. The limited atomic mobility and diffu -
sion at T transform lead to only a minimal LRO establishment, esti -
mated to be ~33% of the reference state at 0 K.
Al10Hf20Nb22Ti33V15
We demonstrated that an Al reduction in the AlHfNbTi system re-
duces B2- LRO, improving plasticity and slightly reducing strength. 
While pursuing a further Al reduction, we also explored partially 
substituting Hf with V . Vanadium has a high Poisson’s ratio among 
the refractory elements, and with benefits of lower density and cost. 
The inclusion of V is predicted to maintain a single B2 phase. In ad-
dition, vanadium exhibits a moderate binary mixing enthalpy with 
Al (table S5), suggesting a potential substitution of strong Al- Hf 
bonds with weaker Al- V bonds, which may contribute further to the 
reduction of LRO. This strategic compositional modification has re-
sulted in the development of Al 10Hf20Nb22Ti33V15, a stable single 
B2- phase alloy exhibiting both compression plasticity and tensile 
ductility.
The XRD and SEM characterizations (Fig. 3, A and E) reveal a 
single phase, and the B2- LRO is observable in the TEM- SAED (inset 
of Fig. 3E and fig. S6). The compression test (Fig. 4A) yields a σYS of 
1.2 GPa, with no fracture up to 50% height reduction, aligning with 
the reduced B2- LRO leading to lower strength but more plasticity. 
High- temperature compression tests (Fig. 4G) maintain σYS above 
800 MPa at 700°C, with a rapid strength decline around 800°C. The 
tensile test (Fig. 4B) exhibits a σYS of 1.0 GPa and εf of 9%, with ten-
sile fracture surfaces (Fig. 4D) further substantiating the ductility. 
Herein, to the best knowledge of the authors, the current alloy is the 
first instance of a single B2 phase Al- RHEA alloy exhibiting 9% ten-
sile ductility in the as- cast condition. While several disordered BCC 
RHEAs with excellent ductility (10 to 20%) have been reported in 
recent years (2), our findings challenge the assumption that B2 LRO 
inherently compromises ductility, thereby making the observed ten-
sile ductility in a single B2 Al- RHEA a notable achievement. Contin-
ued research efforts into mechanical and thermal treatments are 
anticipated to refine the microstructure and further enhance the 
ductility of the alloy, though such investigations fall beyond the 
scope of this article and will not be further discussed. Further TEM 
analysis was performed at 4 and 10% strains. At a 4% strain (Fig. 4E), 
discrete long dislocations with the curved morphology are observed. 
Such morphology likely indicates dislocation pinning resulting from 
the chemical ordering of the B2 phase, which contrasts with the 
Fig. 6. Supercells of Al25Hf25Nb25Ti25 after ab initio relaxation and AIMD simulations. (A to C) Ab initio relaxation of Al 25hf25nb25ti25, starting from Mc- determined 
supercell at (A) 300 K, (B) 1373 K, and (c) 2000 K. (D to F) AiMD simulations for the Al25hf25nb25ti25 at 300 K, quenched from an Mc- determined supercell (D) at 300 K, (e) 
1373 K, and (F) 2000 K. the axes represent the cartesian coordinates of each atom in angstroms. the atoms size indicates their vertical height. the calculated relaxed lattice 
distortions, <|ΔR| > (defined in the Methods section), and the relaxed energies, ΔE, are included for each structure.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 9

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
9 of 14
typical straight dislocations commonly seen in BCC RHEAs (39). At 
a 10% strain (Fig. 4F), there is a noticeable increase in dislocation 
density and dislocation- dislocation interaction. Multiple slip sys-
tems along <111> are activated, with intersecting slip bands (white 
arrows) and frequent dislocation tangles (yellow arrows). The activa-
tion of multiple slip systems is hypothesized to contribute to the high 
plasticity/ductility observed in these alloys.
In addition, what captures our attention is the relatively low strain 
hardening in the tensile plastic region (Fig. 4B). A hypothesis for this 
phenomenon is that an intriguing yet often overlooked factor influ-
encing the disordered BCC- B2 transformation is strain or deforma-
tion. For example, a 50% compression reduction in AlNbTiVZr 0.5 
results in the loss of B2 LRO and a B2- to- disordered BCC transfor-
mation (11). Systems with lower LRO are more prone to such trans-
formations (11). Deformation processes, including dislocation glide, 
annihilation, and recovery, can alter atomic arrangements and dis-
rupt long- range atomic ordering (40). In our alloy, it is likely that as 
soon as the material enters the plastic region, the formation and 
movement of dislocations reduce the LRO. This reduction in LRO 
would inevitably diminish the LRO- strengthening effect, making 
subsequent dislocation movement easier and reducing the strain- 
hardening effect. This hypothesis presents an intriguing mechanism 
for balancing strength and ductility: Before permanent damage oc-
curs, the B2 LRO provides a higher yield stress. However, once the 
material undergoes permanent plastic deformation, the automatic 
reduction in B2 LRO could help prevent early failure, as seen in most 
strong but brittle materials. However, such plausible emphasis needs 
experimental verification, such as the in situ neutron diffraction.
The MC results (Fig. 5, A and F) show a Ttransform of ~750 K, 
markedly below the predicted T melt of ~ 2058 K. Nonetheless, the 
Al10Hf20Nb22Ti33V15 manifests a faint B2 ordering, likely attributable 
to the restrained yet present atomic mobility around Ttransform. Such a 
faint B2 LRO is obscured by the XRD background noise and can only 
be resolved by TEM. Correspondingly, STEM- HAADF images in 
Fig. 3 (I and K) exhibit minimal atom intensity variation. The unob-
servable and observable weak B2 ordering noted in the two methods 
(XRD and TEM) can be attributed to the difference in scattering factors 
using x- ray and electron beam. An MC study shows that Al and Hf 
segregate to different sublattices, while the Nb and V exhibit weak 
superlattice occupancy tendencies when cooling to slightly below 
Ttransform (~750 K, Fig. 5F). A further temperature decline below 500 K 
leads to pronounced elemental segregation driven by the nominal 
impact of entropy. However, this low- temperature region is less im-
portant as achieving the MC- predicted equilibrium state is nearly 
impossible given the exceptionally sluggish atomic diffusion.
Comparative study of Al- RHEAs’ mechanical properties
Around 200 HEAs are compared for compressive σYS and εf in Fig. 
4D, with the red line highlighting the trend of increased strength 
with decreased plasticity. Most Al- RHEAs exhibit limited plasticity, 
potentially due to the alloy’s inherent brittleness (41), as elaborated 
in the next section; strong Al- induced B2- LRO; and brittle IM for-
mation (11, 13). However, Al- RHEAs designed in the present work 
diverge from this norm, achieving both high strength and plasticity/
ductility. These ICME- designed Al- RHEAs exhibit inherent ductility 
and avoid brittle IM formation. Subsequent experimental MC hybrid 
optimizations are applied to adjust the LRO, thereby enhancing the 
plasticity/ductility of the alloy without compromising its strength.
VEC valley of metal brittleness and DFT analysis
During the ICME ML training process, we identified an intriguing 
correlation between VEC (21) and HEA plasticity. Figure 7A shows 
a “VEC valley” of brittleness between 5.5 and 6.2 in graph plotting 
compressive σYS against VEC. This valley is not attributed to data 
deficiency, as we specifically targeted HEAs in this VEC range. Previous 
ML studies (42, 43) have recognized the strong VEC- plasticity/ductility 
correlations, and the D parameter, known to indicate plasticity/ductility, 
also correlates with VEC (29,  30). Notably, our Al- RHEAs are con-
sistently located in the lower- VEC regions, outside the valley, where 
high- plasticity/ductility HEAs are typically found.
Empirical studies (21) suggest a “spectrum” of the VEC- HEA 
phase formation, where VEC < 6 favors BCC formation, 6 < VEC < 7.8 
leads to a mixed FCC- BCC phase, and VEC  > 7.8 leads to a single 
FCC phase. The range, 6.88  < VEC  < 7.84, tends to form brittle 
Fig. 7. The VEC valley for alloy brittleness and its DFT explanation. (A) comparison of the compressive fracture strain and vec among heAs in different categories. in 
both figures, 3D represents heAs with only 3D- transition metals. RheAs denote heAs with only refractory elements. Al+ represents the inclusion of Al. the four alloys in 
the current work are highlighted by the star symbol. (B) the DOS of Mo (black line) showing the variation of D /parenleft.s1EF
/parenright.s1 with respect to the vec in a rigid- band model. Plotting 
symbols are placed at energies corresponding to vecs of the periodic table columns 4 to 8 ( ti- Fe columns). the Fermi energy for vec = 6 is set to zero. the brittle region 
(5.5 < vec < 6.2) is shaded. the crystal orbital hamiltonian population (cOhP) (50) is plotted in the red curve. the negative and positive cOhP values indicate bonding and 
antibonding states, respectively.
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 10

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
10 of 14
topologically close- packed (TCP) phases (e.g., Laves and Sigma) 
(44). The VEC valley resides near the higher BCC and mixed FCC- 
BCC regions, close to the brittle TCP region. To the right of the 
valley, HEAs typically form ductile FCC phases, while to the left, 
they form ductile BCC phases. A decreasing VEC lowers the Fermi 
level in the band structure, leading to an earlier occurrence of the 
critical strain for shear instability and thus inherently enhancing 
the plasticity/ductility (41). Therefore, the VEC valley only occupies 
the higher end of the BCC region.
Beyond these reasons, a more in- depth, quantitative analysis is 
critical for deciphering the fundamental mechanisms that underpin 
this phenomenon, and DFT was applied to provide more insight. Prior 
studies (45, 46) suggest that the Fermi level density of states, D /parenleft.s1EF
/parenright.s1, 
correlates with plasticity/ductility due to the strength of metallic bond-
ing relative to ionic and covalent bonds. Other work has linked high 
plasticity/ductility to incipient shear instabilities governed by the prox-
imity of the Fermi level to topologically unstable energy- band crossings 
(47, 48). Electronic- structure effects may thus help explain the non-
monotonic variation of fracture strain with respect to VEC. Figure 7B 
presents D(E) for a representative refractory metal, BCC Mo, with 
VEC = 6 at the center of the experimental region of interest. The pro-
nounced pseudogap around the Fermi level at EF = 0 is caused by the 
Eg − T2g splitting at the Γ k- point with the Mo d- band half- filled in its 
standard electron configuration, 5s14d5. In a rigid band model (49), we 
may assume that D(E) for the alloys under study qualitatively resem-
bles that of Mo, with the chief difference (other than the possible 
magnetism) being the placement of the Fermi level, which grows 
monotonically with VEC. The VEC valley for brittleness (Fig. 7B) 
roughly coincides with the region of relatively low D /parenleft.s1EF
/parenright.s1. Moreover, as 
demonstrated by the crystal orbital Hamilton population (COHP , 
Fig. 7B) (50), the Eg − T2g split that creates the deep pseudogap sepa-
rates occupied bonding states (negative COHP) from antibonding 
(positive COHP). The Fermi level for Mo lies in this gap, and thus the 
valley represents the maximum degree of covalency in the bonding. 
Covalent bonds create strong shear moduli that lower the Poisson ratio, 
contributing to brittleness. Besides, the Thomas- Fermi screening length 
varies as 1/
/uni221A.s1
D /parenleft.s1EF
/parenright.s1. Therefore, a low D /parenleft.s1EF
/parenright.s1 corresponds to a large 
screening length. Al- transition metal alloys are subject to strong charge 
transfer that, together with the large screening length, makes the bond-
ing more ionic in character. Last, we want to remind the reader that the 
avoidance of the VEC valley is potentially a necessary condition, but 
not a sufficient condition for locating ductile HEAs. As can be seen 
from Fig. 7A, many HEAs outside the VEC valley still exhibit low duc-
tility due to factors, such as unfavored IM formation.
In addition, we calculated the D /parenleft.s1EF
/parenright.s1 for the alloys in this study 
using MC supercells at 500 K and 2500 K (Table 1), corresponding 
to ordered and disordered atomic distributions, respectively. The 
DFT explanations for the VEC valley of brittleness are again appli-
cable: The steadily decreasing D /parenleft.s1EF
/parenright.s1 values with increasing Al con-
tent seem to suggest a correlation with plasticity, as discovered in 
other metallic systems (45). The B2 ordering appears to have mini-
mal impact on the D /parenleft.s1EF
/parenright.s1, except in the case of Al 25Hf25Nb25Ti25. 
This is likely because all alloys in this study are substantially distant 
from the 50% of the Al fraction, where strong pseudogaps are typi-
cally observed in alloys containing late transition metals, such as 
Al- Mn through Al- Ni (51).
DISCUSSION
HEAs offer a remarkable latitude in designing alloys with multiple 
promising properties. This potential, however, brings the complex 
challenge of systematically exploring the HEA compositional space 
for optimal compositions suitable for various applications. The past 
decade has witnessed a surge in the HEA- phase prediction research 
(26), and recognized ML and CALPAHD as ideal computational 
tools for high- throughput computation. Concurrently, many models 
for predicting properties emerged with high accuracies (42, 43, 52), 
paving the way for the inception of all- encompassing ICME HEA 
design models. The discovery of the strong, yet ductile Al- RHEAs 
epitomizes a refined template model, and the ICME framework and 
submodels can be customized accordingly to divergent design 
objectives. While ICME effectively identifies promising composi-
tional zones, it is ambitious to rely on it alone in a multiobjective 
quest to determine the optimal composition. As shown with the 
AlHfNbTi(V) system, fine- tuning the composition necessitates 
deeper theoretical analysis, such as MC and DFT, complemented by 
experimental validation and refinement.
To review the AlHfNbTi(V) system, four B2 Al- RHEAs were de-
signed with plasticity primarily determined by B2- LRO and adjustable 
through the Al content. MC studies suggest that the LRO may also be 
modulated through specific thermal treatments, tailoring ductility 
for specific applications. Notably, AlHfNbTi(V) alloys demonstrate 
toughness surpassing most extant HEAs, with the Al incorporation ef-
fectively reducing cost and density while enhancing oxidation resis-
tance, positioning this system as promising for continued optimization 
and research.
Regarding the fundamental mechanism of the VEC- plasticity 
correlation, first- principles calculations have elucidated an elec-
tronic origin of the VEC valley. A more in- depth investigation is 
imperative, propelling the field toward an enriched understanding 
of electronic structure effects on alloy ductility. Concurrently, stra-
tegically avoiding the VEC valley is advised in designing future 
ductile alloys.
Table 1. D (EF) calculated using the MC structure at 500 and 1500 K for alloys in the present work. 
Composition D /parenleft.s1EF
/parenright.s1—500 K (states per electron volt per atom) D /parenleft.s1EF
/parenright.s1—2500 K (states per electron volt per atom)
 Al10hf20nb22ti33v15 1.36 1.34
 Al15hf25nb32ti28 1.21 1.20
 Al20hf24nb29ti27 1.13 1.15
 Al25hf25nb25ti25 1.00 1.10
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 11

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
11 of 14
Moving ahead, we envision this innovative alloy- design strat-
egy as a blueprint for designing alloys with structural applica-
tions. We also aim to deepen understanding of the elemental 
role in the atomic ordering and mechanical properties in HEAs 
and explore VEC- centric compositional tuning to overcome brit-
tleness, thereby perfecting the approach and enriching the theo-
retical framework.
METHODS
EMCs of D parameter
The D parameter quantifies the ratio between the surface energy as-
sociated with the cleavage fracture ( γsf ) and the energy associated 
with the unstable stacking fault (γusf ) (29). A distinct correlation has 
been observed between the compression fracture strain and the 
DFT- calculated D parameter for BCC HEAs (29) because it has 
been postulated that the ductility of BCC alloys is influenced by the 
interplay between the dislocation emission and cleavage- fracture 
propagation in the vicinity of a crack tip (30). Despite its impor -
tance, the D parameter computed by DFT is computationally expen-
sive and not suitable for high- throughput simulations. Alternatively, 
in our effective medium method (28), the D parameter is calculated 
by considering the values of surface energies and unstable stacking 
fault energies along the same atomic planes and dislocation direc-
tions for each constituent element with the equation and details 
listed in table S1.
ML mechanical properties and phase- formation 
prediction model
The ML mechanical property prediction database includes 272 com-
pressive yield strength (σYS) and 157 compressive fracture strain (εf ) 
measurements measured at both ambient temperature and elevated 
temperatures up to 1600°C. The complete ML feature set is listed in 
table S1, where the T test/Tmelt feature, the testing temperature rela-
tive to melting temperature, highlights the effect of testing tempera-
ture on material properties. Feature selection will be refined from 
this set. Several ML algorithms, including the support vector regres-
sor, random forest regressor (RFR), K- nearest neighbor, and linear 
regression, were applied to the σYS and εf datasets, using the Python’ s 
scikit- learn library. The GA (27) (GA parameters in table S3) was 
used for the optimal feature selection from the complete feature set 
(table S1). The GA process used the 10- fold cross- validation for 
overfitting avoidance and GridSearchCV() for hyperparameter opti-
mization, identifying RFR as the best algorithm for both σYS and εf 
predictions with the lowest prediction RMSE. The GA- determined 
optimal feature combinations are included in table S2.
The ML- phase formation prediction models are detailed in our 
prior work (24, 25).
ICME alloy system selection
Of the 84 equimolar quaternary Al- RHEAs, 16 Al- RHEAs systems 
are screened out by the ML prediction of forming the B2 phase with-
out other IMs. These systems are then predicted for the compressive 
σYS, εf , Tmelt (Eq. 9), and ν (equation in table S1). Three heavier Al- 
RHEAs, with ρ exceeding 10 g/cm3, are excluded due to their nota-
bly higher density, compared to Ni- and Co- based superalloys. The 
predicted property values for each system are summarized in table 
S4. Each alloy is scored using
where p i represents the predicted value of the i th property for the 
alloy, p i−best and p i−range are, respectively, the best value (i.e., the highest 
εf , σYS, Tmelt, and ν) and the range for the ith property among all the 
candidates. A higher score represents a better overall performance.
Experiment methods
High- purity raw elements (>99.99 wt %) were arc melted in a water- 
cooled copper crucible using a 400- A current. Each melt lasted 30 s, 
with at least five melts performed to ensure chemical homogeneity, 
and the ingots were flipped between each melt. The ingots were later 
polished for XRD and SEM analysis. Parts of the ingots were also 
suction- cast into copper molds to produce a rod- shaped sample 
(3 mm diameter and 10 mm height) for compression testing and 
TEM sample preparation.
The XRD/SEM samples were polished down to a grit size of 1 μm 
with diamond suspension and finished with a 0.06- μm colloidal 
silica suspension. The TEM samples were sliced from the suction- 
cast rod with a thickness of 500 μm. These thin slices were further 
polished to a thickness below 100 μm, followed by electron polish-
ing to create TEM transparent regions for imaging.
The XRD measurements were conducted on the polished sample 
by a PANalytical Empyrean diffractometer with Cu Kα radiation 
and a scanning rate of approximately 0.15 degrees/s. The SEM char-
acterization was conducted on an FEI Quanta 650 equipped with 
EDS. The TEM analysis was performed, using an FEI Titan Trans-
mission Electron Microscope and a Thermo Scientific Spectra 
300 (S)TEM with an accelerating voltage of 200 kV .
Cylindrical samples with a diameter of 3 mm and a gauge length 
of 6 mm were used for compression testing. Compression tests were 
performed on a computer- controlled, uniaxial- mechanical testing 
system (an MTS servo- hydraulic load frame) with an initial strain 
rate of 1 × 10−3 s−1. The load and displacement values of the testing 
system were recorded without specimens, and these displacement 
values were subtracted from the measured displacement values in 
compression tests at their corresponding load. This method ex-
cludes the elastic responses of the load frame, load cell, and sample 
grips. Then, the deformation of the specimens could be calculated. 
Tensile samples with a gauge length of 2 cm were cut from the arc- 
melted ingots by electrical discharge machining. Tensile tests were 
conducted on a computer- controlled, uniaxial mechanical testing 
system (an MTS servo- hydraulic load frame) with an initial strain 
rate of 2 × 10−4 s−1. The strain values were recorded with an attached 
extensometer.
Density functional theory
The first- principles calculations were performed within the electron-
ic DFT (53,  54), using the Vienna Ab initio Simulation Package 
(V ASP) code (55, 56) in the Perdew- Burke- Ernzerhof generalized 
gradient approximation (57). Atomic coordinates and lattice param-
eters were relaxed with a high k- point density and default plane- wave 
energy cutoff. The Mo density of states (DOS) was calculated, using 
tetrahedron integration with a subsequent 0.1 eV Gaussian smearing, 
and we have shifted the energy scale to place the Fermi energy of Mo 
at zero. Fermi energies for VEC  = 4 to 8 were calculated from the 
integrated density of states. The COHP (50) was calculated using the 
score =
/uni2211.s1
alli
p i − p i−best
p i−range (1)
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 12

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
12 of 14
LOBSTER code (58) to determine the energy- dependent contribu-
tions of the interatomic bonding to the total energy. The negative and 
positive COHP values indicate bonding and antibonding states, re-
spectively. Electronic orbitals were calculated using V ASP (55,  56) 
and the Mo 4p, 4d, and 5s atomic orbitals were used in the projection. 
Values of COHP are dimensionless, and the integral up to the Fermi 
energy yields an energy related to the bond strength.
AIMD simulations and relaxations were performed for 6 × 6 × 6 
supercells of 432 atoms at the equiatomic composition. A single k- 
point was used in these calculations. AIMD simulations were in the 
NVT ensemble at the temperatures indicated for a duration of 500 fs 
using 1- fs time steps. Conjugate gradient relaxations were per -
formed until the maximum forces fell below 0.01 eV/Å.
After relaxation, the mean atomic displacement, representing the 
lattice distortion is defined as
Here, ������� ⃗R k−0 and � � �⃗Rk are the Cartesian coordinates of the atom, k, be-
fore and after relaxation. ∣ � � �⃗R k − ������� ⃗R k−0∣ represent the magnitude of 
the atomic- displacement vector. N is the total number of atoms in 
the supercell.
Electronic densities of states were calculated for simulated struc-
tures of 432 atoms in a 6 × 6 × 6 BCC supercell. The structures were 
fully relaxed in position and lattice parameters using the electronic 
DFT with standard pseudopotentials and a single electronic k- point. 
The density of state was then calculated for the relaxed structure us-
ing a 2 × 2 × 2 k- point mesh.
MC simulation
The Metropolis MC simulation (20,  34) incorporates the nearest- 
neighbor interaction paradigm with the nearest- neighbor interac-
tion energy, v ij, given by
Here, H ij is the binary energy of formation (59). The parameter z is 
the number of the nearest- neighbor bonds per atom and has a value 
of 4 in the BCC structure (20). H ij values used in this study are 
tabulated in table S5.
The system commences with a randomized structural configura-
tion, mirroring the disordered alloy’ s atomic disposition. Within every 
MC iteration, a random change to the current configuration is pro-
posed. Here, this random alteration is the positional exchange of two 
atoms. The energies of the old and the modified configurations are 
compared. If the modified configuration has lower energy, it is accepted. 
If it has higher energy, it is accepted with a Boltzmann probability, P
where ΔH is the energy difference between the two configurations, 
kB is the Boltzmann constant, and T is the temperature. The MC 
simulation in this study uses a configuration of a 12 × 12 × 12 super-
cell of the BCC unit cell comprising 3456 atoms and executes more 
than 107 MC iterations.
The BCC/B2 lattice comprises two distinct sublattices, α and β. 
In a disordered BCC phase, elements are uniformly distributed be-
tween α and β, while in an ordered B2 matrix, they show sublattice 
preference. The order parameter for atom i, denoted as LROi, is 
given by
Here, xi−α and xi−β represent the occupancy of the element i on the 
α and β sublattices, respectively. The LROi value spans from −1 to 1, 
where 0 denotes a lack of sublattice preference. Conversely, values of 
1 or −1 indicate an exclusive occupancy of a particular sublattice, 
representing the highest degree of atomic ordering.
The alloy’s LRO is defined as
where ci denotes the atomic percentage of each kind of atom, i.e., 
LRO spans between 0 (disordered) and 1 (ordered).
The ratio of the nearest- neighbor pairs, Pairi−j, is defined as
within this context, ni- j represents the count of an atom pair, i- j, in 
the MC supercell. The Pairi−j quantifies the probability of an atom, j, 
being among the nearest neighbors of the atom; i.e., Pairi−j generally 
remains steady at elevated temperatures with a disordered BCC 
phase and is only determined by the atomic percentages of atoms i 
and j in the alloy. As the temperature decreases, certain nearest- 
neighbor pairs gain preference, leading to a deviation of the Pairi−j 
distribution from a random arrangement. This shift underscores the 
dynamic nature of atomic interactions and the emerging order with-
in the system.
The comparison of the measured XRD patterns and the simulat-
ed XRD patterns based on MC structures at 0 K with the highest B2 
LRO can empirically estimate the extent of LRO in the alloy. For 
HEAs, stoichiometric limitations often prevent perfect lattice order-
ing (LRO = 1), as not every element can exclusively occupy a single 
sublattice. For instance, in the Al 15Hf25Nb32Ti28, at least one ele-
ment must occupy both B2 sublattices to balance atom numbers, 
resulting in an LRO of less than 1. A reference state is thus required 
for each HEA to represent the highest LRO achievable for an ener -
getically favored atomic configuration. Herein, we select the MC- 
simulated supercell at 0 K as the reference state. The B2 unit cell 
structure parameters in each Al- RHEA ’s reference state can be de-
rived from Fig. 5 (C to F) at 0 K, with detailed values listed in table 
S7. Powder diffraction patterns are then simulated using the VESTA 
(Visualization for Electronic and Structural Analysis) software (60), 
and the patterns are plotted in fig. S5. By comparing the measured 
XRD patterns with the reference diffraction patterns, we can esti-
mate the extent of LRO relative to the reference state. Theoretically, 
the intensity of superlattice- diffraction peaks is proportional to the 
square of the LRO (61). Here, however, this rule is used only to esti-
mate the LRO in the alloy, accounting for experimental errors from 
the XRD patterns obtained from the bulk material where certain 
favored grain growth orientations may exist. This semiquantitative 
evaluation on the extent of LRO developed in each alloy relative to 
the reference state (S) is expressed as
< ∣ΔR∣ > =
∑
allk ∣ � � �⃗R k − ������� ⃗R k−0 ∣
N
(2)
vij =
H ij
z (3)
P = e
−ΔH
kB T (4)
LROi =
xi−α − x i−β
xi−α + x i−β
(5)
LRO =
/uni221A.s1/uni2211.s1
allici LRO i
2 (6)
Pair i−j =
n i−j
∑
all jn i−j
(7)
S2 =
Isuper−meausured
Isuper−reference (8)
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 13

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
13 of 14
Here, Isuper−meausured and Isuper−reference represent the total intensities 
of B2- superlattice diffraction peaks in the measured XRD pattern 
and the powder diffraction patterns derived from the reference 
state, respectively. These peaks, with Miller indices of (100), (111), 
(210), (221), (300), and (311), are normalized by the total peak in-
tensity in the scanned 2θ range from 20° to 110°. The range of S is 
from 0 to 100%, representing an alloy having no LRO to having a 
similar level of LRO to the reference state.
Alloy melting temperature and density prediction method
Tmelt is predicted by the following method (24)
Here, Ti- j is the binary liquidus temperature of the element pair, i- j, 
on the binary- phase diagram with a relative atomic ratio of ci/cj. The 
method of extracting binary liquidus temperatures is described in 
detail in a previous work (24).
The density, ρ, is predicted by the rule of mixtures
Here, w i and ρi are the weight percentage and density of the 
ith element.
Supplementary Materials
This PDF file includes:
Figs. S1 to S7
tables S1 to S7
References
REFERENCES AND NOTES
 1. D. B. Miracle, O. n. Senkov, A critical review of high entropy alloys and related concepts. 
Acta Mater. 122, 448–511 (2017).
 2. S. Wei, S. J. Kim, J. Kang, Y. Zhang, Y. Zhang, t. Furuhara, e. S. Park, c. c. tasan, natural- 
mixing guided design of refractory high- entropy alloys with as- cast tensile ductility. Nat. 
Mater. 19, 1175–1181 (2020).
 3. X. Yan, P . K. liaw, Y. Zhang, Ultrastrong and ductile Bcc high- entropy alloys with 
low- density via dislocation regulation and nanoprecipitates. J. Mater. Sci. Technol. 110, 
109–116 (2022).
 4. v . Soni, B. Gwalani, O. n. Senkov, B. viswanathan, t. Alam, D. B. Miracle, R. Banerjee, Phase 
stability as a function of temperature in a refractory high- entropy alloy. J. Mater. Res. 33, 
3235–3246 (2018).
 5. v . Soni, B. Gwalani, t. Alam, S. Dasari, Y. Zheng, O. n. Senkov, D. Miracle, R. Banerjee, Phase 
inversion in a two- phase, Bcc+B2, refractory high entropy alloy. Acta Mater. 185, 89–97 (2020).
 6. O. n. Senkov, D. isheim, D. n. Seidman, A. l. Pilchak, Development of a refractory high 
entropy superalloy. Entropy 18, 102 (2016).
 7. l. Wang, J. Ding, S. chen, K. Jin, Q. Zhang, J. c ui, B. Wang, B. chen, t. li, Y. Ren, S. Zheng, 
K. Ming, W. lu, J. hou, G. Sha, J. liang, l. Wang, Y. Xue, e. Ma, tailoring planar slip to 
achieve pure metal- like ductility in body- centred- cubic multi- principal element alloys. 
Nat. Mater. 22, 950–957 (2023).
 8. B. Gorr, F. Mueller, h.- J. christ, h. chen, A. Kauffmann, R. Schweiger, D. v. Szabó, 
M. heilmaier, Development of oxidation resistant refractory high entropy alloys for high 
temperature applications: Recent results and development strategy, in TMS 2018 147th 
Annual Meeting & Exhibition Supplemental Proceedings (Springer international Publishing; 
2018), pp. 647–659.
 9. M. li, Q. chen, X. cui, X. Peng, G. huang, evaluation of corrosion resistance of the 
single- phase light refractory high entropy alloy ticrvnb0.5Al0.5 in chloride environment. 
J. Alloys Compd. 857, 158278 (2021).
 10. S. laube, h. chen, A. Kauffmann, S. Schellert, F. Müller, B. Gorr, J. Müller, B. Butz, 
h. J. christ, M. heilmaier, controlling crystallographic ordering in Mo–cr–ti–Al high 
entropy alloys to enhance ductility. J. Alloys Compd. 823, 153805 
(2020).
 11. n. Y. Yurchenko, n. D. Stepanov, S. v. Zherebtsov, M. A. tikhonovsky, G. A. Salishchev, 
Structure and mechanical properties of B2 ordered refractory AlnbtivZrx (x = 0–1.5) 
high- entropy alloys. Mater. Sci. Eng. A 704, 82–90 (2017).
 12. n. Yurchenko, e . Panina, M. tikhonovsky, G. Salishchev, S. Zherebtsov, n. Stepanov, A new 
refractory ti- nb- hf- Al high entropy alloy strengthened by orthorhombic phase particles. 
Int. J. Refract. Met. Hard Mater. 92, 105322 (2020).
 13. n. Y. Yurchenko, n. D. Stepanov, A. O. Gridneva, M. v. Mishunin, G. A. Salishchev, 
S. v. Zherebtsov, effect of cr and Zr on phase stability of refractory Al- cr- nb- ti- v- Zr 
high- entropy alloys. J. Alloys Compd. 757, 403–414 (2018).
 14. O. n. Senkov, J. K. Jensen, A. l. Pilchak, D. B. Miracle, h. l. Fraser, compositional variation 
effects on the microstructure and properties of a refractory high- entropy superalloy 
AlMo0.5nbta0.5tiZr. Mater. Des. 139, 498–511 (2018).
 15. O. n. Senkov, c. Woodward, D. B. Miracle, Microstructure and properties of aluminum- 
containing refractory high- entropy alloys. JOM 66, 2030–2042 (2014).
 16. A. lacour- Gogny- Goubert, Z. Zhao- huvelin, A. Bachelier- locq, i. Guillot, A. Denquin, 
effect of Al content on microstructure and properties of AlxMonbtiv RccA’s alloys. Mater. 
Sci. Forum 941, 1111–1116 (2018).
 17. G. Ouyang, P . Singh, R. Su, D. D. Johnson, M. J. Kramer, J. h. Perepezko, O. n. Senkov, 
D. Miracle, J. cui, Design of refractory multi- principal- element alloys for high- 
temperature applications. NPJ Comput. Mater. 9, 141 (2023).
 18. J. J. Bhattacharyya, S. B. inman, M. A. Wischhusen, J. Qi, J. Poon, J. R. Scully, S. R. Agnew, 
lightweight, low cost compositionally complex multiphase alloys with optimized 
strength, ductility and corrosion resistance: Discovery, design and mechanistic 
understandings. Mater. Des. 228, 111831 (2023).
 19. Z. Rao, P . Y. tung, R. Xie, Y. Wei, h. Zhang, A. Ferrari, t. P . c. Klaver, F. Körmann, 
P . t. Sukumar, A. K. da Silva, Y. chen, Z. li, D. Ponge, J. neugebauer, O. Gutfleisch, S. Bauer, 
D. Raabe, Machine learning–enabled high- entropy alloy discovery. Science 378, 
eabo4940 (2022).
 20. R. Feng, c. Zhang, M. c. Gao, Z. Pei, F. Zhang, Y. chen, D. Ma, K. An, J. D. Poplawsky, 
l. Ouyang, Y. Ren, J. A. hawk, M. Widom, P . K. liaw, h igh- throughput design of 
high- performance lightweight high- entropy alloys. Nat. Commun. 12, 4329 (2021).
 21. S. Guo, c. ng, J. lu, c. t. liu, effect of valence electron concentration on stability of fcc or 
bcc phase in high entropy alloys. J. Appl. Phys. 109, 103505 (2011).
 22. D. B. Miracle, M. h. tsai, O. n. Senkov, v. Soni, R. Banerjee, Refractory high entropy 
superalloys (RSAs). Scr. Mater. 187, 445–452 (2020).
 23. v . Soni, O. n. Senkov, J.- P . couzinie, Y. Zheng, B. Gwalani, R. Banerjee, Phase stability and 
microstructure evolution in a ductile refractory high entropy alloy Al10nb15ta5ti30Zr40. 
Materialia 9, 100569 (2020).
 24. J. Qi, A. M. cheung, S. J. Poon, high entropy alloys mined from binary phase diagrams. Sci. 
Rep. 9, 15501 (2019).
 25. J. Qi, D. i. hoyos, S. J. Poon, Machine learning- based classification, interpretation, and 
prediction of high- entropy- alloy intermetallic phases. High Entropy Alloys Mater. 1, 
312–326 (2023).
 26. S. J. Poon, J. Qi, A. M. cheung, harnessing the complex compositional space of 
high- entropy alloys, in High- Entropy Materials: Theory, Experiments, and Applications, 
J. Brechtl, P . K. liaw, eds. (Springer international Publishing, 2021), pp. 63–113.
 27. F. hussein, n. Kharma, R. Ward, Genetic algorithms for feature selection and weighting, a 
review and study, in Proceedings of the International Conference on Document Analysis and 
Recognition, ICDAR (ieee; 2001), pp. 1240–1244.
 28. W. P . huhn, M. Widom, A. M. cheung, G. J. Shiflet, S. J. Poon, J. lewandowski, First- 
principles calculation of elastic moduli of early- late transition metal alloys. Phys. Rev. B 89, 
104103 (2014).
 29. Y. J. hu, A. Sundar, S. Ogata, l. Qi, Screening of generalized stacking fault energies, 
surface energies and intrinsic ductile potency of refractory multicomponent alloys. Acta 
Mater. 210, 116800 (2021).
 30. e . Mak, B. Yin, W. A. curtin, A ductility criterion for bcc high entropy alloys. J. Mech. Phys. 
Solids 152, 104389 (2021).
 31. S. Qiu, n. Miao, J. Zhou, Z. Guo, Z. Sun, Strengthening mechanism of aluminum on elastic 
properties of nbvtiZr high- entropy alloys. Intermetallics 92, 7–14 (2018).
 32. S. A. Giles, h. Shortt, P . K. liaw, D. Sengupta, Yield strength- plasticity trade- off and 
uncertainty quantification for machine- learning- based design of refractory high- entropy 
alloys. arXiv:2304.13932 [cond- mat.mtrl- sci] (2023).
 33. Y. S. Zhao, J. Zhang, Y. S. luo, B. Zhang, G. Sha, l. F. li, D. Z. tang, Q. Feng, improvement of 
grain boundary tolerance by minor additions of hf and B in a second generation single 
crystal superalloy. Acta Mater. 176, 109–122 (2019).
 34. l. J. Santodonato, P . K. liaw, R. R. Unocic, h. Bei, J. R. Morris, Predictive multiphase 
evolution in Al- containing high- entropy alloys. Nat. Commun. 9, 4520 (2018).
 35. A. Pathak, A first principles calculation of site occupancy of the B2 phase in ti2AlX (X=v, 
cr, Fe, Mo, ta, nb, Zr, hf and Re) intermetallics. Chin. J. Phys. 60, 339–344 (2019).
 36. F. Körmann, t. Kostiuchenko, A. Shapeev, J. neugebauer, B2 ordering in body- centered- 
cubic Alnbtiv refractory high- entropy alloys. Phys. Rev. Mater. 5, 053803 
(2021).
T melt =
∑
i≠jT i−j × ci × cj
∑
i≠jci × cj
(9)
1
ρ =
/uni2211.s1
i
w i
ρi
(10)
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025

## Page 14

Qi et al., Sci. Adv. 10, eadq0083 (2024) 4 December 2024
Science ADv AnceS | ReSeAR ch AR ticle
14 of 14
 37. B. Feng, M. Widom, elastic stability and lattice distortion of refractory high entropy alloys. 
Mater. Chem. Phys. 210, 309–314 (2018).
 38. O. n. Senkov, J.- P . couzinie, S. i. Rao, v. Soni, R. Banerjee, temperature dependent 
deformation behavior and strengthening mechanisms in a low density refractory high 
entropy alloy Al10nb15ta5ti30Zr40. Materialia 9, 100627 (2020).
 39. R. R. eleti, n. Stepanov, n. Yurchenko, D. Klimenko, S. Zherebtsov, Plastic deformation of 
solid- solution strengthened hf- nb- ta- ti- Zr body- centered cubic medium/high- entropy 
alloys. Scr. Mater. 200, 113927 (2021).
 40. c. Rentenberger, h. P . Karnthaler, On the evolution of a deformation induced 
nanostructure in a ni3Al alloy. Acta Mater. 53, 3031–3040 (2005).
 41. S. Sheikh, S. Shafeie, Q. hu, J. Ahlström, c. Persson, J. veselý, J. Zýka, U. Klement, S. Guo, 
Alloy design for intrinsically ductile refractory high- entropy alloys. J. Appl. Phys. 120, 
164902 (2016).
 42. c. Wen, c. Wang, Y. Zhang, S. Antonov, D. Xue, t. lookman, Y. Su, Modeling solid solution 
strengthening in high entropy alloys using machine learning. Acta Mater. 212, 116917 (2021).
 43. G. vazquez, P . Singh, D. Sauceda, R. couperthwaite, n. Britt, K. Youssef, D. D. Johnson, 
R. Arróyave, efficient machine- learning model for fast assessment of elastic properties of 
high- entropy alloys. Acta Mater. 232, 117924 (2022).
 44. M.- h. tsai, K.- Y. tsai, c.- W. tsai, c. lee, c.- c. Juan, J.- W. Yeh, criterion for sigma phase 
formation in cr- and v- containing high- entropy alloys. Mater. Res. Lett. 1, 207–212 (2013).
 45. X. J. Gu, S. J. Poon, G. J. Shiflet, M. Widom, Ductility improvement of amorphous steels: 
Roles of shear modulus and electronic structure. Acta Mater. 56, 88–94 (2008).
 46. X. J. Gu, S. J. Poon, G. J. Shiflet, M. Widom, Mechanical properties, glass transition 
temperature, and bond enthalpy trends of high metalloid Fe- based bulk metallic glasses. 
Appl. Phys. Lett. 92, 161910 (2008).
 47. B. Feng, M. Widom, Band structure theory of the bcc to hcp Burgers distortion. Phys. Rev. 
B 98, 174108 (2018).
 48. v . Raghuraman, M. Widom, M. c. Gao, nonlinear deformation and elasticity of Bcc 
refractory metals and alloys. Phys Rev Mater 6, 053601 (2022).
 49. n. F. Mott, h. Jones, The Theory of the Properties of Metals and Alloys (Dover Publications, 1958).
 50. R. Dronskowski, P . e. Blöchl, crystal orbital hamilton populations (cOhP). energy- resolved 
visualization of chemical bonding in solids based on density- functional calculations. 
J. Phys. Chem. 97, 8617–8624 (1993).
 51. M. Mihalkovič, M. Widom, First- principles calculations of cohesive energies in the Al- co 
binary alloy system. Phys. Rev. B 75, 014207 (2007).
 52. U. Bhandari, M. R. Rafi, c. Zhang, S. Yang, Yield strength prediction of high- entropy alloys 
using machine learning. Mater Today Commun 26, 101871 (2021).
 53. P . hohenberg, W. Kohn, i nhomogeneous electron gas. Phys. Rev. 136, B864–B871 
(1964).
 54. W. Kohn, l. J. Sham, Self- consistent equations including exchange and correlation effects. 
Phys. Rev. 140, A1133–A1138 (1965).
 55. G. Kresse, J. Furthmüller, efficient iterative schemes for ab initio total- energy calculations 
using a plane- wave basis set. Phys. Rev. B 54, 11169–11186 (1996).
 56. G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented- wave 
method. Phys. Rev. B 59, 1758–1775 (1999).
 57. J. P . Perdew, K. Burke, M. ernzerhof, Generalized gradient approximation made simple. 
Phys. Rev. Lett. 77, 3865–3868 (1996).
 58. S. Maintz, v. l. Deringer, A. l. tchougréeff, R. Dronskowski, l OBSteR: A tool to extract 
chemical bonding from plane- wave based DFt. J. Comput. Chem. 37, 1030–1035 (2016).
 59. M. c. troparevsky, J. R. Morris, P . R. c. Kent, A. R. l upini, G. M. Stocks, c riteria for 
predicting the formation of single- phase high- entropy alloys. Phys. Rev. X 5, 011041 
(2015).
 60. K. Momma, F. izumi, VESTA 3 for three- dimensional visualization of crystal, volumetric and 
morphology data. J. Appl. Cryst. 44, 1272–1276 (2011).
 61. A. Guinier, X- Ray Diffraction: In Crystals, Imperfect Crystals, and Amorphous Bodies (courier 
corporation, 1963).
 62. R. tran, Z. Xu, B. Radhakrishnan, D. Winston, W. Sun, K. A. Persson, S. P . Ong, Surface 
energies of elemental crystals. Sci. Data 3, 160080 (2016).
 63. X. Z. Wu, R. Wang, S. F. Wang, Q. Y. Wei, Ab initio calculations of generalized- stacking- fault 
energy surfaces and surface energies for Fcc metals. Appl. Surf. Sci. 256, 6345–6349 
(2010).
 64. X. Wu, R. Wang, S. Wang, Generalized- stacking- fault energy and surface properties for 
hcP metals: A first- principles study. Appl. Surf. Sci. 256, 3409–3412 (2010).
 65. t . l. Achmad, W. Fu, h. chen, c. Zhang, Z. G. Yang, First- principles calculations of 
generalized- stacking- fault- energy of co- based alloys. Comput. Mater. Sci. 121, 86–96 
(2016).
 66. B. Bienvenu, c. c. Fu, e. clouet, impact of magnetism on screw dislocations in 
body- centered cubic chromium. Acta Mater. 200, 570–580 (2020).
 67. P . tu, Y. Zheng, c. Zhuang, X. Zeng, h. Zhu, A high- throughput computation framework 
for generalized stacking fault energies of pure metals. Comput. Mater. Sci. 159, 357–364 
(2019).
 68. X.- t. chen, l. Shao, n. Ding, J.- M. Duan, B.- Y. tang, Stacking fault energy of basal plane for 
hexagonal closed- packed medium entropy alloy Zrhfti: Ab initio prediction. Appl. Phys. A 
127, 670 (2021).
 69. X. Wang, S. Xu, W. R. Jian, X. G. li, Y. Su, i. J. Beyerlein, Generalized stacking fault energies 
and Peierls stresses in refractory body- centered cubic metals from machine learning- 
based interatomic potentials. Comput. Mater. Sci. 192, 110364 (2021).
 70. X. Zhang, J. tang, l. Deng, G. Zhong, X. liu, Y. li, h. Deng, W. hu, the effects of interstitial 
impurities on the mechanical properties of vanadium alloys: A first- principles study. 
J. Alloys Compd. 701, 975–980 (2017).
 71. R. hill, the elastic behaviour of a crystalline aggregate. Proc. Phys. Soc. A 65, 349 (1952).
 72. A. Reuss, Berechnung der Fließgrenze von Mischkristallen auf Grund der 
Plastizitätsbedingung für einkristalle. Z. Angew. Math. Mech. 9, 49–58 (1929).
 73. A. takeuchi, A. inoue, classification of bulk metallic glasses by atomic size difference, heat 
of mixing and period of constituent elements and its application to characterization of 
the main alloying element. Mater. Trans. 46, 2817–2829 (2005).
 74. i. toda- caraballo, A general formulation for solid solution hardening effect in 
multicomponent alloys. Scr. Mater. 127, 113–117 (2017).
 75. c. varvenne, A. luque, W. A. curtin, theory of strengthening in fcc high entropy alloys. 
Acta Mater. 118, 164–176 (2016).
 76. Y. F. Ye, c. t. liu, Y. Yang, A geometric model for intrinsic residual strain and phase stability 
in high entropy alloys. Acta Mater. 94, 152–161 (2015).
Acknowledgments: M.W. acknowledges a discussion with Amit Samanta on the link between 
the Fermi level density of states and ductility. Funding: this work was supported by the 
Department of energy under grant no. De- Sc0014506 (M.W.), the Office of naval Research 
under grant no. n00014- 23- 1- 2441 (J.Q., D.i.h., and J.P .), the national Science Foundation 
(DMR—1611180, 1809640, and 2226508) (X.F. and P .K.l.), the US Army Research Office 
(FA9550- 23- 1- 0503, W911nF- 13- 1- 0438, and W911nF- 19- 2- 0049) (X.F. and P .K.l.), the 
Department of energy (DOe De- ee0011185) (P .K.l.), and the State of tennessee and tennessee 
higher education commission (thec) through their support of the center for Materials 
Processing (cMP) at the University of tennessee (X.F.). the present research used the resources 
of the national energy Research Scientific computing center (neRSc), a US Department of 
energy Office of Science User Facility operated under contract number De- Ac02- 05ch11231, 
using the neRSc award, BeS- eRcAP24744. (M.W.). Author contributions: conceptualization: 
J.Q., M.W., J.P ., and P .K.l. Methodology: J.Q., J.P ., D.i.h., M.W., and P .K.l. investigation: J.Q., X.F., 
D.i.h., and M.W. visualization: J.Q. and M.W. Supervision: J.P ., P .K.l., and M.W. Writing—original 
draft: J.Q., X.F., and M.W. Writing—review and editing: J.Q., J.P ., and P .K.l. Competing 
interests: the authors declare that they have no competing interests. Data and materials 
availability: All data needed to evaluate the conclusions in the paper are present in the paper 
and/or the Supplementary Materials.
Submitted 22 April 2024 
Accepted 30 October 2024 
Published 4 December 2024 
10.1126/sciadv.adq0083
Downloaded from https://www.science.org at Xi'an Jiaotong University on November 25, 2025
