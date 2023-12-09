from Flight import *                                                                                                        # import everyhing from Flight.py
from Airport import *                                                                                                       # import everything from Airport.py

class Aviation:                                                                                                             # starting class Aviation
    def __init__(self):                                                                                                     # initialising class variables
       self._allAirports={}                                                                                                 # declaring _allAirports as a dictionary/set
       self._allFlights={}                                                                                                  # declaring _allFlights as a dictionary/set
       self._allCountries = {}                                                                                              # declaring _allCountries as a dictionary/set
    def getAllAirports(self):                                                                                               # getter to get _allAirports dictionary
       return self._allAirports                                                                                             # return _allAirports dictionary

    def getAllFlights(self):                                                                                                # getter to get _allflights dictionary
       return self._allFlights                                                                                              # returns _allFlights dictionary

    def getAllCountries(self):                                                                                              # getter to get _allCountries set
       return self._allCountries                                                                                            # returns a set containing all countries

    def setAllAirports(self, airports):                                                                                     # setter to set _allAirports
       self._allAirports = airports                                                                                         # set allirports set to the set provided

    def setAllFlights(self, flights):                                                                                       # setter to set all flights dictionary
       self._allFlights = flights                                                                                           # sets all flights set to the flights set provided

    def setAllCountries(self, countries):                                                                                   # setter to set _allCountries list
       self._allCountries = countries                                                                                       # sets _allCountries set to the set provided

    def loadData(self, airportFile, flightFile, countriesFile):                                                             # loads the text files provided into respective dictionaries/sets
        try:                                                                                                                # try except statement to open text files
            f = open(countriesFile, "r", encoding='utf8')                                                                   # opening first file in read only mode
            for line in f:                                                                                                  # loop to iterate over each line in the text file
                line = line.strip()                                                                                         # removing white spaces from the beginning and end of the line
                parts = line.split(",")                                                                                     # splitting line into elements at the commas
                self._allCountries[parts[0].strip()] = parts[1].strip()                                                     # setting _allcountries dictionaries with country as the key and continents as the value, while remocing white spaces from them at the beginning and the end
            f.close()                                                                                                       # closing the file

            f = open(airportFile, "r", encoding='utf8')                                                                     # opening second file in read only mode
            for line in f:                                                                                                  # for loop to iterate through each line
                line = line.strip()                                                                                         # remove white spaces from the front and end of the line
                parts = line.split(",")                                                                                     # creating list parts splitting the line at commas
                continent = self._allCountries[parts[1].strip()]                                                            # getting continent name from all countries dictionary
                ap = Airport(parts[0].strip(), parts[2].strip(), parts[1].strip(), continent)                               # creating ap as an Airport object
                self._allAirports[ap.getCode()]=ap                                                                          # setting up _allAirports dictionary with Code as key and ap as a value
            f.close()                                                                                                       # close the file

            for key in self._allAirports:                                                                                   # iterating over keys in the dictionary
                self._allFlights[key] = []                                                                                  # creating empty list associated with the key in dictionary _allFlights
            f = open(flightFile, "r", encoding='utf8')                                                                      # opening third file in read only mode
            for line in f:                                                                                                  # iterating over each line in the text file
                line = line.strip()                                                                                         # removing white spaces from the start and end of the line
                parts = line.split(",")                                                                                     # creating list parts; wplitting line into elements at commas
                orig = self._allAirports[parts[1].strip()]                                                                  # setting origin city;removing white space from start and end of the element
                dest = self._allAirports[parts[2].strip()]                                                                  # setting destination city;removing white space from start and end of the element
                fl = Flight(parts[0].strip(), orig, dest)                                                                   # creating Flight object
                self._allFlights[orig.getCode()].append(fl)                                                                 # adding flight object to list associated with the code of the airport in _allFlights dictionary
            f.close()                                                                                                       # close file

        except:                                                                                                             # except statement returning false if any error in above code
            return False                                                                                                    # return fals if there is problem in the code
        return True                                                                                                         # returns tru if the code executes without error

    def getAirportByCode(self, code):                                                                                       # method to get ariport name from airport code provided
        for airport in self._allAirports:                                                                                   # iteration through the airport codes(keys) in the dictionary _allAirports
            if airport == code:                                                                                             # if provided code matches the key
                return self._allAirports[airport]                                                                           # return list associated with the airport(key) in the dicionary ._allAirports
        return -1                                                                                                           # if none matches return -1

    def findAllCityFlights(self, city):                                                                                     # method to find all flights fro or to that city
        result = []                                                                                                         # creating empty list result
        for flightList in self._allFlights.values():                                                                        # iterating through values (list) in  _allFlights dictionary
            for flight in flightList:                                                                                       # looping through elements in the list of list (values)
                if city in (flight.getOrigin().getCity(), flight.getDestination().getCity()):                               # if provided city is found in origin or detination city associated with the flight
                    result.append(flight)                                                                                   # add flight to the results list
        return result                                                                                                       # returns result list

    def findFlightByNo(self, flightNo):                                                                                     # method to find flight by flight number
        for flightList in self._allFlights.values():                                                                        # looping through _allFlights dictionary values
            for flight in flightList:                                                                                       # values being list, iterating through the values of the list
                if flight.getFlightNumber() == flightNo:                                                                    # getting flight number of the value using getFlightNumber() method and comparing thet to flightNo
                    return flight                                                                                           # returning the list element(flight) if the flight number matches
        return -1                                                                                                           # return -1 if none of the flight Number matches match

    def findAllCountryFlights(self, country):                                                                               # method to find flight to and from a country
        result = []                                                                                                         # creating empty list to store values
        for flightList in self._allFlights.values():                                                                        # looping through _allFlights dictionary Values
            for flight in flightList:                                                                                       # looping through the elements of the list
                originCountry =  flight.getOrigin().getCountry()                                                            # using getOrigin and getCountry method to get originating country of the flight
                destinationCountry =  flight.getDestination().getCountry()                                                  # using getOrigin and getCountry method to get destination country of the flight
                if originCountry == country or destinationCountry == country:                                               # checking if origin or destination matches the given country
                    result.append(flight)                                                                                   # if matches append that flight to details to the result list
        return result                                                                                                       # return result list at the end of the loop

    def findFlightBetween(self, origAirport, destAirport):                                                                  # Method to find flight between two given airports
        for flight in self._allFlights.get(origAirport.getCode(), []):                                                      # Check for direct flight; matching origin airport with the elements in the list while loopng through the values
            if flight.getDestination() == destAirport:                                                                      # getting destination of the flight in the list and comparing with destination airport provided
                return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"     # returning direct flight if found; exit the method if found
        connecting_airports = set()                                                                                         # finding single hop flights
        for flight in self._allFlights.get(origAirport.getCode(), []):                                                      # finding elements(all ariports) with same origin airport
            for potential_connecting_flight in self._allFlights.get(flight.getDestination().getCode(), []):                 # looping through the list containing those flights
                if potential_connecting_flight.getDestination() == destAirport:                                             # if destination of the flight is same as required destination
                    connecting_airports.add(flight.getDestination().getCode())                                              # adding flight to the connecting_airtports set if a match found
        if len(connecting_airports) > 0:                                                                                    # checking if the set is not empty
            return connecting_airports                                                                                      # retuning the set
        else:                                                                                                               # if no connecting flight found
            return -1                                                                                                       # return negative

    def findReturnFlight(self, firstFlight):                                                                                # finding return flight
        for flightList in self._allFlights.values():                                                                        # looping through the list of lists in _allFlights
         for flight in flightList:                                                                                          # looping through the elements of the list
            if flight.getOrigin() == firstFlight.getDestination() and flight.getDestination() == firstFlight.getOrigin():   # comparing destination of given flight with origin of file in the loop and destination of flight in the loop with the given flight
                return flight                                                                                               # if both match, return the flight in the loop
        return -1                                                                                                           # negative if not flight matches
    def findFlightsAcross(self, ocean):                                                                                     # Method to find flights accross the given ocean
        greenZone = ["Canada", "United States", "Mexico", "Brazil", "Colombia"]                                             # creating a list of countries in Green zone
        blueZone= ["South Africa","Kenya","Libya","England","Portugal","France","Italy"]                                    # creating a list of countries in Blue zone
        redZone= ["China","India","South Korea","Philippines","Australia","Palestine","United Arab Emirates"]               # creating a list of countries in Red zone

        flightsAcross = set()                                                                                               # creating empty set to store flights
        if ocean == "Atlantic":                                                                                             # checking if provided ocean is Atlantic
            for flights in self._allFlights.values():                                                                       # looping through list of lists linked with values in _allFlights
               for flight in flights:                                                                                       # looping through elements in the list flights
                if flight.getOrigin().getCountry() in greenZone and flight.getDestination().getCountry() in blueZone:       # if flights origin country is in green zone and destination country is in blue zone
                    flightsAcross.add(flight.getFlightNumber())                                                             # add flight Number to flightsAcross set
                elif flight.getDestination().getCountry() in greenZone and flight.getOrigin().getCountry() in blueZone:     # if flights destination country is in green zone and origin country is in blue zone
                    flightsAcross.add(flight.getFlightNumber())                                                             # add flight number to the set flightsAcross
        elif ocean == "Pacific":                                                                                            # if ocean is pacific
            for flights in self._allFlights.values():                                                                       # looping through list of lists linked with values in _allFlights
              for flight in flights:                                                                                        # looping through elements in the list flights
                if flight.getOrigin().getCountry() in greenZone and flight.getDestination().getCountry() in redZone:        # if flights origin country is in green zone and destination country is in red zone
                    flightsAcross.add(flight.getFlightNumber())                                                             # add flight number to the set flightsAcross
                elif flight.getDestination().getCountry() in greenZone and flight.getOrigin().getCountry() in redZone:      # if flights destination country is in green zone and origin country is in red zone
                    flightsAcross.add(flight.getFlightNumber())                                                             # add flight number to the set flightsAcross
        if len(flightsAcross)!=0:                                                                                           # checking if flightsAcross is not an empty set
            return flightsAcross                                                                                            # return flightsAcross set
        else:                                                                                                               # if the set is empty
            return -1                                                                                                       # return negative