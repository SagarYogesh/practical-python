# bounce.py
#
# Exercise 1.5
drop_height = 100 # Meters

for i in range(10):
    bounce_height = round((3 * drop_height)/5, 4) # Meters
    print("Bounce height:", bounce_height)
    drop_height = bounce_height
