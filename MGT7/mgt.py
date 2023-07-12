class Mgt():
    def __init__(self):

        self.SHARE_HOLDING_PATTERN_Promoters = {
        "Individual/Hindu Undivided Family" : {
                'Indian' : {'Equity':{'Number of shares':'NUM_ES_INDIAN','Percentage':'PER_ES_INDIAN'},
                           'Preference':{'Number of shares':'NUM_PS_INDIAN','Percentage':'PER_PS_INDIAN'}},
                'non-resident Indian (NRI)': {'Equity':{'Number of shares':'NUM_ES_NRI','Percentage':'PER_ES_NRI'},
                           'Preference':{'Number of shares':'NUM_PS_NRI','Percentage':'PER_PS_NRI'}
                            },
                'Foreign national (other than NRI)' : {'Equity':{'Number of shares':'NUM_ES_FN','Percentage':'PER_ES_FN'},
                           'Preference':{'Number of shares':'NUM_PS_FN','Percentage':'PER_PS_FN'}
                            },
            },
        
        "Government":{'Central Government' : {'Equity':{'Number of shares':'NUM_ES_CENT_GOV','Percentage':'PER_ES_CENT_GOV'},
                                            'Preference':{'Number of shares':'NUM_PS_CENT_GOV','Percentage':'PER_PS_CENT_GOV'}
                                                },
                    'State Government' :{'Equity':{'Number of shares':'NUM_ES_STAT_GOV','Percentage':'PER_ES_STAT_GOV'},
                                        'Preference':{'Number of shares':'NUM_PS_STAT_GOV','Percentage':'PER_PS_STAT_GOV'},
                                        }, 
                    'Government companies' : {'Equity':{'Number of shares':'NUM_ES_GOV_CMP','Percentage':'PER_ES_GOV_CMP'},
                                            'Preference':{'Number of shares':'NUM_PS_GOV_CMP','Percentage':'PER_PS_GOV_CMP'}
                                            },
        "Insurance companies" : {'Equity':{'Number of shares':'NUM_ES_INS_CMP','Percentage':'PER_ES_INS_CMP'},
                                            'Preference':{'Number of shares':'NUM_PS_INS_CMP','Percentage':'PER_PS_INS_CMP'}
                                            },},
        "Banks" : {'Equity':{'Number of shares':'NUM_ES_BANKS','Percentage':'PER_ES_BANKS'},
                           'Preference':{'Number of shares':'NUM_PS_BANKS','Percentage':'PER_PS_BANKS'}
                            },
        "Financial institutions" : {'Equity':{'Number of shares':'NUM_ES_FI','Percentage':'PER_ES_FI'},
                           'Preference':{'Number of shares':'NUM_PS_FI','Percentage':'PER_PS_FI'}
                            },
        "Financial institutions" : {'Equity':{'Number of shares':'NUM_ES_FI_INV','Percentage':'PER_ES_FI_INV'},
                            'Preference':{'Number of shares':'NUM_PS_FI_INV','Percentage':'PER_PS_FI_INV'}
                            },
        "Mutual funds" : {'Equity':{'Number of shares':'NUM_ES_MF','Percentage':'PER_ES_MF'},
                            'Preference':{'Number of shares':'NUM_PS_MF','Percentage':'PER_PS_MF'}
                            },
        "Venture capital" : {'Equity':{'Number of shares':'IN_NS_VEN_CAP','Percentage':'IN_PS_VEN_CAP'},
                            'Preference':{'Number of shares':'FRGN_NS_VEN_CAP','Percentage':'FRGN_PS_VEN_CAP'}
                            },
        "Body corporate (not mentioned above)" : {'Equity':{'Number of shares':'NUM_ES_BODY_COP','Percentage':'PER_ES_BODY_COP'},
                            'Preference':{'Number of shares':'NUM_PS_BODY_COP','Percentage':'PER_PS_BODY_COP'}
                            },
        "Others" : {'Equity':{'Number of shares':'NUM_ES_OTHR_SH','Percentage':'PER_ES_OTHR_SH'},
                            'Preference':{'Number of shares':'NUM_PS_OTHR_SH','Percentage':'PER_PS_OTHR_SH'}
                            },
        "Total" : {'Equity':{'Number of shares':'NUM_ES_TOTAL','Percentage':'PER_ES_TOTAL'},
                   'Preference':{'Number of shares':'NUM_PS_TOTAL','Percentage':'PER_PS_TOTAL'}
                            },
        "Total number of shareholders (promoters)" : 'TOT_NO_SHARE_HLD'
        }


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

        return table
    
    def share_holding_pattern_promoters(self,form_fields):
        output = self.map_data(form_fields,self.SHARE_HOLDING_PATTERN_Promoters)
        return output
