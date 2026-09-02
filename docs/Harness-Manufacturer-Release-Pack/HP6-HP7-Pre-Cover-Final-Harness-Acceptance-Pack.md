# HP-6 Pre-Cover Inspection + HP-7 Final Harness Acceptance Pack

## Purpose

Define the two manufacturing acceptance gates immediately after a Rev 1 harness is built under `MANUFACTURING_RELEASED_REV1`.

- **HP-6** inspects construction while critical details are still visible, before final sleeving, boots, moulding or other covering hides them.
- **HP-7** verifies the completed harness after covering, electrical test and dimensional inspection, before it is released for vehicle installation and first-power qualification.

Neither gate authorises engine start by itself.

## Entry condition

HP-6 may begin only when:

- `MANUFACTURING_RELEASED_REV1` has been issued;
- the harness serial number is assigned;
- the controlled build traveller is active;
- wire, cavity, splice, protection, dimension and identification schedules match the released revision.

## HP-6 Pre-Cover Inspection

### 1. Configuration identity

Verify:

- harness serial;
- configuration revision;
- formboard revision;
- build traveller revision;
- production schedule revisions;
- approved deviations applicable to this serial.

### 2. Wire and circuit construction

Inspect visible construction against the Production Wire / Circuit Master Schedule.

Confirm:

- correct conductor sizes;
- correct circuit identification;
- correct branch assignment;
- 4.0 mm² minimum Pump 1 and Pump 2 feeds;
- 4.0 mm² dedicated Pump 1 and Pump 2 returns;
- B15 released conductor size;
- B39 and B40 remain segregated as released;
- no undocumented wire substitution.

### 3. Connector/cavity population

Before boots or covering obscure wire entry, verify:

- correct housing;
- correct cavity population;
- correct terminal family;
- correct seal;
- secondary lock installed;
- unused sealed cavities plugged where required;
- wire-to-terminal size compatibility;
- no terminal push-back;
- no damaged seals.

### 4. Splices and junctions

Inspect every production splice/junction that will become hidden.

Confirm:

- splice ID;
- conductor count/sizes;
- approved splice method;
- correct physical location;
- sealing/insulation method;
- no precision sensor/reference splice merged into high-current return;
- J-P01/J-P02 construction matches released architecture;
- no undocumented splice exists.

### 5. CAN

Verify:

- CAN-H/CAN-L pair identity;
- twist maintained through trunk and branches;
- untwist at terminations minimized;
- X51 is a short service stub;
- no undocumented star splice;
- no hidden termination resistor.

### 6. CKP/CAM trigger integrity

Verify:

- released polarity preserved;
- released shielding/twist method preserved;
- routing separation from ignition/high-current paths;
- no unnecessary trigger splice;
- any approved repair-pigtail transition is documented.

### 7. X70 Two-Step

Verify:

- relay/socket matches released configuration;
- PMU O11 side is correct;
- FT550 A21 contact side is dry-contact only;
- no +12 V path exists to A21 contact side;
- coil suppression, if fitted, matches released polarity/configuration.

### 8. Routing / breakouts / strain relief

Verify:

- breakout positions against formboard;
- branch lengths before final closure;
- service-loop allowances;
- bend radii;
- connector strain relief;
- no splice in a dynamic flex zone unless explicitly approved;
- heat-protection locations are prepared correctly.

### 9. Pre-cover evidence

Required photographs should include:

- full harness on formboard;
- every splice before concealment;
- J-P01 and J-P02;
- B15 path;
- Pump 1/2 high-current paths;
- B39/B40 distribution;
- CAN construction;
- CKP/CAM construction;
- X70;
- representative connector rear/wire-entry views;
- all approved deviations.

### HP-6 result

PASS state:

`HP6_PRE_COVER_ACCEPTED`

FAIL/HOLD state:

`HP6_HOLD_CORRECTION_REQUIRED`

Final covering shall not proceed while an HP-6 blocking defect remains open.

---

# HP-7 Final Harness Acceptance

HP-7 begins after HP-6 PASS, final covering/booting and manufacturer electrical testing.

### 1. Final visual inspection

Verify:

- covering complete and undamaged;
- boots correctly seated;
- labels readable and correctly positioned;
- no exposed conductor;
- no sharp transition likely to chafe;
- branch exits and strain relief acceptable;
- connector seals/locks intact;
- heat protection matches released schedule.

### 2. 100% point-to-point continuity

Test every production circuit against the released wire/cavity schedule.

Required result:

- correct source-to-destination continuity;
- no swapped front/rear injector or coil circuits;
- correct CAN-H/CAN-L polarity;
- correct CKP/CAM polarity;
- correct X70 contact path.

### 3. Isolation / short-circuit test

With sensitive electronics disconnected as required, verify no unintended continuity:

- between unrelated circuits;
- between +12 V and ground;
- between +12 V and sensor/reference circuits;
- between FT550 A21 dry-contact side and +12 V;
- between CAN conductors and power/ground;
- between sensor ground and prohibited high-current ground paths.

### 4. CAN termination check

Verify the harness itself contains no unapproved termination and that the measured system configuration is consistent with the released topology when connected in the approved test arrangement.

### 5. Dimensional inspection

Check controlled branch dimensions against released tolerance.

Record at minimum:

- B15;
- FT550;
- PMU16;
- SparkPRO;
- both pump feeds/returns;
- injector/coil branches;
- CKP/CAM;
- B11/B12 where applicable;
- X50/X51/X70;
- VSS/rear branch;
- steering/front branch where applicable.

### 6. Mechanical quality

Verify:

- connector retention;
- terminal retention sampling/inspection;
- accepted pull-test evidence;
- no excessive harness stiffness at moving interfaces;
- no exposed splice or unprotected junction;
- mounting/clamp features installed where harness supplied.

### 7. Protection configuration

Verify installed fuses/relays/protection hardware supplied with the harness match the released Protection / Fuse / PMU Current-Limit Master Schedule.

Electronic PMU current limits are configuration-controlled separately but their intended branch/channel mapping must agree with the harness.

### 8. Final documentation

The manufacturer shall return:

- completed build traveller;
- HP-6 register;
- HP-7 register;
- electrical test report;
- dimensional report;
- pull-test/crimp evidence;
- photo evidence;
- deviations/RFIs linked to final disposition;
- as-built BOM/revision;
- harness serial/build record.

### HP-7 result

PASS state:

`HP7_FINAL_HARNESS_ACCEPTED`

This authorises release of the harness for controlled vehicle installation and subsequent first-power qualification.

It does not automatically issue:

`FIRST_POWER_AUTHORISED`

or

`FIRST_START_AUTHORISED`

Those remain separate commissioning gates.

## Nonconformance rule

Any HP-6 or HP-7 failure shall be recorded against the harness serial. Rework must identify:

- defect;
- root cause where known;
- rework method;
- affected circuits;
- documents/deviation reference;
- required retest;
- retest evidence;
- final disposition.

A repaired harness cannot be accepted merely because the visible defect has disappeared. The applicable electrical/mechanical tests must be repeated.

## Release ladder

`MANUFACTURING_RELEASED_REV1`

→ build traveller

→ `HP6_PRE_COVER_ACCEPTED`

→ final covering + manufacturer electrical test

→ `HP7_FINAL_HARNESS_ACCEPTED`

→ controlled vehicle installation

→ first-power gate

→ first-start gate

→ Golden Harness qualification.
