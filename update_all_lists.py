import json
import subprocess
from pathlib import Path

def main():
    config_file = Path("google_lists.json")
    if not config_file.exists():
        print(f"{config_file} not found. Nothing to update.")
        return

    with open(config_file, "r") as f:
        lists = json.load(f)

    for item in lists:
        url = item.get("url")
        neighborhood_id = item.get("neighborhood_id")

        if url and neighborhood_id:
            print(f"\n--- Updating {neighborhood_id} from {url} ---")
            subprocess.run(["python", "update_from_google_list.py", url, neighborhood_id], check=False)

if __name__ == "__main__":
    main()
