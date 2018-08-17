import math
import Point

class MyMath_Class:
   @staticmethod
   def calculate_discriminant(a_coefficient, b_coefficient, c_coefficient):
        discriminant = 0

        discriminant = math.pow(b_coefficient, 2) - 4*a_coefficient*c_coefficient

        return discriminant

   def calculate_discriminant_self(self, a_coefficient, b_coefficient, c_coefficient):
       discriminant = 0

       discriminant = math.pow(b_coefficient, 2) - 4 * a_coefficient * c_coefficient

       return discriminant

   def calculate_Roots(a_coefficient, b_coefficient, c_coefficient):
        roots = []
        discriminant = MyMath_Class.calculate_discriminant(a_coefficient, b_coefficient, c_coefficient)
        if discriminant > 0:
            root1 = (-b_coefficient + math.sqrt(discriminant)) / (2 * a_coefficient)
            roots.append(root1)
            root2 = (-b_coefficient - math.sqrt(discriminant)) / (2 * a_coefficient)
            roots.append(root2)
        elif 0 == discriminant:
            root = (-b_coefficient) / (2 * a_coefficient)
            roots.append(root)

        return(roots)

   def CalculateApogeePoint(a_coefficient, b_coefficient, c_coefficient):
        ApogeePoint = Point.Point_Class()
        ApogeePoint.x_value = -b_coefficient / (2 * a_coefficient)
        ApogeePoint.y_value = -MyMath_Class.calculate_discriminant(a_coefficient, b_coefficient, c_coefficient) / (4 * a_coefficient)

        return (ApogeePoint)

   def CalculateFunctionValue(a_coefficient, b_coefficient, c_coefficient, x_value):
        y_value = a_coefficient * math.pow(x_value, 2) + b_coefficient * x_value + c_coefficient
        return (y_value)

def calculate_discriminant_non_static(self, a_coefficient, b_coefficient, c_coefficient):
        discriminant = 0

        discriminant = math.pow(b_coefficient, 2) - 4*a_coefficient*c_coefficient

        return discriminant
