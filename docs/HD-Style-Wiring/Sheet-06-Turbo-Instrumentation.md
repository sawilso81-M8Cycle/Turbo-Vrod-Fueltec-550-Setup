# Sheet 06 - Turbo Instrumentation

## Purpose

This sheet extends the Rev 0 HD-style harness to support additional turbo-engine protection and development sensors while preserving the OEM Harley sensor baseline.

## Mandatory added sensors

### Fuel pressure transducer

- Supply: FT550 5 V sensor reference, subject to selected sensor compatibility.
- Return: FT550 precision sensor return.
- Signal: spare FT550 analogue input, exact cavity `VERIFY`.
- Mounting: fuel rail or pressure reference point representative of injector rail pressure.
- Primary calculation: fuel differential pressure = rail pressure - manifold pressure.

### Engine oil pressure transducer

- Supply: FT550 5 V sensor reference, subject to selected sensor compatibility.
- Return: FT550 precision sensor return.
- Signal: spare FT550 analogue input, exact cavity `VERIFY`.
- Mounting: main engine oil gallery.
- OEM oil-pressure switch remains installed unless deliberately removed later.

### Post-intercooler IAT

- Location: downstream of compression/intercooling and upstream of the cylinders.
- Purpose: actual charge-temperature measurement for ignition/boost protection.
- Supply/return/input: defined by selected sensor; FT550-compatible input `VERIFY`.
- OEM IAT remains installed as an independent reference channel where practical.

### Wideband lambda front/rear

Preferred architecture:

- one wideband sensor per cylinder;
- controller or CAN interface selected to be FuelTech-compatible;
- avoid unnecessary analogue conversion where a verified digital/CAN path is available;
- exact CAN or input allocation remains `VERIFY` until hardware selection.

## Recommended turbo-health sensors

### Front/rear EGT

Use a dedicated EGT interface/module appropriate to thermocouple inputs. Do not connect K-type probes directly to ordinary analogue inputs.

### Turbo oil pressure

Use where the turbo oil feed includes a restrictor/filter or otherwise warrants independent confirmation.

### Crankcase pressure

Use a low-range bidirectional/positive pressure sensor appropriate to the expected crankcase operating range.

### EMAP

Measure pre-turbine exhaust manifold pressure through suitable high-temperature isolation/conditioning hardware. The pressure transducer itself should not be directly exposed to exhaust temperature beyond its rating.

### Wastegate/dome pressure

Add only if dome-pressure or CO2-assisted boost control is fitted.

### Turbo shaft speed

Requires compatible turbo-speed pickup and signal-conditioning hardware. Input method remains `VERIFY` until sensor/controller selection.

## Drag-development channels

- front wheel speed;
- gear position;
- IMU;
- brake pressure;
- suspension position;
- compressor outlet pressure.

These should not displace mandatory protection channels if FT550 input capacity becomes constrained. A CAN expansion/logger module is preferred for lower-priority development channels where appropriate.

## New harness branch IDs

- B17 - fuel pressure
- B18 - engine oil pressure
- B19 - post-IC IAT
- B20 - front lambda
- B21 - rear lambda
- B22 - front EGT
- B23 - rear EGT
- B24 - turbo oil pressure
- B25 - crankcase pressure
- B26 - EMAP
- B27 - dome pressure
- B28 - turbo speed
- B29 - front wheel speed
- B30 - gear position
- B31 - IMU / expansion CAN

## Sensor-reference rule

Do not power these sensors from PMU-16 +5 V merely because that output exists. Precision engine-management sensors should use the FT550 reference/return architecture unless the selected sensor/controller manufacturer explicitly requires another supply method.

## Input-capacity gate

Before freezing Rev 1, perform an FT550 input-capacity audit covering:

1. all retained OEM sensors;
2. all mandatory added sensors;
3. dual lambda interface requirements;
4. EGT interface requirements;
5. remaining analogue/digital/frequency inputs;
6. CAN expansion options.

Any development-only sensor that cannot be accommodated without compromising engine protection moves to a dedicated CAN logger/expansion module.
