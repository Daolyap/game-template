# Bevy (Rust)

Data-driven ECS engine in Rust. Code-only (no editor), fast at runtime,
slow to compile. Good for systems-heavy games and simulations when the user
likes Rust.

## Install
`rustup` (stable toolchain), then add `bevy` (pin the minor version: the API
changes between releases). Linux needs `libasound2-dev`, `libudev-dev`, and
`libwayland-dev`/X11 dev packages. Physics: `bevy_rapier2d`/`bevy_rapier3d`
or `avian`.

## Speed up builds
- Enable `dynamic_linking` (Bevy feature) in dev, use the `lld` or `mold`
  linker, and set `opt-level = 1` for dev with `opt-level = 3` for
  dependencies in `Cargo.toml` profiles.

## Layout
```
src/main.rs        app setup, plugins, CLI modes
src/sim/           components, systems, resources (no rendering)
src/view/          rendering, UI, audio plugins
assets/            loaded by AssetServer
tests/             integration tests building an App with MinimalPlugins
```

## Testing
- Build an `App` with `MinimalPlugins` (no window), add the sim plugins,
  insert resources, call `app.update()` N times, then query the `World`.
- `cargo test` runs it. Seed RNG from a resource (`rand_chacha` with a fixed
  seed).
- Fixed timestep: run gameplay in `FixedUpdate` and set `Time<Fixed>` to
  60 or 120 Hz.

## Screenshots and recording
- `bevy::render::view::screenshot` (the `Screenshot` component or
  `ScreenshotManager`, depending on version) saves the primary window to a
  file. Run under xvfb with a real renderer (lavapipe/llvmpipe for software
  Vulkan if there's no GPU).

## Build
`cargo build --release` per target. Cross-compiling to Windows from Linux
needs `x86_64-pc-windows-gnu` plus mingw, or `cargo-xwin`. Web:
`wasm32-unknown-unknown` with `wasm-bindgen` or `trunk`.

## Pitfalls
- System ordering is parallel by default: use `.chain()` or explicit
  ordering where it matters.
- Despawning entities that other components reference: use `Option<Entity>`
  and check `world.get_entity`.
- Version churn: tutorials go stale fast. Check docs.rs for the pinned
  version.
