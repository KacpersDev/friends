print("Enter the number of friends joining (including you): ")
guests = int(input())
friends = dict()

def party():
    if guests <= 0:
        return print("No one is joining for the party")
    else:
        if guests > 0:
            print("")
            print("Enter the name of every friend (including you), each on a new line: ")
            for guests_value in range(guests):
                guests_value = input()
                friends[guests_value] = 0
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
    print(friends)