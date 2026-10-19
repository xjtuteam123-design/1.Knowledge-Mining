# Adv Eng Mater - 2023 - Lu - Data‐Driven  Cross‐Component  Design and Optimization of   ‐Strengthened Co‐Based Superalloys

<!-- source: D:\总文献\Adv Eng Mater - 2023 - Lu - Data‐Driven  Cross‐Component  Design and Optimization of   ‐Strengthened Co‐Based Superalloys.pdf -->
<!-- file_sha256: 8332cc514818d0b4c8d3274d36208f1df7b145ec893abfe052f939f6d8b3eddb -->

## Page 1

Data-Driven “Cross-Component” Design and Optimization
of γ 0-Strengthened Co-Based Superalloys
Song Lu, Min Zou, Xiaorui Zhang, Stoichko Antonov, Wendao Li, Longfei Li,*
and Qiang Feng*
1. Introduction
The discovery of ordered γ 0 precipitates in the system of Co – Al–
W-based alloys paves a new pathway for the development of high-
temperature superalloys applied at high temperatures. [1,2]
Compared to the widely used Ni-based superalloys, the potential
for higher temperature capability is expected
with Co-based superalloys due to the higher
melting temperature of the major matrix
component, Co. [3,4] This is very attractive
for hot-end components in advanced aero-
engines to further improve the fuel ef ﬁ-
ciency and mechanical properties. In
addition, Co-based superalloys usually have
a higher sul ﬁde melting temperature than
Ni-based superalloys, which is bene ﬁcial
for the long-term service in an environment
containing sulfur, such as industrial gas tur-
bines.[4] However, due to the complexity of
the actual service environment, commercial
superalloys need to fulﬁll a variety of physi-
cal and chemical properties simultaneously,
such as creep, fatigue, oxidation, corrosion,
and density, which is done by tailoring the
alloy composition typically comprising more
than nine components. [5]
Until now, the research ofγ0-strengthened
Co-based superalloys has gradually evolved
from exploring alloying principles, consid-
ering individual or multiple elements, [6– 8]
to the optimization of different properties
in an alloy with complex components ( ≥7).[9– 11] Many research-
ers have demonstrated that Ni addition can signi ﬁcantly expand
the γ þ γ 0 phase region,[12,13] which contributes to the tailoring of
the microstructure by the addition of other refractory elements.
Thus, a series of CoNi-based superalloys have been developed in
recent years. Ta, Ti, and Nb improve the γ 0 solvus temperature
(Tγ 0 ) and the temperature capability, [14– 16] while they also pro-
mote the precipitation of TCP phases, which are harmful to
mechanical properties. [17,18] Cr is bene ﬁcial for improving the
oxidation and corrosion resistance, but it reduces the Tγ 0 and area
fraction of γ 0 precipitates (Aγ 0 ).[19,20] Mo, W, and Re provide good
solid solution strengthening effects in Ni-based superalloys with
a negative mis ﬁt( aγ 0 < aγ). In contrast, Mo lowers the mis ﬁto f
γ 0-strengthened Co-based superalloys, which generally exhibit a
positive misﬁt( aγ 0 > aγ), by increasing the lattice constant of the
γ matrix. This normally results in a transition of the γ 0 precipitate
morphology from cuboidal to spherical,[21] which is beneﬁcial for
the microstructural stability during the long-term service pro-
cess. W is the γ 0-forming element in γ 0-strengthened Co-based
superalloys,[22] and its solution effect is lower than that in
Ni-based superalloys. Moreover, the addition of W will greatly
increase the density. Although Re can signi ﬁcantly improve
the creep resistance of Ni-based superalloys by strongly
S. Lu, M. Zou, X. Zhang, W. Li, L. Li, Q. Feng
Beijing Advanced Innovation Center for Materials Genome Engineering
State Key Laboratory for Advanced Metals and Materials
University of Science and Technology Beijing
Beijing 100083, China
E-mail: lilf@skl.ustb.edu.cn; qfeng@skl.ustb.edu.cn
S. Antonov
Department of Microstructure Physics and Alloy Design
Max-Planck-Institut für Eisenforschung GmbH
40237 Düsseldorf, Germany
W. Li
School of Materials Science and Engineering
Xiangtan University
Xiangtan 411105, China
The ORCID identi ﬁcation number(s) for the author(s) of this article
can be found under https://doi.org/10.1002/adem.202201257.
DOI: 10.1002/adem.202201257
The design of complex multicomponent superalloys has always been challenging
due to the interaction of multiple elements and stringent requirements for
various properties. Herein, an integrated approach to designing the high-
component (>7) γ 0-strengthened Co-based superalloys with well-balanced prop-
erties is developed by combining the diffusion multiples and machine-learning
models. A “cross-component” prediction is achieved by the machine-learning
models, where two types of novenary superalloys are screened out for aeroengine
and industrial gas turbine blades, respectively, based on the experimental database
mainly consisting of six to seven elements. The method is veriﬁed to be effective or
slightly more favorable than the Calculation of Phase Diagram (CALPHAD) in
predicting the γ 0 solvus temperature ( Tγ 0 ) and phase constituent of the high-
component alloys when reasonable data of low-component alloys are just provided.
Furthermore, the oxidation resistance and hardness of polycrystal superalloys as
well as the compressive strength of single-crystal superalloys are tested. Finally,
some factors affecting the accuracy of “cross-component” prediction are dis-
cussed. Expanding the compositional range and supplementing the critical
interaction data of multiple elements in the database are bene ﬁcial for improving
the accuracy of the “cross-component” prediction.
RESEARCH ARTICLE
www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (1 of 11) © 2023 Wiley-VCH GmbH

## Page 2

segregating to the γ matrix, lowering the effective diffusion coef-
ﬁcients, and leading to a large lattice distortion, no obvious
improvement of creep property is detected in the γ 0-strengthened
Co-based superalloys containing Re. [23] Thus, it is essential to
understand the synergetic effects of multiple elements when
making compositional optimization of γ 0-strengthened Co-based
superalloys.
In the early days of CoNi-based superalloy research, conven-
tional methods were used to prepare a series of individual alloys
and further screened them by their Tγ 0 , phase constituents, den-
sity, oxidation, and so on. [10,21,24] Due to the limitation of experi-
mental methods and databases, it was dif ﬁcult to realize a
synergistic consideration and optimization of multiple physical
and chemical properties. To accelerate the design process, calcu-
lation methods like density functional theory (DFT) and thermo-
dynamic calculation were applied based on the materials
knowledge. Even so, the DFT calculation of superalloys within
a complex system would consume extended time and be costly.
Thermodynamic calculation can ef ﬁciently navigate the relation-
ship among the complex compositions and some physical prop-
erties, such as the Aγ 0 , Tγ 0 , and phase constituents. But the
accuracy of the Calculation of Phase Diagram (CALPHAD) is
strongly affected by the accuracy and size of the thermodynamic
database. Until now, signi ﬁcant amount of experimental or
simulative works have been performed to improve the effective-
ness of the thermodynamic database, especially for the high-
component alloys. Even so, the CALPHAD method was
ineffective at predicting phase equilibria behavior when Cr is
introduced to Co – Ni– Al– W, as reported by Lass. [25] Similar
results were also reported in the high-component γ 0-strengthened
Co-based superalloys containing W, Ta, Mo, or Nb. [11,25–27] Thus,
it is important to develop a novel approach for ef ﬁciently predict-
ing the complex system ’sp r o p e r t i e s .
Machine learning has been recently introduced into the design
of γ 0-strengthened Co-based superalloys due to the superiority
and high efﬁciency in processing a large amount of multidimen-
sional data. [11,21,27,28] One or more properties have been simul-
taneously considered in these studies. Moreover, all of these
researches show that the prediction accuracy strongly depends
on the quality and quantity of the database, although multiple
algorithms were employed and carefully optimized to build
the machine-learning models. However, it is dif ﬁcult and costly
to produce a large amount of high-quality data using traditional
experimental approaches. Thus, Liu et al. [11] integrated the
composition– microstructure data calculated by the CALPHAD
into the machine-learning model, and predicted the behavior
of some septenary γ 0-strengthened Co-based superalloys.
However, as mentioned the low accuracy of thermodynamic data-
bases, especially around phase boundaries, is still a hurdle and the
deleterious phases precipitated in predicted alloys. Additionally,
experimental databases were also built to predict the Co –Ti– V–
X[29] or CoNi-based alloy systems[27] based on the individual tradi-
tional experimental approaches and published results. This
has been veri ﬁed to be available for the quick search for the
γ 0-strengthened Co-based superalloys with high Tγ 0 .H o w e v e r ,
large deviations were exhibited in the machine-learning predic-
tions of phase constituents and Aγ 0 .[11,27,30] All the methods men-
tioned above cannot compensate for the insuf ﬁcient high-quality
data. Thus, the prediction is normally carried out within a selected
database to ﬁnd a local maximum or minimum.[31] It is difﬁcult to
extrapolate outside the database, let alone perform the“cross-com-
ponent” prediction, wherein the prediction has higher compo-
nents than the alloys in the database. In fact, the “black box” in
machine-learning models also involves calculations, which may
not be understandable, of the synergetic effects of multiple ele-
ments. As such, it is theoretically possible for the machine-learn-
ing model to make a “cross-component” prediction, when the
database is accurate enough and the correct algorithms are
selected and trained properly.
Multicomponent diffusion multiple is a high-throughput exper-
imental method, which can quickly obtain a large amount of quan-
titative experimental data in a wide range of compositions. [32,33]
Moreover, compared to the underpopulated CALPHAD databases,
the diffusion multiples have an obvious advantage in determining
the phase boundaries inγ0-strengthened Co-based superalloys. The
high accuracy of experimental data around the phase boundaries
can also be used to supplement the CALPHAD databases, as
reported in our previous works. [26,34] Therefore, it is expected to
improve the accuracy of prediction within the database and allow
for “cross-component” predictions by integrating the diffusion mul-
tiple with the machine-learning model.
In this study, a large database on the relationship between the
compositions and microstructures was established by two mul-
ticomponent diffusion multiples. Additionally, some data,
including the microstructure and Tγ 0 , were obtained from indi-
vidual experiments in our previous works and related literature.
Subsequently, a machine-learning framework was constructed to
perform “cross-component” predictions of γ 0-strengthened Co-
based superalloys containing up to nine elements, based on
domain knowledge-driven empirical design criteria for the aero-
engines and industrial gas turbines. Polycrystal and single-crystal
alloys were produced to verify some critical physical and
chemical properties. Optimization strategies for the “diffusion-
multiple þ machine-learning” method are further proposed
based on the experimental results of the prediction superalloys.
This work will be signi ﬁcant for accelerating the development of
alloys with complex components.
2. Results and Discussions
2.1. Work ﬂow of Machine-Learning Strategy
The upper temperature capability strongly depends on the Tγ 0 ,
i.e., γ 0 strengthening is provided below this temperature. In addi-
tion, the microstructural stability (phase constituent) and Aγ 0 at
the service temperature are the critical parameters affecting the
mechanical performance, viz., tensile/compressive, creep, and
fatigue properties. Therefore, the above three fundamental phys-
ical properties/parameters are mainly optimized in this study.
Figure 1 shows the work ﬂow of multiperformance optimiza-
tion for γ 0-strengthened Co-based superalloys by integrating
experimental data and machine-learning models. First, a large
experimental database consisting of the relationship among
the alloy composition with the phase constituents, Tγ 0 , and Aγ 0
was established. The data for the phase constituent and Aγ 0
mainly come from the diffusion multiples (data set), individual
experimental alloys (single data) of our group, and published
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (2 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

literature. In contrast, the data of Tγ 0 were mainly obtained
through individual experiments from our previous works and
other published results. It should be noted that all data in the data-
base come from γ 0-strengthened Co-based superalloys with eight
or less components, and most of them consist of six to seven ele-
ments. This will be further detailed in the following sections.
A classiﬁcation model was applied to predict the output values
of phase constituent: “0” for γ single phase, “1” for γ/γ 0 two-
phase microstructure, and “2” denoting the existence of detri-
mental phases. A regression model was used to predict a
numeric outcome ( Tγ 0 and Aγ 0 ) of the input alloy composition.
After that, several widely used machine-learning algorithms were
further screened out by the exhaustive method to determine the
optimal algorithm for the investigated composition – physical
properties (phase constituents, Tγ 0 , and Aγ 0 ) relationships.
Random forest (RF), XGBoost (eXtreme Gradient Boosting, also
known as GBDT), deep neural network (DNN), k-nearest neigh-
bor (k-NN), and logistic regression (LR) algorithms were employed
to build the phase constituent classiﬁcation model, and the validity
was evaluated by the value of macro-F1.[35] Linear regressions (Lin),
RF, GBDT, DNN, and Support Vector Regression (SVR) with a
radial basis function kernel were applied to build the Tγ 0 and
the Aγ 0 regression models, and the validity was evaluated by
the value of the root-mean-square error (RMSE) and the explained
variance (R2).
RMSE ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
1
n
Xn
i¼1
ðYact /C0 YpreÞ2
s
(1)
R2 ¼ 1 /C0
Pn
i¼1 ðYact /C0 YpreÞ2
Pn
i¼1 ðYact /C0 YaveÞ2 (2)
where Yact is the true value, Ypre is the predicted value, Yave is the
average of Yact,a n d n is the number of the predicted data in the
dataset. The responses of macro- F1 and R2 range from 0 to 1,
where the better the model performance, the closer the value is
to 1, and the RMSE value is smaller. Models were adjusted until
the optimal model performance was obtained. [11,21] Then, the
models were employed to predict the phase constituent, Tγ 0 ,
and Aγ 0 after the elements (up to nine) of γ 0-strengthened
Co-based superalloys were input. Finally, several objective alloy
compositions were screened out based on the design criteria
for different types of superalloys, and the reliability of the model
was evaluated by systematic experiment investigations.
2.1.1. Diffusion Multiple and Design Criteria
Figure 2 exhibits the schematic of two multicomponent diffusion
multiples and the quantitative relationship between composi-
tions and microstructures. The ﬁrst diffusion multiple shown
in Figure 2a was used for the ﬁrst-round alloy screening based
on the microstructure. The base alloy1 was determined by our
previous works on the single-crystal Co – Al– W-based superalloy
(Co– 7Al– 8W– 4Ti– 1Ta (at%)), which has a comparable creep
resistance with ﬁrst-generation Ni-based single-crystal superal-
loys.[36,37] Subsequently, Ni was added to expand the γ þ γ 0 phase
region. The Co – 20Ni– 7Al– 8W– 4Ti– 1Ta (at%) alloy was selected
as the base alloy to further tailor other elements considering the
microstructural stability (Ni, W), creep resistance (Ti, Ta, Mo,
Nb), density (Al) and oxidation resistance (Cr). Of note is that
the maximum number of components is 7 in this diffusion mul-
tiple. Combined with the ﬁrst diffusion multiple, some individ-
ual tests were performed to further verify the microstructural
stability and oxidation resistance of the screened alloys. Then,
a single-crystal superalloy (Co – 30Ni– 11Al– 4W– 4Ti– 1Ta– 5Cr
(at%)) was obtained with a good combination of density, creep,
and oxidation resistance. [38] To further optimize the microstruc-
tural stability and oxidation resistance, the individual effects of
Al, Cr, Ti, Ta, Mo, and Ni on base alloy2 (Co – 30Ni– 11Al– 4W–
2Ti– 1Ta– 5Cr (at%)) were investigated with a second diffusion
multiple, and the maximum component is 8 (Figure 2b).
Additionally, the interaction of two or three elements can be
investigated by analyzing the diffusion couples around the base
alloy2, such as þ2Ta– þ2Mo and þ10Ni– þ2Ti. Figure 2c shows
the typical microstructural evolution with the variation in the
concentrations of Mo and Ta in the þ2Mo– þ2Ta diffusion cou-
ple after being annealed at 1000 °C for 1000 h. The cerulean and
purple circles present the variation of Mo and Ta contents,
Figure 1. Workﬂow of multiperformance optimization for γ 0-strengthened Co-based superalloys by integrating experimental data and machine-learning
models.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (3 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

respectively. The γ/γ 0 microstructure was observed throughout
the þ2Mo– þ2Ta diffusion couple. The morphology of γ 0 precip-
itates changes from being more spherical to being more angular or
cuboidal (viewed from other crystallographic directions, not
shown here) with the increase of Ta (1 !3 at%) and simultaneous
decrease of Mo (2 !0 at%). Meanwhile, the Aγ 0 was measured to
increase from the alloy þ2Mo ( /C25 80%) to þ2Ta ( /C25 87%)
(Figure S1, Supporting Information). Accordingly, 81 datasets
of the phase constituent and the Aγ 0 associated with compositions
were obtained from each diffusion couple. Thus, by integrating
the two diffusion couples and references, [21,39–45] 2275 datasets
were provided for the phase constituent and Aγ 0 models men-
tioned in Figure 1. For the Tγ 0 model, 238 datasets were collected
from references[9,11,13,25,40,46–53] and our individual experiments.
As mentioned in Figure 1, the ﬁnal database was established
by integrating the dataset from the diffusion multiples (phase
constituents, Aγ 0 ) and independent data from individual experi-
ments (Tγ 0 , phase constituents, Aγ 0 ). Different machine-learning
models were applied to the aforementioned three types of data.
Moreover, the validity was evaluated and optimized by the value
of macro- F1 (phase constituent classi ﬁcation models), RMSE,
and R2 (Tγ 0 and Aγ 0 regression models). Among the eight typical
algorithms introduced in Figure 1, the GBDT algorithm had the
best performance for predicting the phase constituents, Tγ 0 , and
Aγ 0 of the new γ 0-strengthened Co-based superalloys with a num-
ber of components up to 9 (details of values macro- F1, RMSE,
and R2 for each model are shown in Figure S2, Supporting
Information).
Besides the Tγ 0 , phase constituent, and Aγ 0 , additional proper-
ties like density and oxidation resistance need to be considered
due to the requirements for different service environments. As
such, combined with the domain knowledge and experience, two
types of design criteria of superalloys were set for aeroengine and
industrial gas turbine blades, respectively, as shown in Table 1 .
For the aeroengine, the superalloys generally work at a higher
temperature (1000 – 1100 °C) than the industrial gas turbine
(900– 1000 °C). Thus, higher Tγ 0 (≥1190 °C), good microstruc-
tural stability ( γ þ γ 0), and Aγ 0 (70– 80%) at 1000 °C were prelimi-
nary set based on the existing experience. [54,55] The above three
fundamental physical properties/parameters were predicted by
the corresponding machine-learning models. The design criteria
for density and oxidation resistance were set as <8.8 g cm/C0 3, cal-
culated by the empirical formula, and Al þ Cr ≥ 16 at% based on
our previous experience.[19,56] Similarly, the design criteria of Tγ 0 ,
phase constituent, Aγ 0 , density as well as oxidation resistance for
the superalloys in industrial gas turbine blades [57– 59] were also
listed, respectively, in Table 1. Moreover, an additional criterion
of high Cr content ( ≥12 at%) was proposed to meet the require-
ment for the corrosion environment in industrial gas turbines.
According to the above criteria and microstructure results in
the database, the search space of superalloys in the aeroengines,
CoaNibAlcWdTieTafCrgMohNbi (at%), was determined as follows:
26% ≤ b ≤ 32%, 8% ≤ c ≤ 13%, 1% ≤ d ≤ 4%, 1% ≤ e ≤ 4%,
1% ≤ f ≤ 4%, 4% ≤ g ≤ 8%, 0% ≤ h ≤ 1.5%, 0% ≤ i ≤ 1.5%,
a > b, c þ g ≥ 16, and a þ b þ c þ d þ e þ f þ g þ h þ i = 100%.
A composition variation step of 1 at% was set for c – g, 2 at%
for b, and 0.5 at% for h – i, which results in a total of 81 920 can-
didates containing up to nine elements. In contrast, the search
space of the industrial gas turbine superalloys is characterized by
the lower and upper limits of Al and Cr content (6% ≤ Al ≤ 11%,
Figure 2. Schematic of two multicomponent diffusion multiples and the quantitative relationship between compositions and microstructures. Diffusion
multiple used for the a) ﬁrst and b) second rounds of the alloy screening. c) Typical microstructural evolution with the variation of the concentrations of
Mo and Ta in the þ2Mo–þ2Ta diffusion couple after being annealed at 1000 °C for 1000 h.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (4 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

12% ≤ Cr ≤ 16%). The search space for other elements and com-
position variation step are the same as the aeroengine, which
gives a total of 122 880 candidates to be explored.
2.2. Experimental Veri ﬁcation
Based on the machine-learning models and design criteria, a
total of 183 and 238 candidate alloys were screened out for
the aeroengines and industrial gas turbines, respectively. To fur-
ther guarantee microstructural stability, objective alloys with a
higher Tγ 0 and lower density were further screened with the
Pareto frontier method. Table 2 lists the nominal compositions
of four novenary alloys, where alloys 9CoNi-A and 9CoNi-B were
designed for the aeroengines, while alloys 9CoNi-C and 9CoNi-D
for the industrial gas turbines.
2.2.1. Microstructural Stability
Figure 3 shows the scanning electron microscopy images of
microstructures in the four novenary alloys after aging at differ-
ent temperatures and hours. Both alloys 9CoNi-A and 9CoNi-B
remain γ/γ 0 microstructure after aging at 1000 °C/500 h, and no
detrimental phases were observed, as shown in Figure 3a,b,
respectively. The morphology of γ 0 precipitates was cuboidal with
an equivalent diameter ( Dγ 0 ) of 877 /C6 266 nm in alloy 9CoNi-A,
while in alloy 9CoNi-B, it was transformed into rounded-edge
rectangles through a coarsening and connecting process.
Thus, the Dγ 0 was not calculated due to the irregular shape of
γ 0 precipitates. The Aγ 0 of alloy 9CoNi-A (73.8 /C6 1.2%) is higher
than that of alloy 9CoNi-B (53.5 /C6 3.2%), which is lower than the
value set by the design criterion (70 – 80%) for the aeroengines
(Table 1). The industrial gas turbine alloys 9CoNi-C and
9CoNi-D keep typical the γ/γ 0 microstructure after aging at
950 °C/600 h, and the corners of the γ 0 precipitates are smooth.
The Aγ 0 of alloys 9CoNi-C and 9CoNi-D were measured to be
51.1 /C6 0.5% and 57.4 /C6 0.8%, respectively. No noticeable
difference of Dγ 0 was found between alloys 9CoNi-C
(373 /C6 86 nm) and 9CoNi-D (388 /C6 80 nm).
2.2.2. Oxidation and Mechanical Properties
Figure 4 shows the oxidation and mechanical properties of the
predicted novenary alloys. The oxidation weight gain shown in
Figure 4a indicates that all four novenary alloys have better oxi-
dation resistance than the Cr-free γ 0-strengthened Co-based
superalloys with a fewer components after 1000 °C/100 h. The
weight gain of the four novenary alloys decreases in the order
of 9CoNi-C > 9CoNi-A > 9CoNi-D/C25 9CoNi-B. The oxidation
resistance of alloys 9CoNi-B and 9CoNi-D is close to that of typi-
cal Ni-based superalloys CMSX-4 and CMSX-6. The oxidation
behavior strongly depends on the interaction of Al and Cr, which
has been studied and shown in our previous works. [19,56] The
Vickers hardness of the four novenary alloys at room tempera-
ture increases in the order of 9CoNi-A < 9CoNi-B < 9CoNi-
C < 9CoNi-D, as shown in Figure 4b. Interestingly, the variation
of Vickers hardness seems to not be closely related to the Aγ 0 . For
example, although the alloy 9CoNi-A has the highest Aγ 0 among
the four novenary alloys, its Vickers hardness is lower than the
other three alloys. In contrast, for the industrial gas turbine alloys
9CoNi-C and 9CoNi-D, the variation of Vickers hardness is posi-
tively correlated with the Aγ 0 . This will be further discussed in the
following sections.
Figure 4c shows 0.2% ﬂow stress curves as a function of tem-
perature for single-crystal alloys 9CoNi-A and 9CoNi-D, together
with other single-crystal CoNi-based alloys with fewer compo-
nents (≤6)[53,60] and Co – Al– W-based alloy. [40] In the whole tem-
perature range, the ﬂow stresses of alloy 9CoNi-D are higher than
that of 9CoNi-A. Alloy 9CoNi-A presents an anomalous yield
behavior and has a higher or comparable yield strength at
800 °C compared to the CoNi- and Co – Al– W-based alloys with
high W content ( ≥4 at%). Above 800 °C, its ﬂow stress decreases
rapidly as it does for other CoNi- and Co – Al– W-based alloys. In
contrast, with the increase of temperature, the ﬂow stresses of
alloy 9CoNi-D decrease without the anomalous yield behavior.
Even so, the alloy 9CoNi-D shows higher ﬂow stresses at temper-
atures below 800 °C than other reported CoNi- or Co – Al– W-
based alloys.
2.3. Comparison between Machine-Learning and CALPHAD
The synergetic effects of multiple elements have always been one
of the key issues for the design of superalloys. The rapid and
accurate establishment of a quantitative relationship between
Table 1. Two types of design criteria of superalloys set for the aeroengine and industrial gas turbine blades based on the existing experience, respectively.
Property Aeroengine Industrial gas turbine
γ 0 Solvus temperature [°C] ≥1190 ≥1100 Machine learning
Phase constituent at 1000 °C γ þ γ 0 γ þ γ 0 Machine learning
γ 0 Area fraction at 1000 °C 70 – 80% 60 – 70% Machine learning
Density [g cm /C0 3] <8.8 <9 Empirical
Oxidation [at%] Al þ Cr ≥ 16 Al þ Cr ≥ 16, Cr ≥ 12 Empirical
Table 2. Nominal compositions of four novenary alloys designed for the
aeroengines and industrial gas turbines, respectively (at%).
Alloy Co Ni Al W Ti Ta Cr Mo Nb
Aeroengine 9CoNi-A Bal. 32 12 2 1 3 4 0.5 0.5
9CoNi-B Bal. 32 10 2 2 3 7 0.5 0.5
Industrial gas turbine 9CoNi-C Bal. 32 7 3 3 1.5 14 0.5 0.5
9CoNi-D Bal. 32 9 2 2 3 12 0.5 0.5
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (5 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

multiple elements and microstructure will greatly accelerate the
development of new alloys. Therefore, many researches have
been done to build thermodynamic and kinetic databases of
γ 0-strengthened Co-based superalloys. [61,62] Moreover, some
CoNi-based superalloys with good microstructural stability and
mechanical properties have been developed through the
CALPHAD.[11,13] Even so, due to the complexity of the synergetic
effects of multiple elements, the existing CALPHAD cannot
Figure 3. Scanning electron microscopy images of microstructures in four novenary alloys after aging at different temperatures and hours. a) 9CoNi-A at
1000 °C/500 h; b) 9CoNi-B at 1000 °C/500 h; c) 9CoNi-C at 950 °C/600 h; d) 9CoNi-C at 950 °C/600 h.
Figure 4. The oxidation and mechanical properties of four novenary alloys. a) Comparison of oxidation weight gains between γ 0-strengthened Co-based
and Ni-based superalloys after 1000 °C/100 h; b) Vickers hardness and the corresponding Aγ 0 ; c) 0.2% ﬂow stress curves as a function of temperature for
single-crystal alloys 9CoNi-A and 9CoNi-D, together with other single-crystal CoNi-based alloys with lower components ( ≤6)[46,60] and Co–Al–W-based
alloy.[40]
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (6 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

effectively predict all the microstructural properties, especially
for the ( γ þ γ 0)/(γ þ γ 0þTCP) phase boundaries in multicompo-
nent alloys.[26] Compared with the CALPHAD, multicomponent
diffusion multiples can quickly obtain experimental data for the
composition and corresponding microstructure. This brings an
advantage in determining the phase boundaries of an alloy sys-
tem.[26,34] The machine-learning method can establish the digital
or functional relationship among multiple elements, microstruc-
tures, and properties. However, its extrapolation is limited due to
the lack of an understandable physical metallurgy principle. In
addition, high-quality data are required during the model training
process to ensure the accuracy of predictions. Therefore, com-
bined with the large high-quality experimental database provided
by the multicomponent diffusion multiple, it is expected to signif-
icantly improve the accuracy of machine-learning predictions.
Figure 5 shows the pseudo-ternary isothermal section of alloy
Co– Al– W– 20Ni– 1Ta– 4Ti (at%) calculated by phase diagram at
1000 °C and a comparison between the experimental data from
the diffusion multiples and the predicted data by the machine-
learning model. The CALPHAD result shows that four phase
regions, including γ, γ þ γ 0, γ þ γ 0 þ β, and γ þ β, exist in the
composition range of 7% ≤ Al ≤ 15%, 0% ≤ W ≤ 8% (at%).
The γ/γ þ γ 0 phase boundary is similar between the experimental
data and CALPHAD. However, there exists an apparent deviation
(/C25 2 at%) for the γ þ γ 0/γ þ γ 0 þ β boundary, as shown in
Figure 5a. In contrast, the machine-learning prediction results
(Figure 5b) show a better ﬁtness with the actual experimental
results (Figure 5a) than the CALPHAD. Thus, it can be summa-
rized that the machine-learning model based on the experimen-
tal data is more accurate than CALPHAD in predicting the phase
constituent, especially when the phase boundary is contained.
Besides the prediction of phase constituent, taking advantage
of experimental data, the machine-learning model also has
higher accuracy than CALPHAD when predicting the Tγ 0 and
Aγ 0 in the database (not shown in this study).
Despite high-accuracy databases, the limited extrapolation
out of the database has always been a critical issue for machine-
learning models. To solve this problem, additional key experimen-
tal tests are generally performed and fed into the database, and
then the machine-learning models are retrained.[11,27,29] As i m i l a r
process will be repeated until an acceptable predicted result is
obtained. For example, the range of A element in a database of
the machine-learning models is 0– 10 at%. It is dif ﬁcult to ensure
good accuracy for predicting the alloys with a content of 10– 20 at%
A unless the supplement of extra experimental data, like alloys
with ≥20 at%A, into the previous database. Meanwhile, to avoid
overﬁtting, some experimental data of alloys with 10 –20 at%A
are also required.
2.4. “Cross-Component” Prediction from Low- to
High-Component γ 0-Strengthened Co-Based Superalloys
Based on the aforementioned principles, the alloys in the data-
base and predictions of the machine-learning models typically
contain the same number of components. Thus, it seems impos-
sible to make a “cross-component” prediction, in which the
high-component alloys are predicted based on data from the
low-component alloys in the database. However, the volume
of extra experiments may be unacceptable because of the com-
plexity of the synergetic effects of multiple elements, especially
for the prediction of high-component ( >7) alloys. Moreover, it is
difﬁcult for researchers to handle the data about simultaneous
variations of complex elements. On the other hand, the predic-
tion results of CALPHAD or “CALPHAD þ machine learning ”
strongly depend on the accuracy of built-in thermodynamic data-
bases, which are uncertain or unavailable for γ 0-strengthened Co-
based superalloys with high components ( >7) for now. [11]
2.4.1. Feasibility of “Diffusion-Multiple þ Machine-Learning”
method to Make “Cross-Component” Prediction
The diffusion multiple has a unique advantage in establishing
the experimental database. Theoretically, any synergetic effects
of multiple elements can be easily obtained by designing the cor-
responding diffusion couples. Thus, it is ideal for the combina-
tion of diffusion-multiple and machine-learning models to
improve the reliability of prediction for the high-component
Figure 5. The pseudo-ternary isothermal section of alloy Co – Al–W–20Ni– 1Ta–4Ti (at%) calculated by phase diagram at 1000 °C and a comparison
between a) the experimental data from the diffusion multiples and b) the predicted data by the machine-learning model.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (7 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

γ 0-strengthened Co-based superalloys. In addition, to make full
use of the advantage of machine learning in processing multidi-
mensional data and reduce the costs of experiments, in the cur-
rent research, the high-precision experimental data provided by
the diffusion multiple mainly came from alloys with six to seven
components. All the elements of the novenary alloys shown in
Table 2 are contained by overlapping two or more diffusion cou-
ples, thus realizing a “pseudo-coverage” to meet the principle of
machine-learning prediction. Therefore, novenary alloys can be
predicated by simulating or ﬁtting the synergetic effects of mul-
tiple elements using machine-learning models.
In this study, the four novenary alloys shown in Table 2 have a
γ þ γ 0 conﬁguration at 950 – 1000 °C and good oxidation resis-
tance at 1000 °C. These mean a good accuracy in the phase con-
stituent prediction and validity of the criterion set for the
oxidation property (Table 1). Figure 6 shows the comparisons
of Tγ 0 and Aγ 0 values among the CALPHAD, machine-learning
(MC), and experimental (TEST) results of four novenary super-
alloys. In terms of the Tγ 0 , the machine-learning results show
comparable or slightly higher accuracy than CALPHAD, as
shown in Figure 6a. The absolute deviations of Tγ 0 between
the machine-learning and experimental results are lower than
20 °C, while the minimum deviation of CALPHAD results is
24 °C for alloys 9CoNi-A, 9CoNi-B, and 9CoNi-C. For the Tγ 0
of alloy 9CoNi-D, both methods show a lower accuracy, a devia-
tion larger than 30 °C compared to the experimental value.
The Aγ 0 results of the four novenary alloys shown in Figure 6b
indicate that the trends predicted by the two methods are similar
to the variation of experimental values. At the same time, their
prediction accuracy is different. The machine-learning result of
alloy 9CoNi-A is comparable or slightly closer to the experimental
value than the CALPHAD. On the contrary, CALPHAD tends to
be favorable for the other three novenary alloys. However, all the
experimental Aγ 0 values of alloys 9CoNi-B, 9CoNi-C, and 9CoNi-
D are lower than the design criteria shown in Table 1. This is
closely related to the database used for the Aγ 0 prediction. The
diffusion couples shown in Figure 2a,b mainly ( >80%) have a
lower Cr content ( ≤6 at%). As such, the database for the
machine-learning model is suf ﬁcient to make a good “cross-
component” prediction on the Aγ 0 of alloy 9CoNi-A with 4 at
%Cr. In contrast, the machine learning predicts the Aγ 0 of alloys
9CoNi-B– D( 7– 14 at%Cr) with a large deviation due to the lack of
Aγ 0 data with high Cr content. In contrast, the thermodynamic
database-dependent CALPHAD is equipped with simulation data
from high to low Cr contents. Although it is not enough to give a
high-precise prediction, the trend is still meaningful for the
design of novel alloys, especially when no experimental data
are available.
2.4.2. Features of “Diffusion-Multiple þ Machine-Learning”
Method
Based on the above comparison, it can be summarized that the
accuracy of the “diffusion-multiple þ machine-learning” method
strongly depends on the experimental data. Although all the indi-
vidual diffusion couples have been combined to improve the
“cross-component” predictable capability, a compositional
boundary still exists. The prediction accuracy near or outside
the boundary decreases rapidly, such as alloys 9CoNi-B – D.
Even so, it should be noted that the aforementioned composition
range is in the alloys with fewer components (6 – 7), not the nove-
nary alloys. The prediction results of alloy 9CoNi-A have proved
the feasibility for the “cross-component” prediction by the
“diffusion-multiple þ machine-learning” method based on a
large number of high-quality experimental data and searching
for the candidates that match the designing criteria. Additionally,
as discussed in Figure 5, the diffusion couple has the advantage
of determining the ( γ þ γ0)/(γ þ γ0þdetrimental phase) boundary
more accurately than the CALPHAD method, which is highly
important for the design of high-component alloys. This has
been further evidenced by a design process based on the
“CALPHADþ machine-learning” method in our previous work,
where most predicted seven-component alloys precipitated the det-
rimental phases due to the low accuracy of the phase boundaries
only using thermodynamic calculation data.[11] For the prediction of
Aγ0 s h o w ni nF i g u r e6 b ,t h e“diffusion-multipleþ machine-learn-
ing” method shows a lower accuracy than the CALPHAD and only
maintains a trend prediction. However, it should be noted that
building the thermodynamic database is a giant project, especially
for the high-component alloy with refractory elements. Many ther-
modynamic parameters, such as Gibbs free energy, entropy, and
enthalpy, are required to obtain a reasonable accuracy. Moreover,
for different thermodynamic databases and objective alloy systems,
the deviation between the experimental and prediction results may
be unacceptable. In this study, besides the advantage in determin-
ing phase boundaries, the“diffusion-multipleþ machine-learning”
Figure 6. Comparison of a) Tγ 0 and b) Aγ 0 values among the CALPHAD, machine-learning, and experimental results of four novenary γ 0-strengthened Co-
based superalloys.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (8 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

method is mainly constructed from multiple algorithms, which can
rapidly build the mapping relation between multiple elements and
thermodynamic properties based on the suf ﬁcient experimental
dataset instead of the sluggish calculation for the fundamental
thermodynamic parameters from numerous low-component
alloys. Complex synergetic effects of multiple elements can be pre-
dicted by machine-learning algorithms, and optimal selections
can be screened based on the existing experimental results. This
has been veri ﬁed to be feasible for designing novel alloy
systems[27,29,30] or widely reported Ni-based superalloys. [28]
Even so, some critical issues still need to be pointed out for the
“cross-component” prediction method in this study. 1) Similar to
the other machine-learning method, the quality and quantity of
data are the most critical factors for prediction accuracy. 2) The
composition of predicted alloys should be included within the
composition range of the database as far as possible, especially
for the elements having a signi ﬁcant impact on the microstruc-
ture and properties, such as Cr. 3) Compared with CALPHAD,
the predictions beyond the scope of the database and the inter-
action between multiple elements are the key problems for the
machine-learning method. Making full use of the advantage of
diffusion multiples and supplementing the critical experimental
data of the low-component alloys should be a solution to improve
the accuracy and capability of “cross-component” prediction. For
example, only four novenary alloys are veri ﬁed in this study, and
the content of Mo and Nb may be too low to affect the phase
constituent of the novenary alloy. Therefore, the supplementary
data containing both Mo and Nb elements will be helpful to
improve the validity of machine-learning models for predicting
the existing four novenary alloys and the high-component alloys
with higher Mo and Nb contents in the future. Moreover, the
advantage of the diffusion couple in predicting the detrimental
phase boundaries will be more critical when more or higher con-
tent of refractory elements are considered in the design criteria. A
large number of alloys with lower Cr contents in the diffusion
multiple contribute to the high prediction accuracy for the alloy
9CoNi-A. For the other three alloys, it is expected to be able to
improve the performance of the machine-learning model for
the Aγ 0 by supplementing the database with more data of high
Cr alloys.
2.5. Relationship between the Composition and Mechanical
Properties
Vickers hardness and compressive strength are two important
and widely studied mechanical properties, which can be easily
obtained and re ﬂect other mechanical performances of superal-
loys to a certain extent. They represent a comprehensive effect of
various strengthening mechanisms in the alloy, such as solution
and precipitation. [28] Thus, it can sometimes be used as one of
the criteria for evaluating superalloys. The strengthening of γ 0
precipitation is one of the most important strengthening mech-
anisms in superalloys. To improve its stability, how to expand the
γ þ γ 0 phase region and improve the Tγ 0 have always been the key
issues for the development of γ0-strengthened Co-based superal-
loys. Combined with the results in this study, during the design
process of alloys 9CoNi-A and 9CoNi-B, higherTγ 0 is demanded to
obtain a higher Aγ 0 at high temperatures. In contrast, for alloys
9CoNi-C and 9CoNi-D, the corrosion resistance seems to be more
important than the Tγ 0 due to the severe corrosion environment
and lower service temperature than the aeroengines. Thus, a high
Cr content (>12 at%) is set as the design criterion of industrial gas
turbine alloys (Table 1). In addition, the effect of solution strength-
ening is also a critical factor that cannot be neglected. As shown in
Figure 4b, although the Aγ 0 of alloy 9CoNi-A (/C25 70%) is obviously
higher than that of 9CoNi-B ( /C25 58%), the variation of Vickers
hardness shows the opposite trend. This can be ascribed to the
comprehensive effect between the solution and precipitation
strengthening. In terms of composition, the alloy 9CoNi-B is dif-
ferent from alloy 9CoNi-A by the lower Al þ Ti and higher Cr con-
tents. The former contributes to the precipitation strengthening
effect as γ 0-forming elements, while the latter enhances the solu-
tion strengthening of the matrix, due to the larger atomic radius
compared to Co, and decreases the Aγ 0 . Therefore, the effect of
solution strengthening is more dominant on the Vickers hardness
than the γ 0 precipitation for alloys 9CoNi-A and 9CoNi-B. In
contrast, the precipitation strengthening seems to be dominant
for the Vickers hardness of alloys 9CoNi-C and 9CoNi-D.
Although the solution strengthening elements in alloy 9CoNi-C
(W þ Mo þ Cr = 17.5 at%) is higher than that in alloy 9CoNi-D
(14.5 at%), the Vickers hardness of alloy 9CoNi-D (HV = /C25 414)
with a higher Aγ 0 (/C25 62%) was slightly higher than that of
alloy 9CoNi-C ( Aγ 0 = /C25 52%, HV = /C25 395). Indeed, for the
four novenary alloys, the variation of Vickers hardness is
more related to the sum of solution strengthening elements in
order of 9CoNi-A W þ Mo þ Cr = 6.5 at% < 9CoNi-BWþMoþCr=9.5 at%
< 9CoNi-CW þ Mo þ Cr = 14.5 at% < 9CoNi-DW þ Mo þ Cr = 17.5 at%.A
similar trend was also observed when comparing the compressive
ﬂow stress of alloys 9CoNi-A and 9CoNi-D (Figure 4c). Especially,
the solution strengthening effect plays a more critical role than the
Aγ 0 at the temperatures below 800 °C. While at higher tempera-
tures ( >800 °C), the in ﬂuence of precipitation strengthening on
the mechanical property increases and the deviation of ﬂow stress
between the alloys 9CoNi-A and 9CoNi-D decreases.
Based on the relationship between the content of solution
strengthening elements, Aγ 0 , Vickers hardness, and compressive
property, to obtain good mechanical properties, the solution
strengthening effect should also be contained in the design cri-
teria besides the Aγ 0 . For example, the impact of solution
strengthening in alloy 9CoNi-A needs to be enhanced when
higher values of Vickers hardness and ﬂow stress are expected.
In addition, the mis ﬁt between γ and γ 0 phases is not considered
in this study, which has a signi ﬁcant inﬂuence on the coarsening
of γ 0 precipitates and creep resistance at high temperatures. For
example, alloy 9CoNi-B may have a higher mis ﬁt value compared
to the alloy 9CoNi-A as estimated by the coarsening of γ 0 precip-
itates at 1000 °C/500 h (Figure 3a,b). Therefore, this is another
factor that needs to be considered for optimizing the design cri-
teria in the future. Accordingly, the corresponding machine-
learning models should also be developed and applied.
3. Conclusions
We propose a “cross-component” prediction method for the
high-component ( >7) γ 0-strengthened Co-based superalloys by
integrating the experimental data from diffusion multiples
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (9 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

assembled by a series of diffusion couples with low number of
components and machine-learning models. Four novenary alloys
were screened out according to the different design criteria for
the aeroengine and industrial gas turbine blades. These alloys
show good microstructural stability at 950 – 1000 °C and oxidation
resistance at 1000 °C. Compared with a CALPHAD approach, the
“diffusion-multiple þ machine-learning” method has been veri-
ﬁed to reach a comparable or slightly higher accuracy for the Tγ 0
of high-component alloys, such as alloy 9CoNi-A, when enough
related data from low-component diffusion couples are provided.
In contrast, the trend prediction by the CALPHAD is still mean-
ingful, especially when the related experimental data are de ﬁ-
cient. Expanding the compositional range in the database and
supplementing the critical interaction data of multiple elements
are beneﬁcial for improving the prediction accuracy of the “cross-
component” machine-learning models. As indicated by the
microstructural stability, compression test, and Vickers hardness
results, the in ﬂuence of solution strengthening and γ/γ 0 misﬁt
should also be considered for the establishment of machine-
learning model and design criteria to further improve mechani-
cal properties in the future.
4. Experimental Section
Thermodynamic Analysis : All the thermodynamic calculations of phase
constituent, Tγ 0 , and Aγ 0 = (Vγ 0 )2/3[37,63] in this study were performed using
the PANDAT software with the commercial Co-based thermodynamic
database PanCo2018.
Machine-Learning Model Fitting: Widely used tenfold cross-validation [64]
was used to avoid over ﬁtting of the selected models. First, the whole data-
set was scrambled and divided randomly into ten subsets. Then, one sub-
set would be used as the testing set, while the other nine subsets would be
used as the training set. Finally, the training set was fed into different algo-
rithms to build machine-learning models. This process would cycle 10
times, where each subset would be used as testing set exactly once.
The brute-force grid search algorithm was employed to optimize and tune
parameters for machine-learning models.
Diffusion-Multiple Preparations : All the individual experimental alloys in
the diffusion multiple were prepared by arc-melting high-purity (>99.9 wt%)
elements in an argon atmosphere and sectioned into blocks to assemble a
collection of diffusion couples. Then, the diffusion multiple was treated by
hot isostatic pressing (HIP) at 1200 °C/160 MPa for 5 h to achieve good
interfacial contact among the alloy pieces. After that, the diffusion multiple
was heat treated in the following process: 1250 °C/24 h þ 1000 °C/1000 h.
More details can be referred to the literature. [21,26,34]
Single-Crystal Superalloys Preparations : All the single-crystal alloys were
melted in a vacuum induction furnace, and subsequently directionally
solidiﬁed into [001]-oriented single-crystal rods with a diameter of
15 mm and a length of /C25 170 mm, using the conventional Bridgman
method. Then the heat-treatment process of single-crystal rods was set
as 1230 °C/12 h þ 1000 °C/24 h þ 800 °C/16 h for the alloy 9CoNi-A, and
1250 °C/12 h þ 1000 °C/4 h þ 800 °C/16 h for the alloy 9CoNi-D.
Compositional Measurements: Composition proﬁles across the diffusion
couple were obtained using quantitative electron probe microanalysis
(EPMA) on a JEOL JXA8230 microprobe at an accelerating voltage of
20 kV with a probe current of 10 nA. The beam spot diameter and the step
size of each EPMA spot were both set as 5 μm.
Physical, Oxidation, and Mechanical properties : Cylindrical samples of
3 mm diameter and 1.5 mm thickness were cut for differential scanning
calorimetry (DSC) experiments. Then, the Tγ 0 was determined by the
NETZSCH STA 449C thermal analyzer under high purity Ar ﬂow with a
heating rate of 10 °C min /C0 1. The hardness was measured using an
HXD-1000TM Vickers hardness testing system with a load of 200 g and
a dwell time of 10 s. The ﬁnal value of Vickers hardness (HV) was obtained
by averaging the results from ﬁve cycles. The density was measured using a
water displacement approach based on the Archimedes principle.
Isothermal oxidation tests were carried out at 1000 °C/100 h in air.
Mass gains were measured by analytical balance with an accuracy of
10/C0 4 g. Compressive specimens with [001] orientation ( <10° deviation)
were machined from heat-treated samples with a gauge length of
7.5 mm and a diameter of 5 mm. Compressive tests were conducted
at room temperature, 600, 700, 800, 900, 950, and 1000 °C with a strain
rate of 10 /C0 4 s/C0 1.
Microstructural Characterizations: The metallographic specimens of dif-
fusion couples and ingots were prepared using standard metallographic
sample preparation techniques and etched in a solution of 1% HF þ 33%
HNO3 þ 33% CH 3COOH þ 33% H 2O (by volume). The microstructure
was characterized by the ZEISS SUPRA 55 ﬁeld-emission scanning elec-
tron microscope. The γ 0 area fraction ( Aγ 0 ) corresponding to each com-
position spot was measured within a rectangle having a size of
5 μm /C2 400 μm (the length is parallel to the interface of the diffusion cou-
ple) by the standard point count method.
Supporting Information
Supporting Information is available from the Wiley Online Library or from
the author.
Acknowledgements
The authors would like to thank Ji-Cheng Zhao for the assistance in the
design of diffusion multiples. This research was supported by the National
Natural Science Foundation of China (grant no.: 52171095, 52201100,
52201024, and 92060113), China Postdoctoral Science Foundation (grant
no.: 2022M710346), Science and Technology on Advanced High
Temperature Structural Materials Laboratory (grant no.: 6142903210207),
Natural Science Foundation of Hunan Province (grant no.: 2022JJ40441),
National Key Research and Development Program of China (grant no.:
2017YFB0702902), and Key-Area Research and Development Program of
Guangdong Province (grant no.: 2019B010943001).
Conﬂict of Interest
The authors declare no con ﬂict of interest.
Data Availability Statement
The data that support the ﬁndings of this study are available from the
corresponding author upon reasonable request.
Keywords
alloy design, co-based superalloys, “cross-component” prediction,
diffusion multiples, machine learning
Received: November 20, 2022
Revised: January 20, 2023
Published online: February 12, 2023
[1] J. Sato, T. Omori, K. Oikawa, I. Ohnuma, R. Kainuma, K. Ishida,
Science 2006, 312, 90.
[2] C. S. Lee, Precipitation-Hardening Characteristics of Ternary Cobalt-
Aluminum-X Alloys , The University of Arizona, Tucson 1971.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (10 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

[3] T. M. Pollock, J. Dibbern, M. Tsunekane, J. Zhu, A. Suzuki, J. Miner.
Metall. Mater. Soc. 2010, 62, 58.
[4] A. Suzuki, H. Inui, T. M. Pollock, Annu. Rev. Mater. Res. 2015, 45, 345.
[5] R. C. Reed, The Superalloys Fundamentals and Applications, Cambridge
University Press, Cambridge 2006.
[6] M. S. Titus, Y. M. Eggeler, A. Suzuki, T. M. Pollock, Acta Mater. 2015,
82, 530.
[7] A. Bauer, S. Neumeier, F. Pyczak, M. Göken, Adv. Eng. Mater. 2014,
17, 748.
[8] F. Xue, H. J. Zhou, X. F. Ding, M. L. Wang, Q. Feng, Mater. Lett. 2013,
112, 215.
[9] S. Neumeier, L. P. Freund, M. Göken, Scr. Mater. 2015, 109, 104.
[10] E. A. Lass, D. J. Sauza, D. C. Dunand, D. N. Seidman, Acta Mater.
2018, 147, 284.
[11] P. Liu, H. Huang, S. Antonov, C. Wen, D. Xue, H. Chen, L. Li, Q. Feng,
T. Omori, Y. Su, Npj Comput. Mater. 2020, 6, 62.
[12] K. Shinagawa, T. Omori, J. Sato, K. Oikawa, I. Ohnuma, R. Kainuma,
K. Ishida, Mater. Trans. 2008, 49, 1474.
[13] W. Li, L. Li, S. Antonov, Q. Feng, Mater. Des. 2019, 180, 107912.
[14] L. Shi, J. J. Yu, C. Y. Cui, X. F. Sun, Mater. Sci. Eng. A. 2015, 635, 50.
[15] A. Bauer, S. Neumeier, F. Pyczak, M. Göken, Scr. Mater. 2010,
63, 1197.
[16] M. Ooshima, K. Tanaka, N. L. Okamoto, K. Kishida, H. Inui, J. Alloys
Compd. 2010, 508, 71.
[17] L. Lilensten, P. Kürnsteiner, J. R. Mianroodi, A. Cervellon, J. Moverare,
M. Segersäll, S. Antonov, P. Kontis, in Superalloys 2020 (Eds: S. Tin,
M. Hardy, J. Clews, J. Cormier, Q. Feng, J. Marcin, C. O ’Brien,
A. Suzuki), John Wiley & Sons, Inc., New York, NY 2020, p. 41.
[18] S. Antonov, W. Chen, S. Lu, D. Isheim, D. N. Seidman, Q. Feng,
E. Sun, S. Tin, Scr. Mater. 2019, 161, 44.
[19] W. Li, L. Li, S. Antonov, F. Lu, Q. Feng, J. Alloys Compd. 2020, 826,
154182.
[20] L. Klein, Y. Shen, M. S. Killian, S. Virtanen, Corros. Sci. 2011, 53, 2713.
[21] M. Zou, W. Li, L. Li, J.-C. Zhao, Q. Feng, in Superalloys 2020(Eds: S. Tin,
M. Hardy, J. Clews, J. Cormier, Q. Feng, J. Marcin, C. O ’Brien,
A. Suzuki), John Wiley & Sons, Inc., New York, NY 2020,p .9 3 7 .
[22] S. Lu, S. Antonov, L. F. Li, C. P. Liu, X. N. Zhang, Y. F. Zheng,
H. L. Fraser, Q. Feng, Acta Mater. 2020, 190, 16.
[23] P. Pandey, A. K. Sawant, B. Nithin, Z. Peng, S. K. Makineni, B. Gault,
K. Chattopadhyay, Acta Mater. 2019, 168, 37.
[24] N. Volz, C. H. Zenk, R. Cherukuri, T. Kalfhaus, M. Weiser,
S. K. Makineni, C. Betzing, M. Lenz, B. Gault, S. G. Fries,
J. Schreuer, R. Vaßen, S. Virtanen, D. Raabe, E. Spiecker,
S. Neumeier, M. Göken, Metall. Mater. Trans. A. 2018, 49, 4099.
[25] E. A. Lass, Metall. Mater. Trans. A. 2017, 48, 2443.
[26] W. Li, L. Li, C. Wei, J.-C. Zhao, Q. Feng,J. Mater. Sci. Technol.2021, 80,1 3 9 .
[27] J. Yu, C. Wang, Y. Chen, C. Wang, X. Liu, Mater. Des.2020, 195,1 0 8 9 9 6 .
[28] N. Khatavkar, S. Swetlana, A. K. Singh, Acta Mater. 2020, 196, 295.
[29] J. Yu, S. Guo, Y. Chen, J. Han, Y. Lu, Q. Jiang, C. Wang, X. Liu,
Intermetallics 2019, 110, 106466.
[30] J. Ruan, W. Xu, T. Yang, J. Yu, S. Yang, J. Luan, T. Omori, C. Wang,
R. Kainuma, K. Ishida, C. T. Liu, X. Liu, Acta Mater. 2020, 186, 425.
[31] Y. Mishin, Acta Mater. 2021, 214, 116980.
[32] J. C. Zhao, Z. Xuan, D. G. Cahill, Mater. Today 2005, 8, 28.
[33] L. Zhu, C. Wei, H. Qi, L. Jiang, Z. Jin, J.-C. Zhao, J. Alloys Compd. 2016,
691, 110.
[34] W. Li, L. Li, S. Antonov, C. Wei, J.-C. Zhao, Q. Feng, J. Alloys Compd.
2021, 881, 160618.
[35] J. Opitz, S. Burst, ArXiv Prepr. ArXiv191103347 2019.
[36] F. Xue, H. J. Zhou, Q. Y. Shi, X. H. Chen, H. Chang, M. L. Wang,
Q. Feng, Scr. Mater. 2015, 97, 37.
[37] S. Lu, S. Antonov, L. F. Li, Q. Feng, Metall. Mater. Trans. A. 2018,
49, 4079.
[38] J. He, M. Zou, L. Li, X. Wang, Q. Feng, Mater. Lett. 2020, 262, 127042.
[39] F. Xue, M. L. Wang, Q. Feng, in Superalloys 2012 (Eds: E. S. Huron,
R. C. Reed, M. C. Hardy, M. J. Mills, R. E. Montero, P. D. Portella,
J. Telesman), TMS, Warrendale 2012, p. 813.
[40] A. Suzuki, T. M. Pollock, Acta Mater. 2008, 56, 1288.
[41] M. S. Titus, High Temperature Deformation Mechanisms of L12-
Containing Co-Based Superalloys , University of California Santa
Barbara, Los Angeles 2015.
[42] A. Bauer, S. Neumeier, F. Pyczak, M. Göken, in Superalloys 2012 (Eds:
E. S. Huron, R. C. Reed, M. C. Hardy, M. J. Mills, R. E. Montero,
P. D. Portella, J. Telesman), TMS, Warrendale 2012, p. 695.
[43] C. H. Zenk, A. Bauer, P. Goik, S. Neumeier, H. J. Stone, M. Göken,
Metall. Mater. Trans. A. 2016, 47, 2141.
[44] M. Weiser, M. C. Galetz, H.-E. Zschau, C. H. Zenk, S. Neumeier,
M. Göken, S. Virtanen, Corros. Sci. 2019, 156, 84.
[45] N. Volz, F. Xue, A. Bezold, C. H. Zenk, S. G. Fries, J. Schreuer,
S. Neumeier, M. Göken, Metall. Mater. Trans. A. 2021, 52, 3931.
[46] L. Shi, J. J. Yu, C. Y. Cui, X. F. Sun, Mater. Lett. 2015, 149, 58.
[47] M. Knop, P. Mulvey, F. Ismail, A. Radecka, K. M. Rahman,
T. C. Lindley, B. A. Shollock, M. C. Hardy, M. P. Moody,
T. L. Martin, P. A. J. Bagot, D. Dye, JOM 2014, 66, 2495.
[48] T. Omori, K. Oikawa, J. Sato, I. Ohnuma, U. R. Kattner, R. Kainuma,
K. Ishida, Intermetallics 2013, 32, 274.
[49] S. Kobayashi, Y. Tsukamoto, T. Takasugi, Intermetallics 2011,
19, 1908.
[50] S. Meher, H. Y. Yan, S. Nag, D. Dye, R. Banerjee, Scr. Mater. 2012,
67, 850.
[51] H.-Y. Yan, J. Coakley, V. A. Vorontsov, N. G. Jones, H. J. Stone,
D. Dye, Mater. Sci. Eng. A 2014, 613, 201.
[52] F. Pyczak, A. Bauer, M. Göken, U. Lorenz, S. Neumeier, M. Oehring,
J. Paul, N. Schell, A. Schreyer, A. Stark, F. Symanzik, J. Alloys Compd.
2015, 632, 110.
[53] H. Y. Yan, V. A. Vorontsov, J. Coakley, N. G. Jones, H. J. Stone, D. Dye,
in Superalloys 2012 (Eds: E. S. Huron, R. C. Reed, M. C. Hardy,
M. J. Mills, R. E. Montero, P. D. Portella, J. Telesman), TMS,
2012, p. 705.
[54] T. M. Pollock, S. Tin, J. Propuls. Power. 2006, 22, 361.
[55] T. Murakumo, T. Kobayashi, Y. Koizumi, H. Harada, Acta Mater.
2004, 52, 3737.
[56] X. Zhuang, L. Li, Q. Feng, in Superalloys 2020 (Eds: S. Tin, M. Hardy,
J. Clews, J. Cormier, Q. Feng, J. Marcin, C. O ’Brien, A. Suzuki), John
Wiley & Sons, Inc, New York, NY 2020, p. 870.
[57] P. Caron, T. Khan, Aerosp. Sci. Technol. 1999, 3, 513.
[58] X. W. Jiang, D. Wang, G. Xie, H. Li, L. H. Lou, J. Zhang, Metall. Mater.
Trans. A. 2014, 45, 6016.
[59] F. Lu, L. F. Li, S. Antonov, Y. F. Zheng, H. L. Fraser, D. Wang,
J. Zhang, Q. Feng, in Superalloys 2020 (Eds: S. Tin, M. Hardy,
J. Clews, J. Cormier, Q. Feng, J. Marcin, C. O ’Brien, A. Suzuki),
John Wiley & Sons, Inc., New York, NY 2020, p. 218.
[60] Z. Fan, X. Wang, Y. Yang, H. Chen, Z. Yang, C. Zhang, Mater. Sci. Eng.
A 2019, 748, 267.
[61] S. Neumeier, H. U. Rehman, J. Neuner, C. H. Zenk, S. Michel,
S. Schuwalow, J. Rogal, R. Drautz, M. Göken, Acta Mater. 2016,
106, 304.
[62] I. Lopez-Galilea, C. Zenk, S. Neumeier, S. Huth, W. Theisen,
M. Göken, Adv. Eng. Mater. 2014, 17, 741.
[63] S. Giese, A. Bezold, M. Pröbstle, A. Heckl, S. Neumeier, M. Göken,
Metall. Mater. Trans. A 2020, 51, 6195.
[64] D. R. Goldstein, J. Am. Stat. Assoc. 2005, 100, 1464.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201257 2201257 (11 of 11) © 2023 Wiley-VCH GmbH
 15272648, 2023, 10, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201257 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
