import unittest
from ProblemSolving import station_power

class StationTests(unittest.TestCase):
    
    # setup method to create objects
    def setUp(self):
        print("setting up")
        self.test_power = station_power([0,0],[[0, 0, 10], [20, 20, 5], [10, 0, 12]])
    
    # tear down method
    def tearDown(self):
        print("Tearing down")
        del self.test_power

    def test_find(self):
        item = self.test_power.find("laatikko",[["yksi","kaksi","kolme"],["sydan","laatikko","pallo"]])
        self.assertEqual(["sydan","laatikko","pallo"],item)

    def test_calculate_distance_and_power(self):
        self.test_power.calculate_distance_and_power([0,0],[[0, 0, 10], [20, 20, 5], [10, 0, 12]])
        
    def test_answer(self):
        answer = self.test_power.calculate_distance_and_power([0,0],[[0, 0, 10], [20, 20, 5], [10, 0, 12]])
        self.test_power.answer(answer)
        

if __name__ == '__main__':
    unittest.main()
