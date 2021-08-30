x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#update values is dictionaries and lists
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y'] = 30

#iterate through a list of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary (students):
    for student in students:
        print(f"first name - {student['first_name']}, last_name - {student['last_name']}")
iterateDictionary(students) 

#Get Values from a List of Dictionaries
def iterateDictionary2 (key_name, some_list):
    for item in some_list:
        print(item[key_name])
iterateDictionary2 ("first_name", students)

#Iterate through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    keys=some_dict.keys()
    for key in keys:
        print(str(len(some_dict[key])), key.upper())
        for item in some_dict[key]:
            print(item)
        print()

printInfo(dojo)

