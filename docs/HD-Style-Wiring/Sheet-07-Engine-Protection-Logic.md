# Sheet 07 - Engine Protection Logic

## Purpose

Define how the additional sensor channels are intended to participate in protection strategy. Exact threshold values are not frozen here; they must be established from engine specification, sensor calibration, test data and tuner validation.

## Protection hierarchy

Use progressive intervention wherever practical:

1. Warning / logging flag.
2. Boost reduction or auxiliary control reduction.
3. Ignition/fuel/torque derate as supported by the FT550 strategy.
4. RPM limitation / hard protection where continued operation is likely to cause damage.
5. Engine shutdown only for conditions where shutdown is safer than continued operation.

## Mandatory monitored conditions

### Fuel differential pressure

Derived condition:

`Fuel Differential Pressure = Fuel Rail Pressure - Manifold Absolute Pressure`

Protection objective:

- detect pump starvation, filter restriction, regulator failure or loss of pressure rise under boost;
- do not rely on rail pressure alone;
- escalate response as differential pressure departs from the validated injector pressure target.

### Engine oil pressure

Protection must be RPM-aware and, where useful, temperature-aware.

- Low pressure at idle is not treated the same as low pressure at high RPM.
- OEM oil-pressure switch may remain as an independent simple warning path.
- True pressure channel is the primary protection input.

### Lambda front/rear

Monitor both absolute mixture and cylinder imbalance.

- persistent lean operation under load -> protection action;
- large front/rear lambda divergence -> warning/derate;
- sensor fault must be distinguished from a genuinely lean cylinder where possible.

### Boost / MAP

- overboost protection uses the FT550 turbo-capable MAP reference;
- OEM MAP may be retained for plausibility comparison where its range allows;
- boost-control faults must default toward lower energy, not increased boost.

### Post-intercooler IAT

Use escalating action at excessive charge temperature:

- warning/log;
- reduce boost and/or ignition advance as validated;
- stronger protection if temperature continues to rise.

## Strongly recommended conditions

### EGT front/rear

- high absolute EGT -> warning/derate;
- abnormal front/rear spread -> cylinder imbalance flag;
- do not use EGT alone as a substitute for lambda.

### Turbo oil pressure

- detect failed/blocked turbo oil feed;
- response should account for whether the sensor is before or after an oil restrictor.

### Crankcase pressure

- high boost-correlated crankcase pressure can indicate blow-by or breather restriction;
- initially log/warn until a safe normal envelope is established from real data.

### EMAP

Initially a development channel.

- track EMAP:MAP ratio;
- use to identify turbine/exhaust restriction;
- do not create hard cut thresholds until the expected operating envelope is established.

### Turbo speed

Where installed, turbo shaft speed becomes a direct hard-limit candidate.

- warning before manufacturer turbo-speed limit;
- boost reduction as limit is approached;
- hard protection if overspeed persists.

## PMU-16 interaction

The PMU may provide additional protection evidence through current monitoring:

- fuel pump current unexpectedly low/high;
- fan current fault;
- charge-cooler pump current fault;
- auxiliary device short/open circuit.

A current-reading alone does not prove fluid flow. Sensor evidence should be combined where practical.

## CAN-loss and sensor-fault behaviour

For every protection channel define:

- open-circuit behaviour;
- short-to-ground behaviour;
- short-to-5V/12V behaviour where applicable;
- implausible-range detection;
- CAN timeout behaviour for networked sensors;
- default strategy when the measurement is lost.

Loss of a protection sensor must not silently convert to unrestricted boost operation.

## Calibration gate

No warning, derate or cut threshold is to be released until:

1. sensor transfer function is verified;
2. normal engine operating envelope is logged;
3. transient behaviour is understood;
4. nuisance-trigger risk is assessed;
5. the selected response is validated on the dyno/bench as applicable.
