
#!/usr/bin/env python3
"""
Repository Structure Validator
Project: PDF Password Auditing with John the Ripper

Checks required folders, files, screenshots, documentation,
and local Markdown links.
"""

from pathlib import Path
import re
import sys

# Project root directory (parent of scripts/)
ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    ".gitignore",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "FOLDER-STRUCTURE.md",
    "SECURITY.md",
    "docs/README.md",
    "docs/EVIDENCE.md",
    "docs/Cybersecurity-Lab-Report.pdf",
    "references/SOURCES.md",
    "scripts/validate_repo.py",
    ".github/workflows/repository-checks.yml",
]

REQUIRED_SCREENSHOTS = [
    "01-johnny-setup.jpg",
    "02-johnny-configuration.jpg",
    "03-john-ripper-run-folder.jpg",
    "04-pdf-hash-sample-1.jpg",
    "05-pdf-hash-sample-2.jpg",
    "06-johnny-audit-result-1.jpg",
    "07-johnny-audit-result-2.jpg",
    "08-networkwalks-flag-achievement.jpg",
]

REQUIRED_DIRECTORIES = [
    "docs",
    "references",
    "screenshots",
    "scripts",
    ".github/workflows",
]

errors = []
warnings = []


def check_directories():
    """Verify that all required directories exist."""
    print("\n[1/4] Checking directories...")

    for directory in REQUIRED_DIRECTORIES:
        path = ROOT / directory

        if path.is_dir():
            print(f"  [OK] {directory}/")
        else:
            errors.append(f"Missing directory: {directory}/")
            print(f"  [FAIL] {directory}/")


def check_files():
    """Verify that all required files exist and are non-empty."""
    print("\n[2/4] Checking required files...")

    for filename in REQUIRED_FILES:
        path = ROOT / filename

        if not path.is_file():
            errors.append(f"Missing file: {filename}")
            print(f"  [FAIL] {filename}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty file: {filename}")
            print(f"  [FAIL] {filename} (empty)")
        else:
            print(f"  [OK] {filename}")


def check_screenshots():
    """Verify screenshot files and basic image signatures."""
    print("\n[3/4] Checking screenshots...")

    signatures = {
        ".jpg": (b"\xff\xd8\xff",),
        ".jpeg": (b"\xff\xd8\xff",),
        ".png": (b"\x89PNG\r\n\x1a\n",),
    }

    for filename in REQUIRED_SCREENSHOTS:
        path = ROOT / "screenshots" / filename

        if not path.is_file():
            errors.append(f"Missing screenshot: {filename}")
            print(f"  [FAIL] {filename}")
            continue

        extension = path.suffix.lower()
        valid_signatures = signatures.get(extension)

        if not valid_signatures:
            warnings.append(f"Unrecognized image extension: {filename}")
            print(f"  [WARN] {filename}: extension not checked")
            continue

        with path.open("rb") as image_file:
            header = image_file.read(8)

        if any(header.startswith(sig) for sig in valid_signatures):
            print(f"  [OK] {filename}")
        else:
            errors.append(f"Invalid image signature: {filename}")
            print(f"  [FAIL] {filename}: invalid image format")


def check_markdown_links():
    """Check relative local links in Markdown files."""
    print("\n[4/4] Checking local Markdown links...")

    markdown_files = list(ROOT.rglob("*.md"))
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

    for markdown_file in markdown_files:
        try:
            content = markdown_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            warnings.append(
                f"Could not read Markdown file: {markdown_file.relative_to(ROOT)}"
            )
            continue

        for target in link_pattern.findall(content):
            target = target.strip()

            # Ignore external URLs, email links and page anchors.
            if (
                target.startswith(("http://", "https://", "mailto:", "#"))
                or "://" in target
            ):
                continue

            target = target.split("#", 1)[0].split("?", 1)[0]

            if not target:
                continue

            linked_path = (markdown_file.parent / target).resolve()

            if not linked_path.exists():
                relative_file = markdown_file.relative_to(ROOT)
                errors.append(
                    f"Broken local link in {relative_file}: {target}"
                )
                print(f"  [FAIL] {relative_file} -> {target}")

    if not any("Broken local link" in error for error in errors):
        print("  [OK] No broken local Markdown links found.")


def main():
    print("=" * 60)
    print("       REPOSITORY STRUCTURE VALIDATOR")
    print("=" * 60)
    print(f"Project: {ROOT.name}")

    check_directories()
    check_files()
    check_screenshots()
    check_markdown_links()

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    print(f"Errors   : {len(errors)}")
    print(f"Warnings : {len(warnings)}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")

        print("\n[FAILED] Please fix the issues listed above.")
        return 1

    print("\n[SUCCESS] Repository structure validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
          
