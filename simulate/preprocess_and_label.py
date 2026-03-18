import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("plant_health_data.csv")

FEATURE_COLUMNS = [
    "Soil_Moisture",
    "Ambient_Temperature",
    "Humidity",
    "Light_Intensity"
]

LABEL_COLUMN = "Plant_Health_Status"

X = df[FEATURE_COLUMNS]
y = df[LABEL_COLUMN].astype(str)

y = y.str.lower().str.strip()

label_mapping = {
    "healthy": 0,
    "moderate stress": 1,
    "high stress": 2
}

y = y.map(label_mapping)

mask = y.notna()
X = X[mask]
y = y[mask]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

clean_df = pd.DataFrame(X_scaled, columns=FEATURE_COLUMNS)
clean_df["label"] = y.astype(int)

clean_df.to_csv("clean_data.csv", index=False)

print("clean_data.csv created successfully!")
print("Class distribution:")
print(clean_df["label"].value_counts())
