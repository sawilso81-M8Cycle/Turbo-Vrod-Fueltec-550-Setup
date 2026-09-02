# Dyno Load Commissioning & Boost Enablement Pack

## Purpose

Define the controlled transition from `LOW_LOAD_HEAT_CYCLE_VALIDATED` into progressively loaded dyno operation and staged boost enablement for the Turbo V-Rod / FT550 / PMU16 system.

This pack is deliberately staged. A successful low-load engine does not automatically earn full boost.

## Entry conditions

Do not begin unless:

- `LOW_LOAD_HEAT_CYCLE_VALIDATED` is PASS;
- engine/turbo mechanical commissioning requirements permit dyno loading;
- dyno and motorcycle restraint/cooling arrangements are suitable;
- tyre/driveline condition is accepted for the intended test;
- fuel pressure and oil pressure monitoring are verified;
- wideband/lambda monitoring is verified;
- FT550, PMU16 and SparkPRO configuration versions are archived;
- trigger/sync is stable hot and cold;
- no unresolved electrical thermal issue remains;
- fuel pump switching/protection decisions are frozen;
- B15/B39/B40 protection is frozen;
- boost-control plumbing and wastegate hardware are physically verified;
- turbo lubrication and drain arrangements are accepted;
- an emergency abort/shutdown method is immediately available.

## Configuration policy

Every dyno stage shall record the exact calibration/configuration used. Calibration changes are versioned between runs. Never overwrite the previous known state.

Before loaded operation record:

- FT550 calibration file/revision;
- PMU configuration revision;
- SparkPRO/dwell configuration;
- fuel type;
- base fuel pressure/reference condition;
- injector PN/data source;
- wastegate spring/base-boost configuration;
- boost-control solenoid/plumbing configuration;
- boost target/limit configuration;
- ignition strategy;
- AFR/lambda target strategy;
- rev limit;
- Two-Step/launch state;
- turbo-speed sensor configuration if fitted.

## DL-0 Dyno static verification

With engine off and then at controlled idle verify:

- motorcycle restraint;
- dyno speed/RPM acquisition;
- exhaust extraction and cooling airflow;
- fuel/oil pressure channels;
- AFR/lambda channel;
- MAP/boost channel;
- TPS;
- engine temperature/IAT;
- FT550 RPM;
- PMU status;
- emergency shutdown;
- data logging.

Output: `DL0_DYNO_SETUP_ACCEPTED`

## DL-1 No-boost / minimum-load sweep

Begin with boost control disabled and the lowest practical load consistent with useful validation.

Verify under increasing but modest RPM/load:

- stable trigger/sync;
- fuel pressure behaviour;
- oil pressure behaviour;
- AFR/lambda control;
- MAP response;
- injector duty behaviour;
- ignition operation;
- charging voltage;
- Pump 1/2 current;
- B39/B40 electrical stability;
- PMU faults/current limiting;
- coolant/IAT trends.

Output: `DL1_LOW_LOAD_DYNO_ACCEPTED`

## DL-2 Wastegate/base-boost verification

Before closed-loop/electronic boost escalation, verify the mechanical wastegate/base-boost behaviour using the approved safe configuration.

Confirm:

- boost-control solenoid state cannot accidentally command more boost than intended;
- wastegate reference plumbing is correct;
- achieved boost follows the expected mechanical configuration;
- boost does not creep uncontrollably across the tested RPM range;
- fuel pressure tracks the required reference/differential strategy;
- AFR/lambda remains within the approved commissioning envelope;
- no trigger or ignition instability occurs.

If achieved boost exceeds the approved stage ceiling, abort and diagnose rather than compensating with tuning alone.

Output: `DL2_BASE_BOOST_VERIFIED`

## DL-3 Fuel-system differential-pressure validation

For boosted operation, evaluate fuel pressure relative to manifold pressure according to the installed regulator/system design.

Record throughout each loaded run:

- manifold pressure;
- fuel rail pressure;
- calculated differential fuel pressure where applicable;
- Pump 1 current;
- Pump 2 current;
- injector duty;
- battery voltage.

A falling differential pressure, unexplained pump-current change or injector-duty saturation is a load-escalation blocker.

Output: `DL3_FUEL_DELIVERY_ACCEPTED`

## DL-4 Progressive boost stages

Boost may be increased only in predefined stages approved before each run.

For each stage define:

- boost ceiling;
- RPM ceiling;
- load/run duration;
- AFR/lambda target/abort envelope;
- fuel-pressure differential requirement;
- oil-pressure requirement;
- temperature ceiling;
- ignition strategy;
- injector-duty ceiling;
- turbo-speed ceiling if measured;
- operator abort criteria.

A PASS at one stage permits consideration of the next stage. It does not automatically authorise it.

Output per stage: `BOOST_STAGE_n_ACCEPTED`

## DL-5 Ignition and combustion review

Review ignition conservatively using the available verified evidence and instrumentation.

Record:

- commanded ignition timing;
- RPM/load/MAP;
- AFR/lambda;
- temperatures;
- any available knock/combustion evidence;
- spark/dwell configuration;
- plug/engine inspection evidence where used by the tuner.

Do not treat absence of an audible knock event as proof of safe ignition timing.

Output: `DL5_IGNITION_REVIEW_ACCEPTED`

## DL-6 Turbo-speed monitoring if fitted

If turbo-speed sensing is installed, validate the sensor at low speed/load before using it as a protection input.

Record turbo speed against:

- engine RPM;
- MAP/boost;
- throttle;
- exhaust/load condition;
- boost-control command.

The maximum permissible turbo speed shall come from the exact turbocharger manufacturer/compressor assembly data, not a generic turbo value.

Configure warning/abort thresholds only after sensor scaling and source data are verified.

Output: `DL6_TURBO_SPEED_VALIDATED` or `DL6_DNP`

## DL-7 Electrical high-load validation

At each approved higher-load stage capture:

- B15 voltage/current where available;
- PMU input voltage;
- Pump 1/2 current;
- B39 injector supply behaviour;
- B40 SparkPRO supply behaviour;
- charging voltage;
- PMU current-limit/fault state;
- connector/junction temperature evidence between runs.

The electrical system must remain stable as engine load rises.

Output: `DL7_HIGH_LOAD_ELECTRICAL_ACCEPTED`

## DL-8 Thermal recovery and repeatability

Do not stack runs faster than the cooling system, turbo and engine can recover safely.

Record pre-run and post-run:

- engine/coolant temperature;
- IAT;
- oil temperature if measured;
- fuel temperature if measured;
- turbo/engine thermal observations;
- harness/connector observations.

Repeat an accepted stage where necessary to demonstrate repeatability before escalation.

Output: `DL8_REPEATABILITY_ACCEPTED`

## DL-9 Boost enablement release

After the approved progressive stages have passed, engineering/tuner review shall define the maximum boost and RPM currently released for the next development phase.

Record explicitly:

- released boost ceiling;
- released RPM ceiling;
- fuel used;
- calibration revision;
- environmental/dyno context;
- remaining restrictions;
- whether Two-Step remains disabled.

Output: `CONTROLLED_BOOST_OPERATION_RELEASED`

This is not automatically a final race calibration.

## Automatic abort categories

Abort the loaded run for any verified unsafe condition including:

- oil pressure outside approved limits;
- fuel pressure/differential pressure outside approved limits;
- confirmed unsafe AFR/lambda;
- uncontrolled overboost or boost creep beyond the stage ceiling;
- injector duty beyond the approved ceiling;
- turbo speed beyond the exact turbo's approved limit if measured;
- trigger/sync loss;
- repeated ECU/PMU reset or electrical protection event;
- unsafe temperature;
- abnormal mechanical noise;
- fuel/oil/coolant leak;
- electrical overheating/smoke;
- tyre/driveline/dyno restraint concern.

Numeric thresholds are configuration-specific and shall be entered in the stage register from verified sources and tuner/engineering approval.

## Two-Step / launch control

Two-Step remains a separate commissioning gate. Electrical operation of X70/A21 has already been verified, but combustion-based Two-Step testing introduces substantial thermal and mechanical load.

Do not enable it merely because normal boost dyno stages pass.

## Release state

After DL-0 through applicable DL-9 stages PASS:

`DYNO_LOAD_COMMISSIONING_ACCEPTED`

and the explicitly approved operating envelope is recorded as:

`CONTROLLED_BOOST_OPERATION_RELEASED`

## Next gate

Proceed to `Two-Step-Launch-Control-Commissioning-Pack`, followed later by final calibration validation and Golden Harness qualification.
