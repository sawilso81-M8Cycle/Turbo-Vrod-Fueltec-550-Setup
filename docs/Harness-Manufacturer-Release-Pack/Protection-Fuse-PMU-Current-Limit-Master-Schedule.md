# Protection / Fuse / PMU Current-Limit Master Schedule

## Purpose

Provide one authoritative protection map for every powered branch in the Rev 1 Turbo V-Rod harness.

This schedule complements the Production Wire/Circuit, Connector/Cavity, and Splice/Junction master schedules. A powered branch is not HP-5 ready until its protection device, rating/current limit, transient strategy, coordination relationship and evidence state are defined.

## Protection hierarchy

Use the following order of control:

1. primary battery/master protection;
2. B15 PMU feed protection;
3. PMU electronic output protection or external branch fuse/relay protection;
4. dedicated engine-critical branch protection such as B39 and B40;
5. local service/accessory protection where applicable.

Protection must protect the weakest approved part of the downstream path, not merely the conductor.

## Required fields per branch

Every protected circuit shall identify:

- branch/circuit ID;
- function;
- source;
- destination/load;
- conductor size;
- expected continuous current;
- transient/inrush current;
- protection type;
- protection value/current limit;
- time-delay/transient strategy;
- PMU output/channel if applicable;
- upstream protection;
- downstream protection;
- conductor capability evidence;
- terminal/connector capability evidence;
- coordination result;
- final release state.

## Locked rules

- fuel-pump branches retain 4.0 mm² minimum feed and dedicated 4.0 mm² return;
- B15 retains 10 mm² baseline unless an approved engineering change upsizes it;
- B39 and B40 remain independently protected;
- no protection value may exceed the proven capability of any wire, terminal, connector, splice or switching device in the path;
- a PMU current-limit setting is still a protection device and must be documented like a fuse;
- nuisance trips are solved by understanding the real transient, not by blindly increasing the limit;
- external power-stage branches require source-side protection appropriate to the high-current path;
- service +12 V at X50/X51 must be separately limited/protected.

## PMU output branches

For PMU-driven loads record:

- exact PMU16 hardware revision;
- exact output/channel;
- channel continuous/transient capability from authoritative documentation;
- measured load current/inrush;
- configured current limit;
- trip delay/profile if supported;
- retry/latch behaviour if supported;
- fault reporting requirement;
- whether the PMU channel directly carries load current or commands an external stage.

## External relay/SSR branches

Where a PMU output becomes a command only, separate the two protection functions:

- low-current PMU command/output protection;
- separately protected high-current load path.

Do not treat relay contact rating as branch protection.

## Selective coordination

The intended order under a branch fault is normally:

`local/branch protection → upstream distribution protection → master protection`

where practical.

The goal is to prevent a non-critical auxiliary branch fault from unnecessarily killing the entire engine-management system while still ensuring engine-critical faults fail predictably.

## Release states

Working row:

`PROTECTION_VALUE_PENDING`

Evidence accepted but final build data not complete:

`PROTECTION_ARCHITECTURE_FROZEN`

HP-5 ready:

`HP5_RELEASED`

Master schedule release:

`PROTECTION_MASTER_SCHEDULE_HP5_RELEASED`

## STOP conditions

Do not release a protection row when:

- current/inrush evidence is required but missing;
- exact PMU channel/hardware is unknown;
- terminal/connector current capability is unverified;
- proposed value exceeds the downstream path capability;
- coordination with upstream protection has not been reviewed;
- abnormal heating or voltage drop remains unresolved;
- switching architecture remains undecided.
