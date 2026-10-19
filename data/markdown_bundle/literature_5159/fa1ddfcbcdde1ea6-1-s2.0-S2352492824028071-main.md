# 1-s2.0-S2352492824028071-main

<!-- source: D:\总文献\1-s2.0-S2352492824028071-main.pdf -->
<!-- file_sha256: 5b7526de845999a34181d57e16497ec78d546b8127e3bee8cdb6cc3a20ab65ce -->

## Page 1

Study on the tensile behaviour and nano deformation mechanism of 
Nickel-based single crystal superalloys with γ / γ’ structure at atomic scale
Zongxiao Zhu
*
, Hongmiao Zhang , Yingpeng Xu , Bingqi Yi , Jialong Wang , Zihan Sun
School of Mechanical and Electronical Engineering, Lanzhou University of Technology, Lanzhou 730050, China
ARTICLE INFO
Keywords:
Nickel-based single crystal superalloys
Tensile behavior
Molecular dynamics
ABSTRACT
To study the deformation mechanism of Nickel-based single crystal superalloys (NBSC) during tensile process, 
tensile experiments on NBSC are carried out by molecular dynamics to systematically analyze stress-strain, shear 
strain, atomic migration and defect evolution. The effects of the structure of the two phases and the strength -
ening elements on the tensile behavior are analyzed by comparing the pure Ni phase, the pure Ni
3
Al phase and 
the Ni phase containing the strengthening elements Cr and Co from a microscopic view. The results show that the 
interaction between the two-phase structural dislocations during tensile process balances the stress concentration 
and reduces the degree of plastic deformation that occurs within the matrix. The γ / γ’ interface separates the 
strain morphology and inhibits the slip of the shear band between the two phases, resulting in enhanced 
deformation resistance of the matrix. By comparing the three single-phase structures, the γ / γ’ structure has the 
highest yield point. From the shear strain distribution pattern, the portion of the two-phase structure with a 
larger degree of shear strain mainly occurs at the interface as well as at the edge of the matrix.
1. Introduce
Nickel-based single crystal superalloys (NBSC) are extensively used 
in the manufacture of aeroengine and turbine blades of gas turbine as a 
key material for hot side part because they exhibit outstanding thermal 
mechanical properties, corrosion resistance, and strong environmental 
stability under high-temperature environments [1 – 5] . The microstruc -
ture of NBSC is primarily made up of the matrix phase γ (Ni) and the 
strengthening phase γ’ (Ni
3
Al) [6,7] , in which the γ phase is based on Ni 
with a variety of elements, and the γ’ phase is embedded in the γ matrix 
with a cubic structure. γ and γ’ phases are prone to form a co-lattice 
interface due to the similarity of lattice constants and the interface is a 
prominent factor influencing the micromechanical properties of NBSC. 
The tensile test, as a commonly used mechanical property test method, 
can detect the yield strength of alloys and provide effective data for the 
improvement and optimization of alloy materials [8,9] . In addition, 
other structural instabilities could play an important role in the yield 
strength in Ni matrix [10,11] . Therefore, a systematic study of the ten -
sile deformation mechanism of NBSC is necessary.
There have been some achievements in experimental studies of NBSC 
tension. Zhang et al. [12] experimentally studied the 
γ / γ’ -microstructure of NBSC during [001]-oriented tensile creep. The 
outcomes showed that the development of the γ / γ’ -microstructure was 
correlated with the kinetics of the stress morphology during tensile 
process. Xuan et al. [13] researched the impact of hot isostatic pressing 
with regard to the mid-temperature tensile properties of NBSC. The re -
sults showed that Hot isostatic pressing could increase the 
mid-temperature plasticity of NBSC, but the yield strength remained 
unchanged. Tan et al. [14] researched the impact of temperature with 
regard to the microstructural changes of the new NBSC and the corre -
sponding deformation mechanism in tensile experiments. It can be 
found that at 760 
◦
C the disintegration and cross-slip of a/2 < 101 >
dislocations, while at 980 
◦
C shear dislocation pairs controlled the 
mechanism of deformation. Lv et al. [15] researched the tensile prop -
erties and related mechanisms of NBSC. The results showed that the 
main fracture mode changed with increasing temperature, gradually 
evolving from pure shear to microporous stacking fracture.
From the above studies, it can be found that the research on the 
tensile properties of NBSC mainly focuses on the experimental obser -
vation of phenomena, and some of the experimental results are indi -
rectly inferred from the observation of phenomena without direct 
verification. In addition, the experimental investigation process needs to 
consume certain materials and testing resources. However, molecular 
dynamics (MD) simulations can link changes at the nanoscale, dynamic 
* Corresponding author.
E-mail address: 20170021@lut.edu.cn (Z. Zhu). 
Contents lists available at ScienceDirect
Materials Today Communications
journal homepage: www.else vier.com/loc ate/mtcomm
https://doi.org/10.1016/j.mtcomm.2024.110826
Received 28 April 2024; Received in revised form 21 October 2024; Accepted 25 October 2024 
Materials Today Communications 41 (2024) 110826 
Available online 26 October 2024 
2352-4928/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## Page 2

migration and microscopic evolution to mechanical properties, 
providing an efficient reference for experiments and saving time and 
costs [16 – 18] . Chen et al. [19] used MD method to research the tensile 
mechanism and mechanical properties of NBSC, and it is found that 
NBSC exhibits anisotropy in mechanical properties. Yin et al. [20]
analyzed the influence of crystallographic orientation with respect to the 
plastic deformation and mechanical properties of uniaxially stretched 
NBSC two-phase models by MD, and found that the models with 
different orientations exhibited tension asymmetry. The outcomes show 
that the evolution of dislocations and stacking could lead to crystal 
anisotropy. Wang et al. [21] modeled the tensile process of FeNiCrCoCu 
high-entropy alloys by MD and perceived that the FCC structure could be 
transformed into an irregular atomic structure. Li et al. [22] researched 
the tensile deformation of NBSC using MD simulations and found that 
the rise in tensile stress was due to slip accumulation of dislocations. Wu 
et al. [23] researched the impact of Re with respect to the creep behavior 
of NBSC in tension using MD method, and observed that Re could 
improve the resistance to creep of NBSC. Du et al. [24] investigated the 
influence of twin boundaries (TB) as well as temperature with respect to 
the cyclic plasticity of CoCrFeMnNi by MD simulations. The results 
showed that the interaction between some dislocations in CoCrFeMnNi 
led to a large number of lattice disturbances within it. Chen et al. [25]
researched the microstructural development of NBSC under different 
impact velocities by MD simulation. The findings showed that the 
interfacial dislocation network consisting of Stair-rod dislocations can 
resist the development of Shockley dislocations at certain velocities.
From the previous studies, it can be observed that there are fewer 
systematic researches with respect to the mechanical properties of NBSC 
reinforcing elements and interfacial synergies on the mechanical prop -
erties, transitions between crystal structure atoms, displaced atoms as 
well as stress distributions during tensile processes. Therefore, this paper 
establishes the NBSC tensile model of γ / γ’ structure, and systematically 
investigates the NBSC tensile behavior under the synergistic effect of 
reinforcing elements and γ / γ’ interfaces to show the tensile mechanism 
of NBSC from the nanoscale. Due to the DSA (dynamic strain aging) 
effect, alloying elements (Cr and Co) added to the γ phase interact with 
the dislocations [26,27] . This suggests that the DSA effect is related to 
the movement of dislocations and thus has an impact on the micro -
mechanical properties of Nickel-based alloys. Additionally, the pure Ni 
phase, the pure Ni
3
Al phase and the Ni phase with Cr and Co added are 
designed to analyze more deeply the influence in the γ / γ’ structure and 
the enhanced elements on the tensile mechanism. The overall structure 
of the paper is as follows: Section 2 shows the parameters used to 
establish the model and the methodology used. Section 3 analyses the 
deformation mechanism of the two-phase model and makes a compar -
ative analysis with the single-phase model. Section 4 demonstrates the 
conclusions drawn from the study done.
2. Simulation method
2.1. Modeling
NBSC are mainly composed of γ phase and γ’ phase. Some alloying 
elements (Re, Cr, Co, Mo, W, etc.) are enriched in the γ phase, of which 
Cr and Co elements account for a relatively high proportion, and to a 
certain extent, they can have an impact on the alloy properties [28] . 
Referring to the ratios of Cr and Co elements in some widely used NBSC, 
within the range of real alloy element ratios, the ratios of Cr and Co 
elements in the alloy is selected to be 9 % as the parameter for this 
simulation [6,29] . To investigate the two-phase structure of NBSC and 
the influence of strengthening elements on the tensile deformation, a 
pure Ni phase model, a pure Ni
3
Al phase model, a Ni phase model with 
the enhanced elements Co and Cr (NiCrCo phase), and a NiCrCo/Ni
3
Al 
( γ / γ’ ) two-phase model have been established, and the percentage of 
elemental content in each model is shown in Table 1 .
The NBSC tensile model and single-phase tensile model of the FCC 
structure were built using ATOMSK software, and in order to minimize 
the error in dimensions in comparing the simulation results, the four 
models were set to the same dimensions, as shown in Fig. 1 . The various 
components of the tensile simulation are shown in Table 2 , in which 
each model size is 300 Å × 70 Å × 70 Å. To equilibrate the temperature of 
the RVE (Representative volume element) at 300 K, the temperature in 
the RVE is adjusted by means of a Nos ´e-Hoover thermostat [30] before 
the tensile movement, and relaxation is carried out under a 
constant-pressure and constant-temperature (NPT) ensemble. The uti -
lization of periodic boundary conditions in the X, Y and Z directions 
reduces the impact of boundary influences on the modelled outcomes 
[31,32] . In this simulation experiment, a fixed loading strain rate is 
applied in the X-axis direction using the lammps software, and the 
tensile motion is carried out at a setup condition at a strain rate of 10
9 
s
 1 
till the total strain is 30 %. The simulation process outputs data every 
100 steps at a time step of 1 fs, as well as the output is post-processed 
using the visualization software OVITO [33] .
2.2. Setting of potential functions
To accurately reflect the interactions between individual atoms in 
the simulation model, the embedded-atom method potential (EAM po -
tential) [34] and Morse potential [35] are used in this paper. The in -
teractions between Ni-Ni ， Ni-Al ， Ni-Cr, Ni-Co, Cr-Cr, Co-Co and Al-Al 
are described through the EAM potential [36,37] , as shown in formula 
(1): 
Table 1 
Components of each elemental content in the simulation (at%).
Element Ni Al Cr Co
Ni phase 100 % 0 0 0
Ni
3
Al phase 75 % 25 % 0 0
NiCrCo phase 82 % 0 9 % 9 %
γ / γ’ phase 61.5 % 20.5 % 9 % 9 %
Fig. 1. Tensile simulation models of Nickel-based single crystal superalloys. (a) 
axial side view; (b) side view; (c)the unit cell of Ni with Co and Cr; (d)the unit 
cell of Ni
3
Al.
Table 2 
Simulation parameters.
Materials RVE
Dimensions Cubic: 30 nm × 7 nm × 7 nm
Interatomic potential EAM, Morse
Timestep 1 fs
Initial temperature 300k
Strain rate 10
9 
s
 1
Total strain ε 30 %
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
2

## Page 3

E
tot
=
1
2
∑
ij
ϕ
ij
( r
ij
) +
∑
i
F ( ρ
i
)
i
ρ
i
=
∑
j ∕= i
ρ
j
( r
ij
)
(1) 
Where, ϕ
ij 
represents the interatomic pairing potential; the embedded 
potential of atom i is denoted as F
i
; a function of the e-cloud density is 
denoted as ρ
j
; the e-cloud density of other atoms is denoted as ρ
i
; r
ij 
represents the Interatomic distance.
Morse potential can depict the interaction of Al-Co and Al-Cr [38] ， 
as shown in formula (2): 
U
M orse
( r
ij
) = D [ e
 2 α ( r
ij
 r
0
)
 2 e
 α ( r
ij
 r
0
)
] (2) 
Where, D represents the coherence potential, r
ij 
represents the balance 
length between atoms i and j, r
0 
represents the length of separation, and 
the bulk modulus is denoted as α . Table 3 shows the potential energy 
data [39 – 41] .
3. Results and discussion
3.1. Analysis of force and micro deformation
To study the change of mechanical properties of the RVE during 
stretching, the stress-strain curves of the simulation model are plotted 
and the dislocation line morphology at special stages is demonstrated, as 
shown in Fig. 2 . The stress-strain curve reflects three stages. The first 
stage represents the linear growth part of the curve in the range of 
strains from 0 % to 7.4 %, which mainly shows the elastic behavior of 
the RVE in the early stages of tension. Fig. 2 (b) shows the dislocation 
line morphology at 5 % strain, few dislocation lines are generated inside 
the RVE during the elastic phase. The second stage, between 7.4 % and 
8.5 % of strain, is characterized by a sharp decrease in tensile stress. In 
the vicinity of point (c), the internal part of the RVE resists the external 
stresses through elastic deformation, resulting in almost no increase in 
dislocation lines. However, the dislocation lines in the γ and γ’ phases at 
point (d) increase dramatically because this is the intermediate stage of 
stable plastic deformation, and more dislocation lines are generated to 
release the energy generated by the maximum tensile stress, as shown in 
Fig. 2 (c) and (d). The third stage is in the range of 8.5 %-30 % and 
Table 3 
Data for the Morse potential energy.
Atomic 
type
Cohesion energy D 
(eV)
Elastic modulus α 
(Å
 1
)
Equilibrium distancer
0 
(Å)
Al-Co 0.64770 1.68950 2.69700
Al-Cr 0.345413 1.36835 2.98603
Fig. 2. (a) Stress-strain curve, (b) Strain 5 %, (c) Strain 7.4 %, (d) Strain 8.5 %, (e) Strain 15 %, (f) Strain 30 %. The green line indicates the Shockley dislocation, the 
pink line indicates the Stair-rod dislocation, the deep blue line indicates the Perfect dislocation, and the light blue and yellow lines indicate the Frank dislocation and 
the Hirth dislocation, respectively.
Fig. 3. Dynamic variation curves for different dislocation line lengths.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
3

## Page 4

mainly reflects plastic deformation. The dislocation lines are filled inside 
the matrix, new dislocations are continuously generated as tensile pro -
ceeds, and most of the dislocation tend to favor the γ’ reinforced phase 
side, as shown in Fig. 2 (e), which is in agreement with the findings of 
Tan et al. [14] and Chen et al. [19] . In Fig. 2 (f), the influence of the 
interface on the deformation is weakened, and the dislocation line slip 
accumulates and starts to extend towards the γ phase, giving rise to a 
more continuous deformation of the two phases than before. At the same 
time, the dislocations interact more frequently, stabilizing the range of 
fluctuations in stress magnitude.
In conclusion, the mechanical characteristics of NBSC are intimately 
linked to the microstructure deformation. The first dramatic increase of 
dislocation lines appears when the RVE attains the yield point. The yield 
point is correlated with the change in the length of dislocation lines, 
resulting in the length of each type of dislocation line showing different 
trends before and after the yield point.
Fig. 3 shows the trend of dislocation lines with the degree of strain, 
which allows a more intuitive representation of the relationship be -
tween the evolution of dislocation lines and mechanical properties 
during tensile processes. In the elastic phase, only the Perfect dislocation 
line in Fig. 3 (a) is changing drastically. However, the lengths of the other 
types of dislocation lines (Hirth, Frank, Shockley and Stair-rod) are not 
changing much and the length of the total dislocation line is changing 
smoothly as shown in Fig. 3 (b). This reflects the fact that Perfect dis -
locations have a dominant effect on the elastic deformation of the tensile 
process, leading to a linear increase in stress. The total dislocation length 
increases sharply when the stress attains an extreme value, however, 
when the strain reaches near 12 %, there is a tendency for the total 
dislocation line length to decrease, as shown in region 1 in Fig. 3 (b). 
These significant changes in the trend before and after the yield point 
indicate that there is a sign of change in the deformation stage of the 
RVE, which shows that the RVE has changed from the elastic deforma -
tion stage to the plastic deformation stage. Throughout the deformation 
process, Shockley dislocations make up the largest proportion of the 
tensile process, and the change in the length of the total dislocation line 
is mainly dominated by the length of the Shockley dislocation line, so 
the Shockley dislocations also show a tendency to decrease at a strain of 
12 %. However, the length of the Stair-rod dislocation line raises at this 
point, suggesting that the Stair-rod dislocation inhibits the development 
of the Shockley dislocation. With the tensile exercise, the Stair-rod 
dislocation is second only to the Shockley dislocation in length. When 
the plastic deformation stage is attained, the fluctuation in the length 
change of the Hirth dislocation line is the largest compared to the Frank 
dislocation and Perfect dislocation. Meanwhile, the stresses in the plastic 
phase oscillate due to the interaction between dislocations. Therefore, 
the interaction between dislocations in the two-phase structure while 
the tensile process balances the stress concentration and reduces the 
degree of plastic deformation that occurs within the matrix.
In tensile process of NBSC, the difference between the two phases 
inside the RVE causes a special phenomenon in the von Mises stress. To 
explore the stress variation inside the RVE, the scattered data of von 
Mises stress values at different stages and the stress variation cloud map 
were selected as shown in Fig. 4 , where the number of scattered points 
represents the magnitude of the stress. It can be seen that there is quite 
different in the von Mises stress distribution between two phases, with 
the stress values within the γ phase appearing rapidly and showing large 
values in the early stages of stretching, while the γ’ phase has lower 
stress values, as shown in Fig. 4 (a). It indicates that the γ phase is sub -
jected to much more stress than the γ’ phase. When the RVE is stretched 
to the elastic limit, the stress value of the γ’ phase shows a dramatic rise 
in magnitude, and the stress value of the γ phase gradually transitions to 
the γ’ phase, but it can still be seen that the γ phase is subjected to much 
more stress than the γ’ phase, as shown in Fig. 4 (b). Therefore, it can be 
deduced that the γ phase is more prone to strain compared to the γ’ 
phase at the same strain. When the elastic deformation exceeds the 
critical point, then the value in the region of stress concentration inside 
the RVE show a slight decrease, and the discrepancy between the stress 
values of γ phase and γ’ phase is not significant. This is because after the 
RVE reaches the elastic limit, the nano deformation between the two 
phases is more continuous than before, which reduces the stress con -
centration as shown in Fig. 4 (c). Besides, the degree of strain occurring 
in the two phases at the same time during RVE stretching varies, as 
shown in Fig. 4 (d)-(l). At the early stage of stretching, the γ phase is the 
first to strain and the strain region of the γ phase is more scattered, while 
Fig. 4. Dynamic changes in the distribution of von Mises stress in RVE during stretching.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
4

## Page 5

the γ’ phase strains relatively later and the strain region is relatively 
concentrated. When stretching the RVE is continued, the strain 
morphology of the γ’ phase is more uniformly distributed and regular 
compared to the γ phase. When stretching reaches a later stage, the in -
fluence of γ / γ’ interface on the tensile properties is gradually weakened, 
leading to the phenomenon of irregular distribution of the strain region, 
and the strain pattern is more scattered compared with the previous 
stage. Therefore, the interface has a hindering effect on the transfer of 
von Mises stresses during the stretching process, separating the strain 
appearance of the two phases. Especially when the RVE reaches the 
elastic limit, the difference in the strain appearance of the two phases is 
more obvious.
To visualize the deformation of the RVE during the tensile stress 
more obviously, the morphological graph of shear strain was extracted, 
as shown in Fig. 5 . In Fig. 5 (a) and (b), the shear strains that occur are 
small and these strains essentially develop along a 45
◦
shear band. It is 
not until the strain reaches 13 % that the atomic distributions of shear 
strain in two phases begin to show a more pronounced difference. The 
shear band changes at the interface and higher shear strain atoms 
appear, which shows that the interface begins to be disrupted, as shown 
in Fig. 5 (c) and (d). As the tensile motion continues, the region of high 
shear strain concentration gradually increases, and the shear notch at 
Fig. 5. Shear strain maps for the specific region.
Fig. 6. Development of defects during tensile process.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
5

## Page 6

the interface becomes more and more obvious, however, there are few 
high shear strain bands in two phases, as shown in Fig. 5 (e) and (f). In 
summary, the deformation that occurs inside the matrix during the 
initial stage of stretching is dominated by elastic deformation. With the 
continuous loading of the tensile movement, the stresses continuously 
act to cause deformation inside the workpiece. The presence of the 
interface blocks the conduction of shear strain between the two phases, 
resulting in significant plastic deformation at the interface. Additionally, 
the shear strain will change the slip direction when it encounters the 
interface, so that part of the shear strain is conducted to the edge of the 
workpiece, resulting in a small amount of plastic deformation at the 
edge of the workpiece as well. But the high shear strain at the interface is 
more obvious. The outcomes indicate that the presence of the γ / γ’ 
interface inhibits the slip of the shear band between the two phases, 
resulting in enhanced deformation resistance of the matrix.
3.2. Defect morphology and displacement trends
The matrix undergoes elastic and plastic deformation during tensile 
process. Plastic deformation is permanent and usually involves the 
movement of dislocations. Dislocations (crystal defects) can be 
expressed by the structure of the HCP composition. To study the 
microscopic deformation of the two-phase defects during the tensile 
process, the dynamics of the γ / γ’ model is analyzed using Common 
Neighbor Analysis (CNA), as shown in Fig. 6 , where the blue atoms show 
the BCC structural atoms, the white atoms show amorphous atoms and 
atoms of the plastically deformed layer, and the red atoms show the HCP 
structural atoms. From Fig. 6 (a1) - (a4), most of the defects appear in 
the γ phase during the tensile process, while merely a few defects 
penetrate into the middle of the γ’ phase. As tensile motion proceeds, a 
plenty of defects occur in both the γ phase and the γ’ phase, and the 
defects fill the entire RVE, at which point the strain is 10 %, as shown in 
Fig. 6 (b1) - (b4). This is because after the stress reaches the yield point, 
the defects slip and heap up at the γ / γ’ interface, accumulating to a 
certain extent leading to the destruction of the structure of the two- 
phase interface, inducing the weakening of the barrier influence of the 
interface on the defects. In Fig. 6 (c1) - (c4), atomic clusters inside the 
RVE also start to appear, which is due to the fact that some of the 
energetically unstable atoms in the γ’ phase are captured by the defect 
clusters to form atomic clusters. Meanwhile, the interface separates the 
defect evolution of the two phases. Furthermore, the fracture of defects 
in the I region of the γ phase disappears due to the energy generated by 
the disruption of the interface, but the γ’ phase gradually shows a slip 
accumulation.
Fig. 7. Dynamic changes of different types of structural atoms in the γ phase and γ’ phase. The red curve represents the change of structural atoms in the γ phase and 
the blue curve represents the change of structural atoms in the γ’ phase. (a) BCC; (b) HCP; (c) Other.
Fig. 8. Dynamic variation of displacement vector with different strain levels.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
6

## Page 7

Fig. 7 depicts the process of change in atomic number of different 
structural types with increasing strain. Fig. 7 (a), (b) and (c) show the 
dynamic curves of the number of BCC structural atoms, HCP structural 
atoms and amorphous structural atoms in the γ phase and γ’ phase, 
respectively. From Fig. 7 (a), the number of BCC structural atoms in the γ 
phase increases dramatically when the RVE reaches the elastic limit and 
produces a much larger maxima than BCC structural atoms in the γ’ 
phase. After the strain reaches 10 %, there is not much difference in 
atomic number between the BCC structures of the γ phase and the γ’ 
phase, and there is even a phase in which there are more atoms in the 
BCC structure of the γ’ phase than in the γ phase. In Fig. 7 (b) and (c), the 
HCP structural atoms and other structural atoms in the γ’ phase grow 
faster and have a much larger overall number than in the γ phase. This is 
due to the fact that the defects are mainly composed of HCP atoms and 
the phenomenon of defect slip accumulation in the γ’ phase occurs 
during stretching, leading to a gradual growth of HCP structural atoms. 
Moreover, the γ / γ’ interface inside the RVE is destroyed after attaining 
the elastic limit, and the RVE undergoes plastic deformation, which is 
accompanied by partial annihilation of defects and a gradual growth in 
the amount of other structural atoms. The results show that with the 
stretching process, the FCC structural atoms are gradually change the 
atoms of the BCC structure, HCP structure and other structures, etc. 
Meanwhile, the plastic deformation of the γ’ phase raises partly with the 
destruction of the interface after the RVE reaches the elastic limit.
To deeply study the deformation mechanism inside the RVE, 
displacement vector nephogram is obtained to describe the motion trend 
of the atoms, as shown in Fig. 8 . In the early stage of stretching, the 
atomic displacement trend in the middle region ① of the RVE starts to be 
biased toward the loading direction, and the atomic displacement trend 
in the two end regions ② moves completely toward the loading direc -
tion, as shown in Fig. 8 (a). As the strain reaches the elastic limit, the 
trend of the displacement vectors in region ③ begins to diverge and 
different slip bands appear. In addition, the displacement vectors of the γ 
and γ’ phases exhibit different directions, with only the upper half of the 
γ phase in region ③ deforming more and having a more intensive 
displacement tendency, whereas the displacement tendency of the γ’ 
phase has only a smidgen of aggregation, indicating that the deforma -
tion is smaller than that of the γ phase, as shown in Fig. 8 (b). As the 
tensile motion continues, the deformation of the intermediate part 
gradually stabilizes, and the displacement vectors of both phases follow 
the direction of the interface, as shown in region ④ of Fig. 8 (c). In region 
⑤ , the displacement vectors of the two phases become gradient in the 
longitudinal direction both toward the loading direction, and the 
deformation of the two phases varies in the transverse direction due to 
the presence of the interface. Summarizing the above analysis, owing to 
the impact of the interface on the motion of atoms in the tensile process, 
the change of displacement vectors inside the RVE reflects that the 
motion tendency of atoms between the two phases is affected in different 
forms. Especially in the plastic deformation stage, the displacement 
vector in region ④ is basically differentiated along the interface.
Fig. 9 displays the evolution curves of the atomic number with strain 
for different displacement intervals. The alteration in atomic count in -
side the RVE is mainly concentrated in atoms with displacements of 
5 – 10 Å. The trend of the change curve is quite comparable to that of the 
stress-strain curve. The expression of elastic deformation in the stress- 
strain curve is mainly characterised by internal dislocations as well as 
defects in the matrix during the tensile process. During tensile process, 
elastic and plastic deformation within the material occurs alternately, 
and the counted displaced atoms may be caused by the accumulation of 
the previous form of deformation. Therefore, the change in the number 
of atoms with displacements of 5 – 10 Å is mostly a phenomenon that 
manifests itself in the elastic deformation phase. The initiation points of 
the atomic change curves for displacements of 10 – 15 Å, 15 – 20 Å, 
20 – 25 Å, and 25 – 30 Å lag behind the 5 – 10 Å change curves in that 
order, and the trends of these curves with strain are very similar. 
However, atoms with displacements greater than 30 Å appear only after 
18 % strain, and the change curve has been showing an increasing trend. 
This is because the gap at the interface, which gradually weakens the 
effect on the displaced atoms in the range of greater deformation.
3.3. Comparison of tensile properties between single-phase and two-phase 
structural models
To systematically investigate the variation in tensile properties be -
tween the single-phase model and the two-phase structural model, 
tensile motions are carried out for the pure Ni phase, NiCrCo phase, 
Ni
3
Al phase, and NiCrCo/Ni
3
Al ( γ / γ’ ) two-phase structure, respectively. 
Fig. 10 displays the comparative stress-strain curves of different models 
during stretching. It is found that the stress peak of the stress-strain 
curve of the two-phase structure model is the largest. This suggests 
that the two-phase structure has the largest elastic limit compared to the 
other three single-phase models. Within 10 %-30 % of strain, the stress 
trends of the NiCrCo and Ni
3
Al phases are very similar, and the stresses 
are somewhat larger than the model for the γ / γ’ structure, reflecting the 
greater degree of deformation of the NiCrCo and Ni
3
Al phases within 
this phase. However, the Ni phase, although less stressed in the plastic 
deformation stage, oscillates somewhat more than the two phases, 
Fig. 9. Trend in the atomic number of different displacement intervals.
Fig. 10. Stress-strain curves for different models.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
7

## Page 8

resulting in unstable tensile nano deformation of the Ni phase. As a 
result, the two-phase structure increases the resistance of the matrix to 
externally induced deformation due to the presence of interfaces, which 
enhances the mechanical performance of the two-phase structural NBSC.
Fig. 11 shows the trend of atomic quantity with shear strain values 
greater than 0.35 during stretching and the morphology of the shear 
strain morphology in the above four models. In Fig. 11 (a), the model 
with two-phase structure produces the highest amount of shear strain 
atoms in the strain 0 – 15 % range. The growth trend of the number of 
shear strain atoms for the four models within 15 %-20 % of strain 
changes as the tensile movement proceeds. Within 20 %-30 % of strain, 
the growth state of each model remains constant. It is clearly observed 
that the Ni
3
Al phase has the highest amount of shear strain atoms, the Ni 
model has the least, while the two-phase model has the second utmost 
amount of shear strain atoms. In the shear strain morphology, the strain 
degree of NiCrCo phase is a bit greater than that of pure Ni phase, the 
Fig. 11. (a) Dynamic variation of atomic amount of shear strain with tensile strain rate in different models. (b), (c), (d) and (e) are all strain morphologies at 
30 % strain.
Fig. 12. Evolution of defects in different models.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
8

## Page 9

strain distribution of these two models is tighter compared to that of 
Ni
3
Al phase, and the parts of the three models with larger shear strain 
degree appear on the slip surface, as shown in Fig. 11 (b),(c) and (d). 
However, the portion of the γ / γ’ structure where the degree of shear 
strain is greater occurs mainly at the interface as well as at the edges of 
the RVE, which suggests that the interface has a hindering impact on the 
development of shear strain in the interior of the RVE.
Adopting the CNA method, the atoms of the FCC structure in the 
crystals are removed to analyze the defect evolution, as shown in Fig. 12 . 
In the Ni phase, lumpy defects and a few clusters of atoms appear inside 
the RVE at the beginning of stretching. As the tensile process proceeds, 
the defects gradually increase until they grow to a certain point where 
they gradually fracture and decompose as shown in Fig. 12 (a). However, 
after the Cr and Co are added to the Ni model, the defects appearing at 
the early stage of stretching are basically all point defects, most of which 
are atoms in the plastic deformation layer, and the defects appear as slip 
planes after the RVE has been stretched for some time, as shown in 
Fig. 12 (b). In Fig. 12 (c), the defects appearing in the Ni
3
Al phase during 
tension are overall neat and all extend in the same direction of the slip 
surface. In the late stage of stretching, the defects within the Ni
3
Alphase 
fracture from the middle position along the loading direction and fill 
both ends of the RVE. When the NiCrCo/Ni
3
Al structure is stretched, the 
γ phase takes the lead in the whole defects and atoms of the BCC 
structure, while the γ’ phase shows few point defects. In addition, it can 
be seen that the motion form of defects is more irregular than the single- 
phase model, as shown in Fig. 12 (d). This suggests that adding the 
strengthening elements Co and Cr causes the internal defects and 
dislocation organization of high-temperature alloys to undergo a 
complex movement, making the reaction processes that occur more 
varied. The main reason for this situation is that the addition of Co and 
Cr elements improves the solution strengthening and precipitation 
strengthening of NBSC. As a result, the two-phase nickel-based alloys are 
enhanced in tensile strength by adding certain content of Cr and Co, 
which confirms the higher yield strength of the two-phase model shown 
in Fig. 10 .
To observe the trend of defective atomic number more obviously, the 
curves of atomic number of BCC, HCP and other structures in different 
models are counted, as shown in Fig. 13 . The atoms of the BCC structure 
are basically unchanged in the four models. The amount of the HCP 
structural atoms changes drastically in the Ni phase, while the change of 
the other structural atoms is relatively smooth, as shown in Fig. 13 (a). 
When Cr and Co elements are incorporated in the Ni phase, the trend of 
the HCP structural atoms changes from drastic change to basically sta -
ble, while the other structural atomic number show a gradual growth 
during tensile process, as shown in Fig. 13 (b). The HCP structural atomic 
number in the Ni
3
Al phase increases dramatically from the elastic phase, 
and the trend of HCP structural atomic amount begins to slow down 
when the strain reaches the elastic limit. Besides, the trend of the 
number of other structural atoms also increases steadily, but it is very 
different from the trend of the HCP structural atomic amount, as shown 
in Fig. 13 (c). The defect atomic quantities in the γ / γ’ model are sub -
stantially unchanged in the early stage of stretching, and the trends of 
the number of HCP structural atoms and other structural atoms are very 
similar as the degree of strain increases, as shown in Fig. 13 (d). The 
outcomes display that the γ / γ’ model has a prominent blocking impact 
on the development of defect atoms when the RVE is deforming 
Fig. 13. Dynamic curves of defective atomic amount in different models. (Other represents atoms with amorphous structures and atoms with plastic deformation 
layer structures.).
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
9

## Page 10

elastically. As stretching proceeds, the strain attains the yield point and 
the RVE begins to shift the deformation mode, which signifies that the 
dislocations begin to contact and interact with each other, leading to a 
dramatic rise in the HCP and other structures, but owing to the existence 
of the interface, the trend of the HCP structure afterward will not be as 
drastic as the change of the pure Ni phase and the pure Ni
3
Al phase.
The potential energy data for the four models are shown in Fig. 14
(a). It can be obviously shown that the Ni phase has the highest potential 
energy, however, the potential energy of the NiCrCo phase is lower than 
that of both the Ni
3
Al phase and the two-phase model. In addition, the 
displaced atomic amount of the NiCrCo phase starts to increase first and 
the moment of the extreme point appears earlier than that of the Ni 
phase, the Ni
3
Al phase and the two-phase model, as shown in Fig. 14 (b). 
This is because during the tensile motion of the NiCrCo phase, more 
work is done between the Cr, Co and Ni atoms than between the Ni 
atoms alone in the Ni model, leading to an increment in kinetic energy 
and a reduction in potential energy. Additionally, the tendency of the 
two-phase model in terms of displaced atomic amount is comparable to 
that of the Ni phase and Ni
3
Al phase.
4. Conclusion
In this paper, the tensile mechanism of nickel-based single crystal 
superalloys is systematically studied using a MD approach. Moreover, 
the effect of γ / γ’ interface with enhanced elements with respect to the 
tensile properties is discussed by comparative analysis of single-phase 
models, and the following conclusions are concluded: 
1. In the tensile process, massive Shockley and Stair-rod dislocations 
are generated inside the RVE to release energy generated by the 
maximum tensile stress and to reduce the stress concentration, and 
Perfect dislocations have a dominant role in the elastic deformation 
process. When the strain attains the elastic limit, the von Mises stress 
distributions of two phases differ greatly due to the presence of 
interface. Besides, the interface can block the slip of shear strain 
between the two phases and promote ability to resist deformation.
2. After the structure of the γ / γ’ interface is destroyed, some of the 
defects in the γ phase break off as well as disappear, but the defects of 
γ’ phase gradually slip and pile up, resulting in more atoms of the 
HCP structure than in the γ phase. Moreover, the γ / γ’ interface 
causes a difference in the motion trend of the displacement vectors of 
the two phases when stretching is carried out. In particular, during 
the plastic deformation stage, the two phases develop in the 
longitudinal direction in a gradient, and the motion trends in the 
transverse direction are not synchronized.
3. The NiCrCo/Ni
3
Al( γ / γ’ ) model is more resistant to deformation than 
the Ni phase, NiCrCo phase, and Ni
3
Al phase. The synergistic action 
of the interface with the strengthening elements Co and Cr enhances 
the ability of the two-phase structure to resist the externally induced 
microscopic deformation, which promotes the yield strength of the 
γ / γ’ structure.
Ethics
We declare that our paper has not been submitted or published 
elsewhere; All data in this paper are true and reliable, and the main data 
and charts have not been published; This article does not contain 
plagiarism or infringement of others ’ intellectual property rights; This 
study does not involve human or animals.
CRediT authorship contribution statement
Zongxiao Zhu: Conceptualization. Hongmiao Zhang: Data cura -
tion. Yingpeng Xu: Formal analysis. Bingqi Yi: Resources, Project 
administration. Jialong Wang: Resources, Project administration. 
Zihan Sun: Validation.
Declaration of Competing Interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgements
This work was supported by the National Natural Science Foundation 
of China (Grant No. 52265025), the Gansu Provincial Natural Science 
Foundation (23JRRA811), and the Open Project of State Key Laboratory 
of Solid Lubrication (LSL-2215).
Data Availability
Data will be made available on request. The data that support the 
findings of this study are available from the corresponding author, upon 
reasonable request. 
Fig. 14. (a) Comparison of different model potential energies during stretching, (b) Correspondence between atomic amount and strain for different model dis -
placements of 10 – 20 Å.
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
10

## Page 11

References
[1] Y. Li, Y.-F. Yu, Z.-B. Wang, X.-Y. Liang, W.-B. Kan, F. Lin, Additive manufacturing 
of nickel-based superalloy single crystals with IN-738 alloy, Acta Metall. Sin. (Engl. 
Lett. ) (2022) 1 – 6, https://doi.org/10.1007/s40195-021-01320-3 .
[2] Z. Mao, Y. Zhu, Y. Zhao, H. Xie, Y. Yang, Y. Zhou, X. Huang, Z. Liu, High-cycle 
fatigue failure behavior of nickel-based single crystal alloys with different 
deviation angles in a high-temperature environment, Mater. Charact. 203 (2023) 
113118, https://doi.org/10.1016/j.matchar.2023.113118 .
[3] Z. Lou, Y. Yan, Y. Geng, X. Zhao, Z. Hao, The effect of anisotropy of nickel-based 
single crystal alloys on the surface quality of sub-nanometer and near atomic scale 
cutting, Intermetallics 145 (2022) 107536, https://doi.org/10.1016/j. 
intermet.2022.107536 .
[4] G. Wang, S. Zhang, S. Tian, N. Tian, G. Zhao, H. Yan, Microstructure evolution and 
deformation mechanism of a [111]-oriented nickel-based single-crystal superalloy 
during high-temperature creep, J. Mater. Res. Technol. 16 (2022) 495 – 504, 
https://doi.org/10.1016/j.jmrt.2021.12.011 .
[5] T. Ning, Z. Guoqi, M. Tai, T. Sugui, L. Lirong, Y. Huajin, W. Guangyan, J. Fangwei, 
Ultra-high-temperature creep behavior of a single-crystal nickel-based superalloy 
containing 6% Re/5% Ru, Mater. Charact. 180 (2021) 111394, https://doi.org/ 
10.1016/j.matchar.2021.111394 .
[6] H. Long, S. Mao, Y. Liu, Z. Zhang, X. Han, Microstructural and compositional 
design of Ni-based single crystalline superalloys – A review, J. Alloy. Compd. 743 
(2018) 203 – 220, https://doi.org/10.1016/j.jallcom.2018.01.224 .
[7] Q. Ding, Z. Lao, H. Wei, J. Li, H. Bei, Z. Zhang, Site occupancy of alloying elements 
in γ ′ phase of nickel-base single crystal superalloys, Intermetallics 121 (2020) 
106772, https://doi.org/10.1016/j.intermet.2020.106772 .
[8] W. Wu, Y. Guo, Y. Wang, Evolution of misfit dislocation network and tensile 
properties in Ni-based superalloys: a molecular dynamics simulation, Sci. China 
Phys., Mech. Astron. 55 (2012) 419 – 427, https://doi.org/10.1007/s11433-012- 
4630-z .
[9] F. Han, B. Zhou, H. Huang, B. Leng, Y. Lu, J. Dong, Z. Li, X. Zhou, The tensile 
behavior of GH3535 superalloy at elevated temperature, Mater. Chem. Phys. 182 
(2016) 22 – 31, https://doi.org/10.1016/j.matchemphys.2016.07.001 .
[10] S. Chen, X. Xie, W. Li, R. Feng, B. Chen, J. Qiao, Y. Ren, Y. Zhang, K.A. Dahmen, P. 
K. Liaw, Temperature effects on the serrated behavior of an Al0. 5CoCrCuFeNi 
high-entropy alloy, Mater. Chem. Phys. 210 (2018) 20 – 28, https://doi.org/ 
10.1016/j.matchemphys.2017.09.004 .
[11] E. Wyszkowska, C. Mieszczynski, A. Azarov, I. J ´o ´zwik, A. Kosi ´nska, W. Chromi ´nski, 
R. Diduszko, W. Huo, I. Cie ´slik, J. Jagielski, Tuning heterogeneous ion-radiation 
damage by composition in Ni x Fe 1 x binary single crystals, Nanoscale 15 (2023) 
4870 – 4881, https://doi.org/10.1039/D2NR06178C .
[12] Y. Zhang, Z. Wen, H. Pei, Y. Zhao, Z. Li, Z. Yue, Microstructure evolution 
mechanisms in Nickel-based single crystal superalloys under multiaxial stress state, 
J. Alloy. Compd. 797 (2019) 1059 – 1077, https://doi.org/10.1016/j. 
jallcom.2019.05.143 .
[13] W. Xuan, X. Zhang, Y. Zhao, J. Li, B. Wang, X. Ren, Z. Ren, Mechanism of improved 
intermediate temperature plasticity of nickel-base single crystal superalloy with 
hot isostatic pressing, J. Mater. Res. Technol. 14 (2021) 1609 – 1617, https://doi. 
org/10.1016/j.jmrt.2021.07.010 .
[14] Z. Tan, X. Wang, Y. Du, T. Duan, Y. Yang, J. Liu, J. Liu, L. Yang, J. Li, Y. Zhou, 
Temperature dependence on tensile deformation mechanisms in a novel Nickel- 
based single crystal superalloy, Mater. Sci. Eng.: A 776 (2020) 138997, https://doi. 
org/10.1016/j.msea.2020.138997 .
[15] P. Lv, L. Liu, G. Zhao, S. Guo, Z. Zhou, Y. Zhao, J. Zhang, Temperature effects on 
tensile behaviors and relevant deformation mechanisms of a low-cost nickel-based 
single crystal superalloy containing 1.5% Re, J. Alloy. Compd. 926 (2022) 166819, 
https://doi.org/10.1016/j.jallcom.2022.166819 .
[16] F. Xu, F. Fang, X. Zhang, Effects of recovery and side flow on surface generation in 
nano-cutting of single crystal silicon, Comput. Mater. Sci. 143 (2018) 133 – 142, 
https://doi.org/10.1016/j.commatsci.2017.11.002 .
[17] Y. Xu, M. Wang, F. Zhu, X. Liu, Q. Chen, J. Hu, Z. Lu, P. Zeng, Y. Liu, A molecular 
dynamic study of nano-grinding of a monocrystalline copper-silicon substrate, 
Appl. Surf. Sci. 493 (2019) 933 – 947, https://doi.org/10.1016/j. 
apsusc.2019.07.076 .
[18] L. Zhang, H. Tanaka, Atomic scale deformation in silicon monocrystals induced by 
two-body and three-body contact sliding, Tribology Int. 31 (1998) 425 – 433, 
https://doi.org/10.1016/S0301-679X(98)00064-4 .
[19] B. Chen, W.-P. Wu, M.-X. Chen, Orientation dependence of microstructure 
deformation mechanism and tensile mechanical properties of Nickel-based single 
crystal superalloys: a molecular dynamics simulation, Comput. Mater. Sci. 202 
(2022) 111015, https://doi.org/10.1016/j.commatsci.2021.111015 .
[20] Q. Yin, Y. Lian, Z. Wen, H. Pei, J. Wang, Z. Yue, Atomic simulation of the effect of 
orientation on tensile/compressive properties in nickel-based single crystal 
superalloys, J. Alloy. Compd. 893 (2022) 162210, https://doi.org/10.1016/j. 
jallcom.2021.162210 .
[21] Q. Wang, J. Guo, W. Chen, Y. Tian, Molecular dynamics simulations of tensile 
properties for FeNiCrCoCu high-entropy alloy, Mater. Today Commun. 38 (2024) 
108187, https://doi.org/10.1016/j.mtcomm.2024.108187 .
[22] H. Li, W. Du, Y. Liu, Molecular dynamics study of tension process of Ni-Based 
superalloy, Acta Metall. Sin. (Engl. Lett. ) 33 (2020) 741 – 750, https://doi.org/ 
10.1007/s40195-020-01004-4 .
[23] W. Wu, B. Chen, H. Shen, Z. Ding, Molecular dynamics simulation of rhenium 
effects on creep behavior of Ni-based single crystal superalloys, Prog. Nat. Sci.: 
Mater. Int. 32 (2022) 259 – 266, https://doi.org/10.1016/j.pnsc.2022.01.010 .
[24] X. Du, X. Lu, S. Shuang, Z. Wang, Q.-l Xiong, G. Kang, X. Zhang, Cyclic plasticity of 
CoCrFeMnNi high-entropy alloy (HEA): a molecular dynamics simulation, Int. J. 
Appl. Mech. 13 (2021) 2150006, https://doi.org/10.1142/s175882512150006x .
[25] B. Chen, W.-P. Wu, Molecular dynamics simulations of dynamics mechanical 
behavior and interfacial microstructure evolution of Ni-based single crystal 
superalloys under shock loading, J. Mater. Res. Technol. 15 (2021) 6786 – 6796, 
https://doi.org/10.1016/j.jmrt.2021.11.116 .
[26] L. Kurpaska, M. Clozel, J. O ’ Connell, I. J ´o ´zwik, E. Wyszkowska, W. Huo, 
W. Chrominski, D. Kalita, S. Nori, F. Fang, Nanoindentation responses of Fe – Cr 
alloys from room temperature to 600
◦
C, Mater. Sci. Eng.: A 902 (2024) 146590, 
https://doi.org/10.1016/j.msea.2024.146590 .
[27] D. Caillard, An in situ study of hardening and softening of iron by carbon 
interstitials, Acta Mater. 59 (2011) 4974 – 4989, https://doi.org/10.1016/j. 
actamat.2011.04.048 .
[28] R. Darolia, Development of strong, oxidation and corrosion resistant nickel-based 
superalloys: critical review of challenges, progress and prospects, Int. Mater. Rev. 
64 (2019) 355 – 380, https://doi.org/10.1080/09506608.2018.1516713 .
[29] W. Xia, X. Zhao, L. Yue, Z. Zhang, A review of composition evolution in Ni-based 
single crystal superalloys, J. Mater. Sci. Technol. 44 (2020) 76 – 95, https://doi.org/ 
10.1016/j.jmst.2020.01.026 .
[30] S. Nos ´e, A unified formulation of the constant temperature molecular dynamics 
methods, J. Chem. Phys. 81 (1984) 511 – 519, https://doi.org/10.1063/1.447334 .
[31] Y. Wang, S. Tang, J. Guo, Molecular dynamics study on deformation behaviour of 
monocrystalline GaN during nano abrasive machining, Appl. Surf. Sci. 510 (2020) 
145492, https://doi.org/10.1016/j.apsusc.2020.145492 .
[32] P.-Z. Zhu, C. Qiu, F.-Z. Fang, D.-D. Yuan, X.-C. Shen, Molecular dynamics 
simulations of nanometric cutting mechanisms of amorphous alloy, Appl. Surf. Sci. 
317 (2014) 432 – 442, https://doi.org/10.1016/j.apsusc.2014.08.031 .
[33] A. Stukowski, Visualization and analysis of atomistic simulation data with 
OVITO – the Open Visualization Tool, Model. Simul. Mater. Sci. Eng. 18 (2009) 
015012, https://doi.org/10.1088/0965-0393/18/1/015012 .
[34] P. Wang, W. Wu, F. Cui, X. Yang, A. Pan, Investigation of thermal and mechanical 
effects during electrically-assisted compression of CoCrFeNiW0. 5 high entropy 
alloy, Mater. Charact. 202 (2023) 112981, https://doi.org/10.1016/j. 
matchar.2023.112981 .
[35] L. Kurpaska, F.J. Dominguez-Gutierrez, Y. Zhang, K. Mulewska, H. Bei, W. 
J. Weber, A. Kosi ´nska, W. Chrominski, I. Jozwik, R. Alvarez-Donado, Effects of Fe 
atoms on hardening of a nickel matrix: nanoindentation experiments and atom- 
scale numerical modeling, Mater. Des. 217 (2022) 110639, https://doi.org/ 
10.1016/j.matdes.2022.110639 .
[36] J. Du, C. Wang, T. Yu, Construction and application of multi-element EAM 
potential (Ni – Al – Re) in γ / γ ′ Ni-based single crystal superalloys, Model. Simul. 
Mater. Sci. Eng. 21 (2012) 015007, https://doi.org/10.1088/0965-0393/21/1/ 
015007 .
[37] Q.N. Fan, C.Y. Wang, T. Yu, J.P. Du, A ternary Ni – Al – W EAM potential for Ni-based 
single crystal superalloys, Phys. B 456 (2015) 283 – 292, https://doi.org/10.1016/j. 
physb.2014.09.012 .
[38] S. Foiles, M. Baskes, M.S. Daw, Embedded-atom-method functions for the fcc 
metals Cu, Ag, Au, Ni, Pd, Pt, and their alloys, Phys. Rev. B 33 (1986) 7983, 
https://doi.org/10.1103/physrevb.33.7983 .
[39] Z. Hao, R. Cui, Y. Fan, J. Lin, Diffusion mechanism of tools and simulation in 
nanoscale cutting the Ni – Fe – Cr series of Nickel-based superalloy, Int. J. Mech. Sci. 
150 (2019) 625 – 636, https://doi.org/10.1016/j.ijmecsci.2018.10.058 .
[40] G. Bonny, D. Terentyev, R.C. Pasianot, S. Ponc ´e, A. Bakaev, Interatomic potential 
to study plasticity in stainless steels: the FeNiCr model alloy, Model. Simul. Mater. 
Sci. Eng. 19 (2011) 085008, https://doi.org/10.1088/0965-0393/19/8/085008 .
[41] Y.-m Kang, N.-x Chen, J. Shen, Atomistic simulation of the lattice constants and 
lattice vibrations in RT4Al8 (R = Nd, Sm; T = Cr, Mn, Cu, Fe), J. Alloy. Compd. 352 
(2003) 26 – 33, https://doi.org/10.1016/s0925-8388(02)01134-9 .
Z. Zhu et al. Materials Today Communications 41 (2024) 110826 
11
