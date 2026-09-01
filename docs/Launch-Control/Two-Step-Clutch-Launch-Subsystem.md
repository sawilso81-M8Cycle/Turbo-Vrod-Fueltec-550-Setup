# Two-Step Clutch Launch Subsystem

## Purpose

Add a dedicated clutch-triggered Two-Step / launch subsystem to the Turbo V-Rod Destroyer FT550 + ECUMASTER PMU-16 architecture.

The subsystem is intentionally separated from the normal engine rev limiter and from boost control. The FT550 performs the actual Two-Step rev-limiter strategy; the PMU-16 owns launch permissives, clutch state, safety interlocks and the hardwired Two-Step request.

## Official FuelTech behaviour used by this design

FuelTech's FT450/FT550/FT550LITE/FT600 manual provides a dedicated 2-step rev limiter with programmable ignition retard, fuel enrichment, maximum electronic-throttle position, minimum TPS for launch corrections, activation by button or input sensor, and post-launch rejection logic. FuelTech also documents a clutch-button strategy where the clutch input marks the actual launch event after the 2-step has been armed.

The master repository shall preserve the distinction between:

- normal rev limiter;
- Two-Step launch limiter;
- optional staging/3-step functions;
- boost-control strategy.

## Hardware architecture

### PMU input allocation

- **PMU A6** = `CLUTCH_DISCRETE`
- **PMU A7** = `CLUTCH_POSITION` optional analogue position sensor

A6 is the authoritative hard launch-interlock input.

A7 is recommended for development/race logging because it allows bite-point and release-rate analysis. A7 does not replace the hard A6 safety state until the analogue sensor and plausibility logic have been independently validated.

### PMU output allocation

- **PMU O11** = `TWO_STEP_REQUEST_TO_FT550`

O11 shall drive a dedicated FT550 white digital input configured for positive/switched-12-V activation, subject to final confirmation of the selected FT550 white input cavity and electrical interface.

If the final FT550 white-input configuration requires ground activation instead, insert an approved low-side/open-drain interface stage. Do not assume polarity at harness build without verification.

### FT550 input allocation

Reserve one otherwise-unused FT550 White input as:

`FT_TWO_STEP_REQUEST`

Exact connector cavity remains **VERIFY** until reconciled against the final project FT550 input map. Do not displace MAP, oil pressure, fuel pressure, IAT, gear or other already-reserved project channels without an explicit revision.

### Optional clutch-position sensor

Preferred final race architecture:

- mechanically independent clutch-position sensor;
- 5 V supply from a verified sensor-reference source;
- precision sensor return;
- analogue signal to PMU A7;
- environmental sealing and strain relief suitable for clutch-lever vibration and steering movement.

The position sensor is primarily for state estimation/logging:

- fully pulled;
- pre-bite;
- bite region;
- release transition;
- fully released.

## Launch state machine

### TS-STATE-0 DISARMED

Two-Step request OFF.

Entry occurs on power-up, kill, master-off, invalid required signal, timeout, launch completion or explicit disarm.

### TS-STATE-1 ARMED_WAIT_CLUTCH

Launch system deliberately armed but Two-Step request remains OFF until all prerequisites are valid.

### TS-STATE-2 CLUTCH_HELD_READY

Required conditions are simultaneously true:

- launch armed;
- master/run healthy;
- kill healthy;
- clutch discrete ACTIVE;
- valid gear condition;
- vehicle/wheel speed below build-specific arming threshold;
- TPS above configured minimum where applicable;
- RPM below normal engine limit and inside launch arming window;
- no critical PMU/ECU fault;
- MAP/boost state inside permitted staging region;
- Two-Step rejection timer not active.

PMU O11 may become active in this state.

### TS-STATE-3 TWO_STEP_ACTIVE

O11 = ON and FT550 confirms/behaves as configured Two-Step.

FT550 owns:

- launch RPM target;
- ignition-cut strategy;
- launch ignition retard;
- launch fuel enrichment;
- optional electronic-throttle limit;
- internal 2-step rejection rules.

PMU continues monitoring clutch, kill/master, gear, speed, CAN validity and faults.

### TS-STATE-4 LAUNCH_RELEASE

Detected on validated clutch release / clutch-position transition.

Immediately remove O11 Two-Step request unless the final FT550 clutch-button workflow explicitly requires a different release sequencing proven during validation.

Launch event timestamp is latched for logging and time-based launch functions.

### TS-STATE-5 POST_LAUNCH_LOCKOUT

Two-Step is blocked from re-arming while the bike is in a launched/run state.

Re-arm requires the defined reset conditions such as low speed, clutch reset, explicit launch re-arm and absence of critical faults.

## PMU Two-Step permissive

Conceptual logic:

`TWO_STEP_PERMISSIVE = LAUNCH_ARMED AND MASTER_OK AND KILL_OK AND CLUTCH_DISCRETE AND GEAR_VALID AND SPEED_ARM_OK AND RPM_ARM_OK AND TPS_ARM_OK AND FAULT_FREE AND POST_LAUNCH_LOCKOUT_FALSE`

`O11 = TWO_STEP_PERMISSIVE`

Every signal used to increase launch authority must have an explicit validity flag.

Invalid gear, speed, clutch, RPM or launch-arm state must make O11 OFF.

## Clutch signal plausibility

Where A7 clutch position is fitted, compare A6 and A7.

Examples:

- A6 says clutch pulled but A7 reports released region for longer than debounce tolerance -> `CLUTCH_PLAUSIBILITY_FAULT`.
- A6 says released while A7 remains fully pulled -> fault.
- A7 out-of-range/open/short -> position invalid; A6 remains authoritative if independently healthy.

A clutch plausibility fault disarms Two-Step.

## Debounce and timing

The build-specific PMU project shall define and record:

- clutch switch debounce;
- launch-arm debounce;
- minimum active time before Two-Step request;
- launch-release transition confirmation;
- maximum Two-Step dwell time;
- post-launch lockout time/state;
- re-arm conditions.

Do not use generic copied timing values without vehicle test evidence.

## Launch RPM

Launch RPM is a calibration variable in FT550 and shall be incremented only under the Launch & Track validation process.

The first clutch Two-Step validation shall use the lowest practical controlled launch RPM that safely demonstrates function.

Launch RPM must remain independently lower than the normal engine rev limiter.

## Boost interaction

Two-Step activation does not automatically grant full boost authority.

Launch boost requires its own permissive and validated limit.

Recommended authority chain:

`TWO_STEP_ACTIVE` -> may permit only the currently validated staging/launch boost target.

Any loss of clutch/gear/speed/CAN/MAP validity must reduce boost authority and de-energise the boost-control path as defined by the existing fail-safe architecture.

## Safety precedence

Highest priority to lowest:

1. hardwired kill;
2. master/run disable;
3. critical PMU/ECU protection;
4. clutch/gear/speed validity;
5. post-launch lockout;
6. launch arm;
7. Two-Step request;
8. launch boost enhancement.

Two-Step must never defeat the normal engine rev limiter.

## Logging channels

Minimum channels:

- `LAUNCH_ARMED`
- `CLUTCH_DISCRETE`
- `CLUTCH_POSITION`
- `CLUTCH_POSITION_VALID`
- `CLUTCH_PLAUSIBILITY_FAULT`
- `TWO_STEP_PERMISSIVE`
- `TWO_STEP_REQUEST_O11`
- FT550 Two-Step active status where available
- RPM
- TPS
- MAP
- gear
- vehicle speed / front and rear wheel speed where available
- launch event timestamp
- post-launch lockout
- boost target
- boost duty
- lambda front/rear
- fuel pressure
- oil pressure

## Release states

Initial state: `TWO_STEP_CLUTCH_NOT_VALIDATED`

Progression:

`TWO_STEP_CLUTCH_NOT_VALIDATED`
-> `TWO_STEP_CLUTCH_BENCH_VALIDATED`
-> `TWO_STEP_CLUTCH_STATIC_VALIDATED`
-> `TWO_STEP_CLUTCH_TRACK_VALIDATED`

Only the final state may be included in a competition-release manifest.

## Open hardware gates

- exact FT550 white-input connector cavity for `FT_TWO_STEP_REQUEST`;
- final O11-to-FT550 electrical polarity/interface confirmation;
- clutch discrete switch hardware and connector;
- optional clutch-position sensor model and calibration;
- final A6/A7 terminal assignments in the harness schedule;
- final wire sizes/connector hardware.
