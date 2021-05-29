# Portscan simples e rápido em python
  Um simples e rápido port scanner onde só é verificado se a conexão com a porta de um determinado host foi feita com sucesso ou não (sem analisar flags tcp). Para que o processo seja realizado de forma menos demorada, foi utilizada a biblioteca "multiprocessing" do python3, que permite que vários processos sejam executados independentemente. O código comentado e sua explicação poderão ser encontrados no site que está sendo construído.


## Como utilizar o script:

  Primeiramente, por ser um arquivo em python, pode ser iníciado de algumas formas: 
  python portScan.py [ARGS]
  ou 
  ./portScan.py [ARGS]  . Nesse último caso, deve-se conceder permissão de execução ao arquivo
  
  É possível acessar o menu de opções possíveis utilizando -h ou --help junto ao script, da seguinte forma:
  ./portScan.py -h ou ./portScan.py --help
  Obs: o mesmo vale para executar o script utilizando "python". Assim, será possível perceber a seguinte saída:
  
  ![Captura de tela de 2021-05-19 22-57-56](https://user-images.githubusercontent.com/62412445/118907347-bc43f280-b8f5-11eb-9a06-460cb3c288dc.png)
  
  A partir dessa saída, vemos que existe um valor que sempre deverá ser executado junto ao script, sendo ele o endereço IP ou domínio alvo.
  Além disso, existem 2 possibilidades para a execução do scan corretamente, utilizar -m ou --mainports junto ao IP/domínio, fará com que o scan seja feito nas 1000 principais portas (mais utilizadas). Mas também é possível especificar isso manualmente, utilizando a opção -p ou --ports. Lembrando que ao utilizar -p ou --ports, é necessário especificar quais serão as portas analisadas separadas por vírgula.
  
  ## Exemplos
  
  ### ./portScan.py -m site.com
  Scan das 1000 principais portas no site "site.com"
  
  ### ./portScan.py -m 192.168.0.12
  Scan das 1000 principais portas no IP "192.168.0.12"
  
  ### ./portScan.py -p 21,22,80 site.com
  Scan nas portas 21,22 e 80 no site "site.com"
  
  ### python portScan.py -p 80 192.168.0.12
  Scan na porta 80 no IP "192.168.0.12"
  
  ## Implementações futuras
  
  Analisar os serviços que estão sendo executados nas portas (banner grabbing)

  
  




