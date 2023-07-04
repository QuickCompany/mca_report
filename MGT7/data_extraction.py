class mgt7_data_extraction():
    def __init__(self):
        self.individual_hindu_undivided_family = {
                'Indian' : [] ,
                'non-resident Indian (NRI)': [] ,
                'Foreign national (other than NRI)' : []
            }

        self.government = {'Central Government' : [] , 'State Government' : [] , 'Government companies' : []}
        self.insurance_companies = []
        self.Banks = []
        self.Financial_institutions =  []
        self.Foreign_institutional_investors = []
        self.Mutual_funds = []
        self.Venture_capital = []
        self.Body_corporate = []
        self.Others = []
        self.Total = []


    def return_share_holding_data(self):
        data = {}
        data['Individual/Hindu Undivided Family'] = self.individual_hindu_undivided_family
        data['Government'] = self.government
        data['Insurance companies'] = self.insurance_companies
        data['Banks'] = self.Banks
        data['Financial institutions'] = self.Financial_institutions
        data['Foreign institutional investors'] = self.Foreign_institutional_investors
        data['Mutual funds'] = self.Mutual_funds
        data['Venture capital'] = self.Venture_capital
        data['Body corporate (not mentioned above)'] = self.Body_corporate
        data['Others'] = self.Others[1:]
        data['Total'] = self.Total

        return (data)

    def share_holding_data_merging(self,data , row):
        if '.Row2' in  row:
            self.individual_hindu_undivided_family['Indian'].append(data)
        if '.Row3' in  row:
            self.individual_hindu_undivided_family['non-resident Indian (NRI)'].append(data)
        if '.Row4' in  row:
            self.individual_hindu_undivided_family['Foreign national (other than NRI)'].append(data)
        if '.Row6' in  row:
            self.government['Central Government'].append(data)
        if '.Row7' in  row:
            self.government['State Government'].append(data)
        if '.Row8' in  row:
            self.government['Government companies'].append(data)
        if '.Row9' in  row:
            self.insurance_companies.append(data)
        if '.Row10' in  row:
            self.Banks.append(data)
        if '.Row11' in  row:
            self.Financial_institutions.append(data)
        if '.Row12' in  row:
            self.Foreign_institutional_investors.append(data)
        if '.Row13' in  row:
            self.Mutual_funds.append(data)
        if '.Row14' in  row:
            self.Venture_capital.append(data)
        if '.Row15' in  row:
            self.Body_corporate.append(data)
        if '.Row16' in  row:
            self.Others.append(data)
        if '.Row17' in  row:
            self.Total.append(data)


    def parse_share_holding(self,value_element):
        desired_value = value_element
        object_element = desired_value.getparent()  # Get the parent element
        dict_elements = object_element.findall('.//string')
        if len(dict_elements) >= 5:
            self.share_holding_data_merging(dict_elements[-1].text , dict_elements[-3].text)
        else:
            self.share_holding_data_merging(None , dict_elements[-2].text)

    def parse_string(self,value_element):
        desired_value = value_element
        object_element = desired_value.getparent()  # Get the parent element
        dict_elements = object_element.findall('.//string')
        if len(dict_elements) >= 5:
            return dict_elements[-1].text
        else:
            return None

    def parse_table(self,value_element):

        desired_value = value_element
        object_element = desired_value.getparent()
        dict_elements = object_element.findall('.//string')

        if len(dict_elements) >= 5:
            return dict_elements[-1].text

        else:
            return None


    def directors_data(self,table):
        directors_table = []
        for i in range(0,len(table),5):
            d = {}
            d['name'] = table[i]
            d['din/pan'] = table[i+1]
            d['designation'] = table[i+2]
            d['number_of_equity_shares_hold'] = table[i+3]
            d['date_of_cessation'] = table[i+4]

            directors_table.append(d)

        return directors_table