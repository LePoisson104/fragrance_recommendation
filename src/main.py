import pandas as pd
from encoder import parse_note

df = pd.read_csv(
    "data/fra_cleaned.csv",
    sep=";",
    encoding="cp1252",
    decimal=","
)


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# print(df.columns.tolist())
# print(df.isnull().sum())

note_columns = [
    "top",
    "middle",
    "base",
    "mainaccord1",
    "mainaccord2",
    "mainaccord3",
    "mainaccord4",
    "mainaccord5"
]


df[note_columns] = df[note_columns].fillna("")

df["top"] = df["top"].apply(parse_note)
df["middle"] = df["middle"].apply(parse_note)
df["base"] = df["base"].apply(parse_note)

df["all_notes"] = df.apply(
    lambda row: sorted(set(
        row["top"]
        + row["middle"]
        + row["base"]
    )),
    axis=1
)

# print(df[["perfume", "all_notes"]].head())

