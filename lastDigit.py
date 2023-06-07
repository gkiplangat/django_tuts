#import random
import random

#declare variables
number = random.randint(-10000, 10000)
last_digit = 0
message = 0;

#Check for the last digit
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10


#condition for the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "is zero"
else:
    message = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number,last_digit, message))
