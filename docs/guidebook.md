# Learning Python: A Personal Guidebook

*A narrative guide to Python, structured for understanding — not necessarily in the order things were learned, but in the order that makes them make sense.*

---

## About This Document

**Style:** O'Reilly-style narrative guidebook  
**Companion documents:** [Encyclopedia](encyclopedia.md) · [Journal](journal.md)  
**Repository:** [README](../README.md)

Where the [Encyclopedia](encyclopedia.md) is a lookup tool, this document is meant to be read. It takes concepts as they emerge across sessions and arranges them into the sequence that best explains *why* things work the way they do — not just *what* they do.

This means chapters may appear or expand after their topics have already been worked through in practice. The guidebook is always slightly behind the sessions, catching up and consolidating as understanding deepens.

The projects built throughout this journey appear here too — not as code dumps, but as worked examples that illustrate the concepts in their surrounding chapters.

---

## AI Assistance Record

This document is maintained with the assistance of an AI model acting as a documentation and teaching guide. Model changes are recorded below.

| Model | Version | Active From | Active To |
|-------|---------|-------------|-----------|
| Claude Sonnet | 4.6 | June 1, 2026 | present |

---

## A Note on the Learning Approach

This guidebook is not the product of a structured course. It grew from real sessions, with real confusion, real wrong turns, and real moments of things suddenly making sense. Where the order of learning was less than ideal, this document reorders it. Where a concept was misunderstood before being corrected, only the correct understanding appears here — the journey to it lives in the [Journal](journal.md).

Python is learned here with purpose — each topic is introduced when it earns its place, usually because a project needs it.

---

## Contents

*Chapters are added as their topics are covered in sessions. The table of contents below reflects the intended eventual structure, with status indicators showing what has been written.*

| Chapter | Title | Status |
|---------|-------|--------|
| 0 | [Before the First Line — Setting Up](#chapter-0-before-the-first-line--setting-up) | ✅ Complete |
| 1 | The Shape of a Python Program | ⏳ Pending |
| 2 | Values, Variables, and Types | ⏳ Pending |
| 3 | Making Decisions — Control Flow | ⏳ Pending |
| 4 | Doing Things Repeatedly — Loops | ⏳ Pending |
| 5 | Organising Code — Functions | ⏳ Pending |
| 6 | Organising Data — Collections | ⏳ Pending |
| 7 | Worked Example: D&D Character Generator | ⏳ Pending |
| 8 | Reading and Writing Files | ⏳ Pending |
| 9 | When Things Go Wrong — Error Handling | ⏳ Pending |
| 10 | Thinking in Objects — OOP | ⏳ Pending |

---

---

## Chapter 0: Before the First Line — Setting Up

*The tools, the environment, and the habits that make everything else possible.*

### 0.1 Why the Environment Matters

One of the least glamorous but most important things about learning to code is getting your environment right before writing a single line. A mismatched Python version, a missing dependency, or an editor without the right extensions can turn a simple problem into an hours-long debugging session that has nothing to do with code.

This chapter covers the setup done at the start of this project — and the reasoning behind each choice.

> 🔗 **Journal reference:** [Session 1](journal.md#session-1--june-1-2026) covers the decisions made during initial project setup.

### 0.2 What You Need

Three things form the foundation of this setup:

- **Python** — the language runtime. The thing that actually reads and executes your code.
- **VS Code** — the editor. Where you write code, run it, and debug it.
- **Git + GitHub** — version control. How you save your work history and share it publicly.

Everything else — libraries, tools, extensions — gets added when a specific project needs it.

### 0.3 Python Installation and Version Management

**Install from python.org, not the Microsoft Store.**

On Windows, Python can be installed in several ways. The Microsoft Store version installs a wrapper called an App Execution Alias rather than a real executable. This causes silent problems: pip behaves unreliably, virtual environments can break, and VS Code struggles to detect the interpreter correctly. The alias shows `Version 0.0.0.0` when inspected with `Get-Command python` in PowerShell — that's not a broken version number, it's just metadata about the wrapper itself.

The correct approach is to download the installer directly from **python.org/downloads** and run it. On the first screen, tick **"Add python.exe to PATH"** before clicking anything else. This is the most commonly missed step and causes the most downstream confusion.

**Verifying your installation:**

Once installed, open a terminal and run:

```powershell
python --version
```

Then confirm which Python is actually being called:

```powershell
python -c "import sys; print(sys.executable)"
```

The path returned should point somewhere like `C:\Users\yourname\AppData\Local\Programs\Python\Python3xx\python.exe` — not `Microsoft\WindowsApps`. If you see the latter, the Store alias is still intercepting the command.

Also confirm pip — Python's package manager — is present and wired to the same installation:

```powershell
pip --version
```

The path in pip's output should match the path from the `sys.executable` check above.

**A note on PowerShell vs the Windows Command Prompt:**

PowerShell is not the same as the old Command Prompt, and it's not the same as a Unix terminal. It has its own language and its own aliases that can shadow commands you expect to exist. A key example: `where` in PowerShell is an alias for `Where-Object` — a PowerShell filtering command — not the Windows `where.exe` that locates executables. Running `where python` in PowerShell returns nothing and no error, because it ran *something*, just not what was intended. The correct PowerShell equivalent is `Get-Command python`.

When something returns no output and no error in PowerShell, that's often why.

### 0.4 VS Code and Recommended Extensions

VS Code is the editor used throughout this project. It's free, well-maintained, and has strong Python support.

**Core extensions installed at setup:**

| Extension | Publisher | Purpose |
|-----------|-----------|---------|
| Python | Microsoft | Core Python support — IntelliSense, run buttons, debugging. Installs Pylance and the Python Debugger alongside it. |
| Indent Rainbow | oderwat | Colours each indentation level differently. Critical for Python, where indentation is syntax — a wrong indent changes what code does or breaks it entirely. |
| Error Lens | Alexander | Shows errors and warnings inline next to the code, rather than as underlines you have to hover over. |
| GitLens | GitKraken | Layers Git history directly into the editor — shows what changed, when, and in which commit, without leaving the file. |

**Selecting the Python interpreter:**

After installing the Python extension, VS Code needs to be told which Python installation to use. Open the Command Palette (`Ctrl+Shift+P`), type `Python: Select Interpreter`, and choose the path confirmed during the installation verification step. This ensures VS Code and the terminal are using the same Python.

### 0.5 The Terminal — Your Other Editor

The terminal is where you run code, install packages, and interact with Git. VS Code has an integrated terminal accessible via `Ctrl+`` (the backtick key, above Tab). Using the integrated terminal is a good habit — it keeps everything in one place and ensures the terminal uses the same environment VS Code is pointed at.

**A few terminal fundamentals worth knowing early:**

- Commands do exactly what you type — including the parts you didn't mean. Read the full command before pressing Enter.
- `cd` navigates between folders. `cd ~\Documents` goes to your Documents folder. `cd ..` goes up one level.
- `mkdir Projects` creates a folder called Projects in the current location.
- When Git output is long, it opens in a pager called `less`. The terminal appears stuck with `(END)` at the bottom. Press `q` to exit.

### 0.6 GitHub — Tracking Your Work From Day One

Git is a version control system — it tracks changes to your files over time, letting you see what changed, when, and why. GitHub is a hosting platform for Git repositories, making them accessible online and shareable.

**Setting up Git identity:**

Before making any commits, Git needs to know who you are. This identity appears on every commit in your history:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@youremail.com"
```

Also update the default branch name to match GitHub's modern default:

```powershell
git config --global init.defaultbranch main
```

**The four-stage mental model:**

Every change to a file goes through four states before it's on GitHub:

1. **Untracked / Modified** — the change exists on your machine; Git isn't doing anything with it yet
2. **Staged** — you've told Git to include this change in the next commit (`git add .`)
3. **Committed** — the change is saved as a permanent local snapshot (`git commit -m "message"`)
4. **Pushed** — the snapshot is sent to GitHub (`git push`)

`git status` at any point shows you where your files currently sit in this pipeline.

**Starting a project the clean way:**

Create the repository on GitHub first (with no README, no .gitignore, no licence — these create a commit that complicates the first push). Then clone it locally:

```powershell
git clone https://github.com/yourusername/your-repo-name
```

Cloning creates the folder, names it to match the repo, and sets up the GitHub connection automatically. This is cleaner than creating a local folder first and connecting the remote manually.

> 🔗 **Journal reference:** [Session 2](journal.md#session-2--june-1-2026) covers the full account of the environment setup, including the mistakes made and what they revealed.

---

---

*This guidebook grows with the project. For exact syntax and function definitions, see the [Encyclopedia](encyclopedia.md). For the session-by-session account of how understanding developed, see the [Journal](journal.md).*
