# Rev 1 Terminal and Conductor Release Gate

## Purpose

This document defines what is frozen now and what must still be proven before the harness BOM can be released for manufacture.

## Frozen now

- PMU-16 output and input cavity map from official PMU-16 Pinout v1.2.
- PMU output current classes: O1/O2/O3/O4/O5/O12/O13/O14/O15/O16 are 25 A class; O6/O7/O8/O9/O10/O11 are 15 A class.
- FT550 known sensor/power/CAN cavities already recorded in the production cavity schedule.
- Low-level sensor/CAN/command conductor design class: 0.35 mm2 / 22 AWG provisional.
- Medium low-current control design class: 0.5 mm2 / 20 AWG provisional.
- Selected ECU/auxiliary supply design class: 0.75 mm2 / 18 AWG provisional where load evidence supports it.
- CKP uses dedicated shielded twisted pair.
- CAN uses dedicated twisted pair with final topology/termination still open.

## Not frozen yet

### High-current PMU outputs

Final wire size for the following cannot be released from PMU output rating alone:

- O1 primary fuel pump;
- O2 secondary fuel pump if fitted;
- O3 radiator fan 1;
- O4 radiator fan 2 if fitted;
- O5 charge/intercooler pump if fitted;
- PMU main battery stud feed.

For each circuit record:

1. steady-state current;
2. startup/inrush current;
3. one-way branch length;
4. acceptable voltage drop;
5. ambient/heat-zone exposure;
6. connector/terminal continuous-current capability.

The conductor is then selected to satisfy the load and terminal, not merely the PMU output maximum.

### Engine-critical actuator wiring

Injector and ignition-coil supply/control sizes remain gated by:

- measured or verified injector current;
- coil electrical type/current profile;
- FT550 output/driver assignment;
- final EPM switching architecture.

### PMU terminal part numbers

The repository currently contains the official PMU cavity map and identifies the Sicma/FCI connector family, but does not yet contain the exact terminal part-number table matched to conductor cross-section.

Therefore no terminal PN is to be guessed.

Before BOM release, populate for every used PMU cavity:

- terminal manufacturer;
- terminal part number;
- supported conductor cross-section;
- seal part number / wire OD range where applicable;
- cavity plug for every unused sealed location;
- approved crimp tooling and inspection criterion.

## Wire construction requirement

Final wire product shall be motorsport/automotive grade with temperature, abrasion, oil/fuel and vibration suitability appropriate to each zone. Exact manufacturer/product series remains open until sourcing is frozen.

## Release rule

A circuit may move from `PROVISIONAL` to `FROZEN` only when:

- conductor size is justified by measured/verified current and route length;
- terminal PN is compatible with that conductor;
- connector rating is adequate;
- protection/current limit coordinates with the conductor and load;
- the production cavity schedule and BOM agree.

No PMU high-current branch or engine-critical supply may be manufactured from a `MEASUREMENT GATED` row.
