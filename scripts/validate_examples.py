#!/usr/bin/env python3
"""Validate synthetic examples against the public JSON Schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:
    sys.stderr.write(
        "Missing dependency. Install with:\n"
        "  pip install 'jsonschema>=4.18' referencing\n"
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"

PAIRS = [
    ("production-operation.schema.json", "production-operation.sample.json"),
    ("bom-line.schema.json", "bom-line.sample.json"),
    ("routing-card.schema.json", "routing-card.sample.json"),
    ("planning-task.schema.json", "planning-task.sample.json"),
]


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def build_registry() -> Registry:
    registry = Registry()
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        contents = load(path)
        # Register under both $id (if present) and the file name used by $ref.
        resource = Resource.from_contents(contents, default_specification=DRAFT202012)
        if "$id" in contents:
            registry = registry.with_resource(contents["$id"], resource)
        registry = registry.with_resource(path.name, resource)
        registry = registry.with_resource(f"https://example.local/iskra/schemas/{path.name}", resource)
    return registry


def main() -> int:
    registry = build_registry()
    errors = 0
    for schema_name, example_name in PAIRS:
        schema = load(SCHEMA_DIR / schema_name)
        instance = load(EXAMPLES_DIR / example_name)
        validator = Draft202012Validator(schema, registry=registry)
        errs = sorted(validator.iter_errors(instance), key=lambda e: e.path)
        if errs:
            errors += 1
            print(f"FAIL  {example_name}")
            for e in errs:
                loc = ".".join(str(p) for p in e.absolute_path) or "(root)"
                print(f"  - {loc}: {e.message}")
        else:
            print(f"OK    {example_name}")
    if errors:
        print(f"\n{errors} example(s) failed validation.")
        return 1
    print("\nAll examples valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
