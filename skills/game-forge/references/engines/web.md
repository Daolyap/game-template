# Web games: Phaser, PixiJS, Three.js, plain canvas

Best when the brief says "play in a browser" or "send a link". TypeScript is
recommended.

## Stack choices
- **Phaser 3**: full 2D framework (scenes, arcade and Matter physics,
  tilemaps, audio, input).
- **PixiJS**: fast 2D renderer; bring your own game structure and physics
  (matter-js, planck.js for Box2D semantics, Rapier via WASM).
- **Three.js / Babylon.js**: 3D. Babylon is more batteries-included.
- **Plain canvas/WebGL**: for tiny games and jams.
- Tooling: Vite (`npm create vite@latest`) for dev server and bundling;
  Vitest for unit tests; Playwright for browser smoke tests and screenshots.

## Layout
```
index.html
src/sim/       pure TypeScript game logic (no DOM, no Phaser imports)
src/game/      scenes, rendering, input, audio
src/content/   data definitions
public/assets/ images, audio (served as-is)
tests/unit/    vitest specs on src/sim
tests/e2e/     playwright smoke and screenshot specs
```

## Testing
- Unit: keep `src/sim` free of browser APIs, so `vitest run` exercises rules
  in Node, seeded with a small PRNG (mulberry32, or `seedrandom`).
- Smoke and screenshots: Playwright launches Chromium headless; serve with
  `vite preview`, load `/?scenario=blast&t=2`, wait for a `window.__ready`
  flag the game sets, then `page.screenshot({ path })`. Drive input with
  `page.mouse` and `page.keyboard`.
- Expose a debug hook (`window.__game`) in dev builds for tests to step time
  and spawn things.
- Determinism: drive the loop with a fixed step and allow tests to call
  `step(n)` instead of using requestAnimationFrame.

## Audio
- Web Audio API (or Howler.js). Browsers block audio until a user gesture,
  so start the audio context on the first click or key.
- Prefer OGG plus an MP3 fallback (Safari), or AAC/M4A.

## Build and ship
- `vite build` writes `dist/`, a static site. Host on itch.io (zip upload),
  GitHub Pages, Netlify or Cloudflare Pages.
- Check total download size and first-load time; compress textures and
  audio.
- Desktop wrapper if needed: Electron or Tauri.

## Pitfalls
- High-DPI screens: size the canvas by `devicePixelRatio` for crisp
  rendering.
- Tab hidden means requestAnimationFrame pauses; clamp dt on return.
- Mobile: handle touch, orientation and the virtual keyboard; test on a real
  phone (ask the user).
- CORS: assets must be served from the same origin or with the right
  headers, and `file://` won't work.
