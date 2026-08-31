# Sheet 06 - Turbo Instrumentation

## Purpose

This sheet extends the Rev 0 HD-style harness to support additional turbo-engine protection and development sensors while preserving the OEM Harley sensor baseline.

## FT550 input-capacity result

The input-capacity audit is now complete at architecture level.

Direct FT550 resources are reserved first for engine-protection channels. Development instrumentation is moved to CAN expansion/logger unless it must participate in active FT550 control.

Reference:

- `../Sensor-Expansion/FT550-Input-Capacity-Audit.md`
- `../Sensor-Expansion/FT550-Input-Allocation.csv`

### Direct FT550 reservation order

1. Existing core engine inputs: CKP, TPS, ECT, VSS and OEM IAT.
2. Fuel-pressure transducer.
3. Engine oil-pressure transducer.
4. Post-intercooler IAT.
5. OEM MAP retained as requested.
6. Any additional channel proven necessary for direct FT550 control/protection.

The FT550 internal 7-bar MAP uses no external analogue cavity and remains available as the turbo-capable manifold/boost reference.

## Mandatory added sensors

### Fuel pressure transducer

- Supply: FT550 5 V sensor reference, subject to selected sensor compatibility.
- Return: FT550 precision sensor return.
- Signal: **reserved direct FT550 analogue input**, exact cavity `VERIFY`.
- Mounting: fuel rail or pressure reference point representative of injector rail pressure.
- Primary calculation: fuel differential pressure = rail pressure - manifold pressure.

### Engine oil pressure transducer

- Supply: FT550 5 V sensor reference, subject to selected sensor compatibility.
- Return: FT550 precision sensor return.
- Signal: **reserved direct FT550 analogue input**, exact cavity `VERIFY`.
- Mounting: main engine oil gallery.
- OEM oil-pressure switch remains installed as an independent simple path unless deliberately removed later.

### Post-intercooler IAT

- Location: downstream of compression/intercooling and upstream of the cylinders.
- Purpose: actual charge-temperature measurement for ignition/boost protection.
- Signal: **reserved direct FT550 compatible input**, exact cavity `VERIFY`.
- OEM IAT remains installed as an independent reference channel where practical.

### OEM MAP

- Original Harley MAP hardware remains part of the harness as requested.
- Exact FT550 analogue cavity remains `VERIFY`.
- The OEM MAP may be used for plausibility/reference within its verified operating range.
- It does not replace the FT550 internal 7-bar MAP for turbo-range protection.

### Wideband lambda front/rear

Preferred architecture:

- one wideband sensor per cylinder;
- verified FuelTech-compatible digital/CAN interface;
- do not consume two generic analogue inputs unless the selected hardware requires it;
- exact CAN or input allocation remains `VERIFY` until hardware selection.

## Tier 2 channels - direct only when control requires it

These default to expansion/logger but may move directly to FT550 when active control requires the channel:

- wastegate/dome pressure;
- turbo shaft speed;
- gear position;
- front wheel speed;
- turbo oil pressure;
- crankcase pressure.

## Tier 3 channels - expansion/logger preferred

- front EGT;
- rear EGT;
- EMAP;
- intercooler coolant temperature;
- IMU;
- brake pressure;
- suspension position;
- compressor outlet pressure.

Front/rear EGT require an appropriate thermocouple interface. K-type probes must not be wired directly to ordinary analogue inputs.

## Harness branch IDs

- B17 - fuel pressure, direct FT550 reserved
- B18 - engine oil pressure, direct FT550 reserved
- B19 - post-IC IAT, direct FT550 reserved
- B20 - front lambda interface
- B21 - rear lambda interface
- B22 - front EGT / expansion
- B23 - rear EGT / expansion
- B24 - turbo oil pressure
- B25 - crankcase pressure
- B26 - EMAP / expansion
- B27 - dome pressure
- B28 - turbo speed
- B29 - front wheel speed
- B30 - gear position
- B31 - expansion CAN / IMU / logger backbone

## Sensor-reference rule

Do not power added precision sensors from PMU-16 +5 V merely because that output exists. Precision engine-management sensors should use the FT550 reference/return architecture unless the selected sensor/controller manufacturer explicitly requires another supply method.

## Remaining release gate

The architecture allocation is frozen, but the exact spare FT550 analogue/digital/frequency cavities are not yet present as verified repository data.

Rev 1 therefore still requires:

1. exact FT550 spare-input cavity inventory;
2. fuel-pressure input cavity;
3. oil-pressure input cavity;
4. post-IC IAT cavity;
5. OEM MAP cavity;
6. verified dual-lambda interface;
7. decision on which Tier 2 channels require direct FT550 access;
8. selection of the CAN expansion/logger for Tier 3 channels.

No spare cavity is to be invented to satisfy the drawing.
