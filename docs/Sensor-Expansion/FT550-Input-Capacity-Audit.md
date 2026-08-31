# FT550 Input Capacity Audit

## Purpose

This audit decides which sensor channels must terminate directly at the FuelTech FT550 and which channels should be assigned to CAN expansion or a dedicated logger so engine-protection inputs are never displaced by development instrumentation.

## Repository-grounded baseline

Known direct FT550 assignments already recorded in this repository:

- A18 - CKP reference
- A19 - CKP signal
- A22 - OEM TPS
- A24 - OEM ECT
- A26 - OEM VSS
- B5 - OEM IAT

The following retained OEM functions still require exact FT550 input assignment:

- OEM MAP
- OEM oil-pressure switch
- OEM neutral switch

The FT550 internal 7-bar MAP requires no external analogue-input cavity.

## Allocation rule

Direct FT550 inputs are reserved in this order:

1. engine position / core control inputs;
2. engine-protection sensors that must remain available even if CAN expansion is lost;
3. vehicle-state inputs needed by FT550 control strategy;
4. turbo-health channels where direct ECU protection is materially beneficial;
5. development / logging-only channels.

## Tier 1 - retain directly on FT550

| Channel | Reason | Working allocation state |
|---|---|---|
| CKP | engine position | A18/A19 already recorded |
| OEM TPS | load/rider demand | A22 already recorded |
| OEM ECT | engine thermal protection | A24 already recorded |
| OEM VSS | speed / strategy | A26 already recorded |
| OEM IAT | OEM reference channel | B5 already recorded |
| Fuel pressure | direct differential-fuel-pressure protection | exact spare analogue cavity VERIFY |
| Engine oil pressure | direct engine protection | exact spare analogue cavity VERIFY |
| Post-intercooler IAT | direct charge-temperature protection | exact compatible input VERIFY |
| OEM MAP | retain requested OEM hardware and plausibility reference | exact analogue cavity VERIFY |

## Tier 2 - direct FT550 only when needed for active control/protection

| Channel | Default destination | Move direct to FT550 when... |
|---|---|---|
| Wastegate/dome pressure | FT550 or verified expansion | dome-pressure control requires it |
| Turbo shaft speed | conditioned frequency/CAN | FT550 can directly enforce verified overspeed strategy |
| Gear position | FT550 or expansion | gear-based boost/ignition strategy requires direct ECU availability |
| Front wheel speed | expansion/logger preferred | FT550 traction/launch logic specifically requires direct channel |
| Turbo oil pressure | expansion acceptable | it is promoted from monitoring to direct protection |
| Crankcase pressure | expansion/logger preferred | protection envelope is validated and direct action is required |

## Tier 3 - preferred CAN expansion / logger

These should not consume scarce direct FT550 inputs unless a later control requirement justifies it:

- front EGT;
- rear EGT;
- EMAP;
- intercooler coolant temperature;
- IMU;
- brake pressure;
- suspension travel;
- compressor outlet pressure;
- other development channels.

EGT requires an appropriate thermocouple interface regardless of final transport method.

## Lambda strategy

Front and rear wideband lambda remain mandatory, but the preferred architecture is a verified FuelTech-compatible digital/CAN solution rather than consuming two generic analogue inputs. Exact hardware and communications remain a release blocker until selected and verified.

## Result

The design can proceed without assuming that every sensor must physically enter the FT550 connector.

The minimum direct-input expansion above the OEM baseline is:

- fuel pressure;
- engine oil pressure;
- post-intercooler IAT;
- OEM MAP input if retained as an active FT550 channel.

Everything else is evaluated against control/protection need before being granted a direct FT550 resource.

## Remaining capacity blocker

The repository does not yet contain a verified complete FT550 input/cavity inventory sufficient to name the exact spare analogue, digital and frequency cavities for all of the above channels. Therefore no spare cavity is invented here.

Before Rev 1 harness release:

1. import/record the exact FT550 connector input inventory from the authorised manufacturer reference;
2. mark which cavities are consumed by the existing V-Rod installation;
3. allocate fuel pressure, oil pressure, post-IC IAT and OEM MAP first;
4. verify lambda CAN/digital architecture;
5. allocate remaining direct-control channels;
6. route Tier 3 channels to expansion/logger.
