# Materials Genome Engineering Advances - 2025 - Liu - Intelligent optimized design of novel high‐temperature titanium alloys

<!-- source: D:\总文献\Materials Genome Engineering Advances - 2025 - Liu - Intelligent optimized design of novel high‐temperature titanium alloys.pdf -->
<!-- file_sha256: ae3d1b9a6dfd08267799eb2a2e6be4291b5dd8d0168a118f3d8bacd656d07cb8 -->

## Page 1

Received: 25 December 2024
-
Accepted: 7 March 2025
DOI: 10.1002/mgea.70006
RESEARCH AR TICLE
Intelligent optimized design of novel high-temperatur e titanium
alloys
Lingzhi Liu
1
| Lixian Lian
1
| Xingyue Li
2
| Wu Jiaqi
1
| W ang Hu
2
| Y ing Liu
1
1
College of Materials Science and Engineering,
Sichuan University, Chengdu, China
2
School of Computer Science and Engineering,
University of Electronic Science and T echnology of
China, Chengdu, China
Correspondence
Lixian Lian, College of Materials Science and
Engineering, Sichuan University , No. 24 South
Section 1, Y ihuan Road, Chengdu 610065, China.
Email: scu_lianyi@126.com
Abstract
600°C is regarded as the “thermal barrier” temperature for traditional T i-based
alloys. As the working temperature rises, alloys' creep performance and strength
at high temperatures exhibit a dramatic decrease, which becomes a major obstacle
to the development of high-temperature titanium alloys. In order to break the
thermal barrier temperature, a new design strategy that integrates machine learning
with multiobjective optimization has been employed. A high-precision predictive
model has been established, achieving R
2
values exceeding 0.9, with mean absolute
error (MAE) and root mean square error (RMSE) not exceeding 5 and 1 1,
respectively . By referencing domain knowledge, constraints have been proposed,
leading to the optimization. Additionally , the α
2
phase is utilized as a reinforcement
phase, balancing plasticity while controlling its content range. T itanium alloys that
demonstrate high yield strength (greater than 490 MPa) and extended creep life
(exceeding 25 h), suitable for conditions up to 650°C, have been designed using
multiobjective optimization with constraints. Compared to current typical high-
temperature titanium alloys, these newly developed alloys exhibit superior yield
strength and creep life with similar density and cost. This method provides a
valuable reference for designing advanced high-temperature titanium alloys.
KEYWORDS
high-temperature titanium alloys, machine learning, multiobjective optimization, creep life, α
2
phase
1 | INTRODUCTION
The excellent performance of modern military fighters and
civilian aircraft largely depends on the application of
advanced aero-engines, with the rapid development of these
engines closely linked to the extensive application of high-
temperature titanium alloys. T itanium alloys are character-
ized by their low density , heat resistance, corrosion resistance,
and high specific strength. They are one of the most significant
research directions in the field of aerospace alloys.
[1]
They are
primarily employed in components that demand high-
temperature durability , such as engine blades, disks, and cas-
ings, earning them the designation of “space metal.”
W ith the development of technology and societal prog-
ress, there is an increasing demand for high-performance
materials, particularly new materials capable of with-
standing extreme conditions.
[2]
The latest generation of
aircraft engines, which boasts a high thrust-to-weight ratio
(exceeding 10), operates under severe conditions within their
high-pressure compressor systems, as these components are
situated near the combustion chamber and must endure
exceptionally high temperatures.
[3]
At present, the highest
temperature titanium alloy in use worldwide is the IMI834
titanium alloy , which has a maximum service temperature of
only 600°C.
[4]
Therefore, breaking through the “thermal
barrier”, the development of high-temperature titanium
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original
work is properly cited.
© 2025 The Author(s). Materials Genome Engineering Advances published by W iley-VCH GmbH on behalf of University of Science and T echnology Beijing.
Materials Genome Engineering Advances. 2025;3:e70006. wileyonlinelibrary .com/journal/mgea
-
1 of 12
https://doi.org/10.1002/mgea.70006

## Page 2

alloys with service temperatures of 650°C and above is
particularly important and urgent. W ith increasing service
temperatures, the creep resistance and strength of titanium
alloys decline dramatically . This decline in performance is
insufficient to meet the demands for high-temperature ap-
plications, posing a major obstacle to the development of
titanium alloys.
[5]
If the design and development of high-
temperature titanium alloys completely rely on the tradi-
tional composition design, using the trial-and-error method
of increasing or decreasing the types and contents of ele-
ments, or by the method of field experience only , a larg e
amount of cost and time will be consumed. High-
temperature titanium alloys typically require the synergi stic
eff ect of multiple elements to enhance their comprehensive
performance under elevated temperatures, which also leads
to a huge compositional space, and the complex interactions
between elements also pose substantial challenges for
compositional design.
The emer gence of materials genetic engineering has
promoted the development of materials big data, and the
data-driven combined materials design approach has
become the fourth paradigm in materials research and
development.
[6–8]
Malinov et al.
[9]
established a neural
network model based on 764 titanium alloy data samples,
using composition, heat treatment conditions, and working
temperature as inputs to predict mechanical properties such
as tensile strength, elongation, and elastic modulus as out-
puts. The model's predicted values demonstrated a strong
correlation with experimental results, and it was found that
the amount of sample data was proportional to the prediction
accuracy . Changlu Zhou et al.
[10]
proposed two cross-
materials transfer learning strategies based on data from
Fe-based, Ni-based, and Co-based materials to predict the
creep life of high-temperature titanium alloys. However , the
limited quantity of titanium alloy samples in the training
dataset resulted in some models achieving an R
2
value of
only around 0.79, which is insufficient for ensuring accuracy
and stability . Currently , there are relatively few studies
employing machine learning for high-temperature titanium
alloys, and most focus solely on predicting performance
without addressing the design and optimization of the alloy
composition, which is mainly due to the challenges associ-
ated with data collection. Experimental data regarding the
performance of titanium alloys at elevated temperatures are
scarce, particularly concerning creep behavior above 600°C.
The performance of machine learning models is highly
dependent on the quality and quantity of the dataset,
[1 1]
and
in order to obtain better prediction performance and fully
exploit the optimization-seeking ability of the model, a
larg er dataset is required to train the model. JMatPro is a
powerful software for phase diagram calculations and
property simulations of metallic materials, especially for
multicomponent alloys, which is able to provide accurate
predictions and analyses of material properties. It is widely
used in the materials science and engineering fields.
[12]
Bin
Zhang
[13]
used JMatPro to accurately predict the chemical
composition and precipitation kinetics of the η phase in
high-entropy alloys. Ruochen Sun
[14]
investigated how
elemental content aff ects high-temperature performance in
T i-V-Cr and T i-Al-V alloys by employing thermodynamic
calculations through JMatPro to explore the influences of
elements such as Al, V , and Cr . Y unhe Y u et al.
[15]
used
JMatPro to simulate equilibrium phase structures and
properties resulting from mixtures formed by varying pro-
portions of Norem02 alloy combined with F304 stainless
steel. They compared experimental results with simulated
outcomes, revealing minimal discrepancies that validated
the accuracy of the simulations.
In response to the challenge of limited experimental data
on high-temperature titanium alloys, this study aims to
establish a comprehensive database and develop accurate
machine learning models for performance prediction. Uti-
lizing JMatPro software, we conducted high-throughput data
collection, resulting in 56,134 sets of data that encompass
alloy composition, microstructure, and mechanical proper -
ties. Combined with the multiobjective genetic algorithm
that optimizes and balances high-temperature yield strength
and creep life, high-temperature titanium alloys with
enhanced comprehensive mechanical properties are ob-
tained, which effectively improves the efficiency of the alloy
design and provides a new idea and method for the
composition design of high-temperature titanium alloys.
2 | METHODS
2.1 | Design strategy
The design strategy for high-temperature titanium alloys that
integrates machine learning with multiobjective optimization
of alloy composition is illustrated in Figure 1 . This strategy
can be divided into three main components: database
establishment, machine learning model development, and
multiobjective optimization, followed by performance
comparison. First, a substantial database was created by
using the JMatPro software to conduct a high-throughput
collection of 56,134 sets of data on alloy composition,
microstructure, and mechanical properties at 650°C through
an application programming interface. Subsequently , ma-
chine learning models were developed to assess the yield
strength, creep life, and volume fraction of the α
2
phase ( V
α 2
)
of alloys at 650°C. By leveraging empirical knowledge to
establish constraint conditions and integrating multiobjective
optimization algorithms, tar get alloy compositions that meet
specified requirements were optimized. These optimized
alloy compositions were then compared with existing high-
temperature titanium alloys. This strategy effectively com-
bines machine learning with multiobjective optimization for
alloy composition design. It not only balances two critical
performances of yield strength and creep life but also obtains
alloys with superior comprehensive mechanical properties
while reducing experimental costs and time. Consequently , it
provides a highly efficient and cost-effective method for
composition design.
2 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

2.2 | Database building
The composition and properties of existing high-temperature
titanium alloys, the role of elements, and the range of content
are collected through the literature. Based on the existing
typical high-temperature titanium alloy system T i-Al-Sn-Zr-
Mo-Si, elements T a, Nb, B, and C are added. T a can ef fec-
tively refine the grain structure and significantly enhance the
strength and creep resistance of titanium alloys at elevated
temperatures.
[16]
Nb is a weaker β -stabilizing element, has
similar electronegativity to T i, and has a larg er solidification
in the α phase, which plays a good solid solution strength-
ening role, refines the microstructure, and improves oxida-
tion resistance.
[17–19]
Furthermore, the dif fusion coefficients
of Nb and T a in α -T i are very small, which not only ensures
that the alloy has the best high-temperature creep resistance,
high fatigue strength, and fracture toughness but also
maintains sufficient plasticity and thermal stability .
[20]
A
small amount of B can markedly improve the microstructure
by refining grains, increasing phase boundaries to impede
dislocation movement, thereby enhancing the alloy's creep
resistance and high-temperature strength.
[21]
The addition of
trace amounts of C can ef fectively expand the processing
window of the upper α þ β region in near-α titanium alloys
and reduce the rate of change of the primary α volume
fraction with temperature. Additionally , it improves the ho-
mogeneity of the α precipitation phase, refines the grain, and
improves the plasticity of the alloy .
[22]
The 10 alloying el-
ements above were used as variables to define the compo-
sition space, as shown in T able 1 , and random sampling of
the composition was performed within the defined range.
The phase content, high-temperature strength, and creep life
of the equilibrium state at 650°C for each composition were
calculated using high-throughput methods from the titanium
alloy database of the JMatPro software, and a total of 56,134
sets of data were collected to develop the machine learning
model.
2.3 | Establishment of machine learning
model
The feedforward neural network (FNN) model has powerful
nonlinear mapping and parallel processing capabilities.
[23,24]
It is a network composed of interconnected artificial neurons,
where information flows unidirectionally from input nodes
to hidden layer nodes, and finally to output nodes. This ar -
chitecture enables the FNN to address problems that are not
amenable to conventional statistical methods.
[25,26]
The alloy
compositions listed in T able 1 were used as inputs, whereas
yield strength, creep life at 150 MPa, and the volume frac-
tion of the α
2
phase ( V
α 2
) of the alloy at 650°C were used as
outputs for constructing the FNN machine learning model.
The sample data were divided into a training set, a validation
set, and a test set in a ratio of 7:1.5:1.5. The validation set is
utilized to evaluate the performance of the model at each
epoch during training, assisting in determining whether early
stopping of the model training is necessary to prevent
overfitting. Additionally , an ensemble model comprising 20
base models has been incorporated. During the training of
the ensemble model, a separate test set is established. This
test set will be used to assess the performance of the
ensemble model. The remaining data will be redivided into
training and validation sets for each iteration of base model
training. Each base model under goes training with dif ferent
configurations for its respective training and validation sets,
FIGURE 1 Framework diagram for alloy composition design based on machine learning and multiobjective optimization.
-
3 of 12
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

which aids in enhancing both prediction accuracy and sta-
bility while ensuring robustness. Because of differen ces in
units and distribution ranges of the data, some values may be
significantly larger , whereas others are much smaller . This
disparity can lead to slower conver gence rates for neural
networks and extended training times. The data need to be
normalized and scaled to the same range to improve the
performance and stability of the model.
Determining the optimal number of hidden layers and
neuron nodes in a neural network model is a critical aspect of
its design. Although increasing the number of hidden layers
can improve the model's capabilities, it also raises the
complexity and training difficulty of the model. A suitable
number of nodes can improve the model's mapping and
generalization abilities. However , having too many or too
few nodes can negatively impact network performance. In
order to find the FNN model with optimal performance, we
refer to the empirical formula (Equation ( 1 )) for determining
the number of nodes in the hidden layer .
[27]
n
1
¼
ffiffiffiffiffiffiffiffiffiffiffi ffi
m þ n
p
þ a ð 1 Þ
where n
1
is the number of neurons, m is the number of input
layer cells, n is the number of output layer cells, and a is a
parameter (0 ≤ a ≤ 10). In addition, considering the larg e
number of samples, the quantity of nodes and hidden layers
will be increased appropriately to achieve the best
performance.
The performance of the models was comprehensively
measured using mean absolute error (MAE), root mean
square error (RMSE), and the coefficient of determination
( R
2
), expressed in Equations (2)–(4) , respectively .
M AE ¼
1
n
X
n
i ¼ 1
�
�
� Y
i
− Y
�
i
�
�
� ð 2 Þ
RM S E ¼
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffiffiffiffiffiffiffiffi ffi
1
n
X
n
i ¼ 1
�
Y
i
− Y
�
i
�
2
v
u
u
t
ð 3 Þ
R
2
¼ 1 −
P
n
i ¼ 1
�
Y
i
− Y
�
i
�
2
P
n
i ¼ 1
�
Y
i
− Y
�
2
ð 4 Þ
where Y
i
represents the observed value of the i th sample, Y
�
i
stands for the predicted value of the i th sample, and Y is the
average of the observed value. In addition, n is the number of
data samples. The smaller the MAE and RMSE , the smaller
the model error will be. The R
2
within [0,1] is an evaluating
indicator to represent the proportion of response variation
“explained” by the regressors.
2.4 | Multiobjective optimization strategy
Balancing the optimal values of various properties of ma-
terials to achieve comprehensive performance optimization
has long been a challenge in the field of materials science.
Multiobjective genetic algorithms facilitate global searches,
yielding a set of Pareto optimal solutions for multiobjective
collaborative optimization. The nondominated sorting ge-
netic algorithm II (NSGA-II) is an efficient genetic algo-
rithm in the field of multiobjective optimization. By
incorporating key techniques such as fast nondominated
sorting, crowding distance, and elite-preserving operator , it
significantly enhances the performance of traditional genetic
algorithms when addressing multiobjective optimization
problems.
[28]
This method has found widespread application
across various domains, including materials science, engi-
neering design, economics, and finance. Particularly in sce-
narios that require simultaneous consideration of multiple
objectives, it has become one of the standard tools for
solving multiobjective optimization challenges.
[29,30]
In this
study , the optimization module is NSGA-II, which uses FNN
as the surrogate model. W e referenced existing equivalent
criteria for high-temperature titanium alloy composition
design. The constraints considered include Al equivalent,
Mo equivalent, the coefficient of β stabilization, and the
content of the α
2
phase, with specified ranges established for
these constraints.
In 1970, Rosenberg
[31]
proposed the famous empirical
formula for Al equivalent, defined by the following equation:
Al eq : ¼ % Al þ
% S n
3
þ
% Z r
6
þ
% Ga
2
þ 10 % O ≤ 8 % � 9 %
ð 5 Þ
As long as the Al equivalent is less than 8–9%, the α
2
phase may not appear in the alloy , which establishes a
practical guideline for the composition design of high-
temperature titanium alloys. In the past, the α
2
phase was
usually considered a harmful phase with embrittlement eff ect
on titanium alloys, and the precipitation of α
2
should be
avoided in high-temperature titanium alloys. However , in
recent years, studies have shown that the high-temperature
strength of the α
2
phase is much higher than that of the α
phase, which can also significantly improve the creep
properties of the alloy .
[32,33]
Moreover , the plasticity of
α þ α
2
alloys can be improved by adjusting the addition of
T ABLE 1 Composition space.
Element Al Sn Zr Mo Si Nb T a B C Ti
Content (wt.%) 5.6–8 0–4.8 1.5–1 1 0–5 0.1–0.6 0–3 0–2 0–0.5 0–0.06 Bal.
4 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

specific elements and through heat treatment to control their
volume fraction, precipitate size, and distribution.
[34,35]
For
instance, high-temperature titanium alloys, such as IMI834,
have allowed the precipitation of the α
2
phase while mark-
edly improving creep properties without severely compro-
mising plasticity . This makes it possible to utilize the α
2
phase to strengthen α titanium alloys; thus, breaking through
the limitation on the Al equivalent has gradually become one
of the development directions for the composition design of
high-temperature titanium alloys. In this study , in order to
enhance the strength and creep life of high-temperature ti-
tanium alloys by using the α
2
phase as a reinforcing phase,
the Al equivalent is used as a constraint to expand the range
from 8% to 9.5%.
The Mo equivalent is also a common method for
designing the composition of titanium alloys, which is
closely related to mechanical properties, phase transition
behavior , and deformation mechanism of titanium al-
loys
[36,37]
(shown in Equation ( 6 )). Generally , as the mo-
lybdenum equivalent of the alloy increases, the solid solution
strengthening eff ect of the β phase is gradually enhanced, but
a higher molybdenum equivalent of the alloy will cause an
uneven distribution of the second phase phenomenon.
Therefore, the rational selection of an alloy's molybdenum
equivalent is essential to achieve excellent mechanical
properties. Cai Jianming
[2]
pointed out that as the operating
temperature of titanium alloys increases, the Mo equivalent
tends to decrease. For titanium alloys intended for long-term
use at high temperatures, it is recommended that the mo-
lybdenum equivalent be controlled within the range of
0.5%–1%.
M o eq : ¼
% M o
1
þ
% T a
4
þ
% N b
3 : 3
þ
% W
2
þ
% V
1 : 4
þ
% C r
0 : 6
þ
% N i
0 : 8
þ
% M n
0 : 6
þ
% F e
0 : 5
þ
% C o
0 : 9
ð 6 Þ
Because of the direct relationship between the quantity
and stability of the β phase and the β -stabilizing elements in
titanium alloys, a method for classifying titanium alloys
based on their β -stabilizing coefficient has been pro-
posed.
[38,39]
The coefficient of β stabilization (K
β
)
[40,41]
is
shown in Equation ( 7 ), where c
i
is the concentration of the β -
stabilizing element in the alloy and c
k
is its critical con-
centration. The critical concentrations of the β -stabilizing
elements commonly used are listed in T able 2 .
K
β
¼
C
1
C
k 1
þ
C
2
C
k 2
þ
C
3
C
k 3
þ … þ
C
n
C
k n
ð 7 Þ
According to the coefficient of β stabilization (K
β
), ti-
tanium alloys can be classified into dif ferent types as fol-
lows
[40,42,43]
: α alloys K
β
is 0–0.07, near-α alloys K
β
is 0.07–
0.25, α þ β alloys K
β
is 0.25–1.0, metastable β alloys K
β
is
1.0–2.8, and β alloys K
β
is > 2.8. The α phase is a hexagonal
close-packed structure and has a lower dif fusion rate than the
β phase with a body-centered cubic structure. Therefore,
high-temperature titanium alloys are generally designed with
an α -phase matrix supplemented by a small amount of β
phase, classifying them as near-α alloys. This configuration
retains the advantages of high heat resistance and thermal
stability characteristic of α alloys while also incorporating
the strength and good plasticity associated with α þ β al-
loys.
[44,45]
W ang Y ong et al.
[46]
conducted research on the
T i-650 alloy with varying contents of β -stabilizing elements
and found that the best tensile properties at 650°C were
achieved when the K
β
value was between 0.3 and 0.35.
Consequently , in this study , the coefficient of β stabilization
is taken as a constraint in the range of 0.07–0.35. Consid-
ering that common β -stabilizing elements in high-
temperature titanium alloys include Mo, Nb, and T a, it is
noted that there are similarities between the formulas for
calculating the K
β
coefficient and the Mo equivalent.
Therefore, by integrating these considerations within the
specified range, we established a constrained range for the
Mo equivalent from 0.5 to 3.5.
Furthermore, an excessive amount of the α
2
phase in the
alloy can significantly impair its plasticity , leading to
increased brittleness. In order to consider plasticity , the ef-
fect of the α
2
phase on the properties is further investigated
by systematically increasing its content and categorizing it
into ranges, as shown in T able 3 . The optimization of alloy
composition will be conducted within these six specified
ranges.
As a result, through multiobjective optimization with
constraints, novel high-temperature titanium alloys with
excellent comprehensive mechanical properties at 650°C
have been optimized.
3 | RESUL TS AND DISCUSSION
3.1 | The pr edictive performance of the
FNN models
In the construction of the feedforward neural network (FNN)
model, the number of nodes and the hidden layers are two
critical parameters that significantly affect the model's per -
formance and complexity . Selecting appropriate parameters
not only enhances the predictive capability of the model but
also reduces computational costs and training time. As
illustrated in Figure 2 , Models 1–14 consist of a single
hidden layer with varying numbers of nodes, ranging from 4
to 14, as well as configurations with 16, 32, and 64 nodes.
Models 15–16 feature two hidden layers with node counts of
16 and 8 and 32 and 16, whereas Model 17 incorporates
three hidden layers with node counts of 16, 32, and 16. The
T ABLE 2 Critical concentrations of the stabilizing elements
commonly used.
Element T a Nb W V Cu Mo Co Ni Mn Fe Cr
C
k
(wt.%) 40 33 20 14 13 10 9 8 6 5 4
-
5 of 12
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

FNN model established in this study demonstrates high ac-
curacy in predicting the mechanical properties and micro-
structure of high-temperature titanium alloys. All models
exhibit an R
2
value exceeding 0.9, with mean absolute error
(MAE) and root mean square error (RMSE) values not
surpassing thresholds of 5 and 1 1, respectively . By gradually
increasing the number of nodes and hidden layers in the
FNN framework, the accuracy of the model rises continu-
ously . Considering that Model 15 achieved an R
2
value
exceeding 0.99, with RMSE and MAE values of 3.76 and
1.23, respectively , the predictive performance of this model
has proven to be sufficiently outstanding. Adding more
nodes or hidden layers would increase both the complexity
of the model and the difficulty of training, potentially lead-
ing to overfitting. Therefore, we selected an FNN model with
two hidden layers containing 16 and 8 nodes, respectively .
The model was built using the composition as input and the
yield strength at 650°C, creep life, and the volume fraction
of the α
2
phase as outputs, and the structure of the model is
illustrated in Figure 3 .
3.2 | The re sults of multiobjective
optimization
The optimization objectives and constraints of multi-
objective optimization are determined based on domain
knowledge. The optimization module is nondominated
sorting genetic algorithm II (NSGA-II) using FNN as the
surrogate model, achieving the global search, finding the
well-distributed Pareto front, and high-quality sets of Pareto-
optimal solutions for the candidate compositions of new
high-temperature titanium alloys. In the optimization process
of the models, after establishing constraint conditions, opti-
mization begins within the component space. Subsequently ,
a machine learning surrogate model is employed to obtain
performance metrics corresponding to the current compo-
nents. This iterative cycle continues until optimal solutions
on the Pareto front are identified, thereby generalizing new
alloy compositions. The Pareto fronts obtained through
optimization within dif ferent ranges of the α
2
phase content
are illustrated in Figure 4 . Each solution on the front rep-
resents an optimal trade-of f between two performance ob-
jectives. The high-temperature yield strength of the solutions
decreases first by a small amount and then rapidly as the
creep life increases. In order to obtain alloys with both su-
perior high-temperature strength and extended creep life, we
select the optimal solutions prior to significant reductions in
high-temperature strength, as indicated by arrows in the
figures. The six optimal solutions were reverse-mapped to
obtain their corresponding candidate alloy compositions.
These properties, along with the α
2
phase content, are listed
in T able 4 . A summary of the six Pareto fronts derived from
optimizations across various ranges of the α
2
phase content
is presented in Figure 5 . It can be observed that as the α
2
phase content increases, there is a slight enhancement in the
alloy's high-temperature yield strength accompanied by a
notable increase in creep life. This indicates that α
2
con-
tributes positively to both yield strength and creep perfor -
mance enhancement. Furthermore, considering the influence
of α
2
on ductility , an alloy with suitable ranges of the α
2
phase content can be selected based on specific usage re-
quirements and application scenarios.
3.3 | Accuracy verification of multiobjective
optimization
The neural network exhibits a certain degree of generaliza-
tion ability , allowing it to make predictions in regions
T ABLE 3 The content ranges of the α
2
phase.
Content (at. %) 0% 0%–5% 5%–10% 10%–15% 15%–20% 20%–25%
FIGURE 2 Comparison of the accuracy of machine learning models with different hidden layers and nodes. (a) R
2
score; (b) MAE, RMSE.
6 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

beyond the training data. However , excessive extrapolation
may lead to instability . In order to verify the accuracy of the
multiobjective optimization results, the alloy compositions
corresponding to the optimized solutions are verified for the
performance and microstructure parameters. The alloys in
the optimization results were selected that include six
candidate alloys, and the high-temperature yield strength,
creep life, and the α
2
phase content at 650°C were calculated
using the JMatPro software and compared with the predicted
values from the multiobjective optimization. The results of
the comparison between the predicted and JMatPro-
calculated values are shown in Figure 6 . The star symbols
FIGURE 3 The configurations of the FNN model.
FIGURE 4 Pareto fronts obtained by searching for optimization in different α
2
phase content ranges, respectively . (a) α
2
phase content of 0%; (b) α
2
phase content range of 0%–5%; (c) α
2
phase content of 5%–10%; (d) α
2
phase content of 10%–15%; (e) α
2
phase content of 15%–20%; and (f) α
2
phase
content of 20–25%.
-
7 of 12
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

represent the six candidate alloys optimized in this study .
The dotted line indicates the similarity between the JMatPro
calculation values and the optimization values. The predicted
and calculated values of the two objective properties and the
α
2
phase content of the six candidate alloys are shown in
T able 5 . The alloy composition points of these alloys are
primarily distributed near the 45° midline, and the errors
between the predicted and calculated values of the six
candidate alloys are very small, which means that the pre-
dicted values of the optimization and the calculated values of
the JMatPro software are highly consistent, and there is no
excessive extrapolation to make the optimization inaccurate.
Overall, this study establishes a machine learning model
integrated with a multiobjective genetic algorithm to opti-
mize the composition design of high-temperature titanium
alloys, demonstrating remarkable reliability .
3.4 | Comparison with existing high-
temperatur e titanium alloys performance
The compositions of existing typical high-temperature tita-
nium alloys were collected from the literature,
[2,47–54]
and the
yield strength and creep life of each alloy at 650°C were
calculated using JMatPro. A comparison with the properties of
the candidate alloys is shown in Figure 7 . In the figure, the six
candidate alloys obtained in this study exhibit higher high-
temperature yield strength and longer creep life at 650°C
compared to existing high-temperature titanium alloys. The
design methodology of machine learning combined with
multiobjective optimization is able to balance the high-
temperature yield strength and creep life properties, signifi-
cantly accelerating the development process of new materials
and providing high-performance material solutions. In
T ABLE 4 Candidate alloys.
Alloy Y ield strength (650°C/MPa) Creep life (650°C/150 MPa) V α
2
(at. %)
A1 501.37 25.1 1 0.00%
A2 491.79 30.84 4.52%
A3 499.31 38.02 9.98%
A4 504.45 45.50 15.00%
A5 513.23 57.35 19.95%
A6 524.49 72.01 25.00%
FIGURE 5 Distribution of six Pareto fronts obtained by searching for optimization in different α
2
phase content ranges.
8 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

addition, high-temperature titanium alloys primarily consist of
titanium along with other alloying elements. Commonly
added alloying elements, such as Mo, Nb, T a, and Zr , are
relatively expensive. Thus, manufacturing costs and density
are critical factors that must be considered for their practical
application. T aking the A6 alloy designed in this study as an
example, a comparison of its properties, costs, and density
with existing alloys is illustrated in Figure 8 . It can be seen that
the optimized A6 alloy has significantly excellent high-
temperature yield strength and creep properties, whereas its
cost and density are very similar to existing alloys, with a
promising potential for in-depth applied research.
4 | CONCLUSION
The development of artificial intelligence and intelligent
computing is not only a symbol of technological advance-
ment but also a significant force leading social change and
industrial transformation. W ith the progress of artificial in-
telligence research, machine learning is developing rapidly
and playing an increasingly important role in various fields
to help solve more complex problems, which has a very
broad development prospect. In this paper , using the high-
throughput calculations of alloy composition, microstruc-
ture, and properties based on a data-driven approach, we
propose a new comprehensive design strategy that integrates
machine learning with multiobjective optimization algo-
rithms. By referencing the domain knowledge of the
compositional design equivalence criterion as a constraint
and regulating the microstructure parameters of the alloys,
we optimize new high-temperature titanium alloys that
simultaneously meet requirements for the high-temperature
yield strength and creep life while exhibiting excellent
comprehensive performance. The main conclusions are as
follows:
(1) Utilizing the JMatPro simulation software, a high-
throughput approach was employed to rapidly collect
extensive data on alloy composition, microstructure, and
mechanical properties, thereby establishing a compre-
hensive high-temperature titanium alloy database. T ak-
ing the composition as input and the high-temperature
yield strength, creep life, and microstructure parameters
as output, a high-precision machine learning prediction
model was developed.
(2) By integrating a multiobjective genetic algorithm for
global search, candidate alloy compositions are optimized
FIGURE 6 Comparisons of the optimization values and the calculated values using the JMatPro software. (a) Y ield strength; (b) creep life; (c) α
2
phase content.
T ABLE 5 Comparisons of multiobjective optimization and JMatPro.
Properties and microscopic parameters Item A1 A2 A3 A4 A5 A6
Y ield strength V-OPT 501.37 491.79 499.31 504.45 513.23 524.49
V-JMP 502.89 492.48 494.13 503.69 514.1 1 524.33
Error 1.52 0.69 − 5.18 − 0.76 0.88 − 0.16
Creep life V-OPT 25.1 1 30.84 38.02 45.5 57.35 72.01
V-JMP 24.17 31.46 37.88 46.94 57.10 72.06
Error − 0.94 0.62 − 0.14 0.44 − 0.25 0.05
Vα
2
V-OPT 0.00% 4.52% 9.98% 15.00% 19.95% 25.00%
V-JMP 0.00% 4.46% 9.5% 14.91% 19.57% 24.79%
Err or 0 − 0.06% − 0.48% − 0.08% − 0.38% − 0.21%
Note : V-OPT stands for “value from optimization”; V-JMP represents “value from JMatPro”.
-
9 of 12
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

within the constraints, and the predicted values of the
properties and microstructural parameters of the candi-
date alloys are highly consistent with the calculated
values from JMatPro, which indicates that the machine
learning model combined with the multiobjective genetic
algorithm established in this study demonstrates strong
reliability in optimizing the composition design of high-
temperature titanium alloys.
FIGURE 7 Comparison of the calculated performance values of candidate alloys with existing high-temperature titanium alloys.
FIGURE 8 Comparison of the performance, cost, and density of the A6 alloy with existing high-temperature titanium alloys.
10 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

(3) The α
2
phase is considered a reinforcing phase to
improve the high-temperature strength and creep life of
the alloy while considering the plasticity , limiting the
range of its content, and gradient dividing the interval to
find the optimal alloy . W ith the increase in the α
2
phase
content, the yield strength and creep life of the opti-
mized alloys increase significantly , indicating the
strengthening ef fect of the α
2
phase. Consequently , this
leads to obtain titanium alloys with excellent compre-
hensive mechanical properties at elevated temperatures.
(4) A new strategy based on machine learning combined
with multiobjective optimization has successfully sur-
passed the traditional thermal barrier temperature of ti-
tanium alloys at 600°C. This approach has led to the
design of a novel high-temperature titanium alloy that
maintains excellent high-temperature strength, long
creep life, and minimal plastic deformation even at
650°C, resulting in outstanding comprehensive me-
chanical properties. Compared to existing typical high-
temperature titanium alloys, this new material exhibits
comparable cost and density while demonstrating sig-
nificant advantages in high-temperature yield strength
and creep life, providing a valuable reference for the
future design of high-temperature titanium alloys.
AUTHOR CONTRIBUTIONS
Lingzhi Liu : Investigation; methodology; writing-original
draft; writing – review and editing; data curation. Lixian
Lian : W riting – review and editing; methodology; funding
acquisition; project administration. Xingyue Li : Software,
data curation, validation. Jiaqi Wu : W riting – review and
editing; data curation. W ang Hu : Conceptualization; meth-
odology; software. Y ing Liu : Supervision; project adminis-
tration; funding acquisition; resources.
ACKNOWLEDGEMENTS
This study is financially supported by the National Natural
Science Foundation of China under Grant No. 61976046.
CONFLICT OF INTEREST ST A TEMENT
The authors declare no conflicts of interest.
DA T A A V AILABILITY ST A TEMENT
The data that support the findings of this study are available
from the corresponding author upon reasonable request.
ORCID
Lixian Lian
 https://orcid.org/0000-0001-8660-497X
REFERENCES
1. Ziyong C, Y ingying L, Y anfang J, Xiaozhao M, Lihua C, Y apeng C.
Research on 650°C high temperature titanium alloy technology for
aero-engine. Aer onaut Manufact T echnol . 2019;62 (19):22-30.
2. Jianming C, Chunxiao C. Alloy design and application expectation of
A new generation 600°C high temperature titanium alloy . J Aer o-
nautical Mater . 2014;34 (4):27-36.
3. Chunyan H, Lijun Z. The development and application of high tem-
perature titanium alloy at domestic and abroad. W orld Nonferr ous
Metals . 2016(1):21-25.
4. An Z, Y uandong Z, Xiuliang L, et al. Advanced aerospace titanium
alloy materials research progress. Sci T echnol Innov . 2023(13):9092.
5. Dong H, Shaoli Y, Lan M, et al. Current research status and devel-
opment of high-temperature titanium alloys. Ir on Steel V anadium
T itan . 2018;39 (1):6066.
6. Agrawal A, Choudhary A. Perspective: materials informatics and big
data: realization of the “fourth paradigm” of science in materials
science. APL Mater . 2016;4 (5):053208.
7. Xiaoxi M, Aitao T, Y uChen Z, et al. Research progress of machine
learning in material science. Mater Rep . 2021;35 (15):151 15-15124.
8. Y ong N, Zhiqiang H, Y ao-qi W, Zhu Y. Machine learning-based beta
transus temperature prediction for titanium alloys. J Mater Res
T echnol . 2023;23:515-529.
9. Malinov S, Sha W, McKeown J. Modelling the correlation between
processing parameters and properties in titanium alloys using artificial
neural network. Comput Mater Sci . 2001;21 (3):375-394.
10. Changlu Z, Ruihao Y, Baolong S, et al. Creep rupture life prediction
of high-temperature titanium alloy using cross-material transfer
learning. J Mater Sci T echnol . 2024;178:39-47.
1 1. Xiujuan L, Pengcheng X, Juanjuan Z, Lu W, Li M, W ang G. Material
machine learning for alloys: applications, challenges and perspectives.
J Alloys Compd . 2022;921:165984.
12. Y ujie D, Kui W. Study on the isothermal quenching process of C55E
steel chain plates with JMatPro software. J Mech T ransm . 2024;
48 (6):147-152.
13. Zhang B, Mu W, Cai Y. The ef fect of cooling rate on the precipitation
behavior and fracture toughness of the η phase in LDED CoCrFeNiT i
high-entropy alloy . Mater Sci Eng . 2024;914:147172.
14. Ruochen S, Guangbao M. Influence of alloying elements content on
high temperature properties of T i-V-Cr and T i-Al-V series titanium
alloys: a JMatPro program calculation study . J Phys Conf .
2023;2639 (1):012019.
15. Zhongbing C, Y unhe Y, Hou J, Zhu P, Zhang J. Microstructure and
properties of iron-based surfacing layer based on JmatPro software
simulation calculation. V ibr oeng Pr ocedia . 2023;50:180-186.
16. Zhuomeng L, Shewei X, Y ongqing Z. Research progress on the creep
resistance of high-temperature titanium alloys: a review . Metals .
2023;13 (12):1975.
17. Jingjie D, Fengyun Z, Amin W, et al. Effect of Nb doping on high
temperature oxidation resistance of T i-Al alloyed coatings. J Mater
Eng . 2017;45 (2):24-31.
18. Jiang H, Hirohasi M, Lu Y, Imanari H. Effect of Nb on the high
temperature oxidation of T i–(0–50 at. %) Al. Scr Mater .
2002;46 (9):639-643.
19. Huang X, W en P, Li G, et al. Effects of T a and Nb on high-
temperature oxidation properties of T i-6Al-3.5Sn-4Hf-0.4Si-X al-
loys. J Alloys Compd . 2024;1002:175143.
20. Gurrappa I, Manova D, Gerlach JW, Mändl S, Rauschenbach B.
Influence of nitrogen implantation on the high temperature oxida-
tion of titanium-base alloys. Surf Coating T echnol . 2006;201 (6):
3536-3546.
21. Qiang L, Sheng H, Y akai Z, Gao Y, Ramamurty U. Simultaneous
enhancements of strength, ductility , and toughness in a T iB reinforced
titanium matrix composite. Acta Mater . 2023;254:1 18995.
22. Prado J, Song X, Hu D, W u X. The influence of oxygen and carbon-
content on aging of T i-15-3. J Mater Eng Perform .
2005;14 (6):728-734.
23. Hemeida AM, Hassan SA, Mohamed AA, et al. Nature-inspired al-
gorithms for feed-forward neural network classifiers: a survey of one
decade of research. Ain Shams Eng J . 2020;1 1 (3):659-675.
24. Shengya L, Shujuan H. A machine learning method of accelerating
multiscale analysis for spatially varying microstructures. Int J Mech
Sci . 2024;266:108952.
-
1 1 of 12
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 12

25. Y uedan D, Y u Z, Xiufang G, et al. An intelligent design for Ni-based
superalloy based on machine learning and multi-objective optimiza-
tion. Mater Des . 2022;221:1 10935.
26. Jianxin X, Y anjing S, Dezhen X, et al. Machine learning for materials
research and development. Acta Metall Sin . 2021;57 (1 1):1343-1361.
27. Zhexue G, Zhiqiang S. Artificial Neural Network Theory and Matlab
R2007 Realization . Electronics Industry Press; 2007.234.
28. V erma S, Pant M, Snasel V. A comprehensive review on NSGA-II for
multi-objective combinatorial optimization problems. IEEE Access .
2021;9:57757-57791.
29. Deb K, Pratap A, Agarwal S, Meyarivan T. A fast and elitist multi-
objective genetic algorithm: NSGA-II. IEEE T rans Evol Comput .
2002;6 (2):182-197.
30. Haiping M, Y ajing Z, Shengyi S, Liu T, Shan Y. A comprehensive
survey on NSGA-II for multi-objective optimization and applications.
Artif Intell Rev . 2023;56 (12):15217-15270.
31. Rosenberg HW. T itanium alloying in theory and practice. In: The
Science, T echnology and Application of T itanium ; 1970:851-859.
32. Koike J, Egashira K, Maruyama K, Oikawa H. High temperature
strength of α T iAl alloys with a locally ordered structure. Mater Sci
Eng . 1996;213 (1-2):98-102.
33. Narayana PL, Kim SW, Hong JK, Reddy N, Y eom JT. T ensile
properties of a newly developed high-temperature titanium alloy at
room temperature and 650°C. Mater Sci Eng . 2018;718:287-291.
34. Onodera H, Nakazawa S, Ohno K, Y amagata T, Y amazaki M. Creep
properties of α þ α
2
high temperature titanium alloys designed by the
aid of thermodynamics. ISIJ Int . 1991;31 (8):875-881.
35. Jun Z, Dong L. α
2
Or der ed Phase in High T emperatur e T itanium
Alloys . Northeastern University Press; 2002.
36. Y anhua G, Jingzhe N, Juexian C, Sun Z, Dan Z, Chang H. Relative
strength of β phase stabilization by transition metals in titanium alloys:
the Mo equivalent from a first principles study . Mater T oday Commun .
2023;35:106123.
37. Y ili L, Hongze F, Ruirun C, Sun S, Xue X, Guo J. Optimization of (α
þ β) microstructure and trade-off between strength and toughness:
based on Mo[eq] and d electron theory in β-T i alloy . Mater Des .
2023;231:1 12022.
38. Antipov AI, Moiseev VN. Coefficient of β-stabilization of titanium
alloys. Metal Sci Heat T r eat . 1997;39 (12):499-503.
39. Shuxin S, Xu G, Bei H, et al. The ef fect of microstructure on room and
medium temperature tensile properties of titanium alloy fabricated by
laser additive manufacturing used in aeroengine. Aer onautical Sci and
T echnol . 2022;33 (9):66-76.
40. Y ongqing Z, Y ongnan C, Xuemin Z, et al. Phase T ransformation and
Heat T r eatment of T itanium Alloy . Central South University Press; 2012.
41. Delai OY, Shiqiang L, Xia C, et al. T ransformation of deformation-
induced martensite in TB6 titanium alloy . Chin J Nonferr ous
Metals . 2010;20 (12):2307-2312.
42. Guangrong W, Qi G, Jixiong L, et al. Composition design of beta-
titanium alloys: theoretical methodological and practical advances.
Mater Rev . 2017;31 (3):44-51.
43. Peters M, Hemptenmacher J, Kumpfert J, et al. Structur e and Pr operties
of T itanium and T itanium Alloys . John W iley and Sons, Ltd; 2005.
44. Gogia AK. High-temperature titanium alloys. Def Sci J . 2005;55 (2):
149-173.
45. Shang L, T ongsheng D, Y inghui Z, Liang Y, Li R, Dong T. Review on
the creep resistance of high-temperature titanium alloy . T rans Indian
Inst Metals . 2021;74 (2):215-222.
46. Y ong W, Bin L, Rui Y. Effect of (Mo, W) content and heat treatment
on the tensile properties of a high-temperature titanium alloy . Chin J
Mater Res . 2010;24 (3):283-288.
47. Jianming C, Guangbao M, Fan G, et al. Research and development of
some advanced high temperature titanium alloys for aero-engine. J
Mater Eng . 2016;44 (8):1-10.
48. T abie VM, Chong L, Saifu W, Li J, Xu X. Mechanical properties of
near alpha titanium alloys for high-temperature applications - a re-
view . Air craft Eng Aer o T echnol . 2020;92 (4):521-540.
49. Chandravanshi VK, Sarkar R, Kamat SV, Nandy T. Effect of boron on
microstructure and mechanical properties of thermomechanically
processed near alpha titanium alloy T i-1 100. J Alloys Compd .
201 1;509 (18):5506-5514.
50. Qingjiang W, Jianrong L, Rui Y. High temperature titanium alloys:
status and perspective. J Aer onautical Mater . 2014;34 (4):1-26.
51. Chandravanshi VK, Sarkar R, Ghosal P, Kamat S, Nandy T. Effect of
minor additions of boron on microstructure and mechanical properties
of as-cast near α titanium alloy . Metallur gical Mater T rans A .
2010;41 (4):936-946.
52. Minmin W, Xinyue L, Bo J. Effect of second phase addition on me-
chanical properties of 7715D high temperature alloy . Chin J Nonfer-
r ous Metals . 2010;20 (S1):156-160.
53. Rui G, Bin L, Rongjun X, et al. Microstructure and mechanical
properties of powder metallurgy high temperature titanium alloy with
high Si content. Mater Sci Eng . 2020;777:138993.
54. Guangbao M, Y ong T, Hang C, et al. Progress on additive
manufacturing of 600°C high-temperature titanium alloys. J Aer o-
nautical Mater . 2024;44 (1):15-30.
How to cite this article: Liu L, Lian L, Li X, Jiaqi W,
Hu W, Liu Y. Intelligent optimized design of novel
high-temperature titanium alloys. Materials Genome
Engineering Advances . 2025;3(3):e70006. https://doi.
org/ 10.1002/mgea.70006
12 of 12
-
 29409497, 2025, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/mgea.70006 by Xian Jiaotong University, Wiley Online Library on [25/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
