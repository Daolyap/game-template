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

_TODO_

### 1.2 One-sentence pitch `required`
> What is it, for whom, and why is it fun? e.g. "A cosy fishing roguelite where every lake is a hand-made puzzle."

_TODO_

### 1.3 Genre and references `required`
> Genre(s), and 2–5 existing games, films or books it should feel like. Say which part of each: "the combat of Hades, the mood of Firewatch".

_TODO_

### 1.4 What makes it different
> Why would someone play this instead of the games above?

_TODO_

### 1.5 Is this a jam game, a prototype, a hobby project or a commercial release? `required`

_TODO_

---

## 2. Players

### 2.1 Who is it for? `required`
> Age range, gamer or casual, any specific community (speedrunners, kids, people who play on the train).

_TODO_

### 2.2 Session length
> A typical play session: 2 minutes? An evening?

_TODO_

### 2.3 Difficulty and skill
> Forgiving or punishing? Is there a learning curve you want?

_TODO_

### 2.4 Content rating and sensitivities
> Violence, gore, language, themes. Anything that must not appear?

_TODO_

---

## 3. Platforms and technology

### 3.1 Target platforms `required`
> Primary first. Windows / macOS / Linux / Web browser / Android / iOS / Switch / PlayStation / Xbox / VR / other.

_TODO_

### 3.2 Input `required`
> Keyboard and mouse, gamepad, touch, motion, other. Which is primary?

_TODO_

### 3.3 Engine, framework or language
> Any preference or requirement (Godot, Unity, Unreal, LÖVE, Phaser, Pygame, Bevy, plain code...)? Languages you know or want to learn? Anything you want to avoid? `DECIDE` is fine.

_TODO_

### 3.4 2D or 3D, and camera `required`
> Side view, top-down, isometric, first person, third person, fixed screen...

_TODO_

### 3.5 Performance and hardware
> Target frame rate, lowest machine it should run on, screen resolutions and aspect ratios, offline or online.

_TODO_

### 3.6 Your setup
> What OS do you develop and play-test on? Can you run builds and play them yourself? How should builds reach you (zip, installer, browser link, store beta)?

_TODO_

---

## 4. Core loop

### 4.1 Moment to moment `required`
> What does the player do every few seconds? Describe the verbs: run, jump, aim, place, talk...

_TODO_

### 4.2 Session loop
> What does a full session look like, start to finish? What makes them want "one more go"?

_TODO_

### 4.3 Long-term progression
> Unlocks, levels, story, collection, mastery, none?

_TODO_

### 4.4 Win, lose and fail states
> How does a run, level or game end? What happens on failure?

_TODO_

---

## 5. Mechanics and systems

### 5.1 Mechanics list `required`
> Every mechanic you can think of, most important first. Mark the ones that are essential for the first playable version.

_TODO_

### 5.2 Controls
> Which input does what? A rough table is fine.

_TODO_

### 5.3 Physics and realism
> Arcade or simulated? Real-world numbers (gravity, speeds, masses) or stylised? Any physics that's central (ragdolls, vehicles, destruction, fluids)?

_TODO_

### 5.4 AI and characters
> Enemies, companions, crowds, opponents. How smart, and in what way?

_TODO_

### 5.5 Procedural or hand-made content
> Levels, items, worlds: generated, designed, or both?

_TODO_

### 5.6 Economy and numbers
> Currencies, stats, damage, scoring. Rough values if you have them.

_TODO_

---

## 6. Content and scope

### 6.1 Content for the first playable version `required`
> The smallest set of levels, characters, items and so on that would let someone play the core loop. Be ruthless.

_TODO_

### 6.2 Content for the full version
> Rough counts: levels, enemies, weapons, hours of play.

_TODO_

### 6.3 Must / should / could / won't
> Prioritise features. "Won't" is as useful as "must".

_TODO_

---

## 7. World, story and tone

### 7.1 Setting
> Where and when? How grounded or fantastical?

_TODO_

### 7.2 Story and characters
> Is there a narrative? How is it told (cutscenes, text, environment, none)?

_TODO_

### 7.3 Tone `required`
> Three adjectives, e.g. "tense, grimy, darkly funny".

_TODO_

---

## 8. Art direction

### 8.1 Visual style `required`
> Pixel art, vector, hand-drawn, low-poly, realistic, stylised 3D... plus reference images or games.

_TODO_

### 8.2 Where the art comes from `required`
> You make it / an artist makes it / free asset packs (CC0) / bought packs / AI-generated / procedural / `DECIDE`. Any licence constraints?

_TODO_

### 8.3 Resolution, palette and animation
> Native resolution (for pixel art), colour palette or mood, how much animation.

_TODO_

### 8.4 Things you dislike
> Styles or looks to avoid. e.g. "no flat shapes stuck together", "no glossy mobile look".

_TODO_

---

## 9. Audio

### 9.1 Music
> Style, references, dynamic or looping, or none.

_TODO_

### 9.2 Sound effects
> Which sounds matter most (weapons, footsteps, UI, ambience)? How picky are you?

_TODO_

### 9.3 Voice
> Voice acting, gibberish, text only?

_TODO_

### 9.4 Where the audio comes from
> You / a composer / free libraries (CC0) / royalty-free bundles / bought / generated / `DECIDE`.

_TODO_

---

## 10. Interface and accessibility

### 10.1 Screens
> Title, menus, settings, pause, inventory, map, editor...

_TODO_

### 10.2 HUD
> What's on screen during play?

_TODO_

### 10.3 Accessibility
> Remappable controls, subtitles, colour-blind modes, difficulty options, reduced motion...

_TODO_

### 10.4 Languages
> Which languages at launch? Later?

_TODO_

---

## 11. Multiplayer and online

### 11.1 Multiplayer `required`
> None / local co-op / local versus / online co-op / online versus / asynchronous (leaderboards, ghosts).

_TODO_

### 11.2 Online services
> Accounts, servers, cloud saves, analytics, mod sharing? Any you must avoid?

_TODO_

---

## 12. Saving and settings

### 12.1 Persistence
> Save anywhere, checkpoints, autosave, no saves, permadeath. Should saves survive game updates?

_TODO_

### 12.2 Modding and user content
> Level editor, mod support, sharing creations?

_TODO_

---

## 13. Business

### 13.1 Price and model
> Free, paid, pay what you want, free with paid extras. (Ads and loot boxes change the design a lot: say if you want them.)

_TODO_

### 13.2 Where it will be published
> itch.io, Steam, app stores, console stores, your website, nowhere.

_TODO_

### 13.3 Store page and marketing assets
> Will you need screenshots, a trailer, capsule art, a press kit?

_TODO_

---

## 14. Constraints

### 14.1 Timeline `required`
> Deadline or milestones (jam end, demo date, launch window), or "no rush".

_TODO_

### 14.2 Team and budget
> Who else is involved? Budget for assets, tools, store fees?

_TODO_

### 14.3 Licences and openness
> Code licence, public or private repo, any assets that can't be redistributed.

_TODO_

---

## 15. Feel and quality bar

### 15.1 What "good" means to you `required`
> When you play it, what should it feel like? What would make you say "yes, that's it"?

_TODO_

### 15.2 Pet peeves
> Things in other games that bug you and must not happen here (floaty jumps, input lag, sounds that are "mid", unreadable UI...).

_TODO_

### 15.3 How you want to give feedback
> Play every build? Weekly check-ins? Live tuning sliders you can adjust yourself? Review pages for art and sound choices?

_TODO_

---

## 16. Working together

### 16.1 Repository and tools
> Where should the code live (GitHub repo name)? Branch and pull-request habits? Issue tracker?

_TODO_

### 16.2 How much autonomy
> Should the developer check in before each feature, each milestone, or only when stuck?

_TODO_

### 16.3 Anything else
> Anything not covered above: inspirations, wild ideas, worries, things you've tried before.

_TODO_
