# Pygame (pygame-ce)

Python 2D library. Good for small games, learning projects and jams. Prefer
`pygame-ce` (the actively maintained community edition; same API).

## Install
`python3 -m venv .venv && . .venv/bin/activate && pip install pygame-ce`
(optionally pymunk for physics, numpy for audio processing).

## Layout
```
game/__main__.py   arg parsing: --test is pytest; --smoke, --shot <scenario>
game/sim/          pure logic (no pygame.display)
game/view/         rendering, UI, audio
game/content/      data definitions
tests/             pytest tests
```

## Headless tests and screenshots
- Unit tests: `pytest`, on `game/sim` only, with `random.Random(seed)`
  instances (not the global `random`).
- No display: set `SDL_VIDEODRIVER=dummy` and `SDL_AUDIODRIVER=dummy`
  before `pygame.init()`. Rendering still works to an off-screen surface, so
  screenshots don't need xvfb:
  `pygame.image.save(screen, "out.png")` after drawing the scenario.
- Smoke: run the main loop with scripted events posted via
  `pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=..., button=1))`.

## Main loop
`clock.tick(fps)` returns milliseconds since the last frame; feed it into a
fixed-step accumulator for the simulation.

## Physics
pymunk (Chipmunk2D) for rigid bodies. Same rule as Box2D: don't add or remove
bodies inside collision callbacks; use post-step callbacks
(`space.add_post_step_callback`).

## Build
PyInstaller (`pyinstaller --onefile --windowed game/__main__.py`) on each
target OS (it doesn't cross-compile). Web: `pygbag` packages pygame for the
browser (asyncio main loop required).

## Pitfalls
- Performance: Python is slow per entity. Keep entity counts modest, and use
  sprite groups and dirty rects, or numpy for bulk maths.
- `convert()` / `convert_alpha()` every loaded image, or blitting is slow.
- Sound: `pygame.mixer` has a limited number of channels; set
  `pygame.mixer.set_num_channels(32)`.
