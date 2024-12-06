# ''' ###########################################################################
#     Title: Advent of Code 2024 - Day 2
#     Author: Markus E. Oberndorfer
# ########################################################################### '''

# ''' IMPORTS '''
# # No imports

# ''' SETTINGS '''
# path = './input.txt'

# ''' CLASSES '''
# class ReportCheck:
#     def __init__(self, path):
#         data = []
#         with open(path, 'r') as file:
#             for line in file:
#                 newline = list(map(int, line.split(' ')))
#                 data.append(newline)
#         self.data = data

#     ''' CLASS METHODS '''
#     def safety_check(self):
#         safety_count = 0
#         for report in self.data:
#             if ReportCheck._safety_check_order(report) and ReportCheck._safety_check_dist(report):
#                 safety_count += 1
#         return safety_count
    
#     def safety_check_dampend(self):
#         safety_count = 0
#         for report in self.data:
#             status, report_, damped = ReportCheck._safety_check_order_damp(report)
#             if status:
#                 if ReportCheck._safety_check_dist_damp(report_, damped):
#                     safety_count += 1
#         return safety_count
    
#     ''' STATIC CLASS METHODS '''
#     @staticmethod
#     def _safety_check_order(report):
#         decrease = True
#         for idx in range(len(report)-1):
#             if not report[idx] > report[idx+1]:
#                 decrease = False
#                 break

#         increase = True
#         for idx in range(len(report)-1):
#             if not report[idx] < report[idx+1]:
#                 increase = False
#                 break
        
#         if increase or decrease:
#             return True
#         else:
#             return False
        
#     @staticmethod
#     def _safety_check_order_damp(report):
#         if ReportCheck._safety_check_order(report) == True:
#             return (True, report, False)
#         else:
#             for idx, _ in enumerate(report):
#                 report_ = report.copy()
#                 _ = report_.pop(idx)
#                 if ReportCheck._safety_check_order(report_) == True:
#                     return (True, report_, True)
#             return (False, None, None)

#     @staticmethod
#     def _safety_check_dist(report):
#         for idx in range(len(report)-1):
#             if abs(report[idx] - report[idx+1]) > 3:
#                 return False
#         return True
    
#     @staticmethod
#     def _safety_check_dist_damp(report, damped):
#         if ReportCheck._safety_check_dist(report) == True:
#             return True
#         else:
#             if damped:
#                 return False
#             else:
#                 for idx, _ in enumerate(report):
#                     report_ = report.copy()
#                     _ = report_.pop(idx)
#                     if ReportCheck._safety_check_dist(report_) == True:
#                         return True

# reportcheck = ReportCheck(path=path)
# res1 = reportcheck.safety_check()
# res2 = reportcheck.safety_check_dampend()
# print(f'Result task 1: {res1}') 
# print(f'Result task 2: {res2}') 

class ReportCheck:
    def __init__(self, path):
        data = []
        with open(path, 'r') as file:
            for line in file:
                newline = list(map(int, line.split()))
                data.append(newline)
        self.data = data

    def safety_check(self):
        """Check reports for safety without dampening."""
        safety_count = 0
        for report in self.data:
            if self._safety_check_order(report) and self._safety_check_dist(report):
                safety_count += 1
        return safety_count

    def safety_check_dampened(self):
        """Check reports for safety with Problem Dampener."""
        safety_count = 0
        for report in self.data:
            # Check original report
            if self._safety_check_order(report) and self._safety_check_dist(report):
                safety_count += 1
            else:
                # Check all single-level removals
                for idx in range(len(report)):
                    modified_report = report[:idx] + report[idx+1:]
                    if self._safety_check_order(modified_report) and self._safety_check_dist(modified_report):
                        safety_count += 1
                        break  # Stop checking further removals for this report
        return safety_count

    @staticmethod
    def _safety_check_order(report):
        """Check if levels are monotonically increasing or decreasing."""
        increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report)-1))
        decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report)-1))
        return increasing or decreasing

    @staticmethod
    def _safety_check_dist(report):
        """Check if all adjacent differences are between 1 and 3."""
        return all(1 <= abs(report[i+1] - report[i]) <= 3 for i in range(len(report)-1))


# Load and process input
path = './input.txt'
reportcheck = ReportCheck(path=path)
res1 = reportcheck.safety_check()
res2 = reportcheck.safety_check_dampened()
print(f'Result task 1: {res1}') 
print(f'Result task 2: {res2}')
