# Turbo V-Rod Destroyer HD-Style Wiring Package

## Scope

This folder defines the new wiring package for a turbo Harley-Davidson VRXSE V-Rod Destroyer using:

- FuelTech FT550 as the engine-management ECU;
- ECUMASTER PMU-16 as the electronically protected power-distribution module;
- original Harley-Davidson / VRXSE / common VRSC sensors and associated OEM engine hardware wherever identified in this repository;
- additional turbo protection/development sensors defined in the Sensor Expansion package;
- a completely new motorsport harness rather than reuse of the original race ECM/main harness architecture.

The drawing style follows Harley-Davidson service-diagram conventions at a project level: circuit sheets, connector identifiers, wire-colour codes, splices, grounds, power feeds and cross-sheet references. It does not reproduce Harley copyrighted drawings.

## Design baseline

The VRXSE engine sensor harness cross-reference in this repository identifies common sensor hardware including CKP 32313-01A, TPS 27975-01, MAP 32416-10, ECT 32315-01, IAT 27388-01, VSS 74402-05B, oil-pressure switch 26561-99 and neutral switch 33902-98A.

The FT550 remains the sole engine ECU. The PMU-16 provides protected high-side power distribution and current monitoring. Precision sensor supply/returns remain isolated from high-current load returns.

## Sheet set

- [Sheet 01 - Master Power and Grounds](Sheet-01-Master-Power-and-Grounds.md)
- [Sheet 02 - OEM Sensors to FT550](Sheet-02-OEM-Sensors-to-FT550.md)
- [Sheet 03 - Injection and Ignition](Sheet-03-Injection-and-Ignition.md)
- [Sheet 04 - PMU16 Power Distribution](Sheet-04-PMU16-Power-Distribution.md)
- [Sheet 05 - Start, Kill, Cooling and Auxiliaries](Sheet-05-Start-Kill-Cooling-Aux.md)
- [Sheet 06 - Turbo Instrumentation](Sheet-06-Turbo-Instrumentation.md)
- [Sheet 07 - Engine Protection Logic](Sheet-07-Engine-Protection-Logic.md)
- [Master Wire and Connector Schedule](Master-Wire-and-Connector-Schedule.csv)
- [Sensor Expansion Package](../Sensor-Expansion/README.md)

## Drawing status legend

- **VERIFIED** - supported by information already recorded in this repository.
- **DESIGN** - project-defined new-harness convention.
- **VERIFY** - must be checked against the exact physical component/manual before termination or energisation.
- **DNP** - do not populate/use.

## Non-negotiable rules

1. Do not join FT550 sensor ground to PMU load ground downstream of the intended battery/engine reference point.
2. CKP wiring must be twisted/shielded and routed away from coils, starter, PMU power outputs and pump/fan wiring.
3. OEM and added precision analogue sensors use the FT550 sensor-reference network where compatible, not the PMU +5 V output by convenience.
4. PMU-16 CAN may be used for status/logic, but engine-critical functions must have defined safe behaviour if CAN is lost.
5. Exact PMU current limits, wire gauges, FT550 injector/ignition output cavities and added-sensor input allocations remain `VERIFY` until precise installed hardware and current manual data are confirmed.
6. Mandatory protection channels take priority over development-only sensors if FT550 input capacity is constrained.
7. No `VERIFY` item may remain on a released production harness drawing.
