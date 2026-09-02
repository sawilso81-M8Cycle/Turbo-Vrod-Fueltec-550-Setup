# Two-Step / Clutch Launch Control Commissioning Pack

## Purpose

Define the controlled commissioning of the Turbo V-Rod clutch-triggered Two-Step / launch-control system after normal dyno load commissioning and controlled boost operation have been validated.

Architecture baseline:

`Clutch / launch request -> PMU16 logic -> PMU O11 -> X70 relay coil -> isolated dry contact -> FT550 A21`

The FT550 A21 side shall remain electrically isolated from +12 V. X70 is the galvanic/function boundary between the PMU output domain and FT550 launch input.

Two-Step combustion testing creates substantial exhaust, turbo, valvetrain and driveline thermal/mechanical stress. It is therefore commissioned separately from ordinary boost tuning.

## Entry conditions

Do not begin combustion-based Two-Step testing unless:

- `DYNO_LOAD_COMMISSIONING_ACCEPTED` is PASS;
- `CONTROLLED_BOOST_OPERATION_RELEASED` is current;
- X70/A21 dead-engine truth-table testing previously passed;
- clutch switch/sensor hardware is mechanically secure and electrically verified;
- FT550 A21 input logic is verified against the exact FT550 configuration/manual evidence;
- PMU O11 logic/configuration is version controlled;
- engine RPM, TPS, MAP/boost, lambda/AFR, fuel pressure and oil pressure are logged;
- engine/coolant and IAT monitoring are valid;
- EGT is logged if installed and validated;
- turbo speed is logged if installed and validated;
- boost-control configuration is known;
- launch test area/dyno arrangement is appropriate and motorcycle restraint is suitable;
- emergency shutdown is immediately available.

## Safety principle

Commission the chain in layers:

1. clutch input only;
2. PMU logic only;
3. X70/A21 electrical transition with engine off;
4. running engine at low-risk conditions;
5. short Two-Step events at conservative RPM;
6. progressive launch-RPM/boost development;
7. launch-release transition validation.

Never begin with a long full-throttle limiter event.

## TS-0 Configuration freeze

Record before testing:

- FT550 calibration revision;
- PMU configuration revision;
- clutch input channel/polarity;
- PMU O11 logic;
- X70 relay/contact configuration;
- FT550 A21 function/polarity;
- Two-Step RPM target;
- activation TPS condition if used;
- activation vehicle-speed condition if used;
- gear/neutral conditions if used;
- maximum activation time;
- ignition retard/cut strategy;
- fuel cut/addition strategy if applicable;
- boost-control state during launch;
- launch boost ceiling;
- release/debounce/delay settings;
- fail-safe state.

Output: `TS0_CONFIGURATION_ACCEPTED`

## TS-1 Clutch input truth table

Engine off.

Verify physical clutch states against the PMU input:

- clutch released;
- clutch fully pulled;
- transition/debounce;
- connector disconnected;
- short/open fault response where safely testable.

The selected fail state must not unexpectedly command Two-Step.

Output: `TS1_CLUTCH_INPUT_ACCEPTED`

## TS-2 PMU O11 / X70 / A21 truth table

Engine off.

For every relevant clutch/enable state verify:

- PMU launch logic result;
- O11 command;
- X70 coil state;
- X70 contact state;
- FT550 A21 state;
- +12 V isolation from A21 contact side.

Output: `TS2_ELECTRICAL_CHAIN_ACCEPTED`

## TS-3 Running-engine non-event validation

Run the engine without intentionally entering Two-Step.

Verify:

- normal clutch use does not trigger launch control outside the defined enable conditions;
- A21 does not chatter;
- RPM signal remains stable;
- no PMU output fault occurs;
- X70 remains thermally/electrically normal.

Output: `TS3_NON_EVENT_BEHAVIOUR_ACCEPTED`

## TS-4 Conservative first Two-Step event

Use a deliberately conservative launch RPM and the shortest practical activation duration needed to validate function.

Record:

- target RPM;
- achieved RPM;
- TPS;
- MAP/boost;
- lambda/AFR;
- fuel pressure;
- oil pressure;
- ignition command/cut state;
- activation duration;
- EGT if fitted;
- turbo speed if fitted;
- engine/IAT temperature;
- trigger/sync state;
- PMU faults.

Stop and inspect after the first successful event.

Output: `TS4_FIRST_EVENT_ACCEPTED`

## TS-5 Progressive launch RPM stages

Increase launch RPM only in predefined stages.

Each stage must define before activation:

- target RPM;
- maximum permitted RPM deviation/overshoot;
- maximum activation duration;
- TPS range;
- boost ceiling;
- AFR/lambda envelope;
- fuel-pressure requirement;
- oil-pressure requirement;
- EGT ceiling if measured;
- turbo-speed ceiling if measured;
- temperature ceilings;
- abort criteria.

Each stage is separately accepted before the next is unlocked.

Output: `LAUNCH_RPM_STAGE_n_ACCEPTED`

## TS-6 Launch boost development

Only after stable RPM-control behaviour.

Develop boost-at-launch progressively rather than maximizing it immediately.

For each stage record:

- Two-Step RPM;
- activation duration;
- MAP/boost build rate;
- peak launch boost;
- wastegate/boost-control command;
- turbo speed if measured;
- EGT if measured;
- AFR/lambda;
- fuel-pressure differential;
- injector duty;
- temperatures.

The exact launch-boost ceiling shall be determined from verified engine/turbo/driveline limits and track requirements.

Output: `LAUNCH_BOOST_STAGE_n_ACCEPTED`

## TS-7 Clutch release / launch exit validation

The release transition is as important as limiter operation.

Verify:

- clutch release removes the launch request predictably;
- PMU O11 transitions correctly;
- X70 releases correctly;
- FT550 A21 changes state correctly;
- no input chatter/retrigger occurs;
- engine transitions from launch strategy to normal calibration cleanly;
- boost-control transition is controlled;
- no unexpected RPM flare or cut persists.

If speed/gear/TPS conditions participate in release logic, verify them independently and together.

Output: `TS7_RELEASE_TRANSITION_ACCEPTED`

## TS-8 Maximum activation-time fail-safe

Two-Step shall not be allowed to remain active indefinitely because a clutch switch, relay or operator state persists.

Verify the configured maximum activation-time strategy and its recovery/re-arm behaviour.

The timeout value is configuration-specific and shall be approved from engine/turbo thermal evidence, not guessed generically.

Output: `TS8_TIMEOUT_FAILSAFE_ACCEPTED`

## TS-9 Fault-state validation

Validate safe behaviour for credible faults where practical without damaging hardware:

- clutch input open/disconnected;
- clutch input implausible/stuck state;
- X70 coil not energising;
- PMU O11 fault/disabled state;
- A21 state inconsistent with command;
- CAN information unavailable where CAN is used by enable logic;
- low voltage/reset condition recovery.

No single ordinary fault should silently create an uncontrolled permanent Two-Step request.

Output: `TS9_FAULT_STATE_ACCEPTED`

## TS-10 Thermal recovery / inspection

Between events inspect and allow recovery appropriate to the hardware.

Monitor/inspect:

- exhaust/turbo temperature;
- turbo oiling;
- SparkPRO/coils;
- B39/B40 paths;
- injectors;
- X70 relay/socket;
- clutch switch/wiring;
- harness near exhaust/turbo;
- PMU faults;
- plugs/engine evidence where required by tuner.

Do not stack limiter events simply to accelerate commissioning.

Output: `TS10_THERMAL_REPEATABILITY_ACCEPTED`

## Abort categories

Immediately release/abort Two-Step and shut down where appropriate for:

- uncontrolled RPM/limiter overshoot;
- failure to release on clutch transition;
- unexpected A21 activation;
- fuel/oil pressure outside approved limits;
- confirmed unsafe AFR/lambda;
- excessive EGT where measured;
- turbo overspeed where measured;
- trigger/sync loss;
- ECU/PMU reset;
- unsafe temperature;
- abnormal mechanical/turbo noise;
- fuel/oil/coolant leak;
- electrical overheating/protection trip;
- driveline/dyno restraint concern.

Numeric thresholds are configuration-specific and belong in the stage register.

## Release state

After TS-0 through applicable TS-10 PASS:

`TWO_STEP_LAUNCH_CONTROL_COMMISSIONED`

The released launch envelope shall separately record maximum approved:

- Two-Step RPM;
- activation duration;
- launch boost;
- RPM/boost operating conditions;
- calibration revision;
- fuel;
- thermal restrictions;
- re-arm/release logic.

This does not by itself equal final race validation.

## Next gate

Proceed to `Track-Launch-and-Final-Race-Validation-Pack`, then final calibration and Golden Harness qualification.
