# AI Executive War Room

A public-safe, runnable multi-agent executive decision simulator.

The lab models a fictional executive council where independent agents represent different leadership perspectives:

- CTO — technology resilience and architecture
- CFO — financial exposure and liquidity
- COO — operational continuity and execution
- CISO — cyber risk and control integrity
- Product — customer impact and product continuity
- Red Team — challenges assumptions and exposes blind spots
- Chair — synthesizes the final decision brief

The simulator runs entirely on deterministic local logic by default. No external AI API is required.

## What It Does

Crisis → Executive Agent Analysis → Independent Recommendations → Conflict Detection → Trade-off Scoring → Red-Team Challenge → Council Synthesis → Dissent Log → Final Executive Brief

## Creative Features

- Multi-agent executive perspectives
- Different risk appetites by role
- Consensus scoring
- Dissent preservation
- Red-team challenge before final recommendation
- Decision reversibility scoring
- Financial / operational / cyber / customer trade-offs
- Crisis injects that evolve during a session
- Decision-confidence meter
- Executive brief generation
- Runnable CLI
- Automated tests

## Quick Start

Run a crisis:

```bash
python -m src.cli run platform-outage
```

Compare two response strategies:

```bash
python -m src.cli compare platform-outage
```

Run a staged war-room exercise:

```bash
python -m src.cli exercise cyber-disruption
```

Run tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Safety & Public Data

All companies, people, prices, systems, vendors, incidents, and crisis data are fictional.

This repository must never contain real company, customer, employee, project, contract, financial, infrastructure, security, incident, or vendor information.

## Author

Eng. Islam El Sherbiny
