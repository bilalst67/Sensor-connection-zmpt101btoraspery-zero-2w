import RPi.GPIO as gp
import time as t
import csv

pin2 = 40

gp.setmode(gp.BOARD)
gp.setup(pin2, gp.IN)

# To add a title on the first run, we open the file in 'w' mode.
with open('veri.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Pin2"])  # Tıtle of the column

for _ in range(50):
    with open('veri.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([ gp.input(pin2)])
    t.sleep(0.001)

gp.cleanup()