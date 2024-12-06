''' ###########################################################################
    Title: Advent of Code 2024 - Day 4
    Author: Markus E. Oberndorfer
########################################################################### '''

''' IMPORTS '''


''' SETTINGS '''
path = 'input.txt'

''' CLASSES '''
class WordSearch:
    def __init__(self, path):
        data = []
        with open(path, 'r') as file:
            for line in file:
                data.append(line.replace('\n', ''))
        self.data = data

    def find_xmas(self):
        xmas_counter = 0
        xmas_counter += WordSearch._get_hori_xmas(self.data)
        xmas_counter += WordSearch._get_vert_xmas(self.data)
        xmas_counter += WordSearch._get_diag_xmas(self.data)

        return xmas_counter
    
    @staticmethod
    def _get_hori_xmas(data):
        hori_xmas = 0
        for line in data:
            hori_xmas += line.count('XMAS')
            hori_xmas += line.count('SAMX')
        return hori_xmas
    
    @staticmethod
    def _get_vert_xmas(data):
        vert_xmas = 0
        vert_lines = [''.join(chars) for chars in zip(*data)]
        for line in vert_lines:
            vert_xmas += line.count('XMAS')
            vert_xmas += line.count('SAMX')
        return vert_xmas
    
    @staticmethod
    def _get_diag_xmas(data):
        diag_xmas = 0
        # Check top to bottom - left to right
        x_max = len(data[0]) - len('XMAS') 
        y_max = len(data) - len('XMAS') 
        for y in range(y_max):
            for x in range(x_max):
                word = ''.join(data[y+i][x+i] for i in range(4))
                if word == 'XMAS' or word == 'SAMX':
                    diag_xmas += 1

        # Check top to bottom - right to left
        x_min = len('XMAS')
        y_max = len(data) - len('XMAS')
        for y in range(y_max):
            for x in reversed(range(x_min, len(data[0]))):
                word = ''.join(data[y+i][x-i] for i in range(4))
                if word == 'XMAS' or word == 'SAMX':
                    diag_xmas += 1

        return diag_xmas



''' MAIN '''
wordsearch = WordSearch(path)
res1 = wordsearch.find_xmas()

print(f'Result task 1: {res1}') 
# print(f'Result task 2: {res2}') 