import pandas as pd

# load workbook
workbook = pd.read_excel("../data/python_assessment_data.xlsx")

## get XPI raw table
# XPI_data = pd.read_excel("../docs/python_assessment_data.xlsx", index_col=[11,12])
XPI_data = workbook.iloc[1:376, 11:13]
XPI_data.columns = XPI_data.iloc[0]
XPI_data = XPI_data[1:]

## get WWW raw table
WWW_data = workbook.iloc[1:39, 14:16]
WWW_data.columns = WWW_data.iloc[0]
WWW_data = WWW_data[1:]

## get AUX raw table
AUX_data = workbook.iloc[3:6, 8:10]
AUX_data.columns = ['Type', 'Value']

# percentages data - considering the simplicity of the data, will manually create it
# note: there is a percentage to apply for the 'fixed' column,
# and two percentages to apply to either 'XPI +1.0%' and 'XPI +2.0%', or to 'WWW +1.0%' and 'WWW +2.0%'.
# as such, for the dataframe to be created, will use the reference 'fixed', 'perc_one' and 'perc_two',
# with the corresponding percentage column values.
percentages_data = [['fixed', 0.030], ['perc_one', 0.010], ['perc_two', 0.020]]
PERC_df = pd.DataFrame(percentages_data, columns=['Ref', 'Percentage'])

## save raw data to be used in calculations
XPI_data.to_csv('../data/XPI_data.csv', index=False)
WWW_data.to_csv('../data/WWW_data.csv', index=False)
AUX_data.to_csv('../data/AUX_data.csv', index=False)
PERC_df.to_csv('../data/PERC_data.csv', index=False)
