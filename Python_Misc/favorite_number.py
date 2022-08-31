def favorite_number():
    response = input("What's your favorite number? ")
    n = int(response)
    print("OK, so it is " + str(n))
    if n % 2 == 0:
        print("A nice even number! ")
    else:
        print("Well, that's odd (/ _ \)")
    print("Here is a question for you...")
    answer = input("What is " + str(n) + " mod 3? ")
    m = int(answer)
    if n % 3 == m: print("Correct!")
    else: print("No, its " + str(n%3))

favorite_number()
