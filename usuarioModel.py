# Classe do Modelo

class usuarioRepetido (Exception):
    '''
    Exceção lançada ao tentar cadastrar duas pessoas com o 
    mesmo CPF
    '''
    def __init__(self):
        super().__init__("Usuário já cadastrado")
        
class Usuario:
    '''Classe do modelo'''

    #Banco de dados,por enquanto simplesmente um dicionário indexado
    #com os CPFs
    _bd = {}

    def __init__(self, nome, idade, pais, email, usuario, senha):
        self._nome = nome
        self._idade = idade
        self._pais = pais
        self._email = email
        self._usuario = usuario
        self._senha = senha
        self._playlists = {}


    def __repr__(self):
        return 'Pessoa({0})'.format(self.nome)

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

    @property
    def pais(self):
        return self._pais
    
    @property
    def email(self):
        return self._email

    @property
    def usuario(self):
        return self._usuario

    @staticmethod
    def adicionar(U):
        '''
        Adiciona a pessoa P no banco de dados.
        ----------
        raise:
          CPFRepetido se o CPF já está no banco de dados
        '''
        
        if U.login in Usuario._bd:
            raise usuarioRepetido()
        Usuario._bd[U.login] = U

   # @staticmethod
    #def listar():
        '''Retornar todas as pessoas cadastradas no banco de dados'''
     #   return Usuario._bd.values()

    #@staticmethod
    #def mudarEmail(cpf, novoEmail):
        '''Chama o método setter para alteração do email'''
     #   Pessoa._bd[cpf].email = novoEmail
     
    def criarPlaylist(self, nome):
        minhaPlay = Playlist(nome)
        self._playlists['nome'] = minhaPlay
    
    def deletarPlaylist(self,login, playlist):
        
        if playlist in self._playlists:
            self._playlists.pop(playlist)
    
        else:
            print("Playlist não existe!")

    @staticmethod
    def entrar(login, senha):

        if login in Usuario._bd:
            
            if senha == Usuario._bd['login'].senha:
                return True
            else:
                print("Senha incorreta!")
                return False

        else:
            print("Esse usuário não existe!")


        def addMusica(self, nomePlaylist, musica):
            
            if nomePlaylist in self._playlists:
                self._playlist['nomePlaylist'].incluirMusica(musica)

class Musica:

    def __init__(self, nome, cantor, genero):
        self._nome = nome
        self._cantor = cantor
        self._genero = genero

    @property
    def nome(self):
        return self._nome

    @property
    def cantor(self):
        return self._cantor

    @property
    def genero(self):
        return self._genero

class Playlist:

    def __init__(self, nome):
        self._nome = nome
        self._musicas = {}

    @property
    def nome(self):
        return self._nome

    @property
    def musicas(self):
        return self._musicas

    def incluirMusica(self, musica):
        self._musicas['musica.nome'] =  musica

class Genero:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
   
    
