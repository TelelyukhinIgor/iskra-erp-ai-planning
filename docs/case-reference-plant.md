# Reference plant case — “Iskra”

All figures in this case are illustrative assumptions of a reference plant model for discussion. They are not measured statistics of a real plant or results of a real deployment.

## Status of this case

This case is built on a **reference model** of a household-appliance discrete plant. Effect figures below are **calculated estimates** under that model. They are **not** audited results of a real deployment.

Use them to discuss order-of-magnitude value and pilot scope — not as a contractual performance guarantee.

## Plant profile (reference model)

| Attribute | Value in model |
|-----------|----------------|
| Industry | Household electrical appliances |
| Headcount | 310 people, 2 shifts |
| Catalogue | 38 finished-good models |
| Key equipment | 27 critical units (incl. multiple moulding presses) |
| Areas | Stamping, plastics moulding, machining, electrical assembly, two assembly lines, QC, packing |
| Engineering archive (model assumption) | ~4 800 drawings (of which ~2 900 paper/scans), ~1 900 routing sheets, ~6 400 item master positions |
| Systems of record | Existing ERP; optional MES; payroll/HR in the plant’s usual systems |

## Starting pains (model assumptions)

- Building a production plan for **one** order: about **4 working days** in spreadsheets; redo on every change.
- Technology knowledge concentrated in **two or three** process engineers; large share of drawings only on paper/scans.
- About **29%** of orders ship late; leadership often hears about misses from the customer.
- Leadership status pack: about **2 days** of manual collection.

## Illustrative planning run (synthetic order)

**Synthetic order REF-0418** (model assumption): 1 750 finished goods across five catalogue models; customer asks for **30** working days.

Calculated machine-side draft time in the model: **~1 hour 40 minutes** end-to-end (vs. ~4 days / ~32 person-hours manual), broken into proposal steps such as order capture, archive match, BOM explosion, routing draft, stock check, buy list, schedule, cost/cash sketch, and task fan-out. **Human approval** sits on top of that draft.

In the modelled run, two issues are flagged **before** release: a moulding work centre above 100% load (rebalanced onto a sister press) and a long-lead component (switched to an alternate with a shorter stated lead time). The modelled feasible horizon is **23** working days against the 30-day request.

Product names, quantities, and retailers in marketing decks are **synthetic** for the reference story; this repository does not include real-plant drawings or confidential commercial numbers.

## Calculated estimates after six months (model)

| Indicator | Before | After |
|-----------|--------|-------|
| Order entry → approved plan | 4 working days | 1 working day |
| On-time shipment share | 71% | 88% |
| Average order lead time | 34 working days | 27 working days (−20%) |
| Design → shop transfer errors | baseline | −60% |
| Material inventory | baseline | −12% (dead stock −15%) |
| Time to prepare a new modification | baseline | −50% |
| Bottleneck (moulding) utilisation | 74% | 82% |
| Overtime hours | baseline | −30% |
| Leadership status pack | ~2 days manual | near-real-time / ~15‑minute refresh in the model narrative |

Archive digitisation (illustrative estimate): in the model narrative, thousands of drawings/routing sheets move into a searchable digital store over roughly **seven weeks**, with a minority of spots marked for process-engineer confirmation rather than silent guessing.

## Rollout pattern (model)

1. Express assessment of data and archive readiness.  
2. Pilot on **one** product family beside the manual plan.  
3. Scale to the full catalogue and leadership workstation.  

The reference story uses a **nine-month** full-cycle sketch (illustrative estimate), assuming the plant is not stopped. Real calendars depend on archive quality and governance — fixed only after assessment.

## What this case deliberately omits

- Names of real plants, live SKUs, supplier contracts, payroll, or drawings.  
- Pilot price lists and commercial terms.  
- Proprietary model choices, prompts, solver formulations, and ERP adapter code.
