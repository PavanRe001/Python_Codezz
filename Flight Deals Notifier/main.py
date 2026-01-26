from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
from dotenv import load_dotenv


load_dotenv()
# Initialize all managers
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get destination data from Sheety
sheet_data = data_manager.get_destination_data()

# Set your origin city code
ORIGIN_CITY_IATA = "BLR"  # Change this to your origin city

# Define search window (6 months from today)
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)

# Search for flights to each destination
for destination in sheet_data:
    print(f"\nSearching flights to {destination['city']}...")
    
    # Get flights
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    
    # Find the cheapest flight
    cheapest_flight = FlightData.find_cheapest_flight(flights)
    
    # Check if price is lower than the lowest price in the sheet
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"✈️ Low price alert! Only £{cheapest_flight.price} to fly from "
              f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
              f"departing {cheapest_flight.out_date} and returning {cheapest_flight.return_date}.")
        
        # Send notification
        message = (f"Low price alert! Only £{cheapest_flight.price} to fly from "
                   f"{cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                   f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}.")
        
        notification_manager.send_notification(message)

print("\n✅ Flight search complete!")
