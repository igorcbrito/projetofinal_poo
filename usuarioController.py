import tkinter as tk
from application import AppGUI
from usuarioModel import *

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Controller:
     def __init__(self, host, port):
        
       #Abrindo porta de comunicação
       self._host = host
       self._port = port


    def iniciar(self):

        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Pessoa')

        # Criar o objeto View
        self.view = PessoaGUI(self.root, self)

        #Loop
        self.root.mainloop()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
                    while True:
                        dados = conn.recv(2048)
                        opc = dados.decode()
                        print(opc)
                        if opc == "entrar":
                            conn.send(b'esperando dados...')
                            login = conn.recv(2048)
                            senha = conn.recv(2048)
                            permissao = Usuario.entrar()
                            if permissao == True:
                                self.view.entrar()
                        
                            
                        elif opc == "listar":
                            conn.send(str.encode(json.dumps(self._listaProds, cls=produto.MyEncoder)))
                        elif opc == "consultar":
                            conn.send(b'Consultando produtos...')
                            codigo = conn.recv(2048)
                            resultadoConsulta = Produto.consultar(int(codigo.decode()))
                            conn.send(str.encode(json.dumps(resultadoConsulta, cls=produto.MyEncoder)))
                        elif opc == "terminar":
                            break
        
        
                print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))



        

