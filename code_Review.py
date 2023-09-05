import numpy as np
import matplotlib.pyplot as plt

# Create an array of x values from -2*pi to 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate the sine values for each x
y = np.sin(x)

Z = np.cos(y)

# Create a plot 
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue')

# Add labels and a legend 
    plt.xlabel('x')  
   plt.ylabel('sin(x)')  
  plt.title('Sine Function')  
 plt.legend() 

# Show the plot 
plt.grid(True)
plt.show()

x = [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]
y = np.sin(x)  

# Plot the sine function 
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='red')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Function (Incorrect Data Structure)')
plt.legend()
plt.grid(True)
plt.show()
