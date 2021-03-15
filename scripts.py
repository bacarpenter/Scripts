#!/usr/local/bin/python3

from rich import print
from os import system, getcwd

# Import scripts from pyScripts module if being run from outside directory
if getcwd() == '/Users/bencarpenter':
    from pyScripts import buildClass
    from pyScripts import mergePdf
    from pyScripts import scriptTitleBuilder
    from pyScripts import VHSWeekTool

# Other wise, do a normal import
else:
    import buildClass
    import mergePdf
    import scriptTitleBuilder
    import VHSWeekTool

# Need to make a function, as the sync notes is a shell script


def syncNotes():
    system("cd ~/Notes && ./sync")


scripts = [
    buildClass,
    mergePdf,
    scriptTitleBuilder,
    VHSWeekTool,
    syncNotes,
]


def main():
    # Welcome
    print('[bold green]Script Launcher[/bold green] | Ben Carpenter, 2021\n-------------------------------------')

    # Print script options
    for i in range(len(scripts)):
        scriptName = scripts[i].__name__.replace("pyScripts.", "")
        print(f"[{i}] {scriptName}")

    try:
        toLaunch = int(input("Launch: "))
        if toLaunch > len(scripts) or toLaunch < 0:
            raise(1)
    except Exception:
        # Not taking all exceptions, such as ⌃C, as user may want to exit, and I do not want to handle that here.
        print("[bold red]Error. Invalid Script Option.[/bold red]")
        exit(1)  # Exception 1 == Invalid Script option
    except KeyboardInterrupt:
        # Handle a keyboard interrupt command, so that the stack trace doesn't get printred
        print("\nGood bye 👋")
        exit(0)

    print("Wooosh... 🐢")

    if isinstance(scripts[toLaunch], type(main)):
        """
        Compares type of script[i] to the know function main(). If they 
        are the same type (both functions), then run it as a function. 
        Other wise, run the main function in the external script
        """

        scripts[toLaunch]()

    else:
        scripts[toLaunch].main()


if __name__ == "__main__":
    main()
