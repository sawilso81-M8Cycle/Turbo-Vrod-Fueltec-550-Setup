# FT550 -> PMU-16 CAN Signal Dictionary

## Purpose

Define the minimum CAN data set the ECUMASTER PMU-16 is allowed to consume from the FuelTech FT550, together with timeout and fallback behaviour. This document intentionally freezes signal intent and safety behaviour before freezing FuelTech CAN frame IDs/scaling.

## Bus baseline

- Physical bus: FT550 CAN A <-> PMU-16 CAN2.
- Bitrate: 1 Mbps.
- Topology: linear trunk with FT550 and PMU at physical ends.
- Service tap: X51, short stub only, no permanent termination.
- FT550 physical pins: A16 CAN HIGH, A15 CAN LOW.
- PMU physical pins: pin 24 CAN2 HIGH, pin 37 CAN2 LOW.

## Design rule

The PMU shall not depend on CAN for any function that must remain available during a CAN fault unless a hardwired fallback exists.

CAN data may influence auxiliary power logic, staged-load logic, cooling strategy, warnings and logging. A single stale or invalid FT550 frame must never cause uncontrolled fuel-pump, fan or engine-power behaviour.

## Core signal dictionary

| Signal_ID | Signal | Source | PMU use | Priority | Timeout | Timeout fallback | Frame/status |
|---|---|---|---|---|---|---|---|
| CAN-001 | Engine RPM | FT550 | Engine-running state; pump/fan logic; logging | CRITICAL | 250 ms provisional | Treat RPM as invalid/zero; preserve only hardwired-safe pump logic | Frame ID/scaling VERIFY |
| CAN-002 | TPS / throttle position | FT550 | Staged auxiliary logic; logging | HIGH | 250 ms provisional | Ignore TPS-dependent enhancements; no shutdown action | Frame ID/scaling VERIFY |
| CAN-003 | Coolant temperature | FT550 | Fan control request / thermal escalation | CRITICAL | 1000 ms provisional | Enter conservative fan strategy, not fan-off | Frame ID/scaling VERIFY |
| CAN-004 | Fuel pressure | FT550 | Fuel-system warning/derate request support; logging | CRITICAL | 250 ms provisional | Mark invalid; do not infer healthy pressure | Frame ID/scaling VERIFY |
| CAN-005 | Engine oil pressure | FT550 | Warning/protection support; logging | CRITICAL | 250 ms provisional | Mark invalid; do not infer healthy pressure | Frame ID/scaling VERIFY |
| CAN-006 | MAP / boost | FT550 | Boost-dependent auxiliary/staging logic; logging | HIGH | 250 ms provisional | Disable boost-dependent auxiliary enhancements | Frame ID/scaling VERIFY |
| CAN-007 | Battery voltage | FT550 | PMU diagnostics and load-shed context | MEDIUM | 1000 ms provisional | Use PMU-local supply measurement where available | Frame ID/scaling VERIFY |
| CAN-008 | Engine-running derived state | PMU derived from RPM + validity | Fuel-pump continuation and state logic | CRITICAL | inherits RPM | FALSE/UNKNOWN on RPM timeout | Derived, no direct frame required |
| CAN-009 | ECU fault / warning state | FT550 if available | Warning lamp/logging only initially | MEDIUM | 1000 ms provisional | Mark ECU status unknown | Availability VERIFY |
| CAN-010 | Gear position | FT550 if configured | Gear-based staged auxiliaries/logging | LOW | 1000 ms provisional | Ignore gear-based enhancements | Availability/frame VERIFY |

## PMU logic rules

### Primary fuel pump O1

Primary fuel-pump operation must not rely solely on a continuously valid CAN RPM message. Use a hardwired master-enable/start-request path as the primary authority, with CAN RPM only as an engine-running confirmation where practical.

CAN loss shall not instantly kill the primary pump while the engine is running. The final PMU logic must use a validated timeout and hardwired-state combination to avoid both false shutdown and indefinite pumping after engine stop.

### Secondary fuel pump O2

Secondary/staged pump logic may use RPM, TPS, MAP/boost and fuel-pressure context. On CAN timeout, staged operation shall fall back to a conservative safe state selected during commissioning. Default design preference is OFF unless disabling it would create a fuel-supply hazard at the current operating state; this must be proven on the bike/dyno.

### Cooling fans O3/O4

Coolant-temperature CAN timeout must fail toward cooling, not away from it. If coolant temperature becomes stale while ignition/master enable is active, the PMU should command a conservative fan strategy after a defined grace period.

### Charge-cooler pump O5

If fitted, the default after CAN loss while engine-running/master-enable remains credible should be ON or another conservative thermal state, subject to measured electrical capacity.

### Boost-control supply O6

CAN loss shall not create additional boost. The boost-control electrical supply and pneumatic strategy must fail toward minimum mechanical boost.

### Warning output O8

CAN timeout or invalid critical channels may illuminate the PMU warning output, with logic that distinguishes communications failure from confirmed low fuel/oil pressure.

## Signal validity

Each imported FT550 channel shall have:

1. raw frame reception validity;
2. timeout timer;
3. range plausibility check;
4. `VALID`, `STALE` or `INVALID` internal state;
5. separate value and validity variables in PMU Client logic.

Do not substitute the last known value indefinitely after timeout.

## Provisional plausibility ranges

These ranges are implementation guards only and must be tuned to the final motorcycle setup:

- RPM: 0 to project rev-limit + margin.
- TPS: 0 to 100 percent.
- Coolant temperature: physically plausible sensor range.
- Fuel pressure: selected transducer calibrated range.
- Oil pressure: selected transducer calibrated range.
- MAP/boost: selected FT550/internal MAP calibrated range.
- Battery voltage: motorcycle operating range with start-cranking allowance.

## Frame-map freeze procedure

The signal intent above is frozen. Frame IDs, byte positions, endian order, signedness, scaling, offsets and update rates remain `VERIFY` until obtained from one of:

- FuelTech official CAN protocol documentation;
- verified FT550 CAN broadcast configuration/export;
- controlled bench capture correlated against FTManager live values.

For each signal, record:

`CAN ID -> DLC -> start byte/bit -> length -> endian -> signed -> factor -> offset -> units -> nominal period -> timeout`.

## Safety hierarchy

Hardwired input > locally measured PMU state > validated FT550 CAN signal > stale/unknown.

CAN is not allowed to manufacture certainty. If a critical signal is stale, PMU logic must know it is stale.

## Release status

- Signal set and use-cases: FROZEN.
- Timeout philosophy: FROZEN, durations provisional pending bench update-rate evidence.
- Failure-state direction: FROZEN.
- Frame IDs/scaling: OPEN.
- PMU Client implementation/testing: OPEN.
