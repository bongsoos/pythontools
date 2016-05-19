'''
arraytools.py

Manipulating arrays

author: Bongsoo Suh
created: 2016-05-18

(C) 2016 bongsoos
'''

import numpy as _np

def concate(arry, axis=0):
    '''
    arry (list)
        list of arrays to concatenate)
    axis (int)
    '''
    if len(arry)>1:
        for i in range(len(arry)):
            if i==0:
                c_array = arry[i]
            else:
                c_array = _np.concatenate((c_array, arry[i]), axis=axis)
    return c_array
