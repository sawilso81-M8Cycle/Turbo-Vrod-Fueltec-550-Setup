# Sheet 07 - Two-Step Clutch Launch

## Functional schematic

```text
                         OEM CLUTCH SWITCH 71620-08
                         (authoritative discrete state)
                                  |
                                  | B41
                                  v
                         X71 CLUTCH SWITCH SERVICE
                                  |
                                  v
                       PMU-16 A6 / PIN 18
                       CLUTCH_DISCRETE
                                  |
                                  |  PMU launch permissive logic
                                  v
                       PMU-16 O11 / PIN 3
                       TWO_STEP_REQUEST
                                  |
                                  | B42  +12 V high-side command
                                  v
                    +-----------------------------+
                    | X70 TWO-STEP INTERFACE      |
                    | TE MICRO RELAY K 1393280-5 |
                    |                             |
PMU O11 ----------->| coil +                      |
J-P02 GND ----------| coil -                      |
                    |                             |
FT550 A21 ----------| NO contact                  |
SIGNAL GND ---------| common contact              |
                    +-----------------------------+
                                  |
                                  | contact closes to ground
                                  v
                    FT550 X01 A21 / WHITE #2
                    FT_TWO_STEP_REQUEST
                                  |
                                  v
                    FT550 2-STEP / LAUNCH LIMITER

OPTIONAL CLUTCH POSITION:

PMU +5 V -----------+
                    |
                    v
              X72 HONEYWELL RTY050LVNAX
              5 V HALL ROTARY SENSOR
                    |
                    +------ signal ------> PMU A7 / PIN 32
                    |
SENSOR GND ---------+
```

## Circuit schedule

| Circuit | From | To | Function | Initial wire class | Status |
|---|---|---|---|---|---|
| B41 | X71 OEM clutch switch | PMU A6 pin 18 | clutch discrete state | 0.35 mm2 | polarity test required |
| B42 | PMU O11 pin 3 | X70 relay coil + | Two-Step interlocked command | 0.35-0.5 mm2 | frozen function |
| B43 | X70 relay contact | FT550 A21 White #2 | ground-active Two-Step request | 0.35 mm2 | frozen function |
| B44 | X72 Hall sensor | PMU A7 pin 32 | clutch position analogue signal | 0.35 mm2 | optional / calibration gated |

## X70 cavity schedule

| Cavity | Connection | Function |
|---|---|---|
| 1 | PMU O11 pin 3 | relay coil positive |
| 2 | J-P02 ground | relay coil return |
| 3 | FT550 A21 White #2 | switched Two-Step input |
| 4 | signal/power reference ground | dry-contact ground source |

## X71 clutch switch

X71 retains the OEM Harley clutch-switch connector system wherever practical. Primary switch part number: 71620-08. Exact mating connector/terminal kit must be identified from the installed switch harness before a replacement connector is crimped.

## X72 clutch position

Optional sensor baseline: Honeywell RTY050LVNAX, 5 V Hall-effect rotary position sensor. Verify actual clutch-lever travel falls inside the sensor operating range before final bracket manufacture.

## Safety truth table

| Launch arm | Kill/master healthy | Clutch A6 | Required signals valid | O11 | FT550 A21 | Two-Step |
|---|---|---|---|---|---|---|
| 0 | X | X | X | OFF | open | OFF |
| 1 | 0 | X | X | OFF | open | OFF |
| 1 | 1 | 0 | 1 | OFF | open | OFF |
| 1 | 1 | 1 | 0 | OFF | open | OFF |
| 1 | 1 | 1 | 1 | ON | grounded via X70 | PERMITTED |

## Failure behaviour

- O11 power loss: relay releases; FT550 A21 becomes open; Two-Step request OFF.
- X70 relay coil open: request cannot activate.
- X70 contact open: request cannot activate.
- A6 invalid: PMU request OFF.
- A7 invalid: position-based refinement disabled; A6 remains authoritative if independently valid.
- Kill/master event: O11 OFF immediately.

## Validation before track use

1. Prove A6 polarity and debounce statically.
2. Verify O11 never applies +12 V to FT550 A21.
3. Measure X70 operate/release timing and ensure release is fast enough for launch transition.
4. Confirm A21 is open when O11 is OFF and near ground only when O11 is ON.
5. Verify kill/master removal releases X70 regardless of software launch state.
6. Calibrate A7 pulled/bite/released regions if the Hall sensor is fitted.
7. Perform stationary Two-Step validation before any launch test.
