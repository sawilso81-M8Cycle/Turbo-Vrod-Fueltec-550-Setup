# Hardware Current and Connector Evidence Pack

## Purpose

This milestone closes the remaining high-current and connector-identification gaps before Rev 1 harness release. It does not guess load current, inrush, connector family, terminal or driver compatibility.

## Evidence to collect

1. Primary fuel pump steady and inrush current.
2. Secondary fuel pump steady and inrush current if fitted.
3. Radiator fan steady and inrush current for each fitted fan.
4. Charge/intercooler pump steady and inrush current if fitted.
5. Front/rear injector resistance and operating-current evidence.
6. Front/rear ignition-coil resistance/current/driver-type evidence.
7. Physical connector family, cavity count, keying, terminal size and seal details for injectors and coils.
8. Exact harness branch length for every high-current circuit after module/load mounting is frozen.

## Measurement rules

- Measure at the actual expected operating voltage range, not only from nominal 12 V assumptions.
- Record both steady current and startup/inrush where applicable.
- Use a current probe/shunt with adequate bandwidth for motor inrush and injector/coil pulses.
- Record ambient/component temperature when it can materially affect current.
- Do not infer injector or ignition driver compatibility from resistance alone.
- Keep screenshots/photos/oscilloscope captures with the evidence ID referenced in the CSV register.

## Acceptance logic

A load is considered electrically characterized only when the repository contains sufficient evidence to determine:

- normal operating current;
- worst credible transient/inrush current;
- conductor size for actual route length and environment;
- PMU current-limit/trip strategy where PMU-powered;
- connector/terminal current suitability;
- failure behavior and retry strategy.

## Files

- `Load-Current-Measurement-Sheet.csv`
- `Injector-Coil-Connector-Evidence.csv`
- `Bench-Test-Procedure.md`
- `Evidence-Register.csv`
