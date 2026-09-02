# Project Master Release Dashboard – Turbo V-Rod FT550 Harness

## Purpose

Provide one authoritative project-level view of what is frozen, what remains evidence-gated, what requires manufacturer DFM, and what prevents the first electrically functional Rev 1 harness.

This dashboard is a status summary only. The detailed freeze, verification and release documents remain authoritative for each system.

## Current overall state

**Architecture:** substantially frozen  
**Manufacturer package:** Rev 2 released for RFQ/DFM  
**Functional harness manufacture:** NOT YET AUTHORISED  
**First power:** NOT YET AUTHORISED  
**Golden Harness:** NOT YET VALIDATED

Current release banner:

`DFM_REV2_RELEASED / RFQ_READY / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

## Completion matrix

| Area | Architecture | Procurement / DFM | Measurement / Evidence | Production Release |
|---|---|---|---|---|
| FT550 ECU interface | FROZEN | connector/tooling review | final cavity audit | GATED |
| PMU16 architecture | FROZEN | terminal/tooling DFM | exact used-cavity verification | GATED |
| SparkPRO ignition | FROZEN | connector/build review | coil current + dwell | GATED |
| Fuel pump wiring | FROZEN | HDSCS/MCP family frozen | pump current/inrush/thermal | GATED |
| Fuel pump switching | DUAL PATH FROZEN | external-stage PN if required | direct PMU vs external stage | GATED |
| Radiator fan B11 | FROZEN BASELINE | connector DFM | current/inrush/thermal | GATED |
| Charge-cooler B12 | FROZEN BASELINE / DNP OPTION | connector DFM | fitted status + current | GATED |
| B15 primary PMU feed | 10 mm² BASELINE FROZEN | junction/protection DFM | simultaneous-load calculation | GATED |
| B39 injector supply | FROZEN | protection implementation | injector electrical verification | GATED |
| B40 ignition supply | FROZEN | protection implementation | dwell/current verification | GATED |
| Injector driver path | DIRECT/PNH PATH FROZEN | P&H PN only if required | injector impedance/current | GATED |
| CKP/CAM trigger | FROZEN | routing/build DFM | installed signal integrity | GATED |
| CAN backbone | FROZEN | X51 hardware DFM | exact termination state | GATED |
| X51 CAN service | FROZEN | exact DTM PNs | acceptance tests | GATED |
| X50 engineering interface | FROZEN | exact housing/cavity count | final cavity schedule | GATED |
| X70 Two-Step | FROZEN | socket/carrier DFM | bench truth table | GATED |
| OEM X10-X23 | IDENTIFICATION METHOD FROZEN | exact connectors/pigtails | physical ID/cavity evidence | GATED |
| Branch dimensions | METHOD FROZEN | manufacturer measurement process | physical bike measurement | GATED |
| Harness acceptance | FROZEN PROCESS | manufacturer test capability | prototype evidence | FUTURE |
| Golden Harness | FROZEN PROCESS | formboard process | successful prototype | FUTURE |
| Repeat production | CONFIG CONTROL FROZEN | serial/document process | Golden Harness validation | FUTURE |

## Hard blockers to MANUFACTURING_RELEASED_REV1

The following must be closed or explicitly dispositioned before functional harness manufacture:

1. actual fuel-pump identification and electrical verification;
2. injector electrical class and final driver decision;
3. coil/SparkPRO dwell and current verification sufficient to freeze B40;
4. B11 radiator-fan electrical data;
5. B12 fitted/DNP decision and electrical data if fitted;
6. exact PMU16 hardware revision and used cavity/terminal/wire audit;
7. exact OEM X10-X23 connector or controlled repair-pigtail solutions;
8. X70 relay socket/carrier selection;
9. X50 exact connector/cavity count;
10. X51 exact procurement set;
11. CAN termination configuration;
12. B15 master protection and primary junction hardware;
13. B39 final protection;
14. B40 final protection;
15. branch dimensions or approved manufacturer measurement-build exception;
16. manufacturer Rev 2 DFM return accepted;
17. all blocking RFIs/deviations closed;
18. crimp/tooling compatibility confirmed for every production terminal.

## Work that can proceed now

Without waiting for electrical testing, the project can proceed with:

- harness manufacturer RFQ;
- manufacturer DFM review;
- exact connector sourcing proposals;
- X50/X51/X70 procurement proposals;
- PMU/FT550 crimp tooling review;
- OEM connector physical photography/identification;
- motorcycle branch measurements;
- wire/sleeve/boot material selection;
- formboard/Golden Harness planning;
- quotation and lead-time review.

## Measurement campaign

The fastest physical evidence campaign should capture in one workshop session where practical:

### Electrical
- Pump 1/2 exact PN and native connector;
- pump cold/hot inrush and steady current;
- injector PN/markings/resistance;
- coil PN/markings and SparkPRO test data;
- radiator-fan PN/current;
- charge-cooler pump PN/current if fitted.

### Connector identification
- X10-X23 full photograph set;
- moulded markings;
- cavity count/keying;
- OEM wire colours;
- pigtail conductor sizes.

### Physical dimensions
- ECU/PMU/SparkPRO positions;
- battery/J-P01/J-P02 positions;
- pump branches;
- injector/coil branches;
- fan/cooling branches;
- CKP/CAM/VSS routes;
- steering and suspension movement allowances;
- turbo/exhaust heat-clearance zones;
- X50/X51/X70 service positions.

## Manufacturer return campaign

The Rev 2 package shall be issued using the controlled package generator. Manufacturer returns are reviewed through the Manufacturer Return Review + Engineering Release Gate.

Required return includes:

- completed DFM response register;
- connector/terminal proposals;
- RFIs;
- deviations;
- wire/sleeving/boot proposal;
- test/process capability;
- formboard process;
- quotation and lead time.

## Release ladder

`RFQ_READY`

↓

`DFM_REV2_RELEASED`

↓ manufacturer return + measurement closure

`HP1_DFM_ACCEPTED`

↓

`HP2_CONNECTOR_PROCUREMENT_ACCEPTED`

↓

`HP3_ELECTRICAL_BLOCKERS_CLOSED`

↓

`HP4_DIMENSIONAL_RELEASED`

↓

`HP5_CRIMP_RELEASED`

↓

`MANUFACTURING_RELEASED_REV1`

↓

Prototype build / pre-cover acceptance

↓

First-power / first-start qualification

↓

`GOLDEN_HARNESS_VALIDATED`

↓

`AS_BUILT_CONFIGURATION_FROZEN`

↓

`REPEAT_BUILD_RELEASED`

## Next recommended milestone

Build the **Physical Measurement & Evidence Capture Master Pack** so all remaining bike-side measurements, connector photographs, device IDs and branch dimensions can be captured in one controlled workshop session instead of piecemeal.
