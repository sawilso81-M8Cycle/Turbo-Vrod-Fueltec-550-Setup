# Connector & Terminal Procurement Freeze – Rev 1

## Purpose

Convert the harness connector architecture into a controlled purchasing package suitable for prototype procurement and repeat-build sourcing.

## Authority hierarchy

1. Official device manufacturer connector/pinout documentation.
2. Existing verified project cavity schedule.
3. Physical connector identification on the motorcycle/component.
4. Approved service pigtail where a bare mating connector cannot be verified.

No connector, terminal, seal or cavity-plug part number may be invented to close a purchasing row.

## PMU16 connector family – VERIFIED

ECUMASTER PMU-16 pinout v1.2 identifies the 39-position Sicma / FCI connector system and these terminal families:

- `211CC2S2160P` – 1.5 mm terminal family, 14–17 AWG class.
- `211CC3S2120` – 2.8 mm terminal family, 14–16 AWG class.
- `211CC3S3120` – 2.8 mm terminal family, 10–12 AWG class.

The PMU main battery supply remains through the centre stud, not through the 39-way output connector.

For the 4.0 mm² fuel-pump cable rule, final termination into O1/O2 remains conditional on the selected terminal family, actual conductor OD/crimp compatibility, measured pump current and direct-PMU-drive approval. If direct drive is not approved, O1/O2 become control-only and the 4.0 mm² pump power cable terminates at the external power stage instead.

## Deutsch DTM service-break baseline – VERIFIED

For X71 clutch service break:

- housing pair baseline: `DTM04-2P` ↔ `DTM06-2S`;
- size-20 socket baseline already frozen: `0462-201-20141`;
- matching size-20 pin baseline: `0460-202-20141` for 0.5 mm² / 20 AWG class.

Final contact selection must still match the actual selected wire OD, insulation and crimp tooling.

## Fuel-pump connector rule

Primary and optional secondary fuel-pump branches are now designed around 4.0 mm² feed and 4.0 mm² dedicated return.

The pump connector/terminal system must:

- physically accept the selected 4.0 mm² wire series without conductor folding;
- have continuous current capability above the measured pump steady current with thermal margin;
- tolerate measured inrush;
- be sealed for motorcycle/fuel-system environment;
- avoid becoming the lowest-current element in the branch;
- be independently serviceable.

Final connector selection remains `PUMP_VERIFICATION_GATED` until the exact pump model/current and mating interface are confirmed.

## OEM sensor and engine hardware strategy

Where Harley service information identifies the sensor/device but does not expose the mating connector service PN, the preferred order is:

1. identify the connector from the physical device/pigtail;
2. source a traceable OEM or OEM-equivalent repair connector;
3. preserve a known-good OEM pigtail and create a controlled sealed service break;
4. do not cut directly at the device simply to force a preferred aftermarket connector.

This applies to CKP, TPS, MAP, ECT, IAT, VSS, injectors and coils until each mating connector is physically identified.

## FT550 / SparkPRO strategy

Where FuelTech supplies a completed harness or pigtail, use the supplied connector/pigtail unless an exact bare service connector and terminal system is verified. The manufacturer may not substitute a visually similar connector.

## Procurement release states

- `VERIFIED_PN` – exact purchasable part number verified from official source or physical identification.
- `VERIFIED_FAMILY` – connector family verified; exact terminal/seal variant still wire-range dependent.
- `SERVICE_PIGTAIL_APPROVED` – controlled pigtail is the production strategy.
- `PHYSICAL_ID_REQUIRED` – device must be inspected before purchase.
- `DEVICE_SELECTION_GATED` – connector cannot be frozen until the load/sensor itself is selected.
- `DNP` – deliberately not populated.

## Current status

`CONNECTOR_PROCUREMENT_FREEZE_PARTIAL`

PMU16 family and X71 DTM service break are verified. Fuel-pump, retained OEM engine devices, some service connectors and optional Peak & Hold hardware remain physical/device-selection gated.
