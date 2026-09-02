# Rev 2 Manufacturer Package Generator Release

## Purpose

Provide a repeatable method to create a clean manufacturer-facing ZIP from the controlled repository rather than manually selecting files for each issue.

## Generator

Repository tool:

`tools/build_manufacturer_release_rev2.py`

Run from repository root:

```text
python tools/build_manufacturer_release_rev2.py
```

## Output

The generator creates:

`dist/Harness-Manufacturer-Release-Pack-Rev2.zip`

and an unpacked staging copy under:

`dist/Harness-Manufacturer-Release-Pack-Rev2/`

## Package structure

- `README-FIRST.txt`
- `BUILD-INFO.txt`
- `00_PACKAGE_MANIFEST.csv`
- `SHA256SUMS.txt`
- `01_Manufacturer_Release/`
- `02_Commissioning_Gates/`

## Controls

The build fails if any mandatory controlled file is missing.

Every packaged controlled file receives a SHA-256 hash in the manifest. A second checksum file allows the complete issued package to be checked for accidental modification.

ZIP timestamps are fixed to improve reproducibility.

The generator intentionally excludes unrelated development-repository material.

## Release banner

Every generated package remains:

`RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED`

until a later engineering release explicitly promotes the project to `MANUFACTURING_RELEASED_REV1`.

## Manufacturer workflow

1. Generate ZIP from a clean repository checkout.
2. Record the resulting ZIP SHA-256 in the issue/transmittal record.
3. Send the ZIP to the selected harness builder.
4. Builder starts at `README-FIRST.txt` and `00-Manufacturer-Release-Index-Rev2.md`.
5. Builder returns DFM response, RFIs, deviations, proposed PNs/methods and quotation.
6. Engineering reviews the returned package.
7. Only after blocker closure and signed release may an electrically functional Rev 1 harness be manufactured.

## Milestone state

`REV2_MANUFACTURER_PACKAGE_GENERATOR_RELEASED`
