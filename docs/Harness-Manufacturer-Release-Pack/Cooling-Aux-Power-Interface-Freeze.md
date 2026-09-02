# Radiator Fan + Charge-Cooler Pump Power Interface Freeze – Rev 1

## Purpose

Freeze the harness-side architecture for B11 radiator fan and B12 charge/intercooler pump while keeping final conductor and protection values tied to the actual selected devices and measured inrush current.

## Design principle

Do not copy the 4.0 mm² fuel-pump architecture by default. These loads shall be sized from real current, route length, voltage-drop target, PMU output capability, connector/terminal current capability and thermal environment.

## B11 radiator fan

Current prototype baseline:

- branch ID: B11;
- approximate routed length: 950 mm;
- first-cut length: 1100 mm;
- provisional conductor: 2.5 mm² feed and matched return where a dedicated return is used;
- control/output: PMU O3 baseline;
- final status: MEASUREMENT GATED.

### B11 release rule

2.5 mm² is retained as the Rev 1 prototype baseline until fan PN and current data are available. Final production sizing shall be calculated from measured steady current and worst-case start/inrush current at operating voltage and representative temperature.

If O3 current/thermal capability is insufficient for the selected fan, O3 becomes a control output for an external relay/SSR/power stage. The main harness branch remains modular so this change does not require redesign of upstream signal logic.

### B11 service connector

Use a sealed 2-way automotive connector whose contacts:

- accept the final conductor size without folding strands;
- carry measured steady current with thermal margin;
- tolerate fan start/inrush current;
- are keyed and polarity controlled;
- provide positive secondary lock/CPA where the selected family supports it;
- are located away from direct radiator/exhaust heat and water spray where practical.

Preferred family class: Deutsch DT, TE HDSCS/MCP, or an OEM-equivalent sealed high-current 2-way family selected to match actual fan current and wire size.

Do not freeze DTM or Superseal 1.5 for B11 if final current/wire size exceeds their verified capability.

## B12 charge/intercooler pump

Current prototype baseline:

- branch ID: B12;
- approximate routed length: 850 mm;
- first-cut length: 1000 mm;
- provisional conductor: 2.0 mm² feed and matched return where a dedicated return is used;
- control/output: PMU O5 baseline;
- build state: DNP unless a charge/intercooler pump is actually fitted.

### B12 release rule

If the system is not fitted, B12 shall be marked DNP throughout the build record, connector schedule, formboard and acceptance test.

If fitted, 2.0 mm² remains a prototype baseline only. Final wire and connector selection require the actual pump PN, measured/datasheet steady current, inrush current, duty cycle, route length, ambient temperature and PMU O5 capability.

If O5 cannot comfortably switch the selected pump, O5 becomes a control output for an external relay/SSR/power stage.

### B12 service connector

Use a sealed 2-way automotive connector selected from the actual pump current class. A smaller connector family may be used than the fuel-pump interface if verified current and conductor size support it, but the connector may not become the lowest-rated element in the circuit.

## Protection coordination

For both B11 and B12, final electronic current limit/fuse/relay protection shall be coordinated to:

1. measured normal operating current;
2. measured start/inrush current;
3. conductor ampacity and loom derating;
4. connector/terminal continuous-current capability;
5. PMU output capability if directly driven;
6. voltage-drop target;
7. nuisance-trip avoidance;
8. fail-safe behavior.

Protection shall not be selected simply by matching a guessed motor current.

## Grounding

Where a dedicated return is used, size it to the same current class as the feed unless a documented calculation supports a different architecture. Do not route fan/pump load current through sensor/reference ground circuits.

## Harness modularity

B11 and B12 shall terminate at serviceable connectors or controlled pigtails so a future fan/pump replacement can be accommodated without cutting the main loom.

Preferred structure:

`PMU/direct or external power stage -> main branch -> sealed service break -> short device-specific pigtail -> fan/pump`

## Final release states

B11 must finish as one of:

- `B11_DIRECT_PMU_DRIVE_APPROVED`
- `B11_EXTERNAL_POWER_STAGE_REQUIRED`

B12 must finish as one of:

- `B12_DNP`
- `B12_DIRECT_PMU_DRIVE_APPROVED`
- `B12_EXTERNAL_POWER_STAGE_REQUIRED`

## Current state

`COOLING_AUX_POWER_INTERFACE_ARCHITECTURE_FROZEN`

`B11_B12_DEVICE_CURRENT_AND_PROTECTION_MEASUREMENT_GATED`
