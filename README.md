# NumPy Calculator Project

## Project Description

This project implements a simple calculator using NumPy to perform various statistical calculations on a list of numbers. 
The calculator computes the mean, standard deviation, variance, maximum, minimum, and sum of a given list. This project 
is an excellent demonstration of NumPy's capabilities and how it can be used to perform efficient numerical computations.

## Folder Structure

The project directory is structured as follows:

```
numpy-stats-calculator/
│
├── data/
│   └── input_data.csv
│
├── figures/
│   └── results.png
│
├── scripts/
│   ├── calculate.py
│   └── test_calculate.py
│
├── README.md
│
└── requirements.txt
```

## Files Description

- `data/input_data.csv`: Contains the input list of numbers.
- `figures/results.png`: Visual representation of the calculated metrics.
- `src/calculate.py`: Main script for performing calculations and plotting results.
- `src/test_calculate.py`: Test script to ensure the calculations are correct.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies required to run the project.


## Features

- **Input Validation**: Ensures the input list contains exactly nine elements.
- **Statistical Calculations**: Computes mean, variance, standard deviation, maximum, minimum, and sum for both rows, columns, and the entire 3x3 matrix.
- **Error Handling**: Properly handles errors such as incorrect list length and non-numeric values.
- **Testing**: Includes a comprehensive set of unit tests to validate the functionality.

## Requirements

To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/mrowurakwarteng/Exploratory-Data-Analyses/numpy-stats-calculator.git
    cd numpy-stats-calculator
    ```

2. **Run the Calculator**:

    Place your list data in the `data/input_data.csv` file.

    ```bash
    python scripts/calculate.py
    ```

3. **Run Unit Tests**:

    ```bash
    python -m unittest scripts/test_calculate.py
    ```

## Functions

### calculate

```python
def calculate(list_data):
    if len(list_data) != 9:
        raise ValueError('List must contain exactly nine numbers')

    try:
        array_data = np.array(list_data, dtype=float).reshape(3, 3)
    except ValueError:
        raise TypeError('List must contain numeric values')

    # Calculations
    calculations = {
        'mean': [np.mean(array_data, axis=0).tolist(), np.mean(array_data, axis=1).tolist(), np.mean(array_data).tolist()],
        'variance': [np.var(array_data, axis=0).tolist(), np.var(array_data, axis=1).tolist(), np.var(array_data).tolist()],
        'standard deviation': [np.std(array_data, axis=0).tolist(), np.std(array_data, axis=1).tolist(), np.std(array_data).tolist()],
        'max': [np.max(array_data, axis=0).tolist(), np.max(array_data, axis=1).tolist(), np.max(array_data).tolist()],
        'min': [np.min(array_data, axis=0).tolist(), np.min(array_data, axis=1).tolist(), np.min(array_data).tolist()],
        'sum': [np.sum(array_data, axis=0).tolist(), np.sum(array_data, axis=1).tolist(), np.sum(array_data).tolist()]
    }

    return calculations
```

### plot_results

visualises the calculated metrics using bar plots: extracts metrics for axis 0, axis 1 and overall from hte calculations
dictionary and uses subplots to create a grid of 6 subplots, each to display one metric (mean, variance, standard 
deviation, max, min and sum)

```python
def plot_results(calculations):
    categories = ['Mean', 'Variance', 'Standard Deviation', 'Max', 'Min', 'Sum']
    values_axis0 = [calculations['mean'][0], calculations['variance'][0], calculations['standard deviation'][0], calculations['max'][0], calculations['min'][0], calculations['sum'][0]]
    values_axis1 = [calculations['mean'][1], calculations['variance'][1], calculations['standard deviation'][1], calculations['max'][1], calculations['min'][1], calculations['sum'][1]]
    values_overall = [calculations['mean'][2], calculations['variance'][2], calculations['standard deviation'][2], calculations['max'][2], calculations['min'][2], calculations['sum'][2]]

    fig, axs = plt.subplots(3, 2, figsize=(12, 10))

    for i, ax in enumerate(axs.flat):
        if i < len(categories):
            ax.bar(['Axis 0', 'Axis 1', 'Overall'], [values_axis0[i], values_axis1[i], values_overall[i]], color=['#5DADE2', '#48C9B0', '#F4D03F'])
            ax.set_title(categories[i])
            ax.set_ylabel(categories[i])

    plt.tight_layout()
    plt.savefig('../figures/results.png')
    plt.show()
```


### load_data

```python
def load_data(filepath):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The dataset is empty.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("The data file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The data file is empty or not properly formatted.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
```

## Tests

The `test_calculate.py` file contains unit tests for the `calculate` function to ensure its correctness. The tests cover:

- Valid input with exactly nine numeric elements.
- Invalid input with fewer or more than nine elements.
- Non-numeric input values.

Example test case:

```python
import unittest
from scripts.calculate import calculate

class TestCalculate(unittest.TestCase):
    def test_calculate_valid_input(self):
        list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = calculate(list_data)
        expected_result = {
            'mean': [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[7, 8, 9], [3, 6, 9], 9],
            'min': [[1, 2, 3], [1, 4, 7], 1],
            'sum': [[12, 15, 18], [6, 15, 24], 45]
        }
        self.assertEqual(result, expected_result)

    def test_calculate_invalid_input_length(self):
        list_data = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.assertRaises(ValueError):
            calculate(list_data)

    def test_calculate_empty_input(self):
        list_data = []
        with self.assertRaises(ValueError):
            calculate(list_data)

    def test_calculate_non_numeric_input(self):
        list_data = [1, 2, 3, 4, 'five', 6, 7, 8, 9]
        with self.assertRaises(TypeError):
            calculate(list_data)

if __name__ == '__main__':
    unittest.main()
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -am 'Add some awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
