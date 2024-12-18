''' ###########################################################################
    Title: Advent of Code 2024 - Day 4
    Author: Markus E. Oberndorfer
########################################################################### '''

''' IMPORTS '''
import numpy as np

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
    
    def find_x_mas(self):
        num_rows = len(self.data)
        num_cols = len(self.data[0])
        data_npy = np.zeros((num_rows, num_cols), dtype=str)
        for idx in range(num_rows):
            data_npy[idx, :] = np.array([elem for elem in self.data[idx]])
        x_mas_counter = WordSearch.sliding_block_method(data_npy)
        return x_mas_counter
    

    @staticmethod
    def sliding_block_method(data):
        
        mas_counter = 0
        for y_i in range(len(data[0])-2):
            for x_i in range(len(data[0])-2):
                block = data[y_i:y_i+3, x_i:x_i+3]
                mas_counter += WordSearch.anaylize_block(block)

        return mas_counter

    @staticmethod
    def anaylize_block(block):
        diag1 = block[0, 0] + block[1, 1] + block[2, 2]
        diag2 = block[2, 0] + block[1, 1] + block[0, 2]
        if diag1 == 'MAS' or diag1 == 'SAM':
            if diag2 == 'MAS' or diag2 == 'SAM':
                return 1
        return 0
    

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
        x_max = len(data[0]) - len('XMAS') + 1
        y_max = len(data) - len('XMAS') + 1
        for y in range(y_max):
            for x in range(x_max):
                word = ''.join(data[y+i][x+i] for i in range(4))
                if word == 'XMAS' or word == 'SAMX':
                    diag_xmas += 1

        # Check top to bottom - right to left
        x_min = len('XMAS') - 1
        y_max = len(data) - len('XMAS') + 1
        for y in range(y_max):
            for x in reversed(range(x_min, len(data[0]))):
                word = ''.join(data[y+i][x-i] for i in range(4))
                if word == 'XMAS' or word == 'SAMX':
                    diag_xmas += 1

        return diag_xmas



''' MAIN '''
wordsearch = WordSearch(path)
res1 = wordsearch.find_xmas()
res2 = wordsearch.find_x_mas()

print(f'Result task 1: {res1}') 
print(f'Result task 2: {res2}') 