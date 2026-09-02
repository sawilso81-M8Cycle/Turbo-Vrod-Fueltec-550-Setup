# Harness Label / Wire Identification / Build Traveller Master Pack

## Purpose

Translate the engineering release set into repeatable shop-floor manufacturing instructions for every harness serial.

This pack ties together the Production Wire Schedule, Connector/Cavity Schedule, Splice/Junction Schedule, Protection Schedule, dimensional release, crimp/tooling requirements, pre-cover inspection and final acceptance records.

## Core production rule

A harness is not considered built to configuration merely because the electrical functions work. The builder must also reproduce:

- conductor size/specification;
- circuit identity;
- connector/cavity assignment;
- splice/junction method;
- branch dimensions;
- protection implementation;
- twist/shielding requirements;
- heat protection;
- labels;
- build/test evidence;
- serial traceability.

## Harness serial identification

Every harness build receives a unique serial before wire cutting begins.

Recommended format:

`TVR-FT550-HARNESS-R1-####`

The serial follows the harness through cutting, crimping, assembly, test, fitment, repair and Golden Harness qualification.

## Harness main label

The completed harness shall carry a durable identification label containing at minimum:

- project: Turbo V-Rod FT550;
- harness serial;
- configuration revision;
- Golden Harness/formboard revision where applicable;
- manufacturer ID;
- build date.

Preferred format example:

`TVR-FT550 / R1 / SN0001 / GH-A / 2026-09`

Label material and print method remain manufacturer DFM-controlled but must be suitable for automotive heat, oil and moisture exposure.

## Connector labels

Every major serviceable connector shall be identified with its controlled designator where practical.

Examples:

- X10 CKP;
- X13 MAP;
- X19 Front Injector;
- X20 Rear Injector;
- X21 Front Coil;
- X22 Rear Coil;
- X30 Pump 1;
- X31 Pump 2;
- X50 Engineering/Service;
- X51 CAN Service;
- X62/X63 Injector Driver Interface;
- X70 Two-Step Relay.

Labels must not obscure locks, seals, latch movement or connector markings needed for service.

## Wire identification

The preferred production method is one of:

1. printed wire ID repeated along the conductor;
2. durable heat-shrink ID at both conductor ends;
3. controlled colour/stripe system plus endpoint labels.

Every conductor must remain traceable to the Production Wire / Circuit Master Schedule.

Minimum endpoint marking should include the circuit ID where packaging allows.

## Circuit-ID control

No circuit ID may be reused for a different function within the same configuration revision.

Unused/spare wires shall be explicitly marked `SPARE` or DNP in the controlled schedule. They are not to be silently reassigned on the shop floor.

## Build traveller structure

Each harness serial receives one Build Traveller. It records the progression through:

### BT-01 Document issue
- configuration revision;
- formboard revision;
- wire schedule revision;
- cavity schedule revision;
- splice schedule revision;
- protection schedule revision;
- approved deviations;
- builder acknowledgement.

### BT-02 Material issue
- wire batches/specification;
- connector PNs;
- terminal PNs;
- seals/locks/plugs;
- sleeving/heat shielding;
- junction hardware;
- protective devices;
- labels.

### BT-03 Cut / preparation
- conductor ID;
- cut length;
- strip length/tool setup where controlled;
- twist/shield preparation;
- heat-sleeve placement before terminal installation where required.

### BT-04 Crimp / terminal assembly
- terminal PN;
- wire size;
- crimp tooling;
- sample/pull-test reference;
- operator signoff;
- visual crimp inspection.

### BT-05 Connector population
- connector ID;
- cavity map revision;
- terminal lock confirmation;
- secondary lock/TPA/CPA confirmation;
- cavity plugs fitted;
- cavity photo where required.

### BT-06 Splice/junction build
- splice/junction ID;
- circuits joined;
- method/tool;
- sealing;
- physical location;
- inspection signoff.

### BT-07 Formboard assembly
- branch dimensions;
- breakout positions;
- service loops;
- clamp/retention positions;
- twist/shield routing;
- heat protection;
- X50/X51/X70 locations.

### BT-08 Pre-cover hold point HP-6

Before final sleeving/boot closure:

- complete photo set;
- continuity spot-check or full test as required;
- verify 4.0 mm² pump circuits;
- verify B15 size;
- verify CAN pair;
- verify CKP/CAM routing;
- verify sensor-ground segregation;
- verify X70/A21 dry-contact architecture;
- verify all approved deviations.

Engineering/manufacturer acceptance is required before proceeding where HP-6 is defined as a hold.

### BT-09 Final covering / labels
- sleeve/boot application;
- heat-shield application;
- connector and branch labels;
- main serial label;
- final strain relief.

### BT-10 Final electrical test
- 100% continuity;
- polarity;
- no cross-short;
- isolation;
- CAN-H/L verification;
- no hidden CAN termination;
- service-power backfeed check;
- X70/A21 isolation.

### BT-11 Final dimensional inspection
- branch length sample/100% check as required;
- connector orientation;
- service loops;
- formboard comparison;
- overall visual inspection.

### BT-12 Release to installation
- test report reference;
- deviations incorporated;
- build record complete;
- manufacturer QA signoff;
- engineering acceptance state.

## Pull-test control

The manufacturer shall define and return a crimp pull-test/sampling plan during DFM.

The traveller records the relevant pull-test batch/sample evidence for the terminal/wire combinations used.

A failed crimp validation blocks production using that setup until corrected and revalidated.

## Photograph requirements

Minimum photo sets should include:

- overall formboard pre-cover;
- every splice/junction before concealment;
- PMU connector/cavity population where required;
- FT550 connector/cavity population where required;
- X30/X31 high-current pump interfaces;
- X50/X51/X70 interfaces;
- CKP/CAM twist/shield routing;
- heat-protection sections;
- final completed harness with serial label.

Recommended naming:

`SN0001_BT08_overall_precover_01.jpg`

`SN0001_X30_pump1_01.jpg`

## Label durability acceptance

Labels shall remain legible after normal handling and must not create stiff stress risers immediately at connector exits.

No adhesive label should be placed where heat/oil/water exposure exceeds its rating.

## Deviation handling

Any shop-floor condition that prevents build to the released traveller requires RFI/deviation handling before the affected step proceeds.

Examples:

- specified terminal unavailable;
- wire does not fit seal;
- formboard dimension conflicts with connector orientation;
- sleeve cannot pass an installed connector;
- splice location causes excessive bundle diameter;
- label location interferes with serviceability.

## Release state

Current:

`BUILD_TRAVELLER_MASTER_PACK_RELEASED`

After manufacturer DFM confirmation:

`BUILD_TRAVELLER_METHOD_ACCEPTED`

For a specific harness serial after BT-01 through BT-12 pass:

`HARNESS_BUILD_RECORD_COMPLETE`

This record supports HP-6 pre-cover and HP-7 final harness acceptance but does not itself authorise first power.
