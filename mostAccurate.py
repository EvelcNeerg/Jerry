#!/usr/bin/env python3.6
"""
Finds the most accurate result of ImageComparison.py
"""

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


def most_accurate():
    with open("Data/accuracyData.txt", "r") as file:
        acc_array = file.read().split('\n')
        acc_array.pop(-1)
        img_d = {}
        for i in range(len(acc_array)):
            acc_array[i] = acc_array[i].split(",")
            f_name = acc_array[i][-1]
            acc_array[i].pop(-1)
            acc_array[i] = [int(x) for x in acc_array[i]]
            acc_array[i] = acc_array[i][0] / int((acc_array[i][0] + acc_array[i][1]))
            img_d[acc_array[i]] = f_name
        return max(acc_array), img_d


