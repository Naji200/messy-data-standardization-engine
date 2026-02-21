import pandas as pd
import yaml
from pathlib import Path
from .config import *
from .io_utils import copy_to_bronze
from .standardize import standardize, load_mapping
from .validate import validate
from .write_outputs import write_silver, write_quarantine

def main():
    mapping = load_mapping(MAPPING_PATH)
    contract = yaml.safe_load(open(CONTRACT_PATH))

    for file in INPUT_DIR.glob("*.csv"):
        bronze_file = copy_to_bronze(file, BRONZE_DIR)

        df = pd.read_csv(bronze_file)
        df = standardize(df, mapping)

        good, bad = validate(df, contract)

        write_silver(good, SILVER_DIR)
        write_quarantine(bad, QUARANTINE_DIR, file.stem)

if __name__ == "__main__":
    main()