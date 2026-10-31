# Working in this folder

See `~/.claude/CLAUDE.md` (canonical copy: `github.com/DDMrt/claude-config`)
for general conventions that apply here too: git workflow defaults, large
files/OneDrive, per-project venvs, LAN-IP links instead of localhost. This
file only covers what's specific to games.

## What this is

Simple video games for Dillon's 2-year-old son. **Dillon designs the games;
Claude builds them.** Don't invent game concepts or add features on its own.
Ask Dillon, and offer suggestions only when he asks or when a design detail
is genuinely missing.

## Requirements

- Must run on **iPhone (Safari), Amazon Fire tablet (Silk browser) and PC**.
  Default approach: plain HTML/JS web games (canvas, Web Audio for sound),
  installable to the home screen as a PWA (manifest + service worker).
- Built for a toddler: huge tap targets, every tap gets a response, no
  failing or losing, no reading needed, short fun feedback (sound, color,
  motion). Block zoom, scroll and long-press menus.
- iPhone needs a user tap (e.g. a big play button) before sound can start.
- Media (images/audio) stays out of git per the global rules. Prefer
  synthesized sound and code-drawn graphics where practical.

## Layout

- One subfolder per game (e.g. `games/<game_name>/index.html`).
- `_reference/balloon_pop/` is an early prototype Claude built before Dillon
  clarified he wants to design the games himself. Its code shows working
  patterns (canvas setup, multi-touch, iOS audio unlock, PWA files, an icon
  generator using only the standard library). Reuse it as reference, not as
  a game to extend unless he asks.

## Testing and hosting

- Local testing: serve the game folder with `python -m http.server 8080
  --bind 0.0.0.0` and send the LAN-IP link (see the global file). Works only
  on home Wi-Fi while the PC is on. Service workers don't register over
  plain-http LAN, so offline/install only works once it's hosted on https.
- Repo: `github.com/DDMrt/kid-games` (private). Pushing still needs Dillon's
  yes every time.
- Permanent hosting: not set up yet. GitHub Pages needs a public repo on the
  free plan, so it would mean changing visibility or picking another https
  host. Dillon decides.
- For locking him inside the game: Guided Access on iPhone; screen pinning or
  a child profile on the Fire tablet.
