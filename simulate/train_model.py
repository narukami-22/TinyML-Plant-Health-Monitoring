import tensorflow as tf
import pandas as pd

df = pd.read_csv("clean_data.csv")

X = df[["soil","temp","humidity","light"]]
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
model.save("plant_model.keras")

print("Model trained successfully")