# Data model (evaluation schemas)

These JSON Schemas describe **generic** artefacts a planning layer exchanges with people and with an ERP/MES. They are intentionally high-level: enough to show systems-analysis quality, not enough to reverse-engineer a proprietary implementation.

- Schemas live in [`../schemas/`](../schemas/).
- Synthetic examples live in [`../examples/`](../examples/).
- Validate with: `python scripts/validate_examples.py` (from repo root).

## Objects

| Schema | Purpose |
|--------|---------|
| `routing-card.schema.json` | Approved or draft routing for one manufactured item |
| `production-operation.schema.json` | One step inside a routing (work centre, time norms) |
| `bom-line.schema.json` | One component/material line of a product structure |
| `planning-task.schema.json` | A task published to a plant function after a planning run |

## Conventions

- Identifiers are opaque strings (`id`); plants map them to ERP keys during integration.
- Quantities use decimal strings or numbers plus an explicit `uom` (unit of measure).
- `status` values are closed enums suitable for human-in-the-loop workflows (`draft` → `in_review` → `approved` / `rejected`).
- No plant-specific custom fields, pricing algorithms, or recognition metadata are included.

## Non-goals

- Not an ERP schema replacement.
- Not a full ISA-95 / B2MML profile.
- Not a wire format for the production product.
