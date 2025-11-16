from .src.core.main import main # rewrite to src.project_name.main
import argparse

def parse_args() -> argparse.ArgumentParser:
    parser         = argparse.ArgumentParser()
    subparsers     = parser.add_subparsers(dest="command")
    
    example_parser = subparsers.add_parser("example",
                     help="Show example comman")
    
    example_parser.add_argument('-o', '--option', 
        action="store_true", help="Show example option")
    
    return parser.parse_args()

if __name__ == "__main__": 
    args = parse_args()
    if not args.command: main()
    
    if args.command == "example":
        if args.option: ...       # do something
        else: ...                 # do something
    else: parser.print_help()