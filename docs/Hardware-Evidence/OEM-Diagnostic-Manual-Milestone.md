# OEM Diagnostic Manual Milestone — 2006 VRSC / VRXSE

## Objective

Advance injector and ignition electrical characterization using Harley-Davidson factory literature only where possible.

## Factory literature baseline

Harley-Davidson identifies the following 2006 VRSC service publications:

- 99501-06A — VRSC Service Manual
- 99499-06A — VRSC Electrical Diagnostics Manual

These are the authoritative next-stage references for injector and ignition diagnostic values.

## OEM hardware confirmed for VRXSE Destroyer

### Fuel injectors

- Harley high-flow injector kit: 27791-05
- Individual injector: 27772-06
- Quantity: 2
- OEM Race Tuner injector calibration: 6.37 g/s
- OEM statement: approximately 30% greater fuel flow than the standard VRSC injector

### Ignition coils

- Harley coil assembly: 32477-01A
- Coil boot: 31651-01
- Quantity: 2
- VRXSE Destroyer uses special race ECM 33225-06

Harley factory parts data also shows 32477-01A across the wider VRSC family, which makes VRSC electrical diagnostic procedures relevant to the Destroyer coil hardware.

## Diagnostic-manual search result

The public Harley SIP pages confirm 99499-06A as the correct 2006 VRSC Electrical Diagnostics Manual, but the searchable public SIP index does not expose the specific injector resistance/current or coil primary resistance/current-ramp procedures from that manual.

Therefore the following values are NOT OEM-frozen yet:

- injector DC resistance / impedance classification;
- injector peak and hold current profile;
- ignition coil primary resistance;
- ignition coil dwell/saturation current;
- internal igniter / smart-coil status;
- exact FT550 ignition-driver compatibility.

## Supporting evidence that is deliberately not promoted to OEM specification

A specialist V-Rod replacement-coil catalogue describes the 32477-01A replacement class as approximately 0.7 ohm. This is useful supporting evidence that the coil may be a low-resistance ECU-driven design, but it is not Harley factory data and therefore must not be used as the production configuration value without verification.

Earlier aftermarket listings describing 3-ohm replacements are likewise not accepted as an OEM specification because the claims conflict.

## Engineering consequence

The project must continue to treat the OEM coils as electrically unverified until either:

1. the relevant pages from 99499-06A are obtained and added as permitted engineering evidence; or
2. the installed 32477-01A coils are characterized on the bench with low-resistance/Kelvin measurement plus current-ramp testing.

The same rule applies to 27772-06 injector impedance and current behavior.

## Release rule

No FT550 injector-driver mode, ignition-driver mode, dwell table, peak/hold strategy, final wire size, or connector terminal current rating may be frozen solely from aftermarket replacement specifications.
