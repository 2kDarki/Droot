from datetime import datetime

readme = """# Markdown Syntax

1. Headers
 - # Main header
 - ## Subheader
 - ### Sub-subheader

2. Text
 - Just write as you normally write
 - **bold text**
 - _italic text_ of *italic text*
 - > this is a commented sentence

3. Lists
 - '-' for unordered list item, e.g., (- item/sentence)
 - '1.' for ordered list item, e.g., (1. item/sentence)

4. Code
 - `Inline code`
 - ```Multiline code```

5. Sugars
 - '---' or '***' for seperating sections

> Pro tip: Write in Notion and then copy-paste what you wrote. Copying from Notion automatically converts the copied text to Markdown."""

gitignore = """Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

C extensions
*.so

Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

PyInstaller
*.manifest
*.spec

Installer logs
pip-log.txt
pip-delete-this-directory.txt

Unit test / coverage
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
test-results/

Translations
*.mo
*.pot

Django stuff
*.log
local_settings.py
db.sqlite3
media/

Flask stuff
instance/
.webassets-cache

Scrapy stuff
.scrapy

Sphinx documentation
docs/_build/

PyBuilder
target/

IPython
profile_default/
ipython_config.py

mypy
.mypy_cache/
.dmypy.json
dmypy.json

Pyre
.pyre/

pytype
.pytype/

Cython debug symbols
cython_debug/

VS Code
.vscode/

JetBrains
.idea/

MacOS
.DS_Store

Virtual environments
env/
venv/
ENV/
env.bak/
venv.bak/

System files
Thumbs.db
Desktop.ini"""

def gen_toml(project_name: str, author: str) -> str:
    name  = project_name.lower()
    toml  = "[project]\n"
    toml += f"""name = "{project_name}"\n"""
    toml += """version = "0.1.0"
description = "description goes in here"
authors = [{ name = """+f""""{author}", email = """+""""your.email@gmail.com" }]
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.scripts]\n"""
    toml += f"""{name} = "{name}.main:main"\n"""
    toml += """
[tool.setuptools]
package-dir = { "" = "src" }

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta\""""
    return toml

def gen_runpy(name):
    return f"""from src.{name.lower()}.main import main
import argparse
import sys

def parse_args() -> argparse.ArgumentParser:
    parser         = argparse.ArgumentParser()
    subparsers     = parser.add_subparsers(dest="command")
    
    example_parser = subparsers.add_parser("example",
                     help="Show example command")
    
    example_parser.add_argument('-o', '--option', 
        action="store_true", help="Show example option")
    
    return parser.parse_args()

if __name__ == "__main__": 
    args = parse_args()
    if not args.command: sys.exit(main())
    
    if args.command == "example":
        if args.option: ...       # do something
        else: ...                 # do something
    else: ...                     # do something"""

def get_license(lic: str, owner: str) -> str: 
    year         = datetime.now().year
    licenses_map = {
"MIT": f"""MIT License

Copyright (c) {year} {owner}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:                      

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.                           

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""",

"Apache-2.0": f"""Apache License 2.0

Copyright (c) {year} {owner}

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0    

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and limitations under the License.""",

"BSD-3-Clause": f"""BSD 3-Clause License

Copyright (c) {year}, {owner}
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the {owner} nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DAMAGES ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE.""",

"GPL-3.0": f"""GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

Copyright (C) {year} {owner}

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 

See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see 

    https://www.gnu.org/licenses/.""",

"MPL-2.0": f"""MOZILLA PUBLIC LICENSE
Version 2.0

Copyright (C) {year} {owner}

This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.

The MPL-2.0 license permits the use, modification, and distribution of this software, provided that the source code is made available under the same license. Any modifications to the original code must also be licensed under the MPL-2.0, although it allows for the combination of the software with other files that may be under different licenses.

The software is provided on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND.

By using, modifying, or distributing this software, you acknowledge that you have read and understood the terms and conditions of the MPL-2.0 license.

You should have received a copy of the Mozilla Public License along with this software. If not, see 
    https://mozilla.org/MPL/2.0/.""",

"Unlicense": f"""This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author has dedicated any and all copyright interest in the software to the public domain as of {year}.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND."""}

    if lic == "all": return licenses_map
    return licenses_map.get(lic)
