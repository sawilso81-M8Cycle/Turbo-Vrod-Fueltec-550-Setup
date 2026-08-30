# Connector Index

## Project connector IDs

| ID | Device / location | Domain | Status |
|---|---|---|---|
| X01 | FuelTech FT550 connector A | EPM/SIM | DESIGN, cavity assignments partly verified |
| X02 | FuelTech FT550 connector B | EPM/SIM | DESIGN, cavity assignments partly verified |
| X03 | ECUMASTER PMU-16 main connector | APM/COMM | DESIGN, exact cavity map VERIFY |
| X10 | OEM CKP 32313-01A | SIM | OEM device identified |
| X11 | OEM TPS 27975-01 | SIM | OEM device identified |
| X12 | OEM MAP 32416-10 | SIM | OEM device identified |
| X13 | OEM ECT 32315-01 | SIM | OEM device identified |
| X14 | OEM IAT 27388-01 | SIM | OEM device identified |
| X15 | OEM VSS 74402-05B | SIM/POWER | OEM device identified |
| X16 | OEM oil pressure switch 26561-99 | SIM | OEM device identified |
| X17 | OEM neutral switch 33902-98A | SIM | OEM device identified |
| X20 | Front injector | EPM | OEM hardware retained, connector/terminal VERIFY |
| X21 | Rear injector | EPM | OEM hardware retained, connector/terminal VERIFY |
| X22 | Front ignition coil | EPM | OEM hardware retained, connector/driver VERIFY |
| X23 | Rear ignition coil | EPM | OEM hardware retained, connector/driver VERIFY |
| X30 | Primary fuel pump | APM | installed/OEM hardware VERIFY |
| X31 | Secondary fuel pump | APM | optional, DNP unless fitted |
| X32 | Radiator fan 1 | APM | OEM hardware retained where applicable |
| X33 | Radiator fan 2 | APM | optional, DNP unless fitted |
| X34 | Charge-cooler / auxiliary pump | APM | optional |
| X40 | Main battery positive distribution stud | POWER | DESIGN |
| X41 | Engine/battery negative star point | POWER | DESIGN |
| X42 | Sensor-reference splice pack | SIM | DESIGN |
| X43 | Sensor-ground splice pack | SIM | DESIGN |
| X50 | Service / logger auxiliary connector | APM/COMM | DESIGN |
| X51 | CAN service junction | COMM | DESIGN, termination topology VERIFY |

## Rules

1. X42 and X43 are not chassis-ground convenience points. They exist only to distribute FT550 sensor reference and sensor return.
2. X40 and X41 must be physically separated from X42/X43 except at the intended ECU/battery reference relationship.
3. CKP X10 must route directly toward X01 using a dedicated twisted/shielded branch.
4. X03 PMU high-current conductors must not share a loom bundle with CKP or low-level analogue sensor branches where practical.
5. Connector family, terminal part number, seal, backshell and cavity plugs must be added before production release.
