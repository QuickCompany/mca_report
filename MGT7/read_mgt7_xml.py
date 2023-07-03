from lxml import etree
import subprocess
import os
from MGT7.data_extraction import parse_table , parse_string ,directors_data
from pdf_to_xml import dumps_pdf

table = []
data =  {}

key_mappings = {
    '.Page1[0].CIN[0]': 'CIN',
    '.Page1[0].PAN[0]': 'PAN',
    '.Page1[0].GLN[0]': 'GLN',
    '.Page1[0].Name[0]': 'NAME',
    '.Page1[0].Email[0]': 'EMAIL',
    '.Page1[0].Telephone[0]': 'TELEPHONE',
    '.Page1[0].Website[0]': 'WEBSITE',
    '.Page1[0].DateOfIncorporation': 'DATE_OF_INCORPORATION',
    '.FinancialYearFrom[0]': 'FINANCIAL_YEAR_FROM',
    '.FinancialYearTo[0]': 'FINANCIAL_YEAR_TO',
    '.DateOfAgm[0]': 'DATE_OF_AGM',
    '.DueDateAgm[0]': 'DUE_DATE_OF_AGM'
}


def mgt7_form(cin,file_name):
    dumps_pdf(cin,file_name)

    # Load the XML file
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(f'{cin}/{file_name}.xml', parser=parser)
    root = tree.getroot()

    for value_element in root.iter('value'):
        string_element = value_element.find('string')

        if string_element is not None:
            text = string_element.text
            if text:
                if ".SectionVIIIADynamic[0].Table13[0]" in text:
                    table.append(parse_table(value_element))

                else:
                    for key, value in key_mappings.items():
                        if key in text:
                            data[value] =  parse_string(value_element)
                            break

    data['directors'] = directors_data(table)

    return data

# print(parse_mgt7('U51909TG1998PLC029205','[14]_[04-Feb-2019]_Form MGT-7-04022019_signed'))
