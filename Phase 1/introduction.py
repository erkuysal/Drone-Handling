# Introduction to dronekit and it's capabilities ( basic level )

"""
    This file's main purpose is being an index for dronekit library's so users who'll develop furthermore
    using this can know where to look for its capabilities.
"""

# Import the necessary modules from DroneKit
from dronekit import connect, VehicleMode


# Function to connect to the drone and obtain the Vehicle object
def connect_to_drone(connection_string):
    print(f"Connecting to the drone on {connection_string}")
    vehicle = connect(connection_string, wait_ready=True)
    print("Connected to the drone!")
    return vehicle


# Function to demonstrate -----------> [Vehicle] <----------- object capabilities
def demonstrate_vehicle_capabilities(vehicle):
    print("\n** Vehicle Object Capabilities **")

    # Take off
    print("Taking off...")
    vehicle.simple_takeoff(10)  # Take off to 10 meters

    # Wait until the vehicle reaches a certain altitude
    while vehicle.location.global_relative_frame.alt < 9:
        print(f"Altitude: {vehicle.location.global_relative_frame.alt} meters")
        time.sleep(1)

    # Land the drone
    print("Landing...")
    vehicle.mode = VehicleMode("LAND")

    # Close connection
    vehicle.close()


# Function to demonstrate -----------> [Location] <----------- object capabilities
def demonstrate_location_capabilities(vehicle):
    print("\n** Location Object Capabilities **")

    # Print current location
    print("Current Location:")
    print(vehicle.location.global_frame)

    # Set a waypoint
    waypoint_location = vehicle.location.global_relative_frame
    waypoint_location.lat += 0.0001
    waypoint_location.lon += 0.0001
    waypoint_location.alt = 15.0

    print(f"Setting waypoint to: {waypoint_location}")
    vehicle.simple_goto(waypoint_location)

    # Wait until the vehicle reaches the waypoint
    while vehicle.mode.name == "GUIDED":
        distance_to_waypoint = vehicle.location.global_frame.distance_to(waypoint_location)
        print(f"Distance to waypoint: {distance_to_waypoint} meters")
        time.sleep(1)


# Function to demonstrate -----------> [Attitude]  <----------- object capabilities
def demonstrate_attitude_capabilities(vehicle):
    print("\n** Attitude Object Capabilities **")

    # Print current attitude (roll, pitch, yaw)
    print("Current Attitude:")
    print(vehicle.attitude)

    # Perform a roll maneuver
    print("Performing a roll maneuver...")
    vehicle.channels.overrides = {'1': 1700}  # Roll to the right
    time.sleep(2)
    vehicle.channels.overrides = {}  # Stop rolling

    # Close connection
    vehicle.close()


if __name__ == "__main__":
    import time

    # Connection string for simulated drone (replace with actual connection string)
    connection_string = "udp:127.0.0.1:14550"

    # Connect to the drone
    drone_vehicle = connect_to_drone(connection_string)

    # Demonstrate capabilities of Vehicle, Location, and Attitude objects
    demonstrate_vehicle_capabilities(drone_vehicle)
    demonstrate_location_capabilities(drone_vehicle)
    demonstrate_attitude_capabilities(drone_vehicle)
