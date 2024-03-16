# ISA Calculator

# Constants
LAPSE_RATE = 0.0065  # lapse rate in K/m
STANDARD_TEMPERATURE_SEA_LEVEL = 288.15  # in K
STANDARD_PRESSURE_SEA_LEVEL = 101325  # in Pa
STANDARD_DENSITY_SEA_LEVEL = 1.225  # in kg/m^3
GAS_CONSTANT_AIR = 287.05  # in J/(kg·K)
GRAVITY_ACCELERATION = 9.80665  # in m/s^2
GAMMA = 1.4  # adiabatic index for air


# Functions
def temperature_(altitude):
    # ISA temperature calculation in Kelvin
    if altitude < 11000:
        temperature = STANDARD_TEMPERATURE_SEA_LEVEL - LAPSE_RATE * altitude
    else:
        temperature = 216.65
    return temperature


def pressure_(altitude):
    # ISA pressure calculation in Pa
    if altitude < 11000:
        pressure = STANDARD_PRESSURE_SEA_LEVEL * (1 - LAPSE_RATE * altitude / STANDARD_TEMPERATURE_SEA_LEVEL) ** (
                    GRAVITY_ACCELERATION / (LAPSE_RATE * GAS_CONSTANT_AIR))
    else:
        pressure = 22632.06 * 2.71828 ** (
                    -GRAVITY_ACCELERATION / (GAS_CONSTANT_AIR * temperature_(11000)) * (altitude - 11000))
    return pressure


def density_(altitude):
    # ISA density calculation in kg/m^3
    temperature = temperature_(altitude)
    pressure = pressure_(altitude)
    density = pressure / (GAS_CONSTANT_AIR * temperature)
    return density


def speed_of_sound(altitude):
    # Speed of sound calculation in m/s
    temperature = temperature_(altitude)
    speed_of_sound = (GAMMA * GAS_CONSTANT_AIR * temperature) ** 0.5
    return speed_of_sound


def viscosity(altitude):
    # Dynamic viscosity calculation in kg/(m*s)
    temperature = temperature_(altitude)
    viscosity = (1.458e-6 * temperature ** 1.5) / (temperature + 110.4)

    # Dynamic viscosity calculation in N·s/m²
    viscosity_ = viscosity * GRAVITY_ACCELERATION  # Convert from kg/(m·s) to N·s/m²
    return viscosity, viscosity_


def mach_number(altitude, speed):
    # Mach number calculation
    speed_of_sound_at_altitude = speed_of_sound(altitude)
    mach_number = speed / speed_of_sound_at_altitude
    return mach_number


def dynamic_pressure(altitude, speed):
    # Dynamic pressure calculation in Pa
    density_at_altitude = density_(altitude)
    dynamic_pressure = 0.5 * density_at_altitude * speed ** 2
    return dynamic_pressure


def critical_cp(altitude):
    # Critical pressure coefficient calculation
    critical_cp = 1 - (0.076 * altitude / 288.15) ** 0.906
    return critical_cp


def vacuum_cp(altitude):
    # Vacuum pressure coefficient calculation
    vacuum_cp = 1 - (0.245 * altitude / 288.15) ** 4.255
    return vacuum_cp


def reynolds_number(altitude, speed, reference_length):
    # Reynolds number calculation
    density_at_altitude = density_(altitude)
    viscosity_at_altitude, viscosity_ = viscosity(altitude)
    reynolds_number = density_at_altitude * speed * reference_length / viscosity_at_altitude
    return reynolds_number


def laminar_cf(reynolds_number):
    # Laminar skin friction coefficient calculation
    laminar_cf = 1.328 / (reynolds_number ** 0.5)
    return laminar_cf


def turbulent_cf(reynolds_number):
    # Turbulent skin friction coefficient calculation
    turbulent_cf = 0.074 / (reynolds_number ** 0.2)
    return turbulent_cf


def print_values(altitude, speed, reference_length):
    temperature = temperature_(altitude)
    density = density_(altitude)
    pressure = pressure_(altitude)
    speed_of_sound_value = speed_of_sound(altitude)
    viscosity_value, viscosity_value_ = viscosity(altitude)
    mach_number_value = mach_number(altitude, speed)
    dynamic_pressure_value = dynamic_pressure(altitude, speed)
    critical_cp_value = critical_cp(altitude)
    vacuum_cp_value = vacuum_cp(altitude)
    reynolds_number_value = reynolds_number(altitude, speed, reference_length)
    laminar_cf_value = laminar_cf(reynolds_number_value)
    turbulent_cf_value = turbulent_cf(reynolds_number_value)

    print("\nResults:")
    print(f"Temperature: {temperature} K")
    print(f"Density: {density} kg/m^3")
    print(f"Pressure: {pressure} Pa")
    print(f"Speed of Sound: {speed_of_sound_value} m/s")
    print(f"Viscosity: {viscosity_value} kg/(m*s)"
          f"\nViscosity: {viscosity_value_} N·s/m²")
    print(f"Mach Number: {mach_number_value}")
    print(f"Dynamic Pressure: {dynamic_pressure_value} Pa")
    print(f"Critical Cp: {critical_cp_value}")
    print(f"Vacuum Cp: {vacuum_cp_value}")
    print(f"Reynolds Number: {reynolds_number_value}")
    print(f"Laminar Cf: {laminar_cf_value}")
    print(f"Turbulent Cf: {turbulent_cf_value}")


def main():
    altitude = float(input("Enter altitude (m): "))
    speed = float(input("Enter speed (m/s): "))
    reference_length = float(input("Enter reference length (m): "))

    print_values(altitude, speed, reference_length)


if __name__ == "__main__":
    main()
