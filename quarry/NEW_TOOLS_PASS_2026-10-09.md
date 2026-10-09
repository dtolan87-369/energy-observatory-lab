# New Tools Pass — 9 Oct 2026

## High priority pilots

### OpenResearch — MIT
Local-first research-agent workspace supporting Codex and other agents, local models, literature sources, experiment logs and artifacts.

**Use:** pilot one bounded Observatory research question.  
**Guardrail:** results feed existing Research Objects / evidence; do not create a parallel taxonomy.

### Atlas — Apache-2.0
Source control / context layer for coding agents with checkpoints and shared local project memory.

**Use:** strong candidate for the coding workstation because the Observatory uses multiple agents.  
**Guardrail:** GitHub remains canonical remote source control.

### RuView — MIT
Wi-Fi CSI spatial sensing platform.

**Use:** potentially excellent Fields / Invisible Catalogue / Sixth Sense research lead using cheap ESP32-class sensing.  
**Guardrail:** health/vital-sign claims require independent validation. Do not present it as a medical device. Start with presence/motion/room-state measurements.

### VoiceStudio — AGPL-3.0
Local voice cloning/design/dubbing/transcription workflow.

**Use:** optional media production / narration.  
**Guardrail:** use only voices Daniel owns or has clear consent to use. Modified/network deployments carry AGPL obligations.

## Useful but not immediate

### Pi — MIT
Extensible agent harness with unified provider API and coding agent.

Useful if we later need a custom agent runtime. Current stack already has Codex + Atlas/OpenResearch candidates, so avoid adding complexity without a clear gap.

### MiroFish — AGPL-3.0
Multi-agent social simulation.

Could be useful for fictional audience / scenario exploration or game-world experiments, but **simulation output is not market prediction evidence**. High API consumption also makes it poor for the first low-credit stack.

### ASC — Apache-2.0
Fast Android APK analysis/decompilation.

Useful only if the Observatory develops/reviews Android apps or needs legitimate mobile reverse-engineering/security work. Not a core install now.

## Media / archive additions

### Docling — MIT
Strong candidate for local document/PDF extraction into the Observatory index.

### Playwright — Apache-2.0
High-value automated browser testing for the Observatory website: responsive checks, interaction regression, screenshots and repeatable acceptance tests.

### OpenRefine — BSD-style
Excellent archaeology/data-cleaning tool for messy tables, source inventories and normalized metadata while preserving originals.

### DuckDB — MIT
Excellent lightweight local query engine for CSV/Parquet experiment data and archive indices.

### OBS Studio — GPL-2.0
Local screen/camera capture.

### Kdenlive — GPL-3.0
Local non-linear video editor.

### FFmpeg — LGPL/GPL depending build
Media conversion, clipping, thumbnails and automated batch processing.

### Remotion — custom commercial terms
Programmatic video generation is useful, but inspect current licence before depending on it commercially.

## Rule

> ADD A TOOL ONLY WHEN IT CLOSES A SPECIFIC GAP IN AN ACTIVE LOOP.
