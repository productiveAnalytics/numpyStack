import sys
import math
import numpy as np

from pprint import pprint

DEFAULT_RATE_OF_INTEREST = 10 # initial constant
PRECISON = 4

# Matrix =
#           Income , Cost
#  year 0  [ 0     , 200  ]  <--- Initial income and Initial/Upfront Cost
#          | 50    , 100  |
#          | 100   , 50   |
#          [ 300   , 0    ]
yearwise_income_and_cost_matrix = np.matrix('0 200; 50 100; 100 50; 300 0')


def process(cmd_args) -> None :
    matrix_provided_flg = False
    # Set the Rate of Interest - either from command parameter or use Default
    if (cmd_args) :
        rate_of_interest = float(cmd_args[0])
        print('Rate of Interest = ', str(rate_of_interest))

        if (len(cmd_args) > 1) :
            matrix_input_str = cmd_args[1]
            try :
                yearwise_income_and_cost_matrix = np.matrix(matrix_input_str)
                matrix_provided_flg = True
            except ValueError as valErr:
                print(valErr)
                print('Unable to parse the Income & Cost matrix')
                print('Exiting...')
                raise SystemExit
    else :
        rate_of_interest = DEFAULT_RATE_OF_INTEREST
        print('Using *Default* Rate of Interest ', DEFAULT_RATE_OF_INTEREST)    

    print('Using matrix provided by ', 'User' if matrix_provided_flg else 'System')
    pprint(yearwise_income_and_cost_matrix)
    
    npv = calc_Net_Present_Value (yearwise_income_and_cost_matrix, rate_of_interest)
    print('NPV = ', npv)
    

def calc_Present_Value (Future_Value : float, Rate_of_Return : float, year : int) -> float :
    ''' PV = FV / ((1 + r) ** n) '''
    denom = math.pow( (1 + Rate_of_Return/100) , year )

    # Round to four decimal places
    return round(Future_Value / denom, PRECISON)

def calc_Net_Present_Value(yearwise_income_and_cost_mat : np.matrix, rate_of_return: float) -> float :
    ''' Calculates Net Prsent Value
        i.e. sum (Present Value for incomes) - sum (Present Value for costs)
        across all the years, assuming constant Rate of Return
    '''

    # Confirm the Matrix has correct shape i.e. N_No_of_Rows x Exactly 2 Columns
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
            
    print()
    sum_of_pv_of_income = round(sum_of_pv_of_income, PRECISON)
    sum_of_pv_of_cost   = round(sum_of_pv_of_cost, PRECISON)
    print('Total PV of Income = ', sum_of_pv_of_income)
    print('Total PV of Cost   = ', sum_of_pv_of_cost)

    net_present_value = (sum_of_pv_of_income - sum_of_pv_of_cost)
    return round(net_present_value, PRECISON)


if __name__ == "__main__":
   print('Usage:')
   print('  py calculate_Net_Present_Value.py <Rate_of_Interest> <Income_Cost_matrix_representation_surrounded_by_Double_Quotes>')
   print('  e.g py calculate_Net_Present_Value.py 10 "0 200; 50 100; 100 50; 300 0"')
   print()
   cmd_params_list = sys.argv[1:]
   print('Program arguments {0}'.format(cmd_params_list))
   process(cmd_params_list)
