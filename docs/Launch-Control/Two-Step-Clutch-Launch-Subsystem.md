# Two-Step Clutch Launch Subsystem

## Purpose

Add a dedicated clutch-triggered Two-Step / launch subsystem to the Turbo V-Rod Destroyer FT550 + ECUMASTER PMU-16 architecture.

The subsystem is intentionally separated from the normal engine rev limiter and from boost control. The FT550 performs the actual Two-Step rev-limiter strategy; the PMU-16 owns launch permissives, clutch state, safety interlocks and the hardwired Two-Step request.

## Official FuelTech behaviour used by this design

FuelTech's FT450/FT550/FT550LITE/FT600 manual provides a dedicated 2-step rev limiter and documents the clutch-button strategy. On the PROBIKE harness, **FT550 connector A cavity A21 / White input #2** is the dedicated **2-Step / clutch switch** input.

FuelTech's electrical diagram shows the 2-Step/Clutch input is **ground activated**: the switch closes the White input to battery negative/chassis.

Therefore **PMU O11 MUST NOT be connected directly to FT550 A21** because O11 is a high-side +12 V output. A low-side/open-drain interface is mandatory between O11 and A21.

## Hardware architecture

### OEM clutch discrete input

Primary discrete clutch hardware is the OEM VRXSE clutch switch:

- Harley-Davidson **71620-08 — SWITCH, clutch — VRXSE**;
- Harley-Davidson **46865-06 — clutch switch spring clip**.

The OEM switch is used as the authoritative launch-interlock state, subject to bench continuity/polarity confirmation before wiring release.

### PMU input allocation

- **PMU A6 / pin 18** = `CLUTCH_DISCRETE`
- **PMU A7 / pin 32** = `CLUTCH_POSITION` optional analogue position sensor

A6 is the authoritative hard launch-interlock input.

A6 shall be implemented as a 0-5 V discrete circuit. Until internal-pullup behaviour is proven for the installed PMU project, use an external pull-up to the PMU 5 V reference and let the clutch switch pull A6 toward PMU ground. Final pull-up resistance and switch polarity are bench-test gated.

A7 is recommended for development/race logging because it allows bite-point and release-rate analysis. A7 does not replace the hard A6 safety state until the analogue sensor and plausibility logic have been independently validated.

### PMU output allocation

- **PMU O11 / pin 3** = `TWO_STEP_REQUEST_HIGH_SIDE`

O11 drives only the control side of the Two-Step low-side interface module X70.

### X70 low-side interface

X70 converts the PMU O11 high-side request into the ground-active signal required by FT550 A21.

Required interface behaviour:

- O11 OFF -> X70 output high impedance -> FT550 A21 inactive;
- O11 ON -> X70 pulls FT550 A21 to clean ECU/signal ground -> Two-Step request active;
- loss of PMU power, interface power or command -> A21 returns inactive/high impedance;
- interface must not source +12 V into A21;
- interface switching/release delay must be characterised during bench validation;
- use an automotive-rated protected solid-state low-side/open-drain stage in the production build; exact semiconductor/module PN remains a component-selection gate.

A mechanical relay may be used only for temporary bench proving, not as the production baseline, unless latency/bounce/endurance are explicitly validated and accepted.

### FT550 input allocation — FROZEN

- **FT550 X01/A21 / White #2** = `FT_TWO_STEP_REQUEST`
- Function = dedicated `2-Step / clutch switch` input
- Electrical activation = **pull to ground**

This cavity is now frozen and does not displace MAP, oil pressure, fuel pressure, TPS, ECT, IAT, VSS, gear or expansion inputs.

### Optional clutch-position sensor

Preferred final race architecture:

- non-contact Hall-effect rotary or short-stroke linear position sensor;
- 5 V supply from PMU +5 V pin 15 if current budget permits;
- PMU ground/reference return;
- analogue signal to PMU A7 pin 32;
- nominal ratiometric output compatible with the PMU 0-5 V input range;
- mechanically independent from the discrete switch;
- environmental sealing and strain relief suitable for steering movement, vibration and clutch-lever operation.

Exact sensor model is **mechanical-mock-up gated**. The project shall freeze the sensor only after confirming stroke/angle, mounting, connector clearance and full lever travel without side loading.

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

O11 = ON, X70 pulls A21 to ground, and FT550 confirms/behaves as configured Two-Step.

FT550 owns launch RPM target, ignition-cut strategy, launch ignition retard, launch fuel enrichment, optional electronic-throttle limit and internal 2-step rejection rules.

PMU continues monitoring clutch, kill/master, gear, speed, CAN validity and faults.

### TS-STATE-4 LAUNCH_RELEASE

Detected on validated clutch release / clutch-position transition.

Immediately remove O11 request unless the final FT550 clutch-button workflow explicitly requires a different release sequencing proven during validation.

Launch event timestamp is latched for logging and time-based launch functions.

### TS-STATE-5 POST_LAUNCH_LOCKOUT

Two-Step is blocked from re-arming while the bike is in a launched/run state.

Re-arm requires the defined reset conditions such as low speed, clutch reset, explicit launch re-arm and absence of critical faults.

## PMU Two-Step permissive

`TWO_STEP_PERMISSIVE = LAUNCH_ARMED AND MASTER_OK AND KILL_OK AND CLUTCH_DISCRETE AND GEAR_VALID AND SPEED_ARM_OK AND RPM_ARM_OK AND TPS_ARM_OK AND FAULT_FREE AND POST_LAUNCH_LOCKOUT_FALSE`

`O11 = TWO_STEP_PERMISSIVE`

Every signal used to increase launch authority must have an explicit validity flag. Invalid gear, speed, clutch, RPM or launch-arm state makes O11 OFF.

## Clutch signal plausibility

Where A7 clutch position is fitted, compare A6 and A7. A clutch plausibility fault disarms Two-Step.

## Debounce and timing

The build-specific PMU project shall define and record clutch-switch debounce, launch-arm debounce, minimum active time, launch-release confirmation, maximum Two-Step dwell, post-launch lockout and re-arm conditions. Do not use copied timing values without vehicle test evidence.

## Launch RPM and boost interaction

Launch RPM remains a calibration variable in FT550 and must remain independently lower than the normal engine rev limiter.

Two-Step activation does not automatically grant full boost authority. Launch boost retains its own permissive and validated limit.

## Safety precedence

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

Minimum channels: `LAUNCH_ARMED`, `CLUTCH_DISCRETE`, `CLUTCH_POSITION`, `CLUTCH_POSITION_VALID`, `CLUTCH_PLAUSIBILITY_FAULT`, `TWO_STEP_PERMISSIVE`, `TWO_STEP_REQUEST_O11`, FT550 Two-Step active status where available, RPM, TPS, MAP, gear, vehicle/front/rear wheel speed, launch event timestamp, lockout, boost target/duty, lambda front/rear, fuel pressure and oil pressure.

## Release states

`TWO_STEP_CLUTCH_NOT_VALIDATED` -> `TWO_STEP_CLUTCH_BENCH_VALIDATED` -> `TWO_STEP_CLUTCH_STATIC_VALIDATED` -> `TWO_STEP_CLUTCH_TRACK_VALIDATED`

Only the final state may be included in a competition-release manifest.

## Remaining hardware gates

- X70 exact automotive protected low-side interface component/module;
- OEM 71620-08 switch continuity/polarity and physical connector/terminal identification;
- optional clutch-position sensor exact model and calibration;
- final wire lengths and sealed service connector hardware;
- bench verification of A6 pull-up value and X70 activation/release timing.
