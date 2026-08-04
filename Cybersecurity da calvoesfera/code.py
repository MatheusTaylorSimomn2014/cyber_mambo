import os

contador_global = 0

def incrementar():
    global contador_global
    contador_global += 1
    print(f"Contador incrementado para: {contador_global}")

def executar_backup(nome_arquivo):
    comando = "tar -cvf backup.tar " + nome_arquivo
    os.system(comando)

if __name__ == '__main__':
    print('Bem vindo ao super app vulneravel!', end='\n\n')
    print('Funcoes:\n1. Contador Global\n2. Fazer Backup')
    option = input('Digite qual funÃ§ao deseja executar:\n> ')
    match option:
        case "1":
            incrementar()
        case "2":
            executar_backup(input('Digite o nome do arquivo:\n> '))