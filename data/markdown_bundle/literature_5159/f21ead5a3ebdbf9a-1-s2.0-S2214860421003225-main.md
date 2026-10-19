# 1-s2.0-S2214860421003225-main

<!-- source: D:\总文献\1-s2.0-S2214860421003225-main.pdf -->
<!-- file_sha256: 8bbf6af7e73082ca62d4a49ca8497373754588dddd9aff58fbcb45b7b24b48ca -->

## Page 1

Additive Manufacturing 46 (2021) 102158
Available online 7 July 2021
2214-8604/© 2021 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/).
Microcrack mitigation during laser scanning of tungsten via preheating and 
alloying strategies 
Bey Vrancken
a , b , *
, Rishi K. Ganeriwala
a
, Aiden A. Martin
a
, Manyalibo J. Matthews
a 
a
Lawrence Livermore National Laboratory, 7000 East Avenue, Livermore, CA 94550, USA 
b
Department of Mechanical Engineering, KU Leuven, Celestijnenlaan 300, 3001 Leuven, Belgium 
ARTICLE INFO 
Keywords: 
Tungsten 
Laser powder bed fusion 
Additive manufacturing 
Microcracking 
Preheating 
Ductile-to-brittle transition 
ABSTRACT 
When tungsten is processed by laser powder bed fusion additive manufacturing, the combination of high residual 
stresses and tungsten ’ s inherent ductile-to-brittle transition leads to a network of microcracks. While preheating 
is widely accepted as the most efficient way to reduce residual stresses in additively manufactured parts, thus far 
it has proven ineffective in completely eliminating microcracking in tungsten. In addition to preheating, 
changing the alloy composition is an increasingly popular approach to circumvent cracking. This work utilizes in 
situ high-speed optical imaging combined with thermomechanical modeling to elucidate the effect of preheating 
and alloying with 2 wt% rare earth oxides on the cracking behavior in powderless single track and hatch strategy 
laser scans. Optical imaging reveals two distinct cracking mechanisms in the fusion zone and the heat affected 
zone, both of which are eliminated by substrate preheating temperatures of 773 – 873 K. Due to the lower melting 
point of the rare earth oxide inclusions, the melt behavior becomes more turbulent and processing parameters 
need to be adjusted accordingly, but the cracking characteristics remained the same. The response to preheating 
was similar for both pure tungsten and the alloys tested in this study; there was no beneficial effect of the alloy 
additions. This work shows that the fundamental metallurgical cause of microcracking in tungsten can be cir -
cumvented, in a step towards structural applications of additively manufactured tungsten. 
1. Introduction 
Tungsten (W) is the preferred material for plasma facing components 
in the divertor of the ITER fusion reactor, in part due to its high melting 
temperature, high thermal conductivity, and low fuel retention [1] . 
Nevertheless, pure W is difficult to process and possesses undesirable 
properties, such as weak grain boundaries and a ductile to brittle tran -
sition (DBT) that occurs around 473 – 673 K [2,3] . The DBT is caused by 
the limited mobility of ½ < 111 > screw dislocations in the BCC lattice [4, 
5] , and the DBT temperature (DBTT) can be decreased by an ultrafine 
grain size [6,7] , lower impurity content [8] , or alloying, particularly 
with rhenium [9,10] . Using other substitutional alloying elements [11] 
or alloying with dispersed oxides or carbides [2,12] has in general not 
proven effective at lowering the DBTT, though these do strengthen the 
material - in particular the grain boundaries - increase the recrystalli -
zation temperature, and can refine the microstructure. 
In laser powder bed fusion (LPBF), the laser locally melts metal 
powder in successive layers to create an object defined by 2D slices of a 
3D CAD file. The localized heat source creates a small melt pool that is 
on the order of 10
 3 
mm
3 
in volume, which results in rapid and repeated 
heating and cooling cycles, and thermal gradients in excess of 10
6 
K/m 
[13] . In all metals, the residual stresses that are thus generated lead to 
distortion [14] and affect the mechanical performance [15,16] . For 
some metals, macro- or microcracks are created, often times through a 
combination of residual stress and metallurgical phenomena such as 
solidification cracking, liquiation cracking, precipitation hardening, or 
the formation of undesired phases [17,18] . Specifically for W, our pre -
vious work shows that microcracking in W LPBF happens due to the 
DBT, by observation of the delay between solidification and cracking 
that corresponds to the time it takes for the material to cool to the DBTT 
[19] . 
Microcracking affects the structural integrity of parts but is not an 
issue for non-loaded W parts such as collimators or waveguides. Instead, 
those applications leverage tungsten ’ s high density, and have previously 
been successfully produced by LPBF [20] . Near full density W parts have 
been made in several efforts [21 – 23] , and many studies have tried to 
mitigate the microcracking in W, mainly by using alloying additions or 
preheating. Nanosized ZrC powder additions reduced grain size by 50% 
* Corresponding author at: Department of Mechanical Engineering, KU Leuven, Celestijnenlaan 300, 3001 Leuven, Belgium. 
E-mail address: bey.vrancken@kuleuven.be (B. Vrancken). 
Contents lists available at ScienceDirect 
Additive Manufacturing 
journal homepag e: www.else vier.com/loc ate/addma 
https://doi.org/10.1016/j.addma.2021.102158 
Received 13 April 2021; Received in revised form 25 June 2021; Accepted 30 June 2021

## Page 2

Additive Manufacturing 46 (2021) 102158
2
and reduced cracking [24] , as did alloying with 5 wt% Ta in Ref. 25 , 
though Ref. 26 indicates Ta alloying was ineffective. Excessive micro -
cracking occurs for high energy densities (high power P and/or low 
speed v ), as observed in W-3Ta [27] and Mo [28] , which also cracks due 
to the DBT. Ivekovi ´c et al. [29] found that microcracks are present after 
LPBF of a W7Ni3Fe tungsten heavy alloy despite preheating to 673 K, 
but that cracks could be eliminated by heat treating at 1773 K, possibly 
by backfilling with the low melting temperature Ni-Fe-W rich binder 
phase. 
For most metals, preheating is the most effective way to mitigate 
residual stresses in LPBF [30 – 32] . In W, preheating to 673 K did not lead 
to significant improvements [26] , but preheating to 1273 K reduced 
cracking and changed the crack network morphology [33] . Typically, 
the crack network consists of cracks along the center of the scan vectors, 
with S-shaped connecting branches due to the grain morphology [26] . 
Preheating to 1273 K led to a more uniform crack network but did not 
eliminate cracking [33] . Wright [34] compared LPBF and electron beam 
melting (EBM) of W, and found that the combination of the vacuum 
environment and 1273 K preheating used in EBM is able to mitigate 
microcracking. 
Our earlier work using in situ high-speed optical imaging visualizes 
the DBT by capturing delayed cracking in the fusion zone that coincides 
with the cooldown to the DBTT [19] . In this work, a similar approach is 
used to study the effect of two common microcracking mitigation stra -
tegies, namely preheating up to 873 K and alloying with 2 wt% of rare 
earth oxides. 
2. Materials & methods 
2.1. In situ high-speed video 
The high-speed imaging experimental setup is schematically shown 
in Fig. 1 , and is adapted slightly from that described in Ref. 19 . A 
Photron Fastcam SA-Z high-speed camera coupled to an Infinity Model 
K2 DistaMax ™ long-distance microscope captures high resolution video 
at a 60 kHz frame rate and 896 × 368 pixel resolution, with an equiv -
alent magnification of 2.55 µ m/pixel. The dichroic longpass filter (950 
nm cutoff) mounted outside the vacuum chamber enables top-down 
imaging. A Cavilux HF 500 W low coherence laser source ( λ = 808 
nm) pulsed at 1 µ s provides coaxial lighting, while a Yb-fiber laser ( λ =
1070 nm, P
max
= 500 W, Ø = 80 µ m (1/ e
2
), YLR-500-WC-Y14, IPG 
Photonics) coupled to a galvanometer scanning mirror system (Nutfield 
Technology, 3XB 3-Axis Scan Head) scans across the stationary field of 
view. The vacuum chamber was evacuated to 10
 2 
Torr and backfilled 
with Ar to 740 Torr, which flowed at 650 SCCM during the experiments, 
keeping the oxygen content in the atmosphere below 30 ppm as moni -
tored by a Zirox XS22 vacuum probe. The substrates are placed in a 
custom nickel holder attached to a Momentive PBN/PG heater. The 
substrate temperature is measured using a K-type thermocouple spot 
welded to the nickel holder A combination of Macor insulation, custom 
Cu heatsink, and standoffs are used to limit the temperature of an 
Attocube ECSx5050 linear nanopositioner, to which the assembly is 
mounted, to below 373 K. 
2.2. Material and processing 
The 4 mm thick pure W substrates are cut from a 25.4 mm diameter, 
> 99.95% purity, < 30 ppm oxygen, pure W rod (Eagle Alloys Corpo -
ration) using wire EDM, and the surface partially ground using 1200 grit 
SiO
2 
paper. This material is referred to as ‘pure W
′
in the remainder of 
this work. Three different tungsten oxide dispersion strengthened alloys, 
alloyed with 2 wt% of (1) La
2
O
3
, (2) CeO
2
, and (3) a mix of 1.75 wt% 
La
2
O
3
, 0.12 wt% ZrO
2
, and 0.12 wt% Y
2
O
3
, were investigated. Since 
there was no discernible difference in their behavior, the oxide disper -
sion strengthened alloys will all be referred to as W-Rare Earth Oxides or 
W-REO. They are supplied by Midwest Tungsten as 3.2 mm (1/8
′′
) 
diameter, 178 mm (7
′′
) length welding electrodes, and sectioned longi -
tudinally to expose a flat surface on which the scans were performed. 
Microcracks in pure W welding electrodes from Midwest Tungsten were 
observed to behave similarly to that in the pure W rod material from 
Eagle Alloys Corporation, validating the use of welding electrodes as 
substrate material. The motivation to investigate oxide strengthened W 
is multifold. First, small, dispersed inclusions strengthen the grain 
boundaries in tungsten by taking up interstitial impurities that would 
otherwise reside along, and weaken the grain boundaries [35,36] . This 
would increase the resistance to intergranular crack propagation, the 
dominant cracking regime in W [37] . Second, though such oxide par -
ticles have generally been ineffective at affecting the DBTT, one study 
suggests a beneficial effect on lowering the DBTT, strongest for ThO
2 
and Na
2
O [38] . Lastly, these particles significantly increase the recrys -
tallization temperature, which is the upper boundary of the temperature 
working range [38] . While the recrystallization temperature is not the 
subject of this investigation, a W material suitable for fusion applica -
tions requires a higher recrystallization temperature. If this material is to 
be processed by LPBF, the behavior of the enabling particles needs to be 
understood. 
2.3. Characterization 
The crack network morphology and melt pool width on the top 
surface are examined using a Keyence VK-X100 3D laser scanning mi -
croscope. The substrates are sectioned, ground, and polished using 
standard metallographic sample preparation techniques. The micro -
structure is studied after swab etching for 5 – 60 s with a modified Mur -
akami ’ s reagent (15 g K
3
Fe(CN)
4 
+ 2 g KOH dissolved in 100 ml H
2
O) 
using a FEI Quanta 200 environmental SEM. 
2.4. Thermomechanical modeling 
The implicit, Lagrangian finite element code Diablo [39] is used to 
perform thermomechanical simulations for a range of preheating tem -
peratures. Convection ( h = 10 W/m
2
-K), radiation ( ε = 0.23), and 
evaporation boundary conditions are included on the top surface of the 
model. For both convection and radiation, a far field temperature of 
T
∞
= 303 K is used. The evaporation boundary condition includes the 
effects of latent heat of evaporation and the heat loss due to mass flux 
from vaporization [40] . The bottom surface of the tungsten substrate is 
Camera
Bandpass filter
Ar
W substrate
Scanning laser
Dichroic Beamsplitter
Illumination laser
Vacuum chamber
Heating element
Insulation/Heat Management
Linear stage
Long-distance microscope
Fig. 1. Schematic representation of the experimental setup enabling in situ 
high-speed optical imaging and laser scanning experiments at high 
temperature. 
B. Vrancken et al.

## Page 3

Additive Manufacturing 46 (2021) 102158
3
fixed at the preheating temperature and zero normal displacements are 
prescribed on all sides of the computational domain except the top 
surface. As Diablo is a Lagrangian code, fluid flow after melting is not 
explicitly modeled. Thus, a Goldak [41] type volumetric heat source is 
used with the ellipsoidal dimensions tuned to match the experimental 
melt pool width, as validated in Ref. 19 . The effective absorptivity for 
the modeled process parameters (P = 400 W, v = 400 mm/s) is 0.55 as 
determined from experiments conducted in Ref. 42 . 
Temperature-dependent thermophysical properties for pure W are 
obtained up to melt from Refs. 43,44 . Temperature-dependent me -
chanical properties are obtained up to at least 1473 K from Appendix A 
of the ITER structural design criteria for in-vessel components (SDC-IC) 
[45] . Since no mechanical properties could be found at higher temper -
atures, the yield stress is linearly extrapolated to 0 MPa at the melt 
temperature, such that there would be zero deviatoric stress at tem -
peratures greater than melt. Similarly, the Young ’ s modulus is decreased 
to 10% of its room temperature value upon reaching melt. All other 
material properties are held constant above their reported temperature 
range. A finite deformation, strain rate independent material model with 
linear isotropic hardening is used, as described in [46] . All accumulated 
plastic strains are reset upon reaching the melt temperature. Further 
details concerning the numerical solution strategies employed by Diablo 
can be found in [47] . 
Half symmetry, with the symmetry plane along the center of the scan 
track and normal vector transverse to the scan direction, is used to 
reduce the size of the simulations. After a mesh size sensitivity analysis, 
a mesh size of 10 µ m is used along the longitudinal direction (x) of the 
beam and 5 – 10 µ m spacing along the transverse direction (y) within the 
vicinity of the melt pool. A similar mesh size is used in the z , or depth, 
direction. The mesh size increases further away from the melt area. The 
total simulation domain is 3.5 × 1.25 × 2 mm
3
, large enough to avoid 
boundary condition uncertainties affecting the results in the heat 
affected zone (HAZ). Each simulation consists of approximately 1 
million elements and requires computation times on the order of 10
3 
cpu-hours. 
3. Results 
3.1. Substrate preheating 
In our previous work, the median temperature at which delayed, 
sudden cracking occurred for P = 400 W and v = 400 mm/s was 594 K 
(with a 534 – 648 K Q1 - Q3 interval) [19] . Fig. 2 a shows the resulting 
crack network for this parameter set as a combination of parallel cracks 
adjacent to the scan track, connected by periodic transversal cracks 
across the solidified weld. Supplementary Video 1 a further shows that 
the cracks occur suddenly, consistent with the previously observed 
cracking behavior, and the melt width without preheating is 87 ± 2 µ m. 
e
b
No preheating
No preheating c
773 K
773 K573 K
100 µm 100 µm
100 µm
Fig. 2. (a – c) Top surface of two adjacent scan tracks using P = 400 W, v = 400 mm/s showing (a) cracking across and adjacent to the scan track without preheating, 
(b) cracking only in the adjacent material for 573 K preheating, indicated by 2 white arrows, and (c) scan tracks without cracks with 773 K preheating. (d) Crack 
pattern of a 1 by 2 mm area scanned using hatch spacing h = 25 µ m, and (e) absence of cracks in a 1 by 2 mm area scanned using 773 K preheating. 
Video 1. Microcrack behavior of pure tungsten using P = 400 W, 
v = 400 mm/s, (a) at room temperature, (b) at 573 K, and (c) at 773 K. At 
room temperature (a), sudden cracking occurs around and behind the moving 
melt pool, while this type of cracking is absent at preheating temperatures 
above 523 K. Between 573 K and 773 K, cracks grow continuously in front of 
and alongside the melt pool. At and above 773 K, both types of cracking are 
eliminated.A video clip is available online. Supplementary material related to 
this article can be found online at doi:10.1016/j.addma.2021.102158. 
B. Vrancken et al.

## Page 4

Additive Manufacturing 46 (2021) 102158
4
The transversal cracks are eliminated by preheating the substrate to 
573 K, leaving only a branched crack network in the HAZ alongside the 
scan, indicated by the white arrows in Fig. 2 b. This major difference is 
also visible when comparing Supplementary Video 1 a with Video 1b , as 
cracks no longer appear suddenly after a certain delay when using 573 K 
preheating, but rather form continuously alongside the melt pool. The 
melt is also slightly wider at 91 ± 2 µ m. Lastly, Fig. 2 c and Video 1c 
show that preheating to 773 – 873 K, well above the DBTT, eliminates 
both cracking mechanisms. The melt track is considerably wider at 
103 ± 2 µ m , and Fig. 2 c shows nearly no cracks in either the solidified 
material or the substrate around it. The exact temperature above which 
complete elimination of cracks occurred in this work ranged from 773 K 
to 873 K, likely depending on the amount of time the sample tempera -
ture was allowed to stabilize at the testing temperature. The crack 
mitigating effect of preheating persists when scaling up from a single 
scan track to a hatched area. Without preheating, a large crack network 
is formed as in Fig. 2 d, whereas only small, isolated cracks are found 
using 773 K preheating in Fig. 2 e. 
Fig. 3 compares the simulated Von Mises residual stresses resulting 
from a 2 mm long laser scan using P = 400 W, v = 400 mm/s, without 
preheating ( Fig. 3 a) and using T
preheat
= 773 K ( Fig. 3 b). The compar -
ison along the horizontal symmetry line, for the first half of the scan 
vector, shows absolute stresses that are 35 – 40% lower when using 773 K 
preheating. In Fig. 3 c and d, the second half of the scan vector is shown, 
but the residual stresses are scaled by the yield stress at the relevant 
preheating temperature. Without preheating, the room temperature 
yield stress equals 1350 MPa, whereas the yield stress at 773 K is only 
855 MPa [45] . Fig. 3 c and d show that the residual stress reaches the 
yield stress in both cases but is also limited by the yield stress. No further 
stresses are introduced during subsequent cooling under equilibrium 
conditions, resulting in the lower final residual stresses for 773 K pre -
heating, as shown in Fig. 3 b. The significant drop of the yield stress with 
increasing temperature is the major driver for the reduction in residual 
stresses with increasing preheating. For preheating temperatures that 
exceed the DBTT, the maximum residual stresses that are introduced 
into the material are lower than the material ’ s strength at the DBTT, and 
therefore do not cross the threshold required to induce DBT driven 
microcracking. From Fig. 3 d, it is also apparent that preheating enlarges 
the area that experiences relatively high residual stress, as a result of 
lower thermal gradients that translate to lower residual stress gradients. 
A third benefit of preheating is related to the strain rate dependence of 
the DBTT [5,48] . The DBTT increases with increasing strain rate, but the 
strain rate at the DBTT is reduced from ~ 10
0
-10
1 
s
 1 
without pre -
heating [19] to ~ 10
 6 
s
 1 
during equilibrium cooling (taken as 
0.17 K/s) for preheating temperatures above the DBTT. 
As mentioned earlier, cracking persists at preheating temperatures 
above the DBTT, though the mechanism and location are different. At 
and above 573 K and below 773 – 873 K, delayed cracking no longer 
occurs after passage of the melt pool, which indicates that the DBT 
driven cracking is effectively avoided. The mechanism for continuous 
cracking in the substrate in front of and alongside the melt up to 
773 – 873 K is unclear and subject of future work, though this too was 
avoided by sufficiently high preheating temperatures. 
3.2. Alloying 
Fig. 4 a and b compare the top surface of a P = 400 W, v = 400 mm/s 
weld on pure W with a weld on a W-REO substrate. Compared to pure W, 
the W-REO weld shows signs of an unstable melt pool, spatter, and a 
different crack network morphology. This is evident in Supplementary 
Video 2 , in which close-up videos of a pure W weld and W-REO weld are 
compared for identical scan parameters that were suitable to form a 
stable melt pool in pure W [19] . In Video 2a, the pure W melt pool is 
stable and in conduction mode. A crack network continuously grows in 
front of and adjacent to the melt pool, in addition to two delayed, but 
sudden transversal cracks in the solidified material at X = 48 µ m from 
the left edge of the video and t = 3100 µ s, and X = 426 µ m and 
t = 4720 µ s. In contrast, the melt of the alloyed material in Video 2b is 
turbulent and unstable. In addition to a significant vapor plume, spatter 
is ejected from the melt in all directions, and sometimes entrained in the 
vapor plume. While there is no crack network developing alongside the 
moving melt, the surface of the heat affected zone displays a peculiar 
pattern shown in Fig. 4 c. Liquiation of the rare earth oxides in the heat 
affected zone causes droplets to be pushed to the surface, where they 
leave circular contour lines after evaporation and/or dissociation. 
Finally, after a significantly longer delay than in the pure W, a crack 
traverses the solidified scan track in Video 2b at X = 59 (below the weld) 
and 171 µ m (above the weld) at t = 5840 µ s. The two opposite, 
perfectly perpendicular cracks in the adjacent substrate connect through 
a longitudinal crack running down the center of the scan track, which is 
not visible due to the black contrast of the solidified weld. Such longi -
tudinal cracks are also observed in pure W for excessive powers, and are 
associated with deeper melt pools. 
The melt pool cross sections in Fig. 5 show that W-REO melt pools are 
extremely narrow and deep compared to pure W for identical P - v con -
ditions. In Fig. 5 a, using P = 300 W and v = 300 mm/s results in a 
shallow, 87 µ m wide and 25 µ m deep melt pool for pure W, which is in 
stark contrast to the 93 µ m wide and 260 µ m deep melt pool for W-REO 
shown in Fig. 5 b. Similarly, the relatively large, 236 µ m wide and 
223 µ m deep melt pool for pure W shown in Fig. 5 c for P = 450 W and 
500 µm
a c
b d
No prehea/g415ng
500°C
Fig. 3. Top surface view of Von Mises residual stress simulations in and around a 2 mm track using P = 400 W, v = 400 mm/s, without preheating (a and c) and 
T
preheat
= 773 K (b and d), plotted as the absolute (a and b) Von Mises stress and relative to the yield stress at the relevant temperature (c and d). The dashed line 
outlines the scan track, the white arrow the scan direction. 
B. Vrancken et al.

## Page 5

Additive Manufacturing 46 (2021) 102158
5
v = 100 mm/s, differs significantly from the melt shown in Fig. 5 d 
(90 µ m wide and 695 µ m deep). Moreover, a vertical crack network 
reaches from the surface down to the bottom of the melt cross section for 
the W-REO material. Scan parameters that were suitable for pure W 
therefore need to be revised for use on W-REO. Fig. 5 e shows that 
reducing the laser power to 200 W with a 200 mm/s scan speed results 
in the formation of more shallow melt pools, in this case 69 µ m wide and 
18 µ m deep. Lastly, Fig. 5 f highlights a notable difference between the 
microstructures of the pure W and W-REO substrates. For pure W 
( Fig. 5 a and b), the substrate microstructure consists of vertically 
elongated grains, and the melt pool is hard to distinguish from the 
substrate due to epitaxial solidification, only noticeable through spo -
radic porosity at the melt pool boundary and angled grain boundaries 
from grains growing towards the top center of the melt. The W-REO 
substrate also consists of elongated grains, though these are roughly one 
order of magnitude smaller and oriented horizontally. The rare earth 
oxide particles (darker contrast in Fig. 5 e and f) are similarly elongated 
and have a cross section of around 1 µ m with lengths ranging from 5 µ m 
to 30 µ m . The rare earth oxide particles (darker contrast in Fig. 5 e and f) 
are distributed evenly throughout the substrate at the grain boundaries 
between the elongated W grains. Analysis of a representative number of 
particles (399 particles in a 280 µ m by 170 µ m area) shows a median 
cross section of 4.1 µ m
2 
(range 0 – 52 µ m
2
) and median aspect ratio of 7.9 
(range 1.3 – 39). When this material melts during laser scanning, the W 
matrix grains cannot solidify epitaxially due to the unfavorable grain 
orientations of the substrate and form new, equiaxed grains. The rare 
earth oxides will globularize and float upwards, potentially even boiling 
out of the melt, as is evident from the significant vapor plume in Sup -
plementary Video 2b. If they fail to reach the surface before solidifica -
tion, they remain as round particles, two of which are shown in the melt 
cross section in Fig. 5 e. This is similar to the globularization of the ThO
2 
particles in thoriated W (another type of W welding electrode) exposed 
to sub-second melting and solidification cycles in Ref. 49 . While it ap -
pears that the microcracking is reduced in the W-REO material in Fig. 4 b 
and Fig. 7 a compared to the pure W in Fig. 4 a, the different crack 
network morphologies are caused by the morphological grain texture of 
200 µm 
Pure W 
W - REO 
W - REO 
200 µm 
100 µm 
a 
b 
c 
Fig. 4. Top surface scan track morphology using P = 400 W, v = 400 mm/s showing (a) a stable melt behavior and smooth track with a branched network of cracks 
for pure W, versus (b) an irregularly shaped track of W – REO, with evidence of spatter adjacent to the track, and cracks that run perfectly perpendicular to the scan 
track in the adjacent material. In (c) the W – REO material adjacent to the scan track displays a contour line pattern due to liquiation of REO particles in the heat 
affected zone. 
Video 2. Scan track of (a) pure tungsten and (b) W-2La
2
O
3 
using P = 450 W, 
v = 300 mm/s. In (a), the melt pool is stable and in conduction mode, and a 
crack network continuously develops in front of and alongside the melt pool, as 
well as delayed cracking within the scan track at t = 3100 µ s and 4720 µ s. In 
(b) there is a significant vapor plume, and spatter is ejected from the melt pool. 
Small liquid droplets are pushed out of the substrate material adjacent to the 
melt pool, and a crack occurs at t = 5840 µ s.A video clip is available online. 
Supplementary material related to this article can be found online at 
doi:10.1016/j.addma.2021.102158. 
B. Vrancken et al.

## Page 6

Additive Manufacturing 46 (2021) 102158
6
the substrate. For pure W, the elongated grains oriented perpendicular 
to the surface create a grain boundary network that is prone to crack 
growth and branching, whereas the grain orientation in the W-REO 
material disables transversal cracks from branching towards each other 
to form a continuous network. While transgranular cracking could take 
place, intergranular cracking is typically the dominant cracking regime 
in W, due to the low solubility of interstitial impurities that segregate to 
the grain boundaries [36] . Brittle inclusions situated at the grain 
boundaries can shift the cracking regime from transgranular to inter -
granular [50] , but in this case, intergranular is already the dominant 
mechanism. The difference in grain morphology is therefore considered 
to be the most important factor in the different crack network mor -
phologies, and not the effect of the oxide particles itself. 
In our previous work [19] , the time delay between solidification and 
transversal cracking in the fusion zone was demonstrated to increase 
with increasing linear energy density P / v . Using the same methodology, 
Fig. 6 shows the linear correlation also exists for W-REO, albeit with a 
longer delay for similar P / v ratios compared to pure W. All three 
different W alloys behave similarly and are assumed to fall on the same 
linear correlation. For some parameter sets, the longitudinal cracks in 
the W-REO material reduced the amount of transversal cracking to the 
extent that no transversal cracks were observed in the field of view of the 
100 µm
a bd
c
ef
10 µm10 µm
100 µm
100 µm 100 µm
W W-REO
W-REO
W-REOW-REO
W
Fig. 5. Melt pool differences between pure W (a and c) and W-REO (b,d,e,f) for the same process parameters (a and b: P = 300 W, v = 300 mm/s. c and d: 
P = 450 W, v = 100 mm/s). The melt pools in W-REO are narrow and deep with vertical cracks extending to the bottom (b and d), compared to the wider melt pools 
in pure W (a and c). (e) Adjusting the parameters to P = 200 W and v = 200 mm/s results in better melt pool shapes for W-REO. The morphological orientation of the 
grains in the substrates differ as well, being elongated in the vertical direction for pure W (a and c), and in the horizontal direction for W-REO (f). 
B. Vrancken et al.

## Page 7

Additive Manufacturing 46 (2021) 102158
7
high-speed video in any of the ten repetitions. Notably, this happened 
for P = 450 W and v = 100 mm/s for all three different W-REO mate -
rials, which is why there is such a large gap in the data points for the 
W-REO between P/v = 3 and 6 J/mm. 
3.3. Preheating and alloying 
Due to the unstable behavior of the W-REO alloy melt pool discussed 
in the previous section, the power and speed were adjusted towards 
lower energy inputs for the following experiments. As a result, the scan 
tracks using P = 250 W and v = 400 mm/s shown in Fig. 7 a and b 
present a smooth and continuous weld bead, 72 µ m wide and 19 µ m 
deep without preheating and 88 µ m wide and 22 µ m deep for 773 K 
preheating. Adjacent to the weld lines, the HAZ is clearly visible. While 
longitudinal cracking was still prevalent in the W-REO material dis -
cussed in Section 3.2 , this is now absent by lowering the energy input, 
likely due to limiting the melt depth. Transversal cracks are still present 
without preheating, and are indicated with arrows in Fig. 7 a. When 
scanning multiple vectors adjacent to each other with a hatch spacing 
h = 25 µ m as shown in Fig. 7 c, long transversal cracks are formed that 
span across multiple scan vectors. The cracks follow a zigzag pattern, 
changing direction locally to run perpendicular to the visible ripples or 
‘chevrons ’ that mark the trailing, solidifying edge of the melt pool in 
order to follow the grain boundaries in the solidified material. Applying 
a preheating temperature to the W-REO material has similar effects as 
have been described for pure W in Section 3.1 . There are no discernable 
cracks in the single track in Fig. 7 b, and while cracks are not completely 
eliminated in Fig. 7 d (indicated by the white arrow), the crack opening 
displacement is greatly reduced. 
4. Discussion 
4.1. Alloy element behavior 
At 2713 K (Y
2
O
3
), 2588 K (La
2
O
3
), and 2873 K (CeO
2
), the rare earth 
oxides all have a congruent melting point roughly 1000 K lower than the 
melting point of pure W, which melts at 3695 K. Additionally, these 
oxides have significant vapor pressures below their melting point, with 
La
2
O
3 
and Y
2
O
3 
dissociating readily according to M
2
O
3 
(s) → 2MO 
(g) + ½ O
2 
(g) for T > 2300 K and 2500 K, respectively [51,52] . CeO
2 
is 
not a sesquioxide and sublimates slightly substoichiometrically to 
CeO
2 x
. In fact, CeO
2 
sublimation is used to deposit thin film 
anti-reflective optical coatings, indicating that it also has a substantial 
vapor pressure before melting [53] . This dissociation and sublimation of 
the oxides is the cause of the turbulent melt behavior and significant 
vapor plume visible in Video 2b, and the resulting deep keyhole mode 
melt pools for excessive power inputs. Within the melt, the fraction of 
oxides that does melt forms large, coherent spherical particles as shown 
in Fig. 5 e. In the HAZ, these oxides melt and sublimate while the sur -
rounding W matrix remains solid. As a result, the liquid oxide can be 
seen bubbling up adjacent to the melt pool in Video 2b, leaving the 
concentric ring patterns shown in Fig. 4 c. 
The release of oxygen through the above-mentioned dissociation 
reaction is a cause of concern. An increasing oxygen impurity concen -
tration in W also increases the DBTT [8] , which would make cracking 
even harder to circumvent by preheating. However, the W-REO material 
in this work reacted similarly to preheating as pure W, with a near full 
elimination of cracks by substrate preheating to 773 K, indicating that 
0
5
10
15
20
25
30
35
0123456
Crack delay [ms] 
P/v [J/mm] 
Pure W
W - 2% La2O3
W - 2% CeO2
W - 2% Mix
Fig. 6. Time delay between solidification and cracking in the fusion zone in -
creases with increasing energy input P/v. The different W alloys display a 
similar behavior, in which cracking appears later than in pure W (pure W data 
from [19] ). 
100 µm 100 µm
cd
100 µm 100 µm
ab No preheating 773 K
Fig. 7. Scan track morphology for W-REO using P = 250 W, v = 400 mm/s. (a) Without preheating, cracks run perpendicular to the scan track. (b) Using 773 K 
preheating, the melt pool is wider and cracks are eliminated. (c) Cracks run perpendicular across all scan vectors, in a zigzag pattern obeying the local grain boundary 
orientations. (d) Some cracks are still present, though shorter and with a smaller opening. 
B. Vrancken et al.

## Page 8

Additive Manufacturing 46 (2021) 102158
8
the O
2 
was not absorbed in significant quantities by the W melt. 
4.2. W-REO cracking 
The crack network morphology differs greatly between the pure W 
and the W-REO material. 
Our previous work describes a linear correlation between the linear 
energy input P/v , and the time delay between solidification and cracking 
[19] , wherein the solidified material takes longer to cool down to the 
DBTT for higher P / v ratios. This correlation is captured by rewriting the 
Rosenthal equation [54] as in Eq. (1) , where t
crack 
is the time it takes for 
the material to reach the cracking temperature T
crack 
(equivalent to the 
DBTT) after passage of a traveling point heat source, t
melt 
the time to 
reach the solidification/melting temperature T
melt 
(3695 K), A the laser 
absorptivity, k the thermal conductivity, and T
ambient 
the surrounding 
equilibrium temperature (303 K). 
∆ t = t
crack
 t
m
=
P
v
(
A
2 π k
)(
1
T
crack
 T
ambient
 
1
T
melt
 T
ambient
)
(1) 
For the pure W data in Fig. 6 , the baseline median cracking tem -
perature was found to be around 500 K, though it increased significantly 
for low P/v due to an increase in strain rate [19] . Fig. 6 also shows that 
cracking delays for the W-REO alloys examined in this work are 2.5 
times longer than for pure W. However, it is incorrect to assume that this 
difference is due to a lower DBTT. On the contrary, the W-REO material 
displayed an identical response to preheating as the pure W, in partic -
ular the temperature at which the sudden and delayed cracking was no 
longer observed. Moreover, the various REO used in this work and other 
particles such as TiC have not been shown to significantly affect the 
DBTT, especially not as micron-sized particles [2,12,55] . Instead, the 
different slopes of the linear correlations in Fig. 6 are caused by (1) a 
different thermal conductivity and (2) a significantly more efficient 
energy coupling through the keyhole shaped melt pool morphology of 
the W-REO material. 
First, Righini et al. [56] found that the electrical resistivity, and by 
correlation the thermal conductivity, of W – 2 wt% ThO
2 
was very 
similar to that of pure W above 1200 K up until melting, differing 
slightly due to the vol% of ThO
2 
in the W matrix. However, Gaudio et al. 
[57] used Swartz and Pohl ’ s [58] description of the thermal conduc -
tivity as a function of the distance between phonon scattering centers (i. 
e. the distance between the oxide particles) to show that the conduc -
tivities of pure W and W – 1 wt% La
2
O
3 
diverge significantly towards 
room temperature. The temperature-dependent thermal conductivity for 
the pure W and W-REO material in this work is calculated as in Ref. 57 
(using scattering center distances of 100 µ m and 5 µ m for pure W and 
W-REO, respectively), and shown in Fig. 8 . Eq. (1) can then be re-written 
and solved as a piecewise function as in Eq. (2) below, in which Δ t
i 
is the 
time interval to cool down between temperatures T
i 
and T
i + 1 
with 
T
0
= T
crack
≤ T
i
< T
melt
= T
M 
and k
i 
is the average thermal conductivity 
in the T
i 
– T
i + 1 
interval. The summation term on the right side of Eq. (2) 
is 17% larger for the W-REO material due to the different thermal 
conductivity at lower temperatures, which is the first factor contributing 
to the different cracking delays of pure W and W-REO alloys. 
∆ t =
∑
M
i = 0
∆ t
i
=
P
v
A
2 π
∑
M
i = 0
1
k
i
(
1
T
i
 T
ambient
 
1
T
i + 1
 T
ambient
)
(2) 
Second, Righini et al. [56] also found that there is no significant 
difference in the inherent absorptivity of pure W and W-REO. However, 
the melt pool shape varies greatly in this work between the two mate -
rials. For pure W, using Eq. (2) and the linear fit of the data in Fig. 6 
yields an absorptivity A = 0.32. This value matches well with the 
measured absorptivity value of 0.3 during laser scanning of W in con -
duction mode, as measured over a wide range of process parameters by 
Matthews et al. [42] . The shallow melt shape and stable melt pool sur -
face observed for pure W for nearly all of the P-v combinations are clear 
indications that conduction mode occurred for pure W in this work as 
well. Similarly, the same procedure results in an absorptivity A = 0.68 
for the W-REO material, which again corresponds well with the ab -
sorptivity of 0.7 found in Ref. 42 , this time for keyhole mode welding, 
since multiple reflections of the laser light inside the keyhole vapor 
depression increase the overall absorptivity [59,60] . As shown in Fig. 5 b 
and d, the W-REO melt was indeed a narrow and deep keyhole for most 
of the parameter combinations used to determine the data points in 
Fig. 6 . 
4.3. Towards complete crack mitigation 
This work suggests that the microcracking issue in W during LPBF is 
not a fundamental problem that cannot be overcome, as cracking was 
gradually reduced by increasing the preheating temperature, and was 
completely eliminated by preheating above 773 – 873 K. However, pre -
heating to 673 K [26] or even 1273 K [33] still resulted in a network of 
cracks inside LPBF fabricated W parts in other studies. The only differ -
ence is that building a 3D part requires W powder compared to the W 
rods used as substrates in this work. Converting W raw material into 
spherical powders suitable for LPBF drastically increases the oxygen 
impurity content. For example, the W rod in this work contains 
< 30 ppm of oxygen, as per the supplier. On the other hand, TEKNA 
states that their spherical W powders contain < 250 ppm of oxygen 
[61] . Stephens [8] found that an increase in oxygen content from 10 to 
50 ppm increased the DBTT of their material from 623 K to 823 K. It is 
therefore plausible that a material with up to 250 ppm of O content has a 
DBTT above 1273 K, or at least that this temperature is not far enough 
above the DBTT to mitigate cracking. Unfortunately, the LPBF process 
requires the feedstock to consist of fine powders. To accommodate 
higher O content in commercially available powder, an active oxygen 
removal strategy is required, similar to that demonstrated for Mo by 
Kaserer et al. [62] and Braun et al. [63] , who by the addition of 
elemental C to the Mo powder outgassed some CO at high preheating 
temperatures, and formed Mo
2
C during the process. The formation of CO 
consumed O both from the Mo and from the atmosphere, while the Mo
2
C 
has a higher interstitial solubility for O. For W, an even more aggressive 
strategy might be appropriate since the DBTT of W is higher than that of 
Mo, by directly bonding O to a different element with a higher affinity 
than W. This in situ formation of an oxide ideally serves a dual purpose: 
to remove O from the W matrix as well as strengthening the grain 
boundaries and inducing some degree of grain refinement. 
To that effect, the oxide particles in this work failed to complete their 
intended purpose. They were already oxidized and had a limited 
50
70
90
110
130
150
170
500 1000 1500 2000 2500 3000 3500
Thermal conductivity k [W/Km]
T emperature [K]
W-REO
Pure W
ITER Appendix A [45]
Fig. 8. Calculated thermal conductivity of W-REO (dashed line) and pure W 
(solid line) using the same procedure as in Ref. 57 . For reference, the pure W 
conductivity as stated in the ITER Appendix A [45] is given by the dotted line. 
B. Vrancken et al.

## Page 9

Additive Manufacturing 46 (2021) 102158
9
potential to further extract oxygen from the W matrix. Second, the large 
oxide particles were not broken up and finely dispersed within the melt 
pool but remained coherent and spheroidized into large round particles, 
hereby failing to act as grain boundary strengtheners or grain refiners. In 
situ formation of secondary particles typically leads to a much finer 
distribution thereof in the final microstructure [64] . In future work, we 
intend to introduce pure metal precursor particles with a greater affinity 
for oxygen than W to bind the oxygen, and form nanosized particle re -
inforcements at the grain boundaries. Of the oxides investigated in this 
work, ZrO
2 
or Y
2
O
3 
are preferred over La
2
O
3 
or CeO
2 
because of the 
higher melting point of pure Y (1799 K) or Zr (2128 K) versus 1193 K for 
La and 1071 K for Ce. 
5. Conclusion 
Microcracking was fully eliminated in W substrates by preheating to 
above 773 K, which shows that the problems caused by the ductile-to- 
brittle transition during LPBF of W can be circumvented. The rare 
earth oxide alloy additions in this work did not perform as intended, as 
they neither removed oxygen from the W matrix, nor were they finely 
dispersed along the grain boundaries in the melt. However, a combined 
approach of preheating to temperatures safely above the DBTT with an 
active oxygen getter alloying strategy is likely to completely eliminate 
cracks in W parts. 
CRediT authorship contribution statement 
Bey Vrancken : Conceptualization, Methodology, Validation, Inves -
tigation, Writing - original draft, Visualization, Project administration. 
Rishi K. Ganeriwala : Methodology, Software, Writing - review & 
editing. Aiden A. Martin : Resources, Writing - review & editing. 
Manyalibo J. Matthews : Conceptualization, Resources, Writing - re -
view & editing, Supervision, Funding acquisition. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgements 
B.V. would like to thank Gabe Guss for the assistance in setting up the 
high-speed video experiments. This work was performed under the 
auspices of the U.S. Department of Energy by Lawrence Livermore Na -
tional Laboratory under Contract No. DE-AC52-07NA27344. This work 
was funded by the Laboratory Directed Research and Development 
Program at LLNL under project tracking code 18-ERD-057 and 18-SI- 
003. 
References 
[1] T. Hirai, S. Panayotis, V. Barabash, C. Amzallag, F. Escourbiac, A. Durocher, 
M. Merola, J. Linke, Th Loewenhoff, G. Pintsuk, M. Wirtz, I. Uytdenhouwen, Use of 
tungsten material for the ITER divertor, Nucl. Mater. Energy 9 (2016) 616 – 622, 
https://doi.org/10.1016/j.nme.2016.07.003 . 
[2] S. Antusch, D.E.J. Armstrong, T.B. Britton, L. Commin, J.S.K.-L. Gibson, 
H. Greuner, J. Hoffmann, W. Knabl, G. Pintsuk, M. Rieth, S.G. Roberts, 
T. Weingaertner, Mechanical and microstructural investigations of tungsten and 
doped tungsten materials produced via powder injection molding, Nucl. Mater. 
Energy 3 – 4 (2015) 22 – 31, https://doi.org/10.1016/j.nme.2015.04.002 . 
[3] P. Gumbsch, J. Riedle, A. Hartmaier, H.F. Fischmeister, Controlling factors for the 
brittle-to-ductile transition in tungsten single crystals, Science 282 (1998) 
1293 – 1295, https://doi.org/10.1126/science.282.5392.1293 . 
[4] E. Tarleton, S.G. Roberts, Dislocation dynamic modelling of the brittle – ductile 
transition in tungsten, Philos. Mag. 89 (2009) 2759 – 2769, https://doi.org/ 
10.1080/14786430902992619 . 
[5] A. Giannattasio, Z. Yao, E. Tarleton, S.G. Roberts, Brittle – ductile transitions in 
polycrystalline tungsten, Philos. Mag. 90 (2010) 3947 – 3959, https://doi.org/ 
10.1080/14786435.2010.502145 . 
[6] A.A.N. N ´emeth, J. Reiser, D.E.J. Armstrong, M. Rieth, The nature of the brittle-to- 
ductile transition of ultra fine grained tungsten (W) foil, Int. J. Refract. Met. Hard 
Mater. 50 (2015) 9 – 15, https://doi.org/10.1016/j.ijrmhm.2014.11.005 . 
[7] G. Liu, G.J. Zhang, F. Jiang, D. Ding, Y.J. Sun, J. Sun, E. Ma, Nanostructured high- 
strength molybdenum alloys with unprecedented tensile ductility, Nat. Mater. (n. 
d.). 〈 https://www.nature.com/articles/nmat3544 〉 . (Accessed 3 December 2020). 
[8] J.R. Stephens, Effects of Interstitial Impurities on the Low-Temperature Tensile 
Properties of Tungsten, National Aeronautics and Space Administration Cleveland 
OH Lewis Research Center, 1964. 〈 https://apps.dtic.mil/sti/citations/ADA396979 
〉 . (Accessed 15 September 2020). 
[9] M. Garfinkle, W.D. Klopp, W.R. Witzke, Superplasticity in tungsten–rhenium 
alloys, Undefined, 1968. /paper/SUPERPLASTICITY-IN-TUNGSTEN–RHENIUM- 
ALLOYS.-Garfinkle-Klopp/fea377190f40a82be0712ff7dcdfc6499f4cf6d7 . 
(Accessed 3 December 2020). 
[10] P.L. Raffo, Yielding and fracture in tungsten and tungsten-rhenium alloys, J. Less 
Common Met. 17 (1969) 133 – 149, https://doi.org/10.1016/0022-5088(69) 
90047-2 . 
[11] T. Palacios, J.Y. Pastor, Tungsten – vanadium – yttria alloys for fusion power reactors 
(II): mechanical characterization, Int. J. Refract. Met. Hard Mater. 54 (2016) 
159 – 164, https://doi.org/10.1016/j.ijrmhm.2015.07.031 . 
[12] M. Battabyal, R. Sch ¨aublin, P. Sp ¨atig, N. Baluc, W – 2wt%Y2O3 composite: 
microstructure and mechanical properties, Mater. Sci. Eng. A 538 (2012) 53 – 57, 
https://doi.org/10.1016/j.msea.2012.01.011 . 
[13] I. Yadroitsev, P. Krakhmalev, I. Yadroitsava, Selective laser melting of Ti6Al4V 
alloy for biomedical applications: temperature monitoring and microstructural 
evolution, J. Alloy. Compd. 583 (2014) 404 – 409, https://doi.org/10.1016/j. 
jallcom.2013.08.183 . 
[14] J.-P. Kruth, J. Deckers, E. Yasa, R. Wauthl ´e, Assessing and comparing influencing 
factors of residual stresses in selective laser melting using a novel analysis method, 
Proc. Inst. Mech. Eng. Part B J. Eng. Manuf. 226 (2012) 980 – 991, https://doi.org/ 
10.1177/0954405412437085 . 
[15] B. Vrancken, V. Cain, R. Knutsen, J. Van Humbeeck, Residual stress via the contour 
method in compact tension specimens produced via selective laser melting, Scr. 
Mater. 87 (2014) 29 – 32, https://doi.org/10.1016/j.scriptamat.2014.05.016 . 
[16] S. Leuders, M. Th ¨one, A. Riemer, T. Niendorf, T. Tr ¨oster, H.A. Richard, H.J. Maier, 
On the mechanical behaviour of titanium alloy TiAl6V4 manufactured by selective 
laser melting: fatigue resistance and crack growth performance, Int. J. Fatigue 48 
(2013) 300 – 307, https://doi.org/10.1016/j.ijfatigue.2012.11.011 . 
[17] M.M. Attallah, R. Jennings, X. Wang, L.N. Carter, Additive manufacturing of Ni- 
based superalloys: the outstanding issues, MRS Bull. 41 (2016) 758 – 764, https:// 
doi.org/10.1557/mrs.2016.211 . 
[18] J.H. Martin, B.D. Yahata, J.M. Hundley, J.A. Mayer, T.A. Schaedler, T.M. Pollock, 
3D printing of high-strength aluminium alloys, Nature 549 (2017) 365 – 369, 
https://doi.org/10.1038/nature23894 . 
[19] B. Vrancken, R.K. Ganeriwala, M.J. Matthews, Analysis of laser-induced 
microcracking in tungsten under additive manufacturing conditions: experiment 
and simulation, Acta Mater. 194 (2020) 464 – 472, https://doi.org/10.1016/j. 
actamat.2020.04.060 . 
[20] K. Deprez, S. Vandenberghe, K. Van Audenhaege, J. Van Vaerenbergh, R. Van 
Holen, Rapid additive manufacturing of MR compatible multipinhole collimators 
with selective laser melting of tungsten powder, Med. Phys. 40 (2013), 012501, 
https://doi.org/10.1118/1.4769122 . 
[21] A.C. Field, L.N. Carter, N.J.E. Adkins, M.M. Attallah, M.J. Gorley, M. Strangwood, 
The effect of powder characteristics on build quality of high-purity tungsten 
produced via laser powder bed fusion (LPBF), Met. Mater. Trans. A 51 (2020) 
1367 – 1378, https://doi.org/10.1007/s11661-019-05601-6 . 
[22] A.T. Sidambe, Y. Tian, P.B. Prangnell, P. Fox, Effect of processing parameters on 
the densification, microstructure and crystallographic texture during the laser 
powder bed fusion of pure tungsten, Int. J. Refract. Met. Hard Mater. 78 (2019) 
254 – 263, https://doi.org/10.1016/j.ijrmhm.2018.10.004 . 
[23] B. Vrancken, R. Wauthl ´e, J.-P. Kruth, J. Van Humbeeck, Study of the influence of 
material properties on residual stress in selective laser melting, in: Proceedings of 
the Solid Freeform Fabrication Symposium, 2013, pp. 393 – 407. 〈 https://lirias.kul 
euven.be/1572878 〉 . (Accessed 31 March 2020). 
[24] K. Li, D. Wang, L. Xing, Y. Wang, C. Yu, J. Chen, T. Zhang, J. Ma, W. Liu, Z. Shen, 
Crack suppression in additively manufactured tungsten by introducing secondary- 
phase nanoparticles into the matrix, Int. J. Refract. Met. Hard Mater. 79 (2019) 
158 – 163, https://doi.org/10.1016/j.ijrmhm.2018.11.013 . 
[25] D. Wang, Z. Wang, K. Li, J. Ma, W. Liu, Z. Shen, Cracking in laser additively 
manufactured W: initiation mechanism and a suppression approach by alloying, 
Mater. Des. 162 (2019) 384 – 393, https://doi.org/10.1016/j.matdes.2018.12.010 . 
[26] A. Ivekovi ´c, N. Omidvari, B. Vrancken, K. Lietaert, L. Thijs, K. Vanmeensel, 
J. Vleugels, J.-P. Kruth, Selective laser melting of tungsten and tungsten alloys, Int. 
J. Refract. Met. Hard Mater. 72 (2018) 27 – 32, https://doi.org/10.1016/j. 
ijrmhm.2017.12.005 . 
[27] K. Li, Y. Li, W. Chen, C. Zhao, Y. Yuan, L. Cheng, T.W. Morgan, W. Liu, Z. (James) 
Shen, Effect of Ta addition on the fuzz formation of additively manufactured W 
based materials, Nucl. Fusion (2020), https://doi.org/10.1088/1741-4326/ 
ab8a69 . 
[28] D. Wang, C. Yu, J. Ma, W. Liu, Z. Shen, Densification and crack suppression in 
selective laser melting of pure molybdenum, Mater. Des. 129 (2017) 44 – 52, 
https://doi.org/10.1016/j.matdes.2017.04.094 . 
[29] A. Ivekovi ´c, M.L. Montero-Sistiaga, K. Vanmeensel, J.-P. Kruth, J. Vleugels, Effect 
of processing parameters on microstructure and properties of tungsten heavy alloys 
fabricated by SLM, Int. J. Refract. Met. Hard Mater. 82 (2019) 23 – 30, https://doi. 
org/10.1016/j.ijrmhm.2019.03.020 . 
B. Vrancken et al.

## Page 10

Additive Manufacturing 46 (2021) 102158
10
[30] K. Kempen, B. Vrancken, S. Buls, L. Thijs, J. Van Humbeeck, J.-P. Kruth, Selective 
laser melting of crack-free high density M2 high speed steel parts by baseplate 
preheating, J. Manuf. Sci. Eng. 136 (2014) . 
[31] D. Buchbinder, W. Meiners, N. Pirch, K. Wissenbach, J. Schrage, Investigation on 
reducing distortion by preheating during manufacture of aluminum components 
using selective laser melting, J. Laser Appl. 26 (2014), 012004, https://doi.org/ 
10.2351/1.4828755 . 
[32] B. Vrancken, S. Buls, J.-P. Kruth, J. Van Humbeeck, Influence of preheating and 
oxygen content on Selective Laser Melting of Ti6Al4V, in: Proceedings of the 16th 
RAPDASA Conference, 2015. 〈 https://lirias.kuleuven.be/1748568 〉 (accessed 
March 31, 2020). 
[33] A. v Müller, G. Schlick, R. Neu, C. Anst ¨att, T. Klimkait, J. Lee, B. Pascher, 
M. Schmitt, C. Seidel, Additive manufacturing of pure tungsten by means of 
selective laser beam melting with substrate preheating temperatures up to 1000 ∘ C, 
Nucl. Mater. Energy 19 (2019) 184 – 188, https://doi.org/10.1016/j. 
nme.2019.02.034 . 
[34] J. Wright, Additive Manufacturing of Tungsten via Selective Laser Melting and 
Electron Beam Melting (PhD), University of Sheffield, 2019. 〈 http://etheses.white 
rose.ac.uk/26247/ 〉 . (Accessed 3 December 2020). 
[35] R.I. Jaffee, G.T. Hahn, Structural Considerations in Developing Refractory Metal 
Alloys, Defense Metals Information Center, Battelle Memorial Institute, 1963. 
[36] B. Gludovatz, Fracture Behavior of Tungsten, University of Leoben, 2010 . 
[37] B. Gludovatz, S. Wurster, A. Hoffmann, R. Pippan, Fracture toughness of 
polycrystalline tungsten alloys, Int. J. Refract. Met. Hard Mater. 28 (2010) 
674 – 678, https://doi.org/10.1016/j.ijrmhm.2010.04.007 . 
[38] R.I. Jaffee, B.C. Allen, D.J. Maykuth, Effects of dispersions on the recrystallization 
and ductile to brittle transition behavior of tungsten, in: Powder Metallurgy in the 
Nuclear Age: Plansee Proceedings 1961, Metallwerk Plansee AG, Reutte/Tyrol, n. 
d., pp. 770 – 798. 
[39] J.M. Solberg, N.E. Hodge, M.A. Puso, S.T. Castonguay, R.K. Ganeriwala, R. 
M. Ferencz, Diablo: A Parallel, Implicit Multi-physics Finite Element Code for 
Engineering Analysis User Manual, Lawrence Livermore National Laboratory, 
2018 . 
[40] J. Barrett, C. Clement, Kinetic evaporation and condensation rates and their 
coefficients, J. Colloid Interface Sci. 150 (1992) 352 – 364, https://doi.org/ 
10.1016/0021-9797(92)90205-Z . 
[41] J. Goldak, A. Chakravarti, M. Bibby, A new finite element model for welding heat 
sources, Metall. Trans. B 15 (1984) 299 – 305, https://doi.org/10.1007/ 
BF02667333 . 
[42] M. Matthews, J. Trapp, G. Guss, A. Rubenchik, Direct measurements of laser 
absorptivity during metal melt pool formation associated with powder bed fusion 
additive manufacturing processes, J. Laser Appl. 30 (2018), 032302, https://doi. 
org/10.2351/1.5040636 . 
[43] P. Tolias, Analytical expressions for thermophysical properties of solid and liquid 
tungsten relevant for fusion applications, Nucl. Mater. Energy 13 (2017) 42 – 57, 
https://doi.org/10.1016/j.nme.2017.08.002 . 
[44] J.J. Valencia, P.N. Quested, Thermophysical properties, in: ASM Handbook, 
Volume 15: Casting, ASM International, 2008, pp. 468 – 481, https://doi.org/ 
10.1361/asmhba0005240 . 
[45] Appendix A to ITER SDC-IC, 2013. 
[46] R.K. Ganeriwala, M. Strantza, W.E. King, B. Clausen, T.Q. Phan, L.E. Levine, D. 
W. Brown, N.E. Hodge, Evaluation of a thermomechanical model for prediction of 
residual stress during laser powder bed fusion of Ti-6Al-4V, Addit. Manuf. 27 
(2019) 489 – 502, https://doi.org/10.1016/j.addma.2019.03.034 . 
[47] N.E. Hodge, R.M. Ferencz, J.M. Solberg, Implementation of a thermomechanical 
model for the simulation of selective laser melting, Comput. Mech. 54 (2014) 
33 – 51, https://doi.org/10.1007/s00466-014-1024-2 . 
[48] A. Giannattasio, S.G. Roberts, Strain-rate dependence of the brittle-to-ductile 
transition temperature in tungsten, Philos. Mag. 87 (2007) 2589 – 2598, https://doi. 
org/10.1080/14786430701253197 . 
[49] E.C. Horrigan, J. Haidar, F. Righini, Physical changes in tungsten and thoriated 
tungsten electrodes after subsecond heating, Int. J. Thermophys. 17 (1996) 
1037 – 1045, https://doi.org/10.1007/BF01441992 . 
[50] M.F. Ashby, C. Gandhi, D.M.R. Taplin, Overview No. 3 Fracture-mechanism maps 
and their construction for f.c.c. metals and alloys, Acta Metall. 27 (1979) 699 – 729, 
https://doi.org/10.1016/0001-6160(79)90105-6 . 
[51] H.W. Goldstein, P.N. Walsh, D. White, Rare earths. I. Vaporization of La2O3 and 
Nd2O3: dissociation energies of gaseous LaO and NdO1, J. Phys. Chem. 65 (1961) 
1400 – 1404, https://doi.org/10.1021/j100826a029 . 
[52] P.N. Walsh, H.W. Goldstein, D. White, Vaporization of rare-earth oxides, J. Am. 
Ceram. Soc. 43 (1960) 229 – 233, https://doi.org/10.1111/j.1151-2916.1960. 
tb14589.x . 
[53] G. Atanassov, R. Thielsch, D. Popov, Optical properties of TiO2, Y2O3 and CeO2 
thin films deposited by electron beam evaporation, Thin Solid Films 223 (1993) 
288 – 292, https://doi.org/10.1016/0040-6090(93)90534-V . 
[54] D. Rosenthal, The theory of moving sources of heat and its application to metal 
treatments, Trans. ASME 43 (1946) 849 – 866 . 
[55] G. Pintsuk, D. Blagoeva, J. Opschoor, Thermal shock behavior of tungsten based 
alloys manufactured via powder injection molding, J. Nucl. Mater. 442 (2013) 
S282 – S286, https://doi.org/10.1016/j.jnucmat.2013.01.342 . 
[56] F. Righini, J. Spisiak, G.C. Bussolino, A. Rosso, J. Haidar, Measurement of 
thermophysical properties by a pulse-heating method: thoriated tungsten in the 
range 1200 to 3600 K, Int. J. Thermophys. 15 (1994) 1311 – 1322, https://doi.org/ 
10.1007/BF01458839 . 
[57] P. Gaudio, R. Montanari, E. Pakhomova, M. Richetta, A. Varone, W-1% La2O3 
submitted to a single laser pulse: effect of particles on heat transfer and surface 
morphology, Metals 8 (2018) 389, https://doi.org/10.3390/met8060389 . 
[58] E.T. Swartz, R.O. Pohl, Thermal boundary resistance, Rev. Mod. Phys. 61 (1989) 
605 – 668, https://doi.org/10.1103/RevModPhys.61.605 . 
[59] T.R. Allen, W. Huang, J.R. Tanner, W. Tan, J.M. Fraser, B.J. Simonds, Energy- 
coupling mechanisms revealed through simultaneous keyhole depth and 
absorptance measurements during laser-metal processing, Phys. Rev. Appl. 13 
(2020), 064070, https://doi.org/10.1103/PhysRevApplied.13.064070 . 
[60] J. Ye, S.A. Khairallah, A.M. Rubenchik, M.F. Crumb, G. Guss, J. Belak, M. 
J. Matthews, Energy coupling mechanisms and scaling behavior associated with 
laser powder bed fusion additive manufacturing, Adv. Eng. Mater. 21 (2019), 
1900185, https://doi.org/10.1002/adem.201900185 . 
[61] Tekna, Spherical Tungsten Metal Powder, Tekna, n.d. 〈 http://www.tekna.com 
/spherical-powders/tungsten 〉 . (Accessed 15 December 2020). 
[62] L. Kaserer, J. Braun, J. Stajkovic, K.-H. Leitz, B. Tabernig, P. Singer, I. Letofsky- 
Papst, H. Kestler, G. Leichtfried, Fully dense and crack free molybdenum 
manufactured by Selective Laser Melting through alloying with carbon, Int. J. 
Refract. Met. Hard Mater. 84 (2019), 105000, https://doi.org/10.1016/j. 
ijrmhm.2019.105000 . 
[63] J. Braun, L. Kaserer, I. Letofsky-Papst, K.-H. Leitz, H. Kestler, G. Leichtfried, On the 
role of carbon in molybdenum manufactured by Laser Powder Bed Fusion, Int. J. 
Refract. Met. Hard Mater. 92 (2020), 105283, https://doi.org/10.1016/j. 
ijrmhm.2020.105283 . 
[64] B. Vrancken, S. Dadbakhsh, R. Mertens, K. Vanmeensel, J. Vleugels, S. Yang, J.- 
P. Kruth, Selective Laser Melting process optimization of Ti – Mo – TiC metal matrix 
composites, CIRP Ann. 68 (2019) 221 – 224, https://doi.org/10.1016/j. 
cirp.2019.04.120 . 
B. Vrancken et al.
