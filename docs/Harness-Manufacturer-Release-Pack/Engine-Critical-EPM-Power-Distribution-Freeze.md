# Engine-Critical EPM Power Distribution Freeze – B39 Injector Supply / B40 Ignition Supply

## Purpose

Freeze the architecture for the injector and ignition common power feeds without inventing final fuse/current-limit values before injector and coil electrical evidence is complete.

## Architecture

B39 injector supply and B40 ignition/SparkPRO supply are separate engine-critical branches. They shall not share one protection device, one undersized splice, or one ambiguous common feed.

Preferred topology:

`J-P01 protected engine-power source -> B39 injector protection -> injector +12 V distribution`

`J-P01 protected engine-power source -> B40 ignition protection -> SparkPRO / coil +12 V distribution`

The PMU may command or directly protect these branches only when the exact output/current/thermal limits are verified for the selected hardware and load. Otherwise use an approved external protected stage.

## B39 Injector common +12 V

Current prototype baseline:

- conductor: 1.0 mm²;
- approximate routed length: 500 mm;
- prototype first cut: 650 mm;
- destination: common injector +12 V distribution feeding front/rear injectors or selected Peak & Hold module path.

Final conductor/protection acceptance requires:

- injector electrical class and final direct-drive vs Peak & Hold decision;
- aggregate injector supply current under maximum intended duty cycle;
- voltage-drop test at operating voltage;
- connector/terminal thermal margin;
- protection time-current behaviour compatible with injector inrush/pulsed loading.

Do not assume injector low-side driver current equals B39 supply-wire current without measurement/evidence.

## B40 Ignition / SparkPRO / coil +12 V

Current prototype baseline:

- conductor: 1.5 mm²;
- approximate routed length: 500 mm;
- prototype first cut: 650 mm;
- destination: SparkPRO / coil supply distribution as defined by the released ignition architecture.

Final conductor/protection acceptance requires:

- measured/verified coil current ramp at accepted dwell;
- both-cylinder maximum simultaneous credible load;
- SparkPRO supply current requirement;
- cranking-voltage behaviour;
- voltage-drop and connector-temperature evidence;
- protection coordination that does not nuisance-trip during cranking or launch operation.

Dwell remains evidence-gated. Increasing dwell is not an acceptable substitute for inadequate supply voltage or poor wiring.

## Grounding

- SparkPRO grounds remain dedicated low-impedance returns to the released J-P02 power-ground/star architecture.
- Injector driver returns remain per FT550/Peak & Hold architecture.
- Neither B39 nor B40 high-current return path may be routed through precision sensor ground/reference circuits.

## Protection rules

B39 and B40 require independent protection settings/devices.

Final values are not frozen until load evidence is complete. Protection must be selected from measured steady/pulsed/inrush current, conductor ampacity, connector limits, ambient temperature and voltage-drop targets.

No final fuse/current-limit value shall be selected only from conductor size.

## Failure containment

A B39 injector-supply fault shall not remove B40 ignition power unless master/kill logic intentionally removes all engine power.

A B40 ignition-supply fault shall not back-feed B39 or precision-sensor supplies.

Kill/master action must remove injector and ignition energy according to the released first-start/commissioning safety architecture.

## Acceptance states

B39 final state:

- `B39_DIRECT_DISTRIBUTION_APPROVED`, or
- `B39_EXTERNAL_PROTECTED_STAGE_REQUIRED`.

B40 final state:

- `B40_DIRECT_DISTRIBUTION_APPROVED`, or
- `B40_EXTERNAL_PROTECTED_STAGE_REQUIRED`.

## Current release status

**B39_EPM_POWER_ARCHITECTURE_FROZEN / CURRENT_PROTECTION_MEASUREMENT_GATED**

**B40_EPM_POWER_ARCHITECTURE_FROZEN / DWELL_CURRENT_PROTECTION_MEASUREMENT_GATED**

The 1.0 mm² B39 and 1.5 mm² B40 prototype baselines remain valid for prototype planning only until the electrical evidence closes them.