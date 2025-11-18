from .sanitize import catch_invalid
import argparse

def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="droot",
             description="Generate a new Python project "
             +"using the Droot-type structure.")

    parser.add_argument("-n", "--name", type=str, 
           required=True, help="Name of the project.")

    parser.add_argument("-a", "--author", type=str,
           required=True, help="Author of the project.")

    parser.add_argument("-l", "--license", type=str,
           default="MIT", choices=["MIT", "Apache-2.0", 
           "GPL-3.0","BSD-3-Clause","MPL-2.0", "Unlicense"],
           help="Primary license to apply (default: MIT).")

    parser.add_argument("--dual-license", type=str,
           choices=["MIT", "Apache-2.0", "GPL-3.0", 
           "BSD-3-Clause", "MPL-2.0", "Unlicense"],
           help="Optional second license to include.")

    parser.add_argument("-p", "--path", type=str,
           default=".", help="Directory path where the "
           +"project will be created (default: current "
           +"directory).")

    parser.add_argument("--force", action="store_true", help
           ="Force overwrite existing files if they exist.")

    parser.add_argument("--no-license", action="store_true",
           help="Skip creating a LICENSE file.")

    parser.add_argument("--minimal", action="store_true",
           help="Create a minimal project (no utils or "
           "autotests).")

    return catch_invalid(parser.parse_args())
