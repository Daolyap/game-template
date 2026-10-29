# Release: builds, store pages, trailers

## Builds

- One script (`scripts/build.sh` or an engine export preset) produces every
  target build into `build/`, which is ignored by git.
- Stamp the version (from git describe or a VERSION file) into the build and
  show it on the title screen. Bug reports need it.
- Per platform:
  - **Windows**: a zip with the exe and DLLs. For LÖVE, fuse the `.love`
    onto `love.exe`. Code signing avoids SmartScreen warnings but costs money.
  - **macOS**: an `.app` bundle; signing and notarisation need an Apple
    developer account and macOS. Without them, users must right-click → Open.
  - **Linux**: an AppImage or tar.gz; Steam handles most dependencies.
  - **Web**: a static folder (index.html plus assets). Test it served over
    HTTP, not opened from a file, and check load time.
  - **Android / iOS**: engine export plus signing keys; iOS needs Xcode on a
    Mac.
  - **Consoles**: platform developer programs, devkits and certification.
    Plan months ahead.
- Smoke-test each build: launch it, start a game, quit. Under xvfb for
  desktop builds where possible.

## Store media

Render store media from the game itself with scripted scenes (the `shot` and
`record` modes), so it stays honest and can be regenerated after changes:

- **Screenshots** (Steam wants at least 5 at 1920×1080): one feature per
  shot, the UI hidden except for a deliberate UI shot, staged at the
  most legible moment of the action.
- **Clips**: 5–12 s scenarios with a camera timeline and slow motion for the
  key beat. Mix the game's own sounds into them (see testing.md).
- **Trailer**: a title card, 6–10 captioned segments, then an end card.
  Overlay the captions with ffmpeg, fade between segments, carry the audio
  through, and loudness-normalise the result (`loudnorm=I=-16:TP=-1.5`).
  Lead with the most striking moment; keep it under 90 s.
- **Capsule art**: compose with Pillow from renders plus the logo, in each
  required size. For Steam: header 920×430, small 462×174, main 1232×706,
  vertical 748×896, library 600×900, hero 3840×1240, logo 1280×720.
- Keep the scripts in the repo (`scripts/store/`), and the output in
  `build/store/`.

## Before shipping

- Credits list complete and every asset licence confirmed (credits.md).
- No debug keys or cheat menus left enabled, unless they're intended.
- Settings persist; saves from the previous version load (or are migrated).
- The game handles a missing audio device, a resized window and alt-tab.
- Crash handler writes a log file the player can send.
- Ask the user before uploading or publishing anything.
