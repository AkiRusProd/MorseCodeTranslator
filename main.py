import sys,os
from PySide2 import QtCore, QtGui, QtWidgets
from PySideGUI import Ui_MainWindow

app=QtWidgets.QApplication(sys.argv)

MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()




en_dict = {

#   key:dict[key]

    'A': '.-',              'U': '..-',
    'B': '-...',            'V': '...-',
    'C': '-.-.',            'W': '.--',
    'D': '-..',             'X': '-..-',
    'E': '.',               'Y': '-.--',
    'F': '..-.',            'Z': '--..',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',             '1': '.----',        '.': '.-.-.-',        '=': '-...-',
    'L': '.-..',            '2': '..---',        ':': '---...',        '+': '.-.-.',
    'M': '--',              '3': '...--',        ';': '-.-.-.',        '-': '-....-',
    'N': '-.',              '4': '....-',        ',': '--..--',        '_': '..--.-',
    'O': '---',             '5': '.....',        '?': '..--..',        '"': '.-..-.',
    'P': '.--.',            '6': '-....',        '!': '-.-.--',        '$': '...-..-',
    'Q': '--.-',            '7': '--...',        '/': '-..-.',         '@': '.--.-.',
    'R': '.-.',             '8': '---..',        '(': '-.--.',         '¿': '..-.-',
    'S': '...',             '9': '----.',        ')': '-.--.-',        '¡': '--...-',
    'T': '-',               '0': '-----',        '&':'.-...',
    


}

ru_dict = {

#   key:dict[key]

    'А': '.-',              'У': '..-',          'Ч': '---.',
    'Б': '-...',            'Ж': '...-',         'Ш': '----',
    'Ц': '-.-.',            'В': '.--',          'Ъ': '--.--',
    'Д': '-..',             'Ь': '-..-',         'Э': '..-..',
    'Е': '.',               'Ы': '-.--',         'Ю': '..--',
    'Ф': '..-.',            'З': '--..',         'Я': '.-.-',
    'Г': '--.',             
    'Х': '....',            
    'И': '..',              
    'Й': '.---',
    'К': '-.-',             '1': '.----',        '.': '.-.-.-',        '=': '-...-',
    'Л': '.-..',            '2': '..---',        ':': '---...',        '+': '.-.-.',
    'М': '--',              '3': '...--',        ';': '-.-.-.',        '-': '-....-',
    'Н': '-.',              '4': '....-',        ',': '--..--',        '_': '..--.-',
    'О': '---',             '5': '.....',        '?': '..--..',        '"': '.-..-.',
    'П': '.--.',            '6': '-....',        '!': '-.-.--',        '$': '...-..-',
    'Щ': '--.-',            '7': '--...',        '/': '-..-.',         '@': '.--.-.',
    'Р': '.-.',             '8': '---..',        '(': '-.--.',         '¿': '..-.-',
    'С': '...',             '9': '----.',        ')': '-.--.-',        '¡': '--...-',
    'Т': '-',               '0': '-----',        '&':'.-...',          
    


}

dict=en_dict

def open_file():
    filename =QtWidgets.QFileDialog.getOpenFileName()

    if filename[0]:
        f = open(filename[0],'r')

        with f:
            data = f.read()
            ui.textEdit.setPlainText(data)
    

def save_1st_bar():
    try:
        filename = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "", "", "(*.txt)")[0]
        data =ui.textEdit.toPlainText()
        with open(filename, 'w') as f:
                    f.write(data)
                    f.close()
    except:
        pass
def save_2nd_bar():
    try:
        filename = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "", "", "(*.txt)")[0]
        data =ui.textEdit_2.toPlainText()
        with open(filename, 'w') as f:
                    f.write(data)
                    f.close()
    except:
        pass


def clear_all():
    ui.textEdit.clear()
    ui.textEdit_2.clear()

def decrypt(dict):
    
    temp=[]
    decr_text=[]
    
    text=ui.textEdit.toPlainText()
    temp=text.split(sep=' ')

    for i in range(len(temp)):
        if temp[i]=='':
                decr_text.append(' ')

        for key in dict:
            if temp[i]==dict[key]:
                decr_text.append(key)

    print(decr_text)
    convListToStr = ''.join([str(elem) for elem in decr_text]) 
    ui.textEdit_2.setPlainText(convListToStr)
    


def encrypt(dict):
   
    encr_text=[]
    text=str.upper(ui.textEdit.toPlainText())
    temp=list(text)
    print(temp)

    for i in range(len(temp)):
        if temp[i]==' ':
                encr_text.append(temp[i])

        for key in dict:
            if temp[i]==key:
                encr_text.append(dict[key])
    print(*encr_text)
    convListToStr = ' '.join([str(elem) for elem in encr_text]) 
    ui.textEdit_2.setPlainText(convListToStr)
    

    
def translate():
    
    ui.textEdit_2.clear()
    if ui.comboBox.currentIndex()==0:
        dict=en_dict
        
        print('en')
    else:
        dict=ru_dict
        
        print('ru')
    
    if ui.comboBox_2.currentIndex()==0:
        decrypt(dict)
    else:
        encrypt(dict)


    

    

ui.actionOpen.triggered.connect(open_file)
ui.actionText_from_1st_bar.triggered.connect(save_1st_bar)
ui.actionText_from_2nd_bar.triggered.connect(save_2nd_bar)

ui.pushButton.clicked.connect(translate)
ui.pushButton_2.clicked.connect(clear_all)





sys.exit(app.exec_())