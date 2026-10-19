# Near crack free additive manufacturing of a novel W-Nb-C alloy

<!-- source: D:\总文献\Near crack free additive manufacturing of a novel W-Nb-C alloy.pdf -->
<!-- file_sha256: 3a84a235415a53b2c15a3b0a453b9e3ce6ef19aaf4c80b4d92691debf2df3def -->

## Page 1

Materials Research Letters
ISSN: 2166-3831 (Online) Journal homepage: www.tandfonline.com/journals/tmrl20
Near crack free additive manufacturing of a novel
W-Nb-C alloy
Prithvi D. Awasthi, Abhijeet Dhal, Fredrick N. Michael & Rajiv S. Mishra
To cite this article: Prithvi D. Awasthi, Abhijeet Dhal, Fredrick N. Michael & Rajiv S. Mishra
(2025) Near crack free additive manufacturing of a novel W-Nb-C alloy, Materials Research
Letters, 13:1, 67-75, DOI: 10.1080/21663831.2024.2419475
To link to this article: https://doi.org/10.1080/21663831.2024.2419475
© 2024 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group.
Published online: 30 Oct 2024.
Submit your article to this journal 
Article views: 1731
View related articles 
View Crossmark data
Citing articles: 4 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tmrl20

## Page 2

MATER.RES.LETT.
2025,VOL.13,NO.1,67–75
https://doi.org/10.1080/21663831.2024.2419475
ORIGINAL REPORT
Near crack free additive manufacturing of a novel W-Nb-C alloy
Prithvi D. Awasthia,b, Abhijeet Dhala, Fredrick N. Michaelc and Rajiv S. Mishraa,b
aDepartmentofMaterialScienceandEngineering,UniversityofNorthTexas,Denton,TX,USA; bCenterforAgileandAdaptiveAdditive
Manufacturing,UniversityofNorthTexas,Denton,TX,USA; cMaterials&ProcessesLaboratory,MarshallSpaceFlightCenter,National
AeronauticsandSpaceAdministration,Huntsville,AL,USA
ABSTRACT
The high ductile brittle transition temperature of tungsten (W) poses challenges like cracking and
porosity during its laser-powder bed additive manufacturing (L-PBFAM). Computational alloy design
evaluated niobium (Nb) and carbon (C) to activate eutectic solidification, addressing the cracking
issues during the terminal stage of solidification. Furthermore, these elements prevent O segrega-
tion at grain boundaries, thereby enhancing grain boundary cohesion in W. In combination with
effective process parameters, the novel W-Nb-C alloy developed for L-PBFAM produces near crack-
free specimens with heterogeneous microstructures. The intrinsic mechanical responses associated
with the heterogenous microstructure were delineated by nanoindentation analysis.
IMPACT STATEMENT
Novel W-Nb-C alloy yields near crack-free component via L-PBFAM. It demonstrates good printability
without compromising mechanical and high-temperature properties.
ARTICLE HISTORY
Received11May2024
KEYWORDS
Tungstenalloy;alloydesign;
laser-powderbedadditive
manufacturing;
nanoindentation
Introduction
The rising demand for high-temperature materials for
extreme engineering applications (e.g. in space propul-
sion vehicle, nuclear fusion reactor, etc.) has driven
research on laser-powder bed fusion additive manufac-
turing (L-PBFAM) of refractory alloys [1–5]. One of the
refractory metals that has taken significant scientific and
commercial appeal is tungsten (W), due to its superior
elastic stiffness, high density, excellent thermal conduc-
tivity, good mechanical stability at elevated temperature,
andrelativeabundance.WandW-richalloysareusedas
ignitiontubesforrocketengines,fusion-facingtiles,heat
sinks, and pinhole collimators; parts that involve intri-
c a t eg e o m e t r i e s ,h i g ha s p e c tr a t i o ,a n dc l o s et o l e r a n c e s
[1,2,6]. This makes their fabrication via conventional
manufacturing processes costly and ineffective, under-
scoring the need for novel manufacturing routes such as
L-PBFAM. However, the production of W components
using the L-PBFAM faces significant challenges due to
CONTACT RajivS.Mishra rajiv.mishra@unt.edu DepartmentofMaterialScienceandEngineering,UniversityofNorthTexas,Denton,TX,76207,USA;
CenterforAgileandAdaptiveAdditiveManufacturing,UniversityofNorthTexas,Denton,TX,76207,USA
inherent problems such as cracking and porosity, which
are attributed to its low room temperature ductility and
highductile-to-brittletransitiontemperature(DBTT)in
therangeof150–450°C[7 –9].HotcrackinginWoccurs
primarily when the rapid solidification-induced residual
stressesexceedtheyieldstrengthofW(pureWhasvery
lowductilityintension).Additionally,poorgrainbound-
ary cohesion because of process-induced oxidation and
intragranular cracking due to insufficient liquid perme-
ation during solidification are other factors contributing
tocrackingduringL-PBFAMofW.
Attempts to suppress cracks by using suitable process
parametersandenvironmentalcontrolduringL-PBFAM
have reduced the crack density but have not eliminated
the issue completely. These attempts include: (i) keeping
the chamber O
2 levels below 100ppm, (ii) heating build
plates up to 1000°C, and (iii) various scanning strategies
accompanied by different laser power, scanning speed,
andhatchspacing[ 5,10].
©2024TheAuthor(s).PublishedbyInformaUKLimited,tradingasTaylor&FrancisGroup.
ThisisanOpenAccessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercialLicense( http://creativecommons.org/licenses/by-nc/4.0/),whichpermits
unrestrictednon-commercialuse,distribution,andreproductioninanymedium,providedtheoriginalworkisproperlycited. Thetermsonwhichthisarticlehasbeenpublishedallow
thepostingoftheAcceptedManuscriptinarepositorybytheauthor(s)orwiththeirconsent.

## Page 3

68 P. D. AWASTHI ET AL.
An alternative and more fundamental approach to
increasing ductility and preventing cracks in conven-
tional manufacturing (powder metallurgy route) of W
has been through alloying, which has not been explored
significantly in additive manufacturing [7]. Crack-free
microstructures have been reported in W-heavy alloys,
however, such alloys lose high-temperature properties
[11,12]. Multiple studies have reported that alloying W
withT aandNbreducescrackdensitywhencomparedto
pure W, but the complete elimination of cracks remains
a main issue [13–15]. Furthermore, the mechanical per-
formance of these alloys is inferior due to premature
cracking and limited plasticity. Factors influencing lim-
itedplasticityofWare:(i)body-centeredcubicstructure
that inherently lacks closed pack planes, (ii) high fric-
tional (Peierls) stress of W, and (iii) low grain bound-
ary cohesion leading to premature fracture. In this view,
novel W-rich alloys for L-PBFAM need to be developed
withgreaterprintability-performancesynergyinfocus.
And, another yet related alternative, complementary
to the alloying approach, is that of the addition of dis-
persoids as nano-inclusions. Mixing nanoparticles with
W-powders has remarkably led to crack mitigation dur-
ingL-PBFAM[ 16].Thiswillbegenerallytrueforrefrac-
torymetalsandtheiralloysasthenanometersscalemetal
oxides (MO) and metal carbides (MC) if un-melted or
even if partially melted at the appropriate solidification
range will act as copious nucleation sites lending them-
s e l v e st ot h ec r e a t i o no fm a n ym o r er e fi n e da n dr e l a -
tively equiaxed grains. If blended in with powder and
wellmixed,theseevenifmeltedfullywilladdequivalent
amounts of weight percent of the elemental constituents
in a well dispersed and mixed way in the melt solution
and may also contribute to the localin-situreformation
of nanoscale phases that will also drive nucleation and
grainrefinement.
Mishra and Thapliyal have presented a modified
Olsen-Cohen systems approach as an effective strategy
to develop crack-free, high-performance novel Al alloys
and damage-tolerant high entropy alloys for L-PBFAM
[17,18]. This study applies a similar computational alloy
designframeworktoidentifyW-richalloysthatcaneffec-
t i v e l ya d d r e s st h ei s s u eo fc r a c k i n gi nL - P B F A Ma n d
simultaneously enhance mechanical properties in the
finalcomponent.Forthispurpose,thermodynamicmod-
els including Scheil-Gulliver solidification simulations
(SGSS) wereemployed. Successful near crack-freeprint-
ing of a novel W-Nb-C alloy with minimal porosity was
achieved, and the contributing factors have been ana-
lyzed and discussed. The microstructure and associated
mechanicalpropertiesofvariousmicrostructuralentities
havebeencharacterizedandcorrelatedforacomprehen-
siveunderstandingofthealloy.
Methods and materials
For the alloy design, ThermoCalc 2023a (with TCHEA-
6 database) was utilized. Phase diagrams and SGSS plots
to understand the solidification kinetics of the W-alloys
as a function of alloying compositions were computed.
Basedonmultipleiterations,anoptimumcompositionof
89.55W-10Nb-0.45C (wt.%) was determined to have the
potential for superior printability-performance synergy.
Commercially pure W and Nb powders were sourced
from H.C. Starck GmbH and high purity C powders
weresourcedfromNanoshelUK.Thepurepowderswere
sieved using−325 mesh. Following this, powders corre-
sponding to the novel composition were measured and
mixedusingaplanetaryballmillfor8hoursusingstain-
lesssteelballsat200rpm.Micro-tracS3500analyzerwas
used to measure the size distribution of powders. LECO
ON736 and C844 were used to measure the amount of
O
2 andCpresentinthepowders,respectively.Thepow-
ders were then put in a rotary mixer for another 8hours
forfurthermixing,followedbydryingat80°Ctoremove
any moisture before loading into the supply chamber of
the L-PBFAM machine. Aconity MIDI equipped with a
1000W laser of 80
µmb e a ms i z ew a su s e dt om a n u f a c -
ture 10×10 ×8mm3 coupons. The substrate tempera-
ture was set to 600°C (significantly above DBTT of W)
throughout the entire build. L-PBFAM was performed
using 900W power and 600mm/s scanning velocity.
Layer thickness was set at 50
µma n dh a t c hs p a c i n gw a s
100 µm with an interlayer rotational angle of 67°. The
substrate plate was heated to 600°C, which is above the
DBTTofW.TheO 2 levelinthebuildchamberwasmain-
tained below 10ppm throughout the build. Once the
sampleswereprinted,electricdischargemachine(EDM)
was used to cut sample for characterization along the
builddirection.Densitymeasurementsweretakenusing
the ASTM-B311 standard. The samples were polished
p r e c i s e l yu s i n gas e r i e so fd i a m o n dl a p p i n gp l a t e sf o l -
lowed by cloth-polishing using a 0.02
µm colloidal silica
suspension inan AlliedMultiprep semi-automatichigh-
precision polisher. Microstructural analysis was done
usingaThermoFischerScientificApreo2scanningelec-
tronmicroscope(SEM)equippedwithenergydispersive
spectroscopy (EDS) and Trinity detection system con-
sisting of three in-lens/in-column back scattered elec-
tron(BSE)andsecondaryelectron(SE)detectors.Images
from multiple locations with various levels of magnifi-
cation were captured to comprehend the heterogenous
distributionofdifferentphasespresentinthemicrostruc-
ture. Vickers microhardness measurements were carried
out on a Buehler Wilson VH3300 auto hardness tester
with a nominal load of 500g with dwell time of 10s.
The microhardness test captures the average mechanical

## Page 4

MATER. RES. LETT. 69
response in the scale of melt pools. To delineate the
mechanical heterogeneity and understand the mechan-
ical behavior of various phases within a single melt pool
nanoindentation was performed using FemtoTools FT-
NMT04 nanomechanical testing unit. A sphero-conical
tipwithanapexradiusof5
µmwasusedtomakeindents
in a 2×20 grid pattern with an inter-indent spacing of
10 µm,andthetestwasperformedincontinuousstiffness
measurementmode.Post-indentationSEMmicrography
wasperformedtoconfirmthelocationoftheindentation
gridwithrespecttothemeltpool.
Results
Figure 1(a) shows the pseudo-binary phase diagram
of (W-10Nb)-C, where liquid+BCC phases exist in
hypoeutectic region at 0.45 wt.% C. A transition is
observed near 2750°C where liquid+BCC transforms
into BCC+FCC as outcome of eutectic transformation
of W and Nb with C. The SGSS (Figure1(b)) indicates
thatsolidificationstartsat3123°Candprogressessteeply
until 0.7mol fraction of solid (F
s) at 2748°C where the
growthofprimaryandsecondarydendritesisprominent
Figure 1. Thermodynamicsimulationsforalloydesign:(a)pseudo-binaryphasediagramof(W-10Nb)-C,(b)temperaturevsmolefrac-
tion of solid present in melt pool based on SGSS, (c) formation of diﬀerent phases and volume fraction of phases as function of pool
temperatureduringcooling,and(d)componentsinFCC-carbidephaseasafunctionofpooltemperature.

## Page 5

70 P. D. AWASTHI ET AL.
Figure 2. W-Nb-C powder characterization (a) SEM image showing polyhedral powder morphology, (b) EDS map, and (c) statistical
quantiﬁcationofpowdersize.
because of rapid solidification. Following this, a region
of eutectic solidification is observed tillFs = 1 allowing
for the remaining liquid to flow between dendritic arms
creating channels consisting of BCC and FCC phase.
AnalysisofFigure 1(c,d)indicatethatathighertempera-
tures, the FCC phase composition consists of W, Nb and
C, but as the melt pool cools, W gets depleted and Nb
and C becomes more dominant. This indicates a copre-
cipitatedcarbideofWandNbsegregatedduringeutectic
solidification.
Figure 2(a) shows the polyhedral-shaped W and
Nb powders used in this work because of their cost-
efficiency. Figure2(b) shows an EDS map with the dis-
tribution of W (red) and Nb (yellow) powders. The
size distribution of the sieved powders is represented in
Figure 2(c). A layer size of 50
µm was chosen as 90%
o ft h ep o w d e rp a r t i c l e sw e r es m a l l e rt h a n5 3µm. The
powder contained 0.104±0.002 wt.% O2, possibly from
o x i d el a y e r sf o r m e da r o u n dp o w d e r s ,a n dt h eCc o n t e n t
was 0.486±0.009 wt.%, which was comparable to the
amount addedin composition.
Figure 3 shows the microstructure of the L-PBFAM
W-Nb-C alloy along the build direction. Defects in the
form of spherical and aspherical pores were detected,
although cracks were not observed (Figure3(a)). Den-
sity measurement of the alloy computed a value of
15.61g/cm
3. Considering theoretical density of the
present alloy composition as 16.81g/cm3,t h er e l a t i v e
density of the build is calculated as 93%. The variation
i nw i d t ha n dd e p t ho ft h em e l tp o o li nF i g u r e3(b) is
attributable to the 67° rotational angle between the suc-
ceeding layers. The region near the bottom of melt pool
mostly comprised of the W-Nb solid-solution (SS) with
coarse columnar Nb-rich phase segregation. Numerous
partially melted W powders were found, which likely
resulted from insufficient energy to completely liquify
all the powders. The partially melted W powders were
driven by Marangoni eddies during solidification and
disproportionately observedat thetop ofmelt pool. The
EDS map in Figure3(c) shows the qualitative elemen-
tal distribution between various phases. The region near
the partially melted W primarily composed of W-Nb SS
with minimal presence of C and O, whereas the darker
regionsurroundingthedendritesiscomposedofNb-rich
phasecontainingCandO,indicatingchanceofoxideand
carbidesinthese regions.Asnoted fromFigure 1(c),the
coprecipitatedcarbidephases((W
xNb1−x)-C1)arelastto
solidify via eutectic solidification and are expected to be
observed in segregation channels. Figure3(d,e) are high
magnificationimagesofvariousregionsfocusingondif-
ferentphasespresentinthemicrostructure.Uponcloser
investigation, dendritic segregation of various shapes
and sizes are observed from bottom to top of the melt
pool,furtheraidingtothemicrostructuralheterogeneity.
Fine scale precipitates can be seen in Figure3(f) sur-
rounded by the matrix phase. The EDS line scan (inset

## Page 6

MATER. RES. LETT. 71
Figure 3. Multi-scale microstructural characterization: (a) low magniﬁcation component scale image shows minimal pores near-crack
freebuild,(b)micrographspanningmultiplemeltpoolsshowspartiallymeltedWpowdersonthetopendofthepool,(c)highmagniﬁ-
cationimageofthetopregionandcorrespondingEDSmapsshowingthedistributionofW,Nb,CandO,(d,e)magniﬁedimagecapturing
ﬁne-scaledendritesandsurroundingcarbidesandoxides,and(f)trappedoxideandcarbideparticlesintheW-richSSmatrix,insetimage
showstheEDSlinescan.
of Figure3(f)) indicates enrichment of W and O in the
dark precipitate surrounded by a Nb-W-C rich phase.
V a r i a t i o ni nm e c h a n i c a lp r o p e r t i e si nc o m p o n e n t
scale is estimated by microhardness linescan
(Figure 4(a)). Vickers hardness values ranging from
401.5HV0.5 to 822.6HV0.5 depending on different loca-
t i o n si nt h eb u i l dw a so b s e r v e d .T h eh a r d n e s sv a l u e s
were high compared to many W alloys processed by
L-PBFAM [13,19,20] indicating improved mechanical
properties. Each microhardness indent corresponds to
a length scale equivalent of melt pool dimension and
therefore, captures the combined mechanical response
o ft h ep o o l .T h em i c r o s t ru c t u r a lh e t e r o g e n e i t yo b s e rv e d
in Figure3 is expected to impart wide variations in the
mechanical response within a single pool. To delineate
this mechanical heterogeneity, nanoindentation force-
displacement (P-h) curves of critical regions within the
pool (Figure 4(b)) were captured and analyzed. The
plastic region under the spherical tip is idealized as a
cylinder, and using the approach established by Parthak
and Kalidindi [21 ], local stress–strain curves were
derivedandplottedinFigure 4(d).Eachmicrostructural
constituent showed unique micromechanical behavior.
The P-h curves corresponding to partially melted W
regionsshowedtheloweststrengthandhighestplasticity
(Figure 4(c)). The rest of the three curves demonstrated

## Page 7

72 P. D. AWASTHI ET AL.
Figure 4. Nanoindentation investigation: (a) microhardness variation across the specimen height, (b) microstructure of indented
regions, (b1) top region, (b2) bottom region of pool, (c) correspondingP-h curves, (d) nanoindentation stress-strain curves showing
phase-dependentmechanicalresponse.
high strength and low plasticity which corresponded
to a composite microstructure consisting of W-Nb SS,
and/orcarbideandoxide-richsegregationchannels.Fur-
thermore, a remarkable elbow in the P-h curves was
observed, which correlates to massive recovery of elastic
strain during unloading. Detailed micromechanics will
bediscussedintheupcomingsection.
Discussion
Thepresentworkemploysacombinationofeffectivepro-
cess parameters and a novel alloy design strategy to suc-
cessfullymitigatecrackingissuesduringL-PBFAM.From
the processing standpoint, a heated substrate plate helps
to maintain the build temperature significantly above
DBTT of W, thereby keeping it in a ductile state and
abatingtheresidualstressesduringL-PBFAM.Theinno-
vative alloy design also mitigates the cracking issues due
to its unique solidification and phase evolution kinet-
ics. During solidification, the dendritic coherency point
(DCP) corresponds to the stage (typically F
s > 0.65)
whendendritesformcoherentnetworksandimpingeon
each other; developing residual stress on contact points
between the dendritic tips. For the present W-Nb-C
alloy, eutectic solidification is achieved fromF
s of 0.7 to
1, which enables opportune permeation of liquid film
between the dendritic networks. The liquid film aids
in absorbing residual stresses between impinging den-
driticarms.Moreover,eutecticsolidificationreducesthe
growthrate,selectivelyloweringthecriticalsolidification
rangeafterDCP.Finally,minimalchangeintemperature
towards the terminal solidification stage (F
s = 0.98–1)
enablesgreaterresidencetimeoftheliquidfilm,enabling
effective liquid backfilling into the cracks, followed by
grain bridging upon complete solidification. Note that
h o tc r a c ks u s c e p t i b i l i t yi sh i g h e s ta tt h et e r m i n a ls o l i d -
ificationstage.
T h eo r i g i no fc r a c k si sn o tj u s tl i m i t e dt oh i g hr e s i d -
ual stresses but also to the O enrichment at the grain
boundary,resultinginpoorgrainboundarycohesionand
eventual cracking at the boundaries. Minimizing cham-
ber O
2 level helps in minimizing the O contamination

## Page 8

MATER. RES. LETT. 73
at the grain boundary to a significant level. The remain-
i n gOn e e d st ob ea d d r e s s e db ya l l o y i n ge l e m e n t st h a t
can alter oxidation kinetics and prevent grain bound-
ary contamination in W. The selection of Nb and C as
a l l o y i n ge l e m e n t sa i d si na c h i e v i n gt h i sf e a t .A p a r tf r o m
activating eutectic solidification, the presence of C also
facilitates reactions with O to form CO and CO
2 during
laser-powder interaction. When the temperature rises,
theenthalpyofformationtoformCOandCO
2 increases
comparedtometaloxides.Venables et al. showed that at
higher temperatures metal oxides such as WO3 dissoci-
ateintometalandOandtheproducedOreactswithCto
formCO
2 [22]. Additionally,theyalsoshowedthatwhen
CencountersW O3 above675°C,thereactiontakesplace
resultingintheformationofCOandCO 2.Throughsuch
reactions,theconcentrationofOinthemeltpoolismin-
imized, however, at the cost of gas pores formation by
entrapment of CO and CO
2 during rapid solidification,
as seen in Figure3(a). Note that due to its lower aspect
ratio,gasporespromoteisotropicstresslocalization,and
thereforedonotcontributetocatastrophicfailureinsim-
ilar order as hot-cracks and lack of fusion defects. Nb
alsoplaysanimportantpartinminimizinggrainbound-
a r yc o n t a m i n a t i o n ,a si ti sa c t sa sp r e f e r e n t i a le l e m e n t
f o ro x i d ef o r m a t i o nd u et ot h el o w e re n t h a l p yo ff o r -
mation (/Delta1H)o fN b
2O5 (−3.04eV) compared to WO2
(−2.04eV) and WO3 (−2.18eV) [10]. These solidifica-
tion phenomena synergistically prevent grain boundary
contamination in the W-rich phase.
The unique solidification thermokinetics of the novel
alloy help to retain its high melting temperature and
mechanical properties. The/Delta1Hof NbC (−0.458eV) is
lower than that of WC (−0.122eV) [10]. Consequently,
the addition of Nb and C favors the formation of NbC
i nt h em e l tp o o l ,w h i c hi sb e n e fi c i a la sN b Ce x h i b i t sa
highermeltingtemperatureof3600°CcomparedtoWC,
which has a melting temperature of 2870°C [23]. The
formation of such high melting temperature phases dur-
ing eutectic solidification do not compromise the high-
temperature property of W alloy, which is a common
issueinmanyotherW-basedalloys(suchasW-Cu,W-Ti,
W-Ni alloys) developed for L-PBFAM, that form rela-
tively softer and low melting temperature phases during
solidification. Furthermore, the mechanical properties
of the carbide phases formed during eutectic solidifica-
tion are either higher or comparable with pure W. The
coprecipitatedcarbidepresentinthesegregationchannel
combined with their heterogenous distribution is favor-
able for further enhancing the mechanical response by
activating hetero-deformation and back-stress induced
strengthening[24].
High strength and limited plastic deformation pre-
vail among the heterogenous phase-specific mechanical
responses (Figure4(b–d)) in the W-Nb-C alloy. Based
on first-principal calculation, solute-dislocation interac-
tion energy (E
0
int) and Peierls misfit (τ′)a r ec a l c u l a t e d
as 0.048 and 0.211eV for W-Nb SS [25]. The posi-
tive value implies weak repulsive interactions with the
1
2 <111> screw dislocation, destabilizing the easy-core
geometry and promoting kink migration. As a result,
Nb-solute imparts SS hardening effect in W. Further-
more, the modulus mismatch imparts high elastic strain
at incoherent W-NbC interface. The maximum elastic
modulus of W is reported to be 405GPa, compared to
535GPa for NbC and 630GPa for WC via nanoinden-
tation [26–28]. Introduction of Nb in W influences the
elasticmodulusnegatively[ 29].Therateofelasticrecov-
eryduringnanoindentationdependsonrelativefraction
of W-Nb SS and carbide rich segregation in the interac-
tion volume under the tip (Figure4(c)). In the region
with very fine segregation spacing, density of W-Nb SS
interface with fine scale carbides is highest, leading to
v e r yl a r g ee l b o wi nt h eu n l o a d i n gc u r v e( F i g u r e4(c)).
The strength at peak load captures the cumulative effect
of lattice stress of material under the tip, and extrinsic
factor which influences the dislocation storage capabil-
ity (work hardening) of the material during indentation.
The intrinsic lattice stress of NbC is higher than W, and
t h er e l a t i v ev o l u m ef r a c t i o no fW - N bS Si sh i g hi nb o t h
red and blue marked region in Figure4(b
1,b2). The dis-
locationstoragecapabilitydependsonthemeanfreepath
ofdislocationmotion,whichdependsonthesegregation
spacingenrichedwithNbCprecipitates,ishigherinblue
region.Therefore,theblueregionshowshigheststrength
duetobothintrinsicandextrinsicfactors.Thisindicates
the heterogenous microstructure developed by eutectic
solidificationiseffectiveinenhancingthestrengthofthe
novelW-Nb-Calloy.
Conclusion
In the present work, a novel ternary W-10Nb-0.45C
(wt.%) alloy was designed for L-PBFAM using a compu-
tational approach. Successful fabrication of near crack-
free coupons was achieved. This compositional design
strategy employs two major ideas for eliminating cracks:
(i) eutectic compositions to minimize the effects of
thermal residual stress, and (ii) the use of C to form
CO and CO
2 that reduces the amount of oxygen in
the melt pool. The formation of hierarchical heteroge-
neousmicrostructuresconsistingofW-Nbsolid-solution
(SS), Nb-rich eutectic, and carbides results in wide
v a r i a t i o ni nm e c h a n i c a lr e s p o n s et h a ti sb e n e fi c i a lf o r
high-temperature applications. The complete melting
of W-powders was not achieved resulting in the non-
homogeneous distribution of alloying elements. This

## Page 9

74 P. D. AWASTHI ET AL.
i s s u ec o u l db em i t i g a t e di nf u t u r es t u d i e sb ys e l e c t i n g
smaller powder sizes, using a combination of power and
scanningspeedtoincreasetheenergydensityofthemelt-
pool as well as employing re-melt scan strategy during
printing.Theuseofpre-alloyedpowdercanalsoalleviate
thisissue,whilesimultaneouslyscalingupfromthecur-
rentprototypingstage.Furthermore,thisstrategyofalloy
d e s i g nc a nbeu s e dt oi d e n t i fyo t h e rW - a l l o ys y s t e m sf o r
successfulprintingofnearcrack-freecomponents.
Acknowledgements
The authors acknowledge the Center for Agile and Adaptive
Additive Manufacturing (CAAAM) at the University of North
T exasforaccesstothepowderassessmentandlaserpowderbed
fusionadditivemanufacturingfacilities.
Disclosure statement
No potential conflict of interest was reported by the authors.
Funding
This work was supported by NASA under grant number
#80NSSC21M0273.
Credit authorship contribution statement
Prithvi D. Awasthi: Methodology, Formal analysis, Valida-
tion, Investigation, Data Curation, Visualization, Writing —
Original Draft. Abhijeet Dhal: Investigation, Formal analy-
sis, Writing — Review & Editing.Fredrick N. Michael: Con-
ceptualization, Methodology, Funding acquisition, Writing —
review&editing. Rajiv S. Mishra:Conceptualization,Funding
acquisition,Formalanalysis,Writing—review&editing.
References
[1] TalignaniA,SeedeR,WhittA,etal.Areviewonadditive
manufacturingofrefractorytungstenandtungstenalloys.
AdditManuf. 2022;58:103009.doi:10.1016/j.addma.2022.
103009
[2] Morcos P, Elwany A, Karaman I, et al. Review: addi-
tive manufacturing of pure tungsten and tungsten-based
alloys. J Mater Sci. 2022;57:9769–9806. doi:10.1007/
s10853-022-07183-y
[3] Awasthi PD, Agrawal P, Haridas RS, et al. Mechanical
properties and microstructural characteristics of addi-
tively manufactured C103 niobium alloy. Mater Sci Eng
A.2022;831:142183.doi:10.1016/j.msea.2021.142183
[4] Chesetti A, Banerjee S, Dasari S, et al. 3D printable
low density B2+BCC refractory element based com-
plex concentrated alloy with high compressive strength
and plasticity. Scr Mater.2023;225:115160. doi:10.1016/j.
scriptamat.2022.115160
[5] Sharma S, Krishna KVM, Joshi SS, et al. Laser based
additive manufacturing of tungsten: multi-scale thermo-
kinetic and thermo-mechanical computational model
and experiments. Acta Mater.2023;259:119244. doi:10.
1016/j.actamat.2023.119244
[6] Müller Av, Dorow-Gerspach D,Balden M,etal.Progress
in additive manufacturing of pure tungsten for plasma-
facing component applications. J Nucl Mater.2022;566:
153760.doi:10.1016/j.jnucmat.2022.153760
[7] RenC,FangZZ,KoopmanM,etal.Methodsforimprov-
ingductilityoftungsten-Areview.IntJRefractMetHard
Mater. 2018;75:170–183. doi:10.1016/j.ijrmhm.2018.04.
012
[8] Yin C, Terentyev D, Zhang T, et al. Ductile to brit-
tle transition temperature of advanced tungsten alloys
for nuclear fusion applications deduced by miniaturized
three-point bending tests. Int J Refract Met Hard Mater.
2021;95:105464.doi:10.1016/j.ijrmhm.2020.105464
[ 9 ]C h e nJ ,L iM ,L iK ,e ta l .C r a c k i n gm e c h a n i s m si na d d i -
tively manufactured pure tungsten from printing single
tracks,thinwallsandcubes.MaterDes. 2023;234:112363.
doi:10.1016/j.matdes.2023.112363
[10] IvekovićA,OmidvariN,VranckenB,etal.Selectivelaser
meltingoftungstenandtungstenalloys.IntJRefractMet
Hard Mater.2018;72:27–32. doi:10.1016/j.ijrmhm.2017.
12.005
[11] WangM,LiR,YuanT,etal.SelectivelasermeltingofW-
Ni-Cu composite powder: densification, microstructure
evolution and nano-crystalline formation. Int J Refract
Met Hard Mater. 2018;70:9–18. doi:10.1016/j.ijrmhm.
2017.09.004
[12] Zhang DQ, Liu ZH, Cai QZ, et al. Influence of Ni
content on microstructure of W–Ni alloy produced by
s e l e c t i v el a s e rm e l t i n g .I n tJR e f r a c tM e tH a r dM a t e r .
2014;45:15–22.doi:10.1016/j.ijrmhm.2014.02.007
[13] LiJ,W eiZ,ZhouB,etal.Preparation,microstructure,and
microhardnessofselectivelaser-meltedW–3Tasample.J
Mater Res.2020;35:2016–2024.doi:10.1557/jmr.2020.71
[14] Xue J, Feng Z, Tang J, et al. Selective laser melting addi-
tive manufacturing of tungsten with niobium alloying:
microstructure and suppression mechanism of microc-
racks. J Alloys Compd.2021;874:159879. doi:10.1016/j.
jallcom.2021.159879
[15] Li K, Ma G, Xing L, et al. Crack suppression via in-situ
oxidation in additively manufactured W-Ta alloy. Mater
Lett.2020;263:127212.doi:10.1016/j.matlet.2019.127212
[ 1 6 ]Z h o uY ,C h eY - S ,W a n gC ,e ta l .S e l e c t i v el a s e rm e l t -
ing high-performance ZrC-reinforced tungsten compos-
ites with tailored microstructure and suppressed crack-
ing susceptibility. Tungsten.2021;3:72–88.
 doi:10.1007/
s42864-021-00076-8
[17] Mishra RS, Thapliyal S. Design approaches for print=
ability-performancesynergyinAlalloysforlaser-powder
bedadditivemanufacturing.MaterDes. 2021;204:109640.
doi:10.1016/j.matdes.2021.109640
[18] Dhal A, Thapliyal S, Agrawal P, et al. Multimodal
and multiscale strengthening mechanisms in Al-Ni-Zr-
Ti-Mn alloy processed by laser powder bed fusion
additive manufacturing. Mater Des. 2024;237:112602.
doi:10.1016/j.matdes.2023.112602
[19] HuZ,ZhaoY,GuanK,etal.Puretungstenandoxidedis-
persionstrengthenedtungstenmanufacturedbyselective
laser melting: microstructure and cracking mechanism.
microstructure and cracking mechanism. Addit Manuf.
2020;36:101579.doi:10.1016/j.addma.2020.101579
[20] Guo M, Gu D, Xi L, et al. Selective laser melting addi-
tive manufacturing of pure tungsten: role of volumetric

## Page 10

MATER. RES. LETT. 75
energy density on densification, microstructure and
mechanical properties. Int J Refract Met Hard Mater.
2019;84:105025.doi:10.1016/j.ijrmhm.2019.105025
[21] PathakS,KalidindiSR.Sphericalnanoindentationstress–
strain curves. Mater Sci Eng R Rep. 2015;91:1–36.
doi:10.1016/j.mser.2015.02.001
[ 2 2 ]V e n a b l e sD S ,B r o w nM E .R e d u c t i o no ft u n g s t e no x i d e s
with hydrogen and with hydrogen and carbon. Ther-
mochim Acta. 1996;285:361–382. doi: 10.1016/0040-
6031(96)02951-6
[23] CastleE,CsanádiT,GrassoS,etal.Processingandproper-
ties of high-entropy ultra-high temperature carbides. Sci
Rep.2018;8:8609.doi:10.1038/s41598-018-26827-1
[24] ZhuY,WuX.Perspectiveonhetero-deformationinduced
(HDI) hardening and back stress. Mater Res Lett.
2019;7:393–398.doi:10.1080/21663831.2019.1616331
[ 2 5 ]H uY - J ,F e l l i n g e rM R ,B u t l e rB G ,e ta l .S o l u t e - i n d u c e d
solid-solution softening and hardening in bcc tungsten.
Acta Mater. 2017;141:304–316. doi:10.1016/j.actamat.
2017.09.019
[26] Yu H, Das S, Yu H, et al. Orientation dependence of the
nano-indentation behaviour of pure tungsten. Scr Mater.
2020;189:135–139.doi:10.1016/j.scriptamat.2020.08.014
[27] ZhangH,DeLucaF,WangH,etal.Deformation mecha-
nismofWCsinglecrystalsundernanoindentation:effects
of surface defects and orientation on pop-in and hys-
teresis. Int J Refract Met Hard Mater.2022;106:105850.
doi:10.1016/j.ijrmhm.2022.105850
[ 2 8 ]B a l k oJ ,C s a n á d iT ,S e d l á kR ,e ta l .N a n o i n d e n t a t i o na n d
t r i b o l o gyo fV C ,N b Ca n dZ r Cr e f r a c t o ryc a r b i d e s .JE u r
Ceram Soc.2017;37:4371–4377. doi:10.1016/j.jeurceram
soc.2017.04.064
[29] Liu W, Huang Y, Wang Y, et al. W–Ta–Nb solid solu-
tions prepared by vacuum arc melting: microstruc-
ture evolution and mechanical properties. Vacuum.
2023;212:111959.doi:10.1016/j.vacuum.2023.111959
