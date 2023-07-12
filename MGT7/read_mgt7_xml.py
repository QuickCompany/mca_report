import pikepdf
import sys
import os
import re
import xmltodict
import json
from MGT7.mgt import Mgt


    
def mgt7_form(xml):
    mgt_form = Mgt()

    # # Convert XML to dictionary
    xml_dict = xmltodict.parse(xml)
    # # Convert dictionary to JSON
    json_data = json.dumps(xml_dict, indent=2)
    json_data = json.loads(json_data)


    # # Print the JSON data

    share_holding_pattern_promoters = mgt_form.share_holding_pattern_promoters(json_data['xfa:datasets']['xfa:data']['data']['ZMCA_NCA_MGT_7'])
    # profit_and_loss_output = mgt_form.profit_and_loss(json_data['xfa:datasets']['xfa:data']['data']['ZMCA_NCA_AOC4_II'])

    return share_holding_pattern_promoters

    # output = {'BALANCE SHEET' : balance_sheet_output , "PROFIT AND LOSS" : profit_and_loss_output}

    # return output
