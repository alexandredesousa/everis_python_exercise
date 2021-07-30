import pandas as pd
from src import functions

xpi_data = pd.read_csv('../data/XPI_data.csv')
aux_data = pd.read_csv('../data/AUX_data.csv')
perc_data = pd.read_csv('../data/PERC_data.csv')
www_data = pd.read_csv('../data/WWW_data.csv')

# testing Fixed
fixed_rate = perc_data[perc_data.Ref == 'fixed']['Percentage'].item()
test_fixed_2000 = round(functions.fixed(1.81, fixed_rate), 2)
test_fixed_2009 = round(functions.fixed(1.38, fixed_rate), 2)

# testing XPI
aux_val = aux_data[aux_data.Type == '2021']['Value'].item()
test_XPI_2000 = round(functions.xpi_function(aux_val, 2000, xpi_data), 2)
test_XPI_2009 = round(functions.xpi_function(aux_val, 2009, xpi_data), 2)

# testing WWW
test_WWW_2000 = round(functions.www_function(2000, www_data), 2)
test_WWW_2009 = round(functions.www_function(2009, www_data), 2)

print(xpi_data.head)