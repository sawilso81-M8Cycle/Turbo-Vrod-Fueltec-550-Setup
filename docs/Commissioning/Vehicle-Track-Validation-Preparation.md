# Vehicle / Track Validation Preparation

## Authority

This milestone becomes executable only after the dyno calibration is frozen and the project has reached `DYNO_CALIBRATION_FROZEN_READY_FOR_VEHICLE_VALIDATION_PREP`.

It prepares the Turbo V-Rod Destroyer for controlled vehicle-level validation. It does **not** authorise unrestricted launch, top-speed or competition operation.

## Core principle

Vehicle validation must prove that the dyno-validated engine/calibration remains safe when exposed to real drivetrain load, vibration, heat soak, wheel-speed behaviour, braking, shifting and transient chassis dynamics.

## VT-001 Chassis and drivetrain readiness

Verify at minimum:

- tyres, pressures and condition suitable for the planned test environment;
- wheel bearings and axle security;
- steering-head and swingarm integrity;
- brake operation and fluid condition;
- chain/belt/final-drive condition and tension;
- engine/transmission mounting hardware;
- clutch operation and free-play strategy;
- throttle return and grip operation;
- fuel/oil/coolant systems leak free;
- turbo/exhaust/intake hardware secure;
- harness clear of steering, suspension, hot surfaces and rotating parts.

Any mechanical uncertainty blocks progression.

## VT-002 Electrical/vibration readiness

Inspect and strain-relieve FT550, PMU-16, SparkPRO-2, X51, X60-X65, sensor connectors and all high-current branches.

Confirm:

- no connector can fret against a sharp edge;
- grounds cannot loosen under vibration;
- CAN wiring remains twisted/secured;
- CKP wiring remains separated from ignition/high-current conductors;
- heat shielding and loom support are adequate around turbo/exhaust zones.

## VT-003 Control-state lock

Before each vehicle session record:

- FTManager calibration revision;
- PMU project revision;
- boost-control revision;
- hardware build revision;
- tyre/final-drive configuration;
- test environment and operator.

Do not change boost, ignition, fuel and launch strategy simultaneously.

## VT-004 Low-speed function check

Begin with controlled low-speed operation only.

Validate:

- throttle progression;
- clutch engagement;
- brakes;
- steering;
- gear indication;
- engine response and return to idle;
- no harness movement/fouling;
- no fluid leaks after movement.

## VT-005 Wheel-speed and gear validation

Where wheel-speed/gear signals are available, verify actual selected gear and wheel-speed behaviour against logged values.

Do not use gear-based boost authority until gear decoding is proven through the intended gears.

## VT-006 Gear-by-gear boost-authority matrix

Create a build-specific table for each validated gear with:

- allowed boost target or duty ceiling;
- RPM window;
- TPS/load window;
- speed window where applicable;
- traction/wheel-speed plausibility requirements;
- fallback target when gear/wheel-speed data becomes invalid.

Invalid gear or wheel-speed input must never increase boost authority.

## VT-007 Brake and kill validation

At controlled low load verify:

- rider kill immediately removes engine torque authority as designed;
- brake operation remains mechanically independent of ECU/PMU state;
- any brake-linked control logic cannot prevent normal braking;
- master/kill state is logged correctly;
- restart behaviour is deterministic after a kill event.

## VT-008 Heat-soak and vibration session

Run a controlled vehicle session long enough to expose the harness and modules to realistic vibration and heat soak without exceeding the validated load envelope.

Inspect:

- FT550/PMU/SparkPRO temperatures and mounting;
- connector movement;
- PMU current-limit/retry history;
- CAN errors/dropouts;
- CKP/sync stability;
- fuel/oil/coolant leaks;
- turbo/exhaust heat impact on adjacent wiring.

## VT-009 Staged road/track load progression

Progress through a predefined test matrix from low to higher vehicle load, always remaining inside the dyno-validated engine envelope.

At each step log at minimum:

- RPM;
- TPS;
- MAP/boost target/actual;
- gear;
- vehicle/wheel speed where available;
- lambda front/rear;
- fuel and oil pressure;
- IAT/ECT;
- battery voltage;
- ignition timing;
- injector duty;
- PMU/CAN faults;
- boost correction/duty.

## VT-010 Traction and wheel-speed behaviour

Observe rear-wheel acceleration and any available front/rear speed comparison under staged load.

This stage is observation and validation first. Do not enable aggressive torque-management strategies merely because wheel-speed data exists.

Any traction intervention must later be commissioned with its own explicit test and release gate.

## VT-011 Shift/transient validation

Validate throttle lift, reapplication, gear change and boost recovery behaviour under controlled conditions.

Look for:

- fuel-pressure disturbance;
- boost overshoot after shift;
- lambda excursion;
- ignition breakup;
- sync error;
- drivetrain shock;
- unstable gear detection.

## VT-012 Post-session inspection

After each significant session inspect:

- tyres and brakes;
- final drive;
- engine/turbo fasteners;
- fuel/oil/coolant systems;
- harness and connectors;
- SparkPRO and PMU mounting;
- sensor leads;
- heat shields;
- PMU faults/current events.

## VT-013 Log and calibration review

Review every session before progressing. Any unexplained anomaly blocks the next test stage.

All calibration changes receive a new revision and stated reason.

## Launch and competition lockout

Launch-control, high-energy standing starts and competition operation remain locked until a separate launch/track-release milestone is completed.

Required lockout state before that milestone:

`LAUNCH_NOT_AUTHORISED`

## Release state

Project state during this milestone:

`VEHICLE_VALIDATION_ONLY`

Successful completion permits promotion to:

`READY_FOR_LAUNCH_AND_TRACK_RELEASE_PREP`

This state still does not itself authorise launch or competition use.
