# Production Harness Milestone

## Purpose

This milestone converts the Rev 0 HD-style wiring concept into a build-oriented harness definition for the Turbo V-Rod Destroyer using the repository's current baselines:

- FuelTech FT550 as sole engine ECU;
- ECUMASTER PMU-16 as protected power-distribution backbone;
- OEM VRXSE/VRSC engine sensors and identified OEM hardware;
- new motorsport harness, not a re-use of the original race main harness.

## Deliverables

- `Connector-Index.md` — project connector identifiers and functions.
- `Connector-Cavity-Schedule.csv` — cavity-by-cavity termination schedule.
- `Splice-Ground-Reference.md` — splice and ground naming/topology.
- `Harness-Branch-Schedule.csv` — physical branch definition and routing intent.
- `Verification-Register.csv` — all open engineering items that block release.
- `Release-Checklist.md` — production release gate for Rev 1 harness drawings.

## Release philosophy

A project-defined connector ID may be frozen before every manufacturer cavity is known, but no critical conductor may be terminated from a `VERIFY` row. Unknown PMU-16 cavities, FT550 power/ground cavities, injector/ignition outputs, OEM injector/coil connector details, sensor calibration curves and current limits remain explicit blockers.

The purpose of this milestone is to make missing information obvious and bounded. It is not to convert unknowns into assumptions.
