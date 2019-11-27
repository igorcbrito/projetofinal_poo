# Definição do View  para a Pessoa 
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

class PessoaGUI:
    ''' Mostrar as informações da pessoa'''
    
    def __init__(self, master, controller):
        '''master=Janela Principal
           controller: define as ações
        '''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        #Variaveis para os campos de texto
        self.vcpf = StringVar()
        self.vnome = StringVar()
        self.vemail = StringVar()

        #Criação dos rótulos e os campos de texto
        self.lcpf = tk.Label(self.frame, text="CPF:")
        self.ecpf = tk.Entry(self.frame, textvariable=self.vcpf)
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.enome = tk.Entry(self.frame,show="*")
        self.lemail = tk.Label(self.frame, text="Email:")
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.btnAdd = tk.Button(self.frame, text="Adicionar")
        self.btnList = tk.Button(self.frame, text="Listar")
        self.btnClean = tk.Button(self.frame, text="Limpar")
        self.btnChange = tk.Button(self.frame, text="Alterar E-mail")
        self.btnDelete = tk.Button(self.frame, text="Excluir pessoa")
        
        # Adicionar os widgets
        self.lcpf.grid(row=0, column=0)
        self.ecpf.grid(row=0, column=1)
        self.lnome.grid(row=1, column=0)
        self.enome.grid(row=1, column=1)
        self.lemail.grid(row=2, column=0)
        self.eemail.grid(row=2, column=1)
        self.btnAdd.grid(row=3, column=0)
        self.btnList.grid(row=3, column=1)
        self.btnClean.grid(row=3, column=2)
        self.btnChange.grid(row=4,column=0)
        self.btnDelete.grid(row=4, column=1)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnAdd.bind("<Button>",
                             lambda e: controller.adicionar_pessoa(self.vcpf.get(),self.vnome.get(), self.vemail.get()));

        self.btnList.bind("<Button>", lambda e: controller.listar_pessoas());

        self.btnChange.bind("<Button>", lambda e: controller.atualizar_email(self.vcpf.get(),self.vemail.get()));

        self.btnDelete.bind("<Button>", lambda e: controller.excluir_pessoa(self.vcpf.get()))

        # A ação deste botão chama direitamente um dos métodos do view
        self.btnClean.bind("<Button>", lambda e: self.limpar());

    
        #Focus no CPF
        self.ecpf.focus_set()

    def limpar(self):
        '''Remover os textos dos campos'''
        self.vcpf.set("")
        self.vnome.set("")
        self.vemail.set("")
        #Focus no campo CPF
        self.ecpf.focus_set()
        self.ecpf['state'] = 'normal'
        self.enome['state'] = 'normal'
        

    

    def adicionar_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Pessoa", "Pessoa Adicionada (CPF = {0})!".format(self.vcpf.get()))

    def excluir_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Pessoa", "Pessoa excluída!")
        
    def excluir_erro(self):
        '''Mostrar uma mensagem informando que a operação não foi bem sucedida'''
        messagebox.showerror("Pessoa", "Pessoa inexistente!")

    def email_alterado(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Pessoa", "Email alterado com sucesso!")

    def erro_email(self):
        '''Mostrar uma mensagem informando que a operação não foi bem sucedida'''
        messagebox.showerror("Pessoa", "Nenhum email para alterar!")

    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror("Pessoa", "Impossível adicionar duas pessoas com o mesmo CPF = {0}".format(self.vcpf.get()))

    def mostrar_pessoa(self, p, win):
        '''
        Mostrar as informações da pessoa
        Note que esta função retorna outra função (necessária para
        implementar o command do botão)
        '''
        def fmostrar(e):
            self.vcpf.set(p.cpf)
            self.vnome.set(p.nome)
            self.vemail.set(p.email)
            # Fechar a janela
            win.destroy()
            self.ecpf.focus_set()
            self.ecpf['state'] = 'disabled'
            self.enome['state'] = 'disabled'
            self.eemail.focus_set()
        return fmostrar


    def listar(self, L):
         '''Mostrar a lista de pessoas L'''
         win = tk.Toplevel()
         win.wm_title("Lista de Pessoas")

         tk.Label(win, text="CPF",bg="black", fg="white", width=15).grid(row=0, column=0)
         tk.Label(win, text="Nome",bg="black", fg="white", width=40).grid(row=0, column=1)
         tk.Label(win, text="Email",bg="black", fg="white", width=20).grid(row=0, column=2)
         i =1
         for p in L:
             LCPF = tk.Label(win, text=p.cpf, fg="blue")
             LCPF.bind("<Button>", self.mostrar_pessoa(p, win))
             LCPF.grid(row=i, column=0)
             tk.Label(win, text=p.nome).grid(row=i, column=1)
             tk.Label(win, text=p.email).grid(row=i, column=2)
             i += 1
