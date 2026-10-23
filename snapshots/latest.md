# Free-model snapshot 2026-10-23

Automated daily health check by [freemodel-sync](https://github.com/ndwlbj/freemodel-sync) 0.3.0, generated 2026-10-23T02:53:25Z. Results are informational only: one tiny request per model from GitHub Actions, so availability and latency can differ for you.

## Providers

| Provider | Status | Free models | Probes sent | Notes |
|---|---|---|---|---|
| openrouter | account_error | 16 | 11 | account/quota error (200): xingchen-agi/xing4.0-29b-a4b:free is temporarily rate-limited upstream. Please retry shortly, or add your own key to accumulate your rate limits: https://openrouter.ai/setti; daily free limit 50 |
| groq | ok | 4 | 4 | - |

**20** free models, **8** ok, 7 failed, 5 not probed (probe cap 15 per provider).

## Models

| Provider | Model | Status | TTFT ms | Total ms | Context | Tools | Expires |
|---|---|---|---|---|---|---|---|
| groq | `qwen/qwen3.8-27b` | ok | 55 | 59 | 131072 | no | - |
| openrouter | `nvidia/nemotron-3.5-lightning:free` | ok | 128 | 261 | 1000000 | yes | - |
| openrouter | `recursive/flint-v1.0:free` | ok | 134 | 248 | 262144 | yes | - |
| groq | `openai/gpt-oss-20b` | ok | 221 | 235 | 131072 | no | - |
| groq | `allam-2-7b` | ok | 246 | 257 | 4096 | no | - |
| groq | `openai/gpt-oss-120b` | ok | 295 | 323 | 131072 | no | - |
| openrouter | `dots-studio/dots-3-note-preview:free` | ok | 486 | 919 | 512000 | yes | 2026-12-31 |
| openrouter | `nvidia/nemotron-3-ultra-550b-a55b:free` | ok | 1065 | 1799 | 1000000 | yes | - |
| openrouter | `google/gemma-4-26b-a4b-it:free` | 429 | - | 182 | 262144 | yes | - |
| openrouter | `google/gemma-4-31b-it:free` | 429 | - | 1446 | 262144 | yes | - |
| openrouter | `nvidia/nemotron-3-super-120b-a12b:free` | 404 | - | 129 | 262144 | yes | - |
| openrouter | `nvidia/nemotron-3.5-super-vl:free` | 502 | - | 355 | 1000000 | yes | - |
| openrouter | `thinkingmachines/inkling-small:free` | 403 | - | 22 | 1048576 | yes | - |
| openrouter | `thinkingmachines/inkling:free` | 403 | - | 17 | 1048576 | yes | - |
| openrouter | `xingchen-agi/xing4.0-29b-a4b:free` | error | - | 11562 | 262144 | yes | - |
| openrouter | `cohere/north-mini-code:free` | not_probed | - | - | 256000 | yes | - |
| openrouter | `liquid/lfm-2.5-2.6b:free` | not_probed | - | - | 65536 | yes | - |
| openrouter | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | not_probed | - | - | 256000 | yes | - |
| openrouter | `poolside/laguna-s-2.1:free` | not_probed | - | - | 262144 | yes | 2026-10-31 |
| openrouter | `poolside/laguna-xs-2.1:free` | not_probed | - | - | 262144 | yes | 2026-10-31 |

## Changes

No earlier snapshot to compare with.

### Expiring within 14 days

- `openrouter|poolside/laguna-s-2.1:free`: 2026-10-31 (8 days)
- `openrouter|poolside/laguna-xs-2.1:free`: 2026-10-31 (8 days)

Expiry dates come from OpenRouter's `expiration_date` field. Groq publishes no expiry dates, so Groq models never appear here.
