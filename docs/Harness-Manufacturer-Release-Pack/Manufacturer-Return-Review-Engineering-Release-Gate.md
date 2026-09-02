# Manufacturer Return Review & Engineering Release Gate

## Purpose

Define the controlled engineering review that converts a returned harness-builder DFM/RFI/deviation package into an approved Rev 1 manufacturing release.

This gate exists to prevent a quotation, DFM response or partial parts proposal from being mistaken for authorisation to build an electrically functional harness.

## Entry condition

The review begins only when the manufacturer has returned the applicable Rev 2 package items, including:

- completed `Harness-Manufacturer-DFM-Response-Register.csv`;
- completed RFIs;
- proposed deviations;
- connector/terminal/boot/wire datasheets;
- quotation and lead-time information;
- proposed test and document-control process;
- any requested sample crimps, photos or tooling information.

## Review classes

### Class 1 – Commercial / informational

Includes pricing, lead time, MOQ, NRE, standard build-process description and availability.

These items may be accepted without affecting electrical release.

### Class 2 – DFM implementation

Includes connector housings, terminals, seals, boots, strain relief, wire family, sleeving, labels, splice processes and formboard method.

These require engineering acceptance before procurement/build release.

### Class 3 – Electrical / safety critical

Includes:

- PMU cavity/terminal/wire selection;
- 4.0 mm² fuel-pump interfaces;
- direct PMU vs external pump stage;
- B11/B12 switching/protection;
- B15 protection;
- B39/B40 protection;
- injector direct-drive vs Peak & Hold;
- X70 Two-Step hardware;
- CAN topology/termination;
- CKP/CAM routing or shielding;
- sensor/reference-ground architecture.

Class 3 items must be supported by the applicable measurement, authoritative documentation and/or test evidence. Manufacturer preference alone is not sufficient.

## Mandatory review questions

For every returned DFM line, RFI and deviation ask:

1. Does it preserve the released electrical function?
2. Does it accept the specified conductor size and insulation OD?
3. Is the current/temperature rating adequate with margin?
4. Does it preserve sensor-ground and high-current-ground segregation?
5. Does it change CAN topology or termination?
6. Does it alter CKP/CAM signal integrity?
7. Does it introduce an undocumented splice or branch?
8. Does it create a serviceability problem?
9. Does it create turbo/exhaust thermal exposure?
10. Is the part repeatably purchasable?
11. Is the proposed crimp tooling/workmanship method controlled?
12. Does the proposal require an update to any released drawing/register/BOM?

## Scoring

Each applicable review item receives one of:

- `PASS` – acceptable as returned;
- `PASS_WITH_DOCUMENT_UPDATE` – technically acceptable but controlled docs must be revised before release;
- `RFI_REQUIRED` – insufficient/ambiguous information;
- `REJECT` – not acceptable;
- `NOT_APPLICABLE`.

No Class 3 item may remain `RFI_REQUIRED` or `REJECT` at manufacturing release.

## Release blockers that must be closed

Before `MANUFACTURING_RELEASED_REV1`, all applicable G0/G1 blockers must be closed or formally dispositioned. At minimum this includes:

- fuel-pump PN/current/inrush evidence and final switching architecture;
- injector electrical class and direct-drive/Peak & Hold decision;
- coil/SparkPRO dwell-current evidence and B40 acceptance;
- radiator fan and charge-cooler pump disposition/current evidence;
- PMU cavity-terminal-wire audit;
- X10–X23 OEM connector/pigtail resolution;
- X70 socket/carrier and bench truth-table acceptance;
- X50/X51 exact connector selections as applicable;
- B15/B39/B40 protection closeout;
- CAN termination/topology acceptance;
- manufacturer DFM/substitution review.

G2 dimensional/physical gates may remain open only under a documented prototype-measurement exception that does not compromise electrical safety.

## Required engineering outputs

The review shall produce:

- completed `Manufacturer-Return-Review-Register.csv`;
- updated DFM/RFI/deviation registers with dispositions;
- approved connector/terminal BOM changes;
- approved wire/sleeving/splice changes;
- updated cavity and wire schedules;
- updated dimensional exception list if applicable;
- `Manufacturing-Release-Authorisation-Rev1.md` only when all release conditions are met.

## Hold-point promotion

### HP-1 DFM return accepted

All manufacturer responses are reviewed and no critical ambiguity remains.

### HP-2 Connector procurement accepted

Exact housings, terminals, seals, cavity plugs, boots and tooling are accepted.

### HP-3 Electrical blocker closure

All applicable Class 3 electrical blockers are closed.

### HP-4 Dimensional release

Physical dimensions are frozen or an approved measurement-build exception exists.

### HP-5 Crimp release

Every used cavity/terminal/wire combination is signed off.

Only after HP-1 through HP-5 pass may the engineering release be promoted to:

`MANUFACTURING_RELEASED_REV1`

## Automatic stop conditions

Release is blocked immediately if any of the following appears in the manufacturer return:

- proposed fuel-pump conductor below 4.0 mm²;
- proposed B15 conductor below 10 mm² without approved engineering change;
- +12 V introduced to FT550 A21 Two-Step contact path;
- hidden CAN termination;
- sensor ground merged into a high-current return;
- unverified visually matched OEM connector;
- terminal outside approved wire range;
- unresolved PMU cavity ambiguity;
- unapproved injector-driver architecture change;
- missing thermal/clearance mitigation in a known turbo/exhaust zone.

## Current state

`MANUFACTURER_RETURN_REVIEW_GATE_RELEASED / AWAITING_MANUFACTURER_RETURN`

The existence of this review process does not itself authorise manufacture.
