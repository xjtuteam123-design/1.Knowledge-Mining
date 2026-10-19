# 10.1115_1.4027814

<!-- source: D:\总文献\10.1115_1.4027814.pdf -->
<!-- file_sha256: e18b21ce52418da8b3a7d1dd7654b475b0b11cbca54e4ca60e17b49ba83e4ecc -->

## Page 1

Honghong Su
Department of Engineering Mechanics, 
Chongqing University, 
Chongqing 400044, China;
AML, Department of Engineering Mechanics, 
Tsinghua University, 
Beijing 100084, China
Xufei Fang
AML, Department of Engineering Mechanics, 
Tsinghua University, 
Beijing 100084, China;
Center for Mechanics and Materials, 
Tsinghua University, 
Beijing 100084, China
Xue Feng1
AML, Department of Engineering Mechanics, 
Tsinghua University, 
Beijing 100084, China;
Center for Mechanics and Materials, 
Tsinghua University, 
Beijing 100084, China 
e-mail; fengxue@tsinghua.edu.cn
Bo Yan
Department of Engineering Mechanics, 
Chongqing University, 
Chongqing 400044, China
The Temperature-Dependent 
Strength of Metals: Theory 
and Experimental Validation
In this work, we propose a strength theory as a function of temperature and state of 
stresses for metals. Based on the fracture in the hydrostatic stress, we derived a general­
ized strength model, in which the fracture strength decreases almost linearly with the 
increasing of the temperature. Furthermore this generalized strength model was extended 
to the general state of stresses by replacing the equivalent hydrostatic stresses with the 
temperature effect based on the general thermodynamics principles. Molecular dynamics 
(MD) simulation was also conducted to simulate the fracture evolution at high tempera­
ture and to explain the mechanism of temperature-dependent strength at atomic scale. 
The proposed model was also verified by experiment of Mo-lOCu alloy at elevated tem­
perature. [DOI: 10.1115/1.4027814]
Keywords: fracture strength, high temperature, metals, molecular dynamics simulation
1 Introduction
With the unyielding increase of the thrust-weight ratio of air­
craft, the demand for the service temperature of the aircraft hot 
end components rises accordingly. As one class of important engi­
neering materials, refractory metals (Mo, Ta, Nb, Zr, etc.) and 
alloys, which possess the properties of high melting points, high 
temperature resistance and corrosion resistance, are being widely 
used in the components of the aero engines, re-entry hot ends, etc. 
[1-5]. The excellent mechanical properties of these metals and 
alloys at high temperature are comparable to some high tempera­
ture structure ceramics, such as ultrahigh temperature ceramics 
and have a higher ductility [6,7], However, at elevated tempera­
ture, the mechanical parameters of the metals, such as modulus, 
yield strength, and fracture strength could change enormously due 
to the temperature effect [8-10] and other damage factors such as 
oxidation [11,12]. Among these mechanical properties, the frac­
ture strength can be very sensitive to temperature, and is critically 
important for engineering design and structural safety, especially 
for the design with the brittle fracture strength criterion. Thus, the 
strength theory of metals and alloys has been intensively studied, 
both from a micro scale [13-20] and macroscale. Zhurkov’s study 
[21] showed that fracture strength is time and strain-rate depend­
ent. He also came up with an empirical equation establishing the 
relation for tensile strength a, fracture time, and temperature
m I/o kTa(T) =
----------In
y y
(i)
’Corresponding author.
Contributed by the Applied Mechanics Division of ASME for publication in the 
Journal of A pplied M echanics . Manuscript received May 12, 2014; final manuscript 
received June 3, 2014; accepted manuscript posted June 6, 2014; published online 
June 19, 2014. Editor: Yonggang Huang.
where k is the Boltzmann constant, to is taken to be 10- '3 s for 
different solids. Uo, y are materials constants of solids. 
U = Uo — ya is the activation energy for the breakage of internal 
atomic bonds under the action of thermal fluctuations, Uo is the 
value of activation energy when a — > 0.
Based on Eq. (1), Vettegren et al. [22] concluded that the ten­
sile strength at a constant strain rate is approximately a linear 
function of temperature. However, these two former proposed 
equations are empirical, and the mechanism is not yet clear. To, 
Uo, and y need to be obtained either through experimental tests or 
by mathematical fitting. Besides, the application of the formula is 
limited for fracture strength, while not applicable for other 
strength theories, neither was the difference under various stress 
states taken into consideration. When t > t o exp(t/o/LT) in 
Eq. (1), the tensile strength would be minus, which contradicts the 
fact. This equation is also incapable of describing the critical point 
where t = xc for irreversible fracture transfer.
Selinger et al. [23] presented the expression of free energy by 
using elastic constants and dislocation energy. The critical posi­
tion for the fracture strength was also analyzed through the 
extremum conditions of the free energy. But this model did not 
present a concrete form of expression. The elastic constants and 
dislocation energy are too complicated to be described since they 
are related to temperature, and it is not yet to be applied for real 
engineering conditions. Furthermore, this fracture strength is also 
limited in characterizing the material defects.
Traditional strength theory is usually presented in the form 
f (ojj, r.ij) = Const, and there are relatively complete criterions for 
strength at room temperature already, fitting for different materi­
als and stress status. However, at high temperature these theories 
do not apply well. The basic idea of this work is that for metals 
subjected to high temperature, if we can convert the temperature 
effect into equivalent stress or strain, and integrate them into the 
traditional strength theory, then it is likely to make further pro­
gress based on the existent theories.
Journal of Applied Mechanics Copyright ©2014 by ASME SEPTEMBER 2014 , Vol. 81 / 091003-1

## Page 2

In this work, we propose to establish temperature-dependent 
fracture strength theory under quasi-static conditions (small strain 
rate, which could be treated as isothermal fracture process) based 
on the general thermodynamics principles, and to present the 
equations of state at critical points at the starting point of the irre­
versible process. Furthermore, based on these equations, we 
obtained a method to transform the temperature effect into equiva­
lent stress in general stress fields and analyze the strength within 
the frame of traditional strength theory. A theoretical result under 
general stress status is presented, and the theory is also verified by 
MD simulation for metallic molybdenum and experiments of 
Mo-lOCu alloys.
2 Theoretical Analysis
2.1 High Temperature Strength Theory in Hydrostatic 
Stress. The general equations of state in thermodynamics are 
expressed with basic quantities'such as temperature, pressure and 
volume, etc. In order to establish the temperature equivalent 
stress, we first analyzed the quasi-static isothermal fracture in 
hydrostatic stress and obtained the temperature-dependent fracture 
strength theory (in hydrostatic stress, the fracture is brittle). Based 
on this strength theory, we further obtained the expression for 
temperature equivalent stress under general state of stress. Then, 
we supetposed the temperature equivalent stress and mechanical 
stress together, and used the traditional strength theory to com­
plete the strength analysis. In this way, the material defects would 
still be characterized in the strength limit of the original strength 
theory, while the temperature effect would be an equivalent stress, 
which is irrelevant from the material defects.
Assume the material is under hydrostatic stress ay = am 8y 
= — Pdy and the ambient temperature is T. Here, ay is stress ten­
sor, am = (l/3)<r** is the mean stress, P is hydrostatic pressure, 
and S ij is Kronecker delta. For hydrostatic stress, there is no plas­
tic deformation but only work done from the volume deformation. 
From the fundamental thermodynamic relations, we have
dU = TdS - PdV = TdS + am dV (2)
where U is internal energy, V is volume, S is entropy, and P is 
pressure, am = (1/3 )ak k is the mean stress, respectively. Rewrite 
Eq. (2) as
The subscript T in Eq. (3) stands for isothermal process. Here, 
(dU/dV)T= n contains the effects of heat and force, so we 
defined it as the generalized force corresponding to the general­
ized coordinates V , and it stands for the effect of volume change 
on the internal energy under isothermal condition. When T= 0, 
hydrostatic stress am is equal to (dU/dV)T. So for fracture, we 
can define the generalized force n as strength, and the correspond­
ing strength criterion is
(4)
The key to apply Eq. (6) is to determine c p . Since it is difficult 
to calculate ( dP/dT)v under high stress condition, we rewrite c p 
by using Maxwell relations
P
(7)
here aP is the isobaric coefficient of thermal expansion, Cy is 
molar heat capacity at constant volume, and y is Griineisen param­
eter. It should be noted that the value of o c P pT or y in high stress 
and strain condition is different from that in normal pressure. 
When the volume remains constant, the thermal pressure is a lin­
ear function of temperature for many classes of solids at tempera­
ture above the Debye temperature [24]. This means that a P flT can 
be treated as a constant [10,24]. When the volumetric strain 
approaches the critical state of fracture, aP (iT at high temperature 
may still be constant (later the Mo-lOCu alloy experimental data 
did prove this assumption), i.e.,
c p = aP pT = (p{V) (8)
Apply it into Eq. (6) and it yields to the final expression of the 
strength criterion
rcOm, T) = cpT + am = itc (9)
We call this equation the generalized stress strength criterion. 
The difference of V is relatively small when the materials frac­
ture are under different conditions of (T, am ), this means (p(V) 
can be taken as a constant when n = nc and we have
7") < p 0T 4- am ~ 7 i c (10)
This equation is the strength theory at high temperature with a 
linear expression.
It is practicable to calculate the value of c p 0 by testing different 
status of (T, ac) of the materials and fitting them in a linear way. 
For two data points, we have
{T2)-c rc(Tx) 
h - (11)
Apart from the experimental way to calculate < p 0, here, we 
derive theoretical expression of c p by analyzing the Griineisen pa­
rameter. We study the local damage region of the specimen. The 
atoms in this region should be almost independent of each other at 
the critical state of fracture. We can treat coordinate of particle as 
normal coordinate (coordinate of phonon), and therefore, charac­
teristic frequency of phonon has the inverse ratio with the cube 
root of volume, and Griineisen parameter can be written as
lf dh\V d\nV 3 (12)
According to the Maxwell relations in thennodynamics, we have
Let c p = ( dS/dV)T= ( dP/dT)v and combine Eqs. (3) and (4), 
we have
n = cpT + am = cpT + pTd (6)
here pT is isothermal bulk modulus and 9 is volume deformation.
where k is proportionality constant, y f is Griineisen parameter at 
the critical state of fracture, c o is characteristic frequency, and V is 
molar volume.
Substituting Eq. (12) into Eq. (7), we have
<P =
CyiJ)
3V (13)
Apply Eq. (13) in Eq. (9) and it yields to
Cv(T)
3E
+ < 7 m — T C c (14)
091003-2 / Vol. 81, SEPTEMBER 2014 Transactions of the ASME

## Page 3

1800 Equation (17) can be further approximated as
F ig . 1 T h e o re tic a l p re d ic tio n o f te m p e ra tu re -d e p e n d e n t 
s tre n g th u n d e r h y d ro s ta tic stre s s s ta te
Using Einstein’s model of heat capacity [10,25]
Thus, the generalized stress strength criterion becomes
C m = nc - ^ T (18)
In Fig. 1, it shows the curves predicted by the theory above. 
The material’s constants n c and V are estimated from data of meal 
molybdenum at room temperature. The solid line is computed by 
using Eq. (16) and the dashed line by Eq. (17). We can see there 
is only a very small difference between these two curves and the 
strength decreases almost linearly as the temperature increases.
2.2 Strength Theory for General State of Stress. The afore­
mentioned analysis is based on the hydrostatic stress status in 
which the fracture process occurs simultaneously in three direc­
tions. However, it is not practical for most of the actual stress sta­
tus. So we consider the general state of stress, the principle 
stresses are 07 = (1 = 1, 2,3), and the applicable strength criterion 
at T = 0 K is/(ff;) = <7C , that is ,/(07) is equivalent stress.
We rewrite Eq. (14) as
n c - am = < j > { T) (19)
where
m =
Cv(T)
3V (20)
( j) ( T ) = n c — am can be viewed as a temperature equivalent 
stress for fracture, it has the dimension of energy per unit volume, 
and reflects the strength variation with temperature change. 
Popularize Eq. (19) to general stress state, we have
/?0 zexp( y
V T ^ e xp (jT ) - 1
r + <?m — n c (16)
At very high temperature (e.g., T » 0 ), Eq. (16) can be 
approximated as
+ < r m — 7 T C (17)
At low temperature, (R T/V )exp(0/T ) is much smaller than 
am , Eq. (17) still holds. That is, Eq. (17) is a comprehensive 
approximation within the whole temperature range.
< r c -/(<t,) = Q(T) (21)
Equation (21) is the strength criterion in general state of 
stresses.
If nc is known, we can substitute ffi = 02 = ff3 = om into 
Eq. (21) and compare with Eq. (19) to find f 1 (T ).
Generally, uni-axial tensile is a more common case, so we try 
to derive the expression of strength in uni-axial tensile stress state.
Temperature equivalent stress for fracture is insensitive to the 
fabrication process and defects of the materials, thus we can treat 
it as ideal strength problem and use energy as strength criterion. 
From the perspective of energy, as long as we can equalize 07 to 
hydrostatic stress am , and let the work W y (work from am on vol­
ume change 0 due to s,) be equal to W2 (work from 07 on s,)- 
Assume the plastic deformation would not change the volume,
F ig . 2 U n i-a x ia l te n s ile s tre s s -s tra in c u rv e s o f M o (M D s im u la tio n )
Journal of Applied Mechanics SEPTEMBER 2014, Vol. 81 / 091003-3

## Page 4

Fig. 3 Temperature dependent tensile strength of Mo (MD simulation)
Table 1 Fracture strength of Mo-1 OCu
T (K) S (MPa) e/lO'2 a (MPa)
300“ 470 15 540.5
1073“ 252 Bb 284.76
1173 204.2 12.9 230.5
1273 170.2 11.6 189.9
1373 108.1 7.2 115.9
1473 86.7 8.5 94.1
The data at 300 K and 1073 K are from Ref. [26], and we replaced the 
engineering fracture stress by tensile strength.
b13% is an approximate value as it is not given in Ref. [26], S is engineer­
ing stress, e is engineering strain, the true stress a = (1 + e)S.
_ (ff| + O '! + ffj) — 2t/((TiO-2 + + fflO -3)
a m ~ {l-2v)(o1+o2 + o3) (22)
where v is Poisson’s ratio, 8, is the principle strain, and we assume 
> 0 because temperature equivalent stress always should do 
positive work in each direction, whether in tensile stress state or 
compressive.
For uni-axial tensile test (cri > 0, a2 = 03 = 0), Eq. (22) becomes
Fig. 4 Strength curves of Mo for plane stress states at different 
temperatures (MD simulation)
0i = (1 - 2 v)om (23)
and the plastic work under isothermal loading condition would 
transfer into the environment as heat, making no contribution to 
the fracture. So we only consider the energy in the elastic defor­
mation, and for tension of isotropic materials, we have
1 1
Wl = 2 c rm © = 2 ffm(81 + 82 + £3)
W 2 = J O l8 l + <r282 + 0-383)
W \ = W2
1 , , .. =>£l = -(ffl - v ( < T 2 + 0-3))
82 = p ( o 2 - v{a 1 + 0 3 ))
83 =~(<T3 ~ 1 + 02))C * J
That means temperature equivalent stress in hydrostatic 4 > (T ) 
should multiply (1 — 2v) in this stress state.
£i(r) = ( l - 2^(70 (24)
Using maximum tensile stress criterion /(cr,) = and Eqs. 
(24) and (21), we can get temperature dependent uni-axial tensile 
strength
df-«V = (l-2 i/)0 (r )« (l-2 i/)£ r (25)
where cr, and < J c t are uni-axial tensile strength at temperature T and 
T= 0, respectively.
3 MD Simulation
Here, we used the MD to conduct the simulation on metal mo­
lybdenum for the theory proposed above. The simulation tool
091003-4 / Vol. 81, SEPTEMBER 2014 Transactions of the ASME

## Page 5

Table 2 Material constants of Mo-1 OCu
Mo Cu Mo-10Cua
V/10-6 -m3 ■ moP1 9.4 7.1 9.17
V 0.31 0.33 0.312
aThe material parameters for Mo-lOCu are obtained by weighting those of 
Mo and Cu, and the weight is 90% for Mo, 10% for Cu, respectively.
Fig. 5 Tem perature-dependent fracture strength of Mo-1 OCu
used is a classical MD simulator, Lammps. The crystal structure 
for Mo is (body-centered cubic) and the lattice constant is 3.8581. 
A periodic boundary condition in each direction is adopted. The 
simulation cell size is 10 lattice units in each direction, with 2000
atoms in total. The potentials of the metal are obtained from Ref. 
[27]. Since moles (IV), pressure (P), and temperature (T) are con­
served for isothermal-isobaric ensemble, thus, the NPT ensemble 
is adopted. The load method is fix deform, and at x(100) and 
y(010) directions, respectively. The strain rate is set to be 10 9 /s, 
with a simulation temperature range from 300K-1800K.
The simulation results include large amount of data, and for 
simplicity, we present the following two figures to show the ten­
sile simulation at 300 K and 1800K, respectively.
As shown in Fig. 2, the fluctuation becomes more intense as the 
temperature increases, and a uniform filter is used to smooth the 
fluctuation. For each loading simulation, it correspondingly has a 
stress-strain curve, and we have obtained a total of 200 sets of 
data. About 30 sets of temperature dependent fracture strength 
curves were generated by using these data. Figure 3 shows 
strength-temperature curves for two different stress states.
From Fig. 3, we can see that the strength decreases as the tem­
perature increases, but with a lower decreasing speed at higher 
temperature. The tendency of the curve corresponds well with Eq. 
(17) qualitatively. Quantitative computations are not applicable, 
because MD simulations are incapable of taking into considera­
tion of the material defects and it also adopts a very high loading 
speed.
As shown in Fig. 4, each point corresponds to a MD simulation. 
This figure shows that strength curve can be expressed as a linear 
combination by o\ and er2, and the lines representing strength 
at different temperatures are parallel. This result agrees with 
Eq. (21).
The fracture strength criterion in general stress state can be 
written as
Aai+Ba2 + Cij 3 + D = Q(T) exists cr, > 0 and o\ > a2 > 03
E(o\ +<72 + <d ) +F = S1(T) each cr, <0 and ai><J2>(72
(26)
Fig. 6 M icrom orphologies of Mo-1 OCu fracture surface at different tem peratures
Journal of Applied Mechanics SEPTEMBER 2014, Vol. 81 / 091003-5

## Page 6

where A, B, C, D, E, and F are constants, £1(0) = 0 and £1(7’) are 
decided by Eq. (19). Notice that the tensile strength is different 
from compressive strength.
4 Experiments and Analysis
The quasi-static tensile test for Mo-lOCu alloy specimens were 
carried out at high temperature and the data are shown in Tables 1 
and 2.
Take the data (7o = 1173, c r ® = 230.5), substitute it into Eq. 
(25) and ignore the change of Poisson’s ratio, we have
a,{T) = a°- (T - T0) = 630.377 - 0.34IT (MPa)
where T is only taken for the value without unit. The comparison 
of theoretical result and experimental data are shown in Fig. 5.
From Fig. 5, we can see that the data from low temperature till 
high temperature fit well with the theory, especially under 1356 K 
(the melting point of Cu). The reason that the data of 1373K and 
1473 K are relatively smaller is possibly due to the melting and 
vaporization of the Cu (10 wt. %) in the specimens, as shown in 
Fig. 6. When the temperature approaches to the melting point of 
Cu, the theoretical fracture strength is lower. This is can be 
explained by two factors. First, the microstructure changes when 
the temperature exceeds the recrystallization temperature, espe­
cially that the defects due to processing and fabrication would dis­
appear near the melting point. Second, the Poisson’s ratio would 
approach to 0.5 when the temperature is close to the melting 
point.
In Fig. 6, we can see from the scanning electron microscope 
morphologies of the fracture surface of Mo-Cu alloy that at the 
four different temperatures, the Mo phase is stable and no obvious 
phase transition of Mo occurs, which consists with our simplified 
model. Even though the microstructures of the materials are 
changed in working conditions, there will be consequently the dis­
crete change of Cy and V . In this case, we would only need to 
apply this strength theory piecewise, and it is expected that the 
result would be the same with accuracy.
5 Conclusion
In this paper, we proposed a theory to develop the fractured 
strength theory at high temperature, and we also deduced an 
expression formula related to temperature, in which the material 
parameters have clear physical meanings. Furthermore, by using 
this theory we can get the fracture strength at high temperature 
based on the data at low temperature, which is applicable for engi­
neering purposes. A MD simulation is conducted for the valida­
tion of the theory and the results agree well with the theory.
The data from the experiments of Mo-lOCu alloys indicate that 
there seems to be a linear relation between the fracture strength 
and temperature, especially within the range of the actual working 
temperature, which confonns well to our theory. For more compli­
cated nonmetallic materials, further experiments are needed for 
the validation.
From the strength theory in this paper we can see that the tem­
perature equivalent stress is only related to the temperature and 
volume, while insensitive to the fabrication conditions and defects 
of the materials. However, with the temperature increasing to the 
melting points of the materials, the fabrication defects would van­
ish, so the theory is not yet precise enough for the temperature 
range approaching the melting points and it needs further comple­
tion, too. Poisson’s ratio is temperature-dependent too. This factor 
will affect the strength theory at ultrahigh temperature, especially 
near the melting point. It needs further consideration in the theory. 
The fracture strength is rate-dependent. In this work, we only 
dealt with the quasi-static process (isothermal process). The
ultrahigh strain-rate process (isentropic process) and higher strain- 
rate process are yet to be investigated.
Acknowledgment
We gratefully acknowledge the support from National Natural 
Science Foundation of China (Grant Nos. 11222220, 11227801, 
11320101001, 11002078, and 11372155) and Tsinghua University 
Initiative Scientific Research Program (No. 2011Z02173). Hon- 
ghong Su and Xufei Fang contributed equally to this work.
References
[1] Jiang, H„ Hirohasi, M„ Lu, Y„ and Imanari, H„ 2002, “Effect of Nb on the High 
Temperature Oxidation of Ti-(0-50 at. %)A1,” Scr. Mater., 46(9), pp. 639-643."
[2] Ma, C. L„ Li, J. G., Tan, Y., Tanaka, R., and Hanada, S., 2004, “Microstructure 
and Mechanical Properties of Nb/Nb5Si3 In-Situ Composites in Nb-Mo-Si and 
Nb-W-Si System,” Mater. Sci. Eng. A, 386(1-2), pp. 375-383.
[3] Senkov, O. N., Scott, J. M„ Senkova, S. V., Miracle, D. B., and Woodward, C. 
F., 2011, “Microstructure and Room Temperature Properties of a High-Entropy 
TaNbHfZrTi Alloy,” J. Alloys Compd., 509(20), pp. 6043-6048.
[4] Liu, C. M„ Wang, H. M„ Zhang, S. Q„ Tang, H. B„ and Zhang, A. L., 2014, 
“Microstructure and Oxidation Behavior of New Refractory High Entropy 
Alloys,” J. Alloys Compd., 583, pp. 162-169.
[5] Varma, S. K., 2010, “Refractory Metals— An Exploration of High-Temperature 
Materials,” JOM, 62(10), pp. 12.
[6] Yoshimi, K„ Nakatani, S., Nomura, N., and Hanada, S„ 2003. “Thermal Expan­
sion, Strength and Oxidation Resistance of Mo/MosSiB2 In-Situ Composites at 
Elevated Temperature,” Intermetallics, 11(8), pp. 787-794.
[7] Yoko, Y.-M., 2000, “High Temperature Strength of IR-Based Refractory Super­
alloys,” J. Jpn. Inst, Met., 64, pp. 1068-1075.
[8] Armstrong, R. W.. and Walley, S. M„ 2008, “High Strain Rate Properties of 
Metals and Alloys,” Inter. Mater. Rev., 53(3), pp. 105-128.
[9] Carreker, R. P., and Hibbard, W. R., 1953, “Tensile Deformation of High- 
Purity Copper as a Function of Temperature, Strain Rate, and Grain Size,” Acta 
Metall., 1(6), pp. 654— 663.
[10] Su, H. H., Fang, X. F., Feng, X., and Yan, B., 2014, “Temperature-Dependent 
Modulus of Metals Based on Lattice Vibration Theory,” ASME J. Appl Mech 
81(4), p. 041017.
[11] Hu, S. L., and Shen, S. P., 2013, “Non-Equilibrium Thermodynamics and Var­
iational Principles for Fully Coupled Thermal-Mechanical-Chemical Proc­
esses,” Acta Mech., 224(12), pp. 2895-2910.
[12] Suo, Y. H.. and Shen, S. P.. 2013, “General Approach on Chemistry and Stress 
Coupling Effects During Oxidation,” J. Appl. Phys., 114(16), p. 164905.
[13] Wei, Y. J„ and Gao, H. J., 2008, “An Elastic-Viscoplastic Model of Deforma­
tion in Nanocrystalline Metals Based on Coupled Mechanisms in Grain Boun­
daries and Grain Interiors,” Mater. Sci. Eng. A, 478(1-2), pp. 16-25.
[14] Wei. Y. J., 2011, “Anisotropic Size Effect in Strength in Coherent Nanowires 
With Tilted Twins,” Phys. Rev. B, 84(1), p. 014107.
[15] Wei, Y. J., 2011, “Scaling of Maximum Strength With Grain Size in Nano- 
twinned fee Metals,” Phys. Rev. B, 83(13), p. 132104.
[16] Vikas, T., and Min, Z., 2006, “Tension-Compression Strength Asymmetry of 
Nanocrystalline a-Fe20 , + fcc-Al Ceramic-Metal Composites," Appl Phys 
Lett., 88. p. 233107.
[17] Vikas, T., and Min, Z., 2006, “Classical Molecular-Dynamics Potential for the 
Mechanical Strength of Nanocrystalline Composite fcc-Al + a- Fe20 3,” Phys 
Rev. B, 73(17), p. 174116.
[18] Qiang, Y„ Bazant, Z. P„ Bayldon, J., Le, J.-L., Caner, F. C., Ng, W. H„ Waas, A. 
M„ and Daniel, I. M.. 2009, “Scaling of Strength of Metal-Composite Joints— 
Part I: Experimental Investigation,” ASME J. Appl. Mech., 77(1), p. 011011.
[19] Le, J.-L., Bazant, Z. P., and Yu, Q., 2009, “Scaling of SU'ength of Metal-Composite 
Joints—Part II: Interface Fracture Analysis,” ASME J. Appl. Mech., 77(1), p. 011012.
[20] Yu, Q., Bazant, Z. P., and Le, J.-L., 2013, “Scaling of Strength of Metal- 
Composite Joints—Part III: Numerical Simulation,” ASME J. Appl Mech 
80(5), p. 054503.
[21 ] Zhurkov, S. N., 1984, “Kinetic Concept of the Strength of Solids,” Int. J. Fract 
26(4), pp. 295-307.
[22] Vettegren, V. I., Kulik, V. B., and Bronnikov, S. V., 2005, “Temperature De­
pendence of the Tensile Strength of Polymers and Metals at Elevated Temper­
atures,” Tech. Phys. Lett., 31(11), pp. 969-972.
[23] Selinger, R. L. B., Wang, Z. G., Gelbart, W. M., and Ben-Shaul, A., 1991, 
“Statistical-Thermodynamic Approach to Fracture,” Phys. Rev. A, 43(8), pp 
4396-4400.
[24J Yamamoto, S., and Anderson, O. L., 1987, “Elasticity and Anharmonicity of Potas­
sium Chloride at High Temperature,” Phys. Chem. Miner., 14(4), pp. 332-340.
[25] Born, M., and Huang, K., 1954, Dynamical Theory of Crystal Lattices, Claren­
don, Oxford, UK.
[26] Liu, B., Bai, P. K., Chen, J., and Bu, Z. X., 2009, “Study on Rapid Prototyping 
Preparation Process of Molybdenum/Copper Composites.” J. North Univ. 
China, Nat. Sci. Ed., 30, pp. 85— 89, available at: http://caod.oriprobe. 
com/artic!es/15280954/Study_on Rapid_Prototyping_Preparation_Process_ of_ 
Molybdenum_Copper_Co.htm
[27] Zhou, X. W„ Johnson, R. A., and Wadley, H. N. G., 2004, “Misfit-Energy- 
Increasing Dislocations in Vapor-Deposited CoFe/NiFe Multilayers,” Phys 
Rev. B, 69(14), p. 144113.
091003-6 / Vol. 81, SEPTEMBER 2014 Transactions of the ASME

## Page 7

Copyright
of
Journal
of
Applied
Mechanics
is
the
property
of
American
Society
of
Mechanical
Engineers
and
its
content
may
not
be
copied
or
emailed
to
multiple
sites
or
posted
to
a
listserv
without
the
copyright
holder's
express
written
permission.
However,
users
may
print,
download,
or
email
articles
for
individual
use.
