# Basket is a simple class for a MVP stage shopping application
# You can make a new basket by adding a name, list of products and a price
# You can return the name of the customer, the contents of the basket and the price
# You can add items later as well
# You can count the new price if you have a discount

# TODO: exception handling, user input...

class Basket:
    def __init__(self, customer, contents, price):
        self.customer = customer
        self.contents = contents
        self.price = price

    def return_customer(self):
        return self.customer
        
    def return_contents(self):
        return self.contents

    def return_price(self):
        return self.price

    def add_product(self, product, product_price):
        self.contents.append(product)
        self.price += product_price

    def delete_product(self, product, product_price):
        for i in self.contents:
            if i == product:
                self.contents.remove(product)
        self.price -= product_price
                    
    def count_discount_price(self, percent):
        discount = percent / 100.0
        return self.price - self.price * discount

    def check_price(self, product):
        product_price = [["maito","banaani","hernekeitto","minttu","kahvi","suklaakakku"],[2.3,0.7,3.1,4,5.6,9.9]]
        i = product_price[0].index(product)
        return product_price[1][i]

    def new_customer(self):
        #user input:
        cont = 'tyhja'
        contents = list[]
        product_prices = list[]
        user = input("Asiakkaan nimi: ")
        print('Anna 0 jos haluat lopettaa ostosten luettelun')
        if(cont != '0'):
            cont = input("Ostos: ")
            contents.append(cont)
            pric = input("Hinta: ")
            product_prices.append(pric)
            #check
            if(len(contents)==len(product_prices)):
                continue
            else:
                print("ostokset ja hinnat eiv‰t t‰sm‰‰")
                new_customer():           
        else:
            print(user, contents, product_prices)
            asiakkaan_ostoskori = Basket(user, contents, product_prices)

# Making a test object:
jarin_ostoskori = Basket("Jari", ["maito","banaani","hernekeitto"], 7)
sarin_ostoskori = Basket("Sari", ["minttu","kahvi","suklaakakku"], 18.5)
