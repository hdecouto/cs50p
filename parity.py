def main():
    x = int(input("what's x? "))
    if is_even(x)   :
        print("even")
    else:
        print("odd")    

def is_even(n):
    #not pythonic way
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # pythonic way but less preferred
    #return True if n % 2 == 0 else False

    #tighter pythonic way more preferred
    return n % 2 == 0

main()