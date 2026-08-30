# Rev 1 Production Harness Release Checklist

## Documentation

- [ ] All five HD-style schematic sheets cross-reference current circuit IDs.
- [ ] Connector index matches the cavity schedule.
- [ ] Every populated connector cavity has a terminal family/part number.
- [ ] Every unused sealed connector cavity has a cavity plug specified.
- [ ] Harness branch schedule contains measured lengths.
- [ ] Wire schedule contains final conductor size and insulation specification.
- [ ] Splice IDs and physical splice locations are shown on harness drawing.

## Electrical verification

- [ ] Verification Register contains no release-blocking `VERIFY` rows.
- [ ] CKP polarity and waveform captured during cranking.
- [ ] TPS calibration verified at closed and WOT.
- [ ] MAP, ECT and IAT transfer functions verified.
- [ ] VSS amplitude and pulses/revolution verified.
- [ ] Injector electrical characteristics verified.
- [ ] OEM coil driver compatibility verified.
- [ ] PMU-16 output current limits validated against measured loads.
- [ ] Main positive protection and conductor sizing calculation completed.
- [ ] Ground voltage-drop test completed during cranking.

## Harness QA

- [ ] 100% point-to-point continuity check completed.
- [ ] No unintended continuity between +12 V, 5 V reference, sensor return and chassis/load return.
- [ ] CKP pair continuity, isolation and shield termination checked.
- [ ] CAN H/L continuity and termination resistance checked with system unpowered.
- [ ] Pin-retention pull check performed on every connector.
- [ ] Seals, boots and cavity plugs installed.
- [ ] Harness protected against heat, abrasion, steering/suspension motion and engine movement.

## Powered bench test

- [ ] PMU powered without loads and diagnostics normal.
- [ ] FT550 powered with injectors/coils disabled.
- [ ] 5 V reference stable with all OEM sensors connected.
- [ ] Sensor channels remain stable while PMU loads are cycled.
- [ ] Fuel pump output protection verified.
- [ ] Fan output protection verified.
- [ ] CAN loss produces defined safe states.
- [ ] Emergency stop / kill strategy removes engine torque as designed.

## Release record

When all items are complete, record:

- harness revision;
- FT550 configuration revision;
- PMU configuration revision;
- build date;
- verification date;
- as-built deviations;
- tester/approver;
- archived continuity and oscilloscope evidence.

Only then may the package move from **Rev 0 Engineering** to **Rev 1 Production**.
