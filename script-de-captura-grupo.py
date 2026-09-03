import psutil as p
from datetime import datetime
import time as t
import mysql.connector
import math

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="leo12345",
    database="grupo10"
)

cursor = db.cursor()

print("\n=========================")
print("\n        BEM-VINDO!")
print("\n=========================")

def capturaDados(id):
    usoCpu = p.cpu_percent(interval=0)
    freqCpu = p.cpu_freq().current
    usoRam = p.virtual_memory().percent


def menuCaptura(id):

    while True:

        print("\n-----------Menu-De-Captura-e-Analise-----------")  

        resposta = str(input("\n\nO que deseja analisar: \n1- Cpu, \n2- Ram, \n3- Disco, \n4- Rede \n5- Historico, \n9-Sair\n\nEscolha uma opção: "))

        if resposta == '1':
            while True:
                print("Uso da Cpu: ", p.cpu_percent(interval=0), "%")
                print("Frequência atual da Cpu: ", p.cpu_freq().current, "Mhz\n\n")

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')

                print("\nO programa está rodando. Precione 'ctrl + c' para sair.\n\n")

                t.sleep(3)


def menu():

    while True:

        print("\n-----------Menu-----------")

        maquina = str(input("\n\n1- Entrar, \n2- Cadastrar Máquina, \n3- Sair\n\nEscolha uma opção: "))
            
        if maquina == '1':
            while True:
                # Entrada
                idMaquina = str(input("Id da Maquina: "))
                nomeMaquina = str(input("Nome da maquina: "))

                comando_sql = "SELECT nome FROM maquina WHERE id = %s"

                valores = [
                    (idMaquina)
                ]

                cursor.execute(comando_sql, valores)
                resultados = cursor.fetchone()

                print(resultados)

                if resultados[0] == nomeMaquina:
                    print("Entrando...")
                    menuCaptura(idMaquina)
                    return idMaquina
                    
                else:
                    print("Acesso Negado! Tente novamente...")
                    continue

        elif maquina == '2':

            # Dados da maquina
            nome = str(input("Nome da máquina: "))
            nuclosFisicos = p.cpu_count(logical = False)
            nuclosLogicos = p.cpu_count(logical = True)
            capacidadeDeDisco = p.disk_usage('/').total
            ramTotal = p.virtual_memory().total

            ramFormatado = ramTotal /1000000000
            discoFormatado = capacidadeDeDisco / 1000000000

            # Verificacao do que foi inserido
            print("Dados: ", nome, nuclosFisicos, nuclosLogicos, round(discoFormatado, 1), round(ramFormatado, 1))

            comando_sql = "INSERT INTO maquina (nome, nucleosFisicos, nucleosLogicos, capacidadeTotal, ramTotal, dtCadastro) VALUE (%s, %s, %s, %s, %s, NOW())"

            valores = [
                (nome, nuclosFisicos, nuclosLogicos, round(discoFormatado, 1), math.floor(ramFormatado))
            ]

            cursor.executemany(comando_sql, valores)
            db.commit()

            print(cursor.rowcount, "Os dados da maquina foram cadastrados!")
            print("\nFaça login!\n")

            menu()

        elif maquina == '3':
            print("Até a próxima!")
            break

        else:
            print("Opção Inválida!")
            continue

menu()



