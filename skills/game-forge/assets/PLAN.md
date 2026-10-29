# <Title>: Plan

Source: `docs/GAME_BRIEF.md` (read it first). This file records what was
decided, how the game is built and in what order. Update it when a decision
changes; never silently diverge from it.

## Summary

<One paragraph: the game, the player, the first playable version.>

Riskiest assumptions:
1. <...>
2. <...>
3. <...>

## Decision log

| # | Decision | Choice | Why | Brief ref |
|---|---|---|---|---|
| D1 | Engine / framework | <e.g. Godot 4.3, GDScript> | <runs headless here, exports to all targets in 3.1, user knows Python-like syntax> | 3.1, 3.3 |
| D2 | Language | | | |
| D3 | Rendering (2D/3D, resolution, scaling) | | | 3.4, 8.3 |
| D4 | Physics (engine built-in / custom / none; units) | | | 5.3 |
| D5 | Input handling and rebinding | | | 3.2, 10.3 |
| D6 | Audio (library, mixing, sourcing) | | | 9.x |
| D7 | UI approach | | | 10.x |
| D8 | Save format and versioning | | | 12.1 |
| D9 | Art pipeline and sources | | | 8.2 |
| D10 | Audio pipeline and sources | | | 9.4 |
| D11 | Test, screenshot and build tooling | | | 3.6 |
| D12 | Every `DECIDE` from the brief | | | |

## Architecture

```
<directory tree of the planned project>
```

- **Main loop**: <fixed timestep for simulation at N Hz, rendering at display rate, interpolation or not>
- **Simulation vs presentation**: <which modules never touch rendering or audio, so tests can run them headless>
- **State ownership**: <who owns world state, how entities are created and destroyed, scene graph or ECS>
- **Data**: <content defined as data files or tables; where tunable numbers live>
- **Saving**: <what is serialised, format, version field, migration>
- **Debug modes**: `test`, `smoke`, `shot`, `build` (exact commands in CLAUDE.md)

## Milestones

Each milestone is a playable build. "Done" means its checks pass and the
user has played it.

### M0: Scaffold
- Player can: launch the game and quit.
- Checks: test, smoke, shot and build commands all run; CI (if any) green.

### M1: Vertical slice
- Player can: <one complete core loop, start to finish, rough art>
- Checks: <tests for the rules involved; a screenshot of each screen; smoke drives one full loop>

### M2: <...>
- Player can:
- Checks:

### M3: Content and polish
### M4: Release candidate

## Risks and experiments

| Risk | Why it matters | Cheapest experiment | When |
|---|---|---|---|
| | | | |

## Open questions

- <anything the brief left open that doesn't block M0/M1>
