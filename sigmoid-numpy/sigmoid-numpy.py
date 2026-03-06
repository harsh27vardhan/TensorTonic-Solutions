import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    arr = np.array(x);
    data = 1/(1+np.exp(-arr))
    return data.tolist()