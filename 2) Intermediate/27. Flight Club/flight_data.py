class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

    def find_cheapest_flight(self, data):

        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", 0)

        first_flight = data['data'][0]
        lowest_price = float(first_flight['price']['grandTotal'])
        nr_stops = len(first_flight['itineraries'][0]['segments']) - 1
        origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
        destination = first_flight['itineraries'][0]['segments'][nr_stops]['arrival']['iataCode']
        out_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
        return_date = first_flight['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]

        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

        for flight in data['data']:
            price = float(first_flight['price']['grandTotal'])
            if price < lowest_price:
                lowest_price = float(first_flight['price']['grandTotal'])
                origin = flight['itineraries'][0]['segments'][0]['departure']['iataCode']
                destination = flight['itineraries'][0]['segments'][nr_stops]['arrival']['iataCode']
                out_date = flight['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
                return_date = flight['itineraries'][0]['segments'][0]['arrival']['at'].split('T')[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
                print(f"Lowest price to {destination} is £{lowest_price}")

        return cheapest_flight
