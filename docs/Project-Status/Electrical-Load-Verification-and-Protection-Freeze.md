# Electrical Load Verification & Protection Freeze

## Purpose

Close PBR-007, PBR-008, PBR-010, PBR-012, PBR-013 and PBR-014 using measured electrical evidence rather than nominal assumptions.

This milestone converts the provisional high-current architecture into the released protection baseline for the Turbo V-Rod FT550 / PMU16 harness.

## Entry conditions

Before powered load testing:

- exact Pump 1 and Pump 2 hardware is identified;
- exact injector hardware is identified;
- exact ignition coil and SparkPRO hardware is identified;
- conductor sizes and terminal families for the tested circuit are known;
- battery/charging source is suitable for the test;
- fuel-system testing is performed safely with the required pressure monitoring;
- test instruments are suitable for expected current and voltage;
- emergency isolation is available;
- no circuit is protected above the rating of its weakest verified conductor/terminal/component.

## Locked baseline

Pump 1 and Pump 2 power feeds and dedicated returns remain minimum 4.0 mm² unless a later engineering revision deliberately increases them.

This milestone does not automatically approve PMU direct switching. Pump current and PMU output capability must be compared using verified data.

## ELV-0 Instrument and test setup

Record:

- DMM make/model/serial if available;
- current clamp/shunt make/model/range;
- voltage measurement points;
- battery voltage before test;
- charging/supply voltage where relevant;
- fuel pressure/reference condition;
- ambient temperature;
- conductor/connector configuration;
- PMU firmware/config revision;
- FT550 configuration revision where relevant.

Output: `ELV0_TEST_SETUP_ACCEPTED`

## ELV-1 Fuel Pump 1 electrical characterization

Measure under representative operating conditions:

- supply voltage at source;
- voltage at pump connector;
- steady-state current;
- start/inrush current where instrument bandwidth permits meaningful capture;
- fuel pressure;
- connector/terminal temperature trend where practical;
- voltage drop across feed path;
- voltage drop across return path.

Repeat at relevant pressure/load conditions where pump demand changes materially.

Output: `PUMP1_ELECTRICAL_LOAD_VERIFIED`

## ELV-2 Fuel Pump 2 electrical characterization

Repeat ELV-1 for Pump 2.

Output: `PUMP2_ELECTRICAL_LOAD_VERIFIED`

## ELV-3 Pump switching decision

For each pump compare:

- measured continuous current;
- measured/credible transient current;
- PMU output continuous capability;
- PMU transient/current-limit behaviour;
- ambient/thermal derating requirements;
- connector/terminal ratings;
- conductor capability;
- desired fault containment;
- consequence of nuisance current limiting.

Decision options:

- `PMU_DIRECT_APPROVED`;
- `EXTERNAL_RELAY_REQUIRED`;
- `EXTERNAL_SOLID_STATE_POWER_STAGE_REQUIRED`;
- `ARCHITECTURE_REVIEW_REQUIRED`.

Do not parallel PMU outputs or increase current limits unless explicitly permitted by verified ECUMASTER documentation for the exact configuration.

Output: `FUEL_PUMP_POWER_ARCHITECTURE_FROZEN`

## ELV-4 Injector electrical verification / B39

Record exact injector PN and verified electrical data. Where practical confirm measured resistance/current characteristics against the source data.

Verify:

- injector driver compatibility;
- B39 supply conductor/terminal path;
- expected simultaneous injector load;
- fuse/current-limit strategy;
- voltage drop under representative operation;
- no inappropriate sharing with precision sensor supply.

Output: `INJECTOR_ARCHITECTURE_FROZEN`

## ELV-5 SparkPRO / coil verification / B40

Record exact coil PN and SparkPRO revision.

Verify:

- coil/SparkPRO compatibility from authoritative data;
- dwell source and released dwell configuration;
- B40 supply current under representative operation;
- conductor/terminal capability;
- protection/current-limit strategy;
- voltage stability during ignition operation;
- thermal behaviour where relevant.

Do not infer safe dwell solely from idle operation.

Output: `IGNITION_ARCHITECTURE_FROZEN`

## ELV-6 Fan and auxiliary load verification

For radiator fan, charge-cooler pump and other material PMU loads, record:

- exact hardware PN where available;
- steady current;
- startup/transient current where relevant;
- supply voltage;
- PMU channel;
- conductor/terminal size;
- protection/current-limit setting;
- thermal evidence.

Output: `AUXILIARY_LOADS_VERIFIED`

## ELV-7 B15 primary feed validation

B15 must be coordinated against the aggregate system demand and downstream branch protection.

Record/verify:

- conductor size/type;
- terminal/ring/stud hardware;
- primary protection hardware;
- measured system current in representative states;
- cranking behaviour where applicable;
- running/charging voltage;
- voltage drop;
- thermal evidence;
- downstream protection relationship.

Output: `B15_PRIMARY_PROTECTION_VERIFIED`

## ELV-8 Protection coordination freeze

For every controlled high-current circuit establish:

1. measured normal continuous load;
2. credible transient/start load;
3. conductor capability;
4. terminal/connector capability;
5. load/device maximum requirement;
6. PMU output capability if directly switched;
7. selected fuse/current limit;
8. time/transient rationale where applicable;
9. fault containment relationship;
10. evidence source.

The selected protection shall protect the wiring and connection system while avoiding nuisance operation during verified normal transients.

No fuse/current-limit value is to be selected merely by rounding the measured current upward.

Output: `PROTECTION_COORDINATION_FROZEN`

## ELV-9 Regression / fault review

Before release verify that a single branch fault cannot unnecessarily remove unrelated engine-critical domains where segregation is intended.

Review:

- Pump 1 fault;
- Pump 2 fault;
- injector B39 fault;
- ignition B40 fault;
- fan fault;
- auxiliary pump fault;
- PMU output fault;
- primary B15 fault;
- ground-path fault.

Output: `HIGH_CURRENT_FAULT_CONTAINMENT_REVIEWED`

## Release gate

The milestone passes only when applicable ELV stages have evidence and no unresolved protection value remains provisional for manufacturer release.

Required outputs:

`PUMP1_ELECTRICAL_LOAD_VERIFIED`

`PUMP2_ELECTRICAL_LOAD_VERIFIED`

`FUEL_PUMP_POWER_ARCHITECTURE_FROZEN`

`INJECTOR_ARCHITECTURE_FROZEN`

`IGNITION_ARCHITECTURE_FROZEN`

`HIGH_CURRENT_LOADS_VERIFIED`

`PROTECTION_COORDINATION_FROZEN`

Successful completion unlocks final production-schedule freeze and `HARNESS_DOCUMENT_SET_FROZEN`.
