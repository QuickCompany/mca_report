from lxml import etree
import os
import subprocess

key_mappings = {
    '.chargcreaid_C[0]': 'charge_creation_identification_number',
    '.CHName_C[0]': 'name',
    '.CHAddress_C[0]' : 'address',
    '.NewDate_D[0]' : 'charge_creation_date',
    '.NewModDate_D[0]' : 'charge_last_modified_date',
    '.finalamtsec_N[0]' : 'final_amount_secured',
    '.datesatisfaction_D[0]' : 'date_of_satisfaction_of_charge_in_full',
    '.CLN_C[0]' : 'CIN'
}

data = {}

def dumps_pdf(cin,file_name):

    print("PDF TO XML")    

    if not os.path.exists(cin):
        os.makedirs(cin)

    command = ['dumppdf.py', '-a', f'{cin}/{file_name}.pdf']
    output_file = f'{cin}/{file_name}.xml'

    # Open the output file in append mode ('a') and redirect the command output to it (stdout)
    with open(output_file, 'a') as file:
        subprocess.run(command, stdout=file, check=True)

def parse_string(value_element):
    desired_value = value_element
    object_element = desired_value.getparent()  # Get the parent element
    dict_elements = object_element.findall('.//string')

    if len(dict_elements) >= 4:
        return dict_elements[-2].text
    else:
        return None

def form17(cin,file_name):

    dumps_pdf(cin,file_name)

    parser = etree.XMLParser(recover=True)
    tree = etree.parse(f'{cin}/{file_name}.xml', parser=parser)
    root = tree.getroot()

    for value_element in root.iter('value'):
        string_element = value_element.find('string')

        if string_element is not None:
            text = string_element.text
            if text:
                for key, value in key_mappings.items():
                    if key in text:
                        data[value] =  parse_string(value_element)
                        break

    print(data)

form17('U26943RJ1948SGC000612','Form 17-070608-ChargeId-80043520.PDF')