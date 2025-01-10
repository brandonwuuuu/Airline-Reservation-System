# Airline-Reservation-System
A system that enables users to efficiently manage and access their flight details. It provides essential information such as flight origin, destination, seat assignments, and departure schedules. Users can view their purchased tickets, explore associated flight numbers, and access details about the aircraft involved.

ENTITIES:

CLASS: Defines types of flight classes (e.g., Economy, Business) with a priority_level indicating
boarding or service priority.

AIRLINE: Stores details about airlines, including their name, country, website, and contact
phone number.

FLIGHT: Contains information about individual flights, such as flight number, destination, origin,
associated airline, and departure/arrival times.

FLIGHT_CLASS: Associates flights with specific classes (e.g., Economy, Business), storing
fare details for each class on a given flight.

AIRCRAFT_TYPE: Represents different types of aircraft, identified by a model number and
manufacturer.

AIRPORT: Contains information about airports, including their code, name, city, province/state,
and country.

PASSENGER: Holds details of passengers, including personal identification like passport
number and contact information.

USER: Links passengers to user accounts with a unique ID and password for system access.

TICKET: Represents a flight ticket, associating passengers, flights, and flight classes.

FLIGHT_AIRCRAFT: Links flights with the specific aircraft type used for operation.

FLIGHT_AIRPORT: Maps flights to the airports they are associated with, either as origin or
destination


Instructions on how to run interface:
 1. Gointo the directory containing the templates folder, database and airlineApp.py in
 command prompt
 2. Type in pip install flask and enter
 3. Type in pip install db-sqlite3 and enter
 4. Type in python airlineApp.py and click on the link provided (http://127.0.0.1:5000/)
 5. Navigate through the interface by selecting a ticket or search a flight
