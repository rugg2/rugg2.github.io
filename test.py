import tensorflow as tf
import pandas as pd 


def test_function(x, y=1, super_long_variable_name_to_test_black=12):
    # print(pwd)

    new = x + 1
    print(tf.VERSION)
    print(pd.__version__)
    new += 1
    # prout

    return new ** 3 + y - super_long_variable_name_to_test_black


test_function(x=9, y=2, super_long_variable_name_to_test_black=0)
print(test_function(2))
