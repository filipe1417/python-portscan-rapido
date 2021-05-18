# Portscan simples e rápido
Um simples port scan onde só é verificado se a conexão com a porta de um host foi feita com sucesso ou não (sem analisar flags tcp). A ideia é otimizá-lo para que fique com uma boa performance. Para que o processo seja realizado de forma menos demorada, foi utilizada a biblioteca "multiprocessing" do python3, que permite que vários processos sejam executados independentemente.

Seu uso pode ser feito das seguintes formas:

  Ex1: ./portScan.py google.com.br 21,22,80,80
    Onde o primeiro argumento é o host - IP ou domínio - e o segundo as portas
    
  Ex2: ./portScan.py 192.168.1.10 80
  
  Ex3: python portScan.py google.com.br 21
