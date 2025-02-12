import matplotlib.pyplot as pl
import pandas as pd
import time as t

# data ending time measurement
start_time = t.time()

# Data read
veri = pd.read_csv("veri.csv")

# Pin 2 values
pin2_values = veri.iloc[:, 0].values

# Graph drawing
pl.plot(range(len(pin2_values)), pin2_values, color='blue', label='Pin 2', marker='x')

# Graph settings
pl.xlabel('Örnek Numarasi')  
pl.ylabel('Gerilim (V)')
pl.title('Pin 2 Gerilim Grafiği')

# ending time result
print("Zaman:", t.time() - start_time)

# Graph show
pl.legend()
pl.show()