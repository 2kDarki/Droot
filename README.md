# Droot

**Droot** (short for **Darkian Root**) is a Python project scaffolding tool designed to help developers quickly bootstrap new Python applications with a clean, consistent, and well-organized project structure — which I call the **Droot-type project structure**.

## Why Droot?

Starting a new Python project often involves repetitive setup tasks: creating folders, adding boilerplate files, initializing version control, configuring licenses, and more. Droot automates these routine steps, so you can focus on writing code faster and with best practices baked in.

---

## Features

- Creates a standardized folder layout:
  ```
  project_name/
  ├── LICENSE
  ├── README.md
  ├── pyproject.toml
  ├── requirements.txt
  ├── run.py
  ├── src/
      ├── project_name/
          ├── __init__.py
          └── main.py
      ├── autotests.py
      └── utils.py
      └── tests/
  ```
- Supports multiple popular open-source licenses (MIT, Apache 2.0, GPL, BSD, Unlicense)
- Automatically populates license files with current year and author name
- Adds starter boilerplate files for application entry point, utility functions, and test skeletons
- Adds metadata comments ("watermarks") in `__init__.py`
- Interactive CLI to provide project details and select license(s)
- Modular design for future extensibility and custom workflows

---

## Installation

Clone the repository (or use pip once published):

```bash
git clone https://github.com/2kDarki/Droot.git
cd Droot
```

> You can also install it globally or use directly from the source.

---

## Usage

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
| `--dual-license` | Optional second license           |
| `--no-license`   | Skip license generation           |
| `--minimal`      | Skip test setup and extras        |
| `--force`        | Overwrite if folder exists        |

---

## Configuration

Currently, Droot uses a fixed folder structure (the **Droot-type structure**) tailored for Python projects. In future versions, we may add support for other project types.

## Testing

Test scripts should be placed inside the `src/tests/` folder.

Run all tests with:

```bash
python src/autotests.py
```

---

## License

Droot itself is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome!  
If you'd like to write tests, improve logic, or add features:

- Fork the repo  
- Create a feature branch  
- Submit a pull request  

---

# Disclaimer

Droot is a powerful tool that manipulates the filesystem — it creates folders, generates files, and, in some cases (when `--force` is used), removes existing directories. While it includes safety checks and input validation to prevent accidental data loss, **misuse or edge-case errors may still lead to destructive behavior**.

## Important notes

- Always double-check your inputs (especially project name and target path).  
- Avoid running Droot in critical or sensitive directories.  
- If testing or experimenting with Droot, use a safe, empty workspace.  
- When using the CLI arguments, be cautious with `--force`, as it can delete existing content in the target folder.
- NB: Its only when `--force` is true that it overwrites.

**By using Droot, you accept full responsibility for how it interacts with your system.** It is provided *as-is*, with no guarantees of safety in all environments.

That said — with careful use, Droot is a reliable and productivity-boosting tool.
