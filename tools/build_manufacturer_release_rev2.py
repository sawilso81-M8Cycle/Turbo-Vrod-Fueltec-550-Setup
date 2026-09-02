#!/usr/bin/env python3
"""Build the controlled Harness Manufacturer Release Pack Rev 2 ZIP.

Run from the repository root:
    python tools/build_manufacturer_release_rev2.py

The script intentionally fails if a mandatory release file is missing. It copies
only manufacturer-relevant controlled files into a clean staging directory,
generates SHA-256 checksums and creates a deterministic ZIP under dist/.
"""

from __future__ import annotations

import csv
import hashlib
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MFR = ROOT / "docs" / "Harness-Manufacturer-Release-Pack"
COMM = ROOT / "docs" / "Commissioning"
DIST = ROOT / "dist"
STAGE = DIST / "Harness-Manufacturer-Release-Pack-Rev2"
ZIP_PATH = DIST / "Harness-Manufacturer-Release-Pack-Rev2.zip"

MANDATORY = [
    MFR / "00-Manufacturer-Release-Index-Rev2.md",
    MFR / "Manufacturer-Release-Document-Register-Rev2.csv",
    MFR / "Harness-Manufacturer-DFM-Release-Pack-Rev2.md",
    MFR / "Harness-Manufacturer-DFM-Response-Register.csv",
    MFR / "Harness-Manufacturer-RFI-Register.csv",
    MFR / "Harness-Manufacturer-Deviation-Register.csv",
    MFR / "Pre-Manufacture-Release-Audit.md",
    MFR / "Pre-Manufacture-Release-Audit-Register.csv",
    MFR / "G0-G1-Blocker-Burn-Down-Review.md",
    MFR / "G0-G1-Burn-Down-Register.csv",
    MFR / "Master-Build-Blocker-Register.csv",
    MFR / "PMU16-Connector-Terminal-Production-Freeze.md",
    MFR / "PMU16-Cavity-Terminal-Wire-Audit.md",
    MFR / "PMU16-Cavity-Terminal-Wire-Audit.csv",
    MFR / "Fuel-Pump-Power-Interface-Freeze.md",
    MFR / "Fuel-Pump-Power-Interface-Verification-Register.csv",
    MFR / "Cooling-Aux-Power-Interface-Freeze.md",
    MFR / "Cooling-Aux-Power-Verification-Register.csv",
    MFR / "Primary-Power-Distribution-Freeze.md",
    MFR / "Primary-Power-Verification-Register.csv",
    MFR / "Engine-Critical-EPM-Power-Distribution-Freeze.md",
    MFR / "Engine-Critical-EPM-Power-Verification-Register.csv",
    MFR / "Injector-Electrical-Architecture-Freeze.md",
    MFR / "Injector-Electrical-Decision-Register.csv",
    MFR / "Ignition-Coil-SparkPRO-Electrical-Freeze.md",
    MFR / "Ignition-Coil-SparkPRO-Verification-Register.csv",
    MFR / "Trigger-Integrity-Freeze.md",
    MFR / "Trigger-Integrity-Verification-Register.csv",
    MFR / "CAN-Service-Interface-Production-Freeze.md",
    MFR / "CAN-Service-Verification-Register.csv",
    MFR / "X70-Two-Step-Relay-Hardware-Freeze.md",
    MFR / "X70-Two-Step-Relay-Verification-Register.csv",
    MFR / "OEM-Connector-Physical-Identification-Pack.md",
    MFR / "OEM-Connector-Physical-ID-Register.csv",
    MFR / "X50-Master-Engineering-Service-Connector-Freeze.md",
    MFR / "X50-Service-Connector-Cavity-Register.csv",
    COMM / "Fuel-Pump-Verification-Pack.md",
    COMM / "Fuel-Pump-Verification-Worksheet.csv",
    COMM / "Fuel-Pump-Switching-Decision-Register.csv",
    COMM / "Injector-Electrical-Verification-Pack.md",
    COMM / "Injector-Electrical-Verification-Worksheet.csv",
    COMM / "Injector-Driver-Final-Decision.csv",
    COMM / "Coil-SparkPRO-Verification-Pack.md",
    COMM / "Coil-SparkPRO-Verification-Worksheet.csv",
    COMM / "Coil-Dwell-B40-Final-Decision.csv",
    COMM / "Cooling-Load-Verification-Pack.md",
    COMM / "Cooling-Load-Verification-Worksheet.csv",
    COMM / "Cooling-Load-Final-Decision.csv",
    COMM / "First-Power-First-Start-Master-Release-Gate.md",
    COMM / "First-Power-First-Start-Verification-Register.csv",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def target_for(src: Path) -> Path:
    if src.is_relative_to(MFR):
        return STAGE / "01_Manufacturer_Release" / src.name
    if src.is_relative_to(COMM):
        return STAGE / "02_Commissioning_Gates" / src.name
    raise ValueError(src)


def main() -> int:
    missing = [p for p in MANDATORY if not p.is_file()]
    if missing:
        print("ERROR: manufacturer package not built. Mandatory files missing:", file=sys.stderr)
        for p in missing:
            print(f"  - {p.relative_to(ROOT)}", file=sys.stderr)
        return 2

    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    DIST.mkdir(parents=True, exist_ok=True)

    manifest_rows = []
    for src in MANDATORY:
        dst = target_for(src)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        manifest_rows.append({
            "Package_Path": dst.relative_to(STAGE).as_posix(),
            "Repository_Path": src.relative_to(ROOT).as_posix(),
            "SHA256": sha256(dst),
            "Bytes": dst.stat().st_size,
        })

    manifest = STAGE / "00_PACKAGE_MANIFEST.csv"
    with manifest.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Package_Path", "Repository_Path", "SHA256", "Bytes"])
        writer.writeheader()
        writer.writerows(manifest_rows)

    readme = STAGE / "README-FIRST.txt"
    readme.write_text(
        "Turbo V-Rod Harness Manufacturer Release Pack Rev 2\n"
        "===================================================\n\n"
        "Authority: RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED\n\n"
        "Start with:\n"
        "  01_Manufacturer_Release/00-Manufacturer-Release-Index-Rev2.md\n\n"
        "Manufacturer return files:\n"
        "  Harness-Manufacturer-DFM-Response-Register.csv\n"
        "  Harness-Manufacturer-RFI-Register.csv\n"
        "  Harness-Manufacturer-Deviation-Register.csv\n\n"
        "Do not begin an electrically functional Rev 1 harness until engineering issues\n"
        "MANUFACTURING_RELEASED_REV1.\n",
        encoding="utf-8",
    )

    checksums = STAGE / "SHA256SUMS.txt"
    checksum_files = [readme, manifest] + [target_for(p) for p in MANDATORY]
    checksums.write_text(
        "".join(f"{sha256(p)}  {p.relative_to(STAGE).as_posix()}\n" for p in checksum_files),
        encoding="utf-8",
    )

    build_info = STAGE / "BUILD-INFO.txt"
    build_info.write_text(
        "Package: Harness-Manufacturer-Release-Pack-Rev2\n"
        f"Generated UTC: {datetime.now(timezone.utc).isoformat()}\n"
        f"Controlled files: {len(MANDATORY)}\n"
        "Release authority: RFQ_AND_DFM_ALLOWED / FUNCTIONAL_BUILD_NOT_YET_AUTHORISED\n",
        encoding="utf-8",
    )

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    # Fixed ZIP timestamps improve reproducibility across repeated builds.
    fixed_time = (2026, 9, 3, 0, 0, 0)
    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in STAGE.rglob("*") if p.is_file()):
            arc = Path(STAGE.name) / path.relative_to(STAGE)
            info = zipfile.ZipInfo(arc.as_posix(), fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    print(f"Built: {ZIP_PATH.relative_to(ROOT)}")
    print(f"Files: {len(MANDATORY)} controlled + manifest/readme/checksums/build-info")
    print(f"SHA256: {sha256(ZIP_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
