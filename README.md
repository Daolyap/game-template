# game-forge

A Claude skill for making a game of any kind, in any engine, from the first
idea to a release build.

It starts with an **Initiate** phase: you fill in a game brief that covers
everything a developer needs to know before writing code (pitch, platforms,
core loop, mechanics, scope, art and audio direction, feel, timeline, how
you want to give feedback). Then Claude plans the project, scaffolds it with
tests and screenshot tools so it can check its own work, and builds it in
playable slices that you review.

## Phases

| Phase | What happens | Output |
|---|---|---|
| 0. Initiate | Claude copies the brief template into your repo, pre-fills what you've said, you fill in the rest; a checker finds gaps; Claude asks only about what would change the plan | `docs/GAME_BRIEF.md` |
| 1. Plan | Engine and tech decisions with reasons, architecture, milestones, risks | `docs/PLAN.md`, `CLAUDE.md` |
| 2. Scaffold | A runnable skeleton with headless tests, a scripted smoke test, screenshot capture and a build command | Working commands |
| 3. Build | Vertical slices, test-first for rules, each checked by screenshot and handed to you to play | Playable milestones |
| 4. Polish | Feel, sound and art passes; review pages for asset picks; a live tuning panel | A game that feels right to you |
| 5. Release | Builds per platform, store screenshots and a trailer rendered from the game | Shippable builds |

## What's inside

```
skills/game-forge/
├── SKILL.md                    the workflow
├── assets/
│   ├── GAME_BRIEF.md           the Initiate document you fill in
│   ├── PLAN.md                 plan template
│   └── CLAUDE.md.template      agent notes for the new game's repo
├── scripts/check_brief.py      reports missing answers in a brief
├── references/
│   ├── initiate.md             running the Initiate phase
│   ├── engine-selection.md     choosing an engine Claude can test
│   ├── engines/                Godot, LÖVE, web (Phaser/Pixi/Three), Pygame, Unity, Unreal, Bevy
│   ├── architecture.md         loop, state, units, saving, input
│   ├── testing.md              headless tests, smoke tests, screenshots, recording
│   ├── workflow.md             milestones, feedback, tuning panels
│   ├── assets-audio.md         sourcing, licences and processing art and sound
│   ├── release.md              builds, store media, trailers
│   └── lessons.md              field notes from building a large physics sandbox
└── evals/                      test cases (claude plugin eval format)
```

## Install

**Claude Code**: copy (or symlink) the skill into your skills folder:

```
git clone https://github.com/Daolyap/game-forge
mkdir -p ~/.claude/skills
cp -r game-forge/skills/game-forge ~/.claude/skills/
```

or into a project's `.claude/skills/` to share it with everyone working on
that repo.

**Claude.ai**: zip the `skills/game-forge` folder and upload it under
Settings → Capabilities → Skills.

## Use

Just describe your game: "I want to make a cosy fishing roguelite for PC
and Switch". Claude will start the Initiate phase and give you the brief to
fill in. You can answer `DECIDE` to anything you'd rather Claude choose.

Check a brief yourself at any time:

```
python3 skills/game-forge/scripts/check_brief.py docs/GAME_BRIEF.md
```

## Licence

MIT
