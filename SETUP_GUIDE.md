# NashTech Bootcamp - Quick Setup Guide

## For New Laptop Setup (After Git Clone)

### Prerequisites
- **VS Code** (already installed)
- **Python 3.x** (download from [python.org](https://www.python.org/downloads/))
- **Git** (for cloning the repo)

---

## Step 1: Clone the Repository
```bash
git clone <repository-url>
cd NashTech_Bootcamp
```

---

## Step 2: Create Virtual Environment
Navigate to the project folder and create a Python virtual environment:

```bash
# Windows
python -m venv .venv

# Mac/Linux
python3 -m venv .venv
```

---

## Step 3: Activate Virtual Environment

**Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
.venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

✅ You should see `(.venv)` prefix in your terminal when activated.

---

## Step 4: Install Dependencies
```bash
pip install pandas
```

---

## Step 5: Configure VS Code
1. Open VS Code in the project folder: `code .`
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Search for **"Python: Select Interpreter"**
4. Choose the interpreter from `.venv` folder (should show `.venv` in the path)

---

## Step 6: Run the Code

### Run Individual ETL Drills:
```bash
python etl_drill_01.py
python etl_drill_02.py
python etl_drill_03.py
python etl_drill_04.py
```

### Run Main File:
```bash
python main.py
```

---

## File Overview
- **etl_drill_01.py** - Pure Python transaction aggregation (no Pandas)
- **etl_drill_02.py** - ETL operations using drill_01
- **etl_drill_03.py** - Pandas-based operations with JSON
- **etl_drill_04.py** - Pandas operations
- **data_source.json** - Input data
- **data.csv** - CSV data file
- **filtered_report.csv** - Output report

---

## Tips for Development

### Update Code:
- Make changes to `.py` files
- Save with `Ctrl+S`
- VS Code will auto-format if configured

### Verify Dependencies:
```bash
pip list
```

### Deactivate Virtual Environment:
```bash
deactivate
```

### Troubleshooting:
- **ModuleNotFoundError**: Make sure `.venv` is activated and dependencies installed
- **Python not found**: Install Python and add to PATH
- **VS Code can't find interpreter**: Reload VS Code after selecting interpreter

---

## Git Workflow
```bash
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Your message"

# Push
git push origin main
```

---

**Happy coding! 🚀**
