from tkinter import filedialog, Tk


# Lets the user select a data file and returns the path
def select_data_file():
    Tk().withdraw()
    return filedialog.askopenfilename(title='Select data file')


# Saves a Pandas DataFrame as a CSV file
def dataframe_to_csv(dataframe, path):
    dataframe.to_csv(path, sep=';', decimal=',', index=False)
