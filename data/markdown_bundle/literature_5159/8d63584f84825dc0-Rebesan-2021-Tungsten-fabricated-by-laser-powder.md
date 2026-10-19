# Rebesan-2021-Tungsten-fabricated-by-laser-powder

<!-- source: D:\总文献\Rebesan-2021-Tungsten-fabricated-by-laser-powder.pdf -->
<!-- file_sha256: 99d72118030985031abf52403e4ae2a3c355d120700778580f6e8e23ac78e260 -->

## Page 1

Originalarbeit
Berg Huettenmaenn Monatsh (2021) Vol. 166 (5): 263–269
https://doi.org/10.1007/s00501-021-01 109-y
© The Author(s) 2021
T ungsten Fabricated by Laser Powder Bed Fusion
Pietro Rebesan1,2, Massimiliano Bonesso 1,3, Claudio Gennari 3,R a z v a nD i m a1, Adriano Pepato1,a n d
Maurizio V edani2
1Padova Division, National Institute for Nuclear Physics (INFN), Padova, Italy
2Department of Mechanical Engineering, Politecnico di Milano, Milano, Italy
3Department of Industrial Engineering, University of Padua, Padova, Italy
Received March 5, 2021; accepted April 5, 2021; published online April 28, 2021
Abstract: Additive Manufacturing (AM) is the process
that allows the production of complex geometry and
lightweight components. Thanks to the high density of
refractory metals, AM could be a possible solution for
their application in the aerospace ﬁeld and for biomedical
or future nuclear fusion devices. Y et, Laser Powder Bed
Fusion (LPBF) of refractory metals as T a, Mo, and W faces
some challenges due to their main properties: high melting
point, heat conductivity, and susceptibility to cracks.
The purpose of this study is to optimize the process pa-
rameters in order to produce high-density T ungsten parts
by LPBF on an EOS M100 (maximum power of 170 W). The
characterization is performed through physical properties
measurements and microstructural analysis. Single Scan
T racks (SSTs) are produced on the top surfaces of T ungsten
blocks to evaluate the process parameters that give regu-
lar-shape and continuous melt-pools. Both analytical and
experimental optimizations of process parameters were
performed. Micro-hardness measurements were done for
dense bulk specimens. Finally, a description of suscepti-
bility to cracks of additivel y manufactured T ungsten was
performed.
Keywords: Laser Powder Bed Fusion (LPBF), Selective
Laser Melting (SLM), Refractory metals, T ungsten, Cracks,
Single Scan T racks
T ungsten hergestellt durch Laserpulverbett-Fusion
Zusammenfassung: Additive Manufacturing (AM) ist der
Prozess, der die Herstellung komplexer Geometrien und
leichter Komponenten ermöglicht. Dank der hohen Dich-
te von Refraktärmetallen könnte AM eine mögliche Lösung
P. R e b e s a n (/envelopeback)
Padova Division,
National Institute for Nuclear Physics (INFN),
Via Marzolo, 8,
35131 Padova, Italy
pietro.rebesan@pd.infn.it
für deren Anwendung im Bereich der Luft- und Raumfahrt
sowie für biomedizinische oder zukünftige Kernfusionsge-
räte sein. Die Laserpulverbettfusion (LPBF) von feuerfes-
ten Metallen, wie T a, Mo und W, steht jedoch aufgrund
ihrer Haupteigenschaften vor einigen Herausforderungen:
hoher Schmelzpunkt, Wärmeleitfähigkeit und Ri ssanfällig-
keit. Der Zweck dieser Studie ist die Optimierung der Pro-
zessparameter, um ein hochdichtes Wolframteil durch LPBF
auf einer EOS M100 (maximale Leistung von 170 W) her-
zustellen. Die Charakterisierung erfolgt durch Messungen
der physikalischen Eigenschaften und Mikrostrukturanaly-
se. Single Scan T racks (SSTs) werden auf den oberen Ober-
ﬂächen von Wolframblöcken erzeugt, um die Prozesspa-
rameter zu bewerten, die regelmäßig geformte und kon-
tinuierliche Schmelzpools ergeben. Es wurde sowohl eine
analytische als auch eine experimentelle Optimierung der
Prozessparameter sowie Mikrohärtemessungen für dich-
te Massenproben durchgeführt. Schließlich wurde die An-
fälligkeit für Risse von additiv hergestelltem Wolfram be-
schrieben.
Schlüsselwörter: Laser Pulverbettfusion (LPBF), Selektives
Laserschmelzen (SLM), Feuerfeste Metalle, Wolfram,
Risse, Single-Scan-Spuren
1. Introduction
Refractory metals belong to the group of transition metals
and are also called “ultra-high temperature materials” .I n
addition to the high melting temperatures, they have prop-
erties, like high density, high thermal conductivity, and ex-
cellent corrosion resistance, that make them suitable for
many applications [ 1]. For example, T ungsten is a promis-
ing candidate for nuclear fusion devices [ 2]; the prolifera-
tion of human osteoblast is much higher on tantalum com-
pared to the most commonly used Ti-6Al-4V [ 3]; and ﬁnally
for space and aerospace applications in order to increase
the temperature capabilities of devices [ 4].
Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5 © The Author(s) 263

## Page 2

Originalarbeit
T ungsten produced by the laser powder bed fusion pro-
cess is the subject of this contribution.
The traditional subtractive process for refractory metal
tools is complicated and expensive, both for the waste of
material that is removed and for the cost of tools suitable
for hard metals, such as W, T a, and Mo. For instance, the
extremely high melting temperature, in addition to its high
afﬁnity towards oxygen at high temperatures, makes it dif-
ﬁcult to process refractory metals components via conven-
tional processing technologies like casting without a con-
trolled atmosphere [ 5].
These reasons lead to the need of investigating Addi-
tive Manufacturing technologies and in particular the LPBF
process. The production of refractory metals by Additive
Manufacturing offers many advantages. The possibility of
recycling the unmelted particles is one of the most impor-
tant aspects for highly expensive powders like T a. Due to
their high melting point, the energy required to melt a vol-
ume of material is given by the focused energy of the laser
beam which locally raises the temperature up to the melt-
ing point. AM is the only process that allows the produc-
tion of complex geometry and lightweight refractory met-
als components, two important features for these kinds of
materials, according to their high density and their possi-
ble applications in the aerospace ﬁeld, and for biomedical
or future nuclear fusion devices.Y et, selective laser melt-
ing of W faces some challenges due to its main properties:
high melting point, heat conduc tivity, and susceptibility to
cracks.
In this study, the optimization of the main process pa-
rameters in order to obtain T ungsten fully-dense compo-
nents is performed and the susceptibility of W components
produced by SLM to crack is described.
2. Material and Methods
2.1 Powder and System
For the optimization of the main process parameters, cubic
samples in additively manufactured W were produced us-
ing an EOS M100 DMLS system by Electro-Optical Systems
Gmbh. (EOS). The M100 machine is equipped with a 200W
Yb:Y AG laser with a wavelength of 1064 nm and a 40 μm
Gaussian spot diameter.
High purity T ungsten (99.9%) raw material utilized for
this study were highly spherical powders TEKMAT™ W-25.
Plasma densiﬁcation and spheroidization were done by
T ekna Advanced Materials Inc. W powders have a particle
size distribution of D
10 =1 0μm, D90 =2 5μm.
The LPBF process was performed under Ar atmosphere.
The oxygen content in the building chamber was about
0.1%. Before printing began, the platform was preheated
to 80 °C (353 K).
2.2 Process Parameters
The optimization of the main process parameters, such
as laser power, scanning speed, and hatching distance,
was performed in order to obtain fully dense components.
W samples were built using a carbon steel substrate.
T wo strategies were adopted in order to ﬁnd the opti-
mal process parameters: the analytical starting approach
and the experimental conﬁrmation test. Considering that
the main feature of this refractory metal is the high melting
point, some preliminary calculations were done in order to
narrow the window of possible process parameters related
to the melting of the powder bed [ 6]. Single Scan T rack
(SST) analyses were performed to observe the inﬂuence
of the main process parameter related to the melting of
the material, laser power, and scanning speed. Thirty-two
SSTs were produced on the top surfaces of sixteen blocks
(8 mm × 8 mm × 8 mm), combining four laser power values
with eight scanning speed values. The production of blocks
and SSTs were done in only one step. For the block produc-
tion, the laser power was ﬁxed to 170 W, the scanning speed
and hatching distance were in the range of 400–800 mm/s
and 0.04–0.07 mm, respectively.
The scanning strategy chosen for W production was the
bidirectional pattern with a 67° rotation between adjacent
layers in order to cut down the residual stress as much as
possible. The stripes were scanned always in the oppo-
site direction to the argon ﬂow to minimize the presence
of sparks and droplets of molten metal on the powder bed
that has not yet been melted. The layer thickness ( t)s e -
lected was 20μm in order to guarantee a good bonding be-
tween consecutive layers. Considering the extremely high
melting point of T ungsten, this layer thickness allows the
homogeneous melting of the powder bed, and the re-melt-
ing of previous layers could result in a possible reduction
of lack of fusion and delamination.
When the SLM process was concluded, the samples
were detached from the platform by a wire Electrical Dis-
charge Machine (EDM – SODICK AQ 750 LH).
2.3 Characterization
The ﬂowability of W powder was measured with standard
test methods for the ﬂow rate of metal powders using the
Hall Flowmeter funnel (according to ASTM B213 – 20 ). The
test was performed ﬁve times with Method 2 (dynamic start
to ﬂow). The density of as-built W specimens was mea-
sured using the Archimedes’ Principle (according to ASTM
B962 – 17).
The surface morphology observation and microstruc-
tural analysis of blocks and SSTs as-fabricated were per-
formed using a scanning electron microscope (Leica Cam-
bridge Stereoscan LEO 440, Leic a Microsystems S.r.l., Mi-
lan, Italy). The SSTs thickness was measured with ImageJ
image processing software. T ungsten samples were pre-
pared with standard metallographic preparation and elec-
trolytically etched with a solution of 10 g in 100 ml of dis-
tilled water of sodium hydroxide (NaOH) at 2 V for 15 s.
Microhardness measurements were performed on a Leitz
Miniload 2 (Leica Microsystem S.r.l., Milan, Italy) micro-
hardness tester with 200 g load. The measurement uncer-
tainty for the ﬂowability test, micro-hardness, was calcu-
lated as the standard deviation on the measurement, while,
264 © The Author(s) Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5

## Page 3

Originalarbeit
Fig. 1: SEM images of the
Single Scan T racks (SSTs)
obtained using different scan
laser Power (P) and Scan
Speed (v)
for the density measurement, the uncertainty was calcu-
lated with the Kline & McClintoc formulation [ 7].
3. Result and Discussion
3.1 Powder Characterization
The powder morphology plays an important role in ad-
ditively manufactured W production. Lower part density
(16 g/cm3) was produced in the study of Zhou et al. [ 8],
where the raw material was W powder with an irregular
shape. Wang et al. [ 9] made a comparison between two
different morphologies, polyhedral and spherical powders,
obtaining a density of 84% and 96% of the theoretical den-
sity. Also T an et al. [ 6] conﬁrmed the importance of the
spherical powder. After a parameter optimization, speci-
mens with high density values of 19.01 g/cm3 (98.5% of TD)
were produced.
The particle size distribution (PDS) has a strong inﬂuence
on laser absorption and on track formation during the SLM
process. Zhang et al. [ 10] demonstrated that the powder
Fig. 2: a, b SEM images of SSTs used for width measure with ImageJ;c Thickness of continuous SSTs as a function of scan speed
layer absorptivity is strongly dependent on the PSD. The
powder-to-laser absorptivity is 0.6030 when the particle di-
ameter is in the range of 5–15μm, it diminished up to 0.4986
in the range of 15–45μm. On the other hand, the PSD inﬂu-
ences the powder ﬂowability, which can affect powder bed
particle distribution during the process [11]. The ﬂowability
test performed with Method 2 (dynamic start to ﬂow) gives
a ﬂow rate of 12.4 ± 0.5 s/50 gr for T ungsten powder.
Although there was no ﬂow with Method 1 (static start to
ﬂow) of the powder during the test with the Hall Flowmeter,
the powder was still well distributed on the platform, also
thanks to the use of a recoater with a metal blade.
3.2 Selective Laser Melted T ungsten
Fig. 1 shows SEM images of the Single Scan T racks (SSTs)
produced on the top surface of the T ungsten blocks using
different scan laser power ( P) and scan speed ( v). In the
melting of T ungsten powder, the SSTs production gives an
immediate and effective response if the energy supplied is
sufﬁcient to melt the powder bed. Four values were chosen
Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5 © The Author(s) 265

## Page 4

Originalarbeit
for laser power (100, 125, 150, 170 W). For each laser power
value listed, the scanning speed was set at 200, 300, 400,
500, 700, 800, 900, 1000 mm/s. Fig. 1 shows the important
role of the scan speed in the production of SSTs. With scan
speeds included in the range of 800–1000 mm/s, it can be
observed that the production of a melt track does not take
place, but only the formation of W drops is visible, which
are more evident at the higher powers. Another signiﬁcant
range is from 500 to 700 mm/s, where fragmented and ir-
regular SSTs were melted by the laser during the process
except for the highest value of laser power (170 W). Finally,
the range of 200–400 mm/s (and also 500 mm/s for the laser
power of 170 W) is the range in which the single tracks were
continuous and homogeneous.
The effect of laser power in this successful production is
related to the width of the tracks (Fig. 2).
If the effective power increases, the volume of the
molten pool increases in turn, while the viscosity de-
creases, causing melt hydrodynamics (driven by Marangoni
effect) to become the most important factor. When the
scanning speed decreases, the heat affected zone becomes
larger. For this reason, the melt pool involves more powder
from its boundaries [ 12]. Fig. 2 shows the quantiﬁcation of
continuous and homogeneous Single Scan T rack thickness
as a function of the laser scanning speed, considering the
different laser powers adopted. It can be seen from the
graph of Fig. 2c that the thickness of the SSTs is strongly
correlated to the laser power, with the same scanning
speed chosen. The evaluation of SSTs morphology and
the trend of data related to their thickness, in addition to
the test of block fabrication, give important information in
the choice of parameters for fully dense component pro-
duction and also to produce an intact contour, thin walls,
and lattice structures.
The parameter optimization in order to produce fully
dense T ungsten blocks started with the analytic method
proposed by T an et al. [6]. These calculations are based on
Q
p (J/mm3), which is the energy required to melt the vol-
ume of material (also called Volume Energy Density). The
estimation of this energy has been calculated with Eq. 1:
Qp = ρcp (Tm −T0)+ ρLf (1)
TABLE 1
Physical properties used for theoretical calculation of
Qp and Qv
Physical Properties Value Unit
Density (ρ) 19.25 g·cm–3
Speciﬁc Heat ( cp)1 3 2 J ( k g · K ) –1
Melting Point ( tm) 3693 (3420) K (°C)
Initial T emperature (t0) 353 (80) K (°C)
Latent Heat of Fusion ( Lf)2 . 2 0 × 1 0 5 J·kg–1
Laser Absorptivity (α)0 , 5 6 [ 1 0 ]
Laser Beam Radius ( rlb)2 0 µ m
Melt Pool Radius ( rm)4 0 µ m
Layer Thickness ( lt)2 0 µ m
The physical properties used for the theoretical calcula-
tion of Qp are listed in T able1.
The volumetric laser energy per unit volume Q v (J/mm3)
of T ungsten powders can be determined from the expres-
sion as follows:
Qv = πr2
lb EinΔt
Vm
(2)
Ein = 2αP
πr2
lb
(1 −e2)(1 −0.2) (3)
Where Ein (W/mm2) (Eq. 3) is the effective energy used for
melting the powders, obtained from the average laser en-
ergy ﬂux, which is the function of laser absorptivity (α), laser
Power (P), and laser beam radius (rlb). In the Ein calculation,
also the energy lost by convection, radiation, and evapora-
tion (total heat loss = 20%) [ 13] is considered.Δt is the laser
exposure time and is a function of the scan speed ( v)a n d
laser beam radius ( rlb). Vm is the effective volume of the
molten pool. The melt pool geometry is simpliﬁed as a part
of a sphere, an approximation that is also conﬁrmed by
Bajaj’ s simulation studies [14], mainly due to the thermal
properties of the refractory metal. The radius of the melt
track is estimated twice as the r
lb, considering roughly the
minimum width of the SSTs measured (average of about
80 µm) as shown in the diagram of Fig. 2. The laser melting
depth was considered equal to double of the layer thick-
ness (l
t) in order to guarantee adhesion between one layer
and the next thanks to re-melting. Moreover, re-melting de-
creases the possibility of forming the balling phenomenon
due to rapid solidiﬁcation and of reducing thermal stresses.
The second part of T able 1 lists also the geometrical pa-
rameters of the melting zone, the laser and powder param-
eters. Compared to the work proposed by T an et al. [ 6],
the value of the absorptivity is not that of the ﬂat material
(0.41), but the one calculated by Zhang et al. [ 10], chosen
conservatively considering the maximum value D
90 of the
PSD used (D 90 =2 5µ m ) .
Theoretically, in order to completely melt the pow-
ders, the volumetric laser energy per unit volume has to
be greater than the energy required to melt a volume of
material (Qv >Q p).
The experimental test was performed with the laser
power ﬁxed at 170 W and four different scan speeds set
at 400, 500, 600, 800 mm/s. For all four combinations of
parameters, Q
v >Q p is widely satisﬁed, as illustrated in the
results of the calculations in T able 2, even if the Qp value
of W is high, because of the high melting point and density,
TABLE 2
Calculations of Qv and Qp for different laser parame-
ters chosen for experimental test
p [W] v [mm/s] η =p / v Qv [J/mm3] Qp [J/mm3]
170 400 0.43 49.15 12.73
170 500 0.34 39.32 12.73
170 600 0.28 32.77 12.73
170 800 0.21 24.58 12.73
266 © The Author(s) Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5

## Page 5

Originalarbeit
Fig. 3: SEM image of block surface with hatching distance of 0.7 mm. De-
tails on surface morphology and cracks type
resulting in large temperature gradient and residual stress
[15].
The production of T ungsten blocks was performed with
four different values of hatching distance from 0.04 to
0.07 mm. The choice of this range of hatching distance was
based on some considerations of machine parameters as
the laser beam radius ( rlb) and some of the main properties
of T ungsten.
The dynamic viscosity μ of pure T ungsten was high be-
cause of the high melting point, high surface tension, and
cohesive energy [ 16, 17]. This leads to a low ﬂowability of
the melt pool. When the overlap between two consecutive
scan tracks (hatching distance— hd) is insufﬁcient, there is
the possibility of formation of defects, also called lack-of-
fusion (LoF), as shown in Fig. 3. For this reason, the choice
of the hatching distance was in the range of 0.04 ÷ 0.07 mm,
where 0.04 is the value of laser spot diameter (40 µm). This
should guarantee the overlap between consecutive scan
Fig. 4: a W blocks;b Density measured with Archimedes’ method as function of hatch distance (hd) at different scan speed (v)
tracks, even with a re-melting of at least half of the melting
track.
The choice of such low hatching distances was beneﬁ-
cial as can be seen from the density measurements with
the Archimedes’ method, shown in the diagram of Fig. 4b.
For scan speed values in the range 400–600 mm/s, the den-
sity measured was higher than 99%, with a maximum of
99.61 ± 0.5% for a scan speed of 600 mm/s.
A micro-mechanical characterization of the selective
laser melted T ungsten was performed by an indentation
test. The Vickers micro-hardness was measured on the
specimens with a higher density, obtained with a scan
speed of 400, 500, and 600 mm/s and the hatching dis-
tance of 0.04 mm. The same results were found for these
three samples, with an average of 420 HV and a standard
deviation of 13.5. The result is in line with the hardness
found by Wen et al. [ 17] and a greater hardness compared
to conventional SPS processed T ungsten (in the range of
320 ÷ 400 HV) [18].
3.3 Susceptibility to Crack
T ungsten specimens show a typical behaviour of this re-
fractory metal produced by LPBF process: high cracking
tendency. As shown in Fig. 3, which displays some details
on surface morphology and crack types on a W specimen,
cracks grow by a certain regulation and are distributed ho-
mogenously on the surface of the samples. Thanks to the
scheme proposed in Fig. 3, it is possible to deﬁne two kinds
of cracks. The longitudinal ones, which initiate and propa-
gate along the centre of the melt-pool, and the transverse
cracks that are perpendicular to the surface ripples gen-
erated by the laser during the continuous scanning. Lon-
gitudinal cracks are linear and fragmented with a length
between 30 and 100 µm. T ransverse cracks are shorter and
have an “S”-shape. They exactly follow the shape of the
grain boundary, as can be seen from the SEM images of
Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5 © The Author(s) 267

## Page 6

Originalarbeit
Fig. 5: a SEM image of W elec-
trolytically etched sample dis-
playing a crack network;b SEM
Image of Mo sample displaying
amagniﬁcation ofgrainbound-
aries and micro-cracks
Fig. 5a showing the surface of the T ungsten sample after
polishing and electrolytical etching.
The extensive cracking observed in additively manufac-
tured T ungsten is the result of the thermal stresses aris-
ing during rapid solidiﬁcation or recrystallization [ 19]. As
the temperature drops below the ductile to brittle transi-
tion temperature (DBTT), the residual stress rises above
the yield strength in the brittle material, resulting in a crack
formation. Micro-cracks that we can see in the SEM images
of Fig. 5b are like the intergranular hot cracking in fusion
welds in T ungsten. They originate from the aggregation
of nanopores at the grain boundaries. Wang et al. [ 20]
demonstrated that the formation of nanopores can be as-
cribed the boiling tungsten oxides (WOx) in the hot melting
pool. These gas pores are pushed into grain boundaries
during rapid solidiﬁcation.
Wang et al. [ 21] observed that a differentiation of scan-
ning strategy and re-melting cannot suppress the cracks,
the only effect is a redistribution and change in the shape
of defects. With a substrate preheating of 1000 °C, there
is a reduction, but no complete mitigation of the micro-
cracks [ 22]. Therefore, the only way to avoid cracking on
SLM T ungsten is to eliminate or control the impurities. This
is possible in two ways, the ﬁrst one consists in avoiding
any contact of the powder with an oxidizing atmosphere
throughout the complete process route, the second way,
more feasible, is by alloying it [ 23, 24].
4. Conclusion
In this contribution, the production of fully dense T ungsten
specimens has been optimized starting from an analytical
method. The process quality was quantiﬁed with the high
value of density achieved of 99.6%.
Continuous and homogeneous Single Scan T racks
(SSTs) of W were produced and measured. SSTs studying
allows also to deﬁne the window of optimal laser power
process parameters in order to produce intact contour, thin
wall, and lattice structures.
The micro-hardness measured in fully dense T ungsten
(420 HV) specimens was slightly higher than commercial
and SPS T ungsten [25].
T ungsten processed by LPBF shows its tendency toward
hot cracking. The strong presence of cracks leads to the con-
clusion that this material is not suitable to be processed by
SLM in the current form. The investigation is in progress
to understand if there is the po ssibility to use them as tra-
ditional pure T ungsten components or rather in non-struc-
tural applications.
Funding. OpenaccessfundingprovidedbyPolitecnicodiMilanowithinthe
CRUI-CAREAgreement.
Open Access This article is licensed under a Creative Commons Attribu-
tion 4.0 International License, which permits use, sharing, adaptation,
distribution and reproduction in any medium or format, as long as you
give appropriate credit to the original author(s) and the source, provide a
link to the Creative Commons licence, and indicate if changes were made.
The images or other third party material in this article are included in the
article’ s Creative Commons licence, unless indicated otherwise in a credit
line to the material. If material is not included in the article’ s Creative
Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permis-
sion directly from the copyright holder. T o view a copy of this licence, visit
http://creativecommons.org/licenses/by/4.0/.
References
1 . Shabalin, I. L.: Ultra-High T emperature Materials I, A Comprehen-
sive Guide and Reference Book, Dordrecht: Springer, 2014
2. Hirai, T .; Panayotis, S.; Barabash, V .; Amzallag, C.; Escourbiac, F .;
Durocher, A.; Merola, M.; Linke, J.; Loewenhoff, T .; Pintsuk, G.;
Wirtz, M.; Uytdenhouwen, I.: Use of tungsten material for the ITER
divertor, Nuclear Materials and Energy, 9 (2016), pp 616–622
3. Wauthle, R.; Van Der Stok, J.; Yavari, S. A.; Van Humbeeck, J.; Kruth,
J. P .; Zadpoor, A. A.; Weinans, H.; Mulier, M.; Schrooten, J.: Addi-
tively manufactured porous tantalum implants, Acta Biomaterialia,
14 (2015), pp 217–225
4. Zhang, H.; Xu, W.; Xu, Y .; Lu, Z.; Li, D.: The thermal-mechanical
behavior of WT aMoNb high-entropy alloy via selective laser melt-
ing (SLM): experiment and simulation, International Journal of Ad-
vanced Manufacturing T echnology, 96 (2018), pp 461–474
5. Balla, V . K.; Bodhak, S.; Bose, S.; Bandyopadhyay, A.: Porous
tantalum structures for bone implants: Fabrication, mechanical
and in vitro biological properties, Acta Biomaterialia, 6 (2010),
pp 3349–3359
6. T an, C.; Zhou, K.; Ma, W.; Attard, B.; Zhang, P .: Selective laser melt-
ing of high-performance pure tungsten : parameter design , densiﬁ-
cation behavior and mechanical properties, Science and T echnology
of Advanced Materials, 6996 (2018), pp 1–1 1
7 . Kline, S. J.; McClintock, F . A.: Describing uncertainties in single-
sample experiments, Mechanical Engineering, 75(1953), no 1, pp
3–8
8. Zhou, X.; Liu, X.; Zhang, D.; Shen, Z.; Liu, W.: Ba lling phenomena
in selective laser melted tungsten, Journal of M aterials Processing
T ech., 222 (2015), pp 33–42
268 © The Author(s) Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5

## Page 7

Originalarbeit
9. Wang, D.; Yu, C.; Zhou, X.; Ma, J.; Liu, W.; Shen, Z.: Dense Pure
T ungsten Fabricated by Selective Laser Melting, Applied Sciences
2017 .https://doi.org/10.3390/app7040430
10. Zhang, J.; Gu, D.; Y ang, Y .; Zhang, H.; Chen, H.; Dai, D.; Lin, K.:
Inﬂuence of Particle Size on Laser Absorption and Scanning T rack
Formation Mechanisms of Pure T ungsten Powder During Selective
Laser Melting, Engineering, 5 (2019), pp 736–745
1 1 . Spierings, A. B.; Voegtlin, M.; Bauer, T .; Wegener, K.: Powder
ﬂowability characterisation met hodology for powder-bed-based
metal additive manufacturing, Progress in Additive Manufacturing,
1 (2016), pp 9–20
12. Y adroitsev, I.; Bertrand, P .; Smurov, I.: Parametric analysis of the se-
lective laser melting process, Applied Surface Science, 253 (2007),
pp 8064–8069
13. Han, L.; Liou, F . W.; Musti, S.: Thermal behavior and geometry
model of melt pool in laser material process, Journal of Heat T rans-
fer, 127 (2005), pp 1005–1014
14. Bajaj, P .; Wright, J.; T odd, I.; Jägle, E. A.: Predictive process param-
eter selection for Selective Laser Melting Manufacturing: Applica-
tions to high thermal conductivity alloys, Additive Manufacturing,
27 (2019), pp 246–258
15. T ang, L.; Landers, R. G.: Melt pool temperature control for laser
metal deposition processes-part I: Online temperature control,
Jour-
nal of Manufacturing Science and Engineering, T ransactions of the
ASME, 132 (2010), pp 0110101–0110109
16. Gu, D.; Hagedorn, Y . C.; Meiners, W.; Meng, G.; Batista, R. J. S.;
Wissenbach, K.; Poprawe, R.: Densiﬁcation behavior, microstruc-
ture evolution, and wear performance of selective laser melting
processed commercially pure titan ium, Acta Materialia, 60 (2012),
pp 3849–3860
17 . Wen, S.; Wang, C.; Zhou, Y .; Duan, L.; Wei, Q.; Y ang, S.: High-den-
sity tungsten fabricated by selective laser melting : Densi ﬁ cation ,
microstructure , mechanical and thermal performance, Optics and
Laser T echnology, 1 16 (2019), pp 128–138
18. Liu, G. Y .; Ni, S.; Song, M.: Effect of indentation size and grain/sub-
grain size on microhardness of high purity tungsten, T ransactions
of Nonferrous Metals Society of China (English Edition), 25 (2015),
pp 3240–3246
19. Budaev, V . P .; Martynenko, Y . V .; Karpov, A. V .; Belova, N. E.;
Zhitlukhin, A. M.; Klimov, N. S.; Podkovyrov, V . L.; Barsuk, V . A.;
Putrik, A. B.; Y aroshevskaya, A. D.; Giniyatulin, R. N.; Safronov,
V . M.; Khimchenko, L. N.: T ungsten recrysta llization and cracking
under ITER-relevant heat loads, Journal of Nuclear M aterials, 463
(2015), pp 237–240
20. Wang, D.; Wang, Z.; Li, K.; Ma, J.; Liu, W.; Shen, Z.: Cracking in
laser additively manufactured W: Initiation mechanism and a sup-
pression approach by alloying, Materials and Design, 162 (2019),
pp 384–393
21 . Wang, D. Z.; Li, K. L.; Yu, C. F .; Ma, J.; Liu, W.; Shen, Z. J.: Cracking
Behavior in Additively Manufactured Pure T ungsten, Acta Metallur-
gica Sinica (English Letters), 32 (2019), pp 127–135
22. Müller, A.; Schlick, G.; Neu, R.; Anstätt, C.; Klimkait, T .; Lee, J.;
Pascher, B.; Schmitt, M.; Seidel, C.: Additive manufacturing of pure
tungsten by means of selective laser beam melting with substrate
preheating temperatures up to 1000 ○ C, Nuclear Materials and En-
ergy, 19 (2019), pp 184–188
23. Kaserer, L.; Braun, J.; Stajkovic, J.; Leitz, K. H.; T abernig, B.; Singer,
P .; Letofsky-Papst, I.; Kestler, H.; Leichtfried, G.: Fully dense and
crack free molybdenum manufactured by Selective Laser Melting
through alloying with carbon, International Journal of Refractory
Metals and Hard Materials, 84 (2019), p. 105000
24. Omidvari, N.; Vrancken, B.; Lietaert, K.; Vanmeensel, K.; Vleugels,
J.; Kruth, J.: Selective laser melting of tungsten and tungsten alloys,
International Journal of Refractory Metals and Hard Materials 72
(2018), pp 27–32
25. Choi, J.; Sung, H. M.; Roh, K. B.; Hong, S. H.; Kim, G. H.; Han, H.
N.: Fabrication of sintered tungsten by spark plasma sintering and
investigation of thermal stability, International Journal of Refractory
Metals and Hard Materials, 69 (2017), pp 164–169
Publisher’s Note.SpringerNatureremainsneutralwithregardtojurisdictional
claimsinpublishedmapsandinstitutionalaﬃliations.
Berg Huettenmaenn Monatsh (2021), 166. Jg., Heft 5 © The Author(s) 269
