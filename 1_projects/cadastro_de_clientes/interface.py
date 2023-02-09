from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs(): #Classe que cria as funções do back-end
    def limpa_cliente(self): #Cria a ação de limpar as entradas
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self): #conecta ao banco de dados
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando banco de dados")
    def desconecta_bd(self): #desconecta do banco de dados
        self.conn.close(); print("Desconectando banco de dados")
    def montaTabelas(self): #cria banco de dados
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL, 
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO  clientes (nome_cliente, telefone, cidade)
            VALUES (?,?,?) """, (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.selec_lista()
        self.limpa_cliente()
    def selec_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """) # Define a ordem da lista
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3 , col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4) 
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.selec_lista()

class Application(Funcs): #Classe que cria as funções do front-end
    def __init__(self):
        self.root = root
        self.tela() #congira o fundo da tela
        self.frames_da_tela() #chama os frames da tela
        self.widgets_frame1() #chama os botões dentro do frame1
        self.lista_frame2() #chama a lista do frame2
        self.montaTabelas() #cria banco de dados (se já criado, ignora)
        self.selec_lista()
        root.mainloop() #abre o GUI
    
    def tela(self):
        self.root.title("Cadastro de Cliente") #determina o nome na barra superior
        self.root.configure(background='#1e3743') #determina cor de fundo da tela
        self.root.geometry("750x500") #determina o tamanho ninicial da tela
        self.root.resizable(True, True) #False faz a tela ficar fixa
        self.root.maxsize(900, 600)
        self.root.minsize(600, 400)
    
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, 
        bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=3) #cria a borda do frame
        self.frame_1.place(relx= 0.02 , rely=0.03, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root,
        bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=3)
        self.frame_2.place(relx= 0.02 , rely=0.5, relwidth=0.96, relheight=0.46)
    
    def widgets_frame1(self):

    ### BOTÕES

        self.bt_limpar = Button(self.frame_1, text= "Limpar", #cria o botão dentro do frame1
            bd= 2, bg= '#107bd2',  #estiliza a forma botão
            font= ('verdana', 8, 'bold'), fg= 'white', #estiliza o texto do botão
            command= self.limpa_cliente) #determina ação do comando 
        self.bt_limpar.place(relx= 0.2 , rely=0.1, relwidth=0.1, relheight=0.15) #posiciona o botão no frame1

        self.bt_buscar = Button(self.frame_1, text= "Buscar",
            bd= 2, bg= '#107bd2',  
            font= ('verdana', 8, 'bold'), fg= 'white')
        self.bt_buscar.place(relx= 0.3 , rely=0.1, relwidth=0.1, relheight=0.15) 
        
        self.bt_novo = Button(self.frame_1, text= "Novo", 
            bd= 2, bg= '#107bd2', 
            font= ('verdana', 8, 'bold'), fg= 'white',
            command= self.add_cliente) 
        self.bt_novo.place(relx= 0.6 , rely=0.1, relwidth=0.1, relheight=0.15) 
        
        self.bt_alterar = Button(self.frame_1, text= "Alterar", 
            bd= 2, bg= '#107bd2', 
            font= ('verdana', 8, 'bold'), fg= 'white') 
        self.bt_alterar.place(relx= 0.7 , rely=0.1, relwidth=0.1, relheight=0.15) 

        self.bt_apagar = Button(self.frame_1, text= "Apagar",
            bd= 2, bg= '#107bd2', 
            font= ('verdana', 8, 'bold'), fg= 'white') 
        self.bt_apagar.place(relx= 0.8 , rely=0.1, relwidth=0.1, relheight=0.15)


    ### ENTRADAS

        self.lb_codigo = Label(self.frame_1, text = "Código", #Cria o rótulo "Código" no frame1
            bg = '#dfe3ee', fg= '#107bd2') #Estiliza o rótulo
        self.lb_codigo.place(relx= 0.05 , rely=0.05)
        self.codigo_entry = Entry(self.frame_1) #Cria a entrada do "Código" no frame1
        self.codigo_entry.place(relx= 0.05 , rely= 0.15, relwidth= 0.08)

        self.lb_nome = Label(self.frame_1, text = "Nome", bg = '#dfe3ee', fg= '#107bd2')
        self.lb_nome.place(relx= 0.05 , rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05 , rely= 0.45, relwidth= 0.8)

        self.lb_fone = Label(self.frame_1, text = "Telefone", bg = '#dfe3ee', fg= '#107bd2')
        self.lb_fone.place(relx= 0.05 , rely=0.6)
        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx= 0.05 , rely= 0.7, relwidth= 0.4)

        self.lb_cidade = Label(self.frame_1, text = "Cidade", bg = '#dfe3ee', fg= '#107bd2')
        self.lb_cidade.place(relx= 0.5 , rely=0.6)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.5 , rely= 0.7, relwidth= 0.4)

    def lista_frame2(self):
        self.listaCli= ttk.Treeview(self.frame_2, height= 3, column= ("col1", "col2", "col3", "col4",)) #cria o treeview
        
        self.listaCli.heading("#0", text= "") #nomeia a coluna
        self.listaCli.heading("#1", text= "Código")
        self.listaCli.heading("#2", text= "Nome")
        self.listaCli.heading("#3", text= "Telefone")
        self.listaCli.heading("#4", text= "Cidade")

        self.listaCli.column("#0", width= 1) #define o tamanho da coluna
        self.listaCli.column("#1", width= 50)
        self.listaCli.column("#2", width= 200)
        self.listaCli.column("#3", width= 125)
        self.listaCli.column("#4", width= 125)

        self.listaCli.place(relx= 0.01 , rely= 0.1, relwidth= 0.95, relheight= 0.85) #posiciona a lista

        self.scroolLista = Scrollbar(self.frame_2, orient= 'vertical') #cria a barra de rolagem
        self.listaCli.configure(yscroll=self.scroolLista.set) #define a barra de rolagem como pertencente à lista
        self.scroolLista.place(relx= 0.96, rely= 0.1, relwidth= 0.03, relheight= 0.85)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick) #vincula método ao clique duplo


Application()
        