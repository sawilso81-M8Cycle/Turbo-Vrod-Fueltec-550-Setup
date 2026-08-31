# VRXSE OEM Injector and Ignition Coil Research

## Scope

This note records only manufacturer-backed or strongly corroborated identification evidence for the 2006 VRXSE V-Rod Destroyer injector and ignition-coil hardware. Electrical values are not inferred from similar-looking components.

## Fuel injectors

Harley-Davidson VRXSE parts information identifies:

- VRXSE fuel injector kit: `27791-05`;
- the kit is fitted to the VRXSE throttle-body/fuel-rail assembly;
- Harley-Davidson instruction sheet J03928, titled `VRXSE PERFORMANCE INJECTOR KIT`, states that kit 27791-05 contains two fuel injectors with O-rings, part number `27772-06`.

### Project conclusion

Front and rear injector hardware baseline:

`Harley-Davidson 27772-06`

Status:

- part number: VERIFIED;
- quantity: two;
- connector family: VERIFY;
- injector impedance: VERIFY;
- peak/hold current: VERIFY;
- FT550 injector-driver configuration: VERIFY.

No low-impedance/high-impedance classification is to be assigned until supported by a verified specification or bench measurement.

## Ignition coils

Harley-Davidson VRSC parts information identifies plug-top ignition coil assembly `32477-01A`, quantity two. The same coil part number is used broadly across the VRSC family, and fitment data includes the VRXSE Destroyer.

### Project conclusion

Front and rear ignition-coil hardware baseline:

`Harley-Davidson 32477-01A`

Status:

- part number: VERIFIED;
- quantity: two;
- plug-top construction: VERIFIED;
- connector family: VERIFY;
- cavity/pin functions: VERIFY;
- primary resistance: VERIFY;
- charging-current waveform: VERIFY;
- internal igniter/smart-coil status: VERIFY;
- FT550 ignition-driver compatibility: VERIFY.

Do not assume the coil is a smart coil or a conventional inductive coil from appearance alone.

## Authoritative sources used

1. Harley-Davidson 2006 VRXSE Parts Catalog, publication 99452-06A.
2. Harley-Davidson instruction J03928, `VRXSE PERFORMANCE INJECTOR KIT`, kit 27791-05.
3. Harley-Davidson VRSC parts catalog entries for coil assembly 32477-01A and cross-model fitment evidence.

## Release impact

This research closes component identity but does not close electrical compatibility.

The following still require either primary manufacturer data or bench evidence:

1. injector resistance and dynamic current;
2. injector connector/terminal family;
3. coil primary resistance and current ramp;
4. coil connector/terminal family;
5. coil pin functions;
6. whether the coil includes an internal igniter;
7. final FT550 injector and ignition output assignments and dwell/current strategy.

These measurements should be captured in the Hardware Evidence package before Rev 1 harness release.
