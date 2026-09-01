# Pre-Manufacture Release Audit – Rev 1 Harness

## Purpose

This audit is the formal bridge between engineering development and authorisation for a harness builder to manufacture the Rev 1 prototype.

It consolidates the Master Build Blocker Register, manufacturer release pack, dimensional freeze pack, high-current closure work, FT550/PMU16 interface freezes, injector/ignition/trigger gates and first-start controls.

## Release decision

The project shall remain:

`REV1_PROTOTYPE_BUILD_NOT_YET_AUTHORISED`

until all G0 and G1 build blockers are either CLOSED/PASS or have a documented engineering disposition explicitly allowing prototype manufacture.

G2 physical-fit items may only remain open when the manufacturer is being engaged specifically to measure/build the first vehicle-fitted prototype and the open dimensions are clearly marked as prototype measurement gates.

G3 documentation/improvement items must not conceal an electrical, thermal or mechanical safety dependency.

## Audit summary

### Closed at architecture level

- FT550 connector build strategy: official FuelTech connector-kit/custom-harness architecture frozen.
- PMU16 connector/terminal architecture: Sicma/FCI family frozen; conductor-to-terminal selection remains subject to final cavity/current audit.
- Fuel-pump conductor baseline: 4.0 mm² feed and 4.0 mm² dedicated return per pump frozen.
- Injector harness topology: X62/X63 serviceable direct-drive/Peak-and-Hold architecture frozen; electrical class remains measurement gated.
- SparkPRO ignition architecture: FT550 → SparkPRO → coils frozen; dwell/current remains measurement gated.
- Trigger architecture: CKP/CAM shielding/routing and verification process frozen; waveform/sync remains measurement gated.
- Two-Step architecture: PMU O11 → sealed relay → dry-contact ground to FT550 A21 frozen; exact relay hardware remains open.
- First-power/first-start staged release process frozen.

### G0/G1 blockers still requiring closure before unrestricted prototype build

1. Actual fuel-pump PN and steady/inrush/thermal verification.
2. Final pump switching decision: direct PMU only if verified within exact PMU hardware/output/terminal capability, otherwise external power stage.
3. Final B11/B12/B15/B39/B40 current/protection decisions.
4. Final PMU cavity-to-terminal-to-wire audit.
5. Physical identification of retained OEM sensor/injector/coil mating connectors or controlled repair-pigtail strategy.
6. Fuel-pump connector rated for the final current and 4.0 mm² conductors.
7. X50/X51 service/CAN connector kits and completed-network termination audit.
8. X70 relay/holder/suppression hardware selection and bench truth-table test.
9. Injector impedance/current evidence and final direct-drive vs Peak & Hold decision.
10. Harness-builder DFM review and controlled substitution/deviation response.

### G2 physical blockers

- major component mounting positions;
- D00-D10 datum positions;
- B01-B44 measured routed lengths;
- B20-B31 DNP/defined disposition;
- steering full-lock movement;
- suspension/full-travel movement;
- turbo/exhaust clearance and heat protection;
- final 1:1 formboard after Golden Harness fit.

## Prototype-build release categories

### A. RFQ only

Allowed immediately. Builder may quote materials, labour, NRE, lead time, DFM and repeat-build pricing. No harness manufacture is authorised.

State: `RFQ_READY`.

### B. Measurement / mock-up harness

Allowed only with engineering approval. May be used to establish branch dimensions and connector orientation. It must not be represented as electrically released for first power.

State: `PROTOTYPE_MEASUREMENT_BUILD_ONLY`.

### C. Electrically functional Rev 1 prototype

Requires every applicable G0/G1 blocker closed and physical open items explicitly controlled.

State: `MANUFACTURING_RELEASED_REV1`.

### D. Repeat production

Requires prototype fit, completed acceptance testing, accepted as-built dimensions/BOM and Golden Harness validation.

State: `GOLDEN_HARNESS_VALIDATED / REPEAT_BUILD_RELEASED`.

## Manufacturer RFIs

Any ambiguity involving connector cavity, wire size, ground domain, sensor polarity, CAN termination, PMU output, FT550 cavity, injector architecture, ignition architecture, pump switching or Two-Step wiring requires an RFI. The builder shall not make an undocumented assumption.

## Audit evidence package

Before `MANUFACTURING_RELEASED_REV1`, retain:

- completed `Pre-Manufacture-Release-Audit-Register.csv`;
- latest Master Build Blocker Register;
- completed connector/terminal procurement audit;
- high-current final decision register;
- injector electrical decision register;
- ignition/SparkPRO verification evidence applicable before build;
- trigger wiring release data applicable before build;
- dimensional worksheet or approved prototype-measurement exception;
- manufacturer DFM response;
- approved deviation register;
- engineering release signoff.

## Current audit result

**PRE_MANUFACTURE_AUDIT_RELEASED / BUILD_BLOCKERS_REMAIN**

Permitted now: RFQ, DFM review, component procurement review, bike measurement planning.

Not yet permitted: unrestricted electrically functional Rev 1 harness manufacture or first-power release.
