fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "apple":
        print("I don't like apple, skipping...")
        continue
    print("I like", fruit)

else:
    print("No more fruits left!")
