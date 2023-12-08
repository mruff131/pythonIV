

class StringConversion():
    '''
    Exercise 2 - Write a Python class which has two methods get_String 
    and print_String. get_String accept a string from the user 
    and print_String print the string in upper case
    '''


    def get_String(self):
        self.user_string = input('Type your string: ')


    def print_String(self):
        print(self.user_string.upper())


my_String = StringConversion()
my_String.get_String()
my_String.print_String()
