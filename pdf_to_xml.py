import os , subprocess

def dumps_pdf(cin,file_name):

    print("PDF TO XML")
    if not os.path.exists(cin):
        os.makedirs(cin)
    command = ['dumppdf.py', '-a', f'{cin}/{file_name}']
    output_file = f'{cin}/{file_name}.xml'
    # Open the output file in append mode ('a') and redirect the command output to it (stdout)
    with open(output_file, 'a') as file:
        subprocess.run(command, stdout=file, check=True)