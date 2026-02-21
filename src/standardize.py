import pandas as pd
import yaml
from dateutil import parser

def load_mapping(path):
    with open(path) as f:
        return yaml.safe_load(f)

def rename_columns(df, mapping):
    rename_dict = {}
    for standard, synonyms in mapping.items():
        for col in df.columns:
            if col in synonyms:
                rename_dict[col] = standard
    return df.rename(columns=rename_dict)

def build_full_name(df):
    if "full_name" not in df.columns and "first_name" in df.columns:
        df["full_name"] = df["first_name"].fillna("") + " " + df["last_name"].fillna("")
    return df

def normalize_phone(phone):
    if pd.isna(phone):
        return None
    return ''.join(filter(str.isdigit, str(phone)))[-10:]

def parse_date(date):
    try:
        return parser.parse(str(date)).date()
    except:
        return None

def standardize(df, mapping):
    df = rename_columns(df, mapping)
    df = build_full_name(df)

    if "phone" in df.columns:
        df["phone"] = df["phone"].apply(normalize_phone)

    df["signup_date"] = df["signup_date"].apply(parse_date)

    return df