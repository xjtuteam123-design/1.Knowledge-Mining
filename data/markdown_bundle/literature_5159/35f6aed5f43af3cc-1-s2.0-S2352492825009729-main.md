# 1-s2.0-S2352492825009729-main

<!-- source: D:\总文献\1-s2.0-S2352492825009729-main.pdf -->
<!-- file_sha256: 7fa8125d8ae115e3d2d7e73cf94b80784d27979ea77999aa07964d7d616db208 -->

## Page 1

Study on microstructure and mechanics of Cr/Nb on NiCrMo-based fusion 
clad metal based on BP artificial neural network
Guangyu Liu
a
, Yuntao Li
a , *
, Yanchang Qi
b
, Chengyong Ma
b
a
School of Materials Science and Engineering, Tianjin University of Technology, Tianjin 300384, China
b
Central Iron and Steel Research Institute, Beijing 100081, China
ARTICLE INFO
Keywords:
Bp neural network
NiCrMo alloy
Cr/Nb ratio
Low temperature impact toughness
Tensile strength
ABSTRACT
The influence of the Cr/Nb ratio on the low-temperature impact toughness and tensile strength of NiCrMo alloy 
weld metal was investigated. Results from the BP neural network model predictions indicated that within the Cr/ 
Nb ratio range of 7.76 – 12.00, the tensile strength initially increased before subsequently decreasing, with the 
lowest value occurring at a Cr/Nb ratio of 10.43, which yielded a tensile strength of 679 MPa. The low- 
temperature impact toughness decreased proportionally at a nearly constant rate of 4.89, declining from 
72.13 J/cm² to 51.39 J/cm². Experimental data revealed that as the Cr/Nb ratio decreased from 11.68 to 9.16, 
the volume fraction and average size of NbC and Laves phases in the NiCrMo alloy weld metal significantly 
increased, resulting in a reduction of the low-temperature impact toughness from 71 J/cm² to 56 J/cm², while 
the tensile strength remained relatively stable at approximately 686 MPa.
1. Introduction
The 9 % Ni steel, characterized as a low-carbon quenched and 
tempered steel with a martensite and bainite microstructure, is exten -
sively utilized in the production of large liquefied natural gas (LNG) 
storage and transportation equipment, as well as in various cryogenic 
applications. This widespread use is attributed to its excellent toughness 
and high strength at extremely low temperatures [1] . The selection of 
welding materials for 9 % Ni steel has positioned NiCrMo series welding 
materials as representatives of nickel-based alloy welding due to their 
outstanding performance. In the deposited metal,Cr exhibits a higher 
affinity for oxygen than Fe, enabling the formation of a stable (Fe, Cr) ₂ O ₃ 
oxide film on the surface. This oxide film effectively hinders the outward 
diffusion of metal elements and the inward diffusion of detrimental el -
ements such as O, N, and S, thereby safeguarding the alloy against 
corrosion. It is important to note that Cr is a potent carbide-forming 
element capable of generating various carbides (e.g., Cr ₃ C ₂ , Cr ₃ C ₆ , and 
Cr ₇ C ₃ ). The precipitation of Cr carbides along grain boundaries results in 
Cr depletion, consequently diminishing the corrosion resistance of the 
weld metal. While increasing the Cr content can alleviate corrosion is -
sues associated with Cr-depleted zones, excessively high Cr levels in 
alloys C- and N-containing may adversely affect performance. High Cr 
content can lead to the formation of a continuous network of Cr carbides 
at the grain boundaries, which can reduce the material ’ s plasticity and 
toughness, and may also induce cracks, deformation, and localized 
melting at the edges of the deposited metal [2] . Therefore, the Cr con -
tent cannot be increased indefinitely. The introduction of Nb can 
effectively mitigate the phenomenon of Cr depletion, as Nb exhibits a 
significantly higher affinity for C than Cr, thereby preferentially forming 
NbC. Consequently, the addition of Nb aids in reducing Cr loss in the 
grain boundary regions. Relevant studies have demonstrated that in 
other nickel-based alloys, the incorporation of Nb can significantly 
enhance high-temperature strength by forming stable NbC and Ni phases 
[3] . However, in various nickel-based alloys or stainless steels, the 
presence of Nb may result in a decline in the weldability and mechanical 
properties (such as low-temperature impact toughness and fracture 
strength) of the weldments, primarily due to the formation of hard and 
brittle Nb-rich phases [4,5] . Therefore, it is essential to investigate the 
Cr/Nb ratio in NiCrMo deposited metal.
This study employed a model based on the Back Propagation (BP) 
neural network to investigate the impact of CR/Nb on the low- 
temperature impact toughness and tensile strength of NiCrMo alloys. 
The BP neural network is a multi-layer feedforward neural network 
trained using the error backpropagation algorithm, which possesses 
robust nonlinear fitting capabilities and can effectively address 
modeling and prediction challenges in complex systems [6,7] .
* Corresponding author.
E-mail address: 1950148383@qq.com (Y. Li). 
Contents lists available at ScienceDirect
Materials Today Communications
journal homepage: www.else vier.com/loc ate/mtcomm
https://doi.org/10.1016/j.mtcomm.2025.112460
Received 20 February 2025; Received in revised form 1 April 2025; Accepted 5 April 2025 
Materials Today Communications 46 (2025) 112460 
Available online 11 April 2025 
2352-4928/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## Page 2

The BP neural network consists of an input layer, several hidden 
layers, and an output layer. It processes and analyzes complex data by 
learning the mapping relationship between inputs and outputs [8] . In 
this study, we constructed a BP neural network where the elements 
contained in the welding electrode serve as input parameters, while the 
low-temperature impact toughness and tensile strength are designated 
as output parameters. Multiple layers are incorporated in the network to 
predict the sensitivity of the elements ’ influence on the input parameters 
and output properties, as well as to elucidate their complex relation -
ships.Yong Liu et al. [9] based on their research on artificial neural 
networks, found that the high-temperature hardness of hot die steel 
increases with the content of alloying elements such as C, Si, Mo, W, Ni, 
V, and Cr, but decreases with further increases in the content of these 
alloying elements. Additionally, Yang Xiawei et al. [10] employed a BP 
algorithm-trained artificial neural network model to accurately predict 
the mechanical properties of A357 alloy, effectively reflecting the 
impact of heat treatment process parameters on the alloy ’ s performance. 
Through contour maps, they visually demonstrated the relationship 
between aging parameters and ultimate tensile strength, as well as 
elongation.
To investigate the impact of the Cr/Nb ratio on the microstructure 
and mechanical properties, the lower limit of the Cr/Nb ratio was 
established at 9.16 (Nb = 1.3 wt%) to ensure adequate NbC precipitation 
while preventing excessive Laves phase formation. The upper limit was 
set at 11.68 (Cr ≤ 12 wt%, Nb = 1.01 wt%) to reduce Cr depletion without 
compromising thermal conductivity, thereby optimizing the mechanical 
properties of the NiCrMo weld metal. To achieve this, the ratio of Nb to 
Cr was varied by adjusting the composition of the electrode flux coating, 
ensuring that the concentrations of other elements in the NiCrFe-6 
deposited metal remained largely stable. This approach facilitates a 
clearer elucidation of the specific effects of Nb on the microstructure and 
mechanical properties. This study is the first to reveal the quantitative 
relationship between the Cr/Nb ratio and the strength-toughness of 
NiCrMo deposited metals by regulating the competitive precipitation 
behavior of NbC and Laves phases, filling a critical research gap in the 
precise control of second-phase precipitates and the synergistic opti -
mization of cryogenic performance in nickel-based welding materials.
2. Materials and methods
2.1. BP neural network structure selection and optimization
The establishment of training files for neural network performance 
requires a substantial amount of accurate and reliable sample data. The 
BP neural network database in this study is derived from 54 sets of 
experimental results of welding wires with different compositions and 
their mechanical properties, as detailed in the preliminary work titled 
"Study on the Processability and Microstructure Properties of Nickel- 
Based Electrodes for LNG Storage Tanks". These data were processed 
and calculated using MATLAB software. The dataset encompasses 
various combinations of NiCrMo alloy elements along with their corre -
sponding low-temperature impact toughness and tensile performance 
indicators, thereby providing a rich sample set for training the BP neural 
network.
Constructing a model first involves determining the number of pro -
cessing elements (see Fig. 1 ). Each processing element in the input layer 
corresponds to an input variable, while those in the output layer 
correspond to the desired output. The hidden layer, which contains a 
system-determined number of processing elements, plays a crucial role 
in establishing the relationships and interrelationships between the 
processing elements in the input layer and those in the hidden layer, 
ultimately deriving the best estimate of the output. Subsequent stages of 
model construction include defining additional parameters, such as 
selecting the learning rule (the mathematical method employed by the 
program to associate processing elements throughout the model), the 
learning coefficient (the value assigned to both the output layer and 
hidden layer, as well as the entire model), and the transfer mode (which 
converts the weighted sum of processing elements into an output pre -
diction) [11] . In the BP neural network modeling process, three data 
files were utilized: the training file, the testing file, and the sensitivity 
file. The data were normalized to a range of either 0 – 1 or 1 – 1, 
depending on the expected transfer function, which modifies the sum of 
weights to produce the output. The schematic diagram is presented in 
Fig. 1 .
The specific data set includes the following:
Input parameters: mass percentage of each element in the wire: C, Si, 
Mn, P, S, Cr, Ni, Mo, Nb, Fe, W.
Output parameters: low temperature impact toughness (impact 
absorbed energy at 196
◦
C) and tensile strength.
In the process of model construction and training, data preprocessing 
is initially performed. This includes data cleaning to remove outliers and 
incomplete data, ensuring high data quality, as well as normalizing both 
input and output data to a range of [0,1] to facilitate network conver -
gence. Subsequently, the network architecture is designed such that the 
number of neurons in the input layer corresponds to the number of input 
parameters. One or more hidden layers are established, each containing 
an appropriate number of neurons, with the optimal number determined 
through trial and error. The output layer ’ s neuron count matches the 
number of output parameters. We employed a three-layer back -
propagation (BP) network structure of 11 × 8 × 2. Specifically, the 
input layer is designed with 11 neurons, corresponding to the number of 
input parameters, including 54 distinct alloy elements as input features. 
The input-output relationship is articulated in Equation (2 1). 
y
k
= f
(
∑
n 1
j = 0
ω
jk
x
i
 θ
k
)
x
j
= f
(
∑
n 1
j = 0
ω
ij
x
i
 θ
j
)
(2-1) 
Where: ω
ij 
is the weight between the input layer and the hidden layer; θ
j 
is the threshold between the input layer and the hidden layer; ω
jk 
is the 
weight between the hidden layer and the output layer θ
j 
is the threshold 
between the hidden layer and the output layer; and f (x) is the node 
transfer function, which is a Sigmoid function in this network [12 – 14] .
The improved BP algorithm is as follows:
For the P1st sample 
ω
sq
( n
0
+ 1 ) = ω
sq
( n
0
)
∑
p
δ
sq
x
s
+ α Δ ω
sq
( n
0
) (2-2) 
For the output layer: sq = jk 
δ
jk
= ( t
k
 y
k
) y
k
( 1 y
k
)
/
γ
k
(2-3) 
For the hidden layer: sq = ij 
Fig. 1. Schematic diagram of the principle of BP artificial neural network.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
2

## Page 3

δ
ij
=
∑
m 1
k = 0
δ
jk
x
j
( 1 x
j
)
/
γ
j
(2-4) 
The hidden layer consists of eight neurons, a number determined 
through iterative trials and model validation to effectively capture the 
complex relationships between input features and output performance. 
The output layer consists of two neurons, corresponding to the two 
performance metrics: low-temperature impact toughness and tensile 
strength. This structural design enables the network to learn and predict 
the mapping relationship between alloy element content and perfor -
mance metrics [15,16] . The preprocessed dataset is utilized to train the 
BP neural network, employing the gradient descent algorithm to opti -
mize network weights and thresholds, minimize the mean square error 
(MSE), and establish training parameters such as learning rate and 
iteration count [17,18] .To ensure the model ’ s generalization capability, 
the dataset is partitioned into a training set, a validation set, and a test 
set. Model parameters are fine-tuned using the validation set to prevent 
overfitting, while the test set is employed to assess the model ’ s predic -
tive performance.
2.2. Experimental section
The lower limit of the Cr/Nb ratio is set at 9.16 (Nb = 1.3 wt%) to 
ensure sufficient NbC precipitation while preventing excessive forma -
tion of the Laves phase. The upper limit is set at 11.68 (Cr ≤ 12 wt%, Nb 
= 1.01 wt%) to reduce Cr depletion without compromising thermal 
conductivity, thereby optimizing the mechanical properties of NiCrMo 
weld metal. Additionally, an intermediate Cr/Nb ratio of 9.92 was 
selected to validate the consistent trend of mechanical properties with 
varying Cr/Nb ratios.Within this range, three specific electrodes with 
Cr/Nb content, labeled as CN1, CN2, and CN3, are utilized due to their 
good welding process stability. All electrodes utilize pure nickel as the 
core material, and the proportions of all elements conform to the AWS 
A5.11/a 5.11 M-2018 ENiCrMo-6 standard.
In this experiment, the Nb content was kept within the range of 
1.0 wt% to 1.5 wt%, while the Cr content was set between 11.0 wt% and 
13.0 wt%. To accurately assess the impact of Nb content on the prop -
erties of ENiCrMo-6, the concentrations of other elements, including Cr, 
Fe, Mo, and W, in the nickel-based alloy weld metal were kept consis -
tent. Table 1 presents the chemical compositions of the three weld 
metals, which exhibit Cr/Nb ratios of 11.68, 9.92, and 9.16 wt%, 
respectively.
The base material used in the experiment consisted of a 9 % nickel 
steel plate with dimensions of 400 mm × 200 mm × 20 mm. The V- 
groove angle of the welded joint was set at 30
◦
, with a root gap of 4 mm. 
Welding was conducted in the vertical position utilizing a Fronius Tps- 
5000 welding machine for manual arc welding. The welding parame -
ters were optimized to a current of 93 – 95 A, voltage of 23 – 24 V, speed 
of 8.5 – 9 cm/min, heat input of 15 – 16 kJ/cm, and interpass temperature 
maintained below 100 
◦
C. A total of 35 – 40 weld passes were executed. 
Following the welding process, X-ray inspection was performed to verify 
the absence of defects such as pores and cracks in the deposited metal.
For microstructural analysis, weld deposit samples were prepared 
using standard metallographic polishing techniques and subsequently 
etched with a 10 % chromic acid solution. The instruments used for 
microstructure analysis included an optical microscope (OM, Olympus 
GX51), scanning electron microscopes (SEM, JSM-IT800 and Quanta 
650 FEG), an energy dispersive spectrometer (EDS, Oxford X-Max50), 
and an electron probe microanalyzer (EPMA, JXA-iHP200F). The impact 
fracture morphology was examined using SEM, and the area fraction and 
size of precipitates were quantified using Image Pro Plus software.
In accordance with the AWS B4.0 – 2016 standard, low-temperature 
impact specimens featuring a V-notch at the center were extracted 
from the deposited metal and subsequently tested at 196
◦
C utilizing a 
Charpy pendulum impact tester. Transverse tensile specimens were 
sourced from the welded joint of a 20 mm thick plate and tested at room 
temperature using a WE-300E tensile testing machine. Hardness testing 
was conducted employing a VH-5 Vickers semi-automatic hardness 
tester, applying a load of 1 kg and maintaining a dwell time of 
10 seconds. The assembly diagram is depicted in Fig. 2 .
3. Results
3.1. BP neural network calculation results
70 % of the data in the dataset is used as training samples, while 
30 % is used as output samples, and a random seed is set to ensure 
consistent results in each calculation. During the BP neural network 
computation process, the number of iteration steps is limited to fewer 
than 50. The comparison between the actual and predicted values of 
low-temperature impact toughness and tensile strength is presented in 
Fig. 3 and Table 2 , respectively. The error between the actual and pre -
dicted values is less than 10 %, indicating a close alignment between the 
predicted data and the actual values.
The sensitivity of elements to low-temperature impact toughness, 
calculated by the BP neural network, is shown in Fig. 4 . The sensitivity of 
the Cr/Nb ratio to the low-temperature impact toughness of ENiCrMo-6 
weld metal (0.021) ranks just below that of the matrix elements Ni and 
Mn. While the addition of Mn can enhance the toughness of the matrix 
and refine the Nb-rich phase, increasing the manganese content simul -
taneously reduces the size of the Nb-rich phase and increases the size of 
the Mn-rich phase. Excessive precipitation of the Mn-rich phase at grain 
boundaries may contribute to crack formation [19,20] . Therefore, it is 
crucial to consider the influence of the Cr/Nb ratio on mechanical 
properties.
Fig. 5 illustrates the trends in low-temperature impact toughness of 
Table 1 
Chemical composition of the deposited metals (wt%).
NO. C Si Mn Cr Ni Mo Nb Fe W Cr/Ni
CN1 0.04 0.31 3.09 11.8 71.26 6.1 1.01 4.65 1.23 11.68
CN2 0.051 0.4 3.24 12.7 68.24 6.51 1.28 6.13 1.31 9.92
CN3 0.052 0.52 2.95 11.91 70.15 5.98 1.3 5.85 1.24 9.16
Base metal 0.048 0.016 0.28 0.72 9.2 0.064 0.016 0.0031 0.002 9.2
Fig. 2. Weld assembly and sampling of the deposited metal.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
3

## Page 4

NiCrMo alloys with varying element content, as calculated by the BP 
artificial neural network. Within the dataset range, the elements Mn, Cr, 
and Ni exhibit a positive correlation with the low-temperature impact 
toughness of the deposited metal, while C, Si, P, S, Mo, Nb, and W ele -
ments show a negative correlation. For the Fe element, the low- 
temperature toughness initially decreases and then increases with ris -
ing element content, reaching its minimum at 6.86 %. The Cr/Nb ratio, 
which is the focus of this study, ranges from 7.76 to 12.00. Within this 
range, the low-temperature impact toughness decreases from 72.13 J/ 
cm
2 
to 51.39 J/cm
2
, demonstrating an overall declining trend that ap -
proximates a proportional straight line. It is predicted that as the Cr/Nb 
ratio increases, the low-temperature impact toughness will decrease 
proportionally at a rate of approximately 4.89, leading to a significant 
reduction in impact toughness from 72.13 J/cm
2 
to 51.39 J/cm
2
.
The reduction in low-temperature impact toughness is primarily 
attributed to the combined effects of three factors. Firstly, the increase in 
the amount of brittle phases is evidenced by the volume fraction of Nb- 
rich phases (NbC + Laves) rising from 1.86 % to 2.31 %, along with an 
enhancement in their continuity ( Fig. 7 ), which significantly reduces the 
material ’ s impact resistance. Secondly, an analysis of crack propagation 
paths indicates that impact fractures primarily propagate along the grain 
boundary Nb-rich phases ( Fig. 12 ). These hard and brittle phases are 
more susceptible to initiating microcracks and facilitating their rapid 
propagation in the low-temperature environment of 196
◦
C. Lastly, 
EPMA results reveal a noticeable segregation of Nb elements in the 
interdendritic regions ( Fig. 9 ). This local uneven distribution of ele -
ments contributes to an intensification of microstructural in -
homogeneity, thereby triggering a significant stress concentration 
effect. Collectively, these three factors interact synergistically, leading 
to a substantial decrease in the material ’ s impact toughness [21] .
Fig. 6 illustrates the variation trend of tensile strength in NiCrMo 
alloy as a function of element content, as calculated by the BP artificial 
Fig. 3. True versus predicted values: (a) low temperature impact work (b) tensile strength.
Table 2 
Comparison of actual value with the predicted value.
NO. 1 2 3 4 5 6 7 8 9 10
Cryogenic impact toughness (J/cm
2
) Predicted value 75 66 54 57 72 48 69 52 80 72
Actual value 62 57 59 56 74 41 72 49 73 66
Tensile strength (MPa) Predicted value 689 685 669 698 650 755 718 560 746 697
Actual value 680 673 665 690 668 721 716 554 745 690
Fig. 4. Sensitivities of elements related to mechanical properties ： (a) Low temperature impact work (b) Tensile strength.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
4

## Page 5

Fig. 5. Effect of elements on low temperature impact toughness ： (a)The influence of C on toughness;(b)The influence of Si on toughness;(c)The influence of Mn on 
toughness;(d)The influence of P on toughness;(e)The influence of S on toughness;(f)The influence of Cr on toughness;(g)The influence of Ni on toughness;(h)The 
influence of Mo on toughness;(i)The influence of Nb on toughness;(j)The influence of Fe on toughness;(k)The influence of W on toughness;(a)The influence of Cr/Nb 
on toughness.
Fig. 6. Effect of elements on tensile strength ： (a)The influence of C on tensile strength;(b)The influence of Si on tensile strength;(c)The influence of Mn on tensile 
strength;(d)The influence of P on tensile strength;(e)The influence of S on tensile strength;(f)The influence of Cr on tensile strength;(g)The influence of Ni on tensile 
strength(h)The influence of Mo on tensile strength;(i)The influence of Nb on tensile strength;(j)The influence of Fe on tensile strength;(k)The influence of W on tensile 
strength;(a)The influence of Cr/Nb on tensile strength.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
5

## Page 6

neural network. Within the dataset range, the tensile strength initially 
decreases to a minimum before increasing with higher contents of C, Si, 
S, and Fe. The elements Mn and P exhibit a positive correlation with the 
low-temperature impact toughness of the deposited metal within the 
dataset range. The tensile strength remains approximately at 677 MPa 
with Cr content ranging from 10.89 % to 12.00 %, showing no signifi -
cant change. From 12.00 % to 13.23 %, the tensile strength increases 
from 677 MPa to 690 MPa. With Nb content ranging from 1.02 % to 
1.33 %, the tensile strength remains around 680 MPa, also showing no 
significant change. From 1.33 % to 1.50 %, the tensile strength increases 
from 680 MPa to 682 MPa. The tensile strength initially increases and 
then decreases within the Cr/Nb ratio range of 7.76 – 12.00, with the 
minimum value corresponding to a tensile strength of 679 MPa when 
the Cr/Nb ratio is 10.43.
The phenomenon of increased NbC phase while maintaining stable 
tensile strength can be attributed to the interplay between strengthening 
and weakening mechanisms. On one hand, NbC, as a hard phase, can pin 
grain boundaries — especially in the composite structure of the γ phase 
and NbC — thereby hindering dislocation movement through the Oro -
wan mechanism and providing significant strengthening effects [22] . On 
the other hand, excessive continuous precipitation of the Laves phase 
(Ni3Nb) at grain boundaries ( Fig. 8 ) can weaken interfacial bonding 
strength, while the coarsening of NbC particles (with average sizes 
increasing from 1.71 μ m to 3.53 μ m) can diminish their precipitation 
strengthening effects. The mutual cancellation of these two mechanisms 
results in the tensile strength remaining relatively stable, despite the 
increase in material hardness due to the higher NbC content ( Fig. 11 ).
3.2. Experiments on cladding metals
Fig. 7 presents metallographic structure photographs of the depos -
ited metal from three covered electrodes with decreasing Cr/Nb ratios. It 
is evident that the weld metal of the self-developed ENiCrMo-6 exhibits 
good fusion and is free from welding defects such as inclusions, micro -
cracks, and porosity, while maintaining a roughly similar microstruc -
ture. Under electron microscopy, the microstructure of the three groups 
Fig. 7. Microstructure under SEM: (a) and (b) CN1; (c) and (d) CN2; (e) and (f) CN3.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
6

## Page 7

of deposited metals consists of a golden-black austenitic matrix and 
white precipitates, displaying a distinct columnar crystal morphology 
with generally large grain sizes. The austenitic FCC structure reveals a 
dendritic morphology and demonstrates clear orientation selectivity. As 
the Cr/Nb ratio decreases from 11.68 (CN1) to 9.16 (CN3), the grain 
morphology remains unchanged despite variations in Cr and Nb con -
centrations, and the precipitates tend to aggregate more in the inter -
dendritic regions. However, with the decrease in the Cr/Nb ratio, the 
number of precipitated phases significantly increases, the dendritic arms 
become more developed, and the precipitated phases at the grain 
boundaries exhibit greater continuity.
To investigate the effect of the Cr/Nb ratio on the size and quantity of 
precipitates in the deposited metal, each sample was scanned 10 times 
using scanning electron microscopy (SEM) at a magnification of 5000x. 
The obtained SEM images were processed using Image-Pro Plus soft -
ware, from which the volume fraction and average size of the pre -
cipitates in each deposited metal were determined, as shown in Fig. 8 . As 
the Cr/Nb ratio decreased from 11.68 to 9.12, the average sizes of the 
precipitates were measured at 1.71 μ m (CN1), 2.49 μ m (CN2), and 3.53 
μ m (CN3), with corresponding volume fractions of 1.86 % (CN1), 
2.14 % (CN2), and 2.31 % (CN3). It is evident that with the decrease in 
the Cr/Nb ratio in the deposited metal, both the average size and the 
volume fraction of the precipitates significantly increase.
Through EPMA (Electron Probe X-ray Micro-Analyzer) analysis of 
the dendritic and interdendritic regions of austenite, as illustrated in 
Fig. 9 , significant elemental segregation is observed in the interdendritic 
regions. The matrix element, Ni, is predominantly distributed within the 
grains, while the concentrations of Si, Mo, Mn, and Nb are markedly 
higher in the interdendritic regions compared to the interior of the 
dendrites. Conversely, the concentrations of Ni, Cr, W, and Fe are 
notably lower in the interdendritic regions than within the dendrites. 
This phenomenon is attributed to the differing diffusion rates of alloying 
elements during the solidification process. Circular precipitates are 
distributed within the grains, with O content exceeding 50 %, and they 
also contain elevated levels of Si, Al, and Mn. The intergranular pre -
cipitates exhibit higher levels of Nb and C. From the EPMA electron 
probe analysis results, it can be inferred that the round precipitates 
within the grain boundaries are oxides of Si, Al, and Mn, while the 
irregular precipitates formed at the grain boundaries are NbC. 
Furthermore, comparison across multiple EPMA fields reveals that as the 
Cr/Nb ratio decreases, the precipitation of M23C6 significantly di -
minishes. This reduction is attributed to the increase in Nb elements 
replacing Cr to form NbC, which mitigates the depletion of Cr and en -
hances the corrosion resistance of the deposited metal. The decrease in 
M23C6 also positively influences the mechanical properties of the 
deposited metal [23,24] .
Due to the application of welded components in LNG storage tanks, 
Charpy impact tests were conducted on V-notch impact specimens of 
three types of weld metals at a low temperature of 196
◦
C. Each type of 
weld metal was tested three times, and the average values were ob -
tained. Tensile tests were performed on tensile specimens of the three 
types of weld metals at room temperature, with each type tested twice to 
derive the average values. The results of the low-temperature impact 
and tensile tests are presented in Fig. 11 . CN1 (Cr/Nb = 11.68) exhibited 
the best low-temperature impact toughness, with an average value of 
71 J/cm
2
from three tests and an average tensile strength of 688 MPa 
from two tests. CN2 (Cr/Nb = 9.92) had an average low-temperature 
impact value of 65 J/cm
2 
from three tests and an average tensile 
strength of 670 MPa from two tests. The average value of the three low- 
temperature impact test results for CN3 (Cr/Nb = 9.16) is 56 J/cm
2
, and 
the average value of the two tensile test results is 686 MPa ( Fig. 10 ). It 
can be observed that there is a clear relationship between low- 
temperature impact toughness and strength with respect to Nb con -
tent; namely, as the content decreases, the low-temperature impact 
Fig. 8. Cr/Nb effect on the size and number of precipitated phases ： (a) CN1; (b) CN2; (c) CN3; (d) Grain size changes with Cr/Nb.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
7

## Page 8

toughness of the weld metal gradually diminishes, while the tensile 
strength remains relatively stable. This trend aligns closely with the 
predictions made by the artificial neural network for low-temperature 
impact toughness and tensile strength. The tensile strength and elon -
gation follow the order CN1 > CN3 > CN2, while the reduction of area 
follows the order CN3 > CN1 > CN2.
4. Discussion
4.1. Influence of Cr/Nb on microstructure and mechanical properties of 
cladding metals
Since the three deposited metals were prepared using the same 
welding process and parameters, the microstructure at the center of the 
butt weld is mainly determined by the chemical composition. Observing 
the data in Table 1 , it is evident that the main alloying elements 
(excluding Cr and Nb) and impurity contents remain relatively constant. 
Fig. 9. EPMA images under individual elemental markets.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
8

## Page 9

Therefore, the notable differences in the dendritic morphology of the 
three deposited metals can be attributed to variations in the Cr/Nb ratio.
In the weld metal with a matrix composed of approximately 70 % Ni, 
the microstructure is predominantly austenite, characterized by sub -
grain boundaries and secondary subgrain boundaries. Fig. 8 illustrates 
that the microstructure of the weld metal displays a typical dendritic 
structure. In the electron probe microanalysis presented in Fig. 10 , sig -
nificant elemental segregation is observed at the grain boundaries, with 
Si, Mo, Mn, and Nb tending to segregate towards the interdendritic re -
gions, while Ni, Cr, W, and Fe are mainly distributed inside the grains. As 
the Cr/Nb ratio decreases, the harder NbC and detrimental Laves phases 
are more likely to nucleate in the interdendritic regions, resulting in a 
decrease in low-temperature impact toughness and an increase in the 
hardness of the weld metal [25] .
In the preparation process of ENiCrFe-6 weld metal, although Ti and 
Al are not included in its standard composition (see Table 1 ), these el -
ements are introduced through the flux coating used during the welding 
process. Ti and Al are primarily added to the flux as deoxidizers to 
eliminate oxygen from the molten metal. During the welding operation, 
most of the Ti and Al deoxidizers react with oxygen, and the resulting 
oxides, along with silicon (Si), subsequently enter the slag. Huangwang 
et al. [26] found that in nickel-based alloys, these tiny oxide particles 
serve as the core for NbC formation during solidification. Furthermore, 
moderate amounts of Ti and Al contribute positively by reducing the 
porosity of the cladding metal and enhancing its resistance to thermal 
cracking. The formation and distribution of these oxides significantly 
impact the microstructure and properties of the deposited metal. They 
not only affect the mechanical properties but also influence corrosion 
resistance and heat resistance. Therefore, controlling and optimizing 
these oxides are crucial steps in enhancing the quality of the deposited 
metal.
Zhengxin Qi et al. [20] found that the solidification temperature 
range ( Δ T = T1 - Ts, where Tl is the liquid-phase line temperature and 
Ts is the solid-phase line temperature) of nickel-based alloys increases 
with an increase in Nb content. This increase results in a slower 
solid-state phase transition, providing more time and opportunity for 
nucleation, and leading to a slower growth rate that produces smaller 
grains. Conversely, in the fully austenitic structure of nickel-based al -
loys, the NbC phase, which is distributed along the grain boundaries, 
generates a drag force that impedes the movement of these boundaries. 
This phenomenon effectively ’ nails ’ the alloy grain boundaries, inhib -
iting the growth of austenitic grains and thereby contributing to grain 
refinement and strengthening of the weld metal.
As the Cr/Nb ratio decreases, the quantity and size of harmful pre -
cipitates, such as NbC and the Laves phase, significantly increase (as 
illustrated in Fig. 8 ). The solidification point of NbC (1325
◦
C) is higher 
than that of the Laves phase (1266
◦
C). During the cooling process, NbC 
nucleates first and primarily grows in the form of a composite structure 
of the γ phase and NbC. As the solidification process continues, the 
segregation of Nb elements to the interdendritic regions resulting in the 
formation of NbC and Laves phases, both of which are significantly 
harder than the austenitic matrix [27] .
The Vickers hardness test results for the three types of welded joints 
are presented in Fig. 11 . As the Cr/Nb ratio decreases, the Vickers 
hardness at the center of the deposited metal increases from 249.3 to 
313.7, while the Vickers hardness at the edge of the deposited metal 
rises from 210.9 to 250.3. This hardness distribution is mainly due to the 
hardening effect caused by the heat-affected zone during multilayer 
multi-pass welding.This hardness distribution can be attributed to the 
hardening effect in the heat-affected zone. During the multi-layer and 
multi-pass welding process, the heat-affected zone experiences thermal 
cycling and rapid cooling, leading to martensitic transformation and the 
formation of a significant amount of hardened martensite. The base 
metal primarily consists of lath martensite and inter-lath retained 
austenite, which also exhibits a certain hardening trend during the 
welding process. The deposited metal zone is mainly composed of a fully 
austenitic structure, resulting in the lowest hardness [28,29] . In contrast 
to austenite with higher Ni content, the Nb-rich precipitates exhibit 
higher hardness [30,31] . As the Cr/Nb ratio decreased from 11.68 to 
9.16, the volume fraction of the harder precipitates, particularly NbC 
Fig. 10. Effect of Cr/Nb on tensile strength and low temperature impact toughness ： Cryogenic impact toughness and tensile strength; (b) Tensile test curve.
Fig. 11. Effect of Cr/Nb on hardness.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
9

## Page 10

and Laves phases, increased, resulting in a gradual rise in the hardness of 
the deposited metal. The locations and contents of these precipitates are 
detailed in Table 3 .
The impact fracture morphologies of the three types of deposited 
metals, as observed under scanning electron microscopy (SEM), are 
illustrated in Fig. 12 . At low magnification, numerous dimples are pre -
sent on all three fracture surfaces, indicating a typical ductile fracture. 
At high magnification, precipitates within the dimples can be observed 
and are identified as Nb-rich phases through energy dispersive spec -
troscopy (EDS) analysis. These Nb-rich phases, which exhibit greater 
hardness than the matrix, consist of NbC and a small amount of Laves 
phase. They display brittleness and fragility during low-temperature 
impact tests. Upon impact, these phases absorb energy through their 
fragmentation, contributing to the brittleness of the weld metal and 
consequently reducing its toughness.
As the Cr/Nb ratio decreased from 11.68 to 9.16, both the average 
size and volume fraction of the Nb-rich phase increased, accompanied 
by a rise in the content of Ni3Nb and NbC. In the strengthening exper -
iment conducted by DuPont, which involved the addition of Nb elements 
to nickel-based alloys, it was observed that the primary strengthening 
mechanism in these alloys was attributed to the presence of micron- 
sized γ’’ phase (Ni3Nb), characterized by a high yield strength of 
approximately 1300 MPa [32 – 34] . The significant lattice mismatch 
between the austenitic γ phase and the γ’’ phase leads to a pronounced 
coherency stress strengthening effect. An increase in the content of the 
γ’’ phase (Ni3Nb) results in enhanced strength of the deposited metal.
As the Cr/Nb ratio decreases, the Nb-rich phase distributed at the 
grain boundaries transitions from discontinuous precipitation to 
continuous precipitation. Additionally, the NbC within this phase also 
transforms into continuous precipitation at the grain boundaries, 
generating a dragging force that hinders the movement of the grain 
boundaries. This phenomenon pins the grain boundaries of the alloy, 
suppresses the growth of austenite grains, and leads to the refinement of 
alloy grains, thereby strengthening the deposited metal [5,35 – 37] . The 
fracture path of the impact specimens tends to propagate along the 
Nb-rich phase, resulting in a decrease in low-temperature impact energy 
from 80 J/cm
2
to 64 J/cm
2
, while the tensile strength remains largely 
unchanged (as shown in Fig. 11 ). By comparing the experimental data 
with the values predicted by the artificial neural network, it is observed 
that both the low-temperature impact energy and tensile strength values 
and trends exhibit a high degree of agreement with the calculated re -
sults. This provides valuable data guidance for the subsequent design of 
NiCrMo series welding electrode compositions, enabling more accurate 
estimations of the mechanical properties of metals based on their 
elemental composition.
5. Conclusions
Conclusion 1: The developed 11 × 8 × 2 structured BP neural 
network accurately predicted of composition-property relationships, 
quantitatively characterizing the nonlinear relationship between the Cr/ 
Nb ratio and mechanical properties. As the Cr/Nb ratio increased, the 
Table 3 
Location and element content of precipitated phase (wt%).
Precipitated phase location The type of precipitated phase C O Nb Mo Ni Cr Fe Mn Al Si W
Matrix phase Austenite - - 1.06 6.84 73.30 11.63 3.19 3.14 0.21 0.35 0.14
Over the grain boundary Nb-rich phase 19.16 8.24 23.76 4.25 32.15 6.78 2.48 2.02 0.34 0.47 -
I ntragranular Oxide phase 9.32 32.12 0.20 3.22 29.87 10.89 3.57 5.31 4.80 0.39 0.19
I ntragranular Laves phase 6.85 2.67 23.17 6.82 38.08 8.17 6.82 3.98 0.68 2.68 -
Fig. 12. Fracture morphology of low-temperature impact pattern. (a) CN1; (b) CN2; (c) CN3;(d)and(e) Precipitated phase point seconds.
G. Liu et al. Materials Today Communications 46 (2025) 112460 
10

## Page 11

tensile strength initially decreased before subsequently increasing, with 
a predicted minimum tensile strength of 679 MPa at Cr/Nb = 10.43. In 
contrast, the impact toughness decreased linearly at a rate of 4.89.
Conclusion 2: This study elucidated the microscopic mechanism by 
which the Cr/Nb ratio influences the strength and toughness of NiCrMo 
weld metal through the regulation of competitive precipitation behavior 
between NbC and Laves phases. When the Cr/Nb ratio decreased from 
11.68 to 9.16, the interdendritic segregation of Nb elements resulted in 
an increase in the volume fraction of precipitated phases and coarsening 
of their average size. The continuously distributed Laves phase (Ni3Nb) 
formed brittle channels, leading to a reduction in low-temperature 
impact energy, while the Orowan strengthening effect of NbC main -
tained the tensile strength at a stable level of 680 ± 11 MPa.
Conclusion 3: As the Cr/Nb ratio decreased, the Nb-rich phase in the 
NiCrMo alloy weld metal transitioned from discontinuous to continuous 
precipitation, resulting in an increase in the hardness of the weld metal. 
The increased content of NbC endowed the weld metal with higher 
strength, while the presence of the Laves phase negatively impacted the 
low-temperature impact toughness of the weld metal. Therefore, 
rational control of the Cr/Nb ratio is significantly important for 
improving the mechanical properties of NiCrMo alloy deposited metal.
CRediT authorship contribution statement
GuangYu Liu Guangyu: Writing – original draft, Visualization, 
Software, Investigation. Liu Guangyu: Writing – original draft, Visual -
ization, Software, Investigation. Qi Yanchang: Resources, Formal 
analysis, Data curation. Ma Chengyong: Writing – review & editing, 
Validation, Funding acquisition, Conceptualization. Li Yuntao: Super -
vision, Funding acquisition, Formal analysis, Conceptualization.
Declaration of Competing Interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Data Availability
Data will be made available on request.
References
[1] A. Kern, U. Schriever, J. Stumpfe, Development of 9% nickel steel for LNG 
applications, Steel Res. Int. 78 (2007) 189 – 194, https://doi.org/10.1002/ 
srin.200705879 .
[2] H. Naffakh, M. Shamanian, F. Ashrafizadeh, Dissimilar welding of AISI 310 
austenitic stainless steel to nickel-based alloy Inconel 657, n.d..
[3] S.L. Jeng, H.T. Lee, W.P. Rehbach, T.Y. Kuo, T.E. Weirich, J.P. Mayer, Effects of Nb 
on the microstructure and corrosive property in the Alloy 690 – SUS 304L 
weldment, Mater. Sci. Eng.: A 397 (2005) 229 – 238, https://doi.org/10.1016/j. 
msea.2005.02.042 .
[4] D. Kong, C. Dong, X. Ni, L. Zhang, C. Man, J. Yao, Y. Ji, Y. Ying, K. Xiao, X. Cheng, 
X. Li, High-throughput fabrication of nickel-based alloys with different Nb contents 
via a dual-feed additive manufacturing system: effect of Nb content on 
microstructural and mechanical properties, J. Alloy. Compd. 785 (2019) 826 – 837, 
https://doi.org/10.1016/j.jallcom.2019.01.263 .
[5] T. Xu, Y. Shi, Z. Jiang, L. Wu, Y. Ma, Z. Wang, Improvement of cryogenic toughness 
for 9% Ni steel keyhole TIG butt-welded joints with a Ni interlayer, Mater. Sci. Eng. 
A 835 (2022) 142661 .
[6] J. Jones, D. MacKay, Neural network modelling of the mechanical properties of 
nickel base superalloys, in 1996, pp. 417 – 424.
[7] H. Wen, S. Wang, J. Jin, X. Wang, X. Tang, Y. Zhang, L. Deng, P. Gong, D. Li, 
B. Ning, Deep learning-based modeling of the strain rate-dependent 
thermomechanical processing response for a novel HIPed P/M nickel-based 
superalloy, J. Mater. Process. Technol. 324 (2024) 118226 .
[8] Y. Zhu, Y. Cao, Q. He, J. Zhang, R. Luo, H. Di, G. Huang, Q. Liu, Three-dimensional 
hot processing map of a nickel-based superalloy (Alloy 925) established by 
modified artificial neural network model, Intermetallics 141 (2022) 107433 .
[9] K. Abd El-Aziz, D. Saber, A. Megahed, Investigation and prediction of abrasive 
wear rate of heat-treated HCCIs with different Cr/C ratios using artificial neural 
networks, Int. J. Met. 15 (2021) 1149 – 1163 .
[10] X. Yang, J. Zhu, Z. Nong, H. Dong, Z. Lai, L. Ying, F. Liu, Prediction of mechanical 
properties of A357 alloy using artificial neural network, Trans. Nonferrous Met. 
Soc. China 23 (2013) 788 – 795 .
[11] S. Saha, S. Kumar, V.K. Mahakur, S. Sharma, A. Saha, Development and machine 
learning based prediction of carbon/hemp/ramie sandwich composite as 
sustainable and ecofriendly solution for automobile application, Mater. Today 
Commun. 41 (2024) 110817, https://doi.org/10.1016/j.mtcomm.2024.110817 .
[12] J. Li, J. Cheng, J. Shi, F. Huang, Brief Introduction of Back Propagation (BP) Neural 
Network Algorithm and Its Improvement, in: Springer, 2012, pp. 553 – 558 .
[13] Institute of Electrical and Electronics Engineers, 2010 5th IEEE Conference on 
Industrial Electronics and Applications, IEEE, 2010.
[14] C. Li, K. Xu, M. Lou, L. Wang, K. Chang, Machine learning-enabled prediction of 
high-temperature oxidation resistance for Ni-based alloys, Corros. Sci. 234 (2024) 
112152 .
[15] S.S. Haudet, M.A. Rodriguez, R.M. Carranza, Determining the effect of the main 
alloying elements on localized corrosion in nickel alloys using artificial neural 
networks, Procedia Mater. Sci. 8 (2015) 21 – 28 .
[16] A. Sankar, Exploring the mechanical performance of additively manufactured 
nickel-based Alloy 718 under high strain rate and high temperature conditions, 
(2024).
[17] H. Weng, H. Yuan, Quantitative representation of directional microstructures of 
single-crystal superalloys in cyclic crystal plasticity based on neural networks, Int. 
J. Plast. 170 (2023) 103757 .
[18] W. Chunhui, S. Zhihui, Z. Jiaqing, S. Chaoyang, W. Wenrui, Z. Jiaming, Creep 
deformation constitutive model of BSTMUF601 superalloy using BP neural 
network method, Rare Met. Mater. Eng. 49 (2020) .
[19] G. Ilevbare, G. Burstein, The role of alloyed molybdenum in the inhibition of 
pitting corrosion in stainless steels, Corros. Sci. 43 (2001) 485 – 513 .
[20] Z. Qi, Y. Li, Y. Qi, J. Fan, C. Ma, Z. Tian, Effect of Nb content variations on the 
microstructure and mechanical properties of NiCrMo welded joints, Mater. 
Charact. 212 (2024) 113974, https://doi.org/10.1016/j.matchar.2024.113974 .
[21] Effect of alloying elements and temperature on impact toughness of cryogenic 
austenitic steels - ScienceDirect, n.d.. 〈 https://www.sciencedirect.com/science/ 
article/abs/pii/S0921509300017974 〉 (Accessed April 1, 2025).
[22] R. Scattergood, D. Bacon, The Orowan mechanism in anisotropic crystals, Philos. 
Mag. 31 (1975) 179 – 198 .
[23] A. Evangeline, P. Sathiya, B. Arivazhagan, Laves phase formation and segregation 
of Nb in Ni – Cr – Mo superalloy over 316l by hot wire (HW) TIG cladding process, 
Arab. J. Sci. Eng. 45 (2020) 9685 – 9698 .
[24] K. Mageshkumar, N. Arivazhagan, P. Kuppan, Studies on the effect of filler wires on 
micro level segregation of alloying elements in the alloy 617 weld fusion zone, 
Mater. Res. Express 6 (2019) 116579, https://doi.org/10.1088/2053-1591/ 
ab4946 .
[25] Z. Qi, Y. Li, Y. Qi, Z. Tian, C. Ma, Effect of Mo/Nb ratio variations on the 
microstructure and cryogenic impact toughness of NiCrMo deposited metals, 
J. Mater. Res. Technol. 29 (2024) 5656 – 5666 .
[26] H. Wang, G. He, Effects of Nb/Cr on the cryogenic impact toughness of the 
deposited metal of ENiCrFe-9, Mater. Sci. Eng.: A 672 (2016) 15 – 22 .
[27] J. Kangazian, N. Sayyar, M. Shamanian, Influence of microstructural features on 
the mechanical behavior of Incoloy 825 welds, Metallogr. Microstruct. Anal. 6 
(2017) 190 – 199 .
[28] S. Liang, X. Wang, H.S. Zurob, NbC precipitation during multi-pass deformation of 
a nickel-based model alloy: Experiments and modelling, Mater. Sci. Eng. A 772 
(2020) 138748 .
[29] T. Matsunaga, H. Hongo, M. Tabuchi, Interfacial failure in dissimilar weld joint of 
high boron 9% chromium steel and nickel-based alloy under high-temperature 
creep condition, Mater. Sci. Eng.: A 695 (2017) 302 – 308 .
[30] P. Nash, A. Nash, The Nb Ni (niobium-nickel) system, Bull. Alloy Ph. Diagr. 7 
(1986) 124 – 130 .
[31] G. Smith, S. Patel, The role of niobium in wrought precipitation-hardened nickel- 
base alloys, Superalloys 718 (2005) 135 – 154 .
[32] Y. Liu, H. Zhang, Q. Guo, X. Zhou, Z. Ma, Y. Huang, H. Li, Microstructure evolution 
of Inconel 718 superalloy during hot working and its recent development tendency, 
Acta Met. Sin. 54 (2018) 1653 – 1664 .
[33] J. Siefert, J. Shingledecker, J. DuPont, S. David, Weldability and weld performance 
of candidate nickel based superalloys for advanced ultrasupercritical fossil power 
plants Part II: weldability and cross-weld creep performance, Sci. Technol. Weld. 
Join. 21 (2016) 397 – 427 .
[34] S. Huang, R. Liu, L. Li, O. Van der Biest, J. Vleugels, NbC as grain growth inhibitor 
and carbide in WC – Co hardmetals, Int. J. Refract. Met. Hard Mater. 26 (2008) 
389 – 395 .
[35] M.G.D.V. Cuppari, S.F. Santos, Physical properties of the NbC carbide, Metals 6 
(2016) 250 .
[36] J. Katagiri, S. Nomoto, M. Kusano, M. Watanabe, Influence of high Reynolds 
number flow inside molten pool on keyhole instability-induced pore formation 
process in laser powder bed fusion, Mater. Today Commun. (2025) 111756 .
[37] E. Asghari, R. Hayati, A. Momeni, N. Setoudeh, A. Mohassel, S. Mortezaei, 
Predicting the flow stress of Inconel 617 superalloy using constitutive equation and 
artificial neural network approach, Mater. Today Commun. 43 (2025) 111690, 
https://doi.org/10.1016/j.mtcomm.2025.111690 .
G. Liu et al. Materials Today Communications 46 (2025) 112460 
11
