# B15 / B39 / B40 Protection & Load Coordination Pack

## Purpose

Convert accepted measured load evidence into the final protection and conductor decisions for the three engine-critical power paths:

- **B15** – primary PMU16 supply;
- **B39** – injector power supply;
- **B40** – SparkPRO / ignition power supply.

This pack closes a major portion of HP-3 Electrical Blocker Closure and prevents protection values being chosen from nominal guesses.

## Locked starting architecture

### B15

- function: battery / J-P01 to PMU16 primary supply;
- conductor baseline: **10 mm²**;
- final protection: measurement/load-model gated;
- junction hardware: production PN/ratings must be frozen before manufacture.

### B39

- function: engine-critical injector supply;
- baseline conductor: **1.0 mm²**, subject to final verified injector architecture/current and terminal capability;
- independent protection required;
- must not be casually combined with B40.

### B40

- function: SparkPRO / ignition supply;
- baseline conductor: **1.5 mm²**, subject to measured ignition current, dwell strategy, terminal capability and thermal evidence;
- independent protection required;
- must not be casually combined with B39.

## Coordination philosophy

Protection must satisfy all of the following rather than only the load's nominal running current:

1. carry expected continuous load with adequate margin;
2. tolerate legitimate transient/inrush current without nuisance operation;
3. protect the conductor and connector/terminal path;
4. remain within PMU output/channel limitations where electronically protected;
5. coordinate upstream and downstream protection so a branch fault does not unnecessarily remove unrelated engine-critical functions;
6. account for temperature, bundling and installation environment;
7. use measured installed load evidence where available.

A larger fuse/current limit is not an acceptable cure for nuisance trips unless the entire downstream path is proven suitable.

## B15 simultaneous-load model

B15 must be evaluated using a realistic worst credible simultaneous operating state, not the sum of every theoretical transient peak occurring at once.

Model at minimum:

- FT550 supply load if sourced through the relevant distribution path;
- PMU16 self-consumption;
- B39 injector load;
- B40 ignition/SparkPRO load;
- Pump 1 load if PMU driven;
- Pump 2 load if PMU driven;
- radiator fan B11 if PMU driven;
- charge-cooler pump B12 if fitted/PMU driven;
- other engine-critical PMU outputs included in the released architecture.

Create at least these cases:

- **LC-01 Key On / Engine Off**;
- **LC-02 Cranking**;
- **LC-03 Idle / Low Load**;
- **LC-04 High RPM / High Fuel Demand**;
- **LC-05 High RPM + Both Pumps + Cooling**;
- **LC-06 Hot Restart**;
- **LC-07 Credible Worst Continuous**.

Do not simply add unrelated one-time inrush peaks unless the control logic permits them to coincide.

## B15 acceptance checks

Freeze B15 only when:

- continuous and transient load model is populated;
- 10 mm² conductor remains compatible with chosen terminals/junctions;
- voltage-drop estimate/measurement is acceptable;
- upstream protective device rating/type is selected;
- protective device interrupting/current capability is suitable for the application;
- J-P01 hardware rating exceeds the released requirement;
- cable routing/temperature environment is accepted;
- cranking and hot-operation evidence does not reveal abnormal heating or reset behaviour.

## B39 injector branch checks

Use the accepted injector decision and electrical evidence to establish:

- number of injectors on branch;
- injector type/driver architecture;
- expected average and peak supply behaviour;
- wire length;
- terminal current capability;
- selected conductor;
- protection/current-limit value;
- fault behaviour.

If a peak-and-hold stage is introduced, B39 must be re-evaluated around the actual stage architecture rather than the earlier direct-drive baseline.

## B40 ignition branch checks

Use accepted SparkPRO/coil testing to establish:

- SparkPRO supply current;
- coil/dwell operating envelope;
- high-RPM current behaviour;
- hot current behaviour;
- conductor/terminal capability;
- protection/current-limit value;
- voltage drop;
- thermal result.

Do not release B40 solely from coil DC resistance.

## Selective protection requirement

A fault on B39 should, where architecture permits, remove injector power without unnecessarily removing unrelated auxiliary systems.

A fault on B40 should, where architecture permits, remove ignition power without collapsing unrelated auxiliary power.

B15 is upstream and must protect the primary PMU feed while allowing properly selected downstream electronic/fused protection to clear branch faults first where practical.

## Voltage-drop review

For each path record:

- source voltage;
- load current;
- conductor length;
- conductor cross-section;
- measured or calculated drop;
- connector/junction contribution where measurable;
- load-end voltage.

Use measured installed voltage drop during prototype qualification to validate the design calculation.

## Thermal review

Protection/conductor acceptance includes the complete path:

- wire;
- crimp;
- terminal;
- housing;
- splice/junction;
- fuse/relay/PMU terminal;
- local ambient/heat exposure.

The smallest-capability element in the path can become the real limit.

## Release decisions

B15:

`B15_PROTECTION_FROZEN`

B39:

`B39_PROTECTION_FROZEN`

B40:

`B40_PROTECTION_FROZEN`

When all three are accepted and the other HP-3 electrical blockers are closed:

`HP3_ELECTRICAL_BLOCKERS_CLOSED`

## Stop conditions

Do not freeze a branch if:

- measured load data is missing where required;
- terminal current capability is unverified;
- proposed protection exceeds the proven downstream path capability;
- unexplained voltage drop exists;
- abnormal heating exists;
- PMU/channel behaviour is outside verified capability;
- an electrical architecture decision is still open.

## Current release state

`B15_B39_B40_COORDINATION_PACK_RELEASED / FINAL_VALUES_EVIDENCE_GATED`
