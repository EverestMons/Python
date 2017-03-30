x = range(60, 101)
import random
y = random.sample(x,10)


def Score(list):
    for grade in list:
        if grade < 70:
            print "Score: ", grade, "; Your grade is D"
        if grade > 69 and grade < 80:
            print "Score: ", grade, "; Your grade is C"
        if grade > 79 and grade < 90:
            print "Score: ", grade, "; Your grade is B"
        if grade > 89 and grade <= 100:
            print "Score: ", grade, "; Your grade is A"


print Score(y)
