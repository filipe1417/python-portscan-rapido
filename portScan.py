#!/usr/bin/python3

import sys, socket, multiprocessing
#importação das bibliotecas utilizadas

host = socket.gethostbyname(sys.argv[1])
#armazenamento do endereço IPV4 do host na variável "host". A função "gethostbyname()" garante->
#-> que mesmo o usuário passando um nome de domínio, o valor armazenado será o endereço IP.

portas = sys.argv[2]
#aqui são armazenadas as portas escolhidas pelo usuário.

def portScan(host,porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((host,int(porta))) == 0:
        print("Porta " + porta + " aberta")
#criação da função que define o port scan. "int(p)" garante que o valor da porta seja passada para inteiro e possa funcionar corretamente dentro da função ->
#-> "connect_ex()" 

if __name__ == '__main__':
    jobs = []
    for p in portas.split(","):
        l = multiprocessing.Process(target=portScan, args=(host,p))
        l.start()
#caso o usuário digite mais de uma porta, separando por vírgula, o "split(",")" vai garantir -> 
#-> que a string seja transformada em valores distintos

