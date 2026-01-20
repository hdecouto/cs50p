# ask user for their name
#name = input("what's your name? ").strip().title()
"""
say hello to the user
"""
# remove any leading or trailing whitespace from the name and capitalize
#name = name.strip().title()
# capitalize the first letter of the name
#name = name.capitalize()
# titelize the name (capitalize first letter of each word)
#name = name.title()
#split the name into parts and capitalize each part
#first,last = name.split()

# print a greeting message
#print(f"hello,{first}")

#from py_compile import main


def main():  
    name = input("what's your name? ")
    hello()
#print(name)

def hello(to="world"):  # hello is a custom function that takes one parameter 'to'
    print(f"hello, {to}")

main()