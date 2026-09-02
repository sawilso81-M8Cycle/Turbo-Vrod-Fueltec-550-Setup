# Single-Session Electrical Test Campaign Pack

## Purpose

Consolidate the remaining high-priority electrical evidence campaign into one controlled workshop sequence covering fuel pumps, injectors, SparkPRO/coils and cooling loads.

This campaign supplies evidence for BD-001 through BD-004 and the HP-3 Electrical Blocker Closure gate. It does not authorise final wiring values by assumption and does not authorise first engine start.

## Test order

Run in this order where practical:

1. Session setup / instrument verification;
2. component identity capture;
3. passive resistance/continuity checks with circuits de-energised;
4. fuel-pump current/inrush/voltage-drop tests;
5. cooling-load current/inrush tests;
6. injector electrical classification;
7. SparkPRO/coil controlled verification;
8. hot/repeat measurements where applicable;
9. results review and engineering decisions.

Stop immediately on unexpected heating, smoke, unstable supply, wiring damage, abnormal current or equipment limits being exceeded.

## Instruments

Recommended minimum:

- current clamp with DC inrush/min-max capture suitable for expected pump/fan currents;
- calibrated or verified DMM;
- bench supply only where appropriate and correctly current limited;
- oscilloscope for injector/ignition/trigger-related waveform work where required;
- temperature measurement device;
- fused test leads;
- known-good battery/charging source;
- FuelTech FTManager logging where relevant;
- PMU logging/configuration tools where relevant.

Record instrument model, serial number if available, range and verification/calibration status in the master register.

## General measurement rules

- Record battery/source voltage at the same time as current.
- Distinguish inrush/peak from steady-state current.
- Record cold and hot results where thermal state changes the load materially.
- Do not size protection from one unexplained peak reading.
- Do not substitute catalogue current for measured installed current where a physical test is available.
- Keep raw evidence such as screenshots, logs and scope captures.

## EC-01 Fuel Pump 1

Capture:

- exact PN and manufacturer;
- native connector;
- source voltage before activation;
- cold inrush/peak current;
- cold steady current;
- voltage at pump while running;
- voltage drop feed side;
- voltage drop return side;
- hot steady current after representative operation;
- hot restart inrush where safe/practical;
- connector/terminal temperature trend.

Repeat for Pump 2 as EC-02.

### Fuel-pump decision output

Use measured evidence to decide:

`DIRECT_PMU_DRIVE_APPROVED`

or

`EXTERNAL_POWER_STAGE_REQUIRED`

The 4.0 mm² minimum feed and 4.0 mm² dedicated return per pump remain locked regardless of the switching decision unless a later engineering change explicitly revises them.

## EC-03 Injector electrical classification

For front and rear injectors capture:

- exact PN/markings;
- resistance at known approximate temperature;
- pair-to-pair consistency;
- manufacturer electrical data if available;
- any existing driver requirement evidence.

Do not infer injector driver mode solely from appearance.

Decision output:

`FT550_DIRECT_DRIVER_APPROVED`

or

`PEAK_AND_HOLD_STAGE_REQUIRED`

or

`FURTHER_TEST_REQUIRED`

## EC-04 SparkPRO / coils

Capture exact coil and SparkPRO hardware identification first.

Controlled verification should establish enough evidence to freeze:

- coil/SparkPRO supply current;
- B40 conductor/protection requirement;
- commanded dwell operating range;
- evidence of abnormal coil/SparkPRO heating;
- supply voltage during representative operation;
- ignition noise effects where observable.

Do not conduct uncontrolled high-energy spark testing near fuel vapour or open fuel systems.

Decision output:

`B40_PROTECTION_FROZEN`

and, only with adequate evidence,

`DWELL_BASELINE_RELEASED`

Otherwise retain `FURTHER_TEST_REQUIRED`.

## EC-05 Radiator fan B11

Capture:

- exact PN/markings;
- cold start/inrush current;
- steady current;
- hot/restart current where applicable;
- supply voltage;
- connector temperature;
- voltage drop.

Decision output determines final B11 wire/protection and direct-PMU/external-stage architecture.

## EC-06 Charge-cooler pump B12

First record:

`FITTED`

or

`DNP`

If fitted, capture the same current/inrush/voltage-drop/thermal evidence appropriate to the device.

## Evidence naming

Recommended pattern:

`EC##_DEVICE_TESTTYPE_YYYYMMDD.ext`

Examples:

`EC01_PUMP1_INRUSH_20260903.png`

`EC03_FRONT_INJECTOR_RESISTANCE_20260903.jpg`

`EC04_SPARKPRO_SUPPLY_CURRENT_20260903.csv`

## Session closeout

Before ending the electrical campaign:

- confirm all raw evidence is saved;
- confirm every measured value has units;
- record source voltage for current tests;
- flag suspect measurements for retest rather than averaging them away;
- record device temperature/state where relevant;
- identify any instrument range limitations;
- update each engineering decision register only from accepted evidence.

## Release state

Current:

`SINGLE_SESSION_ELECTRICAL_TEST_CAMPAIGN_RELEASED`

After complete accepted testing:

`BD001_BD004_EVIDENCE_CAPTURED`

After engineering disposition:

`HP3_ELECTRICAL_BLOCKERS_CLOSED`

only if every applicable HP-3 blocker is genuinely resolved.
