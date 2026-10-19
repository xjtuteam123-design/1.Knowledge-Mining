# 10.1016_j.jallcom.2017.03.179

<!-- source: D:\总文献\10.1016_j.jallcom.2017.03.179.pdf -->
<!-- file_sha256: c06dd4076252d485cb5f12883f38dd1b747d452dca71b65fa6435f473a5d3db0 -->

## Page 1

Effect of refractory elements and Al on the high temperature oxidation
of Ni-base superalloys and modelling of their oxidation resistance
Dae Won Yun, Seong Moon Seo, Hi Won Jeong, Young Soo Yoo *
Korea Institute of Materials Science, 797 Changwondaero, Changwon, Gyungnam 641-831, South Korea
article info
Article history:
Received 23 November 2016
Received in revised form
20 February 2017
Accepted 17 March 2017
Available online 19 March 2017
Keywords:
High-temperature alloys
Superalloys
Nickel
Oxidation
Modelling
SEM
abstract
The oxidation resistance of Ni-Co-Cr-Al-W-Mo-Ta-Re-Ru alloys is evaluated by cyclic oxidation at 1 100 /C14 C
and modelled using an arti ﬁcial neural network. The database required for the modelling was con-
structed using design of experiment (the Box-Behnken method) followed by oxidation experiments. The
obtained model with a 7-10-1 architecture exhibits consistent prediction of the experimental data
(R ¼ 0.999). Cr and Al enhance the oxidation resistance by promoting the formation of a protective
NiAl
2O4 layer. Mo and Ru are detrimental to the oxidation resistance. W, Ta and Re exhibit complex
behaviours depending on the contents of other alloying elements.
© 2017 Elsevier B.V. All rights reserved.
1. Introduction
Gas turbines are key systems in both the aerospace and thermal
power plant industries. Since gas turbine components are exposed
to high mechanical loading and severe environmental attack at
high temperatures, Ni-base superalloys are widely used in gas
turbine engines. Increasing the turbine inlet temperature results in
a favourable reduction in the fuel cost and emission by enhancing
the ef ﬁciency of gas turbine engines [1]. However, mechanical
properties, such as the high temperature tensile strength and creep
strength, and the environmental resistance, such as the oxidation
resistance of materials for turbine components, should be further
improved to increase the operating temperature. To enhance the
high temperature tensile strength and creep strength of Ni-base
superalloys, the content of refractory metals such as Mo, W, Ta,
Re and Ru has been increased, and the content of Cr, which provides
oxidation resistance, has been decreased. Although these compo-
sitional changes improve the mechanical properties [2e5], they can
be detrimental to the oxidation resistance [6e8]. In particular, Ru,
Mo and Re can form volatile oxide species; therefore, the oxidation
resistance of alloys containing a large amount of these elements can
be deteriorated [9e12]. Since both the mechanical and oxidation
properties are important in superalloys, it is important to balance
both properties in the development of superalloys.
For a large number of alloying elements used in superalloys,
computational modelling can be an effective tool in the develop-
ment of superalloys with balanced mechanical and oxidation
properties [13e16]. In a previous study on Ni-Cr-W-Mo alloys,
artiﬁcial neural networks (ANN) were successfully employed to
model the oxidation properties [16]. However, the growing number
of variables exponentially increases the number of experiment
required to generate the database for the modelling. For a full
factorial design with 7 variables and 3 levels, 2187 samples have to
be tested, which is practically impossible. Therefore, design of ex-
periments (DOE) can solve this problem by reducing the number of
experiments required to obtain relations between the variables and
properties. By combining computational modelling with DOE, a
promising tool can be created for the development of superalloys.
In this study, 6 refractory elements (Cr, Mo, W, Ta, Re and Ru)
and Al were selected as variables with a compositional range of Ni-
6Co-(2e8)Cr-(0e3)Mo-(2e10)W-(4.5e6.5)Al-(2e10)Ta-(0e6)Re-
(0e6)Ru in wt%. If a full factorial design were employed with 3
levels in each component, 2187 samples would be tested, as
mentioned earlier. By using the Box-Behnken method, the number
of samples required to generate the database for ANN modelling is
reduced to 62 samples with 57 different compositions. In the Box-* Corresponding author.
E-mail address: yys@kims.re.kr (Y.S. Yoo).
Contents lists available at ScienceDirect
Journal of Alloys and Compounds
journal homepage: http://www.elsevier .com/locate/jalcom
http://dx.doi.org/10.1016/j.jallcom.2017.03.179
0925-8388/© 2017 Elsevier B.V. All rights reserved.
Journal of Alloys and Compounds 710 (2017) 8 e19

## Page 2

Behnken design for 7 factors, 6 samples with identical chemical
compositions with the centre point of the compositional range (Ni-
6Co-5Cr-1.5Mo-6W-5.5Al-6Ta-3Re-3Ru) should be tested due to
the statistical importance.
The oxidation resistance of the samples was evaluated by a cy-
clic oxidation test for 50 cycles with a one-hour dwell at 1 100 /C14 C.
The database of the weight changes after 50 cycles was constructed
and modelled by using ANNs, which is similar to a previous study
[16]. The model was successfully constructed in the Cr-Mo-W-Al-
Ta-Re-Ru space and was consistent with the experimental data
(with multiple correlation coef ﬁcient R ¼ 0.999). The weight
change behaviour was analysed using a simple statistical spalling
model proposed by Poquillon and Monceau [17]. The oxide
microstructure was analysed with scanning electron microscopy
(SEM) to study the effect of each element on the high temperature
oxidation.
2. Materials and methods
In the alloy design framework, the goal was to ﬁnd out the effect
of alloying elements including Cr, Mo, W, Al, Ta, Re, and Ru on the
oxidation resistance of Ni-base superalloy. The Box-Behnken design
was employed to DOE to minimize the number of samples in this
study. This design scheme requires smaller experiment runs than
the other schemes such as central composite design (CCD); the CCD
gives 152 runs for 7 independent variables while the Box-Behnken
design [18] gives 62 runs for the same number of variables.
In Box-Behnken design, the levels of the concentrations of
alloying elements were determined according to three coded levels
designated as /C0 1, 0, and þ1. These codes represent the lower limit,
the central value, and the upper limit of an independent variable,
respectively. The zero level is presented as the central design point,
corresponding to the central value of the range of independent
variables under interest. The central points were repeated for 6
times to stabilize the extrapolation around the central region.
The /C0 1 and þ1 levels are edge points which correspond to the
maximum and the minimum values to be tested. The compositional
ranges of tested alloys are shown along with the coded levels in
Table 1. The lower limit and the upper limit of each factor represent
reasonable range of alloying elements in single crystal Ni-base
superalloys. 62 alloy compositions were designed according to
the Box-Behnken method for 7 alloying elements ( Table 2 ). The
alloys from A57 to A62 have an identical composition as a centre
point of the compositional range. To save space, the weight changes
after 50 cycles, which are used in ANN modelling, are also listed in
Table 2.
The samples were prepared by vacuum arc melting. Impurities
that are detrimental to the oxidation resistance, such as S, are
strictly controlled during the raw material selection and the
melting process under 1 ppm. From each ingot, the oxidation
samples are prepared by electrical discharge cutting and micro-
cutting to make discs with 10 mm diameters and 3 mm thick-
nesses. The samples were ground using SiC papers up to 1000-grit
and cleaned in acetone and ethanol before the cyclic oxidation
experiments.
Cyclic oxidation is performed in an open-end furnace equipped
with a programmable specimen in/out system. One cycle of ex-
periments in this study is composed of heating at 1 100 /C14 C for
60 min and cooling in open air for 30 min to room temperature.
Fig. 1 shows the actual temperature pro ﬁle during the cyclic
oxidation experiment. The weights of samples are measured after 0,
2, 4, 16, 20, 32, 36 and 50 cycles using a digital balance with an
accuracy of 10 /C0 4 g. Spalled oxide scales were not incorporated in
the weight measurement. After the oxidation experiment, the ox-
ide scale of the specimens was examined by SEM in the back-
scattered electron imaging (BEI) mode and energy dispersive
spectroscopy.
3. Results and discussion
3.1. Weight changes during cyclic oxidation
The weight change of selected experimental alloys during the
cyclic oxidation is shown in Fig. 2 . One thermal cycle consisted of
exposure at 1 100
/C14 C for 1 h and cooling for 30 min to room tem-
perature. The alloys shown in Fig. 2 contain 5 wt% Cr except A47
and A48. The alloys with 8 wt% Cr or 5 wt% Cr þ 6.5 wt% Al,
including the alloys that are not presented in Fig. 2 , showed no
signiﬁcant weight gain or loss during the experiment, which in-
dicates excellent oxidation resistance. The oxidation resistance of
these alloys were better than that of CMSX-4, which is known to
have excellent oxidation resistance among single crystal Ni-base
superalloys, in the literature [19]. The other alloys showed signi ﬁ-
cant amounts of weight loss. In general, the addition of Cr and Al
was bene ﬁcial to the oxidation resistance. The addition of Ta was
slightly beneﬁcial in some cases. Mo, W and Ru were detrimental to
the oxidation resistance as known in the literature [6e8]. Re had no
signiﬁcant effect on the oxidation resistance.
For an in-depth study of the effect of alloying elements, the
weight change after 50 cycles of the oxidation experiment with
respect to the content of each alloying element is plotted in Fig. 3.
An increase in the Cr content from 2 wt% to 8 wt % signi ﬁcantly
improved the oxidation resistance ( Fig. 3(a)). An increase in the Al
content from 4.5 wt% to 6.5 wt% also improved the oxidation
resistance, except for the alloys with 8 wt% Cr ( Fig. 3 (b)). Mo
addition up to 3 wt% was detrimental to the oxidation resistance.
However, its detrimental effect was reduced when the content of W
was 2 wt% ( Fig. 3 (c)). The effect of W on the oxidation resistance
was generally negative. However, its negative effect was dimin-
ished when the contents of Cr and Al were suf ﬁciently high, as in
the case of the alloys with 8 wt% Cr and 5 wt% Cr þ 6.5 wt% Al
(Fig. 3(d)). The addition of Ta was somewhat bene ﬁcial up to 10 wt
%, except for the alloys with 2 wt% Cr or 8 wt% Cr ( Fig. 3(e)). For the
alloys with 2 wt% Cr, the addition of Ta showed a negative effect.
Moreover, no signi ﬁcant effect was observed for alloys with 8 wt%
Cr. Both positive and negative effects of Ta on the oxidation resis-
tance of Ni-base alloys were reported in the literature [20,21]. The
effect of Re on the oxidation resistance was not monotonous, and it
differed depending on the content of Cr and Al ( Fig. 3 (f)). Monir-
uzzaman et al. reported that the harmful effect of Re was altered by
the content of Al [22], which is similar results with this study. The
addition of up to 6 wt % Ru resulted in an adverse effect on the
oxidation resistance. Similar to the effect of W, the adverse effect of
Ru was reduced when the contents of Cr and Al were suf ﬁciently
high (Fig. 3 (g)).
Table 1
Level values used in the Box-Behnken method.
Level
/C0 10 þ1
Cr 2 5 8
Al 4.5 5.5 6.5
W2 6 1 0
Mo 0 1.5 3
Ta 2 6 10
Re 0 3 6
Ru 0 3 6
Co e 6 e
Ni e Bal. e
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 9

## Page 3

Prior to ANN analysis, linear model analysis was also performed
with the weight changes of the alloys with 5 wt% Cr and 5.5 wt% Al
after the cyclic oxidation to investigate the effect of each refractory
element on the oxidation resistance; the result is presented in
Fig. 4 . The output value was calculated by the following equation.
The linear coef ﬁcients and the constant were determined to mini-
mize the sum of squared deviations.
yðxÞ¼
XI
i¼1
wixi þ c (1)
xi is the weight percent of each alloying element as the input value,
y(x) is the weight change after 50 cycles as the output value, wi and
c are the linear coef ﬁcient for each alloying element and the con-
stant for the model.
Table 2
Nominal alloy composition used in this study and their oxidation properties. The compositions are expressed in weight percent (wt%).
Alloy Name Cr Mo W Al Ta Re Ru Co Ni Weight change after 50 cycles (mg/cm 2)
A01 5.0 1.5 6.0 4.5 2.0 0.0 3.0 6.0 bal. /C0 39.6
A02 5.0 1.5 6.0 6.5 2.0 0.0 3.0 6.0 bal. /C0 6.8
A03 5.0 1.5 6.0 4.5 10.0 0.0 3.0 6.0 bal. /C0 18.7
A04 5.0 1.5 6.0 6.5 10.0 0.0 3.0 6.0 bal. /C0 3.5
A05 5.0 1.5 6.0 4.5 2.0 6.0 3.0 6.0 bal. /C0 28.0
A06 5.0 1.5 6.0 6.5 2.0 6.0 3.0 6.0 bal. /C0 14.4
A07 5.0 1.5 6.0 4.5 10.0 6.0 3.0 6.0 bal. /C0 27.3
A08 5.0 1.5 6.0 6.5 10.0 6.0 3.0 6.0 bal. 0.0
A09 2.0 1.5 6.0 5.5 6.0 0.0 0.0 6.0 bal. /C0 42.4
A10 8.0 1.5 6.0 5.5 6.0 0.0 0.0 6.0 bal. /C0 3.3
A11 2.0 1.5 6.0 5.5 6.0 6.0 0.0 6.0 bal. /C0 28.7
A12 8.0 1.5 6.0 5.5 6.0 6.0 0.0 6.0 bal. /C0 2.3
A13 2.0 1.5 6.0 5.5 6.0 0.0 6.0 6.0 bal. /C0 66.6
A14 8.0 1.5 6.0 5.5 6.0 0.0 6.0 6.0 bal. /C0 3.2
A15 2.0 1.5 6.0 5.5 6.0 6.0 6.0 6.0 bal. /C0 59.2
A16 8.0 1.5 6.0 5.5 6.0 6.0 6.0 6.0 bal. /C0 3.8
A17 5.0 0.0 6.0 5.5 2.0 3.0 0.0 6.0 bal. /C0 8.1
A18 5.0 3.0 6.0 5.5 2.0 3.0 0.0 6.0 bal. /C0 18.8
A19 5.0 0.0 6.0 5.5 10.0 3.0 0.0 6.0 bal. /C0 4.0
A20 5.0 3.0 6.0 5.5 10.0 3.0 0.0 6.0 bal. /C0 10.6
A21 5.0 0.0 6.0 5.5 2.0 3.0 6.0 6.0 bal. /C0 17.2
A22 5.0 3.0 6.0 5.5 2.0 3.0 6.0 6.0 bal. /C0 32.0
A23 5.0 0.0 6.0 5.5 10.0 3.0 6.0 6.0 bal. /C0 13.7
A24 5.0 3.0 6.0 5.5 10.0 3.0 6.0 6.0 bal. /C0 20.1
A25 2.0 0.0 6.0 4.5 6.0 3.0 3.0 6.0 bal. /C0 85.5
A26 8.0 0.0 6.0 4.5 6.0 3.0 3.0 6.0 bal. /C0 2.0
A27 2.0 3.0 6.0 4.5 6.0 3.0 3.0 6.0 bal. /C0 71.8
A28 8.0 3.0 6.0 4.5 6.0 3.0 3.0 6.0 bal. /C0 3.1
A29 2.0 0.0 6.0 6.5 6.0 3.0 3.0 6.0 bal. /C0 18.5
A30 8.0 0.0 6.0 6.5 6.0 3.0 3.0 6.0 bal. /C0 7.9
A31 2.0 3.0 6.0 6.5 6.0 3.0 3.0 6.0 bal. /C0 34.1
A32 8.0 3.0 6.0 6.5 6.0 3.0 3.0 6.0 bal. /C0 2.0
A33 5.0 1.5 2.0 4.5 6.0 3.0 0.0 6.0 bal. /C0 21.5
A34 5.0 1.5 10.0 4.5 6.0 3.0 0.0 6.0 bal. /C0 30.7
A35 5.0 1.5 2.0 6.5 6.0 3.0 0.0 6.0 bal.
/C0 12.3
A36 5.0 1.5 10.0 6.5 6.0 3.0 0.0 6.0 bal. /C0 7.9
A37 5.0 1.5 2.0 4.5 6.0 3.0 6.0 6.0 bal. /C0 36.3
A38 5.0 1.5 10.0 4.5 6.0 3.0 6.0 6.0 bal. /C0 49.6
A39 5.0 1.5 2.0 6.5 6.0 3.0 6.0 6.0 bal. /C0 12.1
A40 5.0 1.5 10.0 6.5 6.0 3.0 6.0 6.0 bal. /C0 8.2
A41 2.0 1.5 2.0 5.5 2.0 3.0 3.0 6.0 bal. /C0 22.0
A42 8.0 1.5 2.0 5.5 2.0 3.0 3.0 6.0 bal. /C0 8.2
A43 2.0 1.5 10.0 5.5 2.0 3.0 3.0 6.0 bal. /C0 56.3
A44 8.0 1.5 10.0 5.5 2.0 3.0 3.0 6.0 bal. /C0 3.5
A45 2.0 1.5 2.0 5.5 10.0 3.0 3.0 6.0 bal. /C0 64.3
A46 8.0 1.5 2.0 5.5 10.0 3.0 3.0 6.0 bal. /C0 2.3
A47 2.0 1.5 10.0 5.5 10.0 3.0 3.0 6.0 bal. /C0 42.2
A48 8.0 1.5 10.0 5.5 10.0 3.0 3.0 6.0 bal. 0.0
A49 5.0 0.0 2.0 5.5 6.0 0.0 3.0 6.0 bal. /C0 10.7
A50 5.0 3.0 2.0 5.5 6.0 0.0 3.0 6.0 bal. /C0 16.0
A51 5.0 0.0 10.0 5.5 6.0 0.0 3.0 6.0 bal. /C0 9.2
A52 5.0 3.0 10.0 5.5 6.0 0.0 3.0 6.0 bal. /C0 21.7
A53 5.0 0.0 2.0 5.5 6.0 6.0 3.0 6.0 bal. /C0 10.9
A54 5.0 3.0 2.0 5.5 6.0 6.0 3.0 6.0 bal. /C0 14.1
A55 5.0 0.0 10.0 5.5 6.0 6.0 3.0 6.0 bal. /C0 16.6
A56 5.0 3.0 10.0 5.5 6.0 6.0 3.0 6.0 bal. /C0 21.5
A57 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 18.0
A58 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 21.7
A59 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 20.5
A60 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 17.5
A61 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 22.2
A62 5.0 1.5 6.0 5.5 6.0 3.0 3.0 6.0 bal. /C0 20.5
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e1910

## Page 4

The other composition range of Cr and Al was not analysed, as
their data points were not suf ﬁcient for the analysis. The calculated
value from the linear model showed a reasonable agreement with
the experimental data ( Fig. 4 (a)). Mo and Ru were detrimental to
the oxidation resistance, and W also showed a negative effect. Re
only had a small negative effect on the oxidation resistance, and Ta
was bene ﬁcial to the oxidation resistance in a given composition
range (Fig. 4 (b)).
To separately observe the effect of alloying elements on the
spallation of an oxide scale and the oxidation rate, the weight
change data were analysed using a simple statistical model [17].
Some assumptions in the model are not valid in this study. How-
ever, the spalling probability and the parabolic rate constant ob-
tained by the model can be useful for a study that compares the
cyclic oxidation of alloys with similar chemical compositions.
Moreover, the model was successful in our previous study for
analysing the effect of Si and Al on the oxidation resistance of Ni-Cr-
W-Mo alloys [23]. The ﬁtted lines in Fig. 2 show the plausibility of
the model. The spalling probability and the parabolic rate constant
of selected experimental alloys obtained by the model are pre-
sented in Fig. 5. Cr was effective in reducing both spallation and the
oxidation rate, whereas Al was mainly effective in reducing
spallation. Mo and Ru deteriorated the oxidation resistance by
increasing spallation. Ta showed a bene ﬁcial effect on reducing
spallation. Furthermore, the addition of up to 6 wt% Re was negli-
gible to the oxidation resistance. The effect of W could not be
analysed by the model due to the incompatibility of the ﬁtted
curves by the model with the experimental data.
3.2. Microstructure of the oxide scale
After the cyclic oxidation experiment, the oxide scale of the
specimens was examined by SEM. To observe the effect of the
alloying element on the microstructure of oxide scale, the oxide
microstructure of selected specimens were compared. The micro-
graphs show the representative microstructure of the oxide scale
where the oxide scales was relatively intact. The areas where the
oxide scale was spalled out were not shown, because they do not
show the microstructure of the oxide scales properly. In the areas
where the oxide scale was relatively intact, the microstructure of
the oxide scale was quite uniform. Since the addition of up to 6 wt%
Re had negligible effect on the oxide microstructure, micrographs
that compare the oxide microstructure of specimens with and
without Re are not presented. The oxide phases were mainly
identiﬁed by energy dispersive spectroscopy (EDS) analysis. Anal-
ysis results of X-ray diffraction and EDS in previous studies with
similar oxide microstructure [16,23] and analysis results in the
literature [24e29] were taken into consideration when identifying
the oxide phases.
Fig. 6 shows the effect of Cr on the oxide microstructure. The
typical oxide scale of specimen A41 with 2 wt% Cr consisted of a
thick mixed oxide layer, a Ni-Cr spinel layer and a discrete NiAl
2O4
layer. In addition, the mixed oxide layer was composed of NiO, Ni-
Cr spinels and NiWO
4 particles, which appear as white particles
(Fig. 6 (a)). The outermost part of the oxide scale, which is pre-
sumably a NiO layer, is seemingly spalled during the cooling pro-
cess. In contrast, the oxide scale of specimen A42 with 8 wt% Cr
consisted of a thin mixed oxide layer, a Ni-Cr spinel layer and a
continuous NiAl 2O4 layer. The mixed oxide layer was mainly
composed of Ni-Cr spinels, and it contains a small amount of NiO
and NiWO 4 particles ( Fig. 6 (b)). The increase in the Cr content
suppressed the formation of the transient oxides of NiWO 4 and NiO
and promoted the formation of a protective NiAl 2O4 layer by acting
as an oxygen getter [30,31].
Fig. 7 shows the effect of Al on the oxide microstructure. The
oxide scale of specimen A01 with 4.5 wt% Al mainly consisted of a
NiO layer and a mixed oxide layer. The mixed layer was composed
of either NiO-NiWO4 (Fig. 7(a)) or NiO-spinel-NiWO4 (Fig. 7(b)). The
innermost part of the oxide scale consisted of either an internal
oxidation zone of spinels ( Fig. 7 (a)) or a discrete NiAl 2O4 layer
(Fig. 7 (b)). Cracks were observed along the mixed oxide layer,
which aggravate spallation of the oxide scale. On the contrary, the
oxide scale of specimen A02 with 6.5 wt% Al consisted of a mixed
oxide layer, a Ni-Cr spinel layer and a continuous NiAl 2O4 layer.
Moreover, the mixed oxide layer was composed of NiO, Ni-Cr spi-
nels and NiWO4 particles (Fig. 7(c)). A small amount of NiO was also
found on the outermost part of the oxide scale. The increase in the
Al content promoted the formation of a protective NiAl 2O4 layer,
and it also reduced the formation of the mixed oxide layer, which is
prone to spallation.
Fig. 8 shows the effect of Mo on the oxide microstructure. In
both the specimens of A49 without any Mo and A50 with 3 wt% Mo,
the oxide scales were composed of a NiO layer, a mixed oxide layer,
a Ni-Cr spinel layer and a NiAl2O4 layer. Furthermore, the formation
of oxide nodules was observed in some areas of both specimens
(Fig. 8 (a), (c) and (d)). However, the size of the oxide nodules
formed on the specimen with 3 wt% Mo was much larger, and the
Fig. 1. The actual temperature pro ﬁle during the cyclic oxidation experiment.
Fig. 2. Weight change with oxidation cycles of one-hour exposures at 1 100 /C14 C for
selected experimental alloys and CMSX-4 from the literature [19].
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 11

## Page 5

Fig. 3. Weight change after 50 cycles of the oxidation experiment with respect to the content of (a) Cr, (b) Al, (c) Mo, (d) W, (e) Ta, (f) Re and (g) Ru.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e1912

## Page 6

nodules were more frequently observed. It seems that the evapo-
ration of Mo species deteriorated the stability of the protective
oxide scale. This promoted the formation of oxide nodules. A
similar effect of Mo was found in a study with ferritic stainless
steels [32].
Fig. 9 shows the effect of W on the oxide microstructure. In both
specimens of A53 with 2 wt% W and A55 with 10 wt% W, the oxide
scales consisted of a NiO layer, a mixed oxide layer, a Ni-Cr spinel
layer and a continuous NiAl 2O4 layer. However, thick layers of NiO
and NiO-spinel-NiWO4 mixed oxides were found in several areas of
specimen A55 with 10 wt% W ( Fig. 9 (c)). Since this mixed oxide
layer contains a large amount of pores, it is prone to cracking and
spalling ( Fig. 9 (d)). An increase in the W content from 2 wt% to
10 wt% facilitated the growth of NiO and the mixed oxide layer.
Fig. 10 shows the effect of Ta on the oxide microstructure. The
oxide scale of specimen A17 with 2 wt% Ta mainly consisted of a
NiO layer, a mixed oxide layer, Ni-Cr spinels and a NiAl
2O4 layer
(Fig. 10(a)). The formation of a discrete Al 2O3 layer was observed in
only a limited area (Fig. 10(b)). In specimen A19 with 10 wt% Ta, the
formation of NiO and NiWO 4 was suppressed; moreover, CrTaO 4
was found beneath or inside the NiAl 2O4 layer (Fig. 10(c) and (d)).
Fig. 4. Linear model analysis result for the weight changes after the cyclic oxidation of the alloys with 5 wt% Cr and 5.5 wt% Al: (a) experimental and calculate d weight changes and
(b) linear coef ﬁcient of each alloying element.
Fig. 5. Parabolic rate constant and spalling probability of selected experimental alloys
calculated by the simple statistical spalling model.
Fig. 6. BEI cross-sectional microstructure of (a) specimen A41 with 2 wt% Cr and (b) specimen A42 with 8 wt% Cr after 50 cycles of cyclic oxidation.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 13

## Page 7

Fig. 7. BEI cross-sectional microstructure of (a) and (b) specimen A01 with 4.5 wt% Al and (c) specimen A02 with 6.5 wt% Al after 50 cycles of cyclic oxidation.
Fig. 8. BEI cross-sectional microstructure of (a) and (b) specimen A49 without Mo and (c) and (d) specimen A50 with 3 wt% Mo after 50 cycles of cyclic oxidation.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e1914

## Page 8

Fig. 9. BEI cross-sectional microstructure of (a) specimen A53 with 2 wt% W and (b), (c) and (d) specimen A55 with 10 wt% W after 50 cycles of cyclic oxidation.
Fig. 10. BEI cross-sectional microstructure of (a) and (b) specimen A17 with 2 wt% Ta and (c) and (d) specimen A19 with 10 wt% Ta after 50 cycles of cyclic oxidatio n.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 15

## Page 9

The formation of CrTaO 4 in Ni- and Co-base alloys with Ta and Cr
was reported in the literature [26e29]. Another change in the oxide
microstructure was the formation of a continuous Al 2O3 layer.
Compared to specimen A1 7 with 2 wt% Ta, the formation of Al 2O3
was more frequently observed in specimen A19 with 10 wt% Ta.
Additionally, areas with a continuous Al 2O3 layer, as shown in
Fig. 10(d), were also found in specimen A19. Ta presumably acted as
an oxygen getter similar to Cr, which promoted the formation of a
continuous Al 2O3 layer. Since the equilibrium oxygen partial pres-
sure of Ta (8.3 /C2 10/C0 23 atm [33]) is slightly lower than that of Cr
(2.6 /C2 10/C0 20 atm [34])a t1 1 0 0/C14 C, Ta can also act as an oxygen getter
for the formation of Al 2O3.
Fig. 1 1 shows the effect of Ru on the oxide microstructure. In
specimen A19 without any Ru, the oxide scale mainly consisted of a
Cr-Ni spinel layer and a NiAl 2O4 layer, and NiO and NiWO 4 were
found in some areas (Fig. 1 1(a)). Moreover, the formation of NiO and
NiWO4 was suppressed in the area with a CrTaO 4 layer (Fig. 1 1(b)).
However, a thick NiO layer and a mixed oxide layer, composed of
NiO, Ni-Cr spinels and NiWO 4, were formed on specimen A23 with
6 wt% Ru ( Fig. 1 1(c)). The formation of NiWO 4 particles was
observed in even the area with a CrTaO4 layer (Fig. 1 1(d)). Similar to
Mo, Ru seems to deteriorate the stability of the protective oxide
scale and to promote the formation of NiO and NiWO 4 by forming
volatile oxide species.
The changes in the oxide microstructure with respect to the
changes in the content of each alloying element were consistent
with the weight change data of Fig. 2 . Cr and Al improved the
oxidation resistance by promoting the formation of protective
NiAl2O4 and by suppressing the formation of transient oxides such
as NiO and NiWO 4. Mo and Ru disturbed a barrier property of the
oxide scale and promoted the formation of transient oxides by
forming volatile oxide species such as MoO 3 and RuO 3 [9e12].W
also deteriorated the oxidation resistance by accelerating the
Fig. 1 1. BEI cross-sectional microstructure of (a) and (b) specimen A19 without Ru and (c) and (d) specimen A23 with 6 wt% Ru after 50 cycles of cyclic oxidation.
Fig. 12. Real and predicted values of the cyclic oxidation weight change. The prediction
was made by the ANN model with a 7-10-1 architecture. Error bars are also provided.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e1916

## Page 10

formation of the mixed oxide layer containing NiWO 4. Ta enhanced
the oxidation resistance by encouraging the formation of a
continuous Al 2O3 layer and by suppressing the formation of tran-
sient oxides. The addition of up to 6 wt% Re had a negligible effect
on the oxidation resistance and the microstructure.
3.3. Arti ﬁcial neural network modelling
The cyclic oxidation database is constructed by setting contents
of Cr, Al, Mo, W, Ta, Re and Ru as the input parameters and the
weight change after 50 cycles as the output ( Table 2). A program by
Radford Neal [35] was used in the ANN training and prediction in
this study. The output value, y(x), is calculated by following
equations.
yðxÞ¼
XH
h¼1
ghvh þ bo (2)
ghðxÞ¼ tanh
 XI
i¼1
xiwih þ bh
!
(3)
Here, xi and gh(x) are the input value and the value of the hidden
node, wih and bh are the weight and the bias on the connection from
input i to hidden node h, v h and bo are the weight and the bias on
the connection from hidden node h to output. The values of the
weights and the biases are randomly assigned as an initial value. By
neural network training process, the values of the weights and the
biases are adjusted to predict the output value properly. Detailed
information on ANN training can be found in previous studies
[15,16]. Only one hidden layer is employed in this study, which can
be expressed as ‘7-x-1’ with ‘x’ as the number of nodes in the
hidden layer. A total of 46 architectures from‘7-5-1’ to ‘7-50-1’ were
tested to ﬁnd a model consistent with the actual experimental data
while preventing over- ﬁtting [36,37]. Among the tested architec-
tures, a 7-10-1 architecture showed the highest value of the mul-
tiple correlation coef ﬁcient R (R ¼ 0.999) and was chosen for the
study. The real and predicted weight change data are shown in
Fig. 12. The predicted value by ANN modelling shows good agree-
ment with the experimental data. The short error bars in Fig. 12also
indicate that each prediction is performed with very high
conﬁdence.
Figs. 13 and 14show contour maps of the weight change after 50
cycles predicted by the ANN model, which are a part of the ANN
Fig. 13. Contour maps of the weight change after 50 cycles in terms of the W and Mo contents for Ni-6Co-xCr-yAl-6Ta-3Re-3Ru alloys generated by the ANN predicti on. A scale bar
indicating the weight change value is located on the right side of each contour map.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 17

## Page 11

modelling results. The contour maps in Fig. 13 were plotted by
changing the W content from 2 to 10 wt% and the Mo content from
0 to 3 wt% with a step size of 0.1 wt% for various Cr and Al contents.
As observed in the scale bar of the contour maps, the overall weight
loss was reduced as the Cr and Al contents increased. However, the
effect of Mo and W varied with the Cr and Al contents. In alloys with
2 wt% Cr and 4.5 wt% Al, it was predicted that an increase in the W
and Mo contents would result in a reduction in the weight loss. A
similar behaviour was observed in a study with Ni-Cr-W-Mo alloys
[16]. The reduced thermal expansion mismatch between a metal
substrate and an oxide scale was proposed as a mechanism for the
reduction in the weight loss of alloys with low Cr content and high
W and Mo contents [16]. In alloys with more than 5 wt% Cr or 5.5 wt
% Al, an increase in the W and Mo contents was generally harmful
for the oxidation resistance. As observed from Fig. 3(c), the harmful
effect of Mo was reduced with 2 wt% W in alloys with 5 wt% Cr and
5.5 wt% Al. In alloys with 5 wt% Cr þ 6.5 wt% Al and alloys with 8 wt
% Cr, however, the harmful effect of W on the oxidation resistance
was diminished.
The contour maps in Fig. 14 were plotted by changing the Re
content from 0 to 6 wt% and the Ru content from 0 to 6 wt% with a
step size of 0.1 wt% for various Cr and Al contents. In the same
manner as Fig. 13, the overall weight loss was reduced as the Cr and
Al contents increased. Ru was detrimental to the oxidation resis-
tance in all cases. However, the effect of Re was varied depending
on the Cr and Al contents. In alloys with 2 wt% Cr and 5 wt%
Cr þ 4.5 wt% Al, it was predicted that the addition of up to 6 wt% Re
would be slightly bene ﬁcial to the oxidation resistance. In alloys
with 8 wt% Cr and 6.5 wt% Al, the addition of Re also had a beneﬁcial
effect. In contrast, the addition of Re was harmful to the oxidation
resistance in alloys with 5 wt% Cr þ 6.5 wt% Al and 8 wt%
Cr þ (4.5e5.5) wt% Al. In alloys with 5 wt% Cr and 5.5 wt% Al, Re
only had a small amount of negative effect on the oxidation resis-
tance. This is consistent with the result of the linear model analysis
(Fig. 4).
As observed from Figs. 13 and 14 , the effect of an alloying
element can be altered by the contents of other alloying elements.
Since there is complex interaction between the alloying elements,
in most cases, their behaviour cannot be ﬁtted by a simple linear
model. Moreover, modelling becomes more dif ﬁcult as the number
of variables increases. By using ANN, however, the oxidation
resistance was successfully modelled in the complex system with 7
variables. This combined method of DOE and ANN can be a useful
tool in the development of not only superalloys but also other
Fig. 14. Contour maps of the weight change after 50 cycles in terms of the Re and Ru contents for Ni-6Co-xCr-yAl-6Ta-6W-1.5Mo alloys generated by the ANN predic tion. A scale bar
indicating the weight change value is located on the right side of each contour map.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e1918

## Page 12

complex alloys.
4. Conclusions
To model the oxidation resistance of Ni-base superalloys with a
chemical composition range of Ni-6Co-(2 e8)Cr-(0e3)Mo-(2e10)
W-(4.5e6.5)Al-(2e10)Ta-(0e6)Re-(0e6)Ru with ANN, weight
changes were measured after 50 cycles of a one-hour dwell at
110 0/C14 C. The Box-Behnken method was used to reduce the number
of samples required to generate the database for the modelling.
Compared to the full factorial design, the required number of
samples reduced from 2187 to 62 by this method. The obtained
ANN model had a 7-10-1 architecture and a multiple correlation
coefﬁcient of 0.999.
An increase in Cr and Al was bene ﬁcial to the oxidation resis-
tance by promoting the formation of a protective NiAl 2O4 layer and
by suppressing the formation of transient oxides such as NiO and
NiWO4. An increase in Mo and W was generally harmful to the
oxidation resistance by promoting the formation of NiO and a
porous mixed oxide layer that consisted of NiWO4 and Ni-Cr spinel,
except in the alloys with 2 wt% Cr and 4.5 wt% Al. In those alloys, an
increase in Mo and W reduced the weight loss. In alloys with 5 wt%
Cr þ 6.5 wt% Al and alloys with 8 wt% Cr, the harmful effect of W
known in the literature was eliminated. It was found that the
harmful effect of W can be suppressed by alloying suf ﬁcient
amount of Cr and Al in this study. An increase in Ru was detrimental
to the oxidation resistance by promoting the formation of NiO and
NiWO
4. It was also found that Ta and Re can show both positive and
negative effects on the oxidation resistance depending on the
contents of Cr as well as Al.
Acknowledgements
This research was supported by a grant from the Fundamental
R&D Program for Strategic Core Materials (grant no. 10043795)
funded by the Ministry of Trade, Industry and Energy, Republic of
Korea.
References
[1] A. Klenk, K. Maile, H. Theofel, A. Helmrich, R. Husemann, J. Heinemann,
G. Lüdenbach, in: Proceedings of the 8th Li /C18ege Conference on Materials for
Advanced Power Engineering, vol. 2006, 2006, pp. 1597 e1608.
[2] Astrid Heckl, Ralf Rettig, Robert F. Singer, Adv. Mater. Res. 278 (2011)
339e344.
[3] F.H. Latief, K. Kakehi, H. An-Chou Yeh, H. Murakami, Mater. Sci. Eng. A 592
(2014) 143 e152.
[4] M.V. Nathal, L.J. Ebert, Metall. Trans. A 16 (1985) 1863 e1870.
[5] Jian Zhang, Jinguo Li, Tao Jin, Xiaofeng Sun, Zhuangqi Hu, Mater. Sci. Eng. A
527 (2010) 3051 e3056.
[6] G. Brewster, I.M. Edmonds, S. Gray, Oxid. Met. 81 (2014) 345 e356.
[7] Q. Feng, B. Tryon, L.J. Carroll, T.M. Pollock, Mater. Sci. Eng. A 458 (2007)
184e194.
[8] K. Kawagishi, A. Sato, H. Harada, A.-C. Yeh, Y. Koizumi, T. Kobayashi, Mater. Sci.
Tech. 25 (2009) 271 e275.
[9] Neil Birks, Gerald H. Meier, Fred S. Pettit, Introduction to the High-
temperature Oxidation of Metals, second ed., Cambridge University Press,
2006, pp. 86 e88.
[10] Qingqing Yang, Weihao Xiong, Shiqi Li, Hongxia Dai, Jun Li, J. Alloys Compd.
506 (2010) 461 e467.
[11] Wayne E. Bell, M. Tagami, J. Phys. Chem. 67 (1963) 2432 e2436.
[12] J.E. Battles, G.E. Gundersen, R.K. Edwards, J. Phys. Chem. 72 (1968)
3963e3969.
[13] H.K.D.H. Bhadeshia, D.J.C. MacKay, L.E. Svensson, Mater. Sci. Tech. 11 (1995)
1046e1051.
[14] H. Fujii, D.J.C. MacKay, H.K.D.H. Bhadeshia, ISIJ Int. 36 (1996) 1373 e1382.
[15] Y.S. Yoo, C.Y. Jo, C.N. Jones, Mater. Sci. Eng. A 336 (2002) 22 e29.
[16] Dae Won Yun, S.M. Seo, H.W. Jeong, I.S. Kim, Y.S. Yoo, J. Alloys Compd. 587
(2014) 105 e112.
[17] D. Poquillon, D. Monceau, Oxid. Met. 59 (2003) 409 e431.
[18] G.E.P. Box, D.W. Behnken, Technometrics 2 (1960) 455 e475.
[19] R. Orosz, U. Krupp, H.-J. Christ, D. Monceau, Oxid. Met. 68 (2007) 165 e176.
[20] Sherwin W. Yang, Oxid. Met. 15 (1981) 375 e397.
[21] A. Sato, Y.-L. Chiu, R.C. Reed, Acta Mater. 59 (2011) 225 e240.
[22] Md. Moniruzzaman, M. Maeda, Y. Murata, M. Morinaga, ISIJ Int. 43 (2003)
386e393.
[23] Dae Won Yun, S.M. Seo, H.W. Jeong, Y.S. Yoo, Corros. Sci. 83 (2014) 176 e188.
[24] C.M. Younes, G.C. Allen, J.A. Nicholson, Corros. Eng. Sci. Tech. 42 (2007) 80 e88.
[25] A. Akhtar, M.S. Hook, R.C. Reed, Metall. Mater. Trans. A 36 (2005) 3001 e3017.
[26] C.T. Liu, J. Ma, X.F. Sun, J. Alloys Compd. 491 (2010) 522 e526.
[27] Hee-Soo Kim, Si-Jun Park, Seong-Moon Seo, Young-Soo Yoo, Hi-Won Jeong,
HeeJin Jang, Met. Mater. Int. 22 (2016) 789 e796.
[28] M.H. Li, X.F. Sun, T. Jin, H.R. Guan, Z.Q. Hu, Oxid. Met. 60 (2003) 195 e210.
[29] G.N. Irving, J. Stringer, D.P. Whittle, Corros. Sci. 15 (1975) 337 e344.
[30] C. Wagner, J. Electrochem. Soc. 103 (1956) 627 e633.
[31] C. Wagner, Corros. Sci. 5 (1965) 751 e764.
[32] Dae Won Yun, Hyung Suk Seo, Jae Ho Jun, Jae Myung Lee, Kyoo Young Kim,
Int. J. Hydrogen Energy 37 (2012) 10328 e10336.
[33] S.P. Garg, N. Krishnamurthy, A. Awasthi, M. Venkatraman, J. Phase Equilib. 17
(1996) 63 e77.
[34] F.N. Mazandarany, R.D. Pehlke, J. Electrochem. Soc. 121 (1974) 711 e714.
[35] R.M. Neal, Retrieved June 24, 2013, http://www.cs.utoronto.ca/~radford/.
[36] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Nature 323 (1986) 533 e536.
[37] R.P. Lippmann, IEEE Acoust. Speech Signal Process. Mag. 4 (1987) 4 e22.
D.W. Yun et al. / Journal of Alloys and Compounds 710 (2017) 8 e19 19
