#task1 

a = 67                       #integer 
b = "string value"           #string 
c = 8.99                     #float/decimalval
d = True                     #booloean 

print(type(a)) #int 
print(type(b)) #str
print(type(c)) #float
print(type(d)) #bool  

print(a) # 67
print(b) # string value
print(c) # 8.99
print(d) # True


#task2  

def check_even_odd(num):
    if num % 2 ==0: # it'll check num is odd o even
        print("even") # gonna execute if num is even
    else:
        print("odd") # if number is odd


check_even_odd(55) 


#task3/4
# list numbers 
list = [1,2,3,0,4,5,-8,0,6,-11,77] 

# loop through each value in list to check +ve 0 -ve
for i in list:
    if i > 0:
        print("+ve") 
    elif i == 0:
        print("val==0") 
    else:
        print("-ve")  

#task5 
#main func to find out factorial of given func
def factorial(x):
    a = 1 
    while x > 0:
        a *= x 
        x = x - 1 
    return a  

zx = int(input("enter numbr : ")) 
r = factorial(zx) 
print(f"factorial of {zx} is {r}") 

#------------------------------------assignment2---------------------------------------- 
#task1
bool1 = bool(input("enter 1st bool :")) # first boolean value
bool2 = bool(input("enter 2nd bool : ")) # second boolean value 
print(bool1 and bool2) # true
print(bool1 or bool2) # tue
print( not bool1) #false 
print(not bool2) #false 

#task2 
#taking input of two types values float and integer
number = int(input("enter number:")) 
floatvalue = float(input("enter float value : "))
print(f"addition {number+floatvalue}")
print(f"sub {number-floatvalue}") 
print(f"div {number/floatvalue}")
print(f"mul {number*floatvalue}") 

#task3 
string = "python" 
low = string.lower() #for lower
up = string.upper() #for upper 
if string == "python":
    print("yes") 
else:
    print("no")

print(len(string)) # 6

# for doing joining( concatenation) in tupple
tuple1=('red','yellow','green')
tuple2=('1','2','3')
tuple3=tuple1+tuple2
print(tuple3)  

car = {
"brand": "Ford"
,"model": "Mustang",
"year": 2020}
x = car.values()
print(x)
#before the change
car["year"] = 2024
print(x)
car["year"] = 2025
print(x)
print("Yes, 'model' is one of the keys in the  dictionary")

dictionary={
"brand": "Ford",
"model": "Mustang",
"year": 2023}
dictionary["model"]
print(dictionary)
dictionary = {
"brand": "Ford",
"model": "Mustang",
"year": 2026}
mydict=dictionary.copy()
print(mydict)


#split
spl="HELLO,WORLD"
xdd=spl.split(",")
print(xdd)    


#replace
cff="HI,BROTHER"
print(cff.replace("E","J")) 



  



    




  



