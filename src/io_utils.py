import shutil
from datetime import datetime
from pathlib import Path

def copy_to_bronze(file_path, bronze_dir):
    today = datetime.now().strftime("%Y-%m-%d")
    dest_dir = bronze_dir / today
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest = dest_dir / file_path.name
    shutil.copy(file_path, dest)
    return dest