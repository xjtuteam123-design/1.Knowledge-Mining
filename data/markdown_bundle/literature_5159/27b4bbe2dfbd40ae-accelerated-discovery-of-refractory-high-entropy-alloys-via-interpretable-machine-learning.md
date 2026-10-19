# accelerated-discovery-of-refractory-high-entropy-alloys-via-interpretable-machine-learning

<!-- source: D:\总文献\accelerated-discovery-of-refractory-high-entropy-alloys-via-interpretable-machine-learning.pdf -->
<!-- file_sha256: 1736529dbb8cf9f44ad15dcc81235426fe8b8c9aafc2f860bf48a1435572f74a -->

## Page 1

Accelerated Discovery of Refractory High-Entropy Alloys via
Interpretable Machine Learning
Jian Cao, Chang Liu, Zian Chen, Haichao Li, Lina Xu,* Hongping Xiao, Shun Wang,* Xiao He,*
and Guoyong Fang*
Cite This: J. Phys. Chem. Lett. 2025, 16, 8806−8814
 Read Online
ACCESS
Metrics & More
 Article Recommendations *
sı Supporting Information
ABSTRACT: Due to the outstanding thermal stability, inherent
high melting points, and elevated temperature strengths, refractory
high-entropy alloys (RHEAs) have been widely used for extreme
environments in aerospace, nuclear energy, and advanced
propulsion systems. Herein, we present an integrated design and
simulation framework for RHEAs, combining machine learning
potentials, supervised regression models, and multiobjective
optimization algorithms. Utilizing a universal neuroevolution
potential version 1 (UNEP-v1), the framework significantly
enhances the accuracy of atomic-scale simulation while substantially
reducing computational cost. High-throughput molecular dynamics
simulations generate melting points and ultimate tensile strengths at
1000 K for various alloy compositions. Supervised regression models
enable a rapid performance prediction. Integrating Shapley Additive exPlanations, Partial Dependence Plots, Accumulated Local
Effects, and Individual Conditional Expectation analysis can provide a comprehensive interpretability toolkit. Validation of the
proposed method in the TiVCrZrMo alloy system demonstrates its efficacy in designing high-strength, high-temperature resistant
alloys. We not only develop a precise and interpretable predictive modeling paradigm but also establish procedural frameworks,
promoting the integration of atomic-scale simulations with data-driven approaches for RHEAs in extreme environments.
W
ith increasing performance demands for materials in
extreme environments such as aerospace, nuclear
energy, and propulsion systems, refractory high-entropy alloys
(RHEAs) stand out as promising candidates of high-temper-
ature applications.
1−3
Compared to conventional alloys,
RHEAs consist of refractory elements from the fourth to
sixth periods and IV to VI groups including Ti, V, Cr, Zr, Nb,
Mo, Hf, Ta, and W and supplemented by elements like Al, Co,
and Ni. This composition diversity not only provides a broader
space for component regulation but also grants thermal
stability and mechanical properties at high temperatures.
4
Despite their promising potential, vast compositional spaces
of RHEAs face significant challenges for modeling, screening,
and experimental validation. RHEAs have high melting points
that complicate their fabrication and performance evaluations.
These heavily rely on specific experimental conditions, making
the traditional trial-and-error optimization method inefficient
or infeasible.
5,6
Conventional theoretical methods, such as
density functional theory (DFT), phase diagrams (CAL-
PHAD), and classical molecular dynamics (MD) calculations,
can partially fill experimental gaps. But, they have high
computational costs and inadequate accuracy for predicting the
properties, such as thermal stability and high-temperature
strength.
7−11
Recently, machine learning (ML) has emerged as a
promising, efficient, and data-driven alternative for predicting
alloy properties. However, the application of ML to RHEAs is
significantly constrained by data scarcity. Machine learning
potentials (MLPs) are capable of significantly enhancing MD
simulation accuracy and maintaining physical consistency and
have attracted substantial interest in materials science.
12−15
In
this work, we utilize a neuroevolution potential (NEP), the
universal neuroevolution potential version 1 (UNEP-v1).
Compared with other machine learning potentials (such as
SNAP, MTP, and NequIP) and traditional empirical
potentials, like the embedded atom method (EAM), UNEP-
v1 demonstrates excellent consistency with first-principles
calculations and experimental results across key physical
properties, including lattice vibrations, elastic module, melting
points, and formation energies.
16−20
Received: May 27, 2025
Revised: July 29, 2025
Accepted: August 18, 2025
Published: August 20, 2025
Letterpubs.acs.org/JPCL
© 2025 American Chemical Society
8806
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
Downloaded via XI'AN JIAOTONG UNIV on November 29, 2025 at 12:10:44 (UTC).
See https://pubs.acs.org/sharingguidelines for options on how to legitimately share published articles.

## Page 2

Herein, we introduce the framework for the design and
simulation of RHEAs, integrating machine learning potential,
supervised regression model, and multiobjective genetic
algorithm (MOGA) to efficiently design RHEAs with high
strength and temperature resistance, shown in Figure 1. By
employing the UNEP-v1 potential, we achieve high-accuracy
atomic-scale simulations, significantly reducing computational
costs. High-throughput MD simulations can obtain critical
performance parameters such as melting points (T
m
) and
ultimate tensile strengths (UTS) at 1000 K. Supervised
learning regression models facilitate rapid performance
predictions. Furthermore, we integrate interpretability analyses
including Shapley Additive exPlanation (SHAP), Partial
Dependence Plot (PDP), Accumulated Local Effects (ALE),
and Individual Conditional Expectation (ICE) plots to form a
comprehensive explanatory framework.
21−25
Finally, alloy
compositions are optimized through multiobjective genetic
algorithms, demonstrating the validity and efficiency of our
approach within the TiVCrZrMo RHEA system. This
integrated atomic-scale simulation and data-driven learning
approach provides precise predictive modeling and robust
theoretical support for designing and discovering RHEAs
suitable for extreme service conditions.
For atomic-scale modeling of RHEAs, a body-centered cubic
(BCC) crystal structure was constructed employing periodic
boundary conditions using our High-Entropy Alloy Design and
Simulation (HEADS) program,
26
a Python-based framework
developed on the Atomic Simulation Environment (ASE)
program.
27
Leveraging its native Python architecture, HEADS
allows seamless integration with machine learning and
optimization workflows, facilitating data-driven alloy design.
The initial lattice parameters for each composition were set
with reference to the largest experimental lattice constant
among the constituent BCC elements, ensuring physical
realism during structural relaxation. To model compositionally
complex systems, HEADS represents multicomponent alloys as
ideal random solid solutions, assigning atomic species through
a calibrated stochastic algorithm that preserves the overall
homogeneity. The initial configurations were minimized via
the conjugate gradient (CG) method to eliminate high-energy
configurations. Subsequently, RHEA structures were thermally
equilibrated at 300 K under constant-temperature ensemble
conditions through MD simulations, ensuring the thermody-
namic stability. This two-step structural preparation ensures
the reasonableness of the configurations at the structural,
energetic, and thermodynamic levels, laying a robust
foundation for subsequent mechanical and thermodynamic
studies.
In this work, all structures of TiVCrZrMo RHEAs were
constructed based on the BCC lattice via HEADS, ensuring a
uniform distribution of elements, shown in Figure S1a of
Supporting Information. The UNEP-v1 applicability of four
TiVCrZrMo alloy compositions was validated,
28−30
as shown
in Figure S1b. To balance computational accuracy and cost, a
supercell size of approximately 8 × 8 × 8 nm was selected. As
listed in Table S1, this size provides sufficient atomic
representativeness while significantly reducing computational
cost.
To construct a comprehensive data set for T
m
and UTS,
high-throughput MD simulations were performed on a set of
461 TiVCrZrMo alloy compositions. These compositions were
generated by varying the elemental fractions in 10 atom %
intervals while ensuring the concentration of any single
element did not exceed 50 atom %, covering both four-
element and five-element alloy models. For each composition,
simulations were performed by using periodic boundary
Figure 1. General framework for design and simulation of RHEAs combining (a) molecular dynamics, (b) machine learning, and (c) multiobjective
genetic algorithm.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8807

## Page 3

conditions in the x, y, and z directions. Structures were initially
stabilized via a conjugate gradient method. T
m
was determined
via a multistage heating and annealing approach. In this
method, long-duration simulations were carried out at
incremental temperature intervals. The key was to identify
abrupt changes in the system’s energy, which served as
indicators for T
m
. Beginning with an initial temperature of 300
K, under an isobaric−isothermal ensemble (NPT) at 1 atm
pressure, the system temperature was incremented by 30 K
every 5 ps until reaching 4200 K.
31−33
The high-temperature
strength, represented by UTS, was simulated through uniaxial
tensile tests at 1000 K. After the system underwent sufficient
relaxation and attained thermal equilibrium under the NPT
ensemble at 1 atm pressure, the Nose-Hoover thermostat and
barostat ensured stable temperature and pressure regulation. A
uniaxial tensile test was applied along the x-direction, with zero
stress conditions in the y and z directions. The strain rate was
set to 1 × 1 × 10
10
s
−1
with a time step of 1 fs. Stress−strain
data were sampled every 0.1 ps, and the maximum stress was
recorded as the UTS value.
34−36
Figure S2 illustrates this
workflow using Ti
0.2
V
0.2
Zr
0.3
Mo
0.3
as an example, including
both the temperature-potential energy curve for T
m
extraction
and the stress−strain response for UTS determination.
Following the construction of the composition-property data
set, feature engineering was performed to accurately predict
the T
m
and UTS of RHEAs. Descriptors related to the crystal
structure and thermodynamic properties were extracted and
screened. Based on an extensive literature survey, 18
descriptors were initially established to characterize RHEAs
and listed in Table S2.
37−45
Despite the wealth of significant
features that provide a solid physical basis for predicting
RHEAs performance, the presence of many highly correlated
features can lead to multicollinearity. This phenomenon results
in disproportionately high weights being assigned to certain
features, passively diminishing the informative contributions of
others. Such feature redundancy not only undermines the
physical interpretability of the model but also increases the risk
of overfitting. Therefore, selecting a representative subset of
features through feature engineering is essential. This approach
enhances model interpretability and improves predictive
performance.
46,47
Considering that T
m
and UTS are different
types of performance indicators with significantly different
impact factors and internal mechanisms, we ensure that the
selected feature subsets are closely correlated with each target
attribute. The model predictions can approximate the actual
values within an acceptable error range; we conducted feature
engineering screening for T
m
and UTS, respectively. A three-
level feature engineering framework was established, consisting
of: (1) feature correlation filtering, (2) feature importance
ranking, and (3) performance-driven feature selection. This
hierarchical approach ensures the retention of physically
independent features while enabling nonlinear models to
capture complex interdependencies.
The Pearson correlation coefficient (PCC) was employed as
the metric to quantify feature interdependence.
48
A threshold
of |PCC| > 0.9 was adopted to identify strongly correlated
feature pairs. As shown in Figure S3, four distinct groups of
correlated features were highlighted: (“m”, “AN”), (“VEC”,
“G”), (“K”, “G”), (“Λ”, “δ”), and (“ρ”, “MP”). Following the
identification of highly colinear feature sets using the PCC
criterion, the random forest model was utilized to reveal the
mapping between features and target properties. The resulting
feature importance scores, derived from the model outputs,
guide a targeted feature selection strategy. As illustrated in
Figure S4, the features are ordered from left to right in
descending importance. For T
m
prediction, a combined
analysis of the PCC results and importance rankings led to
the removal of the following features (“N”, “G”, “AN”, “ρ”,
“dSmix”, “δ”). Consequently, 12 key variables were retained
from the initial set of 18. These retained features encompass
bonding energetics (e.g., “dHmix”), crystallographic parame-
ters (e.g., “Λ”, “a”), and thermodynamic stability indicators
(e.g., “ΔG”), thereby mitigating multicollinearity while
preserving critical physical interpretability in relation to T
m
mechanisms. In the prediction of UTS, based on the same
analytical framework, the feature “σK” with insufficient
importance was additionally excluded. Finally, 11 key variables
were screened out from the 18 features. Subsequent to the
correlation and feature importance analyses, this study further
employed recursive feature elimination (RFE) combined with
cross-validation (CV) to reduce dimensionality and enhance
the computational efficiency. As shown in Figure 2, a
comprehensive assessment of model performance guided the
final feature selection: nine features were retained for T
m
prediction, and eight features for UTS prediction. This
approach ensured an optimal balance between the model
accuracy and simplicity.
After feature engineering was completed, we aimed to
identify the most suitable regression model for predicting the
performance of RHEAs. Twelve representative supervised
learning algorithms were selected for model training and
evaluation, including Lasso Regression (Lasso), Ridge
Regression (Ridge), Support Vector Regression (SVR), K-
Nearest Neighbors Regression (KNR), Gaussian Process
Regression (GPR), Artificial Neural Network (ANN),
Decision Tree Regression (DTR), Random Forest Regression
(RFR), Extra Trees Regression (ETR), Gradient Boosting
Regression (GBR), AdaBoost Regression (ABR), and Extreme
Figure 2. RFE process with R
2
and RMSE as evaluation indexes.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8808

## Page 4

Gradient Boosting Regression (XGBR).
49−60
Multiple stat-
istical metrics�Coefficient of Determination (R
2
), Root Mean
Square Error (RMSE), and Mean Absolute Percentage Error
(MAPE)�were employed to evaluate model perform-
ance.
61−63
The data set was split into training and testing
sets in a 4:1 ratio, and model overfitting was mitigated using 10
× 10-fold cross-validation. Grid search was applied to fine-tune
the hyper-parameters for each machine learning model. The
optimized hyper-parameters for all models were summarized in
Table S3.
Table S4 presents the performance of the different
supervised learning models in predicting T
m
and UTS on
both training and testing data sets. The evaluation metrics
include R
2
, RMSE, and MAPE. For T
m
prediction, the GBR
model exhibited superior performance with a test R
2
of 0.98,
RMSE of 43.12, and MAPE of 1.68%, highlighting its strong
capability in capturing the complex relationships governing T
m
.
For UTS prediction, the XGBR model outperformed others,
achieving a test R
2
of 0.98, RMSE of 0.38, and MAPE of 8.26%,
fully validating the effectiveness of this model for UTS
prediction. Traditional linear models such as Lasso and Ridge
performed less favorably, with lower test R
2
values (e.g., Lasso
yielded an R
2
of 0.4916 for T
m
) and higher error metrics,
reflecting their limited ability to capture the underlying data
complexity. Nonlinear models, including SVR, KNR, and tree-
based approaches (DTR, RFR, and ETR), generally out-
performed linear models. Notably, ensemble tree-based
methods such as GBR and XGBR consistently achieved higher
R
2
values and lower errors, underscoring their advantages in
handling nonlinear and complex data structures.
Considering all performance metrics, the GBR model
demonstrated exceptional accuracy in predicting T
m
, while
the XGBR model yielded superior results for the UTS
prediction. Both models exhibited excellent fitting precision
and generalization capability. As illustrated in Figure 3, the
predicted values generated by these two models align closely
with the diagonal line for both the training and testing sets,
indicating strong agreement between the predicted and
experimentally observed values. Notably, the test R
2
values
for both tasks exceeded 0.95, confirming a high level of
correlation and predictive reliability.
Although machine learning models have achieved impressive
performances in predictive tasks, their “black-box” nature often
limits a deeper understanding of the underlying predictive
Figure 3. Regression parity plots of T
m
and UTS predictions based on the GBR and XGBR models. (a, b) Predicted vs actual T
m
values for the
training and testing sets using the GBR model. (c, d) Predicted vs actual UTS values for the training and testing sets using the XGBR model.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8809

## Page 5

mechanisms. To enhance the transparency and physical
interpretability of the models, we systematically analyzed the
T
m
prediction model and the UTS prediction model for
RHEAs using multiple interpretability methods. The analysis
incorporated SHAP, PDP, ICE, and ALE methods. These tools
offer both global and local perspectives on feature contribu-
tions, thereby aiding the physical interpretation of model
behavior.
For the prediction model of T
m
, the SHAP summary plot
(Figure 4a) and feature importance ranking plot (Figure 4b)
collectively indicate that Λ, m, and η are the three input
features with the highest contribution in the model, with their
mean absolute SHAP values being 0.254, 0.178, and 0.122,
respectively. Notably, Λ not only demonstrates the highest
contribution but also exhibits the widest distribution of SHAP
values across different samples, indicating that this feature
possesses excellent predictive capability and stability over
diverse chemical compositions. It serves as the most robust
stability indicator in the model, which aligns with existing
research conclusions that higher mixing entropy and moderate
atomic size differences enhance solid solution stability and
thermal stability.
64
While m and η rank below Λ in
contribution, they still show stable positive impacts across
multiple value ranges. To further illustrate the response
patterns and localized trends, Figure 4c presents the combined
PDP and ICE plots for these three features. The PDP curve for
Λ shows a marked upward trend near 3000 K, beyond which
its contribution to T
m
becomes increasingly significant. The
corresponding ICE curves exhibit consistent upward shifts
across multiple samples in this region, indicating that higher Λ
values generally promote T
m
enhancement. For η, the PDP
indicates a positive contribution to T
m
within the higher
resistivity regime. This may be attributed to the fact that high
resistivity often corresponds to stronger electron localization,
reduced metallicity, or increased structural complexity�
factors that are generally associated with higher melting points
in complex or ceramic materials.
65−67
Regarding m, both PDP
and ALE plots reveal a monotonic increasing trend, implying
that higher atomic mass positively influences T
m
, likely through
modulation of lattice vibrations and phonon behavior.
68
The
ALE plot (Figure 4d) further validates these trends from a
bias-corrected perspective. Λ shows a steady rise in the
medium-to-high range, reinforcing its dominant role in T
m
prediction. η exhibits its strongest local effect around 50 μΩ·
cm, while m contributes more moderately but maintains a
consistently increasing trend. The model demonstrates not
only statistical accuracy but also the ability to extract physically
meaningful patterns: Λ acts as a primary entropy-structure
descriptor, η reflects resistivity-related stability mechanisms,
and m serves as a secondary regulator influencing phonon
dynamics. This interpretive framework validates the model’s
internal logic and offers theoretical guidance for the composi-
tional design of high-T
m
materials.
Building on the interpretive analysis of the T
m
prediction
model, we further conducted a systematic interpretive analysis
of the UTS prediction model. The SHAP summary plot
(Figure S5a) and feature importance bar chart (Figure S5b)
reveal that Λ, K, η, and VEC are the four most influential
features in the model’s predictions. The SHAP value
distribution for Λ is markedly asymmetric: high Λ values are
predominantly associated with positive contributions, while
low Λ values are clustered in the −0.5 to 0 range, indicating a
Figure 4. Machine learning interpretability analysis for T
m
: (a) SHAP values, (b) feature importance, (c) PDP-ICE curves for selected features,
showing global and instance-level effects, (d) ALE plots illustrating bias-corrected local feature effects with 95% confidence intervals.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8810

## Page 6

negative impact. For K, the SHAP distribution is primarily
positive and directionally consistent, though a few samples
exhibit slight negative contributions. While η ranks highly in
importance, its SHAP values are symmetrically distributed
around zero. This suggests a nonlinear relationship between η
and UTS in the system, with η having no consistent directional
influence on the model output. In contrast, the VEC exhibits a
strongly negative SHAP distribution, indicating that high VEC
values generally suppress UTS predictions, reflecting a
unidirectional negative regulatory effect. In Figure S5c, the
PDP curve for Λ displays a sharp increase near 2700 K, and the
ICE curves converge in this region, indicating a consistent
strengthening effect across samples. This is consistent with
previous findings that high configurational entropy enhances
lattice homogeneity and strengthens mechanical properties.
64
For VEC, both PDP and ICE plots exhibit a monotonic
decreasing trend, with a particularly steep decline when VEC >
5.3, which suggests that high VEC may promote brittleness or
the formation of intermetallic phases, thereby degrading
mechanical performance.
69
The ALE analysis (Figure S5d)
further elucidates these effects in a bias-corrected context. The
influence of Λ continues to increase, especially in the 2800−
4000 range. K exhibits localized nonmonotonic behavior, with
a peak enhancement effect near 137, indicating a complex
modulus interaction mechanism. Meanwhile, the VEC shows a
consistently negative gradient. Figure S5 reveals several key
patterns captured by the UTS prediction model: Λ acts as a
primary entropy-structure descriptor playing a pivotal role in
the model, K functions as a threshold-activated stiffness
modulator, and VEC serves as a directional weakening feature.
Although η exhibits statistical relevance, its contribution trend
lacks directional clarity.
Through the interpretability analysis of the prediction
models for the two key performances (T
m
and UTS), we not
only clarify the core features that dominate the prediction
performance in each model but also reveal the nonlinear
relationship between the physical mechanism and the
numerical response. This multidimensional and multimethod
interpretability strategy provides a solid foundation for
understanding the internal mechanisms of high-throughput
machine learning models and enhancing their guiding value in
the design of new materials.
In the design of RHEAs, achieving a synergistic optimization
of high strength and thermal resistance remains a central
challenge. To address this, a multiobjective genetic algorithm
(MOGA) was employed to optimize compositions within the
TiVCrZrMo system. The algorithm was implemented using
the distributed evolutionary algorithms in the Python (DEAP)
library.
70
Each individual solution is represented as a vector x =
{x
1
, x
2
, x
3
, x
4
, x
5
}, where x
i
denotes the mass fraction of the i-th
element in the alloy. A normalization condition was enforced
to ensure that the sum of all element proportions equals 1. The
T
m
prediction model and UTS prediction model fitted by
supervised learning algorithms were integrated as objective
functions T(x) and U(x), respectively. The fitness function
F(x) in MOGA is defined as
x x xF ( ) (w T ( ), w U( )) T U = · ·
(1)
where x is the vector of alloy composition, T(x) and U(x)
represent T
m
and UTS, respectively, and the weights w
T
and
w
U
are used to adjust the relative importance of each objective
during the optimization process.
The GBR model was used to predict T
m
, and the XGBR
model was applied to predict UTS at 1000 K, both serving as
fitness functions for the MOGA framework. It was initialized
with a population size of 100 and evolved over 50 generations.
In each generation, new individuals were generated using a
crossover probability of 0.7 and a mutation probability of 0.3.
To balance local convergence and population diversity, a
preservation strategy was adopted in which parent and
offspring populations were merged, and the top 500 non-
dominated solutions were selected to advance the Pareto front.
Figure 5 presents the distribution of optimization results
under two different performance weight ratios: 1:1 and 1:2.
Purple dots denote all computed candidates generated during
the optimization process, while orange dots indicate the
Pareto-optimal front. The selection of the 1:1 and 1:2 weight
ratios was intended to explore the sensitivity of the solution
space to varying levels of prioritization between the thermal
resistance and mechanical strength. The 1:1 ratio serves as a
balanced baseline where both objectives are treated equally,
while the 1:2 ratio emphasizes UTS to examine how enhanced
weighting of the mechanical performance alters the solution
landscape. This design allows for a practical sensitivity analysis
of the multiobjective framework, revealing the trade-offs and
search dynamics under different prioritization schemes.
Importantly, the weight ratios used here are not fixed
parameters but were selected for demonstration purposes,
Figure 5. Pareto solutions of T
m
and UTS with weight ratios (a) 1:1 and (b) 1:2.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8811

## Page 7

highlighting the flexibility and tunability of the MOGA
framework. In real-world applications, these weights can be
readily adjusted based on specific design requirements or
operational goals.
A distinct shift in the Pareto front toward the high-UTS
region is observed when transitioning from balanced weighting
(1:1) to the UTS-focused setting (1:2), indicating that the
algorithm adapts its search direction according to the defined
preference. Under the 1:1 condition (Figure 5a), the Pareto
front is broadly distributed. Several solutions achieved T
m
values above 2700 K while maintaining UTS above 10 GPa,
illustrating the model’s efficacy in capturing compositions with
balanced high performance. When the weighting is skewed to
1:2 (Figure 5b), favoring UTS, the front shifts accordingly;
while T
m
slightly decreases in some candidates, the maximum
UTS reaches over 12 GPa.
In summary, we proposed a novel integrated design
framework for RHEAs, combining MLP-MD, feature engineer-
ing, supervised regression models, and MOGA. This frame-
work efficiently achieves full-process intelligent design, from
atomic-scale simulations and property predictions to compo-
sition optimization. Initially, accurate MD simulations of the
TiVCrZrMo RHEA were performed using the UNEP-v1
potentials, extracting critical performance parameters such as
T
m
and UTS from temperature-energy and stress−strain
curves, providing high-quality data for subsequent modeling.
An initial set of 18 descriptors was constructed based on
material compositions and structural features. Through
rigorous feature engineering, we selected subsets highly
correlated with targeted properties and employed 12 main-
stream supervised learning algorithms for modeling evaluation.
GBR showed superior performance in predicting T
m
, while
XGBR exhibited excellent accuracy and generalization
capabilities for predicting UTS at 1000 K. Additionally,
interpretability analyses using SHAP, ALE, and PDP clarified
the underlying physical mechanisms of key descriptors,
enhancing the physical transparency of the models. Leveraging
trained predictive models within an MOGA, we optimized
alloy compositions for simultaneous high T
m
and UTS, clearly
revealing compositional influences on coupled properties and
identifying multiple optimal compositions. The HEADS V2.0
framework thus significantly enhances the computational
efficiency and interpretability, offering practical and robust
solutions for high-throughput screening and intelligent
optimization of RHEAs.
■
ASSOCIATED CONTENT
*
sı
Supporting Information
The Supporting Information is available free of charge at
https://pubs.acs.org/doi/10.1021/acs.jpclett.5c01616.
RHEA models, NEP- and DFT-calculated energies;
Temperature-potential energy, stress−strain curves;
Heat map of Pearson correlation coefficient; T
m
and
UTS feature importance diagram; Machine learning
interpretability for UTS; Comparison of the predicted
melting points and CPU time; Eighteen features and
calculation formulas; Hyper-parameter selection and the
range for different models; Comparative regression
performance of 12 ML models (PDF)
■
AUTHOR INFORMATION
Corresponding Authors
Lina Xu − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China;
orcid.org/0000-0002-0455-3839; Email: xulina@
wzu.edu.cn
Shun Wang − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China;
Email: shunwang@wzu.edu.cn
Xiao He − Shanghai Engineering Research Center of Molecular
Therapeutics and New Drug Development, Shanghai
Frontiers Science Center of Molecule Intelligent Syntheses,
School of Chemistry and Molecular Engineering, East China
Normal University, Shanghai 200062, China; Chongqing
Key Laboratory of Precision Optics, Chongqing Institute of
East China Normal University, Chongqing 401120, China;
New York University-East China Normal University Center
for Computational Chemistry, New York University
Shanghai, Shanghai 200062, China;
 orcid.org/0000-
0002-4199-8175; Email: xiaohe@phy.ecnu.edu.cn
Guoyong Fang − College of Chemistry and Materials
Engineering, Wenzhou University, Wenzhou 325035, China;
orcid.org/0000-0001-6817-3790; Email: fanggy@
wzu.edu.cn
Authors
Jian Cao − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China
Chang Liu − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China
Zian Chen − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China
Haichao Li − College of Chemistry and Materials Engineering,
Wenzhou University, Wenzhou 325035, China
Hongping Xiao − College of Chemistry and Materials
Engineering, Wenzhou University, Wenzhou 325035, China
Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.jpclett.5c01616
Notes
The authors declare no competing financial interest.
■
ACKNOWLEDGMENTS
This work was supported by the National Natural Science
Foundation of China (52331009, 21703158, and 21873073),
the Basic Research Project of Wenzhou City (L20240001 and
L20240002). X. H. was supported by the National Natural
Science Foundation of China (92477103 and 22273023), the
National Key Research and Development Program of China
(2019YFA0905200), Natural Science Foundation of Shanghai
Municipality (23ZR1418200), Natural Science Foundation of
Chongqing Municipality (CSTB2023NSCQ-MSX0616),
Shanghai Frontiers Science Center of Molecule Intelligent
Syntheses, Shanghai Future Discipline Program (Quantum
Science and Technology), Shanghai Municipal Education
Commission’s ″Artificial Intelligence-Driven Research Para-
digm Reform and Discipline Advancement Program″, and the
Fundamental Research Funds for the Central Universities. We
gratefully acknowledge Supercomputer Center of East China
Normal University (ECNU Multifunctional Platform for
Innovation 001) for providing computation facilities.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8812

## Page 8

■
REFERENCES
(1) Pacchioni, G. Designing Ductile Refractory High-Entropy Alloys.
Nat. Rev. Mater. 2025, 10, 1.
(2) Abdullah, M. R.; Peng, Z. Review and Perspective on Additive
Manufacturing of Refractory High Entropy Alloys. Mater. Today Adv.
2024, 22, 100497.
(3) Eldabah, N. M.; Pratap, A.; Pandey, A.; Sardana, N.; Sidhu, S. S.;
Gepreel, M. A.-H. Design Approaches of High-Entropy Alloys Using
Artificial Intelligence: A Review. Adv. Eng. Mater. 2025, 27, 2402504.
(4) Yang, L.; Xiong, K.; Jin, C.; Dai, H.; Wu, H.; Zhang, S.; He, J.;
Guo, Y.; Mao, Y. Effects of Ti Content on Mechanical Properties of
VNbTaTi
x
. J. Mater. Sci. Technol. 2024, 171, 55−67.
(5) Zheng, W.; Lu ̈ , S.; Wu, S.; Chen, X.; Guo, W. Development of
MoNbVTa
x
Refractory High Entropy Alloy with High Strength at
Elevated Temperature. Mater. Sci. Eng., A 2022, 850, 143554.
(6) Sun, J.; Ning, S.; Zhao, J.; Zhou, Y.; Yun, X.; Huang, Z. High
Entropy Cemented Carbide Coupling High Entropy Ceramic and
High Entropy Alloy. Appl. Mater. Today 2025, 42, 102563.
(7) Melnick, A. B.; Soolshenko, V. K. Thermodynamic Design of
High-Entropy Refractory Alloys. J. Alloys Compd. 2017, 694, 223.
(8) Li, T.; Wang, S.; Fan, W.; Lu, Y.; Wang, T.; Li, T.; Liaw, P. K.
CALPHAD-Aided Design for Superior Thermal Stability and
Mechanical Behavior in a TiZrHfNb Refractory High-Entropy
Alloy. Acta Mater. 2023, 246, 118728.
(9) Chen, S.; Aitken, Z. H.; Pattamatta, S.; Wu, Z.; Yu, Z. G.;
Srolovitz, D. J.; Liaw, P. K.; Zhang, Y.-W. Short-Range Ordering
Alters the Dislocation Nucleation and Propagation in Refractory
High-Entropy Alloys. Mater. Today 2023, 65, 14.
(10) Sun, R.; Yin, H.; Liu, J.; Xie, S.; Zhang, C.; Zhang, R.; Wang, Y.;
Khan, D. F.; Qu, X. Screening the TiZrHfNbVMoTa Refractory
High-Entropy Alloys with Multi-Property Constraints. J. Alloys
Compd. 2025, 1020, 179284.
(11) Rao, Y.; Baruffi, C.; De Luca, A.; Leinenbach, C.; Curtin, W.A.
Theory-Guided Design of High-Strength, High-Melting Point,
Ductile, Low-Density, Single-Phase BCC High Entropy Alloys. Acta
Mater. 2022, 237, 118132.
(12) Rao, Z.; Tung, P.-Y.; Xie, R.; Wei, Y.; Zhang, H.; Ferrari, A.;
et al. Machine Learning-Enabled High-Entropy Alloy Discovery.
Science 2022, 378, 78.
(13) Liu, X.; Zhang, J.; Pei, Z. Machine Learning for High-Entropy
Alloys: Progress, Challenges and Opportunities. Prog. Mater. Sci.
2023, 131, 101018.
(14) Zhang, J.; Cai, C.; Kim, G.; Wang, Y.; Chen, W. Composition
Design of High-Entropy Alloys with Deep Sets Learning. npj Comput.
Mater. 2022, 8, 28.
(15) Qiao, L.; Zhu, J. Cuckoo Search-Artificial Neural Network
Aided the Composition Design in Al-Cr-Co-Fe-Ni High Entropy
Alloys. Appl. Surf. Sci. 2024, 669, 160539.
(16) Wu, L.; Li, T. A Machine Learning Interatomic Potential for
High Entropy Alloys. J. Mech. Phys. Solids 2024, 187, 105639.
(17) Zhao, J.; Zhao, S.; Luding, S. The Role of Particle Shape in
Computational Modelling of Granular Matter. Nat. Rev. Phys. 2023, 5,
505.
(18) Xia, J.; Zhang, Y.; Jiang, B. The Evolution of Machine Learning
Potentials for Molecules, Reactions and Materials. Chem. Soc. Rev.
2025, 54, 4790−4821.
(19) Hwang, S.; Jung, J.; Hong, C.; Jeong, W.; Kang, S.; Han, S.
Stability and Equilibrium Structures of Unknown Ternary Metal
Oxides Explored by Machine-Learned Potentials. J. Am. Chem. Soc.
2023, 145, 19378.
(20) Song, K.; Zhao, R.; Liu, J.; Wang, Y.; Lindgren, E.; Wang, Y.;
Chen, S.; Xu, K.; Liang, T.; Ying, P.; Xu, N.; Zhao, Z.; Shi, J.; Wang,
J.; Lyu, S.; Zeng, Z.; Liang, S.; Dong, H.; Sun, L.; Chen, Y.; Zhang, Z.;
Guo, W.; Qian, P.; Sun, J.; Fan, Z.; et al. General-Purpose Machine-
Learned Potential for 16 Elemental Metals and Their Alloys. Nat.
Commun. 2024, 15, 2287.
(21) Goldstein, A.; Kapelner, A.; Bleich, J.; Pitkin, E. Peeking Inside
the Black Box: Visualizing Statistical Learning with Plots of Individual
Conditional Expectation. J. Comput. Graph. Stat. 2015, 24, 44.
(22) Apley, D. W.; Zhu, J. Visualizing the Effects of Predictor
Variables in Black Box Supervised Learning Models. J. R. Stat. Soc. Ser.
B 2020, 82, 1059.
(23) Maulana Kusdhany, M. I.; Lyth, S. M. New Insights into
Hydrogen Uptake on Porous Carbon Materials via Explainable
Machine Learning. Carbon 2021, 179, 190.
(24) Rodríguez-Pérez, R.; Bajorath, J. Interpretation of Machine
Learning Models Using Shapley Values: Application to Compound
Potency and Multi-Target Activity Predictions. J. Comput.-Aided Mol.
Des. 2020, 34, 1013.
(25) Ren, J.; Xiao, L. Physics-Guided Neural Network for Fatigue
Life Prediction of FCC-Based Multi-Principal Element Alloys. Scr.
Mater. 2024, 253, 116307.
(26) Xu, L.; Cao, J.; Chen, Z.; Li, H.; Zhang, H.; Hu, W.; Sun, S.;
Fang, G. High-Entropy Alloy Design and Simulation Program,
HEADS V1.0; Wenzhou University, 2024.
(27) Hjorth Larsen, A.; Jorgen Mortensen, J.; Blomqvist, J.; Castelli,
I. E.; Christensen, R.; et al. The Atomic Simulation Environment�A
Python Library for Working with Atoms. J. Phys.: Condens. Matter
2017, 29, 273002.
(28) Kresse, G.; Furthmu ̈ ller, J. Efficient Iterative Schemes for Ab
Initio Total-Energy Calculations Using a Plane-Wave Basis Set. Phys.
Rev. B 1996, 54, 11169−11186.
(29) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient
Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865−3868.
(30) Becke, A. D. Density-Functional Thermochemistry. I. The
Effect of the Exchange-Only Gradient Correction. J. Chem. Phys.
1992, 96, 2155−2180.
(31) Wang, B.; Shan, X.; Zhao, H.; Bai, S.; Wang, B.; Tian, Y.; Tang,
Y. High-Temperature Deformation Behavior and Microstructural
Evolution of NbZrTiTa Refractory High Entropy Alloy. J. Alloys
Compd. 2023, 936, 168059.
(32) Chen, X.; Pan, Y.; Weng, S.; Hu, H.; Li, C.; Fu, T. Atomic
Insights of Grain Boundary Behaviors in TaWNbMo Refractory High
Entropy Alloys. J. Mater. Res. Technol. 2024, 30, 8999.
(33) Song, Z.; Luo, W.; Fan, X.; Zhu, Y. Atomic Fast Dynamic
Motion on the Cu Nanoparticle’s Surface before Melting: A
Molecular Dynamics Study. Appl. Surf. Sci. 2022, 606, 154901.
(34) Zhang, L.; Qian, K.; Huang, J.; Liu, M.; Shibuta, Y. Molecular
Dynamics Simulation and Machine Learning of Mechanical Response
in Non-Equiatomic FeCrNiCoMn High-Entropy Alloy. J. Mater. Res.
Technol. 2021, 13, 2043.
(35) Achmad, T. L.; Wibowo, P. A.; Sukma, F. T. S. Design of High
Entropy Superalloy FeNiCrCoAl Using Molecular Dynamics,
Computational Thermodynamics, and Machine Learning. J. Alloys
Compd. 2025, 1010, 177514.
(36) Nguyen, H.-G.; Le, T.-D.; Nguyen, H.-G.; Fang, T.-H.
Mechanical Properties of AlCoCrCuFeNi High-Entropy Alloys
Using Molecular Dynamics and Machine Learning. Mater. Sci. Eng.,
R 2024, 160, 100833.
(37) Yang, Z.; Gao, W. Applications of Machine Learning in Alloy
Catalysts: Rational Selection and Future Development of Descriptors.
Adv. Sci. 2022, 9, 12.
(38) Burakovsky, L.; Greeff, C. W.; Preston, D. L. Analytic Model of
the Shear Modulus at All Temperatures and Densities. Phys. Rev.
2003, 67, 67.
(39) Chen, L. Chemical Potential and Gibbs Free Energy. MRS Bull.
2019, 44, 520−523.
(40) Khabyah, Z.; Zaman, M.; Koam, A.; Ahmad, M.; Ullah, M.
Minimum Zagreb Eccentricity Indices of Two-Mode Network with
Applications in Boiling Point and Benzenoid Hydrocarbons.
Mathematics 2022, 10, 1393.
(41) Zhou, Z.; Zhou, Y.; He, Q.; Ding, Z.; Li, F.; Yang, Y. Machine
Learning Guided Appraisal and Exploration of Phase Design for High
Entropy Alloys. npj Comput. Mater. 2019, 5, 128.
(42) Zhang, Y.; Zhou, Y.; Lin, J.; Chen, G.; Liaw, P. K. Solid-
Solution Phase Formation Rules for Multicomponent Alloys. Adv.
Eng. Mater. 2008, 10, 534.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8813

## Page 9

(43) Zhang, Y.; Yang, X.; Liaw, P. Alloy Design and Properties
Optimization of High Entropy Alloys. JOM 2012, 64, 830.
(44) Dong, Y.; Lu, Y.; Jiang, L.; Wang, T.; Li, T. Effects of
Electronegativity on the Stability of Topologically Close Packed Phase
in High Entropy Alloys. Intermetallics 2014, 52, 105.
(45) Farache, D. E.; Verduzco, J. C.; McClure, Z. D.; Desai, S.;
Strachan, A. Active Learning and Molecular Dynamics Simulations to
Find High Melting Temperature Alloys. Comput. Mater. Sci. 2022,
209, 111386.
(46) Cai, J.; Luo, J.; Wang, S.; Yang, S. Feature Selection in Machine
Learning: A New Perspective. Neurocomputing 2018, 300, 70.
(47) Lu, W.; Xiao, R.; Yang, J.; Li, H.; Zhang, W. Data Mining-Aided
Materials Discovery and Optimization. J. Materiomics 2017, 3, 191.
(48) Zhang, H.; Fu, H.; He, X.; Wang, C.; Jiang, L.; Chen, L. Q.;
Xie, J. Dramatically Enhanced Combination of Ultimate Tensile
Strength and Electric Conductivity of Alloys via Machine Learning
Screening. Acta Mater. 2020, 200, 803.
(49) Krzywinski, M.; Altman, N. Multiple Linear Regression. Nat.
Methods 2015, 12, 1103.
(50) Dreiseitl, S.; Ohno-Machado, L. Logistic Regression and
Artificial Neural Network Classification Models: A Methodology
Review. J. Biomed. Inform. 2002, 35, 352.
(51) Bansal, M.; Goyal, A.; Choudhary, A. A Comparative Analysis
of K-Nearest Neighbor, Genetic, Support Vector Machine, Decision
Tree, and Long Short Term Memory Algorithms in Machine
Learning. Decis. Anal. 2022, 3, 1.
(52) Tancret, F.; Toda-Caraballo, I.; Menou, E.; Díaz-Del, A.
Designing High Entropy Alloys Employing Thermodynamics and
Gaussian Process Statistical Analysis. Mater. Des. 2017, 115, 486.
(53) Hornik, K. Approximation Capabilities of Multilayer Feedfor-
ward Networks. Neural Netw 1991, 4, 251.
(54) Bansal, M.; Malik, S.; Kumar, M.; Meena, N. Arduino-Based
Smart Walking Cane for Visually Impaired People. Proc. Int. Conf.
Inventive Syst. Control 2020, 21, 462.
(55) Breiman, L. Random Forests. Mach. Learn. 2001, 45, 5.
(56) Geurts, P.; Ernst, D.; Wehenkel, L. Extremely Randomized
Trees. Mach. Learn. 2006, 63, 3.
(57) Larestani, A.; Mousavi, S. P.; Hadavimoghaddam, F.; Hemmati-
Sarapardeh, A. Predicting Formation Damage of Oil Fields due to
Mineral Scaling during Water-Flooding Operations: Gradient
Boosting Decision Tree and Cascade-Forward Back-Propagation
Network. J. Pet. Sci. Eng. 2022, 208, 109315.
(58) Freund, Y.; Schapire, R. E. A Decision-Theoretic Generalization
of On-Line Learning and an Application to Boosting. J. Comput. Syst.
Sci. 1997, 55, 119.
(59) Chen, T.; Guestrin, C. XGBoost: A Scalable Tree Boosting
System. Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data
Min. 2016, 13, 785.
(60) Feng, K.; Hong, H.; Tang, K.; Wang, J. Decision Making with
Machine Learning and ROC Curves. arXiv 2019, DOI: 10.48550/
arXiv.1905.02810.
(61) Li, W.; Yang, T.; Liu, C.; Huang, Y.; Chen, C.; Pan, H.; Xie, G.;
Tai, H.; Jiang, Y.; Wu, Y.; Kang, Z.; Chen, L. Q.; Su, Y.; Hong, Z.
Optimizing Piezoelectric Nanocomposites by High-Throughput
Phase-Field Simulation and Machine Learning. Adv. Sci. 2022, 9,
220550.
(62) de Myttenaere, A.; Golden, B.; Le Grand, B.; Rossi, F. Mean
Absolute Percentage Error for Regression Models. Neurocomputing
2016, 192, 38.
(63) Zhang, S.; He, X.; Xia, X.; Xiao, P.; Wu, Q.; Zheng, F.; Lu, Q.
Machine-Learning-Enabled Framework in Engineering Plastics
Discovery: A Case Study of Designing Polyimides with Desired
Glass-Transition Temperature. ACS Appl. Mater. Interfaces 2023, 15,
37893−37902.
(64) Zhang, Y.; Zuo, T. T.; Tang, Z.; Gao, M. C.; Dahmen, K. A.;
Liaw, P. K.; Lu, Z. P. Microstructures and Properties of High-Entropy
Alloys. Prog. Mater. Sci. 2014, 61, 1.
(65) Benrazzouq, S.-E.; Ghanbaja, J.; Migot, S.; Milichko, V. A.;
Pierson, J.-F. Chemically-Driven Control of Electrical Resistivity of
High-Entropy Alloys. Appl. Mater. Today 2025, 44, 102726.
(66) Chen, H.; Xu, Y. J.; Liu, L. H.; Chen, Y.; Wróbel, J.; Cong, D.
Y.; Tian, F. Y.; Wang, Y. Lattice Distortion Tuning Resistivity of the
Invar Effect in High-Entropy Alloys. Phys. Rev. B 2025, 111, 094209.
(67) Kim, K.; Kaviany, M. Thermal Conductivity Switch: Optimal
Semiconductor/Metal Melting Transition. Phys. Rev. B 2016, 94,
155203.
(68) Toberer, E. S.; Zevalkink, A.; Snyder, G. J. Phonon Engineering
through Crystal Chemistry. J. Mater. Chem. 2011, 21, 15843−15852.
(69) George, E. P.; Raabe, D.; Ritchie, R. O. High-Entropy Alloys.
Nat. Rev. Mater. 2019, 4, 515−534.
(70) Deb, K.; Jain, H. An Evolutionary Many-Objective
Optimization Algorithm Using Reference-Point-Based Nondominated
Sorting Approach, Part I: Solving Problems with Box Constraints.
IEEE Trans. Evol. Comput. 2014, 18, 577−594.
The Journal of Physical Chemistry Letters pubs.acs.org/JPCL Letter
https://doi.org/10.1021/acs.jpclett.5c01616
J. Phys. Chem. Lett. 2025, 16, 8806−8814
8814
