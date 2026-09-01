# Harness Formboard Specification – Rev 1

## Purpose

Define the manufacturing board / string-board drawing required to reproduce the accepted Turbo V-Rod harness after dimensional freeze.

## Drawing format

Preferred master format:

- vector PDF plus native CAD/source file;
- scale 1:1 for physical formboard print where practical;
- dimensions in millimetres;
- revision block and harness-set serial/revision field;
- connector IDs and branch IDs shown at every endpoint;
- breakout datums tied back to D00–D10;
- electrical circuit IDs referenced rather than relying only on colour.

## Required drawing content

For B01–B44 and all auxiliary branches show:

- routed centreline length;
- start and end datums;
- breakout position from nearest parent datum;
- connector orientation / clocking where assembly-sensitive;
- branch angle/direction where needed for fit;
- finished branch length and manufacturing tolerance;
- minimum service loop where applicable;
- loom covering type and nominal diameter;
- boot/transition type;
- splice-pack locations;
- shield termination locations;
- CAN twist/trunk/service-stub notes;
- heat-protection start/end points;
- P-clip / strain-relief reference locations;
- moving-branch requirements for steering/suspension;
- DNP branches clearly crossed out or identified as optional.

## Board datum convention

D00 is the master board origin. All breakout coordinates should be reproducible from D00 or the nearest controlled secondary datum.

Suggested axes:

- X = main-harness travel direction on the board;
- Y = branch offset;
- connector clocking expressed relative to board face or an annotated viewing direction.

The board drawing is a manufacturing aid. It does not override connector cavity schedules or electrical schematics.

## Prototype-to-golden conversion

Prototype formboard may use the current approximate dimensions and first-cut lengths. After motorcycle fitment:

1. record accepted final dimensions in `B01-B44-Dimensional-Freeze-Worksheet.csv`;
2. update every formboard branch to final finished length;
3. mark approved service-loop lengths;
4. update connector/boot positions;
5. add as-built splice locations;
6. incorporate approved DFM changes;
7. increment drawing revision;
8. use only the accepted revision for repeat harness manufacture.

## Manufacturing controls

- No branch may be shortened outside tolerance without engineering disposition.
- Extra service loop shall not be hidden inside DR-25 solely to consume excess conductor.
- Splice locations are controlled dimensions after Golden Harness validation.
- Moving branches shall be checked on the motorcycle even if they fit the formboard.
- Connector labels and harness serial/revision labels are mandatory.

## Electrical production freeze state

Electrical architecture and low-current circuit classes are sufficiently defined for formboard development.

The board remains `DIMENSIONAL_DRAFT` until bike measurements replace current estimates.

Promotion to `FORMBOARD_REV1_RELEASED` requires dimensional freeze, high-current sizing closeout, connector purchasing BOM closeout and prototype-fit approval.
