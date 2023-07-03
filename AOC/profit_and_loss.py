#PROFIT AND LOSS
REVENUE_FROM_OPERATIONS = {'Domestic Turnover':{
                                'Sales of goods manufactured':[],
                                'Sales of goods traded':[],
                                'Sales or supply of services' : [],
                           },
                           'Export turnover':{
                                'Sales of goods manufactured':[],
                                'Sales of goods traded':[],
                                'Sales or supply of services' : [],
                           },
                           }

OTHER_INCOME  = []
TOTAL_REVENUE = []

EXPENSES = {
            'Cost of material consumed' : [],
            'Purchases of stock in trade' : [],
            'Changes in inventories of -Finished goods' : [],
            "-Work-in-progress" : [],
            "-Stock-in-trade" : [],
            "Employee benefit Expense" : [],
            "Managerial remuneration" :[] ,
            "Payment to Auditors" : [] ,
            "Insurance expenses" : [],
            "Power and fuel" : [],
            "Finance cost" : [],
            "Depreciation and Amortisation expense" : [],
            "Other expenses" : [],
            "Total expenses" : [],
}

PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX = []
EXCEPTIONAL_ITEMS = []
PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX = []
EXTRAORDINARY_ITEMS = []
PROFIT_BEFORE_TAX = []

TAX_EXPENSES = {'Current tax' : [] , 'Deffered tax' : []}

PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS = []
PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS = []

TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS = []
PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX = []
PROFIT_LOSS = []

EARNINGS_PER_EQUITY_SHARE_BREOFRE_EXTRAORDINARY_ITEMS = {'Basic' : [] , 'Diluted' : []}

EARNINGS_PER_EQUITY_SHARE_AFTER_EXTRAORDINARY_ITEMS = {'Basic' : [] , 'Diluted' : []}

def parse_string(value_element):
    desired_value = value_element
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')
    if len(dict_elements) >= 5:
        return dict_elements[-1].text
    else:
        return None

data = {}

def profit_and_loss(value_text,text):

    desired_value = value_text
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')

    # print(dict_elements[-2].text.replace('NumericField',''))

    if len(dict_elements) >= 5:
        if int(dict_elements[-2].text.replace('NumericField','')) in range(30,99):
            data[dict_elements[-2].text] = dict_elements[-1].text

        # return dict_elements[-1].text
    else:
        if int(dict_elements[-1].text.replace('NumericField','')) in range(30,99):
            data[dict_elements[-1].text] =  None

def print_all_data():
    sorted_data = sorted(data.items())

    profit_and_loss_data = {}

    #REVENUE FROM OPERATION
    for i in range(0,12):
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales of goods manufactured'].append(sorted_data[i][1])
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales of goods traded'].append(sorted_data[i][1])
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales or supply of services'].append(sorted_data[i][1])
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Export turnover']['Sales of goods manufactured'].append(sorted_data[i][1])
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Export turnover']['Sales of goods traded'].append(sorted_data[i][1])
        if i in range(0,2):
            REVENUE_FROM_OPERATIONS['Export turnover']['Sales or supply of services'].append(sorted_data[i][1])

    #OTHER INCOME AND TOTAL INCOME
    OTHER_INCOME.append(sorted_data[12][1])
    OTHER_INCOME.append(sorted_data[13][1])
    TOTAL_REVENUE.append(sorted_data[14][1])
    TOTAL_REVENUE.append(sorted_data[15][1])

    #EXPENSES
    EXPENSES_KEY_LIST = list(EXPENSES.keys())
    num = 16
    for i in range(16,44,2):
        for j in range(0,2):
            EXPENSES[EXPENSES_KEY_LIST[i - num]].append(sorted_data[i + j][1])
        num+=1

    for i in range(44,46):
        PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX.append(sorted_data[i][1])

    for i in range(46,48):
        EXCEPTIONAL_ITEMS.append(sorted_data[i][1])

    for i in range(48,50):
        PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX.append(sorted_data[i][1])

    for i in range(50,52):
        EXTRAORDINARY_ITEMS.append(sorted_data[i][1])

    for i in range(52,54):
        PROFIT_BEFORE_TAX.append(sorted_data[i][1])

    #TAX EXPENSES
    TAX_EXPENSES_KEY_LIST = list(TAX_EXPENSES.keys())
    num = 54
    for i in range(54,58,2):
        for j in range(0,2):
            TAX_EXPENSES[TAX_EXPENSES_KEY_LIST[i - num]].append(sorted_data[i + j][1])
        num+=1

    for i in range(58,60):
        PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS.append(sorted_data[i][1])

    for i in range(60,62):
        PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS.append(sorted_data[i][1])

    for i in range(62,64):
        TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS.append(sorted_data[i][1])

    for i in range(64,66):
        PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX.append(sorted_data[i][1])

    for i in range(66,68):
        PROFIT_LOSS.append(sorted_data[i][1])

    profit_and_loss_data['Revenue from operations'] = REVENUE_FROM_OPERATIONS
    profit_and_loss_data['Other income'] = OTHER_INCOME
    profit_and_loss_data['Total Revenue (I+II)'] = TOTAL_REVENUE
    profit_and_loss_data['Expenses'] = EXPENSES
    profit_and_loss_data['Profit before exceptional and extraordinary items and tax (III-IV)'] = PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX
    profit_and_loss_data['Exceptional items'] = EXCEPTIONAL_ITEMS
    profit_and_loss_data['Profit before extraordinary items and tax (V-VI)'] = PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX
    profit_and_loss_data['Extraordinary items'] = EXTRAORDINARY_ITEMS
    profit_and_loss_data['Profit before tax (VII-VIII)'] = PROFIT_BEFORE_TAX
    profit_and_loss_data['Tax Expenses'] = TAX_EXPENSES
    profit_and_loss_data['(XI) Profit (Loss) for the period from continuing Operations (IX-X)'] = PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS
    profit_and_loss_data['Profit/(Loss) from discontinuing operations'] = PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS
    profit_and_loss_data['Tax expense of discontinuing operations'] = TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS
    profit_and_loss_data['Profit /(Loss) from discontinuing operations (after tax) (XII-XIII)'] = PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX
    profit_and_loss_data['Profit/ (Loss) (XI+XIV)'] = PROFIT_LOSS
    profit_and_loss_data['Earnings per equity share before extraordinary items'] = EARNINGS_PER_EQUITY_SHARE_BREOFRE_EXTRAORDINARY_ITEMS
    profit_and_loss_data['Earnings per equity share after extraordinary items'] = EARNINGS_PER_EQUITY_SHARE_AFTER_EXTRAORDINARY_ITEMS

    return (profit_and_loss_data)