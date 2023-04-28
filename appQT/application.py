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
            i =+ 1
    return test

def plus_region (f) :
    test = True
    i = 0
    j = 0
    k = 0
    l = 0
    while (test) :
        try :
            e = load (f)
            if (e['regV']=='Tunis') :
                i =+ 1
            elif (e['regV']=='Sud de la Tunisie') :
                j =+ 1
            elif (e['regV']=='Nord-ouest de la Tunisie') :
                k =+ 1
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



    
def ajouter():
    f = open ('voyage.dat','ab')
    e = {}
    mat = w.mat.text()
    nomETprenom = w.nompnom.text()
    rIng = w.rIng
    rOuv = w.rOuv
    if rIng.isChecked :
        fct = 'Ingénieur'
    else :
        fct = 'Ouvrier'
    regV = w.regV.currentText()
    nbH = w.nbH.text()
    if not(alphanum(mat)) or len(mat) != 10 :
        print(alphanum(mat))
        QMessageBox.critical (w,'error','le mat doit etre un chaine alphanum de 10 caracteres ')
    elif len(nomETprenom) > 70 or len(nomETprenom) < 5 :
        QMessageBox.critical(w,'error','le nom et prenom doit etre un chaine entre 5 et 70 ')
    elif not(rIng.isChecked) and not(rOuv.isChecked) :
        QMessageBox.critical(w,'error','selecte un fonction ')
    elif w.rOuv.currentIndex() < 0 :
        QMessageBox.critical (w,'error','select un region de voyage ')
    elif num (nbH) or int(nbH) > 10 :
        QMessageBox.critical(w,'error','nb heure doit etre un entie supp de 10 ')
    else :
        e['mat'] = mat
        e['nomEtprenom'] = nomETprenom
        e['fct'] = fct
        e['regV'] = regV
        e['nbH'] = nbH
        dump(e,f)
        f.close()
        f = open('voyage.dat','rb')
        plus_region (f) # Procedur pour cherhcer le plus region choisi
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
            e = f.load ()
            w.tw.setItem(i,0,QTableWidgetItem(str(e['mat'])))
            w.tw.setItem(i,1,QTableWidgetItem(str(e['nomETprenom'])))
            w.tw.setItem(i,2,QTableWidgetItem(str(e['fct'])))
            w.tw.setItem(i,3,QTableWidgetItem(str(e['regV'])))
            w.tw.setItem(i,4,QTableWidgetItem(str(e['nbH'])))
            i =+ 1
        except :
            test = False
    f.close()

    


#------Exploitation de l'interface graphique------
app = QApplication([])
w = loadUi("interface.ui")
w.show()
w.mat.setFocus()
f = open ('voyage.dat','wb')
w.ajout.clicked.connect(ajouter)
w.aff.clicked.connect(afficher)
app.exec_()