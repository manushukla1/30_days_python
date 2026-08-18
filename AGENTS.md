# AGENTS.md - 30DaysPython Learning Project

## Project Overview
This is a 30-day progressive Python learning project focused on building foundational programming skills. Files are organized by learning day/topic and use a consistent real-world metaphor (building a house with laborers) to contextualize concepts.

## Core Architecture & Learning Principles

### Day-Based Organization Pattern
- Files named as `{concept}_day_{N}.py` or `{topic}_day_{N}.py`
- Progression: Day 1 (Variables/Types) → Day 2 (Operators) → Day 3 (Conditionals) → Day 4+ (Data Structures)
- Each file is **independently runnable** with `python filename.py`
- **No module imports between files** - each is self-contained for learning isolation

### Contextual Learning Metaphor
All exercises use consistent scenario: Building a 4-room house (4 BHK) with multiple laborers
- **Concrete examples:** Labour names (Mahesh, Ramesh, Mithlesh), wages, working days, absent days
- **Ranges:** 100 sq ft × 100 sq ft land, 50 total working days
- **Why:** Helps students connect abstract concepts to real-world problems (wage calculations, resource allocation)

## Developer & Student Workflows

### Running Code
```bash
# Execute individual script directly
python calculator.py
python if_else_day_3.py
python list_comprehension.py
```

### Logging Convention
- **All files import:** `from loguru import logger` (top of file)
- **Primary output method:** `logger.info(message)` for displaying results
- **Current state:** Mix of `print()` and `logger.info()` - transition to logger for consistency
- **Note:** logger is set to INFO level by default; statements are executed, not configured

### Learning Experimentation Pattern
Each file typically contains:
1. **Active code** - Currently learning concept
2. **Commented code blocks** - Alternative approaches showing:
   - Traditional loops vs. list comprehensions (see `list_comprehension.py`)
   - Nested conditionals vs. elif chains (see `if_else_day_3.py`)
   - Direct iteration vs. index-based loops (see `loops.py`)

**When modifying:** Preserve commented alternatives - they're intentional pedagogical scaffolding.

## Code Patterns & Conventions

### Input/Output Pattern
```python
# Interactive input for user practice
variable = input("Prompt text: ")
# Calculation or processing
result = perform_operation(variable)
# Logging output for visibility
logger.info(f"Result: {result}")
```

### Data Structure Examples
- **Lists:** `labour = ["Sonu", "goru", "donu"]` or `labour_with_cost = [["Sonu", 400], ["goru", 400]]`
- **Dictionaries:** `labour_with_cost = {"Mahesh": 500, "Ramesh": 400}` with parallel dicts for related data
- **Common calculations:** wage totals, working day adjustments, absence penalties

### Control Flow Patterns
- **Even/odd checks:** `if number % 2 == 0` (modulo operator, Day 2 concept)
- **Range loops:** `for i in range(1, 11)` for iteration practice
- **List comprehensions:** `[i for i in range(1,11) if i%2==0]` with conditional variants

## Critical Integration Points

### External Dependencies
- **loguru:** Logging framework imported in every file
  - No configuration needed in these scripts (uses defaults)
  - Used as primary output method for clarity
  - Install: `pip install loguru`

### Inter-File Relationships
- **No direct dependencies** between files
- Each day builds on concepts independently
- Related files by topic (not imports):
  - Variables & operators: `Variable_day_1.py`, `Operator_day_2.py`
  - Control flow: `if_else_day_3.py`, `Loops.py`
  - Data structures: `list_day_4.py`, `dictionary_l1.py`, `list_comprehension.py`

## Adding New Learning Modules

### File Structure Template
```python
from loguru import logger

# Student's name (learning day marker)
# Day X: [Concept Name]

# Active learning code
result = operation()
logger.info(f"Result: {result}")

# Commented alternative approach showing different technique
# Old approach code...
```

### Naming Convention
- Main concept: `{concept}_{day_number}.py`
- Related sub-topics: `{specific_topic}_list.py` or `{action}_at_location_list.py`
- Format: lowercase with underscores, day markers at end

## Testing & Validation

### Manual Verification
- Run each script independently to verify user input handling
- Verify logger outputs display correctly
- Check for division by zero handling (see `calculator.py` line 26)

### Expected Behaviors
- **Calculator:** Handles operators (+,-,*,/), division by zero, session termination
- **List operations:** Handles multidimensional list access, insertions
- **Loops:** Correctly iterate using range and enumerate patterns

## Development Considerations

### Code Style Notes
- Mixed naming: Some variables use camelCase (`lg_of_land`, `bd_of_land`), others snake_case (`number_to_insert`)
- Prioritize **consistency with existing day's patterns** over PEP 8
- Comments explain "why" not "what" (code is learning material)

### Common Pitfalls to Avoid
1. **Don't remove commented code** - shows learning alternatives
2. **Keep scripts independently executable** - don't add inter-file imports
3. **Maintain the labor/house metaphor** for consistency across files
4. **Use logger.info() for visible output** rather than print() in new code

---
**Last Updated:** 2026-06-06 | **Focus:** Python Fundamentals (Days 1-4)

