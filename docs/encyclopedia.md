# Python Encyclopedia

*A living reference document — every syntax element, built-in function, keyword, and concept encountered during this project, defined and illustrated with minimal working examples.*

---

## About This Document

**Style:** Reference encyclopedia — lookup-first, explanation-second  
**Companion documents:** [Guidebook](guidebook.md) · [Journal](journal.md)  
**Repository:** [README](../README.md)

This document is not meant to be read front to back. It is a reference. When a term, function, or piece of syntax appears during a session, it gets an entry here. Entries include:

- What it is
- Syntax pattern
- A minimal working example
- Notes on common mistakes or edge cases where relevant
- A pointer to the [Guidebook](guidebook.md) if the concept is explored in a fuller narrative context

---

## AI Assistance Record

This document is maintained with the assistance of an AI model acting as a documentation guide. Model changes are recorded below.

| Model | Version | Active From | Active To |
|-------|---------|-------------|-----------|
| Claude Sonnet | 4.6 | June 1, 2026 | present |

---

## How Entries Are Organised

Entries are grouped by **category**, then listed alphabetically within each category. Each entry follows this template:

```
### term_or_function_name

**Category:** e.g. Built-in Function / Keyword / Operator / Data Type  
**Introduced:** Session N — [link to journal entry]  
**Guidebook reference:** Chapter X — [link]

Brief definition.

**Syntax:**
[code block]

**Example:**
[code block]

**Notes:** Any gotchas, edge cases, or common mistakes.
```

---

## Categories

- [Data Types](#data-types)
- [Variables & Assignment](#variables--assignment)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Loops](#loops)
- [Collections](#collections)
- [String Methods](#string-methods)
- [Built-in Functions](#built-in-functions)
- [Modules & Imports](#modules--imports)
- [File I/O](#file-io)
- [Error Handling](#error-handling)
- [Object-Oriented Programming](#object-oriented-programming)

---

## Data Types

### bool

**Category:** Data Type
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A boolean value — either `True` or `False`. Used for anything that is a yes/no state, such as whether a character has proficiency in a skill.

**Syntax:**
```python
variable = True
variable = False
```

**Example:**
```python
has_proficiency = True
is_conscious = False
```

**Notes:** `bool` is a subclass of `int` in Python — `True` equals `1` and `False` equals `0`. They are equal in value but different in type (`type(True)` returns `bool`, not `int`). Always use `True`/`False` rather than `1`/`0` when the intent is boolean — it's more readable and more precise.

---

### float

**Category:** Data Type
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A decimal (floating-point) number. Regular division with `/` always returns a float, even when the result is a whole number.

**Syntax:**
```python
variable = 3.14
```

**Example:**
```python
average_damage = 4.5
result = 10 / 2  # returns 5.0, not 5
```

**Notes:** Use `int` for whole numbers unless decimals are genuinely needed. For D&D calculations, most values (stats, modifiers, gold pieces) are integers. Use `//` instead of `/` when you want whole-number division results.

---

### int

**Category:** Data Type
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A whole number, positive or negative, with no decimal point.

**Syntax:**
```python
variable = 42
variable = -3
```

**Example:**
```python
character_level = 1
movement_speed = 30
modifier = -2
```

**Notes:** No quotes — quotes make it a string. `int('5')` converts a string to an integer if needed. Most D&D values are integers: stats, modifiers, hit points, level, speed, gold.

---

### str

**Category:** Data Type
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A string — any sequence of characters enclosed in quotes. Represents text.

**Syntax:**
```python
variable = 'text'
variable = "text"
```

**Example:**
```python
race_name = 'Tiefling'
class_name = 'Rogue'
title = 'D&D Character Generator'
```

**Notes:** Single and double quotes both work — pick one and be consistent throughout a project. This project uses single quotes. A string containing a single quote should use double quotes to wrap it, or escape the quote with `\'`.

---

## Variables & Assignment

### comments

**Category:** Syntax
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A comment is a line (or part of a line) that Python ignores entirely. Used to leave notes in code for human readers.

**Syntax:**
```python
# Full-line comment
code = 'here'  # Inline comment after code
```

**Example:**
```python
# D&D modifier: every 2 points above or below 10 gives +1 or -1
mod_str = (stat_str - 10) // 2
```

**Notes:** Comments should explain *why* something exists, not *what* it does — the code itself should make the what clear. A comment that restates the formula in the next line adds nothing. A comment explaining the D&D rule behind it adds context the code can't convey.

---

### variable assignment

**Category:** Syntax
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A variable is a named container for a value. Assignment uses `=`, which means "store this value under this name" — not equality.

**Syntax:**
```python
name = value
```

**Example:**
```python
race = 'Tiefling'
level = 1
speed = 30
has_darkvision = True
```

**Notes:** Variable names use `snake_case` in Python — all lowercase, words separated by underscores. Names should describe what the value represents. The `=` in assignment is not the same as mathematical equality — it's an instruction to store.

---

## Operators

### `%` — modulo

**Category:** Operator
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Returns the remainder after division.

**Syntax:**
```python
result = a % b
```

**Example:**
```python
10 % 3  # 1
8 % 2   # 0 (no remainder — useful for checking even/odd)
```

**Notes:** Useful for checking divisibility (`n % 2 == 0` means n is even). Less common in this project than `//`.

---

### `//` — floor division

**Category:** Operator
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Divides two numbers and rounds the result *down* to the nearest whole number (toward negative infinity). Always returns an `int` when both operands are integers.

**Syntax:**
```python
result = a // b
```

**Example:**
```python
14 // 2   # 7
10 // 3   # 3 (rounds down from 3.33)
-1 // 2   # -1 (rounds toward negative infinity, not toward zero)
```

**Notes:** Used for D&D modifier calculation: `modifier = (score - 10) // 2`. Replaces `math.floor(x / 2)` — no import needed. The behaviour with negative numbers is important: `-1 // 2` returns `-1`, not `0`, because floor division always rounds *down*, not toward zero.

---

### arithmetic operators

**Category:** Operator
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Standard arithmetic. Python supports addition, subtraction, multiplication, division, floor division, and modulo.

**Syntax:**
```python
a + b   # addition
a - b   # subtraction
a * b   # multiplication
a / b   # division (always returns float)
a // b  # floor division (returns int)
a % b   # modulo / remainder
```

**Example:**
```python
hit_points = 8 + 2        # 10
damage = 6 - 1            # 5
double = speed * 2        # 60
half = 10 / 4             # 2.5 (float)
modifier = (14 - 10) // 2 # 2 (int)
```

**Notes:** `/` always returns a float. `//` always returns an int (when operands are ints). Parentheses control order of operations as in standard maths.

---

## Control Flow

*No entries yet.*

---

## Functions

*No entries yet.*

---

## Loops

*No entries yet.*

---

## Collections

### list

**Category:** Collection
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

An ordered, mutable collection of values stored in a single variable. Items are enclosed in square brackets and separated by commas.

**Syntax:**
```python
my_list = [value1, value2, value3]
```

**Example:**
```python
races = ['Bugbear', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Gnome']
spell_pool = ['Fireball', 'Magic Missile', 'Shield']
stats = [15, 14, 13, 12, 10, 8]
```

**Accessing items by index** (zero-based):
```python
races[0]   # 'Bugbear' — first item
races[2]   # 'Tiefling' — third item
races[-1]  # 'Gnome' — last item, always
races[-2]  # 'Dragonborn' — second to last, always
```

**Notes:** Indexes start at `0`, not `1`. Negative indexes count from the end — `[-1]` is always the last item regardless of list length. Hardcoding the last index (`races[4]`) breaks if the list changes size; `races[-1]` does not.

---

## String Methods

### f-strings

**Category:** String Formatting
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

A formatted string literal — a string prefixed with `f` where variables or expressions inside `{}` are evaluated and inserted into the string at runtime.

**Syntax:**
```python
f'text {variable} more text'
f'text {expression}'
```

**Example:**
```python
race = 'Tiefling'
level = 3
print(f'You are a level {level} {race}.')
# Output: You are a level 3 Tiefling.

stats = [15, 14, 13]
print(f'Highest stat: {stats[0]}')

races = ['Hill Dwarf', 'Elf', 'Human']
print(f'There are {len(races)} races available.')
```

**Notes:** The `f` prefix must come immediately before the opening quote — `f'...'` or `f"..."`. Any valid Python expression can go inside `{}`, including function calls like `len()`. Prefer f-strings over string concatenation with `+` — they are more readable and avoid the need to call `str()` on non-string values.

---

## Built-in Functions

### `len()`

**Category:** Built-in Function
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Returns the number of items in a collection (list, string, dictionary, etc.).

**Syntax:**
```python
len(collection)
```

**Example:**
```python
races = ['Bugbear', 'Half-Orc', 'Tiefling']
len(races)        # 3
len('Tiefling')   # 8 (counts characters in a string)
```

**Notes:** Works on any sequence type. Commonly used inside f-strings: `f'Choose from {len(races)} races'`.

---

### `print()`

**Category:** Built-in Function
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Outputs text (or any value) to the terminal. The primary tool for seeing what your code is doing.

**Syntax:**
```python
print(value)
print(f'label: {variable}')
```

**Example:**
```python
print('D&D Character Generator')
print(42)
print(True)

race = 'Tiefling'
print(f'Your race is: {race}')
```

**Notes:** `print()` can accept any data type — it converts values to strings automatically. Passing a variable name *without* quotes prints its value; passing it *with* quotes prints the word itself. Use f-strings for labelled output rather than concatenating with `+`.

---

## Modules & Imports

### `import`

**Category:** Keyword
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Loads a module (a file of pre-written Python code) so its functions and tools can be used. Import statements belong at the top of a file.

**Syntax:**
```python
import module_name
```

**Example:**
```python
import random
import math
```

**Notes:** After `import random`, all functions in the module are accessed as `random.function_name()`. Avoid `from module import *` (as used in HeroGen's `from math import *`) — it imports everything into the current namespace invisibly, making it unclear where functions come from.

---

### `random.choice()`

**Category:** Module Function
**Introduced:** [Session 4](journal.md#session-4--june-4-2026)
**Guidebook reference:** [Chapter 1](guidebook.md#chapter-1-the-shape-of-a-python-program)

Selects and returns one item at random from a non-empty list (or other sequence). Requires `import random`.

**Syntax:**
```python
import random
random.choice(sequence)
```

**Example:**
```python
import random

races = ['Bugbear', 'Half-Orc', 'Tiefling', 'Dragonborn', 'Gnome']
chosen_race = random.choice(races)
print(f'You got the {chosen_race} race!')
```

**Notes:** Store the result in a variable if it will be referenced more than once — calling `random.choice()` a second time produces a *different* random result, which would make the character inconsistent. Every call is independent.

---

## File I/O

*No entries yet.*

---

## Error Handling

*No entries yet.*

---

## Object-Oriented Programming

*No entries yet.*

---

---

*This document grows with the project. For the story behind each concept, see the [Guidebook](guidebook.md). For when and how each was learned, see the [Journal](journal.md).*
