# Sheet 04 - ECUMASTER PMU-16 Power Distribution

## Role

The PMU-16 is the high-current auxiliary power-distribution backbone. It replaces conventional relay/fuse branches for non-precision loads while adding current measurement and programmable protection.

## Functional allocation freeze

The following O1-O16 functional assignments are frozen at project-design level. Exact connector cavities remain `VERIFY` until the official PMU-16 pinout table is present in repository-readable form.

| PMU output | Frozen function | Control concept | Failure action | Status |
|---|---|---|---|---|
| O1 | Primary fuel pump | FT550 request or PMU engine-running logic | engine protection / fuel-loss response | DESIGN FROZEN; current limit VERIFY |
| O2 | Secondary/staged fuel pump | staged by boost/RPM/load request | boost/load reduction or shutdown | DESIGN FROZEN; DNP if not fitted |
| O3 | Radiator fan 1 | ECT threshold / override | warning + temperature protection | DESIGN FROZEN |
| O4 | Radiator fan 2 | ECT threshold / staged | warning + temperature protection | DESIGN FROZEN; DNP if not fitted |
| O5 | Charge/intercooler pump | ignition/engine run | warning / boost restriction | DESIGN FROZEN; DNP if not fitted |
| O6 | Boost-control solenoid +12 V | engine-control enable; control topology VERIFY | default to mechanical/base boost | DESIGN FROZEN |
| O7 | Auxiliary coolant / race pump | application-specific | application-specific | RESERVED |
| O8 | Warning/fault lamp | PMU/FT550 fault logic | driver indication | DESIGN FROZEN |
| O9 | Race accessory feed | switched | isolate on fault | RESERVED |
| O10 | Logger/display/service feed | ignition switched | non-engine-critical | DESIGN FROZEN |
| O11 | Spare high-side output 1 | none | off | RESERVED |
| O12 | Spare high-side output 2 | none | off | RESERVED |
| O13 | Spare high-side output 3 | none | off | RESERVED |
| O14 | Spare high-side output 4 | none | off | RESERVED |
| O15 | Spare high-side output 5 | none | off | RESERVED |
| O16 | Spare high-side output 6 | none | off | RESERVED |

## PMU input allocation philosophy

PMU A1-A16 are reserved for power-system commands and status, not for replacing the FT550 precision sensor network.

Working project allocation intent:

- A1 - master enable / ignition request
- A2 - start request
- A3 - kill request / emergency torque-disable request
- A4 - fan manual override
- A5 - service/test mode
- A6-A16 - reserved for future power-system logic or verified discrete status

These input-function assignments are project-defined and may be frozen only after exact cavity mapping is extracted from the official PMU-16 pinout.

## CAN architecture

- PMU CAN1 is the preferred FT550/vehicle control-and-status bus once exact physical pins and message compatibility are verified.
- PMU CAN2 is reserved for expansion/logger/service use unless a later architecture decision changes this.
- No CAN identifiers or payloads are defined until supported by verified manufacturer documentation.

Critical behaviour must remain safe without CAN:

- boost control defaults to base/mechanical boost;
- fuel-pump state is explicitly defined on CAN loss;
- cooling behaviour fails safe;
- kill/master isolation remains hardwired.

## Protection setup

For every populated output, measure actual steady current and inrush. Then configure current limits, trip thresholds, retry timing and retry count from the ECUMASTER manual and measured load evidence. Generic current guesses are not permitted in the released configuration.

## Remaining pin-level blocker

The repository currently records the official PMU-16 pinout document reference but does not contain its pin table in readable text form. Therefore the following remain `VERIFY`:

1. exact connector cavity for O1-O16;
2. exact connector cavity for A1-A16;
3. exact CAN1 H/L cavities;
4. exact CAN2 H/L cavities;
5. switched +12 V input cavity;
6. PMU ground cavity/cavities;
7. +5 V output cavity;
8. terminal family / wire-size limits.

No connector cavity is to be guessed from memory or generic PMU examples.