# Harness Build Release Gate Review

## Purpose

Provide one authoritative go/no-go register for releasing the Turbo V-Rod FT550 / PMU16 harness from engineering/RFQ status into Rev 1 prototype manufacture and, later, repeat manufacture.

This document does not replace the detailed source files. It consolidates their release-critical state.

## Release ladder

`RFQ_READY / BUILD_DATA_OPEN`
→ `BUILD_GATE_REVIEW_ACTIVE`
→ `REV1_PROTOTYPE_BUILD_AUTHORISED`
→ prototype manufacture
→ physical fit / electrical acceptance
→ `MANUFACTURING_RELEASED_REV1`
→ `GOLDEN_HARNESS_VALIDATED`

## Gate classes

- **G0 Safety / architecture**: must be closed before powered vehicle testing.
- **G1 Build critical**: must be closed or formally dispositioned before a harness builder crimps the affected branch.
- **G2 Prototype fit critical**: may remain estimated for initial quotation but must be closed during/after prototype fit before repeat manufacture.
- **G3 Optional / DNP**: must be explicitly fitted or DNP. It cannot remain ambiguous.

## Current consolidated status

### Closed / strong baseline

- FT550 + PMU16 + SparkPRO-2 architecture defined.
- CAN backbone architecture defined.
- sensor/reference-ground segregation defined.
- permanent circuit IDs defined.
- low-current conductor classes defined.
- fuel-pump feed and dedicated return fixed at **4.0 mm² per pump**.
- fuel-pump switching architecture intentionally measurement gated: direct PMU drive may only be approved after actual pump current/inrush/thermal verification; otherwise external power stage required.
- Two-Step request architecture defined: PMU permission → sealed dry-contact relay interface → FT550 A21 ground request.
- +12 V is prohibited from FT550 A21.
- OEM clutch switch strategy and DTM service break defined.
- prototype branch-length estimates exist.
- D00-D10 physical datum framework exists.
- manufacturer RFQ, build record and acceptance test exist.
- OEM connector strategy defined: exact connector where positively identified; otherwise verified OEM repair pigtail + controlled service break.

## Build release blockers

### BG-001 Fuel pump electrical verification — G0/G1

Required evidence:
- exact pump make/model;
- measured steady current at representative system voltage/pressure;
- cold/hot start inrush or peak current;
- connector and terminal continuous/peak capability;
- voltage drop on 4.0 mm² feed and 4.0 mm² dedicated return;
- thermal check at connector/terminal;
- PMU O1/O2 direct-drive suitability determination.

Disposition must be exactly one of:
- `DIRECT_PMU_DRIVE_APPROVED`, or
- `EXTERNAL_POWER_STAGE_REQUIRED`.

### BG-002 High-current load closure — G1

Close actual current/inrush and protection for:
- B11 radiator fan;
- B12 charge/intercooler pump if fitted;
- B15 PMU main feed aggregate load;
- B39 injector common supply;
- B40 ignition/coil common supply.

### BG-003 PMU connector / terminal final selection — G1

Confirm each used PMU cavity has the correct Sicma terminal for conductor size and current. The PMU main feed remains via the specified stud architecture. Do not force a conductor into an incompatible cavity terminal.

### BG-004 FT550 connector/service-terminal build method — G1

Choose one:
- use FuelTech supplied PROBIKE/approved harness and splice/service-break architecture; or
- build from the official FT550 Connector Kit/service terminals.

FuelTech publishes an FT550 Connector Kit containing A/B connectors and terminals, so improvised ECU terminals are not acceptable.

### BG-005 OEM engine connector physical identification — G1

Physically verify X10-X23 before final crimping:
- CKP;
- TPS;
- MAP;
- ECT;
- IAT;
- VSS;
- front/rear injector;
- front/rear coil.

Where an exact mating housing is not positively identified, preserve a verified OEM repair pigtail and transition through the approved service-break family.

### BG-006 Fuel-pump connector — G0/G1

Select a connector/terminal system that:
- accepts 4.0 mm² feed and return without conductor folding/reduction;
- is sealed for the installed environment;
- has continuous and transient current margin for the verified pump;
- has positive retention and serviceability.

DTM is not authorised for the pump power circuit.

### BG-007 X50/X51 service connectors — G1

Freeze housings, contacts, seals, cavity plugs, caps and keying. X51 CAN service branch must preserve CAN topology and not introduce unintended permanent termination.

### BG-008 Two-Step X70 relay hardware — G0/G1

Freeze the actual sealed relay/holder and suppression arrangement. Verify:
- O11 energises relay coil correctly;
- relay contact is dry SPST-NO;
- contact closes FT550 A21 to approved ground only;
- O11/power loss opens A21;
- +12 V cannot reach A21;
- release time is acceptable for clutch-launch transition.

### BG-009 Injector electrical architecture — G0/G1

Close injector impedance/current evidence and disposition direct FT550 drive versus Peak & Hold. B36-B38 must be either fitted per approved architecture or explicitly DNP.

### BG-010 Physical component mounting locations — G2

Freeze FT550, PMU16, SparkPRO, X70, boost solenoid, service connector and other major device positions before dimensional release.

### BG-011 B01-B44 physical dimensions — G2

Replace prototype estimates with routed motorcycle measurements. B20-B31 must be defined or explicitly DNP.

### BG-012 Steering/suspension movement — G0/G2

Verify B41 clutch branch at full-left, centre and full-right steering lock. Verify VSS/rear branches through required suspension movement. No terminal or wire may carry movement load.

### BG-013 Turbo/exhaust thermal clearance — G0/G2

Record hot-zone clearances and heat-protection lengths. Heat sleeve is not permission to route against a hot surface.

### BG-014 Formboard release — G2

Populate the 1:1 formboard from accepted dimensions, breakouts, clocking, boots, covering, splices, heat protection and clamp points.

### BG-015 Manufacturer DFM review — G1

Harness builder must report:
- proposed material substitutions;
- terminal/tooling limitations;
- branch/boot concerns;
- splice-method changes;
- relay implementation;
- test capability;
- any conflict between drawings and physical connector hardware.

No silent substitution is allowed.

## Prototype build authority

`REV1_PROTOTYPE_BUILD_AUTHORISED` may be granted when all G0 and G1 items applicable to the branches being built are PASS or have a written engineering disposition. G2 dimensional items may use the released prototype cut allowances only when the build is explicitly labelled prototype and the builder records the as-built dimensions.

## Repeat manufacture authority

Repeat manufacture is prohibited until:
- prototype fits without forced connector position or unapproved cutting;
- final dimensions are captured;
- all electrical acceptance tests pass;
- connector/terminal BOM is frozen;
- deviations are incorporated into the released revision;
- Golden Harness photographs and as-built records are archived.

## Current state

**`BUILD_GATE_REVIEW_ACTIVE / REV1_PROTOTYPE_BUILD_NOT_YET_AUTHORISED`**
