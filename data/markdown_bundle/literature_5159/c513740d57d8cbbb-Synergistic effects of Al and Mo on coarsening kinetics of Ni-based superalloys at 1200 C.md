# Synergistic effects of Al and Mo on coarsening kinetics of Ni-based superalloys at 1200 C

<!-- source: D:\总文献\Synergistic effects of Al and Mo on coarsening kinetics of Ni-based superalloys at 1200 C.pdf -->
<!-- file_sha256: 5b2611b9096868055623dc2c5f9290d50c3af7829c646a0132db6b58876e13db -->

## Page 1

Materials Research Letters
ISSN: 2166-3831 (Online) Journal homepage: www.tandfonline.com/journals/tmrl20
Synergistic eﬀects of Al and Mo on coarsening
kinetics of Ni-based superalloys at 1200°C
Mingzhe Li, Wenyue Zhao, Yi Ru, Yanling Pei, Shusuo Li & Shengkai Gong
To cite this article: Mingzhe Li, Wenyue Zhao, Yi Ru, Yanling Pei, Shusuo Li & Shengkai Gong
(2025) Synergistic eﬀects of Al and Mo on coarsening kinetics of Ni-based superalloys at
1200°C, Materials Research Letters, 13:2, 113-121, DOI: 10.1080/21663831.2024.2425772
To link to this article: https://doi.org/10.1080/21663831.2024.2425772
© 2024 The Author(s). Published by Informa
UK Limited, trading as Taylor & Francis
Group.
View supplementary material 
Published online: 11 Nov 2024.
Submit your article to this journal 
Article views: 848
View related articles 
View Crossmark data
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=tmrl20

## Page 2

MATER.RES.LETT.
2025,VOL.13,NO.2,113–121
https://doi.org/10.1080/21663831.2024.2425772
ORIGINAL REPORT
Synergistic effects of Al and Mo on coarsening kinetics of Ni-based superalloys
at 1200°C
Mingzhe Lia, Wenyue Zhaob,Y iR ub,c, Yanling Peib, Shusuo Lia,d and Shengkai Gongb,d
aResearchInstituteofAero-Engine,BeihangUniversity,Beijing,People’sRepublicofChina; bSchoolofMaterialsScienceandEngineering,
BeihangUniversity,Beijing,People’sRepublicofChina; cTianmushanLaboratory,Hangzhou,People’sRepublicofChina; dAECCGuizhouLiyang
AviationPowerCompanyLimited,Guizhou,People’sRepublicofChina
ABSTRACT
The interaction effects of γ -strengthening and γ ’-former elements have long troubled the alloying
design of superalloys, especially improvingγ ’-thermostability by Al addition against higher temper-
atures. Here we establish a thermodynamics-based phase-field model to reveal the γ ’-coarsening
kinetics at 1200°C for well-designed ternary Ni-based superalloys containing γ ’-former element Al
and γ -strengthening element Mo. The inhibition effect of Al on coarsening is interestingly enhanced
by Mo addition to signify their synergistic effects. The contributions of lattice misfit, diffusion coeffi-
cients and elemental partitioning are analysed by decoupling coarsening theories. And an estimation
method of the coarsening rate controlled by slow-diffusing element is also established.
IMPACT STATEMENT
Thermodynamics-based ternary phase-field simulations of superalloys signify the synergistic effect
of Al and Mo on inhibiting γ ’ coarsening and reveal the interaction between γ -strengthening and
γ ’-former elements.
ARTICLE HISTORY
Received19June2024
KEYWORDS
Single-crystalsuperalloy;
coarseningkinetics;
phase-ﬁeldsimulation;
multicomponentdiﬀusion
Introduction
Enhancingtheultra-hightemperaturemechanicalprop-
erties of Ni-based single-crystal (SX) superalloys is ben-
eficial for designing aero-engines with higher thrust-to-
weight ratios [1,2]. During servicing at ultra-high tem-
perature, γ
′phase in superalloys inevitably starts to dis-
solve, and its volume fraction decreases consequently.
Previousresearchhasshownthatthemechanicalproper-
tiesofSXsuperalloyswoulddecreasedramatically,when
the amount, size and morphology ofγ
′strengthening
phasedeviatefromtheiroptimalstates[ 3–5].Recently,a
seriesofSXsuperalloyshaveexhibitedexcellentmechan-
ical properties at 1200°C [6–8] .I no r d e rt og i v ef u l l
play ofγ’p r e c i p i t a t e st om a i n t a i nt h es t r e n g t ho fs u p e r -
alloys at ultra-high temperature, these newly-designed
superalloys are characterized by high contents of Al, Ta
CONTACT WenyueZhao wendyzhao56@buaa.edu.cn SchoolofMaterialsScienceandEngineering,BeihangUniversity,No.37XueyuanRoad,
Beijing100191,People’sRepublicofChina
Supplementaldataforthisarticlecanbeaccessedonlineat https://doi.org/10.1080/21663831.2024.2425772.
and Mo and obvious higher volume fractions ofγ’a sa
result [9,10]. Sinceγ’ coarsening is a typical diffusion-
controlled process in superalloys at high temperature,
the microstructural evolution of these SX superalloys at
ultra-hightemperaturemightbehavedifferentcompared
totraditionalNi-basedSXsuperalloys[11 ,12].Thecoars-
ening kinetics and mechanisms behind are required to
berevealedviaclarifyingthecomplexinteractionamong
differentalloyingelementscontrolledbytemperature.
Characterization techniques, such as synchrotron
radiationX-raydiffractionandneutrondiffraction,have
enabled the measurements of lattice misfit and residual
stress in superalloys at ultra-high temperatures [13–15].
The in-situ observation of the microstructure evolu-
tionofsuperalloysathighertemperatureusingscanning
electron microscopy are also emerging [16]. However,
©2024TheAuthor(s).PublishedbyInformaUKLimited,tradingasTaylor&FrancisGroup.
ThisisanOpenAccessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercialLicense( http://creativecommons.org/licenses/by-nc/4.0/),whichpermits
unrestrictednon-commercialuse,distribution,andreproductioninanymedium,providedtheoriginalworkisproperlycited. Thetermsonwhichthisarticlehasbeenpublishedallow
thepostingoftheAcceptedManuscriptinarepositorybytheauthor(s)orwiththeirconsent.

## Page 3

114 M. LI ET AL.
the in-situ quantitative studies on the γ′ coarsening
kinetics of superalloys at 1200°C by using experimental
methodsremainchallenging[5 ,9,10].Hence,mesoscopic
simulations have become powerful means to study the
entiremicrostructureevolutionofsuperalloysatanytem-
perature and time and to reveal the elemental effects,
thankstotheirclearphysicalmeaningsandmathematical
expressions[17–20].
The phase-field method has been widely used in sim-
ulation of microstructure evolution of superalloys, such
as γ
′precipitation [21–23], coarsening [23–26], rafting
[22,27–29], creep damage [30–33]a n do t h e rc o m p l e x
microstructuralevolution[ 34–36].However,thehighest
temperature applied in these simulations is 1100°C [34]
while most being below 850°C, the microstructure evo-
lution behaviour of superalloys at 1200°C has not been
simulated yet. Moreover, most of these simulations sim-
plify the composition field of Ni-based superalloys to a
binary Ni-Al model, in which the interaction between
solute components is neglected. For multi-component
simulations, existing models often require fitting near
equilibrium states in order to handle a wide composi-
tion domain [25,37–39]. In addition, some models have
tolimitthedrivingforceofphasetransitiontoensurethe
existingofcompositiongradientfordiffusionfluxcalcu-
lation[39,40].Inotherwords,thephase-fieldmodelthat
can freely expand to large range of elemental contents is
still absent for the microstructural evolution simulation
of superalloys. Therefore, we develop a ternary Ni-Al-
Mophase-fieldmodelcoupledwiththermodynamicand
kinetic databases in this work. Comprehensive simula-
tionstudiesonthemicrostructuralevolutionofSXsuper-
alloyswithdifferentcontentsofAlandMoat1200°Care
carried out by using this model. The synergistic effects
of Al and Mo on theγ
′ coarsening kinetics are dis-
cussed in detail, which is expected to guide the design
ofhigh-performanceSXsuperalloysappliedatultra-high
temperature.
Simulation methods
Ou rm od e le m p l o y sagr a n d - po t e n tiala p p r oa c h[41–43]
coupled with a thermodynamic database from Thermo-
Calc software [44] to perform the isothermal simula-
tions of Ni-Al-Mo at 1200°C. The field variables in the
simulationsrepresent:
• Phase-field variables φ indicate the phase fractions
such that φ
α = 1a ta n yp l a c ei nb u l kp h a s eα and
φα = 0atanyplacenotinbulkphase α,
• Compositionfield candci representsthespatialvaria-
tion of the chemical composition of diffusing compo-
nenti,
• Diffusionpotentialfield ˜µand ˜μi representsthediffer-
ence between the chemical potentials of solute com-
ponent i, and solvent component A, defined as˜μ
i =
μi − μA,
Thetotalenergyequationcanbeexpressedasfollows:
/Omega1(φ, ˜μ) =
∫
V
(ωint(φ) + ωbulk(φ, ˜μ) + ωel(φ))dV (1)
where ωint(φ) represents the interfacial energy [45],
ωbulk(φ, ˜µ) represents the chemical energy of the bulk
phases [41], ωel(φ) represents the elastic energy [23,45].
For details of each energy item, see Part 1 of Supple-
mentary Materials. The field variables evolve towards
minimizingthetotalenergy,andtheevolutionequations
canbewrittengenerallyas:
∂φ
α
∂t =− Lφ
δ/Omega1
δφα
(2)
∂ci
∂t =− ∇· ⃗ji =∇·
n∑
j
Mij(φ)∇˜μj (3)
∂ ˜μi
∂t =
n∑
j
/Theta1ij(φ)
(∂cj
∂t − ∂φα
∂t (cα
j −cβ
j )
)
(4)
where Lφ,i st h ei n t e r f a c i a lm o b i l i t y ;⃗ji is the flux of dif-
fusing componenti;Mij is the coefficient of the Onsager
matrixrelating ⃗ji tothediffusionpotentialofsolutej, /Theta1ij
isthethermodynamicfactormatrix.
Modellingadiffusion-controlledprocesslikecoarsen-
ing, the movement of the interface can be also regarded
as diffusion-controlled. Therefore, the interfacial mobil-
ityL
φ issettothelargestvalueavailablethattheinterface
profile is stable [24,26,46]. Considering the similarities
in the partitioning behaviours ofγ’-former elements Ta
andAl,aswellasbehavioursof γ-strengtheningelements
R e ,Wa n dM o ,t h i sw o r ks i m p l i fi e st h en e w l yd e s i g n e d
superalloys as ternary Ni-Al-Mo alloys to focus on the
key effects of Al and Mo components. The phase-field
modelsofthisseriesofNi-Al-Mosystemsareconstructed
accordingly,inthepremiseofhighervolumefractionsof
γ’ before aging at 1200°C. Reliable simulation parame-
ters are selected from existing experiments and simula-
tions[26,34,47],listedinTable 1.Thespecificcriteriafor
theseselectionscanbefoundinPart2ofSupplementary
Materials.
The simulations are initialized with a supercooledγ
phase and nucleation sites ofγ’ phase inserted using a
semi-random method at mean intervals of 80 nm. The
content of Al varies from 16.0 to 17.5 at. % and content

## Page 4

MATER. RES. LETT. 115
Table 1. Input parameters for the phase-ﬁeld simulations of Ni-Al-Mo alloys. (∗ Lattice misﬁt varies with alloy
composition).
Elasticconstantsof γ Elasticconstantsof γ’
Parameter Cγ
11 Cγ
12 Cγ
44 Cγ′
11 Cγ′
12 Cγ′
44
Value 215.5MPa 162.0MPa 77.6MPa 222.7MPa 164.2MPa 85.6MPa
Latticemisﬁt Interfaceenergy Interfacemobility Gridpoints Gridspacing Timestep
Parameter δγ/γ ′ σγ/γ ′ Lφ Nx dx dt
Value 0 ∼− 0.5%∗ 0.05J/m2 2.0e-12 512 1.0e-8m 1.0e-4s
of Mo varies from 4.0 to 7.0 at. %. An illustration of the
a l l o yc o m p o s i t i o no fa l ls i m u l a t i o n so nat e r n a r yp h a s e
diagram can be found in Part 3 of Supplementary Mate-
rials. The lattice misfitδ
γ/γ ′ = 2(aγ′−aγ )/(aγ′+aγ ),
correspondingtodifferentNi-Al-Moalloycompositions
areobtainedfromThermoCalcandlistedinTableS1.To
discuss the limiting effect of misfit stress on coarsening,
we also conducted simulations in which the composi-
tionandlatticemisfitweredecoupled.( δ
γ/γ ′wassettoa
fixedvalueas −0.3%forcomparison.Thisvalueischosen
basedontheusualvalueoftypicalNi-basedsingle-crystal
superalloyCMSX-4.)
Simulation results and discussion
The microstructural evolution of a series of Ni-Al-Mo
alloys with typical composition similar to real super-
alloys is simulated at 1200°C. Firstly, the steady-state
coarsening stage can be specified for all the simula-
t i o n so fN i - A l - M oa l l o y s( s e eP a r t4o fS u p p l e m e n -
tary Material). Coarsening kinetics of all these alloys
obey the cubic law ¯r
3
t − ¯r3
0 = KSIMt. The average size
of the precipitated phase (γ’p h a s e )i sd e n o t e da s¯rt,
while ¯r0 represents the initial average radius ofγ’p h a se .
We fit the data of steady-state coarsening stage by the
cubic law to obtain coarsening rateK
SIM for each alloy
composition. The effects on volume fraction ofγ′and
KSIM as Al and Mo content changing are plotted in
Figure1.
ForthealloyswithlowMocontentof4.0at.%,increas-
ingtheAlcontentfrom16.0at.%to17.5at.%significantly
increases the volume fraction and the coarsening rate of
γ′both as shown in Figure1(a), which are consistent
with the expectations of coarsening theory. In contrast,
increasing the Mo content from 4.0 at.% to 7.0 at.% in
the alloys with low Al content of 16.0 at.% reduces the
coarsening rate ofγ
′as shown in Figure1(b), although
thevolumefractionof γ′isalsoincreasedslightly.These
results are similar to those obtained by simulation at
800°C in Ref. [38]. It is worth noting that increasing the
Alcontentfrom16.0at.%to17.5at.%obviouslyreduces
the γ
′c o a r s e n i n gr a t e so ft h ea l l o y sw i t hh i g hM oc o n -
tent of 7.0 at.%, as shown in Figure1(c). Although their
descent degrees of the coarsening rates are smaller than
t h o s ei nt h el o w - A la l l o y sw i t hi n c r e a s i n gM oc o n t e n t ,
moreincreasesofvolumefractionshowinthesehigh-Mo
a l l o y sw i t hi n c r e a s i n gA lc o n t e n t .T h e s es u g g e s tap o s s i -
bilityininhibitingcoarseningwithmaintaininghigher γ
′
f r a c t i o na tt h es a m et i m eb yt h es y n e r g i s t i ce ff e c t so fA l
and Mo.
The γ/γ
′lattice misfit δγ/γ ′ is conventionally con-
sidered to have close relationship with microstructural
evolution,whichalsovarieswithalloycomposition.Spe-
cifictothealloyssimulatedhere,thealloyswithlowcon-
tent of Mo generally have positiveδ
γ/γ ′,w h i l et h eδγ/γ ′
b e c o m e sn e g a t i v ew i t hi n c r e a s i n gM oc o n t e n t .I n c r e a s -
ing Al content also slightly decreases the lattice misfit
both for low-Mo and high-Mo alloys. These variation
laws are self-consistent with those ofγ
′coarsening rate
varied with alloy composition, in which a more nega-
tive δ
γ/γ ′ results in a slower coarsening rate. Moreover,
althoughδγ/γ ′approachingtozerousuallyleadstoaran-
dom distribution of theγ′particles with spherical mor-
phologies, theγ′particles begin to align along the (001)
direction since theδγ/γ ′ become negative with increas-
ing Mo content in low-Al alloys (Figure1(b)). In order
t or e v e a lt h er o l eo fl a t t i c em i s fi tp l a y e di nt h ec o a r s -
ening kinetics controlled by Al and Mo, simulations of
thealloyswithfixed δ
γ/γ ′arealsoconductedascompar-
isons. However, similar synergistic effects of Al and Mo
stillpersists,indicatingthatfactorsotherthanlatticemis-
fit also play significant roles. We discuss the mechanism
behind in detailed later, in order to propose a new co-
regulation way by Al and Mo on the microstructure of
superalloys.
Phase-field modelling has superiorities in revealing
themicrostructureevolutionkinetics,benefitingfromits
explicitexpressionwithclearphysicalmeanings.Asillus-
tratedinFigure 2(a,b),wecalculatetheenergydensities,
which is the total energy divided by total volume. The
interface energy density keeps decreasing with time as
thedrivingforceforsteady-statecoarsening.Onthecon-
trary, the elastic energy density induced by lattice misfit
increases, as the resistance. This effect of lattice misfit
on coarsening is in debate, mainly because the effects
of diffusion [48], volume fraction [49] and coalescence

## Page 5

116 M. LI ET AL.
Figure 1. Thevolumefractionandcoarseningrateofγ ′variedwith(a)increasingAlcontentintheNi-(16.0 ∼17.5)Al-4.0Mo(at.%)alloy,
(b)increasingMocontentintheNi-16.0Al-(4.0 ∼7.0)Mo(at.%)alloyand(c)increasingAlcontentintheNi-(16.0 ∼17.5)Al-7.0Mo(at.%)
alloy. The morphologies of the alloys are represented by the composition ﬁeld of Mo after 20 s of steady-state coarsening at 1200°C.
The coloured solid lines represent the coarsening ratewhile the coloured dashed lines represent coarsening ratewhen lattice misﬁt is
decoupledandﬁxedat −0.3%.
[49–51] are not excluded. Therefore, we decompose the
simulatedcoarseningrate KSIM toanalysetheroleofeach
component. SinceKLSW is usually predicted by coars-
ening theory with zero volume fraction [52], the rela-
tionship betweenKSIM and KLSW can be represented by
theratio f(ϕγ′
) = KSIM
KLSW > 1,whichmakesthesimulated
KSIM always larger than the theoreticalKLSW.T h i sr a t i o
f is also called ‘relative coarsening rate’ [12,53,52], as a
function of precipitate volume fraction. This ratio can
be obtained from analytical models or numerical simu-
lations.Inourphase-fieldsimulationswheremisfitstress
is not considered, this ratio can be derived, thatK
SIM
shoulddividebythetheoreticalvalueof KLSW byMorral
andPurdy[ 54],
KLSW = 2gσVm
[/Delta1Cγ−γ′
]T[Mγ]−1[/Delta1Cγ−γ′
]
(5)
Here, the difference of composition between γ/γ′
[/Delta1Cγ−γ′
] and the Onsager diffusion coefficient matrix
[Mγ] can be retrieved from thermodynamic databases.
The constantg is a geometric factor, andσ is the inter-
facial energy. When misfit stress is not considered, the
ratio f is plotted in Figure3(c), noted asf
0.B yd e c o u -
pling lattice misfit effect from that of alloy composition,
w ec a no b ta i nth er a ti oa tea c hs pec i fi cδ
γ/γ ′,d e n o t eda s

## Page 6

MATER. RES. LETT. 117
Figure 2. Theevolutionof(a)interfaceenergydensityand(b)elasticenergydensityofNi-17.0Al-6.0Moat.%alloyat1200°C,thebegin-
ningofsteady-statecoarseningstageismarkedwithdashline;(c)TheratioofthesimulatedcoarseningratetotheLSWtheorycoarsening
rateasafunctionof γ′volumefraction,thedottedcurvesrepresenttheﬁttingcurvesofallthesimulationresultsbyusingspeciﬁclattice
misﬁts;(d)Calculatedeﬀectiveinterfacialenergyasafunctionof γ′volumefraction,withspeciﬁclatticemisﬁt.
fδ. As the coarsening rates of alloys with different com-
positions but fixedδγ/γ ′ =− 0.3% plotted in Figure1,
i ti se v i d e n tt h a tt h es y n e r g i s t i ce ff e c to fA la n dM oo n
the coarsening is weakened but not disappeared. This
indicatesthatthereareadditionalfactorsinfluencingthe
coarsening rate beyond the changes inδ
γ/γ ′. According
to analytic models [55], KSIM can be decomposed into
threecomponents,
KSIM = f0 ·2gσ · β (6)
where β representsthediffusion-dependentcomponent,
while the term 2gσ is diffusion-independent. Since the
effect of elastic strain energy is opposite to that of inter-
facial energy σ, and the value of functionf
δ is always
smaller thanf0 value, we can merge the effect of inter-
facial energy density and elastic energy density as an
effective interfacial energyσeff =
(fδ
f0
)
· σ. Accordingly,
theterm σ inEquation(6)canbereplacedby σeff,
KSIM = f0 ·2gσeff · β (7)
As shown in Figure2(d), σeff decrease to lower values
than the input interfacial energy (0.05 J/m2)a st h ev o l -
ume fraction of γ′increases and the δγ/γ ′ gets more
negative.
As for the diffusion-dependent component, combin-
ing Equation (5) and Equation (6), we get the following
form,
β = Vm
[/Delta1Cγ−γ′
]T[Mγ]−1[/Delta1Cγ−γ′
]
(8)
With the molar volumeVm fixed in our simulations, the
compositional difference betweenmatrix and precipitate
[/Delta1C
γ−γ′
]w i l lv a r yu n i f o r m l y ,w h e ns o m ep r e c i p i t a t e s
shrink,andtheothersgrowunderthecontrolofinterfa-
cial energy. For the Onsager diffusion coefficient matrix
[M
γ]alsovariedwithmicrostructureevolution,themul-
ticomponent diffusion in Ni-Al-Mo is observed to fur-
ther reduce the diffusion coefficient of Mo as shown in
Figure 3. Evaluating the diffusion kinetics by diffusion
potentialvariation,zoneswithlowerModiffusionpoten-
tial (also lower Onsager diffusion coefficientM
MoMo)
around shrinking γ’ particles are observed due to the

## Page 7

118 M. LI ET AL.
Figure 3. The variations in diﬀusion potential anddiﬀusion coeﬃcient of Mo during the shrinkage of aγ′particle in Ni-17.0Al-6.0Mo
(at.%)alloy.DiﬀusioncoeﬃcientofMobecomeslowerinthe‘LowMoPotentialZones’.
rapid diffusion of Al but the slow diffusion of Mo. These
‘LowMoPotentialZones’alsoresultinafurtherreduced
diffusion flux of Mo controlled by decreasing magnitude
of −M
AlMo,sincethediffusionpotentialgradientofAlis
oppositetothatofMo.
When calculatingβ, it is generally assumed that the
element with slower diffusion will dominate. Therefore,
thediffusion-dependentcomponentcanbesimplifiedas
follows[55]:
β ≈ V
mMγ
Slow
(/Delta1Cγ−γ′
Slow )
2 (9)
In the diffusion matrix [Mγ] of the Ni-Al-Mo system,
Mγ
MoMo is observed to be an order of magnitude smaller
than Mγ
AlAl.W h i c hm a k e s/Delta1Cγ−γ′
Mo become the primary
determinant of the coarsening rate/Delta1Cγ−γ′
Slow . The distri-
bution of Mo betweenγ/γ′is calculated and plotted in
Figure4(a,b), /Delta1Cγ−γ′
Mo increasesbothwiththeincreaseof
MoandtheincreaseofAl.Thecorrespondingdiffusion-
dependent component β is represented byK
LSW and
plotted in Figure4(c). The diffusion-dependent compo-
nentdecreasessignificantlywiththeadditionofMo.The-
oretically,asinFigure 4(d),anincreaseintheAlcontent
alsoleadstoareductioninthediffusion-dependentcom-
ponent, which will become more pronounced at higher
Moconcentrations.Replacingthe β inEquation(7)with
Equation(9), K
SIM canbeestimatedasfollows,
KSIM ≈ f0 ·2gσeff · VmMγ
Slow
(/Delta1Cγ−γ′
Slow )
2 (10)
Equation (7) successfully decouples the controlling
factors of coarsening rate, and Equation (10) provides
an estimate under the control of slow-diffusing element.
With the addition of Al in high-Mo alloys, the increases
off
0 inEquation(10)canbefullyoffsetbythedecreases
ofσeff andMγ
Slow,aswellastheincreaseof /Delta1Cγ−γ′
Slow .These
revealtheinteractioneffectsof γ-strengtheningelement
Mo and γ’-former element Al well. Moreover, further
analysisontheinterfacialenergyandelasticstrainenergy
willhelptostudythekineticsofothercomplexevolution
of γ/γ’microstructures,suchascoalescingandrafting.
Conclusions
A ternary Ni-Al-Mo phase-field model is established to
investigate the coarsening behaviour of SX superalloys

## Page 8

MATER. RES. LETT. 119
Figure 4. CompositionaldiﬀerencesofMobetween γ/γ′variedwiththecontentsofMoandAlduringthe γ′coarseningofNi-Al-Mo
alloysat1200°C:(a)takethemolefractionofMoasmainvariable;(b)takethemolefractionofAlasmainvariable;(c)TheLSWtheory
coarseningrateofallsimulatedalloys;(d)TheregulatedLSWtheoreticalcoarseningratestothoseofNi-16Al-xMo(x = 4∼7at.%)varied
withthemolefractionofAl.
withhighercontentsofAlandMoat1200°C.Thesyner-
gisticeffectsofAlandMoonthesteady-statecoarsening
rate K
SIM are revealed via the controlling roles of dif-
fusion potential, diffusion coefficient and composition
field. On one hand, the diffusion-independent compo-
nentsof K
LSW isdecr easedb yincr easingAlco n ten t,d ue
to the lower effective interfacial energyσeff with high
volumefractionof γ′andwithmorenegativelatticemis-
fit. While on the other hand, a localized reduction in
theOnsagerdiffusioncoefficient M
γ
MoMo andanincrease
in the compositional difference/Delta1Cγ−γ′
Mo are obtained by
the synergistic effects of Mo and Al on the diffusion-
dependent component ofK
LSW. The faster diffusion of
Al than that of Mo makes/Delta1Cγ−γ′
Mo become the primary
determinant of the coarsening rate, and the Al effects on
/Delta1Cγ−γ′
Mo i sf u r t h e rs t r e n g t h e n e db yi n c r e a s i n gM oc o n -
tent. These findings suggest that higher Al content may
not only enhances the mechanical properties of high-
Mo superalloys but also stabilize their microstructures
at ultra-high temperature, by achieving highγ
′volume
fractionandlowcoarseningrateatthesametime.
Disclosure statement
Nopotentialconflictofinterestwasreportedbytheauthor(s).
Funding
This work was financially supported by the National Natu-
ral Science Foundation of Chinas (nos. 92060302), Science
Centerfor GasTurbineProject (No. P2022-B-IV-005-001,No.
P2022-A-I-002–002),KeyResearchandDevelopmentProgram
of Zhejiang Province (No. 2024SSYS0085, No. 2024SSYS0076)
andBeijingNovaProgramNo.20230484318.
References
[1] ReedRC.Thesuperalloysfundamentalsandapplications.
New York: Cambridge University Press;2006.
[2] PollockTM,TinS.Nickel-basedsuperalloysforadvanced
turbine engines: chemistry, microstructure and proper-
ties. J Propuls Power. 2006;22:361–374. doi:10.2514/1.
18239
[ 3 ]N a z m yM ,E p i s h i nA ,L i n kT ,e ta l .Ar e v i e wo fd e g r a -
dation in single crystal nickel based superalloys. Energy
Mater. 2013;1:263–268. doi:10.1179/174892406X17
1271

## Page 9

120 M. LI ET AL.
[4] Murakumo T, Kobayashi T, Koizumi Y, et al. Creep
behaviour of Ni-base single-crystal superalloys with var-
ious γ′volume fraction. Acta Mater.2004;52:3737–3744.
doi:10.1016/j.actamat.2004.04.028
[ 5 ]R uY ,Z h a n gH ,P e iY ,e ta l .N e wt y p eo fγ′phase in Ni
basedsinglecrystalsuperalloys:Itsformationmechanism
and strengthening effect. Mater Des.2018;145:181–195.
doi:10.1016/j.matdes.2018.02.053
[6] Ru Y, Zhang H, Pei Y, et al. Improved 1200°C stress
rupture property of single crystal superalloys by γ
′-
forming elements addition. Scr Mater.2018;147:21–26.
doi:10.1016/j.scriptamat.2017.12.023
[7] Luo L, Ru Y, Ma Y, et al. Design for 1200°C creep prop-
erties of Ni-based single crystal superalloys: effect ofγ′-
formingelementsanditsmicroscopicmechanism.Mater
Sci Eng A.2022;832:142494. doi:10.1016/j.msea.2021.14
2494
[8] Huang J, Ru Y, Zhang H, et al. Subgrains of γ′
phase in a single-crystal superalloy induced by ultra-
high temperature creep. Scr Mater. 2023;235:115616.
doi:10.1016/j.scriptamat.2023.115616
[ 9 ]L u oL ,R uY ,Q i nL ,e ta l .E ff e c t so fa l l o y e da l u m i n u m
andtantalumonthetopologicalinversionbehaviorofNi-
basedsinglecrystal superalloys athightemperature.Adv
EngMater. 2019;21(2):1800793.
[10] Ru Y, Hu B, Zhao W, et al. Topologically inverse
microstructure in single-crystal superalloys: microstruc-
tural stability and properties at ultrahigh temperature.
Mater Res Lett.2021;9:497–506. doi:10.1080/21663831.
2021.1982785
[11] Baldan A. Review progress in Ostwald ripening theories
andtheirapplicationstothe γ
′-precipitatesinnickel-base
superalloys part II nickel-base superalloys. J Mater Sci.
2002;37:2379–2405.doi:10.1023/A:1015408116016
[12] Ardell A. Precipitate coarsening in solids: modern theo-
ries,chronicdisagreementwithexperiment.PhaseTrans-
form.1988;87:485–494.
[ 1 3 ]C h e nY ,P r a s a t hb a b uR ,S l a t e rT J A ,e ta l .A ni n v e s t i g a -
tion of diffusion-mediated cyclic coarsening and rever-
sal coarsening in an advanced Ni-based superalloy. Acta
Mater. 2016;110:295–305. doi: 10.1016/j.actamat.2016.
02.067
[ 1 4 ]Z r n í kJ ,S t r u n zP ,V r c h o v i n s k yV ,e ta l .C r e e pd e f o r m a -
tion and microstructural examination of a prior ther-
mally exposed nickel base superalloy. Key Eng Mater.
2004;274–276:925–930.
[ 1 5 ]Z r n i kJ ,S t r u n zP ,V r c h o v i n s k yV ,e ta l .D e g r a d a t i o no f
creeppropertiesinalong-termthermallyexposednickel
base superalloy. Mater Sci Eng A. 2004;387–389:728–
733.
[16] Ma J, Lu J, Tang L, et al. A novel instrument for inves-
tigating the dynamic microstructure evolution of high
temperature service materials up to 1150 °C in scanning
electron microscope. Rev Sci Instrum.2020;91:043704.
doi:10.1063/1.5142807
[17] Moelans N, Blanpain B, Wollants P. An introduction
to phase-field modeling of microstructure evolution.
Calphad. 2008;32:268–294. doi:10.1016/j.calphad.2007.
11.003
[18] Steinbach I. Phase-field models in materials science.
Model Simul Mater Sci Eng.2009;17:073001.doi:10.1088
/0965-0393/17/7/073001
[19] Garnier T, Finel A, Le Bouar Y, et al. Simulation of alloy
thermodynamics: from an atomic to a mesoscale Hamil-
tonian.PhysRevB. 2012;86:054103.
[20] Xingjun L, Yuechao C, Yong L, et al. Present research
situation and prospect of multi-scale design in novelCo-
basedsuperalloys:areview.ActaMetallSin. 2020;56:1–20.
[21] Wang Y, Banerjee D, Su CC, et al. Field kinetic model
and computer simulation of precipitation of L12 ordered
intermetallics from f.c.c. solid solution. Acta Mater.
1998;46:2983–3001.doi:10.1016/S1359-6454(98)00015-9
[22] Li DY, Chen LQ. Computer simulation of morpho-
logical evolution and rafting of γ
′ particles in Ni-
based superalloys under applied stresses. Scr Mater.
1997;37:1271–1277.doi:10.1016/S1359-6462(97)00276-5
[ 2 3 ]V a i t h y a n a t h a nV ,C h e nL .C o a r s e n i n go fo r d e r e di n t e r -
metallic precipitates with coherency stress. Acta Mater.
2002;50:4061–4073.doi:10.1016/S1359-6454(02)00204-5
[ 2 4 ]Z h uJ ,W a n gT ,A r d e l lA ,e ta l .T h r e e - d i m e n s i o n a l
phase-field simulations of coarsening kinetics of gamma
‘particles in binary Ni-Al alloys. Acta Mater.2004;52:
2837–2845.doi:10.1016/j.actamat.2004.02.032
[25] Wang T, Sheng G, Liu Z-K, et al. Coarsening kinetics of
gamma‘precipitatesintheNi-Al-Mosystem.ActaMater.
2008;56:5544–5551.doi:10.1016/j.actamat.2008.07.024
[26] Rajendran MK, Shchyglo O, Steinbach I. Large scale 3-D
phase-field simulation of coarsening in Ni-base superal-
loys.MATECWebofConferences. 2014;14:11001.
[ 2 7 ]T s u k a d aY ,K o y a m aT ,K u b o t aF ,e ta l .P h a s e - fi e l d
simulation of rafting kinetics in a nickel-based sin-
gle crystal superalloy. Intermetallics. 2017;85:187–196.
doi:10.1016/j.intermet.2017.02.017
[28] Wang C, Ali MA, Gao S, et al. Combined phase-field
crystal plasticity simulation of P- and N-type rafting
in Co-based superalloys. Acta Mater. 2019;175:21–34.
doi:10.1016/j.actamat.2019.05.063
[29] WangD,LiY,ShiS,etal.Elementmigrationduringstress
rafting of gamma ‘-Co-3(Al, W) precipitates. Philos Mag
Lett. 2020;100:202–212. doi:10.1080/09500839.2020.17
41043
[ 3 0 ]T s u k a d aY ,M u r a t aY ,K o y a m aT ,e ta l .C r e e pd e f o r m a -
tion and rafting in nickel-based superalloys simulated by
thephase-fieldmethodusingclassicalflowandcreepthe-
ories. Acta Mater.2011;59:6378–6386. doi:10.1016/j.acta
mat.2011.06.050
[31] Yang M, Zhang J, Wei H, et al. A phase-field model for
creep behavior in nickel-base single-crystal superalloy:
coupled with creep damage. Scr Mater.2018;147:16–20.
doi:10.1016/j.scriptamat.2017.12.008
[32] Yang M, Zhang J, Gui W, et al. Coupling phase field with
creepdamagetostudygamma‘evolutionandcreepdefor-
mation of single crystal superalloys. J Mater Sci Technol.
2021;71:129–137.doi:10.1016/j.jmst.2020.07.036
[33] Cottura M, Appolaire B, Finel A, et al. Microstructure
evolution under [110] creep in Ni-base superalloys. Acta
Mater.2021;212:116851.
[34] Goerler JV, Lopez-Galilea I, Roncery LM, et al. Topolog-
i c a lp h a s ei n v e r s i o na f t e rl o n g - t e r mt h e r m a le x p o s u r eo f
nickel-base superalloys: experiment and phase-field sim-
ulation. Acta Mater.2017;124:151–158. doi:10.1016/j.act
amat.2016.10.059
[35] Ali MA, Amin W, Shchyglo O, et al. 45-degree raft-
ing in Ni-based superalloys: A combined phase-field

## Page 10

MATER. RES. LETT. 121
and strain gradient crystal plasticity study. Int J Plast.
2020;128:102659.
[36] ZhouX,LiY,WuX,etal.Initialprecipitationandcoarsen-
ingofthephaseininverseNi-Alalloys.MaterHighT emp.
2017;34:208–214.doi:10.1080/09603409.2016.1277448
[37] BhaskarMS.Quantitativephasefieldmodellingofprecip-
itate coarsening in Ni-Al-Mo alloys. Comput Mater Sci.
2018;146:102–111.doi:10.1016/j.commatsci.2018.01.021
[38] Wang Z, Liang C, Wang D, et al. Composition and tem-
perature dependence of kinetic behavior ofγ
′precipi-
tation in Ni–Al–Cr–Mo quaternary model superalloys:
Ap h a s efi e l ds t u d y .JA l l o y sC o m p d .2024;976:172982.
doi:10.1016/j.jallcom.2023.172982
[39] Wang H, Li Y, Zhang X, et al. Composition distribu-
tion and kinetics evolution of gamma ‘phase in Ni-(17
invertedexclamationx)Al-xMo(at.%)alloys.JMaterRes
Technol-JMRT. 2021;15:561–571. doi:10.1016/j.jmrt.20
21.08.053
[40] Kim SG. Large-scale three-dimensional simulation of
Ostwald ripening. Acta Mater. 2007;55:6513–6525.
doi:10.1016/j.actamat.2007.07.058
[41] ChatterjeeS,Moelans N. Agrand-potential based phase-
field approach for simulating growth of intermetallic
phases in multicomponent alloy systems. Acta Mater.
2021;206:116630.
[42] Plapp M. Unified derivation of phase-field models for
alloy solidification from a grand-potential functional.
PhysRevE. 2011;84:031601.
[43] Choudhury A, Kellner M, Nestler B. A method for cou-
pling the phase-field model based on a grand-potential
formalismtothermodynamicdatabases.CurrOpinSolid
State Mater Sci.2015;19:287–300. doi:10.1016/j.cossms.
2015.03.003
[44] Andersson J-O, Helander T, Höglund L, et al. Thermo-
Calc & DICTRA, computational tools for materials sci-
ence. Calphad. 2002;26:273–312. doi:10.1016/S0364-59
16(02)00037-8
[45] T egelerM,ShchygloO,KamachaliRD,etal.Parallelmul-
tiphase field simulations with OpenPhase. Comput Phys
Commun. 2017;215:173–187. doi: 10.1016/j.cpc.2017.
01.023
[46] Kundin J, Mushongera L, Goehler T, et al. Phase-
field modeling of the gamma ‘-coarsening behavior in
Ni-based superalloys. Acta Mater. 2012;60:3758–3772.
doi:10.1016/j.actamat.2012.03.023
[47] Fahrmann M, Hermann W, Fahrmann E, et al. Deter-
mination of matrix and precipitate elastic constants in
(γ–γ
′) Ni-base model alloys, and their relevance to raft-
ing. Mater Sci Eng A.1999;260:212–221. doi:10.1016/S0
921-5093(98)00953-8
[ 4 8 ]C o n l e yJ G ,F i n eM E ,W e e r t m a nJ R .E ff e c to fl a t t i c ed i s -
registry variation on the late stage phase transformation
behavior of precipitates in Ni-Al-Mo alloys. Acta Metall.
1989;37:1251–1263.doi:10.1016/0001-6160(89)90119-3
[ 4 9 ]L i uC ,L iY ,Z h uL ,e ta l .E ff e c to fc o h e r e n tl a t t i c e
mismatch on the morphology and kinetics of ordered
precipitates. J Mater Eng Perform.2018;27:4968–4977.
doi:10.1007/s11665-018-3572-7
[ 5 0 ]P f a uB ,S t a d l e rL - M ,S e p i o lB ,e ta l .C o a r s e n i n gd y n a m -
ics in elastically anisotropic alloys. Phys Rev B.2006;73:
180101.doi:10.1103/PhysRevB.73.180101
[51] WangC,HuangJ,KongH,etal.Theeffectoftemperature
and misfit on γ
′precipitation in Co-Ti alloys: phase-
fieldmodelingandexperiments.JPhaseEquilibriaDiffus.
2020;41:15–26.doi:10.1007/s11669-019-00775-3
[52] Baldan A. Review progress in Ostwald ripening the-
ories and their applications to nickel-base superal-
loys part I: Ostwald ripening theories. J Mater Sci.
2002;37:2171–2202.doi:10.1023/A:1015388912729
[53] Streitenberger P. Analytical description of phase coars-
ening at high volume fractions. Acta Mater. 2013;61:
5026–5035.doi:10.1016/j.actamat.2013.04.042
[ 5 4 ]M o r r a lJ E ,P u r d yG R .P a r t i c l ec o a r s e n i n gi nb i n a r y
and multicomponent alloys. Scr Metall Mater.1994;30:
905–908.doi:10.1016/0956-716X(94)90413-8
[55] Wang KG, Wang GQ. Phase coarsening in multicompo-
nent systems. Phys Rev E.2017;95:022609. doi:10.1103/
PhysRevE.95.022609
