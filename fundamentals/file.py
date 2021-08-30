num1 = 42 #variable declaration, initialize number
num2 = 2.3 #variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize array of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize object
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize array of strings
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value from tuple
pizza_toppings.append('Mushrooms') #log statement
print(person['name']) #log statement, access value from dictionary
person['name'] = 'George' #access value from dictionary, change value
person['eye_color'] = 'blue' #access value from dictionary, change value
print(fruit[2]) #log statement, access value from tuple

if num1 > 45: #conditional if
    print("It's greater") #log statment
else: #condition else
    print("It's lower") #log statement

if len(string) < 5: #conditional if, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #conditional else if, length check
    print("It's a long word!") #log statement
else: #conditional else
    print("Just right!") #log statement

for x in range(5): #for loop start (5)
    print(x) #log statement
for x in range(2,5): #for loop start (3)
    print(x)  #log statement
for x in range(2,10,3):  #for loop start (3)
    print(x)  #log statement
x = 0 #variable declaration, initialize number;
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #while increment

pizza_toppings.pop() #add value tuple
pizza_toppings.pop(1) #add value tuple

print(person) #log statement
person.pop('eye_color') #add value to dictionary
print(person) #log statement

for topping in pizza_toppings: #for loop start, length check
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break #for loop break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop start
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function declaration
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_times(4) #function call

def print_hello_x_or_ten_times(x = 10): #function declaration
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call


"""
Bonus section
"""

# print(num3)   NameError: name <variable name> is not defined
# num3 = 72     variable declaration, initialize number
# fruit[0] = 'cranberry'   change value
# print(person['favorite_team'])  KeyError: 'favorite_team'
# print(pizza_toppings[7])  IndexError: list index out of range
#   print(boolean) #log statement
# fruit.append('raspberry')  AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  add value