"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

"""
Another way Easy way to add stuff 
locations = {'North America': {'USA': ['Mountain View']}}
#locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}
"""

locations = {'North America': {'USA': ['Mountain View','Atlanta']},'Asia': {'India': ['Bangalore'],'Chaina': ['Shanghai']},'Africa':{'Egypt': ['Cairo']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.1
American City
American City
"""
print(*sorted(locations['North America']['USA']),sep ="\n")


"""2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:2
Asian City - Country
Asian City - Country"""

print(2)
lists = []
#here we took cities[0] as cities is a list and cities[0] is the string inside list
for country,cities in  locations['Asia'].items():
    append_list = cities[0] + "- "+ country
    lists.append(append_list)
    
sortedlist = sorted(lists)
for city in sortedlist:
    print(city)

