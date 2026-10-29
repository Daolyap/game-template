# Choosing an engine or framework

Pick the engine that satisfies the brief's hard constraints, that you can
**run, test and screenshot in your own environment**, and that the user can
live with long term. If the user named one, use it unless it truly can't
meet a hard constraint; then explain the conflict and let them choose.

## Step 1: hard constraints from the brief

| Brief says | Implication |
|---|---|
| Consoles (Switch, PlayStation, Xbox) | Unity or Unreal have the smoothest console paths; Godot via third-party porting partners; needs a developer account and devkit either way |
| Web browser primary | Phaser, PixiJS, Three.js/Babylon.js, or Godot/Unity web export (bigger downloads, slower start) |
| Mobile primary | Godot, Unity, Defold, or web; LÖVE runs on Android/iOS but tooling is rougher |
| High-end 3D, photorealism | Unreal, or Unity (HDRP) |
| Stylised 3D, small team | Godot 4, Unity |
| 2D, physics sandbox or simulation | LÖVE (Box2D), Godot, Unity 2D, Bevy (Rapier) |
| 2D pixel art | Godot, LÖVE, Phaser, MonoGame, Pygame (small games) |
| Must be open source / no licence fees | Godot, LÖVE, Bevy, Phaser, Pygame, MonoGame, Defold |
| User wants to learn a language | Python → Pygame or Godot (GDScript); C# → Godot (C#), Unity, MonoGame; JS/TS → Phaser; Rust → Bevy; Lua → LÖVE, Defold; C++ → Unreal |
| Game jam (48–72 h) | Whatever the user already knows; otherwise Godot or LÖVE (fast iteration) |

## Step 2: can you verify it here?

You can't judge a game you can't run. Check before committing to an engine:

- Is it installable in this environment (package manager, a direct download,
  or a container)? Try it: install it and run a hello-world before writing
  the plan.
- Can it run without a display (headless mode, or under `xvfb-run`)?
- Can you capture a frame to a PNG from a script?
- Can you build for the primary target from this OS?

| Engine | Headless tests | Screenshot from script | Build from Linux | Notes |
|---|---|---|---|---|
| Godot 4 | `godot --headless` (GUT or gdUnit4 for tests) | `get_viewport().get_texture().get_image().save_png()` under xvfb | Windows, Linux, Web, Android (export templates); macOS/iOS export but need Apple tools to sign | Very good fit for agents: text scene files, single binary |
| LÖVE 11 | Own test mode with `t.window = false` in conf.lua | `love.graphics.captureScreenshot` under xvfb | `.love` file plus fused Windows exe; macOS app by zip; Linux AppImage | Tiny, fast, Lua; you write more yourself |
| Phaser / web | Node test runner on pure logic; Playwright for the browser | Playwright `page.screenshot()` | Static site anywhere | Easiest to share (a link) |
| Pygame | `SDL_VIDEODRIVER=dummy` | `pygame.image.save(screen, ...)` | PyInstaller per OS (build on each OS) | Good for small games and learning |
| Bevy | `cargo test`; `MinimalPlugins` for headless | Screenshot plugin under xvfb | Cross-compiling needs extra toolchains | Fast, ECS-native, long compiles |
| Unity | `-batchmode -nographics -runTests` | `ScreenCapture` in batch mode (needs graphics, not `-nographics`) | Needs a Unity licence activated in this environment | Heavy install; licence activation is often the blocker |
| Unreal | `-nullrhi` automation tests | High-res screenshot command | Large install, slow builds | Usually impractical to verify from a cloud container |
| MonoGame | `dotnet test` on logic | Render to RenderTarget2D and save | `dotnet publish` per runtime | C#, code-first |
| Defold | Limited headless | Under xvfb | Bob the builder (Java) | Lua, small builds, good for mobile/web |

If the best engine for the brief can't be verified here (typically Unity or
Unreal in a cloud container), say so, and pick one:

1. Keep all game rules in plain, engine-independent code you *can* test
   (C# class library, C++ module), with a thin engine layer the user tests.
2. Ask the user to run builds and send screenshots or logs. Agree that
   cadence in the plan.
3. Propose a verifiable engine instead, and explain the trade-off.

## Step 3: write it down

Record the choice in PLAN.md's decision log with the reason, the version
(pin an exact one) and what you verified (installed, ran headless,
screenshot, built). Then read `references/engines/<engine>.md`.

If no file exists for the chosen engine, research it before scaffolding:
the official docs for headless running, testing frameworks, screenshot
capture and export. Write your own notes into the game's CLAUDE.md in the
same shape as the engine files here.
