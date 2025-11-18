# Droots

**Droots** (short for **Darkian Root Scaffolding**) is a Python project scaffolding tool designed to help developers quickly bootstrap new Python applications with a clean, consistent, and well-organized project structure.

---

## Why Droots?

Starting a new Python project often involves repetitive setup tasks: creating folders, adding boilerplate files, initializing version control, configuring licenses, and more. Droots automates these routine steps, so you can focus on writing code faster and with best practices baked in.

---

## Features

- Creates a standardized folder layout:
  ```
  Project_name/
  ├── .gitignore
  ├── LICENSE
  ├── README.md
  ├── pyproject.toml
  ├── requirements.txt
  ├── run.py
  ├── src/
      ├── project_name/
      |   ├── __init__.py
      |   └── main.py
      ├── autotest.py
      ├── utils.py
      └── tests/
  ```
- Supports multiple popular open-source licenses (MIT, Apache 2.0, GPL 3.0, BSD, MPL 2.0, Unlicense)
- Automatically populates license files with current year and author name
- Adds starter boilerplate files for application entry point, utility functions, and test skeletons
- Adds metadata comments ("watermarks") in `__init__.py`
- Interactive CLI to provide project details and select license(s)
- Modular design for future extensibility and custom workflows

---

## Installation

Clone the repository:

```bash
git clone https://github.com/2kDarki/Droot.git
cd Droot
```
or use pip:
```bash
pip install droots
```

> You can also install it globally or use directly from the source.

---

## Usage

### Run Droots to start scaffolding your new project

1. You can launch Droots interactively:

```bash
python run.py
```
or if installed through pip
```bash
python -m droots # or just: droots
```

2. Or provide arguments directly:

```bash
python run.py --name Habitrax --author Darki --license MIT --path .
```
or if installed through pip
```bash
python -m droots --name Droots --author Darki --license MIT --path .
```
  
### Available Flags

| Flag             | Description                       |
|------------------|-----------------------------------|
| `-n`, `--name`   | Project name                      |
| `-a`, `--author` | Author name                       |
| `-p`, `--path`   | Target folder for project         | | `-l`, `--license`| License type (`MIT`, `GPL`, etc.) |
| `--dual-license` | Optional second license           |
| `--no-license`   | Skip license generation           |
| `--minimal`      | Skip test setup and extras        |
| `--force`        | Overwrite if folder exists        |

---

## Configuration

Currently, Droots uses a fixed folder structure tailored for Python projects. In future versions, we may add support for other project types.

---

## Testing

Test scripts should be placed inside the `src/tests/` folder.

Run all tests with:

```bash
python src/autotest.py
```

---

## License

Droots itself is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome!  
If you'd like to write tests, improve logic, or add features:

- Fork the repo  
- Create a feature branch  
- Submit a pull request  

---

# Disclaimer

Droots is a powerful tool that manipulates the filesystem — it creates folders, generates files, and, in some cases (when `--force` is used), removes existing directories. While it includes safety checks and input validation to prevent accidental data loss, **misuse or edge-case errors may still lead to destructive behavior**.

---

## Important notes

- Always double-check your inputs (especially project name and target path).  
- Avoid running Droots in critical or sensitive directories.  
- If testing or experimenting with Droots, use a safe, empty workspace.  
- When using the CLI arguments, be cautious with `--force`, as it can delete existing content in the target folder.
- NB: Its only when `--force` is true that it overwrites.

**By using Droots, you accept full responsibility for how it interacts with your system.** It is provided **as-is**, with no guarantees of safety in all environments.

> That said — with careful use, Droots is a reliable and productivity-boosting tool.