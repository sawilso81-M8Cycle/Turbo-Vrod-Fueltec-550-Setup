# First-Start Preparation and GO / NO-GO Gate

## Purpose

This milestone prepares the Turbo V-Rod Destroyer FT550/PMU-16 installation for its first controlled combustion event. It does **not** authorise starting the engine by itself.

First start is permitted only after every mandatory gate below is recorded PASS with evidence.

## Mandatory preconditions

The Vehicle First-Power / No-Start procedure must already be complete, including stable FT550 and PMU power, verified 5 V reference, plausible sensors, live CAN, correct hardwired kill priority and a clean CKP/RPM signal during cranking.

### FS-G01 Injector electrical interface

- Measure both OEM 27772-06 injectors individually.
- Record controlled-temperature resistance and current evidence under HC-008/HC-009.
- Freeze exactly one configuration:
  - `DIRECT_DRIVE_APPROVED`, or
  - `PEAK_HOLD_INSTALLED - <exact FuelTech model/current class>`.
- Verify X62-X65 configuration physically matches the build record.
- Do not energise injectors while this gate is OPEN.

### FS-G02 Ignition electrical interface

- SparkPRO-2 remains the frozen passive-coil driver.
- Record both 32477-01A coil primary resistance/current-ramp evidence under HC-010/HC-011.
- Freeze a conservative initial dwell/current strategy from verified evidence and FuelTech limits.
- Confirm SparkPRO grounds, driven outputs and coil polarity/routing.
- Do not perform powered spark testing until this gate is PASS.

### FS-G03 Base timing / synchronisation

Before fuel is enabled:

1. Disable injector operation.
2. Use a timing light during cranking or other FuelTech-approved synchronisation method.
3. Command a fixed safe reference ignition angle in FTManager.
4. Confirm observed crank timing agrees with commanded timing within the project's accepted tolerance.
5. Correct trigger edge/offset only from measured evidence.
6. Repeat the check after any CKP polarity, trigger or offset change.

Do not attempt first combustion with unverified crank synchronisation.

### FS-G04 Fuel-system pressure and leak integrity

Before injectors are permitted to fire:

- pressure-test the complete fuel system with ignition disabled;
- verify pump prime/run logic;
- verify fuel-pressure sensor against a trusted mechanical reference where practical;
- inspect rail, injector seals, hose ends, regulator, filter and fittings;
- hold pressure long enough to identify seepage;
- record static/prime pressure and pressure decay;
- verify no fuel reaches unintended electrical or hot zones.

Any leak = immediate NO-GO.

### FS-G05 Lambda readiness

- Install and configure the selected wideband hardware.
- Confirm sensor heater/control status and sane free-air/ambient behaviour per manufacturer procedure.
- Confirm front/rear cylinder assignment if dual lambda is fitted.
- Confirm FTManager receives the intended lambda channels.
- Disable closed-loop corrections for the first controlled start unless a verified base calibration and commissioning plan explicitly enables them.

### FS-G06 Base calibration sanity

Before first start, independently review:

- engine displacement and cylinder count;
- firing/order configuration applicable to the VRXSE engine;
- injector flow value and electrical interface;
- fuel pressure/reference strategy;
- trigger pattern and synchronisation settings;
- ignition output assignment A8/A9 through SparkPRO-2;
- injector assignment A1/A2;
- TPS calibration;
- MAP/ECT/IAT calibration;
- conservative cranking/start enrichment;
- conservative ignition timing;
- boost control disabled so pneumatic system remains at minimum mechanical boost;
- rev limit and protection settings suitable for commissioning.

The OEM Destroyer injector calibration evidence already stored in the project identifies 27772-06 injectors and the 6.37 g/s factory race-tuner flow value. Do not substitute an aftermarket flow value without new evidence.

### FS-G07 Protection thresholds

Before first start:

- O6 boost-solenoid supply must remain disabled;
- configure conservative oil-pressure warning/shutdown strategy without treating sensor-invalid as healthy;
- configure fuel-pressure warning strategy;
- configure ECT warning/fan strategy;
- verify kill input immediately removes ignition/injection enable intent;
- freeze PMU current limits only where measured load evidence supports them;
- ensure logger/FTManager recording is active for the first start.

Do not use unverified CAN pressure values as the sole engine-protection path.

### FS-G08 Mechanical readiness

Confirm at minimum:

- engine oil level and correct priming state;
- coolant filled/bled where applicable;
- fuel type matches calibration;
- throttle mechanically returns to closed position;
- intake/turbo plumbing secure;
- exhaust clear of loose material;
- battery secured and adequately charged;
- transmission neutral independently confirmed;
- motorcycle restrained and ventilated;
- fire extinguisher and immediate master/kill access available.

## First-start release state

The build record must contain one of these states:

- `FIRST_START_NO_GO`
- `FIRST_START_READY`

`FIRST_START_READY` requires FS-G01 through FS-G08 PASS plus completion of the no-start release gate.

## First-start operating envelope

When authorised later, the first start is a short commissioning event, not a tuning pull. Boost control remains disabled. The operator watches RPM, oil pressure, fuel pressure, lambda, ECT, battery voltage, CAN health and PMU faults and uses the hardwired kill for any abnormal condition.

No load, high RPM or boost testing is authorised by this document.

## Evidence retention

Retain FTManager logs, PMU logs, CAN capture, timing verification evidence, fuel-pressure/leak-test record, injector/coil electrical evidence and completed checklist with the build/revision identifier.
