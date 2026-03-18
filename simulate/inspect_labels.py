import pandas as pd

df = pd.read_csv("plant_health_data.csv")

print("Unique Plant_Health_Status values:")
print(df["Plant_Health_Status"].unique())
