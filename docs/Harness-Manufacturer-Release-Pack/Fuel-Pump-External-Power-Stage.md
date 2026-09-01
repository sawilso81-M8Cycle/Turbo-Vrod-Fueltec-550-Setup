# Fuel Pump External Power Stage – Verified PMU16 Constraint

## Verified constraint

ECUMASTER documents PMU16 O1 (pin 38) and O2 (pin 39) as 25 A maximum high-side outputs. ECUMASTER also states that connector-terminal current capacity must be derated for temperature and adjacent loaded terminals.

The project fuel-pump design basis now allows an individual pump to draw up to approximately 30 A. Therefore a 30 A-capable pump shall not be powered directly from O1 or O2.

## Rev 1 architecture

PMU O1/O2 remain logic/control outputs only for fuel-pump switching.

Recommended power path:

`Battery / protected high-current distribution -> dedicated fuse/protection -> sealed automotive relay or approved solid-state high-current switch -> fuel pump -> dedicated power return/star ground`

Control path:

`PMU O1 or O2 -> relay/SSR control input`

The external switching device must default OFF on loss of PMU command or control power.

## Cable rule

- 2.5 mm² remains the absolute project minimum fuel-pump conductor size.
- For a circuit genuinely designed around 30 A, 4.0 mm² is the recommended production baseline for both feed and dedicated return, subject to actual route length, selected wire series, ambient/loom derating, connector capability and measured voltage drop.
- Do not pass the 30 A pump current through the PMU 39-pin output terminal.

## Switching hardware requirements

Select a sealed automotive relay, contactor or motorsport solid-state power switch with:

- continuous current rating comfortably above the measured pump steady current;
- inrush capability above measured pump peak current;
- suitable 12-14.5 V automotive environment rating;
- sealed connector/terminal system rated for the selected conductor and current;
- suppression compatible with PMU output control;
- fail-OFF behaviour;
- serviceable replacement without cutting the main loom.

A nominal >=40 A automotive relay/SSR class is an initial procurement floor only. Final selection must use the actual pump current/inrush evidence and manufacturer derating data.

## Protection

The external pump power branch requires dedicated short-circuit protection coordinated to the conductor, connector and pump. Protection value is not automatically 30 A merely because the pump may draw 30 A; it must be selected from measured operating/inrush current and the selected fuse/electronic protection time-current behaviour.

## PMU logic retained

PMU still owns:

- prime timing;
- start/run permission;
- kill/master priority;
- CAN/RPM fallback logic;
- warning/fault logic;
- external relay/SSR command.

The PMU no longer carries the full pump load current in this architecture.

## Release status

`FUEL_PUMP_EXTERNAL_POWER_STAGE_REQUIRED`

Closeout requires exact pump model, measured steady/inrush current, relay/SSR selection, fuse/protection selection, connector/terminal selection and installed voltage-drop validation.
