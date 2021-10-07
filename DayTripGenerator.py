import random


destinations = ["Disney World", "Oktoberfest", "Crawfish Festival", "Mawmaw's House"]
restaurants = ["Applebee's", "Schnitzel Emporium", "Pizza Hut", "Sullivan's"]
transportation = ['Car', 'Bicycle', '4-wheeler', 'Yee Yee Truck']
entertainment = ['Miley Cyrus Concert', 'Chainsaw Juggler', 'Sock Manufacturing Tour', 'Mud-riding']
day_trip = []
satisfaction = ''


def indecisive_trip (x):
    random_trip = random.choice(x)
    print (random_trip)
    return (random_trip)

def begin (p):
    print("Welcome to the RNGeezus Trip Generator. This will help you find something to do for the day since you have no ideas.")
    print ("Below, you will see your selections for the day.  If you do not like any of these suggestions, you may have them produced again.")
    day_trip.append (indecisive_trip(destinations))
    day_trip.append (indecisive_trip(restaurants))
    day_trip.append (indecisive_trip(transportation))
    day_trip.append (indecisive_trip(entertainment))


def satisfaction (h):
    satisfaction = input ('Please type y if you are satisfied or n if you are not')
    return (satisfaction)

def choose_again (q):
     if satisfaction == ('y'):
         print('We are glad you are satisfied with your selection. Please have a pleasant trip and remember to wear your seatbelt.')
     if satisfaction == ('n'):
         unsatisfied = (input('Please select the option you would like to change: 1:destination, 2:restaurant, 3:transportation, or 4:entertainment '))

         if unsatisfied == ('1'):
             day_trip.pop(0)
             day_trip.insert(0, indecisive_trip(destinations))
            
         elif unsatisfied == ('2'):
             day_trip.pop(1)
             day_trip.insert(1, indecisive_trip(restaurants))
             
            
         elif unsatisfied == ('3'):
             day_trip.pop(2)
             day_trip.insert(2, indecisive_trip(transportation))
             
            
         elif unsatisfied == ('4'):
             day_trip.pop(3)
             day_trip.insert(3, indecisive_trip(entertainment))
             
     return day_trip    

begin(indecisive_trip)

while satisfaction != ('y'):
    #begin(indecisive_trip)
    choose_again(indecisive_trip)
    satisfaction = input ('Please type y if you are satisfied or n if you are not')
    #if satisfaction == ('y'):
print ('Here is your randomly generated day trip:')
print (day_trip)
print ("Thank you for using the RNGeezus Trip Generator.  Enjoy your day away! ")






