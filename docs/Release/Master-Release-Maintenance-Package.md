# Master Release & Maintenance Package

## Purpose

This document is the authoritative release spine for the Turbo V-Rod Destroyer FT550 / ECUMASTER PMU-16 system. It consolidates configuration identity, hardware and wiring revision, software/calibration identity, verification status, event inspection, maintenance expectations and change-control rules.

No operational release state is valid unless the configuration recorded here matches the physical motorcycle and the corresponding evidence package.

## Release states

Permitted states are:

- DEVELOPMENT_ONLY
- FIRST_START_NO_GO
- FIRST_START_READY
- IDLE_COMMISSIONING_ONLY
- NO_BOOST_LIGHT_LOAD_ONLY
- SPRING_PRESSURE_ONLY
- OPEN_LOOP_BOOST_ONLY
- CLOSED_LOOP_BOOST_COMMISSIONING_ONLY
- HIGHER_LOAD_TUNING_ONLY
- FULL_POWER_DYNO_VALIDATION_ONLY
- VEHICLE_VALIDATION_ONLY
- LAUNCH_TRACK_VALIDATION_ONLY
- COMPETITION_RELEASE_CANDIDATE
- COMPETITION_RELEASED

The current state must be explicit in the release manifest. A release cannot inherit authority from a previous configuration after a controlled item changes.

## Configuration manifest

Every release must identify at minimum:

- motorcycle VIN/chassis identifier;
- engine configuration/revision;
- turbocharger and wastegate hardware;
- wastegate spring/base pressure identity;
- boost-control solenoid identity and plumbing revision;
- fuel type;
- injector part number and electrical interface mode;
- SparkPRO-2 identity and ignition configuration;
- FT550 serial/identity where available;
- FTManager calibration filename and checksum/hash;
- PMU-16 serial/identity where available;
- PMU Client project filename and checksum/hash;
- harness revision;
- connector/cavity schedule revision;
- BOM revision;
- CAN map revision;
- wheel/tyre and gearing configuration where relevant to gear/wheel-speed logic;
- launch/shift strategy revision where enabled.

## Immutable release bundle

For every promoted release, retain a read-only bundle containing:

1. FTManager calibration used.
2. PMU project used.
3. Wiring and connector schedules.
4. BOM snapshot.
5. Verification registers applicable to the release state.
6. Dyno/track logs supporting the promotion.
7. First-start/idle/light-load/boost/high-load/full-power evidence as applicable.
8. Change log from the preceding release.
9. Completed release manifest.

Any later modification creates a new release candidate rather than silently replacing an existing bundle.

## Pre-event inspection

Before dyno, track or competition use verify:

- no active critical ECU/PMU faults;
- harness, grounds and high-current connections secure;
- PMU main feed and protection hardware secure;
- SparkPRO mounting and grounds secure;
- injector interface configuration matches release manifest;
- fuel system dry and leak-free;
- fuel pressure system verified operational;
- oil and coolant levels correct;
- turbo oil/drain and intake/exhaust plumbing secure;
- wastegate/solenoid plumbing intact;
- boost fail-safe path still returns to spring pressure when de-energised;
- wheels/tyres/brakes/chassis/drivetrain meet event requirements;
- wheel-speed and gear inputs valid if used for control;
- hardwired kill and required brake/clutch interlocks operate;
- logger storage/timebase ready;
- fuel type matches calibration.

A failed critical item blocks the session.

## Post-event inspection

After every significant dyno or track session:

- inspect fuel, oil and coolant systems;
- inspect turbo/exhaust and heat shielding;
- inspect wiring near heat/vibration zones;
- inspect SparkPRO, PMU and EPM connectors for movement or heat;
- review PMU overcurrent/retry/fault history;
- review FT550 sync/CAN/fault history;
- inspect drive system, mounts and fasteners;
- compare fuel-pressure, lambda, IAT/ECT and boost behaviour to the accepted release baseline;
- note abnormal noise, smell, vibration or transient behaviour;
- record all repairs/adjustments before the next run.

## Maintenance schedule philosophy

This repository does not invent generic service intervals for race hardware. Intervals are frozen per component using manufacturer requirements, measured wear and event severity.

Track at minimum:

- engine oil/filter;
- fuel filter and pump health;
- injector inspection/flow verification as required;
- spark plugs and ignition components;
- turbocharger shaft/play/oil system inspection;
- wastegate and boost-control plumbing;
- cooling system;
- battery/charging system;
- harness/connector inspection;
- PMU high-current terminals;
- drivetrain/chain/belt/sprockets/cush/fasteners as applicable;
- brakes/tyres/wheels;
- wheel-speed sensors;
- lambda sensors;
- log-review cadence.

Intervals must be stated as event count, operating hours, distance, calendar interval or inspection-after-condition, whichever is appropriate.

## Change-control classes

### Class A: no release impact

Examples: documentation clarification, non-functional label update, evidence formatting.

Action: document change; no operational regression test required unless ambiguity exists.

### Class B: local regression required

Examples: connector service replacement with identical qualified part, non-control harness repair, replacement sensor of identical verified type.

Action: rerun the directly affected verification/test gates.

### Class C: calibration/control regression required

Examples: fuel change, injector change, ignition hardware/dwell change, boost target/control change, gearing or wheel-size change affecting logic, CAN map/filter change, PMU output policy change.

Action: reopen the relevant commissioning chain from the earliest impacted milestone.

### Class D: full release invalidation

Examples: engine hardware change, turbo/wastegate change, major fuel-system change, FT550/PMU replacement with unverified configuration, harness architecture change, launch/shift architecture change.

Action: release returns to DEVELOPMENT_ONLY or other explicitly justified earlier gate and must be re-promoted through evidence.

## Release invalidation triggers

Immediately invalidate the competition release if any of the following occurs:

- critical wiring or connector change without regression evidence;
- untracked FTManager or PMU project change;
- different fuel without approved calibration;
- injector or ignition hardware change;
- wastegate spring/solenoid/plumbing change;
- tyre/wheel/gearing change that affects control assumptions;
- recurring PMU overcurrent/retry event;
- unexplained CAN/sync dropout;
- unexplained fuel/oil pressure or lambda anomaly;
- engine/turbo mechanical damage or teardown;
- failed hardwired kill/interlock test.

## Event log

Each session should record:

- date/location/event;
- operator/rider;
- release ID;
- calibration/PMU hashes;
- fuel type;
- ambient/track conditions where useful;
- tyre/gearing configuration;
- run/pass identifiers;
- abnormal events;
- maintenance performed;
- resulting release state.

## Master release decision

The system is `COMPETITION_RELEASED` only when:

- all required preceding milestone gates are PASS;
- applicable verification registers contain no unresolved release-blocking items;
- the immutable configuration bundle exists;
- pre-event inspection is PASS;
- change-control review finds no unvalidated Class C/D modification;
- the release manifest is signed/revision-controlled.

If any requirement is not satisfied, the release state must be reduced to the highest supported validated state.
