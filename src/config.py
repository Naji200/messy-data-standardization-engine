from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_DIR = BASE_DIR / "data" / "input"
BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"
QUARANTINE_DIR = BASE_DIR / "data" / "quarantine"
REPORT_DIR = BASE_DIR / "data" / "reports"

CONTRACT_PATH = BASE_DIR / "contracts" / "customer_contract.yaml"
MAPPING_PATH = BASE_DIR / "contracts" / "mappings.yaml"
