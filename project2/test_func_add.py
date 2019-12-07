from unittest import TestCase
from project2 import calc_func


class TestFunc_add(TestCase):
    def test_func_add(self):
        #self.fail()

        self.assertEqual(calc_func.My_Calculator.func_add(self,5,7), 12)
        self.assertNotEqual(calc_func.My_Calculator.func_add(self,5,7), 11)

        self.assertEqual(calc_func.My_Calculator.func_mul(self,5,7), 35)
        self.assertNotEqual(calc_func.My_Calculator.func_mul(self,5,7), 3)



