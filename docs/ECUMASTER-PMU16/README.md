# ECUMASTER PMU-16 Reference Pack

This folder records the official ECUMASTER PMU-16 / PMU-16 DL documentation relevant to the Turbo V-Rod + FuelTech FT550 project.

## Official sources

### PMU User Manual

- Product family: PMU-16 / PMU-16 DL / PMU-16 AS / PMU-24 DL
- Manual: PMU User Manual 101.2.1
- Published: 2026-04-23
- Official ECUMASTER downloads page: https://www.ecumaster.com/downloads/
- Official manual PDF: https://www.ecumaster.com/files/PMU/PMU_Manual.pdf

### PMU-16 Pinout

- Document: PMU-16 Pinout v1.2
- Published: 2025-04-16
- Official pinout PDF: https://www.ecumaster.com/files/PMU/PMU-16_Pinout_v1.2.pdf

### Product page

- Official product page: https://www.ecumaster.com/products/pmu/

## Verified capabilities relevant to this project

The PMU-16 provides 16 electronically protected high-side power outputs with continuous current sensing, programmable over-current protection, self-reset strategies, logic-based control, CAN communications and logging of output state/current/voltage data.

The current PMU-16 pinout defines:

- 16 power outputs O1-O16;
- 16 analogue/digital inputs A1-A16;
- +5 V sensor/reference output;
- switched +12 V input;
- ground;
- CAN1 H/L;
- CAN2 H/L.

The exact permitted current per output and terminal/wire limitations must be taken from the current ECUMASTER manual and pinout before a production wiring schedule is frozen.

## Turbo V-Rod architecture position

The PMU-16 is being evaluated as the preferred candidate backbone for the APM (Auxiliary Power Module). It is not yet approved as a wholesale replacement for the three-domain architecture.

The project retains:

1. EPM - engine-critical ECU / ignition / injection power and control;
2. APM - pumps, cooling, boost-related auxiliaries and other high-current loads;
3. SIM - precision sensors, sensor grounds, signal conditioning and communications.

The PMU-16 may substantially reduce conventional relays, fuses and custom APM circuitry while adding current monitoring, diagnostics, configurable protection and CAN status reporting.

## Candidate APM loads

Subject to verified current, inrush and safety analysis, candidate PMU-16 loads include:

- primary fuel pump;
- secondary fuel pump;
- radiator fan(s);
- intercooler/water pump;
- water/methanol pump if fitted;
- boost-control solenoid supply;
- auxiliary cooling devices;
- warning / auxiliary outputs;
- non-precision race electrical loads.

Engine-critical power should only be moved onto the PMU after failure-mode analysis confirms that the resulting architecture is safer and electrically cleaner than the dedicated EPM arrangement.

## CAN integration objective

A future milestone is to define FT550-to-PMU CAN messaging so the PMU can receive requested states and the FT550/logger/display can receive PMU output state, current and fault information.

Until this mapping is proven from official CAN documentation, no CAN identifiers or payloads should be guessed.
