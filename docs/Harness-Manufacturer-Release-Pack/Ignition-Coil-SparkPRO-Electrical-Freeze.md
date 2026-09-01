# Ignition Coil + SparkPRO Electrical Freeze

## Purpose

Freeze the ignition wiring architecture around the retained V-Rod coils and FuelTech SparkPRO-2 while keeping dwell/current limits evidence-based.

## Architecture

- FT550 ignition commands drive SparkPRO-2 inputs.
- SparkPRO-2 drives the retained front/rear coils.
- Coil +12 V supply is a dedicated protected EPM branch.
- SparkPRO power and grounds use dedicated engine-management power/ground paths.
- CKP/CAM and precision sensor wiring remain physically segregated from SparkPRO/coil conductors.

## Frozen signal assignments

- Front ignition command: FT550 A8 -> SparkPRO channel 1 input.
- Rear ignition command: FT550 A9 -> SparkPRO channel 2 input.
- SparkPRO channel 1 output -> front coil primary.
- SparkPRO channel 2 output -> rear coil primary.

## Wiring classes

- FT550-to-SparkPRO command conductors: 0.50 mm².
- SparkPRO-to-coil driven conductors: 1.00 mm² baseline.
- SparkPRO grounds: 1.00 mm² each minimum baseline unless FuelTech documentation or measured current requires larger.
- B40 ignition/coil common +12 V: 1.50 mm² provisional baseline until measured coil/current evidence closes the load calculation.

## Required coil evidence

For each retained 32477-01A coil, capture:

1. primary resistance at known ambient temperature;
2. secondary resistance where meaningful/accessible;
3. exact supply voltage during test;
4. current ramp versus dwell using SparkPRO-2;
5. peak primary current at candidate dwell settings;
6. SparkPRO temperature during repeated operation;
7. coil temperature during repeated operation;
8. front/rear comparison;
9. evidence of saturation onset or diminishing current rise;
10. clean spark/sync behaviour during cranking and first idle.

## Dwell rule

Do not choose dwell by generic coil type, power target or trial-and-error increases.

Initial dwell must be conservative and based on verified FuelTech/SparkPRO guidance plus measured current-ramp behaviour of the actual coils. Increase dwell only when evidence shows additional useful current/energy without excessive coil or SparkPRO heating.

## First-start restrictions

Before first combustion:

- verify coil polarity and primary wiring;
- verify front/rear channel mapping;
- confirm no direct FT550 high-current coil drive bypasses SparkPRO;
- confirm SparkPRO grounds have low resistance to the approved EPM star point;
- confirm B40 supply protection is active;
- disable any unnecessary aggressive ignition cut/retard strategy until base spark behaviour is proven;
- confirm CKP/CAM signals remain stable with ignition outputs active.

## B40 production freeze

B40 may be promoted from `MEASUREMENT_GATED` only after:

- actual coil current is measured at the approved dwell;
- both-coil simultaneous worst credible load is calculated;
- selected conductor resistance and routed length are known;
- connector/terminal ratings exceed the load with thermal margin;
- protection setting is coordinated to the conductor and load;
- installed voltage drop is verified.

## Grounding

SparkPRO grounds must return to the dedicated EPM/engine-management star. They must not share a convenience return through fan, pump, chassis-lighting or other noisy auxiliary current paths.

The coil high-current return path must follow the released SparkPRO/FuelTech architecture and must not contaminate precision sensor returns.

## Final release states

- `SPARKPRO_COIL_ARCHITECTURE_FROZEN`
- `COIL_DWELL_CURRENT_MEASUREMENT_GATED`
- `B40_IGNITION_SUPPLY_MEASUREMENT_GATED`

Promotion to first-start-ready ignition requires all required test rows in `Ignition-Coil-SparkPRO-Verification-Register.csv` to pass.
