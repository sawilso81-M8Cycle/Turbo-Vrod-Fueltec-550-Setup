# PMU16 Connector & Terminal Production Freeze – Rev 1

## Purpose

Close BG-007 by defining the production termination rules for the ECUMASTER PMU-16 39-position connector, especially the 4.0 mm² fuel-pump architecture.

## Authority

Use the current official ECUMASTER PMU-16 pinout/manual as the primary authority. The PMU main battery feed is via the centre stud. Output conductors use the released 39-position Sicma/FCI connector system and the terminal family specified by ECUMASTER.

## Verified terminal families

- `211CC2S2160P` – Sicma 1.5 mm terminal family, 14–17 AWG class.
- `211CC3S2120` – Sicma 2.8 mm terminal family, 14–16 AWG class.
- `211CC3S3120` – Sicma 2.8 mm terminal family, 10–12 AWG class.

Final crimp approval still requires compatibility with the actual selected M22759/32 or equivalent conductor OD/insulation and the harness builder's calibrated tooling.

## PMU output ratings used by this project

For the standard PMU-16 architecture used by this repository, O1/O2 are treated as 25 A-class outputs. No load expected to exceed the applicable output rating may be connected directly merely because the conductor itself is larger.

The current ECUMASTER manual also documents higher-current paired-terminal arrangements on some newer/other PMU variants. These arrangements must not be assumed for this build unless the exact purchased PMU hardware/version and official pinout explicitly support them.

## 4.0 mm² fuel-pump termination rule

The fuel-pump feed and dedicated return remain fixed at **4.0 mm² minimum production conductor size**.

The 10–12 AWG-class Sicma 2.8 terminal family is the only PMU connector terminal family in the verified list that is a plausible direct match for approximately 4.0 mm² conductor. However, this does **not** by itself authorise direct PMU pump drive.

Direct PMU drive may be released only when all of the following are true:

1. exact purchased PMU hardware and output rating are verified;
2. actual pump steady current is measured;
3. cold-start/hot-restart inrush is measured;
4. selected 4.0 mm² wire fits the terminal crimp barrel and seal/connector system correctly without folding or strand removal;
5. terminal continuous-current capability has adequate thermal margin;
6. PMU output protection/current model is configured and proven on bench;
7. voltage drop at pump under worst expected operating state is acceptable;
8. connector temperature rise is acceptable during sustained operation;
9. adjacent loaded PMU terminals do not cause unacceptable thermal derating.

If any criterion fails, the PMU output becomes control-only and the pump is supplied through an approved external relay/solid-state power stage. The 4.0 mm² pump feed then terminates at that external stage rather than being forced through the PMU connector.

## Return-path rule

The dedicated 4.0 mm² pump return does not terminate into a low-current PMU signal ground. It must use the released high-current return/ground architecture and a termination system rated for the measured current and environment.

## Crimp and QA rules

For every PMU terminal family used:

- use calibrated tooling suitable for the exact terminal;
- verify conductor and insulation crimp geometry;
- no folded conductors, trimmed strands or solder reinforcement;
- perform sample pull-test/retention validation appropriate to the harness manufacturer's QA system;
- verify cavity retention after insertion;
- install seals/cavity plugs as required by the connector system;
- record terminal PN, wire PN, wire size and crimp tool/die in the Harness Build Record.

## PMU production release table

| Circuit class | Production rule |
|---|---|
| PMU main B+ | Centre stud; size from aggregate load/voltage-drop/protection calculation |
| 0.35–0.50 mm² commands/signals | Use verified terminal family matched to actual wire/insulation |
| 0.75–1.5 mm² controlled loads | Use verified terminal family matched to actual wire and output rating |
| 2.5 mm² loads | Use appropriate 2.8 mm terminal family only after current/thermal check |
| 4.0 mm² fuel-pump feed | 10–12 AWG-class terminal candidate; direct-drive remains pump-measurement gated |
| 4.0 mm² pump return | Dedicated high-current ground path, not PMU signal-ground cavity |

## Release decision

BG-007 is **CLOSED AT CONNECTOR/TERMINAL ARCHITECTURE LEVEL**.

The fuel-pump switching decision remains a separate BG-001 load-verification gate and is not closed by this milestone.

State: `PMU16_CONNECTOR_TERMINAL_ARCHITECTURE_FROZEN / PUMP_DIRECT_DRIVE_MEASUREMENT_GATED`.
