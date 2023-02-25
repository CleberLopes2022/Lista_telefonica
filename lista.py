from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

from  dados import *

# cores -----------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#f0f3f5"  # cizenta / grey
co2 = "#feffff"  # branca
co3 = "#38576b"  # preta / black
co4 = "#403d3d"   # letra
co5 = "#6f9fbd"  # azul
co6 = "#ef5350"   # vermelha
co7 = "#93cd95"   # verde

janela = Tk()
janela.title('Minha Agenda Telefonica')
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE, height= FALSE)
p1 = PhotoImage(file = 'celular.png')
janela.iconphoto(False, p1)

style = Style(janela)
style.theme_use("clam")

# frames

frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=500, height=248, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0,columnspan=2, pady=1, padx=10, sticky=NW)

# configurando frame_cima

l_nome = Label(frame_cima, text='Agenda Telefonica', anchor=NE, font=('arial 20 bold'),bg=co3, fg=co1)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=500, anchor=NE, font=('arial 1'),bg=co2, fg=co1)
l_linha.place(x=0, y=46)

# configurando frame_baixo

l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('ivy 10'),bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left',relief='flat', font=('',10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_sexo = Label(frame_baixo, text='Sexo *', anchor=NW,relief='flat', font=('ivy 10'),bg=co1, fg=co4)
l_sexo.place(x=10, y=50)
c_sexo = Combobox(frame_baixo, width=32)
c_sexo['value'] = ('', 'F', 'M')
c_sexo.place(x=80, y=50)

l_telefone = Label(frame_baixo, text='Telefon *', anchor=NW, font=('ivy 10'),bg=co1, fg=co4)
l_telefone.place(x=10, y=80)
e_telefone = Entry(frame_baixo, width=25, justify='left', relief='flat',font=('',10), highlightthickness=1)
e_telefone.place(x=80, y=80)

l_email = Label(frame_baixo, text='Email *', anchor=NW, font=('ivy 10'),bg=co1, fg=co4)
l_email.place(x=10, y=110)
e_email = Entry(frame_baixo, width=25, justify='left', relief='flat',font=('',10), highlightthickness=1)
e_email.place(x=80, y=110)

global tree
# configurando o frame tabela
list_header = ['Nome', 'Sexo', 'Telefone', 'email']

tree = ttk.Treeview(frame_tabela, selectmode="extended",
                        columns=list_header, show="headings")

def mostrar_dados():

    list_header = ['Nome', 'Sexo', 'Telefone', 'email']

    dados = exibir_dados()


    # vertical scrollbar
    vsb = ttk.Scrollbar(
        frame_tabela, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # cabeçalho
    tree.heading(0,text='Nome', anchor=NW)
    tree.heading(1,text='Sexo', anchor=NW)
    tree.heading(2,text='Telefone', anchor=NW)
    tree.heading(3,text='Email', anchor=NW)


    # corpo
    tree.column(0,width=110, anchor='nw')
    tree.column(1,width=60, anchor='nw')
    tree.column(2,width=110, anchor='nw')
    tree.column(0,width=110, anchor='nw')

    for item in dados:
        tree.insert('', 'end', values=item)


mostrar_dados()

# função inserir

def inserir():
    nome = e_nome.get()
    sexo = c_sexo.get()
    telefone = e_telefone.get()
    email = e_email.get()

    dados = [nome, sexo, telefone, email]

    if nome == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor preencha todos os campos')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Os dados forma adicionados com sucesso!')

        e_nome.delete(0,'end')
        c_sexo.delete(0,'end')
        e_telefone.delete(0,'end')
        e_email.delete(0,'end')

        mostrar_dados()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']


        nome = tree_lista[0]
        sexo = tree_lista[1]
        telefone = str(tree_lista[2])
        email = tree_lista[3]

        e_nome.insert(0,nome)
        c_sexo.insert(0,sexo)
        e_telefone.insert(0,telefone)
        e_email.insert(0,email)

        def confirmar():
            nome = e_nome.get()
            sexo = c_sexo.get()
            telefone_novo = e_telefone.get()
            email = e_email.get()

            dados = [telefone,nome, sexo, telefone_novo, email]

            atualizar_dados(dados)

  
            messagebox.showinfo('Dados', 'Os dados forma atualizados com sucesso!')

            e_nome.delete(0,'end')
            c_sexo.delete(0,'end')
            e_telefone.delete(0,'end')
            e_email.delete(0,'end')

            b_confirmar.destroy()

            mostrar_dados()

        messagebox.showinfo('Dados', 'Os dados foram atualizados com sucesso!')

        
        b_confirmar = Button(frame_baixo,command=confirmar, text='Confirmar',width= 10,  font=('ivy 8 bold'),bg=co5, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=110)

    except:
        messagebox.showwarning('Dados', 'por favor selecione uma informação na tabela para atualizar')

def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        telefone = str(tree_lista[2])

        remover_dados(telefone)

        messagebox.showinfo('Dados', 'Os dados forma deletados com sucesso!')

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        mostrar_dados()


    except:
        messagebox.showwarning('Dados', 'por favor selecione uma informação na tabela para atualizar')


def procurar():

    telefone = e_procurar.get()

    dados = pesquisar_dados(telefone)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)

    e_procurar.delete(0,'end')

# criando o botao procurar

l_procurar = Button(frame_baixo, command=procurar,text='Procurar', font=('ivy 8 bold'),bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_procurar.place(x=290, y=20)
e_procurar = Entry(frame_baixo, width=16, justify='left',relief='flat', font=('',11), highlightthickness=1)
e_procurar.place(x=347, y=21)


l_ver = Button(frame_baixo, command=mostrar_dados,text='Exibir dados', width=10, font=('ivy 8 bold'),bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_ver.place(x=290, y=50)

l_adicionar = Button(frame_baixo,command=inserir, text='Adicionar',width= 10,  font=('ivy 8 bold'),bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
l_adicionar.place(x=400, y=50)

l_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10,font=('ivy 8 bold'),bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
l_atualizar.place(x=400, y=80)

l_deletar = Button(frame_baixo,command=remover,text='Deletar', width=10,font=('ivy 8 bold'),bg=co6, fg=co4, relief=RAISED, overrelief=RIDGE)
l_deletar.place(x=400, y=110)


janela.mainloop()