# Launch & Track Release

## Authority

This package becomes executable only after the vehicle-validation milestone reaches `READY_FOR_LAUNCH_AND_TRACK_RELEASE_PREP` with retained evidence.

It authorises staged launch and track validation only. It does not create a blanket competition release. The bike remains test-only until the final release gate is passed and the released configuration is frozen.

## Configuration lock

Before every launch/track session record:

- FTManager calibration revision;
- PMU project revision;
- boost-control configuration;
- hardware build revision;
- tyre/wheel configuration;
- launch and shift configuration;
- wheel-speed source/configuration;
- weather/track conditions where relevant;
- logger configuration.

No unlogged configuration change is permitted between passes.

## LT-001 Mechanical and chassis release

Confirm chassis, steering, wheels, tyres, brakes, drivetrain, mounts, fasteners, chain/belt/final drive, clutch and all safety hardware are inspected and suitable for the intended staged test.

Any unresolved chassis/drivetrain defect = NO-GO.

## LT-002 Safety inputs and abort controls

Verify before every session:

- hardwired kill works immediately;
- master enable works;
- brake input is correctly detected;
- clutch input is correctly detected if used;
- neutral/gear state is verified;
- launch cannot arm in an invalid state;
- CAN loss or invalid gear/wheel-speed cannot increase boost authority;
- O6 de-energised path still returns to minimum mechanical boost.

## LT-003 Launch arming prerequisites

Launch control may arm only when all project-defined prerequisites are true. Typical prerequisites may include valid engine-running state, verified gear/neutral state, clutch/brake state, minimum/maximum RPM window, valid wheel-speed data and healthy CAN/PMU state.

The exact logical expression must be frozen in the build-specific release record.

If a required prerequisite is invalid or stale, launch state must remain disarmed.

## LT-004 Launch RPM baseline

Establish launch-RPM control first at minimal launch torque/boost authority.

Validate:

- repeatable RPM control;
- no uncontrolled oscillation;
- no sync loss;
- no pressure or lambda anomaly;
- clutch/brake interlock behaviour;
- immediate exit when launch prerequisites are removed.

Do not combine a new launch-RPM strategy with an aggressive new boost strategy in the same first test.

## LT-005 Launch boost authority

Start from the lowest practical launch-boost authority consistent with the verified wastegate/boost system.

Increase only after reviewing complete logs from the previous launch.

Any unexpected boost jump, creep, pressure loss, severe lambda divergence, misfire, wheel-speed plausibility failure or uncontrolled wheel lift blocks progression.

## LT-006 Wheel-speed and slip validation

Verify front/rear wheel-speed signals, scaling and direction under actual acceleration.

Where slip logic is used:

- calculate slip only from validated sources;
- define plausible operating ranges;
- stale/invalid wheel-speed must reduce torque/boost authority or disable traction logic safely;
- traction intervention must be distinguishable in logs from normal boost/ignition control.

Do not use unverified slip values to add torque.

## LT-007 Front-wheel lift handling

If front-wheel lift detection is available, validate the signal independently before using it for control.

Control response should reduce propulsion authority in a predictable, bounded way. Loss of front-wheel-speed during a genuine lift must not be misinterpreted as a sensor failure that increases torque.

The exact lift-response strategy remains build-specific and must be log validated.

## LT-008 Shift strategy validation

Validate each intended shift strategy progressively.

Confirm:

- correct gear transition detection;
- no false shift trigger;
- acceptable RPM recovery;
- boost/torque authority after shift remains within the verified gear map;
- fuel/oil/lambda/thermal channels remain stable;
- no CAN/sync fault occurs during shift transient.

## LT-009 Short launch progression

Progress through deliberately limited launches before any full-pass attempt.

Suggested sequence concept:

1. launch only / immediate abort;
2. short low-speed acceleration;
3. longer acceleration with one verified shift;
4. progressively longer distance only after prior logs are accepted.

Distance, RPM and load boundaries must be defined in the build-specific test sheet rather than assumed here.

## LT-010 Brake and kill response under motion

At a safe low-energy condition, verify that removing propulsion demand through rider controls and hardwired kill produces the expected rapid safe state without PMU/ECU latch-up or unsafe output persistence.

Do not simulate this at an energy level where loss of propulsion control could create an unacceptable hazard.

## LT-011 Progressive track passes

Once short-launch progression is accepted, perform staged track passes with increasing duration/authority. Review each pass before the next.

Required logged channels include at minimum:

- RPM;
- gear;
- TPS;
- MAP/boost target/actual;
- boost-control duty/correction;
- front/rear wheel speed;
- calculated slip if used;
- lambda front/rear;
- fuel pressure;
- oil pressure;
- IAT/ECT;
- battery voltage;
- ignition timing;
- injector duty where available;
- PMU outputs/faults;
- CAN health;
- launch/traction/shift state flags.

## LT-012 Full-pass validation gate

A first full pass is permitted only after the staged launches and partial passes show repeatable behaviour with no unresolved critical anomaly.

Treat the first full pass as validation, not an attempt to maximise performance.

Abort for any unexplained boost overshoot, pressure loss, severe lambda divergence, misfire/sync loss, traction instability, uncontrolled lift, drivetrain/chassis concern, thermal escalation or critical PMU/CAN fault.

## LT-013 Repeatability and heat-soak

Repeat only after appropriate inspection and cooldown. Compare successive passes for:

- launch RPM consistency;
- boost curve consistency;
- shift timing/RPM recovery;
- wheel-speed/slip pattern;
- lambda and fuel-pressure repeatability;
- temperature rise;
- PMU current/fault history;
- connector/harness heat exposure.

Increasing drift with heat blocks competition release.

## LT-014 Post-session inspection

After each session inspect:

- tyres/wheels/brakes;
- steering/suspension;
- clutch/final drive;
- engine/turbo/exhaust mounts;
- fuel/oil/coolant system;
- harness abrasion/heat exposure;
- FT550/PMU/SparkPRO mounting and connectors;
- boost-control plumbing;
- logs for PMU overcurrent/retry and CAN errors.

## LT-015 Competition configuration freeze

When the test program is accepted, freeze together:

- FTManager calibration;
- PMU project;
- boost tables/limits;
- launch strategy;
- gear-based authority tables;
- traction/wheel-speed settings;
- shift strategy;
- hardware build revision;
- tyre/wheel configuration relevant to wheel-speed scaling.

Any subsequent material change reopens the relevant verification gates.

## Release states

Progression:

`READY_FOR_LAUNCH_AND_TRACK_RELEASE_PREP`
→ `LAUNCH_TRACK_VALIDATION_ONLY`
→ `COMPETITION_RELEASE_CANDIDATE`
→ `COMPETITION_RELEASED`

`COMPETITION_RELEASED` requires all mandatory LT tests PASS, no unresolved critical anomaly, configuration freeze complete and a final release record signed/revision-controlled.

## Important boundary

Competition release is conditional on the tested configuration and operating envelope. It is not transferable automatically to different boost levels, fuels, tyres, gearing, engine hardware or calibration revisions.
