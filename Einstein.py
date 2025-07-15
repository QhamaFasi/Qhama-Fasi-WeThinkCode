# einstein.py

# Speed of light in meters per second
speed_of_light = 300000000

# Ask the user for mass (in kilograms)
mass_str = input("Enter mass in kilograms: ")

# Convert the string input to an integer
mass = int(mass_str)

# Calculate energy using E = mc^2
energy = mass * speed_of_light * speed_of_light

# Show the energy in joules
print("Energy in joules:", energy)

