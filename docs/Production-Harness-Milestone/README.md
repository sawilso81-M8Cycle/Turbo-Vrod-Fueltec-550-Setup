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
- `Wire-Size-Schedule.csv` — circuit-by-circuit provisional/final conductor classes and measurement gates.
- `Rev1-Harness-BOM.csv` — Rev 1 manufacturing BOM framework with frozen versus release-blocking selections.
- `Terminal-Selection-Gate.md` — terminal/conductor compatibility and release rules.
- `Verification-Register.csv` — all open engineering items that block release.
- `Release-Checklist.md` — production release gate for Rev 1 harness drawings.

## Current state

The PMU-16 pin-level map and key FT550 protection cavities are now frozen. The harness has advanced into the wire-size and BOM phase.

Low-level design classes are provisionally established for sensor, command, CAN and selected auxiliary circuits. High-current PMU outputs, PMU main feed, injector supplies and ignition-coil supplies remain measurement-gated because final conductor size must be based on the actual load, inrush, route length, voltage-drop target, heat zone and terminal capability.

The exact PMU Sicma/FCI terminal part numbers remain open until conductor sizes are frozen and the terminal table is present in repository-readable form.

## Release philosophy

A project-defined connector ID and provisional conductor class may be frozen before every terminal part number and physical length is known, but no critical conductor may be manufactured from a `VERIFY` or `MEASUREMENT GATED` row.

The purpose of this milestone is to make missing information obvious and bounded. It is not to convert unknowns into assumptions.
