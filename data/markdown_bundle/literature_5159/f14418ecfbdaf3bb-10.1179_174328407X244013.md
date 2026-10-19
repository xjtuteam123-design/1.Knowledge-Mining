# 10.1179_174328407X244013

<!-- source: D:\总文献\10.1179_174328407X244013.pdf -->
<!-- file_sha256: 3d9492296d3761460d3985467ed6fc2f1ba8143d6134ea17f88b604f417371d6 -->

## Page 1

Adaptive numerical modelling of high
temperature strength, creep and fatigue
behaviour in Ni based superalloys
I. Di Martino 1, J. W. Brooks 1, P. A. S. Reed 2, P. Holdway 1 and A. Wisbey *1
The mechanical behaviour of high performance Ni alloys is required for many applications and
where experimental data is not readily available then a suitable predictive approach would be
beneficial. There are numerous routes to achieve this, however, here the data driven neural
network method has been adopted to produce models for the tensile, creep and fatigue
performance of nickel base alloys. These models have been successfully developed and tested
against a range of criteria. The tensile and creep models have displayed excellent fidelity to
known nickel alloy behaviour, while good correspondence was also achieved for the fatigue
properties (both strain and stress controlled). Potential routes to further improve the performance
of these models have been discussed.
Keywords: Nickel superalloys, Neural network modelling, Creep, Fatigue, Tensile strength
Introduction
The estimation of the mechanical performance of Ni
alloys, based on their composition and manufacturing
process is an attractive capability for a wide range of
activities, including initial component stressing and
liﬁng and alloy development and optimisation. One
potential route to achieve this objective is by the use of
artiﬁcial neural network modelling and this is explored
in this paper. Here ﬁve properties have been modelled –
the yield and ultimate strengths, the creep rupture life
and the stress and strain controlled fatigue lives. A wide
range of Ni alloys have been considered in the present
work to provide the greatest applicability.
Neural network (NN) modelling is a mathematically
based approach for the assessment of complex inter-
relationships within systems, in this case between Ni
alloy composition, manufacturing method, heat treat-
ment, crystallography and the mechanical properties.
For a more detailed study of the use of NN models in
the present context see references.
1–3 Neural network
approaches have been applied to predictions of: wear, 4
property modelling in Al alloys, 5 fatigue lives of com-
posites,6 a range of titanium alloy properties; 7 plastic
deformation behaviour, 8 fatigue9 and strength 10 model-
ling in Ni base alloys. Some authors have emphasised
the importance of model transparency in evaluating such
adaptive numerical modelling approaches. 11 The work
reported here is a further step in the development of
these tools for Ni alloys and although the models are
‘curve ﬁts’ (albeit fairly complex) to existing data, they
offer the possibility of providing an improved under-
standing of the mechanical property data relationships
with features like composition and manufacturing
process.
3 However, there will be limits on the applic-
ability of the models, dependent on the input data and
metallurgical understanding will still be required in their
use.
The present work has used the Neuromat software
developed at Cambridge University. One particular
advantage of this software is the use of Bayesian
statistics to assist in the choice of the most probable
distribution of weights for a given data set. This
software offers the user error bounds on any predictions
made, which give a good indication of the strengths and
weaknesses of any particular model architecture, model
or prediction. Thus the error bounds increase in size
where data is sparse within the original ‘training’ data
set and thus there is greater uncertainty in the ﬁtting of
the data. The NN’s are composed of an interconnected
array of input nodes (the input data, like composition, in
this case), linked by a relational function (a hyperbolic
tangent here) to an output node (our property of
interest). The relational function is known as a ‘hidden
unit’ and the number of these can be varied dependent
on the complexity of the problem to be solved. The
training of the NN essentially gives weights to the input
nodes and biases to the ‘hidden units’, minimising the
error between the actual output values and the predicted
values. Since this is a multi-dimensional minimisation
problem, then multiple starting points for the error
minimisation function are required (known as ‘seeds’) to
reduce the possibility of becoming trapped in false
minima.
Each of the ﬁve NN models developed for the various
properties in the present work were preliminarily tested
1High Temperature Materials and Lifing, QinetiQ, Farnborough, Hants,
GU14 0LX, UK
2Engineering Materials, University of Southampton, Highfield, Southampton,
UK
*Corresponding author, email AWISBEY@qinetiq.com
1402
/C2232007 Institute of Materials, Minerals and Mining
Published by Maney on behalf of the Institute
Received 25 April 2007; accepted 10 July 2007
DOI 10.1179/174328407X244013
Materials Science and Technology 2007 VOL 23 NO 12

## Page 2

and validated against known metallurgical trends and
‘seen’ data, i.e. data present within the databases used
for the training and creation of the neural network itself.
Furthermore, a number of mechanical tests were
undertaken on the French Ni base disc alloy (N18)
and a recently released alloy (Haynes 282). The results of
these tests would provide mechanical properties ‘unseen’
by the models, hence enabling some degree of validation
of the models to be undertaken. The performance of the
models is discussed in the light of these assessments.
Assembly and assessment of data bases
Databases for the ﬁve mechanical properties of Ni alloys
have been developed to provide the neural network
‘training’ information for the predictive models of:
(i) yield strength
(ii) ultimate tensile strength
(iii) creep rupture life
(iv) fatigue life for both strain controlled and stress
controlled.
Each of these databases consists of up to 1500 lines of
data (but falling to ,800 lines for the fatigue databases),
combining both QinetiQ ‘in house’ and publicly avail-
able data on up to 150 different alloy compositions, with
cast (conventional, directional solidiﬁed and single
crystal), wrought and powder metallurgy forms being
represented. The inputs into each of the databases
included: chemical composition (up to 20 elements),
manufacturing process, crystallographic structure, heat
treatment (with three temperature and time steps) and
mechanical test conditions. This has led to up to 30
different input parameters for the fatigue databases,
since these require the most parameters to represent the
test conditions. Studies were then conducted to examine
the feasibility of reducing the number of these input
parameters, since it is known that the accuracy of the
predictions made are related to the number of input
parameters and available dataset size. Thus the possibi-
lity of consolidating the Al and Ti concentrations into a
single c9 strengthening parameter, or using the Smith–
Watson–Topper parameter
12 to eliminate R ratio (mini-
mum strain/maximum strain) for the strain controlled
fatigue has been investigated. Another area for devel-
opment has been the treatment of alloys which utilise
heat treatment sequences with more than three steps, for
example, single crystal Ni alloys, like CMSX4. Thus
diffusional effects were accounted for and related heat
treatments consolidated into a single effective heat
treatment step. Alongside these developments the actual
data inputs were also assessed in an attempt to ensure
accuracy of the input ‘training’ data.
Neural network model development and
performance
Once the databases had been assembled and initial
optimisation had been completed then the ﬁve neural
network models were trained using the Cambridge
University, Neuromat software. The architecture of the
neural network (number of ‘hidden units’ and ‘seeds’)
was determined and trials indicated that a similar
architecture for all ﬁve of the models appeared to give
good results (some of the assessment criteria are shown
below). Once presented with the database for each
mechanical property the Neuromat software then
randomly splits the data in half (in this case) and trains
the neural network on half of the data. This training
creates multiple models (dependent on the number of
‘hidden units’ and ‘seeds’ selected) and these results are
then compared automatically with the remaining half of
the data to generate an indication of the error between
the prediction and actual data. These error results are
then displayed for all of the models to enable the user to
select the models with the lowest error level. A number
of the best models can then be combined into a
‘committee’ to further improve the accuracy of the
prediction and again the error is generated for the
number of models included in the ‘committee’ and thus
permitting the user to select the best performing method.
A key part of the NN model development has been
the identiﬁcation of appropriate assessment criteria to
evaluate the models. Thus the following assessments
have been adopted:
(i) comparison of NN model predictions against
data within the original training database
(known as ‘seen’ data)
(ii) sensitivity of the NN models to changes in the
input parameters to known metallurgical effects,
for example, increasing Ti and Al concentrations
to increase strength, eliminating ageing heat
treatments to lower strengths and increasing test
temperatures. This could often be a qualitative
assessment because of the lack of adequate
validating data, however, this was a valuable
exercise in confirming model performance
against known metallurgical behaviour
(iii) comparison of the NN model predictions to
experimentally determined mechanically proper-
ties not available to the training databases
(known as ‘unseen’ data). This is obviously a
key test of the predictive capacity of the models.
The remainder of the present paper deals with the results
obtained with the above assessments.
Tensile properties
The performance of the yield (YS) and ultimate strength
(UTS) NN models are dealt with together here because
their behaviour was generally linked closely. A wide
range of Ni alloys was selected from the original training
dataset, to represent the various types of alloys (cast,
wrought, powder metallurgy (PM)) and compositional
extremities (e.g. high Fe in Nim 901) available to the NN
model. These were then used to assess the various NN
model’s performance against ‘seen’ data. An example of
this is shown in Fig. 1, for the yield strength of the
PM alloy Merl 76 (Ni–12 ?4Cr–18?6Co–3?3Mo–1?4Nb–
4?3Ti–5?1Al–0?35Hf–0?06Zr–0?02C), where very good
agreement was found. The fairly tight error bounds
predicted by the model should also be noted and such
behaviour is consistent with availability of this data
within the training dataset. Similar behaviour was found
with the UTS NN model, as shown for the Nim 901
alloy in Fig. 2.
A number of sensitivity studies to known metallurgi-
cal phenomena have been undertaken, studying a range
of alloy compositions. Figure 3 shows the predicted
effects of increasing and decreasing the Al and Ti
contents in the cast IN 738 (Ni–16Cr–8 ?5Co–1?75Mo–
2Nb–2?6W–3?4Ti–3?4Al–0?1Zr–0?17C–0?01B) alloy. Thus
an increase in Al and Ti led to a predicted increase in
Di Martino et al. Modelling of high temperature strength, c reep and fatigue behaviour in superalloys
Materials Science and Technology 2007 VOL 23 NO 12 1403

## Page 3

YS, while decreasing the Al and Ti reduced the YS
predicted, consistent with metallurgical expectations. In
a similar manner the heat treatment for a range of alloys
was changed to investigate the NN model predictions
and again these were found to generally agree with the
metallurgical expectations, e.g. solution annealed mate-
rial showed lower strength, than a solution treated and
aged material.
The ﬁnal assessment undertaken here was to compare
the performance of the models against ‘unseen’ data, i.e.
not available within the original training set. Thus in
Fig. 4 the NN YS model predictions for the French
PM N18 alloy (Ni–11 ?1Cr–15?4Co–6?4Mo–4?3Ti–
4?3Al–0?5Hf–0?019Zr–0?022C–0?008B), which was not
available in the training data, may be seen. This shows
excellent agreement between the experimental and
predictions. It should also be noted that while the error
bounds have increased in magnitude compared with
those seen for the ‘seen’ data, they are still relatively
small. These comparisons suggest a good overall
performance for the strength predictions, although there
are some extremes within the data space, where the
predictions were less conﬁdent.
Creep rupture properties
A similar process to that used with the tensile properties
was pursued with the creep rupture performance. Thus
the replication of data within the database, i.e. the ‘seen’
data was assessed initially and the NN model predictions
were found to give very good agreement and examples
are shown in Fig. 5 for the single crystal Ni alloy,
CMSX4 (Ni–6 ?5Cr–9Co–0?6Mo–5?6Al–1?0Ti–6?5Ta–
6W), at 1050 uC and Fig. 6 for the conventionally cast
IN 738 at 850 uC. Following this check of the NN model
performance the sensitivity to known metallurgical
phenomena was then assessed. For the creep properties,
features like increasing rhenium concentration in a cast
1 Neural network prediction of YS of PM Merl 76 alloy
(‘seen’) versus temperature: predicted values are com-
pared with actual test data (dotted lines represent
error bounds associated with predictions)
2 Prediction of UTS for Nim 901 alloy (‘seen’) versus
temperature: predicted values are compared with
experimental data (dotted lines represent error bounds
associated with predictions)
3 Neural network sensitivity to compositional changes
for YS of IN 738 alloy (‘seen’), Al and Ti contents
increased and decreased by 1 wt-%: test data for stan-
dard IN 738 are also shown
4 Neural network prediction of YS of wrought N18 alloy
(‘unseen’) versus temperature, compared with actual
test data (dotted lines represent error bounds asso-
ciated with predictions)
5 Neural network prediction of creep rupture stress
(CRS) for single crystal Ni alloy, CMSX4 (‘seen’) at
1050uC and compared with literature data (dotted lines
represent error bounds associated with prediction)
Di Martino et al. Modelling of high temperature strength, cr eep and fatigue behaviour in superalloys
1404 Materials Science and Technology 2007 VOL 23 NO 12

## Page 4

alloy (Fig. 7) or examining the difference between the
performance of polycrystalline or single crystal forms of
a single alloy composition (where the single crystal
variant can usually have a superior creep rupture
performance, compared with polycrystalline material)
were studied. Again very good agreement was found
between the NN model and metallurgical expectation,
for example, rhenium additions increased creep rupture
life. The ﬁnal assessment was the prediction of ‘unseen’
data and this proved to be difﬁcult to achieve because of
the very large number of alloys within this particular
database, however, the low cost single crystal Ni alloy,
CM186 (Ni–6Cr–9Co–0?5Mo–8Ta–5?7Al–0?7Ti–1?4Hf–
0?07C), was not represented and thus used as part of this
validation exercise (Fig. 8). Excellent correspondence
between the experimental CM186 creep rupture lives
and those predicted by the NN model were found. It is
worth noting the CM186 alloy was reasonably similar in
composition to some of those within the database and
thus the NN model might be expected to give a
reasonable representation of the experimental data.
The creep rupture database was the largest of the ﬁve
assembled and this was reﬂected in its excellent
performance, however, one of the great strengths of this
modelling approach is the relative ease with which
additional data may be added to the training dataset and
new models generated. Further data for this mechanical
property has been recently identiﬁed and it is anticipated
that this will further strengthen the predictive capabil-
ities of this particular model. This also suggests that this
may be a valuable method for storage and archiving of
mechanical test data, in addition to the predictive
capabilities of the models.
Fatigue properties
The fatigue performance of alloys is a signiﬁcantly more
complex property to characterise than the creep above,
however, initial developments of two databases and
models have been undertaken, for both the strain and
stress controlled fatigue properties. The strain controlled
properties are of great interest for the liﬁng of com-
ponents like turbine discs, while for sheet structures the
stress controlled properties are more often used. In
contrast to the creep properties the databases assembled
for the fatigue were the smallest of those reported here,
at ,800 lines of data in each. This is partly a reﬂection
on the smaller number of studies on fatigue, compared
with creep but also the commercial value of such
information and hence a lack of published data.
A major difference between the strain and stress
controlled databases is that the strain controlled is
mostly populated by low frequency, low cycle data,
while the stress controlled database is much more mixed
with high frequency ( ,100 Hz) data, along side much
lower frequencies (e.g. 0 ?25 Hz) and both high and low
cycle data. Thus in many ways the strain controlled data
was simpler to characterise by the NN model than the
stress controlled conditions.
Despite the size of the databases reasonable agree-
ment was achieved for the ‘seen’ data, as shown in Fig. 9
for the single crystal Ni alloy, CMSX4 within the strain
controlled fatigue model. Figure 10 also illustrates
this latter point, but with the stress controlled data.
However, Fig. 10 also serves to highlight the problem of
dealing with the inherent scatter in fatigue data and
often the relatively small datasets available for some
alloys. Given these problems, it is perhaps surprising
that the NN model has produced such a good ﬁt to the
actual data. One aspect of note, especially relevant to
the stress controlled model was that it has captured the
higher stress portion of the S–N curve well but the ‘run
out’ behaviour has not been predicted, even for the
‘seen’ data. This is somewhat disappointing, however, an
approach to improve this has been considered and may
6 Neural network prediction for CRS for conventionally
cast IN 738 alloy (‘seen’), tested at 850 uCa n dc o m -
pared with experimental data (dotted lines represent
error bounds associated with predictions)
7 Neural network sensitivity to compositional changes
for single crystal alloy, CMSX4 (‘seen’) at 950 uC: stan-
dard CMSX4 contains ,2?6 wt-%Re and this was
increased to 6 wt-% in model
8 Neural network prediction for CRS of single crystal
alloy, CM186 (‘unseen’) at 950 uC and compared with
experimental data (dotted lines represent error bounds
associated with predictions)
Di Martino et al. Modelling of high temperature strength, c reep and fatigue behaviour in superalloys
Materials Science and Technology 2007 VOL 23 NO 12 1405

## Page 5

be implemented in later versions of this model. This
would have the added beneﬁt of adding extra data to the
training database.
Sensitivity studies for the prediction of metallurgical
phenomena were again undertaken, but here took the
form of evaluating the effect of changing the test
temperature, R ratios and heat treatment practices.
These were generally predicted very well by both the
strain and stress controlled fatigue models. As with the
previous models, the ﬁnal tests have been in relation to
‘unseen’ data and here the models performed surpris-
ingly well, given the size of the databases available for
the model training. Figure 11 shows the prediction of
stress controlled fatigue performance for the recently
developed Haynes 282 alloy (Ni–19 ?5Cr–10Co–8?5Mo–
2?1Ti–1?5Al–1?5Fe–0?06C–0?005B) at room tempera-
ture, along with experimental data. The good general
agreement is clear, although the lack of ‘run out’ type
behaviour in the NN model is again noticeable. This was
felt to be a good test of the NN model because, not only
was the composition not in the database, but room
temperature test data was also not particularly well
represented either. The associated error bounds for the
Haynes 282 model predictions reﬂect the uncertainties
that the lack of composition and test temperature cause
the model. It is worth also noting that in addition to this
testing against the Haynes 282 alloy, both fatigue
models were also tested against the French disc alloy,
known as N18 (Ni–11 ?1Cr–15?4Co–6?4Mo–4?3Ti–
4?3Al–0?5Hf–0?019Zr–0?022C–0?008B) at 650 uCa n d
here reasonable correspondence was again achieved.
13
Some work was undertaken with the strain controlled
fatigue model to enhance it’s predictive capability by
using the Smith–Watson–Topper parameter 4 to reduce
the number of input variables. However, testing of this
approach showed poorer performance than the models
shown here, which used the full input range. Thus this
approach was abandoned. Further improvements with
these fatigue models will be possible and at present
increased training database sizes appears to be the most
powerful route to achieve this. In particular signiﬁcant
development of the strain controlled fatigue model
should be possible with this route.
Summary and conclusions
Models to predict ﬁve mechanical properties (tensile,
creep and fatigue) of Ni base alloys have been developed
and demonstrated. These models are based on the data
driven neural network approach and the models for the
tensile and creep behaviour have proved to be very
powerful in predicting these properties of Ni base alloys.
The fatigue models (both strain and stress controlled)
are at a slightly earlier stage of development but are
starting to produce encouraging results. The models
developed here will have many applications, including
initial component stressing and liﬁng determinations,
alloy development, and input data generation for ﬁnite
element packages. The good performance of the models
on known data highlights the potential of the method
for data capture and archiving.
Acknowledgement
The authors would like to thank the UK Ministry of
Defence (MOD) for their financial support of this work.
References
1. D. J. C. MacKay: Math. Model. Weld Phenom ., 1997, (3), 359–389.
2. D. J. C. MacKay: Neur. Comput ., 1992, 4, (3), 415–447.
3. H. K. D. H. Bhadeshia: ISIJ Int ., 1999, 39, 966–979.
4. L. J. Xu, J. D. Xing, S. Z. Wei, Y. Z. Zhang and R. Long: Mater.
Sci. Technol ., 2007, 23, (3), 315–319.
9 Neural network prediction and experimental data for
strain controlled fatigue performance of single crystal
Ni alloy CMSX4 at 550 uC, and R50?5 (dotted lines
represent error bounds associated with predictions; Nf
5 cycles to failure)
10 Neural network prediction and experimental data for
stress controlled fatigue performance of experimental
cast alloy NASAIR at 870 uC (dotted lines represent
error bounds associated with prediction; Nf 5 cycles
to failure)
11 Neural network prediction and experimental data of
stress controlled fatigue behaviour of Haynes 282
sheet (fully heat treated) at room temperature, R50
(Nf 5 cycles to failure)
Di Martino et al. Modelling of high temperature strength, cr eep and fatigue behaviour in superalloys
1406 Materials Science and Technology 2007 VOL 23 NO 12

## Page 6

5. M. J. Starink, I. Sinclair, P. A. S. Reed and P. J. Gregson: Mater.
Sci. Forum , 2000, 331–337, 97–110.
6. A. Bezazi, S. G. Pierce, K. Worden and E. H. Harkati: Int. J.
Fatig., 2007, 29, (4), 738–747.
7. S. Malinov and W. Sha: Mater. Sci. Eng. A , 2004, A365, (1–2),
202–211.
8. Y. Huang and P. L. Blackwell: Mater. Sci. Technol ., 2002, 18, (10),
1104–1108.
9. J. M. Schooling, M. Brown, P. A. S. Reed: Mater. Sci. Eng. A ,
1999, A260, (1–2), 222–239.
10. F. Tancret, H. K. D. H. Bhadeshia and D. J. MacKay: ISIJ Int .,
1999, 39, (10), 1020–1026.
11. O. P. Femminella, M. J. Starink, M. Brown, I. Sinclair, C. J.
Harris and P. A. S. Reed: ISIJ Int ., 1999, 39, (10), 1027–
1037.
12. K. N. Smith, P. Watson, T. H. Topper: J. Mater., 1970, 5, (4), 767–
778.
13. I. Di Martino, J. W. Brooks, P. A. Reed, A. Wisbey: Proc. Conf.
Parsons 2007, Glasgow, UK, September 2007, Institute of
Materials, Minerals and Mining.
Di Martino et al. Modelling of high temperature strength, c reep and fatigue behaviour in superalloys
Materials Science and Technology 2007 VOL 23 NO 12 1407
