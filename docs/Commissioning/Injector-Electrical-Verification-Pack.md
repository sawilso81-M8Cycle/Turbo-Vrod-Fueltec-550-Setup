# Injector Electrical Verification Pack – BD-002

## Purpose

Close the injector electrical-class blocker for the retained V-Rod injectors and make the final evidence-based decision between direct FT550 injector drive and the prepared Peak & Hold path.

This document supplements the previously frozen injector architecture. It does not assume injector impedance from vehicle model, appearance or an unverified cross-reference.

## Frozen architecture

- Front injector command: FT550 A1 / Blue #1.
- Rear injector command: FT550 A2 / Blue #2.
- B39 is the separately protected injector +12 V supply branch.
- X62/X63 provide the controlled service architecture for either direct drive or an intervening Peak & Hold module.
- Harness construction shall preserve both options until the injector electrical class is accepted.

## Safety and equipment

Required equipment should include:

- calibrated DMM capable of low-ohm measurement with lead compensation;
- regulated current-limited DC supply;
- oscilloscope with suitable voltage/current probes or current clamp;
- injector pulse driver/test equipment appropriate to the injector type;
- FuelTech FT550 and FTManager for final compatibility testing;
- suitable non-flammable or approved injector test-fluid arrangement for dynamic flow testing where performed;
- temperature measurement for injector/driver/connector thermal checks.

Do not continuously energise an injector coil from battery voltage to estimate current. Injector testing shall use controlled pulse widths/duty cycles appropriate to the hardware.

## IV-1 Physical identification

Record for each injector:

- front/rear position;
- Harley/OEM PN and all body markings;
- connector family and cavity polarity;
- physical condition;
- whether both injectors are the same PN;
- any replacement/history information available.

Photograph markings and connector keying before testing.

## IV-2 Cold DC resistance

At a known injector temperature:

1. isolate the injector electrically;
2. zero/compensate meter lead resistance;
3. measure resistance across the injector coil;
4. repeat at least three times;
5. record ambient/injector temperature;
6. repeat for both injectors.

Front/rear mismatch outside the expected manufacturing tolerance for the verified injector type requires investigation before proceeding.

## IV-3 Warm resistance

After controlled warming to representative operating temperature, repeat resistance measurement and record temperature.

This establishes how coil resistance/current changes with heat and prevents a cold-only classification.

## IV-4 Dynamic current waveform

Using a suitable pulsed injector driver, capture:

- supply voltage;
- commanded pulse width;
- peak current;
- current-rise slope;
- current at pintle opening/inflection where visible;
- hold/steady current behaviour;
- turn-off/flyback behaviour;
- pulse repetition rate/duty cycle;
- injector and driver temperature.

Capture both injectors under the same conditions.

## IV-5 FT550 compatibility check

Before direct FT550 operation, verify the exact FT550 injector-output requirements from the applicable FuelTech manual/configuration for the hardware/firmware in use.

Direct drive may only be approved when:

1. injector impedance/electrical class is positively identified;
2. measured peak/steady current is compatible with the FT550 output capability;
3. the required drive strategy is supported by the FT550 configuration;
4. repeated pulsed operation produces no output fault or abnormal heating;
5. B39 supply voltage drop and protection are acceptable;
6. injector connectors/terminals pass thermal inspection;
7. both channels operate correctly and independently;
8. engineering signs the decision register.

If any criterion is not proven, direct drive is not released.

## IV-6 Peak & Hold path

If the injector electrical class requires external Peak & Hold control, or direct FT550 compatibility cannot be proven, disposition becomes:

`PEAK_HOLD_REQUIRED`

The selected module must then be verified for:

- injector electrical class;
- number of channels;
- peak-current setting;
- hold-current setting;
- FT550 command compatibility;
- supply current and B39 impact;
- grounding;
- flyback management;
- thermal performance;
- connector/terminal suitability;
- fail-safe behaviour.

X62/X63 shall allow the module to be installed without cutting/reworking the core harness.

## IV-7 B39 supply closure

Use measured injector data to calculate the final B39 requirement.

Record:

- maximum credible simultaneous injector electrical load;
- supply voltage during cranking and running;
- B39 voltage drop;
- terminal/connector temperature;
- final conductor acceptance or required upsize;
- protection type/value/configuration.

The existing 1.0 mm² B39 conductor is a prototype baseline, not permission to ignore the measured result.

## IV-8 Functional tests

After the selected architecture is installed:

- verify front command operates front injector only;
- verify rear command operates rear injector only;
- verify no cross-channel short;
- verify injector +12 V disappears under intended master/kill strategy;
- verify FT550/Peak & Hold reports no electrical faults;
- verify repeated pulse operation;
- verify cranking voltage behaviour;
- verify no material disturbance to 5 V reference/sensor ground/CAN.

## Final decision

Exactly one final state shall be entered per injector system:

`DIRECT_DRIVE_APPROVED`

or

`PEAK_HOLD_REQUIRED / PEAK_HOLD_VERIFIED`

Until the evidence is complete:

`INJECTOR_ELECTRICAL_VERIFICATION_PENDING`

BD-002 closes only after the electrical class, driver architecture and B39 supply/protection are accepted.
