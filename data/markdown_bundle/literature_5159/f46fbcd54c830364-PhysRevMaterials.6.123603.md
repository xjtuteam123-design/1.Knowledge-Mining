# PhysRevMaterials.6.123603

<!-- source: D:\总文献\PhysRevMaterials.6.123603.pdf -->
<!-- file_sha256: a6b3321e596090f9cd00aea222944ea3277a0bd58ae298edf3085a8f012155eb -->

## Page 1

PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
Highly interpretable machine learning framework for prediction of mechanical
properties of nickel based superalloys
Nikhil Khatavkar and Abhishek Kumar Singh *
Materials Research Centre, Indian Institute of Science, Bangalore 560012, India
(Received 9 August 2022; revised 2 November 2022; accepted 14 November 2022; published 7 December 2022)
Superalloys are a special class of heavy-duty materials with excellent strength retention and chemical stability
at very high temperatures. Nickel-based superalloys are used commercially in aircraft turbines, power plants,
and space launch vehicles. The optimization of mechanical properties of alloys has been traditionally carried out
using experimental approaches, which demand massive costs in terms of time and infrastructure for testing. In
this paper, we propose a method for mechanical property prediction of Ni-based superalloys by learning from
past experimental results using machine learning (ML). Five highly accurate ML models are developed to predict
yield strength (YS), ultimate tensile strength (UTS), creep rupture life, fatigue life with stress, and strain values.
We have developed an extensive database containing mechanical properties of over 1500 Ni-based superalloys.
Basic material parameters such as the composition of the alloy, annealing conditions, and testing conditions
are also collected and used as features for developing the ML models. The prediction root mean squared errors
for the YS, UTS, creep, and fatigue life models are 0.11, 0.06, 0.19, 0.22, which are minimal, leading to a
highly accurate estimation of the target values. These ML models are highly transferable and require a minimum
number of input features. In addition, feature analysis performed by SHapley Additive exPlanations (SHAP)
for individual properties reveals the relative signiﬁcance of each descriptor in deciding the target property. We
demonstrate that a uniﬁed and highly accurate ML framework can be developed using common features for all
mechanical properties. The models are developed on experimental data, making them directly applicable for
industries.
DOI: 10.1103/PhysRevMaterials.6.123603
I. INTRODUCTION
Nickel-based superalloys have emerged as the most fa-
vored class of materials for applications involving high
strength along with superior creep and fatigue properties at
high temperatures. Ni-based superalloys enable systems to
operate at very high temperatures, which leads to high efﬁ-
ciency and lower fuel consumption [ 1]. Some of the modern
superalloys can operate at temperatures over 80% of the
melting temperature, extending their operating temperatures
over 1200
◦C[ 2–4]. As a result, superalloys are heavily em-
ployed in gas turbines for aircraft propulsion engines and
electricity generators [5–7]. These superior properties are due
to several decades of optimization of composition and mi-
crostructure s [ 8,9]. Initially, the enhancement of properties
resulted from improved microstructures by employing sophis-
ticated casting techniques. The directionally cast superalloys
were a noticeable improvement over the wrought alloys as the
grain boundaries in the direction of load can be effectively
eliminated to reduce the risk of nucleation of cracks. The
microstructural design was improved further by producing
single-crystal superalloys. In addition, vast enhancement in
strength and creep /fatigue resistance is made possible by
optimization of the precipitate γ
′ phase [ 10,11]. The pres-
ence of a γ′ phase in addition to the matrix γ phase in this
*abhishek@iisc.ac.in
generation of superalloys imparts the required strengthening
through precipitation hardening and blocking dislocation mo-
tion [ 12,13]. Optimization of composition of the superalloy
can also provide better mechanical properties by solid solution
strengthening and inﬂuencing the volume fraction and distri-
bution of γ
′ precipitates. Several elements such as Mo, W,
Ta, Ti, and Nb are beneﬁcial for the precipitation process, and
the lattice mismatch induced between the γ and γ
′due to the
addition of these elements leads to dislocation immobilization
at the boundaries [ 14,15]. However, this crucial optimization
process of microstructural and compositional parameters is
painstakingly slow due to the vast compositional space. In
addition, experimental determination of creep rupture lifetime
and fatigue cycles to failure is also highly time and cost
intensive.
The introduction of machine learning (ML) in the ﬁeld of
material science in the last few years has led to signiﬁcant
acceleration in the process of materials discovery [ 16–19].
ML utilizes several algorithms to learn the dominant patterns
in the existing data and connect them to the desirable property.
These patterns are then used to predict the property of a new
set of data. ML has been used successfully in the past to
predict diverse material properties such as band gaps [ 20–22],
band edges [ 23], lattice thermal conductivity [ 24], glass tran-
sition temperatures [25], dielectric constants [26], and Vickers
hardness [ 27,28]. Recently, ML has also been successfully
applied to high entropy alloys for prediction of phase, hard-
ness, and solid solution forming ability [ 29–31]. Moreover,
2475-9953/2022/6(12)/123603(16) 123603-1 ©2022 American Physical Society

## Page 2

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
ML methods have successfully optimized several properties
of nickel-based superalloys such as phase fraction of γ′phase,
density, solvus temperature of the γ′ phase, and lattice mis-
match of the γ and γ′ phases [ 32–34]. These properties
of superalloys play an important role in designing turbines
with enhanced lifetimes. ML was also used to predict the
chemical composition of the different phases of nickel-based
superalloys [ 33]. In addition, the most important criteria for
consideration of any material for turbine applications are the
simultaneous presence of high yield strength (YS), fatigue,
and creep life at high temperatures. Approaches which can
simultaneously predict and optimize the properties of interest
for Ni-based superalloys exist [32]. However, it will be highly
beneﬁcial if analysis of features is performed rigorously for
thorough understanding of the ML models developed.
In this paper, we develop a unifying ML modeling scheme
to predict the mechanical properties of nickel-based superal-
loys. The mechanical properties include YS (MPa), ultimate
tensile strength (UTS) (MPa), creep rupture life (hours), and
fatigue life (number of cycles). These four properties are es-
sential and are widely studied while selecting components for
heavy-duty applications. It is desirable to have the largest pos-
sible values for these properties while in operation; however,
it is usually observed that these properties have conﬂicting
requirements in terms of compositions and treatment. For
instance, increasing the creep rupture life of a material may
lead to fracture vulnerability due to fatigue. In the ML models
developed, these properties can be calculated simultaneously
using compositions, treatment conditions, and testing condi-
tions. The ML models use minimal data as input, making it
easy to use and highly transferable across different properties.
ML models are developed using Gaussian process regression
(GPR) for YS, UTS, and creep rupture life. Moreover, the
testing conditions for determining fatigue life include stress
and strain amplitude [ 35–37]. Therefore, separate ML models
are developed for including stress and strain as independent
features. Finally, using feature engineering, we perform in-
depth feature analysis and identify a set of features which are
highly correlated to all the mechanical properties considered
in this paper. This set of features is employed to develop a
uniﬁed ML model framework that simultaneously predicts all
the mechanical properties.
II. METHODOLOGY
A database was initially built for Ni-based superalloys.
The data utilized for developing the ML model development
is taken from literature [ 13,35–103]. This database contains
the compositions, annealing schedules, and testing conditions
as the features /descriptors for developing the ML models
and the mechanical properties as the ﬁnal target property.
The features selected are easily available in any experimental
study. The data set contains 349 values for YS, 248 for UTS,
and 383 for creep rupture life along with their corresponding
features. Moreover, 318 values exist for fatigue life with stress
and 384 for fatigue life with strain. All the data collected
contain 1610 values from recent literature, and all data was
selected only if all the mentioned descriptors and at least one
of the target properties of a material were present. The sources
(DOIs) of the data are also presented in Supplemental Material
Table 1 [104]. The compositions of the superalloys consist of
24 elements recorded in weight percentages. It is ensured that
the sum of all the elements must add up to 100%; otherwise,
the data is not considered further. The annealing schedule
considers the two-step procedure, which is generally followed
for Ni-based superalloys. The annealing temperatures are
recorded in Celsius and denoted as T
1
an and T 2
an, respectively.
Similarly, the annealing times are recorded in hours and de-
noted as t
1
an and t2
an, respectively. Solutionizing treatment is
also a widely reported parameter for Ni-based superalloys, in
which the alloy is heated above its solvus temperature. How-
ever, this treatment is only a precursor step in the precipitation
hardening process before annealing. The material properties
change drastically after the annealing process is complete.
Therefore, we choose not to include solutionizing treatment
for this paper. The distribution of the compositions and the
annealing schedule is presented in Supplemental Material
Table 2. In addition to the composition and heat treatment
parameters, we also include composition-averaged elemental
features as descriptors in this paper. The elemental features in
this paper are easily available and provide additional sets of
information that can be highly relevant for this study. Thus,
the database consists of 43 features which are presented in
Supplemental Material Table 3. The target properties are con-
verted to log values before further process. To keep user input
to a bare minimum, selecting only the most basic features
for this paper becomes crucial. Therefore, any other input
derived from other experiments or modeling is included in the
development of ML models.
Traditional experimental methods of mechanical property
determination are specialized and accurate; however, these
methods are highly time intensive and costly when applied for
exploratory research. The creep-fracture life of some materi-
als can reach 10
4 to 105 hours, and fatigue life can reach over
108 cycles. The sheer amount of time required alone makes the
swift determination of mechanical properties a challenging
task. To circumvent this, we use the database to build ML
models for faster prediction of the properties as compared to
experiments. One of the crucial aspects of ML is to identify
the features which are highly relevant for the prediction of
the target properties. In this paper, the least absolute shrink-
age and selection operator (LASSO) is employed for feature
selection [ 105]. LASSO is a regression and regularization
technique that determines the weights of features by minimiz-
ing the ordinary least squares (OLS) term subject to the L1
penalty term, which can be represented as
min
{1
N||y − wx||2 + λ||w||1
}
, (1)
where x, y, N, λ are the feature vector, target, the size of data
set and penalty parameter, which controls the shrinkage of
the coefﬁcients, respectively. Larger values of λ lead to larger
reduction in the number of features. The optimization of the
parameter λ is performed manually. LASSO is an embedded
feature selection method that removes features that are either
redundant or are poorly correlated to the property [ 106]. Sev-
eral unique methods are also available for feature selection
such as the data-driven multilayer feature selection method
(DML − FS
dek )[ 107]. Since the number of features in this
123603-2

## Page 3

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
work is manageable, we proceed with LASSO for the feature
selection process.
For the prediction of the properties, we have employed
GPR based on the Bayesian inference approach. In GPR,
the algorithm chooses the suitable functional form, which
makes it a nonparametric approach [ 108]. Instead of deter-
mining ﬁxed parameters for a function, GPR employs output
distribution from various functions using a Gaussian process
distribution. The possibility of selecting the functions poses
a problem since the space of possible functions is inﬁnite.
Therefore, some initial assumptions are made to restrict the
search in functional space, known as prior. This space is
deﬁned such that the mean of all functions is zero, while the
standard deviation throughout the space is ∑
p and can be
represented as
w ∼ N (0,/Sigma1p ). (2)
The target output in GPR takes the following form [ 109]:
y = ˆy + ϵ, (3)
where ˆy represents the Gaussian distribution for target pre-
diction, which is to be determined, and ϵ is a Gaussian
distribution of noise with zero mean and a constant variance.
The joint Gaussian distribution for the target property can be
represented as
ˆy(x) = N(μ(x), k(x, x
′)), (4)
where N represents a normal multivariate distribution with
μ(x) mean and k(x, x′) covariance. The noise assumption with
the model gives rise to likelihood. Likelihood is deﬁned as the
probability density of parameters ﬁtting the given data and is
represented as
p(y|X, w) = N
(
X
Tw,σ 2
n I
)
(5)
where X is the feature vector (X = (x1, x2, ...,xn )T ). The
weights (w) are updated to increase the probability of the
function ﬁtting the data and are represented by the posterior
as
p(w|y, X) = likelihood ∗ prior
marginal likelihood , (6)
where the marginal likelihood is a constant value independent
of the weights. Posterior captures all the information from
likelihood and prior. If only numerator terms are considered,
the posterior assumes the form of
p(w|y, X) ∼ N
(
¯w = 1
σ 2n
A−1Xy, A−1
)
, (7)
where A = σ−2
n XXT + /Sigma1−1
p . This is a Gaussian distribution
with ¯ w as the mean and A −1 as the covariance matrix. This
method scales poorly as O(n3 ) due to the computationally
costly step of multiplication of XX T and inversion of the ma-
trix A. Instead of the multiplication, a kernel trick is applied to
reduce the number of calculations involved. For implementa-
tion, several kernels such as the polynomial (quadratic), radial
basis function (RBF), dot-product, and Matern kernels are
available. The kernel selection is essential for the accuracy
of the ﬁnal ML model. In this paper, we have evaluated all the
kernels for ML model development suitable for the data set.
Finally, the predictions are made for unknown data by
performing an average over all the functional values, weighted
by posterior probability density. The ﬁnal distribution has the
form of Gaussian function, which is represented as
p(f
∗|x∗, X, y) = N
( 1
σ 2n
xT
∗ A−1Xy, xT
∗ A−1x∗
)
, (8)
where x∗ is the input for the prediction of the target property
through the function f∗.
It is important to analyze the built ML models for ob-
taining the dominant trends that help to maximize the target
properties. After training efﬁcient ML models, analysis of the
ML models is done using the Pearson correlation coefﬁcients
(PCCs). The PCC is deﬁned as [ 110]
ρ(X, y) = cov(X, y)/σ
X ∗ σy (9)
where cov() is the covariance function and σ is the vari-
ance. X and y denote the feature and target properties under
consideration, respectively. The PCC measures the linear cor-
relation between the target property and individual features.
The value of the PCC ranges between −1t o1f o rn o r m a l l y
distributed standardized data. Positive correlation implies that
as the value of feature X increases, the value of y will also
increase. A larger magnitude indicates a stronger correlation
between the feature and target properties. The GPR-based ML
algorithms and PCCs are implemented on Python using the
SCIKIT-LEARN ML library [ 111].
III. RESULTS
A. Data preprocessing
The data collected was subjected to ﬁltering conditions to
ensure that only high-quality and valid data is used for the ML
modeling. The validity of compositions was ensured by sum-
ming all elemental compositions. The data set was selected if
the elemental compositions add up to 100%. Only weight per-
centages are used for composition in this study as it is the most
common form of representation in literature. Some inaccura-
cies pertaining to individual element concentrations were also
corrected by referring to the alternative sources as presented
in Supplemental Material Table 4. Next, standardization of
the features was performed using the standard scalar feature
in the Python
SKLEARN library [111]. Standardization is done
to bring all features to a uniform scale such that the mean of
the feature distribution is zero and the standard deviation is
one. The range of values after standardization is presented for
all features for different properties in Supplemental Material
Fig. 1.
B. ML model development
The purpose of our paper is to develop a uniﬁed and
robust approach for the prediction of mechanical properties
that are most crucial while evaluating the usefulness of a
superalloy in demanding applications. The schematic of the
work is depicted in Fig. 1, showing the important steps in
this approach. The collected data is segregated according to
the target property and ML models are developed using the
algorithms discussed in the Methodology section.
123603-3

## Page 4

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
(a) (b) (c)
FIG. 1. Schematic representation of the work. (a) A database is established with experimental data from the literature. The data is subjected
to rigorous ﬁltering conditions and standardization. (b) Feature engineering is performed for individual data sets to identify the relevant
descriptors and study the effect on the target property. (c) ML models are developed for individual properties using the identiﬁed crucial
features.
To determine the ML models’ accuracy, we use the coef-
ﬁcients of determination ( R2), and root mean squared error
(rmse). The coefﬁcient of determination is deﬁned as the
proportion of variation of the dependent variable (target prop-
erty), which is captured by the variations in independent
variables or features. R
2 is an important parameter, which
gives us the quantitative value of the quality of the ML models
developed. R
2 is deﬁned as
R2 = 1 −
∑
i (yi − y′
i )2
∑
i (yi − ymean )2 , (10)
where vymean is the mean of all outcomes. R2 ranges between
0 to 1, where 1 represents best ﬁtting of model while 0 repre-
sents minimum ﬁtting. The rmse for a given data set is deﬁned
as the standard deviation of the residual errors between pre-
dicted and actual values. It can be represented as
rmse =
√
1
n
n∑
i
(yi − y′
i )2, (11)
where n is the number of individual data, y i is the actual
value, and y’ i is the predicted value. rmse is preferred over
the other absolute errors as it assigns greater priority to the
largest errors due to the squared term. The minimum value
of rmse represents that the ML model has a high prediction
accuracy.
Initially, the ML model is developed using GPR for the
YS of superalloys. The data was split in a training and test-
ing set in the ratio of 90:10, and important features were
selected using LASSO. To select the most important features
for training the ML models, the λ parameter in LASSO was
varied from 0.01 to 0.3. The best results for the λ value for
all the properties along with the LASSO score is presented in
Supplemental Material Table 5. It is found that increasing the
λ to a larger value excludes the important features. Hence, the
λ value is set to 0.01 for building ML models for YS.
The result of the ML model for different kernels is pre-
sented in Table I. It can be observed that the GPR model
that employs the quadratic kernel performs better than the
other kernels. The GPR model with a quadratic kernel delivers
highly accurate predictions for YS on the training and test data
with R
2 of 0.97/0.95 (train/test data) and rmse of 0.11 /0.11.
Moreover, the GPR model with the Matern kernel also per-
forms well with R
2 of 0.96/0.92 and rmse of 0.12 /0.13. In
comparison, GPR models with RBF and dot-product kernels
perform poorly. The rmse for dot product and RBF kernels are
0.38 and 0.18, which are signiﬁcantly larger than the quadratic
and Matern kernels. The results are analogous to other works,
where the estimation of the thermal conductivity of frost is
performed using GPR and Matern and quadratic kernels, pro-
ducing highly accurate predictions [ 112]. Figure 2(a) depicts
the performance of the GPR model, where it is observed that
most of the testing data lie near the 45
◦ dashed line.
The ML model developed in this paper employs 17
LASSO-selected features. This feature set includes 14 compo-
sitional features, two annealing parameters, and the tempera-
ture at which YS is measured. Individual PCCs of selected
features are shown in Fig. 3. The compositions of Nb, Fe,
Cr, Mo, and Zr are directly correlated with the YS, implying
an enhancing effect through the addition of these elements.
These elements are useful in providing strength to super-
alloys through solid-solution strengthening. These elements
strengthen the γ matrix by impeding the movement of the
123603-4

## Page 5

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
TABLE I. Performance of GPR models with different kernels for the mechanical properties (Bold fonts represent the best values for the
mechanical properties).
Matern Dot Quadratic RBF
Property R2 rmse R2 rmse R2 rmse R2 rmse
YS 0.96 /0.92 0.12 /0.13 0.59 /0.71 0.38 /0.38 0.97/0.95 0.11 /0.12 0.98/0.92 0.18 /0.19
UTS 0.98 /0.98 0.07 /0.08 0.58 /0.60 0.33 /0.33 0.99/0.98 0.04 /0.06 0.89/0.89 0.17 /0.17
Creep 0.95/0.92 0.17 /0.19 0.52/0.48 1.24 /1.26 0.99 /0.77 0.04 /0.67 0.98 /0.96 0.22 /0.37
Fatigue stress 0.96/0.96 0.32 /0.32 0.84/0.78 1.51 /1.51 0.99 /0.88 0.11 /1.10 0.98 /0.90 1.01 /1.04
Fatigue strain 0.95/0.92 0.22 /0.22 0.52/0.56 1.54 /1.56 0.96 /0.96 0.44 /0.40 0.92 /0.92 0.63 /0.61
dislocation. The effect of the strengthening depends on the
difference in the atomic radius. Most of the selected elements
have diameters larger than Ni, leading to high strengthening.
Co and Ti are slightly negatively correlated, indicating that
adding these elements does not lead to signiﬁcant changes
in the YS. The positive correlation of annealing time and
temperatures with YS in Fig. 3 points to the relative dynamics
of formation and distribution of the γ
′ phase. An increase of
annealing temperature leads to higher nucleation and growth
of the γ
′ phase in the material, leading to enhanced YS
through precipitation hardening [ 113]. However, an increase
of annealing time beyond a speciﬁc limit leads to coalescence
of the γ′phases leading to large precipitate diameters, which
is detrimental to the superalloy. Therefore, a proper balance in
the annealing time and temperature is necessary to maintain
high YS. In most metals, the YS decreases with increas-
ing temperature. The decrease is attributed to activation of
dislocation motion that assists plastic deformation at high
temperature [ 114]. However, superalloys exhibit a peculiar
phenomena known as the yield point anomaly, where the YS
of the material increases with temperature up to a speciﬁc
limit [ 115,116]. The data used in this paper contain several
observations from this temperature range, and therefore the
larger values of YS obtained at the higher temperatures make
FIG. 2. The actual versus predicted values of best GPR models for (a) YS, (b) UTS, (c) creep, (d) fatigue with stress as feature (fatigue
stress), (e) fatigue with strain as feature (fatigue strain). The data in all the mechanical properties lies near the black line, which implies that
the ML models are highly accurate.
123603-5

## Page 6

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
FIG. 3. Feature importance of composition and experimental conditions (stress and temperature of experiment) for the prediction of YS,
UTS, creep rupture life. The correlations are presented as heat map for individual features.
the correlation of YS with temperature positive. Our ML
model predicts the yield point anomaly of Ni-based super-
alloys with reasonable accuracy as shown in Supplemental
Material Fig. 2.
In literature, the estimation of YS analytically is done
by constructing mathematical models using ﬁxed composi-
tion or the majority elements in the superalloy such as Ni,
Co, and microstructural features such as the γ and γ
′ phase
distributions, volume fractions, and temperature [ 117–119].
These models are specialized for a particular set of com-
positions or speciﬁc precipitate shapes, making them highly
accurate provided the assumptions of composition and pre-
cipitate geometry hold [ 120]. However, the validity of these
models remains untested for different experimental condi-
tions. We have approached this problem with a general and
much less time-intensive procedure by applying data-driven
ML models.
Previously, ML model development for determining the YS
of superalloys was carried out using small subsets of data,
leading to a higher bias toward speciﬁc compositions [ 121].
Moreover, the recent availability of several highly specialized
ML algorithms generates a need to explore further improve-
ment possibilities. To develop this model, we included the data
from all the generations of superalloys to reduce the inherent
bias the ML algorithm may acquire for certain compositions.
The resulting prediction error of YS of 0.11 on a logarithmic
scale, which translates to 1.2 MPa, is the lowest achieved
among all the ML or analytical models developed.
The next property under consideration is the UTS. The
data set for UTS, which consists of 41 features, is reduced
initially using LASSO. The optimum result was obtained at
λ value of 0.05, which reduced the number of features to
eight. Using these features, ML models were developed using
GPR employing different kernels. The best results for the ML
models developed using different kernels are shown in TableI.
The models developed using quadratic, Matern, and the RBF
kernels show low rmse values. However, the R
2 value of the
RBF kernel is considerably low (0.89 /0.89) compared to the
Matern and quadratic kernels. The ML model obtained the
best results with the quadratic kernel having R
2 of 0.99/0.98
and rmse of 0.04/0.06. These results for the prediction of UTS
are unprecedented, with minimal errors of prediction in log
scale. When converted to a normal scale, the values show an
error of 1.09 /1.14 MPa, which indicates a considerable im-
provement in accuracy when the entire range of the property
is considered. The true versus predicted values for the best ML
model for UTS are shown in Fig. 2(b). The plot conﬁrms that
the ML model captures the trend in the data set with a high
degree of accuracy.
To study the effect of the selected features on the UTS,
we examine their Pearson’s correlation coefﬁcient as shown
in Fig. 3. Elements that provide solid solution strengthening
lead to an increase in the UTS. Therefore, Ti, Cr, and Mn
show a positive correlation with the UTS. The presence of
trace amounts of carbon also leads to an increase of UTS due
to the formation of hard carbide phases. The carbide phases
hinder the dislocation movements and inhibit the sliding of
grains relative to each other, thereby increasing the strength
of superalloys [122]. At the same time, the effect of excessive
annealing is detrimental for the UTS. An increase of anneal-
ing time/temperature leads to the formation of secondary γ
′
phases, which are generally larger in dimensions than the
primary γ′ phase. This increase in size is responsible for the
deleterious effect on the UTS at room temperatures [ 123].
The negative correlation of measurement temperature with the
UTS is a complex phenomenon [ 124] and can be attributed to
the shearing of the γ
′phase after the YS is reached. This effect
is enhanced for higher temperatures and larger precipitate
phases.
To serve as a component of the turbine, a material must
bear heavy loading at high temperatures, which can be esti-
mated by creep strength [ 125,126]. Creep strength is one of
the most important and widely studied superalloy properties.
Consequently, several models for predicting the creep of su-
peralloys exist that employ a wide variety of input properties
of the material [ 127–130]. The primary role of creep resis-
tance is attributed to the more prominent presence of the γ
′
phase, which provides resistance to the defect diffusion [ 131].
Larger precipitate sizes and small γ channels are beneﬁ-
cial for increasing the creep resistance of superalloys [ 131].
Several analytical models sensitive to the compositional and
microstructural properties have been proposed for the simu-
lation of creep in two-phase superalloys [ 132–135]. Although
accurate and sensitive to speciﬁc compositions, these models
fail to capture the broader attributes that lead to signiﬁcantly
larger rupture lives. To circumvent the problem, data-driven
models are being employed to predict creep rupture life of var-
ious high-temperature alloys [ 136–138]. This has enhanced
the capability of making an informed prediction of the rupture
life of superalloys. Liu et al. accurately predicted the creep
rupture life of Ni-based single crystal alloys using the di-
vide and conquer self-adaptive (DCSA) ML approach, where
initially the data was clustered according to the creep mech-
anisms and further optimal ML models were developed for
123603-6

## Page 7

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
prediction of the creep life. Similarly, creep life has also been
predicted using neural networks combined with Monte Carlo
techniques [ 138]. Our aim is to explore approaches that can
provide highly accurate results while simultaneously reducing
the complexity of the model. Therefore, in this paper, we
develop ML models for creep rupture life using the most
basic features used in experiments and study the dependence
of rupture life on its composition, annealing parameters, and
measurement conditions. Using LASSO, the most effective
features are selected, then utilized to build ML models.
It is observed that for the prediction of rupture life of
superalloys, the GPR model with the quadratic kernel yields
the lowest rmse value for the training data set. However, there
is a signiﬁcant difference between the train rmse (0.04) and
test rmse (0.67). The difference between the R
2 values of the
train data (0.99) and test data (0.77) is also signiﬁcant. This
difference between the test /train rmse and R
2 values in the
GPR model with the quadratic kernel indicates overﬁtting.
Overﬁtting occurs when the ML algorithm ﬁts the noise and
the training data, leading to the failure in the accurate pre-
diction of test data. The GPR model with Matern kernel is
the most accurate model with R
2 of 0.95 /0.92 and rmse of
0.17/0.19. Figure 2(c) shows the true versus predicted values
for the GPR model. The data lies along the line conﬁrming the
model’s accuracy.
From Fig. 3, it is clear that the elements responsible for
the formation of the γ
′phase show a positive correlation with
the rupture life. This is expected as precipitate phases such as
the γ
′and carbide phases reduce creep rates. The presence of
precipitate phases impedes both dislocations’ movement and
diffusing atoms while resisting the grain reorientation. There-
fore, the addition of these substances is expected to increase
creep strength. A critical aspect of the models is that the com-
positions of Re and Ru are not identiﬁed as important features.
This trend is surprising since the successive generations of Ni-
based superalloys are based on the addition and optimization
of these elements from the 1980s [8]. On closer analysis of the
collected data, it is observed that the composition of both these
elements is either usually ﬁxed near three wt % in experiments
or the older generation of the superalloys; these elements are
absent. This leads to the exclusion of both these elements from
the ML models as the minimal variance is encountered with
the target property. However, adding these elements in small
quantities is beneﬁcial for creep strength. The effect of Re and
other elements is discussed in detail in the next section. In
experiments, carbon is usually present in trace quantities to
enhance creep properties [139,140]. However, the larger com-
position of carbon has been deemed as detrimental for creep
properties due to the excessive formation of brittle MC, M
23C6
and M4C3 phases at grain boundaries. Therefore, the negative
trend presented by our ML model is in agreement with the
experimental observations on rupture life [ 140]. In addition,
the negative correlation of both creep stress and temperature
of creep is an obvious conclusion analogous to empirical
models.
The next model was developed to predict fatigue life of
superalloys. Fatigue is also one of the most critical and
widely studied properties. The engine components experience
variations of loading conditions during the various stages of
operation, making the study of fatigue at elevated temper-
atures in addition to the creep necessary. In the literature,
we found that the reported fatigue parameters include the
temperature of measurement, stress range, stress amplitude,
and strain range. The presence of two different parameters
based on stress and strain makes it challenging to ﬁt a single
ML model since the direct conversion of stress range to strain
range and vice versa is not possible. Owing to a large amount
of data in both cases, we build two separate ML models for
the two regimes. The ﬁrst ML model uses stress range, tem-
perature, annealing conditions, composition, and elemental
features as the descriptors for the ML model. We denote this
ML model as the fatigue-stress ML model. After applying
LASSO, the number of features is reduced to 19 from 42.
It is observed that the GPR model with the quadratic kernel,
which was the best model for YS and UTS, is severely over-
ﬁtted for the given set of features. The best model for fatigue
is the GPR model with Matern kernel with R
2 of 0.96/0.96
and rmse of 0.32 /0.32. Figure 2(d) represents the true versus
predicted values for the GPR ML model for fatigue using
stress as a feature. The ML model predicts the fatigue life for
unknown data accurately.
To analyze the feature dependency of the ML model, Pear-
son correlation was calculated and is presented in Fig. 4(a).
The ﬁgure shows that elements such as Mo, Nb, Fe, and Mn
positively correlate with fatigue life, while elements such as
C, Ni, and Co show a negative correlation with the number
of cycles. Carbon is responsible for forming hard precipitate
carbide phases in the microstructure. Although beneﬁcial up
to a certain extent for the creep properties, this precipitation is
highly detrimental for the fatigue properties. The formation
of rigid grain boundaries due to carbides often can serve
as the initiation point of a crack in superalloys [ 141]. The
negative correlation of nickel and cobalt is an obvious con-
clusion since the addition of larger amounts of γ
′ forming
elements, fatigue, and creep enhancers reduce these elements.
This trend is being captured as a negative correlation. In addi-
tion, the annealing conditions show a negative correlation with
the fatigue life, indicating that severe annealing conditions
can have an adverse effect on fatigue life due to prolonged
heating.
The second ML model developed for fatigue life is based
on the strain range the materials are subjected to in testing
conditions (denoted as the fatigue-strain ML model). LASSO
is applied on the feature set, which yields 19 important fea-
tures for predicting fatigue life. The GPR models are trained
using the four kernels. It is observed that the Matern kernel
performs better than the quadratic, dot-product, and RBF
kernels. Hence, the GRP model with the Matern kernel is
employed for developing the ML model. The best result ob-
tained for the GPR model is R
2 of 0.94 /0.94 and rmse of
0.22/0.22. The GPR model with Matern kernel outperforms
the quadratic kernel in fatigue models. Figure 2(e) represents
the true versus predicted trends for the fatigue model with
strain range. With its higher accuracy, this ML model is best
suited for predicting fatigue life. The correlation analysis for
the fatigue model is presented in Fig. 4(b).F r o mF i g .4(b),i t
is concluded that solid solution strengthening elements lead
to an increase in the fatigue life, whereas elements such as
carbon, phosphorus, and silicon lead to a decrease in fatigue
life. The negative correlation of Re composition on fatigue
123603-7

## Page 8

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
FIG. 4. Feature importance for fatigue life predicted through (a) stress range(MPa), (b) strain range (%).
life is an apparent departure from the experiments [ 142].
It is widely recognized that Re is responsible for the
enhancement of fatigue and creep life of Ni-based superalloys.
Re is generally added in constant and sparse quantities, mak-
ing it difﬁcult to determine the correlation with fatigue life
accurately. The effect of Re on creep and fatigue properties
has been analyzed further in the next section. Annealing tem-
peratures show a small positive correlation and time shows a
negative correlation. This implies that short annealing sched-
ules at higher temperatures enhance fatigue properties. This is
expected as ﬁne grained alloys show superior fatigue perfor-
mance due to delayed crack initiation. [ 143]. In addition, as
expected, the temperature of fatigue, strain range, and stress
range show a negative correlation, implying the reduction
of fatigue life with an increase of any of these parameters.
High temperature is known to enhance the cross slip in su-
peralloys, leading to faster dislocation movement and defect
formation [144].
Our paper aimed to build a framework such that a uniform
set of features is deemed sufﬁcient for calculating all the
crucial mechanical properties. The primary features selected
are mutually independent, as seen from Figs. S3– S7, with
minimal cross correlations. The inclusion of these primary
features is sufﬁcient for accurate property prediction and it
reduces the need for the calculation of other complex derived
parameters for property prediction. Moreover, the ML mod-
els developed in this paper give a more accurate prediction
without partitioning the data into different regimes, as usually
seen in the case of the low-cycle and high-cycle fatigue or
for the different mechanisms of creep rupture. GPR models
with quadratic kernels provide very high accuracy for predict-
ing YS and UTS, while Matern kernels are best suited for
predicting creep and fatigue strength. The quadratic kernel
is sufﬁcient for accurate prediction since YS and UTS are
properties with relatively more straightforward mechanisms.
However, creep and fatigue strength are complex properties
with several competing mechanisms and damage accumula-
tion over time; therefore, it is difﬁcult to model them using
simpler kernel algorithms. Severe overﬁtting of the quadratic
kernel-based models is a direct result of the same. On the
other hand, GPR, which ﬁts the data to an advanced ker-
nel, is highly suited for predicting complex properties such
as creep and fatigue strength. To compare with other ML
algorithms, we also trained the models using SVR and XG-
Boost, presented in Supplemental Material Table 6. The ML
models trained using other algorithms perform poorly when
compared to the GPR models. The relatively low rmse val-
ues for all the GPR-based models in this paper demonstrate
the effectiveness of the GPR for modeling the mechanical
properties.
IV . DISCUSSION
To test the applicability of ML models developed in this
paper, we performed validation tests by collecting new data
to test the ML models [ 122,145–154]. The validation of the
ML models was performed to check whether the ML models
are able to predict properties of the unknown data set. We
collected experimental data for all the mechanical properties,
including YS, UTS, creep, and fatigue strength, and the cor-
responding composition, annealing, and testing parameters.
In total, we collected 78 new data. The data was collected
from literature and the source (DOI) of the data is present in
Supplemental Material Table 1. The elemental features were
generated for the new data set, and the data was then stan-
dardized using standard scalar with already ﬁtted parameters.
The data was then subjected to the same approach employed
for the test data set. Each ML model developed has a different
set of features for the prediction of the target property. We
selected the features required from the new data to predict
each mechanical property using our ML models. The results
of the validation test are plotted in Figs. S8– S11. The valida-
tion results reveal that the ML models predict the mechanical
properties of unknown data with high accuracy. All data lies
within the range of ±0.5 from the black line, indicating highly
precise predictions. Moreover, it can be observed that the ML
models built in this paper can be utilized directly without any
additional operations for predicting the properties of unique
superalloys.
The ML models developed in this paper using GPR involve
highly complex algorithms for training. This renders the ML
models essentially as black boxes which are difﬁcult to in-
terpret directly. To analyze our best ML models, we employ
SHapley Additive exPlanations (SHAP) to reveal the effect of
individual features on the ML model [ 155–157]. The details
of SHAP implementation are presented in the Supplemental
Material. We study the effects of critical elemental concentra-
tions on the creep and fatigue properties of the superalloys.
123603-8

## Page 9

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
FIG. 5. SHAP force plot for some individual data set demonstrating the effects of rhenium addition on the creep rupture life of the material.
The red arrows indicate that addition of a feature leads to increase of creep rupture life, while blue arrows represent that addition of the feature
leads to decrease of rupture life.
One of the most important elements responsible for strength-
ening at high temperatures is rhenium. Rhenium is used for
solid solution strengthening and enhances creep-resistance
properties by arresting the growth of γ
′ phase particles by
introducing more signiﬁcant lattice misﬁts, which limit the
movement of dislocations and diffusion of atoms [ 158–160].
In addition, the introduction of rhenium to superalloys can ef-
fectively increase fatigue resistance [ 46] of superalloys. From
the ML models developed for creep and fatigue in this paper, it
may initially seem that rhenium is not identiﬁed as an impor-
tant parameter. However, through SHAP analysis of the ML
model, we ﬁnd that rhenium indeed plays a crucial role in in-
creasing the creep resistance of superalloys. The SHAP force
plot is shown in Fig. 5 to demonstrate the effect of rhenium. In
Fig. 5, the base values represent the average value of the creep
rupture life when no feature is revealed to the ML model. In
this case, the ML model relies on the average values of all
features in the data set. The red and blue arrows represent the
effect of introducing individual features on the ﬁnal output
value of creep rupture life. The red arrow represents that the
addition of a feature leads to an increase in the rupture life
over the base value, while the blue arrow represents that the
addition of a feature value leads to a decrease in rupture life.
The length of the arrows represents the magnitude or relative
importance of an individual feature. From Fig. 5, it is observed
that rhenium addition leads to a signiﬁcant increase in the
creep rupture life of superalloys. The contribution of rhenium
for increasing the rupture life is similar in magnitude in most
cases. The ﬁndings are similar to experimental study, where
rhenium containing alloy shows the best creep properties be-
cause of solid solution strengthening in the γ phase and low
diffusion coefﬁcients at high temperatures, leading to effective
resistance to dislocation motion in the γ [161]. From the force
plot, it is also inferred that elements like titanium, cobalt, and
molybdenum also contribute signiﬁcantly in increasing the
creep rupture life of a material. The temperature of creep test
(T) and stress are the two most important factors that reduce
the rupture life of superalloys.
123603-9

## Page 10

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
FIG. 6. SHAP dependence plot for rhenium addition on creep
rupture life of the superalloys.
To further analyze the effect of elemental composition on
creep and fatigue life of superalloys, we plot the dependence
plot for elemental concentrations using SHAP . Figure6 shows
the dependence plot for rhenium addition on creep rupture
life. The vertical line (E[Re]) represents the average com-
position of around 2% of rhenium and the horizontal line
represents the expected value of the model. From Fig. 6,i t
is inferred that rhenium composition above 1.35% is highly
beneﬁcial for the creep properties of superalloys. According
to the ML model developed, the best effect is observed for rhe-
nium composition of 4%. The advantage of creep properties
diminishes on further addition of rhenium. After the composi-
tion of 6.4%, the addition of rhenium becomes harmful for the
superalloys. The results of the ML model are consistent with
experimental results, where it is reported that the addition of
large amounts of rhenium leads to precipitation of harmful
TCP phases, which signiﬁcantly decrease the creep resistance
of superalloys [ 162,163]. Similarly, SHAP-dependence plot
analysis for creep strengthening elements such as C, Cr, Co,
Nb, Ta, Ti, W is presented in the Supplemental Material in
Figs. S12– S18. The optimum range of compositions for the
elements for increasing the creep rupture is predicted through
the ML model. This range is presented in Table II. The forma-
tion of carbide phases limits the range of carbon addition. The
ML model predicts that the elements Co, Cr, Ta, Ti, and W
are beneﬁcial in a wide composition range for creep rupture
strength. A similar analysis for fatigue is presented in the
Supplemental Material. The dependence plots for elemental
concentrations for fatigue life are plotted in Figs. S-19– S-23.
TABLE II. Ideal range of composition (in %) for creep rupture life.
Element Lower limit Upper limit
C0 1
Co 0 12
Cr 0 14
Nb 0 0.3
Re 1.35 6.4
Ta 1
Ti 0 1.2
W0 7
TABLE III. Ideal range of composition (in %) for fatigue life.
Element Lower limit Upper limit
C 0 0.06
Co 0 7.6
Mo 0 2.75
Nb 0.15 4.4
Ti 2
Using the best ML models for fatigue, we predicted the best
range for different elements. The range of the ideal compo-
sitions are presented in Table III. It is seen that the addition
of titanium and molybdenum has a signiﬁcant impact on the
fatigue life of superalloys. Similarly, adding cobalt in fewer
quantities is beneﬁcial for fatigue properties.
After accessing the feature importance for all the proper-
ties, it is essential to develop a framework encompassing a
set of uniﬁed ML models for the mechanical properties that
reﬂect the impact of all the important features. Developing
such models is vital to capture all the intricate feature-property
relationships of Ni-based superalloys. We analyzed all the
GPR-based ML model features for all mechanical properties.
The chosen features for individual property prediction are
present in Figs. 3 and 4. It can be seen that the feature space
varies widely for different properties. Therefore, we aim to
identify standard features for developing the unifying ML
models. While selecting features, it has to be ascertained that
the features highly correlated to any mechanical property are
not excluded. We ﬁrst include all the features present in at
least three of the ﬁve ML models developed, leading to the
selection of 15 features. We observe that the compositions
of some selected elements do not possess a signiﬁcant cor-
relation to any of the properties. We, therefore, drop these
compositions and instead include all the annealing parameters
and highly correlated compositions from each property. The
list consists of 15 features using ML models for the mechani-
cal properties which we developed. The results of the uniﬁed
ML models are presented in Table IV. It can be observed
that several ML models are developed for a wide range of
mechanical properties through target selection of the highly
correlated features. The uniﬁed ML models developed in this
paper are developed using Python libraries and are exported
using the Joblib library, making them highly transferable and
directly employable for the prediction of mechanical prop-
erties without any additional requirements. To the best of
TABLE IV . Results for the unifying ML models utilizing com-
mon set of features for prediction.
GPR models
Property R2 rmse
YS 0.96 /0.96 0.11 /0.11
UTS 0.98 /0.97 0.07 /0.08
Creep 0.99 /0.97 0.15 /0.28
Fatigue stress 0.96 /0.95 0.74 /0.75
Fatigue strain 0.95 /0.94 0.51 /0.51
123603-10

## Page 11

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
the authors’ knowledge, no such parallel framework exists in
literature which predicts all the mechanical properties with
high accuracy.
The results can be further improved if contributions from
elements such as cerium and lanthanum, which are crucial
for oxidation resistance of superalloys, are also added in
the study. Since the focus of this paper is on mechanical
properties only, we excluded the contribution from these ele-
ments. The presence of impurities such as sulfur, phosphorus,
and nitrogen can also lead to local changes in the physical
characteristics, which are not considered in this paper. Other
parameters such as the microstructure and strain rate can also
be explored in further research. In this paper, we explore ML-
driven approaches to streamline and accelerate the process of
discovery of unique superalloys. The approach will be useful
for designing materials at reduced costs and can be extended
to other classes of materials.
V . CONCLUSIONS
In this paper, we have developed a uniﬁed ML framework
for predicting mechanical properties of Ni-based superalloys
using the feature reduction technique LASSO and ML. Most
basic features such as composition, heat treatment conditions,
and mechanical testing conditions are employed in this study,
and the most dominant features are selected using LASSO
for ML model development. GPR-based models are used to
predict YS, tensile strength, creep rupture life, and fatigue
life (employing stress and strain as features). The ML models
developed for the mechanical properties have unprecedented
accuracy. The ML models in this paper eliminate the need to
partition the data for different regimes of creep and fatigue.
The models show low errors when validated using unseen data
from the literature. Further, SHAP analysis of the ML models
developed reveals essential characteristics of the individual
constituent elements. The ideal composition of elements is
determined for creep and fatigue by analyzing the SHAP de-
pendence plot. Finally, using feature engineering, we identify
essential features for developing a uniﬁed ML framework for
simultaneous prediction of all mechanical properties. The ap-
proach developed in this paper is highly transferable to other
classes of materials/properties with minimal modiﬁcations.
The data required to reproduce these ﬁndings will be made
available on GitHub.
ACKNOWLEDGMENTS
The authors acknowledge ﬁnancial support from
Aeronautics Research Development Board (ARDB),
Ministry of Defence, India under Grant No.
ARDB/GTMAP/01/2031993/M/I. The authors thank
the support from Materials Informatics Initiative of IISc
(MI3). The authors acknowledge the support from the
Institute of Eminence (IoE) scheme of The University Grants
Commission (UGC), India. The authors thank Materials
Research Centre (MRC) and Supercomputer Education and
Research Centre (SERC) at Indian Institute of Science,
Bangalore for providing the required computational facilities.
N.K. acknowledges Sucheta Swetlana of Materials Research
Centre, IISC, for her valuable insights and suggestions.
[1] R. Reed and C. Rae, Physical Metallurgy , 5th ed. (Elsevier,
UK, 2014), p. 2215.
[2] A. P . Mouritz,Introduction to Aerospace Materials(Woodhead
Publishing, Cambridge, UK, 2012), p. 251.
[3] J. Cormier, X. Milhet, and J. Mendez, Non-isothermal
creep at very high temperature of the nickel-based
single crystal superalloy MC
2, Acta Mater. 55, 6250
(2007).
[4] X. Zhou, T. Ma, Y . Li, L. Li, K. Wang, Y . Zhang, Y . Lai,
and P . Zhang, Secondary γ ’ evolution and relationship to hot
deformation behavior of a supersolvus-treated superalloy with
high precipitate volume fraction, Mater. Sci. Eng. A. 761,
138046 (2019).
[5] M. J. Donachie and S. J. Donachie, Superalloys: A Technical
Guide (ASM international, Ohio, USA, 2002).
[6] P . Caron and T. Khan, Evolution of Ni-based superalloys
for single crystal gas turbine blade applications, Aerosp. Sci.
Technol. 3, 513 (1999) .
[7] R. Schafrik and R. Sprague, Gas turbine materials, Adv. Mater.
Process 5, 29 (2004).
[8] H. Long, S. Mao, Y . Liu, Z. Zhang, and X. Han, Microstruc-
tural and compositional design of Ni-based single crystalline
superalloys—a review, J. Alloys Compd. 743, 203 (2018) .
[9] W. Xia, X. Zhao, L. Y ue, and Z. Zhang, A review of composi-
tion evolution in Ni-based single crystal superalloys, J. Mater.
Sci. Technol. 44, 76 (2020) .
[10] K. Kakehi, Effect of primary and secondary precipitates on
creep strength of Ni-base superalloy single crystals, Mater.
Sci. Eng. A 278, 135 (2000) .
[11] T. Murakumo, Y . Koizumi, K. Kobayashi, and H. Harada,
Creep strength of Ni-base single-crystal superalloys on the
γ /γ ’ tie-line, Superalloys 2004, 155 (2004) .
[12] E. Nembach and G. Neite, Precipitation hardening of su-
peralloys by ordered γ
′-particles, Prog. Mater. Sci. 29, 177
(1985).
[13] A. Heckl, S. Neumeier, M. Göken, and R. Singer, The effect of
R ea n dR uo n γ /γ′ microstructure, γ -solid solution strength-
ening and creep strength in nickel-base superalloys, Mater.
Sci. Eng. A 528, 3435 (2011).
[14] B. Wang, J. Zhang, T. Huang, H. Su, Z. Li, L. Liu, and H. Fu,
Inﬂuence of W, Re, Cr, and Mo on microstructural stability
of the third generation Ni-based single crystal superalloys,
J. Mater. Res. 31, 3381 (2016).
[15] K. A. Christoﬁdou, M. C. Hardy, H.-Y . Li, C. Argyrakis, H.
Kitaguchi, N. G. Jones, P . M. Mignanelli, A. S. Wilson, O. M.
M e s s é ,E .J .P i c k e r i n get al. , On the effect of Nb on the mi-
crostructure and properties of next generation polycrystalline
powder metallurgy Ni-based superalloys, Metall. Mater. Trans.
A 49, 3896 (2018) .
[16] R. K. Barik and A. K. Singh, Accelerated discovery of the
valley-polarized quantum anomalous Hall effect in MXenes,
Chem. Mater. 33, 6311 (2021).
123603-11

## Page 12

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
[17] G. Pilania, C. Wang, X. Jiang, S. Rajasekaran, and R.
Ramprasad, Accelerating materials property predictions using
machine learning, Sci. Rep. 3, 2810 (2013) .
[18] R. Ramprasad, R. Batra, G. Pilania, A. Mannodi-
Kanakkithodi, and C. Kim, Machine learning in materials
informatics: Recent applications and prospects, Npj Comput.
Mater. 3, 54 (2017) .
[19] Y . Liu, T. Zhao, W. Ju, and S. Shi, Materials discovery and
design using machine learning, J. Materiomics 3, 159 (2017) .
[20] A. C. Rajan, A. Mishra, S. Satsangi, R. V aish, H. Mizuseki,
K.-R. Lee, and A. K. Singh, Machine-learning-assisted ac-
curate band gap predictions of functionalized MXene, Chem.
Mater. 30, 4031 (2018) .
[21] J. Lee, A. Seko, K. Shitara, K. Nakayama, and I. Tanaka,
Prediction model of band gap for inorganic compounds by
combination of density functional theory calculations and ma-
chine learning techniques, P h y s .R e v .B93, 115104 (2016).
[22] R. Gurnani, D. Kamal, H. Tran, H. Sahu, K. Scharm, U.
Ashraf, and R. Ramprasad, polyg2g: A novel machine learn-
ing algorithm applied to the generative design of polymer
dielectrics, Chem. Mater. 33, 7008 (2021).
[23] A. Mishra, S. Satsangi, A. C. Rajan, H. Mizuseki, K.-R. Lee,
and A. K. Singh, Accelerated data-driven accurate positioning
of the band edges of MXenes, J. Phys. Chem. Lett. 10, 780
(2019).
[24] R. Juneja, G. Y umnam, S. Satsangi, and A. K. Singh, Coupling
the high-throughput property map to machine learning for
predicting lattice thermal conductivity, Chem. Mater. 31, 5145
(2019).
[25] C. Kim, A. Chandrasekaran, A. Jha, and R. Ramprasad,
Active-learning and materials design: the example of high
glass transition temperature polymers, MRS Commun. 9, 860
(2019).
[ 2 6 ]L .C h e n ,C .K i m ,R .B a t r a ,J .P .L i g h t s t o n e ,C .W u ,Z .L i ,
A. A. Deshmukh, Y . Wang, H. D. Tran, P . V ashishta et al. ,
Frequency-dependent dielectric constant prediction of poly-
mers using machine learning, Npj Comput. Mater. 6, 1 (2020).
[27] S. Swetlana, N. Khatavkar, and A. K. Singh, Development
of Vickers hardness prediction models via microstructural
analysis and machine learning, J. Mater. Sci. 55, 15845
(2020).
[28] N. Khatavkar, S. Swetlana, and A. K. Singh, Accelerated pre-
diction of Vickers hardness of Co-and Ni-based superalloys
from microstructure and composition using advanced image
processing techniques and machine learning, Acta Mater. 196,
295 (2020).
[29] W. Huang, P . Martin, and H. L. Zhuang, Machine-learning
phase prediction of high-entropy alloys, Acta Mater. 169, 225
(2019).
[30] C. Wen, Y . Zhang, C. Wang, D. Xue, Y . Bai, S. Antonov, L.
Dai, T. Lookman, and Y . Su, Machine learning assisted design
of high entropy alloys with desired property, Acta Mater. 170,
109 (2019).
[31] K. Kaufmann and K. S. V ecchio, Searching for high entropy
alloys: A machine learning approach, Acta Mater. 198, 178
(2020).
[32] B. Conduit, N. G. Jones, H. J. Stone, and G. J. Conduit, Design
of a nickel-base superalloy using a neural network, Mater. Des.
131, 358 (2017) .
[33] P . L. Taylor and G. Conduit, Machine learning predictions of
superalloy microstructure, Comput. Mater. Sci. 201, 110916
(2022).
[34] Y . Zhang and X. Xu, Lattice misﬁt predictions via the Gaus-
sian process regression for Ni-based single crystal superalloys,
Met. Mater. Int. 27, 235 (2021) .
[35] H. Hong, J. Kang, B. G. Choi, I. Kim, Y . Y oo, and C. Jo,
A comparative study on thermomechanical and low cycle fa-
tigue failures of a single crystal nickel-based superalloy, Int. J.
Fatigue 33, 1592 (2011) .
[36] P . R. Barrett, R. Ahmed, M. Menon, and T. Hassan, Isothermal
low-cycle fatigue and fatigue-creep of Haynes 230, Int. J.
Solids Struct. 88-89, 146 (2016) .
[37] B. Du, J. Y ang, C. Cui, and X. Sun, Effects of grain size on the
high-cycle fatigue behavior of IN792 superalloy, Mater. Des.
65, 57 (2015) .
[38] A. Sengupta, S. Putatunda, L. Bartosiewicz, J. Hangas, P .
Nailos, M. Peputapeck, and F. Alberts, Tensile behavior of
a new single-crystal nickel-based superalloy (CMSX-4) at
room and elevated temperatures, J. Mater. Eng. Perform. 3,7 3
(1994).
[39] T. Khan and P . Caron, Effect of processing conditions
and heat treatments on mechanical properties of single-
crystal superalloy CMSX-2, Mater. Sci. Technol. 2, 486
(1986).
[40] B. Wilson, E. Cutler, and G. Fuchs, Effect of solidiﬁcation
parameters on the microstructures and properties of CMSX-
10, Mater. Sci. Eng. A 479, 356 (2008) .
[41] L. Liu, T. Huang, J. Zhang, and H. Fu, Microstructure and
stress rupture properties of single crystal superalloy CMSX-2
under high thermal gradient directional solidiﬁcation, Mater.
Lett. 61, 227 (2007).
[42] K. Harris and J. B. Wahl, Improved single crystal superalloys,
CMSX-4 (SLS)[La+Y] and CMSX-486, Superalloys 2004,4 5
(2004).
[43] M. Acharya and G. Fuchs, The effect of long-term thermal
exposures on the microstructure and properties of CMSX-10
single crystal Ni-base superalloys, Mater. Sci. Eng. A 381, 143
(2004).
[44] K. Harris, G. Erickson, and R. Schwer, MAR-M247
derivations-CM247 LC DS alloy, CMSX single crystal alloys,
properties and performance, Superalloys 221 (1984).
[45] J. V eys and R. Mevrel, Inﬂuence of protective coatings on the
mechanical properties of CMSX-2 and Cotac 784, Mater. Sci.
Eng. 88, 253 (1987).
[46] G. Erickson, The development and application of CMSX-10,
Superalloys 35 (1996).
[47] K. Fullagar, R. Broomﬁeld, M. Hulands, K. Harris, G.
Erickson, and S. Sikkenga, Aero engine test experience with
CMSX-4® alloy single-crystal turbine blades, J. Eng. Gas
Turbines Power
118, 380 (1996) .
[48] J. B. Wahl and K. Harris, New single crystal superalloys,
CMSX®-8 and CMSX®-7, in Turbo Expo: Power for Land,
Sea, and Air (American Society of Mechanical Engineers,
Düsseldorf, Germany, 2014), V ol. 45752, p. V006T22A002.
[49] P . Xia, J. Y u, X. Sun, H. Guan, and Z. Hu, Inﬂuence of thermal
exposure on γ ’ precipitation and tensile properties of DZ951
alloy, Mater. Charact. 58, 645 (2007) .
[50] C. Körner, M. Ramsperger, C. Meid, D. Bürger, P .
Wollgramm, M. Bartsch, and G. Eggeler, Microstructure and
mechanical properties of CMSX-4 single crystals prepared
123603-12

## Page 13

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
by additive manufacturing, M e t a l l .M a t e r .T r a n s .A49, 3781
(2018).
[51] V . Sabelkin, G. Joshi, S. Mall, W. Porter, and R. John, Mono-
tonic tension and creep behavior of single crystal CMSX-486
under combustion environment, Mater. Sci. Eng. A 569, 106
(2013).
[52] J. Lapin, T. Pelachová, and O. Bajana, The effect
of microstructure on mechanical properties of single
crystal CMSX-4 superalloy, in Proceedings of the 22nd
International Conference on Metallurgy and Materials,
Metal (Tanger, Brno, Czech Republic, EU, 2013),
p. 1277.
[53] T. Coppola, S. Riscifuli, O. Tassa, and G. Pasquero, Ther-
momechanical fatigue behavior of bare and coated CMSX-4,
J. Eng. Gas Turbines Power 132, 012101 (2010) .
[54] A. Sengupta and S. K. Putatunda, Dynamic strain aging in a
new single crystal nickel-based superalloy (CMSX-4), J. Test.
Eval. 23, 87 (1995) .
[55] A. Sato, J. J. Moverare, M. Hasselqvist, and R. C. Reed, On
the mechanical behavior of a new single-crystal superalloy for
industrial gas turbine applications, Metall. Mater. Trans. A 43,
2302 (2012).
[56] J. Lapin, T. Pelachova, and M. Gebura, The effect of
creep exposure on microstructure stability and tensile prop-
erties of single crystal nickel based superalloy CMSX-4,
Kovove Mater. 50, 379 (2012).
[57] R. Reed, N. Matan, D. Cox, M. Rist, and C. Rae, Creep of
CMSX-4 superalloy single crystals: Effects of rafting at high
temperature, Acta Mater. 47, 3367 (1999).
[58] A. Sato, H. Harada, A.-C. Y eh, K. Kawagishi, T. Kobayashi,
Y . Koizumi, T. Y okokawa, and J. Zhang, A 5th generation
SC superalloy with balanced high temperature properties and
processability, Superalloys 131 (2008).
[59] A. Basak and S. Das, Effect of heat treatment on the mi-
crostructures of CMSX-4® processed through scanning laser
epitaxy (SLE), in 2017 International Solid Freeform Fabrica-
tion Symposium (University of Texas at Austin, Austin, Texas,
USA, 2017).
[60] J. B. Wahl and K. Harris, Improved 3rd generation single
crystal superalloy CMSX-4® plus (SLS)-a study of evolution-
ary alloy development (Cannon-Muskegon, Muskegon, MI,
1984).
[61] M. D. Fitzpatrick, W. D. Brentnall, A. Meier, G. L.
Erickson, and G. DeBoer, Design of a high efﬁciency
industrial turbine blade utilizing third generation single
crystal alloy CMSX®-10, in Turbo Expo: Power for
Land, Sea, and Air (American Society of Mechanical
Engineers, Orlando, Florida, USA, 1997), V ol. 78712,
p. V004T12A022.
[62] K. Kobayashi, K. Y amaguchi, M. Hayakawa, and M. Kimura,
High-temperature fatigue properties of austenitic superalloys
718, A286 and 304L, Int. J. Fatigue 30, 1978 (2008) .
[63] M. Lamm and R. Singer, The effect of casting conditions on
the high-cycle fatigue properties of the single-crystal nickel-
base superalloy PW A 1483, Metall. Mater. Trans. A 38, 1177
(2007).
[64] J. Tian, J. Villegas, W. Y uan, D. Fielden, L. Shaw, P . Liaw, and
D. Klarstrom, A study of the effect of nanostructured surface
layers on the fatigue behaviors of a C-2000 superalloy, Mater.
Sci. Eng. A 468-470, 164 (2007) .
[65] K. Rahmani and S. Nategh, Inﬂuence of aluminide diffusion
coating on low cycle fatigue properties of René 80, Mater. Sci.
Eng. A 486, 686 (2008) .
[66] S. Lee, Y . Lu, P . Liaw, L. Chen, S. Thompson, J. Blust,
P . Browning, A. Bhattacharya, J. Aurrecoechea, and D.
Klarstrom, Tensile-hold low-cycle-fatigue properties of solid-
solution-strengthened superalloys at elevated temperatures,
Mater. Sci. Eng. A 504, 64 (2009) .
[67] Z. Shi, X. Wang, S. Liu, and J. Li, Low cycle fatigue proper-
ties and microstructure evolution at 760
◦C of a single crystal
superalloy, Prog. Nat. Sci.: Mater. Int. 25, 78 (2015) .
[68] T. Billot, P . Villechaise, M. Jouiad, and J. Mendez,
Creep–fatigue behavior at high temperature of a UDIMET
720 nickel-base superalloy, Int. J. Fatigue 32, 824
(2010).
[69] R. Kowalewski and H. Mughrabi, Inﬂuence of a plasma-
sprayed NiCrAlY coating on the low-cycle fatigue behaviour
of a directionally solidiﬁed nickel-base superalloy, Mater. Sci.
Eng. A 247, 295 (1998) .
[70] Y . Ro, H. Zhou, Y . Koizumi, T. Y okokawa, T. Kobayashi, H.
Harada, and I. Okada, Thermal-mechanical fatigue property
of Ni-base single crystal superalloys TMS-82 + and TMS-75,
Mater. Trans. 45, 396 (2004).
[71] M. Aydinöz, F. Brenne, M. Schaper, C. Schaak, W. Tillmann,
J. Nellesen, and T. Niendorf, On the microstructural and me-
chanical properties of post-treated additively manufactured
Inconel 718 superalloy under quasi-static and cyclic loading,
Mater. Sci. Eng. A 669, 246 (2016) .
[72] L. Chen, Z. Wang, G. Y ao, and J. Tian, The inﬂuence of
temperature on low cycle fatigue behavior of nickel base su-
peralloy GH4049, Int. J. Fatigue 21, 791 (1999) .
[73] J. Y u, X. Sun, T. Jin, N. Zhao, H. Guan, and Z. Hu, High
temperature creep and low cycle fatigue of a nickel-base su-
peralloy, Mater. Sci. Eng. A 527, 2379 (2010).
[74] P . Zhang, Q. Zhu, C. Hu, C.-j. Wang, G. Chen, and H.-y. Qin,
Cyclic deformation behavior of a nickel-base superalloy under
fatigue loading, Mater. Des. 69, 12 (2015) .
[75] H.-E. Huang and C.-H. Koo, Characteristics and mechanical
properties of polycrystalline CM 247 LC superalloy casting,
Mater. Trans. 45, 562 (2004).
[76] J. Gayda and R. Miner, Fatigue crack initiation and propaga-
tion in several nickel-base superalloys at 650 C, Int. J. Fatigue
5, 135 (1983) .
[77] J. Miao, T. M. Pollock, and J. W. Jones, Crystallographic
fatigue crack initiation in nickel-based superalloy René 88DT
at elevated temperature, Acta Mater. 57, 5964 (2009) .
[78] A. Mostafaei, S. H. V . R. Neelapu, C. Kisailus, L. M. Nath,
T. D. Jacobs, and M. Chmielus, Characterizing surface ﬁnish
and fatigue behavior in binder-jet 3D-printed nickel-based su-
peralloy 625, Addit. Manuf. 24, 200 (2018).
[79] Y . Itoh, M. Saitoh, and Y . Ishiwata, Inﬂuence of high-
temperature protective coatings on the mechanical properties
of nickel-based superalloys, J. Mater. Sci. 34, 3957 (1999) .
[80] Y . Jinxia, Q. Zheng, S. Xiaofeng, G. Hengrong, and H.
Zhuangqi, Thermal fatigue behavior of K465 superalloy, Rare
Met. 25, 202 (2006).
[81] M. Ott and H. Mughrabi, Dependence of the high-temperature
low-cycle fatigue behaviour of the monocrystalline nickel-
base superalloys CMSX-4 and CMSX-6 on the γ /γ ’ morphol-
ogy, Mater. Sci. Eng. A 272, 24 (1999) .
123603-13

## Page 14

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
[82] J. Gayda, T. Gabb, and R. Miner, Fatigue crack propagation
of nickel-base superalloys at 650 ◦C, in Symp. on Low-Cycle
Fatigue Directions for the Future , NAS 1.15: 87150 (ASTM
International, New Y ork, USA, 1985).
[83] J. Li and R. Wahi, Investigation of γ /γ ’ lattice mismatch in the
polycrystalline nickel-base superalloy IN738LC : Inﬂuence of
heat treatment and creep deformation, Acta Metall. Mater. 43,
507 (1995).
[84] C. Cui, Y . Gu, Y . Y uan, T. Osada, and H. Harada, Enhanced
mechanical properties in a new Ni–Co base superalloy by
controlling microstructures, Mater. Sci. Eng. A 528, 5465
(2011).
[85] P . Li, S.-S. Li, and Y .-S. Han, Inﬂuence of solution heat
treatment on microstructure and stress rupture properties of a
Ni3Al base single crystal superalloy IC6SX, Intermetallics 19,
182 (2011).
[86] L.-R. Liu, T. Jin, N.-R. Zhao, Z. Wang, X. Sun, H. Guan, and
Z. Hu, Effect of carbon addition on the creep properties in a
Ni-based single crystal superalloy, Mater. Sci. Eng. A 385, 105
(2004).
[87] X. Qin, J. Guo, C. Y uan, J. Hou, L. Zhou, and H. Y e, Long-
term thermal exposure responses of the microstructure and
properties of a cast Ni-base superalloy, Mater. Sci. Eng. A 543,
121 (2012).
[88] C. Tian, G. Han, C. Cui, and X. Sun, Effects of Co content
on tensile properties and deformation behaviors of Ni-based
disk superalloys at different temperatures, Mater. Des. 88, 123
(2015).
[89] D. Kaoumi and K. Hrutkay, Tensile deformation behavior and
microstructure evolution of Ni-based superalloy 617, J. Nucl.
Mater. 454, 265 (2014) .
[90] X. Xiong, D. Quan, P . Dai, Z. Wang, Q. Zhang, and Z. Y ue,
Tensile behavior of nickel-base single-crystal superalloy DD6,
Mater. Sci. Eng. A 636, 608 (2015) .
[91] C. Boehlert and S. Longanbach, A comparison of the mi-
crostructure and creep behavior of cold rolled HA YNES ® 230
alloy and HA YNES ® 282 alloy, Mater. Sci. Eng. A 528, 4888
(2011).
[92] K. Hrutkay and D. Kaoumi, Tensile deformation behavior of a
nickel based superalloy at different temperatures, Mater. Sci.
Eng. A 599, 196 (2014) .
[93] G. Chen, Y . Zhang, D. Xu, Y . Lin, and X. Chen, Low cycle
fatigue and creep-fatigue interaction behavior of nickel-base
superalloy GH4169 at elevated temperature of 650 C, Mater.
Sci. Eng. A 655, 175 (2016) .
[94] I. Kim, B. Choi, H. Hong, J. Do, and C. Jo, Inﬂuence of ther-
mal exposure on the microstructural evolution and mechanical
properties of a wrought Ni-base superalloy, Mater. Sci. Eng. A
593, 55 (2014) .
[95] D.-X. Wen, Y . Lin, J. Chen, X.-M. Chen, J.-L. Zhang,
Y .-J. Liang, and L.-T. Li, Work-hardening behaviors of
typical solution-treated and aged Ni-based superalloys
during hot deformation, J. Alloys Compd. 618, 372
(2015).
[96] J. Wang, W.-G. Guo, Y . Su, P . Zhou, and K. Y uan, Anomalous
behaviors of a single-crystal Nickel-base superalloy over a
wide range of temperatures and strain rates, Mech. Mater. 94
,
79 (2016).
[97] T. Wang, C. Wang, W. Sun, X. Qin, J. Guo, and L. Zhou, Mi-
crostructure evolution and mechanical properties of GH984G
alloy with different Ti/Al ratios during long-term thermal ex-
posure, Mater. Des. 62, 225 (2014) .
[98] J. Shingledecker, N. Evans, and G. Pharr, Inﬂuences of com-
position and grain size on creep–rupture behavior of Inconel®
alloy 740, Mater. Sci. Eng. A 578, 277 (2013) .
[99] F. Y ang, E. Liu, Z. Zhi, J. Tong, and L. Ning, Inﬂuence of Ti
content on microstructure, mechanical properties and castabil-
ity of directionally solidiﬁed superalloy DZ125L, Mater. Des.
61, 41 (2014) .
[100] X. Wang, J. Liu, T. Jin, and X. Sun, Tensile behaviors and
deformation mechanisms of a nickel-base single crystal super-
alloy at different temperatures, Mater. Sci. Eng. A 598, 154
(2014).
[101] Y . Y uan, Y . Gu, C. Cui, T. Osada, T. Tetsui, T. Y okokawa,
and H. Harada, Creep mechanisms of U720Li disc superalloy
at intermediate temperature, Mater. Sci. Eng. A 528, 5106
(2011).
[102] J. Zhang, T. Murakumo, Y . Koizumi, and H. Harada, The
inﬂuence of interfacial dislocation arrangements in a fourth
generation single crystal TMS-138 superalloy on creep prop-
erties, J. Mater. Sci. 38, 4883 (2003).
[103] H. Bor, C. Chao, and C. Ma, The inﬂuence of magnesium on
carbide characteristics and creep behavior of the Mar-M247
superalloy, Scr. Mater. 38, 329 (1997) .
[104] See Supplemental Material at http://link.aps.org/supplemental/
10.1103/PhysRevMaterials.6.123603 for details regarding the
data, ML models, and supplemental ﬁgures.
[105] R. Tibshirani, Regression shrinkage and selection via the lasso,
J. R. Stat. Soc., B: Stat. Methodol 58, 267 (1996).
[106] Y . Liu, B. Guo, X. Zou, Y . Li, and S. Shi, Ma-
chine learning assisted materials design and discovery
for rechargeable batteries, Energy Storage Mater. 31, 434
(2020).
[107] Y . Liu, J.-M. Wu, M. Avdeev, and S.-Q. Shi, Multi-layer
feature selection incorporating weighted score-based expert
knowledge toward modeling materials with targeted proper-
ties, Adv. Theory Simul. 3, 1900215 (2020).
[108] K. P . Murphy, Machine Learning: A Probabilistic Perspective
(MIT Press, Cambridge, UK, 2012).
[109] J. Quinonero-Candela and C. E. Rasmussen, A unifying view
of sparse approximate Gaussian process regression, J. Mach.
Learn. Res. 6, 1939 (2005).
[110] J. Benesty, J. Chen, Y . Huang, and I. Cohen, Noise Reduction
in Speech Processing (Springer, Berlin, Heidelberg, 2009).
[111] F. Pedregosa, G. V aroquaux, A. Gramfort, V . Michel, B.
Thirion, O. Grisel, M. Blondel, P . Prettenhofer, R. Weiss,
V . Dubourg et al. , Scikit-learn: Machine learning in Python,
J. Mach. Learn. Res. 12, 2825 (2011).
[112] X. Zhou, F. Zhou, and M. Naseri, An insight into the estima-
tion of frost thermal conductivity on parallel surface channels
using kernel based GPR strategy, Sci. Rep. 11, 7203 (2021) .
[113] G. A. Rao, M. Kumar, M. Srinivas, and D. Sarma, Effect of
standard heat treatment on the microstructure and mechanical
properties of hot isostatically pressed superalloy Inconel 718,
Mater. Sci. Eng. A 355
, 114 (2003) .
[114] R. E. Smallman, Modern Physical Metallurgy (Elsevier, UK,
2016).
[115] A. K. Roy and A. V enkatesh, Evaluation of yield strength
anomaly of alloy 718 at 700-800 ◦C, J. Alloys Compd. 496,
393 (2010).
123603-14

## Page 15

HIGHL Y INTERPRETABLE MACHINE LEARNING … PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
[116] P . Geng, W. Li, X. Zhang, Y . Deng, H. Kou, J. Ma, J. Shao,
L. Chen, and X. Wu, A theoretical model for yield strength
anomaly of Ni-base superalloys at elevated temperature, J.
Alloys Compd. 706, 340 (2017) .
[117] D. J. Crudden, B. Raeisinia, N. Warnken, and R. C. Reed,
Analysis of the chemistry of Ni-base turbine disk superalloys
using an alloys-by-design modeling approach, Metall. Mater.
Trans. A 44, 2418 (2013) .
[118] D. Collins and H. Stone, A modelling approach to yield
strength optimisation in a nickel-base superalloy, Int. J. Plast.
54, 96 (2014).
[119] X. Zhang, W. Li, J. Ma, P . Geng, J. Shao, and X. Wu, A novel
temperature dependent yield strength model for metals con-
sidering precipitation strengthening and strain rate, Comput.
Mater. Sci. 129, 147 (2017) .
[120] Y .-K. Kim, D. Kim, H.-K. Kim, E.-Y . Y oon, Y . Lee, C.-S.
Oh, and B.-J. Lee, A numerical model to predict mechanical
properties of Ni-base disk superalloys, Int. J. Plast. 110, 123
(2018).
[121] Y . Y oo, I. Kim, D. Kim, C. Jo, H. Kim, and C. Jones, The
application of neural network to the development of single
crystal superalloys, Superalloys 942 (2004).
[122] C.-N. Wei, H.-Y . Bor, and L. Chang, The effects of carbon
content on the microstructure and elevated temperature tensile
strength of a nickel-base superalloy, Mater. Sci. Eng. A 527,
3741 (2010).
[123] E. Balikci, A. Raman, and R. Mirshams, Tensile strengthen-
ing in the nickel-base superalloy IN738LC, J. Mater. Eng.
Perform. 9, 324 (2000).
[124] G. Bai, J. Li, R. Hu, Z. Tang, X. Xue, and H. Fu, Effect of
temperature on tensile behavior of Ni–Cr–W based superalloy,
Mater. Sci. Eng. A 528, 1974 (2011).
[125] D. Bürger, A. Parsa, M. Ramsperger, C. Körner, and G.
Eggeler, Creep properties of single crystal Ni-base superalloys
(SX): A comparison between conventionally cast and additive
manufactured CMSX-4 materials, Mater. Sci. Eng. A 762,
138098 (2019).
[126] B. Du, Z. Hu, L. Sheng, C. Cui, J. Y ang, Y . Zheng, and X. Sun,
Tensile, creep behavior and microstructure evolution of an as-
cast Ni-based K417G polycrystalline superalloy, J. Mater. Sci.
Technol. 34, 1805 (2018) .
[127] W. Harrison, M. Whittaker, and S. Williams, Recent advances
in creep modelling of the nickel base superalloy, alloy 720Li,
Materials 6, 1118 (2013).
[128] A. Ma, D. Dye, and R. Reed, A model for the creep defor-
mation behaviour of single-crystal superalloy CMSX-4, Acta
Mater. 56, 1657 (2008) .
[129] A. Staroselsky and B. N. Cassenti, Creep, plasticity, and fa-
tigue of single crystal superalloy, Int. J. Solids Struct. 48, 2060
(2011).
[130] D. MacLachlan and D. Knowles, Creep-behavior modeling of
the single-crystal superalloy CMSX-4, Metall. Mater. Trans.
A 31, 1401 (2000) .
[131] W. Xia, X. Zhao, L. Y ue, and Z. Zhang, Microstructural
evolution and creep mechanisms in Ni-based single crys-
tal superalloys: A review, J. Alloys Compd. 819
, 152954
(2020).
[132] Z. Zhu, H. Basoalto, N. Warnken, and R. Reed, A model for
the creep deformation behaviour of nickel-based single crystal
superalloys, Acta Mater. 60, 4888 (2012).
[133] R. MacKay, T. Gabb, and M. Nathal, Microstructure-sensitive
creep models for nickel-base superalloy single crystals, Mater.
Sci. Eng. A 582, 397 (2013) .
[134] P . Wollgramm, H. Buck, K. Neuking, A. Parsa, S. Schuwalow,
J. Rogal, R. Drautz, and G. Eggeler, On the role of Re
in the stress and temperature dependence of creep of Ni-
base single crystal superalloys, Mater. Sci. Eng. A 628, 382
(2015).
[135] Z. Peng, G. Tian, J. Jiang, M. Li, Y . Chen, J. Zou, and
F. P . Dunne, Mechanistic behaviour and modelling of creep in
powder metallurgy FGH96 nickel superalloy, Mater. Sci. Eng.
A 676, 441 (2016) .
[136] Y . Liu, J. Wu, Z. Wang, X.-G. Lu, M. Avdeev, S. Shi, C. Wang,
and T. Y u, Predicting creep rupture life of Ni-based single
crystal superalloys using divide-and-conquer approach based
machine learning, Acta Mater. 195, 454 (2020) .
[137] D. Shin, Y . Y amamoto, M. P . Brady, S. Lee, and J. A. Haynes,
Modern data analytics approach to predict creep of high-
temperature alloys, Acta Mater. 168, 321 (2019) .
[138] Y . Y oo, C. Jo, and C. Jones, Compositional prediction of creep
rupture life of single crystal Ni-base superalloy by Bayesian
neural network, Mater. Sci. Eng. A 336, 22 (2002) .
[139] Y . Xu, Q. Jin, X. Xiao, X. Cao, G. Jia, Y . Zhu, and H.
Yin, Strengthening mechanisms of carbon in modiﬁed nickel-
based superalloy Nimonic 80A, Mater. Sci. Eng. A. 528, 4600
(2011).
[140] L. Wang, D. Wang, T. Liu, X. Li, W. Jiang, G. Zhang, and L.
Lou, Effect of minor carbon additions on the high-temperature
creep behavior of a single-crystal nickel-based superalloy,
Mater. Charact. 104, 81 (2015) .
[141] R. Jiang, D. Bull, A. Evangelou, A. Harte, F. Pierron, I.
Sinclair, M. Preuss, X. Hu, and P . Reed, Strain accumulation
and fatigue crack initiation at pores and carbides in a SX
superalloy at room temperature, Int. J. Fatigue 114, 22 (2018).
[142] M. Huang and J. Zhu, An overview of rhenium effect in single-
crystal superalloys, Rare Metals 35, 127 (2016).
[143] R. Jiang, N. Karpasitis, N. Gao, and P . Reed, Effects of
microstructures on fatigue crack initiation and short crack
propagation at room temperature in an advanced disc super-
alloy, Mater. Sci. Eng. A. 641, 148 (2015) .
[144] A. Pineau and S. D. Antolovich, High temperature fatigue
of nickel-base superalloys–a review with special emphasis on
deformation modes and oxidation, Eng. Fail. Anal. 16, 2668
(2009).
[145] A. Cervellon, J. Cormier, F. Mauget, Z. Hervier, and Y . Nadot,
V ery high cycle fatigue of Ni-based single-crystal superalloys
at high temperature, Metall. Mater. Trans. A 49, 3938 (2018).
[146] T. Murakumo, T. Kobayashi, Y . Koizumi, and H. Harada,
Creep behaviour of Ni-base single-crystal superalloys with
various γ ’ volume fraction, Acta Mater. 52, 3737 (2004).
[147] A.-C. Y eh, A. Sato, T. Kobayashi, and H. Harada, On the
creep and phase stability of advanced Ni-base single crystal
superalloys, Mater. Sci. Eng. A 490, 445 (2008) .
[148] C. Cui, Y . Gu, D. Ping, and H. Harada, Microstructural evo-
lution and mechanical properties of a Ni-based superalloy,
TMW-4, Metall. Mater. Trans. A 40, 282 (2009) .
[149] L. Gong, B. Chen, L. Zhang, Y . Ma, and K. Liu, Effect of
cooling rate on microstructure, microsegregation and mechan-
ical properties of cast Ni-based superalloy K417G, J. Mater.
Sci. Technol. 34, 811 (2018) .
123603-15

## Page 16

NIKHIL KHA TA VKAR AND ABHISHEK KUMAR SINGH PHYSICAL REVIEW MA TERIALS 6, 123603 (2022)
[150] Z. Lian, J. Y u, X. Sun, H. Guan, and Z. Hu, Temperature
dependence of tensile behavior of Ni-based superalloy M951,
Mater. Sci. Eng. A 489, 227 (2008) .
[151] Y . Gu, H. Harada, C. Cui, D. Ping, A. Sato, and J. Fujioka,
New Ni-Co base disk superalloys with higher strength and
creep resistance, Scr. Mater. 55, 815 (2006) .
[152] L. Tan, Y . Li, W. Deng, Y . Liu, F. Liu, Y . Nie, and L. Jiang,
Tensile properties of three newly developed Ni-base powder
metallurgy superalloys, J. Alloys Compd. 804, 322 (2019) .
[153] P . Zhang, Y . Y uan, J. Li, Y . Xu, X. Song, and G. Y ang, Tensile
deformation mechanisms in a new directionally solidiﬁed Ni-
base superalloy containing coarse γ ’ precipitates at 650
◦C,
Mater. Sci. Eng. A 702, 343 (2017) .
[154] S. Jha, M. Caton, and J. Larsen, Mean vs. life-limiting fa-
tigue behavior of a nickel-based superalloy, Superalloys 565
(2008).
[155] S. M. Lundberg and S.-I. Lee, A uniﬁed approach to interpret-
ing model predictions, Adv. Neural. Inf. Process. Syst. 30,1
(2017).
[156] S. M. Lundberg, B. Nair, M. S. V avilala, M. Horibe, M. J.
Eisses, T. Adams, D. E. Liston, D. K.-W. Low, S.-F. Newman,
J. Kim et al., Explainable machine-learning predictions for the
prevention of hypoxaemia during surgery, Nat. Biomed. Eng.
2, 749 (2018).
[157] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin,
B. Nair, R. Katz, J. Himmelfarb, N. Bansal, and S.-I. Lee,
From local explanations to global understanding with explain-
able AI for trees, Nat. Mach. Intell. 2, 56 (2020).
[158] R. C. Reed, The Superalloys: Fundamentals and Applications
(Cambridge University Press, Cambridge, UK, 2008).
[159] K. Harris, G. Erickson, S. Sikkenga, W. Brentnall,
J. Aurrecoechea, and K. Kubarych, Development of
two rhenium-containing superalloys for single-crystal
blade and directionally solidiﬁed vane applications in
advanced turbine engines, J. Mater. Eng. Perform. 2, 481
(1993).
[160] T. M. Pollock, The growth and elevated temperature stability
of high refractory nickel-base single crystals, Mater. Sci. Eng.
B 32, 255 (1995) .
[161] S. Giese, A. Bezold, M. Pröbstle, A. Heckl, S. Neumeier,
and M. Göken, The importance of diffusivity and partitioning
behavior of solid solution strengthening elements for the high
temperature creep strength of Ni-base superalloys, Metall.
Mater. Trans. A 51, 6195 (2020).
[162] K. Cheng, C. Jo, D. Kim, T. Jin, and Z. Hu, Unexpected
precipitation of a Re-rich phase in single crystal superalloy
CMSX-4 during thermal exposure, J. Metall. 2012, 308568
(2012).
[163] R. Jayaram and M. Miller, Inﬂuence of phase composition
and microstructure on the high temperature creep properties
of a model single crystal nickel-base superalloy: An atom
probe/AEM study, Acta Metall. Mater. 43, 1979 (1995).
123603-16
