''' ###########################################################################
    Title: Advent of Code 2024 - Day 3
    Author: Markus E. Oberndorfer
########################################################################### '''

''' IMPORTS '''
import re

''' SETTINGS '''
path = 'input.txt'

''' CLASSES '''
class MullOver:
    def __init__(self, path):
        data = []
        with open(path, 'r') as file:
            for line in file:
                data.append(line)
        self.data = data

    def calculate_1(self):
        mul_sum = 0
        for line in self.data:
            muls = MullOver._get_muls(line)
            for elem in muls:
                mul_sum += elem[0] * elem[1]
        return mul_sum
    
    def calculate_2(self):
        mul_sum = 0
        line = ''
        for line_ in self.data:
            line += line_
        muls = MullOver._get_muls_dos(line)
        for elem in muls:
            mul_sum += elem[0] * elem[1]
        return mul_sum

    # Static Class Functions
    @staticmethod
    def _get_muls(line):
        # Regular expression for 'mul(X,Y)' where X and Y are numbers up to 3 digits
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = [(int(elem[0]), int(elem[1])) for elem in re.findall(pattern, line)]
        return matches
    
    @staticmethod
    def _get_muls_dos(line):
        # Regular expression for 'mul(X,Y)' where X and Y are numbers up to 3 digits
        pattern = r"(do\(\)|don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))"
        matches_ = re.finditer(pattern, line)

        use_mul = True
        matches = []

        for match in matches_:
            if match.group(0) == "do()":  # Matches "do()" or "don't()"
                use_mul = True
            if match.group(0) == "don't()":  # Matches "do()" or "don't()"
                use_mul = False

            if 'mul' in match.group(0):
                if use_mul:
                    matches.append((int(match.group(3)), int(match.group(4))))

        return matches

''' MAIN '''
mullover = MullOver(path=path)
res1 = mullover.calculate_1()
res2 = mullover.calculate_2()
print(f'Result task 1: {res1}') 
print(f'Result task 2: {res2}') 

