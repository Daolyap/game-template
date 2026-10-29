---
name: game-forge
description: End-to-end workflow for making a video game of any kind, in any engine (Godot, Unity, Unreal, LÖVE, Phaser/web, Pygame, Bevy, MonoGame or none), starting from a design brief the user fills in. Use this skill whenever someone wants to make, start, prototype, plan or continue building a game, or turn a game idea into a project, even if they only say "I have an idea for a game", "let's make a platformer", "game jam", or name an engine. Also use it when a game repo has a docs/GAME_BRIEF.md or docs/PLAN.md, or when asked to pick an engine, write a game design document, scaffold a game project, set up game tests, or package a game for release.
---

# Game Forge

You are about to build a game with someone, probably starting with no context
about them, their taste or their machine. Games fail in predictable ways when
an agent builds them: the agent starts coding before anyone has decided what
the game *is*, picks an engine it can't run or test, ships "programmer art"
nobody wanted, can't see or hear what it made, and drifts from the person's
taste because feel was never written down. This skill exists to prevent each
of those.

The work runs in phases. Each one ends with something written down in the
game's repo, so a later session (yours or another agent's) can pick up cold.

| Phase | Output in the repo | Gate to move on |
|---|---|---|
| 0. Initiate | `docs/GAME_BRIEF.md` filled in | `scripts/check_brief.py` reports no missing required answers, and the user confirms |
| 1. Plan | `docs/PLAN.md` (decisions, architecture, milestones), `CLAUDE.md` | User approves the plan |
| 2. Scaffold | Runnable skeleton with test, screenshot and build commands | Every command in CLAUDE.md works |
| 3. Build | Vertical slices, each verified | Milestone's acceptance checks pass and the user has played it |
| 4. Polish | Feel, audio, art pass, tuning | User signs off on feel |
| 5. Release | Builds, store media, credits | Builds launch on target platforms |

Work out which phase you're in before doing anything. If there is no brief,
you are in phase 0 no matter how eager the user is to see code: a day spent on
the brief saves weeks of rework. The one exception: if the user explicitly
says "skip the brief, just prototype X", do it, but say what you're assuming,
and offer the brief afterwards.

## Phase 0: Initiate

The goal is a brief that contains everything you'd otherwise have to guess.
Read `references/initiate.md` for the full procedure. In short:

1. Copy `assets/GAME_BRIEF.md` into the game repo as `docs/GAME_BRIEF.md`
   (create the repo or folder if needed).
2. Pre-fill every answer you can from what the user has already said. Mark
   each one you inferred with `(inferred)` so they can correct it rather than
   retype it.
3. Hand it over. Tell them where the file is, that `required` sections matter
   most, and that `DECIDE` is a valid answer: it means "you choose, and
   record why". Don't fire forty questions at them in chat. The document is
   the interface; chat is for the handful of things that need a conversation.
4. When they say it's done, run
   `python3 <skill-dir>/scripts/check_brief.py docs/GAME_BRIEF.md`. It lists
   unanswered required fields, optional gaps and `DECIDE` delegations.
5. Ask only about the gaps that would change the plan (platform, engine
   constraints, scope, art source). Group the questions, offer a recommended
   answer for each, and write their replies back into the brief.
6. Read the brief back as a one-paragraph summary plus the three riskiest
   assumptions, and get a yes before planning.

If the user can't or won't fill a document (say they're on a phone), run the
same brief as a conversation, a section at a time, and write it up yourself.

## Phase 1: Plan

Produce `docs/PLAN.md` from `assets/PLAN.md`. It has four parts:

- **Decision log.** Every `DECIDE` from the brief, plus engine, language,
  rendering, physics, audio, UI, save format and asset pipeline. One line of
  reasoning each. Read `references/engine-selection.md` to choose an engine,
  then the matching `references/engines/<engine>.md` for its specifics.
  Choose something you can **run headlessly and test in this environment**,
  unless the brief rules that out. If the user's target is consoles or mobile,
  say what you can and can't verify from here.
- **Architecture.** Modules, the main loop, state ownership, how data flows.
  Use `references/architecture.md`. Keep simulation separate from rendering
  so tests can run the game without a window. This one decision is what lets
  you verify your own work later.
- **Milestones.** A vertical slice first (one complete loop, ugly but
  playable), then widen. Each milestone lists what the user will be able to
  do, and the checks that prove it. See `references/workflow.md`.
- **Risks.** What could sink it (performance, an unproven mechanic, asset
  supply, an engine limit) and the cheapest experiment that retires each.

Also write the game repo's `CLAUDE.md` from `assets/CLAUDE.md.template`:
layout, commands, conventions and "rules that bite". Future sessions start
from that file, so keep it current as the project grows.

Show the plan and wait for approval. Planning is cheap to change; code isn't.

## Phase 2: Scaffold

Build the skeleton before any features: the game opens a window, runs its
loop, and quits cleanly. More importantly, it has the **eyes and ears** you'll
use for the rest of the project. Read `references/testing.md`. At minimum:

- `test`: headless simulation tests with a fixed random seed (deterministic).
- `smoke`: drives the real game with scripted input for a few seconds, under
  a virtual display (`xvfb-run`) if there's no screen.
- `shot`: renders a named scenario to a PNG you can look at.
- `build`: produces a runnable build for the primary platform.

Put each command in CLAUDE.md and run all of them before calling the scaffold
done. Commit, push, open a PR if the repo uses them.

## Phase 3: Build

Build one vertical slice at a time. Each slice goes through this loop:

1. Write or extend a test that fails for the behaviour you're adding, for
   anything with rules (physics, damage, scoring, AI, saving).
2. Implement the behaviour.
3. Run the tests and the smoke test.
4. Render a screenshot of it (`shot`) and **look at the image**. Most visual
   bugs are obvious at a glance and invisible in code.
5. Commit with a message that says what the player can now do.
6. Tell the user what to try, in concrete terms ("press F with the rifle
   held: it should kick up and settle in about half a second"). Feel can only
   be judged by a human playing it.

Keep the user's taste central. When they give feedback, write durable
preferences into CLAUDE.md or the brief's "feel" section so they survive the
session. If they keep tuning the same numbers, build them a live tuning panel
(see `references/workflow.md`): it puts the knobs in their hands and ends the
back-and-forth.

## Phase 4: Polish

Polish is where most of the perceived quality comes from. Read
`references/assets-audio.md` for sourcing and pipelines, and
`references/lessons.md` for the mistakes this is meant to save you from.

- Audio usually matters more than people expect, and people are picky about
  it. Offer candidates for important sounds and let them pick, rather than
  choosing alone. A simple review page with play buttons works well.
- Prefer real recordings, scans and hand-tuned art over flat procedural
  shapes. Track every asset's source and licence in a credits file as you
  add it, not at the end.
- Add "juice" (screen shake, hit pause, particles, easing) in proportion to
  the tone the brief describes, and behind tuning knobs.

## Phase 5: Release

Read `references/release.md`: packaging per platform, version stamping,
store screenshots and a trailer rendered from scripted scenes, and the
licence and credits check.

## Working habits that matter throughout

- **Real units and real numbers** where the game is grounded in reality
  (metres, kilograms, seconds). Tuning gets far easier when values mean
  something. Stylised games still benefit from one consistent unit system.
- **Determinism**: one seeded random generator for gameplay, a separate one
  for cosmetic effects, so visuals never change test outcomes.
- **Small, verified steps beat big leaps.** Never report something as working
  that you haven't run. If you couldn't verify it (no audio device, no console
  devkit), say so plainly.
- **Write down what you learn.** Pitfalls go into CLAUDE.md "rules that
  bite" the moment you hit them.
- **Ask before outward-facing actions**: publishing builds, uploading to
  stores, posting anything.

## Reference map

Read these when the phase calls for them, not all up front.

| File | When |
|---|---|
| `references/initiate.md` | Running phase 0 |
| `references/engine-selection.md` | Choosing an engine or framework |
| `references/engines/*.md` | After choosing: setup, headless testing, builds, pitfalls for that engine |
| `references/architecture.md` | Designing modules, loop, state, saving |
| `references/workflow.md` | Milestones, slicing, feedback loops, tuning panels |
| `references/testing.md` | Making the game testable and visible to you |
| `references/assets-audio.md` | Finding, licensing and processing art and sound |
| `references/release.md` | Builds, store pages, trailers |
| `references/lessons.md` | Field notes from a real project: read once before phase 2 |
| `assets/GAME_BRIEF.md` | The initiate document |
| `assets/PLAN.md` | Plan template |
| `assets/CLAUDE.md.template` | Agent notes for the new game repo |
| `scripts/check_brief.py` | Checking the brief for gaps |
