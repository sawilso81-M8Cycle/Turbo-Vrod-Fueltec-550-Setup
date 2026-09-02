# Coil + SparkPRO Verification Pack – BD-003

## Purpose

Close the ignition-current/dwell blocker using measured evidence from the actual retained coils, FuelTech SparkPRO-2, B40 supply branch and installed electrical environment.

The goal is to establish a safe dwell/current operating window, verify SparkPRO channel behaviour, and close the B40 conductor/protection decision.

## Frozen architecture

- FT550 A8 → SparkPRO channel 1 → front coil.
- FT550 A9 → SparkPRO channel 2 → rear coil.
- B40 is the separately protected ignition/coil +12 V supply branch.
- SparkPRO grounds return to the approved high-current ground architecture, not sensor ground.
- CKP/CAM wiring remains segregated from driven coil outputs and B40.

## Required equipment

Use suitably rated/calibrated equipment:

- low-ohm DMM with lead compensation;
- oscilloscope with suitable voltage and current probes/current clamp;
- regulated automotive supply or vehicle battery/charging source;
- thermocouples/contact temperature probes;
- FuelTech FT550 + FTManager;
- SparkPRO-2 installed exactly as intended;
- suitable spark-gap or actual plug arrangement for controlled testing;
- emergency power isolation.

## CS-1 Physical identification

Record for each coil:

- position: front/rear;
- exact PN and body markings;
- connector identity and polarity;
- plug/lead arrangement;
- physical condition;
- whether both coils are the same PN.

Photograph each coil and connector before testing.

## CS-2 Primary resistance

At known temperature:

1. isolate the coil;
2. compensate lead resistance;
3. measure primary resistance at least three times;
4. repeat for both coils;
5. record coil temperature.

If meaningful/accessible, record secondary resistance only where the coil architecture permits a valid measurement.

## CS-3 SparkPRO channel verification

With ignition disabled from firing the engine:

- confirm FT550 A8 commands SparkPRO CH1 only;
- confirm FT550 A9 commands SparkPRO CH2 only;
- verify no cross-channel actuation;
- verify SparkPRO supply and grounds;
- verify no output remains unintentionally active at key-on or shutdown.

## CS-4 Dwell/current sweep

Perform a controlled current-ramp sweep using conservative initial dwell.

For each test point record:

- supply voltage;
- commanded dwell;
- peak primary current;
- current-rise slope;
- point where current begins to saturate/flatten;
- SparkPRO temperature;
- coil temperature;
- B40 voltage drop;
- connector/terminal temperature;
- spark behaviour.

Increase dwell only in controlled steps. Stop if current saturation, abnormal heating, SparkPRO faulting or coil distress occurs.

Do not select production dwell merely by maximum spark intensity. The preferred operating region is the shortest dwell that provides stable ignition energy with electrical and thermal margin.

## CS-5 Voltage sweep

Repeat representative dwell/current tests at voltages covering:

- cranking voltage;
- nominal running voltage;
- charging-system upper operating voltage.

This allows the FT550 dwell strategy to account for battery voltage rather than using one fixed value blindly.

## CS-6 Thermal soak

Operate the coils/SparkPRO at a representative worst credible duty cycle long enough to identify thermal trend.

Record temperatures at:

- front coil;
- rear coil;
- SparkPRO body;
- B40 branch connector(s);
- B40 conductor near termination;
- B40 protection device/output.

No progressive uncontrolled temperature rise, terminal relaxation, odour, insulation damage or recurring SparkPRO fault is acceptable.

## CS-7 B40 supply closure

Use the measured ignition current to determine:

- maximum credible aggregate B40 current;
- cranking and running voltage drop;
- final conductor acceptance or required upsize;
- final connector/terminal class;
- protection type/value/configuration.

The existing 1.5 mm² B40 is a prototype baseline only until these measurements are complete.

## CS-8 Noise-immunity checks

With SparkPRO and coils operating, verify:

- CKP waveform remains clean;
- CAM waveform remains clean;
- FT550 retains sync;
- CAN remains stable;
- 5 V reference and precision sensors remain plausible;
- no PMU/FT550 resets occur;
- no false Two-Step/clutch input event is induced.

Capture scope/logger evidence if any disturbance is observed.

## CS-9 First-fire dwell release

Before first combustion, define a conservative initial dwell table based on the measured current ramp and voltage sweep.

The first-start dwell must:

- remain below the demonstrated saturation/thermal-risk region;
- include battery-voltage compensation where appropriate;
- be revision controlled;
- be verified at first idle before any higher-RPM or loaded operation.

## Final outputs

Produce:

- completed `Coil-SparkPRO-Verification-Worksheet.csv`;
- dwell/current waveform captures;
- voltage-sweep evidence;
- thermal record;
- B40 voltage-drop/protection decision;
- final first-start dwell release;
- engineering signoff.

## Release states

Until testing is complete:

`COIL_SPARKPRO_VERIFICATION_PENDING`

When a safe dwell/current operating window and B40 architecture are accepted:

`COIL_DWELL_CURRENT_VERIFIED`

and

`B40_PROTECTION_AND_CONDUCTOR_ACCEPTED`

BD-003 closes only after both states are achieved.
