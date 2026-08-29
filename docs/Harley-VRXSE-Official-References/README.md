# Harley-Davidson VRXSE Official Reference Set

This folder records the Harley-Davidson source material used to develop the VRXSE Destroyer to FuelTech FT550 wiring conversion.

## Key discovery

The 2006 VRXSE V-Rod Destroyer uses a race-specific main harness and ECM, but the engine sensor harness is listed as **70155-03**. That same engine harness is also used on production 2006 VRSCA, VRSCD and VRSCR models.

This creates a useful factory cross-reference path:

**VRXSE Destroyer engine sensors -> 70155-03 engine harness -> 2006 VRSCA/VRSCD wiring diagrams -> FuelTech FT550**

## Factory publication set

| Publication | Description | Use in this project |
|---|---|---|
| **99450-06** | 2006 VRXSE Model Service/Owner's Manual | Destroyer-specific service and race-bike reference |
| **99452-06A** | 2006 VRXSE Parts Catalog | Destroyer-specific part numbers, sensors, harnesses and components |
| **99499-06A** | 2006 VRSC Electrical Diagnostic Manual | Electrical diagnostics, connector identification and circuit verification |
| **99501-06A** | 2006 VRSC Service Manual | Production VRSC system and engine-service reference |
| **99949-06** | 2006 Wiring Diagrams | Primary circuit cross-reference for the common engine sensor harness |

## Important 99949-06 wiring sheets

The most useful production VRSC drawings identified for this conversion are:

- **Page 79**: VRSCA/VRSCD main harness circuits including CKP, TPS, IAT and neutral-related wiring.
- **Page 80**: VSS, MAP, ECT, oil-pressure and associated circuits.
- **Page 81C**: ignition/engine-management circuit showing CKP, TPS, MAP, ECT and IAT relationships to the ECM.

The production diagrams show TPS, MAP, ECT and IAT using a dedicated **BK/W sensor-ground/reference return**, rather than relying on a random chassis return. This is important to the SIM design.

## VRXSE component findings

The working parts-catalog cross-reference identifies the following Destroyer components:

| Function | Harley part number | Working status |
|---|---:|---|
| Crank position sensor | **32313-01A** | Identified from VRXSE parts information |
| Throttle position sensor kit | **27975-01** | Identified from VRXSE parts information |
| MAP sensor | **32416-10** | Identified from VRXSE parts information |
| Engine coolant temperature sensor | **32315-01** | Identified from VRXSE parts information |
| Intake air temperature sensor | **27388-01** | Identified from VRXSE parts information |
| Vehicle speed sensor | **74402-05B** | Identified from VRXSE parts information |
| Oil pressure switch | **26561-99** | Identified from VRXSE parts information |
| Neutral switch | **33902-98A** | Identified from VRXSE parts information |
| Engine sensor harness | **70155-03** | Critical cross-model harness finding |
| VRXSE main harness | **70126-06** | Destroyer race-specific main harness |
| VRXSE race ECM | **33225-06** | Destroyer race-specific ECM |

## Cam-position finding

No OEM cam-position sensor has yet been identified in the VRXSE parts reference or the reviewed 2006 engine-control diagrams. Until independently disproved, the conversion should treat the Destroyer as a **crank-only OEM engine-position system**.

This means FT550 cam-sync input must remain unused unless a proper engineered cam-sync solution is added.

## Official Harley-Davidson online references

- Harley-Davidson Service Information Portal: https://serviceinfo.harley-davidson.com/
- 2006 VRXSE parts-information source used during research: https://serviceinfo.harley-davidson.com/sip/service/document/1686747604714851644
- 2006 wiring-diagram document used during research: https://serviceinfo.harley-davidson.com/sip/content/document/view?groupId=9&id=5533

## Provenance rule

Harley-Davidson SIP and the exact factory publication for the applicable model/year outrank forum posts, aftermarket diagrams and recollection. If a conflict exists, record the conflict and preserve the source rather than silently choosing a convenient answer.
