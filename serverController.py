#Classe do controlador do servidor SEEEEEEERVIDOOOOOOOOOOR

from usuarioModel import *


class ControllerSC:
    '''
    O controlador define 2 ações:
     - adicionar_pessoa: para adicionar novas pessoas no banco de
       dados.  
     - listar_pessoas: retornar a lista das pessoas

     Note que as 2 ações supracitadas utilizam a classe do Modelo para
     consultar/atualizar o banco de dados
    '''

    def __init__(self):
        pass
    
    @staticmethod
    def entrarSC(login, senha):
        resultado = Usuario.entrar(login, senha)
        return resultado

    @staticmethod
    def cadastrarSC(usuario):
        Usuario.adicionar(usuario)

    @staticmethod
    def criarPlaylist(dicioPlaylist):
        
        musicas = Playlist.criarPlaylist(dicioPlaylist)
        minhasMusicas = json.dumps(musicas.encode())
        return  minhasMusicas
        