from obstruction_class import is_impenetrable 
"""importing the function is_impenetrable from obstruction_class.py"""

# simulated data
speed = 10 
""" speed in miles per hour """

distance = 15
"""distance in miles"""

location_b = distance / speed * 60
""" Expected time in minutes (converted from hours) """

location_a = 78
""" Simulated actual time in minutes """

if is_impenetrable(location_b, location_a):
    """
    if the explorers are late, print "There is an impenetrable obstruction!"
    if the explorers are on time, print "There is no impenetrable obstruction!"

    """
    print("There is an impenetrable obstruction!")
else:
    print("There is no impenetrable obstruction!")
