# games — Status

**Last updated:** 2026-10-31

## Where things stand

- Git repo: `github.com/DDMrt/kid-games` (**private**, branch `main`), created
  2026-10-31. Not to be confused with the older, unrelated `DDMrt/Games`
  (a 2022 Python game). Leave that one alone.
- `.gitignore` excludes media (png/jpg/audio/video). Each game's icons are
  regenerated with `python make_icons.py` in that game's folder (standard
  library only).
- `_reference/balloon_pop/` holds an earlier prototype (tap floating balloons
  to pop them). It's reference code only; it was never play-tested on the
  real devices. It is **not** in the git repo (gitignored at Dillon's
  request, 2026-10-31); the only copy is this local folder.

## Games

### forest_friends (first build 2026-10-31, not yet play-tested on devices)

Dillon's design: a side-scrolling platformer (a mix of Mario-style running
and Ori-style vertical movement).

- Pick one of 4 animals: squirrel, puppy, raccoon, bird. They look different
  but all move the same: walk, jump, a double jump (flutter) in the air, and
  holding jump makes them float down slowly.
- Level 1 is a magical forest. Tree branches are one-way platforms. There
  are butterflies, falling leaves, swaying flowers, glowing mushrooms and
  floating sparkles.
- Enemies are goofy purple beetles and hopping green slimes. Landing on one
  pops it into stars. Running into one from the side gives a gentle "boing"
  bounce back. There are no lives and no restarts.
- The key sits high in the 5th tree, about 55% of the way through. The gate
  at the end stays shut without the key: the animal shows a "key" thought
  bubble and the key slot in the top-left pulses. With the key, the key
  flies into the lock, the doors open and a rainbow appears.
- Win screen: confetti, then two buttons: replay (green arrow) and choose
  animal (orange paw).
- Controls: big on-screen ◀ ▶ buttons on the left and a jump button on the
  right. The whole left half of the screen counts as move and the right half
  as jump. On PC: arrow keys / WASD, plus space to jump.
- Code-drawn graphics and synthesized sound, one `index.html`. A headless
  smoke test plus a bot run reached the win screen at phone and PC sizes.

## Next steps

1. Play-test `forest_friends` on iPhone, Fire tablet and PC over the LAN link
   (`python -m http.server 8080 --bind 0.0.0.0` in the game folder). Tune
   speed, jump height, button size and difficulty from how he actually plays.
2. Decide on permanent hosting. The repo is private, and GitHub Pages on a
   free plan needs a public repo. Options: make it public, a paid plan, or
   another free https host (e.g. Netlify or Cloudflare Pages, which can deploy
   from a private repo).
