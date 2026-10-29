# Godot 4.x

Open-source 2D and 3D engine. GDScript (Python-like) or C#. Scenes and
resources are text files (`.tscn`, `.tres`), so an agent can read, write and
diff them. A strong default for agent-built games.

## Install
- Download the single binary (and the export templates matching that
  version) from godotengine.org or GitHub releases. Pin the exact version
  (for example 4.3-stable) in CLAUDE.md. The C# build needs the .NET SDK.
- Headless: run the editor binary with `--headless`.

## Layout
```
project.godot
scenes/        main.tscn, level_*.tscn, ui/*.tscn
scripts/       sim/ (pure logic, no nodes where possible), game/ (node scripts)
data/          *.tres resources or JSON for content definitions
tests/         unit tests (GUT or gdUnit4), scenario scripts for screenshots
addons/        gut/ or gdUnit4/
```

## Running and testing
- Run a scene: `godot --path . res://scenes/main.tscn`.
- Run a script without a scene: `godot --headless --script res://tests/run.gd`
  (the script `extends SceneTree` and calls `quit(code)`).
- Unit tests: GUT (`godot --headless -s addons/gut/gut_cmdln.gd -gdir=res://tests -gexit`)
  or gdUnit4 (has its own CLI runner). Install either from the asset library
  or by copying it into `addons/`.
- Keep rules in classes that extend `RefCounted`, not `Node`, so tests can
  construct them without a scene tree.
- Physics needs the scene tree. For physics tests, instance the scene in a
  test `SceneTree` and step with `await get_tree().physics_frame`.
- Determinism: `seed(1234)` or a `RandomNumberGenerator` with a fixed seed.

## Screenshots and recording
- Under xvfb (not `--headless`, which has no renderer):
  `xvfb-run -a godot --path . --resolution 1920x1080 res://tests/shot.tscn -- --scenario=blast --seconds=2`.
  In the script: `await get_tree().create_timer(t).timeout`, then
  `get_viewport().get_texture().get_image().save_png("user://out.png")` and `get_tree().quit()`.
- Movie Maker mode: `--write-movie out.avi --fixed-fps 30` records
  deterministic frames (and audio) to AVI or PNG sequences, which is great
  for trailers.
- Read user arguments with `OS.get_cmdline_user_args()` (anything after `--`).

## Export
- Create presets in `export_presets.cfg` (an editor-made one can be
  committed), then run `godot --headless --export-release "Windows Desktop" build/Game.exe`.
- Export templates must match the editor version exactly.
- Web export needs cross-origin isolation headers for threads (or use a
  single-threaded build).

## Pitfalls
- `--headless` disables rendering: use xvfb for anything visual.
- `.import` folders and `.godot/` are generated: ignore `.godot/` in git, but
  commit the `*.import` files next to assets.
- Physics callbacks: use `call_deferred` or `set_deferred` to add or remove
  bodies and change collision shapes during signals.
- Typed GDScript (`var hp: float`) catches mistakes early, so prefer it.
- Large scene files merge badly. Split scenes and instance them.
