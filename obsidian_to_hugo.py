"""
obsidian_to_hugo.py
===================
Converts Obsidian .md files into Hugo-compatible markdown and copies
them to the right folder in your Hugo project.

REQUIREMENTS: Python 3.6+  —  no extra libraries needed.

HOW TO USE:
  py obsidian_to_hugo.py
  (or drag-and-drop a .md file onto this script in Explorer)
"""

import re
import sys
from pathlib import Path
from datetime import date

# ══════════════════════════════════════════════════════════════════
#  CONFIGURE THESE PATHS FOR YOUR MACHINE
# ══════════════════════════════════════════════════════════════════

HUGO_CONTENT = Path(r"F:\Personal Projects\Programming\Projects\Hugo\boundlessandtimelesswiki\content")

BASE = r"F:\Obsidian Notes\DungeonMaster\Campaign\AdventureThroughPlaneandTime\BoundlessandTimeless"

# Each entry is a label → Obsidian folder path.
# These show up in the source menu so you pick a folder, then pick a file.
OBSIDIAN_SOURCES = {
    "Ellenlyf Party — Session Notes":   Path(BASE + r"\00.Introduction\02.Players\Ellenlyf Party\Party Session Notes"),
    "C'est La Vie Party — Session Notes":Path(BASE + r"\00.Introduction\02.Players\Cest La Vie Party\Party Session Notes"),
    "Ellenlyf Party — Player Characters":Path(BASE + r"\00.Introduction\02.Players\Ellenlyf Party"),
    "C'est La Vie — Player Characters":  Path(BASE + r"\00.Introduction\02.Players\Cest La Vie Party"),
    "NPCs — War-Torn / Shattar-Kai":     Path(BASE + r"\01.Into The Stories\02.ACT1.Artifacts Hunting\War-Torn Plane - Stalemate of the Titans\Main NPC"),
    "NPCs — Frontier / Fistful of Schemes": Path(BASE + r"\01.Into The Stories\02.ACT1.Artifacts Hunting\Tech-Dominant Plane - A Fistful of Schemes\Main NPC"),
    "NPCs — Barovia / Sunless World":    Path(BASE + r"\01.Into The Stories\02.ACT1.Artifacts Hunting\Sunless World - The Hidden Truth\Main NPC"),
    "NPCs — Aruendel / Father's Burden": Path(BASE + r"\01.Into The Stories\02.ACT1.Artifacts Hunting\Paladin's Past - A Father's Burden\Character"),
    "NPCs — Bureau of Time and Plane":   Path(BASE + r"\02.NPCs&Factions\Bureau of Time and Plane"),
    "House Rules":                        Path(BASE + r"\00.Introduction\01.Houses Rules"),
}

# ══════════════════════════════════════════════════════════════════
#  HUGO DESTINATION FOLDERS  (relative to HUGO_CONTENT)
# ══════════════════════════════════════════════════════════════════

DESTINATIONS = {
    "1":  {"label": "Ellenlyf Party — session note",      "path": "campaigns/boundless-and-timeless/session-notes/ellenlyf-party",     "naming": "number"},
    "2":  {"label": "C'est La Vie Party — session note",  "path": "campaigns/boundless-and-timeless/session-notes/cestlavie-party",     "naming": "number"},
    "3":  {"label": "NPC — Shattar-Kai",                  "path": "campaigns/boundless-and-timeless/npcs/shattar-kai",                 "naming": "keep"},
    "4":  {"label": "NPC — The Frontier",                 "path": "campaigns/boundless-and-timeless/npcs/thefrontier",                 "naming": "keep"},
    "5":  {"label": "NPC — Bureau of Time and Plane",     "path": "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane",         "naming": "keep"},
    "6":  {"label": "NPC — Aruendel",                     "path": "campaigns/boundless-and-timeless/npcs/aruendel",                    "naming": "keep"},
    "7":  {"label": "NPC — Barovia",                      "path": "campaigns/boundless-and-timeless/npcs/barovia",                     "naming": "keep"},
    "8":  {"label": "NPC — Verdant's Maw",                "path": "campaigns/boundless-and-timeless/npcs/verdant-maw",                 "naming": "keep"},
    "9":  {"label": "Player Character",                   "path": "campaigns/boundless-and-timeless/player-characters",                "naming": "keep"},
    "10": {"label": "House Rule",                         "path": "house-rules",                                                      "naming": "keep"},
    "0":  {"label": "Custom path (I'll type it)",         "path": None,                                                               "naming": "keep"},
}

# ══════════════════════════════════════════════════════════════════
#  CHARACTER REGISTRY
#  Maps Obsidian [[wiki link names]] → Hugo page paths.
#  Add new characters here as you create their Hugo pages.
#  Paths are relative to content/ — no leading slash needed.
# ══════════════════════════════════════════════════════════════════

CHARACTER_SLUGS = {
    # ── Player Characters — Ellenlyf ──────────────────────────────
    "Sephire":               "campaigns/boundless-and-timeless/player-characters/sephire",
    "Kairos":                "campaigns/boundless-and-timeless/player-characters/kairos",
    "Froggo":                "campaigns/boundless-and-timeless/player-characters/froggo",
    "Minerva":               "campaigns/boundless-and-timeless/player-characters/minerva",
    "Verdian Suyanti":       "campaigns/boundless-and-timeless/player-characters/verdian-suyanti",
    "Asep":                  "campaigns/boundless-and-timeless/player-characters/asep",
    # ── Player Characters — C'est La Vie ──────────────────────────
    "Gwyn":                  "campaigns/boundless-and-timeless/player-characters/gwyn",
    "Ashenka Rois":          "campaigns/boundless-and-timeless/player-characters/ashenka-rois",
    "Whisky":                "campaigns/boundless-and-timeless/player-characters/whisky",
    "Alizar Valts":          "campaigns/boundless-and-timeless/player-characters/alizar-valts",
    "Jeno":                  "campaigns/boundless-and-timeless/player-characters/jeno",
    "Klir":                  "campaigns/boundless-and-timeless/player-characters/klir",
    # ── NPCs — Aruendel ───────────────────────────────────────────
    "The Daughter":          "campaigns/boundless-and-timeless/npcs/aruendel/the-daughter",
    "Elira":                 "campaigns/boundless-and-timeless/npcs/aruendel/the-daughter",
    "The Don Quixote":       "campaigns/boundless-and-timeless/npcs/aruendel/the-don-quixote",
    "The Mother":            "campaigns/boundless-and-timeless/npcs/aruendel/the-mother",
    "Selaveth":              "campaigns/boundless-and-timeless/npcs/aruendel/the-mother",
    "The Paladin":           "campaigns/boundless-and-timeless/npcs/aruendel/the-paladin",
    "Ser Aldric":            "campaigns/boundless-and-timeless/npcs/aruendel/the-paladin",
    "Aldric":                "campaigns/boundless-and-timeless/npcs/aruendel/the-paladin",
    # ── NPCs — Bureau of Time and Plane ───────────────────────────
    "Awanama":               "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane/awanama",
    "Damian":                "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane/damian-the-squeeky-devils",
    "Grand Library":         "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane/grand-library",
    "Pustakawan":            "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane/pustakawan",
    "Shaperite":             "campaigns/boundless-and-timeless/npcs/bureauoftimeandplane/shaperite",
    # ── NPCs — Shattar-Kai ────────────────────────────────────────
    "Ember":                 "campaigns/boundless-and-timeless/npcs/shattar-kai/ember",
    "Eric Valtan":           "campaigns/boundless-and-timeless/npcs/shattar-kai/eric-valtan",
    "Father Malen":          "campaigns/boundless-and-timeless/npcs/shattar-kai/father-malen",
    "General Valtan":        "campaigns/boundless-and-timeless/npcs/shattar-kai/general-valtan",
    "Nikael of Fire Banner": "campaigns/boundless-and-timeless/npcs/shattar-kai/nikael-of-fire-banner",
    "Sofia Fyrwurd":         "campaigns/boundless-and-timeless/npcs/shattar-kai/sofia-fyrwurd",
    # ── NPCs — The Frontier ───────────────────────────────────────
    "Angel Eye":             "campaigns/boundless-and-timeless/npcs/thefrontier/angel-eye",
    "Baron Blackthorn":      "campaigns/boundless-and-timeless/npcs/thefrontier/baron-blackthorn",
    "Marshal Eliza Kane":    "campaigns/boundless-and-timeless/npcs/thefrontier/marshal-eliza-kane",
    "Professor Thinkwistle": "campaigns/boundless-and-timeless/npcs/thefrontier/professor-thinkwistle",
    "Red Jack The Showman":  "campaigns/boundless-and-timeless/npcs/thefrontier/red-jack-the-showman",
    # ── NPCs — Barovia ────────────────────────────────────────────
    "Hawa":                  "campaigns/boundless-and-timeless/npcs/barovia/hawa",
    "HAWA":                  "campaigns/boundless-and-timeless/npcs/barovia/hawa",
    # ── NPCs — Verdant's Maw ──────────────────────────────────────
    "Guardian":              "campaigns/boundless-and-timeless/npcs/verdant-maw/guardian",
}

# ══════════════════════════════════════════════════════════════════
#  OBSIDIAN CALLOUT → HUGO MARKDOWN ALERT MAPPING
#  Hugo v0.154+ deprecated {{< hint >}} in favour of
#  native markdown alerts:  > [!NOTE], > [!TIP], etc.
# ══════════════════════════════════════════════════════════════════

CALLOUT_MAP = {
    # Obsidian type  →  Hugo/GitHub markdown alert type
    "info":      "NOTE",
    "note":      "NOTE",
    "abstract":  "NOTE",
    "summary":   "NOTE",
    "tip":       "TIP",
    "hint":      "TIP",
    "important": "IMPORTANT",
    "success":   "TIP",
    "check":     "TIP",
    "done":      "TIP",
    "warning":   "WARNING",
    "caution":   "CAUTION",
    "attention": "WARNING",
    "failure":   "WARNING",
    "fail":      "WARNING",
    "missing":   "WARNING",
    "danger":    "CAUTION",
    "error":     "CAUTION",
    "bug":       "CAUTION",
    "question":  "NOTE",
    "help":      "NOTE",
    "faq":       "NOTE",
    "example":   "NOTE",
    "quote":     "NOTE",
    "cite":      "NOTE",
    "todo":      "WARNING",
}

# Obsidian-only frontmatter keys — stripped before publishing
OBSIDIAN_FM_FIELDS = {
    "ImportedOn", "RWtopicId", "parent", "up", "prev", "next",
    "bookmarked", "cssclasses", "cssclass", "kanban-plugin",
    "excalidraw-plugin", "excalidraw-open-md",
}


# ══════════════════════════════════════════════════════════════════
#  CONVERSION FUNCTIONS
# ══════════════════════════════════════════════════════════════════

def slugify(name: str) -> str:
    """Convert any string to a Hugo-friendly lowercase slug."""
    name = name.lower().strip()
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-")


def parse_obsidian_filename(stem: str) -> tuple[str, str]:
    """
    Parses Obsidian session filenames like:
      "26 - Path Of Righteousness Filled With Wickedness"
      "07 - The Final Stretch of Mages - Bureau Saga"
      "01 - Fire in Highfalls - Neverwinter Saga 1"

    Returns (number, title) — title strips trailing saga/arc labels.
    Returns ("", stem) if the pattern doesn't match (e.g. NPC files).
    """
    m = re.match(r"^(\d+)\s*[-\u2013\u2014]\s*(.+)$", stem)
    if not m:
        return ("", stem)
    num = m.group(1).strip()
    title = m.group(2).strip()
    # Strip trailing arc labels: "- Bureau Saga", "- Neverwinter Saga 1", etc.
    title = re.sub(r"\s*[-\u2013\u2014]\s*[\w][\w\s]+Saga[\w\s]*$", "", title).strip()
    return (num, title)


def strip_obsidian_frontmatter(text: str) -> tuple[str, dict]:
    """
    Parse YAML frontmatter, remove Obsidian-only fields.
    Handles multi-line list values under stripped keys.
    Returns (cleaned_text, dict_of_removed_fields).
    """
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not fm_match:
        return text, {}

    fm_block = fm_match.group(1)
    body = text[fm_match.end():]
    removed = {}
    kept_lines = []
    skip_multiline = False
    current_key = None

    for line in fm_block.splitlines():
        key_match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*)\s*:", line)
        if key_match:
            current_key = key_match.group(1)
            skip_multiline = current_key in OBSIDIAN_FM_FIELDS
            if skip_multiline:
                removed[current_key] = line
                continue
        elif skip_multiline and (
            line.startswith("  ") or line.startswith("\t") or line.strip().startswith("-")
        ):
            removed.setdefault(current_key, "")
            removed[current_key] += "\n" + line
            continue
        else:
            skip_multiline = False
        kept_lines.append(line)

    return "---\n" + "\n".join(kept_lines) + "\n---\n" + body, removed


def inject_frontmatter(text: str, title: str, num: str) -> str:
    """
    Ensure title, date, and weight exist in frontmatter.
    Injects them at the TOP of the frontmatter block so they're
    easy to find. Never overwrites fields that already exist.
    """
    fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not fm_match:
        # No frontmatter at all — create a minimal one
        additions = []
        if title:
            additions.append(f'title: "{title}"')
        additions.append(f"date: {date.today().isoformat()}")
        if num:
            additions.append(f"weight: {int(num)}")
        return "---\n" + "\n".join(additions) + "\n---\n" + text

    fm = fm_match.group(1)
    body = text[fm_match.end():]
    injected = []

    if title and not re.search(r"^title\s*:", fm, re.MULTILINE):
        injected.append(f'title: "{title}"')

    if not re.search(r"^date\s*:", fm, re.MULTILINE):
        injected.append(f"date: {date.today().isoformat()}")

    if num and not re.search(r"^weight\s*:", fm, re.MULTILINE):
        injected.append(f"weight: {int(num)}")

    if injected:
        fm = "\n".join(injected) + "\n" + fm

    return f"---\n{fm}\n---\n{body}"


def convert_wiki_links(text: str) -> tuple[str, list[str]]:
    """
    [[Name]]         → [Name]({{< relref "path" >}})
    [[Name|Display]] → [Display]({{< relref "path" >}})

    Unknown names → plain bold text + inline comment (no broken Hugo refs).
    Returns (converted_text, list_of_unknown_names).
    """
    unknown = []

    def replace_link(m):
        inner = m.group(1)
        if "|" in inner:
            name, display = inner.split("|", 1)
            name, display = name.strip(), display.strip()
        else:
            name = display = inner.strip()

        if name in CHARACTER_SLUGS:
            path = CHARACTER_SLUGS[name]
            return f'[{display}]({{{{< relref "{path}" >}}}})'
        else:
            # Plain text — won't break Hugo build, easy to spot and fix
            unknown.append(name)
            return f"**{display}** <!-- FIXME [[{name}]] not in CHARACTER_SLUGS -->"

    converted = re.sub(r"\[\[([^\]]+)\]\]", replace_link, text)
    return converted, unknown


def convert_callouts(text: str) -> str:
    """
    Converts Obsidian callout blocks to Hugo/GitHub markdown alert format.

    Obsidian:              Hugo (markdown alerts, no shortcode needed):
    > [!INFO] Title   →   > [!NOTE]
    > body line 1     →   > **Title**
    > body line 2     →   > body line 1
                          > body line 2

    This format works natively in Hugo v0.154+ without any shortcode.
    The {{< hint >}} shortcode is deprecated in your Hugo version.
    """
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        m = re.match(r"^>\s*\[!([A-Za-z]+)\][-+]?\s*(.*)?$", line)
        if m:
            callout_type = m.group(1).lower()
            callout_title = (m.group(2) or "").strip()
            alert_type = CALLOUT_MAP.get(callout_type, "NOTE")

            # Collect body lines (all subsequent > lines)
            body_lines = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                body_lines.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1

            # Emit markdown alert
            result.append(f"> [!{alert_type}]")
            if callout_title:
                result.append(f"> **{callout_title}**")
            for bl in body_lines:
                result.append(f"> {bl}" if bl.strip() else ">")
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def fix_image_paths(text: str) -> str:
    """
    z_Assets/Misc/Fin.webp              -> /images/Fin.webp
    Numbered vault paths (03.x/...)     -> FIXME comment (can't auto-resolve)
    """
    # Obsidian z_Assets paths
    def fix_zassets(m):
        filename = Path(m.group(2).replace("\\", "/")).name
        return f"![{m.group(1)}](/images/{filename})"
    text = re.sub(r"!\[([^\]]*)\]\(z_Assets/([^)]+)\)", fix_zassets, text)

    # Numbered vault relative paths (Windows-style)
    def fix_numbered(m):
        filename = Path(m.group(2).replace("\\", "/")).name
        return f"![{m.group(1)}](/images/{filename}) <!-- FIXME copy {filename} to static/images/ -->"
    text = re.sub(r"!\[([^\]]*)\]\(([0-9]+\.[^)]+)\)", fix_numbered, text)

    # Vault-relative .md links (e.g. bestiary links)
    text = re.sub(
        r"\[([^\]]+)\]\([0-9]+\.[^\)]+\.md[^\)]*\)",
        lambda m: f"**{m.group(1)}** <!-- FIXME vault-relative link, update manually -->",
        text,
    )
    return text


def remove_templater_cursors(text: str) -> str:
    """Remove unfired Templater placeholder syntax: <% tp.file.cursor() %>"""
    text = re.sub(r"<%[-_]?\s*tp\.[^%]+%>", "", text)
    text = re.sub(r"<%[-_]?\s*[^%]+%>", "", text)
    return text


def remove_ob_timelines(text: str) -> str:
    """Strip ob-timelines plugin divs (inert in Hugo, invisible to readers)."""
    return re.sub(
        r"<div[^>]*class=['\"]ob-timelines['\"][^>]*>.*?</div>",
        "<!-- TIMELINE ob-timelines removed — convert to prose if needed -->",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )


def convert_file(source: Path, title: str = "", num: str = "") -> str:
    """
    Run the full conversion pipeline on a file.
    Returns the converted text as a string.
    """
    text = source.read_text(encoding="utf-8", errors="replace")
    print(f"\n  Converting: {source.name}")

    # 1. Strip Obsidian-only frontmatter fields
    text, removed = strip_obsidian_frontmatter(text)
    if removed:
        print(f"  Stripped fields: {', '.join(removed.keys())}")

    # 2. Remove Templater cursors and ob-timelines blocks
    text = remove_templater_cursors(text)
    text = remove_ob_timelines(text)

    # 3. Convert wiki links
    wl_count = len(re.findall(r"\[\[", text))
    text, unknowns = convert_wiki_links(text)
    if wl_count:
        resolved = wl_count - len(unknowns)
        print(f"  Wiki links: {resolved}/{wl_count} resolved", end="")
        if unknowns:
            print(f"  |  {len(unknowns)} unknown: {', '.join(set(unknowns))}")
        else:
            print()

    # 4. Convert Obsidian callouts → markdown alerts
    cl_count = len(re.findall(r"^>\s*\[!", text, re.MULTILINE))
    text = convert_callouts(text)
    if cl_count:
        print(f"  Callouts: {cl_count} converted to markdown alerts")

    # 5. Fix image paths
    text = fix_image_paths(text)

    # 6. Inject missing frontmatter fields (title, date, weight)
    text = inject_frontmatter(text, title, num)

    fixmes = text.count("FIXME")
    if fixmes:
        print(f"  FIXMEs:  {fixmes} — open in VSCode, Ctrl+F 'FIXME' to resolve")

    return text


# ══════════════════════════════════════════════════════════════════
#  INTERACTIVE CLI
# ══════════════════════════════════════════════════════════════════

def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{prompt}{suffix}: ").strip()
    return val if val else default


def pick_source_folder() -> Path:
    """
    Show a numbered menu of known Obsidian source folders.
    Returns the chosen Path.
    """
    keys = list(OBSIDIAN_SOURCES.keys())
    col_w = max(len(k) for k in keys) + 2

    print("\n  Which Obsidian folder are you converting from?\n")
    for i, key in enumerate(keys, 1):
        path = OBSIDIAN_SOURCES[key]
        status = "✓" if path.exists() else "✗ path not found"
        print(f"    {i:2})  {key:{col_w}}  {status}")
    print(f"\n     0)  Enter path manually")

    while True:
        choice = ask("\n  Enter number").strip()
        if choice == "0":
            raw = ask("  Full path to folder").strip().strip("\"'")
            return Path(raw)
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return OBSIDIAN_SOURCES[keys[int(choice) - 1]]
        print("  Invalid — enter a number from the list.")


def list_folder_files(folder: Path) -> list[Path]:
    """
    List .md files in the given folder, directly (not recursive).
    Skips files starting with _ (index files, templates).
    """
    return sorted(
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() == ".md" and not f.stem.startswith("_")
    )


def pick_file_from_folder(folder: Path) -> Path | None:
    """
    Show numbered file list, return chosen Path or None if cancelled.
    Displays parsed session number + title for easy scanning.
    """
    files = list_folder_files(folder)
    if not files:
        print(f"\n  No .md files found in:\n  {folder}")
        return None

    print(f"\n  Files in: {folder.name}  ({len(files)} found)\n")
    for i, f in enumerate(files, 1):
        num, title = parse_obsidian_filename(f.stem)
        label = f"[{int(num):02d}] {title}" if num else f.stem
        print(f"    {i:3})  {label}")

    while True:
        choice = ask("\n  Enter number (or 0 to go back)").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        print("  Invalid — enter a number from the list.")


def pick_destination() -> tuple[Path, str]:
    """Return (dest_folder_path, naming_mode)."""
    print("\n  Where should this file go in Hugo?\n")
    for key, info in DESTINATIONS.items():
        print(f"    {key:2})  {info['label']}")

    while True:
        choice = ask("\n  Enter number").strip()
        info = DESTINATIONS.get(choice)
        if not info:
            print("  Invalid — enter a number from the list.")
            continue
        if info["path"] is None:
            custom = ask("  Relative path from Hugo content/")
            return HUGO_CONTENT / custom, "keep"
        return HUGO_CONTENT / info["path"], info["naming"]


def build_output_filename(source: Path, naming: str, num: str, title: str) -> str:
    """
    Determine the Hugo output filename based on naming mode.
      number → 27.md  (zero-padded)
      keep   → slugified version of original stem
    """
    if naming == "number" and num:
        return f"{int(num):02d}.md"
    # Default: slugify the original filename
    return slugify(source.stem) + ".md"


# ══════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("  Obsidian  ->  Hugo Converter")
    print("  Boundless and Timeless Wiki")
    print("=" * 60)

    if not HUGO_CONTENT.exists():
        print(f"\n  ERROR: Hugo content folder not found:")
        print(f"  {HUGO_CONTENT}")
        print(f"\n  Edit HUGO_CONTENT at the top of this script.")
        input("  Press Enter to exit...")
        return

    # ── Step 1: Get the source .md file ──────────────────────────
    if len(sys.argv) > 1:
        # Drag-and-drop a .md file onto the script in Explorer
        source = Path(sys.argv[1].strip("\"'"))
        print(f"\n  File dropped: {source.name}")
    else:
        source_folder = pick_source_folder()

        if not source_folder.exists():
            print(f"\n  ERROR: Folder not found:\n  {source_folder}")
            print(f"  Check the path in OBSIDIAN_SOURCES at the top of the script.")
            input("  Press Enter to exit...")
            return

        source = pick_file_from_folder(source_folder)
        if source is None:
            print("  Cancelled.")
            input("  Press Enter to exit...")
            return

    if not source.exists() or source.is_dir():
        print(f"\n  ERROR: File not found: {source}")
        input("  Press Enter to exit...")
        return

    if source.suffix.lower() != ".md":
        print(f"\n  ERROR: Not a .md file: {source.name}")
        input("  Press Enter to exit...")
        return

    # ── Step 2: Parse filename → number + title ───────────────────
    num, parsed_title = parse_obsidian_filename(source.stem)

    if num and parsed_title:
        print(f"\n  Detected:  #{int(num):02d}  —  {parsed_title}")
        confirm_title = ask("  Use as Hugo title? (y/n)", "y").lower()
        if confirm_title != "y":
            parsed_title = ask("  Title", source.stem)
            num = ask("  Session number", num)
    else:
        # NPC or other file — use the stem directly (will be slugified)
        parsed_title = source.stem

    # ── Step 3: Pick Hugo destination ────────────────────────────
    dest_folder, naming = pick_destination()
    output_name = build_output_filename(source, naming, num, parsed_title)
    dest_path = dest_folder / output_name

    # ── Step 4: Review and confirm ───────────────────────────────
    print(f"\n  {'─' * 54}")
    print(f"  Source  :  {source.name}")
    print(f"  Title   :  {parsed_title}")
    print(f"  Dest    :  {dest_path}")
    print(f"  URL     :  .../{output_name.replace('.md', '')}/")
    print(f"  {'─' * 54}")

    if dest_path.exists():
        print(f"\n  File already exists at destination.")
        if ask("  Overwrite? (y/n)", "n").lower() != "y":
            print("  Cancelled.")
            input("  Press Enter to exit...")
            return

    if ask("\n  Proceed? (y/n)", "y").lower() != "y":
        print("  Cancelled.")
        input("  Press Enter to exit...")
        return

    # ── Step 5: Convert and write ─────────────────────────────────
    converted = convert_file(source, title=parsed_title, num=num)

    dest_folder.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(converted, encoding="utf-8")

    # ── Step 6: Summary ───────────────────────────────────────────
    print(f"\n  ✓ Done!  ->  {dest_path}")
    fixmes = converted.count("FIXME")
    if fixmes:
        print(f"\n  {fixmes} FIXME(s) to review:")
        print(f"    Open in VSCode, press Ctrl+F, search for FIXME")
        print(f"    These are plain comments — Hugo builds fine without fixing them.")
        print(f"    But clean them up before sharing the link with players.")
    print(f"\n  Next:")
    print(f"    1. Fix any FIXMEs in VSCode")
    print(f"    2. Copy new images to your Hugo static/images/ folder")
    print(f"    3. git add  +  git commit  +  git push  ->  Cloudflare builds")
    print()
    input("  Press Enter to exit...")


if __name__ == "__main__":
    main()