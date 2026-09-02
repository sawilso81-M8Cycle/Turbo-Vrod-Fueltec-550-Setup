# Physical Measurement & Evidence Capture Master Pack

## Purpose

Close the remaining motorcycle-side evidence gates in one controlled workshop campaign. This pack captures component identity, OEM connector evidence, branch dimensions, routing constraints, thermal zones and the physical information required for manufacturer DFM and Rev 1 harness release.

This is a measurement/evidence activity. It does not authorise first power or engine operation.

## Session objectives

A successful session should leave engineering with enough evidence to:

1. identify every retained X10-X23 device and mating connector strategy;
2. freeze the physical positions of FT550, PMU16, SparkPRO, J-P01, J-P02, X50, X51 and X70;
3. replace approximate harness lengths with measured routing dimensions;
4. document steering/suspension/service-loop requirements;
5. identify turbo/exhaust thermal zones and protection requirements;
6. identify actual fuel pumps, injectors, coils, fan and charge-cooler pump if fitted;
7. prepare the separate electrical verification campaigns without guessing component identity.

## Required equipment

Recommended:

- digital caliper;
- 3-5 m flexible tape measure;
- flexible wire/string for routed-length measurement;
- masking tape and removable branch labels;
- paint marker or numbered tags;
- phone/camera with macro capability;
- ruler/scale for connector photographs;
- multimeter for unpowered continuity only;
- inspection light;
- mirror/borescope where useful;
- notebook/tablet with the capture registers;
- cable ties or temporary hook-and-loop straps for mock routing.

Do not probe powered unknown cavities during this campaign.

## Measurement datum convention

Use fixed physical datums rather than vague descriptions.

Recommended primary datums:

- D0 battery positive/J-P01 centre;
- D1 battery negative/J-P02 centre;
- D2 PMU16 connector datum;
- D3 FT550 connector datum;
- D4 SparkPRO connector datum;
- D5 steering-head centreline reference;
- D6 engine front/head reference;
- D7 engine rear/head reference;
- D8 fuel-tank/pump harness exit;
- D9 radiator/fan connector location;
- D10 rear-frame/VSS route datum.

Record actual chosen datum descriptions and photographs before taking dimensions.

## Length measurement rule

Harness lengths are routed centreline lengths, not straight-line distances through space.

For every branch:

1. temporarily route string/wire along the intended harness path;
2. respect clamps, bends, heat clearances and moving joints;
3. mark breakout and connector datum points;
4. remove and measure the routed string;
5. separately record service-loop allowance;
6. record desired manufacturing tolerance;
7. photograph the installed measurement route.

Do not hide service allowance inside an unexplained oversized dimension.

## Device identity capture

Capture the following for each applicable device:

- device name;
- X-number/circuit group;
- manufacturer;
- exact PN;
- all markings;
- connector cavity count;
- native pigtail wire colours;
- approximate native wire size;
- mounting position;
- photograph references.

Priority devices:

- Pump 1;
- Pump 2;
- front injector;
- rear injector;
- front coil;
- rear coil;
- radiator fan;
- charge-cooler pump if fitted;
- CKP;
- CAM if fitted/used;
- TPS;
- MAP;
- engine temperature;
- IAT;
- VSS;
- any other retained OEM X10-X23 device.

## OEM connector photo standard

For each X10-X23 interface capture at minimum:

1. device overview;
2. mating face straight-on;
3. wire-entry face straight-on;
4. latch/keying side;
5. moulded markings close-up;
6. cavity/wire colours;
7. mating harness connector/pigtail where available;
8. one image with ruler/caliper scale.

Filename pattern:

`X##_DEVICE_01_overview.jpg`

`X##_DEVICE_02_mating-face.jpg`

`X##_DEVICE_03_wire-entry.jpg`

Continue sequentially.

## High-current physical capture

### Fuel pumps

Record:

- pump PN/brand;
- pump connector type;
- native terminal size if visible;
- pump branch route;
- route length from released power-stage/PMU location;
- dedicated return route to J-P02;
- service-connector preferred location;
- available space for HDSCS/MCP interface;
- nearby heat/movement/water exposure.

The 4.0 mm² minimum feed and dedicated 4.0 mm² return rule remains locked.

### B15 / J-P01 / J-P02

Record:

- battery terminal positions;
- J-P01/J-P02 mounting position;
- available stud/terminal clearance;
- B15 routed length;
- bend radius/strain-relief constraints;
- nearby heat and moving parts;
- service access.

## ECU/PMU/SparkPRO capture

For each module record:

- final intended mounting location;
- connector orientation;
- available connector removal space;
- harness exit direction;
- distance to primary trunk;
- nearby ignition/high-current/heat sources;
- mounting photographs with scale.

## Dynamic movement checks

### Steering

Mock-route affected branches and capture:

- centre;
- full left lock;
- full right lock;
- minimum slack at each state;
- pinch/rub locations;
- preferred clamp points.

### Rear/suspension

For VSS/rear branches record expected movement envelope and ensure the route cannot tension, pinch or touch rotating/hot components.

## Thermal-zone capture

Identify every harness section near:

- turbocharger;
- turbine/downpipe;
- exhaust headers;
- radiator/fan hot-air discharge;
- engine head/cylinder hot zones;
- oil/fuel lines where separation matters.

Record nearest practical clearance and whether sleeve, reflective barrier, boot or reroute is required.

Do not convert a poor route into an acceptable route merely by adding heat sleeve if a safer route exists.

## X50 / X51 / X70 physical placement

Record preferred location and service access for:

- X50 engineering/service connector;
- X51 CAN service connector;
- X70 Two-Step relay/socket.

Check that X70 remains away from severe heat/water exposure and that X50/X51 can be reached without major vehicle disassembly where practical.

## Evidence quality gate

A measurement row is accepted only when:

- the datum is defined;
- the measurement method is clear;
- the value is recorded in mm;
- a photograph supports the route/location where practical;
- service allowance is separately identified;
- no unresolved interference is visible.

A connector-identification row is accepted only when the image set is sufficient to distinguish keying, cavity count and markings.

## Workshop exit criteria

Before ending the session verify:

- all priority devices have identity photos;
- every used X10-X23 interface has a photo set or a documented access blocker;
- all primary module/junction locations are frozen or flagged;
- every major branch has a routed measurement;
- steering movement is captured;
- rear movement route is captured;
- heat zones are documented;
- X50/X51/X70 positions are recorded;
- missing evidence is listed explicitly rather than remembered informally.

## Release state

Current state:

`PHYSICAL_MEASUREMENT_EVIDENCE_CAPTURE_PACK_RELEASED`

After completion and engineering review:

`BIKE_SIDE_PHYSICAL_EVIDENCE_CAPTURED`

This state contributes to HP-2 connector procurement acceptance and HP-4 dimensional release, but does not itself authorise manufacture or first power.
