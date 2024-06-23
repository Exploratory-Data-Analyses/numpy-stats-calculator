'''
    This is a simple program that uses numpy to calculate mean,
    standard deviation, variance, maximum, minimum and sum of a List
    NB: The list should have 9 elements; the results should be list of list

    Ref: FreeCodeCamp.org - Data Analysis with Python Projects
         Project 1: Mean-Variance-Standard Deviation Calculator
'''

import numpy as np

def calculate(list_data):
    if len(list_data) < 9:
        raise ValueError('List must contain nine numbers')

    array_data = np.array(list_data)
    array_data = array_data.reshape(3,3)

#   do the calculations
    axis0_mean = np.mean(array_data, axis=0).tolist()
    axis1_mean = np.mean(array_data, axis=1).tolist()
    avg = np.mean(array_data)

    axis0_var = np.var(array_data, axis=0).tolist()
    axis1_var = np.var(array_data, axis=1).tolist()
    variance = np.var(array_data)

    axis0_std = np.std(array_data, axis=0).tolist()
    axis1_std = np.std(array_data, axis=1).tolist()
    std_dev = np.std(array_data)

    axis0_max = np.max(array_data, axis=0).tolist()
    axis1_max = np.max(array_data, axis=1).tolist()
    maximum = np.max(array_data)

    axis0_min = np.min(array_data, axis=0).tolist()
    axis1_min = np.min(array_data, axis=1).tolist()
    minimum = np.min(array_data)

    axis0_sum = np.sum(array_data, axis=0).tolist()
    axis1_sum = np.sum(array_data, axis=1).tolist()
    summ = np.sum(array_data)

    output = {
                'mean': [axis0_mean, axis1_mean, avg],
                'variance': [axis0_var, axis1_var, variance],
                'standard deviation': [axis0_std, axis1_std, std_dev],
                'max': [axis0_max, axis1_max, maximum],
                'min': [axis0_min, axis1_min, minimum],
                'sum': [axis0_sum, axis1_sum, summ]
            }

    print(output)


