# Repository Master Index & Physical Build Readiness Audit

## Purpose

Convert the completed engineering-document roadmap into one controlled build-readiness view.

The repository now contains architecture, harness manufacturing, commissioning, dyno, boost, launch, track, race-release, Golden Harness and handover documentation. The remaining job is not to create more theoretical stages. It is to close physical evidence and release blockers until the project is genuinely buildable, testable and repeatable.

## Current repository architecture

### Core project control
- `README.md`
- `ROADMAP.md`
- `docs/Project-Master-Release-Dashboard.md`
- `docs/Project-Master-Completion-Matrix.csv`
- `docs/Release/`

### Vehicle / FT550 architecture
- `docs/VRXSE-FT550/`
- `docs/HD-Style-Wiring/`
- `docs/FuelTech-Official-Manuals/`
- `docs/Harley-VRXSE-Official-References/`

### PMU / power control
- `docs/ECUMASTER-PMU16/`
- `docs/PMU-Control/`
- `docs/EPM-Driver-Interface/`

### CAN / communications
- `docs/CAN-Backbone/`

### Sensors
- `docs/Sensor-Expansion/`

### Two-Step / launch control
- `docs/Launch-Control/`
- `docs/HD-Style-Wiring/Sheet-07-Two-Step-Clutch-Launch.md`

### Harness production
- `docs/Production-Harness-Milestone/`
- `docs/Harness-Manufacturer-Release-Pack/`

### Commissioning / validation
- `docs/Commissioning/`
- `docs/Boost-Control/`
- `docs/Track-Validation/`

### Final handover
- `docs/Handover/`

## Audit principle

A document existing in Git does not mean the corresponding physical requirement is verified.

Status meanings:

- `DOCUMENTED` = design/procedure exists;
- `PROVISIONAL` = engineering baseline exists but physical/source evidence is incomplete;
- `BLOCKED` = required evidence/decision prevents release;
- `READY_FOR_TEST` = documentation is sufficient to perform the physical test;
- `VERIFIED` = physical/source evidence has been captured and accepted;
- `RELEASED` = all upstream gates required for the specific release have passed;
- `DNP` = deliberately not populated / not fitted, with rationale;
- `SUPERSEDED` = retained only for history.

## Highest-priority physical blockers

### P0. Harness dimensional freeze

The repository contains a prototype length schedule, bike-side measurement worksheet, B01-B44 dimensional freeze worksheet, formboard specification and physical dimension capture register. Approximate dimensions are not production release dimensions.

Required closure:

1. place all major components in their final physical locations;
2. define datum points and branch breakouts;
3. measure B01-B44 on the actual motorcycle;
4. include service loops, steering/suspension movement and thermal routing allowances;
5. update production length/formboard data;
6. sign dimensional freeze.

Release state: `PHYSICAL_HARNESS_DIMENSIONS_FROZEN`

### P0. OEM connector / terminal physical identification

The repository contains connector identification and pigtail verification registers. Any unresolved OEM housing, terminal, seal, cavity orientation or mating identity remains a manufacturing blocker.

Required closure:

- photograph/identify each unresolved connector;
- confirm cavity orientation from the mating face;
- confirm terminal family and wire-size compatibility;
- confirm seals/cavity plugs;
- verify pigtails electrically before promoting them to production.

Release state: `OEM_CONNECTOR_SET_VERIFIED`

### P0. Fuel pump exact hardware and current verification

Pump feeds/returns remain locked at minimum 4.0 mm² for the current design baseline. Final protection/switching depends on the exact installed pumps and measured current.

Required closure:

- record Pump 1 and Pump 2 manufacturer/PN;
- obtain manufacturer electrical data where available;
- measure steady-state and relevant inrush/current behaviour under representative voltage/pressure/load;
- confirm connector/terminal suitability;
- decide PMU direct switching versus external relay/power stage based on verified load and PMU capability;
- freeze protection settings.

Release state: `FUEL_PUMP_POWER_ARCHITECTURE_FROZEN`

### P0. Injector exact hardware / driver compatibility

Required closure:

- record injector PN;
- confirm impedance/driver requirement and characterization source;
- verify FT550/driver architecture compatibility;
- freeze B39 supply/protection;
- freeze calibration data used for first start.

Release state: `INJECTOR_ARCHITECTURE_FROZEN`

### P0. Coil / SparkPRO / dwell verification

Required closure:

- record exact coil PN and SparkPRO hardware revision;
- verify coil primary characteristics and SparkPRO compatibility;
- establish dwell from verified source/test evidence;
- confirm B40 supply/protection;
- archive released ignition configuration.

Release state: `IGNITION_ARCHITECTURE_FROZEN`

### P0. Final protection coordination

B15, B39, B40, pump, fan and auxiliary protection must be based on verified loads and conductor/terminal capability.

Required closure:

- complete measured load campaign;
- populate final current limits/fuses;
- confirm discrimination/fault containment;
- confirm no protection value exceeds downstream conductor/terminal capability;
- freeze protection master schedule.

Release state: `PROTECTION_COORDINATION_FROZEN`

## P1 blockers before harness manufacturer release

### Physical PMU/FT550/SparkPRO locations
Confirm mounting, connector access, bend radius, serviceability and heat/water exposure.

### X70 final hardware
The project baseline uses the isolated X70 relay architecture for Two-Step. Confirm the production relay/socket/terminal set and ensure any earlier PCB concept remains superseded unless deliberately reinstated through change control.

### CAN backbone
Confirm physical endpoint positions, termination, service connector location, bitrate/configuration and harness routing.

### Sensor connector set
Confirm all OEM and added sensor connectors, seals, wire gauges and calibration identity.

### Ground termination hardware
Confirm battery/chassis/engine/ECU/PMU ground studs, ring terminals, fasteners and physical routing while preserving the designed current-path segregation.

## P2 blockers before first power

- harness HP6 pre-cover inspection PASS;
- HP7 final acceptance PASS;
- installed harness serial recorded;
- as-built deviations closed;
- FT550/PMU/SparkPRO configurations archived;
- no unresolved continuity/isolation faults;
- 5 V reference and sensor ground verified;
- CAN termination/polarity verified;
- fuel system leak test complete;
- first-power configuration evidence record complete.

Release state: `FIRST_POWER_READY`

## P3 blockers before first start

- first-power dead-engine commissioning accepted;
- trigger/sync evidence accepted;
- injector configuration verified;
- ignition/dwell verified;
- oil-system preparation complete;
- fuel pressure verified;
- wideband operational;
- boost and Two-Step disabled for initial start;
- emergency shutdown available.

Release state: `FIRST_START_READY`

## P4 validation gates

Physical build completion does not bypass the established gates:

1. first start;
2. low-load heat cycle and sensor correlation;
3. no-boost/light-load validation;
4. wastegate/base-boost validation;
5. progressive dyno load;
6. controlled boost enablement;
7. Two-Step commissioning;
8. track launch validation;
9. final race validation;
10. Golden Harness validation;
11. repeat-build qualification;
12. project handover.

## Duplicate / overlapping documentation policy

The repository intentionally contains historical and progressive documents. Where multiple documents cover similar commissioning stages, the newest explicit release pack/checklist should control execution unless a master dashboard/release manifest identifies another document as controlling.

Do not delete historical engineering evidence merely because a later pack supersedes it. Mark superseded material in release control when ambiguity could affect manufacture or commissioning.

## Build-readiness target

The immediate target is:

`PHYSICAL_BUILD_INPUTS_VERIFIED`

That state requires all P0 items to be closed with evidence, not assumptions.

It then permits:

`HARNESS_MANUFACTURER_RELEASE_READY`

followed by the existing HP1-HP7 manufacturing and acceptance gates.

## Next execution sequence

The recommended order is:

1. physical bike measurement session;
2. connector/terminal identification session;
3. exact pump/injector/coil hardware capture;
4. electrical load measurement campaign;
5. final protection coordination;
6. update/freeze production schedules;
7. generate manufacturer release ZIP;
8. obtain manufacturer DFM response;
9. build prototype harness;
10. HP6/HP7 acceptance;
11. install and begin first-power commissioning.

This sequence should now drive future milestones. New documentation should be created only where it closes a specific physical blocker, records evidence or controls a required test/release.
