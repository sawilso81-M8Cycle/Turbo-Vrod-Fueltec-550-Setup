# FT550 Harness Interface Freeze – Rev 1

## Purpose

Close Build Gate BG-004 at the FT550 side by defining the approved ECU connector/harness architecture for the Turbo V-Rod Rev 1 harness.

## Approved FuelTech source

FuelTech FT550 Connector Kit PN **5011100278** is the preferred bare-connector procurement baseline when manufacturing a custom harness. FuelTech states the kit includes:

- 2 x FT550 connectors A & B;
- 56 x FT550 terminals;
- 1 x CAN A harness;
- 1 x CAN B connector kit.

The official FuelTech PROBIKE harness documentation remains the pin/function authority for the motorcycle-oriented FT550 interface.

## Rev 1 architecture decision

The harness builder may use either of the following, but must state which option is quoted/built:

### Option A – Custom harness from FT550 Connector Kit – PREFERRED

Use FuelTech PN 5011100278 and terminate the project harness directly into the FT550 A/B connectors according to the released cavity schedule.

Advantages:

- cleanest integration with the PMU16 architecture;
- eliminates unnecessary legacy relay/fuse hardware from a generic harness;
- allows project-standard circuit IDs, wire sizes, DR-25 construction and branch geometry;
- gives complete control of sensor-ground and power-domain topology;
- best basis for a repeatable Golden Harness.

### Option B – Genuine FuelTech PROBIKE harness as donor/interface

A genuine PROBIKE harness may be used if the builder prefers FuelTech's terminated motorcycle loom as the ECU-side interface. Any retained FuelTech relays/fuses, Peak & Hold connectors, expansion connectors and branch wiring must be documented in the as-built package.

Do not duplicate PMU-controlled power stages simply because the donor harness contains relays. Any change to the released power architecture requires engineering disposition.

## Key PROBIKE A interface functions to preserve

The official FuelTech PROBIKE documentation identifies the following FT550 functions used by this project:

- power ground;
- signal ground;
- switched +12 V ECU supply;
- sensor +5 V;
- CAN A LOW/HIGH;
- CAM input;
- crank/RPM reference input;
- White #2 / FT550 A21: 2-Step / clutch-switch input;
- White #3: TPS;
- White #4: oil pressure;
- White #5: coolant/H2O temperature;
- White #6: fuel pressure;
- White #7: speed;
- Gray ignition outputs to SparkPRO;
- Blue injection outputs.

PROBIKE B additionally provides CAN B, IAT, additional pressure inputs, gear-position input and additional injector/output capability.

## Two-Step requirement

FT550 White #2 / A21 remains the project Two-Step request input. It is ground activated through the controlled X70 sealed relay sub-harness. PMU O11 high-side output must never be connected directly to A21.

## CAN requirement

The custom harness shall preserve the released FT550 ↔ PMU CAN topology. The FuelTech connector kit's supplied CAN A harness may be retained/adapted only if it matches the released topology and termination strategy. No hidden extra termination is permitted.

## Power requirement

The FT550 supply and grounds must follow the released project power/ground topology. A generic PROBIKE harness relay architecture is not automatically authoritative over the PMU16 architecture.

## Injector architecture gate

The PROBIKE harness is designed to support FuelTech Peak & Hold hardware for low-impedance injectors and a bypass/jumper arrangement for high-impedance injectors. Therefore injector electrical verification remains mandatory before the final direct-drive versus Peak & Hold state is released.

## Manufacturing requirements

The harness builder shall:

1. procure genuine FuelTech connector/harness hardware or approved traceable equivalent;
2. record the exact FuelTech kit/harness PN in the build record;
3. perform 100% cavity-to-circuit verification before ECU connection;
4. never use wire colour alone as circuit authority;
5. preserve project circuit IDs and labels;
6. document any unused FT550 cavities and seal/protect them appropriately;
7. provide pre-cover photographs of FT550 connector breakouts;
8. perform continuity/isolation tests with the FT550 disconnected.

## Release status

BG-004 FT550 connector/harness architecture: **CLOSED – OPTION A PREFERRED / OPTION B CONTROLLED ALTERNATIVE**.

Remaining related gates:

- exact as-built terminal/contact traceability from the purchased FuelTech kit;
- injector impedance/driver decision;
- physical branch dimensions;
- final CAN termination verification on the completed harness.
