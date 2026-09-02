# Final Calibration Release & Race Configuration Archive

## Purpose

Freeze the exact validated race configuration after track launch and final race validation so the motorcycle can always be returned to a known, reproducible, evidence-backed state.

This archive binds the engine calibration, power-management configuration, ignition/dwell state, launch-control logic, boost-control settings, protection limits, sensor scaling and race operating envelope into one controlled release.

## Entry conditions

Do not issue a final race configuration unless:

- `TRACK_LAUNCH_VALIDATED` is PASS;
- `FINAL_RACE_VALIDATION_ACCEPTED` is PASS;
- FT550 calibration used for the accepted race runs is saved;
- PMU16 configuration used for the accepted race runs is saved;
- SparkPRO/dwell configuration is identified;
- Two-Step launch-control configuration is identified;
- boost-control configuration is identified;
- sensor scaling/calibration state is identified;
- B15/B39/B40 and PMU output protection state is identified;
- fuel type and fuel-system baseline are recorded;
- the final accepted race logs are archived;
- no unresolved race-critical nonconformance remains.

## Release identity

Recommended naming convention:

`TVR-FT550-RACE-R##`

where `R##` is the controlled race-release revision.

Example:

`TVR-FT550-RACE-R01`

Every release shall include a human-readable manifest and machine-verifiable hashes/checksums for all archived configuration files.

## Required configuration set

### FT550

Archive:

- exact calibration/export file;
- calibration revision/name;
- firmware version;
- injector configuration;
- trigger configuration;
- ignition output mapping;
- dwell configuration/reference;
- VE/fuel tables;
- ignition tables;
- boost-control tables/limits;
- Two-Step/launch settings;
- rev limits;
- sensor calibrations;
- protection/engine-safety strategies;
- data-logging channel configuration where relevant.

### PMU16

Archive:

- exact PMU configuration/export;
- firmware version;
- output/channel assignment;
- Pump 1/2 strategy;
- B11/B12 strategy;
- B39/B40 enable/protection logic;
- X70 O11 logic;
- clutch input logic;
- timeout/fail-safe logic;
- current limits/protection values;
- CAN configuration;
- diagnostic/fault strategy.

### SparkPRO / ignition

Record:

- exact hardware PN/revision;
- supply architecture;
- validated dwell strategy;
- any hardware settings;
- coil PN;
- ignition wiring revision.

### Two-Step / launch control

Record:

- clutch input polarity/debounce;
- PMU enable conditions;
- O11 logic;
- X70 configuration;
- FT550 A21 polarity/function;
- launch RPM;
- maximum activation duration;
- launch boost ceiling;
- launch release/re-arm logic;
- fault-state behaviour.

### Boost system

Record:

- exact turbocharger PN/configuration;
- wastegate spring/base-boost configuration;
- boost-control solenoid PN/plumbing;
- boost-control strategy;
- released boost ceiling;
- released RPM ceiling;
- turbo-speed warning/limit if fitted;
- relevant temperature/pressure limits.

### Fuel system

Record:

- fuel type;
- base/reference fuel pressure;
- Pump 1/2 PN;
- injector PN;
- injector characterization source;
- final switching architecture;
- final pump protection/current limits;
- final injector protection.

### Protection

Archive the final released protection state for:

- B15;
- B39;
- B40;
- Pump 1;
- Pump 2;
- B11;
- B12;
- X50 service power if fitted;
- X70 relay coil;
- FT550 supply;
- other race-critical PMU outputs.

## Race operating envelope

Every release shall state the maximum currently approved:

- engine RPM;
- boost pressure;
- Two-Step RPM;
- Two-Step activation duration;
- launch boost;
- fuel type;
- tyre/gear/final-drive assumptions where relevant to validation;
- temperature/pressure restrictions;
- turbo-speed limit if measured;
- any track-only or dyno-only restrictions.

Do not imply a release is valid outside the environment/configuration actually tested.

## Checksum/archive requirements

For every archived binary/text configuration file, record:

- filename;
- system;
- size;
- SHA-256 hash;
- creation/export date;
- source application/version;
- operator;
- notes.

The final release folder should be immutable in practice. New tuning work creates a new working copy and later a new race-release revision rather than altering the prior release.

## Rollback set

Maintain at minimum:

1. `LAST_KNOWN_GOOD_RACE`;
2. `LAST_KNOWN_GOOD_DYNO`;
3. `FIRST_START_BASELINE`;
4. `CURRENT_DEVELOPMENT`.

The motorcycle shall be recoverable to `LAST_KNOWN_GOOD_RACE` without reconstructing settings from screenshots or memory.

## Change classification

After final race release:

### Class A – non-functional documentation

No calibration/hardware effect. Update documentation only.

### Class B – calibration refinement

Fuel/ignition/boost/launch table or limit changes with no wiring/hardware architecture change. Requires new config revision and targeted validation.

### Class C – hardware/configuration interaction

Injector, pump, coil, sensor, turbo, wastegate, fuel type, PMU output or protection changes. Requires subsystem revalidation before new race release.

### Class D – architecture

Harness, power architecture, FT550/PMU/SparkPRO topology, Two-Step chain or CAN/trigger architecture change. Requires broader regression and may invalidate Golden Harness/race release status.

## Final release signoff

A race release is promoted only when the manifest confirms:

- exact files present;
- hashes recorded;
- accepted race logs linked;
- released operating envelope documented;
- rollback set complete;
- hardware state documented;
- protection state documented;
- no blocking nonconformance open;
- engineering/tuner signoff complete.

Final state:

`FINAL_RACE_CONFIGURATION_ARCHIVED`

When the release is also installed/verified on the motorcycle:

`FINAL_RACE_CONFIGURATION_ACTIVE`

## Next milestone

Proceed to the Project Final Validation / Golden Harness & Repeat-Build Release milestone, which will close the complete development lifecycle and identify any remaining production-versus-race-configuration differences.
