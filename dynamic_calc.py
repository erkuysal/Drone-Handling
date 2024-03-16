import time

# Function definitions for ISA calculations (temperature_ISA, pressure_ISA, density_ISA, etc.)
from Calc.ISA_Calc_V3 import ISA

calc = ISA()

def update_drone_position():
    # Simulated function to update drone position (altitude)
    # In a real scenario, this function would interact with the drone's sensors to get the altitude
    return  # Update drone position


def main():
    while True:
        # Update drone position (altitude)
        altitude = update_drone_position()

        # Calculate ISA values based on the new altitude
        temperature = calc.temperature_(altitude)
        pressure = calc.pressure_(altitude)
        density = calc.density_(altitude)
        speed_of_sound_value = calc.speed_of_sound(altitude)
        dynamic_viscosity_kg_per_ms, dynamic_viscosity_N_sec_per_m2 = calc.viscosity(altitude)

        # Print ISA values
        print("\nISA Values at Altitude", altitude, "m:")
        print("Temperature:", temperature, "K")
        print("Pressure:", pressure, "Pa")
        print("Density:", density, "kg/m^3")
        print("Speed of Sound:", speed_of_sound_value, "m/s")
        print("Dynamic Viscosity (kg/(m·s)):", dynamic_viscosity_kg_per_ms)
        print("Dynamic Viscosity (N·s/m²):", dynamic_viscosity_N_sec_per_m2)

        # Wait for a short period before updating the drone position again
        time.sleep(0.5)  # Adjust the time interval as needed


if __name__ == "__main__":
    main()
