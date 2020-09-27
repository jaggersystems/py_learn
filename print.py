from math import *

person_name = "Stefan"
person_age = 35.123
is_male = True

## Strings
print(person_name + " is " + person_age.__str__() + " years old")

future_age = person_age + 10

print("in 10 years\" he will be " + future_age.__str__())

print(person_name[0])

print("letter f is at index " + person_name.index("f").__str__())

print(person_name.replace("Stefan", "Moo"))

print(person_name)


## Numbers

print(3 + 4.5)

print(10 % 3) # modulus operator prints remaining amount

print("Age is now " + str(person_age))

print(abs(person_age)) ## absolute value

print(pow(3, 6))

print(min(5,6))

print(round(3.1))

print (floor(3.6)) # round down
print (ceil(3.6)) # round up
print (sqrt(4))


# name = input("Enter your name: ")
# print("Hello " + name + "!")

num1 = input("Enter a number : ")
num2 = input("Enter anothe1r number : ")
result = float(num1) + float(num2)

print(result)

