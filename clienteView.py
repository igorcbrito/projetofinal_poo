import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
       

class AppGUI:

    def __init__(self, master, tipo, controller):

        self.controller = controller
        self.tipo = tipo
        self.frame = tk.Frame(master)
        self.frame.pack()

        if(self.tipo == 0):
            self.controller.root_main.iconify()
            self.frame = tk.Frame(master)
            self.frame.pack()

            #Variáveis capturadoras de informação
            self.vusuario = StringVar()
            self.vsenha = StringVar()

            #Botões e entradas

            self.llogin = tk.Label(self.frame, text="Usuário:")
            self.lsenha = tk.Label(self.frame, text="Senha:")
            self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
            self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
            self.btnEntrar = tk.Button(self.frame, text="Entrar")
            self.btnCadastrar = tk.Button(self.frame, text="Cadastrar")

            #Adicionar Widgets
            self.llogin.grid(row=0,column=0)
            self.lsenha.grid(row=1,column=0)
            self.eusuario.grid(row=0,column=1)
            self.esenha.grid(row=1,column=1)
            self.btnCadastrar.grid(row=2,column=0)
            self.btnEntrar.grid(row=2,column=1)

            ##acao do botao para cadastrar - abrirá uma nova janela top.level
            self.btnCadastrar.bind("<Button>", lambda e: self.cadastrar())

            ##acao do botao para entrar - abrira uma nova janela root
            self.btnEntrar.bind("<Button>", lambda e: controller.logar(self.vusuario.get(), self.vsenha.get()))

        if(self.tipo == 1):
            self.frame = tk.Frame(self.controller.root_main)
            self.frame.pack()

            self.lemexecucao = tk.Label(self.frame, text="Em Execucao:")
            self.lartista = tk.Label(self.frame, text="Artista:")
            self.btnVerPlaylist = tk.Button(self.frame, text="Ver Playlist")
            self.btnFavoritar = tk.Button(self.frame, text="Favoritar")
            self.btnExecutar = tk.Button(self.frame, text="Executar")
            self.btnPausar = tk.Button(self.frame, text="Pausar")
            self.btnnPular = tk.Button(self.frame, text="Pular")
            self.btnVoltar = tk.Button(self.frame, text="Voltar")
            self.btnCriar = tk.Button(self.frame, text="Criar Playlist")

            #Adicionar Widgets
            self.lemexecucao.grid(row=0,column=0)
            self.lartista.grid(row=1,column=0)
            self.btnVerPlaylist.grid(row=2,column=0)
            self.btnFavoritar.grid(row=2,column=1)
            self.btnExecutar.grid(row=2,column=2)
            self.btnPausar.grid(row=3,column=0)
            self.btnnPular.grid(row=3,column=1)
            self.btnVoltar.grid(row=3,column=2)
            self.btnCriar.grid(row=3, column=3)


            self.btnVerPlaylist.bind("<Button>", lambda e: self.abrirPlaylist());

            self.btnCriar.bind("<Button>", lambda e: self.criarPlaylist()) #Abre a janela de criar uma playlist




    def cadastrar(self):
        ##deixar comentado, motivo ver comentario na funcao de limpar
        #self.eusuario['state'] = 'disabled'
        #self.esenha['state'] = 'disabled'
        self.controller.root.iconify()
        self.win = tk.Toplevel()
        self.win.wm_title("Cadastro")
        self.win.geometry('400x200')
        self.frame = tk.Frame(self.win)
        self.frame.pack()


        #captura informações para cadastro
        self.vnome = StringVar()
        self.vemail = StringVar()
        self.vidade = StringVar()
        self.vpais = StringVar()
        self.vusuario = StringVar()
        self.vsenha = StringVar()

        #Botões e campos de entrada
        self.lusuario = tk.Label(self.frame, text="Usuário:")
        self.lsenha = tk.Label(self.frame, text="Senha:")
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.lemail = tk.Label(self.frame, text="Email:")
        self.lidade = tk.Label(self.frame, text="Idade:")
        self.lpais = tk.Label(self.frame, text="País:")
        self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.eidade = tk.Entry(self.frame, textvariable=self.vidade)
        self.epais = tk.Entry(self.frame, textvariable=self.vpais)
        self.btnTerminar = tk.Button(self.frame, text="Terminar") #Finaliza a operação de cadastro

        self.lnome.grid(row=0,column=0)
        self.enome.grid(row=0,column=1)
        self.lidade.grid(row=1,column=0)
        self.eidade.grid(row=1,column=1)
        self.lpais.grid(row=2,column=0)
        self.epais.grid(row=2,column=1)
        self.lemail.grid(row=3,column=0)
        self.eemail.grid(row=3,column=1)
        self.lusuario.grid(row=4,column=0)
        self.eusuario.grid(row=4,column=1)
        self.lsenha.grid(row=5,column=0)
        self.esenha.grid(row=5,column=1)
        self.btnTerminar.grid(row=6,column=0)

        self.btnTerminar.bind("<Button>", lambda e: self.controller.cadastrar(self.vnome.get(), self.vidade.get(), self.vpais.get(), self.vemail.get(), self.vusuario.get(), self.vsenha.get()))

    
    def limpar(self):
        '''Remover os textos dos campos'''
        self.win.destroy()
        self.controller.root.deiconify()
        ## linhas 94 e 95 deveria funcionar para reabilitar os campos loguin e senha da tela root1, mas só desabilita o do loguin. Vou deixar comentado por hora
        #self.eusuario['state'] = 'normal'
        #self.esenha['state'] = 'normal'
        self.vusuario.set("")
        self.vsenha.set("")
        #Focus no campo 
        self.eusuario.focus_set()
        
    def entrar(self):
        self.controller.root.iconify()
        self.controller.root_main.deiconify()
        MinhatelaPrincipal = AppGUI(self.controller.root_main, 1, self.controller)
        self.controller.root_main.mainloop()

    def entrar_erro(self):
        messagebox.showerror("Erro", "Dados incorretos!")

    def cadastrar_erro(self):
        messagebox.showerror("Erro", "Não é possível cadastrar, pois já exoste!")

    def cadastrar_sucesso(self):
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    
    def retornarMainWindow(self):
        self.win.destroy()
        self.controller.root_main.deiconify()

    def abrirPlaylist(self):
        self.controller.root.iconify()
        self.controller.root_main.iconify()
        self.win = tk.Toplevel()
        self.win.wm_title("Playlist Favoritas")
        self.win.geometry('400x200')
        self.frame = tk.Frame(self.win)
        self.frame.pack()


        #captura informações para cadastro
        self.vnome = StringVar()
        self.vemail = StringVar()
        self.vidade = StringVar()
        self.vpais = StringVar()
        self.vusuario = StringVar()
        self.vsenha = StringVar()

        #Botões e campos de entrada
        self.lusuario = tk.Label(self.frame, text="Usuário:")
        self.lsenha = tk.Label(self.frame, text="Senha:")
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.lemail = tk.Label(self.frame, text="Email:")
        self.lidade = tk.Label(self.frame, text="Idade:")
        self.lpais = tk.Label(self.frame, text="País:")
        self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.eidade = tk.Entry(self.frame, textvariable=self.vidade)
        self.epais = tk.Entry(self.frame, textvariable=self.vpais)
        self.btnRetornar = tk.Button(self.frame, text="Terminar") #Finaliza a operação de cadastro

        self.lnome.grid(row=0,column=0)
        self.enome.grid(row=0,column=1)
        self.lidade.grid(row=1,column=0)
        self.eidade.grid(row=1,column=1)
        self.lpais.grid(row=2,column=0)
        self.epais.grid(row=2,column=1)
        self.lemail.grid(row=3,column=0)
        self.eemail.grid(row=3,column=1)
        self.lusuario.grid(row=4,column=0)
        self.eusuario.grid(row=4,column=1)
        self.lsenha.grid(row=5,column=0)
        self.esenha.grid(row=5,column=1)
        self.btnRetornar.grid(row=6,column=0)

        self.btnRetornar.bind("<Button>", lambda e: self.retornarMainWindow())

    def criarPlaylist(self):
        '''Abre uma nova janela de criar playlist'''
        self.controller.root.iconify()
        self.controller.root_main.iconify()
        self.win = tk.Toplevel()
        self.win.wm_title("Criar playlist")
        self.win.geometry('400x600')
        self.frame = tk.Frame(self.win)
        self.frame.pack()

        self.vnomeplay = StringVar()
        self.var0 = tk.IntVar()
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        
        
        
        self.lnomeplay = tk.Label(self.frame, text="Nome da Playlist:")
        self.enomeplay = tk.Entry(self.frame, textvariable=self.vnomeplay)
        self.chk0 = tk.Checkbutton(self.frame, text='Holiday - Green Day', variable=self.var0)
        self.chk1 = tk.Checkbutton(self.frame, text='Sugar - Maroon 5', variable=self.var1)
        self.chk2 = tk.Checkbutton(self.frame, text='Lonely Day - System Of a Down', variable=self.var2)
        self.chk3 = tk.Checkbutton(self.frame, text='Señorita - Shawn Mendes', variable=self.var3) # Thatiana
        self.chk4 = tk.Checkbutton(self.frame, text='Sign Of The Times - Harry Styles', variable=self.var4)
        self.chk5 = tk.Checkbutton(self.frame, text='Nothing Else Matters - Metallica', variable=self.var5)
        self.chk6 = tk.Checkbutton(self.frame, text='Violet Hill - Coldplay', variable=self.var6)
        self.btnSalvar = tk.Button(self.frame, text="Salvar")

        self.lnomeplay.grid(row=0,column=0)
        self.enomeplay.grid(row=0,column=1)
        self.chk0.grid(row=1,column=0)
        self.chk1.grid(row=2,column=0)
        self.chk2.grid(row=3,column=0)
        self.chk3.grid(row=4,column=0)
        self.chk4.grid(row=5,column=0)
        self.chk5.grid(row=6,column=0)
        self.chk6.grid(row=7,column=0)
        self.btnSalvar.grid(row=8,column=0)

        self.btnSalvar.bind("<Button>", lambda e: self.controller.armazenarPlaylist(self.vnomeplay.get(), self.var0.get(), self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(), self.var6.get()))
        

    def criarPlaylist_sucesso(self):
        '''Mostrar um pop-up dizendo que a playlist foi criada'''
        messagebox.showinfo("Criar Playlist", "Sua playlist foi criada!")

    def criarPlaylist_erro(self):
        '''Mostra um pop-up com erro quando algo de errado ocorre ao criar uma playlist'''
        messagebox.showerror("Criar Playlist", "O nome da playlist já está sendo utilizado!")
        