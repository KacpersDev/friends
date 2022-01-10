
# Created on 10/01/2020

# Author - KacpersDev

print("Enter the number of friends joining (including you) : ")
guests = int(input())
value = {"test": 0}

def update(value, people):
    a = {f'{people}': 0}
    return value.update(a)
def party():
    if guests <= 0:
        return print("No one is joining for the party")
    else:
        if guests > 0:
            print("Enter the name of every friend (including you), each on a new line: ")
            value.pop('test')
            for guests_value in range(guests):
                guests_value = input()
                update(value, guests_value)
party()
if guests > 0:
    print(value)
