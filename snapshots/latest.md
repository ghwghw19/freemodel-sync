# Free-model snapshot 2026-10-24

Automated daily health check by [freemodel-sync](https://github.com/ndwlbj/freemodel-sync) 0.3.1, generated 2026-10-24T10:19:33Z. Results are informational only: one tiny request per model from GitHub Actions, so availability and latency can differ for you.

## Providers

| Provider | Status | Free models | Probes sent | Notes |
|---|---|---|---|---|
| openrouter | ok | 16 | 15 | daily free limit 50 |
| groq | ok | 4 | 4 | - |

**20** free models, **14** ok, 5 failed, 1 not probed (probe cap 15 per provider).

## Models

| Provider | Model | Status | TTFT ms | Total ms | Context | Tools | Expires |
|---|---|---|---|---|---|---|---|
| groq | `qwen/qwen3.8-27b` | ok | 48 | 50 | 131072 | no | - |
| openrouter | `nvidia/nemotron-3.5-lightning:free` | ok | 168 | 306 | 1000000 | yes | - |
| openrouter | `cohere/north-mini-code:free` | ok | 170 | 548 | 256000 | yes | - |
| groq | `openai/gpt-oss-120b` | ok | 196 | 222 | 131072 | no | - |
| groq | `allam-2-7b` | ok | 242 | 251 | 4096 | no | - |
| groq | `openai/gpt-oss-20b` | ok | 247 | 260 | 131072 | no | - |
| openrouter | `nvidia/nemotron-3.5-super-vl:free` | ok | 291 | 405 | 1000000 | yes | - |
| openrouter | `nvidia/nemotron-3-ultra-550b-a55b:free` | ok | 382 | 488 | 1000000 | yes | - |
| openrouter | `recursive/flint-v1.0:free` | ok | 402 | 531 | 262144 | yes | - |
| openrouter | `liquid/lfm-2.5-2.6b:free` | ok | 414 | 1870 | 65536 | yes | - |
| openrouter | `dots-studio/dots-3-note-preview:free` | ok | 499 | 924 | 512000 | yes | 2026-12-31 |
| openrouter | `google/gemma-4-26b-a4b-it:free` | ok | 556 | 579 | 262144 | yes | - |
| openrouter | `xingchen-agi/xing4.0-29b-a4b:free` | ok | 1452 | 1636 | 262144 | yes | - |
| openrouter | `poolside/laguna-s-2.1:free` | ok | 5579 | 5789 | 262144 | yes | 2026-10-31 |
| openrouter | `google/gemma-4-31b-it:free` | 429 | - | 161 | 262144 | yes | - |
| openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | error | - | 95 | 256000 | yes | - |
| openrouter | `nvidia/nemotron-3-super-120b-a12b:free` | 404 | - | 78 | 262144 | yes | - |
| openrouter | `thinkingmachines/inkling-small:free` | 403 | - | 31 | 1048576 | yes | - |
| openrouter | `thinkingmachines/inkling:free` | 403 | - | 34 | 1048576 | yes | - |
| openrouter | `poolside/laguna-xs-2.1:free` | not_probed | - | - | 262144 | yes | 2026-10-31 |

## Changes

Compared with 2026-10-23:

- Added: none
- Removed: none
- Status changed: `openrouter|google/gemma-4-26b-a4b-it:free` 429 -> ok, `openrouter|nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` ok -> error, `openrouter|xingchen-agi/xing4.0-29b-a4b:free` 429 -> ok

### Expiring within 14 days

- `openrouter|poolside/laguna-s-2.1:free`: 2026-10-31 (7 days)
- `openrouter|poolside/laguna-xs-2.1:free`: 2026-10-31 (7 days)

Expiry dates come from OpenRouter's `expiration_date` field. Groq publishes no expiry dates, so Groq models never appear here.
