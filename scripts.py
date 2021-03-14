#!/usr/local/bin/python3

from rich import print
from os import system

# Import scripts
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
        print(f"[{i}] {scripts[i].__name__}")

    i = int(input("Launch: "))
    print("Wooosh... 🐢")

    if isinstance(scripts[i], type(main)):
        """
        Compares type of script[i] to the know function main(). If they 
        are the same type (both functions), then run it as a function. 
        Other wise, run the main function in the external script
        """

        scripts[i]()

    else:
        scripts[i].main()


if __name__ == "__main__":
    main()
