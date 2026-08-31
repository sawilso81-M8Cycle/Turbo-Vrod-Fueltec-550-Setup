# FT550 Verified Cavity Map — Turbo V-Rod Protection Baseline

This file records the FT550 connector cavities verified from FuelTech manufacturer documentation and the project allocation built around them.

## Connector A

| Cavity | Manufacturer function / wire | Turbo V-Rod use |
|---|---|---|
| A12 | Signal ground | Precision signal-ground/reference option |
| A13 | +12 V input from relay | FT550 switched ECU supply |
| A14 | 5 V sensor output | Sensor-reference splice SP-S01 |
| A15 | CAN A LOW | FT550 CAN A bus |
| A16 | CAN A HIGH | FT550 CAN A bus |
| A17 | Cam sync | DNP unless engineered cam sync is later added |
| A18 | RPM reference input | OEM CKP reference |
| A19 | RPM signal input | OEM CKP signal |
| A20 | White input #1 generic | Reserved by project for OEM MAP signal, configuration/calibration VERIFY |
| A21 | White input #2 / 2-step | Reserved for launch/clutch strategy unless reassigned |
| A22 | White input #3 | OEM TPS |
| A23 | White input #4 / oil pressure | Added true engine oil-pressure transducer |
| A24 | White input #5 / H2O temperature | OEM ECT |
| A25 | White input #6 / fuel pressure | Added fuel-pressure transducer |
| A26 | White input #7 | OEM VSS in PROBIKE project configuration |

## Connector B

| Cavity | Manufacturer function / wire | Turbo V-Rod use |
|---|---|---|
| B1 | Power ground | FT550 power ground |
| B2 | Power ground | FT550 power ground |
| B3 | CAN B LOW | Reserved CAN B |
| B4 | CAN B HIGH | Reserved CAN B |
| B5 | White input #8 / IAT | OEM IAT |
| B6 | White input #9 / Pan Vac or back pressure | Candidate crankcase-pressure channel if direct FT550 monitoring is selected |
| B7 | White input #10 / wastegate or nitrous pressure | Candidate wastegate/dome pressure channel |
| B12 | White input #11 free | Reserved post-intercooler IAT; exact sensor/configuration VERIFY |
| B13 | White input #12 free | Held as spare protection input |
| B18 | White input #13 / gear position | Gear-position channel if fitted |
| B19 | White input #14 / rear shock | Available development input if not otherwise required |
| B26 | Sensor ground | Precision sensor-ground distribution option |

## Allocation policy

The project deliberately keeps A23 and A25 for true engine oil and fuel pressure because these channels directly support engine protection. B12 is reserved for post-intercooler IAT before development-only sensors consume spare inputs.

Dual lambda should use a verified CAN/digital FuelTech-compatible path where possible. EGT, IMU and most development sensors should use CAN expansion/logger capacity rather than displace protection inputs.

## Remaining caveats

A manufacturer-verified physical cavity does not by itself prove that every sensor type can be configured on that input. Before Rev 1 release, verify FTManager configuration capability, selected sensor transfer functions and wiring requirements for A20/B12 and any conditional Tier-2 channels.
