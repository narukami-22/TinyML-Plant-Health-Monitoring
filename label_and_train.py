import pandas as pd
import tensorflow as tf

df = pd.read_csv("clean_data.csv")

def label(row):
    if row["soil"] < 0.25:
        return 0   # Underwatered
    elif row["soil"] > 0.75:
        return 1   # Overwatered
    elif row["temp"] > 0.7:
        return 2   # Poor environment
    else:
        return 3   # Healthy

df["label"] = df.apply(label, axis=1)

X = df[["soil", "temp", "humidity", "light"]]
y = df["label"]

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(4, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X, y, epochs=30)
model.save("plant_model")

print("Model trained and saved")
