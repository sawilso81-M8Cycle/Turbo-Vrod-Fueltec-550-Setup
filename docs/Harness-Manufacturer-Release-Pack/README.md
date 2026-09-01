# Turbo V-Rod FT550 / PMU16 Harness Manufacturer Release Pack

## Purpose

This folder is the controlled hand-off package for quoting, manufacture, inspection and acceptance of the custom Turbo V-Rod Destroyer electrical harness.

The manufacturer is **not** being asked to redesign the electrical architecture. Where a circuit, connector, conductor size, branch length or component is marked OPEN / VERIFY / MEASUREMENT GATED, stop and request engineering disposition before manufacture.

## System architecture

The harness supports:

- FuelTech FT550 PROBIKE ECU;
- ECUMASTER PMU-16 power distribution;
- FuelTech SparkPRO-2 ignition driver;
- OEM Harley-Davidson VRXSE/Destroyer sensors and engine hardware where retained;
- turbo/boost instrumentation and control;
- CAN backbone between FT550 and PMU;
- clutch / Two-Step launch subsystem;
- modular serviceable sub-harness construction.

## Preferred harness construction

Unless a released drawing states otherwise:

- motorsport/automotive ETFE thin-wall wire, M22759/32 or approved equivalent;
- Raychem DR-25 or approved equivalent heat/chemical-resistant loom covering;
- adhesive-lined heat shrink at transitions and boots;
- sealed Deutsch DTM/DT or specified OEM/FuelTech/ECUMASTER connectors;
- proper calibrated open-barrel crimp tooling for every terminal family;
- no solder-spliced production signal wiring unless specifically approved;
- sealed ultrasonic/open-barrel production splices or approved motorsport splice method;
- twisted CAN pair with topology and termination preserved;
- CKP and other noise-sensitive circuits routed away from ignition/injector/high-current conductors;
- sensor/reference grounds segregated from high-current return paths as defined by project documents;
- labels must remain readable after final loom covering is installed.

## Modular loom split

Quote and manufacture as separable assemblies where practical:

1. **H01 Main ECU / Engine Harness** – FT550, OEM engine sensors, CKP/TPS/MAP/ECT/IAT and primary engine interfaces.
2. **H02 PMU / Power Harness** – PMU-16 main power, hardwired command inputs and controlled outputs.
3. **H03 EPM Ignition / Injector Harness** – SparkPRO-2, coils, injectors and optional Peak & Hold interface path.
4. **H04 Sensor / Turbo Instrumentation Harness** – oil/fuel pressure, post-intercooler IAT and approved auxiliary sensors.
5. **H05 CAN / Service Harness** – FT550 ↔ PMU CAN backbone and X51 service break.
6. **H06 Two-Step / Clutch Harness** – OEM clutch switch service break, PMU A6, O11 relay interface and FT550 A21.
7. **H07 Boost-Control Harness** – O6 boost-solenoid circuit and associated service connector.

A manufacturer may recommend different physical break points for packaging/serviceability, but electrical changes require approval before implementation.

## X70 Two-Step implementation for Rev 1 harness

**Custom X70 PCB is bypassed for the present harness revision.**

Implement X70 as a sealed replaceable relay sub-harness:

- PMU O11 provides +12 V high-side command to relay coil;
- relay coil return to approved power ground;
- normally-open dry contact connects FT550 A21 / White #2 to ground when O11 is energised;
- FT550 A21 must never be exposed to +12 V;
- use an automotive 12 V SPST-NO relay or sealed equivalent with appropriate coil suppression;
- suppression must be compatible with PMU O11 and must not cause unacceptable relay release delay;
- relay/sub-harness must be replaceable without cutting the main loom.

The manufacturer may propose a preferred sealed relay/holder with datasheet and part numbers for engineering approval.

## Controlled source documents

The manufacturer shall use the latest repository revisions of:

- `docs/HD-Style-Wiring/` – functional wiring sheets;
- `docs/Production-Harness-Milestone/Connector-Cavity-Schedule.csv`;
- `docs/Production-Harness-Milestone/Connector-Index.md`;
- `docs/Production-Harness-Milestone/Harness-Branch-Schedule.csv`;
- `docs/Production-Harness-Milestone/Wire-Size-Schedule.csv`;
- `docs/Production-Harness-Milestone/Rev1-Harness-BOM.csv`;
- `docs/Production-Harness-Milestone/Splice-Ground-Reference.md`;
- `docs/Production-Harness-Milestone/Terminal-Selection-Gate.md`;
- `docs/Production-Harness-Milestone/Verification-Register.csv`;
- `docs/ECUMASTER-PMU16/`;
- `docs/EPM-Driver-Interface/`;
- `docs/CAN-Backbone/`;
- `docs/Launch-Control/`.

This pack adds the commercial/manufacturing requirements, acceptance criteria and quote schedule. It does not supersede verified pin/cavity data in the controlled engineering files.

## Deliverables required from manufacturer

Before build:

- quotation against `Manufacturer-RFQ.csv`;
- proposed connector/terminal substitutions, if any;
- proposed wire and loom material series;
- proposed X70 sealed relay implementation;
- confirmation of tooling capability for selected terminal families;
- confirmation of electrical test capability.

With completed harness:

- completed `Harness-Build-Record.csv`;
- completed `Harness-Acceptance-Test.csv`;
- as-built branch dimensions;
- as-built connector/terminal/boot part numbers;
- continuity/netlist test report;
- insulation/isolation test report using limits safe for connected electronics (electronics disconnected during inappropriate high-voltage tests);
- crimp/tooling traceability where available;
- photographs of harness before final covering and completed harness;
- list of all approved deviations;
- serial number and build revision label.

## Release states

- `RFQ_READY` – package suitable for manufacturer quotation.
- `BUILD_DATA_OPEN` – quotation possible but one or more build-critical engineering gates remain open.
- `MANUFACTURING_RELEASED` – all build-critical dimensions, conductor sizes, connector/terminal selections and engineering dispositions are frozen.
- `HARNESS_ACCEPTED` – completed harness passes documentation, visual and electrical acceptance testing.

Current state: **RFQ_READY / BUILD_DATA_OPEN**.

Do not represent this package as `MANUFACTURING_RELEASED` until every YES release blocker applicable to the harness has been closed or formally dispositioned.
