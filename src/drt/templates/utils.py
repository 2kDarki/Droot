from pathlib import Path
from typing import Any
from math import inf
import unicodedata
import shutil
import sys
import re
import os

TESTS_DIR  = Path(__file__).resolve().parent / "tests"
TERM_WIDTH = shutil.get_terminal_size().columns or 80
HALF_TERM  = int(TERM_WIDTH / 2)
UNITTHRESH = {
            "second": 60, 
            "minute": 60, 
              "hour": 24, 
               "day": 7, 
              "week": 4, 
             "month": 12,
              "year": inf
}

def helper(skip: bool | int = len(sys.argv) > 2) -> None:
    help_args = ["-h", "--h", "-help", "--help"]
    if not any_in(help_args, eq=sys.argv):
        if not skip: return
            
    m, g, i = "magenta", "green", HALF_TERM - 23
    helper  = center("《 AUTOMATED TESTS 》", "—", m, g)
    print(f"\n{helper}")
    
    print("\nUsage:")
    print(f"    autotest.py   {' '*(i+4)}Run all tests")
    print(f"    autotest.py module{' '*i}Test module")
    
    print("\nModules:")
    for file in sorted(TESTS_DIR.glob("*.py")):
        name = file.stem
        if name.startswith("_"): continue
        print(f"    {name}")
    
    underline(hue=g, alone=True)
    sys.exit(any_in(help_args, eq=sys.argv))

def format_time(time: int | float) -> str:
    units = list(UNITTHRESH.keys())     
    def get_timeunits(time: int | float
                     ) -> list[list[int|float, str]]:
        timeunits = []
        limits = [UNITTHRESH[u] for u in units]
        for limit, unit in zip(limits, units):
            if time >= limit:
                time = round(time)
                shaved, time = shave(time, limit)
                timeunits.append([shaved, unit])
            else:
                timeunits.append([time, unit])
                break
        
        return timeunits
        
    timeunits = get_timeunits(time)
    for i, timeunit in enumerate(timeunits):
        time, unit   = timeunit
        unit         = pluralize(time, unit)
        timeunits[i] = [time, unit]
        
    return format_time_string(timeunits[::-1])

def format_time_string(*args) -> str:
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]
    
    parts = []
    try: parts = [f"{unit[0]} {unit[1]}" for unit in 
         args if unit[0] != 0]
    except TypeError: 
        if args[0] != 0: parts=[f"{args[0]} {args[1]}"]
    
    if len(parts) > 1: return ', '.join(parts[:-1]
                       ) + f" and {parts[-1]}"
    elif len(parts) == 1: return parts[0]
    else: return "just now"

def shave(num: int | float, limit: int) -> tuple[int]:
    major = int(num / limit)
    shaved = num - major * limit
    return round(shaved), major

def pluralize(n: int | float, word: str) -> str:
    if n == 1: return word
    else: return word + 's'

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def underline(hue: str | None = None, alone: bool = 
              False) -> None:
    if alone: print()
    print(style_text("—" * TERM_WIDTH, hue))
    if alone: print()

def strip_ansi(s: str) -> str:
    return re.sub(r'\x1B[@-_][0-?]*[ -/]*[@-~]', '', s)

def visual_width(s: str) -> int:
    clean = strip_ansi(s)
    width = 0
    for ch in clean:
        width += 2 if unicodedata.east_asian_width(
            ch) in ['F', 'W'] else 1
    return width

def style_text(text: str, fg: str | None = None, 
               underline: bool = False) -> str:
    colors = {
        "black": 30, "red": 31, "green": 32, 
        "yellow": 33, "blue": 34, "magenta": 35,
        "cyan": 36, "white": 37,
        "gray": 90, "lightred": 91, "lightgreen": 92,
        "lightyellow": 93, "purple": 94,
        "lightmagenta": 95, "lightcyan": 96
    }

    styles = []
    if underline: styles.append("4")
    if fg: styles.append(str(colors[fg]))
    if styles:
      return f"\033[{';'.join(styles)}m{text}\033[0m"
    return text

def center(arg, line: str = " ", hue: str | None = None, 
           line_hue: str | None = None) -> str:        
        vis_width = visual_width(str(arg))    
        total_pad = max(TERM_WIDTH - vis_width, 0)
        left_pad  = total_pad // 2
        right_pad = total_pad - left_pad
    
        left   = style_text(line *  left_pad, line_hue)
        right  = style_text(line * right_pad, line_hue)
        middle = style_text(str(arg), hue)
        
        if line == " ": return f"{left}{middle}"
        return f"{left}{middle}{right}"

def any_in(*args, eq: Any | None = None) -> bool:
    if len(args) == 1:
        args = args[0]
        if not isinstance(args, (list, tuple)):
            return args in eq
            
    for arg in args: 
        if arg in eq: return True
    return False
