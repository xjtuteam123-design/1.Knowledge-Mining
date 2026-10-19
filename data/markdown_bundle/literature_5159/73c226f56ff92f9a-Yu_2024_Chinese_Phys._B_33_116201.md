# Yu_2024_Chinese_Phys._B_33_116201

<!-- source: D:\总文献\Yu_2024_Chinese_Phys._B_33_116201.pdf -->
<!-- file_sha256: 4d0312bec8308975614aa21f16a331d7913f3d12b52c148455afa62607a24871 -->

## Page 1

Chinese Physics B
       
PAPER
A molecular dynamics study on mechanical
performance and deformation mechanisms in
nanotwinned NiCo-based alloys with nano-
precipitates under high temperatures
To cite this article: Zihao Yu et al 2024 Chinese Phys. B 33 116201
 
View the article online for updates and enhancements.
You may also like
Self-adjusting voxelated electrochemical
three-dimensional printing of metallic
microstructures
Xianghe Meng, Xiaomo Wu, Xingjian Shen
et al.
-
Communication—Fabrication of Vertical 
Nanotwinned Copper with (220) Texture
by Direct Current Electrodeposition
Yu Bai, Hua Hu, Huiqin Ling et al.
-
Communication—Growth of <111> 
Nanotwinned Nickel Films on <111>
Nanotwinned Cu Substrates
Yi-Cheng Chu and Chih Chen
-
This content was downloaded from IP address 202.200.234.50 on 29/11/2025 at 11:48

## Page 2

Chin. Phys. B 33, 116201 (2024)
A molecular dynamics study on mechanical performance and
deformation mechanisms in nanotwinned NiCo-based
alloys with nano-precipitates under high temperatures
Zihao Yu(于子皓)1, Hongyu Wang( 王鸿宇)1, Ligang Sun( 孙李刚)2, Zhihui Li( 李志辉)3,4, and Linli Zhu( 朱林利)1,†
1School of Aeronautics and Astronautics, Center for X-Mechanics, Zhejiang University, Hangzhou 310027, China
2School of Science, Harbin Institute of Technology, Shenzhen 518067, China
3Hypervelocity Aerodynamics Institute, China Aerodynamics Research and Development Center, Mianyang 621000, China
4National Laboratory for Computational Fluid Dynamics, Beijing 100191, China
(Received 23 May 2024; revised manuscript received 4 August 2024; accepted manuscript online 8 August 2024)
Molecular dynamics simulations are performed to investigate the mechanical behavior of nanotwinned NiCo-based
alloys containing coherent L1 2 nano-precipitates at different temperatures, as well as the interactions between the dis-
locations and nano-precipitates within the nanotwins. The simulation results demonstrate that both the yield stress and
ﬂow stress in the nanotwinned NiCo-based alloys with nano-precipitates decrease as the temperature rises, because the
higher temperatures lead to the generation of more defects during yielding and lower dislocation density during plastic
deformation. Moreover, the coherent L12 phase exhibits excellent thermal stability, which enables the hinderance of dislo-
cation motion at elevated temperatures via the wrapping and cutting mechanisms of dislocations. The synergistic effect of
nanotwins and nano-precipitates results in more signiﬁcant strengthening behavior in the nanotwinned NiCo-based alloys
under high temperatures. In addition, the high-temperature mechanical behavior of nanotwinned NiCo-based alloys with
nano-precipitates is sensitive to the size and volume fraction of the microstructures. These ﬁndings could be helpful for the
design of nanotwins and nano-precipitates to improve the high-temperature mechanical properties of NiCo-based alloys.
Keywords: NiCo-based alloys, high temperature, nano-precipitate, nanotwins, molecular dynamics simula-
tion, mechanical behavior, deformation mechanism, dislocations
PACS:62.20.F–, 61.72.Mm, 68.35.bd, 02.70.Ns DOI: 10.1088/1674-1056/ad6cca
1. Introduction
With the increasing demand for materials that exhibit su-
perior performance under extreme conditions, the deforma-
tion behavior and mechanical properties of metallic materi-
als at elevated temperatures have garnered signiﬁcant attention
in recent years. [1–3] It has been proved that high-entropy al-
loys (HEAs) and multi-principal element alloys (MEAs) pos-
sess better mechanical properties and demonstrate outstand-
ing performances in high-temperature environments. [4–7] For
example, the high-temperature performance of NiCo-based
alloys containing nano-precipitates has been under contin-
uous scrutiny. [8–11] In nickel-based high-entropy alloys, the
addition of a certain amount of Al elements, followed by
appropriate annealing treatment, can result in the formation
of a highly stable L1 2 precipitate, Ni 3Al, within the alloy,
which remains stable at high temperatures. These precipitates
could signiﬁcantly strengthen the alloy and greatly enhance its
tensile strength and creep resistance under high-temperature
conditions.[12–14] Some studies also reported that introducing
nanotwins into NiCo-based alloys can enhance the plastic de-
formation capacity of the material.[15–17] This improvement is
attributed to the more effective hindrance posed by the high-
density twin boundaries (TBs) on dislocation motion. [18–20]
Concurrently, nanotwins exhibit excellent thermal stability un-
der high-temperature conditions, contributing to the enhance-
ment of the alloy’s plastic deformation behavior during service
at high temperatures.[21–23]
In the past, substantial research has been conducted
using atomic-scale computational methods to explore the
mechanical behavior and underlying mechanisms of nanos-
tructured metals, such as nanotwinned metals and those
containing nano-precipitates. [24–27] These studies have also
discussed the interaction mechanisms between dislocations
and these microstructures. [28–30] For instance, Zhu et al .
used atomic simulations to investigate the barrier mecha-
nism of twin boundaries against dislocations and uncov-
ered the relationship between the width of the dislocation
piled-up zone near the twin boundaries and the stretching
process.[29] Atomic-scale approaches have also been used to
study the mechanical properties of metals at both low and
high temperatures, [23,31–33] such as Liu et al ., who utilized
molecular dynamics (MD) to explore the tensile strength and
plastic behavior of CoCrCuFeNi across different temperature
regimes.[34] However, even though experimental and theoret-
ical studies have reported the strengthening effects of com-
bined nano-precipitates and nanotwins at room temperature in
NiCo-based alloys, [35–37] there is a relative dearth of discus-
†Corresponding author. E-mail: llzhu@zju.edu.cn
© 2024 Chinese Physical Society and IOP Publishing Ltd http://iopscience.iop.org/cpb 　 　 　http://cpb.iphy.ac.cn
116201-1

## Page 3

Chin. Phys. B 33, 116201 (2024)
sion on the high-temperature mechanical properties and defor-
mation mechanisms of nanotwinned NiCo-based alloys with
nano-precipitates.
In this work, the atomic method is utilized to quanti-
tatively investigate the mechanical properties and deforma-
tion mechanisms in NiCo-based alloys containing both Ni 3Al
nano-precipitates and NiCoCr nanotwins under high temper-
ature. By employing MD simulations, the tensile deforma-
tion behavior of nanotwinned NiCo-based alloys with nano-
precipitates under different temperatures is modeled to explore
the impact of high temperature on the deformation behavior
and mechanical properties of such novel nanostructured NiCo-
based alloys. The quantitative relationship between the tem-
perature and the mechanical performance, such as the yield
stress and ﬂow stress, is analyzed. And the interactions among
the nanotwins, L1 2 precipitates, and dislocation motion in
the high-temperature environment, as well as their synergis-
tic strengthening mechanisms, are discussed in detail.
2. Simulation method
The MD simulations in this work are performed using
the large-scale atomic/molecular massively parallel simulator
(LAMMPS),[38] in which the NiCoCrFeAl ﬁve-element EAM
potential developed by Farkas and Caro is used to describe the
interatomic potential. [39] In the simulated model, the nano-
precipitates are supposed to locate at the twin boundaries,
where the volume fraction of the precipitate is 30%, as shown
in Figs. 1(a)–1(c). The total atomic number of the simulation
is approximately 1110000, and its three directions adopt peri-
odic conditions. The twin space is 11.7 nm, and the diameter
of the L1 2 precipitate (Ni 3Al) is 6 nm. In the simulations,
the temperatures are set as 823 K, 923 K, 1023 K, 1123 K,
1223 K, and 1323 K, respectively, and then held for a certain
amount of time under the NPT with 0 bar pressure. The simu-
lation cells are subjected to tensile simulation along the Z di-
rection. The engineering strain rate for loading is 2 × 108 s−1.
The simulation results are processed using atomic visualiza-
tion software (OVITO), and the crystal structure is analyzed
by common neighbor analysis (CNA).[40]
3. Results and discussion
3.1. Deformation mechanisms at high temperature
Firstly, the MD simulation results of the tensile stress–
strain curves for the nanotwinned NiCo-based alloys with 30%
precipitates at various temperatures are plotted in Fig. 1(d). It
can be observed that the slope of the curves in the elastic defor-
mation stage decreases with increasing temperature, indicating
that the elastic modulus softens as the temperature rises. Ad-
ditionally, in these stress–strain curves, a marked drop occurs
when the stress reaches its maximum value, known as the yield
stress, with the corresponding strain in the MD simulation de-
ﬁned as the elastic limit strain. It can also be discerned from
Fig. 1(d) that both the elastic limit strain and the yield stress
decrease with rising temperature. On the basis of the MD sim-
ulation results, quantitative analysis of the variations in the
elastic modulus, elastic limit strain, and yield stress with tem-
perature is then conducted, as illustrated in Figs. 2(a) and 2(b).
One can note from the ﬁgures that the elastic modulus con-
sistently decreases with escalating temperature, which aligns
with the reports in existing work. [41] Moreover, it can also be
found from Figs. 2(a) and 2(b) that a clear linear decline in
both the elastic limit strain and the yield stress with increasing
temperature is evident. Finally, as depicted in Fig. 1(d), the
stress–strain curves enter a relatively steady plastic deforma-
tion stage, corresponding to the plastic ﬂow stage, following
the attainment of the maximum stress.
0 0.02 0.04 0.06 0.08 0
1
2
3
4
5
6
7
8Stress (GPa) 
Strain (100%) 
 823 K
 923 K
 1023 K
 1123 K
 1223 K
 1323 K
(d) 
z y
Fig. 1. The atomic composition of the MD model in which the substrate is
made up of Ni, Co, and Cr; the circular portion represents the L12 precip-
itates (a). A detailed view of the precipitates in which the red represents
Ni atoms and the white represents Al atoms (b). A lattice schematic of
the alloy, wherein the green signiﬁes the FCC structure; a single layer
of red atoms represents twin boundaries (TB); the precipitate region is
highlighted with brighter atoms, maintaining the FCC structure (c). The
simulated stress–strain curves under tensile loading across a temperature
range from 823 K to 1323 K (d).
To analyze the intrinsic mechanism behind the decrease
in yield stress of the nanotwinned NiCo-based alloys with L12
nano-precipitates as the temperature increases, it can be recog-
nized that in the MD simulations, the beginning of the yielding
regime is associated with the generation of a certain volume of
defects prior to plastic ﬂow. In the yielding regime, during ten-
sile simulations, one can primarily observe two types of defect
formations: one is the formation of stacking faults, exempli-
ﬁed by the multiple layers of red atoms seen in Figs. 2(c) and
2(d); the other is the transformation of FCC crystal atoms into
disordered atoms, represented by the white amorphous clusters
in Figs. 2(e) and 2(f). To quantify the relationship between de-
fects and yield stress, one can statistically assess the volumet-
ric fraction of defective atoms present at the moment of yield-
ing. Since the pre-existing amorphous atoms from the high-
temperature environment do not inﬂuence the assessment, the
number of disordered atoms can be subtracted before tension
116201-2

## Page 4

Chin. Phys. B 33, 116201 (2024)
from the total defect count at the point of yielding. Thereby,
ﬁgure 2(b) shows the relationship between the temperature and
the fraction of defective atoms produced at yielding, compared
with the curve for the variation of yield strength with respect
to the temperature. From the ﬁgure, it can be observed that as
the temperature rises, the fraction of defective atoms increases
concurrently with a decrease in yield stress. Hence, during
high-temperature tensile processes, it becomes easier for de-
fects to form, and the increased generation of these defects
leads to a lower yield stress in the alloys.
823 923 1023 1123 1223 1323 
120 
125 
130 
135 
140 
145 
150 
Elastic modulus (GPa)
Temperature (K) 
(a) 
823 923 1023 1123 1223 1323 
4.5 
5.0 
5.5 
6.0 
6.5 
7.0 
7.5 
8.0 
Yield stress
Atomic fraction of nucleated defects 
Temperature (K) 
Yield stress (GPa) 
0.02 
0.04 
0.06 
0.08 
0.10 
0.12 
0.14 
0.16 
0.18 
Atomic fraction of nucleated
 defects (100%) 
(b)
Fig. 2. The elastic modulus and elastic limit strain of the nanotwinned NiCo-based alloys with nano-precipitates varying with the temperature in
the MD simulations (a); the yield stress of the nanotwinned NiCo-based alloys with nano-precipitates and the fraction of defect-forming atoms
around the yielding point as functions of the temperatures (b); two primary types of defects that emerge upon yielding in the alloy (c)–(f). In
(c) and (d), the red atoms represent dislocation-type defects, where (d) is a schematic of the stacking faults without the background FCC (green)
atoms. In (e) and (f), the white-colored atoms indicate the structure where some atoms have transformed into an amorphous state, with (f)
illustrating the matrix atoms removed from the FCC (green) background in (e). The vertical single-layer of red atoms represents the TBs.
Meanwhile, the mean ﬂow stresses of the nanotwinned
NiCo-based alloys with L1 2 nano-precipitates in the range of
2% plastic strain are calculated for different temperatures, as
shown in curve II in Fig. 3. It can be noted from the ﬁgure
that the ﬂow stress gradually decreases as the temperature rises
from 823 K to 1323K, with a plateau region observed when
the temperature increases from 923 K to 1023 K. A further in-
crease in temperature leads to a subsequent drop in the ﬂow
stress. Since the ﬂow stress in materials is directly propor-
tional to the density of full dislocations, as described by the
Taylor model,[13] the dislocation density in the range of 2%
plastic strain is examined to obtain the mean dislocation den-
sity, presented as curve I in Fig. 3. Here, it is apparent that the
ﬂow stress and mean dislocation density follow a similar trend
as the temperature increases. Additionally, the variations of
the ﬂow stress with temperature for both nanotwinned NiCo-
based alloys with and without nano-precipitates are plotted as
curves II and III in Fig. 3, respectively. It can be discovered
from the ﬁgure that the strengthening effects of the L1 2 nano-
precipitates become remarkable with increasing temperature.
This suggests that, even at high temperatures, the L1 2 nano-
precipitates are able to keep hindering the movement of dislo-
cations within the twin boundaries. With both precipitates and
twin boundaries impeding dislocation motion, the synergistic
strengthening behavior arises by accumulating more disloca-
tions within the alloy.
823 923 1023 1123 1223 13231.6
1.8
2.0
2.2
2.4
2.6 Nanotwin with nano-precipitates 
Nanotwin without nano-precipitates 
Flow stress (GPa) 
Dislocation density (1013 cm-2)
Temperature (K) 
I.
II.
III.
1.9
2.0
2.1
2.2
2.3
2.4
Fig. 3. The correlation between the average dislocation density and
temperature during the ﬂow stress stage is given in curve (I), compared
with the average ﬂow stress varying with the temperature in nanotwinned
NiCo-based alloys with nano-precipitates in curve (II). The relationship
between the average ﬂow stress and temperature in nanotwinned NiCo-
based alloys without precipitates is given in curve (III), serving as a com-
parison against those with precipitates.
116201-3

## Page 5

Chin. Phys. B 33, 116201 (2024)
Similar to the mechanisms observed at room temperature,
there are two main modes of interaction between dislocations
and precipitates: the wrapping mechanism, and the cutting
mechanism. Figures 4(a)–4(c) show the wrapping mechanism
observed during deformation at the temperature of 823 K. It
is evident that the dislocations form distinct rings around the
precipitates without further spreading, as shown in Fig. 4(c).
At this point, the interior of the precipitates remains clean with
no dislocations, while external dislocations are pinned outside
the precipitate due to the presence of the ring-shaped disloca-
tions, as seen in Fig. 4(b). This mechanism can increase the
dislocation density within the twins to enhance the strength.
Figures 4(d)–4(f) present the cutting mechanism observed dur-
ing deformation at 923 K. It is equally clear from Fig. 4(e) that
the dislocations cut into the precipitates and get pinned inside
them. Unlike the wrapping mechanism, numerous dislocations
are trapped within the precipitates in this case: see Fig. 4(f).
Since the TBs within the precipitate also create obstacles to
prevent the dislocation movement, there is still the pinning ef-
fect once the dislocation enters the precipitate. This could lead
to an overall increase in the dislocation density within the nan-
otwinned NiCo-based alloys, thus augmenting the ﬂow stress
and making the material stronger.
Fig. 4. The CNA analysis of the wrapping mechanism of precipitates un-
der the temperature of 823 K, where (b) corresponds to the dashed area
in (a), and (c) is the DXA analysis for (b). The CNA analysis of the cut-
ting mechanism of precipitates under the temperature of 923 K where (e)
corresponds to the dashed area in (d), and (f) is the DXA analysis for (e).
Figure 5 presents the dislocation distributions of nan-
otwinned NiCo-based alloys with nano-precipitates at temper-
atures of 823 K, 1023 K, and 1323 K, respectively, when the
plastic strain is 1%. It can be found from the ﬁgure that the
overall number of dislocations visibly declines as the temper-
ature rises, corresponding to the decreasing overall ﬂow stress.
One can also observe that the wrapping mechanism becomes
increasingly prevalent, while the cutting mechanism dimin-
ishes with increasing temperature. This is because, at higher
temperatures, the L1 2 precipitates exert a stronger inhibitory
effect on dislocation movement relative to the twin boundaries.
According to Fig. 3, despite the downward trend of the over-
all ﬂow stress between 823 K and 1323 K, the strengthening
effect of the L12 precipitates becomes more pronounced. This
enhanced reinforcement is attributed to the more prominent
strengthening role played by the wrapping mechanism around
the precipitates, as shown in Fig. 5. Therefore, it can be con-
cluded that within the temperature range of 823 K to 1323 K,
the synergistic strengthening behavior occurs as a result of the
nano-precipitates and nanotwins in NiCo-based alloys.
Fig. 5. The dislocation distributions in nanotwinned NiCo-based alloys
with nano-precipitates after 1% plastic strain at the temperatures of 823 K
(a), 1023 K (b), and 1323 K (c).
3.2. Mechanical performance with various sizes and vol-
ume fractions of microstructures
Since the geometrical size and volume fraction of mi-
crostructures can affect the mechanical performance of nanos-
tructured metallic materials signiﬁcantly, [42–46] further MD
simulations are conducted to explore the high-temperature me-
chanical performance of nanotwinned NiCo-based alloys with
nano-precipitates for various sizes and volume fractions of
nanotwins and nano-precipitates. Figure 6 shows the effect
of the volume fraction of nano-precipitates on the mechanical
performance of nanotwinned NiCo-based alloy at high tem-
peratures. The stress–strain curves for the volume fractions of
10% and 20% are plotted in Figs. 6(a) and 6(b), respectively.
By combining with Fig. 1(d), one can obtain the yield stress
and ﬂow stress varying with temperature for different volume
fractions of nano-precipitates, as presented in Figs. 6(c) and
6(d), respectively. It is found in the ﬁgures that both the yield
stress and ﬂow stress are weakened as the temperature in-
creases, and the volume fraction can change the dependence
of these mechanical properties on temperature. In Fig. 6(c),
it can be observed that up to 1023 K, the changes in the yield
stress with volume fractions are not signiﬁcant. With a further
increase in temperature, the dependence of the yield stress on
the volume fraction becomes more pronounced at higher tem-
peratures. In Fig. 6(d), within the temperature range of 823 K
to 1323 K, one can see that as the volume fraction of the pre-
cipitates decreases, the ﬂow stress increases. Additionally, the
ﬂow stress becomes more sensitive to the temperature in the
lower volume fraction of nano-precipitates.
The high-temperature mechanical properties of nan-
otwinned NiCo-based alloys for different sizes of nano-
precipitates are also simulated and plotted in Fig. 7. The
stress–strain curves for the nano-precipitate diameters of 3 nm
and 9 nm are given in Figs. 7(a) and 7(b), respectively. Sim-
ilarly, by combining with Fig. 1(d), one can achieve the yield
stress and ﬂow stress of nanotwinned NiCo-based alloys as
116201-4

## Page 6

Chin. Phys. B 33, 116201 (2024)
0 0.02 0.04 0.06 0.080
1
2
3
4
5
6
7
8
Stress (GPa) 
Strain (100%)
 823 K
 1023 K
 1223 K
 1323 K
(a) Volume fraction - 10%
0 0.02 0.04 0.06 0.080
2
4
6
8
Stress (GPa) 
Strain (100%)
 823 K
 1023 K
 1223 K
 1323 K
(b) Volume fraction - 20%
823 1023 1223 1323
4.5
5.0
5.5
6.0
6.5
7.0
7.5
 10%
 20%
 30%
Yeild stress (GPa) 
Temperature (K) 
(c)
823 1023 1223 1323
2.0
2.4
2.8
3.2
 10%
 20%
 30%
Flow stress (GPa) 
Temperature (K) 
(d)
Fig. 6. The stress–strain curves for the volume fractions of Ni 3Al nano-precipitates of 10% (a) and 20% (b), and the yield stress (c) and ﬂow
stress (d) varying with the temperature for the volume fractions of Ni3Al nano-precipitates of 10%, 20%, and 30%.
0 0.02 0.04 0.06 0.080
2
4
6
8
Stress (GPa) 
Strain (100%)
823 K
1023 K
1223 K
1323 K
(a) Nano-precipitates - 3 nm
0 0.02 0.04 0.06 0.080
1
2
3
4
5
6
Stress (GPa) 
Strain (100%)
823 K
1023 K
1223 K
1323 K
(b) Nano-precipitates - 9 nm
823 1023 1223 1323
4
5
6
7
8
NP - 3 nm
NP - 6 nm
NP - 9 nm
Yeild stress (GPa) 
Temperature (K) 
(c)
823 1023 1223 1323
2.0
2.4
2.8
3.2 NP - 3 nm
NP - 6 nm
NP - 9 nm
Flow stress (GPa) 
Temperature (K) 
(d)
Fig. 7. The stress–strain curves for the diameters of Ni3Al nano-precipitates of 3 nm (a) and 9 nm (b), and the yield stress (c) and ﬂow stress (d)
varying with the temperature in the Ni3Al nano-precipitates of 3 nm, 6 nm and 9 nm.
116201-5

## Page 7

Chin. Phys. B 33, 116201 (2024)
0 0.02 0.04 0.060
1
2
3
4
5
6
7
Stress (GPa) 
Strain (100%)
 823 K
 1023 K
 1223 K
 1323 K
(a) Nano-twin spacing - 8 nm
0 0.02 0.04 0.06 0.080
1
2
3
4
5
6
7
8
Stress (GPa) 
Strain (100%)
 823 K
 1023 K
 1223 K
 1323 K
(b) Nano-twin spacing - 14.8 nm
823 1023 1223 1323
4
5
6
7
 NT - 8 nm
 NT - 11.7 nm
 NT - 14.8 nm
Yeild stress (GPa) 
Temperature (K) 
(c)
823 1023 1223 1323
1.8
2.1
2.4
2.7
3.0 NT - 8 nm
 NT 11.7 nm
 NT - 14.8 nm
Flow stress (GPa) 
Temperature (K) 
(d)
Fig. 8. The stress–strain curves for the twin spacing of 8 nm (a) and 14.8 nm (b) with the volume fraction of 6 nm-Ni 3Al nano-precipitates, and
the yield stress (c) and ﬂow stress (d) varying with temperature for the twin spacings of 8 nm, 11.7 nm and 14.8 nm.
functions of temperature for different nano-precipitate sizes,
as shown in Figs. 7(c) and 7(d), respectively. It can be seen
in Fig. 7(c) that within the temperature range of 823 K to
1323 K, the yield stress decreases as the size of the precipi-
tates increases. In Fig. 7(d), one can ﬁnd that the ﬂow stress
is the highest for the precipitate size of 3 nm, is the lowest for
6 nm, and then rises slightly for 9 nm. This is because the vol-
ume fraction of 3 nm sized nano-precipitates is much lower
than those for the 6 nm and 9 nm sized nano-precipitates,
leading to the higher ﬂow stress, as shown in Fig. 6(d). It
can also be suggested from Fig. 7(d) that there should be a
critical diameter of precipitates between 3 nm and 9 nm to
achieve the minimum ﬂow stress in nanotwinned NiCo-based
alloys for a given twin spacing. Figure 8 further discusses
the inﬂuence of twin spacing on the high-temperature me-
chanical properties of nanotwinned NiCo-based alloys with
nano-precipitates. Figures 8(a) and 8(b) depict the stress–
strain curves of nanotwinned NiCo-based alloys with nano-
precipitates for the twin spacings of 8 nm and 14.8 nm, respec-
tively. Then, one can obtain the yield stress and ﬂow stress
varying with the temperature for different twin spacings by
combining Figs. 1(d), 8(a) and 8(b). It can be seen in Fig. 8(c)
that within the temperature range of 823 K to 1323 K, the yield
stress of the alloys also increases as the twin spacing increases.
Conversely, it is clearly shown in Fig. 8(d) that the ﬂow stress
decreases as the twin spacing increases. This aligns with the
well-established phenomenon that the strengthening effect in-
creases as the twin spacing decreases due to the excellent ther-
mal stability of nanotwins.[47,48]
4. Conclusion
In summary, atomic simulations were performed to moni-
tor the effects of nanotwins and nano-precipitates on the high-
temperature mechanical properties and strengthening mecha-
nisms in NiCo-based alloys. The molecular dynamic simula-
tions revealed that the proliferation of defective atoms at the
onset of yielding makes the yield stress decrease when the
temperature increases. The decrement of the ﬂow stress in
nanotwinned NiCo-based alloys with nano-precipitates with
the higher temperature comes from the variation of disloca-
tion density with the temperature. Furthermore, the nano-
precipitates could enhance the high-temperature strengthen-
ing behavior in nanotwinned NiCo-based alloys. This stems
from the dislocation interactions with both the nanotwins and
the nano-precipitates, including the wrapping and cutting be-
havior of dislocations. As the temperature increases, the ten-
116201-6

## Page 8

Chin. Phys. B 33, 116201 (2024)
dency for dislocation wrapping increases while cutting activ-
ity diminishes, suggesting that dislocation wrapping provides
a more pronounced strengthening contribution. The results of
MD simulations also demonstrated that a higher yield stress
can be achieved for a higher volume fraction of precipitates,
a smaller nano-precipitate size and larger twin spacing. En-
hanced ﬂow stress can be obtained for the lower volume frac-
tion of precipitates, the smaller nano-precipitate size and the
smaller twin spacing. The ﬁndings in this work could be help-
ful for the optimization of nanotwins and nano-precipitates
to improve the high-temperature mechanical performance of
NiCo-based alloys.
Acknowledgments
Project supported by the National Natural Science Foun-
dation of China (Grant No. 12072317) and the Natural Science
Foundation of Zhejiang Province (Grant No. LZ21A020002).
Ligang Sun gratefully acknowledges the support received
from the Guangdong Basic and Applied Basic Research
Foundation (Grant No. 22022A1515011402), the Science,
Technology and Innovation Commission of Shenzhen Mu-
nicipality (Grant No. GXWD20231130102735001), and De-
velopment and Reform Commission of Shenzhen (Grant
No. XMHT20220103004).
References
[1] Juan C C, Tsai M H, Tsai C W, et al. 2015 Intermetallics 62 76
[2] Maresca F and Curtin W A 2020 Acta Mater .182 235
[3] Wang M L, Lu Y P, Lan J G, et al. 2023 Acta Mater .248 118806
[4] Gludovatz B, Hohenwarter A, Catoor D, et al. 2014 Science 345 1153
[5] Gludovatz B, Hohenwarter A, Thurston K V S, et al. 2016 Nat. Comm
7 10602
[6] Diao H Y , Feng R, Dahmen K A and Liaw P K 2017 Curr . Opin. Solid
ST. M. 21 252
[7] Guo Y N, Su H J, Zhou H T, et al. 2022 J. Mater . Sci. Technol.111 298
[8] Wu Z, Bei H, Pharr G M and George E P 2014 Acta Mater .81 428
[9] Schneider M, George E P, Manescau T J, et al. 2020 Int. J. Plasticity
124 155
[10] Verma A, Tarate P, Abhyankar A C, et al. 2019 Scr . Mater .161 28
[11] Li W J and Wang C Y 2020 Chin. Phys. B 29 026102
[12] Zhang Z J, Sheng H W, Wang Z J, et al. 2017 Nat. Commun. 8 14390
[13] Ding L, Hilhorst A, Idrissi H and Jacques P J 2022 Acta Mater . 234
118049
[14] Li Z, Hu Y , Li X, et al. 2023 Compos. Pt. B-Eng. 265 110965
[15] Fan J, Ji X, Fu L, et al. 2022 Int. J. Plasticity 157 103398
[16] Zhu Z Y , Yan S H, Chen H and Gou G Q 2021 Mater . Sci. Eng. A 803
140501
[17] Zhang T W, Ma S G, Zhao D, et al. 2020 Int. J. Plasticity 124 226
[18] Liu X W, Sun L G, Zhu L L, et al. 2018 Acta Mater .149 397
[19] Chen A Y , Zhu L L, Sun L G, et al. 2019 Nat. Comm. 10 1403
[20] Wu G, Chan K C, Zhu L L, Sun L G and Lu J 2017 Nature 545 80
[21] Chen G, Peng Y , Zheng G, et al. 2016 Nat. Mater .15 876
[22] Edwards T E J, Rohbeck N, Husz ´ar E, et al. 2022 Adv. Sci. 9 2203544
[23] He X, Xu Z Y and Ni Y S 2024 Chin. Phys. B 33 016201
[24] Barrett C D, Tschopp M A and El Kadiri H 2012 Scr . Mater .66 666
[25] An M R, Song H Y and Su J F 2012 Chin. Phys. B 21 106202
[26] Zhang Z Y , Wang B, Huang S L, et al. 2016 Mater . Des.106 313
[27] Fan H D, Zhu Y X, El-Awady J A and Raabe D 2018 Int. J. Plasticity
106 186
[28] Chen Y , Fang Q, Luo S, et al. 2022 Int. J. Plasticity 155 103333
[29] Zhu L, Ruan H, Li X, et al. 2011 Acta Mater .59 5544
[30] Tian Y Y , Luo G J, Fang Q H, Li J and Peng J 2022 Chin. Phys. B 31
066204
[31] Sun Z H, Zhang J, Xin G X, et al. 2022 Intermetallics 142 107444
[32] Afkham Y , Bahramyan M, Mousavian R T and Brabazon D 2017
Mater . Sci. Eng. A698 143
[33] Xie L, Brault P, Thomann A L, Bauchire J M, et al. 2013 Appl. Surf.
Sci. 285 810
[34] Liu J 2020 Phys. Lett. A 384 126516
[35] Zhang H, Ren Z Y , Tong Y G, et al. 2023 J. Mater . Sci. Technol. 156
172
[36] Zhang H, Tong Y G, Cao S H, et al. 2022 J. Alloys Compd. 919 165715
[37] Liu L Y , Zhang Y , Ma J M,et al. 2022 Scr . Mater .217 114771
[38] Thompson A P, Aktulga H M, et al. 2022 Comput. Phys. Commun. 271
108171
[39] Farkas D and Caro A 2020 J. Mater . Res.35 3031
[40] Zhang J, Ma S H, Xiong Y X, et al. 2021 Acta Mater .219 117238
[41] Liu R G, Tang J, Jiang J X, et al. 2022 Extreme Mech. Lett. 56 101875
[42] Sun L G, Wu G, Wang Q and Lu J 2020 Mater . Today38 114
[43] An M R, Lei Y F, Su M J, et al. 2023 Chin. Phys. B 32 066201
[44] Jiao L, Zhu L, Gan B, et al. 2023 Mech. Mater .186 104806
[45] Zhou M, Wang W, Su H J, et al. 2024 Chin. Phys. B 33 056501
[46] Xing R L and Liu X P 2024 Chin. Phys. B 33 016202
[47] Zhang B B, Yan F K, Zhao M J, et al. 2018 Acta Mater .151 310
[48] Sun L G, Li D, Zhu L, et al. 2020 Int. J. Plasticity 128 102685
116201-7
