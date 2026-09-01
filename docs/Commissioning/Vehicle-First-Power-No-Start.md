# Vehicle First-Power / No-Start Commissioning

## Objective

Commission the Turbo V-Rod Destroyer electrical system on the vehicle without permitting combustion. The purpose is to verify power distribution, grounds, references, sensor plausibility, CAN communications, PMU behavior, SparkPRO wiring, injector interface integrity and starter/cranking signals before fuel injection and ignition are enabled.

## Non-negotiable state

Before beginning:

- Fuel injectors electrically disabled at X62/X63 interface or injector +12 V feed isolated.
- SparkPRO coil outputs disabled/unplugged at X61 or coil +12 V feed isolated.
- Fuel pump output O1 disabled unless a specific low-risk pump test is being executed.
- Boost-control solenoid O6 de-energised.
- Motorcycle secured against movement.
- Battery fully charged and fused/protected test supply available.
- Fire extinguisher present.
- No fuel leaks or exposed conductors.

No step in this procedure authorises first start.

## Stage 1 - Cold resistance and polarity checks

With battery disconnected:

1. Verify battery positive is not shorted to J-P02 ground.
2. Verify J-P02 to engine case has very low resistance.
3. Verify FT550 B1/B2 power grounds return to J-P02 and are not routed through sensor-return splices.
4. Verify SparkPRO pins 2 and 5 each return independently to J-P02.
5. Verify PMU pin 25 returns to J-P02.
6. Verify sensor return A12/B26 is isolated from high-current output paths except at the intended reference topology.
7. Verify CAN H/L continuity end-to-end and no H/L short.
8. Verify approximately 60 ohms across CAN H/L only when both end terminations are enabled.
9. Verify CKP shield/low-level wiring has no continuity to ignition primary conductors.

GO criterion: no unexpected shorts, opens or cross-domain continuity.

## Stage 2 - Current-limited first power

Power the system through a current-limited source or suitable fused test feed.

Initial conditions:

- PMU outputs disabled.
- Injectors disabled.
- SparkPRO coil outputs disabled.
- Starter disabled.

Verify:

- FT550 powers normally.
- PMU-16 powers normally.
- No unexpected heating.
- No PMU output activates.
- Battery/current draw is within a plausible electronics-only range and stable.
- No smoke, odor or connector heating.

Any unexpected current rise is an immediate STOP condition.

## Stage 3 - Reference-voltage verification

Measure at FT550 and at sensor connectors:

- A14 5 V reference to selected sensor return.
- Sensor return A12/B26 relative to J-P02.
- TPS 5 V supply.
- MAP 5 V supply if configured.
- Fuel-pressure and oil-pressure transducer 5 V supplies.

Acceptance:

- 5 V reference stable and within manufacturer tolerance.
- No meaningful reference collapse as sensors are connected one at a time.
- Sensor return does not carry actuator/load current.

Record every measurement.

## Stage 4 - Static sensor plausibility

With engine stopped:

### TPS

- Closed-throttle voltage plausible.
- Smooth increase to WOT.
- No dropouts.
- Calibrate closed/WOT in FTManager only after electrical behavior is proven.

### MAP

- Engine-off reading consistent with atmospheric pressure.
- Apply known vacuum/pressure if available and confirm monotonic response.

### ECT / IAT

- Both temperatures plausible for ambient/engine condition.
- Warm sensors gently and confirm direction/rate of change.

### Oil and fuel pressure transducers

- Engine-off values near expected zero/reference state.
- Known test pressure preferred before release.

### VSS / gear / neutral

- Verify neutral-switch logic.
- Rotate wheel/output safely and confirm VSS activity if practical.

No implausible sensor may be bypassed with a software offset merely to continue commissioning.

## Stage 5 - CAN backbone live verification

Configure CAN2 at 1 Mbps.

Capture FT550 CAN A traffic and record:

- Actual ProductID / unique identifier.
- Arbitration IDs for MessageIDs 0x600, 0x601, 0x602.
- Update rate.
- Decoded TPS/MAP/ECT/RPM/pressure values compared to FTManager.

Then populate PMU Client production receive filters.

Verify:

- FT_TPS_VALID.
- FT_MAP_VALID.
- FT_ECT_VALID.
- FT_OILP_VALID.
- FT_FUELP_VALID.
- FT_RPM_VALID when cranking later.

Do not enable PMU logic based on assumed unique-ID-0 arbitration IDs.

## Stage 6 - PMU low-risk output tests

Use temporary low-current loads where possible before connecting final devices.

Test individually:

- O8 warning lamp.
- O10 logger/service feed.
- O3/O4 fan outputs using test lamp/load before final fan where practical.
- O5 charge-cooler pump output if fitted.
- O6 boost solenoid supply with solenoid disconnected first.

Confirm commanded state, measured voltage, PMU current reading and fault reporting.

High-current pump/fan tests must still follow the dedicated bench/current evidence procedures before final current-limit freeze.

## Stage 7 - Fuel-pump dry control validation

Keep fuel delivery disabled or pump electrically substituted by a safe test load.

Validate O1 logic:

1. MASTER_ENABLE off -> O1 off.
2. MASTER_ENABLE on -> prime only for configured duration.
3. No start/RPM -> O1 turns off after prime.
4. START_REQUEST -> O1 on.
5. KILL_REQUEST -> O1 off immediately.
6. Simulated/later real RPM valid -> run continuation behaves as designed.
7. CAN loss -> grace/fallback behavior matches PMU control specification.

Do not use this stage to pressurise an unverified fuel system.

## Stage 8 - SparkPRO continuity and command-path verification

Coils remain disconnected from SparkPRO outputs.

Verify:

- FT550 A8 reaches SparkPRO pin 1 only.
- FT550 A9 reaches SparkPRO pin 3 only.
- SparkPRO pin 6 routes only to front coil branch.
- SparkPRO pin 4 routes only to rear coil branch.
- SparkPRO pins 2 and 5 each have independent 1.0 mm2 power-ground returns to J-P02.
- No continuity exists between SparkPRO outputs and CKP/sensor wiring.

If oscilloscope-safe test mode is available, verify A8/A9 logic-command activity without energising coils.

Do not connect coils until HC-010/HC-011 and dwell strategy are closed.

## Stage 9 - Injector-interface verification

Injectors remain disabled.

Confirm exactly one configuration is installed:

- DIRECT_DRIVE_APPROVED, or
- PEAK_HOLD_INSTALLED.

Verify:

- A1 routes only to front-injector command path.
- A2 routes only to rear-injector command path.
- Direct jumper and Peak & Hold path cannot both be active.
- X62-X65 labels match build record.
- Injector +12 V feed remains isolated for no-start commissioning.

No injector may be pulsed until HC-008/HC-009 close the electrical-class gate.

## Stage 10 - Starter/cranking test with fuel and ignition disabled

Only after Stages 1-9 pass:

- Keep injectors disabled.
- Keep coils/SparkPRO outputs disabled.
- Enable starter circuit.
- Crank engine briefly.

Record:

- Battery voltage during crank.
- J-P02/engine ground voltage drop.
- FT550 supply voltage.
- PMU supply voltage.
- CKP waveform and polarity.
- FT550 cranking RPM.
- PMU FT_RPM and FT_RPM_VALID.
- CAN health during cranking.
- Any resets or brownouts.

Acceptance:

- Stable FT550/PMU operation.
- No unexpected reset.
- Clean CKP waveform.
- Consistent cranking RPM.
- Correct ENGINE_CRANKING state.
- Fuel pump and ignition remain disabled by commissioning interlock.

## Stage 11 - Kill and fault-priority test on vehicle

While cranking-disabled or with starter inhibited:

- Assert KILL_REQUEST.
- Confirm O1/O2/O6 off.
- Confirm warning/status behavior.
- Remove CAN and confirm fallback states.
- Restore CAN and confirm deterministic recovery.

Hardwired kill must remain authoritative regardless of CAN state.

## Stage 12 - No-start release review

The vehicle may advance to the first-start preparation milestone only when all items below are recorded PASS:

- Power/ground integrity.
- 5 V reference stability.
- Static sensor plausibility.
- Live FT550 CAN arbitration IDs captured.
- PMU receive channels proven.
- PMU safe-state output logic proven.
- SparkPRO pin path verified with coils still disabled.
- Injector interface mode physically verified with injectors still disabled.
- CKP polarity/waveform and cranking RPM proven.
- No ECU/PMU brownout during cranking.
- Kill priority and CAN-loss behavior proven.

First-start permission additionally requires injector electrical class, coil dwell/current strategy, fuel-system leak/pressure test, timing verification strategy and all other release gates identified in the Verification Register.

## Evidence package

Save:

- photos of J-P01/J-P02 and module mounting;
- multimeter readings;
- scope captures for CKP/cranking supply;
- FTManager screenshots/logs;
- PMU Client logs;
- CAN capture;
- completed test matrix;
- any failed-test corrective action.

## Release state

Vehicle first-power/no-start procedure: **FROZEN REV 0.1**.

Actual vehicle execution: **NOT YET PERFORMED**.
