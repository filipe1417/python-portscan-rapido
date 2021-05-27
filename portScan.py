#!/usr/bin/python3

import sys, socket, multiprocessing, argparse
from constantes import portasPrincipais

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m","--mainports", help="Realiza um scan nas 1000 principais portas tcp", action="store_true")
group.add_argument("-p","--ports", help="Especifique as portas, separando por virgula ou hífen")
parser.add_argument("ip",help="Digite o endereço ip ou domínio")
args = parser.parse_args()

def portScan(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host,int(porta))) == 0:
        print("Porta " + porta + " aberta")

def multiProcess(host, portScan, p):
        l = multiprocessing.Process(target=portScan, args=(host,str(p)))
        l.start()

def main():
    try:
        host = socket.gethostbyname(args.ip)
    except socket.gaierror:
        print("Host inválido, tente novamente")
        sys.exit(1)

    if args.mainports:
        portas = portasPrincipais
        for p in portas:
            multiProcess(host, portScan, p)

    else:
        portas = args.ports
        for p in portas.split(","):
            multiProcess(host, portScan, p)
            
if __name__ == "__main__":
    main()