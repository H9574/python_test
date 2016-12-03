import unittest
from ostoskori_testi import Basket
import numbers

class BasketTests(unittest.TestCase):
    
    # setup method to create objects
    def setUp(self):
        print("setting up")
        self.sarin_ostoskori = Basket("Sari", ["minttu","suklaakakku","maito","maito","banaani","hernekeitto","banaani","banaani"], 23.7)
    
    # tear down method
    def tearDown(self):
        print("Tearing down")
        del self.sarin_ostoskori

    # test if variable customer is a string
    def test_customer_is_string(self):
        self.assertIsInstance(self.sarin_ostoskori.customer, str, "variable customer is not a string")

    # test if variable contents is a list
    def test_contents_are_list(self):
        self.assertIsInstance(self.sarin_ostoskori.contents, list, "variable content is not a list")

    # test if variable price is a number
    def test_price_is_number(self):
        self.assertIsInstance(self.sarin_ostoskori.price, numbers.Number, "variable price is not a number")

    # test if add_product method adds a product to the list
    def test_can_add_product(self):
        self.sarin_ostoskori.add_product("minttu", 4)
        self.assertIn("minttu", self.sarin_ostoskori.contents, "add_product did not add new item")

    # test of delete_product method deletes a product
    def test_can_delete_product(self):
        self.sarin_ostoskori.delete_product("minttu", 4)
        self.assertNotIn("minttu", self.sarin_ostoskori.contents, "delete_product did not delete item")

    # test of count_discount_price method counts price
    def test_count_discount_price(self):
        self.sarin_ostoskori.count_discount_price(30.0)

#laatimani testit
        
    # test return_price method returns right name
    def test_return_customer(self):
        self.assertEqual(self.sarin_ostoskori.return_customer(),"Sari")

    # test return_price method returns right products
    def test_return_contents(self):
        self.assertEqual(self.sarin_ostoskori.return_contents(),["minttu","suklaakakku","maito","maito","banaani","hernekeitto","banaani","banaani"])

    # test return_price method returns right price
    def test_return_price(self):
        self.assertEqual(self.sarin_ostoskori.return_price(),23.7)

    # test basket price is right when compared to items
    def test_items_and_prices(self):
        product_number = 0
        price = 0.0
        while(product_number < self.sarin_ostoskori.count_all_in_basket()):
            product = self.sarin_ostoskori.get_one_product_from_basket(product_number)
            product_number = product_number+1
            price = price + self.sarin_ostoskori.check_price(product)
        self.assertEqual(self.sarin_ostoskori.return_price(),price)

    # test of new_name method gives new name
    def test_new_customer(self):
        self.sarin_ostoskori.new_name("Jari")
        self.assertEqual(self.sarin_ostoskori.return_customer(),"Jari")
        
    # test of count_check_price method checks the price
    def test_check_price(self):
        self.sarin_ostoskori.check_price("suklaakakku")

    # test of check_all_in_basket method to count items in basket
    def test_count_all_in_basket(self):
        self.sarin_ostoskori.count_all_in_basket()

    # test of check_numbers_in_basket method to count items in basket
    def test_count_items_in_basket(self):
        self.sarin_ostoskori.count_items_in_basket()

    # test of get_one_product_from_basket method checks one spesific item from basket
    def test_get_one_product_from_basket(self):
        self.sarin_ostoskori.get_one_product_from_basket(1)

if __name__ == '__main__':
    unittest.main()
