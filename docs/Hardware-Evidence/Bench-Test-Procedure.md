# Bench Test Procedure - Loads, Injectors and Ignition Coils

## Scope

This procedure generates the measured evidence required to freeze conductor size, connector/terminal selection and PMU current protection for the Turbo V-Rod Destroyer harness.

## Safety

Use a fused bench supply/battery arrangement appropriate to the tested load. Secure motors/fans before energising. Keep fuel-system electrical testing separated from fuel vapour. Do not pulse injectors dry for extended periods. Do not energise ignition coils without an appropriate test arrangement and known driver strategy.

## A. PMU-powered motor and auxiliary loads

For each load HC-001 to HC-007:

1. Record exact installed component part number and connector.
2. Record supply voltage before activation.
3. Capture startup/inrush current with a current probe or suitable shunt/logger.
4. Record peak current and approximate inrush duration.
5. Run until current stabilises and record steady current.
6. Repeat at the upper expected charging-system voltage where safe and practical.
7. Record route length from PMU to load and load return path.
8. Enter results into `Load-Current-Measurement-Sheet.csv`.
9. Only after these measurements, choose conductor size and PMU trip/retry values.

Acceptance requires stable operation without nuisance trip and a protection setting that remains below the safe capacity of the selected conductor/terminal while tolerating legitimate inrush.

## B. Injector characterization

For each injector HC-008/HC-009 and CC-001/CC-002:

1. Identify part number and connector family from the physical component.
2. Photograph connector face, keying and wire entry.
3. Measure coil resistance at controlled temperature and record meter method.
4. Verify whether the injector is high-impedance/saturated or requires peak-and-hold treatment from authoritative data or waveform testing.
5. When using a suitable injector driver/tester, capture current waveform and record peak/steady characteristics.
6. Determine terminal current suitability and final conductor class.
7. Do not connect to an FT550 injector output until driver compatibility is established.

## C. Ignition coil characterization

For each coil HC-010/HC-011 and CC-003/CC-004:

1. Identify exact coil part number and connector cavity functions.
2. Photograph connector face/keying and terminal style.
3. Establish whether the coil is smart/logic-level or requires an external/internal ignition power driver.
4. Measure primary resistance only as supporting evidence, not as proof of driver type.
5. Capture current/dwell waveform with appropriate test equipment if documentation does not conclusively establish compatibility.
6. Confirm required supply, ground and trigger polarity/level.
7. Freeze FT550 output/driver arrangement only after compatibility is verified.

## D. Evidence naming

Use evidence IDs from the CSV files. Store each image/capture with the ID in the filename, for example `HC-001-primary-pump-inrush.png` or `CC-003-front-coil-connector.jpg`.

## Release gate

Do not freeze a high-current wire size, PMU current limit, injector driver assignment or coil driver assignment until the corresponding evidence row is complete and status is `VERIFIED`.
