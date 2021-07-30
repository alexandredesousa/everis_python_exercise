import pandas as pd

# functions as in excel
def fixed_function(year_t1_val, fixed_rate):
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

def compute_solution(xpi_data, www_data, aux_val, fixed_rate, perc_one_rate, perc_two_rate):

    head = ['year', 'fixed', 'xpi', 'xpi+1.0%', 'xpi+2.0%', 'www', 'www+1.0%', 'www+2.0%']
    solution_zero = [2021, 1.00, 1.00, 1.00, 1.00, www_function(2021, www_data),1.00, 1.00]

    computed_solution = [solution_zero]

    year_start = 2020
    year_end = 1990
    # year_end = 2018

    for i in range(year_start, year_end-1, -1):
        current_year = i

        # fixed
        fixed = fixed_function(computed_solution[-1][1], fixed_rate)

        # XPI
        xpi_current = xpi_function(aux_val, current_year, xpi_data)
        xpi_t1 = computed_solution[-1][2]
        xpi1p_current = element_percent_increase_function(perc_one_rate, xpi_current, xpi_t1)
        xpi1p_t1 = computed_solution[-1][3]
        xpi2p_current = element_percent_increase_function(perc_two_rate, xpi1p_current, xpi1p_t1)

        # WWW
        www_current = www_function(current_year, www_data)
        www_t1 = computed_solution[-1][5]
        www1p_current = element_percent_increase_function(perc_one_rate, www_current,www_t1)
        www1p_t1 = computed_solution[-1][6]
        www2p_current = element_percent_increase_function(perc_two_rate, www1p_current, www1p_t1)

        computed_solution.append([current_year,
                                  fixed,
                                  xpi_current, xpi1p_current, xpi2p_current,
                                  www_current, www1p_current, www2p_current])

    solution_df = pd.DataFrame(computed_solution, columns=head)

    print("almost there")



