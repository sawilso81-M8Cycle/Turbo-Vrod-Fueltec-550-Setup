# Manufacturer Release Index & Transmittal – Rev 2

**Project:** Turbo V-Rod Destroyer – FuelTech FT550 / ECUMASTER PMU16 / SparkPRO Harness  
**Release:** Harness Manufacturer Release Pack Rev 2  
**Purpose:** RFQ + Design-for-Manufacture Review + Controlled Prototype Planning  
**Current authority:** `RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

---

## 1. Transmittal instruction

This document is the front door to the Rev 2 manufacturer release package.

The recipient shall review the documents listed below and return the requested DFM, RFI, deviation, commercial and component-selection information before any electrically functional harness manufacture is authorised.

**Do not manufacture an electrically functional Rev 1 harness from this transmittal alone.**

The engineering release state must explicitly become:

`MANUFACTURING_RELEASED_REV1`

before functional manufacture begins.

---

## 2. Supersession

Rev 2 supersedes earlier manufacturer-facing guidance wherever a conflict exists.

Earlier drawings, worksheets and release-pack files remain useful as supporting engineering history only where they do not conflict with a later Rev 2 freeze or register.

Priority when documents conflict:

1. latest explicit Engineering Change / approved deviation;
2. this Rev 2 transmittal and DFM release pack;
3. latest architecture/freeze document for the affected system;
4. latest verification/decision register;
5. latest wire/cavity/BOM schedule;
6. earlier reference-pack material.

The manufacturer shall raise an RFI rather than deciding which conflicting requirement to use.

---

## 3. Mandatory read-first documents

### MFR-001
`00-Manufacturer-Release-Index-Rev2.md`  
This transmittal and release index.

### MFR-002
`Harness-Manufacturer-DFM-Release-Pack-Rev2.md`  
Defines permitted work, prohibited assumptions, DFM return requirements, build classes and hold points.

### MFR-003
`Pre-Manufacture-Release-Audit.md`  
Defines the release logic between RFQ, measurement prototype, functional prototype and repeat production.

### MFR-004
`G0-G1-Blocker-Burn-Down-Review.md`  
Identifies the remaining engineering blockers preventing unrestricted Rev 1 functional manufacture.

### MFR-005
`Master-Build-Blocker-Register.csv`  
Master blocker history and gate register.

---

## 4. Architecture and production freeze documents

### ECU / FT550
- `FT550-Interface-Verification-Register.csv`
- applicable FT550 interface freeze documentation in this release folder/repository.

### PMU16
- `PMU16-Connector-Terminal-Production-Freeze.md`
- `PMU16-Cavity-Terminal-Wire-Audit.md`
- `PMU16-Cavity-Terminal-Wire-Audit.csv`

### Fuel pumps
- `Fuel-Pump-Power-Interface-Freeze.md`
- `Fuel-Pump-Power-Interface-Verification-Register.csv`

**Locked rule:** 4.0 mm² minimum feed and 4.0 mm² dedicated return per fuel pump.

### Cooling / auxiliaries
- `Cooling-Aux-Power-Interface-Freeze.md`
- `Cooling-Aux-Power-Verification-Register.csv`

### Primary power
- `Primary-Power-Distribution-Freeze.md`
- `Primary-Power-Verification-Register.csv`

**B15 baseline:** 10 mm² battery/J-P01 to PMU main feed.

### Injector / ignition power
- `Engine-Critical-EPM-Power-Distribution-Freeze.md`
- `Engine-Critical-EPM-Power-Verification-Register.csv`

### Injectors
- `Injector-Electrical-Architecture-Freeze.md`
- `Injector-Electrical-Decision-Register.csv`

### Ignition / SparkPRO
- `Ignition-Coil-SparkPRO-Electrical-Freeze.md`
- `Ignition-Coil-SparkPRO-Verification-Register.csv`

### Trigger integrity
- `Trigger-Integrity-Freeze.md`
- `Trigger-Integrity-Verification-Register.csv`

### CAN / X51
- `CAN-Service-Interface-Production-Freeze.md`
- `CAN-Service-Verification-Register.csv`

### Two-Step / X70
- `X70-Two-Step-Relay-Hardware-Freeze.md`
- `X70-Two-Step-Relay-Verification-Register.csv`

### OEM interfaces X10-X23
- `OEM-Connector-Physical-Identification-Pack.md`
- `OEM-Connector-Physical-ID-Register.csv`

### X50 engineering/service interface
- `X50-Master-Engineering-Service-Connector-Freeze.md`
- `X50-Service-Connector-Cavity-Register.csv`

---

## 5. Commissioning / measurement-gate documents

These documents define evidence that remains required before the affected circuits receive final electrical release.

- `../Commissioning/Fuel-Pump-Verification-Pack.md`
- `../Commissioning/Fuel-Pump-Verification-Worksheet.csv`
- `../Commissioning/Fuel-Pump-Switching-Decision-Register.csv`
- `../Commissioning/Injector-Electrical-Verification-Pack.md`
- `../Commissioning/Injector-Electrical-Verification-Worksheet.csv`
- `../Commissioning/Injector-Driver-Final-Decision.csv`
- `../Commissioning/Coil-SparkPRO-Verification-Pack.md`
- `../Commissioning/Coil-SparkPRO-Verification-Worksheet.csv`
- `../Commissioning/Coil-Dwell-B40-Final-Decision.csv`
- `../Commissioning/Cooling-Load-Verification-Pack.md`
- `../Commissioning/Cooling-Load-Verification-Worksheet.csv`
- `../Commissioning/Cooling-Load-Final-Decision.csv`
- `../Commissioning/First-Power-First-Start-Master-Release-Gate.md`
- `../Commissioning/First-Power-First-Start-Verification-Register.csv`

The manufacturer is not expected to invent missing measurement values.

---

## 6. Files manufacturer must complete and return

### Required DFM return
`Harness-Manufacturer-DFM-Response-Register.csv`

Every applicable DFM row shall contain the proposed PN/method, evidence, availability, lead time, MOQ/cost impact where relevant, and comments.

### RFI register
`Harness-Manufacturer-RFI-Register.csv`

Use for ambiguity, unavailable parts, missing dimensions, cavity conflicts, terminal/wire incompatibility or any requirement that cannot be implemented exactly as released.

### Deviation register
`Harness-Manufacturer-Deviation-Register.csv`

Use for any proposed departure from the baseline. A deviation is not authorised until engineering marks it `APPROVED`.

---

## 7. Critical no-assumption rules

The manufacturer shall not assume:

- fuel-pump direct PMU drive is approved;
- injector direct FT550 drive is approved;
- final coil dwell is known;
- B11/B12/B39/B40 final protection values are known;
- PMU cavity numbers can be inferred from function names;
- an OEM connector is correct because it visually fits;
- X51 requires an additional CAN termination resistor;
- X50 may carry high-current circuits;
- FT550 A21 may receive +12 V;
- estimated branch lengths are production dimensions.

Raise an RFI instead.

---

## 8. Locked items manufacturer shall preserve

- FT550 + PMU16 + SparkPRO system architecture;
- separate engine-critical, auxiliary/high-current and precision-sensor current paths;
- 4.0 mm² minimum fuel-pump feed per pump;
- 4.0 mm² dedicated fuel-pump return per pump;
- 10 mm² B15 PMU-feed baseline;
- independent B39 injector and B40 ignition protection architecture;
- X70 dry-contact Two-Step architecture to FT550 A21;
- linear FT550↔PMU CAN backbone;
- X51 as short service CAN stub with no hidden termination;
- X50 as low/medium-current engineering/service connector only;
- CKP/CAM trigger-integrity requirements;
- OEM X10-X23 exact-connector or controlled-pigtail verification rule.

---

## 9. Requested quotation structure

Please quote separately:

1. DFM/NRE engineering review;
2. vehicle measurement / branch-dimension session if offered;
3. one measurement/mock-up harness if recommended;
4. one electrically functional Rev 1 prototype after release;
5. second identical prototype;
6. repeat-build price at quantities 2, 5 and 10 where practical;
7. Golden Harness/formboard creation;
8. test documentation;
9. optional spare service/repair pigtail kit;
10. freight and estimated lead time.

Identify customer-supplied components separately from manufacturer-supplied components.

---

## 10. Hold-point acknowledgement

The manufacturer shall acknowledge the following before accepting a functional build order:

- HP-1 DFM return accepted;
- HP-2 connector procurement accepted;
- HP-3 electrical blocker closure;
- HP-4 dimensional release;
- HP-5 crimp release;
- HP-6 pre-cover inspection;
- HP-7 final harness acceptance.

---

## 11. Current project state

**Released now:**

`RFQ_READY`

`DFM_REV2_RELEASED`

`PROTOTYPE_MEASUREMENT_PLANNING_ALLOWED`

**Not released yet:**

`MANUFACTURING_RELEASED_REV1`

`FIRST_POWER_AUTHORISED`

`REPEAT_BUILD_RELEASED`

---

## 12. Return package requested from manufacturer

Please return:

- completed DFM response register;
- RFIs;
- proposed deviations;
- connector/terminal datasheets and PNs;
- proposed wire/sleeving/boot specifications;
- DFM notes;
- quotation;
- proposed build/test process;
- proposed timing for measurement and prototype manufacture.

Engineering will review the return package and issue the next controlled release.
