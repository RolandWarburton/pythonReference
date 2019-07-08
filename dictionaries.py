dictionary = {"roland": 1, "rinne": 2, "adam": 3}
print(dictionary["roland"])

numbers = {
    1: "onee",
    2: "twoo",
    3: "threee"
}
# search a list and return TRUE or FALSE
print(1 in numbers)

# search and return a custom error
print(numbers.get(1, "error, key not found"))
