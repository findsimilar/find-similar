"""
Proximity calculation module
"""
import numpy as np


def calc_proximity(known_data, find_similar):
    """
    Main calc proximity function
    :param known_data: Known data as matrix
    :param find_similar: Function to find similars
    """
    result = np.zeros_like(known_data)

    with np.nditer(result, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = 1.0

    result = result.astype('float64')
    return [result]


def calc_value_position(known_data, find_similar, value):
    all_values = np.copy(known_data).reshape(1, known_data.size).tolist()[0]
    result = find_similar(value, all_values)
    order_result = [item.text for item in result]
    return order_result.index(value)
