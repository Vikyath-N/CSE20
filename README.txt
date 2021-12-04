README file for MyOwnClass.py written by Vikyath Naradasi




Class Documentation:


The main purpose of the Parent Class “Airplane” is to set forward a list of common variables and attributes that an airplane can have. For example, the altitude, wings, plane size, and year variables can be commonly used for all types of aircraft and are not limited to a single generic aircraft.




The Parent class variables I used are:
windows: the number of windows as an int value
pilots: the number of pilots the aircraft has an int value






The CommericaialAirplane class variables I used are:
altitude: the plane’s altitude as an int value 
wings: the number of wings the aircraft has as an int value
plane_size: the size of the plane in meters as an int value 
year: the year the plane was built in as an int value




The ArmyJet class variables I used are:
range: the total number of kilometers the plane can fly in the air 


         The max_speed() method data variables I used are
mass: the mass of the airplane
gravity: gravity constant
area: surface area of the plane
drag: the drag force constant (average value)


The cost() method data variables I used are
color: the color of the airplane
manufacturer: the country of origin of the airplane
manu_cost: the cost of the plane per manufacturer
color_cost: the cost of the plane per color
final_cost: the final cost of the airplane using a custom formula in USD


The get_plane_size() and the get_altitude() methods are the two get-set methods that I used and these are for getting information about the altitude in terms of kilometers of where the airplane will be and the size of the plane in terms of meters in length from the cockpit all the way to the rudder. 


The max_speed() method finds the max speed or the terminal velocity of the aircraft by using the terminal velocity formula from: https://sciencing.com/maximum-value-polynomial-5792769.html. The method returns a string "The max speed is {max_velocity} m/s" and this is essential because one of the most important attributes for Army jets is how fast they are able to fly.




The cost() method finds the cost of the aircraft given two parameters “color” and “manufacturer”. Along with the three data variables, it runs a chain of if-else statements for the color and manufacturer by the country of origin and returns a formatted string of the final cost in USD. Got the associated costs from: https://www.forbes.com/sites/niallmccarthy/2016/08/16/the-hourly-cost-of-operating-the-u-s-militarys-fighter-fleet-infographic/?sh=54fed5ac685f




Demo Program Documentation:


In my demo program, the user uses the main(): function to edit and enter their parameters. The user can construct objects by calling the constructor and inputting parameters in the object. The Parent class and derived classes will then use these user-entered parameters to run the methods. These methods will return the method’s “return” statements, in my case the specified formatted string for that method. 


Instructions:
Use the 
Jet1 = ArmyJet("High", 13, 2019, 0)
        Je1_speed = Jet1.max_speed(80000, 10, 15, 0.00003)
In lines 89-91 inside of the main() method and input your own parameters*


*make sure the parameters are in the same type().