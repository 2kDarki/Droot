from src.droot.sanitize import resolve_path, required
from src.droot.templates import utils, nonpies
from src.droot.constructor import Constructor
from src.droot.sanitize import get_licenses
from src.droot.argparser import parse_args
from src.droot import helper
from typing import NoReturn

def menu() -> NoReturn:
    head = utils.center("《 DROOT 》","=","magenta","green")
    print(f"{head}\n")
    
    prompts = helper.label([
        "Project name: ", "Author: ",
        f"Path {helper.cwd}{helper.os.sep}", 
        "Licensed [y/n]: ", "Dual licensed [y/n]: ",
        "Minimal (no automated tests) [y/n]: ", 
        "Overiding existing project [y/n]: "
    ])
    name          = required(input(prompts[0]), 0).strip()
    author        = required(input(prompts[1]), 1).strip()
    path          = resolve_path(input(prompts[2]))
    no_lic        = input(prompts[3]).strip().lower() != "y"
    lic, dual_lic = get_licenses(no_lic, prompts[4], author)
    minimal       = input(prompts[5]).strip().lower() == "y"
    force         = input(prompts[6]).strip().lower() == "y"
    
    Constructor(
        pro_name=name,
        author=author,
        path=path,
        lic=lic,
        dual_lic=dual_lic,
        no_lic=no_lic,
        minimal=minimal,
        force=force)
    
    utils.underline(hue="magenta")
    utils.sys.exit(0)

if __name__ == "__main__":
    try:
        if len(utils.sys.argv) == 1: menu()
    except (EOFError, KeyboardInterrupt) as e:
        if isinstance(e, EOFError): print()
        helper.err("Droot terminated. ", transmit=True)
        utils.underline(hue="red")
        utils.sys.exit(1)
    
    args = parse_args()
    Constructor(
        pro_name=args.name,
        author=args.author,
        path=args.path,
        lic=args.license,
        dual_lic=args.dual_license,
        no_lic=args.no_license,
        minimal=args.minimal,
        force=args.force)
