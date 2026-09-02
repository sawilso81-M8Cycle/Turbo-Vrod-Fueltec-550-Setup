# Project Completion & Handover Pack

## Purpose

Define the controlled handover of the Turbo V-Rod FT550 / PMU16 project after Golden Harness validation, repeat-build release and final race configuration archival.

The handover pack is the operational front door to the completed engineering package. It tells the tuner, harness manufacturer, race crew and future maintainer which documents control the vehicle, what may be changed, what must be inspected and how to recover a known-good configuration.

## Completion entry conditions

Project completion may be declared only when applicable evidence supports:

- `FINAL_RACE_VALIDATION_ACCEPTED`;
- `FINAL_RACE_CONFIGURATION_ARCHIVED`;
- `GOLDEN_HARNESS_VALIDATED`;
- `AS_BUILT_CONFIGURATION_FROZEN`;
- `REPEAT_BUILD_RELEASED`;
- no unresolved safety-critical electrical nonconformance;
- final controlled documents are identifiable by revision;
- known operational limitations are documented.

## Handover roles

### Tuner pack

Provide the tuner with controlled copies/references for:

- final FT550 race calibration and SHA-256 identity;
- last-known-good dyno calibration;
- PMU16 configuration relevant to engine operation;
- SparkPRO/dwell configuration;
- injector characterization and fuel-pressure reference condition;
- boost-control/wastegate configuration;
- Two-Step/launch envelope;
- sensor scaling/correlation records;
- dyno and track validation evidence;
- abort/protection limits;
- current operating envelope.

The tuner shall not change harness protection, PMU channel assignment or safety interlocks without engineering change control.

### Harness manufacturer pack

Provide the manufacturer with the released manufacturing set only, including:

- Production Wire / Circuit Master Schedule;
- Connector / Cavity Master Schedule;
- Splice / Junction Master Schedule;
- Protection / Fuse / PMU Current-Limit Master Schedule where applicable to supplied hardware;
- dimensional/formboard schedule;
- label/identification schedule;
- build traveller;
- HP-6 and HP-7 acceptance requirements;
- released BOM and approved substitutions;
- Golden Harness / repeat-build release record;
- approved deviations incorporated into the repeat-build baseline.

Do not provide a race-crew field repair as an undocumented manufacturing revision.

### Race crew pack

Provide a concise operational set containing:

- current race release ID;
- fuel requirement;
- maximum released RPM/boost;
- Two-Step RPM/duration/launch-boost envelope;
- normal pre-run checks;
- critical pressures/temperatures/abort limits from the verified race configuration;
- emergency shutdown method;
- fuse/relay/service-spares map;
- X50/X51 service access information;
- post-run inspection checklist;
- fault/recovery quick guide;
- explicit prohibited changes.

### Maintenance / electrical service pack

Provide:

- final wiring/cavity/splice schedules;
- connector/terminal/seal identification;
- service test points;
- ground architecture;
- CAN topology;
- X70 Two-Step architecture;
- protection schedule;
- field-repair rules;
- inspection intervals/triggers;
- approved spare components;
- configuration recovery procedure.

## Operational limitations

The final handover shall explicitly record limitations that remain applicable, including as relevant:

- approved fuel only;
- approved boost ceiling;
- approved RPM ceiling;
- approved launch RPM and activation duration;
- turbo-speed limit if validated and used;
- injector-duty limit;
- pressure/temperature abort thresholds;
- ambient/track restrictions where applicable;
- calibration-specific hardware assumptions;
- no unapproved sensor substitution;
- no unapproved pump substitution;
- no harness/protection modification outside change control.

A missing limitation is not permission to exceed the validated envelope.

## Pre-event / pre-run inspection

At minimum inspect:

- battery/main power security;
- J-P01/J-P02/B15 condition;
- PMU/FT550/SparkPRO connectors;
- Pump 1/2 high-current connections;
- B39/B40 paths;
- X70 relay/socket and clutch-switch wiring;
- CAN/service connectors capped and secured;
- harness near turbo/exhaust;
- fuel/oil/coolant leaks;
- sensor plausibility at key-on;
- fuel pressure prime;
- current configuration/release identity.

## Post-run inspection

Inspect/log as appropriate:

- PMU faults/trips;
- ECU trigger/sync errors;
- pressure/temperature anomalies;
- pump-current anomalies;
- B15/J-P01/J-P02 heat evidence;
- Pump 1/2 connector heat;
- B39/B40 heat;
- X70 condition;
- harness thermal exposure near turbo/exhaust;
- chafing or movement;
- fuel/oil/coolant leaks;
- calibration/configuration changes made during the event.

## Periodic inspection philosophy

Inspection frequency shall be based on service severity and accumulated evidence rather than an invented universal mileage interval.

Mandatory inspection triggers include:

- after initial repeat-build installation;
- after any electrical protection trip with unexplained cause;
- after a fuel-pump or fan overcurrent event;
- after turbo/exhaust heat damage or abnormal heat exposure;
- after crash/impact or major mechanical work affecting harness routing;
- after connector water/chemical contamination;
- after harness repair;
- after repeated high-current connector temperature rise;
- before returning to race use after extended storage;
- after any configuration change affecting protection or output mapping.

## Spare parts strategy

The handover shall maintain a controlled spare list for critical service items, including as applicable:

- released fuses/protection devices;
- X70 relay and approved socket/terminals;
- connector housings;
- terminals and wire seals;
- cavity plugs;
- approved wire sizes/types;
- heat-shrink/sealing materials;
- CAN/service connector caps;
- pump/fan connector repair components;
- clutch-switch repair components.

A spare part is not approved merely because it physically fits.

## Field repair rules

Field repair is intended to restore the released electrical function safely, not redesign it at the track.

Rules:

1. identify the affected circuit from the controlled schedules;
2. isolate power before repair;
3. use the released conductor size/type or an approved engineering substitution;
4. use the released terminal/seal family where the connector is retained;
5. preserve CAN twist/polarity and trigger shielding/twist requirements;
6. preserve sensor-ground segregation;
7. preserve B39/B40 separation;
8. preserve X70/A21 dry-contact isolation;
9. do not bypass protection to keep the bike running;
10. document every repair against the harness serial;
11. perform applicable continuity/isolation/function tests before return to service;
12. promote any permanent field solution through engineering change control before it becomes the repeat-build method.

## Configuration recovery

Maintain recoverable copies of:

- `LAST_KNOWN_GOOD_RACE`;
- `LAST_KNOWN_GOOD_DYNO`;
- `FIRST_START_BASELINE`;
- `CURRENT_DEVELOPMENT`.

Before restoring a configuration, confirm the physical hardware still matches the assumptions of that configuration.

Never load an older calibration blindly after injectors, sensors, pumps, wastegate hardware, ignition hardware or wiring architecture have changed.

## Change control after completion

After project completion, modifications are classified as:

- **Class A – documentation-only:** no physical/configuration behaviour change;
- **Class B – service-equivalent:** approved like-for-like replacement with evidence;
- **Class C – configuration change:** calibration/PMU/boost/launch/protection change requiring validation proportional to risk;
- **Class D – hardware architecture change:** wiring, connector, sensor, pump, ignition, fuel, turbo or protection change requiring engineering review and regression testing.

A Class C or D change may suspend `FINAL_RACE_CONFIGURATION_ACTIVE` or `REPEAT_BUILD_RELEASED` until the affected validation gates are repeated.

## Final project state

When the release index, limitations, maintenance strategy, spares, field-repair rules and stakeholder packs are complete:

`PROJECT_HANDOVER_COMPLETE`

The project then enters controlled operational support:

`IN_SERVICE_CONFIGURATION_CONTROL_ACTIVE`

These states do not mean development can never continue. They mean future development starts from a known, traceable, recoverable baseline rather than from tribal knowledge.
