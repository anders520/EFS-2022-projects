wB = {'ardvark': 'aardvark', 'broter': 'brother', 'freind': 'friend', 'frist': 'first', 'crasy': 'crazy'}
keys = list(wB.keys())
values = list(wB.values())
def correct_typos():
    num = 0
    while True:
        if num < len(keys):
            print(keys[num])
        else: break
        answer = str(input("What's the correct word? "))
        if answer == "": break
        while answer != values[num]:
            answer = str(input("Wrong! Guess again... "))
            if answer == "":
                num = len(keys) * 2
                break
        else:
            print("Correct!")
            num += 1
        
