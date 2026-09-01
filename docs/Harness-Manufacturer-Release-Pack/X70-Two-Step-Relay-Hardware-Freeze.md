# X70 Two-Step Relay Hardware Freeze – Rev 1

## Purpose

Close the physical relay implementation for the clutch-triggered Two-Step request while continuing to bypass the custom X70 PCB.

## Functional requirement

PMU16 O11 is a high-side +12 V output. FT550 A21 / White #2 is a ground-active Two-Step input. They shall never be connected directly.

Production function:

`PMU O11 -> 12 V relay coil -> isolated NO dry contact -> FT550 A21 to approved ground`

Truth table:

- O11 OFF: relay de-energised, A21 open, Two-Step request OFF.
- O11 ON: relay energised, NO contact closes A21 to ground, Two-Step request ON.
- PMU power lost: relay de-energises, A21 opens, Two-Step request OFF.
- relay removed/open-circuit: A21 remains open, Two-Step request OFF.

## Selected relay baseline

Primary relay baseline: **TE Connectivity Micro Relay A, PN 1393292-5 / V23074A1001A402**.

Verified characteristics from TE:

- automotive plug-in/socket-mount relay;
- 12 VDC coil;
- 1 Form A / SPST-NO contact;
- 25 A contact rating, with 30 A limiting continuous-current data;
- coil resistance approximately 119 ohm;
- coil power approximately 1.42 W;
- integrated resistor suppression version per TE Micro Relay A product coding;
- operating temperature approximately -40 °C to +125 °C;
- quick-connect terminals.

This application switches only the low-current FT550 input-to-ground request, so contact-current capability is far above the functional requirement.

## Suppression strategy

Use the resistor-suppressed relay variant. Do not add an external flyback diode across the coil unless engineering revises the design.

Reason:

- resistor suppression reduces inductive kick without the long release delay associated with a simple freewheel diode;
- fast release is desirable at clutch launch transition;
- duplicate suppression components can alter relay release behaviour and are not to be added casually.

Measured relay release time remains an acceptance test rather than being assumed from generic relay data.

## Socket / holder strategy

Use a standard Micro-ISO socket/holder mechanically compatible with TE Micro Relay A quick-connect blade layout.

The socket assembly shall:

- retain the relay positively under motorcycle vibration;
- be mounted in a sealed relay enclosure or weather-protected electronics area;
- use genuine automotive female terminals sized to the actual 0.35/0.50 mm² conductors;
- provide strain relief so terminal retention is not carrying harness loads;
- allow relay replacement without cutting the loom;
- be keyed/labelled as `X70 TWO-STEP RELAY`;
- prevent accidental interchange with a differently wired relay position where possible.

The exact socket-carrier PN may be selected by the harness manufacturer from a traceable Micro-ISO automotive relay-holder system, but must be recorded in the final build BOM and approved at DFM. A loose unretained relay with individual push-on terminals is not acceptable.

## Circuit allocation

- Coil positive: PMU O11, circuit `2STEP-CMD`, 0.50 mm².
- Coil negative: approved power/control ground, 0.50 mm².
- Contact common: approved ground, 0.35 mm² minimum.
- Contact NO: FT550 A21 / White #2, circuit `2STEP-REQ`, 0.35 mm².

No +12 V conductor is permitted on the A21 contact side.

## Mounting

Preferred location:

- close enough to PMU/FT550 to keep B43/B44 short;
- away from direct exhaust/turbo radiant heat;
- away from standing water/spray path;
- service-accessible without removing the main engine harness;
- oriented and retained so vibration cannot walk the relay out of the holder.

Existing prototype length baselines remain:

- B43 PMU O11 -> X70: approximately 450 mm installed / 550 mm first cut;
- B44 X70 -> FT550 A21: approximately 350 mm installed / 450 mm first cut.

Final dimensions remain bike-measurement gated.

## Bench acceptance

Before installation:

1. verify coil resistance and record ambient temperature;
2. energise from a representative 12-14.5 V supply;
3. verify NO contact closes only when coil is energised;
4. verify A21-side circuit is isolated from +12 V at all times;
5. measure O11/relay coil current;
6. measure contact resistance closed;
7. measure release time after command removal;
8. cycle at least 100 operations during prototype validation with no sticking/intermittency;
9. verify relay removal produces Two-Step OFF state;
10. verify kill/master removal causes prompt Two-Step request release.

## Release state

**X70_RELAY_FUNCTION_AND_RELAY_PN_FROZEN**

**X70_SOCKET_CARRIER_PN_DFM_GATED**

BG-008 may be considered functionally closed once the final harness-builder socket/holder PN is recorded and the powered truth-table test passes.
