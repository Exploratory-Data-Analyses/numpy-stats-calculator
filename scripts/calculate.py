'''
    This is a simple program that uses numpy to calculate mean,
    standard deviation, variance, maximum, minimum and sum of a List
    NB: The list should have 9 elements; the results should be list of list
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate(list_data):
    if len(list_data) != 9:
        raise ValueError('List must contain exactly nine numbers')

    try:
        array_data = np.array(list_data, dtype=float).reshape(3, 3)
    except ValueError:
        raise TypeError('List must contain numeric values')

    calculations = {
        'mean': [np.mean(array_data, axis=0).tolist(), np.mean(array_data, axis=1).tolist(), np.mean(array_data).tolist()],
        'variance': [np.var(array_data, axis=0).tolist(), np.var(array_data, axis=1).tolist(), np.var(array_data).tolist()],
        'standard deviation': [np.std(array_data, axis=0).tolist(), np.std(array_data, axis=1).tolist(), np.std(array_data).tolist()],
        'max': [np.max(array_data, axis=0).tolist(), np.max(array_data, axis=1).tolist(), np.max(array_data).tolist()],
        'min': [np.min(array_data, axis=0).tolist(), np.min(array_data, axis=1).tolist(), np.min(array_data).tolist()],
        'sum': [np.sum(array_data, axis=0).tolist(), np.sum(array_data, axis=1).tolist(), np.sum(array_data).tolist()]
    }

    return calculations

def plot_results(calculations):
    categories = ['Mean', 'Variance', 'Standard Deviation', 'Max', 'Min', 'Sum']
    values_axis0 = [calculations['mean'][0], calculations['variance'][0], calculations['standard deviation'][0], calculations['max'][0], calculations['min'][0], calculations['sum'][0]]
    values_axis1 = [calculations['mean'][1], calculations['variance'][1], calculations['standard deviation'][1], calculations['max'][1], calculations['min'][1], calculations['sum'][1]]
    values_overall = [calculations['mean'][2], calculations['variance'][2], calculations['standard deviation'][2], calculations['max'][2], calculations['min'][2], calculations['sum'][2]]

    fig, axs = plt.subplots(3, 2, figsize=(12, 10))

    for i, ax in enumerate(axs.flat):
        if i < len(categories):
            values_to_plot = [values_axis0[i], values_axis1[i], [values_overall[i]]]
            ax.boxplot(values_to_plot, labels=['Axis 0', 'Axis 1', 'Overall'])
            ax.set_title(categories[i])
            ax.set_ylabel(categories[i])

    plt.tight_layout()
    plt.savefig('../figures/results.png')
    plt.show()

def main():
    # Load data
    try:
        df = pd.read_csv('../data/input_data.csv', header=None)
        list_data = df.values.flatten().tolist()
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Perform calculations
    try:
        calculations = calculate(list_data)
    except Exception as e:
        print(f"Error in calculations: {e}")
        return

    # Plot results
    try:
        plot_results(calculations)
    except Exception as e:
        print(f"Error plotting results: {e}")

if __name__ == "__main__":
    main()
