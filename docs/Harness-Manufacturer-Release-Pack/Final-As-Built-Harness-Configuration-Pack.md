# Final As-Built Harness Configuration Pack – Rev 1

## Purpose

Define the controlled configuration record that accompanies every accepted Turbo V-Rod harness and prevents the repeat-build definition from drifting away from the validated Golden Harness.

The production master is not one drawing and it is not the physical harness alone. It is the complete controlled configuration set defined here.

## Configuration baseline

A repeat harness may only be represented as equivalent to the Golden Harness when all applicable records identify the same released configuration revision.

Required master records:

1. As-Built BOM;
2. circuit/wire schedule;
3. connector/cavity schedule;
4. splice schedule;
5. branch-dimension schedule;
6. protection/current-limit schedule;
7. connector/terminal/seal/tooling schedule;
8. heat-protection and sleeving schedule;
9. labels/identification schedule;
10. approved deviations/ECNs;
11. electrical acceptance report;
12. harness serial/build record.

## Identification convention

Recommended harness identification:

`TVR-FT550-HARNESS-R1-####`

where `####` is the unique sequential harness serial.

The physical harness label should include at minimum:

- project/product identifier;
- harness serial number;
- configuration revision;
- build date;
- manufacturer identifier;
- Golden Harness/formboard revision.

## As-built BOM requirements

Every installed production item shall have a controlled row, including:

- connector housings;
- contacts/terminals;
- seals;
- secondary locks;
- cavity plugs;
- boots/backshells;
- wire by size/specification/colour;
- sleeving;
- heat shielding;
- junction hardware;
- fuses/relays/protective devices where harness supplied;
- labels;
- splice components;
- service connectors;
- repair pigtails where approved.

Manufacturer substitutions require an approved deviation/ECN before they become as-built baseline material.

## Circuit/wire schedule

Every conductor shall identify:

- circuit ID;
- function;
- from connector/cavity;
- to connector/cavity;
- conductor cross-section;
- wire specification;
- colour/stripe or printed ID;
- approximate cut length where controlled;
- signal/power class;
- twist/shield requirement;
- branch/bundle assignment;
- applicable protection.

Locked production rules such as 4.0 mm² minimum fuel-pump feeds and dedicated returns remain explicit in this schedule.

## Connector/cavity schedule

Every populated cavity shall identify exact housing and terminal configuration. Every intentionally unused sealed cavity shall identify its cavity plug/DNP state.

No undocumented spare-cavity repurposing is permitted.

## Splice schedule

Every production splice shall identify:

- splice ID;
- circuits joined;
- method;
- conductor sizes/count;
- physical branch location or controlled datum;
- sealing/insulation method;
- inspection/test requirement.

Sensor/reference splices and high-current splices shall remain distinguishable.

## Branch-dimension schedule

Dimensions shall be captured from the validated vehicle-fit state, not from early approximate estimates.

Record:

- datum-to-breakout distance;
- breakout-to-connector length;
- service-loop allowance where controlled;
- branch orientation where relevant;
- tolerance;
- heat/movement note;
- formboard reference.

## Protection schedule

Record the final accepted value/configuration for every protected branch, including electronic PMU protection where applicable.

Measurement-gated values shall not remain `TBD` in a repeat-build release.

## Change control

After Golden Harness validation, changes are classified:

### Class 1 – documentation-only

No physical/electrical change. May be accepted through controlled document correction.

### Class 2 – dimensional/manufacturing

Changes branch length, breakout, sleeving, booting or manufacturing method without intentional circuit-function change. Requires fit/manufacturing re-verification appropriate to impact.

### Class 3 – electrical

Changes conductor size, terminal, connector family, protection, splice topology, circuit assignment, CAN/trigger wiring or grounding. Requires engineering review and applicable electrical retest.

### Class 4 – architecture

Changes FT550/PMU/SparkPRO functional architecture, pump switching strategy, injector driver strategy, Two-Step logic or other safety/engine-critical function. Requires formal engineering release and broader regression test.

## Serial traceability

Each harness build record shall identify:

- serial number;
- customer/project vehicle if assigned;
- configuration revision;
- Golden Harness/formboard revision;
- manufacturer;
- technician/build operator where available;
- build date;
- inspection/test report reference;
- deviations applied;
- final disposition.

## Repair traceability

Any later harness repair affecting a controlled circuit should be recorded against the serial number with date, location, repair method, parts used and post-repair tests.

## Release states

Before Golden Harness qualification:

`AS_BUILT_CONFIGURATION_TEMPLATE_RELEASED`

After prototype qualification and document incorporation:

`AS_BUILT_CONFIGURATION_FROZEN`

After repeat-production authorisation:

`REPEAT_BUILD_CONFIGURATION_CONTROL_ACTIVE`
