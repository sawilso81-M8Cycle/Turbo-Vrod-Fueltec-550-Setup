# Two-Step Component Freeze

## Scope

Freeze the physical component baseline for the clutch-triggered Two-Step subsystem.

## FT550 input

- FT550 connector X01 cavity A21 / White #2 = `FT_TWO_STEP_REQUEST`.
- FuelTech documents this input as ground-activated.
- Therefore PMU O11 high-side output must not connect directly to A21.

## X70 interface baseline

Production baseline: galvanically simple dry-contact interface using a 12 V automotive relay.

- Relay family: TE Connectivity Micro Relay K.
- Baseline part: **1393280-5**.
- Function: SPST-NO dry contact.
- Coil: 12 VDC.
- PMU O11 energises the relay coil.
- Relay NO contact pulls FT550 A21 to clean ground.
- Inactive state leaves A21 open/high-impedance.

This interface is intentionally simple and easy to diagnose. It prevents PMU O11 +12 V from being applied to the ground-triggered FT550 input.

### X70 wiring

- X70-1 = PMU O11 / pin 3 -> relay coil +
- X70-2 = relay coil - -> J-P02 power ground
- X70-3 = FT550 A21 / White #2
- X70-4 = signal ground used by relay NO contact

Contact state:

- O11 OFF -> A21 open -> Two-Step request inactive
- O11 ON -> A21 connected to ground -> Two-Step request active

Final relay socket/PCB carrier and suppression strategy must be verified before harness release. If an integral-suppression relay variant is substituted, polarity must be observed.

## Primary clutch switch

Primary hard discrete input remains OEM Harley clutch switch **71620-08**.

- PMU A6 / pin 18 = `CLUTCH_DISCRETE`.
- Use PMU software pull-up/pull-down configuration only after physical switch polarity is measured.
- The OEM switch is the authoritative discrete interlock for launch permission.

Harley service parts evidence also identifies the clutch-switch spring clip **46865-06** for the VRXSE-family arrangement.

## X71 connector policy

X71 = OEM clutch-switch service connector.

Exact mating housing/terminal part number remains physical-identification gated because the accessible Harley parts information identifies the switch but does not expose a standalone mating connector kit for 71620-08.

Preferred release method:

1. retain the OEM left-hand switch harness/connector where serviceable; or
2. identify the installed connector family by inspection and freeze the housing, terminals, seals and cavity lock before crimp release.

No generic two-pin connector substitution is allowed without confirming sealing, terminal current rating, retention and handlebar-motion strain relief.

## Optional clutch-position sensor

Development/race baseline: **Honeywell RTY050LVNAX** Hall-effect rotary position sensor.

Manufacturer characteristics used by this project:

- non-contact Hall-effect rotary sensing;
- 50 degree total sensing range (plus/minus 25 degrees);
- 5 VDC supply;
- ratiometric nominal output approximately 0.5 V to 4.5 V;
- North American pinout style;
- integral shaft without lever.

Allocation:

- PMU +5 V output -> sensor Vcc
- J-SIM/PMU sensor ground -> sensor ground
- PMU A7 / pin 32 -> sensor output

The RTY050LVNAX is a baseline only until the physical clutch-lever arc is measured. If lever rotation cannot be mapped cleanly into the 50-degree range, select another RTY range using the same evidence process rather than mechanically over-travelling the sensor.

## X72 connector

X72 = clutch-position sensor connector.

Use the connector/pinout specified for the selected Honeywell RTY variant. Final harness release requires the actual sensor connector and terminal kit to be populated in the BOM.

## Electrical hierarchy

Two-Step launch authority remains:

`OEM clutch switch -> PMU A6 -> PMU safety logic -> PMU O11 -> X70 dry-contact ground switch -> FT550 A21 -> FT550 Two-Step`

Optional A7 position sensing adds plausibility and launch-analysis capability but does not replace A6 as the hard clutch state.

## Release status

- FT550 input cavity: FROZEN
- PMU A6/A7/O11 cavities: FROZEN
- X70 functional topology: FROZEN
- X70 baseline relay: FROZEN TE 1393280-5
- OEM clutch switch: FROZEN 71620-08
- Optional position sensor baseline: FROZEN Honeywell RTY050LVNAX, subject to physical travel validation
- X71 mating connector: OPEN PHYSICAL IDENTIFICATION
- X72 exact connector kit: VERIFY AGAINST PURCHASED SENSOR
