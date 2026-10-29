# Milestones, slices and feedback loops

## Vertical slice first

The first milestone after the scaffold is one complete loop: the player can
start, play the core verb, succeed or fail, and start again. Use placeholder
art, but make it *readable*. This proves the game is fun (or isn't) before
weeks go into content.

Widen afterwards: more content, more systems, then polish. Don't build
the eighth weapon before the first one feels good.

## Writing a milestone

```
### M2: Combat
- Player can: pick up a rifle, aim with the mouse, fire, reload; enemies
  take damage by hit location and fall when killed.
- Checks:
  - test: a rifle round to the head of a standing target kills it
  - test: an empty magazine reloads in 2.6 s and plays the reload sound
  - smoke: spawn every weapon, fire each once, no errors
  - shot: "range" scenario shows a target with an entry wound
- Feel to confirm with the user: recoil kick and settle, reload timing
```

The checks are how you know you're done, and the "feel" line is what you ask
the user to try.

## The build loop

For each change: test first (for rules), implement, run tests and smoke,
take a screenshot and look at it, commit, then tell the user what to try.
Push regularly; small commits with clear messages ("Blades stick and can run
people through") double as a changelog.

When the user reports a bug, reproduce it in a test or a scripted scenario
first. If you can't reproduce it, say so and ask for steps, a save file or a
video. Don't "fix" blind.

## Handling feedback

Users give feedback in batches, often mixing bugs, taste and new ideas.
Turn each batch into a task list, fix the quick and clear things first,
and ask about anything ambiguous with a recommended answer. Write durable
preferences ("hates floaty jumps", "wants bass in gunshots", "no timers on
TNT") into CLAUDE.md so later sessions honour them.

Taste decisions (which sound, which art style, which of three jump curves)
are the user's. Make them cheap to decide:

- **Review pages**: an HTML page with play buttons for sound candidates, or
  side-by-side images for art options, loudness- or size-matched so the
  comparison is fair. Let them mark favourites.
- **Live tuning panel**: in-game sliders for the numbers that set feel
  (jump height, gravity, recoil, stiffness, volumes), changed while the game
  runs. Save the values to a file, and add a "copy changes" button that puts
  the differences from the defaults on the clipboard so the user can paste
  them back to you. Then make their values the new defaults. This ends long
  tuning back-and-forths.

## When the user wants to play

Give them a build they can run with no setup: a zip with the executable for
their OS, a web link, or one command. Say what changed and what to try:

> New in this build: the rifle reloads with a magazine sound, and blades
> stick in people. Try: spawn a spear (Melee tab), drag it fast into a
> person's chest; it should go through and stay in.

## Keeping a long project healthy

- Keep CLAUDE.md current: layout, commands, rules that bite, user
  preferences. It is the next session's memory.
- Keep PLAN.md current: tick off milestones, log new decisions.
- Run the full test suite and smoke before every push.
- When a file passes about 1,500 lines, split it along a natural seam.
- Remove debug prints and probes before committing.
