# B15 Main PMU Feed + Primary Power Distribution Freeze – Rev 1

## Purpose

Freeze the architecture for battery-to-PMU power, master protection, primary positive distribution and high-current ground return so the harness manufacturer has one authoritative power backbone.

## Verified PMU16 constraints

ECUMASTER documents the standard PMU-16 / PMU-16 DL with:

- one M6 battery stud;
- 10 × 25 A continuous outputs;
- 6 × 15 A continuous outputs;
- 150 A total continuous output capability;
- internal current sensing and electronic overcurrent/thermal protection on outputs.

The PMU main battery feed therefore uses the M6 stud and shall not be routed through the 39-way output connector.

## B15 cable baseline

B15 remains:

- function: battery / protected positive distribution → PMU M6 battery stud;
- nominal routed length: ~400 mm;
- prototype first-cut length: ~500 mm;
- conductor baseline: **10.0 mm²**;
- termination: crimped ring / stud terminal correctly matched to 10 mm² cable and M6 stud hardware;
- protection: dedicated upstream master short-circuit protection located as close to the source/junction as practical.

The 10 mm² cable is now the Rev 1 production baseline for B15. It may only be upsized if the final aggregate-load, route, thermal or voltage-drop calculation requires it. Downsizing requires formal engineering revision.

## Positive power architecture

Preferred architecture:

`Battery + → master isolation / battery isolator as applicable → primary protection → J-P01 insulated positive junction → B15 10 mm² → PMU M6 stud`

J-P01 may also supply approved external high-current stages such as a fuel-pump relay/SSR if direct PMU drive is not accepted. These external branches require their own coordinated protection.

No unfused or unprotected auxiliary branch is to be hidden downstream of J-P01.

## Master protection philosophy

The B15 upstream protection device is for catastrophic short-circuit / cable protection. It is not a substitute for the PMU's per-output electronic protection.

Final master protection value must be selected from:

1. maximum credible simultaneous PMU load;
2. normal continuous operating current;
3. short-duration inrush / cranking-related electrical states that actually pass through B15;
4. 10 mm² cable ampacity under the selected wire series, bundle and ambient conditions;
5. ring terminal, junction and isolator ratings;
6. time-current behaviour of the selected fuse/breaker.

Do not select the master fuse simply by adding every output's headline maximum rating. Use a realistic simultaneous-load model.

## Simultaneous-load model

The manufacturer/commissioning team shall complete the aggregate load register for at least these states:

- Key-on / engine off;
- Cranking;
- Idle cold;
- Idle hot with radiator fan running;
- Normal cruise / road load;
- High-load / boost;
- Launch / Two-Step active;
- Maximum credible race operating state with fuel pump(s), fan, charge-cooler pump, injectors, ignition, boost solenoid and service loads as fitted.

Record measured PMU total current where possible and compare against calculated estimates.

## External fuel-pump power stage relationship

If pump testing ultimately requires an external high-current relay/SSR, the heavy pump load may be supplied from J-P01 rather than through a PMU high-current output. In that case:

- PMU O1/O2 remains control only;
- external pump feed receives its own branch protection;
- 4.0 mm² pump feed and 4.0 mm² dedicated return remain frozen;
- external pump current is not counted as PMU output current, but it is still part of total battery/system load planning.

## J-P01 positive junction

J-P01 shall be:

- insulated / covered;
- mechanically fixed;
- sized for B15 and all approved external power-stage branches;
- protected against accidental tool contact;
- accessible for service without disturbing signal harnesses;
- located away from turbo/exhaust heat and fuel leakage risk;
- labelled `J-P01 PRIMARY +12V DISTRIBUTION`.

Exact hardware PN remains DFM/procurement gated pending physical packaging.

## Ground architecture

High-current returns shall converge through the controlled power-ground architecture, not through sensor/reference grounds.

Preferred high-current path:

`Load dedicated return / engine return → J-P02 power ground star → battery negative / approved engine-battery ground path`

Rules:

- fuel-pump 4.0 mm² dedicated returns stay high-current;
- fan/pump returns use conductor size matched to final load calculation;
- SparkPRO power grounds remain low-impedance and return to the approved ignition/power ground point;
- PMU electronics ground pin remains a module reference/ground path and is not used as a substitute for heavy load returns;
- FT550 sensor grounds and 5 V references remain segregated from pump/fan/coil high-current returns;
- engine block, battery negative and chassis bonding must be validated for low resistance under cranking and high-load operation.

## Ground straps / engine bonding

Before first power and cranking, verify:

- battery negative to engine bond;
- engine to chassis bond if chassis is used as a return path;
- PMU/J-P02 power-ground connection;
- no unintended current is forced through throttle/sensor/CAN shields or small signal grounds.

Voltage drop shall be measured during cranking and high-current operation, not inferred only from static resistance.

## B15 acceptance criteria

B15 may become `PRODUCTION_FROZEN` when:

- final installed route is known;
- 10 mm² cable and insulation series are selected;
- ring terminal PN and crimp tooling are frozen;
- J-P01 hardware is frozen;
- master protection device PN/rating is frozen from aggregate-load calculation;
- aggregate PMU current is measured/validated;
- B15 voltage drop is acceptable under maximum credible PMU load;
- terminal/junction temperature remains acceptable;
- battery/engine/J-P02 ground voltage drop is accepted.

## Release state

**PRIMARY_POWER_ARCHITECTURE_FROZEN**

**B15_10MM2_CABLE_BASELINE_FROZEN**

**MASTER_PROTECTION_VALUE_AND_JUNCTION_HARDWARE_LOAD_GATED**
