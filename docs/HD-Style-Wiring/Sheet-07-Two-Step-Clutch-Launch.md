# Sheet 07 - Two-Step Clutch Launch

## Functional schematic

```text
                         OEM CLUTCH SWITCH 71620-08
                         (authoritative discrete state)
                                  |
                                  | B41
                                  v
                     X71 DTM 2-WAY SERVICE BREAK
                       DTM04-2P / DTM06-2S
                                  |
                                  v
                       PMU-16 A6 / PIN 18
                       CLUTCH_DISCRETE
                                  |
                                  | PMU launch permissive logic
                                  v
                       PMU-16 O11 / PIN 3
                       TWO_STEP_REQUEST
                                  |
                                  | B42 +12 V high-side command
                                  v
                    +--------------------------------+
                    | X70 TWO-STEP INTERFACE PCB    |
                    | K1 TE 1393280-5               |
                    | Micro Relay K, 12 V, SPST-NO  |
                    |                                |
PMU O11 ----------->| K1 coil +                     |
J-P02 GND ----------| K1 coil -                     |
                    | D1 bidirectional TVS /        |
                    | verified suppression network  |
                    | across relay coil             |
                    |                                |
FT550 A21 ----------| K1 NO contact                 |
CONTACT GND --------| K1 contact common             |
                    +--------------------------------+
                                  |
                                  | contact closes to ground
                                  v
                    FT550 X01 A21 / WHITE #2
                    FT_TWO_STEP_REQUEST
                                  |
                                  v
                    FT550 2-STEP / LAUNCH LIMITER

OPTIONAL CLUTCH POSITION:

PMU +5 V pin 15 ----+--------------------> X72 pin 1 Vcc
PMU reference GND --+--------------------> X72 pin 2 GND
X72 pin 3 OUTPUT ------------------------> PMU A7 / pin 32

X72 SENSOR: HONEYWELL RTY050LVNAX
NORTH AMERICAN PINOUT
```

## Circuit schedule

| Circuit | From | To | Function | Initial wire class | Status |
|---|---|---|---|---|---|
| B41 | OEM clutch switch via X71 | PMU A6 pin 18 | clutch discrete state | 0.35-0.5 mm2 | production service-break architecture frozen |
| B42 | PMU O11 pin 3 | X70 K1 coil + | Two-Step interlocked command | 0.35-0.5 mm2 | frozen function |
| B43 | X70 K1 dry contact | FT550 A21 White #2 | ground-active Two-Step request | 0.35 mm2 | frozen function |
| B44 | X72 Hall sensor pin 3 | PMU A7 pin 32 | clutch position analogue signal | 0.35 mm2 | optional / calibration gated |

## X70 production interface

K1: TE Connectivity 1393280-5, Micro Relay K, 12 VDC coil, SPST-NO, PCB through-hole.

X70 is a small sealed/pottable manufactured interface PCB, not a loose relay/socket assembly.

| X70 cavity | Connection | Function |
|---|---|---|
| 1 | PMU O11 pin 3 | K1 coil positive |
| 2 | J-P02 ground | K1 coil return |
| 3 | FT550 A21 White #2 | switched Two-Step input |
| 4 | contact ground | dry-contact ground source |

Suppression is fitted only across the relay coil. Production preference is a bidirectional TVS or verified diode/zener network that limits the O11 turn-off transient while preserving rapid relay release. Exact D1 is frozen only after PMU O11 transient/clamp compatibility is verified.

Do not use a plain flyback diode as the production default without measured acceptance of its increased release time.

The PCB includes TP1 O11_CMD, TP2 PWR_GND, TP3 FT_A21 and TP4 CONTACT_GND.

Full PCB requirements and tests are defined in `docs/Launch-Control/X70-Two-Step-Interface-PCB-Spec.md` and `docs/Launch-Control/X70-PCB-Bench-Test-Record.csv`.

## X71 clutch switch service break

The OEM switch remains Harley 71620-08. Because the accessible Harley parts data does not expose a standalone switch-body mating connector service kit, preserve the OEM pigtail and place X71 downstream as the new harness service break.

Production connector family:

- DTM04-2P receptacle;
- DTM06-2S plug;
- size-20 contacts to suit final conductor;
- TE 0462-201-20141 nickel solid socket contact is acceptable for 0.2-0.5 mm2 where the socket side requires that contact;
- matching DTM size-20 pin contact, wedgelocks and seals to suit final housing/wire.

## X72 clutch position

Optional sensor: Honeywell RTY050LVNAX.

North American pinout:

| Pin | Function | Project connection |
|---|---|---|
| 1 | Vcc | PMU +5 V pin 15 |
| 2 | GND | PMU reference ground |
| 3 | Output | PMU A7 pin 32 |

Nominal output is approximately 0.5 V to 4.5 V ratiometric over the configured 50 degree sensing range. Verify actual lever geometry before manufacturing the sensor bracket.

## Safety truth table

| Launch arm | Kill/master healthy | Clutch A6 | Required signals valid | O11 | FT550 A21 | Two-Step |
|---|---|---|---|---|---|---|
| 0 | X | X | X | OFF | open | OFF |
| 1 | 0 | X | X | OFF | open | OFF |
| 1 | 1 | 0 | 1 | OFF | open | OFF |
| 1 | 1 | 1 | 0 | OFF | open | OFF |
| 1 | 1 | 1 | 1 | ON | grounded via X70 | PERMITTED |

## Failure behaviour

- O11 power loss: K1 releases; FT550 A21 becomes open; Two-Step request OFF.
- X70 relay coil open: request cannot activate.
- X70 contact open: request cannot activate.
- D1/suppression open: suppression is lost but the dry contact still fails open; board is not release-eligible until repaired.
- D1/suppression short: O11 should current-limit/fault and K1 cannot energise; Two-Step remains OFF.
- A6 invalid: PMU request OFF.
- A7 invalid: position refinement disabled; A6 remains authoritative if independently valid.
- Kill/master event: O11 OFF immediately.

## Validation before track use

1. Prove A6 polarity and debounce statically.
2. Verify O11 never applies +12 V to FT550 A21.
3. Complete X70-PCB-001 through X70-PCB-008 on the assembled interface PCB.
4. Measure X70 contact release timing with the actual production suppression component fitted.
5. Confirm A21 is open when O11 is OFF and near ground only when O11 is ON.
6. Verify kill/master removal releases X70 regardless of software launch state.
7. Verify X71 retention/sealing and full-lock handlebar strain relief.
8. Calibrate A7 pulled/bite/released regions if the Hall sensor is fitted.
9. Perform stationary Two-Step validation before any launch test.

## Production release

See `docs/Launch-Control/Two-Step-Production-Loom-Release.md`.

The X70 design state is `X70_PCB_ELECTRICAL_SPEC_FROZEN` until the KiCad schematic/layout and prototype validation gates are complete.

The loom state remains `TWO_STEP_CLUTCH_NOT_VALIDATED` until all production and functional tests pass.
