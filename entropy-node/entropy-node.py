import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    arr = np.array(y)
    values, counts = np.unique(arr, return_counts=True)
    probabilities = counts/arr.size

    return float(np.sum(np.log2(probabilities) * -probabilities))