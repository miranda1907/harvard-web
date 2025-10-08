people = [
    {"name": "Harry", "house": "Griff"},
    {"name": "Ron", "house": "Griff"},
    {"name": "Herm", "house": "griff"}
]

#def f(person):
   # return person["name"]
#people.sort(key=f)

people.sort(key= lambda person:person["name"])
print(people)