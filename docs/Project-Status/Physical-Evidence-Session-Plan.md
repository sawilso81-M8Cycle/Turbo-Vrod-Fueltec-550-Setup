# Physical Evidence Session Plan

## Objective

Close the highest-value P0/P1 build blockers in one structured motorcycle inspection session before further manufacturing release work.

## Bring to the session

- motorcycle in intended component-layout state;
- FT550, PMU16, SparkPRO, X70 and selected pumps/injectors/coils where available;
- flexible tape measure and steel rule;
- vernier caliper;
- label maker / temporary numbered tags;
- camera/phone;
- DMM;
- current clamp suitable for later powered tests;
- connector terminal extraction/inspection tools where appropriate;
- notebook or direct access to repository worksheets.

## Session A: component location freeze

Photograph and identify final/proposed locations for:

- FT550;
- PMU16;
- SparkPRO;
- X70;
- Pump 1 / Pump 2;
- radiator fan interface;
- charge-cooler pump if fitted;
- wideband/controller;
- MAP/pressure sensors;
- X50 engineering connector;
- X51 CAN/service connector;
- primary power and ground junctions.

Record mounting orientation, connector exit direction, available bend radius, heat exposure and service access.

## Session B: harness dimensions

Use the controlled B01-B44 worksheet.

For each branch:

1. identify start and end datum;
2. route a flexible tape/string along the intended harness path;
3. account for actual bends rather than straight-line distance;
4. verify steering/suspension/engine movement where relevant;
5. record required service loop separately;
6. record heat-protection zone;
7. photograph the route with branch ID visible;
8. record measured route length and proposed production cut length.

Do not convert approximate historical lengths directly into production lengths without this step.

## Session C: connector evidence

For every unresolved connector capture:

- component name;
- connector ID;
- overall connector photo;
- mating-face photo;
- wire-entry photo;
- manufacturer markings;
- cavity count;
- keying;
- cavity numbering if visible;
- existing wire colours/sizes;
- seal style;
- terminal dimensions/markings where safely accessible.

Do not infer cavity numbering from a rear-view photo when the production schedule is defined from mating-face orientation.

## Session D: exact hardware capture

Record manufacturer and PN for:

- Pump 1;
- Pump 2;
- injectors;
- ignition coils;
- SparkPRO;
- boost-control solenoid;
- wastegate;
- pressure sensors;
- wideband controller/sensor;
- clutch switch/sensor;
- X70 relay/socket.

Photograph labels/markings.

## Session E: ground and power physical evidence

Identify and photograph:

- battery positive distribution;
- battery negative;
- engine ground;
- chassis ground if used;
- FT550 grounds;
- PMU grounds;
- SparkPRO ground;
- high-current pump returns;
- sensor-ground architecture boundaries.

Record proposed ring terminal stud sizes only after physical measurement. Do not guess fastener size.

## Session F: CAN/service physical topology

Record:

- FT550 CAN location;
- PMU CAN location;
- X51 location;
- any additional CAN node;
- physical termination points;
- approximate bus lengths;
- stub lengths;
- service access/cap arrangement.

## Session closeout

After the session:

1. populate the physical evidence registers;
2. attach/reference photographs consistently;
3. resolve connector procurement PNs;
4. update B01-B44 production dimensions;
5. update the Production Wire Circuit Master Schedule;
6. update Connector Cavity Master Schedule;
7. update Splice/Junction schedule if physical routing changes it;
8. update protection schedule only after powered load testing;
9. review the Physical Build Readiness Punchlist;
10. issue `PHYSICAL_BUILD_INPUTS_VERIFIED` only when all P0 evidence is actually closed.

## Powered load session remains separate

Do not combine the unpowered measurement/identification session with ad-hoc powered current testing unless the vehicle electrical state is specifically prepared for the applicable commissioning procedure.

The subsequent powered campaign should measure pump, fan, injector/ignition supply and primary power behaviour using the existing Electrical Test Campaign and component-specific verification packs.
