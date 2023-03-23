import sys
import numpy as np
import os

# Host do Metasploitable 2
# host = '192.168.64.3'
    
class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 
    orange = '\033[38;5;214m'

def run_command(command : str):
    os.system(command)

def specific_scan(host):
    
    range = input("\nDigite o intervalo de portas (ex: 1-100, 800, 945): ")
    ports = range.split(',')
    for port in ports:
        if '-' in port:
            ports.remove(port)
            start, end = port.split('-')
            sequence = np.arange(int(start), int(end)+1)
            ports = (np.concatenate((ports, sequence))).astype(int)
            
    print(f"{COLORS.BOLD}{COLORS.OKBLUE}Portas selecionadas: {ports}{COLORS.ENDC}\n")

    for port in ports:
        print("\n------------------------------------------------------------------------------------------------")
        command = f"nmap -sV -p{port} {host}"
        print(f"{COLORS.BOLD}{COLORS.OKCYAN}|Porta {port}|{command}{COLORS.ENDC}")
        print(f"{COLORS.BOLD}{COLORS.OKGREEN}Comando sendo executado: {command}{COLORS.ENDC}")
        run_command(command)

def general_scan(host):

    well_known_ports = {
    20: 'File Transfer Protocol (FTP) - Data transfer over network',
    21: 'File Transfer Protocol (FTP) - Control commands over network',
    22: 'Secure Shell (SSH) - Secure remote login and file transfer',
    23: 'Telnet - Remote terminal connection',
    25: 'Simple Mail Transfer Protocol (SMTP) - Email routing over networks',
    53: 'Domain Name System (DNS) - Translates domain names to IP addresses',
    80: 'Hypertext Transfer Protocol (HTTP) - Web browsing and communication',
    110: 'Post Office Protocol version 3 (POP3) - Email retrieval from server',
    119: 'Network News Transfer Protocol (NNTP) - Reading and posting Usenet news articles',
    143: 'Internet Message Access Protocol (IMAP) - Email retrieval from server',
    443: 'Hypertext Transfer Protocol Secure (HTTPS) - Encrypted web browsing and communication'
    }

    for port, description in well_known_ports.items():
        print("\n------------------------------------------------------------------------------------------------")
        command = f"nmap -sV -p{port} {host}"
        print(f"{COLORS.BOLD}{COLORS.OKCYAN}|Porta {port}| {description}{COLORS.ENDC}")
        print(f"{COLORS.BOLD}{COLORS.OKGREEN}Comando sendo executado: {command}{COLORS.ENDC}")
        run_command(command)

def open_ports(host):
    # Mostra portas TCP e UDP abertas
    command = f"nmap -sV {host} | grep 'open'"
    run_command(command)

def check_vulnerabilities(host):
    # Verifica vulnerabilidades em portas abertas
    port = input("\nDigite a porta que deseja verificar a vulnerabilidade: ")
    command = f"nmap -sV -p{port} - -script vuln {host}"
    run_command(command)

def main():

    host = input("Digite o IP do host alvo: ")

    print(f'''{COLORS.BOLD}{COLORS.HEADER}\nQual tipo de scan você deseja realizar? 
          \n\n[1] Geral (Well Known Ports). 
          \n\n[2] Específico (Range personalizado).
          \n\n[3] Verificar vulnerabilidades de portas abertas.
          \n\n[4] Mostrar portas TCP e UDP abertas.
          \n{COLORS.ENDC}''')
    
    option = str(input("Digite a opção desejada: "))

    if option == '1':
        print(f"{COLORS.BOLD}Executando o scan geral.{COLORS.ENDC}")
        general_scan(host)
    
    elif option == '2':
        print(f"{COLORS.BOLD}Executando o scan específico.{COLORS.ENDC}")
        specific_scan(host)

    elif option == '3':
        print(f"{COLORS.BOLD}\nVerificando vulnerabilidades de portas abertas.{COLORS.ENDC}")
        check_vulnerabilities(host)

    elif option == '4':
        print(f"{COLORS.BOLD}\nMostrando portas TCP e UDP abertas.{COLORS.ENDC}")
        open_ports(host)

    else:
        print("Opção inválida.")
        sys.exit()

if __name__ == "__main__":
    main()