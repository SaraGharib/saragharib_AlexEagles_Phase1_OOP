class Airport:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Airline:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_id, airline, departure, arrival, price, time):
        self.flight_id = flight_id
        self.airline = airline
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.time = time

    def __str__(self):
        return (f"Flight {self.flight_id} by {self.airline.name} from {self.departure} "
                f"to {self.arrival} at {self.time} - ${self.price}")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Booking:
    def __init__(self, customer, flight, meal_option=None, services=None):
        self.customer = customer
        self.flight = flight
        self.meal_option = meal_option
        self.services = services if services else []

    def __str__(self):
        services_str = ', '.join(self.services) if self.services else 'None'
        return (f"Booking for {self.customer.name} ({self.customer.email}):\n"
                f"{self.flight}\nMeal: {self.meal_option if self.meal_option else 'None'}\n"
                f"Services: {services_str}")


class FlightBookingSystem:
    def __init__(self):
        self.flights = []
        self.meal_options = {
            "1": "Meal1",
            "2": "Meal2",
            "3": "Meal3",
            "4": "Meal4"
        }
        self.services = {
            "1": "Extra Baggage - $50",
            "2": "Priority Boarding - $30",
            "3": "In-Flight WiFi - $20",
            "4": "Travel Insurance - $100"
        }

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, departure, arrival, criteria=None):
        # Normalize case and strip whitespace
        departure = departure.strip().lower()
        arrival = arrival.strip().lower()
        flights = [f for f in self.flights if
                   f.departure.strip().lower() == departure and f.arrival.strip().lower() == arrival]
        if criteria:
            flights.sort(key=criteria)
        return flights

    def book_flight(self, customer, flight, meal_option=None, services=None):
        return Booking(customer, flight, meal_option, services)


def main():
    system = FlightBookingSystem()

    # Initialize airports
    hba = Airport("Borg AlArab")
    lxr = Airport("Luxor")
    cai = Airport("Cairo")
    ssh = Airport("Sharm El Sheikh")

    # Initialize an airline
    egyptair = Airline("EgyptAir")

    # Initialize available flights
    flight1 = Flight(101, egyptair, hba.name, cai.name, 500, "10:00 AM")
    flight2 = Flight(102, egyptair, cai.name, lxr.name, 600, "12:00 PM")
    flight3 = Flight(103, egyptair, cai.name, lxr.name, 450, "02:00 PM")
    flight4 = Flight(104, egyptair, hba.name, ssh.name, 400, "03:00 PM")
    flight5 = Flight(105, egyptair, ssh.name, cai.name, 550, "05:00 PM")

    # Add flights to the system
    system.add_flight(flight1)
    system.add_flight(flight2)
    system.add_flight(flight3)
    system.add_flight(flight4)
    system.add_flight(flight5)

    print("Welcome!!")

    # Enter customer information
    customer_name = input("Enter your name: ")
    customer_email = input("Enter your email: ")
    customer = Customer(customer_name, customer_email)

    # Print all available flights
    print("\nAvailable Flights:")
    for i, flight in enumerate(system.flights):
        print(f"{i + 1}. {flight}")

    # Search for flights
    departure = input("\nEnter departure airport: ").strip().lower()
    arrival = input("Enter arrival airport: ").strip().lower()
    criteria = input("Sort by (price/time): ")

    flights = system.search_flights(departure, arrival,
                                    lambda f: f.price if criteria == "price" else f.time)
    if flights:
        print("\nFiltered Available Flights:")
        for i, flight in enumerate(flights):
            print(f"{i + 1}. {flight}")
        flight_choice = int(input("Select a flight (number): ")) - 1
        flight = flights[flight_choice]

        # Choose meal option
        print("\nAvailable Meal Options:")
        for key, meal in system.meal_options.items():
            print(f"{key}. {meal}")
        meal_choice = input("Select a meal option (number): ")
        meal_option = system.meal_options.get(meal_choice, None)

        # Choose additional services
        print("\nAvailable Additional Services:")
        for key, service in system.services.items():
            print(f"{key}. {service}")
        service_choices = input("Select additional services (comma-separated numbers, or leave blank): ").split(", ")
        services = [system.services.get(choice.strip(), None) for choice in service_choices if choice.strip()]

        # Book the flight
        booking = system.book_flight(customer, flight, meal_option, services)
        print(f"\nBooking successful:\n{booking}")
    else:
        print("No flights available for the selected route.")


if __name__ == "__main__":
    main()
