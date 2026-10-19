# GraphRAG Entity and Display Rules

The graph separates material identity, physical samples, processing routes,
observed structure, mechanisms, and measured properties. Source wording and
evidence remain traceable, but author sample codes and internal database IDs
must never become canvas labels.

## Visible scientific node types

| Node type | Meaning | Example |
|---|---|---|
| Alloy | Alloy family or material system | `Nb-W alloy`, `refractory high-entropy alloy` |
| Composition | A multi-element chemical identity shared across papers | `Nb-10W-1Zr-0.1C` |
| Element | A chemical element; also represents a pure single-element material | `Nb`, `Mo`, `W` |
| Sample | A paper-scoped physical specimen linked to its composition or element | `Nb-1Zr · annealed` |
| Fabrication Process | Primary preparation, consolidation, shaping, or additive-manufacturing step | `vacuum arc melting`, `LPBF`, `hot rolling` |
| Post Treatment | Heat or surface treatment after fabrication | `Annealing · 1000 °C · 1 h` |
| Microstructure | Grain, morphology, precipitate distribution, or another structural feature | `columnar grain` |
| Phase | Crystal structure or chemical phase | `BCC`, `B2`, `Laves phase`, `ZrC` |
| Defect | Crack, pore, void, vacancy, dislocation, segregation, or inclusion | `lack-of-fusion pore` |
| Mechanism | Explicitly reported physical or chemical mechanism | `solid-solution strengthening` |
| Property | A measured numerical value, range, or bound | `Yield strength: 500 MPa` |
| Machine Learning Model | A model trained, validated, or applied by the paper | `random forest` |

Paper provenance is stored as evidence attributes (PDF, page, quote, table,
and figure), not as a canvas node. Material state, characterization parameters,
and test conditions are attributes rather than standalone nodes.

## Directed scientific paths

```text
Alloy -> Composition -> Element
Composition / pure Element -> Fabrication Process -> Post Treatment -> Sample
Composition / pure Element -> Sample  (only if no route is reported)
Sample / latest Process -> Phase / Microstructure / Defect -> Mechanism -> Property
Sample / latest Process -> Property  (test conditions stay in Property attributes)
Sample / Composition -> Machine Learning Model -> predicted Property
```

The same multi-element composition may merge across papers. A process node is
merged only when its method, parameters, input state, and output state are
identical. Samples and numerical measurements remain paper-scoped.

## Property rule

A Property node is created only when `value`, `min_value`, or `max_value`
contains an explicit, decision-relevant material-performance or
model-performance number. Grain/particle size, phase fraction, composition,
process shrinkage, porosity, and test/process parameters remain attributes.
Units and complete test conditions remain in the Property attributes. A
material Property connects directly to its Sample or relevant latest Process;
a model metric connects to its Machine Learning Model.

## Sample and composition naming

- `original_name` preserves the exact source designation only in metadata.
- `canonical_name` contains the complete source-supported chemistry.
- Opaque codes such as `7#`, `S1`, or `Sample A` are never displayed.
- Material state is metadata, not a separate node.
- A pure single-element material uses its Element node directly; it does not
  create a redundant Composition or Alloy node.
- Sample labels use `composition · state · distinguishing process`. If two
  specimens remain indistinguishable, a neutral `specimen 1`, `specimen 2`,
  and so on is used without implying a new alloy designation.
- Element nodes are periodic-table elements only. A compound additive such as
  `B4C`, `La2O3`, or `ZrO2` links its constituent elements while the original
  formula remains in edge metadata; a physical compound may also be a Phase.

## Machine-learning rule

A Machine Learning Model node is allowed only when the paper itself trains,
validates, compares, or applies the model. Task, inputs, target, dataset,
validation, and numerical metrics remain structured attributes.

## Visual rules

- Every node is circular; color encodes type.
- Clicking a node or edge opens attributes and source evidence.
- Internal IDs, raw HTML, and source-language author codes never appear in the
  tooltip.
- Core labels are restricted to Alloy, Composition, Element, and Phase.
- Process labels include key temperature, duration, and pressure values.
- A bounded view suppresses isolated nodes and process routes whose downstream
  Sample would otherwise be missing.

Saved paper-level JSON can be reprojected into these rules without an API call:

```powershell
python scripts\rebuild_graph_from_json.py
```
