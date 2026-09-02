# Harness Formboard Specification – Current Manufacturer Package

## Purpose
Define the manufacturing board / string-board drawing required to reproduce the accepted Turbo V-Rod harness after dimensional freeze.

## Drawing format
- vector PDF plus native CAD/source file preferred;
- scale 1:1 where practical;
- dimensions in millimetres;
- revision block and harness-set serial/revision field;
- connector IDs and branch IDs at every endpoint;
- breakout datums tied back to controlled datums;
- electrical circuit IDs referenced rather than relying only on colour.

## Required drawing content
For B01–B44 and all auxiliary branches show routed centreline length, start/end datums, breakout positions, connector orientation/clocking where assembly-sensitive, branch direction where needed, finished branch length/tolerance, service loop, loom covering, boots/transitions, splice-pack locations, shield termination, CAN twist/trunk/service-stub notes, heat-protection start/end points, strain-relief/P-clip locations, moving-branch requirements and DNP/optional branches.

## Prototype-to-golden conversion
Prototype formboard may use current approximate dimensions and first-cut lengths. After motorcycle fitment:
1. record accepted final dimensions;
2. update every branch to final finished length;
3. mark approved service-loop lengths;
4. update connector/boot positions;
5. add as-built splice locations;
6. incorporate approved DFM changes;
7. increment drawing revision;
8. use only the accepted revision for repeat manufacture.

## Manufacturing controls
- No branch may be shortened outside tolerance without engineering disposition.
- Extra service loop shall not be hidden inside loom covering merely to consume excess conductor.
- Splice locations become controlled dimensions after Golden Harness validation.
- Moving branches shall be checked on the motorcycle even if they fit the formboard.
- Connector labels and harness serial/revision labels are mandatory.

## Current state
The formboard remains `DIMENSIONAL_DRAFT` until bike measurements replace current estimates.

Promotion to `FORMBOARD_REV1_RELEASED` requires dimensional freeze, high-current sizing closeout, connector purchasing BOM closeout and prototype-fit approval.
