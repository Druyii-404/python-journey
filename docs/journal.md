# Learning Journal

*A session-by-session account of the Python learning journey — dates, decisions, detours, mistakes, and milestones.*

---

## About This Document

**Style:** Personal journal / development log  
**Companion documents:** [Encyclopedia](encyclopedia.md) · [Guidebook](guidebook.md)  
**Repository:** [README](../README.md)

This document is the rawest of the three. Where the [Guidebook](guidebook.md) presents a clean, ordered understanding and the [Encyclopedia](encyclopedia.md) is a polished reference, the journal is honest. It records what actually happened in each session — including where the plan deviated, where something was harder than expected, and where a mistake turned into a useful lesson.

Each session entry follows a consistent format. Entries are listed in reverse chronological order (newest first) for easy reference.

---

## AI Assistance Record

This project uses AI as a supporting tool — as a guide, coach, and documentation assistant. It does not write code on behalf of the learner. The model in use is tracked below, and any model change is recorded with its date so readers can understand any shifts in the project's voice or approach.

| Model | Version | Active From | Active To |
|-------|---------|-------------|-----------|
| Claude Sonnet | 4.6 | June 1, 2026 | present |

---

## Session Entry Format

Every session uses the following structure:

```
---

## Session N — [Date]

**Model active:** [Model name + version]  
**Session focus:** [One-line summary]  
**Documents updated this session:** [List of docs touched]

### What Was Planned
[What we intended to cover]

### What Actually Happened
[What we covered — including deviations from the plan]

### Key Moments
[Specific things that landed, broke, or surprised — the moments worth remembering]

### Mistakes & What They Taught
[Errors, misconceptions corrected, wrong paths taken]

### Added to the Encyclopedia
[Links to new entries in encyclopedia.md]

### Added to the Guidebook
[Links to new/updated sections in guidebook.md]

### Next Session
[What's planned for next time]
```

---

---

## Session 3 — June 2, 2026

**Model active:** Claude Sonnet 4.6
**Session focus:** D&D Character Generator scoping, historical HeroGen review, and project plan
**Documents updated this session:** Journal (this entry), README (project scope), created `projects/dnd_character_generator/BRIEF.md`

### What Was Planned

Scope the D&D Character Generator before writing any code — agreeing on what the program needs to do, how ambitious to be, and how to approach it as a learning vehicle.

### What Actually Happened

The session opened with a privacy fix: the Session 2 journal entry contained the actual GitHub username in a repository URL. This was corrected to `yourusername` as a generic placeholder, and a standing rule was established — any personally identifying paths, usernames, or account details are anonymised before being written to these documents, not after.

**Historical review — HeroGen (May–July 2020)**

Before scoping the new project, the original self-taught attempt was reviewed in full. The project consisted of ten files:

- `Hero_Generator.py` — the main entry point, importing from all other modules
- `Race_Picker.py` — 16 races with subrace logic, Dragonborn colour variants, Half-Elf special handling
- `Class_Picker.py` — 12 classes with subclass variants (Cleric domains, Sorcerer origins, Warlock patrons, Fighter styles, Ranger features)
- `Stat_Gen.py` — 4d6 drop-lowest stat generation across a pool of six
- `Background_Gen.py` — 13 PHB backgrounds with full personality, ideal, bond, and flaw tables, plus variants
- `Trinket_Gen.py` — 100-item trinket pool
- `Dice Rolls.py` — a dice utility module (d2 through d100)
- `Core_v3.py` — an earlier iteration of the stat roller
- `Playground.py` — isolated test code for skill proficiency logic
- `Abilities_List.py` — a stub placeholder (just the word "abilities")

The original inspiration was [Who the f*** is my DND character?](https://whothefuckismydndcharacter.com/) — a flavour-first generator. What was actually built went considerably further: a mechanically complete Level 1 character generator covering stats, skills, saves, features, spells, equipment, languages, armor class, health, money, and personality. The earliest file is dated May 13, 2020; the latest July 5, 2020.

**What HeroGen revealed**

The code was functional but showed the characteristic patterns of self-taught work — things that worked without necessarily being understood:

- **Lists of lists** used everywhere because dictionaries weren't known. Positions like `race[7]` for speed, `race[8]` for skills, `race[9]` for languages — readable to nobody.
- **`while len(x) <= N`** used instead of `for` loops throughout.
- **The same 18-branch `if/elif` chain** for skill proficiency checking written three times over (once for race, once for background, once for class).
- **String concatenation** with `+` and `str()` instead of f-strings.
- **Modules that run code on import** — `stat_pool()` fires the moment `Stat_Gen` is imported, which is a structural problem.
- **`from math import *`** used just to access `floor()`.

None of this prevented the code from working. All of it is what the rebuild is for.

**Scoping decisions made**

The project was scoped in three phases:

- **Phase 1 — Core rebuild:** Regenerate all of HeroGen's output using proper Python — dictionaries instead of indexed lists, `for` loops, f-strings, clean functions, modules that don't execute on import.
- **Phase 2 — Desktop UI:** A `tkinter` window with a Generate button. Character sheet displayed in the app. Possibly with options to lock a race or class before generating.
- **Phase 3 — PDF export:** Map the generated character onto the official 5e fillable character sheet PDF using `pypdf`, producing a file ready to print and play.

The UI choice was deliberate: `tkinter` (desktop window) was chosen over a browser-based interface (Flask) because it stays within Python fundamentals, introduces GUI concepts without web dependencies, and produces a more satisfying standalone result. A web interface remains a future option but isn't the immediate learning priority.

### Key Moments

- **HeroGen was more complete than expected** — reviewing it made clear that the gap isn't "I've never done this," it's "I did this without fully understanding it." The rebuild is about closing that gap.
- **The instinct vs. understanding framing** — the clearest way to articulate what's different about the new project: the old code shows what was achievable by feel; the new code will show what's achievable by comprehension.
- **PDF as the finish line** — the decision that the final output should be a playable character sheet, not just terminal output, gives the project a concrete and satisfying end state.

### Mistakes & What They Taught

- **Privacy oversight from Session 2** — the GitHub username had been written directly into the journal. Public repositories need all identifying information removed before it's committed, not corrected after. The fix is simple; the habit is what matters.

### Added to the Encyclopedia

No Python syntax entries — this was a planning session.

### Added to the Guidebook

No new chapters — this was a planning session.

### Next Session

- First Python concepts: variables, data types, `print()`
- First Encyclopedia entries
- First lines of code written for the D&D Character Generator
- Starting point: understanding what a variable is before building the race dictionary

---

## Session 2 — June 1, 2026

**Model active:** Claude Sonnet 4.6
**Session focus:** Development environment verification, VS Code extensions, Git configuration, GitHub repository setup
**Documents updated this session:** Journal (this entry), Guidebook (Chapter 0 completed)

### What Was Planned

Verify and clean up the existing Python and Git installations, install the core VS Code extensions, configure GitHub, and get the three documents pushed to a live public repository.

### What Actually Happened

The session ran largely to plan, though the environment threw up several issues that needed working through before the clean setup was confirmed — which is normal for a first-time Windows dev environment.

**Python verification** revealed the installation was coming from a Microsoft Store App Execution Alias rather than a proper python.org installation. The distinction matters because Store-based Python causes silent problems with pip, virtual environments, and VS Code's interpreter detection. Python was reinstalled from python.org (via winget, resulting in the `pythoncore-3.14-64` installation), the Store aliases were toggled off and back on via Settings → Apps → Advanced app settings → App execution aliases, and the installation was confirmed clean using `python -c "import sys; print(sys.executable)"`.

**Final confirmed environment:**
- Python 3.14.3 at `C:\Users\yourusername\AppData\Local\Python\pythoncore-3.14-64\python.exe`
- pip 26.0.1 wired to the same installation
- Git 2.54.0.windows.1

**VS Code extensions installed:**
- Python (Microsoft) — includes Pylance and Python Debugger
- Indent Rainbow
- Error Lens
- GitLens

The Python interpreter was manually selected in VS Code via `Ctrl+Shift+P → Python: Select Interpreter` to ensure VS Code was pointed at the correct installation.

**Git was configured** with user identity and the default branch name updated from `master` to `main` to match GitHub's modern default.

**GitHub repository** `python-journey` created at `https://github.com/yourusername/python-journey`, cloned locally to `C:\Users\yourusername\Documents\Projects\python-journey`, files added, and first commit pushed successfully.

### Key Moments

- **First terminal command** — the very first command typed was `copilot-debug <your command here>python --version`, including the placeholder text literally. A good early lesson: read the full command before hitting Enter, especially when copying from somewhere else.
- **The `where` alias problem** — `where python` in PowerShell returned nothing because `where` is aliased to `Where-Object` in PowerShell, not the Windows `where.exe` command. Silent non-answers in a terminal are often caused by running a different command than intended. The fix is `where.exe python` or `Get-Command python`.
- **Microsoft Store Python** — the `Get-Command python` output showing `Version 0.0.0.0` was the tell. App Execution Aliases always report 0.0.0.0 regardless of what they point to; it's not a broken version number, it's just metadata about the alias wrapper itself.
- **First commit and push** — the four-stage Git mental model (untracked → staged → committed → pushed) was introduced and executed successfully. The repository is live and public.

### Mistakes & What They Taught

- **`python -- version` with a space** — typing `python -- version` instead of `python --version` caused Python to treat `version` as a filename to execute rather than a flag. The error message was accurate but confusing without knowing why. Command-line flags have no space between `--` and the flag name.
- **The `(END)` pager** — after running `git config --list`, the output opened in `less` (Git's pager for long output) and the terminal appeared stuck. Pressing `q` exits the pager. This will appear again.
- **Placeholder text** — treated instructional template text as part of the command to type. Terminal prompts do exactly what you tell them, including the parts you didn't mean.

### Added to the Encyclopedia

No Python syntax entries yet — the session was environment setup only.

### Added to the Guidebook

- Chapter 0 fully written: [Before the First Line — Setting Up](guidebook.md#chapter-0-before-the-first-line--setting-up)

### Next Session

- Scope the D&D Character Generator — define what the program needs to do before writing any code
- First Python concepts: variables, data types, `print()`
- First Encyclopedia entries expected

---

---

## Session 1 — June 1, 2026

**Model active:** Claude Sonnet 4.6  
**Session focus:** Project scoping, document architecture, and establishing ground rules  
**Documents updated this session:** README, Encyclopedia (structure), Guidebook (structure + Ch.0 outline), Journal (this entry)

### What Was Planned

The initial session had no code in it by design. The goal was to establish the project properly before touching Python — agreeing on structure, purpose, and the working relationship between learner and AI guide.

### What Actually Happened

The session opened with a detailed project brief covering three purposes: guided Python learning (coaching-not-writing), living documentation, and broader development environment oversight. There was also an articulation of long-term influences — Sebastian Lague's creative/visual coding style, and a physical computing interest shaped by Azeron-style devices and the atarabyte community.

A frank assessment of scope was requested. The conclusion was:

- Core learning path (Python → creative coding → physical computing) is coherent and well-motivated
- PCB/hardware design and home networking are valid long-term interests but deliberately parked — out of scope for the foreseeable future
- The three-document system is a strong structural choice
- The biggest risk is documents falling behind sessions — agreed to do update passes at the end of each session

A decision was made to begin coding with a **D&D player character generator** — a project previously attempted independently, chosen because it exercises core competencies (variables, data types, control flow, functions, collections) without requiring external libraries.

The three documents and repository structure were then designed and created, including:
- Consistent cross-referencing via relative markdown links
- AI model tracking tables in all three documents and the README
- A session entry template for the journal
- A GitHub-ready folder structure (`/docs`, `/projects`)

### Key Moments

- **Scope calibration:** The conversation about which interests genuinely connect to Python (almost everything except PCB design and networking) was useful — the learner arrived with broad interests and left with a phased framing that doesn't require abandoning anything, just sequencing it.
- **AI transparency decision:** The learner specifically asked for AI use to be disclosed prominently and for the model to be tracked. This was built in as a first-class feature of all documents rather than a footnote.
- **Document philosophy:** The distinction between the three documents was clarified — encyclopedia is for *lookup*, guidebook is for *understanding*, journal is for *honesty*. Each serves a different reader state.

### Mistakes & What They Taught

No coding yet — no code mistakes. The one structural note: the original project brief included home networking and PCB design without a clear sense of their distance from the Python track. Working through the scope assessment clarified that these aren't Python extensions — they're separate disciplines. Better to name that clearly at the start than discover it after frustration.

### Added to the Encyclopedia

- Document structure and category framework established (no content entries yet)

### Added to the Guidebook

- Chapter 0 outline created: *Before the First Line — Setting Up*
- Content pending until dev environment session

### Next Session

- Set up the development environment (Python installation, VS Code, recommended extensions, terminal basics)
- Begin the D&D Character Generator project — scoping what the program needs to do before writing any code
- First Encyclopedia entries expected: data types, variables, `print()`

---

---

*Entries above this line are the most recent. Scroll down for earlier sessions.*

*For the structured understanding behind what's learned here, see the [Guidebook](guidebook.md). For quick syntax lookup, see the [Encyclopedia](encyclopedia.md).*
