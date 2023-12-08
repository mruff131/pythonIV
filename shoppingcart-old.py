
def shoppingCart():
    """
    1) Takes in input
    2) Stores user input into a dictionary or list
    3) The User can add or delete items
    4) The User can see current shopping list
    5) The program Loops until user 'quits'
    6) Upon quiting the program, print out all items in the user's list
      """
    shoppingDict = {}
    nested_list = []
    print('----------------------------------')
    user_name = input("What's your name?\n")
    shoppingDict[user_name] = nested_list

    
    while True:
        print('Name:', user_name)
        print('Shopping Cart:', nested_list)
        print('----------------------------------')
        prompt_user = input('Do you want to "add" or "remove" an item from your shopping cart or "quit"?\n')
        

        if  prompt_user.lower() == "quit":
            print(shoppingDict)
            print('----------------------------------')
            break
        
        elif prompt_user.lower() == "add":
            add_item = input('What do you want to add?\n')
            nested_list.append(add_item.lower())
            print('----------------------------------')
            print(f'{add_item} was added to your cart.')
            print('----------------------------------')
            continue
            

        elif prompt_user.lower() == "remove":
            if len(nested_list) < 1:
                print('Sorry. There are no items in your cart to remove.')
                print('----------------------------------')
                continue

            else:
                delete_item = input('What do you want to remove from your shopping cart?\n')
                try:
                    nested_list.remove(delete_item.lower())
                    print(f'{delete_item} has been removed from your shopping cart.')
                    print('----------------------------------')
                    continue
                except:
                    print('***Item not found. Please type an item from your shopping cart and try again.***')
                    print('----------------------------------')
                    continue
        else:
            print('Invalid entry. Try again.')
            print('----------------------------------')
            continue


shoppingCart()