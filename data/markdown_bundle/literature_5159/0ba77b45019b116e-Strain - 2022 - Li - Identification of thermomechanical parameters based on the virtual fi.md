# Strain - 2022 - Li - Identification of thermomechanical parameters based on the virtual fields method combined with the

<!-- source: D:\总文献\Strain - 2022 - Li - Identification of thermomechanical parameters based on the virtual fields method combined with the.pdf -->
<!-- file_sha256: 0062311ab9fee1de67cd3b0c2467d2f60d69a2cf72fd4fefca9e04f710fb5623 -->

## Page 1

RESEARCH ARTICLE
Identification of thermomechanical parameters based on
the virtual fields method combined with the sampling
moiré method
Yangyang Li | Huimin Xie
School of Aerospace Engineering,
Tsinghua University, Beijing, China
Correspondence
Huimin Xie, School of Aerospace
Engineering, Tsinghua University. Beijing,
China.
Email:
xiehm@mail.tsinghua.edu.cn
Funding information
National Key Research and Development
Program of China, Grant/Award Number:
2017YFB1103900; National Natural
Science Foundation of China,
Grant/Award Numbers: 11972209,
12032013; National Science and
Technology Major Project, Grant/Award
Number: 2017-VI-0003-0073
Abstract
Thermomechanical parameters are important indicators for evaluating the
mechanical properties of superalloys and generally include the coefficients of
stiffness and thermal expansion at high temperatures. At present, there are
few methods for simultaneously characterising the thermomechanical parame-
ters of superalloys, especially single-crystal superalloys. To satisfy the demand
for simultaneously identifying the thermomechanical parameters of
orthotropic superalloys, an optimised virtual fields method for decoupling the
thermomechanical parameters was developed in this study by combining the
self-developed heat-resistant grids and the sampling moiré method. First, sev-
eral factors, including the oblique angle of the grids, image noise and
thermomechanical coupling phenomena, were studied through numerical
experiments to analyse their influences on the identification accuracy. Then,
an optimised identification strategy was established. Finally, the
thermomechanical parameters of Ni-based polycrystalline and single-crystal
superalloys were successfully identified and comparatively studied. The identi-
fication results demonstrate that the proposed method is highly accurate and
robust. This research will provide an effective way to accurately characterise
the multiple parameters of superalloys at high temperatures.
KEYWORDS
Ni-based superalloys, sampling moiré method, thermomechanical parameters, virtual
fields method
1 | INTRODUCTION
Superalloys refer to a kind of metal material that can work for a long time in a high-temperature environment above
600/C14 C and have been widely applied in fields such as aerospace and engineering. [1] Among them, several have become
important structural materials for hot-end components, such as engine blades. Studying the mechanical properties of
these superalloys in high-temperature environments is a prerequisite for their practical application. Therefore, charac-
terisation of the thermomechanical parameters of these superalloys has garnered extensive attention from researchers
and designers. Based on existing results, in the determination of the stress –strain relationship, the measurement of
strains at high temperatures remains challenging. In practical applications, only the average strain within a centimetre
length can be calculated using extensometers, and strain gauges can only quantify the average strain at a single point.
Received: 29 April 2022 Revised: 25 August 2022 Accepted: 3 October 2022
DOI: 10.1111/str.12429
Strain. 2023;59:e12429. wileyonlinelibrary.com/journal/str © 2022 John Wiley & Sons Ltd. 1o f2 4
https://doi.org/10.1111/str.12429

## Page 2

In addition, the sensing elements used in the above-mentioned techniques at high temperatures are expensive. When
characterising the constitutive parameters of orthotropic materials using these techniques, multiple specimens with dif-
ferent orientations are often necessary, and several sets of experiments are required to compute all constitutive parame-
ters. Therefore, the entire experimental procedure is complex and costly. The identification methods for constitutive
parameters based on full-field measurements have rapidly developed and could make full use of nonuniform deforma-
tion fields to identify all the parameters through one experiment. There are numerous well-studied inversion strategies
such as integrated digital image correlation,
[2,3] the modified error in the constitutive equation approach [4] and the
virtual fields method (VFM). [5–7]
Among these, the VFM has the advantage of efficient calculation and has been widely used in various constitutive
models.[8–10] In related studies for simultaneous characterisation of thermomechanical parameters, Hao et al. [11]
characterised the thermomechanical behaviour of isotropic materials based on the eigenfunction VFM (E-VFM). [12]
Afterwards, Hao et al. [13] extended the E-VFM to identify the thermomechanical parameters of orthotropic materials
using the unnotched Iosipescu configuration. Unlike Hao et al., Ma et al. [14] manually selected six virtual displacement
fields for the three-point bending configuration of composite materials and simultaneously identified four elastic con-
stants and two coefficients of thermal expansion (CTE). Recently, Su et al. [15] searched effective virtual displacement
fields using the minimum condition number of a matrix based on polynomial virtual fields and successfully identified
the stiffness coefficients and CTE of composite materials. From the above literature, several advances have been made
in the theory and application of characterising the thermomechanical parameters using the VFM. However, these stud-
ies have limitations. For the VFM, a more automated and general procedure for decoupling the thermomechanical
parameters remains an important issue.
Full-field deformation measurement is a vital basis of the VFM for characterising the mechanical properties of
materials. Optical full-field measurement techniques such as digital image correlation (DIC),
[16–18] moiré interference
(MI),[19–21] and the grid method [22,23] can provide a wealth of deformation information for the VFM. In recent years,
the sampling moiré (SM) method has rapidly developed as a new moiré technique and has been widely applied in defor-
mation measurements at the macro- and micro-scales.
[24–28] Compared with MI, the SM method does not require high-
density diffraction gratings and can achieve high-precision measurements using low-frequency gratings. Moreover, the
fabrication procedure for gratings in the SM method is simpler, more efficient and low-cost, especially for heat-resistant
gratings.[29] The SM method also does not require a complex optical interferometric system. [29] The change in image
contrast at high temperatures has little effect on the SM; therefore, the decorrelation phenomenon of the speckle
images in high-temperature DIC can be avoided. Several studies have shown that the moiré method has a stronger anti-
noise capability than DIC. [7,30] The grid method (or localised spectrum analysis, LSA) is another widely studied method
of retrieving phase and phase derivatives from grid images. Compared with the SM method, the grid method utilises
the windowed Fourier transform, and the SM method is a global phase analysis technique. More information about the
gird method is discussed in Grédiac et al. [22] Owing to the advantages of the SM method for deformation measurements,
it is necessary to match the SM method with the VFM. Nevertheless, when calculating the strain fields using the SM
method, numerical calculations, such as image filtering and displacement smoothing, are involved. Therefore, ensuring
the identification accuracy of the VFM combined with the SM method (SM-VFM) is an issue that must be studied
urgently.
To address the above issues, the identification error of the SM-VFM procedure was systematically investigated in
this study, and the thermomechanical parameters of Ni-based polycrystalline superalloy (NBPS) and Ni-based single-
crystal superalloy (NBSCS) were successfully decoupled by the proposed optimal SM-VFM procedure. The research
framework is illustrated in Figure
1, and this manuscript is organised as follows: In ‘Theory’, the basic principle of
the two-dimensional (2D) moiré phase analysis using the SM method was introduced, and based on the noise mini-
mization optimization procedure of the optimised VFM theory in Pierron and Grédiac, [5] a procedure for decoupling
the coefficients of stiffness and thermal expansion was derived, which does not require simulation data. In ‘Simula-
tion analysis ’, the strain fields near the specimen edges were corrected via interpolation, and the influence of the
oblique angle of the grids and image noise on the accuracy of the identification results was analysed. Subsequently,
the thermomechanical coupling phenomenon was studied. In Section
4, combined with the SM method and self-
developed grid fabrication technique, the thermomechanical parameters (stiffness coefficients and CTE) of the NBPS
(650/C14 C) and NBSCS (800 /C14 C) were successfully characterised. The simulated and experimental results demonstrate
the feasibility and high robustness of the SM-VFM procedure for parameter identification at room and high
temperatures.
2o f2 4 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

2 | THEORY
2.1 | 2D moiré phase analysis using the SM method
The 2D grid patterns for the SM method are shown in Figure 2, which can be treated as a combination of two parallel
gratings (gratings X and Y). In Figure 2, the grating pitches of gratings X and Y are both pg, and the angle between the
principal direction of grating X and the x-direction is θ.
The orthogonal grids described above can be separated to obtain gratings X and Y through mean filtering or
frequency-domain filtering.[31] Taking grating X as an example, intensity IX can be expressed as follows:
Parameter identification of the SM-VFM at room and high temperatures 
Simulation analysis
Theory
Isotropic materials
(Ni-based polycrystalline 
superalloys) 
Full-field measurements using 2D-SM technique
Orthotropic materials
(Ni-based single-crystal 
superalloys) 
Stiffness coefficients and 
CTE
Applications
Fabrication of the 
heat-resistant grids
Image acquisition 
system at high 
temperatures
Optimized VFM
Thermomechanical 
coupling effectsImage noiseOblique angle of grids
Optimized virtual fields method2D sampling moiré method 
Stiffness coefficients
Room temperature High temperature 
FIGURE 1 Research framework
FIGURE 2 Diagram of 2D grids for the sampling moiré (SM) method. (a) Simulated and (b) experimental grids. ( pgX = pgY = pg in this
paper)
LI AND XIE 3o f2 4
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

IX ¼ AX þ BX cos 2 π x
pXx
þ y
pXy
 !"#
¼ AX þ BX cos ϕXðÞ , ð1Þ
where AX and BX are the background and modulated amplitude of grating X, respectively, and ϕX represents the phase
of grating X. pXx and pXy are the pitches in the x and y directions caused by the incline of grating X, as shown in
Figure 2a.
After N-step downsampling and interpolation of grating X, the intensities of the phase-shifting moiré fringes can be
obtained using[31]
Im/C0 X x, y; kðÞ ¼ AX þ BX cos 2 π x
pXx
þ y
pXy
/C0 x
N
 !
þ 2π k
N
"#
¼ AX þ BX cos ΦX x, yðÞ þ 2π k
N
/C20/C21
, k ¼ 0, 1, … , N /C0 1ðÞ ,
ð2Þ
where ΦX represents the moiré phase before deformation. Generally, the cubic spline interpolation was implemented to
generate the phase-shifting moiré fringes. [24] Furthermore, the moiré phase can be calculated from the phase-shifting
method using a discrete Fourier transform (DFT) algorithm [31]:
ΦX ¼/C0 arc tan
PN/C0 1
k¼0 Im/C0 X x, y;kðÞ sin 2 πk=NðÞPN/C0 1
k¼0 Im/C0 X x, y;kðÞ cos 2 πk=NðÞ
: ð3Þ
The relationship between the phase difference and displacement fields between a deformed state and an initial state
can be represented by [31]
ΔΦX ¼ Φ0
X /C0 Φ0
X ¼ 2π x /C0 ux
pXx
þ y /C0 uy
pXy
 !
/C0 2π x
pXx
þ y
pXy
 !
¼/C0 2π ux
pXx
þ uy
pXy
 !
,
ð4Þ
where Φ0
X represents the moiré phase after deformation, Φ0
X represents the moiré phase of the initial state, and ux and
uy represent the displacement fields in the x and y directions, respectively.
By performing the same analysis on grating Y, final expressions for the displacement fields can be obtained using [31]
ux
uy
"#
¼/C0 1
2π
1=pXx 1=pXy
1=pYx 1=pYy
"# /C0 1
ΔΦX
ΔΦY
"#
¼/C0 pg
2π
cos θ /C0 sin θ
sinθ cos θ
"# /C0 1
ΔΦX
ΔΦY
"#
,
ð5Þ
where pYx, pYy, and θ are defined in Figure 2. To calculate the strain fields, the least-squares plane fit (LSPF) was
adopted in this paper, and it is implemented by a 2D Savitzky –Golay digital differentiator with high computational
efficiency.[32]
4o f2 4 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

2.2 | Optimised VFM for decoupling thermomechanical parameters
Ni-based superalloys are a class of materials that exhibit excellent mechanical properties at high temperatures;
for example, their tensile strength can reach hundreds of MPa at 1000 /C14 C. Among them, NBPS has isotropic
properties, whereas NBSCS is orthotropic because of its face-centred cubic structure. The NBSCS belongs to the cubic
crystal system; therefore, the elastic stiffness matrix C of the NBSCS in the case of three dimensions (3D) can be
given by
[33–36]
C ¼
C11 C12 C12 000
C12 C11 C12 000
C12 C12 C11 000
000 C44 00
0000 C44 0
00000 C44
2
666666
664
3
777777
775
C44 ≠ C11 /C0 C12
2ðÞ
, ð6Þ
where Cij (i, j = 1,2,4) are the three independent components of the stiffness matrix in the crystal coordinate system.
For the in-plane strain and stress in the 1 –2 plane, the constitutive relationships of the NBSCS can be
represented by[37]
σ11
σ22
σ12
2
64
3
75 ¼
Q11 Q12 0
Q12 Q11 0
00 Q66
2
64
3
75
ε11
ε22
γ12
2
64
3
75, ð7Þ
where σij (i, j = 1, 2) are the stress components, ε11 and ε22 are the normal strain components, γ12 is the engineering
shear strain component and Qij (i, j = 1,2,6) are the in-plane stiffness coefficients. Different from the isotropic constitu-
tive, Q66 is not equal to ( Q11-Q12)/2 in Equation ( 7). The relationship between Qij and Cij is presented in Appendix A.
Based on the noise minimization optimization procedure in Pierron and Grédiac, [5] assuming that the strain fields
contain noise, the thermoelastic constitutive relationships of the NBSCS at high temperatures are expressed as follows:
σ11
σ22
σ12
2
64
3
75 ¼
Q11 Q12 0
Q12 Q11 0
00 Q66
2
64
3
75
ε11 /C0 γβ1ðÞ /C0 αΔT
ε22 /C0 γβ2ðÞ /C0 αΔT
γ12 /C0 γβ6
2
64
3
75, ð8Þ
where γ is the amplitude of the random variable strain field and βi (i = 1,2,6) are zero-mean Gaussian processes.
Detailed reasons for these hypotheses can be referred to Pierron and Grédiac. [5] α is the CTE along the crystal axes
(i.e. 1–2 plane), and ΔT is the temperature change.
For the quasi-static and in-plane problem neglecting the virtual acceleration work, the governing equation of the
VFM can be represented by [5]
Z
S
σijε/C3
ijdS ¼
Z
Lf
Tiu/C3
i dli , j ¼ 1, 2ðÞ , ð9Þ
where S is the domain, ε/C3
ij represents the virtual strain fields, Lf is the boundary where the external force Ti is applied
and u/C3
i expresses the virtual displacement components on Lf.
Equation (8) can be inserted into Equation ( 9) to obtain the following equation:
LI AND XIE 5o f2 4
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

Q11
Z
S
ε11 /C0 γη1ðÞ ε/C3
11 þ ε22 /C0 γη2ðÞ ε/C3
22
/C2/C3
dS þ Q12
Z
S
ε11 /C0 γη1ðÞ ε/C3
22 þ ε22 /C0 γη2ðÞ ε/C3
11
/C2/C3
dS
þQ66
Z
S
γ12 /C0 γη6ðÞ γ/C3
12dS /C0 A
Z
S
ε/C3
11 þ ε/C3
22
/C0/C1
dS ¼
Z
Lf
Tiu/C3
i dl,
ð10Þ
where the coupling term A is ( Q11 + Q12)αΔT. Polynomial functions are used to express the virtual displacement
fields[5]:
u/C3
1 ¼
Xm
i¼0
Xn
j¼0
Aij
x1
L
/C16/C17 i x2
w
/C16/C17 j
u/C3
2 ¼
Xm
i¼0
Xn
j¼0
Bij
x1
L
/C16/C17 i x2
w
/C16/C17 j
,
ð11Þ
where Aij and Bij are unknown coefficients, L and w are the typical dimensions along the x1-direction and x2-direction,
respectively, and m and n are selected as three in this study. The benefit of Equation ( 11) is that the unknown coeffi-
cients are linearly related to the variables x and y; therefore, the noise minimization optimization procedure was easy to
analyse, and it is convenient to store the virtual fields in MATLAB.
The coupling term A and stiffness coefficients Qij can be identified according to the noise minimization optimization
procedure in Pierron and Grédiac [5]; detailed equation derivations are illustrated in Appendix B. Finally, the CTE can
be calculated according to the following equation:
α ¼ A
Q11 þ Q12ðÞ ΔT : ð12Þ
3 | SIMULATION ANALYSIS
In this section, numerical experiments that were performed to analyse the identification errors in the SM-VFM proce-
dure are described. First, the strain fields near the specimen edge were numerically corrected. Subsequently, several
important factors influencing the identification results were comparatively studied, including the oblique angle of the
grids, image noise and the coupling phenomena of the thermomechanical properties.
3.1 | Simulation procedure
In the numerical experiments, the three-point bending configuration was utilised because it has been widely studied for
characterising multiple parameters of orthotropic materials at both room and elevated temperatures. [2,15,39] First, the
displacement fields were calculated by ABAQUS/Standard. Three parts (the fixed end, loading end and specimen) were
established in ABAQUS, as shown in Figure 3. There were contacts between the fixed end, loading end and specimen.
For the contact properties, the normal behaviour was ‘hard’ contact, and the tangential behaviour was frictionless. All
displacements at the bottom of the fixed end were constrained, and the displacement in the x-direction was constrained
at the loading end and right side of the specimen. The material coordinate system (1 –2) was consistent with the coordi-
nate system ( x-y). The element type was CPS4, and the element size of the specimen was 0.025 mm. The selection of ele-
ment sizes can be found in Ma et al. [14] Based on Su et al., [15] the geometric size ratio L/h was set to 1.67. The CTE set
in ABAQUS/Standard was 18 /C2 10/C0 6//C14 C, and ΔT was set in the module of predefined fields. The other parameters in
ABAQUS are listed in Table 1.
The simulated experimental procedure is shown in Figure 4 and was realised using self-programmed MATLAB
codes. The displacements at the nodes were exported from ABAQUS and interpolated at pixel positions to generate
the deformed image. The data reconstruction procedure can be realised using the MATLAB function griddata.
6o f2 4 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

h
L
x
y
tF0
1
2
Fixed end
Specimen
Loading end
A
B Fixed end
Specimen
B
r
r
Specimen
Loading endA
FIGURE 3 Schematic view of the three-point bending configuration in ABAQUS
TABLE 1 Parameters set in ABAQUS
L (mm) h (mm) t (mm) r (mm) Q11 (GPa) Q12 (GPa) Q66 (GPa) F0 (N)
15 9 2 2 150 45 100 920.3
Interpolation at the pixel positions
U(x,y),V(x,y)
Reference image
I0={(1+cosφX)h(1+cosφY)}h255/4
φX=2π(x/pXx+y/pXy)
φY=2π(x/pYx+y/pYy)
Deformed image
I1 ={(1+cosφ’X)h(1+cosφ’Y)}h255/4
φ’X=φ X+2π(U/pXx+V / pXy)
φ’Y=φ Y+2π(U/pYx+V / pYy)
Introduction of the noise, mean filtering
IX IY IY’IX’
ΦX ΦY ΦX’ ΦY’
unit: pixelU V
Down sampling, interpolating and DFT
Smoothing and LSPF
Parameter identification using VFM
-2 20
-3×10
εxx
-2 20 -4×10
εyy
0-5-10 5
γxy
-4×10
-10-15 -5
Parallel gratings
Moiré phases
Displacement fields
Strain fields
x
y
Displacement fields from 
FEM
FIGURE 4 Flowchart of the simulated experiments
LI AND XIE 7o f2 4
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

Similar data reconstruction methods can be found in Rossi et al. [6] The size of the simulated images (8-bit level)
was 361 /C2 601 pixels 2, which was the same as in real experiments. Typically, in the SM method, continuous func-
tions consisting of a sine or cosine function are used to generate the grid images. [40,41] In this study, the grid images
were modelled by the equations in Figure 4, which agree well with the experimental images (see Figure 1). The
images were finally exported to simulate the quantized versions of the real camera sensors using the MATLAB
function imwrite.
3.2 | Correction of the strain field near the specimen edges
In the SM method, the grating is downsampled with sampling pitch ps, and then moiré patterns are generated by
cubic spline interpolation. [24] Taking a one-dimensional SM method as an example, owing to the lack of sufficient
grayscale information near the specimen edges, overinterpolation will occur, which results in a large phase error
(see Figure 5).
Figure 5a indicates that because of equally spaced sampling, the interpolated values of the moiré patterns near the
specimen edges exceeded the original range of the grey value. Figure 5b shows that when ps was close to pg, the relative
error of the phase gradient d ΦX/dx was smaller and the number of inaccurate data points was lower. In general, the
width of the zone is pg/2 to pg. Considering that the VFM is sensitive to data near the specimen edges, it is necessary to
correct the strain fields of the SM. [6,42] In this study, different numerical methods for correcting the strain fields near
the specimen edges were comparatively investigated, the results of which are shown in Figure 6.
Figure 6a illustrates two numerical strategies: A and B. For strategy A, inaccurate data (the displacement or strain)
are first deleted. Then, the final column (row) of the remaining data is placed in the final column (row) of the original
data, and cubic spline interpolation is finally performed. Conversely, for strategy B, the final few columns (rows) of the
remaining data are supplemented to the boundary of the original data in an interval of one column (row).
The displacement and strain fields were processed according to the aforementioned two strategies. The specific pro-
cedure was as follows: For the displacement fields ( U0) calculated using the SM method, the corrected displacement
fields (Uc) were obtained using either strategy A or B. Finally, the corrected strain fields ( εc) were obtained according to
Uc (Method-01 and Method-02 in Figure 6) using the LSPF. An alternative processing method was to first obtain the
uncorrected strain field ( ε0) directly from U0, and then the corrected strain fields ( εc) were obtained by performing
either strategy A or B on ε0 (Method-03 and Method-04 in Figure 6).
The corrected strain fields are shown in Figure 6b. Furthermore, the RMSE of the strain fields ( εxx) with different
grating pitches were analysed, as shown in Figure 6c. It can be observed that the accuracy of the strain fields near the
specimen edges can be improved by performing strategy A on the uncorrected strain fields. For strategy A, fewer data
were impacted by field reconstruction than in strategy B. For Method-01, further numerical errors will be brought about
when the strain calculation was performed on the reconstructed displacement field than in Method-03. It should be
noted that the sampling pitch p
s was pg-1 in Figure 6c.
(b)
A
A
B
B
x (pixel)
Relative error of dΦX / dx
ps=10
ps=11
ps=13
ps=14
(a) pg=12
=10SV
=11SV
=13SV
=14SV
0
10 20 30
0.02
0
0.04
0.06
0.08
0
0.02
0.04
0.06
0.08
270 280 290 300
FIGURE 5 (a) Generated moiré patterns (blue lines) and (b) relative errors of the phase gradient with different sampling pitches ps
(grating pitch pg = 12)
8o f2 4 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

3.3 | Error analysis
3.3.1 | Influence of the oblique angle of the grids
In practical experiments, there is always an oblique angle between the grids and specimen (see Figure 2); therefore, it is
necessary to analyse the influence of the oblique angle on the SM-VFM procedure. For grids with a small oblique angle
(usually ≤10
/C14 ), mean filtering with a regular rectangular window is often used to separate the orthogonal grids to obtain
gratings X and Y. For a regular rectangular window, the window height ( h0, unit: pixels) is generally equal to pg, and
the window width ( w0, unit: pixels) is generally one or two pixels. The value of the window is 1/( h0 /C2 w0). When the
oblique angle becomes too large (>10 /C14 ), the identification errors increase significantly, as shown in Figure 7.I n
Figure 7, the weighted relative error Errw is defined as [7,43]
Errw ¼
P
ij
QIde
ij /C0 QRe f
ij
/C12/C12/C12
/C12/C12/C12
P
ij
QRe f
ij
, ij ¼ 11 12 66 /C138 ,½ð 13Þ
where QRe f
ij are the reference values (see Table 1) and QIde
ij are the identification values. In Figure 7, the blue star
markers represent the identification errors using the finite element (FE) strain fields (averaged value at the element
centre).
Remaining data
Interpolated data
Inaccurate data
BA(a)
(b)
C
Method-01: displacement interpolation with A
Method-02: displacement interpolation with B
Method-03: strain interpolation with A
Method-04: strain interpolation with B
(c)
C
Grating pitch (pixels)
)ESMR(01goL niartS
Strain
Position (Pixel)
2
2.5
-4×10
1.5
1
0.5
92 96 100
Accurate strain
Method - 01
Method - 02
Method - 03
Method - 04
Uncorrected strain
8 10 12 14
-4.2
-4.4
-4.6
-4.8
-5
-5.2
-5.4
Method- 04
Method - 03
Method - 02
Method - 01
Uncorrected
1
FIGURE 6 (a) Strategies A and B, (b) corrected strain fields and (c) root-mean-square errors (RMSE) of the strain fields with different pg
LI AND XIE 9o f2 4
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

To address this problem, the nonrectangular mean filtering with an oblique window was investigated in this study,
as shown in Figure 8a. The rectangular window size was 12 /C2 1 pixels, and the values were 1/12. The oblique window
size was 14 /C2 7 pixels 2; the value of the yellow square was 1/14, and the rest was zero. For the oblique window, it is
(a) Errw(ΔT=0 ȭ) (b) Errw(ΔT=100 ȭ)
(c) CTE (ΔT=100 ȭ)
FIGURE 7 Comparison of two types of mean filtering windows. (a) Errw (ΔT = 0/C14 C), (b) Errw (ΔT = 100/C14 C) and (c) coefficients of
thermal expansion (CTE) . (pg = 12 pixels, ps = 11 pixels)
0.0833
1
12
Rectangular 
window
0
0.0714
14
1
17
Oblique window(a)
x
y
Grating X
Grating Y
Rectangular 
window
Oblique 
window
A
(b)
B
(c)
C
D
E
F
(d)
G
H
Fourier domain Fourier domain Fourier domain
FIGURE 8 (a) Schematic diagram of filtering with two types of windows to obtain grating X, (b) amplitude spectrum of the simulated
parallel grating X, (c) amplitude spectrum of the filtered grating X using a regular rectangular window and (d) amplitude spectrum of the
filtered grating X using an oblique window. (Oblique angle = 25/C14 )
10 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

recommended that the window height ( h1, unit: pixels) be selected as pg to 1.5 pg and the window width ( w1, unit:
pixels) be selected as pg /C2 sinθ. The values near the diagonal of the window were 1/ h1, and those of the rest of the win-
dow were 0. Figure 7 shows that the identification errors were significantly reduced after performing mean filtering
with an oblique window when the oblique angle was greater than 10 /C14 . According to Section 2.1, the phase retrieving in
the SM method was based on parallel gratings. The Fourier spectrum of a perfect parallel grating X is shown in
Figure 8b. For the grids with a large oblique angle, if a regular rectangular window is still used to perform mean filter-
ing, the frequency components in other directions will appear, as shown in Figure 8c. The oblique window can avoid
this problem (see Figure 8d). It should be noted that frequency-domain filtering can also be used to separate the orthog-
onal grids; however, this method is limited by its low efficiency. Hence, it will not be discussed in this paper. In the
practical experiment, if the position of the sample is not significantly inclined during the grid fabrication procedure, the
angle of inclination of the grid is usually within 5 /C14 .
Furthermore, for grids with a large oblique angle (>10 /C14 ), the influence of the sampling pitch ps on the identification
errors was comparatively studied. Assuming the oblique angle was 13 /C14 and the grating pitches were 8, 10, 12 and
14 pixels, the identification errors under different sampling pitches were analysed, as shown in Figure 9. The results
prove that, if the sampling pitch ps is still pg-1, the identification errors are relatively large, and when ps is approxi-
mately pg/2, the identification errors of each parameter are relatively small.
3.3.2 | Influence of image noise
Image noise is another important factor that affects the measurement accuracy of deformation fields. In the SM
method, mean filtering of the grid images and smoothing of the displacement fields are two essential steps (see
Figure 4). The orthogonal grids could be separated into two unidirectional gratings (gratings X and Y) by mean filtering,
and the image could also be smoothed to reduce the noise effect. Additionally, numerous studies have demonstrated
that strain fields directly calculated from the displacement fields generally have large noise
[6,23] and that strain fields
calculated from smoothed displacement fields are significantly better. In this study, white Gaussian noise was added to
Errw(ΔT=0 ȭ)(a) Errw(ΔT=100 ȭ)(b)
CTE (ΔT=100 ȭ)(c)
rorre evitaleR
Relative error
rorre evitaleR
FIGURE 9 Comparison of different sampling pitches. (a) Errw (ΔT = 0/C14 C), (b) Errw (ΔT = 100/C14 C), and (c) coefficients of thermal
expansion (CTE). (Oblique angle = 13/C14 )
LI AND XIE 11 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 12

the grey level value of the grid images (oblique angle = 5/C14 ), and a standard deviation (SD) of five grey levels was consid-
ered. Rectangular mean filtering was performed M times to separate the orthogonal grids and then the displacement
fields were smoothed N times with the 2D Gaussian smoothing kernel (the window size was 6 σ, and σ was the Gaussian
kernel SD[44]).
To guarantee identification quality, the relationship between M and N was studied, as shown in Figure 10a–c
(Gaussian kernel SD = 4). The results show that, compared with grid image filtering, the greater the number of dis-
placement field smoothing, the larger the errors on the identification results. Therefore, it is recommended that image
filtering and displacement smoothing be performed less than five times. The appropriate Gaussian kernel SD σ was also
discussed, as shown in Figure
10d (image filtering: two times, displacement smoothing: one time). Because σ deter-
mines the Gaussian window size (6 σ /C2 6σ), a small σ was considered. It is recommended that σ be within 7.
To further illustrate the influence of image filtering and displacement smoothing on the strain fields, the strain
fields were obtained after three times of image filtering and displacement smoothing in the SM method and compared
with the FE strain fields in terms of the mean value (Mean), SD, maximum value (Max.) and minimum value (Min.)
(see Figure 11). The FE strain fields were calculated from the FE displacement fields (nonsmoothed) using LSPF. The
results in Figure 11 show that the strain fields from the SM and FE methods were barely statistically different. There-
fore, it is believed that the strain gradients measured in this study were unaffected.
3.3.3 | Analysis of the thermomechanical coupling phenomenon
The coupling effect between the stiffness coefficients and CTE is related to the mechanical load ( F) and temperature
change ( ΔT). In response to this issue, the influence of these two factors ( F and ΔT) on identification accuracy was
analysed. Image filtering (rectangular window, 12 /C2 1 pixels 2) and displacement smoothing (Gaussian kernel SD = 4)
were performed twice.
Figure 12 shows the effects of F and ΔT on the identification errors. In Figure 12a, the identification errors of CTE
decreased significantly from a large value with increasing ΔT, and the identification accuracy of Q11 and Q66 was still
(d)Relative error
Errw(ΔT=0 ȭ)(a)
1
N
M
5 10 15
10
15
5
0.5
0.4
0.3
0.2
0.1
Errw(ΔT=100 ȭ)(b)
1
N
M
5 10 15
10
15
5
0.4
0.3
0.2
0.1
α (ΔT=100 ȭ)(c)
1
M
N
5 10 15
10
15
5
0.08
0.06
0.04
0.02
FIGURE 10 Identification errors with different numbers of filtering and smoothing performed. ( pg = 12 pixels, ps = 11 pixels)
12 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 13

high; however, the errors of Q12 gradually increased. In Figure 12b, the identification errors of Q66 and CTE were con-
sistently low (<1%) with increasing F, while the errors of Q11 and Q12 gradually decreased from a large value. In
Figure 12c, the sensitivity to noise of Q11 and Q66 was lower than that of Q12, and with the increase of ΔT, the sensitivity
to noise of the stiffness coefficients remained unchanged, while the sensitivity to noise of the coupling term A gradually
decreased from a larger value and tend to be stable. In Figure 12d, the noise sensitivity of all parameters decreased
εxx γxyεyy
(a)
εyyεxx γxy
(b)
0HDQ 6' 0D[ 0LQ0HDQ 6' 0D[ 0LQ 0HDQ 6' 0D[ 0LQ
0HDQ 6' 0D[ 0LQ0HDQ 6' 0D[ 0LQ 0HDQ 6' 0D[ 0LQ
01(niartS -6)
Strain (10-6)
Strain (10-6)
01(niartS -6)
Strain (10-6)
Strain (10-6)
0.2
0.1
0
-0.1
-0.2
0
0
0.2
0.4
0.2
-0.2
0
0
0.1
-0.1
-0.2 -0.2
-0.1
0
FIGURE 11 Comparison of the strain fields from the finite element (FE) and sampling moiré (SM) methods. (a) ΔT = 0/C14 C, and
(b) ΔT = 100/C14 C. (Oblique angle = 5/C14 , noise level = 2%, grids filtering with the rectangular window, Gaussian kernel SD = 4, pg = 12 pixels,
and ps = 11 pixels)
F=920 N ΔT=100 ȭ
rorre evitaleR
Relative error
(a) (b)
(c) (d)
F=920 N ΔT=100 ȭ
FIGURE 12 Identification errors with (a) ΔT, (b) F and relative sensitivity to noise of the stiffness coefficients Qij and coupling term A
with (c) ΔT, (d) F (Oblique angle = 5/C14 , noise level = 2%, pg = 12 pixels, and ps = 11 pixels)
LI AND XIE 13 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 14

gradually with the increase of F, and the noise sensitivity of Q12 was still higher than that of the other three parameters.
Therefore, the effects of F and ΔT on the identification results should be considered simultaneously in practical
experiments.
According to the results in Figure 12, on the premise of ensuring the elastic state, the parameters should be identi-
fied under a large mechanical load in practical experiments. In addition, according to Equation ( 12), the measurement
errors on ΔT (ΔTerror in Figure 13) will only affect the calculation of the CTE; they will not affect the accuracy of the
stiffness coefficients, as shown in Figure 13a. Interestingly, the error on α was minimal when ΔTerror was /C0 1/C14 C instead
of 0/C14 C. This phenomenon was mainly caused by various numerical procedures in the SM method, such as image filter-
ing and displacement smoothing. Figure 13b shows the relative errors of CTE calculated from the SM and FE methods.
For the FE method, the results in Figure 13b were calculated directly from the FE strain fields without interpolation,
smoothing and so on, as in the SM method; therefore, the error on α was minimal for an error on ΔT of 0 /C14 Ca sw e
would expect. Additionally, the special optimised virtual displacement and strain fields for identifying the four parame-
ters (ΔT = 100/C14 C, F = 920 N) were presented in Appendix C (see Figures C1–C4).
3.3.4 | Summaries
In summary, to minimise the identification errors of the SM-VFM procedure, several factors should be considered. First,
the strain fields near the specimen edge should be corrected (Method-03 in Section 3.2). The appropriate sampling pitch
ps should be chosen; when the oblique angle is within 10 /C14 , ps is recommended to be pg-1. If the oblique angle is greater
than 10 /C14 , an oblique window should be considered when performing mean filtering. In addition, the sampling pitch ps
should be approximately pg/2 rather than pg-1. Therefore, to facilitate the calculation, it is recommended that the
oblique angle of the grids be within 10 /C14 in real experiments. Second, image filtering and displacement smoothing
should be performed five times or less, and for displacement smoothing, a smaller Gaussian kernel SD is better than a
larger Gaussian kernel SD.
In addition, compared with the identification errors on the CTE affected by the temperature change, the identifica-
tion errors on the stiffness coefficients are more affected by the mechanical load; therefore, on the premise of ensuring
the elastic state, a large mechanical load should be ensured in real experiments.
4 | APPLICATIONS
4.1 | Experimental procedure
The measurement system at high temperatures is shown in Figure 14a, including a bi-telecentric lens, blue light source,
blue bandpass filter, CMOS and loading system consisting of a heating furnace and three-point bending device. With
rorre evitaleR
ΔTerror (ȭ) ΔTerror (ȭ)
(a) (b)
FIGURE 13 (a) Identification errors with ΔTerror and (b) relative errors of coefficients of thermal expansion (CTE) calculated from the
sampling moiré (SM) and finite element (FE) methods with ΔTerror.( ΔT = 100/C14 C, F = 920 N, oblique angle = 5/C14 , noise level = 2%, pg = 12
pixels, and ps = 11 pixels)
14 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 15

the blue light source and blue bandpass filter, the influence of black-body radiation of high-temperature objects on the
intensity of captured images can be eliminated. [45] Additionally, the strain measurement will not be influenced by the
optical glass in the measuring light path. [46]
Heat-resistant grids are important deformation carriers in the SM method at high temperatures. The heat-resistant
grids in this study were fabricated based on our previous study using the etched-paint-film grid-fabrication technique,
which has proven to be advantageous in terms of operation simplicity, high efficiency and cost-effectiveness. [29] In addi-
tion, the grayscale distribution of the grid images was close to a sinusoidal distribution, which satisfied the demand for
using sparse gratings in deformation measurements. The size of the plate-shaped specimen was
28 mm /C2 9m m /C2 2m m( 2 L /C2 h /C2 t), as shown in Figure
14b, and the optical image of the fabricated orthogonal grids
with a pitch of 0.31 mm is shown in Figure 14c. According to the analysis in Section 3.3.1, for the identification accu-
racy and convenience of calculation, the oblique angle of the grid was within 5 /C14 . The NBSCS specimen was prepared by
a cut along the orthotropy axes of the NBSCS material; therefore, the crystal orientation of the NBSCS specimen was
aligned with the measurement axis ( x-y).
Temperature 
controller
Computer
Blue LED 
CMOS
Bilateral telecentric lens
Blue bandpass filter
Heating furnace
Observation window
Sample
(a)
(c)
500 μm
h
t
(b)
FIGURE 14 (a) Measurement system, (b) specimen and (c) optical image of the grids
TABLE 2 Imaging and specifications of the sampling moiré method
Camera MER-130-30UM-L
Pixel depth 8 bits
Field of view (mm 2) 33.2 /C2 27.6
Field of view (pixels 2) 1280 /C2 1064
Image scale ≈38 pixels/mm
Noise level (20 /C14 C) 1.14%
Noise level (800 /C14 C) 1.57%
ps 11 pixels
pg 0.31 mm ( ≈11.8 pixels)
Image prefiltering Mean filtering, four times
Mean filtering window Rectangular, 12 /C2 1 pixels2
Displacement smoothing Gaussian, kernel 4, four times
Strain window (pixels) 64
LI AND XIE 15 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 16

Based on the analysis in Sections 3.3.1 and 3.3.2, the imaging and specifications of the SM method are listed in
Table 2. Before the experiments, the specimen was preloaded to 30 N, which effectively prevented the rigid body
movement when the loading end touched the specimen and shortened the testing time at high temperatures. Sub-
sequently, 30 images were continuously recorded at each loading step to perform the grayscale-averaging technique.
The noise levels at 20 /C14 C and 800 /C14 C were calculated by the ratio of the noise SD to the grid amplitude (256 in this
study) as a percentage. [47] Furthermore, for the high-temperature experiments, considering the time required to sta-
bilise the thermal expansion of the specimen, the hold time at 30 N was set to 15 min. To avoid strain concentra-
tion at the loading end and plastic deformation, images of the unloading process were used for the SM-VFM
procedure.
(a)
200 400 600 1000 12000 800
x (pixel)
300
200
100 )lexip(y
0
Moiré phase in x-direction
20 ȭ/2300 N
(b)
200 400 600 1000 12000 800
x (pixel)
300
200
100y (pixel)
0
Moiré phase in y-direction
20 ȭ/2300 N
(c)
200 400 600 1000 12000 800
x (pixel)
300
200
100 )lexip(y
0
Moiré phase in x-direction
650 ȭ/2400 N
(d)
200 400 600 1000 12000 800
x (pixel)
300
200
100y (pixel)
0
Moiré phase in y-direction
650 ȭ/2400 N
x
y
FIGURE 15 Wrapped moiré phases at (a, b) 20 /C14 C and (c, d) 650 /C14 C
FIGURE 16 Deformation fields of the Ni-based polycrystalline superalloy (NBPS) specimen at 20 /C14 C( F = 2130 N)
16 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 17

4.2 | Experimental results of the NBPS specimen
The wrapped moiré phases of the NBPS specimen at 20 /C14 C and 650 /C14 C are shown in Figure 15, the deformation fields
at 20 /C14 C are shown in Figure 16 and the thermomechanical coupling deformation fields at 650 /C14 C are shown in
Figure 17. Figure 15 shows that the wrapped moiré phases were smooth with a small variation, indicating that the
fabricated sparse grids were of good quality at room and high temperatures. The wrapped phases were
FIGURE 17 Thermomechanical coupling deformation fields of the Ni-based polycrystalline superalloy (NBPS) specimen at 650 /C14 C
(ΔT = 50/C14 C, F = 2,230 N)
Load (kN)
Q11 (GPa)
Q12 (GPa)
(a)
Q11 (GPa)
Q12 (GPa)
Load (kN)
(b)
Load (kN)
Q11 (a PG)
Q12 (GPa)
(c)
Load (kN)
CTE (h10-6 ȭ-1)
(d)
FIGURE 18 Identification results of the Ni-based polycrystalline superalloy (NBPS) specimen. (a) 20 /C14 C, (b) ΔT = 50/C14 C, (c) ΔT = 100/C14 C
and (d) coefficients of thermal expansion (CTE). Blue dashed lines indicate the Q11 reference, whereas the red dashed lines represent the Q12
reference (see Table 3)
LI AND XIE 17 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 18

discontinuous, and a local-phase unwrapping algorithm must be performed to obtain continuous phases. [48] The
results shown in Figures 16 and 17 are consistent with the deformation fields of the three-point bending configura-
tion, indicating the feasibility of the self-developed low-frequency grids combined with the SM method to measure
nonuniform deformation fields. The strain fields near the specimen edges were corrected according to the conclu-
sions presented in Section 3.2.
According to the conclusions in Section 3.3.3, within the elastic deformation range, the mechanical load should be
large to obtain accurate results. The strain fields calculated using the SM method were used as the input for the VFM,
TABLE 3 Identification results of the NBPS specimen
Q11/SD (GPa) Q12/SD (GPa) α/SD (10/C0 6//C14 C)
20/C14 C VFM 222.4/6.89 61.8/4.5 -
Reference[29] 218.9//C0 62.8//C0 -
Error 1.6% 1.6% -
650/C14 C(ΔT = 50/C14 C) VFM 178.2/13.5 56.6/7.1 18.81/0.495
Reference[29] 182.7//C0 59.2//C0 17.28//C0
Error /C0 2.5% /C0 4.4% 8.8%
650/C14 C(ΔT = 100/C14 C) VFM 167.3/11.6 50.7/4.9 18.46/0.054
Reference[29] 182.7//C0 59.2//C0 18.35//C0
Error /C0 8.4% 14.4% 0.60%
Abbreviations: NBPS, Ni-based polycrystalline superalloy; VFM, virtual fields method.
Qij (GPa)
Qij (GPa)
Qij (GPa)
CTE (10-6/ȭ)
Load (kN) Load (kN)
Load (kN) Load (kN)
(a) (b)
(c) (d)
FIGURE 19 Identification results of the Ni-based single-crystal superalloy (NBSCS). (a) 20 /C14 C, (b) ΔT = 50/C14 C, (c) ΔT = 100/C14 C and
(d) coefficients of thermal expansion (CTE)
18 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 19

and the obtained identification results are shown in Figure 18. Table 3 shows a comparison between the VFM results
(averaged values) and reference values from our previous study. [29] The results in Figure 18 and Table 3 indicate the
high accuracy and robustness of the proposed SM-VFM procedure. Note that the reference values of the CTE were cal-
culated by the ratio of the average thermal strain to ΔT. To measure the average thermal strain, the grid images at
550/C14 C/30 N and 600 /C14 C/30 N were selected as the reference images, and the grid image at 650 /C14 C/30 N was selected as
the deformed image. It should be noted that the CTE is dependent on the temperature; therefore, two temperature
changes (ΔT = 50/C14 C and ΔT = 100/C14 C) were studied in the experiments.
TABLE 4 Identification results of the NBSCS specimen
Q11/SD (GPa) Q12/SD (GPa) Q66/SD (GPa) CTE/SD (10 /C0 6//C14 C)
20/C14 C 155.7/4.1 53.2/2.44 113.8/11.9 -
800/C14 C(ΔT = 50/C14 C) 119.3/4.89 44.4/3.18 104.1/7.83 23.04/0.795
800/C14 C(ΔT = 100/C14 C) 122.4/5.63 43.4/3.24 102.4/5.56 20.10/0.178
Abbreviations: CTE, coefficients of thermal expansion; NBSCS, Ni-based single-crystal superalloy; SD, standard deviation.
[001]
[110]
[111]
[001]
[110]
[111]
Plane A Plane B
(e) NBPS (f) NBSCS
A
[001]
B B
[001](c) 20 ȭ (d) 800 ȭ
A
205.5
205
206
204.5
GPa
156.5
157
156
155.5
155
200
250
150
GPa
200
250GPa GPa
150
100
[010]
[100]
[001]
[010]
[100]
[001](a) 20 ȭ (b) 650 ȭ
[100]
[010]
[100]
[010]
unit:GPa
FIGURE 20 Modulus E[hkl] of (a, b, e) Ni-based polycrystalline superalloy (NBPS) and (c, d, f) and Ni-based single-crystal superalloy
(NBSCS)
LI AND XIE 19 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 20

4.3 | Experimental results of the NBSCS specimen
The same experimental procedure was conducted on the NBSCS specimen, and the identified stiffness coefficients and
CTE are shown in Figure 19. The average values and SD of each parameter are listed in Table 4.
Furthermore, to compare the modulus distributions of the two Ni-based superalloys at room and high temperatures,
the modulus E[hkl] along the arbitrary crystallographic axes was calculated using the following equation [33]:.
1
E hkl½/C138
¼ S11 /C0 2 S11 /C0 S12 /C0 S44
2
/C18/C19
l2
1l2
2
þ l2
1l2
3
þ l2
2l2
3
/C0/C1
, ð14Þ
where Sij (i, j = 1,2,4) are the compliance coefficients, which can be calculated from the inverse of the stiffness matrix
Q, and the expressions for l1, l2 and l3 are as follows:
l1 ¼ hﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
h2 þ k2 þ l2
p , l2 ¼ kﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
h2 þ k2 þ l2
p , l3 ¼ lﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
h2 þ k2 þ l2
p : ð15Þ
The moduli E[hkl] of the NBPS and NBSCS at room and high temperatures are shown in Figure 20. The modulus distri-
bution of the NBPS exhibited isotropic properties, and the modulus distribution of the NBSCS exhibited orthotropic
properties. For the NBSCS, the modulus ratio δ is defined as E
[001]/E[111], and the smaller the value of δ, the more obvi-
ous the anisotropy of the modulus. The moduli E[001] and E[111] of NBSCS at 20 /C14 C were 137.5 and 270.5 GPa, respec-
tively, and the moduli E[001] and E[111] at 800 /C14 C were 104.9 and 244.0 GPa, respectively. The modulus ratios δ of the
NBSCS at 20 /C14 C and 800 /C14 C were 0.508 and 0.430, respectively, indicating that the anisotropic property of the NBSCS
was more obvious at high temperatures.
5 | CONCLUSIONS
To simultaneously characterise the thermomechanical parameters of superalloys, an optimised VFM combined with
the SM method (SM-VFM) was developed, and the issues of robustness and accuracy of the identification results have
been well addressed. The main conclusions are as follows:
The identification errors of the SM-VFM procedure were analysed through numerical experiments using the three-
point bending configuration, and the identification strategy was finally optimised. The results showed that the oblique
angle of the grids and image noise had a significant influence on the identification errors (>10%). To achieve high accu-
racy and robustness of the identification results, for gratings with a large oblique angle (>10
/C14 ), the oblique window is
recommended to perform mean filtering, and ps should be approximately pg/2. Meanwhile, image filtering and displace-
ment smoothing should be performed five times or less.
Using the etched-paint-film grid-fabrication technique, heat-resistant orthogonal grids with a frequency of four
lines/mm were successfully fabricated on plate-shaped specimens of the NBPS and NBSCS. The stiffness coefficients
and CTE of the two superalloys were accurately quantified using the developed SM-VFM procedure. For the NBPS, the
three independent stiffness coefficients decreased at high temperatures, and the modulus ratio E
[001]/E[111] also
decreased, indicating that the anisotropy became more obvious at high temperatures.
The research presented herein provides an efficient and low-cost method for accurately identifying the
thermomechanical parameters of materials and is expected to be applied in the characterisation of the
thermomechanical properties of new single-crystal materials.
ACKNOWLEDGEMENTS
This work is financially supported by the National Natural Science Foundation of China (grant nos. 12032013 and
11972209), the National Key Research and Development Program of China (grant no. 2017YFB1103900) and the
National Science and Technology Major Project (2017-VI-0003-0073).
20 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 21

DATA AVAILABILITY STATEMENT
Data are available on request from the authors.
ORCID
Yangyang Li https://orcid.org/0000-0002-1672-2548
REFERENCES
[1] Q. Zhu, G. Chen, C. Wang, L. Cheng, H. Qin, P. Zhang, Metals 2019, 9, 1153.
[2] J. Dong, Z. Liu, J. Gao, Exp. Mech. 2017, 57, 31.
[3] F. Hild, S. Roux, Strain 2006, 42, 69.
[4] S. Guchhait, B. Banerjee, J. Alla, Inverse Probl. Sci. Eng. 2018, 26, 1356.
[5] F. Pierron, M. Grédiac, The virtual fields method , Springer, New York, USA 2012.
[6] M. Rossi, P. Lava, F. Pierron, D. Debruyne, M. Sasso, Strain 2015, 51, 206.
[7] M. Zhou, H. Xie, L. Wu, Opt. Lasers Eng. 2016, 87, 214.
[8] A. Tayeb, J. B. Le Cam, M. Grédiac, E. Toussaint, E. Robin, X. Balandraud, F. Canévet, Strain 2021, 57, e12397.
[9] P. Livens, S. Avril, J. Dirckx, Strain 2021, 57, e12398.
[10] H. Jiang, Z. Lei, R. Bai, J. Liu, Z. Guo, H. Dong, W. Feng, Exp. Mech. 2021, 61, 867.
[11] W. Hao, G. Guo, Y. Zhang, X. Chen, Adv. Eng. Softw. 2016, 93, 22.
[12] N. Nigamaa, S. J. Subramanian, Int. J. Solids Struct. 2014, 51, 295.
[13] W. Hao, Y. Zhang, Y. Yuan, Polym. Test. 2016, 50, 224.
[14] Y. Ma, X. Yao, X. Liu, W. Hao, D. Fang, Proc. R. Soc. A 2013, 469, 20130124.
[15] Y. Su, X. Yao, S. Wang, Y. Ma, Mech. Mater. 2018, 124, 33.
[16] P. Luong, R. Bonnaire, J. N. Périé, Q. Sirvin, L. Penazzi, Strain 2021, 57, e12388.
[17] L. Yu, B. Pan, Exp. Mech. 2021, 61, 1121.
[18] Y. Li, J. Li, Q. Duan, H. Xie, S. Liu, Acta Mech. Sin. 2021, 37, 456.
[19] B. Guo, H. Wang, H. Xie, P. Chen, Theor. Appl. Mech. Lett. 2014, 4, 021010.
[20] M. Zhou, H. Xie, L. Li, Acta Mech. Sin. 2019, 35, 78.
[21] Q. Cao, H. Xie, H. Wang, Strain 2018, 55, e12299.
[22] M. Grédiac, F. Sur, B. Blaysat, Strain 2016, 52, 205.
[23] M. Grédiac, F. Sur, Strain 2014, 50,1 .
[24] Q. Wang, S. Ri, T. Enomoto, Exp. Mech. 2020, 60, 611.
[25] S. Ri, Q. Wang, H. Tsuda, H. Shirasaki, K. Kuribayashi, Strain 2020, 56, e12351.
[26] Z. Lei, Z. Wang, Appl. Mech. Mater. 2012, 226–228, 1975.
[27] Q. Wang, S. Ri, P. Xia, Appl. Optics 2021, 60, 1637.
[28] M. Yadi, Y. Morimoto, M. Ueki, Y. Takaya, J. Phys. Photonics 2021, 3, 024005.
[29] Y. Li, Q. Zhang, H. Xie, Meas. Sci. Technol. 2021, 32, 105008.
[30] W. Shi, Q. Zhang, H. Xie, W. He, Appl. Sci. 2021, 11, 5175.
[31] Q. Wang, S. Ri, H. Tsuda, M. Koyama, K. Tsuzaki, Opt. Express 2017, 25, 13465.
[32] B. Pan, H. Xie, Z. Guo, T. Hua, Optim. Eng. 2007, 46, 033601.
[33] P. E. Aba-Perea, T. Pirling, P. J. Withers, J. Kelleher, S. Kabra, M. Preuss, Mater. Design. 2016, 89, 856.
[34] H. Long, S. Mao, Y. Lin, Z. Zhang, X. Han, J. Alloys Compd. 2018, 743, 203.
[35] J. Everaerts, C. Papadaki, W. Li, A. M. Korsunsky, J. Mech. Phys. Solids 2019, 131, 303.
[36] S. Haussühl, Physical properties of crystals: An introduction , Wiley-VCH, Weinheim, Germany 2007.
[37] Q. Cao, Y. Li, H. Xie, Opt. Lasers Eng. 2020, 125, 105854.
[38] G. Shen, G. Hu, B. Liu, Mechanics of composite materials , Second ed., Tsinghua University publishing house co, Beijing 2013.
[39] M. Grédiac, F. Pierron, Int. J. Numer. Meth. Eng. 2004, 59, 1287.
[40] R. Chen, Q. Zhang, W. He, H. Xie, Opt. Lasers Eng. 2022, 149, 106811.
[41] Q. Wang, S. Ri, Theor. Appl. Mech. Lett. 2022, 12, 100327.
[42] L. Jiang, B. Guo, H. Xie, Acta Mech. Sin. 2015, 31, 173.
[43] M. Zhou, H. Xie, Strain 2019, 55, e12326.
[44] E. W. Grafarend, Linear and nonlinear models: Fixed effects, random effects, and mixed models , Walter de Gruyter, Berlin, Germany
2006.
[45] B. Pan, D. Wu, Z. Wang, Y. Xia, Meas. Sci. Technol. 2011, 22, 015701.
[46] Y. Su, X. Yao, S. Wang, Y. Ma, Optim. Eng. 2017, 56, 034106.
[47] K. Qian, N. Agarwal, S. Ri, Q. Wang, Optim. Eng. 2018, 57,1 .
[48] Q. Wang, S. Ri, H. Tsuda, M. Koyama, Opt. Lasers Eng. 2018, 110, 155.
LI AND XIE 21 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 22

How to cite this article: Y. Li, H. Xie, Strain 2023, 59(1), e12429. https://doi.org/10.1111/str.12429
APPENDIX A
For a cubic crystal system under the crystal axis, the 3D compliance matrix S3D and 2D compliance matrix S2D (in-plane
stress condition) can be expressed as
S3D ¼
S11 S12 S12 000
S12 S11 S12 000
S12 S12 S11 000
000 S44 00
0000 S44 0
00000 S44
2
666
66666
4
3
777
77777
5
, S
2D ¼
S11 S12 0
S12 S11 0
00 S66
2
64
3
75
S66¼S44ðÞ
, ðA1Þ
where Sij are the compliance coefficients.
According to C ¼ S/C0 1
3D and Q ¼ S/C0 1
2D , the relationship between Cij and Qij can be written as [38]
Q11 ¼ C11 /C0 C2
12
C11
Q12 ¼ C12 /C0 C2
12
C11
Q66 ¼ C44:
ðA2Þ
APPENDIX B
Assuming that Equation 10 is linear to the four unknown parameters ( Q11, Q12, Q66 and A), which is not strictly the
case for A since this parameter depends on Q11 and Q12 in a nonlinear way; therefore, it may be a complicated way to
define the optimised virtual fields if this assumption is not considered since the problem is nonlinear. According to
Pierron and Grédiac,
[5] the variances of the stiffness coefficients Qij and coupling terms A can be expressed as follows:
VQ ij
/C0/C1
¼ γ2 S
n
/C18/C19 2
Qapp
11ðÞ 2 þ Qapp
12ðÞ 2/C16/C17 Xn
i¼1
ε/C3 kðÞ
11 MiðÞ
/C16/C17 2
þ ε/C3 kðÞ
22 MiðÞ
/C16/C17 2/C18/C19
þ …
"
… þ 4Qapp
11 Qapp
12
Xn
i¼1
ε/C3 kðÞ
11 MiðÞ ε/C3 kðÞ
22 MiðÞ þ Qapp
66ðÞ 2Xn
i¼1
γ/C3 kðÞ
12 MiðÞ
/C16/C17 2
#
i, j ¼ 1, 2, 6;k ¼ 1, 2, 3ðÞ
VAðÞ ¼ γ2 S
n
/C18/C19 2
Qapp
11ðÞ 2 þ Qapp
12ðÞ 2/C16/C17 Xn
i¼1
ε/C3 kðÞ
11 MiðÞ
/C16/C17 2
þ ε/C3 kðÞ
22 MiðÞ
/C16/C17 2/C18/C19
þ …
"
… þ 4Qapp
11 Qapp
12
Xn
i¼1
ε/C3 kðÞ
11 MiðÞ ε/C3 kðÞ
22 MiðÞ þ Qapp
66ðÞ 2Xn
i¼1
γ/C3 kðÞ
12 MiðÞ
/C16/C17 2
#
,
k ¼ 4ðÞ
ðB1Þ
where n is the number of discretization elements of the calculated area, Qapp
ij i, j ¼ 1, 2, 6ðÞ represents the approximate
parameters and Mi is the i-th discretization element.
22 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 23

Substituting Equation ( 11) into Equation ( B1), the following equations are obtained:
VQ ij
/C0/C1
¼ 1
2 Y kðÞ /C1 HY kðÞ γ2 ¼ η kðÞ
/C16/C17 2
γ2 k ¼ 1, 2, 3ðÞ
VAðÞ ¼ 1
2 Y kðÞ /C1 HY kðÞ γ2 ¼ η kðÞ
/C16/C17 2
γ2 k ¼ 4ðÞ ,
ðB2Þ
where H is a 2( m + 1)(n + 1) matrix and Y(k) is a vector containing the unknown parameters Aij and Bij. Further details
about H and Y(k) are available in Pierron and Grédiac. [5] The ratios of η kðÞ and Qij, A can be used to evaluate the sensi-
tivity to noise of each identified parameter.
In addition, according to the theory of the special VFM and boundary conditions, the constraint equations are repre-
sented by Pierron and Grédiac. [5]
AY kðÞ ¼ Z kðÞ , ðB3Þ
where Z(k) is a vector containing 1 and 0.
By minimising the variance of the k-th parameter as an example, it can be expressed as the following quadratic pro-
gramming problem:
min 1
2 γ2Y kðÞ /C1 HY kðÞ
s:t: AY kðÞ ¼ Z kðÞ :
ðB4Þ
According to the Lagrangian multiplier method, the k-th Lagrangian function is defined as follows:
L Y kðÞ , λ kðÞ
/C16/C17
¼ 1
2 Y kðÞ /C1 HY kðÞ þ λ kðÞ /C1 AY kðÞ /C0 Z kðÞ
/C16/C17
, ðB5Þ
where λ kðÞ is a vector containing Lagrange multipliers.
And the optimality conditions of Equation ( B5) can be expressed by
rYL Y kðÞ , λ kðÞ
/C16/C17
¼ 0
rλL Y kðÞ , λ kðÞ
/C16/C17
¼ 0:
ðB6Þ
Then, the stiffness coefficients Qij and coupling terms A can be identified using the following equation [5]:
HA t
A0
/C20/C21 Y kðÞ
λ kðÞ
()
¼ 0
Ζ kðÞ
/C26/C27
k ¼ 1, 2, 3, 4ðÞ : ðB7Þ
It should be noted that solving Equation ( B7) is an iterative process because the matrix H was dependent on the Qij
parameters which are also unknown ( Qapp
ij in Equation B1). According to Pierron and Grédiac, [5] a first guess for Qij
was used to get a set of special virtual fields and a first guess for the coupling term A was also needed. Then, these
special virtual fields were utilised to get a new set of Qij parameters and coupling term A. And the new set of Qij
parameters was used to obtain a new set of virtual fields and so on. These procedures were iterative until the Qij and
A converge.
LI AND XIE 23 of 24
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 24

APPENDIX C
FIGURE C3 Special optimised virtual displacement and strain fields for identifying Q66
FIGURE C1 Special optimised virtual displacement and strain fields for identifying Q11
FIGURE C2 Special optimised virtual displacement and strain fields for identifying Q12
FIGURE C4 Special optimised virtual displacement and strain fields for identifying the coupling term a
24 of 24 LI AND XIE
 14751305, 2023, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/str.12429 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
