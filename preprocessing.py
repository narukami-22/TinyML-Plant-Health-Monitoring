import pandas as pd

df = pd.read_csv("plant_data.csv",
                 names=["soil", "temp", "humidity", "light"])

df.dropna(inplace=True)

df["soil"] /= 100
df["temp"] /= 50
df["humidity"] /= 100
df["light"] /= 1000

df.to_csv("clean_data.csv", index=False)
print("Preprocessing done")