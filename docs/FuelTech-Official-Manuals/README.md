# FuelTech Official Manuals

This folder is the authoritative documentation index for the FuelTech FT550 used in the Turbo V-Rod project.

The links below point directly to FuelTech-hosted PDF manuals so the project always has traceable manufacturer provenance rather than relying on third-party mirrors.

## 1. FT450 / FT550 / FT550LITE / FT600 ECU Manual

- Manufacturer: FuelTech
- Product relevance: Primary FT550 ECU installation, configuration, connector pinout, power, ground, inputs, outputs, trigger, CAN and engine-management reference.
- FuelTech manuals library listing: FT600 / FT550 / FT550LITE / FT450 Manual, Version 2.9, approximately 24 MB.
- Official PDF: https://files.fueltech.net/manuals/FT450_FT550_FT550LITE_FT600.pdf
- Project reference: [FT550-ECU-Manual.md](FT550-ECU-Manual.md)

## 2. FT550 Connector Kit Manual

- Manufacturer: FuelTech
- Product relevance: FT550 A/B connector cavities, terminal identification and connector assembly reference.
- FuelTech manuals library listing: Version 1.0, approximately 200 KB.
- Official PDF: https://files.fueltech.net/manuals/Kit_Terminais_FT550.pdf
- Project reference: [FT550-Connector-Kit.md](FT550-Connector-Kit.md)

## 3. PROBIKE Wiring Harness Owner's Manual

- Manufacturer: FuelTech
- Product relevance: Motorcycle-specific FT450/FT550 wiring architecture, relay/fuse structure, sensor grounds, power grounds, CAN, crank/cam, injectors, ignition and auxiliary I/O.
- Manual version: 1.0, April 2020.
- Official PDF: https://files.fueltech.net/manual/Ingles/PROBIKE_Harness.pdf
- Project reference: [PROBIKE-Harness-Manual.md](PROBIKE-Harness-Manual.md)

## Turbo V-Rod engineering rule

These manuals define the FuelTech manufacturer requirements. They do **not** by themselves define the final Turbo V-Rod electrical architecture.

The project-specific design should retain the FuelTech requirements while applying deliberate electrical-domain segregation for:

1. **EPM — Engine Power Module**: ECU and engine-critical actuators.
2. **APM — Auxiliary Power Module**: fuel pumps, cooling, boost-related and other high-current auxiliary loads.
3. **SIM — Sensor Interface Module**: precision sensor supplies, sensor-reference grounds, signal conditioning and communications.

All three domains share the required vehicle electrical reference, but high-current load paths and precision sensor/reference paths must be controlled separately so pump, fan, injector, coil and other switching currents do not contaminate engine-management measurements.

## Retrieval helper

Run [`Fetch-FuelTech-Manuals.ps1`](Fetch-FuelTech-Manuals.ps1) from PowerShell to download current copies of all three PDFs directly from FuelTech into a local `vendor/` subfolder.

> FuelTech remains the authoritative publisher. Before freezing a production harness revision, verify the current manual revision against the official FuelTech manuals library: https://www.fueltech.net/pages/manuals-fueltech
