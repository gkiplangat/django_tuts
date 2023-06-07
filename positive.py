import random
number = random.randint(-10, 10)
message = 0;
if number > 0:
    message = "is positive"
elif number == 0:
    message = "is zero"
else:
    message = "is negative"
print("{} {}".format(number, message))
