from dotenv import load_dotenv


load_dotenv()
class FlightData:
    """Class to handle flight data and find the cheapest flights"""
    
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    @staticmethod
    def find_cheapest_flight(data):
        """Find the cheapest flight from Amadeus API response data"""
        # Handle empty data if no flight or Amadeus rate limit exceeded
        if data is None or not data.get('data'):
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

        # Data from the first flight in the json
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        # Initialize FlightData with the first flight for comparison
        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

        # Iterate through all flights to find the cheapest one
        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            if price < lowest_price:
                lowest_price = price
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
                print(f"Lowest price to {destination} is £{lowest_price}")

        return cheapest_flight
