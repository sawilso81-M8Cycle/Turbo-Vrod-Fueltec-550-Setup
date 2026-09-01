# FTCAN 2.0 -> ECUMASTER PMU-16 Implementation

## Milestone status

The application-layer protocol is now defined far enough to build PMU Client receive channels for the core engine signals without guessing byte locations.

FuelTech FTCAN 2.0 provides fixed 100 Hz simple real-time broadcasts using MessageIDs 0x600, 0x601 and 0x602. All simple-frame values are signed 16-bit, big-endian.

For the FT550/FT600 family, the working arbitration IDs expected with ProductID 0x5020 / unique ID 0 are:

- 0x14080600
- 0x14080601
- 0x14080602

These arbitration IDs must still be confirmed by a live FT550 CAN capture because the FTCAN ProductID includes a configurable/assigned unique identifier. PMU logic shall not assume unique ID 0 until captured.

## Fixed simple broadcast map

### MessageID 0x600

| Bytes | Signal | Scaling |
|---|---|---|
| 0-1 | TPS | raw * 0.1 % |
| 2-3 | MAP | raw * 0.001 bar |
| 4-5 | Air temperature | raw * 0.1 C |
| 6-7 | Engine temperature | raw * 0.1 C |

### MessageID 0x601

| Bytes | Signal | Scaling |
|---|---|---|
| 0-1 | Oil pressure | raw * 0.001 bar |
| 2-3 | Fuel pressure | raw * 0.001 bar |
| 4-5 | Water pressure | raw * 0.001 bar |
| 6-7 | Gear | FuelTech Note 2 encoding |

### MessageID 0x602

| Bytes | Signal | Scaling |
|---|---|---|
| 0-1 | O2 | raw * 0.001 lambda |
| 2-3 | ECU RPM | raw * 1 rpm |
| 4-5 | Oil temperature | protocol-defined temperature scaling |
| 6-7 | PitLimit switch | protocol-defined state encoding |

## Tagged real-time MeasureIDs

The FTCAN tagged real-time broadcasts carry repeating 4-byte records:

- MeasureID: unsigned 16-bit big-endian
- value/status: signed/unsigned 16-bit big-endian as defined by the protocol

The least-significant bit of MeasureID indicates value versus status. The data identifier is MeasureID >> 1.

Core verified MeasureIDs relevant to this project include:

| MeasureID | Signal | Scaling |
|---|---|---|
| 0x0002 | TPS | 0.1 % |
| 0x0004 | MAP | 0.001 bar |
| 0x0006 | Air temperature | 0.1 C |
| 0x0008 | Engine temperature | 0.1 C |
| 0x000A | Oil pressure | 0.001 bar |
| 0x000C | Fuel pressure | 0.001 bar |
| 0x0012 | ECU battery voltage | 0.01 V |
| 0x0022 | Gear | FuelTech Note 2 |
| 0x0084 | ECU RPM | 1 rpm |

The simple broadcasts are preferred in PMU Client for signals they contain because their byte locations are fixed and the frame rate is 100 Hz. Tagged parsing should be added only for data absent from 0x600-0x602, beginning with battery voltage.

## PMU Client channel plan

Create separate value and validity variables. Recommended names:

- FT_RPM / FT_RPM_VALID
- FT_TPS / FT_TPS_VALID
- FT_MAP_BAR / FT_MAP_VALID
- FT_ECT_C / FT_ECT_VALID
- FT_OILP_BAR / FT_OILP_VALID
- FT_FUELP_BAR / FT_FUELP_VALID
- FT_GEAR / FT_GEAR_VALID
- FT_BATTV / FT_BATTV_VALID

Never use a stale value simply because the numeric variable retains its last decoded value.

## Timeouts

Use the existing project signal dictionary as the initial timeout policy:

- RPM/TPS/MAP/fuel pressure/oil pressure: 250 ms
- ECT/gear/battery voltage: 1000 ms

These are project safety-policy values, not FuelTech protocol requirements.

## Source filtering

FTCAN arbitration IDs contain ProductID, DataFieldID and MessageID. The PMU configuration must accept the actual FT550 ProductID observed on the motorcycle, not an arbitrary FuelTech transmitter that happens to send the same MeasureID.

Before Rev 1 release:

1. Capture the live FT550 at 1 Mbps.
2. Record its ProductID/unique identifier.
3. Confirm simple frames 0x600-0x602 and their observed arbitration IDs.
4. Compare decoded RPM/TPS/MAP/ECT against FTManager values.
5. Confirm oil/fuel pressure scaling with known values.
6. Confirm gear encoding on the installed configuration.
7. Implement battery voltage from tagged MeasureID 0x0012 if required.
8. Do not implement ECU warning/fault state until its exact public protocol definition is verified.

## Safety rule

CAN values assist PMU logic but do not replace hardwired master/kill/start safety paths. Any CAN timeout must produce the fallback already documented in the project signal dictionary.
