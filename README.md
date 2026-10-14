# GenDocx 📄

A lightweight, flexible Python toolkit for automating Microsoft Word (`.docx`) document generation from templates using [`docxtpl`](https://github.com/elapouite/docxtpl) and Jinja2 templating.

---

## ✨ Features

- **Dynamic Variable Detection (`gendocx.py`):** Automatically scans your Word template for Jinja2 tags (`{{ variable }}`) and prompts for input in the terminal—no hardcoding required.
- **Command-Line Interface (`gendocx-with-cli.py`):** Inject values directly via CLI flags and key-value arguments (`key=value`), ideal for scripts, build pipelines, or CI/CD tasks.
- **Guided Form Script (`gendocx-n-io-prompt.py`):** Simple interactive prompt workflow for fixed invoice/contract fields.
- **Turnkey VS Code Setup:** Pre-configured tasks (`tasks.json`), launch configurations (`launch.json`), formatting on save with Black (`settings.json`), and recommended extensions (`extensions.json`).

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or later
- Microsoft Word or any `.docx` compatible editor

### 2. Setup Virtual Environment & Install Dependencies

```powershell
# Clone or navigate to the repository
cd GenDocx

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📝 How Templates Work

In Microsoft Word, design your layout as usual and place Jinja2 tags anywhere you want dynamic content:

```text
Welcome to {{ company_name }}!
Our focus is {{ company_area_of_expertise }}.
```

Save your file as `template.docx` in the project root (or point to any custom path via flags).

---

## 🛠️ Usage

### Option 1: Dynamic Scanning & Interactive Prompting (Recommended)

Automatically detects all tags defined in `template.docx` and prompts you for each one in human-readable title case:

```powershell
python gendocx.py
```

**Example interaction:**
```text
Loading Word template...

Please fill out the following template fields:
Enter Company Area Of Expertise: Cloud Infrastructure
Enter Company Name: Acme Cloud LLC

Success! Document saved as 'filled_document.docx'
```

---

### Option 2: Command-Line Interface (CLI)

Pass values directly through command-line arguments without interactive prompts:

```powershell
# Use default template.docx and output.docx
python gendocx-with-cli.py company_name="Acme Corp" company_area_of_expertise="Data Analytics"

# Specify custom template and output paths
python gendocx-with-cli.py -t "templates/invoice.docx" -o "output/invoice_101.docx" client_name="Contoso" amount="$2,500"
```

#### CLI Options:
| Flag | Description | Default |
| :--- | :--- | :--- |
| `-t`, `--template` | Path to input template `.docx` | `template.docx` |
| `-o`, `--output` | Destination path for generated `.docx` | `output.docx` |
| `key=value` | Space-separated key-value pairs to populate | *(none)* |

---

### Option 3: Fixed-Field Guided Form

For quick recurring invoices with fixed standard fields (`client_name`, `project_name`, `amount`, `due_date`):

```powershell
python gendocx-n-io-prompt.py
```

---

## 💻 VS Code Integration

This project includes pre-configured settings in the `.vscode/` directory:

- **Run Default Build Task (`Ctrl + Shift + B`):**
  Executes `gendocx-with-cli.py` with sample arguments using your active Python interpreter.
- **Debugging (`F5`):**
  Open the Run & Debug panel (`Ctrl + Shift + D`) and select:
  - *Python: Run with Default Files*
  - *Python: Run with Custom Flags*
- **Auto-Formatting:**
  Formatted automatically on save using the Microsoft Black Formatter extension.

---

## 📂 Repository Structure

```text
GenDocx/
├── .vscode/
│   ├── extensions.json       # Recommended workspace extensions
│   ├── launch.json           # Debugger launch configurations
│   ├── settings.json         # Workspace settings & Black formatter configuration
│   └── tasks.json            # One-click build task configuration
├── .gitignore                # Ignores generated *.docx outputs
├── gendocx.py                # Dynamic tag discovery & interactive prompt
├── gendocx-with-cli.py       # Full CLI interface with argparse
├── gendocx-n-io-prompt.py    # Guided interactive prompt for fixed fields
├── requirements.txt          # Python dependencies
├── template.docx             # Base Word template
└── README.md                 # Project documentation
```

---

## ⚠️ Troubleshooting

> **`[Errno 13] Permission denied: 'output.docx'`**  
> If Microsoft Word currently has `output.docx` (or your destination file) open, Windows locks the file. Close the document in Word before running the script.
