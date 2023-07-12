import json

class Aoc():
    def __init__(self):
    #BALANCE SHEET

        self.BALANCE_SHEET = {
            "EQUITY_AND_LIABILITIES" : {
                "Shareholder's Fund": {
                    'Share capital': 'SHARE_CAPITAL_CR','Reserves and surplus': 'RESERVE_SURPLUS1','Money received against share warrants': 'MONEY_RECEIVD_CR'},
                'Share application money pending allotment': "SHARE_APP_MON_CR" ,
                'Non - current liabilities': {'Long term borrowings': 'LONG_TERM_BORR_C','Deferred tax liabilities (net)': 'DEFERRED_TL_CR','Other long term liabilities': 'OTHER_LNG_TRM_CR','Long term provisions': 'LONG_TERM_PROV_C'
                },
                'Current liabilities': {'Short term borrowings': 'SHORT_TERM_BOR_C','Trade payables': 'TRADE_PAYABLES_C','Other current liabilities': 'OTHER_CURR_LIA_C','Short term provisions': 'SHORT_TERM_PRO_C'
                },
                'equity_total' : 'TOTAL_CURR_REP'
                },
            "ASSETS" : {
                'Non-current assets': 
                {'Fixed assets': {
                'Tangible assets': 'TANGIBLE_ASSET_C',
                'Intangible assets': 'INTANGIBLE_AST_C',
                'Capital work-in-progress': 'CAPITAL_WIP_CR',
                'Intangible assets under development' : 'INTANGIBLE_AUD_C',
                },
                'Non-current Investments': 'NON_CURR_INV_CR','Deferred tax assets (net)': 'DEFERRED_TA_CR','Long term loans and advances' : 'LT_LOANS_ADV_CR','Other non-current assets' : 'OTHER_NON_CA_CR',
                },
                'current_assets': {'Current Investment': 'CURRENT_INV_CR','Inventories': 'INVENTORIES_CR','Trade receivables': 'TRADE_RECEIV_CR','Cash and cash equivalents' : 'CASH_AND_EQU_CR','Short term loans and advances' : 'SHORT_TRM_LOA_CR','Other current assets' : 'OTHER_NON_CA_CR',
                },
                'assets_total' : 'TOTAL_CURR_REP1'
                }
            }

        #profit and loss
        self.PROFIT_AND_LOSS = {
        "Revenue from operations" : {'Domestic Turnover':{
                                        'Sales of goods manufactured':'SALES_GOODS_CR',
                                        'Sales of goods traded':'SALES_GOODS_T_CR',
                                        'Sales or supply of services' : 'SALES_SUPPLY_CR',
                                },
                                'Export turnover':{
                                        'Sales of goods manufactured':'SALES_GOODS1_CR',
                                        'Sales of goods traded':'SALES_GOODS1_CR',
                                        'Sales or supply of services' : 'SALES_SUPPLY1_CR',
                                },
                                },
        "Other income" : 'OTHER_INCOME_CR',
        "Total Revenue (I+II)" : 'TOTAL_REVENUE_CR',
        "Expenses" : {
                    'Cost of material consumed' : 'COST_MATERIAL_CR',
                    'Purchases of stock in trade' : 'PURCHASE_STOCK_C',
                    'Changes in inventories of -Finished goods' : 'FINISHED_GOODS_C',
                    "-Work-in-progress" : 'WORK_IN_PROG_CR',
                    "-Stock-in-trade" : 'STOCK_IN_TRADE_C',
                    "Employee benefit Expense" : 'EMP_BENEFIT_EX_C',
                    "Managerial remuneration" :'MANGERIAL_REM_CR',
                    "Payment to Auditors" : 'PAYMENT_AUDTRS_C',
                    "Insurance expenses" : 'INSURANCE_EXP_CR',
                    "Power and fuel" : 'POWER_FUEL_CR',
                    "Finance cost" : 'FINANCE_COST_CR',
                    "Depreciation and Amortisation expense" : 'DEPRECTN_AMORT_C',
                    "Other expenses" : 'OTHER_EXPENSES_C',
                    "Total expenses" : 'TOTAL_EXPENSES_C',
        },
        "Profit before exceptional and extraordinary items and tax (III-IV)" : 'PROFIT_BEFORE_CR',
        "Exceptional items" : 'EXCEPTIONL_ITM_C',
        "Profit before extraordinary items and tax (V-VI)" : 'PROFIT_BEFORE_CR',
        "Extraordinary items" : 'EXTRAORDINARY_CR',
        "Profit before tax (VII-VIII)" : 'PROF_B_TAX_7_8_C',
        "Tax Expense" : {'Current tax' :'CURRENT_TAX_CR' , 'Deffered tax' : 'DEFERRED_TAX_CR'},
        "Profit (Loss) for the period from continuing Operations (IX-X)" : 'PROF_LOSS_OPER_C',
        "Profit/(Loss) from discontinuing operations" : 'PROF_LOSS_DO_CR',
        "Tax expense of dicontinuing operations" : 'TAX_EXPNS_DIS_CR',
        "Profit /(Loss) from discontinuing operations (after tax) (XII-XIII)" : 'PROF_LOS_12_13_C',
        "Profit/ (Loss) (XI+XIV)" : 'PROF_LOS_11_14_C',
        "Earnings per equity share before extraordinary items" : {'Basic' : 'BASIC_BEFR_EI_CR' , 'Diluted' : 'DILUTED_BEF_EI_C'},
        "Earnings per equity share after extraordinary items" : {'Basic' : 'BASIC_AFTR_EI_CR' , 'Diluted' : 'DILUTED_AFT_EI_C'},
        }
        
        self.data = {}

    def mapping_data(self,response):
        data_keys = self.data.keys()

        for key in response.keys():
            if type(response[key]) == dict: 
                for sub_key in response[key].keys():
                    if sub_key in data_keys:
                        response[key][sub_key] = self.data[sub_key]
            else:
                if key in data_keys:
                    response[key] = self.data[key]
            
        return response

    def map_data(self, response, table):
        def process_value(value):
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    value[sub_key] = process_value(sub_value)
            else:
                return response[value]
            return value

        for key, value in table.items():
            table[key] = process_value(value)

        print(table)
        return table
    
    def balance_sheet(self,form_fields):
        
        output = self.map_data(form_fields,self.BALANCE_SHEET)
        return output

    def profit_and_loss(self,form_fields):
        output = self.map_data(form_fields,self.PROFIT_AND_LOSS)
        return output
