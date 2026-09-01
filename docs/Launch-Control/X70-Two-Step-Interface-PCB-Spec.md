# X70 Two-Step Interface PCB - Manufacturing Specification

## Purpose

X70 converts the ECUMASTER PMU-16 O11 high-side +12 V launch-permissive output into a galvanically simple dry-contact ground request for the FuelTech FT550 A21 / White #2 Two-Step input.

The FT550 input must never be exposed directly to PMU O11 +12 V.

## Functional architecture

```text
PMU O11 / pin 3 ---- J1-1 ----+---- K1 coil +
                              |
                              +---- TP1 O11_CMD

J-P02 power ground --- J1-2 ------- K1 coil - ---- TP2 GND

                       suppression
                    across K1 coil only

FT550 A21 / White #2 -- J1-3 ---- K1 NO contact ----+
                                                     |
J-SIGNAL_GND ---------- J1-4 ---- K1 COM contact ----+

TP3 = FT_A21
TP4 = CONTACT_GND
```

K1 contact closes only when O11 is energised.

Normal states:

- O11 OFF -> K1 released -> FT550 A21 open/high-impedance -> Two-Step request OFF.
- O11 ON -> K1 energised -> FT550 A21 connected to ground -> Two-Step request ON.

## Frozen component baseline

### K1 relay

- Manufacturer: TE Connectivity
- Family: Micro Relay K
- Project baseline: `1393280-5`
- Coil: 12 VDC
- Contact: SPST normally open
- Board mounting: through-hole
- Function: electrical isolation between PMU high-side command and FT550 ground-trigger input

Do not replace K1 with a relay containing an internal suppression diode unless coil polarity and release-time behaviour are revalidated.

## Suppression strategy

### Preferred production approach

Use a **bidirectional TVS across K1 coil**, rather than a plain flyback diode, to suppress the inductive transient while retaining faster relay release.

Reference designator: `D1`

Initial design class:

- bidirectional TVS;
- standoff voltage safely above normal vehicle charging voltage;
- clamp voltage compatible with the PMU O11 output-stage rating;
- pulse capability comfortably exceeding the energy in the ~47 mA relay coil.

**Exact D1 part number remains VERIFY until the permitted PMU O11 inductive-clamp/output transient rating is confirmed.**

Prototype fallback: leave D1 footprint capable of accepting either a bidirectional TVS or a diode/zener network. Do not ship a production board with D1 omitted.

A conventional single flyback diode may be used only for bench comparison; its slower relay release must be measured and accepted before release.

## Connector J1 / X70

Use one keyed sealed 4-way automotive connector.

Pin allocation is frozen:

| Pin | Net | Function |
|---|---|---|
| 1 | O11_CMD | PMU O11 high-side command to K1 coil + |
| 2 | PWR_GND | K1 coil return to J-P02 |
| 3 | FT_A21 | FT550 A21 / White #2 |
| 4 | CONTACT_GND | clean ground source for K1 dry contact |

Connector family selection must support 0.35-0.5 mm2 conductors, automotive temperature/vibration environment, positive latch and environmental sealing.

## Ground segregation

J1-2 is the relay-coil power return and routes to J-P02.

J1-4 is the dry-contact ground used only to pull FT550 A21 low. Keep J1-4 electrically separate from the coil return on the PCB except where the project grounding architecture explicitly joins them outside X70.

Do not allow coil current to flow through the FT550 precision sensor-ground conductor.

## PCB electrical design rules

- 2-layer FR-4 minimum.
- 1.6 mm nominal board thickness unless enclosure dictates otherwise.
- 1 oz copper minimum.
- Through-hole K1 footprint with mechanical solder support on all relay pins.
- Minimum 1.0 mm trace width for relay-coil command/return paths is preferred even though current is low, for robustness.
- FT_A21/contact paths may use 0.5 mm or greater traces.
- Keep relay coil copper physically separated from the FT_A21 dry-contact route where practical.
- No shared copper path between relay-coil return and FT_A21 contact ground before their designated connector pins.
- Add generous annular rings and teardrops for through-hole relay and connector pads where supported.
- Provide test pads TP1-TP4 large enough for hook/probe access.
- Add board identifier, revision and pin-1 marking on silkscreen.
- Add `X70 TWO-STEP INTERFACE` and `A21 GROUND TRIGGER ONLY` on silkscreen.

## Environmental design

The board shall be installed in a sealed or potted enclosure away from direct exhaust/turbo radiant heat.

Preferred protection:

- conformal coating after electrical test;
- sealed connector;
- strain relief on harness exit;
- rigid mounting with vibration isolation where required;
- no unsupported relay mass on a flexible board edge.

Do not pot until the prototype has passed all electrical and thermal tests.

## Mechanical target

Keep the PCB compact enough to mount close to the PMU/ECU electrical area without creating a long FT550 A21 branch.

Initial board envelope target: <= 45 mm x 35 mm excluding harness strain relief.

Final dimensions are layout dependent and shall be frozen in the KiCad manufacturing milestone.

## Design-for-test

Required test points:

- TP1 `O11_CMD`
- TP2 `PWR_GND`
- TP3 `FT_A21`
- TP4 `CONTACT_GND`

Recommended optional points:

- TP5 coil positive after connector input
- TP6 suppression-node probe point

## Electrical acceptance tests

### X70-PCB-001 unpowered continuity

O11_CMD to PWR_GND: no short.

FT_A21 to CONTACT_GND: open with relay unpowered.

Coil and dry-contact domains must show no unintended continuity.

### X70-PCB-002 coil current

At normal vehicle voltage range, measure K1 coil current and compare with relay manufacturer expectations and PMU O11 loading.

### X70-PCB-003 contact operation

Energise J1-1 relative to J1-2.

PASS: J1-3 to J1-4 changes from open to low-resistance closed state.

### X70-PCB-004 release timing

Measure O11 removal to contact opening using an oscilloscope/logic capture.

Record actual release time with production D1 suppression fitted.

Do not infer release timing from relay catalogue data alone.

### X70-PCB-005 transient suppression

Scope K1 coil voltage at turn-off.

PASS: transient remains within the verified PMU O11 output-stage limit and does not couple a damaging or false-trigger transient into FT_A21.

### X70-PCB-006 FT550 isolation

With PMU O11 active, verify FT_A21 is pulled to ground only through K1 contacts and never sees vehicle +12 V.

### X70-PCB-007 failure-open behaviour

Disconnect K1 coil, disconnect O11 command and remove board power in separate tests.

PASS: FT_A21 remains open and Two-Step request cannot assert.

### X70-PCB-008 endurance bench cycle

Cycle K1 repeatedly under representative control conditions while logging contact state and release timing. Any contact sticking or release-time drift blocks release.

## Manufacturing outputs required next

The fabrication package shall eventually contain:

- KiCad schematic;
- KiCad PCB layout;
- Gerber X2 or standard Gerber set;
- Excellon drill files;
- board drawing/dimensions;
- BOM with manufacturer part numbers;
- pick-and-place file for SMD suppression components where applicable;
- assembly drawing;
- test procedure and test-record template.

## Release state

Current state: `X70_PCB_ELECTRICAL_SPEC_FROZEN`

Production state requires:

1. PMU O11 transient/clamp rating verified;
2. exact D1 suppression component frozen;
3. exact J1 connector family frozen;
4. KiCad schematic/ERC complete;
5. PCB layout/DRC complete;
6. prototype build;
7. X70-PCB-001 through X70-PCB-008 PASS.
