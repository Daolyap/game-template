# Unreal Engine 5

C++ and Blueprints; top-end 3D, consoles, large teams. Installs are tens of
GB and builds are slow. From a cloud container it's rarely practical to run
the editor, so plan verification with the user.

## When to choose it
High-fidelity 3D, console targets, the user already knows Unreal, or
specific features (Nanite, Lumen, MetaHumans). Otherwise prefer Godot or
Unity for an agent-led project.

## Setup
- Epic Games Launcher (Windows/macOS), or build from source on Linux
  (requires linking a GitHub account to Epic to access the repository).
- Projects: `.uproject`, `Source/<Game>/` (C++ modules), `Content/`
  (binary `.uasset` files: use Git LFS or Perforce), `Config/`.

## Testing
- Automation framework: `UnrealEditor-Cmd <Project>.uproject -ExecCmds="Automation RunTests <Filter>;Quit" -unattended -nullrhi -nosplash -log`.
- Functional tests (`AFunctionalTest` actors) run in maps.
- Keep game rules in plain C++ classes (or a separate module) that you can
  unit test without the editor.

## Screenshots and builds
- `HighResShot 1920x1080` console command, or automation screenshot tests
  (require a real RHI, not `-nullrhi`).
- Builds: `RunUAT BuildCookRun -project=... -platform=Win64 -clientconfig=Shipping -cook -stage -pak -archive -archivedirectory=build/`.

## Working with the user
- Assets are binary and edited in the editor. Expect the user to do editor
  work (level layout, materials), while you write C++ and data and review
  their changes through logs, screenshots and automation results.
- Agree on a loop: you push code, they build and run it, they send logs or
  screenshots, you iterate.

## Pitfalls
- Hot reload is unreliable; use Live Coding or restart the editor.
- UPROPERTY/UFUNCTION macros are required for reflection; missing them
  silently drops data from saves and Blueprints.
- Blueprint-heavy logic can't be diffed or reviewed as text. Keep core rules
  in C++.
