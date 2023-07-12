from AOC.aoc import Aoc
import pikepdf
import sys
import os
import re
import xmltodict
import json



    
def aoc_form(xml):
    balance_sheet = Aoc()

    # # Convert XML to dictionary
    xml_dict = xmltodict.parse(xml)
    # # Convert dictionary to JSON
    json_data = json.dumps(xml_dict, indent=2)
    json_data = json.loads(json_data)
    # # Print the JSON data

    balance_sheet_output = balance_sheet.balance_sheet(json_data['xfa:datasets']['xfa:data']['data']['ZMCA_NCA_AOC_4'])
    profit_and_loss_output = balance_sheet.profit_and_loss(json_data['xfa:datasets']['xfa:data']['data']['ZMCA_NCA_AOC4_II'])
    
    output = {'BALANCE SHEET' : balance_sheet_output , "PROFIT AND LOSS" : profit_and_loss_output}

    return output
