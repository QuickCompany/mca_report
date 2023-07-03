from lxml import etree
import subprocess
import os

table = []

data =  {}

individual_hindu_undivided_family = {
        'indian' : [] ,
        'non-resident_Indian_(NRI)': [] ,
        'Foreign_national_(other_than_NRI)' : []
    }


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

def parse_string(value_element):
    desired_value = value_element
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')
    if len(dict_elements) >= 5:
        return dict_elements[-1].text
    else:
        return None



def parse_table(value_element):

    desired_value = value_element
    object_element = desired_value.getparent()
    dict_elements = object_element.findall('.//string')

    # for i in dict_elements:
    #     print(i.text)

    if len(dict_elements) >= 5:
        table.append(dict_elements[-1].text)

    else:
        table.append(None)

def directors_data(table):
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

def dumps_pdf(cin,file_name):

    print("PDF TO XML")
    if not os.path.exists(cin):
        os.makedirs(cin)
    command = ['dumppdf.py', '-a', f'{cin}/{file_name}.pdf']
    output_file = f'{cin}/{file_name}.xml'
    # Open the output file in append mode ('a') and redirect the command output to it (stdout)
    with open(output_file, 'a') as file:
        subprocess.run(command, stdout=file, check=True)

def parse_mgt7(cin,file_name):
    # dumps_pdf(cin,file_name)

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
                    parse_table(value_element)

                if '.SectionVI[0].Promotors[0]' in text:
                    print(parse_string(value_element))
                    # parse_string(value_element)
                        # individual_hindu_undivided_family['shareholders_fund']['share_capital'].append(value)

                else:
                    for key, value in key_mappings.items():
                        if key in text:
                            data[value] =  parse_string(value_element)
                            break



    data['directors'] = directors_data(table)

    # return data

print(parse_mgt7('U51909TG1998PLC029205','[14]_[04-Feb-2019]_Form MGT-7-04022019_signed'))
