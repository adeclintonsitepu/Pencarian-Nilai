#import libraries
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
import gspread

connect = gspread.service_account(filename=('service_account.json'))

# Connection to filename spreadsheet
sheetname = connect.open('test')

# Connection to Sheet spreadsheet
worksheetname = sheetname.worksheet('Sheet2')
worksheetnilai = sheetname.worksheet('Sheet1')

#Initialize the flask App
app = Flask(__name__)

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button
@app.route('/cari',methods=['POST'])
def cari():
    '''
    For rendering results on HTML GUI
    '''
    int_features = []
    int_features = [x for x in request.form.values()]
    
    input_Username = int_features[0]
    input_Password = int_features[1]

    find_Username = worksheetname.find(query=input_Username,in_column=1)
    
    if find_Username:
        find_Password = worksheetname.cell(int(find_Username.row), 3).value
        find_Nilai = worksheetnilai.find(query=input_Username, in_column=1)
        nilai = worksheetnilai.row_values(find_Nilai.row)
        
        Nama_mahasiswa = nilai[1]
        NIM_Mahasiswa = nilai[0]
        Prodi_Mahasiswa = nilai[2]
        Nilai_Akhir = nilai[-2]
        Grade = nilai[-1]
        nilai = nilai[3:-2]
        range = int(len(nilai))

        header_table = worksheetnilai.row_values(1)
        header_table = header_table[3:-2]

        if (find_Password == input_Password):
            return render_template('Tabel.html', Nilai=nilai, Header=header_table, Nama=Nama_mahasiswa, NIM=NIM_Mahasiswa, Prodi=Prodi_Mahasiswa, Range=range, nilaiAkhir=Nilai_Akhir, grade=Grade)
        
        return render_template('index.html', Error = 'Password Salah', Username=input_Username, Password = input_Password)
    
    return render_template('index.html', Error = 'Username Salah', Username=input_Username, Password = input_Password)   

if __name__ == "__main__":
    app.run(debug=True)