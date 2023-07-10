class AocProfitLoss():
    def __init__(self) :
        #PROFIT AND LOSS
        self.REVENUE_FROM_OPERATIONS = {'Domestic Turnover':{
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

        self.OTHER_INCOME  = []
        self.TOTAL_REVENUE = []

        self.EXPENSES = {
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

        self.PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX = []
        self.EXCEPTIONAL_ITEMS = []
        self.PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX = []
        self.EXTRAORDINARY_ITEMS = []
        self.PROFIT_BEFORE_TAX = []

        self.TAX_EXPENSES = {'Current tax' : [] , 'Deffered tax' : []}

        self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS = []
        self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS = []

        self.TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS = []
        self.PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX = []
        self.PROFIT_LOSS = []

        self.EARNINGS_PER_EQUITY_SHARE_BREOFRE_EXTRAORDINARY_ITEMS = {'Basic' : [] , 'Diluted' : []}

        self.EARNINGS_PER_EQUITY_SHARE_AFTER_EXTRAORDINARY_ITEMS = {'Basic' : [] , 'Diluted' : []}

        self.data = {}

    def parse_string(self,value_element):
        desired_value = value_element
        object_element = desired_value.getparent()  # Get the parent element
        dict_elements = object_element.findall('.//string')
        if len(dict_elements) >= 5:
            return dict_elements[-1].text
        else:
            return None



    def profit_and_loss(self,value_text,text):

        desired_value = value_text
        object_element = desired_value.getparent()  # Get the parent element
        dict_elements = object_element.findall('.//string')

        # print(dict_elements[-2].text.replace('NumericField',''))

        if len(dict_elements) >= 5:
            if int(dict_elements[-2].text.replace('NumericField','')) in range(30,99):
                self.data[dict_elements[-2].text] = dict_elements[-1].text

            # return dict_elements[-1].text
        else:
            if int(dict_elements[-1].text.replace('NumericField','')) in range(30,99):
                self.data[dict_elements[-1].text] =  None

    def print_all_data(self,):
        sorted_data = sorted(self.data.items())

        profit_and_loss_data = {}

        print(sorted_data)

        # #REVENUE FROM OPERATION
        # for i in range(0,12):
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales of goods manufactured'].append(sorted_data[i][1])
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales of goods traded'].append(sorted_data[i][1])
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Domestic Turnover']['Sales or supply of services'].append(sorted_data[i][1])
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Export turnover']['Sales of goods manufactured'].append(sorted_data[i][1])
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Export turnover']['Sales of goods traded'].append(sorted_data[i][1])
        #     if i in range(0,2):
        #         self.REVENUE_FROM_OPERATIONS['Export turnover']['Sales or supply of services'].append(sorted_data[i][1])

        # #OTHER INCOME AND TOTAL INCOME
        # self.OTHER_INCOME.append(sorted_data[12][1])
        # self.OTHER_INCOME.append(sorted_data[13][1])
        # self.TOTAL_REVENUE.append(sorted_data[14][1])
        # self.TOTAL_REVENUE.append(sorted_data[15][1])

        # #EXPENSES
        # EXPENSES_KEY_LIST = list(self.EXPENSES.keys())
        # num = 16
        # for i in range(16,44,2):
        #     for j in range(0,2):
        #         self.EXPENSES[EXPENSES_KEY_LIST[i - num]].append(sorted_data[i + j][1])
        #     num+=1

        # for i in range(44,46):
        #     self.PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX.append(sorted_data[i][1])

        # for i in range(46,48):
        #     self.EXCEPTIONAL_ITEMS.append(sorted_data[i][1])

        # for i in range(48,50):
        #     self.PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX.append(sorted_data[i][1])

        # for i in range(50,52):
        #     self.EXTRAORDINARY_ITEMS.append(sorted_data[i][1])

        # for i in range(52,54):
        #     self.PROFIT_BEFORE_TAX.append(sorted_data[i][1])

        # #TAX EXPENSES
        # TAX_EXPENSES_KEY_LIST = list(self.TAX_EXPENSES.keys())
        # num = 54
        # for i in range(54,58,2):
        #     for j in range(0,2):
        #         self.TAX_EXPENSES[TAX_EXPENSES_KEY_LIST[i - num]].append(sorted_data[i + j][1])
        #     num+=1

        # for i in range(58,60):
        #     self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS.append(sorted_data[i][1])

        # for i in range(60,62):
        #     self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS.append(sorted_data[i][1])

        # for i in range(62,64):
        #     self.TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS.append(sorted_data[i][1])

        # for i in range(64,66):
        #     self.PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX.append(sorted_data[i][1])

        # for i in range(66,68):
        #     self.PROFIT_LOSS.append(sorted_data[i][1])

        # profit_and_loss_data['Revenue from operations'] = self.REVENUE_FROM_OPERATIONS
        # profit_and_loss_data['Other income'] = self.OTHER_INCOME
        # profit_and_loss_data['Total Revenue (I+II)'] = self.TOTAL_REVENUE
        # profit_and_loss_data['Expenses'] = self.EXPENSES
        # profit_and_loss_data['Profit before exceptional and extraordinary items and tax (III-IV)'] = self.PROFIT_BEFORE_EXCEPTIONAL_AND_EXTRAORDINARY_ITEMS_AND_TAX
        # profit_and_loss_data['Exceptional items'] = self.EXCEPTIONAL_ITEMS
        # profit_and_loss_data['Profit before extraordinary items and tax (V-VI)'] = self.PROFIT_BEFORE_EXTRAORINARY_ITEMS_AND_TAX
        # profit_and_loss_data['Extraordinary items'] = self.EXTRAORDINARY_ITEMS
        # profit_and_loss_data['Profit before tax (VII-VIII)'] = self.PROFIT_BEFORE_TAX
        # profit_and_loss_data['Tax Expenses'] = self.TAX_EXPENSES
        # profit_and_loss_data['(XI) Profit (Loss) for the period from continuing Operations (IX-X)'] = self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_CONTINUING_OPERATIONS
        # profit_and_loss_data['Profit/(Loss) from discontinuing operations'] = self.PROFIT_LOSS_FOR_THE_PERIOD_FROM_DISCONTINUING_OPERATIONS
        # profit_and_loss_data['Tax expense of discontinuing operations'] = self.TAX_EXPENSE_OF_DISCONTINUING_OPERATIONS
        # profit_and_loss_data['Profit /(Loss) from discontinuing operations (after tax) (XII-XIII)'] = self.PROFIT_LOSS_FROM_DISCONTINUING_OPERATIONS_AFTER_TAX
        # profit_and_loss_data['Profit/ (Loss) (XI+XIV)'] = self.PROFIT_LOSS
        # profit_and_loss_data['Earnings per equity share before extraordinary items'] = self.EARNINGS_PER_EQUITY_SHARE_BREOFRE_EXTRAORDINARY_ITEMS
        # profit_and_loss_data['Earnings per equity share after extraordinary items'] = self.EARNINGS_PER_EQUITY_SHARE_AFTER_EXTRAORDINARY_ITEMS

        # return (profit_and_loss_data)