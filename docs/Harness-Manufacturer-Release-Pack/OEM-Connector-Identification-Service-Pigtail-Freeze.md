# OEM Connector Identification & Service-Pigtail Freeze

## Purpose

Close the retained Harley-Davidson VRXSE/Destroyer engine-device interfaces without inventing connector part numbers. Where the OEM parts catalogue identifies a sensor but not its mating harness housing, the Rev 1 production strategy is to preserve a verified OEM connector/pigtail and terminate it into a controlled motorsport service break.

## Verified VRXSE device baseline

Harley-Davidson VRXSE parts data confirms the following retained-device references used by this project:

- CKP: 32313-01A crankshaft position sensor; catalogue also lists terminal 74194-98 with the sensor.
- MAP: 32416-10 MAP sensor.
- VSS: 74402-05B speed sensor.
- Coil: 32477-01A coil assembly; 31651-01 coil boot.
- Oil-pressure switch: 26561-99 if retained for discrete warning/protection use.
- Neutral switch: 33902-98A if retained.

TPS, ECT, IAT and injector identities already used in the project must be physically cross-checked against the actual Destroyer before a bare mating housing is purchased.

## Rev 1 connector policy

### Category A – exact mating connector positively identified

Use the released housing, terminal, seal, wedge/lock and boot part numbers directly.

### Category B – OEM sensor identified but mating housing not positively identified

Do **not** substitute a visually similar connector. Obtain a genuine or known-compatible OEM repair pigtail, prove fit/keying/retention/sealing on the actual component, then create a controlled service break 100–150 mm downstream where packaging permits.

Preferred service-break families:

- low-current 2–4 circuit sensor/command interfaces: Deutsch DTM, size-20 contacts;
- circuits exceeding DTM contact/wire capability: Deutsch DT, DTP or another released higher-current sealed family selected to the actual load and conductor size.

TE documents DTM as size-20, 7.5 A contacts with a nominal 0.35–2.5 mm² family wire range. This makes DTM appropriate for sensor and command service breaks, not the 4.0 mm² fuel-pump power path.

### Category C – device itself not frozen

Connector remains device-selection gated. This applies to the primary fuel pump, optional secondary fuel pump, charge-cooler pump and any replacement fan until the exact hardware is confirmed.

## OEM pigtail acceptance

Every retained OEM pigtail must pass:

1. positive physical mating to the actual device;
2. correct keying and latch retention;
3. seal condition inspection;
4. terminal retention pull check appropriate to the connector;
5. cavity-to-device-function continuity identification;
6. minimum 100 mm of healthy conductor beyond the rear seal where practical;
7. no brittle, heat-damaged, oil-swollen or previously pierced insulation;
8. splice/service-break location outside the hottest or highest-flex zone where practical.

Unknown wire colours are not electrical evidence. Each cavity is identified by function and continuity before integration.

## CKP special rule

The CKP branch is noise critical. If an OEM CKP pigtail is used, preserve the released shield/twisted-pair strategy from the service transition back to the FT550. Keep the transition compact and away from coils, SparkPRO, injector power, starter and pump conductors. Do not ground a cable shield at both ends unless the released CKP shield strategy explicitly requires it.

## Fuel-pump special rule

Fuel-pump feed and dedicated return are frozen at 4.0 mm² per pump. Do not use DTM for the pump-current path. The pump connector must be selected only after the exact pump is verified and must accept the conductor directly or use an approved sealed transition with adequate current, temperature and voltage-drop margin.

The switching architecture remains measurement gated until actual pump steady current and inrush are verified.

## Rev 1 serviceability rule

Where a pigtail strategy is used, the OEM connector must remain replaceable without opening the complete main loom. The service break receives an X-number, cavity map and mating repair lead definition.

## Release states

- `OEM_DEVICE_VERIFIED`
- `OEM_MATING_CONNECTOR_FROZEN`
- `OEM_PIGTAIL_SERVICE_BREAK_FROZEN`
- `PHYSICAL_ID_REQUIRED`
- `DEVICE_SELECTION_GATED`

A circuit may proceed to Rev 1 prototype manufacture using `OEM_PIGTAIL_SERVICE_BREAK_FROZEN`; it does not need a bare OEM housing PN if the validated pigtail is deliberately part of the controlled BOM.

Current state: **OEM_CONNECTOR_STRATEGY_FROZEN / PHYSICAL_IDENTIFICATION_PARTIAL**.
