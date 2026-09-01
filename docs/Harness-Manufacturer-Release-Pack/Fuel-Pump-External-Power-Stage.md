# Fuel Pump Power Stage – 4.0 mm² Wiring Baseline and Measurement-Gated Relay Decision

## Verified PMU constraint

ECUMASTER documents PMU16 O1 (pin 38) and O2 (pin 39) as 25 A maximum high-side outputs. Connector-terminal current capability must also be considered with temperature and adjacent loaded terminals.

## Project decision

Fuel-pump feed and dedicated return conductors are now **4.0 mm² production baseline per pump**.

This cable size is fixed for the present harness revision and is not conditional on the final pump current measurement.

The decision to drive the pump directly from PMU O1/O2 or through an external relay/SSR is **measurement gated**.

Do not assume an external relay is required until the actual installed pump is identified and its steady-state and inrush current are measured under representative operating conditions.

## Direct PMU path eligibility

Direct PMU drive may be considered only if all of the following are proven:

- measured steady-state pump current is comfortably below the applicable PMU output continuous limit;
- measured inrush/peak current and duration are compatible with the PMU output protection/current-limit behaviour;
- the exact PMU terminal/contact and connector arrangement is suitable for the measured current with applicable derating;
- 4.0 mm² conductor is compatible with the selected terminal/contact or an approved transition is used;
- configured PMU current protection can tolerate normal pump inrush while still protecting the conductor/connector/load;
- installed voltage-drop and thermal tests pass;
- repeated hot-start and hot-fuel operating tests do not create nuisance trips or terminal overheating.

If any of those conditions fail, use the external power-stage architecture below.

## External power-stage fallback

If measured pump current is too high for comfortable direct PMU operation:

`Battery / protected distribution -> dedicated fuse/protection -> sealed automotive relay or approved solid-state high-current switch -> 4.0 mm² pump feed -> pump -> 4.0 mm² dedicated return/star ground`

Control path:

`PMU O1 or O2 -> relay/SSR control input`

The external switching device must default OFF on loss of PMU command or control power.

## Cable rule

- fuel-pump positive feed: **4.0 mm²**;
- dedicated fuel-pump return: **4.0 mm²**;
- applies independently to primary and any secondary/staged pump;
- do not downsize after a low-current measurement without a formal project revision;
- final connector/terminal selection must accept the 4.0 mm² conductor or use an approved sealed transition/power connector arrangement.

## Measurement required before switching decision

Record for each pump:

1. exact manufacturer/model/part number;
2. test voltage;
3. fuel type and representative system pressure/flow condition;
4. cold-start peak/inrush current;
5. stabilised steady current;
6. hot pump/hot fuel steady current;
7. restart inrush when hot;
8. PMU output current trace if trialled directly;
9. connector/terminal temperature rise;
10. installed voltage drop on both positive and return paths.

## Decision states

Use exactly one final state per pump:

- `DIRECT_PMU_DRIVE_APPROVED`
- `EXTERNAL_POWER_STAGE_REQUIRED`

Until measurement is complete:

`FUEL_PUMP_SWITCHING_ARCHITECTURE_MEASUREMENT_GATED`

## Protection

Protection settings are selected from the measured operating and inrush evidence. A 30 A design assumption does not automatically mean a 30 A fuse or PMU limit.

## PMU logic

Whether direct or external switched, the PMU retains ownership of:

- prime timing;
- start/run permission;
- kill/master priority;
- CAN/RPM fallback logic;
- warning/fault logic.

## Current release status

**4.0 mm² PUMP FEED/RETURN FROZEN**

**RELAY/SSR DECISION PENDING PUMP VERIFICATION**
