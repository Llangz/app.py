# Three main data structures
# tuple, list, dictionary

months = ('Jan', 'Feb', 'March', 'April', 'May', 'June') #tuple
names = ['John','Mary', 'Mike', 'Miry', 'Hellen', 'Hilda'] #list

person = {'names' : 'Mary Mwangi', "age" :23, 'height' : 2.1, 'gender': 'F'} #dictionary

# access data
print(months [0])
print(months [1])
print(months)

for month in months:
    print(month)

print("-------------------------------------")
print(names [0])
print(names)

for name in names:
    print(name)

print("--------------------------------------")

print(person [ 'names' ])
print(person [ 'age' ])
print(person [ 'gender' ])
print(person [ 'height' ])


print("-------------------------------------")

for key, value in person.items():
    print(key, value)

# adding data
# tupple == immutable object

# list
names.append("Kim")
names.append("Joan")
print(names)

# list
person ["weight"] = 76
person ["color"] = "Black"
print(person)

# removing from
print("--------------------------------------")
names.remove("John")
person.pop('names')
print(names)
print(person)

# clearing
print("-------------------------")
names.clear()
person.clear()

print(names)
print(person)

print("---------------------------")
people = [{"name":"Erika Tschierse","age":49},{"name":"Cathy Winnett","age":12},{"name":"Adelice Ansett","age":25},{"name":"Maybelle Bourton","age":30},{"name":"Bryce Nibley","age":61},{"name":"Rubetta Graybeal","age":61},{"name":"Micheal Engley","age":29},{"name":"Lillis Chisnell","age":12},{"name":"Andre Whebell","age":47},{"name":"Demetrius Heakins","age":20},{"name":"Lucienne Griffe","age":30},{"name":"Jackqueline Gatteridge","age":39},{"name":"Corabel Marriott","age":39},{"name":"Dolores Mungan","age":47},{"name":"Granny Lerwill","age":60},{"name":"Layney Kobsch","age":27},{"name":"Quinton McLoughlin","age":45},{"name":"Cordula Riche","age":22},{"name":"Gradeigh Deller","age":43},{"name":"Skip Connachan","age":65},{"name":"Wendell Daintree","age":33},{"name":"Fleurette Clutten","age":39},{"name":"Sharona Shillaker","age":27},{"name":"Clark Vedstra","age":26},{"name":"Penni Jakucewicz","age":17},{"name":"Elsie Chugg","age":42},{"name":"Randene Meriott","age":34},{"name":"Avis Chattock","age":19},{"name":"Bartholomeo Mac Giany","age":16},{"name":"Nobe Dalrymple","age":70},{"name":"Jania Parmer","age":20},{"name":"Evvie Balderstone","age":62},{"name":"Bernardina Belleny","age":62},{"name":"Millisent Capelow","age":14},{"name":"Codie Statersfield","age":42},{"name":"Cissiee Kunze","age":36},{"name":"Basilius Eddisford","age":20},{"name":"Zachariah Sterte","age":37},{"name":"Roanne Buckell","age":24},{"name":"Broderick Everex","age":57},{"name":"Harriott Feragh","age":16},{"name":"Jo-ann Ayliff","age":46},{"name":"Codi Diwell","age":64},{"name":"Marcie Lidgett","age":58},{"name":"Zaria Lardeux","age":66},{"name":"D'arcy Drezzer","age":54},{"name":"Bernard Lowey","age":55},{"name":"Sande Frunks","age":68},{"name":"Hagen Mighele","age":43},{"name":"Trude Avann","age":40},{"name":"Velma Iacovino","age":38},{"name":"Stevana Dingsdale","age":43},{"name":"Cammy Baxstare","age":53},{"name":"Sibyl Sheering","age":69},{"name":"Ahmad Berthod","age":13},{"name":"Shawn Scrimshire","age":17},{"name":"Meriel Michel","age":45},{"name":"Trista Kobpal","age":24},{"name":"Laird Roalfe","age":27},{"name":"Rancell Headan","age":37},{"name":"Abbe Sykora","age":51},{"name":"Scotti Grimsley","age":42},{"name":"Elfreda Branscomb","age":36},{"name":"Artur Schermick","age":65},{"name":"Gasper Dafydd","age":22},{"name":"Dorena Bonifas","age":62},{"name":"Halsey Emlen","age":54},{"name":"Bobine Mcmanaman","age":53},{"name":"Jameson Hackinge","age":27},{"name":"Hansiain Lovelady","age":59},{"name":"Vincenz Van Leeuwen","age":12},{"name":"Olivette Bridge","age":32},{"name":"Trent Newsome","age":64},{"name":"Frederica Kohen","age":14},{"name":"Les Everard","age":64},{"name":"Maurene Malletratt","age":69},{"name":"Lonna Rickersey","age":69},{"name":"Nessie Ander","age":70},{"name":"Carney Crose","age":41},{"name":"Tobye Kingham","age":38},{"name":"Isadore Hazeldene","age":58},{"name":"Teena Sach","age":29},{"name":"Jaclin Duggon","age":34},{"name":"Maurizio Baddiley","age":55},{"name":"Sol Domel","age":67},{"name":"Byram Doucette","age":32},{"name":"Birgitta Pleasaunce","age":49},{"name":"Mort Eldered","age":29},{"name":"Leontine Bodemeaid","age":45},{"name":"Frasier Comelli","age":65},{"name":"Laverna Samet","age":17},{"name":"Courtney Weekes","age":51},{"name":"Brigitta Fabbri","age":39},{"name":"Gerda Allans","age":25},{"name":"Lisetta Bert","age":25},{"name":"Andree Toffolo","age":39},{"name":"Mandie Hopewell","age":55},{"name":"Gerry Zellick","age":61},{"name":"Sampson Shovell","age":14},{"name":"Whitman Eva","age":52}]

p1 = people [0]
print(p1 ["name"], p1 ["age"])

total = 0
for p in people:
    total += p["age"]
    print(p ["name"])

print(total / len(people))
print(total)

print("-----------------------------------")

print(people)

from operator import itemgetter

sorted_list = sorted(people, key=itemgetter("age"), reverse=True)
print(sorted_list)
print("--------------------------------------------------------")

for user in sorted_list:
    print(user["name"] , user["age"])


