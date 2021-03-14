from rich import print
from rich.align import Align
from rich.panel import Panel
from rich.text import Text
from rich.padding import Padding
from rich.columns import Columns


def main():
    text = [Text("         ______________\n        /             /|\n       /             / |\n      /____________ /  |\n     | ___________ |   |\n     ||           ||   |\n     ||           ||   |\n     ||           ||   |\n     ||___________||   |\n     |   _______   |  /\n    /|  (_______)  | /\n   ( |_____________|/\n    \\\n.=======================.\n| ::::::::::::::::  ::: |\n| ::::::::::::::[]  ::: |\n|   -----------     ::: |\n`-----------------------'"), Text("Welcome to Macintosh", style="blue bold")]
    panel = Padding(Panel(Columns(text, padding=(0, 12))), 1)
    print(panel)


if __name__ == "__main__":
    main()
