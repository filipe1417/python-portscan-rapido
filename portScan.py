#!/usr/bin/python3

import sys, socket, multiprocessing, argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m","--mainports", help="Realiza um scan nas 100 principais portas", action="store_true")
group.add_argument("-p","--ports", help="Especifique as portas, separando por virgula")
parser.add_argument("ip",help="Digite o endereço ip ou domínio")
args = parser.parse_args()
#criação dos argumentos para utilização do script 

def portScan(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host,int(porta))) == 0:
        print("Porta " + porta + " aberta")
#definição da função que realiza a validação nas portas

def multiProcess(host, portScan, p):
        l = multiprocessing.Process(target=portScan, args=(host,str(p)))
        l.start()
#definição da função de multiprocessing

if __name__ == "__main__":
    def main():
        try:
            host = socket.gethostbyname(args.ip)
        except socket.gaierror:
            print("Host inválido, tente novamente")
            sys.exit(1)

        if args.mainports:
            portas = [7,9,13,21,22,23,25,26,37,53,79,80,81,88,106,110,111,113,119,135,139,143,144,179,199,389,427,443,444,445,465,513,514,515,543,544,548,554,587,631,646,873,990,993,995,1025,1026,1027,1028,1029,1110,1433,1720,1723,1755,1900,2000,2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000,6001,6646,7070,8000,8008,8009,8080,8081,8443,8888,9100,9999,10000,32768,49152,49157]
            for p in portas:
                multiProcess(host, portScan, p)

        else:
            portas = args.ports
            
            for p in portas.split(","):
                multiProcess(host, portScan, p)
    #definição da função main

    main()
    #execução da função main