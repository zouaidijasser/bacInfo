from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load

def alphanum(ch) :
    ch = ch.upper()
    i = 0
    test = True
    while (i < len(ch) and test) :
        if not(ch[i] >= '0' and ch[i] <= '9') and not(ch[i] >= 'A' and ch[i] <= 'Z') :
            test = False
        else :
            i += 1
    return test

def num (ch) :
    i = 0
    test = True
    while (i<len(ch) and test ) :
        if ch[i] > '9' or ch[i] < '0' :
            test = False
        else :
            i += 1
    return test

def plus_region () :
    f = open ('voyage.dat','rb')
    test = True
    i = 0
    j = 0
    k = 0
    l = 0
    while (test) :
        try :
            e = load (f)
            print(e['regV'])
            if (e['regV']=='Tunis') :
                i += 1
            elif (e['regV']=='Sud de la Tunisie') :
                j += 1
            elif (e['regV']=='Nord-ouest de la Tunisie') :
                k += 1
            else :
                l += 1
        except :
            test = False
    h = i
    if j > h :
        h = j
    if k > h :
        h = k
    if l > h :
        h = l
    if h == i :
        w.destV.setText('Tunis')
    elif h == j :
        w.destV.setText('Sud')
    elif h == k :
        w.destV.setText('Nord')
    else :
        w.destV.setText('Djerba')
    f.close()



    
def ajouter():
    f = open ('voyage.dat','ab')
    mat = w.mat.text()
    nomETprenom = w.nompnom.text()
    r1 = w.rIng
    r2 = w.rOuv
    regV = w.regV.currentText()
    nbH = w.nbH.text()
    if not(alphanum(mat)) or len(mat) != 10 :
        QMessageBox.critical (w,'error','le mat doit etre un chaine alphanum de 10 caracteres ')
    elif len(nomETprenom) > 70 or len(nomETprenom) < 5 :
        QMessageBox.critical(w,'error','le nom et prenom doit etre un chaine entre 5 et 70 ')
    elif r1.isChecked() == False and r2.isChecked() == False :
        QMessageBox.critical(w,'error','select un fonction ')
    elif not(num (nbH)) or nbH == '' :
        QMessageBox.critical(w,'error','nb heure doit etre un entie supp de 10 ')
    else :
        if r1.isChecked() :
            fct = 'Ingénieur'
        else :
            fct = 'Ouvrier'
        e = {}
        print(mat)
        print(nomETprenom)
        print(fct)
        print(regV)
        print(nbH)
        e['mat'] = mat
        e['nomETprenom'] = nomETprenom
        e['fct'] = fct
        e['regV'] = regV
        e['nbH'] = nbH
        dump(e,f)
        f.close()
        QMessageBox.information (w,'ajouter','le emp est ajouté ')
        w.mat.setText('')
        w.nompnom.setText('')
        w.rIng.setAutoExclusive(False)
        w.rIng.setChecked(False)
        w.rOuv.setAutoExclusive(False)
        w.rOuv.setChecked(False)
        w.regV.setCurrentIndex(0)
        w.nbH.setText('')
        w.mat.setFocus()


def afficher () :
    f = open ('voyage.dat','rb')
    test = True
    i = 0
    while test :
        try :
            e = load(f)
            print(e)
            w.tw.setItem(i,0, QTableWidgetItem (e['mat']))
            w.tw.setItem(i,1, QTableWidgetItem (e['nomETprenom']))
            w.tw.setItem(i,2, QTableWidgetItem (e['fct']))
            w.tw.setItem(i,3, QTableWidgetItem (e['regV']))
            w.tw.setItem(i,4, QTableWidgetItem (e['nbH']))
            i += 1
        except :
            test = False
    f.close()

    


#------Exploitation de l'interface graphique------
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.mat.setFocus()
w.tw.setColumnCount(5)
w.tw.setRowCount(60)
f = open ('voyage.dat','wb')
w.ajout.clicked.connect(ajouter)
w.aff.clicked.connect(afficher)
w.btn.clicked.connect(plus_region) # Procedur pour cherhcer le plus region choisi
app.exec_()