from lxml import etree
import os
import subprocess
from AOC.balance_sheet import balance_sheet
from AOC.profit_and_loss import profit_and_loss , print_all_data

def dumps_pdf(cin,file_name):
    command = ['dumppdf.py', '-a', f'{cin}/{file_name}']

    output_file = f'{cin}/{file_name}.xml'

    # Open the output file in append mode ('a') and redirect the command output to it (stdout)
    with open(output_file, 'a') as file:
        subprocess.run(command, stdout=file, check=True)


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

            if text and ".BalanceSheet1_PartB[0]" in text:
                data['balance_sheet'] = balance_sheet(value_element , text)

            if text and ".NumericField" in text:
                profit_and_loss(value_element , text)

    data['statement of profit and loss'] = print_all_data()

    return data


# print(aoc_form('vikhil','Form AOC-4-14092022_signed.pdf'))

