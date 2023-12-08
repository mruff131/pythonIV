class ShopingCart():
   
    def __init__(self):
        self.shopping_list = []
       

    def add_item(self):
        add_input = input('What would you like to add?')
        self.shopping_list.append(add_input.lower())
        print(f'You added {add_input} to your shopping cart.')
        print('----------------------------------')
    
    def remove_item(self):
        remove_input = input('What would you like to remove?')
        if remove_input.lower() in self.shopping_list:
            self.shopping_list.remove(remove_input.lower())
            print(f'You removed {remove_input} from your shopping cart.')
            print('----------------------------------')
        else:
            print(remove_input,'is not in shopping cart')
         

    def view_items(self):
        print(self.shopping_list)

your_cart = ShopingCart()
# your_cart.add_item()
# your_cart.remove_item('hotdogg')
# your_cart.view_items()    
    

def run():
    while True:
        prompt_user = input('Do you want to "add", "remove", "view" an item from your shopping cart or "quit"?\n')
        if prompt_user.lower() == "add":
            your_cart.add_item()

        elif prompt_user.lower() == "remove":
            your_cart.remove_item()
        
        elif prompt_user.lower() == "view":
           your_cart.view_items()
        
        elif prompt_user.lower() == "quit":
            print('----------------------------------')
            print("Thanks for shopping!")
            print('----------------------------------')
            break
        
        else:
            print('Invalid input, try again.')
            print('----------------------------------')

run()

    

