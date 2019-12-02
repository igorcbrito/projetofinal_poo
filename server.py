'''Mudei os nomes dos arquivos e criei novos para não causar confusão:
- nossa View agora se chama clienteView.py
- o controlador do cliente se chama cliente controller
- criei o arquivo server
- criei o controlador do server chamado serverController.py

Nosso model permanece usuarioModel.py!

Devo lembrar que:
- o cliente controller faz comunicação via socket com server
- o server possui o seu controlador
- o controlador do server faz uma comunicação direta com o model
- o model vai abrigar o tiny db

E também:
- o cliente passa os dados para o seu controlador de forma direta
- quando for passar as informações via socket devemos juntar as informações num dicionário json com
json.dumps, passar esse dicionário para string binária usando encode. Ao receber no controller, voltar 
para o formato de dicionário json com decode e para manipular as informações contidas usar json.loads'''


import socket
from serverController import ControllerSC
from usuarioModel import *
import json

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Adicionar e listar produtos (segundo a escolha do cliente)'''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
                    while True:
                        dados = conn.recv(2048)
                        conn.send(b'Ok')
                        opc = dados.decode()
                        print(opc)
                        if opc == "entrar": 
                            
                            cred = conn.recv(2048) # Recebe
                            log_pass = json.loads(cred.decode()) #De
                            usuario = log_pass['usuario']
                            senha = log_pass['senha']

                            permission = ControllerSC.entrarSC(usuario, senha)
                            permission_str = str(permission)
                            print(permission_str)
                            print(type(permission_str))
                            conn.send(permission_str.encode()) # Minha dúvida é se posso por um if dentro do controlador do cliente

                        elif opc == "cadastrar":
                            infos = conn.recv(2048)
                            conn.send(b'Cadastrando...')
                            dados = json.loads(infos.decode())

                            U = Usuario(dados['nome'], dados['idade'], dados['pais'], dados['email'], dados['usuario'], dados['senha'])
                        
                            ControllerSC.cadastrarSC(U)

                        elif opc == "criarPlaylist":
                            
                            infos = conn.recv(2048)
                            
                            conn.send(b'Criando playlists')
                            
                            print("entreeeeeeeeeeei22222")
                            playlist = json.loads(infos.decode()) #Preciso enviar esse dicionário para o server controller e mandar para model para fazer as escolhas
                            #Pode ser feito usando if e verificando se é 0 ou 1 e criando as os obj de musica passando para uma lista
                            minhaPlaylist = ControllerSC.criarPlaylist(playlist)
                            
                            #conn.recv(2048)
                            conn.send(minhaPlaylist)


                        elif opc == "terminar":
                            break        
        
                print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
