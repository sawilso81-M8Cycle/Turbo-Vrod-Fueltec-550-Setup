# Trigger Integrity Freeze – CKP / CAM / First-Start Sync Gate

## Purpose

Freeze the wiring, routing, polarity-verification and evidence requirements for the V-Rod crank and cam trigger system before first-start authorisation with the FuelTech FT550.

## Architecture

The trigger system shall retain the OEM engine trigger hardware unless deliberately revised.

Primary trigger paths:

- CKP sensor → shielded/twisted low-level trigger branch → FT550 crank input.
- CAM sensor, where used/required by the final sync strategy → dedicated low-level signal branch → FT550 cam input.

CKP and CAM wiring shall remain physically segregated from SparkPRO outputs, coil power, injector power, starter conductors, fuel-pump conductors and other high di/dt circuits.

## Polarity rule

CKP/CAM polarity shall not be frozen by wire colour alone.

Final polarity requires oscilloscope evidence from the actual sensor and installed trigger wheel/target during cranking. If the sensor is VR, polarity must be selected so the FT550 sees the intended zero-crossing/edge orientation. If the sensor is Hall, supply, ground and signal polarity must be verified from measured electrical behaviour and official documentation.

A reversed trigger that still produces RPM is not automatically acceptable.

## Shielding

For VR CKP:

- use shielded twisted pair;
- preserve pair twist to the connector breakout as far as practical;
- terminate shield according to the verified FuelTech strategy;
- do not ground shield at both ends unless the released design explicitly requires it;
- shield shall not carry sensor return current.

CAM shielding, if required by the selected sensor type/noise environment, follows the same single-authority termination principle.

## Required oscilloscope evidence

Capture and retain:

1. CKP waveform during starter cranking with ignition disabled;
2. CKP waveform during starter cranking with SparkPRO powered but coils disabled;
3. CKP waveform during starter cranking with coils/injectors enabled where safe;
4. CAM waveform during cranking if used;
5. CKP/CAM phase relationship if sequential operation depends on it;
6. waveform at first idle;
7. waveform during a controlled RPM increase after idle validation;
8. trigger waveform during operation of major electrical loads where practical.

Record scope scale, probe points, battery voltage, RPM and test configuration for every capture.

## FT550 configuration freeze

Do not finalise trigger-wheel pattern, missing-tooth configuration, edge selection, filter, sensitivity, phase or sync strategy until waveform evidence supports it.

Any FuelTech preset may be used as a starting reference only. The installed engine evidence is authoritative.

## Cranking sync acceptance

Before fuel and ignition are enabled for a first-start attempt, verify:

- stable RPM signal during cranking;
- no false tooth events;
- no intermittent RPM dropouts;
- correct CKP polarity/edge;
- correct CAM recognition if used;
- stable sync status through repeated cranking cycles;
- no sync degradation when SparkPRO and other normal electronics are powered.

## Ignition-noise immunity

After first safe ignition enable, specifically check for:

- CKP ringing coincident with coil firing;
- false edges or RPM spikes;
- CAM corruption;
- sync loss;
- waveform clipping;
- ground-reference shift.

If ignition activity corrupts the trigger, do not hide the problem with aggressive software filtering before fixing routing, grounding, shielding or signal amplitude.

## Routing rules

- CKP/CAM branches cross high-current branches at approximately right angles where unavoidable.
- Avoid long parallel runs with ignition, injector, starter, pump or fan wiring.
- Keep trigger splice/service transitions away from SparkPRO and coil branches.
- Do not share high-current ground return paths with trigger sensor returns.
- Any OEM pigtail-to-motorsport service break must preserve shielding/twist strategy.

## First-start release gate

First-start may only be promoted to `TRIGGER_SYNC_ACCEPTED_FOR_FIRST_START` when:

- trigger sensor type is confirmed;
- polarity is scope-verified;
- CKP/CAM phase is documented where applicable;
- FT550 configuration is revision-controlled;
- repeated cranking sync is stable;
- ignition-noise immunity is acceptable;
- harness routing and shielding match the released design;
- evidence captures are archived.

## Current state

`TRIGGER_ARCHITECTURE_FROZEN / WAVEFORM_AND_SYNC_MEASUREMENT_GATED`
