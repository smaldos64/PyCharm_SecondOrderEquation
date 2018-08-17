import unittest
#from unittest import TestCase

from MyMath import MyMath_Class

import Point


class TestMyMath_Class(unittest.TestCase):
    def test_calculate_discriminant(self):
        Discriminant = MyMath_Class.calculate_discriminant(4, 10, 4)
        self.assertEqual(Discriminant, 36)

        Discriminant = MyMath_Class.calculate_discriminant(2, 4, 2)
        self.assertEqual(Discriminant, 0)

        Discriminant = MyMath_Class.calculate_discriminant(2, 2, 2)
        self.assertEqual(Discriminant, -12)

    def test_calculate_roots(self):
        RootPointList = []

        RootPointList = MyMath_Class.calculate_Roots(4, 10, 4)
        self.assertEqual(RootPointList[0], -0.5)
        self.assertEqual(RootPointList[1], -2)

        del RootPointList[:]

        RootPointList = MyMath_Class.calculate_Roots(2, 4, 2)
        self.assertEqual(RootPointList[0], -1)

        del RootPointList[:]

        RootPointList = MyMath_Class.calculate_Roots(2, 2, 2)
        self.assertEqual(RootPointList.__len__(), 0)

    def test_calculate_function_value(self):
        CurrenPoints = []
        CurrentPoint = Point.Point_Class()

        CurrenPoints.append(Point.Point_Class())
        CurrenPoints[0].x_value = 1
        CurrenPoints[0].y_value = MyMath_Class.CalculateFunctionValue(4, 10, 4, 1)
        self.assertEqual(CurrenPoints[0].y_value, 18) and self.assertEqual(CurrenPoints[0].x_value, 1)

        CurrenPoints.append(Point.Point_Class())
        CurrenPoints[1].x_value = 2
        CurrenPoints[1].y_value = MyMath_Class.CalculateFunctionValue(4, 10, 4, 2)
        self.assertEqual(CurrenPoints[1].y_value, 40) and self.assertEqual(CurrenPoints[1].x_value, 2)

        CurrenPoints.append("Lars")
        CurrenPoints.append(53)

        # self.fail()


if __name__ == '__main__':
    unittest.main()



