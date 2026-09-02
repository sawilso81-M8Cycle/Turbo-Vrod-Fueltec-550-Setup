# Track Launch & Final Race Validation Pack

## Purpose

Define the controlled transition from dyno-proven Two-Step/launch-control operation into real track launches and final race-package validation.

This milestone validates the complete system in the environment that matters: clutch release, traction, wheel speed, engine RPM recovery, boost recovery, fuel delivery, ignition stability, electrical integrity, thermal behaviour and repeatability under actual launch acceleration.

## Entry conditions

Do not begin unless:

- `TWO_STEP_LAUNCH_CONTROL_COMMISSIONED` is PASS;
- `DYNO_LOAD_COMMISSIONING_ACCEPTED` is current;
- `CONTROLLED_BOOST_OPERATION_RELEASED` is current;
- mechanical inspection confirms drivetrain, clutch, chain/belt, tyres, brakes and fasteners are suitable for launch testing;
- track/test area is controlled and appropriate;
- required rider safety equipment and event/site procedures are satisfied;
- FT550, PMU16 and SparkPRO configuration revisions are archived;
- launch RPM, max activation time and launch-boost ceilings are explicitly defined;
- fuel, oil, AFR/lambda and temperature monitoring are valid;
- data logging is functioning;
- emergency shutdown and test-abort communication are defined.

## Test philosophy

Track validation remains progressive.

Start with short, deliberately reduced-energy launches and build toward the intended race launch only after the preceding stage demonstrates stable engine, electrical and chassis behaviour.

Do not chase elapsed time before the launch system is repeatable.

## TR-0 Pre-track baseline

Before the first launch record:

- calibration revision;
- PMU revision;
- launch-control revision;
- fuel;
- tyre pressures;
- rider/bike mass if used for analysis;
- launch RPM target;
- max launch duration;
- launch boost ceiling;
- boost strategy after clutch release;
- ambient temperature;
- track surface/condition notes;
- engine temperature;
- IAT;
- fuel pressure;
- battery voltage;
- clutch adjustment/state.

Output: `TR0_TRACK_BASELINE_ACCEPTED`

## TR-1 Static clutch/launch recheck

At the track, engine off or in a safe static state, reconfirm:

- clutch input transition;
- PMU launch request;
- X70 operation;
- FT550 A21 state;
- release transition;
- no A21 +12 V exposure;
- no input chatter.

Output: `TR1_STATIC_LAUNCH_CHAIN_ACCEPTED`

## TR-2 Reduced-energy launch

Perform a deliberately reduced-energy first launch.

Limit one or more of:

- launch RPM;
- TPS;
- launch boost;
- run distance;
- gear progression.

Capture:

- clutch release timestamp/state;
- engine RPM before release;
- minimum RPM after clutch engagement;
- RPM recovery rate;
- MAP/boost at release;
- boost drop/recovery;
- TPS;
- wheel speed/VSS;
- fuel pressure/differential;
- AFR/lambda;
- ignition command;
- injector duty;
- PMU faults;
- battery voltage;
- trigger errors.

Output: `TR2_REDUCED_LAUNCH_ACCEPTED`

## TR-3 Clutch-release behaviour

Analyse launch transition rather than only the resulting 60-foot time.

Evaluate:

- clutch release timing/repeatability;
- RPM drop magnitude;
- RPM recovery;
- engine bog or flare;
- boost loss and recovery;
- rear-wheel acceleration;
- front-wheel behaviour if measured/observed;
- wheelspin;
- clutch slip;
- driveline shock;
- A21 release timing;
- boost-control transition.

Output: `TR3_CLUTCH_RELEASE_BEHAVIOUR_ACCEPTED`

## TR-4 Progressive launch stages

Increase launch energy only in predefined stages.

Each stage should specify:

- launch RPM;
- launch boost ceiling;
- max Two-Step duration;
- TPS expectation;
- permitted run distance;
- shift/gear ceiling if restricted;
- wheelspin/traction abort criteria;
- RPM bog/overshoot criteria;
- fuel/oil/AFR/temperature limits;
- turbo-speed/EGT limits if measured.

Each stage is accepted individually before escalation.

Output: `TRACK_LAUNCH_STAGE_n_ACCEPTED`

## TR-5 Wheel-speed / RPM correlation

Where wheel-speed data is available, correlate:

- engine RPM;
- gear;
- rear-wheel speed;
- front-wheel speed if available;
- calculated expected vehicle speed;
- slip ratio;
- clutch slip indication;
- launch acceleration.

Unexpected divergence shall be classified as tyre slip, clutch slip, sensor error or gearing/model mismatch before using the data for control decisions.

Output: `TR5_SPEED_RPM_CORRELATION_ACCEPTED`

## TR-6 Boost recovery after launch

Evaluate boost during and after clutch release:

- boost at release;
- minimum boost after engagement;
- time to recover to target;
- RPM at recovery;
- wastegate/solenoid command;
- turbo speed if measured;
- AFR/lambda;
- fuel differential pressure.

Do not increase launch boost solely to hide poor clutch/RPM recovery.

Output: `TR6_BOOST_RECOVERY_ACCEPTED`

## TR-7 Electrical stability under launch acceleration

Review:

- B15/PMU voltage;
- battery/charging voltage;
- Pump 1/2 current;
- B39/B40 behaviour;
- PMU current limits/faults;
- CAN stability;
- trigger/sync errors;
- X70/A21 behaviour;
- connector/junction thermal evidence between runs.

Output: `TR7_TRACK_ELECTRICAL_ACCEPTED`

## TR-8 Repeatability

Repeat the same accepted stage without calibration changes where practical.

Compare:

- launch RPM;
- launch boost;
- RPM drop;
- RPM recovery;
- boost recovery;
- 60-foot or equivalent early acceleration metric;
- AFR/lambda;
- fuel pressure;
- wheel slip;
- temperatures;
- electrical faults.

A single excellent launch does not establish repeatability.

Output: `TR8_REPEATABILITY_ACCEPTED`

## TR-9 Extended run / shift validation

Once launch behaviour is stable, validate the transition into subsequent acceleration/shift events under the separately approved dyno/race operating envelope.

Record:

- gear transitions;
- RPM recovery;
- boost recovery;
- AFR/lambda;
- fuel pressure;
- ignition state;
- electrical stability;
- speed/acceleration.

Do not exceed the currently approved boost/RPM envelope.

Output: `TR9_ACCELERATION_TRANSITION_ACCEPTED`

## TR-10 Post-run inspection

After significant launches/runs inspect:

- clutch condition/adjustment;
- drivetrain;
- tyres;
- turbo/exhaust hardware;
- fuel/oil/coolant leaks;
- J-P01/J-P02/B15;
- pump connectors;
- B39/B40;
- X70;
- engine/PMU grounds;
- harness heat/chafe areas;
- connector retention.

Output: `TR10_POST_TRACK_INSPECTION_ACCEPTED`

## TR-11 Final race configuration freeze

Once track behaviour is repeatable, define the race-released configuration:

- FT550 calibration revision;
- PMU revision;
- SparkPRO/dwell configuration;
- launch RPM;
- launch boost;
- maximum Two-Step duration;
- clutch-input/release logic;
- boost strategy after launch;
- fuel;
- RPM limit;
- boost limit;
- protection limits;
- sensor abort thresholds;
- required warm-up/pre-stage conditions;
- remaining restrictions.

Output: `FINAL_RACE_CONFIGURATION_FROZEN`

## TR-12 Final race validation

Final validation requires multiple accepted track passes/runs under the frozen configuration with no unexplained electrical, fuel, ignition, trigger, thermal or launch-control fault.

The required count and performance envelope are project/team-specific and shall be documented rather than assumed.

Output: `FINAL_RACE_VALIDATION_ACCEPTED`

## Abort categories

Abort the launch/run for:

- unintended launch-control activation;
- failure to release launch control;
- uncontrolled wheelspin or instability;
- severe clutch slip or driveline shock;
- unsafe RPM excursion;
- oil/fuel pressure outside approved limits;
- confirmed unsafe AFR/lambda;
- turbo overspeed/EGT violation where measured;
- trigger/sync loss;
- ECU/PMU reset;
- unsafe temperature;
- electrical protection trip/heating;
- mechanical or rider-safety concern.

## Release state

After all applicable TR stages PASS:

`TRACK_LAUNCH_VALIDATED`

and, after frozen-configuration repeatability:

`FINAL_RACE_VALIDATION_ACCEPTED`

This state supports final calibration release and Golden Harness/production closure.
