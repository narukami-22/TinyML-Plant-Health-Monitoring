import pandas as pd

df = pd.read_csv("plant_data.csv")

def label(row):
    if row["soil"] < 25:
        return 0   # Underwatered
    elif row["soil"] > 75:
        return 1   # Overwatered
    elif row["temp"] > 35:
        return 2   # Poor Environment
    else:
        return 3   # Healthy

df["label"] = df.apply(label, axis=1)

df["soil"] /= 100
df["temp"] /= 50
df["humidity"] /= 100
df["light"] /= 1000

df.to_csv("clean_data.csv", index=False)
print("Preprocessing & labeling done")
