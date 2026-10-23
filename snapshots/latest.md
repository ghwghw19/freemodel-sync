# Free-model snapshot 2026-10-23

Automated daily health check by [freemodel-sync](https://github.com/ndwlbj/freemodel-sync) 0.3.0, generated 2026-10-23T05:30:04Z. Results are informational only: one tiny request per model from GitHub Actions, so availability and latency can differ for you.

## Providers

| Provider | Status | Free models | Probes sent | Notes |
|---|---|---|---|---|
| openrouter | ok | 16 | 15 | daily free limit 50 |
| groq | ok | 4 | 4 | - |

**20** free models, **13** ok, 6 failed, 1 not probed (probe cap 15 per provider).

## Models

| Provider | Model | Status | TTFT ms | Total ms | Context | Tools | Expires |
|---|---|---|---|---|---|---|---|
| groq | `qwen/qwen3.8-27b` | ok | 45 | 48 | 131072 | no | - |
| groq | `openai/gpt-oss-20b` | ok | 163 | 176 | 131072 | no | - |
| openrouter | `nvidia/nemotron-3.5-lightning:free` | ok | 202 | 375 | 1000000 | yes | - |
| groq | `openai/gpt-oss-120b` | ok | 214 | 241 | 131072 | no | - |
| openrouter | `cohere/north-mini-code:free` | ok | 224 | 419 | 256000 | yes | - |
| openrouter | `nvidia/nemotron-3.5-super-vl:free` | ok | 258 | 438 | 1000000 | yes | - |
| groq | `allam-2-7b` | ok | 291 | 300 | 4096 | no | - |
| openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | ok | 291 | 753 | 256000 | yes | - |
| openrouter | `nvidia/nemotron-3-ultra-550b-a55b:free` | ok | 417 | 589 | 1000000 | yes | - |
| openrouter | `dots-studio/dots-3-note-preview:free` | ok | 465 | 992 | 512000 | yes | 2026-12-31 |
| openrouter | `poolside/laguna-s-2.1:free` | ok | 493 | 624 | 262144 | yes | 2026-10-31 |
| openrouter | `recursive/flint-v1.0:free` | ok | 514 | 608 | 262144 | yes | - |
| openrouter | `liquid/lfm-2.5-2.6b:free` | ok | 6364 | 7862 | 65536 | yes | - |
| openrouter | `google/gemma-4-26b-a4b-it:free` | 429 | - | 199 | 262144 | yes | - |
| openrouter | `google/gemma-4-31b-it:free` | 429 | - | 117 | 262144 | yes | - |
| openrouter | `nvidia/nemotron-3-super-120b-a12b:free` | 404 | - | 88 | 262144 | yes | - |
| openrouter | `thinkingmachines/inkling-small:free` | 403 | - | 19 | 1048576 | yes | - |
| openrouter | `thinkingmachines/inkling:free` | 403 | - | 104 | 1048576 | yes | - |
| openrouter | `xingchen-agi/xing4.0-29b-a4b:free` | 429 | - | 358 | 262144 | yes | - |
| openrouter | `poolside/laguna-xs-2.1:free` | not_probed | - | - | 262144 | yes | 2026-10-31 |

## Changes

No earlier snapshot to compare with.

### Expiring within 14 days

- `openrouter|poolside/laguna-s-2.1:free`: 2026-10-31 (8 days)
- `openrouter|poolside/laguna-xs-2.1:free`: 2026-10-31 (8 days)

Expiry dates come from OpenRouter's `expiration_date` field. Groq publishes no expiry dates, so Groq models never appear here.
