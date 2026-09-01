# Higher-Load / Dyno Tuning Preparation

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_HIGHER_LOAD_TUNING_PREP` under the closed-loop boost commissioning release gate.

It authorises structured higher-load dyno preparation and staged load-cell validation. It does **not** authorise an unrestricted full-power pull until the final release gate in this document is passed.

## Core tuning philosophy

Progress from proven lower-load cells into higher-load regions in controlled steps. Fuel, ignition and boost must not all be changed aggressively at the same time.

The tuning sequence is:

1. confirm fuel-system capacity and pressure stability;
2. validate injector duty/headroom;
3. establish lambda control/targets by cylinder where available;
4. validate ignition timing conservatively;
5. confirm thermal stability and repeatability;
6. only then increase load/boost target.

## DY-001 Dyno and vehicle setup

Before load testing:

- secure motorcycle correctly for the dyno type;
- verify tyre condition/pressure and drivetrain condition;
- verify cooling airflow and exhaust extraction;
- verify fire suppression and hardwired kill access;
- record fuel type/batch where practical;
- record ambient temperature, pressure and humidity if dyno correction is used;
- record FTManager, PMU and build revisions;
- verify closed-loop boost control release state and protection configuration.

PASS: physical setup safe and revision-controlled.

## DY-002 Instrumentation readiness

Minimum channels for higher-load operation:

- RPM;
- TPS;
- MAP/boost;
- lambda front;
- lambda rear where dual sensors are installed;
- fuel pressure;
- oil pressure;
- injector duty/pulsewidth where available;
- ignition timing;
- IAT/post-intercooler IAT;
- ECT;
- battery voltage;
- PMU O1/O2/O3/O4/O5/O6 state/current where applicable;
- CAN health/validity;
- boost target and actual MAP;
- boost duty/feed-forward/closed-loop correction;
- engine protection/fault states.

Do not begin higher-load work without trustworthy fuel pressure and lambda data.

## DY-003 Fuel-system capacity gate

Using progressively higher load, verify fuel pressure remains stable relative to the configured pressure strategy.

Record:

- fuel pressure versus MAP;
- primary/secondary pump activation where staged;
- pump current;
- injector duty/pulsewidth;
- battery voltage;
- fuel temperature where available.

Any unexplained pressure decay, pump current-limit event or insufficient injector headroom blocks progression.

The build-specific acceptance limit for maximum injector duty must be explicitly recorded. Do not hard-code a generic internet percentage into this master procedure.

## DY-004 Cylinder-specific lambda gate

Where front/rear lambda is available, evaluate cylinders independently.

At each accepted load cell record:

- commanded lambda;
- front measured lambda;
- rear measured lambda;
- cylinder trim if applied;
- repeatability over more than one sample.

Do not hide a persistent cylinder imbalance with a single averaged lambda value.

If only one lambda channel is available, note the limitation prominently in the run record and use a more conservative progression strategy.

## DY-005 Staged load-cell matrix

Create a build-specific table of RPM versus load/MAP zones.

Progress one band at a time from already-proven regions.

For each cell:

1. enter from a previously accepted cell;
2. stabilise only long enough for valid data;
3. inspect lambda, fuel pressure, ignition behaviour and temperatures;
4. abort immediately if a protection threshold or abnormal trend appears;
5. mark the cell PASS/FAIL/RETEST before progressing.

Do not jump across untested regions solely because the engine appears stable at a higher point.

## DY-006 Fuel tuning discipline

Fuel changes should be made before ignition optimisation in a new load region unless there is a compelling evidence-backed reason otherwise.

Requirements:

- preserve pre-change calibration revision;
- change a clearly identified fuel table/trim family;
- state expected effect;
- perform a repeat run;
- compare logged result;
- retain or revert based on evidence.

Closed-loop lambda correction, if enabled, must not be allowed to mask a poor base map during validation.

## DY-007 Ignition tuning discipline

Ignition timing must be approached conservatively after fueling is stable.

Requirements:

- use verified base timing synchronisation;
- record commanded timing by tested cell;
- make small revision-controlled changes;
- monitor torque response, lambda stability, exhaust/thermal response and any available combustion/knock evidence;
- stop advancing timing when additional advance no longer provides justified benefit or when any adverse evidence appears.

Do not assume maximum torque timing is automatically safe for repeated high-load operation.

## DY-008 Knock / combustion evidence

If reliable knock/combustion instrumentation is available, record its source, calibration and interpretation method.

Potential evidence sources may include dedicated knock detection, in-cylinder/pressure tools, plug inspection, EGT balance, dyno torque response and repeatability.

Absence of a trustworthy knock channel must be documented and should drive a more conservative ignition strategy. Do not treat noisy OEM-style knock data as authoritative without validation on this engine.

## DY-009 Thermal envelope

Track at minimum:

- IAT/post-intercooler IAT;
- ECT;
- oil temperature if available;
- fuel temperature if available;
- SparkPRO/coil heating observations;
- PMU/output thermal/current events;
- turbo/exhaust heat exposure to wiring.

Define build-specific cooldown and maximum-temperature gates before higher-load testing. Do not continue increasing load through unexplained heat soak.

## DY-010 Boost-target progression

Higher boost targets may be introduced only after the current lower target is repeatable and fuel/thermal margins are acceptable.

For each target level record:

- target MAP/boost;
- achieved peak and steady MAP;
- overshoot;
- feed-forward duty;
- closed-loop correction;
- fuel pressure;
- lambda by cylinder;
- ignition timing;
- injector duty;
- IAT/ECT;
- any protection action.

A target level that needs excessive closed-loop correction reopens the feed-forward calibration rather than being accepted by force.

## DY-011 Repeatability requirement

A cell/target is not considered validated from one successful run.

Require repeated evidence under similar conditions before promotion. Variability in boost, fuel pressure, lambda, ignition behaviour or thermal response must be understood before additional load is added.

## DY-012 Protection validation at higher load

Without deliberately endangering the engine, prove that configured protections remain active in the higher-load calibration.

Validate through safe simulation or bounded conditions where possible:

- hard overboost protection;
- MAP invalid fallback;
- CAN invalid fallback;
- fuel-pressure fault response;
- lambda fault/invalid handling;
- ECT/IAT thermal protection;
- PMU O6 de-energised fallback;
- hardwired kill priority.

## DY-013 Post-run inspection

After each meaningful load increase inspect:

- fuel/oil/coolant leaks;
- plugs if part of the tuning evidence plan;
- turbo/manifold/exhaust hardware;
- charge piping/couplers;
- injector/rail area;
- SparkPRO/coils;
- PMU and high-current terminals;
- harness heat exposure;
- any evidence of detonation/pre-ignition damage if suspected.

## DY-014 Full-power pull readiness review

Before the first unrestricted/full-power pull, all of the following must be frozen and reviewed:

- fuel system has demonstrated required pressure/flow margin;
- injector duty/headroom is acceptable;
- lambda targets are validated and cylinder imbalance addressed;
- ignition table in the intended high-load region is conservative and evidence-backed;
- boost target/control is repeatable;
- hard overboost protection is verified;
- IAT/ECT/oil thermal envelope is defined;
- closed-loop boost correction is not excessive;
- no unresolved CAN/PMU/injector/ignition fault exists;
- drivetrain/tyre/dyno setup is suitable for the expected power;
- operator/observer abort plan is understood.

## Release state

Until DY-001 through DY-014 and their required evidence pass, project state remains:

`HIGHER_LOAD_TUNING_ONLY`

Successful review promotes to:

`READY_FOR_FULL_POWER_PULL_PREP`

This state means the system is prepared for a separately controlled full-power validation milestone. It is not a blanket authorisation for repeated maximum-power runs.
