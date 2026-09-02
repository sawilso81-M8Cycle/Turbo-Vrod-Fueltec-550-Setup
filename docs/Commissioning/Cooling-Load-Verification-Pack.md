# Cooling Load Verification Pack – BD-004

## Purpose

Close the radiator-fan and optional charge-cooler-pump electrical blockers using measured current, inrush, voltage-drop and thermal data from the actual installed hardware.

This pack determines the final B11/B12 conductor size, protection strategy and whether each load can be driven directly from the selected PMU16 output or requires an external relay/solid-state power stage.

## Frozen architecture inputs

- B11 radiator fan prototype baseline: 2.5 mm².
- B12 charge-cooler pump prototype baseline: 2.0 mm² if fitted.
- B11/B12 remain separately protected.
- Direct PMU drive is permitted only after exact PMU hardware/output capability and measured load evidence agree.
- If B12 is not fitted, disposition is `B12_DNP`.

## Required equipment

- DC current clamp with peak/inrush capture;
- DMM with min/max logging;
- oscilloscope or data logger where useful for startup profile;
- thermocouples/contact temperature probes;
- representative 12–14.5 V source;
- suitable test protection and emergency isolation;
- PMU logging/configuration access if direct-drive testing is authorised.

Do not use an underspecified handheld meter current range in series with fan/pump startup current.

## Device identification gate

Before electrical testing record for each device:

- manufacturer and exact PN;
- nominal voltage;
- manufacturer current data if available;
- connector/terminal family;
- control mode: ON/OFF, PWM or staged;
- final mounting location;
- environmental/temperature exposure.

## B11 radiator-fan test sequence

### CF-1 Cold start inrush

Capture at least 5 cold starts:

- source voltage;
- peak current;
- inrush duration;
- minimum fan-terminal voltage;
- PMU/protection response;
- connector/terminal temperature before test.

### CF-2 Hot restart inrush

After the fan/motor has operated to representative under-hood temperature, repeat at least 5 starts and record peak current and duration.

### CF-3 Continuous current

Operate the fan at normal continuous duty and record:

- steady current;
- source voltage;
- fan-terminal voltage;
- B11 feed drop;
- return-path drop;
- PMU/output or external-switch drop;
- ambient temperature.

### CF-4 Thermal soak

Run until temperatures stabilise or for the approved test duration. Record temperature at:

- PMU terminal if direct-drive testing is authorised;
- external relay/SSR if fitted;
- fan connector;
- B11 feed termination;
- B11 return termination;
- J-P01/J-P02 interface points.

### CF-5 Simultaneous-load test

Test fan operation with representative concurrent loads including fuel pump(s), ignition, injectors and charge-cooler pump if fitted. Confirm no ECU/PMU reset, CAN fault or unacceptable supply sag.

## B12 charge-cooler pump test sequence

If B12 is fitted, perform equivalent testing:

- cold inrush;
- warm inrush;
- steady current;
- voltage drop;
- thermal soak;
- simultaneous-load test;
- repeated start cycles;
- PMU protection response.

If not fitted, formally mark every B12 verification item `DNP` and close the branch as `B12_DNP`.

## Direct PMU decision gate

Direct PMU drive may only be approved for B11 or B12 when:

1. exact PMU hardware/version and selected output rating are verified;
2. measured continuous current has acceptable engineering margin;
3. measured cold/hot inrush is compatible with output transient/protection capability;
4. exact PMU cavity/terminal/conductor combination is valid;
5. connector and wire thermal tests pass;
6. voltage drop passes;
7. PMU protection can be configured without nuisance trips;
8. repeated starts pass;
9. simultaneous-load testing passes;
10. engineering signs the final decision register.

Otherwise disposition is:

`B11_EXTERNAL_POWER_STAGE_REQUIRED`

or

`B12_EXTERNAL_POWER_STAGE_REQUIRED`

## Conductor finalisation

After measured data is available, calculate final conductor acceptance using:

- continuous current;
- inrush profile;
- route length;
- ambient/loom derating;
- connector terminal capability;
- voltage-drop target;
- protection coordination.

The prototype baselines may be upsized. They shall not be downsized without documented calculation and engineering approval.

## Protection closeout

Final electronic current limit, fuse or external-stage branch protection shall be based on measured startup and steady-state behaviour, not simply on nominal motor current.

Protection must tolerate legitimate startup while protecting the conductor, terminal, connector and switching device under fault conditions.

## Final outputs

For B11 and B12 produce:

- completed `Cooling-Load-Verification-Worksheet.csv`;
- inrush/current traces;
- voltage-drop record;
- thermal record;
- exact device and connector photographs;
- exact PMU hardware/output record;
- final conductor size;
- final protection value/configuration;
- final switching disposition;
- engineering signoff.

## Release states

Until testing is complete:

`COOLING_LOAD_VERIFICATION_PENDING`

Successful B11 direct-drive outcome:

`B11_DIRECT_PMU_DRIVE_APPROVED`

Successful B11 external-stage outcome:

`B11_EXTERNAL_POWER_STAGE_REQUIRED / VERIFIED`

B12 outcomes:

`B12_DNP`

or

`B12_DIRECT_PMU_DRIVE_APPROVED`

or

`B12_EXTERNAL_POWER_STAGE_REQUIRED / VERIFIED`

BD-004 closes only when B11 is fully accepted and B12 is either fully accepted or formally DNP.
