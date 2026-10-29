# Unity (2022 LTS / Unity 6)

C# engine with the broadest platform reach, consoles included. Heavy to
install and needs licence activation, which is usually the blocker in a
cloud container. Check early whether you can run it here.

## Install and licence
- Unity Hub, or headless editor installs via `unityhub --headless install`.
  On Linux CI, the `unityci/editor` Docker images (GameCI) are the
  practical route.
- Activation: Personal licences need a `.ulf` file or serial; GameCI documents
  the steps. Without activation, batch mode fails. If you can't activate,
  tell the user and use the "plain C# core" approach below.

## Layout
```
Assets/Scripts/Sim/       plain C# (no MonoBehaviour), in its own assembly definition
Assets/Scripts/Game/      MonoBehaviours, UI, rendering glue
Assets/Data/              ScriptableObjects for content definitions
Assets/Tests/EditMode/    NUnit tests of Sim
Assets/Tests/PlayMode/    tests that load scenes and step frames
Packages/manifest.json
ProjectSettings/
```
Commit `Assets/`, `Packages/` and `ProjectSettings/`; ignore `Library/`,
`Temp/`, `Logs/`, `Builds/` and `UserSettings/`. Use text serialisation
with visible meta files (the default), and Git LFS for big binaries.

## Testing
- Unity Test Framework (NUnit):
  `unity -batchmode -nographics -projectPath . -runTests -testPlatform EditMode -testResults results.xml`
  (and `-testPlatform PlayMode`).
- A plain C# core can also be unit tested with `dotnet test` outside Unity
  entirely: put Sim in a netstandard class library that Unity references.
  You can always verify that part from here.
- Determinism: `UnityEngine.Random.InitState(seed)` or `System.Random(seed)`
  in Sim. Physics: Unity physics isn't bit-deterministic across machines, so
  test outcomes with tolerances.

## Screenshots and builds
- `ScreenCapture.CaptureScreenshot` needs a graphics device: run batch mode
  without `-nographics`, under xvfb on Linux.
- Builds: `unity -batchmode -quit -projectPath . -executeMethod BuildScript.Build`
  with a static `BuildScript` using `BuildPipeline.BuildPlayer`. Each target
  needs its build-support module installed.

## Pitfalls
- Domain reload and script compilation are slow, so batch changes.
- Scene and prefab YAML merges badly: one owner per scene, prefabs for
  reuse.
- Don't put game rules in `Update()` of many MonoBehaviours; drive the
  simulation from one manager with a fixed step (`FixedUpdate` or your own).
- Licence terms change; check the current Unity runtime fee and licence
  policy with the user for commercial projects.
