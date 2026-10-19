# 1-s2.0-S2238785424019069-main

<!-- source: D:\总文献\1-s2.0-S2238785424019069-main.pdf -->
<!-- file_sha256: 305bde2a7d8e2bf0f41a88993a251eba4c60733dc0e87f49210794d3cb87c5fd -->

## Page 1

Journal of Materials Research and Technology 32 (2024) 2830–2842
Available online 22 August 2024
2238-7854/© 2024 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/).
Liberalizing the effects of Al and Cr in coatings for enhanced interface 
stability with Mo-rich Ni
3
Al-based superalloys
Lilun Geng
a , e
, Wenyue Zhao
a , *
, Yi Ru
a , b , d
, Mingzhe Li
c
, Fan Yang
a
, Yunpeng Hu
a
, Boxuan 
Du
a
, Yang Cao
a
, Yanling Pei
a
, Shusuo Li
a , c , d
, Shengkai Gong
a , b , d , *
a
School of Materials Science and Engineering, Beihang University, Beijing, 100191, China
b
Tianmushan Laboratory, Hangzhou, Zhejiang Province, 311115, China
c
Research Institute of Aero-Engine, Beihang University, Beijing, 100191, China
d
AECC Guizhou Liyang Aviation Power Company Limited, Guizhou, 550014, China
e
Institute of engineering thermophysics, Chinese Academy of Sciences, Beijing, 100190, China
ARTICLE INFO
Keywords:
Metal coatings
Superalloy
Interface
Thermodynamic diagrams
Phase field
ABSTRACT
The interfacial behaviors between protective coatings and substrate single-crystal superalloys significantly 
impact their service performances. This work focuses on the elements interdiffusion and microstructural evo -
lution at the interface between a NiCrAlY coating and a series of high-Mo Ni
3
Al-based single-crystal superalloys, 
through the coupled phase-field simulations and DICTRA kinetics calculations of their model systems. The 
critical roles of Al and Cr played in the microstructural evolution at coating/superalloy interface have been 
confirmed, which requires the appropriate content decreases of Al and Cr in the coating at 1100 
◦
C. However, the 
addition of Mo reduces the driving force of element diffusion from coating to substrate by increasing the ac -
tivities of Al and Cr in superalloy. Moreover, increasing the Mo content in superalloy from 8 wt% to 10 wt% 
could also counteract the promoting effect of Al on Ni mobility and mitigate the γ ′ coarsening and detrimental 
TCP precipitation. Therefore, the effects of Mo enable the reasonable increase of Al content in coating to better 
balance the interfacial stability and oxidation resistance of coated superalloy, besides its advantage in reducing 
the anisotropy of TCP precipitate. The obtained interfacial evolution mechanisms resulting from the phase 
transformation thermodynamics and element interdiffusion kinetics are expected to aid the coating design for 
advanced single-crystal superalloys servicing at ultra-high temperature.
1. Introduction
It is difficult to balance high-temperature mechanical properties and 
oxidation/corrosion resistance as the inlet temperature of advanced gas 
turbine engines increasing. Protective coatings are required for single- 
crystal (SX) superalloys in service above 1100 
◦
C [ 1 , 2 ]. MCrAlY (M =
Ni, Co, Ni and Co) and aluminide coatings are frequently used as bond 
coatings and thermal barrier coatings. However, there are significant 
differences in the chemical composition, phase constitution and micro -
structure between superalloys and coatings. Therefore, element inter -
diffusion often occurs inevitably at the interface between coatings and 
superalloys, driven by the chemical potential gradient, temperature 
gradient and stress gradient during service. An interdiffusion zone (IDZ) 
beneath the coating/superalloys interface usually forms as a result [ 3 , 4 ]. 
In addition, secondary reaction zones (SRZ) may also form at the 
interface near superalloy under high-temperature diffusion or 
thermal-mechanical coupling conditions [ 5 , 6 ]. The lower solubilities of 
refractory elements Mo, Re and W in γ ′ phases lead to the precipitation of 
the Topologically Close Packed (TCP) phases. The near surface γ - γ ′ 
microstructure of the alloy will also degrade with new phases formed, 
which deteriorates the long-term microstructural stability of superalloy 
and its mechanical properties eventually [ 7 – 10 ]. Further application of 
protective coatings to single crystal superalloys is restricted by the 
microstructure instability of coating/superalloy interface due to the 
intense interdiffusion of various elements.
Superalloys often incorporate numerous refractory elements like W, 
* Corresponding author. Key Laboratory of Aerospace Materials and Performance (Ministry of Education), School of Materials Science and Engineering, Beihang 
University, 37 Xueyuan Rd., Beijing, 100191, China.
** Corresponding author. School of Materials Science and Engineering, Beihang University, Beijing, 100191, China.
E-mail address: wendyzhao56@buaa.edu.cn (W. Zhao). 
Contents lists available at ScienceDirect
Journal of Materials Research and Technology
journal homep age: www.elsevi er.com/loc ate/jmrt
https://doi.org/10.1016/j.jmrt.2024.08.116
Received 18 June 2024; Received in revised form 31 July 2024; Accepted 19 August 2024

## Page 2

Journal of Materials Research and Technology 32 (2024) 2830–2842
2831
Mo, Re to enhance their temperature-bearing capacity. This poses a 
significant challenge to their microstructural stabilities. At the same 
time, the interaction between coatings and superalloys becomes 
increasingly complex as the contents and variety of alloying elements 
increase. The influence zone width of (Ni, Pt)Al coatings is notably 
greater for the third-generation CMSX-10 SX superalloys compared with 
the second-generation one CMSX-4 [ 11 , 12 ]. Similarly, the impacts of 
identical aluminizing coatings on the interface are obviously different 
for the four distinct substrates superalloys: Hastelloy X, DZ411, DZ125, 
and DD6 [ 13 ]. The type of TCP at the coating/superalloy interface is 
related to the superalloy composition. With the same PtAl coating, μ or P 
phases precipitate at the interface near Ren ´e N5 alloy while μ or σ phases 
precipitate for the CMSX-4 case [ 14 ]. As a γ -phase forming element, Mo 
is effective for improve the solid solution strengthening and interfacial 
strengthening of Ni-based SX superalloys. However, Mo is also a stronger 
TCP phase forming element [ 15 ]. The α -Mo, δ -NiMo and P phases are all 
prone to precipitate in Mo-rich superalloys [ 16 ]. Therefore, the appli -
cability of coating for a specific superalloy should be evaluated based on 
its interfacial behavior, due to the complex interdiffusion behavior of 
various alloying elements at different temperatures.
Interfacial microstructure morphology has an important influence on 
the properties of coating/superalloy systems as well. The TCP phases 
with various morphologies affect crack formation differently [ 17 ]. 
Furthermore, the morphology of the precipitated phase can also influ -
ence the diffusion rate of elements [ 18 ]. For example, larger and wider 
μ -phases formed at the interface between the aluminide coating and the 
CMSX-4 alloy, compared with the smaller σ -phases formed at the 
interface between coating and the RR3000 alloy. This results in a longer 
diffusion path for elements and slower growth of the interfacial influ -
ence zone for the CMSX-4 alloy [ 4 ]. Hence, a comprehensive evaluation 
of the microstructural stability of coating/superalloy interface with 
phase morphology is indispensable to better predict the lifetime of the 
material system.
The behavior of the coating/single crystal superalloy interface is 
complex due to the multiple alloying elements and phases. In order to 
accelerate the development and implementation of new protective 
coatings, computational simulation methods are of great values in pre -
dicting the diffusion behavior between coatings and superalloys and 
elucidating the mechanisms behind. The thermodynamic and kinetic 
results calculated by Thermo-Calc software indicate that Ta and W ad -
ditions increased the activities of Al and Cr while reduced Ni activity. 
Consequently, the reduced effective mobilities of Al and Cr elements 
under lower driving forces increase the volume fraction of γ ʹ phase and 
elongated the coating life [ 19 ]. Yuan [ 20 ] found that Al with high ac -
tivity in the superalloy tends to form a β phase layer at the coat -
ing/superalloy interface. In addition to increasing the Al content in 
superalloys, increasing Cr, Ta, Mo and Re elements can also enhance the 
activity of Al. Although the one-dimensional diffusion calculations 
mentioned above can study the elemental diffusion and phase distri -
bution at coating/superalloy interface, it is infeasible for them to 
accurately predict the non-equilibrium microstructure and the 
morphology of phases.
Phase field simulation can obtain the two-dimensional/three- 
dimensional morphology of the microstructure and involve the effect 
of temperature gradient or stress at the same time. Wu [ 21 , 22 ] studied 
interdiffusion microstructures of γ + β and γ + γ ʹ phases in the Ni – Al – Cr 
system. The influence of temperature gradients were investigated in the 
four types of bond coatings/superalloy systems (including β , γ , and γ ʹ 
phases) [ 23 , 24 ]. The results indicate that temperature gradient pro -
motes the depletion of Al concentration in the coatings. However, the 
effect of the magnitude of the temperature gradient on the concentration 
evolution is neglected in the diffusion couples. Li [ 25 ] found that a novel 
uphill diffusion phenomenon of Al was clarified by the change in the 
chemical potential in Ni – Al – Cr diffusion couple. In addition, the for -
mation of the precipitate-free zone (PFZ) due to the temperature 
gradient effects was also discussed. However, the above simulation 
works mainly focus on the forming elements of coatings, i.e., the 
Ni – Al – Cr ternary systems, while less attention is paid to the strength -
ening elements in the substrate superalloys.
Our previous work has designed a series of high-Al, high-Mo, low-Re 
Ni
3
Al-based SX superalloys. Their compositional characteristics promise 
both excellent mechanical properties and a low density compared with 
conventional Ni-based SX superalloys, with Mo as one of the main 
strengthening elements [ 26 – 28 ]. However, this new compositional 
design of superalloys may bring about changes to its interfacial behavior 
with coatings. Therefore, this paper comprehensively studies the 
microstructural evolution between a NiCrAlY coating and a series of 
high-Mo single-crystal superalloys (Ni – 8Al-1.5Cr-1.5Re-3Ta-(0, 8, 10, 
12) Mo (wt.%)) at 1100 
◦
C, by using coupled phase field simulation and 
DICTRA kinetic calculation methods. The range of superalloy composi -
tions is chosen based on the true nominal composition. We pay a close 
attention to the effects of Mo, Al and Cr elements on the interfacial 
behavior, in order to provide a feasible guidance to the coating design 
for advanced single crystal superalloys applied in aero-engines, espe -
cially towards the ones with higher Al and Mo contents.
2. Model and methods
2.1. DICTRA diffusion simulations
A coupled thermodynamic-kinetic approach was used to simulate the 
diffusion in the alloy/coating system based on the “ homogenization ” 
model proposed by Larsson [ 29 ]. The diffusion simulations, thermody -
namic calculations of TCP phase precipitation and phase diagram cal -
culations are carried out using Thermo-Calc/DICTRA software [ 30 ]. The 
Wiener upper bound or more generally termed “ rule of mixtures ” is 
used, assuming diffusion only occurs in the γ (DIS_FCC_A1), γ ′ 
(FCC_L12#2), and β -NiAl (BCC_B2#2) phases. Overall, the γ , γ ′ , β , α , σ 
and P phases are taken into consideration in the present simulation. This 
model has been successfully applied to the microstructural evolution 
simulation in the system of Ni-based alloys and MCrAlY coatings [ 31 ,
32 ]. Thermodynamic and kinetic data are taken from the TCNi10 [ 33 ] 
and MobNi5 [ 34 ] databases, respectively. In this work, we analyze the 
interdiffusion behavior and microstructural evolution near the coat -
ing/superalloy interface, focusing on the influence of Mo on the 
microstructural stability of superalloy.
2.2. Phase field model
(1) Free energy
In the Ni – Al – Cr – Mo quaternary alloy system, we use three compo -
sition fields, c
i
( r , t ) , nine order parameters, η
p
i
( r , t ) , p = 1, 2, 3 with i = Al, 
Cr or Mo, to describe the microstructural evolution. The total free energy 
of the system can be expressed as [ 35 ]: 
F =
∫
v
(
f
 
c
i
, η
p
i
)
+
∑
i , j = Al , Cr , Mo
κ
ij
 
∇ c
i
∇ c
j
)
+ κ
η
∑
i = Al , Cr , Mo
∑
p
 
∇ η
p
i
)
2
+ F
el
)
dV
(1) 
where κ
ij 
and κ
η 
are the gradient energy coefficients related to concen -
tration and order parameter, respectively. F
el 
is the elastic strain energy. 
f
 
c
i
, η
p
i
)
is the Gibbs free energy density, f = g/V
m
, V
m 
is the molar vol -
ume. The Gibbs free energy can be expressed as [ 36 ]: 
g
 
c
Al
, c
Cr
, c
Mo
, η
p
Al
, η
p
Cr
, η
p
Mo
)
= g
dis
( c
Al
, c
Cr
, c
Mo
)
+ g
order
 
c
Al
, c
Cr
, c
Mo
, η
p
Al
, η
p
Cr
, η
p
Mo
)
 g
order
 
c
Al
, c
Cr
, c
Mo
, η
p
Al
= η
p
Cr
= η
p
Mo
= 0
)
(2) 
g
dis
( c
Al
, c
Cr
, c
Mo
) and g
order
 
c
Al
, c
Cr
, c
Mo
, η
p
Al
, η
p
Cr
, η
p
Mo
)
are the Gibbs en -
ergies of the disordered and ordering phases, respectively. Based on the 
L. Geng et al.

## Page 3

Journal of Materials Research and Technology 32 (2024) 2830–2842
2832
substitutional solid solution model, the Gibbs free energy of the disor -
dered phase can be obtained by Ref. [ 37 ]: 
g
dis
( c
i
) =
∑
i
c
i
G
0
i
+ RT
∑
i
c
i
ln c
i
+
∑
i
∑
j > i
c
i
c
j
∑
m
n = 0
n
L
fcc
i , j
 
c
i
 c
j
)
n
+
∑
i
∑
j > i
∑
k > j
c
i
c
j
c
k
L
fcc
i , j , k
(3) 
According to the four sublattice model, the Gibbs free energy of 
ordering phase can be calculated by: 
g
order
 
y
s
i
)
=
∑
i
∑
j
∑
k
∑
l
y
( 1 )
i
y
( 2 )
j
y
( 3 )
k
y
( 4 )
l
Δ G
order
ijkl
+
RT
4
∑
s
∑
i
y
( s )
i
ln
(
y
( s )
i
)
+
∑
s
∑
i
∑
j > i
y
( s )
i
y
( s )
j
∑
1
n = 0
n
L
order
i , j
(
y
( s )
i
 y
( s )
j
)
n
(4) 
where i , j , k and l denote the Al, Cr, Mo, and Ni elements, c
i 
is the mole 
fraction of element i . G
0
i
, 
n
L
fcc
i , j
, L
fcc
i , j , k
, Δ G
order
ijkl
, 
n
L
order
i , j 
are the binary and 
ternary interaction parameters, respectively [ 37 – 40 ].
The gradient energy describes the energy penalty due to the inho -
mogeneous distribution of phase-field variables near interfaces 
expressed as the following: 
f
gra
=
∑
i , j = Al , Cr , Mo
κ
ij
 
∇ c
i
∇ c
j
)
+ κ
η
∑
i = Al , Cr , Mo
∑
p
 
∇ η
p
i
)
2
(5) 
where κ is the gradient energy coefficient and it can be obtained from the 
interfacial energy ( σ ) and interface thickness (2 λ ) according to the 
following relationships. When describing TCP growth, κ
η 
is replaced 
with κ
p
η
, indicating that it is related to orientation p , and the interface 
energy is anisotropic. 
σ =
̅̅̅̅̅̅ ̅
κ ⋅ ω
√
3
̅̅ ̅
2
√ (6) 
2 λ = 2 . 2
̅̅ ̅
2
√
⋅
̅̅̅ ̅
κ
ω
√
(7) 
The elastic strain energy contribution due to lattice misfit between 
the precipitate and the matrix is evaluated by Khachaturyan ’ s micro -
elasticity theory [ 41 ]: 
F
el
=
1
2
C
ijkl
(
ε
ij
 ε
0
ij
)
 
ε
kl
 ε
0
kl
)
(8) 
where C
ijkl 
are elastic constants, ε
0
ij 
is the stress-free transformation strain 
(SFTS) between the precipitate and the matrix. ε
ij 
is the total strain, that 
is solved by the stress balance ∇ ⋅ σ = 0 at each step.
(2) Diffusion-controlled evolution equation
The precipitation is mainly caused by the diffusion with chemical 
potential gradient as the driving force. The diffusion flux is expressed as 
the gradient of the chemical potential [ 42 ]: 
J
i
= M
i
∇ μ
i
( i = Ni , Al , Cr , Mo ) (9) 
where M
i 
is the intrinsic mobility of the element i and M
i
= c
i
β
i
, β
i 
is the 
atomic mobility of element i , and ∇ μ
i 
is the chemical potential gradient. 
Using the Gibbs – Duhem relation 
∑
i
c
i
∇ μ
i
= 0, ∇ μ
i 
can be expressed as 
follows: 
μ
Al
= ( 1 c
Al
)∇ μ
eff
Al
 c
Cr
∇ μ
eff
Cr
 c
Mo
∇ μ
eff
Mo
(10a) 
μ
Cr
= ( 1 c
Cr
)∇ μ
eff
Cr
 c
Al
∇ μ
eff
Al
 c
Mo
∇ μ
eff
Mo
(10b) 
μ
Mo
= ( 1 c
Mo
)∇ μ
eff
Mo
 c
Al
∇ μ
eff
Al
 c
Cr
∇ μ
eff
Cr
(10b) 
μ
Ni
= c
Al
∇ μ
eff
Al
 c
Cr
∇ μ
eff
Cr
 c
Mo
∇ μ
eff
Mo
(10c) 
where μ
eff
Al
= μ
Al
 μ
Ni
, μ
eff
Cr
= μ
Cr
 μ
Ni 
and μ
eff
Mo
= μ
Mo
 μ
Ni 
are the 
effective chemical potentials of Al, Cr and Mo, respectively. According to 
the results of Shewmon [ 43 ], 
∑
i
J
i
= 0, The net diffusion flux of each 
element is given by: 
̃
J = J
i
 c
i
( J
Ni
+ J
Al
+ J
Cr
+ J
Mo
) ( i = Ni , Al , Cr , Mo ) (11) 
Substituting Eqs. 9 and 10 into Eq. (11) provides the interdiffusion 
flux of individual element [ 44 ] as follows: 
̃
J
Al
= 
[
( 1 c
Al
)
2
M
Al
+ c
2
Al
( M
Ni
+ M
Cr
+ M
Mo
)
]
∇ μ
eff
Al
+ [ c
Cr
( 1 c
Al
) M
Al
+ c
Al
( 1 c
Cr
) M
Cr
 c
Al
c
Cr
( M
Ni
+ M
Mo
)]∇ μ
eff
Cr
+ [ c
Mo
( 1 c
Al
) M
Al
+ c
Al
( 1 c
Mo
) M
Mo
 c
Al
c
Mo
( M
Ni
+ M
Cr
)]∇ μ
eff
Mo
(12a) 
̃
J
Cr
= 
[
( 1 c
Cr
)
2
M
Cr
+ c
2
Cr
( M
Ni
+ M
Al
+ M
Mo
)
]
∇ μ
eff
Cr
+ [ c
Al
( 1 c
Cr
) M
Cr
+ c
Cr
( 1 c
Al
) M
Al
 c
Al
c
Cr
( M
Ni
+ M
Mo
)]∇ μ
eff
Al
+ [ c
Mo
( 1 c
Cr
) M
Cr
+ c
Cr
( 1 c
Mo
) M
Mo
 c
Cr
c
Mo
( M
Ni
+ M
Al
)]∇ μ
eff
Mo
(12b) 
̃
J
Mo
= 
[
( 1 c
Mo
)
2
M
Mo
+ c
2
Mo
( M
Ni
+ M
Al
+ M
Cr
)
]
∇ μ
eff
Mo
+ [ c
Al
( 1 c
Mo
) M
Mo
+ c
Mo
( 1 c
Al
) M
Al
 c
Al
c
Mo
( M
Ni
+ M
Cr
)]∇ μ
eff
Al
+ [ c
Cr
( 1 c
Mo
) M
Mo
+ c
Mo
( 1 c
Cr
) M
Cr
 c
Cr
c
Mo
( M
Ni
+ M
Al
)]∇ μ
eff
Cr
(12c) 
Eq. (12) can be re-written as follows: 
̃
J
Al
= M
AlAl
∇ μ
eff
Al
 M
AlCr
∇ μ
eff
Cr
 M
AlMo
∇ μ
eff
Mo
(13a) 
̃
J
Cr
= M
CrAl
∇ μ
eff
Al
 M
CrCr
∇ μ
eff
Cr
 M
CrMo
∇ μ
eff
Mo
(13b) 
̃
J
Mo
= M
MoAl
∇ μ
eff
Al
 M
MoCr
∇ μ
eff
Cr
 M
MoMo
∇ μ
eff
Mo
(13c) 
where M
ij 
is the chemical mobility [ 44 ]: 
M
AlAl
= ( 1 c
Al
)
2
β
Al
c
Al
+ c
2
Al
β
Cr
c
Cr
+ c
2
Al
β
Ni
c
Ni
+ c
2
Al
β
Mo
c
Mo
(14a) 
M
CrCr
= ( 1 c
Cr
)
2
β
Cr
c
Cr
+ c
2
Cr
β
Al
c
Al
+ c
2
Cr
β
Ni
c
Ni
+ c
2
Cr
β
Mo
c
Mo
(14b) 
M
MoMo
= ( 1 c
Mo
)
2
β
Mo
c
Mo
+ c
2
Mo
β
Al
c
Al
+ c
2
Mo
β
Ni
c
Ni
+ c
2
Mo
β
Cr
c
Cr
(14c) 
M
AlCr
= M
CrAl
= c
Cr
( 1 c
Al
) β
Al
c
Al
 c
Al
( 1 c
Cr
) β
Cr
c
Cr
+ c
Al
c
Cr
( β
Ni
c
Ni
+ β
Mo
c
Mo
) (14d) 
M
AlMo
= M
MoAl
= c
Mo
( 1 c
Al
) β
Al
c
Al
 c
Al
( 1 c
Mo
) β
Mo
c
Mo
+ c
Al
c
Mo
( β
Ni
c
Ni
+ β
Cr
c
Cr
) (14e) 
M
CrMo
= M
MoCr
= c
Mo
( 1 c
Cr
) β
Cr
c
Cr
 c
Cr
( 1 c
Mo
) β
Mo
c
Mo
+ c
Cr
c
Mo
( β
Ni
c
Ni
+ β
Al
c
Al
) (14f) 
For simplicity, it is assumed that M
AlCr
= M
CrAl
, M
AlMo
= M
MoAl 
and 
M
CrMo
= M
MoCr
, although they may not be equal in reality for most 
quaternary systems.
The atomic mobility ( β
i
) is expressed by: 
β
i
=
1
RT
exp
(
Δ Q
∗
RT
)
(15) 
R is the gas constant, and T is the absolute temperature. Δ Q
∗
is the 
L. Geng et al.

## Page 4

Journal of Materials Research and Technology 32 (2024) 2830–2842
2833
diffusion activation energy. According to the results of Engstr ¨om and 
Ågren [ 45 ], diffusion activation energy is expressed as: 
Δ Q
∗
= c
Cr
Δ Q
∗ Cr
i
+ c
Al
Δ Q
∗ Al
i
+ c
Ni
Δ Q
∗ Ni
i
+ c
Mo
Δ Q
∗ Mo
i
+ c
Cr
c
Al
0
Δ Q
∗ Cr , Al
i
+ c
Al
c
Mo
0
Δ Q
∗ Al , Mo
i
+ c
Al
c
Ni
0
Δ Q
∗ Al , Ni
i
+ c
Cr
c
Ni
0
Δ Q
∗ Cr , Ni
i
+ c
Cr
c
Mo
0
Δ Q
∗ Cr , Mo
i
+ c
Mo
c
Ni
0
Δ Q
∗ Mo , Ni
i
(16) 
2.3. Numerical method and parameters
The nonlinear Cahn – Hilliard diffusion [ 46 ] and time-dependent 
Ginsburg – Landau equations [ 47 ] are used to govern the evolution pro -
cess of the concentration and order parameter fields, respectively. 
∂ c
i
∂ t
=
∑
i
∇ ⋅
(
M
ij
∇
δ F
δ c
j
)
+ ξ
c
( r , t ) , i = Al , Cr , Mo , j = Al , Cr , Mo , (17) 
∂ η
j
i
∂ t
= M
η
δ F
δ η
j
i
+ ξ
η
i
( r , t ) , i = Al , Cr , Mo , j = 1 , 2 , 3 (18) 
A semi-implicit Fourier spectral method is adopted to solve Eqs. (17) 
and (18) [ 48 ]. 
∂ η
Al
( r , t )
∂ t
= M
η
(
∂ f
∂ η
Al
 2 κ
η
∇
2
η
Al
+
∂ f
el
∂ η
Al
)
+ ξ
η
Al
( r , t ) (20a) 
∂ η
Cr
( r , t )
∂ t
= M
η
(
∂ f
∂ η
Cr
 2 κ
η
∇
2
η
Cr
+
∂ f
el
∂ η
Cr
)
+ ξ
η
Cr
( r , t ) (20b) 
∂ η
Mo
( r , t )
∂ t
= M
η
(
∂ f
∂ η
Mo
 2 κ
η
∇
2
η
Mo
+
∂ f
el
∂ η
Mo
)
+ ξ
Mo
( r , t ) (20c) 
The gradient energy coefficients κ
CrAl
= κ
AlCr
= 6 . 6 × 10
 12
J ⋅ m
 2
, 
κ
AlAl
= κ
CrCr
= κ
MoMo
= 3 . 72 × 10
 9
J ⋅ m
 2
, κ
MoAl
= κ
AlMo
= κ
MoCr
=
κ
CrMo
= 2 . 08 × 10
 13
J ⋅ m
 2
, and κ
η
= 3 . 7 × 10
 16
J ⋅ m
 2
. The thermal 
noise terms ξ ( r , t ) are added to the initial concentrations and LRO pa -
rameters, respectively, which are used to trigger the initial nucleation of 
phases. The numerical simulation in a cell of 512 nm × 512 nm is 
conducted with periodic boundary conditions and grid size l = 0.5 ×
10
 9 
m. The time step is Δ t = 0.005.
3. Results and discussion
3.1. Phase equilibria
The higher Mo content in the new Ni
3
Al-based SX superalloys is the 
key to ensure their desired mechanical properties at high temperature. 
While Mo is likely to attend the microstructural evolution at the inter -
facial zone between coating and superalloy. Therefore, considering the 
compositional characteristics of the coating system (Al, Cr) and the SX 
superalloy (Mo, Al) system, the phase equilibrium of the Ni – Al – Cr – Mo 
quaternary system at 1100 
◦
C is studied first by thermodynamic calcu -
lation ( Fig. 1 ).
∂ c
Al
( r , t )
∂ t
= V
2
m
∇ ⋅
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣
M
AlAl
∇
(
∂ f
∂ c
Al
 2 κ
AlAl
∇
2
c
Al
 2 κ
AlCr
∇
2
c
Cr
 2 κ
AlMo
∇
2
c
Mo
+
∂ f
el
∂ c
Al
)
+ M
AlCr
∇
(
∂ f
∂ c
Cr
 2 κ
CrAl
∇
2
c
Al
 2 κ
CrCr
∇
2
c
Cr
 2 κ
CrMo
∇
2
c
Mo
+
∂ f
el
∂ c
Cr
)
+ M
AlMo
∇
(
∂ f
∂ c
Mo
 2 κ
MoAl
∇
2
c
Al
 2 κ
MoCr
∇
2
c
Cr
 2 κ
MoMo
∇
2
c
Mo
+
∂ f
el
∂ c
Mo
)
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦
+ ξ
c
( r , t ) (19a) 
∂ c
Cr
( r , t )
∂ t
= V
2
m
∇ ⋅
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣
M
CrAl
∇
(
∂ f
∂ c
Al
 2 κ
AlAl
∇
2
c
Al
 2 κ
AlCr
∇
2
c
Cr
 2 κ
AlMo
∇
2
c
Mo
+
∂ f
el
∂ c
Al
)
+ M
CrCr
∇
(
∂ f
∂ c
Cr
 2 κ
CrAl
∇
2
c
Al
 2 κ
CrCr
∇
2
c
Cr
 2 κ
CrMo
∇
2
c
Mo
+
∂ f
el
∂ c
Cr
)
+ M
CrMo
∇
(
∂ f
∂ c
Mo
 2 κ
MoAl
∇
2
c
Al
 2 κ
MoCr
∇
2
c
Cr
 2 κ
MoMo
∇
2
c
Mo
+
∂ f
el
∂ c
Mo
)
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦
+ ξ
c
( r , t ) (19b) 
∂ c
Mo
( r , t )
∂ t
= V
2
m
∇ ⋅
⎡
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣
M
MoAl
∇
(
∂ f
∂ c
Al
 2 κ
AlAl
∇
2
c
Al
 2 κ
AlCr
∇
2
c
Cr
 2 κ
AlMo
∇
2
c
Mo
+
∂ f
el
∂ c
Al
)
+ M
MoCr
∇
(
∂ f
∂ c
Cr
 2 κ
CrAl
∇
2
c
Al
 2 κ
CrCr
∇
2
c
Cr
 2 κ
CrMo
∇
2
c
Mo
+
∂ f
el
∂ c
Cr
)
+ M
MoMo
∇
(
∂ f
∂ c
Mo
 2 κ
MoAl
∇
2
c
Al
 2 κ
MoCr
∇
2
c
Cr
 2 κ
MoMo
∇
2
c
Mo
+
∂ f
el
∂ c
Mo
)
⎤
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦
+ ξ
c
( r , t ) (19c) 
L. Geng et al.

## Page 5

Journal of Materials Research and Technology 32 (2024) 2830–2842
2834
Fig. 1 (a) illustrates the calculated isothermal section of the Ni-rich 
part of the ternary Ni – Cr – Al system at 1100 
◦
C, as a comparison to the 
Ni – Al – Cr – Mo quaternary system. The two-phase γ + γ ′ microstructure is 
a basis for high temperature creep strength of the single-crystal super -
alloys. As indicated in Fig. 1 (b – d), the influence of Mo on the ternary 
Ni – Cr – Al system is illustrated using a calculated Ni – Cr – Al section of the 
quaternary system Ni – Cr – Al-xMo (x = 8, 10, 12 wt%). The addition of 
Mo suppresses the size of the γ region in the Ni – Cr – Al – Mo section and 
enlarges its γ + γ ′ region [ 40 ]. In other words, Mo not only acts as a solid 
solution strengthener in the γ -matrix but also increases the mole fraction 
of γ ′ phase.
The mole fractions of γ ′ phase in the more model alloys containing Re 
and Ta with more realistic compositions are also calculated as a function 
of temperature, and the results are shown in Fig. 2 . The 0Mo SX su -
peralloy is located in the γ + γ ′ region with the calculated γ ′ mole fraction 
of approximately 0.4 at 1100 
◦
C. The γ ′ volume fraction increases 
slightly with a further increase in Mo content [ 49 ]. However, the γ ′ 
phase gradually dissolves as the temperature is elevated. Above 1150 
◦
C, 
the mole fraction of γ ′ phase is larger in 10Mo compared with 12Mo, 
which is due to the precipitation of the P phase in 10Mo dissolving at 
high temperatures. Similar to the results above 1150 
◦
C, the mole 
fraction of γ ′ phase is lower in 12Mo compared with that in 10Mo below 
1100 
◦
C due to the more σ -phase precipitates in 12Mo. Moreover, the 
regions of P, σ and α phases also increase due to their Mo-rich features.
Thermodynamic equilibria of Ni – 8Al-1.5Cr-1.5Re-3.0Ta-xMo model 
alloys are calculated as a function of Mo content to further analyze the 
precipitation behavior of the TCP phase at different temperature. The 
calculated temperatures ranged from 600 
◦
C to 1300 
◦
C. As shown in 
Fig. 3 , the addition of 8 wt% Mo to the superalloy may precipitate small 
amounts of σ and R phases below 1100 
◦
C. The σ phase still precipitates 
with 10 wt% and 12 wt% Mo. The P phase begins to appear at about 
980 
◦
C. Furthermore, the increasing addition of Mo to the alloy leads to 
increases in the contents and precipitation temperature ranges of σ and P 
phases. Above 1200 
◦
C, no Mo-rich precipitate forms based on ther -
modynamics calculations. It has been shown that when the oxidation 
temperature is below 900 
◦
C, the precipitated TCP phase is metastable 
with relatively low volume fraction [ 50 ]. The formed TCP phases have 
larger spatial distribution densities and sizes when the oxidation tem -
perature is elevated to 1100 
◦
C [ 51 , 52 ]. However, when the temperature 
is higher than 1200 
◦
C, the solubility of refractory elements increases 
with decreasing γ ′ phase volume fraction, making the TCP phase hard to 
precipitate from matrix [ 53 ]. The TCP precipitation behavior varied 
Fig. 1. Calculated isothermal sections at 1100 
◦
C (using database TCNI10, Thermo-Calc) (a) Ni – Al – Cr; (b) Ni – Al – Cr – 8Mo; (c) Ni – Al – Cr – 10Mo; (d) Ni – Al – Cr – 12Mo 
systems (wt.%).
L. Geng et al.

## Page 6

Journal of Materials Research and Technology 32 (2024) 2830–2842
2835
with temperature obtained in this work is basically consistent with those 
mentioned above. While the excessive addition of Mo content increases 
the possibility of TCP phase formation, which deteriorates the long-term 
microstructural stability of superalloy.
3.2. Interdiffusion behavior at coating/superalloy interface
In order to clarify the coating/superalloy interfacial behavior, 
further kinetic simulations are carried out in the systems with varied 
substrate compositions Ni – 8Al-1.5Cr-1.5Re-3Ta – Mo (8, 10, 12 wt%) but 
a fixed coating composition (Ni – 10Al – 20Cr). The distributions of 
precipitated phases and main elements in these systems after oxidization 
at 1100 
◦
C for 100 h are shown in Fig. 4 (a) - (c) and Fig. 4 (d) – (f) 
respectively. The internal diffusion of Al and Cr from coating to sub -
strate leads to the transformation of the phase constitution in coating 
from the initial γ + β phase to the γ + γ ′ phase. It can be seen that Mo-rich 
phases with different structures may precipitate at different depths from 
the coating surface in the normal direction of the coating/superalloy 
interface, controlled by the elemental concentration gradient [ 54 ]. With 
the increase of Mo content, more TCP phases precipitate at the coat -
ing/superalloy interface in a wider region. Their phase structures 
simultaneously change from σ phase to P and α phase. The kinetic 
simulation results reveal the presence of α phase, which is absent in 
previous thermodynamic calculations. This is probably due to the Al 
aggregation at the interface with approximately 8.6 wt% of content 
( Fig. 4 (d) ), which is higher than the 8 wt% Al content used in the 
thermodynamic calculations. Although the initial Mo contents in the 
superalloys are different, the content of Mo content reaching the coating 
surface after oxidation is similar. This suggests that higher Mo addition 
in superalloys results in a larger gradient of Mo from superalloy to 
coating. This also affect the distributions of the Al and Cr elements, 
particularly increases the Al content at the coating surface ( Fig. 4 (d) ). 
Furthermore, surface oxidation can also affect the content of Al and Cr 
Fig. 2. Calculated mole fractions of γ ′ -phase in studied Ni – 8Al-1.5Cr-1.5Re- 
3.0Ta-xMo (x = 0, 8, 10, 12 wt%) model alloys as a function of temperature.
Fig. 3. Equilibrium phase diagrams of the Ni – 8Al-1.5Cr-1.5Re-3.0Ta-xMo model alloys: (a) x = 8 wt%; (b) x = 10 wt%; (c) x = 12 wt%.
L. Geng et al.

## Page 7

Journal of Materials Research and Technology 32 (2024) 2830–2842
2836
Fig. 4. Influences of Mo content on the distributions of phase and elements in coating/superalloy systems after exposure at 1100 
◦
C for 100 h: (a) γ / γ ′ phase; (b) P 
phase; (c) σ / α phase; (d) Al; (e) Cr; (f) Mo.
Fig. 5. Effect of Mo concentration on the chemical activities in superalloys at 1100 
◦
C: 
(a) Al; (b) Cr.
Table 1 
Calculated mobilities of elements in single phases at 1100 
◦
C (database MOBNi5, Thermo-Calc). The values are normalized to respective mobilities in base Ni – 8Al- 
1.5Cr-1.5Re-3Ta – 8Mo alloy S
0 
(wt.%).
Al Cr Ni Mo Re Ta
γ γ ′ γ γ ′ γ γ ′ γ γ ′ γ γ ′ γ γ ′
S
0 
( + 5Cr) 1.35 1.19 1.44 1.20 1.87 0.98 1.04 1.33 0.99 1.01 1.01 0.99
S
0 
( + 5Al) 1.50 1.12 1.79 1.16 5.31 1.89 1.05 1.07 0.97 0.93 1.01 0.75
L. Geng et al.

## Page 8

Journal of Materials Research and Technology 32 (2024) 2830–2842
2837
elements in the coating due to the Al is consumed by oxidation, which 
will be our subsequent research in the near future.
In order to elucidate the effect of diffusion driving force on micro -
structural evolution at interface, the variation of Al and Cr chemical 
activities with Mo content in the superalloy is calculated. The addition of 
Mo increases the Al activity as shown in Fig. 5 . The addition of Mo in -
creases the segregation of Al in γ ′ phase [ 55 , 56 ]. Moreover, more Mo 
addition also increases the volume fraction of γ ′ in superalloy [ 56 ]. 
Therefore, the Al activity in superalloy is increased by Mo via its com -
bined effects on Al solubilities and fractions of γ - γ ′ phases. In terms of the 
changing rates of Al and Cr activities, the effect of increasing Mo content 
on Cr activity is weaker than that of Al. The higher activities of Al and Cr 
as well as the lower Ni activity in the superalloy reduce their activity 
gradients between the coating and superalloy [ 57 ].
In order to clarify the effect of Al and Cr diffusion from coating to the 
superalloys, the mobilities of elements in single phases ( γ , γ ′ ) at 1100 
◦
C 
and corresponding effective mobilities for the model alloys with 
different contents of Al and Cr are calculated further using the Thermo- 
Calc kinetic database MOBNi5. The obtained results are normalized to 
those in the base model alloy S
0 
(Ni – 8Al-1.5Cr-1.5Re-3Ta – 8Mo) for 
comparison. It is the fact that diffusivities in the ordered γ ′ -Ni
3
Al phase 
are generally 1 – 2 orders of magnitude lower than that in γ -Ni [ 58 ]. 
Hence, the kinetic properties of the γ + γ ′ -microstructure strongly 
depend on the phase fraction of γ ′ phase. The Al and Cr elements in the 
coatings diffused towards the superalloy.
The effect of compositional changes at the interface between the 
coating and superalloy on the diffusion rate of elements is clarified. As 
listed in Table 1 , the Al and Cr elements tend to increase the mobility of 
Ni, Al, Cr and Mo elements in both phases, except a slight decrease of Ni 
mobility in γ ′ phase shows with added 5 wt% Cr in S
0
. The effect of Al on 
the mobility of Ni in the γ ′ phase is particularly significant, with the 
entry of 5 wt% Al increasing its mobility by a factor of five. It indicates 
that Al and Cr elements from coating into the superalloy will signifi -
cantly accelerate microstructural evolution at the coating/superalloy 
interface. In contrast to the case of the Al and Cr elements, the contents 
of Al and Cr have greater effects on the mobility of Mo in the γ ′ phase. On 
the contrary, the addition of Cr has almost no effect on the mobilities of 
Re and Ta in the γ - γ ′ phases. Specifically, the compositional changes in 
the substrate superalloys due to different Cr additions have less pro -
nounced effects on the high activation energies needed for Re and Ta 
diffusion. Hence, the higher addition of Cr has almost no effect on the 
mobilities of Re and Ta in the γ - γ ′ phases. On the contrary, both acting as 
the main formation elements of γ ′ phase in superalloy, Al content has an 
obvious effect on the segregation of Ta in γ ′ , which significantly reduces 
the mobility of Ta in γ ′ consequently.
3.3. Microstructural evolution with different Mo concentrations
In contrast to one-dimensional kinetics simulations performed by 
DICTRA, the phase-field simulation approach allows the description of 
spontaneous microstructural evolution in multi-component and multi- 
phase diffusion couples without any local equilibrium.
For simplification, the Y element is neglected in the NiCrAlY coating 
due to its low content. The main elements of the high-Mo Ni
3
Al-based SX 
superalloys are Ni, Al, Cr, Re, Ta and Mo. Due to the limitations in phase- 
field model for the number of elements and the intention to compare 
with previous thermodynamic results, a phase-field model of 
Ni – Al – Cr – Mo quaternary diffusion couple is established in this work. 
The precipitates and interface morphology of γ + γ ′ / γ + β coating/su -
peralloy system (Ni – 8Al-1.5Cr – 12Mo/Ni – 10Al – 20Cr, (wt.%)) aged at 
1100 
◦
C are shown in Fig. 6 . It is observed that the γ ′ precipitates have 
spherical morphologies and their sizes gradually increase with 
increasing aging time. It is reported that the γ / γ ′ lattice misfit in 
Ni – Al – Mo alloys decreases with increasing Mo concentration, with a 
positive value at low Mo content and a negative value at high Mo con -
tent [ 59 ]. The γ ′ particles would be spherical due to the small amount of 
γ / γ ′ lattice misfit. Therefore, the spherical morphology of γ ′ phase is 
reasonable in the present phase field simulations. Moreover, the simu -
lation results also show a precipitate-free zone (PFZ) formed at coat -
ing/superalloy interface, i.e., single-phase region, are formed as labeled 
with the red dotted lines in Fig. 6 (b) . Similar PFZ was also found in γ +
γ ′ / γ + γ ′ diffusion couple [ 25 ]. In fact, the formation of the PFZ is 
considered to be induced by the Kirkendall effect, which changes the 
diffusivity and leads to a deviation from the linear zigzag diffusion path 
predicted by the error function theory [ 60 ].
In order to study the effects of Mo in superalloys, the microstructural 
evolutions of the coating/superalloy interfaces at 1100 
◦
C for t * = 10000 
are illustrated and compared among different Mo content in Fig. 7 . The 
initial composition of the coating is fixed as Ni – 10Al – 20Cr. It is found 
that the PFZ region width slightly decrease with increasing Mo content, 
due to the decrease of the Al and Cr chemical potential gradients be -
tween the coating and superalloy. The change in the width of the PFZ 
region with increasing aging time is shown in Fig. 8 . It shows that the 
diffusion-controlled PFZ region width evolution approximately con -
forms to the parabolic law. The width of the PFZ region increases more 
slowly with the increase of Mo content. Nevertheless, for the inner part 
of superalloy, the higher the Mo content, the lower the size of the γ ′ 
phase. As shown earlier, the addition of Mo increases the mole fraction 
Fig. 6. Temporal microstructural evolution of Ni – 8Al-1.5Cr – 12Mo/Ni – 10Al – 20Cr (wt.%) system at 1100 
◦
C: (a) t * = 100; (b) t * = 5000; (c) t * = 10000; (d) t * 
= 15000.
L. Geng et al.

## Page 9

Journal of Materials Research and Technology 32 (2024) 2830–2842
2838
of γ ′ phase in superalloy, which reduces the coarsening rate of γ ′ phase. 
Whereas, it is also reported that in the Ni – 10Al-8.5Cr-xMo (2, 3, 4 at.%) 
system, the average radius of γ ′ decreases with increasing Mo concen -
tration [ 61 ]. These results indicate that the addition of Mo can effec -
tively reduce the γ ′ size and improve the γ - γ ′ microstructural stability in 
superalloy.
Fig. 9 demonstrates the concentration distributions of Ni, Al, Cr and 
Mo elements at 1100 
◦
C for t* = 10000 across the interface between 
coating and superalloy, which extracted from the phase-field simulation 
results with Position 256 as the initial interface position (position is the 
simulation grid). It can be seen that all the interfaces move to the 
superalloy side with increasing aging time, while the effect of Mo is 
probably weak due to the limit simulation scale of phase field. Moreover, 
the effects of Mo on elemental diffusion are consistent with the kinetic 
simulation results in Fig. 4 .
Essentially, the change in the microstructural evolution with Mo 
content results from the Mo effects on the diffusion coefficients of other 
elements. Therefore, the mobility of main elements (Ni, Al, Cr, Re, Ta 
and Mo) in single phase ( γ or γ ′ ) at 1100 
◦
C is calculated to analyze the 
effects of Mo further. The calculation method is the same as that used to 
obtain the data in Table 1 . As shown in Fig. 10 , the addition of Mo in -
creases the mobility of Al, Cr and Ta in the γ phase and decreases the 
mobility of Mo, Re and Ta in the γ ′ phase. While the Ni mobilities in both 
phases decrease first and then increase with increasing Mo content. 
Especially, the mobility of Ni in γ phase decreased significantly when Mo 
content increased from 8 wt% to 10 wt%. And when the Mo content is 
further increased to 12 wt%, the Ni mobility in the γ phase remains 
almost unchanged compared with that in the alloys with 8 wt% Mo. On 
the other hand, the mobilities of Al in γ and γ ′ phases all increase with 
increasing Mo content. Therefore, the addition of Mo increases the mole 
fraction of γ ′ phase and decreases the coarsening rate of γ ′ phase by 
reducing the mobility of Mo and Ni. In addition, the addition of Mo also 
reduces the PFZ region width at coating/superalloy interface due to the 
increase of Al and Cr activities in superalloy. However, it is important to 
note that increasing Mo content still increases the possibility of TCP 
phase formation.
3.4. Morphology evolution of TCP precipitate growth
Due to the complex compositions of different types of TCP phases, it 
is still unfeasible to include the evolution of these TCP phases in a 
quaternary phase-field model, which already considers γ and γ ′ phases. 
However, the morphology and growth of the TCP phase is crucial for the 
microstructural stability and mechanical properties of SX superalloys. 
Therefore, the growth kinetics of TCP phase is simulated by using a 
Fig. 7. Temporal microstructural evolution of Ni – 8Al-1.5Cr-xMo/Ni – 10Al – 20Cr system at 1100 
◦
C for t * = 10000 (a) x = 8 wt%; (b) x = 10 wt%; (c) x = 12Mo wt.%; 
(d) The γ ′ particle size distribution (PSD) in superalloy; (e) The γ ′ particle size distribution (PSD) in coating.
Fig. 8. PFZ Region width evolution of Ni – 8Al-1.5Cr-xMo (x = 8, 10, 12 wt 
%)/Ni – 10Al – 20Cr system at 1100 
◦
C.
L. Geng et al.

## Page 10

Journal of Materials Research and Technology 32 (2024) 2830–2842
2839
separate phase-field model. In order to mimic the anisotropy of TCP 
phase, the SFTS in elastic strain energy (eq. (18) ) is set to be anisotropic 
as follows: 
ε
0
ij
=
⎛
⎝
0 . 0345 0 0
0 0 . 0285 0
0 0 0 . 0027
⎞
⎠
(21) 
The growth of a single TCP phase particle at 1100 
◦
C is simulated 
first. As shown in Fig. 11 (a) , the TCP precipitate grows into a plate-like 
morphology as time increases. The high aspect ratio of the growth 
morphology is a result of the synergistic effects of the anisotropic 
interfacial energy, elastic strain energy and interface mobility anisot -
ropy, which is consistent with previous experimental observations [ 62 ]. 
The diffusion-controlled TCP phase lengthening is much faster than the 
interface-controlled thickening, leading to a large diameter/thickness 
aspect ratio [ 63 ].
We have also performed simulations to investigate the specific role of 
the compositional eigenstrain ε
c 
in the TCP growth kinetics and 
morphology ( Fig. 11 (b) ). Compositional strain is caused by the differ -
ence in size between two atoms. Compositional eigenstrain decreases 
the rate of growth in radius and increases the rate of growth in thickness. 
The consideration of ε
c 
will increase the value of 
⃒
⃒
ε
0
11
⃒
⃒
and 
⃒
⃒
ε
0
22
⃒
⃒
while 
decrease the value of 
⃒
⃒
ε
0
33
⃒
⃒
, thus decreasing the anisotropy of the total 
eigenstrain. Therefore, the radius/thickness ratio of the precipitated 
Fig. 9. Concentration distribution of Ni – 8Al-1.5Cr-xMo (x = 8, 10, 12 wt%)/Ni – 10Al – 20Cr system at 1100 
◦
C for t * = 10000: (a) Ni; (b) Al; (c) Cr; (d) Mo.
Fig. 10. Calculated mobilities of elements in single phases at 1100 
◦
C 
normalized to respective mobilities in base Ni – 8Al-1.5Cr-1.5Re-3Ta – 8Mo 
alloy S
0
.
L. Geng et al.

## Page 11

Journal of Materials Research and Technology 32 (2024) 2830–2842
2840
phase can be reduced by adding elements that make the precipitated 
phase composition eigenstrain positive with respect to the matrix. Ni, Al, 
Cr and Mo are the key elements in the new-designed Ni
3
Al-based SX 
superalloys with NiCrAlY coating. In the Mo-rich TCP precipitation 
phase, the atomic radii of Cr and Mo are smaller than that of Al but 
larger than that of Ni ( Table 2 ). As a result, the substitution of Ni atoms 
by Cr and Mo may lead to positive compositional strain, while the 
substitution of Al leads to negative compositional strain. The re -
placements of Ni atoms with Al may result in positive compositional 
strain since the atomic radius of Al is larger than that of Ni. Therefore, an 
increase in Cr and Mo concentrations at the interface between the 
coating and superalloy may decrease the TCP phase anisotropy, while an 
increase in Al concentration may increase the TCP phase anisotropy. 
Based on this, a theoretical basis is provided for regulating the 
morphology of the TCP phase and reducing its influence on the me -
chanical properties of SX superalloys by coating composition design.
One of the main advantages of phase-field method is its ability to 
Fig. 11. 3-D phase field simulations of a single precipitate of Ni – 10Al – 10Cr – 12Mo (wt.%) at 1100 
◦
C: (a) plate-like precipitate morphology at t * = 10000; (b) 
precipitate lengthening and thickening kinetics.
Table 2 
Atomic radius of Ni, Al, Cr, Mo element [ 64 ].
Al Cr Ni Mo
Atomic radius (Å) 1.43 1.30 1.28 1.39
Fig. 12. Morphology evolution of sphere-shaped and plate-shaped precipitates of Ni – 10Al – 10Cr – 12Mo (wt.%) at 1100 
◦
C(a) t * = 1000(b) t * = 5000(c) t * = 10000(d) 
t * = 15000.
L. Geng et al.

## Page 12

Journal of Materials Research and Technology 32 (2024) 2830–2842
2841
handle multiple precipitates belonging to different orientation variants 
which interact not only chemically but also elastically and evolve 
through a combined diffusional and reaction processes. The morphology 
of TCP observed under scanning electron microscope (SEM) is mainly 
point-like, rod-like and needle-like. Whereas, in reality, these shapes 
may be projections of spherical, rod or plate-like phases [ 62 ]. It is re -
ported that the α phase tends to be dot-like, whereas the σ and P phases 
tend to be plate-like in the superalloy [ 16 , 65 ]. As an illustrative example 
to study the growth kinetics and 3-D morphological evolution of TCP 
precipitated at coating/superalloy interface, we artificially introduce 6 
spherical particles of Ni – 10Al – 10Cr – 12Mo (wt.%) as nuclei with 
different variants and simulate their evolution by using phase-field 
model. As shown in Fig. 12 , these spherical nuclei then grow into 
plate morphologies, and the plates of different variants are perpendic -
ular to each other respectively. Prolonged oxidation usually leads to the 
coarsening of TCP phases precipitates at the coating/superalloy inter -
face. The simulation results at longer aging time demonstrate that the 
spherical and plate-like TCP phases interact with each other further and 
change their morphologies into ellipsoidal and flatter plate-like. These 
results have provided more comprehensive insights on the TCP 
morphology evolution at coating/superalloy interface, compensating 
the deficiency of two-dimensional experimental observation.
4. Conclusions
The protective coating is required to be adapt the substrate SX su -
peralloys, by taking into account the oxidation resistance and interfacial 
stability of the material system. Previous experimental and simulation 
results have already indicated that the degradation of coating/superal -
loy systems strongly depend on their compositions. This study focuses on 
the key elemental effects on the interdiffusion behavior and micro -
structural evolution at the interface between high-Mo and high-Al SX 
superalloys and NiCrAlY coating. The main conclusions are as follows:
(1) For Ni
3
Al-based single crystal alloys with high Mo content, the 
diffusion of Al and Cr elements from high-temperature protective 
coatings significantly increases the mobilities of Al, Cr, Mo, and 
Ni. Increasing the Mo content in the superalloy can reduce the Ni 
mobility in the γ phase, thereby balancing the effect of Al on the 
Ni mobility and aiding in enhancing the microstructural stability.
(2) Mo addition to the superalloy increases the mole fraction of the γ ′ 
phase, reduces the driving force of element diffusion from coating 
to superalloy by increasing the activities of Al and Cr in super -
alloy. However, an excessive content of Mo result in a larger 
gradient of Mo from superalloy to coating, leading to more pre -
cipitation of TCP phases. A transition in the phase structure from 
σ phase to P and α phases.
(3) The plate-like TCP phase growth by phase field simulations in -
dicates that compositional strain increases the value of 
⃒
⃒
ε
0
11
⃒
⃒
and 
⃒
⃒
ε
0
22
⃒
⃒
while reduces the 
⃒
⃒
ε
0
33
⃒
⃒
, leading to decreased eigenstrain 
anisotropy. An increase in Cr and Mo content leads to a positive 
compositional strain, resulting in a decreased radius/thickness 
ratio of the precipitated phase. The effects of Mo enable the 
reasonable increase of Al content in coating to better balance the 
interfacial stability and oxidation resistance, especially for the 
lower tendency of TCP precipitation over 1100 
◦
C.
This work has verified the feasibility of the efficient design of 
advanced coatings with the aid of thermodynamic and kinetic calcula -
tions on microstructural evolution. The research achievements on key 
elemental effects have also provided a guidance to design adaptive 
coating for the high-Mo SX superalloys servicing at ultra-high 
temperature.
Data availability
All necessary data is included within this paper.
CRediT authorship contribution statement
Lilun Geng: Conceptualization, Methodology, Investigation, Formal 
analysis, Writing – original draft, Writing – review & editing, Visuali -
zation. Wenyue Zhao: Conceptualization, Software, Funding acquisi -
tion, Investigation, Writing – review & editing. Yi Ru: 
Conceptualization, Investigation, Writing – review & editing. Mingzhe 
Li: Software. Fan Yang: Investigation. Yunpeng Hu: Investigation. 
Boxuan Du: Data curation. Yang Cao: Formal analysis. Yanling Pei: 
Resources, Funding acquisition. Shusuo Li: Funding acquisition, Su -
pervision. Shengkai Gong: Funding acquisition, Supervision, Project 
administration.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgements
This research is sponsored by the National Natural Science Founda -
tion of China (Nos. 92360302), Science Center for Gas Turbine Project 
(P2022-B-IV-005-001 and P2022-A-I-002 – 002), Key R & D Program of 
Zhejiang (Nos. 2024SSYS0085 and 2024SSYS0076) and Beijing Nova 
Program No. 20230484318.
References
[1] Kalush A, Texier D, Ecochard M, Sirvin Q, Choquet K, Gheno T, et al. Size effects on 
high temperature oxidation of MCrAlY coatings processed via APS and HVOF 
depositions. Surf Coat Technol 2022;440:128483. https://doi.org/10.1016/j. 
surfcoat.2022.128483 .
[2] Das DK. Microstructure and high temperature oxidation behavior of Pt-modified 
aluminide bond coats on Ni-base superalloys. Prog Mater Sci 2013;58:151 – 82. 
https://doi.org/10.1016/j.pmatsci.2012.08.002 .
[3] Latief FH, Kakehi K. Influence of heat treatment on anisotropic creep behavior of 
aluminide coating on a Ni-base single crystal superalloy. Mater Des 2013;52: 
134 – 42. https://doi.org/10.1016/j.matdes.2013.04.101 .
[4] Rae CMF, Hook MS, Reed RC. The effect of TCP morphology on the development of 
aluminide coated superalloys. Mater Sci Eng, A 2005;396:231 – 9. https://doi.org/ 
10.1016/j.msea.2005.01.005 .
[5] Matsuoka Y, Aoki Y, Matsumoto K, Satou A, Suzuki T, Chikugo K, et al. The 
formation of SRZ on a fourth generation single crystal superalloy applied with 
aluminide coating, Superalloys 2004. TMS; 2004. p. 637 – 42 .
[6] Das DK, Murphy KS, Ma S, Pollock TM. Formation of secondary reaction zones in 
diffusion aluminide-coated Ni-base single-crystal superalloys containing 
ruthenium. Metall Mater Trans A 2008;39:1647 – 57. https://doi.org/10.1007/ 
s11661-008-9534-1 .
[7] Esakkiraja N, Gupta A, Jayaram V, Hickel T, Divinski SV, Paul A. Diffusion, defects 
and understanding the growth of a multicomponent interdiffusion zone between 
Pt-modified B2 NiAl bond coat and single crystal superalloy. Acta Mater 2020;195: 
35 – 49. https://doi.org/10.1016/j.actamat.2020.04.016 .
[8] Dahl KV, Hald J, Horsewell A. Interdiffusion between Ni-based superalloy and 
MCrAlY coating. Defect Diffusion Forum 2006;258 – 260:73 – 8. https://dx.doi. 
org/10.4028/www.scientific.net/DDF.258-260.73 .
[9] Yang L, Chen M, Wang J, Qiao Y, Guo P, Zhu S, et al. Microstructure and 
composition evolution of a single-crystal superalloy caused by elements 
interdiffusion with an overlay NiCrAlY coating on oxidation. J Mater Sci Technol 
2020;45:49 – 58. https://doi.org/10.1016/j.jmst.2019.11.017 .
[10] Walston WS, Schaeffer JC, Murphy WH. A new type of microstructural instability 
in superalloys-SRZ, Superalloys 1996. Pennsylvania: TMS; 1996. p. 9 – 18 .
[11] Tawancy HM, Mohamed AI, Abbas NM. Effect of superalloy substrate composition 
on the performance of a thermal barrier coating system. J Mater Sci Technol 2003; 
38:3797 – 807 .
[12] Reid M, Pomeroy MJ, Robinson JS. Microstructural instability in coated single 
crystal superalloys. J Mater Process Technol 2004;153 – 154:660 – 5. https://doi. 
org/10.1016/j.jmatprotec.2004.04.132 .
[13] Zhou Y, Wang L, Wang G, Jin D, Hao W, Zhao X, et al. Influence of substrate 
composition on the oxidation performance of nickel aluminide coating prepared by 
pack cementation. Corrosion Sci 2016;110:284 – 95. https://doi.org/10.1016/j. 
corsci.2016.04.041 .
L. Geng et al.

## Page 13

Journal of Materials Research and Technology 32 (2024) 2830–2842
2842
[14] Kiruthika P, Makineni SK, Srivastava C, Chattopadhyay K, Paul A. Growth 
mechanism of the interdiffusion zone between platinum modified bond coats and 
single crystal superalloys. Acta Mater 2016;105:438 – 48. https://doi.org/10.1016/ 
j.actamat.2015.12.014 .
[15] Zhang J, Li J, Jin T, Sun X, Hu Z. Effect of Mo concentration on creep properties of 
a single crystal nickel-base superalloy. Mater Sci Eng, A 2010;527:3051 – 6. https:// 
doi.org/10.1016/j.msea.2010.01.045 .
[16] Liu Y, Zou M, Su H, Geng L, Yu Y, Zheng W, et al. Coating-associated 
microstructure evolution and elemental interdiffusion behavior at a Mo-rich nickel- 
based superalloy. Surf Coat Technol 2021;411:127005. https://doi.org/10.1016/j. 
surfcoat.2021.127005 .
[17] Simonetti M, Caron P. Role and behaviour of μ phase during deformation of a 
nickel-based single crystal superalloy. Mater Sci Eng, A 1998;254:1 – 12. https:// 
doi.org/10.1016/S0921-5093(98)00766-7 .
[18] Chen QZ, Jones CN, Knowles DM. Effect of alloying chemistry on MC carbide 
morphology in modified RR2072 and RR2086 SX superalloys. Scripta Mater 2002; 
47:669 – 75. https://doi.org/10.1016/S1359-6462(02)00266-X .
[19] Galiullin T, Chyrkin A, Pillai R, Vassen R, Quadakkers WJ. Effect of alloying 
elements in Ni-base substrate material on interdiffusion processes in MCrAlY- 
coated systems. Surf Coat Technol 2018;350:359 – 68. https://doi.org/10.1016/j. 
surfcoat.2018.07.020 .
[20] Yuan K, Peng RL, Li XH. A continuous β -NiAl layer forming at the interface of a 
MCrAlY and CMSX-4. J Therm Spray Technol 2015;25:244 – 51. https://doi.org/ 
10.1007/s11666-015-0293-4 .
[21] Wu K, Chang Y, Wang Y. Simulating interdiffusion microstructures in Ni – Al – Cr 
diffusion couples: a phase field approach coupled with CALPHAD database. Scripta 
Mater 2004;50:1145 – 50. https://doi.org/10.1016/j.scriptamat.2004.01.025 .
[22] Wu K, Zhou N, Pan X, Morral JE, Wang Y. Multiphase Ni – Cr – Al diffusion couples: a 
comparison of phase field simulations with experimental data. Acta Mater 2008;56: 
3854 – 61. https://doi.org/10.1016/j.actamat.2008.02.051 .
[23] Ta N, Zhang L, Tang Y, Chen W, Du Y. Effect of temperature gradient on 
microstructure evolution in Ni – Al – Cr bond coat/substrate systems: a phase-field 
study. Surf Coat Technol 2015;261:364 – 74. https://doi.org/10.1016/j. 
surfcoat.2014.10.061 .
[24] Ta N, Zhang L, Du Y. A trial to design γ / γ ′ bond coat in Ni – Al – Cr mode TBCs aided 
by phase-field simulation. Coatings 2018;8:1 – 19. https://doi.org/10.3390/ 
coatings8120421 .
[25] Li Y, Wang H, Chen J, Yang S, Sang P, Long H. Temperature gradient driving 
interdiffusion interface and composition evolution in Ni – Al – Cr alloys. Rare Met 
2022;41:3186 – 96. https://doi.org/10.1007/s12598-022-02024-y .
[26] Ru Y, Zhang H, Pei Y, Fu Y, Li S, Gong S, et al. New type of γ ′ phase in Ni based 
single crystal superalloys: its formation mechanism and strengthening effect. Mater 
Des 2018;145:181 – 95. https://doi.org/10.1016/j.matdes.2018.02.053 .
[27] Luo L, Ma Y, Li S, Pei Y, Qin L, Gong S. Evolutions of microstructure and lattice 
misfit in a γ ′ -rich Ni-based superalloy during ultra-high temperature thermal cycle. 
Intermetallics 2018;99:18 – 26. https://doi.org/10.1016/j.intermet.2018.05.011 .
[28] Ai C, Li Q, Zhang J, Su H, Yang W, Liu L, et al. Effect of substituting Mo for W on 
γ / γ ′ partitioning behaviors of alloying elements in heat-treated second generation 
Ni based single crystal superalloys: an atom probe tomography study. 
Intermetallics 2021;134:107198. https://doi.org/10.1016/j. 
intermet.2021.107198 .
[29] Larsson H, Engstr ¨om A. A homogenization approach to diffusion simulations 
applied to α + γ Fe – Cr – Ni diffusion couples. Acta Mater 2006;54:2431 – 9. https:// 
doi.org/10.1016/j.actamat.2006.01.020 .
[30] Andersson JO, Helander T, Hoglund L, Shi P, Sundman B. Thermo-Calc & DICTRA, 
computational tools for materials science. Calphad 2002;26:273 – 312 .
[31] Larsson H, H ¨oglund L. Multiphase diffusion simulations in 1D using the DICTRA 
homogenization model. Calphad 2009;33:495 – 501. https://doi.org/10.1016/j. 
calphad.2009.06.004 .
[32] Chen H, Barman T. Thermo-Calc and DICTRA modelling of the β -phase depletion 
behaviour in CoNiCrAlY coating alloys at different Al contents. Comput Mater Sci 
2018;147:103 – 14. https://doi.org/10.1016/j.commatsci.2018.02.013 .
[33] Thermo-Calc T. TCS Ni-based superalloys database, TCNI10 Thermo-calc. 2021 .
[34] Thermo-Calc M. TCS Ni-alloys mobility database. MOBNI5 thermo-calc. 2021 .
[35] Kitashima T, Wang J, Harada H. Phase-field simulation with the CALPHAD method 
for the microstructure evolution of multi-component Ni-base superalloys. 
Intermetallics 2008;16:239 – 45. https://doi.org/10.1016/j.intermet.2007.10.001 .
[36] Zhu JZ, Liu ZK, Vaithyanathan V, Chen LQ. Linking phase-field model to 
CALPHAD: application to precipitate shape evolution in Ni-base alloys. Scripta 
Mater 2002;46:401 – 6 .
[37] Huang W, Chang YA. Thermodynamic properties of the Ni-Al-Cr system. 
Intermetallics 1999;7:863 – 74 .
[38] Jindal V, Sarma BN, Lele S. A thermodynamic assessment of the Cr – Mo system 
using CE-CVM. Calphad 2013;43:80 – 5. https://doi.org/10.1016/j. 
calphad.2013.10.003 .
[39] Zhou SH, Wang Y, Chen LQ, Liu ZK, Napolitano RE. Solution-based thermodynamic 
modeling of the Ni – Al – Mo system using first-principles calculations. Calphad 2014; 
46:124 – 33. https://doi.org/10.1016/j.calphad.2014.03.002 .
[40] Peng J, Franke P, Seifert HJ. Experimental investigation and CALPHAD assessment 
of the eutectic trough in the system NiAl-Cr-Mo. J Phase Equilibria Diffus 2016;37: 
592 – 600. https://doi.org/10.1007/s11669-016-0490-y .
[41] Wang YU, Jin YM, Khachaturyan AG. Phase field microelasticity theory and 
modeling of elastically and structurally inhomogeneous solid. J Appl Phys 2002;92: 
1351 – 60. https://doi.org/10.1063/1.1492859 .
[42] Mohanty RR, Sohn Y. Phase-field investigation of multicomponent diffusion in 
single-phase and two-phase diffusion couples. J Phase Equilibria Diffus 2006;27: 
676 – 83. https://doi.org/10.1361/154770306x153738 .
[43] Shewmon PG. Diffusion in solids. Springer: McGraw-Hill Book Company; 1963 .
[44] Huang C, Cruz MOdl, Swift BW. Phase separation of ternary mixtures: symmetric 
polymer blends. Macromolecules 1995;28:7996 – 8005 .
[45] Engstr ¨om A, 
¨
Agren J
¨
A. Assessment of diffusional mobilities in face-centered cubic 
Ni-Cr-Al alloys. Int J Mater Res 1996;87:92 – 7. https://doi.org/10.1515/ijmr-1996- 
870205 .
[46] Cahn JW, Hilliard JE. Free energy of a nonuniform system. I. interfacial free 
energy. J Chem Phys 1958;28:258 – 67 .
[47] Allen SM, Cahn JW. A microscopic theory for antiphase boundary motion and its 
application to antiphase domain coarsening. Acta Metall 1979;27:1085 – 95. 
https://doi.org/10.1016/0001-6160(79)90196-2 .
[48] Chen LQ, Shen J. Applications of semi-implicit fourier-spectral method to phase 
field equations. Comput Phys Commun 1998;108:147 – 58 .
[49] Zhang Y, Fu H, Zhou X, Zhang Y, Xie J. Effects of aluminum and molybdenum 
content on the microstructure and properties of multi-component γ ′ -strengthened 
cobalt-base superalloys. Mater Sci Eng, A 2018;737:265 – 73. https://doi.org/ 
10.1016/j.msea.2018.09.058 .
[50] RAE CMF, Reed RC. The precipitation of topologically close-packed phases in 
rhenium-containing superalloys. Acta Mater 2001;49:4113 – 25 .
[51] Long H, Liu Y, Mao S, Wei H, Zhang J, Ma S, et al. Effect of chemical composition 
on particle morphology of topologically close-packed precipitates in a Ni-based 
single crystal superalloy. Scripta Mater 2018;157:100 – 5. https://doi.org/10.1016/ 
j.scriptamat.2018.07.041 .
[52] Gao S, Liu Z, Li C, Zhou Y, Jin T. In situ TEM investigation on the precipitation 
behavior of μ phase in Ni-base single crystal superalloys. Acta Mater 2016;110: 
268 – 75. https://doi.org/10.1016/j.actamat.2016.03.046 .
[53] Tan Z, Yang L, Wang X, Du Y, Ye L, Hou G, et al. Evolution of TCP phase during 
long term thermal exposure in several Re-containing single crystal superalloys. 
Acta Metall Sin 2019;33:731 – 40. https://doi.org/10.1007/s40195-019-00976-2 .
[54] Kang J, Liu Y, Zhou J, Zhuo W, Zhang J, Zeng J, et al. Temperature-dependent 
evolution mechanism of interface microstructure between gradient MCrAlY 
coatings and nickel-based superalloy. Mater Des 2024;237:112585. https://doi. 
org/10.1016/j.matdes.2023.112585 .
[55] Cheng Y, Zhao X, Xia W, Yue Q, Gu Y, Wei X, et al. Effect of Mo on microstructural 
stability of a 4th generation Ni-based single crystal superalloy. J Mater Res Technol 
2022;21:2672 – 81. https://doi.org/10.1016/j.jmrt.2022.10.072 .
[56] Ma Z, Pei Y, Luo L, Qin L, Li S, Gong S. Partitioning behavior and lattice misfit of 
γ / γ ′ phases in Ni-based superalloys with different Mo additions. Rare Met 2020;40: 
920 – 7. https://doi.org/10.1007/s12598-019-01309-z .
[57] Wen S, Tang Y, Zhong J, Zhang L, Du Y, Zheng F. High-throughput measurements 
of interdiffusivity matrices in face centered cubic Ni – Al – Mo alloys at 1273 – 1473 K. 
J Mater Res 2017;32:2188 – 201. https://doi.org/10.1557/jmr.2017.44 .
[58] Campbell CE. Assessment of the diffusion mobilites in the γ ′ and B2 phases in the 
Ni – Al – Cr system. Acta Mater 2008;56:4277 – 90. https://doi.org/10.1016/j. 
actamat.2008.04.061 .
[59] Wang T, Chen L, Liu Z. First-principles calculations and phenomenological 
modeling of lattice misfit in Ni-base superalloys. Mater Sci Eng, A 2006;431: 
196 – 200. https://doi.org/10.1016/j.msea.2006.05.152 .
[60] Wu K, Morral JE, Wang Y. A phase field study of microstructural changes due to the 
kirkendall effect in two-phase diffusion couples. Acta Mater 2001;49:3401 – 8 .
[61] Wang Z, Liang C, Wang D, Ding X. Composition and temperature dependence of 
kinetic behavior of γ ′ precipitation in Ni-Al-Cr-Mo quaternary model superalloys: a 
phase field study. J Alloys Compd 2024;976:172982. https://doi.org/10.1016/j. 
jallcom.2023.172982 .
[62] Zhang Y, Zhang J, Li P, Jin H, Zhang W, Wang Z, et al. Characterization of 
topologically close-packed phases and precipitation behavior of P phase in a Ni- 
based single crystal superalloy. Intermetallics 2020;125:106887. https://doi.org/ 
10.1016/j.intermet.2020.106887 .
[63] Ji Y, Chen L. Phase-field model of stoichiometric compounds and solution phases. 
Acta Mater 2022;234:118007. https://doi.org/10.1016/j.actamat.2022.118007 .
[64] Miracle DB, Sanders WS, Senkov ON. The influence of efficient atomic packing on 
the constitution of metallic glasses. Philos Mag 2003;83:2409 – 28. https://doi.org/ 
10.1080/1478643031000098828 .
[65] Dubiel B, Indyka P, KalembaRec I, Kruk A, Moskalewicz T, Radziszewska A, et al. 
The influence of high temperature annealing and creep on the microstructure and 
chemical element distribution in the γ , γ ′ and TCP phases in single crystal Ni-base 
superalloy. J Alloys Compd 2018;731:693 – 703. https://doi.org/10.1016/j. 
jallcom.2017.10.076 .
L. Geng et al.
