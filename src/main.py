import pandas as pd
from src import functions

# raw data
xpi_data = pd.read_csv('../data/XPI_data.csv')
aux_data = pd.read_csv('../data/AUX_data.csv')
perc_data = pd.read_csv('../data/PERC_data.csv')
www_data = pd.read_csv('../data/WWW_data.csv')

aux_val = aux_data[aux_data.Type == '2021']['Value'].item()

fixed_rate = perc_data[perc_data.Ref == 'fixed']['Percentage'].item()
perc_one = perc_data[perc_data.Ref == 'perc_one']['Percentage'].item()
perc_two = perc_data[perc_data.Ref == 'perc_two']['Percentage'].item()

functions.compute_solution(xpi_data, www_data, aux_val, fixed_rate, perc_one, perc_two)