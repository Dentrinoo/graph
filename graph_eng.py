from math import exp  # Import the exponential function from the math module

# Taking input values from the user for initial z, step size, and final z
z = float(input('Enter the initial value of the variable: '))
hz = float(input('Enter the step size for the variable: '))
kon = float(input('Enter the final value of the variable: '))
rkon = kon + 0.1e-10  # Slightly extend the range to include the final value due to floating-point precision

# Initialize variables
a = z  # Store the initial value of z
s = []  # Array to store S1 values
zed = []  # Array to store z values
k = 0  # Counter for the number of elements in the arrays
n = 0  # Counter for the graph plotting
d = 0  # Flag for determining the presence of the x-axis
s1pol = 0  # Counter for positive values of S1
s2pol = 0  # Counter for positive values of S2
g = 1  # Unused variable

# Finding the maximum and minimum of S1 and calculating S1 and S2 values
print('\nTable of function values: ')
print('      Z           S1             S2')
while z < rkon:  # Iterate while z is less than the extended final value
    s1 = z**3 - 4.51*z**2 - 23.9*z + 20.1  # Calculate S1
    s2 = exp(-z) - (z - 1)**2  # Calculate S2
    s.append(s1)  # Append S1 value to the list
    zed.append(z)  # Append the current z value to the list
    
    # Print S1 and S2 values with appropriate formatting
    if abs(s1) >= 9999 and abs(s2) >= 9999:
        print('{:10.3f}    {:9.2e}      {:9.2e}'.format(z, s1, s2))
    elif abs(s1) >= 9999 and 0 <= abs(s2) <= 9999:
        print('{:10.3f}    {:9.2e}      {:9.3f}'.format(z, s1, s2))
    elif abs(s2) >= 9999 and 0 <= abs(s1) <= 9999:
        print('{:10.3f}    {:9.3f}      {:9.2e}'.format(z, s1, s2))
    elif 0 <= abs(s2) <= 9999 and 0 <= abs(s1) <= 9999:
        print('{:10.3f}    {:9.3f}      {:9.3f}'.format(z, s1, s2))

    # Determine the minimum and maximum of S1
    if a == z:
        s1min = s1  # Initialize s1min with the first S1 value
        s1max = s1  # Initialize s1max with the first S1 value
    elif s1min > s1:
        s1min = s1  # Update s1min if the current S1 is smaller
    elif s1max < s1:
        s1max = s1  # Update s1max if the current S1 is larger

    # Count positive values of S1 and S2
    if s1 > 0:
        s1pol += 1
    if s2 > 0:
        s2pol += 1

    k += 1  # Increment the element counter
    z += hz  # Increment z by the step size

# Print counts of positive S1 and S2 values
print('\nNumber of positive elements in function S1: ', s1pol)
print('Number of positive elements in function S2: ', s2pol)

# Calculate the position of the z-axis for the graph
print()
ox = (-s1min) / (s1max - s1min) * 65  # Scale the axis position to 65 columns
ox = round(ox)  # Round to the nearest integer
print()

# Check if the x-axis crosses the graph (S1 has positive and negative values)
if s1max > 0 and s1min < 0:
    d = 1  # Flag indicating the presence of the x-axis

# Print the graph title
print('Graph of function S1:')
print()

# Plot the graph of S1
while n < k:  # Iterate through the calculated values
    m = (s[n] - s1min) / (s1max - s1min) * 65  # Scale S1 values to 65 columns
    m = int(m)  # Convert to an integer for positioning
    r = 0  # Position counter
    t = 0  # Tracker for the number of printed elements in the row

    if ox == m:
        t += 1  # Adjust if the axis overlaps with the graph point

    print('{:9.3f}'.format(zed[n]), end='')  # Print the current z value
    print(' ', end='')  # Add space before the graph

    while True:  # Loop to plot points
        if r == m:  # Plot the graph point
            print('*', end='')
            t += 1
            r += 1
            if d == 0:  # Adjust for the absence of the axis
                t += 1
            continue
        if r == ox and d == 1:  # Plot the x-axis
            print('|', end='')
            t += 1
            r += 1
            continue

        print(' ', end='')  # Print spaces for alignment
        r += 1
        if t >= 2:  # End the row after plotting the point and axis (if any)
            print('')
            break
    n += 1  # Increment the graph counter

input()  # Pause the program to view the output