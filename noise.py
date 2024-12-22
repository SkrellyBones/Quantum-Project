import numpy as np
import matplotlib.pyplot as plt
#literally googled "generate chaotic noise in python" and this came up in the fucking ai search lmao

def logistic_map(x, r):
  return r * x * (1 - x)

def generate_chaotic_noise(x0, r, n):
  x = np.zeros(n)
  x[0] = x0
  for i in range(1, n):
    x[i] = logistic_map(x[i-1], r)
  return x

# Generate chaotic noise
x0 = 0.5
r = 3.9
n = 1000
noise = generate_chaotic_noise(x0, r, n)

# Plot the noise
plt.plot(noise)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Chaotic Noise')
plt.show()