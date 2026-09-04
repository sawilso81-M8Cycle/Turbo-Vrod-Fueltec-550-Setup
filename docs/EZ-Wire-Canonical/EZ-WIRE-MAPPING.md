# EZ Wire Mapping and Entry Sequence

## Current EZ Wire capability

EZ Wire publicly documents the following workflow:

1. create a wiring harness and select measurement units;
2. import reusable devices from its Device Library or create connectors manually;
3. add cavity descriptions;
4. enable/create wire types and cable types;
5. create cavity-to-cavity wire connections;
6. create branches and visual layout/lengths;
7. configure wire idents;
8. review generated cut list and BOM.

This canonical folder matches those concepts. It does **not** claim that EZ Wire currently accepts these exact CSVs as a native full-harness import format.

## Recommended project creation order

### 1. Harness containers

Create EZ Wire harnesses from `01-harnesses.csv`, using millimetres.

Recommended starting project: `H-MAIN Turbo V-Rod Main Engine Harness`.

The smaller harness records may be separate physical harnesses or organizational subprojects depending on the manufacturer's build strategy. Do not alter electrical connections when choosing project grouping.

### 2. Devices

Use `02-devices.csv`.

Prefer EZ Wire Device Library entries when the device is an exact hardware match and its cavity data is verified against this repository. ECUMASTER devices are publicly listed as supported by EZ Wire's Device Library, so compare any PMU16 library entry against `04-cavities.csv` before accepting it.

If a library device disagrees with the canonical repository, the repository remains controlling until engineering explicitly approves a change.

### 3. Connectors

Create connectors from `03-connectors.csv`.

- `TBD` cavity counts stay unresolved until physical evidence closes them.
- Do not create invented cavities merely to make a visual diagram look complete.
- Abstract junctions such as J-P01/J-P02 may be represented as manual connectors/junction nodes.

### 4. Cavities

Populate cavity descriptions from `04-cavities.csv`.

Important fields:

- `canonical_circuit_id` = current conductor/circuit key;
- `original_circuit_id` = legacy/source connector-schedule identifier when different;
- `evidence_state` = whether the cavity is verified or still gated.

Never overwrite the canonical circuit ID with an older connector-schedule alias.

### 5. Wire types and cable types

Enable/create types from `05-wire-types.csv`.

Recommended EZ Wire cable objects:

- `CAN035` as a 2-conductor twisted CAN cable;
- `CKP035` as a 2-conductor shielded/twisted trigger cable;
- sensor branches may use individual `SENSOR035` conductors unless a reusable cable object is preferred.

Wire colors/idents have not been invented in this canonical conversion. Enter them only after released identification data exists.

### 6. Connections

Create connections from `06-connections.csv`.

`connection_id` is the immutable repository Circuit ID and should be copied into EZ Wire's wire number/description field wherever practical.

Do not renumber PWR-002, GND-001, INJ-001, CAN-001, etc. inside EZ Wire unless EZ Wire also retains the canonical ID in a visible custom/description field.

Where an endpoint is abstract or `TBD`, leave the physical cavity unresolved rather than choosing one by convenience.

### 7. Splices and junctions

Create splice/junction nodes from `07-splices-junctions.csv`.

Key topology rules:

- J-P01 is primary positive distribution.
- J-P02 is high-current ground only.
- S-SENS-02 precision sensor ground must remain separate from J-P02.
- S-CAN-01 is a short service branch and does not add termination.

### 8. Branches and lengths

Use `08-branches-lengths.csv` to seed the visual diagram.

`approx_length_mm` and `prototype_cut_length_mm` are provisional whenever `ezwire_length_state=PROVISIONAL`.

Do not use them as final production cut lengths until the physical dimension freeze is complete.

The stale prototype B10 2.5 mm² note is explicitly superseded in the canonical dataset by the later frozen **4.0 mm² minimum** Pump 1 requirement. This is source reconciliation, not a design change.

### 9. Protection metadata

EZ Wire's connection/BOM model does not replace the engineering protection register. Preserve `09-protection-metadata.csv` alongside the EZ Wire project.

Do not type guessed current-limit/fuse values into connector descriptions merely to remove TBDs.

### 10. Evidence holds

Before issuing production documentation from EZ Wire, review every row in `10-unresolved-evidence.csv`.

A released EZ Wire print/cut list must not imply that an open physical/electrical evidence item has been approved.

## Field mapping

| Canonical field | EZ Wire concept |
|---|---|
| `harness_id` | Wiring Harness project/name prefix |
| `device_id` | Device Library/custom device |
| `connector_id` | Connector short name |
| `cavity` | Connector pin/cavity |
| `description` | Cavity description |
| `connection_id` | Wire Number / Description canonical ID |
| `wire_type_id` | Enabled wire or cable type |
| `from_endpoint/from_cavity` | Connection starting cavity |
| `to_endpoint/to_cavity` | Connection destination cavity |
| `branch_id` | Visual diagram branch / route grouping |
| `approx_length_mm` | Provisional visual route length only |
| `prototype_cut_length_mm` | Prototype planning value only |
| `release_state/evidence_state` | External engineering hold metadata; retain in description/notes |

## Validation invariants

Any EZ Wire representation of this project must satisfy all of the following:

1. Pump 1 feed and dedicated return are each >=4.0 mm².
2. Pump 2 feed and dedicated return are each >=4.0 mm² when fitted.
3. B15 remains 10.0 mm² baseline unless formally revised.
4. B39 and B40 remain separate protected branches.
5. FT550 precision sensor-ground circuits do not terminate into high-current J-P02 load paths.
6. FT550 A21 is only connected through the X70 isolated dry-contact topology and never to +12 V.
7. CAN-H and CAN-L remain a twisted pair between FT550 and PMU CAN2 with X51 as a short service stub.
8. No hidden third CAN termination is introduced.
9. Injector front/rear and ignition front/rear channels remain distinct.
10. Direct injector drive versus Peak & Hold remains unresolved until evidence closes it.
11. PMU direct versus external pump switching remains unresolved until measured load evidence closes it.
12. All `TBD`, `VERIFY`, `PHYSICAL_ID_REQUIRED`, `DFM_GATED`, `EVIDENCE_GATED`, and `PROTECTION_VALUE_PENDING` states remain visible rather than being silently replaced.

## Canonical release state

`EZ_WIRE_CANONICAL_BASELINE_READY`

The next data maturity state is:

`EZ_WIRE_PHYSICAL_EVIDENCE_CLOSED`

followed by:

`EZ_WIRE_PRODUCTION_DATASET_RELEASED`

Only the latter should be used to generate final manufacturer cut lists without hold annotations.