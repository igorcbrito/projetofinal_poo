#Test
# Note que só precisamos do controlador para interagir com o sistema
from clienteController import Controller

# Fará comunicação com o server
HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

if __name__ == "__main__":
    C = Controller(HOST, PORT)

