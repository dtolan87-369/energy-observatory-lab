# Observatory Operating Network

The Observatory uses different systems for different jobs. Do not ask one model or one app to do everything.

## Core roles

### ChatGPT / Astra
Use for:
- difficult scientific reasoning;
- architecture and synthesis across domains;
- adversarial review;
- connected-tool orchestration;
- final evidence-boundary checks.

### Codex
Use for:
- repository implementation;
- scripts, tests, refactors;
- repeatable software changes;
- code review / issue execution.

### Gemini
Use as:
- independent second opinion;
- broad candidate generation;
- adversarial critique;
- alternative mechanism / layout exploration;
- Google-native work where appropriate.

### Local Ollama models
Use for:
- cheap high-volume generation;
- first-pass classification;
- summarisation;
- duplicate clustering;
- boilerplate code / documentation;
- product / game candidate expansion.

Do not use local models as the sole judge of evidence or safety.

### OpenResearch
Pilot for:
- literature-grounded research-agent projects;
- experiment memory;
- hypothesis / experiment artifact tracking;
- local research runs using Codex / other supported agents.

Do not let it silently create a second Observatory taxonomy. Feed results back into existing evidence and Research Object systems.

### Atlas
Pilot as the multi-agent development cockpit.
Best fit:
- Codex + other coding agents on the same repo;
- checkpointing which agent changed what;
- shared local project memory;
- switching agents without losing implementation context.

Atlas complements GitHub; it does not replace GitHub as the canonical repository.

### Pi
Optional agent-runtime/toolkit.
Potentially useful for custom local agents and RPC automation, but overlaps with Codex/Atlas/OpenResearch.
Treat as HOLD until a concrete missing capability appears.
Run sandboxed because upstream documents that it otherwise inherits user/process permissions.

## Data / continuity

### Dropbox
Historical source archive and large-file source storage.
Do not duplicate it into GitHub.

### Google Drive / START HERE
Human-readable rolling programme continuation and current major decisions.

### GitHub
Working engineering record:
- code;
- scripts;
- CAD briefs;
- issues;
- tests;
- public-safe schemas/templates;
- release artifacts.

### Airtable
Structured candidate / product / quarry funnel.
Good for status, licence, evidence and commercial potential.

## Creation

- FreeCAD / Onshape — engineering CAD
- CadQuery / build123d / BOSL2 — machine-scale parametric geometry
- Blender — visual / organic / presentation geometry
- KiCad / PlatformIO — electronics and firmware
- Godot — original games / interactive science
- Python / Jupyter / PyMeasure / PyVISA / pySerial — measurement and analysis
- OpenCV / AprilTag — automated visual evidence and machine-native tooling

## Media / distribution

- Canva — Observatory visual language / carousels
- Descript — transcript / edit workflows when available
- OBS Studio — recording
- Kdenlive / FFmpeg — local video editing / conversion
- VoiceStudio — optional local voice/dubbing; only own/consented voices and respect AGPL obligations
- Metricool — scheduling / analytics
- vidIQ — YouTube topic/keyword/outlier work once a channel is authorized
- website — canonical public Observatory experience
- Stripe / Shopify — payment / store only after a product earns release

## Operating principle

> ROUTE EACH TASK TO THE CHEAPEST SYSTEM THAT CAN DO IT WELL, THEN ESCALATE ONLY WHEN THE DECISION NEEDS STRONGER REASONING.
