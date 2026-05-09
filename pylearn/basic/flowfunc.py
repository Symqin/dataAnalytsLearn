# if else elif

age = 18

if age < 18:
    print("you are a child")
elif age == 18:
    print("you are a teenager")
else:
    print("you are a senior")


# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break  # exit the loop when i is 5
    print(i)
    
    if i % 2 == 0:
        continue  # skip the rest of the loop for even numbers
    print(i)

    if i in range(10):
        pass  # do nothing, just a placeholder

# functions

def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!


#default parameter
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())  # Output: Hello, Guest!
print(greet("Bob"))  # Output: Hello, Bob!

#lambda function

square = lambda x: x ** 2
print(square(5))  # Output: 25
