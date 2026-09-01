# Peak & Hold Injector Interface Freeze

## Milestone objective

Freeze the physical architecture for the optional FuelTech Peak & Hold injector driver without prematurely selecting a current class for the OEM Harley 27772-06 injectors.

## Fixed upstream/downstream architecture

- FT550 A1 Blue #1 = front injector command.
- FT550 A2 Blue #2 = rear injector command.
- X62 = FT550 injector-command service junction.
- X63 = engine-side injector-load junction.
- X64 = optional Peak & Hold input connector.
- X65 = optional Peak & Hold output connector.

The production harness shall support exactly one configuration:

### DIRECT_DRIVE_APPROVED

FT550 A1/A2 -> X62 direct service jumper -> X63 -> OEM 27772-06 injectors.

This mode is permitted only after HC-008/HC-009 prove injector impedance/current is within FuelTech FT550 direct-drive limits.

### PEAK_HOLD_INSTALLED

FT550 A1/A2 -> X62 -> X64 -> FuelTech Peak & Hold -> X65 -> X63 -> OEM 27772-06 injectors.

This mode is mandatory if measured injector impedance is below the FuelTech direct-drive threshold or measured current/loading requires current control.

## Current-class selection

FuelTech Peak & Hold hardware is available in multiple peak/hold current classes. The project shall not select 2A/0.5A, 4A/1A, 8A/2A or another supported variant until HC-008 and HC-009 are closed against the installed 27772-06 injectors.

Selection evidence must include:

- injector resistance at controlled temperature;
- supply voltage during test;
- steady/current waveform;
- opening/current behaviour where measurable;
- confirmation of one injector per channel;
- FuelTech compatibility check.

## Harness interlock

The direct jumper and Peak & Hold module path are mechanically mutually exclusive. Do not create a Y-branch that can energise both paths.

Every released harness must carry one durable configuration label:

- `DIRECT_DRIVE_APPROVED`, or
- `PEAK_HOLD_INSTALLED - <driver current class>`.

## Connector policy

X62-X65 are service-interface IDs, not assumed manufacturer connector part numbers.

Final housing, terminal, seal and cavity-plug selection must be environmentally sealed, keyed against accidental interchange, compatible with the final conductor cross-section and rated for measured injector current.

Where a FuelTech supplied Peak & Hold harness/connector kit is used, retain its manufacturer connector and splice the project harness only through an approved service junction. Do not substitute terminal systems without verifying current and environmental ratings.

## Power and ground

Peak & Hold power/ground wiring, where required by the selected FuelTech unit, shall follow that unit's manufacturer manual. Driver power current must not return through FT550 sensor ground A12/B26.

Injector +12 V remains an EPM protected feed. The Peak & Hold module controls the injector low-side/current path only as defined by the selected FuelTech hardware.

## Release gates

Before this interface becomes Rev 1 production-ready:

1. Close HC-008 and HC-009.
2. Freeze DIRECT_DRIVE_APPROVED or PEAK_HOLD_INSTALLED.
3. If Peak & Hold is required, freeze the exact FuelTech current-class/model.
4. Freeze X62-X65 connector families and terminals.
5. Freeze B36-B40 conductor sizes from measured current and route length.
6. Update Sheet 03 and the production BOM with the selected configuration.

## Status

Physical architecture: **FROZEN**.

Peak & Hold current class: **MEASUREMENT GATED**.

X62-X65 exact connector hardware: **OPEN**.
