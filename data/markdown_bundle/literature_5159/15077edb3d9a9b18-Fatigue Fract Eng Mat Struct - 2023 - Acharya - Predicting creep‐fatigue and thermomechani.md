# Fatigue Fract Eng Mat Struct - 2023 - Acharya - Predicting creep‐fatigue and thermomechanical fatigue life of Ni‐base

<!-- source: D:\总文献\Fatigue Fract Eng Mat Struct - 2023 - Acharya - Predicting creep‐fatigue and thermomechanical fatigue life of Ni‐base.pdf -->
<!-- file_sha256: 25f58e03f7adf462983f5f5827726f97999866e1a4ba353d12877526df159dd0 -->

## Page 1

ORIGINAL ARTICLE
Predicting creep-fatigue and thermomechanical fatigue life
of Ni-base superalloys using a probabilistic physics-guided
neural network
Rohan Acharya 1 | Alexander N. Caputo 2 | Richard W. Neu 1,2
1Woodruff School of Mechanical
Engineering, Georgia Institute of
Technology, Atlanta, Georgia, USA
2School of Materials Science and
Engineering, Georgia Institute of
Technology, Atlanta, Georgia, USA
Correspondence
Richard W. Neu, Woodruff School of
Mechanical Engineering, Georgia Institute
of Technology, Atlanta, GA, USA.
Email:
rick.neu@gatech.edu
Abstract
Predicting the life of thermomechanical fatigue (TMF) is challenging because
there are several parameters describing the mechanical and thermal cycles
including dwell periods within the cycle that can impact life. The relationships
between these TMF history parameters and fatigue life are not always clear.
This paper explores the use of a neural network (NN) with a probabilistic
physics-guided architecture to learn these relationships and predict the cycles
to failure for a wide range of possible creep-fatigue and thermomechanical
fatigue histories. Using inputs of strain range, maximum and minimum tem-
perature, the phasing between the thermal and mechanical cycles, cycling fre-
quency, and dwell time in either tension or compression, the model predicts
both the mean fatigue life and its confidence intervals (CI). The model is dem-
onstrated from a comprehensive set of data on single-crystal and directionally
solidified Ni-base superalloys extracted from the literature. The model is evalu-
ated in several ways to determine the success of learning the relationship
between the applied TMF histories and cycles to failure.
KEYWORDS
creep-fatigue, fatigue life prediction, neural network, Ni-base superalloys, thermomechanical
fatigue
1 | INTRODUCTION
Single-crystal (SX) and directionally solidified (DS) Ni-
base superalloys are typically used as the primary struc-
tural material for blades and vanes in the hot section of
gas turbine systems. They are subject to TMF involving
dwell periods at high temperature, also called hold times,
during the operation of these systems. Determining the
life of these components operating in this extreme envi-
ronment is challenging due to the multiple parameters
needed to describe the TMF histories that can influence
life. Some of the primary parameters representing the
TMF histories include the strain range, the maximum
and minimum temperatures of the thermal cycle, the rate
of loading and time of the dwells, whether the dwells
occur when the material is in tension or compression, the
difference in phase between the thermal and mechanical
cycles, and the crystal orientation. The crystal orientation
is particularly important in Ni-base superalloys because
the elastic properties at the crystal level and entire speci-
men for SX alloys are highly anisotropic varying by more
than a factor of two from the least stiff <001> and most
stiff <111> orientations.
Forming a model to learn the relationships and to
predict when failure will occur, particularly for multitude
of TMF loading cases where experimental data does not
exist, is valuable for both designers and condition-based
health monitoring. Such a model also provides an
Received: 6 October 2022 Revised: 22 December 2022 Accepted: 5 January 2023
DOI: 10.1111/ffe.13948
1554 © 2023 John Wiley & Sons Ltd. Fatigue Fract Eng Mater Struct. 2023;46:1554–1571.wileyonlinelibrary.com/journal/ffe

## Page 2

expanded understanding of the relationships that differ-
ent TMF loading histories have on fatigue life. In addi-
tion, the model should properly account for runouts; that
is, fatigue tests stopped before failure occurs, which
requires a statistical modeling approach to deal with this
right-censored data.
Machine learning (ML) models in fatigue and fracture
are a growing area of research to model and predict
fatigue life, fatigue crack growth, fatigue strength, and
current fatigue damage state.
1 Of these, only a few have
explored the complex creep-fatigue and TMF behavior of
materials. Venkatesh and Rack
2 showed that NN can
potentially better predict creep-fatigue data than conven-
tional parametric equations including modified Coffin –
Manson, linear life fraction, and hysteresis energy
methods typically used to correlate data. Zhang et al.
3
studied the predictive power of various ML models
including support vector regression, Gaussian process
regression, and NN to predict fatigue failure of high tem-
perature structures subject to creep, fatigue, and creep-
fatigue conditions. They used a dataset of 316 austenitic
stainless steel gathered from multiple sources in the open
literature. The dataset included the influence of strain
range, temperature, hold time, and composition, evaluat-
ing various ML models, though did not show the pre-
dicted creep-rupture and strain-life curves to evaluate
whether the trends predicted are physically consistent
and robust. Chen et al.
4 explored the use of NNs in tur-
bine engines of commercial aircrafts to predict TMF dam-
age accumulation under various operating conditions
training using data generated from NASA's aircraft gas
turbine engine simulator. Schooling et al.
5 explored the
prediction of fatigue thresholds of Ni-based superalloys
with the use of a NN using elements of fuzzy logic to
guide the training of the NN. Recently, Chen and Liu
6
proposed a new NN architecture to predict stress-life
curves. The novelty of their work is incorporating prede-
fined constraints based on the current knowledge of the
physics of fatigue to guide training. The physics-guided
constraints are applied during training to force the NN to
adhere to known physics-informed trends, such as the
flattening of slope of a stress-life curve as the stress
decreases. This helps the model conform to known phys-
ics and be robust as opposed to letting the NN depend
solely on the statistical relations it learns solely from the
data. In addition, the uncertainty quantification of the
predicted fatigue life, which is critical to know for risk
analysis and management, is also an output of the Chen
and Liu NN architecture. The uncertainty quantification
also provides a natural method to include runout data in
the training through the loss function. Together, the new
NN architecture is coined by Chen and Liu
6 as a probabi-
listic physics-guided neural network (PPgNN). They
demonstrated the PPgNN using stress range and mean
stress as inputs on various isothermal HCF datasets
involving metals, alloys, and composites. Expanding on
this work, the PPgNN was used to predict the tempera-
ture dependence on the strain-life curves of wrought Ti-
6Al-4V
7 and used to predict the stress-life of an additively
manufactured Ti-6Al-4V, where in addition to stress
range and mean stress, various process parameters were
used as input to predict how the stress-life curve will
change with processing parameters.
8
In this paper, a new NN-based model is developed for
TMF and creep-fatigue life prediction using several ele-
ments of the architecture of PPgNN employed by Chen
and Liu.
6 This new PPgNN model is demonstrated by
training it using a comprehensive database of TMF and
creep-fatigue data on SX and DS Ni-base superalloys
extracted from the open literature. To limit the scope and
verify that such an approach can be used, the data are
limited to SX alloys loaded in <001> and DS alloys
loaded parallel to the grain growth direction, which is
also nominally oriented as <001>.
2 | METHODS
2.1 | Extracting data from literature
The open literature was searched for fatigue data on SX
and DS Ni-base superalloys used in rotating components
of gas turbine systems. Instead of gathering data for just
one alloy (composition), which likely would not have
provided sufficient data to train a NN for a wide range of
test TMF histories, fatigue data from similar classes of
superalloys were acquired. All data included in the data-
base were cast and heat treated using a typical treatment,
solution treated and age hardened, though the specific
temperatures and times of these heat treatment steps var-
ied. All these superalloys are typically γ
0 strengthened,
containing from 50 to 70% γ0. The data acquired included
the cycles to failure ( Nf ), strain range ( εr ), dwell time in
minutes, when the dwell occurs (tension [T] or compres-
sion [C]), maximum and minimum temperatures in
/C14 C,
cyclic frequency, and test type. The test type was classi-
fied into isothermal fatigue (IF) and thermomechanical
fatigue (TMF). TMF tests were further classified by cycle
type being either linear out-of-phase (OP) or linear in-
phase (IP) describing whether the thermal and mechani-
cal cycles are IP or OP with each other. A summary of
the references used to build the database is given in
Table
1. The total number of test data extracted and
included in the database was 451.
To collect information to train a model with, plots
and tables from literature were datamined. The
ACHARYA ET AL . 1555
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 3

information was stored into an .xlsx file and parsed to
only included data of SX superalloys axially loaded in a
cubic direction, that is, <001>, and DS superalloys
loaded in the longitudinal direction, that is, the grain
growth direction.
2.2 | Framework of the probabilistic
physics-guided neural network
There are multiple NN architectures that have different
purposes and varying results. In this work, the basic
TABLE 1 Summary of data collected from open literature
Reference Material SX or DS Test type Dwell type
Estrada Rodas, Gorgannejad, Neu 9 CMSX-8 SX IF None, T, C
Amaro, Antolovich, Neu 10 PWA1484 SX TMF None, C
Segersäll, Leidermark, Moverare 11 STAL-15 SX TMF C
Segersäll, Deng12 STAL-15 SX TMF T
Lafata, Rettberg, He, Pollock 13 René N5 SX IF C
Hong, Choi, Kim, Yoo, Jo 14 CMSX-4 SX IF T&C
Hong, Kang, Choi, Kim, Yoo, Jo 15 CSMX-4 SX TMF None
Hong, Yoon, Choi, Kim, Yoo, Jo 16 CSMX-4 SX TMF None
Egly, Lang, Löhe 17 CSMX-4 SX TMF T
Moverare, Johansson, Reed 18 CMSX-4 SX TMF C
Ott, Mughrabi19 CMSX-4, CSMX-6 SX IF None
Okazaki, Take, Kakehi, Yamazaki, Sakane,
Arai, et al 20
CMSX-4
CM247LC
SX
DS
IF, TMF
IF, TMF
None, C
None, C
Wahl, Harris
21 CMSX-4 PLUS SX IF None
Yandt, Wu, Tsuno, Sato 22 LSC-11, CSMX-4 SX IF None, C
Okazaki, Sakaguchi23 CMSX-2, CSMX-4 SX IF, TMF None
Wahl, Harris24 CMSX-7, CMSX-8 SX IF None
Reed, Moverare, Sato, Karlsson, Hasselqvist 25 STAL-15 SX TMF C
Sato, Moverare, Hasselqvist, Reed 26 STAL-15 SX TMF C
Segersäll, Kontis, Pedrazzini, Bagot, Moody,
Moverare, et al 27
STAL-15,
STAL-15-Si,
STAL-15-Re
SX TMF C
Moverare, Johansson
28 SCA425Hf SX TMF C
Gabb, Gayda, Miner 29 René N4 SX IF None
Yu, Sun, Jin, Zhao, Guan, Hu 30 SRR99 SX IF None
Han, Yu, Sun, Hu 31 SRR99 SX TMF None
Fleury, Rémy32 AM1 SX IF None
Estrada Rodas33 CMSX-8 SX TMF None
Shenoy, Gordon, McDowell, Neu 34 GTD-111 DS IF None, T, C
Gordon35 GTD-111 DS IF None, T, C
Engler-Pinto, Jr., Noseda, Nazmy, Fezai-Aria 36 CM247LC DS TMF None
Kirka37 CM247LC DS IF, TMF None, T, C
Kirka, Brindley, Neu, Antolovich, Shinde, Gravett 38 CM247LC DS IF, TMF None, T, C
Guth, Petr/C19aˇs, ˇSkorík, Kruml, Man, Lang, et al 39 CM247LC DS TMF None, T, C
Okazaki, Tabata, Nohmi 40 René 80H, CM247LC DS IF None
Rai, Sahu, Das, Paulose, Fernando 41 CM247LC DS IF None, T
Moore, Neu42 CM247LC DS IF None, C
1556 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 4

architecture of the probabilistic physics-guided neural
network (PPgNN) proposed by Chen and Liu 6 is adopted
and modified by adding several new inputs relevant to
creep-fatigue and TMF. The outputs of the PPgNN are
the mean life ( μ) and standard deviation in life ( σ), which
has the importance of providing a predicted confidence
interval.
The PPgNN model created, shown in Figure 1, has
one input layer, one hidden layer, and two output layers.
The connections between neurons from one layer to
another are dictated by the physics-guided constraints
that need to be applied to the model. As discussed in
more detail later, two constraints are applied to the
strain range, fatigue life, and standard deviation. To
apply these constraints, the input neuron for strain
range must be connected to separate neurons in the
hidden layer so that the appropriate weight and bias
constraints can be applied just to those neurons in the
hidden layer. The number of neurons selected to be in
the hidden layer was the minimum needed to obtain
reasonable predictions, noting that training time
increased with the addition of neurons in the
hidden layer without discernable improvement in the
predictions.
The data in the input layer is organized into three
types of inputs: TMF history parameters, cycles to failure,
and runout index. There are seven input variables that
define the TMF history: strain range ( ε
r ), maximum tem-
perature ( Tmax )i n /C14 C, minimum temperature ( Tmin)
in /C14 C, cyclic frequency in Hz, an alternative form of the
temperature-strain phase factor ( TSPFalt ), time of dwell
in compression (Dwell Comp.) in minutes, and time of
dwell in tension (Dwell Ten.) in minutes. The TSPFalt is
defined as
TSPFalt ¼ Tmax /C0 TminðÞ
Scaling Factor /C3 TSPF ð1Þ
with the scaling factor being set to 500 /C14 C and TSPF is
defined as
TSPF ¼ 0 for IF TSPF ¼ 1 for IP TMF TSPF
¼/C0 1 for OP TMF ð2Þ
Therefore, TSPFalt of 0 signifies isothermal fatigue (IF), a
value less than 0 signifies OP TMF, and a value greater
than 0 signifies IP TMF, and the magnitude of TSPFalt
indicates the severity of the thermal cycle, which is not
captured in the basic definition of TSPF. The scaling fac-
tor was set arbitrarily to 500 /C14 C, which is representative of
an intermediate temperature range typically prescribed
in TMF tests of this class of superalloys. Consequently,
prescribed temperature ranges greater than 500 /C14 C will
have a TSPFalt magnitude greater than unity, and tem-
perature ranges smaller than 500 /C14 C will have a TSPFalt
magnitude less than unity.
Cyclic frequency inputs were scaled logarithmically
(base 10) to allow for the NN to train better since these
inputs can vary by several orders of magnitude. Cycles to
failure, N, was similarly scaled logarithmically (base 10)
to give a similar importance to both shorter and longer
fatigue lives. Consequently, the values of the first output
layer, the mean fatigue life, μ, and standard deviation of
fatigue life, σ, are scaled with log NðÞ and need to be
FIGURE 1 Architecture of the PPgNN for prediction of strain-life curves with confidence intervals for TMF histories [Colour figure can
be viewed at wileyonlinelibrary.com]
ACHARYA ET AL . 1557
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 5

converted back to obtain actual predicted life and stan-
dard deviation in terms of number of cycles. All inputs
were normalized using
bX
i ¼ Xi /C0 min ðÞ
max ðÞ /C0 min ðÞ ð3Þ
where bXi represents the normalized value and  repre-
sents all values in each data category. This allows for the
ML model to train better with no parameter having a
larger impact on the output than another and allows for
the NN to disregard the possibility of negative values
which may violate the physics-based constraints. The
parameter, strain range, ε
r , is connected to different neu-
rons in the hidden layer than the remaining TMF param-
eters, which have no constraints on them, to simplify the
derivation of the expressions for the physics-guided
constraints.
6
The hidden layer of the NN is used to introduce the
nonlinearity through activation functions that gives NNs
their robustness in regression. The mathematical expres-
sion for each NN neuron is given by
z
lðÞ
k ¼ b l/C0 1ðÞ
k þ
Xpl/C0 1
j¼1 w l/C0 1ðÞ
kj a l/C0 1ðÞ
j l ¼ 1, 2…, L ð4Þ
where z lðÞ
k is the neuron output which depends on
the outputs of neurons from previous layers a l/C0 1ðÞ
j , modi-
fied by a weight, w l/C0 1ðÞ
kj , and bias, b l/C0 1ðÞ
k , obtained by the
NN training process, where k is a specified neuron in the
layer, j is a neuron from the previous layer, and pl is the
number of neurons in the lth layer. Here, l is the layer of
the NN with l ¼ 1 being an input layer, l ¼ L being the
output layer, and all layers between being hidden layers.
An activation function, defined generically as
a
lðÞ
k ¼ g lðÞ
k z lðÞ
k
/C16/C17
k ¼ 1, 2…, pl, ð5Þ
scales the output of the neurons in the previous layer,
z lðÞ
k . The activation functions, g lðÞ
k z lðÞ
k
/C16/C17
, controls the scal-
ing of the output of each neuron.
The model uses multiple activation functions in its
hidden and output layer. The first hidden layer is filled
with neurons that use the activation function a
lðÞ
k ¼
g lðÞ
k z lðÞ
k
/C16/C17
where g lðÞ
k z lðÞ
k
/C16/C17
is tanh(x), which uses the
equation
g zðÞ ¼ ez /C0 e/C0 z
ez þ e/C0 z ð6Þ
The tanh is a popular activation function to introduce
nonlinearity and was shown to work well in the PPgNN
architecture.6 For the first output layer, the mean life is
calculated using a linear activation function,
gzðÞ ¼ z: ð7Þ
Output neurons for this NN are left linear to allow for
the model to produce an unbounded output which is
desired for most regression problems. 6
Neurons from the first hidden layer are also used to
predict the standard deviation, which is calculated with
an elu + 1 activation function defined as
gzðÞ ¼ ez, z <0
z þ 1, z ≥ 0
/C26
ð8Þ
Here, elu stands for exponential linear unit defined by
gzðÞ ¼ ez /C0 1, z <0
z, z ≥ 0
/C26
ð9Þ
The elu + 1 activation function in Equation ( 8)i sa
modification of elu, Equation ( 9), by adding one to the
output necessary to constrain the standard deviation to
be positive as required by definition. Finally, the two
neurons in the first output layer are used to predict a
new modified mean log(N) value, μ
r , which is adjusted
with the standard deviation to relax the curvature con-
straint which cannot go zero and hence is somewhat over
restrictive. The desired curvature should approach zero at
very long lives. By not employing the constraint on this
last output layer, the curvature can relax during training
to better represent a strain-life curve approaching a
fatigue limit at very long lives.
6 The final outputs are the
modified mean log NðÞ , μr , and standard deviation of
log NðÞ , σ.
The NN uses a custom loss function and an optimizer
to update the weights and biases in each neuron during
the training process. The loss function measures the per-
formance of the model. The custom loss function is
defined as
6
L ¼/C0
Xn
i¼1 δi log f log NiÞjμi,σiðÞð½/C138f
þ 1 /C0 δiðÞ log 1 /C0 F log NiðÞ j μi,σiðÞ½/C138 g
ð10Þ
where n is the number of data points in the set of data.
The runout index, δi, is left as a categorical variable with
0 signifying a runout test and a 1 signifying a test that
resulted in specimen failure, with the subscript i repre-
senting the index for each test data. The loss function
assumes a normal distribution to calculate the likelihood
that failure will occur at the predicted number of cycles.
The probability density function is used to calculate
1558 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 6

likelihood that the predicted life matches the observed
value in the case of a failure, represented by the first term
of Equation (
10). However, in the case of a runout, the
loss function calculates the likelihood that the predicted
life is larger than the observed life, represented by the
second term of Equation (
10). The custom loss function
accounts for runout by using the runout index so that the
equation calculates the log of the probability distribution
function, f log N
iÞjμi, σiðÞð , if the specimen failed or calcu-
lates the log of the cumulative distribution function,
F log NiðÞ j μi, σiðÞ , if the specimen was a runout. The
results are made positive so that a lower likelihood
results in a larger loss. Assuming a normal distribution,
the likelihood will increase as the predicted life
approaches the observed value and thus decrease the
loss.
6
The optimizer uses the loss function to adjust all the
weights and biases. Here, the Adam optimizer algorithm
was used.
43 Hyperparameters, that is, the parameters that
control the learning process of a ML model, can be
adjusted to impact the training and the predictions of the
trained model. The three primary hyperparameters for
training the NN are the number of epochs, the batch size,
and learning rate. One epoch occurs when the NN has
passed through the dataset once and the batch size deter-
mines the number of samples that is passed through the
NN before the neurons' weights and biases are updated.
The NN will train each set of data, also called batch, until
it passes through the whole dataset therefore completing
one epoch. The learning rate affects how much the opti-
mizer will change the weights and biases each time they
are updated.
All code including data processing, NN building, and
model testing was conducted using TensorFlow 2.1.0,
Scikit-learn 1.0.2, and TensorFlow-Probability 0.8.0 in
Python 3.7.13 with Anaconda version 2.2.0 as an environ-
ment and IDE manager. TensorFlow's package was used
to import Keras's backend functions and construct the
NN model. Scikit-learn was used to scale the data.
TensorFlow-probability was used to normalize the mean
life and standard deviation and to calculate loss.
Prior to training the PPgNN, the physics-guided con-
straints are implemented by constraining the weight and
biases of certain neurons to match known experimental
trends observed in strain-life curves. Table
2 shows the
two physics-guided relationships that were used to set
constraints on εr , μ, and σ. The constraint that ∂2 μ
∂εr 2 ≥ 0
enforces that slope of the strain-life curve decreases as
the strain range decreases. The
∂σ
∂εr
≤ 0 constraint forces
the standard deviation to increase as the strain range
decreases replicating the heteroscedastic nature of fatigue
life data. The expressions for these depend on the NN
architecture and the mathematical expressions for the
neurons. Details of the derivation of these expressions are
given in Chen and Liu.
6
The model training is guided by setting three training
hyperparameters: batch size, learning rate, and epochs.
The batch size of the PPgNN is set to one to simulate a
stochastic gradient decent by updating the model's
parameters after each test data point.
44 The NN uses the
Adam optimizer with a default learning rate of 0.001,
which is recommended when the batch size is small.
There is no clear rule to determine the number of
epochs a NN should train so to determine how the model
was training, it was initially trained with 350 epochs. The
loss of the model calculated with Equation ( 10) was
tracked at every epoch and graphed to show how quickly
the model can minimize loss relative to the training data-
set. As seen in Figure
2, the model's loss continues to
decrease with epochs but has very little change after
200 epochs. To prevent possible overfitting, early stop-
ping was applied, and the model was trained for
TABLE 2 Constraints on the weights and biases corresponding
to physics knowledge
Physics
knowledge
Weight
constraints
Bias
constraints
∂2 μ
∂εr 2 ≥ 0 w 1ðÞ
j1 ≥ 0, w 2ðÞ
1j ≤ 0
or
w
1ðÞ
j1 ≤ 0, w 2ðÞ
1j ≥ 0
b 1ðÞ
j ≥ 0
or
b
1ðÞ
j ≤ 0
∂σ
∂εr
≤ 0 w 1ðÞ
j1 ≥ 0, w 2ðÞ
2j ≤ 0
or
w
1ðÞ
j1 ≤ 0, w 2ðÞ
2j ≥ 0
None
FIGURE 2 Plot depicting the calculated loss as a function of
training time (epochs) for the PPgNN [Colour figure can be viewed
at wileyonlinelibrary.com]
ACHARYA ET AL . 1559
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 7

120 epochs for every subsequent test. The model took a
little over a second to train one epoch and about 3 min to
train fully using the whole dataset on an computer with
Windows and an Intel(R) Core (TM) i7-4770K CPU @
3.50GHz processor. No attempts were made to further
tune these hyperparameters since training time was not a
critical issue in this study.
Different initial biases and weights will result in dif-
ferent outputs of a NN thus introducing an element of
randomness. For this model, biases and weights are ran-
domly initiated to improve the performance and effi-
ciency of the NN model and to allow for further analysis
of resulting confidence intervals and strain-life curves.
45
All data were used when training the model to learn the
relationships between the parameters except for when
the model was evaluated with metrics in goodness of fit
and cross validation. The model trained with all data
gives the best-case outputs for life and the goodness of fit
and cross validation tests help to determine if the model
is robust and predicting life within a factor of 3. For some
sets of input conditions, the model was trained and made
to predict multiple times. This was done by first creating
a different set of randomly initialized weights and biases.
The model is then trained with the same hyperpara-
meters. Finally, the trained model was tasked to make
predictions before looping through the process again.
This was repeated 10 times to determine the sensitivity of
the initial weights and biases on the predictions.
To generate the strain-life plots, the predicted mean
life, μ, from the trained model is evaluated at multiple
strain ranges to create a smooth curve. In addition, the
95% confidence interval curves are created using the out-
put standard deviation at each strain range using
Confidence Interval ¼ μ /C6 1:96 /C3 σ ð11Þ
The metric used to test the model is the mean square
error (MSE),
MSE ¼
1
n
Xn
i¼1 yp /C0 yo
/C16/C17 2
ð12Þ
where yp ¼ log10 predicted valueðÞ and
yo ¼ log10 measured valueðÞ . The MSE is used to evaluate
goodness of fit plots and for cross validation.
3 | RESULTS AND DISCUSSION
3.1 | Strain-life curves
Several examples of strain-life curves with the 95% confi-
dence intervals (CI) generated using trained NN model
are shown in Figures 3–7. To observe how well the pre-
dicted strain-life curves relate to the experiments, experi-
mental data with similar test conditions are also shown
on these plots. Since there are few experimental data that
have the exact test conditions as the fixed TMF history
used for each prediction, the plot includes experimental
data that are close to the same TMF history parameters.
The criteria for determining which data to included is
given in Table
3. All parameters except for dwell time are
given a range of values centered around the prescribed
value. Dwells are split into six categories, three involving
tension dwells and three compression dwells. Within
each sign of dwell, there are three categories: (i) no dwell
which includes cycles where the dwell is 1 s or less,
(ii) short dwells, less than or equal to 5 min, and
(iii) long dwells, greater than 5 min. The input for these
dwells for purposes for prediction are (i) 0 min,
(ii) 5 min, and (iii) 20 min, respectively. For TMF, the
minimum temperature has less of an influence than max-
imum temperature, and there are less data exploring the
influence. Hence, to plot sufficient TMF data, the crite-
rion for selecting the minimum temperature is wider
than maximum temperature.
Figure
3 shows the predicted strain-life curve for iso-
thermal fatigue at 900 /C14 C and frequency of 0.033 Hz for
which a considerable amount of experimental data is
available. The experimental data cover a wide span of
strain ranges from 0.4% to 2.4% to illustrate how the pre-
diction curves represent the mean and 95% CI of the data.
Figure
4 shows the strain-life curves for isothermal
fatigue at 600 /C14 C and 1000 /C14 C at a higher cyclic frequency
FIGURE 3 Predicted strain-life curve for isothermal fatigue at
900/C14 C and frequency 0.033 Hz [Colour figure can be viewed at
wileyonlinelibrary.com]
1560 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 8

of 0.33 Hz. The impact of not including the runout data
in the training is illustrated in Figure 4C,D, which can be
compared directly to Figure 4A,B, respectively. Clearly,
not including the runout data results in the mean life
curve being shifted to lower lives (i.e., more conservative
predictions) and the span of the 95% CI is much reduced
at the lower strain range, high fatigue life conditions.
Even when the runout data is included in the training,
the model still tends to provide a conservative prediction
for the runout data. This suggests that including addi-
tional runout data, which tends to be sparse in strain-life
datasets, will improve the predictions particularly at the
lower strain ranges.
Considering that the experimental data are extracted
from multiple sources and different alloys, most of the
data are within the 95% CI of the mean life curves when
the runout data are included. The data are trained on
the complete dataset; therefore, when parsing out and
probing a specific test condition, the experimental data
shown may not necessarily go through the mean life
curve, such as shown in Figure
3, if a regression analysis
was isolated to the smaller dataset of just the data
shown in this plot. Instead, the mean and 95% CI pre-
dictions of strain-life are dependent on the entire data-
set, providing considerably greater robustness to the
predictions. The span of the CI increases with decreas-
ing strain range as required by the constraints included
in the training.
Figure
5 shows strain-life predictions for out-of-phase
TMF with Tmax = 1000/C14 C considering the influence of
FIGURE 4 Predicted strain-life curves for isothermal fatigue at cyclic frequency of 0.33 Hz showing (A) 600 /C14 C trained using all
experimental data, (B) 1000 /C14 C trained using all experimental data, (C) 600 /C14 C trained with runout data removed, and (D) 1000 /C14 C trained
with runout data removed [Colour figure can be viewed at wileyonlinelibrary.com]
ACHARYA ET AL . 1561
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 9

compressive dwells occurring during the hot part of the
cycle. The plots (B) and (C) in this figure also show how
little the impact dwell compression greater than 5 min
has on life. The data points in plot (C) were taken from
the same paper that used a different material compared
with plots (A) and (B). These can help explain why a
dwell compression of 20 min resulted in a slightly larger
life then 5-min compressive dwell. Similarly, Figure
6
shows in-phase TMF considering the influence of tensile
dwells occurring during the hot part of the cycle. The
model struggles to predict a lower slope often described
by strain life curves of IP test cases suggesting that the
model may need more IP data or physics guided
constraints. A case of IF with a compressive dwell is
shown in Figure
7 that shows a strain life curve fitting
the data well.
3.2 | Goodness of fit
A common method to visualize and evaluate the accu-
racy of a trained NN model is to create a goodness of fit
(GOF) plot in which the actual mean life values are com-
pared directly to the predicted mean life values. To test
for overfitting, the available data was separated into test-
ing data and training data randomly. The GOF plot
FIGURE 6 Predicted strain-life curves for IP thermomechanical fatigue with a maximum temperature of 950 /C14 C, a minimum
temperature of 100 /C14 C, a TSPFalt of 1.7, and frequency 0.0015 Hz showing (A) no dwell and (B) 20-min tensile dwell [Colour figure can be
viewed at wileyonlinelibrary.com]
FIGURE 5 Predicted strain-life curves for OP thermomechanical fatigue with a maximum temperature of 1000 /C14 C, a minimum
temperature of 100 /C14 C, a TSPFalt of /C0 1.6, and frequency 0.0014 Hz showing (A) no dwell, (B) 5-min compressive dwell, and (C) 20-min
compressive dwell [Colour figure can be viewed at wileyonlinelibrary.com]
1562 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 10

shown in Figure 8 was made with using a 20%/80% test/
train split on the training data. This allows for the model
to train with 80% of completely randomly selected data
and is then tasked with predicting log NðÞ for the remain-
ing 20% of the data which is shown in this plot. The GOF
plot shown in Figure
9 was made using all data available
to train and testing with all the data points. The two
dashed lines show a factor of three of life, N. To get an
evaluation of the model, the model was trained 10 times
using a randomly selected 20%/80% test train split each
time and then evaluated with MSE each time with an
average result of 0.188 ± 0.041. This is a low error show-
ing that the model can predict life within a factor of
3. The average MSE of 10 predictions from the model
trained with all data is 0.168 ± 0.011. The smaller MSE
and variation in MSE shows that there were certain test
parameters that the model never learned during the test
train split tests. From both figures and metrics it can be
seen that the model is able to predict life within a factor
of 3 but struggles particularly with runouts. The model
often predicts a lower life than the experimental life
value of the runout data point indicating that the model
FIGURE 7 Predicted strain-life curve for isothermal fatigue at 1100 /C14 C and frequency 0.008 Hz with (A) 2-min tensile dwell and
(B) 2-min compression dwell [Colour figure can be viewed at wileyonlinelibrary.com]
TABLE 3 Criteria for selecting experimental data for comparing to predictions
History
type TSPF alt
Max temperature
(
/C14 C)
Min temperature
(/C14 C)
Log cyclic frequency
log (Hz)
Dwell tension
(minutes)
Dwell compression
(minutes)
IF ±0.0 ±50 ±50 ±0.65 0 ≤ DwellT ≤ 1
60
1
60 < DwellT ≤ 5
5< DwellT ≤ 20
0 ≤ DwellC ≤ 1
60
1
60 < DwellC ≤ 5
5< DwellC ≤ 20
TMF ±0.3 ±50 ±200
FIGURE 8 GOF plot of predicted versus experimental fatigue
lives with 20%/80% test/train split [Colour figure can be viewed at
wileyonlinelibrary.com]
ACHARYA ET AL . 1563
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 11

does not approach a slope of zero asymptotically quick
enough as the strain range decreases. This deviation
appears to be particularly significant when the test fre-
quency is high and no dwells are imposed. These condi-
tions are sparse in the database, suggesting that
additional data under these long-life conditions may
improve the predictions.
3.3 | K-fold cross validation
The model was also evaluated using k-fold cross valida-
tion, which is a good measure of how well the model is
preforming. This test involves splitting the dataset into
k number of folds and then removing one fold of the
dataset and having the model train with the remaining
folds. The model is then asked to predict the outputs of
the data samples in the holdout set using a metric to eval-
uate accuracy of the model. This process is then repeated
for each fold. This differs from the test/train split test
shown earlier that splits the dataset randomly every time.
The model was evaluated with five-fold cross validation
using the metric MSE from Equation
12 to score the
accuracy of model for each tested fold that resulted in an
average cross validation score of 0.186 ± 0.025. The aver-
age cross validation score is similar to the average MSE
score for the 20%/80% GOF test train split and has a
lower standard deviation. The low standard deviation in
the cross validation helps to show that the model is able
to predict life from TMF histories not provided in the
training data with low error. The standard deviation for
the k-fold test is smaller than the GOF MSE standard
deviation because the model only predicts against each
data point once whereas in GOF there is a chance that
the testing sample could contain data already predicted
for. Therefore, the GOF could have multiple data points
or very few data points that were runouts leading to a
larger range of MSE scores. From these scores and Fig-
ures
8 and 9 it is clear that there are certain test cases
that model struggles with consistently but is overall able
to predict life well.
The model trained with 80% of the data can perform
sufficiently with the predicted mean life falling around
a factor of two of actual life as shown by the average
MSE values and the GOF plot. The k-fold test shows
that the model trained with 80% of data remains robust
while still predicting life within a factor of 3. Figure
8
shows that the model can struggle to learn certain rela-
tionships between parameters if those test parameters
are not provided in the training data. A model trained
with all data helps the model learn remaining relation-
ships between parameters to give a best case prediction
of life.
3.4 | Mean of multiple trainings
During the training of a NN, there can exist an element
of randomness defined by the initial training data
selected and the initial randomly selected weights and
biases. To understand how this randomness affects the
trained model, the NN model was trained 10 times using
different randomly selected weights and biases each time.
The resulting mean and 95% CI strain-life curves for two
sets of test conditions are shown in Figures
10 and 11.
The bolder curves in these plots represent the mean of
the 10 predictions. Figure 10 shows a plot with the same
control parameters used to generate Figure 3. Figure 11
shows an out-of-phase TMF case. These plots show that
the sensitivity to the initial weights and biases is about a
factor of two on fatigue life.
A detailed statistical analysis to determine how many
trainings are needed to minimize the error in the mean
of multiple predictions was not conducted. The objective
here is to simply show visually the influence of the initial
random weights and biases. The mean of 10 trainings
was arbitrarily selected for illustration. Certainly, one
could select to train additional times and after each train-
ing, calculate how much the mean prediction has chan-
ged from the prior mean prediction and use a criterion
based on minimizing the change in the mean prediction
to systematically determine the number of trainings
required to the minimize the error.
FIGURE 9 GOF plot of predicted versus experimental fatigue
lives using all data [Colour figure can be viewed at
wileyonlinelibrary.com]
1564 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 12

3.5 | Effect of setting physics guided
constraints
To test how physics-guided constraints affected the
model, two plots of dμ
dεr
over strain range εr were created,
shown in Figure 12A,B, one created using the NN
architecture shown in Figure 1 with physics-guided con-
straints used in the training, while the other was created
without the final output layer and without either the
weight or bias constraints (Table
2) to represent the
known relationships among the mean life, standard devi-
ation, and strain range. The model without the con-
straints does not follow the constraint that
∂2 μ
∂εr 2 ≥ 0 when
the strain range is low. This is also shown in the strain
life curves, shown in Figure
12C,D, where the model
without constraints almost has a linear shape and has a
steeper slope at the very end. On the other hand, the
model with constraints has a strain life curve with a slope
that decreases as the strain range decreased.
The influence of the variance constraint,
∂σ
∂εr
≤ 0, is
discernable in most of the predictions in that the span of
the 95% CI increases as the strain range decreases. Even
when the variance constraint is not applied, shown in
Figure
12C, the predictions using the experimental data
still show a greater variance at lower lives indicating that
there is sufficient data to capture the heteroscedastic
nature of the fatigue lives. By including the variance con-
straint, the resulting predictions will be more robust
especially important when training a dataset that is
sparser.
3.6 | Comparative influence of TMF test
parameters
The key advantage of using a NN model is the ability to
predict the fatigue life of all possible combinations of
temperature, strain rate, and dwells to get the compre-
hensive view of the relative effects of different parameters
while providing confidence intervals to quantify the
uncertainty in the predictions. To show how the model
learned the influence each TMF history parameter on
fatigue life, several prediction plots showing the mean
fatigue lives were generated. Isothermal fatigue predic-
tions shown in Figure
13 expose the influence of temper-
ature, cyclic frequency, and dwells on the fatigue life.
The predictions show that increasing temperature by
100
/C14 C results in a 2 /C2 decrease in life. Reducing the cyclic
frequency by more than 3 orders of magnitude
(i.e., comparing a 1 s cycle to about 20 min cycle) reduces
the life 8 /C2 at 1100
/C14 C and about 5 /C2 at 650 /C14 C. Imposing a
dwell decreases life further with tensile dwells being
about 4/C2 worse than compressive dwells. The predictions
also show that at low strain ranges, tensile dwells become
less detrimental, likely related to the peak tensile stress
during the dwell being sufficiently below the yield
strength. Yet compressive dwells continue to be detri-
mental at low strain ranges, resulting in a steeper strain-
life curve, which likely related to an oxidation-fatigue
FIGURE 11 Ten predictions of the strain-life curve for OP
TMF with a maximum temperature of 900 /C14 C a minimum
temperature of 400 /C14 C, TSPFalt of /C0 1, and frequency 0.0033 Hz
[Colour figure can be viewed at wileyonlinelibrary.com]
FIGURE 10 Ten predictions of the strain-life curve for
isothermal fatigue at 900 /C14 C and frequency 0.033 Hz, each starting
with different random weights and biases [Colour figure can be
viewed at
wileyonlinelibrary.com]
ACHARYA ET AL . 1565
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 13

interaction consistent with what has been observed
experimentally.34
The influence of maximum temperature, minimum
temperature, and long dwell on OP TMF is shown in
Figure 14. In TMF, the maximum temperature has a far
greater impact on fatigue life than the minimum temper-
ature. While it is documented that a lower minimum
temperature is more detrimental,
38,46 the maximum tem-
perature is still clearly the most critical one. Long dwells
at the maximum temperature of OP TMF cycle, therefore
compressive stress, are more detrimental when the strain
range is low and fatigue lives longer. The influence of
these parameters on IP TMF is shown in Figure
15. For
continuous cycling with no dwells, the lives of IP TMF
are comparable with OP TMF. However, tensile dwells
under IP TMF tend to result in 5 /C2 lower life than hot
compressive dwells in OP TMF.
The influence of IP and OP TMF on the model's pre-
dictions can be seen in Figure 16. The lives of IP and OP
TMF exhibit a crossover with OP TMF having a steeper
slope than IP TMF. Consequently, IP TMF has longer life
at low strain ranges and shorter life at high strain ranges
in comparison to OP TMF. These life trends are generally
consistent with data in the literature. One study assessing
the higher strain range conditions only, IP TMF exhibited
around 3/C2 to 5/C2 lower life than OP TMF
38 while another
study reporting lower strain range test data closer to the
transition showed that the difference between the IP and
OP TMF is less than a factor of two.
31 These experimental
trends are typically based on just a handful of data. The
FIGURE 12 (A) Model without physics-guided constraints and (B) model with constraints, (C) strain-life curve for isothermal fatigue at
800/C14 C and frequency 0.02 Hz without constraints, and (D) strain-life curve with constraints [Colour figure can be viewed at
wileyonlinelibrary.com]
1566 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 14

predictions using the larger database indicate that the dif-
ference in life between IP and OP TMF for a given tem-
perature and strain range is less than a factor of two,
which is consistent with the latter study comprising tests
conditions in the intermediate strain ranges.
In the future, for artificial intelligence (AI) to be used
to make assessments of fatigue and durability in complex
high temperature environments involving cyclic loading,
relationships among the various parameters need to be
learned often from multiple sources extracted from litera-
ture and databases to ensure robustness of the predic-
tions. This paper provides the machine learning
foundations for AI to be used in fatigue life assessments
in extreme environments. However, several challenges
remain before AI can readily make fatigue assessments.
In this work, the database was manually generated which
involved digitizing data from strain-life plots reported in
papers and reports, extracting data from tables, extracting
test parameters which were reported in diverse ways
(e.g., strain rate vs. cyclic frequency) requiring some ele-
ments of conversion to consistent parameters sets. While
this was a time-consuming step, it is still more feasible,
taking considerably much less time and is less costly than
running a new test program to generate the data to popu-
late the database. Hence, automated datamining of peer-
reviewed literature, conference proceedings, dissertations
and theses, and other reports still needs development for
AI to become realistic. In addition, the experimental data
FIGURE 13 Isothermal fatigue predictions showing (A) influence of temperature at 0.01 Hz cyclic frequency, (B) influence of frequency
at three different temperatures, and (C) influence of 20 min dwells, comparing tensile versus compressive dwells, at three different
temperatures and 0.0008 Hz cyclic frequency [Colour figure can be viewed at wileyonlinelibrary.com]
FIGURE 14 Out-of-phase (OP) thermomechanical fatigue (TMF) predictions showing (A) influence of Tmax for constant Tmin at 100/C14 C
and 0.0033 Hz cyclic frequency, (B) influence of Tmin for a constant Tmax at 950/C14 C and 0.0033 Hz cyclic frequency, and (C) influence of Tmax
with 20 min compressive dwell for constant Tmin at 100/C14 C and 0.0008 Hz cyclic frequency [Colour figure can be viewed at wileyonlinelibrary.
com]
ACHARYA ET AL . 1567
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 15

itself is statistical in nature, yet each test point typically is
associated with a single fatigue life value. The uncer-
tainties associated with processing and the microstruc-
ture are currently not captured in most studies.
Therefore, all the inputs of the model are still determinis-
tic values in this study. If enough fatigue data is used to
train the model, a Monte Carlo method could be used to
make some assessments on how known statistical vari-
ability in the inputs influence the variability in the
predictions.
By using a comprehensive database extracted from
several sources, the resulting model is robust in the sense
that one rogue set of data will not overly misguide the
decisions made using the model predictions. It can also
be used to quickly identify data that is an outlier which
may suggest some unique property, either good or bad, or
some problem with the testing or data analysis. It also
provides a comprehensive picture of the performance of
existing SX and DS superalloys that can be used to com-
pare to emerging high temperature materials.
Here, the physics-guided constraints used are rather
simple. Future work should focus on ways to bring more
physics into the NN architecture or other ML methods to
improve the predictions for fatigue. This is helpful since
fatigue life will always be limited by sparse datasets.
High-throughput test methods for fatigue do not readily
exist particularly for testing in extreme environments.
For SX and DS Ni-base superalloys, the influence of
crystal orientation in SX and off-axis loading in DS on
the strain-life behavior is significant.
9–12,29,32,47–49 This
critical microstructure parameter as well as possibly
other secondary microstructural influences such as the γ0
precipitate volume fraction and morphology were not
included in the present work, primarily because of the
limited data available to train the model and noting that
the effect on fatigue life was typically not more than a
factor of two.
19,26,50 Since the relationship between crys-
tal orientation and elastic modulus is well known, it can
be used either as a physics-guided constraint or an added
input. In low cycle fatigue, the cyclic plastic strain that
correlates to fatigue life depends on the total applied
strain range and cyclic elastic strain range which is
related to the orientation-dependent elastic modulus.
Further modifications to the PPgNN model are currently
FIGURE 15 In-phase (IP) thermomechanical fatigue (TMF) predictions showing (A) influence of Tmax for constant Tmin at 100/C14 C and
0.0033 Hz cyclic frequency (B) influence of Tmin for a constant Tmax at 950/C14 C and 0.0033 Hz cyclic frequency, and (C) influence of Tmax with
20 min tensile dwell for constant Tmin at 100/C14 C and 0.0008 Hz cyclic frequency [Colour figure can be viewed at wileyonlinelibrary.com]
FIGURE 16 Thermomechanical fatigue (TMF) predictions
showing influence of in-phase (IP) and out-of-phase (OP) for
constant Tmin at 100/C14 C and 0.0033 Hz cyclic frequency [Colour
figure can be viewed at wileyonlinelibrary.com]
1568 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 16

being explored to include the effect of orientation in the
input. Other inputs that may improve the predictions
including the elemental composition and the various pro-
cess parameters. Adding process information, which is
often not completely reported, and dealing with this
missing data in a NN are feasible as shown by Chen and
Liu.
8 In this study, every data record was complete and
hence we did not need to contend with missing input
data. In addition, the inputs considered only linear IP
and OP TMF loading. However, actual loading conditions
may not conform to these basic TMF cycles. The data
available is too sparse on phase shifts
17 and alternative
cycles such as diamond cycles 20,23 to train the model to
predict cycle shapes. However, this is not as large of any
issue since either linear IP TMF or OP TMF tends to be
the worst TMF cycle type.
4 | CONCLUSIONS
This paper demonstrates the use of a probabilistic
physics-guided neural network (PPgNN) for developing a
robust model to predict the cycles to failure under an
extraordinary wide range of thermomechanical fatigue
and creep-fatigue test conditions. The model developed
in this paper serves to confirm the value of the PPgNN
architecture.
• A new PPgNN architecture for predicting thermome-
chanical fatigue and creep-fatigue including identify-
ing the essential inputs and pre- and post-processing of
the data has been established.
• This paper shows that fatigue data extracted (data-
mined) from multiple sources in the open literature
and compiled can then be used as a dataset for devel-
oping a robust fatigue life model that includes uncer-
tainty for a single class of materials, in this case,
directionally-solidified and single-crystal Ni-base
superalloys with similar chemistries and heat treat-
ments typically used for gas turbine blades and vanes.
• The model captures the essential life behaviors typi-
cally observed such as a cross-over in IP and OP TMF,
reduced life with increasing temperature or added
dwells, with the predictions, something that an expert
in the field takes years to understand.
• Setting physics-guided constraints improves the model
predictions making them more robust particularly
when the dataset used for training is sparse.
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are avail-
able in Zenodo at
https://doi.org/10.5281/zenodo.
7476962.51 These data were derived from resources
available in the public domain. 9–42 The trained model
used in this work that can generate prediction curves
such as those shown in Figures
10 and 11 for any input
within the bounds of the model is available through a
web link, which can be obtained by contacting the corre-
sponding author.
REFERENCES
1. Chen J, Liu Y. Fatigue modeling using neural networks: a com-
prehensive review. Fatigue Fract Eng Mater Struct . 2022;45(4):
945-979.
2. Venkatesh V. A neural network approach to elevated tempera-
ture creep –fatigue life prediction. Int J Fatigue . 1999;21(3):
225-234.
3. Zhang X-C, Gong J-G, Xuan F-Z. A deep learning based life
prediction method for components under creep, fatigue and
creep-fatigue conditions. Int J Fatigue . 2021;148:106236.
4. Chen CLP, Kim J, Guo TH. Monte Carlo simulation for system
damage prediction: an example from thermo-mechanical
fatigue (TMF) damage for a turbine engine. In: 2006 IEEE/SMC
International Conference on System of Systems Engineering .
IEEE; 2006:30-34.
5. Schooling JM, Brown M, Reed PAS. An example of the use of
neural computing techniques in materials science —the model-
ling of fatigue thresholds in Ni-base superalloys. Mater Sci Eng
A. 1999;260(1-2):222-239.
6. Chen J, Liu Y. Probabilistic physics-guided machine learning
for fatigue data analysis. Expert Syst Appl . 2021;168:114316.
7. Chen J, Liu Y. Physics-guided machine learning for multi-
factor fatigue analysis and uncertainty quantification. In: AIAA
Scitech 2021 Forum . Reston, Virginia: American Institute of
Aeronautics and Astronautics; 2021.
8. Chen J, Liu Y. Fatigue property prediction of additively manu-
factured Ti-6Al-4V using probabilistic physics-guided learning.
Addit Manuf. 2021;39:101876.
9. Estrada Rodas EA, Gorgannejad S, Neu RW. Creep-fatigue
behaviour of single-crystal Ni-base superalloy CMSX-8. Fatigue
Fract Eng Mater Struct . 2019;42(9):2155-2171.
10. Amaro RL, Antolovich SD, Neu RW. Mechanism-based life
model for out-of-phase thermomechanical fatigue in single
crystal Ni-base superalloys. Fatigue Fract Eng Mater Struct .
2012;35(7):658-671.
11. Segersäll M, Leidermark D, Moverare JJ. Influence of crystal
orientation on the thermomechanical fatigue behaviour in a
single-crystal superalloy. Mater Sci Eng A . 2015;623:68-77.
12. Segersäll M, Deng D. A comparative study between in- and
out-of-phase thermomechanical fatigue behaviour of a single-
crystal superalloy. Int J Fatigue . 2021;146:106162.
13. Lafata MA, Rettberg LH, He MY, Pollock TM. Oxidation-
assisted crack growth in single-crystal superalloys during
fatigue with compressive holds. Metall Mater Trans A . 2018;
49(1):105-116.
14. Hong HU, Choi BG, Kim IS, Yoo YS, Jo CY. Characterization
of deformation mechanisms during low cycle fatigue of a single
crystal nickel-based superalloy. J Mater Sci . 2011;46(15):5245-
5251.
15. Hong HU, Kang JG, Choi BG, Kim IS, Yoo YS, Jo CY. A com-
parative study on thermomechanical and low cycle fatigue
ACHARYA ET AL . 1569
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 17

failures of a single crystal nickel-based superalloy. Int J Fatigue .
2011;33(12):1592-1599.
16. Hong HU, Yoon JG, Choi BG, Kim IS, Yoo YS, Jo CY. Local-
ized microtwin formation and failure during out-of-phase ther-
momechanical fatigue of a single crystal nickel-based
superalloy. Int J Fatigue . 2014;69:22-27.
17. Egly T, Lang K, Lohe D. Influence of phase shift and strain
path on the thermomechanical fatigue behavior of CMSX-4
specimens. Int J Fatigue . 2008;30(2):249-256.
18. Moverare JJ, Johansson S, Reed RC. Deformation and damage
mechanisms during thermal –mechanical fatigue of a single-
crystal superalloy. Acta Mater. 2009;57(7):2266-2276.
19. Ott M, Mughrabi H. Dependence of the high-temperature low-
cycle fatigue behaviour of the monocrystalline nickel-base
superalloys CMSX-4 and CMSX-6 on the γ/γ'-morphology.
Mater Sci Eng A . 1999;272(1):24-30.
20. Masakazu O, Take K, Kakehi K, Yamazaki Y. Collaborative
research on thermo-mechanical and isothermal low-cycle
fatigue strength of Ni-base superalloys and protective coatings
at elevated temperatures in the society of materials science,
Japan (JSMS). ASTM Special Tech Publ . 2003;4:180-194.
21. Wahl JB, Harris K. CMSX-4
® plus single crystal alloy develop-
ment, characterization and application development. In: Super-
alloys 2016. Hoboken, NJ, USA: John Wiley & Sons, Inc.; 2016:
25-33.
22. Yandt S, Wu X-J, Tsuno N, Sato A. Cyclic dwell fatigue behav-
iour of single crystal Ni-base superalloys with/without rhe-
nium. In: Superalloys 2012 . Hoboken, NJ, USA: John Wiley &
Sons, Inc.; 2012:501-508.
23. Okazaki M, Sakaguchi M. Thermo-mechanical fatigue failure
of a single crystal Ni-based superalloy. Int J Fatigue . 2008;30(2):
318-323.
24. Wahl JB, Harris K. New single crystal superalloys, CMSX-7 and
CMSX-8. In: Superalloys 2012 . Hoboken, NJ, USA: John
Wiley & Sons, Inc.; 2012:177-188.
25. Reed RC, Moverare JJ, Sato A, Karlsson F, Hasselqvist M. A
new single crystal superalloy for power generation applications.
In: Superalloys 2012 . Hoboken, NJ, USA: John Wiley & Sons,
Inc.; 2012:197-204.
26. Sato A, Moverare JJ, Hasselqvist M, Reed RC. On the mechani-
cal behavior of a new single-crystal superalloy for industrial
gas turbine applications. Metall Mater Trans A . 2012;43(7):
2302-2315.
27. Segersäll M, Kontis P, Pedrazzini S, et al. Thermal –mechanical
fatigue behaviour of a new single crystal superalloy: effects of
Si and re alloying. Acta Mater. 2015;95:456-467.
28. Moverare JJ, Johansson S. Damage mechanisms of a high-Cr
single crystal superalloy during thermomechanical fatigue.
Mater Sci Eng A . 2010;527(3):553-558.
29. Gabb TP, Gayda J, Miner RV. Orientation and temperature
dependence of some mechanical properties of the single-crystal
nickel-base superalloy René N4: part II. Low cycle fatigue
behavior. Metall Trans A . 1986;17(3):497-505.
30. Yu J, Sun X, Jin T, Zhao N, Guan H, Hu Z. High temperature
creep and low cycle fatigue of a nickel-base superalloy. Mater
Sci Eng a . 2010;527(9):2379-2389.
31. Han GM, Yu JJ, Sun XF, Hu ZQ. Thermo-mechanical fatigue
behavior of a single crystal nickel-based superalloy. Mater Sci
Eng A. 2011;528(19-20):6217-6224.
32. Fleury E, Rémy L. Low cycle fatigue damage in nickel-base
superalloy single crystals at elevated temperature. Mater Sci
Eng a. 1993;167(1-2):23-30.
33. Estrada Rodas AE. Microstructure-sensitive creep-fatigue inter-
action crystal-viscoplasticity model for single-crystal nickel-
base superalloys. PhD Dissertation, Georgia Institute of Tech-
nology, Atlanta, GA, USA. 2017.
34. Shenoy MM, Gordon AP, McDowell DL, Neu RW. Thermome-
chanical fatigue behavior of a directionally solidified Ni-Base
superalloy. J Eng Mater Technol . 2005;127(3):325-336.
35. Gordon AP. Crack initiation modeling of a directionally-
solidified nickel-base superalloy. PhD Dissertation, Georgia
Institute of Technology, Atlanta, GA, USA. 2006.
36. Engler-Pinto JCC, Noseda C, Nazmy MY, Rezai-Aria F. Inter-
action between creep and thermo-mechanical fatigue of
CM247LC-DS. In: Superalloys 1996 (Eighth International Sym-
posium). TMS; 1996:319-325.
37. Kirka M. Thermomechanical behavior of a directionally solidi-
fied nickel-base superalloy in the aged state. PhD Dissertation,
Georgia Institute of Technology, Atlanta, GA, USA. 2014.
38. Kirka MM, Brindley KA, Neu RW, Antolovich SD, Shinde SR,
Gravett PW. Parameters influencing thermomechanical fatigue
of a directionally-solidified Ni-base superalloy. Int J Fatigue .
2015;81:48-60.
39. Guth S, Petr /C19aˇsR , ˇSkorík V, et al. Influence of dwell times on
the thermomechanical fatigue behavior of a directionally solid-
ified Ni-base superalloy. Int J Fatigue . 2015;80:426-433.
40. Okazaki M, Tabata T, Nohmi S. Intrinsic stage i crack growth
of directionally solidified Ni-Base superalloys during low-cycle
fatigue at elevated temperature. Metall Trans A . 1990;21(8):
2201-2208.
41. Rai RK, Sahu JK, Das SK, Paulose N, Fernando C. Creep-
fatigue deformation micromechanisms of a directionally solidi-
fied nickel-base superalloy at 850
/C14 C. Fatigue Fract Eng Mater
Struct. 2020;43(1):51-62.
42. Moore ZJ, Neu RW. Creep fatigue of a directionally solidified
Ni-base superalloy —smooth and cylindrically notched speci-
mens. Fatigue Fract Eng Mater Struct . 2011;34(1):17-31.
43. Kingma D, Ba J. Adam: a method for stochastic optimization.
In: International Conference on Learning Representations . San
Diego: 3rd International Conference on Learning Representa-
tions; 2014.
44. Ruder S. An overview of gradient descent optimization algo-
rithms. arXiv preprint arXiv:1609.04747 . September 2016.
45. Scardapane S, Wang D. Randomness in neural networks: an
overview. WIREs Data Mining Knowledge Discovery . 2017;
7(2):18.
46. Arrell D, Hasselqvist M, Sommer C, Moverare J. On TMF dam-
age, degradation effects, and the associated T-min influence on
TMF test results in y/y Al. In: Superalloys 2004 (Tenth Interna-
tional Symposium). TMS; 2004:291-294.
47. Arakere NK, Orozco E. Analysis of low cycle fatigue properties
of single crystal nickel-base turbine blade superalloys. High
Temp Mater Process . 2001;20(5-6):403-419.
48. Segersäll M, Moverare JJ, Simonsson K, Johansson S. Deforma-
tion and damage mechanisms during thermomechanical
fatigue of a single-crystal superalloy in the <001> and <011>
directions. In: Superalloys 2012 (Twelfth International Sympo-
sium). John Wiley & Sons, Inc.; 2012:215-223.
1570 ACHARYA ET AL .
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

## Page 18

49. Liu L, Meng J, Liu J, Zhang H, Sun X, Zhou Y. Investigation on
low cycle fatigue behaviors of the [001] and [011] oriental sin-
gle crystal superalloy at 760
/C14 C. Mater Sci Eng A . 2018;734:1-6.
50. Kirka MM, Brindley KA, Neu RW, Antolovich SD, Shinde SR,
Gravett PW. Influence of coarsened and rafted microstructures
on the thermomechanical fatigue of a Ni-base superalloy. Int J
Fatigue. 2015;81:191-201.
51. Neu RW. Compilation of LCF and TMF Data for Single-Crystal
and Directionally-Solidified Ni-base Superalloys Loaded in
h001i [Data set]. Zenodo. doi:
10.5281/zenodo.7476962
How to cite this article: Acharya R, Caputo AN,
Neu RW. Predicting creep-fatigue and
thermomechanical fatigue life of Ni-base
superalloys using a probabilistic physics-guided
neural network. Fatigue Fract Eng Mater Struct .
2023;46(4):1554‐1571. doi:
10.1111/ffe.13948
ACHARYA ET AL . 1571
 14602695, 2023, 4, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/ffe.13948 by Xian Jiaotong University, Wiley Online Library on [01/12/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
