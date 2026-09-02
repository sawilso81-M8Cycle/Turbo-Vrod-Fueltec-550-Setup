# Splice / Junction Master Schedule – Rev 1

## Purpose

Define every intentional electrical join point in the Rev 1 Turbo V-Rod harness so the loom builder has one controlled reference for high-current distribution, precision references, signal fan-out, branch breakouts and serviceable junctions.

This schedule complements the Production Wire / Circuit Master Schedule and Connector / Cavity Master Schedule. No undocumented splice is permitted in production.

## Junction classes

### J-P01 – Primary positive distribution

Engine/vehicle primary positive junction. Carries protected battery-derived feeds including B15 and other released positive branches.

Rules:

- hardware current rating must exceed the released simultaneous load;
- every outgoing branch retains its own required downstream protection where applicable;
- no precision sensor reference or sensor ground may use J-P01;
- branch ring/terminal stack-up, nut/washer hardware and torque requirement shall be frozen in the production pack;
- protective booting/insulation and service access required.

### J-P02 – High-current ground star

Primary high-current return junction.

Typical returns include:

- fuel-pump dedicated returns;
- fan/pump high-current returns;
- SparkPRO/ignition power ground where the released architecture requires it;
- other high-current auxiliary returns.

Rules:

- do not merge FT550 precision sensor ground/reference returns into J-P02 unless an explicit released architecture says so;
- cable/terminal stack-up must support the released current;
- battery negative / engine / chassis bonding relationships must remain documented.

### S-SENS – Precision sensor/reference splices

Low-current precision splice class for 5 V reference or sensor-ground fan-out only where the released FT550 architecture requires a shared branch.

Rules:

- do not combine 5 V reference and sensor ground in one splice;
- keep physically separate from high-current splice clusters;
- splice method must be suitable for low-level sensor circuits;
- use controlled circuit IDs and conductor sizes;
- maintain shield/drain strategy for any nearby shielded circuits.

### S-CAN

CAN joins are discouraged. The FT550↔PMU16 network remains a linear backbone with X51 as a short service stub.

Rules:

- no undocumented CAN star splice;
- no hidden termination resistor;
- if a documented branch splice is unavoidable, preserve twist as close as practical and record exact branch length.

### S-TRG

CKP/CAM trigger circuits should not be spliced unless required by an approved repair-pigtail/service-break strategy.

Rules:

- polarity must be maintained;
- shielding/twist must be preserved;
- no shared splice with unrelated sensor circuits.

## Manufacturing method

Preferred splice methods shall be manufacturer-DFM approved and may include sealed open-barrel crimp splice, ultrasonic weld, or other repeatable automotive/motorsport method suitable for the conductor sizes and environment.

A solder-only inline splice is not the default production method unless explicitly approved for a specific repair/application.

Every production splice must define:

- splice ID;
- electrical function;
- input circuit(s);
- output circuit(s);
- conductor size/count;
- method/tooling;
- seal/insulation method;
- physical location or datum;
- inspection/pull-test requirement where applicable.

## Physical-location control

Splices shall not be placed:

- directly at a connector backshell where they prevent strain relief;
- inside high-flex steering or suspension movement zones;
- against turbo/exhaust hot surfaces;
- where bodywork crushes the splice;
- in locations that trap water without sealing;
- clustered in a way that produces a large rigid loom lump unless packaging has been verified.

Precision sensor splices shall be kept away from SparkPRO, coil primary wiring, starter current paths and fuel-pump high-current branches where practical.

## Breakout distinction

A harness branch breakout is not automatically an electrical splice. If conductors merely separate into different branches without joining electrically, record the breakout in the branch/formboard schedule rather than inventing a splice ID.

## Release state

Current:

`SPLICE_JUNCTION_MASTER_SCHEDULE_WORKING_BASELINE`

Final HP-5 state:

`SPLICE_JUNCTION_MASTER_SCHEDULE_HP5_RELEASED`

Only after every used splice/junction row has exact conductor count, method, location and manufacturing disposition.
