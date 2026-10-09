# Local AI

## Purpose

Use the local PC for high-volume, lower-cost work while preserving frontier models for difficult decisions.

Current workstation baseline:
- 16 GB system RAM
- NVIDIA GeForce GTX 1660 Ti
- 6 GB dedicated VRAM
- NVMe storage

## Initial workload class

Target small-to-mid quantized models first, roughly 4B–8B, and measure actual speed/quality before moving larger.

## Local tasks

Good first uses:
- classify/summarise archive subsets;
- generate many candidate mechanisms/game ideas;
- draft repetitive code/docs;
- cluster duplicates;
- produce first-pass product descriptions;
- compare candidate parameter sets.

Do not delegate final evidence judgments, high-risk engineering decisions or unsupported scientific claims solely to a local model.

## Benchmark set

Run the same three prompts on every candidate model:

1. Generate 30 Impossible Book page mechanisms under the current architecture.
2. Classify a sample of Observatory notes into existing categories without inventing new taxonomy.
3. Generate 10 machine-native connector concepts and state the trade-off behind each.

Record:
- tokens/s or response time;
- RAM/VRAM use;
- instruction-following;
- duplication rate;
- hallucinated claims;
- usefulness after human review.
