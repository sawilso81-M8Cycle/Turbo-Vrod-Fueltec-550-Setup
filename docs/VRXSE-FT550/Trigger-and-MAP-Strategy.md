# Trigger and MAP Strategy

## Crank trigger

The working Harley VRXSE/VRSC cross-reference identifies the crank sensor as part number **32313-01A**, with a two-wire engine-position circuit.

The current FT550 working mapping is:

- Harley CKP signal -> **FT550 A19 RPM+**
- Harley CKP reference -> **FT550 A18 RPM- / VR reference**

FuelTech documentation describes the corresponding VR trigger convention as signal and low-reference inputs. Polarity must still be verified with an oscilloscope during cranking before fuel and ignition are enabled.

## Required crank-trigger commissioning sequence

1. Confirm CKP sensor resistance against service data where applicable.
2. Confirm no continuity from either CKP conductor to unintended chassis earth unless the sensor design specifically requires it.
3. Scope both wires while cranking.
4. Confirm clean waveform amplitude and polarity.
5. Confirm FT550 reports stable cranking RPM.
6. Confirm trigger edge / tooth configuration using FuelTech documentation and timing-light verification.
7. Only then enable ignition and fuel.
8. Lock mechanical timing with a timing light before tuning load or boost.

## Cam-sync status

No OEM cam-position sensor has yet been identified in the reviewed VRXSE parts information or the relevant 2006 engine-control diagrams.

Therefore:

- do **not** assign the FT550 cam-sync input to an assumed wire;
- treat the OEM system as crank-only until proven otherwise;
- configure the initial FT550 strategy accordingly;
- if true sequential phase information is required, design and validate a dedicated cam-sync pickup.

### Future cam-sync option

A future engineered cam-sync system should define:

- physical trigger location;
- one-event-per-cycle geometry;
- sensor technology;
- air gap;
- supply voltage;
- polarity;
- shielding;
- input conditioning;
- failure mode;
- synchronisation window relative to crank position;
- serviceability.

Do not add cam sync solely to fill an unused FT550 pin. It must add reliable phase information.

## MAP strategy for the turbo engine

The OEM Harley MAP sensor is not intended to be assumed suitable as the primary high-boost load sensor without verified range and calibration.

The preferred primary load strategy is the **FT550 internal 7-bar MAP sensor**, using a dedicated pneumatic reference from the intake manifold.

### Recommended plumbing

For individual throttle bodies / runners:

1. take a small pressure reference from each relevant intake runner;
2. combine the references into a small common manifold / pulse-damping chamber where appropriate;
3. run a short, protected hose to the FT550 MAP port;
4. avoid fuel pooling, sharp kinks, heat damage and boost leaks;
5. verify the ECU reads local barometric pressure with the engine off before starting.

### OEM MAP retention

The Harley MAP sensor may be retained as a secondary diagnostic channel if:

- its electrical transfer function is verified;
- its pressure range is verified;
- it does not exceed the intended pressure range under boost;
- the FT550 analogue input used is correctly configured.

It should not be relied upon for engine protection merely because it physically fits the original intake.

## Boost-related protection channels

For a turbo Destroyer, the FT550 strategy should ultimately correlate:

- manifold pressure;
- fuel pressure;
- oil pressure;
- lambda;
- engine coolant temperature;
- intake air temperature;
- RPM;
- throttle position;
- optional EGT front/rear;
- optional turbo oil pressure;
- optional wastegate dome pressure.

Protection logic should be designed around verified sensor data rather than a single boost-limit value.
