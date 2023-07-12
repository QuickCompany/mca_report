# import pikepdf
# import sys
# import os
# import re
# import xmltodict
# import json

# class XfaObj(dict):
#     def __init__(self, sourcePdf):
#         self.source = sourcePdf
#         self.root = self.source.Root.AcroForm.XFA
#         self.xfaDict = {}
        
#         for i,item in enumerate(self.root):
#             if(i % 2 == 0 and isinstance(item,pikepdf.String)):
#                 #print(f'label {i}: {item}')
#                 label = f'{item}'
#                 self.xfaDict[label] = self.root[i+1]
#         #this next line is way more important/useful than it appears!
#         # it makes someone able to treat an XfaObj as a dict pretty much.
#         super(XfaObj,self).__init__(self.xfaDict)
         

#     def __getitem__(self,key):
#         if(isinstance(self.xfaDict[key],pikepdf.Stream)):
#             return self.xfaDict[key].read_bytes().decode('utf-8')
#         else:
#             print('xfa item detected was not a stream')
#             return self.xfaDict[key]

#     #note: pikepdf.Stream requires straight up bytes. 
#     def __setitem__(self,key,value):
#         if(isinstance(value,str)):
#             value = bytes(value,'utf-8')
#         self.xfaDict[key].write(value)

# fileName = '/root/mca_report/Form AOC-4-15022022.pdf'

# with pikepdf.Pdf.open(fileName) as pdfData:
#         xfaDict = XfaObj(pdfData)
#         for key in xfaDict.keys():
#             if key.lower() == 'datasets':
#                 xml = (xfaDict[key])
        
        
# # Convert XML to dictionary
# xml_dict = xmltodict.parse(xml)

# # Convert dictionary to JSON
# json_data = json.dumps(xml_dict, indent=2)

# # Print the JSON data
# print(json_data)



import PyPDF2 as pypdf

def read_acroform(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf = pypdf.PdfReader(pdf_file)
    form_data = {}

    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        annotations = page.get('/Annots', [])
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                field_name = annotation['/T']
                field_value = annotation['/V']

                # Resolve indirect references if necessary
                if isinstance(field_value, pypdf.generic.IndirectObject):
                    field_value = field_value.resolve()

                if field_name in form_data:
                    # Field name already exists, append the value to the list
                    form_data[field_name].append(field_value)
                else:
                    # Field name is encountered for the first time, create a new list
                    form_data[field_name] = [field_value]

    return form_data

# Example usage
pdf_path = '/root/mca_report/aoc_form/Form AOC-4-14092022_signed.pdf'
acroform_data = read_acroform(pdf_path)

# Print the extracted form field values
for field_name, field_values in acroform_data.items():
    print(f'{field_name}: {field_values}')
