from pathlib import Path


desktop_path = Path.home()/"Desktop"

for i in range(100):
    with open(desktop_path/f"virus_file_{i}.txt", "w") as f:
        f.write("This is a virus file. Delete it immediately!\n")
