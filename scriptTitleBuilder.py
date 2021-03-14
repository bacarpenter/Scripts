from rich import print as richPrint
from datetime import datetime as dt

AUTHOR_NAME = "Ben Carpenter"
YEAR = dt.now().year


def main():
    richPrint(
        "[bold green]Script Title Builder[/bold green] | Ben Carpenter, 2021")
    richPrint("------------------------------------------")
    title = input("Title: ")
    useRich = not (input("Use rich (Y/n): ") == "n")

    titleString = ""
    if useRich:
        titleString += f"[bold green]{title}[/bold green] | {AUTHOR_NAME}, {YEAR}\n"
        for char in titleString[:-26]:
            titleString += "-"

        print(repr(titleString))
    else:
        titleString += f"{title} | {AUTHOR_NAME}, {YEAR}\n"
        for char in titleString:
            titleString += "-"

        print(titleString)


if __name__ == "__main__":
    main()
