# PMU16 Cavity / Terminal / Wire Audit – BD-005

## Purpose

Close the PMU16 connector-production blocker by verifying every used PMU circuit against:

- exact cavity/pin number;
- function/output/input assignment;
- conductor size;
- terminal family;
- terminal wire-range compatibility;
- current class;
- environmental/thermal margin;
- harness-builder crimp tooling.

This audit does not permit a guessed cavity number. Where the exact pin is not yet proven from the controlled ECUMASTER pinout/configuration, the row remains `PINOUT_VERIFY_REQUIRED`.

## Frozen PMU terminal families

The project has already frozen the following Sicma/FCI terminal families for the PMU16 connector system:

- `211CC2S2160P` – 1.5 mm terminal family, low/medium-current circuits;
- `211CC3S2120` – 2.8 mm terminal family, approximately 14–16 AWG class;
- `211CC3S3120` – 2.8 mm terminal family, approximately 10–12 AWG class and candidate for 4.0 mm² conductors.

The exact seal/terminal variant must match the selected wire insulation diameter and the actual cavity in the purchased PMU16 connector shell.

## Audit rules

1. Pinout authority is the exact ECUMASTER PMU16 hardware/version documentation and the released PMU configuration.
2. Wire size authority is the latest project wire-size schedule and final measured load decision.
3. Terminal selection must satisfy both conductor size and current/thermal requirements.
4. A terminal physically accepting the wire is not sufficient evidence of electrical suitability.
5. No conductor may be folded to fit an oversized terminal.
6. No strands may be removed to fit an undersized terminal.
7. High-current terminals adjacent to other loaded terminals require thermal/derating consideration.
8. Unused cavities shall remain empty or be fitted with the correct cavity plug/seal as required by the connector family.
9. The harness builder must use calibrated tooling for the exact terminal family and conductor range.
10. Final release requires a completed cavity-terminal-wire-current audit signed by engineering and manufacturer QA.

## Circuit groups to audit

### High-current / power outputs

- fuel pump output command/power path as selected after BD-001;
- radiator fan output path B11;
- charge-cooler pump output path B12 if fitted;
- boost-control solenoid O6;
- any other PMU high-current auxiliary output used in the released configuration.

### Low-current outputs / commands

- X70 Two-Step relay command O11;
- warning/status outputs where fitted;
- external relay/SSR control outputs if a high-current load is externalised.

### Inputs

- clutch input A6;
- optional clutch Hall/position input if used;
- ignition/master/kill inputs;
- any hardwired pressure/temperature/switch inputs assigned to PMU logic.

### CAN / communications

- PMU CAN-H;
- PMU CAN-L;
- any required module reference/ground associated with service architecture.

### Grounds / supply references

- PMU electronics ground(s);
- PMU main battery stud is outside the multiway terminal audit but must be cross-checked against the primary-power release package.

## Fuel-pump 4.0 mm² rule

The 4.0 mm² fuel-pump feed/return rule remains frozen.

If direct PMU drive is eventually approved, the exact PMU output cavity and its terminal must be proven compatible with:

- 4.0 mm² conductor;
- measured steady current;
- measured inrush current;
- thermal environment;
- adjacent loaded cavities;
- PMU output rating/protection strategy.

If this cannot be proven, use the PMU output only as a low-current command for an external power stage. Do not downsize the pump conductor merely to fit the PMU connector.

## Manufacturer crimp release

Before production crimping, the harness builder shall submit or confirm:

- terminal PN per used PMU cavity;
- conductor PN/size per circuit;
- seal PN where separate;
- crimp tool and die/applicator identification;
- pull-test capability;
- sample crimp photographs or first-article crimp inspection where requested.

## Acceptance criteria

Every used PMU cavity must resolve to exactly one controlled combination:

`PMU cavity → circuit ID → function → conductor size → terminal PN → seal → tooling → current class → PASS`

Any row with `TBD`, `VERIFY`, `UNKNOWN`, or conflicting source data remains a manufacturing blocker.

## Release state

Current state:

`PMU_CAVITY_TERMINAL_AUDIT_FRAMEWORK_FROZEN`

Final state after exact pinout/cavity verification:

`PMU_CAVITY_TERMINAL_WIRE_AUDIT_PASS`

BD-005 closes only after every used PMU cavity is PASS or explicitly DNP.
