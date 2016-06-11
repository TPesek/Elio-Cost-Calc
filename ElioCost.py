

miles_til_death = 200000 #number of miles that each car is going to drive during its life span is 200,000


gas_price = 4 #price of gas is 4 dollars per gallon


def starting_cost(car_type):        #define starting cost
    if car_type == "elio":
        msrp = 7800
        return msrp
        print (msrp)                #output starting cost
    if car_type == "toyota":
        msrp = 4000
        return msrp
        print (msrp)
def miles_cost(car_type):           #define cost of miles
    if car_type == "elio":
        mpg = 83
        starting = 0               #starting miles is 0
    if car_type == "toyota":
        mpg = 41
        starting = 100000
    cost = ((miles_til_death - starting)/mpg)*gas_price
    return cost
    print (cost)                    #output cost


'''define cost of car for its entire life span. This means (cost of miles) plus (starting cost)'''

def total_cost(car_type):
    lifespan = miles_cost(car_type) + starting_cost(car_type)
    return int(lifespan)                 #output lifespan cost

'''print the results for both car models'''

print ("This program will compare two car models: one with incredible gas milage, \
and one with good gas milage.")
print ("     One is new, and the other is used.")
print ("We are trying to \
determine which is cheaper to own, given the gas milage and the starting price as")
print ("variables, and the cost of gas and total miles driven as constants.")
print ("")
input("press [enter] to continue")
print ("")

print ("The cost of buying a new \"Elio\" is $%s, \
and the cost of buying a 2004 \"Toyota Corolla\" with 100k miles \
is $%s." % (starting_cost("elio"), starting_cost("toyota")))
print ("")
input("press [enter] to continue")
print ("")

print ("If we assume that both cars will have 200k miles on them \
before they are too expensive to maintain, then the new Elio \
will be driven all 200k, and the Toyota--which started with 100k--\
will be driven an additional 100k.")
print ("")
input("press [enter] to continue")
print ("")

print ("Finally, realize that the Elio gets 83 mpg, and the Toyota gets 41 mpg.")
print ("Also, we are assuming 4 dollars per gallon of gas.")
print ("")
input("press [enter] to continue")
print ("")

print("So, the question is, which is cheaper to buy and own? The new gas-sipping Elio? \
or the stalwort Toyota Corolla?")
print ("")
input("press [enter] to continue")
print ("")

print("First, we find the cost gas for each respective number of miles driven.\
 For the Elio, this is $%i." % (miles_cost("elio")))
print ("For the Toyota, it turns out that this is only slightly more: $%i." % miles_cost("toyota"))
print ("")
print("Then, we add the original cost of the car to the cost of its gas. Can you guess which is more expensive?")
print ("")
input("press [enter] to see the RESULT")
print ("")

print ("RESULT: The Elio will end up costing $%i, and the \
Toyota will end up costing $%i." % (total_cost("elio"),total_cost("toyota")))
print("")
input(". . .")
print("")

print("You might notice that this program does not take into account \
the fact that we are driving 100k on one car and 200k on another! See \
my next program, ElioCostRevisited.py , for a more accurate comparison.")
print("Thank you for joining me in ElioCost.py! Buy safely.")
