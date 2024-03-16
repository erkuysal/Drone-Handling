class ISA:
    def __init__(self):
        self.GRAVITY_ACCELERATION = 9.80665  # in m/s^2
        self.STANDARD_TEMPERATURE_SEA_LEVEL = 288.15  # in K
        self.STANDARD_PRESSURE_SEA_LEVEL = 101325  # in Pa
        self.STANDARD_DENSITY_SEA_LEVEL = 1.225  # in kg/m^3
        self.GAS_CONSTANT_AIR = 287.05  # in J/(kg·K)
        self.LAPSE_RATE = 0.0065  # in K/m
        self.GAMMA = 1.4  # adiabatic index for air

    def temperature_(self, altitude):
        if altitude < 11000:
            temperature = self.STANDARD_TEMPERATURE_SEA_LEVEL - self.LAPSE_RATE * altitude
        else:
            temperature = 216.65
        return temperature

    def pressure_(self, altitude):
        if altitude < 11000:
            pressure = (self.STANDARD_PRESSURE_SEA_LEVEL
                        * (1 - self.LAPSE_RATE * altitude / self.STANDARD_TEMPERATURE_SEA_LEVEL)
                        ** (self.GRAVITY_ACCELERATION / (self.LAPSE_RATE * self.GAS_CONSTANT_AIR)))
        else:
            pressure = 22632.06 * 2.71828 ** (-self.GRAVITY_ACCELERATION
                                              / (self.GAS_CONSTANT_AIR * self.temperature_(11000))
                                              * (altitude - 11000))
        return pressure

    def density_(self, altitude):
        temperature = self.temperature_(altitude)
        pressure = self.pressure_(altitude)
        density = pressure / (self.GAS_CONSTANT_AIR * temperature)
        return density

    def speed_of_sound(self, altitude):
        temperature = self.temperature_(altitude)
        speed_of_sound = (self.GAMMA * self.GAS_CONSTANT_AIR * temperature) ** 0.5
        return speed_of_sound

    def viscosity(self, altitude):
        temperature = self.temperature_(altitude)
        dynamic_viscosity = (1.458e-6 * temperature ** 1.5) / (temperature + 110.4)
        return dynamic_viscosity

    def mach_number(self, altitude, speed):
        speed_of_sound_at_altitude = self.speed_of_sound(altitude)
        mach_number = speed / speed_of_sound_at_altitude
        return mach_number

    def dynamic_pressure(self, altitude, speed):
        density_at_altitude = self.density_(altitude)
        dynamic_pressure = 0.5 * density_at_altitude * speed ** 2
        return dynamic_pressure

    def critical_cp(self, altitude):
        critical_cp = 1 - (0.076 * altitude / 288.15) ** 0.906
        return critical_cp

    def vacuum_cp(self, altitude):
        vacuum_cp = 1 - (0.245 * altitude / 288.15) ** 4.255
        return vacuum_cp

    def reynolds_number(self, altitude, speed, reference_length):
        density_at_altitude = self.density_(altitude)
        viscosity_at_altitude = self.viscosity(altitude)
        reynolds_number = density_at_altitude * speed * reference_length / viscosity_at_altitude
        return reynolds_number

    def laminar_cf(self, reynolds_number):
        laminar_cf = 1.328 / (reynolds_number ** 0.5)
        return laminar_cf

    def turbulent_cf(self, reynolds_number):
        turbulent_cf = 0.074 / (reynolds_number ** 0.2)
        return turbulent_cf

