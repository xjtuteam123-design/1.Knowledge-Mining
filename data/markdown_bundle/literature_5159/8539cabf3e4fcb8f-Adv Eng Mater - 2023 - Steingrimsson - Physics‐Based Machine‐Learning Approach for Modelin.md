# Adv Eng Mater - 2023 - Steingrimsson - Physics‐Based Machine‐Learning Approach for Modeling the Temperature‐Dependent Yield

<!-- source: D:\总文献\Adv Eng Mater - 2023 - Steingrimsson - Physics‐Based Machine‐Learning Approach for Modeling the Temperature‐Dependent Yield.pdf -->
<!-- file_sha256: e9d37c21e95fe6d6c098ab2c34dc7dc8889d320ecfec3185d5b2b99c2867d5d3 -->

## Page 1

Physics-Based Machine-Learning Approach for Modeling
the Temperature-Dependent Yield Strength of Superalloys
Baldur Steingrimsson,* Xuesong Fan, Benjamin Adam, and Peter K. Liaw
1. Introduction
The conventional approach to alloy design assumes selecting a
main component based on the primary property needed in
the alloy, with one or more additions to provide secondary prop-
erties. For over six decades, superalloys have provided reliable
and cost-effective means for achieving high operating tempera-
tures and stress conditions, ﬁrst in aircraft and later in industrial
gas turbines.[1] The zenith of superalloy development was in the
1960s, as columnar grain alloys and single
crystals were then made feasible, and many
polycrystalline alloys matured into com-
mercial reality. [1] Since then, advances in
powder metallurgy processing, single-
crystal and directionally solidi ﬁed alloy
designs, and oxide-dispersion strengthen-
ing have ensued, along with advances in
additive manufacturing and integrated
computational materials engineering.
In the case of nickel-based superalloys,
nickel is selected as the main component
because of its high melting point.
Nevertheless, chromium is added to pre-
vent corrosion, and titanium and alumi-
num are included to increase strength.
The Ni-based superalloys can accommo-
date γ, γ 0, γ 00, carbides, or topologically
closed-packaged (TCP) phases, as explained
in the Supporting Information. Co-based
superalloys can similarly contain γ, γ 0, car-
bide, or TCP phases. The Co-based super-
alloys are usually strengthened by a combination of carbides and
solid-solution hardening. [1] The use of steels for applications
necessitating superalloys may also be of interest, as further
explained in the Supporting Information, because certain steels
have exhibited creep and oxidation resistance close to that of
the Ni-based superalloys, while being much less expensive to
manufacture.
Machine learning (ML) and data analytics, coupled with
physics-based modeling, can assist with the effective search of
the compositional space of superalloys and with the optimization
of thermomechanical postprocesses. Figure 1 outlines the mul-
tiple sources that affect the mechanical properties of superalloys.
As opposed to speci ﬁcally applying ML, narrowly de ﬁned in
terms of multivariate regression, single-layer or multi-layer neu-
ral networks, Bayesian graphical models, random forest models,
support vector machines (SVMs), or decision trees, to the iden-
tiﬁcation of superalloy compositions of interest, we reformulate
the task in the broader context of engineering optimization. [2–4]
We recommend selecting an optimization technique suitable for
the application at hand and the data available, but we certainly
include ML in the consideration. Our rationale is based in part
on observations from Agrawal et al. [5] According to Table 2 and
Figure 5 of ref. [5], there is at most a difference of a few percen-
tages between the techniques applied to model the fatigue
strengths of stainless steels. Speci ﬁcally, in terms of the coef ﬁ-
cient of correlation, R2, which represents the variance explained
by the model, a decision table method produced the R2 of 0.901,
an instance-based K-nearest neighbor (IBK) method an R2 of
B. Steingrimsson
Imagars LLC
P.O. Box 261, Wilsonville, OR 97070, USA
E-mail: baldur@imagars.com
B. Steingrimsson
Department of Manufacturing, Mechanical and Engineering Technology
Oregon Institute of Technology
Wilsonville, OR 97070, USA
B. Steingrimsson, B. Adam
School of Mechanical, Industrial and Manufacturing Engineering
Oregon State University
Corvallis, OR 97331, USA
X. Fan, P. K. Liaw
Department of Materials Science and Engineering
The University of Tennessee
Knoxville, TN 37996, USA
The ORCID identi ﬁcation number(s) for the author(s) of this article
can be found under https://doi.org/10.1002/adem.202201903.
DOI: 10.1002/adem.202201903
In the pursuit of developing high-temperature alloys with improved properties for
meeting the performance requirements of next-generation energy and aerospace
demands, integrated computational materials engineering has played a crucial
role. Herein, a machine learning approach is presented, capable of predicting the
temperature-dependent yield strengths of superalloys utilizing a bilinear log
model. Importantly, the model introduces the parameter break temperature,
Tbreak, which serves as an upper boundary for operating conditions, ensuring
acceptable mechanical performance. In contrast to conventional black-box
approaches, our model is based on the underlying fundamental physics built
directly into the model. A technique of global optimization, one allowing the
concurrent optimization of model parameters over the low- and high-temperature
regimes, is presented. The results presented extend previous work on high-
entropy alloys (HEAs) and offer further support for the bilinear log model and its
applicability for modeling the temperature-dependent strength behavior of
superalloys as well as HEAs.
RESEARCH ARTICLE
www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (1 of 9) © 2023 Wiley-VCH GmbH

## Page 2

0.920, an instance-based K-nearest neighbor method with
entropy-based distance function (Kstar) an R2 of 0.941, a SVM
method an R2 of 0.959, a linear regression method with nonlin-
ear transformation of certain input variables (LRTrans) method
an R2 of 0.959, a robust ﬁt regression (RobustFitLSR) method an
R2 of 0.961, a linear regression method an R2 of 0.963, a pace
regression method an R2 of 0.963, an arti ﬁcial neural network
method an R2 of 0.972, a reduced error pruning tree
(REPTree) method an R2 of 0.972, a M5 model tree method
(a conventional decision tree method with the option of
linear regression functions at the nodes) an R2 of 0.978 and a
multivariate polynomial regression method an R2 of 0.980,
according to Table 2. [5] Here, fatigue dataset for steel from the
National Institute of Material Science was analyzed. The fatigue
dataset consisted of 437 instances/rows, 25 features/
columns (composition and processing parameters), together
with a single target property (fatigue strength). The 437 instances
comprised of 371 instances of carbon and low-alloy steels, 48
instances of carburizing steels, and 18 instances of spring steels.
For further background information on the application of ML to
the modeling of mechanical properties of alloys and on the moti-
vation for coupling with physics-based modeling approaches,
refer to refs. [2 –4].
This paper introduces a bilinear log model for predicting the
yield strength (YS) of superalloys across temperatures. It
consists of separate exponentials for a low-temperature and a
high-temperature regime, with a break temperature, Tbreak,i n
between. The underlying physics is accounted for, e.g., through
diffusion processes required to initiate phase transformation
processes in the high-temperature regime. [6] Moreover, we show
how piecewise linear regression can be employed to extend the
model beyond two exponentials and yield accurate ﬁt, in the case
of a nonconvex objective function caused by hump(s) in the
data.[3] Previous models for the temperature dependence of
YS only accounted for a single exponential. [7,8] However,
the break temperature is crucial for the optimization of the
high-temperature properties of alloys. For reliable operation,
the temperature of turbine blades or disks (rotors) made from
refractory superalloys may need to stay below Tbreak. Once the
temperature increases beyond Tbreak, the superalloys can lose
strengths rapidly due to rapid diffusion, facilitating dislocation
motion and dissolution of strengthening phases. [6] We consider
Tbreak a crucial parameter in the design of superalloys with
tailored high-temperature properties, one warranting the inclu-
sion in the superalloy speci ﬁcations. Hence, it is of paramount
importance to be able to estimate Tbreak accurately, e.g., using the
global-optimization approach presented in prior works by
Steingrimsson et al. [3]
In terms of impacts, this paper addresses a physics-based, i.e.,
not a black box, approach to ML and data analytics. Preference to
such approaches, especially for applications involving materials
science, may primarily stem from the fact that they involve fewer
parameters than the black-box models and hence require less
input data. With experiments often being time-consuming and
expensive, in the case of such applications, high-quality input
data tend to be a scarce resource. Moreover, the physics-based
modeling approaches help establish causal links between
output observations and the behavior of the underlying material
system.
2. Results and Discussion
Figure 1 summarizes the multiple sources that impact the
mechanical properties of superalloys. It bears noting that
improvements in the YS may come at the expense of other prop-
erties. Hence, we have suggested a framework for joint
optimization.[2–4] For instance, there typically is a trade-off
between the ductility and the strength of the superalloys.
Figure 1 presents an inverse design process, where components
of the design are explicitly calculated from the target perfor-
mance metrics provided.
For 40 superalloy compositions, Table 1 compares the perfor-
mance of the bilinear log model to that of a model based on a
single exponential. When averaged over these 40 compositions,
the bilinear log model results in a mean squared error (MSE) of
0.00175 in the logarithmic domain, compared to the MSE of
0.0525 for the model based on a single exponential. This differ-
ence is exacerbated in the linear domain, where the bilinear log
model yields the MSE of only 4,151 MPa 2, compared to the MSE
of 25 836 MPa 2 for the model based on a single exponential.
Analogous to Wu et al., [7] we employ a model with a single expo-
nential for the overall YS, σy(T ), of the form
σyðTÞ¼ σaexp /C0 T
C
/C18/C19
þ σb (1)
where σa, C, and σb represent ﬁtting coef ﬁcients.
In an effort to identify superalloy compositions exhibiting the
ability to retain strengths at high temperatures, we present
Figure 2 and 3. The strengths of most metals tend to decrease
with temperature, as dislocation motion becomes thermally acti-
vated.[9] In the case of high-temperature applications, one may
look to derive a model of the form
YS ¼ hðcomposition, TÞ (2)
for the prediction of the YS of the superalloys across
temperatures.
The strength vs temperature data presented in Figure 2–4 does
not suggest a linear relationship but rather an exponential one.
Therefore, a multivariate linear regression may not constitute a
preferred approach. Figure 2 –4 exhibit a high-temperature and a
Figure 1. High-level depiction of the role of ML and optimization inferring
the features giving rise to the superalloy properties observed, including the
yield strength. [2,4]
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (2 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

Table 1. Quantiﬁcation of the ability of superalloy compositions to retain yield strengths at high temperatures. Tbreak refers to the breaking point between
bilinear log models, de ﬁned in Equation (10).
No. Alloy Category Solvus
temperature [°C]
Tbreak [°C] MSE: two exponentials MSE: tingle exponential
Log Linear Log Linear
1 Waspaloy Ni-base (precipit. hard.) 1330 755.2 6.367e-04 5118 0.0070 44 260
2 Udimet D979 Fe-Ni-base (precipit. hard.) 1390 717.7 0.005391 7678 0.0138 36 204
3 Udimet 720 Ni-base (precipit. hard.) 1371 Not enough high-temp data pts. 0.00056 243 720
4 Udimet 520 Ni-base (precipit. hard.) 1371 728.6 5.663e-05 2221 0.0162 50 701
5 Udimet 500 Ni-base (precipit. hard.) 1360 748.9 7.901e-05 1331 0.0181 48 108
6 Astroloy Ni-base (precipit. hard.) 1399 760.6 5.759e-04 6643 0.0091 80 097
7 Incoloy 825 Fe-Ni-base (solid sol.) 1370 727.6 3.196e-07 14 0.0367 2,198
8 Inconel 807 Fe-Ni-base (solid sol.) 1275 774.1 1.069e-04 1358 0.00136 3,442
9 Inconel 802 Fe-Ni-base (solid sol.) 1372 760.0 0.00252 1049 0.00495 2,248
10 Inconel 801 Fe-Ni-base (solid sol.) 1372 Not enough high-temp data pts. 0.00009 10 504
11 Inconel 800 Fe-Ni-base (solid sol.) 1357 675.8 4.131e-04 637 0.00163 2,364
12 Incoloy 800 Fe-Ni-base (solid sol.) 1350 Not enough high-temp data pts. 0.00623 699.8
13 Inconel X750 Ni-base (precipit. hard.) 1393 Not enough high-temp data pts. 0.00000 90 438
14 Inconel 718 Ni-base (precipit. hard.) 1260 717.3 0.01707 7622 0.00819 58 230
15 Inconel 625 Ni-base (solid sol.) 1290 766.8 2.911e-04 598 0.01615 14 501
16 Inconel 617 (sheet) Ni-base (solid sol.) 1332 893.4 0.00201 2790 0.00235 4,010
17 Inconel 601 Ni-base (solid sol.) 1360 735.0 7.862e-04 99 0.18572 7,360
18 Inconel 600 Ni-base (solid sol.) 1354 760.1 1.639e-04 10 0.22850 4,314
19 Ti 6Al4V α and β phases 1604 501.6 1.793e-04 134 0.01299 12 367
20 Haynes 556 Fe-Ni-base (solid sol.) 1371 775.6 1.039e-04 1390 0.00107 3,771
21 Haynes 230 (a) Ni-base (solid sol.) 1288 798.4 0.002124 1591 0.00376 6,176
22 Haynes 230 (b) Ni-base (solid sol.) 1288 829.3 0.002035 260 0.12314 7,681
23 Haynes 188 Co-base (solid sol.) 1315 932.8 0.001307 4807 0.00138 6,002
24 Hastelloy C22 Ni-base (solid sol.) 1357 Not enough high-temp data pts. 0.00020 4,647
25 Hastelloy S Ni-base (solid sol.) 1335 765.2 8.509e-05 454 0.00859 6,211
26 Hastelloy X Ni-base (solid sol.) 1260 837.6 0.002745 212 0.13881 5,298
27 Hastelloy X (10 μm) Ni-base (solid sol.) 1260 744.4 0.003165 137 0.24225 11 620
28 Rene 95 Ni-base (precipit. hard.) 1343 627.6 0.000001 80 757 0.00135 217 771
29 Rene 41 Ni-base (precipit. hard.) 1316 748.1 0.000009 663 0.03624 79 716
30 Pure Nickel Ni-base 1455 Not enough high-temp data pts. 0.00892 64
31 Nickel 201 Ni-base (solid sol.) 1435 Not enough high-temp data pts. 0.00246 132
32 Nickel 200 Ni-base (solid sol.) 1435 349.4 0.001337 22 0.01677 258
33 Nimonic 263 Ni-base (precipit. hard.) 1300 758.8 0.000262 82 0.08506 15 601
34 Nimonic 90 Ni-base (precipit. hard.) 1310 724.8 7.875e-05 74 0.08111 29 514
35 Nimonic 80a Ni-base (precipit. hard.) 1320 754.3 0.000351 156 0.05091 19 933
36 Nimonic 75 Fe-Ni-base (solid sol.) 1340 731.2 0.001561 92 0.06840 1,391
37 Nimonic PE16 Fe-Ni-base (precipit. hard.) 1310 731.6 2.512e-05 7 0.1399 16 557
38 Nimonic PE13 Fe-Ni-base (solid sol.) 1310 Not enough high-temp data pts. 0.00131 6,424
39 N155 Fe-Ni-base (solid sol.) 1288 847.5 0.008876 687 0.0670 2,998
40 L605 Co-base (solid sol.) 1330 Not enough high-temp data pts. 0.00782 3,666
Average (No. 1-2, 4-9, 11, 14-23, 25-30, 32-37, and 39): 0.00175 4151 0.0525 25 836
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (3 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

low-temperature regime. Automated black-box model ML suites,
such as the Tree-Based Pipeline Optimization Tool, [10] may be
inappropriate due to their limited ability to provide much-needed
insights into the underlying physics. Instead, one is motivated to
make the most of the limited data available by incorporating
important a priori information about the underlying physics into
the model structure, for the purpose of deriving such insights.
Speciﬁcs on the algorithmic aspects of the incorporation of a pri-
ori information into the bilinear log model are presented in
Section 4. The results in Figure 2 –4 were derived using the
global-optimization approach, applied separately to individual
alloys, for the purpose of obtaining a tighter ﬁt and more accurate
estimation of Tbreak than for separate optimization over the low-
and high-temperature regimes.
In regards to the underlying physics, Ni-based superalloys
containing γ 0 phases tend to be particularly resistant to temper-
ature with reference to their in-service mechanical properties. [9]
Strengthening generally occurs through both alloying elements
acting as solutes in the face-centered-cubic (FCC) austenitic
matrix phase and through the solute-precipitation strengthening,
such as the γ 0 phase. This phase is responsible for the YS of
many nickel-based superalloys being relatively insensitive to tem-
perature. The effect arises from dislocation locking on secondary
{100} slip planes caused by cross-slipping of primary dislocations
on {111} slip planes in the γ 0 phases during plastic deformation.
Ordinary dislocation slip occurs on the {111} <110> plane, both
for the γ and the γ 0 phases. There is, however, a tendency for
dislocations in the γ 0 phase to cross-slip onto secondary {100}
Figure 2. Quantiﬁcation of modeling accuracy of the bilinear log model for
the composition No. 17 from Table 1 (Inconel 601) and comparison to
that of a model with a single exponential, a) in the logarithmic domain
and b) in the linear domain.
Figure 3. Quantiﬁcation of modeling accuracy of the bilinear log model for
the composition No. 18 from Table 1 (Inconel 600) and comparison to
that of a model with a single exponential, a) in the logarithmic domain
and b) in the linear domain.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (4 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

planes, where they can have a lower anti-phase domain boundary
energy (APB). These secondary slip planes are thermally acti-
vated, similar to the APB energy, which is crucial for maximizing
the strengthening provided by the presence of γ 0 phases. At the
same time, strengthening contributions from both the γ 0 phase
and the APB energy decrease with an increase in temperature.
This correlates with ﬁndings in the present results, such as
the signature peak in the ﬂow stress, seen for γ 0-strengthened
superalloys.[11,12]
When higher strength is required at lower temperatures, e.g.,
for turbine discs, precipitation strengthening in Ni-based super-
alloys can still be utilized, either by employing other phases, such
as the γ 00 phase in Nb-bearing alloys or multimodal size distri-
bution of the γ 0 phase. The γ 00 phase occurs in Ni-based super-
alloys, such as Inconel 718, which have signi ﬁcant addition of
Niobium or Vanadium. The stoichiometry of the γ 00 phase is
Ni3Nb or Ni 3V and consists of a body-centered-tetragonal lattice
with an ordered arrangement of Nickel and Niobium atoms.
Strengthening occurs primarily through coherency-hardening
and order-hardening mechanisms. [9]
The governing deformation mechanism is ordinary slip on the
{111}<110> plane, both for the γ and the γ 0 phases. There is,
however, a tendency for dislocations in the γ 0 phase to cross-slip
onto {100} planes, where they can attain a lower APB energy.
Situations can arise where an extended dislocation is partly on
a close-packed plane and partly on a cube plane. Such a disloca-
tion can become locked and result in an increase in strength,
which can help retain strength in the low-temperature regime.
In the elevated-temperature regime, thermally activated micro-
structural phenomena tend to be suf ﬁciently violent to allow dis-
locations to overcome obstacles. [9]
Figure 5 offers a comparison of temperature-dependent YSs
across superalloy compositions. The three primary categories
of superalloys are commonly identi ﬁed in the literature as
Figure 4. Quantiﬁcation of modeling accuracy of the bilinear log model for
the composition No. 27 from Table 1 (Hastelloy X 10 μm), and compari-
son to that of a model with a single exponential, a) in the logarithmic
domain and b) in the linear domain.
Figure 5. Comparison of temperature-dependent yield-strength properties
of Fe-Ni-, Ni-, and Co-based superalloys, a) separated for alloys classes
and b) separated by each respective alloy; reproduced from ref. [1]. In
a), SS refers to solid-solution strengthening, but PPT to precipitation
strengthening.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (5 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

1) Fe-Ni-, 2) Ni-, and 3) Co-based superalloys. [1] Fe–Ni-based
superalloys, such as the popular Inconel 718, came into existence
as an extension of the stainless-steel technology and are generally
heat treated for both their wrought and cast conventions. Co- and
Ni-based superalloys may be heat treated or not, wrought or cast,
depending on the application and composition involved. Figure 5
illustrates the following: 1) The precipitation-strengthened
superalloys seem to result in higher YS than the solid-
solution-strengthened ones in the case of both the Ni-based
and the Fe-Ni-based superalloys. 2) The Ni-based superalloys
tend to produce higher YS than the Fe-Ni-based superalloys in
the case of both precipitation and solid-solution strengthening.
The superior YS of the precipitation-strengthened superalloys
is illustrated in Figure 5, reproduced from strength-temperature
diagrams widely utilized in the literature. [1] Superalloys can be
strengthened not only through solid-solution strengthening
but also through the presence of strengthening phases, such
as precipitates. Co-based superalloys can exhibit a tendency
toward the transformation of the FCC matrix phase into stable
lower temperature phases. In the case of Ni- and Fe-Ni-based
superalloys, the FCC matrices can exhibit favorable characteris-
tics for the precipitation of uniquely effective strengthening
phases.[1]
When looking at the superalloy compositions from the
Supporting Information, the following observations stand out:
1) Many of the superalloys, such as Astroloy, Hastelloy S,
Hastelloy X, and Waspaloy, Nimonic PE16, Rene 41, Nimonic
80a, Nimonic 90, Rene 95, Nickel 200, Nimonic 263, Udimet
520, Udimet 500, Haynes 556, Inconel 600, Inconel 601,
Incoloy 825, and Inconel 807, present fairly straight forward
cases, where the bilinear log model offers much better perfor-
mance than the model based on a single exponent. 2) For some
of the superalloys, such as Nimonic PE 13, Nickel 201, Udimet
720, Inconel 801, Inconel X750, and Hastelloy C22, accurate
modeling seems to be precluded by a lack of data points in
the high-temperature regime. 3) Some of the superalloys, such
as Udimet D979, Inconel 802, Inconel 800, Inconel 625, Inconel
617 (sheet), Haynes 188, and Nimonic 75, seem to exhibit behav-
ior featuring a ﬂat intermediate regime. 4) At least one of the
superalloys, such as Inconel 718, may exhibit a trilinear log
behavior. 5) Both con ﬁgurations of the Haynes 230 superalloy,
as well as the L605 superalloy, seem to exhibit an anomalous
yield-strength phenomenon, i.e., a hump between the
low- and high-temperature regimes. [3]
The good match of the bilinear log model with the temperature-
dependent strength data for Astroloy, Hastelloy S, Hastelloy X,
Waspaloy, Nimonic PE16, Rene 41, Nimonic 80a, Nimonic 90,
Rene 95, Nickel 200, Nimonic 263, Udimet 520, Udimet 500,
Haynes 556, Inconel 600, Inconel 601, Incoloy 825, and
Inconel 807 is consistent with the observations from Figure
2–3, and previous ﬁndings by the authors.[3,13] The models utilized
here are presented in Section 4.
The experimental data for the superalloys Nimonic PE13,
Nickel 201, Udimet 720, Inconel 801, Inconel X750, and
Hastelloy C22 did not allow for the estimation of an exponent
for the high-temperature regime. In order to estimate the
high-temperature exponent, at least two data points above
Tbreak are necessary.
A ﬂat intermediate regime, such as observed for Udimet
D979, Inconel 802, Inconel 800, Inconel 625, Inconel 617 (sheet),
Haynes 188, and Nimonic 75, has also been reported for
medium- and high-entropy alloys (MEAs and HEAs) in prior
work by Steingrimsson et al. [13] These cases may necessitate
the application of the tri-linear log model from
Equation (13)–(16). Possible explanations for a tri-linear behavior
for intrinsic temperature-dependent YSs in body-centered cubic
(BCC) metals and substitutional solid solutions have been dis-
cussed by some researchers: [14] 1) Plastic deformation of the
BCC metals and alloys is believed to be mediated by the thermally
activated formation and movement of kink pairs at low temper-
atures. 2) Above a certain “critical temperature ”,a ﬂat-strength
plateau is achieved, where the strength becomes virtually temper-
ature or strain-rate independent. 3) When the test temperature
exceeds approx. 40% of the melting temperature, diffusional pro-
cesses can lead to a rapid decrease of yield stress, and the YS
becomes strain-rate dependent again.
In the presently utilized case of the tri-linear log model, two
break temperatures, Tbreak1 and Tbreak2, are considered. [3]
However, the explanations outlined previously only reference
one such temperature and refer to it as the “critical temperature”
or “knee temperature ”, which apparently corresponds to Tbreak1
in our model.
The ﬂat intermediate plateau seems less prevalent in alloys
with FCC-crystal structures. The FCC-crystal structure possesses
12 slip planes with 4 closest packed {111} planes and 3 closest
packed <110> directions per plane. The hexagonal close packed
(HCP) crystal structure, on the other hand, only has three active
slip systems at room temperature. The BCC crystal structure
does not have truly closest packed planes, but one closest-packed
direction, the <111> direction; therefore, dislocation mobility is
critically dependent on thermal activation in BCC metals.
Extensive research has been conducted on the subject of slip sys-
tems, Peierls barriers, dislocation mechanisms, ﬂow stress, and
temperature-dependent stress behavior in BCC vs FCC metals;
see, for example, works by Seeger et al. [15,16] In the speci ﬁc case
of Inconel 718, the need for a tri-linear log model may be hard to
ascertain due to the possible uncertainty in the experimentally
measured data points.
The hump between the low- and high-temperature regimes,
i.e., the anomalous yield-strength phenomenon, is characteristic
of the γ 0-o r γ 00-strengthened superalloys. [3,12] The phenomenon
manifests itself as a positive temperature dependence of the total
YS and is found in superalloys strengthened by L1 2-ordered
intermetallics.[17] The increasing strength of the γ 0 phase with
temperature is explained by a thermally-activated cross slip of
dislocations from {111} planes to {100} planes, where locking
of partial dislocations occurs. [18,19] The in ﬂuence of the γ 0
strengthening increases with increasing γ 0 volume fraction
and increasing temperature below the peak YS, as seen in
Figure S5 from the Supporting Information. [11,20] Additional fac-
tors involve the γ 0 size, γ 0 solute content, γ–γ 0 mismatch, and
both the stacking fault energy as well as the APB energy. The
latter two factors are the major contributions to hardening for
both the matrix phase as well as the precipitate phase and are
both strongly affected by alloying additions. [21]
Supplementary datasets for the factors mentioned above were
collected for all the alloys presented in Table S1 from the
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (6 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

Supporting Information, where possible, for the solution-
annealed and peak-aged condition, maximizing the precipita-
tion-strengthening effect. In reviewing the data on the strength-
ening-precipitate type, volume fraction, and average size, as well
as the lattice mis ﬁt for all alloys, the signi ﬁcant scatter becomes
apparent, resulting from the lack of data, lack in consistency in
the methodology and processing. While this feature provides
challenges to data extraction and comparability, it also shows
the complex precipitation and growth as a function of prior proc-
essing and heat treatment, as well as the need for incorporating
physics-based prediction models that can account for multi-
modal-precipitate distributions. [22,23]
For example, this trend is illustrated by the alloy CMSX-4, a
γ 0-strengthened, single-crystal, nickel-based superalloy, where
three exponentials are needed for accurate modeling in case
of heat treatment A, but four exponentials in case of heat treat-
ment B, according to the Figure S4 from the Supporting
Information.[3,17]
3. Conclusions
In conclusion, we proposed a bilinear log model for predicting
the YS of superalloys across temperatures and studied its effec-
tiveness for 38 distinct compositions or 40 total con ﬁgurations.
We considered the break temperature, Tbreak, an important
parameter for the design of superalloy materials with favorable
properties at elevated temperatures, one warranting the inclusion
in the superalloy alloy speci ﬁcations. For reliable operations, and
not accounting for coatings, the operating temperatures for the
corresponding superalloys may need to stay below Tbreak. Earlier
models for the temperature dependence of the YS only accounted
for a single exponential and thus did not feature a break temper-
ature. Across these 40 con ﬁgurations, we demonstrated a much
superior performance of the bilinear log model compared to the
one comprising a single exponential. In the logarithmic domain,
the bilinear log model resulted in MSE of 0.00175, compared to
the MSE of 0.0525 for the single-exponent model. But in the lin-
ear domain, the bilinear log model produced MSE of 4151 MPa 2,
averaged across these 40 conﬁgurations, compared to the MSE of
25 836 MPa2 for the single-exponent model. Our observations
regarding the superior YS behavior of precipitation-strengthened
superalloys, compared to solid-solution strengthened superal-
loys, for both the Ni- and Fe-Ni-based superalloys, were consis-
tent with literature data.[1] Similarly, our observations concerning
superior YS properties of Ni-based superalloys, compared to
Fe-Ni-based superalloys, in the case of both precipitation and
solid-solution hardening, were also consistent with the available
literature.[1]
4. Experimental Section
Although the primary emphasis here is on the YS, the optimization of
the mechanical properties is assumed to take place within a framework for
joint optimization. [3,13]
Methodology for Maximization of the YS : Our approach accurately cap-
tures the input sources that contribute to variations in the YS observed
relative to variations in the output. The input parameters for the model
used in the present work are [3]
Input ¼ð composition, T, process, defects, grain size, microstructure Þ
(3)
In this context, “defects” are deﬁned broadly, such as to include inho-
mogeneities, impurities, dislocations, or other microstructural features,
while T represents temperature. Analogously, the term “microstructure”
broadly represents microstructures here, at the nano or the microscale,
as well as phase properties, and the term “process” broadly refers to
manufacturing processes and any type of postprocessing. Similarly, the
term “grain size ” generally refers to the size distribution of all grains.
Table S1 from the Supporting Information, comprises an initial step
toward parametrization of the microstructure of the superalloys under
study. Table S1 from the Supporting Information, lists key microstructure
properties that impact the high-temperature strength properties of the
superalloys at hand. According to Table S1 from the Supporting
Information, these microstructure properties involve the precipitate/dis-
persoid type, the volume fraction, the average grain size of the primary
precipitate, the average grain size of the secondary or aged precipitate
form, the grain size of the matrix, as well as the lattice mismatch between
the austenite matrix and precipitate phase at a constant temperature. In
our modeling, we seek to focus on the in ﬂuence of a speci ﬁc microstruc-
tural feature, secondary strengthening phases, such as γ 0, as identi ﬁed by
the existence of in ﬂection (break) points in our modeling results.
Section 4.4 of ref. [4] accounts for the dependence between input sources,
and Section 4.5 of ref. [4] addresses the expected dependence of the US on
the individual input sources listed. The prediction model can be summa-
rized as [3,13]
US ¼ h½composition, T, process, defects ðprocess, TÞ,
grainsðprocess, TÞ, microstructure ðprocess, TÞ/C138
(4)
If the YS corresponding to a certain input combination is known, one
can simply look up the known value. However, if the YS corresponding to a
given input combination is not known, then a prediction step can be
applied (e.g., interpolation or extrapolation). [13]
Methodology for Modeling YS at Elevated Temperatures: Senkov et al. pro-
vide physics-based foundation for the bilinear log model. [6] The diffusion
processes required to initiate phase transformations generally become
noticeable at temperatures T > 0.4 Tm, according to Senkov et al., while
at T < 0.4 Tm, the phase transformations are kinetically restricted. [6] When
T < 0.4 Tm, the atoms are generally not able to move out of the lattice, and
no phase transformations can take place. This tendency applies to low-
entropy alloys, MEAs, and HEAs and serves to explain a model comprising
two exponentials.[3] A single-exponential model does not take into account
diffusion effects and agrees well with the experimental data only at rela-
tively low temperatures, where diffusion-controlling deformation mecha-
nisms can be ignored. But as the temperature increases, the chemical
bonds between the elements become softer. A diffusion-controlled regime
is generally observed above /C25 0.5–0.6 Tm. The diffusion-controlled regime
can be distinguished from the low-temperature regime by a more rapid
drop in strength with increasing temperature because now dislocations
are able to move more easily around obstacles. [3]
Motivated by Figure 3c,d of ref. [3], along with the physics-based
insights from ref. [6], we model the temperature dependence of the
YS(T ), in terms of a bilinear log model, parametrized by the melting tem-
perature, Tm, as follows [13]
YSðTÞ¼ minðlogðYS1ðTÞÞ, log ðYS2ðTÞÞÞ (5)
YS1ðTÞ¼ expð/C0 C1 /C2 T=Tm þ C2Þ,0 < T < Tbreak (6)
YS2ðTÞ¼ expð/C0 C3 /C2 T=Tm þ C4Þ, Tbreak < T < Tm (7)
Tbreak is subjected to a separate physics (diffusion)-induced
constraint[6]
0.35 ≲ Tbreak=Tm ≲ 0.55 (8)
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (7 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

as well as a continuity constraint between the low- and high-temperature
regimes
YS1ðTbreakÞ¼ YS2ðTbreakÞ (9)
Tbreak ¼ ðC4 /C0 C2Þ
ðC3 /C0 C1Þ Tm (10)
As elucidated in, [3,13] a conceptually simple approach for ﬁtting the
model in Equation (5) –(10) to the YS data available consists of ﬁrst
deriving the constant coef ﬁcients, C1 and C2, by applying linear
regression to the data points available to the lowest temperature
region (0 < T < 0.35 Tm) as well as to the intermediate region
(0.35 Tm ≤ T ≤ 0.55 Tm). One can then obtain the constants, C3 and
C4, by applying linear regression to the data points available to the inter-
mediate (0.35 Tm ≤ T ≤ 0.55 Tm) and high-temperature ( T > 0.55 Tm)
regions. Note that Tbreak does not have to be known in advance. As sup-
ported by Equation (10), Tbreak is an inherent property of a given alloy that
emerges from the model as the break point between the two linear
regions. The model in Equation (5) –(7) comprises only four independent
parameters, C1, C2, C3, and C4, which simply can be estimated by applying
linear regression separately to low- and high-temperature regimes, even to
a fairly small data set. Note, furthermore, that for a new alloy system,
Tm does not have to be known experimentally in advance either; a rough
estimate for Tm may be obtained by using “the rule of mixing ” and a more
reﬁned estimate obtained by employing the Calculation of Phase Diagram
simulations.[4]
A superior method for deriving the coef ﬁcients C1, C2, C3, and C4,
entails the concurrent optimization over the low- and high-temperature
regimes using global optimization. Here, one looks to minimize [13]
min
C1 , C2 , C3 , C4
norm2
i
ððYSðTiÞ/C0 yiÞ2Þ (11)
where yi represents the YS values measured
YSðTiÞ¼ minðlogðYS1ðTiÞÞ, log ðYS2ðTiÞÞÞ (12)
and YS 1(Ti) and YS 2(Ti) are modeled, employing Equation (6) and (7),
respectively. MATLAB provides a function, fminunc(), for solving this sort
of unconstrained minimization over a generic function.
Depending on the grain sizes and the compositions comprising the
superalloys, a tri-linear log model may offer a better ﬁt for speci ﬁc super-
alloys:[3,13,24]
YSðTÞ¼ minðYS1ðTÞ, YS2ðTÞ, YS3ðTÞÞ (13)
YS1ðTÞ¼ expð/C0 C1 /C2 T=Tm þ C2Þ,0 < T < Tbreak1 (14)
YS2ðTÞ¼ expð/C0 C3 /C2 T=Tm þ C4Þ, Tbreak1 < T < Tbreak2 (15)
YS3ðTÞ¼ expð/C0 C5 /C2 T=Tm þ C6Þ, Tbreak2 < T < Tm (16)
The trilinear log model is suitable for the analysis of an anomalous yield
stress phenomenon in select superalloys, such as CMSX-4. [3] Table S2 and
S3 from the Supporting Information, present comparison of models com-
prising one exponential, two exponents, three exponentials, and four expo-
nentials (a practical approach to model selection) for the superalloy
datasets available for this study. As explained in Supplementary Note 7
of ref. [3], a practical approach to model selection, supported by
Table S2 and S3 from the Supporting Information, assumes one stops
increasing the model order, once the MSE tapers off. The practical
approach assumes the model selected is the one corresponding to the
onset of the tapering.
Supplementary Figure 5 and 6 of ref.[3] capture an application of piece-
wise linear regression, a classical technique, needed to address challenges
imposed by nonconvexity of the objective function possible, in cases of
trilinear or quad-linear log models. In such cases, one can expand the
parameter set such as to explicitly include the break temperatures. The
extra parameters help in terms of maintaining dependence across temper-
ature regimes during concurrent optimization across the temperature
regimes. Supplementary Figure 7 and 8 of ref. [3] capture MATLAB
pseudo-code for the bilinear log model (a convex case with no piece-wise
linear regression needed) and a trilinear log model (a possibly nonconvex
case, one bene ﬁtting from piecewise linear regression).
As further explained in Supplementary Note 8 of ref. [3], at least ( n þ 1)
data points are needed for the accurate derivation of a model comprising
of n exponentials, where n = 1, 2, 3, … , assuming individual, piecewise
linear ﬁts (no concurrent optimization). However, in the case of concur-
rent optimization over the low- and high-temperature regimes, using an
algorithm based on the MATLAB pseudo-code in Supplementary Figure 7
of ref. [3] for the bilinear log model, four data points are needed for the full
deﬁnition of the problem (since the bilinear log model contains four
parameters). Similarly, for concurrent optimization over the individual-
temperature regimes, using an algorithm based on the MATLAB
pseudo-code in Supplementary Figure 8 of ref. [3] for the trilinear log
model, eight data points are needed for full de ﬁnition of the problem
(since the model now contains eight parameters). Table S2 and S3 from
the Supporting Information, illustrate that large majority of the superalloy
compositions under consideration comprise of fewer than eight
(T, YS( T )) combinations.
As for the black-box models, it is important to consider the small num-
ber of YS( T ) data points for a given superalloy composition, per Table S2
and S3 from the Supporting Information. With typically only 5 –7 YS( T )
combinations measured for most superalloy compositions, excluding
the one corresponding to no YS at the solvus temperature, black-box mod-
els may be limited to a single layer and several nodes (assuming at least
one input data point per model parameter to be estimated). The small size
of the data set does not allow for separate training and testing sets. The
small size of the data set, for each superalloy composition, in this case,
does not allow for meaningful implementation of black-box models.
Hence, to make the most of the limited data set available, it is important
to consider the physics-based modeling of the YS.
Supporting Information
Supporting Information is available from the Wiley Online Library or from
the author.
Acknowledgements
X.F. and P.K.L. very much appreciate the support of the U.S. Army
Research Of ﬁce Project (W911NF-13-1-0438 and W911NF-19-2-0049)
with the program managers, Drs. M. P. Bakas, S. N. Mathaudhu, and
D. M. Stepp. P.K.L. thanks the support from the National Science
Foundation (DMR-1611180, 1809640, and 2226508) with the program
directors, Drs. J. Madison, J. Yang, G. Shi ﬂet, and D. Farkas. X.F. and
P.K.L. also appreciate the support from the Bunch Fellowship. X.F. and
P.K.L. would like to acknowledge funding from the State of Tennessee
and Tennessee Higher Education Commission (THEC) through their
support of the Center for Materials Processing (CMP). BS very much
appreciates the support from the National Science Foundation (IIP-
1447395 and IIP-1632408), with the program directors, Drs. G. Larsen
and R. Mehta, from the U.S. Air Force (FA864921P0754), with J. Evans
as the program manager, and from the U.S. Navy (N6833521C0420), with
Drs. D. Shi ﬂer and J. Wolk as the program managers. The authors also
want to thank Dr. Graham Tewksbury for offering insightful comments
on strengthening mechanisms in superalloys during an October 21,
2021, material science graduate seminar presentation, conducted by BS
at Oregon State University. The authors similarly want to thank
Dr. Chanho Lee for bringing precursors to Figure S1 –S3 from the
Supporting Information, to their attention.
Conﬂict of Interest
The authors declare no con ﬂict of interest.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (8 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

Data Availability Statement
The data that support the ﬁndings of this study are available from the
corresponding author upon reasonable request.
Keywords
high temperature, machine learning, physics-based modeling, structural
materials, superalloys, yield strength
Received: December 28, 2022
Revised: February 27, 2023
Published online: March 23, 2023
[1] M. J. Donachie, S. J. Donachie, in Superalloys, A Technical Guide 2nd
edition, ASM International, Almere, The Netherlands 2002.
[2] B. Steingrimsson, X. Fan, A. Kulkarni, D. Kim, P. K. Liaw, US
Patent16/782,829, 2020.
[3] B. Steingrimsson, X. Fan, X. Yang, M. C. Gao, Y. Zhang, P. K. Liaw,
NPJ Computational Materials 2021, 7.
[4] B. Steingrimsson, X. Fan, A. Kulkarni, M. C. Gao, P. K. Liaw, in High-
Entropy Materials: Theory, Experiments, and Applications , (Eds:
J. Brechtl, P. K. Liaw), Springer Nature, Cham, Switzerland 2021,
pp. 115 –238.
[5] A. Agrawal, P. D. Deshpande, A. Cecen, G. P. Basavarsu, Integrat.
Mater. Manuf. Innov. 2014, 3, 90.
[6] O. N. Senkov, S. Gorsse, D. B. Miracle, Acta Mater. 2019, 175, 394.
[7] Z. Wu, H. Bei, G. M. Pharr, E. P. George, Acta Mater. 2014. 81, 428.
[8] F. Maresca, W. A. Curtin, Acta Mater. 2020, 182, 235.
[9] H. K. D. H .Bhadeshia, in Nickel Based Superalloys , University of
Cambridge, Cambridge, UK 2019.
[10] T. T. Le, W. Fu, J. H. Moore, Bioinformatics 2020, 36, 250.
[11] R. C. Reed, in The Superalloys: Fundamentals and Applications ,
Cambridge University Press, Cambridge, UK 2008.
[12] C. T. Sims, N. S. Stoloff, W. C. Hagel, Superalloys II, Vol. 8. Wiley, New
York 1987.
[13] B. Steingrimsson, X. Fan, R. Feng, P. K. Liaw, Appl. Mater. Today
2023, 31, 101747.
[14] H. Chen, A. Kauffmann, S. Laube, I. C. Choi, R. Schwaiger, Y. Huang,
K. Lichtenberg, F. Muller, B. Gorr, H. J. Christ, M. Heilmaier, Metall.
Mater. Trans. A 2018, 49, 772.
[15] A. Seeger, Mater. Sci. Eng. A 2001, 319–321, 254.
[16] A. Seeger, Zeitschrift für Metallkunde 2002, 93, 760.
[17] A. Sengupta, S. K. Putatunda, L. Bartosiewicz, et al., J. Mater. Eng.
Perform. 1994, 3, 73.
[18] B. Kear, Trans. Metall. Soc. AIME 1962, 224, 674.
[19] B. Kear, Trans. Metall. Soc. AIME 1962, 224, 669.
[20] T. Kruml, E. Conforto, B. Lo Piccolo, D. Caillard, J. L. Martin, Acta
Mater. 2002, 50, 5091.
[21] Z. Chen, K. Kishida, H. Inui, M. Heilmaier, U. Glatzel, G. Eggeler, Acta
Mater. 2022, 238, 118224.
[22] E. I. Galindo-Nava, C. M. F. Rae, Mater. Sci. Eng. A 2015, 636,
434.
[23] E. I. Galindo-Nava, L. D. Connor, C. M. F. Rae, Acta Mater. 2015, 98,
377.
[24] F. Otto, A. Diouhý, C. Somsen, H. Bei, G. Eggeler, E. P. George, Acta
Mater. 2013, 61, 5743.
www.advancedsciencenews.com www.aem-journal.com
Adv. Eng. Mater. 2023, 25, 2201903 2201903 (9 of 9) © 2023 Wiley-VCH GmbH
 15272648, 2023, 14, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202201903 by Xian Jiaotong University, Wiley Online Library on [27/11/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
