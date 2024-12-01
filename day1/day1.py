''' ###########################################################################
    Title: Advent of Code 2024 - Day 1
    Author: Markus E. Oberndorfer
########################################################################### '''

''' IMPORTS '''
import numpy as np

''' SETTINGS '''
path = './input.txt'

''' CLASSES '''
class list_reader:
    def __init__(self, path):
        data = []
        with open(path, 'r') as file:
            for line in file:
                newline = line[:-1].split(' ')
                newline = [int(newline[0]), int(newline[-1])]
                data.append(newline)
        self.data = np.array(data)

    def seperate_lists_and_sort(self):
        self.list1 = self.data[:, 0]
        self.list1.sort()
        self.list2 = self.data[:, 1]
        self.list2.sort()

    def calc_distance_sum(self):
        distance = abs(self.list1 - self.list2)
        return sum(distance)
    
    def calc_similarity_score(self):
        sim_score = 0
        for elem in self.list1:
            counter = sum(self.list2 == elem)
            sim_score += elem * counter
        return sim_score

''' MAIN '''
lst_reader = list_reader(path=path)
lst_reader.seperate_lists_and_sort()
res1 = lst_reader.calc_distance_sum()
res2 = lst_reader.calc_similarity_score()
print(f'Result task 1: {res1}') 
print(f'Result task 2: {res2}') 