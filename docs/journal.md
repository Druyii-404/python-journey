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
- Python 3.14.3 at `C:\Users\<username>\AppData\Local\Python\pythoncore-3.14-64\python.exe`
- pip 26.0.1 wired to the same installation
- Git 2.54.0.windows.1

**VS Code extensions installed:**
- Python (Microsoft) — includes Pylance and Python Debugger
- Indent Rainbow
- Error Lens
- GitLens

The Python interpreter was manually selected in VS Code via `Ctrl+Shift+P → Python: Select Interpreter` to ensure VS Code was pointed at the correct installation.

**Git was configured** with user identity and the default branch name updated from `master` to `main` to match GitHub's modern default.

**GitHub repository** `python-journey` created at `https://github.com/Druyii-404/python-journey`, cloned locally to `C:\Users\<username>\Documents\Projects\python-journey`, files added, and first commit pushed successfully.

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
