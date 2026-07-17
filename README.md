# jacob.reiter.cv — personal CV site

A single static HTML page. No framework, no build step, no dependencies to install.
Everything lives in **`index.html`** (markup + CSS + a little vanilla JS for the scroll-nav).

- **Live site:** https://jacob.reiter.cv
- **Root domain:** https://reiter.cv → forwards to `jacob.reiter.cv`
- **Repo:** https://github.com/jacobereiter/jacob-reiter-cv (must stay **public** — see Gotchas)
- **This folder** (`~/website`) is a git clone of that repo. Edit here, commit, push → the live site updates in ~1 minute.

---

## Make an edit (the whole workflow)

```bash
cd ~/website
git pull                       # get any changes made elsewhere first
# ...edit index.html...
git add index.html
git commit -m "describe the change"
git push
```

GitHub Pages rebuilds automatically on push. Give it 30–60s, then hard-refresh
(`Cmd-Shift-R`) the live site.

That's the entire deploy process. There is no build, no `npm`, no CI to babysit.

---

## Preview locally before pushing

Two options:

1. **Just open the file** — `open ~/website/index.html` renders fine in a browser.
2. **Local server** (matches how Pages serves it):
   ```bash
   python3 ~/website/serve.py        # serves this folder on http://localhost:8080
   ```
   `serve.py` is a tiny stdlib HTTP server — needs only Python 3, which ships with macOS.
   (Claude Code can also launch this via the "website" entry in `~/.claude/launch.json`.)

---

## Editing the content

It's one file, top to bottom:

- **`<style>`** in the `<head>` — all CSS. Two-column layout: sticky left `<aside>`
  (name, tagline, contact links, section nav) and right `<main>` (the content).
  The `@media (max-width: 700px)` block collapses it to one column on mobile.
- **`<aside>`** — name, subtitle, contact links, and the `#sidebar` nav. If you add or
  rename a `<h2 id="...">` section in `<main>`, update the matching `<a href="#...">`
  in the nav so scroll-highlighting keeps working.
- **`<main>`** — the sections: About → Education → Experience → Publications, each an
  `<h2 id="...">` followed by `.role` / `.edu` / `.pub` blocks. Copy an existing block
  as a template.
- **`<script>`** at the bottom — highlights the current section in the left nav as you
  scroll. You normally don't need to touch it.

---

## Accounts & tools (what you need, and why)

| Thing | What / where | Notes |
|---|---|---|
| **GitHub account** | `jacobereiter` | Owns the repo and Pages deployment. |
| **`git`** | preinstalled on macOS | The only tool required to edit + deploy. |
| **`gh` CLI** | installed at `~/bin/gh` | Optional but handy. Already logged in as `jacobereiter` (`gh auth status` to check). Used once to wire up git auth: `gh auth setup-git`. |
| **`python3`** | preinstalled on macOS | Only for the optional local preview server. |
| **Porkbun account** | where `reiter.cv` is registered | Only needed to touch DNS / the domain (rare — see below). |

If `git push` ever asks for a username/password, re-run **`gh auth setup-git`** to
restore the credential helper (that's what lets HTTPS pushes work without a password).

---

## Domain & DNS (rarely touched)

The domain `reiter.cv` is registered at **Porkbun**. Two pieces make the URLs work:

- **`jacob.reiter.cv`** → a `CNAME` DNS record pointing to `jacobereiter.github.io`.
  This is the real site. The `CNAME` **file** in this repo tells GitHub Pages to serve
  under that hostname — **don't delete it**, or the custom domain breaks.
- **`reiter.cv`** (root) → Porkbun **URL forwarding** to `https://jacob.reiter.cv`.
  (Root domains can't be `CNAME`s, so forwarding is used instead.)

HTTPS is handled by GitHub (Let's Encrypt cert, auto-renewed) and is enforced.
You only log into Porkbun if you're changing the domain or DNS.

---

## Gotchas / things that have bitten us

- **The repo must be public.** GitHub Pages doesn't serve from private repos on the free
  plan — making it private silently disables the site. Keep it public.
- **Don't delete `CNAME`.** It's what binds the custom domain to Pages.
- **Pull before you edit.** Edits sometimes happen from more than one machine/clone;
  `git pull` first to avoid conflicts.
- **Changes not showing?** It's almost always browser cache — hard-refresh
  (`Cmd-Shift-R`). If still stale after a couple minutes, check the repo's
  Actions/Pages build succeeded on GitHub.
