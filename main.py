#!/usr/bin/env python3
## Importing the necessary libraries
from utils.console import print_markdown
from rich import console
import time

# Setup the console
console = console.Console()

# Print welcome message
print_markdown("""
# Welcome to pokeinject!
""")
console.print("[blue]This is a tool to inject a custom mod into a pokete.\n")

# Rebuild the mods.py file
def rebuild():
    # Get confirmation from the user
    console.print("[bold red] > We are going to rebuild the mods.py file. This will erase all your modifications. Are you sure? [bold green]y/n")
    answer = input()
    if answer == "y":
        # Erase the file and rebuild it
        rebuilding = f"""
#!/usr/bin/env python3
version = "0.1.0"
name = "pokeinject-mod"

def mod_p_data(p_data):
"""
        console.print("[bold red] > Rebuilding mods.py file.")
        time.sleep(1)
        with open("pokete/mods/mods.py", "w") as f:
            f.write(rebuilding)
    else:
        console.print("[bold red] > Cancelled.")
        exit()

def main():
    console.print("[bold green] > How many pokete do you want to rename?")
    pokete = int(input())
    rebuild()
    for i in range(pokete):
        console.print("[bold green] > What is the name of the pokete?")
        pokete_name = input()
        console.print("[bold green] > What is the new name of the pokete?")
        new_name = input()
        rebuilding = f"""   p_data.pokes["{pokete_name}"]["name"] = "{new_name}"
        """
        with open("pokete/mods/mods.py", "a") as f:
            f.write(rebuilding)
    console.print("[bold green] > Done! Now run __init__.py to reload the mod.")

main()