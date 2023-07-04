from lxml import etree
import os
import subprocess
from pdf_to_xml import dumps_pdf
from AOC.balance_sheet import balance_sheet
from AOC.profit_and_loss import profit_and_loss , print_all_data

key_mappings = {
    '.Segment2_1[0].Current[0]': 'FINANCIAL_YEAR_FROM',
    '.Segment2_1[0].CurrentTo[0]': 'FINANCIAL_YEAR_TO',
}

def parse_string(value_element):
    desired_value = value_element
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')
    if len(dict_elements) >= 5:
        return dict_elements[-1].text
    else:
        return None

def aoc_form(cin,file_name):
    data = {}

    dumps_pdf(cin,file_name)

    parser = etree.XMLParser(recover=True)
    tree = etree.parse(f'{cin}/{file_name}.xml', parser=parser)
    root = tree.getroot()

    for value_element in root.iter('value'):
        string_element = value_element.find('string')

        if string_element is not None:
            text = string_element.text

            if text:

                if ".BalanceSheet1_PartB[0]" in text:
                    data['balance_sheet'] = balance_sheet(value_element , text)

                if ".NumericField" in text:
                    profit_and_loss(value_element , text)

                else:
                    for key, value in key_mappings.items():
                        if key in text:
                            data[value] =  parse_string(value_element)
                            break

    data['statement of profit and loss'] = print_all_data()

    return data


# print(aoc_form('vikhil','Form AOC-4-14092022_signed.pdf'))

