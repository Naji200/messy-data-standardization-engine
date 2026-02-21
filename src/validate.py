import re
import pandas as pd

def validate(df, contract):
    good = []
    bad = []

    email_pattern = re.compile(contract["email_regex"])
    seen_ids = set()

    for _, row in df.iterrows():
        reasons = []

        if pd.isna(row.get("customer_id")):
            reasons.append("missing_customer_id")

        if pd.isna(row.get("full_name")):
            reasons.append("missing_full_name")

        if not email_pattern.match(str(row.get("email"))):
            reasons.append("invalid_email")

        if pd.isna(row.get("signup_date")):
            reasons.append("invalid_date")

        if row.get("customer_id") in seen_ids:
            reasons.append("duplicate_customer_id")

        seen_ids.add(row.get("customer_id"))

        if reasons:
            row["reject_reason"] = ",".join(reasons)
            bad.append(row)
        else:
            good.append(row)

    return pd.DataFrame(good), pd.DataFrame(bad)