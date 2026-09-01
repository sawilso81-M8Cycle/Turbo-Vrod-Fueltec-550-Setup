# Full-Power Pull & Final Dyno Validation

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_FULL_POWER_PULL_PREP` and all higher-load tuning gates are PASS.

It authorises controlled full-load dyno validation only. It does not authorise track use, launch testing, top-speed testing or competition deployment.

## FP-001 Pre-pull release check

Before each full-load pull confirm:

- current FTManager calibration revision is recorded;
- PMU project revision is recorded;
- boost-control strategy revision is recorded;
- injector mode and fuel-pressure strategy are frozen;
- lambda front/rear are operational and correctly assigned;
- fuel and oil pressure channels are valid;
- ECT/IAT are inside the build-specific starting window;
- no CAN or PMU fault is active;
- hardwired kill is verified;
- dyno restraint/ventilation/cooling are verified;
- previous pull/log review is complete;
- no unresolved mechanical or thermal concern exists.

## FP-002 First full-load pull envelope

The first full-load pull is a validation event, not a power-maximisation event.

Use the previously approved boost target, RPM ceiling and load path. Do not add boost, timing or rev limit in the same pull.

Record continuously:

- RPM;
- TPS;
- MAP/boost target and actual;
- lambda front and rear;
- injector duty;
- fuel pressure;
- oil pressure;
- ECT/IAT;
- battery voltage;
- ignition timing;
- PMU O1/O2/O3/O4/O5/O6 state/current where available;
- CAN health;
- boost-control correction/feed-forward;
- any sync/misfire/fault indicator.

## FP-003 Immediate abort criteria

Abort the pull immediately for any unexplained or unsafe condition, including:

- fuel-pressure decay outside the verified strategy;
- oil-pressure loss or invalidity;
- lambda excursion outside the build-specific allowed region;
- one cylinder diverging materially from the other;
- injector duty reaching the build-specific release limit;
- uncontrolled boost rise, overshoot or creep;
- sync loss, misfire or RPM dropout;
- severe detonation/combustion evidence where monitored;
- ECT/IAT exceeding build-specific limits;
- PMU current-limit or retry event on a critical output;
- CAN loss affecting required protection or boost control;
- abnormal mechanical noise;
- operator uncertainty about a critical reading.

Do not embed generic internet values for AFR, injector duty, timing, pressure or temperature. Those limits must come from the verified build evidence.

## FP-004 First-pull log review

Do not repeat the pull until the complete log is reviewed.

Required review areas:

- front/rear lambda agreement and trend;
- injector-duty margin;
- fuel-pressure stability versus MAP/load;
- oil-pressure trend versus RPM/temperature;
- boost target/actual tracking;
- closed-loop correction magnitude;
- ignition timing behaviour;
- thermal rise;
- PMU output current and fault history;
- CAN validity;
- evidence of sync/misfire.

Any unexplained anomaly reopens the relevant lower-stage gate.

## FP-005 Repeatability pulls

After FP-004 PASS, perform repeat pulls only after returning to the defined pre-pull thermal state.

PASS requires repeatable:

- boost curve;
- lambda behaviour;
- fuel pressure;
- injector duty;
- ignition timing;
- torque/power curve shape;
- thermal rise;
- PMU/CAN behaviour.

Do not call one exceptional pull the final calibration.

## FP-006 Fuel-system headroom freeze

At the highest authorised load, record final injector duty, fuel pressure, pump behaviour and any secondary-pump staging.

The final calibration must retain documented margin from injector/pump/driver limits. If the system is at the edge of capacity, progression stops and hardware capacity must be addressed.

## FP-007 Cylinder-balance validation

Where dual lambda is fitted, verify front/rear cylinder behaviour independently across the full-load run.

Do not accept a good averaged lambda if one cylinder is outside the build-specific acceptable window.

## FP-008 Ignition/combustion validation

Review ignition timing together with torque response, lambda, plugs/combustion evidence and any available knock/combustion instrumentation.

Do not advance timing solely because torque increased on one pull. Final timing must be repeatable and conservative against the available evidence.

## FP-009 Thermal saturation / cooldown validation

Define the required cooldown state before another full-load pull.

Record IAT, ECT and relevant component temperatures across repeated runs. Heat soak that materially changes boost, lambda, timing demand or fuel pressure blocks final freeze until understood.

## FP-010 Mechanical and plug inspection

After the planned full-power sequence, shut down and inspect:

- plugs/combustion evidence where appropriate;
- fuel/oil/coolant leaks;
- turbo/exhaust fasteners;
- charge plumbing;
- SparkPRO/coils/connectors;
- PMU/FT550 connectors;
- harness heat exposure;
- wastegate/solenoid plumbing;
- unusual debris/noise/signs of distress.

## FP-011 Final calibration freeze

Only after repeatable PASS results:

- save final FTManager calibration with immutable revision identifier;
- save PMU project revision;
- save boost-control configuration;
- archive dyno graphs and all logs;
- record fuel type, boost target, rev limit, injector configuration and protection thresholds;
- record hardware revision and sensor calibration references;
- create a change-control note stating what would invalidate the freeze.

## FP-012 Final dyno validation report

Create a final report containing:

- calibration identifiers;
- hardware identifiers;
- peak and representative power/torque data;
- boost target versus actual;
- lambda front/rear;
- injector duty and fuel-pressure margin;
- oil-pressure evidence;
- thermal data;
- timing summary;
- PMU/CAN fault summary;
- repeatability evidence;
- unresolved limitations/operating restrictions.

## Release state

The project remains `FULL_POWER_DYNO_VALIDATION_ONLY` until FP-001 through FP-012 PASS.

Promotion target: `DYNO_CALIBRATION_FROZEN_READY_FOR_VEHICLE_VALIDATION_PREP`.

This state still does not authorise track launch, competition, top-speed or unrestricted road operation. Those require a separate vehicle/track validation milestone.
