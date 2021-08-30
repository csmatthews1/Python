#Basic
for x in range(151):
    print(x)

#Mulitiples of Five
for x in range(5,1005,5):
    print(x)

#Counting, the Dojo Way
for x in range(1,101):
    if(x%5 == 0):
        if(x%2 == 0):
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(x);

#Whoa. That Sucker's Huge
sum = 0;
for x in range(1,500000,2):
    sum += x
print(f"Sum of odds between 1 and 500,000: {sum}")

# #Countdown by Fours
for x in range (2018,0,-4):
    print(x)

#Flexible Counter
lowNum = 2
highNum = 25
mult = 3
for x in range(lowNum,highNum+1):
    if (x%mult==0):
        print(x)