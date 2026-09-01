# Open-Loop Boost Control Commissioning

## Authority

This procedure becomes executable only after the project reaches `READY_FOR_OPEN_LOOP_BOOST_CONTROL_PREP` and the spring-pressure baseline is accepted.

It authorises staged open-loop solenoid duty testing only. It does not authorise closed-loop boost control, unrestricted boost targets, power pulls, launch testing or high-RPM competition operation.

## Required baseline

Before enabling O6:

- WG-001 through WG-012 required items PASS;
- spring-pressure baseline documented and repeatable;
- O6 de-energised state proven to return minimum mechanical boost;
- solenoid plumbing and port function verified;
- build-specific MAP hard limit and abort threshold documented;
- fuel and oil pressure protection active;
- lambda logging valid;
- ECT/IAT monitoring valid;
- hardwired kill verified;
- PMU/CAN logging armed;
- boost-control duty source and output polarity documented.

## Control philosophy

Open-loop duty is introduced in small deliberate steps from the minimum command that produces a measurable response. The project must not assume that a generic duty percentage corresponds to a generic boost pressure.

Every duty change requires a new calibration/revision identifier and a complete log review before progression.

## OL-001 O6 electrical activation check

With engine not under boost load, command the smallest safe output state necessary to prove:

- O6 energises only when intended;
- solenoid polarity matches the pneumatic design;
- PMU current is within expected range;
- no overcurrent/retry event occurs;
- loss of command returns O6 OFF.

PASS: electrical control is deterministic and fail-safe.

## OL-002 Zero/minimum-duty boost run

Perform a controlled run at the minimum active duty command.

Record:

- commanded duty;
- MAP/boost curve;
- RPM;
- TPS/load;
- fuel pressure;
- oil pressure;
- lambda front/rear where available;
- ECT/IAT;
- battery voltage;
- PMU O6 status/current;
- CAN health;
- ignition timing and injector duty where available.

PASS: boost remains close to the accepted spring-pressure behaviour and no protection limit is approached.

## OL-003 First incremental duty step

Increase duty only by the build-specific approved increment.

Purpose: determine whether boost response is monotonic, stable and predictable.

Abort on:

- unexpected boost jump;
- overshoot beyond the build-specific limit;
- fuel-pressure instability;
- unsafe lambda trend;
- ignition breakup/misfire;
- rapid IAT/ECT rise;
- CAN/PMU fault;
- any sign that O6 OFF would not reduce boost.

## OL-004 Duty-response map

Repeat at successive approved low duty points until enough evidence exists to build an initial open-loop duty-to-boost map.

Do not interpolate aggressively through untested regions.

For each point, record steady/peak MAP, overshoot, spool rate, RPM/load region and thermal/fuel-system conditions.

## OL-005 Overshoot and creep assessment

At each accepted duty point distinguish:

- commanded boost rise from duty increase;
- transient overshoot;
- RPM-dependent creep;
- heat-soak-related drift;
- pneumatic hysteresis/stiction.

Any non-monotonic or unexplained behaviour blocks higher duty.

## OL-006 Gear/load restriction validation

If open-loop duty will later vary by gear, throttle or RPM, validate the underlying gear/load signals before using them to increase boost.

Unknown/invalid gear or load state must fall back to the lowest authorised duty or O6 OFF.

## OL-007 Fuel-system tracking under boost

At the highest authorised open-loop point, verify fuel pressure tracks the configured strategy and pump current remains within protection limits.

A falling pressure trend or PMU current-limit event is a NO-GO for more boost.

## OL-008 Thermal review

Review IAT, ECT and any EGT/EMAP data available across repeated runs.

Do not progress if temperature rise is cumulative, unexplained or outside the build-specific commissioning envelope.

## OL-009 Live fail-safe validation

At a low-energy accepted boost point, deliberately remove O6 command using the planned safe method and confirm:

- O6 de-energises;
- boost falls toward spring-pressure baseline;
- PMU records the event;
- no unsafe transient occurs;
- control recovers deterministically after reset/re-enable.

Do not perform this test at the highest achieved boost point.

## OL-010 CAN-loss / invalid-MAP validation

Use controlled simulation or a low-energy run to prove that CAN loss or invalid MAP cannot command a higher duty.

Fail-safe state is O6 OFF or the lowest explicitly authorised duty defined by the project safety logic.

## OL-011 Post-run inspection

Inspect wastegate plumbing, solenoid, hoses, fittings, turbo/intake hardware, fuel system, ignition hardware, PMU/O6 branch and heat exposure.

## OL-012 Open-loop release review

The open-loop map may be accepted only when:

- duty-to-boost response is repeatable;
- overshoot and creep are characterised;
- fuel/oil pressures remain stable;
- lambda and thermal behaviour are acceptable;
- fail-safe tests pass;
- CAN/PMU logic never increases boost on invalid data;
- no unresolved mechanical/electrical issue remains.

## Release state

Project state remains `OPEN_LOOP_BOOST_ONLY` until OL-001 through OL-012 required items PASS.

Promotion target: `READY_FOR_CLOSED_LOOP_BOOST_CONTROL_PREP`.

This document does not authorise closed-loop boost control by itself.
