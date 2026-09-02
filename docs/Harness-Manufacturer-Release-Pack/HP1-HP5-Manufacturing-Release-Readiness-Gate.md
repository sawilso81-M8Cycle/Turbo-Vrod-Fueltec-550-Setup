# HP-1 through HP-5 Manufacturing Release Readiness Gate

## Purpose

Provide the final consolidated engineering gate between the current RFQ/DFM state and authorisation to manufacture the first electrically functional Rev 1 Turbo V-Rod harness.

This gate does not replace the detailed subsystem freezes, test packs or manufacturer-return documents. It confirms that their required outputs have been completed and accepted.

## Current state

`HP1_HP5_RELEASE_GATE_RELEASED / MANUFACTURING_RELEASED_REV1_NOT_YET_ISSUED`

## Release rule

`MANUFACTURING_RELEASED_REV1` may be issued only when HP-1 through HP-5 are all PASS and no STOP condition remains open.

A conditional or assumed PASS is not a PASS.

---

# HP-1 – Manufacturer DFM Return Accepted

Required:

- Rev 2 manufacturer package issued under controlled checksum/transmittal;
- completed Manufacturer DFM Response Register returned;
- wire family/specification accepted;
- splice method accepted;
- sleeving/heat-protection method accepted;
- strain-relief/booting method accepted;
- labelling method accepted;
- continuity/isolation test capability accepted;
- pull-test capability accepted;
- formboard/Golden Harness process accepted;
- revision/serial traceability process accepted;
- commercial/NRE/prototype quotation reviewed;
- all blocking manufacturer RFIs dispositioned;
- all proposed deviations either APPROVED or REJECTED/CLOSED.

Output:

`HP1_DFM_ACCEPTED`

---

# HP-2 – Connector & Procurement Release

Required:

- FT550 connector-kit/terminal/tooling method accepted;
- PMU16 exact hardware revision identified;
- every used PMU cavity mapped to exact compatible terminal and wire range;
- fuel-pump HDSCS/MCP service-interface hardware accepted;
- X50 exact housing/contact/seal/cavity configuration accepted;
- X51 exact DTM housing/contact/cap configuration accepted;
- X70 relay socket/carrier and terminals accepted;
- OEM X10-X23 interfaces resolved to exact connector or approved repair pigtail;
- every selected terminal accepts the released conductor size;
- seals/secondary locks/cavity plugs identified;
- procurement availability/MOQ/lead-time risks accepted.

Output:

`HP2_CONNECTOR_PROCUREMENT_ACCEPTED`

---

# HP-3 – Electrical Blockers Closed

Required as applicable:

- Pump 1 and Pump 2 identity verified;
- pump cold/hot inrush and steady-current evidence accepted;
- pump direct-PMU vs external-stage decision frozen;
- 4.0 mm² minimum pump feeds retained;
- 4.0 mm² dedicated pump returns retained;
- injector identity and electrical class verified;
- injector direct-drive vs Peak & Hold decision frozen;
- SparkPRO/coil identity and electrical evidence accepted;
- dwell baseline either released or explicitly controlled for later calibration without compromising harness sizing;
- B11 fan load and switching/protection decision frozen;
- B12 marked DNP or its load/switching/protection decision frozen;
- B15 load cases and primary protection accepted;
- B39 final conductor/protection accepted;
- B40 final conductor/protection accepted;
- CAN termination configuration verified;
- X70 A21 dry-contact truth table verified;
- no unresolved electrical architecture conflict remains.

Output:

`HP3_ELECTRICAL_BLOCKERS_CLOSED`

---

# HP-4 – Dimensional Release

Required:

- primary physical datums defined;
- FT550/PMU16/SparkPRO positions accepted;
- J-P01/J-P02 positions accepted;
- pump branch routes measured;
- injector/coil/sensor branches measured;
- B11/B12 branches measured where applicable;
- X50/X51/X70 positions measured;
- steering centre/full-left/full-right movement accepted;
- rear/VSS movement accepted;
- turbo/exhaust heat zones documented;
- service-loop allowances explicitly recorded;
- manufacturing tolerances assigned;
- unresolved physical clashes closed;
- branch-dimension schedule released.

A manufacturer measurement/mock-up exception may satisfy HP-4 only if formally approved and the resulting dimensions are controlled before electrical functional completion.

Output:

`HP4_DIMENSIONAL_RELEASED`

---

# HP-5 – Crimp / Production Definition Released

Required:

- final circuit/wire schedule released;
- final connector/cavity schedule released;
- final splice schedule released;
- final branch-dimension schedule released;
- final protection schedule released;
- final connector/terminal/seal schedule released;
- crimp tooling identified;
- conductor/terminal combinations within approved ranges;
- pull-test/sampling plan accepted;
- CAN twist/shield instructions frozen;
- CKP/CAM trigger wiring instructions frozen;
- heat-protection/sleeving schedule frozen;
- labels/identification schedule frozen;
- pre-cover inspection requirements included in build traveller;
- manufacturer acknowledges HP-6 and HP-7 remain post-manufacture acceptance gates.

Output:

`HP5_CRIMP_RELEASED`

---

# STOP conditions

The release shall remain blocked if any of the following exists:

- proposed pump conductor below 4.0 mm² feed or dedicated return;
- +12 V path onto the FT550 A21 dry-contact side;
- hidden or unapproved CAN termination;
- sensor/reference ground merged into uncontrolled high-current return;
- terminal outside its approved conductor range;
- unverified look-alike OEM connector used as production baseline;
- unresolved PMU cavity ambiguity;
- protection value exceeds proven conductor/terminal/connector capability;
- unresolved abnormal heating or voltage drop;
- unresolved architecture-changing RFI/deviation;
- missing branch dimension that cannot be safely closed by an approved measurement-build process;
- document revisions conflict without disposition.

---

# Final release action

When HP-1 through HP-5 are PASS:

1. complete `HP1-HP5-Manufacturing-Release-Readiness-Register.csv`;
2. complete `Manufacturing-Release-Authorisation-Rev1-TEMPLATE.md` with exact controlled revisions;
3. change release state to `MANUFACTURING_RELEASED_REV1`;
4. issue a new controlled manufacturer ZIP containing the manufacturing-release configuration;
5. record ZIP SHA-256 and transmittal;
6. manufacturer may then begin the first electrically functional Rev 1 harness;
7. HP-6 pre-cover inspection and HP-7 final harness acceptance remain mandatory.

## Important distinction

`MANUFACTURING_RELEASED_REV1` authorises manufacture of the prototype configuration. It does **not** mean:

- first power is automatically authorised;
- first engine start is automatically authorised;
- the prototype is the Golden Harness;
- repeat production is authorised.

Those states remain separately gated.
