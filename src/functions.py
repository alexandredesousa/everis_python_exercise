# functions as in excel
def fixed(year_t1_val, fixed_rate):
    return year_t1_val*(1+fixed_rate)

def xpi_function(aux_val, year_t, xpi_table):
    year_t_data = xpi_table[xpi_table.Year == year_t]
    #values = year_t_data.iloc[:, 1]
    #mean = values = year_t_data.iloc[:, 1].mean()
    year_average = year_t_data.iloc[:, 1].mean()
    return aux_val/year_average

def www_function(year_t, www_table):
    last_www = www_table.iloc[-1, 1]
    # current_www = www_table[www_table.Year == year_t]['Value'].item()
    # for some reason key value = 'Value' fails in this case. use iloc
    current_www = www_table[www_table.Year == year_t].iloc[0, 1]#.item()
    return last_www/current_www

def element_percent_increase_function(percentage, preceding_element_t, preceding_element_t1):
    ""
    return preceding_element_t + preceding_element_t1 * percentage
