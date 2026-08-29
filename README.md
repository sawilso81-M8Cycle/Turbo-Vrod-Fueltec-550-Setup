# Turbo V-Rod FuelTech FT550 Setup

Engineering repository for integrating a FuelTech FT550 ECU into a Harley-Davidson VRXSE V-Rod Destroyer / Revolution-engine turbo application.

## Design intent

The project combines Harley-Davidson factory wiring information with FuelTech manufacturer documentation to produce a verified, serviceable, motorsport-grade engine-management harness.

The working architecture separates the electrical system into three controlled domains:

1. **EPM — Engine Power Module**: FT550, injectors, ignition and engine-critical actuators.
2. **APM — Auxiliary Power Module**: fuel pumps, cooling, boost-control and other high-current auxiliary loads.
3. **SIM — Sensor Interface Module**: precision sensor supplies, signal returns, trigger wiring, conditioning and communications.

All three domains retain the required common vehicle electrical reference, but high-current paths are deliberately separated from precision measurement paths.

## Documentation

- [FuelTech Official Manuals](docs/FuelTech-Official-Manuals/README.md)
- [Harley VRXSE Official References](docs/Harley-VRXSE-Official-References/README.md)
- [VRXSE to FT550 Sensor Matrix](docs/VRXSE-FT550/VRXSE-to-FT550-Sensor-Matrix.md)
- [Electrical Architecture and Grounding](docs/VRXSE-FT550/Electrical-Architecture-and-Grounding.md)
- [Trigger and MAP Strategy](docs/VRXSE-FT550/Trigger-and-MAP-Strategy.md)
- [Development Roadmap](ROADMAP.md)

## Verification rule

No circuit is production-ready merely because it appears in this repository. Every pin, wire colour, sensor type, transfer function, polarity and supply requirement must be verified against the exact Harley-Davidson publication and current FuelTech manual revision before energising the harness.

Where a value is not yet verified, it must remain explicitly marked **VERIFY** rather than being inferred.
