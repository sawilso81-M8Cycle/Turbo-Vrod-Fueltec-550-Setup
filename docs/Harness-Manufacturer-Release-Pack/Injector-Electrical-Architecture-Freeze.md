# Injector Electrical Architecture Freeze – FT550 / V-Rod

## Purpose

Close BG-009 by freezing the harness architecture for both possible injector electrical classes while preventing an unverified injector from being connected directly to the FT550.

## Fixed ECU assignment

The production harness retains:

- Front injector command: FT550 A1 / Blue #1
- Rear injector command: FT550 A2 / Blue #2

These remain the authoritative front/rear injector control outputs.

## Physical injector baseline

The retained OEM injector baseline is Harley-Davidson 27772-06 front/rear injector hardware unless the build record explicitly changes injector model.

The electrical class of the actual injectors must be measured before first powered injection testing.

## Harness architecture

The harness shall be manufactured with a serviceable injector interface that supports either of the following final configurations without cutting the main FT550 loom.

### Path A – Direct FT550 drive

`FT550 A1/A2 -> X62 service interface -> direct-drive bypass link -> X63 injector engine branch -> injectors`

This path may only be fitted when the injector evidence is explicitly dispositioned:

`DIRECT_DRIVE_APPROVED`

### Path B – Peak & Hold interface

`FT550 A1/A2 -> X62 service interface -> Peak & Hold input -> Peak & Hold output -> X63 injector engine branch -> injectors`

This path is mandatory when the injector current/impedance class is not approved for direct FT550 control.

The selected Peak & Hold module and current class must be frozen before manufacture of the final link harness.

## Common +12 V injector feed

B39 remains a separate engine-critical switched supply branch.

Current baseline:

- 1.0 mm² provisional supply conductor;
- final conductor/protection subject to measured injector current and driver architecture;
- injector supply current must not share precision sensor supply or return paths;
- branch protection must be coordinated to conductor, connector and injector/driver current.

## Required measurements

Complete both injectors individually at known ambient temperature:

1. part number / physical identity;
2. DC coil resistance;
3. test temperature;
4. driver configuration used for dynamic test;
5. peak current;
6. hold/steady current where applicable;
7. current waveform capture;
8. voltage used for test;
9. connector/terminal temperature or abnormal heating during representative operation;
10. front/rear comparison.

A meaningful front/rear mismatch reopens injector hardware verification.

## Decision rule

The final state must be exactly one of:

- `DIRECT_DRIVE_APPROVED`
- `PEAK_HOLD_REQUIRED`

`UNKNOWN`, `ASSUMED` or an internet resistance value is not a production disposition.

If direct-drive compatibility cannot be proven from official FuelTech limits plus actual measured injector evidence, default to `PEAK_HOLD_REQUIRED` rather than risking FT550 injector drivers.

## Harness manufacturing rule

X62/X63 shall be keyed and serviceable so a direct-drive bypass or Peak & Hold interface can be changed without altering the FT550 A/B connector harness.

The manufacturer shall not permanently splice A1/A2 directly to the injectors before BG-009 closure.

## First-start interlock

Fuel and ignition commissioning remains blocked until:

- HC-008 front injector evidence complete;
- HC-009 rear injector evidence complete;
- final direct/P&H disposition recorded;
- B39 conductor/protection frozen;
- X62/X63 connector and terminal selections frozen;
- FTManager injector configuration matches installed architecture.

## Release state

Current state: `INJECTOR_ARCHITECTURE_FROZEN / ELECTRICAL_CLASS_MEASUREMENT_GATED`

BG-009 closes only when the actual injectors are measured and one final architecture is recorded in `Injector-Electrical-Decision-Register.csv`.
