# Connector / Cavity Master Schedule – Rev 1

## Purpose

Create the pin-by-pin connector reference that pairs with the Production Wire / Circuit Master Schedule and becomes the harness builder's authoritative interface map.

This schedule covers FT550, PMU16, retained OEM X10-X23 interfaces, fuel-pump service connectors X30/X31, X50, X51, injector driver service interfaces X62/X63 and X70 Two-Step relay interface.

## Release rule

A connector/cavity row may only be promoted to `HP5_RELEASED` when the following are known and accepted:

- exact connector/interface ID;
- exact cavity/pin number;
- circuit ID;
- function;
- conductor size;
- terminal/contact PN;
- seal/secondary lock where applicable;
- source/destination relationship;
- polarity or signal class where relevant;
- supporting evidence/source;
- no conflicting cavity assignment exists.

Where exact pin numbers are not yet supported by authoritative evidence, the row shall remain `VERIFY_REQUIRED`. No inferred cavity number is permitted in the production baseline.

## FT550 interfaces

The FT550 rows shall use the official connector-kit/custom-harness architecture and retain known functional assignments such as:

- Front injector command: A1 / Blue #1;
- Rear injector command: A2 / Blue #2;
- SparkPRO CH1 command: A8;
- SparkPRO CH2 command: A9;
- Two-Step dry-contact input: A21.

Any other FT550 cavity assignment must be verified against the applicable FuelTech documentation/configuration before release.

## PMU16 interfaces

The PMU16 section shall record:

- exact hardware revision;
- used output/input function;
- exact connector/cavity;
- selected terminal family;
- conductor range;
- circuit ID;
- final current class.

Previously identified Sicma/FCI terminal families remain candidates only until each cavity/wire combination is explicitly accepted.

## OEM X10-X23 interfaces

Every used X10-X23 device shall be either:

`EXACT_CONNECTOR_FROZEN`

or

`OEM_PIGTAIL_FROZEN`

before production release.

The cavity schedule shall reflect verified wire colours, cavity numbering, signal function and polarity. Visual similarity is not sufficient.

## X30/X31 fuel-pump service interfaces

X30 and X31 remain sealed HDSCS/MCP-class service breaks.

Each requires at minimum:

- pump positive feed cavity using 4.0 mm² conductor;
- dedicated pump return cavity using 4.0 mm² conductor;
- exact housing/contact/seal selection;
- native pump-side pigtail mapping.

Do not repurpose these interfaces for lower-current auxiliary circuits.

## X50 engineering/service connector

X50 remains low/medium-current only.

Candidate functions include service ground, optional protected service +12 V, engineering digital/analogue I/O and approved spares. CAN is omitted unless specifically required because X51 is the preferred diagnostic CAN interface.

## X51 CAN service connector

Frozen cavity function baseline:

1. CAN-H;
2. CAN-L;
3. service ground;
4. optional protected service +12 V or DNP.

No hidden termination resistor is permitted in X51.

## X62/X63 injector driver service interfaces

X62/X63 preserve both injector architectures:

`FT550 A1/A2 -> X62 -> direct bypass -> X63 -> injectors`

or

`FT550 A1/A2 -> X62 -> Peak & Hold module -> X63 -> injectors`

The final cavity map shall prevent front/rear channel reversal and shall make the direct-bypass/Peak-and-Hold configuration mechanically clear.

## X70 Two-Step relay interface

X70 shall preserve:

- PMU O11 relay-coil command;
- relay coil return as defined by the released architecture;
- normally-open dry contact to FT550 A21;
- dry-contact ground reference;
- strict isolation of the A21 contact side from +12 V.

## QA rules

Before HP-5 release:

- no cavity is assigned to two unrelated circuits;
- no required cavity is left blank;
- every DNP cavity is explicitly labelled;
- H/L polarity is consistent for CAN;
- sensor ground and power ground are not merged by connector mapping;
- FT550 A21 contact path contains no +12 V source;
- trigger polarity remains controlled;
- pump polarity is explicit;
- front/rear injector and coil channels cannot be swapped by ambiguous labelling;
- exact terminals match the released conductor sizes.

## Current state

`CONNECTOR_CAVITY_MASTER_SCHEDULE_RELEASED_AS_WORKING_BASELINE`

Individual rows remain `VERIFY_REQUIRED`, `DFM_PENDING`, `PHYSICAL_ID_REQUIRED` or equivalent until the evidence gate is closed.

Final state:

`CONNECTOR_CAVITY_MASTER_SCHEDULE_HP5_RELEASED`
