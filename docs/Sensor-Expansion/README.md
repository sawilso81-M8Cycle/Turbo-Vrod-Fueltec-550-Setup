# Sensor Expansion and Engine Protection

This package extends the Turbo V-Rod Destroyer wiring design beyond the OEM sensor baseline without replacing the original Harley sensor set.

## Objective

Add the minimum additional instrumentation required to make a serious turbo VRXSE installation observable, protectable and tunable.

The OEM sensor baseline remains:

- CKP 32313-01A
- TPS 27975-01
- MAP 32416-10
- ECT 32315-01
- IAT 27388-01
- VSS 74402-05B
- Oil-pressure switch 26561-99
- Neutral switch 33902-98A

Additional sensors are grouped by purpose rather than simply by available FT550 inputs.

## Priority groups

### Group A - Mandatory engine-protection instrumentation

1. Wideband lambda / O2, preferably one per cylinder.
2. Fuel-pressure transducer.
3. Engine oil-pressure transducer.
4. FT550 internal 7-bar MAP used as turbo load/boost reference while retaining OEM MAP as an independent reference channel where practical.
5. Post-compressor / post-intercooler IAT positioned to represent actual charge temperature entering the engine.

### Group B - Strongly recommended turbo-health instrumentation

1. Front-cylinder EGT.
2. Rear-cylinder EGT.
3. Turbo oil-pressure sensor where the turbo feed merits independent monitoring.
4. Crankcase-pressure sensor.
5. Intercooler water temperature if water-to-air charge cooling is used.
6. Exhaust manifold pressure / EMAP for turbine and exhaust-system development.
7. Wastegate/dome pressure where dome-controlled boost is used.
8. Turbo shaft-speed sensor for overspeed protection and compressor-map validation.

### Group C - Drag-development instrumentation

1. Front wheel-speed sensor.
2. Gear-position input.
3. IMU / longitudinal acceleration and pitch.
4. Brake-pressure input.
5. Optional suspension-travel / ride-height channels.
6. Optional compressor-outlet pressure for intercooler/throttle pressure-drop analysis.

## Core engineering value

The expansion is intended to convert the system from command-only engine management to outcome-aware engine management.

Examples:

- Fuel pressure + MAP -> injector differential-pressure monitoring.
- Lambda front + rear -> cylinder mixture comparison.
- EGT front + rear -> cylinder thermal comparison.
- Oil pressure + RPM -> real oil-system protection rather than a simple switch.
- EMAP + MAP -> turbine/exhaust restriction ratio.
- Turbo speed + MAP + RPM -> overspeed protection and turbo sizing validation.
- Front speed + rear/transmission speed -> wheel-slip analysis.
- IMU + wheel speed -> launch and wheelie analysis.

## Wiring impact

The existing five-sheet wiring package remains valid but must be revised to accommodate the expansion.

Required additions:

- new analogue-input allocation table;
- additional FT550 sensor-reference and sensor-return branches where compatible;
- dedicated sensor connectors and harness branches;
- new turbo-instrumentation schematic sheet;
- protection-strategy sheet mapping sensor faults to warning/derate/cut actions;
- expansion of the production connector index and harness branch schedule;
- new VERIFY items for exact input cavities, transfer functions and selected sensor models.

No existing OEM sensor is removed by this expansion.
