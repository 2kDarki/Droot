from .templates.utils import style_text, TERM_WIDTH, sys
from collections.abc import KeysView as keys
from pathlib import Path
import textwrap as wrap
import random
import time
import os

prefix = f"~{os.sep}...{os.sep}"
cwd    = str(Path.cwd())

if len(cwd.split(os.sep)) > 3:
    cwd = prefix + os.sep.join(cwd.split(os.sep)[-2:])

def gen_otp() -> str:
    number = random.randint(0, 999)
    return format_order(number, deno=3)

def list_items(items:list|tuple|dict, guide:str|None = None,
               indent: bool = False) -> None:
    items = [str(i) for i in items]    
    if guide: print(style_text(guide, underline=True)+":")  
    for opt, item in enumerate(items):
        order = format_order(opt+1, form=" ")
        text = f"{order}. {item}"
        if indent:          
              i = len(order) + 2 + len(item.split(":")[0])+2
              text = wrap.fill(text,subsequent_indent=" "*i,
                     width=TERM_WIDTH)
        print(text)

def format_order(order, deno:int = 2, form:str = "0")-> str:
    if not isinstance(form, str): 
        raise TypeError("form should be a string")
    if not isinstance(deno, int) or deno < 0:
        raise TypeError("deno should be an integer")
    return str(order).rjust(deno, form)

def label(iterable: list | tuple | dict | str,
         hue: str = "cyan") -> list[str] | str:
    if isinstance(iterable, str):
        return style_text(iterable, fg=hue)
    return [style_text(head, fg=hue) for head in iterable]

def choose(options: dict|list, cursor: str = ">>> ",
          hue: str | None = "cyan"):
    """
Custom input menu for choosing an option from a list

Usage:
  - This function does not list the options.
  - This function works best when paired with the 
    function list_items(...)
  - For the full function, check out my toolkit on GitHub:
    https://github.com/2kDarki/TUI-Toolkit

Args:
    options (dict): a dictionary or list containing the
                    values to be chosen by their index
                    position
    cursor   (str): a cursor input prompt. Default '>>> '
    hue      (str): the color of the cursor
    """
    while True:
        try:
            choice = input(style_text(cursor, hue))
            choice = int(choice) - 1
            if 0 <= choice < len(options):
                return pick_from(options, choice)
        except ValueError: pass
        err(f"Choose a number between 1 and {len(options)}")

def pick_from(iterable: list|tuple|dict|keys, choice: int):
    if choice < 0: choice = len(iterable)-abs(choice)
    if isinstance(iterable, (list, tuple, keys)):
        return list(iterable)[choice]
    return next((iterable[val] for pos, val in 
           enumerate(iterable) if pos == int(choice)))

def err(msg: str|None = None, transmit: bool = False, 
        otp: bool = False) -> None:
    if otp:
        msg = "Incorrect OTP. Overwrite aborted."
        transmit = True
    if not transmit: 
      print(f"\n{style_text(msg, 'red')}\n")
      return
    print()
    for ch in msg:
        delay = 0.1
        if ch == " ": delay = 0.5
        print(style_text(ch, "red"), end="", flush=True)
        time.sleep(delay)
    print("\n")
    if otp: sys.exit(1)
