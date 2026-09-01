# Injector and Ignition Driver Interface Decision

## Purpose

Freeze the safest FT550 interface architecture for the OEM Harley VRXSE/V-Rod injector and ignition hardware while preserving the OEM engine hardware baseline.

## OEM ignition coil classification

The OEM ignition coil is Harley-Davidson 32477-01A.

Available product imagery for genuine/used 32477-01A coils clearly shows a **two-terminal electrical connector**. A conventional smart coil with an integrated igniter normally requires separate power, ground and logic-trigger connections. A two-terminal primary connection therefore indicates a passive/dumb coil architecture in which primary current switching must occur externally to the coil.

### Project decision

**32477-01A is treated as a passive/dumb two-terminal coil for the FT550 installation.**

The FT550 gray ignition outputs must therefore **not** drive the coil primary directly.

Frozen command architecture:

- FT550 A8 / Gray #1 -> external ignition driver channel 1 input -> front 32477-01A coil
- FT550 A9 / Gray #2 -> external ignition driver channel 2 input -> rear 32477-01A coil

FuelTech explicitly states that dumb/passive coils require an external igniter such as SparkPRO and that FT gray ignition outputs cannot directly drive dumb coils.

### External igniter baseline

Use a two-channel FuelTech-compatible inductive ignition driver, with **SparkPRO-2 or an equivalently verified FuelTech-supported driver** as the project baseline.

Exact driver part number, mounting, connector, conductor size and thermal environment remain to be frozen in the BOM milestone.

### Still measurement-gated

The passive-coil classification closes the smart-vs-dumb topology question but does not establish:

- primary resistance;
- saturation current;
- dwell requirement;
- maximum safe current;
- thermal limit.

These remain bench/OEM-spec gates before final dwell calibration.

## OEM injector classification

OEM Destroyer high-flow injectors are Harley 27772-06, supplied in kit 27791-05. Harley specifies 6.37 g/s calibration flow and approximately 30 percent greater flow than standard VRSC injectors.

No authoritative public Harley source has yet established injector electrical resistance/impedance.

FuelTech blue outputs A1/A2 can directly control injectors where impedance and aggregate current are within FuelTech limits. FuelTech requires Peak & Hold when injector impedance is below 7 ohms or where the configured injector load exceeds the permitted direct-drive limits.

### Project decision

Keep both wiring possibilities available until resistance is measured:

- Direct path: FT550 A1/A2 blue outputs -> injectors, only if measured impedance/current is within FuelTech direct-drive limits.
- Peak & Hold path: FT550 A1/A2 -> FuelTech Peak & Hold driver -> injectors, mandatory if impedance is below 7 ohms or otherwise required by FuelTech limits.

Do not energise the injectors until HC-008/HC-009 are closed.

## Wiring-release consequence

The ignition architecture is now sufficiently defined to add an external ignition-driver connector and branch to the production harness.

The injector harness retains a configurable interface point so a Peak & Hold module can be fitted without rebuilding the engine-side loom.

## Evidence hierarchy

1. FuelTech FT450/FT550/FT600 manual for ECU output limits and dumb-coil driver requirements.
2. Harley OEM part identity for 32477-01A and 27772-06.
3. Physical connector evidence for 32477-01A two-terminal construction.
4. Bench measurements for resistance/current/dwell values not published by Harley.
