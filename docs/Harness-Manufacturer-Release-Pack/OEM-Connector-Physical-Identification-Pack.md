# OEM Connector Physical Identification Pack – X10–X23

## Purpose

Close the remaining physical-identification gap for retained OEM V-Rod sensors, injectors and coils before Rev 1 harness manufacture.

This pack deliberately separates **known component identity** from **verified mating-connector identity**. No connector housing or terminal may be released from visual similarity alone.

## Production rule

For each retained OEM device, use one of two accepted outcomes:

1. **Exact mating connector frozen** – housing, terminal, seal, lock/TPA and cavity map are positively identified and purchasable; or
2. **OEM repair pigtail frozen** – a genuine/verified mating pigtail is used at the component, followed by a controlled sealed service break into the new harness.

If neither is proven, the interface remains `PHYSICAL_ID_REQUIRED` and cannot be released for production.

## Interfaces in scope

The X10–X23 register shall cover the retained engine/vehicle devices including, where applicable:

- CKP / crank position;
- CAM position if fitted/used;
- TPS / throttle position;
- MAP;
- engine/coolant temperature;
- intake-air temperature;
- vehicle-speed sensor;
- oil/fuel/other retained OEM sensor interfaces defined by the harness schedule;
- front injector;
- rear injector;
- front ignition coil;
- rear ignition coil;
- any additional retained OEM connector already assigned an X10–X23 designator.

The latest released wire/interface schedule remains authoritative for exact X-number-to-device mapping.

## Identification evidence required

For every connector capture:

- device manufacturer and OEM PN;
- all moulded connector markings and logos;
- cavity count;
- connector gender viewed at the mating face;
- keying/polarisation geometry;
- latch style;
- secondary lock / TPA / CPA style and colour;
- seal style and colour;
- approximate housing dimensions;
- terminal blade/pin size where measurable;
- conductor outside diameter and conductor cross-section of the OEM pigtail where known;
- cavity numbering moulded into housing;
- wire colour at each cavity;
- circuit function established by authoritative schematic or continuity test;
- clear photographs of mating face, wire-entry face, side profile, latch and markings.

## Photograph standard

Use a ruler or caliper reference in at least one image. Do not rely on perspective-heavy photographs.

Minimum image set per interface:

1. device + connector overview;
2. straight-on mating face;
3. straight-on wire-entry face;
4. latch/keying side;
5. moulded markings close-up;
6. cavity/wire colours;
7. mating harness connector/pigtail if available.

Recommended filenames:

`X10_CKP_01_overview.jpg`
`X10_CKP_02_mating-face.jpg`
`X10_CKP_03_wire-entry.jpg`

and equivalent for each X-number.

## Electrical verification

Before assigning cavity functions:

- disconnect power;
- use authoritative OEM information where available;
- otherwise continuity-test only to known circuit endpoints;
- do not apply 12 V to an unknown sensor cavity;
- distinguish 5 V reference, sensor ground and signal before connection to FT550;
- preserve CKP/CAM polarity evidence rather than assuming wire colour;
- injector polarity/supply side shall match the released injector architecture;
- coil interfaces shall match the SparkPRO architecture.

## Connector selection hierarchy

Preferred order:

1. exact OEM/connector-manufacturer housing and terminals;
2. exact reputable equivalent from the original connector family;
3. genuine OEM repair pigtail;
4. verified quality repair pigtail plus controlled service break.

Do not approve generic marketplace pigtails solely because they plug in.

## Service-pigtail fallback

When exact loose components cannot be confidently sourced, retain a short OEM repair pigtail at the sensor/device.

Low-current sensor pigtails may transition through an appropriately sized sealed Deutsch DTM service break where packaging permits.

CKP/CAM pigtails require additional controls:

- keep transition short;
- preserve twisted/shielded construction as applicable;
- do not connect shield drain at both ends unless the released trigger design explicitly requires it;
- keep the service break away from SparkPRO, coils, starter, injectors and pump power;
- document polarity through the transition.

Fuel-pump high-current interfaces are excluded from a low-current DTM fallback and follow the separate HDSCS/MCP fuel-pump interface freeze.

## Crimp/tooling gate

For every loose connector solution record:

- housing PN;
- terminal PN;
- wire seal PN if separate;
- TPA/CPA/secondary lock PN if separate;
- cavity plug PN;
- approved conductor range;
- approved insulation/seal range;
- recommended crimp tooling;
- pull-test requirement;
- supplier/source.

A connector family is not production-frozen until its terminal accepts the actual wire used in that circuit.

## Acceptance

An interface becomes `EXACT_CONNECTOR_FROZEN` when the mating housing, terminals, seals/locks, cavity numbering and circuit map are all verified.

An interface becomes `OEM_PIGTAIL_FROZEN` when the exact mating pigtail is verified and its transition/service-break architecture is fully documented.

Anything else remains `PHYSICAL_ID_REQUIRED`.

## Release state

Current milestone state:

`OEM_CONNECTOR_PHYSICAL_IDENTIFICATION_FRAMEWORK_FROZEN`

Final manufacturing release requires every used X10–X23 row to be either:

`EXACT_CONNECTOR_FROZEN`

or

`OEM_PIGTAIL_FROZEN`
