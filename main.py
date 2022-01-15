import random

print("Enter the number of friends joining (including you): ")
guests = int(input())
friends = dict()
guests_name = []

def party():
    if guests <= 0:
        print()
        return print("No one is joining for the party")
    else:
        if guests > 0:
            print("")
            print("Enter the name of every friend (including you), each on a new line: ")
            for guests_value in range(guests):
                guests_value = input()
                friends[guests_value] = 0
                guests_name.append(guests_value)
def lucky():
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = str(input())
    if answer == "No":
        print()
        return print("No one is going to be lucky")
    elif answer == "Yes":
        luck_number = guests - 1
        luck = random.randint(0, luck_number)
        print()
        print(f"{guests_name[luck]} is the lucky one!")

party()
if guests > 0:
    print()
    total = int(input("Enter the total bill value:"))
    per_user = round(total / guests, 2)
    for f in friends:
        if per_user % 2 == 0:
            round(per_user, 2)
            friends[f] = int(per_user)
        else:
            friends[f] = per_user
    print()
    lucky()
