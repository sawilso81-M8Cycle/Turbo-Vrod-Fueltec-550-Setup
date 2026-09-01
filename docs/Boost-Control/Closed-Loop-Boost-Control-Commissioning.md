# Closed-Loop Boost Control Preparation & Commissioning

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_CLOSED_LOOP_BOOST_CONTROL_PREP` and the open-loop boost table has been proven repeatable.

It authorises staged closed-loop boost control development only. It does not authorise unrestricted boost, final race calibration, high-load competition use or launch/anti-lag operation.

## Core control philosophy

Closed-loop boost must sit on top of a proven open-loop duty table. The controller corrects error around a known feed-forward baseline; it must not be used to discover the system from scratch.

If any critical input becomes invalid, boost authority must reduce, never increase.

Critical validity inputs include:

- MAP / boost pressure;
- RPM;
- TPS/load where used in target selection;
- gear where used in target caps;
- CAN health if PMU/ECU coordination depends on CAN;
- fuel pressure and lambda protection states where configured as boost inhibit conditions.

Any critical invalid state forces O6 toward the minimum-energy / spring-pressure fallback already proven during WG commissioning.

## CL-001 Feed-forward table freeze

Freeze the last accepted open-loop duty table as the initial feed-forward table.

For each validated operating region record:

- RPM;
- load/TPS;
- gear if relevant;
- commanded duty;
- achieved MAP;
- ambient conditions;
- fuel pressure;
- lambda;
- IAT/ECT;
- notes on overshoot/creep.

Do not extrapolate into untested high-load cells for closed-loop use.

## CL-002 Target table definition

Create a conservative target-boost table with explicit caps by the dimensions actually used by the system, for example RPM, TPS/load and gear.

The target table must remain inside the previously proven safe operating envelope.

No target may exceed a region where open-loop control, fuel system, lambda, ignition, temperature and protection behaviour have been validated.

## CL-003 Initial controller gains

Begin with conservative closed-loop authority and low gains.

The exact P/I/D or equivalent FuelTech control values are build-specific and must not be copied from generic internet examples.

Initial strategy:

- feed-forward does most of the work;
- proportional correction is limited;
- integral authority is tightly capped and reset/limited when conditions leave the active region;
- derivative/filtering is used only if supported and justified by logged behaviour;
- total duty is clamped to a verified minimum and maximum from the open-loop milestone.

## CL-004 Error and correction limits

Define build-specific limits for:

- target minus actual MAP error;
- maximum positive duty correction;
- maximum negative correction;
- duty slew rate;
- integral accumulation;
- overshoot threshold;
- overshoot duration;
- recovery hysteresis.

No single controller correction may jump directly into an unvalidated duty region.

## CL-005 Overshoot protection

Create at least two independent layers:

1. control-layer correction reducing duty as target is exceeded;
2. hard protection layer that removes boost-control authority and returns to spring-pressure fallback if the build-specific overboost threshold is exceeded.

The hard protection threshold must be independent of normal PID correction logic.

Where practical, a second pressure source or independent protection path should be used for high-consequence overboost protection.

## CL-006 Gear / RPM / TPS target caps

Where gear, RPM or TPS/load are used to select boost target:

- invalid gear = use lowest authorised boost target or spring-pressure fallback;
- invalid RPM = disable closed-loop boost authority;
- invalid TPS/load = disable boost increase;
- invalid CAN source used for any cap = fail to the lowest safe target.

A stale value must never hold a high-boost target active.

## CL-007 First closed-loop activation

Enable closed-loop control only in a low-energy, previously validated region.

Record:

- target MAP;
- actual MAP;
- feed-forward duty;
- correction duty;
- total duty;
- RPM/load/TPS;
- gear;
- fuel pressure;
- lambda;
- IAT/ECT;
- ignition timing;
- injector duty where available;
- CAN health;
- PMU O6 current/fault state.

PASS: controller converges without overshoot, oscillation, creep or protection anomaly.

## CL-008 Gain progression

Adjust one control parameter family at a time.

For every change:

- document reason;
- record old/new value;
- repeat the same operating region;
- compare target tracking, overshoot, settling and duty behaviour;
- revert if improvement is not clear.

Do not change target table and controller gains simultaneously during initial commissioning.

## CL-009 Transient validation

Test controlled throttle/load transitions only after steady-state tracking is stable.

Validate:

- no target spike;
- no duty spike into unvalidated range;
- no oscillation after throttle changes;
- boost decays cleanly on unload;
- fuel pressure and lambda remain safe;
- O6 de-energises correctly on abort.

## CL-010 Protection and sensor-failure tests

Using controlled simulation where practical, verify:

- MAP invalid -> spring-pressure fallback;
- CAN invalid -> lowest safe target or O6 OFF as designed;
- gear invalid -> lowest target/fallback;
- fuel-pressure protection trigger -> boost authority removed;
- lambda protection trigger -> boost authority removed where configured;
- ECT/IAT over-limit -> target reduced or boost authority removed according to the build-specific strategy.

Do not intentionally create real oil starvation, fuel starvation or dangerous overtemperature to test protection logic.

## CL-011 Repeatability across conditions

Repeat accepted closed-loop cells across reasonable changes in engine temperature and ambient conditions.

Large changes in required correction duty indicate feed-forward or pneumatic inconsistency and must be resolved before increasing targets.

## CL-012 Post-session review

Review every session for:

- peak target error;
- overshoot magnitude/duration;
- settling time;
- correction duty range;
- integral accumulation if applicable;
- fuel pressure trend;
- lambda trend;
- IAT/ECT trend;
- ignition timing;
- PMU/O6 faults;
- CAN validity dropouts;
- any evidence of wastegate creep.

## Release gate

Project state remains `CLOSED_LOOP_BOOST_COMMISSIONING_ONLY` until required CL tests pass.

Promotion target: `READY_FOR_HIGHER_LOAD_TUNING_PREP`.

Promotion requires:

- repeatable target tracking in all authorised cells;
- no unexplained overshoot or oscillation;
- validated spring-pressure fallback on critical signal loss;
- stable fuel pressure and lambda;
- acceptable thermal behaviour;
- no PMU/CAN protection anomaly;
- revision-controlled target/feed-forward/gain tables;
- a separately reviewed higher-load tuning plan.

This milestone does not itself authorise unrestricted boost, final dyno tuning, launch control or racing.
