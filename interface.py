from PySide2.QtWidgets import QApplication, QFrame, QLabel, QPushButton , QWidget
from PySide2.QtWidgets import QLineEdit
from pymongo import MongoClient
client = MongoClient()
client
client = MongoClient(host="localhost", port=27017)

db = client.alunoCad
db
banco = db.banco
banco

import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("janela do sistema")
        self.setGeometry(300, 300, 1000, 700)
       
        self.setToolTip("cad de alunos e adm de notas")

        self.setStyleSheet('background-color: rgb(7,104,114)')



        self.janela_principal()
        




    def janela_principal(self):

        #BOTAO QUE ABRE FRAME DE ADICIONAR 
        self.btn_adicionar = QPushButton('adicionar', self)
        self.btn_adicionar.setGeometry(0,0,170,50)
        self.btn_adicionar.setStyleSheet('color: rgb(255,255,255)')
        self.btn_adicionar.clicked.connect(self.exibir_area_adicionar)

        #BOTAO QUE ABRE FRAME DE EDITAR
        self.btn_editar = QPushButton('editar', self)
        self.btn_editar.setGeometry(0,50,170,50)
        self.btn_editar.setStyleSheet('color: rgb(255,255,255)')
        self.btn_editar.clicked.connect(self.exibir_area_editar)

        #BOTAO QUE ABRE FRAME DE PESQUISAR
        self.btn_pesquisar = QPushButton('pesquisar', self)
        self.btn_pesquisar.setGeometry(0,100,170,50)
        self.btn_pesquisar.setStyleSheet('color: rgb(255,255,255)')
        self.btn_pesquisar.clicked.connect(self.exibir_area_pesquisar)

        #BOTAO QUE ABRE FRAME DE DELETAR
        self.btn_deletar = QPushButton('deletar', self)
        self.btn_deletar.setGeometry(0,150,170,50)
        self.btn_deletar.setStyleSheet('color: rgb(255,255,255)')
        self.btn_deletar.clicked.connect(self.exibir_area_deletar)


#============================frames==================================



        #FRAME DE ADICIONAR (OCULTO E SO APARECE QUANDO CLICA NO BOTÃO ADICIONAR)
        global frm_adicionar
        self.frm_adicionar = QFrame(self)
        self.frm_adicionar.setGeometry(170,0,830,700)
        self.frm_adicionar.setStyleSheet('background-color: rgb(255,255,255)')
        self.frm_adicionar.setVisible(False)


        #elementos do frame ADICIONAR:

        self.lbl_adicionar=QLabel('Nome', self.frm_adicionar)
        self.lbl_adicionar.setGeometry(20, 50, 55, 16)

        self.lbl_nota1=QLabel('Nota 1',self.frm_adicionar)
        self.lbl_nota1.setGeometry(20, 90, 55, 16)

        self.lbl_nota2=QLabel('Nota 2',self.frm_adicionar)
        self.lbl_nota2.setGeometry(20, 130, 55, 16)

        global txt_nome
        self.txt_nome = QLineEdit(self.frm_adicionar)
        self.txt_nome.setGeometry(80,50,721,22)

        global txt_nota1
        self.txt_nota1 = QLineEdit(self.frm_adicionar)
        self.txt_nota1.setGeometry(80,90,721,22)

        global txt_nota2
        self.txt_nota2 = QLineEdit(self.frm_adicionar)
        self.txt_nota2.setGeometry(80,130,721,22)

        self.btn_limpar = QPushButton('Limpar', self.frm_adicionar)
        self.btn_limpar.setGeometry(20,650,115,22)
        self.btn_limpar.clicked.connect(self.limpar_add)

        self.btn_gravar = QPushButton('Gravar', self.frm_adicionar)
        self.btn_gravar.setGeometry(700,650,115,22)
        self.btn_gravar.clicked.connect(self.add_mongo)
        

        #FRAME DE EDITAR (OCULTO E SO APARECE QUANDO CLICA NO BOTÃO ADICIONAR)
        global frm_editar
        self.frm_editar = QFrame(self)
        self.frm_editar.setGeometry(170,0,830,700)
        self.frm_editar.setStyleSheet('background-color: rgb(255,255,255)')
        self.frm_editar.setVisible(False)
        

        #elementos do frame :editar
        global campo_busca
        self.campo_busca = QLineEdit(self.frm_editar)
        self.campo_busca.setGeometry(20,20,800,22)
        self.campo_busca.setPlaceholderText('000.000.000.000')


        self.lbl_adicionar_edit=QLabel('Nome', self.frm_editar)
        self.lbl_adicionar_edit.setGeometry(20, 50, 55, 16)

        self.lbl_nota1_edit=QLabel('Nota 1',self.frm_editar)
        self.lbl_nota1_edit.setGeometry(20, 90, 55, 16)

        self.lbl_nota2_edit=QLabel('Nota 2',self.frm_editar)
        self.lbl_nota2_edit.setGeometry(20, 130, 55, 16)

        global txt_nome_edit
        self.txt_nome_edit = QLineEdit(self.frm_editar)
        self.txt_nome_edit.setGeometry(80,50,721,22)

        global txt_nota1_edit
        self.txt_nota1_edit = QLineEdit(self.frm_editar)
        self.txt_nota1_edit.setGeometry(80,90,721,22)

        global txt_nota2_edit
        self.txt_nota2_edit = QLineEdit(self.frm_editar)
        self.txt_nota2_edit.setGeometry(80,130,721,22)

        self.btn_limpar_edit = QPushButton('Limpar', self.frm_editar)
        self.btn_limpar_edit.setGeometry(20,650,115,22)
        self.btn_limpar_edit.clicked.connect(self.limpar_editar)

        self.btn_gravar_edit = QPushButton('Gravar', self.frm_editar)
        self.btn_gravar_edit.setGeometry(700,650,115,22)
        self.btn_gravar_edit.clicked.connect(self.editar_aluno)

        #FRAME DE PESQUISAR (OCULTO E SO APARECE QUANDO CLICA NO BOTÃO ADICIONAR)
        global frm_pesquisar
        self.frm_pesquisar = QFrame(self)
        self.frm_pesquisar.setGeometry(170,1,830,700)
        self.frm_pesquisar.setStyleSheet('background-color: rgb(255,255,255)')
        self.frm_pesquisar.setVisible(False)


        #elementos do frame PESQUISAR:
        self.lbl_nome = QLabel('nome', self.frm_pesquisar)
        self.lbl_nome.setGeometry(20,50,55,16)

        global txt_nome01
        self.txt_nome01 = QLineEdit (self.frm_pesquisar)
        self.txt_nome01.setGeometry(80,50,600,22)
        


        self.btn_pesquisar01 = QPushButton('Pesquisar', self.frm_pesquisar)
        self.btn_pesquisar01.setGeometry(700,50,80,22)
        self.btn_pesquisar01.clicked.connect(self.pesquisa_aluno)

        global lbl_infos
        self.lbl_infos=QLabel("dados",self.frm_pesquisar)
        self.lbl_infos.setGeometry(350,150,915,10)
        self.lbl_infos.setVisible(False)

        self.btn_limpar_pesquisa = QPushButton('limpar', self.frm_pesquisar)
        self.btn_limpar_pesquisa.setGeometry(700,650,115,22)
        self.btn_limpar_pesquisa.clicked.connect(self.limpa_pesquisa)



        #FRAME DE DELETAR (OCULTO E SO APARECE QUANDO CLICA NO BOTÃO ADICIONAR)
        global frm_deletar
        self.frm_deletar = QFrame(self)
        self.frm_deletar.setGeometry(170,0,830,700)
        self.frm_deletar.setStyleSheet('background-color: rgb(255,255,255)')
        self.frm_deletar.setVisible(False)

         #elementos do frame deletar:

        self.lbl_nome_delete = QLabel('nome', self.frm_deletar)
        self.lbl_nome_delete.setGeometry(20,50,55,16)

        global txt_nome_delete
        self.txt_nome_delete = QLineEdit (self.frm_deletar)
        self.txt_nome_delete.setGeometry(80,50,600,22)

        self.btn_deletar_delete = QPushButton('Deletar', self.frm_deletar)
        self.btn_deletar_delete.setGeometry(700,50,80,22)
        self.btn_deletar_delete.clicked.connect(self.delete_aluno)



        global total_frames
        self.total_frames = (self.frm_adicionar, self.frm_editar, self.frm_pesquisar, self.frm_deletar)


    def pesquisa_aluno(self):
        global lbl_infos
        global txt_nome01
        texto = self.txt_nome01.text()
        
        for doc in banco.find({"nome": texto}):
            esse = str(doc)

        
        self.lbl_infos=QLabel(esse,self.frm_pesquisar)
        self.lbl_infos.setGeometry(30,150,915,10)
        self.lbl_infos.setVisible(True)
    
    def limpa_pesquisa(self):
        global lbl_infos
        global txt_nome01
        self.lbl_infos.setVisible(False)
        self.txt_nome01.clear()
    



    def add_mongo(self):
        global txt_nome
        global txt_nota1
        global txt_nota2
        nota1 = float(self.txt_nota1.text())
        nota2 = float(self.txt_nota2.text())
        media = (nota1+nota2)/2
        if media >= 7:
            aprovado = True
        else:
            aprovado = False
        dados = {
        "nome": self.txt_nome.text(),
        "nota1": self.txt_nota1.text(),
        "nota2": self.txt_nota2.text(),
        "media": media,
        "Aprovação": aprovado

        }
        result = banco.insert_one(dados)
        result


    def limpar_add(self):
        global txt_nome
        global txt_nota1
        global txt_nota2
        self.txt_nome.clear()
        self.txt_nota1.clear()
        self.txt_nota2.clear()


    def limpar_editar(self):
        global campo_busca
        global txt_nome_edit
        global txt_nota1_edit
        global txt_nota2_edit
        self.campo_busca.clear()
        self.txt_nome_edit.clear()
        self.txt_nota1_edit.clear()
        self.txt_nota2_edit.clear()
    
    def editar_aluno(self):
        global campo_busca
        global txt_nome_edit
        global txt_nota1_edit
        global txt_nota2_edit
        nome_banco=str(self.campo_busca.text())
        nome_aluno=str(self.txt_nome_edit.text())
        nota1 = float(self.txt_nota1_edit.text())
        nota2 = float(self.txt_nota2_edit.text())
        media = (nota1+nota2)/2
        if media >= 7:
            aprovado = True
        else:
            aprovado = False

        novasinfo = {
        "nome": nome_aluno,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "Aprovação": aprovado
        }
        editando = banco.update({"nome": nome_banco}, novasinfo)
        editando

    

    def delete_aluno(self):

        global txt_nome_delete
        nomeDelete = str(self.txt_nome_delete.text())
        resultee = banco.delete_one({"nome": nomeDelete})
        resultee
        self.txt_nome_delete.clear()



    def ocultar_frames(self):
        global total_frames
        for f in self.total_frames:
            if f.isVisible()== True:
                f.setVisible(False)



    def exibir_area_adicionar(self):
        global frm_cadastro
        self.ocultar_frames()
        self.frm_adicionar.setVisible(True)

    def exibir_area_editar(self):
        global frm_editar
        self.ocultar_frames()
        self.frm_editar.setVisible(True)

    def exibir_area_pesquisar(self):
        global frm_pesquisar
        self.ocultar_frames()
        self.frm_pesquisar.setVisible(True)

    def exibir_area_deletar(self):
        global frm_deletar
        self.ocultar_frames()
        self.frm_deletar.setVisible(True)

        




#manter a janela aberta 
myApp = QApplication(sys.argv)

janela =  window()
janela.show()

myApp.exec_()
sys.exit(0)