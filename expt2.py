import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

object_length = 19

shadow = [35.3, 19, 0, 19, 41]
times = ["09:00", "11:00", "12:00", "13:00", "15:00"] 
angle_of_elevations = []

for length in shadow:
    if length == 0:
        angle_of_elevations.append(90.0) 
    else:
       
        angle_of_elevations.append(np.degrees(np.arctan(object_length / length)))

df = pd.DataFrame({
    'Time': times,
    'Shadow Length': shadow,
    'Angle of Elevation (Degrees)': angle_of_elevations
})

print("--- Shadow Lengths and Angles of Elevation ---")
print(df)
print("\nMinimum Shadow Length: 0")
print(f"Maximum Angle of Elevation: 90.0 degrees (at 0 shadow length)")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(times, shadow, marker='o', color='b')
plt.title('Time vs Shadow Length')
plt.xlabel('Time')
plt.ylabel('Shadow Length')
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(times, angle_of_elevations, marker='o', color='r')
plt.title('Time vs Solar Elevation Angle')
plt.xlabel('Time')
plt.ylabel('Angle of Elevation (Degrees)')
plt.grid(True)

plt.tight_layout()
plt.show()
