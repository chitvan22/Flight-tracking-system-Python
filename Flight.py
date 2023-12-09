from Airport import *                                                                                                               # import everything from Airport.py

class Flight:                                                                                                                       # staring flights class
   def __init__(self, flightNo, origAirport, destAirport):                                                                             # init method with flightNo, origAirport and destAirport as inputs
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):                                            # checking if origAirport and destAirport are Airport objects
            raise TypeError("The origin and destination must be Airport objects")                                                   # raising error if not

        elif not isinstance(flightNo, str) or len(flightNo) != 6 or not flightNo[:3].isalpha() or not flightNo[3:].isdigit():       # Checking if flightNo is in correct format
            raise TypeError("The flight number format is incorrect")                                                                # raising error if not

        else:                                                                                                                       # if no errors initialise variables
            self._flightNo = flightNo
            self._origin = origAirport
            self._destination = destAirport

   def __repr__(self):                                                                                                              # representing international and domestic flights in specific formats
        domestic = "domestic" if self.isDomesticFlight() else "international"                                                       # storing domestic or international in the variable domestic
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{domestic}]"                  # return the file with domestic or internation al phrase depending on the flight

   def __eq__(self, other):                                                                                                         # defining equal parameter
       if not isinstance(other, Flight):                                                                                            # comparing Flight and other object
           return False                                                                                                             # return false if they are not the same
       return self._origin == other._origin and self._destination == other._destination                                             # return true if origin and destinaton of the both the flights is the same

   def getFlightNumber(self):                                                                                                       # getter to get flight number
       return self._flightNo                                                                                                        # return flight number

   def getOrigin(self):                                                                                                             # getter to get origin of a flight
       return self._origin                                                                                                          # returns origin of a flight

   def getDestination(self):                                                                                                        # getter to get destination of a flight
       return self._destination                                                                                                     # returns destination of a flight

   def isDomesticFlight(self):                                                                                                      # method to check if a flight is domestic
       return self._origin.getCountry() == self._destination.getCountry()                                                           # return true if origin and destination country is the same

   def setOrigin(self, origin):                                                                                                     # setter to set origin
       if not isinstance(origin, Airport):                                                                                          # check if origin is airport object
           raise TypeError("The origin must be an Airport object")                                                                  # raise error if not
       self._origin = origin                                                                                                        # set self._origin as origin id the object is Airport object

   def setDestination(self, destination):                                                                                           # setter to set destination
       if not isinstance(destination, Airport):                                                                                     # check if destination is airport object
           raise TypeError("The destination must be an Airport object")                                                             # raise error if it is not
       self._destination = destination                                                                                              # set self_destination as destination if no errors