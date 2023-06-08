menu = ['coffee', 'matcha latte', 'earl grey', 'lemon meringue pie']

stock_dictionary = {'coffee': 25,
                    'matcha latte': 15,
                    'earl grey': 15,
                    'lemon meringue pie': 25
                    }


price_dictionary = {'coffee' : 2.5,
                    'matcha latte': 3.5,
                    'earl grey' : 2.0,
                    'lemon meringue pie' : 4.0,
                    }

print('Menu:')

print()

print(menu[0])
print(menu[1])
print(menu[2])
print(menu[3])

print()

# Saves stock for each item on menu in corresponding variables.
total_coffee = stock_dictionary['coffee'] * price_dictionary['coffee']
total_matcha = stock_dictionary['matcha latte'] * price_dictionary['matcha latte']
total_earl_grey = stock_dictionary['earl grey'] * price_dictionary['earl grey']
total_LMP = stock_dictionary['lemon meringue pie'] * price_dictionary['lemon meringue pie']

# While loop makes sure to keep asking the user questions and to input selections. Enables user to select from menu to see individual stock and also to see total cafe stock.
while True:
    menu_choice = input('Select item from menu to check it\'s stock OR type T to see Total cafe stock : \n').lower()
    if menu_choice == menu[0]:
        total_coffee = stock_dictionary['coffee'] * price_dictionary['coffee']
        print('Total stock of cofee is: ', total_coffee)
    if menu_choice == menu[1]:
        total_matcha = stock_dictionary['matcha latte'] * price_dictionary['matcha latte']
        print('Total stock of matcha latte is: ', total_matcha)
    if menu_choice == menu[2]:
        total_earl_grey = stock_dictionary['earl grey'] * price_dictionary['earl grey']
        print('Total stock of earl grey is: ', total_earl_grey)
    if menu_choice == menu[3]:
        total_LMP = stock_dictionary['lemon meringue pie'] * price_dictionary['lemon meringue pie']
        print('Total stock of cofee is: ', total_LMP)
    elif menu_choice == 't':
        total_cafe_stock = total_coffee + total_matcha + total_earl_grey + total_LMP
        print(total_cafe_stock)


# Below was my first attempt:
# I wanted to use a for loop to iterate through matching keys (coffee * coffee) but could not work out how to do it. 
# I managed to iterate through all the keys in dictionaries and display their calcualtions.
# But that is not useful here as we don't need to multiply coffee by tea etc.
# I have an upcoming 1 : 1 where I want to ask for help with this.

    # menu = ['coffee', 'matcha latte', 'earl grey', 'lemon meringue pie']

    # stock_dictionary = {'coffee': 25,
    #                     'matcha latte': 15,
    #                     'earl grey': 15,
    #                     'lemon meringue pie': 25
    #                     }


    # price_dictionary = {'coffee' : 2.5,
    #                     'matcha latte': 3.5,
    #                     'earl grey' : 2.0,
    #                     'lemon meringue pie' : 4.0,
    #                     }


    # for stock in stock_dictionary:
    #     stock_val = (stock_dictionary[stock])
    #     for price in price_dictionary:
    #             price_val = (price_dictionary[price])
    #             price_total_stock = print('{} * {} = {}'.format(stock_val, price_val, stock_val * price_val))
