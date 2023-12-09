class Airport:                                                          # creating class
    def __init__(self, code, city, country, continent):                 # __init__ method start
        self._code = code                                               # initialising variables
        self._city = city
        self._country = country
        self._continent = continent

    def __repr__(self):                                                 # method for representation of flight
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self):                                                  # getter method to get flight code
        return self._code

    def getCity(self):                                                  # getter method to get city
        return self._city

    def getCountry(self):                                               # getter method to get country
        return self._country

    def getContinent(self):                                             # getter method to get continent
        return self._continent

    def setCity(self, city):                                            # setter to set city
        self._city = city

    def setCountry(self, country):                                      # setter to set country
        self._country = country

    def setContinent(self, continent):                                  # setter to set continent
        self._continent = continent