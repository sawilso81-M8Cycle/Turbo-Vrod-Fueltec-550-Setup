# ECUMASTER PMU Client Receive Configuration

## Objective

Translate the frozen FTCAN 2.0 frame map into a PMU Client implementation specification with explicit value variables, validity variables, timeout handling, plausibility checks and fallback behaviour.

## Bus

- PMU interface: CAN2
- Bitrate: 1 Mbps
- FT550 source: CAN A via X51 backbone
- Physical topology: linear FT550 -> X51 -> PMU-16
- PMU CAN2 termination: enabled at PMU end
- Service connector X51: no permanent termination

## Frame sources

Use the live-captured FT550 arbitration IDs corresponding to FTCAN MessageIDs 0x600, 0x601 and 0x602. Working unique-ID-0 examples are 0x14080600, 0x14080601 and 0x14080602, but production PMU configuration must use the actual IDs captured from the installed FT550.

## Receive channels

### Frame 0x600 family

Create these PMU Client receive channels:

| PMU variable | Bytes | Type | Scale | Offset | Unit | Timeout |
|---|---:|---|---:|---:|---|---:|
| FT_TPS | 0-1 | signed 16-bit BE | 0.1 | 0 | % | 250 ms |
| FT_MAP_BAR | 2-3 | signed 16-bit BE | 0.001 | 0 | bar | 250 ms |
| FT_IAT_C | 4-5 | signed 16-bit BE | 0.1 | 0 | C | 1000 ms |
| FT_ECT_C | 6-7 | signed 16-bit BE | 0.1 | 0 | C | 1000 ms |

### Frame 0x601 family

| PMU variable | Bytes | Type | Scale | Offset | Unit | Timeout |
|---|---:|---|---:|---:|---|---:|
| FT_OILP_BAR | 0-1 | signed 16-bit BE | 0.001 | 0 | bar | 250 ms |
| FT_FUELP_BAR | 2-3 | signed 16-bit BE | 0.001 | 0 | bar | 250 ms |
| FT_WATERP_BAR | 4-5 | signed 16-bit BE | 0.001 | 0 | bar | 1000 ms |
| FT_GEAR_RAW | 6-7 | signed 16-bit BE | protocol encoding | 0 | raw | 1000 ms |

### Frame 0x602 family

| PMU variable | Bytes | Type | Scale | Offset | Unit | Timeout |
|---|---:|---|---:|---:|---|---:|
| FT_LAMBDA | 0-1 | signed 16-bit BE | 0.001 | 0 | lambda | 250 ms |
| FT_RPM | 2-3 | signed 16-bit BE | 1 | 0 | rpm | 250 ms |
| FT_OILT_C | 4-5 | signed 16-bit BE | verify public protocol scaling | 0 | C | 1000 ms |
| FT_PITLIMIT_RAW | 6-7 | signed 16-bit BE | protocol encoding | 0 | raw | 1000 ms |

## Validity variables

For every receive channel used by control logic, create a separate boolean validity variable. Minimum set:

- FT_RPM_VALID
- FT_TPS_VALID
- FT_MAP_VALID
- FT_IAT_VALID
- FT_ECT_VALID
- FT_OILP_VALID
- FT_FUELP_VALID
- FT_GEAR_VALID
- FT_LAMBDA_VALID
- FT_BATTV_VALID

Validity is TRUE only when:

1. the expected source frame has been received within its timeout;
2. the decoded value is within the plausibility range below;
3. no protocol/source-ID mismatch is present.

## Plausibility ranges

Initial PMU-side sanity checks:

| Signal | Minimum | Maximum | Invalid action |
|---|---:|---:|---|
| RPM | 0 | 12000 rpm | mark invalid |
| TPS | -1 | 101 % | mark invalid |
| MAP | -1.2 | 7.0 bar | mark invalid |
| IAT | -40 | 180 C | mark invalid |
| ECT | -40 | 180 C | mark invalid |
| Oil pressure | -0.2 | 15 bar | mark invalid |
| Fuel pressure | -0.2 | 15 bar | mark invalid |
| Lambda | 0.5 | 2.0 | mark invalid |
| Battery voltage | 6 | 18 V | mark invalid |

These are PMU plausibility limits, not calibration limits.

## Derived state variables

### ENGINE_RUNNING

Initial rule:

`ENGINE_RUNNING = FT_RPM_VALID && FT_RPM > 400`

Do not use this as the sole fuel-pump safety path. Hardwired master/start inputs remain authoritative.

### ENGINE_CRANKING

Suggested initial rule:

`ENGINE_CRANKING = FT_RPM_VALID && FT_RPM > 0 && FT_RPM <= 400`

### CAN_FT550_HEALTHY

TRUE only if all critical channels currently required by active PMU logic are valid. Do not require optional channels such as gear or lambda if their associated function is disabled.

## Fallback rules

- RPM timeout: ENGINE_RUNNING becomes FALSE/UNKNOWN; pump continuation falls back to hardwired-safe logic.
- TPS timeout: disable TPS-based auxiliary enhancements.
- MAP timeout: disable boost-dependent auxiliary enhancements and select minimum-boost strategy where PMU has authority.
- ECT timeout: command conservative fan strategy rather than fan off.
- Fuel-pressure timeout: mark pressure unknown; do not infer healthy pressure.
- Oil-pressure timeout: mark pressure unknown; do not infer healthy pressure.
- Gear timeout: disable gear-based logic.
- Battery-voltage timeout: use PMU-local supply measurement if configured.

## Tagged battery-voltage channel

Battery voltage is not in simple frame 0x600-0x602. Implement tagged FTCAN MeasureID 0x0012 only after confirming the exact tagged frame layout/source arbitration ID on the installed FT550.

Target variable:

`FT_BATTV = raw * 0.01 V`

Keep FT_BATTV_VALID independent of simple-frame validity.

## PMU Client implementation sequence

1. Configure CAN2 at 1 Mbps.
2. Enter the live-captured FT550 arbitration IDs for 0x600-0x602.
3. Create the receive channels exactly as above.
4. Create timeout/validity variables.
5. Add plausibility checks.
6. Add ENGINE_RUNNING / ENGINE_CRANKING / CAN_FT550_HEALTHY derived variables.
7. Bind PMU output logic only to `value && VALID`, never value alone.
8. Add tagged battery voltage after live capture confirms its source frame.
9. Bench-test stale-frame behaviour by stopping each source frame independently where possible.
10. Perform full CAN-disconnect fault test per V067.

## Release state

Receive-channel definition: FROZEN.

Live arbitration IDs: CAPTURE GATED.

PMU Client project file: NOT YET BUILT IN SOFTWARE.

CAN-loss validation: TEST REQUIRED.
