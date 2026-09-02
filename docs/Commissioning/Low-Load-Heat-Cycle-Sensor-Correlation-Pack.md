# Low-Load Heat-Cycle & Sensor Correlation Pack

## Purpose

Validate the installed Turbo V-Rod electrical, fuel, ignition, cooling and sensor systems through controlled no-load and low-load heat cycles after `FIRST_START_COMMISSIONING_ACCEPTED`.

This milestone is the bridge between first start and dyno/load development. It is not a boost-tuning or power-validation procedure.

## Entry conditions

Do not begin unless:

- `FIRST_START_COMMISSIONING_ACCEPTED` is PASS;
- first-start log has been reviewed;
- no unresolved oil/fuel/coolant leak exists;
- no unexplained trigger/sync fault remains;
- no abnormal electrical heating remains;
- baseline FT550/PMU/SparkPRO configurations are version controlled;
- oil pressure, fuel pressure and AFR monitoring remain operational;
- cooling system is ready for controlled heat cycles;
- boost control remains disabled or otherwise positively limited to the approved non-boost state;
- Two-Step/launch control remains disabled for combustion testing.

## Core rule

This procedure correlates sensors and electrical behaviour against independent observations where practical. Do not make a questionable sensor look correct by editing its calibration until wiring, reference supply, ground integrity and the independent reference have been checked.

## HC-0 Cold-soak baseline

Before starting after sufficient temperature equalisation, record:

- ambient temperature from an independent reference;
- FT550 IAT;
- FT550 engine/coolant temperature;
- MAP/barometric reading with engine off;
- TPS closed reading;
- battery voltage;
- fuel pressure before and after prime;
- 5 V reference;
- sensor-ground offset where practical.

Temperature sensors should correlate plausibly with the independent ambient reference when genuinely cold soaked.

Output: `HC0_COLD_BASELINE_ACCEPTED`

## HC-1 Start and stabilisation

Start using the accepted first-start configuration.

Confirm:

- oil pressure response;
- fuel pressure stability;
- AFR validity;
- stable trigger/sync;
- no ECU/PMU resets;
- charging voltage;
- plausible MAP/TPS;
- no new leaks/noise.

Output: `HC1_START_STABLE`

## HC-2 Controlled warm-up correlation

Log at regular intervals selected by the technician and appropriate to the rate of temperature change.

Record:

- elapsed time;
- RPM;
- TPS;
- MAP;
- AFR/lambda;
- fuel pressure;
- oil pressure;
- IAT;
- engine/coolant temperature;
- independent temperature reference where available;
- battery/charging voltage;
- Pump 1 current;
- Pump 2 current;
- B11 current/state;
- B12 current/state if fitted;
- PMU faults/current-limit state;
- trigger errors.

Output: `HC2_WARMUP_CORRELATION_ACCEPTED`

## HC-3 Cooling control validation

Allow temperature to reach only the approved range required to verify the released cooling strategy.

Verify:

- temperature signal is plausible before fan control is trusted;
- B11 command occurs according to the approved PMU/ECU strategy;
- B11 current remains consistent with accepted electrical testing;
- temperature responds appropriately after fan activation;
- B12 charge-cooler pump operates as configured if fitted;
- no cooling protection trip occurs;
- no connector/wire heating develops.

Do not continue heating solely to force a fan event if temperature becomes unsafe.

Output: `HC3_COOLING_CONTROL_ACCEPTED`

## HC-4 Low-load response checks

Only after stable temperature and pressure behaviour.

Use brief controlled no-load/very-low-load RPM changes appropriate to the engine's mechanical commissioning requirements.

Verify:

- TPS response remains smooth;
- MAP responds logically;
- RPM/trigger remains stable;
- fuel pressure remains stable;
- AFR response remains credible;
- charging voltage remains stable;
- no PMU trips occur;
- B39/B40 behaviour remains stable;
- no harness movement/contact appears.

This is not permission for high RPM, boost, road loading or dyno power pulls.

Output: `HC4_LOW_LOAD_RESPONSE_ACCEPTED`

## HC-5 Hot shutdown and heat-soak

After the approved warm-up period, shut down deliberately and record:

- shutdown temperature;
- oil pressure immediately before shutdown;
- fuel pressure immediately before shutdown;
- battery voltage;
- post-shutdown temperature rise/heat soak;
- IAT heat soak;
- fuel pressure decay trend;
- visible leak inspection;
- harness/connector thermal inspection.

Pay particular attention to wiring near turbo/exhaust heat sources.

Output: `HC5_HEAT_SOAK_ACCEPTED`

## HC-6 Hot restart

After the defined heat-soak period, perform a controlled hot restart if mechanical commissioning requirements permit.

Capture:

- cranking minimum battery voltage;
- PMU/FT550 reset behaviour;
- hot-start time/quality;
- oil pressure recovery;
- fuel pressure;
- AFR validity;
- trigger/sync;
- charging voltage;
- pump current;
- abnormal electrical heating.

Output: `HC6_HOT_RESTART_ACCEPTED`

## HC-7 Repeat heat cycles

Perform the number of heat cycles required by the engine/turbo mechanical commissioning plan. This electrical pack does not invent a universal break-in cycle count.

For each cycle retain comparable cold/start/warm/hot/shutdown data so drift can be detected.

Look for:

- worsening voltage drop;
- increasing pump/fan current;
- connector heating;
- sensor offset drift;
- trigger errors emerging hot;
- ground-reference movement;
- fuel-pressure instability;
- charging-system instability.

Output: `HC7_REPEATABILITY_ACCEPTED`

## Sensor correlation rules

### TPS

Check closed position, smooth sweep and repeatability. Calibration changes require evidence that mechanical stop/linkage and electrical wiring are correct.

### MAP

Engine-off MAP should correlate with local barometric pressure/reference closely enough to support the selected sensor calibration. Running response must be physically plausible.

### IAT / engine temperature

Cold-soak readings should be compared with an independent temperature reference. Hot readings should be checked for plausible trend and response rather than assumed exact without a suitable reference.

### Fuel pressure

Compare ECU/logged pressure, if electronically measured, against a trusted independent gauge/transducer where practical. Record reference conditions for base pressure.

### Oil pressure

Where ECU/logged oil pressure is used for protection, correlate it with a trusted independent reference before relying on automatic shutdown thresholds.

### AFR / lambda

Confirm controller/sensor status and configuration. If independent comparison equipment is available during later dyno work, correlation should be repeated under load.

### Battery / charging voltage

Compare ECU/PMU logged voltage with DMM measurement at relevant power points to identify offset caused by wiring or calibration.

## Electrical thermal inspection

At hot condition inspect/measure as practical:

- B15/J-P01/J-P02;
- PMU connector;
- Pump 1/2 connectors;
- B39 injector supply path;
- B40 SparkPRO supply path;
- B11/B12 connectors;
- main grounds;
- X70 relay/socket;
- harness near turbo/exhaust.

Any progressive heating trend must be explained before load is increased.

## Abort conditions

Stop the run for:

- oil/fuel pressure outside verified safe limits;
- fuel/oil/coolant leak;
- confirmed unsafe AFR/lambda;
- uncontrolled RPM;
- trigger/sync instability;
- repeated ECU/PMU reset;
- protection trip without understood cause;
- unsafe temperature;
- abnormal mechanical noise;
- electrical smell/smoke/heating;
- turbo oiling concern;
- sensor behaviour inconsistent enough that protection/tuning decisions cannot be trusted.

Numeric thresholds remain configuration-specific and must be populated from verified sources.

## Release state

After HC-0 through HC-7 and the sensor-correlation register are accepted:

`LOW_LOAD_HEAT_CYCLE_VALIDATED`

This authorises progression to controlled dyno/load commissioning under a separate gate.

It does not authorise unrestricted boost, Two-Step/launch operation, road/race use or full-load tuning.

## Next gate

Proceed to `Dyno-Load-Commissioning-and-Boost-Enablement-Pack`.
