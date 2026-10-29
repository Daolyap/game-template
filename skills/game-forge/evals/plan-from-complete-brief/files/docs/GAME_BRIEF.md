# Game Brief

This document is everything the developer (a person or an AI agent) needs to
know before building your game. Fill in as much as you can. Rough notes are
fine; bullet points are fine; "like the jump in Celeste" is a great answer.

How to answer:

- Replace each `_TODO_` with your answer.
- Sections tagged `required` are the ones that change how the game is built.
  Please answer them, even briefly.
- `DECIDE` is a valid answer anywhere. It means "you choose, and write down
  why". Use it whenever you don't know or don't mind.
- `N/A` means the question doesn't apply to this game.
- Answers marked `(inferred)` were filled in from earlier conversation. Fix
  any that are wrong and delete the marker on ones that are right.
- Links, images and reference videos are welcome anywhere.

---

## 1. Identity

### 1.1 Working title `required`
> A name to use for now. It can change.

Tidebreak

### 1.2 One-sentence pitch `required`
> What is it, for whom, and why is it fun? e.g. "A cosy fishing roguelite where every lake is a hand-made puzzle."

A browser tower-defence game where you build sea walls and lighthouses to hold back a rising, storm-driven tide; for people who like short clever puzzles.

### 1.3 Genre and references `required`
> Genre(s), and 2–5 existing games, films or books it should feel like. Say which part of each: "the combat of Hades, the mood of Firewatch".

Tower defence / puzzle. Kingdom Rush (readable waves, upgrade paths), Islanders (calm, minimal art), Bad North (tiny islands, weather).

### 1.4 What makes it different
> Why would someone play this instead of the games above?

The enemy is the water itself: waves flow around your walls with simple fluid rules, so placement is a puzzle, not just DPS.

### 1.5 Is this a jam game, a prototype, a hobby project or a commercial release? `required`

Hobby project, maybe itch.io later.

---

## 2. Players

### 2.1 Who is it for? `required`
> Age range, gamer or casual, any specific community (speedrunners, kids, people who play on the train).

Casual puzzle fans, 12+, people who play in a lunch break.

### 2.2 Session length
> A typical play session: 2 minutes? An evening?

5-15 minutes per island.

### 2.3 Difficulty and skill
> Forgiving or punishing? Is there a learning curve you want?

Gentle first islands, hard optional ones.

### 2.4 Content rating and sensitivities
> Violence, gore, language, themes. Anything that must not appear?

None; family friendly.

---

## 3. Platforms and technology

### 3.1 Target platforms `required`
> Primary first. Windows / macOS / Linux / Web browser / Android / iOS / Switch / PlayStation / Xbox / VR / other.

Web browser (desktop first), mobile browser later.

### 3.2 Input `required`
> Keyboard and mouse, gamepad, touch, motion, other. Which is primary?

Mouse primary, touch later.

### 3.3 Engine, framework or language
> Any preference or requirement (Godot, Unity, Unreal, LÖVE, Phaser, Pygame, Bevy, plain code...)? Languages you know or want to learn? Anything you want to avoid? `DECIDE` is fine.

DECIDE

### 3.4 2D or 3D, and camera `required`
> Side view, top-down, isometric, first person, third person, fixed screen...

2D, top-down, slight angle like Bad North but flat.

### 3.5 Performance and hardware
> Target frame rate, lowest machine it should run on, screen resolutions and aspect ratios, offline or online.

60 fps on a 5-year-old laptop; offline once loaded.

### 3.6 Your setup
> What OS do you develop and play-test on? Can you run builds and play them yourself? How should builds reach you (zip, installer, browser link, store beta)?

Windows laptop with Chrome. I can play any link you send.

---

## 4. Core loop

### 4.1 Moment to moment `required`
> What does the player do every few seconds? Describe the verbs: run, jump, aim, place, talk...

Place walls, groynes and pumps on a grid between waves; watch the tide come in; patch leaks with limited sandbags.

### 4.2 Session loop
> What does a full session look like, start to finish? What makes them want "one more go"?

One island: 5 waves of rising tide, each stronger; keep the village dry to win.

### 4.3 Long-term progression
> Unlocks, levels, story, collection, mastery, none?

Unlock new islands and building types.

### 4.4 Win, lose and fail states
> How does a run, level or game end? What happens on failure?

Lose if water reaches the village 3 times. Win by surviving the last wave.

---

## 5. Mechanics and systems

### 5.1 Mechanics list `required`
> Every mechanic you can think of, most important first. Mark the ones that are essential for the first playable version.

Essential: grid placement, water flow sim, wave timer, village flood check. Later: pumps, wind, storms, upgrades.

### 5.2 Controls
> Which input does what? A rough table is fine.

Left click place, right click remove, Q/E rotate, space starts wave early.

### 5.3 Physics and realism
> Arcade or simulated? Real-world numbers (gravity, speeds, masses) or stylised? Any physics that's central (ragdolls, vehicles, destruction, fluids)?

Stylised, cellular water flow; no rigid bodies.

### 5.4 AI and characters
> Enemies, companions, crowds, opponents. How smart, and in what way?

None

### 5.5 Procedural or hand-made content
> Levels, items, worlds: generated, designed, or both?

Hand-made islands.

### 5.6 Economy and numbers
> Currencies, stats, damage, scoring. Rough values if you have them.

Coins per wave survived; walls cost 1-5 coins.

---

## 6. Content and scope

### 6.1 Content for the first playable version `required`
> The smallest set of levels, characters, items and so on that would let someone play the core loop. Be ruthless.

1 island, 3 building types, 5 waves.

### 6.2 Content for the full version
> Rough counts: levels, enemies, weapons, hours of play.

12 islands, 8 building types.

### 6.3 Must / should / could / won't
> Prioritise features. "Won't" is as useful as "must".

Must: flow sim, placement. Won't: multiplayer.

---

## 7. World, story and tone

### 7.1 Setting
> Where and when? How grounded or fantastical?

North-sea fishing villages, slightly whimsical.

### 7.2 Story and characters
> Is there a narrative? How is it told (cutscenes, text, environment, none)?

None, just island names.

### 7.3 Tone `required`
> Three adjectives, e.g. "tense, grimy, darkly funny".

Calm, tense, cosy.

---

## 8. Art direction

### 8.1 Visual style `required`
> Pixel art, vector, hand-drawn, low-poly, realistic, stylised 3D... plus reference images or games.

Minimal flat colour like Islanders, soft shadows.

### 8.2 Where the art comes from `required`
> You make it / an artist makes it / free asset packs (CC0) / bought packs / AI-generated / procedural / `DECIDE`. Any licence constraints?

DECIDE (CC0 is fine, no AI art please).

### 8.3 Resolution, palette and animation
> Native resolution (for pixel art), colour palette or mood, how much animation.

Muted blues and sand colours; little animation except water.

### 8.4 Things you dislike
> Styles or looks to avoid. e.g. "no flat shapes stuck together", "no glossy mobile look".

Cartoony outlines, glossy mobile look.

---

## 9. Audio

### 9.1 Music
> Style, references, dynamic or looping, or none.

Gentle ambient loop.

### 9.2 Sound effects
> Which sounds matter most (weapons, footsteps, UI, ambience)? How picky are you?

Waves, wood placement thunk, bell when the tide turns.

### 9.3 Voice
> Voice acting, gibberish, text only?

None

### 9.4 Where the audio comes from
> You / a composer / free libraries (CC0) / royalty-free bundles / bought / generated / `DECIDE`.

DECIDE (CC0).

---

## 10. Interface and accessibility

### 10.1 Screens
> Title, menus, settings, pause, inventory, map, editor...

Title, island select, settings, pause.

### 10.2 HUD
> What's on screen during play?

Coins, wave number, tide gauge.

### 10.3 Accessibility
> Remappable controls, subtitles, colour-blind modes, difficulty options, reduced motion...

Colour-blind safe palette, remappable keys.

### 10.4 Languages
> Which languages at launch? Later?

English

---

## 11. Multiplayer and online

### 11.1 Multiplayer `required`
> None / local co-op / local versus / online co-op / online versus / asynchronous (leaderboards, ghosts).

None

### 11.2 Online services
> Accounts, servers, cloud saves, analytics, mod sharing? Any you must avoid?

None

---

## 12. Saving and settings

### 12.1 Persistence
> Save anywhere, checkpoints, autosave, no saves, permadeath. Should saves survive game updates?

Autosave progress per island in localStorage.

### 12.2 Modding and user content
> Level editor, mod support, sharing creations?

No

---

## 13. Business

### 13.1 Price and model
> Free, paid, pay what you want, free with paid extras. (Ads and loot boxes change the design a lot: say if you want them.)

Free

### 13.2 Where it will be published
> itch.io, Steam, app stores, console stores, your website, nowhere.

itch.io

### 13.3 Store page and marketing assets
> Will you need screenshots, a trailer, capsule art, a press kit?

Screenshots only.

---

## 14. Constraints

### 14.1 Timeline `required`
> Deadline or milestones (jam end, demo date, launch window), or "no rush".

Playable first island in 2 weeks, no hard deadline after.

### 14.2 Team and budget
> Who else is involved? Budget for assets, tools, store fees?

Just me, no budget.

### 14.3 Licences and openness
> Code licence, public or private repo, any assets that can't be redistributed.

MIT, public repo.

---

## 15. Feel and quality bar

### 15.1 What "good" means to you `required`
> When you play it, what should it feel like? What would make you say "yes, that's it"?

Water that looks and behaves believably; satisfying moment when a wall holds.

### 15.2 Pet peeves
> Things in other games that bug you and must not happen here (floaty jumps, input lag, sounds that are "mid", unreadable UI...).

Laggy placement, unclear why I lost.

### 15.3 How you want to give feedback
> Play every build? Weekly check-ins? Live tuning sliders you can adjust yourself? Review pages for art and sound choices?

Play each build via a link; sliders for wave strength would be nice.

---

## 16. Working together

### 16.1 Repository and tools
> Where should the code live (GitHub repo name)? Branch and pull-request habits? Issue tracker?

GitHub, new repo tidebreak.

### 16.2 How much autonomy
> Should the developer check in before each feature, each milestone, or only when stuck?

Check in at milestones.

### 16.3 Anything else
> Anything not covered above: inspirations, wild ideas, worries, things you've tried before.

N/A
