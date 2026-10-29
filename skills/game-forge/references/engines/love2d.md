# LÖVE (love2d) 11.x

Lua 2D framework with Box2D physics, OpenAL audio and a simple graphics API.
It has no editor: everything is code, which suits agents well.

## Install
- Linux: `apt install love` (check `love --version` says 11.5), or the
  AppImage from love2d.org. Windows/macOS: installers on love2d.org.
- Lua version: LuaJIT (Lua 5.1 semantics).

## Layout
```
main.lua        -- parses args (--test, --smoke, --shot, --record), boots modes
conf.lua        -- window settings; disables window/graphics/audio for --test
src/sim/        -- simulation (no love.graphics / love.audio)
src/game/       -- input, UI, rendering, camera
src/content/    -- data-driven definitions
tests/run.lua   -- headless test runner; tests/test_*.lua
tests/smoke.lua -- scripted UI run; tests/shots.lua -- screenshot scenarios
```

## Headless tests
`conf.lua` can read the arguments:
```lua
function love.conf(t)
  local test = false
  for _, a in ipairs(arg or {}) do if a == "--test" then test = true end end
  if test then
    t.window = false
    t.modules.graphics, t.modules.window, t.modules.audio = false, false, false
  end
end
```
In `love.load`, run the tests and `love.event.quit(failed > 0 and 1 or 0)`.
Set the seed with `love.math.setRandomSeed(1234)` before each test.

## Smoke and screenshots
- `xvfb-run -a love . --smoke`, with `ALSOFT_DRIVERS=null` for audio.
- Screenshot: `love.graphics.captureScreenshot(function(img) ... img:encode("png") ... end)`
  runs at the end of the frame; write the PNG and quit inside the callback.
- Set the window size per run (`love.window.setMode(w, h)`) to render
  1920×1080 store shots.
- Recording: one fixed update per draw, capture each frame and write
  `img:getString()` (RGBA) to an `io.popen("ffmpeg ... -f rawvideo -pix_fmt rgba ...", "w")` pipe.

## Physics (love.physics = Box2D)
- Choose a meter scale: `love.physics.setMeter(60)`, and use it everywhere.
- Fixed step (for example 1/120 s) with an accumulator.
- Never create or destroy bodies or joints in `beginContact`/`preSolve`
  callbacks: queue them. Errors inside callbacks are easy to lose, so wrap
  them in pcall and rethrow after `world:update`.
- Mouse joints: tune frequency and damping by mass ratio; wheel joint springs
  by load per wheel.

## Audio
- `love.audio.newSource(path, "static")` for effects and `"stream"` for
  music or ambience; `Source:clone()` for overlapping plays.
- EFX reverb and filters: `love.audio.setEffect`, `Source:setFilter`
  (check `love.audio.isEffectsSupported()`).

## Build
- `.love` = zip of the project root (`main.lua` at the top level).
- Windows: `cat love.exe game.love > Game.exe`, then ship it with love's
  DLLs and licence in a zip.
- macOS: copy the `.love` into `love.app/Contents/Resources/`, then edit
  Info.plist.
- Linux: AppImage via love's appimage tooling.

## Pitfalls
- Multiple returns are truncated unless they're the last argument.
- `love.graphics` state (colour, blend mode, line width, scissor) leaks
  between draws: reset what you change.
- Canvases: render them outside the active scissor and transform; set
  `dpiscale` explicitly for crisp sprites.
- The "add" blend mode doesn't accumulate destination alpha.
- `love.math.random` is the global generator. Use
  `love.math.newRandomGenerator` for cosmetic randomness.
