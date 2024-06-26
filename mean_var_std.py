import numpy as np

def calculate(*numbers):
    # Check if exactly 9 numbers are provided
    if len(numbers) != 9:
        return "Please provide exactly 9 digits in the input list."

    # Create a 3x3 matrix from the input list
    matrix = np.array(numbers).reshape(3, 3)

    # Calculate statistics
    mean_axis0 = np.mean(matrix, axis=0)
    mean_axis1 = np.mean(matrix, axis=1)
    mean_flattened = np.mean(matrix)

    variance_axis0 = np.var(matrix, axis=0)
    variance_axis1 = np.var(matrix, axis=1)
    variance_flattened = np.var(matrix)

    std_axis0 = np.std(matrix, axis=0)
    std_axis1 = np.std(matrix, axis=1)
    std_flattened = np.std(matrix)

    max_axis0 = np.max(matrix, axis=0)
    max_axis1 = np.max(matrix, axis=1)
    max_flattened = np.max(matrix)

    min_axis0 = np.min(matrix, axis=0)
    min_axis1 = np.min(matrix, axis=1)
    min_flattened = np.min(matrix)

    sum_axis0 = np.sum(matrix, axis=0)
    sum_axis1 = np.sum(matrix, axis=1)
    sum_flattened = np.sum(matrix)

    print(matrix)

    # Create the dictionary
    stats_dict = {
        "mean": [mean_axis0, mean_axis1, mean_flattened],
        "variance": [variance_axis0, variance_axis1, variance_flattened],
        "standard deviation": [std_axis0, std_axis1, std_flattened],
        "max": [max_axis0, max_axis1, max_flattened],
        "min": [min_axis0, min_axis1, min_flattened],
        "sum": [sum_axis0, sum_axis1, sum_flattened]
    }

    return stats_dict
# Example usage:
calculate(0,1,2,3,4,5,6,7,8)
