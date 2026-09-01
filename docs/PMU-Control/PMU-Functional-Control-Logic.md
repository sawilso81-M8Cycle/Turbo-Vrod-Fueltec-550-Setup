# ECUMASTER PMU-16 Functional Control Logic

## Objective

Define the first production control strategy for PMU-16 outputs using hardwired command inputs plus the validated FT550 CAN variables already defined in the repository.

## Safety precedence

For every control function use the following authority order:

1. Hardwired kill / master safety input.
2. PMU-local input or measured state.
3. Valid FT550 CAN signal.
4. Fallback state.

CAN is never the sole authority for master enable, kill or starter safety.

## Core hardwired PMU inputs

- A1 / pin 29 = MASTER_ENABLE
- A2 / pin 16 = START_REQUEST
- A3 / pin 30 = KILL_REQUEST
- A4 / pin 17 = FAN_OVERRIDE
- A5 / pin 31 = SERVICE_MODE

Input polarity remains installation-verified before final software release.

## Derived master states

### SYSTEM_ARMED

`SYSTEM_ARMED = MASTER_ENABLE && !KILL_REQUEST`

### ENGINE_RUNNING

Initial CAN-assisted state:

`ENGINE_RUNNING = FT_RPM_VALID && FT_RPM > 400`

### ENGINE_CRANKING

`ENGINE_CRANKING = START_REQUEST || (FT_RPM_VALID && FT_RPM > 0 && FT_RPM <= 400)`

### CAN_FT550_HEALTHY

TRUE only when the currently required CAN channels are valid. Optional channels shall not make the whole bus unhealthy when their related feature is disabled.

## O1 Primary fuel pump

### Objective

Provide controlled prime, cranking support and engine-running continuation without relying exclusively on CAN.

### Initial logic

- OFF whenever SYSTEM_ARMED is FALSE.
- ON for configurable `FUEL_PRIME_TIME` after SYSTEM_ARMED transitions FALSE -> TRUE.
- ON while START_REQUEST is TRUE.
- ON while ENGINE_RUNNING is TRUE.
- If CAN RPM becomes invalid after the engine has been confirmed running, retain pump only for a short configurable grace period before falling back to the hardwired-safe strategy.
- KILL_REQUEST removes O1 immediately regardless of CAN state.

### Initial parameters

- FUEL_PRIME_TIME = 3.0 s starting value.
- CAN_RPM_LOSS_GRACE = 1.0 s starting value.

These are commissioning parameters, not final calibrated values.

## O2 Secondary / staged fuel pump

Default state: DNP unless the final fuel system requires it.

If populated, initial strategy:

`O2 = SYSTEM_ARMED && ENGINE_RUNNING && FT_MAP_VALID && FT_MAP_BAR > SECONDARY_PUMP_MAP_ON`

Add hysteresis and minimum-on time before production use.

CAN failure fallback: O2 OFF unless the final fuel-pressure validation proves an alternate safer strategy.

Do not use O2 logic to compensate for an undersized primary fuel system.

## O3 Radiator fan 1

### Normal strategy

- FAN_OVERRIDE forces O3 ON when SYSTEM_ARMED is TRUE.
- With valid ECT, use thermostatic hysteresis.
- With invalid/stale ECT while SYSTEM_ARMED is TRUE, command conservative fan ON after a short validation delay rather than leaving the fan OFF.

Initial calibration placeholders:

- FAN1_ON_C = 95 C
- FAN1_OFF_C = 90 C

These values are placeholders until the cooling strategy is validated for the installed V-Rod/turbo configuration.

## O4 Radiator fan 2

If fitted, stagger fan 2 above fan 1 to reduce simultaneous inrush.

Initial placeholders:

- FAN2_ON_C = 100 C
- FAN2_OFF_C = 94 C
- START_STAGGER = 0.5 s minimum after fan 1 command

CAN ECT invalid fallback: fan 2 may also be commanded ON under the conservative thermal strategy if engine operation continues.

## O5 Charge-cooler / intercooler pump

If fitted:

- ON whenever SYSTEM_ARMED && ENGINE_RUNNING.
- Optionally continue for a timed post-run period after ENGINE_RUNNING becomes FALSE if thermal testing shows benefit.
- SERVICE_MODE may command the pump for bleeding/testing with engine off.

Initial post-run placeholder: 30 s.

## O6 Boost-control solenoid supply

PMU provides protected power only. FT550 remains the boost-control authority unless the final system deliberately changes that architecture.

Initial rule:

`O6 = SYSTEM_ARMED && ENGINE_RUNNING && CAN_FT550_HEALTHY`

If FT_MAP_VALID becomes FALSE or CAN health fails, O6 goes OFF so the pneumatic/mechanical system returns to its defined minimum-boost state.

The wastegate plumbing must therefore be inherently safe with O6 unpowered.

## O8 Warning output

O8 drives the project warning lamp / warning request.

Initial warning causes:

- CAN critical signal invalid while engine running.
- Fuel pressure invalid or protection threshold exceeded once those limits are commissioned.
- Oil pressure invalid or protection threshold exceeded once those limits are commissioned.
- PMU output overcurrent/fault on required engine-support loads.
- Thermal fallback active because ECT is invalid.
- Optional ECU warning state once a verified FTCAN status definition exists.

Warning logic must distinguish `SENSOR_UNKNOWN` from `SENSOR_LOW`. Unknown is not healthy.

## O10 Logger / service feed

Initial rule:

- ON when SYSTEM_ARMED.
- ON in SERVICE_MODE even with engine stopped.
- Optional delayed power-off for log flush after MASTER_ENABLE is removed, if the connected logger requires it.

## Kill behaviour

KILL_REQUEST has highest priority among normal software commands.

Minimum required immediate actions:

- O1 primary fuel pump OFF.
- O2 secondary fuel pump OFF.
- O6 boost solenoid supply OFF.
- Engine-support outputs that can continue safely after kill, such as fans, may remain active only if the final strategy explicitly permits it.

KILL_REQUEST must not depend on FTCAN reception.

## CAN-loss fallback matrix

| Function | CAN dependency | Loss response |
|---|---|---|
| Primary fuel pump | RPM assists run confirmation | use hardwired start/master strategy; terminate CAN-only continuation after grace period |
| Secondary fuel pump | MAP/RPM | OFF |
| Fan 1 | ECT | conservative ON strategy |
| Fan 2 | ECT | conservative thermal strategy if fitted |
| Charge-cooler pump | RPM | project-defined conservative continuation; do not oscillate on stale RPM |
| Boost solenoid supply | CAN health/MAP | OFF -> minimum mechanical boost |
| Warning lamp | CAN health | ON / fault indication |
| Logger feed | none required | remain controlled by master/service logic |

## Output fault handling

Every populated PMU output shall have:

- measured steady-state current;
- measured inrush where applicable;
- configured current limit;
- retry policy;
- latched/non-latched fault decision;
- logged fault state.

Safety-critical loads shall not use unlimited automatic retry. Fuel-pump and fan retry strategy must be validated on the real hardware.

## Implementation sequence in PMU Client

1. Create hardwired input variables A1-A5 with verified polarity.
2. Import FT550 receive variables and validity states.
3. Create SYSTEM_ARMED, ENGINE_RUNNING, ENGINE_CRANKING and CAN_FT550_HEALTHY.
4. Implement O1 prime/start/run logic.
5. Implement O3/O4 fan hysteresis and invalid-ECT fallback.
6. Implement O5/O6 only if fitted.
7. Implement O8 warning aggregation.
8. Implement O10 service/logger logic.
9. Add output current limits only after hardware evidence closes HC-001 to HC-007.
10. Execute fault-injection tests: CAN unplug, ECT frame stale, RPM frame stale, kill asserted, PMU output overload simulation where safe.

## Release state

Control architecture: **FROZEN REV 0.1**.

Calibration thresholds/current limits: **TEST GATED**.

PMU Client project file: **TO BE IMPLEMENTED FROM THIS SPEC**.
