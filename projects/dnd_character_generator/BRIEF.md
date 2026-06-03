# Project Brief: D&D Character Generator

**Repository:** [README](../../README.md)  
**Journal reference:** [Session 3](../../docs/journal.md#session-3--june-2-2026)  
**Status:** In progress — Phase 1 not yet started

---

## Overview

A fully randomised Dungeons & Dragons 5th Edition Level 1 character generator, built across three phases. The project is both a learning vehicle and a functional tool — each phase introduces new Python concepts while producing something progressively more useful.

The end state is a desktop application that generates a complete playable character and exports it to a ready-to-print PDF character sheet.

---

## Historical Context

This is a rebuild, not a first attempt. A version of this project — called **HeroGen** — was self-taught and completed between May and July 2020. HeroGen worked. It produced complete Level 1 characters covering race, class, background, stats, skills, saves, features, equipment, spells, and languages.

What it revealed, on review, were the characteristic patterns of code written by instinct rather than understanding:

- **Lists of lists** used as the primary data structure because dictionaries weren't known. Data was accessed by position (`race[7]` for speed) rather than by name (`race["speed"]`).
- **`while len(x) <= N`** used in place of `for` loops throughout.
- The **same 18-branch `if/elif` chain** for skill proficiencies written three separate times.
- **String concatenation** with `+` and `str()` instead of f-strings.
- **Modules that execute code on import**, causing side effects the moment a file is loaded.

The rebuild replaces each of these patterns with the proper Python approach — not because HeroGen was wrong, but because understanding *why* the better approach is better is the point of the exercise.

---

## Scope

### What it generates

A complete, randomised Level 1 D&D 5e character, including:

- Race (with subrace logic and special cases — Dragonborn colour variants, Half-Elf stat distribution, High Elf cantrip)
- Class (with subclass variants — Cleric domains, Sorcerer origins, Warlock patrons, Fighter styles, Ranger favored enemy/terrain)
- Ability scores (4d6, drop lowest, across a pool of six)
- Background (with personality trait, ideal, bond, and flaw)
- Skill proficiencies (from race, background, and class, with Rogue expertise)
- Saving throw proficiencies
- Features and racial traits (including calculated values like Dragonborn breath weapon DC)
- Armor class (including class-specific formulas for Barbarian, Monk, Draconic Sorcerer)
- Hit points
- Speed
- Languages
- Equipment (randomised per class starting equipment tables)
- Weapon, armor, and tool proficiencies
- Spell pools (cantrips and 1st level spells, for all spellcasting classes)
- Spell save DC and attack modifier
- Money (by background)
- A trinket

### What it does not include

- Multiclassing
- Feats
- Levels above 1
- Subrace options beyond those present in HeroGen
- Races, classes, or backgrounds from sources other than the core PHB and a small number of Sword Coast Adventurer's Guide additions

---

## Phase Breakdown

### Phase 1 — Core Mechanics (Python fundamentals)

**Goal:** Reproduce all of HeroGen's output using proper Python patterns. Terminal output only at this stage.

**Python concepts introduced:**

| Concept | Where it appears |
|---------|-----------------|
| Variables and data types | Storing character name, speed, level |
| `print()` and f-strings | Formatted character output |
| Lists | Spell pools, equipment lists, language lists |
| Dictionaries | Race, class, and background data |
| `random` module | All selection and generation |
| Functions | Generation logic — one function per concern |
| `for` loops | Iterating over skills, features, proficiencies |
| Conditionals | Special case handling (Half-Elf, Dragonborn, etc.) |
| Modules and imports | Splitting generation logic across files |
| `math.floor()` | Ability score modifier calculation |

**Output:** A formatted character sheet printed to the terminal.

---

### Phase 2 — Desktop UI (tkinter)

**Goal:** Wrap the generation engine in a desktop window. The core logic from Phase 1 is unchanged — the UI is a layer on top.

**New concepts introduced:**

| Concept | Where it appears |
|---------|-----------------|
| `tkinter` basics | Window, frame, button, label widgets |
| Event-driven programming | The Generate button calling generation functions |
| Widget layout | Organising the character sheet display |
| Optional: input widgets | Dropdowns to lock a race or class before generating |

**Output:** A standalone desktop application. Click Generate, see a character.

---

### Phase 3 — PDF Export (pypdf)

**Goal:** Map the generated character data onto the official D&D 5e fillable character sheet PDF and save it to disk.

**New concepts introduced:**

| Concept | Where it appears |
|---------|-----------------|
| `pypdf` library | Reading and writing PDF form fields |
| File I/O | Saving the filled PDF to a chosen location |
| Data mapping | Matching generated values to PDF field names |
| Optional: file dialog | `tkinter.filedialog` for save-as prompt |

**Output:** A completed, printable PDF character sheet ready for the table.

---

## Libraries

| Library | Phase | Notes |
|---------|-------|-------|
| `random` | 1 | Built-in |
| `math` | 1 | Built-in (used for `floor()` in modifier calculation) |
| `tkinter` | 2 | Built-in |
| `pypdf` | 3 | Requires `pip install pypdf` |

---

## File Structure (target)

```
projects/dnd_character_generator/
├── BRIEF.md                  ← This document
├── main.py                   ← Entry point (Phase 2+: launches the UI)
├── generator/
│   ├── race.py               ← Race data and selection
│   ├── class_.py             ← Class data and selection
│   ├── background.py         ← Background data and selection
│   ├── stats.py              ← Ability score generation
│   ├── character.py          ← Assembles the full character from components
│   └── spells.py             ← Spell pool data
├── ui/
│   └── app.py                ← tkinter UI (Phase 2)
└── export/
    └── pdf.py                ← PDF generation (Phase 3)
```

*This structure will be established incrementally — early sessions will use a single file.*

---

*For session-by-session progress on this project, see the [Journal](../../docs/journal.md).*
