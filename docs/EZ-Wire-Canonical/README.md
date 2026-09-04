# EZ Wire Canonical Harness Dataset

## Purpose

This folder converts the existing Turbo V-Rod FT550 / ECUMASTER PMU16 repository into a normalized, EZ Wire-ready canonical dataset **without changing any electrical design decisions**.

The canonical layer is an interchange model only. It does not redesign circuits, change wire sizes, assign missing connector cavities, invent protection values, change PMU logic, or resolve physical hardware evidence by assumption.

## EZ Wire model alignment

EZ Wire designs are built around harnesses, devices/connectors, connector cavities, wire types/cable types, cavity-to-cavity connections, branches/lengths, wire idents and BOM information. This folder mirrors that object model so the project can be entered/imported into EZ Wire with minimal translation.

Public EZ Wire documentation currently describes device-library import plus manual connector/connection creation and CSV BOM export. A documented arbitrary full-harness CSV import format is not presently published, so these files are intentionally canonical/interchange CSVs rather than falsely claiming to be a native EZ Wire import file.

## Authority order

When repository files disagree, canonical generation uses this authority order:

1. explicit later engineering freeze/release decisions;
2. `Production-Wire-Circuit-Master-Schedule.csv` for conductor/circuit intent;
3. `Connector-Cavity-Master-Schedule.csv` for connector/cavity evidence where consistent;
4. verified device pinout files such as `PMU16-Pinout-v1.2.csv`;
5. splice/junction and protection master schedules;
6. dimensional/formboard files;
7. older prototype/estimate documents.

No value is silently promoted across an evidence gate.

## Locked electrical decisions preserved

- Pump 1 feed: **4.0 mm² minimum**.
- Pump 1 dedicated return: **4.0 mm² minimum**.
- Pump 2 feed: **4.0 mm² minimum**.
- Pump 2 dedicated return: **4.0 mm² minimum**.
- B15 PMU main feed: **10.0 mm² baseline**.
- B39 injector power and B40 ignition/SparkPRO power remain separate protected branches.
- FT550 precision sensor ground remains separate from uncontrolled high-current returns.
- CAN remains a linear FT550 ↔ PMU CAN2 backbone at **1 Mbps**, with a short X51 service stub and no hidden service termination.
- Two-Step remains `PMU O11 -> X70 TE 1393292-5 relay coil -> isolated dry contact -> FT550 A21`.
- **+12 V is prohibited from the FT550 A21 dry-contact side.**
- Direct PMU versus external fuel-pump power stage remains measurement-gated.
- Injector direct-drive versus Peak & Hold remains evidence-gated.

## Canonical files

- `01-harnesses.csv` — top-level EZ Wire harness containers.
- `02-devices.csv` — reusable ECU/PDM/sensor/load/device records.
- `03-connectors.csv` — connector definitions.
- `04-cavities.csv` — cavity descriptions and pin evidence.
- `05-wire-types.csv` — normalized metric wire types and special cable definitions.
- `06-connections.csv` — one canonical row per released/provisional conductor path.
- `07-splices-junctions.csv` — splice, stud and junction nodes.
- `08-branches-lengths.csv` — EZ Wire visual-diagram branch/length seed data.
- `09-protection-metadata.csv` — protection/current-limit metadata, including unresolved values.
- `10-unresolved-evidence.csv` — physical/electrical hold points that must remain visible during EZ Wire entry.
- `EZ-WIRE-MAPPING.md` — field mapping and recommended entry sequence.

## Release state

This dataset is `EZ_WIRE_CANONICAL_BASELINE_READY`.

It is suitable for:

- creating EZ Wire harness projects;
- creating/importing reusable device definitions;
- populating connectors and cavity descriptions;
- enabling wire/cable types;
- creating the circuit connections;
- laying out branches and provisional lengths;
- validating circuit completeness against the repository.

It is **not** permission to convert `TBD`, `VERIFY`, `PHYSICAL_ID_REQUIRED`, `DFM_GATED`, `EVIDENCE_GATED`, or `PROTECTION_VALUE_PENDING` fields into released production values.