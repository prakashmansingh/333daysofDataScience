import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the simulated datasets
vehicle_data = pd.read_csv('vehicle_registration_data.csv')
charging_stations_data = pd.read_csv('charging_stations_data.csv')

# Calculate the number of EV registrations per year
vehicle_data['EV_Registrations'] = (vehicle_data['Total_Vehicle_Registrations'] * vehicle_data['EV_Percentage'] / 100).astype(int)

# Plot the trend of EV registrations over the years
plt.figure(figsize=(10, 6))
plt.plot(vehicle_data['Year'], vehicle_data['EV_Registrations'], marker='o', linestyle='-', color='b')
plt.title('Trend of EV Registrations in Nepal')
plt.xlabel('Year')
plt.ylabel('Number of EV Registrations')
plt.grid(True)
plt.show()

# Plot the locations of charging stations
plt.figure(figsize=(8, 8))
plt.scatter(charging_stations_data['Longitude'], charging_stations_data['Latitude'], c='r', marker='^')
for i, location in enumerate(charging_stations_data['Location']):
    plt.annotate(location, (charging_stations_data['Longitude'][i], charging_stations_data['Latitude'][i]), textcoords="offset points", xytext=(0,5), ha='center')
plt.title('EV Charging Stations in Nepal')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()                                                                                                                             