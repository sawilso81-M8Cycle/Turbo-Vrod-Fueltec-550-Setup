# FT550 <-> PMU-16 CAN Backbone Freeze

## Milestone objective

Freeze the production CAN communications spine between the FuelTech FT550 and ECUMASTER PMU-16.

## Manufacturer constraints

FuelTech FTCAN 2.0 uses CAN 2.0B extended frames at **1 Mbps**.

ECUMASTER PMU-16 provides two CAN 2.0 A/B interfaces. CAN2 supports 125 / 250 / 500 / 1000 kbps and includes software-controlled termination. CAN1 is fixed at 1 Mbps and has no internal termination.

## Project bus selection

The project shall use:

- **FT550 CAN A**
  - A15 = CAN LOW
  - A16 = CAN HIGH
- **PMU-16 CAN2**
  - pin 37 = CAN2 LOW
  - pin 24 = CAN2 HIGH
- Bus speed = **1 Mbps**

This selection leaves PMU CAN1 free for future ECUMASTER-native equipment and keeps FT550 CAN B reserved for future expansion.

## Physical topology

Use a linear trunk. Do not create a star network.

Recommended order:

`FT550 -> service/CAN junction X51 -> PMU-16 CAN2`

The service branch from X51 to a diagnostic adapter must be a short stub. At 1 Mbps keep the service stub as short as practical and target <= 0.3 m.

All CAN wiring shall use a 120-ohm characteristic-impedance twisted pair suitable for motorsport/automotive service.

## Termination

The bus shall have exactly two 120-ohm terminations, one at each physical end of the trunk.

### PMU end

Use the PMU-16 CAN2 software-controlled termination only if the PMU is physically located at one end of the bus. For the baseline architecture the PMU is treated as one physical end, so CAN2 termination shall be **ENABLED** in PMU Client.

### FT550 end

FuelTech requires a CAN terminator on its CAN network. Install the FuelTech CAN terminator at the FT550 end of the trunk.

Do not install an additional termination at X51 or on a service adapter when both end resistors are already present.

## Service connector X51

X51 is the CAN service junction and shall expose at minimum:

1. CAN HIGH
2. CAN LOW
3. chassis/power ground reference for diagnostic equipment
4. protected service +12 V only if the selected diagnostic adapter requires it

X51 must not contain a permanent 120-ohm termination.

A temporary diagnostic tool that contains switchable termination must have that termination disabled during normal connection to the completed vehicle bus.

## Signal mapping

| Source | Function | Destination |
|---|---|---|
| FT550 A16 | CAN A HIGH | PMU pin 24 CAN2 HIGH |
| FT550 A15 | CAN A LOW | PMU pin 37 CAN2 LOW |
| X51-H | service CAN HIGH tap | trunk only |
| X51-L | service CAN LOW tap | trunk only |

## Communication strategy

The physical layer is frozen at 1 Mbps. Application-level traffic is not assumed to be natively compatible simply because both devices share the bus.

PMU Client shall be configured to receive only the specific FT550 CAN frames/signals required for PMU logic. Where a FuelTech signal is not available in a directly usable form, use a verified custom CAN definition rather than inferring IDs/scaling.

Critical PMU outputs shall not depend exclusively on unverified CAN data. Loss-of-CAN behaviour must be explicitly defined per function.

Examples:

- fuel pump control: local PMU fallback / hard enable strategy required;
- fan control: safe local fallback permitted;
- warning/logging channels: may fail passive;
- engine torque or shutdown requests: require validated fail-safe logic.

## CAN-loss safety rule

Every CAN-dependent PMU function must define:

- signal timeout;
- plausibility check;
- fallback state;
- recovery behaviour;
- logged fault flag.

Loss of the FT550-PMU CAN link must not create an uncontrolled engine-running state or silently disable a required cooling/fuel protection function.

## Commissioning tests

1. With power off, measure approximately 60 ohms between CAN H and CAN L with both end terminations active.
2. Verify no third terminator is present.
3. Confirm FT550 and PMU CAN2 are both configured for 1 Mbps.
4. Confirm CAN2 termination enabled at PMU baseline end.
5. Power system and verify no persistent CAN error counters.
6. Validate each consumed PMU signal against the FT550 displayed/logged value.
7. Disconnect CAN deliberately and verify every defined fallback state.
8. Reconnect and verify deterministic recovery.

## Release state

Physical bus selection: **FROZEN**.

Bitrate: **FROZEN at 1 Mbps**.

Termination architecture: **FROZEN**.

Service junction architecture: **FROZEN**.

Still open:

- exact X51 connector family/terminal PNs;
- final physical trunk/stub lengths after module placement;
- application-layer FT550 CAN frame IDs/scaling used by PMU logic;
- per-function CAN-loss fallback validation.
