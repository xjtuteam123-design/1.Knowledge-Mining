# 1-s2.0-S0927025625000795-main

<!-- source: D:\总文献\1-s2.0-S0927025625000795-main.pdf -->
<!-- file_sha256: b4d2e72ee55b7cc2aded96586d9ad93ad3019c9187fced43097e548006e9d075 -->

## Page 1

Full Length Article
Effect of two-phase microstructure characteristics on high strain rate 
elastoplastic deformation of superalloys: A three-dimensional discrete 
dislocation dynamics study
Ronghai Wu
a , b , *
, Zheng Wang
c
, Xiaoxiang Wu
d
, Heng Li
b , *
a
Shenzhen Research Institute of Northwestern Polytechnical University, Shenzhen 518057, PR China
b
State Key Lab of Solidification Processing, School of Materials Science and Engineering, Northwestern Polytechnical University, Xi ’ an 710072, PR China
c
School of Mechanics, Civil Engineering and Architecture, Northwestern Polytechnical University, Xi ’ an 710129, PR China
d
School of Iron and Steel, Soochow University, Suzhou 215137, PR China
ARTICLE INFO
Keywords:
Discrete dislocation dynamics
Elastoplastic deformation
Superalloys
Micromechanics
ABSTRACT
The two-phase microstructure may bring excellent mechanical properties to materials such as superalloys used 
for advanced turbine engines. Experiments and continuum scale simulations focus on normal strain rate ( < 10
1 
s
 1
) deformation, while atomistic simulations focus on ultra-high strain rate ( > 10
6 
s
 1
) deformation. The high 
strain rate regime in-between has attracted much less attention. In the present work, by developing a three- 
dimensional discrete dislocation dynamics with continuum description of two-phase microstructure, the effect 
of matrix channel, precipitate APB energy, precipitate volume fraction, matrix/precipitate coherent interface 
misfit on high strain rate (2 × 10
3 
s
 1
) elastoplastic deformation of two-phase superalloys are systematically 
studied. The control variable approach of different two-phase microstructure characteristics, which is difficult to 
conduct in experiments, is strictly applied in the present work to reach quantitative simulations. The stress – strain 
response, evolution of dislocation density on each slip system, three-dimensional microstructure and three- 
dimensional stress field are analyzed in detailed to investigate the mechanisms behind. Some common elasto -
plastic features irrelevant to the distinction of two-phase microstructure characteristics, as well as some specific 
elastoplastic features closely relevant to different two-phase microstructure characteristics are revealed. The 
elastoplastic commonalities and distinctions between normal, high and ultra-high strain rates are also discussed. 
Some suggestion for improving the high temperature strength of superalloys is proposed.
1. Introduction
The excellent resistance to high temperature deformation of Ni- 
based single crystal superalloys is closely attributed to their distinctive 
two-phase microstructure [1 – 5] , which consists of FCC-structured γ 
matrix and L1
2
-structured γ’ precipitates [6] . The qualitative mecha -
nisms how the characteristics of two-phase microstructure affect me -
chanical properties have been roughly understood. The γ’ precipitate 
APB energy, γ matrix channel width, γ’ volume fraction and γ / γ’ inter -
face misfit may all have influence on the elastoplastic deformation of 
superalloys [7 – 9] . Although existing high-resolution microscopic ob -
servations can provide some details on the phase structure and dislo -
cation evolution of Ni-based single crystal alloys [10 – 13] , experimental 
techniques cannot obtain real-time evolution processes of 
microstructures. It is difficult to obtain information on stress fields, 
strain fields, energy fields, etc., which makes it difficult to quantitatively 
explain deformation mechanisms. Besides, it is also difficult to quanti -
tatively change one characteristic while keeping the rest characteristics 
the same in experiments. Hence, the quantitative understanding on ef -
fect of two-phase microstructure characteristics on plastic deformation 
have not been reached and the mechanisms behind are not clear yet. 
With the development of numerical simulation methods, some attempts 
have been made for the quantitative understanding on effect of two- 
phase microstructure characteristics on plastic deformation [14 – 19] . 
However, the dislocation dynamics at continuum scale is not mature yet, 
it is not desirable in the scenario that fine dislocation activities with 
different characteristics of two-phase microstructure are required. Be -
sides, experiments and continuum scale simulations mainly focus on 
* Corresponding authors at: State Key Lab of Solidification Processing, School of Materials Science and Engineering, Northwestern Polytechnical University, Xi ’ an 
710072, PR China.
E-mail addresses: ronghai.wu@nwpu.edu.cn (R. Wu), liheng@nwpu.edu.cn (H. Li). 
Contents lists available at ScienceDirect
Computational Materials Science
journal homepag e: www.else vier.com/loc ate/comma tsci
https://doi.org/10.1016/j.commatsci.2025.113736
Received 29 October 2024; Received in revised form 14 January 2025; Accepted 24 January 2025 
Computational Materials Science 250 (2025) 113736 
Available online 1 February 2025 
0927-0256/© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## Page 2

normal strain rate ( < 10
1 
s
 1
) deformation, while atomistic simulations 
mainly focus on ultra-high strain rate ( > 10
6 
s
 1
) deformation due to 
their small temporal-spatial limit.
Instead, discrete dislocation dynamics (DDD) is naturally suitable for 
high strain rate simulation and has been used in the study of Ni-based 
superalloys and other alloys [20 – 22] . Yashiro et al. introduced a back 
stress model into traditional DDD methods, studied the effect of APB 
energy on dislocation motion, and demonstrated the process of dislo -
cations cutting through the γ ’ phase in Ni-based single crystal alloys 
[23] . Huang and Yang et al. further extended the back stress model and 
established a DDD model that can reflect the decomposition of dislo -
cations and the interaction between incomplete dislocations in high- 
temperature alloys [24 – 26] . Similarly, Huang et al. also studied the 
influence of interface dislocation networks on dislocation evolution in 
the matrix channels of Ni-based single crystal superalloys by combining 
them with finite element method based on this model, and extended the 
DDD framework of Ni-based single crystal superalloys to more effec -
tively simulate the shear of a large number of precipitated phases in 
super dislocation pairs [27,28] . Haghighat and co-workers developed a 
novel 3D-DDD with a hybrid mobility law for glide and climb to study 
the evolution of the dislocation activities in a γ / γ ′ microstructure of a 
single crystal Ni-based superalloy for different climb rates and loading 
conditions [29] . The method was also used to reveal the origin of creep 
dislocations in a single crystal Ni-based superalloy [30] . Zhang and co- 
workers introduced residual stress, interactions between dislocations 
and grain boundaries to studied role of the residual stress, geometrically 
necessary dislocations and related kinematic hardening in gradient 
grained materials [31,32] . The above work all use regular cubic pre -
cipitation phases, which can lead to singularity of forces, and do not 
consider the effect of other microstructure characteristics such as γ’ APB 
energy, γ / γ’ interface misfit and γ matrix width.
In the present work, we develop a 3D DDD method coupling to 
continuum description of different two-phase microstructure charac -
teristics. The high strain rate tensile behaviors of single crystal super -
alloys with different APB energy, γ matrix channel width, γ’ volume 
fraction and γ / γ’ interface misfit are simulated. The quantitative effect 
of two-phase microstructure characteristics on elastoplastic deformation 
is analyzed in detail.
2. Materials and methods
2.1. Simulation setup
For purely discrete dislocation simulations, grid mesh is not needed. 
Nevertheless, to describe the phase microstructure, grid mesh is intro -
duced into the simulations. The microstructure consists of one γ’ pre -
cipitate surrounded by γ matrix channels, with one dislocation segment 
in each of the {111} < -110 > main slip systems in the γ matrix is 
randomly prescribed, as shown in Fig. 1 . The endpoints of dislocation 
segment are pinned by the two intersected γ / γ’ interfaces, leading to 
artificial Frank-Read sources. The γ’ precipitate is a cube with smoothed 
edges to avoid stress singularity caused by sharp edges. The simulation 
domain is a cuboid with 560 × 570 × 590 nm instead of a cube, in order 
to avoid dislocations self-annihilation. Tensile loading is applied along 
the vertical direction (or [001]) with constant strain rate of 2000 s
 1 
at 
1253 K. Settings with different γ matrix channel widths (60 nm, 80 nm, 
and 100 nm), γ’ APB energies (62.5 mJ / m
2
, 125 mJ / m
2
, and 250 
mJ / m
2
), γ’ volume fractions (55.5 %, 67.5 %, and 74.3 %) and γ / γ’ 
interface lattice misfits (0.0, 0.003, and 0.006) are simulated. The 
other simulations parameters are listed in Table 1 . From C
11
, C
12 
and 
C
44
, the bulk modulus is calculated by K = ( C
11
+ C
12
) / 3, which is in -
dependent of slip systems. The shear modulus and Poisson ’ s ratio are 
calculated by G = C
44 
and ν = C
12
/ ( C
11
+ C
12
) for the {1 1 1} 〈 1 1 0 〉
slip systems loading along 〈 0 0 1 〉 direction. The simulation setup agrees 
with typical microstructure observed in experiments. The DDD codes are 
developed based on TRIDIS which discretizes dislocation lines into 
alternating sequences of pure edge and screw segments [22,33] .
2.2. Modelling 3D DDD with continuum description of two-phase 
microstructure
According to experiments, the evolution of γ’ precipitate takes place 
at a time scale of hours while DDD simulation is at nanoseconds to mi -
croseconds, so the γ’ precipitate is assumed to be static. In the γ matrix, 
the effective stress τ
eff 
of exerted on dislocation segments is the sum -
mation of the following stresses: (1) Long-range interaction stresses σ
int 
generated by other dislocation segments except for adjacent dislocation 
segments; (2) Long-range misfit stress σ
mis 
caused by the coherent γ / γ’ 
interface; (3) Long-range externally applied stress σ
app
; (4) Short-range 
line tension stress τ
lt 
between the current dislocation segment and 
adjacent dislocation segments due to curvature; (5) Short-range Peierls- 
Nabarro stress τ
P 
due to the lattice friction. The long-range stresses are 
projected to each slip system. The resolved shear stress τ
g 
is calculated 
using the Peach-K ¨ohler equation [34] : 
τ
g
=
{[
 
σ
app
+ σ
int
+ σ
mis
)
•
b
b
]
× l
}
• g (1) 
Fig. 1. Illustration of initial microstructure for simulations.
Table 1 
Simulation parameters.
Parameter Value
The length of γ’ precipitate 550 nm × 570 nm × 590 nm
Burgers vector 0.25 nm
Initial dislocation density
1 × 10
13
m
- 2
Temperature 1253 K
C
11
( γ phase) 210 GPa
C
12
( γ phase) 154 GPa
C
44
( γ phase) 85 GPa
C
11
( γ ′ phase) 220 GPa
C
12
( γ ′ phase) 140 GPa
C
44
( γ ′ phase) 122 GPa
C
44
( γ ′ phase) 122 GPa
R. Wu et al. Computational Materials Science 250 (2025) 113736 
2

## Page 3

where b is the Burgers vector, b is the magnitude of the Burgers vector, l 
is the line vector of the dislocation segment, and g is the slip direction. 
The external stress σ
app 
can be directly added to simulation domain as a 
homogenous stress, as we use periodic boundary. The interaction stress 
σ
int 
of the i -th dislocation segment induced by the j -th dislocation 
segment in the global coordinate system is calculated by 
 
σ
int
i
)
j
=
 
σ
int
i
)
j → A
 
 
σ
int
i
)
j → B
(2) 
where A and B indicate the two endpoints of the j -th dislocation 
segment. 
 
σ
int
i
)
j → A 
and 
 
σ
int
i
)
j → B 
are stresses induced by semi-infinite 
dislocation segments with endpoints A and B , respectively. The 
detailed formula is given in previous literature [35] . Summarizing the 
interaction stress produced by all the dislocation segments, the total 
interaction stress of i -th dislocation segment is obtained by: 
σ
int
i
=
∑
N
m ∕= i
 
σ
int
i
)
m
(3) 
where N is the total number of dislocation segments. The misfit stress 
σ
mis 
is induced by the coherent γ / γ’ misfit strain ε
mis 
which can be 
regarded as the subtraction of total strain and elastic strain by: 
ε
mis
= ε ε
el
(4) 
The relation between elastic strain and stress follows the Hooke ’ s law 
by: 
σ = C : ε
el
(5) 
C = ( 1 ϕ ) C
γ
+ ϕ C
γ ʹ
(6) 
where C is the stifiness tensor which is regarded as an interpolation of 
the stiffness tensors of the γ and γ’ phases. It is defined ϕ = 1 in the γ’ and 
ϕ = 0 in the γ . We assuming that mechanical equilibrium is reached 
instantaneously at each time step, that is 
∇ • σ = 0 (7) 
Substituting Eqs. (4) – (6) into Eq. (7), σ can be numerically solved fast 
Fourier transform. The continuum description in the present work is 
mainly reflected by the modulus mismatch and γ / γ ′ misfit induced long- 
range stress σ . Note that when solving Eq. (7), numeric grids are needed. 
The effective stress τ
eff 
acting on dislocations can be calculated as: 
τ
eff
=
⎧
⎨
⎩
0 , if τ
P
≥
⃒
⃒
τ
g
+ τ
lt
⃒
⃒
in γ
τ
g
+ τ
lt
- τ
P
, if τ
P
<
⃒
⃒
τ
g
+ τ
lt
⃒
⃒
in γ
τ
g
+ τ
lt
- τ
P
+ τ
APB
, in γ ʹ
(8) 
where the calculation of τ
lt 
is given in previous literature [36] . Note that 
the direction (or sign) of τ
lt 
points to the center of a dislocation loop. 
When a dislocation segment cuts into the γ’ precipitate, the resulting 
sheared area transforms into an anti-phase boundary (APB), possessing a 
free energy that exceeds twice the energy of the γ / γ’ interface. As the 
system constantly prefers lower energy scenario, the anti-phase 
boundary serves as a resistance stress to push the dislocation segment 
out of the γ’ precipitate, which is the origin of the APB stress. However, 
if another dislocation segment (i.e. trailing dislocation) on the same slip 
plane also cuts into the γ’ precipitate following the leading dislocation 
segment, the sheared area of the trailing dislocation closes the APB, 
lowering the system free energy. So, it is much easier to cut into the γ’ 
precipitate by a pair of dislocations (i.e. super dislocations) than by a 
single dislocation. Initially, one dislocation segment in each of the 
{111} < -110 > main slip systems in the γ matrix is randomly prescribed, 
as shown in Fig. 1 . The endpoints of dislocation segment are pinned by 
the two intersected γ / γ’ interfaces, leading to artificial Frank-Read 
sources. Then dislocations multiply in the γ matrix and pile up at the 
γ / γ’ interface. As the multiplication and pile-up go on, super dislocations 
may form and cut into the γ’ precipitate. The leading and trailing dis -
locations are mainly distinguished by the following equation [24] : 
F
app
=
[(
σ
app
•
b
b
)
× l
]
• g (9) 
F
int
=
[(
σ
int
•
b
b
)
× l
]
• g (10) 
where the shear forces F
app 
and F
int 
in the slip direction of leading and 
trailing dislocations are calculated. The leading dislocation is exerted 
external shear force F
app 
dragging it into the γ’ precipitate and the shear 
force F
int 
from trailing dislocation pushing it into the γ’ precipitate, 
hence there is F
app
× F
int 
≥ 0 for the leading dislocation. The trailing 
dislocation is exerted external shear force F
app 
dragging it into the γ’ 
precipitate and the shear force F
int 
from leading dislocation pushing 
way from of the γ’ precipitate, hence there is F
app
× F
int 
< 0 for the 
trailing dislocation. At the same time, the leading dislocation is sub -
jected to a back stress τ
APB
= -sign ( τ
eff
) χ
APB
/ b pushing it out of the γ’ 
precipitate and the trailing dislocation is subjected to the same attractive 
stress τ
APB 
= sign ( τ
eff
) χ
APB
/ bto close the APB.
The velocity v of a single dislocation segment is calculated from the 
local stress field by: 
v =
τ
eff
| b |
B
(9) 
where B is the drag coefficient. The shear strain of a simulation cell is 
determined by summing up the swept area by all the mobile dislocations 
in each slip system. The glide shear strain η of a slip system is computed 
as: 
η =
b
V
∑
N
i = 1
L
i
v
i
Δ t (10) 
where V is the volume of the simulation cell, i is the number of dislo -
cation segments and Δ t is the time step of dislocation glide. Thus, the 
components of the plastic strain tensor are given by: 
ε
pl
ij
=
∑
12
k
1
2
(
n
k
i
b
k
j
+ n
k
j
b
k
i
)
η
k
(11) 
where n
k
i 
and b
k
i 
are the component of the slip plane normal and the 
Burgers vector of the slip system k , respectively.
3. Results and discussions
3.1. Effect of matrix channel width on elastoplastic deformation
By setting three different γ matrix channel widths (60 nm,80 nm and 
100 nm), the effect of γ matrix channel width on elastoplastic defor -
mation is studied. The APB energy, γ’ precipitate volume fraction and 
γ / γ’ misfit are fixed to 125 mJ/m
2
, 67.5 % and 0.003, respectively. The 
stress – strain curves and hardening rate-strain curves are shown in Fig. 2 . 
It can be seen that the stress – strain curves first increase linearly in the 
elastic deformation stage to total strain of 0.4 %, then increase non -
linearly in the plastic deformation stage and reach the maximum at total 
strain around 2.0 %-2.5 %, regardless of the γ matrix channel width. It 
can be seen from Fig. 2 (a) that under the same strain in the elastic 
deformation stage, the stresses with different γ matrix channel widths 
are the same. Under the same strain in the plastic deformation stage, the 
stress decreases as the γ matrix channel width increases. In other words, 
it needs higher stress to generate the same plastic deformation for nar -
rower γ matrix channel. This can also be evidently seen in Fig. 2 (b), 
where the hardening rate is plotted. It is because the narrower γ matrix 
R. Wu et al. Computational Materials Science 250 (2025) 113736 
3

## Page 4

channel width leads to bigger line tension resistance for bowing out of 
dislocations. The hardening rate is calculated by d σ
zz
/ d ε
pl
zz
, where the 
d σ
zz 
and d ε
pl
zz 
are the increments of stress and plastic strain in the loading 
direction, respectively. Fig. 3 shows the 3D microstructure at plastic 
strain 0.2 %. As can be seen, dislocation networks are well formed and 
more dislocations are deposited at the γ / γ’ interfaces with narrower γ 
matrix channel.
To have a statistical understanding on the effect of γ matrix channel 
width on plastic deformation, the evolution of dislocation density on 
each slip system is plotted in Fig. 4 . It can be seen in Fig. 4 (a) that the 
total dislocation density constantly increases with plastic strain 
regardless of the γ matrix channel width, while at the same plastic strain, 
the total dislocation density decreases as the channel width increases. 
The ratio of the initial slopes (the dotted straight lines) in Fig. 4 (a) is 
about 100:80:60 for the channel width of 60:80:100. It can be explained 
as follows. Assuming a length increment of dislocation segment 2 Δ x in 
the γ matrix channel, then increment of dislocation density is calculated 
by Δ ρ = 2 Δ x / V, where V is the volume of simulation domain. The 
increment of sheared area can be estimated by a rectangle d Δ x, where d 
is the γ channel width. The increment of plastic strain can be estimated 
as Δ ε
pl
zz
= b d Δ x / V. Therefore, the ratio of the initial slopes (the dotted 
straight lines) in Fig. 4 (a) can be estimated by Δ ρ / Δ ε
pl
zz
= 2 / bd, in which 
the ratio is inversely proportional to the channel width. Dislocations do 
not cut into the γ’ precipitate until the plastic strain 0.2 %, which cor -
responds to the microstructure in Fig. 3 . The reason is that the leading 
dislocation needs large pushing stress from the trailing dislocations 
while pilling up at the γ / γ’ interfaces, to overcome the APB stress 
resistance for cutting into the γ’ precipitate. An interesting phenomenon 
is that dislocation density increases with the plastic strian linearly before 
dislocations cuttting into the γ’ precipitate and the slope of such line -
arity is bigger for narrower γ matrix channel, while the slope remains 
nonlinearly positive but decreases after dislocations cuttting into the γ’ 
precipitate. The reason of the linearity before dislocations cuttting into 
the γ’ precipitate is that the dislocation multiply in the γ matrix channel 
and we use linear relation between plastic strain rate and dislocation 
density (i.e. the Orowan equation). However, after dislocations cuttting 
into the γ’ precipitate, dislocations move as leading-trailing pairs in the 
γ’ precipitate, the linear relation between plastic strain rate and dislo -
cation density breaks. From Fig. 4 (b)-(d), it can be seen that there are 
eight active slip systems, as the rest Schmid factors of the rest four slip 
systems are all zero. The activity of dislocations in the slip system varies 
at different channel widths. With channel widths of 60 nm and 100 nm, 
dislocations on slip system 2 are the most active, while not the case with 
channel width of 80 nm. The reason is that with different channel 
widths, the effective driving dislocations are different, and hence the 
motion sequence of dislocation on each slip system and timing that they 
interact with other dislocations are different.
3.2. Effect of precipitate APB energy on elastoplastic deformation
By setting three different γ’ APB energies (62.5 mJ / m
2
, 125 mJ / m
2
, 
Fig. 2. Tensile curves with different with different γ matrix channel widths: (a) Stress – strain; (b) Hardening rate-strain.
Fig. 3. 3D microstructures at plastic strain 0.2 % with different γ matrix channel widths: (a) 60 nm; (b) 80 nm; (c) 100 nm.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
4

## Page 5

and 250 mJ / m
2
), the effect of γ’ APB energy on elastoplastic deforma -
tion is studied. The γ matrix channel width, γ’ precipitate volume frac -
tion and γ / γ’ misfit are fixed to 80 nm, 67.5 % and 0.003, respectively. 
The stress – strain curves and hardening rate-strain curves are shown in 
Fig. 5 . The corresponding 3D microstructures at total stain of 0.1 %, 1 % 
and 2.5 % are shown in Fig. 6 , Fig. 7 and Fig. 8 , respectively. As can be 
seen in Fig. 5 (a), the stresses in the elastic stage increase with total 
strain linearly up to 0.5 %, regardless of the γ’ APB energy. Fig. 6 shows 
that dislocations slightly bow out in the γ matrix during this stage, the 
effective stress is not big enough to overcome the maximum line tension 
stress (or the minimum curvature) and Peierls-Nabarro stress. However, 
it is interesting to note that from DDD point of view, there are also slight 
dislocation activities take place in the elastic deformation, which is in 
contradictory to traditional macroscopic knowledge on elasticity and 
plasticity. After total strain about 0.6 %, the stresses with APB energies 
of 125 mJ / m
2 
and 250 mJ / m
2 
increase nonlinearly without distinction 
up to about 1.5 %, but the stress – strain curve with APB energy of 62.5 
mJ / m
2 
soon enters a plateau. This can also be evidently seen from the 
hardening rate curves in Fig. 5 (b). The reason is that massive disloca -
tions have cut into the γ’ precipitate with the lowest APB energy, which 
is not the case with higher APB energies, as shown in Fig. 7 , where the 
3D microstructures at total strain of 1 % are plotted. As the plastic 
deformation goes on, the stress – strain curves with APB energies of 125 
Fig. 4. Evolution of dislocation density: (a) total dislocation density; (b)-(c) dislocation density on each slip system with different γ matrix channel widths: (b) 60 nm; 
(b) 80 nm; (c) 100 nm.
Fig. 5. Tensile curves with different with different APB energies: (a) Stress – strain; (b) Hardening rate-strain.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
5

## Page 6

mJ / m
2 
and 250 mJ / m
2 
bifurcate after total strain of 1.5 %. The reason is 
that as more dislocations pile up at the γ / γ’ interfaces, the pushing stress 
exerted on the leading dislocation is big enough to overcome the me -
dium APB stress (125 mJ / m
2
) resistance for cutting into the γ’ precip -
itate, but still not enough to overcome the biggest APB stress (250 
mJ / m
2
) despite that the dislocation networks at the γ / γ’ interfaces are 
very dense already, as shown in Fig. 8 . It is fairly to state that γ’ APB 
energy is a significant strengthening mechanism which makes notable 
change to the plastic deformation of single crystal superalloys.
Fig. 9 (a) shows the evolution of total dislocation density and the 
dislocation density cutting into γ’ precipitate, which again confirms the 
that total dislocation density increases linearly with plastic strain before 
dislocations cutting into the γ’ precipitate. After dislocations cutting into 
the γ’ precipitate, the multiplication of dislocations dramatically slows 
down as now dislocations in the γ’ precipitate move as relatively fixed 
leading-trailing pairs. The evolution of dislocation density on each slip 
system with different γ’ APB energies is shown in Fig. 9 (b)-(d). The most 
active slip systems with different γ’ APB energies are different. With the 
smallest and biggest APB energies, the dislocation multiplications are 
mainly focused on the third slip system (S03) and the second slip system 
(S02), respectively. However, the contribution of slip systems is much 
more uniform in the case with medium APB energy. It is a natural result 
of interactions between dislocations and the r ’ precipitate, as well as 
mutual interactions between dislocations. It is difficult to obtain a more 
detailed explanation on it, as once the motion sequence of one of hun -
dreds of dislocation segments changes, the result changes 
Fig. 6. 3D microstructures at total strain 0.1 % with different γ’ APB energies: (a) 62.5 mJ/m2; (b) 125 mJ/m2; (c) 250 mJ/m2.
Fig. 7. 3D microstructures at total strain 1 % with different γ’ APB energies: (a) 62.5 mJ / m
2
; (b) 125 mJ / m
2
; (c) 250 mJ / m
2
.
Fig. 8. 3D microstructures at total strain 2.5 % with different γ’ APB energies: (a) 62.5 mJ / m
2
; (b) 125 mJ / m
2
; (c) 250 mJ / m
2
.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
6

## Page 7

consequentially. Let alone the complicated result as a chaos assemble of 
hundreds of dislocation segments.
3.3. Effect of precipitate volume fraction on elastoplastic deformation
By setting three different γ’ precipitate volume fraction (55.5 %, 
67.5 % and 74.3 %), its effect on elastoplastic deformation is studied. 
The γ matrix channel width, γ’ APB energy and γ / γ’ interface misfit are 
fixed to 80 nm, 125 mJ / m
2 
and 0.003, respectively. To achieve 
different γ’ precipitate volume fractions while keeping channel width 
the same, the size of γ’ precipitate and simulation domain are different 
for the three cases. The simulation domain are 350 nm × 370 nm × 390 
nm, 550 nm × 570 nm × 590 nm and 750 nm × 770 nm × 790 nm for 
the three cases, as shown in Fig. 11 . Hence, the present effect of γ’ 
precipitate volume fraction can be also regarded as the effect of γ’ size. 
The stress – strain curves and hardening rate-strain curves are shown in 
Fig. 9. Evolution of dislocation density: (a) total dislocation density; (b)-(c) dislocation density on each slip system with different γ’ APB energies: (b) 62.5 mJ/m2; 
(c) 125 mJ/m2; (d) 250 mJ/m2.
Fig. 10. Tensile curves with different with different γ’ precipitate volume fractions: (a) Stress – strain; (b) Hardening rate-strain.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
7

## Page 8

Fig. 10 and the corresponding 3D microstructures at plastic stain of 0.6 
% is shown in Fig. 11 . As can be seen, like the stress – strain curves under 
other microstructure characteristics, the stresses exhibit linear- 
nonlinear combined increment as the deformation goes on. At the 
same total strain, the stress is bigger with higher γ’ precipitate volume 
fraction. As the γ matrix channel width is the same, the stronger hard -
ening of higher γ’ precipitate volume fraction is not from the line tension 
resistance caused by the curvature of dislocation. It is more likely from 
the longer path that dislocations loop over a bigger γ’ precipitate size (or 
higher γ’ precipitate volume fraction). It can be seen from the 3D mi -
crostructures that the dislocation networks piling up at the γ / γ’ in -
terfaces are denser with higher γ’ precipitate volume fraction due to the 
bigger loading stress. However, when taking a look at the evolution of 
dislocation density in Fig. 12 , the dislocation density is lower for higher 
γ’ precipitate volume fraction at 0.6 % plastic strain, which is counter -
intuitive to the intuition of 3D microstructures in Fig. 11 . The reason is 
that the total dislocation density is calculated by ρ = l V, where l is the 
total length of dislocation segments and V is the simulation domain size. 
The total length of dislocation segments is indeed longer with higher γ’ 
precipitate volume fraction, but at the same time, the domain size is also 
bigger with higher γ’ precipitate volume fraction. The interesting phe -
nomenon that total dislocation density increases linearly with plastic 
strain before dislocations cutting into the γ’ precipitate and dramatically 
slows down after that, still holds. Another interesting phenomenon is 
that unlike the cases with different matrix channel widths and APB en -
ergies in which a few active slip systems dominate over other slip sys -
tems, the plastic contribution from different active slip systems is much 
more uniform in the present case.
3.4. Effect of matrix/precipitate interface misfit on elastoplastic 
deformation
By setting three different γ / γ’ interface misfits (0.0, 0.003, and 
 0.006), its effect on elastoplastic deformation is studied. The γ matrix 
channel width, γ’ APB energy and γ’ precipitate volume fraction are 
fixed to 80 nm, 125 mJ / m
2 
and 67.5 %, respectively. The stress – strain 
curves and hardening rate-strain curves are shown in Fig. 13 . Unlike the 
distinct stress – strain curves with different γ matrix channel widths, γ’ 
precipitate APB energies and γ’ precipitate volume fractions, the 
stress – strain curves with different γ / γ’ interface misfits are not distin -
guishable during the whole elastoplastic deformation stage. The 
resolved shear stress (RSS) fields on the first slip system (S01) induced 
by γ / γ’ interface misfits of 0.003 and 0.006 without external loading 
are plotted in Fig. 14 . It can be seen that the distribution of RSS is similar 
with different γ / γ’ interface misfits, while bigger magnitude of γ / γ’ 
interface misfit leads to bigger magnitude of RSS. The RSS on the x-y 
plane channel and the z-y plane channel are mostly affected by γ / γ’ 
interface misfit, but with the opposite sign. The RSS on the x-z plane 
channel is almost unaffected by γ / γ’ interface misfit.
To further understand the indiscrimination, the corresponding 3D 
microstructures viewing from different axes are shown in Figs. 15 – 17 . It 
can be observed that on the x-y plane, the density of dislocations in -
creases as the magnitude of γ / γ’ interface misfits increases. In contrast, 
on the y-z and x-z planes, the density of dislocations decreases as the 
magnitude of γ / γ’ interface misfits increases. The inhomogeneity of 
dislocation density distribution on different channels comprehensively 
leads to homogeneous and uniform dislocation density distribution 
overall regardless of the γ / γ’ interface misfit, as shown in Fig. 18 , which 
is a natural result of the RRS distribution. The same evolution of dislo -
cation density hence leads to the same stress – strain response.
The elastoplastic deformations of two-phase superalloys under 
different strain rate regimes are very different. Experiments and con -
tinuum scale simulations mainly focus on normal strain rate ( < 10
1 
s
 1
) 
deformation [14,15,17] , atomistic simulations mainly focus on ultra- 
high strain rate ( > 10
6 
s
 1
) deformation due to their small temporal- 
spacial limit [37 – 39] , while the present work studies the strain rate 
(2 × 10
3 
s
 1
) in-between. The normal strain rate regime includes the 
typical creep and fatigue strain rate ( < 10
-3 
s
 1
) under which the turbine 
disc and blade operate at service. The maximum applied stress of creep 
and fatigue is typically below the macroscopic yield point, hence most of 
the time, dislocations are blocked by the γ’ precipitates and pile up at the 
γ / γ’ interfaces. Stacking faults are not formed until the very late stage 
that the leading dislocation of pile-up dislocation structure possesses 
enough stress from the following dislocations to cut into the γ’ pre -
cipitates as dislocation pairs. In contrast, during the ultra-high strain 
rate deformation, the stress – strain curve rapidly increases to a ultra-high 
yield point, followed by a sharp drop right after the yield point, and 
massive stacking faults with partial dislocations form abruptly. The 
stress – strain curves in the present work do not have sharp drop right 
after the yield point, the waiting time that dislocations cut into the γ’ 
precipitates is much longer than that under normal strain rate while 
much shorter than that under ultra-high strain rate. Neverthless, there 
are common inspirations can be summarized for the design of more 
advanced superalloys for turbine components, regardless of the strain 
rate. It has been widely confirmed that the excellent high temperature 
strength of superalloys mainly comes from the big APB energy combined 
with high volume fraction of the γ’ precipitates. Specifically, the big APB 
energy prevents dislocations cutting into the γ’ precipitates, which 
forces dislocation to move in the γ matrix. Simultaneously, the high 
volume fraction of γ’ precipitates yields narrow γ matrix channels, 
which further leads to big line tension resistance stress for dislocations 
to move in the γ matrix. So, it is always beneficial to have bigger APB 
energy by adding some rare earth elements. It is also beneficial to in -
crease the volume fraction of γ’ precipitates up to a critical point, but not 
always the higher the better. If the γ matrix channels are too close 
together due to a very high volume fraction, dislocation interactions can 
Fig. 11. 3D microstructures with different γ’ precipitate volume fractions at plastic strain 0.6%: (a) 55.5%; (b) 67.5%; (c) 74.3%.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
8

## Page 9

lead to more severe localized stresses and strain localization, which 
could lead to eariler dislocation cutting of γ’ precipitates and crack 
initiation. So, the key point of strengthing for superalloys is to enhance 
the resistance of dislocation motion by controling the γ’ APB energy, γ’ 
volume fraction or γ channel width, up to a point that would not trigger 
eariler dislocation cutting of γ’ precipitates and crack initiation.
In the end, we would like to address some remarks on why the 
dislocation climb and cross-slip are not considered, as well as the 
terminology “ high strain rate ” in the present work. Generally, it is good 
to have more comprehensive mechanisms including dislocation climb 
and cross-slip in the DDD framework. However, it might be more 
physical to have dislocation glide only in the present case of single 
crystal Ni-based superalloys. Regarding dislocation climb, it takes places 
at a time scale three-order of magnitude bigger than dislocation glide, 
which is reflected by the drag coefficient of mobility law that its value is 
three-order of magnitude bigger for glide than for climb [40,41] . As 
Fig. 12. Evolution of dislocation density: (a) total dislocation density; (b)-(c) dislocation density on each slip system with different γ’ precipiatate volume fractions: 
(b) 55.5%; (c) 67.5%; (d) 74.3%.
Fig. 13. Tensile curves with different with different γ / γ’ interface misfits: (a) Stress – strain; (b) Hardening rate-strain.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
9

## Page 10

dislocation climb is a vacancy associated process and vacancy evolution 
is diffusion controlled. The present work is considered on time scales 
where diffusion (dislocation climb and coarsening of γ’ ) makes no 
appreciable contribution to microstructure evolution. Regarding dislo -
cation cross-slip, as its onset is triggered by a phenomenological coef -
ficient in the equation of cross-slip in dislocation dynamics, the resulting 
stress – strain curves sensitively depend on the tuning of the phenome -
nological coefficient [42] . We have not found a reliable way to bench -
mark the phenomenological coefficient, so we determined to turn off the 
cross-slip. However, we think it would be beneficial to incorporate 
dislocation climb if the evolution of vacancy and γ’ precipitates are 
considered by a multi-time-scale scheme in future work.
The terminology “ high strain rate ” in the present work is a concept 
on reference to the absolute strain rate value commonly used in the 
plasticity community. More specifically, the strain rates < 10
1 
s
 1 
typically conducted in experiments and continuum scale simulations are 
regarded as “ normal strain rates ” , while strain rates > 10
6 
s
 1 
typically 
conducted in atomistic simulations are regarded as “ ultra-high strain 
rates ” . However, a much more physical strain rate-dislocation density 
conjugated definition has been proposed recently [43] , in which the 
“ high ” or “ low ” strain rate is defined by yielding physics associated with 
dislocation density. The strain rate-dislocation density combination in 
the present work is indeed in an “ intermediate ” regime between the 
“ high ” and “ low ” regimes according to the recent physical definition 
Fig. 14. The distribution of shear stress field on slip systems under different γ / γ’ interface misfits: (a) 0.003; (b) 0.006.
Fig. 15. 3D microstructures at plastic strain 0.2% viewing along z direction (i.e. the x-y plane), with different γ / γ’ interface misfits: (a) 0.0; (b) 0.003; (c) 0.006.
Fig. 16. 3D microstructures at plastic strain 0.2 % viewing along x direction (i.e. the y-z plane), with different γ / γ’ interface misfits: (a) 0.0; (b) 0.003; (c) 0.006.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
10

## Page 11

[43] .
4. Conclusions
By developing 3D DDD with continuum description of static two- 
phase microstructure, the effect of matrix channel, precipitate APB en -
ergy, precipitate volume fraction, matrix/precipitate interface misfit on 
the elastoplastic deformation of γ / γ’ two-phase single crystal superal -
loys are studied. The main conclusions are as follows. 
1. Unlike the traditional macroscopic perception that there is no 
dislocation activity in the elastic deformation stage, DDD simulations 
show that there is slight dislocation bowing out while the stress – -
strain curve is still linear in the elastic deformation stage, regardless 
of the two-phase microstructure characteristics.
2. Dislocations multiply in the γ matrix channels at the early stage of 
plastic deformation and pile up at γ / γ’ interfaces due to the resis -
tance of γ’ APB energy. Dislocations cut into the γ’ precipitate when 
the push stress excreted on the leading dislocation of pile-up struc -
ture is big enough to overcome the γ’ APB stress, regardless of the 
two-phase microstructure characteristics.
3. Total dislocation density increases linearly with plastic strain before 
dislocations cutting into the γ’ precipitate and dramatically slows 
down after that, since dislocations in the γ’ precipitate move as 
relatively fixed leading-trailing pairs afterwards, regardless of the 
two-phase microstructure characteristics.
4. Smaller γ matrix channel width leads to stronger hardening and 
increased dislocation density, as more during stress is needed for 
overcome stronger line tension resistance caused by smaller γ matrix 
channel width.
Fig. 17. 3D microstructures at plastic strain 0.2% viewing along y direction (i.e. the x-z plane), with different γ / γ’ interface misfits: (a) 0.0; (b) 0.003; (c) 0.006.
Fig. 18. Evolution of dislocation density: (a) total dislocation density; (b)-(c) dislocation density on each slip system with different γ / γ’ interface misfits: (b) 0; (c) 
 0.003; (d) 0.006.
R. Wu et al. Computational Materials Science 250 (2025) 113736 
11

## Page 12

5. Bigger γ’ APB energy leads to stronger hardening and later cutting 
through of the γ’ precipitate by dislocations, as more pilling up dis -
locations are needed on the γ/γ’ interfaces to provide enough push 
stress to the leading dislocation for cutting into the γ’ precipitate.
6. Higher γ’ precipitate volume fraction leads to stronger hardening, as 
longer path is required for dislocations to loop over bigger γ’ pre -
cipitate size.
7. The γ/γ’ interface misfit leads to inhomogeneous resolved shear 
stress and hence dislocation activity in different γ matrix channels, 
but such an inhomogeneity comprehensively leads to overall ho -
mogeneous dislocation activity and hence the same stress–strain 
response. Therefore, the γ/γ’ interface misfit has trivial effect on the 
elastoplastic deformation.
CRediT authorship contribution statement
Ronghai Wu: Writing – review & editing, Writing – original draft, 
Supervision, Investigation, Conceptualization. Zheng Wang: Visuali -
zation, Methodology, Data curation. Xiaoxiang Wu: Supervision. Heng 
Li: Writing – review & editing, Supervision.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgements
Financial support from the High-tech Research and Development 
Center of the Ministry of Science and Technology of China (No. 
2022YFB3705402), Guangdong Basic and Applied Basic Research 
Foundation (No. 2024A1515010578) and National Natural Science 
Foundation of China (No. 12272299). We thank Prof. Dr. Marc Fivel and 
Prof. Dr. Alexander Hartmaier for providing the basic TRIDIS codes. We 
also thank Dr. Siwen Gao for technical support on TRIDIS codes.
Data availability
Data will be made available on request.
References
[1] M. Liu, Q. Zheng, X. Wang, C. Xu, Mech. Mater. 164 (2022) .
[2] S. Zhou, M. Hu, C. Li, Q. Guo, L. Yu, H. Ding, Y. Liu, Mater. Sci. Eng. A 855 (2022) .
[3] L. Luo, Y. Ru, Y. Ma, S. Li, S. Gong, Mater. Sci. Eng. A 832 (2022) .
[4] G. Gudivada, A.K. Pandey, J. Alloy. Compd. 963 (2023) .
[5] T.M. Pollock, S. Tin, J. Propul. Power 22 (2006) 361–374 .
[6] P. Qu, W. Yang, J. Qin, C. Liu, X. Duan, J. Zhang, L. Liu, Intermetallics 162 (2023) .
[7] A.R. Khoei, M. Youzi, G.T. Eshlaghi, Mech. Mater. 171 (2022) .
[8] Z. Zhou, L. Liu, P. Lv, J. Zhang, J. Alloy. Compd. 960 (2023) .
[9] Y. Li, X. Wang, Z. Tan, J. Liu, J. Liu, J. Li, Y. Zhou, X. Sun, Intermetallics 148 
(2022) .
[10] Y. Xingfu, T. Sugui, W. Minggang, Z. Shu, L. Xudong, C. Shusen, Mater. Sci. Eng. A 
499 (2009) 352–359 .
[11] T. Murakumo, T. Kobayashi, Y. Koizumi, H. Harada, Acta Mater. 52 (2004) 
3737–3744 .
[12] V. Sass, M. Feller-Kniepmeier, Mater. Sci. Eng. A 245 (1998) 19–28 .
[13] V. Sass, U. Glatzel, M. Feller-Kniepmeier, Acta Mater. 44 (1996) 1967–1977 .
[14] R. Wu, M. Zaiser, S. Sandfeld, Int. J. Plast 95 (2017) 142–162 .
[15] R. Wu, Z. Yue, M. Wang, J. Alloy. Compd. 779 (2019) 326–334 .
[16] S. Shi, Y. Li, Z. Yan, S. Yang, Y. Ju, Int. J. Mech. Sci. 227 (2022) .
[17] R. Wu, Y. Zhang, Int. J. Plast 157 (2022) .
[18] J.-B. le Graverend, Int. J. Mech. Sci. 239 (2023) .
[19] S. Chaudhary, P.J. Guruprasad, A. Patra, Mech. Mater. 174 (2022) .
[20] K.-P. Gradwohl, W. Miller, N. Dropka, R.R. Sumathi, Comput. Mater. Sci 211 
(2022) .
[21] K. Chen, L. Zhan, Z. Ma, Y. Xu, T. Gao, S. Lao, Comput. Mater. Sci 240 (2024) .
[22] S. Gao, M. Fivel, A. Ma, A. Hartmaier, J. Mech. Phys. Solids 76 (2015) 276–290 .
[23] K. Yashiro, F. Kurose, Y. Nakashima, K. Kubo, Y. Tomita, H.M. Zbib, Int. J. Plast 22 
(2006) 713–723 .
[24] M. Huang, L. Zhao, J. Tong, Int. J. Plast 28 (2012) 141–158 .
[25] M. Huang, Z. Li, J. Mech. Phys. Solids 61 (2013) 2454–2472 .
[26] H. Yang, Z. Li, M. Huang, Comput. Mater. Sci 75 (2013) 52–59 .
[27] S. Huang, M. Huang, Z. Li, Int. J. Plast 110 (2018) 1–18 .
[28] S. Huang, M. Huang, Model. Simul. Mater. Sci. Eng. 29 (2021) .
[29] S.M. Hafez Haghighat, G. Eggeler, D. Raabe, Acta Mater. 61 (2013) 3709–3723 .
[30] F. Ram, Z. Li, S. Zaefferer, S.H. Haghighat, R.C. Reed, Acta Mater. 109 (2016) 
151–161 .
[31] S. Lu, N. Ao, Q. Kan, S.-C. Wu, G. Kang, X. Zhang, Int. J. Mech. Sci. (2023) .
[32] X. Zhang, J. Zhao, G. Kang, M. Zaiser, Int. J. Plast (2023) .
[33] M.C. Fivel, G.R. Canova, Model. Simul. Mater. Sci. Eng. 7 (1999) 753 .
[34] M. Peach, J.S. Koehler, Phys. Rev. 80 (1950) 436–439 .
[35] R.D. Wit, Phys. Status Solidi 20 (1967) 567–573 .
[36] J.E.A. Foreman, Phil. Mag. 15 (1967) 1011–1021 .
[37] R. Wu, Q. Yin, J. Wang, Q. Mao, X. Zhang, Z. Wen, J. Alloy. Compd. 862 (2021) .
[38] R. Wu, Y. Zhao, Q. Yin, J. Wang, X. Ai, Z. Wen, J. Alloy. Compd. 855 (2021) .
[39] Q. Yin, R. Wu, J. Wang, S. Chen, Y. Lian, Z. Wen, Mech. Mater. 160 (2021) .
[40] D. Mordehai, E. Clouet, M. Fivel, M. Verdier, Phil. Mag. 88 (2008) 899–925 .
[41] F. Liu, Z.L. Liu, P. Lin, Z. Zhuang, Int. J. Plast 92 (2017) 2–18 .
[42] A. Malka-Markovitz, D. Mordehai, Phil. Mag. (2019) 1–21 .
[43] H. Fan, Q. Wang, J.A. El-Awady, D. Raabe, M. Zaiser, Nat Commun 12 (2021) 
1845 .
R. Wu et al. Computational Materials Science 250 (2025) 113736 
12
