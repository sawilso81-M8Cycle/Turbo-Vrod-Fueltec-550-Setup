# First-Power / First-Start Master Release Gate

## Purpose

Provide one authoritative go/no-go checklist before the Turbo V-Rod is allowed to progress from completed wiring to powered ECU/PMU, cranking, fuel enable, spark enable and first combustion.

This gate consolidates upstream requirements from the harness, PMU16, FT550, SparkPRO, injector, trigger, CAN, sensor, fuel-pump and Two-Step workstreams.

## State progression

`HARNESS_BUILD_COMPLETE` → `READY_FOR_FIRST_POWER` → `FIRST_POWER_VALIDATED` → `READY_FOR_DRY_CRANK` → `DRY_CRANK_VALIDATED` → `READY_FOR_FUEL_PRIME` → `FUEL_SYSTEM_VALIDATED` → `READY_FOR_SPARK_TEST` → `SPARK_SYSTEM_VALIDATED` → `READY_FOR_FIRST_START` → `FIRST_START_AUTHORISED`.

No state may be skipped.

## Gate A — Documentation/configuration lock

PASS requires:

- harness revision identified;
- FTManager calibration revision identified;
- PMU project revision identified;
- SparkPRO configuration identified;
- injector architecture state recorded;
- trigger configuration revision recorded;
- fuel-pump switching architecture state recorded;
- connector/cavity schedule revision recorded;
- open G0/G1 blockers reviewed;
- no undocumented wiring deviation.

## Gate B — Unpowered electrical acceptance

Before connecting FT550, PMU16, SparkPRO, injectors, coils or sensors:

- 100% continuity test complete;
- no unintended power-to-ground short;
- no cross-circuit shorts;
- polarity confirmed;
- CAN H/L continuity and polarity confirmed;
- sensor-ground topology confirmed;
- CKP/CAM shielding/segregation confirmed;
- fuel-pump 4.0 mm² feed/return architecture confirmed;
- Two-Step X70 dry-contact path verified open when inactive;
- FT550 A21 proven isolated from +12 V;
- all unused powered cavities safely terminated/insulated.

PASS: harness electrically matches released documentation.

## Gate C — First power, loads inhibited

Initial power-on must be performed with engine outputs inhibited as required:

- injectors disconnected or software-disabled;
- coils/SparkPRO outputs disabled or coils disconnected as appropriate;
- boost solenoid disabled;
- fuel-pump command inhibited unless specifically required for the test;
- Two-Step command inactive.

Validate:

- battery voltage and polarity;
- PMU boot and configuration identity;
- FT550 boot and configuration identity;
- CAN communication;
- no abnormal current draw;
- no hot connector/module;
- no PMU overcurrent/retry fault;
- 5 V reference within expected range;
- sensor-ground/reference stability;
- critical sensors plausible with engine stationary.

Any smoke, heat, abnormal smell, overcurrent, reversed polarity or unexpected output activation is an immediate power-down.

## Gate D — PMU hardwired control validation

Prove with engine unable to start:

- master enable;
- start request;
- kill request;
- service/test input;
- fan override if fitted;
- O6 boost command remains inhibited;
- O11 Two-Step request behaves per state machine;
- kill/master removal de-energises all engine-authority outputs as designed.

## Gate E — Fuel-pump architecture decision

Before the fuel system is pressurised, the pump branch must have one accepted state:

- `DIRECT_PMU_DRIVE_APPROVED`, or
- `EXTERNAL_POWER_STAGE_REQUIRED` and fitted/verified.

The pump feed and dedicated return remain 4.0 mm².

PASS requires:

- pump current/inrush evidence complete;
- connector/terminal capability accepted;
- protection/current-limit value set;
- no nuisance PMU shutdown in accepted configuration;
- prime/run/kill logic proven;
- no leak during controlled pressure test.

## Gate F — Injector architecture decision

Before fuel-and-spark cranking, injector architecture must be exactly one of:

- `DIRECT_DRIVE_APPROVED`, or
- `PEAK_HOLD_REQUIRED` with driver fitted and verified.

PASS requires front/rear injector resistance/current evidence, channel mapping and supply polarity verified.

## Gate G — Trigger / dry-crank validation

With fuel and spark disabled:

- crank engine;
- capture CKP/CAM waveforms;
- verify RPM stability;
- verify synchronisation;
- verify CKP/CAM polarity and configured edge;
- verify no sync dropouts;
- verify starter-current/noise does not corrupt trigger signals;
- verify oil-pressure rise where mechanically appropriate;
- verify battery voltage remains acceptable for ECU/PMU operation.

PASS promotes to `DRY_CRANK_VALIDATED`.

## Gate H — Fuel prime and pressure validation

With spark disabled and no intent to start:

- enable pump prime;
- confirm fuel pressure;
- inspect all fuel fittings/rails/injectors for leakage;
- verify fuel-pressure sensor scaling against a known reference if available;
- verify pump current and voltage drop in installed state;
- verify pump stops on kill/master command.

Any leak is immediate NO-GO.

## Gate I — Spark system validation

With fuel disabled:

- verify SparkPRO configuration;
- verify front/rear channel mapping;
- verify coil polarity/supply;
- use a safe spark-test method;
- confirm no unexpected continuous coil charge;
- verify dwell is the approved commissioning value;
- verify no abnormal coil/SparkPRO heating;
- confirm trigger sync remains stable with ignition electronics energised.

## Gate J — Sensor plausibility before first start

At minimum validate:

- TPS closed-throttle and sweep plausibility;
- MAP ambient plausibility;
- ECT/IAT ambient plausibility;
- oil/fuel-pressure zero/reference behaviour;
- battery voltage;
- VSS stationary state;
- clutch/Two-Step state;
- CAN health.

No critical sensor may be accepted solely because FTManager displays a number.

## Gate K — First-start configuration limits

Before enabling both fuel and spark:

- boost control disabled / minimum-energy state;
- Two-Step launch function disabled unless specifically being stationary-tested after first-start release;
- conservative first-start rev limit configured;
- no launch control;
- no closed-loop boost control;
- commissioning dwell only;
- injector architecture verified;
- base fuel/ignition calibration revision locked;
- logger channels enabled for RPM, MAP, TPS, lambda where available, fuel pressure, oil pressure, ECT, IAT, battery voltage, CAN health and PMU faults.

Do not invent universal RPM/dwell/lambda thresholds here. Use the build-specific commissioning values already accepted in the project.

## Gate L — First-start authorisation

`FIRST_START_AUTHORISED` requires all mandatory gates A–K PASS and no unresolved G0/G1 blocker.

At first start:

- one operator controls ignition/start;
- one observer watches fuel/oil/coolant leaks and abnormal heat/noise where practical;
- immediate kill access is maintained;
- start only long enough to establish safe oil pressure, stable sync and basic sensor plausibility;
- abort immediately for no oil pressure, fuel leak, severe misfire, sync loss, abnormal mechanical noise, uncontrolled RPM, overheating or electrical fault.

Successful first combustion does not mean the engine is commissioned. It only allows progression into the existing Initial Idle commissioning procedure.

## Promotion

After successful first start and post-run inspection:

`FIRST_START_AUTHORISED` → `FIRST_START_COMPLETED` → `IDLE_COMMISSIONING_ONLY`.

## Current status

`FIRST_POWER_FIRST_START_MASTER_GATE_RELEASED / EXECUTION_PENDING`
