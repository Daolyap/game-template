# Architecture for games an agent can build and verify

These patterns hold across engines. The engine files say how each maps onto
a particular engine.

## Separate simulation from presentation

The single most useful structural decision. Split the code into:

- **Simulation**: world state, rules, physics, AI, damage, scoring, saving.
  No drawing, no audio, no reading the mouse directly. Given the same inputs
  and seed, it produces the same state.
- **Presentation**: rendering, animation, particles, audio, camera, UI. It
  reads simulation state and turns it into pixels and sound.
- **Input**: maps devices to *intents* ("jump", "aim at x, y", "fire") that
  the simulation consumes. Tests feed intents directly.

This lets tests run the game headless at thousands of steps per second,
lets you replay a bug from a seed and an input log, and keeps rendering
changes from breaking rules.

Events flow from simulation to presentation ("entity 12 took 30 damage at
x, y") through a queue or callback. The presentation decides how that looks
and sounds.

## The main loop

Use a **fixed timestep** for simulation (60 or 120 Hz) and render at the
display rate:

```
accumulator += min(frame_dt, 0.1)        # clamp: a long hitch must not spiral
while accumulator >= STEP:
    simulate(STEP)
    accumulator -= STEP
render(alpha = accumulator / STEP)        # optional interpolation
```

Fixed steps make physics stable and tests reproducible. Slow motion scales
how much time is added to the accumulator, not the step size. Pausing stops
adding time, but still renders and handles UI.

## Entities and state

Pick one model and stay consistent:

- **Scene tree / nodes** (Godot, Unity GameObjects): natural in those
  engines. Keep rules in plain scripts or classes that tests can construct
  without a scene where possible.
- **Entity-component-system** (Bevy, or a hand-rolled one): good for many
  similar things (bullets, particles, crowds).
- **Data-driven entity definitions**: whatever the runtime model, define
  content (weapons, enemies, items, levels) as data: a table, JSON or
  resource file with a few hooks for behaviour. Adding content then means
  adding data, a smoke test can spawn every definition, and balance numbers
  live in one place.

Rules for state:

- One owner per piece of state. The world owns entities; entities own their
  parts.
- Never create or destroy physics bodies inside physics callbacks (Box2D,
  PhysX and Rapier all forbid or punish it). Queue the change and apply it
  after the step.
- Give every entity a stable id. Save files, replays and network messages
  refer to ids, not object references.

## Units and numbers

Pick a unit system on day one and write it in CLAUDE.md, e.g. "1 m = 64 px;
kg; s". For grounded games, use real values (gravity 9.81 m/s², a person
75 kg, a pistol round 350 m/s); tuning becomes reasoning instead of
guessing. For stylised games, still keep units consistent and put every
tunable in one data file.

## Randomness

- One seeded generator for anything that affects gameplay.
- A separate generator for cosmetic randomness (particle jitter, which
  footstep sample plays), so changing visuals never changes test results.
- Tests set the seed explicitly.

## Saving

- Serialise simulation state only (positions, velocities, health,
  inventory, ids, held-item relationships), never presentation objects.
- Put a `version` field in every save and write a migration when the format
  changes.
- Watch for serialiser quirks. One common trap: a JSON encoder that treats
  any table with a `[1]` key as an array, so a table that mixes array and
  hash keys loses data.
- Round-trip test: save, load, save again; the two files must match. Also
  test that relationships survive (an item a character holds must still be
  held after loading).
- "Undo" is often cheapest as a save snapshot plus load.

## Input

- Map raw input to actions in one place, so remapping and gamepad support
  are data changes.
- Buffer jumps and attacks for a few frames, and allow coyote time on
  platform edges. These are what make controls feel responsive.

## UI

- Immediate-mode UI (draw and handle input each frame) is quick to build and
  easy to test in code-first engines. Engine UI systems (Godot Control,
  Unity UI Toolkit) are better for complex menus.
- Pre-render anything expensive (icons, text atlases) at load time, outside
  the frame's drawing state.
- Group related controls, put destructive actions apart and in a warning
  colour, and make sure text never truncates silently.

## Performance

- Profile before optimising. Most engines have a profiler, so use it.
- Typical costs: too many physics bodies, per-frame allocation (garbage
  collection hitches), overdraw from big translucent sprites, re-uploading
  textures, and expensive work inside per-entity loops.
- Cache drawn art for static things (render once to a texture), and cap
  particle counts.
- Add a performance test: spawn N of the heaviest thing and assert the step
  time stays under budget.
