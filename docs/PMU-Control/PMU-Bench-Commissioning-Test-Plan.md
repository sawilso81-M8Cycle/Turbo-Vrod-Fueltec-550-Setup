# PMU Bench Commissioning and Fault-Injection Test Plan

## Objective

Validate the PMU-16 control architecture before installation on the Turbo V-Rod Destroyer. This plan converts the frozen control logic into repeatable bench tests with explicit stimulus, expected behaviour and evidence IDs.

## Bench prerequisites

- ECUMASTER PMU-16 configured with the project output allocation.
- Regulated 12-14.5 V bench supply with current limiting.
- Fused test loads or representative lamps/resistors before real pumps/fans are connected.
- CAN source capable of transmitting the frozen FT550 FTCAN receive frames at 1 Mbps.
- Oscilloscope or logging current clamp where inrush/current timing is required.
- Emergency bench master disconnect.
- No fuel, injectors, coils or boost-control hardware connected during initial logic tests.

## Evidence IDs

Use `BT-xxx` for bench-test evidence. Attach logs/screenshots/waveforms against the matching test ID.

## Test sequence

### BT-001 PMU power-up sanity

Setup: all output loads disconnected or dummy loads fitted.

Stimulus: apply PMU main power and switched power.

Expected:
- PMU boots without fault.
- all outputs remain in their configured safe initial states;
- CAN2 reports configured 1 Mbps state;
- no output activates solely because CAN traffic is absent.

Pass: no unexpected output energisation or reset.

### BT-002 Hardwired master enable priority

Stimulus: toggle A1 MASTER_ENABLE with CAN healthy and then absent.

Expected:
- outputs requiring master enable cannot energise with A1 inactive;
- CAN data alone cannot override MASTER_ENABLE.

Pass: hardwired master input is authoritative.

### BT-003 Kill request priority

Stimulus: command A3 KILL_REQUEST while O1/O6 are active in simulation.

Expected:
- O1 primary pump OFF according to kill rule;
- O6 boost-solenoid supply OFF immediately;
- no CAN value may keep O1/O6 on;
- warning indication may remain active if configured.

Pass: kill input overrides all CAN-derived enable states.

### BT-004 Primary fuel-pump prime

Stimulus: MASTER_ENABLE rising edge, no RPM, no START_REQUEST.

Expected:
- O1 performs the configured prime event only;
- O1 turns OFF at end of prime if engine is not cranking/running.

Record:
- prime duration;
- current profile with representative or real pump in later load test.

Pass: repeatable prime with no unintended latch-on.

### BT-005 Fuel-pump start continuation

Stimulus: MASTER_ENABLE active; assert START_REQUEST.

Expected:
- O1 ON during start request even before valid CAN RPM is present, according to frozen hardwired-safe logic.

Pass: pump runs during commanded crank state.

### BT-006 Fuel-pump run state from CAN RPM

Stimulus: transmit valid FT_RPM > 400 rpm and valid frame timing; release START_REQUEST.

Expected:
- ENGINE_RUNNING true;
- O1 remains ON;
- no chatter across the 400 rpm threshold when RPM is steady.

Pass: stable pump continuation.

### BT-007 RPM/CAN loss while running

Stimulus: with O1 ON and ENGINE_RUNNING true, stop 0x602 traffic or disconnect CAN.

Expected:
- FT_RPM_VALID becomes false after configured timeout;
- O1 follows the documented hardwired-safe grace/fallback logic;
- O1 does not remain latched indefinitely on stale RPM.

Pass: deterministic timeout and shutdown behaviour.

### BT-008 CAN recovery after RPM timeout

Stimulus: restore valid 0x602 traffic after BT-007.

Expected:
- validity returns only after fresh valid frames;
- O1 returns to normal run logic without rapid cycling.

Pass: deterministic recovery.

### BT-009 Fan 1 normal thermostat logic

Stimulus: sweep simulated FT_ECT_C across configured ON and OFF thresholds.

Expected:
- O3 turns ON at high threshold;
- O3 remains ON through hysteresis band;
- O3 turns OFF only below low threshold.

Pass: no relay-like chatter around threshold.

### BT-010 Fan override

Stimulus: assert A4 FAN_OVERRIDE with ECT low and CAN healthy/absent.

Expected:
- O3 ON regardless of ECT validity while master state permits it.

Pass: hardwired override works independently of CAN.

### BT-011 ECT CAN-loss fallback

Stimulus: make FT_ECT invalid by stopping frame 0x600.

Expected:
- O3 enters conservative ON strategy rather than OFF;
- warning state records ECT invalid if configured.

Pass: fan fail-safe is conservative.

### BT-012 Optional Fan 2 strategy

Applicable only if O4 populated.

Stimulus: sweep ECT and simulate Fan 1 state/fault.

Expected: staggered or backup behaviour exactly matches selected strategy.

Pass: no contradictory output state.

### BT-013 Charge-cooler pump run logic

Applicable if O5 populated.

Stimulus: engine-running state valid; then CAN loss; then SERVICE_MODE.

Expected:
- O5 follows engine-running logic;
- CAN loss does not chatter the pump;
- service mode permits bleed/test operation as designed.

Pass: stable intended operation.

### BT-014 Boost-solenoid healthy enable

Stimulus: MASTER_ENABLE true, KILL false, valid RPM/MAP/CAN health.

Expected: O6 may energise only when all required validity conditions are true.

Pass: no O6 enable from stale/invalid MAP or RPM.

### BT-015 Boost-solenoid CAN-loss safe state

Stimulus: while O6 ON, remove CAN or invalidate MAP.

Expected:
- O6 OFF;
- hardware returns to minimum mechanical boost strategy;
- no automatic re-enable until valid conditions are restored.

Pass: fail-safe de-energise proven.

### BT-016 Warning lamp aggregation

Stimulus one at a time:
- CAN unhealthy;
- ECT invalid;
- fuel pressure invalid;
- oil pressure invalid;
- PMU output fault.

Expected:
- O8 warning output asserts according to aggregation rules;
- clearing one cause does not extinguish warning while another cause remains.

Pass: warning aggregation deterministic.

### BT-017 Service/logger output

Stimulus: toggle MASTER_ENABLE and SERVICE_MODE.

Expected: O10 follows frozen service/logger logic and is unaffected by CAN validity.

Pass: output state matches matrix.

### BT-018 Output overcurrent trip

Use a current-limited test load before real hardware.

Stimulus: increase current above provisional output threshold.

Expected:
- target PMU output trips/protects according to configured strategy;
- fault state is visible/logged;
- unrelated outputs remain operating unless intentionally grouped.

Pass: fault containment works.

### BT-019 Output retry behaviour

Applicable where retry is enabled.

Stimulus: create transient overcurrent then remove it.

Expected:
- retry timing/count matches project setting;
- critical outputs do not enter uncontrolled rapid retry loops.

Pass: deterministic retry or latched-off behaviour.

### BT-020 PMU reset/brownout recovery

Stimulus: controlled supply dip within safe bench limits.

Expected:
- no unsafe output pulse during reset;
- outputs return through normal state logic after reboot;
- O6 remains fail-safe until CAN validity is restored.

Pass: reset recovery safe.

### BT-021 CAN bus open-circuit

Stimulus: physically open CAN H or CAN L at X51.

Expected:
- validity timers expire;
- CAN-dependent outputs enter documented fallback;
- PMU remains electrically stable.

Pass: same safety intent as complete CAN disconnect.

### BT-022 CAN termination fault

Stimulus: remove one termination on the bench network.

Expected:
- communication degradation/failure is detected through validity logic;
- no control output treats intermittent stale data as healthy.

Pass: validity design contains the fault.

### BT-023 Out-of-range CAN values

Stimulus: send valid frames containing deliberately implausible RPM/TPS/MAP/ECT/pressure values.

Expected:
- corresponding `*_VALID` becomes false due to plausibility checks;
- dependent functions enter fallback.

Pass: numerical plausibility checks proven.

### BT-024 Wrong source arbitration ID

Stimulus: send correctly formatted 0x600-0x602 content from a non-approved arbitration/source ID.

Expected:
- production filter ignores the frames;
- no dependent validity flag is asserted.

Pass: source filtering works.

### BT-025 Full kill + CAN fault combined

Stimulus: run simulated engine state, then simultaneously assert KILL_REQUEST and remove CAN.

Expected:
- kill path wins immediately;
- O1 and O6 OFF;
- no race condition or delayed stale-state continuation.

Pass: combined-fault priority proven.

## Load-current commissioning stage

After logic tests pass, replace dummy loads one at a time with real hardware and close the relevant HC evidence IDs:

- HC-001 primary fuel pump;
- HC-002 secondary fuel pump if fitted;
- HC-003 radiator fan 1;
- HC-004 radiator fan 2 if fitted;
- HC-005 charge-cooler pump if fitted;
- HC-006 boost solenoid;
- HC-007 logger/service load.

Record steady current, inrush, inrush duration, PMU current limit, retry policy, route length and final conductor size.

## Release rule

No PMU-controlled high-current load may move to vehicle installation until:

1. its logic tests pass;
2. its actual current/inrush evidence is recorded;
3. output protection is set from measured data;
4. conductor/terminal ratings are frozen;
5. CAN-loss behaviour is proven where CAN affects the output.
