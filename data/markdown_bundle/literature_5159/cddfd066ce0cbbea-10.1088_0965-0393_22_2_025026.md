# 10.1088_0965-0393_22_2_025026

<!-- source: D:\总文献\10.1088_0965-0393_22_2_025026.pdf -->
<!-- file_sha256: cfe881ef72a1289a9b3e082d30d550c975e93e873d0546044c078be3ce2f5791 -->

## Page 1

This content has been downloaded from IOPscience. Please scroll down to see the full text.
Download details:
IP Address: 131.95.109.31
This content was downloaded on 08/11/2014 at 17:28
Please note that terms and conditions apply.
Tertiary dendritic instability in late stage solidification of Ni-based superalloys
View the table of contents for this issue, or go to the journal homepage for more
2014 Modelling Simul. Mater. Sci. Eng. 22 025026
(http://iopscience.iop.org/0965-0393/22/2/025026)
Home Search Collections Journals About Contact us My IOPscience

## Page 2

Modelling and Simulation in Materials Science and Engineering
Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 (9pp) doi:10.1088/0965-0393/22/2/025026
Tertiary dendritic instability in late stage
solidiﬁcation of Ni-based superalloys
M M Franke 1, R F Singer 1 and I Steinbach 2
1 Institute of Science and Technology of Metals, Department of Materials Science and
Engineering, University of Erlangen, Martensstr. 5, D-91058 Erlangen, Germany
2 Chair of Scale Bridging Thermodynamic and Kinetic Simulation, University of
Bochum, Stiepelerstr. 129, D-44801 Bochum, Germany
E-mail: martin.franke@ww.uni-erlangen.de
Received 4 October 2013, revised 15 January 2014
Accepted for publication 20 January 2014
Published 13 February 2014
Abstract
Derivatives of the commercial alloy CMSX-4 were directionally solidiﬁed and
characterized with respect to their ﬁnal dendrite microstructure. The results
indicate that Ni-based superalloys with high segregation levels show signiﬁcant
instability in secondary dendrite arms and an increased tendency for tertiary
arm formation, respectively. Phase-ﬁeld simulations were used to explore
the impact of chemical composition on morphological instability and tertiary
arm formation during the directional solidiﬁcation of Ni-based superalloys.
It is found that an increase in speciﬁc alloying elements in the overall alloy
composition leads to pronounced segregation at the end of solidiﬁcation. This
causes strong growth restriction of the secondary arms and triggers tertiary arm
formation. The proposed mechanism explains experimental microstructures
found in modiﬁcations of the base alloy CMSX-4.
Keywords: Ni-based superalloys, dendritic solidiﬁcation, morphological
instability, phase-ﬁeld simulation
Nomenclature
c composition (c0: initial composition, cL: liquidus composition,
cS: solidus composition)
D diffusion coefﬁcient
f( t) function of time f( t) = (1 − t ˙T/T 0)
fl fraction of liquid
i element index
k static anisotropy coefﬁcient
m liquidus slope
T temperature (T0: initial temperature, which is related to the liquidus temperature)
0965-0393/14/025026+09$33.00 © 2014 IOP Publishing Ltd Printed in the UK 1

## Page 3

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
˙T cooling rate
t time
v withdrawal speed
/Gamma1Gibbs Thomson coefﬁcient
/Delta1c concentration gradient at the interface
/Delta1Tint solidiﬁcation range at the interface
θ angle (relative orientation of the interface normal to the anisotropic grain)
λint wavelength of interface instabilities
λ1 primary dendrite arm spacing
λ2 secondary dendrite arm spacing
σ interfacial energy (σ0: initial interfacial energy)
R tip radius of the growing protrusion
1. Introduction
High-performance turbine blades and vanes from Ni-based superalloys are mainly fabricated by
investment casting. For the most demanding applications directional solidiﬁcation is employed
to produce columnar or single-crystal dendritic structures. The dendritic structure is generally
characterized by the dendrite arm spacing and displays strong microsegregation between the
dendrite core and the interdendritic regions, usually called the ‘interdendritic eutectic’. A
study by Giamei and Tschinkel ( 1976) showed that a reduction of the dendrite arm spacing is
very much desired as it leads to less microsegregation and greater homogeneity. The amount
of microporosity typically found in vacuum castings is again directly related to the primary
dendrite arm spacing and the formation of secondary and tertiary branches (Lecomte-Beckers
1988). Lamm and Singer ( 2007) explained the lower microporosity content, which is linked
to sufﬁcient feeding, with smaller dendrite arm spacings and smooth dendrite morphologies.
Moreover, the formation of freckles, which appear as elongated chains of dendrite fragments,
is attributed to the dendrite morphology and the ﬂow of interdendritic liquid (Beckermann
et al 2000 ). However, the lower tendency to form freckles might be enhanced by an increased
frictional force due to morphological instabilities and tertiary arm formation, respectively.
In general, the formation of a dendrite is related to constitutional undercooling and starts
with the breakdown of an unstable planar solid/liquid interface. The resultant interface
perturbations (interface instabilities) are characterized by the wavelength λ
int (1), which is
of great importance in the theory of dendritic growth (Kurz and Fisher 1989):
λint = 2π
( D/Gamma1
vm/Delta1c
)1/2
, (1)
where D is the diffusion coefﬁcient of the solute in the liquid; /Gamma1is Gibbs Thomson coefﬁcient;
v is the withdrawal speed 3; /Delta1cis the concentration gradient at the interface and m is the
liquidus slope. Tips (positive protrusions with radius R) will tend to grow more rapidly than
depressions as they can also reject solute in the lateral directions. Favourably oriented tips
will form into primary trunks as well as secondary and tertiary branches. Once the primary
spacing is established, it remains constant during, or after, steady-state solidiﬁcation (Kurz and
Fisher 1989). The primary dendrite arm spacing λ
1 is predominantly affected by the cooling
rate, which is related to the temperature of the heating furnace, the design of the bafﬂe and the
withdrawal speed (Franke et al 2010; 2013). Secondary dendrites grow almost perpendicularly
3 The velocity of the solidiﬁcation front can be associated with the withdrawal speed in the case of directional
solidiﬁcation.
2

## Page 4

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
Table 1. Nominal (initial) composition c0 of alloys as used in the experiments (weight
per cent).
Alloy Al Co Cr Mo Ta Ti W Hf Re Ni
Alloy1 6 9 6.5 0.6 3 2 6 — — bal.
Alloy2 4,75 9 6.5 0.6 7 2 6 — — bal.
Alloy3 6 9 6.5 0.6 3 1 6 0.5 — bal.
Alloy4 4,65 9 6.5 0,6 7 1 6 0.5 — bal.
Alloy5 5,6 9 6.5 0.6 3,2 0.7 6 1.4 — bal.
CMSX-4 5,6 9 6.5 0.6 6,5 1 6 0.1 3 bal.
to the primary trunks for ⟨100 ⟩dendrites in fcc Ni-based alloys and eliminate each other as
long as their length is less thanλ1/2. Their ﬁnal distribution is commonly governed by ripening
reactions, which cause more widely spaced secondary branches (Kurz and Fisher 1989). In the
case of directional or equiaxed growth, the secondary dendrite arm spacing λ2 is essentially
related to the cooling rate (Feurer and Wunderlin 1977, Kurz and Fisher 1989). Tertiary arm
formation is commonly related to the branching mechanism in steady-state growth experiments
where they are observed to grow from secondary branches in the direction of the temperature
gradient to form new primary trunks (Somboonsuk and Trivedi1985,S a et al 2004). In contrast
to these tertiary arms, the new ﬁnding of this work reveals that tertiary arms grow in the plane
perpendicular to the temperature gradient. Thus, a full set of permutations of growth directions
in fcc crystals is realized. The tertiary instability is not subject to a stabilizing temperature
gradient. This must be investigated more closely in subsequent investigations.
The recent experimental ﬁndings of the authors of this paper indicate that directionally
solidiﬁed Ni-based superalloys may show a signiﬁcant instability for secondary dendrite
arms during the later stage of solidiﬁcation where ripening is expected to control mainly
the microstructure evolution (Franke 2013). The aim of this work was to explore the impact of
chemical composition on morphological instability and tertiary arm formation in the later
stage of dendritic solidiﬁcation of Ni-based superalloys. Solidiﬁcation experiments with
different compositional modiﬁcations of the commercial alloy CMSX-4 were performed and
the specimens were subsequently characterized with respect to their ﬁnal microstructure. The
cause of the instability was investigated using a phase-ﬁeld simulation (for a recent review see
Steinbach ( 2013)) and was related to the growth restriction dependent on the concentration
gradient at the interface.
2. Experiments
2.1. Setup
The compositions of the investigated alloys represent derivatives of the commercial Ni-based
superalloy CMSX-4 with changes in the Al, Ta, Ti and Hf content, as well as the complete
removal of Re (table 1). The ﬁnal compositions were adjusted in our laboratory by adding
the desired elements to a master heat, which was provided by the chair of Metallurgische
Prozesstechnik und Metallrecycling (Aachen, Germany). CMSX-4 was provided by a
commercial vendor, Doncasters Precision Castings GmbH (Bochum, Germany).
A Bridgman vacuum investment casting unit was used to directionally solidify the alloys
as cylindrical bars. The melt was homogenized for 5 min at 1560
◦C before casting into the
1500 ◦C preheated mould (ﬁgure 1). The casting mould was assembled from dense rubalit
alumina tubes, mounted on a Ni-plate on top of a water-cooled copper chill plate. All castings
3

## Page 5

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
Figure 1. Drawing of the mould used in this study. The casting mould was assembled
from a gating system (1) and dense rubalit alumina tubes (2), which are mounted on a
Ni-plate (3).
were performed at a withdrawal rate of 3 mm min−1. The working pressure of the casting unit
was set to 10−3 mbar.
The as-cast microstructure of directionally solidiﬁed Ni-based superalloys was investi-
gated in terms of primary dendrite arm spacing and the morphological instability of secondary
branches. The castings were investigated using micrographs on cut samples from the middle
of castings at 70–90 mm distance from the chill plate. The primary dendrite arm spacing was
determined by counting all of the primary arms within a large area. From the number of
primary arms within this area, an average spacing was calculated (Jacobi and Schwerdtfeger
1976). Furthermore, the morphological instability of the secondary branches was obtained
through qualitative analysis.
2.2. Results
The experimentally derived primary dendrite arm spacing is listed in table 2 for each alloy.
Figure 2 exempliﬁes the as-cast microstructure of the investigated alloys. It can clearly be seen
that Ni-based superalloys differ from each other in terms of morphological instability, although
the casting conditions and primary dendrite arm spacings (242±11 µm) are almost constant. In
particular, no tertiary arm formation is observed for alloy1 (ﬁgure 2(a)), while alloy3 displays
some tertiary branching (ﬁgure 2(b)). Alloy5 is characterized by very signiﬁcant tertiary arm
formation (ﬁgure 2(c)), i.e. pronounced instabilities of secondary dendrite arms with respect
to alloy1, where the secondary arms show an almost convex contour.
3. Simulation of microstructure formation
3.1. Modelling
The multiphase multicomponent phase-ﬁeld code MICRESS was used to simulate the
microstructure formation of dendrites perpendicular to the growth direction of primary trunks
4

## Page 6

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
Figure 2. As-cast microstructure of directionally solidiﬁed castings. The morphology
of representative dendrites is marked by a solid line. ( a) Alloy1, (b) alloy3, (c) alloy5.
No tertiary arm formation is observed for alloy1, while alloy5 shows a strong tendency
for tertiary arm formation. The primary trunk spacing is the same.
Table 2. Mean primary dendrite arm spacing.
Alloy Alloy1 Alloy2 Alloy3 Alloy4 Alloy5 CMSX-4
Mean primary dendrite arm 233 250 253 244 246 232
spacing λ1 (µm)
in a unit cell (ﬁgure 3) corresponding to the cross-section associated with one single dendritic
trunk (Warnkenet al 2009). MICRESS provides coupling of a multicomponent diffusion solver
and a phase-ﬁeld solver in order to account for solute transport (the Scheil–Gulliver model). A
coupling to a thermodynamic calculation via the TQ interface of Thermo-Calc is implemented
in MICRESS in order to calculate the driving force of phase transformation and the partitioning
of alloying elements. Furthermore, linearized phase diagrams are applied in order to simplify
the mathematical treatment of the solidiﬁcation process (Eiken et al 2006, Steinbach 2009).
Important settings and the boundary conditions used in this study are listed in table 3.
In general, the isothermal cross-section of a dendrite is initiated at the very ﬁrst stage of
solidiﬁcation by the use of a four-fold shape function (table 3). During further solidiﬁcation,
the morphology of dendrites is ruled by diffusion and element distribution (diffusion-limited
growth). The phase-ﬁeld modelling of eutectic reactions at the last stage of solidiﬁcation is
based on several simpliﬁcations concerning nucleation and growth. Nucleation is described
by a seed undercooling model, which is based on a predeﬁned critical nucleation undercooling
and the given nucleant positions at the interface dendrite/liquid. Further on, the ﬁne two-phase
region (γ/γ
′′-mixture) that cannot be resolved in a phase-ﬁeld simulation is replaced by a
diffuse phase mixture. For these reasons, no perfect match for simulations and experiments
concerning the structure and the amount of the interdendritic eutectic can be expected.
3.2. Results
The morphology of the dendritic phase within the isothermal unit cell is illustrated in ﬁgure 4
and corresponds to a thermal gradient of 5000 K m −1, a withdrawal speed of 3 mm min−1 and
5

## Page 7

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
Figure 3. Schematic cross-section of one single dendritic trunk (four-fold shape)
perpendicular to the [0 0 1] direction. The unit cell used for the simulation of
microstructure evolution is labelled by the solid line. It was applied to limit the
computational effort.
Table 3. Settings and boundary conditions for the isothermal unit cell model.
Parameter Software/ Database/V alue
V ersion MICRESS 6.001
Thermo-Calc Classic V ersion S (2532)
DICTRA V ersion 25
Interface TQ 7
Thermodynamic database TTNi7
Kinetic database: MobNi1
Grid 150 in the x-direction;
1i nt h ey-direction;
150 in the z-direction
Resolution 0.8 µm
Temperature Initial temperature: T
0
Boundary condition: T( t) = T0f( t)
Concentration Initial concentration: c0
Boundary conditions: symmetry
Interface thickness 3.5 cells
Primary dendrite arm spacing 240 µm
Cooling rate, thermal gradient, withdrawal speed 0,25 K s
−1; 5000 K m−1; 3 mm min−1
Phases LIQUID; fcc A1; GAMMA PRIME
Interfacial energy LIQUID /fcc A1: σ0 = 50 mJ m−2
Crystal symmetry Cubic
Anisotropy of interfacial energy σ = σ0(1 − k cos(4θ))
(Four-fold shape function) with k = 0.2
a remaining liquid fraction of 0.15. The results indicate differences in dendritic morphology
and are in good qualitative agreement with the experimental ﬁndings (ﬁgure 2). Tertiary arm
formation is not observed for alloy1 (ﬁgure 4(a)). Alloy3 displays weak branching and alloy5
is characterized by signiﬁcant tertiary arms.
6

## Page 8

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
Figure 4. Calculated morphology of a secondary dendrite within the unit cell (fraction
liquid = 0.15). (a) Alloy1, (b) alloy3, (c) alloy5.
Figure 5. Calculated solidiﬁcation range at the interface/Delta1Tintt dependent on the fraction
of liquid fl.
The growth of the dendritic phase is linked to the evolution of microsegregation and the
ensuing partitioning of the alloying elements. For further analysis, information from the phase-
ﬁeld simulation about the element content at the interface in solidc
S,i and liquid statecL,i as well
as the liquidus slopes mi is used to calculate the solidiﬁcation range at the interface 4 /Delta1Tint (2),
which is a measure of constitutional undercooling, the propensity for dendritic growth (Ilschner
and Singer 2010) and the reﬁnement of microstructure (Kurz and Fisher 1989, Johnsson 1994):
/Delta1T
int (t) =
∑
i
⏐⏐mi(t)(cL,i(t) − cS,i(t))
⏐⏐. (2)
Figure 5 illustrates the calculated evolution of the solidiﬁcation range at the interface depending
on the liquid fraction for different alloys. It is clear that /Delta1Tint changes during the solidiﬁcation
process. In general, the progress in solidiﬁcation provides an increase in the amount of
redistribution and in the corresponding solidiﬁcation range /Delta1T
int . The impact of the chemical
composition seems to be less pronounced at the beginning of solidiﬁcation. The investigated
alloys display nearly the same /Delta1T
int for high contents of liquid fraction. In contrast, the
estimated solidiﬁcation ranges at the interface differ signiﬁcantly at the very last stage of
solidiﬁcation (liquid fraction < 0.1).
4 It should be noted that this solidiﬁcation range is only valid in linear extrapolation and does not consider secondary
phase formation. It is used here as a measure of the amount of redistribution at the interface.
7

## Page 9

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
In summary, we can identify a clear order in the tendency for instability in the different
alloys. The lowest tendency shows alloy1. The tendency increases to alloy2 with the increase
of the Ta concentration. The next increase to CMSX-4 can be related to the increase in Hf by
0.1 wt%. A further increase in Hf to 0.5 wt% and again an increase in Ta leads to the increased
segregation in alloy3 and alloy4 (table 1). Clearly, alloy5 has the top segregation and shows a
pronounced tendency to instability (ﬁgure 2).
4. Discussion
The phase-ﬁeld modelling of dendritic solidiﬁcation and segregation is based on
simpliﬁcations. In contrast to the equilibrium solidiﬁcation, which is only valid for full
diffusion in the solid and liquid phases (lever rule), the non-equilibrium solidiﬁcation and the
evolution of/Delta1T
int are based on complete liquid mixing and no solid-state diffusion (the Scheil–
Gulliver model). It is obvious that the Scheil–Gulliver model provides a poor approximation
of the ﬁnal liquid composition, since the maximum liquid concentration is inﬁnite. On the
other hand, equilibrium solidiﬁcation (lever rule) is not qualiﬁed for most solutes because of
their low solid-state diffusion. The real degree of segregation usually lies between Scheil–
Gulliver segregation and equilibrium (Rettig et al 2009). Furthermore, it should be pointed
out that the liquidus slopes used for the calculation of /Delta1T
int are derived from linearized binary
phase diagrams, i.e. neglecting cross effects between the different solutes. For these reasons
no perfect match for simulations and experiments concerning the element distribution and the
corresponding solidiﬁcation range at the interface should be expected. However, the performed
simulations are highly relevant as they demonstrate a correlation between segregation and
morphology.
Ni-based superalloys with compositions that lead to high segregation levels during
solidiﬁcation show signiﬁcant instability in secondary dendrite arms, while the primary
dendrite arm spacing is essentially independent from compositional modiﬁcations. In general,
the primary spacing is established at the beginning of solidiﬁcation and it will not change
during, or after, solidiﬁcation. At this early stage of solidiﬁcation, the segregation level is
quite low and independent from the composition. The investigated alloys display similar
solidiﬁcation ranges at the interface and therefore no great differences in primary trunk
spacing. In contrast, the tertiary arm formation (late stage instabilities of secondary dendrite
arms) occurs mainly at the end of solidiﬁcation. Alloys that are characterized by high
segregation levels display large values of /Delta1T
int and an increased tendency for tertiary arm
formation.
In general, a large solidiﬁcation range corresponds to a large amount of solute to be
redistributed at the growing interface. This leads to the so-called growth restriction, which
has to be overcome by a ﬁne microstructure. The growth restriction provides an explanation
for the observed instability of the structure at the end of solidiﬁcation where the instability
wavelength λ
int (1), or the radius of the growing protrusion R, is to a ﬁrst approximation
inversely proportional to the square root of the concentration gradient/Delta1cand the solidiﬁcation
range /Delta1Tint , respectively.
5. Conclusion
• Ni-based superalloys with high segregation levels show signiﬁcant late stage instability
of secondary dendrite arms. In contrast, the primary dendrite arm spacing displays no
dependence on highly segregating elements.
8

## Page 10

Modelling Simul. Mater. Sci. Eng. 22 (2014) 025026 M M Franke et al
• Highly segregating elements such as Ta and Hf enlarge the concentration gradient /Delta1c
and impede the redistribution process at the growing interface during solidiﬁcation. This
leads to the so-called growth restriction that provides a reﬁned microstructure at the end
of solidiﬁcation and gives an explanation for the observed differences in morphological
instabilities and tertiary arm formation, respectively.
Acknowledgment
The authors gratefully acknowledge the ﬁnancial support of the Deutsche Forschungs
Gemeinschaft (DFG) within the collaborative research centre SFB/Transregio 103.
References
Beckermann C, G u J P and Boettinge r W J 2000 Development of a freckle predictor via Rayleigh number, method
for single-crystal nickel-base superalloy castings Metall. Mater . Trans.A 31 2545–56
Eiken J, Boettger B and Steinbach I 2006 Multiphase-ﬁeld approach for multicomponent alloys with extrapolation
scheme for numerical application Phys. Rev. E 73 066122
Feurer U and Wunderlin R 1977 Einﬂuss der Zusammensetzung und der Erstarrungsbedingungen auf die
Dendritenmorphologie bin ¨arer Al-Legierungen (Oberursel: Deutsche Gesellschaft f ¨ur Metallkunde)
Franke M M 2013 Auswirkungen der Legierungszusammensetzung auf die Morphologie und die Festigkeit des
Dendritennetzwerkes bei der gerichteten Erstarrung von Nickelbasis-Superlegierungen (Erlangen: FAU
University Presss)
Franke M M, Hilbinger R M, Heckl A and Singer R F 2010 Effect of thermo physical properties and processing
conditions on primary dendrite arm spacing of nickel-base superalloys—numerical approach Int. F oundry
Res./Giessereiforschung 62 14–18
Franke M M, Hilbinger R M, Lohm¨uller A and Singer R F 2013 The Effect of liquid metal cooling on thermal gradients
in directional solidiﬁcation of superalloys: thermal analysis J. Mater . Process. Technol.213 2081–8
Giamei A F and Tschinkel J G 1976 Liquid metal cooling: a new solidiﬁcation technique Metall. Trans. A 7 1427–34
Ilschner B and Singe r R F 2010 Werkstoffwissenschaften und Fertigungstechnik (Heidelberg: Springer)
Jacobi H and Schwerdtfeger K 1976 Dendrite morphology of steady state unidirectionally solidiﬁed steel Metall.
Trans. A 7 811–20
Johnsson M 1994 Inﬂuence of Si and Fe on the grain reﬁnement of aluminium Z. Metallk. 85 781–5
KarunaratneMSA ,C o xDC , Carter P and Ree d R C 2000 Conf. Proc. Superalloys (Champion, PA) ed T M Pollock
and R D Kissinger (Warrendale, PA: TMS) pp 263–72
Konter M, Newnham M and Toennes C 1997Nickel-Base SuperalloySwitzerland patent application WO1997CH00229
Kurz W and Fishe r D J 1989 Fundamentals of Solidiﬁcation (Durnten-Zurich: Trans Tech Publications Ltd)
Lamm M and Singer R F 2007 The effect of casting conditions on the high cycle fatigue properties of the single-crystal
nickel-base superalloy PW A1483Metall. Mater . Trans.A 38 1177–83
Lecomte-Beckers J 1988 Conf. Proc. Superalloys (Champion, PA) ed S Reichman an d D N Duhl (Warrendale, PA:
TMS) pp 713–21
Rettig R, Heckl A, Neumeier S, Pyczak F, G ¨oken M and Singe r R F 2009 Defect and Diffusion F orum vol 289–292
pp 101–8 (Durnten-Zurich: Trans Tech Publications)
R¨osler J, Konter M and T ¨onnes C 1996 Conf. Proc. Superalloys (Champion, PA) ed R D Kissinger and D J Deye
(Warrendale, PA: TMS) pp 515–22
S´a F, Rocha O L, Siqueir a C A and Garcia A 2004 The effect of solidiﬁcation variables on tertiary dendrite arm
spacing in unsteady-state directional solidiﬁcation of Sn–Pb and Al–Cu alloys Mater . Sci. Eng.A 373 131–8
Somboonsuk K and Trivedi R 1985 Dynamical studies of dendritic growth Acta Metall. 33 1051–60
Steinbach I 2009 Phase-ﬁeld models in materials science Modelling Simul. Mater . Sci. Eng. 17 073001
Steinbach I 2013 Phase-ﬁeld model for microstructure evolution at the mesoscopic scale Annu. Rev. Mater . Res.
43 89–107
Warnken N, Ma D, Drevermann A, Reed R C, Fries S G and Steinbach I 2009 Phase-ﬁeld modelling of as-cast
microstructure evolution in nickel-based superalloys Acta Mater .57 5862–75
9
