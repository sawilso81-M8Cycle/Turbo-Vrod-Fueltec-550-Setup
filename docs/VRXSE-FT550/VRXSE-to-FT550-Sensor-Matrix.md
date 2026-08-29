# VRXSE Destroyer to FuelTech FT550 Sensor Matrix

This is the working engineering cross-reference between the 2006 Harley-Davidson VRXSE Destroyer / common VRSC engine sensor circuits and the FuelTech FT550.

> **Important:** This matrix is not permission to energise a harness. Verify exact cavity numbers, wire colours, polarity, sensor calibration and the current FT550 manual before final termination.

## Primary sensor matrix

| Function | Harley component / wiring | OEM circuit information | Proposed FT550 destination | Domain | Status / action |
|---|---|---|---|---|---|
| **Crank position (CKP)** | 32313-01A; R + BK at connector [79] | Working cross-reference: ECM 30 CKP+ / ECM 12 CKP- | **A19 RPM+ / A18 RPM reference-** | SIM | Scope polarity and waveform during cranking before ignition enable |
| **Throttle position (TPS)** | 27975-01; GY/V signal, R/W 5 V, BK/W sensor return at [88] | Working cross-reference: ECM 24 signal / 14 supply / 26 sensor return | **A22 White #3 TPS**, FT550 5 V reference and sensor ground | SIM | Verify transfer curve, closed and WOT voltages |
| **MAP** | 32416-10; V/W signal, R/W 5 V, BK/W sensor return at [80] | Working cross-reference: ECM 25 signal / 14 supply / 26 sensor return | Prefer **FT550 internal 7-bar MAP** as primary load sensor | SIM | Retain OEM MAP only as optional reference/diagnostic input after calibration is verified |
| **Coolant temperature (ECT)** | 32315-01; PK/Y signal + BK/W sensor return at [90] | Working cross-reference: ECM 6 signal / 26 sensor return | **A24 White #5 H2O** + FT550 sensor ground | SIM | Verify thermistor curve before relying on displayed temperature |
| **Intake air temperature (IAT)** | 27388-01; LGN/Y signal + BK/W sensor return at [89] | Working cross-reference: ECM 7 signal / 26 sensor return | **B5 White #8 IAT** + FT550 sensor ground | SIM | Verify calibration curve and sensor placement for boosted application |
| **Vehicle speed sensor (VSS)** | 74402-05B; BK/R +12 V, BK/BE output, BK ground at [65] | Working cross-reference: ECM 33 speed signal | **A26 White #7 Speed** | SIM | Confirm pulse form, amplitude and pulses/revolution before configuration |
| **Oil pressure switch** | 26561-99; GN/Y at [120] | OEM warning/switch circuit | Spare FT digital input if required | SIM | Strong recommendation: add true pressure transducer for engine protection |
| **Neutral switch** | 33902-98A; [131] | OEM switch circuit | Spare FT digital input | SIM | Verify whether switched-to-ground and required pull-up strategy |
| **Cam sync** | No OEM sensor identified | None identified in reviewed VRXSE/2006 control information | Leave FT550 cam input unused unless engineered sensor is added | SIM | Treat as crank-only until proven otherwise |

## Additional turbo sensors recommended

These are not necessarily OEM Destroyer sensors, but are recommended for a serious turbo FT550 installation.

| Sensor | Purpose | Preferred domain | Recommendation |
|---|---|---|---|
| Fuel pressure transducer | Differential fuel-pressure monitoring and protection | SIM | High priority |
| Engine oil pressure transducer | Real pressure logging and shutdown strategy | SIM | High priority |
| Boost / manifold pressure | Primary engine load | SIM | Use FT550 internal 7-bar MAP with dedicated manifold reference |
| Exhaust lambda / wideband O2 | Closed-loop mixture control and logging | SIM / communications | Use FuelTech-compatible wideband system per manufacturer requirements |
| Turbo oil pressure, if separate circuit | Turbo lubrication protection | SIM | Recommended where turbo supply merits independent monitoring |
| Wastegate dome / CO2 pressure, if used | Closed-loop boost-control reference | SIM | Add only if boost strategy requires it |
| EGT front cylinder | Cylinder thermal comparison | SIM | Optional but valuable for development |
| EGT rear cylinder | Cylinder thermal comparison | SIM | Optional but valuable for development |

## FT550 working pin assignments used in this project

The current working design uses the following FT550 inputs from the FuelTech PROBIKE / FT550 documentation:

- **A18**: VR crank reference / RPM-
- **A19**: VR crank signal / RPM+
- **A22 / White #3**: TPS
- **A24 / White #5**: engine coolant / H2O temperature
- **A26 / White #7**: speed input
- **B5 / White #8**: intake air temperature

These remain subject to final verification against the exact harness and manual revision physically used on the bike.

## Sensor supply philosophy

Do not reuse the Harley sensor-ground network as a generic chassis earth.

TPS, ECT, IAT and any retained analogue MAP/reference sensors should be wired through the **SIM precision sensor network** and returned to the FT550-designated sensor ground/reference according to FuelTech requirements.

The following must not share uncontrolled return paths with precision sensor grounds:

- fuel pumps;
- cooling fans;
- ignition coils;
- injectors;
- boost-control solenoids;
- starter circuits;
- other high-current PWM or relay loads.

## Required verification before harness freeze

For every row above record:

1. Harley connector number.
2. Harley connector cavity.
3. wire colour.
4. sensor part number.
5. sensor electrical type.
6. supply voltage.
7. output range / transfer curve.
8. polarity.
9. FT550 connector and cavity.
10. FuelTech wire colour.
11. SIM terminal number.
12. shield/twist requirement.
13. fuse/protection requirement if powered.
14. bench-test result.
15. engine-running validation result.

A production drawing should not contain unresolved `VERIFY` items.
