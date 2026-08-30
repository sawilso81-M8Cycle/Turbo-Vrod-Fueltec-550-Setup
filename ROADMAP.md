# Turbo V-Rod FuelTech FT550 Development Roadmap

## Milestone 1 — Source Baseline

**Status: IN PROGRESS / substantially established**

- [x] Add FuelTech FT550/FT600 official manual references.
- [x] Add FT550 connector-kit reference.
- [x] Add FuelTech PROBIKE motorcycle-harness reference.
- [x] Record Harley VRXSE/VRSC factory publication set.
- [x] Record key 70155-03 engine-harness cross-model finding.
- [x] Record known VRXSE sensor part numbers.
- [x] Add ECUMASTER PMU-16 official manual and pinout references.
- [x] Add PMU-16 architecture evaluation for Turbo V-Rod use.
- [ ] Obtain/archive permitted working copies of the exact Harley publications used for engineering access.
- [ ] Confirm every quoted drawing page/circuit against the exact publication revision.

## Milestone 2 — Master Sensor Matrix

**Status: STARTED**

- [x] CKP working cross-reference.
- [x] TPS working cross-reference.
- [x] MAP working cross-reference.
- [x] ECT working cross-reference.
- [x] IAT working cross-reference.
- [x] VSS working cross-reference.
- [x] Oil-pressure-switch working cross-reference.
- [x] Neutral-switch working cross-reference.
- [x] Record no OEM cam-sync sensor currently identified.
- [ ] Verify Harley connector cavity for every sensor.
- [ ] Verify wire colour at the actual 70155-03 harness.
- [ ] Verify sensor supply voltage.
- [ ] Verify transfer curve / resistance curve / pulse specification.
- [ ] Assign final SIM terminal numbers.
- [ ] Freeze FT550 A/B connector cavity assignment.

## Milestone 3 — Turbo Instrumentation

- [ ] Select fuel-pressure transducer and range.
- [ ] Select engine-oil-pressure transducer and range.
- [ ] Decide whether separate turbo-oil-pressure monitoring is required.
- [ ] Select wideband lambda hardware and communications method.
- [ ] Decide EGT strategy: none / front only / front + rear.
- [ ] Define wastegate/dome pressure sensing if closed-loop dome control is used.
- [ ] Define IAT location downstream of compression/intercooling appropriate to tuning strategy.
- [ ] Finalise FT550 internal 7-bar MAP plumbing if later used as secondary/reference source; OEM MAP remains the current requested hardware baseline.

## Milestone 4 — Trigger Validation

- [ ] Bench resistance/continuity checks on CKP.
- [ ] Oscilloscope CKP waveform while cranking.
- [ ] Confirm polarity into A19/A18.
- [ ] Confirm stable FT550 cranking RPM.
- [ ] Determine trigger pattern/configuration from verified physical and service data.
- [ ] Verify commanded/mechanical timing with timing light.
- [ ] Decide whether crank-only operation is sufficient.
- [ ] If required, engineer and validate a cam-sync system.

## Milestone 5 — EPM / APM / SIM Detailed Design

### EPM

- [ ] FT550 protected feed and ground.
- [ ] Injector supply and switching architecture.
- [ ] Ignition-coil supply and control architecture.
- [ ] Engine-critical relay / solid-state protection design.
- [ ] Evaluate whether any engine-critical loads should be migrated to PMU-16 after failure-mode analysis.
- [ ] Fuse / electronic protection schedule.

### APM

- [x] ECUMASTER PMU-16 identified as preferred APM backbone.
- [x] Create initial PMU-16 output allocation structure in HD-style wiring package.
- [ ] Measure/verify steady-state and inrush current for every candidate load.
- [ ] Define per-output current limits, retry behaviour and fault actions.
- [ ] Freeze primary fuel-pump circuit.
- [ ] Freeze secondary fuel-pump circuit if used.
- [ ] Freeze cooling-fan circuits.
- [ ] Freeze boost-solenoid supply/control.
- [ ] Freeze auxiliary pump/accessory circuits.
- [ ] Inrush and flyback protection review.
- [ ] Bench-test PMU switching while monitoring FT550 analogue channels for induced noise.

### SIM

- [x] Define project sensor-reference splice architecture.
- [x] Define precision sensor-return topology.
- [x] Define CKP as dedicated twisted/shielded branch.
- [ ] Freeze exact FT550 5 V and sensor-ground cavities.
- [ ] Freeze analogue sensor input cavities.
- [ ] Freeze digital switch inputs.
- [ ] Speed input conditioning if required.
- [ ] Communications routing.
- [ ] Connector and service-test-point definition.

## Milestone 5A — FT550 ↔ PMU-16 Communications

- [ ] Obtain/verify ECUMASTER CAN documentation relevant to PMU-16.
- [ ] Determine whether direct FT550-to-PMU command/status exchange is supported in the desired configuration.
- [ ] Define CAN bus bitrate, termination and physical topology.
- [ ] Define default safe states on CAN loss.
- [ ] Identify PMU current, voltage, state and fault channels to log.
- [ ] Keep critical enable paths hardwired where CAN loss must not create an unsafe state.
- [ ] Bench-validate CAN messaging before assigning any safety-critical dependency to it.

No CAN identifiers or payload definitions may be guessed.

## Milestone 6 — Full VRXSE-to-FT550 Master Wiring Matrix

**Status: REV 0 COMPLETE / verification remains open**

- [x] Create HD-style multi-sheet wiring package.
- [x] Create master wire and connector schedule.
- [x] Map known OEM sensors to working FT550 cavities.
- [x] Establish PMU-16 working output allocation.
- [x] Establish EPM/APM/SIM domain boundaries.
- [ ] Eliminate every release-blocking `VERIFY` item.

No production matrix row may contain an unresolved critical `VERIFY` item.

## Milestone 6A — Production Connector and Harness Definition

**Status: STARTED / framework complete**

- [x] Create project connector index X01-X51.
- [x] Create cavity-by-cavity termination schedule.
- [x] Create sensor splice and ground reference SP-S01/J-P01/G01 series.
- [x] Create physical harness branch schedule B01-B16.
- [x] Create formal Verification Register V001-V035.
- [x] Create Rev 1 Production Harness Release Checklist.
- [ ] Identify exact FT550 remaining cavities from repository-authorised source material.
- [ ] Identify exact PMU-16 connector cavities from repository-authorised source material.
- [ ] Identify OEM injector connector family/terminals.
- [ ] Identify OEM coil connector family/terminals and electrical driver type.
- [ ] Freeze wire gauge for every conductor after measured load/current data.
- [ ] Select terminal part numbers, seals, backshells and cavity plugs.
- [ ] Measure physical branch lengths after FT550/PMU mounting locations are frozen.
- [ ] Produce Rev 1 released connector drawings with zero critical `VERIFY` entries.

Reference folder: `docs/Production-Harness-Milestone/`

## Milestone 7 — Outputs and Vehicle Functions

After the sensor side is frozen, map and verify:

- [ ] front injector;
- [ ] rear injector;
- [ ] front ignition coil;
- [ ] rear ignition coil;
- [ ] fuel pump(s);
- [ ] radiator fan(s);
- [ ] starter/request logic as required;
- [ ] boost-control solenoid;
- [ ] launch / 2-step input;
- [ ] air-shifter input/output if fitted;
- [ ] warning lamp / fault output;
- [ ] tachometer / dash compatibility if retained;
- [ ] data-logging outputs / CAN.

## Milestone 8 — Bench Harness Commissioning

- [ ] Continuity test every conductor.
- [ ] Insulation/short check between domains.
- [ ] Validate all fuse/electronic protection values.
- [ ] Power ECU with actuators disconnected.
- [ ] Validate 5 V reference.
- [ ] Validate every sensor channel.
- [ ] Cycle pumps/fans/solenoids and watch analogue channels for induced noise.
- [ ] Validate PMU-16 current sensing and trip/retry behaviour on every configured output.
- [ ] Crank with fuel/ignition disabled and validate trigger.
- [ ] Confirm emergency stop / master isolation behaviour.

## Milestone 9 — First Start and NA/Low-Load Validation

- [ ] First start without boost demand.
- [ ] Lock ignition timing.
- [ ] Verify oil pressure immediately.
- [ ] Verify fuel pressure against manifold pressure.
- [ ] Verify coolant and IAT plausibility.
- [ ] Verify lambda.
- [ ] Verify PMU current draw and fault status under running conditions.
- [ ] Heat-cycle and inspect harness/connectors.
- [ ] Save first verified FT550 configuration baseline.
- [ ] Save matching PMU configuration baseline.

## Milestone 10 — Boost Commissioning

- [ ] Wastegate-spring/base-boost testing.
- [ ] Fuel-pressure differential validation under boost.
- [ ] Lambda validation by cylinder where instrumentation permits.
- [ ] IAT/ECT/EGT trend review.
- [ ] Progressive boost-control enablement.
- [ ] Engine-protection thresholds.
- [ ] PMU protection thresholds reviewed against measured race-load currents.
- [ ] Data-log review after every stage.

## Final release gate

The harness and configuration may be marked production-ready only when:

1. all critical circuits have primary-source provenance;
2. every FT550 pin assignment is frozen;
3. every sensor calibration is verified;
4. CKP polarity and timing are physically validated;
5. high-current switching does not corrupt sensor readings;
6. PMU-16 output allocation and current limits are fully validated;
7. protection strategies have been tested;
8. as-built wiring matches the released drawings;
9. the final FT550 configuration is archived with the hardware revision;
10. the matching PMU configuration is archived;
11. the Production Harness Verification Register contains zero release-blocking `VERIFY` entries.
