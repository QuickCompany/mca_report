from flask import Flask, render_template , request 
from AOC.read_aoc_xml import aoc_form
from MGT7.read_mgt7_xml import mgt7_form
import os
from io import BytesIO
import pikepdf
from AOC.aoc import Aoc



app = Flask(__name__)


if not os.path.exists("file"):
    os.makedirs("file")

class XfaObj(dict):
    def __init__(self, sourcePdf):
        self.source = sourcePdf
        self.root = self.source.Root.AcroForm.XFA
        self.xfaDict = {}
        
        for i,item in enumerate(self.root):
            if(i % 2 == 0 and isinstance(item,pikepdf.String)):
                #print(f'label {i}: {item}')
                label = f'{item}'
                self.xfaDict[label] = self.root[i+1]
        #this next line is way more important/useful than it appears!
        # it makes someone able to treat an XfaObj as a dict pretty much.
        super(XfaObj,self).__init__(self.xfaDict)
         

    def __getitem__(self,key):
        if(isinstance(self.xfaDict[key],pikepdf.Stream)):
            return self.xfaDict[key].read_bytes().decode('utf-8')
        else:
            print('xfa item detected was not a stream')
            return self.xfaDict[key]

    #note: pikepdf.Stream requires straight up bytes. 
    def __setitem__(self,key,value):
        if(isinstance(value,str)):
            value = bytes(value,'utf-8')
        self.xfaDict[key].write(value)

def pdf_to_xml(file_name):
    with pikepdf.Pdf.open(file_name) as pdfData:
        xfaDict = XfaObj(pdfData)
        for key in xfaDict.keys():
            if key.lower() == 'datasets':
                xml = (xfaDict[key])

    return xml

@app.route('/mgt7',methods=['GET' , 'POST'])
def MGT7():
    File = request.files['file']
    filename = File.filename
    cin = request.form['cin']
    if not os.path.exists(cin):
        os.makedirs(cin)

    filename = f'{cin}/{filename}'
    File.save(filename)
    
    xml = pdf_to_xml(filename)

    if "mgt-7" in filename.lower():
        return mgt7_form(xml)

    return "200"

@app.route('/aoc',methods=['GET' , 'POST'])
def aoc():
    File = request.files['file']
    filename = File.filename
    cin = request.form['cin']

    if not os.path.exists(cin):
        os.makedirs(cin)

    filename = f'{cin}/{filename}'
    File.save(filename)

    xml = pdf_to_xml(filename)
    
    os.remove(filename)

    if 'aoc' in filename.lower():
        return aoc_form(xml)

    return "200"

if __name__ == '__main__':
    app.run(debug=True , port = 8097 , host = "0.0.0.0")
