Projeto criado para receber 20 valores em forma de segundos de atletas que participaram da última corrida. Separar os dados em :
* Melhor tempo | Pior tempo
* Diferença entre o Melhor tempo e Pior tempo
* Tempo médio
* Quantidade de atletas acima da media e abaixo
* Número da camisa do melhor atleta
* Classificar em grupos de Elite, Regular e Iniciante 

A variável  ```tempo = [] ``` foi criada em forma de array sem valor presente. Para que possa receber os valores posteriormente.

O loop ``` for i in range(20):
    tempo = float(input(f"Digite o tempo do atleta {i+1} (em segundos): "))
    tempos.append(tempo) ```
Foi criada para receber os 20 valores; 

Existe uma variável dentro do loop : ``` tempo = float(input(f"Digite o tempo do atleta {i+1} (em segundos): ")) ```
Que é utilizada para receber os valores e armazenar;

Em : ``` tempos.append(tempo) ```, serve para adicionar valores na array;
