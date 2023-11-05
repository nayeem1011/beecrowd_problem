# Read the integer value from the input
N = int(input())

# Calculate hours, minutes, and seconds
hours = N // 3600
minutes = (N % 3600) // 60
seconds = N % 60

# Print the time in the format HH:MM:SS
print("{:d}:{:d}:{:d}".format(hours, minutes, seconds))