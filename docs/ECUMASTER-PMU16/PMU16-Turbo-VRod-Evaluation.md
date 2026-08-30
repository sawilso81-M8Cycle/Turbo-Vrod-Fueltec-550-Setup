# ECUMASTER PMU-16 Evaluation for Turbo V-Rod + FuelTech FT550

## Status

**Candidate architecture component - not yet design-frozen.**

## Why it is attractive

The PMU-16 can replace a large portion of conventional relay/fuse hardware in the Auxiliary Power Module while adding:

- per-output current sensing;
- programmable electronic protection;
- retry/self-reset behaviour;
- logic-based output control;
- CAN-based command/status exchange;
- logging and diagnostics;
- reduced relay/fuse/socket count.

For a turbo motorcycle this is valuable because fuel pumps, cooling fans, intercooler pumps and other auxiliary loads can be supervised rather than simply switched.

## Proposed role

### Keep outside PMU initially

- precision 5 V sensor references;
- sensor returns;
- CKP / trigger signal conditioning;
- high-impedance analogue measurements;
- any circuitry whose failure could corrupt sensor reference integrity.

These remain in SIM.

### Candidate PMU-16 loads

1. Fuel pump 1
2. Fuel pump 2 / staged pump
3. Radiator fan 1
4. Radiator fan 2 if required
5. Intercooler / charge-cooler pump
6. Water/methanol pump if fitted
7. Boost-control solenoid supply
8. Auxiliary coolant pump
9. Warning / fault lamp
10. Race auxiliary supply
11. Spare controlled output
12. Spare controlled output

Final output allocation depends on measured steady-state and inrush currents and the exact PMU output rating/terminal restrictions.

## EPM question

The PMU could potentially supply FT550, injectors and ignition coils, but this should not be assumed to be better simply because the hardware permits it.

Before migrating engine-critical loads from a dedicated EPM, analyse:

- common-mode failure consequences;
- PMU restart behaviour;
- loss-of-CAN behaviour;
- over-current trip/retry behaviour;
- ignition-coil transient current;
- injector current profile;
- voltage drop during cranking;
- emergency-stop behaviour;
- whether one PMU fault can remove all engine power simultaneously.

A split architecture may remain preferable:

- EPM = FT550 + ignition/injection critical circuits;
- PMU-16/APM = pumps, cooling and auxiliary loads;
- SIM = precision measurements.

## FT550 interaction

Preferred control philosophy:

- hardwired critical enable paths where loss of CAN must not create an unsafe state;
- CAN for status, diagnostics and non-critical command exchange where supported;
- explicit default states on loss of CAN;
- PMU current/fault information logged alongside FT550 engine data.

## Protection philosophy

Every PMU output should have a documented:

- load name;
- wire gauge;
- connector/terminal;
- expected steady current;
- expected inrush current;
- soft current limit if used;
- hard trip threshold;
- retry timing;
- maximum retry count where applicable;
- fault action;
- FT550 response if the load fails;
- bench-test method.

## Recommended next engineering task

Create a `PMU16-Output-Allocation.csv` or Markdown master table and populate it only from actual component current data and the current PMU-16 manual. Then bench-test each high-current load through the PMU while watching FT550 sensor channels for electrical interference.
