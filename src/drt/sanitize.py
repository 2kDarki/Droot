from .config import invalid_chars, reserved
from .templates import utils, nonpies
from argparse import ArgumentParser
from . import helper
import os

def resolve_path(path: str, catch: bool = False) -> helper.Path:
    """Resolves a relative/absolute path to an absolute Path."""
    max_tries, attempts = 3, 0
    cwd = helper.Path.cwd()
    
    while attempts < max_tries:
        err = "Directory doesn't exist! Try again."   
        if not path or path == ".": return cwd.resolve()
        resolved = (cwd / path).resolve()
        if resolved.exists():
            try:
                (resolved / ".drt").mkdir()
                (resolved / ".drt").rmdir()
                return True if catch else resolved
            except OSError as e:
                if catch: return False
                err =("Permission denied! Try a different "
                    + "directory.")
                if isinstance(e, FileExistsError):
                    err =("Unable to write to this "
                        + "directory. Directory contains a"
                        + " directory named '.drt'. Use "
                        + "a different directory or rename"
                        + " '.drt' directory.")
                elif not isinstance(e, PermissionError):
                    err =(f"Invalid path {path!r}. "
                        + "Try again.")
    
        attempts += 1
        if attempts == max_tries:              
            helper.err(f"Max tries ({attempts}) reached! "
            +    "Defaulting to current working directory:"
            +     f"  '{cwd}'")
            return cwd
        
        if catch: return False
        helper.err(err)   
        path = input(helper.label(f"Path {cwd}{os.sep}"))       
        
def required(data: str, field: int = 0, 
            catch: bool = False) -> str:
    name        = "Project name" if not field else "Author"
    field_name  = name + (" name" if field else "")  
    
    while True:
        err = f"{field_name} is required. "
        if data:
            err = f"Name {data!r} is reserved. "
            if utils.any_in(invalid_chars, eq=data):
                i = 0
                for ch in data:
                    if ch in invalid_chars:
                        i = invalid_chars.index(ch)
                        break
                inv = invalid_chars[i]     
                err = f"Invalid character '{inv}'. "
            elif data.lower() not in reserved: 
                return True if catch else data
        if catch: return False
        helper.err(err + "Try again.")
        data = input(helper.label(f"{name}: ")).strip()

def get_licenses(no_lic: bool, prompt: str | None = None, 
                 author: str | None = None, catch: bool = 
                 False) -> list[str|None, str|None]:
    license_map = nonpies.get_license("all",author or"drt")
    if catch: return no_lic in list(license_map.keys())
    if no_lic: return [None, None]
    
    print()
    licenses = []
    for i in range(2):               
        tag = "Choose license"
        helper.list_items(license_map, guide=tag)
        licenses.append(helper.choose(license_map.keys()))
        print()
        if i == 0:
            dual = input(prompt).strip().lower() == "y"
            if not dual:
                licenses.append(None)
                break
            del license_map[licenses[0]]
            print()
                
    return licenses

def catch_invalid(args: ArgumentParser) -> ArgumentParser:
    invalid = []
    valid   = [required, get_licenses, resolve_path]
    for pos, (key, arg) in enumerate(vars(args).items()):
        if pos < 5: i = int(pos / 2)
        else: break
        if not valid[i](arg, catch=True):
            invalid.append([key, arg])
    
    notify = [
f"Invalid name. Invalid character(s) found.", 
"Invalid license. Defaulting to MIT.",
f"Invalid path {vars(args)['path']!r}. Defaulting to: "
f"{helper.cwd}"]
    
    keys      = list(vars(args).keys())
    caught    = []
    terminate = False
    new_path  = False
    new_lic   = False
    new_duo   = False
    for key, arg in invalid:
        if arg is None: continue
        if key in ["name", "author"]: terminate = True
        if key == "path":             new_path  = True
        if key == "license":          new_lic   = True
        if key == "dual_license":     new_duo   = True
        i = int(keys.index(key) / 2)
        if i > 2: break
        caught.append(f"{key.title()}: {notify[i]}")
    
    if caught:
        print()
        helper.list_items(caught, "Invalid inputs", True)
        if not terminate: print()
    
    if terminate:
        helper.err("Droots terminated. Invalid name(s).",1)
        utils.sys.exit(1)
    
    if new_path: args.path        = "."
    if new_lic: args.license      = "MIT"
    if new_duo: args.dual_license = None
    
    return args
