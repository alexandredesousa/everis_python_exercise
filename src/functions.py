import pandas as pd

# functions as in excel
# for details on the functions implementation see the assumption in the README file.

def fixed_function(year_t1_val, fixed_rate):
    # computes an increase from t+1 (t1) of a given rate.
    return year_t1_val*(1+fixed_rate)

def xpi_function(aux_val, year_t, xpi_table):
    # computes a ratio between a base value (aux_val) and the average of the records for year_t, from table XPI.
    year_t_data = xpi_table[xpi_table.Year == year_t]
    year_average = year_t_data.iloc[:, 1].mean()
    return aux_val/year_average

def www_function(year_t, www_table):
    # ratio between the record for the last year, and year_t, from table WWW.
    last_www = www_table.iloc[-1, 1]
    current_www = www_table[www_table.Year == year_t].iloc[0, 1]
    return last_www/current_www

def element_percent_increase_function(percentage, preceding_element_t, preceding_element_t1):
    """
    Preceding element refers to the previous column - for instance,
    XPI+1.0% column uses data from the XPI column, whereas XPI+2.0% column uses data from the XPI+1.0% column,
    in each case, the preceding column; same holds true for the WWW derived computations.

    In any case, requires the preceding elements for the current (computation) year (t), and the following year
    (t+1, denoted t1 in the variable).

    :param percentage: the percentage computations just differ in the percentage used for the increment, thus also param.
    :param preceding_element_t: preceding element for the computation year.
    :param preceding_element_t1: preceding element for the computation's following year (t+1)
    :return: current year value added of a percentage increment from t+1 (float)
    """

    return preceding_element_t + preceding_element_t1 * percentage

def compute_solution(xpi_data, www_data, aux_val, fixed_rate, perc_one_rate, perc_two_rate):
    """
    Given all the raw data, computes the solution table.

    Considering the structure, for the last year presented (2021) the values are all set rather computed,
    making believe that these are in fact the initial conditions.
    The solution is then constructed based on that year, so the cycle runs from the year presented as last up to the first
    one in reverse order.

    :param xpi_data: XPI raw table
    :param www_data: WWW raw table
    :param aux_val: The base value from the AUX table (year 2021)
    :param fixed_rate: The rate to be used for the computation in the 'fixed' column
    :param perc_one_rate: The rate to be used for the xxx+1.0% columns.
    :param perc_two_rate: The rate to be used for the xxx+1.0% columns.
    :return: returns the solution table in the reverse order as presented in the docs, not rounded [pandas data frame]
    """

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

    return solution_df



