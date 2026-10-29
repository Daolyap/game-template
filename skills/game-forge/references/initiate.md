# Phase 0: Initiate

The brief is the contract between the person's head and the code. Your job
in this phase is to make filling it in easy, and to make sure that nothing
the plan depends on is left as a guess.

## Setting up the brief

1. Find or create the game's repo or folder. If the user named a repo, use
   it; otherwise ask once where the code should live, defaulting to a new
   folder named after the working title.
2. Copy `assets/GAME_BRIEF.md` to `docs/GAME_BRIEF.md`.
3. Pre-fill from the conversation. Anything the user has said (genre,
   platform, references, "I hate floaty jumps") goes into the matching
   answer with `(inferred)` appended. Don't invent answers they haven't
   implied: a pre-filled guess they skim past is worse than a blank.
4. Commit it ("Add game brief"), so their edits show up as a diff.

## Handing it over

Keep the message short and practical:

- where the file is (path, and a link if the repo is on GitHub);
- that the `required` questions matter most, and they're marked;
- that `DECIDE` and `N/A` are fine answers, and rough notes are welcome;
- that you've pre-filled N answers marked `(inferred)` for them to check;
- that you'll check it for gaps when they're done.

Don't paste the whole brief into chat or list all the questions. If they'd
rather answer in chat (on a phone, or they just prefer talking), go section
by section, two or three questions at a time, and write the answers into
the file yourself.

## Checking it

Run the checker from the skill directory:

```
python3 <skill-dir>/scripts/check_brief.py docs/GAME_BRIEF.md
```

It prints missing required answers, inferred answers awaiting
confirmation, `DECIDE` delegations and unanswered optional questions, and
exits non-zero while required answers are missing.

Then read the answers yourself, because the checker only sees blanks. Look
for:

- **Contradictions**: "runs on a phone" with "realistic 3D destruction", a
  two-week deadline with forty levels, "no AI art" with "art: DECIDE".
- **Vague answers to required questions**: "fun" as the feel target, "all
  platforms". Ask for one concrete example.
- **Hidden scope**: online multiplayer, procedural generation, level
  editors, physics-heavy systems and localisation each multiply the work.
  If one appears casually, check it's really wanted in the first version.
- **Unverifiable targets**: consoles and iOS need devkits or Apple hardware
  you may not have. Say early what you can and can't test.

## Follow-up questions

Ask only what would change the plan. A good batch is under ten questions,
grouped by topic, each with a recommended answer so the user can reply
"yes to all":

> **Platforms.** You listed PC and Switch. Switch needs a Nintendo developer
> account and devkit, which I can't test from here. Recommend: build for PC
> first, keep the engine Switch-capable (Godot or Unity), revisit at M3. OK?

Write every reply back into the brief (replacing `_TODO_` or the
`(inferred)` marker), and commit.

## The read-back

Before planning, give the user:

1. a one-paragraph summary of the game as you now understand it;
2. what the first playable version contains;
3. the three riskiest assumptions, and how you'd test each cheaply.

Move to phase 1 when they say yes. If they correct something, fix the
brief first, then the summary.

## Defaults for unanswered optional questions

Fill these silently (record them in PLAN.md's decision log) unless the
brief suggests otherwise:

| Question | Default |
|---|---|
| Session length | 10–30 minutes |
| Accessibility | Remappable controls, subtitles if any speech, a reduced screen-shake option |
| Languages | English only, with strings kept in one place for later translation |
| Saving | Autosave at natural breaks; settings saved separately |
| Online services | None |
| Feedback style | A playable build at each milestone, plus a tuning panel for feel numbers |
| Autonomy | Check in at each milestone, or when blocked on a taste decision |
