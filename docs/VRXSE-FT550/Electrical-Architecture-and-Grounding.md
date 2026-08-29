# Electrical Architecture and Grounding

## Three-domain architecture

The Turbo V-Rod FT550 installation is intentionally divided into three electrical domains.

### 1. EPM — Engine Power Module

Purpose: supply and control the FT550 and engine-critical actuators.

Typical loads:

- FT550 ECU power;
- injectors;
- ignition-coil power/control interfaces;
- engine-critical relays;
- other engine-control actuators where loss would immediately stop or endanger the engine.

### 2. APM — Auxiliary Power Module

Purpose: isolate large or electrically noisy auxiliary loads from engine-management measurement circuits.

Typical loads:

- primary and secondary fuel pumps;
- radiator / cooling fans;
- intercooler or charge-cooling pumps where fitted;
- boost-control hardware that requires substantial current;
- auxiliary pumps, heaters or race accessories;
- other high-current switched loads.

### 3. SIM — Sensor Interface Module

Purpose: keep precision engine measurement and trigger circuits electrically quiet and traceable.

Typical circuits:

- TPS;
- ECT;
- IAT;
- optional external MAP / pressure sensors;
- fuel pressure;
- oil pressure;
- VSS;
- CKP and any future cam-sync input;
- EGT conditioning where used;
- reference supplies;
- sensor grounds;
- communications and conditioned low-level signals.

## Common reference does not mean common current path

All three domains ultimately share the vehicle's electrical reference, but that does **not** mean their current paths should be arbitrarily tied together throughout the harness.

The objective is to prevent large changing currents from pumps, fans, coils, injectors, relays and solenoids from creating voltage offsets in the low-current reference paths used by the ECU to measure sensors.

## Harley factory clue

The reviewed 2006 VRSC engine-management drawings show TPS, MAP, ECT and IAT using a dedicated **BK/W sensor return/reference network**. This supports the principle that these devices are not intended to use a random chassis bolt as their measurement return.

For the FT550 conversion, that philosophy is retained and strengthened through the SIM.

## Grounding rules

1. **Sensor grounds are measurement returns, not convenience earths.**
2. CKP reference/shield wiring must remain in the precision domain.
3. Do not ground a sensor body or signal-return conductor to a pump, fan, starter or coil ground point unless the manufacturer explicitly requires it.
4. High-current device returns should be sized and routed for their own load, not through ECU/sensor-reference conductors.
5. Star-point or controlled commoning should occur only at deliberate engineering locations.
6. The battery negative / engine block relationship must be low resistance and mechanically robust.
7. Shield termination should follow the sensor/ECU manufacturer's recommendation and must not be improvised at both ends without evidence.
8. Separate physical routing should be used where practical between CKP/analogue sensor wiring and ignition/pump/fan/high-current PWM wiring.

## Power distribution rules

- Give EPM, APM and SIM deliberate fused feeds rather than cascading uncontrolled branches from one small conductor.
- Protect conductors for the conductor ampacity and expected fault current, not merely the normal load.
- Relay and solid-state switching architecture must consider inrush, inductive flyback and PWM operation.
- Precision 5 V references come from the ECU/reference system intended for sensors, not from an arbitrary 5 V converter.
- Do not power a 5 V sensor from 12 V because the OEM harness happened to contain a red wire nearby.

## Noise-sensitive circuits

Highest-priority segregation:

1. CKP / engine-speed trigger.
2. Future cam-sync signal if added.
3. TPS.
4. Pressure transducers.
5. Temperature sensors.
6. Wideband analogue outputs, if analogue signalling is used.

Keep these away from:

- coil primary wiring;
- spark-plug leads;
- starter motor cables;
- alternator/regulator high-current wiring;
- fuel-pump PWM feeds;
- cooling-fan feeds;
- boost solenoids where aggressively PWM driven.

## Commissioning checks

Before first start:

- continuity-test every ground domain;
- measure resistance between ECU ground, engine block and battery negative;
- verify no sensor return is accidentally tied into a high-current load return downstream of the intended common point;
- verify 5 V reference with sensors connected;
- log TPS, ECT, IAT, MAP and pressure inputs with engine off and high-current auxiliaries manually cycled;
- investigate any sensor movement caused by switching pumps/fans/solenoids;
- scope CKP while cranking before enabling fuel and ignition.

The acceptance criterion is not merely that the bike starts. The acceptance criterion is that high-current electrical activity does not materially corrupt the signals the FT550 uses to protect and control the engine.
