# Turbo V-Rod FT550 / PMU16 Harness – Current Manufacturer Construction Package

## Purpose

This folder is a duplicated manufacturer-facing snapshot of the current controlling harness information held elsewhere in the repository. It is intended to give the harness builder one working folder for DFM, quotation, prototype planning and, only after formal release, construction.

## Current authority

`RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

Do **not** manufacture an electrically functional Rev 1 harness until engineering explicitly issues:

`MANUFACTURING_RELEASED_REV1`

## Conflict priority inside this folder

If two duplicated files disagree, use this priority:

1. this README and later explicit Engineering Change / approved deviation;
2. `01-Production-Wire-Circuit-Master-Schedule.csv`;
3. `02-Connector-Cavity-Master-Schedule.csv`;
4. `03-Splice-Junction-Master-Schedule.csv`;
5. `04-Protection-Fuse-PMU-Current-Limit-Master-Schedule.csv`;
6. exact verified hardware/terminal evidence;
7. prototype/estimated dimensional schedules.

Raise an RFI instead of choosing between conflicting requirements.

## Critical locked corrections

### Fuel pumps

The **current controlling requirement is minimum 4.0 mm² feed and 4.0 mm² dedicated return for each fuel pump**.

An older prototype length schedule contains a legacy Pump 1 line showing `2.5 MINIMUM`. That value is **SUPERSEDED** and must not be used for construction.

Use:

- Pump 1 feed: **4.0 mm² minimum**;
- Pump 1 dedicated return: **4.0 mm² minimum**;
- Pump 2 feed: **4.0 mm² minimum**;
- Pump 2 dedicated return: **4.0 mm² minimum**.

Final direct-PMU versus external relay/power-stage architecture remains measurement gated until exact pump current and PMU capability are verified.

### B15

B15 battery/J-P01 to PMU primary feed baseline is **10.0 mm²**, with final protection evidence gated.

### B39 / B40

Injector supply B39 and ignition/SparkPRO supply B40 remain independent protected branches. Final protection values remain evidence gated.

### Two-Step

Current production architecture bypasses the custom PCB. Use the replaceable X70 relay sub-harness architecture:

`PMU O11 -> X70 relay coil -> isolated dry contact -> FT550 A21`

**+12 V must never be connected to FT550 A21.**

### CAN

Maintain a linear FT550 ↔ PMU CAN backbone, short X51 service stub and no hidden termination resistor.

### Sensor grounding

Precision sensor grounds/references must not be merged into uncontrolled high-current return paths.

## Folder contents

- `01-Production-Wire-Circuit-Master-Schedule.csv` – conductor-level construction baseline.
- `02-Connector-Cavity-Master-Schedule.csv` – interface/cavity map and release state.
- `03-Splice-Junction-Master-Schedule.csv` – controlled electrical join points.
- `04-Protection-Fuse-PMU-Current-Limit-Master-Schedule.csv` – branch protection baseline and pending values.
- `05-Prototype-Cable-Size-Length-Schedule.csv` – approximate/pre-measurement branch lengths only; see fuel-pump correction above.
- `06-Connector-Purchasing-BOM.csv` – connector/terminal procurement baseline.
- `07-PMU16-Cavity-Terminal-Wire-Audit.csv` – PMU cavity/wire/terminal verification status.
- `08-Manufacturing-Requirements.md` – workmanship and process requirements.
- `09-Harness-Formboard-Specification.md` – formboard/dimensional controls.
- `10-Harness-Build-Traveller-Template.csv` – production traveller/hold points.
- `11-Manufacturer-DFM-Response-Register.csv` – manufacturer return sheet.

## Manufacturer must return

Please complete and return the DFM response register together with:

- exact proposed connector/terminal/seal PNs;
- crimp tooling and pull-test method;
- wire family/specification;
- sleeving/heat-protection proposal;
- splice method;
- formboard/measurement method;
- RFIs for every unresolved cavity, dimension or hardware conflict;
- proposed deviations;
- quotation and lead time.

## No-assumption list

Do not assume:

- estimated branch lengths are final production dimensions;
- pump direct-PMU drive is approved;
- B11/B12/B39/B40 protection values are final;
- unresolved PMU cavity assignments may be inferred;
- an OEM connector is correct because it physically fits;
- X51 needs an extra termination resistor;
- FT550 A21 may receive +12 V.

## Release progression

`RFQ_AND_DFM_ALLOWED`

→ physical measurement / hardware verification

→ electrical load verification / protection freeze

→ `HARNESS_DOCUMENT_SET_FROZEN`

→ `MANUFACTURING_RELEASED_REV1`

→ prototype build

→ HP6 pre-cover inspection

→ HP7 final harness acceptance.
