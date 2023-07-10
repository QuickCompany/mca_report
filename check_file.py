import pikepdf

pdf = pikepdf.open('/Users/vikhil/Desktop/quickcompany/mca_report/aoc_form/Form AOC-4-15022022.pdf')
pdf.save('my_good_pdf.pdf')


# import PyPDF2 as pypdf

# def find_in_dict(needle, haystack):
#     for key, value in haystack.items():
#         if key == needle:
#             return value
#         if isinstance(value, dict):
#             x = find_in_dict(needle, value)
#             if x is not None:
#                 return x

# pdf_path = '/Users/vikhil/Desktop/quickcompany/mca_report/aoc_form/Form AOC-4-20012021_signed.pdf'
# pdf_file = open(pdf_path, 'rb')
# pdf_reader = pypdf.PdfReader(pdf_file)

# trailer_dict = pdf_reader.trailer
# print(trailer_dict)
# xfa = find_in_dict('/XFA', trailer_dict)
# # print(xfa)
# # xml = xfa[7].get_object().getData()

# # print(xml)

# # pdf_file.close()




# import PyPDF2 as pypdf

# pdf_path = '/Users/vikhil/Desktop/quickcompany/mca_report/aoc_form/Form AOC-4-15022022.pdf'
# pdf_file = open(pdf_path, 'rb')
# pdf_reader = pypdf.PdfReader(pdf_file)

# form_fields = pdf_reader.get_form_text_fields()

# print(form_fields)


# pdf_file.close()


