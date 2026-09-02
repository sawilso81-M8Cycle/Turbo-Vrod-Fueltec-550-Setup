# Prototype Harness Acceptance & Golden Harness Qualification – Rev 1

## Purpose

Define the controlled acceptance path after an electrically functional Rev 1 harness has been authorised and manufactured. This gate prevents a prototype that merely powers up from becoming the repeat-production master without dimensional, electrical, thermal, serviceability and vehicle-fit evidence.

## Entry condition

This process may begin only after:

`MANUFACTURING_RELEASED_REV1`

has been formally issued.

A harness built under RFQ/DFM or measurement-only authority cannot be promoted directly to Golden Harness status.

## Qualification stages

### GH-1 Manufacturer pre-cover inspection

Before final sleeving/boots permanently hide construction, record:

- complete harness laid out against formboard/drawing;
- every branch label;
- connector IDs and cavity orientation;
- splice locations;
- CAN twisted-pair construction;
- CKP/CAM trigger routing/shielding;
- fuel-pump 4.0 mm² feeds and dedicated 4.0 mm² returns;
- B15 10 mm² main feed;
- B39/B40 segregation;
- sensor-ground segregation;
- heat-protection locations;
- strain relief and service loops;
- all approved deviations.

Engineering must accept the pre-cover evidence before final closure where practical.

### GH-2 Bench electrical acceptance

With FT550, PMU16, SparkPRO and sensitive devices disconnected as required, complete:

- 100% point-to-point continuity;
- cavity mapping;
- polarity;
- no unintended cross-circuit continuity;
- isolation from +12 V and ground as applicable;
- power-ground vs sensor-ground segregation;
- CAN-H/CAN-L polarity and isolation;
- no hidden CAN termination;
- X70 A21 dry-contact isolation;
- service-power backfeed test;
- splice verification;
- protective-device location/value verification;
- connector latch/seal/secondary-lock inspection.

No electronics shall be connected to a harness with unresolved electrical discrepancies.

### GH-3 Dimensional / vehicle-fit acceptance

Install the harness on the motorcycle without forcing connectors or branches into position.

Verify:

- FT550, PMU16 and SparkPRO branch lengths;
- fuel-pump branch lengths;
- injector and coil service loops;
- full steering-lock movement where applicable;
- full suspension movement for VSS/rear branches;
- turbo/exhaust clearance;
- radiator/fan clearance;
- clutch/Two-Step branch movement;
- access to X50/X51/X70 and service connectors;
- no connector carries harness weight;
- no branch is tensioned at full movement;
- no excessive loop can contact hot/rotating components;
- bodywork/tank/seat can be installed without crushing the loom.

Every dimensional correction shall be recorded in the Golden Harness correction register before repeat manufacture.

### GH-4 First-power qualification

Follow the separate First-Power/First-Start Master Release Gate.

Minimum harness-specific evidence includes:

- correct protected supply at FT550/PMU/SparkPRO;
- expected grounds and voltage drops;
- no smoke/heating/odour;
- no unexpected current draw;
- stable 5 V reference;
- stable CAN communications;
- correct sensor plausibility;
- correct X70 Two-Step truth table;
- fuel-pump outputs behave according to the released direct/external-stage architecture;
- fan/pump outputs behave according to released architecture.

### GH-5 Cranking / first-start qualification

Record:

- battery voltage during cranking;
- FT550 and PMU minimum voltage;
- CAN errors/resets;
- CKP/CAM synchronisation quality;
- injector and SparkPRO behaviour;
- B39/B40 voltage drop;
- pump voltage/current;
- abnormal harness/connector heating;
- ignition noise effects;
- Two-Step/clutch logic where safe to verify.

A successful engine start does not override an electrical or thermal failure.

### GH-6 Hot operational qualification

After controlled operation, inspect and record temperatures at high-current connectors, PMU terminals, B15 junctions, pump interfaces, B39/B40 connections, X70 and heat-exposed loom sections.

Reinspect:

- turbo/exhaust clearance after heat growth;
- loom movement/chafe marks;
- connector retention;
- service-loop movement;
- CAN/trigger stability;
- protection trips or PMU logged faults.

### GH-7 Post-test teardown inspection

Where accessible, inspect for:

- terminal push-back;
- fretting;
- seal displacement;
- insulation marking/chafe;
- sleeve glazing/heat damage;
- loosened junction hardware;
- strained branches;
- evidence of water/contaminant ingress;
- relay/socket heating;
- connector discolouration.

## Golden Harness promotion

The prototype may be promoted only when all applicable acceptance rows are PASS and all corrections are incorporated into controlled as-built documents.

Promotion state:

`GOLDEN_HARNESS_VALIDATED`

This means the accepted physical harness, as-built BOM, cavity schedule, splice schedule, branch dimensions, protection schedule and test evidence together define the production master.

The physical harness alone is not sufficient configuration control.

## Repeat-build release

Repeat manufacture additionally requires:

- Golden Harness/formboard revision frozen;
- all prototype deviations incorporated or closed;
- all temporary measurement notes removed from production documents;
- final connector and terminal PNs frozen;
- final protection values frozen;
- final wire sizes frozen;
- final branch dimensions frozen;
- manufacturer test plan frozen;
- serial/build traceability established.

Final state:

`REPEAT_BUILD_RELEASED`

## Change control after Golden Harness

Any change to circuit function, conductor size, connector family, terminal, splice position, protection, branch dimension, CAN topology, trigger wiring or high-current routing requires controlled review.

A dimensional change that affects fit or movement requires re-fit verification. An electrical change requires the applicable electrical acceptance tests to be repeated.
