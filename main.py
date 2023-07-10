from flask import Flask, render_template , request
from AOC.read_aoc_xml import aoc_form
from MGT7.read_mgt7_xml import mgt7_form
import os
import pdfrw


app = Flask(__name__)

if not os.path.exists("file"):
    os.makedirs("file")


@app.route('/mgt7',methods=['GET' , 'POST'])
def MGT7():
    File = request.files['file']
    name = File.filename
    cin = request.form['cin']
    if not os.path.exists(cin):
        os.makedirs(cin)

    File.save(f'{cin}/{name}')

    if "mgt-7" in name.lower():
        return mgt7_form(cin,name)

    return "200"

@app.route('/aoc',methods=['GET' , 'POST'])
def aoc():
    File = request.files['file']
    name = File.filename
    cin = request.form['cin']
    if not os.path.exists(cin):
        os.makedirs(cin)

    filename = f'{cin}/{name}'

    File.save(filename)

    if "aoc" in name.lower():
        pdf = pdfrw.PdfReader(filename)

        print(pdf)

        # Check if the PDF contains XFA data
        if "/XFA" in pdf.keys():
            # Extract XFA data
            xfa_data = pdf['/XFA'].decode('utf-8')
            print("XFA Data:")
            print(xfa_data)
        else:
            return aoc_form(cin,name)

    return "200"

if __name__ == '__main__':
    app.run(debug=True , port = 8097 , host = "0.0.0.0")
