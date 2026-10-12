import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks

# Step 1 & 2: Load the recorded .wav file
file_name = "conch.wav"  # Replace with your actual file name
sample_rate, data = wavfile.read(file_name)

# If the audio is stereo (2 channels), convert it to mono by taking the first channel
if len(data.shape) > 1:
    data = data[:, 0]

# Step 3: Time-Domain Analysis (Waveform)
# Calculate the duration of the audio to create a time array
duration = len(data) / sample_rate
time = np.linspace(0., duration, len(data))

# Step 4: Frequency-Domain Analysis (Spectrum using FFT)
n = len(data)
yf = np.fft.fft(data)  # Perform Fast Fourier Transform
xf = np.fft.fftfreq(n, 1 / sample_rate)  # Generate frequency axes

# We only need the positive half of the frequencies
yf = np.abs(yf[:n//2])
xf = xf[:n//2]

# Step 5 & 6: Find Fundamental Frequency and Harmonics
# Find peaks in the frequency spectrum
# 'height' filters out background noise, 'distance' ensures peaks aren't too close
peaks, _ = find_peaks(yf, height=np.max(yf)*0.1, distance=sample_rate/50)

peak_freqs = xf[peaks]
peak_amps = yf[peaks]

# Sort peaks by amplitude to find the main pitch (highest peak)
sorted_indices = np.argsort(peak_amps)[::-1]
fundamental_freq = peak_freqs[sorted_indices[0]]

# Sort the remaining peaks by frequency to identify harmonics above the fundamental
sorted_freq_peaks = np.sort(peak_freqs)
harmonics = [f for f in sorted_freq_peaks if f > fundamental_freq][:3] # Get the first 3 harmonics

# --- Console Output ---
print("-" * 30)
print(f"Fundamental Frequency (f0): {fundamental_freq:.2f} Hz")
for i, harm in enumerate(harmonics, start=1):
    print(f"Harmonic {i}: {harm:.2f} Hz")
    print(f"Ratio (Harmonic / f0): {harm/fundamental_freq:.2f}")
print("-" * 30)

# --- Plotting ---
plt.figure(figsize=(12, 6))

# Plot 1: Time Domain
plt.subplot(2, 1, 1)
plt.plot(time, data, color='teal')
plt.title('Time Domain (Waveform)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True, alpha=0.3)

# Plot 2: Frequency Domain (FFT)
plt.subplot(2, 1, 2)
plt.plot(xf, yf, color='darkred')
plt.title('Frequency Spectrum (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, max(harmonics)*1.5 if harmonics else 2000) # Zoom into the relevant frequency range
plt.grid(True, alpha=0.3)

# Highlight the fundamental frequency on the plot
plt.axvline(x=fundamental_freq, color='gold', linestyle='--', label=f'f0 = {fundamental_freq:.1f} Hz')
plt.legend()

plt.tight_layout()
plt.show()