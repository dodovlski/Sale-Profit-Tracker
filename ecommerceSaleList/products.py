import sqlite3
import time


class Product:
    def __init__(self, name, purchase_price, sale_price, profit):
        self.profit = profit
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price

    def __str__(self):
        return "name           : {}\npurchase_price : $ {}\nsale_price     : $ {}\nprofit         : $ {}".format(
            self.name, self.purchase_price, self.sale_price, self.profit
        )


class ProductLibrary:
    def __init__(self):
        self.cursor = None
        self.con = None
        self.createConnection()

    def createConnection(self):
        self.con = sqlite3.connect("products.db")
        self.cursor = self.con.cursor()

        query = (
            "CREATE TABLE IF NOT EXISTS products (name TEXT, purchase_price FLOAT, "
            "sale_price FLOAT, profit FLOAT)"
        )

        self.cursor.execute(query)
        self.con.commit()

    def disconnect(self):
        self.con.close()

    def addProduct(self, product):
        query = "INSERT INTO products (name, purchase_price, sale_price, profit) VALUES (?, ?, ?, ?)"
        total_profit = product.sale_price - product.purchase_price

        self.cursor.execute(
            query,
            (product.name, product.purchase_price, product.sale_price, total_profit),
        )
        self.con.commit()

    def getAllProducts(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()

        if len(products) == 0:
            print("No products found")
        else:
            print("***********************************")
            for i in products:
                product = Product(i[0], i[1], i[2], i[3])
                print(product)
                print("***********************************")

    def productQuery(self, product):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (product,))
        products = self.cursor.fetchall()

        if len(products) == 0:
            print("No products found")
        else:
            product = Product(
                products[0][0], products[0][1], products[0][2], products[0][3]
            )
            print(product)

    def getTotalProfit(self):
        query = "SELECT SUM(profit) FROM products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()

        if len(products) == 0:
            print("No products found")
        else:
            all_profit = 0
            print("*********************")
            for i in products:
                all_profit += i[0]
            print("Total profit: $ {}".format(all_profit))
            print("*********************")

    def profitRate(self):
        query = "SELECT SUM(profit) FROM products"
        self.cursor.execute(query)
        products = self.cursor.fetchall()

        query2 = "SELECT SUM(sale_price) FROM products"
        self.cursor.execute(query2)
        sales = self.cursor.fetchall()

        all_profit = 0
        all_sales = 0

        for i in products:
            all_profit += i[0]

        for i in sales:
            all_sales += i[0]

        print("Profit Rate :" + str(all_profit / all_sales))
