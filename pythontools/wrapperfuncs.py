import numpy as np
import time

def parent(num):
    def first_child():
        return 'printing from first child'
    def second_child():
        return 'printing from second child'
    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child


def my_decorator(func):
    def wrapper():
        num=10
        if num==10:
            print 'yes!'
        else:
            print 'no!'
        func()
        print 'something is happening after some_function() is called'
    return wrapper

def tempfunc():
    print 'wheee!'



def timing_function(func):
    '''
    Returns execution time
    '''
    def wrapper():
        start_time = time.time()
        start_localtime = time.asctime(time.localtime(start_time))
        func()
        end_time = time.time()
        end_localtime = time.asctime(time.localtime(end_time))
        print 'start time: ', start_localtime
        print 'end time: ', end_localtime
        print 'Run-Time: %10.4f minutes\n' %((end_time-start_time)/60)
        return
    return wrapper

def sleep_decorator(func):
    '''
    Limits how fast the function is called
    '''
    def wrapper(*args, **kwargs):
        time.sleep(2)
        return func(*args, **kwargs)
    return wrapper

from functools import wraps
#from flask 

@timing_function
def tempfunc1():
    num_list = []
    for num in range(10000):
        num_list.append(num)
    print('\nSum of all the numbers: '+str((sum(num_list))))

@sleep_decorator
def print_number(num):
    return num

'''
class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
'''


class Celsius(object):
    def __init__(self, temperature = 0):
        self._temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value



