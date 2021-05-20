# Portscan simples e rápido em python
  Um simples port scan onde só é verificado se a conexão com a porta de um host foi feita com sucesso ou não (sem analisar flags tcp). A ideia é otimizá-lo para que fique com uma boa performance. Para que o processo seja realizado de forma menos demorada, foi utilizada a biblioteca "multiprocessing" do python3, que permite que vários processos sejam executados independentemente. O código comentado e sua explicação poderão ser encontrados no site que está sendo construído.


## Como utilizar o script:
  Primeiramente, por ser um arquivo em python, pode ser iníciado de algumas formas: 
  python portScan.py [ARGS]
  ou 
  ./portScan.py [ARGS]  Nesse caso, deve-se conceder permissão de execução ao arquivo
  
  É possível acessar o menu de opções possíveis utilizando -h ou --help junto ao script, da seguinte forma:
  ./portScan.py -h ou ./portScan.py --help
  Obs: o mesmo vale para executar o script utilizando "python"
  Assim, será possível perceber a seguinte saída:
  ![Captura de tela de 2021-05-19 22-57-56](https://user-images.githubusercontent.com/62412445/118907347-bc43f280-b8f5-11eb-9a06-460cb3c288dc.png)


  
  




