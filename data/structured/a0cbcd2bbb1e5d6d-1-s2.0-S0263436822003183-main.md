# Paper Metadata

- **Title**: Refined W-3.5Nb alloy fabricated by electron beam melting via doped carbon
- **Authors**: Guangyu Yang, Wenpeng Jia, Jian Wang, Nan Liu, Liang Jia
- **Journal**: International Journal of Refractory Metals and Hard Materials
- **Year**: 2023 (Available online 24 December 2022)
- **DOI**: 10.1016/j.ijrmhm.2022.106094
- **Volume**: 111, 106094
- **Corresponding Author**: Guangyu Yang (yanggy0403@163.com)
- **Affiliation**: State Key Laboratory of Porous Metal Materials, Northwest Institute for Nonferrous Metal Research, Xi'an 710016, China

# Alloy System and Research Object

- **Alloy system studied**: W-Nb alloy (specifically W-3.5Nb) and carbon-doped variant (W-3.5Nb-0.7C)
- **Material category**: Additively manufactured tungsten-based alloy fabricated by Electron Beam Melting (EBM), also referred to as Selective Electron Beam Melting (SEBM)
- **Base alloy**: W-3.5Nb (tungsten-niobium solid solution alloy)
- **Modified alloy**: W-3.5Nb-0.7C (carbon-doped tungsten-niobium alloy)
- **Research objective**: To address the challenge of crack-free and refined W-based alloy fabrication in EBM by introducing 0.7 wt% carbon, aiming to simultaneously improve forming quality (crack reduction) and reduce grain size in AM tungsten

# Alloy Composition

## Feedstock Powder Compositions (Table 1)

| Alloy | W (wt%) | Nb (wt%) | C (wt%) | O (wt%) |
|-------|---------|----------|---------|---------|
| W-3.5Nb | Balance | 3.59 | 0.004 | 0.023 |
| W-3.5Nb-0.7C | Balance | 3.8 | 0.73 | 0.010 |

- **Powder particle size**: 15–53 μm, spherical, prepared by plasma spheroidization
- **Alloying elements present**: W (matrix), Nb (3.59–3.8 wt%), C (0.004 wt% baseline, 0.73 wt% doped variant)
- **Impurity levels**: O = 0.023 wt% (W-3.5Nb) and 0.010 wt% (W-3.5Nb-0.7C)
- **No elements**: Mo, Ta, Zr, Hf, Ti, V, Cr, Al, Si, Re, B, Y, La, N are not included in the alloy composition; no ppm-level impurity data for C, N, H beyond O are explicitly reported

# Processing and Heat Treatment

## Additive Manufacturing (EBM)
- **Method**: Electron Beam Melting (EBM), system: Sailong S2 (Xi'an Sailong Metal Materials Co., Ltd., China)
- **Sample dimensions**: 10 mm × 10 mm × 10 mm cubic samples
- **Vacuum atmosphere**: Vacuum pressure < 10² Pa
- **Preheating**: Build platform preheated to 600 °C with electron beam before deposition
- **Layer thickness**: 0.05 mm
- **Beam current**: 19–21 mA
- **Scanning speed**: 1100 mm/s
- **Scan strategy**: Scan direction rotated by 90° between layers
- **Build chamber temperature**: Kept at elevated temperature throughout the build process (E-beam rapid scanning of high-power electron beam)

## Powder Preparation
- **Feedstock**: Pre-alloyed spherical powders prepared by plasma spheroidization
- **Supplier**: Stardust Technology (Guangdong), Co., Ltd., China
- **Particle size range**: 15–53 μm

## Heat Treatment / Post-Processing of Built Samples
- Not explicitly stated in the original paper. The samples were characterized in as-built condition.

# Microstructure and Phase Constitution

## W-3.5Nb Alloy (As-Built)
- **Matrix phase**: Single-phase tungsten solid solution (BCC)
- **Grain morphology**: Coarse columnar grains along the building direction Z
- **Preferred orientation**: Distinct (100) crystallographic texture (confirmed by EBSD pole figures)
- **Crack features**: Long cracks located at coarse columnar grain boundaries propagating across multiple deposited layers; rough crack surfaces with discontinuous holes (solidification cracking morphology)
- **Solidification path**: Forced epitaxial growth, grains growing opposite to heat flow direction

## W-3.5Nb-0.7C Alloy (As-Built)
- **Grain size**: ~30 μm (smaller grain size compared to W-3.5Nb)
- **Grain morphology**: Suppressed coarse columnar grains; periodically distributed microstructure with cycle period close to layer thickness (0.05 mm)
- **Microstructural layering**: Tiny equiaxed grains at the bottom of each layer; tiny columnar grains in upper regions
- **Fine dendritic microstructure colonies**: Adjacent cell colonies separated by different orientations
- **Phases**: Tungsten solid solution + small amount of eutectic W/W₂C in interdendritic gap regions
- **Elemental distribution (from EDS maps)**: 
  - Dendrite arms: rich in tungsten and niobium
  - Dendrite gaps/interdendritic regions: rich in tungsten, niobium, and carbon
- **Eutectic phase**: W/W₂C formed in a closed network structure surrounding the W phase
- **Preferred orientation**: Barely recognizable (EBSD confirms near absence of preferential direction)
- **Crack features**: Little cracks and pores along grain boundaries

## Crack Mechanisms Discussed
- **W-3.5Nb cracking type**: Solidification cracking attributed to broadened solidification range caused by Nb addition (semi-solid/mushy zone at end of solidification)
- **Crack morphology**: Rough surfaces with discontinuous holes, consistent with solidification cracking
- **Oxygen role**: Authors state oxygen (0.023 wt% in W-3.5Nb powder vs 0.017 wt% in their previous pure W study) has no significant effect on EBM tungsten cracking; residual stress and oxygen influence not deeply analyzed in this study
- **Solid-state cracking**: Referenced from literature but not the dominant mode in EBM W-3.5Nb due to EBM preheating (in-situ stress release at annealing temperature of W-based material)

# Mechanical Properties

| Property | W-3.5Nb | W-3.5Nb-0.7C | Increase |
|----------|---------|--------------|----------|
| Average Vickers hardness | 382 HV | 696 HV | +82% |
| Compressive strength (at RT) | 962.89 MPa | 1892.56 MPa | +96% |

## Hardness Details (Table 2)
- **W-3.5Nb**: Individual values 427, 407, 420, 418 HV; average = 382 HV (Note: the average reported in text as 382 HV appears inconsistent with the tabulated individual values averaging ~418 HV; original paper states average 382 HV)
- **W-3.5Nb-0.7C**: Individual values 696, 692, 700, 696 HV; average = 696 HV
- **Test conditions**: Load = 50 g; dwell time = 10 s

## Compression Test
- **Temperature**: Ambient (room temperature)
- **Strain rate**: 0.001/s
- **Sample dimensions**: Cylindrical φ 5 mm × 5 mm
- **Machine**: Instron 5985
- **W-3.5Nb compressive strength**: 962.89 MPa
- **W-3.5Nb-0.7C compressive strength**: 1892.56 MPa
- **Fracture mode**: Both alloys show smooth fracture surfaces without deformation marks; typical intergranular fracture mode; brittle fracture

## Mechanical Property Enhancement Mechanism
- **Hardness increase attributed to**: Presence of W₂C in a closed network structure (per authors)
- **Strength increase**: Attributed to carbon addition and eutectic phase formation, refined microstructure

## High-Temperature Mechanical Properties
- Not explicitly stated in the original paper. All mechanical testing was at ambient/room temperature.

## Creep Performance, Fracture Toughness, Elastic Modulus, Density
- Not explicitly stated in the original paper.

# Oxidation Resistance and Service Stability

- Not explicitly stated in the original paper. The paper focuses on room-temperature microstructure, cracking behavior, and mechanical properties of as-built EBM samples. No oxidation weight gain, oxide layer characterization, or high-temperature oxidation/corrosion data are presented. No discussion of high-temperature embrittlement beyond the mention of DBTT in tungsten and the inherent brittleness at room temperature observed in compression fracture.

# Element-Function Knowledge Cards

---

## Knowledge Card: Carbon (C)

- **Element**: Carbon (C)
- **Applicable Alloy System**: W-Nb-based alloys fabricated by electron beam melting (EBM)/selective electron beam melting (SEBM); EBM W-3.5Nb alloy; also reported effective in AM Mo-based alloys
- **Addition Amount or Composition Range**: 0.7 wt% (0.73 wt% in powder, nominally W-3.5Nb-0.7C); low distribution coefficient of carbon in tungsten = 0.0017
- **Main Function**: Grain refinement (suppresses coarse columnar structure); reduction of solidification cracks along grain boundaries; significant strengthening (hardness and compressive strength improvement)
- **Microstructural Mechanism**:
  - Low carbon distribution coefficient (0.0017) causes concentration gradient at solid/liquid interface during solidification
  - Carbon enrichment in liquid ahead of advancing solidification front creates constitutional supercooling
  - Constitutional supercooling triggers nucleation at the bottom of molten pool, forming tiny equiaxed grains
  - Carbon accumulation ahead of solidification front reduces solidification front velocity, increasing thermal supercooling
  - Combined thermal + constitutional supercooling refines microstructure
  - Formation of eutectic W/W₂C phase in interdendritic gap regions with low melting point
  - Eutectic phase forms closed network structure surrounding W dendrite phase
- **Property Effect**:
  - Grain size reduced to ~30 μm, coarse columnar grains suppressed
  - Microhardness increased from 382 HV to 696 HV (+82%)
  - Room-temperature compressive strength increased from 962.89 MPa to 1892.56 MPa (+96%)
  - Preferential crystallographic orientation (⟨100⟩) eliminated
  - Solidification cracks along grain boundaries significantly reduced
- **Potential Side Effects**:
  - Fracture remains brittle (intergranular fracture mode with smooth fracture surfaces, no deformation marks)
  - Formation of W₂C carbide network may contribute to brittleness at room temperature
- **Original Evidence**: 
  - Table 1 (powder compositions)
  - XRD patterns (Figure 8) showing W₂C formation
  - EBSD IPF maps (Figures 3, 5, 6)
  - Element distribution maps (Figure 7)
  - Microhardness data (Table 2)
  - Compressive stress-strain curves (Figure 11)
  - "The low distribution coefficient of carbon in tungsten... is 0.0017 [32]..."
  - "Supercooling (thermal supercooling together with constitutional supercooling) refined the microstructure of W-3.5Nb alloy effectively."

---

## Knowledge Card: Niobium (Nb)

- **Element**: Niobium (Nb)
- **Applicable Alloy System**: W-based alloys (W-3.5Nb); Nb forms complete solid solution with W during melting; EBM W-Nb system
- **Addition Amount or Composition Range**: 3.59 wt% (W-3.5Nb powder); 3.8 wt% (W-3.5Nb-0.7C powder)
- **Main Function**: Alloying element forming complete solid solution with tungsten; broadens solidification range (creates mushy zone)
- **Microstructural Mechanism**:
  - Forms complete solid solution with W during melting
  - Broadens solidification range with a semisolid (mushy) region at the end of solidification
  - Contributes to solidification cracking susceptibility by increasing the semisolid temperature range
  - In W-Nb-C system, Nb is present in both dendritic arms and interdendritic regions
- **Property Effect**:
  - W-3.5Nb alloy as baseline: hardness = 382 HV, compressive strength = 962.89 MPa, brittle intergranular fracture
  - The specific strengthening or ductilizing effect of Nb is not quantified in this paper; it serves as the baseline alloying element
- **Potential Side Effects**:
  - Broadened solidification range with semi-solid region at end of solidification causes intergranular solidification cracking (shrinkage in mushy zone + thermal contraction)
- **Original Evidence**: 
  - "Tungsten and niobium form a complete solid solution during the melting process."
  - "Compared with pure tungsten, W-3.5Nb alloy has a broaden solidification range with a region of semisolid (called mushy) at the end of the solidification process."
  - Element distribution maps (Figure 7b, 7c) showing Nb in dendrites and gaps

---

## Knowledge Card: Carbon + Tungsten (C + W)

- **Element/Element Combination**: Carbon + Tungsten (C/W₂C eutectic formation)
- **Applicable Alloy System**: W-C binary system; W-3.5Nb-0.7C alloy
- **Addition Amount or Composition Range**: C content = 0.73 wt% (0.7 wt% nominal); W₂C carbide formed in interdendritic eutectic regions
- **Main Function**: Eutectic phase (W/W₂C) formation with low melting point improves terminal liquid fluidity, filling shrinkage gaps; W₂C closed network structure contributes to strength/hardness
- **Microstructural Mechanism**:
  - During terminal solidification with decreasing temperature, eutectic reaction L → W₂C + W occurs in the W-C binary system
  - W-3.5Nb-0.7C exhibits mixed structure of dendritic phase + interdendritic eutectic phase
  - W₂C forms as closed network structure surrounding W phase
  - Micro-segregation of carbon promotes formation of low-melting eutectic phase
  - Low-melting eutectic increases flowability of liquid to fill gaps caused by shrinkage between dendrites
- **Property Effect**:
  - Hardness increase from 382 to 696 HV (+82%) attributed to W₂C closed network structure
  - Compressive strength increase from 962.89 to 1892.56 MPa
  - Cracks along grain boundaries significantly reduced
- **Potential Side Effects**:
  - Room-temperature brittleness persists (smooth fracture surfaces, intergranular mode, no deformation marks)
- **Original Evidence**: 
  - "W-3.5Nb-0.7C alloy shows tungsten solid solution and a small amount of eutectic W/W₂C in gap regions."
  - "Micro-segregation of carbon is a possible condition for reducing solidification cracking, which promotes the formation of low-melting eutectic phase, increasing the flowability of liquid to fill the gap caused by shrinkage between dendrites in time."
  - "The reason for the high hardness is the present of W₂C in a closed network structure."

---

## Knowledge Card: Oxygen (O)

- **Element**: Oxygen (O)
- **Applicable Alloy System**: EBM W-based alloys (W-3.5Nb and W-3.5Nb-0.7C in this paper; previous EBM pure tungsten work referenced)
- **Addition Amount or Composition Range in Paper**: W-3.5Nb powder O = 0.023 wt%; W-3.5Nb-0.7C powder O = 0.010 wt% (lower oxygen content in C-doped powder, likely due to carbon deoxidation during powder preparation)
- **Main Function**: In prior literature, O at grain boundaries may contribute to cracking in SLM tungsten; in this EBM work, the authors state oxygen has no significant effect on cracking
- **Microstructural Mechanism**:
  - Previous EBM pure tungsten study by same group showed oxygen content of 0.017 wt% (similar to this study's 0.023 wt%) with no significant effect on cracking
  - In EBM, preheating and elevated chamber temperature in-situ release stress effectively
- **Property Effect**: Not quantified in this paper; authors state "oxygen has no significant effect on cracking in EBM tungsten"
- **Potential Side Effects**: In literature (AM tungsten), oxygen at grain boundaries can form oxides, agglomerate pores, and weaken grain boundary strength; the authors do not identify this as a significant factor in this EBM study
- **Original Evidence**: 
  - Table 1 (O content of powders)
  - "Meanwhile, oxygen content of the spherical powder used in the previous research was 0.017 wt%, which was similar with this study of 0.023 wt%. The results showed that oxygen has no significant effect on cracking in EBM tungsten."

---

# Strengthening Mechanism Knowledge Cards

## Mechanism Card 1: Grain Refinement via Constitutional + Thermal Supercooling (Carbon-Induced)

- **Mechanism**: Grain refinement through combined constitutional supercooling and thermal supercooling induced by carbon alloying in EBM
- **Related Elements**: Carbon (C)
- **Typical Alloys**: W-3.5Nb-0.7C; also applicable to carbon-doped Mo-based alloys in literature
- **Key Compositions**: 0.7 wt% C in W-3.5Nb; carbon low distribution coefficient in W (0.0017)
- **Microstructural Changes**:
  - Coarse columnar grains (⟨100⟩ preferred orientation) → refined ~30 μm grains with no preferential orientation
  - Periodically laminated microstructure with repeated cycle period of 0.05 mm (matching EBM layer thickness)
  - Tiny equiaxed grains at layer bottom, tiny columnar grains at layer top
  - Fine dendritic microstructure colonies with W/W₂C eutectic in interdendritic regions
- **Property Improvements**:
  - Hardness: 382 → 696 HV (+82%)
  - Compressive strength: 962.89 → 1892.56 MPa (RT)
  - Crack formation significantly reduced at grain boundaries
  - Elimination of ⟨100⟩ preferred texture
- **Risks and Limitations**:
  - Room-temperature brittleness remains (intergranular fracture with no plastic deformation)
  - W₂C network may adversely affect ductility at ambient temperatures
  - Effective only at appropriate C addition levels (too much C may lead to excessive brittle carbide formation)
- **Original Evidence**: "Doping 0.7 wt% carbon transforms coarse columnar grains of W-3.5Nb alloy into fine dendrites with W phase being surrounded by a closed network of eutectic phase due to thermal supercooling together with constitutional supercooling."

## Mechanism Card 2: Solidification Crack Suppression via Low-Melting Eutectic + Grain Refinement

- **Mechanism**: Reduction of solidification cracks through formation of low-melting-point eutectic liquid (improved terminal solidification fluidity) and grain refinement (accommodating local strain)
- **Related Elements**: Carbon (forming W/W₂C eutectic)
- **Typical Alloys**: W-3.5Nb-0.7C EBM alloy
- **Key Compositions**: 0.7 wt% C; W/W₂C eutectic phase
- **Microstructural Changes**:
  - Reduction of long cracks along coarse columnar grain boundaries propagating across multiple layers
  - Little cracks and pores along grain boundaries after C addition
  - Refined grain structure (~30 μm)
  - Eutectic W/W₂C filling interdendritic gaps and shrinkage cavities
- **Property Improvements**:
  - Effective suppression of solidification cracks
  - Improved forming quality and structural integrity
- **Risks and Limitations**:
  - Some cracks and pores still present after C addition (not completely eliminated)
  - W₃.5Nb without C shows severe solidification cracking due to broad mushy zone
- **Original Evidence**: "The addition of carbon generates eutectic phase with low melting point and refines the microstructure, effectively reducing the solidification crack along the grain boundary."

## Mechanism Card 3: Second-Phase Strengthening via W₂C Closed Network Structure

- **Mechanism**: Hardening/strengthening through W₂C carbide phase forming a closed network structure around W dendrite matrix
- **Related Elements**: Carbon (C), Tungsten (W)
- **Typical Alloys**: W-3.5Nb-0.7C EBM alloy
- **Key Compositions**: 0.73 wt% C (forming W₂C)
- **Microstructural Changes**:
  - W₂C eutectic phase forming closed network structure surrounding W dendrites
  - Dendrite arms: W and Nb rich; interdendritic gaps: W, Nb, and C rich
- **Property Improvements**:
  - Microhardness: 382 → 696 HV (+82%)
  - Compressive strength: 962.89 → 1892.56 MPa (nearly doubled at room temperature)
- **Risks and Limitations**:
  - No improvement in room-temperature ductility; brittle intergranular fracture persists
  - Network carbide structure may be detrimental to toughness
- **Original Evidence**: "The reason for the high hardness is the present of W₂C in a closed network structure."

## Mechanism Card 4: Solid Solution Strengthening in W-Nb System

- **Mechanism**: Solid solution strengthening via complete solid solution formation between W and Nb
- **Related Elements**: Niobium (Nb) in tungsten matrix
- **Typical Alloys**: W-3.5Nb EBM alloy
- **Key Compositions**: 3.59 wt% Nb (baseline); 3.8 wt% Nb (C-doped variant)
- **Microstructural Changes**: Complete solid solution of Nb in BCC tungsten matrix
- **Property Improvements**:
  - Baseline properties: 382 HV, 962.89 MPa compressive strength
  - Nb broadening solidification range creates mushy zone → increases solidification cracking susceptibility
- **Risks and Limitations**:
  - Broadened solidification range with semi-solid/mushy region triggers intergranular solidification cracking
  - No grain refinement benefit from Nb alone; coarse columnar structure persists with ⟨100⟩ texture
- **Original Evidence**: "Tungsten and niobium form a complete solid solution during the melting process." + "Compared with pure tungsten, W-3.5Nb alloy has a broaden solidification range with a region of semisolid (called mushy) at the end of the solidification process."

## Mechanism Card 5: EBM-Specific Process Advantages for W-Based Alloys

- **Mechanism**: EBM process characteristics (vacuum, high preheat, elevated build chamber temperature) enable in-situ stress relief and reduction of solid-state cracking in tungsten
- **Related Elements**: Process parameters rather than alloy composition
- **Typical Alloys**: Pure tungsten and W-based alloys (W-3.5Nb, W-3.5Nb-0.7C)
- **Key Compositions/Parameters**: Preheating build platform to 600 °C; vacuum < 10² Pa; layer thickness 0.05 mm; beam current 19–21 mA; scanning speed 1100 mm/s; 90° layer rotation
- **Microstructural Changes**: In-situ stress release at elevated build chamber temperature reaching annealing temperature of W-based material
- **Property Improvements**: Reduced solid-state cracking compared to SLM; densified and improved build quality
- **Risks and Limitations**: 
  - Coarse columnar microstructure still forms due to high thermal conductivity of W (epitaxial growth along heat flow direction)
  - Solidification cracking remains for Nb-containing alloys without C addition
- **Original Evidence**: "Due to the characteristic of preheating treatment in EBM, the temperature within the built chamber reaches the annealing temperature of W-based material to in-situ release the stress effectively and reduce solid-state cracking obviously."

# Key Conclusions

1. **Successful fabrication**: Both W-3.5Nb and W-3.5Nb-0.7C alloys were successfully fabricated by Electron Beam Melting (EBM).

2. **Carbon-induced grain refinement**: Doping 0.7 wt% carbon transforms the coarse columnar grain structure of W-3.5Nb alloy (~⟨100⟩ preferred orientation) into refined fine dendrites (~30 μm) with tungsten phase being surrounded by a closed network of eutectic W/W₂C phase.

3. **Refinement mechanism**: The refinement arises from combined thermal supercooling (due to reduced solidification front velocity from carbon accumulation ahead of the front) and constitutional supercooling (due to carbon's extremely low distribution coefficient of 0.0017 in tungsten, creating solute enrichment and supercooling at the solid/liquid interface).

4. **Crack suppression**: Carbon addition generates a low-melting eutectic phase and refines the microstructure, effectively reducing solidification cracks along grain boundaries. The eutectic improves terminal liquid fluidity and fills shrinkage gaps between dendrites.

5. **Property improvement**: 
   - Microhardness increased from 382 HV (W-3.5Nb) to 696 HV (W-3.5Nb-0.7C), an 82% increase.
   - Compressive strength increased from 962.89 MPa to 1892.56 MPa (nearly doubled).
   - Both alloys exhibited brittle, smooth, intergranular fracture at room temperature.

6. **W-3.5Nb without carbon** exhibits coarse columnar grains with long solidification cracks along grain boundaries, attributed to the broadened solidification range caused by Nb addition.

7. **New perspective**: The approach offers a new perspective on AM fabrication of high-quality W-based alloys via carbon alloying for simultaneous grain refinement and crack reduction.

# Limitations and Applicable Scope

**Limitations explicitly stated or implied:**
- The mechanical testing was performed only at room/ambient temperature; high-temperature mechanical properties are not characterized.
- Both alloys remain brittle at room temperature (smooth fracture surfaces, intergranular fracture, no deformation marks), even after carbon addition.
- Complete crack-free and pore-free consolidation is not achieved: "little cracks and pores" remain along grain boundaries in the C-doped sample.
- The paper does not investigate oxidation resistance, high-temperature stability, creep, fatigue, or fracture toughness.
- The specific effect of carbon on high-temperature mechanical properties is not addressed.
- The exact quantitative contribution of grain refinement (Hall-Petch) versus W₂C second-phase strengthening is not separated.
- The apparent discrepancy in reported W-3.5Nb average hardness (text reports 382 HV average, while tabulated individual values average ~418 HV) is not clarified in the original paper.
- The work focuses on a single carbon addition level (0.7 wt%); the influence of varying carbon content or other carbide-forming elements (Hf, Ta, Zr) is not explored in this specific study.
- No post-process heat treatment is explored; only as-built condition characterized.
- Long-term service stability and response to thermal cycling or radiation environments are not within the scope of this paper.
- No nitrogen, hydrogen, or other impurity analysis is provided beyond oxygen and carbon.

**Applicable scope:**
- The findings are most directly applicable to EBM/SEBM of W-Nb-C alloys for refractory applications such as plasma-facing components in fusion reactors.
- The grain refinement and crack reduction approach (carbon micro-alloying) is likely transferable to other powder-bed-fusion AM of tungsten-based and molybdenum-based alloys, as supported by literature references in the paper.
