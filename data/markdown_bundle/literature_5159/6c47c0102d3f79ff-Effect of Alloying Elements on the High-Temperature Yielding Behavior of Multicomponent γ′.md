# Effect of Alloying Elements on the High-Temperature Yielding Behavior of Multicomponent γ′-L12 Alloys

<!-- source: D:\总文献\Effect of Alloying Elements on the High-Temperature Yielding Behavior of Multicomponent γ′-L12 Alloys.pdf -->
<!-- file_sha256: 278ccbebed4e368e773fc91cc486d4e4ac3bd4856d3d0c41321159e48d69e311 -->

## Page 1

Citation: Wang, C.-Y.; Matsunaga, S.;
Toda, Y.; Murakami, H.; Yeh, A.-C.;
Yamabe-Mitarai, Y. Effect of Alloying
Elements on the High-Temperature
Yielding Behavior of Multicomponent
γ′-L12 Alloys. Materials 2024, 17, 2280.
https://doi.org/10.3390/
ma17102280
Academic Editor: Joan-Josep Suñol
Received: 19 April 2024
Revised: 3 May 2024
Accepted: 9 May 2024
Published: 11 May 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
materials
Article
Effect of Alloying Elements on the High-Temperature Yielding
Behavior of Multicomponent γ′-L12 Alloys
Chen-Yuan Wang 1, Sae Matsunaga 1,*
 , Yoshiaki Toda2
 , Hideyuki Murakami 2,3
 , An-Chou Yeh 4
and Yoko Yamabe-Mitarai 1,*
1 Department of Advanced Materials Science, The University of Tokyo, 5-1-5 Kashiwanoha,
Kashiwa-shi 277-8561, Chiba, Japan; 1775090211@edu.k.u-tokyo.ac.jp
2 National Institute for Materials Science, 1-2-1 Sengen, Tsukuba 305-0047, Ibaraki, Japan;
toda.yoshiaki@nims.go.jp (Y.T.); murakami.hideyuki@nims.go.jp (H.M.)
3 Department of Nanoengineering and Nanoscience, Waseda University, Shinjuku 169-8555, Tokyo, Japan
4 High Entropy Materials Center, National Tsing Hua University, Hsinchu 30013, Taiwan;
yehac@mx.nthu.edu.tw
* Correspondence: smatsun@edu.k.u-tokyo.ac.jp (S.M.); mitarai.yoko@edu.k.u-tokyo.ac.jp (Y.Y.-M.)
Abstract: The exceptional mechanical properties of Ni-based high entropy alloys are due to the
presence of ordered L12 (γ′) precipitates embedded within a disordered matrix phase. While the
strengthening contribution of the γ′ phase is generally accepted, there is no consensus on the precise
contribution of the individual strengthening mechanisms to the overall strength. In addition, changes
in alloy composition influence several different mechanisms, making the assessment of alloying
conditions complex. Multicomponent L12-ordered single-phase alloys were systematically developed
with the aid of CALPHAD thermodynamic calculations. The alloying elements Co, Cr, Ti, and Nb
were chosen to complexify the Ni3Al structure. The existence of the γ′ single phase was validated
by microstructure characterization and phase identification. A high-temperature compression test
from 500 ◦C to 1000 ◦C revealed a positive temperature dependence of strength before reaching the
peak strength in the studied alloys NiCoCrAl, NiCoCrAlTi, and NiCoCrAlNb. Ti and Nb alloying
addition significantly enhanced the high-temperature yield strengths before the peak temperature.
The yield strength was modeled by summing the individual effects of solid solution strengthening,
grain boundary strengthening, order strengthening, and cross-slip-induced strengthening. Cross-
slip-induced strengthening was shown to be the key contributor to the high-temperature strength
enhancement.
Keywords: multicomponent alloy; high-temperature deformation; intermetallic compounds; CAL-
PHAD
1. Introduction
Ni-based superalloys have been extensively employed as critical high-temperature
structural materials used in aerospace engineering and the power generation industry
due to their superior high-temperature mechanical properties, which are derived from
the combination of 60–70% volume fraction of ordered γ′ precipitates (L12) coherently
embedded in the solid-solution γ matrix (FCC-A1) [1]. The alloy design of Ni-based su-
peralloys has approached its limit for performance enhancements due to the constraints
of Ni-based systems. A novel concept in alloy design, high entropy alloys (HEAs), has
made a breakthrough in conventional alloys by revisiting the vast composition space [2].
Precipitation-strengthened HEAs, as newly emerging structural materials, are highly attrac-
tive due to their combination of strength and ductility [3–9]. Compared to grain boundary
strengthening and solid solution strengthening, precipitation strengthening of multicom-
ponent L12 nanoprecipitates can significantly improve the yield strength of HEAs while
maintaining good ductility. Yeh et al. [9] first introduced the L12 nanoprecipitates of (Ni,
Materials 2024, 17, 2280. https://doi.org/10.3390/ma17102280 https://www.mdpi.com/journal/materials

## Page 2

Materials 2024, 17, 2280 2 of 12
Co)3Ti into the FeCoNiCr system by adding Ti to form a precipitation-strengthened HEA.
Later, Yang et al. [8] designed and developed a complex alloy (FeNiCo)86Al7Ti7 with multi-
component L12 intermetallic particles (Ni, Co, Fe)3(Ti, Al, Fe) and reported a combination
of high strength (~1 GPa) and excellent ductility (~50%) at room temperature. They at-
tributed the pronounced increase in yield strength to the high ordering strengthening by
the high density of L12 nanoprecipitates and the higher anti-phase boundary energy (APBE)
provided by Ti addition.
Recently, Yang et al. [10] developed a multicomponent L12-ordered alloy, NiCoFeAlTiB,
and observed that the materials did not experience obvious softening behavior below
800 ◦C under the hardness test. Long et al. [11] investigated a multicomponent Co-based
L12 ordered single phase intermetallic alloy and found that the alloy exhibited anomalous
yield strength increase from 250 ◦C to 800 ◦C. The stress anomaly was stronger than
ternary L12 Co3(Al, W) and B-doped Ni3Al. These results revealed that a high-temperature
capability could be achieved by the complex L12 intermetallic. It is well known that the L12
phase exhibits anomalous yielding behavior, represented by a substantial yield strength
increase at intermediate temperatures [1]. This positive temperature dependence of stress
of L12 precipitates confers excellent high-temperature mechanical properties. It has been
generally accepted that the anomalous yielding behavior was due to the Kear–Wilsdorf
mechanism, forming anti-phase boundary (APB)-coupled dislocation pairs by thermally
activated cross-slip of a screw segment of the superpartial dislocation from octahedral {111}
planes to cube {010} planes. While the strength in Ni-based superalloys is proportional to
the APBE, the anisotropy in APBE between octahedral {111} planes and cube {010} planes
determines the yield strength anomaly. Since a perfect dislocation slipping on the plane in
Ni3Al consists of four Shockley partial dislocations and bounding one APB fault and two
complex stacking faults (CSF), the occurrence of thermally activated cross-slip process is
dependent on APB and CSF energies [12,13].
Considerable efforts have been devoted to researching the composition dependence
of the high-temperature strength and associated planar fault energies [ 14–18]. Mishima
et al. [14,19] systematically investigated the effect of ternary addition on the temperature
dependence of strength in ternary Ni3Al compounds. Among the investigated alloying
elements, Ti, Zr, Hf, V , Nb, Ta, Mo, W, Ti, Nb, and Ta produced the most drastic strength
increment. Moreover, advances in computational models and modern computers allow for
the APBE of the ternary Ni3Al intermetallic compounds to be predicted by density function
theory (DFT) calculations [13,20–24]. Gorbatov et al. [23] studied the effect of composition
on the APBE on both octahedral planes and cube planes of Ni-based L12-ordered alloys by
ab initio calculations and reported ternary alloying additions. Ti, V , and Cr occupied the Al
sublattice site and increased the APBE for both {111} and {010} planes, while Co, Cu, and
Fe occupied the Ni sublattice site and sightly affected both the {111} and {010} APBE.
Recent studies on the deformation mechanisms of L12-strengthened alloys revealed
that γ′-strengtheners, such as Ti, Ta, and Nb, significantly improved the creep performance
by forming the other phases at planar defects, which are considered to have slower de-
formation kinetics [25]. In addition, the experimental and computational works showed
Co and Cr and γ′ strengtheners significantly affected the phase transformation, which
preferentially occurred at planar defects. While forming an ordered phase with slower
formation kinetics can enhance the high-temperature creep performance, the formation
of disordered phases will degrade it. Determining the resulting phase hinges on subtle
discrepancies in nominal alloy composition [25–28]. Although the deformation mechanisms
of γ′-strengthened alloys have been investigated for decades, there are still some uncovered
questions about the γ′ phase. In γ + γ′ structures, deformation mechanisms are usually
significantly affected by the interactions at γ and γ′ interface [29]; thus, elucidating the
strengthening effect solely attributable to the γ′ phase has proven to be a formidable task.
Furthermore, while numerous recent studies have been dedicated to the effect of alloying
elements on the γ′-shearing mechanisms, their influence on phenomena unique to the L12

## Page 3

Materials 2024, 17, 2280 3 of 12
structure, such as the elevation of yielding stress at high temperatures, remains significantly
underexplored in a systematic manner.
Fundamental and systematic studies on multicomponent L1 2 phases are urgently
required to accelerate the advancement of L1 2-strengthened alloys. The precipitation
strengthening by L12-type Ni3Al nanoparticles has been extensively investigated in Ni-
based superalloys and HEAs. However, most previously investigated Ni 3Al phases are
compositionally simple and contain a lower level of ternary elements. Because of the
extensive alloying addition of Cr and Co in Ni-based superalloys and L1 2 precipitation
strengthened HEAs and their effect on local phase transformation, these two elements
were chosen as a base with Ni 3Al to design multicomponent L1 2 alloys. This work sys-
tematically varied compositions by substituting Ni and Al with Ti or Nb to study the
compositional effects on the yielding behaviors of the L12 phase. The investigated multi-
component L12 alloys were systematically designed using the thermodynamics software
CALPHAD Thermo-Calc TCNI8 Ni-based Superalloys Database [30]. The yielding behav-
iors of the multicomponent L12 alloys were evaluated by high-temperature compression
tests. The analysis and discussion will delve into the contribution of different strengthening
mechanisms under various alloying conditions.
2. Materials and Methods
The multicomponent γ′ (L12-ordered) single phase was designed by utilizing the
Thermo-Calc© TCNI8 database [30], aiming to obtain L12-ordered single phase within the
temperature range between 800 ◦C and 950 ◦C. We developed three systems, as follows:
• NiCoCrAl,
• NiCoCrAlTi,
• NiCoCrAlNb.
The pseudo-binary isopleths and volume fraction diagrams of three multicomponent
systems were calculated to confirm the solubility limit of Ti or Nb alloying addition in
NiCoCrAl alloy without forming any secondary phases. Ti and Nb were carefully added
to avoid exceeding their solubility limits, approximately 2 at%, in the NiCoCrAl alloy.
Selected compositions for the studied alloys are listed in Table 1 and marked using the
dash lines in Figure 1.
Table 1. Nominal compositions of the studied alloys (at%).
Al Co Cr Ni Ti Nb
CY1 21 10 5 64 - -
CY2 20 10 5 63 2 -
CY3 20 10 5 63 - 2
Materials 2024, 17, x FOR PEER REVIEW 4 of 12 
 
 
 
Figure 1. The pseudo-binary isopleth of three diﬀerent multicomponent systems: (a) NiCo10Cr5Al, 
(b) NiCo10Cr5Al20Ti, and (c) NiCo10Cr5Al20Nb. 
Table 1. Nominal compositions of the studied alloys (at%). 
 Al Co Cr Ni Ti Nb 
CY1 21 10 5 64 - - 
CY2 20 10 5 63 2 - 
CY3 20 10 5 63 - 2 
3. Results and Discussion 
3.1. Microstructures 
The volume fraction diagrams of the desi gned alloys are shown in Figure 2. The γ’ 
(L12-ordered) single phase exists in the range of 659–1104 °C in CY1, 870–1060 °C in CY2, 
and 858–991 °C in CY3. The temperature window with only the L12-ordered single phase 
narrowed by adding the ﬁfth element, while the γ + γ’ two-phase window broadened. The 
γ + γ′ window is 1104–1163 °C in CY1, 1060–1171 °C in CY2, and 991–1133 °C in CY3. Both 
Ti and Nb were classi ﬁed as γ′-stabilizers in terms of the alloy design strategy for γ + γ′ 
two-phase Ni-based superalloys [1]. Our calculation results indicated that these elements 
stabilized the L12-ordered phase in a wide range of temperatures with the existence of the 
γ matrix while they decreased the L12-ordered single-phase window. We also investigated 
the site occupancy in each alloy using thermodynamic calculations. It was simulated that 
Co tended to occupy the Ni sublattice sites, while Cr, Ti, and Nb atoms substituted the Al 
site atoms to create (Ni, Co)3(Al, Cr) in CY1, (Ni, Co)3(Al, Cr, Ti) in CY2, and (Ni, Co)3(Al, 
Cr, Nb) in CY3. 
 
Figure 2. Volume fraction diagrams of the following multicomponent L1 2-ordered intermetallic 
compounds: (a) CY1 (NiCoCrAl), (b) CY2 (NiCoCrAlTi), and (c) CY3 (NiCoCrAlNb). 
Figure 1. The pseudo-binary isopleth of three different multicomponent systems: (a) NiCo10Cr5Al,
(b) NiCo10Cr5Al20Ti, and (c) NiCo10Cr5Al20Nb.

## Page 4

Materials 2024, 17, 2280 4 of 12
In total, 300 g of the studied alloy ingots were prepared by the vacuum arc melt-
ing (VAM) process under an argon atmosphere with a Ti getter. Repeated melting was
carried out at least six times to ensure the chemical homogeneity. As-cast samples were
homogenized at 980 ◦C for 168 h, followed by air cooling to room temperature. For CY3
alloy with Nb alloying addition, a prior solution heat treatment (SHT) at 1280 ◦C for 168 h
was necessary to eliminate the dendritic structure caused by the severe Nb segregation.
The constituent phases were identified using an X-ray diffractometer (XRD, SmartLab,
Rigaku, Tokyo, Japan). The microstructures of each alloy were characterized using scan-
ning electron microscopy (SEM, JSM-7200 F, JEOL, Tokyo, Japan). The phase transformation
temperatures of the studied alloys were determined by differential thermal analysis (DTA,
Labsys DSC/DTA, Setaram, Caluire-et-Cuire, France) experiments between 25 ◦C and
1500 ◦C, with a scanning rate of 10 ◦C/min. Cuboid compression specimens with 3 mm and
6 mm width and height length were sectioned by a high-speed precision cutting machine.
High-temperature compression tests were performed to understand the strength evolution
at 500, 600, 700, 800, 900, and 1000 ◦C with a strain rate of 10 −4 s−1. All the tests were
interrupted after reaching approximately 10% plastic strain.
3. Results and Discussion
3.1. Microstructures
The volume fraction diagrams of the designed alloys are shown in Figure 2. The γ’
(L12-ordered) single phase exists in the range of 659–1104 ◦C in CY1, 870–1060 ◦C in CY2,
and 858–991 ◦C in CY3. The temperature window with only the L12-ordered single phase
narrowed by adding the fifth element, while the γ + γ’ two-phase window broadened. The
γ + γ′ window is 1104–1163 ◦C in CY1, 1060–1171 ◦C in CY2, and 991–1133 ◦C in CY3. Both
Ti and Nb were classified as γ′-stabilizers in terms of the alloy design strategy for γ + γ′
two-phase Ni-based superalloys [1]. Our calculation results indicated that these elements
stabilized the L12-ordered phase in a wide range of temperatures with the existence of the
γ matrix while they decreased the L12-ordered single-phase window. We also investigated
the site occupancy in each alloy using thermodynamic calculations. It was simulated that
Co tended to occupy the Ni sublattice sites, while Cr, Ti, and Nb atoms substituted the Al
site atoms to create (Ni, Co)3(Al, Cr) in CY1, (Ni, Co)3(Al, Cr, Ti) in CY2, and (Ni, Co)3(Al,
Cr, Nb) in CY3.
Materials 2024, 17, x FOR PEER REVIEW 4 of 12 
 
 
 
Figure 1. The pseudo-binary isopleth of three diﬀerent multicomponent systems: (a) NiCo10Cr5Al, 
(b) NiCo10Cr5Al20Ti, and (c) NiCo10Cr5Al20Nb. 
Table 1. Nominal compositions of the studied alloys (at%). 
 Al Co Cr Ni Ti Nb 
CY1 21 10 5 64 - - 
CY2 20 10 5 63 2 - 
CY3 20 10 5 63 - 2 
3. Results and Discussion 
3.1. Microstructures 
The volume fraction diagrams of the desi gned alloys are shown in Figure 2. The γ’ 
(L12-ordered) single phase exists in the range of 659–1104 °C in CY1, 870–1060 °C in CY2, 
and 858–991 °C in CY3. The temperature window with only the L12-ordered single phase 
narrowed by adding the ﬁfth element, while the γ + γ’ two-phase window broadened. The 
γ + γ′ window is 1104–1163 °C in CY1, 1060–1171 °C in CY2, and 991–1133 °C in CY3. Both 
Ti and Nb were classi ﬁed as γ′-stabilizers in terms of the alloy design strategy for γ + γ′ 
two-phase Ni-based superalloys [1]. Our calculation results indicated that these elements 
stabilized the L12-ordered phase in a wide range of temperatures with the existence of the 
γ matrix while they decreased the L12-ordered single-phase window. We also investigated 
the site occupancy in each alloy using thermodynamic calculations. It was simulated that 
Co tended to occupy the Ni sublattice sites, while Cr, Ti, and Nb atoms substituted the Al 
site atoms to create (Ni, Co)3(Al, Cr) in CY1, (Ni, Co)3(Al, Cr, Ti) in CY2, and (Ni, Co)3(Al, 
Cr, Nb) in CY3. 
 
Figure 2. Volume fraction diagrams of the following multicomponent L1 2-ordered intermetallic 
compounds: (a) CY1 (NiCoCrAl), (b) CY2 (NiCoCrAlTi), and (c) CY3 (NiCoCrAlNb). 
Figure 2. Volume fraction diagrams of the following multicomponent L1 2-ordered intermetallic
compounds: (a) CY1 (NiCoCrAl), (b) CY2 (NiCoCrAlTi), and (c) CY3 (NiCoCrAlNb).
Figure 3 shows the microstructure of the CY1, CY2, and CY3 alloys after homogenizing
heat treatment. All alloys exhibited single-phase microstructures after the heat treatments.
The average grain size of each alloy is around 503 µm in CY1, 849 µm in CY2, and 323 µm
in CY3. Any secondary phases were not detected either within the grains or at the grain
boundaries, as shown in Figure 3d–f, which confirms that we successfully designed and
manufactured the multicomponent L12-ordered single-phase alloys.

## Page 5

Materials 2024, 17, 2280 5 of 12
Materials 2024, 17, x FOR PEER REVIEW 5 of 12 
 
 
Figure 3 shows the microstructure of the CY1, CY2, and CY3 alloys after homogeniz-
ing heat treatment. All alloys exhibited sing le-phase microstructures after the heat treat-
ments. The average grain size of each alloy is around 503 µm in CY1, 849 µm in CY2, and 
323 µm in CY3. Any secondary phases were not detected either within the grains or at the 
grain boundaries, as shown in Figure 3d–f, which conﬁrms that we successfully designed 
and manufactured the multicomponent L1
2-ordered single-phase alloys. 
 
Figure 3. Backscatter images of microstructures after the heat treatments under diﬀerent magniﬁca-
tions: (a) CY1 (250×), (b) CY2 (250×), (c) CY3 (250×), (d) CY1 (10,000×), (e) CY2 (10,000×), and (f) CY3 
(10,000×). 
Figure 4 shows the indexed XRD spectra peaks. The 2θ values, corresponding to the 
indexed diﬀraction peaks of the studied alloys, are listed with the ones of Ni3Al in JCPDS 
ﬁles in Table 2. The 2 θ values of the studied alloys CY1, CY2, and CY3 agreed well with 
the values in JCPDS ﬁles, which conﬁrmed the existence of an L12-ordered single phase in 
the studied alloys. Minor di ﬀerences from the JCPDS ﬁles could arise from the peak 
broadening due to diﬀerences in grain size, lattice strain, and changes in lattice parameters 
[31]. The crystal structure and microstructure of the alloys after the heat treatments were 
in good agreement with the prediction from the calculated equilibrium phase diagrams. 
 
Figure 4. XRD analysis of the multicomponent L12-ordered intermetallic alloys. 
Figure 3. Backscatter images of microstructures after the heat treatments under different magnifi-
cations: (a) CY1 (250×), (b) CY2 (250×), (c) CY3 (250×), (d) CY1 (10,000×), (e) CY2 (10,000×), and
(f) CY3 (10,000×).
Figure 4 shows the indexed XRD spectra peaks. The 2θ values, corresponding to the
indexed diffraction peaks of the studied alloys, are listed with the ones of Ni3Al in JCPDS
files in Table 2. The 2θ values of the studied alloys CY1, CY2, and CY3 agreed well with the
values in JCPDS files, which confirmed the existence of an L12-ordered single phase in the
studied alloys. Minor differences from the JCPDS files could arise from the peak broadening
due to differences in grain size, lattice strain, and changes in lattice parameters [31]. The
crystal structure and microstructure of the alloys after the heat treatments were in good
agreement with the prediction from the calculated equilibrium phase diagrams.
Materials 2024, 17, x FOR PEER REVIEW 5 of 12 
 
 
Figure 3 shows the microstructure of the CY1, CY2, and CY3 alloys after homogeniz-
ing heat treatment. All alloys exhibited sing le-phase microstructures after the heat treat-
ments. The average grain size of each alloy is around 503 µm in CY1, 849 µm in CY2, and 
323 µm in CY3. Any secondary phases were not detected either within the grains or at the 
grain boundaries, as shown in Figure 3d–f, which conﬁrms that we successfully designed 
and manufactured the multicomponent L1
2-ordered single-phase alloys. 
 
Figure 3. Backscatter images of microstructures after the heat treatments under diﬀerent magniﬁca-
tions: (a) CY1 (250×), (b) CY2 (250×), (c) CY3 (250×), (d) CY1 (10,000×), (e) CY2 (10,000×), and (f) CY3 
(10,000×). 
Figure 4 shows the indexed XRD spectra peaks. The 2θ values, corresponding to the 
indexed diﬀraction peaks of the studied alloys, are listed with the ones of Ni3Al in JCPDS 
ﬁles in Table 2. The 2 θ values of the studied alloys CY1, CY2, and CY3 agreed well with 
the values in JCPDS ﬁles, which conﬁrmed the existence of an L12-ordered single phase in 
the studied alloys. Minor di ﬀerences from the JCPDS ﬁles could arise from the peak 
broadening due to diﬀerences in grain size, lattice strain, and changes in lattice parameters 
[31]. The crystal structure and microstructure of the alloys after the heat treatments were 
in good agreement with the prediction from the calculated equilibrium phase diagrams. 
 
Figure 4. XRD analysis of the multicomponent L12-ordered intermetallic alloys. 
Figure 4. XRD analysis of the multicomponent L12-ordered intermetallic alloys.
Table 2. The 2θ (◦) values with related diffraction plane of L12-ordered phase and the corresponding
values in JCPDS files and the lattice constants of the studied alloys.
(100) (111) (200) (220) (311) Lattice Constant
(Å)
JCPDS 24.90 43.60 50.70 75.02 91.21 -
CY1 24.98 43.87 51.51 75.02 91.50 3.48
CY2 24.78 43.98 50.59 74.81 91.14 3.58
CY3 24.77 44.03 51.00 75.24 91.18 3.59

## Page 6

Materials 2024, 17, 2280 6 of 12
Figure 5 shows the DTA heating curves of the heat-treated CY1, CY2, and CY3 alloys.
The onset temperature of endothermic peaks was determined as the phase transformation
temperatures and solvus temperatures. The phase transformation temperatures (PTTs)
were defined as the temperatures at which the alloys could retain the L12-ordered single
phase. Above these temperatures, the secondary and third phases started to form. The
PTTs and solvus temperatures are summarized in Table 3. The PTTs of the CY1, CY2 and
CY3 alloys were 1217 ◦C, 1244 ◦C, and 1298 ◦C, respectively. The results showed that
the L12-ordered single phase persisted at higher temperatures in the quinary alloys with
Ti or Nb alloying additions. In the Ni-based superalloys with γ + γ′ structure, adding
Ti or Nb increased γ′-solvus temperatures, indicating these elements could stabilize the
L12-ordered phase at elevated temperatures. Since our alloys were designed only to have
an L12-ordered single phase, the aforementioned effect of γ′-formers was observed as the
expansion of an L12-ordered single-phase regime. The solidus temperatures for the CY1,
CY2, and CY3 alloys were 1353 ◦C, 1324 ◦C, and 1305 ◦C, respectively. The decrease in
solidus caused by Ti alloying addition was also observed in Ni-based superalloys due to
the strong partition tendency of Ti to liquid phase, forming segregation phases with lower
melting temperatures and reducing the solidus temperature of the alloy [32,33].
Materials 2024, 17, x FOR PEER REVIEW 6 of 12 
 
 
Table 2. The 2θ (°) values with related diﬀraction plane of L12-ordered phase and the corresponding 
values in JCPDS ﬁles and the lattice constants of the studied alloys. 
 (100) (111) (200) (220) (311) 
Lattice 
Constant 
(Å) 
JCPDS 24.90 43.60 50.70 75.02 91.21 - 
CY1 24.98 43.87 51.51 75.02 91.50 3.48 
CY2 24.78 43.98 50.59 74.81 91.14 3.58 
CY3 24.77 44.03 51.00 75.24 91.18 3.59 
Figure 5 shows the DTA heating curves of the heat-treated CY1, CY2, and CY3 alloys. 
The onset temperature of endothermic peaks was determined as the phase transformation 
temperatures and solvus temperatures. The phase transformation temperatures (PTTs) 
were deﬁned as the temperatures at which the alloys could retain the L1 2-ordered single 
phase. Above these temperatures, the second ary and third phases started to form. The 
PTTs and solvus temperatures are summarized in Table 3. The PTTs of the CY1, CY2 and 
CY3 alloys were 1217 °C, 1244 °C, and 1298 °C, respectively. The results showed that the 
L12-ordered single phase persisted at higher temperatures in the quinary alloys with Ti or 
Nb alloying additions. In the Ni-based superalloys with γ + γ′ structure, adding Ti or Nb 
increased γ′-solvus temperatures, indicating these elements could stabilize the L1 2-or-
dered phase at elevated temperatures. Since our alloys were designed only to have an L12-
ordered single phase, the aforementioned eﬀect of γ′-formers was observed as the expan-
sion of an L1 2-ordered single-phase regime. The solidus temperatures for the CY1, CY2, 
and CY3 alloys were 1353 °C, 1324 °C, and 1305 °C, respectively. The decrease in solidus 
caused by Ti alloying addition was also observed in Ni-based superalloys due to the 
strong partition tendency of Ti to liquid phase, forming segregation phases with lower 
melting temperatures and reducing the solidus temperature of the alloy [32,33]. 
 
Figure 5. DTA heating curves of the studied alloys: (a) CY1, (b) CY2, and (c) CY3. 
Table 3. Phase transformation temperatures and solidus temperatures for the studied alloys. 
 CY1 (°C) CY2 (°C) CY3 (°C) 
Phase transformation temperature 1217 1244 1298 
Solidus temperature 1353 1324 1305 
3.2. Yielding Behavior through Temperatures 
Figure 6 depicts the 0.2% yield stress measured from the high-temperature compres-
sion tests for CY1, CY2, and CY3 along the def ormation temperatures. The yield stress 
measured at each temperature is summarized in Table 4. Regardless of the testing temper-
ature, CY3 exhibited the highest yield stre ss among the three alloys before the peak 
Figure 5. DTA heating curves of the studied alloys: (a) CY1, (b) CY2, and (c) CY3.
Table 3. Phase transformation temperatures and solidus temperatures for the studied alloys.
CY1 (◦C) CY2 ( ◦C) CY3 ( ◦C)
Phase transformation temperature 1217 1244 1298
Solidus temperature 1353 1324 1305
3.2. Yielding Behavior through T emperatures
Figure 6 depicts the 0.2% yield stress measured from the high-temperature compres-
sion tests for CY1, CY2, and CY3 along the deformation temperatures. The yield stress
measured at each temperature is summarized in Table 4. Regardless of the testing tem-
perature, CY3 exhibited the highest yield stress among the three alloys before the peak
temperature. All alloys exhibited yield stress increasing monotonically before reaching a
maximum and then significantly decreasing with increasing the testing temperature after
reaching the peak temperature. The difference in the yield stresses significantly decreased
after the peak temperatures.
Table 4. Yield strengths of the studied alloys at different temperatures.
(◦C) CY1 (MPa) CY2 (MPa) CY3 (MPa)
500 324.7 420.5 587.7
600 391.2 510.6 655.9
700 426.5 677.7 690.4
800 511.5 617.6 685.2
900 417.1 407.0 433.7
1000 259.5 300.9 288.7

## Page 7

Materials 2024, 17, 2280 7 of 12
Materials 2024, 17, x FOR PEER REVIEW 7 of 12 
 
 
temperature. All alloys exhibited yield stress increasing monotonically before reaching a 
maximum and then signiﬁcantly decreasing with increasing the testing temperature after 
reaching the peak temperature. The diﬀerence in the yield stresses signiﬁcantly decreased 
after the peak temperatures. 
Comparing the yield stress of CY1, the ones of CY2 are 30% higher at 500 °C, 31% 
higher at 600 °C, and 59% higher at 700 °C. In addition, the yield stresses of CY3 are 81% 
higher at 500 °C, 68% higher at 600 °C, and 62% higher at 700 °C. The peak strengths for 
CY1, CY2, and CY3 alloys were 426 MPa, 678 MPa, and 690 MPa, respectively. Our results 
revealed that the ﬁfth alloying addition produced a signi ﬁcant enhancement in the yield 
stress while exhibiting anom alous yielding behavior, whic h was reported in numerous 
studies about the high-temperature mechanical behavior of L1
2-Ni3Al. Mishima et al. [14] 
investigated the eﬀect of ternary addition of several fourth, ﬁfth, and sixth group elements 
on the high-temperature mechanical response of polycrystalline Ni 3Al and reported that 
4 at% Ti addition, which substituted at Al si tes, reached the peak strength of about 560 
MPa and 2 at% Nb substitution obtained the peak strength of about 620 MPa at 600 °C. It 
has been generally accepted that Co and Cr addition in Ni-based superalloys strengthen 
the γ matrix [1]. However, in this research, comparing the compression results of poly-
crystalline Ni
3Al from Lopez and Hancock [17] with CY2 and CY3, a noticeable strength 
enhancement was obtained by adding Co and Cr in Ni 3Al. Furthermore, comparing the 
three alloys studied in the research, the Ti or Nb alloying addition showed a signi ﬁcant 
increase in peak strength. 
 
Figure 6. Temperature dependence of strengths. 
Table 4. Yield strengths of the studied alloys at diﬀerent temperatures. 
(°C) CY1 (MPa) CY2 (MPa) CY3 (MPa) 
500 324.7 420.5 587.7 
600 391.2 510.6 655.9 
700 426.5 677.7 690.4 
800 511.5 617.6 685.2 
900 417.1 407.0 433.7 
1000 259.5 300.9 288.7 
Figure 6. Temperature dependence of strengths.
Comparing the yield stress of CY1, the ones of CY2 are 30% higher at 500 ◦C, 31%
higher at 600 ◦C, and 59% higher at 700 ◦C. In addition, the yield stresses of CY3 are 81%
higher at 500 ◦C, 68% higher at 600 ◦C, and 62% higher at 700 ◦C. The peak strengths for
CY1, CY2, and CY3 alloys were 426 MPa, 678 MPa, and 690 MPa, respectively. Our results
revealed that the fifth alloying addition produced a significant enhancement in the yield
stress while exhibiting anomalous yielding behavior, which was reported in numerous
studies about the high-temperature mechanical behavior of L12-Ni3Al. Mishima et al. [14]
investigated the effect of ternary addition of several fourth, fifth, and sixth group elements
on the high-temperature mechanical response of polycrystalline Ni3Al and reported that 4
at% Ti addition, which substituted at Al sites, reached the peak strength of about 560 MPa
and 2 at% Nb substitution obtained the peak strength of about 620 MPa at 600 ◦C. It has
been generally accepted that Co and Cr addition in Ni-based superalloys strengthen the γ
matrix [1]. However, in this research, comparing the compression results of polycrystalline
Ni3Al from Lopez and Hancock [17] with CY2 and CY3, a noticeable strength enhancement
was obtained by adding Co and Cr in Ni 3Al. Furthermore, comparing the three alloys
studied in the research, the Ti or Nb alloying addition showed a significant increase in
peak strength.
During the high-temperature compression deformation up to the peak temperature,
the yield strength of the alloys depends on the solid solution strengthening (∆σSS), grain
boundary strengthening by the Hall–Petch effect (∆σgb), ordering strengthening (∆σOS),
and cross-slip-induced strengthening (∆σKW) [34–36], as follows:
σy = ∆σSS + ∆σgb + ∆σOS + ∆σKW. (1)
We evaluated the contribution of each strengthening mechanism at peak temperature
(800 ◦C for CY1 and 700 ◦C for CY2 and CY3) using Equation (1) above. The contribution
of solid solution strengthening, ∆σSS, was calculated using the pySSpredict, a Python-
based toolkit that automates the high-throughput calculations of solid solution strength of
complex concentrated alloys based on the solid solution strengthening and edge dislocation
models for FCC and BCC alloys [37,38]. The calculated values of ∆σSS are 20 MPa, 24 MPa,
and 32 MPa for the CY1, CY2, and CY3 alloys, respectively. Nb produced the most
prominent strength enhancement via the solid solution strengthening, followed by Ti
addition, which was consistent with the measurement of lattice constants through XRD.

## Page 8

Materials 2024, 17, 2280 8 of 12
The grain boundary strengthening effect can be expressed as the Hall–Petch relation-
ship [39]:
∆σgb = σ0 + kd−1, (2)
where σ0 is the lattice friction stress, k is the Hall–Petch coefficient, and d is the average
grain size. Since the average grain size of our alloy is ≈500 µm for CY1, ≈850 µm for
CY2, and ≈330 µm for CY3, the effect of grain boundary strengthening is expected to be
relatively small in all alloys.
In addition to the solid solution strengthening and grain boundary strengthening, the
planar fault energy was assumed to contribute to the significant strength enhancement [40].
The strengthening effect of the L1 2 phase is mainly due to the ordering strengthening
caused by adding different elements. Since the bonding force between atoms of different
elements is greater than between atoms of the same elements, the ordered arrangement of
atoms of different types will contribute to a higher strength for the ordered alloy, according
to the expression of the ordering strengthening (∆σOS) [41]:
∆σOS = M0.81 γAPB
2b
 3π f
8
1/2
, (3)
where M is the Taylor factor, γAPB is APBE, b is the burgers vector, and f is the volume
fraction of the L12 phase. Since APBE dominates the γ′-shearing event by both weakly-
coupled dislocations and strongly-coupled dislocations, higher APBE would enhance the
overall strengthening of the L12-ordered phase before the peak temperatures. Chandran
and Sondhi [42] investigated the effect of Ti and Nb on the Ni3Al by DFT calculations. They
reported that Nb and Ti could significantly increase APBE but the Nb effect is stronger with
Ni3Al1−xNbx with x ≈ 0.20. This research used a DFT method, developed by Crudden
et al. [22], to estimate the APBE of the studied alloys. It is assumed that the change in APBE
can be determined using a linear superposition of the effects of the individual alloying
elements according to the equation
∆EAPB = E0
APB + ∑
n
i (kixi), (4)
where xi is the concentration in at% of the solute element i in the L12-ordered phase and
ki is the coefficient for change in APBE, listed in Table 5. E0
APB is the APBE for Ni 3Al
(193 ± 13 mJ m−2) measured using TEM by Kruml et al. [ 43]. The APBE of the CY1,
CY2, and CY3 alloys were 153 mJ/mol, 183 mJ/mol, and 196 mJ/mol, respectively. The
calculated contribution values to yield strength from ordering strengthening, ∆σOS, are
81 MPa, 97 MPa, and 104 MPa for CY1, CY2, and CY3, respectively. The calculation result
indicates that adding Ti or Nb results in an obvious increase in the APBE and, thus, the
contribution of ordering strengthening in the studied alloys.
Table 5. Coefficients for change in APBE [22].
Coefficient Co Cr Ti Nb
ki (mJ m−2/at.pct) −1.50 −5.00 15.00 21.40
With increasing temperature, the strength of the L12-ordered phase increases, which is
controlled by the thermally activated cross slip of dislocations from {111} to {010} planes.
The number of dislocations in the L12 phase increased as plastic deformation was induced,
resulting in the difficulty in dislocation movement along the L1 2 structure. This study
estimated the contribution of cross-slip-induced strengthening (∆σKW) by subtracting the
solid solution strengthening and the ordering strengthening from the total peak yield
strength, summarized in Figure 7. The values obtained for cross-slip-induced strengthening
are 325 MPa, 557 MPa, and 554 MPa for CY1, CY2, and CY3, respectively. Therefore, it was
assumed that the cross-slip-induced strengthening dominated the peak yield strength and

## Page 9

Materials 2024, 17, 2280 9 of 12
the significant strength enhancement was achieved by adding the fifth elements, namely Ti
or Nb. Yu et al. [13] have investigated the effect of alloying element on dislocation in Ni3Al
using the DFT method and reported that Ti addition could reduce the cross-slip activation
enthalpy and facilitate the cross-slip process to form dislocation locks, thus resulting in
more difficult dislocation movement and higher flow stress in the anomalous temperature
regime of Ni3Al. According to our experimental results, Nb can provide a similar level of
cross-slip-induced strengthening as Ti in the NiCoCrAl alloy system.
Materials 2024, 17, x FOR PEER REVIEW 9 of 12 
 
 
Table 5. Coeﬃcients for change in APBE [22]. 
Coefficient Co Cr Ti Nb 
ki (mJ m−2/at.pct) −1.50 −5.00 15.00 21.40 
With increasing temperature, the strength of the L12-ordered phase increases, which 
is controlled by the thermally activated cross slip of dislocations from {111} to {010} planes. 
The number of dislocations in the L1
2 phase increased as plastic deformation was induced, 
resulting in the diﬃculty in dislocation movement along the L12 structure. This study es-
timated the contribution of cr oss-slip-induced strengthening ( 𝛥𝜎KW) by subtracting the 
solid solution strengthening and the orderin g strengthening from the total peak yield 
strength, summarized in Figure 7. The values obtained for cross-slip-induced strengthen-
ing are 325 MPa, 557 MPa, and 554 MPa for CY1, CY2, and CY3, respectively. Therefore, 
it was assumed that the cross-slip-induc ed strengthening dominated the peak yield 
strength and the signi ﬁcant strength enhancement was achieved by adding the ﬁfth ele-
ments, namely Ti or Nb. Yu et al. [13] have investigated the e ﬀect of alloying element on 
dislocation in Ni3Al using the DFT method and reported that Ti addition could reduce the 
cross-slip activation enthalpy and facilitate the cross-slip process to form dislocation locks, 
thus resulting in more diﬃcult dislocation movement and higher ﬂow stress in the anom-
alous temperature regime of Ni3Al. According to our experimental results, Nb can provide 
a similar level of cross-slip-induced strengthening as Ti in the NiCoCrAl alloy system. 
 
Figure 7. Strength contribution of diﬀerent strengthening mechanisms. 
In addition to the strength enhancement, a slight decrease in the peak temperature 
for the positive temperature dependence was observed in the quinary CY2 and CY3 alloys. 
This phenomenon was also observed in previous studies with ternary alloying addition 
in Ni
3Al alloys and the peak temperature would further decrease with increasing alloying 
addition of the ternary elemen ts [14,16,17]. Lopez and Hanc ock [17] suggested that the 
decrease in peak temperature was due to the strong in ﬂuence of Ti on the onset of cube 
slip. Kruml et al. [43] proposed and veriﬁed that increasing the CSF energy increased the 
strength up to the peak temperature and decreased the strength above the peak tempera-
ture, thus lowering the peak temperature. According to the CSF energies calculated by Yu 
et al. [13] using the DFT method, Ti was found to increase the CSF energy, consistent with 
the lower peak temperature observed in this research. 
From a technical point of view, the peak temperature is usually at the highest tem-
perature where the materials are used [44]. Ni-based superalloys [45–48] and L1
2-strength-
ened HEAs [49–52] have exhibited anomalou s positive temperature dependence of 
Figure 7. Strength contribution of different strengthening mechanisms.
In addition to the strength enhancement, a slight decrease in the peak temperature for
the positive temperature dependence was observed in the quinary CY2 and CY3 alloys. This
phenomenon was also observed in previous studies with ternary alloying addition in Ni3Al
alloys and the peak temperature would further decrease with increasing alloying addition
of the ternary elements [14,16,17]. Lopez and Hancock [17] suggested that the decrease in
peak temperature was due to the strong influence of Ti on the onset of cube slip. Kruml
et al. [ 43] proposed and verified that increasing the CSF energy increased the strength
up to the peak temperature and decreased the strength above the peak temperature, thus
lowering the peak temperature. According to the CSF energies calculated by Yu et al. [13]
using the DFT method, Ti was found to increase the CSF energy, consistent with the lower
peak temperature observed in this research.
From a technical point of view, the peak temperature is usually at the highest tempera-
ture where the materials are used [44]. Ni-based superalloys [45–48] and L12-strengthened
HEAs [49–52] have exhibited anomalous positive temperature dependence of strength
at intermediate temperatures followed by a decrease in yield strength with increasing
temperatures. The decrease in strength has been explained mainly by degradation of
microstructures and transition of deformation mechanisms. Since the L12-ordered single
phase microstructure in our systematically designed alloys was thermodynamically stable
at the peak temperatures, the possibility of a microstructure degradation has been ruled
out for the cause of the decreased yield strength above the peak temperatures. Our results
revealed the intrinsic capability of the multicomponent L12-ordered phases and suggested
that the difference in the yield strength before the peak temperatures was significantly
influenced by the difference in the contribution of cross-slip-induced strengthening, which
was strongly associated with the alloying compositions of the multicomponent L12-ordered
phase. This work has shed light on the significance of cross-slip-induced strengthening in
the multicomponent L12-ordered phase and can serve as a guideline for the future design
of L12-strengthened HEAs.
According to the DFT calculation result of activation energy of the cross-slip process
by Yu et al. [13], Re, W, and Ta possess a higher probability of cross-slip process than the
alloying addition of Ti and therefore, these elements are predicted to be more efficient in

## Page 10

Materials 2024, 17, 2280 10 of 12
strengthening the Ni3Al phase, which is worthy of further experimental evaluation and
investigation. In addition, further analysis of the deformed samples will be carried out
to elucidate the relationship between the compositions of the L12-ordered phase and the
underlying deformation mechanism.
4. Conclusions
Three multicomponent L12-ordered single phase alloys were designed and fabricated
to investigate the effect of multicomponent alloying conditions on the yielding behavior
from 500 ◦C to 1000 ◦C. The primary conclusions can be summarized as follows.
• Multicomponent L12-ordered alloys, designed using the Calphad Thermo-Calc© soft-
ware, were successfully fabricated via VAM and optimized heat treatment. Both
microstructure and crystal structure analysis confirmed the formation of L12-ordered
single phase, demonstrating that ThermoCalc is a powerful software for intermetallic
alloy design;
• The multicomponent L12-ordered alloys exhibited a positive temperature dependence.
The addition of Ti or Nb significantly increased strength up to the peak temperature;
• The addition of Ti or Nb enhanced the solid solution strengthening, ordering strength-
ening, and cross-slip-induced strengthening. The cross-slip-induced strengthening
was the most dominant strengthening mechanism in L12-ordered alloys and Ti or Nb
addition remarkably increased the contribution of cross-slip-induced strengthening.
Author Contributions: Conceptualization, S.M., H.M., A.-C.Y. and Y.Y.-M.; methodology, H.M.,
A.-C.Y. and S.M.; software, C.-Y.W. and S.M.; validation, C.-Y.W.; formal analysis, C.-Y.W., Y.T. and
S.M.; investigation, C.-Y.W., Y.T. and S.M.; resources, Y.T. and Y.Y.-M.; data curation, C.-Y.W.; writing—
original draft preparation, C.-Y.W.; writing—review and editing, S.M. and Y.Y.-M.; visualization,
C.-Y.W.; supervision, H.M., A.-C.Y., S.M. and Y.Y.-M.; project administration, Y.Y.-M.; funding
acquisition, Y.Y.-M. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data are contained within the article.
Conflicts of Interest: The authors declare no conflicts of interest.
References
1. Reed, R.C. The Superalloys: Fundamentals and Applications ; Cambridge University Press: Cambridge, UK, 2008.
2. Jien-Wei, Y. Recent progress in high entropy alloys. Ann. Chim. Sci. Mat. 2006, 31, 633–648.
3. He, J.; Wang, H.; Huang, H.; Xu, X.; Chen, M.; Wu, Y.; Liu, X.; Nieh, T.; An, K.; Lu, Z. A precipitation-hardened high-entropy alloy
with outstanding tensile properties. Acta Mater. 2016, 102, 187–196. [CrossRef]
4. Shafiee, A.; Moon, J.; Kim, H.S.; Jahazi, M.; Nili-Ahmadabadi, M. Precipitation behaviour and mechanical properties of a new
wrought high entropy superalloy. Mater. Sci. Eng. A 2019, 749, 271–280. [CrossRef]
5. Liu, L.; Zhang, Y.; Han, J.; Wang, X.; Jiang, W.; Liu, C.T.; Zhang, Z.; Liaw, P .K. Nanoprecipitate-strengthened high-entropy alloys.
Adv. Sci. 2021, 8, 2100870. [CrossRef] [PubMed]
6. Yang, T.; Zhao, Y.; Liu, W.; Zhu, J.; Kai, J.; Liu, C. Ductilizing brittle high-entropy alloys via tailoring valence electron concentrations
of precipitates by controlled elemental partitioning. Mater. Res. Lett. 2018, 6, 600–606. [CrossRef]
7. Tong, Y.; Chen, D.; Han, B.; Wang, J.; Feng, R.; Yang, T.; Zhao, C.; Zhao, Y.; Guo, W.; Shimizu, Y. Outstanding tensile properties
of a precipitation-strengthened FeCoNiCrTi0. 2 high-entropy alloy at room and cryogenic temperatures. Acta Mater. 2019, 165,
228–240. [CrossRef]
8. Yang, T.; Zhao, Y.; Tong, Y.; Jiao, Z.; Wei, J.; Cai, J.; Han, X.; Chen, D.; Hu, A.; Kai, J. Multicomponent intermetallic nanoparticles
and superb mechanical behaviors of complex alloys. Science 2018, 362, 933–937. [CrossRef] [PubMed]
9. Yeh, A.-C.; Chang, Y.-J.; Tsai, C.-W.; Wang, Y.-C.; Yeh, J.-W.; Kuo, C.-M. On the solidification and phase stability of a Co-Cr-Fe-Ni-Ti
high-entropy alloy. Metall. Mater. T rans. A 2014, 45, 184–190. [CrossRef]
10. Yang, T.; Zhao, Y.; Li, W.; Yu, C.; Luan, J.; Lin, D.; Fan, L.; Jiao, Z.; Liu, W.; Liu, X. Ultrahigh-strength and ductile superlattice
alloys with nanoscale disordered interfaces. Science 2020, 369, 427–432. [CrossRef]

## Page 11

Materials 2024, 17, 2280 11 of 12
11. Long, F.; Baik, S.-I.; Chung, D.-W.; Xue, F.; Lass, E.A.; Seidman, D.N.; Dunand, D.C. Microstructure and creep performance of a
multicomponent co-based L12–ordered intermetallic alloy. Acta Mater. 2020, 196, 396–408. [CrossRef]
12. Yoo, M. On the theory of anomalous yield behavior of Ni/sub 3/Al-Effect of elastic anisotropy. Scr. Metall. 1986, 20, 915–920.
[CrossRef]
13. Yu, X.-X.; Wang, C.-Y. Effect of alloying element on dislocation cross-slip inγ′-Ni3Al: A first-principles study. Philos. Mag. 2012,
92, 4028–4039. [CrossRef]
14. Mishima, Y.; Ochiai, S.; Yodogawa, M.; Suzuki, T. Mechanical properties of Ni 3Al with ternary addition of transition metal
elements. T rans. Jpn. Inst. Met. 1986, 27, 41–50. [CrossRef]
15. Vamsi, K.; Karthikeyan, S. Effect of off-stoichiometry and ternary additions on planar fault energies in Ni3Al. Superalloys 2012,
2012, 521–530.
16. Karnthaler, H.; Mühlbacher, E.T.; Rentenberger, C. The influence of the fault energies on the anomalous mechanical behaviour of
Ni3Al alloys. Acta Mater. 1996, 44, 547–560. [CrossRef]
17. Lopez, J.; Hanock, G. The effects of non-stoichiometry and titanium additions on the mechanical behaviour of Ni3Al (γ′). Phys.
Status Solidi (A) 1970, 2, 469–474. [CrossRef]
18. Thornton, P .; Davies, R.; Johnston, T. The temperature dependence of the flow stress of theγ′ phase based upon Ni3Al. Metall.
T rans.1970, 1, 207–218. [CrossRef]
19. Mishima, Y.; Ochiai, S.; Hamao, N.; Yodogawa, M.; Suzuki, T. Solid solution hardening of Ni3Al with ternary additions. T rans.
Jpn. Inst. Met. 1986, 27, 648–655. [CrossRef]
20. Vamsi, K.; Karthikeyan, S. Modeling APB energies in multicomponent Ni-base superalloys. Intermetallics 2021, 132, 107124.
[CrossRef]
21. Dodaran, M.; Ettefagh, A.H.; Guo, S.; Khonsari, M.; Meng, W.; Shamsaei, N.; Shao, S. Effect of alloying elements on theγ’antiphase
boundary energy in Ni-base superalloys. Intermetallics 2020, 117, 106670. [CrossRef]
22. Crudden, D.; Mottura, A.; Warnken, N.; Raeisinia, B.; Reed, R. Modelling of the influence of alloy composition on flow stress in
high-strength nickel-based superalloys. Acta Mater. 2014, 75, 356–370. [CrossRef]
23. Gorbatov, O.I.; Lomaev, I.; Gornostyrev, Y.N.; Ruban, A.V .; Furrer, D.; Venkatesh, V .; Novikov, D.; Burlatsky, S. Effect of
composition on antiphase boundary energy in Ni 3 Al based alloys: Ab initio calculations. Phys. Rev. B 2016, 93, 224106.
[CrossRef]
24. Wang, H.-P .; Sluiter, M.; Kawazoe, Y. Prediction of the Effect of Ti on the (111) and (100) Antiphase Boundary Energy in Ni3Al.
Mater. T rans. JIM1999, 40, 1301–1305. [CrossRef]
25. Barba, D.; Egan, A.; Utada, S.; Gong, Y.; Tang, Y.; Mazanova, V .; Mills, M.; Reed, R. Deformation Mechanisms Rationalisation to
Design for Creep Resistance in Polycrystalline Ni-Based Superalloys. Metall. Mater. T rans. A 2023, 54, 1886–1901. [CrossRef]
26. Feng, L.; Rao, Y.; Ghazisaeidi, M.; Mills, M.J.; Wang, Y. Quantitative prediction of Suzuki segregation at stacking faults of the
γ’phase in Ni-base superalloys. Acta Mater. 2020, 200, 223–235. [CrossRef]
27. Rao, Y.; Smith, T.M.; Mills, M.; Ghazisaeidi, M. Segregation of alloying elements to planar faults inγ’-Ni3Al. Acta Mater. 2018, 148,
173–184. [CrossRef]
28. Egan, A.J.; Xue, F.; Rao, Y.; Sparks, G.; Marquis, E.; Ghazisaeidi, M.; Tin, S.; Mills, M.J. Local phase transformation strengthening
at Microtwin boundaries in nickel-based superalloys. Acta Mater. 2022, 238, 118206. [CrossRef]
29. Ardell, A.J. Precipitation hardening. Metall. T rans. A 1985, 16, 2131–2165. [CrossRef]
30. Andersson, J.-O.; Helander, T.; Höglund, L.; Shi, P .; Sundman, B. Thermo-Calc & DICTRA, computational tools for materials
science. Calphad 2002, 26, 273–312.
31. Yu, Y.; Zhou, J.; Chen, J.; Zhou, H.; Guo, C.; Guo, B. Synthesis of nanocrystalline Ni 3Al by mechanical alloying and its
microstructural characterization. J. Alloys Compd. 2010, 498, 107–112. [CrossRef]
32. De Luca, A.; Kenel, C.; Griffiths, S.; Joglekar, S.S.; Leinenbach, C.; Dunand, D.C. Microstructure and defects in a Ni-Cr-Al-Ti
γ/γ’model superalloy processed by laser powder bed fusion. Mater. Des. 2021, 201, 109531. [CrossRef]
33. Christofidou, K.; Jones, N.; Pickering, E.; Flacau, R.; Hardy, M.C.; Stone, H. The microstructure and hardness of Ni-Co-Al-Ti-Cr
quinary alloys. J. Alloys Compd. 2016, 688, 542–552. [CrossRef]
34. Kozar, R.; Suzuki, A.; Milligan, W.; Schirra, J.; Savage, M.; Pollock, T. Strengthening mechanisms in polycrystalline multimodal
nickel-base superalloys. Metall. Mater. T rans. A 2009, 40, 1588–1603. [CrossRef]
35. Goodfellow, A. Strengthening mechanisms in polycrystalline nickel-based superalloys. Mater. Sci. T echnol. 2018, 34, 1793–1808.
[CrossRef]
36. Li, Z.; Fu, L.; Peng, J.; Zheng, H.; Ji, X.; Sun, Y.; Ma, S.; Shan, A. Improving mechanical properties of an FCC high-entropy alloy by
γ′ and B2 precipitates strengthening. Mater. Charact. 2020, 159, 109989. [CrossRef]
37. Wen, D.; Titus, M.S. pySSpredict: A python-based solid-solution strength prediction toolkit for complex concentrated alloys.
Comput. Mater. Sci. 2023, 220, 111977. [CrossRef]
38. Varvenne, C.; Luque, A.; Curtin, W.A. Theory of strengthening in fcc high entropy alloys. Acta Mater. 2016, 118, 164–176.
[CrossRef]
39. Schulson, E.; Weihs, T.; Viens, D.; Baker, I. The effect of grain size on the yield strength of Ni3Al. Acta Metall. 1985, 33, 1587–1591.
[CrossRef]

## Page 12

Materials 2024, 17, 2280 12 of 12
40. Goodfellow, A.; Galindo-Nava, E.; Schwalbe, C.; Stone, H. The role of composition on the extent of individual strengthening
mechanisms in polycrystalline Ni-based superalloys. Mater. Des. 2019, 173, 107760. [CrossRef]
41. Seidman, D.N.; Marquis, E.A.; Dunand, D.C. Precipitation strengthening at ambient and elevated temperatures of heat-treatable
Al (Sc) alloys. Acta Mater. 2002, 50, 4021–4035. [CrossRef]
42. Chandran, M.; Sondhi, S. First-principle calculation of APB energy in Ni-based binary and ternary alloys. Model. Simul. Mater. Sci.
Eng. 2011, 19, 025008. [CrossRef]
43. Kruml, T.; Conforto, E.; Piccolo, B.L.; Caillard, D.; Martin, J. From dislocation cores to strength and work-hardening: A study of
binary Ni3Al. Acta Mater. 2002, 50, 5091–5101. [CrossRef]
44. Nembach, E. The high temperature peak of the yield strength of γ′-strengthened superalloys. Mater. Sci. Eng. A 2006, 429,
277–286. [CrossRef]
45. Zhang, H.; Wang, Q.; Gong, X.; Wang, T.; Zhang, W.; Chen, K.; Wang, C.; Liu, Y.; Wang, Q. Dependence on temperature of
compression behavior and deformation mechanisms of nickel-based single crystal CMSX-4. J. Alloys Compd. 2021, 866, 158878.
[CrossRef]
46. MacLachlan, D.; Knowles, D. Modelling and prediction of the stress rupture behaviour of single crystal superalloys. Mater. Sci.
Eng. A 2001, 302, 275–285. [CrossRef]
47. Wang, G.; Liu, J.; Liu, J.; Wang, X.; Zhou, Y.; Sun, X.; Zhang, H.; Jin, T. Temperature dependence of tensile behavior and
deformation microstructure of a Re-containing Ni-base single crystal superalloy. Mater. Des. 2017, 130, 131–139. [CrossRef]
48. Wang, T.; Zhang, H.; Liu, C.; Gong, X.; Pei, Y.; Zou, Y.; Liu, Y.; Wang, Q. Effect of temperature on tensile behavior, fracture
morphology and deformation mechanisms of Nickel-based single crystal CMSX-4. J. Alloys Compd. 2022, 912, 165175. [CrossRef]
49. Daoud, H.; Manzoni, A.; Wanderka, N.; Glatzel, U. High-temperature tensile strength of Al 10 Co 25 Cr 8 Fe 15 Ni 36 Ti 6
compositionally complex alloy (high-entropy alloy). JOM 2015, 67, 2271–2277. [CrossRef]
50. Zhao, Y.; Yang, T.; Li, Y.; Fan, L.; Han, B.; Jiao, Z.; Chen, D.; Liu, C.; Kai, J. Superior high-temperature properties and deformation-
induced planar faults in a novel L12-strengthened high-entropy alloy. Acta Mater. 2020, 188, 517–527. [CrossRef]
51. Yuan, J.; Wang, Z.; Jin, X.; Han, P .; Qiao, J. L12-strengthened heterostructure high-entropy alloys with ultra-high strength over a
wide temperature range. Mater. Sci. Eng. A 2022, 853, 143712. [CrossRef]
52. Gao, L.; Wu, Y.; An, N.; Chen, J.; Liu, X.; Bai, R.; Hui, X. Nanoscale L12 phase precipitation induced superb ambient and high
temperature mechanical properties in Ni–Co–Cr–Al system high-entropy superalloys. Mater. Sci. Eng. A 2024, 898, 145995.
[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
