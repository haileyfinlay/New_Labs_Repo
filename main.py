import math
print("Hello World!")
print("Hello console!")
my_name = "Hailey"
work_from_home = "True"
side = 15
radius = 10
print(my_name)
print(work_from_home)
print(side)
print(radius)
print("My name is " + my_name)
print(f"The radius of the circle is {radius}")
wfh = "The length of each side of the square is "
print(wfh + str(side))
forecase = f"I work from home: {work_from_home}"
print(forecase)
square_area = side * side
square_perim = 4 * side
circle_area = math.pi * radius * radius
circle_perim = 2 * math.pi * radius
print(f"The square area is {square_area}")
print(square_perim)
print(circle_area)
print(circle_perim)

travel_options = ["foot","bike","car","airplane"]
opts = "The travel options are:"
print(opts)
print(f"1){travel_options[0]}")
print(f"1){travel_options[1]}")
print(f"1){travel_options[2]}")
print(f"1){travel_options[3]}")
travel_type = input("How would you like to travel? ")
print(f"Travel type: {travel_type}")
distance = 100
time = 0
cost = 0
if travel_type == "foot":
    print("Walking is free! Speed is 3pmh.")
    cost = 0
    time = distance / 3
elif travel_type == "bike":
    rent_bike = input("Do you need to rent the bike? (yes or no) ")
    if rent_bike == "yes":
        print("Bike rental is $45! Speed is 10mph")
        cost = 45
    else:
        print("Biking is free! Speed is 10mph.")
    cost = 0
    time = distance / 10
elif travel_type == "car":
    print("Driving is $0.25/mi. Speed is 60mph.")
    cost = 0.25 * distance
    time = distance / 60
elif travel_type == "airplane":
    passenger_count = int(input("How many passengers?"))
    print("Flying is $0.10/mi. Speed is 400mph")
    cost = 0.1*distance*passenger_count
    time = distance / 400
else:
    print(f"Sorry. {travel_type} is an invalid option")
print(f"Traveling {distance} miles by {travel_type} took {time} hours and cost ${cost}")
cost_bar = "Cost: "
for x in range(math.ceil(cost)):
    cost_bar += "$"
print(cost_bar)
time_bar = "Time: "
for y in range(math.ceil(time)):
    time_bar += "/"
print(time_bar)
