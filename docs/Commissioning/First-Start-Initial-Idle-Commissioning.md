# First-Start & Initial-Idle Commissioning

## Status and authority

This procedure is executable only when `FIRST_START_READY` has been formally achieved under `First-Start-Preparation-Gate.md`. Until then it is a planning document only.

This milestone authorises a controlled first combustion and idle-only validation. It does not authorise loaded operation, boost, dyno pulls, road testing or high RPM.

## Required personnel and equipment

Minimum recommended setup:

- operator with immediate access to start/master controls;
- observer with immediate access to the hardwired kill;
- FTManager live display and logging;
- PMU Client/logging or equivalent PMU status visibility;
- verified wideband lambda monitoring;
- oil-pressure and fuel-pressure channels visible;
- ECT and battery voltage visible;
- fire extinguisher immediately accessible;
- ventilation/exhaust extraction suitable for indoor operation;
- timing light available for post-start timing confirmation;
- inspection light and absorbent material for leak checks.

## Configuration lock before start

Record calibration/revision identifiers before energising.

Required state:

- injector mode matches FS-G01 build record;
- SparkPRO-2 configuration and initial dwell match FS-G02;
- base timing synchronisation FS-G03 PASS;
- fuel leak/pressure FS-G04 PASS;
- lambda FS-G05 PASS;
- base calibration FS-G06 PASS;
- protection FS-G07 PASS;
- mechanical readiness FS-G08 PASS;
- no-start commissioning FS-G09 PASS;
- PMU O6 boost-solenoid output disabled;
- no launch/boost/high-RPM strategy active;
- data logging armed before cranking.

## Abort philosophy

The operator or observer may abort for any unexplained condition. Do not continue merely to obtain more data.

Immediate kill / NO-GO conditions include:

- no verified oil pressure promptly after start;
- fuel leak, fuel spray or strong unexplained fuel odour;
- fuel pressure grossly outside the verified commissioning target;
- uncontrolled RPM or throttle position;
- severe mechanical noise;
- smoke from wiring/electronics or abnormal electrical heating;
- loss of ECU/PMU power stability;
- SparkPRO/coil wiring fault or repeated ignition-driver fault;
- lambda indicating an obviously unsafe condition after sensors are active and readings are valid;
- coolant leak or rapid abnormal temperature rise;
- PMU critical fault;
- CAN loss that defeats a required commissioning monitor;
- operator uncertainty about a critical reading.

Do not encode generic internet pressure/lambda/timing numbers as project limits. Exact numeric abort thresholds must come from the verified engine/fuel-system/calibration evidence and be recorded in the build-specific commissioning sheet.

## IC-001 Pre-crank snapshot

With master ON and engine stopped:

1. Start FTManager/PMU logging.
2. Record battery voltage.
3. Record TPS, MAP, IAT and ECT.
4. Record oil and fuel pressure before prime.
5. Verify RPM = 0 and engine-running state false.
6. Verify O6 boost control remains OFF.
7. Verify kill input is healthy and immediately accessible.

PASS: all values plausible and no critical faults.

## IC-002 Fuel prime

Command normal prime sequence without cranking.

Record:

- prime duration;
- fuel pressure reached;
- pump current if available;
- PMU O1 status/current;
- pressure decay after prime;
- physical leak inspection.

Any leak = immediate NO-GO.

## IC-003 First combustion

Crank and allow the engine to start. Do not use unnecessary throttle.

At the instant the engine fires, priority order is:

1. oil pressure established/credible;
2. RPM controlled;
3. fuel pressure credible;
4. no fuel/oil/coolant leak;
5. no electrical/PMU/SparkPRO critical fault;
6. lambda becomes available and plausible as sensor state permits;
7. battery/charging behaviour plausible;
8. ECT progression plausible.

If the engine does not start cleanly within the project's defined cranking-attempt limit, stop and diagnose. Do not repeatedly crank while changing multiple calibration variables at once.

## IC-004 0-10 second inspection

Observer checks:

- oil/fuel/coolant leaks;
- rail/injector seals;
- fuel hose/fittings;
- exhaust/turbo area;
- wiring near SparkPRO/coils;
- PMU output status;
- unexpected smoke, heat or noise.

Operator watches oil pressure, fuel pressure, RPM, TPS, battery voltage and critical faults.

PASS: stable controlled idle/fast-idle commissioning state with no abort condition.

## IC-005 10-30 second inspection

Continue only after IC-004 PASS.

Add checks for:

- lambda front/rear assignment and plausibility;
- MAP plausibility at idle;
- ECT rising smoothly;
- injector and ignition channel behaviour;
- CAN health and validity flags;
- PMU fuel-pump run state;
- charging voltage trend;
- abnormal local heating.

Do not tune aggressively during this window. Record observations first.

## IC-006 30-60 second inspection

Continue only if temperatures, pressures and lambda remain credible.

Confirm:

- idle is controllable;
- no growing fluid leak;
- no harness/connector hot spot;
- no PMU current-limit/retry event;
- no CAN timeout;
- fuel pressure remains stable;
- oil pressure remains credible as temperature changes;
- lambda behaviour is repeatable enough for later calibration work.

A deliberate shutdown at or before 60 seconds is acceptable and preferred if any uncertainty exists.

## IC-007 Controlled shutdown

Use the normal kill/master strategy and verify:

- injector/ignition enable is removed;
- fuel pump stops according to control logic;
- engine-running state returns false;
- no output remains unintentionally energised;
- logs are saved before cycling power unnecessarily.

## IC-008 Immediate post-run inspection

Engine OFF:

- inspect all fuel fittings and injector seals again;
- inspect oil/coolant system;
- inspect turbo/exhaust proximity to harness;
- touch-check only safe accessible electrical connectors/modules for abnormal heating;
- inspect SparkPRO mounting/grounds;
- inspect PMU faults/current events;
- inspect X60-X65 and EPM branches;
- record fuel-pressure decay;
- note smells/noises/observations while fresh.

## IC-009 Log review

Review FTManager, PMU and CAN logs before another start.

Minimum channels:

- RPM;
- TPS;
- MAP;
- IAT;
- ECT;
- oil pressure;
- fuel pressure;
- lambda front/rear where fitted;
- battery voltage;
- PMU O1/O3/O6 states/current where available;
- CAN validity/health;
- engine-running state;
- relevant ECU/PMU faults.

Do not make multiple unrelated calibration changes from one short run. Each change should have a stated reason and revision record.

## IC-010 Warm-idle progression gate

A second/longer idle session is permitted only after IC-001 through IC-009 are PASS and the first-run log has been reviewed.

Warm-idle work should establish:

- repeatable starting;
- stable fuel pressure;
- credible oil pressure through temperature rise;
- correct fan strategy when temperature reaches the verified fan-control region;
- stable lambda behaviour;
- stable charging voltage;
- no thermal wiring/connector problem;
- no PMU current-limit events;
- no CAN dropouts;
- timing remains synchronised.

## IC-011 Post-warm timing verification

Where the FuelTech commissioning method permits, recheck commanded versus observed ignition timing after stable operation. Any discrepancy reopens FS-G03 and blocks progression.

## Release state

The build remains `IDLE_COMMISSIONING_ONLY` until all required IC tests pass.

Successful completion may promote the project to `READY_FOR_NO_BOOST_LIGHT_LOAD_PREP`.

It does **not** authorise boost or dyno power testing.

## Required retained evidence

- completed Initial-Idle-Test-Matrix.csv;
- FTManager first-start log;
- PMU log;
- CAN capture where available;
- first-run pressure/lambda/temperature summary;
- post-run leak/thermal inspection record;
- calibration file/revision used;
- any timing verification evidence;
- list of every calibration or wiring change made after the run.
