import MyMath
from MyMath import MyMath_Class

import ToolsScreen
import Point

from MyInput import MyInput_Class

""""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
"""

if __name__ == '__main__':
    A_Coefficient = 0
    B_Coefficient = 0
    C_Coefficient = 0
    Discriminant = 0
    roots = []
    Points = []
    myMath_obj = MyMath.MyMath_Class()

    """"
    myclass = MyNumbers()
    myiter = iter(myclass)

    for x in myiter:
        print(x)
    """

    while True:
        ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(1)

        A_Coefficient = MyInput_Class.InputFloat("Indtast a koefficient : ")
        B_Coefficient = MyInput_Class.InputFloat("Indtast b koefficient : ")
        C_Coefficient = MyInput_Class.InputFloat("Indtast c koefficient : ")

        ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(2)

        Discriminant = myMath_obj.calculate_discriminant(A_Coefficient, B_Coefficient,C_Coefficient)
        print("Discriminant er : %d" % Discriminant)

        Discriminant = myMath_obj.calculate_discriminant_self(A_Coefficient, B_Coefficient, C_Coefficient)
        print("Discriminant er : %d" % Discriminant)

        Discriminant = MyMath.MyMath_Class.calculate_discriminant(A_Coefficient, B_Coefficient, C_Coefficient)
        print("Discriminant er : %d" % Discriminant)

        Discriminant = MyMath_Class.calculate_discriminant(A_Coefficient, B_Coefficient, C_Coefficient)
        # Igen på grund af linje 2 kan vi arbejde direkte på MyMath klassen i filen MyMath.py
        print("Discriminant er : %d" % Discriminant)

        Discriminant = MyMath_Class.calculate_discriminant_self(myMath_obj, A_Coefficient, B_Coefficient, C_Coefficient)
        # Ifølge Beginning Python bogen nederst side 149 kan vi også bruge denne syntaks.
        print("Discriminant er : %d" % Discriminant)

        roots = MyMath_Class.calculate_Roots(A_Coefficient, B_Coefficient, C_Coefficient)
        if roots.__len__() > 0:
            ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(1)
            RodNummer = 1;
            for rod in roots:
                RootPoint = Point.Point_Class()
                RootPoint.x_value = rod
                print("Rod %d er : (%s; %s)" % (RodNummer, RootPoint.x_value, RootPoint.y_value))
                RodNummer += 1
            #print("Rødder er : {}".roots)

        ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(1)
        ApogeePoint = MyMath_Class.CalculateApogeePoint(A_Coefficient, B_Coefficient, C_Coefficient)
        print("Toppunkt er : (%s; %s)" % (ApogeePoint.x_value, ApogeePoint.y_value))

        NumberOfPointsInserted = 1
        #PointToInvestigate = Point.Point_Class()
        while True:
            x_value = MyInput_Class.InputFloat("Indtast %d. x værdi der skal beregnes y værdi for (100 afslutter) : " % (NumberOfPointsInserted))
            if 100 != float(x_value):
                PointToInvestigate = Point.Point_Class()
                PointToInvestigate.x_value = float(x_value)
                PointToInvestigate.y_value = MyMath_Class.CalculateFunctionValue(A_Coefficient, B_Coefficient, C_Coefficient, PointToInvestigate.x_value)
                Points.append(PointToInvestigate)
                NumberOfPointsInserted += 1
            else:
                break

        NumberOfPointsPrinted = 1
        if Points.__len__() > 0:
            ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(1)

        for Point in Points:
           print("Punkt %d : (%s; %s)" % (NumberOfPointsPrinted, Point.x_value, Point.y_value))
           NumberOfPointsPrinted += 1
        #print(myMath.__class__)
        #print(myMath.__sizeof__())

        del Points[:] # Clear Point List
        ToolsScreen.ToolsScreen_Class.Make_Empty_Lines(1)

        RunAgain = input("0 = stop. Andet = kør igen : ")

        if 0 == int(RunAgain):
            break
