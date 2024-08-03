"""
Array Row and column deletion.
"""

import numpy as np

if __name__ == "__main__":
     two_d_array = np.array([[1,2,3,4,5], [6,6,7,8,9], [10, 20, 30, 40, 50]], dtype=int)
     nuu_array = np.delete(two_d_array, 0, axis=0)
     nuw_two = np.delete(two_d_array, 1, axis=1)