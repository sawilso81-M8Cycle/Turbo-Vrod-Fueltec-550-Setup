# Turbo V-Rod FT550 / PMU16 Installation & Commissioning Manual

**Project:** Turbo V-Rod Destroyer / VRXSE  
**Engine-management:** FuelTech FT550  
**Power management:** ECUMASTER PMU16  
**Ignition driver:** FuelTech SparkPRO  
**Harness:** Project Rev 1 production architecture  
**Manual state:** WORKING CONTROLLED MANUAL / PHYSICAL VALUES REMAIN EVIDENCE GATED WHERE MARKED

---

# How to use this manual

This manual is intended to be the workshop sequence from parts-on-bench through final dyno validation. It consolidates the repository engineering into one readable procedure, but the Git repository remains the source of truth for controlled values, verification worksheets and later revisions.

Every objective starts with a short plain-English explanation of what the system does and why the step matters. Each installation section then gives a numbered procedure, test points and a release condition. Do not skip a failed test point merely because the next system appears to work.

Repository status words mean:

- **FROZEN / VERIFIED:** use as released unless an engineering change supersedes it.
- **TBD / VERIFY / OPEN:** do not guess. Inspect, measure or obtain authoritative source evidence.
- **MEASUREMENT_GATED:** the circuit architecture is known but final current, protection, terminal or length depends on the actual hardware.
- **DNP:** do not populate unless the project deliberately enables that feature.
- **SUPERSEDED:** retain for history only; do not build from it.

## Current supersession rules used by this manual

1. Fuel Pump 1 and Pump 2 feeds are **4.0 mm² minimum**, each with a **dedicated 4.0 mm² return** to the high-current return structure. Older 2.5 mm² pump notes are superseded.
2. B15 battery/J-P01 to PMU main feed baseline is **10.0 mm²**, final protection evidence gated.
3. B39 injector power and B40 ignition/SparkPRO power are independent protected engine-critical branches.
4. The current Two-Step interface **bypasses the old custom X70 PCB**. Use the TE 1393292-5 resistor-suppressed relay architecture: PMU O11 energises the relay coil; the isolated NO dry contact grounds FT550 A21. **+12 V must never reach A21.**
5. The CAN spine is FT550 CAN A to PMU CAN2 at 1 Mbps with exactly two end terminations. X51 is a short service stub with no permanent termination.

Primary helper files: `docs/Project-Master-Release-Dashboard.md`, `docs/Project-Status/Repository-Master-Index-and-Build-Readiness-Audit.md`, `docs/Manufacturer-Construction-Package-Current/00-READ-ME-FIRST.md`, `docs/Harness-Manufacturer-Release-Pack/README.md`.

---

# CHAPTER 1 - COMPLETE BILL OF MATERIALS

## Objective brief

Before installation begins, put every required component, connector, wire type, protection device, test instrument and consumable on one controlled list. Missing hardware creates the temptation to substitute something that "looks close". In a motorsport harness, that is how intermittent faults acquire a passport.

Use `docs/Production-Harness-Milestone/Rev1-Harness-BOM.csv`, `docs/Manufacturer-Construction-Package-Current/06-Connector-Purchasing-BOM.csv`, `docs/Launch-Control/Two-Step-Physical-Hardware-BOM.csv`, `docs/Handover/Handover-Spare-Parts-Maintenance-Register.csv` and all applicable freeze files before procurement.

## 1.1 Core control hardware

| Item | Requirement | Qty | Status / action |
|---|---|---:|---|
| FuelTech FT550 | Project ECU baseline | 1 | FROZEN |
| ECUMASTER PMU16 | Project PDM baseline | 1 | FROZEN |
| FuelTech SparkPRO 2-channel | Passive-coil current driver | 1 | Exact installed model/revision VERIFY |
| PMU16 39-way connector | Sicma/FCI family matching exact PMU | 1 | Family verified, exact production combination VERIFY |
| FT550 connector kit | Genuine FuelTech service kit or supplied harness connector | 1 set | VERIFY service PN/tooling |
| Laptop + FTManager | ECU setup/logging | 1 | REQUIRED |
| Laptop + PMU Client | PMU programming/logging | 1 | REQUIRED |

PMU terminal families currently documented are 211CC2S2160P for the 1.5 mm contact family, 211CC3S2120 for the 2.8 mm 14-16 AWG family and 211CC3S3120 for the 2.8 mm 10-12 AWG family. Match each cavity, conductor outside diameter and current class before crimping.

## 1.2 Primary power and ground hardware

- B15 10.0 mm² motorsport/automotive cable, final installed length bike-measured.
- Main battery-to-PMU protection device, **rating TBD until final load/protection coordination**.
- J-P01 insulated positive distribution point / high-current junction, hardware rating to exceed released load.
- J-P02 high-current ground star/junction.
- Appropriate battery, engine and device ring terminals matched to actual stud diameters and conductor sizes.
- Boots/covers for exposed positive studs.
- Dedicated PMU device ground conductor to J-P02.
- Dedicated FT550 primary ground path per FT550 architecture.
- Precision FT550 sensor-ground bus/splice pack, separate from J-P02 high-current return.

Helper files: `Sheet-01-Master-Power-and-Grounds.md`, `Primary-Power-Distribution-Freeze.md`, `Primary-Power-Verification-Register.csv`, `Splice-Ground-Reference.md`, `Splice-Junction-Master-Schedule.csv`.

## 1.3 Wire and cable

Minimum workshop stock should include the released motorsport thin-wall family or an approved equivalent, preferably ETFE/M22759-style where suitable.

- 0.35 mm²: precision signals, CAN conductors, trigger conductors where terminal compatible, clutch/Two-Step signal side.
- 0.50 mm²: injector commands, ignition commands, X70 relay coil/control wiring.
- 0.75 mm²: selected service/auxiliary power and boost solenoid supply.
- 1.0 mm²: current B39 injector branch baseline and SparkPRO/coil paths where specified.
- 1.5 mm²: current B40 ignition supply baseline.
- 2.0 mm²: charge-cooler pump provisional baseline if fitted.
- 2.5 mm²: radiator fan provisional baseline pending measured load.
- **4.0 mm²:** Pump 1 feed, Pump 1 dedicated return, Pump 2 feed, Pump 2 dedicated return.
- **10.0 mm²:** B15 PMU main-feed baseline.
- 120-ohm-characteristic-impedance CAN twisted pair, 2 x 0.35 mm² class.
- Low-capacitance shielded twisted pair for CKP.

Do not fold a small conductor to make it fit an oversized terminal. Select the correct terminal or revise the connector through DFM/change control.

## 1.4 Connectors and service interfaces

Required or planned connector groups include:

- OEM CKP connector matching sensor 32313-01A.
- OEM TPS connector matching 27975-01.
- OEM MAP connector matching 32416-10.
- OEM ECT connector matching 32315-01.
- OEM IAT connector matching 27388-01.
- OEM VSS connector matching 74402-05B.
- Front/rear injector connectors matching installed 27772-06 injector hardware only after physical verification.
- Front/rear coil connectors matching installed 32477-01A coil hardware only after physical verification.
- X30 Pump 1 service break: TE HDSCS/MCP sealed high-current family sized for 4-6 mm², exact mating half DFM verified.
- X31 Pump 2 service break: same electrical class with alternate key/identification.
- X50 engineering/service connector: sealed low/medium-current only.
- X51 CAN service connector: Deutsch DTM 4-way family, exact housing/contact/cap PNs freeze before final manufacture.
- X62/X63 injector-driver service junction pair allowing direct-drive bypass or optional Peak & Hold module.
- X70 Two-Step relay holder/socket for TE 1393292-5 relay, exact holder PN DFM gated.
- X71 clutch switch service connector, current family Deutsch DTM04-2P / DTM06-2S with appropriate contacts.

Use `Connector-Cavity-Master-Schedule.csv`, `Connector-Purchasing-BOM.csv`, `OEM-Connector-Physical-ID-Register.csv`, `OEM-Pigtail-Verification-Register.csv` and `Connector-Terminal-Procurement-Freeze.md`.

## 1.5 Fuel system electrical hardware

- Pump 1 exact make/PN: **VERIFY BEFORE RELEASE**.
- Pump 2 exact make/PN if fitted: **VERIFY BEFORE RELEASE**.
- 4.0 mm² feed and return wiring for each pump.
- X30/X31 sealed high-current service connectors.
- If measured pump load exceeds safe PMU direct-drive capability/margin: approved external relay or solid-state power stage, branch protection and control wiring.
- Fuel-pressure transducer, 5 V compatible, range selected for actual rail/regulator system.
- Mechanical/reference fuel pressure gauge for commissioning correlation.

Helper files: `Fuel-Pump-Power-Interface-Freeze.md`, `Fuel-Pump-External-Power-Stage.md`, `Fuel-Pump-Verification-Pack.md`, `Fuel-Pump-Power-Stage-Decision-Register.csv`.

## 1.6 Injector and ignition hardware

- 2 x installed injectors, exact PN verified; project research currently points to Harley 27772-06 baseline but physical installed hardware wins.
- Optional FuelTech-compatible Peak & Hold module **only if electrical verification requires it**.
- 2 x passive ignition coils, exact installed PN verified; project baseline 32477-01A.
- 1 x FuelTech SparkPRO 2-channel.
- SparkPRO connector/service hardware and B40 protected supply.

Do not set injector driver mode or dwell from appearance. Complete the injector and coil verification worksheets first.

## 1.7 Sensors

Core retained sensors:

- CKP 32313-01A baseline.
- TPS 27975-01 baseline.
- MAP 32416-10 baseline.
- ECT 32315-01 baseline.
- IAT 27388-01 baseline.
- VSS 74402-05B baseline.

Added mandatory/strongly recommended instrumentation for this turbo project:

- fuel pressure transducer;
- engine oil pressure transducer;
- post-intercooler IAT;
- dual wideband lambda, preferably one channel per cylinder;
- boost/MAP via verified FT550 input/internal MAP strategy.

Development sensors as required: wastegate/dome pressure, turbo speed, front wheel speed, turbo oil pressure, crankcase pressure, EGT front/rear, EMAP, intercooler coolant temperature, IMU, brake pressure/switch, suspension travel. Do not wire thermocouples directly to standard analogue inputs without the appropriate interface/controller.

## 1.8 Cooling, boost and auxiliary hardware

- Radiator fan 1, exact PN/load VERIFY.
- Radiator fan 2 only if fitted.
- Charge/intercooler pump only if fitted.
- Boost-control solenoid, exact PN/current VERIFY.
- Pneumatic wastegate hardware configured so unpowered boost solenoid returns system to minimum mechanical boost.
- Warning lamp if O8 used.
- Logger/display/service load if O10 used.

## 1.9 Two-Step / clutch hardware

Current production implementation:

- OEM clutch switch Harley 71620-08.
- OEM spring clip 46865-06.
- X71 sealed clutch-switch connector.
- Input pull-up/interface as required after bench polarity verification.
- TE Connectivity Micro Relay A **1393292-5 / V23074A1001A402**, 12 V coil, resistor suppression.
- Traceable retained Micro-ISO-compatible holder/socket with correct female terminals.
- 0.50 mm² coil command and return.
- 0.35 mm² dry-contact common and A21 request wire.
- Optional A7 clutch-position Hall sensor only after mechanical mock-up.

Old X70 PCB files remain useful engineering history but are **not the current physical build**.

## 1.10 Harness protection and consumables

- DR-25 or approved equivalent main loom covering.
- Turbo/exhaust-rated additional heat sleeve/barrier/boots by zone.
- Raychem-style moulded boots/heat-shrink transitions or manufacturer-approved equivalent.
- Adhesive-lined heat shrink only where the released process calls for it.
- Abrasion braid/sleeve in rub-risk zones.
- Rubber-lined P-clips / approved harness clamps.
- Grommets where loom passes edges/panels.
- Cavity plugs and seals for unused sealed connectors.
- Heat-shrink circuit/branch labels and permanent harness serial label.
- Approved sealed splice hardware/process.

## 1.11 Workshop and commissioning equipment

- Quality DMM with low-ohm and min/max capability.
- DC current clamp capable of pump/fan inrush capture.
- Oscilloscope suitable for CKP/trigger and ignition diagnostic work.
- Current-limited bench supply where appropriate.
- Battery charger/support supply suitable for ECU programming and cranking tests.
- Fused test leads and breakout leads.
- Independent fuel-pressure gauge/reference transducer.
- Independent oil-pressure reference where practical.
- Temperature measurement device.
- Laptop with FTManager and PMU Client.
- CAN interface/service lead for X51.
- Crimp tooling for every released terminal family.
- Terminal extraction tools.
- Pull-test equipment or manufacturer pull-test records.
- Fire extinguisher suitable for workshop fuel/electrical work.
- Dyno with suitable motorcycle restraint, extraction and cooling for final stages.

**Chapter 1 release:** Do not start final harness installation until missing BOM items are either physically identified, formally DNP or controlled as a deliberate test-gated item.

---

# CHAPTER 2 - UNDERSTANDING THE ELECTRICAL ARCHITECTURE

## Objective brief

The bike has several electrical "neighbourhoods" sharing one battery. High-current pumps and fans are noisy neighbours. Sensors are the library. This architecture keeps the nightclub out of the library while still giving everything one controlled electrical reference.

### Engine-critical power domain

FT550, injector supply B39 and ignition/SparkPRO supply B40 are engine-critical. Faults should be contained so an auxiliary branch does not casually reset the ECU or corrupt precision signals.

### Auxiliary/high-current PMU domain

PMU16 controls pumps, fans, charge-cooler pump, boost-solenoid supply, warnings and service loads.

### Precision sensor domain

FT550 5 V reference and FT550 sensor ground serve precision sensors. This ground is not a convenient general earth point.

## Required ground structure

- G1: battery negative to engine, heavy primary return.
- G2: battery negative/high-current star to PMU ground path.
- G3: FT550 primary power ground to controlled star point.
- G4: FT550 sensor ground bus only.
- G5: chassis/bond only as verified.

**Test point:** With battery disconnected, confirm no pump/fan/SparkPRO power return terminates into G4 sensor ground.

Reference: `docs/VRXSE-FT550/Electrical-Architecture-and-Grounding.md`, `Sheet-01-Master-Power-and-Grounds.md`, `Splice-Ground-Reference.md`.

---

# CHAPTER 3 - PHYSICAL LAYOUT, MEASUREMENT AND HARNESS ROUTING

## Objective brief

Before connecting anything, decide where every module lives and where the loom physically travels. Electrical perfection with a loom touching a turbine housing is merely a delayed smoke test.

## 3.1 Freeze component locations

1. Mount or mock up FT550, PMU16, SparkPRO, J-P01, J-P02, X70, X50, X51 and all selected pumps/sensors.
2. Orient connectors so the loom can leave each device without a sharp bend.
3. Leave service room to unlatch and remove connectors.
4. Keep FT550/PMU/SparkPRO away from direct exhaust/turbo radiant heat and water paths.
5. Put X70 where the relay can be serviced without cutting the loom.
6. Put X51 where a diagnostic lead can be attached without dismantling half the motorcycle.

**Test point:** Photograph each final location with connector orientation and a scale/reference. Complete `Physical-Bike-Evidence-Master-Register.csv`.

## 3.2 Measure B01-B44

1. Use string or flexible wire along the real intended route, not a straight-line tape measurement through open space.
2. Mark start datum, breakout and endpoint.
3. Record routed centreline length.
4. Record service loop separately.
5. Move steering full left and full right for B41/B42/front branches.
6. Move suspension/rear branches through the practical movement envelope.
7. Mark heat-protection zones.
8. Enter actual values into `B01-B44-Physical-Dimension-Capture.csv` and later `B01-B44-Dimensional-Freeze-Worksheet.csv`.

Prototype first-cut examples are provided in `05-Prototype-Cable-Size-Length-Schedule.csv`, but they are not permission to ignore bike measurement.

## 3.3 Routing rules

- CKP/shielded trigger wiring away from coils, injector drive, starter and pump/fan current paths.
- CAN twisted pair remains twisted through the trunk and short service branch.
- Sensor reference/signal loom separated from high-current branches where practical.
- No splice in steering flex zones.
- No hidden extra loop stuffed inside DR-25 to consume an inaccurate branch length.
- Heat sleeve supplements clearance; it does not justify routing directly beside the turbine/downpipe when a safer route exists.

**Release:** `PHYSICAL_HARNESS_DIMENSIONS_FROZEN` only after real measurements and movement checks pass.

---

# CHAPTER 4 - PRIMARY POWER, MASTER ISOLATION AND GROUNDS

## Objective brief

This is the foundation. A poor main feed or ground creates symptoms everywhere: ECU resets, false sensor readings, CAN errors, weak pumps and hot terminals. Build power from the battery outward, and test each layer before adding loads.

## 4.1 Battery disconnected mechanical installation

1. Disconnect battery negative, then positive as required by safe workshop practice.
2. Install J-P01 insulated positive junction.
3. Install J-P02 high-current ground star.
4. Install B15 10.0 mm² baseline from protected battery/J-P01 path to PMU main stud.
5. Install PMU device ground to J-P02.
6. Install FT550 primary ground to the released star structure.
7. Install dedicated Pump 1/2 returns to J-P02, never to sensor ground.
8. Protect exposed positive studs with boots/covers.

## 4.2 Unpowered tests

- Measure continuity battery negative -> engine -> J-P02.
- Check FT550 primary ground path continuity.
- Confirm G4 precision sensor ground does not carry intentional pump/fan/coil returns.
- Confirm no short B+ to ground before installing main protection.

Use milliohm/voltage-drop methods for final validation rather than trusting continuity-beeper alone.

## 4.3 B15 protection

The final B15 fuse/breaker rating remains evidence gated. Use `Primary-Power-Load-Case-Register.csv`, `B15-B39-B40-Protection-Load-Coordination-Pack.md` and `Protection-Coordination-Final-Freeze-Register.csv` to close it after measured loads.

**Do not fit a larger fuse merely because the smaller one opens.** The fuse must protect cable, terminal, connector and junction path.

---

# CHAPTER 5 - PMU16 WIRING AND INITIAL CHANNEL PARAMETERS

## Objective brief

The PMU16 is the electrical traffic controller. It replaces a collection of conventional fuses/relays with monitored high-side outputs and programmable logic. The initial configuration should be deliberately conservative: outputs disabled until their wiring is verified, current limits only frozen after actual load measurements, and hardwired master/kill logic always outranks CAN.

## 5.1 Verified physical pin map used by this project

| PMU item | Pin | Hardware capability | Initial project use |
|---|---:|---|---|
| Main battery stud | STUD | 150 A max constant device rating | B15 protected feed |
| Ground | 25 | device ground | J-P02 |
| +12 V switched | 7 | switched input | PMU enable supply |
| +5 V | 15 | 500 mA max | PMU-local reference only |
| O1 | 38 | 25 A high-side | Primary fuel pump |
| O2 | 39 | 25 A high-side | Secondary/staged pump if fitted |
| O3 | 26 | 25 A high-side | Radiator fan 1 |
| O4 | 13 | 25 A high-side | Radiator fan 2 if fitted |
| O5 | 12 | 25 A high-side | Charge-cooler pump if fitted |
| O6 | 11 | 15 A high-side | Boost-solenoid protected supply |
| O7 | 10 | 15 A high-side | reserved auxiliary |
| O8 | 9 | 15 A high-side | warning/fault lamp if used |
| O9 | 5 | 15 A high-side | reserved race accessory |
| O10 | 4 | 15 A high-side | logger/display/service feed |
| O11 | 3 | 15 A high-side | X70 Two-Step relay coil command |
| O12 | 2 | 25 A high-side | reserve |
| O13 | 1 | 25 A high-side | reserve |
| O14 | 14 | 25 A high-side | reserve |
| O15 | 27 | 25 A high-side | reserve |
| O16 | 28 | 25 A high-side | reserve |
| A1 | 29 | 0-5 V input | MASTER_ENABLE |
| A2 | 16 | 0-5 V input | START_REQUEST |
| A3 | 30 | 0-5 V input | KILL_REQUEST |
| A4 | 17 | 0-5 V input | FAN_OVERRIDE |
| A5 | 31 | 0-5 V input | SERVICE_MODE |
| A6 | 18 | 0-5 V input | clutch discrete input |
| A7 | 32 | 0-5 V input | optional clutch position |
| CAN2 H/L | 24 / 37 | 125/250/500/1000 kbps | FT550 vehicle CAN at 1 Mbps |
| CAN1 H/L | 23 / 36 | fixed 1 Mbps | reserved peripheral/expansion baseline |

Note: older allocation sheets may label O11/A6/A7 as reserved. Current project-specific freeze assigns O11 to X70, A6 to the clutch switch and A7 to optional clutch position.

## 5.2 Initial PMU logic parameters

These are commissioning starting values, not final race calibration:

- `SYSTEM_ARMED = MASTER_ENABLE && !KILL_REQUEST`
- `ENGINE_RUNNING = FT_RPM_VALID && FT_RPM > 400`
- `ENGINE_CRANKING = START_REQUEST || (FT_RPM_VALID && FT_RPM > 0 && FT_RPM <= 400)`
- O1 fuel prime time: **3.0 s starting value**.
- CAN RPM loss grace for O1: **1.0 s starting value**.
- Fan 1 starting placeholders: ON 95 C / OFF 90 C.
- Fan 2 if fitted: ON 100 C / OFF 94 C, minimum 0.5 s stagger after Fan 1.
- Charge-cooler post-run placeholder if used: 30 s.
- O6 boost-solenoid supply: ON only when SYSTEM_ARMED, ENGINE_RUNNING and required CAN health is valid; OFF on relevant CAN/MAP failure so plumbing returns to mechanical minimum boost.
- O10 service/logger: ON with SYSTEM_ARMED and permitted in SERVICE_MODE.
- Kill request immediately removes O1, O2 and O6. Fans may remain only if the validated strategy explicitly allows cooling after kill.

## 5.3 Initial output current-limit policy

Do **not** type generic current limits into PMU Client and call the job finished.

1. Leave nonessential output disabled until branch continuity/polarity is verified.
2. Measure actual steady and start/inrush current with `Electrical-Load-Test-Master-Register.csv`.
3. Confirm terminal and conductor capability.
4. Confirm PMU channel continuous/transient capability.
5. Set current limit/retry profile only after the normal transient is understood.
6. Validate overload/fault response safely.
7. Record final values in `Protection-Fuse-PMU-Current-Limit-Master-Schedule.csv` and protection freeze registers.

**Special fuel-pump rule:** O1/O2 are 25 A-class outputs. Because the final pumps may approach or exceed that territory, do not assume direct PMU drive. If measured current, transient demand or required thermal margin is unsuitable, O1/O2 become low-current commands for external stages while the 4.0 mm² pump feed/return remains.

## 5.4 PMU bench test before bike power

Use `PMU-Bench-Commissioning-Test-Plan.md` and `PMU-Bench-Test-Matrix.csv`.

- Verify A1-A6 polarity one input at a time.
- Verify each output using a low-risk representative load/test lamp or appropriate bench fixture, not the engine hardware first.
- Verify kill overrides normal logic.
- Verify output labels correspond to physical pins.
- Verify O11 changes state only under intended clutch/launch permissive logic.
- Save PMU project revision before installing on bike.

---

# CHAPTER 6 - FT550 SENSOR AND TRIGGER INSTALLATION

## Objective brief

The FT550 makes decisions from sensor voltage. A sensor can be perfectly healthy and still lie to the ECU if its 5 V reference, ground or signal wire is wrong. Install and test sensors as precision circuits, not accessories.

## 6.1 CKP crank sensor

Baseline: Harley 32313-01A, two-wire VR sensor.

1. Route as dedicated twisted/shielded pair B02.
2. Keep it away from starter, coils, SparkPRO outputs, injector drive and pump/fan feeds.
3. Project FT550 target is A19 RPM+ and A18 RPM-.
4. Do not permanently assume polarity from wire colour alone. Scope during dead-engine crank and confirm sync.
5. Shield termination follows released trigger-integrity document; do not create multiple random shield grounds.

**Test:** during FP-9 crank test, RPM must be stable/plausible and trigger/sync status free from unexplained faults.

## 6.2 TPS

Baseline 27975-01: R/W 5 V, BK/W sensor return, GY/V signal, project FT550 signal A22.

1. Key off: verify no signal short to B+ or power ground.
2. Key on: verify 5 V reference and sensor-ground integrity.
3. Observe raw TPS voltage/percentage closed.
4. Open throttle slowly to full and back. Reading must be smooth and monotonic.
5. Calibrate only after mechanical stops/linkage are correct.

## 6.3 MAP

Baseline OEM MAP 32416-10 is retained. Connect 5 V, sensor ground and signal to the verified FT550 analog input allocation. FT550 internal 7-bar MAP may be used as additional turbo reference according to the final calibration strategy.

**Test:** engine off MAP should correlate plausibly with local barometric pressure/reference.

## 6.4 ECT and IAT

ECT baseline 32315-01 to FT550 A24. OEM IAT baseline 27388-01 to FT550 B5. Verify curves against the exact sensor definition before trusting protection thresholds.

**Test:** after a true cold soak, IAT and engine-temperature readings should be close to an independent ambient reference. Large disagreement is a wiring/calibration investigation, not something to hide by editing a table blindly.

## 6.5 VSS

Baseline 74402-05B: supply, signal and return according to verified physical connector. Project FT550 speed input A26.

**Test:** stationary reading zero; later wheel/dyno test verifies pulses/scaling.

## 6.6 Added pressure/temperature sensors

Fuel pressure and oil pressure use FT550 5 V reference and precision sensor ground unless the exact sensor/controller requires another scheme. Post-intercooler IAT is routed as a precision sensor. Record every sensor PN, range, scaling, input cavity and calibration source in `Sensor-Expansion-Matrix.csv` and `FT550-Input-Allocation.csv`.

---

# CHAPTER 7 - INJECTOR SYSTEM, B39 AND DRIVER DECISION

## Objective brief

An injector is an electrically operated valve, but the ECU output must be compatible with the coil inside it. Low-impedance injectors can demand more current than a direct ECU driver is designed to handle, so this project deliberately includes a serviceable direct-drive/Peak & Hold decision point.

## 7.1 Install the power and command paths

- FT550 A1 Blue #1 = front injector command.
- FT550 A2 Blue #2 = rear injector command.
- B39 = independent protected injector +12 V supply.
- X62/X63 = service junction allowing a removable direct link or Peak & Hold module.

## 7.2 Before connecting injectors

1. Record exact injector PN and markings.
2. Measure resistance at known approximate temperature.
3. Compare front/rear consistency.
4. Obtain manufacturer/verified electrical characterization.
5. Complete `Injector-Electrical-Verification-Worksheet.csv`.
6. Decide `FT550_DIRECT_DRIVER_APPROVED`, `PEAK_AND_HOLD_STAGE_REQUIRED` or `FURTHER_TEST_REQUIRED`.

Do not fit both direct bypass and Peak & Hold simultaneously.

## 7.3 Test points

- B39 correct voltage only when intended.
- No B39 leakage into sensor/reference circuits.
- Front/rear command continuity correct and not swapped.
- Injector current/load and B39 voltage drop acceptable under controlled test/running conditions.

Final B39 conductor/protection is frozen using `B15-B39-B40-Final-Protection-Decision-Register.csv`.

---

# CHAPTER 8 - IGNITION, SPARKPRO AND B40

## Objective brief

The FT550 A8/A9 outputs are ignition commands. The passive V-Rod coils require the SparkPRO current driver between ECU and coils. The SparkPRO is the muscle; the FT550 is the conductor waving the baton.

## 8.1 Wiring

- FT550 A8 -> SparkPRO CH1 input -> front coil.
- FT550 A9 -> SparkPRO CH2 input -> rear coil.
- SparkPRO pin 1 CH1 input, 0.50 mm².
- pin 2 power ground to J-P02, 1.0 mm².
- pin 3 CH2 input, 0.50 mm².
- pin 4 CH2 output to rear coil, 1.0 mm².
- pin 5 second power ground to J-P02, 1.0 mm².
- pin 6 CH1 output to front coil, 1.0 mm².
- B40 provides independent protected SparkPRO/ignition power according to final hardware topology.

Both SparkPRO grounds are mandatory. Do not route them into FT550 sensor ground.

## 8.2 Dwell verification

1. Record exact coil PN and SparkPRO model/revision.
2. Use manufacturer/source evidence and controlled testing to establish dwell baseline.
3. Do not infer safe dwell from idle or coil DC resistance alone.
4. Record B40 supply current and hot behaviour.
5. Freeze `B40_PROTECTION_FROZEN` only after evidence is accepted.

Helper files: `Coil-SparkPRO-Verification-Pack.md`, `Coil-Dwell-B40-Final-Decision.csv`, `Ignition-Coil-SparkPRO-Electrical-Freeze.md`.

---

# CHAPTER 9 - FUEL PUMPS

## Objective brief

The pump circuit is one of the hardest-working branches on the bike. Voltage lost in cable/terminals becomes heat and lost fuel pressure. That is why both feed and return are deliberately oversized relative to small signal wiring.

## 9.1 Wiring requirement

For **each pump**:

- feed = 4.0 mm² minimum;
- dedicated return = 4.0 mm² minimum;
- high-current sealed X30/X31 service interface;
- return goes to J-P02, not FT550 sensor ground;
- final protection based on measured load and connector/terminal capability.

## 9.2 Direct PMU versus external stage

1. Identify exact pump PN.
2. Measure cold inrush/start current.
3. Measure steady current at representative supply voltage and fuel-system pressure/load.
4. Repeat hot/restart where practical.
5. Measure voltage at pump and feed/return drops.
6. Compare results with O1/O2 PMU capability and thermal/current-limit behaviour.
7. If margin is inadequate, use external relay/solid-state power stage commanded by PMU.
8. Record decision in `Fuel-Pump-Power-Stage-Decision-Register.csv`.

## 9.3 Functional logic

O1 initial strategy: prime 3 s after arming, run during start request and confirmed engine running, kill removes immediately. O2 remains DNP unless required, then staged by validated load/MAP strategy with safe fallback.

**Test point:** Pump output command, measured current, fuel pressure and connector temperature must tell a coherent story. Rising pump current plus falling pressure is not "just a tune issue".

---

# CHAPTER 10 - COOLING, BOOST SOLENOID AND AUXILIARIES

## Objective brief

Cooling and boost control are auxiliary systems electrically, but they protect engine hardware. A fan or charge-pump fault should not corrupt sensor ground or reset the ECU; a boost-solenoid electrical fault must return the turbo system to mechanical minimum boost.

## 10.1 Fan 1 / O3

Current hardware pin 26, 25 A class. B11 wire baseline 2.5 mm² provisional pending measured fan inrush/steady current.

Initial temperature placeholders: 95 C ON, 90 C OFF. These are not final validated engine targets.

If ECT becomes invalid while engine remains armed/running, initial strategy is conservative fan ON after validation delay rather than assuming cold.

## 10.2 Fan 2 / O4 if fitted

Pin 13, 25 A. Initial placeholders 100 C ON / 94 C OFF, 0.5 s start stagger after Fan 1.

## 10.3 Charge-cooler pump / O5 if fitted

Pin 12, 25 A. Initial strategy on while SYSTEM_ARMED and ENGINE_RUNNING, plus SERVICE_MODE for bleed/testing. Optional 30 s post-run placeholder only after validation.

## 10.4 Boost-control supply / O6

Pin 11, 15 A. PMU provides protected supply; FT550 remains boost-control authority.

O6 goes OFF on required CAN/MAP failure, so pneumatic plumbing must produce minimum mechanical boost when de-energised.

---

# CHAPTER 11 - CAN AND SERVICE CONNECTIONS

## Objective brief

CAN is a two-wire digital conversation. Both wires matter as a pair, both ends need termination, and extra branches/terminators can turn a clean conversation into everyone talking through a fan.

## 11.1 Frozen bus

- FT550 CAN A LOW = A15.
- FT550 CAN A HIGH = A16.
- PMU CAN2 LOW = pin 37.
- PMU CAN2 HIGH = pin 24.
- bitrate = 1 Mbps.
- topology = linear FT550 -> X51 short service tap -> PMU16.
- service stub target <= 0.3 m.
- exactly two 120-ohm terminations: FuelTech terminator at FT550 end and PMU CAN2 software termination at PMU end for baseline layout.

## 11.2 Power-off test

With both normal end terminations active, measure approximately 60 ohms between CAN-H and CAN-L. A very different reading requires diagnosis before power-up. Do not add a resistor at X51 to "fix" a reading without understanding the topology.

## 11.3 Powered test

1. FT550 and PMU CAN2 both 1 Mbps.
2. Verify PMU receives only validated FT550 signal definitions.
3. Compare PMU-received RPM/MAP/ECT values with FT550 display/log.
4. Deliberately disconnect CAN during bench/controlled testing and confirm every fallback state.
5. Reconnect and confirm deterministic recovery.

Reference: `FT550-PMU16-CAN-Backbone.md`, `FTCAN20-PMU-Frame-Map.csv`, `PMU-Client-Receive-Configuration.md`.

---

# CHAPTER 12 - TWO-STEP CLUTCH SYSTEM

## Objective brief

The clutch switch tells the PMU when launch logic may be requested. PMU O11 is a +12 V high-side output, while FT550 A21 is a ground-active input. The X70 relay is an electrical translator that keeps those two worlds isolated.

## 12.1 Current physical wiring

`OEM clutch switch -> PMU A6 pin18 -> PMU logic -> O11 pin3 -> X70 12V relay coil`

The X70 relay contact side is isolated:

`approved ground -> X70 COM -> X70 NO -> FT550 A21`

O11 OFF = relay open = A21 open = Two-Step OFF.  
O11 ON = relay closed = A21 grounded = Two-Step request ON.  
Loss of PMU/relay = open = fail OFF.

Use TE 1393292-5 resistor-suppressed relay. Do not add an external flyback diode unless the design is formally revised.

## 12.2 Bench test

1. Measure coil resistance and record ambient temperature.
2. Energise coil from representative 12-14.5 V source.
3. Verify NO contact only closes when energised.
4. Verify A21-side has no electrical path to +12 V.
5. Measure relay coil current.
6. Check contact resistance.
7. Confirm prompt release after command removal.
8. Cycle at least the prototype-validation count specified in X70 freeze.
9. Remove relay and confirm A21 stays open/Two-Step OFF.

## 12.3 Clutch truth table

Before engine start, test clutch released, pulled, transition/debounce and disconnected-fault states using `Two-Step-Truth-Table-Register.csv`. The failed/disconnected state must not silently command Two-Step.

---

# CHAPTER 13 - HARNESS INSTALLATION AND HP6/HP7 ACCEPTANCE

## Objective brief

A harness is not finished when the connectors click. It is finished when routing, terminal retention, continuity, isolation, heat protection and documentation all agree with the build schedule.

## 13.1 Fit the harness

1. Lay loom loosely on the bike using branch IDs.
2. Connect major modules first without forcing branches.
3. Confirm each branch reaches with the intended service loop.
4. Check full steering lock and suspension movement.
5. Add clamps/P-clips from fixed points outward.
6. Apply heat protection only in released zones.
7. Ensure X50/X51 remain accessible and capped.
8. Keep X70 serviceable.

## 13.2 HP6 pre-cover / construction inspection

For a new manufacturer harness, HP6 occurs before hidden splices/construction are covered. Verify 4.0 mm² pump circuits, B15, B39/B40 segregation, connector population, splice construction, sensor-ground segregation, CAN twist, CKP integrity, X70 dry-contact isolation and branch positions.

## 13.3 HP7 final acceptance

Complete 100% point-to-point continuity, isolation, CAN polarity, trigger polarity, injector/coil front-rear mapping, dimensions, terminal retention, pull-test evidence, labels and documentation.

No harness moves to first-power commissioning until `HP7_FINAL_HARNESS_ACCEPTED`.

---

# CHAPTER 14 - COMPLETE PRE-POWER TEST SEQUENCE

## Objective brief

The safest first power-up is the boring one. This chapter proves the loom is electrically sane before expensive electronics are asked to discover a wiring error with their internal smoke.

## 14.1 Battery disconnected

- Inspect every connector lock.
- Verify B+ to power ground has no hard short.
- Verify A21 dry-contact side isolated from +12 V.
- CAN H/L not shorted to B+ or ground.
- FT550 5 V/reference not shorted to B+.
- Sensor ground not intentionally merged with high-current return.
- Confirm expected ground continuity.

## 14.2 Controlled first energisation

With pumps, ignition and auxiliaries disabled and engine not cranking, use current-limited power where practical. Watch current draw, smoke/odour, unexpected relay/load activity, FT550/PMU boot and protection events.

Any unexplained behaviour = power off and diagnose.

---

# PART VII - COMPLETE SCHEMATICS AND HARNESS REFERENCE

# CHAPTER 15 - TEXT SCHEMATICS

## 15.1 Master power

```text
BATTERY +
   |
   +--> MASTER / PRIMARY PROTECTION
          |
          +--> J-P01 POSITIVE DISTRIBUTION
                 |
                 +--> B15 10 mm² --> PMU16 MAIN STUD
                 +--> protected FT550 supply path
                 +--> B39 injector supply
                 +--> B40 SparkPRO/ignition supply
                 +--> external pump power stages if final decision requires

BATTERY - / ENGINE PRIMARY RETURN
   |
   +--> J-P02 HIGH-CURRENT GROUND STAR
          +--> PMU ground pin25
          +--> FT550 primary power ground architecture
          +--> SparkPRO power grounds
          +--> Pump1 4 mm² dedicated return
          +--> Pump2 4 mm² dedicated return
          +--> fan/aux returns as released

FT550 SENSOR GROUND
   +--> precision sensor return splice only
   X   NO pump/fan/coil/starter high-current returns
```

## 15.2 Fuel pumps

```text
DIRECT-PMU option only if verified:
PMU O1 pin38 --> 4.0 mm² --> X30 --> Pump1 +
Pump1 - --> X30 --> 4.0 mm² --> J-P02

PMU O2 pin39 --> 4.0 mm² --> X31 --> Pump2 +
Pump2 - --> X31 --> 4.0 mm² --> J-P02

EXTERNAL-STAGE option if required:
PMU O1/O2 --> low-current command --> approved power stage
J-P01/protected source --> stage --> 4.0 mm² --> pump
pump --> 4.0 mm² --> J-P02
```

## 15.3 Injection

```text
J-P01/EPM --> B39 protected supply --> supply splice --> Front Injector +
                                             \------> Rear Injector +

FT550 A1 --> X62 front --> [direct bypass OR Peak&Hold] --> X63 --> Front Injector command
FT550 A2 --> X62 rear  --> [direct bypass OR Peak&Hold] --> X63 --> Rear Injector command
```

## 15.4 Ignition

```text
FT550 A8 --> SparkPRO pin1 CH1 input
FT550 A9 --> SparkPRO pin3 CH2 input
B40 protected power --> SparkPRO/ignition power as exact hardware requires
SparkPRO pin2 + pin5 --> J-P02 power ground
SparkPRO pin6 CH1 output --> Front coil
SparkPRO pin4 CH2 output --> Rear coil
```

## 15.5 CAN

```text
FuelTech terminator
     |
FT550 CAN A
 A16 H ===================== H pin24 PMU CAN2
 A15 L ===================== L pin37 PMU CAN2
             |
             +-- X51 short diagnostic stub <=300 mm

PMU CAN2 termination = ENABLED at PMU end
No permanent X51 terminator
Target powered-off H-L resistance with both end terminators = approx 60 ohm
```

## 15.6 Two-Step

```text
Clutch switch --> PMU A6 pin18
                     |
                 launch logic
                     |
PMU O11 pin3 --> X70 relay coil +
J-P02/control GND --> X70 relay coil -

APPROVED GROUND --> X70 COM
X70 NO ---------> FT550 A21

NEVER connect +12 V to FT550 A21.
```

## 15.7 Key branch schedule

Use the complete controlling files for every circuit: `Production-Wire-Circuit-Master-Schedule.csv`, `Connector-Cavity-Master-Schedule.csv`, `Splice-Junction-Master-Schedule.csv`, `Protection-Fuse-PMU-Current-Limit-Master-Schedule.csv`, `Master-Wire-and-Connector-Schedule.csv`, `Harness-Branch-Schedule.csv`, `Wire-Size-Schedule.csv`, `B01-B44-Dimensional-Freeze-Worksheet.csv` and `Harness-Physical-Dimension-Capture-Register.csv`.

Key current branch baselines:

- B01 FT550 sensor spine: mixed 0.35 mm².
- B02 CKP: 2 x 0.35 mm² shielded twisted.
- B03 TPS: 3 x 0.35.
- B04 MAP: 3 x 0.35.
- B05 ECT: 2 x 0.35.
- B06 IAT: 2 x 0.35.
- B07 VSS: 3 x 0.35.
- B08 injector control plus B39 supply.
- B09 coil primary driven branch.
- B10/B10R Pump1 feed/return: 4.0 mm² minimum each.
- Pump2 feed/return: 4.0 mm² minimum each.
- B11 fan: 2.5 mm² provisional.
- B12 charge cooler: 2.0 mm² provisional.
- B14 CAN: 2 x 0.35 twisted.
- B15 PMU feed: 10.0 mm² baseline.
- B17 fuel pressure: 3 x 0.35.
- B18 oil pressure: 3 x 0.35.
- B19 post-IC IAT: 2 x 0.35.
- B32 A8/A9 SparkPRO commands: 2 x 0.50.
- B33 SparkPRO grounds/power as released.
- B34 SparkPRO coil outputs: 2 x 1.00.
- B35 A1/A2 injector commands: 2 x 0.50.
- B36 direct-drive bypass: 2 x 0.50, fit only after approval.
- B37/B38 Peak & Hold path only if selected.
- B39 injector +12 V: 1.0 mm² provisional.
- B40 ignition +12 V: 1.5 mm² provisional.
- B41 clutch switch: 2 x 0.35.
- B42 optional clutch position: 3 x 0.35.
- B43 O11 to X70: 0.50.
- B44 X70 to A21: 0.35.

Final production lengths come from the physical freeze, not prototype estimates.

---

# PART VIII - COMMISSIONING: FIRST POWER TO FINAL DYNO

# CHAPTER 16 - FIRST POWER / DEAD ENGINE

## Objective brief

Power the electronics and prove every electrical function while deliberately preventing the engine from starting. This separates wiring faults from combustion/tuning faults.

### FP-0 Installation inspection
Verify routing, clamps, heat clearance, steering/suspension movement, connector locks, J-P01/J-P02, B15 protection, pumps and X70.

### FP-1 Unpowered isolation
Check B+ to ground sanity, A21 isolation, CAN isolation, 5 V/reference isolation and ground architecture.

### FP-2 Controlled first energisation
Engine not cranking, pumps/ignition/aux disabled. Power system under controlled/current-limited conditions where practical. No unexplained current draw, heating, smoke or uncommanded loads.

### FP-3 Power rails
Measure battery/source, J-P01, PMU B15 input, FT550 supply, B39 and B40 when intentionally enabled. Record voltage drop.

### FP-4 Reference rails
Verify FT550 5 V reference and sensor ground before trusting sensors.

### FP-5 Sensor plausibility
TPS closed/sweep, MAP ambient, IAT/ECT ambient plausibility, VSS zero, added sensors plausible.

### FP-6 CAN
Verify 1 Mbps link, no bus-off, X51 service, termination and signal agreement.

### FP-7 PMU outputs
One at a time: Pump1, Pump2, fan, charge-cooler, B39 enable, B40 enable, X70 coil. Record current and fault state.

### FP-8 Two-Step truth table
Clutch -> A6 -> O11 -> X70 -> A21; confirm fail OFF and no +12 V at A21.

### FP-9 Dead-engine crank
Positively inhibit fuel and ignition. Short crank while logging battery min voltage, PMU min voltage, FT550 reset state, RPM, trigger/sync, CAN, B15 drop and sensors. No intentional injection or spark.

### FP-10 Inspection
Inspect B15/J-P01/J-P02, pump connectors, B39/B40, PMU connector, protection and grounds for heat/distress.

Release only when `FIRST_POWER_COMMISSIONING_ACCEPTED`.

---

# CHAPTER 17 - FIRST START

## Objective brief

The first combustion event is an inspection exercise, not a horsepower event. Boost and Two-Step remain disabled. The priority order is oil pressure, fuel pressure, stable sync, valid AFR and no leaks/noise.

## 17.1 Pre-start configuration freeze

Record FT550 calibration filename/revision, injector data/source, base fuel pressure, trigger config, ignition output config, dwell source, cranking fuel, idle target, initial rev limit, wideband config, PMU revision and SparkPRO hardware. Keep boost and Two-Step disabled.

## 17.2 FS-0 walk-around

Inspect fuel, oil/turbo oil, coolant, throttle return, exhaust/turbo clearance, battery/main grounds, pump/injector/ignition connectors, tools/rags and extraction.

## 17.3 FS-1 fuel prime

Key on. Record battery voltage, pump state/current, achieved fuel pressure, pressure stability and leak check. Any leak = stop and depressurise.

## 17.4 FS-2 oil readiness

Complete engine/turbo oil priming per mechanical build procedure. Where the approved procedure supports it, verify oil pressure during no-start crank before combustion.

## 17.5 FS-3 first combustion

Brief first attempt. Immediately observe oil pressure, fuel pressure, RPM, wideband validity, trigger errors, charging voltage, PMU trips, noise, leaks and throttle/idle behaviour. If it does not start promptly, stop and diagnose rather than extended repeated cranking.

## 17.6 First 30 seconds

Keep RPM low. Continuously monitor oil pressure, fuel pressure, AFR validity, RPM, temperature trend, charging voltage, sync, PMU faults and leaks/noise.

## 17.7 Early warm-up and shutdown

Log RPM, pressures, AFR, temperatures, MAP, voltage, PMU faults, trigger errors, pump current and cooling state. Verify fan/cooler operation only within safe temperature. Shut down deliberately and inspect all high-current/heat-sensitive connections.

## 17.8 Save first-start log

Archive before changing the calibration. Review crank voltage, sync, pressures, AFR, sensors, PMU faults, pump behaviour and injector/ignition consistency.

Release: `FIRST_START_COMMISSIONING_ACCEPTED`.

Numeric abort thresholds for oil/fuel pressure, AFR, temperature and RPM must come from the verified installed engine/fuel/turbo configuration, not generic values.

---

# CHAPTER 18 - HEAT CYCLES AND SENSOR CORRELATION

## Objective brief

Now prove that the bike still tells the truth when hot. Many wiring, sensor and trigger faults only emerge with heat soak.

### HC-0 cold soak
Compare IAT/ECT to independent ambient, MAP to barometric reference, TPS closed, battery, 5 V reference and sensor-ground offset.

### HC-1 start stable
Oil/fuel pressure, AFR, sync, charging, MAP/TPS and no leaks.

### HC-2 warm-up correlation
Log RPM, TPS, MAP, AFR, pressures, temperatures, battery, pump currents, B11/B12, PMU faults and trigger errors at regular intervals.

### HC-3 cooling validation
Confirm fan command matches plausible temperature, fan current matches electrical test, temperatures respond and no wire/connector heating develops.

### HC-4 low-load response
Brief no-load/very-low-load RPM changes. Verify TPS/MAP/trigger/fuel/AFR/charging/B39/B40 stability.

### HC-5 heat soak
Record shutdown temperatures, pressure decay, post-shutdown IAT/temperature rise and harness thermal condition.

### HC-6 hot restart
Capture cranking voltage, ECU/PMU reset, start quality, pressures, AFR, sync, pump current.

### HC-7 repeatability
Perform only the heat-cycle count required by the mechanical engine/turbo plan. Look for drift in current, voltage drop, sensor offset, trigger integrity or fuel pressure.

Release: `LOW_LOAD_HEAT_CYCLE_VALIDATED`.

---

# CHAPTER 19 - NO-BOOST AND WASTEGATE BASELINE

## Objective brief

Before electronic boost control does anything clever, prove the motorcycle behaves under light load and that the wastegate plumbing alone limits boost predictably.

1. Disable electronic boost command/O6 as required so the system is in minimum mechanical boost configuration.
2. Perform no-boost/light-load dyno checks using `No-Boost-Light-Load-Commissioning.md` and matrix.
3. Validate fuel pressure, AFR, trigger/sync, oil pressure, injector duty, voltage and temperatures.
4. Verify wastegate reference plumbing.
5. Progress only to the approved base-boost verification envelope.
6. If boost creeps beyond the approved ceiling, abort and correct mechanical/pneumatic causes rather than masking it with more fuel/timing changes.

Reference: `Wastegate-Minimum-Boost-Baseline.md`, `Open-Loop-Boost-Control-Commissioning.md`, `Closed-Loop-Boost-Control-Commissioning.md`.

---

# CHAPTER 20 - PROGRESSIVE DYNO LOAD AND BOOST ENABLEMENT

## Objective brief

Load and boost are introduced like a staircase, not a cliff. Every run must prove fuel delivery, oiling, lambda, ignition, temperature, electrical stability and turbo control before the next stage is unlocked.

### DL-0 static dyno setup
Verify restraints, dyno RPM/speed, cooling airflow, extraction, pressure channels, lambda, MAP, TPS, temperatures, PMU status, kill and logging.

### DL-1 minimum-load sweep
Boost control disabled/minimum. Increase load modestly and verify trigger, pressures, AFR, MAP, injector duty, ignition, voltage, pump current, B39/B40 and PMU state.

### DL-2 base boost
Validate mechanical wastegate/base-boost, no uncontrolled creep, correct fuel-pressure relationship and stable AFR/trigger.

### DL-3 fuel differential
For a manifold-referenced fuel system, track rail pressure relative to MAP. A falling differential, unexplained pump-current change or injector saturation blocks escalation.

### DL-4 progressive boost stages
Before each run pre-enter boost ceiling, RPM ceiling, duration/load path, AFR/lambda envelope, fuel differential minimum, oil requirement, temperature maximum, ignition strategy, injector-duty ceiling, turbo-speed ceiling if measured and abort criteria. A pass allows consideration of the next stage; it does not auto-unlock it.

### DL-5 ignition review
Review commanded timing together with load/MAP, AFR, temperatures and combustion evidence. Absence of audible knock is not proof of safe timing.

### DL-6 turbo speed if fitted
Validate sensor scaling at low load before using it for protection. Maximum speed comes from the exact turbo manufacturer/compressor assembly data.

### DL-7 high-load electrical
Capture B15/PMU voltage, pump currents, B39/B40, charging, PMU faults/current limiting and connector temperatures between runs.

### DL-8 recovery/repeatability
Return to defined thermal condition before escalation. Repeat accepted stages where necessary.

### DL-9 controlled boost release
Record currently released boost ceiling, RPM ceiling, fuel, calibration revision, environment/dyno context and remaining restrictions. Two-Step stays disabled until its separate gate.

Release: `DYNO_LOAD_COMMISSIONING_ACCEPTED` and `CONTROLLED_BOOST_OPERATION_RELEASED`.

---

# CHAPTER 21 - FINAL FULL-POWER DYNO VALIDATION

## Objective brief

The final dyno pull is not the moment to try three new ideas at once. It is a repeatability and margin test of an already developed configuration.

## 21.1 FP-001 pre-pull release

For every full-load pull confirm current FTManager revision, PMU revision, boost-control revision, injector mode, fuel strategy, both lambda channels if fitted, fuel/oil pressure, ECT/IAT starting condition, no PMU/CAN faults, kill function, restraint/cooling/extraction and previous-log review.

## 21.2 FP-002 first full-load pull

Use already approved boost target, RPM ceiling and load path. Do not simultaneously increase boost, ignition and rev limit.

Log continuously:

- RPM and TPS;
- boost target/actual;
- front/rear lambda;
- injector duty;
- fuel and oil pressure;
- ECT/IAT;
- battery voltage;
- ignition timing;
- PMU O1/O2/O3/O4/O5/O6 current/state where available;
- CAN health;
- boost correction/feed-forward;
- sync/misfire/fault status.

## 21.3 Abort immediately for

Fuel pressure decay, oil pressure loss/invalidity, unsafe lambda, material cylinder-to-cylinder divergence, injector duty at released limit, uncontrolled boost, sync/misfire/RPM dropout, severe combustion concern, temperatures above released limit, critical PMU current-limit/retry event, CAN loss that removes required protection, mechanical noise or operator uncertainty about a critical channel.

## 21.4 Log review before another pull

Review cylinder lambda balance, injector margin, fuel pressure vs MAP, oil pressure vs RPM/temp, boost target/actual, closed-loop correction, timing, thermal rise, PMU current/faults, CAN and sync/misfire evidence.

Any unexplained anomaly reopens its lower commissioning gate.

## 21.5 Repeatability pulls

Repeat only from a defined thermal state. Final acceptance requires repeatable boost, lambda, pressure, injector duty, timing, torque/power curve shape, thermal rise and PMU/CAN behaviour.

## 21.6 Final capacity and hardware review

At highest authorised load, freeze injector duty, fuel-pressure margin, pump behaviour/staging, turbo-speed margin if measured and thermal condition. If hardware operates at the edge of capacity, stop progression and increase hardware capacity rather than burying the shortage in calibration.

## 21.7 Final calibration freeze

Save immutable FTManager calibration revision, PMU project, boost-control configuration, all logs and dyno graphs. Record fuel type, released boost/RPM, injector configuration, protection thresholds, hardware revision and sensor calibration sources.

Create the final dyno report with power/torque, boost, cylinder lambda, injector/fuel margin, oil pressure, thermal data, timing summary, PMU/CAN faults and operating restrictions.

Promotion target: `DYNO_CALIBRATION_FROZEN_READY_FOR_VEHICLE_VALIDATION_PREP`.

---

# REPOSITORY REFERENCE POLICY

This manual must be read with `docs/Manual/Repository-MD-CSV-Reference-Matrix.csv`. That matrix inventories the repository `.md` and `.csv` engineering assets by discipline and identifies their role as controlling, supporting, verification, commissioning, historical/superseded or handover material.

When this manual and a later explicit engineering-change or approved release file conflict, the later controlled release wins. Never resolve a conflict by choosing whichever value is more convenient.

# END OF CONTROLLED WORKSHOP MANUAL
