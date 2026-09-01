# High-Current Load Closure – Harness Production Gate

## Purpose

Close the remaining load-dependent cable-size and protection decisions for the Turbo V-Rod FT550 / PMU16 harness without relying on generic current guesses.

## Circuits covered

- B10 primary fuel pump / PMU O1
- B11 radiator fan 1 / PMU O3
- B12 charge/intercooler pump / PMU O5 if fitted
- B15 PMU main battery feed
- B39 injector common +12 V
- B40 ignition/coil common +12 V
- PMU device ground
- SparkPRO ground paths
- O6 boost-control solenoid supply

## Rule

A provisional conductor may be used for RFQ and first-prototype material planning, but no high-current circuit becomes `PRODUCTION_FROZEN` until all of the following are known:

1. exact load manufacturer/model or physically identified OEM part;
2. actual system voltage used for test;
3. steady-state current;
4. inrush/peak current where applicable;
5. routed conductor length;
6. conductor material/series and temperature class;
7. terminal and connector current capability;
8. PMU output/current-limit capability or external fuse/protection value;
9. calculated voltage drop at steady current;
10. acceptable thermal/protection margin;
11. measured installed voltage drop after build.

## Test voltage

Measure at realistic motorcycle electrical-system voltage and record the exact test voltage. Do not compare currents measured at different voltages without noting the difference.

## Measurement methods

### Motors / pumps / fans

Use a suitable DC supply or vehicle battery with current measurement capable of capturing inrush. Test the actual installed or purchased component.

Record:

- voltage immediately before energising;
- peak/inrush current;
- steady current after stabilisation;
- component temperature/ambient where relevant;
- whether the component was mechanically loaded in a representative way.

A free-running pump or fan may draw less than it does in the installed system, so final vehicle validation remains required.

### Injectors

For each 27772-06 injector record coil resistance at known ambient temperature and, using the approved driver architecture, capture current behaviour. The result determines direct-drive versus Peak & Hold configuration and B39 supply demand.

### Coils / SparkPRO

For each 32477-01A coil record primary resistance and current-ramp evidence using the approved SparkPRO configuration. Initial dwell must come from verified commissioning evidence, not from raising dwell to increase current arbitrarily.

### PMU main feed

Calculate B15 from the worst credible simultaneous PMU-controlled load state, not by simply adding PMU output nameplate ratings.

Create at least these states:

- KEY_ON / ENGINE_OFF
- CRANKING
- ENGINE_RUNNING_NORMAL
- HOT_IDLE_FANS_ON
- BOOST_RUN
- MAX_EXPECTED_AUXILIARY_STATE

For each state sum actual measured/validated steady currents and identify short-duration inrush overlaps separately.

## Voltage-drop calculation

For a copper conductor:

`Vdrop = I × R_per_m × one_way_length_m`

Where the return path is a separate wire of the same size and length, calculate both legs or use total loop length.

Do not assume chassis return equals zero resistance. High-current return paths require their own measured voltage-drop validation.

Final production selection must use the actual selected wire manufacturer's conductor resistance where available rather than a generic copper table.

## Protection coordination

For each PMU output:

- operating current must sit below the configured continuous trip/current-limit region with sensible margin;
- inrush must not create nuisance shutdown;
- current limit must still protect the conductor and connector;
- repeated auto-retry must not thermally abuse a stalled motor or shorted load;
- protection setting must not be increased merely to hide an undersized conductor or failing component.

For B15 main feed, coordinate the upstream battery protection device with the selected main-feed conductor and downstream PMU architecture.

## Provisional conductor baselines retained

Until measured evidence closes the rows:

- B10 primary fuel pump: 2.0 mm²
- B11 radiator fan 1: 2.5 mm²
- B12 charge/intercooler pump: 2.0 mm²
- B15 PMU main feed: 10 mm²
- B39 injector common supply: 1.0 mm²
- B40 ignition/coil common supply: 1.5 mm²
- PMU device ground: 1.0 mm² minimum baseline
- SparkPRO grounds: 1.0 mm² each baseline
- O6 boost solenoid: 0.75 mm²

These are not permission to downsize a measured load that requires more conductor.

## Production freeze criteria

A row may be promoted from `MEASUREMENT_GATED` to `PRODUCTION_FROZEN` only when `High-Current-Load-Test-Worksheet.csv` contains complete measured evidence and `High-Current-Sizing-Final-Decision.csv` records:

- final wire size;
- final terminal/contact PN;
- final connector housing;
- final PMU current limit/fuse setting;
- calculated voltage drop;
- measured installed voltage drop target/test result;
- engineering disposition.

## Current milestone status

`HIGH_CURRENT_CLOSURE_FRAMEWORK_RELEASED / LOAD_MEASUREMENTS_PENDING`

This milestone closes the engineering method. Actual component measurements remain mandatory before `MANUFACTURING_RELEASED_REV1`.
