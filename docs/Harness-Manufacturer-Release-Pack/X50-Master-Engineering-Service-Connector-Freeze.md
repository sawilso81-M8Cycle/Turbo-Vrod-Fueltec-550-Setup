# X50 Master Engineering / Service Connector Freeze – Rev 1

## Purpose

Define X50 as the controlled removable interface between the main vehicle harness and the engineering/service branch without compromising engine-critical reliability, CAN topology, sensor integrity or high-current segregation.

## Role of X50

X50 is **not** a universal bulkhead through which every circuit must pass.

It is reserved for low/medium-current engineering and service functions where a removable branch materially improves commissioning, logging, troubleshooting or future expansion.

The following shall **not** be routed through X50 merely for convenience:

- 4.0 mm² fuel-pump power or returns;
- B15 PMU main feed;
- starter or battery primary current;
- coil primary power where doing so adds an unnecessary contact pair;
- other high-current circuits already assigned dedicated service connectors;
- precision sensor grounds unless the released circuit architecture explicitly requires passage through X50.

## Connector family baseline

Freeze X50 to a **sealed Deutsch DT/DTM or equivalent motorsport multiway family selected by final circuit count and conductor range**.

Preferred production philosophy:

- DTM size-20 contacts for low-current signal circuits up to the verified conductor range;
- DT size-16 contacts where 0.75–2.0 mm² service circuits require the larger contact family;
- use separate keyed connectors rather than mixing incompatible current/contact classes if the final circuit set demands it.

The exact housing PN is frozen only after the final X50 circuit count and contact mix are confirmed. The manufacturer may nominate a genuine TE/Deutsch housing during DFM, but substitutions require engineering approval.

## Recommended circuit allocation

X50 should preferentially carry only the engineering/service circuits actually required. Candidate functions are:

1. CAN-H pass-through/service access where required;
2. CAN-L pass-through/service access where required;
3. service ground/reference;
4. protected service +12 V if required;
5. spare digital input;
6. spare digital output/control;
7. spare analogue input;
8. logger/engineering enable;
9. future sensor signal;
10. future sensor reference/return only where explicitly designed.

Unused cavities are to be sealed and recorded as SPARE/DNP. No cavity may be silently repurposed.

## CAN rule

X50 must not create a CAN star network.

If CAN passes through X50:

- CAN-H and CAN-L remain a twisted pair;
- H/L polarity is preserved;
- pair untwist at the connector is minimised;
- there is no termination resistor inside X50;
- the service branch remains governed by the separate X51 CAN Service Interface Freeze;
- connector removal must not leave an undocumented termination condition.

Where practical, keep X51 as the primary diagnostic CAN access and omit CAN from X50 unless X50 genuinely needs it.

## Sensor/reference rule

X50 is not permitted to merge power ground and sensor ground.

If a precision analogue circuit crosses X50:

- signal and its intended reference/return are documented as a pair/group;
- 5 V reference is protected from accidental service +12 V adjacency where possible;
- cavity arrangement should reduce the consequence of mis-pinning;
- shielding/drain strategy is preserved where applicable;
- no high-current return shares the connector.

CKP/CAM should remain on their dedicated trigger path and should not be routed through X50 unless packaging makes it unavoidable and trigger-integrity testing explicitly accepts it.

## Service power

Any +12 V at X50 shall be:

- separately protected;
- labelled `SERVICE_12V`;
- sized for the intended diagnostic load only;
- incapable of back-feeding the PMU/FT550 or vehicle supply from an external tool;
- isolated or omitted if no powered engineering accessory requires it.

## Mechanical requirements

X50 shall:

- be sealed for the installation environment;
- have positive latch/secondary lock as applicable;
- be positioned where it can be serviced without exhaust/turbo heat exposure;
- be strain-relieved on both harness halves;
- have a mounting/retention strategy that prevents connector mass hanging from individual wires;
- use cavity plugs in every unused sealed position;
- be labelled `X50 ENGINEERING/SERVICE` on the harness drawing and physical loom.

## Harness-builder release data

Before X50 can be marked production-frozen, the builder shall return:

- proposed housing pair PN;
- wedge/secondary-lock PN where separate;
- terminal PN by conductor size;
- seal PN where separate;
- cavity-plug PN;
- backshell/boot/strain-relief proposal if used;
- crimp-tool recommendation;
- cavity-count confirmation;
- DFM comments;
- availability and repeat-build sourcing.

## Acceptance tests

- cavity-to-cavity continuity against released schedule;
- no adjacent-cavity short;
- insulation/isolation to chassis and +12 V where applicable;
- CAN polarity/continuity if CAN fitted;
- service-power polarity and protection if fitted;
- no service-power backfeed;
- connector latch/retention check;
- seal/cavity-plug inspection;
- pull/strain-relief inspection;
- final photograph before loom covering;
- label verification.

## Release state

Architecture state:

`X50_SERVICE_INTERFACE_ARCHITECTURE_FROZEN`

Procurement state:

`X50_EXACT_HOUSING_AND_CAVITY_COUNT_DFM_GATED`

Final state after DFM and cavity schedule approval:

`X50_PRODUCTION_CONNECTOR_FROZEN`
