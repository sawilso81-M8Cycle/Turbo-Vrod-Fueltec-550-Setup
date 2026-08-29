# Turbo V-Rod FuelTech FT550 Development Roadmap

## Milestone 1 — Source Baseline

**Status: IN PROGRESS / substantially established**

- [x] Add FuelTech FT550/FT600 official manual references.
- [x] Add FT550 connector-kit reference.
- [x] Add FuelTech PROBIKE motorcycle-harness reference.
- [x] Record Harley VRXSE/VRSC factory publication set.
- [x] Record key 70155-03 engine-harness cross-model finding.
- [x] Record known VRXSE sensor part numbers.
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
- [ ] Finalise FT550 internal 7-bar MAP plumbing.

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
- [ ] Fuse schedule.

### APM

- [ ] Primary fuel-pump circuit.
- [ ] Secondary fuel-pump circuit if used.
- [ ] Cooling-fan circuits.
- [ ] Boost-solenoid supply/control.
- [ ] Auxiliary pump/accessory circuits.
- [ ] Inrush and flyback protection review.

### SIM

- [ ] 5 V reference distribution.
- [ ] Precision sensor-return topology.
- [ ] CKP shield/twist routing.
- [ ] Analogue sensor inputs.
- [ ] Digital switch inputs.
- [ ] Speed input conditioning if required.
- [ ] Communications routing.
- [ ] Connector and service-test-point definition.

## Milestone 6 — Full VRXSE-to-FT550 Master Wiring Matrix

Create a production table containing, for every circuit:

- function;
- Harley component part number;
- Harley connector number;
- Harley connector cavity;
- Harley wire colour;
- OEM ECM pin where relevant;
- sensor/actuator electrical type;
- supply voltage;
- expected signal range;
- FT550 connector and cavity;
- FuelTech wire colour;
- EPM/APM/SIM domain;
- module terminal;
- wire gauge;
- shield/twist requirement;
- fuse value;
- relay/driver details;
- ground point;
- test procedure;
- source/provenance;
- verification status.

No production matrix row may contain an unresolved critical `VERIFY` item.

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
- [ ] Validate all fuse values.
- [ ] Power ECU with actuators disconnected.
- [ ] Validate 5 V reference.
- [ ] Validate every sensor channel.
- [ ] Cycle pumps/fans/solenoids and watch analogue channels for induced noise.
- [ ] Crank with fuel/ignition disabled and validate trigger.
- [ ] Confirm emergency stop / master isolation behaviour.

## Milestone 9 — First Start and NA/Low-Load Validation

- [ ] First start without boost demand.
- [ ] Lock ignition timing.
- [ ] Verify oil pressure immediately.
- [ ] Verify fuel pressure against manifold pressure.
- [ ] Verify coolant and IAT plausibility.
- [ ] Verify lambda.
- [ ] Heat-cycle and inspect harness/connectors.
- [ ] Save first verified FT550 configuration baseline.

## Milestone 10 — Boost Commissioning

- [ ] Wastegate-spring/base-boost testing.
- [ ] Fuel-pressure differential validation under boost.
- [ ] Lambda validation by cylinder where instrumentation permits.
- [ ] IAT/ECT/EGT trend review.
- [ ] Progressive boost-control enablement.
- [ ] Engine-protection thresholds.
- [ ] Data-log review after every stage.

## Final release gate

The harness and configuration may be marked production-ready only when:

1. all critical circuits have primary-source provenance;
2. every FT550 pin assignment is frozen;
3. every sensor calibration is verified;
4. CKP polarity and timing are physically validated;
5. high-current switching does not corrupt sensor readings;
6. protection strategies have been tested;
7. as-built wiring matches the released drawings;
8. the final FT550 configuration is archived with the hardware revision.
