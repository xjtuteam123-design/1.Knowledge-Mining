# Heat-resistant aluminum alloy design using explainable machine learning

<!-- source: D:\总文献\Heat-resistant aluminum alloy design using explainable machine learning.pdf -->
<!-- file_sha256: 77755ad362810203df3503a768e2a282ed0c1db577ac87affa9241eb94c997bc -->

## Page 1

Materials & Design 243 (2024) 113057
Available online 31 May 2024
0264-1275/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/).
Heat-resistant aluminum alloy design using explainable machine learning 
Jinxian Huang
a
, Daisuke Ando
a , *
, Yuji Sutou
a , b 
a
Department of Materials Science, Tohoku University, Sendai 980-8579, Miyagi, Japan 
b
Advanced Institute for Materials Research, Tohoku University, Sendai 980-8577, Miyagi, Japan 
ARTICLE INFO 
Keywords: 
Alloy design 
Aluminum alloys 
Machine learning 
Mechanical properties 
ABSTRACT 
The high-temperature strength of aluminum alloys must be enhanced for improving their applicability across 
industries. This study proposes a machine learning approach for developing heat-resistant aluminum alloys. 
Using a combination of correlation-based screening and genetic algorithms, feature selection was performed on 
descriptors derived from the atomic compositions of alloys. Then, alloy compositions and descriptors were used 
as input variables of the model to improve its robustness and applicability due to the richness of information. 
Four distinct alloys were discovered by employing Bayesian optimization within the framework of a quaternary 
alloy system. The best alloy demonstrated an exceptional high-temperature strength of 175 MPa at 300 
◦
C in the 
absence of heat treatment. Microstructural analyses of these alloys indicated the critical role of vanadium-rich 
intermetallics in enhancing the high-temperature strength of aluminum alloys. Furthermore, the output of the 
model was explained using the SHapley Additive exPlanations method. The findings emphasize the critical 
importance of titanium and vanadium in enhancing the high-temperature strength of aluminum alloys tailored 
for environments with high thermal stress. 
1. Introduction 
Aluminum alloys are widely used across industries such as automo -
tive and aerospace [1,2] . However, some applications demand high- 
temperature performance aluminum alloys. For instance, cast 
aluminum alloys are used to fabricate brake discs for electrical vehicles, 
where these alloys are subjected to a maximum service temperature of 
~ 300 
◦
C [3] . Nonetheless, the available commercial aluminum alloys 
pose a limitation: their strength decreases at high temperatures, limiting 
their application in high-temperature environments over 250 
◦
C [4] . 
Therefore, aluminum alloys tailored to withstand such high-temperature 
conditions, i.e., heat-resistant aluminum alloys, must be developed. The 
strength of aluminum alloys considerably degrades under high tem -
peratures due to the rapid coarsening of strengthening phases. The 7075 
alloy, when subjected to thermal exposure at 300 
◦
C for 1 h, exhibited a 
transformation wherein the nanoscale precipitates dissolved and coarse 
Mg(Zn, Cu)
2 
precipitates formed on the surface of Al
18
Mg
3
Cr
2 
dispersoid 
particles [5] . In the Al-Mg-Si alloys, the highly effective precipitation 
strengthening phase, β ʹʹ , transforms to β ʹ and the precipitate size rapidly 
increases during extended thermal exposure even at temperatures as low 
as 150 
◦
C [6] . The θ ʹ phase in Al-Cu alloys maintained its size stability 
below 230 
◦
C, notably exceeding the operational temperatures of Al-Zn- 
Mg and Al-Mg-Si alloys. However, when exposed to higher tempera -
tures, the θ ʹ phase undergoes significant coarsening, which degrades the 
strength of alloys [7] . 
Recent studies on heat-resistant aluminum alloys have predomi -
nantly focused on introducing Sc into Al-Cu alloys to stabilize precipi -
tation strengthening [8] . Gao et al. found that the segregation of Sc at 
the θ ′ -Al
2
Cu/matrix interface improved the thermostability of the 
θ ′ -Al
2
Cu precipitates [9] . Lu et al. proposed that multiple interface 
structures in an Al-Cu-Mg-Ag-Si-Sc alloy synergistically decelerated the 
coarsening of θ ′ -Al
2
Cu precipitates [10] . Although these findings high -
light the crucial role of Sc in enhancing the high-temperature strength of 
aluminum alloys, the high cost of Sc necessitates the exploration of 
alternative, more affordable elements or alloy systems. It has been re -
ported that introducing Fe into Al-Si alloys results in the formation of 
needle-like Fe-rich intermetallics, which, despite their stability at high 
temperatures, negatively impact ductility and castability [11 – 13] . 
Similarly, the addition of Mn, Cr, and Ce to Al-Si alloys has been shown 
to produce comparable effects, enhancing high-temperature strength 
but potentially compromising other mechanical properties due to their 
inherent brittleness [14 – 16] . Additionally, while the combined addition 
of Zr, V, and Ti has been shown to enhance the strength and fatigue life 
of aluminum alloys at room temperature through the formation of 
* Corresponding author. 
E-mail address: daisuke.ando.c4@tohoku.ac.jp (D. Ando). 
Contents lists available at ScienceDirect 
Materials & Design 
journal homep age: www.el sevier.com/l ocate/matde s 
https://doi.org/10.1016/j.matdes.2024.113057 
Received 6 February 2024; Received in revised form 2 May 2024; Accepted 28 May 2024

## Page 2

Materials & Design 243 (2024) 113057
2
trialuminide precipitates [17] , their effect on high-temperature perfor -
mance remains ambiguous [18,19] . The complex composition of these 
alloys complicates the identification of elements beneficial for high- 
temperature strength. Therefore, it is crucial to develop strategies to 
effectively address this challenge. 
Knowledge-guided methodologies are conventionally used for 
designing alloys. Recently, machine learning, a data-guided technique, 
has found extensive application in materials science. Machine learning 
models predict the performance of materials from curated datasets, 
significantly reducing the need for extensive experimental trials. The 
successful application of machine learning has notably contributed to 
the development of new alloys such as Cu alloys [20,21] and high- 
entropy alloys [22 – 26] . Machine learning has played a pivotal role in 
the development of advanced aluminum alloys as well. Li et al. 
employed the Kriging model within the Al-Zn-Mg-Cu alloy system to find 
high-strength alloy compositions [27] and Cao et al. developed strate -
gies using a limited dataset of 40 samples to optimize the stress corrosion 
cracking resistance of the same alloy system [28] . Similarly, Park et al. 
and Li et al. developed high-strength aluminum alloys focusing on 7xxx 
series via machine learning [29,30] . Chaudry et al. created a compre -
hensive dataset for Al-Cu-Mg-x alloys and utilized the gradient boosted 
tree algorithm to pinpoint alloys with superior hardness [31] . Juan et al. 
further advanced the field by implementing a knowledge-aware design 
system driven by the extreme gradient boosting algorithm, boosting the 
tensile strength of aviation aluminum alloys to an impressive 812 MPa at 
room temperature [32] . Despite these advancements, the application of 
machine learning specifically to enhance the high-temperature strength 
of aluminum alloys remains underexplored. Moreover, previous studies 
have often focused on optimizing the composition across all input ele -
ments within a specific alloy type, which limits the potential to discern 
which alloying elements are most beneficial for targeted properties. This 
gap underscores the need for more targeted research that could further 
refine the application of machine learning in developing heat-resistant 
aluminum alloys. 
At present, the high-temperature mechanical properties of heat- 
treated aluminum alloys are predominantly studied. However, certain 
applications, such as complex thin-wall castings for automotive and 
aerospace components, may not necessitate heat treatment [33,34] . 
Thus, machine learning was used herein to develop non-heat-treated, 
heat-resistant cast aluminum alloys that could sustain a high tempera -
ture of 300 
◦
C similar to the components used in the automotive industry 
[35] . Additionally, alternative combinations of micro-alloying elements, 
besides Sc, were identified to effectively enhance the high-temperature 
strength of aluminum alloys. 
2. Dataset and machine learning flow 
2.1. Dataset curation 
To expedite data collection, text-mining technique was used to 
search relevant sources using keyword matching. Then, a manual 
screening process was implemented to identify reliable data. A dataset 
containing 407 entries was collated from various published research 
articles and patents. Each dataset entry included details of the chemical 
composition of aluminum alloys, heat treatment conditions, and tensile 
test temperatures. The corresponding ultimate tensile strength (UTS) 
was collected as the output. The composition encompassed a total of 15 
alloying elements: Cu, Si, Mg, Mn, Fe, Zn, Ni, Ti, Sc, V, Zr, Cr, Ce, La, and 
Mo. Heat treatment was categorized into six groups: as-cast, T4, T5, T6, 
T7, and high-temperature exposure after aging (referred to as T7L 
hereafter). These heat treatment conditions were labeled by an ordinal 
encoder to obtain numerical values before constructing the machine 
learning model. Tensile test temperatures across the dataset ranged from 
100 
◦
C to 450 
◦
C. Fig. 1 shows the UTS of alloys subjected to different 
heat treatments and test temperatures. As we focus on cast aluminum 
alloys, the dataset exclusively contained data on alloys produced via 
conventional casting, devoid of any deformation processing. This 
stringent focus ensured the reliability of dataset and its alignment with 
our research objectives. 
To feed more information into the machine learning model, 29 de -
scriptors (besides the main inputs) were chosen, including physical, 
crystal, and chemical information of elements that potentially impact 
the mechanical properties of alloys [24] . The mean and variance of each 
descriptor value were calculated based on the atomic composition of 
alloys within the dataset using Eq. (1) and Eq. (2) , respectively. 
D
mi
=
∑
 
D
ij
a
j
)
/
∑
a
j
(1) 
D
vi
=
∑
[
 
D
ij
 D
mi
)
2
× a
j
]/
∑
a
j
(2) 
where D
mi 
and D
vi 
are the mean and variance of a given descriptor i for 
each data in the dataset, respectively; D
ij 
is the value of descriptor i of a 
given element j ; and a
j 
is the atomic fraction of element j in the 
composition. Furthermore, an additional set of five descriptors was 
added to gain deeper insight into the information of alloys. Thus, 63 
descriptor values (29 × 2 + 5) were calculated for subsequent feature 
selection. Detailed information regarding these descriptors can be found 
in Tables S1 and S2 . The dataset was randomly partitioned into two 
segments. Ninety percent of the entries were allocated to the training set 
for the machine learning model, and the remaining entries were desig -
nated as the testing set to assess the generalizability. The numerical 
features were normalized using Eq. (3) . 
z
i
= ( x
i
 u ) / s (3) 
For a specific descriptor, z
i 
represents the z-score value of i
th 
entry, x
i 
is 
the raw value, u and s are the mean and standard variation in the 
training set, respectively. 
2.2. Design of heat-resistant aluminum alloys using machine learning 
According to the no free lunch theorem that suggests no single ma -
chine learning algorithm universally outperforms others, we systemat -
ically compared different algorithms to identify the most effective one 
for our dataset. Specifically, the Support Vector Regression (SVR) and 
ExtraTrees (ET) algorithms were performed based on the scikit-learn 
package in Python [36,37] . Gaussian Process Regression (GP) was per -
formed using the GPy [38 – 40] , and the XGBoost (XGB) algorithm was 
implemented with the XGBoost package [41] . For the Artificial Neural 
Network (ANN), it was built based on TensorFlow framework [42,43] . 
Bayesian Optimization was employed by the Optuna [44] . These models 
were compared based on the tenfold cross-validation (CV) results using 
Fig. 1. Overview of the dataset. 
J. Huang et al.

## Page 3

Materials & Design 243 (2024) 113057
3
the mean absolute error (MAE) as the scoring metric within the training 
set. The performance of models was evaluated in the testing set based on 
the R
2 
value as follows: 
MAE =
∑
n
i = 1
| y
i
 ̂y
i
|
n
(4) 
R
2
= 1 
1
n
∑
n
i = 1
( y
i
 ̂y
i
)
2
1
n
∑
n
i = 1
( y
i
 y )
2
(5) 
where y
i 
is the actual value in the dataset, ̂y
i 
is the value predicted by the 
model, and y is the mean value. 
The aforementioned algorithms were initially used to build a model 
using main inputs. The model with lowest training bias was then 
selected to train on the dataset with additional descriptors. The de -
scriptors were initially screened using a correlation-based analytical 
method based on the Pearson correlation coefficient (PCC). This 
screening was conducted because a large number of descriptors and 
multicollinearity would make training difficult. Descriptors with a PCC 
greater than 0.8 with each other were considered highly correlated. In 
such a process, the descriptor with a higher coefficient of variation ( Cv 
= σ / µ ; σ : mean; µ : variance) was retained, as it was expected to provide 
greater variation in information. Then, the genetic algorithm was used 
to identify the best descriptor combination. The screened descriptors 
were used as inputs alongside the main inputs to train the model for 
predicting the high-temperature UTS of aluminum alloys. 
For the design of heat-resistant aluminum alloys, a candidate space 
for alloy compositions was defined ( Table S3 ). The primary goal of this 
study was to develop cost-effective cast heat-resistant aluminum alloys, 
with an emphasis on affordability. To this end, Sc was excluded due to its 
high cost. Rather than searching across all possible alloy compositions, 
as seen in some studies [45,46] , this research strategically limited its 
exploration to quaternary alloy systems. This approach not only sim -
plifies the composition but also effectively narrows down the large 
composition space to combinations likely to enhance high-temperature 
performance. Hence, composition optimization was conducted for 364 
( C
3
14
) quaternary alloy systems. We then focused on optimizing UTS at 
300 
◦
C in the as-cast state as our primary performance metric. Using 
Bayesian optimization over 100 iterations, the performance of various 
alloy compositions for each quaternary alloy system was systematically 
evaluated, identifying the compositions that demonstrated the highest 
strength. For each quaternary alloy system, one composition was pro -
posed by optimization. Upon completion of the optimization process, 
the resulting compositions were sorted and ranked. The top four can -
didates with the highest UTS were selected for further experimental 
validation. 
2.3. Model explanation 
To gain insights into the underlying rationale behind the recom -
mendations of the proposed alloy from the machine learning model, the 
SHapley Additive exPlanations (SHAP) method was used for further 
investigation [47] . SHAP yields importance values, referred to as SHAP 
values, for each feature related to a specific prediction. These values 
offer insights into the particular alloy compositions favored by the 
model. The inputs were sorted based on the SHAP values for discussion 
and analysis. 
3. Experimental procedure 
3.1. Materials preparation 
Pure commercial aluminum ( > 99.7 wt%), Al-50Cu (in wt. %), Al- 
20Si, Al-10Ni, Al-5Ti, and Al-5 V master alloys were used as raw ma -
terials for experiments. The alloy was melted in a high-frequency 
induction furnace in an argon atmosphere and subsequently poured into 
a permanent mold at approximately 750 
◦
C. 
3.2. Tensile testing 
Specimens for the tensile testing experiments were cut from the as- 
cast ingot and processed into flat plates with a gauge length of 15 
mm. The tensile test was performed at least three times in a universal 
testing machine (SHIMADZU AG-X Plus) at 300 
◦
C with a strain rate of 
0.001/s. Before the test, the specimens were preheated in a thermostatic 
chamber. A thermocouple was positioned near the specimen to ensure 
that the temperature reached the designated test temperature. 
3.3. Microstructure characterization 
Phase analysis was performed using X-ray diffraction (XRD; RIGAKU 
ULTIMA) with Cu-K α radiation ( λ = 1.5405 Å). The scan speed was 10
◦
/ 
min and scan range was 10
◦
-80
◦
. The microstructure was examined via 
optical microscopy (OM; Lasertec OPTELICS HYBRID) and field- 
emission scanning electrode microscopy (FE-SEM; JSM-6500F) inte -
grated with energy-dispersive X-ray spectrometry (EDS). Specimens 
prepared for OM and SEM observations were mechanically polished. 
Then, specimens containing high Si content were directly etched with 
Keller ’ s reagent for 10 s. The remaining specimens underwent electro -
polishing using a solution composed of 90 % ethanol and 10 % 
perchloric acid. For fractographic analysis, the specimens were cleaned 
with absolute ethyl alcohol immediately after the high-temperature 
tensile test without undergoing any additional polishing. 
4. Results 
4.1. Machine learning results 
The split training set containing 367 entries was used to train the 
machine learning models with main inputs and predict the high- 
temperature UTS of aluminum alloys. The testing set was shielded to 
prevent any data leakage, and the model performance was evaluated 
based on the CV result. As shown in Fig. 2 , the ET model exhibited the 
lowest MAE in tenfold validation, specifically at 16.3 ± 2.2 MPa. This 
indicates that the ET model achieved the highest accuracy among the 
tested models and was therefore used for subsequent flows. 
The additional descriptors first underwent a two-step feature engi -
neering process. After PCC screening, the number of additional de -
scriptors was reduced from 63 to 16. Fig. 3 shows that the coefficients of 
the remaining descriptors are all below 0.8. Here, the prefix “ v- ” sig -
nifies the variance of value for each entry. These descriptors were 
further filtered through a genetic algorithm, which iterated 100 
Fig. 2. Training results for machine learning model using different algorithms. 
J. Huang et al.

## Page 4

Materials & Design 243 (2024) 113057
4
generations, and the CV result of the model was defined as the fitness 
function to guide the production of new generations. Consequently, 
three descriptors, “ v-max solubility, ” “ v-modulus, ” and “ modulus 
mismatch, ” were proposed as descriptors that favor the performance of 
the ET model. 
Fig. 4 a shows the training results with and without additional de -
scriptors. The introduction of additional descriptors effectively improves 
the performance of the ET model, as evidenced by the decrease in the 
mean CV result from 16.3 (without descriptors) to 14.4 (with de -
scriptors). This shows an approximate 12 % improvement, highlighting 
the effectiveness of incorporating additional descriptors in the alloy 
design. The ET model trained with additional descriptors was ultimately 
validated on the testing set. The fitness on the training and testing sets 
were 0.98 and 0.92, respectively ( Fig. 4 b). 
The trained ET model used the provided dataset and descriptors to 
predict the strength of unknown alloys during Bayesian optimization. 
Table 1 shows the detailed composition of the four alloys proposed by 
the machine learning model along with the corresponding predicted 
strength. 
4.2. Evaluation of high-temperature strength 
Fig. 5 shows the engineering strain – stress curves for four alloys, as 
proposed by the machine learning model, tested at 300 
◦
C in the as-cast 
state. The ASCV alloy exhibited the best performance, with a high 
average UTS of 175 MPa, yield strength of 111 MPa, and elongation of 
Fig. 3. The heatmap of descriptors screened by PCC. 
Fig. 4. a Comparison of CV results with and without additional descriptors; b fitness based on the training set and testing set. 
Table 1 
Nominal compositions of the proposed alloys (wt.%), measured compositions 
are shown in parentheses. 
Alloy Al Cu Si Ni Ti V Predicted 
UTS/ MPa 
ANTV Bal. 5.80 
(5.88) 
0.24 
(0.21) 
0.55 
(0.53) 
146.1 
ACTV Bal. 3.10 
(3.26) 
0.24 
(0.25) 
0.65 
(0.62) 
149.1 
ASTV Bal. 7.55 
(7.16) 
0.21 
(0.20) 
0.45 
(0.52) 
149.9 
ASCV Bal. 1.40 
(1.49) 
7.05 
(6.83) 
0.50 
(0.55) 
143.8 
J. Huang et al.

## Page 5

Materials & Design 243 (2024) 113057
5
16.5 %. Thus, the ASCV alloy shows exceptional high-temperature 
strength and good ductility at 300 
◦
C. The ACTV and ASTV alloys 
have comparable strengths of 153 and 158 MPa, respectively. Although 
the ANTV alloy showing the lowest strength of 131 MPa in these testing 
conditions, all the alloys proposed by the machine learning model 
exhibited satisfactory performance for high-temperature applications. 
4.3. Microstructure characterization 
It is easy to see that polyhedral intermetallics present in all examined 
alloys, as shown in Fig. 6 . For ANTV alloy, the microstructure comprises 
an eutectic structure which is attributed to a near-eutectic composition. 
The distribution of intermetallics in this alloy is uniform and smaller 
than that observed in other alloys. The microstructure of ACTV alloy 
consists of Al
2
Cu phase and intermetallics distributing within grains. In 
the Si-rich alloys, it can be observed that intermetallics are inter -
connected with eutectic silicon particles, as shown in Fig. 6 c and d, 
marked by red arrows. 
Fig. 7 more clearly reveals the presence of intermetallics in alloys. 
The areas analyzed by EDS are indicated by numerical markers in the 
images, and the corresponding results are summarized in Table 2 . The 
identified intermetallics are likely Al
10
V, possibly formed via a peritectic 
reaction occurring at 662.1 
◦
C as follows: L + Al
10
V → α -Al [48] . In 
conjunction with the OM and SEM observations, the XRD patterns of the 
proposed as-cast alloys show their microstructure characteristics 
( Fig. 8 ). Fig. 8 b is an enlarged view of the XRD pattern that shows 
several weak peaks corresponding to Al
10
V. Al
10
V peaks are absent for 
the spectrum of the ASTV alloy, which could be attributed to either a low 
volume fraction of Al
10
V or differences in the tested area. 
Fig. 5. a Strain-stress curve of the as-cast alloys measured experimentally at 300 
◦
C and b statistical values derived from the experimental data. 
Fig. 6. The OM microstructure of a ANTV, b ACTV, c ASTV and d ASCV. Red arrows indicate intermetallics in ASTV and ASCV alloys. (For interpretation of the 
references to colour in this figure legend, the reader is referred to the web version of this article.) 
J. Huang et al.

## Page 6

Materials & Design 243 (2024) 113057
6
4.4. Feature importance 
To further understand the inputs that influence model recommends, 
the SHAP method was used. Fig. 9 shows a summary plot of the input 
features derived from the training set. The magnitude of the SHAP 
values indicates the degree of influence of a feature on the output of the 
model; larger values represent greater impact. 
The analysis highlights that test temperature and heat treatment are 
pivotal factors that considerably affect the model output. In addition, Ti, 
Cu, Si, V, Fe, and Zr have a moderate impact on the predicted values. The 
analysis also underscores the importance of all additional descriptors, 
each contributing to a certain extent to the predictions. However, it is 
observed that other elements like Sc, Cr, and Mo, while still influential, 
have a relatively minor impact on the model output compared to the 
aforementioned elements. 
Fig. 7. SEM images of the intermetallics in the a ANTV, b ACTV, c ASTV and d ASCV alloy. 
Table 2 
EDS analysis results corresponding to the area marked in Fig. 6 , in wt. % (at. %). 
Area Al Ni Cu Si Ti V 
1 83.38 
(90.33) 
 3.60 
(2.20) 
13.02 
(7.47) 
2 80.34 
(88.76) 
 3.29 
(1.55) 
 3.20 
(1.99) 
13.17 
(7.70) 
3 79.20 
(86.42) 
 3.05 
(3.20) 
3.66 
(2.25) 
14.08 
(8.14) 
4 77.49 
(85.70) 
 2.98 
(1.40) 
3.05 
(3.24) 
 16.48 
(9.65) 
Fig. 8. a XRD spectra of the proposed alloys in the as-cast state and b an enlarged observation. 
J. Huang et al.

## Page 7

Materials & Design 243 (2024) 113057
7
5. Discussion 
5.1. Model accuracy 
An optimal machine learning model should exhibit consistent per -
formance on both the training and testing sets, signaling the absence of 
overfitting. This consistency ensures that the model generalizes well to 
new, unseen data, reflecting its robustness and reliability. According to 
the “ over-fitting ” index (R
2
Test
/R
2
Train
), a value of this index closer to 1 
indicates a better model. The over-fitting for the ET model used in this 
study is 0.94 ( Fig. 4 ), suggesting a similar level of accuracy on both the 
training and testing datasets implies excellent generalization perfor -
mance. Thus, the developed model has sufficient robustness and accu -
racy to be used in the design of alloys that were not included in the 
training set. 
Table 3 shows the comparative analysis between the predicted and 
experimental values for the alloys. Results demonstrate that the pre -
dictions for ASTV and ACTV alloys align closely with their experimental 
results. The prediction bias for the ASCV alloy is more pronounced than 
the other alloys, but it remains within acceptable bounds when evalu -
ated against recent publications in machine learning-based alloy design 
[22] . The average prediction bias for the proposed alloys is ~ 9.2 %, 
which is considered sufficiently accurate. This consistency emphasizes 
the effectiveness of the ET model throughout the entire design process, 
highlighting its capability to accurately predict alloy properties. 
5.2. Mechanical properties 
The proposed alloys showed superior high-temperature mechanical 
properties than the other developed heat-resistant aluminum alloys. For 
instance, although the ANTV alloy had the lowest strength among the 
four alloys, its performance was comparable to that of the Al-6Ni-0.4Sc 
(wt. %) alloy, with a UTS of 138 MPa and an elongation of 11 % at 
300 
◦
C [49] . Considering the high cost of Sc, the ANTV alloy was a more 
affordable composition. It had a similar high-temperature strength of 
131 MPa and an enhanced elongation of 22 %, making it an attractive 
alternative in terms of both performance and cost-effectiveness. 
Furthermore, the addition of Ti and V to the Al-5.8Ni alloy results in a 
notable enhancement in strength compared with the Al-6Ni binary near- 
eutectic alloy, which exhibits a strength of 110 MPa at 300 
◦
C. Thus, the 
Fig. 9. SHAP summary plot showing the input ranking by mean SHAP values. 
Table 3 
Comparison of predicted and experimental values. 
Alloy Pred. value / MPa Exp. value / MPa Bias / % 
ANTV 146.1 131.2 ± 2.8 11.3 
ACTV 149.1 152.6 ± 0.3 2.3 
ASTV 149.9 158.4 ± 5.1 5.4 
ASCV 143.8 174.9 ± 6.0 17.8 
J. Huang et al.

## Page 8

Materials & Design 243 (2024) 113057
8
exceptional performance of the proposed alloys is attributed to the 
incorporation of Ti and V. 
Al
10
V intermetallics were present in all the proposed alloys ( Figs. 6 
and 7 ). Therefore, it is reasonable to suggest that the observed 
enhancement in high-temperature strength may be associated with these 
V-rich intermetallics. Typically, intermetallics are considered brittle 
fracture sources that deteriorate the strength and ductility of aluminum 
alloys due to their large size and brittleness, such as Fe-rich in -
termetallics [50,51] . However, the fractographic images reveal that the 
fracture surfaces of four alloys were characterized by ductile fractures 
with dimples morphology, as depicted in Fig. 10 . The microstructure of 
the ASCV alloy before and after the tensile test is shown in Fig. 11 . It can 
be observed that the eutectic Si particles fractured after deformation, 
while the V-rich intermetallics remained intact. This indicates that the 
presence of V-rich intermetallics does not pose a detrimental effect on 
the mechanical properties of aluminum alloys. The underlying reasons 
for this phenomenon can be attributed to three factors. (1) The size of V- 
rich intermetallics in alloys ( Fig. 6 ), which increases in the following 
sequence: ANTV > ASTV > ASCV > ACTV. This variation in size is 
primarily due to the difference in eutectic and peritectic temperatures 
among the alloy components. The Al-Ni eutectic reaction occurs at the 
highest temperature, whereas the Al-Cu reaction occurs at the lowest 
temperature. However, the average dimensions of the V-rich in -
termetallics in all four alloys are consistently below 7 μ m, which is 
considerably smaller compared to Fe-rich intermetallics that exceed 100 
μ m [11] . The small size of intermetallics will not degrade the ductility 
but enhance the mechanical properties [52] . (2) V-rich intermetallics 
had a polyhedral shape, which is considered more favorable than the 
needle-like intermetallic, as they lead to less stress concentration 
[13,53] . (3) V-rich intermetallics were found within the dimples on the 
fracture surface of ASCV alloy, as indicated by red arrows and evidenced 
by EDS mapping in Fig. 12 . Small dimples were observed surrounding 
the V-rich intermetallics, which remained attached to the matrix, sug -
gesting that ductile deformation and good interface bonding can impede 
dislocation movements. Thus, V-rich intermetallics contribute to the 
enhanced high-temperature strength of the proposed aluminum alloys. 
However, the detailed mechanisms underlying the strengthening effect 
of V-rich intermetallics fall outside the scope of this study and are the 
subject of another ongoing research. 
5.3. Feature importance 
Numerous studies have indicated that incorporating additional de -
scriptors can enhance the performance of machine learning models 
[21,54] , which is further corroborated by the results of our study. The 
SHAP value analysis reveals that test temperature and heat treatment 
markedly influence the high-temperature strength of aluminum alloys 
( Fig. 9 ). Obviously, the strength of alloys is greatly affected by its 
microstructure and the ambient temperature, both of which are pre -
dominantly determined by the conditions of heat treatment and testing 
conditions. Then, Cu and Si are the two elements with the highest fre -
quency in the training set because the heat-resistant aluminum alloys 
developed so far are mainly based on Al-Cu and Al-Si alloys. In addition, 
the high SHAP values of Cu in some cases are attributed to some of the 
high Cu alloys (Cu > 20 wt%) in the dataset. These high-Cu alloys 
have excellent high-temperature strength but are not within the scope of 
this study due to their extremely poor castability and ductility. The 
above reasons result in Cu and Si being important in predictions from the 
model. In addition, the four proposed alloys contained Ti and V, and 
their importance is underscored by the SHAP values. This suggests that 
these two elements are the most promising micro-alloying element 
combination for developing heat-resistant aluminum alloys based on the 
model output. The SHAP value summary plots (see Fig. S1 ) and force 
plots ( Fig. S2 ), substantiate these findings, showing that the additions of 
Ti and V particularly enhance the predicted strength significantly more 
than other elements. These insights affirm the critical influence of spe -
cific alloying elements on the high-temperature performance of the 
aluminum alloys. Although the influence of Ti and V on high- 
temperature strength of alloys has been scarcely reported, the excep -
tionally high activation enthalpy and low diffusion rates of Ti and V 
( Fig. 13 ) indicate that these elements are potential candidates for use in 
the next generation of heat-resistant aluminum alloys. The lower 
diffusion rates indicate better thermostability at elevated temperatures 
[55] , which is further substantiated by the excellent high-temperature 
strength of the four alloys. Moreover, elements such as Fe, Zr, and Mn 
show a low diffusivity in the aluminum matrix; therefore, they exert a 
Fig. 10. Fracture surface after high-temperature tensile test for the a ANTV, b ACTV, c ASTV, and d ASCV alloys. 
J. Huang et al.

## Page 9

Materials & Design 243 (2024) 113057
9
moderate impact on the output. 
The three additional descriptors have an influence on the model. The 
variance of modulus and modulus mismatch, indicating the difference in 
the elastic modulus and shear modulus between alloying elements, may 
contribute to the strength of the alloys via modulus mismatch 
strengthening [ 56 ]. Furthermore, the variance of maximum solubility in 
the aluminum matrix is associated with solid solution strengthening and 
precipitation strengthening, which are the two most effective main 
strengthening mechanisms in aluminum alloys. Thus, the inclusion of 
these additional descriptors enriches the information of dataset, 
bridging the gap between machine learning and materials science and 
improving the performance of the machine learning model. 
5.4. Comparison with other studies 
Table 4 compares the high-temperature strengths of alloys designed 
in this study with those reported in the last five years and the alloys from 
the training set [ 57 – 65 ]. The aluminum alloys proposed herein exhibit 
superior performance despite having simpler compositions, which in -
dicates the success of the machine learning-based design approach and 
its potential for application in future studies. 
6. Conclusions 
In this study, for the first time, a machine learning model with the ET 
algorithm was used to successfully design heat-resistant aluminum 
Fig. 11. Microstructures of ASCV alloy a before and b after high-temperature tensile test. The presence of V-rich intermetallics is indicated by red arrows. (For 
interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.) 
Fig. 12. Enlarged view of the fracture surface in ASCV alloy: a secondary electron image, b back scattered electron image and c EDS mapping of V element shows V- 
rich intermetallics (red arrows) located within the dimples. (For interpretation of the references to colour in this figure legend, the reader is referred to the web 
version of this article.) 
Fig. 13. a Activation enthalpy Q of solute elements in α -Al; dashed line indicates the Q for self-diffusion and b diffusivity of elements in α -Al at different temperature; 
dashed line indicates the self-diffusivity of Al. 
J. Huang et al.

## Page 10

Materials & Design 243 (2024) 113057
10
alloys intended for use at elevated temperatures. The results are sum -
marized as follows: 
(1) The ET model was built and enhanced with additional de -
scriptors. Test results showed a low MAE and high R
2
. The four 
alloys proposed by the ET model demonstrated satisfactory 
strength at 300 
◦
C in an as-cast state. The alloy with the best 
mechanical properties achieved a UTS of 175 MPa and an elon -
gation of 16.5 %. 
(2) Microstructural analysis revealed the presence of intermetallics 
in all the alloys, identified as the Al
10
V phase formed through 
peritectic reactions. The observation of fracture surfaces indi -
cated ductile fractures in all alloys. The presence of V-rich in -
termetallics is suggested to play a key role in imparting the alloys 
with an excellent high-temperature strength. 
(3) The SHAP method provided insights into the rationale behind the 
machine learning model. The results revealed test temperature 
and heat treatment as the most significant factors influencing the 
model output. Moreover, Ti and V were deemed beneficial for 
enhancing the high-temperature performance of the aluminum 
alloy. This study introduces a fresh perspective on the develop -
ment of heat-resistant aluminum alloys, and further research in 
this area is currently underway. The incorporation of machine 
learning techniques presents a promising avenue for the devel -
opment of a new generation of advanced, heat-resistant 
aluminum alloys. 
CRediT authorship contribution statement 
Jinxian Huang: Writing – review & editing, Writing – original draft, 
Visualization, Software, Investigation, Funding acquisition, Formal 
analysis, Data curation. Daisuke Ando: Writing – review & editing, 
Visualization, Supervision, Project administration, Methodology, 
Funding acquisition, Data curation, Conceptualization. Yuji Sutou: 
Writing – review & editing, Supervision, Project administration, Fund -
ing acquisition. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Data availability 
Data that support the findings of this report are available from the 
corresponding author upon request. 
Acknowledgements 
This work was supported by JSPS KAKENHI Grant Number 
23KJ0143, 23H01293 and The Light Metal Foundation Inc. (Japan). 
Appendix A. Supplementary data 
Supplementary data to this article can be found online at https://doi. 
org/10.1016/j.matdes.2024.113057 . 
References 
[1] J.C. Williams, E.A. Starke, Progress in structural materials for aerospace systems, 
Acta Mater. 51 (2003) 5775 – 5799 . 
[2] T. Dursun, C. Soutis, Recent developments in advanced aircraft aluminium alloys, 
Mater. Des. 1980 – 2015 (56) (2014) 862 – 871 . 
[3] T. Mahmoudi, A. Parvizi, E. Poursaeidi, A. Rahi, Thermo-mechanical analysis of 
functionally graded wheel-mounted brake disk, J Mech Sci Technol. 29 (2015) 
4197 – 4204 . 
[4] R.A. Michi, A. Plotkowski, A. Shyam, R.R. Dehoff, et al., Towards high-temperature 
applications of aluminium alloys enabled by additive manufacturing, Int. Mater. 
Rev. 1 – 48 (2021) . 
[5] J.K. Zheng, X. Xu, R. Luo, X. Zeng, et al., Degradation of precipitation hardening in 
7075 alloy subject to thermal exposure: A Cs-corrected STEM study, J Alloys 
Compd. 741 (2018) 656 – 660 . 
[6] Q. Li, J. Qin, D. Jiang, D. Yi, et al., Precipitate coarsening and mechanical 
properties in 6082 aluminium alloy during long-term thermal exposure, J Alloys 
Compd. 909 (2022) 164819 . 
[7] Z. Chen, Y. Zhao, Z. Zhang, Theoretical and experimental study of precipitation and 
coarsening kinetics of θ ′ phase in Al – Cu alloy, Vacuum 189 (2021) 110263 . 
[8] H. Xue, C. Yang, F. De Geuser, P. Zhang, et al., Highly stable coherent 
nanoprecipitates via diffusion-dominated solute uptake and interstitial ordering, 
Nat Mater. 22 (2023) 431 – 441 . 
[9] Y.H. Gao, L.F. Cao, C. Yang, J.Y. Zhang, et al., Co-stabilization of θ ′ -Al2Cu and 
Al3Sc precipitates in Sc-microalloyed Al – Cu alloy with enhanced creep resistance, 
Materials Today Nano. 6 (2019) 100035 . 
[10] Q. Lu, J. Wang, H. Li, S. Jin, et al., Synergy of multiple precipitate/matrix interface 
structures for a heat resistant high-strength Al alloy, Nat Commun. 14 (2023) 2959 . 
[11] J. Mathew, G. Remy, M.A. Williams, F. Tang, et al., Effect of Fe Intermetallics on 
Microstructure and Properties of Al-7Si Alloys, JOM 71 (2019) 4362 – 4369 . 
[12] H. Yang, S. Ji, Z. Fan, Effect of heat treatment and Fe content on the microstructure 
and mechanical properties of die-cast Al – Si – Cu alloys, Mater Design. 85 (2015) 
823 – 832 . 
[13] G. Saito, K. Takagi, M. Yoshida, Review on Fe-Based Intermetallic Compounds in 
Al-Si Casting Alloys, Journal of Japan Foundary Engineering Society. 83 (2011) 
47 – 57 . 
[14] Z. Qian, X. Liu, D. Zhao, G. Zhang, Effects of trace Mn addition on the elevated 
temperature tensile strength and microstructure of a low-iron Al – Si piston alloy, 
Mater. Lett. 62 (2008) 2146 – 2149 . 
[15] G. Li, H. Liao, X. Suo, Y. Tang, et al., Cr-induced morphology change of primary 
Mn-rich phase in Al-Si-Cu-Mn heat resistant aluminum alloys and its contribution 
to high temperature strength, Mater. Sci. Eng. A 709 (2018) 90 – 96 . 
[16] H. Liao, H. Xu, Y. Hu, Effect of RE addition on solidification process and high- 
temperature strength of Al 12%Si 4%Cu 1.6%Mn heat-resistant alloy, Trans. 
Nonferrous Met. Soc. Chin. 29 (2019) 1117 – 1126 . 
[17] H.A. Elhadari, H.A. Patel, D.L. Chen, W. Kasprzak, Tensile and fatigue properties of 
a cast aluminum alloy with Ti, Zr and V additions, Mater. Sci. Eng. A 528 (2011) 
8128 – 8138 . 
[18] W. Kasprzak, B.S. Amirkhiz, M. Niewczas, Structure and properties of cast Al – Si 
based alloy with Zr – V – Ti additions and its evaluation of high temperature 
performance, J. Alloys Compd. 595 (2014) 67 – 79 . 
[19] H. Dai, L. Wang, B. Dong, J. Miao, et al., Microstructure and high-temperature 
mechanical properties of new-type heat-resisting aluminum alloy 
Al6.5Cu2Ni0.5Zr0.3Ti0.25V under the T7 condition, Mater Lett. 332 (2023) 
133503 . 
[20] H. Zhang, H. Fu, X. He, C. Wang, et al., Dramatically enhanced combination of 
ultimate tensile strength and electric conductivity of alloys via machine learning 
screening, Acta Mater. 200 (2020) 803 – 810 . 
[21] H. Zhang, H. Fu, S. Zhu, W. Yong, et al., Machine learning assisted composition 
effective design for precipitation strengthened copper alloys, Acta Mater. 215 
(2021) 117118 . 
[22] Z. Rao, P.-Y. Tung, R. Xie, Y. Wei, et al., Machine learning – enabled high-entropy 
alloy discovery, Science 378 (2022) 78 – 85 . 
[23] G. Vazquez, P. Singh, D. Sauceda, R. Couperthwaite, et al., Efficient machine- 
learning model for fast assessment of elastic properties of high-entropy alloys, Acta 
Mater. 232 (2022) 117924 . 
[24] Y. Zhang, C. Wen, C. Wang, S. Antonov, et al., Phase prediction in high entropy 
alloys with a rational selection of materials descriptors and machine learning 
models, Acta Mater. 185 (2020) 528 – 539 . 
[25] T. Zheng, X. Hu, F. He, Q. Wu, et al., Tailoring nanoprecipitates for ultra-strong 
high-entropy alloys via machine learning and prestrain aging, J Mater Sci Technol. 
69 (2021) 156 – 167 . 
Table 4 
Comparison of high-temperature UTS with other studies. 
Alloy UTS at 300 
◦
C (MPa) Reference 
Al-7.05Si-1.4Cu-0.5 V 174.9 ± 6.0 This study 
Al-7.55Si-0.21Ti-0.45 V 158.4 ± 5.1 This study 
Al-5.8Ni-0.24Ti-0.55 V 131.2 ± 2.8 This study 
Al-3.1Cu-0.24Ti-0.65 V 152.6 ± 0.3 This study 
Al-5 Mg-3.5Zn-2Cu-2Ni 100 [57] 
Al-7Si-2Cu-0.35 Mg-0.2Ni-0.2Mn-0.8RE 156 [58] 
Al-5Cu-0.6Mn-1Fe-1.5Ni 152 [59] 
Al-9Cu-6Ce-1Zr-0.45Mn 156 [60] 
Al-5 Mg-1Ca-0.5Sc-0.2Zr-0.5Mn 133 [61] 
Al-11Si-3.5Cu-0.9 Mg-2.1Ni-0.25Ce 147 [62] 
Al-12Ce-1Cu-0.8 Mg 143 [63] 
Al-5Cu-1Mn-0.5Ni 141 [64] 
Al-4Cu-Sb-Mn 131 [65] 
J. Huang et al.

## Page 11

Materials & Design 243 (2024) 113057
11
[26] C. Wen, Y. Zhang, C. Wang, D. Xue, et al., Machine learning assisted design of high 
entropy alloys with desired property, Acta Mater. 170 (2019) 109 – 117 . 
[27] J. Li, Y. Zhang, X. Cao, Q. Zeng, et al., Accelerated discovery of high-strength 
aluminum alloys by machine learning, Communications Materials. 1 (2020) 73 . 
[28] C. Xinyu, Z. Yingbo, L. Jiaheng, C. Hui, Composition design of 7XXX aluminum 
alloys optimizing stress corrosion cracking resistance using machine learning, 
Mater Res Express. 7 (2020) 046506 . 
[29] S. Park, S.H. Kayani, K. Euh, E. Seo, et al., High strength aluminum alloys design 
via explainable artificial intelligence, J Alloys Compd. 903 (2022) 163828 . 
[30] B. Li, Y. Du, Z.S. Zheng, X.C. Ye, et al., Manipulation of mechanical properties of 
7xxx aluminum alloy via a hybrid approach of machine learning and key 
experiments, J. Mater. Res. Technol. 19 (2022) 2483 – 2496 . 
[31] U. Masood Chaudry, K. Hamad, T. Abuhmed, Machine learning-aided design of 
aluminum alloys with high performance, Mater Today Commun. 26 (2021) 
101897 . 
[32] J. Yong-fei, N. Guo-shuai, Y. Yang, D. Yong-bing, et al., Knowledge-aware design of 
high-strength aviation aluminum alloys via machine learning, J. Mater. Res. 
Technol. 24 (2023) 346 – 361 . 
[33] R. Hu, C. Guo, M. Ma, A study on high strength, high plasticity, Non-Heat Treated 
Die-Cast Aluminum Alloy. Materials. 15 (2021) 295 . 
[34] P. Shurkin, T. Akopyan, A. Musin, “ Promising casting aluminum alloys without 
requirement for heat treatment ” in (METAL, 2019), pp. 1210 – 1215. 
[35] M. Pekguleryuz, E. Ozbakir, A.R. Farkoosh, “ Diesel Engine: Applications of 
Aluminum Alloys ” in Encyclopedia of Aluminum and Its Alloys (CRC Press, Boca 
Raton, Ed. 1 (2019) 743 – 762 . 
[36] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, et al. , Scikit-learn: Machine 
Learning in Python. MACHINE LEARNING IN PYTHON. 
[37] P. Geurts, D. Ernst, L. Wehenkel, Extremely randomized trees, Mach Learn. 63 
(2006) 3 – 42 . 
[38] C. E. Rasmussen, C. K. I. Williams, Gaussian processes for machine learning (MIT 
Press, Cambridge, Mass, 2006), Adaptive computation and machine learning . 
[39] C. K. I. Williams, C. E. Rasmussen, Gaussian Processes for Regression. 
[40] GPy, GPy: A Gaussian process framework in python (2012), (available at http:// 
github.com/SheffieldML/GPy). 
[41] T. Chen, C. Guestrin, “ XGBoost: A Scalable Tree Boosting System ” in Proceedings of 
the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data 
Mining (ACM, San Francisco California USA, 2016; https://dl.acm.org/doi/ 
10.1145/2939672.2939785), pp. 785 – 794. 
[42] M. Abadi, P. Barham, J. Chen, Z. Chen, et al. , TensorFlow: A system for large-scale 
machine learning. 
[43] F. Chollet, Keras (2015), (available at https://github.com/fchollet/keras). 
[44] T. Akiba, S. Sano, T. Yanase, T. Ohta, et al. , “ Optuna: A Next-generation 
Hyperparameter Optimization Framework ” in Proceedings of the 25th ACM SIGKDD 
International Conference on Knowledge Discovery & Data Mining (ACM, Anchorage AK 
USA, 2019; https://dl.acm.org/doi/10.1145/3292500.3330701), pp. 2623 – 2631. 
[45] S. Pan, Y. Wang, J. Yu, M. Yang, et al., Accelerated discovery of high-performance 
Cu-Ni-Co-Si alloys through machine learning, Mater Design. 209 (2021) 109929 . 
[46] F. Zhao, C. Lei, Q. Zhao, H. Yang, et al., Predicting the property contour-map and 
optimum composition of Cu-Co-Si alloys via machine learning, Mater Today 
Commun. 30 (2022) 103138 . 
[47] S. M. Lundberg, S.-I. Lee, A Unified Approach to Interpreting Model Predictions. 
[48] J.L. Murray, AI-V (Aluminum-Vanadium), Bull. Alloy Phase Diagr. 10 (1989) 
351 – 357 . 
[49] C. Suwanpreecha, P. Pandee, U. Patakham, New generation of eutectic Al-Ni 
casting alloys for elevated temperature services, Mater. Sci. Eng. A 709 (2018) 
46 – 54 . 
[50] Z. Ma, A.M. Samuel, H.W. Doty, S. Valtierra, et al., Effect of Fe content on the 
fracture behaviour of Al – Si – Cu cast alloys, Mater Design. 57 (2014) 366 – 373 . 
[51] J. Huang, J. Li, C. Li, C. Huang, et al., Elimination of edge cracks and centerline 
segregation of twin-roll cast aluminum strip by ultrasonic melt treatment, J. Mater. 
Res. Technol. 9 (2020) 5034 – 5044 . 
[52] H.D. Merchant, J.G. Morris, D.S. Hodgson, Characterization of intermetallics in 
aluminum alloy 3004, Mater Charact. 25 (1990) 339 – 373 . 
[53] L. Zhang, J. Gao, L.N.W. Damoah, D.G. Robertson, Removal of Iron From 
Aluminum: A Review, Miner. Process. Extr. Metall. Rev. 33 (2012) 99 – 157 . 
[54] Q. Zhao, H. Yang, J. Liu, H. Zhou, et al., Machine learning-assisted discovery of 
strong and conductive Cu alloys: data mining from discarded experiments and 
physical features, Mater Design. 197 (2021) 109248 . 
[55] K.E. Knipling, D.C. Dunand, D.N. Seidman, Criteria for developing castable, creep- 
resistant aluminum-based alloys – A review, Z. Metallkd. 20 (2006) . 
[56] Z. Feng, Y. Zhang, J. Tan, Y. Chen, et al., Large strain hardening of magnesium 
containing in situ nanoparticles, Nanotechnol. Rev. 10 (2021) 1018 – 1030 . 
[57] R. Li, N. Takata, A. Suzuki, M. Kobashi, Design of heat-resistant Al – Mg – Zn – Cu – Ni 
quinary alloy: Controlling intermetallic phases and mechanical performance at 
elevated temperature, Mater. Sci. Eng. A 857 (2022) 144055 . 
[58] X.H. Zhang, G.C. Su, Y.Y. Han, X.H. Ai, et al., A study on the composition 
optimization and mechanical properties of Al – Mg – Si cast alloys, Mater. Sci. Eng. A 
527 (2010) 3852 – 3856 . 
[59] B. Lin, W. Zhang, X. Zheng, Y. Zhao, et al., Developing high performance 
mechanical properties at elevated temperature in squeeze cast Al-Cu-Mn-Fe-Ni 
alloys, Mater Charact 150 (2019) 128 – 137 . 
[60] S. Bahl, A. Plotkowski, K. Sisco, D.N. Leonard, et al., Elevated temperature ductility 
dip in an additively manufactured Al-Cu-Ce alloy, Acta Mater. 220 (2021) 117285 . 
[61] H. Du, S. Zhang, B. Zhang, X. Tao, et al., Ca-modified Al – Mg – Sc alloy with high 
strength at elevated temperatures due to a hierarchical microstructure, J Mater Sci. 
56 (2021) 16145 – 16157 . 
[62] H.Q. Liu, J.C. Pang, M. Wang, S.X. Li, et al., Effect of temperature on the 
mechanical properties of Al – Si – Cu – Mg – Ni – Ce alloy, Mater. Sci. Eng. A 824 (2021) 
141762 . 
[63] Y. Wang, F. Hou, Z. Fu, H. Mao, et al., Microstructure and mechanical properties of 
novel heat-resistant Al-12Ce-xCu-yMg alloy under laser melting, J Alloys Compd. 
924 (2022) 166359 . 
[64] J. Chen, H. Liao, Y. Wu, H. Li, Contributions to high temperature strengthening 
from three types of heat-resistant phases formed during solidification, solution 
treatment and ageing treatment of Al-Cu-Mn-Ni alloys respectively, Mater. Sci. 
Eng. A 772 (2020) 138819 . 
[65] G. Li, H. Liao, J. Zheng, M. Yang, et al., Synergistic effect of joint addition of Sb +
Mn on high temperature strengthening in Al – 4Cu heat-resistant alloy, Mater. Sci. 
Eng. A 851 (2022) 143623 . 
J. Huang et al.
