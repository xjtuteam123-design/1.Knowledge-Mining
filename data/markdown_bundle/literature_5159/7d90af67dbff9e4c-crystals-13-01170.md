# crystals-13-01170

<!-- source: D:\总文献\crystals-13-01170.pdf -->
<!-- file_sha256: 360829b5cd64248256dbbf0017bbeda0fba62e2c0ecf77cf14c58f5679317bd1 -->

## Page 1

Citation: Zhu, B.; Jia, M.; Zhao, R.;
Wan, M. Comparative Analysis of
Three Constitutive Models and
Microstructure Characteristics of
Nb521 during Hot Deformation.
Crystals 2023, 13, 1170. https://
doi.org/10.3390/cryst13081170
Academic Editors: Yufei Zu,
Huifang Pang, Fan Wu and
Hongbin Bei
Received: 5 May 2023
Revised: 12 June 2023
Accepted: 6 July 2023
Published: 27 July 2023
Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
crystals
Article
Comparative Analysis of Three Constitutive Models
and Microstructure Characteristics of Nb521
during Hot Deformation
Baohui Zhu 1,2,3
 , Minghang Jia 1, Rui Zhao 1,4, * and Min Wan 1,4
1 School of Mechanical Engineering and Automation, Beihang University, Beijing 100191, China;
zbhwel@163.com (B.Z.)
2 State Key Laboratory of Special Rare Metal Materials, Northwest Rare Metal Materials Research Institute
Ningxia Co., Ltd., Shizuishan 753000, China
3 Ningxia Horizontal Titanium Industry Co., Ltd., Shizuishan 753000, China
4 Jiangxi Research Institute of Beihang University, Beihang University, Nanchang 330024, China
* Correspondence: buaazhaorui@163.com
Abstract: This study presents an exploration of the ﬂow stress constitutive model and the deformation
mechanism of Nb521, both critical for its practical application. Hot-compression experiments were
performed on Nb521 at temperatures ranging from 1523 K to 1723 K and strain rates ranging from
0.01 to 10 s−1. In addition, the microstructure evolution was concurrently studied through scanning
electron microscopy (SEM) and electron backscattered diffraction (EBSD). The stress–strain behaviour
of Nb521 was assessed, leading to the development of three constitutive models: the Johnson–Cook
model, the modiﬁed Johnson–Cook model and the Arrhenius model. In the course of the deformation
process, it is consistently observed that the hardening effect surpasses the softening effect during the
plastic phase, with no observable occurrence of a steady-state phase. The modiﬁed Johnson–Cook
model offers superior predictive accuracy. Both grain elongation and torsion are the main deformation
mechanisms of Nb521 and speciﬁc texture forms during stretching. This study also reveals that
fractures at both room temperature and high temperatures are brittle in nature. The elucidation of
the constitutive model and underlying deformation mechanisms in this study offers indispensable
insights into the hot-deformation behaviour of Nb521.
Keywords: Nb521 alloy; constitutive equation; hot-deformation behaviour; in situ EBSD
1. Introduction
The Nb521 alloy, characterized by moderate strength and plasticity, has been utilized
to manufacture thin walls and complex-shaped parts on rocket engines [ 1], satellites
and spacecraft [ 2] due to its low density, high speciﬁc strength at high temperatures
(600~1600 ◦C) [3] and excellent cold [4] and hot formability [5]. Current scholarly research
has studied the mechanical properties of Nb521. For instance, Xia et al. [ 6] demonstrate
that the suitable addition of niobium carbide particles can bolster the high-temperature
strength of the Nb521 alloy. Xin et al.’s [7] study indicated a positive correlation between
the processing rate of the cold rotary forging process and the alloy’s strength, with optimal
mechanical properties observed at a processing rate of 60%. However, the complex nature
of Nb521’s hot-deformation process renders the effects of strain rate and temperature on
ﬂow stress challenging to describe precisely and reliably via a single-material constitutive
model. Therefore, it is necessary to reasonably compare and analyse various constitutive
models for Nb521.
Constitutive relation, which describes the correlation between ﬂow stress and strain,
strain rate and temperature, plays a pivotal role in ﬁnite-element simulation. Widely
employed models such as the Johnson–Cook [8] and the Arrhenius [9] constitutive models
Crystals 2023, 13, 1170. https://doi.org/10.3390/cryst13081170 https://www.mdpi.com/journal/crystals

## Page 2

Crystals 2023, 13, 1170 2 of 18
are commonly used to characterize the hot deformation of metals due to their simplicity and
broad applicability in the plastic constitutive relations of metals. Yang et al. [10] proposed a
Johnson–Cook model for FG D6A and pointed out that grain reﬁnement reduces the strain
rate sensitivity of the material. Mohamed Toumi Nasri [11] identiﬁed the parameters of
the Johnson–Cook model for A1050 at different temperatures through experimental and
numerical simulation and studied the failure behaviour in hot forming. Qian et al. [ 12]
proposed a modiﬁed Johnson–Cook model considering the coupled effects of strain, strain
rate and temperature on the behaviour of the material, which can give an accurate and
credible prediction of the dynamic behaviour of the CuCrZr alloy over a wide range of
strain rates and temperatures. Wang et al. [ 13] proposed the modiﬁed Johnson–Cook
model by introducing high-temperature softening parameters, which can correctly describe
the deformation behaviour at any temperature within a speciﬁc range. Yang et al. [ 14]
proposed the strain-modiﬁed Arrhenius constitutive equation for 20MnCr5, which has
strong prediction ability, and provided the temperature and strain rate interval to avoid
its plastic instability. Xia et al. [15] applied the Arrhenius constitutive model to study the
hot-deformation behaviour of Ti-6Al-4V-0.1Ru and used a series of material constants as
polynomial functions of strain to improve the accuracy of ﬁnite-element method simulation.
Hu et al. [16] compared the prediction ability of the modiﬁed Johnson–Cook model and
Arrhenius model about Ti-6Al-4V and pointed out that the prediction accuracy of the
Arrhenius model was higher than that of the modiﬁed Johnson–Cook model. Therefore,
in this research, Johnson–Cook and Arrhenius constitutive equations were employed to
investigate Nb521.
Electron backscattered diffraction (EBSD) provides a reliable means to characterize
the microstructure and micro-texture of materials, yielding substantial crystallographic
information about samples. Wan et al. [17] studied the deformation mechanism of RHEAs
during tensile deformation using discontinuous in situ EBSD and pointed out that the dif-
ference in slip behaviour causes the difference in ultimate tensile strength. Wang et al. [18]
determined the crystal orientation and orientation contrast by the scattered electron of
EBSD and measured the interfacial misorientation of low angles. Ye et al. [19] used EBSD to
study the plastic deformation of polycrystalline structures. They veriﬁed the existence of ad-
ditional obstacles to dislocation slip caused by ordered structures in the plastic deformation
process. Zhu et al. [20] studied nickel-based superalloys with EBSD and other technologies.
Their research pointed out that the tensile deformation would produce texture, and the
fracture behaviour was controlled by intergranular fracture and transgranular fracture. In
the present study, EBSD was deployed to ascertain the plastic deformation mechanism,
microstructure and texture of Nb521.
Research on the fracture mechanism of Nb521 is also noteworthy. Cai et al. [21] pointed
out that Nb521 presented plastic or brittle fractures at different oxidation temperatures
through scanning electron microscopy (SEM) fracture morphology. However, none ob-
served the fracture process and microstructure evolution of Nb521. Han et al. [22] observed
the microstructure evolution of materials through in situ SEM experiments, including slip
marks and initiation and propagation of short cracks. Gao et al. [23] adopted in situ tensile
experiments combined with SEM, EBSD and digital image correlation (DIC) and pointed
out that the fracture mechanism of the material changed from ductile transgranular fracture
to brittle intergranular–transgranular mixed fracture with the increase in grain size. Liu
et al. [24] used in situ SEM combined with EBSD and DIC to show that the crack occurs at
the triangular point during alloy fracture and spreads along the grain boundary to generate
an intergranular crack. In this study, we utilized in situ SEM, coupled with EBSD and other
technologies, to analyse the entire fracture process of materials.
The plastic-forming capacity, high-temperature strengthening mechanism and fracture
mechanism of Nb521 have not been studied [ 25]. Further research remains essential to
meet the high-performance requirements of aerospace engines. In this research, the hot-
deformation behaviour of Nb521 was analysed through a high-temperature compression
experiment. The Johnson–Cook model, modiﬁed Johnson–Cook model and Arrhenius

## Page 3

Crystals 2023, 13, 1170 3 of 18
model were established, and the high-temperature ﬂow stress was predicted. In addition,
the deformation and fracture mechanism of Nb521 were studied by discontinuous in situ
EBSD and in situ SEM experiments. This paper aims to offer data support and theoretical
reference for the forming process of Nb521.
2. Materials
The hot-compression experiment of sample Nb521 was carried out on the Gleeble-
3500 simulation testing machine (Dynamic System Inc., New York, NY, USA). The Nb521
cylinder size is ϕ8 mm × 12 mm, annealed in a vacuum. The chemical composition is
shown in Table 1. The surface roughness of the sample was polished to less than or equal
to 1.6µm to reduce friction in the deformation process, and then the hot-compression test
was carried out on the test machine. The compression experiment was conducted at a
temperature of 1523 K to 1723 K, with an interval of 50 K. The strain rates were 0.01 s−1,
0.1 s−1, 1 s−1 and 10 s−1. The true strain of the experiment was 0.7. The experiment used
water quenching.
Table 1. Chemical composition of Nb521 alloy (wt/%).
Composition of Nb521 Alloy
W Mo Zr C N O Cu Ti Fe Si Ta Nb
5.14 1.87 1.33 0.0095 0.0060 0.010 0.001 0.016 0.001 0.0028 0.59 Bal
3. Result and Discussion
3.1. Stress–Strain Curve
Figure 1 presents the true stress–true strain curves for Nb521 under various strain
rates. There is a monotonic increase in stress corresponding to the strain, signifying an
initial occurrence of strain hardening, which can be attributed to an increase in dislocation
density [26]. No yield plateau is produced. At the same strain rate, the stress decreases with
the temperature increase. This is because as the temperature increases, the atomic thermal
motion of the metal becomes intense, and dislocation is more likely to cancel out, resulting
in thermal softening instead of hardening. As shown in Figure 1, the ﬂow stress increases
with the increase in strain rate at the same temperature due to the work hardening caused
by the increase in dislocation. For example, at 1523 K, the true stress is 282 MPa when the
strain rate is 0.01 and the strain of 0.2. It increases to 415 MPa when the strain rate is 10.
During the plastic phase, as the strain increases, the ﬂow stress monotonically increases
until fracture, indicating that the hardening effect is always greater than the softening effect
during the deformation process.
3.2. Johnson–Cook Model
The Johnson–Cook model is as follows:
σ =
(
A + B
( ε
ε0
)n)
•
[
1 + C ln
( .
εp
.
ε0
)][
1 −
( T − T0
Tmelt − T0
)m]
(1)
In the equation, σ is ﬂow stress (MPa), ε is true strain, ε0 refers to the reference strain,
.
εp
is the strain rate of this material (s−1) and
.
ε0 is the reference strain rate (s−1). A is the yield
strength at the reference temperature and reference strain rate; B is the strain-hardening
coefﬁcient; n is the strain-hardening index; C is the strain-rate-hardening coefﬁcient; T is
the experimental temperature (K); T0 is the reference temperature (K); Tmelt is the melting
temperature (2725 K); and m is the thermal-softening index [27]. In the ﬁtting process, the
reference temperature is 1523 K, the reference strain rate is 0.1 s−1 and the reference strain
is 0.1 for determining the parameters in the constitutive equation. In Equation (1), the ﬁrst
term determines the shape of the ﬁtting curve, the second term determines its relationship
with strain rate and the third term determines its relationship with temperature.

## Page 4

Crystals 2023, 13, 1170 4 of 18
Crystals 2023, 13, x FOR PEER REVIEW 4 of 19 
 
 
 
Figure 1. Nb521 true strain–stress curve. (a) 0.01 −1s ; (b) 0.1 −1s ; (c) 1 −1s ; (d) 10 −1s . 
3.2. Johnson–Cook Model 
The Johnson–Cook model is as follows: 
       − =+ • + −      −      


0
00 0
1l n 1
nm
p
melt
TTAB C TT
εεσ εε
 (1)
In the equation, σ is ﬂow stress (MPa), ε is true strain, ε0 refers to the reference 
strain, εp is the strain rate of this material ( −1s ) and ε0 is the reference strain rate ( −1s ). 
A is the yield strength at the reference temperature and reference strain rate; B is the strain-
hardening coeﬃcient; n is the strain-hardening index; C is the strain-rate-hardening coef-
ﬁcient; T is the experimental temperature (K); 0T is the reference temperature (K); meltT 
is the melting temperature (2725 K); and m is the thermal-softening index [27]. In the ﬁt-
ting process, the reference temperature is 1523 K, the reference strain rate is 0.1 −1s and 
the reference strain is 0.1 for determining the parameters in the constitutive equation. In 
Equation (1), the ﬁrst term determines the shape of the ﬁtting curve, the second term de-
termines its relationship with strain rate an d the third term determines its relationship 
with temperature. 
The Johnson–Cook model’s parameters can be ﬁtted independently. At the reference 
temperature of 1523 K and the reference strain rate of 0.1 1−s , Equation (1) can be ex-
pressed as 
εσ ε
 =+   0
n
AB (2)
Figure 1. Nb521 true strain–stress curve. (a) 0.01 s−1; (b) 0.1 s−1; (c) 1 s−1; (d) 10 s−1.
The Johnson–Cook model’s parameters can be ﬁtted independently. At the refer-
ence temperature of 1523 K and the reference strain rate of 0.1 s−1, Equation (1) can be
expressed as
σ =
(
A + B
( ε
ε0
)n)
(2)
Under this deformation condition, as shown in Figure 2a,A is the material’s yield stress
of 176.99 MPa. We can obtain the relationship between ln(σ − A) and ln ε at the reference
temperature and strain rate by substituting A into the equation. n can be conﬁrmed by the
slope of the linear ﬁtting, which equals 0.8577, and lnB is the intercept of 6.51, this means
that B is 59.45 MPa.
Crystals 2023, 13, x FOR PEER REVIEW 5 of 19 
 
 
Under this deformation condition, as shown in Figure 2a, A is the material’s yield 
stress of 176.99 MPa. We can obtain the relationship between ()σ −ln A and εln at the 
reference temperature and strain rate by substituting A into the equation. n can be con-
ﬁrmed by the slope of the linear ﬁtting, which equals 0.8577, and ln B is the intercept of 
6.51, this means that B is 59.45 MPa. 
 
(a) ( b) ( c) 
Figure 2. The relationship between (a) εln and ()σ −ln A at 1523 K and 0.1 −1s ; (b) ()εε 0ln p 
and ()σε + nAB at 1523 K; and ( c) () ( ) −− 00ln meltTT T T and ()σε −+ln 1 nAB . The 
curves are the linear ﬁtting results. 
At the deformation temperature of 1523 K, the equation transformed into the equa-
tion below: 
()
ε
σε ε
 
=+ +   

0
1l n
pn
pAB C (3)
The C value can be obtained by ﬁxed-intercept linear ﬁtting the slope of 
ε
ε

0
ln( )
p
 and 
σ
ε+
n
AB
, which is 0.068, as depicted in Figure 2b. At the strain rate of 0.1 −1s , the equation 
became 
()
  −=+ −  − 
0
0
1
m
n
melt
TTAB TTσε (4)
Through linear ﬁtting of σ
ε
 − +
ln 1 nAB
 and  −
 −
0
0
ln
melt
TT
TT
, m can be obtained by 
the slope of 0.75 as shown in Figure 2c. 
The constitutive equation is as follows: 
() ()
0.75
0.86 1523176.99 59.44 10 1 0.068 ln 10 1 2725 1523
Tσε ε
  −   =+ × × + × −  − 
 (5)
The ﬂow stress predicted by the initial model is compared with the experimental val-
ues in Figure 3. 
Figure 2. The relationship between (a) ln ε and ln(σ − A) at 1523 K and 0.1 s−1; (b) ln
( .
εp/
.
ε0
)
and
σ/(A + Bεn) at 1523 K; and ( c) ln[(T − T0)/(Tmelt − T0)] and ln[1 − σ/(A + Bεn)]. The curves are
the linear ﬁtting results.

## Page 5

Crystals 2023, 13, 1170 5 of 18
At the deformation temperature of 1523 K, the equation transformed into theequation below:
σ =
(
A + Bεn
p
)[
1 + C ln
( .
εp
.
ε0
)]
(3)
The C value can be obtained by ﬁxed-intercept linear ﬁtting the slope of ln(
.
εp.
ε0
)
and σ
A+Bεn , which is 0.068, as depicted in Figure 2b. At the strain rate of 0.1 s−1, the
equation became
σ = (A + Bεn)
[
1 −
( T − T0
Tmelt − T0
)m]
(4)
Through linear ﬁtting of ln
(
1 − σ
A+Bεn
)
and ln
(
T−T0
Tmelt −T0
)
, m can be obtained by the
slope of 0.75 as shown in Figure 2c.
The constitutive equation is as follows:
σ =
[
176.99 + 59.44 × (10ε)0.86
]
×
[
1 + 0.068 ln
(
10
.
ε
)]
×
[
1 −
( T − 1523
2725 − 1523
)0.75]
(5)
The ﬂow stress predicted by the initial model is compared with the experimental
values in Figure 3.
Crystals 2023, 13, x FOR PEER REVIEW 6 of 19 
 
 
 
Figure 3. Comparison between the predicted and experimental value of ﬂow stress using the John-
son–Cook model at diﬀerent strain rates: (a) 0.01 
−1s ; (b) 0.1 −1s ; (c) 1 −1s ; (d) 10 −1s . 
Comparing the predicted and experimental values, as depicted in Figure 3, the John-
son–Cook model exhibits enhanced precision under diﬀerent deformation conditions. No-
tably, at a strain rate of 0.01 −1s , the predicted values demonstrate substantial deviation, 
presenting a considerable discrepancy with changes in the temperature gradient. At a 
strain rate of 0.1 −1s , the predicted values demonstrate increased accuracy, and the low 
strain is more accurate when the strain rate is 1 
−1s . However, the strain increment is 
smaller than the experimental valu e. When the strain rate is 10 
−1s , the predicted value 
aligns accurately with the strain increment, but the value varies with the temperature gra-
dient. Overall, the predicted value of the Johnson–Cook model under low strain is be tter 
than that under high strain [28]. When the te mperature is 1723 K and the strain rate is 1 
−1s , the maximum absolute error reaches 52.48 MPa. When the temperature is 1723 K and 
the strain rate is 0.01 −1s , the maximum relative error reaches 24.02%. 
3.3. Modiﬁed Johnson–Cook Model 
The parameters of the Johnson–Cook model are further ﬁtted and obtained by mod-
iﬁcation [29]. Polynomial ﬁtting was performed to get A, B, C, m and n represented by 
strain rates [12] to improve prediction accura cy. As shown in Table 2, the values of the 
parameters corresponding to each strain rate can be obtained by nonlinear ﬁtting of ﬁve 
curves at di ﬀerent temperatures under that strain rate using the Levenberg–Marquardt 
method [30]. Table 3 presents the coeﬃcient value of polynomial ﬁtting. 
Figure 3. Comparison between the predicted and experimental value of ﬂow stress using the Johnson–
Cook model at different strain rates: (a) 0.01 s−1; (b) 0.1 s−1; (c) 1 s−1; (d) 10 s−1.
Comparing the predicted and experimental values, as depicted in Figure 3, the
Johnson–Cook model exhibits enhanced precision under different deformation conditions.
Notably, at a strain rate of 0.01 s−1, the predicted values demonstrate substantial deviation,

## Page 6

Crystals 2023, 13, 1170 6 of 18
presenting a considerable discrepancy with changes in the temperature gradient. At a strain
rate of 0.1 s−1, the predicted values demonstrate increased accuracy, and the low strain is
more accurate when the strain rate is 1 s−1. However, the strain increment is smaller than
the experimental value. When the strain rate is 10 s−1, the predicted value aligns accurately
with the strain increment, but the value varies with the temperature gradient. Overall,
the predicted value of the Johnson–Cook model under low strain is better than that under
high strain [28]. When the temperature is 1723 K and the strain rate is 1 s−1, the maximum
absolute error reaches 52.48 MPa. When the temperature is 1723 K and the strain rate is
0.01 s−1, the maximum relative error reaches 24.02%.
3.3. Modiﬁed Johnson–Cook Model
The parameters of the Johnson–Cook model are further ﬁtted and obtained by mod-
iﬁcation [ 29]. Polynomial ﬁtting was performed to get A, B, C, m and n represented by
strain rates [12] to improve prediction accuracy. As shown in Table 2, the values of the
parameters corresponding to each strain rate can be obtained by nonlinear ﬁtting of ﬁve
curves at different temperatures under that strain rate using the Levenberg–Marquardt
method [30]. Table 3 presents the coefﬁcient value of polynomial ﬁtting.



A = A0 + A1 ln
( .
ε
)
+ A2
[
ln
( .
ε
)]2 + A3
[
ln
( .
ε
)]3
B = B0 + B1 ln
( .
ε
)
+ B2
[
ln
( .
ε
)]2 + B3
[
ln
( .
ε
)]3
C = C0 + C1 ln
( .
ε
)
+ C2
[
ln
( .
ε
)]2
m = M0 + M1 ln
( .
ε
)
+ M2
[
ln
( .
ε
)]2 + M3
[
ln
( .
ε
)]3
n = N0 + N1 ln
( .
ε
)
+ N2
[
ln
( .
ε
)]2 + N3
[
ln
( .
ε
)]3
(6)
Table 2. Parameter values obtained by nonlinear ﬁtting.
.
ε ln(
.
ε) A B C m n
0.01 −4.60 164.28 81.99 0.042 0.484 0.67
0.1 −2.30 149.43 91.78 0.707 0.637
1 0 129.66 56.40 0.196 0.697 0.893
10 2.30 172.98 65.59 0.069 0.824 0.793
Table 3. The coefﬁcient value obtained by polynomial ﬁtting.
A B C m n
A0 = 129.66 B 0 = 56.40 C 0 = 0.196 M 0 = 0.697 N 0 = 0.893
A1 = 0.19 B 1 = −12.18 C 1 = −0.025 M 1 = −0.0016 N 1 = 0.080
A2 = 5.95 B 2 = 4.20 C 2 = −0.013 M 2 = 0.0131 N 2 = −0.0335
A3 = 0.93 B 3 = 1.23
Crystals 2023, 13, x FOR PEER REVIEW 7 of 19 
 
 
( ) ( ) ( )
( ) ( ) ( )
( ) ( )
( ) ( ) ( )
( ) ( ) ( )
23
0 1 2 3
23
0 1 2 3
2
0 1 2
23
0 1 2 3
23
0 1 2 3
ln ln ln
ln ln ln
ln ln
ln ln ln
ln ln ln
A A A A A
B B B B B
C C C C
m M M M M
n N N N N
  
  

  
  
    = + + +    
    = + + +    
 = + + 
    = + + +    
    = + + +    
 (6) 
Table 2. Parameter values obtained by nonlinear fitting. 

 
( )ln
  A B C m n 
0.01 −4.60 164.28 81.99 0.042 0.484 0.67 
0.1 −2.30 149.43 91.78 0.707 0.637 
1 0 129.66 56.40 0.196 0.697 0.893 
10 2.30 172.98 65.59 0.069 0.824 0.793 
Table 3. The coefficient value obtained by polynomial fitting. 
A B C m n 
A0=129.66 B0=56.40 C0=0.196 M0=0.697 N0=0.893 
A1=0.19 B1=−12.18 C1=−0.025 M1=−0.0016 N1=0.080 
A2=5.95 B2=4.20 C2=−0.013 M2=0.0131 N2=−0.0335 
A3=0.93 B3=1.23 M3=0.00509 N3=−0.00877 
As seen from Figure 4, with the change in strain rate, the value of parameter A pre-
sents a quadratic function relationship with strain rate. In contrast, other parameters have 
no such connection. 
 
Figure 4. Relationships between A, B, C, m, n and 

ln . 
The modified Johnson–Cook constitutive equation is as follows: 
( ) ( )( )
( )
( )( ) ( ) ( )
( )
     = + + − − −    
 0010 1 10 1
mn
meltA B C T T T T

     
 (7) 
The predicted value of flowing stress can be obtained under varying conditions. The 
comparison between the experimental and predicted values is represented in Figure 5. As 
per Figure 5, the modified Johnson–Cook model provides a more precise prediction than 
the Johnson–Cook model. When the temperature is 1523 K, and the strain rate is 0.01 
−1s
 M3 = 0.00509 N 3 = −0.00877
As seen from Figure 4, with the change in strain rate, the value of parameter A presents
a quadratic function relationship with strain rate. In contrast, other parameters have no
such connection.
The modiﬁed Johnson–Cook constitutive equation is as follows:
σ =
[
A
( .
ε
)
+ B
( .
ε
)
(10ε)n(
.
ε)][
1 + C
( .
ε
)(
10
.
ε
)]{
1 − [(T − T0)/(Tmelt − T0)]m(
.
ε)}
(7)
The predicted value of ﬂowing stress can be obtained under varying conditions. The
comparison between the experimental and predicted values is represented in Figure 5.
As per Figure 5, the modiﬁed Johnson–Cook model provides a more precise prediction
than the Johnson–Cook model. When the temperature is 1523 K, and the strain rate is 0.01
s−1, the predicted value is inconsistent with the experiment with the increase in strain.
However, prediction performance improves at other temperatures and strain rates. The

## Page 7

Crystals 2023, 13, 1170 7 of 18
maximum absolute error of 19.71 MPa and the maximum relative error of 4.94% appeared
at the temperature of 1723 K and the strain rate of 1 s−1. The modiﬁed Johnson–Cook
model is more precise than the Johnson–Cook model.
Crystals 2023, 13, x FOR PEER REVIEW 7 of 19 
 
 
() () ()
() () ()
() ()
() () ()
() () ()
23
01 2 3
23
01 2 3
2
01 2
23
01 2 3
23
01 2 3
ln ln ln
ln ln ln
ln ln
ln ln ln
ln ln ln
AA A A A
BB B B B
CC C C
mM M M M
nN N N N
εε ε
εε ε
εε
εε ε
εε ε
  =+ + +  
  =+ + +  
 =+ + 
  =+ + +  
  =+ + +  
 
 

 
 
 (6)
Table 2. Parameter values obtained by nonlinear ﬁtting. 
ε ()ln ε A B C m n 
0.01 −4.60 164.28 81.99 0.042 0.484 0.67 
0.1 −2.30 149.43 91.78 0.707 0.637 
1 0 129.66 56.40 0.196 0.697 0.893 
10 2.30 172.98 65.59 0.069 0.824 0.793 
Table 3. The coeﬃcient value obtained by polynomial ﬁtting. 
A B C m n 
A0=129.66 B 0=56.40 C 0=0.196 M 0=0.697 N 0=0.893 
A1=0.19 B 1=−12.18 C 1=−0.025 M 1=−0.0016 N 1=0.080 
A2=5.95 B 2=4.20 C 2=−0.013 M 2=0.0131 N 2=−0.0335 
A3=0.93 B 3=1.23 M 3=0.00509 N 3=−0.00877 
As seen from Figure 4, with the change in strain rate, the value of parameter A pre-
sents a quadratic function relationship with strain rate. In contrast, other parameters have 
no such connection. 
 
Figure 4. Relationships between A, B, C, m, n and εln . 
The modiﬁed Johnson–Cook constitutive equation is as follows: 
() () ( )
()
() ( ) ( ) ( )
()
{ }   =+ + − − −   

   0010 1 10 1
mn
meltAB C T T T T
εε
σ ε εε εε (7)
The predicted value of ﬂowing stress can be obtained under varying conditions. The 
comparison between the experimental and predicted values is represented in Figure 5. As 
per Figure 5, the modiﬁed Johnson–Cook model provides a more precise prediction than 
the Johnson–Cook model. When the temperature is 1523 K, and the strain rate is 0.01 
−1s
Figure 4. Relationships between A, B, C, m, n and ln
.
ε.
Crystals 2023, 13, x FOR PEER REVIEW 8 of 19 
 
 
, the predicted value is inconsistent with the experiment with the increase in strain. How-
ever, prediction performance improves at other temperatures and strain rates. The maxi-
mum absolute error of 19.71 MPa and the maximum relative error of 4.94% appeared at 
the temperature of 1723 K and the strain rate of 1 
−1s . The modiﬁed Johnson–Cook model 
is more precise than the Johnson–Cook model. 
 
Figure 5. Comparison between predicted and experimental values of ﬂow stress using the modiﬁed 
Johnson–Cook model at a strain rate of (a) 0.01 −1s ; (b) 0.1 −1s ; (c) 1 −1s ; and (d) 10 −1s . 
3.4. Arrhenius Model 
The Arrhenius model can well describe the constitutive relationship between temper-
ature, strain rate and strain during hot deformation [31]. Its form is expressed as follows: 
()εσ
−
=⋅ ⋅
Q
c RTeF e (8)
()
()
βσ
σα σ
σα σ
ασ σ
 <=>

1 ,0 . 8
,1 . 2
sinh ,
n
n
Fe
for all
 (9)
The inﬂuence of temperature and strain rate on deformation behaviour can be ex-
pressed by the Zener–Hollomon parameter, which is 
ε=⋅ 
Q
RTZe (10)
Figure 5. Comparison between predicted and experimental values of ﬂow stress using the modiﬁed
Johnson–Cook model at a strain rate of (a) 0.01 s−1; (b) 0.1 s−1; (c) 1 s−1; and (d) 10 s−1.
3.4. Arrhenius Model
The Arrhenius model can well describe the constitutive relationship between tempera-
ture, strain rate and strain during hot deformation [31]. Its form is expressed as follows:
.
ε = ec · F(σ) · e− Q
RT (8)

## Page 8

Crystals 2023, 13, 1170 8 of 18
F(σ) =



σn1, ασ < 0.8
eβσ, ασ > 1.2
[sinh(ασ)]n, f or all σ
(9)
The inﬂuence of temperature and strain rate on deformation behaviour can be ex-
pressed by the Zener–Hollomon parameter, which is
Z =
.
ε · e
Q
RT (10)
where
.
ε refers to the strain rate (s−1), Q is the activation energy of hot deformation (kJ /mol)
and R is the universal gas constant (8.314 J · mol −1 · K−1). Q reﬂects the microstructure
mechanism in the hot-deformation process, and c is the frequency index. α, β, n1, n are ma-
terial constants in which α = β/n1. It must be noted that the power form and exponential
form work for low-stress levels (ασ < 0.8) and high-stress levels (ασ > 1.2). The hyperbolic
sine function in the third equation is more general, covering a wider stress range. There-
fore, this research used the hyperbolic sine function to describe the thermal-deformation
behaviour of the Nb521 alloy.
At the strain of 0.2, the value of n1 and β can be obtained by the relationship be-
tween ln
.
ε − ln σ and ln
.
ε − σ under ﬁve different temperatures using linear ﬁtting, and
α = β/n1 = 0.0039 MPa−1. These relations are shown in Figure 6.
Crystals 2023, 13, x FOR PEER REVIEW 9 of 19 
 
 
where ε refers to the strain rate ( −1s ), Q is the activation energy of hot deformation (
/kJ mol ) and R is the universal gas constant (8.314 
−−⋅⋅ 11J mol K ). Q reﬂects the microstruc-
ture mechanism in the hot-deformation process, and c is the frequency index. αβ,, , 1nn 
are material constants in which αβ= 1n . It must be noted that the power form and ex-
ponential form work for low-stress levels (ασ < 0.8) and high-stress levels (ασ > 1.2 ). The 
hyperbolic sine function in the third equati on is more general, covering a wider stress 
range. Therefore, this research used the hyperbolic sine function to describe the thermal-
deformation behaviour of the Nb521 alloy. 
At the strain of 0.2, the value of 1n and β can be obtained by the relationship be-
tween εσ−ln ln and εσ−ln under ﬁve diﬀerent temperatures using linear ﬁtting, and 
αβ −== 1
1 0.0039MPan . These relations are shown in Figure 6. 
 
Figure 6. The relationship between: (a) () ( )εσ−ln ln ; (b) ()εσ−ln ; (c) ()εα σ − ln ln sinh ; (d) 
()ασ −ln sinh 1000 T . 
The value of A and B can be obtained by the relationship between 
()εα σ − ln ln sinh and ()ασ −ln sinh 1000 T primely, which is 10.04 and 6.46. Thus, 
the activation energy is =××= 540.0 kJQR A B m o l . 
With the value of Z of four strain rates and ﬁve temperatures, a total of 20 conditions, 
the relationship between ()ασ− ln ln sinhZ can be con ﬁrmed. The value of n and c can 
be obtained by their slope and intercept, which are 9.87 and 37.21. 
Combining equation and Z, the explicit form of ﬂow stress is acquired as follows: 
(d) 
Figure 6. The relationship between: ( a) ln
( .
ε
)
− ln(σ); ( b) ln
( .
ε
)
− σ; ( c) ln
.
ε − ln[sinh(ασ)];
(d) ln[sinh(ασ)] − 1000/T.
The value of A and B can be obtained by the relationship between ln
.
ε − ln[sinh(ασ)]
and ln[sinh(ασ)] − 1000/T primely, which is 10.04 and 6.46. Thus, the activation energy is
Q = R × A × B = 540.0 kJ/mol.

## Page 9

Crystals 2023, 13, 1170 9 of 18
With the value of Z of four strain rates and ﬁve temperatures, a total of 20 conditions,
the relationship between ln Z − ln[sinh(ασ)] can be conﬁrmed. The value of n and c can be
obtained by their slope and intercept, which are 9.87 and 37.21.
Combining equation and Z, the explicit form of ﬂow stress is acquired as follows:
σ = 1
α ln



( Z
ec
) 1
n
+
[( Z
ec
) 2
n
+ 1
] 1
2



(11)
Under different temperatures and strain rates, strain affects both the ﬂow stress and
the material constant [ 32]. The material constants are polynomial functions within the
strain range. The equations are as follows:



α = C0 + C1ε + C2ε2 + C3ε3 + C4ε4 + C5ε5
n = D0 + D1ε + D2ε2 + D3ε3 + D4ε4 + D5ε5
Q = E0 + E1ε + E2ε2 + E3ε3 + E4ε4 + E5ε5
c = F0 + F1ε + F2ε2 + F3ε3 + F4ε4 + F5ε5
(12)
The result can be obtained by performing multi-order polynomial ﬁtting onα, n, Q
and c, as shown in Figure 7. The coefﬁcients of the polynomial ﬁtting can be acquired in
Table 4. From the table, the value of material parameters at any deformation temperature
and strain rate can be determined. Figure 8 illustrates the variation of parameters with
respect to strain. The Arrhenius model is as follows:



σ = 1
α(ε) ln



( Z[Q(ε)]
ec(ε)
) 1
n(ε)
+
[( Z[Q(ε)]
ec(ε)
) 2
n(ε)
+ 1
] 1
2



Z =
.
ε · e[ Q(ε)
RT ]
(13)
Table 4. Coefﬁcients of the polynomial for α, n, Q and c.
α n Q c
C0 = 0.0055 D0 = 23.61 E0 = 1120.6 F0 = 77.69
C1 = −0.011 D1 = −311.7 E1 = −13, 337 F1 = −905.11
C2 = 0.017 D2 = 2748.5 E2 = 118, 552 F2 = 7930.6
C3 = −0.012 D3 = −11, 608 E3 = −502, 966 F3 = −33, 389
C4 = −0.0079 D4 = 23, 300 E4 = 1, 010, 224 F4 = 66, 684
C5 = 0.018 D5 = −17, 945 E5 = −778, 931 F5 = −51, 200
Crystals 2023, 13, x FOR PEER REVIEW 10 of 19 
 
 
σ α
   =+ +     
1
12 2
1 ln 1
nn
cc
ZZ
ee
 (11)
Under diﬀerent temperatures and strain rates, strain aﬀects both the ﬂow stress and 
the material constant [32]. The material constants are polynomial functions within the 
strain range. The equations are as follows: 
α ε εεεε
εε ε ε ε
ε εεεε
εε ε ε ε
 = + ++++
 = + ++++ =+ + + + +
 = + ++++
2345
0 1 2345
2345
0 1 2345
2345
0 1 2345
2345
0 1 2345
C C CCCC
nD D D D D D
QE E E E E E
cF F F F F F
 (12)
The result can be obtained by performing multi-order polynomial ﬁtting on α, n, Q 
and c, as shown in Figure 7. The coe ﬃcients of the polynomial ﬁtting can be acquired in 
Table 4. From the table, the value of material parameters at any deformation temperature 
and strain rate can be determined. Figure 8 illustrates the variation of parameters with 
respect to strain. The Arrhenius model is as follows: 
() () () ()
()
εε
εε
εε
ε
σ αε
ε
  



       =+ +        

=⋅ 
1
12 2
() ()
1 ln 1()
nn
QQ
cc
Q
RT
ZZ
ee
Ze
 (13)
Table 4. Coeﬃcients of the polynomial for α, n, Q and c. 
α n Q c 
=0 0.0055C =0 23.61D =0 1120.6E =0 77.69F 
−=1 0.011C −=1 311.7D −=1 13337E −=1 905.11F 
=2 0.017C =2 2748.5D =2 118552E =2 7930.6F 
−=3 0.012C −=3 11608D −=3 502966E −=3 33389F 
−=4 0.0079C =4 23300D =4 1010224E =4 66684F 
=5 0.018C −=5 17945D −=5 778931E −=5 51200F 
 
Figure 7. Relationship between lnZ and ln[sinh(ασ)]. 
Figure 7. Relationship between lnZ and ln[sinh(ασ)].

## Page 10

Crystals 2023, 13, 1170 10 of 18
Crystals 2023, 13, x FOR PEER REVIEW 11 of 19 
 
 
 
Figure 8. Relationships between material parameters and ε : (a) α ; (b) n; (c) Q; (d) c. 
The Arrhenius model’s predicted and experimental value comparison is illustrated 
in Figure 9. As can be seen from Figu re 9, when the strain rate is 0.01 −1s , the predicted 
value is smaller than the actual value at 1523 K but larger than the actual value at other 
temperatures. When the strain rate is 0.1 −1s , the predicted value is small when the tem-
perature exceeds 1623 K, and the prediction e ﬀect is better at other temperatures. When 
the strain rate is 1 −1s , the predicted value is more accurate at low strain, but with the 
increase in strain, the stress increment is sm aller than the actual value. When the strain 
rate is 10 −1s , the increment of the predicted value with the temperature gradient is larger 
than the actual value. Overall, when the strain rate is high and the strain is minimal, the 
predicted value is more accurate, and the accu racy decreases with strain increment [33]. 
The deviations could be due to the intrinsic limitations of the constitutive equation. 
Figure 8. Relationships between material parameters and ε: (a) α; (b) n; (c) Q; (d) c.
The Arrhenius model’s predicted and experimental value comparison is illustrated in
Figure 9. As can be seen from Figure 9, when the strain rate is 0.01s−1, the predicted value is
smaller than the actual value at 1523 K but larger than the actual value at other temperatures.
When the strain rate is 0.1 s−1, the predicted value is small when the temperature exceeds
1623 K, and the prediction effect is better at other temperatures. When the strain rate is
1 s−1, the predicted value is more accurate at low strain, but with the increase in strain,
the stress increment is smaller than the actual value. When the strain rate is 10 s−1, the
increment of the predicted value with the temperature gradient is larger than the actual
value. Overall, when the strain rate is high and the strain is minimal, the predicted value is
more accurate, and the accuracy decreases with strain increment [33]. The deviations could
be due to the intrinsic limitations of the constitutive equation.
3.5. Precision Analysis
Chao et al. [34] assert that the prediction results of the classical Johnson–Cook model
exhibit apparent strain hardening, and the error is relatively large when the strain is
larger. Based on the comparison, it can be deduced that the Johnson–Cook model provides
reasonably accurate predictions only when applied within the speciﬁed range of reference
temperature and strain rate. The model’s effectiveness is limited to a narrow range around
the reference conditions, as it only incorporates the effects of work hardening, strain-
rate-induced hardening and temperature-induced hardening and softening. The model
overlooks the interaction among these factors during the actual deformation process. Unlike
the original Johnson–Cook model, the thermal-softening index m and hardening coefﬁcient
C of Nb521 were associated with strain and strain rate. A more precise predicted value of
ﬂow stress can be obtained by quadratic ﬁtting. This indicates that the high-temperature
ﬂow behaviour of Nb521 is controlled by thermal softening, strain hardening and strain
rate hardening. In addition, its coupling effect with strain, temperature and strain rate
should also be considered. Therefore, when the temperature and strain rate differ greatly

## Page 11

Crystals 2023, 13, 1170 11 of 18
from the reference temperature and strain rate used to determine the parameters, the
Johnson–Cook model cannot consider these coupling effects, thus leading to a huge error
in the predicted value. The modiﬁed Johnson–Cook model can more accurately predict the
high-temperature deformation of Nb521. However, at the temperature of 1523 K with a
strain rate of 0.01 s−1, the prediction is more inaccurate than others. The cause may be the
error during the experiment. Since the modiﬁed Johnson–Cook model does not involve the
recovery of dislocation density, the practicability has not been improved.
Crystals 2023, 13, x FOR PEER REVIEW 12 of 19 
 
 
 
Figure 9. Comparison between predicted and experimental ﬂow stress using the strain-compen-
sated Arrhenius model at diﬀerent strain rates: (a) 0.01 −1s ; (b) 0.1 −1s ; (c) 1 −1s ; (d) 10 −1s . 
3.5. Precision Analysis 
Chao et al. [34] assert that the prediction results of the classical Johnson–Cook model 
exhibit apparent strain harden ing, and the error is relatively large when the strain is 
larger. Based on the comparison, it can be deduced that the Johnson–Cook model provides 
reasonably accurate predictions only when applied within the speciﬁed range of reference 
temperature and strain rate. The model’s eﬀectiveness is limited to a narrow range around 
the reference conditions, as it only incorporates the eﬀects of work hardening, strain-rate-
induced hardening and temperature-induced hardening and softening. The model over-
looks the interaction among these factors duri ng the actual deformation process. Unlike 
the original Johnson–Cook model, the thermal-softening index m and hardening coe ﬃ-
cient C of Nb521 were associated with strain and strain rate. A more precise predicted 
value of ﬂow stress can be obtained by quadratic ﬁtting. This indicates that the high-tem-
perature ﬂow behaviour of Nb521 is controlled by thermal softening, strain hardening 
and strain rate hardening. In addition, its coupling e ﬀect with strain, temperature and 
strain rate should also be considered. Ther efore, when the temperature and strain rate 
diﬀer greatly from the reference temperature and strain rate used to determine the param-
eters, the Johnson–Cook model cannot consider these coupling e ﬀects, thus leading to a 
huge error in the predicted value. The modiﬁed Johnson–Cook model can more accurately 
predict the high-temperature deformation of Nb521. However, at the temperature of 1523 
K with a strain rate of 0.01 
−1s , the prediction is more ina ccurate than others. The cause 
may be the error during the experiment. Since the modi ﬁed Johnson–Cook model does 
not involve the recovery of dislocation density, the practicability has not been improved. 
To further assess the accuracy of the three constitutive models, each model’s absolute 
and relative errors were calculated when the strain was 0.3. The errors of the predicted 
values under the three constitutive equation s are shown in Table 5. The maximum error 
of the Johnson–Cook model is 30.97 MPa when the temperature is 1673 K and the strain 
rate is 0.01 
−1s . Its relative error value ranges from −8.95% to 16.56%. The maximum error 
Figure 9. Comparison between predicted and experimental ﬂow stress using the strain-compensated
Arrhenius model at different strain rates: (a) 0.01 s−1; (b) 0.1 s−1; (c) 1 s−1; (d) 10 s−1.
To further assess the accuracy of the three constitutive models, each model’s absolute
and relative errors were calculated when the strain was 0.3. The errors of the predicted
values under the three constitutive equations are shown in Table 5. The maximum error of
the Johnson–Cook model is 30.97 MPa when the temperature is 1673 K and the strain rate
is 0.01 s−1. Its relative error value ranges from −8.95% to 16.56%. The maximum error of
the modiﬁed Johnson–Cook model occurs when the temperature is 1623 K and the strain
rate is 1 s−1, reaching 7.46 MPa. Its relative error value ranges from −2.16% to 2.25%. The
maximum error of the Arrhenius model occurs when the temperature is 1523 K and the
strain rate is 10, reaching 30.12 MPa. Its relative error value ranges from −9.64% to 7.20%.
It is apparent that the modiﬁed Johnson–Cook model exhibits the highest accuracy and an
effective prediction effect.

## Page 12

Crystals 2023, 13, 1170 12 of 18
Table 5. Absolute error value and relative error value of three kinds of constitutive models under
different deformation conditions at a strain of 0.3.
T/K
.
ε/s−1 ∆σJ−C/MPa ∆σMJ−C/MPa ∆σARR/MPa RE σJ−C(%) RE σMJ−C(%) RE σARR(%)
1523
0.01 −27.32 −0.09 −29.42 −8.95 −0.03 −9.64
0.1 −4.52 −5.01 −0.95 −1.35 −1.50 −0.29
1 −25.64 −2.90 −11.25 −6.30 −0.71 −2.77
10 1.00 0.23 30.12 0.23 0.05 6.98
1573
0.01 11.66 −1.19 4.81 4.81 −0.49 1.98
0.1 4.97 4.44 4.91 1.68 1.50 1.66
1 −11.36 7.10 1.17 −3.16 1.97 0.32
10 −12.52 −2.70 17.19 −3.07 −0.66 4.21
1623
0.01 21.44 −1.26 8.44 10.03 −0.59 3.94
0.1 −5.61 −6.14 −11.68 −1.97 −2.16 −4.11
1 −8.63 7.46 −1.44 −2.61 2.25 −0.43
10 −13.14 1.13 12.55 −3.46 0.30 3.31
1673
0.01 30.97 3.17 13.47 16.56 1.69 7.20
0.1 −3.29 −3.80 −13.95 −1.26 −1.45 −5.33
1 −12.50 1.72 −9.60 −4.01 0.55 −3.08
10 −13.85 3.10 8.40 −3.92 0.88 2.38
1723
0.01 27.24 −3.29 7.10 15.63 −1.89 4.07
0.1 1.58 1.09 −11.87 0.67 0.46 −5.00
1 −17.93 −5.31 −17.73 −6.09 −1.80 −6.03
10 −23.84 −5.27 −3.72 −7.06 −1.56 −1.10
3.6. In Situ EBSD Tensile Test
An in situ EBSD stretching experiment was conducted on Nb521. Figure 10a illustrates
the loading and deformation curves of the tensile experiment. The EBSD sampling is con-
ducted in A, B, C and D. Figure 10b–e are the comparisons of the initial stage (A) and plastic
deformation phase (D). Figure 10b represents the surface morphology change of Nb521. It
is evident that with the stretching, the internal slip system of each grain is activated, the
slip track in different directions can be observed on the surface, some grains are elongated
and there is convex between grains. Figure 10c displays the evolution of the recrystallized
structure. With stretching, the original recrystallized structure almost all becomes the
deformation structure. Bibhanshu et al. [ 35] proposed that changes in grain orientation
could be identiﬁed by colour changes within grains, and high-angle grain boundaries
would shift to medium-angle grain boundaries and then small-angle grain boundaries.
Figure 10d presents the orientation distribution diagram of the inverse pole ﬁgure, where
different colours indicate different orientations of grains. After stretching, the colour in-
side the grain changes, suggesting that the grain twists and crystal orientation changes
during the deformation process. Crystals primarily oriented along the ~(001) direction
(highlighted in red in the ﬁgure) undergo signiﬁcant morphological changes relative to the
tensile direction, while the grain orientation deviates minimally from the initial orientation.
On the other hand, grains oriented approximately along ~(111) (highlighted in blue in the
ﬁgure) and ~(101) (highlighted in green in the ﬁgure) exhibit a shift towards the red region.
Figure 10e represents the distribution map of grain boundaries, with the thin line indicating
the presence of low-angle grain boundaries. It is evident that there is a substantial increase
in low-angle grain boundaries resulting from grain boundary torsion induced by stretching.
The formation of low-angle grain boundaries parallels high-angle grain boundaries and
mainly occurs near hard particles. Figure 10 provides an illustration of the cooperative
deformation mechanisms in Nb521, involving dislocation slip and grain rotation during
the loading process. The plastic stage is characterized by strain hardening, attributed to the
stretching of grains, alterations in crystal orientation and enhanced deformation resistance.

## Page 13

Crystals 2023, 13, 1170 13 of 18
Crystals 2023, 13, x FOR PEER REVIEW 14 of 19 
 
 
the red region. Figure 10e represents the dist ribution map of grain boundaries, with the 
thin line indicating the presence of low-angle grain boundaries. It is evident that there is 
a substantial increase in low-angle grain boundaries resulting from grain boundary tor-
sion induced by stretching. The formation of low-angle grain boundaries parallels high-
angle grain boundaries and mainly occurs near hard particles. Figure 10 provides an il-
lustration of the cooperative deformation mechanisms in Nb521, involving dislocation 
slip and grain rotation during the loading process. The plastic stage is characterized by 
strain hardening, a ttributed to the stretching of grains , alterations in crystal orientation 
and enhanced deformation resistance. 
 
Figure 10. In situ EBSD tensile tests give ( a) load–displacement curve; and ﬁgures by Channel 5 
show (b) morphology of the sample surface; ( c) recrystallized fraction; ( d) inverse pole ﬁgure; (e) 
low- and high-angle grain boundary at the displacement of 0 and 1900. 
Figure 11 displays the pole ﬁgure of {100},{110},{111} for Nb521 when the displace-
ment is 0, 1100, 1500 and 1900 µm, where X0 is TD and Y0 is RD. Wu et al. [36] outlined 
that grains tend to be arrang ed rather than dispersed with increased stress, and larger 
tensile stress will enhance the cubic texture. It can be observed that there is no speci ﬁc 
texture in the material at the beginning, but with the progress of stretching, a particular 
texture is gradually formed. Since Nb is a body -centred cubic crystal, it can be seen that 
the material has a {001} <110> cubic texture [37]. This observation indicates that stretching 
causes the Nb521 grains to tend to arrange to form a speci ﬁc texture, thus possibly en-
hancing work hardening. 
Figure 10. In situ EBSD tensile tests give (a) load–displacement curve; and ﬁgures by Channel 5 show
(b) morphology of the sample surface; (c) recrystallized fraction; (d) inverse pole ﬁgure; (e) low- and
high-angle grain boundary at the displacement of 0 and 1900.
Figure 11 displays the pole ﬁgure of {100},{110},{111} for Nb521 when the displacement
is 0, 1100, 1500 and 1900 µm, where X0 is TD and Y0 is RD. Wu et al. [ 36] outlined that
grains tend to be arranged rather than dispersed with increased stress, and larger tensile
stress will enhance the cubic texture. It can be observed that there is no speciﬁc texture in
the material at the beginning, but with the progress of stretching, a particular texture is
gradually formed. Since Nb is a body-centred cubic crystal, it can be seen that the material
has a {001} <110> cubic texture [ 37]. This observation indicates that stretching causes
the Nb521 grains to tend to arrange to form a speciﬁc texture, thus possibly enhancing
work hardening.
3.7. Fracture Analysis
Figure 12 illustrates the SEM image of the in situ tensile curve of Nb521 at room
temperature and the surface morphology of the specimen during the tensile process. There
is no obvious plastic deformation characteristic at the low strain stage. The ﬁrst crack in
the tensile process occurs near the grain boundary (Figure 12c) and expands along the
direction perpendicular to the stress (Figure 12d). It can be seen that there are impurity
particles in the crack, indicating that the crack is a microcrack induced by impurity particles
at the grain boundary. As shown in Figure 12e, numerous other cracks are formed near the
refracture surface after the initial crack. The growth of these cracks weakens the material’s
bearing capacity, ultimately resulting in a brittle fracture [38]. Most of the cracks are located
at a certain distance from the fracture plane [ 39]. The main crack formation takes place
near the fracture stage (Figure 12a), which suggests that the critical cleavage fracture stress
of Nb521 is approximately 500 MPa.

## Page 14

Crystals 2023, 13, 1170 14 of 18
Crystals 2023, 13, x FOR PEER REVIEW 15 of 19 
 
 
 
Figure 11. Pole ﬁgure of Nb521 at the displacement of 0, 1100, 1500 and 1900. 
3.7. Fracture Analysis 
Figure 12 illustrates the SEM image of the in situ tensile curve of Nb521 at room tem-
perature and the surface morphology of the specimen during the tensile process. There is 
no obvious plastic deformation characteristic at the low strain stage. The ﬁrst crack in the 
tensile process occurs near the grain boundary (Figure 12c) and expands along the direc-
tion perpendicular to the stress (Figure 12d). It can be seen that there are impurity particles 
in the crack, indicating that the crack is a microcrack induced by impurity particles at the 
grain boundary. As shown in Figure 12e, numerous other cracks are formed near the re-
fracture surface after the initial crack. The growth of these cracks weakens the material’s 
bearing capacity, ultimately resulting in a bri ttle fracture [38]. Most of the cracks are lo-
cated at a certain distance from the fracture plane [39]. The main crack formation takes 
place near the fracture stage (Figure 12a), which suggests that the critical cleavage fracture 
stress of Nb521 is approximately 500 MPa. 
Figure 11. Pole ﬁgure of Nb521 at the displacement of 0, 1100, 1500 and 1900.
Figure 13 illustrates the in situ tensile curve of Nb521 at the temperature of 1473 K.
SEM ﬁgures are obtained in the order of a, b, c, d and e during the phase of fracture. As
can be seen from Figure 13a,b, cracks appear on the sample’s surface and gradually grow.
There are no impurity particles inside the sample, indicating that under the condition
of hot deformation, the microcracks are not induced by impurity particles but under the
interference of a particular stress state and other conditions. It can be seen from Figure 13c
that cracks appear on both sides of the prefabricated damage and increase with stretching.
According to Figure 13d,e, although cracks appeared on both sides, the fracture surface
appeared in the middle instead of the crack, indicating that the sample fracture at 1473 K
was a brittle fracture induced by non-impurity particles.

## Page 15

Crystals 2023, 13, 1170 15 of 18
Crystals 2023, 13, x FOR PEER REVIEW 16 of 19 
 
 
 
Figure 12. The in situ tensile curve at room temperature and micromorphology in the surface at the 
displacement of (a) 864.38 µm, (b) 1377.54 µm, (c) necking, (d) 1404 µm and (e) fracture. 
Figure 13 illustrates the in situ tensile cu rve of Nb521 at the temperature of 1473 K. 
SEM ﬁgures are obtained in the order of a, b, c, d and e during the phase of fracture. As 
can be seen from Figure 13a,b, cracks appear on the sample’s surface and gradually grow. 
There are no impurity particles inside the sample, indicating that under the condition of 
hot deformation, the microcracks are not induced by impurity particles but under the in-
terference of a particular stress state and other conditions. It can be seen from Figure 13c 
that cracks appear on both sides of the prefabricated damage and increase with stretching. 
According to Figure 13d,e, although cracks a ppeared on both sides, the fracture surface 
appeared in the middle instead of the crack, indicating that the sample fracture at 1473 K 
was a brittle fracture induced by non-impurity particles. 
 
Figure 12. The in situ tensile curve at room temperature and micromorphology in the surface at the
displacement of (a) 864.38µm, (b) 1377.54µm, (c) necking, (d) 1404µm and (e) fracture.
Crystals 2023, 13, x FOR PEER REVIEW 16 of 19 
 
 
 
Figure 12. The in situ tensile curve at room temperature and micromorphology in the surface at the 
displacement of (a) 864.38 µm, (b) 1377.54 µm, (c) necking, (d) 1404 µm and (e) fracture. 
Figure 13 illustrates the in situ tensile cu rve of Nb521 at the temperature of 1473 K. 
SEM ﬁgures are obtained in the order of a, b, c, d and e during the phase of fracture. As 
can be seen from Figure 13a,b, cracks appear on the sample’s surface and gradually grow. 
There are no impurity particles inside the sample, indicating that under the condition of 
hot deformation, the microcracks are not induced by impurity particles but under the in-
terference of a particular stress state and other conditions. It can be seen from Figure 13c 
that cracks appear on both sides of the prefabricated damage and increase with stretching. 
According to Figure 13d,e, although cracks a ppeared on both sides, the fracture surface 
appeared in the middle instead of the crack, indicating that the sample fracture at 1473 K 
was a brittle fracture induced by non-impurity particles. 
 
Figure 13. The in situ tensile curve at 1473 K and micromorphology in the surface at the phase
of (a) cracks occurred, (b) cracks grew, (c) cracks on both sides, ( d) cracks propagate and merge,
(e) fracture occurred. All (a–e) occurs during the phase of fracture.
4. Conclusions
The hot-deformation behaviour of Nb521 at strain temperatures of 1523, 1573, 1623,
1673 and 1723 K and strain rates of 0.01, 0.1, 1 and 10 s−1 were studied by hot-compression
experiments. The Johnson–Cook model, modiﬁed Johnson–Cook model and Arrhenius
model were established based on the true stress–strain curves obtained by experiments.
The accuracy of the three models for high-temperature ﬂow stress prediction of Nb521 was
compared. The microstructure and fracture mechanism of Nb521 were studied by in situ

## Page 16

Crystals 2023, 13, 1170 16 of 18
tensile test and in situ EBSD tensile test. According to the research results, the following
conclusions can be drawn:
1. All three models exhibit varying degrees of error. The maximum errors of the Johnson–
Cook model, modiﬁed Johnson–Cook model and Arrhenius model are 30.97 MPa,
7.46 MPa and 30.12 MPa, and the relative errors are 16.56%, 2.25% and 9.64%. Among
them, the modiﬁed Johnson–Cook model demonstrates superior accuracy. The JC
model displays good prediction accuracy only when referring to reference strain
and temperature. It can be seen from the MJC model that the parameters of Nb521
vary greatly at different temperatures and strain rates, which may be because the
deformation mechanism of Nb521 is affected at higher temperatures and strain rates.
2. Both grain elongation and torsion are the main deformation mechanism of Nb521,
and {001} <110> cubic texture gradually forms with stretching.
3. The fracture mechanism of Nb521 at room temperature and high temperature has
been revealed. At room temperature, microcracks induced by impurity particles
at the grain boundary initiate the fracture. At high temperatures, the microcracks
are not induced by impurity particles but by speciﬁc stress conditions. The cracks
appear on both sides along with the stretching, leading to the brittle fracture of the
surface structure.
Author Contributions: Conceptualization, B.Z.; methodology, B.Z. and M.J.; formal analysis, B.Z.
and M.J.; investigation, M.J.; resources, M.W.; data curation, B.Z. and M.J.; writing—original draft
preparation, B.Z. and M.J.; writing—review and editing, R.Z.; visualization, M.J.; supervision, R.Z.;
funding acquisition, R.Z. and M.W. All authors have read and agreed to the published version of
the manuscript.
Funding: This research was funded by the project (grant number 52105316 from National Natural
Science Foundation of China), the project (grant number 20212BAB214046 from Natural Science
Foundation of Jiangxi Province), and the Fundamental Research Funds for the Central Universities
(Qingba from BeiHang University), and the State Key Laboratory of Special Rare Metal Materials in
Northwest Rare Metal Materials Research Institute Ningxia Co., Ltd. (grant number SKL2018K002).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The author would like to acknowledge the ﬁnancial support of Zhejiang Qiyue
Technology Co., Ltd. for providing the facilities for the EBSD analysis and experimental works, and
Jiangxi Research Institute of Beihang University for assistance during experiments and writing.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1. Wang, N.; Li, H.; Xu, F.; Yin, Z.; Zhang, X. Recent Development of Advanced Materials for Liquid Rocket Thruster Chambers.
Aerosp. Mater. Technol. 2019, 49, 1–8.
2. Zhang, C.; Hu, G. Structure, Properties and Applaction of Nb521 Alloys. Aerosp. Mater. Technol. 2012, 42, 105–107.
3. Senkov, O.N.; Rao, S.I.; Butler, T.M.; Chaput, K.J. Ductile Nb alloys with reduced density and cost. J. Alloys Compd. 2019,
808, 151685. [CrossRef]
4. Luo, Y.; Zhai, B. Research on precision spinning-pressure forming process of large-size thin-walled nozzle made of niobium
tungsten alloy. J. Rocket. Propuls. 2016, 42, 68–73.
5. Yapici, G.G. Simultaneous improvement in strength and ductility of severely deformed niobium alloy. Mater. Lett. 2020,
279, 128443. [CrossRef]
6. Xia, M.; Zheng, X.; Liu, H.; Bai, R.; Cai, X.; Wang, F. Effect of Nb2C Particle Size and Content on Microstructure and Properties of
Niobium Alloy. Hot Work. Technol. 2016, 45, 115–117. [CrossRef]
7. Xin, M.; Lv, Y.; Li, S.; Zhang, X.; Wang, H.; Han, W.; Hu, X.; Shen, L. Effects of Cold Rotary Forging on Microstructure and
Mechanical Properties of Nb521 Alloy Bars. Rare Met. Cem. Carbides 2018, 46, 37–42.
8. Johnson, G.R.; Cook, W.H. Fracture characteristics of three metals subjected to various strains, strain rates, temperatures and
pressures. Eng. Fract. Mech. 1985, 21, 31–48. [CrossRef]

## Page 17

Crystals 2023, 13, 1170 17 of 18
9. Bodunrin, M.O. Flow stress prediction using hyperbolic-sine Arrhenius constants optimised by simple generalised reduced
gradient reﬁnement. J. Mater. Res. Technol.-JmrT 2020, 9, 2376–2386. [CrossRef]
10. Yang, Z.; Feng, X.; Zhang, X.; Shen, Y.; Huang, X.; Xie, R. Study on Dynamic Mechanical Behaviors and J–C Constitutive Model of
a Fine-Grained D6A Steel. Crystals 2022, 12, 806. [CrossRef]
11. Nasri, M.T.; Abbassi, F.; Ahmad, F.; Makhlouﬁ, W.; Ayadi, M.; Mehboob, H.; Choi, H.S. Experimental and numerical investigation
of sheet metal failure based on Johnson-Cook model and Erichsen test over a wide range of temperatures. Mech. Adv. Mater.
Struct. 2022, 30, 2087–2100. [CrossRef]
12. Qian, X.; Peng, X.; Song, Y.; Huang, J.; Wei, Y.; Liu, P .; Mao, X.; Zhang, J.; Wang, L. Dynamic constitutive relationship of CuCrZr
alloy based on Johnson-Cook model. Nucl. Mater. Energy 2020, 24, 100768. [CrossRef]
13. Wang, Y.; Zhou, D.; Zhou, Y.; Sha, A.; Cheng, H.; Yan, Y. A Constitutive Relation Based on the Johnson–Cook Model for
Ti-22Al-23Nb-2(Mo, Zr) Alloy at Elevated Temperature. Crystals 2021, 11, 754. [CrossRef]
14. Yang, J.; Wang, L.; Zheng, Y.; Zhong, Z. Strain Modiﬁed Constitutive Equation and Processing Maps of High Quality 20MnCr5(SH)
Gear Steel. Crystals 2021, 11, 536. [CrossRef]
15. Xia, Y.F.; Jiang, W.; Cheng, Q.; Jiang, L.; Jin, L. Hot deformation behavior of Ti-6Al-4V-0.1Ru alloy during isothermal compression.
Trans. Nonferrous Met. Soc. China 2020, 30, 134–146. [CrossRef]
16. Hu, M.; Dong, L.; Zhang, Z.; Lei, X.; Yang, R.; Sha, Y. Correction of Flow Curves and Constitutive Modelling of a Ti-6Al-4V Alloy.
Metals 2018, 8, 256. [CrossRef]
17. Wan, Q.; Hua, K.; Tong, Y.; Wu, Y.; Zhang, F.; Li, X.; Wang, H. Interrupted in-situ EBSD study of crystallographic characteristics
and deformation micro-mechanism in TiZrHfNb refractory high entropy alloys during uniaxial tensile deformation. Mater.
Charact. 2022, 189, 111960. [CrossRef]
18. Wang, Z.; Zaefferer, S. On the accuracy of grain boundary character determination by pseudo-3D EBSD.Mater. Charact. 2017, 130,
33–38. [CrossRef]
19. Ye, Z.; Li, C.; Zheng, M.; Zhang, X.; Yang, X.; Gu, J. In-situ EBSD/DIC-based investigation of deformation and fracture mechanism
in FCC- and L12-structured FeCoNiV high-entropy alloys. Int. J. Plast. 2022, 152, 103247. [CrossRef]
20. Zhu, Q.; Wang, C.; Qin, H.; Chen, G.; Zhang, P . Effect of the grain size on the microtensile deformation and fracture behaviors of a
nickel-based superalloy via EBSD and in-situ synchrotron radiation X-ray tomography .Mater. Charact.2019, 156, 109875. [CrossRef]
21. Cai, X.; Li, Q.; Xia, M.; Li, W.; Zheng, X.; Wang, F.; Liu, H.; Bai, R. Effect of Oxidizing Temperature on Mechanical Properties of
Nb521 Alloy. Hot Work. Technol. 2021, 50, 36–38. [CrossRef]
22. Han, Q.; Wang, W.; Fang, J.; Cui, H.; Zhang, H.; Yang, X.; Mu, Q.; Xu, J.; Shi, H. In-situ SEM and EBSD study on fretting fatigue
crack initiation of a directionally solidiﬁed Ni-based superalloy. Int. J. Fatigue 2022, 161, 106908. [CrossRef]
23. Gao, W.; Lu, J.; Zhou, J.; Liu, L.E.; Wang, J.; Zhang, Y.; Zhang, Z. Effect of grain size on deformation and fracture of Inconel718:
An in-situ SEM-EBSD-DIC investigation. Mater. Sci. Eng. A 2022, 861, 144361. [CrossRef]
24. Liu, J.; Sun, J.; Chen, Q.; Lu, L. Intergranular Cracking in Mg-Gd-Y Alloy during Tension Test. Crystals 2022, 12, 1040. [CrossRef]
25. Zhu, B.; Wu, X.; Wan, M.; Zhao, G.; Cao, Y.; Luo, W.; Li, S.; He, J. Progress of high temperature niobium alloy for aerospace
applications. Chin. J. Nonferrous Met. 2022, 1–33. [CrossRef]
26. Lin, X.; Huang, H.; Yuan, X.; Wang, Y.; Zheng, B.; Zuo, X.; Zhou, G. Establishment and validity veriﬁcation of the hot processing
map of a Ti-47.5Al-2.5V-1.0Cr-0.2Zr alloy with a lamellar microstructure.Mater. Charact. 2022, 183, 111599. [CrossRef]
27. Shokry, A.; Gowid, S.; Mulki, H.; Kharmanda, G. On the Prediction of the Flow Behavior of Metals and Alloys at a Wide Range
of Temperatures and Strain Rates Using Johnson-Cook and Modiﬁed Johnson-Cook-Based Models: A Review. Materials 2023,
16, 1574. [CrossRef] [PubMed]
28. Zhang, D.-N.; Shangguan, Q.-Q.; Xie, C.-J.; Liu, F. A modiﬁed Johnson–Cook model of dynamic tensile behaviors for 7075-T6
aluminum alloy. J. Alloys Compd. 2015, 619, 186–194. [CrossRef]
29. Ojal, N.; Cherukuri, H.P .; Schmitz, T.L.; Devlugt, K.T.; Jaycox, A.W. A combined experimental and numerical approach that
eliminates the non-uniqueness associated with the Johnson-Cook parameters obtained using inverse methods. Int. J. Adv. Manuf.
Technol. 2022, 120, 2373–2384. [CrossRef]
30. Wang, C.; Shi, D.; Yang, X.; Li, S.; Dong, C. An improved viscoplastic constitutive model and its application to creep behavior of
turbine blade. Mater. Sci. Eng. A 2017, 707, 344–355. [CrossRef]
31. Wu, M.; Zhang, S.; Ma, S.; Yan, H.; Wang, W.; Li, Q. Hot Deformation Behavior of Q345 Steel and Its Application in Rapid Shear
Connection. Materials 2019, 12, 2186. [CrossRef] [PubMed]
32. Zhao, G.; Tian, Y.; Song, Y.; Li, J.; Li, H.; Zhang, J. A Comparative Study of Three Constitutive Models concerning Thermo-
Mechanical Behavior of Q345 Steel during Hot Deformation. Crystals 2022, 12, 1262. [CrossRef]
33. Niu, D.; Zhao, C.; Li, D.; Wang, Z.; Luo, Z.; Zhang, W. Constitutive Modeling of the Flow Stress Behavior for the Hot Deformation
of Cu-15Ni-8Sn Alloys. Front. Mater. 2020, 7, 577867. [CrossRef]
34. Chao, Z.L.; Jiang, L.T.; Chen, G.Q.; Zhang, Q.; Zhang, N.B.; Zhao, Q.Q.; Pang, B.J.; Wu, G.H. A modiﬁed Johnson-Cook model
with damage degradation for B4Cp/Al composites. Compos. Struct. 2022, 282, 115029. [CrossRef]
35. Bibhanshu, N.; Gussev, M.N.; Massey, C.P .; Field, K.G. Investigation of deformation mechanisms in an advanced FeCrAl alloy
using in-situ SEM-EBSD testing. Mater. Sci. Eng. A 2022, 832, 142373. [CrossRef]
36. Wu, X.; Suo, H.; Ji, Y.; Li, J.; Ma, L.; Liu, M.; Zhang, Z.; Wang, Q. Systematical analysis on the grain orientation evolution of pure
nickel under plastic deformation by using in-situ EBSD. Mater. Sci. Eng. A 2020, 792, 139722. [CrossRef]

## Page 18

Crystals 2023, 13, 1170 18 of 18
37. Zhang, Z.-W.; Li, Z.; Liu, Y.; Wang, J.-T. Path Dependency of Plastic Deformation in Crystals: Work Hardening, Crystallographic
Rotation and Dislocation Structure Evolution. Crystals 2022, 12, 999. [CrossRef]
38. Jiang, J.; Zhai, H.; Du, M.; Wang, D.; Pei, X.; Ma, X.; Wang, B. Temperature-dependent deformation and cracking behavior in Cr
coating for accident tolerant fuel cladding: An in-situ SEM study. Surf. Coat. Technol. 2021, 427, 127815. [CrossRef]
39. Li, S.; Wang, Y.; Wang, X. In-situ Observation of the Deformation and Fracture Behaviors of Long-Term Thermally Aged Cast
Duplex Stainless Steels. Metals 2019, 9, 258. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
