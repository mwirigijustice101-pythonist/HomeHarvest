class coffeApp:

    def __int__(self):

        # store menu and sales

        self.menu = {"Espresso": 2.00,"Latter": 3.50, "cappuccino": 4.00}

        self.sales = 0

        self.last_order = None #store last order for receipt

    #show coffe menu

    def show_menu(self):

        print("\n-- coffe menu --")

        for coffe, price in self.menu.items():

            print(f"{coffe} : ${price}")

    # take order from the user

    def take_order(self):

        self.show_menu()

        choice = input("\nEnter coffe name: ")

        if choice in self.menu:

            price = self.menu[choice]

            print(f"{choice} served!#i should put a coffe emoji here")

            self.sales += price

            self.last_order = (choice, price)

        else:

            print("x coffe not available")

    # print receipt for te last order

    def print_receipt(self):

        if not self.last_order:

            print("\n No order found to print receipt")

            return

        coffe,price = self.last_order

        print("\n-----RECEIPT-----")

        print(f"{coffe}")

        print(f"price ${price}")

        print("----------------------")

        print("Thank you for your purchase!  ")

    # check total sales

    def view_sales(self):

        print(f"\nTotal sales: ${self.sales}")

    # main menu loop

    def run(self):

          while True:

              print("\n=== coffe App Menu ===")

              print("1. show menu")

              print("2. Order coffe")

              print("3. print Receipt")

              print("4. view sales")

              print ("5. Exit")

              option = input("choice option: ")

              if option == "1":

                  self.show_menu()

              elif option == "2":

                  self.take_order()

              elif option == "3":

                  self.print_receipt()

              elif option == "4":

                  self.print_sales()

              elif option == "5":

                  print("GOODBYE!")

                  break

              else:

                  print("Invalid choice")


# start the app
#
# app = coffeApp()
















