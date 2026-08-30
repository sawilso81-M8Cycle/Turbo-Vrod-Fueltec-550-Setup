# Turbo V-Rod FuelTech FT550 Setup

Engineering repository for integrating a FuelTech FT550 ECU and ECUMASTER PMU-16 into a Harley-Davidson VRXSE V-Rod Destroyer / Revolution-engine turbo application.

## Design intent

The project combines the verified Harley-Davidson factory information and manufacturer references already stored in this repository to produce a new, serviceable motorsport harness.

The current architecture is:

1. **EPM — Engine Power Module**: FT550, injectors, ignition and engine-critical actuator power/control.
2. **APM — ECUMASTER PMU-16**: electronically protected fuel-pump, cooling and auxiliary high-current distribution.
3. **SIM — Sensor Interface**: original OEM Harley sensors, precision sensor supplies/returns, CKP wiring and low-level signals.

All three domains share the required vehicle reference but high-current load paths remain separated from precision measurement paths.

## Complete wiring package

- **[HD-Style Turbo V-Rod Complete Wiring Package](docs/HD-Style-Wiring/README.md)**
- [Sheet 01 - Master Power and Grounds](docs/HD-Style-Wiring/Sheet-01-Master-Power-and-Grounds.md)
- [Sheet 02 - OEM Sensors to FT550](docs/HD-Style-Wiring/Sheet-02-OEM-Sensors-to-FT550.md)
- [Sheet 03 - Injection and Ignition](docs/HD-Style-Wiring/Sheet-03-Injection-and-Ignition.md)
- [Sheet 04 - PMU16 Power Distribution](docs/HD-Style-Wiring/Sheet-04-PMU16-Power-Distribution.md)
- [Sheet 05 - Start, Kill, Cooling and Auxiliaries](docs/HD-Style-Wiring/Sheet-05-Start-Kill-Cooling-Aux.md)
- [Master Wire and Connector Schedule](docs/HD-Style-Wiring/Master-Wire-and-Connector-Schedule.csv)

## Production harness milestone

- **[Production Harness Milestone](docs/Production-Harness-Milestone/README.md)**
- [Connector Index](docs/Production-Harness-Milestone/Connector-Index.md)
- [Connector Cavity Schedule](docs/Production-Harness-Milestone/Connector-Cavity-Schedule.csv)
- [Splice and Ground Reference](docs/Production-Harness-Milestone/Splice-Ground-Reference.md)
- [Harness Branch Schedule](docs/Production-Harness-Milestone/Harness-Branch-Schedule.csv)
- [Verification Register](docs/Production-Harness-Milestone/Verification-Register.csv)
- [Rev 1 Release Checklist](docs/Production-Harness-Milestone/Release-Checklist.md)

## Supporting documentation

- [FuelTech Official Manuals](docs/FuelTech-Official-Manuals/README.md)
- [ECUMASTER PMU-16 References](docs/ECUMASTER-PMU16/README.md)
- [Harley VRXSE Official References](docs/Harley-VRXSE-Official-References/README.md)
- [VRXSE to FT550 Sensor Matrix](docs/VRXSE-FT550/VRXSE-to-FT550-Sensor-Matrix.md)
- [Electrical Architecture and Grounding](docs/VRXSE-FT550/Electrical-Architecture-and-Grounding.md)
- [Trigger and MAP Strategy](docs/VRXSE-FT550/Trigger-and-MAP-Strategy.md)
- [Development Roadmap](ROADMAP.md)

## OEM sensor baseline

The wiring package retains the original VRXSE/common-VRSC sensor hardware identified in the repository: CKP 32313-01A, TPS 27975-01, MAP 32416-10, ECT 32315-01, IAT 27388-01, VSS 74402-05B, oil-pressure switch 26561-99 and neutral switch 33902-98A.

## Verification rule

No circuit is production-ready merely because it appears in this repository. Every unresolved pin, wire colour, sensor calibration, output current, driver type and supply requirement remains explicitly marked **VERIFY** until confirmed against the exact physical hardware and manufacturer documentation. No `VERIFY` item may remain in the released production harness.
