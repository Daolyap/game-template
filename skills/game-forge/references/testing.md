# Making the game testable and visible to you

You can't watch the game the way a player does, so build the senses you
need into it: modes that run it headless, drive it with scripted input,
render frames to images and record clips. Add these in phase 2, before
features. Every hour spent here saves days of guessing.

## The four modes

Expose them as command-line flags (or engine-specific equivalents) and
list the exact commands in CLAUDE.md.

### 1. `test`: headless simulation tests

- Runs without a window or audio. In LÖVE, `conf.lua` disables the window,
  graphics and audio modules when `--test` is passed; in Godot, use
  `--headless`; for Pygame, set `SDL_VIDEODRIVER=dummy`; for web, run the
  logic under Node.
- Fixed seed per test, so results are deterministic.
- A tiny runner is enough: a list of named test functions, each given a
  fresh world, reporting PASS or FAIL with timing and a short detail line.
  Allow filtering by name (`TEST=reload`).
- Test behaviour in game terms: "a 9 mm round to the chest at 5 m doesn't
  penetrate a steel plate", "the player can't jump twice without
  double-jump", "a save and load keeps held items in hand".
- Print the measured number in the detail line ("damage 3065", "head 8°
  nod"). When a test fails, you see by how much.
- Include a "spawn everything and simulate" test: it catches broken content
  definitions.

### 2. `smoke`: drive the real game

- Starts the real game with its UI and runs a script of inputs: click
  buttons, open menus, spawn things, drag them, press keys, save and load.
  Check results after each step (`check(cond, "pistol is held")`) and print
  a list of passes.
- Runs under a virtual display when there's no screen:
  `xvfb-run -a <command>`. Audio can use a null driver
  (`ALSOFT_DRIVERS=null` for OpenAL, `SDL_AUDIODRIVER=dummy` for SDL).
- Put the pointer where the script clicks, as a player would. A drag that
  starts with the mouse elsewhere yanks things across the screen and causes
  failures that aren't real.
- Make the smoke test exit non-zero on failure so it can gate commits and CI.

### 3. `shot`: render a scenario to an image

```
<game> --shot out.png <scenario> <seconds> [zoom] [camera x y] [hideui]
```

- Scenarios are small scripts: spawn things, set the camera, trigger
  events. Keep them in one file (`tests/shots`).
- Simulate to the requested time with fixed steps, render one frame and save
  it as PNG.
- Then **look at the image** with your image-reading tool. Check what you
  changed, and also scan for collateral damage: overlapping UI, truncated
  text, art in the wrong place, missing textures.
- Crop and zoom into the area of interest when details are small.
- Render UI shots at more than one window size (1280×720 and 1920×1080) to
  catch layout bugs.

### 4. `record`: film a scenario

```
<game> --record out.mp4 <scenario> <seconds> [fps] [--size WxH]
```

- Advance the scenario by exactly one frame per captured frame
  (`dt = 1/fps`), grab the frame, and pipe raw RGBA frames into ffmpeg
  (`-f rawvideo -pix_fmt rgba -s WxH -r FPS -i -`).
- A scenario can return a `tick(t, dt)` timeline function that moves the
  camera along eased keyframes, triggers events at set times and changes the
  time scale for slow motion.
- To review a clip without watching it, tile frames into a contact sheet:
  `ffmpeg -i clip.mp4 -vf "fps=1,scale=480:-1,tile=4x3" -frames:v 1 sheet.png`.
- For sound, log every sound the game starts during recording (film time,
  sample file, volume, pitch, pan) to a JSON file next to the clip. Then mix
  the soundtrack offline with numpy and mux it in with ffmpeg. This works
  even where there's no audio device.

## Verifying audio without speakers

- Check that every sound class referenced in code has files (a smoke check).
- Measure loudness of sample families (RMS of the loud part) and normalise
  so a footstep doesn't drown out a gunshot.
- Plot waveforms or spectrograms to PNG to check onsets, clipping and
  length.
- Render a short preview mix (a burst of shots, a reload) to MP3 and send it
  to the user to judge.

## CI

If the repo is on GitHub, add a workflow that installs the engine and runs
`test` and `smoke` (under xvfb) on every push. Keep it fast; skip heavy
performance tests or mark them.

## What you still can't verify

Feel (weight, timing, satisfaction), how sound comes across on real
speakers, controller rumble, and performance on the user's hardware all need
a human. Say so, and tell them exactly what to try.
