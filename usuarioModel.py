# Classe do Modelo
import json
from tinydb import TinyDB, Query

class usuarioRepetido (Exception):
    '''
    Exceção lançada ao tentar cadastrar duas pessoas com o 
    mesmo CPF
    '''
    def __init__(self):
        super().__init__("Usuário já cadastrado")

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        d = vars(o) # Atributos do objeto
        return d

    @staticmethod
    def decode(d):
        '''recebe como parâmetro um dicionario'''
        return Usuario(d['_nome'], d['_idade'], d['_pais'], d['_email'], d['_usuario'], d['_senha'])
        
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
    def senha(self):
        return self._senha
    
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
        '''Adiciona o usuário U no banco de dados.'''
        if Usuario.verificarUsuario(U.usuario) is True: # Lança um erro caso já exista um usuário cadastrado
            raise usuarioRepetido

        else:
            with  TinyDB('usuarios.json') as db: # Aqui serão salvos os usuários
                # Insert recebe como parâmetro um dicionário
                Usuario._bd[U.usuario] = U
                db.insert((Usuario._bd[U.usuario]).toDict()) # Adiciona uma pessoa a uma base de dados


    @staticmethod
    def verificarUsuario(usuario):
        '''Verifica se o usuário está dentro do banco de dados'''
        with  TinyDB('usuarios.json') as db:
            Q = Query()
            l = db.search(Q._usuario == usuario) # Procura todo mundo com esse usuario e coloca em uma lista

        if l != []: # Caso a lista contenha itens, retorna True
            return True

        else:
            return False

     
    def criarPlaylist(self, nome, musicas):
        minhaPlay = Playlist(nome)
        self._playlists['nome'] = minhaPlay

    
    def deletarPlaylist(self,login, playlist):
        
        if playlist in self._playlists:
            self._playlists.pop(playlist)
    
        else:
            print("Playlist não existe!")

    @staticmethod
    def entrar(login, senha):
        '''Libera o acesso as outras funcionalidades ao usuário'''
        if Usuario.verificarUsuario(login) is True: # Se a existir um usuário com esse login a lista não é vazia e aqui é True
            with  TinyDB('usuarios.json') as db: # Vou procurar o usuário no banco de dados e vou saber se a senha está correta
                Q = Query()
                l = db.search(Q._usuario == login)
                usuario = l[0]
                if usuario['_senha'] == senha:
                    return True
                else:
                    return False
        else:
            return False

    def addMusica(self, nomePlaylist, musica):
            
        if nomePlaylist in self._playlists:
            self._playlist['nomePlaylist'].incluirMusica(musica)

    def toDict(self):
        '''Retorna a representacao como dicionario'''
        s = json.dumps(self, cls=MyEncoder)
        return json.loads(s)

    @staticmethod
    def fromDict(d):
        s = json.dumps(d)
        return json.loads(s, object_hook=MyEncoder.decode)

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
        self._musicas = []

    @property
    def nome(self):
        return self._nome

    @property
    def musicas(self):
        return self._musicas

    def incluirMusica(self, musica):
        self._musicas['musica.nome'] =  musica

    @staticmethod
    def criarPlaylist(dicio):
        '''Cria uma Playlist'''

        print('Entrei no criar playlist')
        for (key, obj) in dicio.items():
            if (key == 'm0' and obj == 1) :
                Playlist._musicas.append(Musica0)
            if (key == 'm1' and obj == 1) :
                Playlist._musicas.append(Musica1)
            if (key == 'm2' and obj == 1) :
                Playlist._musicas.append(Musica2)
            if (key == 'm3' and obj == 1) :
                Playlist._musicas.append(Musica3)
            if (key == 'm4' and obj == 1) :
                Playlist._musicas.append(Musica4)
            if (key == 'm5' and obj == 1) :
                Playlist._musicas.append(Musica5)
            if (key == 'm6' and obj == 1) :
                Playlist._musicas.append(Musica6)
        return Playlist._musicas

class Genero:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
   

Rock = Genero('Rock')
Pop = Genero('Pop')
HeavyMetal = Genero('Heavy Metal')
Alternativo = Genero('Alternativo')

Musica0 = Musica('Holiday', 'Green Day', Rock)
Musica1 = Musica('Sugar', 'Maroon 5', Pop)
Musica2 = Musica('Lonely Day', 'System Of a Down', Rock)
Musica3 = Musica('Señorita', 'Shawn Mendes', Pop)
Musica4 = Musica('Sign Of The Times', 'Harry Styles', Pop)
Musica5 = Musica('Nothing Else Matters', 'Metallica', HeavyMetal)
Musica6 = Musica('Violet Hill', 'Coldplay', Alternativo)


musicas = [Musica0, Musica1, Musica2, Musica3, Musica4, Musica5, Musica6]