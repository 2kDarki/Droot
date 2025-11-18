<<<<<<< HEAD
# Droot

**Droot** (short for **Darkian Root**) is a Python project scaffolding tool designed to help developers quickly bootstrap new Python applications with a clean, consistent, and well-organized project structure — which I call the **Droot-type project structure**.

## Why Droot?

Starting a new Python project often involves repetitive setup tasks: creating folders, adding boilerplate files, initializing version control, configuring licenses, and more. Droot automates these routine steps, so you can focus on writing code faster and with best practices baked in.
=======
# Droots

**Droots** (short for **Darkian Root Scaffolding**) is a Python project scaffolding tool designed to help developers quickly bootstrap new Python applications with a clean, consistent, and well-organized project structure.

---

## Why Droots?

Starting a new Python project often involves repetitive setup tasks: creating folders, adding boilerplate files, initializing version control, configuring licenses, and more. Droots automates these routine steps, so you can focus on writing code faster and with best practices baked in.
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

---

## Features

- Creates a standardized folder layout:
  ```
<<<<<<< HEAD
  project_name/
=======
  Project_name/
  ├── .gitignore
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)
  ├── LICENSE
  ├── README.md
  ├── pyproject.toml
  ├── requirements.txt
  ├── run.py
  ├── src/
      ├── project_name/
<<<<<<< HEAD
          ├── __init__.py
          └── main.py
      ├── autotests.py
      └── utils.py
      └── tests/
  ```
- Supports multiple popular open-source licenses (MIT, Apache 2.0, GPL, BSD, Unlicense)
=======
      |   ├── __init__.py
      |   └── main.py
      ├── autotest.py
      ├── utils.py
      └── tests/
  ```
- Supports multiple popular open-source licenses (MIT, Apache 2.0, GPL 3.0, BSD, MPL 2.0, Unlicense)
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)
- Automatically populates license files with current year and author name
- Adds starter boilerplate files for application entry point, utility functions, and test skeletons
- Adds metadata comments ("watermarks") in `__init__.py`
- Interactive CLI to provide project details and select license(s)
- Modular design for future extensibility and custom workflows

---

## Installation

<<<<<<< HEAD
Clone the repository (or use pip once published):
=======
Clone the repository:
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

```bash
git clone https://github.com/2kDarki/Droot.git
cd Droot
```
<<<<<<< HEAD
=======
or use pip:
```bash
pip install droots
```
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

> You can also install it globally or use directly from the source.

---

## Usage

<<<<<<< HEAD
Run Droot to start scaffolding your new project:

You can launch Droot interactively:

```bash
python droot.py
```

Or provide arguments directly:

```bash
python droot.py --name Droot --author Darki --license MIT --path ./
```
  
Available Flags:

| Flag             | Description                       |
|------------------|-----------------------------------|
| `--name`         | Project name                      |
| `--author`       | Author name                       |
| `--path`         | Target folder for project         | | `--license`      | License type (`MIT`, `GPL`, etc.) |
=======
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
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)
| `--dual-license` | Optional second license           |
| `--no-license`   | Skip license generation           |
| `--minimal`      | Skip test setup and extras        |
| `--force`        | Overwrite if folder exists        |

---

## Configuration

<<<<<<< HEAD
Currently, Droot uses a fixed folder structure (the **Droot-type structure**) tailored for Python projects. In future versions, we may add support for other project types.
=======
Currently, Droots uses a fixed folder structure tailored for Python projects. In future versions, we may add support for other project types.

---
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

## Testing

Test scripts should be placed inside the `src/tests/` folder.

Run all tests with:

```bash
<<<<<<< HEAD
python src/autotests.py
=======
python src/autotest.py
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)
```

---

## License

<<<<<<< HEAD
Droot itself is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
=======
Droots itself is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

---

## Contributing

Contributions are welcome!  
If you'd like to write tests, improve logic, or add features:

- Fork the repo  
- Create a feature branch  
- Submit a pull request  

---

# Disclaimer

<<<<<<< HEAD
Droot is a powerful tool that manipulates the filesystem — it creates folders, generates files, and, in some cases (when `--force` is used), removes existing directories. While it includes safety checks and input validation to prevent accidental data loss, **misuse or edge-case errors may still lead to destructive behavior**.
=======
Droots is a powerful tool that manipulates the filesystem — it creates folders, generates files, and, in some cases (when `--force` is used), removes existing directories. While it includes safety checks and input validation to prevent accidental data loss, **misuse or edge-case errors may still lead to destructive behavior**.

---
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)

## Important notes

- Always double-check your inputs (especially project name and target path).  
<<<<<<< HEAD
- Avoid running Droot in critical or sensitive directories.  
- If testing or experimenting with Droot, use a safe, empty workspace.  
- When using the CLI arguments, be cautious with `--force`, as it can delete existing content in the target folder.
- NB: Its only when `--force` is true that it overwrites.

**By using Droot, you accept full responsibility for how it interacts with your system.** It is provided *as-is*, with no guarantees of safety in all environments.

That said — with careful use, Droot is a reliable and productivity-boosting tool.
=======
- Avoid running Droots in critical or sensitive directories.  
- If testing or experimenting with Droots, use a safe, empty workspace.  
- When using the CLI arguments, be cautious with `--force`, as it can delete existing content in the target folder.
- NB: Its only when `--force` is true that it overwrites.

**By using Droots, you accept full responsibility for how it interacts with your system.** It is provided **as-is**, with no guarantees of safety in all environments.

> That said — with careful use, Droots is a reliable and productivity-boosting tool.
>>>>>>> 05f2ae0 (Fixed folder structure, missing entry point in PyPI, and inconsistent naming)
