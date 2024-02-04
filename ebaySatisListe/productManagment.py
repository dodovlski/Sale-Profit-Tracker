import time

from products import *


def main():
    print(
        """
*********************
1. Add a product
2. All products
3. Total profit
4. Profit Rate
5. Exit
*********************
"""
    )


library = ProductLibrary()
main()

while True:
    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting")
        time.sleep(2)
        break

    elif choice == "1":
        name = input("Enter product name: ")
        purchase_price = float(input("Enter product purchase price: "))
        sale_price = float(input("Enter product sale price: "))
        profit = sale_price - purchase_price

        new_product = Product(name, purchase_price, sale_price, profit)
        print("Adding product...")
        time.sleep(2)
        library.addProduct(new_product)
        print("******************************")
        print("Product Added successfully")

    elif choice == "2":
        library.getAllProducts()

    elif choice == "3":
        library.getTotalProfit()

    elif choice == "4":
        library.profitRate()
