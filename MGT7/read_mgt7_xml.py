from lxml import etree
import subprocess
import os
from MGT7.data_extraction import mgt7_data_extraction
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

def xml_parsing(root,param):
    mgt_class  = mgt7_data_extraction()
    for value_element in root.iter('value'):
        string_element = value_element.find('string')

        if string_element is not None:
            text = string_element.text
            if text:
                if not param:
                    if ".SectionVIIIADynamic[0].Table13[0]" in text:
                        table.append(mgt_class.parse_table(value_element))

                    if 'data[0].FormMGT7_Dtls[0].MainPage[0].SectionVI[0].Promotors[0].Table9[0]' in text:
                        mgt_class.parse_share_holding(value_element)

                    else:
                        for key, value in key_mappings.items():
                            if key in text:
                                data[value] =  mgt_class.parse_string(value_element)
                                break
                else:
                    if 'data[0].FormMGT7_Dtls[0].MainPage[0].SectionVI[0].Public[0].Table9[0]' in text:
                        mgt_class.parse_share_holding(value_element)

    if not param:
        data['directors'] = mgt_class.directors_data(table)
        data['SHARE HOLDING PATTERN - Promoters (not applicable for OPC)'] = mgt_class.return_share_holding_data()
    else:
        data['SHARE HOLDING PATTERN - Public/Other than promoters '] = mgt_class.return_share_holding_data()


def mgt7_form(cin,file_name):
    dumps_pdf(cin,file_name)

    # Load the XML file
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(f'{cin}/{file_name}.xml', parser=parser)
    root = tree.getroot()

    xml_parsing(root,False)
    xml_parsing(root,True)

    os.remove(f'{cin}/{file_name}')
    os.remove(f'{cin}/{file_name}.xml')

    return data

# print(parse_mgt7('U51909TG1998PLC029205','[14]_[04-Feb-2019]_Form MGT-7-04022019_signed'))
