# First Start Authorisation & Initial Engine Run Pack

## Purpose

Define the controlled transition from `FIRST_POWER_COMMISSIONING_ACCEPTED` to the first combustion event and initial no-load engine run.

This is a commissioning procedure, not a tuning or dyno procedure. Boosted load, launch control, Two-Step operation under combustion, road operation and power pulls remain prohibited until later gates.

## Entry conditions

First start remains blocked unless:

- `FIRST_POWER_COMMISSIONING_ACCEPTED` is PASS;
- harness serial/as-built revision is known;
- FT550, PMU16 and SparkPRO hardware/configuration revisions are recorded;
- CKP/CAM cranking signal and synchronisation evidence are accepted;
- fuel system is mechanically complete and leak checked;
- oil system is correctly filled/primed as required by the engine build procedure;
- cooling system is complete and filled/bled sufficiently for the planned short run;
- throttle returns correctly and TPS is plausible;
- MAP, IAT and engine-temperature readings are plausible;
- wideband/AFR system is installed, configured and known to be operational before relying on AFR data;
- fuel pressure can be monitored;
- oil pressure can be monitored;
- emergency engine shutdown is immediately available;
- fire extinguisher suitable for the work area is accessible;
- motorcycle is mechanically secured and transmission state is controlled;
- exhaust/turbo area is clear of loose materials and fuel residue;
- no open electrical or fuel-system nonconformance remains.

## Baseline calibration rule

The initial calibration must be a deliberately conservative, verified starting calibration appropriate to the installed engine, injectors, fuel pressure, trigger pattern, ignition system and sensors.

Do not use the first start to discover whether injector characterization, trigger configuration or ignition outputs were guessed correctly.

Before cranking with fuel and spark enabled, record:

- calibration filename/revision;
- injector data/source;
- base fuel pressure target;
- trigger configuration;
- ignition output configuration;
- dwell baseline/source;
- cranking fuel settings;
- idle target;
- initial rev limit;
- boost-control state;
- Two-Step/launch-control state.

Boost control and Two-Step shall be disabled/inhibited for first start unless a later approved procedure explicitly requires otherwise.

## FS-0 Final pre-start walk-around

Immediately before first start:

- inspect all fuel fittings/rails/lines;
- inspect oil lines/filter/cooler/turbo oil plumbing where applicable;
- inspect coolant connections;
- inspect throttle linkage/cable/return;
- confirm exhaust/turbo clearances;
- confirm battery terminals and main grounds secure;
- confirm pump, injector and ignition connectors locked;
- confirm no tools/rags remain in engine/exhaust/intake area;
- confirm ventilation/exhaust extraction appropriate to the workspace.

Output: `FS0_PRESTART_ACCEPTED`

## FS-1 Key-on fuel-system prime

Command/allow the normal prime sequence without cranking.

Record:

- battery voltage;
- Pump 1/Pump 2 state;
- fuel pressure achieved;
- pressure stability after prime;
- visible/odour leak inspection;
- PMU pump current where available;
- any protection trip.

Any fuel leak = immediate stop, depressurise safely and HOLD.

Output: `FS1_FUEL_PRIME_ACCEPTED`

## FS-2 Oil-system readiness

Confirm the oil-system preparation required by the engine/turbo build has been completed.

Where oil pressure can be established/verified during no-start cranking under the applicable mechanical procedure, record the evidence before combustion.

Do not repeatedly crank an engine without an approved lubrication strategy merely to chase an electrical milestone.

Output: `FS2_OIL_SYSTEM_READY`

## FS-3 First combustion attempt

Enable the released fuel and ignition configuration only after FS-0 through FS-2 PASS.

First attempt should be brief and controlled.

Observe immediately:

- oil pressure response;
- fuel pressure;
- RPM;
- AFR/wideband status;
- FT550 synchronisation/trigger errors;
- battery/charging voltage;
- PMU trips/current-limit events;
- abnormal mechanical noise;
- fuel/oil/coolant leaks;
- smoke unrelated to normal assembly residue;
- throttle/idle control behaviour.

If the engine does not start promptly, stop and diagnose. Do not use repeated long cranking as a substitute for diagnosis.

Output when successful and stable enough to continue: `FS3_FIRST_COMBUSTION_ACCEPTED`

## FS-4 Immediate 0-30 second run window

Keep RPM low and avoid unnecessary throttle input.

Monitor continuously:

- oil pressure;
- fuel pressure;
- AFR/wideband validity;
- engine RPM;
- engine temperature trend;
- battery/charging voltage;
- trigger/sync status;
- PMU fault status;
- visible leaks;
- abnormal noise.

No boost target, launch control or Two-Step testing is permitted.

Output: `FS4_INITIAL_30S_ACCEPTED`

## FS-5 Early warm-up window

If FS-4 is stable, continue a controlled no-load warm-up only as required for inspection and validation.

Record at defined intervals:

- elapsed time;
- RPM;
- oil pressure;
- fuel pressure;
- AFR;
- coolant/engine temperature;
- IAT;
- MAP;
- battery/charging voltage;
- PMU faults;
- ECU trigger errors;
- Pump 1/2 current where available;
- B11/B12 state.

Do not hold a fresh or unknown engine at one arbitrary RPM solely to satisfy this electrical procedure. Mechanical break-in requirements take precedence.

Output: `FS5_EARLY_WARMUP_ACCEPTED`

## FS-6 Cooling-system functional check

During a controlled warm-up, verify the cooling strategy without allowing unsafe temperature.

Check as applicable:

- temperature sensor plausibility;
- B11 radiator-fan command/operation;
- B12 charge-cooler pump if fitted;
- PMU current/fault behaviour;
- coolant leaks;
- temperature response.

Output: `FS6_COOLING_FUNCTION_ACCEPTED`

## FS-7 Electrical/thermal inspection after shutdown

Shut the engine down deliberately before extended operation.

Inspect:

- B15/J-P01/J-P02;
- PMU connector;
- B39/B40 paths;
- SparkPRO/coils;
- injector connectors;
- Pump 1/2 high-current connectors;
- X70;
- grounds;
- harness near turbo/exhaust;
- fuse/protection hardware.

Look for heat, discolouration, odour, looseness, chafing or movement.

Output: `FS7_POST_RUN_INSPECTION_ACCEPTED`

## FS-8 Data-log review

Save the complete first-start log before changing calibration.

Review at minimum:

- cranking and start RPM;
- sync/trigger errors;
- battery voltage during crank;
- charging voltage after start;
- oil pressure trend;
- fuel pressure trend;
- AFR validity/trend;
- MAP/TPS/IAT/temperature plausibility;
- PMU faults/current-limit events;
- pump behaviour;
- injector/ignition configuration consistency.

Calibration corrections shall be versioned. Do not overwrite the evidence of the first-start configuration.

Output: `FS8_FIRST_START_LOG_REVIEWED`

## Automatic abort conditions

Immediately shut down for any of the following:

- absent or clearly unsafe oil pressure;
- fuel leak or rapidly falling unexplained fuel pressure;
- coolant leak that threatens safe operation;
- uncontrolled RPM or throttle;
- severe lean indication where AFR data is confirmed valid;
- confirmed ignition/trigger instability that risks engine damage;
- repeated ECU/PMU reset;
- abnormal mechanical knock/grinding/contact noise;
- smoke, wiring smell or electrical overheating;
- protection device repeatedly tripping;
- unsafe engine/coolant temperature;
- turbo oiling problem;
- any condition where the operator cannot explain whether continued running is safe.

The exact numeric abort thresholds for oil pressure, fuel pressure, AFR, temperature and RPM shall come from the verified engine/fuel/turbo configuration and approved commissioning calibration, not invented generic values.

## First-start release state

When FS-0 through FS-8 are PASS and evidence is reviewed:

`FIRST_START_COMMISSIONING_ACCEPTED`

This permits progression to controlled low-load validation under a separate milestone.

It does not authorise:

- boost operation;
- Two-Step under combustion;
- launch testing;
- full-load dyno pulls;
- road use;
- race use;
- Golden Harness status.

## Next gate

Proceed to `Low-Load-Heat-Cycle-and-Sensor-Correlation-Pack` before any boosted or high-load calibration work.
