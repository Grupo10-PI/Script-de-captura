import psutil as p
from datetime import datetime
import time as t
import mysql.connector
# from dotenv import load_dotenv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="leo12345",
    database="python"
)

cursor = db.cursor()

print("\n=========================")
print("\n        BEM-VINDO")
print("\n=========================")

while True: 
    escolha = str(input("\nESCOLHA UM HARDWARE PARA ANALIZAR\n1- CPU, \n2- RAM, \n3- DISK, \n4- HISTORICO, \n5- SAIR\nDIGITE AQUI: "))

    if escolha.upper() == '1':
        escolha2 = str(input("\nANALISAR: (1- USO, 2- FREQUENCIA ou 3- CPUS 4- VOLTAR)"))
        if escolha2.upper() == '1':
                while True:
                    uso = p.cpu_percent(interval=0)
                    print("USO CPU: ")
                    print(uso, '%\n')

                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')
                    
                    comando_sql = "INSERT INTO processador (processador_uso, dt_captura) VALUE (%s, NOW())"
                    valores = [
                        (uso)
                    ]

                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print(cursor.rowcount, "Os dados foram inseridos")

                    print("\nO programa está rodando. Precione 'ctrl + c' para sair.")

                    t.sleep(5)

        elif escolha2.upper() == '2':
                while True:
                    print("\nFREQUENCIA CPU: ")
                    print(p.cpu_freq().current, 'Mhz\n')
                
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')

                    print("\nO programa está rodando. Precione 'ctrl + c' para sair.")
                            
                    t.sleep(5)

        elif escolha2.upper() == '3':
                while True:
                    print("TOTAL CPU's: ")
                    print(p.cpu_count(),'\n')
                            
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')
                                        
                    break

        elif escolha2 == '4':
             continue

    elif escolha.upper() == '2':
        escolha2 = str(input("\nANALISAR: (1- USO, 2- TOTAL 3- VOLTAR)"))
        if escolha2.upper() == '1':
            while True: 
                    uso = p.virtual_memory().percent
                    print("USO RAM: ")
                    print(uso, '%\n')
 
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')

                    comando_sql = "INSERT INTO ram (ram_uso, dt_captura) VALUE (%s, NOW())"
                    valores = [
                        (uso)
                    ]

                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print(cursor.rowcount, "Os dados foram inseridos")

                    print("\nO programa está rodando. Precione 'ctrl + c' para sair.")
                                        
                    t.sleep(5)

        elif escolha2.upper() == '2':
                while True:
                    print("TOTAL RAM: ")
                    print(p.virtual_memory().total, 'bytes\n')
                            
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')
                                        
                    break;  

        elif escolha2 == '3':
             continue 

    elif escolha.upper() == '3':
        escolha2 = str(input("\nANALISAR: (1- TOTAL ou 2- PERCENT ou 3-VOLTAR)")) 
        if escolha2.upper() == '1':
                while True:
                    print("TOTAL DISK: ")
                    print(p.disk_usage('/').total, 'bytes\n')
                            
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')

                    print("\nO programa está rodando. Precione 'ctrl + c' para sair.")
                                        
                    t.sleep(5)                                

        elif escolha2.upper() == '2':
                while True:
                    uso = p.disk_usage('/').percent
                    print("TOTAL DISK: ")
                    print(uso, '%\n')
                    
                    agora = datetime.now()
                    data_formatada = agora.strftime("%d/%m/%Y")
                    hora_atual = datetime.now().strftime("%H:%M:%S")
                    print("DATA E HORA DA CAPTURA: ")
                    print(data_formatada, hora_atual, '\n')

                    comando_sql = "INSERT INTO disco (disco_uso, dt_captura) VALUE (%s, NOW())"
                    valores = [
                        (uso)
                    ]

                    cursor.execute(comando_sql, valores)
                    db.commit()

                    print(cursor.rowcount, "Os dados foram inseridos")  

                    print("\nO programa está rodando. Precione 'ctrl + c' para sair.")             
                                        
                    t.sleep(5)

        elif escolha2 == '3':
             continue
        
    elif escolha == '4':
            cursor.execute("SELECT * FROM processador")
        
            resultados = cursor.fetchall()
            for resultado in resultados:
                print(resultado)

    elif escolha == '5':
        print("GOODBYE!")
        break

    else: 
        print("ERRO, OPCAO INVALIDA")
        continue
       
