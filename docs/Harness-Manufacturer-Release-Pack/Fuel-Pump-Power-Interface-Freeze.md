# Fuel-Pump Power Interface Freeze – Rev 1

## Purpose

Freeze the harness-side high-current service interface for the primary and optional secondary fuel pumps while preserving the measurement-gated decision between direct PMU drive and an external power stage.

## Locked conductor rule

Each fuel-pump circuit uses:

- **4.0 mm² feed**;
- **4.0 mm² dedicated return**;
- no downsizing through a connector pigtail, relay lead or ground transition without engineering approval.

## Selected connector family

The preferred production family is **TE Connectivity Heavy Duty Sealed Connector Series (HDSCS) using AMP MCP 6.3/4.8K contacts**, 2-position, sealed, free-hanging wire-to-wire configuration.

Why this family:

- TE documents 2-position sealed HDSCS housings in the MCP 6.3/4.8K family with up to **40 A maximum contact rating** depending on exact contact/housing configuration;
- the family is rated for harsh automotive use and -40 °C to +140 °C housing operating temperature;
- sealable MCP contacts are available for **4.0 mm²** conductors;
- the connector can serve as a repeatable harness-side service break regardless of the native pump connector.

## Preferred harness-side baseline

Housing family baseline:

- **TE 1-1564542-1** or keyed equivalent within the same 2-position HDSCS MCP 6.3/4.8K family, selected to prevent cross-connection between Pump 1 and Pump 2 where both are fitted.

Contact baseline for 4.0 mm²:

- **TE 1241418-4** tin-plated sealable MCP 6.3/4.8K receptacle, 4–6 mm², typical 36 A;
- silver-plated **TE 1-1241418-3** is an alternative high-current candidate, 4–6 mm², typical 37 A, subject to mating-contact compatibility and manufacturer DFM approval;
- **TE 1241416-1** accepts 2.5–4.0 mm² and is rated around 30 A typical, so it is not the preferred margin choice for a pump that may approach 30 A continuously.

Final tab-side contact and exact mating housing shall be selected from TE-compatible HDSCS/MCP parts during manufacturer DFM and documented in the as-built BOM. No mixed-brand or visually similar contact substitution is allowed without written approval.

## Native pump connector strategy

The selected pump may have its own moulded connector or pigtail. Do not force the pump body to use HDSCS.

Preferred arrangement:

`Main harness 4.0 mm² → HDSCS X30/X31 service break → short 4.0 mm² pump-specific pigtail → native pump connector`

This allows the main harness to remain repeatable while only the short pump pigtail changes if the fuel-pump model changes.

The pump-specific pigtail shall not be reduced below 4.0 mm² unless the pump manufacturer's native connector/wire design is explicitly accepted after current and voltage-drop verification.

## Direct PMU drive compatibility

If pump testing eventually proves `DIRECT_PMU_DRIVE_APPROVED`:

`PMU O1/O2 → 4.0 mm² branch → X30/X31 HDSCS → pump pigtail → pump`

Approval still requires exact PMU hardware, cavity terminal, measured steady/inrush current, connector thermal behaviour and installed voltage-drop evidence.

## External power-stage compatibility

If pump testing results in `EXTERNAL_POWER_STAGE_REQUIRED`:

`Protected battery/high-current distribution → relay/SSR/contact stage → 4.0 mm² branch → X30/X31 HDSCS → pump pigtail → pump`

PMU O1/O2 then become control outputs only. X30/X31 remain unchanged, which prevents the main harness from needing redesign.

## Keying / identification

Where two pumps are fitted:

- Pump 1 and Pump 2 must use different keyed housings or an unmistakable physical/label strategy;
- labels `FP1-PWR/RTN` and `FP2-PWR/RTN` must remain visible after final loom covering;
- reverse polarity must be impossible through correct cavity assignment and keying.

## Environmental requirements

- service break must be outside direct fuel immersion unless the selected connector is specifically approved for immersion;
- mount away from exhaust/turbo radiant heat;
- provide strain relief so pump vibration is not carried into the terminal crimp;
- no unsupported connector mass at the pump body;
- use correct seals for the selected 4.0 mm² wire insulation diameter.

## Acceptance criteria

Before production release:

1. exact pump PN identified;
2. measured steady and inrush current recorded;
3. exact HDSCS housing pair and both mating contact PNs documented;
4. selected contacts accept the actual 4.0 mm² wire and insulation diameter;
5. crimp pull/inspection evidence accepted;
6. continuous-current temperature-rise test completed at representative current;
7. voltage drop across the mated connector recorded;
8. polarity and cavity map verified;
9. pump-specific native pigtail connector identified;
10. direct-PMU vs external-stage decision formally dispositioned.

## Release state

**FUEL_PUMP_HARNESS_SERVICE_INTERFACE_FAMILY_FROZEN**

**PUMP_NATIVE_CONNECTOR_AND_FINAL_SWITCHING_DECISION_MEASUREMENT_GATED**
