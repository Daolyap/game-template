# Art and audio: sourcing, licences, pipelines

Players judge a game by how it looks and sounds before they notice anything
else. Agents tend to under-invest here: flat shapes, a few synthesized beeps.
Use real material where you can, process it consistently, and let the user
choose the important pieces.

## Licences, in order of ease

| Licence | Can you ship it in the game? | Attribution? | Notes |
|---|---|---|---|
| CC0 / public domain | Yes | No (credit anyway) | Best default |
| CC-BY | Yes | Yes, in credits | Track author and link |
| CC-BY-SA | Yes, but derived assets inherit SA | Yes | Avoid for code-adjacent assets |
| CC-BY-NC | Only if the game is never sold | Yes | Avoid for anything commercial |
| Royalty-free bundles (e.g. Sonniss GDC) | Yes, inside a game | Usually no | Usually can't be redistributed as a standalone library; check before putting raw files in a public repo |
| Bought asset packs | Usually, per the store's licence | Varies | Read the licence; often no redistribution of source files |
| AI-generated | Depends on the tool's terms | No | Ask the user first: some people object to it on principle |

Keep a `docs/CREDITS.md` (or `assets/CREDITS.md`) table: asset, source URL,
author, licence. Add the row when you add the asset. Never use an asset
whose licence you couldn't confirm.

## Where to find things

**Art and textures**
- Kenney (kenney.nl): huge CC0 2D and 3D packs, consistent style.
- OpenGameArt (opengameart.org): mixed licences; filter by CC0.
- ambientCG, Poly Haven: CC0 PBR textures, HDRIs and models; scans of real
  surfaces work well as overlay detail even in 2D.
- Quaternius, KayKit: CC0 low-poly 3D models.
- itch.io asset packs: free and paid, check each licence.

**Sound**
- Freesound (freesound.org): filter by CC0. Rate-limits aggressive
  downloading, so space requests out.
- OpenGameArt: CC0 sound packs (impacts, foley, ambience).
- Kenney audio packs: CC0 UI and impact sounds.
- Sonniss GDC Game Audio Bundles: tens of GB of professional,
  royalty-free recordings (guns, explosions, foley, ambience). Excellent
  quality; mind the redistribution caveat above.
- The Free Firearm Sound Library (OpenGameArt): CC0 field recordings.

**Music**
- Free Music Archive and OpenGameArt (check licences), Kevin MacLeod
  (CC-BY), or commission. Ask the user: music sets tone more than anything.

**Fonts**
- Google Fonts (OFL licence) are safe to bundle.

## Pipelines: scripts, not hand-editing

Write a build script per asset type (`scripts/make_sfx.py`,
`make_textures.py`) that downloads sources into a cache, processes them and
writes game-ready files. Reproducible, reviewable and easy to rerun when a
choice changes.

Sound processing (Python, numpy and ffmpeg):
- Decode with ffmpeg to float32 at one sample rate.
- **Slice multi-shot recordings at their onsets** (envelope peaks), keeping
  each event's natural tail.
- **Normalise by loudness of the loud part (RMS), not peak**, per family, so
  sounds within a class sit at the same perceived level.
- For impacts that should hit harder, soft-limit (tanh) the transient, then
  level the body.
- For bursts where each shot masks the next (machine guns), splice each
  shot's attack onto the clean tail of the burst's last shot. You get
  variants that repeat naturally at the gun's rate.
- Loops: crossfade the end into the start.
- Mid/side recordings: use the mid channel as the mono mix.
- Export several variants per sound (`name_1.ogg ... name_n.ogg`); the game
  picks one at random and adds about ±5% pitch variation.
- Encode to Ogg Vorbis (mono for positional effects, stereo for ambience and
  music).
- Re-running the script re-encodes everything. Restore unchanged files from
  version control to avoid noisy diffs.

In-game audio behaviour worth building:
- A mix level per sound class (gunshots above footsteps), set in one table
  and exposed in the tuning panel.
- Positional panning and distance attenuation; a low-pass filter for
  distance; speed-of-sound delay for far explosions in large worlds.
- Pitch follows the time scale (slow motion sounds deep).
- A voice cap: when it's reached, the oldest voice is stopped.
- Ambience well under the effects. Users notice when it's too loud.
- Reverb per environment where the engine supports it (OpenAL EFX,
  FMOD/Wwise, Godot audio buses).

Art processing:
- Pack sprites into atlases, and keep source files (Aseprite, Krita,
  Blender) in the repo or a linked store.
- For procedural or vector art, build detail in layers (base shape, shading,
  edge highlights, texture overlay). Silhouettes made of "a few shapes stuck
  together" read as placeholder art.
- Bake static art to textures at load (and at device pixel ratio) for speed
  and crispness.

## Letting the user choose

For any asset the user cares about (weapon sounds, main character, music),
build a review page:

- an HTML file listing candidates with play buttons (or image cards), labels
  with source and licence, and a "pick" toggle stored in localStorage;
- candidates matched for loudness (or size) so the comparison is fair;
- the current in-game version included as a baseline.

Publish or send it, ask for picks, then integrate exactly what they chose and
render a short preview (an MP3 of a burst and a reload, or a screenshot) for
confirmation.
