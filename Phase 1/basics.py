# Take off / Landing Basics.

import dronekit
import time

# Connect to the vehicle
vehicle = dronekit.connect('tcp:127.0.0.1:5760')  # Replace with actual vehicle connection string

# Wait for the connection to be established
while not vehicle.is_armable:
    print("Waiting for vehicle to become armable")
    time.sleep(1)

# Set takeoff altitude (in meters)
target_altitude = 5

print("Taking off!")
vehicle.simple_takeoff(target_altitude)

# Wait for the vehicle to reach the target altitude
while True:
    print("Altitude: ", vehicle.location.global_relative_frame.alt)
    if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
        print("Target altitude reached!")
        break
    time.sleep(1)

# Hover for a few seconds
time.sleep(5)

print("Landing")
vehicle.mode = dronekit.VehicleMode("LAND")

# Wait for the vehicle to land
while vehicle.armed:
    time.sleep(1)

print("Landed successfully!")

# Close the vehicle object
vehicle.close()