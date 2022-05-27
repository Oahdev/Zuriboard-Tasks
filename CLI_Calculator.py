import re
print("CLI Calculator")
print("Type 'quit' to end")
status = True
result = 0
def calc():
    global status
    global result
    value = ""
    if result == 0:
        value = input("Enter your equation:")
    else:
        value = input(str(result))
    if value == "quit":
        status = False
        print("You stoped the calculator.")
    else:
        value = re.sub('[a-zA-Z,.:;{}()=]', "", value)
        if result == 0:
            result = eval(value)
        else:
            result = eval(str(result) + value)
        print("Last result:", result)
while status:
    calc()
