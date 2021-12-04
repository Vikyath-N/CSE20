# Vikyath Naradasi
# CSE 20
# Assignment 10.1: MyOwnClass
# This assignment uses inheritance and polymorphism to create my own custom class
# I choose to do a my Parent Class on Airplanes b/c I love Airplanes
# Got the terminal velocity formula from: https://sciencing.com/maximum-value-polynomial-5792769.html
# Parts and costs of a plane form: https://www.forbes.com/sites/niallmccarthy/2016/08/16/the-hourly-cost-of-operating-the-u-s-militarys-fighter-fleet-infographic/?sh=54fed5ac685f


class Airplane:
    #Parent Class declaration
    def __init__(self, altitude="", wings=0, plane_size=0, year=0):
    # Constructor method declaration and initializing parameters
        self.__altitude = altitude
        self.__wings = wings
        self.__plane_size = plane_size
        self.__year = year
        #Class variables declaration
    def get_plane_size(self):
        return self.__plane_size
        #first get-set method
        #returns the plane size value
    def get_altitude(self):
        return self.__altitude
        #second get-set method
        #returns the plane altitude value

class CommercialAirplane(Airplane):
    # CommercialAirplane is a class derived from the "Airplane" parent class
    def __init__(self, altitude, plane_size, windows = 0, pilots =0):
        # Constructor declaration and extending parameters for this class
        super().__init__(altitude=altitude, plane_size=plane_size)
        # super() key word to inherit all the methods from the parent class
        self.__windows = windows
        self.__pilots = pilots
        #new data variables for this class
    def __str__(self):
        return (f"Airplane info: Plane is {self.get_plane_size()} meters, has {self.__windows} plane windows, has {self.__pilots} pilots,  and is at {self.get_plane_size()} km above ground.")
    #retruns the formatted string of the 2 get-methods and one class variable

class ArmyJet(Airplane):
    # ArmyJet is a class derived from the "Airplane" parent class
    def __init__(self, altitude, plane_size, year, range=0):
        # Constructor declaration and extending parameters for this class
        super().__init__(altitude=altitude, plane_size=plane_size, year=year)
        # super() key word to inherit all the methods from the parent class
        self.__range = range
        # new data variables for this class
    def max_speed(self, mass, gravity, area, drag):
        #max speed method that takes in the four parameters
        self.__mass = mass
        self.__gravity = gravity
        self.__area = area
        self.__drag = drag
        max_velocity = int(((4*self.__mass*self.__gravity)/(self.__area*self.__drag))**0.5)
        #formula for the maximum (terminal) velocity
        return (f"The max speed is {max_velocity} m/s")
        #reterns a formatted string of the maximum velocity
    def cost(self, color, manufacturer):
        #cost method that takes in the two parameters
        self.__color = str(color)
        self.__manufacturer = str(manufacturer)

        #if-else statements for costs by manufacturer
        if self.__manufacturer == "USA":
            manu_cost = 20
        elif self.__manufacturer == "RUSSIA":
            manu_cost = 15
        else:
            manu_cost = 10

        # if-else statements for costs by color
        if self.__color == "RED":
            color_cost = 7
        elif self.__color == "YELLOW":
            color_cost = 3
        else:
            color_cost = 5

        #finla cost equation
        final_cost = color_cost * manu_cost
        return(f"The final plane cost is ${final_cost} million dollars")
        ##reterns a formatted string of the final cost

def main():
    #testing my code using main function
    #feel free to enter your own values
        #Plane1 = CommercialAirplane("High", plane_size=45, windows=90, pilots=2)
        Jet1 = ArmyJet("High", 13, 2019, 0)
        Je1_speed = Jet1.max_speed(80000, 10, 15, 0.00003)
        print(Je1_speed)
        # print(Plane1.get_plane_size())
        # print(str(Plane1))
        Jet2 = ArmyJet("High", 13, 2019, 0)
        Jet2_cost = Jet2.cost("RED", "USA")
        print(Jet2_cost)


if __name__ == "__main__":
    #main function declaration
    main()


