import sys
sys.path.append('../src/')

import unittest
from ddt import ddt, data, unpack
import forward_Tsang_Darren as targetCode #change to file name


@ddt
class TestForward(unittest.TestCase):
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)

##################################################
#		Complete the code below
##################################################  
    # (xT_1Distribution, eT, transitionTable, sensorTable, expectedResult)
    @data(
        ({0:0.5, 1:0.5}, 0, {0:{0:0.5, 1:0.5}, 1:{0:0.5, 1:0.5}}, {0:{0:.33, 1:0.33, 2:0.34}, 1:{0:0.33, 1:0.33, 2:0.34}}, {0: 0.5, 1: 0.5}),
        ({0:0.9, 1:0.1}, 1, {0:{0:0.8, 1:0.2}, 1:{0:0.99, 1:0.01}}, {0:{0:0.1, 1:0.2, 2:0.7}, 1:{0:0.4, 1:0.4, 2:0.2}}, {0: 0.69348, 1: 0.30652}),
        ({0:0.25, 1:0.75}, 2, {0:{0:0.45, 1:0.55}, 1:{0:0.33, 1:0.67}}, {0:{0:0.2, 1:0.2, 2:0.6}, 1:{0:0.1, 1:0.8, 2:0.1}}, {0: 0.77143, 1: 0.22857})
    )
    @unpack
    def test_forward(self, xT_1Distribution, eT, transitionTable, sensorTable, expectedResult):
        calculatedResult = targetCode.forward(xT_1Distribution, eT, transitionTable, sensorTable)
        self.assertNumericDictAlmostEqual(calculatedResult, expectedResult, places=4)

##################################################
#		Complete the code above
##################################################  
	
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)