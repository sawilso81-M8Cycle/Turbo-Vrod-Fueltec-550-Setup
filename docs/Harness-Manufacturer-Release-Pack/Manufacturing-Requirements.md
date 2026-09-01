# Manufacturing Requirements – Rev 1 Prototype Harness

## 1. Scope

These requirements apply to the first prototype and repeat builds of the Turbo V-Rod FT550 / ECUMASTER PMU16 harness set.

## 2. Manufacturer responsibility

The manufacturer is responsible for workmanship, correct application of specified connector systems, crimp quality, sealing, loom construction, electrical testing and accurate as-built documentation.

The manufacturer shall not silently correct, reinterpret or substitute an engineering circuit. Raise an RFI for discrepancies.

## 3. Prototype measurement strategy

Several branch lengths remain vehicle-measurement gated. For the first prototype, preferred options in order are:

1. manufacturer measures the motorcycle with major components installed;
2. engineering supplies an approved dimensioned mock-up/string-board schedule;
3. manufacturer produces a deliberately serviceable prototype with agreed trim allowance, followed by final dimension freeze after fitment.

Do not guess branch lengths from photographs.

## 4. Wire

Preferred low-current construction is M22759/32 ETFE or a documented equivalent motorsport thin-wall wire. Final gauge follows `Wire-Size-Schedule.csv`; provisional gauges are not authority to manufacture where the schedule says MEASUREMENT GATED or VERIFY.

High-current PMU output and main-feed conductors must be sized from measured current/inrush, route length, voltage-drop target, ambient/loom derating and terminal capability.

## 5. CAN

Use a proper twisted pair. Preserve CAN H/CAN L polarity. Keep stubs short. Do not add hidden termination resistors. X51 service access must not alter normal bus termination.

## 6. Sensor and signal circuits

Keep CKP and precision analogue circuits physically separated from coil, injector, fan, pump, starter and other high di/dt conductors. Preserve released sensor-ground/reference topology. Do not return precision sensors through a convenient chassis/high-current ground.

## 7. Splices

Splices must be mechanically supported, sealed and staggered where appropriate to avoid a large rigid loom lump. No household solder/twist/heatshrink construction. Any soldered joint required by a specific device must be explicitly approved.

## 8. Connectors and terminals

Use exact released connector families and terminal wire ranges. Do not crimp an undersize wire into an oversize terminal by folding the conductor. Use cavity plugs in unused sealed cavities where required.

Where an OEM mating connector is unavailable, preserve the OEM pigtail and create the specified service break rather than cutting directly at the component.

## 9. Two-Step relay interface

Rev 1 bypasses the custom X70 PCB. The manufacturer shall build a replaceable sealed relay sub-harness.

Functional requirement:

- O11 OFF → FT550 A21 open → Two-Step request OFF.
- O11 ON → relay NO contact closes A21 to approved ground → Two-Step request permitted.
- relay/O11 power failure → contact open → fail OFF.
- +12 V must never be connected to FT550 A21.

Submit relay, socket/holder and suppression PNs before manufacture.

## 10. Covering and heat protection

DR-25 or approved equivalent is preferred for the main motorsport loom. Provide additional heat protection near turbo/exhaust zones. Heat protection does not substitute for adequate physical clearance.

## 11. Labels

Every service connector and major branch shall carry the controlled connector/branch ID. Harness-set and sub-harness serial numbers shall remain visible after installation.

## 12. Testing

100% electrical test is required. At minimum verify:

- intended continuity;
- no cross-circuit shorts;
- no unintended power-to-ground shorts;
- connector cavity identity;
- CAN polarity;
- X70 relay truth table;
- power/ground polarity.

Do not perform high-voltage insulation testing through connected FT550, PMU, SparkPRO, sensors or other electronics. Any hipot/megger method must be agreed before use.

## 13. Deviations

Every deviation requires a unique ID and disposition of APPROVED / REWORK / REJECT. A verbal workshop change is not an approved production change.

## 14. Repeatability

The first accepted prototype becomes the dimensional/as-built baseline for repeat manufacture. Repeat harnesses must use the frozen revision and controlled substitutions only. Each harness receives its own serial and test report.
