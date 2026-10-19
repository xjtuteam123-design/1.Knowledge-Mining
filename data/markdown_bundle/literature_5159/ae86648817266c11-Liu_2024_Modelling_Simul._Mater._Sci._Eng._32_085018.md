# Liu_2024_Modelling_Simul._Mater._Sci._Eng._32_085018

<!-- source: D:\总文献\Liu_2024_Modelling_Simul._Mater._Sci._Eng._32_085018.pdf -->
<!-- file_sha256: 383e182c67caddb7bd00aeb24e10f97fce2e5023ef9f954698f4abf434edea82 -->

## Page 1

Modelling and
Simulation in Materials
Science and
Engineering
      
PAPER • OPEN ACCESS
Strengthening by {110} and {112} edge
dislocations in BCC high entropy alloys
To cite this article: Xin Liu et al 2024 Modelling Simul. Mater. Sci. Eng. 32 085018
 
View the article online for updates and enhancements.
You may also like
An atomistic K-test framework for general
grain boundaries and triclinic single
crystals
F Brunner, P Andric and F Maresca
-
An affine formulation of eigenstrain-based
homogenization method and its application
to polycrystal plasticity
Aslan Nasirov and Caglar Oskay
-
Crystal plasticity based constitutive model
for deformation in metastable titanium
alloys
P Christie, M A Siddiq, U B Asim et al.
-
This content was downloaded from IP address 202.200.234.50 on 27/11/2025 at 07:53

## Page 2

Modelling and Simulation in Materials Science and Engineering
Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 (23pp) https://doi.org/10.1088/1361 -651X/ad8ada
Strengthening by {110} and {112} edge
dislocations in BCC high entropy alloys
Xin Liu 1,∗, Rui Barreira 2,3, M Rahbar Niazi 1
and W A Curtin 1,2
1 Laboratory for Multiscale Mechanics Modeling, ´Ecole Polytechnique Fédérale de
Lausanne, Lausanne 1015, Switzerland
2 School of Engineering, Brown University, Providence, RI 02912, United States of
America
3 Artificial Intelligence in Mechanics and Manufacturing, ETH Zürich, Zurich
8005, Switzerland
E-mail: xin.liu@epfl.ch
Received 19 August 2024; revised 16 October 2024
Accepted for publication 24 October 2024
Published 6 November 2024
Abstract
Mechanical tests and microscopy studies on body-centered cubic (BCC) high
entropy alloys reveal transitions from screw to edge dislocation slip and from
{110} to {112} slip plane activity. Here, a strengthening theory for BCC edge
dislocation slip on {112} planes is thus developed that parallels a recent theory
for {110} slip. Using the atomistic dislocation pressure fields for four BCC
elements (Nb, Ta, Mo, W) as proxies to span the range of likely alloy cores,
theory predicts that the zero temperature yield strength for {112} slip is slightly
lower (0%–20%) than that for {110} slip but that the associated energy barrier
is slightly (0%–20%) higher. This leads to cancelling effects, and hence very
similar strengths, at finite temperatures and strain rates. Full atomistic results
on selected dilute binary alloys show some shifts in these trends, but with
similar magnitudes and cancelling effects. The close strengths of {110} and
{112} slip modes indicate that subtle aspects beyond the scope of the theory
will determine which slip system controls the observed strengthening. This
∗
Author to whom any correspondence should be addressed.
Original Content from this work may be used under the terms of the Creative Commons Attribution
4.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the
title of the work, journal citation and DOI.
© 2024 The Author(s). Published by IOP Publishing Ltd 1

## Page 3

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
closeness in strength cements the use of the {110} edge theory for guiding
alloy design independent of actual slip system.
Keywords: yield strength , high entropy alloys, theory, edge dislocation,
BCC alloys
1 . Introduction
High entropy alloys (HEAs) are multi-component alloys with non-dilute solute concentrations
that maintain a single phase structure. With the emergence of various types of HEAs, refractory
body-centered cubic (BCC) HEAs composed of elements in the Cr–Mo–Nb–V–Ta–W–Hf–
Ti–Zr family have attracted great interest [ 1–6]. Refractory HEAs typically have impressive
mechanical properties such as high room temperature yield strength and strength retention at
very high temperatures [ 3, 5, 7–9] that are necessary for applications in power generation,
aerospace engines, and other technologies but often with insufficient ductility and/or fracture
toughness. A major goal is thus to identify new alloys with the balance of strength and ductility
needed for applications.
The origins of the high strength are well understood in terms of general solid-solution
strengthening theories [ 6, 10–15]. In dilute solid-solution alloys, strengthening is due to a
low concentration of alloying elements have large misfits relative to the matrix element. In
HEAs, in contrast, all elemental components have misfits relative to the average lattice con-
stant and so HEAs are 100% solute-strengthened albeit with smaller misfits. However, overall
strengthening in HEAs is significant. Theories have now been developed for both (i) edge dis-
locations in both FCC and BCC crystals [6, 10, 11, 14, 15] and (ii) screw dislocations for BCC
crystals [12–14]. Of interest here is the edge dislocation theory, which postulates that solute-
dislocation interactions drive edge dislocations to become wavy as dislocation segments find
local favorable solute fluctuations that pin the segments. A combination of resolved shear
stress and temperature is then required to drive thermally-activated dislocation glide of these
segments out of their local minima. While it is well-known that screw dislocation motion con-
trols the yield strength and flow behavior in elemental BCC metals and dilute BCC alloys, due
to the very compact screw core, but recent research suggest that edge dislocation strengthen-
ing is increasingly competitive with screw strength and may control strength in BCC HEAs
with large solute misfit parameters [ 16–18]. TEM observations in a few alloys have reported
a prevalence of non-screw dislocations [ 15, 19], supporting the theoretical concept.
Deformation in BCC alloys is understood to occur predominantly by dislocations with
Burgers vectors 1/2 ⟨111⟩ and most typically gliding on {110} planes. However, non-{110}
slip is known to arise in some BCC metals and dilute alloys, and more recently has been seen
in medium entropy alloys (MEAs) [19]. The competition between {110} and {112} slip is typ-
ically examined in the context of screw dislocations because the compact screw core in BCC
metals can glide, in principle, on any crystalline slip plane containing the 1/2 ⟨111⟩ Burgers
vector. Recent work on BCC alloys proposes that alloying can drive a change in core structure
from a non-degenerate core to a degenerate core, with a concomitant change in slip from the
{110} to the {112} planes [ 20]. Nonetheless, since screw motion on different planes is always
feasible, the study of edge dislocations gliding on different planes becomes relevant. It is then
possible that, in some alloys, edge dislocations control strength and that {112} slip is preferred
over {110} slip. Recent room temperature studies on polycrystals and micropillars have shown
that {112} slip is preferred in TiZrNbHfTa but dominated by screw dislocations while {110}
and {112} slip can be observed in MoNbTaVW with a mixture of edge and screw dislocations
[21]. Application of {110} edge theory has previously predicted the measured tensile yield
2

## Page 4

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
strengths in both alloys [ 6, 22] in good agreement with experiments. In light of recent results
suggesting {112} slip to be competitive with {110} slip, we develop the theory for strength-
ening of edge dislocations gliding on {112} using the same framework as previously used for
glide on {110} in HEAs.
A key concept in the theory is the existence of an ‘average atom’ [ 23] that is a single hypo-
thetical atom that, when put into the same crystal structure as the HEA, has the same average
material properties (e.g. elastic constants, lattice constants, stacking fault energies, etc) as the
true random alloy but without the randomness, as shown in figures 1(a) and (b). The average
dislocation core structure can then be created in this ‘average alloy’ (figure 1(c)). Each of the
n elements within an n-component HEA can then be considered as a solute in the ‘average
atom’ matrix, with misfit volume ∆V n. The interaction energy between a solute and a disloca-
tion in the average alloy can also be determined at every atomic position around the dislocation
(figures 1(d)–(f)). The pressure field p(x, y) around the average alloy dislocation core can also
be computed (figure 1(g)), and then the solute-dislocation interaction energy at each atomistic
point (x, y) can be approximated as −p(x, y)∆Vn (figures 1(h)–(j)). The elasticity approxim-
ation is not exact, and so the difference between the full interaction energy and the elastic
approximation, called the ‘chemical’ interaction energy by Maresca and Curtin [ 6], is the dif-
ference between these two (figures 1(k)–(m)). Explicit creation of an interatomic ‘average
atom’ potential has been demonstrated for EAM potentials, but it is the conceptual framework
that is important. Results in figure 1 are shown for the equiatomic NbTaV alloy using the Zhou
et al interatomic potentials [24] but the approach is generic and conceptual.
In this work, we use the elasticity theory as the basis for comparing {110} and {112}
slip, and hence we require average dislocation core structures (figure 1(c)) and pressure fields
(figure 1(g)). Since the dislocation core structures and pressure fields depend predominantly
on the alloy elastic constants and unstable stacking fault energy (USFE), we use the disloca-
tion cores in four elemental metal (Nb, Ta, Mo, W) as proxies for the average core structures
of multicomponent alloys spanning a range of potential core structures (range of elastic con-
stants and USFEs). Our results would also apply to dilute alloys of Nb, Ta, Mo, and W, but that
is not the purpose of the study. Furthermore, while it is possible to create dislocation in the true
random multicomponent alloy using suitable interatomic potentials (see, for example, [ 6, 19,
22, 25–28]), it is not possible to extract the solute-dislocation interaction energies because the
dislocations have already responded to the precise local solute configurations in any one real-
ization of the random alloy. The motion of dislocations in a random alloy can also be studied
by direct atomistic simulations, but such simulations must be done (i) at precise length scales
dictated by theory or very long (and hence costly) lengths, (ii) always over many sample real-
izations to obtain statistically reliable results, and (iii) for each alloy composition of interest.
Such brute-force investigation does not reveal intrinsic understanding nor enable any predic-
tions of behavior of new alloys.
With the above sketch of the conceptual framework, we proceed with the analysis as
follows. We first show that the elastic and core energies for both 1/2 ⟨111⟩{110} and
1/2⟨111⟩{112} edge dislocations are very similar, using two different interatomic potentials
for Nb, Ta, Mo, and W. Then, within the limit of elasticity theory, we show that the com-
petition in slip between {112} and {110} depends only on the two different dislocation core
structures and, specifically, on their non-dimensional pressure fields. Using the atomistic res-
ults on the proxy materials (elemental Nb, Ta, Mo, W), we are able to assess variations in {112}
versus {110} strengthening across possible BCC alloys having very different elastic moduli
and unstable stacking fault energies. We find the ratios of both the T = 0 K critical resolved
shear stress (CRSS) and the energy barrier for dislocation motion to be close to unity across
all alloys, with the {112} CRSS being lower by at most 20% and the barrier being higher by
3

## Page 5

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure 1 . Schematic of conceptual framework for HEA modeling. The average alloy
(b) is obtained from the real random alloy (a); (c) an edge dislocation is inserted into
the average alloy; (d)–(f) solute-dislocation interaction energies Un
sd(x, y) for all solute
types n at all atomic positions are computed for the average alloy dislocation core; (g) the
pressure field p(x, y) at each atom in/around the average alloy dislocation is computed;
(h)–(j) the elastic approximation to the solute-dislocation interaction energy is computed
using solute misfits and the average alloy pressure field; (k)–(m) the difference between
the total solute-dislocation interaction energy (parts (d)–(f)) and the elasticity approx-
imation (parts (h)–(j)) is the ‘chemical’ contribution to the solute-dislocation interaction
energy.
4

## Page 6

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
at most 20%. Moving beyond elasticity, we introduce explicit atomistic solutes into some of
our proxy matrix materials and examine the strength predictions further, again conclude that
{112} and {110} strengths are close.
The remainder of this paper is organized as follows. In section 2, we examine the elastic
and core energies of the relevant edge dislocations. In section 3, we review the theory for alloy
strengthening in the elasticity limit, highlighting the differences between {110} and {112} slip.
In section 4, we briefly examine the effect of the chemical energy in the context of ‘solutes in
the average alloy’. In section 5, we summarize our findings. Several Appendices present the
full alloy strengthening theory, validation studies of the interatomic potentials, and additional
data.
2. {110} and {112} dislocation energies
The predominance of {110} slip or {112} slip could depend, in principle, on the relative total
dislocation energies. Although the Burgers vector b and anisotropic elastic constants ( C11,
C12, C44) are the same for both slip systems, the long-range elastic energy and the dislocation
core energy could differ between {110} and {112} dislocations. The screw dislocation core is
compact and degenerate, and so the elastic and core energies are identical for all possible slip
systems. Thus, any significant differences in the edge dislocation energies might determine
which slip system is dominant. The elastic and core energies also determine the line tension
that plays a role in edge strengthening. We have thus examined the total energies for the {110}
and {112} cores in our proxy systems of Nb, Ta, Mo, and W using two different interatomic
potentials, the machine-learning SNAP [ 29] and the EAM Zhou et al [24] potentials. The
SNAP potentials are trained on first-principles density functional theory (DFT) data while the
EAM potentials are fit mainly to experimental lattice and elastic properties. Relevant properties
of SNAP potentials for Nb, Ta, Mo, and W are shown in appendix A with comparisons to
experiments or first-principles DFT.
To measure the dislocation energies, we follow the procedure discussed recently in Hu
et al [30, 31]. First, a dislocation is inserted into a cylindrical simulation cell of radius R ≫
b, with periodicity along the axial line direction, using the continuum anisotropic V olterra
displacement field computing using Stroh theory [ 32]. Second, atoms within 20 Å of the outer
boundary are held fixed at the continuum displacements and all interior atoms are relaxed to
achieve the minimum energy dislocation configuration. The total atomistic dislocation energy
(total energy minus cohesive energy) is then computed within cylinders of radius r over the
range b < r < R. Theory predicts that the total energy for r outside of some core region can be
represented as
Etot (r) = K ln
 r
b

+ Ecore (b) (1)
where K is the Stroh anisotropic elastic coefficient for the elastic energy and Ecore(b) is ‘the
core’ energy measured at the arbitrary but convenient reference length b. No identification of
‘the core’ is needed although deviations of the atomistic energy away from the elasticity scaling
of Etot(r) are indicative of ‘the core’ (inelastic) region. However, the competition between
{110} and {112} dislocations lies in the total energy at large r, which is fully characterized by
K and Ecore(b).
Figure 2 shows the total energy Etot(r) versus r/b for Nb, Ta, Mo, and W, as computed
using both potentials and both types of edge dislocations. The SNAP results for Nb stand
out as unusual and will be discussed below. Table 1 shows the Stroh K factors and effective
core energy Ecore(b) for each case. Of importance here is that, for each element and each
5

## Page 7

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure 2. Total dislocation energyEtot(r) versus r/b for Nb, Ta, Mo, and W, as computed
using SNAP and EAM Zhou et al for {110} and {112} edge dislocations. The black
dash line shows the linear fit with Stroh theoretical K computed using SNAP Nb elastic
constants.
Table 1 . Stroh elastic K (GPa) factors and effective core energy Ecore(b) (eV Å−1) for
Nb, Ta, Mo, and W as computed using SNAP and EAM Zhou et al for {110} and {112}
edge dislocations.
Nb Ta Mo W
{112} {110} {112} {110} {112} {110} {112} {110}
K (EAM) 73.13 72.40 106.7 106.0 175.3 175.0 222.4 222.4
Ecore(b) (EAM) 0.292 0.270 0.440 0.394 0.630 0.596 0.781 0.735
K (SNAP) 63.26 58.56 92.80 92.56 157.2 156.8 239.6 239.3
Ecore(b) (SNAP) −0.437 −0.345 0.429 0.426 0.609 0.574 0.741 0.713
potential, the {110} and {112} K coefficients are nearly identical so that the long-range elastic
energy is increasing at essentially the same rate. The small differences arise only due to the
elastic anisotropy. The differences between {110} and {112} energies are thus almost entirely
determined by Ecore(b). In all cases, Ecore(b) for {112} is slightly higher ( ∼30 meV Å−1) than
for {110}, corresponding to the near-constant offset in total energies observed at larger. While
∼30 meV Å−1 is not negligible, the typical total wavy dislocation energies in alloys, due to
the presence of solutes (see below), will be lower than the pure elemental energies and can
shift the relative energies of {110} and {112} by comparable amounts. From these results for
the total energy, and recalling that the screw energy is independent of slip plane, we conclude
that the core energy differences between {110} and {112} are not expected to determine the
slip preference in BCC alloys.
6

## Page 8

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
A close examination of Etot(r) for the {112} dislocation as described by the Zhou et al
potential shows a small but distinct jump in energy around r/b = 2. The Zhou et al {112}
core structures also appear to have more abrupt local atomistic shifts than the SNAP cores
(not shown here). These features have some effects on predictions of strengthening and so our
studies of strengthening in this paper focus on the SNAP potentials.
However, the SNAP Nb potential predicts a very unusual, and unphysical,Etot(r) at small to
intermediate distances for both {110} and {112} dislocations. Unlike all other cases, including
the Zhou et al Nb dislocations, after an initial energy increase at small r/b the energy then
increases very gradually out to at least r/b = 30, far from ‘the core’ region of all other cases.
Only at distances of r/b ≈ 100 is the elastic scaling approached (dashed line). These results are
not an artifact of the simulation method, geometry, or cell size. Both DFT and, hence, the SNAP
potential predict a very small C44 relative to experiments (see appendix A). It may be the case
that the SNAP Nb potential is too soft in the non-linear deformation regime beyond the elastic
limit, corresponding to the region outside of the dislocation core. While we compare the Nb
SNAP core to our DFT-computed core in appendix A, the DFT cell size is small and the elastic
displacement field is imposed as a boundary condition over a significant portion of the cell (see
figure A2). Hence, the deviations in energy seen in figure 2 or in any atomic displacements
are not discernible in these small cells. In general, since a machine-learning potential provides
no guarantee of proper behavior outside the domain of training, the observed behavior for Nb
may just reflect an unidentified inaccuracy in the potential even though it was trained on DFT
input. Below, we will nonetheless study the solute strengthening using the SNAP cores for Nb,
but report some key differences relative to results for Ta, Mo, and W.
3. Strengthening theory of {112} vs. {110} edge dislocations
In a random field of solutes, an initially straight dislocation aligned along z interacts with
local fluctuations in the solute configuration and becomes spontaneously wavy to find regions
of favorable (low energy) solute configurations [ 6]. In the wavy structure, segments of char-
acteristic length ζ c reside in local low-energy minima and face energy barriers, created by
adjacent unfavorable solute environments at a characteristic distance wc. The characteristic
lengths ζ c and wc are derived by minimizing the total dislocation energy. In edge strengthen-
ing theory, the primary solute-edge dislocation interaction Un
sd(xi, yi) is the elastic interaction
between the solute misfit volumes ∆Vn (n = 1, 2, . . .) and the pressure field p(xi, yi) produced
by the dislocation at each (projected) atomic position (xi, yi), Un
sd(xi, yi) ≈ −p(xi, yi)∆Vn (see
figure 1). The pressure field can be written in terms of the average alloy elastic moduli ¯µ, ¯ν
and a dimensionless pressure field f(xi, yi) as p(xi, yi) = − ¯µ
3π
(1+¯ν)
(1−¯ν) f(xi, yi), where the dimen-
sionless pressure field f(xi, yi) depends only on the spreading of the Burgers vector in the glide
plane or, in other words, the dislocation core structure. The full theoretical analysis (see [6, 11]
and appendix B.) for an n-component alloy with composition {cn} then leads to a predicted
T = 0 K shear yield stress τy0 and a zero-stress energy barrier ∆Eb given by
τy0 = π
2
2
4
√
2
Γb10
β
κ
 ¯µ
3π
1 + ¯ν
1 − ¯ν
4 X
n
cn∆V2
n
!23
5
1
3 F 4 (wc) ρ2
Lb7
w5c
 1
3
(2)
and
∆Eb =
"
4
√
2Γb κ
β
 ¯µ
3π
1 + ¯ν
1 − ¯ν
2 X
n
cn∆V2
n
!# 1
3 w2
cF 2 (wc) ρL
b
 1
3
. (3)
7

## Page 9

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Above, F(wc) =
P
i( f(xi + wc, yi) − f(xi, yi))21/2
is the root mean square change in the
dimensionless pressure field when the dislocation glides by the characteristic distance wc (dis-
tance from local minimum energy to local maximum energy), where the characteristic value
wc is the solution of ∂F(w)
∂w = F(w)
2w , leading to F(wc). Also, the sum is over all lattice sites per
periodic unit along the dislocation line, ρL is the atomic line density, and Γ is the line tension.
The ratio β/κ = 1.48 [6] emerges from a statistical analysis of the wavy dislocation. At finite
temperature T, the finite strain-rate flow stress τy(T, ˙ϵ) is then obtained as
τy (T, ˙ϵ) = τy0 exp
"
− 1
0.55
 kT
∆Eb
ln ˙ϵ0
˙ϵ
0.91#
(4)
which is a fit to bridge low- and high- T results with sufficient accuracy [ 6].
In the above formulation, only the dimensionless quantity F(wc) derived from the dimen-
sionless pressure field, the associated wc, and the atomic line density ρL depend on the dislo-
cation core structure and, thus, the dislocation glide plane. Hence, only these quantities differ
between {110} and {112} slip, independent of alloy composition. This is a key insight in our
analysis, making it broadly general across BCC alloys. We can then identify dimensionless
energy barrier and yield strength quantities as
f ∆E =
 w2
cF 2 (wc) ρL
b
 1
3
(5)
and
f τ =
 F 4 (wc) ρ2
Lb7
w5c
 1
3
(6)
and only these quantities differentiate {110} and {112} slip strengthening in a given alloy .
The relative strengths of {110} and {112} edge dislocations thus depend on the respect-
ive atomistic edge dislocation core structures, associated wc, and atomic line densities ( ρL =
1/(2
√
2b) for {110} and ρL = 1/( 2
3
√
6b) for {112}) appearing in f ∆E and f τ . Here, as dis-
cussed in the Introduction, we use the atomistic core structures predicted by the SNAP poten-
tials for the elemental BCC metals Nb, Ta, Mo and W as proxies for the range of possible
reference ‘average alloy’ cores arising in real multicomponent alloys. To verify the accuracy
of the SNAP potentials for these elements, comparisons with DFT reference quantities are
examined in appendix A. We have also validated the SNAP potential versus DFT for the edge
dislocation core structures in pure Nb, Ta and Mo, and compared SNAP to our own DFT-
trained neural network potential [ 33] for W (see appendix A). These four elements span a
wide range of elastic constants and USFE (table A2), which together determine the spreading
of the edge core. We recall the results for the SNAP Nb potential in the previous section, which
suggest this potential is not quantitatively as accurate as those for Ta, Mo and W. Nonetheless,
consistency in results across these elemental core structures would then suggest consistency
across alloys that have elastic constants and USFEs within the (broad) range spanned by these
proxy elements.
The atomistic edge dislocation cores for both {110} and {112} as calculated using the
SNAP potential for Nb, Ta, Mo, and W are shown in figure 3. The atomic core structures are
very similar across all the elements. For visualization purposes, each figure shows the ‘extra’
plane of atoms characteristic of the edge dislocation. Following atomic planes across the core,
the Ta {112} core shows a slightly more pronounced ‘kink’ adjacent to the ‘extra’ plane of
atoms at the very core, but otherwise there are few identifiable differences among the core
structures. In spite of the issues with the Etot(r) at intermediate r/b, the Nb cores appear quite
8

## Page 10

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure 3. Dimensionless pressure field f(xi, yi) of edge dislocations on (a) {110} and (b)
{112} slip planes for pure Nb, Ta, Mo and W as calculated using the SNAP potentials.
For visualization purposes, the ‘extra’ plane of atoms corresponding to the center of the
core is indicated by dashed line.
Table 2. Dimensionless characteristic strength parameters for edge dislocations.
Nb Ta Mo W
{112} {110} {112} {110} {112} {110} {112} {110}
wc/b 3.00 2.67 5.00 4.33 4.00 3.33 4.00 4.00
F(wc) 3.61 4.65 4.03 5.30 3.76 4.58 3.64 4.78
f ∆E 4.16 3.79 6.29 5.71 5.17 4.35 5.07 5.05
f τ 0.64 0.76 0.32 0.40 0.42 0.51 0.40 0.40
∆Eb{112}/∆Eb{110} 1.10 1.10 1.19 1.00
τy0{112}/τy0{110} 0.85 0.79 0.82 1.01
similar to those for Ta, Mo, and W. The colors in figure3 show the dimensionless pressure field
f(xi, yi) computed for each atom in the system. For both {110} and {112} cores, the patterns
of f(xi, yi) are similar across the elements but vary in spatial extent, with Nb showing a more-
localized field and Ta showing the least-localized field.
From the dimensionless pressure field, the dimensionless characteristic energyF(w) is com-
puted as a function of w in the discrete periodic increments along the glide direction ( b/3 for
{110}, b for {112}). The characteristic waviness amplitude wc is then obtained by numeric-
ally solving ∂F(w)
∂w = F(w)
2w . The nearest integer multiple of the increment ( b/3 or b for the two
cases) is taken as wc, as shown in table 2. Because final results, especially τy0, depend notably
on wc, the coarse integer scale of the increments for {112} slip has some effect on the numer-
ical results. In appendix C, we use the numerically-minimized value of wc to understand the
effects of using the nearest integer value of wc. Use of the non-integer value could physically
correspond to a wavy dislocation that can locally adopt either of the integer values around the
non-integer wc. The nearest-integer values of wc across the elements follow the visual spread
of the pressure fields shown in figure 3. Nb has a relatively smaller wc, and this may be related
to the unusual Etot(r) (see figure 2) because the mid-range pressure field is much lower than
9

## Page 11

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
it should be physically, making core effects more important. The wc for Ta {112} slip is lar-
ger than other cases, consistent with the wider pressure distribution possibly connected to the
more-pronounced kinks in the atomic planes to the left of the core center.
In spite of the differences in wc, the resulting values for F(wc) are quite similar across all
the elements, ranging only from 3.61 to 4.03 for {112} slip and 4.58 to 5.30 for {110} slip.
Thus, there is a high degree of consistency across these proxy elements for each slip system
even though the elastic constants and USFE values differ (see appendix A). In addition, the
reduction in total energy per unit length scales as (ρ2
LF 4(wc)/wc)1/3 [15], and the ratio of this
energy between {112} and {110} is very small, differing by at most +4% in Mo and -5%
in Ta. Hence, the energetics of the wavy dislocations in an alloy does not notably favor one
dislocation type over another.
The dimensionless energy barrier f ∆E and dimensionless zero-temperature yield stress f τ
are computed for each core structure using equations ( 5) and ( 6), as shown in table 2. These
quantities involve both F(wc) and wc and so vary more than F(wc) due to the additional role
of wc in the strengthening theory. Most importantly, the ratios of the {112} and {110} energy
barriers and of the zero temperature yield stresses are shown and do not differ significantly.
The ratio of zero-temperature yield stress ranges from 0.85 to 1.01, so that {112} slip is slightly
preferred (lower strength) over {110} slip across all these core structures. The ratio of energy
barriers follows the opposite trend, ranging from 1.0 to 1.19, so that {110} slip has lower
energy barriers. The combination of lowerT = 0 K strength but higher energy barrier for {112}
slip implies (see equation (4)) that the strengths for {112} and {110} will become increasingly
similar with increasing temperature. The same conclusions are obtained using the non-integer
values of wc, which reduce the differences between {110} and {112} for both strengths and
barriers (see appendix C). The close similarity between {110} and {112} slip strengthening is
the main result of this paper.
Here we have assumed that the Peierls stresses for both {110} and {112} slip are negligible
compared to the alloy strengthening. Atomistic studies of the Peierls stress for {110} slip in
BCC elements and ‘average alloys’ show it to be small. In contrast, {112} slip has not been
studied extensively but two studies on pure BCC Fe suggest a rather high Peierls stress [ 34,
35]. So further studies are warranted but beyond the scope of the present paper.
4. Effect of ‘chemical’ energy on strength
The use of elasticity theory enables the analytic study of broad trends in strengthening inde-
pendent of the alloy components (solutes) and composition. As mentioned earlier, ‘chemical’
interactions in the core region also contribute to the solute-dislocation interaction energies
(see figures 1(k)–(m) for a model NbTaV alloy). Examining a range of multicomponent alloys
atomistically using the Zhou et al EAM potentials, Maresca et al found that the {110} chemical
core interactions had a relatively small effect on strengthening. Most importantly, the results
across all alloys could be well-fit to the theoretical form of the elasticity theory with just one
fitting parameter for τy0 and one fitting parameter for ∆Eb. Here, in considering two different
core structures for the {110} and {112} edge dislocations, the chemical core interactions could
differ between the two core structures, leading to larger differences in strengthening.
To probe the role of ‘chemical’ interactions, we have thus examined the atomistic solute-
dislocation interaction energies of Nb in W, Nb in Mo, and W in Ta, again using the SNAP
potentials. Within the framework of HEAs, the W, Mo, and Ta matrices serve as the proxy
‘average atom’ matrices while the Nb and W serve as solutes introduced into these proxy
average alloys. At the same time, since these matrices are actually pure elemental metals,
10

## Page 12

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure 4. Solute-dislocation interaction energy Un
sd(xi, yi) and the ‘chemical correction’
Un
chem(xi, yi) for edge dislocations on (a) {110} and (b) {112} slip planes for W in Ta cal-
culated by SNAP . For visualization purposes, the ‘extra’ plane of atoms corresponding
to the center of the core is indicated by dashed line.
the studied here is also a study of ‘dilute’ alloys of the stated compositions, although that
is not the purpose of the study. In addition, these three cases are chosen because they have
the largest solute misfit volumes and avoid the possibly problematic Nb dislocation core of
the SNAP potential. The total interaction energy Un
sd(xi, yi) and the ‘chemical correction’
Un
chem(xi, yi) = Un
sd(xi, yi) − (−p(xi, yi)∆Vn) are shown in figures 4–6 for each alloy, respect-
ively. The chemical energies are localized to the core region, as expected (as in figures 1(k)–
(m)), and vary across the alloys. For Nb in Mo, the chemical interactions are very small. For
Nb in W and W in Ta, the chemical interactions are comparable to the misfit contributions in
the core. Executing the strengthening analysis using the full interaction energies, we obtain
new values for wc and an effective F(wc), leading to new values for τy0 and ∆Eb as shown
in table 3. A main general feature is a reduction in wc, leading to changes in the subsequent
strength and energy barrier parameters. However, the changes are common to both {110} and
{112} and so the ratios between them are not significantly changed. For Nb in Mo, there are
very modest changes mainly related to the very small change in the integer value of wc for
{110} slip. For Nb in W, the strength ratio increases by ∼10% while the barrier decreases by
a similar factor.
For W in Ta, the differences are much larger, mainly related to the notable decrease in
wc for {112} slip that may be related to the sharper kink feature in the {112} Ta core.
But, as shown in appendix B, in the particular case of W in Ta, using the continuous value
of wc = 3.44 rather than the nearest-integer value wc = 3.0 reduces the predicted strength
ratio considerably, bringing it closer to values for other systems. Finally, for comparison,
Maresca et al show full atomistic results for {110} slip in binary TaW using the Zhou et al
potentials and find differences versus elasticity theory of only ∼ +5% for τy0 and ∼ +10%
for ∆Eb. Hence, the W in Ta results here may be a consequence of the SNAP Ta core
1 1

## Page 13

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure 5. Solute-dislocation interaction energy Un
sd(xi, yi) and the ‘chemical correction’
Un
chem(xi, yi) for edge dislocations on (a) {110} and (b) {112} slip planes for Nb in Mo
calculated by SNAP . For visualization purposes, the ‘extra’ plane of atoms correspond-
ing to the center of the core is indicated by dashed line.
Figure 6. Solute-dislocation interaction energy Un
sd(xi, yi) and the ‘chemical correction’
Un
chem(xi, yi) for edge dislocations on (a) {110} and (b) {112} slip planes for Nb in W
calculated by SNAP . For visualization purposes, the ‘extra’ plane of atoms correspond-
ing to the center of the core is indicated by dashed line.
structures or a difference between the dilute limit here and a concentrated alloy (where solute
differences relative to the average alloy material are reduced as compared to dilute binary
alloys).
12

## Page 14

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Table 3. Dimensionless characteristic strength parameters for edge dislocations in dilute
binary alloys.
W in Ta Nb in Mo Nb in W
{112} {110} {112} {110} {112} {110}
wc/b 3.00 3.67 4.00 3.67 3.00 3.33
F(wc) 6.60 8.21 3.81 4.62 3.58 4.91
f ∆E 6.21 6.84 5.22 4.67 4.13 4.56
f τ 1.43 0.95 0.43 0.44 0.63 0.56
∆Eb{112}/∆Eb{110} 0.91 1.12 0.91
τy0{112}/τy0{110} 1.51 0.96 1.13
These limited studies of the ‘chemical’ effect in the core indicate shifts in the strengths and
barriers to varying degrees. For Nb in Mo there is almost no effect while for W in Ta there
is a large effect on the strength. The detailed changes depend on both the solute and the core
structure. Having compared the SNAP core structures to DFT for Nb, Ta and Mo and another
machine-learning potential for W, the accuracy of those cores relative to the DFT cores are reas-
onably verified. So, we anticipate that, as found by Maresca et al for {110} edge dislocations
using the Zhou et al potentials, core chemical effects may change precise values of strength
and barrier but that the differences between {110} and {112} slip strengths will be comparable
to the results using the generic elasticity model. Considering the elasticity results in table 2 and
the results in table 3 including ‘chemical’ energy contributions, we can broadly conclude that
the {112} strengthening parameters are similar to those for {110}. Typical variations in the
{112}/{110} strength and energy barrier ratios are ±20%, but with opposite trends for the τy0
and ∆Eb in any one alloy system. These opposite trends (higher strength but lower barrier, or
vice-versa) lead to some cancellation of effects at finite temperatures, reducing the net differ-
ence in strengths between {112} and {110} slip. We can expect that, when edge dislocations
control alloy strength, experiments may observe either {112} and {110} slip, or both, but the
alloy strength will not be strongly dependent on the precise slip system.
5. Summary
Based on the edge strengthening theory in BCC HEAs, we have used SNAP potentials to calcu-
late the dimensionless pressure field in pure elemental crystals of Nb, Ta, Mo and W that serve
as proxy edge dislocation cores spanning the range of cores that would arise in real multicom-
ponent alloys. The dimensionless pressure field is determined by the dislocation core structure,
and elasticity theory shows that differences between {110} and {112} strengthening depend
only on the differences in the dimensionless pressure field. From the atomistic dimensionless
pressure fields, we obtained dimensionless energy barrier and zero-temperature yield stress
parameters for each slip system. Comparing the dimensionless quantities for {110} and {112}
slip, we find that the strengthening is very similar. Since any theory is imperfect and since we
find that, in a few cases studied, the inclusion of chemical ‘core’ energies can shift quantitative
results, we do not recommend attempting to distinguish theoretically whether edge dislocation
slip is controlled by {110} or {112} slip in any given alloy. The theoretical strengths are too
similar to unambiguously address such a nuanced issue.
Given our conclusions above regarding the similarity in edge strengthening between {110}
and {112} slip, it is also not useful to attempt any comparisons with experiments. Comparisons
of the {110} edge theory versus experiments have already been made in earlier literature, and
13

## Page 15

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
predictions for {112} slip would not be reliable enough, relative to {110} predictions, to draw
firm conclusions about the dominant slip in any given alloy.
The theory here for BCC HEAs is based on edge dislocation motion. Although screw dis-
location motion is well-established to control the yield strength in elemental BCC metals and
dilute BCC alloys, the edge strength is increasingly competitive with the screw strength in
complex alloys with large solute misfits. The edge strengthening can quantitatively explain a
number of experiments to date in BCC HEAs [ 6, 12, 17, 18, 36]. With increasing temperat-
ure, the edge motion can also becomes more important compared to the screw motion in BCC
HEAs. Thus, we believe that the well-studied {110} edge dislocation theory remains a valu-
able approach for guiding alloy design and selection, even if slip in a selected alloy emerges
to be controlled by {112} slip.
Data availability statement
All data that support the findings of this study are included within the article (and any supple-
mentary files).
Acknowledgments
This research was supported by the NCCR MARVEL, a National Centre of Competence in
Research, funded by the Swiss National Science Foundation (Grant Number 205602).
Appendix A. Validation of SNAP potentials
The elastic constants for each element, as predicted by the SNAP potentials, are shown in
table A1, and agree well with DFT results [29] to which the SNAP potentials were fit. We note
that DFT predictions of C44 are, however, very often well below experimental values at low
T, especially for Nb where the error is roughly −35%. How this error affects core structures
computed in either DFT or SNAP is unknown, but lower moduli will tend to reduce the spread
of the Burgers vector distribution, which will affect the pressure field and the resulting F(wc)
and wc. For comparisons of {110} and {112} slip, we assume that the errors due to C44 are
similar and do not affect the comparison. The USFE along ⟨111⟩ direction on {110} and {112}
slip planes are listed in table A2. The USFEs predicted by SNAP potentials are larger than
DFT predictions for each element. SNAP predictions shows that the USFEs in {112} planes
are typically larger than those in {110}, which is consistent with DFT results.
Table A1 . Elastic constants (GPa) of Nb, Ta, Mo and W. The experimental temperature
for Nb is 4 K, and 0 K for the other elements.
SNAP DFT [37] DFT [29] Exp [38]
C11 C12 C44 C11 C12 C44 C11 C12 C44 C11 C12 C44
Nb 266 142 20 243 133 18 249 135 19 253 133 31
Ta 257 161 67 272 164 71 264 161 74 266 158 87
Mo 435 169 96 479 162 97 472 158 106 450 173 125
W 560 218 154 503 215 129 511 200 142 533 205 163
14

## Page 16

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Table A2. Unstable stacking fault energy (mJ m−2) along ⟨111⟩ direction in {110} and
{112} slip planes.
SNAP DFT [39]
{110} {112} {110} {112}
Nb 898 1063 637 752
Ta 837 969 719 829
Mo 1456 1609 1389 1390
W 1853 2074 1692 1714
Figure A1 . Geometry of the supercell (before relaxation) used for the relaxation of dis-
location cores with fixed boundary condition. The positions of the atoms are derived
from V olterra solution. Atoms represented by red color are fixed during the relaxation.
First-principles calculations using DFT within the vienna ab initio simulation package [40]
are conducted to obtain the relaxed core structures of the {110} and {112} edge disloca-
tions in Nb, Ta and Mo. The calculations use the GGA approximation, the PBE exchange
correlation functional [ 41], and PAW pseudopotentials [ 42] with 13 (Nb), 5 (Ta) and 6 (Mo)
states treated as valence electrons. V alence-electron eigenstates are expanded with a spin-free
plane wave basis set, using a cutoff energy of 550 eV . The First-order Methfessel–Paxton
[43] scheme with a smearing parameter of 0.6 eV is used to describe the partial occupancies
of the orbitals. Employing such a relatively large smearing parameter is justified below. A
Γ-centered Monkhorst–Pack [ 44] k-mesh is employed with the interval between neighboring
k-mesh points along any reciprocal lattice vector set to 0.02 Å −1. For example, this k-mesh
density is equivalent to a 15 × 15 × 15 sampling for a 2-atom cubic unit cell BCC Nb (a =
3.308 Å). For a given ionic configuration, relaxation of the electronic degrees of freedom is
performed in a self-consistency loop with convergence at 10−6 eV . All interior ions are relaxed
until all forces are below 10 meV Å −1.
The dislocation cores are relaxed using a super-cell periodic along the dislocation line and
fixed boundary condition applied on its external surfaces with a vacuum thickness of 10 Å.
Figure A1 shows, as an example, the super-cell used for the construction and relaxation of
{110} and {112} dislocations in Nb. The positions of the ions located at the boundary layer
(red colored in figure A1) are fixed according to their V olterra displacement field and all the
15

## Page 17

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Table A3. Bulk properties calculated using two different smearing parameter σ (eV).
Nb Ta Mo
σ = 0.2 [37] σ = 0.6 σ = 0.2 [37] σ = 0.6 σ = 0.2 [37] σ = 0.6
a (Å) 3.308 3.308 3.308 3.295 3.151 3.150
C11 (GPa) 243 244 272 270 479 477
C12 (GPa) 133 132 164 165 162 162
C44 (GPa) 18 16 71 63 97 95
remaining ions (represented by blue color) are relaxed. Creation of a vacuum layer results in
spurious electronic forces in the relaxation region due to Friedel oscillations [ 45]. Using large
super-cell sizes and smearing parameters results in the reduction of these forces but with higher
computational cost for the former and lower accuracy of material properties for the latter. The
cell size and smearing parameters must be chosen judiciously.
The lattice parameter and the elastic constants of Nb, Ta and Mo calculated for two different
smearing values, σ = 0.2 eV and σ = 0.6 eV , are shown in tableA3. The difference is below 1%
in all cases except C44 where there is about 11% difference for Nb and Ta, and 2% difference
for Mo. We note, however, that simply increasing the k-point mesh to 16 × 16 × 16 with the
smearing σ = 0.2 eV yields C44 = 16 GPa, similar to the value for the larger smearing and
slightly smaller k-point mesh. We thus use the smearing of 0.6 eV here.
To analyze the ionic forces due to electronic Friedel oscillations, we calculated the elec-
tronic forces in perfect BCC super-cells with the same sizes and orientations as {110}, and
{112} dislocation super-cells, using smearing of σ = 0.6 eV , with the corresponding equilib-
rium lattice parameters as shown in table A3. In all cases, the forces on the ions in the core of
the dislocations are below 15 meV Å−1 (figure A2), which we deem sufficient for determining
the core structure at an accuracy needed to validate the SNAP potentials.
Figures A3–A5 show the atomic positions and edge component of the Nye tensor for the
Nb, Ta and Mo edge dislocation in the {110} and {112} slip planes. In both slip planes, the
SNAP cores in Nb, Ta and Mo are very similar to the DFT results, in all respects. We have
also created elsewhere a neural-network potential for W trained on a DFT database [ 33]. The
edge core structures for the SNAP W and the NNP W are very similar, as shown in figure A6,
providing further confidence in both potentials.
16

## Page 18

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure A2. The magnitude of the electronic forces due to Friedell oscillations, obtained
by self-consistent calculation on perfect supercells with size and orientations matching
those with dislocation.
17

## Page 19

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure A3. Edge component of Nye tensor for edge dislocations on (a) {110} and (b)
{112} slip planes in Nb. For visualization purposes, the ‘extra’ plane of atoms corres-
ponding to the center of the core is indicated by dashed line.
Figure A4. Edge component of Nye tensor for edge dislocation on (a) {110} and (b)
{112} slip planes in Ta. For visualization purposes, the ‘extra’ plane of atoms corres-
ponding to the center of the core is indicated by dashed line.
18

## Page 20

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Figure A5. Edge component of Nye tensor for edge dislocations on (a) {110} and (b)
{112} slip planes in Mo. For visualization purposes, the ‘extra’ plane of atoms corres-
ponding to the center of the core is indicated by dashed line.
Figure A6. Edge component of Nye tensor for edge dislocation on (a) {110} and (b)
{112} slip planes in W. For visualization purposes, the ‘extra’ plane of atoms corres-
ponding to the center of the core is indicated by dashed line.
19

## Page 21

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Appendix B. Full strengthening theory
The solute-related energy change for a dislocation of length ζ gliding over a distance w is
σ∆Utot = (ζρ L)
1
2 ∆eEp(w) where ρL is the atomic site density along the dislocation line direction
and ∆eEp(w) characterizes the standard deviation of the energy change, per periodic length
along dislocation line, as the dislocation glides a distance w. Combined with the elastic energy
cost to create the waviness due to the dislocation line tensionΓ = αµb2, the total energy change
of dislocation line of length L is
∆Etot (ζ, w) =

κΓ w2
2ζ − β (ζρ L)1/2 ∆eEp (w)
 L
(1 + κ) ζ (B.1)
where κ = 0.56 and β = 0.83 were obtained by a stochastic analysis [ 6].
The characteristic wavelength ζ c is obtained by minimizing the total energy with respect to
ζ as
ζc =
 
4κ2Γ2w4
β2ρL∆eE2p (w)
! 1
3
. (B.2)
The amplitude wc is then obtained from a second minimization of the total energy ∆Etot versus
w, which reduces to the solution of
∂∆eEp (w)
∂w = ∆eEp (w)
2w . (B.3)
The typical energy barrier faced by a segment of length ζ c that lies in a local favorable energy
minimum is then derived to be
∆Eb =
√
2 (ζcρL)
1
2 ∆eEp (wc) . (B.4)
Assisted by a resolved shear stress, the dislocation overcomes this barrier created by the adja-
cent unfavorable environments via thermal activation. The zero-temperature yield stress τy0
due to solute-dislocation interaction is given as
τy0 = π
2
∆Eb
bwcζc
. (B.5)
These results are general and independent of dislocation Burgers vector or glide plane, and so
apply to slip by 1/2 ⟨111⟩ BCC edge dislocations on both the {110} and {112} glide planes.
The energy changes due to the spatial fluctuations in the solutes enter only through
the quantity ∆eEp(w). This energy change depends on the difference ∆Un
sd,i (w) =
Un
sd,i (xi + w, yi ) − Un
sd,i (xi, yi ), which is the change of solute-dislocation interaction energy
due to dislocation glide by w for a solute of type n at the projected in-plane position ( xi, yi)
with respect to the dislocation line at the origin with line direction z. The characteristic poten-
tial energy ∆eEp(w) can then be written as
∆eE2
p (w) =
X
n
cn
X
i
 
∆Un
sd,i (w)
2
(B.6)
where cn is the solute concentration of solute types n, the spatial index i runs over all lattice
sites, and the solute index n runs over all alloy solute types. Here, we use the elasticity approx-
imation for the solute-dislocation interaction energy where Un
sd,i (xi, yi ) = −p(xi, yi)∆Vn with
p(xi, yi) the dislocation pressure field at in-plane position (xi, yi) and ∆V n the misfit volume
of element type n. The dislocation pressure field p(xi, yi) can be scaled using the isotropic
20

## Page 22

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
alloy elastic constants ¯µ and ¯ν as p(xi, yi) = − ¯µ
3π
(1+¯ν)
(1−¯ν) f(xi, yi) where f(xi, yi) is a dimension-
less anisotropic pressure field generated by the distribution of normalised Burgers vector along
the glide plane. Inserting the elasticity approximation into equation ( B.6), the characteristic
potential energy in the theory becomes
∆eEp (w) = ¯µ
3π
(1 + ¯ν)
(1 − ¯ν)
"X
i
∆f2
i (w)
#1/2"X
n
cn∆V2
n
#1/2
(B.7)
where ∆fi(w) = f(xi + w, yi) − f(xi, yi). This energy is thus the product of three separate terms
involving (i) the alloy elastic constants, (ii) the solute misfit volumes and solute concentrations,
and (iii) a dimensionless characteristic energy
F (w) =
"X
i
∆f2
i (w)
#1/2
(B.8)
Note that only the dimensionless characteristic energy depends on the dislocation core struc-
ture and, thus, the dislocation glide plane. So, it is only F(w) that distinguishes between
{110} and {112} slip. Inserting the characteristic potential energy (equation ( B.7)) into
equation (B.3), the characteristic wave amplitude wc becomes the solution of
∂F (w)
∂w = F (w)
2w . (B.9)
With wc determined, the typical energy barrier ∆Eb and the zero-temperature yield stress τy0
then follow as
∆Eb =
"
4
√
2Γb κ
β
 ¯µ
3π
1 + ¯ν
1 − ¯ν
2 X
n
cn∆V2
n
!# 1
3 w2
cF 2 (wc) ρL
b
 1
3
(B.10)
and
τy0 = π
2
2
4
√
2
Γb10
β
κ
 ¯µ
3π
1 + ¯ν
1 − ¯ν
4 X
n
cn∆V2
n
!23
5
1
3 F 4 (wc) ρ2
Lb7
w5c
 1
3
. (B.11)
Only the last term in each equation above depends on details of the dislocation structure, and
we isolate these dimensionless quantities for the barrier and T = 0 K yield stress as
f ∆E =
 w2
cF 2 (wc) ρL
b
 1
3
(B.12)
and
f τ =
 F 4 (wc) ρ2
Lb7
w5c
 1
3
(B.13)
The atomic line density ρL depends on the dislocation line direction, and is ρL = 1/(2
√
2b) for
{110} and ρL = 1/( 2
3
√
6b) for {112}. At finite temperature T, the finite strain-rate flow stress
τy(T, ˙ϵ) is expressed as
τy (T, ˙ϵ) = τy0 exp
"
− 1
0.55
 kT
∆Eb
ln ˙ϵ0
˙ϵ
0.91#
. (B.14)
21

## Page 23

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
Appendix C. Results using non-integer wc
In the theoretical calculations of tables 2 and 3 the characteristic waviness amplitude wc is
taken as the nearest integer multiple of the atomic position increment, b/3 for {110} slip and
b for {112} slip. Here the ‘continuous’ wc is calculated directly from equation ( B.9) without
any discreteness and the relevant dimensionless parameters are shown in tables C1 and C2.
In some {112} cases, such as W in Ta, the continuous value of wc is nearly equidistant from
the adjacent integer values, and use of the nearest integer has a significant effect on resulting
strength parameters. More broadly, use of the continuous wc tends to reduce the differences
between {112} and {110} strengthening parameters, consistent with our conclusion that the
strengths of these two slip systems are quite close.
Table C1 . Dimensionless characteristic strength parameters for edge dislocation using
the continuous wc.
Nb Ta Mo W
{112} {110} {112} {110} {112} {110} {112} {110}
wc/b 2.75 2.70 4.67 4.33 3.71 3.48 3.87 3.84
F(wc) 3.44 4.67 3.88 5.30 3.61 4.67 3.58 4.68
f ∆E 3.80 3.83 5.86 5.71 4.79 4.54 4.89 4.85
f τ 0.69 0.75 0.34 0.40 0.45 0.49 0.41 0.42
∆Eb{112}/∆Eb{110} 0.99 1.03 1.06 1.01
τy0{112}/τy0{110} 0.92 0.84 0.92 0.99
Table C2. Dimensionless characteristic strength parameters for edge dislocation for
dilute binary alloys using the continuous wc.
W in Ta Nb in Mo Nb in W
{112} {110} {112} {110} {112} {110}
wc/b 3.44 3.51 3.69 3.73 3.18 3.39
F(wc) 7.02 8.03 3.65 4.66 3.67 4.95
f ∆E 7.10 6.55 4.81 4.75 4.36 4.64
f τ 1.23 0.99 0.46 0.43 0.59 0.55
∆Eb{112}/∆Eb{110} 1.08 1.01 0.94
τy0{112}/τy0{110} 1.25 1.06 1.08
ORCID iDs
Xin Liu  https://orcid.org/0000-0001-8782-3736
Rui Barreira  https://orcid.org/0009-0000-2659-997X
M Rahbar Niazi  https://orcid.org/0000-0003-4535-8164
References
[1] Senkov O, Wilks G, Miracle D, Chuang C and Liaw P 2010 Intermetallics 18 1758–65
22

## Page 24

Modelling Simul. Mater. Sci. Eng. 32 (2024) 085018 X Liu et al
[2] Y ao H, Qiao J W, Gao M C, Hawk J A, Ma S G and Zhou H 2016 Entropy 18 189
[3] Gludovatz B, Hohenwarter A, Catoor D, Chang E H, George E P and Ritchie R O 2014 Science
345 1153–8
[4] Wu Z, Bei H, Pharr G and George E 2014 Acta Mater .81 428–41
[5] Li Z, Pradeep K G, Deng Y , Raabe D and Tasan C C 2016 Nature 534 227–30
[6] Maresca F and Curtin W A 2020 Acta Mater .182 235–49
[7] Senkov O, Wilks G, Scott J and Miracle D 2011 Intermetallics 19 698–706
[8] Y ao H, Qiao J, Gao M, Hawk J, Ma S, Zhou H and Zhang Y 2016 Mater . Sci. Eng.A 674 203–11
[9] Eleti R R, Stepanov N, Y urchenko N, Zherebtsov S and Maresca F 2022 Scr . Mater .209 114367
[10] V arvenne C, Luque A and Curtin W A 2016 Acta Mater .118 164–76
[11] V arvenne C, Leyson G, Ghazisaeidi M and Curtin W 2017 Acta Mater .124 660–83
[12] Maresca F and Curtin W A 2020 Acta Mater .182 144–62
[13] Ghafarollahi A, Maresca F and Curtin W 2019 Modelling Simul. Mater . Sci. Eng. 27 085011
[14] Rao S, Woodward C, Akdim B, Senkov O and Miracle D 2021 Acta Mater .209 116758
[15] Lee C et al 2021 Nat. Commun. 12 5474
[16] George E P , Curtin W A and Tasan C C 2020 Acta Mater .188 435–74
[17] Baruffi C, Maresca F and Curtin W A 2022 MRS Commun. 12 1111–8
[18] Winkens G et al 2023 Commun. Mater .4 26
[19] Wang F et al 2020 Science 370 95–101
[20] Wang R, Zhu L, Pattamatta S, Srolovitz D J and Wu Z 2024 Mater . Today79 36–48
[21] Tsuru T, Han S, Matsuura S, Chen Z, Kishida K, Iobzenko I, Rao S I, Woodward C, George E P
and Inui H 2024 Nat. Commun. 15 1706
[22] Kubilay R E, Ghafarollahi A, Maresca F and Curtin W A 2021 npj Comput. Mater .7 1–9
[23] V arvenne C, Luque A, Nöhring W G and Curtin W A 2016 Phys. Rev. B 93 104201
[24] Zhou X W, Johnson R A and Wadley H N G 2004 Phys. Rev. B 69 144113
[25] Liu X and Curtin W 2024 Acta Mater .263 119471
[26] Yin S, Zuo Y , Abu-Odeh A, Zheng H, Li X G, Ding J, Ong S P , Asta M and Ritchie R O 2021 Nat.
Commun. 12 4873
[27] He S, Zhou X, Mordehai D and Marian J 2023 Acta Mater .244 118539
[28] Zhou X, He S and Marian J 2022 Materials 15 5468
[29] Li X G, Chen C, Zheng H, Zuo Y and Ong S P 2020 npj Comput. Mater .6 1–10
[30] Hu Y , Szajewski B A, Rodney D and Curtin W A 2019Modelling Simul. Mater . Sci. Eng.28 015005
[31] Anderson P M, Hirth J P and Lothe J 2017 Theory of Dislocations (Cambridge University Press)
[32] Stroh A N 1958 Phil. Mag. A 3 625–46
[33] Liyanage M, Turlo V and Curtin W A 2024 (arXiv: 2406.07157)
[34] Monnet G and Terentyev D 2009 Acta Mater .57 1416–26
[35] Queyreau S, Marian J, Gilbert M R and Wirth B D 2011 Phys. Rev. B 84 064106
[36] Rao Y , Baruffi C, De Luca A, Leinenbach C and Curtin W 2022 Acta Mater .237 118132
[37] Yin B 2018 Unpublished research
[38] Simmons G and Wang H 1971 Single Crystal Elastic Constants and Calculated Aggregate
Properties: A Handbook (MIT Press)
[39] Mak E, Yin B and Curtin W 2021 2021 J. Mech. Phys. Solids 152 104389
[40] Kresse G and Furthmüller J 1996 Phys. Rev. B 54 11169–86
[41] Perdew J P , Burke K and Ernzerhof M 1996 Phys. Rev. Lett. 77 3865–8
[42] Kresse G and Joubert D 1999 Phys. Rev. B 59 1758–75
[43] Methfessel M and Paxton A 1989 Phys. Rev. B 40 3616–21
[44] Monkhorst H J and Pack J D 1976 Phys. Rev. B 13 5188–92
[45] Friedel J 1958 Il Nuovo Cimento 7 287–311
23
