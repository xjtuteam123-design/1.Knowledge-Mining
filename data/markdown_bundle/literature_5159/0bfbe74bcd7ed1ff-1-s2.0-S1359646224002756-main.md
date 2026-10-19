# 1-s2.0-S1359646224002756-main

<!-- source: D:\总文献\1-s2.0-S1359646224002756-main.pdf -->
<!-- file_sha256: 125bff95bf13e11ef8dc284dec9c8e79c7349edc4f8c678f4e1da64bf0a34f60 -->

## Page 1

Scripta Materialia 252 (2024) 116240
Available online 24 June 2024
1359-6462/© 2024 Acta Materialia Inc. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar
technologies.
Accelerated discovery of refractory high-entropy alloys for 
strength-ductility co-optimization: An exploration in NbTaZrHfMo system 
by machine learning 
Cheng Wen
a , b
, Haicheng Shen
a , c
, Yuwan Tian
a , c , *
, Gongqi Lou
a
, Nanchuan Wang
a
, 
Yanjing Su
d 
a
School of Mechanical Engineering, Guangdong Ocean University, Zhanjiang, 524088, China 
b
Zhanjiang Key Laboratory of Ocean Engineering and Equipment Corrosion and Protection, Zhanjiang, 524088, China 
c
Guangdong Provincial Ocean Equipment and Manufacturing Engineering Technology Research Center, Zhanjiang, 524088, China 
d
Beijing Advanced Innovation Center for Materials Genome Engineering, University of Science and Technology Beijing, Beijing, 100083, China 
ARTICLE INFO 
Keywords: 
Refractory high-entropy alloys 
Strength-ductility co-optimization 
Machine learning 
Alloys design 
NbTaZrHfMo 
ABSTRACT 
High temperature (HT) strength and room temperature (RT) ductility trade-offs are always unavoidable in the 
design of refractory high entropy alloys (RHEAs). Exploring the vast chemistry space to find optimally strong and 
ductile RHEAs remains a highly challenging task. Herein, we formulate a machine learning-based design strategy 
fusing uncertainty estimation and clustering analysis to explore a special alloy system (NbTaZrHfMo) for 
collaborative optimization of HT strength and RT ductility. Four non-equimolar alloys with a superior combi -
nation of HT strength, RT ductility and HT specific yield strength were discovered and synthetized. The influence 
of elements on mechanical properties are analyzed and an optimal composition range is identified based on 
model prediction. This work provides a general design approach enabling the concurrent optimization of con -
flicting properties with a small data-trained machine learning model, thereby producing a recipe to accelerate 
the discovery of desired RHEAs and other materials within a vast search space. 
Refractory high entropy alloys (RHEAs) are an emerging type of high 
temperature (HT) material that has drawn much attention due to their 
ability to retain high strength at 1000 ℃ and above [ 1-2 ]. By employing 
refractory elements with high melting points (T
m
) from Group IVB-VIB, 
several RHEAs have already demonstrated HT strength that outperform 
Ni-base superalloys. Typically, the NbTaMoWV alloy exhibits yield 
stress up to 477 MPa, even at 1600 ℃ [ 3 ]. However, most RHEAs suffer 
from room temperature (RT) brittleness with compressive fracture strain 
(FS
RT
) below 10 % and thus are not machinable. As an exception, the 
equimolar NbTaZrHfTi alloy exhibits outstanding deformability with 
FS
RT 
over 50%, but its weak temperature resistance is not competitive 
compared to other RHEAs or superalloys [ 4 ]. Strength-ductility-driven 
composition design has been a key issue in the development of RHEAs 
since their proposal. Sheikh et al. [ 5 ] first proposed a valence electron 
concentration (VEC) rule that there exists a threshold VEC of 4.5 below 
which intrinsic ductility can be achieved in RHEAs. Mak et al. [ 6 ] found 
that VEC = 5 is an approximate borderline. Consequently, the use of VEC 
< 5 is proposed for rapid screening of the ductile compositions of high 
entropy alloys (HEAs). Senkov et al. [ 7 ] further noted that there is a 
proportional trend between the VEC of RHEAs and their RT ductility, but 
there is no clear boundary value separating toughness from brittleness. 
VEC alone may not sufficiently characterize ductility in RHEAs. Never -
theless, the consensus among scholars is that reducing VEC is beneficial 
to their ductility design. Concerning the strength improvement, 
increasing Mo content significantly contributes to the strength of RHEAs 
[ 8 ], especially at HT [ 9-10 ]. Recently, Hu et al. [ 11 ] further revealed 
that Mo-containing RHEAs have in general higher HT strength than 
those without Mo. The addition of W and Ta can also improve the 
temperature resistance of RHEAs, but will seriously deteriorate their RT 
ductility [ 12-15 ]. 
Exploring the vast chemistry space to find optimally strong and 
ductile RHEAs remains a highly challenging task, given a palette con -
taining more than ten elements. Several efforts have been attempted to 
accelerate the discovery of alloys with desired properties. Maresca et al. 
[ 16 ] performed a computationally guided search in an 
Al-Cr-Hf-Mo-Nb-Ta-Ti-V-W-Zr HEA system to identify alloy 
* Corresponding author. 
E-mail address: tianyuwan90@163.com (Y. Tian). 
Contents lists available at ScienceDirect 
Scripta Materialia 
journal homepag e: www.journa ls.elsevier.c om/scripta- materialia 
https://doi.org/10.1016/j.scriptamat.2024.116240 
Received 8 April 2024; Received in revised form 13 June 2024; Accepted 14 June 2024

## Page 2

Scripta Materialia 252 (2024) 116240
2
compositions with potentially high HT strength. Menou et al. [ 17-18 ] 
proposed a computation-based strategy to design light and strong 
single-phase HEAs by searching for alloys in the 
Al-Co-Cr-Cu-Fe-Hf-Mn-Mo-Nb-Ni-Ru-Ta-Ti-V-W-Zr composition space 
using an evolutionary algorithm. Similar work has been undertaken for 
the composition search of 5-element HEAs with hardness improvement 
in a 16-element palette [ 19 ]. Actually, searching the broad swaths of 
compositions within a given alloy system is likely to be more effective 
for finding the target alloy with the desired properties, avoiding blind 
and time-consuming searches on many ingredient continents. Recently, 
efficient composition design of RHEAs have been reported in some 
special chemistry systems such as Nb-Ta-Ti-Hf-Mo [ 20 ], W-Ta-V-Ti-Cr 
[ 21 ], and W-Mo-V-Ta-Nb-Al [ 22 ]. 
Here we focus on a not-yet systematically-explored alloys system 
NbTaZrHfMo, derived from the two typical RHEAs of NbTaMoWV and 
NbTaZrHfTi. In this chemical space, Nb and Ta have a VEC value of 5 
that is the threshold suggestion for toughness design in RHEAs [ 6 ], Zr 
and Hf with low VEC value (4) should be beneficial to ductility 
improvement. Mo addition may be unfavorable due to its higher VEC 
value (6), but is expected to provide considerable (HT) strengthening of 
RHEAs. We formulate a strategy based on machine learning (ML) by 
integrating an uncertainty estimation for alloy search and clustering 
analysis for alloy selection, as shown in Fig. 1(a) , systematically 
exploring the NbTaHfZrMo composition space to accelerate the dis -
covery of RHEAs with synergistic improvements in strength and 
ductility, i.e., the yield strength at HT (YS
1000 ℃
) and fracture strain at 
RT (FS
RT
). 
Two datasets of YS
1000 ℃ 
and FS
RT 
are first assembled from the 
literature and our lab. All the training data used for ML modeling are for 
alloys fabricated by vacuum arc-melting only and their property is 
measured in the as-cast form, in order to minimize the influence of 
processing method. Accordingly, composition is regarded as the primary 
factor influencing the properties of RHEAs. These data are then used to 
train ML models using support vector machine algorithm, which is al -
ways used for modeling small data. Using the elemental content as input, 
the ML model is evaluated by a 5-fold cross-validation method. From 
Fig. 1(b) , the root mean square error ( RMSE ) of the model prediction on 
YS
1000 ℃ 
is 138 MPa, and the correlation coefficient r
cv 
between the 
experimental strength and the predicted values approaches 0.9. The data 
points distributed along the diagonal line indicates that the model is well 
fitted overall. However, there appears to be an obvious underestimation 
of yield strength within the high-value range. For these alloys with 
YS
1000 ℃ 
over 800 MPa, the predicted RMSE is 218 MPa, far beyond the 
average value, while RMSE of the remaining alloys is only 110 MPa. The 
same situation occurs in the prediction on RT ductility (seen in Fig. S1). 
Such model prediction is actually unfavorable for guiding RHEAs design, 
considering the goal of high strength and high ductility. 
Actually, for the small data-trained ML model, uncertainty consid -
eration of the target prediction is essential, especially when applied to 
design materials in a large search space [ 23 ]. The expected improve -
ment (EI) utility indicator balances exploitation (choosing the material 
with the high predicted target) and exploration (using the predicted 
uncertainties to study regions of the searchspace where the model is less 
accurate), as shown in Fig. 1(a) . The EI indicator has been demonstrated 
as efficient for accelerating materials discovery for single-objective 
optimization [ 24-25 ]. We therefore utilize EI indicators instead of 
directly using the ML-predicted YS
1000 ℃ 
and FS
RT 
to guide alloy dis -
covery. The statistical method of ‘bootstrap ’ sampling is used to evaluate 
the properties-prediction uncertainty of each alloy in the NbTaZrHfMo 
system (the molar content of each element is restricted to 5~35 at.% to 
produce 553,401 alloys). Then, the EI values of strength and ductility for 
a given alloy can be calculated according to the prediction distribution. 
The details of EI calculation could be found in our previous work [ 24 ]. 
Unlike the work of single-property optimization using an EI indica -
tor, the balance between antagonistic objectives must be considered in 
multi-objectives design. After obtaining the two EI values for each 
alloy in NbTaZrHfMo composition system, we rank all the alloys 
using non-dominated sorting based on these EI values to identify 
the Pareto front for the virtual space. The EI values of YS
1000 ℃ 
and 
FS
RT 
for RHEAs are shown in the 2D Pareto plot in Fig. 1(c) , where the 
boundary points define an EI-based Pareto front (EIPF) representing the 
optimal trade-off between two objectives. All candidate compositions on 
the Pareto front (PF) are equally favorable and expected to provide 
flexibility in the selection of potential alloys with strength-ductility 
improvement. In this study, clustering analysis on the EIPF is utilized 
to determine the potential alloys viable for experimental synthesis. 
Specifically, we use the K-means algorithm and the “ elbow method ” 
[ 26 ] to select a reasonable number of clusters centers ( K ) by calculating 
the sum of squares within groups (WGSS) as K varies. As shown in Fig. 1 
(e) , the WGSS decreases very slowly after K = 4, thus we consider four 
clusters as a good fit of the data. Another two widely-used methods give 
the same K value recommendation (see details in Supplementary Ma -
terial). Thus, we cluster the data points in the EIPF using K = 4, and four 
corresponding alloys are accordingly identified, as marked in Fig. 1(c) . 
Table 1 provides the composition information of the newly-designed 
RHEAs. In Fig. 1(d) , the model-predicted YS
1000 ℃ 
and FS
RT 
of RHEAs 
in the EIPF are plotted together with that of the original data, in which 
the error bars represent prediction uncertainty. These candidate alloys 
exhibit decent properites combination, with 450 MPa ~ 1200 MPa 
YS
1000 ℃ 
and 10% ~ 40% FS
RT
. According to the error bars, the pre -
diction deviation shows an increasing trend with the increase in both HT 
strength and RT ductility. It means that the model-prediction uncer -
tainty increases as the composition exploration moves to the high-value 
region of alloy ’ s properties. 
The four designed RHEAs are then synthesized by vacuum arc- 
melting and phase-detected by XRD before and after compression 
deformation at 1000 ℃ . As shown in Fig. 2(a) and (b) , the XRD patterns 
suggest that the phase structure is the same before and after hot defor -
mation for alloys A1 and A2, with a disordered BCC solid solution. The 
as-cast alloys A3 and A4 show a BCC structure with an intermetallic (IM) 
phase, while IM is not detected for alloy A3 after HT deformation, and 
some diffraction peaks of IM phase disappear for alloy A4. From alloy Al 
to A4, the diffraction peak shifts to the right as Mo content increases 
could be identified, indicating a reduction of the lattice parameter. This 
may be ascribed to the replacement of Zr or Hf with the larger atomic 
radius of Mo. 
Fig. 2(c) and (d) provide the compressive stress-strain curves of the 
designed RHEAs at RT and 1000 ℃ . Fig. 3(a) illustrates a comparison 
between the properties of these alloys to those in the original data. Alloy 
A1 shows excellent RT ductility with FS
RT 
over 50%, which is compa -
rable to the typical NbTaZrHfTi alloy, while its YS
1000 ℃ 
value is nearly 
1.5 times that of the latter. The YS
1000 ℃ 
value of alloy A4 exceeds 1000 
MPa beyond most of the reported alloys. At a similar high-level of 
YS
1000 ℃
, the FS
RT 
of alloy A4 is improved by more than 3 times from 
4.3% (Al
0.025
Ti
0.2
V
0.075
Zr
0.1
Cr
0.2
Nb
0.2
Mo
0.2
) [ 27 ] to 17.1%. When 
compared to another typical NbTaMoWV alloy, alloy A4 shows a 26% 
increase in HT strength, and the significant improvement in FS
RT 
re -
lieves the alloy of RT brittleness, making the alloy more mechanically 
workable. It is worth emphasizing that the RT yield strength (YS
RT
) of 
alloy A2 is 1501 MPa and the FS
RT 
is 30.5%. In a recent study [ 7 ], 
Senkov et al. pointed out that RHEAs with a minimum of 30% FS
RT 
may 
possess commercially relevant levels of tensile ductility (~4%), which 
are correlated with the compressive YS
RT 
of ≤ 1500 MPa. The A2 alloy is 
such RHEAs that is currently the most likely to achieve the objective of 
extending the use temperature of structural alloys. Additionally, we can 
notice that the newly-designed RHEAs belong to the 
(NbTa)
0.48
(ZrHf)
x
Mo
0.52-x 
subsystem, and from A1 to A4, the HT 
strength increases gradually as the RT ductility decreases with the 
addition of Mo and a certain reduction in Zr and Hf. According to the 
VEC rule, the increase of Zr and Hf lowers VEC and benefits alloys 
ductility. This implies that the potential relationship between alloy 
components and mechanical properties is identified by the model by 
C. Wen et al.

## Page 3

Scripta Materialia 252 (2024) 116240
3
Fig. 1. The ML-driven alloys design. (a) The workflow including four steps; (b) The prediction value of YS
1000 ℃ 
for the alloys by ML model; (c) The EIPF of all the 
alloys in the NbTaZrHfMo system and composition identification by clustering alloys in the EIPF; (d) ML-predicted YS
1000 ℃ 
and FS
RT 
of the alloys in the EIPF with 
uncertainty estimation; (e) Determination of the number of cluster centers ( K ) by “ elbow method ” . 
C. Wen et al.

## Page 4

Scripta Materialia 252 (2024) 116240
4
learning from the original data information. This is very important 
especially when we want to design alloys in a vast space by adjusting the 
ratios of multiple elements. 
To further explore the temperature-resistance performance of the 
newly-designed RHEAs, compressive deformation tests are conducted at 
1200 ℃ . Fig. 3(b) compares their YS
1200 ℃ 
values to that of typical 
RHEAs and shows significant improvement in softening resistance. 
Particularly, alloys A2 and A3 show a high yield stress at 1200 ℃ , and 
the simultaneously-generated higher RT ductility make them more 
attractive than typical RHEAs (for example, NbTaMoWVTi [ 29 ] with 
FS
RT 
below 14%). The IM phase cannot be detected for alloy A3 after HT 
deformation, indicating the possible dissolution of secondary phases at 
1000 ℃ and greater, as previously reported for multi-phase RHEAs [ 30 ]. 
However, the strength loss is only 34.2% from RT to 1000 ℃ and is 
52.3% from RT to 1200 ℃ . It can be inferred that the SSS effect [ 28 ] is 
important for alloy A3 at HT and thus can contribute to its strength. 
RHEAs with extremely high YS
RT 
values ( > 1600 MPa) are not attractive 
HT structural materials as they are brittle at RT and always lose strength 
rapidly above 1000 ℃ , typically like RHEAs containing Al [ 27 , 30 ] and 
Si [ 30 ]. According to Fig. 3(b) , as a comparison, the YS
RT 
of 
AlMo
0.5
NbTa
0.5
TiZr can reach up to 2000 MPa, but it drops precipi -
tously to 250 MPa at 1200 ℃ , indicating its low temperature resistance. 
Meanwhile, the FS
RT 
below 10% indicates its poor RT workability. 
Among the designed RHEAs, alloy A4 exhibits the best HT strength with 
YS
1200 ℃ 
reaching 940 MPa, and its yield strength loss is below 12% from 
1000 ℃ to 1200 ℃ , which is superior to almost all other RHEAs. A 
much-delayed reduction behavior in strength indicates its substantial 
resistance to softening at HT. In contrast to the typical NbMoTaWV 
alloy, the YS
1200 ℃ 
value of alloy A4 increases by 27.9%. The FS
RT 
exceeding 17% also indicates it has much better RT workability than 
NbMoTaWV. When compared to the equimolar NbTaZrHfMo, the 
designed alloys A2 and A3 show a similar temperature-bearing level but 
with a notable increase ratio of FS
RT 
at 25.6% and 90.6 %, and the yield 
strength of alloy A4 at 1000 
◦
C and 1200 
◦
C increase by 14.5% and 
35.4%, respectively. With the further intuitive comparison of 
YS
1000 ℃
/YS
RT 
and YS
1200 ℃
/YS
RT 
shown in Fig. 3(c) and Fig. 3(d) , the 
Table 1 
The composition, phase structure and mechanical properties of the designed RHEAs. 
No. Designed RHEAs Phase (as-cast) YS
RT
, MPa YS
1000 ℃
, MPa YS
1200 ℃
, MPa FS
RT
, % 
A1 Nb0.29Ta0.18Zr0.24Hf0.2Mo0.09 BCC 1217 714 304 > 50 
A2 Nb0.26Ta0.19Zr0.19Hf0.16Mo0.2 BCC 1501 974 669 30.5 
A3 Nb0.31Ta0.17Zr0.15Hf0.14Mo0.23 BCC + IM 1487 979 710 20.1 
A4 Nb0.27Ta0.21Zr0.13Hf0.13Mo0.26 BCC + IM 1547 1061 940 17.2 
vs. NbTaZrHfMo BCC 1524 927 694 16 
vs. NbTaZrHfTi BCC 929 295 92 > 50 
vs. NbTaMoWV BCC 1246 842 735 1.7 
Fig. 2. The phase structure and mechanical properties of the newly-designed RHEAs. (a) XRD paterns of the alloys as-cast (a) and after deformatin at 1000 ℃ (b); The 
compressive stress-strain curves of the newly-designed alloys at RT (c) and 1000 ℃ (d). 
C. Wen et al.

## Page 5

Scripta Materialia 252 (2024) 116240
5
newly-designed alloys exhibit better strength retention than most of the 
reported RHEAs, simultaneously exhibiting superior RT ductility. 
Density is another important concern for alloys used in flight appli -
cations, and alloys with high specific strength (strength-to-density ratio) 
are preferable for reducing weight and fuel consumption. In fact, the 
existing RHEAs always suffer from high density due to the addition of 
heavy elements like W, Ta and Hf. Therefore, we compare the specific 
yield strength (SYS) at 1000 ℃ (YS
1000 ℃
/ ρ ) and 1200 ℃ (YS
1200 ℃
/ ρ ) of 
the newly-synthesized alloys with the reported RHEAs. As shown in 
Fig. 3(e) , the new alloys form a new PF of the YS
1000 ℃
/ ρ and FS
RT
. For 
those RHEAs exhibiting high RT ductility (over 50% FS
RT
), alloy A1 
shows a conspicuous improvement of YS
1000 ℃
/ ρ . Alloy A2 dominates 
such RHEAs with medium ductility with 25~35 % FS
RT
. Although the 
Al/Ti/V-containing RHEAs naturally show low density and thus produce 
high YS
1000 ℃
/ ρ , their very poor RT ductility also leads to little 
machineability, making them unattractive for various applications. 
Regarding YS
1200 ℃
/ ρ , our designed alloys exhibit almost absolute su -
periority to the reported RHEAs, except for NbTaTiHfMo, by substituting 
Ti with Zr to lower alloy density. The FS
RT
-YS
1200 ℃
/ ρ PF moves forward 
obviously, indicating a great attraction and potential of the new RHEAs 
to be used as HT structural material. By exploring the special 
NbTaZrHfMo alloy system from an equimolar composition to non- 
equimolar compositions based on our ML approach, further extensive 
and significant co-improvement of RT ductility, HT strength and HT 
specific yield strength can be realized. The microstructure of the newly- 
designed RHEAs present typical dendrite-interdendrite morphology (see 
Fig. 3. The properties comparision between the newly-designed alloys and the reported RHEAs. (a) The HT strength and RT ductility; (b) The temperature-resistence 
in strength; (c) The ratio of yield stress at 1000 ℃ to that at RT (YS
1000 ℃
/YS
RT
); (d) The ratio of yield stress at 1200 ℃ to that at RT (YS
1200 ℃
/YS
RT
); (e) The specific 
yield strength at 1000 ℃ (YS
1000 ℃
/ ρ ) and (f) the specific yield strength at 1200 ℃ (YS
1200 ℃
/ ρ ) . 
C. Wen et al.

## Page 6

Scripta Materialia 252 (2024) 116240
6
in Supplementary Material). 
Even if the ML models may lead to an underestimated prediction of 
alloy properties within the high-value region, it also can yield reason -
able trends, providing us an effective tool to understand RHEAs and 
thereby accelerating composition screening. Therefore, we use the ML- 
model to predict YS
1000 ℃ 
and FS
RT 
for all alloys in the NbTaZrHfMo 
system to reveal the element influence on alloy properties. As plotted in 
Fig. 4 , the desired properties region is marked by a dashed box repre -
senting a co-optimization for HT strength (temperature-resistance) and 
RT ductility (workability) of RHEAs. Among the five elements, Mo 
shows the most significant impact on alloys ’ mechanical properties, and 
Mo content tends to decrease from the region with high FS
RT 
to that with 
high YS
1000 ℃
. The preferable Mo content is approximately 6~28 at.% in 
such alloy system, which actually covers the range of the newly- 
designed alloys (9~27 at.%). It is worth noting that excessively high 
or low Mo content is detrimental to multi-properties optimization in 
RHEAs design. The increase of Zr and Hf are beneficial to alloy ductility, 
and there is a difference in the favorable range (Hf, 12~20 at.%, Zr, 
15~28 at.%) between them even if they have the same low VEC value of 
4. The trend of a lower content of Hf is advantageous given its higher 
cost when considering the practical application of RHEAs. The effect of 
Ta content on alloy properties is not obvious in such composition sys -
tem. The favorable content is a narrow range approximately 16~25 at. 
%, and excessively high content is always undesirable for both HT 
strength and RT ductility. From the heatmap highlighting Nb, it seems 
that a medium-to-high content of Nb is beneficial for alloy design with a 
strength-ductility balance. It also shows that Nb content below 10 at.% 
will significantly reduce the RT ductility and HT strength of RHEAs. 
In summary, we formulate a data-driven strategy combining ML- 
model prediction of alloy properties, EI-based uncertainty utility and 
clustering-based selection of alloy composition to systematically explore 
the NbTaZrHfMo chemical space, an alloy system determined by 
experience-based intuition, to accelerate the design of RHEAs with a 
synergistic improvement in HT strength and RT ductility. This approach 
is demonstrated as efficient, and four non-equimolar alloys with a su -
perior combination of HT strength, RT ductility and HT specific yield 
strength are discovered and synthetized, which are expected to serve as 
potential alternative materials for HT structural applications. Addi -
tionally, the influence of elements on alloy properties are also analyzed 
in this system, based on ML model prediction, to help us to understand 
the composition design of RHEAs. This work provides a general design 
approach enabling concurrent optimization of conflicting properties 
with small data-trained machine learning. It also offers a recipe to 
rapidly optimize other special materials systems within a vast search 
space and multi-property requirements. 
CRediT authorship contribution statement 
Cheng Wen: Writing – original draft, Methodology, Investigation, 
Conceptualization. Haicheng Shen: Validation, Software, Data cura -
tion. Yuwan Tian: Writing – review & editing, Formal analysis, 
Conceptualization. Gongqi Lou: Software. Nanchuan Wang: Valida -
tion, Software, Data curation. Yanjing Su: Resources, 
Conceptualization. 
Fig.4. The heatmap of properties distribution predicted by ML model for NbTaZrHfMo composition system, revealing the ML-identified relationship between the five 
elements and alloys properties. 
C. Wen et al.

## Page 7

Scripta Materialia 252 (2024) 116240
7
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgements 
This work was supported by the National Natural Science Foundation 
of China (Grant No. 52203293) and the National Key Research and 
Development Program of China (Grant No. 2021YFB3802100). 
Supplementary materials 
Supplementary material associated with this article can be found, in 
the online version, at doi:10.1016/j.scriptamat.2024.116240 . 
References 
[1] J. Chen, X. Zhou, W. Wang, B. Liu, Y. Lv, W. Yang, D. Xu, Y. Liu, A review on 
fundamental of high entropy alloys with promising high-temperature properties, 
J. Alloys Compd. 760 (2018) 15 – 30, https://doi.org/10.1016/j. 
jallcom.2018.05.067 . 
[2] O.N. Senkov, D.B. Miracle, K.L. Chaput, J.P. Couzinie, Development and 
exploration of refractory high entropy alloys-A review, J. Mater. Res. 19 (2018) 
3092 – 3128, https://doi.org/10.1557/jmr.2018.153 . 
[3] O.N. Senkov, G.B. Wilks, D.B. Miracle, C.P. Chuang, P.K. Liaw, Refractory high- 
entropy alloys, Intermetallics 18 (2010) 1758 – 1765, https://doi.org/10.1016/j. 
intermet.2010.05.014 . 
[4] O.N. Senkov, J.M. Scott, S.V. Senkov, F. Meisenkothen, D.B. Miracle, C. 
F. Woodward, Microstructure and elevated temperature properties of a refractory 
TaNbHfZrTi alloy, J. Mater. Sci. 47 (2012) 4062 – 4074, https://doi.org/10.1007/ 
s10853-012-6260-2 . 
[5] S. Sheikh, S. Shafeie, Q. Hu, J. Ahlstr ¨om, Alloy design for intrinsically ductile 
refractory high-entropy alloys, J. Appl. Phys. 120 (2016) 164902, https://doi.org/ 
10.1063/1.4966659 . 
[6] E. Mak, B. Yin, W.A. Curtin, A ductility criterion for bcc high entropy alloys, 
J. Mech. Phys. Solids 152 (2021) 104389, https://doi.org/10.1016/j. 
jmps.2021.104389 . 
[7] O.N. Senkov, D.B. Miracle, S.I. Rao, Correlations to improve room temperature 
ductility of refractory complex concentrated alloys, Mater. Sci. Eng., A 820 (2021) 
141512, https://doi.org/10.1016/j.matdes.2024.112762 . 
[8] C.C. Juan, K.K. Tseng, W.L. Hsu, M.H. Tsai, C.W. Tsai, C.M. Lin, S.K. Chen, S.J. Lin, 
J.W. Yeh, Solution strengthening of ductile refractory HfMoxNbTaTiZr high- 
entropy alloys, Mater. Lett. 175 (2016) 284 – 287, https://doi.org/10.1016/j. 
matlet.2016.03.133 . 
[9] P. Singh, A. Sharma, A.V. Smirnov, M.S. Diallo, P.K. Ray, G. Balasubramanian, D. 
D. Johnson, Design of high-strength refractory complex solid-solution alloys, npj 
Comput. Mater. 4 (2018) 16, https://doi.org/10.1038/s41524-018-0072-0 . 
[10] K.K. Tseng, C.C. Juan, S. Tso, H.C. Chen, C.W Tsai, J.W. Yeh, Effects of Mo, Nb, Ta, 
Ti, and Zr on Mechanical Properties of Equiatomic Hf-Mo-Nb-Ta-Ti-Zr Alloys, 
Entropy 21 (2018) 15, https://doi.org/10.3390/e21010015 . 
[11] Q. Hua, S. Guo, J.L. Guo, F.F. Luo, J.W. Wang, Effect of Mo on high-temperature 
strength of refractory complex concentrated alloys: A perspective of 
electronegativity difference, J. Alloys Compd. 906 (2022) 164186, https://doi.org/ 
10.1016/j.jallcom.2022.164186 . 
[12] Y. Yuan, Y. Wu, Z. Yang, X. Liang, Z. Lei, H. Huang, H. Wang, X. Liu, K. An, W. Wu, 
Z. Lu, Formation, structure and properties of biocompatible TiZrHfNbTa high- 
entropy alloys, Mater. Res. Lett. 7 (2019) 225 – 231, https://doi.org/10.1080/ 
21663831.2019.1584592 . 
[13] Q. Li, H. Zhang, D. Li, Z. Chen, Z. Qi, The effect of configurational entropy on 
mechanical properties of single BCC structural refractory high-entropy alloys 
systems, Int. J. Refract. Met. Hard Mater. 93 (2020) 105370, https://doi.org/ 
10.1016/j.ijrmhm.2020.105370 . 
[14] V.T. Nguyena, M. Qian, Z. Shi, T. Song, L. Huang, J. Zou, Compositional design of 
strong and ductile (tensile) Ti-Zr-Nb-Ta mediumentropy alloys (MEAs) using the 
atomic mismatch approach, Mater. Sci. Eng., A 742 (2019) 762 – 772, https://doi. 
org/10.1016/j.msea.2018.11.054 . 
[15] M. Wang, Z. Ma, Z. Xu, X. Cheng, Microstructures and mechanical properties of 
HfNbTaTiZrW and HfNbTaTiZrMoW refractory high-entropy alloys, J. Alloys 
Compd. 803 (2019) 778 – 785, https://doi.org/10.1016/j.jallcom.2019.06.138 . 
[16] F. Maresca F, W.A. Curtin, Mechanistic origin of high strength in refractory BCC 
high entropy alloys up to 1900K, Acta Mater 182 (2020) 235 – 249, https://doi.org/ 
10.1016/j.actamat.2019.10.015 . 
[17] E. Menou, I. Toda-Caraballo, P.E.J. Rivera-Díaz-del-Castillo, C. Pineau, E. Bertrand, 
G. Ramstein, F. Tancret, Evolutionary design of strong and stable high entropy 
alloys using multi-objective optimisation based on physical models, statistics and 
thermodynamics, Mater. Des. 143 (2018) 185 – 195, https://doi.org/10.1016/j. 
matdes.2018.01.045 . 
[18] E. Menou, E. Tancret, I. Toda-Caraballo I, G. Ramstein, P. Castany, E. Bertrand, 
N. Gautier, P.E.J. Rivera Díaz-Del-Castillo, Computational design of light and 
strong high entropy alloys (HEA): Obtainment of an extremely high specific solid 
solution hardening, Scr. Mater. 156 (2018) 120 – 123, https://doi.org/10.1016/j. 
scriptamat.2018.07.024 . 
[19] J.M. Rickman, H.M. Chan, M.P. Harmer, J.A. Smeltzer, C.J. Marvel, A. Roy, 
G. Balasubramanian, Materials informatics for the screening of multi-principal 
elements and high-entropy alloys, Nat. Commun. 10 (2019) 2618, https://doi.org/ 
10.1038/s41467-019-10533-1 . 
[20] Y. Rao, C. Baruffi, A.D. Luca, C. Leinenbach, W.A. Curtin, Theory-guided design of 
high-strength, high-melting point, ductile, low-density, single-phase BCC high 
entropy alloys, Acta Mater. 237 (2022) 118132, https://doi.org/10.1016/j. 
actamat.2022.118132 . 
[21] Il.H. Kim, H.S. Oh, K.S. Lee, E.S. Park, Optimization of conflicting properties via 
engineering compositional complexity in refractory high entropy alloys, Scr. 
Mater. 199 (2021) 113839, https://doi.org/10.1016/j.scriptamat.2021.113839 . 
[22] B. Vela, C. Acemi, P. Singh, T. Kirk, W. Trehern, E. Norris, D.D. Johnson, 
I. Karaman, R. Arr ´ oyave, High-throughput exploration of the WMoVTaNbAl 
refractory multi-principal-element alloys under multiple property constraints, Acta 
Mater. 248 (2023) 118784, https://doi.org/10.1016/j.actamat.2023.118784 . 
[23] Y. Tian, R.H. Yuan, D.Z. Xue, Y. Zhou, T. Lookman, Role of uncertainty estimation 
in accelerating materials development via active learning, J. Appl. Phys. 128 
(2020) 014103, https://doi.org/10.1063/5.0012405 . 
[24] C. Wen, Y. Zhang, C. Wang, D. Xue, Y. Bai, S. Antonov, L Dai, T. Lookman, Y. Su, 
Machine learning assisted design of high entropy alloys with desired property, Acta 
Mater. 170 (2019) 109 – 117, https://doi.org/10.1016/j.actamat.2019.03.010 . 
[25] D. Xue, P.V. Balachandran, J. Hogden, J. Theiler, D. Xue, T. Lookman, Accelerated 
search for materials with targeted properties by adaptive design, Nat. Commun. 7 
(2016) 11241, https://doi.org/10.1038/ncomms11241 . 
[26] G. Tzortzis, A. Likas, The MinMax k-Means clustering algorithm, Pattern Recogn. 
47 (2014) 2505 – 2516, https://doi.org/10.1016/j.patcog.2014.01.015 . 
[27] O.A. Waseem, H.J. Ryu, Combinatorial development of the low-density high- 
entropy alloy Al
10
Cr
20
Mo
20
Nb
20
Ti
20
Zr
10 
having gigapascal strength at 1000 ℃ , 
J. Alloys Compd. 845 (2020) 155700 https://doi.org/10.1016/j. 
jallcom.2020.155700 . 
[28] C. Wen, C.X. Wang, Y. Zhang, S. Antonov, D. Xue, T. Lookman, Y. Su, Modeling 
solid solution strengthening in high entropy alloys using machine learning, Acta 
Mater. 212 (2021) 116917, https://doi.org/10.1016/j.actamat.2021.116917 . 
[29] Z.D. Han, N. Chen, S.F. Zhao, L.W. Fan, G.N. Yang, Y. Shao, K.F. Yao, Effect of Ti 
additions on mechanical properties of NbMoTaW and VNbMoTaW refractory high 
entropy alloys, Intermetallics 84 (2017) 153 – 157, https://doi.org/10.1016/j. 
intermet.2017.01.007 . 
[30] O.N. Senkov, S. Gorsse, D.B. Miracle, High temperature strength of refractory 
complex concentrated alloys, Acta Mater. 175 (2019) 394 – 405, https://doi.org/ 
10.1016/j.actamat.2019.06.032 . 
C. Wen et al.
