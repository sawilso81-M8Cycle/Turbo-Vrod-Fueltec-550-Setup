# Remaining G0/G1 Blocker Burn-Down Review

## Purpose

Convert the remaining pre-manufacture blockers into a short, ranked closure plan aimed directly at `MANUFACTURING_RELEASED_REV1`.

This review supersedes the older interpretation of several Master Build Blocker Register rows where architecture has since been frozen by later milestones.

## Architecture-frozen items

The following items are no longer open at architecture level:

- BG-004 FT550 connector build method: official FT550 connector-kit/custom harness architecture frozen.
- BG-006 fuel-pump harness-side service interface: HDSCS / AMP MCP high-current service-break family frozen around 4.0 mm² feed and return.
- BG-007 X51 CAN service architecture: Deutsch DTM 4-way service stub frozen; final network termination state remains verification-gated.
- BG-008 X70 Two-Step functional relay architecture: TE 1393292-5 relay baseline frozen; exact socket/carrier remains DFM gated.
- BG-009 injector harness topology: direct-drive / Peak & Hold selectable serviceable architecture frozen; injector electrical class remains measurement gated.
- B15 primary PMU feed architecture: 10 mm² baseline, primary positive distribution and J-P02 ground-star architecture frozen.
- B39 injector-power architecture: separate engine-critical protected branch frozen.
- B40 ignition/SparkPRO power architecture: separate engine-critical protected branch frozen.

## Remaining G0/G1 blockers ranked by closure priority

### Priority 1 – Device/load evidence

1. **Fuel pump actual PN + electrical load evidence**
   - steady current;
   - cold/hot inrush;
   - system voltage during test;
   - connector temperature;
   - branch voltage drop.
   - Final decision: `DIRECT_PMU_DRIVE_APPROVED` or `EXTERNAL_POWER_STAGE_REQUIRED`.

2. **Injector electrical class**
   - front/rear injector PN confirmation;
   - DC resistance at known temperature;
   - current waveform / peak and hold characteristics;
   - FT550 compatibility evidence.
   - Final decision: `DIRECT_DRIVE_APPROVED` or `PEAK_HOLD_REQUIRED`.

3. **Ignition / coil current and dwell evidence**
   - coil PN confirmation;
   - current ramp vs dwell;
   - first-start conservative dwell;
   - B40 aggregate current and protection.

4. **Radiator fan / charge-cooler pump load evidence**
   - exact device PN;
   - steady/inrush current;
   - final conductor and protection decision;
   - direct PMU vs external stage.

### Priority 2 – Connector and terminal closure

5. **PMU used-cavity terminal audit**
   - every used PMU cavity mapped to exact Sicma terminal family;
   - confirm conductor range, current, insulation OD and tooling compatibility.

6. **OEM X10-X23 connector / repair-pigtail identification**
   - CKP, TPS, MAP, ECT, IAT, VSS, injectors and coils;
   - exact bare connector when verified, otherwise controlled OEM repair-pigtail service break.

7. **X70 relay socket/carrier**
   - exact repeatable Micro-ISO socket/carrier PN;
   - terminal PNs and wire range;
   - protected mounting location;
   - powered truth-table / release-time verification.

8. **X50 general service connector**
   - circuit count and package location frozen;
   - exact housing/contact/seal/boot/cap PNs.

### Priority 3 – Electrical calculation closure

9. **B15 master protection value**
   - simultaneous load model;
   - primary cable protection coordination;
   - J-P01 hardware current capability.

10. **B39 injector supply protection value**
    - dependent on injector electrical decision.

11. **B40 ignition supply protection value**
    - dependent on coil current/dwell evidence.

12. **CAN completed-network termination verification**
    - record FT550 termination state;
    - record PMU termination state;
    - record any external resistor;
    - powered-down H-L resistance consistent with documented topology.

### Priority 4 – Manufacturer closure

13. **Builder DFM review**
    - wire series;
    - connector/terminal availability;
    - crimp tooling;
    - DR-25 / boots / transitions;
    - X70 socket implementation;
    - manufacturing tolerances;
    - proposed substitutions.

14. **Deviation approval**
    - every substitution given unique ID and written disposition.

## Physical G2 items remain separate

The following are not solvable by more desk engineering and remain motorcycle-fit gates:

- major component mounting positions;
- D00-D10 physical datum freeze;
- B01-B44 final routed lengths;
- B20-B31 DNP/defined disposition;
- full-lock steering movement;
- rear suspension movement;
- turbo/exhaust thermal clearance;
- final 1:1 formboard after prototype fit.

## Shortest path to manufacturing release

Recommended execution order:

`Pump verification` → `Injector verification` → `Coil/dwell verification` → `Fan/pump load verification` → `PMU terminal audit` → `OEM connector physical ID` → `X70 socket freeze` → `X50 freeze` → `B15/B39/B40 protection closeout` → `CAN termination closeout` → `Manufacturer DFM` → `Engineering release`.

## Current state

**G0_G1_BURN_DOWN_ACTIVE**

The architecture is now substantially frozen. Remaining blockers are primarily evidence, exact part-number, protection-setting and physical-verification tasks rather than new design work.
