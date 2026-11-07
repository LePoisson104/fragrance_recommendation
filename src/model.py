import pandas as pd

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

print(df.columns.tolist())
print(df.isnull().sum())

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
