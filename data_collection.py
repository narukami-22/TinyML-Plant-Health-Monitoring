import serial
import csv

ser = serial.Serial('COM3', 115200)

with open("plant_data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        line = ser.readline().decode().strip()
        # ESP32 should send: soil,temp,humidity,light
        values = line.split(',')
        if len(values) == 4:
            writer.writerow(values)
            print("Saved:", values)





