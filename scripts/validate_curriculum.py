#!/usr/bin/env python3
"""Dependency-free structural checks for the public curriculum repository."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODULES = ROOT / "modules"
REQUIRED_MODULE_FILES = {
    "README.md",
    "manifest.yml",
    "learner-mission.md",
    "trainer-guide.md",
    "rubric.md",
    "debrief.md",
}
REQUIRED_MANIFEST_KEYS = {
    "module_id:",
    "title:",
    "version:",
    "status:",
    "duration_minutes:",
    "outcomes:",
    "deliverables:",
    "safety:",
}
REQUIRED_SAFETY_TERMS = (
    "synthetic",
    "approved",
    "unauthorized",
    "secrets",
)

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)

def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")

def main() -> None:
    for required in (
        "README.md",
        "LICENSE",
        "LICENSE-CONTENT.md",
        "NOTICE.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CITATION.cff",
        "policies/lab-safety.md",
        "CURRICULUM_MAP.md",
    ):
        read(ROOT / required)

    module_dirs = sorted(p for p in MODULES.iterdir() if p.is_dir())
    if len(module_dirs) != 13:
        fail(f"expected 13 module directories, found {len(module_dirs)}")

    ids = []
    for module_dir in module_dirs:
        files = {p.name for p in module_dir.iterdir() if p.is_file()}
        missing = REQUIRED_MODULE_FILES - files
        if missing:
            fail(f"{module_dir.name} missing: {', '.join(sorted(missing))}")
        manifest = read(module_dir / "manifest.yml")
        for key in REQUIRED_MANIFEST_KEYS:
            if key not in manifest:
                fail(f"{module_dir.name}/manifest.yml missing {key}")
        module_id = re.search(r"^module_id:\s*(M\d+)$", manifest, re.MULTILINE)
        if not module_id:
            fail(f"{module_dir.name}/manifest.yml has no valid module_id")
        ids.append(module_id.group(1))
        safety_text = "\n".join([
            manifest.lower(),
            read(module_dir / "learner-mission.md").lower(),
            read(module_dir / "trainer-guide.md").lower(),
        ])
        if not all(term in safety_text for term in REQUIRED_SAFETY_TERMS):
            fail(f"{module_dir.name} is missing one or more safety markers")

    expected_ids = [f"M{i:02d}" for i in range(13)]
    if ids != expected_ids:
        fail(f"module IDs are {ids}; expected {expected_ids}")

    for template in (
        "templates/evidence-log.md",
        "templates/ai-system-inventory.md",
        "templates/agent-action-map.md",
        "templates/evaluation-plan.md",
        "templates/incident-playbook.md",
        "templates/standards-crosswalk.md",
    ):
        read(ROOT / template)

    print(f"OK: validated {len(module_dirs)} modules and required public artifacts")

if __name__ == "__main__":
    main()
