# Physical Harness Measurement & Dimensional Freeze – Rev 1 Prototype

## Purpose

Convert the RFQ/prototype cable-length estimates into measured motorcycle-specific dimensions suitable for a Golden Harness and repeat manufacture.

## Release progression

`RFQ_READY / BUILD_DATA_OPEN` → `PHYSICAL_MEASUREMENT_IN_PROGRESS` → `DIMENSIONAL_FREEZE_CANDIDATE` → `MANUFACTURING_RELEASED_REV1` → prototype fit → `GOLDEN_HARNESS_VALIDATED`.

## Measurement rules

1. Install or positively locate the FT550, PMU16, SparkPRO-2, boost solenoid, relays, service connector, pumps, fans, sensors and all retained OEM devices before measuring.
2. Measure the intended harness route, not straight-line distance between connectors.
3. Measure to connector backshell/boot datum, not sensor body centre.
4. Record service-loop allowance separately from routed length.
5. Steering/headstock branches must be measured at centre, full-left and full-right lock. Use the longest non-strained requirement.
6. Rear/suspension branches must account for full expected suspension movement and service access.
7. Turbo/exhaust branches must record minimum hot-surface clearance and heat-protection length.
8. Record breakout positions from a common harness datum so a manufacturer can reproduce the loom on a harness board.
9. Do not shorten CKP/CAN/sensor routes by crossing high-current ignition, injector, pump, fan or starter paths.
10. Prototype cut lengths remain intentionally longer than installed dimensions until physical fit is accepted.

## Datums

Freeze the following datums before final measurement:

- D00: main harness origin / primary bulk breakout.
- D01: FT550 connector backshell datum.
- D02: PMU16 connector/stud datum.
- D03: SparkPRO-2 connector datum.
- D04: front-cylinder engine breakout.
- D05: rear-cylinder engine breakout.
- D06: headstock/handlebar moving-loop entry.
- D07: rear-frame/fuel-pump breakout.
- D08: radiator/fan breakout.
- D09: turbo/boost-control breakout.
- D10: service/CAN connector location.

Actual physical locations are to be photographed and referenced in the build record.

## Required measurements

Complete `Bike-Side-Measurement-Worksheet.csv` and `B01-B44-Dimensional-Freeze-Worksheet.csv`.

For every branch capture:

- start datum;
- end connector/device;
- routed centreline length;
- service-loop allowance;
- prototype cut length;
- final accepted finished length;
- wire/cable class;
- loom covering diameter/type;
- boot orientation;
- breakout clocking/direction where important;
- heat protection length;
- clamp/P-clip locations;
- minimum bend radius concerns;
- movement requirement;
- manufacturing tolerance after prototype acceptance.

## Suggested dimensional tolerances after Golden Harness validation

These are manufacturing starting points only and may be tightened/relaxed by the harness builder:

- branches ≤300 mm: ±10 mm;
- 301–750 mm: ±15 mm;
- 751–1500 mm: ±20 mm;
- moving/service-loop branches: dimension plus explicit minimum loop requirement rather than relying only on symmetric tolerance.

Connector cavity placement, polarity and electrical topology have zero dimensional tolerance conceptually: they must match the released schedule exactly.

## Golden Harness process

1. Build Rev 1 prototype with current first-cut allowances.
2. Fit without cutting the motorcycle-side OEM components or forcing connectors into position.
3. Mark each breakout and service loop in situ.
4. Remove harness and measure accepted finished dimensions.
5. Record every change from prototype schedule.
6. Update branch drawing/string-board dimensions.
7. Perform full acceptance test.
8. Photograph the accepted harness flat and installed.
9. Freeze the accepted as-built BOM, connector PNs, wire sizes and dimensions.
10. Promote to `GOLDEN_HARNESS_VALIDATED` only after electrical and physical acceptance.

## Release blockers

`MANUFACTURING_RELEASED_REV1` requires at minimum:

- all installed component locations frozen;
- B01–B19 and B32–B44 dimensions measured or formally dispositioned;
- B20–B31 explicitly DNP or fully defined;
- B10/B11/B12/B15/B39/B40 high-current sizing closed from load/current evidence;
- all production connector/terminal selections frozen;
- X70 sealed relay sub-harness components approved;
- steering and suspension movement checks complete;
- turbo/exhaust heat-clearance review complete;
- engineering approval of the dimensional worksheet.

Current state: **PHYSICAL_MEASUREMENT_PACK_RELEASED / MEASUREMENTS_PENDING**.
