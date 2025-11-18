from importlib import import_module
from typing import NoReturn
import argparse
import unittest
from . import utils # Change to: import utils
import time

def retrieve_tests(one_mod: str | None = None) -> unittest.TestCase:
    if one_mod:
        module = import_module(f"tests.{one_mod}")
        return [cls for name, cls in vars(module).items() if 
               isinstance(cls, type) and issubclass(cls, 
               unittest.TestCase) and cls is not 
               unittest.TestCase]
    return unittest.TestLoader().discover(start_dir=str(
           utils.TESTS_DIR), pattern="*.py")

def test_suite(suite: list[type] | None = None) -> unittest.TestSuite:
    if suite is None: return retrieve_tests()
    if isinstance(suite, list):
        ts = unittest.TestSuite()
        for cls in suite: ts.addTest(unittest.TestLoader(
                          ).loadTestsFromTestCase(cls))
        return ts

def render_trace(result: unittest.TestResult) -> None:
    hues    = ["red", "red", "yellow"]
    content = {
        "    ERRORS": result.errors,
        "  FAILURES": result.failures,
        "   SKIPPED": result.skipped,
    }
    
    for i, (tag, trace) in enumerate(content.items()):
        hue    = "green" if not trace else hues[i]
        amount = utils.style_text(len(trace), hue)
        print(f"{tag.title()}: {amount}")
        if i == 2: print()
    
    for (tag, trace), hue in zip(content.items(), hues):
        if not trace: continue
        print(utils.center(f"《 {tag.strip()} 》", hue=hue))
        for pos, (test, traceback) in enumerate(trace):
            method = test._testMethodName
            print(f"\nIndex: {pos+1}")
            print(f" Test: {method[5:]}\n")
            print(traceback)
            if "\n" not in traceback: print()

def run_tests(test_cls: list[type]|None = None) -> NoReturn:
    runner        = unittest.TextTestRunner()
    suite, start  = test_suite(test_cls), time.time()
    result, end   = runner.run(suite),    time.time()   
    failures      = result.failures + result.errors
    off           = result.skipped  + failures
    successful    = result.testsRun - len(off)
    if not result.testsRun: success = True
    else: success = successful != 0
    color         = "red" if failures else "green"
    hue           = "green" if success else "red"
    succeeded     = utils.style_text(successful, hue)
    duration      = utils.format_time(round(end - start, 4))

    utils.clear()    
    header = "《 TESTS RESULT 》"
    print(utils.center(header, "=", "magenta", color))
    print(f"\n Tests ran: {result.testsRun}")
    print(f"  Duration: {duration}")
    print(f"Successful: {succeeded}")
    render_trace(result)
    utils.underline(hue=color)
    utils.sys.exit(0 if result.wasSuccessful() else 1)

if __name__ == "__main__":
    parser     = argparse.ArgumentParser(description=
                 utils.helper())
    subparsers = parser.add_subparsers(dest="command")
    mods       = {"None": None}
    
    for tests_file in sorted(utils.TESTS_DIR.glob("*.py")):
        name = tests_file.stem
        if name.startswith("_"): continue
        subparsers.add_parser(name)
        mods[name] = retrieve_tests(name)

    if not utils.any_in(utils.sys.argv, eq=mods.keys()
        ): utils.helper(skip=len(utils.sys.argv) - 1)

    run_tests(mods[parser.parse_args().command or "None"])
