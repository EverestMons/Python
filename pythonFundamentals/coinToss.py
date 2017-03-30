
import random

# print flip

def Cointoss(number):
    print "Starting the program..."
    tails = 0
    heads = 0
    for i in range(number+1):
        flip = random.randint(0,1)
        if(flip == 0):
            heads += 1
            print("Attempt #"+ str(i) +": Throwing a coin ... It's a head!... Got" + str(tails) + "head(s) so far and" + str(heads) + "tail(s) so far")

        else:
            tails +=1
            print("Attempt #"+ str(i) +": Throwing a coin ... It's a tail!... Got" + str(tails) + "head(s) so far and" + str(heads) + "tail(s) so far")
    print "Ending the program, thank you!"

x =Cointoss(10)
print x
