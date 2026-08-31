# Sheet 04 - ECUMASTER PMU-16 Power Distribution

## Role

The PMU-16 is the high-current auxiliary power-distribution backbone. It replaces conventional relay/fuse branches for non-precision loads while adding current measurement and programmable protection.

## Official pin-level freeze

The PMU-16 39-pin connector map is now verified from ECUMASTER PMU-16 / PMU-16 DL Pinout v1.2 (2025-04-16) and stored in `docs/ECUMASTER-PMU16/PMU16-Pinout-v1.2.csv`.

### Frozen output allocation

| Output | Connector pin | Rating class | Project function | Status |
|---|---:|---:|---|---|
| O1 | 38 | 25 A | Primary fuel pump | VERIFIED PIN / DESIGN FUNCTION |
| O2 | 39 | 25 A | Secondary/staged fuel pump | VERIFIED PIN / DNP if not fitted |
| O3 | 26 | 25 A | Radiator fan 1 | VERIFIED PIN / DESIGN FUNCTION |
| O4 | 13 | 25 A | Radiator fan 2 | VERIFIED PIN / DNP if not fitted |
| O5 | 12 | 25 A | Charge/intercooler pump | VERIFIED PIN / DNP if not fitted |
| O6 | 11 | 15 A | Boost-control solenoid +12 V | VERIFIED PIN / DESIGN FUNCTION |
| O7 | 10 | 15 A | Auxiliary coolant/race pump | VERIFIED PIN / RESERVED |
| O8 | 9 | 15 A | Warning/fault lamp | VERIFIED PIN / DESIGN FUNCTION |
| O9 | 5 | 15 A | Race accessory feed | VERIFIED PIN / RESERVED |
| O10 | 4 | 15 A | Logger/display/service feed | VERIFIED PIN / DESIGN FUNCTION |
| O11 | 3 | 15 A | Spare | VERIFIED PIN / RESERVED |
| O12 | 2 | 25 A | Spare | VERIFIED PIN / RESERVED |
| O13 | 1 | 25 A | Spare | VERIFIED PIN / RESERVED |
| O14 | 14 | 25 A | Spare | VERIFIED PIN / RESERVED |
| O15 | 27 | 25 A | Spare | VERIFIED PIN / RESERVED |
| O16 | 28 | 25 A | Spare | VERIFIED PIN / RESERVED |

## Frozen PMU input allocation

| Input | Connector pin | Project function | Status |
|---|---:|---|---|
| A1 | 29 | Master enable / ignition request | VERIFIED PIN / DESIGN FUNCTION |
| A2 | 16 | Start request | VERIFIED PIN / DESIGN FUNCTION |
| A3 | 30 | Kill / emergency torque-disable request | VERIFIED PIN / DESIGN FUNCTION |
| A4 | 17 | Fan manual override | VERIFIED PIN / DESIGN FUNCTION |
| A5 | 31 | Service/test mode | VERIFIED PIN / DESIGN FUNCTION |
| A6 | 18 | Reserved | VERIFIED PIN |
| A7 | 32 | Reserved | VERIFIED PIN |
| A8 | 19 | Reserved | VERIFIED PIN |
| A9 | 6 | Reserved | VERIFIED PIN |
| A10 | 33 | Reserved | VERIFIED PIN |
| A11 | 20 | Reserved | VERIFIED PIN |
| A12 | 34 | Reserved | VERIFIED PIN |
| A13 | 21 | Reserved | VERIFIED PIN |
| A14 | 8 | Reserved | VERIFIED PIN |
| A15 | 35 | Reserved | VERIFIED PIN |
| A16 | 22 | Reserved | VERIFIED PIN |

## Power and communication pins

- Pin 7: +12 V switched input.
- Pin 15: +5 V output, up to 500 mA.
- Pin 25: device ground.
- Main +12 V battery feed: centre stud, maximum constant current 150 A.
- Pin 23: CAN1H, fixed 1 Mbps.
- Pin 36: CAN1L, fixed 1 Mbps.
- Pin 24: CAN2H, configurable 125/250/500/1000 kbps.
- Pin 37: CAN2L, configurable 125/250/500/1000 kbps.

CAN1 has no internal termination resistor and requires external termination. CAN2 has software-controlled termination.

## CAN architecture

For this project, CAN2 is the preferred candidate for FT550-to-PMU communications because its speed is configurable. CAN1 remains important for PC/peripheral communication at fixed 1 Mbps. Final bus assignment still requires verified FT550 CAN compatibility and the final topology.

No CAN identifiers or payloads are invented in this repository.

## Output electrical classes

- O1-O5 and O12-O16: 25 A maximum constant current per output class.
- O6-O11: 15 A maximum constant current per output class.
- All outputs still require actual load-current and inrush measurement before current-limit configuration is released.

These ratings are output hardware limits, not permission to size conductors or protection blindly to those values.

## Terminal family

Official pinout specifies a Sicma / FCI 39-position connector family with:

- 1.5 mm terminal 211CC2S2160P, 14-17 AWG;
- 2.8 mm terminal 211CC3S2120, 14-16 AWG;
- 2.8 mm terminal 211CC3S3120, 10-12 AWG.

Final terminal choice per cavity must follow the PMU pinout/device terminal arrangement and actual conductor requirement.

## Protection setup

For every populated output, measure actual steady current and inrush. Then configure current limits, trip thresholds, retry timing and retry count using the ECUMASTER manual and measured load evidence. Generic current guesses are not permitted in the released configuration.
