# First Power Authorisation & Dead-Engine Commissioning Pack

## Purpose

Define the controlled commissioning sequence after `HP7_FINAL_HARNESS_ACCEPTED` and before any engine start attempt.

The objective is to prove that power distribution, grounds, references, CAN, sensors, PMU outputs and control logic behave correctly while the engine is deliberately prevented from starting.

## Entry conditions

Do not begin unless:

- `HP7_FINAL_HARNESS_ACCEPTED` is complete;
- harness serial and as-built revision are recorded;
- battery/power source is suitable and protected;
- released fuse/protection hardware is installed;
- FT550 and PMU configurations are identified by revision/hash/export where practical;
- fuel and ignition can be positively inhibited;
- emergency power isolation is immediately accessible;
- no unresolved HP-7 electrical nonconformance remains.

## Dead-engine state

For tests involving cranking, prevent combustion by a controlled method that removes both fuel delivery and ignition energy as required while retaining the signals needed for the specific test.

Do not rely on throttle position or an assumed ECU mode as the sole no-start control.

Record the exact inhibition method before cranking.

## Stage FP-0 – Unpowered installation inspection

Before connecting the battery:

- verify harness routing and clamps;
- inspect turbo/exhaust heat clearances;
- inspect steering full-left/full-right movement;
- inspect rear/suspension movement areas;
- verify connector locks;
- verify J-P01/J-P02 mechanical security;
- verify B15 protection hardware;
- verify Pump 1/2 high-current connections;
- verify X70 installation;
- confirm no loose conductive hardware/tools remain.

Output: `FP0_INSTALLATION_ACCEPTED`

## Stage FP-1 – Unpowered resistance/isolation sanity check

With sensitive modules disconnected where required by the released test method:

- check no hard short exists between B+ and power ground;
- verify FT550 A21 dry-contact side is isolated from +12 V;
- verify CAN-H/CAN-L are not shorted to B+ or ground;
- verify sensor 5 V/reference circuits are not shorted to B+;
- verify sensor ground is not accidentally merged into an uncontrolled high-current return;
- verify expected ground continuity to designated ground points.

Do not use insulation-test voltages that could damage electronics.

Output: `FP1_UNPOWERED_SANITY_ACCEPTED`

## Stage FP-2 – Current-limited first energisation

Where practical use a controlled/current-limited first-power method appropriate to the system before unrestricted battery operation.

Initial state:

- engine not cranking;
- pumps disabled unless specifically commanded for test;
- ignition outputs disabled;
- auxiliary outputs disabled;
- Two-Step inactive.

Observe:

- unexpected current draw;
- smoke/odour/heating;
- PMU/FT550 boot behaviour;
- fuse/protection trips;
- unexpected relay or pump operation.

Any abnormal condition = immediate power removal and HOLD.

Output: `FP2_FIRST_ENERGISATION_ACCEPTED`

## Stage FP-3 – Power rail verification

Record under key-on conditions:

- battery/source voltage;
- voltage at J-P01;
- voltage at PMU B15 input;
- voltage at FT550 supply;
- B39 injector supply when commanded/enabled as intended;
- B40 SparkPRO supply when commanded/enabled as intended;
- voltage drop B+ to PMU;
- primary ground voltage drop where testable without engine operation.

Compare against released design expectations and device operating ranges.

Output: `FP3_POWER_RAILS_ACCEPTED`

## Stage FP-4 – 5 V reference and sensor-ground verification

Before connecting questionable/unverified sensors, establish the reference rails safely.

Verify:

- 5 V reference magnitude;
- stability over key-on period;
- sensor-ground offset to ECU reference;
- no unexpected continuity/current path into high-current ground;
- no sensor supply driven from 12 V.

Then connect/verify sensors in a controlled sequence where practical.

Output: `FP4_REFERENCE_RAILS_ACCEPTED`

## Stage FP-5 – Sensor plausibility

With engine stationary verify plausible readings for applicable sensors:

- TPS closed position and smooth movement;
- MAP near ambient/barometric expectation with engine off;
- IAT near ambient;
- engine temperature plausible for current engine state;
- VSS zero when stationary;
- other analogue/digital sensors plausible;
- no sensor pegged at rail without explanation.

Do not calibrate away a wiring fault.

Output: `FP5_SENSOR_PLAUSIBILITY_ACCEPTED`

## Stage FP-6 – CAN verification

Verify:

- FT550 and PMU communication where configured;
- CAN-H/CAN-L polarity;
- expected bus activity;
- no excessive error counters/bus-off state;
- X51 service access works;
- no hidden/unexpected termination;
- bus resistance/termination result matches the released topology when measured under the correct unpowered test conditions.

Output: `FP6_CAN_ACCEPTED`

## Stage FP-7 – PMU output dry-function test

Test outputs one at a time where safe and appropriate.

Verify command and feedback/current behaviour for applicable branches:

- Pump 1 control;
- Pump 2 control;
- B11 radiator fan;
- B12 charge-cooler pump if fitted;
- B39 injector supply enable architecture;
- B40 ignition supply enable architecture;
- X70 relay coil.

For fuel pumps, use only the minimum duration necessary for electrical verification unless the fuel system is fully commissioned for longer operation.

Output: `FP7_PMU_OUTPUTS_ACCEPTED`

## Stage FP-8 – X70 Two-Step truth-table test

With engine unable to start, verify the complete control chain:

- clutch/input state as applicable;
- PMU O11 command;
- X70 relay energisation;
- dry-contact transition;
- FT550 A21 input state;
- release transition;
- fail state with relay de-energised.

Confirm again that the A21 contact side is never exposed to +12 V.

Output: `FP8_TWO_STEP_ACCEPTED`

## Stage FP-9 – Dead-engine crank signal test

Only after FP-0 through FP-8 PASS.

Positive no-start controls must be active.

During short controlled cranking capture:

- battery minimum voltage;
- PMU minimum input voltage;
- FT550 reset/no-reset behaviour;
- RPM signal;
- CKP/CAM synchronisation status where available;
- trigger errors;
- CAN stability;
- unexpected PMU trips;
- B15 voltage drop;
- sensor plausibility while cranking.

No fuel injection or ignition energy shall be intentionally enabled for this test.

Output: `FP9_DEAD_ENGINE_CRANK_ACCEPTED`

## Stage FP-10 – Post-test thermal/physical inspection

After electrical and crank tests inspect:

- B15 terminals/junctions;
- J-P01/J-P02;
- pump connectors/high-current paths;
- B39/B40 connections;
- PMU connector;
- fuse/protection devices;
- grounds;
- any branch showing measurable voltage drop or unexpected current.

Record temperature or qualitative evidence consistently.

Output: `FP10_POST_TEST_ACCEPTED`

## First-power release

When FP-0 through FP-10 PASS and all commissioning evidence is reviewed:

`FIRST_POWER_COMMISSIONING_ACCEPTED`

This means the installed electrical system has passed dead-engine commissioning.

It does not automatically mean:

`FIRST_START_AUTHORISED`

## Stop conditions

Immediately stop and isolate power for:

- smoke, burning odour or visible insulation distress;
- unexpected conductor/terminal heating;
- uncontrolled pump/fan/ignition operation;
- repeated PMU/ECU resets;
- unexpected +12 V on reference/sensor/A21 circuits;
- abnormal B15 voltage drop;
- CAN bus-off or severe unexplained errors;
- implausible sensor readings indicating probable wiring error;
- unexpected cranking fuel or spark activity;
- any protection device operating without understood cause.

## Evidence

Use `First-Power-Dead-Engine-Commissioning-Register.csv` and retain screenshots/logs/photos against the harness serial and configuration revisions.

## Next gate

After `FIRST_POWER_COMMISSIONING_ACCEPTED`, proceed to the separate First Start Authorisation & Initial Engine Run Pack.
