class Calc:
    def calculator(self, num1, func, num2):

        if type(num1) == str and (num1.startswith('-') and num1[1:].isdigit() or num1.isdigit()):
            num1 = int(num1)
        if type(num2) == str and (num2.startswith('-') and num2[1:].isdigit() or num2.isdigit()):
            num2 = int(num2)

        if not (type(num1) == str or type(num2) == str):
            if func == "+":
                res = num1 + num2
            elif func == "-":
                res = num1 - num2
            elif func == "*":
                res = num1 * num2
            elif func == "/":
                try:
                    res = num1 / num2

                except ZeroDivisionError:
                    print("nije moguce deljenje sa nulom")
                    return False

            else:
                return False
            return res
        else:
            return False