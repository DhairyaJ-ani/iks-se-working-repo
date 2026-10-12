import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Enter experimental data (using dummy data as none was provided)
data = {
    'Wind_Speed_m_s': [2, 4, 6, 8, 10, 12, 14, 16],
    'RPM': [15, 35, 60, 95, 135, 180, 230, 290]
}
df = pd.DataFrame(data)

# 2. Define constants
rho = 1.225  # Air density in kg/m^3
radius = 2.0  # Radius of blade in meters (assumed)

# 3. Calculate swept area
# A = π * r^2
area = np.pi * (radius ** 2)

# 4. Compute wind power using formula
# P = ½(ρ * A * v^3)
df['Power_Watts'] = 0.5 * rho * area * (df['Wind_Speed_m_s'] ** 3)

# 5. Display the stored results in the DataFrame
print("Experimental Data and Calculated Wind Power:")
print(df)

# 6. Plot graphs
plt.figure(figsize=(12, 5))

# Graph 1: Wind Speed vs RPM
plt.subplot(1, 2, 1)
plt.plot(df['Wind_Speed_m_s'], df['RPM'], marker='o', color='blue', linestyle='-')
plt.title('Wind Speed vs RPM')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('RPM')
plt.grid(True)

# Graph 2: Wind Speed vs Power
plt.subplot(1, 2, 2)
plt.plot(df['Wind_Speed_m_s'], df['Power_Watts'], marker='s', color='red', linestyle='-')
plt.title('Wind Speed vs Power')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Power (Watts)')
plt.grid(True)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
