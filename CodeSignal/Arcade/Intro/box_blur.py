import numpy as np
from scipy.ndimage import uniform_filter

def boxBlur(image):
    return np.round(uniform_filter(np.array(image).astype(float))[1:-1, 1:-1], decimals=10).astype(int)