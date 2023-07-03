from lxml import etree
import os
import subprocess

key_mappings = {
    '.Secretary1[0].PAN_C[0]': 'PAN',
    '.Secretary1[0].DIN_C[0]': 'DIN',
    '.ApptmtResig_R[0]' : 'appointment',
    '.CessationReason_C[0]' : 'cessation'
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

    if len(dict_elements) == 4:
        return dict_elements[-1].text
    else:
        return None

def dir12(cin,file_name):

    # dumps_pdf(cin,file_name)

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

dir12('U26943RJ1948PLC000612','Form DIR-12-02082019_signed')