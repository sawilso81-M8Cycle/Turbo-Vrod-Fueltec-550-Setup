# Production Wire / Circuit Master Schedule – Rev 1

## Purpose

Define the loom-builder's authoritative conductor schedule for the Turbo V-Rod FT550 harness. Every production conductor receives a unique circuit ID, source, destination, wire size, signal class, protection rule, branch assignment and release state.

This schedule does not override subsystem freeze documents. Where a value remains evidence-gated, the circuit row is retained but marked accordingly until HP-5 release.

## Circuit ID convention

- `PWR-xxx` – primary/high-current power
- `GND-xxx` – power or dedicated returns
- `EPM-xxx` – engine-critical power
- `INJ-xxx` – injector commands/supplies
- `IGN-xxx` – ignition/SparkPRO
- `SEN-xxx` – analogue/digital sensors
- `TRG-xxx` – CKP/CAM trigger circuits
- `CAN-xxx` – CAN backbone/service
- `CTL-xxx` – low-current control/relay commands
- `AUX-xxx` – cooling/auxiliary loads
- `SRV-xxx` – service/engineering interface
- `SPARE-xxx` – controlled spare/DNP

## Locked production principles

- Fuel-pump positive feeds remain 4.0 mm² minimum.
- Fuel-pump dedicated returns remain 4.0 mm² minimum.
- B15 PMU primary feed remains 10 mm² baseline unless a later engineering change upsizes it.
- B39 injector and B40 ignition supplies remain independent protected branches.
- Sensor ground is not merged into high-current return wiring.
- FT550 A21 Two-Step contact side remains dry-contact-to-ground only, with no +12 V path.
- CAN remains a linear FT550↔PMU backbone with X51 as a short service stub and no hidden termination.
- CKP/CAM remain dedicated trigger circuits with routing/shielding controls.

## Production data required per row

Every released row shall contain:

- unique circuit ID;
- function;
- source connector/cavity;
- destination connector/cavity;
- conductor size;
- wire family/spec;
- colour or printed ID;
- branch/bundle assignment;
- signal class;
- protection device/current limit;
- twist/shield requirement;
- splice ID if applicable;
- released routed/cut length where controlled;
- source and destination terminal PNs;
- release state.

## Release states

`FROZEN` – production value is locked.

`BASELINE_FROZEN / EVIDENCE_GATED` – architecture and minimum/baseline are locked, final value awaits measurement.

`DFM_GATED` – manufacturer component selection remains open within the frozen architecture.

`PHYSICAL_ID_REQUIRED` – exact connector/cavity cannot be released until bike-side evidence is captured.

`DNP` – intentionally not populated.

`HP5_RELEASED` – row has all production data required for crimp/build release.

## HP-5 rule

No conductor may be released to manufacture while its source/destination cavity, conductor size, terminal compatibility, protection and branch routing are still ambiguous.

The CSV companion file is the working master schedule and shall be updated to the final as-built configuration after Golden Harness qualification.
