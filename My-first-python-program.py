print("Labactivity-1")
print("Jancer D. Sagayo")
print("CITCS-1B")
print("==========================================================")
lbs = 400
print("Weight in pounds (lbs): ", end="")
print(lbs)
kg = lbs * 0.454
print("Weight converted to kilograms (kg): ", end="")
print(kg)
print("==================================================")
length = 23
print("Length in miles (mi): ", end="")
print(length)
km = length * 1.609344
print("Length in kilometers (km): ", end="")
print(km)
print("==================================================")
fahrenheit = 59.35
print("Temperature in fahrenheit (°F): ", end="")
print(fahrenheit)
celsius = (fahrenheit - 32) * 5/9
print("Temperature in celsius (°C): ", end="")
print(celsius)
print("=================================================")
student_ages = [20, 22, 23, 19, 21, 25, 18, 20, 24, 22]

average_age = sum(student_ages) / len(student_ages)

print("\nAges of 10 students:")
for index, age in enumerate(student_ages, start=1):
    print(f"Student {index}: {age} years old")

print(f"\nThe average age of the students is {average_age:.2f} years.")
print("===============================================================")
character1 = "Harley"
character2 = "Kentson"
character3 = "Dexter"
character4 = "Jomar"
character5 = "Daniel"
equipment = "magic sword"
item = "ancient amulet"
ability = "fire manipulation"

story = f"""
Once upon a time in the mystical land of Eldoria, there were five brave heroes: {character1}, {character2}, {character3}, {character4}, and {character5}. 
Each of them possessed unique abilities and wielded {equipment}s, their only hope against the dark forces threatening their world.

Their journey began in the quaint village of Lirendale, nestled at the edge of the Enchanted Forest. As fate would have it, a terrible curse had befallen the village, turning its inhabitants into stone statues. Desperate to save their home and loved ones, the heroes set forth.

Their first challenge was to navigate the treacherous depths of the Enchanted Forest, where trees whispered secrets and mythical creatures lurked in the shadows. With {character3}'s keen instincts, they safely emerged on the other side, but their trials had just begun.

In the desolate wastelands of the Dragon's Breath Desert, they encountered a tribe of nomadic Sand Dancers. With {character2}'s diplomatic skills, they formed an alliance and learned the location of the elusive {item}.

The heroes faced their greatest test in the heart of the Volcano Forge, a place where the very earth was molten with fiery rage. With {character5}'s {ability}, they traversed the inferno and reached the chamber of the ancient {item}. But it was guarded by the colossal lava golem, Ignarok.

A fierce battle ensued, and the heroes' determination and unity prevailed. They secured the {item}, unleashing its magic to break the curse upon Lirendale. The villagers were restored, and the land rejoiced in harmony.

As they triumphed over adversity, the heroes' bond grew stronger, and their names would forever be etched in the annals of Eldoria's history. And so, they continued their adventures, protecting their world from darkness and forging their legend as the saviors of Eldoria.
"""

print(story)