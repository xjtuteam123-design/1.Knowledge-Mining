# 10.1088_1361-651X_ab2031

<!-- source: D:\总文献\10.1088_1361-651X_ab2031.pdf -->
<!-- file_sha256: 50328bec545f15db849e6641c97f6528a66241fe9a4e5a4870f9ae64ac09af68 -->

## Page 1

Modelling and Simulation in Materials Science and Engineering
ACCEPTED MANUSCRIPT
Design of Re-free nickel-base single crystal superalloys using modelling
and experimental validations
To cite this article before publication: Longfei Zhang et al 2019 Modelling Simul. Mater. Sci. Eng. in press https://doi.org/10.1088/1361-
651X/ab2031
Manuscript version: Accepted Manuscript
Accepted Manuscript is “the version of the article accepted for publication including all changes made as a result of the peer review process,
and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an ‘Accepted
Manuscript’ watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors”
This Accepted Manuscript is © 2019 IOP Publishing Ltd.
 
During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully
protected by copyright and cannot be reused or reposted elsewhere.
As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse
under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.
After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they
adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0
Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content
within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this
article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be
required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.
View the article online for updates and enhancements.
This content was downloaded from IP address 136.167.3.36 on 19/05/2019 at 05:38

## Page 2

Design of Re-free nickel-base single crystal superalloys using modelling 
and experimental validations 
 
Longfei Zhang1, Zaiwang Huang2*, Yanming Pan2, Liang Jiang1,2 
1. State Key Laboratory of Powder Metallurgy, Light Alloy Research Institute, Central South University, Changsha, 
Hunan, 410083, China 
2. State Key Laboratory of Powder Metallurgy, Powder Metallurgy Research Institute, Central South University, 
Changsha, Hunan, 410083, China 
 
 
Abstract 
Lowering the rhenium (Re) content in nickel -base single cryst al superalloys has been a 
hot topic in recent years. To explore the design space of Re-free nickel-base single crystal 
superalloys, computer-aid model ling procedures were developed based on thermodynamic 
calculations and regression analysis. Regression coefficients for alloy density were updated 
based on Caron’s density model and newly -collected data. A new regression model f or creep 
resistance was also proposed to improve the predictive accuracy and capability. To isolate the 
alloys with a tar geted microstructure, property constraints were defined for the γ′ fraction, γ′ 
solvus, heat treatment window, γ/γ′ lattice misfit and phase stability number. Two Re-free alloys 
SC11 and SC21 were tested to validate the modelling procedures. The results indicated after 
ageing treatment, SC11 that violated the constraints of misfit and phase stability number 
exhibited premature γ′ coalescence; while SC21 that fulfilled all the constraints exhibited the 
targeted microstructure. The inappropriate misfit and phase stability number in SC11 caused 
severe microstructur al degradation during creep, resulting in inferior creep resistance than 
prediction; while SC21 exhibited creep resistance as expected although a limited amount of 
TCP phases were formed during high temperature creep. 
 
Keywords: nickel-base s ingle crystal superalloys; Re-free; density; CALPHAD; γ/γ′ lattice 
misfit; creep resistance 
 
*Corresponding author: 
E-mail: huangzaiwang@csu.edu.cn (Zaiwang Huang) 
 
Page 1 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 3

1. Introduction 
It has been nearly 40 years for the compositional evolution of nickel-base single crystal 
(SC) superalloys, which have been extensively used in aero-engines and industrial gas turbines 
as the materials of hot section components, such as the high pressure turbine blades [1,2]. The 
development of superalloys is stimulated by t he demand for thermal efficiency of turbine 
engines, which requires increasing the temperature capability of these materials [2]. Nowadays, 
advanced nickel-base SC superalloys contain more than eight intentional alloying elements to 
achieve the desired high temperature mechanical properties, standing for alloy system s of 
extreme chemical complexity. 
The development of SC superalloys in the past went through an empirical trial-and-error 
fashion [3-5] since the quantitative relationships that bridging composition, microstructure and 
property have hardly been established. This fashion is very time- and resource-consuming due 
to the sophisticated processes involved and a large number of properties to be validated. 
However, the high temperature mechanical properties indeed have been greatly improved from 
generation to generation [1]. This can be mainly attributed to t he increased addition of 
refractory metals such as molybdenum (Mo), tungsten (W), tantalum (Ta) and rhenium (Re), 
with Re addition being the most prominent. For example, the first generation alloys contain no 
Re, however the second and third generation alloys typically contain 3% and 6% Re in weight, 
respectively. Unfortunately, Re is an extremely rare element on the plane t, which makes the 
alloy production very expensive and greatly risky [6]. Moreover, the promot ed level of 
refractory elements increases the alloy density and makes the alloy prone to the formation of 
detrimental topologically close -packed (TCP) phases [7-9], resulting in counteracting their 
strengthening effects. Therefore, it is of great interest to design new alloys with refractory 
elements, especially Re, being used more effectively. 
Recently, a number of methods have been proposed for designing SC superalloys , 
indicating a potential space for optimizing the alloy compositions. Fink et al [6] have proposed 
“reduced rhenium” alloys René N500 and René N515 with creep resistance close to René N5 
using neural net models, which however rely on proprietary alloy databases. Wahl and Harris 
[10,11] have disclosed a Re -free alloy CM SX-7 and a low -Re alloy CM SX-8, which bear 
temperature capabilities close to CMSX-4. Utilizing the CALPHAD method [12-14], Reed et 
al [15,16] have proposed the alloys-by-design method s, which turn out to be successful in 
designing three new alloys ABD-1/2/3. Rettig et al [17,18] have developed Re-free alloy s 
ERBO/13 and ERBO/15 by applying numerical multi -criteria optimization algorithm using 
thermodynamic calculations, which can reduce the calculation time and find global optimized 
solution. Gong et al [19] have developed a low-Re alloy QTSX based on QuesTek’s proprietary 
ICME design platform. 
In the above mentioned methods, although the alloys-by-design methods are sort of time-
consuming, they are very flexible and dynamic since the design space, design constraints and 
design targets can be customized according to specific application need [16]. More profoundly, 
Page 2 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 4

they are established on the basis of composition-structure-property correlation, and any theory-
based property model can be integrated with to guide the design procedure. In the present study, 
the principles of the alloys-by-design methods are employed to explore the design space for 
Re-free alloys; meanwhile, several property models are changed to fit the modelling procedures. 
A regression analysis for density is built trying to promote the prediction accuracy with respect 
to Caron’s density model [20]. Regression models for lattice parameters of the γ and γ′ phases 
are also proposed using thermodynamic calculations. In addition, a new model for creep 
resistance is proposed with the aid of the CALPHAD method. A series of design constraints of 
calculated properties are defined to screen the alloys with an optimum microstructure. The 
targeted properties of the modelling procedures focus on alloy density and creep resistance of 
SC superalloys. Two alloys are tested to validate the effectiveness of design constraints and the 
proposed property models. 
 
2. Methods 
2.1. Property models 
2.1.1. Alloy density 
A multiple regression model for alloy density has already been proposed by Caron [20] 
for SC superalloys, which can be expressed as follow, 
 
3(g/cm ) 8.296 0.00435 0.0164 0.01295 0.06274
0.0593 0.01811 0.06595 0.0236 0.05441
Co Cr Mo W
Re Ru Al Ti Ta
C C C C
C C C C C
          
         (1) 
where Ci presents the weight percent of element i in the alloy. This model has been widely used 
in developing new alloys [15,17]. However, it was established nearly 20 years ago, and seemed 
to be only valida ted for the densities higher than 8.6 g/cm 3. When it is applied to alloys with 
lower densities, estimated values with large errors can be found generally. Taking CMSX-6 for 
an example, the estimated density is 7.83 g/cm3, which exhibits a relative error of about 1.9 % 
comparing to the measured value 7.98 g/cm3. This deviation may cause misleading in selecting 
candidate compositions when developing alloy with low density. 
With 86 data in literatures [2,10,15,21-24], 9 measured data on our own and 105 data from 
JMatPro [25], the regression coefficients for Caron’s density model were updated, resulting in 
a model formulated as below, with the p-values of all variables and R2adj provided, 
 
3(g/cm ) 8.939 0.0014 0.0197 0.0125 0.0436
0.0508 0.0194 0.128 0.0498 0.0409
Co Cr Mo W
Re Ru Al Ti Ta
C C C C
C C C C C
          
         (2) 
Variable Intercept CAl CCo CCr CMo CW CRe CRu CTi CTa 
p-value * * 0.07 * ** * * ** * * 
R2adj 0.989 
* lower than 10-50; ** lower than 10-10. 
The model (Eq. 2) has identical form with the Caron’s (Eq. 1); however, the intercept is 
Page 3 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 5

increased from 8.296 to 8.939, which almost equals to the density of pure Ni. This accords well 
to the situation when all alloying elements are absent. In addition , the coefficients for Ci are 
changed as indicated in Fig. 1, with the relative density discrepancies between element i and 
Ni, i.e. (ρi-ρNi)/ρNi, also calculated and shown. For elements lighter than Ni, the coefficients are 
negative in both models, which means alloying with them leads to decreas ing in density. The 
situation is inverted for heavier metals. However, in the updated model, the coefficients for 
contents of Al, Ti, Cr, Ta, W and Re are all apparently decreased, and the coefficient for Co 
content becomes very close to zero for the possible reason that Co has almost identical density 
with Ni. In addition, the p-value of the coefficient for Co content is a greater than 0.05, which 
indicates it may have insignificant influence on the alloy density. Only the coefficients for Mo 
and Ru contents remain nearly unchanged. 
 
 
Fig. 1. Comparison of regression coefficients of Caron ’s model and the updated model. The 
relative density discrepancies between elements and Ni are shown in order to understand the 
sign and magnitude of the coefficients. 
 
Fig. 2 shows the comparison of densities estimated by Caron ’s model and the updated 
model for 95 SC superalloys [2,10,15,21-24]. It shows that Caron’s model tends to undervalue 
the densities in the range bel ow 8.6 g/cm3, such as for CMSX -6, SC16 and DD3 (see relative 
errors indicated in brackets); while the updated model has better predictive capability in the 
density range from 8.0 to 9.2 g/cm3. The underestimates of Caron’s model in the lower density 
range can be ascribed to its underestimated intercept and overestimated regression coefficients 
in the higher density range. 
 
Al Ti Cr Co Mo Ru Ta W Re
-0.15
-0.10
-0.05
0.00
0.05
0.10
0.15
Density Coefficient (gcm-3wt%-1)
Element
 Caron's model
 The updated model
-1.5
-1.0
-0.5
0.0
0.5
1.0
1.5
(ρi-ρNi)/ρNi
Page 4 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 6

Fig. 2. Density prediction with Caron’s model and the updated model for the 86 SC superalloys 
[2,10,15,21-24]. The relative error of the predicted density by Caron’s model is shown in 
bracket for three alloys. 
 
2.1.2. γ and γ′ lattice parameters 
Caron [20] has also proposed the regression models to estimate the lattice parameters of 
the γ and γ′ phases at room temperature, which are widely used by others [2,15-17]. However, 
the γ/γ′ misfit is strongly dependent on the temperature, and it is t he value at the operating 
temperature that may determine the kinetics of γ′ coarsening and matters significantly [26]. 
Moreover, the compositions of γ and γ′ phases for Caron’s model are estimated by PHACOMP 
method [27], which is totally empirical and thus may be not suitable for coupling with the 
CALPHAD method. In this work, modelling of γ and γ′ lattice parameters are carried out at 
900 °C, which is a key operating temperature for turbine blades [16]. Table 1 shows the 
concentration range of all elements for the 113 alloys used for modelling. With TTNi8 database 
(Thermotech, Surrey, UK), the compositions of γ and γ′ phases and the lattice parameters are 
calculated using Thermo-Calc [12] and JMatPro, respectively, and then regression analysis for 
the γ and γ′ lattice parameters are established, which take the forms as shown in Eq.3 and Eq.4, 
respectively, with the p-values of all variables and R2adj provided, 
 
Table 1. The concentration ranges (wt.%) of the 113 alloys used for lattice misfit modelling. 
Element Al Co Cr Mo W Ti Ta Re Ru Ni 
Range 3.5~6.4 0~16.5 2~16 0~4 0~10 0~4.75 0~12 0~6.4 0~6 Bal. 
 
 
( ) 3.5582 0.369 0.0243 0.161 0.4573
0.4322 0.283 0.79 0. 9 4
Å
53 0.5
Al Co Cr Mo
Re Ru Ta Ti W
a x x x x
x x x x x
   

    
        
          (3) 
7.8 8.0 8.2 8.4 8.6 8.8 9.0 9.2 9.4
7.8
8.0
8.2
8.4
8.6
8.8
9.0
9.2
9.4
DD3 (-1.40%)
SC16 (-3.17%)
 Caron's model
 The updated model
 Fit of Caron's model 
 Fit of the updated model 
Predicted density (g/cm3)
Measured density (g/cm3)
R2
adj=0.984
R2
adj=0.959
CMSX-6 (-1.89%)
Page 5 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 7

Variable Intercept xγAl xγCo xγCr xγMo xγW xγRe xγRu xγTi xγTa 
p-value * * * * * * * * * * 
R2adj 0.999 
* lower than 10 -40. 
 
 
'( ) 3.5328 0.3336 0.2791 0.5507 0.552
0.3717 0.7284 0.4759 0.4 81
Å
9
Al Cr Mo Re
Ru Ta Ti W
a x x x x
x x x x
   

   
   
   
        
        (4) 
Variable Intercept xγ′Al xγ′Cr xγ′Mo xγ′W xγ′Re xγ′Ru xγ′Ti xγ′Ta 
p-value * * * * * * * * * 
R2adj 0.999 
* lower than 10-30. 
here xγi and xγ′i stand for atomic fractions of element i in the γ and γ′ phase, respectively. The 
unconstrained γ/γ′ lattice misfit at 900 °C is calculated by the common definition as below, 
 
2( ) 100%aa
aa





  (5) 
The dependence of γ/γ′ misfit on temperature should be considered in two aspects, i.e. 
thermal expansion effect and thermodynamic equilibrium. In lower temperature regime where 
diffusion is suppressed and thermal expansion dominates, the change of lattice parameters can 
be estimated using the methods proposed in literatures [15,17]. However, in higher temperature 
regime, the γ′ phase dissolves rapidly and then the compositions of γ and γ′ phases will change 
to approach new state of chemical equilibrium; therefore, the change of lattice parameters 
should be estimated by not only the thermal expansion effect, but also the repartitioning of 
elements into γ and γ′ phases. This nonlinear behavior needs further investigations. 
2.2.3. Creep resistance model 
A number of models for creep resistance have been developed in literatures [15-17,28]. 
Considering the diffusion-controlled process during high temperature creep deformation, Reed 
et al [15, 16] have proposed a creep merit index ( Mcreep), which integrates the effect of all 
alloying elements on slowing down the diffusion rate during creep and is defined as following, 
 
/creep i i
i
M x D 
 (6) 
where xi is the atom fraction of element i in the alloy and 𝐷̃𝑖 is the corresponding interdiffusion 
coefficient. A strong correlation is observed between the measured Larson -Miller parameter 
and the creep merit index for a number of widely researched alloys [16]. However, this theory-
based model assumes that the γ′ fraction is fixed for all alloys, which may overlook the variation 
of precipitation hardening due to different fractions of γ′ phases. 
Yokokawa et al [28] have proposed a regression model for creep -rupture life, which is 
defined as below, 
Page 6 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 8

2
0log( ) ( )i i j k f optC C X C C V V      (7) 
where τ is the creep-rupture life, Xi is the concentration of element i in γ′ phase at temperature 
T, δ is the lattice misfit at temperature T, Vf is the γ′ phase volume fraction at temperature T, 
and C0, Ci, Cj, and C k are regression coefficients. Vopt is defined as the optim al γ′ fraction at 
temperature T which comes from the value reported by Murakumo et al [29]. This model shows 
good prediction accuracy for creep -rupture lives at both 900 °C/392 MPa and 1100 °C/ 137 
MPa. It indicates, apart from alloying elements, the microstructural parameters δ and Vf also 
have significant impact on creep resistance. However, to our knowledge, the data used for 
regression analysis of creep-rupture life and lattice misfit are not disclosed in related literatures 
[28,30], making it difficult to reproduce these models to evaluate unknown alloys. 
Based on the work of Fleischmann et al [31], Rettig et al [17] have employd a solid 
solution strengthening index (ISSS) for evaluating the creep-rupture lifetime, which weights the 
relative effectiveness of the three most potent solid solution strengtheners, i.e. Re, W and Mo, 
to reduce the creep rate in high temperature regime, and has the form as following, 
 
2.44 1.22SSS Re W MoI x x x        (8) 
where xγi is the concentration (at.%) of element i in the γ matrix calculated via CALPHAD for 
required temperature. Like Mcreep, Isss may only take into consideration the diffusion-controlled 
glide/climb process retarded by solid solution strengthening mechanism, which is convenient 
when the fraction and size of γ′ precipitates are assumed fixed at the required temperature; 
however, this confines designing alloys with various amount of γ′ phases. 
According to the models mentioned above, attempts are made in this work to measure the 
contribution of the solid solution strengthening in γ matrix, the precipitate hardening of γ′ phase 
and coherency strengthening from γ/γ′ interface to creep resistance together. For solid solution 
strengthening in γ matrix, a solid solut ion strengthening index s is defined equal to ISSS. For 
precipitate hardening of γ′ phase and coherency strengthening from γ/γ′ interface, the γ′ fraction, 
denoted as f, and the value of lattice misfit δ (Eqs. 3-5), are employed, respectively. All these 
values are calculated via Thermo-Calc with TTNi8 at 900 °C. 
The values of s, f and δ are supposed to be normalized before modelling since they have 
different dimensions. It is known [32] that the second generation alloy CMSX-4 is one of the 
most successful alloys that has been extensively used in aero and industry turbine applications, 
which has shown an excellent combination of high temperature strength and phase stability. 
This can be attributed to its close to optimum microstructural architecture [2], including ~70 
vol.% of γ′ phase and an appropriate γ/γ′ misfit to confer cuboidal γ′ precipitates with a uniform 
size of ~0.5 μm after heat treatment . Furthermore, it is assumed that the refractory metals, 
especially Re, are most effectively used in CMSX-4 without impairing phase stability. Thus, 
CMSX-4 is selected as the alloy for normalization in this work. Using the n ormalized values 
calculated at 900 °C and the Larson-Miller parameter at 300 MPa (LMP) for 14 SC superalloys 
Page 7 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 9

in literatures [10,16], a linear regression model is established, which takes the form as below, 
the p-values of all variables and R2adj provided. 
 
23.899 1.406 2.193 0.0559.942at.% 64.5mol.% 0.169%
sfLMP        (9) 
Variable Intercept s* f* δ* 
p-value 4.2×10-13 3.6×10-7 1.1×10-3 0.27 
R2adj 0.969 
* values after normalization. 
here the normalization bases are the solid solution strengthening index, γ′ fraction and 
magnitude of lattice misfit in CMSX-4 calculated at 900 °C, respectively. Fig. 3 shows that this 
model can reproduce the Larson-Miller parameters with a stronger correlation than the creep 
merit index model (Eq. 6) for the alloys investigated. 
 
 
Fig. 3. Correlations of the predicted LMP and the creep merit index with the measured Larson-
Miller parameters at 300 MPa taken from literatures [10,16], respectively. The two alloys for 
experimental validations are also shown. 
 
2.2. Modelling procedures 
Integrating with the property models (Eq. 2, 5, 9), a framework for systematic modelling 
can be built referring to the alloys-by-design methods [15], as depicted in Fig. 4. 
 
26.0 26.5 27.0 27.5 28.0 28.5 29.0
26.0
26.5
27.0
27.5
28.0
28.5
29.0
PWA1483
MD2
CMSX-2
SRR99
ReneN5
CMSX-7
TMS-82+
CMSX-4
MC-NG
TMS-75
CMSX-10
TMS-138A
TMS-162
CMSX-8
SC21
 Predicted LMP at 300 MPa 
 Creep merit index 
 LMP of two experimental alloys 
Predicted LMP at 300 MPa
Larson-Miller Parameter at 300MPa, P = T[20+lg(t)]/1000
R2
adj = 0.969
SC11
0
2
4
6
8
10
12
14
16
R2
adj = 0.814
Creep Merit Index (m-2s  1015)
Page 8 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 10

Fig. 4. Illustration of the framework for modelling procedures. 
 
Considering the common elements added in the developed SC superalloys [1], the Ni-Cr-
Co-Al-Ti-Ta-Mo-W alloy system was selected for designing Re-free alloys. Table 2 shows the 
definitions of composition range and step size for each element in weight percent . The 
composition ranges were se lected according to th ose of first - and second -generation SC 
superalloys, and the step sizes were set differently to make similar resolutions in atomic percent 
(0.3~0.6 at.%) for alloying elements except Co, which was considered interchangeable with Ni 
in the range . Additional ranges were defined for Mo and W to explore their strengthening 
potentials, since they are regarded as the two most potent solid solution strengtheners when Re 
is absent. A total number of 153125 alloys were generated in the design space according to this 
configuration. 
 
Table 2. The definitions of composition range and step size for each element (wt.%). 
Element Ni Al Ti Cr Co Mo Ta W 
Upper limit Bal. 6.3 2.5 8.0 9.5 6.5 8.5 8.8 
Lower limit Bal. 5.5 0.5 6.0 5.5 0.5 4.5 1.6 
Step size - 0.2 0.5 0.5 1.0 1.0 1.0 1.2 
 
The thermodynamic properties were calculated using Thermo-Calc software package 
(version 3.0.1) coupled with TTNi8 database. A program developed on our own was used to 
guide the calculation process automatically . Only the liquid, γ and γ′ phases were included 
during calculations; other possible phases such as TCPs w ere suppressed. This was based on 
the assumption that only the γ and γ′ phase were present when the alloy begins in service and 
the formation of other phases was delayed due to kinetics factors. Instead, the propensity for 
Page 9 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 11

TCP formation was estimated using the PHACOMP method [35], by which a phase stability 
number Md̅̅̅̅ = ∑ 𝑥𝑖𝑀𝑑𝑖 was given, where xi and Mdi were the mole fraction and the d-orbital 
energy level of element i, respectively. Nevertheless, the thermodynamic calculations with all 
possible phases included were still performed in parallel for the defined alloy space (Table 2), 
and then the total amount of TCPs calculated could be compared with Md̅̅̅̅, as shown in Fig. 5. 
It indicates that by limiting Md̅̅̅̅ below a value, the total amount of TCPs calculated will also 
be safely suppressed below specific values at various temperatures. 
 
 
Fig. 5. Scatter diagram of the computed Md̅̅̅̅ value and the total amount of calculated TCPs at 
various temperatures for the alloy space defined. The alloys with zero TCPs are not shown. 
 
It is well accepted that an optimum microstructure for SC superalloys [2,29] consists of 
60~70 vol.% of γ′ precipitates with cuboidal shape and size of about 0.5 μm, which are evenly 
embedded in the γ matrix after proper heat treatment. This is defined in this work as the targeted 
microstructure, and is considered to be related to five properties, including γ′ fraction, γ′ solvus 
temperature, heat treatment window (HTW), γ/γ′ lattice misfit and phase stability number Md̅̅̅̅,. 
The corresponding reasons are given as following, 
a) The γ′ fraction changes with temperature, and a certain temperature should be selected to 
estimate the γ′ fraction after heat treatment. Here, 900 °C is selected s ince the SC 
superalloys are generally aged near this temperature at last stage and the phase fractions 
should be kept thereafter due to subsequent rapid cooling. 
b) The γ′ solvus temperature should be high to maintain γ′ phases as much as possible at 
service temperatures [20]. 
c) The HTW should be practically broad to allow solution heat treatment to conveniently 
remove the microstructural inhomogeneity due to the dendritic solidification. 
d) The γ/γ′ lattice misfit also depends on temperature. A suitable γ/γ′ misfit should be present 
at the ageing temperature to make sure γ′ precipitates grow into cuboidal shape and reach 
the ideal size at a limited coarsening rate. This temperature can also be set at 900 °C. 
e) The phase stability number Md̅̅̅̅ should be below a critical value to suppress the excessive 
Page 10 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 12

formation of TCP phases, as suggested in Fig. 5. 
To estimate the proper ranges for these properties, calculations were previously tested on 
24 SC superalloys in different generations, which were all considered exhibiting the targeted 
microstructure after corresponding heat treatments. Fig. 6 shows the results, with shaded areas 
depicting the suggested property ranges, which are summarized as following: 
(1) γ′ fraction at 900 °C: 60 mol.% ~ 70 mol.%; 
(2) γ′ solvus: higher than 1250 °C; 
(3) HTW: broader than 40 °C; 
(4) γ/γ′ misfit at 900 °C: -0.3 % ~ -0.1%; 
(5) Md̅̅̅̅: lower than 0.99. 
As shown in Fig. 6, the constraint for γ′ fraction includes 87.5 % of the tested alloys; the 
bottom limit of γ′ solvus seems to be the boundary line between the first and higher generation 
alloys; the constraint for HTW only excludes the alloy CMSX-7, which requires a sophisticated 
solution treatment [36]; the constraint for γ/γ′ lattice misfit at 900 °C almost includes all those 
of first- and second-generation alloys. As for Md̅̅̅̅, although values higher than 0.99 eV often 
appears in Re-free alloys, it can still be set below 0.99 eV to safely suppress the formation of 
TCP phases, as the reference suggested [26]. 
 
 
Fig. 6. The suggested property ranges (the shaded areas) learned from the calculation of 24 SC 
superalloys in different generations. The fractions of alloys in the ranges are also shown. 
 
Applying these constraints successively to the design space defined (Table 2), 3919 alloys 
were isolated. Table 3 lists the number and percentage of computed alloys violating each of the 
suggested property ranges. It can be seen that the γ/γ′ misfit and Md̅̅̅̅ value have the highest 
55
60
65
70
75
1150
1200
1250
1300
1350
40
80
120
-0.8
-0.6
-0.4
-0.2
0.0
0.2
CMSX-2CMSX-6Nasair100PWA1483PWA1480
SRR99AM1AM3
ReneN4
MC2
CMSX-7CMSX-8TMS-82+ReneN5CMSX-4PWA1484CMSX-10ReneN6TMS-75MC-NGEPM-102TMS-138TMS-162TMS-196
0.96
0.97
0.98
0.99
1.00
1.01 γ′ fraction (%)
87.5 %
62.5 %
γ′ solvus (°C)
95.8 %
HTW (°C)γ/γ′ misfit (%)
66.7 %
75.0 %
Md (eV)
Single Crystal Superlloys
1st generation 2nd 3rd 4th & 5th
Page 11 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 13

effectiveness for property screen. 
 
Table 3. The number and percentage of alloys violating each suggested property range. 
Property γ′ fraction γ′ solvus HTW γ/γ′ misfit Md̅̅̅̅ 
Number 90885 72179 39973 134692 109300 
Percentage 59.4% 47.1% 26.1% 87.9% 71.4% 
 
After that, the density model (Eq. 2) and creep resistance model (Eq. 9) were used for 
optimal property selection. The a lloys with lower density and higher creep resistance are 
preferable. Fig. 7 shows the scatter diagram of the predicted density and LMP for the isolated 
alloys. It is indicated that higher LMP is generally related to higher density. Comparing to the 
predicted values of 15 developed SC alloys shown in Fig. 7, the LMPs of the isolated alloys 
overlap those of first-generation alloys, but hardly reach the level of the second-generation. 
However, a large number of isolated alloys fill the gap between the first and second generation 
alloys, and several bear comparable LMPs to the newly-developed alloy CMSX-7. It suggests 
there exists optimization space for the compositions defined in Table 1 , but perhaps no alloy 
can reach the creep resistance level of the second-generation at high temperatures. 
It is feasible to set more stringent constraints to reduce the number of isolated alloys, and 
then set smaller step sizes around the compositions of most preferable alloys to obtain refined 
calculations, or expand the composition ranges to explore additional design space. Moreover, 
other property models, such as the models for cost [15], castability [15,19,37] and oxidation 
resistance [16,38], can be employed to select alloys with more required properties. This will 
become a problem dealing with multi-criteria optimization; the global optimization method [17] 
and genetic algorithm [39] are suitable for designing superalloys in this fashion. However, the 
reliability of the results inferred from these methods depends heavily on the effectiveness of 
the property models employed. Therefore, the design constraints and the established models in 
this work needs validations for further usage in the optimization methods. 
 
 
7.9 8.0 8.1 8.2 8.3 8.4 8.5 8.6 8.7 8.8 8.9 9.0
26.4
26.5
26.6
26.7
26.8
26.9
27.0
27.1
27.2
27.3
27.4
27.5
27.6
SC21
SC11
CMSX-2
CMSX-6
Nasair100
PWA1483
PWA1480
SRR99 MD2
AM1
AM3
CMSX-7
TMS-82+
ReneN5
CMSX-4
ERBO/13ERBO/15
2nd generation alloys
Predicted LMP at 300 MPa
Predicted Density (g/cm3)
1st generation alloys
Page 12 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 14

Fig. 7. Scatter diagram of predicted LMP against density for isolated 3919 alloys (dots) and 15 
developed SC alloys (closed circles). Two experimental alloys (triangles) for validations are 
also shown. 
 
2.3. Alloys for experimental validations 
Table 4 shows the nominal composition (in wt.%) of two alloys, SC11 and SC21, used for 
validations; the calculated properties were also listed . They are within the composition range 
defined in Table 2, except for the 0.3 wt.% of Ti in SC11. The two compositions are identical 
in Cr and Co, similar in Al and Ti; however, the SC11 is significantly higher in Mo but much 
lower in W and a little lower in Ta. Table 2 also shows that SC11 violates the constraints for 
γ/γ′ misfit and phase stability number depicted in Fig. 6; while SC21 obeys all the defined 
constraints. In addition, comparing to the second generation alloys (Fig. 7), SC11 has a lower 
predicted density and surprisingly an almost equivalent LMP; while SC21 has a comparable 
density but lower LMP, which nonetheless is higher than those of the first generation alloys . 
Therefore, these two alloys are convenient for verifying the property constraints set for 
microstructure and the updated models for density and creep resistance. 
 
Table 4. Nominal compositions (wt.%) and calculated properties of alloys for validations. 
Alloy Ni Cr Co Al Ti Ta Mo W 
SC11 Bal. 6.0 6.2 6.05 0.3 6.8 6.5 3.8 
SC21 Bal. 6.0 6.2 5.75 0.5 8.0 1.5 8.0 
Calculated properties 
Alloy s 
(at.%) 
f 
(mol.%) 
δ 
(%) 
γ′ solvus 
(°C) 
HTW 
(°C) 
Md̅̅̅̅ 
(eV) 
ρ 
(g/cm3) LMP 
SC11 10.12 66.0 -0.50 1261.5 63.9 0.992 8.550 27.41 
SC21 6.84 69.2 -0.14 1291.9 41.5 0.988 8.747 27.17 
 
3. Experimental 
Ingots of alloy SC 11 and SC21 with 72 mm in diameter and >600 mm in length were 
produced by vacuum induction melting (VIM) in Cannon -Muskegon Corporation, USA, with 
the measured compositions provided. The ingots were sectioned and then re-melted in a high 
rate solidification furnace (ALD furnace ) at 1500 °C and directionally solidified using 
Bridgman method wit h the withdraw rate of 3 mm/min . Single crystal rods of 16 mm in 
diameter, 160 mm in length were fabricated, and the surfaces were etched by a solution of 75% 
HCl + 25% H2O2 to visually confirm the crystal integrity. The crystallographic orientations of 
the rods were examined by Laue backscatter method. The as-cast rods were solution treated at 
1308 °C for 12 h followed by air cooling, and then were aged at 1080 °C for 4 h, quenched by 
air and aged at 870 °C for 16 h, also quenched by air. Density tests were carried out on an 
electronic density meter (Sartorius YDK03) using the Archimedes’ principle. 
Long term thermal exposure was performed for fully heat treated alloys at 1100 °C up to 
Page 13 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 15

1000 h. The heat treated and thermal exposure samples were grinded, polished and etched with 
a solution of 33% HNO 3, 33% acetic acid, 33% H 2O, and 1% HF for 10 s, which dissolved γ′ 
phases. Microstructures were observed using a scanning electron microscope (SEM , FEI 
Quanta 650). The area fractions of γ′ precipitates in fully heat treated alloys and TCP phases in 
thermal exposed alloys were determined using ImageJ software package. SEM micrographs in 
backscattered electron (BSE) imaging mode were employed for measuring TCP phases since 
they exhibited sharp contrast in this mode. At least 15 fields were evaluated using a threshold 
method to obtain the average area fractions, which were then considered as the volume fractions. 
Creep rupture specimens of 25 mm in gauge length and 5 mm in diameter were prepared 
from the heat treated rods with axis orientation within 10° from [001]. In order to compare with 
the creep rupture lives of CMSX-7, tensile creep tests were performed at three conditions listed 
in the reference [36], including 850 °C/650 MPa, 982 °C/248 MPa and 1040 °C/145 MPa. The 
ruptured specimens were sectioned and prepared for SEM observation. 
 
4. Results and discussions 
4.1. Density and Microstructure 
The measured compositions and experimentally determined densities of the two alloys are 
shown in Table 5. The actual compositions of the alloys were in excellent agreement with the 
nominal compositions. Moreover, the measured densities were almost identical to the predicted 
values (Table 4), which demonstrated the excellent predictive capability of the updated density 
model (Eq. 2) . By contrast, Caron’s model (Eq. 1) can also show a very close value of 8.74 
g/cm3 for SC21; however, it produces an underestimated value of 8.45 g/cm3 for SC11, resulting 
in a relative error of nearly 1.0 %. The lower density in SC11 can be mainly attributed to its 
lower contents in Ta and W and higher content in Mo, since Mo has a density (10.28 g/cm 3) 
much lower than those of Ta (16.68 g/cm3) and W (19.26 g/cm3). 
 
Table 5. The measured composition (wt.%) and density (g/cm3) of experimental alloys. 
Alloy Cr Co Al Ti Ta Mo W Ni Density 
SC11 6.0 6.2 6.03 0.22 6.8 6.5 3.72 Bal. 8.54 
SC21 5.9 6.2 5.76 0.61 8.0 1.5 8.0 Bal. 8.75 
 
No incipient melt ing was observed in SC11 and SC21 after solution treatment. In both 
alloys, the γ′ precipitates were uniformly distributed in the γ matrix and no TCP phases were 
observed after ageing treatment, as shown in Fig. 8. Image analysis showed that t he γ′ phase 
fractions were about 64 vol.% in SC11 and about 68 vol.% in SC21. Since the predicted misfits 
are rather small (Table 4), the γ′ volume fractions should be very close to the γ′ mole fractions 
for both alloys. It is indicated that the γ′ volume fractions observed are in good agreement with 
the γ′ mole fractions c alculated at 900 °C ( Table 4). This suggests that the thermodynamic 
Page 14 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 16

database used can be reliable for predicting phase fractions at room temperature when a proper 
equilibrium temperature is figured out. However, the γ′ precipitates in SC11 were irregular-
shaped and most of them already coalesced with each other (Fig. 8 a). By contrast, the γ′ 
precipitates in SC21 had cuboidal shape with sharp corners, with edge length about 0.6 μm on 
average (Fig. 8b), which met the targeted microstructure proposed for modelling. 
 
 
Fig. 8. SEM micrographs of the microstructure of fully heat-treated alloys. 
 
The coalescence of γ′ phases in SC11 at the early stage of ageing treatment can be related 
to its too large misfit (Table 4), which is out of the constraint range (Fig. 6). This inappropriate 
misfit in SC11 may raise a γ/γ′ interfacial energy beyond a coherent interface can hold, resulting 
in the rapid loss of elastic coherency and γ′ directional coarsening during ageing treatment 
[40,41]. On the other hand, large negative misfit turns out to be permissible in fourth- and fifth-
generation alloys with high Re contents, such as TMS-162 and TMS-196 shown in Fig. 4. Study 
[42] also shows that large negative misfit is favorable in designing TMS-162, since it can impart 
fine dislocation networks at γ/γ′ interface during creep. One reasonable explanation is that the 
presence of high amount of refractories, particularly Re, in high-generation alloys significantly 
reduces the bulk diffusion rate [43], which retards the γ′ coarsening process [44] and thus may 
allow a high misfit. Therefore, it suggests the misfit should be limited to a rationally low level 
for designing Re-free or low-Re alloys. 
The microstructures of the alloys subjected to long-term thermal exposure at 1100 °C are 
shown in Fig. 9 , which indicates a significant γ′ coarsening an d the extent of TCPs with 
increasing exposure time (Table 6). After 500 h exposure, the shape of γ′ precipitates was more 
irregular and massive TCP blocks were found in SC11 (Fig. 9a); while the γ′ precipitates were 
coarsened into rafts and a limited amount of needle-shaped ( probably plate -like in 3D 
perspective) TCPs were found in SC21 (Fig. 9b). As exposure time increased to 1000 h , the 
morphology of TCPs was nearly unchanged for either SC11 (Fig. 9c) or SC21 (Fig. 9d), but the 
volume fractions were increased (Table 6). Thermodynamic calculations also show SC11 will 
form a high amount of μ phase at 700 and 900 °C, while SC21 will only form limited amount 
of P phase at 700 °C (Table 6). The different morphology of TCPs formed in SC11 and SC21 
may be ascribed to the kind of TCPs predicted. 
 
Page 15 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 17

Fig. 9. SEM micrographs of the microstructures of the fully heat -treated alloys exposed at 
1100 °C. The TCP phases in SC11 are indicated by white arrows. 
 
Table 6. The fractions of TCPs by thermal exposure at 1100 °C for different times and by 
thermodynamic calculations at various temperatures (with the predicted phase in bracket). 
Alloy 
Thermal exposure time (vol.%) Thermo-Calc with TTNi8 (mol.%) 
0 500 h 1000 h 700 °C 900 °C 1100 °C 
SC11 0 1.56 ± 0.53 2.28 ± 0.80 7.87 (μ phase) 4.05 (μ phase) 0 
SC21 0 1.23 ± 0.19 1.58 ± 0.30 1.64 (P phase) 0 0 
 
The microstructures of long-term exposed SC11 and SC21 indicate they are both lack of 
phase stability, although the Md̅̅̅̅ value of SC21 (Table 4) meets the constraint (Fig. 6). This 
demonstrates that the critical value for Md̅̅̅̅ may not be properly defined, or alternatively, the 
PHACOMP method may has limitation in predicting TCPs formation with high accuracy. 
Nevertheless, a higher amount of TCP phases is formed in SC11 than that in SC21 ( Table 6), 
which suggests the Md̅̅̅̅ value may be right in predicting the pr opensity of TCP formation. 
Pyczak and Mughrabi [46] have given a detailed explanation for new PHACOMP method, 
which indicates that the critical stability number is dependent on alloy composition. In addition, 
although alloy CMSX-7 has a Md̅̅̅̅ value higher than 0.99 eV ( Fig. 6), it is reported to have 
excellent phase stability [10]. Reed et al [16] also find the limitation of new PHACOMP method 
in the newly -designed alloys and propose an updated version of structure map based on the 
CALPHAD data and the work of Seiser et al [47], which shows better prediction capability for 
TCP phases. However, the prediction accuracy of this method also needs further validations. 
4.2. Creep rupture behavior 
Fig. 10a. shows the creep rupture lives of alloy SC11 and SC21 under three test conditions, 
Page 16 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 18

the corresponding data of CMSX-7 [37] are also shown. Comparing to CMSX-7, SC11 is much 
short in rupture life at each condition; however, SC21 exhibits longer life at 850 °C/650 MPa 
and 1040 °C/145 MPa but shorter life at 982 °C/ 248 MPa. Fig. 10b shows the Larson-Miller 
diagrams of SC11 and SC21 for rupture lives, with the creep data of CMSX-7 and CM SX-4 
taken from the literature [10]. The creep performance of SC21 was found to be very close to 
CMSX-7 in the tested stress range , and comparable to CMSX-4 at 650 MPa ; however, SC11 
exhibited much inferior creep resistance at all test conditions. 
 
 
Fig. 10. (a) Creep rupture lives of SC11 and SC21 at different test conditions and (b) Larson-
Miller curves of SC11 and SC21 for rupture life. 
 
Fig. 11 shows the microstructure of the creep ruptured samples at the gauge sections. After 
rupture at 850 °C/650 MPa, a large number of small TCP blocks were formed and significant 
γ′ coarsening occurred in SC11 (Fig. 11a), while the morphology of γ′ precipitates in SC21 was 
nearly not altered except that the cuboidal shape seemed stretched along the load direction (Fig. 
11b). After rupture at 982 °C/248 MPa, γ′ rafts perpendicular to load directions were formed in 
both SC11 and SC21; however, a large number of TCP phases were observed in SC11, breaking 
the γ′ rafts (Fig. 11c), while only a limited number of TCP phases with small size were found 
in SC21 (Fig. 11d). After rupture at 1040 °C/145 MPa, the rafted structure broke up and were 
significantly twisted; meanwhile a larger amount of TCP phases formed in SC11 than in SC21. 
 
 
850°C/650MPa 982°C/248MPa 1040°C/145MPa
0
50
100
150
200
250
300Rupture life (h)
Creep rupture condition
 SC11
 SC21
 CMSX-7
(a)
24 25 26 27 28 29 30 31
100
200
300
400
500
600
700
800(b)
CMSX-4
CMSX-7
SC21
Stress (MPa)
Larson-Miller parameter, P=T[20+lg(t)]/1000
SC11
Page 17 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 19

Fig. 11. SEM micrographs (BSE mode) of microstructures of the creep ruptured specimens at 
gauge sections. 
 
The measured Larson-Miller parameters at 300 MPa of SC11 and SC21 can be estimated 
by interpolating their Larson-Miller curves in Fig. 9b. The comparison of the measured and the 
predicted values can be seen in Fig. 3. Although SC11 has a predicted LMP equivalent to the 
level of the second generation alloys, it exhibited much inferior creep resistance, which means 
the creep resistance model (Eq. 10) fails in SC11 . Two main reasons can be drawn from the 
experimental results. First, the inappropriate γ/γ′ lattice misfit in SC11 has already caused loss 
of interface coherency and γ′ coalesce at the ageing stage (Fig. 8 a), result ing in the rapid 
microstructure degradation during creep deformation (Fig. 11). Secondly, the too high Md̅̅̅̅ 
value in SC11 impart s excessive amount of TCP phase s during creep deformation, which 
significantly disrupt the γ/γ′ microstructure (Fig. 11) and then degrade the creep strength . By 
contrast, the measured LMP of SC21 agrees very well with the predicted value (Fig. 3). This 
can be attributed to a targeted microstructure obtained in SC21, which is very likely because 
this alloy conforms all the defined property constraints . In addition, although substantial TCP 
phases have formed in SC21 by long -term thermal exposure ( Fig. 9), only a limited amount 
form after creep rupture at high temperatures (Fig. 11), which may have little influence on the 
creep rupture life. 
Therefore, it seems that the creep resistance model (Eq. 9) may be only applicable when 
the targeted microstructure is satisfied. To further illustrate this point, the LMPs of the newly-
developed Re-free alloys ERBO/13 and ERBO/15 are calculated, which are found close to the 
level of the second generation alloys, as shown in Fig. 7. These LMPs should be correctly 
predicted since the se two alloys exhibit creep resistance comparable to CMSX -4 in high 
Page 18 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 20

temperature regime [17,18]. The effectiveness of this model in ERBO/13 and ERBO/15 may 
also depend on the targeted microstructures obtained [17,18]. However, whether the alloy that 
doesn’t have the targeted microstructure will certainly have poor creep resistance is not much 
clear. 
Considering the creep resistance model proposed (Eq. 9), the coefficient for normalized δ 
is much less than those for normalized s and f; in addition, the p -value of this coefficient is 
greater than 0.05 (Eq. 9), which both suggest the misfit is of little significance to model the 
Larson-Miller parameters at 300 MPa. One possible explanation is that, at 900 °C, the variable 
δ is strongly dependent on the variable s. Fig. 12 shows the correlations among these variables 
for the 14 alloys (see Fig. 3) used to establish this model. A strong positive correlation can be 
observed between s and δ (Fig. 12a); while no apparent correlation can be found between f and 
δ (Fig. 12b). Therefore, at 900 °C, the effect of δ is likely being obscured by s. This suggests 
the proposed model (Eq. 10) may be further improved by excluding the term of lattice misfit. 
 
 
Fig. 12. (a) Correlations between the solid solution strengthening (SSS) index and the misfit 
and (b) between the γ′ fraction and the misfit for the 14 investigated alloys. 
 
Similarities can be found between the proposed creep resistance model (Eq. 9) and the 
model developed by Yokokawa et al [28] (Eq. 7). Both models consist of four terms, including 
a constant and three variable terms of composition, γ′ fraction and lattice misfit. However, Eq. 
7 takes the composition of γ′ phase and the quadratic of γ′ fraction for modelling; while Eq. 9 
uses only the contents of three most potent solid solution strengtheners in γ matrix and no power 
law is applied to the γ′ fraction. Since the compositions of γ matrix and γ′ phases are coupled 
to reach thermodynamic equilibrium, Eq. 9 can be considered as a simplified model of Eq. 7. 
In addition, in the work of Yokokawa et al [28], regression analysis of creep-rupture life was 
established under two test conditions, which shows that for the life at 1100 °C/137 MPa, the 
regression coefficient for misfit is much greater than that for the life at 900 °C/392 MPa . It 
suggests if the proposed model (Eq. 9) is used for modelling the creep resistance at lower stress 
and higher temperature, the significance of the lattice misfit may become higher , which may 
expand the use of the proposed model. 
0 1 2 3 4 5
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
0 1 2 3 4 5
0.85
0.90
0.95
1.00
1.05
1.10
1.15
PWA1483
CMSX-2
ReneN5
CMSX-7
TMS-82+
CMSX-4
MC-NG
TMS-75
CMSX-10
TMS-138A TMS-162
MD2
SRR99
CMSX-8
PWA1483
CMSX-2
ReneN5
CMSX-7
TMS-82+
CMSX-4
MC-NG
TMS-75
CMSX-10
TMS-138A
TMS-162
MD2
SRR99
CMSX-8
Normalized SSS index
Normalized lattice misfit
(a)
R2=0.68
Normalized γ' fraction
Normalized lattice misfit
(b)
Page 19 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 21

5. Summary and Conclusions 
Modelling procedures were performed to explore the design space for Re-free nickel-base 
single crystal superalloys, with two alloys SC11 and SC21 tested for validation. The following 
conclusions can be drawn: 
1. A regression analysis of alloy density at room temperature is established with predictive 
capability improved. This model exactly predicts the measured density of SC11 and SC21. 
2. A regression analysis of Larson-Miller parameters at 300 MPa is established, which shows 
better predictive capability for creep resistance than the creep merit index does. 
3. The property constraints of γ′ fraction, γ′ solvus, heat treatment window, γ/γ′ lattice misfit 
and phase stability number are defined to isolate the alloys with an optimum microstructure. 
After ageing treatment, SC11 that violates the constraints of misfit and phase stability 
number exhibits premature γ′ coalescence; while SC21 that fulfills all these constraints 
exhibits an optimum microstructure. 
4. The inappropriate misfit and phase stability number in SC11 cause severe microstructure 
degradation during creep, resulting in inferior creep resistance than prediction; while SC21 
exhibits good creep resistance as expected although a limited amount of TCP phases are 
formed during high temperature creep. 
 
Acknowledgement 
The authors acknowledge the financial support from the National Key Research and 
Development Program of China (2016YFB0700300). Z. H. appreciates the project supported 
by State Key Laboratory of Powder Metallurgy, Central South University, Changsha, China. 
 
References 
[1] P. Caron, T. Khan, Evolution of Ni-based superalloys for single crystal gas turbine blade 
applications, Aerosp. Sci. Technol. 3 (1999) 513-523. 
[2] R. C. Reed, The Superalloys: Fundamentals and Applications. Cambridge: Cambridge 
University Press. 2006. 
[3] K. Harris, G.L. Erickson, W.D. Brentnall, J.M. Aurrecoechea, S.L. Sikkenga, K. G. 
Kubarych, Development of the rhenium containing superalloys CMSX-4 and CM 186LC 
for single-crystal blade and directionally solidified vane applications in advanced turbine-
engines, in: S.D. Antolovich, R.A. Stusrud, R.W. Mackay, D. L. Anton, T. Khan, R.D. 
Kissinger (Eds.), Superalloys 1992. 297-306. 
[4] S. Walston, A. Cetel, R. MacKay, K. O'Hara, D. Duhl, R. Dreshfield , Joint development 
of a fourth generation single crystal superalloy, in: K.A. Green, T. M. Pollock, H. Harada, 
T.E. Howson, R.C. Reed, J.J. Schirra, S. Walston (Eds.), Superalloys 2004. 15-24. 
[5] Y . Koizumi, T. Kobayashi, T. Yokokawa, J.X. Zhang, M. Osawa, H. Harada, Y . Aoki, M. 
Arai, Development of next-generation Ni-base single crystal superalloys, in: K.A. Green, 
Page 20 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 22

T.M. Pollock, H. Harada, T.E. Hows on, R.C. Reed, J.J. Schirra, S. Walston (Eds.), 
Superalloys 2004. 35-43. 
[6] P.J. Fink, J.L. Miller, D.G. Konitzer, Rhenium reduction -alloy design using an 
economically strategic element, JOM. 62 (2010) 55-57. 
[7] M.S.A. Karunaratne, C.M.F. Rae, R.C. Reed, On the microstructural instability of an 
experimental nickel-based single-crystal superalloy, Metall. Mater. Trans. A Phys. Metall. 
Mater. Sci. 32 (2001) 2409-2421. 
[8] C.M.F. Rae, R.C. Reed, The precipitation of topologically close -packed phases in 
rhenium-containing superalloys, Acta Mater. 49 (2001) 4113-4125. 
[9] M. V . Acharya, G.E. Fuchs, The effect of long -term thermal exposures on the 
microstructure and properties of CMSX-10 single crystal Ni-base superalloys, Mater. Sci. 
Eng. A. 381 (2004) 143-153. 
[10] J.B. Wahl, K. Harris, New single crystal superalloys, CMSX-7 and CMSX-8., in: E. Huron, 
M. Hardy, M. Mills, R. Montero, P. Portella, J. Telesman, R.C. Reed (Eds.), Superalloys 
2012. 177-188. 
[11] J. Wahl, K. Harris, New single crystal superalloys - overview and update, MA TEC Web 
Conf. 14 (2014) 17002. 
[12] N. Saunders, A.P. Miodownik. CALPHAD (Calculation of Phase Diagrams): a 
comprehensive guide, In: Cahn Robert W, editor. Pergamon materials series, vol. 1. Oxford: 
Pergamon Press, 1998. 
[13] J.C. Zhao and M.F. Henry, CALPHAD-Is it ready for superalloy design? Adv. Eng. Mater. 
(2002) 501-08. 
[14] U.R. Kattner, the CALPHAD method and its role in material and process development, 
Tecnol. Em Metal. Mater. e Mineração. 13 (2016) 3-15. 
[15] R.C. Reed, T. Tao, N. Warnken, Alloys -By-Design: Application t o nickel -based single 
crystal superalloys, Acta Mater. 57 (2009) 5898-5913. 
[16] R.C. Reed, Z. Zhu, A. Sato, D.J. Crudden, Isolation and testing of new single crystal 
superalloys using alloys-by-design method, Mater. Sci. Eng. A. 667 (2016) 261-278. 
[17] R. Rettig, N.C. Ritter, H.E. Helmer, S. Neumeier, R.F. Singer, Single-crystal nickel-based 
superalloys developed by numerical multi-criteria optimization techniques: Design based 
on thermodynamic calculations and experimental validation, Model. Simul. Mater. Sci. 
Eng. 23 (2015) 35004. 
[18] R. Rettig, K. Matuszewski, A. Müller, H.E. Helmer, N.C. Ritter, R.F. Singer, Development 
of a low-density rhenium-free single crystal Nickel-based superalloy by application of 
numerical multi-criteria optimization using thermodynamic calculations, in: M. Hardy, E. 
Huron, U. Glatzel, B. Griffin, B. Lewis (Eds.), Superalloys 2016. 35-44. 
[19] J. Gong, D. Snyder, T. Kozmel, C. Kern, J.E. Saal, I. Berglund, J. Sebastian, G. Olson, 
ICME design of a castable, creep -resistant, single-crystal turbine alloy, JOM. 69 (2017) 
880-885. 
Page 21 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 23

[20] P. Caron, High γ′ solvus new generation nickel -based superalloys for single crystal 
turbineblade applications, in: T.M. Pollock, R.D. Kissinger, R.R Bowman, K.A. Green, M. 
McLean, S.L. Olson, J.J. Schirra (Eds.), Superalloys 2000. 737-746. 
[21] J.R. Li, Z.G. Zhong, D.Z. Tang, S.Z. Liu, P.Y . Wei, Z.T. Wu, D. Huang, M. Han, A low-
cost second generation single crystal superalloy DD6, in: T.M. Pollock, R.D. Kissinger, 
R.R Bowman, K.A. Green, M. McLean, S.L. Olson, J.J. Schirra (Eds.), Superalloys 2000. 
777-783. 
[22] N. Das, Advances in nickel-based cast superalloys, Trans. Indian Inst. Met. 63 (2010) 265-
274. 
[23] G.L. Erickson, The development of the CMSX-11B and CMSX-11C alloys for industrial 
gas turbine application, in: R.D. Kissinger, D.J. Deye, D.L. Anton, A.D. Cetel, M.V . Nathal, 
T.M. Pollock, D.A. Woodford (Eds.), Superalloys 1996. 45-52. 
[24] A. Sato, A.-C. Yeh, T. Kobayashi, T. Yokokawa, H. Harada, T. Murakumo, J.X. Zhang, 
Fifth generation Ni based single crystal superalloy with superior elevated temperature 
properties, Energy Mater. 2 (2007) 19-25. 
[25] N. Saunders, U.K.Z. Guo, X. Li, A.P. Miodownik, J.-P. Schillé, Using JMatPro to model 
materials properties and behavior, JOM. 55 (2003) 60-65. 
[26] M. Durand-Charee, The microstructure of superalloys, CRC Press LLC, Boca Raton, 1997. 
[27] R. Watanabe and T. Kuno, Alloy design of Nickel-base precipitation hardened superalloys, 
Tetsu-to-Hagané, 61, (1975) 2274; Trans. ISIJ, 16, 437-446. 
[28] T. Yokokawa, H. Harada, K. Kawagishi, Y . Koizumi, T. Kobayashi, Quantitative analysis 
of creep strengthening factors in Ni -base single crystal superalloys, in: E.S. Huron, R.C. 
Reed, M.C. Hardy, M.J. Mills, R.E. Montero, P.D. Portella, J. Telesman (Eds.), Superalloys 
2012. 285-292. 
[29] T. Murakumo, T. Kobayashi, Y . Koizumi, H. Harada, Creep behaviour of Ni-base single-
crystal superalloys with various γ′ volume fraction, Acta Mater. 52 (2004) 3737-3744. 
[30] H. Harada, H. Murakami, Design of Ni -base superalloys, Springer Series in Materials 
Science, 34 (1999) 39-70. 
[31] E. Fleischmann, M. K. Miller, E. Affeldt, U. Glatzel, Quantitative experimental 
determination of the solid solution hardening potential of rhenium, tungsten and 
molybdenum in single-crystal nickel-based superalloys, Acta Mater. 87 (2015) 350-356. 
[32] K. Harris, J.B. Wahl, Improv ed single crystal superalloys CMSX -4 (SLS)[La+Y] and 
CMSX-286, K.A. Green, T.M. Pollock, H. Harada, T.E. Howson, R. C. Reed, J. J. Schirra, 
S. Walston (Eds), Superalloys 2004. 45-52. 
[33] E.C. Caldwell, F.J. Fela, and G.E. Fuchs, Segregation of elements in high refractory 
content single crystal nickel based superalloys, in: K.A. Green, T.M. Pollock, H. Harada, 
T.E. Howson, R. C. Reed, J. J. Schirra, S. Walston (Eds), Superalloys 2004. 811-818. 
[34] M. V . Nathal, Effect of initial gamma prime size on the elevated temperature creep 
properties of single crystal nickel base superalloys, Metall. Trans. A. 18 (1987) 1961-1970. 
Page 22 of 23AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript

## Page 24

[35] M. Morinaga, Y . Murata, H. Yukawa, Recent progress in the new PHACOMP approach, 
in: Proceedings of the Symposium on Materials Design Approaches a nd Experiences, 
Warrendale, PA, USA, TMS - Miner., Metals & Mater. Soc., 2001. 15-27. 
[36] J.B. Wahl, K. Harris, Rhenium-free single crystal superalloy for turbine blades and vane 
applications. US Patent. No. 2013/0129522 A1, 2013. 
[37] R.A. Hobbs, S. Tin, C.M.F. Ra e, A castability model based on elemental solid -liquid 
partitioning in advanced nickel -base single -crystal superalloys, Metall. Mater. Trans. A 
Phys. Metall. Mater. Sci. 36 (2005) 2761-2773. 
[38] A. Sato, Y .L. Chiu, R.C. Reed, Oxidation of nickel-based single-crystal superalloys for 
industrial gas turbine applications, Acta Mater. 59 (2011) 225-240. 
[39] E. Menou, G. Ramstein, E. Bertrand, F. Tancret, Multi -objective constrained design of 
nickel-base superalloys using data mining- and thermodynamics-driven genetic algorithms, 
Model. Simul. Mater. Sci. Eng. 24 (2016). 
[40] S. Tang, L.K. Ning, T.Z. Xin, Z. Zheng, Coarsening Behavior of Gamma prime precipitates 
in a nickel based single crystal superalloy, J. Mater. Sci. Technol. 32 (2016) 172-176. 
[41] S. Neumeier, F. Pyczak, M. Göken, The influence of ruthenium and rhenium on the local 
properties of the γ and γ′ phase in nickel-base superalloys and their consequences for alloy 
behavior, in: R.C. Reed, K.A. Green, P. Caron, T.P. Gabb, M.G. Fahrmann, E.S. Huron, 
S.A. Woodard (Eds.), Superalloys 2008. 109-119. 
[42] Y . Koizumi, T. Kobayashi, T. Yokokawa, J. Zhang, M. Osawa, H. Harada, Y . Aoki, M. Arai, 
Development of next-generation Ni-base single crystal superalloys, in: K.A. Green, T.M. 
Pollock, H. Harada, T.E. Howson, R. C. Reed, J. J. Schirra, S. Walston (Eds), Superalloys 
2004. 35-43. 
[43] A. Mottura, R.C. Reed, What is the role of rhenium in single crystal superalloys? MATEC 
Web Conf. 14 (2014) 01001. 
[44] A.F. Giamei, D.L. Anton, Rhenium additions to a Ni -base superalloy: Effects on 
microstructure, Metall. Trans. A. 16 (1985) 1997-2005. 
[45] J.X. Zhang, J.C. Wang, H. Harada, Y . Koizumi, The effect of lattice misfit on the 
dislocation motion in superalloys during high -temperature low-stress creep, Acta Mater. 
53 (2005) 4623-4633. 
[46] F. Pyczak and H. Mughrabi, An overview of Md-number calculations as a tool for phase 
stability prediction in Ni-base superalloys, Intermetallics and Superalloys, 2006, 10, 523-
532. 
[47] B. Seiser, R. Drautz, D.G. Pettifor, TCP phase predictions in Ni -based superalloys: 
structure maps revisited, Acta Mater. 59 (2) (2011) 749-763. 
Page 23 of 23 AUTHOR SUBMITTED MANUSCRIPT - MSMSE-103587.R2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
Accepted Manuscript
