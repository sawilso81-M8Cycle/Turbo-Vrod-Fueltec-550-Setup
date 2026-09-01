# EPM Driver and Injector Interface Architecture

## Purpose

Freeze the engine-critical driver/interface architecture between the FuelTech FT550 and the retained VRXSE engine hardware without prematurely hard-coding unknown injector or coil electrical values.

## Ignition architecture - frozen

The retained Harley 32477-01A plug-top coils are treated by this project as passive two-terminal coils. They are not to be connected directly to FT550 ignition outputs.

Final command path:

- FT550 A8 / Gray #1 / Ignition output #1 -> external two-channel ignition driver channel 1 -> front 32477-01A coil.
- FT550 A9 / Gray #2 / Ignition output #2 -> external two-channel ignition driver channel 2 -> rear 32477-01A coil.

Preferred hardware class: FuelTech SparkPRO or equivalent FuelTech-approved two-channel-capable passive-coil igniter arrangement.

The exact driver model, dwell table, current limit and thermal installation remain gated by HC-010/HC-011 coil electrical characterization.

## Injector architecture - serviceable dual-mode

The Harley 27772-06 injectors remain the baseline. FT550 outputs are frozen as:

- A1 / Blue #1 / Injection output #1 -> front injector control path.
- A2 / Blue #2 / Injection output #2 -> rear injector control path.

Because OEM injector impedance/current class has not yet been proven, the EPM harness shall include an injector interface service junction that supports both approved configurations:

### Mode A - direct drive

FT550 A1/A2 pass through the service junction directly to the corresponding injectors when measured injector impedance/current is compatible with FuelTech direct-drive requirements.

### Mode B - Peak & Hold

FT550 A1/A2 route from the service junction to a FuelTech-compatible Peak & Hold driver, then from that driver to the injectors when the measured injector electrical class requires it.

No permanent splice shall be used where it would prevent later installation/removal of the Peak & Hold module.

## New project connector IDs

- X60 - ignition driver ECU-side connector or service disconnect.
- X61 - ignition driver coil-side connector.
- X62 - injector interface ECU-side service junction.
- X63 - injector interface engine-side service junction.
- X64 - optional Peak & Hold module input connector.
- X65 - optional Peak & Hold module output connector.

Exact connector families remain `VERIFY` until current, conductor size, environmental rating and packaging are frozen.

## New branch IDs

- B32 - FT550 ignition command branch, A8/A9 to X60.
- B33 - ignition driver power/ground branch.
- B34 - ignition driver output branch, X61 to front/rear coils.
- B35 - FT550 injector command branch, A1/A2 to X62.
- B36 - direct injector bypass link, X62 to X63, fitted only in approved direct-drive mode.
- B37 - Peak & Hold input branch, X62 to X64, DNP until required.
- B38 - Peak & Hold output branch, X65 to X63, DNP until required.
- B39 - injector common +12 V EPM feed.
- B40 - ignition coil common +12 V EPM feed.

## Power-domain rules

Ignition driver, injector +12 V and coil +12 V remain inside the EPM domain. Their high-current grounds and returns shall not share the FT550 precision sensor-return network.

The ignition driver ground shall terminate at the engine/power star J-P02 using the manufacturer-required conductor size and shortest practical low-impedance path.

## Configuration interlock

A harness build record must state exactly one injector mode:

- `DIRECT_DRIVE_APPROVED`, or
- `PEAK_HOLD_INSTALLED`.

A build must never be released with both B36 and B37/B38 simultaneously populated.

## Release gates

Before energisation:

1. HC-008 and HC-009 must close injector impedance/current class.
2. HC-010 and HC-011 must close coil resistance/current-ramp/dwell evidence.
3. Exact ignition-driver hardware must be frozen.
4. Exact Peak & Hold hardware must be frozen if required.
5. X60-X65 connector families and terminal part numbers must be frozen.
6. B33/B34/B39/B40 conductor sizes and protection must be calculated from measured current and route length.
