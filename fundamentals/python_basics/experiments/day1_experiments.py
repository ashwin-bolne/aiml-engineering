# Day 1 Experiments — Basic Python Flow


# 1. Variables
name = "Ashwin"
age = "24"   # intentionally string

print("Name:", name)
print("Age (before conversion):", age)


# 2. Type Conversion
age = int(age)

print("Age (after conversion):", age)
print("Type of age:", type(age))


# 3. Conditional Logic
if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")


# 4. Experiment (IMPORTANT)
# Change values and observe behavior

age = "twenty one"

print("\nTrying invalid conversion...")

try:
    age = int(age)
    print("Converted age:", age)
except ValueError:
    print("Error: Cannot convert string to integer.")



# 5. Functions 

def greet():
    print("Hello")

def greet_user(name):
    print(f"Hello, {name}")

greet()
greet_user("Ashwin")
greet_user("AI Engineer")


def add_numbers(num1, num2):
    return num1 + num2 

result = add_numbers(12, 43)
print(f"sum = {result}")

def is_adult(age):
    return age >= 18

print(is_adult(24))
print(is_adult(14))

def sqr(num):
    return num * num 

print(f"square of {14} = {sqr(14)}")