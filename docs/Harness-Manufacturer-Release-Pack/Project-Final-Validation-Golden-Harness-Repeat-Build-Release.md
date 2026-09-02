# Project Final Validation + Golden Harness / Repeat-Build Release

## Purpose

Close the Turbo V-Rod FT550 harness development loop by proving that the physically installed, race-validated harness is identical in all controlled respects to the as-built production definition and is suitable to become the Golden Harness / repeat-build master.

This milestone links:

- race-validated vehicle configuration;
- physical prototype harness;
- as-built BOM;
- wire/cavity/splice/protection schedules;
- branch dimensions;
- manufacturer build traveller;
- HP-6/HP-7 evidence;
- commissioning logs;
- final race configuration archive.

## Entry conditions

Do not begin final release unless:

- `FINAL_RACE_CONFIGURATION_ARCHIVED` is PASS;
- `FINAL_RACE_CONFIGURATION_ACTIVE` is confirmed on the bike;
- `TRACK_LAUNCH_VALIDATED` is PASS;
- `HP7_FINAL_HARNESS_ACCEPTED` is PASS;
- first-power and first-start commissioning are complete;
- low-load heat-cycle validation is complete;
- dyno load commissioning is complete;
- Two-Step launch control commissioning is complete if fitted/released;
- no unresolved harness-related RFI/deviation/nonconformance remains;
- the harness has accumulated enough validated operation to support a repeat-build decision.

## GF-0 Identity and traceability

Record:

- harness serial;
- harness configuration revision;
- Golden Harness candidate revision;
- formboard revision;
- manufacturer;
- build date;
- FT550 race-release ID;
- PMU configuration revision;
- SparkPRO/dwell revision;
- final protection revision;
- final race operating-envelope revision.

Output: `GF0_TRACEABILITY_ACCEPTED`

## GF-1 Physical configuration comparison

Compare the installed harness to the final as-built configuration.

Verify:

- connector housings/PNs;
- terminal families;
- wire sizes/specs;
- pump 4.0 mm² feeds/returns;
- B15 conductor;
- B39/B40 paths;
- branch dimensions;
- splice locations;
- junction hardware;
- heat protection;
- labels;
- X50/X51/X70 hardware;
- OEM X10-X23 connector/pigtail strategy;
- clamps/strain relief.

Output: `GF1_PHYSICAL_CONFIGURATION_MATCHED`

## GF-2 Electrical configuration comparison

Verify the installed harness still matches the released electrical schedules after dyno/track development.

Check:

- continuity/circuit assignments where practical;
- protection hardware;
- PMU channel mapping;
- CAN topology;
- trigger routing/polarity;
- X70/A21 architecture;
- sensor-ground segregation;
- no temporary dyno/track wiring remains in the production baseline.

Output: `GF2_ELECTRICAL_CONFIGURATION_MATCHED`

## GF-3 Post-race harness condition inspection

Inspect the physical harness after validated high-load/launch operation.

Look for:

- heat damage/discolouration;
- terminal relaxation/push-back;
- connector fretting;
- seal displacement;
- chafe;
- branch tension;
- loosened J-P01/J-P02 hardware;
- relay/socket heating;
- pump connector heating;
- B15/B39/B40 thermal evidence;
- turbo/exhaust heat exposure;
- vibration-related movement.

Any recurring defect must be corrected in the Golden Harness definition rather than accepted as normal.

Output: `GF3_POST_RACE_CONDITION_ACCEPTED`

## GF-4 Configuration drift audit

Review every approved deviation, field repair, trackside change and calibration-driven hardware change made since the Rev 1 harness was first manufactured.

Classify each as:

- incorporated into production baseline;
- temporary development-only and removed;
- superseded;
- rejected;
- requires new revision.

No undocumented trackside modification may enter repeat production.

Output: `GF4_CONFIGURATION_DRIFT_CLOSED`

## GF-5 Golden Harness document freeze

Freeze the final production set:

1. As-Built BOM;
2. Production Wire / Circuit Master Schedule;
3. Connector / Cavity Master Schedule;
4. Splice / Junction Master Schedule;
5. Protection / Fuse / PMU Current-Limit Master Schedule;
6. branch-dimension/formboard schedule;
7. connector/terminal/seal/tooling schedule;
8. sleeving/heat-protection schedule;
9. label/identification schedule;
10. build traveller;
11. HP-6/HP-7 inspection forms;
12. serial/build record template;
13. approved deviations/ECNs;
14. manufacturer test plan.

All production files must point to the same Golden Harness revision.

Output: `GF5_GOLDEN_HARNESS_DOCUMENT_SET_FROZEN`

## GF-6 Golden Harness validation

The physical harness candidate may be promoted when:

- all applicable prototype acceptance rows PASS;
- all corrections are incorporated;
- post-race condition is accepted;
- no temporary development wiring remains;
- all schedules match the installed validated harness;
- repeat-build materials are available or approved alternatives are controlled;
- manufacturer confirms formboard/process is repeatable.

Output:

`GOLDEN_HARNESS_VALIDATED`

## GF-7 Repeat-build process qualification

Before authorising repeat manufacture, verify manufacturer readiness:

- formboard/fixture revision frozen;
- controlled BOM available;
- terminals/connectors repeatably sourceable;
- crimp tooling/process controlled;
- pull-test plan active;
- 100% continuity/isolation test plan active;
- HP-6 pre-cover evidence process active;
- serial traceability active;
- substitution control active;
- deviation/RFI process active;
- packaging/transport method defined where relevant.

Output: `GF7_REPEAT_BUILD_PROCESS_ACCEPTED`

## GF-8 First repeat harness validation

The first harness made from the Golden Harness/formboard definition is treated as a repeat-process qualification article.

Compare it against the Golden Harness for:

- dimensions;
- cavity population;
- wire sizes;
- splice positions;
- labels;
- connector hardware;
- electrical continuity/isolation;
- workmanship.

Where practical, perform vehicle fit verification before declaring the repeat process proven.

Output: `GF8_FIRST_REPEAT_ARTICLE_ACCEPTED`

## Final release

When GF-0 through GF-8 PASS:

`REPEAT_BUILD_RELEASED`

and configuration control becomes:

`REPEAT_BUILD_CONFIGURATION_CONTROL_ACTIVE`

## Change control after release

After repeat-build release, any change to:

- conductor size/spec;
- connector/terminal/seal;
- cavity assignment;
- splice topology/location;
- branch dimension;
- protection;
- CAN/trigger wiring;
- ground/reference architecture;
- X70/A21 architecture;
- high-current routing;
- heat protection;

requires controlled engineering review and the appropriate regression test.

## Final project states

The intended end-state ladder is:

`FINAL_RACE_CONFIGURATION_ARCHIVED`

-> `GOLDEN_HARNESS_VALIDATED`

-> `AS_BUILT_CONFIGURATION_FROZEN`

-> `REPEAT_BUILD_RELEASED`

-> `REPEAT_BUILD_CONFIGURATION_CONTROL_ACTIVE`

At that point, the Rev 1 development harness becomes a controlled, repeatable product definition rather than a one-off prototype.
