# bounce.py
#
# Exercise 1.5

height = 100
i = 0
while i < 10:
    meters = (height * 3) / 5
    height = meters
    i = i + 1
    
    print(i, ' ', round(meters, 4))
