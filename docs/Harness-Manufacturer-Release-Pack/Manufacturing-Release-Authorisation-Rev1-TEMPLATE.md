# Manufacturing Release Authorisation – Rev 1 TEMPLATE

> **CONTROLLED TEMPLATE – NOT AN ACTIVE RELEASE**

## Project

Turbo V-Rod Destroyer – FuelTech FT550 / ECUMASTER PMU16 / SparkPRO complete replacement harness.

## Release statement

This document becomes valid only when every required field is completed, HP-1 through HP-5 are PASS, all applicable Class 3 review items are PASS, and Engineering changes the release state below from `NOT_RELEASED` to `MANUFACTURING_RELEASED_REV1`.

## Release identification

- Release revision: Rev 1
- Release date: TBD
- Released by: TBD
- Manufacturer: TBD
- Manufacturer quotation/reference: TBD
- Controlled repository commit/tag: TBD
- Rev 2 issue-package ZIP SHA-256: TBD
- Approved manufacturer return package reference: TBD

## Hold points

| Hold point | Requirement | State |
|---|---|---|
| HP-1 | DFM return accepted | TBD |
| HP-2 | Connector procurement accepted | TBD |
| HP-3 | Electrical blocker closure | TBD |
| HP-4 | Dimensional release / approved measurement exception | TBD |
| HP-5 | Crimp release | TBD |

## Critical engineering decisions

- Fuel pump switching: TBD
- Pump feed/return: **4.0 mm² minimum each**
- Injector driver architecture: TBD
- B39 conductor/protection: TBD
- SparkPRO/coil dwell release: TBD
- B40 conductor/protection: TBD
- B11 radiator fan switching/protection: TBD
- B12 charge-cooler pump: TBD / DNP
- B15 PMU feed: **10 mm² baseline**; final protection TBD
- PMU hardware revision: TBD
- PMU cavity/terminal audit revision: TBD
- CAN topology/termination: TBD
- X70 Two-Step relay/socket: TBD
- X50 connector: TBD
- X51 connector: TBD
- OEM X10–X23 interface register revision: TBD

## Approved deviations

List approved deviation IDs only. Any unlisted deviation is not authorised.

- TBD

## Approved open G2 exceptions

Only physical/dimensional items explicitly listed here may remain open at functional prototype manufacture.

- TBD

## Manufacturer instructions

Manufacture exactly to the controlled released documents and approved deviations referenced by this authorisation.

No substitution, wire downsize, cavity reassignment, CAN termination change, grounding change, sensor-interface change or routing deviation is permitted without a new RFI/deviation approval.

Pre-cover inspection remains a mandatory hold point. The manufacturer shall not permanently sleeve/close the loom until the required evidence is accepted.

## Release state

`NOT_RELEASED`

This template must not be interpreted as manufacturing authority until that state is explicitly changed to:

`MANUFACTURING_RELEASED_REV1`
