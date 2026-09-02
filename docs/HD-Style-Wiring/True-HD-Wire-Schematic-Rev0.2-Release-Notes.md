# True HD Wire-by-Wire Schematic Set Rev 0.2

## Purpose

Replace the earlier block-diagram emphasis with a conductor-level Harley-Davidson-style harness schematic set.

## Wire accountability

Source authority: `docs/Harness-Manufacturer-Release-Pack/Production-Wire-Circuit-Master-Schedule.csv`.

- Production conductor rows: **53**
- Conductors assigned to a primary schematic sheet: **53**
- Orphan conductors: **0**

Each conductor is identified by its production `Circuit_ID`, wire size, source, destination and release/evidence state.

## Sheet set

1. Legend, release rules and wire accountability
2. Master power, distribution and ground structure
3. Trigger, OEM sensors and precision reference wiring
4. Injection harness - B39, X62/X63 and front/rear injectors
5. Ignition harness - B40, SparkPRO and front/rear coils
6. Fuel pump harness - every high-current conductor
7. Cooling and auxiliary high-current harness
8. CAN backbone and X51 service harness
9. Clutch / X70 Two-Step harness
10. X50 engineering service and controlled expansion
11. Production Wire Ledger 1 of 3
12. Production Wire Ledger 2 of 3
13. Production Wire Ledger 3 of 3

## Authority / conflict policy

1. Production Wire Circuit Master Schedule controls Circuit_ID and conductor existence.
2. Connector / Cavity Master Schedule supplies cavity evidence when current and internally consistent.
3. Verified PMU16 pinout controls PMU physical pin capability.
4. Later explicit hardware freezes override older architecture concepts.
5. `TBD`, `VERIFY`, `PHYSICAL_ID_REQUIRED`, `DFM_GATED` and `EVIDENCE_GATED` remain visible and are not replaced with guesses.

## Locked requirements carried into Rev 0.2

- Pump 1 feed: minimum 4.0 mm2.
- Pump 1 dedicated return: minimum 4.0 mm2.
- Pump 2 feed: minimum 4.0 mm2.
- Pump 2 dedicated return: minimum 4.0 mm2.
- B15 PMU primary feed: 10.0 mm2 baseline, final protection evidence gated.
- FT550 sensor ground remains a precision measurement return and must not carry pump/fan/coil high-current return.
- FT550 A21 is a ground-active dry-contact Two-Step input; +12 V is prohibited.
- Current Two-Step hardware is PMU O11 -> TE 1393292-5 relay -> isolated NO contact -> FT550 A21.
- CAN baseline is FT550 CAN A -> PMU CAN2 at 1 Mbps, linear trunk, short X51 stub, exactly two end terminations.

## Current limitations

This drawing set is conductor-complete relative to the current Production Wire Master Schedule, but it is **not yet a fully manufacturing-released harness** because several connector cavities, terminal part numbers, physical branch lengths, protection values and load-dependent architecture decisions remain evidence gated.

Promotion to Rev 1.0 manufacturer construction drawings requires closure of those physical evidence items and regeneration from the frozen schedules.
