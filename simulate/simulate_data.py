import random
import csv

with open("plant_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["soil","temp","humidity","light"])

    for _ in range(500):
        soil = random.randint(0, 100)
        temp = random.randint(15, 45)
        humidity = random.randint(20, 90)
        light = random.randint(100, 1000)

        writer.writerow([soil, temp, humidity, light])

print("Simulated dataset created")
