# Paper Metadata

- **Title:** Crystal plasticity constitutive modeling of tensile, creep and cyclic deformation in single crystal Ni-based superalloys
- **Authors:** Suketa Chaudhary, P.J. Guruprasad, Anirban Patra
- **Journal:** Mechanics of Materials
- **Year:** 2022
- **DOI:** 10.1016/j.mechmat.2022.104474
- **Alloy system studied:** Single crystal Ni-based superalloys (CMSX-4 and PWA-1484)
- **Research objective:** To develop a microstructure-sensitive crystal plasticity constitutive framework for simulating tensile, cyclic, and creep response of single crystal Ni-based superalloys, accounting for non-Schmid effects, backstress evolution, dislocation climb, and microstructure evolution (rafting and isotropic coarsening).
- **Material category:** Ni-based single crystal superalloys (not a refractory alloy system)

# Alloy System and Research Object

This paper is a **computational constitutive modeling study** rather than an experimental alloy development study. It does not investigate refractory Nb-W, Mo-W, or refractory high-entropy alloys. The two alloys studied are:

1. **CMSX-4** – a commercial single crystal Ni-based superalloy
2. **PWA-1484** – a commercial single crystal Ni-based superalloy

The paper explicitly states: "These materials are similar in composition, with small difference in the alloy element content between them (Rodas and Neu, 2018)."

**Important note:** The paper does not provide the detailed chemical composition (in at.% or wt.%) of CMSX-4 or PWA-1484. The paper focuses on constitutive modeling rather than alloy composition analysis.

# Alloy Composition

## CMSX-4
- **Exact chemical composition:** Not explicitly stated in the original paper.
- The paper notes that the two alloys are "similar in composition, with small difference in the alloy element content between them (Rodas and Neu, 2018)."
- Reference is made to the two-phase microstructure: γ phase (Ni-rich solid solution, FCC) and γ′ phase (Ni₃Al, L1₂ ordered intermetallic precipitates).
- Microstructural parameters given:
  - γ′ volume fraction (fγ′) = 0.72
  - γ matrix volume fraction (fγ) = 0.28

## PWA-1484
- **Exact chemical composition:** Not explicitly stated in the original paper.
- Same microstructural parameters assumed as CMSX-4 (volume fraction fγ′ = 0.72, fγ = 0.28).

## Impurity levels (C, O, N, H)
- Not discussed in the original paper.

# Processing and Heat Treatment

The original paper does not discuss processing routes, manufacturing methods, or heat treatment parameters for the alloys studied. This is a constitutive modeling study that uses experimental data from the literature for calibration.

- The paper notes that "different sources may have used materials with different processing histories for their experiments" but does not provide specific processing details.
- No information is provided on arc melting, vacuum melting, powder metallurgy, additive manufacturing, homogenization, rolling, forging, annealing, or aging.

# Microstructure and Phase Constitution

## Matrix and Precipitate Phases
- **γ phase (matrix):** Ni-rich solid solution with Face-Centered Cubic (FCC) crystal structure
- **γ′ phase (precipitate):** Coherent L1₂-type, long-range ordered intermetallic Ni₃Al precipitates

## Microstructural Parameters (Table 5 of the paper)
- γ′ volume fraction (fγ′): 0.72
- γ matrix volume fraction (fγ): 0.28
- Precipitate size (dγ′): 0.5 × 10⁻³ mm
- Matrix channel width (w₀): 0.06 × 10⁻³ mm
- Initial microstructure periodicity (ζ₀ = w₀ + d₀)

The same microstructural parameters are assumed for both CMSX-4 and PWA-1484 due to lack of experimental data for PWA-1484.

## Microstructure Evolution During Creep
- **Isotropic coarsening:** Ostwald ripening, modeled using LSW theory
  - ζ(t)³ - ζ₀³ = Kt, where K = 3 × 10⁻¹⁶ mm³/s
- **Directional coarsening (rafting):** Modeled using modified JMAK equation
  - Activation energy for rafting (ΔF_r): 6.64 × 10⁻²⁰ J
  - Activation volume (ΔV): 6.64 × 10⁻²⁸ m³
  - Avrami constant (A₀): 1 × 10⁻⁹

## Deformation Systems Considered
- Matrix phase (γ): Octahedral {111}⟨1̄10⟩ slip systems
- Precipitate phase (γ′): Octahedral {111}⟨1̄10⟩ slip systems (forward and backward) + Cube {100}⟨011⟩ slip systems

## Strengthening Mechanisms Discussed
- Orowan hardening (dislocation bowing around γ′ precipitates)
- Non-Schmid effects (APB formation, cross-slip pinning)
- Taylor hardening (dislocation density-based)
- Backstress evolution
- Grain-boundary strengthening: Not applicable (single crystal)
- Precipitation strengthening: Discussed via Orowan mechanism and APB shearing
- Dispersion strengthening: Not applicable
- Solid-solution strengthening: Mentioned implicitly via thermal slip resistance τ₀

# Mechanical Properties

The paper is a constitutive modeling study; no new experimental mechanical property data is generated. Model parameters are calibrated to literature experimental data.

## Calibration Data Used (Table 6)
- **CMSX-4:**
  - Tension tests at 1123 K and 1223 K (Vattré and Fedelich, 2011)
  - Cyclic tests at 1123 K and 1223 K (Vattré and Fedelich, 2011)
  - Creep tests at 1123 K (Vattré and Fedelich, 2011), 1223 K (MacLachlan et al., 2001), 1273 K (Miura et al., 2003)
  - Relaxation tests at 1123 K and 1223 K (Vattré and Fedelich, 2011)
- **PWA-1484:**
  - Tension tests at 1255 K (Staroselsky and Cassenti, 2010)
  - Cyclic tests at 1143 K (Staroselsky and Cassenti, 2011)
  - Creep tests at 1143 K, 1255 K (Staroselsky and Cassenti, 2011); 1200 K (Staroselsky and Cassenti, 2010)
  - Relaxation tests at 1255 K (Staroselsky and Cassenti, 2011)

## Key Observations from Model Predictions

### Tensile Behavior
- Significant flow stress drop (150–200 MPa) from 1123 K to 1223 K for CMSX-4
- [001] orientation: octahedral ⟨111⟩{110} slip dominates
- [̄111] orientation: cube ⟨100⟩{110} slip dominates
- Three-stage deformation observed for [001] loading

### Cyclic Behavior
- Model predicts stabilized hysteresis loops after 2–3 cycles
- Wider hysteresis loop for [̄111] orientation compared to [001]
- Quantitative agreement better for PWA-1484 than CMSX-4

### Creep Behavior
- Steady-state secondary creep is minimal in both experiments and simulations
- Tertiary creep captured by model
- Creep stress range modeled includes 180 MPa, 250 MPa, 450 MPa, 520 MPa

### Temperature-Dependent Parameters (Table 4)
**CMSX-4:**
- τ₀ (octahedral, γ′ phase): 674.25 MPa at 1123–1143 K; 554.18 MPa at 1223–1273 K
- τ₀ (cube, γ′ phase): 411.6 MPa at 1123–1143 K; 286.10 MPa at 1223–1273 K
- τ₀ (octahedral, γ matrix): 265.71 MPa at 1123–1143 K; 228.45 MPa at 1223–1273 K

**PWA-1484:**
- τ₀ (octahedral, γ′ phase): 674.25 MPa at 1123–1143 K; 554.18 MPa at 1223–1273 K
- τ₀ (cube, γ′ phase): 411.6 MPa at 1123–1143 K; 186.10 MPa at 1223–1273 K
- τ₀ (octahedral, γ matrix): 275.7076 MPa at 1123–1143 K; 153.4454 MPa at 1223–1273 K

### Elastic Constants (Table 1)
**γ matrix:**
- C₁₁ = (298.0 − 0.096T) GPa
- C₁₂ = (191.0 − 0.057T) GPa
- C₄₄ = (139.0 − 0.035T) GPa

**γ′ precipitate:**
- C₁₁ = (325.0 − 0.096T) GPa
- C₁₂ = (209.0 − 0.057T) GPa
- C₄₄ = (144.0 − 0.035T) GPa

### Dislocation Climb Parameters
- Activation energy for climb (octahedral): 8.46 × 10⁻¹⁹ J (CMSX-4); 6.42 × 10⁻¹⁹ J (PWA-1484)
- Activation energy for climb (cube): 1.28 × 10⁻¹⁸ J (CMSX-4); 1.38 × 10⁻¹⁸ J (PWA-1484)
- Creep exponent (matrix): n = 5
- Creep exponent (precipitate): n = 10
- Burgers vector: b = 0.249 nm

### Density
- Not explicitly stated in the original paper.

### Hardness, Fracture Toughness, Creep Rupture Life
- Not explicitly stated in the original paper.

# Oxidation Resistance and Service Stability

The original paper does not discuss oxidation resistance, oxidation weight gain, oxide layer types, or effects of alloying elements on oxidation resistance. The paper focuses solely on mechanical constitutive modeling.

High-temperature embrittlement, oxygen embrittlement, nitrogen embrittlement, and grain-boundary oxidation are **not discussed** in the original paper.

# Element-Function Knowledge Cards

**Note:** The original paper does not provide detailed elemental composition data or discuss specific alloying element functions in detail. The following knowledge cards are based on what is explicitly or implicitly discussed in the paper.

---

## [Element or Element Combination]
**Ni₃Al γ′ phase constituent**

## [Applicable Alloy System]
Single crystal Ni-based superalloys (CMSX-4, PWA-1484)

## [Addition Amount or Composition Range]
γ′ volume fraction = 0.72 (as assumed for both CMSX-4 and PWA-1484 in this paper)

## [Main Function]
- Forms coherent L1₂-type long-range ordered intermetallic precipitates
- Primary source of high-temperature strength via precipitation strengthening
- Contributes to anomalous yield behavior (yield strength plateau with temperature)

## [Microstructural Mechanism]
- Orowan looping of matrix dislocations around γ′ precipitates
- Shearing of precipitates by super dislocations leading to APB formation
- Non-Schmid effects due to cross-slip of super-dislocation cores from primary to secondary edge and cube planes
- Directional coarsening (rafting) above ~900 °C

## [Property Effect]
- The paper reports τ₀ (thermal slip resistance) for γ′ phase: 674.25 MPa (octahedral) and 411.6 MPa (cube) at 1123–1143 K for CMSX-4
- No specific room-temperature or high-temperature tensile/creep numerical values are provided for the γ′ phase alone; the paper states: “The original paper does not provide specific numerical values” for individual phase mechanical properties

## [Potential Side Effects]
- Rafting-induced microstructural degradation reduces Orowan stress and accelerates tertiary creep
- Precipitate dissolution may occur beyond critical temperature (not modeled in this paper)

## [Original Evidence]
- Section 1: “coherent L1₂-type, long-range ordered intermetallic Ni₃Al precipitates, called the γ′ phase”
- Section 2.5.2: “Rafting is the morphological change of the γ′ precipitate from cuboidal geometry to elongated rafts at elevated temperatures”
- Table 4: Temperature-dependent τ₀ values

---

## [Element or Element Combination]
**Ni-rich γ matrix phase**

## [Applicable Alloy System]
Single crystal Ni-based superalloys (CMSX-4, PWA-1484)

## [Addition Amount or Composition Range]
γ matrix volume fraction = 0.28

## [Main Function]
- Ductile matrix phase providing toughness and accommodating dislocation activity
- Channel between precipitates where dislocation glide/climb occurs

## [Microstructural Mechanism]
- Octahedral {111}⟨1̄10⟩ slip systems active
- Dislocation glide impeded at γ/γ′ interface
- Dislocation climb along γ/γ′ interface at elevated temperatures
- Orowan hardening dominant in matrix channel

## [Property Effect]
- τ₀ for γ matrix (octahedral): 265.71 MPa (CMSX-4) and 275.7076 MPa (PWA-1484) at 1123–1143 K
- Initial dislocation density: 1 × 10¹¹ m⁻²

## [Potential Side Effects]
- Matrix channel widening during rafting reduces Orowan stress
- Not discussed as having any side effects in the original paper

## [Original Evidence]
- Section 1: “a Ni-rich solid solution, with Face-Centered Cubic (FCC) crystal structure, called the γ phase”
- Table 3: Initial dislocation density for γ matrix = 1 × 10¹¹ m⁻²

---

## [Element or Element Combination]
**Cube slip systems {100}⟨011⟩ in γ′ phase**

## [Applicable Alloy System]
Single crystal Ni-based superalloys (CMSX-4, PWA-1484)

## [Addition Amount or Composition Range]
Not applicable (crystallographic slip system, not an element)

## [Main Function]
- Provides additional deformation mechanism at elevated temperatures
- Dominant for [111] and [̄111] loading orientations

## [Microstructural Mechanism]
- Cube slip activated near [111] orientations at high temperatures
- No non-Schmid effects considered for cube slip systems

## [Property Effect]
- Cube slip activation energy for climb: 1.28 × 10⁻¹⁸ J (CMSX-4); 1.38 × 10⁻¹⁸ J (PWA-1484)
- τ₀ for cube slip: 411.6 MPa at 1123–1143 K; 286.10 MPa at 1223–1273 K (CMSX-4)

## [Potential Side Effects]
- Activation of cube slip reduces flow stress for [111] loading orientation compared to [001]

## [Original Evidence]
- Section 1: “Glide/climb of dislocations on the ⟨001⟩{1̄10} cube slip systems have been observed near the [111] crystal orientation at high temperatures”
- Section 2.1: “the cube {100}⟨011⟩ slip systems are also considered for the precipitate phase”

---

## [Element or Element Combination]
**Orowan hardening parameter (k_oro)**

## [Applicable Alloy System]
Single crystal Ni-based superalloys (CMSX-4, PWA-1484)

## [Addition Amount or Composition Range]
k_oro = 0.25 (dimensionless material constant)

## [Main Function]
- Represents strengthening due to Orowan bowing of dislocations around γ′ precipitates in the matrix channel

## [Microstructural Mechanism]
- Dislocation lines bow around impenetrable γ′ precipitates
- Effective matrix channel width (w̄) affects Orowan stress inversely
- Rafting increases channel width, reducing Orowan stress

## [Property Effect]
- The paper shows that Orowan stress decreases with increasing channel width during rafting
- For tensile loading at 10⁻⁴ s⁻¹, Orowan stress drops abruptly at inelastic deformation onset
- For creep loading at 250 MPa, Orowan stress decreases gradually with time

## [Potential Side Effects]
- Reduction in Orowan stress during rafting contributes to tertiary creep acceleration

## [Original Evidence]
- Eq. (8): s_aj includes k_oro·G_j·b_j/w̄ term for matrix phase
- Section 3.4: “the Orowan stress decreases as the channel width increases”
- Fig. A.12: Orowan stress evolution during tensile and creep loading

# Strengthening Mechanism Knowledge Cards

---

## Solid-Solution Strengthening
- **Related elements:** Not explicitly discussed; implicit in the thermal slip resistance term τ₀
- **Typical alloys:** CMSX-4, PWA-1484
- **Key compositions:** Not provided in the original paper
- **Microstructural changes:** Lattice distortion in γ matrix due to solute atoms
- **Property improvements:** Contributes to thermal slip resistance of γ matrix (τ₀ = 265.71 MPa for CMSX-4 at 1123–1143 K)
- **Risks and limitations:** Not discussed in the original paper

---

## Carbide or Boride Precipitation Strengthening
- **Related elements:** Not discussed
- **Typical alloys:** Not discussed
- **Key compositions:** Not discussed
- **Microstructural changes:** Not discussed
- **Property improvements:** Not discussed
- **Risks and limitations:** Not discussed

---

## Oxide Dispersion Strengthening
- **Related elements:** Not discussed
- **Typical alloys:** Not discussed
- **Key compositions:** Not discussed
- **Microstructural changes:** Not discussed
- **Property improvements:** Not discussed
- **Risks and limitations:** Not discussed

---

## Orowan Hardening / Precipitation Strengthening
- **Related elements:** Ni₃Al (γ′ precipitates)
- **Typical alloys:** CMSX-4, PWA-1484
- **Key compositions:** γ′ volume fraction = 0.72
- **Microstructural changes:** Coherent L1₂ precipitates act as barriers to dislocation glide in γ matrix
- **Property improvements:** Significant athermal slip resistance contribution; Orowan stress inversely proportional to channel width
- **Risks and limitations:** Channel widening during rafting reduces Orowan stress, leading to tertiary creep acceleration

---

## Non-Schmid Effects / Anomalous Yield
- **Related elements:** Ni₃Al (γ′ phase)
- **Typical alloys:** CMSX-4, PWA-1484
- **Key compositions:** Not applicable (mechanism-based)
- **Microstructural changes:** Cross-slip of super-dislocation cores from primary to secondary edge and cube planes; APB formation
- **Property improvements:** Anomalous yield behavior—little or no yield strength decrease up to ~1123 K
- **Risks and limitations:** Non-Schmid effects decay beyond ~1123 K, leading to significant flow stress drop (150–200 MPa from 1123 K to 1223 K)

---

## Dislocation Climb-Enhanced Deformation
- **Related elements:** Not element-specific
- **Typical alloys:** CMSX-4, PWA-1484
- **Key compositions:** Not applicable
- **Microstructural changes:** Dislocation climb perpendicular to slip plane at γ/γ′ interfaces
- **Property improvements:** Dominant deformation mechanism during creep at elevated temperatures (>850–900 °C)
- **Risks and limitations:** Climb contributes to tertiary creep and reduces load-bearing capacity

---

## Rafting-Induced Microstructure Evolution
- **Related elements:** Not element-specific (lattice misfit dependent)
- **Typical alloys:** CMSX-4, PWA-1484
- **Key compositions:** Negative lattice misfit assumed
- **Microstructural changes:** γ′ precipitates change from cuboidal to elongated raft morphology; γ channels widen
- **Property improvements:** Can increase load-bearing capacity when dislocation climb dominates (creep at low stresses)
- **Risks and limitations:** Reduces Orowan stress and coherency, accelerating tertiary creep at higher stresses

---

# Key Conclusions

1. **Model framework:** A dislocation density-based crystal plasticity constitutive model was developed to simulate tensile, cyclic, and creep response of single crystal Ni-based superalloys.

2. **Non-Schmid effects:** The model accounts for orientation- and temperature-dependent yield anisotropy using a non-Schmid model for the precipitate phase.

3. **Backstress evolution:** A slip system-level backstress model captures cyclic response (directional hardening).

4. **Dislocation climb:** Climb kinematics perpendicular to the slip plane are incorporated using a power law model with Peach–Koehler-type normal stress.

5. **Microstructure evolution:** Constitutive equations for rafting (directional coarsening) and isotropic coarsening account for microstructure evolution during creep.

6. **Relative slip activity:** For [001] loading, octahedral slip in the matrix dominates; for [̄111] loading, cube slip in the precipitate dominates. Tensile/cyclic loading is dominated by glide, while creep is dominated by climb.

7. **Rafting orientation dependence:** Rafting occurs for [001] loading but does not occur for [̄111] loading (consistent with experimental observations).

8. **Tertiary creep:** Microstructure degradation (isotropic coarsening and rafting) is identified as a primary contributor to tertiary creep acceleration.

9. **Creep-fatigue predictions:** The model qualitatively predicts relaxation behavior for both alloys, with limitations in capturing cyclic softening and accurate peak stresses.

10. **Model limitations identified:**
    - Does not account for positive lattice misfit
    - Assumes constant γ′ volume fraction (no precipitate dissolution)
    - Does not explicitly model lattice misfit and coherency stresses
    - Does not explicitly account for APB energy temperature dependence
    - Cannot capture damage mechanisms during late-stage tertiary creep
    - Does not model cyclic softening

# Limitations and Applicable Scope

1. **Alloy system limitation:** This paper is **not relevant** to refractory high-temperature alloys, Nb-W-based alloys, Mo-W-based alloys, refractory high-entropy alloys, or additively manufactured refractory alloys. It exclusively addresses single crystal Ni-based superalloys.

2. **No composition data provided:** The paper does not provide detailed chemical compositions (at.% or wt.%) of CMSX-4 or PWA-1484.

3. **No processing/microstructure characterization:** No experimental processing routes, heat treatments, or microstructural characterization data are provided. All experimental data are compiled from literature sources.

4. **Constitutive model assumptions:**
   - Valid only for negative lattice misfit alloys subjected to tension
   - γ′ volume fraction assumed constant (valid up to ~980 °C)
   - Lattice misfit and coherency stresses only implicitly accounted for
   - APB energy temperature dependence not explicitly modeled

5. **Model validation:** Predictions are compared qualitatively with experimental data; quantitative discrepancies exist for cyclic loading at [̄111] orientation, peak stresses in relaxation tests, and tertiary creep rates.

6. **Data source variability:** Experimental data from different sources may involve materials with different processing histories, which could introduce variability in calibration.

7. **Temperature range:** Model calibrated for 1123–1273 K (850–1000 °C), typical operating range for Ni-based superalloys in aerospace applications.
