# Splice and Ground Reference

## Sensor-domain splices

| ID | Function | Conductors | Rule |
|---|---|---|---|
| SP-S01 | FT550 5 V sensor reference distribution | TPS 5 V, OEM MAP 5 V and any later verified 5 V OEM sensor | Fed only from the verified FT550 5 V reference cavity. No PMU +5 V connection. |
| SP-S02 | FT550 sensor return distribution | TPS return, MAP return, ECT return, IAT return and any later verified analogue sensor return | Return only to verified FT550 sensor-ground cavity/cavities. Never bonded to PMU output return or frame downstream. |
| SP-S03 | VSS supply branch | protected switched 12 V to VSS | Protection source and PMU channel remain VERIFY until current/topology are confirmed. |

## Power-domain junctions

| ID | Function | Design intent |
|---|---|---|
| J-P01 | Main battery positive distribution | Feeds PMU-16 main power and separately protected engine-management/EPM feed as finally released. Conductor and master protection VERIFY. |
| J-P02 | Engine/battery negative star | Low-resistance common reference connecting battery negative, engine case, FT550 power grounds and PMU ground as required by manufacturer instructions. |
| J-P03 | Injector switched supply splice | Common protected +12 V feed to front/rear injectors if compatible with final architecture. Current and protection VERIFY. |
| J-P04 | Coil switched supply splice | Common protected +12 V feed to front/rear coils if compatible with final architecture. Current, driver and protection VERIFY. |

## Grounds

| ID | Ground | Allowed loads | Prohibited loads |
|---|---|---|---|
| G01 | Battery negative / engine star | FT550 power grounds, PMU ground, engine block/battery bonding | Sensor returns must not terminate here individually |
| G02 | FT550 sensor return network | OEM TPS/MAP/ECT/IAT and other verified sensor returns | Pumps, fans, coils, injectors, starter, PMU high-current loads |
| G03 | Chassis auxiliary ground | Lamps/service accessories where appropriate | Precision sensor returns and CKP reference |

## CKP shield

CKP 32313-01A receives a dedicated twisted pair from X10 to the FT550. Shield termination remains `VERIFY` until the exact FuelTech recommendation for the installed harness is confirmed. Do not ground the shield at both ends by default.

## Splice construction rule

Production splice method must be selected and documented before release. Preferred implementation is a sealed motorsport splice/crimp or welded splice with strain relief and adhesive-lined sealing, sized to the conductor bundle. Unsealed household-style joints are not permitted.
