# OEM Injector and Ignition-Coil Electrical Characterisation Research

## Scope

This document records what can and cannot currently be proven about the electrical characteristics of the OEM VRXSE/VRSC injector and ignition-coil hardware from public manufacturer/Harley material.

## Hardware identity already established

- Injector kit: Harley-Davidson 27791-05.
- Injector contained in the kit: Harley-Davidson 27772-06.
- Ignition coil: Harley-Davidson 32477-01A, quantity two.

## Authoritative findings

Harley-Davidson parts information consistently identifies 32477-01A as the VRSC/VRXSE coil assembly. Public Harley material reviewed for this milestone does not publish the coil primary resistance, peak current, dwell specification, internal-igniter topology or a direct FT550 driver-compatibility statement.

Likewise, public Harley material reviewed for 27772-06 does not publish injector winding resistance, peak/hold current, dead-time data or a definitive high-impedance/low-impedance classification.

## Secondary evidence retained as comparison only

Aftermarket replacement coils marketed as replacements for Harley 32477-01A are commonly advertised as 3-ohm coils. This is useful comparison evidence but is not accepted as proof that the installed Harley 32477-01A coil itself measures 3 ohms or that its internal construction is identical.

Aftermarket injector listings cross-reference 27772-06, but published flow values vary between replacement products. Those flow claims must not be used as the OEM injector flow rating or as proof of electrical impedance.

## Engineering decision

Do not freeze injector or coil driver strategy from aftermarket replacement claims.

The following remain mandatory evidence gates before Rev 1 release:

1. Measure cold injector resistance on both 27772-06 injectors using a meter appropriate for low-resistance work.
2. Capture injector current waveform under controlled pulsed operation to determine peak/steady behaviour.
3. Measure cold primary resistance of both 32477-01A coils using a four-wire/Kelvin method where practical.
4. Identify connector cavity count and pin functions physically.
5. Determine whether the coil contains an internal igniter by electrical testing and/or verified service information.
6. Capture coil primary current ramp under a controlled test driver before assigning FT550 dwell or direct-driver strategy.
7. Compare front and rear components; a significant mismatch is a component fault or evidence concern, not a calibration target.

## Repository rule

Until these measurements are captured, the injector and coil electrical fields remain `VERIFY`. The project may use the known Harley part numbers for connector sourcing and mechanical identification, but not for assumed impedance, current or driver type.

## Public source notes

- Harley Service Information Portal identifies 32477-01A as the coil assembly across VRSC applications and VRXSE-family fitment.
- Harley documentation confirms the injector kit/part identity already recorded in this repository.
- Secondary replacement-coil listings describing 32477-01A replacements as 3 ohm are retained only as non-authoritative comparison evidence.
