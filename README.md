# Morning-Negotiation
A two agent system for runners where a Coach (optimizes the training plan) and an Athlete (optimizes for how you feel) negotiate what you should run today.

## 1. The Data

**Current**
- Strava bulk download
- for backtesting and evals

**Ongoing/Active** 
- Strava MCP
- used in agent loop

## 2. Tech/Tool Stack
- Python
- LM Studio (Local Inference)
- openai SDK (pointed at LM Studio)
- anthropic SDK (Hosted Inference)
- fastmcp (PrefectHQ)
- SQLite (storage)
- JSONL (tracing)

## 3. Models
### Local
- Qwen 3.5 9B (primary local model)
### Hosted
- Claude Haiku 4.5  (iteration, routing, cheap eval runs)
- Claude Sonnet 5 (**default for Coach and Athlete**)
- Claude Opus 5 (only if Sonnet fails at negotiation)