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
| 1 | [The Shape of a Python Program](#chapter-1-the-shape-of-a-python-program) | ✅ Complete |
| 2 | Values, Variables, and Types | ⏳ Pending |
| 3 | Making Decisions — Control Flow | ⏳ Pending |
| 4 | Doing Things Repeatedly — Loops | ⏳ Pending |
| 5 | Organising Code — Functions | ⏳ Pending |
| 6 | [Organising Data — Collections](#chapter-6-organising-data--collections) | 🔄 In progress |
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

## Chapter 1: The Shape of a Python Program

*Variables, data types, expressions, lists, and how a Python file runs.*

### 1.1 How Python Runs Your Code

When you run a Python file, Python reads it from top to bottom and executes each line in order. There's no separate compilation step — it just runs. This means two things:

First, order matters. If you try to use a variable before you've defined it, Python will error because it hasn't encountered that variable yet when it reaches the line that needs it.

Second, you can see results immediately. Write a line, run the file, see what happens. This tight feedback loop is one of Python's best qualities as a learning environment.

The integrated terminal in VS Code and the `python` interactive shell (opened by typing `python` with no filename) both let you run individual lines on the spot — useful for testing small ideas without running a whole file.

### 1.2 Variables

A variable is a named container for a value. You create one by writing a name, an equals sign, and a value:

```python
race = 'Tiefling'
level = 1
speed = 30
```

The `=` here is not a mathematical equals sign — it's an instruction: "store this value under this name." The name goes on the left; the value goes on the right.

Variable names in Python use `snake_case` — all lowercase, words separated by underscores. Names should describe what the value represents. `race` is better than `r`. `movement_speed` is better than `ms`.

Once a variable is defined, you can use its name anywhere you'd use the value directly:

```python
print(race)         # prints: Tiefling
print(f'Level: {level}')  # prints: Level: 1
```

> 🔗 **Encyclopedia:** [variable assignment](encyclopedia.md#variable-assignment)

### 1.3 Data Types

Every value in Python has a type. The four types used most in this project are:

**`str` — strings.** Any text, wrapped in quotes. `'Tiefling'`, `'D&D Character Generator'`, `'Fireball'`. Single and double quotes both work; this project uses single quotes throughout.

**`int` — integers.** Whole numbers, no quotes. `1`, `30`, `-2`. Most D&D values — level, speed, stats, hit points, gold — are integers.

**`float` — floats.** Decimal numbers. `3.5`, `1.5`. Less common in this project; regular division with `/` always produces a float, even when the result is a whole number (`10 / 2` gives `5.0`, not `5`).

**`bool` — booleans.** `True` or `False`. Capital T and F, no quotes. Used for yes/no states: does this character have proficiency in Perception? Does a race grant darkvision?

Python's `bool` is actually a subclass of `int` — `True` equals `1` and `False` equals `0`. They're equal in value but different in type. Use `True`/`False` rather than `1`/`0` whenever the intent is a yes/no state; the code reads more clearly.

> 🔗 **Encyclopedia:** [str](encyclopedia.md#str) · [int](encyclopedia.md#int) · [float](encyclopedia.md#float) · [bool](encyclopedia.md#bool)

### 1.4 print() and f-strings

`print()` outputs a value to the terminal. It's your primary tool for seeing what your code is actually doing.

```python
print('D&D Character Generator')
print(race)
print(level)
```

Passing a variable name *without* quotes prints its value. Passing it *with* quotes prints the word itself.

For labelled output — showing a value alongside some context — use an **f-string**: a string prefixed with `f` where variables or expressions inside `{}` are evaluated and inserted:

```python
print(f'Race: {race}')           # Race: Tiefling
print(f'Level: {level}')         # Level: 1
print(f'Races available: {len(races)}')  # evaluates len() inline
```

f-strings are cleaner than concatenating with `+` and avoid the need to call `str()` on non-string values. Any valid Python expression can go inside `{}`.

> 🔗 **Encyclopedia:** [print()](encyclopedia.md#print) · [f-strings](encyclopedia.md#f-strings)

### 1.5 Arithmetic and Floor Division

Python supports standard arithmetic — `+`, `-`, `*`, `/`. The one that matters most in this project is `//`: **floor division**, which divides and rounds the result *down* to the nearest whole number.

This is exactly what D&D's modifier formula requires:

```python
modifier = (score - 10) // 2
```

A score of 14: `(14 - 10) // 2 = 2`. A score of 9: `(9 - 10) // 2 = -1`. The floor division handles negative numbers correctly — `-1 // 2` is `-1`, not `0`, because floor division always rounds toward negative infinity.

In the original HeroGen, this calculation used `math.floor()`, which required importing the entire math library. Python's `//` operator does the same job with no import. This is one of many places where knowing the language well removes unnecessary complexity.

> 🔗 **Encyclopedia:** [arithmetic operators](encyclopedia.md#arithmetic-operators) · [// floor division](encyclopedia.md#---floor-division)

### 1.6 Comments

A comment is a note for human readers that Python ignores entirely. Written with `#`:

```python
# D&D modifier: every 2 points above or below 10 gives +1 or -1
modifier = (score - 10) // 2
```

Comments are most valuable when they explain *why* something is written the way it is — the rule, the constraint, or the decision behind the code. A comment that just restates what the next line already shows adds nothing. A comment that explains the D&D rule behind a formula earns its place.

> 🔗 **Encyclopedia:** [comments](encyclopedia.md#comments)

### 1.7 Lists

A list is an ordered collection of values stored in a single variable:

```python
races = ['Bugbear', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Gnome']
```

Square brackets, values separated by commas. The list can hold any type — a list of strings, a list of numbers, or a mix.

Items are accessed by **index** — their position in the list, starting from `0`:

```python
races[0]   # 'Bugbear'
races[2]   # 'Tiefling'
```

Python also supports **negative indexing**: counting from the end. `races[-1]` is always the last item, `races[-2]` the second to last — regardless of how long the list is. Prefer `races[-1]` over `races[4]` for the last item; if the list ever changes length, the negative index still works and the hardcoded one doesn't.

`len()` returns the count of items in any collection:

```python
len(races)  # 5
```

Lists are used throughout the character generator — race pools, spell lists, equipment, languages. They're a foundational structure.

> 🔗 **Encyclopedia:** [list](encyclopedia.md#list) · [len()](encyclopedia.md#len)

### 1.8 Importing Modules and Randomness

Python's standard library contains modules — files of pre-written tools — that can be loaded with `import`. Imports always go at the top of a file:

```python
import random
```

The `random` module provides tools for random selection. The one used most in this project is `random.choice()`, which picks one item at random from a list:

```python
chosen_race = random.choice(races)
```

Every time the program runs, a different race is selected. This one line is the core mechanic of the entire generator — everything else is building the data for it to choose from and presenting the result.

**Important:** store the result in a variable rather than calling `random.choice()` multiple times. Each call is independent and produces a separate random result. If the chosen race is referenced in several places and `random.choice()` is called each time, the program might print one race for the name and a different race for the features. Store once; reference the variable.

> 🔗 **Encyclopedia:** [import](encyclopedia.md#import) · [random.choice()](encyclopedia.md#randomchoice)

### 1.9 Putting It Together — First Lines of the Generator

By the end of Session 4, the working file contained:

```python
import random

title = 'D&D Character Generator'
races = ['Bugbear', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Gnome']
chosen_race = random.choice(races)
stat_str = 14
# D&D modifier: every 2 points above or below 10 gives +1 or -1
mod_str = (stat_str - 10) // 2

print(title)
print(f'Strength: {stat_str} | Modifier: {mod_str}')
print(f'You got the {chosen_race} race out of a possible {len(races)}!')
```

This is not yet a proper character generator — the data is minimal and nothing is structured. But every element is real: a working random selection from a pool, a correct modifier calculation, and formatted output. The chapters ahead will add the data structures and organisation that turn these building blocks into a complete program.

> 🔗 **Journal reference:** [Session 4](journal.md#session-4--june-4-2026) covers the full account of how these concepts were introduced and where mistakes were made.

---

---

---

## Chapter 6: Organising Data — Collections

*Lists, dictionaries, and how structured data makes a generator possible.*

> This chapter covers collections as they've appeared so far. It will expand as loops and more advanced patterns are introduced in later sessions.

### 6.1 The Problem with Scattered Variables

Early in the project, a race was represented as separate variables:

```python
race_name = 'Hill Dwarf'
race_speed = 25
race_con_bonus = 2
```

This works for one race. It falls apart for sixteen. You'd need forty-plus variables, none of them connected, and no way to randomly select one complete "set" of race data as a unit. The solution is a **collection** — a single variable that holds multiple related values together.

Python has several collection types. The two most important for this project are lists and dictionaries.

### 6.2 Lists — Ordered Sequences

A list holds multiple values in order, in a single variable:

```python
races = ['Hill Dwarf', 'Tiefling', 'Vedalken', 'Dragonborn']
```

Items are accessed by their position (**index**), counting from zero:

```python
races[0]   # 'Hill Dwarf'
races[-1]  # 'Dragonborn' — negative index, always the last item
```

`len()` gives the count of items. `random.choice()` picks one at random.

Lists are used throughout the generator for anything that's a pool of options: spell lists, equipment choices, language pools, racial features.

The limitation of a list of strings is that it only stores names — not the associated data. A race isn't just a name. This is where dictionaries come in.

> 🔗 **Encyclopedia:** [list](encyclopedia.md#list)

### 6.3 Dictionaries — Named Data

A dictionary stores data as **key-value pairs**. Instead of accessing data by position, you access it by name:

```python
hill_dwarf = {
    'name': 'Hill Dwarf',
    'speed': 25,
    'bonus_con': 2,
    'bonus_wis': 1
}

hill_dwarf['speed']      # 25
hill_dwarf['bonus_con']  # 2
```

Compare `hill_dwarf['speed']` to HeroGen's `race[7]`. Both retrieve the same value. One tells you what it is; the other tells you nothing without reading the comment at the top of the file that maps positions to meanings.

Dictionaries are defined with curly braces `{}`, keys and values separated by `:`, entries separated by commas. Keys are almost always strings. Values can be any type — integers, strings, booleans, or even lists.

> 🔗 **Encyclopedia:** [dict](encyclopedia.md#dict)

### 6.4 Lists of Dictionaries

A list can contain dictionaries as its items. This is the core data structure for the character generator — a pool of complete race records that `random.choice()` can select from:

```python
races = [
    {'name': 'Hill Dwarf', 'speed': 25, 'bonus_con': 2, 'bonus_wis': 1},
    {'name': 'Tiefling', 'speed': 30, 'bonus_int': 1, 'bonus_cha': 2},
    {'name': 'Vedalken', 'speed': 30, 'bonus_int': 2, 'bonus_wis': 1}
]

chosen_race = random.choice(races)
print(chosen_race['name'])   # one of the three race names, at random
print(chosen_race['speed'])  # the speed for whichever race was chosen
```

`random.choice()` returns one complete dictionary. From that point, all keys are available on the result.

**The consistent keys rule.** Every dictionary in the collection must have the same keys. If `'bonus_con'` exists in Hill Dwarf but not in Tiefling, accessing `chosen_race['bonus_con']` raises a `KeyError` whenever Tiefling is selected. The fix is to include all keys in every dictionary, using `0` or `False` as defaults where there's no relevant value:

```python
{'name': 'Tiefling', 'speed': 30, 'bonus_str': 0, 'bonus_dex': 0,
 'bonus_con': 0, 'bonus_int': 1, 'bonus_wis': 0, 'bonus_cha': 2}
```

This gives the data structure a contract: any code that accesses `chosen_race['bonus_con']` can do so safely, regardless of which race was selected.

### 6.5 Dict Values as Lists — Nested Access

Dictionary values can themselves be lists. Languages and racial features are stored this way:

```python
race = {
    'name': 'Hill Dwarf',
    'languages': ['Common', 'Dwarvish'],
    'speed': 25
}
```

Accessing a value inside a nested list chains two sets of square brackets:

```python
race['languages']     # ['Common', 'Dwarvish'] — the whole list
race['languages'][0]  # 'Common' — first item in the list
race['languages'][1]  # 'Dwarvish' — second item
```

The first `[]` retrieves the list from the dictionary. The second `[]` indexes into it.

The limitation of this approach is that hardcoding `[0]` and `[1]` assumes a fixed number of languages. Races with only one language, or three, break this. The solution — iterating over the list with a `for` loop — is covered in the next chapter.

> 🔗 **Journal reference:** [Session 5](journal.md#session-5--june-5-2026) covers the full account of how these structures were built, including the consistent-keys mistake and how it was corrected.

---

*This guidebook grows with the project. For exact syntax and function definitions, see the [Encyclopedia](encyclopedia.md). For the session-by-session account of how understanding developed, see the [Journal](journal.md).*
