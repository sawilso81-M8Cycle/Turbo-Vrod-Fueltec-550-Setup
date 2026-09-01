# Two-Step Production Loom Release

## Purpose

Move the clutch-triggered Two-Step subsystem from electrically frozen to production-loom ready.

## X70 production interface

The TE Connectivity Micro Relay K 1393280-5 remains the frozen relay element.

Manufacturer / distributor data confirms:

- 12 VDC coil;
- approximately 47.2 mA coil current;
- approximately 254 ohm coil resistance;
- SPST-NO dry contact;
- approximately 3 ms operate and 1.5 ms release time;
- through-hole PCB termination;
- -40 C to +105 C operating range.

Because 1393280-5 is a PCB relay rather than a socketed blade relay, the production release shall use a small dedicated sealed X70 interface PCB rather than an improvised relay socket.

### X70 PCB functional requirements

- relay K1 = TE 1393280-5;
- D1 flyback suppression diode across K1 coil;
- diode orientation: cathode toward PMU O11 / coil positive, anode toward J-P02 ground;
- 4-way sealed external harness connector;
- conformal coating or potted enclosure;
- strain-relieved mounting away from turbo/exhaust radiant heat;
- test pads for O11 command, A21 switched node and ground;
- inactive state must leave FT550 A21 open/high impedance;
- no +12 V may appear on the FT550 A21 contact circuit.

The exact PCB layout may change without changing electrical architecture, provided these requirements remain true.

## X71 OEM clutch switch strategy

Primary switch remains Harley 71620-08.

Accessible Harley parts information identifies the clutch switch kit but does not expose a dedicated standalone mating connector service kit for the switch itself. Therefore the production baseline is:

1. retain the OEM switch/pigtail connection where present;
2. create a service break downstream of the OEM pigtail using a sealed two-way TE Connectivity DEUTSCH DTM connector;
3. do not cut the switch body leads shorter than necessary for serviceability.

### X71 service-break connector baseline

- harness receptacle: DTM04-2P;
- mating plug: DTM06-2S;
- size-20 contacts selected to suit the final 0.35-0.5 mm2 wire;
- preferred nickel solid socket contact for 0.2-0.5 mm2 range: TE 0462-201-20141 where applicable;
- corresponding matching pin contact to be selected from the DTM size-20 family for the same conductor class;
- wedgelocks and cavity seals per selected DTM housings.

This DTM connector is a service break in the new harness. It is not represented as the original Harley switch-body connector.

## X72 Hall sensor pinout

Optional Honeywell RTY050LVNAX uses the North American pinout style:

- pin 1 = Vcc 5 V;
- pin 2 = ground;
- pin 3 = analogue output;

Project allocation:

- X72-1 -> PMU +5 V pin 15;
- X72-2 -> PMU sensor/device reference ground per final PMU sensor-ground plan;
- X72-3 -> PMU A7 pin 32.

Sensor output is nominally ratiometric across approximately 0.5 V to 4.5 V over the selected mechanical sensing range.

The sensor remains optional until actual clutch lever travel is measured and proven to fit the 50 degree total range.

## Branch freeze

- B41 = OEM clutch switch / X71 service break -> PMU A6 pin 18.
- B42 = PMU O11 pin 3 -> X70 K1 coil positive.
- B43 = X70 dry contact -> FT550 X01 A21 White #2 ground-active Two-Step request.
- B44 = X72 Hall output -> PMU A7 pin 32.

## Release tests

Production-loom release requires all of the following:

1. X70 PCB continuity/insulation test.
2. Verify D1 polarity before power.
3. Verify O11 OFF leaves A21 electrically open.
4. Verify O11 ON grounds A21 through dry contact only.
5. Measure that A21 never sees PMU +12 V.
6. Verify relay release on kill/master removal.
7. Measure relay operate/release timing on assembled X70.
8. Verify X71 service connector retention, sealing and handlebar full-lock strain relief.
9. Verify A6 switch polarity and PMU threshold/debounce.
10. If X72 fitted, verify 5 V / ground / signal pinout and full mechanical travel without end-stop overtravel.
11. Verify A6/A7 plausibility logic.
12. Complete stationary FT550 Two-Step function test before track launch testing.

## Release state

`TWO_STEP_LOOM_PRODUCTION_READY` may be assigned only after the X70 PCB, X71 service break, harness continuity and release tests are complete.
