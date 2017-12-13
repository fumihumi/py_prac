import unittest
import calc

class TestCalc(unittest.TestCase):
  # TestCalcクラスの宣言。unittestモジュールのTestCaseクラスを継承
    def setUp(self):
        print('setUp')
        self.c =  calc.Calc()

    def test1(self):
        print('add')
        r = self.c.add(2,3)
        print(f'add(2,3) : {r}')
        self.assertEqual(r,5)

    def test2(self):
        print('add_Test')
        r1 = self.c.add(1,2,3)
        self.assertEqual(r1,6)

    def test3(self):
        print('addtest')
        r2 = self.c.add(1,2,3,4,5,6,7,8,9,10)
        self.assertEqual(r2,55)

    def test4(self):
        print('sub')
        r = self.c.sub(5,3)
        print(f'sub(5,3) : {r}')
        self.assertEqual(r,2)

    def test5(self):
        print('div')
        r = self.c.div(10,2)
        print(f'div(10,2): {r}')
        self.assertEqual(r,5)

    def test6(self):
        print('mul')
        r = self.c.mul(2,4)
        print(f'mul(2,4) : {r}')
        self.assertEqual(r,8)

    def test_calc(self):
        print('testcalc')
        r = self.c.calc('2*3+5')
        self.assertEqual(r,11)

    def testcalc2(self):
        print('calctest')
        r = self.c.sqrt(2)
        self.assertAlmostEqual(r,1.41421356,7)
        

if __name__ == "__main__":
    unittest.main()