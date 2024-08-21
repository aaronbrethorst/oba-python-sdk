from helpers.load_env import load_settings
from helpers.formatters import bold, format_timestamp

from onebusaway import OnebusawaySDK

# Load settings from .env file, if it exists. If not, we'll use the
# Puget Sound server URL (which is also the default in the SDK) and
# the 'TEST' API key.
settings = load_settings(
    {
        "api_key": "TEST",
        "base_url": "https://api.pugetsound.onebusaway.org/",
    }
)

# Create a new instance of the OneBusAway SDK with the settings we loaded.
oba = OnebusawaySDK(**settings)

stopId = "1_19750"  # Replace with actual stop ID

# Retrieve arrival and departure information
response = oba.arrival_and_departure.list(stopId)

# Example to access specific data
arrivals_and_departures = response.data.entry.arrivals_and_departures

for arr_dep in arrivals_and_departures:
    has_realtime_data = arr_dep.predicted_arrival_time > 0

    print(f"{bold(arr_dep.route_short_name)} - {arr_dep.trip_headsign}")

    if arr_dep.predicted_arrival_time > 0:
        print(f"Predicted Arrival Time: {format_timestamp(arr_dep.predicted_arrival_time)}")

    print(f"Scheduled Arrival Time: {format_timestamp(arr_dep.scheduled_arrival_time)}")
    print(f"Vehicle ID: {arr_dep.vehicle_id}")
    print("")
