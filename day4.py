names = []

while True:
    value = input("Enter names (or stop): ")
    if value.lower == "stop":
        break
    names.append(value)

print(names)

print("Total names entered: ", len(names))

if len(names) >= 2:
    names[1] = "Shwethaaaaaaaaa"

else:
    print("Not enough names to replace the second item")