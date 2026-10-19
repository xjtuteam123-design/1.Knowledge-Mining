# metals-14-00590-v2

<!-- source: D:\总文献\metals-14-00590-v2.pdf -->
<!-- file_sha256: fc36449a91b755dc80e3a78efd1dd1a7e9f2f9ccbea36ddd803f922782545117 -->

## Page 1

Citation: Zhou, D.; Shi, C.; Wang, C.;
Sheng, R.; Li, W.; Tong, Y. Tensile
Properties of a Non-Equiatomic
Ni–Co–V Medium Entropy Alloy at
Cryogenic Temperature. Metals 2024,
14, 590. https://doi.org/10.3390/
met14050590
Academic Editor: Cristian Ciobanu
Received: 10 April 2024
Revised: 30 April 2024
Accepted: 15 May 2024
Published: 17 May 2024
Copyright: © 2024 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
metals
Article
Tensile Properties of a Non-Equiatomic Ni–Co–V Medium
Entropy Alloy at Cryogenic Temperature
Dawei Zhou 1, Caijuan Shi 2,*, Caixia Wang 1, Ruixin Sheng 1, Weidong Li 3,* and Yang Tong1,*
1 Institute for Advanced Studies in Precision Materials, Yantai University, Yantai 264005, China;
calawayzhou@s.ytu.edu.cn (D.Z.); wangcaixia@s.ytu.edu.cn (C.W.); shengruixin@s.ytu.edu.cn (R.S.)
2 Synchrotron Radiation Facility, Institute of High Energy Physics, Chinese Academy of Sciences,
Beijing 100049, China
3 Beijing Advanced Innovation Center for Materials Genome Engineering, University of Science and
Technology Beijing, Beijing 100083, China
* Correspondence: shicj@ihep.ac.cn (C.S.); wli20@utk.edu (W.L.); yt1@ytu.edu.cn (Y.T.)
Abstract: The development of strong and ductile alloys for application in cryogenic temperatures
has long been sought after. In this work, we have developed a face-centered cubic Ni10Co56.5V33.5
multi-principal element alloy (MPEA) that exhibits a balanced combination of high strength and
good ductility at 77 K, based on the considerations of large local lattice distortion (LLD) and low
stacking fault energy. The small-grained Ni10Co56.5V33.5 MPEA exhibits a yield strength of 1400 MPa
and an ultimate tensile strength of 1890 MPa, while preserving a good ductility of 23%. Moreover,
precession electron diffraction and transmission electron microscopy revealed multiple deformation
mechanisms, including wavy dislocations, atypically severely twisted dislocation bands, hierarchical
stacking faults, and deformation twins, which are implicated in the alloy’s outstanding mechanical
performance. These insights offer a strategic guide for the design of strong and ductile alloys,
particularly for utilization in extreme environments.
Keywords: multi-principal element alloy; tensile properties; transmission electron microscopy;
density functional theory; deformation mechanism
1. Introduction
The development of multi-principal element alloys (MPEAs), a novel category of solid-
solution alloys with multiple elements in equimolar or near-equimolar proportions [1,2],
has fundamentally transformed alloy design by shifting from the corners of phase diagrams
to their central regions [ 3–6]. The new alloy design strategy has led to the discovery of
novel alloys that surpass the properties exhibited by conventional single-principal element
alloys [7–9]. Notably, a recent study by Liu et al. [9] reports a record-high fracture toughness
in the equiatomic NiCoCr MPEA at the cryogenic temperature of 20 K, 540 MPa·m½. Due
to their remarkable capacity to maintain or even enhance both strength and ductility upon
cooling to cryogenic temperatures [ 10–12], the single-phase face-centered-cubic (FCC)
MPEAs have shown a great potential for application in extreme environments. This is
particularly critical as most alloys are known to experience a reduction in toughness
at decreased temperatures, a phenomenon that becomes more pronounced within the
cryogenic temperature domain [13,14].
Driven by the practical requirements of reducing mass and energy consumption,
the design of ultra-strong and ductile MPEAs remains a continuous endeavor. However,
MPEAs with the FCC structure typically manifest low yield strength. Recently, the max-
imization of local lattice distortion (LLD) [ 15–19] has been proposed as a new strategy
for designing ultra-strong single-phase MPEAs. LLD, considered as one of the core ef-
fects in MPEAs, originates from the large atomic size mismatch among constituents in
MPEAs [3]. Sohn et al. [15] have reported that the single-phase NiCoV MPEA with a severe
Metals 2024, 14, 590. https://doi.org/10.3390/met14050590 https://www.mdpi.com/journal/metals

## Page 2

Metals 2024, 14, 590 2 of 16
LLD, exhibits an exceptional yield strength of ~1 GPa at room temperature. Theoretical
solid-solution strengthening models have been developed from the perspective of LLD.
Okamoto et al. [20] have reported that the yield stress at 0 K for the CoCrFeNiMn and its
derivative quaternary and ternary equiatomic MPEAs is solely governed by the average
static displacements of constituents. Varvenne et al. [ 21] proposed a solute-dislocation
interaction model based on the atomic volume mismatch parameter, which successfully pre-
dicted the yield strength of FCC CoCrFeNiMn and CoCrFeNi MPEAs. Therefore, increasing
LLD is critical for the design of strong MPEAs.
MPEAs with severe LLD, e.g., the equiatomic FCC NiCoV [ 15] and body-centered
cubic NbTaTiVZr [16], often exhibit dislocation-controlled deformation mechanism, and the
strength–ductility trade-off in such MPEAs is often observed due to the reduced mobility
of dislocations at lower temperatures. However, the introduction of multiple deformation
mechanisms is an effective strategy by which to enhance the ductility of MPEAs, and this
can be achieved by reducing the stacking fault energy (SFE) [ 22–24]. When the SFE is
sufficiently low, dislocation cross-slip is suppressed while dislocation decomposition and
even twinning is promoted [ 25]. The reported toughest equiatomic NiCoCr is a typical
MPEA with multiple deformation mechanisms, including planar dislocation slip, stacking
faults (SFs), and deformation twins [26,27].
The equiatomic NiCoV MPEA has garnered significant interest due to its remarkable
tensile properties at both room and cryogenic temperatures [12,15]. Yang et al. [28] have
discovered that, with the decrease of temperature, the equiatomic NiCoV MPEA exhibits
enhanced strength and ductility. They found that this equiatomic MPEA retains planar
dislocation slip as the predominant deformation mechanism at 77 K [28]. This is attributed
to its relatively low SFE and high friction stress due to large LLD, which promotes the
dissociation of full dislocations and retards dislocation motion at cryogenic temperature.
However, the equiatomic NiCoV MPEA may not be the optimal composition, especially
regarding ductility, predominantly characterized by a dislocation-controlled deformation
mechanism. Consequently, an adjustment of the Ni–Co–V atomic ratio, aimed at reducing
SFE to introduce multiple deformation mechanisms while simultaneously preserving a high
degree of LLD, emerges as a viable approach for enhancing the alloy’s mechanical perfor-
mance. In the present work, we developed a non-equiatomic Ni10Co56.5V33.5 MPEA based
on the considerations of optimizing SFE and LLD. Meanwhile, to optimize its mechanical
performance, we embarked on an investigation of the grain size impact on the tensile prop-
erties of the Ni10Co56.5V33.5 MPEA at cryogenic temperature. This study integrated both
computational predictions and experimental characterizations, facilitating a comprehensive
analysis of the MPEA’s microstructure feature and deformation mechanisms.
2. Methodology
2.1. Sample Preparation
The Ni10Co56.5V33.5 alloy was synthesized by arc melting high-purity Ni, Co, and V
metals (≥99.9%) in an atmosphere of high-purity argon. The ingot was flipped and remelted
five times to ensure compositional homogeneity before suction casting into a copper mold
with dimensions of 8 × 8 × 80 mm3. The cast rods were vacuum-sealed in a quartz tube
and homogenized at 1473 K for 24 h, followed by water quenching to preserve the high-
temperature state. The homogenized rods were then cold-rolled longitudinally from a
thickness of 8.0 to 1.5 mm, achieving a thickness reduction of 80%. Flat dog-bone-shaped
tensile specimens with a gauge length of 20 mm and a thickness of 1.5 mm were wire-cut
from the cold-rolled plate along the rolling direction. Recrystallization heat treatment was
then conducted on three tensile specimens at 1473 K for 10 min, 1373 K for 3 min and 1473 K
for 1 min, respectively, to obtain different grain sizes. Figure 1 shows the heat treatment
histories of these samples. These recrystallized tensile samples are henceforth denoted as
S1 to S3. After fine polishing the surfaces with 2000 grit sandpaper, all tensile samples
were subjected to tensile tests at a strain rate of 1 × 10−3 s−1 using an SENS CMT-5105

## Page 3

Metals 2024, 14, 590 3 of 16
10T tensile machine (Shenzhen, China) at the cryogenic temperature of 77 K in a liquid
nitrogen environment.
Figure 1. Heat treatment process in sample preparation.
2.2. Calculations
To examine LLD, first principles calculations were performed using density functional
theory (DFT) implemented in the Vienna ab initio simulation package (VASP) code [29]. The
projected augmented wave (PAW) method was employed in combination with the Perdew–
Burke–Ernzerhof (PBE) [30] generalized gradient approximation [ 31] for the exchange–
correlation potential. A Γ-centered 2 × 2 × 2 k-point grid was used for Brillouin zone
sampling. Wavefunctions were expanded in a plane–wave basis with a kinetic energy cutoff
of 350 eV , and the electronic convergence criterion was set to 1.0× 10−5 eV . Ionic positions
were relaxed until residual ionic forces were below 10−3 eV/Å. For the DFT calculations,
a supercell containing 108 atoms was constructed based on the special quasi-random
structure (SQS) approach [32].
2.3. Characterization
High-energy X-ray diffraction (HEXRD) analysis was conducted for phase identifi-
cation at Beamline 3W1A, Beijing Synchrotron Radiation Research Institute. The incident
X-ray energy was set to 60.16 keV , corresponding to a wavelength of 0.2061 Å. Diffraction
data collection was preformed using a 2-dimensional detector positioned 862 mm away
from the sample stage along the X-ray beam path.
For microstructural characterization, a field-emission scanning electron microscope
(SEM, TESCAN AMBER, Brno, Czech Republic) equipped with an electron backscattered
diffraction probe (EBSD, OXFORD VEGA, Abingdon, UK) and a transmission electron
microscope (TEM, Talos F200X G2) were utilized. Precession electron diffraction (PED)
analysis, undertaken to achieve nanoscale EBSD resolution, was conducted using a TEM
(FEI Tecnai F30, Waltham, MA, USA) equipped with a NanoMEGAS detector. The prepara-
tion of EBSD samples involved grinding with sandpapers of grit ranging from 800 to 2000,
followed by mechanical polishing with a 0.05 µm SiO2 suspension and electropolishing in
a solution with a volume ratio of H2SO4 to CH3OH of 1:4. TEM samples were prepared
using a twin-jet technique with a 10% volume fraction perchloric acid alcohol solution,
applying a voltage of 20 V and maintaining a temperature of 263 K.

## Page 4

Metals 2024, 14, 590 4 of 16
2.4. AI tool
Al tool was utilized solely for the purpose of grammar and syntax checking in the
manuscript. The originality, validity, and integrity of the content of their manuscript was
ensured without any assistance from AI tool.
3. Results
3.1. Microstructure
Figure 2a shows the calculated ternary phase diagram for the Ni–Co–V system at
1373 K. A red dot near the edge of the single FCC region marks the composition of the alloy
under investigation. The choice of composition aims to achieve a balance between ductility
and strength. Vanadium effectively enhances strength in Ni-based alloys [ 33] while the
incorporation of Co into Ni decreases the SFE [ 34], promoting the formation of SFs and
deformation twins. Figure 2b presents the HEXRD profiles of the selected alloy subjected
to various recrystallization heat treatments. The predominant phase is observed to have
an FCC structure and a minor fraction of the σ phase is identified close to the results of
the thermodynamic calculation in Figure 2a. Quantitative XRD phase analysis reveals that
the volume fraction of the σ phase is rather small, with 2.0%, 3.0% and 2.7% for S1, S2 and
S3, respectively.
Figure 2. (a) Ternary phase diagram of Ni–Co–V at 1373 K. Reprinted with permission from ref. [35].
Copyright 2019, Elsevier Ltd. The red dot indicates the studied Ni10Co56.5V33.5 MPEA. (b) HEXRD
profiles of samples after different recrystallization heat treatment. The inset is an enlarged view of
diffraction peaks of the minor σ phase.
Figure 3 shows the inverse pole figures (IPFs) of the recrystallized samples. All sam-
ples were fully recrystallized with an equiaxed grain structure. However, the grain size
distribution varies dramatically between the S1 sample and the others. The S1 sample
exhibits a relatively homogeneous grain size, whereas samples S2 and S3 display a hetero-
geneous microstructure characterized by a mix of large and small grains, as demonstrated
by the grain size distribution histograms in Figure 3. The average grain sizes are 16.0 µm
for sample S1, 5.1 µm for sample S2 and 4.5 µm for sample S3. Additionally, a significant
number of annealing twins is observed in the S1 sample. In contrast, the density of such
annealing twins significantly decreases in the S2 and S3 samples.
We further examined the σ phase in these recrystallized samples. TEM analysis
of the σ phase in the large-grained S1 sample is presented in Figure 4. The high angle
annular dark field (HAADF) image in Figure 4a reveals that small spherical σ precipitates
predominantly exist within the grain interiors with an average diameter of ~130 nm, while
negligible σ precipitates are sparsely distributed at grain boundaries. The high-resolution
transmission electron microscope (HRTEM) image in Figure 4b, taken along the [001] zone
axis of the σ phase, further reveals a semi-coherent interface between small σ precipitate
and the matrix. The fast Fourier transform (FFT) image in the inset of Figure 4b shows a

## Page 5

Metals 2024, 14, 590 5 of 16
typical diffraction pattern of the σ phase. Additionally, the selected area electron diffraction
(SAED) pattern (Figure 4c) closely matches the calculated diffraction pattern of the typical
σ phase, Co 2V3 (Figure 4d), which has a tetragonal structure with a space group of P
42/m n m. Notably, the composition of the σ phase in our Ni–Co–V samples deviate
from the chemical stoichiometry of Co 2V3, resulting in some ordering diffraction spots
(within the yellow circle in Figure 4c) that violate the ideal extinction conditions. Figure 4e
displays an enlarged view of the region highlighted in Figure 4a, showing the distribution
of σ precipitates within a grain. It can be seen that spherical σ precipitates form along
dislocation, revealing a dislocation-assisted precipitation behavior. Moreover, the energy-
dispersive X-ray spectroscopy (EDX) mapping (Figure 4f–h) shows these σ precipitates are
enriched in V and depleted in Ni and Co.
Figure 3. IPFs of recrystallized S1 (a), S2 (b) and S3 (c) samples. Grain size distribution of recrystallized
S1 (d), S2 (e) and S3 (f) samples.
Figure 4. Precipitation behavior in large-grained S1 sample. ( a) HAADF image showing spatial
distribution of σ precipitates. ( b) HRTEM image detailing the interface between matrix and σ
precipitate. (c) SAED pattern of σ precipitate along the [001] zone axis, which closely matches the
calculated diffraction pattern (d) of a typical σ phase, Co2V3. The yellow circles highlight the violation
of the extinction diffraction condition. (e) HAADF image showing dislocation-assisted σ precipitation
behavior within grains. (f–h) Elemental distribution of Ni, Co, V in the region shown in (e).

## Page 6

Metals 2024, 14, 590 6 of 16
The σ phase in the small-grained samples were also examined. Figure 5a shows
a typical spatial distribution of σ precipitates in the small-grained sample. This clearly
demonstrates that σ precipitates are predominantly located at grain boundaries, with an
average diameter of ~455 nm, and some smaller σ precipitates are found within the grains,
with an average diameter of ~180 nm. Furthermore, some nanoscale annealing twins, with
an average width of ~306 nm, are formed in these small grains, contrasting with relatively
large annealing twins in sample S1 observed by EBSD. These observations demonstrate
that a decrease of grain size can reduce the width of annealing twins. The EDX mapping
in Figure 5b–d reveals that the white σ spherical particles in Figure 5a are enriched in
V and depleted in Ni and Co. A quantitative line scan analysis in Figure 5e reveals the
compositional difference between the matrix and σ precipitates.
Figure 5. Precipitation behavior in small-grained S3 sample. ( a) HAADF image showing spatial
distribution of σ precipitates. (b–d) EDX maps of Ni, Co, and V elements in the region shown in (a).
(e) Compositional profiles obtained by an EDX line scan along the direction indicated by the black
arrow in (a).
3.2. Local Lattice Distortion
DFT calculations were conducted to examine the LLD in the Ni10Co56.5V33.5 MPEA.
Figure 6a illustrates the stable supercell structure following the relaxation of ionic positions.
It is evident that atoms deviate from their ideal lattice positions, indicating the existence
of large LLD. We further calculated the statistical distribution of atomic distances among
the nearest neighboring atoms in the relaxed supercell, as depicted in Figure 6b. Notably,
the distances of V–V atomic pairs significantly exceed those of other atomic pairs, which
is consistent with the larger atomic radius of V compared with Ni and Co elements [36].
Therefore, V–V atomic pairs contribute most significantly to the LLD in the Ni–Co–V
MPEA. A widely-adopted parameter for quantifying LLD in MPEAs is the size mismatch
parameter [37],
δ =
r
∑
N
i=1 ci

1 − ri
.
∑
N
j=1 cjrj
2
(1)
where N, ci,j, and ri,j are the total number of constituent elements, atomic fraction, and
atomic radius of the ith or jth element, respectively. Using atomic radii in [38], we calculated
the δ (0.059) of our newly-designed Ni10Co56.5V33.5 MPEA, which is comparable with the
value (0.062) of the equiatomic NiCoV MPEA but is notably larger than that of the most
studied damage-tolerant CoCrFeNiMn (0.039) and NiCoCr (0.048) MPEAs.

## Page 7

Metals 2024, 14, 590 7 of 16
Figure 6. (a) Projection view of the relaxed supercell along [100] orientation. (b) Histogram of atomic
pair distances among the first nearest neighboring atoms.
3.3. Mechanical Properties
Figure 7a presents the engineering stress–strain curves obtained from tensile tests
conducted at 77 K. As grain size decreases from the S1 sample to S3 sample, both yield
strength and tensile strength increase, while elongation decreases. The large-grained S1
sample shows an excellent elongation of 47%, with a moderate yield strength of 841 MPa
and a high ultimate tensile strength (UTS) of 1434 MPa. Samples S2 and S3 demonstrate a
superior balance between strength and ductility. Specifically, S2 exhibits a yield strength
of 1184 MPa and a UTS of 1804 MPa, coupled with an elongation of 33.5%. Conversely,
S3 is characterized by a higher yield strength of 1400 MPa and a UTS of 1890 MPa, with a
slightly lower elongation of 23%. Figure 7b plots strain hardening rate against true strain,
revealing that all samples undergo three stages of strain hardening: a rapid decrease at the
beginning of plastic deformation, followed by a swift increase, and then a gradual decline
before fracture. The second stage is closely related to the yield stage phenomena, as shown
in the inset in Figure 7a.
Figure 7. (a) Engineering stress–strain curves. ( b) Strain hardening rate vs. true strain. Arrows
indicate the y axes of different curves.
Figure 8 plots the product of UTS and elongation against yield strength for vari-
ous MPEAs measured at 77 K. It can be seen that our newly designed Ni 10Co56.5V33.5
MPEA exhibits exceptional combination of strength and ductility at 77 K. Compared
with the equiatomic NiCoV MPEA, the yield strength of the designed Ni 10Co56.5V33.5
MPEA increases by 57.8% from 887 MPa to 1400 MPa. The mechanical performance of the
Ni10Co56.5V33.5 MPEA is better than most of the multiphase MPEAs.

## Page 8

Metals 2024, 14, 590 8 of 16
Figure 8. Yield strength vs. product of UTS and elongation of MPEAs at 77 K. The yield strength,
ultimate tensile strength, and elongation values of other MPEAs adapted from [8,10–12,27,39–70].
3.4. Fractography
Fractography of the deformed samples was examined using SEM, as shown in Figure 9.
A deep dimple structure was observed in the S1 sample. In contrast, the dimples in samples
S2 and S3 are rather small and shallow. Compared with samples S2 and S3, the formation
of the rougher facture surface in the S1 sample consumes more energy, leading to a higher
ductility. Moreover, the average dimple sizes decrease with the reduction of grain size,
aligning with the trend that ductility decreases as grain size diminishes (Figure 7a).
Figure 9. Fractography of the samples deformed at 77 K. Morphology of the fractured surface for
sample S1 (a), sample S2 (b), and Sample S3 (c).
4. Discussion
4.1. Grain Size Effect on Deformation Behavior
Figure 10a–c show the Kernal average misorientation (KAM) maps of samples S1 to
S3, which generally reflects the density of geometrically necessary dislocations. In the
S1 sample, characterized by homogeneous large grains, a high density of dislocations
is observed in most grains, indicating cooperative plastic deformation among different
grains. For samples S2 and S3, which feature heterogeneous and smaller grains, the
density of dislocations dramatically decreases, and dislocation cells, especially in large
grains, are formed. Grain reference orientation deviation (GROD) analysis was further
conducted to examine large orientation changes within grains caused by deformation, as
shown in Figure 10d–f. It is apparent that most grains in the S1 sample underwent severe
orientation changes in order to accommodate large plastic deformation, and a large amount
of low-angle grain boundaries are formed. In the small-grained S2 and S3 samples, large
GROD occurs only within large grains, whereas GROD in small grains remains minimal,
demonstrating a heterogeneous plastic deformation behavior.

## Page 9

Metals 2024, 14, 590 9 of 16
Figure 10. (a–c) KAM maps of fractured samples S1 to S3. The color bar on the left indicates the
degree of misorientation. (d–f) GROD maps. The color bar indicates the degree of orientation change
within grains.
4.2. Deformation Mechanisms
To investigate the deformation mechanisms, we conducted TEM and PED character-
izations on the fractured samples. Figure 11a shows the bright-field TEM image of the
fractured S1 sample. We observe the formation of multiple bands with varying width.
SAED analysis was also conducted to determine whether these bands are deformation
twins. The SAED pattern, shown in the inset of Figure 11a, reveals diffraction spots from
only the single FCC phase. This observation indicates that these deformation bands are
not deformation twins. Based on their longitudinal orientation, these deformation bands
can be classified as the <001> band or the < 111> band. To further confirm the nature of
these bands, PED analysis was performed on the region outlined by the blue dashed box
in Figure 11a. The IPF map in Figure 11b shows that the normal direction of the matrix
plane aligns with the [110] direction, while the normal direction of the bands significantly
deviates from the [110] orientation with severe twist angles exceeding 15◦ relative to the
matrix. These bands twist towards either the <111> or <100> direction. Further analysis of
the orientation differences between these bands and the matrix is presented in Figure 11c,
which plots the orientation deviation profiles along three lines in Figure 11b. It is apparent
that some deformation bands can rotate at an angle of nearly 60 ◦, close to the angle of
deformation twins. Figure 11d shows a typical HRTEM image of the interface between
the matrix and deformation band. This further proves that the deformation band is not a
deformation twin, and that the inset FFT pattern reveals that the deformation band greatly
twisted away from the [110] normal direction of the matrix. These deformation bands
demonstrate that dislocations within these bands can cooperatively rotate to accommodate
large plastic deformation.
In addition to deformation bands, the fractured S1 sample also exhibited other de-
formation mechanisms, such as SFs and deformation twins. The bright-field TEM image
(Figure 12a) demonstrates intersecting SFs within a grain, characterized by multiple de-
formation bands in the matrix. The magnified view in Figure 12b reveals a network of
interwoven SFs, segmenting the matrix into nanoscale subdivisions. Moreover, nanoscale
deformation twins, observed sporadically, serve as barriers to hinder the propagation of
SFs, as shown in the HRTEM image (Figure 12c). In grains lacking severely distorted
deformation bands, an extensive formation of SFs during plastic deformation is noted, as
illustrated in Figure 12d. A SAED pattern from Figure 12d, taken along the [110] zone
axis, discloses characteristic streaking along two directions, signifying the presence of SFs.
Figure 12e zooms into the area highlighted by the orange dashed line in Figure 12d, expos-
ing a hierarchical organization of primary and secondary SFs. This arrangement further

## Page 10

Metals 2024, 14, 590 10 of 16
subdivides the grains into nanoscale regions, invoking a dynamic Hall–Petch effect. Lastly,
an HRTEM image in Figure 12f sheds light on the intricate interactions between SFs along
two orientations. It is evident that SFs on different {111} slip planes intersect, creating char-
acteristic sessile Lomer–Cottrell (LC) locks that potentially obstruct dislocation movement.
Figure 11. (a) Bright-field TEM image showing deformation bands in the large-grained S1 sample. The
inset displays the SAED pattern along the [110] direction of the region highlighted by the red circle.
(b) PED result showing the grain orientation change induced by deformation bands. (c) Orientation
change profiles for the 1, 2, 3 directions indicated in (b). (d) HRTEM image showing the interface
between the matrix and the deformation band. Insets show the corresponding FFT patterns of the
matrix and deformation band.
Further analysis focused on the deformation mechanisms within small-grained sam-
ples. Figure 13a presents an ABF–STEM image capturing the characteristic deformation
microstructure of the fractured S3 sample. Notably, a high density of straight SFs, aligned
in a singular direction and forming channels approximately 50 nm wide across each grain.
These channels, formed by SFs, effectively confine dislocation movement within them
(Figure 13b), thereby providing a dynamic Hall–Petch strengthening mechanism. Consis-
tent with the dynamic Hall–Petch strengthening, the inverse fast Fourier transform (IFFT)
of the HRTEM image (inset of Figure 13c) shows a substantial accumulation of disloca-
tions on both sides of the SF, which contributes to the channel formation. The presence
of streaking perpendicular to the SFs in the inset of Figure 13a further confirms that the
straight lines in Figure 13a are indeed SFs. The presence of SFs in the Ni10Co56.5V33.5 MPEA
suggests a low SFE; however, contrary to expectations of planar slip, wavy dislocations
predominate, as depicted in Figure 13b. In this way, the dislocation morphology aligns
with the large LLD characteristic of the Ni10Co56.5V33.5 MPEA. Additionally, deformation
bands were detected in the small-grained S3 sample, as revealed in the bright-field TEM
image (Figure 13d), with dense dislocations constrained within these deformation bands.
The HAADF image of the same area (Figure 13e) reveals that the dense SFs, interspersed
throughout both the matrix and the deformation bands exhibit varied orientations. This
orientation discrepancy suggests that the deformation bands are markedly twisted, with

## Page 11

Metals 2024, 14, 590 11 of 16
band boundaries serving as effective impediments to the further spread of SFs within the
matrix, thereby contributing to the strengthening effect.
Figure 12. (a) Bright-field TEM image showing dislocation bands and SFs in the fractured S1 sample.
(b) An enlarged view of the area enclosed by the yellow dashed line in (a). (c) HRTEM image of the
interaction between the deformation twin and SFs, with the inset showing the FFT pattern of the
deformation twin. ( d) Annular bright-field scanning TEM (ABF–STEM) image showing SFs. The
inset displays the SAED pattern of the region highlighted by the red dashed line. (e) A magnified
view of the region in orange dashed box in (d). (f) HRTEM image of Lomer–Cottrell locks formed
by SFs.
Our study on deformation mechanisms has revealed that SFs and dislocations serve
as the primary mechanisms across both large- and small-grained samples. Furthermore,
the abundant formation of SFs and deformation bands in both large- and small-grained
samples acts as an effective barrier to dislocation movement, thereby contributing to the
MPEA’s enhanced strength. A distinctive feature of the deformation mechanism in our
newly designed MPEA is the emergence of severely twisted dislocation bands. Similar
dislocation bands or microbands have been identified in alloys such as Fe–28Mn–9Al–0.8C
steel [71], Inconel 718 [ 72], and NiCoFe-based MPEA [ 73], where these alloys typically
exhibit relatively low SFE, conducive to the formation of coplanar dislocations. However,
the Ni10Co56.5V33.5 MPEA distinguishes itself through the development of exceptionally
twisted deformation bands, facilitating a more effective accommodation of large plastic
deformation. While the SFE of the Ni10Co56.5V33.5 is low enough to enable the formation
of SFs and deformation twins, coplanar dislocations are not prevalent within this MPEA.
Instead, the wavy dislocation morphology observed in the Ni10Co56.5V33.5 MPEA aligns
with the substantial LLD, offering a strong drag effect on dislocation motion, thus enhancing
the alloy’s strength. Admittedly, the high strength of the Ni10Co56.5V33.5 MPEA also stems
from precipitate strengthening and strengthening from dislocations that are initially stored
in recrystallized samples. The impact of these factors, however, is limited due to their low
proportion of precipitates and dislocations.

## Page 12

Metals 2024, 14, 590 12 of 16
Figure 13. (a) ABF–STEM image of the fractured small-grained S3 sample. The inset diffraction
pattern was taken from the region highlighted by red circle. ( b) A magnified ABF–STEM image
showing the interaction of SFs and dislocations. (c) HRTEM image of the SF region, with the inset
showing the IFFT-magnified image enclosed by a red dashed line. Yellow T-shapes marks highlight
edge dislocations. (d) Bright-field TEM image of deformation bands. (e) HAADF image of SFs with
different orientations in the matrix and deformation band.
5. Conclusions
In summary, we have designed a non-equiatomic Ni10Co56.5V33.5 MPEA that exhibits
a superior balance between strength and ductility at the cryogenic temperature of 77 K,
achieved by optimizing LLD and SFE. The microstructure and deformation mechanisms
were carefully characterized by HEXRD, EBSD, TEM, and PED. The DFT calculations
provided the fundamental understandings of the LLD. Based on our observations, some
key conclusions can be drawn, as follows:
(a) In the developed Ni 10Co56.5V33.5 MPEA, the predominant phase is FCC accompa-
nied by a minor σ phase, the latter constituting less than 3.0% by volume. In sam-
ples with larger grains, precipitates primarily form along dislocations within the
grains, whereas in those with smaller grains, precipitates are predominantly formed at
grain boundaries.
(b) After recrystallization heat treatments, the large-grained sample shows a relatively
uniform grain size, while the small-grained sample exhibits a heterogeneous mi-
crostructure composed of both large and small grains.
(c) DFT calculations reveal pronounced LLD in the Ni 10Co56.5V33.5 MPEA, as atoms
deviate from ideal lattice sites, with V–V atomic pairs showing the greatest distances
due to vanadium’s larger atomic size. The size mismatch parameter calculated for
this MPEA is comparable with the value for the equiatomic NiCoV MPEA.
(d) By tuning the grain size, the Ni10Co56.5V33.5 MPEA exhibits a yield strength ranging
from 841 to 1400 MPa and an ultimate tensile strength from 1434 to 1890 MPa, with
ductility ranging from 47% to 23%.
(e) In the large-grained sample, the primary deformation mechanisms encompass severely
twisted deformation bands exhibiting rotation angles nearing 60◦, hierarchical SFs,
and sporadic deformation twins. Conversely, the small-grained sample displays a
deformation microstructure defined by deformation bands and SFs aligned in one

## Page 13

Metals 2024, 14, 590 13 of 16
direction within each grain. The formation of dislocation bands and SFs contributes
to a dynamic Hall–Petch effect.
Thus, our study offers insights into the design of strong and ductile MPEAs for
applications at cryogenic temperatures by optimizing LLD and SFE. On the other hand,
the new deformation mechanism of severely distorted deformation band found in the
Ni10Co56.5V33.5 MPEA needs further study to understand its origin.
Author Contributions: Conceptualization, Y.T. and W.L.; methodology, Y.T. and C.S.; formal analysis,
D.Z, C.S., W.L. and Y.T.; investigation, D.Z., C.W., R.S. and Y.T.; resources, Y.T.; data curation, D.Z.
and Y.T.; writing—original draft, D.Z. and Y.T., writing—review and editing, Y.T., C.S. and W.L. All
authors have read and agreed to the published version of the manuscript.
Funding: Y .T. gratefully acknowledges the financial support of the National Natural Science Foundation
of China (Grant No. 52371164), the Taishan Scholars Program of Shandong Province (tsqn202103052),
and the Yantai city matching fund for Taishan Scholars Program of Shandong Province.
Data Availability Statement: The raw data supporting the conclusions of this article will be made
available by the authors on request.
Acknowledgments: AI tool: ChatGPT4, was utilized solely for grammar and syntax checking in
the manuscript.
Conflicts of Interest: The authors declare no conflict of interest.
References
1. Cantor, B.; Chang, I.T.H.; Knight, P .; Vincent, A.J.B. Microstructural development in equiatomic multicomponent alloys.Mater.
Sci. Eng. A 2004, 375–377, 213–218. [CrossRef]
2. Yeh, J.W.; Chen, S.K.; Lin, S.J.; Gan, J.Y.; Chin, T.S.; Shun, T.T.; Tsau, C.H.; Chang, S.Y. Nanostructured High-Entropy Alloys with
Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes. Adv. Eng. Mater. 2004, 6, 299–303. [CrossRef]
3. Zhang, Y.; Zuo, T.T.; Tang, Z.; Gao, M.C.; Dahmen, K.A.; Liaw, P .K.; Lu, Z.P . Microstructures and properties of high-entropy alloys.
Prog. Mater. Sci. 2014, 61, 1–93. [CrossRef]
4. Miracle, D.B.; Senkov, O.N. A critical review of high entropy alloys and related concepts. Acta Mater. 2017, 122, 448–511.
[CrossRef]
5. George, E.P .; Raabe, D.; Ritchie, R.O. High-entropy alloys. Nat. Rev. Mater. 2019, 4, 515–534. [CrossRef]
6. Ye, Y.F.; Wang, Q.; Lu, J.; Liu, C.T.; Yang, Y. High-entropy alloy: Challenges and prospects. Mater. T oday 2016, 19, 349–362.
[CrossRef]
7. Senkov, O.N.; Wilks, G.B.; Scott, J.M.; Miracle, D.B. Mechanical properties of Nb25Mo25Ta25W25 and V20Nb20Mo20Ta20W20
refractory high entropy alloys. Intermetallics 2011, 19, 698–706. [CrossRef]
8. Gludovatz, B.; Hohenwarter, A.; Catoor, D.; Chang, E.H.; George, E.P .; Ritchie, R.O. A fracture-resistant high-entropy alloy for
cryogenic applications. Science 2014, 345, 1153–1158. [CrossRef]
9. Liu, D.; Yu, Q.; Kabra, S.; Jiang, M.; Forna-Kreutzer, P .; Zhang, R.; Payne, M.; Walsh, F.; Gludovatz, B.; Asta, M.; et al. Exceptional
fracture toughness of CrCoNi-based medium- and high-entropy alloys at 20 kelvin. Science 2022, 378, 978–983. [CrossRef]
10. Zhang, C.; Yu, Q.; Tang, Y.T.; Xu, M.; Wang, H.; Zhu, C.; Ell, J.; Zhao, S.; MacDonald, B.E.; Cao, P .; et al. Strong and ductile
FeNiCoAl-based high-entropy alloys for cryogenic to elevated temperature multifunctional applications. Acta Mater. 2023,
242, 118449. [CrossRef]
11. Sun, S.J.; Tian, Y.Z.; An, X.H.; Lin, H.R.; Wang, J.W.; Zhang, Z.F. Ultrahigh cryogenic strength and exceptional ductility in
ultrafine-grained CoCrFeMnNi high-entropy alloy with fully recrystallized structure. Mater. T oday Nano2018, 4, 46–53. [CrossRef]
12. Han, Z.; Ding, C.; Liu, G.; Yang, J.; Du, Y.; Wei, R.; Chen, Y.; Zhang, G. Analysis of deformation behavior of VCoNi medium-entropy
alloy at temperatures ranging from 77 K to 573 K. Intermetallics 2021, 132, 107126. [CrossRef]
13. Byun, T.S.; Hashimoto, N.; Farrell, K. Temperature dependence of strain hardening and plastic instability behaviors in austenitic
stainless steels. Acta Mater. 2004, 52, 3889–3899. [CrossRef]
14. Umezawa, O. Review of the Mechanical Properties of High-Strength Alloys at Cryogenic Temperatures. Mater. Perform. Charact.
2021, 10, 20200138. [CrossRef]
15. Sohn, S.S.; Kwiatkowski da Silva, A.; Ikeda, Y.; Körmann, F.; Lu, W.; Choi, W.S.; Gault, B.; Ponge, D.; Neugebauer, J.; Raabe,
D. Ultrastrong Medium-Entropy Single-Phase Alloys Designed via Severe Lattice Distortion. Adv. Mater. 2019, 31, 1807142.
[CrossRef] [PubMed]
16. Lee, C.; Chou, Y.; Kim, G.; Gao, M.C.; An, K.; Brechtl, J.; Zhang, C.; Chen, W.; Poplawsky, J.D.; Song, G.; et al. Lattice-Distortion-
Enhanced Yield Strength in a Refractory High-Entropy Alloy. Adv. Mater. 2020, 32, 2004029. [CrossRef] [PubMed]
17. Li, Z.; Ma, S.; Zhao, S.; Zhang, W.; Peng, F.; Li, Q.; Yang, T.; Wu, C.-Y.; Wei, D.; Chou, Y.-C.; et al. Achieving superb strength in
single-phase FCC alloys via maximizing volume misfit. Mater. T oday2023, 63, 108–119. [CrossRef]

## Page 14

Metals 2024, 14, 590 14 of 16
18. Lee, C.; Song, G.; Gao, M.C.; Feng, R.; Chen, P .; Brechtl, J.; Chen, Y.; An, K.; Guo, W.; Poplawsky, J.D.; et al. Lattice distortion in a
strong and ductile refractory high-entropy alloy. Acta Mater. 2018, 160, 158–172. [CrossRef]
19. Tong, Y.; Zhao, S.; Bei, H.; Egami, T.; Zhang, Y.; Zhang, F. Severe local lattice distortion in Zr- and/or Hf-containing refractory
multi-principal element alloys. Acta Mater. 2020, 183, 172–181. [CrossRef]
20. Okamoto, N.L.; Yuge, K.; Tanaka, K.; Inui, H.; George, E.P . Atomic displacement in the CrMnFeCoNi high-entropy alloy—A
scaling factor to predict solid solution strengthening. AIP Adv. 2016, 6, 125008. [CrossRef]
21. Varvenne, C.; Luque, A.; Curtin, W.A. Theory of strengthening in fcc high entropy alloys. Acta Mater. 2016, 118, 164–176.
[CrossRef]
22. Li, Z.; Pradeep, K.G.; Deng, Y.; Raabe, D.; Tasan, C.C. Metastable high-entropy dual-phase alloys overcome the strength–ductility
trade-off. Nature 2016, 534, 227–230. [CrossRef] [PubMed]
23. Zhang, Z.J.; Mao, M.M.; Wang, J.; Gludovatz, B.; Zhang, Z.; Mao, S.X.; George, E.P .; Yu, Q.; Ritchie, R.O. Nanoscale origins of the
damage tolerance of the high-entropy alloy CrMnFeCoNi. Nat. Commun. 2015, 6, 10143. [CrossRef] [PubMed]
24. Ming, K.; Lu, W.; Li, Z.; Bi, X.; Wang, J. Amorphous Bands Induced by Low Temperature Tension in a Non-Equiatomic
CrMnFeCoNi Alloy. Acta Mater. 2020, 188, 354–365. [CrossRef]
25. Li, D.; Liaw, P .K.; Xie, L.; Zhang, Y.; Wang, W. Advanced high-entropy alloys breaking the property limits of current materials.
J. Mater. Sci. T echnol. 2024, 186, 219–230. [CrossRef]
26. George, E.P .; Curtin, W.A.; Tasan, C.C. High entropy alloys: A focused review of mechanical properties and deformation
mechanisms. Acta Mater. 2020, 188, 435–474. [CrossRef]
27. Miao, J.; Slone, C.E.; Smith, T.M.; Niu, C.; Bei, H.; Ghazisaeidi, M.; Pharr, G.M.; Mills, M.J. The evolution of the deformation
substructure in a Ni-Co-Cr equiatomic solid solution alloy. Acta Mater. 2017, 132, 35–48. [CrossRef]
28. Yang, D.C.; Jo, Y.H.; Ikeda, Y.; Körmann, F.; Sohn, S.S. Effects of cryogenic temperature on tensile and impact properties in a
medium-entropy VCoNi alloy. J. Mater. Sci. T echnol. 2021, 90, 159–167. [CrossRef]
29. Kresse, G.; Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis
set. Comput. Mater. Sci. 1996, 6, 15–50. [CrossRef]
30. Blöchl, P .E. Projector augmented-wave method. Phys. Rev. B 1994, 50, 17953–17979. [CrossRef]
31. Perdew, J.P .; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple.Phys. Rev. Lett. 1996, 77, 3865–3868.
[CrossRef] [PubMed]
32. Zunger, A.; Wei, S.H.; Ferreira, L.G.; Bernard, J.E. Special quasirandom structures.Phys. Rev. Lett. 1990, 65, 353–356. [CrossRef]
[PubMed]
33. Oh, H.; Kim, S.; Odbadrakh, K.; Ryu, W.; Yoon, K.; Mu, S.; Körmann, F.; Ikeda, Y.; Tasan, C.; Raabe, D.; et al. Engineering
atomic-level complexity in high-entropy and complex concentrated alloys. Nat. Commun. 2019, 10, 1234567890. [CrossRef]
[PubMed]
34. Dodaran, M.S.; Guo, S.; Khonsari, M.M.; Shamsaei, N.; Shao, S. A theoretical calculation of stacking fault energy of Ni alloys: The
effects of temperature and composition. Comput. Mater. Sci. 2021, 191, 110326. [CrossRef]
35. Choi, W.; Jo, Y.H.; Kim, D.G.; Sohn, S.S.; Lee, S.; Lee, B. A thermodynamic description of the Co-Cr-Fe-Ni-V system for
high-entropy alloy design. Calphad 2019, 66, 101624. [CrossRef]
36. Yin, B.; Maresca, F.; Curtin, W.A. Vanadium is an optimal element for strengthening in both fcc and bcc high-entropy alloys.Acta
Mater. 2020, 188, 486–491. [CrossRef]
37. Zhang, Y.; Zhou, Y.J.; Lin, J.P .; Chen, G.L.; Liaw, P .K. Solid-Solution Phase Formation Rules for Multi-component Alloys.Adv. Eng.
Mater. 2008, 10, 534–538. [CrossRef]
38. Periodictable. Available online: https://periodictable.com/ (accessed on 4 April 2024).
39. Han, B.; Zhang, C.; Feng, K.; Li, Z.; Zhang, X.; Shen, Y.; Wang, X.; Kokawa, H.; Li, R.; Wang, Z.; et al. Additively manufactured
high strength and ductility CrCoNi medium entropy alloy with hierarchical microstructure. Mater. Sci. Eng. A 2021, 820, 141545.
[CrossRef]
40. Wu, Z.; Bei, H.; Pharr, G.M.; George, E.P . Temperature dependence of the mechanical properties of equiatomic solid solution
alloys with face-centered cubic crystal structures. Acta Mater. 2014, 81, 428–441. [CrossRef]
41. Gludovatz, B.; Hohenwarter, A.; Thurston, K.V .; Bei, H.; Wu, Z.; George, E.P .; Ritchie, R.O. Exceptional damage-tolerance of a
medium-entropy alloy CrCoNi at cryogenic temperatures. Nat. Commun. 2016, 7, 10602. [CrossRef]
42. Li, J.; Xiao, L.; Ma, X.; Lu, K.; Li, F.; Chen, J. Achieving ultrahigh cryogenic yield strength and sufficient ductility in a medium-
entropy alloy via bimodal grain design. Mater. Sci. Eng. A 2023, 863, 144491. [CrossRef]
43. Liu, J.; Guo, X.; Lin, Q.; He, Z.; An, X.; Li, L.; Liaw, P .K.; Liao, X.; Yu, L.; Lin, J.; et al. Excellent ductility and serration feature of
metastable CoCrFeNi high-entropy alloy at extremely low temperatures. Sci. China Mater. 2019, 62, 853–863. [CrossRef]
44. Kireeva, I.V .; Chumlyakov, Y.I.; Vyrodova, A.V .; Pobedennaya, Z.V .; Karaman, I. Effect of twinning on the orientation dependence
of mechanical behaviour and fracture in single crystals of the equiatomic CoCrFeMnNi high-entropy alloy at 77K. Mater. Sci. Eng.
A 2020, 784, 139315. [CrossRef]
45. Laplanche, G.; Kostka, A.; Horst, O.M.; Eggeler, G.; George, E.P . Microstructure evolution and critical stress for twinning in the
CrMnFeCoNi high-entropy alloy. Acta Mater. 2016, 118, 152–163. [CrossRef]
46. Seol, J.B.; Bae, J.W.; Kim, J.G.; Sung, H.; Li, Z.; Lee, H.H.; Shim, S.H.; Jang, J.H.; Ko, W.-S.; Hong, S.I.; et al. Short-range order
strengthening in boron-doped high-entropy alloys for cryogenic applications. Acta Mater. 2020, 194, 366–377. [CrossRef]

## Page 15

Metals 2024, 14, 590 15 of 16
47. Kim, Y.-K.; Lee, K.-A. Influence of carbon contents on the cryogenic mechanical properties of precipitation-hardened CrMnFeCoNi
high-entropy alloys manufactured by laser powder bed fusion. Mater. Sci. Eng. A 2023, 873, 145042. [CrossRef]
48. Li, J.; Lu, K.; Wang, Y.; Zhang, Y.; Ma, X.; Chen, J.; Zhu, Y. Exceptional cryogenic strength and sufficient ductility of a nanotwinned
high-entropy alloy fabricated by cryogenic multi-directional compression. J. Alloys Compd. 2023, 931, 167533. [CrossRef]
49. Kireeva, I.V .; Chumlyakov, Y.I.; Pobedennaya, Z.V .; Vyrodova, A.V .; Kuksgauzen, I.V .; Kuksgauzen, D.A. Orientation and
temperature dependence of a planar slip and twinning in single crystals of Al0.3CoCrFeNi high-entropy alloy. Mater. Sci. Eng. A
2018, 737, 47–60. [CrossRef]
50. Kireeva, I.V .; Chumlyakov, Y.I.; Pobedennaya, Z.V .; Vyrodova, A.V . Effect ofγ′-phase particles on the orientation and temperature
dependence of the mechanical behaviour of Al0.3CoCrFeNi high-entropy alloy single crystals. Mater. Sci. Eng. A 2020, 772, 138772.
[CrossRef]
51. Li, Q.; Zhang, T.W.; Qiao, J.W.; Ma, S.G.; Zhao, D.; Lu, P .; Wang, Z.H. Mechanical properties and deformation behavior of
dual-phase Al0.6CoCrFeNi high-entropy alloys with heterogeneous structure at room and cryogenic temperatures. J. Alloys
Compd. 2020, 816, 152663. [CrossRef]
52. Yuan, J.; Zhang, H.; Wang, Z.; Han, P .; Qiao, J. Contribution of coherent precipitates on mechanical properties of CoCrFeNiTi0.2
high-entropy alloy at room and cryogenic temperatures. Intermetallics 2023, 154, 107820. [CrossRef]
53. Tong, Y.; Chen, D.; Han, B.; Wang, J.; Feng, R.; Yang, T.; Zhao, C.; Zhao, Y.L.; Guo, W.; Shimizu, Y.; et al. Outstanding tensile
properties of a precipitation-strengthened FeCoNiCrTi0.2 high-entropy alloy at room and cryogenic temperatures. Acta Mater.
2019, 165, 228–240. [CrossRef]
54. Bhattacharjee, T.; Zheng, R.; Chong, Y.; Sheikh, S.; Guo, S.; Clark, I.T.; Okawa, T.; Wani, I.S.; Bhattacharjee, P .P .; Shibata, A.; et al.
Effect of low temperature on tensile properties of AlCoCrFeNi2.1 eutectic high entropy alloy. Mater. Chem. Phys. 2018, 210,
207–212. [CrossRef]
55. Jo, Y.H.; Yang, J.; Doh, K.-Y.; An, W.; Kim, D.W.; Sung, H.; Lee, D.; Kim, H.S.; Sohn, S.S.; Lee, S. Analysis of damage-tolerance of
TRIP-assisted V10Cr10Fe45Co30Ni5 high-entropy alloy at room and cryogenic temperatures. J. Alloys Compd. 2020, 844, 156090.
[CrossRef]
56. Gao, X.; Jiang, W.; Lu, Y.; Ding, Z.; Liu, J.; Liu, W.; Sha, G.; Wang, T.; Li, T.; Chang, I.T.H.; et al. Excellent strength-ductility
combination of Cr26Mn20Fe20Co20Ni14 high-entropy alloy at cryogenic temperatures. J. Mater. Sci. T echnol. 2023, 154, 166–177.
[CrossRef]
57. Jo, Y.H.; Doh, K.-Y.; Kim, D.G.; Lee, K.; Kim, D.W.; Sung, H.; Sohn, S.S.; Lee, D.; Kim, H.S.; Lee, B.-J.; et al. Cryogenic-temperature
fracture toughness analysis of non-equi-atomic V 10Cr10Fe45Co20Ni15 high-entropy alloy. J. Alloys Compd. 2019, 809, 151864.
[CrossRef]
58. Jang, M.J.; Kwak, H.; Lee, Y.W.; Jeong, Y.; Choi, J.; Jo, Y.H.; Choi, W.-M.; Sung, H.J.; Yoon, E.Y.; Praveen, S.; et al. Plastic
Deformation Behavior of 40Fe–25Ni–15Cr–10Co–10V High-Entropy Alloy for Cryogenic Applications. Met. Mater. Int. 2019, 25,
277–284. [CrossRef]
59. Zhang, Z.; Wang, W.; Qin, S.; Yang, M.; Wang, J.; Jiang, P .; Yuan, F.; Wu, X. Dual heterogeneous structured medium-entropy alloys
showing a superior strength-ductility synergy at cryogenic temperature. J. Mater. Res. T echnol. 2022, 17, 3262–3276. [CrossRef]
60. Peng, H.; Huang, S.; Hu, L.; Luo, B.; Li, L.; Baker, I. Electron beam welding of L12-nanoparticle-strengthened strong and ductile
medium-entropy alloys for cryogenic applications. Mater. Sci. Eng. A 2024, 889, 145875. [CrossRef]
61. Li, Y.X.; Nutor, R.K.; Zhao, Q.K.; Zhang, X.P .; Cao, Q.P .; Sohn, S.S.; Wang, X.D.; Ding, S.Q.; Zhang, D.X.; Zhou, H.F.; et al.
Unraveling the deformation behavior of the Fe45Co25Ni10V20 high entropy alloy. Int. J. Plast. 2023, 165, 103619. [CrossRef]
62. Kwon, H.; Sathiyamoorthi, P .; Karthik, G.M.; Asghari-Rad, P .; Zargaran, A.; Do, H.-S.; Lee, B.-J.; Kato, H.; Kim, H.S. 2.3 GPa
cryogenic strength through thermal-induced and deformation-induced body-centered cubic martensite in a novel ferrous medium
entropy alloy. Scr. Mater. 2021, 204, 114157. [CrossRef]
63. Wang, H.; Zhang, K.; Chen, L.; Gao, Q.; Zhao, X.; Chen, C.; Han, Z.; Wei, R. Strengthening Fe50+xMn25Cr15Ni10-x medium-
entropy alloys by Ni/Fe replacement: Experiments and molecular dynamics study. Intermetallics 2023, 155, 107833. [CrossRef]
64. Yin, Y.; Tan, Q.; Yang, N.; Chen, X.; Ren, W.; Liu, L.; Chen, H.; Atrens, A.; Ma, N.; Huang, H.; et al. Cost-effective and facile route
to ultrafine-microstructure high-entropy alloy for cryogenic applications. Mater. Sci. Eng. A 2023, 881, 145408. [CrossRef]
65. Wang, H.; Sun, Q.Y.; Xiao, L.; Sun, J. Effect of grain size on twinning behavior in Ti–2Al–2.5Zr alloy fatigued at 77K.Mater. Sci.
Eng. A 2012, 542, 1–7. [CrossRef]
66. Wen, X.; Zhu, L.; Naeem, M.; Huang, H.; Jiang, S.; Wang, H.; Liu, X.; Zhang, X.; Wang, X.-L.; Wu, Y.; et al. Strong work-hardenable
body-centered-cubic high-entropy alloys at cryogenic temperature. Scr. Mater. 2023, 231, 115434. [CrossRef]
67. Ma, D.; Xu, H.; Ding, J.; Shen, Y.; Zhang, T. Improved strength and ductility of Ti2(CrFeNi)98 multi-principal element alloy at
cryogenic temperature with deformation twins induced by BCC precipitates. Mater. Sci. Eng. A 2023, 862, 144489. [CrossRef]
68. Tang, K.; Wu, Y.K.; Wei, R.; Chen, L.B.; Lu, S.; Qi, Y.L.; Jiang, F.; Sun, J. Achieving superior cryogenic tensile properties in
a Ti-doped (Fe40Mn40Co10Cr10)96.7C3.3 high-entropy alloy by recovering deformation twinning. Mater. Sci. Eng. A 2021,
808, 140927. [CrossRef]
69. Chen, L.; Li, Z.; Dai, P .; Fu, P .; Tang, Q.; Chen, J. Microstructure and tensile properties of metastable Fe50Mn30Co10Cr10
high-entropy alloy prepared via powder metallurgy. J. Alloys Compd. 2023, 955, 170225. [CrossRef]
70. Kim, D.G.; Jo, Y.H.; Yang, J.; Choi, W.-M.; Kim, H.S.; Lee, B.-J.; Sohn, S.S.; Lee, S. Ultrastrong duplex high-entropy alloy with
2 GPa cryogenic strength enabled by an accelerated martensitic transformation. Scr. Mater. 2019, 171, 67–72. [CrossRef]

## Page 16

Metals 2024, 14, 590 16 of 16
71. Yang, T.; Zhao, Y.; Tong, Y.; Jiao, Z.; Wei, J.; Cai, J.; Han, X.; Chen, D.; Hu, A.; Kai, J.; et al. Multicomponent intermetallic
nanoparticles and superb mechanical behaviors of complex alloys. Science 2018, 362, 933–937. [CrossRef]
72. He, J.; Fukuyama, S.; Yokogawa, K. Deformation bands in Inconel 718. Mater. Sci. T echnol. 1995, 11, 914–920. [CrossRef]
73. Yoo, J.; Park, K.-T. Microband-induced plasticity in a high Mn–Al–C light steel. Mater. Sci. Eng. A 2008, 496, 417–424. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
