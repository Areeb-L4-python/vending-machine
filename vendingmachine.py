Menu = [
    { 
        'code':0,
        'item':'Water',
        'Price':2
    },
    {
        'code':1,
        'item':'coca cola',
        'Price':5
    },
    {
        'code':2,
        'item':'Chips',
        'Price':2
    },
    {
        'code':3,
        'item':'TikKat',
        'Price':4
    },
    {
        'code':4,
        'item':'Chocolate Milk',
        'Price':3
    },
    {
        'code':5,
        'item':'Snickers',
        'Price':6
    }
]
is_quit=True
while is_quit == False:
  # code
    
 print("Welcome to the vending machine")
for i in Menu:
    print(f"Item Name: {i['item']} - Price: {i['Price']} - code: {i['code']}")
    query = int(input("Enter the code number of the item you want to get: "))
    for i in Menu:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Great, {item['item']} will cost you {item['Price']} dollars")

        price = int(input(f"Enter {item['Price']} dollars to purchase: "))
        if price == item['Price']:
            print(f"Thank you for buying here is your {item['item']}")
        else:
            print(f"Please enter only {item['Price']} dollars")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')