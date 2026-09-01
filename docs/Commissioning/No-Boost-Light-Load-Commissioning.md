# No-Boost Light-Load Commissioning

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_NO_BOOST_LIGHT_LOAD_PREP` under the Initial Idle commissioning gate.

It authorises controlled no-boost, light-load validation only. It does not authorise boost tuning, power pulls, launch testing, high-RPM operation or competition use.

## Configuration lock

Before each session record FTManager calibration revision, PMU project revision, hardware build revision and logger configuration.

Required configuration:

- O6 boost-control solenoid electrically disabled;
- pneumatic wastegate arrangement verified to produce minimum mechanical boost / safe bypass state;
- rev/load limits configured for commissioning;
- lambda, oil pressure, fuel pressure, ECT, MAP, TPS, RPM and battery voltage logged;
- CAN health/validity logged;
- hardwired kill verified;
- PMU protection logic active;
- cooling system proven through idle commissioning;
- no unresolved first-start or warm-idle anomaly.

## LL-001 Pre-session inspection

Verify fluid levels, fuel system, turbo/intake/exhaust fasteners, harness clearances, SparkPRO mounting, PMU/FT550 connections, battery state, throttle return and brake operation.

PASS: no leak, loose component, damaged harness or unresolved fault.

## LL-002 Static and idle baseline

Warm the engine only enough to establish the previously verified stable baseline. Compare RPM, MAP, lambda, fuel pressure, oil pressure, ECT and battery voltage against the accepted idle session.

PASS: no unexplained drift before applying load.

## LL-003 No-boost proof

Before increasing load, prove the boost-control command remains disabled and the pneumatic arrangement is in its minimum-energy state.

If MAP rises into an unapproved boost region, immediately unload/abort and investigate. Do not continue by simply increasing fuel.

## LL-004 Very-light-load steady-state validation

Apply the smallest practical controlled load, preferably on a suitable dyno or other controlled environment.

Validate:

- RPM and TPS correlation;
- MAP progression;
- lambda plausibility and cylinder-to-cylinder behaviour where dual lambda exists;
- fuel-pressure stability;
- oil-pressure credibility;
- ECT trend;
- battery/charging stability;
- CAN validity;
- PMU output currents/faults.

Hold only long enough to obtain stable evidence.

## LL-005 Low-RPM transient throttle

Perform small throttle openings and closures without entering an unapproved load/RPM region.

Look for:

- clean TPS response;
- no MAP/TPS discontinuity;
- no lean/rich transient severe enough to trigger the build-specific abort criteria;
- no ignition breakup;
- stable fuel pressure;
- controlled return to idle;
- no PMU/CAN fault.

Change one calibration family at a time and retain before/after logs.

## LL-006 Progressive light-load cells

Progress through a predefined commissioning matrix from lower to higher RPM/load only after the previous cell is accepted.

The build-specific matrix must state RPM/load boundaries. Do not invent generic boundaries in the master procedure.

At each cell record at minimum RPM, TPS, MAP, lambda front/rear, injector duty where available, fuel pressure, oil pressure, ECT, IAT, battery voltage, ignition timing, CAN health and PMU faults.

## LL-007 Cooling-system validation

During the session prove:

- ECT rises predictably;
- PMU fan threshold/hysteresis works as commissioned;
- fan current does not trip the PMU output;
- ECT responds appropriately after fan activation;
- no coolant leak develops under heat soak.

Any unexplained temperature rise blocks progression.

## LL-008 Fuel-system load validation

Under the highest authorised light-load cell, verify fuel pressure remains stable relative to the configured fuel-system strategy and that pump current/protection remains acceptable.

A pressure trend that cannot be explained is a NO-GO for increased load.

## LL-009 Ignition and synchronisation review

Review for misfire, sync errors, RPM dropouts and abnormal SparkPRO/coil heating. Recheck timing synchronisation if evidence suggests trigger drift or after any trigger configuration change.

## LL-010 Protection-function validation

Where safe to simulate without risking the engine, validate warning/fallback logic using controlled sensor/CAN simulation rather than deliberately creating real oil/fuel starvation or overheating.

Confirm at minimum CAN-loss behaviour, invalid pressure handling, fan fallback and boost-solenoid de-energised state.

## LL-011 Post-session inspection

Shut down and inspect fuel/oil/coolant systems, turbo/exhaust, harness heat exposure, SparkPRO, PMU connectors and EPM branches. Review PMU overcurrent/retry history.

## LL-012 Log review and calibration discipline

Review the complete session before another progression run. Each calibration change must have a reason, evidence and new revision identifier. Do not stack unrelated changes and then infer causality from the next run.

## Release gate

Project state remains `NO_BOOST_LIGHT_LOAD_ONLY` until all mandatory LL tests pass.

Promotion target: `READY_FOR_WASTEGATE_BASELINE_PREP`.

Promotion requires:

- stable repeatable no-boost/light-load operation;
- verified cooling behaviour;
- stable fuel and oil pressure;
- plausible lambda behaviour;
- no unresolved sync/misfire issue;
- no CAN/PMU protection anomaly;
- completed post-session inspection and log review;
- a separately reviewed wastegate/boost commissioning plan.

This milestone does not itself enable O6 or authorise boost.
