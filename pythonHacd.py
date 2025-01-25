import socket
from datetime import datetime

# Define o alvo
target = input("Digite o endereço IP do alvo: ")

# Converte o endereço IP do alvo se o usuário digitou um hostname
target_ip = socket.gethostbyname(target)

print(f"Escaneando o host: {target_ip}")
print(f"Iniciado em: {datetime.now()}")

# Definindo o intervalo de portas a serem escaneadas
start_port = 1
end_port = 1024

# Função para escanear portas
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao escanear porta {port}: {e}")
        return False

# Escaneando as portas no intervalo definido
for port in range(start_port, end_port + 1):
    if port_scan(port):
        print(f"Porta {port} está aberta")
    else:
        print(f"Porta {port} está fechada")

print(f"Escaneamento concluído em: {datetime.now()}")
