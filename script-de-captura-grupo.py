from datetime import datetime
import math
import time as t
import mysql.connector
import psutil as p

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="primeiromac", 
    database="grupo10"
)

cursor = db.cursor()

print("\n_______________________________________________________________")


def menuCaptura(id):
    while True:
        print("\n Menu de Captura e Análise")  

        selecao1 = str(input("\n\n Selecione o número respectivo a categoria que deseja analisar: \n1- CPU \n2- RAM \n3- Disco \n4- Rede \n5- Histórico de Dados \n6- Sair do Programa\n\nOpção: "))

        if selecao1 == '1':
            while True:

                uso_cpu = p.cpu_percent(interval=0)
                freq_cpu = int(p.cpu_freq().current)

                print("Uso da CPU: ", uso_cpu, "%")
                print("Frequência atual da CPU: ", freq_cpu, "Mhz\n\n")

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = agora.strftime("%H:%M:%S")
                print("Data e Hora da Captura: ")
                print(data_formatada, hora_atual, '\n')

                comando_sql = "INSERT INTO registro (fkMaquina, cpuPorcentagemUso, cpuFrequenciaAtual, dtRegistro) VALUES (%s, %s, %s, NOW())"
                valores = (id, uso_cpu, freq_cpu)
                cursor.execute(comando_sql, valores)
                db.commit()

                print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para interromper o funcionamento.\n\n")

                t.sleep(3)

        elif selecao1 == '2':
            while True:
                ram = p.virtual_memory()
                ram_percentual = ram.percent
                ram_usada_gb = int(ram.used / (1024**3))
                ram_disponivel_gb = int(ram.available / (1024**3))

                print("Uso da RAM: ", ram_percentual, "%")
                print("RAM em uso: ", round(ram.used / 1000000000, 1), "GB\n\n")

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = agora.strftime("%H:%M:%S")
                print("Data e Hora da Captura: ")
                print(data_formatada, hora_atual, '\n')

                comando_sql = "INSERT INTO registro (fkMaquina, ramDisponivel, ramUsada, ramPercentualUso, dtRegistro) VALUES (%s, %s, %s, %s, NOW())"
                valores = (id, ram_disponivel_gb, ram_usada_gb, ram_percentual)
                cursor.execute(comando_sql, valores)
                db.commit()

                print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para interromper o funcionamento.\n\n")

                t.sleep(3)

        elif selecao1 == '3':
            while True:

                disco = p.disk_usage('/')
                disco_percentual = disco.percent
                disco_usado_gb = int(disco.used / (1024**3))
                disco_livre_gb = int(disco.free / (1024**3))

                print("Uso do Disco: ", disco_percentual, "%")
                print("Espaço de Disco em uso: ", round(disco.used / 1000000000, 1), "GB\n\n")

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = agora.strftime("%H:%M:%S")
                print("Data e Hora da Captura: ")
                print(data_formatada, hora_atual, '\n')

                comando_sql = "INSERT INTO registro (fkMaquina, discoEspacoUsado, discoEspacoLivre, dtRegistro) VALUES (%s, %s, %s, NOW())"
                valores = (id, disco_usado_gb, disco_livre_gb)
                cursor.execute(comando_sql, valores)
                db.commit()

                t.sleep(3)

        elif selecao1 == '4':
            while True:

                rede = p.net_io_counters()
                download_bytes = rede.bytes_recv
                upload_bytes = rede.bytes_sent

                print("Bytes Enviados na Rede: ", round(upload_bytes / 1000000, 1), "MB")
                print("Bytes Recebidos na Rede: ", round(download_bytes / 1000000, 1), "MB\n\n")

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = agora.strftime("%H:%M:%S")
                print("Data e Hora da Captura: ")
                print(data_formatada, hora_atual, '\n')
    
                comando_sql = "INSERT INTO registro (fkMaquina, downloadRede, uploadRede, dtRegistro) VALUES (%s, %s, %s, NOW())"
                valores = (id, download_bytes, upload_bytes)
                cursor.execute(comando_sql, valores)
                db.commit()

                print("\nO Programa está em funcionamento. Pressione 'ctrl + c' para interromper o funcionamento.\n\n")
                t.sleep(3)

        elif selecao1 == '5':
            print(f"\nHistórico de Dados da Máquina (ID: {id})")

            cursor_dict = db.cursor(dictionary=True)

            comando_sql = """
                SELECT idRegistro, cpuPorcentagemUso, ramPercentualUso, discoEspacoUsado, downloadRede, uploadRede, dtRegistro 
                FROM registro 
                WHERE fkMaquina = %s 
                ORDER BY dtRegistro DESC 
                LIMIT 10
            """
            
            cursor_dict.execute(comando_sql, (id,))
            historico = cursor_dict.fetchall()

            if historico:
                print("\nÚltimos 10 registros da máquina:")
                for registro in historico:
                    data = registro['dtRegistro'].strftime("%d/%m/%Y %H:%M:%S") if registro['dtRegistro'] else "N/D"
                    
                    print(f"ID: {registro['idRegistro']} | CPU: {registro['cpuPorcentagemUso']}% | RAM: {registro['ramPercentualUso']}% | Disco: {registro['discoEspacoUsado']} GB | Download: {registro['downloadRede']} B | Upload: {registro['uploadRede']} B | Data: {data}")
            else:
                print("\nNenhum histórico encontrado para esta Máquina no Banco de Dados.")

            cursor_dict.close()
            
        elif selecao1 == '6':
            print("Saindo do Menu de Captura...")
            break
        else:
            print("Opção inválida!")


def menu():
    while True:
        print("\n Seja Bem-Vindo ao Programa de Captura de Dados de Hardware!")

        selecao2 = str(input("\n\n Selecione o número respectivo a categoria que deseja acessar: \n\n1- Entrar ao Programa \n2- Cadastrar Máquina ao Programa \n3- Sair do Programa\n\nOpção: "))
            
        if selecao2 == '1':
            while True:
                
                idMaquina = int(input("\nID da Máquina: "))
                nomeMaquina = str(input("Nome da Máquina: "))

                comando_sql = "SELECT nome FROM maquina WHERE id = %s"
                valores = (idMaquina,)  

                cursor.execute(comando_sql, valores)
                resultados = cursor.fetchone()

                if resultados is not None and resultados[0] == nomeMaquina:
                    print("\nAcesso Liberado! O Programa irá realizar a Consulta de Dados respectivos a sua Máquina.")
                    
                    menuCaptura(idMaquina)
                    return idMaquina
                else:
                    print("\nAcesso Negado! ID ou Nome da Máquina incorretos.\n")
                    break  

        elif selecao2 == '2':

            nome = str(input("Nome da máquina: "))
            nucleosFisicos = p.cpu_count(logical=False)
            nucleosLogicos = p.cpu_count(logical=True)
            capacidadeDisco = p.disk_usage('/').total
            ramTotal = p.virtual_memory().total

            capacidadeDiscoFormatado = capacidadeDisco / 1000000000
            ramTotalFormatada = ramTotal / 1000000000

            
            print(f"\n\nDados Capturados: \nNúcleos Físicos: {nucleosFisicos} \nNúcleos Lógicos: {nucleosLogicos} \nCapacidade de Disco Formatado: {round(capacidadeDiscoFormatado, 1)} GB \nCapacidade de RAM Total: {round(ramTotalFormatada, 1)} GB")

            comando_sql = "INSERT INTO maquina (nome, nucleosFisicos, nucleosLogicos, capacidadeTotal, ramTotal, dtCadastro) VALUES (%s, %s, %s, %s, %s, NOW())"
            valores = (nome, nucleosFisicos, nucleosLogicos, round(capacidadeDiscoFormatado, 1), round(ramTotalFormatada, 1))

            cursor.execute(comando_sql, valores)
            db.commit()

            print("\n\nOs Dados da Máquina foram Cadastrados!")
            print(f"ID da máquina cadastrada: {cursor.lastrowid}\n")
            print("Faça o login acessando a Opção 1!\n")

        elif selecao2 == '3':
            print("Até a Próxima!")
            break

        else:
            print("Opção Inválida!")

menu()


