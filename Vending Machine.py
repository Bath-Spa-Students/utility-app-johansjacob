from prettytable import PrettyTable


y='price'

# Vending machine items and prices



A01 = {"A01": "Oman Chips", y: 1.00}
A02 = {"A02": "Sohar Chips", y: 1.00}
A03 = {"A03": "Lays Chips", y: 2.50}
A04 = {"A04": "Pringles Chips", y: 2.50}

B01 = {"B01": "Kinder bueno", y: 5.00,}
B02 = {"B02": "KitKat", y: 3.00}
B03 = {"B03": "Galaxy smooth milk", y: 4.50,}
B04 = {"B04": "Ferrero Rocher", y: 6.00}

C01 = {"C01": "7up", y: 2.50,}
C02 = {"C02": "Pepsi", y: 2.50,}
C03 = {"C03": "Fanta",y: 2.50,}
C04 = {"C05": "Miranda", y: 2.50}

x=[A01,A02,A03,A04,B01,B02,B03,B04,C01,C02,C03,C04]
#SUGGESTED PAIR WHEN BUYING A PRODUCT
item_pairs = {
    "A01": ["Lays Max"],  # Mountain Dew pairs with Lays Max.
    "A02": ["Cheetos flamin Hot"],  # Thumbs Up pairs with Cheetos Flaming Hot
    "A03": [],  # No suggestions for Lipton-Ice Tea
    "B01": ["Kinder bueno"],  # Lays Max pairs with   Kinder Bueno
    "B02": [],  # No suggestions for Cheetos Flaming Hot
    "B03": ["Snickers"],  # Super rings pair with Snickers
    "C01": ["Cheetos Flamin Hot"],  # Twix pairs with Cheetos Flamin Hot
    "C02": ["Super rings"],  # Snickers pairs with Super rings
    "C03": ["Lays Max"],  # Kinder Bueno pairs with Lays Max
}






# A welcome message
print('''

░░░░░██╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗██╗░██████╗  ██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░
░░░░░██║██╔══██╗██║░░██║██╔══██╗████╗░██║╚█║██╔════╝  ██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░
░░░░░██║██║░░██║███████║███████║██╔██╗██║░╚╝╚█████╗░  ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░
██╗░░██║██║░░██║██╔══██║██╔══██║██║╚████║░░░░╚═══██╗  ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗
╚█████╔╝╚█████╔╝██║░░██║██║░░██║██║░╚███║░░░██████╔╝  ░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝''')

print('________________________________________________________________________________________________________________________________________')
print()
print("Welcome to Johan's Vending Machine!")


# Displays the inventory
def display_invent():
    table = PrettyTable()
    table.field_names = ["Item Code", "Item", "Price (AED)"]

    for item in x:
        item_code = next(iter(item.keys()))
        item_name = item[item_code]
        item_price = item[y]
        

        table.add_row([item_code, item_name, item_price])

    print(table)

print()
print('__________________________________________________________________________________________________________________________________')
print()







#input for the amount customer wants to purchase with
while True:
    display_invent()
    try:
        print()
        money = float(input('Enter the amount you wish to spend: '))
        if money < 1:
            print('The amount you have inserted is insufficient. Please try again.')
        else:
            print()
            print(f'       Your current balance is {money}AED.')
            break
    except ValueError:
        print("Invalid input. Please try again.")


print()
print('_______________________________________________________________________________________________________________________________')
print()


    
#vending Machine
def vending_machine():
    while True:
        

        item_code = input("Enter The Item Code You Want To Purchase: ")
        item = next((item for item in x if item_code in item), None)



        if not item:
            print("Invalid Item Code, Try again later!")
            continue

       



    
        print(f"Thank you for your Purchase! Enjoy Your {item[item_code]}")
        change = money - item[y]
        

        
        
        suggestions = item_pairs.get(item_code, [])
        if suggestions:
            p_name = suggestions[0]
            print(f"Would You Like To Pair Your {item[item_code]} with a {p_name}? Yes(Y) or type any key to quit:")
            p_choice = input()
            if p_choice == "Y" or 'y':
                print(f"Here Is Your Change: AED {change:.2f}")
                
            else:
                print("Thank you for the purchase, hope you have a wonderful day. \n Please Come Back Again.")
        break

if __name__ == "__main__":
    vending_machine() # starts the vending machine simulation
    
            