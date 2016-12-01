import unittest
from ostoskori_testi import Basket
import numbers

class BasketTests(unittest.TestCase):
    
    # setup method to create objects
    def setUp(self):
        print("setting up")
        self.sarin_ostoskori = Basket("Sari", ["minttu","kahvi","suklaakakku"], 18.5)
    
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
        self.sarin_ostoskori.delete_product("koira", 20)
        self.assertNotIn("Pasi", self.sarin_ostoskori.contents, "delete_product did not delete item")

    # test of count_discount_price method counts price
    def test_count_discount_price(self):
        self.sarin_ostoskori.count_discount_price(30.0)

    # test of new_customer method makes new customer
    def test_new_customer(self):
        
    # test of count_discount_price method counts price
    def test_check_price(self):
        self.sarin_ostoskori.check_price("suklaakakku")

if __name__ == '__main__':
    unittest.main()
