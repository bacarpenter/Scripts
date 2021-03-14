from os import mkdir, system
from rich import print


CLASS_LOCATION = "/Users/bencarpenter/OneDrive/School/AP Computer Science A"
CLASS_LOCATION_TERM = "/Users/bencarpenter/OneDrive/School/AP\ Computer\ Science\ A"


def main():
    with open(f"{CLASS_LOCATION}/.weekCounter.txt", "r") as wk:
        weekCounter = int(wk.readline())

    with open(f"{CLASS_LOCATION}/.weekCounter.txt", "w") as wk:
        wk.write(str(weekCounter + 1))

    mkdir(f"{CLASS_LOCATION}/Week {weekCounter + 1}")
    system(
        f"cd {CLASS_LOCATION_TERM}/Week\ {weekCounter + 1} && touch {weekCounter + 1}.1\ Discussion\ post.docx")

    print(f"[green]Week {weekCounter + 1} created![/green]")


if __name__ == "__main__":
    main()
