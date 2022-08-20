#!/usr/bin/python3

import sys, socket, multiprocessing, argparse
from constantes import PORTAS_PRINCIPAIS



def port_scan(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host,int(porta))) == 0:
        print(f"Porta {porta} aberta")


def multi_process(host, port_scan, porta):
        l = multiprocessing.Process(target=port_scan, args=(host,str(porta)))
        l.start()


def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-m","--mainports", help="Realiza um scan nas 1000 principais portas tcp", action="store_true")
    group.add_argument("-p","--ports", help="Especifique as portas, separando por virgula ou hífen")
    parser.add_argument("ip",help="Digite o endereço ip ou domínio")
    args = parser.parse_args()

    try:
        host = socket.gethostbyname(args.ip)
    except socket.gaierror:
        print("Host inválido, tente novamente")
        sys.exit(1)

    if args.mainports:
        portas = PORTAS_PRINCIPAIS
        for p in portas:
            multi_process(host, port_scan, p)
    elif args.ports:
        portas = args.ports
        for p in portas.split(","):
            multi_process(host, port_scan, p)
    else:
        print("ERRO: cheque se os argumentos estão corretos")
        sys.exit(1)


if __name__ == "__main__":
    main()
