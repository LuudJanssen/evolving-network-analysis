import os
import numpy


# Makes sure a certain folder exists
def make_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


# Saves a Pandas DataFrame as a CSV file
def dataframe_to_csv(dataframe, path, index):
    dataframe.to_csv(path, sep=';', decimal=',', index=index)


# Saves a Numpy array to a csv file
def ndarray_to_csv(array, path):
    numpy.savetxt(path, array, delimiter=",")
