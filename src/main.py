import pandas as pd

from src import functions

# load raw data
xpi_data = pd.read_csv('../data/XPI_data.csv')
aux_data = pd.read_csv('../data/AUX_data.csv')
perc_data = pd.read_csv('../data/PERC_data.csv')
www_data = pd.read_csv('../data/WWW_data.csv')

# get aux val from aux table (used for XPI computation)
aux_val = aux_data[aux_data.Type == '2021']['Value'].item()

# get percentages from percentages table

# fixed_rate used for fixed computation
fixed_rate = perc_data[perc_data.Ref == 'fixed']['Percentage'].item()

# perc_one and perc_two used for element percent increase computation (XPI+1.0%, XPI+2.0%, WWW+1.0%, WWW+2.0%)
perc_one = perc_data[perc_data.Ref == 'perc_one']['Percentage'].item()
perc_two = perc_data[perc_data.Ref == 'perc_two']['Percentage'].item()

# solution (see functions module)
solution_table = functions.compute_solution(xpi_data, www_data, aux_val, fixed_rate, perc_one, perc_two)
solution_table.to_csv('../data/solution_table.csv', index=False)

solution_reversed_rounded_table = solution_table.iloc[::-1].round(2)
solution_reversed_rounded_table.to_csv('../data/solution_reversed_rounded_table.csv', index=False)

print(solution_reversed_rounded_table)