# CAN & Service Interface Production Freeze – Rev 1

## Purpose

Close BG-007 / PMA-013 and define the production architecture for the FT550 ↔ PMU16 CAN backbone and external service access without introducing accidental termination or unsafe power paths.

## Production architecture

The Rev 1 CAN network shall be a linear backbone:

`FT550 CAN endpoint ↔ twisted-pair trunk ↔ PMU16 CAN endpoint`

X51 is a service/debug access stub only. It shall not become a third permanent termination point.

## X51 service connector

Freeze X51 as a **Deutsch DTM 4-way sealed service connector** with the following controlled cavity functions:

| Cavity | Function | Wire | Rule |
|---|---|---:|---|
| 1 | CAN-H | 0.35 mm² | twisted with cavity 2 conductor |
| 2 | CAN-L | 0.35 mm² | twisted with cavity 1 conductor |
| 3 | Service ground | 0.75 mm² preferred | diagnostic/reference use only; not a high-current return |
| 4 | Optional protected service +12 V | 0.75 mm² | may be DNP; must be separately protected and labelled |

Preferred connector family:

- harness side: Deutsch DTM 4-way plug/receptacle pair selected to suit installation gender and cap strategy;
- contacts: genuine size-20 DTM contacts matched to the selected 0.35/0.75 mm² conductor range;
- unused cavity: fit correct sealing plug if service +12 V is DNP;
- external half: provide a sealing/dust cap when not connected.

Exact housing/contact/cap manufacturer PNs shall be recorded in the purchasing BOM before manufacturer release. Equivalent visually similar connectors are not acceptable without engineering approval.

## X51 stub length

Target finished stub length: **≤300 mm**, with the existing prototype baseline of approximately 250 mm retained.

CAN-H and CAN-L shall remain twisted through the service branch as far as practical. Do not untwist the pair for convenience through a long breakout.

## Termination

The completed powered-down network shall contain exactly the termination required by the verified FT550/PMU configuration.

No termination resistor is to be hidden inside X51.

Before first power:

1. identify whether FT550 termination is internal/configurable/external for the selected CAN port;
2. identify PMU16 termination configuration;
3. record all fitted 120 Ω terminations;
4. measure CAN-H to CAN-L resistance at X51 with the system powered down;
5. where two 120 Ω endpoint terminations are intentionally fitted, approximately 60 Ω is expected;
6. any materially different result requires investigation before power.

Do not force a 60 Ω target if the selected hardware/manual configuration deliberately uses a different topology. The as-built termination record is authoritative.

## Service power

X51 cavity 4 is optional. If fitted:

- it must be a protected service supply, not an unfused battery feed;
- conductor baseline is 0.75 mm²;
- protection/current limit shall be appropriate for the intended CAN interface/logger;
- connector label must identify voltage and maximum permitted service load;
- service equipment shall not back-feed the vehicle electrical system.

If no powered service device is required, cavity 4 shall be DNP and sealed.

## X50 engineering/service break

X50 remains the controlled engineering/service break for the wider harness where required. X50 shall not be used to create an additional CAN star branch. If CAN passes through X50, the pair must preserve polarity, twist and backbone continuity.

The final X50 housing is installation/package dependent and remains procurement-open until its exact circuit count is frozen. X50 is therefore separated from the now-frozen X51 CAN service connector.

## CAN wiring requirements

- 2 × 0.35 mm² automotive/motorsport twisted pair minimum baseline;
- maintain CAN-H/CAN-L polarity end-to-end;
- no chassis-ground conductor is part of the differential pair;
- route away from SparkPRO driven outputs, coil primary power, injector power, starter and fuel-pump high-current conductors;
- cross noisy conductors approximately at right angles where unavoidable;
- no undocumented splice or branch;
- label both ends and X51 with controlled circuit IDs;
- continuity and isolation test before connecting electronics.

## Acceptance tests

The manufacturer shall provide evidence of:

- CAN-H end-to-end continuity;
- CAN-L end-to-end continuity;
- no H/L reversal;
- no H-to-L short;
- no H/L short to +12 V or ground;
- X51 cavity mapping;
- X51 stub length;
- twisted-pair construction;
- powered-down termination resistance;
- successful FT550 ↔ PMU communication after commissioning configuration is loaded;
- no bus errors attributable to harness construction during cranking and ignition operation.

## Release state

**X51_CAN_SERVICE_ARCHITECTURE_FROZEN**

**CAN_TERMINATION_CONFIGURATION_VERIFICATION_GATED**

BG-007 may be considered closed for X51 architecture. Final completed-network topology acceptance remains a commissioning/build gate until exact FT550 and PMU termination states are recorded and measured.
