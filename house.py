name = input("What is your name? ")

# if name == "harry" or name == "hermione" or name == "ron":
#     print("Gryffindor")

# elif name == "draco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:             # handles all other cases
        print("Who?")