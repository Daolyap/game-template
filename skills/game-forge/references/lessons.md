# Field notes

Lessons from building a large 2D physics sandbox (LÖVE, Box2D) with an
agent over many sessions. Most generalise to any engine. Read once before
the scaffold, and again when something odd happens.

## Process

- **The user is the judge of feel and sound, and they are picky.** Several
  rounds went into gunshots ("mid", "no bass"), body impacts ("weird") and
  how floppy arms were. What ended the loops: candidate review pages for
  sounds, and a live tuning panel whose "copy changes" output the user
  pasted back.
- **Batches of feedback mix bugs, taste and wishes.** Make a task list from
  each batch, do the clear things, ask about the ambiguous ones with a
  recommendation, and report what was done item by item.
- **Write preferences down.** "Timers only on grenades, dynamite and pipe
  bombs", "ambience barely noticeable", "athletes shouldn't all have the same
  skin tone": each went into the code or notes so it stayed fixed.
- **Look at every visual change.** Wound textures that looked "goofy", truncated
  inspector labels and a gun held at the wrong angle were obvious in a
  screenshot and invisible in code.
- **Smoke tests catch what unit tests can't**: a person dying off-screen
  because a scripted drag yanked them; a context menu failing because the
  target had moved.

## Simulation

- **Never create or destroy bodies or joints inside physics callbacks.**
  Defer them to after the step. Errors inside callbacks can also be swallowed:
  catch them and rethrow after the step.
- **Damage from pre-collision approach speed**, not contact impulse, so
  resting contact never hurts and stacking stays stable.
- **Joint tearing and load fractures scale with body weight**, so the same
  rule works for a cat and a tank.
- **Explicit spring torques (PD control) on very light chains go unstable**
  (a head on a neck nodding wildly). Use the engine's motors for light
  links, or size gains by the subtree's inertia.
- **Mouse-drag joints**: stiffness depends on the dragged mass. Scale
  frequency and damping by sqrt(holder mass / grabbed mass), cap it, and
  remember a held item drags its holder.
- **Box2D wheel springs are sized by the wheel's mass**, so scale frequency
  by the load per wheel.
- **Time scaling for one entity** (a speedster) is hard: velocities scale by
  the rate, forces by its square; contacts between differently-scaled bodies
  need rescaling, and switching rates must ramp over many steps because of
  solver warm-starting.
- **Structures made of separate bodies** need load paths and no overlaps,
  or they explode or collapse at spawn. Start them static and release them
  when damaged.
- **Projectiles you can watch** (stepped rounds instead of instant
  raycasts) are what make slow motion spectacular. Keep instant hits as an
  option for tests.
- **Energy-based penetration** (energy against tissue resistance per unit
  depth, plus bone cost, capped by blade length) gave believable stabbing,
  skewering and lodging from a few constants.

## Engine and language traps (LÖVE / Lua; similar ones exist elsewhere)

- Lua truncates multiple return values that aren't the last argument:
  `f(a, body:getLocalPoint(x, y), m)` passes only x.
- A local declared inside a function shadows an outer one of the same name.
  A capture table went empty because `files` was also a loop local.
- "Add" blend mode doesn't accumulate destination alpha.
- Render canvases outside the frame's scissor or transform state.
- Cosmetic randomness must use its own generator, or visuals change test
  outcomes.
- Killing processes by a pattern can match your own shell (`pkill -f`).
- Rate-limited asset sites (Freesound) return 403 when hit too fast.

## Presentation

- Particles, blood and other effects update in the game loop, not the
  physics step. Tests that need them must update them explicitly.
- Soft things (smoke, glows, stains, bruises) look far better as real or
  procedural sprites than as translucent circles.
- Real texture scans as a world-space overlay lift flat vector art a lot.
- Detailed wounds read better as layers (skin edge, fat, muscle, cavity,
  organs, bone) than as a red blob.
- UI: group top-bar actions, keep destructive actions apart (bottom-left in
  a warning colour), fit text to its box, size panels to their content.

## Store media

- Showcase scenes as scripts, with a camera timeline and slow-motion beats,
  rendered at 1080p30 through ffmpeg.
- People in a line will shoot each other in the back. Stage gunfights
  side-on with one shooter, or at different heights.
- Heavy targets (cars) soak up rounds, so the impact you staged never shows.
  Check contact sheets before the final render.
- Capture sounds during recording and mix offline; a silent trailer loses
  half its impact.
