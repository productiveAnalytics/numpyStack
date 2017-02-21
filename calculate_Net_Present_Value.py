import sys
import math
import numpy as np

from pprint import pprint

DEFAULT_RATE_OF_INTEREST = 10 # initial constant

# Matrix =
#           Income , Cost
#  year 0  [ 0     , 200  ]  <--- Initial income and Initial/Upfront Cost
#          | 50    , 100  |
#          | 100   , 50    |
#          [ 300   , 0    ]
yearwise_income_and_cost_matrix = np.matrix('0 200; 50 100; 100 50; 300 0')
#yearwise_income_and_cost_matrix = np.matrix('0 200; 50 100')


def process(cmd_args) -> None :
    if (cmd_args) :
        rate_of_interest = int(cmd_args[0])
        print('Rate of Interest = ', str(rate_of_interest))
    else :
        rate_of_interest = DEFAULT_RATE_OF_INTEREST
        print('Using *Default* Rate of Interest ', DEFAULT_RATE_OF_INTEREST)    
    
    pprint(yearwise_income_and_cost_matrix)
    npv = calc_Net_Present_Value (yearwise_income_and_cost_matrix, rate_of_interest)
    print('NPV = ', npv)
    

def calc_Present_Value (Future_Value : float, Rate_of_Return : float, year : int) -> float :
    ''' PV = FV / ((1 + r) ** n) '''
    denom = math.pow( (1 + Rate_of_Return/100) , year )
    #denom = ((1 + Rate_of_Return) ** year)
    return Future_Value / denom

def calc_Net_Present_Value(yearwise_income_and_cost_mat : np.matrix, rate_of_return: float) -> float :
    ''' Calculates Net Prsent Value
        i.e. sum (Present Value for incomes) - sum (Present Value for costs)
        across all the years, assuming constant Rate of Return
    '''
    shape_tup = yearwise_income_and_cost_mat.shape

    number_of_rows    = shape_tup[0]
    number_of_columns = shape_tup[1]

    if number_of_columns != 2 :
        print('The matrix must have TWO columns i.e. Income and Cost')
        print('Exiting...')
        return;

    # Row 0 represent initial income & cost.
    number_of_years = number_of_rows
    print('Number of years = ', number_of_years)

    sum_of_pv_of_income = 0
    sum_of_pv_of_cost = 0

    for year in range(number_of_years) :
        if year == 0 :
            sum_of_pv_of_income = yearwise_income_and_cost_mat.item(0,0)
            sum_of_pv_of_cost   = yearwise_income_and_cost_mat.item(0,1)
        else :
            income = yearwise_income_and_cost_mat.item(year,0)
            cost   = yearwise_income_and_cost_mat.item(year,1)
            print('For year {0}:\tIncome {1} \t Cost {2}'.format(year,income,cost))
            
            pv_income = calc_Present_Value(income, rate_of_return, year)
            pv_cost   = calc_Present_Value(cost, rate_of_return, year)
            print('For year {0} \t PV(income)= {1} \t PV(cost)= {2}'.format(year,pv_income,pv_cost))

            sum_of_pv_of_income += pv_income
            sum_of_pv_of_cost   += pv_cost

            print('Sum of PV of Income ', sum_of_pv_of_income)
            print('Sum of PV of Cost ', sum_of_pv_of_cost)
    
    return (sum_of_pv_of_income - sum_of_pv_of_cost)


if __name__ == "__main__":
   cmd_params_list = sys.argv[1:]
   print('Program arguments {0}'.format(cmd_params_list))
   process(cmd_params_list)
