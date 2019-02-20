# CapstoneProject

NASA battery data analysis
Data Structure:
cycle: top level structure array containing the charge, discharge and impedance operations<br>

    type: operation  type, can be charge, discharge or impedance.

    ambient_temperature: ambient temperature (degree C).

    time: the date and time of the start of the cycle, in MATLAB  date vector format.

    data: data structure containing the measurements

   for charge the fields are:

        Voltage_measured: Battery terminal voltage (Volts)

        Current_measured: Battery output current (Amps)

        Temperature_measured: Battery temperature (degree C)

        Current_charge: Current measured at charger (Amps)

        Voltage_charge: Voltage measured at charger (Volts)

        Time: Time vector for the cycle (secs)

  for discharge the fields are:

        Voltage_measured: Battery terminal voltage (Volts)

        Current_measured: Battery output current (Amps)

        Temperature_measured: Battery temperature (degree C)

        Current_charge: Current measured at load (Amps)

        Voltage_charge: Voltage measured at load (Volts)

        Time: Time vector for the cycle (secs)

        Capacity: Battery capacity (Ahr) for discharge till 2.7V

   for impedance the fields are:

        Sense_current: Current in sense branch (Amps)

        Battery_current: Current in battery branch (Amps)

        Current_ratio: Ratio of the above currents

        Battery_impedance: Battery impedance (Ohms) computed from raw data

        Rectified_impedance: Calibrated and smoothed battery impedance (Ohms)

        Re: Estimated electrolyte resistance (Ohms)

        Rct: Estimated charge transfer resistance (Ohms)
