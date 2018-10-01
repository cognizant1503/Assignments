#PF-Assgn-29
def calculate(distance,no_of_passengers):
    bus_cost = 70*distance/10
    bus_sell = 80 * no_of_passengers
    if(bus_cost<bus_sell):
        return bus_sell - bus_cost
    elif(bus_cost>bus_sell):
        return -1



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))