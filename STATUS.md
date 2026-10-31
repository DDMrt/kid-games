# games — Status

**Last updated:** 2026-10-31

## Where things stand

- Folder set up; no game designed yet.
- Git repo: `github.com/DDMrt/kid-games` (**private**, branch `main`), created
  2026-10-31. Not to be confused with the older, unrelated `DDMrt/Games`
  (a 2022 Python game). Leave that one alone.
- `.gitignore` excludes media (png/jpg/audio/video). The balloon_pop icons
  are regenerated with `python make_icons.py` in that folder.
- Dillon will design the first game; build it together next session.
- `_reference/balloon_pop/` holds an earlier prototype (tap floating balloons
  to pop them). It's reference code only; it was never play-tested on the
  real devices. It is **not** in the git repo (gitignored at Dillon's
  request, 2026-10-31); the only copy is this local folder.

## Next steps

1. Dillon describes his game design (what's on screen, what happens on tap,
   sounds, any characters or themes he wants).
2. Claude builds it in `games/<game_name>/` as a web game, using
   `_reference/balloon_pop/` for proven patterns.
3. Test on iPhone, Fire tablet and PC over the LAN link.
4. Decide on permanent hosting. The repo is private, and GitHub Pages on a
   free plan needs a public repo. Options: make it public, a paid plan, or
   another free https host (e.g. Netlify or Cloudflare Pages, which can deploy
   from a private repo).
