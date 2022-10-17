class Homework(object):
    """Simple class"""

    def vincle_buzz(self, n):
        """
        Display the numbers from 1 to 100 replacing the multiples of 3 by the
        word "VIN" and the multiples of 5 by "CLE". For the cases that are
        multiples of both 3 and 5, use the combination "VINCLE".
        """
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("VINCLE")
            elif i % 3 == 0:
                result.append("VIN")
            elif i % 5 == 0:
                result.append("CLE")
            else:
                result.append(str(i))
        return result


ob1 = Homework()
print(ob1.vincle_buzz(100))
