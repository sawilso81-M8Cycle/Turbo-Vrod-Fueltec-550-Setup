# Two-Step Physical I/O & Hardware Freeze

## Milestone outcome

This milestone freezes the physical control path for clutch-triggered Two-Step while preserving release gates around the low-side interface component, clutch-switch electrical polarity, and optional clutch-position sensor.

## Frozen physical map

### OEM clutch discrete

- Harley-Davidson VRXSE clutch switch: **71620-08**
- Spring clip: **46865-06**
- Harness connector ID: **X71**
- PMU input: **A6 / pin 18**
- Project signal: `CLUTCH_DISCRETE`

The switch is the authoritative discrete launch interlock.

### Optional clutch position

- Harness connector ID: **X72**
- PMU input: **A7 / pin 32**
- Supply: PMU +5 V / pin 15 if current budget permits
- Signal: ratiometric 0-5 V compatible Hall position sensor
- Project signal: `CLUTCH_POSITION`

Exact sensor PN remains gated by lever travel and mounting mock-up.

### Two-Step request

- PMU output: **O11 / pin 3**
- Project output: `TWO_STEP_REQUEST_HIGH_SIDE`
- Interface: **X70 protected solid-state low-side/open-drain stage**
- FT550 connector: **X01 / A21 / White #2**
- FT550 function: `2-Step / clutch switch`
- FT550 activation: **ground active**

The electrical chain is:

`PMU O11 high-side -> X70 control -> X70 low-side/open-drain output -> FT550 A21 White #2`

Direct PMU O11 to A21 wiring is prohibited.

## A6 discrete circuit baseline

Until the installed PMU input configuration is proven to provide a suitable internal pull-up, use a controlled external pull-up from PMU +5 V to A6. The OEM clutch switch then pulls A6 toward PMU ground.

Bench validation shall freeze:

- released-state voltage;
- pulled-state voltage;
- switch continuity/polarity;
- pull-up resistor value;
- debounce;
- open-circuit behaviour;
- short-to-ground behaviour.

Invalid/open clutch state must prevent Two-Step arming.

## X70 production requirements

The production X70 device shall be automotive/race-harness suitable and shall:

- accept the PMU O11 high-side control signal;
- pull FT550 A21 to ground only when commanded;
- remain high impedance when inactive or unpowered;
- prevent +12 V backfeed into the FT550 White input;
- tolerate vehicle transients appropriate to the installation;
- have switching latency and release latency proven against launch requirements;
- use a clean ground/reference topology compatible with the FT550 input circuit;
- be serviceable and identifiable in the harness.

Exact X70 component PN is not guessed in this milestone. It is a release gate requiring datasheet review and bench validation.

## Harness additions

- **B41** X71 OEM clutch switch -> PMU A6
- **B42** optional X72 clutch position -> PMU A7
- **B43** PMU O11 -> X70 control
- **B44** X70 low-side output -> FT550 A21

All are low-current branches. Provisional conductor class is 0.35 mm2 / 22 AWG subject to final terminal and connector compatibility.

## Required bench tests before production release

1. Verify OEM 71620-08 switch polarity and repeatability through full lever travel.
2. Verify A6 voltages and debounce with the selected pull-up.
3. Verify X70 cannot source positive voltage into FT550 A21.
4. Measure O11-command-to-A21-low latency.
5. Measure O11-off-to-A21-high-impedance release latency.
6. Power-cycle PMU/X70 while confirming A21 stays inactive.
7. Open A6 circuit and confirm Two-Step remains disarmed.
8. Short A6 signal to ground and prove the remaining launch permissives still prevent unintended Two-Step activation.
9. Command kill/master-off during active bench Two-Step request and prove O11/X70 release.
10. If A7 is fitted, validate A6/A7 plausibility throughout clutch travel.

## Release state

Physical cavity architecture: **FROZEN**.

OEM clutch switch: **FROZEN**.

FT550 A21 function/polarity: **FROZEN FROM FUELTECH DOCUMENTATION**.

X70 exact component: **OPEN**.

X71 mating connector/terminals: **OPEN**.

Optional A7 position sensor: **OPEN / DNP until selected**.

Two-Step competition release remains blocked until the dedicated Two-Step test and verification registers are passed.
