import psutil as p
from datetime import datetime
import time as t
escolha = str(input("ESCOLHA UM HARDWARE PARA ANALIZAR(CPU, RAM ou DISK): "))


if escolha.upper() == 'CPU':
    escolha2 = str(input("ANALISAR: (USO, FREQUENCIA ou CPUS)"))
    if escolha2.upper() == 'USO':
            while True:
                print("USO CPU: ")
                print(p.cpu_percent(interval=0), '%\n')

                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
            
                t.sleep(5)

    elif escolha2.upper() == 'FREQUENCIA':
            while True:
                print("FREQUENCIA CPU: ")
                print(p.cpu_freq().current, 'Mhz\n')
            
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                        
                t.sleep(5)

    elif escolha2.upper() == 'CPUS':
            while True:
                print("FREQUENCIA CPU: ")
                print(p.cpu_freq().current, 'Mhz\n')
                        
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                                    
                t.sleep(5)

elif escolha.upper() == 'RAM':
    escolha2 = str(input("ANALISAR: (USO ou TOTAL)"))
    if escolha2.upper() == 'USO':
         while True: 
                print("USO RAM: ")
                print(p.virtual_memory().percent, '%\n')
                        
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                                    
                t.sleep(5)

    elif escolha2.upper() == 'TOTAL':
            while True:
                print("TOTAL RAM: ")
                print(p.virtual_memory().total, 'bytes\n')
                        
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                                    
                t.sleep(5)   

elif escolha.upper() == 'DISK':
    escolha2 = str(input("ANALISAR: (TOTAL ou PERCENT)")) 
    if escolha2.upper() == 'TOTAL':
            while True:
                print("TOTAL DISK: ")
                print(p.disk_usage().total, 'bytes\n')
                        
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                                    
                t.sleep(5)                                

    elif escolha2.upper() == 'TOTAL':
            while True:
                print("TOTAL DISK: ")
                print(p.disk_usage().percent, '%\n')
                        
                agora = datetime.now()
                data_formatada = agora.strftime("%d/%m/%Y")
                hora_atual = datetime.now().strftime("%H:%M:%S")
                print("DATA E HORA DA CAPTURA: ")
                print(data_formatada, hora_atual, '\n')
                                    
                t.sleep(5)

else: 
     print("ERRO, OPCAO INVALIDA")
     print("ENCERRANDO...")