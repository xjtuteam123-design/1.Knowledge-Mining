# 1-s2.0-S0921509323012765-main

<!-- source: D:\总文献\1-s2.0-S0921509323012765-main.pdf -->
<!-- file_sha256: 74e50704f6e2f5b1e65f857a5a041a8ad6b4266b2114c3707d23c53573409d26 -->

## Page 1

Materials Science & Engineering A 889 (2024) 145852
Available online 27 October 2023
0921-5093/© 2023 Elsevier B.V. All rights reserved.
Degradation and anisotropy characteristics of fracture toughness in 
Ni-based superalloys after phase coarsening 
Shunyong Zhang
a , b
, Jianfeng Zhao
a , b
, Yanxiang Liang
a , b
, Jicheng Li
a , b , *
, Xicheng Huang
a , b 
a
Institute of Systems Engineering, China Academy of Engineering Physics, Mianyang, 621999, China 
b
Shock and Vibration of Engineering Materials and Structures Key Laboratory of Sichuan Province, Mianyang, 621999, China 
ARTICLE INFO 
Keywords: 
Ni-based superalloys 
Phase coarsening 
Mode I tear test 
Fracture toughness 
Anisotropy 
ABSTRACT 
The effect of phase coarsening on the crack propagation characteristics and the corresponding fracture toughness 
in Ni-based superalloys is investigated by integrating with the finite element method simulations and related 
mechanism analysis, and the relationship between the macroscopic mechanical properties of alloys and the 
evolution in their microstructures are discussed in detail. Related analysis shows that the fracture toughness of 
alloys degraded considerably with phase coarsening. Moreover, the fracture toughness also demonstrates an 
anisotropic characteristic. Specifically, when the volume fraction of precipitate is low or the degree of phase 
coarsening is relatively low, the fracture toughness of alloys increases first and then decreases gradually along 
with increasing the loading angle, showing an inverted "V" shape. In comparison, in the case of a higher volume 
fraction of precipitate or higher degree of phase coarsening, the fracture toughness displays an opposite variation 
trend, and reaches the minimum value at the loading direction of 45
◦
. The corresponding variation character -
istics of fracture toughness are correlated with the evolutions of precipitate shape, size, and distribution within 
the alloys. The change in the microstructure or that in the loading direction affects remarkably the initiation and 
growth of micro-voids within the alloys, and it further affects the crack propagation characteristics, resulting in 
the degradation and anisotropy characteristics of macroscopic fracture toughness in the alloys. Related work is of 
great significance for the structure design of Ni-based superalloys components, the mechanical property evalu -
ation and the life prediction during their service process. 
1. Introduction 
Ni-based superalloys have outstanding mechanical properties at high 
temperatures, such as high strength, good plasticity, considerable fa -
tigue and creep resistance, and they are widely used as hot components 
in important equipment [ 1 – 3 ]. During the service of Ni-based superal -
loys, the precipitate phase in the microstructure is easily coarsened 
(which is also usually called Ostwald ripening), and thus the precipitate 
shape, size, and distribution (PSD) will change significantly [ 4 – 8 ]. 
Generally, the macroscopic mechanical properties of materials are 
closely related to their internal structures. Thus, the microstructural 
change may induce variations in the internal dislocation behavior and in 
the corresponding macroscopic mechanical response [ 9 – 14 ]. Since the 
hot components usually suffer complex loading conditions in service, 
thus the microstructural evolution in component materials and the 
corresponding variation in their mechanical properties [ 1 , 15 ], e.g., 
fracture toughness, fracture energy, would lead to safety risks to the 
equipment. 
Related studies demonstrate that the γ ′ precipitate particles within 
the Ni-based superalloys have a strong hindering effect on the disloca -
tion movement. In the phase coarsening condition, dislocations mainly 
behave as bypassing the precipitate particles, and the strengthening 
effect of the precipitate gradually decreases due to the increase in par -
ticle size [ 16 – 21 ]. Consequently, the mechanical properties of Ni-based 
superalloys, including strength, ductility, fracture toughness and frac -
ture energy, will be changed. Related mode I tear tests indeed showed 
that the fracture characteristics change significantly after phase coars -
ening, such as the crack propagation manner [ 10 , 12 , 21 – 25 ], and thus 
the alloys exhibit different deformation and failure morphologies [ 10 , 
26 – 28 ]. Generally, the experimental observations mainly focus on the 
deformation and failure morphologies of materials before and after the 
test, and related parametric measurement is usually limited on the 
sample surface, and it is hard to track the detailed evolution process of 
the internal structure of materials as well as the corresponding inner 
* Corresponding author. Institute of Systems Engineering, China Academy of Engineering Physics, Mianyang, 621999, China. 
E-mail address: lijc401@caep.cn (J. Li). 
Contents lists available at ScienceDirect 
Materials Science & Engineering A 
journal homepag e: www.else vier.com/loc ate/msea 
https://doi.org/10.1016/j.msea.2023.145852 
Received 1 May 2023; Received in revised form 22 October 2023; Accepted 25 October 2023

## Page 2

Materials Science & Engineering A 889 (2024) 145852
2
parameters, thus related experiments are still difficult to characterize in 
detail the influence of microstructure of materials on their macroscopic 
mechanical properties. 
Complementary to the experimental investigation, the finite element 
method (FEM) simulation has become an effective way to correlate the 
microstructure to the macroscopic mechanical response of metallic 
materials. FEM simulation can obtain the detailed deformation and 
failure process of materials, and investigate the evolution of internal 
parameters, and thus it is conducive to the deeper analysis of the me -
chanical properties. In the authors ’ previous work, FEM models were 
established based on the microstructures of Al – Li alloys, and numerical 
simulations under various deformation conditions were conducted, then 
the variations of mechanical properties of alloys due to phase coars -
ening, including hardness, strength, ductility, fracture toughness and 
fatigue crack propagation, etc., were studied systematically [ 29 – 31 ]. 
The related analysis demonstrated that the FEM simulations can 
describe well the main mechanical properties as well as their variation in 
the alloys with phase coarsening, and such a method provides a practical 
approach to investigate process-structure-property relationships in 
materials. 
Different from the situation of Al – Li alloys, in which the precipitate 
particles always maintain a spherical shape after phase coarsening, the 
coarsening of γ ′ precipitate particles within the Ni-based superalloys 
shows a preferential growth characteristic, and the precipitate shape 
changes generally in the following order: sphere → cube → quasicubic 
→ long strip [ 4 , 5 ]. Therefore, the microstructure of alloys gradually 
displays an anisotropic characteristic. The authors ’ recent investigation 
indeed demonstrated that the hardness of Ni-based superalloys with 
phase coarsening degrades significantly, and especially it gradually 
shows an anisotropic feature [ 32 ]. Although there have been many 
studies on the fracture toughness of Ni-based superalloys [ 12 , 21 – 25 , 33 , 
34 ] systematic analysis on the relationship between fracture charac -
teristics (e.g., crack propagation, fracture toughness, etc.) and micro -
structure of alloys is still lacking. Specifically, the investigation of 
anisotropy in their fracture toughness resulting from phase coarsening is 
rarely seen. 
In the present study, FEM simulations of the Mode I tear test 
regarding Ni-based superalloys with various microstructure character -
istics, including two kinds of volume fractions of γ ′ precipitate phase and 
three degrees of phase coarsening, are conducted. In the simulations, the 
geometrical models are established based on the inner structure of al -
loys. Variations of their fracture characteristics, including crack propa -
gation, fracture toughness and the corresponding anisotropy feature, 
etc., are analyzed in detail, and their correlations with phase coarsening 
in the microstructure are deeply investigated. Moreover, some sugges -
tions for microstructure design and performance optimization of Ni- 
based superalloys are given based on related analysis. 
2. FEM simulations 
Generally, three-dimensional (3-D) FEM geometrical model could 
represent better the actual loading conditions and the crack propagation 
characteristics in materials. Comparatively, two-dimensional (2-D) FEM 
simulation is convenient to investigate directly the deformation and 
failure processes, and it can also cut the calculation amount and save the 
solution time. Moreover, the authors ’ previous work shows that 2-D FEM 
simulation could also describe well the main mechanical behaviors of 
alloys and represent related physical mechanisms [ 29 – 32 ]. Hence, the 
analysis in the present manuscript will mainly be based on the 2-D FEM 
simulations. 
2.1. Geometrical models 
Similar to the authors ’ previous work [ 29 ], the geometrical models 
are established in the pre-processing program of commercial finite 
element software. For convenience of analysis, six kinds of 
microstructures of Ni-based superalloys, including two volume fractions 
of precipitate combined with three degrees of phase coarsening, are 
selected for comparative analysis. To represent the microstructure well, 
it is better to refine the meshes to obtain a good precipitate structure. 
However, mesh refinement will also lead to a significant increase in the 
calculation amount. To reduce the calculation cost, the inhomogeneity 
of microstructure is considered only in the representative zone in the 
specimen where deformation and failure of materials mainly occur, and 
comparatively, the other regions in the specimen are defined as homo -
geneous material, and in these zones the meshes are relatively coarser. 
Integrated with the Mode I tear test experiments and related simu -
lation methods [ 21 , 23 , 29 – 31 , 35 ], the sketch of 2-D model of the flat CT 
specimen and the fixtures are shown in Fig. 1 , in which the red region is 
the representative zone wherein the inhomogeneity of microstructure 
will be considered, and the blue region is considered as homogeneous 
material. The geometrical model is meshed with 4-node plane-strain 
elements, and the representative zone is meshed with 600 × 400 
square elements to balance the calculation accuracy and the computa -
tion cost. In real Ni-based superalloys, due to the deviations in compo -
nents and coarsening kinetics, the shape and distribution characteristics 
of γ ′ precipitation particles are different, and the size distribution is 
wide, with a range of about 10~500 nm, e.g., that in the wrought su -
peralloys with a range of 10~30 nm [ 9 , 36 – 38 ], that in the cast super -
alloys with a range of 30~110 nm [ 11 , 13 , 16 , 17 , 39 , 40 ], and that in the 
single crystal superalloys with a wide range of 100~500 nm [ 8 , 28 , 
41 – 44 ]. Besides, the particle size will further change after phase 
coarsening. In this study, the SC Ni-based superalloys, which are widely 
used in engineering, are selected as an example, and the corresponding 
average γ ′ precipitation size is about 200 nm [ 8 , 28 , 41 – 43 ]. Accordingly, 
the element size in the representative zone is set as 30 nm, i.e., the 
dimension of the representative zone is 18 × 12 μ m. Such an element 
size can present relatively well the shape and distribution characteristics 
Fig. 1. 2-D FE geometrical model for Mode I tear test. 
S. Zhang et al.

## Page 3

Materials Science & Engineering A 889 (2024) 145852
3
of the γ ′ particles in different kinds of Ni-based superalloys with different 
degrees of phase coarsening, i.e., the corresponding geometrical models 
in the FEM simulations are suitable for various microstructural charac -
teristics in real superalloys. Comparatively, to reduce the calculation 
amount, the meshes in other zones will become coarser gradually from 
the representative zone towards the outer sides. Furthermore, in Fig. 1 
the loading condition is also sketched, i.e., Fixture 1 and Fixture 2 on the 
outer surfaces move upwards and downwards respectively at a speed of 
ν , and the specimen is fixed with the two fixtures. 
In the above geometrical model from the pre-processing software, 
the precipitate model is still not included in the representative zone, and 
the precipitate particles need to be further established. In real Ni-based 
superalloys, there is an interface layer between the precipitate particle 
and the matrix, and it is usually a weak zone within the material 
[ 45 – 47 ]. To represent the microstructure of alloys well, the geometrical 
models of precipitate particles and their corresponding interface layers 
are also created simultaneously. 
Based on the format of keyword file in the finite element software, 
the precipitate particles and the corresponding interface layers can be 
defined in the FEM geometrical model through the aid of the Python or 
C ++ program. The element information section in the keyword file lists 
the detailed messages for each element in the geometrical model, 
including element ID number, part ID number to which the element 
belongs, and node ID number that belongs to the element, etc. Similarly, 
in the part information section part ID number and material ID number 
are included. Especially, these ID numbers correspond to each other 
uniquely, and thus by changing the part ID number of an element one 
can change its material dependence correspondingly. Besides, the grid 
node information could be obtained by digital processing of micro -
structure images from TEM scan of real alloys or numerical simulation 
results; integrated with the element information in the representative 
zone of FEM models, the geometrical models of precipitate particles as 
well as the corresponding interface layers are established through a grid 
mapping algorithm. The detailed establishing process is listed as follow: 
(1). Establishment of grids containing precipitate phase and matrix 
phase 
Step 1 Digitize the image of microstructure in real Ni-based superalloys 
through programming process (e.g., Python), and then transform 
it into a gray image through related functions; 
Step 2 Adjust the resolution of gray image by the nearest neighbor 
interpolation method, and make the number of pixel points equal 
to that of elements in the representative zone (600 × 400 pixels); 
Step 3 Binarize the gray image through the image segmentation func -
tion, wherein the black and white pixels correspond to the matrix 
and precipitation phases, respectively, and then correlate the 
Node ID number with the Material ID number (i.e., pixel value). 
Therefore, the transition model containing precipitate phase and 
matrix phase is established during this process. 
(2). Definition of interface layer in the grids 
Step 1 Check grids under the left-right order. When the point property 
belongs to the matrix phase, if its left point belongs to the matrix 
phase and the right point to the precipitate phase, or if its left 
point belongs to the precipitate phase and the right point to the 
matrix phase, then shift the point property as the interface layer. 
Step 2 Repeat Step 1 until all the 600 × 400 grids are checked. During 
this process the interface layers locating in the left and right sides 
of precipitates are established. 
Step 3 Similar to Step 1, check grids under the top-down order. When 
the point property belongs to the matrix phase, if its top point 
belongs to the matrix phase and the down point to the precipitate 
phase, or if its top point belongs to the precipitate phase and the 
down point to the matrix phase, then shift the point property as 
the interface layer. 
Step 4 Repeat Step 3 until all the 600 × 400 grids are checked. During 
this process the interface layers locating in the top and down 
sides of precipitates are established. 
(3). Definition of elements for precipitates and interface layers in the 
FEM geometrical model 
Step 1 Arrange ID numbers for grids in the above process (2) under the 
left-right-down-top order, i.e., the points will be numbered from 
1 to 240000. Such point ID numbers just correspond to the 
element ID numbers in the representative zone generated from 
the pre-processing program of finite element software. 
Step 2 Define the material property for the FEM elements based on the 
point ID number in step 1 and the element ID number. If the point 
material belongs to the precipitate phase or the interface layer 
phase, then shift the material property of the element with the 
same ID number to the corresponding material number, other -
wise keep the element material as the matrix phase. 
Step 3 Repeat Step 2 until all the 240000 elements are checked. 
Integrated with the phase-field simulation results on Ni-based su -
peralloys with phase coarsening [ 48 , 49 ], the FEM models of the repre -
sentative zone are created through the above methods and listed in 
Fig. 2 . To compare the effects of the volume fraction of precipitate and 
the degree of phase coarsening, two volume fractions, V
V 
= 30% and 
60%, are adopted as an example, and the microstructures corresponding 
to three aging time ( t
1 
= 20 h, 10 h; t
2 
= 40 h, 50h; t
3 
= 67 h, 1000 h) are 
considered for each volume fraction value, as shown in Fig. 2 (a – b). It is 
seen that as the aging time increases, the precipitate particles gradually 
transform into a long-strip shape, and their distribution displays a queue 
characteristic. In the later analysis the aging time t
1
, t
2 
and t
3 
will be 
called uniformly as the early, middle, and late phase coarsening stages, 
respectively. Furthermore, to study the anisotropy of mechanical prop -
erties derived from phase coarsening, e.g., the crack propagation and 
fracture toughness, the mechanical behaviors of alloys under different 
loading directions are also investigated, and three loading directions, 
including the longitudinal, oblique, and transverse loadings, are 
selected, i.e., the angle between the axial direction of long-strip pre -
cipitate particles and the movement direction of the fixture is 0
◦
, 45
◦
and 
90
◦
, respectively. The geometrical models of microstructure corre -
sponding to the aging time of t
2 
and t
3 
are listed in Fig. 2 (c – f), and Fig. 3 
further shows the magnification of meshes in the right bottom with a 
size of 2400 nm × 2400 nm corresponding to the microstructure of V
V 
=
60% & t
3
, and it can be seen that fine meshes are obtained through the 
above geometrical model-establishing methods. 
Fig. 4 further shows a transmission electron microscopy (TEM) image 
of the real Ni-based superalloys [ 49 ]. By comparing with the geometric 
models of microstructure corresponding to t
3 
in Fig. 2 , it can be found 
that the FEM models represent relatively well the internal microstruc -
tures of real materials. 
2.2. Constitutive model 
Ni-based superalloys usually behave with an elastic-plastic defor -
mation feature, and this kind of alloy will experience a period of damage 
accumulation before the eventual failure. Meanwhile, though the 
macroscopic mechanical properties of alloys may show an anisotropic 
characteristic, it is mainly derived from the geometry and distribution 
feature of the precipitate particles; Comparatively, regarding each phase 
within the alloy, including the precipitate and the matrix, its own me -
chanical properties can be considered as isotropic. Hence, an isotropic 
elastic-plastic model combined with damage [ 50 ] will be used to 
describe the mechanical behaviors of different phases within the alloy. 
Under this constitutive model, the material will yield after the initial 
elastic deformation, then plastic deformation begins and certain strain 
hardening will occur during this period; When the plastic strain accu -
mulates to a certain value, the damage starts within the material and the 
stress decreases gradually; Finally, damage accumulates to the critical 
S. Zhang et al.

## Page 4

Materials Science & Engineering A 889 (2024) 145852
4
Fig. 2. FEM geometrical models of the representative zone in the specimen corresponding to different microstructures and loading directions. 
S. Zhang et al.

## Page 5

Materials Science & Engineering A 889 (2024) 145852
5
value and failure occurs within the material, at the same time it can no 
longer sustain the external loading. The detailed expressions of the 
model are as the following: 
d ε
ij
= d ε
e
ij
+ d ε
p
ij
(1a) 
d ε
e
ij
=
1 + ν
E
(
d σ
ij
 
ν
1 + ν
d σ
kk
δ
ij
)
(1b) 
d ε
p
ij
=
3 s
ij
2 σ
e
d ε
p
e
(1c) 
ε
p
e
=
∫
t
0
̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅ ̅
2
3
d ε
p
ij
d ε
p
ij
√
(1d) 
σ
e
=
̅̅̅̅̅̅̅̅̅̅̅ ̅
3
2
S
ij
S
ij
√
(1e) 
σ = σ
e
( 1 D ) (2a) 
d D =
⎧
⎪
⎨
⎪
⎩
κ
Q
d ε
p
e
when ε
p
e
> ε
p
e , d
and
σ
m
σ
e
> 
1
3
0 other cases
(2b) 
κ =
1
2
ε
e
: L : ε
e
(2c) 
Eq. (1) implies that the material is isotropic, and the total strain ε is 
decomposed into an elastic part ε
e 
and a plastic part ε
p 
and they are 
decoupled. E and ν are Young ’ s modulus and Poisson ’ s ratio, respec -
tively; S
ij
= σ
ij
 
1
3
σ
k
δ
ij 
is the deviatoric stress tensor; σ
e 
is the von-Mises 
effective stress; and ε
p
e 
is the effective plastic strain. 
In Eq. (2) , D is the damage factor, which takes values in the range of 
0 ≤ D ≤ 1; Q is the material constant relating to the damage rate; ε
p
e , d 
is 
the effective plastic strain threshold after which damage accumulation 
starts within the material; σ
m
/ σ
e 
is the stress triaxiality; κ is the strain 
energy density release rate, and in its expression L
e 
and ε
e 
are the fourth- 
order elasticity tensor and the elastic strain tensor, respectively. 
Thus, isotropic hardening will occur first after the yielding of ma -
terial, and the material softening will start when damage begins. During 
the deformation process, the relationship between the stress σ and the 
strain ε at different stages can be expressed as: 
σ =
⎧
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎩
E ε when ε < σ
y 0
σ
y 0
+ H ε
p
e
when
σ
y 0
E
≤ ε <
(
σ
y 0
E
+ ε
p
e , d
)
(
σ
y 0
+ H ε
p
e , d
)
( 1 D ) when
(
σ
y 0
E
+ ε
p
e , d
)
≤ ε <
(
σ
y 0
E
+ ε
p
e , C
)
0 when ε ≥
(
σ
y 0
E
+ ε
p
e , C
)
(3) 
In Eq. (3) , σ
y 0 
is the initial yielding stress; H is the isotropic hardening 
modulus; ε
p
e , C 
is the critical effective plastic strain at the failure of ma -
terial (i.e., D = 1). 
To illustrate more clearly the variation characteristics of stress dur -
ing the deformation of materials, the stress-strain curve in Eq. (3) is also 
plotted in Fig. 5 . Integrated with related investigations on Ni-based su -
peralloys [ 9 , 11 , 13 , 45 – 47 ]. and based on the authors ’ previous FEM 
simulation work [ 32 ], the model parameters corresponding to different 
phases within the alloys are obtained and listed in Table 1 . It can be 
found that most of the parameters are the same among the three phases, 
and the only difference is the initial yielding stress σ
y 0
, where the 
yielding stress of γ ′ precipitate is the highest, with a value of 1.25 times 
of that in the matrix, and the yielding stress of the interface layer is 
slightly lower compared to that of the matrix. Besides, regarding the 
homogeneous zone, the yielding strength is calculated by the law of 
mixtures [ 50 ], i.e., σ
y 0 HZ
= σ
y 0 P
• V
V
+ σ
y 0 M
• ( 1 V
V
) , and its value 
is also listed in Table 1 . Moreover, the fixtures are defined as ideal elastic 
Fig. 3. Local meshes in the right bottom of representative zone corresponding to the microstructure with V
V 
= 60% & t
3 
and different loading directions. 
Fig. 4. TEM image of microstructure in Ni-based superalloys after phase 
coarsening [ 48 ]. 
S. Zhang et al.

## Page 6

Materials Science & Engineering A 889 (2024) 145852
6
materials. 
3. Results and analysis 
Based on the geometrical and constitutive models in Section 2 , FEM 
simulations and related analysis are conducted in the following, and the 
deformation morphology and crack propagation characteristics in the 
representative zone of the specimen corresponding to various micro -
structures and loading directions will be emphasized. Generally, in real 
quasi-static tests, the strain rate ˙ε usually locates in the range of about 
10
 5
~10
 1
s
 1 
[ 51 , 52 ]. According to the fact that the present consti -
tutive model does not involve the effect of strain rate, to save solution 
time in the simulation, the fixture in the model is loaded at a constant 
low rate, and the strain rate is as 10
 2
s
 1
. The authors ’ previous work 
demonstrated that such a loading approach can save solution time and 
ensure the rationality of FEM simulation results [ 29 – 32 ]. 
3.1. Macroscopic deformation morphologies 
Under the Mode I tear test, the failure of the specimen starts from the 
pre-crack tip. The final fracture morphologies of specimen in the FEM 
simulations mainly show two features, one is that the crack propagation 
direction is almost always perpendicular to the loading direction, as 
shown in Fig. 6 (a); and comparatively, the other form is that the crack 
path usually twists in a certain extent during the late stage of crack 
propagation, as shown in Fig. 6 (b). The real Ni-based superalloys spec -
imens in the Mode I tear test indeed display these two kinds of 
Fig. 5. Sketch of stress-strain relationship in the isotropic elastic-plastic model 
combined with damage. 
Table 1 
Mechanical parameters for different phases in the Ni-based superalloys. 
Phase ρ /(kg/m
3
) E /(GPa) υ σ
y 0
/(MPa) H /(MPa) ε
p
e , d 
Q /(MN/m) 
Matrix 8900 200 0.32 800 50 1.2 2 
Precipitate 8900 200 0.32 1000 50 1.2 2 
Interface layer 8900 200 0.32 750 50 1.2 2 
Homogeneous zone 8900 200 0.32 860 ( V
V 
= 30%) 50 1.2 2 
920 ( V
V 
= 60%) 
Fig. 6. Failure morphologies of Ni-based superalloys specimens under the Mode I tear test. 
S. Zhang et al.

## Page 7

Materials Science & Engineering A 889 (2024) 145852
7
macroscopic fracture morphologies, and some examples are listed in 
Fig. 6 (c – e) [ 22 , 24 , 53 ], wherein Fig. 6 (d) shows the test result under 
fatigue cyclic loading. Our previous work demonstrated that the defor -
mation and failure characteristics in the precipitate strengthened alloys 
under the cyclic loading are similar to that under the Mode I tear 
loading, especially the effect of precipitation particles on the crack 
propagation characteristics is consistent with each other [ 31 ]. Hence, 
the simulation results accord well with the experimental investigations, 
i.e., the FEM simulations describe well the deformation and failure 
characteristics of Ni-based superalloys under the Mode I tear test 
condition. 
3.2. Microscopic deformation characteristics 
In the following the stress evolution within the specimen during the 
loading process will be analyzed, and the case with V
V 
= 30% & t
2 
& r
a 
= 0
◦
is selected as an example. The distribution of von-Mises effective 
stress at the loading displacement of s = 45 nm is shown in Fig. 7 (a), and 
Fig. 7 (b) further lists the magnification of the pre-crack tip zone. It can 
be seen that the disturbance from the loading on the upper and bottom 
fixtures has just arrived at the pre-crack area, and the stress amplitude is 
significantly higher in the area at the front of pre-crack; comparatively, 
as the upper and lower surfaces of pre-crack are free, the stress ampli -
tude in the region near the free surfaces is significantly lower, forming 
an unloading zone. Furthermore, Fig. 7 (b) demonstrates that stress 
concentration occurs in the pre-crack tip, and the corresponding stress 
distribution accords well with the theoretical analysis [ 54 , 55 ]. It is 
worth noting that although the stress measured in the fixtures is still far 
below the yielding stress of alloys, the stress amplitude within the 
pre-crack tip has exceeded the yielding stress, i.e., a local small plastic 
deformation zone occurs, and this phenomenon is also consistent with 
Orowan ’ s theoretical analysis [ 54 ], where the zone is usually called 
‘plastic zone ’ . 
As the loading continues, the plastic zone expands gradually. The 
von-Mises effective stress distribution in front of the pre-crack tip at s =
70 nm is shown in Fig. 7 (c), from which it can be found that the stress 
distribution is similar to that in Fig. 7 (b), however, the range with high 
stress expands significantly. It is also worth noting that the crack does 
not still begin to propagate at this time, i.e., the energy from external 
loading is mainly used for plastic deformation of materials at the pre- 
crack tip during this stage. Moreover, the plastic deformation will act 
as a relaxation stress, and it may lead to a stagnation point in the stress- 
displacement curve in the experimental results [ 56 ]. Besides, Fig. 7 (b – c) 
also show that because the yielding stress of the precipitate phase is 
higher, the stress amplitude in the precipitate particles within the plastic 
zone is significantly higher than that in the matrix, reflecting the 
strengthening effect of precipitate particles. 
Because of the continuous expansion of plastic zone at the crack tip 
during the loading process, materials within a broad region at the pre- 
crack tip begin to yield gradually, and eventually the crack start to 
propagate in an elastic-plastic fracture manner. Similarly, the distribu -
tion of effective plastic strain with the specimen in the case of V
V 
= 30% 
& t
2 
& r
a 
= 0
◦
during the early stage of crack propagation is listed in 
Fig. 8 (a), and the deformation and failure morphology in the case of V
V 
= 60% & t
3 
& r
a 
= 45
◦
during the middle stage of crack propagation is 
shown in Fig. 8 (b). It is seen from Fig. 8 (a) that the crack tip blunts 
significantly, and a large plastic zone is indeed formed in the front of 
crack tip; besides, the effective plastic strain is higher in the region near 
the crack tip, comparatively, it decreases gradually as the distance from 
the crack tip increases, and it drops to zero on the boundary plastic zone. 
Similar deformation feature is also observed in the real tests, Fig. 8 (c) 
shows an optical microscopy (OM) image of AM1 Ni-based superalloys 
specimen in the early stage of crack propagation. [ 57 ], from which it is 
seen that there is indeed an obvious plastic zone around the crack tip, 
and the morphology consists with that in the simulation result in Fig. 8 
(a). Furthermore, Fig. 8 (a) also shows that the plastic deformation 
within the specimen behaves as the propagation of deformation bands, 
and the bands extend along the direction of about ± 45
◦
when the crack 
propagates, almost being consistent with the maximum shear stress 
plane (see Fig. 7 (c) and Ref. [ 58 ]). 
Regarding to real alloys, the plastic deformation is derived from the 
dislocation movement, and the nucleation and propagation of defor -
mation bands are closely related to the nucleation, multiplication and 
movement of dislocations within materials. Besides, for the precipitate 
strengthening alloys, such as Ni-based superalloys, the precipitate par -
ticles usually play as a series of junction barriers, which interact with 
dislocations and impede their movement. There are mainly three ways 
in which dislocations overcome the obstruction of precipitates: directly 
cutting through particles, bypassing particles by the Orowan mecha -
nism, and bypassing particles by climbing [ 59 ], and the movement of 
dislocations usually behaves as bypassing by Orowan mechanism within 
the microstructure with phase coarsening [ 14 ]. The simulation results in 
Fig. 8 (a – b) and experimental investigations in Fig. 8 (d – e) [ 60 , 61 ] 
indeed demonstrates such deformation mechanisms, it is seen that a lot 
of dislocations pile up in the matrix around the precipitate particles; 
moreover, the movement of dislocations and the propagation of crack 
indeed do not cut directly into the particles, whereas bypass the parti -
cles, and this phenomenon accords with the authors ’ previous analysis 
[ 29 – 32 ]. 
Specifically, our previous work [ 29 – 32 ] demonstrated that the 
amplitude of effective plastic strain in the FEM simulations corresponds 
to the dislocation density in the real material, i.e., higher plastic strain 
corresponds to higher dislocation density. Hence, based on the devel -
opment of plastic strains in the FEM simulation, the nucleation and 
movement characteristics of dislocations in real materials can be 
extrapolated. 
Fig. 7. Stress evolution in the specimen with V
V 
= 30% & t
2 
during the Mode I tear test with loading direction of r
a 
= 0
◦
. 
S. Zhang et al.

## Page 8

Materials Science & Engineering A 889 (2024) 145852
8
3.3. Stress-displacement curve 
The stress-displacement curves corresponding to specimens with 
different microstructures are listed in Fig. 9 , where the stress is taken 
from the upper surface of Fixture 1. For comparative analysis on the 
influence of microstructure, only the curve before the crack runs 
completely through representative zone (the red area in Fig. 1 ) are 
shown. It can be found that an obvious stagnation point occurs in the 
curve during the early stage, and the stress amplitude at the stagnation 
point is far less than the yielding stress of materials. This is consistent 
with the above analysis, i.e., a part of the energy from external loading is 
dissipated by local plastic deformation in the early stage. In addition, the 
stress amplitude decreases gradually when the crack begins to propa -
gate, and the curve displays a certain serrated vibration feature, which is 
related to the dynamic strain aging (DSA) effect within the material, and 
it is also correlated to the interaction between the crack and the 
microstructure of alloys [ 29 – 32 ]. 
Fig. 9 shows that the peak value of stress amplitude increases with 
increasing the volume fraction of precipitate V
V
, and this is mainly 
derived from the strengthening effect of precipitate particles. For the 
alloys with the same V
V
, the peak value decreases as the aging time t
a 
increases, implying that the strengthening effect of precipitate is grad -
ually weakened along with the phase coarsening. Besides, as the size of 
particles increases, the time the crack runs through the representative 
zone moves up, and the duration of crack propagation is much shorter 
corresponding to the higher V
V 
value. Furthermore, regarding the cases 
with relatively long aging time ( t
2
, t
3
), the variation of stress becomes no 
longer stable at a certain moment before the crack runs through the 
representative zone completely, and it shows a sudden drop, and then a 
vibration further occurs in the stress-displacement curve during the 
Fig. 8. Plastic zone around the crack tip and propagation path of crack within the microstructure under the Mode I tear test. 
Fig. 9. Stress-displacement curves corresponding to different microstructures in the Mode I tear tests with the loading direction of r
a 
= 0
◦
. 
S. Zhang et al.

## Page 9

Materials Science & Engineering A 889 (2024) 145852
9
subsequent stage. Specifically, as the aging time t
a 
increases, the sudden 
drop in the curve becomes more remarkable, and the drop point also 
moves forward, indicating that the crack propagation is more unstable. 
The time at which the crack runs completely through the representative 
zone is closely related to the sudden drop point of stress curve, and it is 
due to that the path and mode of crack propagation within materials 
changes after the drop point, and it will be analyzed in detail in Section 
4 . 
Similarly, the stress-displacement curves corresponding to the same 
microstructure and different loading directions are also obtained. The 
simulation results indicate that regarding the material with the early 
phase coarsening stage ( t
1
), the curves under three loading directions 
are almost the same for both volume fraction values. Comparatively, for 
materials with the middle ( t
2
) and late ( t
3
) phase coarsening stages, the 
curves under different loading directions are different from each other, 
as seen in Fig. 10 . Similar anisotropic characteristics are also observed in 
real tests, e.g., regarding to GH3536 Ni-based alloy after phase coars -
ening, the load-displacement curves in the tension test under different 
loading directions deviate with each other significantly [ 34 ]. It can be 
found from Fig. 10 that in the conditions of r
a 
= 45
◦
and 90
◦
, the vari -
ation of crack propagation characteristic along with the increase of V
V 
and t
a 
values are similar to that in the case of r
a 
= 0
◦
, i.e., phase 
coarsening is easily to induce that the crack runs through the repre -
sentative zone early under all loading directions. In addition, for the 
cases with the same microstructure but different loading directions, the 
stress-displacement curves are consistent with each other during the 
early stage (before the sudden drop of stress amplitude); comparatively, 
when the sudden drop occurs, the drop points are different from each 
other, and the variation characteristics of curve after the sudden drop 
are also different, as shown in Fig. 10 . 
In the following, the effect of loading direction on the stress- 
displacement curve corresponding to the same microstructure will be 
analyzed in detail. Regarding the material with V
V 
= 30%, the time the 
crack runs through the representative zone moves becomes earlier 
gradually as the loading angle increases; Besides, the effect of phase 
coarsening on the stress drop tendency and the sudden drop point is 
different corresponding to different microstructures, it is seen that for 
materials with middle phase coarsening stage, the sudden drop point of 
stress curve is relatively late under the direction of r
a 
= 45
◦
, compara -
tively, for materials with late phase coarsening stage, the gently period 
in the curve lasts relatively under r
a 
= 90
◦
; It is also worth noting that 
the stress amplitude during the later stage is slightly higher in the 
condition of r
a 
= 45
◦
compared with that of r
a 
= 0
◦
. It means that the 
fracture toughness of alloys not only depends on the time at which the 
crack runs completely through the representative zone, but also is 
closely related to the sudden drop point in the stress curve. 
Regarding the material with V
V 
= 60%, the variation of mechanical 
behaviors along with the loading direction shows a similar feature to 
that with V
V 
= 30%, however, there are also some differences, e.g., for 
materials with middle phase coarsening stage, the vibration in the stress- 
displacement curve decreases first and then increases gradually with 
increasing in loading angle r
a
, comparatively, for materials with middle 
phase coarsening stage, both the sudden drop point in the stress- 
displacement curve and the time at which the crack runs through the 
representative zone become remarkably earlier in the case of r
a 
= 45
◦
, 
while under r
a 
= 90
◦
the critical time for these two parameters is 
delayed. Hence, it is known that there are several factors determining 
the fracture toughness, especially the microstructure of alloys is very 
Fig. 10. Stress-displacement curves corresponding to different microstructures in the Mode I tear tests with different loading directions. 
S. Zhang et al.

## Page 10

Materials Science & Engineering A 889 (2024) 145852
10
important. 
3.4. Relative fracture energy 
In the following, the fracture toughness of materials corresponding 
to various microstructures and loading directions will be analyzed in 
detail. For the Mode I tear test, the total area of envelope under the 
stress-displacement curve reflects the amount of energy consumed by 
the plastic deformation and the crack propagation of materials, and the 
corresponding energy consumption corresponds to the fracture tough -
ness of alloys. Hence, based on the envelope area, the fracture toughness 
of materials with different microstructures and under different loading 
directions can be compared. In the present FEM simulations, the loading 
methods are all set as the uniform motion of the two fixtures, and the 
corresponding stress-displacement curves as well as their envelope areas 
are obtained corresponding to different microstructures and loading 
directions. Therefore, in the following the fracture toughness of alloys 
would not be calculated according to the exact formulae, alternatively, 
the envelope area will be used to analyze the fracture energy and the 
corresponding fracture toughness, and the analysis is mainly based on 
the non-dimensional relative parameters. 
Regarding the stress-displacement curves corresponding to various 
microstructures at r
a 
= 0
◦
(as shown in Fig. 9 ), related envelope areas 
are calculated by the integration method. Then the largest area (corre -
sponding to the V
V 
= 30% & t
1 
material) is selected as the reference 
value, and thus the corresponding relative fracture energy can be ob -
tained by dividing the other area values with the reference one. The 
corresponding relative fracture energy is listed in Fig. 11 (a), and it can 
be seen that it decreases gradually with increasing aging time, i.e., phase 
coarsening weakens the fracture toughness of alloys; besides, the rela -
tive fracture energy decreases more significantly in the case of larger V
V 
value, indicating that the effect of the precipitate phase increases with 
increasing its volume fraction. Therefore, it is known that the variation 
of fracture toughness is dominated by the sudden drop point in the stress 
curve under this loading condition. 
In the following the effect of loading direction on the fracture energy 
of alloys will be further analyzed, and the comparative analysis is mainly 
based on the materials with middle and late phase coarsening stages. 
The reference value is still taken as the envelope area of the stress- 
displacement curve in the case of V
V 
= 30% & t
1 
combined with r
a 
=
0
◦
, and the relative fracture energy under different loading directions is 
listed in Fig. 11 (b). It can be found that the variation is not monotonic 
with the increase in loading angle, and the evolution characteristics are 
different from each other corresponding to different microstructures. 
Regarding the V
V 
= 30% material, the various display as an inverted 
‘V ’ shape, and the maximum relative fracture energy occurs at r
a 
= 45
◦
. 
In addition, for materials with the middle phase coarsening stage, the 
fracture energy changes little when r
a 
increases from 0
◦
to 45
◦
, 
comparatively, it decreases significantly when r
a 
further increases from 
45
◦
to 90
◦
. Therefore, the fracture toughness of alloys is affected by 
several factors simultaneously, e.g., the sudden drop point of stress 
curve and the time at which the crack runs completely through the 
representative zone. 
Regarding the V
V 
= 60% material, the variation of fracture energy 
shows a complex relationship with the loading direction. For alloys with 
the middle phase coarsening stage, the variation characteristic is similar 
to that of V
V 
= 30% material, only the change of corresponding 
amplitude becomes much more remarkable; however, for alloys with the 
late phase coarsening stage, the variation shows a ‘V ’ shape, and the 
minimum fracture energy occurs at r
a 
= 45
◦
, while the maximum value 
at r
a 
= 90
◦
. It is also worth noting that for alloys with the middle phase 
coarsening stage ( t
2
), the fracture energy of the V
V 
= 60% material 
becomes larger than that of V
V 
= 30% alloy when the loading angle r
a 
exceeds a critical value, namely, there are complex factors contributing 
to the variation in the fracture toughness, and the time at which the 
crack runs completely through the representative zone dominates the 
variation characteristics. Hence, it is known that the fracture toughness 
of Ni-based superalloys demonstrates complex anisotropic characteris -
tics after phase coarsening and the corresponding mechanism will be 
analyzed in detail in Section 4 . 
According to the above analysis, it is seen that related FEM simula -
tions can reflect the variation characteristics of fracture toughness well, 
and related comparative analysis among different microstructures and 
loading directions based on the simulation results could provide prac -
tical references. 
4. Mechanism analysis 
It is known from the above analysis that the precipitate phase as well 
as the corresponding phase coarsening in Ni-based superalloys has a 
significant influence on their fracture toughness, and the loading di -
rection will also affect the fracture characteristics after phase coars -
ening. In general, the fracture toughness of alloys decreases remarkably 
with increasing aging time. Particularly, regarding the alloys with the 
middle and late phase coarsening stages, the fracture toughness displays 
an anisotropic feature, and it also shows a complex relationship with the 
variation of loading direction. 
In the following, the mechanism for the variation of fracture 
Fig. 11. Relative fracture energy corresponding to different microstructures and loading directions. 
S. Zhang et al.

## Page 11

Materials Science & Engineering A 889 (2024) 145852
11
toughness of alloys will be analyzed in detail. As mentioned above, the 
fracture toughness is closely related to the dislocations within materials, 
and the movement of dislocations corresponds in appearance to the 
development of plastic deformation bands, thus related analysis can be 
based on the nucleation and development of plastic deformation bands 
within alloys. Moreover, for the convenience of description of the FEM 
simulation results, the parameter of the plastic deformation band will 
mainly be used in the following analysis. As aforementioned, the 
nucleation and development of plastic deformation bands represent the 
nucleation, multiplication, and movement of dislocations, while the 
amplitude of effective plastic strain corresponds to the degree of dislo -
cation density. 
4.1. Weakening characteristics 
Under the same loading conditions, since the influence of phase 
coarsening on different microstructures is similar to each other, the 
representative microstructure with V
V 
= 60% and the typical loading 
direction of r
a 
= 0
◦
will be selected for related analysis, and the early and 
late phase coarsening stages are chosen for comparative analysis. The 
development of effective plastic strain within the representative zones of 
the two specimens under the Mode I tear test is listed in Figs. 12 and 13 . 
It is seen in Fig. 12 that the plastic zone at the crack tip expands 
forward gradually along with the propagation of the crack, and the 
development of plastic deformation bands is mainly through bypassing 
precipitate particles and interacting with them. This is just the reason for 
the increase in yielding stress along with the increase of the volume 
fraction of precipitate (see Fig. 9 ). Furthermore, several factors, 
including the propagation of crack, the nucleation and development of 
plastic deformation bands as well as the interaction with the particles, 
and the stress relaxation in the plastic zone at the crack tip, etc., will 
induce certain DSA effect, and lead to the vibration characteristics in the 
stress-displacement curves (see Figs. 9 and 10 ). In addition, the propa -
gation of crack will lead to failure in some regions of materials, and it 
results in a certain decrease in the geometric strength of specimens, thus 
it causes the gradual decline feature in the stress-displacement curves 
(see Figs. 9 and 10 ). Besides, the propagation direction of the crack is 
mainly perpendicular to the loading direction, and when the crack en -
counters precipitate particles during the propagation process, it prefers 
to cut directly into the particles due to the small size of precipitate 
particles and the relatively short distance between particles. Finally, the 
crack runs completely through the representative zone at the loading 
displacement of s = 4875 nm ( Fig. (12(d)) . It is also found that the 
overall propagation path of crack is relatively straight, and the fracture 
surface in the specimen is relatively smooth. 
Comparatively, Fig. 13 shows that the propagation of crack is stable, 
and the propagation path is also relatively straight during the early 
stage. It is also worth noticing that the plastic deformation bands 
become wider (see Fig. 13 (a)), indicating that the plastic deformation in 
the material is more easily to occur, and therefore the yielding stress 
decreases to a certain extent ( Fig. 9 (b)). During the late stage, the plastic 
zone further expands, the dislocation plugging within the material be -
comes more serious, and the amplitude of effective plastic strain further 
increases, especially in the area around the larger particles. As the 
loading continues, when the crack tip encounters the particles, the 
propagation of crack becomes more difficult, and failure initiates in the 
matrix around the particles at the crack tip area as well as in the plastic 
deformation bands, thus the stress distribution characteristics in the 
surrounding regions are changed, as shown in the red marked zone in 
Fig. 13 (b). Such deformation features are observed in the real test, e.g., 
Gao et al. [ 36 ] ’ s Mode I tear test showed that several micro-voids occur 
in the area around the crack propagation path, as listed in Fig. 14 (a). 
Similarly, in Takahashi et al. [ 24 ] ’ s Mode I tear test, corresponding to SC 
Ni-based superalloy with lower degree of phase coarsening, no 
Fig. 12. Deformation and failure process of the alloy with V
V 
= 60% & t
1 
and the corresponding distribution of effective plastic strain in the Mode I tear test with the 
loading direction of r
a 
= 0
◦
. 
S. Zhang et al.

## Page 12

Materials Science & Engineering A 889 (2024) 145852
12
micro-void occurs in the front of crack tip within the materials, 
comparatively, in the alloy with higher degree of phase coarsening, 
there are several micro-voids nucleate and grow in the front of crack tip, 
and they mainly initiate within the matrix between the particles, as 
shown in Fig. 14 (b). Besides, it can be found that the morphology of 
micro-voids in the real materials (see Fig. 14 (a and b)) accords with the 
simulation result in Fig. 13 (b) well. 
As the geometrical strength of the specimen decreases gradually, the 
Fig. 13. Deformation and failure process of the alloy with V
V 
= 60% & t
3 
and the corresponding distribution of effective plastic strain in the Mode I tear test with the 
loading direction of r
a 
= 0
◦
. 
Fig. 14. Experimental results in mode I tear test with Ni-based superalloys. 
S. Zhang et al.

## Page 13

Materials Science & Engineering A 889 (2024) 145852
13
propagation path of the crack starts to change, i.e., it propagates towards 
the initiated micro-voids, as shown in the red marked zone in Fig. 13 (c). 
At the same time, the micro-voids in the more distant area grow along 
two directions simultaneously and further develop into micro-cracks, 
and the propagation path follows the ± 45
◦
direction roughly (see 
Fig. 13 (c)). Similar failure feature also occurs in the real tests, e.g., 
Cockeram [ 62 ] ’ s tests demonstrated the nucleation and growth of 
micro-crack in the front of crack tip, as shown in Fig. 14 (c); Takahashi 
et al. [ 24 ] ’ s Mode I tear test also observed similar phenomena, i.e., 
micro-voids connect with each other and further develop into 
micro-crack in the front of crack tip, and the corresponding SEM image 
is listed in Fig. 14 (d). 
During this period, the propagation of the crack becomes unstable 
and the failure of material is also relatively faster, particularly, during 
this unstable propagation process, the initiation and growth of new 
micro-voids in the region far away from the crack tip leads to the 
propagation path of crack continues to change, then the propagation 
process becomes more unstable, and the failure of materials is further 
accelerated. Furthermore, the initiation and growth of micro-voids also 
cause stress relaxation, and thus the required stress for crack propaga -
tion decreases precipitously, i.e., a sudden drop occurs in the stress- 
displacement curve (see Figs. 9 and 10 ). Consequently, the crack runs 
completely through the representative zone of the specimen at the 
loading displacement of s = 3245 nm, and the overall propagation path 
of a crack becomes twisted, and the fracture surface in the specimen is 
no longer smooth, as shown in Fig. 13 (d); besides, the propagation path 
of crack prefers to follow the interface layer, and it seldom cuts directly 
into the particles (see Fig. 13 (d)). Again, this crack propagation feature 
is confirmed by the experimental observation, in Takahashi et al. [ 24 ] ’ s 
Mode I tear test, corresponding to SC Ni-based superalloy after phase 
coarsening, the propagation path of crack is relatively twisted and the 
propagation rate is much fast, and thus the load point displacement at 
which the crack runs through the specimen is remarkably reduced 
compared with that in the situation of alloy without phase coarsening, as 
shown in Fig. 14 (e). 
It is known from the above analysis that after the phase coarsening 
within the alloys, the hindering effect of the coarsened particles on the 
movement of dislocations is strengthened gradually, and thus the 
nucleation and growth of the micro-voids are more easily to occur 
around the coarsened particles at the front of crack tip, and then micro- 
voids connect with each other and further develop into micro-crack. This 
further leads to the change in the propagation direction of crack as well 
as the significant decrease of time that the crack runs through the 
representative zone. Therefore, the fracture toughness of the alloy de -
creases gradually with increasing the degree of phase coarsening, i.e., 
the increase of precipitation particle size is the dominating factor which 
induces the reduction of fracture toughness. 
In the following, the influence of volume fraction will be analyzed, 
and the comparative analysis is based on the materials with the late 
phase coarsening stage ( t
3
). The failure morphology of the representa -
tive zone and the corresponding distribution of effective plastic strain in 
the two kinds of materials at the loading displacement of s = 2260 nm is 
listed in Fig. 15 , from which it is seen that as the matrix region between 
the particles within the material with V
V 
= 30% is larger, the plastic 
deformation bands are relatively wide, thus the corresponding yielding 
stress is lower (see Fig. 9 ); besides, the amplitude of effective plastic 
strain is lower, indicating that the dislocation plugging is gentle, thus the 
propagation of crack is relatively stable, and the distance of transverse 
propagation is short. Hence, the crack would consume more time to run 
through the representative zone. In addition, remarkable blunting oc -
curs at the crack tip within the material with V
V 
= 30%, while the crack 
tip in the material with V
V 
= 60% is relatively sharp and its propagation 
is more rapid. Therefore, as the volume fraction of precipitate increases, 
the propagation of the crack becomes more unstable, and the propaga -
tion speed will be accelerated, thus the crack will consume less time to 
run completely through the representative zone, i.e., the fracture 
toughness of the material decreases. Hence, the development of plastic 
deformation bands within the alloy is closely related to the expansion 
channel in the matrix. Along with the increase of volume fraction of 
precipitate, the number of expansion channels decreases, and the width 
also becomes narrower, eventually it leads to a significant acceleration 
of crack propagation rate. As a result, the increase in the volume fraction 
of precipitate will induce a decrease in the fracture toughness of alloys. 
Therefore, it is known that after the phase coarsening within the 
alloys, the strain amplitude is larger near the precipitation phase, i.e., 
dislocations are more easily to accumulate around the coarsened parti -
cles, and micro-voids are more easily to initiate in these regions. 
Accordingly, the propagation of crack within the material will become 
unstable, and it further leads to the decrease of fracture toughness of the 
alloys. In the following, for comprehensive analysis of the propagation 
feature of cracks, the deleted elements in the FEM simulation results due 
to material failure in the condition of r
a 
= 0
◦
are marked in red, and thus 
the corresponding propagation paths of crack in the initial microstruc -
ture can be obtained and listed in Fig. 16 . For the clarity of the figure, all 
other parts (including the matrix, the precipitate particles and the 
interface layers) are shown transparently, and only the contour lines of 
the particles as well as the interface layers are displayed. 
It is worth noting that when the propagation direction of the crack is 
perpendicular to the loading direction, the nucleation of plastic defor -
mation bands initiates at the crack tip, and then the bands develop along 
Fig. 15. Failure morphology in different microstructures at the loading displacement of s = 2260 nm and the corresponding distribution of effective plastic strain in 
the Mode I tear test with loading direction of r
a 
= 0
◦
. 
S. Zhang et al.

## Page 14

Materials Science & Engineering A 889 (2024) 145852
14
the ± 45
◦
directions. After the crack tip becomes blunt, the propagation 
speed of crack decreases, thus the nucleation and development of plastic 
deformation bands are relatively adequate, i.e., it would take more time 
to achieve the same transverse propagation distance for the crack, and 
the energy consumption for the overall deformation and failure of 
specimen also increases (see Figs. 12 and 13 ). In contrast, the nucleation 
of micro-voids usually initiates around the coarsened particles, and their 
growth is mainly along the developing direction of plastic deformation 
bands; besides, there is little new plastic deformation in the specimen 
during the growth process of micro-voids, indicating that the initiation 
and growth of micro-voids almost don ’ t affect the distribution and 
amplitude of plastic deformation in the vicinity, i.e., the energy con -
sumption in the specimen is relatively low during this process (see 
Fig. 13 ). Similarly, when the crack propagates along the ± 45
◦
direc -
tion, it roughly follows the pre-existing plastic deformation band, with a 
small amount of plastic deformation at the crack tip, while little new 
plastic deformation occurs on both sides of the crack, and at the same 
time, the propagation of crack becomes faster and more unstable (see 
Fig. 13 (d)). 
Therefore, it is known from the above analysis that when the prop -
agation path of crack is perpendicular to the loading direction, there are 
more plastic deformation bands initiated around the crack, and the 
bands achieve adequate development. Comparatively, there is little 
plastic deformation in the surrounding materials when the crack prop -
agates along the ± 45
◦
direction. According to that the energy con -
sumption during the elastic deformation in the specimens with various 
microstructures is similar and relatively low, and the plastic deforma -
tion energy is the main factor inducing the difference between the 
fracture toughness of various materials, hence, the propagation path of 
crack which is perpendicular to the loading direction can be defined as 
the effective crack length ( L
e
). For instance, the effective crack length in 
the specimen with microstructure of V
V 
= 30% & t
2 
and loading con -
dition of r
a 
= 0
◦
is L
e
= L
1
+ L
2
, as shown in Fig. 17 . For the alloys with 
the same volume fraction of precipitate, the larger value of L
e 
corre -
sponds to more time consumption for the crack to run completely 
through the representative zone, thus the nucleation and development 
of plastic deformation bands around the crack are more adequate, and 
the region with plastic deformation bands is also wider, i.e., the energy 
consumption derived from plastic deformation in the specimen increases 
(see Figs. 12 (d) and Fig. 13 (d)). Therefore, it can be inferred that the 
effective crack length is closely related to the nucleation and develop -
ment of plastic deformation bands within the specimen and also the 
fracture toughness of materials, and the fracture toughness increases 
with the increase of effective crack length L
e
. 
In addition, it can also be found from Fig. 16 that for the alloys with 
the early phase coarsening stage, because the precipitate particle is 
small, the possibility of direction changes for crack propagation path 
due to the obstruction of precipitate is small, thus the propagation path 
is relatively straight, and the propagation process is stable, therefore, the 
effective crack length is long, and correspondingly the fracture tough -
ness of the material is relatively high (see Fig. 11 (a)). Besides, though 
the effective crack length is similar in the specimens with the two kinds 
of volume fractions of precipitate, the probability of initiation and 
growth of micro-voids around the particles is higher within the alloy 
with V
V 
= 60%, then the micro-voids connect with each other and 
further lead to micro-cracks, hence, the propagation speed of crack is 
higher, and the time at which the crack runs completely through the 
Fig. 16. Propagation paths of crack within different microstructures in the Mode I tear test with loading direction of r
a 
= 0
◦
. 
Fig. 17. Sketch of effective crack length within the specimen in the Mode I 
tear test. 
S. Zhang et al.

## Page 15

Materials Science & Engineering A 889 (2024) 145852
15
representative zone is earlier (see Fig. 9 ), correspondingly, the fracture 
toughness is lower than that of the alloy with V
V 
= 30% (see Fig. 11 (a)). 
Comparatively, regarding the alloys with the middle phase coars -
ening stage, the propagation path of the crack is also relatively straight 
during the early period, however, in the later stage, due to that micro- 
voids initiate in advance near the crack tip and around the large parti -
cles in the front regions, the propagation direction begins to change, and 
the propagation process also becomes unstable. This induces a remark -
able stress decay, and the crack runs through the representative zone of 
the specimen fast (see Fig. 9 ), thus the effective crack length is consid -
erably reduced (see Fig. 16 ), i.e., the fracture toughness of the alloy 
decreases. 
For the alloys with the late phase coarsening stage, as the particle 
size further increases, micro-voids are more easily to initiate around the 
particles, and the initiating time is also earlier. Consequently, the time 
that the crack propagation becomes unstable gradually moves forward, 
and the propagating speed further increases, thus the time at which the 
crack runs completely through the representative zone decreases 
significantly (see Fig. 9 ), the effective crack length becomes much 
shorter, and the propagation path is much more twisted in the later stage 
(see Fig. 16 ). As a result, the fracture toughness of materials decreases 
significantly, and the decrease amplitude increases along with the in -
crease of volume fraction of precipitate (see Fig. 11 (a)). Hence, the 
fracture toughness is closely related to the effective crack length. 
Therefore, it can be known from the above analysis that the fracture 
toughness of Ni-based superalloys generally decreases along with the 
phase coarsening in the microstructure, and the weakness of fracture 
toughness is more remarkable in the alloy with larger volume fraction of 
precipitate. 
4.2. Anisotropic characteristics 
The above analysis in Section 3 shows that regarding the Ni-based 
superalloys with the middle and late phase coarsening stages, because 
of the long-strip shape of precipitate particles and their queue distri -
bution feature, the fracture toughness of alloys displays complex 
anisotropic characteristics. In this section, the mechanism of anisotropy 
in fracture toughness will be analyzed in detail based on the nucleation 
Fig. 18. Deformation and failure process of the V
V 
= 30% & t
3 
specimen and the corresponding distribution of effective plastic strain in the Mode I tear test with 
different loading directions. 
S. Zhang et al.

## Page 16

Materials Science & Engineering A 889 (2024) 145852
16
and development of plastic deformation bands within the microstruc -
ture. Considering that the various characteristics of fracture toughness 
along with the loading direction is similar in the alloys with V
V 
= 30% 
and V
V 
= 60% & t
2
, while the variation is remarkably different in the 
materials with V
V 
= 60% & t
3 
(see Fig. 11 (b)), hence, in the following 
two kinds of microstructures, V
V 
= 30% & t
3 
and V
V 
= 60% & t
3
, are 
chosen for related analysis. The deformation and failure process of these 
two kinds of specimens as well as the corresponding distribution of 
effective plastic strain in the Mode I tear test with different loading di -
rections ( r
a 
= 0
◦
, 45
◦
, and 90
◦
) are listed in Figs. 18 and 19 , respectively. 
It is found in Fig. 18 that regarding the alloy with V
V 
= 30% & t
3
, the 
coarsened precipitate particles become as long-strip shape with small 
aspect ratio, and the distribution of particles also displays a certain 
queue feature, therefore, the hindering effect of the precipitate phase on 
the movement of dislocations will deviate with each other under 
different loading directions. However, in general, due to that the volume 
fraction of particles is low and their distribution is dispersed, i.e., the 
distance between the particles is relatively large, thus the hindering 
effect of particles is relatively weak, and the dislocation plugging is 
relatively gentle. As r
a 
increases gradually from 0
◦
to 45
◦
(see Fig. 18 
(b)), the direction of long-striped particles as well as their queue 
distribution becomes gradually consistent with the development direc -
tion of plastic deformation bands, correspondingly, the hindering effect 
on the development of plastic deformation bands will become weaker, 
and the amplitude of effective plastic strain decreases, indicating that 
the dislocation plugging phenomenon becomes gentler; besides, the 
initiation and growth of micro-voids seldom occur, and the time the 
crack propagation becomes unstable is relatively late. Therefore, the 
effective crack length is longer, and accordingly the fracture toughness 
of the material becomes higher (see Fig. 11 (b)). Comparatively, when r
a 
further increases from 45
◦
to 90
◦
(see Fig. 18 (c)), the hindering effect on 
the movement of dislocations is strengthened gradually, especially, a 
series of micro-voids begin to initiate and growth in the late stage of 
crack propagation, and thus the failure process of materials is acceler -
ated, correspondingly, the fracture toughness decays gradually (see 
Fig. 11 (b)). Therefore, the fracture toughness of the alloys displays 
anisotropic characteristics, nevertheless, as the distribution of particles 
is relatively sparse and the anisotropy of the shape is slight, the devia -
tion among fracture toughness under different loading directions is 
relatively small. 
Similarly, regarding the alloy with V
V 
= 30% & t
2
, because the de -
gree of phase coarsening is small, most of the precipitate particles almost 
Fig. 19. Deformation and failure process of the V
V 
= 60% & t
3 
specimen and the corresponding distribution of effective plastic strain in the Mode I tear test with 
different loading directions. 
S. Zhang et al.

## Page 17

Materials Science & Engineering A 889 (2024) 145852
17
still keep the spherical or cubic shape, i.e., the anisotropy in the particle 
shape is not remarkable (see Fig. 2 (c)), thus the deviation among the 
hindering effect of particles on the movement of dislocations under 
different loading directions is smaller than that in the alloy with V
V 
=
30% & t
3
. It is worth noting that when r
a 
increases from 45
◦
to 90
◦
, the 
time the crack propagation becomes unstable is gradually advanced, and 
the time the crack runs completely through the representative zone also 
becomes significantly earlier (see Fig. 10 (a)), correspondingly, the 
fracture toughness of alloy decays considerably (see Fig. 11 (b)). 
Consequently, the fracture toughness displays complex anisotropic 
characteristics along with the loading direction. Generally, when the 
loading angle is small ( < 45
◦
), the variation trend of anisotropy is similar 
to that in the alloy with V
V 
= 30% & t
3
, however, the influence of 
loading direction on the fracture toughness is not remarkable; compar -
atively, when the loading angle is large ( ≥ 45
◦
), the decay of fracture 
toughness becomes significant with increasing the loading angle (see 
Fig. 11 (b)). Therefore, the fracture toughness is closely related to the 
time micro-voids initiate within the material. 
Regarding the alloy with V
V 
= 60% & t
2
, the precipitate particles also 
display long-strip shape with small aspect ratio, and the distribution 
shows a rough longitudinal queuing feature (see Fig. 2 (e)). However, 
due to the high volume fraction of precipitate, the particles are densely 
distributed with small spacing, thus the hindering effect of precipitate 
on the dislocation movement is relatively strong. As r
a 
increases from 
0
◦
to 45
◦
gradually, the hindering effect of particles is remarkably 
weakened, especially, when r
a 
= 45
◦
, the propagation of the crack is 
relatively stable, and there are few micro-void initiates in the front of the 
crack, the time the crack runs through the representative zone doesn ’ t 
advance, thus the fracture toughness of the alloy increases significantly 
(see Fig. 11 (b)). When r
a 
further increases from 45
◦
to 90
◦
, the time the 
micro-void initiates in the front of crack becomes earlier gradually, the 
propagation of the crack becomes unstable, and the time the crack runs 
completely through the representative zone advances gradually (see 
Fig. 10 (c)), therefore, the fracture toughness of decays significantly (see 
Fig. 11 (b)). Hence, with increasing the precipitate particle density, the 
hindering effect of particles on the movement of dislocations is 
strengthened gradually, and it leads to a more remarkable anisotropy 
characteristic in the fracture toughness. 
Comparatively, in the alloy with V
V 
= 60% & t
3
, most of the pre -
cipitate particles exhibit as long-strip shape after phase coarsening, and 
the distribution displays as significant longitudinal queuing feature. In 
the loading condition of r
a 
= 0
◦
, the effective plastic strain is relatively 
high, indicating that the dislocation pile-up within the material is 
serious, i.e., the hindering effect of precipitate on the development of 
plastic deformation bands is strong, thus the propagation of crack be -
comes extremely unstable. Besides, due to the additional effect of the 
initiation and growth of micro-voids, the path changes several times 
during the propagation process of the crack, and the tear fracture surface 
in the specimen is relatively rough (see Fig. 19 (a)). Along with the 
gradual increase of r
a 
to 45
◦
, the amplitude of effective plastic strain 
decreases, however, because the aspect ratio of precipitate particles is 
large, and the direction of their queuing arrangement becomes consis -
tent with the propagation direction of plastic deformation bands during 
the late stage, therefore, when the crack encounters the precipitate 
particles, it prefers to change the propagation direction along the plastic 
deformation band, and the propagation along the ± 45
◦
direction be -
comes very easy due to the sharp crack tip. Besides, there are a series of 
micro-voids initiating and growing in the front of crack (see Fig. 19 (b)), 
and it further accelerates the propagation rate of the crack, then the time 
the crack runs through the representative zone becomes significantly 
earlier (see Fig. 10 (d)), and thus the fracture toughness of the alloy is 
significantly reduced (see Fig. 11 (b)). 
As r
a 
continues to increase from 45
◦
to 90
◦
, the hindering effect of 
precipitate particles on the dislocation movement is gradually 
strengthened, and the amplitude of effective plastic strain increases. 
Besides, the initial propagation direction of the pre-crack gradually 
becomes consistent with the direction of the queuing arrangement of 
precipitate particles, thus the propagation of the crack is stable during 
the early stage. Hence, the time the crack propagation becomes unstable 
is relatively late (see Fig. 19 (c)), and the time consumption for the crack 
runs through the representative zone increases gradually (see Fig. 10 
(d)). Therefore, the fracture toughness of the alloy increases gradually, 
and it achieves the peak value at r
a 
= 90
◦
(see Fig. 11 (b)). It is worth 
noting that at r
a 
= 90
◦
, the long-strip shape of precipitate particles and 
their queuing arrangement have a strong hindering effect on the prop -
agation of plastic deformation bands; moreover, because the volume 
fraction of precipitate is high, the expansion channel in the matrix for 
the plastic deformation bands is significantly reduced along the ± 45
◦
direction, and the channel also becomes remarkably narrower. 
Accordingly, many plastic deformation bands prefer to shear directly 
through the precipitate particles (see Fig. 19 (c)), and thus the plastic 
deformation in numerous particles leads to the increase of fracture en -
ergy in the alloy. Comparatively, at the loading direction of r
a 
= 45
◦
, the 
plastic deformation bands prefer to bypass the particles through the 
Orowan mechanism (see Fig. 19 (b)), thus the effective stress is relatively 
low. This phenomenon accords well with the corresponding experi -
mental observation [ 63 ]. Therefore, the distribution characteristics of 
precipitation particles play an important role in the propagation of 
plastic deformation bands, and it is the dominating factor determining 
the variation of fracture toughness under different loading directions. 
Similar to Fig. 16 , the deleted elements in the FEM simulation results 
in the representative zone of specimens corresponding to alloys with the 
middle and late phase coarsening stages and different loading directions 
are also marked in red, and the propagation paths of crack in the initial 
microstructures are obtained and shown in Fig. 20 . 
Fig. 20 (a) shows that in the alloy with V
V 
= 30% & t
2
, the distri -
bution of particles is sparse, when in the loading condition of r
a 
= 0
◦
, the 
propagation of the crack is relatively stable during the early stage, and 
the propagation direction will change in the middle stage due to the 
hindering effect of particles, finally the propagation shifts back into the 
direction perpendicular to the loading direction again, therefore, the 
effective crack length is relatively long and it takes a long time to run 
completely through the representative zone. When at r
a 
= 45
◦
, the crack 
propagation is stable during the early stage and the corresponding dis -
tance is relatively long, however, in the late stage the propagation path 
is changed and leads to rapid fracture due to the initiation and growth of 
micro-voids. Accordingly, the effective crack length is similar to that in 
the case of r
a 
= 0
◦
, i.e., the time consumption for the crack runs through 
the representative zones is almost the same, however, because the time 
the propagation of the crack becomes unstable is later, and the effective 
stress is higher (see Fig. 10 (a)), the fracture toughness of the alloy in -
creases at a certain extent (see Fig. 11 (b)). Comparatively, at r
a 
= 90
◦
, 
the hindering effect of particles on the dislocation movement is 
strengthened, and micro-voids initiate in advance surrounding the par -
ticles near the crack tip, thus the time of unstable crack propagation 
becomes earlier gradually, and the effective crack length decreases, 
consequently, the fracture toughness of the alloy decays significantly 
(see Fig. 11 (b)). 
It is found from Fig. 20 (b) that the various characteristics of fracture 
toughness in the alloy with V
V 
= 30% & t
3 
are similar to that with V
V 
=
30% & t
2
. However, as the size of particles becomes larger, and their 
hindering effect of dislocation movement is strengthened, the initiation 
and growth of micro-voids become easier, and thus the effective crack 
length decreases, and it further leads to lower fracture toughness 
compared with that of the alloy with V
V 
= 30% & t
2
. Besides, due to that 
the aspect ratio of particles being larger, and the queuing distribution 
being more remarkable, thus their hindering effect on the propagation of 
plastic deformation bands is stronger, and it further leads to that the 
variation of fracture toughness along with the loading direction becomes 
more significant (see Fig. 11 (b)). Hence, the fracture toughness of alloys 
is closely related to the effective crack length and the initial point at 
which the propagation direction of crack first changes. 
S. Zhang et al.

## Page 18

Materials Science & Engineering A 889 (2024) 145852
18
Regarding the alloys with V
V 
= 60%, the anisotropic characteristics 
of fracture toughness are more complex. Fig. 20 (c) shows that the 
propagation feature of crack in the alloy with V
V 
= 60% & t
2 
is similar to 
that with V
V 
= 30% & t
3 
(see Fig. 11 (b)). At r
a 
= 0
◦
, the crack propa -
gation is stable in the early stage, and the propagation path is more 
twisted during the late stage. When r
a 
= 45
◦
, the hindering effect of 
particles on crack propagation is relatively small, and the propagation 
direction is almost perpendicular to the loading direction, thus the 
propagation path is relatively straight, and the effective crack length is 
longer, leading to relatively high fracture toughness. When r
a 
further 
increases to 90
◦
, the time the propagation becomes unstable becomes 
earlier, and the effective crack length decreases, thus the fracture 
toughness decreases gradually, and the decay is relatively significant 
(see Fig. 11 (b)). Hence, it can be known that with increasing the volume 
fraction of precipitate, the influence of particles on crack propagation is 
strengthened, and the anisotropy of fracture toughness in the alloy 
becomes much more remarkable. 
Comparatively, it is found from Fig. 20 (d) that unlike the other three 
microstructures, in the alloy with V
V 
= 60% & t
3 
most of the precipitate 
particles display as elongated strips, and their distribution displays a 
significant queuing feature. Correspondingly, the propagation of crack 
shows an opposite pattern of variation along with the loading angle. At 
r
a 
= 0
◦
, the hindering effect of particles on dislocation movement is 
strong, and the propagation direction of crack is easy to be changed 
when it encounters the particles, thus the propagation direction changes 
many times and correspondingly the propagation path is relatively 
twisted. As r
a 
= 45
◦
, the time the crack propagation becomes unstable is 
significantly earlier, besides, due to that the queuing arrangement of 
particles is the same as the propagation direction of plastic deformation 
bands, the crack prefers to propagate quickly along the interface layer of 
the precipitate particles located in the plastic deformation bands after its 
propagation direction is changed. Hence, the time the crack runs 
Fig. 20. Propagation paths of crack within different microstructures in the Mode I tear test with various loading directions. 
S. Zhang et al.

## Page 19

Materials Science & Engineering A 889 (2024) 145852
19
completely through the representative zone becomes significantly 
earlier (see Fig. 10 (d)), and the effective crack length is remarkably 
reduced, resulting in a significant decrease in the fracture toughness of 
the alloy. At r
a 
= 90
◦
, the pre-crack propagates directly along the 
interface layer of particles with long-strip shape in the early stage, the 
propagation is relatively stable and the time it becomes unstable is 
relatively late, thus the effective crack length increases remarkably, 
therefore, the fracture toughness increases significantly and achieves the 
maximum value (see Fig. 11 (b)). Hence, the initiating time of micro- 
voids, i.e., the initial point at which the propagation direction of crack 
first changes, and the crack propagation rate, dominates the variation of 
fracture toughness. 
Consequently, it can be known from the above analysis that after 
phase coarsening in the microstructure of Ni-based superalloys, their 
fracture toughness displays anisotropic characteristics gradually, and it 
shows complex variation features along with the loading direction, and 
it is closely related to the number, shape, size, and distribution feature of 
precipitate phase within the material. Generally speaking, when the 
volume fraction of precipitate is low, the fracture toughness of alloys 
with middle and late phase coarsening stages increases first with the 
increase of loading angle, and it achieves the maximum value at r
a 
=
45
◦
, then the fracture toughness decreases gradually with increasing the 
loading angle. Regarding the higher volume fraction of precipitate, the 
fracture toughness of alloys with middle phase coarsening stage is 
similar to that of alloys with lower volume fraction of precipitate; 
comparatively, the fracture toughness of alloys with late phase coars -
ening stage displays an opposite variation feature, and it achieves the 
minimum value at r
a 
= 45
◦
, and the main reason is that the crack is easy 
to propagate quickly along the precipitate particles which with queuing 
arrangement after its propagation direction is changed, and then it 
quickly runs through the representative zone of specimen, resulting in a 
significant reduction in the effective crack length. Hence, it can be 
deduced that the high fracture toughness of Ni-based superalloys de -
pends on an optimum combination of the volume fraction and size of 
precipitate particles, and it is also closely related to the loading 
direction. 
5. Discussions 
The above analysis demonstrates that the present FEM simulations 
can represent the main variation characteristics of fracture toughness in 
Ni-based superalloys, and the fracture toughness is sensitive to their 
microstructure characteristics and the loading direction. It is also worth 
noting that the simulations are based on 2-D scaled models, and only in 
the representative zone of specimens the inhomogeneous property of 
microstructure is considered. The simulation results mainly focus on the 
physical mechanism for the variation of fracture toughness in the alloys 
derived from phase coarsening. The corresponding simplification in 
FEM models is mainly due to the limitations of calculation amount and 
solution time in the software. To analyze more accurately the variation 
of mechanical properties in materials based on numerical simulations, 
numerical models with much larger scales and finer meshes need to be 
established, e.g., 3-D FEM models, and it will lead to a dramatic increase 
in the computation cost. Furthermore, by changing the parameters of the 
constitutive model in the FEM simulations (see Table 1 ), the influence of 
the properties in various phases (precipitate, matrix and interface layer, 
etc.) on the fracture toughness of Ni-based superalloys could be dis -
cussed in more detail. In addition, by considering the strain rate in the 
constitutive model, the strain rate effect on the mechanical properties of 
alloys can also be investigated. More accurate FEM simulations and 
more detailed discussions will be conducted in our future work. 
6. Conclusions 
In this study, the variation of fracture toughness in Ni-base super -
alloys after phase coarsening is deeply investigated. Regarding to alloys 
with variation microstructures, numerical simulations of the Mode I tear 
test under different loading directions are systematically conducted 
based on the mesoscale FEM simulations which can establish ‘structure- 
property ’ relationship in materials, and the variation characteristics of 
fracture toughness as well as the anisotropy due to phase coarsening are 
analyzed in detail integrated with the mechanism of dislocation move -
ment. From the above research, the following conclusions can be drawn: 
(1) Precipitate particles have a significant effect on the fracture 
toughness of Ni-based superalloys. The increase in their volume 
fraction will lead to a decrease in the fracture toughness. Espe -
cially, after phase coarsening, the fracture toughness further de -
cays and displays anisotropic characteristics gradually, and it 
shows complex variation features along with the loading direc -
tion. When the volume fraction of precipitate is low, or the degree 
of phase coarsening is not high enough, the fracture toughness of 
alloys increases first and then decreases gradually along with the 
increase in loading angle, and it achieves the maximum value at 
r
a 
= 45
◦
. In comparison, for the alloys with a high volume frac -
tion of precipitate and a high degree of phase coarsening, the 
variation of fracture toughness along with the loading direction 
displays a ‘V ’ -shape feature, and the maximum value is obtained 
at r
a 
= 90
◦
. 
(2) The variation characteristics of fracture toughness are closely 
related to the microstructural evolution within the Ni-based su -
peralloys, particularly the shape, size and distribution of precip -
itate particles. Changes in the microstructure or loading direction 
will lead to different dislocation behaviors within the alloy, 
including the nucleation, multiplication and movement charac -
teristics. After phase coarsening, the hindering effect of precipi -
tate particles on the dislocation movement is strengthened, the 
dislocation plugging within the material is more serious, and the 
initiation of micro-voids at the crack tip is easier, eventually it 
weakens the fracture toughness of alloys, especially, corre -
sponding to the larger precipitate particle, the time the crack 
propagation becomes unstable is earlier, and thus the fracture 
toughness is lower. In addition, under different loading di -
rections, the hindering effect of precipitate particles after phase 
coarsening, which with long-strip shape and queuing distribu -
tion, on the dislocation movement is different, and consequently 
the fracture toughness displays an anisotropy feature. 
(3) The numerical simulation results can represent well the main 
variation characteristics of fracture toughness in the alloys after 
phase coarsening, and the corresponding approach is of signifi -
cance in the engineering practice, e.g., the evaluation and pre -
diction of safety performance of Ni-based superalloys 
components during their service process, microstructural design 
of Ni-based superalloys in the manufacture, etc. 
CRediT authorship contribution statement 
Shunyong Zhang: Methodology, Formal analysis, Investigation, 
Data curation, Writing – original draft. Jianfeng Zhao: Writing – review 
& editing, Data curation, Formal analysis, Validation. Yanxiang Liang: 
Writing – review & editing, Investigation, Visualization. Jicheng Li: 
Conceptualization, Formal analysis, Resources, Writing – review & 
editing, Supervision, Project administration, Funding acquisition. 
Xicheng Huang: Visualization, Validation, Writing – review & editing. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
S. Zhang et al.

## Page 20

Materials Science & Engineering A 889 (2024) 145852
20
Data availability 
No data was used for the research described in the article. 
Acknowledgements 
The project is supported by National Natural Science Foundation of 
China (12072333) and Outstanding Young Scientist Foundation of 
Sichuan Province of China (2023NSFSC1913). 
References 
[1] R.C. Reed, The Superalloys: Fundamentals and Applications, Cambridge University 
Press, Cambridge, 2008 . 
[2] Z. Wan, L. Hu, Y. Sun, T. Wang, Z. Li, Hot deformation behavior and processing 
workability of a Ni-based alloy, J. Alloys Compd. 769 (2018) 367 – 375, https://doi. 
org/10.1016/j.jallcom.2018.08.010 . 
[3] Y. Liu, J. Shi, Epitaxial growth and stray grain control toward single-crystal 
metallic materials by additive manufacturing: a review, Adv. Eng. Mater. (2023), 
2201917, https://doi.org/10.1002/adem.202201917 . 
[4] A. Baldan, Review Progress in Ostwald ripening theories and their applications to 
nickel-base superalloys Part I: Ostwald ripening theories, J. Mater. Sci. 37 (2002) 
2171 – 2202, https://doi.org/10.1023/A:1015388912729 . 
[5] A. Baldan, Review Progress in Ostwald ripening theories and their applications to 
the γ ′ -precipitates in nickel-base superalloys Part II Nickel-base superalloys, 
J. Mater. Sci. 37 (2002) 2379 – 2405, https://doi.org/10.1023/A:1015408116016 . 
[6] K.G. Wang, G.Q. Wang, E. Gamsj ¨ager, M.E. Glicksman, A comparison of theory and 
simulation with microgravity experiments on phase coarsening, Acta Mater. 221 
(2021), 117402, https://doi.org/10.1016/j.actamat.2021.117402 . 
[7] H. Yan, K.G. Wang, M.E. Glicksman, Microstructural coarsening in dense binary 
systems, Acta Mater. 233 (2022), 117964, https://doi.org/10.1016/j. 
actamat.2022.117964 . 
[8] J. Xu, X. Zhao, W. Li, H. Liu, Q. Yue, H. Duan, Y. Gu, Z. Zhang, Aging process 
design based on the morphological evolution of γ ′ precipitates in a 4th generation 
nickel-based single crystal superalloy, J. Mater. Sci. Technol. 147 (2023) 176 – 188, 
https://doi.org/10.1016/j.jmst.2022.10.072 . 
[9] X. Liu, R. Hu, C. Yang, X. luo, J. Bai, R. Ma, Microstructure evolution and 
strengthening mechanism of γ ′ -strengthening superalloy prepared by laser powder 
bed fusion, Mater. Sci. Eng. A. 871 (2023), 144915, https://doi.org/10.1016/j. 
msea.2023.144915 . 
[10] L. Xiao, Z. Peng, X. Zhao, X. Tu, Z. Cai, Q. Zhong, S. Wang, H. Yu, Microstructure 
and mechanical properties of crack - free Ni - based GH3536 superalloy fabricated 
by laser solid forming, J. Alloys Compd. 921 (2022), 165950, https://doi.org/ 
10.1016/j.jallcom.2022.165950 . 
[11] S. Zhou, M. Hu, C. Li, Q. Guo, L. Yu, H. Ding, Y. Liu, Microstructure-performance 
relationships in Ni-based superalloy with coprecipitation of γ’ and γ’’ phases, 
Mater. Sci. Eng. A. 855 (2022), 143954, https://doi.org/10.1016/j. 
msea.2022.143954 . 
[12] S. Chandra, A. Alankar, M.K. Samal, V.M. Chavan, Insights into fracture behavior 
of Ni-based superalloy single crystals: an atomistic investigation, J. Alloys Compd. 
952 (2023), 169938, https://doi.org/10.1016/j.jallcom.2023.169938 . 
[13] J. Duan, T. An, Y. Gu, H. Yu, B. Gan, X. Lv, J. Qu, J. Du, Z. Bi, Effect of γ’ phase and 
microtwins on the microstructural evolution and mechanical properties of a novel 
Ni – Co base superalloy, Mater. Sci. Eng. A. 865 (2023), 144323, https://doi.org/ 
10.1016/j.msea.2022.144323 . 
[14] B. Sun, T. Zhang, L. Song, L. Zhang, Correlation between secondary γ ′ and high- 
temperature tensile behavior of a powder metallurgy nickel-based superalloy 
EP962NP, Mater. Sci. Eng. A. 866 (2023), 144687, https://doi.org/10.1016/j. 
msea.2023.144687 . 
[15] A. Geranmayeh, M. Malekan, F. Forghani, H. Ghorbani, Microstructural and 
mechanical investigations on the heat treatment rejuvenation of a long-term 
service-exposed GTD-111 Ni-based superalloy, Mater. Sci. Eng. A. 862 (2023), 
144381, https://doi.org/10.1016/j.msea.2022.144381 . 
[16] X.Z. Qin, J.T. Guo, C. Yuan, C.L. Chen, H.Q. Ye, Effects of long-term thermal 
exposure on the microstructure and properties of a cast Ni-base superalloy, Metall. 
Mater. Trans. A. 38 (2007) 3014 – 3022, https://doi.org/10.1007/s11661-007- 
9381-5 . 
[17] P.C. Xia, J.J. Yu, X.F. Sun, H.R. Guan, Z.Q. Hu, The influence of thermal exposure 
on the microstructure and stress rupture property of DZ951 nickel-base alloy, 
J. Alloys Compd. 443 (2007) 125 – 131, https://doi.org/10.1016/j. 
jallcom.2006.09.123 . 
[18] Z.W. Lian, J.J. Yu, X.F. Sun, H.R. Guan, Z.Q. Hu, Temperature dependence of 
tensile behavior of Ni-based superalloy M951, Mater. Sci. Eng. A. 489 (2008) 
227 – 233, https://doi.org/10.1016/j.msea.2008.02.013 . 
[19] J.J. Yu, Z.W. Lian, Z.K. Chu, X.F. Sun, H.R. Guan, Z.Q. Hu, Properties and 
microstructures of M951 alloy after long-term exposure, Mater. Sci. Eng. A. 527 
(2010) 1896 – 1902, https://doi.org/10.1016/j.msea.2009.11.049 . 
[20] B. Li, S.M. Zhang, F.A. Essa, C. Dong, J. Yu, Q. Zhang, Crack propagation and 
microstructural evolution of Ni-based single crystal alloy under shear loads, Rare 
Met. Mater. Eng. 47 (2018) 1370 – 1376, https://doi.org/10.1016/S1875-5372(18) 
30137-1 . 
[21] M.H. Hasan, C. Soi, A. Mirzajavadkhan, S. Rafieian, M. Mehany, Experimental 
study and computer simulation of fracture toughness of Ni base superalloy using 
CT specimen, Int. J. Eng. Mater. Manuf. 3 (2018) 224 – 236, https://doi.org/ 
10.26776/ijemm.03.04.2018.07 . 
[22] Z.X. Wen, Z.F. Yue, Fracture behaviour of the compact tension specimens of nickel- 
based single crystal superalloys at high temperatures, Mater. Sci. Eng. A. 456 
(2007) 189 – 201, https://doi.org/10.1016/j.msea.2006.11.152 . 
[23] R. Firoz, S.K. Basantia, N. Khutia, H.N. Bar, S. Sivaprasad, G.V.S. Murthy, Effect of 
microstructural constituents on mechanical properties and fracture toughness of 
Inconel 718 with anomalous deformation behavior at 650
◦
C, J. Alloys Compd. 845 
(2020), 156276, https://doi.org/10.1016/j.jallcom.2020.156276 . 
[24] Y. Takahashi, D. Kobayashi, S. Fujii, M. Takuma, K. Saitoh, T. Sato, Time- 
dependent crack growth mechanism in Ni-based single crystal superalloys at high- 
temperature, Mater. Sci. Eng. A. 859 (2022), 144179, https://doi.org/10.1016/j. 
msea.2022.144179 . 
[25] S.M. Wen, Z.C. Liu, D. Mi, B.C. Li, S.H. Yang, C. Jiang, Revealing the fatigue crack 
propagation mechanism of a Ni-based superalloy electron beam welded joint 
through in-situ SEM observation, Int. J. Fatig. 162 (2022), 106955, https://doi. 
org/10.1016/j.ijfatigue.2022.106955 . 
[26] S. Sui, J. Chen, X. Ming, S. Zhang, X. Lin, W. Huang, The failure mechanism of 50% 
laser additive manufactured Inconel 718 and the deformation behavior of Laves 
phases during a tensile process, Int. J. Adv. Manuf. Technol. 91 (2017) 2733 – 2740, 
https://doi.org/10.1007/s00170-016-9901-9 . 
[27] Q. Xu, T. Cao, F. Ye, F. Xu, H. Li, X. Fang, J. Zhao, Creep-induced microstructural 
evolution in a nickel-based superalloy designed for advanced ultra-supercritical 
boilers, Mater. Char. 139 (2018) 311 – 318, https://doi.org/10.1016/j. 
matchar.2018.03.008 . 
[28] Z. Yao, J. Hou, Y. Chen, W. Xu, H. Jiang, J. Dong, Effect of micron-sized particles 
on the crack growth behavior of a Ni-based powder metallurgy superalloy, Mater. 
Sci. Eng. A. 860 (2022), 144242, https://doi.org/10.1016/j.msea.2022.144242 . 
[29] J.C. Li, K.G. Wang, Effect of phase coarsening on the mechanical properties of 
alloys: I. Numerical simulations, Eng. Fract. Mech. 201 (2018) 229 – 245, https:// 
doi.org/10.1016/j.engfracmech.2018.06.028 . 
[30] J.C. Li, K.G. Wang, Effect of phase coarsening on the mechanical properties of 
alloys: II. Mechanism analysis, Eng. Fract. Mech. 201 (2018) 246 – 260, https://doi. 
org/10.1016/j.engfracmech.2018.06.026 . 
[31] J.C. Li, K.G. Wang, Influence of phase coarsening on fatigue crack growth in 
precipitate strengthened alloys, Eng. Fract. Mech. 205 (2019) 229 – 252, https:// 
doi.org/10.1016/j.engfracmech.2018.11.029 . 
[32] S.Y. Zhang, J.C. Li, Degradation and anisotropy characteristics of hardness in Ni- 
base superalloys after precipitation phase coarsening, Chin. J. Nonferrous Metals 
32 (2022) 3030 – 3047, https://doi.org/10.11817/j.ysxb.1004.0609.2021-42811 . 
[33] W. Ma, X. Bai, H. Luo, X. Yang, The influence of microstructure on CTOD fracture 
toughness of DZ125 base metal and brazed joint, J. Phys. Conf. Ser. 1653 (2020), 
012032, https://doi.org/10.1088/1742-6596/1653/1/012032 . 
[34] Y. Zhao, B. Gong, Y. Wang, Y. Gu, Effects of microstructure anisotropy on dynamic 
fracture behaviors of a selective laser melting nickel-based superalloy, Mater. Sci. 
Eng. A. 858 (2022), 144133, https://doi.org/10.1016/j.msea.2022.144133 . 
[35] ASTM, Standard Test Method for Vickers Hardness of Metallic Materials, 2003. 
ASTM E92-82e2 . 
[36] Y. Gao, C. Shao, H. Cui, N. Ma, F. Lu, Study on fracture toughness of 617 Ni-based 
alloy welded joint under different elevated temperatures, J. Mater. Res. 35 (2020) 
1790 – 1802, https://doi.org/10.1557/jmr.2020.152 . 
[37] N.R. Jaladurgam, S. Kabra, M.H. Colliander, Macro- and micro-mechanical 
behaviour of a γ ′ strengthened Ni-based superalloy at cryogenic temperatures, 
Mater. Des. 209 (2021), 109954, https://doi.org/10.1016/j.matdes.2021.109954 . 
[38] H. Liu, X. Zhao, Y. Yuan, Y. Dang, W. Li, J. Xu, Y. Cheng, Q. Yue, Y. Gu, Z. Zhang, 
Influence of thermal exposure on microstructural stability and tensile properties of 
a new Ni-base superalloy, J. Mater. Res. Technol. 21 (2022) 4462 – 4472, https:// 
doi.org/10.1016/j.jmrt.2022.11.050 . 
[39] C. Wang, F. Zhang, Y. Wu, L. Zhou, Phase precipitation behavior and its influence 
on mechanical properties of a solid-solution strengthened Ni-based alloy, J. Alloys 
Compd. 931 (2023), 167482, https://doi.org/10.1016/j.jallcom.2022.167482 . 
[40] D. Li, J. Liu, Y. Sun, W.-Q. Huang, N. Li, L. Yang, Microstructure and mechanical 
degradation of K403 Ni-based superalloy from ultra-long-term serviced turbine 
blade, J. Alloys Compd. 957 (2023), 170378, https://doi.org/10.1016/j. 
jallcom.2023.170378 . 
[41] X. Li, X.N. Zhang, C.P. Liu, C.Y. Wang, T. Yu, Z. Zhang, Regular γ / γ ′ phase interface 
instability in a binary model nickel-based single-crystal alloy, J. Alloys Compd. 633 
(2015) 366 – 369, https://doi.org/10.1016/j.jallcom.2015.01.109 . 
[42] Q. Tian, H. Qin, W. Zhang, W. Zhang, H. Li, Q. Du, X. Liu, Evolution of γ ′ 
precipitates in GH4742 superalloy based on complete forging-heat treatment 
process, J. Iron Steel Res. Int. 29 (2022) 1873 – 1885, https://doi.org/10.1007/ 
s42243-022-00782-8 . 
[43] X.Y. Li, H.P. Zhang, J.M. Bai, X.K. Li, J. Jia, C.S. Liu, Y.W. Zhang, J.T. Liu, The 
evolution of γ ′ precipitates and hardness response of a novel PM Ni-based 
superalloy during thermal exposure, J. Alloys Compd. 942 (2023), 168757, 
https://doi.org/10.1016/j.jallcom.2023.168757 . 
[44] W. Zhang, X. Liu, Q. Du, Y. Guo, H. Qin, Q. Tian, M. Zhu, Microstructure evolution 
in GH4742 superalloy by combining hot deformation and heat treatment, J. Mater. 
Res. Technol. 23 (2023) 13 – 35, https://doi.org/10.1016/j.jmrt.2022.12.194 . 
[45] X.Z. Qin, J.T. Guo, C. Yuan, C.L. Chen, J.S. Hou, H.Q. Ye, Decomposition of 
primary MC carbide and its effects on the fracture behaviors of a cast Ni-base 
superalloy, Mater. Sci. Eng. A. 485 (2008) 74 – 79, https://doi.org/10.1016/j. 
msea.2007.07.055 . 
S. Zhang et al.

## Page 21

Materials Science & Engineering A 889 (2024) 145852
21
[46] T. Link, A. Epishin, B. Fedelich, Inhomogeneity of misfit stresses in nickel-base 
superalloys: effect on propagation of matrix dislocation loops, Philos. Mag. A 89 
(2009) 1141 – 1159, https://doi.org/10.1080/14786430902877810 . 
[47] Y. Zhu, Z. Li, M. Huang, Atomistic modeling of the interaction between matrix 
dislocation and interfacial misfit dislocation networks in Ni-based single crystal 
superalloy, Comput. Mater. Sci. 70 (2013) 178 – 186, https://doi.org/10.1016/j. 
commatsci.2012.10.037 . 
[48] Y. Wang, D. Banerjee, C.C. Su, A.G. Khachaturyan, Field kinetic model and 
computer simulation of precipitation of L12 ordered intermetallics from f.c.c. solid 
solution, Acta Mater. 46 (1998) 2983 – 3001, https://doi.org/10.1016/S1359-6454 
(98)00015-9 . 
[49] T. Wang, G. Sheng, Z.-K. Liu, L.-Q. Chen, Coarsening kinetics of γ ′ precipitates in 
the Ni – Al – Mo system, Acta Mater. 56 (2008) 5544 – 5551, https://doi.org/ 
10.1016/j.actamat.2008.07.024 . 
[50] M.A. Meyers, K.K. Chawla, Mechanical Behavior of Materials, Cambridge 
university press, Cambridge, 2008 . 
[51] R.F. Bunshah, Techniques of Metals Research, Interscience Publishers, New York, 
1971. http://cds.cern.ch/record/530363 . (Accessed 12 April 2023). 
[52] M.A. Meyers, Dynamic Behavior of Materials, John wiley & sons, New York, 1994 . 
[53] C. Yeni, M. Kocak, Fracture toughness analysis of laser-beam-welded superalloys 
Inconel 718 and 625, Fatig. Eng. Mater. Struct. 29 (2006) 546 – 557, https://doi. 
org/10.1111/j.1460-2695.2006.01025.x . 
[54] E. Orowan, Fracture and strength of solids, Rep. Prog. Phys. 12 (1949) 185 – 232, 
https://doi.org/10.1088/0034-4885/12/1/309 . 
[55] R.O. Ritchie, J.F. Knott, J.R. Rice, On the relationship between critical tensile stress 
and fracture toughness in mild steel, J. Mech. Phys. Solid. 21 (1973) 395 – 410, 
https://doi.org/10.1016/0022-5096(73)90008-2 . 
[56] J.C. Li, X.W. Chen, F.L. Huang, Inhomogeneous deformation in bulk metallic 
glasses: FEM analysis, Mater. Sci. Eng. A. 620 (2015) 333 – 351, https://doi.org/ 
10.1016/j.msea.2014.10.013 . 
[57] S. Flouriot, S. Forest, G. Cailletaud, A. K ¨oster, L. R ´emy, B. Burgardt, V. Gros, 
S. Mosset, J. Delautre, Strain localization at the crack tip in single crystal CT 
specimens under monotonous loading: 3D Finite Element analyses and application 
to nickel-base superalloys, Int. J. Fract. 124 (2003) 43 – 77, https://doi.org/ 
10.1023/B:FRAC.0000009300.70477.ba . 
[58] B.J. Goodno, J.M. Gere, Mechanics of Materials, Cengage Learning, Stamford, 
2020 . 
[59] M.R. Ahmadi, E. Povoden-Karadeniz, L. Whitmore, M. Stockinger, A. Falahati, 
E. Kozeschnik, Yield strength prediction in Ni-base alloy 718Plus based on thermo- 
kinetic precipitation simulation, Mater. Sci. Eng. A. 608 (2014) 114 – 122, https:// 
doi.org/10.1016/j.msea.2014.04.054 . 
[60] Y.H. Yang, J.J. Yu, X.F. Sun, T. Jin, H.R. Guan, Temperature dependence of impact 
deformation behavior of single crystal Ni based superalloy, Mater. Sci. Technol. 31 
(2015) 1860 – 1866, https://doi.org/10.1179/1743284715Y.0000000037 . 
[61] Y. Takahashi, D. Kobayashi, M. Kashihara, T. Kozawa, S. Arai, Electron- 
microscopic analyses on high-temperature fatigue crack growth mechanism in a Ni- 
based single crystal superalloy, Mater. Sci. Eng. A. 793 (2020), 139821, https:// 
doi.org/10.1016/j.msea.2020.139821 . 
[62] B.V. Cockeram, Fracture toughness testing and toughening mechanisms of some 
commercial cobalt-free hardfacing alloys, Surf. Coat. Technol. 108 – 109 (1998) 
377 – 384, https://doi.org/10.1016/S0257-8972(98)00600-8 . 
[63] S. Chen, H.S. Oh, B. Gludovatz, S.J. Kim, E.S. Park, Z. Zhang, R.O. Ritchie, Q. Yu, 
Real-time observations of TRIP-induced ultrahigh strain hardening in a dual-phase 
CrMnFeCoNi high-entropy alloy, Nat. Commun. 11 (2020) 826, https://doi.org/ 
10.1038/s41467-020-14641-1 . 
S. Zhang et al.
