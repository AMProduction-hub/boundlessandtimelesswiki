# Hugo Smart Layouts — Setup Guide

Drop everything in this zip into your Hugo project root. Merge with existing folders.

---

## What's in here

```
data/
  characters.yaml              ← central character registry

layouts/
  shortcodes/
    npc.html                   ← {{< npc "Father Malen" >}}
    pc.html                    ← {{< pc "Sephire" >}}
    latest-session.html        ← {{< latest-session party="ellenlyf-party" >}}
  partials/
    session-list.html          ← auto-generates session list from files
    docs/inject/
      head.html                ← (unchanged — just loads custom.css)
  _default/
    session-index.html         ← layout for party index pages

static/
  custom.css                   ← replace your existing one
```

---

## Step 1 — Drop files in, replace custom.css

Copy everything into your Hugo project root.
When prompted to merge folders — yes.
When prompted about custom.css — replace it.

---

## Step 2 — Update each party _index.md

Open `content/campaigns/boundless-and-timeless/session-notes/ellenlyf-party/_index.md`

Replace the entire file with this minimal version:

```yaml
---
title: "Ellenlyf Party Sessions"
layout: session-index
weight: 30
bookCollapseSection: true
status: "🟢 Active"
current_arc: "Barovia"
---
```

That's it. Delete all the hand-written session list below it.
Hugo generates the list automatically from the .md files in the folder.

Do the same for `cestlavie-party/_index.md`:

```yaml
---
title: "C'est La Vie Party Sessions"
layout: session-index
weight: 40
bookCollapseSection: true
status: "✅ Completed"
current_arc: "Bureau Saga"
---
```

---

## Step 3 — Add saga field to each session note frontmatter

Each session .md file needs a `saga:` field so the list groups correctly.
The sync script (SYNC.bat) will do this for new files automatically.
For existing files, open each one and add it manually — takes about 10 minutes total.

```yaml
---
title: "Session 26 — Path of Righteousness"
weight: 26
date: 2026-01-15
saga: "Barovia"          ← add this line
---
```

Saga values used so far:
- Neverwinter
- Verdant's Maw
- Aruendel
- Shattar-Kai
- Pequod
- The Frontier
- Barovia

---

## Step 4 — Add latest-session card to the main homepage (optional)

In `content/_index.md`, replace the hard-coded session count text with:

```
{{< latest-session party="ellenlyf-party" >}}
```

It will automatically show the newest session and update itself every time you add one.

---

## Step 5 — Add new characters to data/characters.yaml

When you create a new NPC or PC page:

1. Create their `.md` file in the right Hugo content folder
2. Open `data/characters.yaml` and add:

```yaml
"Their Full Name":
  path: /campaigns/boundless-and-timeless/npcs/location/their-slug
  type: npc
```

3. Use `{{< npc "Their Full Name" >}}` anywhere — Hugo finds the page

---

## How sessions auto-update now

Before: add session → edit _index.md list → update session count → update homepage

After: add session .md file → push → done. Everything updates itself.

---

## Character link colours

- Green  = player character (pc)
- Purple = NPC
- Blue   = location

Missing characters (not in characters.yaml) show with a dashed red underline
so you can spot them easily without the build breaking.
