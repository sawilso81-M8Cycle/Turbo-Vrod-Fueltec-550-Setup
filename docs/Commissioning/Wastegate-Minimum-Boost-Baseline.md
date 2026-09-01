# Wastegate & Minimum-Boost Baseline Commissioning

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_WASTEGATE_BASELINE_PREP` from the No-Boost Light-Load commissioning gate.

It authorises wastegate spring-pressure / minimum-boost validation only. It does not authorise closed-loop boost control, duty-cycle tuning, launch boost, gear-based boost, high-load power pulls or competition use.

## Core safety principle

The pneumatic system must be physically arranged so that loss of PMU O6 power, loss of CAN, loss of ECU command or unplugging the boost-control solenoid returns the engine to the minimum mechanical boost state.

No software setting may be relied upon to create the minimum-boost state.

## WG-001 Wastegate hardware identification

Record:

- wastegate manufacturer and model;
- spring combination / nominal spring pressure;
- actuator port arrangement;
- hose diameter and material;
- boost-control solenoid make/model;
- solenoid port numbering and flow direction;
- boost reference source location;
- all tees/check valves/restrictors;
- whether dome pressure control is fitted.

Do not infer spring pressure from observed boost alone.

## WG-002 Static pressure test

With engine off, use a regulated pressure source appropriate to the wastegate hardware to verify actuator movement and plumbing.

Record:

- pressure at first actuator movement;
- pressure at full expected travel where applicable;
- repeatability over multiple cycles;
- leak-down behaviour;
- mechanical freedom of the linkage/valve.

Any sticking, leakage or non-repeatable operation = NO-GO.

## WG-003 Solenoid plumbing verification

Verify the actual installed solenoid ports against its manufacturer diagram.

Confirm two states:

1. O6 de-energised -> minimum mechanical boost path.
2. O6 energised -> commanded boost-control path.

Do not proceed until those states are physically proven with pressure, not merely inferred from wiring polarity.

## WG-004 Electrical fail-safe polarity

With ignition enabled but engine not running:

- command O6 OFF and verify no solenoid energisation;
- simulate CAN loss and verify O6 remains OFF;
- assert KILL and verify O6 OFF;
- cycle PMU power and verify no transient energisation;
- simulate invalid MAP and verify O6 OFF.

PASS requires the de-energised electrical state to match the safe pneumatic state.

## WG-005 MAP/boost protection readiness

Before any boosted run, configure and verify build-specific limits for:

- maximum authorised MAP/boost for this milestone;
- MAP sensor plausibility;
- overboost response;
- CAN/MAP timeout response;
- fuel-pressure validity/relationship;
- oil-pressure validity;
- lambda validity;
- ECT/IAT constraints;
- rev/load constraints.

Exact numeric thresholds are build-specific and must be justified by engine/turbo/fuel-system evidence. Do not use generic internet values in the master procedure.

## WG-006 First spring-pressure event

Perform the first boost-producing event in the lowest-energy controlled condition that can establish the wastegate baseline.

Preferred environment: controlled dyno or equivalent where load can be removed immediately.

Requirements:

- O6 commanded OFF;
- no closed-loop boost strategy active;
- minimal necessary throttle/load;
- continuous logging of RPM, TPS, MAP, lambda front/rear, fuel pressure, oil pressure, ECT, IAT, ignition timing, battery voltage, CAN health and PMU faults;
- observer ready to unload/kill.

Abort immediately for unexpected boost rise, fuel/oil pressure anomaly, unsafe lambda trend, knock/misfire evidence, CAN/PMU fault, thermal anomaly or any unexplained condition.

## WG-007 Spring-pressure repeatability

Repeat only after the first run log is reviewed and accepted.

The goal is to establish whether spring-pressure boost is repeatable with similar load/RPM conditions.

Record:

- boost onset region;
- peak MAP/boost;
- boost curve shape;
- RPM and TPS at equivalent points;
- fuel pressure trend;
- lambda behaviour;
- IAT/ECT behaviour;
- any wastegate oscillation/creep.

Large unexplained variation blocks progression.

## WG-008 Boost creep / control authority assessment

At the highest authorised spring-pressure test condition, inspect for boost creep or insufficient wastegate authority.

If boost continues to rise beyond the expected spring-pressure behaviour, do not attempt to solve it by adding solenoid control. Investigate wastegate size, reference source, exhaust backpressure, plumbing and mechanical configuration first.

## WG-009 Fuel and thermal validation under spring pressure

Confirm that the fuel system, lambda behaviour, IAT, ECT and oil pressure remain credible at the new load level.

Any unresolved fuel-pressure or thermal limitation blocks all higher-boost work.

## WG-010 Fail-safe live validation

Only where it can be done safely in the controlled environment, prove that removing O6 command returns the system toward the minimum mechanical boost state.

Do not intentionally create a hazardous transient merely to prove a fallback. Use the lowest-energy test that demonstrates the state transition.

## WG-011 Post-session inspection

Inspect:

- wastegate linkage/body;
- all boost-reference hoses/fittings;
- solenoid and connector;
- turbo/exhaust fasteners;
- heat exposure to harness;
- PMU O6 current/fault history;
- fuel/oil/coolant systems;
- SparkPRO/EPM connectors.

## WG-012 Log review and baseline freeze

Before enabling closed-loop boost control, freeze a `SPRING_PRESSURE_BASELINE` record containing:

- hardware revision;
- wastegate spring configuration;
- plumbing diagram revision;
- solenoid part number and port map;
- PMU O6 fail-safe logic revision;
- observed spring-pressure boost behaviour;
- environmental/test context;
- calibration revision;
- all abort/protection settings used.

## Release gate

Project state remains `SPRING_PRESSURE_ONLY` until all mandatory WG tests pass.

Promotion target: `READY_FOR_OPEN_LOOP_BOOST_CONTROL_PREP`.

Promotion requires:

- verified wastegate hardware/spring state;
- repeatable static actuator behaviour;
- physically proven de-energised fail-safe plumbing;
- O6 electrical fail-safe proven;
- stable repeatable spring-pressure boost;
- no unresolved boost creep/control-authority problem;
- acceptable fuel, lambda, oil and thermal behaviour;
- completed post-session inspection and log review.

Closed-loop boost remains prohibited at this milestone.
