# OEM Specs Freeze — VRXSE Destroyer Injector and Ignition Hardware

## Purpose

Freeze only manufacturer-published specifications for the 2006 VRXSE Destroyer injector and ignition-coil hardware used by this FuelTech FT550 conversion.

## Injector — Harley-Davidson 27772-06

Harley-Davidson identifies the VRXSE Performance Injector Kit as kit 27791-05 and states that the kit contains two fuel injectors, part number 27772-06.

Harley-Davidson's V-Rod Destroyer Throttle Body instruction J03889 states that these high-flow Destroyer injectors:

- deliver 30% more fuel than the original equipment injectors;
- require the EFI Race Tuner injector calibration to be set to 6.37 g/s;
- are intended for high-performance / drag-race applications;
- require ECM recalibration when installed.

### OEM values frozen for this project

| Parameter | OEM value | Status |
|---|---:|---|
| Injector part number | 27772-06 | OEM VERIFIED |
| Kit part number | 27791-05 | OEM VERIFIED |
| Quantity | 2 | OEM VERIFIED |
| Fuel-flow calibration | 6.37 g/s | OEM VERIFIED |
| Relative flow increase | 30% over OE VRSC injector | OEM VERIFIED |

### Not published in the accessible OEM material

The following are not frozen because no Harley-Davidson public source located in this research published the value:

- coil/injector winding resistance;
- injector peak current;
- injector hold current;
- opening/dead-time curve;
- minimum pulse width;
- electrical driver classification;
- exact terminal family / seal part numbers.

These remain bench/evidence-gated before FT550 driver configuration and final wire sizing.

## Ignition coil — Harley-Davidson 32477-01A

Harley-Davidson's VRXSE parts information identifies two plug-top ignition coils, part number 32477-01A, used with coil boot 31651-01. The same coil assembly appears across the VRSC platform and in the VRXSE Destroyer parts catalogue.

### OEM values frozen for this project

| Parameter | OEM value | Status |
|---|---:|---|
| Ignition coil part number | 32477-01A | OEM VERIFIED |
| Quantity | 2 | OEM VERIFIED |
| Configuration | plug-top ignition coil | OEM VERIFIED |
| Coil boot | 31651-01 | OEM VERIFIED |

### Not published in the accessible OEM material

Do not freeze the following from aftermarket replacement listings:

- primary resistance;
- secondary resistance;
- saturation current;
- dwell requirement;
- internal igniter / smart-coil status;
- trigger polarity;
- FT550 ignition-driver compatibility;
- exact connector terminal family.

Aftermarket coils replacing 32477-01A are sometimes advertised as 3 ohm. This is comparison evidence only and is not treated as the OEM Harley specification.

## OEM source hierarchy

Primary Harley-Davidson sources used:

1. VRXSE Performance Injector Kit instruction J03928 — kit 27791-05 contains two injectors 27772-06.
2. V-Rod Destroyer Throttle Body instruction J03889 — 30% flow increase and 6.37 g/s Race Tuner calibration.
3. VRXSE parts catalogue / SIP — 32477-01A ignition coil, quantity two, with 31651-01 boot.
4. 2006 VRSC service literature identifies 99501-06A Service Manual and 99499-06A Electrical Diagnostic Manual as the factory-authorised detailed diagnostic references.

## Engineering consequence

The 6.37 g/s injector flow value may now be used as the OEM baseline in the FT550 configuration and injector-sizing documentation. It does not remove the requirement to determine injector electrical characteristics before the FT550 driver strategy is released.

The ignition coil identity is frozen, but coil driver configuration remains blocked until primary resistance/current-ramp and internal-driver behaviour are established by a factory diagnostic specification or direct measurement.
