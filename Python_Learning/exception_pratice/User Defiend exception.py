class Under_age(Exception):     #user defiens exception
    pass
age=17
if age<18:
    raise Under_age('Can not cast the vote')     #Under_age is user defiend exception
else:
    print("Eliglible to caste tehe vote")

