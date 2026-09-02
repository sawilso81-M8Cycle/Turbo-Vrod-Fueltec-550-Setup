# Physical Bike Measurement & Hardware Identification Milestone

## Milestone objective

Convert the open P0/P1 physical-build inputs into a controlled evidence package that can be completed directly against the motorcycle and installed/selected hardware.

This milestone does **not** mark any physical item verified before evidence is captured. Its purpose is to make the physical closure session deterministic, traceable and production-release compatible.

## Entry condition

The Physical Build Readiness Punchlist is controlling. PBR-001 through PBR-018 remain open until actual evidence is entered.

## Exit condition

The milestone exits at `PHYSICAL_BUILD_INPUTS_VERIFIED` only when all applicable P0 physical identity/dimensional items are accepted and no production-critical connector, hardware identity or harness dimension remains assumed.

## Locked rules

1. No assumed Harley connector identity.
2. Connector cavity orientation is controlled from the mating face.
3. Rear wire-entry photographs are supporting evidence only.
4. Approximate harness dimensions cannot be promoted to production dimensions without actual-bike measurement.
5. Pump feeds and returns remain minimum 4.0 mm² at this stage.
6. Pump switching/protection remains provisional until exact pump hardware and measured electrical load are verified.
7. Injector and ignition configuration must use verified hardware/source data rather than guessed characteristics.
8. Separate engine-critical, auxiliary high-current and precision sensor current paths/grounds must be preserved through physical routing.
9. The X70 isolated relay architecture remains the current Two-Step baseline. Earlier PCB concepts remain superseded unless deliberately restored by controlled design change.

## Work package A: component location freeze

Capture the physical location, orientation and connector-exit direction for:

- FT550;
- PMU16;
- SparkPRO;
- X70 Two-Step relay;
- Pump 1;
- Pump 2;
- injectors;
- ignition coils;
- boost solenoid;
- wastegate-related electrical devices;
- wideband controller;
- added pressure sensors;
- X50 engineering connector;
- X51 CAN/service connector;
- major positive distribution points;
- engine/chassis/battery ground points.

Each location requires a photo ID and a location record before `COMPONENT_LOCATIONS_FROZEN` can be issued.

## Work package B: B01-B44 dimensional freeze

Measure each branch on the actual motorcycle using its installed/proposed route.

For each branch record:

- Branch ID;
- start datum;
- end datum;
- measured routed length;
- service-loop allowance;
- movement allowance;
- heat-zone allowance/protection;
- final proposed production length;
- evidence photo IDs;
- PASS/HOLD.

Steering, suspension and engine movement must be considered where relevant. Straight-line measurements are not acceptable where the production harness follows a routed path.

## Work package C: connector identification

For every connector that is not already backed by verified source/physical evidence, capture:

- Device/connector ID;
- manufacturer marking;
- moulded housing number;
- cavity count;
- keying/polarisation;
- mating-face photo;
- rear wire-entry photo;
- cavity numbering evidence;
- terminal family;
- seal family;
- compatible conductor range;
- proposed manufacturer PN;
- verification state.

Status remains `HOLD` if the terminal family or cavity orientation is uncertain.

## Work package D: exact electrical hardware identification

The following devices must have exact manufacturer/PN/revision captured where applicable:

- Pump 1;
- Pump 2;
- injectors;
- ignition coils;
- SparkPRO;
- boost-control solenoid;
- wideband controller and sensor;
- pressure sensors;
- clutch switch/sensor;
- X70 relay/socket.

This milestone captures identity. Powered electrical characterization remains controlled by the subsequent Electrical Load Verification milestone.

## Work package E: physical power/ground topology

Capture the actual proposed/installed:

- battery positive take-off;
- primary protection location;
- PMU feed;
- FT550 feed;
- SparkPRO feed;
- pump power route;
- battery negative;
- engine ground;
- chassis ground where used;
- FT550 grounds;
- PMU grounds;
- SparkPRO ground;
- pump returns;
- sensor reference/sensor ground boundaries.

Record stud/fastener size by physical measurement or verified source only.

## Work package F: CAN topology

Capture:

- node location;
- trunk route;
- service connector location;
- termination location(s);
- approximate trunk length;
- stub lengths;
- shield/twist treatment where applicable;
- connector evidence.

Final electrical CAN verification remains a commissioning activity.

## Acceptance gates

### Gate PBM-1: locations
All production-critical component locations frozen.

### Gate PBM-2: dimensions
B01-B44 have actual-bike measurements and accepted production allowances.

### Gate PBM-3: connectors
No production-critical connector identity, cavity orientation, terminal or seal remains assumed.

### Gate PBM-4: hardware identity
Pump/injector/coil/SparkPRO/X70 and other critical hardware identities captured.

### Gate PBM-5: topology
Physical power, ground and CAN topology captured without violating the intended electrical-domain segregation.

### Gate PBM-6: evidence review
Evidence register reviewed and all P0 physical-input HOLD items closed or explicitly escalated.

## Output state

When PBM-1 through PBM-6 pass:

`PHYSICAL_BUILD_INPUTS_VERIFIED`

The next milestone is then:

`ELECTRICAL_LOAD_VERIFICATION_AND_PROTECTION_FREEZE`

That milestone will measure the actual high-current loads and use those results to freeze pump switching and B15/B39/B40/pump/fan protection before manufacturer release.
