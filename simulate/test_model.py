import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("plant_model.keras")

sample = np.array([[0.20, 0.60, 0.70, 0.50]])
prediction = model.predict(sample)
print("Prediction:", prediction.argmax())