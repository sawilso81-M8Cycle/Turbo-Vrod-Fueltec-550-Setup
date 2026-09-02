# Harness Manufacturer DFM Release Pack – Rev 2

## Project

Turbo V-Rod Destroyer – FuelTech FT550 + ECUMASTER PMU16 + SparkPRO complete replacement harness.

## Purpose

Rev 2 consolidates the engineering freezes developed after the original manufacturer pack and provides the harness builder with a controlled path for quotation, design-for-manufacture review, prototype measurement work and eventual Rev 1 manufacturing release.

This document does **not** by itself authorise an electrically functional harness build.

Current release state:

`DFM_REV2_RELEASED / RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

## Manufacturer scope now authorised

The harness builder may:

- review the complete release pack;
- provide RFQ/NRE/repeat-build pricing;
- nominate exact connector housings, contacts, seals, cavity plugs, boots and tooling where documents explicitly mark those items DFM-gated;
- review conductor sizes and manufacturability without silently downsizing them;
- propose splice, branch, sleeving, strain-relief and formboard methods;
- identify unavailable/obsolete components;
- submit RFIs and controlled substitution proposals;
- participate in vehicle measurement and first Golden Harness development.

The builder may **not**:

- alter FT550/PMU/SparkPRO circuit functions;
- merge sensor ground with high-current ground;
- reduce the locked 4.0 mm² fuel-pump feeds/returns;
- add hidden CAN termination;
- substitute unverified OEM sensor connectors;
- route +12 V onto the FT550 A21 Two-Step dry-contact side;
- change injector direct-drive/Peak & Hold architecture without engineering disposition;
- choose final fuse/eFuse/current-limit values where measurement gates remain open;
- infer missing cavity numbers or wire functions.

## Architecture summary

### ECU

FuelTech FT550 using the official connector-kit/custom-harness strategy. Front/rear injector commands remain A1/A2. Two-Step input remains A21 under the frozen Two-Step architecture.

### Power management

ECUMASTER PMU16. Exact hardware revision and every used cavity remain subject to the PMU cavity-terminal-wire audit before crimp release.

### Ignition

FT550 command → SparkPRO → retained V-Rod coils. Dwell/current and B40 final protection remain measurement gated.

### Fuel pumps

Each pump uses minimum 4.0 mm² feed and dedicated 4.0 mm² return. HDSCS/MCP-class main-harness service interface is frozen. Final direct-PMU vs external power-stage decision remains dependent on actual pump current/inrush/thermal testing.

### Cooling loads

B11 radiator-fan prototype baseline 2.5 mm². B12 charge-cooler pump prototype baseline 2.0 mm² if fitted. Final direct-PMU/external-stage and protection decisions remain measurement gated.

### Primary power

B15 main PMU feed production baseline 10 mm². Battery positive distribution uses J-P01; high-current return architecture uses J-P02. Final master protection value remains simultaneous-load gated.

### Engine-critical supplies

B39 injector supply and B40 ignition/SparkPRO supply are independently protected branches. Their final protection values remain measurement gated.

### CAN/service

FT550 ↔ PMU16 remains a linear CAN backbone. X51 is the short sealed CAN service stub. No hidden termination in X51. X50 is a low/medium-current engineering/service interface and shall not carry primary or fuel-pump current.

### Two-Step

PMU O11 commands X70 relay coil. X70 normally-open dry contact grounds FT550 A21 when commanded. Selected relay baseline is TE 1393292-5/V23074A1001A402; exact socket/carrier remains DFM-gated.

### OEM interfaces

X10–X23 must resolve to either `EXACT_CONNECTOR_FROZEN` or `OEM_PIGTAIL_FROZEN`. Visual similarity is not sufficient evidence.

## Required manufacturer DFM return

Return one completed row for every item in `Harness-Manufacturer-DFM-Response-Register.csv` plus supporting datasheets/photographs where requested.

Key responses required:

1. X70 relay socket/carrier PN and terminals;
2. X50 proposed exact housing/contact family and final cavity count;
3. X51 exact DTM housing/contact/cap PNs;
4. HDSCS/MCP fuel-pump service-interface sourcing confirmation;
5. PMU terminal family availability and crimp tooling;
6. FT550 terminal tooling and connector-kit build method;
7. proposed X10–X23 exact connector/repair-pigtail solutions;
8. proposed wire family/specification by conductor size;
9. high-temperature sleeve/boot strategy near turbo/exhaust;
10. branch-splice method;
11. strain-relief/booting method;
12. label/heat-shrink identification method;
13. continuity/hipot or insulation-test capability;
14. pull-test capability;
15. formboard/Golden Harness process;
16. repeat-build document-control process;
17. component substitution control;
18. lead time, MOQ, NRE and repeat pricing.

## Wire-size control

The manufacturer may recommend an **upsize** based on terminal, thermal, bundling or voltage-drop concerns.

A proposed **downsize** requires an RFI with calculation and engineering approval before use.

The following shall not be downsized in Rev 1 without explicit engineering change:

- fuel-pump feeds: 4.0 mm² minimum;
- fuel-pump dedicated returns: 4.0 mm² minimum;
- B15 PMU main feed: 10 mm² baseline.

B11, B12, B39 and B40 remain measurement-gated baselines and may require upsize.

## RFI process

Use `Harness-Manufacturer-RFI-Register.csv`.

An RFI is mandatory when:

- a connector cannot be sourced;
- a terminal does not accept the specified conductor;
- a cavity/function is ambiguous;
- a proposed route creates heat/movement risk;
- CAN topology would change;
- a sensor-ground/reference circuit would change;
- a substitute component differs electrically or mechanically;
- protection/current capability is uncertain;
- a dimension is missing and cannot be safely derived from the physical bike.

No undocumented assumption is permitted.

## Deviation process

Use `Harness-Manufacturer-Deviation-Register.csv`.

Every deviation requires status `APPROVED` before manufacture. Approval must identify the affected drawing/register/BOM revision.

## Build classes

### Class A – RFQ/DFM

State: `RFQ_READY`

No physical harness manufacture authorised.

### Class B – measurement/mock-up

State: `PROTOTYPE_MEASUREMENT_BUILD_ONLY`

May establish branch lengths, breakout orientation, mounting and service loops. Not released for first power.

### Class C – electrically functional Rev 1 prototype

State: `MANUFACTURING_RELEASED_REV1`

Requires applicable G0/G1 blockers closed and controlled disposition of remaining G2 physical gates.

### Class D – repeat production

State: `GOLDEN_HARNESS_VALIDATED / REPEAT_BUILD_RELEASED`

Requires accepted prototype, as-built documentation, test evidence and controlled Golden Harness/formboard.

## Documents manufacturer shall review

At minimum:

- Pre-Manufacture Release Audit;
- G0/G1 Blocker Burn-Down Review;
- Master Build Blocker Register;
- PMU16 Connector Terminal Production Freeze;
- PMU16 Cavity Terminal Wire Audit;
- FT550 Interface Verification Register;
- Fuel-Pump Power Interface Freeze;
- Cooling Aux Power Interface Freeze;
- Primary Power Distribution Freeze;
- Engine-Critical EPM Power Distribution Freeze;
- Injector Electrical Architecture Freeze;
- Ignition Coil/SparkPRO Electrical Freeze;
- Trigger Integrity Freeze;
- CAN Service Interface Production Freeze;
- X70 Two-Step Relay Hardware Freeze;
- OEM Connector Physical Identification Pack;
- X50 Master Engineering/Service Connector Freeze;
- First-Power/First-Start Master Release Gate;
- dimensional freeze/branch-length documents;
- current released BOM and wire schedule.

## Manufacturer hold points

**HP-1 DFM return accepted** – no component substitutions outstanding.

**HP-2 Connector procurement accepted** – exact housings/contacts/seals/tooling accepted.

**HP-3 Electrical blocker closure** – pump/injector/ignition/cooling measurement gates resolved where required for build.

**HP-4 Dimensional release** – measured dimensions or approved Golden Harness measurement exception.

**HP-5 Crimp release** – exact cavity/terminal/wire schedule signed.

**HP-6 Pre-cover inspection** – photographs, continuity, polarity and branch dimensions accepted before final sleeving.

**HP-7 Harness acceptance** – completed test report and as-built pack accepted.

## Required final manufacturer deliverables

For the functional Rev 1 harness:

- as-built BOM;
- as-built wire/circuit schedule;
- connector cavity schedule;
- splice schedule;
- branch-length/formboard drawing;
- component datasheets for approved substitutions;
- crimp/pull-test record;
- continuity/isolation report;
- CAN polarity report;
- pre-cover photographs;
- final harness photographs;
- deviation register;
- serial/build number;
- manufacturing date;
- builder identification;
- Golden Harness revision once validated.

## Current release

Rev 2 is released to the manufacturer for **quotation and DFM review now**.

It remains explicitly:

`FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

until the engineering release register is promoted to `MANUFACTURING_RELEASED_REV1`.
