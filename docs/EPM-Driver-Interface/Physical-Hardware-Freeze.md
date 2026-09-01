# EPM Physical Hardware Freeze

## Status

Milestone baseline for the Turbo V-Rod Destroyer FT550 engine-power interface.

## Ignition driver

The project ignition architecture remains:

FT550 A8 Gray #1 -> external igniter CH1 -> front OEM 32477-01A coil
FT550 A9 Gray #2 -> external igniter CH2 -> rear OEM 32477-01A coil

FuelTech documents SparkPRO as the supported ignition-driver family for passive/dumb coils. The exact SparkPRO variant, connector kit, dwell and thermal mounting remain release-gated until OEM coil primary resistance/current-ramp evidence is closed.

### Physical mounting requirements

- Mount the igniter to a rigid metallic heat-spreading surface.
- Keep it away from turbo/exhaust radiant heat and direct water/debris exposure.
- Provide service access to both ECU-command and coil-output connectors.
- Keep A8/A9 command wiring separate from CKP wiring.
- Keep driven coil-primary wiring short and segregated from precision analogue wiring.
- Ground/power topology must follow the selected FuelTech igniter manual, not the sensor-ground network.

## Injector interface

FT550 A1/A2 are frozen as the two primary injector outputs.

The production loom shall include a serviceable injector interface junction with two mutually exclusive configurations:

1. DIRECT_DRIVE_APPROVED
2. PEAK_HOLD_INSTALLED

FuelTech states that the blue injector outputs can directly operate saturated injectors within their permitted impedance/load limits, while low-impedance injectors below 7 ohms require a Peak & Hold driver. FuelTech Peak & Hold hardware is available in 2A/0.5A, 4A/1A and 8A/2A versions. The selected current class must match measured/verified 27772-06 electrical characteristics.

### Injector interface junction

Use project connector IDs:

- X62 FT550 injector-output side
- X63 injector-load side
- X64 optional Peak & Hold input
- X65 optional Peak & Hold output

The direct jumper and Peak & Hold paths are mechanically/configurationally mutually exclusive. The released harness must carry a durable configuration label stating DIRECT_DRIVE_APPROVED or PEAK_HOLD_INSTALLED.

## Current release blockers

- OEM 32477-01A coil primary resistance/current ramp/dwell.
- Exact FuelTech ignition-driver model and connector kit.
- OEM 27772-06 injector resistance/current class.
- Peak & Hold current class if required.
- Final mounting location and branch lengths.
- Exact terminals/seals for X60-X65.

## Release rule

No injector or ignition output may be energised until its interface hardware is frozen against the relevant measured/OEM electrical evidence.