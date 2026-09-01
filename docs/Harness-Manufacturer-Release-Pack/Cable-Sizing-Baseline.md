# Cable Sizing Baseline – Prototype / RFQ

## Purpose

Provide a practical cable-size baseline for manufacturer quotation and first-prototype material planning while preserving the existing verification gates for load-dependent circuits.

## Sizes that may be treated as project-standard classes

These classes are sufficiently established for RFQ and prototype planning, subject to terminal compatibility:

- 0.35 mm2 / approximately 22 AWG: sensors, 5 V references, sensor returns, PMU command inputs, clutch discrete, FT550 A21 Two-Step request, CAN conductors when using an appropriate twisted-pair cable.
- 0.50 mm2 / approximately 20 AWG: injector low-side command wiring, FT550-to-SparkPRO ignition commands, low-current relay commands and warning-lamp circuits.
- 0.75 mm2 / approximately 18 AWG: FT550 switched supply, boost-control solenoid feed, logger/service power and similar low/medium-current auxiliary feeds.
- 1.00 mm2 / approximately 17-18 AWG equivalent depending wire series: SparkPRO power-ground/driven-coil conductors where required by FuelTech documentation and selected low-current engine power branches.

## Load-dependent prototype planning baselines

The following are **quoting / first-cut baselines, not final electrical release**:

- injector common +12 V: 1.0 mm2 provisional;
- ignition/coil common +12 V: 1.5 mm2 provisional;
- primary fuel pump: 2.0 mm2 provisional;
- charge/intercooler pump: 2.0 mm2 provisional;
- radiator fan: 2.5 mm2 provisional;
- PMU main battery feed: 10 mm2 provisional for a short approximately 0.4 m route.

These circuits remain subject to actual steady-state current, inrush, route length, ambient temperature/loom derating, terminal capability, permitted voltage drop and final protection setting.

The manufacturer shall quote using these provisional sizes but shall not treat them as immutable if measured load evidence requires a larger conductor.

## Grounding

Signal/sensor returns remain 0.35 mm2 where applicable and shall follow the released sensor-ground topology.

Power grounds must be sized to the associated load, not copied from the signal-ground schedule. SparkPRO ground paths use the manufacturer-required 1.0 mm2 class. Pump/fan/load grounds should match the corresponding load-feed engineering class unless a released design specifies otherwise.

PMU pin 25 device ground is a module/electronics ground and does not replace the individual high-current load returns.

## Prototype length allowance

`Prototype-Cable-Size-Length-Schedule.csv` gives approximate installed lengths plus recommended first-cut lengths. First-cut values intentionally include service/trim allowance. They are suitable for RFQ material estimation and a first prototype, not repeat-manufacturing dimension freeze.

After prototype fitment:

1. trim/reroute only through approved workmanship methods;
2. record every final branch length;
3. update the dimensional schedule;
4. promote accepted dimensions to Rev 1 repeat-manufacture values with agreed tolerances.

## Current status

- Low-level cable sizing: **CONFIRMED CLASS**.
- Medium-current ECU/boost/service sizing: **STRONG PROVISIONAL / VERIFY LOAD**.
- High-current pump/fan/main-feed sizing: **PROTOTYPE BASELINE / MEASUREMENT GATED**.
- Approximate physical lengths: **RFQ / PROTOTYPE ESTIMATE**.
- Repeat-manufacturing lengths: **NOT YET FROZEN**.
