# Fuel Pump Verification Pack – BD-001

## Purpose

Close the highest-priority fuel-pump electrical blocker using measured evidence from the actual pump(s), wiring, connector system and installed electrical environment.

This pack determines whether each pump may be driven directly by the verified PMU16 output or requires an external relay/solid-state power stage.

## Frozen design inputs

- Pump feed conductor: **4.0 mm² minimum production baseline**.
- Dedicated pump return conductor: **4.0 mm² minimum production baseline**.
- Main-harness service interface: sealed HDSCS/MCP current class previously frozen.
- Pump-native connector remains pump-model dependent.
- No reduction below 4.0 mm² is permitted by this test.
- Direct PMU drive is not assumed merely because the conductor and terminal physically fit.

## Required equipment

Use suitably rated and calibrated equipment:

- DC current clamp with inrush/peak capture or suitable current transducer/data logger;
- DMM with min/max logging;
- oscilloscope/data acquisition where needed to capture startup current profile;
- thermocouples or contact temperature probes for connector/terminal/wire temperature rise;
- regulated/high-current 12–14.5 V supply or vehicle battery/charging source representative of the installation;
- appropriate test fuse/circuit breaker and emergency disconnect;
- pressure gauge/transducer so pump load can be tested at representative fuel pressure;
- FuelTech/PMU logging where direct-PMU testing is authorised.

Do not use a handheld multimeter current input in series with a high-current pump unless the meter, leads and test method are explicitly rated for the expected current/inrush.

## Pump identification gate

Before electrical testing record:

- manufacturer;
- exact part number;
- quantity;
- nominal voltage;
- manufacturer current/flow data if available;
- native connector and terminal identification;
- fuel type;
- target base pressure;
- expected maximum differential pressure under boost;
- intended control mode: constant, staged, PWM or other.

If two pumps are fitted, test each pump individually. Do not assume two examples of the same PN draw identical current.

## Test states

### FP-1 Static identity / resistance checks

With power isolated:

- verify feed/return polarity;
- verify no short to chassis or unrelated circuits;
- verify 4.0 mm² feed and return continuity;
- inspect crimp, seal and strain relief;
- record pump winding resistance if meaningful for the pump design.

### FP-2 Cold startup inrush

Test after the pump and fuel are at the agreed cold condition.

Capture:

- supply voltage immediately before command;
- peak current;
- duration above steady-state current;
- minimum pump-terminal voltage during startup;
- PMU/output/protection behaviour if applicable.

Perform at least 5 repeat starts after sufficient reset time.

### FP-3 Warm startup inrush

Bring the pump/fuel/system to representative operating temperature, then repeat at least 5 starts.

Record peak and duration separately from cold data.

### FP-4 Steady current at representative pressure

Record current and pump-terminal voltage at:

1. free/low-load condition only if the pump manufacturer permits it;
2. target base fuel pressure;
3. representative boosted differential pressure;
4. maximum intended operating pressure.

Do not dead-head a pump unless the manufacturer explicitly permits the test method.

### FP-5 Voltage-drop test

Under the highest continuous current test state, measure simultaneously where practical:

- battery/J-P01 supply voltage;
- switching-device input voltage;
- switching-device output voltage;
- X30/X31 input/output voltage;
- pump-terminal voltage;
- pump-return terminal to J-P02/battery-negative drop.

Calculate:

`Total feed drop = source voltage - pump positive terminal voltage`

and separately record return-path drop.

Investigate any unexpectedly concentrated drop across a connector, crimp, switching device or ground joint.

### FP-6 Thermal soak

Operate at the highest credible continuous electrical load long enough for temperatures to stabilise or for the approved test duration.

Record ambient and temperature rise at:

- PMU output terminal if direct-drive testing is authorised;
- external relay/SSR terminals if fitted;
- X30/X31 connector contacts/housing;
- native pump connector;
- 4.0 mm² feed conductor near terminations;
- 4.0 mm² return conductor near terminations;
- J-P01/J-P02 connection points.

No melting, seal damage, discolouration, odour, terminal relaxation or progressive voltage-drop increase is acceptable.

### FP-7 Dynamic electrical environment

Repeat/observe pump behaviour with representative simultaneous loads:

- engine cranking;
- fan operation;
- SparkPRO/coils active;
- injectors active where safely possible;
- charge-cooler pump if fitted;
- normal charging voltage.

Confirm the pump does not cause ECU/PMU resets, CAN faults or unacceptable sensor-reference disturbance.

## PMU direct-drive decision gate

Direct PMU drive may only be approved when all of the following are true:

1. exact PMU hardware/version and selected output rating are verified from authoritative documentation;
2. measured steady current is inside the applicable continuous output capability with engineering margin;
3. measured cold and warm inrush are compatible with the output's transient/protection behaviour;
4. the exact PMU cavity/terminal/wire combination is approved for the conductor and current;
5. thermal testing passes;
6. voltage drop passes;
7. PMU electronic protection can be configured to protect the circuit without nuisance trips;
8. repeated starts pass;
9. simultaneous-load testing passes;
10. engineering signs the decision register.

If any requirement fails or remains unverified, disposition is:

`EXTERNAL_POWER_STAGE_REQUIRED`

Direct drive is never approved by conductor ampacity alone.

## External power-stage path

If required, the PMU output becomes the control command and pump current is carried by a separately protected automotive relay or suitable solid-state stage.

The external stage must then be verified for:

- continuous current;
- startup/inrush current;
- contact/MOSFET thermal performance;
- voltage drop;
- inductive-load suitability;
- fail-safe behaviour;
- environmental sealing;
- terminal compatibility with 4.0 mm² wiring or approved transition;
- branch protection close to the supply source.

## Protection setting

Do not freeze the final fuse/eFuse/current-limit value until measured current data is available.

Protection shall tolerate legitimate startup/inrush while protecting the conductor, terminals, connector and switching device under fault conditions.

The protection value must never be selected simply by rounding the measured steady current upward.

## Final outputs

For each pump produce:

- completed `Fuel-Pump-Verification-Worksheet.csv`;
- current/inrush trace or logger export;
- voltage-drop record;
- thermal record;
- pump and connector photographs;
- exact PMU hardware/output record;
- final switching disposition;
- final protection value/configuration;
- engineering signoff.

## Release states

Until testing is complete:

`FUEL_PUMP_VERIFICATION_PENDING`

Successful direct-drive outcome:

`DIRECT_PMU_DRIVE_APPROVED`

Successful external-stage outcome:

`EXTERNAL_POWER_STAGE_REQUIRED / EXTERNAL_STAGE_VERIFIED`

BD-001 closes only after one of the two final architectures has been fully verified and recorded.
